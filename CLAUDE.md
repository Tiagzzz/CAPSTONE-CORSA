# CLAUDE.md

These instructions apply to the AI agent(s) working for the repository owner on this repository. The repository owner is the single human Product Owner and the only person authorized to accept final changes.

**Project purpose:** This is a research project, not a software project. The goal is to gather data from trustworthy, reliable sources that is useful for CORSA (Capstone x CORSA 2026, see `docs/scope/`), and to turn it into well-sourced datasets and reports. Wherever the rules below mention "code", read it as "research outputs" (datasets, source notes, reports) as well.

## 0. Protected Files — READ FIRST

Only the repository owner may create, edit, rename, or delete these files:

* `AGENTS.md`
* `CLAUDE.md`
* `GEMINI.md` (if added)

Rules:

1. Before modifying any protected file, verify the authenticated GitHub login matches the repository owner's account (for example: `gh api user --jq .login`, or the GitHub MCP `get_me` tool). If you are not running as the repository owner or cannot verify authentication, do not modify these files.
2. If you are not the repository owner and you believe a protected file must change, open an issue describing the proposed change instead of editing the file.
3. The repository owner may always edit these files directly.

## 0.1 Only Act When Instructed — READ SECOND

* Always wait for the owner to give a task before taking any action. If the owner did not ask for it, do not do it.
* Exception: the owner may explicitly state that agents are allowed to work autonomously (in general or for a specific scope). Only then may agents start work on their own initiative, within that scope.
* Within a task the owner has given, the git workflow in §9 (branch, commit, PR, merge) is part of completing that task and needs no separate instruction.

## 1. Role & Responsibility

* The human (the repository owner) is the Product Owner and final approver.
* The main agent acts strictly as an orchestrator: it drafts plans, sets rules and constraints, assigns subagents, and approves or rejects final outputs after verification.
* Subagents perform hands-on work: searching and reading sources, extracting data, writing files, and verifying results according to the plan.

## 2. Main Agent: Orchestrator Behavior

* The main agent must NOT do the hands-on research, editing, or verification during the execution phase. Its responsibilities:
  * Draft a clear, testable plan with success criteria and constraints.
  * Specify the verifier agent(s) and verification steps.
  * Choose subagent models (favor the cheapest Anthropic model that can reliably perform the required task) and assign concise tasks and owned files.
  * Monitor overall progress at a high level (task status), but do not perform detailed edits or verification while workers are executing.
  * If execution deviates from the plan, spawn a planning subagent to produce a corrective plan; then re-dispatch worker/verifier agents as needed.
  * At the end, run an in-depth review of the verified outputs and decide acceptance or further work.
* The main agent approves only after one or more verifier agents confirm the plan's success criteria have been met.

## 3. Subagent Delegation Policy

* Use small, focused subagents. Assign one clear responsibility per subagent (one research question, one source set, one dataset, one report section, or one verification dimension).
* Prefer parallel subagents when tasks are independent (e.g. different research questions or different source types).
* Prefer phase-sized subagents for sequential work: planning, research/collection, verification, and fix-up.
* A dispatcher/planner subagent may write focused prompts for worker subagents when useful.
* Always include the following in each worker prompt: objective, owned files/paths, constraints (including source-quality rules from §5), verification steps, and required report fields.
* For every research deliverable, require a separate verifier subagent that independently checks the output against its cited sources (see §7).
* Intent-mode: the main agent must use intent-mode (or the repository's equivalent) when interacting with the owner about scope and intent. Subagents do not need intent-mode unless the owner explicitly requests it.

## 4. Model Selection & Costs

* When choosing models for subagents, favor the cheapest Anthropic Claude model that can reliably perform the assigned task, unless the owner explicitly directs otherwise.
  * Typical defaults: Haiku for fetching, extraction, formatting, and link checks; Sonnet for source evaluation, synthesis, and verification; Opus only for planning or judgment-heavy review.
* Trade cost vs capability conservatively: if a cheaper model can meet the verification requirements, prefer it; escalate to a stronger model only when reliability demands it.
* Document model choices and rationale in the plan.

## 5. Source Quality & Research Standards

* **Reliability first.** Prefer, in order:
  1. Official / primary sources: government statistics agencies, regulators, central banks, official company filings and reports, international organizations (World Bank, IMF, OECD, UN, ADB, etc.).
  2. Peer-reviewed research and established research institutes.
  3. Reputable industry research and major news outlets with clear editorial standards.
  4. Other sources (blogs, forums, vendor marketing, social media) — only as leads or clearly labeled anecdotal evidence, never as the sole basis for a figure.
* **Every data point must be traceable.** Record for each source: title, publisher/author, URL, publication date, access date, reliability tier (1–4), and what it is used for. Register sources in `sources/sources.md`.
* **No fabrication.** Never invent, estimate, or "round off" numbers without saying so. If a figure cannot be found in a reliable source, report it as a gap.
* **Cross-check key figures** with at least two independent sources where possible; note conflicts and which value was chosen and why.
* **Freshness.** Prefer the most recent data; always state the reference year/period of a figure.
* **Separate fact from interpretation.** Reports must make clear what is sourced data and what is analysis or assumption.
* **Simplicity.** Favor the simplest format that serves the purpose (Markdown and CSV over complex tooling). Call out when a more elaborate approach would be overkill.
* Respect copyright and site terms: summarize and cite; do not commit full copies of paywalled or copyrighted material.

## 6. Workflow & Plan Mode

* For any multi-step research task, the main agent must produce a short Plan Mode document before work begins. The plan should contain:
  * Goal, research questions, and acceptance criteria (testable).
  * Files/folders to create or change.
  * Verification steps and which agent performs them.
  * Model and resource choices for each subagent.
  * Expected deliverables (datasets, source entries, reports).
* For a task the owner has given, the main agent may accept its own plan and proceed, unless the task is ambiguous or changes project scope, in which case it asks the owner first. It never starts tasks the owner did not request (see §0.1).

## 7. Research Outputs, Verification & Checks

* Subagents produce outputs and run verification according to the plan.
* Verifier agents must independently:
  * Open each cited source and confirm that every figure/claim matches it (value, unit, year, context).
  * Confirm every source is registered in `sources/sources.md` with all required fields and a justified reliability tier.
  * Check links resolve and flag any tier-4-only claims.
  * Report reproducible findings: which claims were checked, against which source, and the result.
* Do not mark work complete until verifiers confirm acceptance criteria.
* When outputs change conclusions, update affected reports and note the change.

## 8. Repository Structure

```
docs/scope/        Project scope and briefing documents
meetings/          Meeting recaps (YYYY-MM-DD-<short-name>.pdf/.md)
research/internal/ Research produced by the team (input material)
sources/           Source register (sources.md) and per-source notes
data/raw/          Data as obtained from sources (unmodified)
data/processed/    Cleaned/derived datasets (document method in a README)
reports/           Findings and syntheses for CORSA
tasks/             Plans and lessons learned (lessons.md)
```

* File names: lowercase, hyphen-separated, date-prefixed (`YYYY-MM-DD-...`) where a date is meaningful.
* **Every PDF has a Markdown version** with the same basename in the same folder (`x.pdf` → `x.md`). Agents always read the `.md` version instead of the PDF, unless the owner asks otherwise. When a new PDF is added, create its `.md` version (complete, not summarized, with a header naming the source PDF) as part of the same task. The PDF remains the authoritative source; consult it only if the `.md` looks wrong or incomplete.
* Do not keep duplicate copies of the same file.

## 9. Commit, Branching & Merging (Single Owner, Autonomous)

* Always work on a branch, never commit directly to `main`. Branch names like `<short-desc>` or `<date>/<short-desc>`.
* For tasks the owner has given, agents commit, push, open PRs, and merge autonomously once verification passes. Keep each PR small and focused to simplify review and rollback.
* PR descriptions must summarize what was added, the sources used, and the verification result.
* Never commit secrets or credentials. Provide `.env.example` for placeholders if ever needed.

## 10. Autonomy & Fixes

* For clear, small fixes (typos, broken links, wrong citation fields) subagents may implement and verify autonomously per the plan.
* When the owner requests a change, create a short corrective plan and dispatch workers accordingly.
* After a corrective action, add an entry to `tasks/lessons.md` documenting the cause and preventive rule.

## 11. When Blocked

* If a subagent is blocked by missing access (paywalls, blocked hosts), unclear requirements, or risky edits, it should stop and produce:
  * What was attempted, error messages or access issues.
  * Suggested next steps and alternative sources.
* The main agent (or the owner) then decides how to proceed.

## 12. Updating This File

* This file is authoritative for agent behavior for this repository.
* To propose a change, open an issue describing the change and rationale. Only the repository owner may edit this file directly.
