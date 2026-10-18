# CORSA Jakarta Quantitative Statistics Summary (`compute_stats.py`)

## 1. Price Ladder Brand Concentration (`data/processed/price-ladder.csv`)
- **Total rows:** 89 (67 with numeric `price_idr`, 22 blank range/band/promo rows)
- **Exact vs Approximate numeric rows:** 50 exact (`74.6%`), 17 approximate (`25.4%`: P3PR-025, P3PR-026, P3PR-027, P3PR-028, P3PR-029, P3PR-030, P3PB-23, P3PB-24, P3PB-25, P3PB-30, P3PB-31, P3PB-32, P3PB-33, P3PB-34, P3PB-35, P3PB-36, P3PB-37)
- **Top-3 Brand Concentration:** **83.6%** of all numeric rows come from just 3 brands (Burgreens, Pizza Marzano, Fore Coffee).

| Brand | Numeric Rows (n) | Share (%) | Exact Rows | Approx Rows | Categories Covered |
|---|---:|---:|---:|---:|---|
| Burgreens | 24 | 35.8% | 24 | 0 | bowl, coffee, functional_drink, pasta |
| Pizza Marzano | 18 | 26.9% | 18 | 0 | bowl, coffee, pasta |
| Fore Coffee | 14 | 20.9% | 7 | 7 | coffee |
| Pepper Lunch | 3 | 4.5% | 0 | 3 | pasta |
| Casa Pasta | 1 | 1.5% | 1 | 0 | pasta |
| Sky Pasta | 1 | 1.5% | 0 | 1 | pasta |
| Halo Pasta | 1 | 1.5% | 0 | 1 | pasta |
| Fish Streat | 1 | 1.5% | 0 | 1 | pasta |
| Fish Lab | 1 | 1.5% | 0 | 1 | pasta |
| Kopi Tuku | 1 | 1.5% | 0 | 1 | coffee |
| Tomoro Coffee | 1 | 1.5% | 0 | 1 | coffee |
| Kopi Kenangan | 1 | 1.5% | 0 | 1 | coffee |

## 2. Category Price Distributions — All Numeric vs Exact-Only (IDR)

| Category | Basis | n | Min | P25 | Median | Mean | P75 | IQR | Max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `coffee` | All Numeric | 23 | Rp 10,000 | Rp 24,500 | Rp 29,000 | Rp 27,913 | Rp 31,000 | Rp 6,500 | Rp 38,000 |
| `coffee` | Exact Only | 13 | Rp 24,000 | Rp 29,000 | Rp 30,000 | Rp 30,923 | Rp 33,000 | Rp 4,000 | Rp 38,000 |
| `pasta` | All Numeric | 20 | Rp 20,000 | Rp 52,250 | Rp 86,500 | Rp 73,950 | Rp 96,000 | Rp 43,750 | Rp 109,000 |
| `pasta` | Exact Only | 13 | Rp 20,000 | Rp 92,000 | Rp 95,000 | Rp 88,154 | Rp 105,000 | Rp 13,000 | Rp 109,000 |
| `bowl` | All Numeric | 15 | Rp 50,000 | Rp 57,000 | Rp 60,000 | Rp 66,133 | Rp 68,000 | Rp 11,000 | Rp 105,000 |
| `bowl` | Exact Only | 15 | Rp 50,000 | Rp 57,000 | Rp 60,000 | Rp 66,133 | Rp 68,000 | Rp 11,000 | Rp 105,000 |
| `functional_drink` | All Numeric | 9 | Rp 27,000 | Rp 35,000 | Rp 45,000 | Rp 42,444 | Rp 52,000 | Rp 17,000 | Rp 52,000 |
| `functional_drink` | Exact Only | 9 | Rp 27,000 | Rp 35,000 | Rp 45,000 | Rp 42,444 | Rp 52,000 | Rp 17,000 | Rp 52,000 |

## 3. Sub-Class (`item_class`) Price Distributions — All Numeric vs Exact-Only (IDR)

| Category | `item_class` | n (All / Exact) | Min (All) | P25 (All) | Median (All / Exact) | Mean (All) | P75 (All) | Max (All) | Brands |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `bowl` | `smoothie_bowl` | 3 / 3 | Rp 68,000 | Rp 68,000 | Rp 68,000 / Rp 68,000 | Rp 68,000 | Rp 68,000 | Rp 68,000 | Burgreens (3) |
| `bowl` | `salad_bowl` | 2 / 2 | Rp 65,000 | Rp 65,000 | Rp 65,000 / Rp 65,000 | Rp 65,000 | Rp 65,000 | Rp 65,000 | Burgreens (2) |
| `bowl` | `salad` | 5 / 5 | Rp 50,000 | Rp 60,000 | Rp 60,000 / Rp 60,000 | Rp 76,000 | Rp 105,000 | Rp 105,000 | Pizza Marzano (3), Burgreens (2) |
| `bowl` | `rice_bowl` | 5 / 5 | Rp 50,000 | Rp 55,000 | Rp 55,000 / Rp 55,000 | Rp 55,600 | Rp 59,000 | Rp 59,000 | Burgreens (5) |
| `functional_drink` | `protein_shake` | 3 / 3 | Rp 52,000 | Rp 52,000 | Rp 52,000 / Rp 52,000 | Rp 52,000 | Rp 52,000 | Rp 52,000 | Burgreens (3) |
| `functional_drink` | `smoothie` | 3 / 3 | Rp 45,000 | Rp 45,000 | Rp 45,000 / Rp 45,000 | Rp 45,667 | Rp 46,000 | Rp 47,000 | Burgreens (3) |
| `functional_drink` | `herbal_elixir` | 3 / 3 | Rp 27,000 | Rp 27,000 | Rp 27,000 / Rp 27,000 | Rp 29,667 | Rp 31,000 | Rp 35,000 | Burgreens (3) |
| `coffee` | `signature_coffee` | 6 / 2 | Rp 10,000 | Rp 19,250 | Rp 23,500 / Rp 28,000 | Rp 22,333 | Rp 26,250 | Rp 32,000 | Fore Coffee (2), Burgreens (1), Kopi Tuku (1), Tomoro Coffee (1), Kopi Kenangan (1) |
| `coffee` | `espresso` | 4 / 2 | Rp 22,000 | Rp 22,000 | Rp 23,500 / Rp 27,500 | Rp 24,750 | Rp 26,250 | Rp 30,000 | Fore Coffee (2), Burgreens (1), Pizza Marzano (1) |
| `pasta` | `pasta_main` | 12 / 12 | Rp 60,000 | Rp 92,000 | Rp 95,000 / Rp 95,000 | Rp 93,833 | Rp 106,000 | Rp 109,000 | Pizza Marzano (11), Burgreens (1) |
| `coffee` | `flavoured_americano` | 4 / 0 | Rp 29,000 | Rp 29,000 | Rp 29,000 / — | Rp 29,500 | Rp 29,500 | Rp 31,000 | Fore Coffee (4) |
| `coffee` | `americano` | 1 / 1 | Rp 35,000 | Rp 35,000 | Rp 35,000 / Rp 35,000 | Rp 35,000 | Rp 35,000 | Rp 35,000 | Pizza Marzano (1) |
| `coffee` | `latte` | 1 / 1 | Rp 38,000 | Rp 38,000 | Rp 38,000 / Rp 38,000 | Rp 38,000 | Rp 38,000 | Rp 38,000 | Pizza Marzano (1) |
| `coffee` | `cappuccino` | 1 / 1 | Rp 38,000 | Rp 38,000 | Rp 38,000 / Rp 38,000 | Rp 38,000 | Rp 38,000 | Rp 38,000 | Pizza Marzano (1) |
| `pasta` | `pasta_teppan_japanese_style` | 3 / 0 | Rp 74,000 | Rp 76,500 | Rp 79,000 / — | Rp 78,000 | Rp 80,000 | Rp 81,000 | Pepper Lunch (3) |
| `pasta` | `pasta_low_end_street` | 5 / 1 | Rp 20,000 | Rp 20,000 | Rp 25,000 / Rp 20,000 | Rp 23,800 | Rp 25,000 | Rp 29,000 | Casa Pasta (1), Sky Pasta (1), Halo Pasta (1), Fish Streat (1), Fish Lab (1) |
| `coffee` | `signature_latte` | 6 / 6 | Rp 29,000 | Rp 29,000 | Rp 29,000 / Rp 29,000 | Rp 30,000 | Rp 30,500 | Rp 33,000 | Fore Coffee (6) |

## 4. Target Corridor Demographics & Affordability Ratios
- **Ages 25–39 Population (2024 BPS):** Jakarta Pusat = `244,600` (`DEM-012`), Jakarta Selatan = `535,920` (`DEM-013`), Combined = **`780,520`**.
- **Monthly Per-Capita Prepared Food & Beverage Expenditure (2024 BPS):**
  - DKI Jakarta (`DEM-014`): `Rp 1,095,041` (`39.20%` of `Rp 2,793,654` food; `16.08%` of `Rp 6,809,757` total expenditure).
  - Jakarta Pusat (`DEM-015`): `Rp 1,105,632` (`44.66%` of `Rp 2,475,617` food; `20.21%` of `Rp 5,471,981` total expenditure).
  - Jakarta Selatan (`DEM-016`): `Rp 1,401,532` (`50.11%` of `Rp 2,796,815` food; `19.45%` of `Rp 7,205,368` total expenditure).
- **CORSA Model v0.6 Ticket vs Local Prepared-Food Budgets:**
  - Model Base average in-store guest spend (`Revenue!E16`, `Scenarios!D8`): `Rp 103,375` net (`Rp 113,713` gross with 10% PBJT, `Inputs!F17`).
  - Model Base lunch cover (`Revenue!D9`, `Inputs!F36`): `Rp 120,000` net (`Rp 132,000` gross with 10% PBJT); dinner cover (`Revenue!D11`, `Inputs!F40`): `Rp 140,000` net (`Rp 154,000` gross).
  - **1 average in-store visit (`Rp 113,713` gross)** = **`10.38%`** of DKI Jakarta average monthly prepared-food spend (`Rp 1,095,041`) and **`8.11%`** of Jakarta Selatan average monthly prepared-food spend (`Rp 1,401,532`).
  - **1 lunch visit (`Rp 132,000` gross)** = **`12.05%`** of DKI Jakarta and **`9.42%`** of Jakarta Selatan monthly prepared-food spend; **1 dinner visit (`Rp 154,000` gross)** = **`10.99%`** of Jakarta Selatan monthly prepared-food spend.
  - **4 average visits/month (`Rp 454,852` gross)** consumes **`32.45%`** of an average Jakarta Selatan resident's entire monthly prepared-food budget (`12.3` visits would exhaust `100%` of it).

## 5. CAGE Claim Register Summary (`reports/2026-10-17-cage-switzerland-jakarta.md`)
- **Total claims registered:** 174 (`verified`: 161, `corrected`: 5, `unverified`: 8)
