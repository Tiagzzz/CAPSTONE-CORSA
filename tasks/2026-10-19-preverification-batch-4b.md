# Pre-verification batches 4b and 4c (REG-137)

Verifier: claude-sonnet-V1b, 2026-10-19. Source REG-137: World Bank, Indonesia Economic Prospects December 2025, local PDF `data/raw/2026-10-19-world-bank-indonesia-economic-prospects-dec-2025.pdf` (read via pdftotext on the PDF itself; PDF page = printed page + 9). No web fetch needed (local file, readable). Publisher URL check (pdftotext, pages 1-8): the PDF prints "www.worldbank.org" (publisher site, p. 2-ish front matter), "www.worldbank.org/id" (country page) and the document link "www.worldbank.org/iep" ("This report is available for download in English and Indonesian via: www.worldbank.org/iep"); no full https:// document URL is printed.

## Batch 4b

| item_id | verdict | evidence_quote | corrected_value | page/anchor checked | note |
|---|---|---|---|---|---|
| P2-16 | CONFIRMED | Real GDP growth held at 5.0 percent year-on-year over the first three quarters of 2025 | | PDF p.10 (printed 1) | Also p.15: "first three quarters of 2025 (3Q-25)". |
| P2-17 | CONFIRMED | Growth is projected to hold at 5.0 percent in 2026, rising to 5.2 percent in 2027 | | PDF p.11 (printed 2); Table A.2 PDF p.34 | Table A.2 agrees (5.0 / 5.2). |
| P2-18 | CONFIRMED | contribution to growth moderated slightly to 2.7 percentage points (pp) (53.3 percent of GDP growth), down from 2.8 pp in 2024 | | PDF p.10 (printed 1); p.11 | "expected to contribute less than previous years" on p.11. 2025 = first three quarters. |
| P2-19 | CONFIRMED | Low core inflation, sluggish car and retail sales, and subdued credit growth all point to moderating private consumption | | PDF p.15 (printed 6) | |
| P2-20 | CONFIRMED | In August 2025, 27 percent of households identified themselves as poor, a rise of 7 pp from the previous year | | PDF p.20 (printed 11) | Second part: "deteriorating circumstances rose by 5 pp to 24 percent, largely driven by concerns among the self-classified middle class". |
| P2-21 | CONFIRMED | median real income declined by 0.2 percent monthly, driven by a drop among the middle 40 household group | | PDF p.20 (printed 11) | Period Sep 2024 to Aug 2025, Listening to Indonesia survey. |
| P2-22 | CONFIRMED | Employment rose by 1.3 percent between August 2024 and August 2025, but gains were concentrated in lower-paying sectors | | PDF p.10 (printed 1) | "Real wages have trended down since 2018" same page. |
| P2-23 | CONFIRMED | At 2.6 percent average in 2026-27, inflation is projected to remain anchored within BI's target range of [2.5 percent ±1] | | PDF p.29 (printed 20); Table A.2 PDF p.34 | 2025 average 2.0 from Table A.2 (p.34, printed 25), not p.29; anchor should cite both. |
| P2-24 | CONFIRMED | BI lowered the policy rate by a cumulative 150 basis points since September 2024 to 4.75 percent | | PDF p.10 (printed 1); p.27 | "as of October 2025" appears on p.27 (printed 18): "from 6.25 percent to 4.75 percent as of October 2025". |

## Batch 4c

| item_id | verdict | evidence_quote | corrected_value | page/anchor checked | note |
|---|---|---|---|---|---|
| P2-25 | CONFIRMED | portfolio investment saw net outflows of US$7.8 billion (0.5 percent of GDP) ... the Rupiah fell 2.7 percent, compared to a 0.4 percent drop in the JP Morgan Emerging Market Currency Index | | PDF p.27 (printed 18) | Period July-November 2025. "BI intervened by purchasing IDR123.5 trillion (US$7.4 billion) in government securities on the secondary market" (secondary-market government securities, i.e. bonds). |
| P2-26 | CONFIRMED | The fiscal deficit widened to 2.0 percent of GDP by October 2025, up from 1.4 percent of GDP same period last year | | PDF p.10 (printed 1); p.29; Table A.2 p.34 | 2026 Budget Law target 2.7% on p.10 and p.29 Box A.4. WB projection 2.8% 2025, 2.8% 2026, 2.9% 2027 on p.29 / Table A.2 (not p.10). Deficit is year-to-October, not full year. |
| P2-27 | CONFIRMED | FDI in 3Q-25 declined to 0.9 percent of GDP, from 1.4 percent of GDP in 3Q-24. This decline is attributed to domestic and global uncertainty. | | PDF p.24 (printed 15) | |
| P2-28 | CONFIRMED | Net Foreign Direct Investment 1.0 (2024), 1.1 (2025), 1.2 (2026), 1.5 (2027) | | Table A.2, PDF p.34 (printed 25) | Table row, percent of GDP; 2024 actual, 2025-27 WB projections. |
| P2-29 | CONFIRMED | the Coordinating Ministry for Economic Affairs (CMEA) and Ministry of Finance are preparing a new regulatory debottlenecking reform plan as part of the President's drive for deregulation | | PDF p.24 (printed 15), sentence continues on same page, second column | Claim wording "deregulation drive" matches; sentence also states the aim "To attract more investment". |
| P2-30 | CONFIRMED | upside potential risk arises from ... accelerated implementation of ongoing business, trade and investment deregulation reforms | | PDF p.11 (printed 2) | Downside: "further softening of real wages" and "weaker-than-planned revenues". The text also lists stronger demand in major trading partners as an upside; claim is a subset, not wrong. |
| P2-31 | CONFIRMED | Relatively slow approval processes, complex and uncoordinated permitting, uncertainty over data governance ... deter investors | | PDF p.12 (printed 3) | Context is data centers only, as claim states; text also lists data governance, electricity and water as deterrents. |
| P2-32 | CONFIRMED | in early to mid-August, there were protests against local and building tax increase in Pati (Central Java), Bone (South Su[lawesi]), Cirebon (West Java). The tax increase was subsequently canceled | | PDF p.29 (printed 20), footnote 28 | Source says "local and building tax increase". Link to budget cuts to regions is in Box A.4 body text (same page). Year 2025 is implied by context. |
| P2-33 | CONFIRMED | budget cuts in 2025, with recent attempts to raise local taxes sparking local protests | | PDF p.29 (printed 20), Box A.4 | Source: 2026 Budget Law has a 20% decline in transfers to regions and "a shift toward greater centralization"; strain "already affected by budget cuts in 2025". |
