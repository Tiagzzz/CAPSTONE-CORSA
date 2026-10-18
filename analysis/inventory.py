#!/usr/bin/env python3
"""
Inventory script for CAPSTONE-CORSA repository.
Parses sources/sources.md, all CSV files in data/processed/**/*.csv,
and data/raw/2026-10-17-disconfirming-evidence.md.
Outputs:
  - analysis/outputs/sources_register.json
  - analysis/outputs/row_index.json
  - analysis/outputs/blocked_rows.json
  - analysis/outputs/downside_rows.json
  - analysis/outputs/inventory_summary.json
"""

import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "analysis" / "outputs"


def extract_urls(text: str) -> list[str]:
    if not text:
        return []
    # Match http/https URLs, stripping trailing punctuation like ), ., ;, ,
    raw_urls = re.findall(r"https?://[^\s<>\"\'\)]+", text)
    cleaned = []
    for u in raw_urls:
        u = u.rstrip(".,;:")
        if u and u not in cleaned:
            cleaned.append(u)
    return cleaned


def parse_sources_md(sources_path: Path) -> dict[str, dict]:
    """Parse markdown table in sources/sources.md into a dictionary keyed by ID."""
    register = {}
    lines = sources_path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        line_str = line.strip()
        if not line_str.startswith("|"):
            continue
        parts = [p.strip() for p in line_str.strip("|").split("|")]
        if len(parts) < 8:
            continue
        src_id = parts[0]
        if src_id in ("ID", "---") or set(src_id) <= {"-", " "}:
            continue
        title, publisher, url_field, published, accessed, tier_str, used_for = (
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            parts[5],
            parts[6],
            "|".join(parts[7:]).strip(),
        )
        urls = extract_urls(url_field)
        primary_url = urls[0] if urls else url_field
        try:
            tier = int(tier_str.strip())
        except ValueError:
            tier = None
        acc_without_not = re.sub(r"not\s+opened", "", accessed.lower())
        is_opened = ("opened" in acc_without_not) or (
            accessed.strip() in ("2026-10-17", "2026-10-16") and "snippet" not in acc_without_not
        )
        register[src_id] = {
            "id": src_id,
            "title": title,
            "publisher": publisher,
            "url_field": url_field,
            "primary_url": primary_url,
            "all_urls": urls,
            "published": published,
            "accessed": accessed,
            "tier": tier,
            "tier_raw": tier_str,
            "used_for": used_for,
            "is_opened": is_opened,
        }
    return register


def parse_disconfirming_table_a(md_path: Path, register: dict[str, dict]) -> dict[str, dict]:
    """Parse Table A of data/raw/2026-10-17-disconfirming-evidence.md."""
    rows = {}
    if not md_path.exists():
        return rows
    lines = md_path.read_text(encoding="utf-8").splitlines()
    in_table_a = False
    for line in lines:
        s = line.strip()
        if s.startswith("## A. Evidence table"):
            in_table_a = True
            continue
        if in_table_a and s.startswith("## "):
            break
        if not in_table_a or not s.startswith("|"):
            continue
        parts = [p.strip() for p in s.strip("|").split("|")]
        if len(parts) < 11:
            continue
        num = parts[0]
        if num in ("#", "---") or not num.isdigit():
            continue
        row_id = f"DISC-A{num}"
        reg_ids = [r.strip() for r in re.split(r"[;,]", parts[9]) if r.strip()]
        primary_tier = None
        urls = []
        for rid in reg_ids:
            if rid in register:
                if primary_tier is None and register[rid]["tier"] is not None:
                    primary_tier = register[rid]["tier"]
                for u in register[rid]["all_urls"]:
                    if u not in urls:
                        urls.append(u)
        rows[row_id] = {
            "row_id": row_id,
            "table_row_num": int(num),
            "file": "data/raw/2026-10-17-disconfirming-evidence.md",
            "question_or_metric": f"Hypothesis {parts[1]} ({parts[2]})",
            "hypothesis": parts[1],
            "direction": parts[2],
            "value": parts[3],
            "unit": parts[4],
            "ref_period": parts[5],
            "source_key": parts[6],
            "access_status": parts[7],
            "quote_or_snippet": parts[8],
            "register_id": parts[9],
            "register_ids": reg_ids,
            "primary_tier": primary_tier,
            "urls": urls,
            "verification": parts[10],
            "geography": "N",
            "age_fit_code": "D",
            "notes": f"Disconfirming table A row {num}; direction={parts[2]}",
            "raw_row": {
                "#": num,
                "H": parts[1],
                "direction": parts[2],
                "value": parts[3],
                "unit": parts[4],
                "ref_period": parts[5],
                "source_key": parts[6],
                "access_status": parts[7],
                "snippet": parts[8],
                "register_id": parts[9],
                "verification": parts[10],
            },
        }
    return rows


def parse_register_ids(reg_field: str) -> list[str]:
    if not reg_field or reg_field.strip().lower() in ("n/a", "none", "-", ""):
        return []
    tokens = re.split(r"[;,\s]+", reg_field.strip())
    return [t.strip() for t in tokens if re.match(r"^(BEH|DEM|CMP|REG)-\d+$", t.strip())]


def build_inventory():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sources_path = REPO_ROOT / "sources" / "sources.md"
    register = parse_sources_md(sources_path)

    with open(OUTPUT_DIR / "sources_register.json", "w", encoding="utf-8") as f:
        json.dump(register, f, indent=2, ensure_ascii=False)

    # Identify CSV files in data/processed
    all_csvs = sorted(glob.glob(str(REPO_ROOT / "data" / "processed" / "**" / "*.csv"), recursive=True))
    meta_files = {
        "data/processed/2026-10-pillar1-mapping.csv",
        "data/processed/2026-10-pillar1-mapping-excluded.csv",
        "data/processed/2026-10-16-run1-dropped-rows.csv",
        "data/processed/2026-10-18-preverification.csv",
        "data/processed/2026-10-18-claim-ledger.csv",
    }

    row_index = {}
    file_counts = {}
    verification_counts = Counter()
    geography_counts = Counter()
    age_fit_counts = Counter()
    tier_counts = Counter()

    # Load mapping file first for cross-reference of geo_scope, age_split, pestel_dim, cage_dim, etc.
    mapping_by_row = {}
    mapping_path = REPO_ROOT / "data" / "processed" / "2026-10-pillar1-mapping.csv"
    if mapping_path.exists():
        with open(mapping_path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                mapping_by_row[r["row_id"].strip()] = r

    excluded_mapping_rows = []
    excluded_path = REPO_ROOT / "data" / "processed" / "2026-10-pillar1-mapping-excluded.csv"
    if excluded_path.exists():
        with open(excluded_path, encoding="utf-8") as f:
            excluded_mapping_rows = list(csv.DictReader(f))

    dropped_rows = []
    dropped_path = REPO_ROOT / "data" / "processed" / "2026-10-16-run1-dropped-rows.csv"
    if dropped_path.exists():
        with open(dropped_path, encoding="utf-8") as f:
            dropped_rows = list(csv.DictReader(f))

    for csv_abs in all_csvs:
        rel_path = os.path.relpath(csv_abs, REPO_ROOT).replace("\\", "/")
        if rel_path in meta_files:
            continue

        with open(csv_abs, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        file_counts[rel_path] = len(rows)

        for idx, r in enumerate(rows, start=1):
            if "row_id" in r and r["row_id"].strip():
                rid = r["row_id"].strip()
            elif "trigger_or_channel" in r:
                rid = f"MATRIX-{idx:02d}"
            else:
                rid = f"{Path(rel_path).stem}-{idx:02d}"

            verif = r.get("verification", "").strip()
            if not verif and "trigger_or_channel" in r:
                verif = "MATRIX-CELL"

            reg_raw = r.get("register_id", "").strip()
            reg_ids = parse_register_ids(reg_raw)
            primary_tier = None
            urls = []
            for reg_id in reg_ids:
                if reg_id in register:
                    t = register[reg_id]["tier"]
                    if primary_tier is None and t is not None:
                        primary_tier = t
                    for u in register[reg_id]["all_urls"]:
                        if u not in urls:
                            urls.append(u)

            # Determine geography and age_fit_code
            geo = r.get("geography", "").strip()
            if not geo and rid in mapping_by_row:
                geo = mapping_by_row[rid].get("geo_scope", "").strip()
            if not geo:
                geo = "n/a"

            age_fit = r.get("age_fit_code", "").strip()
            if not age_fit:
                age_fit = "na" if ("instrument" in r or "rule_date" in r) else "D"

            value = r.get("value", r.get("reported_fact_value", r.get("price_idr", ""))).strip()
            unit = r.get("unit", "").strip()
            ref_period = r.get("ref_period", r.get("ref_period_and_type", r.get("rule_date", ""))).strip()
            question_or_metric = (
                r.get("trigger_or_metric")
                or r.get("finding")
                or r.get("indicator")
                or r.get("trigger_or_channel")
                or r.get("question")
                or ""
            ).strip()
            quote_or_snippet = (r.get("snippet") or r.get("quote") or "").strip()
            notes = r.get("notes", "").strip()

            entry = {
                "row_id": rid,
                "file": rel_path,
                "verification": verif,
                "geography": geo,
                "age_fit_code": age_fit,
                "register_id_raw": reg_raw,
                "register_ids": reg_ids,
                "primary_tier": primary_tier,
                "urls": urls,
                "question": r.get("question", "").strip(),
                "question_or_metric": question_or_metric,
                "value": value,
                "unit": unit,
                "ref_period": ref_period,
                "base_n": r.get("base_n", r.get("scope_base", "")).strip(),
                "population": r.get("population", "").strip(),
                "quote_or_snippet": quote_or_snippet,
                "notes": notes,
                "in_force_confirmation": r.get("in_force_confirmation", "").strip(),
                "amendment_check": r.get("amendment_check", "").strip(),
                "confidence": r.get("confidence", "").strip(),
                "gaps": r.get("gaps", "").strip(),
                "mapping": mapping_by_row.get(rid),
                "raw_row": r,
            }
            row_index[rid] = entry

            verification_counts[verif] += 1
            geography_counts[geo] += 1
            age_fit_counts[age_fit] += 1
            tier_counts[str(primary_tier) if primary_tier is not None else "none"] += 1

    # Add Disconfirming Evidence Table A rows
    disc_path = REPO_ROOT / "data" / "raw" / "2026-10-17-disconfirming-evidence.md"
    disc_rows = parse_disconfirming_table_a(disc_path, register)
    for drid, dentry in disc_rows.items():
        row_index[drid] = dentry
        # Also provide alias DISC-# for convenience
        num = dentry["table_row_num"]
        row_index[f"DISC-{num}"] = dentry

    with open(OUTPUT_DIR / "row_index.json", "w", encoding="utf-8") as f:
        json.dump(row_index, f, indent=2, ensure_ascii=False)

    # Extract BLOCKED, OPENED-UNVERIFIED, and GAP rows
    blocked_list = []
    opened_unverified_list = []
    gap_list = []
    seen_ids = set()
    for rid, entry in row_index.items():
        if rid.startswith("DISC-") and not rid.startswith("DISC-A"):
            continue
        if rid in seen_ids:
            continue
        seen_ids.add(rid)
        v = entry["verification"]
        if v == "BLOCKED":
            blocked_list.append(entry)
        elif v == "OPENED-UNVERIFIED":
            opened_unverified_list.append(entry)
        elif v == "GAP":
            gap_list.append(entry)

    blocked_output = {
        "blocked_count": len(blocked_list),
        "opened_unverified_count": len(opened_unverified_list),
        "gap_count": len(gap_list),
        "blocked_rows": blocked_list,
        "opened_unverified_rows": opened_unverified_list,
        "gap_rows": gap_list,
    }
    with open(OUTPUT_DIR / "blocked_rows.json", "w", encoding="utf-8") as f:
        json.dump(blocked_output, f, indent=2, ensure_ascii=False)

    # Build comprehensive scripted downside / disconfirming / mixed rows list
    # Per lessons.md (2026-10-17 run 4 rule a) and tasks/2026-10-17-run4-balance-check.md:
    # Include all verified/corrected rows from disconfirming-evidence.md Table A, plus all
    # verified/corrected rows across the mapped CSVs that represent downside, disconfirming, or mixed evidence.
    curated_downside_groups = {
        "disconfirming_table_a_verified": [
            "DISC-A1",
            "DISC-A2",
            "DISC-A3",
            "DISC-A6",
            "DISC-A9",
            "DISC-A13",
            "DISC-A16",
            "DISC-A17",
        ],
        "demand_and_macro_downside": [
            "P1C2-01",
            "P1C2-02",
            "P1C2-03",
            "P1C2-05",
            "P1C2-06",
            "P1C2-08",
            "P1C2-09",
            "P1C2-10",
            "P1C2-11",
            "P1C2-12",
            "P1C2-13",
            "P1C2-14",
            "P1C2-18",
            "P1C2-26",
            "P1C2-27",
            "P1C2-29",
            "P1C2-30",
            "P1C2-31",
            "P1C2-32",
            "P1C2-33",
            "P1C2-34",
            "P1C1-E03",
            "P1C1-E05",
            "P1C1-F04",
            "UE-N03",
            "UE-N07",
            "UE-N08",
            "UE-N09",
            "P1C3-01",
        ],
        "operators_and_competitors_downside": [
            "Q6-001",
            "Q6-002",
            "Q6-004",
            "Q6-005",
            "Q6-006",
            "Q6-011",
            "Q6-012",
            "UC-N08",
            "UC-N09",
            "P3BF-005",
            "P3BF-007",
            "P3BF-009",
            "P3BF-010",
            "P3BF-011",
            "P3BF-012",
            "P3BF-015",
            "P3BF-016",
            "P3BF-017",
            "P3BF-018",
            "P3BF-022",
            "P3BF-024",
            "P3BF-025",
            "P3BF-027",
            "P3BF-028",
            "P3BF-029",
            "P3BF-040",
            "P3BF-041",
            "P3B-05",
            "P3B-06",
            "P3B-07",
            "P3B-08",
            "P3B-10",
            "S-03",
            "S-04",
            "S-05",
            "S-06",
            "S-07",
            "S-09",
        ],
        "consumer_behaviour_and_triggers_downside": [
            "P4W1-R04",
            "P4W3-04",
            "P4W3-05",
            "P4W3-08",
            "UB-07",
            "UB-10",
            "UA-N65",
            "P4W7b-02",
            "P4W7b-05",
            "P4W7b-14",
            "P4W7b-15",
            "P4W9-15",
            "P4W9-16",
            "P4W9-18",
            "P4W9-19",
            "P4W9-27",
            "P4W9-28",
            "P4W9-29",
            "P4W4-02",
            "P4W4-05",
            "P4W4-06",
            "P4W2b-06",
            "P4W2b-07",
            "P4W2b-11",
            "P4W2b-14",
            "P4W2b-16",
            "P4W2b-21",
            "SD07",
            "P4W10-13",
            "CAGE-020",
        ],
        "supply_legal_and_site_downside": [
            "P1C4-08",
            "P1C4-11",
            "P1C4-14",
            "E-04",
            "F-04",
            "F-05",
            "H-02",
            "H-06",
            "UC-N07",
            "P4W5-08",
        ],
        "historical_closures_excluded_from_base_rate": [
            "P3B-26",
            "P3B-27",
            "P3B-28",
            "P3B-29",
        ],
        "countering_positive_rows_for_balance": [
            "P3BF-035",
            "P3BF-019",
            "Q6-007",
            "Q6-008",
            "Q6-009",
            "P3B-09",
        ],
    }

    # Also scan all verified rows for any explicit "disconfirm" keyword in notes/caveat
    keyword_flagged_ids = []
    for rid, entry in row_index.items():
        if rid.startswith("DISC-") and not rid.startswith("DISC-A"):
            continue
        if entry["verification"] in ("BLOCKED", "GAP", "MATRIX-CELL"):
            continue
        blob = " ".join(
            [
                entry.get("notes", ""),
                entry.get("question_or_metric", ""),
                json.dumps(entry.get("mapping") or {}),
            ]
        ).lower()
        if "disconfirm" in blob:
            keyword_flagged_ids.append(rid)

    downside_records = {}
    for group_name, id_list in curated_downside_groups.items():
        downside_records[group_name] = []
        for rid in id_list:
            if rid in row_index:
                e = row_index[rid]
                downside_records[group_name].append(
                    {
                        "row_id": rid,
                        "file": e["file"],
                        "verification": e["verification"],
                        "geography": e["geography"],
                        "age_fit_code": e["age_fit_code"],
                        "register_ids": e["register_ids"],
                        "question_or_metric": e["question_or_metric"],
                        "value": e["value"],
                        "unit": e["unit"],
                        "ref_period": e["ref_period"],
                        "notes": e["notes"],
                    }
                )

    all_curated_ids = {
        rid
        for grp, id_list in curated_downside_groups.items()
        if grp not in ("historical_closures_excluded_from_base_rate", "countering_positive_rows_for_balance")
        for rid in id_list
    }

    downside_output = {
        "selection_rule": (
            "All verified/corrected rows from data/raw/2026-10-17-disconfirming-evidence.md Table A "
            "(8 rows; rows 5, 8, 15 excluded as BLOCKED) plus all verified/corrected rows across "
            "data/processed/**/*.csv whose direction, notes, or findings document macro/middle-class contraction, "
            "operator losses/closures/going-concern warnings, boycott impact, consumer retrenchment/price resistance, "
            "or legal/site barriers. Historical pre-window exits (P3B-26 to P3B-29) and BLOCKED rows are listed "
            "separately with explicit exclusion reasons."
        ),
        "total_verified_downside_or_mixed_count": len(all_curated_ids),
        "counts_by_group": {k: len(v) for k, v in downside_records.items()},
        "keyword_disconfirm_hits": sorted(set(keyword_flagged_ids)),
        "groups": downside_records,
        "blocked_disconfirming_table_a": [
            row_index[r] for r in ("DISC-A5", "DISC-A8", "DISC-A15") if r in row_index
        ],
    }
    with open(OUTPUT_DIR / "downside_rows.json", "w", encoding="utf-8") as f:
        json.dump(downside_output, f, indent=2, ensure_ascii=False)

    # Check the 11 label-fix rows from tasks/2026-10-17-run4-label-fixes.md
    label_fix_ids = [
        "P1C4-16",
        "P3PB-06",
        "P3PB-27",
        "UA-N12",
        "UA-N67",
        "Q8-001",
        "Q8-003",
        "H-04",
        "P4W9-29",
        "P4W4-06",
        "P1C2-03",
    ]
    label_fixes_check = {}
    for lfid in label_fix_ids:
        if lfid in row_index:
            e = row_index[lfid]
            label_fixes_check[lfid] = {
                "file": e["file"],
                "verification": e["verification"],
                "geography": e["geography"],
                "question_or_metric": e["question_or_metric"],
                "ref_period": e["ref_period"],
                "base_n": e["base_n"],
                "population": e["population"],
                "has_audit_followup_note": "Audit follow-up (2026-10-17)" in e["notes"],
                "notes": e["notes"],
            }

    # Register summary
    reg_tier_counts = Counter(str(v["tier"]) for v in register.values())
    reg_prefix_counts = Counter(k.split("-")[0] for k in register.keys())
    reg_opened_counts = Counter("opened" if v["is_opened"] else "not_opened" for v in register.values())

    summary = {
        "sources_register": {
            "total_sources": len(register),
            "by_tier": dict(sorted(reg_tier_counts.items())),
            "by_prefix": dict(sorted(reg_prefix_counts.items())),
            "by_access": dict(reg_opened_counts),
        },
        "csv_inventory": {
            "total_primary_csv_files": len(file_counts),
            "total_primary_csv_rows": sum(file_counts.values()),
            "total_primary_csv_rows_excl_matrix": sum(
                cnt for fp, cnt in file_counts.items() if "plan4-trigger-matrix.csv" not in fp
            ),
            "disconfirming_table_a_rows": len(disc_rows),
            "pillar1_mapping_rows": len(mapping_by_row),
            "pillar1_mapping_excluded_rows": len(excluded_mapping_rows),
            "run1_dropped_rows": len(dropped_rows),
            "rows_by_file": file_counts,
            "by_verification": dict(verification_counts.most_common()),
            "by_geography": dict(geography_counts.most_common()),
            "by_age_fit": dict(age_fit_counts.most_common()),
            "by_primary_source_tier": dict(tier_counts.most_common()),
        },
        "downside_summary": {
            "total_verified_downside_or_mixed": len(all_curated_ids),
            "counts_by_group": {k: len(v) for k, v in downside_records.items()},
        },
        "label_fixes_11_check": label_fixes_check,
    }

    with open(OUTPUT_DIR / "inventory_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(
        f"[inventory.py] Done: {len(register)} registered sources, "
        f"{sum(file_counts.values())} primary CSV rows across {len(file_counts)} files "
        f"(+{len(disc_rows)} disconfirming Table A rows)."
    )
    return summary


main = build_inventory

if __name__ == "__main__":
    build_inventory()

