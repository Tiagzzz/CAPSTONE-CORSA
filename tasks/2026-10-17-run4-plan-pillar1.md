# Run 4 plan: Pillar 1 deliverables for the 22 Oct interim

Date: 2026-10-17. Owner instruction: Tiago (Product Owner). Replaces the paused run-3 "resume" list in the execution run log. Branch: `claude/kind-hopper-2nopv7` (run-3 work merged from `claude/great-ramanujan-mcp2e3`; `origin/main` already included).

## Goal
Deliver, evidence-backed and independently verified: (1) framework outline, (2) customer target profiles, (3) CAGE applied Switzerland to Jakarta, (4) PESTEL Jakarta. Deadlines: outline 19 Oct; the three drafts 20 Oct; verified and accepted 21 Oct 12:00 UTC.

## Rules (all reports)
Per section: why we looked, data, what it means for CORSA, how to continue. Investor-friendly summary on top. Only VERIFIED-OPENED or CORRECTED-OPENED rows; BLOCKED rows excluded and named. Tags `[row; geo-agefit]`, confidence, Appendix. State plainly when evidence is national/proxy or has no age split. Fix the 11 open label rows (P1C4-16, P3PB-06, P3PB-27, UA-N12, UA-N67, Q8-001, Q8-003, H-04, P4W9-29, P4W4-06, P1C2-03) before a report uses them. Lessons rules: time-limited rules carry their period; verifiers get full rows (notes, in_force_confirmation, amendment_check, gaps); risk sections cite all verified disconfirming rows in scope. Source IDs: own entries from REG-045; never 900 or above. Do not edit `research/internal/` or `docs/scope/`. Merge, never rebase or force-push; never push to `main`.

## Steps and agents
| Step | Task | Agent / model | Owned files |
| --- | --- | --- | --- |
| 1 | Apply V-P2 fixes F1-F16 and audit fixes H-03, H-12, F-05 to Plan 2 report; then re-verify | W-P2 (Sonnet), V-P2b (Sonnet, independent) | `reports/2026-10-17-regulatory-entry-pathway.md`, `tasks/2026-10-17-run4-verification-plan2.md` |
| 2 | Fix the 11 label rows used by Pillar 1 | W-LBL (Sonnet) | the CSVs holding those rows |
| 3 | Shared mapping: row id, PESTEL dim, CAGE dim, implication | W-MAP (Sonnet) | `data/processed/2026-10-pillar1-mapping.csv` |
| 4 | Environmental scan, tier 1 or gap | W-ENV (Sonnet) | `data/raw/2026-10-xx-environmental.md`, `data/processed/2026-10-pestel-environmental.csv`, `sources/sources.md` |
| 5 | Outline (by 19 Oct), profiles, CAGE, PESTEL drafts | W-OUT, W-PROF, W-CAGE, W-PEST (Sonnet; parallel after 3 and 4) | the four report files |
| 6 | Independent verifier per report plus balance check | V-OUT, V-PROF, V-CAGE, V-PEST (Sonnet) | `tasks/2026-10-xx-run4-verification-*.md` |
| 7 | Main agent review, accept in run log | main | run log |
After Pillar 1: balance check on Plan 1-3 reports, remaining label issues, date-sensitive re-checks (H-12 on 19-20 Oct, H-04, T-07), consolidated lawyer/tax list in `tasks/`, then "Run 3 complete" in the run log and a PR "Research run 3 wrap-up" (not merged).

## Acceptance
Every figure traces to a registered source; verifier finds 0 WRONG; every Matthieu claim marked verified / corrected / unverified; disconfirming rows in scope all cited; outline at most one page.
