# CORSA Jakarta Financial Model v0.6 (workbook index)

> Text companion to `2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx` (local file "CORSA_Jakarta_Financial_Model_v0.6.xlsx" provided by Tiago on 2026-10-18; model by Jonas and Marius according to Tiago; file metadata: created 2026-10-06 by openpyxl, last saved 2026-10-18 13:03 UTC by Tiago Reimann), ingested 2026-10-18. The workbook is the authoritative source and holds 16,634 formulas. The CSV files in `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/` contain the **cached cell values** of every sheet (formulas not preserved); all 20 sheets are included in full. It supersedes v0.5 (`2026-10-13-corsa-jakarta-financial-model-v0-5.*`), which is kept for comparison.

## Sheets

| # | Sheet | Range | CSV |
|---|---|---|---|
| 1 | README | A1:B23 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/01-readme.csv` |
| 2 | Dashboard | A1:P58 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/02-dashboard.csv` |
| 3 | Inputs | A1:L103 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/03-inputs.csv` |
| 4 | Rent_Data | A1:T55 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/04-rent-data.csv` |
| 5 | Location | A1:V31 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/05-location.csv` |
| 6 | Menu | A1:Q61 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/06-menu.csv` |
| 7 | Revenue | A1:Q39 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/07-revenue.csv` |
| 8 | Staffing | A1:M31 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/08-staffing.csv` |
| 9 | OPEX | A1:P47 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/09-opex.csv` |
| 10 | CAPEX (Buy) | A1:M55 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/10-capex-buy.csv` |
| 11 | CAPEX (Rent) | A1:AA126 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/11-capex-rent.csv` |
| 12 | Funding | A1:P38 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/12-funding.csv` |
| 13 | Scenarios | A1:S70 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/13-scenarios.csv` |
| 14 | PnL_Monthly | A1:BJ66 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/14-pnl-monthly.csv` |
| 15 | Annual | A1:S40 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/15-annual.csv` |
| 16 | Sensitivity | A1:S75 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/16-sensitivity.csv` |
| 17 | MonteCarlo | A1:AQ1039 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/17-montecarlo.csv` |
| 18 | Sources | A1:G110 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/18-sources.csv` |
| 19 | Research_Tracker | A1:F17 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/19-research-tracker.csv` |
| 20 | Methods | A1:C16 | `2026-10-18-corsa-jakarta-financial-model-v0-6-csv/20-methods.csv` |

## Completeness check (main session, 2026-10-18)

**Structure: complete.** All 20 sheets are populated, every formula has a cached result, and no cached result is an Excel error (0 error values found).

**Not complete:**

1. **PnL_Monthly is built for 13 months only** (columns C to O). Annual (SUMIFS over columns C:BJ, five operating years) and the Dashboard ("over 60 months", 5-year NPV and IRR) expect 60 months. As a result:
   - Annual years 2 to 5 are partial or zero;
   - Dashboard "Year-3 EBITDA" shows 0;
   - the "NPV of 5-year project cash flows" (IDR -3,185,886,005, CHF -147,495) and the project IRR are not meaningful;
   - "Lowest cash balance over 60 months" covers 13 months.

   The same gap exists in v0.5. Year-1 figures, the steady-state Scenarios, break-even and simple payback do not use months 14 to 60.
2. **Inputs are still preliminary, per the workbook itself:**
   - README: "Preliminary – most inputs are placeholders to be validated";
   - Menu: "ILLUSTRATIVE placeholder menu – replace prices with your pri[ces]";
   - Research_Tracker: 5 of 13 questions are "Placeholder" (Realistic investment requirement?; Main CAPEX blocks?; Monthly operating costs?; Food cost & gross margin?; Footfall & customer profile by district?), 4 are "Desk" and 4 are "Model ready";
   - Jonas's README note says he is still checking the numbers and waiting for Pillar 1 inputs.
3. **Version labels:** the README title and Status still say v0.2. The only v0.6 note is dated 16 Oct 2026.
4. **Authorship:** the workbook names only Jonas (README note); Marius is not named. The file metadata shows a script as creator and Tiago as the last saver, so it cannot show who edited what.

## What changed since v0.5

- New switch `Inputs!H4` (CAPEX mode: 1 = Buy, 2 = Lease/sponsor; saved as 2). It feeds Funding, PnL_Monthly, Scenarios, Annual and the Dashboard.
- CAPEX (Rent) rebuilt (55 x 13 to 126 x 27 cells used): per-item financing route, BFI-based lease maths, provider directory, buy-versus-lease summary.
- OPEX row 19 and Dashboard row 29: equipment lease, rental and sponsor payments per month.
- Sources sheet: 88 to 110 rows (README: S83 to S104).
- No other input cell changed. Computed values move through the new switch.

## Key outputs (Dashboard, active scenario, as saved)

| Output | IDR | CHF |
|---|---|---|
| Total investment requirement | 4,266,246,130 | 197,511 |
| Founder equity | 4,320,000,000 | 200,000 |
| Funding gap | -53,753,870 | -2,489 |
| Mature monthly revenue | 735,630,000 | 34,057 |
| Steady-state monthly EBITDA | 134,786,270 | 6,240 |
| Break-even revenue per trading day | 16,761,712 | 776 |
| Year-1 revenue | 7,295,392,080 | 337,750 |
| Year-1 EBITDA | 730,264,586 | 33,809 |
| Break-even guests per day | 137 |  |
| Mature guests per day | 200 |  |
| EBITDA margin at maturity | 0.18 |  |

Scenario comparison (Dashboard, conservative / base / optimistic):

| Row | Conservative | Base | Optimistic |
|---|---|---|---|
| Total investment (CHF) | 314,584 | 197,511 | 159,628 |
| Gap vs CHF 200k equity (CHF) | 114,584 | -2,489 | -40,372 |
| Simple payback (years) | never | 3.38 | 0.93 |
| Break-even guests / day | 222 | 137 | 100 |
| EBITDA margin | -0.22 | 0.18 | 0.38 |

NPV, IRR and years 2 to 5 are affected by item 1 above and are not shown.

## README sheet (verbatim)

- CORSA Jakarta Flagship – Financial Model v0.2
-  Preliminary – most inputs are placeholders to be validated.
- Note from Jonas  | I created this Financial model to give me a general overview of all the components to take into account. I'm using it to. However, even if most data are sourced, I'm currently working on checking all the numbers and data, and verify the accuracy of the finidngs. Many data need to be discussed with the Pillar 1 team, and I'm waiting for their inputs to adjust the model. 
- Purpose | Test whether a 120–180 m² CORSA flagship in Jakarta works commercially, what it costs, whether CHF 200k is enough and which assumptions matter most.
- How to use | 1) Pick scenario in Inputs!D4.  2) Edit blue cells only (Inputs, Rent_Data, Menu, Staffing, CAPEX unit costs, Revenue dwell times).  3) Read Dashboard, Scenarios, Sensitivity, MonteCarlo.
- Colour code | Blue text = hard-coded input · Black = formula · Green = link to another sheet · Yellow fill = key assumption · Light-green fill = key output.
- Currency | Model runs in IDR; CHF shown at the Inputs FX rate. Menu prices are NET of the 10% restaurant tax (PBJT), which is passed through to guests.
- Sheet map | Dashboard → Inputs → Rent_Data → Location → Menu → Revenue → Staffing → OPEX → CAPEX → Funding → Scenarios → PnL_Monthly → Annual → Sensitivity → MonteCarlo → Sources → Research_Tracker → Methods
- Scenario logic | Conservative = fewer guests, lower spend, higher costs/rent, longer ramp-up. Optimistic = the reverse. Scenarios sheet calculates all three in parallel (steady state); PnL_Monthly runs the active one month by month.
- Biggest early finding | Foreign-owned PT PMA rules (IDR 2.5bn paid-up ≈ CHF 115k, IDR 10bn investment plan ≈ CHF 460k per KBLI) may matter more for the CHF 200k question than the CAPEX itself – verify with a lawyer.
- Status | v0.2 – structure complete, numbers indicative, every input traced to a source or marked as an assumption. See Research_Tracker for what to validate before 22 Oct.
- Sources (v0.2) | Added 8 Oct 2026: 32 new sources (S46–S77) and a source trail on every sheet – per-row columns in Inputs (I, K, L), Staffing (K–M), CAPEX (K–M), Menu (O–Q), and a 'Sources & calculation basis' table at the bottom of every other sheet (MonteCarlo: top right).
- v0.6 (16 Oct 2026) | CAPEX (Rent) completed: per-item financing route (buy / finance lease / rental / sponsor), BFI-based lease maths, provider directory, Buy-vs-Lease summary; new switch Inputs!H4 (1 = Buy, 2 = Lease) feeds Funding, PnL, Scenarios, Annual, Dashboard. Sources S83–S104.
