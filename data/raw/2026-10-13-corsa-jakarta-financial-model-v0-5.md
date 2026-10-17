# CORSA Jakarta Financial Model v0.5 (workbook index)

> Text companion to `2026-10-13-corsa-jakarta-financial-model-v0-5.xlsx` (Google Drive file "CORSA_Jakarta_Financial_Model_v0.5_1 - Copy.xlsx", path 05_Finanzen / Jonas Playground, Drive ID 1Q-FbkLoMUwUo3V1VtqG7DAfJwPESJaAV, owner j.vuillaume2003@bluewin.ch, last modified 2026-10-13), created 2026-10-16. The workbook is the authoritative source and holds ~16,200 formulas. The CSV files in `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/` contain the **cached cell values** of every sheet (formulas not preserved); all 20 sheets are included in full. The README sheet of the workbook states: "v0.2 - structure complete, numbers indicative" and that most inputs are placeholders still to be validated; the file name says v0.5 and the 9 Oct finance overview calls it v0.5.1, so treat the version label with care.

## Sheets

| # | Sheet | Range | CSV |
|---|---|---|---|
| 1 | README | A1:B23 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/01-readme.csv` |
| 2 | Dashboard | A1:P58 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/02-dashboard.csv` |
| 3 | Inputs | A1:L103 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/03-inputs.csv` |
| 4 | Rent_Data | A1:T55 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/04-rent-data.csv` |
| 5 | Location | A1:V31 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/05-location.csv` |
| 6 | Menu | A1:Q61 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/06-menu.csv` |
| 7 | Revenue | A1:Q39 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/07-revenue.csv` |
| 8 | Staffing | A1:M31 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/08-staffing.csv` |
| 9 | OPEX | A1:P47 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/09-opex.csv` |
| 10 | CAPEX (Buy) | A1:M55 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/10-capex-buy.csv` |
| 11 | CAPEX (Rent) | A1:M55 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/11-capex-rent.csv` |
| 12 | Funding | A1:P38 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/12-funding.csv` |
| 13 | Scenarios | A1:S70 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/13-scenarios.csv` |
| 14 | PnL_Monthly | A1:BJ66 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/14-pnl-monthly.csv` |
| 15 | Annual | A1:S40 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/15-annual.csv` |
| 16 | Sensitivity | A1:S75 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/16-sensitivity.csv` |
| 17 | MonteCarlo | A1:AQ1039 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/17-montecarlo.csv` |
| 18 | Sources | A1:G88 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/18-sources.csv` |
| 19 | Research_Tracker | A1:F17 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/19-research-tracker.csv` |
| 20 | Methods | A1:C16 | `2026-10-13-corsa-jakarta-financial-model-v0-5-csv/20-methods.csv` |

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
