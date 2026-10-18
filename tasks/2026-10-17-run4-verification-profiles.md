# Run 4 verification: customer target profiles (V-PROF, 2026-10-17)

Report verified: `reports/2026-10-17-customer-target-profiles.md` (W-PROF draft). Verifier: independent (did not write the report). The report was not edited. No git commit.

## Verdict: ACCEPT WITH FIXES

The report is sound on tracing and numbers: 0 WRONG figures among the 159 cited rows, 17 sources re-opened, arithmetic re-adds, the BLOCKED list is exact, and the tag discipline and persona labelling are good. It does not yet meet the lessons rule "risk sections cite ALL verified disconfirming rows in scope" (F1), and one headline price comparison is understated (F2). Both need fixing before acceptance. The other findings are small.

## Findings

Severity: High = must fix before acceptance; Medium = should fix; Low = polish.

| # | Location | Issue | Sev | Fix |
|---|---|---|---|---|
| F1 | Section 6 (also Summary "Facts pointing the other way") | Verified disconfirming or downside rows in scope are missing (full list below the table). The two most relevant: P1C2-09 (middle-class food consumption growth slowed to 0.9% from 4.6% in 2025, non-food 6.4%) and P1C2-29 (Mandiri card data: restaurant spending +4.7% in Q3 2026 against +6.1% in 2025; September total 5.5% is the lowest since Nov 2025). Also DISC-A9, P1C2-30 and UE-N08, plus the chain-pressure rows. | High | Add the rows with tags to section 6 (the "mixed" ones marked as such), or state in one line why a row is out of scope. |
| F2 | Summary "Price is the hard test"; section 3 Analysis; 4.1 Price tolerance | "Placeholder guest spend about IDR 100,000 net, about 1.5 times the Millennial delivery lunch (65,130)". The 100,000 is the model's blended spend across dayparts (07-revenue.csv: 103,375, which includes morning coffee at 65,000). The lunch comparator is the model's lunch ticket (03-inputs.csv `tkt_lunch`: 110,000 / 120,000 / 135,000 net; pasta + drink). Like for like the ratio is about 1.8 (net 120,000 / 65,130) and about 2.0 with tax. 100,000 x 1.1 is also 110,000 while the model's 103,375 x 1.1 is about 113,700. | Medium | Use the lunch ticket against the lunch order, keep the blended figure only as a blended figure, and fix the "1.5 to 1.7" statement and the 1.9% / 7.5% of wage lines to match. |
| F3 | Summary "Money"; section 2 A; 4.1 | "Average Jakarta employee earns 5.9 million, only about 3% above the provincial minimum wage 5,729,876" compares an August 2025 average with the UMP of 1 Jan 2026. Against the UMP in force in August 2025 (P1C2-22: 5,396,761) the margin is about 9%. The UMP is a floor for workers under one year of service (row base). P1C2-23 notes also say the series is volatile (Feb 2025: 4.88 million) and that Jakarta pays 1.8 times the national average (favourable, omitted). | Medium | Compare like years (5.9 vs 5.40 million, or label the 3% as "against the 2026 floor") and add the national comparison for balance. |
| F4 | Summary table, row "Dropped or deferred"; section 5 | Families and groups (segment F, Tiago score 16) are listed as dropped but section 5 gives no reason and no row. Scope "Areas to Analyse" (blueprint 2026-08-13) also lists nightlife and afterhours consumers, premium mall and street culture, and food delivery behaviour; nightlife is not mentioned anywhere. | Medium | Add a two-line entry for families (the brief's own "test later", no verified row) and one line saying nightlife has no verified row. |
| F5 | Tags: P4W10-02, P3BF-033; consistency of P1C1 / UE-N01 labels | National and urban rows labelled "evidenced": P4W10-02 (N-D) twice; P3BF-033 (U-D, but described as Jabodetabek). User rule: national or urban-Java data must be "proxy". Same row types are labelled differently: UE-N01 "evidenced" in the Summary and 4.2 Money but "proxy" in the 4.2 location line; P1C1-S02..P04 "evidenced" elsewhere but "proxy" in the 4.1 location line; Jakarta kota spend rows P1C1-E01/E02 "proxy" while UE-N01 (same kind) is "evidenced". | Medium | Relabel the two rows "proxy" (or recode P3BF-033 to J*); apply one rule to Jakarta all-ages spend rows. |
| F6 | Section 4.3 (also 4.4 and the 4.2 mall line) | Unit of the 397 padel count is unresolved in the CSV notes (P4W10-01 and UC-N07: "lapangan" courts vs "bangunan" buildings; "never mix 326 courts / 397 / 95 venues / 34 clubs"). The report writes "185 of 397 Jakarta padel sites" in the same section as 326 courts and 95 venues and flags only the 95 as a different unit. | Low | Write "397 (unit unresolved: courts or buildings)" and keep it out of any comparison with 326. |
| F7 | Section 6 row "North Jakarta ... above South Jakarta"; section 4.2 location line | The prepared-food figures are right (E04 556,691; E02 548,413; E03 513,174, 2024 round). But the same rows show South Jakarta growing +25% against North +9.4% (E02/E04 snippets), and Tiago's brief table gives total spend South 4.08 vs North 3.83 million (2025), both in South's favour. The text gives only the side that cuts against South. Two different measures are not distinguished. | Low | Name the measure (prepared food 2024) and add the growth and total-spend counterpoints, which belong in the same cell. |
| F8 | Section 6 row "Middle-class savings index 100.4 in February 2026" | A newer verified row exists (P1C2-30, 27 Sep 2026: middle group 100.5 "relatively stable"; upper 95.1 against 94.0 a year earlier). The February reading is presented as the current state. | Low | Cite P1C2-30 beside P1C2-33 and say the index is flat since February. |
| F9 | 4.2 Who | "bank accounts above IDR 2 billion grew 15.99%" - the row (P1C2-27) is the value of deposits held in such accounts (BRI/LPS), not the number of accounts. | Low | Reword to "deposits held in accounts above IDR 2 billion". |
| F10 | Section 3 table, functional drink row | Range ends are not traced: smoothie "45,000-47,000" (47,000 = P3PR-018 not tagged), herbal elixir "27,000-35,000" (27,000 = P3PR-020, -021 not tagged). | Low | Add the row ids. |
| F11 | Row geography coding: P1C3-02, UE-N06, P4W10-08 | Report tags them J* (Jabodetabek); the CSV rows carry geography "J". The report is right (notes say Jabodetabek malls, Greater Jakarta venues), but the recode is not stated and the CSV is not corrected, so a mechanical trace shows a mismatch. P1C1-S07: age code n/a in the row, D in the tag (trivial). | Low | Correct the three CSV cells, or say in section 1 that J* is re-coded from the notes. |
| F12 | 4.1 Occasions; 4.1 and 4.2 "Discovery" | The Jakpat September 2025 sample is called "eight Java cities, no Jakarta". The row names Bogor and Depok, which are Jabodetabek satellites. "No Jakarta" is correct; "no Greater Jakarta" would not be. | Low | Add "(includes Bogor and Depok)". |
| F13 | Section 3 Analysis | "Placeholder latte (50,000) is above every listed latte (maximum 38,000)". True for the verified rows, but the model's own benchmark cells (unverified S31/S46) list lattes of 45,000-61,000 in the same zone. The report excludes them, but the sentence reads as a market fact. | Low | Add "among the verified rows". |
| F14 | Concept fit bullets (4.1-4.4); 4.3 Price tolerance | Judgements not prefixed "Analysis:" (for example 4.2 "Fits: Italian heritage and premium coffee as an occasion product"; 4.3 "an after-session drink and snack fits better than a pasta main"). The persona and the "Analysis:" lines are labelled correctly. | Low | Prefix with "Analysis:". |
| F15 | Appendix A, B | Appendix A cells are cut mid-word (for example "not stated in abstrac", "per-generation n :", "Gen Z is 42% of the sample: P4W1-R11"). Appendix B omits brief claims that have no verified row: 31,000 marathon runners (JIM 2025), 48.9% Gen Z or Millennials of 10.72 million, 17% prepared food share. | Low | Regenerate A without truncation; extend B. |

### F1 detail: verified disconfirming or downside rows in scope that the report does not cite

From `data/raw/2026-10-17-disconfirming-evidence.md` table A (all verified rows; DISC-A1, A2, A3, A6, A13, A16 are cited, BLOCKED rows 5, 8, 15 are correctly named):
- DISC-A9 (VERIFIED-OPENED relay, mixed): 23,470 workers laid off, Jan-May 2026 (Kemnaker, JKP participants only; about 49% below Jan-May 2025's 46,015 = UE-N07). Relevant to 4.1 (office workers). Should appear as mixed.
- DISC-A17 (mixed): GDP growth 5.29% in Q2 2026. Context only; may be listed as a supporting counterpoint.

From `data/processed/plan4-*.csv` and `demand/*.csv` (verified rows, not cited, pointing against or tempering the profiles):
- P1C2-09: middle-class consumption growth, food 0.9% against 4.6%, non-food 6.4% (2025). Touches 4.1, 4.4.
- P1C2-29: Mandiri card spend, restaurants +4.7% Q3 2026 against +6.1% in 2025 (still the fastest category); total September 5.5%, lowest since Nov 2025. Touches 4.1, 4.2, 4.4.
- P1C2-30: Mandiri Saving Index 27 Sep 2026, middle 100.5 stable (updates P1C2-33).
- UE-N08: households calling themselves poor 26.9% (Aug 2025) against 19.5% (2024). Touches 4.1.
- Q6-004, UC-N08, Q6-002: KFC operator FAST closed 19-20 outlets and cut about 400 staff (1,041 fewer employees) to Sep 2025; revenue -0.76% (net loss narrowed, Q6-001). Touches 4.2 (foreign comparables). P3BF-018: Starbucks Indonesia closed 11 outlets and slowed expansion. P3B-05: Burger King Indonesia stores 138 against 147. Q6-012: Starbucks Malaysia revenue -36.5% (proxy comparator). UC-N11: Starbucks management says recovery from boycott still ongoing.
- SD07: SEA delivery average order value trending down slightly (price tolerance, 4.1).
- P4W9-17: 53% of Millennials prefer home-cooked lunches over snacks (frugal strategy); P4W9-26: dining out in the top three spend categories for only 14% of Gen Z; UB-11: 34% price-sensitive; P4W3-07: 51% of pulse chasers regret impulse purchases. Low weight, optional.
- Balance in the other direction: P4W4-01 (48% would pay more than 10% extra for enhanced-nutrition food) tempers the report's "health premium capped at 19%" and is not mentioned.

## Claims checked and results

### (1) Mechanical trace
- 164 bracketed tags parsed (script run on the body, before Appendix A). 159 distinct CSV row ids plus 6 DISC-table-A rows: matches the report's "159 distinct CSV rows (plus 6)" and the Appendix A count of 165.
- Row exists: 159 of 159 (searched `data/processed/**/*.csv`, only files with the survey schema).
- Verification VERIFIED-OPENED or CORRECTED-OPENED: 159 of 159. DISC rows used: A1, A2, A3, A6 (VERIFIED), A13, A16 (CORRECTED-OPENED). No BLOCKED row is used. Section 7 lists 19 BLOCKED ids; they equal the 19 rows of `2026-10-pillar1-mapping-excluded.csv` exactly. DISC rows 5, 8, 15 are named as BLOCKED.
- Geography and age-fit match the row for all tags except: P1C3-02, UE-N06, P4W10-08 (row J, tag J*, justified by notes; F11), P1C1-S07 (age n/a vs D, trivial). Rows with descriptive geography text (for example "South Jakarta (kota)") match the tag letter J.
- Every cited id appears in Appendix A (0 missing). The 21 ids that appear in the body without a tag are BLOCKED ids, label-fix ids in section 1 (P1C2-07, P3PB-06, UA-N67) or Appendix C: no untraced figure found.
- The six label fixes of `tasks/2026-10-17-run4-label-fixes.md` that the report says it applied (P1C2-03, P4W9-29, P4W4-06, P3PB-27, P3PB-06, UA-N67) are reflected in the text: upper class "Mandiri Institute classification", takeout not delivery, NIQ online adults, Bastian "European modern menu", UA-N67 not used for a figure.

### (2) Content check
All 159 cited rows were read in full against the report text (value, unit, year, base, geography; snippet plus `notes`, `proxy_note`, base and in-force columns). No value, unit, year or base mismatch found. Items worth noting were put in the findings (F2, F3, F6, F9, F10). Headline numbers re-computed:
- 535,920 (179,370+178,390+178,160) and 244,600 (81,880+81,020+81,700) and 780,520: correct. 535,920 / 2,360,000 = 22.7%: correct.
- 4.08 / 2.96 = 1.378 (38%): correct. 110,000 / 548,413 = 20.1%: correct. 110,000 / 5.9 million = 1.9%, 440,000 / 5.9 million = 7.5%: correct. 326 / 947 = 34.4%: correct. 100,000 / 65,130 = 1.54 and 110,000 / 65,130 = 1.69: correct as arithmetic (comparator issue in F2). 5.9 / 5.729876 = 1.03: correct as arithmetic (period issue in F3).
- Jakarta CCI 146.8 against 150.0 = 3.2 points: correct.

Sources re-opened (curl -sL, browser user agent, all HTTP 200, no bot-check bypass) and the cited values found on the page: 17 of 18 attempted.
1. Databoks South Jakarta age bands (DEM-029): 179,370 / 178,390 / 178,160. OK.
2. Databoks Central Jakarta prepared food (DEM-030): 513,174, year 2024. OK.
3. Databoks South Jakarta spend (UE-N01): Rp4,08 juta (4,083,229), 2025, +15.57%. OK.
4. GoodStats Jakarta wage (DEM-042): 5.9 million Aug 2025; 5.81 million Aug 2024; Feb 2025 4.88 million. OK.
5. Kompas TV UMP 2026 (DEM-040): 5,729,876, +6.17%. OK.
6. Kontan middle class (DEM-035): 47.9 to 46.7 million, 16.6%. OK.
7. GoodStats delivery lunch (BEH-083): Gen Z 58,609, Gen X 63,250, Millennials 65,130. OK.
8. Databoks padel courts (BEH-091): 326 courts DKI Jakarta. OK.
9. Kontan Liga.Tennis (BEH-095): 400,000 per session plus 50,000 consumption; padel 58.30% aged 21-40. OK (the 57.3% male / 31-40 figure sits on a different source, BEH-096, not opened).
10. detikFood Italian restaurants (CMP-057): Gior 100,000-250,000; Bastian 155,000-380,000. OK.
11. GoodStats Gini (DEM-045): Jakarta 0.435, national 0.368. OK.
12. GoodStats discovery channels (BEH-004): 44% / 40% / 39%. OK.
13. GoodStats restaurants (DEM-062): DKI Jakarta fourth, 202,983. OK.
14. GoodStats cafe survey (BEH-066): 49.1%; 83 / 78 / 70 / 64 / 45 / 27. OK.
15. Investortrust BRI (DEM-044): 8.0% against 3.5% (middle) and 3.6% (lower); deposits above Rp2 billion +15.99% (value of deposits; F9). OK.
16. Bank Indonesia September 2026 consumer survey PDF (DEM-034): 123.5 for the above-Rp5 million group, 127.9 for ages 20-30, 116.1 / 109.2 (index 10). OK.
17. Fore Coffee Annual Report 2025 (CMP-014): "Jabodetabek 149 Fore Coffee, 2 Fore Donut"; 316 stores nationwide. OK.
- Not independently confirmed: Burgreens menu PDF (CMP-052) is an image-only PDF (no text layer); only the metadata creation date (19 Aug 2025) was confirmed. The prices rest on the earlier run-3 verification.

### (3) Status labels
National (N), urban-Java (U) and proxy-country (P) rows are "proxy" everywhere except P4W10-02 and P3BF-033 (F5). Age mismatch (C, D) rows are "proxy" or "evidenced" according to geography, consistent with the stated definition, except the inconsistent treatment of identical row types (F5). Hypothesis labels (no-row brief claims, assumed age bands, P4W10-09 single operator quote) are correct and conservative.

### (4) Fact versus analysis
"Analysis:" and "(arithmetic)" markers are used as the how-to-read section says. Four personas (Dewi, Arief, Raka, Nadia) are each labelled "ILLUSTRATIVE persona (not evidence, invented)". Model prices are labelled placeholders, not evidence. Minor: unlabelled judgements in concept-fit bullets (F14).

### (5) Disconfirming rows
Cited correctly (with the numbers checked): DISC-A1, A2, A3, A6, A13, A16, P1C2-01/05/06, P1C2-10/11/12, P1C2-32/33/34, P1C2-20, P4W9-16/19/28/29, P4W4-02/05/06, P4W7b-14/15, Q6-005/006, P3BF-022, UC-N07, P4W5-08, P4W2b-11/14/21. Missing rows: see F1 detail.

### (6) Tiago's brief
- Score totals re-add from the extended-data scoring sheet: A 4+3+4+4+5+3 = 23; B 3+5+3+4+4+2 = 21; C 2+4+4+5+4+2 = 21; D 4+1+3+3+3+3 = 17; E 1+5+3+4+3+2 = 18; F 4+3+2+2+3+2 = 16. All six match the printed totals. The report's table shows columns A-E only (F not shown or discussed; F4).
- 57.3 to 46.7 million: the brief's series is 57.3 (2019), 53.8, 49.5, 47.9 (2024), 46.7 (2025), "BPS definition via Kontan", change -10.6 million. The report's explanation holds: P1C2-05 (BPS 57.33 million in 2019), P1C2-06 (BPS 47.85 million in 2024, 17.13%) and P1C2-01 (Mandiri 47.9 to 46.7, 16.6%) agree at 2024 (47.85 vs 47.9). The join is two publishers' series on the same BPS Susenas base, matching at the join point. 57.3 - 46.7 = 10.6: correct. The class definitions behind the two series are not printed side by side in the rows, so "like for like" is shown by agreement at 2024 only; the report says exactly that.
- North vs South: brief table (spend per person per month, 2025): South 4.08, North 3.83 (incl. PIK), West 3.08, East 2.71, Central 2.59, Jakarta 2.96 million. Rows UE-N01 (rank 1 of 6 DKI cities) and P1C3-05 confirm 4.08 and 2.96. The report's North vs South claim concerns prepared food in 2024 (556,691 vs 548,413), correct against the rows but a different measure; counterpoints in F7. "Highest in Indonesia" in the brief: the report is right that no row supports a national kota ranking (the rows give rank 1 of 6 DKI cities; Jakarta rank 1 of 37 provinces).
- Bowl price: the brief's "core bowl IDR 85,000 to 110,000" (before tax and service) is quoted correctly; the model prices pasta (82,000-135,000 net; core 89,000-105,000), so the mismatch the report calls out is real. The brief's own text says "pasta bowls" and "healthy bowls cost 1.3 to 2x a delivery lunch", which is worth quoting. The comparison with the model's per-guest figure is understated (F2).

### (7) Acceptance criteria
- Scope groups (blueprint: young professionals, upper-middle class, students, fitness and running communities, creators and lifestyle audiences, expats): all six covered (profiles 4.1-4.4, section 5). Nightlife/afterhours and families not covered (F4).
- 3-4 ranked profiles: 4 ranked (2 primary, 2 secondary). Pass.
- Dropped groups justified: students, creators, expats yes; families no (F4).
- Districts line per profile: present in 4.1, 4.2, 4.3 and 4.4 ("Location fit (one line for Jonas)"). Pass.
- 3-5 assumptions: 5, each with evidence and test. Pass.
- Appendix: A (register id, period, base), B (brief claims with no row), C (segment_use labels). Present; polish in F15.
- Structure why-we-looked / data / what it means / how to continue: present in every section. Investor summary on top: present. BLOCKED rows named: yes.

## Required before acceptance
F1 (High), then F2, F3, F4, F5 (Medium). After the fixes, a short re-check of section 6 against the F1 list is enough. Lessons rule to add if F1 stands: build the risk table from the disconfirming file plus a search of the plan4/demand CSVs for rows whose direction is negative, not from rows already used elsewhere in the report.
