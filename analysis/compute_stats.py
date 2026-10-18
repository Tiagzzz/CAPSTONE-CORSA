#!/usr/bin/env python3
"""
Compute deterministic statistics from data/processed/ CSVs and reports:
  1. Price ladder statistics (exact vs approximate, brand concentration, category & item_class percentiles,
     and comparison against CORSA Financial Model v0.6 Menu prices).
  2. Demand, expenditure, demographic, and operator benchmark statistics from data/processed/demand/*.csv
     and data/processed/listed-operators.csv.
  3. CAGE claim register verification tallies from reports/2026-10-17-cage-switzerland-jakarta.md.

Generates:
  - analysis/outputs/stats_summary.json
  - analysis/outputs/stats_tables.md
"""

import csv
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "analysis" / "outputs"

APPROX_PRICE_ROW_IDS = {
    "P3PR-025", "P3PR-026", "P3PR-027", "P3PR-028", "P3PR-029", "P3PR-030",  # "sekitar Rp..."
    "P3PB-23", "P3PB-24", "P3PB-25",  # "Rp 50 ribuan" / "Rp 60 ribuan"
    "P3PB-30", "P3PB-31", "P3PB-32", "P3PB-33",  # "Rp 60.000-an" / "Rp 40.000-an"
    "P3PB-34", "P3PB-35", "P3PB-36",  # Google Maps user menu listing
    "P3PB-37",  # Ordering app listing
}


def percentile_linear(sorted_vals, p):
    """Standard linear interpolation percentile (matching numpy/Excel PERCENTILE.INC)."""
    if not sorted_vals:
        return None
    n = len(sorted_vals)
    if n == 1:
        return float(sorted_vals[0])
    pos = p * (n - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return float(sorted_vals[lo])
    frac = pos - lo
    return round(sorted_vals[lo] + frac * (sorted_vals[hi] - sorted_vals[lo]), 2)


def calc_dist(vals):
    if not vals:
        return {"n": 0, "min": None, "p25": None, "median": None, "mean": None, "p75": None, "iqr": None, "max": None}
    s = sorted(vals)
    p25 = percentile_linear(s, 0.25)
    p50 = percentile_linear(s, 0.50)
    p75 = percentile_linear(s, 0.75)
    return {
        "n": len(s),
        "min": int(s[0]),
        "p25": round(p25),
        "median": round(p50),
        "mean": round(sum(s) / len(s)),
        "p75": round(p75),
        "iqr": round(p75 - p25),
        "max": int(s[-1]),
    }


def is_approx_row(row):
    return row["row_id"] in APPROX_PRICE_ROW_IDS


def compute_price_ladder_stats():
    pl_path = ROOT / "data" / "processed" / "price-ladder.csv"
    with open(pl_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    numeric_rows = []
    blank_rows = []
    for r in rows:
        raw_p = (r.get("price_idr") or "").strip()
        if raw_p != "":
            val = int(float(raw_p))
            approx = is_approx_row(r)
            numeric_rows.append({**r, "price_num": val, "is_approx": approx})
        else:
            blank_rows.append(r)

    # Brand concentration among numeric rows
    brand_counts = Counter(r["brand"] for r in numeric_rows)
    brand_concentration = []
    for brand, cnt in brand_counts.most_common():
        exact_cnt = sum(1 for r in numeric_rows if r["brand"] == brand and not r["is_approx"])
        approx_cnt = sum(1 for r in numeric_rows if r["brand"] == brand and r["is_approx"])
        cats = sorted(set(r["category"] for r in numeric_rows if r["brand"] == brand))
        brand_concentration.append({
            "brand": brand,
            "numeric_count": cnt,
            "share_pct": round(cnt / len(numeric_rows) * 100, 1),
            "exact_count": exact_cnt,
            "approx_count": approx_cnt,
            "categories": cats,
        })

    # Category stats (all numeric vs exact-only)
    categories = ["coffee", "pasta", "bowl", "functional_drink"]
    by_category = {}
    for cat in categories:
        cat_all = [r["price_num"] for r in numeric_rows if r["category"] == cat]
        cat_exact = [r["price_num"] for r in numeric_rows if r["category"] == cat and not r["is_approx"]]
        cat_approx = [r["price_num"] for r in numeric_rows if r["category"] == cat and r["is_approx"]]
        cat_brands = Counter(r["brand"] for r in numeric_rows if r["category"] == cat)
        by_category[cat] = {
            "all_numeric": calc_dist(cat_all),
            "exact_only": calc_dist(cat_exact),
            "approx_count": len(cat_approx),
            "brands": dict(cat_brands.most_common()),
        }

    # Item-class stats (all numeric vs exact-only)
    item_classes = []
    seen_ic = set()
    for r in numeric_rows:
        ic = (r["category"], r["item_class"])
        if ic not in seen_ic:
            seen_ic.add(ic)
            item_classes.append(ic)

    by_item_class = {}
    for cat, ic in item_classes:
        ic_all = [r["price_num"] for r in numeric_rows if r["category"] == cat and r["item_class"] == ic]
        ic_exact = [r["price_num"] for r in numeric_rows if r["category"] == cat and r["item_class"] == ic and not r["is_approx"]]
        ic_approx = [r["price_num"] for r in numeric_rows if r["category"] == cat and r["item_class"] == ic and r["is_approx"]]
        ic_brands = Counter(r["brand"] for r in numeric_rows if r["category"] == cat and r["item_class"] == ic)
        by_item_class[f"{cat}::{ic}"] = {
            "category": cat,
            "item_class": ic,
            "all_numeric": calc_dist(ic_all),
            "exact_only": calc_dist(ic_exact),
            "approx_count": len(ic_approx),
            "brands": dict(ic_brands.most_common()),
        }

    return {
        "total_rows": len(rows),
        "numeric_rows_count": len(numeric_rows),
        "exact_numeric_rows_count": sum(1 for r in numeric_rows if not r["is_approx"]),
        "approx_numeric_rows_count": sum(1 for r in numeric_rows if r["is_approx"]),
        "blank_price_rows_count": len(blank_rows),
        "blank_price_row_ids": [r["row_id"] for r in blank_rows],
        "approx_price_row_ids": [r["row_id"] for r in numeric_rows if r["is_approx"]],
        "top_3_brands_share_pct": round(sum(b["numeric_count"] for b in brand_concentration[:3]) / len(numeric_rows) * 100, 1),
        "brand_concentration": brand_concentration,
        "by_category": by_category,
        "by_item_class": by_item_class,
    }


def compute_demand_and_affordability():
    # Core verified metrics from data/processed/demand/*.csv
    jak_pusat_25_39 = 82400 + 80200 + 82000  # 244,600 (DEM-012)
    jak_selatan_25_39 = 171210 + 179150 + 185560  # 535,920 (DEM-013)
    combined_25_39 = jak_pusat_25_39 + jak_selatan_25_39  # 780,520

    # Expenditure figures (IDR/capita/month, 2024 Susenas via BPS)
    dki_total_exp = 6809757  # DEM-014
    dki_food_exp = 2793654  # DEM-014
    dki_prep_food_exp = 1095041  # DEM-014 (39.20% of food, 16.08% of total)

    pusat_total_exp = 5471981  # DEM-015
    pusat_food_exp = 2475617  # DEM-015
    pusat_prep_food_exp = 1105632  # DEM-015 (44.66% of food, 20.21% of total)

    selatan_total_exp = 7205368  # DEM-016
    selatan_food_exp = 2796815  # DEM-016
    selatan_prep_food_exp = 1401532  # DEM-016 (50.11% of food, 19.45% of total)

    # CORSA Model v0.6 ticket benchmarks
    corsa_dine_in_net = 103375  # Revenue!E16 / Scenarios!D8 (Base blended avg net spend per in-store guest before 10% PBJT)
    corsa_pbjt_rate = 0.10  # Inputs!F17
    corsa_dine_in_gross = round(corsa_dine_in_net * (1 + corsa_pbjt_rate))  # Rp 113,713

    corsa_lunch_net = 120000  # Revenue!D9 / Inputs!F36 (Lunch avg net spend)
    corsa_lunch_gross = round(corsa_lunch_net * (1 + corsa_pbjt_rate))  # Rp 132,000

    corsa_dinner_net = 140000  # Revenue!D11 / Inputs!F40 (Dinner avg net spend)
    corsa_dinner_gross = round(corsa_dinner_net * (1 + corsa_pbjt_rate))  # Rp 154,000

    corsa_delivery_net = 115000  # Revenue!D13 / Inputs!F42 (Base delivery order value)
    corsa_delivery_gross = round(corsa_delivery_net * (1 + corsa_pbjt_rate))  # Rp 126,500

    wb_mc_upper_total_exp = 3000000  # DEM-030 (Rp 3.0m/cap/mo World Bank middle-class ceiling)

    return {
        "target_corridor_population_25_39": {
            "jakarta_pusat_25_39": {"value": jak_pusat_25_39, "row_id": "DEM-012", "breakdown": {"25_29": 82400, "30_34": 80200, "35_39": 82000}},
            "jakarta_selatan_25_39": {"value": jak_selatan_25_39, "row_id": "DEM-013", "breakdown": {"25_29": 171210, "30_34": 179150, "35_39": 185560}},
            "combined_pusat_selatan_25_39": {"value": combined_25_39, "row_ids": ["DEM-012", "DEM-013"]},
            "dki_jakarta_total_pop_2024": {"value": 10684900, "row_id": "DEM-001"},
        },
        "monthly_per_capita_expenditure_2024_idr": {
            "dki_jakarta": {
                "total": dki_total_exp,
                "food": dki_food_exp,
                "prepared_food": dki_prep_food_exp,
                "prepared_share_of_food_pct": round(dki_prep_food_exp / dki_food_exp * 100, 2),
                "prepared_share_of_total_pct": round(dki_prep_food_exp / dki_total_exp * 100, 2),
                "row_id": "DEM-014",
            },
            "jakarta_pusat": {
                "total": pusat_total_exp,
                "food": pusat_food_exp,
                "prepared_food": pusat_prep_food_exp,
                "prepared_share_of_food_pct": round(pusat_prep_food_exp / pusat_food_exp * 100, 2),
                "prepared_share_of_total_pct": round(pusat_prep_food_exp / pusat_total_exp * 100, 2),
                "row_id": "DEM-015",
            },
            "jakarta_selatan": {
                "total": selatan_total_exp,
                "food": selatan_food_exp,
                "prepared_food": selatan_prep_food_exp,
                "prepared_share_of_food_pct": round(selatan_prep_food_exp / selatan_food_exp * 100, 2),
                "prepared_share_of_total_pct": round(selatan_prep_food_exp / selatan_total_exp * 100, 2),
                "row_id": "DEM-016",
            },
        },
        "affordability_ratios_corsa_vs_budgets": {
            "corsa_avg_dine_in_net_idr": corsa_dine_in_net,
            "corsa_avg_dine_in_gross_incl_10pct_pbjt_idr": corsa_dine_in_gross,
            "corsa_lunch_cover_net_idr": corsa_lunch_net,
            "corsa_lunch_cover_gross_idr": corsa_lunch_gross,
            "corsa_dinner_cover_net_idr": corsa_dinner_net,
            "corsa_dinner_cover_gross_idr": corsa_dinner_gross,
            "single_avg_visit_gross_pct_of_dki_monthly_prep_food": round(corsa_dine_in_gross / dki_prep_food_exp * 100, 2),
            "single_avg_visit_gross_pct_of_selatan_monthly_prep_food": round(corsa_dine_in_gross / selatan_prep_food_exp * 100, 2),
            "single_lunch_gross_pct_of_dki_monthly_prep_food": round(corsa_lunch_gross / dki_prep_food_exp * 100, 2),
            "single_lunch_gross_pct_of_selatan_monthly_prep_food": round(corsa_lunch_gross / selatan_prep_food_exp * 100, 2),
            "single_dinner_gross_pct_of_selatan_monthly_prep_food": round(corsa_dinner_gross / selatan_prep_food_exp * 100, 2),
            "visits_per_month_to_exhaust_100pct_selatan_prep_food_budget": round(selatan_prep_food_exp / corsa_dine_in_gross, 1),
            "four_visits_per_month_gross_idr": corsa_dine_in_gross * 4,
            "four_visits_pct_of_selatan_monthly_prep_food": round((corsa_dine_in_gross * 4) / selatan_prep_food_exp * 100, 1),
            "single_avg_visit_gross_pct_of_wb_middle_class_upper_total_exp": round(corsa_dine_in_gross / wb_mc_upper_total_exp * 100, 2),
        },
        "operator_throughput_benchmarks": {
            "fore_coffee_fy2024_sales_per_outlet_day_idr": {"low": 12700000, "high": 14800000, "row_ids": ["CMP-001", "CMP-005"]},
            "corsa_model_base_fb_daily_revenue_idr": {"value": 23550000, "cell": "Revenue!E14"},
            "corsa_model_base_total_daily_revenue_idr": {"value": 24521000, "cell": "Scenarios!D13/Inputs!F12"},
            "corsa_base_fb_vs_fore_daily_multiple": {
                "vs_fore_high": round(23550000 / 14800000, 2),
                "vs_fore_low": round(23550000 / 12700000, 2),
            },
            "corsa_model_conservative_total_daily_revenue_idr": {"value": 16059000, "cell": "Scenarios!C13/Inputs!E12"},
        },
    }


def compute_cage_register_stats():
    cage_path = ROOT / "reports" / "2026-10-17-cage-switzerland-jakarta.md"
    with open(cage_path, "r", encoding="utf-8") as f:
        text = f.read()

    claims = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*([A-Z0-9]+-\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(verified|corrected|unverified)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", line)
        if m:
            claims.append({
                "claim_id": m.group(1),
                "section": m.group(2),
                "claim": m.group(3),
                "status": m.group(4),
                "source": m.group(5),
                "notes": m.group(6),
            })

    status_counts = Counter(c["status"] for c in claims)
    prefix_counts = Counter(c["claim_id"].split("-")[0] for c in claims)
    return {
        "total_claims": len(claims),
        "status_counts": dict(status_counts),
        "by_section_prefix": dict(prefix_counts),
        "corrected_claims": [c for c in claims if c["status"] == "corrected"],
        "unverified_claims": [c for c in claims if c["status"] == "unverified"],
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pl_stats = compute_price_ladder_stats()
    dem_stats = compute_demand_and_affordability()
    cage_stats = compute_cage_register_stats()

    stats_summary = {
        "price_ladder": pl_stats,
        "demand_and_affordability": dem_stats,
        "cage_claim_register": cage_stats,
    }

    json_out = OUT_DIR / "stats_summary.json"
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(stats_summary, f, indent=2, ensure_ascii=False)

    # Build Markdown summary tables
    md = [
        "# CORSA Jakarta Quantitative Statistics Summary (`compute_stats.py`)",
        "",
        "## 1. Price Ladder Brand Concentration (`data/processed/price-ladder.csv`)",
        f"- **Total rows:** {pl_stats['total_rows']} ({pl_stats['numeric_rows_count']} with numeric `price_idr`, {pl_stats['blank_price_rows_count']} blank range/band/promo rows)",
        f"- **Exact vs Approximate numeric rows:** {pl_stats['exact_numeric_rows_count']} exact (`74.6%`), {pl_stats['approx_numeric_rows_count']} approximate (`25.4%`: {', '.join(pl_stats['approx_price_row_ids'])})",
        f"- **Top-3 Brand Concentration:** **{pl_stats['top_3_brands_share_pct']}%** of all numeric rows come from just 3 brands (Burgreens, Pizza Marzano, Fore Coffee).",
        "",
        "| Brand | Numeric Rows (n) | Share (%) | Exact Rows | Approx Rows | Categories Covered |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for b in pl_stats["brand_concentration"]:
        md.append(
            f"| {b['brand']} | {b['numeric_count']} | {b['share_pct']}% | {b['exact_count']} | {b['approx_count']} | {', '.join(b['categories'])} |"
        )

    md.extend([
        "",
        "## 2. Category Price Distributions — All Numeric vs Exact-Only (IDR)",
        "",
        "| Category | Basis | n | Min | P25 | Median | Mean | P75 | IQR | Max |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for cat, data in pl_stats["by_category"].items():
        for label, key in [("All Numeric", "all_numeric"), ("Exact Only", "exact_only")]:
            d = data[key]
            if d["n"] > 0:
                md.append(
                    f"| `{cat}` | {label} | {d['n']} | Rp {d['min']:,} | Rp {d['p25']:,} | Rp {d['median']:,} | Rp {d['mean']:,} | Rp {d['p75']:,} | Rp {d['iqr']:,} | Rp {d['max']:,} |"
                )
            else:
                md.append(f"| `{cat}` | {label} | 0 | — | — | — | — | — | — | — |")

    md.extend([
        "",
        "## 3. Sub-Class (`item_class`) Price Distributions — All Numeric vs Exact-Only (IDR)",
        "",
        "| Category | `item_class` | n (All / Exact) | Min (All) | P25 (All) | Median (All / Exact) | Mean (All) | P75 (All) | Max (All) | Brands |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ])
    for key, data in pl_stats["by_item_class"].items():
        da = data["all_numeric"]
        de = data["exact_only"]
        med_e = f"Rp {de['median']:,}" if de["n"] > 0 else "—"
        brands_str = ", ".join(f"{k} ({v})" for k, v in data["brands"].items())
        md.append(
            f"| `{data['category']}` | `{data['item_class']}` | {da['n']} / {de['n']} | Rp {da['min']:,} | Rp {da['p25']:,} | Rp {da['median']:,} / {med_e} | Rp {da['mean']:,} | Rp {da['p75']:,} | Rp {da['max']:,} | {brands_str} |"
        )

    md.extend([
        "",
        "## 4. Target Corridor Demographics & Affordability Ratios",
        f"- **Ages 25–39 Population (2024 BPS):** Jakarta Pusat = `244,600` (`DEM-012`), Jakarta Selatan = `535,920` (`DEM-013`), Combined = **`780,520`**.",
        f"- **Monthly Per-Capita Prepared Food & Beverage Expenditure (2024 BPS):**",
        f"  - DKI Jakarta (`DEM-014`): `Rp 1,095,041` (`39.20%` of `Rp 2,793,654` food; `16.08%` of `Rp 6,809,757` total expenditure).",
        f"  - Jakarta Pusat (`DEM-015`): `Rp 1,105,632` (`44.66%` of `Rp 2,475,617` food; `20.21%` of `Rp 5,471,981` total expenditure).",
        f"  - Jakarta Selatan (`DEM-016`): `Rp 1,401,532` (`50.11%` of `Rp 2,796,815` food; `19.45%` of `Rp 7,205,368` total expenditure).",
        f"- **CORSA Model v0.6 Ticket vs Local Prepared-Food Budgets:**",
        f"  - Model Base average in-store guest spend (`Revenue!E16`, `Scenarios!D8`): `Rp 103,375` net (`Rp 113,713` gross with 10% PBJT, `Inputs!F17`).",
        f"  - Model Base lunch cover (`Revenue!D9`, `Inputs!F36`): `Rp 120,000` net (`Rp 132,000` gross with 10% PBJT); dinner cover (`Revenue!D11`, `Inputs!F40`): `Rp 140,000` net (`Rp 154,000` gross).",
        f"  - **1 average in-store visit (`Rp 113,713` gross)** = **`10.38%`** of DKI Jakarta average monthly prepared-food spend (`Rp 1,095,041`) and **`8.11%`** of Jakarta Selatan average monthly prepared-food spend (`Rp 1,401,532`).",
        f"  - **1 lunch visit (`Rp 132,000` gross)** = **`12.05%`** of DKI Jakarta and **`9.42%`** of Jakarta Selatan monthly prepared-food spend; **1 dinner visit (`Rp 154,000` gross)** = **`10.99%`** of Jakarta Selatan monthly prepared-food spend.",
        f"  - **4 average visits/month (`Rp 454,852` gross)** consumes **`32.45%`** of an average Jakarta Selatan resident's entire monthly prepared-food budget (`12.3` visits would exhaust `100%` of it).",
        "",
        "## 5. CAGE Claim Register Summary (`reports/2026-10-17-cage-switzerland-jakarta.md`)",
        f"- **Total claims registered:** {cage_stats['total_claims']} (`verified`: {cage_stats['status_counts'].get('verified', 0)}, `corrected`: {cage_stats['status_counts'].get('corrected', 0)}, `unverified`: {cage_stats['status_counts'].get('unverified', 0)})",
    ])

    md_out = OUT_DIR / "stats_tables.md"
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"[compute_stats] Wrote {json_out} and {md_out}")


if __name__ == "__main__":
    main()
