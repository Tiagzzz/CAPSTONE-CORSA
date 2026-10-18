# Run 4 re-check: customer target profiles (V-PROF2, 2026-10-17)

Report re-checked: `reports/2026-10-17-customer-target-profiles.md` after fixes F1-F15 of `tasks/2026-10-17-run4-verification-profiles.md`. Independent re-check; the report was not edited; no git commit. Method: tag parser run over the body (before Appendix A) against the survey-schema CSVs in `data/processed/`, full rows read (value, snippet, notes, proxy_note, geography, age_fit_code, verification), plus a scripted sweep of all verified CSV rows for negative direction that are not cited. Note: the plan4/demand/price/operator CSVs carry no `in_force_confirmation`, `amendment_check` or `gaps` columns (those belong to the legal CSVs); `notes` and `proxy_note` were read in full for every row checked.

## Verdict: ACCEPT WITH FIXES

All 15 fixes are applied and the trace is clean. Two things remain, both small: section 6 still omits a block of verified foreign-chain downside rows although its header says "all verified rows in scope" (F1 not fully closed), and two residual like-for-like slips from F2/F3 survive in places the fixes did not reach. None needs new research; all are text edits.

## Findings (new or residual)

| # | Location | Issue | Sev | Fix |
|---|---|---|---|---|
| R1 | Section 6 header and F1 | Header says "All verified rows in scope ... are listed". Still not cited anywhere in the body (all verified, in-window): Q6-012 (Starbucks Malaysia revenue -36.5%, proxy comparator) and UC-N11 (MAPB: boycott recovery "still ongoing"), both named in the F1 list; P3B-07 / P3BF-018 conflict (see R4); P3BF-010 (FAST auditor going-concern uncertainty, accumulated losses Rp507.63bn), P3BF-011/012 (FAST operating loss, employees 11,664 vs 13,106), UC-N09 and Q6-011 (FAST losses/revenue), P3BF-020 (Pizza Hut outlets 575 vs 591; mixed because Q6-007 shows a return to profit), P3BF-015/017 (MAPB losses; overlap DISC-A13), P3B-06 (Popeyes store EBITDA margin -20.3%), P3B-10 (Mixue 428 closures, scope disputed between outlets), P3BF-041 (Texas Chicken licensee closed all outlets), P3BF-028 (ENAK loss). These all touch 4.2 (foreign-chain comparables). Not missing: P3B-26..29 (HISTORICAL-NOT-IN-BASE-RATE, pre-window; correctly out). | Medium | Add one consolidated row ("other listed-operator and foreign-entrant pressure: FAST going-concern note P3BF-010, ...") with the ids and the reading "foreign-chain pressure; attribution not shown", or change the header to "listed below are the rows most relevant to the profiles; further foreign-chain rows are in `listed-operators.csv` and `foreign-entrants.csv`". |
| R2 | Section 2 "A, spending power" (line 57) | Still compares the August 2025 average wage 5.9 million with the 2026 UMP 5,729,876 (P1C2-21) with no period caveat. F3 was applied in the Summary only. | Medium | Use P1C2-22 (5,396,761) there, as in the Summary, or label the 2026 floor. |
| R3 | Section 8 assumption 1 | "about IDR 100,000 net (110,000 with tax) for a full CORSA visit ... or trade up from a 58,000-65,000 delivery lunch" still sets the blended figure against a lunch comparator (F2 residue). | Low | Say "lunch ticket 120,000 net (132,000 with tax)" or drop the "trade up" clause. |
| R4 | Section 6 Starbucks row | "Closed 11 outlets" (P3BF-018, closure period not stated) while P3B-07 (opened, Starbucks Indonesia H1 2025) says 11 opened and 16 closed, mostly tier-2 cities. Two differing closure figures, one not shown. | Low | Add P3B-07 and state both. |
| R5 | Section 6 savings-index row | P1C2-30/33 groups are defined by savings balance (middle = Rp1-10 million), not expenditure class; the row notes say not to mix them with BPS classes. The report calls it "middle-class savings index". Also P1C2-29 period labels (Q3, "2025") are inferred in the row notes; the report states them flatly. | Low | Say "Mandiri middle savings group" and "(period labels inferred)". |
| R6 | 4.3 price line | "smoothies 45,000-47,000 [P3PR-013, P3PR-016]" omits P3PR-018 (47,000) that the section 3 table does tag. | Low | Add P3PR-018. |
| R7 | Tag P1C1-S07 | Row age code n/a, tag D (trivial, unchanged from V-PROF). | Low | Ignore or recode. |

## Check results

### (1) Section 6 completeness and counts
- DISC table A rebuilt from the file: verified rows are 1, 2, 3, 6, 9, 13, 16, 17 (5, 8, 15 BLOCKED). All 8 are cited (A9 and A17 now added as "mixed"; A1/A2/A3 in the confidence row; A6, A13, A16 as before). BLOCKED rows 5, 8, 15 are named in section 7 only. Pass.
- From the CSV sweep, the V-PROF F1 list is applied: P1C2-09, P1C2-29, P1C2-30, UE-N08, UE-N07, Q6-004, UC-N08, Q6-002, Q6-001, P3BF-018, P3B-05, SD07, P4W9-17, P4W9-26, UB-11, P4W3-07, and the balancing P4W4-01 are all present with correct values (checked against the full rows: 0.9% vs 4.6% and 6.4%; 4.7% vs 6.1%, Sep 5.5%; 100.5 and 95.1 vs 94.0; 26.9% vs 19.5%; 19 outlets/about 400 vs 20/1,041; 138 vs 147; 53%, 14%, 34%, 51%; 48%). Still missing: R1 list.
- Counts: section 6 holds 64 distinct ids; the Summary says "about 60 rows" (acceptable). The Summary says 180 distinct CSV rows plus 8 DISC; my parse gives 188 distinct ids = 180 CSV + 8 DISC; Appendix A says 188. All three agree. Every cited id appears in Appendix A and Appendix C (0 missing). Appendix A list of DISC rows includes A9 and A17.

### (2) F2 and F3 arithmetic recomputed from the rows
- tkt_lunch (03-inputs.csv line 36): 110,000 / 120,000 / 135,000 net, "Avg net spend – lunch (pasta + drink)". Report: 120,000, range 110,000-135,000. Pass.
- 120,000 / 65,130 = 1.84 (1.8 OK); x1.1 = 132,000 / 65,130 = 2.03 (2.0 OK). 120,000 / 58,609 = 2.05 (2.0 OK); 132,000 / 58,609 = 2.25 (OK).
- 132,000 / 5.9m = 2.24% (2.2% OK); 4 x 132,000 = 528,000 / 5.9m = 8.95% (report 8.9%; rounding to 9.0% would be equally valid, immaterial).
- 5.9 / 5.396761 = 1.093 (about 9% OK; UMP 2025 effective calendar 2025, so in force in August 2025). 5.9 / 5.729876 = 1.030, i.e. the 2026 floor is 2.9% below the average (about 3% below OK). 5.9 / 3.33 = 1.77 (1.8 OK). Feb 2025 4.88 million in the row notes (OK). F3 applied in the Summary; residue R2.
- F2: blended 100,000 now labelled as a different measure in the Summary, section 3 and 4.3; residue R3.

### (3) F4-F15
F4 applied (lines 168-169: families with reason, nightlife "not researched"). F5 applied (P4W10-02 and P3BF-033 now proxy; one rule stated in the tag section, line 8, and applied consistently: Jakarta all-age rows "evidenced" for the area fact, "proxy" in location and judgement lines). F6 applied (397 "unit unresolved", not comparable with 326). F7 applied (measure named, +25% against +9.4% verified in E02/E04 rows, South leads on total spend). F8 applied (P1C2-30 beside P1C2-33). F9 applied ("deposits held in accounts above IDR 2 billion"). F10 applied (P3PR-018, -020, -021 in the table; see R6). F11 applied (re-code stated in section 1 coding notes). F12 applied (Bogor and Depok named; both appear in the P4W1-R04 and UA-N58 rows). F13 applied ("among the verified rows"). F14 applied ("Analysis:" prefix on the three concept-fit bullets and 4.3 price line). F15 applied (Appendix A no longer cut mid-word; Appendix B adds 31,000 marathon runners, 48.9% Gen Z or Millennials, 17% prepared-food share).

### (4) Full tag trace
- 178 tags parsed, 188 distinct ids. Row exists: 180 of 180 CSV ids; verification VERIFIED-OPENED or CORRECTED-OPENED: 180 of 180. The 8 DISC rows are all table-A rows with those statuses. No BLOCKED row is used in any tag; BLOCKED ids occur only in section 7 (and the named rows 5, 8, 15).
- Geography letters: match the row for every tag except P1C3-02, UE-N06, P4W10-08 (row J, tag J*); section 1 states the re-code from the notes. Accepted. (Rows with descriptive text such as "South Jakarta (kota)" map to J.) Age-fit letters match all rows except P1C1-S07 (R7).

### (5) New claims introduced by the fixes, traced to rows
+25% and +9.4% (P1C1-E02, E04 snippets); Central 513,174 (E03); South total 4.08 million and rank 1 of 6 (UE-N01); 2.36 million (P1C1-S07); 5.9/5.396761 (P1C2-22); 1.8x national and 4.88 million (P1C2-23 notes); 100.5, 95.1, 94.0 (P1C2-30); layoffs 23,470 and 49% (DISC-A9, UE-N07, computed 23,470/46,015 = 0.51); GDP 5.29% (DISC-A17); 0.9/4.6/6.4 (P1C2-09); 4.7/6.1/5.5 (P1C2-29); 26.9/19.5 (UE-N08); FAST 19/400 and 20/1,041 (Q6-004, UC-N08); 138 vs 147 (P3B-05); SD07, P4W9-17 (53%), P4W9-26 (14%), UB-11 (34%), P4W3-07 (51%), P4W4-01 (48%). All traced to rows; no untraced figure. Caveats on P1C2-29 and P1C2-30 definitions: R5.

### (6) Length
Whole file: 10,419 words. Body before Appendix A: 7,925 words including the bracketed tags; 6,801 words with the tags stripped. Appendices A to C add about 2,500 words.

## Required before acceptance (none blocks the Summary's conclusions)
R1 and R2 (Medium) should be fixed; R3-R6 are polish. No further research needed. After the edit, re-check only section 6, line 57 and assumption 1.
