# Pre-verification batch 3 — Wave 2b now-items

Checked 2026-10-18 by codex. One original/cited-source fetch per item where possible (two for the wheat compound item); no login, paywall, or bot-challenge bypass was attempted. Compound claims require every component; unresolved components are stated in `corrected_value`.

## Reproducible item log

- `R2-CAGE-UNV-04` — `UNREACHABLE` — UIN repository timed out.
- `R2-CAGE-UNV-05` — `UNREACHABLE` — BPS DKI homepage returned Cloudflare challenge; no age-projection table opened.
- `R2-CAGE-UNV-06` — `CORRECTED` — PP 42/2024 Art. 2(1) supports certification duty, not the exact marketing wording; GE-15 remains unsupported.
- `R2-BLK-01` — `UNREACHABLE` — PwC returned HTTP 403 Access Denied; no blocked-row components reopened.
- `R3-DEM-016` — `CORRECTED` — BPS September 2026 headline CPI is 3.28% YoY, not 2.65%; F&B/tobacco was 4.37% YoY.
- `R3-DEM-019` — `CORRECTED` — official BPS source is Q2-2026 GDP (+5.29% YoY), not the stated middle-class/eating-out claim.
- `R3-DEM-062_and_DEM-063` — `UNREACHABLE` — Kontan timed out; Media Indonesia returned Cloudflare challenge.
- `R3-CMP-017_and_CMP-033_to_035` — `UNREACHABLE` — Blue Bottle official locator returned Cloudflare block.
- `R3-REG-128` — `UNREACHABLE` — Colliers returned Cloudflare challenge.
- `R3-PRICE_LADDER_COMMON_GROUNDS_AND_SALADSTOP` — `NOT-CONFIRMED` — official cited pages provide brand/location information, not direct menu prices.

Output: `analysis/outputs/preverification-batch-3.csv` (10 complete 11-column rows).

Assertions: PASS — exact requested IDs; allowed verdicts; 11 populated columns; evidence quotes at most 25 whitespace-delimited words; checker/date set; no blank cells. Counts: CONFIRMED 0; CORRECTED 3; NOT-CONFIRMED 1; UNREACHABLE 6.

## Blockers

Six items are source-blocked or timed out. Do not use their unresolved claims as facts without an independently accessible source.
