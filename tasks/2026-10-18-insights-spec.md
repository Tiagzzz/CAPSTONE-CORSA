# Task: turn the CORSA repo into an actionable insights report (Phase 1 of 2)

You have access to the GitHub repo `Tiagzzz/CAPSTONE-CORSA`. I am Tiago, the repo owner and Product Owner; this message is your task. Read `CLAUDE.md` in the repo root first. Its rules apply to you as well, especially §5 (source quality) and §9 (git workflow); the merge rule is overridden in section 9 of this prompt. Do not edit `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

## 1. Your role

You are the **orchestrator**. You plan, split the work, spawn sub-agents, integrate their output and check it.
- **Sub-agents:** you may spawn **Gemini sub-agents only**.
- **Economic interpretation:** use **Gemini Argon agents** for demand, income, pricing, unit economics, the financial model and macro.
- **Scripts first:** write Python scripts for everything that can be computed or checked mechanically.
- **Agents for reading and judgement:** use agents only for what needs reading or judgement: interpreting documents, synthesising, writing and verifying.

## 2. Context

- **Client:** CORSA, a Swiss café brand (Italian pasta, specialty coffee, functional drinks, community) planning its first international flagship in Jakarta. The readers are the founders, Samuel and Joshua, who are investor-minded and not food-industry experts.
- **Scope:** `docs/scope/2026-capstone-x-corsa-scope.md`.
  - Pillar 1 (§6, strategic fit) asks for: a strategic fit assessment; a competitor and benchmark map, with **Oakberry as the mandatory benchmark**; a target customer overview; cultural fit; clear implications; and customer, location and validation priorities for a 90-day roadmap.
  - Pillar 2 (§7) is the Jakarta financial model and business case.
- **Deadline:** the **interim presentation is on 21 Oct 2026** (decided in Meeting 5; the scope's "22 Oct" is out of date). We will build the presentation from your report.
- **Dropped by me:** the scope's Singapore, Dubai and Hong Kong comparison. Do not cover it.
- **Two phases:**
  - **Phase 1 (today):** the full report from the data in the repo now.
  - **Phase 2 (tomorrow):** Jonas and Marius will update the financial model (a new `.xlsx`), and Paul will deliver additional sources. Both must then be checked and folded into the report. Build everything today so that Phase 2 is a re-run and a targeted update, not a rewrite (section 7).

## 3. What is in the repo, and how far to trust it

| Area | Content | Trust |
|---|---|---|
| `data/processed/*.csv` | About 655 research rows: demand, middle class, spend, consumer behaviour, price ladder, competitors, regulation, tax and franchise, environment, CAGE. `2026-10-pillar1-mapping.csv` has 574 rows (each verified row mapped to PESTEL and CAGE dimensions); `2026-10-pillar1-mapping-excluded.csv` holds the rows left out | Each row has `verification`, `geography` (J Jakarta, J* Jakarta-coded with caveat, U urban Indonesia, N national, P proxy) and `age_fit_code` (A exact to D none). `VERIFIED-OPENED` and `CORRECTED-OPENED` rows can be used directly. `BLOCKED` rows are unverified: use one only after it passes pre-verification (section 8, wave 2b) |
| `sources/sources.md` | Register of 325 sources with tier (1 official to 4 other) | Cite through this register |
| `reports/` | AI syntheses, all independently verified: PESTEL, CAGE, customer target profiles, purchase triggers (Plan 4), demand economics (Plan 1), regulatory entry pathway (Plan 2), competitor map and price ladder (Plan 3), framework outline, gap analysis | Good starting point. They are long (CAGE about 14,000 words, profiles about 8,500), so **condense them; do not re-research what they already cover** |
| `research/internal/` | Team work: Tiago's customer behaviour report and extended data, the target-customer brief, Paul's first research, Matthieu's CAGE files (culture, administrative, geographic, economic), Ana's Oakberry benchmarks (the 2026-10-18 PDF is the newest), the finance overview | Team claims. Already verified: the CAGE report's claim register (161 of Matthieu's 174 claims) and any claim that matches a verified row. Every other team claim you want to use must pass pre-verification first (section 8, wave 2b) |
| `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.*` | Financial model v0.6 (Jonas and Marius): the `.xlsx`, 20 CSVs of cached values, and an index `.md` with a completeness check | Read the completeness check. PnL_Monthly covers only 13 of 60 months, so years 2 to 5, the NPV and the IRR are **not valid**. Many inputs are placeholders (the README says so; the menu prices are illustrative). Year-1 figures, break-even, steady-state scenarios and simple payback are usable, with the caveat stated. The model's own `Sources` sheet (S01 to S104) has not been independently verified, so any model input you state as a market fact (for example a district's rent level) must pass pre-verification |
| `meetings/` | AI-generated meeting recaps with transcripts | Use them **only** for decisions, requirements and owner preferences. They contain speech-to-text errors, so never use them as evidence for market facts |
| `tasks/` | Plans, verification logs, the audit (`2026-10-17-main-session-audit.md`), the lawyer and tax questions (`2026-10-17-lawyer-and-tax-questions.md`), lessons | Read the audit and `lessons.md` before starting |

**Known limits of the data, to state in the report rather than hide:**
- About half the rows are national (N), most have no age split, and about two thirds are tier-3 relays. **No verified Jakarta row for ages 25 to 39 exists.**
- An independent re-check of 54 random rows found 0 wrong figures; the weak points are framing and labels.
- Still open:
  - the independent check of 11 label fixes (`tasks/2026-10-17-run4-label-fixes.md`);
  - re-checks due on 19 to 20 Oct: the halal Minister decision (row H-12), the BPJPH provisions (H-04) and any new Jakarta PBJT tax-cut decree (T-07);
  - in the Plan 2 report, one source-less "Art. 197" claim and an unsourced CHF rate.

## 4. Rules for every claim

1. **Every factual claim has a source, cited inline:**
   - **External sources:** a Markdown link to the source URL plus the repo row id, e.g. `([BPS via Databoks](https://...), P1C1-F05; J-D)`.
   - **Team files:** the repo path, e.g. `(team: research/internal/2026-10-08-customer-behaviour-report.md)`.
   - **The financial model:** sheet and cell, e.g. `(model v0.6: Dashboard!B8)`.

   A sentence without a source is either labelled **"Analysis:"** (your interpretation) or **"Assumption:"**.
2. **Derived numbers** (sums, medians, ratios) are computed by a script in `analysis/`. The report names the inputs; never type a number by hand.
3. **State the evidence level** wherever a claim could be read as Jakarta-specific: Jakarta, urban Indonesia, national, or proxy, and whether it has an age split. Do not present national data as Jakarta data.
4. **Balanced:** every section that concludes something also states the verified evidence pointing the other way. See the "Facts pointing the other way" sections of the existing reports, and `data/raw/2026-10-17-disconfirming-evidence.md`.
5. **Verify before use:** unverified data may be used, but only after a verifier agent has confirmed it (section 8, wave 2b). Unverified data covers BLOCKED rows, team claims outside the CAGE register, model input sources, and tomorrow Paul's sources. Data that fails verification is not used as fact. It goes into Deliverable 2, Part B, with the reason.
6. **No fabrication:** if a figure does not exist, write it as a gap and say what research would close it.
7. **No names of HSG staff, and no university-internal matters.** The audience is CORSA.
8. **Time-limited rules** (programmes, decrees, discounts) state their validity period and whether they still apply.

## 5. Deliverable 1: the report

**File:** `reports/2026-10-18-corsa-jakarta-insights-report.md`.

**Length:** at most **20 pages of text and links**, which means **at most 10,000 words**, counted by script, excluding Deliverable 2.
- Simple Markdown tables are allowed. No images or charts.
- Lead with conclusions. Each section answers: **why we looked, what the data says, what it means for CORSA, what to do next.**

**Structure** (page budgets are guides; you may add a section if the scope or data needs one, and say why in the changelog):

0. **Executive summary (1 page).** Is Jakarta a sound first flagship, under which conditions, and how should CORSA enter? Then **8 to 12 key messages for the 21 Oct presentation**, one sourced sentence each.
1. **Question, evidence base and limits (half a page).** What the scope asks, what data exists, how strong it is, and what Phase 2 will change.
2. **PESTEL: the Jakarta operating context (about 2.5 pages).** Political, Economic, Social, Technological, Environmental and Legal. For each, give the 3 to 5 factors that matter most for CORSA, the implication, and a confidence level. Derive it from `reports/2026-10-17-pestel-jakarta.md` and the mapping CSV.
3. **CAGE: Switzerland to Jakarta (about 2.5 pages).** Cultural, Administrative, Geographic and Economic. For each: the distance, what it means for CORSA, and whether it **transfers, needs adapting, or must be tested**. Note where entering through an Indonesian network reduces the administrative distance. Derive it from `reports/2026-10-17-cage-switzerland-jakarta.md` and Matthieu's files.
4. **Four target groups, ranked from most to least relevant, and their customer behaviour (about 3.5 pages).**
   - **Ranking criteria:** state them first: size and concentration in Jakarta, spending power and fit with CORSA's price level, behavioural fit with the concept, reachability through channels, and strength of evidence.
   - **For each group:** who they are (age band, income or spend level, districts, occupation); occasions; discovery channels and purchase triggers; price tolerance against the price ladder; which parts of CORSA fit; what must be adapted; and what still needs testing.
   - **Sources:** start from `reports/2026-10-17-customer-target-profiles.md`, `reports/2026-10-17-purchase-triggers-and-channels.md`, the price ladder and Tiago's customer behaviour report, and reconcile them.
   - **Distinct groups:** the profiles report treats "lifestyle café-goers" as an overlay rather than a separate group. Your four must be distinct, or you must explain why not.
   - Say which groups were dropped (for example students, creators and expats) and why.
5. **Competitors, benchmarks and price position (about 2 pages).**
   - A competitor map and where CORSA sits on the price ladder.
   - **Oakberry lessons:** what made it scalable, how it simplified the product, how it translated internationally, the role of health and convenience, risks to avoid, and how CORSA differs.
6. **Location (about 1 page).** Which districts suit which target group, rent levels (model Rent_Data and Location sheets), and the footfall gap.
7. **Entry route and regulation (about 1.5 pages).**
   - PT PMA requirements (the IDR 10bn investment-plan test, paid-up capital), halal, franchise rules and tax.
   - Which entry modes stay open within CHF 200k.
   - Which questions need a lawyer (from the lawyer and tax list).
8. **Financial case (about 2 pages; use Argon agents).**
   - Model v0.6 status and its key outputs for the conservative, base and optimistic scenarios.
   - What drives the result (the Sensitivity and MonteCarlo sheets).
   - What is not valid yet (the 13-month P&L, placeholder inputs).
   - What the Phase 2 model update must fix.
   - Put every model figure in one script-generated table, so Phase 2 can regenerate it.
9. **Key risks and facts pointing the other way (about 1 page).** All verified downside evidence: middle-class budgets, real wages, savings, eating out being cut, foreign-brand performance and boycotts.
10. **Recommendations and strategic implications (about 1.5 pages).** Keep, adapt or test. Conditions for go, adapt and stop. Recommendations follow from the analysis and are labelled as such.
11. **90-day validation roadmap priorities (about 1 page).** Customer, location and validation priorities, and the primary-research brief: what to ask, whom, and how.
12. **Open points and Phase 2 (half a page).** Close with a short **changelog**: v1.0 is Phase 1.

## 6. Deliverable 2: the source appendix

**File:** `reports/2026-10-18-corsa-jakarta-insights-sources-appendix.md`.

- **Part A, sources used:**
  - columns: ID, title, publisher, tier, publication date, URL, report sections, number of claims;
  - plus the team files and model sheets used.
- **Part B, sources not used, with a reason for each:**
  - every register entry not cited in the report, the BLOCKED rows not confirmed in wave 2b, the NOT-CONFIRMED and UNREACHABLE pre-verification items, and the dropped rows;
  - use a reason code and one line of explanation:

  | Code | Meaning |
  |---|---|
  | `BLOCKED` | The source could not be opened (bot challenge, 403, page gone), so it could not be verified |
  | `NOT-CONFIRMED` | Pre-verification opened the source, but it does not support the claim (value, period, base or wording differ) |
  | `OUT-OF-WINDOW` | Before the 2024-10-16 cutoff, or superseded |
  | `DUPLICATE` | The same fact comes from a stronger source |
  | `TIER4-LEAD` | Lead only |
  | `CONTRADICTED` | A stronger source conflicts |
  | `OFF-SCOPE` | Not needed for the report's questions; name the question it served |
  | `CONDENSED-OUT` | Relevant but cut for length; name the section of the long report that still holds it |

- **Part C, pending:** a placeholder for Paul's sources (Phase 2).

Generate Parts A and B by script from `sources/sources.md`, the claim ledger, `data/processed/2026-10-18-preverification.csv` and `data/processed/2026-10-16-run1-dropped-rows.csv`. An agent writes only the reasons a script cannot know (`OFF-SCOPE`, `CONDENSED-OUT`).

## 7. Working files, for verification and Phase 2

- **`analysis/`:** Python scripts and one entry point, `analysis/run_all.py`, which accepts the model path as an argument. The scripts must at least:
  - inventory the repo files and sources;
  - extract the model outputs (all three scenarios), the sensitivity ranking and the completeness flags from the `.xlsx` with openpyxl, reading cached values;
  - compute price-ladder and demand statistics;
  - check links (HTTP status only, no bot-challenge bypass);
  - build the claim ledger;
  - check that every factual sentence in Deliverable 1 has a citation or an "Analysis:" or "Assumption:" label;
  - count words;
  - generate Deliverable 2's Parts A and B and the model-figures table.
- **`data/processed/2026-10-18-claim-ledger.csv`:** one row per claim in Deliverable 1. Columns: `claim_id`, `section`, `claim`, `source_ids`, `evidence_level`, `type` (fact, analysis or assumption), `depends_on` (`model_v0.6`, `team_unverified`, `paul_pending` or `none`), `verification` (the row's existing label, or the pre-verification `item_id`), `verified_by`.
- **`data/processed/2026-10-18-preverification.csv`:** one row per item checked in wave 2b. Columns: `item_id`, `origin` (BLOCKED row id, team file and claim, model source S-id, or Paul source), `claim`, `source_url`, `verdict` (CONFIRMED, CORRECTED, NOT-CONFIRMED or UNREACHABLE), `evidence_quote` (25 words or fewer), `corrected_value`, `checked_by`, `checked_on`. Do not change the `verification` column of the existing CSVs; this file records the new verdicts.
- **`tasks/2026-10-18-insights-plan.md`:** your plan. Write it **before** spawning agents: the waves, which agent owns which files, inputs and outputs.
- **`tasks/2026-10-18-phase2-update-plan.md`:** the exact steps for tomorrow:
  - run `run_all.py` on the new model;
  - diff the model figures;
  - for Paul's sources: register each with its tier, send them through the same batch pre-verification as wave 2b, then map the confirmed ones to sections and claims, and update or add claims;
  - re-run the checks, then bump the report to v1.1 with a changelog.
- **Verification logs:** one file per verifier pass in `tasks/`.

## 8. How to run it (orchestration)

1. **Plan.** Read sections 3 and 4 of this prompt, `CLAUDE.md`, the audit and `lessons.md`. Write the plan file.
2. **Wave 1, scripts (you or a coding agent):** inventory, model extraction, statistics, link check, the ledger skeleton.
3. **Wave 2a, readers (parallel Gemini agents, each with named files and a fixed output file):**
   - team files: Tiago's reports, Paul, Matthieu, Ana's Oakberry;
   - the existing AI reports, condensed per section;
   - **Argon agents** for the economics: demand and middle class, price positioning, the financial model.
   - Each returns sourced bullet notes with citations, and flags every unverified item it wants to use as "needs pre-verification".
4. **Wave 2b, pre-verification of unverified data (batch verifier agents):**
   - **Batches:** collect every flagged item (BLOCKED rows, team claims outside the CAGE register, model input sources the report states as fact) and split them into batches of about 10 to 15 sources. Group by source or website, and give one batch to each verifier agent.
   - **Independence:** a verifier never checks data it collected or a text it wrote.
   - **Method:**
     - open the original source yourself (no bot-challenge, login or paywall bypass);
     - check value, unit, period, base and geography, and that the quoted wording is on the page;
     - for a team claim, find the source the team cited, or failing that a reliable source with the same fact.
   - **Record:** write each verdict to `data/processed/2026-10-18-preverification.csv`, and one log per batch to `tasks/2026-10-18-preverification-batch-N.md`. Register every newly opened source in `sources/sources.md` with its tier.
   - **Use:** only CONFIRMED and CORRECTED items (with the corrected value) may be used. NOT-CONFIRMED and UNREACHABLE items go into Deliverable 2, Part B.
   - **Spot-audit:** have a second, different agent re-check about 10% of the CONFIRMED items. If it disagrees on any item, re-check that whole batch.
5. **Wave 3, writers:** one agent per section group, each owning its sections. Writers use only verified rows and wave-2b CONFIRMED or CORRECTED items. No two agents edit the same file; you merge the sections into Deliverable 1.
6. **Wave 4, independent verification:** agents that did not write the text check every claim against the cited source or row: value, unit, period, base and geography. They also check the balance rule and the evidence labels. Give verifiers **full rows**, including the `notes` columns. Fix, then re-verify any major finding.
7. **Wave 5, condense and finish:** an editor agent cuts to 10,000 words or fewer without dropping a sourced conclusion. The scripts confirm the word count, citation coverage, the ledger and Deliverable 2. Then write the phase-2 plan.

Keep each agent's task small and focused. Prefer several short agents to one long one.

## 9. Git, finish and report back

- Work on a branch, `insights-2026-10-18`, and commit after each wave.
- Open a PR into `main` titled "Phase 1 insights report (2026-10-18)". **Do not merge it**; I review it first.
- Do not edit the team files in `research/internal/` or `docs/scope/`, the model `.xlsx`, or the existing reports. New work goes in new files.
- **Done means:**
  - Deliverable 1 is 10,000 words or fewer and every factual sentence is sourced or labelled;
  - all PESTEL dimensions, all four CAGE dimensions, four ranked target groups linked to customer behaviour, and the Oakberry lessons are covered;
  - every unverified item used in Deliverable 1 passed wave 2b and is recorded in `preverification.csv`;
  - Deliverable 2 lists every source as used or not used, with a reason;
  - the verifiers have no open major findings;
  - the phase-2 plan is written.
- **Final message:** word count, claim count (fact, analysis and assumption), number of sources used and not used, pre-verification results (items checked, and counts of CONFIRMED, CORRECTED, NOT-CONFIRMED and UNREACHABLE), open issues, and anything you could not do and why.
