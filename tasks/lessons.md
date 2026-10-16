# Lessons Learned

After each corrective action, add an entry: date, what went wrong, cause, preventive rule.

<!-- Template:
## YYYY-MM-DD — short title
- **What happened:**
- **Cause:**
- **Preventive rule:**
-->

## 2026-10-16 — Snippet-only collection: errors caught by verification
- **What happened:** In run 1 (hosts blocked, figures taken from search results), independent verifiers found errors or unreproducible figures in about one fifth of the rows: 18 rows were dropped (UNCONFIRMED, DERIVED, duplicate, AUDIT-DISPUTED) and about 20 corrected or downgraded.
- **Error types:** (1) misread subset or category: 6.87% "strongly trust" treated as part of 59.61% "trust" when the source lists them as separate categories; (2) period mix-ups: nine months reported as Q3, a quarter's growth (148.5%) read as full-year, a preliminary one-month count (359) treated as final, wrong qualifier "lowest since September 2025" (June, not July); (3) dates inferred from URL paths or hex IDs instead of read from the page, and survey fieldwork dates confused with publication dates; (4) single-outlet reliance: several figures only appeared in one outlet (Bisnis.com, GoodStats, Tirto) or in republishers of one press text, so a second search was not independent; (5) conflicting headline vs body (Bisnis said GrabFood for Millennials, the body said GoFood; Databoks printed lunch 23% where other sources say 37%); also wrong cited URL (a different Bisnis article than the one carrying the figure), mistyped percentages (-3.22 vs -3.12), and worker arithmetic stored as a data point.
- **Preventive rules:** (a) Record the exact category label and its base for every percentage and check whether categories are additive or nested. (b) State the period type (quarter, 9M, FY, month) in the value cell and never infer it from a headline. (c) Take dates from a page or a second outlet; label URL-inferred dates as such; record fieldwork and publication dates separately. (d) A confirmation counts as independent only if it comes from a different publisher that does not republish the same press text; otherwise mark the row weak. (e) When headline and body disagree, store both and the conflict, and do not pick one without the original. (f) Do not store derived values (differences, durations, sums) as data rows; put them in notes with the formula. (g) Copy the URL of the article that carries the figure, not a related one. (h) Keep snippet-only figures flagged provisional until the source is opened.
