# data/processed: run-1 datasets (Plan 1 surveys and Plan 4 purchase triggers), upgraded in run 1b

**Status after run 1b (2026-10-16).** Run 1 took every value from a WebSearch result because source hosts were blocked. In run 1b the owner widened network access, independent upgrade verifiers (`tasks/2026-10-16-run1b-upgrade-{a..e}.md`) opened the sources, and this fix-up applied their verdicts. Values are now classified by the `verification` code below. **Rows marked BLOCKED remain provisional (snippet-only).** The 118 new candidate rows were checked by second independent verifiers (`tasks/2026-10-16-run1b-verification-new-{1,2}.md`) and carry their verdicts; no row remains OPENED-UNVERIFIED.

## Method

1. **Staging.** Workers wrote findings to `data/raw/<theme>/findings.md` and one CSV per theme here. A registrar assigned register IDs (BEH-, DEM-); the run-1 mapping is in `sources/2026-10-16-run1-key-map.csv`. Each CSV row carries its `register_id` (several IDs separated by `;`: the opened source first, then the originally registered one).
2. **Run 1: snippet-only fallback** (owner-approved deviation from CLAUDE.md section 7, see `tasks/2026-10-16-execution-run-log.md`). Five verifiers re-searched every row (`tasks/2026-10-16-run1-verification-{a..e}.md`); a spot-audit (`tasks/2026-10-16-run1-verifier-audit.md`) disputed some rows.
3. **Run 1b: source opening.** Five new upgrade verifiers opened the cited pages with curl (no bot-challenge bypass) and reported per row: URL opened, printed publication date, a quote from the page, corrections. This fix-up (a) set `verification` from the verdict, (b) set `access_status` to "opened" and replaced `snippet` with the quote from the opened page where the page was opened, (c) applied every correction and label fix (kept in `notes`, prefixed "Run 1b (2026-10-16)"), (d) registered all newly opened sources in `sources/sources.md` (BEH-037 to BEH-064, DEM-020 to DEM-027), and (e) appended the candidate rows the verifiers found. Downloaded PDFs (APJII 2025 and 2026, Playtomic) were kept in the scratchpad and are not in the repository.
4. **Columns.** `row_id, question, trigger_or_metric, value, unit, ref_period, base_n, population, age_band_native, canonical_band, age_fit_code, geography, proxy_note, source_key, access_status, snippet, notes, register_id, verification`. Empty cells were filled with "n/a" (or "not reported" for `base_n`). Row IDs with prefix `UA-`, `UB-`, `UC-`, `UD-`, `UE-` are run-1b candidate rows found by upgrade verifiers U-A to U-E.

## Verification codes (run 1b)

| code | meaning |
| --- | --- |
| VERIFIED-OPENED (original) | the original publisher's page (or file) was opened and the figure matches (value, unit, year) |
| VERIFIED-OPENED (relay) | only a relay outlet was opened (news site, data portal) and the figure matches; the original was not opened. Source tier 3 |
| CORRECTED-OPENED | the opened page showed a different value, base or label; the correction is applied and described in `notes` |
| BLOCKED | the source could not be opened (Cloudflare or Akamai challenge, 403, page gone) and no substitute carried the figure; the run-1 value is kept and the row is **provisional (snippet-only)** |
| OPENED-UNVERIFIED | new candidate row taken from an opened page by an upgrade verifier; it still needs an independent check |

The run-1 codes (CONFIRMED-PROVISIONAL, CONFIRMED-WEAK, CORRECTED-PROVISIONAL, QUALITATIVE-OK) no longer appear in the CSV files; their remarks are still in `notes` with the prefixes V-A to V-E. Rows with "(relay)" are tier-3 sources even where the underlying data is tier 1 (BPS, BI, OJK, company filings).

## Drop rules

Rows with verdict NOT-FOUND-OPENED or DATE-FAIL are removed and listed in `2026-10-16-run1-dropped-rows.csv` (columns `file, row_id, claim, value, verdict, reason`) with the run-1b verdict. In run 1b no existing row was dropped. One new candidate row (UE-N02, Jakpat millennials restaurant survey printed 13 June 2016) failed the date test (before 2024-10-16) and is listed there as DATE-FAIL. The run-1 entries SD11 to SD13 (QRIS FY2025, AUDIT-DISPUTED) were reinstated in `plan4-spend-drivers.csv` as VERIFIED-OPENED (relay): Kontan, 2026-03-12, quoting the BI Deputy Governor; their dropped entries were removed. Three other dropped run-1 rows (P4W1-R12, P4W5-03, P4W5-05) were re-found by upgrade verifiers and re-added as new candidate rows UA-N50, UC-N03 and UC-N04; their dropped entries are kept with a run-1b remark.

## Age-fit and geography codes

Age fit against the canonical bands (Gen Z 18-28, Younger Millennials 29-35, Older Millennials 36-45, Gen X 46-61): A = exact match, B = canonical band fully inside the native band, C = partial or approximate overlap, D = no age split or no usable overlap. Geography: J = Jakarta, U = urban Indonesia (several cities), N = national, P = proxy (other country or region). See Plan 4 section 4 for the full definitions. Corrections in run 1b: the Sep 2025 eating-out survey (P4W1-R04 to R07, UA-N58 to UA-N67) covers eight Java cities and excludes Jakarta, so geography is U; the Mar 2025 delivery-app survey (P4W1-R08) is national (N). No opened source gives an age split for the 25-39 core in any theme.

## Files and row counts

| file | existing rows (run 1b) | new candidate rows | total |
| --- | --- | --- | --- |
| plan4-media-by-age.csv | 11 | 61 (UA) | 72 |
| plan4-social-proof.csv | 4 | 7 (UA) | 11 |
| plan4-novelty.csv | 9 | 11 (UB) | 20 |
| plan4-health.csv | 13 | 4 (UB) | 17 |
| plan4-community-sport.csv | 6 | 7 (UC) | 13 |
| plan4-origin-boycott.csv | 15 | 4 (UC) | 19 |
| plan4-venue.csv | 1 | 3 (UC) | 4 |
| plan4-spend-drivers.csv | 20 + 3 reinstated (SD11-SD13) | 13 (UD) | 36 |
| demand/consumer-surveys.csv | 6 | 8 (UE) | 14 |
| **CSV total** | **88** | **118** | **206** |
| `data/raw/2026-10-17-disconfirming-evidence.md` (table A) | 11 | 0 (see section A2) | 11 |
| 2026-10-16-run1-dropped-rows.csv | 16 rows (18 - 3 reinstated + 1 new DATE-FAIL) | | |

## Rows per verification code (CSV files)

| code | rows | of which existing rows | of which new rows |
| --- | --- | --- | --- |
| VERIFIED-OPENED (original) | 96 | 25 | 71 |
| VERIFIED-OPENED (relay) | 77 | 43 | 34 |
| CORRECTED-OPENED | 16 | 3 | 13 |
| BLOCKED | 17 | 17 | 0 |
| OPENED-UNVERIFIED | 0 | 0 | 0 |
| **total** | **206** | **88** | **118** |

Per file:

| file | original | relay | corrected | BLOCKED | OPENED-UNVERIFIED |
| --- | --- | --- | --- | --- | --- |
| plan4-media-by-age.csv | 46 | 15 | 11 | 0 | 0 |
| plan4-social-proof.csv | 6 | 2 | 0 | 3 | 0 |
| plan4-novelty.csv | 11 | 9 | 0 | 0 | 0 |
| plan4-health.csv | 12 | 0 | 0 | 5 | 0 |
| plan4-community-sport.csv | 4 | 9 | 0 | 0 | 0 |
| plan4-origin-boycott.csv | 3 | 11 | 3 | 2 | 0 |
| plan4-venue.csv | 4 | 0 | 0 | 0 | 0 |
| plan4-spend-drivers.csv | 8 | 21 | 0 | 7 | 0 |
| demand/consumer-surveys.csv | 2 | 10 | 2 | 0 | 0 |

Disconfirming-evidence table A (11 rows): original 3 (rows 1, 2, 3), relay 3 (rows 6, 9, 17), CORRECTED-OPENED 2 (rows 13, 16), BLOCKED 3 (rows 5, 8, 15).

BLOCKED rows (provisional, snippet-only): P4W2-05, P4W2-06, P4W2-07 (Tirto, Cloudflare); P4W4-09 to P4W4-13 (PwC, Akamai); Q6-003, Q6-010 (Bisnis only); SD03, SD04 (Snapcart original gone); SD09, SD10 (Bisnis); SD21, SD22, SD23 (PwC); table A rows 5, 8, 15.

## Caveats

- Rows marked BLOCKED remain provisional (snippet-only).
- The new UA-/UB-/UC-/UD-/UE- rows now carry second-verifier verdicts; some duplicate other rows (UA-N53/N54 vs SD01/SD02; UA-N55/N57 vs UD-N01/UD-N03) and are marked in `notes`.
- Many opened pages are relays of a tier-1 or tier-2 original (Databoks, GoodStats, CNBC, Kontan, Detik); the original was not opened. Several originals sit behind bot challenges (bps.go.id, Bisnis, pwc.com, tirto.id): not bypassed.
- Resolved conflicts: Millennial delivery-app choice (GoFood 37%, Bisnis headline wrong), mall dining 68% (the 64% was another article), QRIS FY2025 (Kontan quotes BI; the BI press release carrying the count was not found), padel 173% (per court per month), MAPB 9M sales -2.77% (filing; -2.84% in press text). Open conflict: Fore Coffee price band (Bisnis Rp20,000 to above 30,000 vs Kompas Rp30,000-40,000), recorded in table A row 15.
- APJII 2026 is newer than APJII 2025 (Gen Z 89.02% vs 87.80%, Millennial 90.34% vs 89.12%); the 2026 YouTube share (1-2%) vs 2025 (17-32%) looks like a questionnaire break and should not be trended.
- Kantar "Dining in the Digital Age" (ID 2026) was opened but carries no numbers (gated download): no rows.

## Run 2 files (2026-10-17)

Run 2 added eight data files (plan4 venue/social proof, age splits, population and spend, middle-class income, listed operators, foreign entrants, Plan 2 entry requirements). Six independent verifiers (`tasks/2026-10-17-run2-verification-{a..f}.md`) opened the sources; a fix-up set `verification` on every row from the verdict and applied each correction (prefix "Run 2 verification (2026-10-17)" in `notes`). Plan 2 legal rows: regulations are pre-window by nature and are used for in-force status; the cited instrument is the tier-1 source, the Hukumonline and DDTC rows are tier-3 relays.

Questions for an Indonesian lawyer: see tasks/2026-10-17-run2-verification-f.md

Plan 2 schema note: `2026-10-p2-entry-requirements.csv` does not use the survey columns. Columns: `row_id, question, finding, value, unit, rule_date, instrument, article, source_key, access_status, quote, in_force_confirmation, amendment_check, confidence, gaps, applies_to_entry_mode, notes, register_id, verification`. Row IDs `E-` = entry requirements (investment threshold, capital, licensing, KBLI), `H-` = halal. `quote` holds the original Indonesian text; `in_force_confirmation` and `amendment_check` record the status check. Other run-2 schemas: `listed-operators.csv` adds `company, metric` after `question`; `foreign-entrants.csv` adds `brand, origin, entry_year, mode, partner, status, status_date, format_price, reasons_fact, reasons_commentary, window_class` after `verification`.

| file | rows | original | relay | corrected | BLOCKED |
| --- | --- | --- | --- | --- | --- |
| plan4-venue-run2.csv | 13 | 9 | 3 | 1 | 0 |
| plan4-social-proof-run2.csv | 23 | 6 | 12 | 5 | 0 |
| plan4-age-splits.csv | 36 | 12 | 24 | 0 | 0 |
| demand/population-spend.csv | 25 | 0 | 25 | 0 | 0 |
| demand/middle-class-income.csv | 30 | 8 | 21 | 1 | 0 |
| listed-operators.csv | 41 | 22 | 16 | 2 | 1 |
| foreign-entrants.csv | 23 | 2 | 15 | 5 | 1 |
| 2026-10-p2-entry-requirements.csv | 25 | 20 | 3 | 2 | 0 |
| **total** | **216** | **79** | **119** | **16** | **2** |

Rows moved to `2026-10-16-run1-dropped-rows.csv` (now 28 rows): DATE-FAIL P3B-18, 19, 21, 23, 24, 25 (foreign-entrants.csv; context kept in `data/raw/2026-10-17-foreign-entrants.md` under "Historical / pre-window context") and DERIVED-MOVE P1C1-P07 (population-spend.csv; value in the notes of P1C1-P01 to P06). foreign-entrants.csv therefore has 23 rows (29 - 6) and population-spend.csv 25 (26 - 1). BLOCKED rows: P3BF-030 (IDX 403, gap row) and P3B-17 (Domino's 250 outlets, RRI blocked; window_class IN-WINDOW-PROVISIONAL).

Geography code note (run 2): J means Jakarta (DKI) only. Greater Jakarta (Jabodetabek) cuts are coded U, for example P3BF-033 (Fore outlets, metric `outlets_jabodetabek`).

## Run 3 files (2026-10-17)

Run 3 added `plan4-misc-run3.csv`, `demand/wheat-foodservice.csv`, `2026-10-p2-tax-franchise.csv`, `2026-10-p2-sentiment-indicators.csv` and `price-ladder.csv`. Three independent verifiers (`tasks/2026-10-17-run3-verification-{a,b,c}.md`) opened the sources; a fix-up set `verification` on every row from the verdict and applied each correction (notes prefixed "Run 3 verification" or "Run 3 fix-up"). The first four files use the survey schema of run 1b (`wheat-foodservice.csv`, `plan4-misc-run3.csv`), the Plan 2 schema (`tax-franchise`: `row_id, question, finding, value, unit, rule_date, instrument, article, ...`) or the sentiment schema (`indicator, reported_fact_value, ref_period_and_type, scope_base, ...`); `price-ladder.csv` adds `brand, item, category, price_idr, tax_service_included, channel, district, item_class, price_basis`. Price statistics are in the DERIVED table of `data/raw/2026-10-17-price-points.md` (recomputed from the CSV, with an "of which approx" column and a brand-concentration note).

Questions for a tax/legal adviser: see tasks/2026-10-17-run3-verification-b.md

| file | rows | original | relay | corrected | BLOCKED |
| --- | --- | --- | --- | --- | --- |
| plan4-misc-run3.csv | 28 | 2 | 25 | 1 | 0 |
| demand/wheat-foodservice.csv | 23 | 10 | 8 | 5 | 0 |
| 2026-10-p2-tax-franchise.csv | 23 (24 - T-14) | 16 | 2 | 5 | 0 |
| 2026-10-p2-sentiment-indicators.csv | 8 (11 - S-01, S-02, S-08) | 1 | 4 | 3 | 0 |
| price-ladder.csv | 89 | 24 | 64 | 1 | 0 |
| **total** | **171** | **53** | **103** | **15** | **0** |

Rows moved to `2026-10-16-run1-dropped-rows.csv` (now 32 rows, 4 added): T-14 (DATE-FAIL, DJP article of 2022), S-01 (DATE-FAIL, MUI fatwa of 2023-11-08, pre-window, not a long-run series; verifier verdict was VERIFIED-OPENED (relay)), S-02 and S-08 (NOT-FOUND-OPENED gap rows). Other notable fixes: Liga.Tennis rows P4W10-10 to -13 set to geography J on the orchestrator's instruction (V3-A noted that the clubs' locations are not stated); P3PB-45 price blanked (25,000 moved to notes); Fore Manuka/Peach/Berry Americanos relabelled `flavoured_americano`; P1C4-08 second source GoodStats registered as DEM-063; REG-041 to REG-044 added for the DJP country page, the SIF list and the two BKPM releases. The APEDA mirror for DEM-050, -060 and -061 was unreachable on re-check; the register now points to the USDA originals at apps.fas.usda.gov.
