# Phase 2 update plan (19 Oct 2026)

Scope: fold the new Excel financial model (replacing v0.6) and Paul's sources into the report. Branch `insights-2026-10-18`; update the existing PR, never merge. Read `tasks/2026-10-18-handoff.md` and `tasks/2026-10-18-progress.md` first. Token rules: grep before reading; never read `row_index.json` or `model_summary.json` in full.

Agents: orchestrator plans and does the final review only. Workers and verifiers are Sonnet; link checks and CSV formatting are Haiku. A verifier is never the author.

## 1. New model and script run (worker W1, Sonnet)
Owns: `data/raw/2026-10-19-corsa-jakarta-financial-model-v<N>.xlsx`, `analysis/outputs/*`.
1. Save the new file in `data/raw/` (date-prefixed). Keep v0.6 (`data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx`); no duplicates of the new file.
2. Snapshot the v0.6 outputs: `mkdir -p <scratchpad>/v06 && cp analysis/outputs/model_figures_table.md analysis/outputs/model_summary.json analysis/outputs/stats_tables.md <scratchpad>/v06/`.
3. Run `python3 analysis/run_all.py --model-path data/raw/<new>.xlsx --skip-links`. `--skip-links` skips the slow HTTP check; link status is rerun once at step 6 without the flag.
4. Diff: `diff <scratchpad>/v06/model_figures_table.md analysis/outputs/model_figures_table.md`, and a short python comparison of the key scalars in `model_summary.json`: three scenarios, sensitivity ranking, completeness flags.
5. Output: a change table (figure, v0.6, new, cell reference) in `tasks/2026-10-19-phase2-model-diff.md`.
Acceptance: the script exits 0, outputs are deterministic on a rerun, and every changed figure is in the table.

## 2. Map model changes to the report (worker W2, Sonnet)
Owns: `reports/2026-10-18-corsa-jakarta-insights-report.md`, `data/processed/2026-10-18-claim-ledger.csv` (via the script).
1. List the claims that depend on the model: `python3 -c "import csv;[print(r['claim_id'],r['section']) for r in csv.DictReader(open('data/processed/2026-10-18-claim-ledger.csv')) if r['depends_on']=='model_v0.6']"`. There are 74 of 152 ledger rows. Also grep the report for `v0.6`, `CHF` and `Annual!`.
2. Match each changed figure to its claims and report cells. Update the figure, cell reference and model version. Change `depends_on` to the new model label (for example `model_v0.7`) and make the labelling consistent in `verify_report.py` if it hardcodes `model_v0.6`.
3. Re-check the Phase 1 model flags and state in the text whether each is closed:
   - only 13 of 60 `PnL_Monthly` months populated (`C4:O53`), with `Annual` years 2–5 at zero;
   - `Dashboard!B17:B26` NPV, IRR and payback invalid;
   - placeholder inputs;
   - the Base-scenario gap versus CHF 200k equity (`Scenarios!C55:E55`);
   - active switches `Inputs!D4` (scenario) and `Inputs!H4` (CAPEX financing).
4. Keep the Analysis:/Assumption: labels. Do not state a figure the new model does not contain.

## 3. Paul's sources (workers W3, Sonnet; W4, Haiku for formatting)
Owns: `sources/sources.md`, `data/processed/2026-10-18-preverification.csv`, `analysis/outputs/preverification-batch-4.csv`, `tasks/2026-10-19-preverification-batch-4.md`.
1. W3 registers each source in `sources/sources.md` (CLAUDE.md §5): title, publisher/author, URL, publication date, access date, tier 1–4, and what it is used for. A tier-4 source is a lead only.
2. W4 appends rows to `2026-10-18-preverification.csv` with the existing columns: `item_id` (prefix `P2-`), `origin`=`Paul source`, `claim`, `source_url`, `priority`, `check=now`, and verdict fields empty.
3. Independent verifier V1 (Sonnet, a different agent from W3) handles the batch. One fetch per source (`curl -sL` and grep, about 5 tool calls at most), no login, bot-challenge or paywall bypass, and a blocked source is UNREACHABLE. It records the verdict, `evidence_quote` (25 words or fewer), `corrected_value`, `checked_by` and `checked_on`.
4. Use only CONFIRMED or CORRECTED items, and cite the corrected value. NOT-CONFIRMED and UNREACHABLE items stay out of the text and go to appendix Part B.
5. Map confirmed items to report sections and claims. Add rows to the ledger (via the script) with `depends_on=paul_pending` resolved to `none`.
6. Fill appendix Part C. The script emits the "Pending: Paul's Phase 2 Sources" placeholder (`verify_report.py` ~line 808); replace it with the registered sources, their verdicts and the sections they feed. Codes for sources left unused go into `analysis/appendix_reason_overrides.json` (`{id: {code, reason}}`).

## 4. Model sources used as fact (verifier V2, Sonnet)
Owns: rows in the preverification CSV.
1. 47 items with `check=if_used` are currently unverified (UNVERIFIED-NOT-USED in Part B).
2. For each one the updated text now states as fact (new model, Paul's sources), run the same one-fetch verification. Others stay UNVERIFIED-NOT-USED.

## 5. Independent claim check (verifier V3, Sonnet, Wave-4 style)
Owns: `tasks/2026-10-19-phase2-verification.md`.
1. Check every changed or added claim against its cited source or model cell: value, unit, year, context.
2. Check evidence labels, section balance and the tier-4 rule. Reuse the `tasks/2026-10-18-wave4-verification-*.md` format.
3. Fix-ups are done by W2, then V3 rechecks. Record the cause in `tasks/lessons.md` after any corrective action (CLAUDE.md §10).

## 6. Rerun checks, release (orchestrator plus W2)
1. `python3 analysis/run_all.py --model-path data/raw/<new>.xlsx` (full, including links). Then confirm `python3 analysis/verify_report.py` regenerates the ledger and appendix.
2. Acceptance, from `analysis/outputs/verify_report_summary.json`: words ≤ 10,000, unsourced = 0, forbidden_hits = 0 (no Singapore/Dubai/Hong Kong comparison, no HSG staff names).
3. Bump the report to v1.1. Rewrite the section 12 open points and Phase 2 paragraph, and add a v1.1 changelog entry: new model, Paul's sources, changed figures, closed or open gaps.
4. Add lines to `tasks/2026-10-18-progress.md` (what, who, result).
5. Checkpoint commits after each step with the prefix `claude:` (or the agent prefix), with the Co-Authored-By trailer. `git push`, update the PR description (sources used, verification result). Do not merge.

## Open issues carried from Phase 1 (section 12 and model flags)
- Missing Jakarta 25–39 occupation/commuter cross-tab.
- No measured micro-catchment footfall.
- Paid-menu validation outstanding.
- Final halal/import treatment undecided.
- Franchise-versus-licence classification open.
- Verified deal rents missing.
- Placeholder model inputs not replaced with primary observations and quotes.
- v0.6 model: 13 of 60 P&L months, `Annual` years 2–5 invalid, displayed NPV/IRR and payback invalid.
- Pre-verification: 11 UNREACHABLE and 5 NOT-CONFIRMED items from wave 2b remain open; 47 `if_used` items unverified unless used.
- 6 ledger claims have `depends_on=team_unverified`: re-check them if Paul's sources cover them.
- `analysis/verify_report.py` hardcodes the label `model_v0.6` (lines ~317, ~326 for `depends_on`/`verification`, ~736 for appendix A.4). Before re-running on the new model, change these to the new version label, or the ledger will mislabel model-dependent claims.
- CORSA's own menu price points in the report are v0.5 placeholders cited to `analysis/notes/r2_pillar1_notes.md`; re-cite them to the new model's `Menu` cells.
