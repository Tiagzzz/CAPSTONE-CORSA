# Plan — Gap analysis and top-4 data-gathering plans (Team A, Jakarta entry)

Date: 2026-10-16. Owner request: identify the key information CORSA needs, pick the top 4 data needs, and have 4 agents each draft a plan to gather one of them. Stop for owner approval after the plans; no data collection yet.

## Constraints (from the owner)

- Reliable sources only (CLAUDE.md §5 tiers 1–3; tier 4 only as leads).
- Public and free sources only.
- Recent data only: published within the last 2 years (on or after 2024-10-16). This does not apply to cyclical or long-run trend series.
- Related or proxy data is allowed (e.g. how much innovation drives purchases) if it is labelled as a proxy.
- Behaviour may be split by age group or target segment.
- Stay inside Team A's scope (Pillar 1 Strategic Fit: research and benchmarking, culture and geography, experiential marketing). Team B owns the financial model and the economics of location choice.
- Jakarta is fixed as the market. The question is how to enter well, but the plans must test the entry assumptions against evidence and not just confirm them.
- Every figure must have a registered source. A figure without one is reported as a gap and left out.

## Phases

| # | Phase | Agent | Model | Output |
| --- | --- | --- | --- | --- |
| 1 | Analyse existing research and list gaps without bias | gap-analyst | Sonnet (needs careful reading and judgment; Haiku is too weak for critical review) | `reports/2026-10-16-existing-research-gap-analysis.md` |
| 2 | Pick the top 4 data needs | main agent | — | section below |
| 3 | Write 4 data-gathering plans, in parallel | planner-1…4 | Sonnet (planning and source evaluation; Opus not needed for a plan with checklists) | `tasks/2026-10-16-plan-<n>-<topic>.md` |
| 4 | Review the plans against the constraints | main agent | — | approve, or send back for fixes |
| — | Owner approval | owner | — | **stop point** |

## Acceptance criteria

- The gap analysis cites a repo file and section for every statement about existing research. It separates claims that are sourced, unsourced/assumed, and contradicted, and lists the open gaps for Team A.
- Each plan states its research questions, candidate sources (named publisher plus URL where known, tier, free/public, expected reference year), method, a proxy strategy, a segmentation approach, how it tests the entry assumptions (disconfirming evidence), the sub-agent breakdown with a model for each, verifier steps, output files, acceptance criteria and risks/gaps.
- No plan relies on a paid, private or tier-4-only source for a figure.

## Known blocker

- The Google Drive folder (https://drive.google.com/drive/folders/1ZdIT3RJRcRrjaVmce6j72oap86LNyeuV) cannot be reached: the network policy denies drive.google.com and there is no Drive connector. The files there cannot be added to the repo or analysed until the owner allows access or uploads them.

## Update — Drive access granted

The owner granted Drive access, and the folder was imported (`tasks/2026-10-16-drive-import-log.md`). The gap analysis was then extended to cover the imported files.

## Top-4 data needs (main agent decision, based on gap analysis v2 §4)

| # | Data need | Gaps covered (gap analysis §4) | Why it ranks in the top 4 |
| --- | --- | --- | --- |
| 1 | **Target-segment demand economics by age/segment**: the real size and income of the target pool, food-away-from-home and café spend, willingness to pay, visit frequency, and wheat/pasta and healthy-food consumption | Gap 1, gap 6, the population gap; middle-class contradiction T-series | The base case assumes 200 guests a day and has no frequency or capture input. The "growing middle class" claim is contradicted by the team's own data. |
| 2 | **Regulatory, political and entry-route pathway**: PT PMA/foreign ownership and investment thresholds, licences (OSS), halal obligations for a foreign F&B outlet, taxes (PBJT), labelling and sugar rules, franchise rules, political and boycott risk to Western brands | Gaps 2 and 11, T16, T17, T28 | This could block entry or change the entry mode. It can be filled from official, free sources. |
| 3 | **Competitive landscape and price ladder in the target districts**: competitor map (Italian/pasta, specialty coffee, healthy bowls, lifestyle/community concepts), published price points, formats, listed-company performance, and foreign-entrant successes and failures in Jakarta | Gaps 3 and 4, T18, T21, T23 | Team B is waiting on Pillar 1 for one reconciled price ladder, and the competitor map is a required scope output. |
| 4 | **Behavioural purchase triggers and acquisition channels by age group**: novelty/innovation sensitivity, health, social proof and influencers, community and sport (running), media and platform use, and the effect of trust in foreign or Italian brands | Gaps 7 and 8; cultural transfer (gap 9) | This is the core of Tiago's experiential-marketing remit. Related or proxy data is explicitly allowed. |

Deferred: micro-location and footfall (gap 5) needs primary counts and overlaps with Team B's economic location choice, so it is only touched as a proxy inside plans 1 and 3. Local expert validation (gap 8) needs primary interviews, so each plan lists the questions it would hand to the team.

## Phase 3 dispatch

Four Sonnet planners run in parallel, one per data need. Each writes `tasks/2026-10-16-plan-<n>-<topic>.md`. They may do a light source-availability check (that a source exists and is free, public and recent) but must not collect data.
