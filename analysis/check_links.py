#!/usr/bin/env python3
"""
Check HTTP reachability of all URLs registered in sources/sources.md.
Uses standard HTTP HEAD (with lightweight Range GET fallback when servers reject HEAD)
without bypassing any bot-challenge or paywall protections.

Generates:
  - analysis/outputs/link_status.json
"""

import argparse
import json
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "analysis" / "outputs"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"


def check_single_url(url: str, timeout: int = 5):
    if not url or not url.startswith("http"):
        return {"url": url, "http_code": 0, "status": "no_http_url"}
    try:
        cmd = [
            "curl", "-sI", "-L",
            "--max-time", str(timeout),
            "-A", USER_AGENT,
            "-o", "/dev/null",
            "-w", "%{http_code}",
            url,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 2)
        code_str = res.stdout.strip()[-3:] if res.stdout.strip() else "000"
        code = int(code_str) if code_str.isdigit() else 0

        if code in (0, 400, 403, 405):
            cmd_get = [
                "curl", "-s", "-L",
                "-r", "0-512",
                "--max-time", str(timeout),
                "-A", USER_AGENT,
                "-o", "/dev/null",
                "-w", "%{http_code}",
                url,
            ]
            res2 = subprocess.run(cmd_get, capture_output=True, text=True, timeout=timeout + 2)
            code_str2 = res2.stdout.strip()[-3:] if res2.stdout.strip() else "000"
            code2 = int(code_str2) if code_str2.isdigit() else 0
            if code2 > 0:
                code = code2
    except Exception:
        code = 0

    if 200 <= code < 300:
        status = "200_ok"
    elif 300 <= code < 400:
        status = "3xx_redirect"
    elif code in (403, 429, 503):
        status = "403_429_503_restricted_or_challenge"
    elif code in (404, 410):
        status = "404_410_not_found"
    elif code == 0:
        status = "timeout_or_connection_error"
    else:
        status = f"http_{code}"

    return {"url": url, "http_code": code, "status": status}


def check_links(skip_network: bool = False):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    reg_path = OUT_DIR / "sources_register.json"
    if not reg_path.exists():
        import inventory
        inventory.build_inventory()

    with open(reg_path, "r", encoding="utf-8") as f:
        sources_dict = json.load(f)

    sources = list(sources_dict.values()) if isinstance(sources_dict, dict) else sources_dict
    unique_urls = sorted({
        s.get("primary_url", "")
        for s in sources
        if s.get("primary_url", "").startswith("http")
    })
    url_results = {}

    if skip_network:
        for u in unique_urls:
            url_results[u] = {"url": u, "http_code": None, "status": "skipped_network_check"}
    else:
        print(f"[check_links] Checking {len(unique_urls)} unique URLs across {len(sources)} source entries...")
        with ThreadPoolExecutor(max_workers=32) as ex:
            future_to_url = {ex.submit(check_single_url, u): u for u in unique_urls}
            for fut in as_completed(future_to_url):
                u = future_to_url[fut]
                url_results[u] = fut.result()

    entries_status = []
    status_counter = Counter()
    for s in sources:
        u = s.get("primary_url", "")
        res = url_results.get(u, {"url": u, "http_code": 0, "status": "no_http_url"})
        status_counter[res["status"]] += 1
        entries_status.append({
            "id": s["id"],
            "title": s["title"],
            "url": u,
            "tier": s["tier"],
            "is_opened_in_repo": s["is_opened"],
            "accessed_in_sources_md": s["accessed"],
            "http_code": res["http_code"],
            "live_check_status": res["status"],
        })

    output = {
        "total_source_entries": len(sources),
        "unique_urls_checked": len(unique_urls),
        "skip_network": skip_network,
        "status_counts_by_source_entry": dict(status_counter),
        "status_counts_by_unique_url": dict(Counter(r["status"] for r in url_results.values())),
        "entries": entries_status,
    }

    out_path = OUT_DIR / "link_status.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[check_links] Wrote {out_path} — summary: {dict(status_counter)}")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check HTTP status of URLs in sources/sources.md")
    parser.add_argument("--skip-network", action="store_true", help="Skip live HTTP network checks")
    args = parser.parse_args()
    check_links(skip_network=args.skip_network)
