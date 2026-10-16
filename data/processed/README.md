# data/processed: run-1 datasets (Plan 1 surveys and Plan 4 purchase triggers)

**All values in this folder are PROVISIONAL.** Every figure was taken from a WebSearch result (publisher, URL and date shown) because source hosts were blocked. No source page was opened. Every `verification` value below therefore means "snippet-only, provisional" until the sources are opened and the figures are checked against them.

## Method

1. **Staging.** Workers wrote findings to `data/raw/<theme>/findings.md` (one block per source with a temporary key, e.g. `P4W2-S1`) and one CSV per theme here. Workers never edited `sources/sources.md`. A registrar then assigned register IDs (BEH-, DEM-); the mapping is in `sources/2026-10-16-run1-key-map.csv`. Each CSV row carries its `register_id`.
2. **Snippet-only deviation from CLAUDE.md §7.** Owner-approved fallback (see `tasks/2026-10-16-execution-run-log.md`): a figure may come from a search result only if it shows publisher, URL and date and the publisher is tier 1-3; the source is marked "snippet-only (not opened)" in the register. Search summaries are tool-written paraphrases, not verbatim page quotes. When hosts become reachable, verifiers open the real sources and upgrade or drop the figures.
3. **Independent verification.** Five separate verifiers (`tasks/2026-10-16-run1-verification-{a..e}.md`) re-searched every row with different wording. A later spot-audit (`tasks/2026-10-16-run1-verifier-audit.md`) disputed some rows. The fix-up applied their verdicts.
4. **Columns.** `row_id, question, trigger_or_metric, value, unit, ref_period, base_n, population, age_band_native, canonical_band, age_fit_code, geography, proxy_note, source_key, access_status, snippet, notes, register_id, verification`. `register_id` can hold two IDs separated by `;` (merged rows). `notes` includes the verifier remarks (prefixed V-A to V-E).

## Verification codes

| code | meaning |
| --- | --- |
| CONFIRMED-PROVISIONAL | a verifier confirmed the row via an independent search |
| CONFIRMED-WEAK | verifier only re-found the same publisher or the same press text, the report calls the row weak or single-outlet, or the spot-audit flagged single-outlet reliance |
| CORRECTED-PROVISIONAL | the row was corrected as the verifier stated (value, period, label, age code); corrected rows that are also single-outlet keep this code |
| QUALITATIVE-OK | qualitative row (no number) judged consistent with independent coverage |

## Drop rules

Rows with verdict UNCONFIRMED (no independent source reproduced the figure), DATE-FAIL (before 2024-10-16, not a labelled trend) or TIER-FAIL (tier-4 only) were removed. DERIVED rows (worker arithmetic, not a sourced figure) go to the notes of a related row, or to the dropped file with verdict DERIVED. Rows the spot-audit disputed are dropped as AUDIT-DISPUTED pending re-verification in run 2. Duplicate rows are merged (Q8-001 and Q8-002) and listed as DUPLICATE-MERGED. All removed rows are in `2026-10-16-run1-dropped-rows.csv` (columns `file, row_id, claim, value, verdict, reason`). No verifier found a DATE-FAIL or TIER-FAIL.

## Age-fit and geography codes

Age fit against the canonical bands (Gen Z 18-28, Younger Millennials 29-35, Older Millennials 36-45, Gen X 46-61): A = exact match, B = canonical band fully inside the native band, C = partial or approximate overlap, D = no age split or no usable overlap. Geography: J = Jakarta, U = urban Indonesia (several cities), N = national, P = proxy (other country or region). See Plan 4 section 4 for the full definitions.

## Files and row counts (surviving rows)

| file | rows |
| --- | --- |
| plan4-media-by-age.csv | 11 |
| plan4-social-proof.csv | 4 |
| plan4-novelty.csv | 9 |
| plan4-health.csv | 13 |
| plan4-community-sport.csv | 6 |
| plan4-origin-boycott.csv | 15 |
| plan4-venue.csv | 1 |
| plan4-spend-drivers.csv | 20 |
| demand/consumer-surveys.csv | 6 |
| **CSV total** | **85** |
| `data/raw/2026-10-17-disconfirming-evidence.md` (table A, 17 rows before) | 11 |
| 2026-10-16-run1-dropped-rows.csv | 18 dropped rows |

## Caveats

- Unresolved conflicts are kept in `notes` (for example the Bisnis headline vs body for Millennial delivery-app choice, 64% vs 68% mall dining).
- Several rows rest on a single outlet; they are marked CONFIRMED-WEAK.
- Newer figures exist for some rows (APJII 2026, MotoGP Mandalika 2026, MAPB FY2025); they were not added because this fix-up did no new research.
