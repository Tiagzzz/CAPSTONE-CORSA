# Pre-verification batch 2b — now-items

**Independent checker:** codex  
**Date:** 2026-10-18  
**Scope:** R2-LBL-11, R2-TIME-01–03, R2-LEG-01, R2-FX-01, R2-ENV-01, and R2-CAGE-UNV-01–03. No checklist, source register, dataset, report, progress, or plan row was edited.

## Method

Opened the supplied original source once where possible, within five requests per item; no access control was bypassed. Time-sensitive items were checked against the current official page/listing on 18 October. CSV quotes are short source evidence (25 words or fewer).

## Results

| Item | Verdict | Reproducible source check | Outcome |
|---|---|---|---|
| R2-LBL-11 | UNREACHABLE | Kontan URL. | Original page returned HTTP 403; the label, value, and stated base cannot be independently checked. |
| R2-TIME-01 | NOT-CONFIRMED | BPJPH homepage/news and JDIH BPJPH current listings. | The current BPJPH statement confirms implementation on 18 October and pending special import rules, but does not establish the claimed Article 160(3) ministerial-decision absence. |
| R2-TIME-02 | CONFIRMED | BPJPH official 9 October news item. | It expressly says implementation starts 18 October 2026, is not postponed, and special provisions are being drafted. |
| R2-TIME-03 | CORRECTED | DDTC relay. | It supports 20% PBJT relief only for March 2026. It cannot establish the absence of a later decree or replace the unopened Kepgub text. |
| R2-LEG-01 | CORRECTED | JDIH BPK PP 42/2024 record. | The current official status says PP 42/2024 revoked PP 39/2021; the exact cited article number was not independently established. |
| R2-FX-01 | CONFIRMED | Report passages and Bank Indonesia transaction-rate page. | The report names no rate/date/source. BI displays a dated 16 October CHF rate, so it cannot supply the report's undocumented conversion retrospectively. |
| R2-ENV-01 | CONFIRMED | PLN current tariff-adjustment list and Q3 document. | Official current list exposes Q3 2026 as the newest document; no Q4 2026 document is listed. The stated B-2/TR rate is Q3-only. |
| R2-CAGE-UNV-01 | CORRECTED | Syarikat original article page. | It is now accessible and supports the 2025 East Jakarta questionnaire study of 100 respondents and the stated significant relationships. |
| R2-CAGE-UNV-02 | CORRECTED | Colliers original report page. | It is now accessible and supports the Q2 2026 Jakarta report's footfall, tenant-ecosystem, and experiential-consumption observations. |
| R2-CAGE-UNV-03 | UNREACHABLE | BPS DKI table URL. | Original table still returned HTTP 403, so the city-density ranking remains unverified. |

## Counts and assertion

- CONFIRMED: 3
- CORRECTED: 4
- NOT-CONFIRMED: 1
- UNREACHABLE: 2

`python3` CSV assertion passed: exact ten IDs, permitted verdicts, eleven populated columns per row, 25-word quote limit, and required checker/date fields.

## Blockers

Kontan and BPS DKI returned HTTP 403. The supplied PP PDF timed out; JDIH BPK independently confirms the revocation status, not the exact article number. The official Kepgub 310/2026 text and a current Q4 tariff document were not available from the opened sources.
