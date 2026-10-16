# Agent performance log

Purpose (owner request): record agents that underperform (issue, changed instructions or model) and agents that perform well or better than expected (reusable prompt pattern). Reuse good patterns; replace underperformers.

| Run | Agent | Model | Task | Outcome | Issue / strength | Action / reusable pattern |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | P4-W7 third place & halal | Sonnet | Plan 4 Q7 | Underperformed vs target: 1 provisional row (target 8–20) | Not the agent's fault mainly: WebFetch DNS-fails and WebSearch returns AI-written summaries without dates or a clear figure-to-URL link, so the agent correctly dropped unmappable figures. Leads logged (Jakpat café n=1,021; GoodStats Sep 2024; Jakarta/Pekalongan/Yogyakarta halal papers). | Keep the strict rule (dropping unmappable figures is the right behaviour). Next prompts: ask for one query per figure, phrased to return the publisher's own page title + date, and require the URL to be cited inline for each figure. Re-run Q7 once hosts open. |
| 1 | P4-W5 community & sport | Sonnet | Plan 4 Q5 | Partial: 8 provisional rows, all snippet-only | Good discipline: left out conflicting padel court counts with unnamed publishers, flagged inferred dates and paraphrased "snippets". Same systemic limit as W7: WebSearch gives model summaries, not raw snippets. | Pattern to reuse: "if two numbers conflict and publishers are unnamed, exclude both and log the conflict". Verifier must treat dates inferred from URLs as unconfirmed. |
