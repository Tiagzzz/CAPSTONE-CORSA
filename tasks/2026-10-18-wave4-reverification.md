# Wave 4 re-verification of MAJOR fixes

- Report: `reports/2026-10-18-corsa-jakarta-insights-report.md` (branch insights-2026-10-18). Verifier did not write or fix the report. No report, CSV or commit changes.
- Checked against: repo rows in `data/processed/`, `data/processed/2026-10-18-preverification.csv`, spec rule 4 (`tasks/2026-10-18-insights-spec.md` lines 45-60), `analysis/outputs/model_summary.json`.
- Result: 13 majors checked: 9 PASS, 4 FAIL (F-09, W4-01, W4-03, W4-04; all label or citation fixes, no wrong figures). Spot-checks: 5 of 5 PASS. Both halves coexist: no conflict markers, `analysis/verify_report.py` gives unsourced=0, forbidden_hits=0.

## Majors

| finding | new text excerpt | checked against | PASS/FAIL | exact fix needed if FAIL |
|---|---|---|---|---|
| F-01 (l.100) | "Jakarta comparables list Pizza Marzano pasta at IDR 69,000-109,000 (city, outlet and tax basis not stated) ... ns-D" | P3PB-02/09 (tax "not stated", outlets not stated); R2-LBL-02 | PASS (small note: "Jakarta comparables list" and the new code `ns` are not defined anywhere; low risk) | none required. Optional: "Comparables list Pizza Marzano pasta ..." |
| F-02 (l.136) | "48% of Gen Z coffee consumers spend under IDR10k to buy or make a cup" | P1C3-01 CORRECTED-OPENED (n=896, buy or make) | PASS | |
| F-03 (l.41) | "80.2% ... (n=643) ... five boycott-sensitive cities (n=810) found 73.1% agreeing that some party benefits ..., a different question" | S-04 (n=643 self-selected, CORRECTED-OPENED), S-03 (n=810, 5 cities) | PASS | |
| F-04 (l.59) | "15.51 billion transactions in 2025 ... 43.06 million merchants by January 2026 ... SD11/SD16" | SD11 (full-year 2025), SD16 (Jan 2026) | PASS | |
| F-05 (l.20, 61) | "42% of delivery-app users typically spend under IDR 50,000 per order (another 42% spend IDR 50,000-100,000)" | SD05, SD06 (unit: % of respondents by typical spend) | PASS | |
| F-06 (l.128) | "Liga.Tennis platform users (all racquet sports, not padel-only) report average spend of about IDR400k per session plus IDR50k for consumption" | P4W10-11 | PASS | |
| F-07 (l.80) | "national online-panel coffee behaviour (Indonesia, no Jakarta or age cut), 44% ... 34% ... 62% of respondents (n=601, national online panel)" | UC-N13, P4W7b-01, CAGE-020 | PASS | |
| F-08 (l.118) | F03 cited with the South Jakarta link `721e41cd0521a99`; "2025" | P1C1-F03, register DEM-020 | PASS | |
| F-09 (l.114, 122, 134) | "pasta-plus-drink ticket of about IDR120k net (about IDR132k with PBJT) ... v0.5 placeholder, team note; re-confirm against model v0.6"; "pasta at IDR89,000-105,000 net (same v0.5 placeholder)"; "full IDR120k net lunch" | Model v0.6 `model_summary.json` Menu sheet (see below) | FAIL (partial): pasta 89-105k IS in v0.6 and can be cited by cell; the 120k/132k ticket is NOT in v0.6; the "re-confirm" question is now answerable | See F-09 answer below. |
| W4-01 (l.140) | "IDR69-109k at Pizza Marzano (menu list, city not stated)" but label "brand-wide menu, city not stated/no age split" for P3PB-02/09 | R2-LBL-02 CORRECTED: "geography: not stated ... do not infer brand-wide" | FAIL (label still says "brand-wide", which the correction forbids) | In l.140 replace "P3PB-02/09; brand-wide menu, city not stated/no age split" with "P3PB-02/09; city and outlet not stated/no age split". (Pepper Lunch and Fore keep "brand-wide menu list, city not stated": their rows say brand-wide, PASS.) |
| W4-02 (l.267) | "73.1% in a five-city survey (cities chosen for high boycott sensitivity, not Jakarta) agreed that some party benefits from the boycott, a different question" | S-03 | PASS | |
| W4-03 (l.162) | "For medium and large ... duty has applied since 18 October 2024; the phase for micro/small ... started 18 October 2026, and CORSA, as a PT PMA or operator of that scale, should be treated as in the 2024 group" | H-01, H-02 (medium/large from 18 Oct 2024; micro/small from 18 Oct 2026), H-04, R2-TIME-02 CONFIRMED | FAIL (dates correct; CORSA classification is an unlabelled judgement, and medium/large status is not sourced) | Replace ", and CORSA, as a PT PMA or operator of that scale, should be treated as in the 2024 group (still in force)." with ". **Assumption:** CORSA, as a PT PMA operating at that scale, would fall in the medium/large (2024) group; confirm the business-scale classification with counsel." |
| W4-04 (l.275) | "Evidence pointing the other way (Section 9): ... P1C2-01/P1C2-02 ... P1C2-10 ... conservative case has negative EBITDA (Section 8; `Scenarios!D6`, `D45`; model v0.6)" | P1C2-01/02/10 OK; Scenarios: C34 = -107,897,672 (conservative EBITDA/month), D6 = 200 guests, D45 = 136.71 | FAIL (small): the negative-EBITDA claim cites base-column cells D6/D45, not the conservative cell | Replace "(Section 8; `Scenarios!D6`, `D45`; model v0.6)" with "(Section 8; `Scenarios!D6`, `D45`, `Scenarios!C34`; model v0.6)". |

## F-09: model v0.6 menu cells (from `analysis/outputs/model_summary.json`, key `menu`, and `model_figures_table.md` section 4)

- Pasta net prices are unchanged from the v0.5 note: Cacio e pepe `Menu!C7` = 89,000; Carbonara `Menu!C8` = 98,000; Ragu `Menu!C9` = 105,000; Pesto `Menu!C10` = 95,000; Truffle cream `Menu!C11` = 135,000; Arrabbiata `Menu!C12` = 82,000. So "89-105k" = `Menu!C7:C9`, and the full IDR82-135k range in l.142 = `Menu!C7:C12` (l.142 currently has no cell).
- Coffee: Espresso `Menu!C13` = 32,000; Latte `Menu!C15` = 50,000.
- PBJT: `Inputs!F17` = 10%, "charged on top of net menu prices", excluded from revenue.
- There is NO pasta-plus-drink lunch ticket cell and no IDR120k or IDR132k value in v0.6. v0.6 blended net spend is `Menu!H30` = 103,375 (`Scenarios!D8`); `Menu!E30` = 100,120 (menu-implied). The note's "IDR 110,000 blended with PBJT" does not match 103,375 x 1.1 = 113,713.

Proposed replacements:
- l.114: "Analysis: a CORSA pasta-plus-coffee lunch built from the model's menu (for example cacio e pepe at IDR89,000, `Menu!C7`, plus espresso at IDR32,000, `Menu!C13`; model v0.6) is a considered purchase, not a routine app lunch; these are illustrative model inputs, net of 10% PBJT (`Inputs!F17`), not market facts." (The sum, IDR121,000, must be script-computed in `analysis/` before it is typed; otherwise omit the total.)
- l.122: "can anchor a pasta at IDR89,000-105,000 net (`Menu!C7:C9`; model v0.6)".
- l.134: replace "a full IDR120k net lunch" with "a full pasta-plus-coffee lunch (pasta IDR82-135k net, `Menu!C7:C12`; model v0.6)".
- Remove the "v0.5 placeholder / re-confirm against model v0.6" wording.

## Spot-checks of minor fixes (5 of 5 PASS)

| finding | new text | checked against | result |
|---|---|---|---|
| F-17 (l.40) | REG-039 URL slug `...tembus-rp1010-t-mayoritas-dari-modal-asing`; "IDR 173.6 trillion (PMA and PMDN combined)" | S-11, register | PASS |
| F-13 (l.128) | "CNA reports 185 of 397 registered padel courts (unit unclear) without a permit (UC-N07) ... two North Jakarta courts sealed 4 March 2026" | UC-N07, P4W5-08 | PASS |
| F-16 (l.120) | "high-income Indonesian beauty shoppers (62% vs 33% for lower income) in a three-country proxy" | P4W2b-08 (CORRECTED) | PASS |
| W4-12 (l.148, l.54) | "48% would pay over 10% more ... only 19% would pay 20% more ... 43% cite cost"; P4W4-01/02/04/06 | P4W4-01, -02, -06 | PASS |
| W4-08 (l.154) | "SCBD median IDR 408,691/m2/month (n=2; one rooftop F&B listing and one unverified office-tower reference listing)" | W4-08 finding text and Location!D8 (not re-derived from Rent_Data) | PASS |

## Coexistence

Both fixers' edits appear together (for example l.100 and l.140 Marzano wording, l.267 and l.41 boycott wording, l.128 and l.148). No conflict markers; `verify_report.py` unsourced=0, forbidden_hits=0. Note: the new geography code `ns` (l.100) and "codes in handoff" (l.29) refer to `tasks/2026-10-18-handoff.md`, which has no entry for `ns`; define it there or write "not stated".

## Fix status (round 2)

- W4-01: l.140 Marzano label now "city and outlet not stated/no age split". FIXED.
- W4-03: CORSA halal classification now labelled **Assumption** with counsel confirmation. FIXED.
- W4-04: `Scenarios!C34` added to the conservative negative-EBITDA citation. FIXED.
- F-09: v0.5 placeholder framing and IDR120k/132k ticket removed; report cites `Menu!H30` (blended net spend 103,375), `Menu!C7:C9`, `Menu!C7:C12`, `Inputs!F17`. No hand-typed derived total, no script needed. FIXED.
- Minor `ns` code: replaced by "geography not stated" in l.100. FIXED.
