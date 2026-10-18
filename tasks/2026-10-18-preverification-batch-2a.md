# Pre-verification batch 2a — R2-LBL-01 to R2-LBL-10

**Independent checker:** codex  
**Date:** 2026-10-18  
**Scope:** label-only validation; no source register, dataset, checklist, or report row was edited.

## Method

Opened each listed source once where possible (maximum three requests per item; R2-LBL-06 required its two cited pages). Tested only the proposed label against source text: value/base, period, geography, metric, question, population, or instrument/article. Quotes in the CSV are brief source evidence (each is at most 25 words). `n/a` is an intentional non-blank, not a missing result.

## Results

| Item | Verdict | Reproducible source check | Outcome |
|---|---|---|---|
| R2-LBL-01 | CONFIRMED | GoodStats DEM-058 page; linked BPS release URL also attempted. | Susenas Sep 2025, overall `garis kemiskinan`, and 4 Mar 2026 relay byline support the fix. The BPS URL did not return readable page text, but its 5 Feb 2026 date is in the linked URL. |
| R2-LBL-02 | CORRECTED | IDN Times CMP-054 page. | No city or outlet is printed; `brand-wide` is an inference, so remove it. |
| R2-LBL-03 | CONFIRMED | detikFood CMP-057 page. | It calls Bastian `konsep Eropa modern` and gives the quoted cross-menu range. |
| R2-LBL-04 | CONFIRMED | APJII 2025 PDF methodology and generation table. | 8,700 and ±1.1% are whole-survey metadata; the Millennial table presents percentages, not subgroup n. |
| R2-LBL-05 | CORRECTED | GoodStats/Jakpat data page. | It establishes the 995 Java-urban survey and 33% chart value, but does not explicitly assign a denominator to that bar. Remove the un-reopened Databoks 955/769 assertion. |
| R2-LBL-06 | CORRECTED | Polri BEH-027 and Antara BEH-028 pages. | Polri reports 140,324; Antara attributes about 142,000 to Erick Thohir. Neither opened page says Polri repeated an organiser count. |
| R2-LBL-07 | CORRECTED | Databoks BEH-029 page. | It supports Lombok, NTB and the 2024/2023 values, but not the 27–29 Sep 2024 race dates. |
| R2-LBL-08 | CONFIRMED | BPJPH REG-012 statement. | It names UU 33/2014; `PP 42/2024` is absent. |
| R2-LBL-09 | CORRECTED | Marketing-Interactive BEH-088 relay. | It supports takeout under spending cutbacks and 2,067 adults, but does not state online collection or weighting. |
| R2-LBL-10 | CONFIRMED | NIQ BEH-013 page. | Methodology explicitly says Jan–Feb 2025, online adult consumers, 19 countries including Indonesia, and adult grocery-shopping population; Indonesia n is absent. |

## Counts and assertion

- CONFIRMED: 5
- CORRECTED: 5
- NOT-CONFIRMED: 0
- UNREACHABLE: 0

`python3` CSV assertion passed: exact ten IDs, permitted verdicts, eleven populated columns per row, quotes at most 25 words, and required checker/date fields present.

## Blockers

None. The BPS endpoint linked by R2-LBL-01 was not readable in this check; that did not change the confirmed GoodStats page wording or the linked-release-date qualification.
