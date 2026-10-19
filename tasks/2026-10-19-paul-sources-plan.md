# Plan: Paul's Phase 2 sources (19 Oct 2026)

Scope: step 3 of `tasks/2026-10-18-phase2-update-plan.md`, plus step 4 for any item used. The new Excel model (steps 1–2) is out of scope. Branch `paul-sources-2026-10-19` (from `main` after PR #6). PR into `main`, not merged. Progress log: `tasks/2026-10-19-paul-sources-progress.md`.

## Sources (8) and register IDs

| ID | Source | Kind |
|---|---|---|
| REG-136 | OECD FDI Regulatory Restrictiveness Index 2025, Business and Finance Policy Papers No. 105 (a7751054-en) | PDF `data/raw/2026-10-19-oecd-fdi-regulatory-restrictiveness-index-2025.pdf` (33 pp) |
| REG-137 | World Bank, Indonesia Economic Prospects Dec 2025, "Digital Foundations for Growth" | PDF `data/raw/2026-10-19-world-bank-indonesia-economic-prospects-dec-2025.pdf` (62 pp) |
| REG-138 | IMF PR 26/010, 2025 Article IV consultation with Indonesia | link |
| REG-139 | US State Dept, 2024 Investment Climate Statement: Indonesia | link |
| REG-140 | World Bank WGI, Political Stability and Absence of Violence (GOV_WGI_PV_SC), Indonesia | link |
| REG-141 | Transparency International, CPI 2025 | link |
| REG-142 | BPJPH: products requiring halal certification from 18 Oct 2026 | link |
| REG-143 | Reuters, student "heading for bankrupt Indonesia" protests, 12 Jun 2026 | link (may be blocked → UNREACHABLE) |

REG prefix because `analysis/inventory.py` only parses BEH/DEM/CMP/REG IDs; next free REG number is 136.

## Research questions
Indonesia-specific: FDI restrictions (F&B retail, F&B services, foreign-ownership caps); macro outlook (growth, inflation, rupiah, policy rate); political stability; corruption; governance; halal certification deadlines; protest/political risk.

## Steps, owners, models

| # | Step | Agent (model) | Owns |
|---|---|---|---|
| 1a | Convert OECD PDF to md (page markers `<!-- page N -->`) | W-PDF1 (Sonnet; long-text fidelity) | `data/raw/2026-10-19-oecd-...md` |
| 1b | Convert World Bank PDF to md | W-PDF2 (Sonnet) | `data/raw/2026-10-19-world-bank-...md` |
| 1c | Extract claims from the 6 links (one fetch each) | W3a (Sonnet) | scratchpad `staging-web.csv` |
| 1d | Check both md files (word ratio ≥ 0.90 of pdftotext, 5 spot checks each, page markers) | V-PDF (Sonnet, not W-PDF1/2) | report only |
| 2 | Extract claims from both md files with page anchors; register all 8 sources | W3b (Sonnet) | `sources/sources.md`, scratchpad `staging-pdf.csv` |
| 3 | Number rows `P2-01…`, write `analysis/outputs/preverification-batch-4.csv`, append to `data/processed/2026-10-18-preverification.csv` (`origin=Paul source`, `check=now`, verdicts empty) | W4 (Haiku; formatting) | both CSVs |
| 4 | Verify in batches of 10–15: PDFs against the PDF (pdftotext of the cited page), links with one fetch each, no bypass | V1a/V1b/V1c (Sonnet; never W3a/W3b) | `tasks/2026-10-19-preverification-batch-4{a,b,c}.md` |
| 5 | Merge verdicts into both CSVs; summary `tasks/2026-10-19-preverification-batch-4.md` | W4 (Haiku) | CSVs |
| 6 | Second-verifier spot check of ≥ 10 % of verdicts | V2 (Sonnet, new agent) | `tasks/2026-10-19-paul-spot-check.md` |
| 7 | Integrate CONFIRMED/CORRECTED items into the report (PESTEL political/economic/legal; CAGE administrative/economic; section 7 entry route); Part C in `verify_report.py`; Part B codes in `analysis/appendix_reason_overrides.json`; changelog line; run `run_all.py --skip-links` | W2 (Sonnet) | report, `analysis/verify_report.py` (Part C only), overrides json |
| 8 | Independent check of every added/changed report sentence vs CSV verdict and source; style rules; no existing fact dropped | V3 (Sonnet, new agent) | `tasks/2026-10-19-paul-report-verification.md` |
| 9 | Fix-ups (W2), full `run_all.py` with links, final review, commit, PR | orchestrator + W2 | — |

## Acceptance criteria
1. Both PDFs have `.md` versions with a header (source PDF, page count, conversion date, PDF authoritative) and page markers; V-PDF passes (word ratio ≥ 0.90, 5 spot checks each).
2. All 8 sources in `sources/sources.md` with all fields and a justified tier.
3. Every extracted claim is a `P2-` row with a page or URL anchor; all have a verdict from an agent other than the extractor, evidence quote ≤ 25 words, `checked_by`, `checked_on`.
4. ≥ 10 % of verdicts re-checked by V2; disagreements resolved and logged.
5. Only CONFIRMED/CORRECTED items appear in the report (corrected values used); agreements/updates/contradictions with existing claims stated; Analysis:/Assumption: labels kept; no existing fact, source or CSV row dropped.
6. Part C lists the 8 sources with verdicts and sections; unused items in Part B with reason codes.
7. `python3 analysis/run_all.py --skip-links` and the full run exit 0; `unsourced_numeric_statements_count` = 0; `disallowed_preverification_fact_citations` empty; forbidden-string lists empty; words ≤ 10,000.
8. Style: "19 Oct 2026", "43 %", thin space as thousands separator in new text.

## Rules
Token rules of `tasks/2026-10-18-handoff.md`. No login, paywall or bot-challenge bypass. Checkpoint commit and push after each step.
