# CORSA Jakarta Financial Model v0.6 — Extracted Figures & Cell Citations

- **Source file:** `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx`
- **Sheets (20):** README, Dashboard, Inputs, Rent_Data, Location, Menu, Revenue, Staffing, OPEX, CAPEX (Buy), CAPEX (Rent), Funding, Scenarios, PnL_Monthly, Annual, Sensitivity, MonteCarlo, Sources, Research_Tracker, Methods
- **Active Scenario Switch:** `Inputs!D4 = 2` (`Inputs!E4 = "Base"`)
- **Active CAPEX Financing Switch:** `Inputs!H4 = 2` (`Inputs!I4 = "Lease – CAPEX (Rent)"`)

## 1. Structural Completeness & Horizon Audit (`PnL_Monthly`, `Annual`, `Dashboard`, `Research_Tracker`)

- **`PnL_Monthly` horizon truncation:** Only **13 of 60 months** are populated (`PnL_Monthly!C4:O53`, Months 1–13 = Jul 2027 – Jul 2028). Columns `P` through `BJ` (Months 14–60) are completely blank (`PnL_Monthly!P4:BJ53`).
- **`Annual` distortion (`Annual!A4:H32`):**
  - Year 1 (`Annual!C5:C19`) sums operating year 1 (Months 1–12): Revenue = `Rp 7,295,392,080` (`CHF 337,750`, `Annual!C21`), EBITDA = `Rp 730,264,586` (`CHF 33,809`, `Annual!C22`), Net Income = `Rp 293,511,415` (`Annual!C16`), Project FCF = `Rp 1,100,769,940` (`Annual!C17`), Closing Cash = `Rp 1,914,702,149` (`Annual!C19`).
  - Year 2 (`Annual!D5:D19`) sums operating year 2 (Months 13–24), where only Month 13 (`PnL_Monthly!O`) is populated: Revenue = `Rp 765,055,200` (`CHF 35,419`), EBITDA = `Rp 136,829,613` (`CHF 6,335`), Project FCF = `Rp 113,216,510`.
  - Years 3, 4, and 5 (`Annual!E5:G19`) evaluate to **`0`** across all revenue, cost, EBITDA, and operating cash-flow lines (only `Annual!G29` has `Rp 75,548,438` from the refundable security deposit).
- **Invalidated `Dashboard` multi-year metrics:**
  - `Dashboard!B17:C17` (Year-3 EBITDA) = `Rp 0` / `CHF 0` (references `Annual!E11`).
  - `Dashboard!B19:C19` & `Annual!C31:D31` (NPV of 5-year project cash flows at 15% discount rate) = `Rp -3,185,886,005` / `CHF -147,495`.
  - `Dashboard!B25` (Payback month, full model) = `> 60 months`.
  - `Dashboard!B26` & `Annual!C30` (Project IRR, 5 yrs) = `-46.9%`.
  - `Dashboard!B18:C18` (Lowest cash balance over 60 months) = `Rp 794,813,727` / `CHF 36,797` (Month 1 cash balance in `PnL_Monthly!C48`, ignoring unpopulated Months 14–60).
- **`Research_Tracker` status (`Research_Tracker!A5:F17`):** 13 rows — **5 `Placeholder`**, **4 `Desk`**, **4 `Model ready`**.

## 2. Side-by-Side Scenario Table (`Scenarios!A6:G56`, Saved Lease Mode `Inputs!H4 = 2`)

| Row | Metric | Unit | Conservative (`C`) | Base (`D`) | Optimistic (`E`) | Cell Reference |
|---:|---|---|---:|---:|---:|---|
| 6 | Guests per day (in-store) | # | 155 | 200 | 255 | `Scenarios!C6:E6` |
| 7 | In-store revenue per day | IDR | Rp 14,400,000 | Rp 20,675,000 | Rp 29,550,000 | `Scenarios!C7:E7` |
| 8 | Avg net spend per guest | IDR | Rp 92,903 | Rp 103,375 | Rp 115,882 | `Scenarios!C8:E8` |
| 9 | Delivery revenue per day | IDR | Rp 1,500,000 | Rp 2,875,000 | Rp 4,550,000 | `Scenarios!C9:E9` |
| 10 | F&B revenue per month | IDR | Rp 477,000,000 | Rp 706,500,000 | Rp 1,023,000,000 | `Scenarios!C10:E10` |
| 11 | Events & B2B | IDR | Rp 0 | Rp 15,000,000 | Rp 25,000,000 | `Scenarios!C11:E11` |
| 12 | Retail | IDR | Rp 4,770,000 | Rp 14,130,000 | Rp 35,805,000 | `Scenarios!C12:E12` |
| 13 | TOTAL REVENUE / MONTH | IDR | Rp 481,770,000 | Rp 735,630,000 | Rp 1,083,805,000 | `Scenarios!C13:E13` |
| 14 | Total revenue / year | CHF | CHF 282,012 | CHF 408,683 | CHF 578,029 | `Scenarios!C14:E14` |
| 16 | COGS (F&B + events + retail) | IDR | Rp 153,668,704 | Rp 215,191,146 | Rp 297,680,714 | `Scenarios!C16:E16` |
| 17 | Packaging | IDR | Rp 10,476,000 | Rp 13,616,250 | Rp 16,098,000 | `Scenarios!C17:E17` |
| 18 | Waste & spoilage | IDR | Rp 9,540,000 | Rp 10,597,500 | Rp 10,230,000 | `Scenarios!C18:E18` |
| 19 | Delivery commission (+VAT on fee) | IDR | Rp 13,986,000 | Rp 22,019,625 | Rp 30,303,000 | `Scenarios!C19:E19` |
| 20 | Payment fees | IDR | Rp 6,551,550 | Rp 7,792,560 | Rp 8,525,745 | `Scenarios!C20:E20` |
| 21 | Marketing, maintenance, misc., royalty | IDR | Rp 36,132,750 | Rp 40,459,650 | Rp 43,352,200 | `Scenarios!C21:E21` |
| 22 | Total variable costs | IDR | Rp 230,355,004 | Rp 309,676,731 | Rp 406,189,659 | `Scenarios!C22:E22` |
| 23 | Contribution margin | IDR | Rp 251,414,996 | Rp 425,953,269 | Rp 677,615,341 | `Scenarios!C23:E23` |
| 24 | Contribution margin % | % | 52.2% | 57.9% | 62.5% | `Scenarios!C24:E24` |
| 26 | Staff (incl. BPJS, THR, benefits) | IDR | Rp 185,573,283 | Rp 166,907,330 | Rp 161,881,030 | `Scenarios!C26:E26` |
| 27 | Rent (incl. gross-up) | IDR | Rp 70,364,536 | Rp 37,774,219 | Rp 30,774,208 | `Scenarios!C27:E27` |
| 28 | Service charge / CAM | IDR | Rp 0 | Rp 0 | Rp 0 | `Scenarios!C28:E28` |
| 29 | Utilities | IDR | Rp 23,891,700 | Rp 19,002,300 | Rp 15,835,250 | `Scenarios!C29:E29` |
| 30 | Fixed overheads (mgmt, accounting, insurance…) + equipment payments in Lease mode | IDR | Rp 79,483,150 | Rp 67,483,150 | Rp 57,483,150 | `Scenarios!C30:E30` |
| 31 | Total fixed costs | IDR | Rp 359,312,669 | Rp 291,166,998 | Rp 265,973,637 | `Scenarios!C31:E31` |
| 32 | Fixed costs excl. rent & service charge | IDR | Rp 288,948,133 | Rp 253,392,780 | Rp 235,199,430 | `Scenarios!C32:E32` |
| 34 | EBITDA / month (steady state) | IDR | Rp -107,897,672 | Rp 134,786,270 | Rp 411,641,704 | `Scenarios!C34:E34` |
| 35 | EBITDA margin | % | -22.4% | 18.3% | 38.0% | `Scenarios!C35:E35` |
| 36 | EBITDA / year | CHF | CHF -63,160 | CHF 74,881 | CHF 219,542 | `Scenarios!C36:E36` |
| 37 | Food & beverage cost % of revenue | % | 31.9% | 29.3% | 27.5% | `Scenarios!C37:E37` |
| 38 | Staff cost % of revenue | % | 38.5% | 22.7% | 14.9% | `Scenarios!C38:E38` |
| 39 | Prime cost % (COGS + staff) | % | 70.4% | 51.9% | 42.4% | `Scenarios!C39:E39` |
| 40 | Occupancy cost % (rent + SC) | % | 14.6% | 5.1% | 2.8% | `Scenarios!C40:E40` |
| 42 | Break-even revenue / month | IDR | Rp 688,527,204 | Rp 502,851,357 | Rp 425,408,843 | `Scenarios!C42:E42` |
| 43 | Break-even revenue / trading day | IDR | Rp 22,950,907 | Rp 16,761,712 | Rp 14,180,295 | `Scenarios!C43:E43` |
| 44 | Break-even revenue / day | CHF | CHF 1,120 | CHF 776 | CHF 630 | `Scenarios!C44:E44` |
| 45 | Break-even guests / day (at current channel mix) | # | 221.52 | 136.71 | 100.09 | `Scenarios!C45:E45` |
| 46 | Margin of safety (revenue above break-even) | % | -42.9% | 31.6% | 60.7% | `Scenarios!C46:E46` |
| 48 | Hard costs (incl. VAT, cost factor) | IDR | Rp 2,062,966,420 | Rp 1,793,883,844 | Rp 1,704,189,652 | `Scenarios!C48:E48` |
| 49 | Soft costs incl. pre-opening payroll | IDR | Rp 955,459,924 | Rp 844,007,330 | Rp 798,510,772 | `Scenarios!C49:E49` |
| 50 | Contingency | IDR | Rp 452,763,952 | Rp 263,789,117 | Rp 187,702,532 | `Scenarios!C50:E50` |
| 51 | Lease (fit-out rent, prepayment, deposit) | IDR | Rp 2,110,936,079 | Rp 604,387,500 | Rp 430,838,906 | `Scenarios!C51:E51` |
| 52 | Working-capital reserve | IDR | Rp 866,844,398 | Rp 760,178,339 | Rp 470,398,859 | `Scenarios!C52:E52` |
| 53 | TOTAL INVESTMENT | IDR | Rp 6,448,970,773 | Rp 4,266,246,130 | Rp 3,591,640,721 | `Scenarios!C53:E53` |
| 54 | Total investment | CHF | CHF 314,584 | CHF 197,511 | CHF 159,628 | `Scenarios!C54:E54` |
| 55 | Gap vs founder equity (+ = need bank/extra equity) | CHF | CHF 114,584 | CHF -2,489 | CHF -40,372 | `Scenarios!C55:E55` |
| 56 | Simple payback (years) = investment ÷ annual EBITDA after tax | years | never | 3.38 | 0.93 | `Scenarios!C56:E56` |

## 3. Lease Mode (`Inputs!H4 = 2`, Saved) vs Buy Mode (`Inputs!H4 = 1`, Computed) Comparison

| Metric | Conservative (Lease / Buy) | Base (Lease / Buy) | Optimistic (Lease / Buy) | Citations |
|---|---:|---:|---:|---|
| Steady-State Monthly Revenue | Rp 481,770,000 | Rp 735,630,000 | Rp 1,083,805,000 | `Scenarios!C13:E13` |
| Fixed Overheads / mo (incl. equip. lease in Lease mode) | Rp 79,483,150 / Rp 61,000,000 | Rp 67,483,150 / Rp 49,000,000 | Rp 57,483,150 / Rp 39,000,000 | `Scenarios!C30:E30`, `CAPEX (Rent)!H47` |
| Total Fixed Costs / mo | Rp 359,312,669 / Rp 340,829,519 | Rp 291,166,998 / Rp 272,683,849 | Rp 265,973,637 / Rp 247,490,488 | `Scenarios!C31:E31` |
| Steady-State Monthly EBITDA (IDR) | Rp -107,897,672 / Rp -89,414,523 | Rp 134,786,270 / Rp 153,269,420 | Rp 411,641,704 / Rp 430,124,853 | `Scenarios!C34:E34` |
| Steady-State EBITDA Margin (%) | -22.4% / -18.6% | 18.3% / 20.8% | 38.0% / 39.7% | `Scenarios!C35:E35` |
| Break-Even Guests / Day | 221.5 / 210.1 | 136.7 / 128.0 | 100.1 / 93.1 | `Scenarios!C45:E45` |
| Total Investment Requirement (IDR) | Rp 6,448,970,773 / Rp 7,453,235,491 | Rp 4,266,246,130 / Rp 5,092,222,453 | Rp 3,591,640,721 / Rp 4,372,998,122 | `Scenarios!C53:E53`, `CAPEX (Rent)!C54:D54` |
| Total Investment Requirement (CHF) | CHF 314,584 / CHF 363,572 | CHF 197,511 / CHF 235,751 | CHF 159,628 / CHF 194,355 | `Scenarios!C54:E54`, `CAPEX (Rent)!C55:D55` |
| Gap (+) / Surplus (-) vs CHF 200k Equity | CHF 114,584 / CHF 163,572 | CHF -2,489 / CHF 35,751 | CHF -40,372 / CHF -5,645 | `Scenarios!C55:E55`, `CAPEX (Rent)!C56:D56` |
| Simple Steady-State Payback After Tax (Yrs) | never / never | 3.38 / 3.55 | 0.93 / 1.09 | `Scenarios!C56:E56` |

## 4. Menu Engineering Table (`Menu!A6:J37`)

| Row | Category | Item | Net Price (IDR) | Food Cost (IDR) | Cost % | Unit Contribution (IDR) | Units / 100 Guests | Class | Cell Ref |
|---:|---|---|---:|---:|---:|---:|---:|---|---|
| 7 | Pasta | Cacio e pepe | Rp 89,000 | Rp 24,000 | 27.0% | Rp 65,000 | 12 | 0.106672 | `Menu!A7:J7` |
| 8 | Pasta | Carbonara (beef bacon, halal) | Rp 98,000 | Rp 30,000 | 30.6% | Rp 68,000 | 15 | 0.146824 | `Menu!A8:J8` |
| 9 | Pasta | Ragù bolognese | Rp 105,000 | Rp 34,000 | 32.4% | Rp 71,000 | 11 | 0.115362 | `Menu!A9:J9` |
| 10 | Pasta | Pesto genovese | Rp 95,000 | Rp 28,000 | 29.5% | Rp 67,000 | 8 | 0.075909 | `Menu!A10:J10` |
| 11 | Pasta | Truffle cream | Rp 135,000 | Rp 45,000 | 33.3% | Rp 90,000 | 5 | 0.067419 | `Menu!A11:J11` |
| 12 | Pasta | Arrabbiata (vegan) | Rp 82,000 | Rp 20,000 | 24.4% | Rp 62,000 | 4 | 0.032761 | `Menu!A12:J12` |
| 13 | Coffee | Espresso | Rp 32,000 | Rp 6,000 | 18.8% | Rp 26,000 | 5 | 0.015981 | `Menu!A13:J13` |
| 14 | Coffee | Americano (hot/iced) | Rp 40,000 | Rp 7,000 | 17.5% | Rp 33,000 | 12 | 0.047942 | `Menu!A14:J14` |
| 15 | Coffee | Latte / flat white | Rp 50,000 | Rp 12,000 | 24.0% | Rp 38,000 | 19 | 0.094886 | `Menu!A15:J15` |
| 16 | Coffee | Signature iced coffee | Rp 58,000 | Rp 14,000 | 24.1% | Rp 44,000 | 10 | 0.05793 | `Menu!A16:J16` |
| 17 | Coffee | Filter / manual brew | Rp 55,000 | Rp 12,000 | 21.8% | Rp 43,000 | 4 | 0.021974 | `Menu!A17:J17` |
| 18 | Functional drinks | Matcha / protein shake | Rp 55,000 | Rp 15,000 | 27.3% | Rp 40,000 | 6 | 0.03296 | `Menu!A18:J18` |
| 19 | Functional drinks | Kombucha / ginger shot | Rp 48,000 | Rp 14,000 | 29.2% | Rp 34,000 | 4 | 0.019177 | `Menu!A19:J19` |
| 20 | Breakfast & snacks | Croissant / pastry | Rp 38,000 | Rp 13,000 | 34.2% | Rp 25,000 | 10 | 0.037954 | `Menu!A20:J20` |
| 21 | Breakfast & snacks | Focaccia sandwich | Rp 75,000 | Rp 24,000 | 32.0% | Rp 51,000 | 6 | 0.044946 | `Menu!A21:J21` |
| 22 | Breakfast & snacks | Yogurt / oat bowl | Rp 65,000 | Rp 20,000 | 30.8% | Rp 45,000 | 4 | 0.025969 | `Menu!A22:J22` |
| 23 | Breakfast & snacks | Tiramisu | Rp 55,000 | Rp 16,000 | 29.1% | Rp 39,000 | 5 | 0.027467 | `Menu!A23:J23` |
| 24 | Add-ons | Extra parmigiano | Rp 15,000 | Rp 5,000 | 33.3% | Rp 10,000 | 6 | 0.008989 | `Menu!A24:J24` |
| 25 | Add-ons | Burrata add-on | Rp 45,000 | Rp 22,000 | 48.9% | Rp 23,000 | 3 | 0.013484 | `Menu!A25:J25` |
| 26 | Add-ons | Oat milk / extra shot | Rp 9,000 | Rp 3,000 | 33.3% | Rp 6,000 | 6 | 0.005394 | `Menu!A26:J26` |

## 5. Sensitivity Tornado (`Sensitivity!A27:D34`) & Monte Carlo (`MonteCarlo!A24:B33`)

| Rank | Driver (±20% flex around Base) | Δ EBITDA @ -20% (IDR) | Δ EBITDA @ +20% (IDR) | Total Swing (IDR) | Cell Ref |
|---:|---|---:|---:|---:|---|
| 1 | Average spend / menu prices | Rp -128,228,883 | Rp 128,228,883 | Rp 256,457,766 | `Sensitivity!A28:D28` |
| 2 | Guest volume (all channels) | Rp -85,190,654 | Rp 85,190,654 | Rp 170,381,307 | `Sensitivity!A29:D29` |
| 3 | Food & beverage cost % | Rp 43,038,229 | Rp -43,038,229 | Rp 86,076,459 | `Sensitivity!A30:D30` |
| 4 | Staff cost | Rp 33,381,466 | Rp -33,381,466 | Rp 66,762,932 | `Sensitivity!A31:D31` |
| 5 | Other fixed costs | Rp 17,297,090 | Rp -17,297,090 | Rp 34,594,180 | `Sensitivity!A32:D32` |
| 6 | Rent + service charge | Rp 7,554,844 | Rp -7,554,844 | Rp 15,109,688 | `Sensitivity!A33:D33` |
| 7 | Delivery commission | Rp 4,403,925 | Rp -4,403,925 | Rp 8,807,850 | `Sensitivity!A34:D34` |

### Monte Carlo Summary (1,000 Steady-State Draws, `MonteCarlo!A24:B33`)

| Metric | Value | Cell Ref |
|---|---:|---|
| Mean monthly EBITDA (IDR) | Rp 134,289,587 | `MonteCarlo!B24` |
| P10 monthly EBITDA | Rp 36,607,408 | `MonteCarlo!B25` |
| P50 monthly EBITDA | Rp 126,927,817 | `MonteCarlo!B26` |
| P90 monthly EBITDA | Rp 239,284,598 | `MonteCarlo!B27` |
| Probability EBITDA < 0 | 1.4% | `MonteCarlo!B28` |
| Probability payback ≤ 3 years | 33.0% | `MonteCarlo!B29` |
| Probability payback ≤ 5 years | 63.0% | `MonteCarlo!B30` |
| Median payback (years, 99 = never) | 3.95 | `MonteCarlo!B31` |
| Correlate volume & spend (same demand shock)? 1 = yes | 1 | `MonteCarlo!B33` |
