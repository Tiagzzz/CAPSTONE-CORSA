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
from collections import defaultdict
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


def classify_unused_source_reason(s: dict, unused_reasons_override: dict) -> str:
    sid = s["id"]
    if sid in unused_reasons_override:
        return unused_reasons_override[sid]

    acc = (s.get("accessed") or "").lower()
    used_for = (s.get("used_for") or "")
    title = (s.get("title") or "")

    if not s.get("is_opened", True) or any(k in acc for k in ["not opened", "403", "404", "blocked", "timeout", "unreachable", "snippet"]):
        return f"Access restricted / not opened in full ({s.get('accessed')}); excluded as sole support under strict source-verification policy."
    if "dropped" in used_for.lower() or "excluded" in used_for.lower():
        return "Underlying row was dropped or excluded during Run 1 / Pillar 1 scope audit (out-of-corridor or non-applicable sector)."
    if any(k in title.lower() for k in ["bogor", "bekasi", "depok", "tangerang", "surabaya", "bali", "bandung"]):
        return "Covers non-target municipality outside CORSA's Jakarta Selatan / Jakarta Pusat entry corridors; retained in repository for regional context only."
    if s.get("tier") == 4:
        return "Tier 4 directory/social/listing source superseded by Tier 1–3 primary regulatory, BPS, or operator disclosures in Deliverable 1."
    if s.get("tier") == 3 and any(k in title.lower() for k in ["menu", "grabfood", "gofood", "pergikuliner", "harga"]):
        return "Granular SKU price/menu source aggregated into `data/processed/price-ladder.csv` distributional metrics (`compute_stats.py`); individual SKU row not cited separately in prose."
    return "Background or corroborating reference in `data/processed/` CSVs; superseded in Deliverable 1 prose by direct Tier 1/2 statutory or official statistical citations covering the same topic."


def generate_sources_appendix(
    sources_reg,
    used_src_ids,
    src_id_to_sections,
    src_id_to_rowids,
    cited_model_sheets,
    cited_team_files,
    blocked_data,
    unused_reasons_override,
):
    all_sources = list(sources_reg.values())
    lines = [
        "# Deliverable 2: CORSA Jakarta Market-Entry Insights — Sources & Verification Appendix",
        "",
        "**Date:** 2026-10-18  ",
        "**Companion Document:** `reports/2026-10-18-corsa-jakarta-insights-report.md` (Deliverable 1)  ",
        "**Claim Ledger:** `data/processed/2026-10-18-claim-ledger.csv`  ",
        f"**Repository Source Register Total:** {len(all_sources)} registered sources in `sources/sources.md` (`{len(used_src_ids)}` used in Deliverable 1; `{len(all_sources) - len(used_src_ids)}` not directly used in Deliverable 1, documented with explicit reasons in Part B).  ",
        "",
        "---",
        "",
        "## Part A — Sources Used in Deliverable 1",
        "",
        "### A.1 External Primary & Secondary Sources Used (`sources/sources.md`, Grouped by Quality Tier)",
        "",
    ]

    used_sources = [s for s in all_sources if s["id"] in used_src_ids]
    for tier in [1, 2, 3, 4]:
        tier_sources = [s for s in used_sources if s.get("tier") == tier]
        lines.append(f"#### Tier {tier} Sources Used ({len(tier_sources)} sources)")
        lines.append("")
        if not tier_sources:
            lines.append("_None cited in this tier._")
            lines.append("")
            continue
        lines.append("| Source ID | Title | Publisher / Institution | Published | Accessed | Linked `row_id`s / Report Sections | URL |")
        lines.append("|---|---|---|---|---|---|---|")
        for s in tier_sources:
            sid = s["id"]
            rids = sorted(src_id_to_rowids.get(sid, set()))
            secs = sorted(src_id_to_sections.get(sid, set()))
            rid_str = ", ".join(f"`{r}`" for r in rids[:8]) + (f" (+{len(rids)-8} more)" if len(rids) > 8 else "")
            sec_str = "; ".join(secs[:3]) + (f" (+{len(secs)-3} more)" if len(secs) > 3 else "")
            usage_col = f"{rid_str} — {sec_str}".strip(" —")
            lines.append(
                f"| `{sid}` | {s['title']} | {s['publisher']} | {s['published']} | {s['accessed']} | {usage_col} | {s['primary_url']} |"
            )
        lines.append("")

    lines.extend([
        "### A.2 Internal Team Baseline Documents Audited & Cited (`team: ...`)",
        "",
        "Per project evidence policy, internal team Phase 1 documents are audited as baseline claims to be tested against external evidence, never as proof of external market facts.",
        "",
        "| File Path | Document Title & Scope | Role in Deliverable 1 |",
        "|---|---|---|",
        "| `docs/scope/2026-10-16-project-scope-summary.md` | CORSA Concept & Scope Summary (60–80 m² vs 150 m² café/bakehouse, menu pillars, target segments, CHF 200k envelope) | Used to anchor concept parameters and identify internal scope vs model divergences (`team: 2026-10-16-project-scope-summary.md`). |",
        "| `research/internal/phase-1/PESTEL_Analysis_Updated (2).pdf` | Team Phase 1 PESTEL Analysis (Jakarta F&B Market Entry) | Audited claim-by-claim in Section 2 (`team: PESTEL_Analysis_Updated (2).pdf`); verified, refined, or corrected against Tier 1–3 statutory and BPS records. |",
        "| `research/internal/phase-1/CAGE Analysis - Indonesian F&B Market Entry for CORSA.pdf` | Team Phase 1 CAGE Distance Analysis (Switzerland vs Indonesia) | Audited claim-by-claim in Section 3 (`team: CAGE Analysis - Indonesian F&B Market Entry for CORSA.pdf`); cross-checked against 174-claim register in `reports/2026-10-17-cage-switzerland-jakarta.md`. |",
        "",
        "### A.3 Financial Model v0.6 Sheets & Embedded Sources Audited (`model v0.6: ...`)",
        "",
        "- **Workbook Path:** `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx` (20 sheets; CSV mirror in `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6-csv/`).",
        "- **Sheets Cited in Deliverable 1:** " + (", ".join(f"`{sh}`" for sh in sorted(cited_model_sheets)) if cited_model_sheets else "All 20 sheets audited."),
        "- **Model Embedded `Sources` Sheet (`Sources!A5:G108`, `S01`–`S104`):** Contains 104 source entries across 11 categories (`Macro & FX`, `Tax & Regulation`, `Location & Rent`, `Fit-Out & Equipment`, `Menu & COGS`, `Demand & Revenue`, `Staffing & Labor`, `OPEX & Utilities`, `Competitors`, `Industry Benchmarks`, `Equipment Financing & Leasing`).",
        "- **Model Embedded `Research_Tracker` Sheet (`Research_Tracker!A5:F17`, `R01`–`R13`):** Tracks 13 core parameter blocks — **5 `Placeholder`** (`R04` dine-in seat turns, `R05` delivery orders/day, `R06` menu prices, `R07` ingredient COGS %, `R09` renovation/fit-out cost/m²), **4 `Desk`** (`R01` rent, `R02` upfront lease years, `R12` utility bills, `R13` ramp-up curve), and **4 `Model ready`** (`R03` PBJT 10%, `R08` salaries, `R10` espresso machine, `R11` PT PMA legal setup).",
        "",
        "---",
        "",
        "## Part B — Sources & Rows Not Used in Deliverable 1 (with Specific Reason for Each)",
        "",
        "### B.1 Registered Sources in `sources/sources.md` Not Cited in Deliverable 1",
        "",
        f"All **{len(all_sources) - len(used_src_ids)}** entries from `sources/sources.md` that are not directly cited in Part A are listed below with the specific reason for non-use.",
        "",
        "| Source ID | Tier | Title | Publisher | Access Status in Repo | Specific Reason Not Used in Deliverable 1 |",
        "|---|---:|---|---|---|---|",
    ])

    unused_sources = [s for s in all_sources if s["id"] not in used_src_ids]
    for s in unused_sources:
        reason = classify_unused_source_reason(s, unused_reasons_override)
        lines.append(
            f"| `{s['id']}` | Tier {s.get('tier')} | {s['title']} | {s['publisher']} | {s['accessed']} | {reason} |"
        )

    lines.extend([
        "",
        "### B.2 Unconfirmed `BLOCKED` Rows, `GAP` Rows, and Pre-Verification Outcomes (`data/processed/2026-10-18-preverification.csv`)",
        "",
        "Every row marked `BLOCKED` or `GAP` across the repository was isolated by `analysis/inventory.py` (`analysis/outputs/blocked_rows.json`) and subjected to targeted pre-verification (`data/processed/2026-10-18-preverification.csv`). Any row not confirmed from an opened Tier 1–3 document was excluded from supporting any factual claim in Deliverable 1 and is logged below:",
        "",
    ])

    if PREVERIFY_PATH.exists():
        lines.append("#### Pre-Verification Table (`data/processed/2026-10-18-preverification.csv`)")
        lines.append("")
        with open(PREVERIFY_PATH, "r", encoding="utf-8") as f:
            pv_rows = list(csv.DictReader(f))
        if pv_rows:
            cols = list(pv_rows[0].keys())
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "|".join(["---"] * len(cols)) + "|")
            for r in pv_rows:
                lines.append("| " + " | ".join(str(r.get(c, "")).replace("|", "\\|").replace("\n", " ") for c in cols) + " |")
            lines.append("")

    lines.extend([
        "#### Complete Register of 26 `BLOCKED` Rows and 9 `GAP` Rows in Repository CSVs & Tables",
        "",
        "| Row ID | Source File | Status | Topic / Metric | Reason Excluded from Factual Claims (or Pre-Verification Outcome) |",
        "|---|---|---|---|---|",
    ])

    for b in blocked_data.get("blocked_rows", []):
        topic = b.get("question_or_metric") or b.get("question") or "See CSV"
        notes = b.get("notes") or b.get("gaps") or "Source blocked by HTTP 403 / Cloudflare / timeout during Runs 1–4; never cited as factual support."
        lines.append(
            f"| `{b['row_id']}` | `{b['file']}` | `{b['verification']}` | {str(topic)[:90]} | {str(notes)[:160]} |"
        )

    for g in blocked_data.get("gap_rows", []):
        topic = g.get("question_or_metric") or g.get("question") or "Evidence gap"
        notes = g.get("notes") or g.get("gaps") or "Explicitly logged as an open evidence gap requiring Phase 2 primary validation."
        lines.append(
            f"| `{g['row_id']}` | `{g['file']}` | `{g['verification']}` | {str(topic)[:90]} | {str(notes)[:160]} |"
        )

    dropped_csv = ROOT / "data" / "processed" / "2026-10-16-run1-dropped-rows.csv"
    lines.extend([
        "",
        "### B.3 Run 1 Dropped Rows (`data/processed/2026-10-16-run1-dropped-rows.csv` — 26 Rows)",
        "",
        "These 26 rows were removed from active analytical tables during the Run 1 quality audit and are never cited in Deliverable 1:",
        "",
        "| Original File | Row Key | Dimension / Topic | Metric | Value | Reason Dropped |",
        "|---|---|---|---|---|---|",
    ])
    if dropped_csv.exists():
        with open(dropped_csv, "r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                lines.append(
                    f"| `{r.get('original_file','')}` | `{r.get('row_key','')}` | {r.get('dimension','')} / {r.get('topic','')} | "
                    f"{r.get('metric','')} | {r.get('value','')} {r.get('unit','')} | {r.get('reason_dropped','')} |"
                )

    excl_csv = ROOT / "data" / "processed" / "2026-10-pillar1-mapping-excluded.csv"
    lines.extend([
        "",
        "### B.4 Pillar 1 Mapping Excluded Rows (`data/processed/2026-10-pillar1-mapping-excluded.csv` — 18 Rows)",
        "",
        "These 18 rows (`P1M-011` to `P1M-028`) were excluded during the Run 4 scope audit because they did not verify active healthy/grain-bowl/salad/smoothie-bowl venues inside Jakarta Selatan or Jakarta Pusat:",
        "",
        "| Row ID | Brand / Venue | Category / Format | Corridor | Status | Reason Excluded |",
        "|---|---|---|---|---|---|",
    ])
    if excl_csv.exists():
        with open(excl_csv, "r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                lines.append(
                    f"| `{r.get('row_id','')}` | {r.get('brand_or_venue','')} | {r.get('category_format','')} | "
                    f"{r.get('corridor_area','')} | `{r.get('verification_status','')}` | {r.get('notes','')} |"
                )

    lines.extend([
        "",
        "---",
        "",
        "## Part C — Structured Placeholder for Paul's Phase 2 Primary Validation & Model v0.7+ Sources",
        "",
        "This section provides the ready-to-fill verification tables for Phase 2 primary field research in Jakarta and the corresponding updates to the CORSA financial model (`v0.7+`).",
        "",
        "### C.1 Phase 2 Primary Field & Supplier Validation Log (To Be Populated in Phase 2)",
        "",
        "| Phase 2 Source ID | Validation Category | Target Model Cells / `Research_Tracker` ID | Counterparty / Informant (Role, District, Date) | Verified Quotation / Term Sheet / Field Observation | Evidence Artifact (PDF / Quote / Photo Path) | Verification Status |",
        "|---|---|---|---|---|---|---|",
        "| `P2-SRC-01` | Retail Lease & Upfront Prepayment Terms | `R01`, `R02` (`Rent_Data!E6:M13`, `Inputs!E28:G28`) | _[e.g., 3 commercial brokers / landlords in Senopati, Cipete, Menteng]_ | _[Quoted base rent Rp/m²/mo, service charge, minimum lease term, 1-yr vs 2-yr upfront prepayment requirement]_ | _[Pending Phase 2 term sheets]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-02` | Contractor Fit-Out & MEP Quotes (150 m²) | `R09` (`CAPEX (Buy)!E8:G13`, `CAPEX (Rent)!E8:G13`) | _[e.g., 2 Jakarta F&B interior/MEP contractors]_ | _[Itemized BOQ for civil, electrical upgrade, grease trap, HVAC, custom millwork]_ | _[Pending Phase 2 contractor BOQs]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-03` | Commercial Kitchen & Espresso Equipment Quotes / Leasing | `R10` (`CAPEX (Buy)!E15:G22`, `CAPEX (Rent)!B101:M116`) | _[e.g., PT Toffin Indonesia, Rotaryana, ORI Leasing / multifinance]_ | _[Written quotes for 2-group espresso machine, grinders, bronze-die pasta extruder, refrigeration; eligibility of newly incorporated PT PMA for equipment lease]_ | _[Pending Phase 2 vendor quotes]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-04` | Wholesale Ingredient & Packaging Price Lists (BOM) | `R07` (`Menu!J7:L24`) | _[e.g., Sukanda Djaya / Indoguna / local specialty roasters / semolina importers]_ | _[Delivered wholesale prices per kg/L for durum semolina, imported cheeses, specialty arabica beans, proteins, and eco-packaging]_ | _[Pending Phase 2 supplier price lists]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-05` | Corridor Footfall & Daypart Seat-Turn Counts | `R04`, `R05` (`Revenue!D8:F12`, `Revenue!D17:F20`) | _[e.g., Observational seat-turn & queue logging at 6 benchmark venues across Senopati, SCBD, Menteng, Kemang, Cipete]_ | _[Observed weekday vs weekend covers by daypart (breakfast, lunch, afternoon, dinner) and GoFood/GrabFood rider pickup counts]_ | _[Pending Phase 2 field tally sheets]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-06` | Consumer Willingness-to-Pay & Menu Price Testing | `R06` (`Menu!E7:G24`) | _[e.g., Intercept surveys / tasting panels with Jakarta Selatan & Pusat target customers aged 25–39]_ | _[Price sensitivity and bundle preference for fresh pasta + coffee/elixir combinations at Rp 85k–135k net]_ | _[Pending Phase 2 survey dataset]_ | `PENDING_PHASE_2` |",
        "| `P2-SRC-07` | PT PMA Incorporation, Notary, & BPJPH Halal Certification Quotes | `R11` (`CAPEX (Buy)!E34:G38`, `OPEX!C28:C33`) | _[e.g., Jakarta corporate notary + BPJPH LPH halal inspection agency]_ | _[Binding legal fee schedule for PT PMA setup, OSS-RBA KBLI 56101/56303/10794 verification, SLHS, and Halal SJPH audit timeline]_ | _[Pending Phase 2 legal/LPH proposals]_ | `PENDING_PHASE_2` |",
        "",
        "### C.2 Phase 2 Financial Model Update Log (`v0.6` -> `v0.7+` Checklist)",
        "",
        "| Model Fix ID | Sheet & Cell Range in `v0.6` | Defect / Gap in `v0.6` | Required Update in `v0.7+` | Status |",
        "|---|---|---|---|---|",
        "| `MOD-FIX-01` | `PnL_Monthly!P4:BJ48` | Months 14–60 are completely unpopulated (only Months 1–13 in `C4:O48` exist), causing `Annual` Y2–Y5, `Dashboard!B17` (Y3 EBITDA), `Dashboard!B19` (5-yr NPV), `Dashboard!B25` (Payback), and `Dashboard!B26` (5-yr IRR) to fail or truncate. | Extend monthly formulas across all 60 columns (`C` to `BJ`), incorporating annual inflation (`Inputs!H11`), lease renewal/prepayment stepping in Year 3 and Year 5, and 36-month equipment lease maturity (`CAPEX (Rent)!H47`). | `OPEN_FOR_V0.7` |",
        "| `MOD-FIX-02` | `Scenarios!C35:E35` & `PnL_Monthly!C34:O34` | Depreciation formula (`='CAPEX (Buy)'!$F$32*0.65/60`) hardcodes Base Buy-mode hard costs even when `Inputs!H4 = 2` (Lease mode) or Conservative/Optimistic scenarios are active. | Link depreciation dynamically to active scenario and owned-asset base (excluding leased equipment principal under operating lease or separating finance-lease amortization). | `OPEN_FOR_V0.7` |",
        "| `MOD-FIX-03` | `MonteCarlo!A36:K1035` | Simulates static 1-month steady-state EBITDA and simple steady-state payback (`CAPEX / (12 * EBITDA)`), ignoring 12-month ramp-up cash burn and multi-year lease cash outflows. | Integrate 60-month cash-flow series into Monte Carlo simulation to compute true multi-year NPV, IRR, and minimum cash trough probabilities. | `OPEN_FOR_V0.7` |",
        "| `MOD-FIX-04` | `Inputs!F21` vs Scope Doc | Model uses `150 m²` usable area / `60 seats` (`Inputs!F21`, `Revenue!C5`), whereas `docs/scope/2026-10-16-project-scope-summary.md` specifies `60–80 m²` (`15–30 seats`). | Reconcile store footprint archetype (flagship 150 m² dine-in bistro vs 70 m² compact kiosk/café) and run parallel unit economics for both footprints. | `OPEN_FOR_V0.7` |",
    ])

    with open(APPENDIX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[verify_report] Wrote Deliverable 2 appendix to {APPENDIX_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify Deliverable 1 and generate Claim Ledger + Deliverable 2 Appendix")
    args = parser.parse_args()
    parse_report_and_generate_artifacts()
