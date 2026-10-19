#!/usr/bin/env python3
"""
Verify Deliverable 1 (reports/2026-10-18-corsa-jakarta-insights-report.md),
generate the Claim Ledger (data/processed/2026-10-18-claim-ledger.csv),
and generate/validate Deliverable 2 (reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md).

Can be run both before Deliverable 1 exists (dry-run / readiness check) and after Deliverable 1 is written.
"""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "analysis" / "outputs"
REPORT_PATH = ROOT / "reports" / "2026-10-18-corsa-jakarta-insights-report.md"
APPENDIX_PATH = ROOT / "reports" / "2026-10-18-corsa-jakarta-insights-sources-appendix.md"
LEDGER_PATH = ROOT / "data" / "processed" / "2026-10-18-claim-ledger.csv"
PREVERIFY_PATH = ROOT / "data" / "processed" / "2026-10-18-preverification.csv"

FORBIDDEN_STRINGS = [
    "Bergmann",
    "Heiko",
    "Rflect",
    "HSG staff",
    "course credit",
    "grading",
]

MODEL_CITATION_PATTERN = re.compile(
    r"(?:model\s+v0\.6\s*:|[A-Za-z_0-9 ()]+![A-Z]{1,2}\d+|\b(?:Inputs|Dashboard|Scenarios|PnL_Monthly|Annual|Rent_Data|Location|Menu|Revenue|Staffing|OPEX|CAPEX \(Buy\)|CAPEX \(Rent\)|Funding|Sensitivity|MonteCarlo|Sources|Research_Tracker|Cover|ReadMe)![A-Z]{1,2}\d+|(?<![A-Za-z0-9_-])(?:S\d{2,3}|R\d{2})(?![A-Za-z0-9_-]))",
    re.IGNORECASE,
)
TEAM_CITATION_PATTERN = re.compile(
    r"(?:team\s*:|PESTEL_Analysis_Updated|CAGE Analysis - Indonesian F&B|2026-10-16-project-scope-summary)",
    re.IGNORECASE,
)
LABEL_PATTERN = re.compile(r"(?:\bAnalysis\s*:|\bAssumption\s*:|\*\*Analysis:\*\*|\*\*Assumption:\*\*)", re.IGNORECASE)


def norm_url(u: str) -> str:
    if not u:
        return ""
    u = u.strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    u = u.rstrip("/")
    return u


def load_json(path: Path, default=None):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def load_csv(path: Path):
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_words(text: str):
    raw_words = len(text.split())
    prose_lines = []
    for line in text.splitlines():
        s = line.strip()
        if re.match(r"^\|[\s\-:|]+\|$", s):
            continue
        s = s.replace("|", " ")
        prose_lines.append(s)
    prose_text = "\n".join(prose_lines)
    prose_text_no_cites = re.sub(r"\([^()]*?(?:model v0\.6|team:|![A-Z]|DISC-|CAGE-|P1|P2|P3|P4|PV-)[^()]*?\)", "", prose_text)
    prose_words = len(prose_text_no_cites.split())
    return raw_words, prose_words


def check_forbidden_strings(text: str, file_label: str):
    hits = []
    for term in FORBIDDEN_STRINGS:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        for line_no, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                hits.append({"file": file_label, "line": line_no, "term": term, "snippet": line.strip()[:120]})
    return hits


def build_dynamic_id_matcher(sources_reg: dict, row_index: dict):
    """Build regex matching any row_id in row_index, any source_id in sources_reg, CAGE claim IDs, or PV-xxx."""
    known_ids = set(row_index.keys()) | set(sources_reg.keys())

    # Add CAGE claim register IDs
    cage_report = ROOT / "reports" / "2026-10-17-cage-switzerland-jakarta.md"
    cage_claim_to_src = defaultdict(set)
    url_to_src_ids = defaultdict(set)
    for sid, s in sources_reg.items():
        for u in s.get("all_urls", []):
            nu = norm_url(u)
            if nu:
                url_to_src_ids[nu].add(sid)

    if cage_report.exists():
        with open(cage_report, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^\|\s*([A-Z0-9]+-\d+)\s*\|", line)
                if m:
                    cid = m.group(1)
                    known_ids.add(cid)
                    for sid in sources_reg:
                        if sid in line:
                            cage_claim_to_src[cid].add(sid)
                    for u_match in re.findall(r"https?://[^\s,;)\"|]+", line):
                        nu = norm_url(u_match)
                        if nu in url_to_src_ids:
                            cage_claim_to_src[cid].update(url_to_src_ids[nu])

    # Sort longest first to avoid partial prefix matches
    escaped = [re.escape(k) for k in sorted(known_ids, key=len, reverse=True) if len(k) >= 3]
    escaped.append(r"PV-\d{2,3}")
    escaped.append(r"DISC-A\d{1,2}")
    pattern = re.compile(r"\b(?:" + "|".join(escaped) + r")\b")
    return pattern, cage_claim_to_src, url_to_src_ids


def parse_report_and_generate_artifacts():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sources_reg = load_json(OUT_DIR / "sources_register.json", {})
    row_index = load_json(OUT_DIR / "row_index.json", {})
    blocked_data = load_json(OUT_DIR / "blocked_rows.json", {})
    unused_reasons_override = load_json(OUT_DIR / "unused_source_reasons.json", {})
    preverify_rows = load_csv(PREVERIFY_PATH)
    preverify_by_item = {r["item_id"]: r for r in preverify_rows}
    preverify_by_row_id = defaultdict(list)
    for r in preverify_rows:
        for row_id in row_index:
            if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(row_id)}(?![A-Za-z0-9_-])", r.get("origin", "")):
                preverify_by_row_id[row_id].append(r)

    id_pattern, cage_claim_to_src, url_to_src_ids = build_dynamic_id_matcher(sources_reg, row_index)

    if not REPORT_PATH.exists():
        summary = {
            "report_exists": False,
            "report_path": str(REPORT_PATH.relative_to(ROOT)),
            "status": "awaiting_deliverable_1",
            "message": "Deliverable 1 not yet created. Run verify_report.py again after writing reports/2026-10-18-corsa-jakarta-insights-report.md.",
        }
        with open(OUT_DIR / "verify_report_summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print("[verify_report] Deliverable 1 not yet present; wrote awaiting_deliverable_1 status.")
        return summary

    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report_text = f.read()

    raw_words, prose_words = count_words(report_text)
    forbidden_hits = check_forbidden_strings(report_text, "reports/2026-10-18-corsa-jakarta-insights-report.md")

    current_section = "Header / Title"
    claims = []
    unsourced_statements = []
    if_used_citations = []
    disallowed_preverification_fact_citations = []
    cited_row_ids_by_section = defaultdict(set)
    cited_src_ids_by_section = defaultdict(set)
    cited_model_sheets = set()
    cited_team_files = set()

    claim_counter = 0
    lines_all = report_text.splitlines()

    for line_no, raw_line in enumerate(lines_all, 1):
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("#"):
            current_section = line.lstrip("#").strip()
            continue

        if re.match(r"^[-*_]{3,}$", line) or re.match(r"^\|[\s\-:|]+\|$", line):
            continue

        if line.startswith("|") and line_no < len(lines_all):
            next_l = lines_all[line_no].strip()
            if re.match(r"^\|[\s\-:|]+\|$", next_l):
                continue

        matched_tokens = id_pattern.findall(line)
        rids = [t for t in matched_tokens if t in row_index or t.startswith("PV-") or t in cage_claim_to_src]
        sids = set(t for t in matched_tokens if t in sources_reg)

        mcites = MODEL_CITATION_PATTERN.findall(line)
        tcites = TEAM_CITATION_PATTERN.findall(line)
        has_label = bool(LABEL_PATTERN.search(line))
        pv_rows = []
        for item_id, pv in preverify_by_item.items():
            if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(item_id)}(?![A-Za-z0-9_-])", line):
                pv_rows.append(pv)
            if pv.get("check") == "if_used":
                for source_id in re.findall(r"\bS\d{2,3}\b", pv.get("origin", "")):
                    if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(source_id)}(?![A-Za-z0-9_-])", line):
                        pv_rows.append(pv)
        for rid in rids:
            pv_rows.extend(preverify_by_row_id.get(rid, []))
        pv_rows = list({r["item_id"]: r for r in pv_rows}.values())

        for u_match in re.findall(r"https?://[^\s,;)\"|]+", line):
            nu = norm_url(u_match)
            if nu in url_to_src_ids:
                sids.update(url_to_src_ids[nu])

        for rid in rids:
            cited_row_ids_by_section[current_section].add(rid)
            if rid in row_index:
                for reg_id in row_index[rid].get("register_ids", []):
                    if reg_id in sources_reg:
                        sids.add(reg_id)
            if rid in cage_claim_to_src:
                sids.update(cage_claim_to_src[rid])

        for sid in sids:
            cited_src_ids_by_section[current_section].add(sid)

        for mc in mcites:
            for sh in [
                "Cover", "ReadMe", "Dashboard", "Inputs", "Rent_Data", "Location",
                "Menu", "Revenue", "Staffing", "OPEX", "CAPEX (Buy)", "CAPEX (Rent)",
                "Funding", "PnL_Monthly", "Annual", "Scenarios", "Sensitivity",
                "MonteCarlo", "Sources", "Research_Tracker"
            ]:
                if sh.lower() in mc.lower():
                    cited_model_sheets.add(sh)

        for tc in tcites:
            if "pestel" in tc.lower():
                cited_team_files.add("research/internal/phase-1/PESTEL_Analysis_Updated (2).pdf")
            if "cage" in tc.lower():
                cited_team_files.add("research/internal/phase-1/CAGE Analysis - Indonesian F&B Market Entry for CORSA.pdf")
            if "scope" in tc.lower() or "team:" in tc.lower():
                cited_team_files.add("docs/scope/2026-10-16-project-scope-summary.md")

        has_citation = bool(rids or mcites or tcites or sids or has_label)
        has_numbers = bool(re.search(r"\b\d+(?:[.,]\d+)?%|\bRp\s*\d|\bCHF\s*\d|\b\d{1,3}(?:,\d{3})+\b", line))

        if not has_citation and has_numbers:
            unsourced_statements.append({
                "line": line_no,
                "section": current_section,
                "text": line[:200],
            })

        if has_citation or has_numbers:
            claim_counter += 1
            cid = f"CLM-{claim_counter:04d}"

            all_src_ids = []
            for rid in dict.fromkeys(rids):
                all_src_ids.append(rid)
            for sid in sorted(sids):
                if sid not in all_src_ids:
                    all_src_ids.append(sid)
            for mc in dict.fromkeys(mcites):
                all_src_ids.append(mc.strip())
            for tc in dict.fromkeys(tcites):
                all_src_ids.append(tc.strip())

            if re.search(r"\bAssumption\s*:|\*\*Assumption:\*\*", line, re.IGNORECASE):
                c_type = "assumption"
            elif re.search(r"\bAnalysis\s*:|\*\*Analysis:\*\*", line, re.IGNORECASE):
                c_type = "analysis"
            else:
                c_type = "fact"

            for pv in pv_rows:
                if pv.get("check") == "if_used":
                    if_used_citations.append({"line": line_no, "item_id": pv["item_id"], "text": line[:200]})
                if pv.get("verdict") in {"NOT-CONFIRMED", "UNREACHABLE"}:
                    disallowed_preverification_fact_citations.append(
                        {"line": line_no, "item_id": pv["item_id"], "verdict": pv["verdict"], "text": line[:200]}
                    )

            if rids or sids:
                v_by = "source_text"
            elif mcites:
                v_by = "model_cell"
            elif has_label:
                v_by = "script_calc"
            else:
                v_by = "manual_check"

            ev_level = "high"
            if c_type == "assumption":
                ev_level = "low"
            elif c_type == "analysis":
                ev_level = "medium"
            elif rids:
                tiers = [row_index[r].get("primary_tier") for r in rids if r in row_index and row_index[r].get("primary_tier")]
                if tiers and min(tiers) >= 3:
                    ev_level = "medium"
            elif not all_src_ids:
                ev_level = "unknown"

            pv_item_ids = list(dict.fromkeys(r["item_id"] for r in pv_rows))
            row_labels = list(dict.fromkeys(
                row_index[r].get("verification", "") for r in rids if r in row_index and row_index[r].get("verification")
            ))
            if pv_item_ids:
                verification = ";".join(pv_item_ids)
            elif row_labels:
                verification = ";".join(row_labels)
            elif mcites:
                verification = "model_v0.6_cell"
            elif sids or tcites:
                verification = "source_register"
            elif has_label:
                verification = "labelled_analysis"
            else:
                verification = "unverified"

            if mcites:
                depends_on = "model_v0.6"
            elif tcites:
                depends_on = "team_unverified"
            else:
                depends_on = "none"

            pv_checkers = list(dict.fromkeys(r.get("checked_by", "") for r in pv_rows if r.get("checked_by")))
            if pv_checkers:
                v_by = ";".join(pv_checkers)

            clean_claim = re.sub(r"\s+", " ", line.strip("| ").strip())
            if len(clean_claim) > 280:
                clean_claim = clean_claim[:277] + "..."

            claims.append({
                "claim_id": cid,
                "section": current_section[:80],
                "claim": clean_claim,
                "source_ids": "; ".join(dict.fromkeys(all_src_ids)) if all_src_ids else ("Analysis/Assumption label" if has_label else "MISSING"),
                "evidence_level": ev_level,
                "type": c_type,
                "depends_on": depends_on,
                "verification": verification,
                "verified_by": v_by,
            })

    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "claim_id", "section", "claim", "source_ids",
        "evidence_level", "type", "depends_on", "verification", "verified_by"
    ]
    with open(LEDGER_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(claims)

    used_src_ids = set()
    src_id_to_sections = defaultdict(set)
    src_id_to_rowids = defaultdict(set)

    for sec, rids in cited_row_ids_by_section.items():
        for rid in rids:
            if rid in row_index:
                for reg_id in row_index[rid].get("register_ids", []):
                    if reg_id in sources_reg:
                        used_src_ids.add(reg_id)
                        src_id_to_sections[reg_id].add(sec)
                        src_id_to_rowids[reg_id].add(rid)
            if rid in cage_claim_to_src:
                for reg_id in cage_claim_to_src[rid]:
                    used_src_ids.add(reg_id)
                    src_id_to_sections[reg_id].add(sec)
                    src_id_to_rowids[reg_id].add(rid)

    for sec, sids in cited_src_ids_by_section.items():
        for sid in sids:
            used_src_ids.add(sid)
            src_id_to_sections[sid].add(sec)

    generate_sources_appendix(
        sources_reg=sources_reg,
        used_src_ids=used_src_ids,
        src_id_to_sections=src_id_to_sections,
        src_id_to_rowids=src_id_to_rowids,
        cited_model_sheets=cited_model_sheets,
        cited_team_files=cited_team_files,
        blocked_data=blocked_data,
        unused_reasons_override=unused_reasons_override,
        claims=claims,
    )

    appendix_forbidden = []
    if APPENDIX_PATH.exists():
        with open(APPENDIX_PATH, "r", encoding="utf-8") as f:
            appendix_forbidden = check_forbidden_strings(f.read(), "reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md")

    summary = {
        "report_exists": True,
        "report_path": str(REPORT_PATH.relative_to(ROOT)),
        "appendix_path": str(APPENDIX_PATH.relative_to(ROOT)),
        "claim_ledger_path": str(LEDGER_PATH.relative_to(ROOT)),
        "word_counts": {
            "raw_words": raw_words,
            "prose_words": prose_words,
            "ceiling": 10000,
            "raw_under_ceiling": raw_words <= 10000,
            "prose_under_ceiling": prose_words <= 10000,
        },
        "claims_logged": len(claims),
        "unsourced_numeric_statements_count": len(unsourced_statements),
        "unsourced_numeric_statements": unsourced_statements[:25],
        "if_used_citations": if_used_citations,
        "disallowed_preverification_fact_citations": disallowed_preverification_fact_citations,
        "forbidden_string_hits_report": forbidden_hits,
        "forbidden_string_hits_appendix": appendix_forbidden,
        "sources_used_count": len(used_src_ids),
        "sources_unused_count": len(sources_reg) - len(used_src_ids),
        "distinct_row_ids_cited": len({r for s in cited_row_ids_by_section.values() for r in s}),
        "model_sheets_cited": sorted(cited_model_sheets),
    }

    with open(OUT_DIR / "verify_report_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(
        f"[verify_report] Verified Deliverable 1: raw_words={raw_words}, prose_words={prose_words}, "
        f"claims={len(claims)}, unsourced={len(unsourced_statements)}, "
        f"forbidden_hits={len(forbidden_hits) + len(appendix_forbidden)}, "
        f"sources_used={len(used_src_ids)}/{len(sources_reg)}"
    )
    return summary


PART_B_CODES = {
    "BLOCKED": "The source could not be opened (bot challenge, 403, page gone), so it could not be verified",
    "NOT-CONFIRMED": "Pre-verification opened the source, but it does not support the claim (value, period, base or wording differ)",
    "OUT-OF-WINDOW": "Before the 2024-10-16 cutoff, or superseded",
    "DUPLICATE": "The same fact comes from a stronger source",
    "TIER4-LEAD": "Lead only",
    "CONTRADICTED": "A stronger source conflicts",
    "OFF-SCOPE": "Not needed for the report's questions (names the question it served)",
    "CONDENSED-OUT": "Relevant but cut for length (names the long report that still holds it)",
    "UNVERIFIED-NOT-USED": "Pre-verification item (check=if_used) with no verdict and not cited in the report",
}
REASON_OVERRIDES_PATH = ROOT / "analysis" / "appendix_reason_overrides.json"
WINDOW_START = (2024, 10, 16)
NON_TARGET_CITY_RE = re.compile(r"\b(Bogor|Bekasi|Depok|Tangerang|Surabaya|Bali|Bandung)\b")
ACCESS_FAIL_RE = re.compile(r"\b(not opened|snippet-only|blocked|unreachable|timeout)\b", re.IGNORECASE)
HTTP_FAIL_RE = re.compile(r"\b(403|404)\b")


def _esc(text) -> str:
    return re.sub(r"\s+", " ", str(text or "")).replace("|", "\\|").strip()


def _trunc_words(text, n=25) -> str:
    words = re.sub(r"\s+", " ", str(text or "")).split()
    return " ".join(words[:n]) + (" ..." if len(words) > n else "")


def _first_clause(text, n=18) -> str:
    t = re.sub(r"\s+", " ", str(text or "")).strip()
    t = re.split(r"(?<=[.;])\s", t)[0].rstrip(".;")
    return _trunc_words(t, n)


def _load_overrides(legacy: dict) -> dict:
    """Merge legacy {id: reason} overrides with analysis/appendix_reason_overrides.json ({id: {code, reason}})."""
    merged = {}
    for k, v in (legacy or {}).items():
        merged[k] = v
    for k, v in (load_json(REASON_OVERRIDES_PATH, {}) or {}).items():
        if not k.startswith("_"):
            merged[k] = v
    return merged


def _override_pair(ov):
    if isinstance(ov, dict):
        return ov["code"], ov["reason"]
    m = re.match(r"^([A-Z0-9-]+):\s*(.*)$", str(ov))
    if m and m.group(1) in PART_B_CODES:
        return m.group(1), m.group(2)
    return "CONDENSED-OUT", str(ov)


def _published_before_window(published: str) -> bool:
    m = re.match(r"^\s*(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", published or "")
    if not m:
        return False
    y = int(m.group(1))
    mo = int(m.group(2)) if m.group(2) else None
    d = int(m.group(3)) if m.group(3) else None
    if mo is None:
        return y < WINDOW_START[0]
    if d is None:
        return (y, mo) < WINDOW_START[:2]
    return (y, mo, d) < WINDOW_START


def build_reference_index(sources_reg: dict):
    """Map source id -> (long reports 2026-10-17-*.md citing it, data/processed CSVs holding it)."""
    ids = sorted(sources_reg, key=len, reverse=True)
    if not ids:
        return {}, {}
    pat = re.compile(r"(?<![A-Za-z0-9_-])(" + "|".join(re.escape(i) for i in ids) + r")(?![A-Za-z0-9_-])")
    in_reports, in_csvs = defaultdict(set), defaultdict(set)
    for p in sorted((ROOT / "reports").glob("2026-10-17-*.md")):
        for sid in set(pat.findall(p.read_text(encoding="utf-8"))):
            in_reports[sid].add(p.name)
    for p in sorted((ROOT / "data" / "processed").rglob("*.csv")):
        if p.name in {"2026-10-18-claim-ledger.csv", "2026-10-18-preverification.csv"}:
            continue
        for sid in set(pat.findall(p.read_text(encoding="utf-8"))):
            in_csvs[sid].add(p.name)
    return in_reports, in_csvs


def classify_unused_source_reason(s: dict, unused_reasons_override: dict, in_reports=None, in_csvs=None):
    """Return (code, one-line reason) for a register entry not cited in the report."""
    sid = s["id"]
    if sid in unused_reasons_override:
        return _override_pair(unused_reasons_override[sid])

    acc = s.get("accessed") or ""
    used_for = s.get("used_for") or ""
    title = s.get("title") or ""

    if (not s.get("is_opened", True)) or ACCESS_FAIL_RE.search(acc) or (HTTP_FAIL_RE.search(acc) and not re.search(r"\bopened\b", acc, re.IGNORECASE)):
        return "BLOCKED", f"Not opened in full ({_trunc_words(re.sub(r'^\\d{4}-\\d{2}-\\d{2};\\s*', '', acc), 14)}); could not be verified."
    if _published_before_window(s.get("published", "")):
        return "OUT-OF-WINDOW", f"Published {_trunc_words(s.get('published'), 6)}, before the 2024-10-16 cutoff."
    if s.get("tier") == 4:
        return "TIER4-LEAD", "Tier 4 source in the register; lead only, never the sole basis for a figure."
    m = NON_TARGET_CITY_RE.search(title)
    if m:
        return "OFF-SCOPE", f"Title names {m.group(1)}, outside the Jakarta Selatan / Jakarta Pusat corridors; served: {_first_clause(used_for)}."
    reports = sorted((in_reports or {}).get(sid, []))
    if reports:
        return "CONDENSED-OUT", "Cut for length; still held in " + ", ".join(f"`reports/{r}`" for r in reports) + "."
    csvs = sorted((in_csvs or {}).get(sid, []))
    if csvs:
        return "OFF-SCOPE", f"Not needed for the report's questions; served: {_first_clause(used_for)} (`{csvs[0]}`" + (f" +{len(csvs)-1} more" if len(csvs) > 1 else "") + ")."
    return "OFF-SCOPE", f"Not referenced in any CSV or 2026-10-17 report; served: {_first_clause(used_for)}."


def classify_preverification(r: dict, cited: set, overrides: dict):
    """Return (state, code, reason); state is 'used' or 'unused'."""
    iid, verdict = r["item_id"], r.get("verdict", "")
    if iid in overrides:
        code, reason = _override_pair(overrides[iid])
        return "unused", code, reason
    host = re.sub(r"^https?://([^/]+).*$", r"\1", r.get("source_url", "") or "")
    if verdict == "NOT-CONFIRMED":
        why = r.get("corrected_value") or r.get("evidence_quote") or "source does not support the claim"
        return "unused", "NOT-CONFIRMED", _trunc_words(why, 30)
    if verdict == "UNREACHABLE":
        return "unused", "BLOCKED", f"Unreachable in wave 2b ({host or 'no URL'}); could not be verified."
    if verdict in {"CONFIRMED", "CORRECTED"}:
        if iid in cited:
            return "used", "", ""
        return "unused", "CONDENSED-OUT", f"Verified in wave 2b ({verdict}) but not cited in the report; origin `{_trunc_words(r.get('origin'), 8)}`."
    if iid in cited:
        return "used", "", ""
    return "unused", "UNVERIFIED-NOT-USED", "check=if_used item with no verdict; not run and not cited in the report."



def _count_claims_for_source(sid, rowids, claims):
    keys = {sid} | set(rowids)
    n = 0
    for c in claims:
        toks = {t.strip() for t in re.split(r";", c.get("source_ids", ""))}
        if toks & keys:
            n += 1
    return n


def generate_sources_appendix(
    sources_reg,
    used_src_ids,
    src_id_to_sections,
    src_id_to_rowids,
    cited_model_sheets,
    cited_team_files,
    blocked_data,
    unused_reasons_override,
    claims=None,
):
    claims = claims or []
    overrides = _load_overrides(unused_reasons_override)
    all_sources = list(sources_reg.values())
    in_reports, in_csvs = build_reference_index(sources_reg)

    preverify = load_csv(PREVERIFY_PATH)
    cited_pv = set()
    pv_sections = defaultdict(set)
    pv_ids = {r["item_id"] for r in preverify}
    for c in claims:
        for tok in re.split(r"[;\s]+", c.get("verification", "")):
            if tok in pv_ids:
                cited_pv.add(tok)
                pv_sections[tok].add(c["section"])
    pv_state = {r["item_id"]: classify_preverification(r, cited_pv, overrides) for r in preverify}
    pv_confirmed_rows = set()  # BLOCKED/GAP row ids confirmed (CONFIRMED/CORRECTED) in wave 2b
    for r in preverify:
        if r.get("verdict") in {"CONFIRMED", "CORRECTED"}:
            for rid in re.findall(r"[A-Za-z0-9][A-Za-z0-9-]*", r.get("origin", "")):
                pv_confirmed_rows.add(rid)

    unused_sources = [s for s in all_sources if s["id"] not in used_src_ids]
    src_rows = []
    for s in unused_sources:
        code, reason = classify_unused_source_reason(s, overrides, in_reports, in_csvs)
        src_rows.append((s, code, reason))

    # Blocked / gap rows (union with the excluded-rows CSV), not confirmed in wave 2b
    row_entries = []
    seen = set()
    unreachable_items = defaultdict(list)
    for r in preverify:
        if r.get("verdict") == "UNREACHABLE":
            for rid in re.findall(r"[A-Za-z0-9][A-Za-z0-9-]*", r.get("origin", "")):
                unreachable_items[rid].append(r["item_id"])
    for kind, key in (("BLOCKED", "blocked_rows"), ("GAP", "gap_rows")):
        for b in blocked_data.get(key, []):
            rid = b["row_id"]
            if rid in seen:
                continue
            seen.add(rid)
            if rid in pv_confirmed_rows:
                continue
            topic = b.get("question_or_metric") or b.get("question") or b.get("claim_short") or "See CSV"
            note = b.get("gaps") or b.get("notes") or b.get("reason_excluded") or ""
            if rid in overrides:
                code, reason = _override_pair(overrides[rid])
            elif rid in unreachable_items:
                code, reason = "BLOCKED", f"Unreachable in wave 2b (item {', '.join(unreachable_items[rid])}); could not be verified."
            elif kind == "GAP":
                code, reason = "BLOCKED", "Evidence gap: " + _first_clause(re.sub(r"^GAP:\s*", "", note), 25) + "."
            else:
                if note.startswith("GAP:"):
                    code, reason = "BLOCKED", "Blocked, not confirmed in wave 2b: " + _first_clause(note[4:], 25) + "."
                else:
                    code, reason = "BLOCKED", "Source blocked or opened only as a snippet; not confirmed in wave 2b."
            row_entries.append((rid, b.get("file", b.get("source_file", "")), kind, topic, code, reason))
    excl_csv = ROOT / "data" / "processed" / "2026-10-pillar1-mapping-excluded.csv"
    for r in load_csv(excl_csv):
        rid = r.get("row_id", "")
        if not rid or rid in seen or rid in pv_confirmed_rows:
            continue
        seen.add(rid)
        row_entries.append((rid, r.get("source_file", ""), r.get("verification", "BLOCKED"), r.get("claim_short", ""), "BLOCKED", "Excluded: " + _first_clause(r.get("reason_excluded", ""), 25) + "."))

    dropped_map = {
        "UNCONFIRMED": "NOT-CONFIRMED", "DERIVED": "NOT-CONFIRMED", "DERIVED-MOVE": "NOT-CONFIRMED",
        "NOT-FOUND-OPENED": "NOT-CONFIRMED", "DUPLICATE-MERGED": "DUPLICATE", "DATE-FAIL": "OUT-OF-WINDOW",
        "TIER-4-LEAD": "TIER4-LEAD",
    }
    dropped = []
    for r in load_csv(ROOT / "data" / "processed" / "2026-10-16-run1-dropped-rows.csv"):
        rid = r.get("row_id", "")
        if rid in overrides:
            code, reason = _override_pair(overrides[rid])
        else:
            code = dropped_map.get(r.get("verdict", ""), "NOT-CONFIRMED")
            reason = _first_clause(re.sub(r"^(Run \d\w? )?(\(?[A-Za-z0-9-]+\)?\s*)?(registrar|verifier)?[^:]{0,40}:\s*", "", r.get("reason", "")), 30) + "."
        dropped.append((r, code, reason))

    pv_unused = [(r, *pv_state[r["item_id"]][1:]) for r in preverify if pv_state[r["item_id"]][0] == "unused"]
    pv_used = [r for r in preverify if pv_state[r["item_id"]][0] == "used"]

    counts = defaultdict(int)
    for _, c, _ in src_rows:
        counts[c] += 1
    for r, c, _ in pv_unused:
        counts[c] += 1
    for e in row_entries:
        counts[e[4]] += 1
    for _, c, _ in dropped:
        counts[c] += 1

    lines = [
        "# Deliverable 2: CORSA Jakarta Market-Entry Insights — Sources Appendix",
        "",
        "**Date:** 2026-10-18  ",
        "**Companion Document:** `reports/2026-10-18-corsa-jakarta-insights-report.md` (Deliverable 1)  ",
        "**Claim Ledger:** `data/processed/2026-10-18-claim-ledger.csv`  ",
        f"**Source Register:** {len(all_sources)} entries in `sources/sources.md`; {len(used_src_ids)} cited in Deliverable 1 (Part A); {len(unused_sources)} not cited (Part B.1).  ",
        "",
        "---",
        "",
        "## Part A — Sources Used in Deliverable 1",
        "",
        "### A.1 Register sources cited in the report",
        "",
        "| ID | Title | Publisher | Tier | Publication date | URL | Report sections | Claims |",
        "|---|---|---|---:|---|---|---|---:|",
    ]
    used_sources = sorted((s for s in all_sources if s["id"] in used_src_ids), key=lambda s: (s.get("tier") or 9, s["id"]))
    for s in used_sources:
        sid = s["id"]
        secs = sorted(src_id_to_sections.get(sid, set()))
        sec_str = "; ".join(secs[:3]) + (f" (+{len(secs)-3} more)" if len(secs) > 3 else "")
        n = _count_claims_for_source(sid, src_id_to_rowids.get(sid, set()), claims)
        lines.append(f"| `{sid}` | {_esc(s['title'])} | {_esc(s['publisher'])} | {s.get('tier')} | {_esc(s['published'])} | {s['primary_url']} | {_esc(sec_str)} | {n} |")
    lines.append("")

    lines.extend([
        "### A.2 Wave-2b pre-verified items cited in the report",
        "",
        "| Item ID | Origin | Verdict | Claim (first 25 words) | Report sections |",
        "|---|---|---|---|---|",
    ])
    for r in pv_used:
        lines.append(f"| `{r['item_id']}` | {_esc(_trunc_words(r['origin'], 10))} | {r.get('verdict') or 'no verdict'} | {_esc(_trunc_words(r['claim']))} | {_esc('; '.join(sorted(pv_sections[r['item_id']])[:3]))} |")
    lines.append("")

    # Reuse the existing team-file and model-sheet blocks (A.3 / A.4).
    lines.extend([
        "### A.3 Internal Team Baseline Documents Audited & Cited (`team: ...`)",
        "",
        "Per project evidence policy, internal team Phase 1 documents are audited as baseline claims to be tested against external evidence, never as proof of external market facts.",
        "",
        "| File Path | Document Title & Scope | Role in Deliverable 1 |",
        "|---|---|---|",
        "| `docs/scope/2026-10-16-project-scope-summary.md` | CORSA Concept & Scope Summary (60–80 m² vs 150 m² café/bakehouse, menu pillars, target segments, CHF 200k envelope) | Used to anchor concept parameters and identify internal scope vs model divergences (`team: 2026-10-16-project-scope-summary.md`). |",
        "| `research/internal/phase-1/PESTEL_Analysis_Updated (2).pdf` | Team Phase 1 PESTEL Analysis (Jakarta F&B Market Entry) | Audited claim-by-claim in Section 2 (`team: PESTEL_Analysis_Updated (2).pdf`); verified, refined, or corrected against Tier 1–3 statutory and BPS records. |",
        "| `research/internal/phase-1/CAGE Analysis - Indonesian F&B Market Entry for CORSA.pdf` | Team Phase 1 CAGE Distance Analysis (Switzerland vs Indonesia) | Audited claim-by-claim in Section 3 (`team: CAGE Analysis - Indonesian F&B Market Entry for CORSA.pdf`); cross-checked against 174-claim register in `reports/2026-10-17-cage-switzerland-jakarta.md`. |",
        "",
        "### A.4 Financial Model v0.6 Sheets & Embedded Sources Audited (`model v0.6: ...`)",
        "",
        "- **Workbook Path:** `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx` (20 sheets; CSV mirror in `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6-csv/`).",
        "- **Sheets Cited in Deliverable 1:** " + (", ".join(f"`{sh}`" for sh in sorted(cited_model_sheets)) if cited_model_sheets else "All 20 sheets audited."),
        "- **Model Embedded `Sources` Sheet (`Sources!A5:G108`, `S01`–`S104`):** Contains 104 source entries across 11 categories (`Macro & FX`, `Tax & Regulation`, `Location & Rent`, `Fit-Out & Equipment`, `Menu & COGS`, `Demand & Revenue`, `Staffing & Labor`, `OPEX & Utilities`, `Competitors`, `Industry Benchmarks`, `Equipment Financing & Leasing`).",
        "- **Model Embedded `Research_Tracker` Sheet (`Research_Tracker!A5:F17`, `R01`–`R13`):** Tracks 13 core parameter blocks — **5 `Placeholder`** (`R04` dine-in seat turns, `R05` delivery orders/day, `R06` menu prices, `R07` ingredient COGS %, `R09` renovation/fit-out cost/m²), **4 `Desk`** (`R01` rent, `R02` upfront lease years, `R12` utility bills, `R13` ramp-up curve), and **4 `Model ready`** (`R03` PBJT 10%, `R08` salaries, `R10` espresso machine, `R11` PT PMA legal setup).",
        "",
    ])

    lines.extend([
        "",
        "---",
        "",
        "## Part B — Sources and Rows Not Used in Deliverable 1",
        "",
        "Every row has one reason code and a one-line explanation. `OFF-SCOPE` and `CONDENSED-OUT` reasons for register entries are derived by the script from where the source id appears (2026-10-17 long reports, then `data/processed/` CSVs); entries in `analysis/appendix_reason_overrides.json` replace the script's choice.",
        "",
        "| Code | Meaning | Rows |",
        "|---|---|---:|",
    ])
    for code, meaning in PART_B_CODES.items():
        lines.append(f"| `{code}` | {meaning} | {counts.get(code, 0)} |")
    lines.extend([
        "",
        f"### B.1 Register entries not cited ({len(src_rows)})",
        "",
        "| ID | Tier | Title | Publisher | Part B code | Reason |",
        "|---|---:|---|---|---|---|",
    ])
    for s, code, reason in src_rows:
        lines.append(f"| `{s['id']}` | {s.get('tier')} | {_esc(s['title'])} | {_esc(s['publisher'])} | `{code}` | {_esc(reason)} |")

    lines.extend([
        "",
        f"### B.2 Pre-verification items not used ({len(pv_unused)})",
        "",
        "Source: `data/processed/2026-10-18-preverification.csv`. Items with a CONFIRMED or CORRECTED verdict that are cited in the report are listed in Part A.2.",
        "",
        "| Item ID | Origin | Check | Verdict | Claim (first 25 words) | Part B code | Reason |",
        "|---|---|---|---|---|---|---|",
    ])
    for r, code, reason in pv_unused:
        lines.append(f"| `{r['item_id']}` | {_esc(_trunc_words(r['origin'], 10))} | {r.get('check','')} | {r.get('verdict') or 'none'} | {_esc(_trunc_words(r['claim']))} | `{code}` | {_esc(reason)} |")

    lines.extend([
        "",
        f"### B.3 `BLOCKED` and `GAP` rows in the CSVs not confirmed in wave 2b ({len(row_entries)})",
        "",
        "Rows confirmed or corrected in wave 2b are omitted here (they appear in Part A.2 or B.2).",
        "",
        "| Row ID | File | Status | Topic / metric | Part B code | Reason |",
        "|---|---|---|---|---|---|",
    ])
    for rid, f, kind, topic, code, reason in row_entries:
        lines.append(f"| `{rid}` | `{Path(str(f)).name}` | `{kind}` | {_esc(_trunc_words(topic, 18))} | `{code}` | {_esc(reason)} |")

    lines.extend([
        "",
        f"### B.4 Run 1 dropped rows ({len(dropped)})",
        "",
        "Source: `data/processed/2026-10-16-run1-dropped-rows.csv`.",
        "",
        "| Row ID | File | Claim | Part B code | Reason |",
        "|---|---|---|---|---|",
    ])
    for r, code, reason in dropped:
        lines.append(f"| `{r.get('row_id','')}` | `{r.get('file','')}` | {_esc(_trunc_words(r.get('claim',''), 18))} | `{code}` | {_esc(reason)} |")

    lines.extend([
        "",
        "---",
        "",
        "## Part C — Paul's Phase 2 Sources (19 Oct 2026)",
        "",
        "Sources REG-136 to REG-143 were pre-verified on 19 Oct 2026 (`analysis/outputs/preverification-batch-4.csv`). Verdict counts are from rows whose claim carries the source id; cited items and sections come from the report.",
        "",
        "| ID | Title | Publisher | Tier | URL | Pre-verification verdicts | Items cited in report | Report sections fed |",
        "|---|---|---|---:|---|---|---|---|",
    ])
    for n in range(136, 144):
        sid = f"REG-{n}"
        s = sources_reg.get(sid)
        if not s:
            continue
        items = [r for r in preverify if f"[{sid};" in r.get("claim", "")]
        verdicts = Counter(r.get("verdict") or "none" for r in items)
        cited = sorted(r["item_id"] for r in items if r["item_id"] in cited_pv)
        secs = sorted({sec for i in cited for sec in pv_sections[i]})
        lines.append(
            f"| `{sid}` | {_esc(s['title'])} | {_esc(s['publisher'])} | {s.get('tier')} | {_esc((s.get('all_urls') or [s.get('primary_url', '')])[0])} | "
            + _esc(", ".join(f"{v} {k}" for k, v in sorted(verdicts.items())))
            + f" | {_esc(', '.join(cited) or 'none')} | {_esc('; '.join(secs) or 'none')} |"
        )

    with open(APPENDIX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[verify_report] Wrote Deliverable 2 appendix to {APPENDIX_PATH}")
    print("[verify_report] Part B rows per code: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify Deliverable 1 and generate Claim Ledger + Deliverable 2 Appendix")
    args = parser.parse_args()
    parse_report_and_generate_artifacts()
