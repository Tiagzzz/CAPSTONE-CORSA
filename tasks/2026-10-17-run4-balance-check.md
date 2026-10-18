# Run 4 balance check: rule 3 (balanced risk sections), Plan 1, 2, 3 reports (W-BAL)

Date of work: 2026-10-18 (task given 2026-10-17). No git commit. Files changed: the three reports below and this log.

## Method

1. Scripts (scratchpad, not committed) loaded the CSVs in scope, kept rows coded VERIFIED-OPENED or CORRECTED-OPENED, and flagged rows whose value, unit, metric, status, notes, snippet, proxy, gaps or reasons text matched a decline, loss, closure, slowdown, boycott, price-resistance, going-concern, "disconfirm", "mixed" or "caution" marker. Table A of `data/raw/2026-10-17-disconfirming-evidence.md` was added by direction (disconfirms or mixed). Scope followed the mapping `data/processed/2026-10-pillar1-mapping.csv` (all in-scope rows are mapped; BLOCKED rows sit in the excluded file).
2. Each flagged row not yet cited was read in full (notes, gaps, in-force and amendment columns where the file has them) and kept or dropped. The keyword pass is a net, not the verdict: the keep or drop decision is a reading of the full row. Regex-only false positives (for example "lower" in a method note) were dropped.
3. "Cited before" means the row id (or, for the disconfirming table, "row N") appears in the report text before my edit. For Plan 3, which cites mostly by register id, a row counted as cited when its figure appears in sections 2 or 3.
4. Tag trace after the edit: every row id in the report resolved in the CSVs, its verification is VERIFIED-OPENED or CORRECTED-OPENED, and the register ids inside the same tag belong to the cited rows.

## Plan 1: `reports/2026-10-17-demand-economics.md`

- Scope: `demand/*.csv` (92 rows), `plan4-spend-drivers.csv`, operator rows of `listed-operators.csv` used for H8, disconfirming table A.
- Edit: new section 2.4 (selection rule, added rows with exact labels and periods, excluded rows), Summary item 6, Appendix. No existing line removed.
- Counts: downside or mixed rows in scope 43 (35 CSV, 8 table); cited before 20 (18 CSV, table rows 6 and 13); added 23; cited after 43. Distinct row ids cited in the report 67 before, 87 after (5 of the 20 new ids are rows named as excluded).
- Added ids: table rows 1, 2, 3, 9, 16, 17; UE-N08, UE-N09, P1C2-02, P1C2-09, P1C2-12, P1C2-13, P1C2-14, P1C2-27, P1C2-29, P1C2-30, P1C2-33, P1C2-34, SD07, P3BF-015, P3BF-022, P3BF-028, P3BF-029.
- Excluded, BLOCKED: table rows 5 (replaced by the opened P1C2-33), 8, 15. Dropped as not downside: UE-N07, P1C1-C01, P1C4-10, SD19, UD-N12 (SD01 stays a context row in section 6).
- Tag trace: 87 row ids, 0 failures (all VERIFIED-OPENED or CORRECTED-OPENED; all register ids match).
- Conclusions affected: none. The added rows are national or regional (ENAK's Jabodetabek cut is Greater Jakarta); no row contradicts a verdict, and the Jakarta half of the H2 criterion stays unmet. The report states this.

## Plan 2: `reports/2026-10-17-regulatory-entry-pathway.md` (accepted; only the section 5 risk text was edited)

- Edit: one paragraph and one table inserted in section 5 before "Surveys". No other line changed (the Summary and Appendix were not touched, so counts are given in section 5 itself).
- Scope: `plan4-origin-boycott.csv`, `2026-10-p2-sentiment-indicators.csv`, operator rows of `listed-operators.csv`, disconfirming table row 13 (= Q6-006).
- Counts: downside or mixed rows in scope 23 (17 operator or boycott rows, 6 survey or political rows S-03 to S-07, S-09); cited before 12; added 11; cited after 23.
- Added ids: Q6-001, Q6-002, Q6-004, Q6-005, Q6-006, Q6-011, Q6-012, UC-N08, P3BF-009, P3BF-018, P3BF-022.
- Excluded, BLOCKED: Q6-003, Q6-010 (named in the report). Not downside: Q6-007, Q6-008, Q6-009 (profit or sales up), Q8-001 to Q8-004 (Mandalika). Consumer-confidence rows left to Plan 1.
- Tag trace (format `[row · register_id · ...]`): 80 row ids, 0 failures except the two BLOCKED ids named as excluded.
- Conclusions affected: none. One point to watch: the Q6-004 notes say the FAST closures had reasons such as lease expiry and relocation, "not only boycott", without a named speaker for the boycott part. The section 5 sentence "none states a boycott cause" is kept; the report says the Q6-004 wording is not relied on. The Q6-012 proxy field "same boycott driver" is a collector label, not a quote, and the report says the cause is not stated.

## Plan 3: `reports/2026-10-17-competitor-map-and-price-ladder.md`

- Edit: new section 2.6, Summary bullet, Appendix. No existing line removed.
- Scope: `listed-operators.csv`, `foreign-entrants.csv`, `price-ladder.csv`.
- Counts: downside or mixed rows in scope 35 (26 operator, 9 foreign entrant, 0 price ladder); cited before 29; added 6; cited after 35. P3BF-007 (Q1 2026 profit) was already cited; the derived Q2 2026 loss of about Rp73.8 bn in its notes is now stated.
- Added ids: P3BF-010, P3BF-011, P3BF-012, P3BF-024, P3BF-025, P3BF-040.
- Excluded, BLOCKED: P3B-17, P3BF-030, disconfirming row 15. Not downside: P3BF-035, P3PB-45, P3PB-50 to P3PB-57. The Starbucks 9M 2025 rows (Q6-005, Q6-006) are outside Plan 3's declared input and are in the Plan 2 report.
- Tag trace: tags are mostly by register id (CMP-); 16 row ids found, 0 failures except BLOCKED P3B-17 and P3BF-030 (named as excluded, existing). One tag in my new text (P3BF-007 with CMP-001) was corrected to cite P3BF-007, P3BF-005 with CMP-002, CMP-001.
- Conclusions affected: none.

## Notes for the verifier

- Plan 2 report file had an mtime later than the others at the start (changed by the lawyer-list worker); I did not touch its other lines.
- The selection is a reading of full rows after a keyword net; an independent verifier should re-run a net with different markers and check that no flagged downside row is missing.
