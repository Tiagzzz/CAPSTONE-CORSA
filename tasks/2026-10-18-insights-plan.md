# Orchestration Plan: Phase 1 CORSA Jakarta Insights Report (2026-10-18)

## Codex continuation (18 Oct 2026)

- Resume at Wave 2b from the empty verdict columns; do not repeat Waves 1 or 2a.
- Run three independent verification batches in parallel, with exclusive batch-log files and result CSVs; a separate integration worker updates the shared checklist, progress log, and checkpoint commits after each approximately 10-item batch.
- Continue the remaining Wave 2b items in the same pattern, then use file-owned writers for Wave 3 and writers who did not author a section for Wave 4 verification. Wave 5 fixes only verified findings, runs the repository checks, writes the appendix and Phase 2 plan, and opens (but does not merge) the PR.
- Acceptance criteria remain those below. Every checklist edit uses `checked_by=codex`; every commit starts `codex:`.
- Model choice (owner decision): use Terra for research and source verification, Sol for deeper analysis/integration/audit, and Luna for prose; split long report text across multiple Luna calls. Keep prompts and owned files narrow to limit usage.

## 1. Objective & Acceptance Criteria

Produce the Phase 1 actionable insights report and full source appendix from `Tiagzzz/CAPSTONE-CORSA` for the **21 Oct 2026** interim presentation, working on branch `insights-2026-10-18` and opening an unmerged PR into `main` titled `"Phase 1 insights report (2026-10-18)"`.

### Deliverables
1. **`reports/2026-10-18-corsa-jakarta-insights-report.md`** (Deliverable 1):
   - Maximum **10,000 words** (counted by script, excluding Deliverable 2).
   - Simple Markdown tables allowed; no images or charts.
   - Leads with conclusions: each section answers **why we looked, what the data says, what it means for CORSA, what to do next**.
   - Sections 0 to 12 covering:
     - `0.` Executive summary (1 page) + 8 to 12 key messages for the 21 Oct presentation (1 sourced sentence each).
     - `1.` Question, evidence base and limits (0.5 page).
     - `2.` PESTEL: the Jakarta operating context (~2.5 pages; Political, Economic, Social, Technological, Environmental, Legal; 3–5 factors each, implication, confidence level).
     - `3.` CAGE: Switzerland to Jakarta (~2.5 pages; Cultural, Administrative, Geographic, Economic; distance, meaning for CORSA, transfers / needs adapting / must be tested, Indonesian network effect on administrative distance).
     - `4.` Four target groups, ranked from most to least relevant, and their customer behaviour (~3.5 pages; explicit ranking criteria first, 4 distinct groups, occasions, discovery channels, purchase triggers, price tolerance vs ladder, fit/adapt/test, plus dropped groups: students, creators, expats and why).
     - `5.` Competitors, benchmarks and price position (~2 pages; competitor map, price ladder position, mandatory Oakberry benchmark lessons: scalability, product simplification, international translation, health/convenience, risks to avoid, how CORSA differs).
     - `6.` Location (~1 page; district-to-target-group fit, rent levels from `Rent_Data` and `Location` sheets, pre-verified where stated as market fact, and footfall gap).
     - `7.` Entry route and regulation (~1.5 pages; PT PMA IDR 10bn plan test, IDR 2.5bn paid-up capital, halal, franchise rules, tax, routes open within CHF 200k, lawyer/tax/BPJPH questions).
     - `8.` Financial case (~2 pages; model v0.6 status, conservative/base/optimistic scenarios, Sensitivity & MonteCarlo drivers, invalid multi-year outputs due to 13-month `PnL_Monthly` and placeholder inputs, Phase 2 fixes needed, single script-generated model-figures table).
     - `9.` Key risks and facts pointing the other way (~1 page; scripted comprehensive coverage of verified downside evidence: middle-class budgets, real wages, savings, eating out cut, foreign-brand performance, boycotts).
     - `10.` Recommendations and strategic implications (~1.5 pages; Keep / Adapt / Test matrix; conditions for Go, Adapt, Stop; all recommendations labelled as Analysis).
     - `11.` 90-day validation roadmap priorities (~1 page; customer, location, validation priorities, primary-research brief: what to ask, whom, how).
     - `12.` Open points, Phase 2 and Changelog (0.5 page; v1.0 = Phase 1).
2. **`reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md`** (Deliverable 2):
   - **Part A (Sources used):** every register source cited (`ID`, `title`, `publisher`, `tier`, `publication date`, `URL`, `report sections`, `number of claims`), plus team files and model sheets used.
   - **Part B (Sources not used, with reason code and 1-line explanation):** every register entry not cited in Deliverable 1, unconfirmed `BLOCKED` rows, `NOT-CONFIRMED` / `UNREACHABLE` pre-verification items, and dropped rows from `2026-10-16-run1-dropped-rows.csv` and `2026-10-pillar1-mapping-excluded.csv`, using standard codes (`BLOCKED`, `NOT-CONFIRMED`, `OUT-OF-WINDOW`, `DUPLICATE`, `TIER4-LEAD`, `CONTRADICTED`, `OFF-SCOPE`, `CONDENSED-OUT`).
   - **Part C (Pending):** structured placeholder for Paul's Phase 2 sources and the Phase 2 model update.
3. **Working & Automation Files (for verification and Phase 2):**
   - `analysis/run_all.py` (accepting `--model-path` argument, defaulting to `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx`) and modular helper scripts in `analysis/`.
   - `data/processed/2026-10-18-preverification.csv` and batch logs `tasks/2026-10-18-preverification-batch-*.md` + spot-audit log.
   - `data/processed/2026-10-18-claim-ledger.csv`.
   - `tasks/2026-10-18-phase2-update-plan.md`.
   - Independent verification logs in `tasks/2026-10-18-verification-*.md`.

---

## 2. Hard Rules & Constraints

1. **Protected & Read-Only Files:** Do NOT edit `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `research/internal/**`, `docs/scope/**`, `data/raw/*.xlsx`, existing `reports/2026-10-16-*` or `reports/2026-10-17-*`, or the `verification` column of existing CSVs.
2. **Every Claim Sourced or Labelled:**
   - External source: `([Publisher](https://...), ROW_ID; GEO-AGEFIT)` (and `[REG-ID]` mapping to `sources/sources.md`).
   - Team file: `(team: research/internal/...)`.
   - Financial model: `(model v0.6: Sheet!Cell)`.
   - Unsourced interpretation or assumption: explicitly prefixed or tagged **`Analysis:`** or **`Assumption:`**.
3. **No Hand-Typed Derived Figures:** All sums, medians, ratios, and model tables are computed by Python scripts in `analysis/`.
4. **Evidence Level Stated:** Every potentially Jakarta-specific claim states geography (`J`, `J*`, `U`, `N`, `P`) and age-fit (`A`–`D` or `na`). Never present national data as Jakarta data.
5. **Balance Rule:** Every section that concludes something also states the verified evidence pointing the other way.
6. **Pre-Verification Gate (Wave 2b):** `BLOCKED` rows, team claims outside the verified 161 CAGE claims, and model `Sources` sheet claims (`S01`–`S104`) used as market facts may ONLY be used as facts if confirmed (`CONFIRMED` or `CORRECTED`) by an independent verifier agent in Wave 2b and logged in `data/processed/2026-10-18-preverification.csv`.
7. **No HSG Staff Names or University-Internal Matters:** Audience is CORSA founders Samuel and Joshua. Do not mention Heiko Bergmann, HSG grading, Rflect, course credits, or student team dynamics.
8. **Time-Limited Rules:** Explicitly state validity periods and current status (e.g., SEHATI 2025 only, Kepgub 722/2025 expired 31 Jan 2026, Kepgub 310/2026 March 2026 only, BPJPH 18 Oct 2026 phase start).
9. **Dropped Scope:** Do NOT cover the Singapore, Dubai, and Hong Kong comparison.

---

## 3. Subagent Architecture & Model Selection

Per owner instructions:
- Spawn **Gemini subagents only** (`Model="inherit"` which runs Gemini 4 Argon in this session, or `flash` only if requested—per tool guidelines and prompt §1, we use `inherit` so economic interpretation and synthesis run on **Gemini Argon**).
- Keep each subagent's task small, focused, with explicit owned output files so no two agents edit the same file.

---

## 4. Execution Waves

### Wave 1: Mechanical Scripts & Repository Inventory
- **Owner:** Coding subagent (`W1-Scripts`) + Orchestrator check.
- **Inputs:** `data/processed/**/*.csv`, `sources/sources.md`, `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx`, `data/raw/2026-10-17-disconfirming-evidence.md`.
- **Outputs:**
  - `analysis/inventory.py`: inventories all CSV rows (655+ rows across all files), maps `source_ids` to `sources/sources.md` (325 entries), lists all `BLOCKED` rows, lists all downside/mixed rows, and checks the 11 label fixes in `tasks/2026-10-17-run4-label-fixes.md`.
  - `analysis/extract_model.py`: uses `openpyxl` (`data_only=True` and formula check) to extract all 3 scenarios (`Conservative`, `Base`, `Optimistic`), `Dashboard` outputs, `Rent_Data`, `Location`, `Menu`, `Staffing`, `OPEX`, `CAPEX (Buy)`, `CAPEX (Rent)`, `Funding`, `Sensitivity` rankings, `MonteCarlo` stats, `Research_Tracker`, and `Sources` (`S01`–`S104`), plus completeness flags (`PnL_Monthly` 13/60 months, Year 2–5 invalid, NPV/IRR invalid). Outputs `analysis/outputs/model_summary.json` and `analysis/outputs/model_figures_table.md`.
  - `analysis/compute_stats.py`: computes price-ladder statistics (with approximate-price flags and brand concentration shares per `lessons.md`), demand and middle-class summary metrics, and CAGE claim register tallies. Outputs `analysis/outputs/stats_summary.json` and `analysis/outputs/stats_tables.md`.
  - `analysis/check_links.py`: checks HTTP status of URLs in `sources/sources.md` (curl/urllib with browser User-Agent, no bot-challenge bypass) and caches results to `analysis/outputs/link_status.json`.
  - `analysis/verify_report.py`: counts words in Deliverable 1, parses every factual sentence/bullet to verify citation coverage or `Analysis:`/`Assumption:` tags, builds `data/processed/2026-10-18-claim-ledger.csv`, and generates Deliverable 2 (`reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md`) Parts A, B, and C.
  - `analysis/run_all.py`: single CLI entrypoint accepting `--model-path` that runs the full pipeline end-to-end.
- **Git checkpoint:** Commit Wave 1 scripts and generated baseline JSON/MD artifacts on `insights-2026-10-18`.

### Wave 2a: Readers & Candidate Unverified Item Extraction (Parallel Gemini Argon Subagents)
Each reader agent reads its assigned files, produces structured sourced bullet notes in `analysis/notes/`, and outputs a structured list of candidate unverified items (`BLOCKED` rows, unverified team claims from Oakberry/Tiago/Paul, and model `Sources` S01–S104 needed as market facts, plus the 11 label-fix rows from `2026-10-17-run4-label-fixes.md` for independent verification).
- **`R1-Team-Oakberry-Behaviour` (Gemini Argon):**
  - Reads: `research/internal/2026-10-18-oakberry-benchmark.md`, `research/internal/2026-10-14-oakberry-benchmark-research1.md`, `research/internal/2026-10-14-oakberry-benchmark-corsa-locations.md`, `research/internal/2026-10-08-customer-behaviour-report.md`, `research/internal/2026-10-08-customer-behaviour-extended-data.md`, `research/internal/corsa-jakarta-target-customer-condensed-v1.md`, `research/internal/corsa-first-research-paul.md`, `meetings/*.md`.
  - Outputs: `analysis/notes/r1_team_notes.md` and `analysis/notes/r1_unverified_candidates.json`.
- **`R2-Pillar1-Syntheses` (Gemini Argon):**
  - Reads: `reports/2026-10-17-pestel-jakarta.md`, `reports/2026-10-17-cage-switzerland-jakarta.md`, `reports/2026-10-17-customer-target-profiles.md`, `reports/2026-10-17-purchase-triggers-and-channels.md`, `reports/2026-10-17-regulatory-entry-pathway.md`, `tasks/2026-10-17-lawyer-and-tax-questions.md`.
  - Outputs: `analysis/notes/r2_pillar1_notes.md` and `analysis/notes/r2_unverified_candidates.json`.
- **`R3-Argon-Economics-Model` (Gemini Argon):**
  - Reads: `reports/2026-10-17-demand-economics.md`, `reports/2026-10-17-competitor-map-and-price-ladder.md`, `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.md`, `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6-csv/*.csv`, `research/internal/2026-10-09-corsa-finance-overview.md`, `analysis/outputs/model_summary.json`, `analysis/outputs/stats_summary.json`.
  - Outputs: `analysis/notes/r3_economics_model_notes.md` and `analysis/notes/r3_unverified_candidates.json`.

### Wave 2b: Batch Pre-Verification of Unverified Data & Open Audit Items (Independent Verifier Subagents)
- **Grouping:** Consolidate all candidate items from Wave 2a into batches of 10–15 items grouped by source/domain:
  - **Batch 1 (`V2b-Batch1`):** Oakberry benchmark claims (`research/internal/2026-10-18-oakberry-benchmark.md` — 11 hyperlinked sources + key metrics: 700+ stores, 40+ countries, $100M+ revenue, 28–32% COGS, 25–60 sqm format, franchise fees, Jakarta stores).
  - **Batch 2 (`V2b-Batch2`):** Financial Model v0.6 market-fact sources (`Rent_Data`, `Location`, `Inputs`, `Staffing`, `OPEX`, `CAPEX (Rent)` key sources `S01`–`S104` cited in Sections 6 & 8, plus current CHF/IDR official exchange rate to replace the unsourced Plan 2 CHF rate).
  - **Batch 3 (`V2b-Batch3`):** Team customer behaviour / location claims outside the verified CAGE register + selected `BLOCKED` CSV rows that could strengthen Sections 2, 4, 5, 9 + time-sensitive checks (`H-12`, `H-04`, `T-07`).
  - **Batch 4 (`V2b-Batch4`):** Independent check of the 11 open label-fix rows from `tasks/2026-10-17-run4-label-fixes.md` (`P1C4-16`, `P3PB-06`, `P3PB-27`, `UA-N12`, `UA-N67`, `Q8-001`, `Q8-003`, `H-04`, `P4W9-29`, `P4W4-06`, `P1C2-03`) + Plan 2 `Art. 197` check against `PP 42/2024`.
- **Outputs:**
  - `tasks/2026-10-18-preverification-batch-1.md` to `batch-4.md`.
  - Consolidated `data/processed/2026-10-18-preverification.csv`.
  - Any newly opened sources registered in `sources/sources.md` with non-overlapping IDs (`REG-910+`).
- **Spot-Audit (`V2b-SpotAudit`):**
  - A separate verifier agent re-checks >=10% of `CONFIRMED` items across batches and logs results to `tasks/2026-10-18-preverification-spot-audit.md`.
- **Git checkpoint:** Commit Wave 2a notes and Wave 2b pre-verification files.

### Wave 3: Section Writers (Parallel Gemini Argon Subagents)
Each writer owns distinct sections, strictly respects word budgets so the merged report is <= 9,500 words (leaving safety margin below the 10,000-word ceiling), uses ONLY verified CSV rows and Wave 2b `CONFIRMED`/`CORRECTED` items, includes `Analysis:` or `Assumption:` on every unsourced interpretation, and includes balanced counter-evidence in every concluding section.
- **`W3-Sec0-1-2-3` (Sections 0, 1, 2, 3 — target ~3,100 words):**
  - Sec 0: Executive Summary & 8–12 Key Messages for 21 Oct (~550 words)
  - Sec 1: Question, Evidence Base & Limits (~300 words)
  - Sec 2: PESTEL: The Jakarta Operating Context (~1,150 words)
  - Sec 3: CAGE: Switzerland to Jakarta (~1,100 words)
  - Output: `analysis/drafts/sec_0_to_3.md`
- **`W3-Sec4-5` (Sections 4, 5 — target ~2,700 words):**
  - Sec 4: Four Target Groups Ranked & Linked to Customer Behaviour (~1,750 words; explicit ranking criteria, 4 distinct groups, dropped groups explained)
  - Sec 5: Competitors, Benchmarks & Price Position, incl. Oakberry (~950 words)
  - Output: `analysis/drafts/sec_4_to_5.md`
- **`W3-Sec6-7-8` (Gemini Argon — Sections 6, 7, 8 — target ~2,200 words):**
  - Sec 6: Location & District Economics (~500 words)
  - Sec 7: Entry Route, Regulation & Legal/Tax Questions (~750 words)
  - Sec 8: Financial Case (Model v0.6) & Script-Generated Table (~950 words)
  - Output: `analysis/drafts/sec_6_to_8.md`
- **`W3-Sec9-10-11-12` (Sections 9, 10, 11, 12 — target ~1,600 words):**
  - Sec 9: Key Risks & Facts Pointing the Other Way (~500 words; scripted complete list of downside rows)
  - Sec 10: Recommendations & Strategic Implications: Keep, Adapt, Test; Go/Adapt/Stop (~550 words)
  - Sec 11: 90-Day Validation Roadmap Priorities & Primary-Research Brief (~400 words)
  - Sec 12: Open Points, Phase 2 Preview & Changelog (~150 words)
  - Output: `analysis/drafts/sec_9_to_12.md`
- **`W3-Unused-Reasons` (Classifier for Deliverable 2 Part B):**
  - Assigns `OFF-SCOPE` or `CONDENSED-OUT` (with specific section/question explanation) to any verified register source not directly cited in Deliverable 1, so `analysis/verify_report.py` can build 100% of Deliverable 2 Part B without missing explanations.
  - Output: `analysis/outputs/unused_source_reasons.json`.
- **Integration:** Orchestrator merges `sec_0_to_3.md`, `sec_4_to_5.md`, `sec_6_to_8.md`, `sec_9_to_12.md` into `reports/2026-10-18-corsa-jakarta-insights-report.md` and runs `python3 analysis/run_all.py`.
- **Git checkpoint:** Commit Wave 3 drafts, merged Deliverable 1, generated Deliverable 2, and claim ledger.

### Wave 4: Independent Verification (Parallel Verifier Subagents)
Independent verifier agents that did NOT write the text inspect the merged report against full CSV rows (including `notes`, `in_force_confirmation`, `amendment_check`, `gaps`), `preverification.csv`, and `model_summary.json`:
- **`V4-Audit-Part1` (verifies Sections 0, 1, 2, 3, 4):**
  - Checks every number, unit, period, base, geography tag, age-fit tag, source URL, balance rule, and absence of HSG internal references.
  - Output: `tasks/2026-10-18-verification-report-part1.md`.
- **`V4-Audit-Part2` (verifies Sections 5, 6, 7, 8, 9, 10, 11, 12 & Deliverable 2):**
  - Checks competitor/price-ladder figures, Oakberry pre-verified claims, Location/Model v0.6 cells, Legal/Halal/Tax citations and time-limits, Section 9 downside completeness, Deliverable 2 completeness, and claim ledger alignment.
  - Output: `tasks/2026-10-18-verification-report-part2.md`.

### Wave 5: Condense, Fix, Re-Verify, Phase 2 Plan & PR
- Apply any fixes flagged by `V4-Audit-Part1` and `V4-Audit-Part2` (via an editor/fixer agent if needed, then re-verify).
- Write `tasks/2026-10-18-phase2-update-plan.md` detailing the exact mechanical + batch pre-verification workflow for folding in tomorrow's updated financial model `.xlsx` and Paul's sources.
- Re-run `python3 analysis/run_all.py` to confirm:
  - Word count <= 10,000 words;
  - 100% factual claim citation or `Analysis:` / `Assumption:` labelling;
  - `data/processed/2026-10-18-claim-ledger.csv` matches Deliverable 1;
  - `reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md` accounts for every source in `sources/sources.md`, every `preverification.csv` row, and every dropped row;
  - 0 open major findings from independent verifiers.
- Commit all changes to `insights-2026-10-18`, push to origin, and open a PR into `main` titled `"Phase 1 insights report (2026-10-18)"` without merging.
