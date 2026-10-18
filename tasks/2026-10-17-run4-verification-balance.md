# Run 4 verification: balance check (V-BAL), Parts A and B

Verifier: independent (did not write the work). Date: 2026-10-18. Nothing edited except this file. No commit.
Inputs read: CLAUDE.md section 5/7, `tasks/lessons.md` (last two entries read in full), `tasks/2026-10-17-run4-balance-check.md`, the three reports, the CSVs in scope (full rows including notes, gaps, in-force, amendment), `data/raw/2026-10-17-disconfirming-evidence.md`, `tasks/2026-10-17-lawyer-and-tax-questions.md`.

## Verdicts

| Part | Verdict |
|---|---|
| A. Plan 1 `demand-economics.md` | **ACCEPT WITH FIXES** (2 low fixes) |
| A. Plan 2 `regulatory-entry-pathway.md`, section 5 | **ACCEPT WITH FIXES** (1 medium fix: the "none states a boycott cause" statement is contradicted by opened rows) |
| A. Plan 3 `competitor-map-and-price-ladder.md` | **ACCEPT WITH FIXES** (low fixes: facts omitted from rows already cited) |
| B. `lawyer-and-tax-questions.md` | **ACCEPT WITH FIXES** (1 medium: L20 repeats the Plan 2 statement; low: wording and tags) |

No wrong figure was found in any added row. The one substantive problem is a balance problem of exactly the type the run-4 lessons describe (a risk statement that is wider than the rows allow).

## Part A

### A1. Independent downside list (different markers)
Method: I read the worker's method (log lines 1 to 4), then scanned all VERIFIED/CORRECTED rows in each scope with a different marker set: closure, closed, exit, loss, declin, slowdown/slow, fell, lower, cut, weak, no evidence, disconfirm, contradict, conflict, mixed, boycott, resist, falling, did not, not significant, drop, decrease, shrink, negative, unemploy, layoff, PHK, turun, rugi. I also read table A of the disconfirming file (rows 1, 2, 3, 5, 6, 8, 9, 13, 15, 16, 17). Every flagged row not named in a report was then read in full.

- **Plan 1:** 25 flagged rows not named. Read in full: P1C2-17 (confidence by age, young adults most confident; 31-40 durable-goods index lower is a different index; not downside), P1C1-P01/P05 (keyword "drop" only), P1C4-22 (noodles up; interested party), SD11/12/13 (QRIS growth), SD17 (PayLater stock; the "no evidence" is a method note), and operator rows for FAST, MAPB, PZZA, ENAK not used for H8. No verified downside row that matters to a Plan 1 verdict is missing. The worker's count (43 = 20 + 23, 35 CSV + 8 table) checks out: the 23 added are 6 table rows, UE-N08, UE-N09, 10 P1C2 rows, SD07, 4 P3BF rows. The table has 11 rows, 8 kept (1, 2, 3, 6, 9, 13, 16, 17), 3 BLOCKED (5, 8, 15).
- **Plan 2:** 17 flagged operator rows not named in the report. All are in `listed-operators.csv`. Q6-xx and S-xx rows: nothing missed (all flagged rows were already cited). Operator rows left out of Plan 2 that Plan 3 counts as downside: P3BF-007 (FAST Q1 2026 profit not holding: Q2 loss about Rp73.8 bn), P3BF-010 (auditor going-concern, accumulated losses Rp507.63 bn), P3BF-011 (FY2025 operating loss Rp312 bn), P3BF-012 (FAST employees -11.0%), P3BF-024 and P3BF-025 (PZZA Q1 mixed; PZZA headcount -2.6%), P3BF-019 (MAPI context, "disconfirming"). They concern the same three operators as the section 5 table, so the scope rule ("operator rows") is applied inconsistently between the Plan 2 and Plan 3 reports (finding A-5). Not wrong, but section 5 says "23 rows in scope" while Plan 3 counts 26 operator rows for the same file.
- **Plan 3:** all 26 operator rows and the foreign-entrant rows P3B-04, -05, -06, -07, -08, -09, -10, -16 are named or carried by figure (the report cites by register id, so a row-id scan alone is not a valid test; I matched by figure). Price-ladder flags (P3PR-025 to 030 "weak", P3PB-16/29 to 33 "mixed", P3PB-51 to 59 "conflict") are price-quality notes, not downside: agree with the worker. No uncited verified downside row found. Facts inside cited rows that are not stated: see A-6.

### A2. Added rows read in full (confirm labels, values, periods, geography)
Rows read in full and compared with the added report text (38): Q6-001, -002, -003, -004, -005, -006, -010, -011, -012; UC-N08; P3BF-005, -007, -009, -010, -011, -012, -015, -018, -022, -024, -025, -028, -029, -030, -040; P1C2-02, -09, -12, -13, -14, -17, -27, -29, -30, -33, -34; UE-N07, -N08, -N09; SD07, SD19. Plus P3BF-002, -003, -004, -017, -019 to -023, -026, -027, -034, -035, -037, -041 and foreign-entrant rows P3B-01, -02, -04 to -10, -16, -17.
Result: labels, values, periods and geography match the rows in every case. Checked computations: FAST employees 11,664 vs 13,106 = -11.0%; PZZA headcount 4,085 vs 4,192 = -2.6%; CFC 19.38 vs 21.03 = -7.8%; ENAK Jabodetabek 636.04 vs 711.06 = -10.6%, share 58.8%; Q2 2026 FAST loss 61.1 + 12.7 = 73.8; layoffs 23,470 vs 46,015 = -49%. Notes:
- P1C2-29: the report says "overall MSI growth 5.5% in September, lowest since Nov 2025" (row: Q3 5.9%, September 5.5%) and says the period labels are inferred, as the row does. OK.
- P1C2-33 text drops the countervailing figures the row records on the same page (MSI +6.5% yoy; middle-class IKK rising for two bands). Low (A-2).
- UE-N08: the value is "read from chart label" in the row; the report does not say so. Low (A-2).
- Q6-001 "loss narrowed 56.99%": 56.99% is a computation (557.08 to 239.58), the row says "about 57%". Not labelled "computed". Low (A-4).

### A3. Excluded and dropped rows
- BLOCKED named in all three reports: Plan 1 table rows 5, 8, 15; Plan 2 Q6-003, Q6-010; Plan 3 P3B-17, P3BF-030, table row 15. Each is BLOCKED in the CSV or table. Fair.
- Row 5 replaced by opened P1C2-33: fair (the CNBC page carries the 100.4 and "lowest since Oct 2023"; the "restaurant +3% (398.7)" line is still unseen, which the row notes).
- Dropped as not downside: UE-N07, P1C1-C01, P1C4-10, SD19, UD-N12 (Plan 1); Q6-007 to -009, Q8-001 to -004 (Plan 2); P3BF-035, P3PB-45, P3PB-50 to 57 (Plan 3). Reasons read against the rows: fair, with one inconsistency: **UE-N07 is listed as "dropped as not downside" in Plan 1 but is also used in the table row 9 line** (A-1). Q6-007 to -009 are profit or sales up: fair. P3BF-035 (Fore profit up; "below target" is annual-report wording) fair.
- The Plan 2 report names Q6-003 as BLOCKED "management view on boycott"; the opened CNBC page of 6 Oct 2025 (row P3B-08, reasons_fact) does carry management naming the boycott. See A-3.

### A4. Counts and Appendix
- Plan 1: Summary item 6, section 2.4 and Appendix all say 43 / 20 / 23 and "no verdict changes". Consistent. Appendix says distinct row ids rose from 67 to 87; my trace finds 91 distinct ids (my regex also catches ids in the excluded and dropped lists and in the table). The 87 cannot be reproduced exactly; not material (A-7).
- Plan 2: 23 = 12 + 11, the 11 added ids match the list (Q6-001, -002, -004, -005, -006, -011, -012, UC-N08, P3BF-009, -018, -022). Counts sit in section 5 only, as stated. Consistent.
- Plan 3: Summary bullet, section 2.6 and Appendix all say 35 / 29 / 6. Consistent.
- Log `run4-balance-check.md` matches the reports.

### A5. Tag trace per report (scripted)
Every row id found in each report was looked up in all CSVs: all VERIFIED-OPENED or CORRECTED-OPENED, except the BLOCKED rows that the report names as excluded. Register ids on each line were compared with the register ids of the rows on that line.
- Plan 1: 91 ids, 0 failures. Register mismatches flagged by the script are all explained (UE-N07 line also carries DEM-023 and DEM-012 from the table row; P1C2-11 line carries DEM-018 from table row 16; P3BF-016/032/034 line carries DEM-025 from table row 13).
- Plan 2: 80 ids, 0 failures except Q6-003 and Q6-010 (BLOCKED, named as excluded).
- Plan 3: 16 row ids, 0 failures except P3B-17 and P3BF-030 (BLOCKED, named as excluded). Added register ids correct: P3BF-010 CMP-005, -011 and -012 CMP-004, -007 CMP-002, -005 CMP-001, -024 CMP-011, -025 CMP-009, -040 CMP-003.

### A6. Plan 2 diff against HEAD~3
`git diff HEAD~3 -- reports/2026-10-17-regulatory-entry-pathway.md`: one hunk, 9 lines added at line 164 (one paragraph, one blank line, one table with four operator rows, one blank line), 0 deleted, all inside section 5 before "Surveys". **No change outside section 5.** (Summary, section 4 and Appendix untouched.)

### A7. Do any added rows contradict a stated verdict?
- **Plan 1:** no. H2 (not confirmed, disconfirmed nationally; Jakarta half unmet) is supported by the added national rows; none is a DKI series; the report says so. H8 unaffected.
- **Plan 3:** no verdict changes. H5 "partly confirmed" is reinforced. Not stated: Burger King Indonesia EBITDA IDR -29 bn (A-6).
- **Plan 2: yes, a sentence.** The section 5 line "Operator results. Filings or filing-based press; none states a boycott cause" (existing, line 154) and the section 4 H6 reason "losses at US-linked operators ... not attributed to boycotts" are contradicted by two verified rows that the balance check did not scope in: P3B-08 (foreign-entrants.csv: FAST disclosure at the 2 Oct 2025 expose, CNBC 6 Oct 2025, opened: losses for five years; Covid, boycott 2023-2024 and falling purchasing power cut in-store transactions) and P3B-07 (Starbucks closures "mainly due to falling traffic and the effect of boycott sentiment", investortrust 30 Jun 2025, outlet paraphrasing the CEO, tier 3, single outlet). The H6 verdict ("Undetermined", about a European brand) does not need to change, but the sentence does. See A-3.

### A8. Q6-004 handling in Plan 2
The row says "19 outlets; 400 employees; to Sep 2025", CNBC 3 Oct 2025 opened, "kurang lebih 400", and its notes add "Reasons include lease expiry and relocation, not only boycott" with no speaker or source for that clause. The report states 19 outlets and about 400 employees affected (management at the 2 Oct 2025 expose), gives the period "to Sep 2025", cites it with BEH-047, says the filing figure differs (20 closed, 1,041 fewer employees, different measure, UC-N08), and says the "not only boycott" wording is not relied on. That is correct and cautious: the figure and period match the row, the unsourced clause is not repeated, and the difference to UC-N08 is stated. The only gap is the one in A-3: the row that actually supplies the speaker and the cause list (P3B-08) is not used, and the sentence "none states a boycott cause" stands beside it. Also "about 400 employees affected" softens the headline word PHK (layoff); acceptable.

## Part B (12 items spot-checked: L1, L8, L10, L11, L18, L19, L20, X3, X5, X8, B1, B5/B6)

| Item | Tag trace | Facts vs row | Result |
|---|---|---|---|
| L1 | E-04, E-05 resolve | Art. 26(4), 28(3) match E-04/E-05 notes | OK |
| L8 | E-03 resolves | IDR 2.5bn, Art. 26(10), 27(1), "kecuali ditentukan lain" match; origin = E-03 gap | OK. The "CHF 200k frame" is not in a row (header flags the undated rate). |
| L10 (added) | E-01, E-12 | OCR-only annex finding, Hukumonline for 56101 only, 56303 OCR-only: matches E-01 gaps and run-2 note | Comes from the E-01 gap column. OK |
| L11 | F-04, F-05 | 5 vs 3+2 years, Kontan list, Tempo 403, "22/2016 per F-05, 22 Tahun 2006 as Kontan prints it": match F-05 | OK. The clause "JDIH lists a 2026 impact assessment on revising the franchise regime" is not in F-05; it comes from the Plan 2 report section 6 text (run-3 verification file), so no tag supports it. Low |
| L18 (added) | E-01 | alcohol manufacture closed, retail conditional, on-premises not researched: matches E-01 gaps | Comes from the E-01 gap column. OK |
| L19 (added) | E-11 | tier-3 RPTKA lead, Art. 170(e): match | Partly from the E-11 gap (official norms for RPTKA/SLHS not found). "Wage and labour rules for the outlet" is not in any gap column; it is the worker's addition. Low |
| L20 | S-03 to S-05 | "operator results do not show a boycott cause" | Contradicted by P3B-07/P3B-08 (A-3). Medium |
| X3 | T-15 | 12% statutory / 11% effective, DDTC relay, PMK 11/2025 unopened: match | OK, time-sensitive note correct |
| X5 (added) | T-09 | "not researched" = T-09 gap (PPh 23 on domestic royalty/dividend) | Comes from the T-09 gap column. OK |
| X8 | T-06, T-07 | 20% Aug-Dec 2025 (Kepgub 722/2025), ended 31 Jan 2026, page images; March 2026 by relay (Kepgub 310/2026); none for Sep-Dec 2026: match | OK |
| B1 | H-03, H-02, E-07 | PMA = "usaha besar" (Art. 26(1) per E-07 note), Art. 98(2) defers, "Analysis only, at most medium" = H-03 medium; SEHATI 2025 only (SEHATI25) matches H-03 gaps and audit note | OK. The IDR 12.5m / 300,000 tariff in "Why it matters" is in H-08, which is not tagged on B1. Low |
| B5 / B6 | H-12, H-04, H-11 | Art. 160(3) due 17 Oct 2026, none found 17 Oct, IDR 800,000 fee; 9 Oct statement, "no postponement"; sanctions (warning, withdrawal; BPJPH closure for medium and large): match H-12, H-04, H-11 | OK. Re-check dates 19-20 Oct 2026 appear in H-02 and H-12 and in the list header; H-04 itself carries no date but the header applies it |

Other checks:
- Time-sensitive notes: SEHATI 2025-only correct. H-04 and H-12 re-check on 19-20 Oct 2026 correct. T-07, E-02 (21 Oct), T-15 correct. Header wording: "checked again 2026-10-18" and "nothing was re-checked on 2026-10-18" sit in tension, and today (18 Oct) the micro and small phase has started while H-04 is written in the future tense ("starts 18 Oct 2026"). Low (B-3).
- No legal conclusion is presented as fact: the Evidence lines keep "our reading", "Analysis", "absence in the articles read". The B1 "PMA is large for halal" is labelled Analysis. OK.
- X9 cites "T-14 dropped as pre-window": T-14 is not in the CSV (dropped-rows file only); the tag is explicitly labelled as dropped, so it is honest but does not resolve to a row. Low.
- The five added items come from row gap columns: L10 (E-01), L18 (E-01), L8 (E-03), X5 (T-09), L19 (E-11, partly). Confirmed.

## Findings table

| # | Location | Issue | Severity | Fix |
|---|---|---|---|---|
| A-1 | Plan 1, section 2.4 | UE-N07 is listed as "dropped as not downside" yet is cited in the table row 9 line; counts and exclusion list disagree | Low | Remove UE-N07 from the dropped list or say "used only as the base of row 9" |
| A-2 | Plan 1, section 2.4 table | P1C2-33 omits the opposite figures the row records (MSI +6.5% yoy; middle-class IKK rising for two bands); UE-N08 omits "read from a chart label" | Low | Add one clause each |
| A-3 | Plan 2, section 5 line 154 (and section 4 H6 row; section 5 added table; Part B L20) | "None states a boycott cause" and "not attributed to boycotts" are contradicted by opened rows P3B-08 (FAST management names the 2023-24 boycott as one of three causes, CNBC 6 Oct 2025) and P3B-07 (Starbucks closures linked to traffic and boycott sentiment, outlet paraphrase of the CEO, tier 3). Q6-003 was excluded as BLOCKED although an opened page carries the management statement | Medium | Reword to: no filing states a boycott cause; FAST management names the boycott (2023-24) as one of three causes (P3B-08, CNBC 6 Oct 2025) and Starbucks closures are tied to boycott sentiment by one tier-3 outlet (P3B-07); H6 stays Undetermined. The H6 reason in section 4 is outside the allowed edit area: send to the owner. Same change in L20 of the question list |
| A-4 | Plan 2, section 5 added table | "loss narrowed 56.99%" is a computation presented without a "computed" label (row says about 57%) | Low | Add "(computed)" |
| A-5 | Plan 2, section 5 selection rule | Operator rows P3BF-007, -010, -011, -012, -019, -024, -025 (same three operators) are counted as downside in Plan 3 (26 operator rows) but not in Plan 2 (23 rows total); the two reports use "operator rows" differently | Low | State in the Plan 2 rule that only boycott-relevant fields of FAST, MAPB and PZZA were considered and that the other operator rows sit in the Plan 3 report, or add P3BF-010 and P3BF-007 |
| A-6 | Plan 3, section 3.1 | Cited rows lose downside facts: Burger King Indonesia EBITDA IDR -29 bn (-11.3%), 9M FY26 revenue -5.1%, Sep 2025 unrest (P3B-05); Popeyes listed under "stable" although the row says "loss-making and worsening"; Mixue's counter fact (group revenue +35%, closures described as optimisation) not stated | Low | Add the P3B-05 EBITDA and revenue figures; rename the Popeyes bullet or add "worsening"; add the Mixue counter clause |
| A-7 | Plan 1 Appendix | "87 distinct row ids" not reproducible (91 by script count) | Low | Restate the count or drop it |
| B-1 | Part B, L20 | Repeats "operator results do not show a boycott cause" (see A-3) | Medium | Same wording fix |
| B-2 | Part B, L11, L19, B1, X9 | L11 impact-assessment clause and L19 "wage and labour rules" have no supporting row tag; B1 tariff figures lack the H-08 tag; X9 tag T-14 points to a dropped row | Low | Add tags (H-08 on B1), mark the L11 clause as "from the Plan 2 report, no row", say "worker addition" for L19 labour rules |
| B-3 | Part B, header | "checked again 2026-10-18" vs "nothing was re-checked on 2026-10-18"; H-04 phrased as future on 18 Oct | Low | Reword both lines |

## Summary
Parts A and B are accurate at the level of values, periods, geography, counts, tag trace and the Plan 2 diff (only section 5 changed). Required before final acceptance: fix A-3 and B-1 (one sentence in Plan 2 section 5 and L20; the section 4 H6 reason needs the owner's decision because the edit area for Plan 2 was limited to section 5). The remaining findings are low.
