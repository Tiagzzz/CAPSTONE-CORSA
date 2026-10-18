# Run 3 report verification V-P3 (figures, hypotheses, placeholders, bias guards, acceptance): Plan 3 report

Date: 2026-10-17. Verifier: V-P3 (independent; did not write the report). Object checked: `reports/2026-10-17-competitor-map-and-price-ladder.md` (3,805 words). Against: CLAUDE.md §5 and §7, `tasks/2026-10-16-plan-3-competitors-price-ladder.md` (§2 hypotheses, §3 saturation test, §6 window rule, §9 acceptance), `tasks/lessons.md`, `data/processed/README.md`, gap analysis §6, and `data/raw/2026-10-13-corsa-jakarta-financial-model-v0-5-csv/06-menu.csv`. The report was not edited. Nothing was committed.

## Verdict: ACCEPT WITH FIXES

No blocker and no fabricated figure. Every number in the Summary and the verdicts traces to a VERIFIED-OPENED or CORRECTED-OPENED row and, where I opened the source, matches it. There are two majors. Both are about interpretation and framing, not arithmetic: (M1) the latte "largest outlier / clear premium bet" claim rests only on mass-chain prices and leaves out disconfirming evidence that sits in the report's own input files; (M2) the Texas Chicken case is described as undated and counted as "zero or one" in-window, although the repo already holds its 2023 exit date. Both fixes are wording changes, with no new research. Several plan §9 deliverables are not met, but the report states each as a gap rather than filling it (see the checklist).

## 1. Method

- **Row trace.** All 42 register IDs cited in the report exist in `sources/sources.md` with tier and access date (script check). All 41 listed-operator rows, 16 in-window foreign-entrant rows (plus the 4 historical and 3 excluded rows) and 89 price-ladder rows carry VERIFIED-OPENED or CORRECTED-OPENED, except the two BLOCKED rows (P3BF-030, P3B-17), which the report correctly excludes.
- **Summary and verdict figures: 100% traced.** Every derived value in §1, §2, §3.1 counts and §4 was recomputed from the CSV values (percentages, differences, shares, medians, brand counts, approximate counts). All reproduce.
- **Other numbers: well above the 50% sample.** All §2.1 to §2.5 values and all §4 statistics were recomputed. Only the places listed in the findings table failed.
- **Sources opened by me** (curl -sL with a Chrome user agent, saved to `/tmp/claude-0/-home-user-CAPSTONE-CORSA/c8401b57-6bf2-5305-9a01-f1d1e4e31e77/scratchpad/vp3/`, parsed with `python3 -I` and `pdftotext`; no bot check bypassed; 20 opened):

| Source (register id) | What I checked | Result |
| --- | --- | --- |
| FAST H1 2026 FS (CMP-001) | 682 outlets (Dec 2025: 690); revenue 2,789,865,271 vs 2,403,271,439; loss (61,146,624) vs (142,312,383); Jakarta RSC 979,989,184; going-concern text | match |
| MAPB H1 2026 FS (CMP-006) | sales 1,670,827 vs 1,520,542; loss (121,506) vs (80,206); 934,485 / 638,841 / 97,501 | match |
| MAPB FY2025 FS (CMP-007) | sales 3,236,043 vs 3,228,133; loss (150,767) vs (146,148) | match |
| Fore H1 2026 FS (CMP-013) | net sales 1,004,934,782,303 vs 662,372,756,900; income 56,488,819,450 vs 42,031,093,163; 363 + 10 + 4 outlets | match |
| Fore FY2025 FS (CMP-015) | net sales 1,497,134,772,364 vs 1,038,659,233,501; income 90,133,042,112 vs 58,219,108,464; 316 + 2 + 4 | match |
| Fore Annual Report 2025 (CMP-014) | 322 outlets total; "149 Fore Coffee" under Jabodetabek | match |
| EmitenNews PZZA (CMP-010) | revenue Rp1.47 trn, -4.54%; profit Rp8.27 bn vs Rp15.56 bn in body, Rp8.4 bn in lead | match; conflict is real and disclosed |
| StockWatch (CMP-005) | loss Rp369.24 bn; accumulated losses Rp507.63 bn; Rp1.33 trn | match; 366.04 is not on this page (finding F5) |
| Detik (CMP-003) | 715 to 690 FAST; 591 to 575 PZZA; Texas Chicken "usai menutup seluruh gerai", loss Rp955.25 juta, sales Rp1.8 bn | match |
| RBA Q3 FY26 deck (CMP-028) | BK 147 to 138; Popeyes 25; Popeyes store EBITDA -20.3%; company EBITDA -29, -11.3% | match |
| Investortrust (CMP-030) | "membuka 11 gerai ... menutup 16 gerai" in H1 2025, boycott cited by the outlet | match |
| CNBC Domino's (CMP-040) | 312 closures worldwide, 233 Japan; Indonesia appears only in the site name | match; supports the report's "never names Indonesia" |
| Industry.co.id (CMP-037) | "Restoran ke-23 Pizza Marzano di Indonesia"; presence since 2006 | match |
| Detik 5 kafe (CMP-036) | Fuglen from Rp60,000++; Harlan + Holden Rp63,000++; Hario from Rp80,000++; Kitsune range Rp50,000++ | match |
| Detik 5 pasta murah (CMP-058) | Halo Rp25,000-an; Sky Rp20,000-an; Casa Rp20,000; Fish Streat Rp29,000-an | match |
| Pepper Lunch (CMP-056) | Rp74 / 79 / 81 ribuan | match |
| Liputan6 (CMP-059) | "Google Maps" regular Rp10 ribu (Tuku), Rp18 ribu | match; approximation flag justified |
| IDN Times Marzano (CMP-054) | pasta 99,000 / 69,000 / 92,000 / 95,000 / 105,000 / 109,000; espresso 30,000, americano 35,000, cappuccino 38,000, latte 38,000; salads 60,000 / 105,000 | match |
| IDN Times Fore signature (CMP-060) | 24,000 / 31,000 / 33,000 / 29,000 x4 | match |
| Burgreens menu PDF (CMP-052) | pages 6 (68) and 12 (60); footer "Prices exclude Government Tax & Service Charge" | match |
| Detik 10 restoran (CMP-049) | Hard Rock 1992 to 2023; Fish & Co. closed 31 Dec 2022; Marché Mövenpick 2009 to 2020 | match |

- **Not opened by me** (traced to rows only): CMP-002, 008, 009, 012 (ENAK), 017, 019 to 026, 031 to 035, 038, 043, 045, 048 to 050, 053, 055, 057, 061 to 065, BEH-048, BEH-052. I did not open IDX. The ENAK and PZZA values rest on a broker mirror and a relay respectively, as the report says.

## 2. Findings table

Severity: Major = must fix before the report is relied on; Medium = fix in the same pass; Minor = wording or housekeeping.

| # | Location | Issue | Severity | Fix |
| --- | --- | --- | --- | --- |
| F1 | §7 point 2; §4 "Comparison with Team B placeholders"; H1 and H2 rows in §5 | **One-sided evidence for "the largest outlier ... a clear premium bet".** The 7 lattes are 6 Fore signature lattes (one chain, IDN Times, no tax basis) and one plain Cafe Latte from a pizza restaurant (Pizza Marzano, 38,000). The comparison is therefore with the mass-chain tier only. Disconfirming evidence in the report's own inputs is not shown: (a) foreign-entrants rows P3B-11 to P3B-15 (Detik 1 Feb 2026, verified by me) give Jakarta specialty-café drink prices from Rp40,000++ to Rp80,000++ (Fuglen 60k, Harlan + Holden 63k, Hario 80k, Kitsune about 50k); (b) the 06-menu.csv benchmark cells, which the report mentions but does not quote, place specialty latte at 38 to 48k, Common Grounds latte at 45 to 52k and mall latte at 55 to 60k. Under these, 50k sits inside the specialty tier. The plan's H2 disconfirmer is "independents above IDR 45k". Plan Q3 asks for placement in the three tiers, which the report does not attempt. Gap-analysis guard B2 requires the opposing finding to be shown. | **Major** | Reword §7.2 to "above the mass-chain latte prices in the ladder (median 29,000, one chain-dominated sample); within the 38 to 60k specialty and mall ranges that Team B's own benchmark cells cite (not verified here) and the Feb 2026 Detik specialty-café list (drinks from 40 to 80k++, tier 3, 'from' prices, not lattes)". Add the P3B-11 to P3B-15 prices as a counter-point to the H2 row. State that only 1 of 7 lattes is a plain latte. Add one sentence that tier placement (plan Q3) was not possible. |
| F2 | §3.1 "Documented full exit in window: none"; §3.2 "zero or one"; §8.1 "Entrant exit dates and reasons (Texas Chicken)"; §3.3 | **Texas Chicken is treated as undated, but the date is in the repo.** CMP-048 (Okezone, 19 Aug 2023) and dropped row P3B-25 (DATE-FAIL) show all restaurants closed by 14 Aug 2023; `data/raw/2026-10-17-foreign-entrants.md` lists it as HISTORICAL-NOT-IN-BASE-RATE (Texas Chicken, with Carl's Jr., in a list of 6). The 2026 Detik article is only a FY2025 results note about a company that had already closed. So the count in window is zero, not "zero or one"; the §8.1 gap is already filled; and §3.3 lists 4 historical cases where the dropped-rows file holds 6. The raw note also records that this was the one exit with a weak local partner (CSMI), which is relevant to H6 as a labelled historical point. | Medium | Move Texas Chicken to §3.3 (exit 2023, CMP-048, historical, not in any rate; add Carl's Jr. or say "6 historical rows held in the raw note"); change "zero or one" to "zero"; delete the Texas Chicken line from §8.1; optionally add one sentence in the H6 row that the only partner-weakness exit on file is historical and excluded. |
| F3 | §4 Team B comparison, bowl sentence; §7 point 4 | **Bowl comparison is not like-for-like.** The one bowl-type placeholder is "Yogurt / oat bowl", 65,000, in the Breakfast & snacks block of 06-menu.csv. The ladder "bowl" class pools Burgreens smoothie, salad and rice bowls with three Pizza Marzano salads (60 to 105k). The nearest analogue (Burgreens smoothie bowls, 68,000 net of tax and service) is not named, and the 5,000 gap to the 60,000 median compares unlike items. The report does say the ladder is Burgreens-led and gives no verdict, so this is framing, not a wrong figure. | Medium | State that the placeholder is a breakfast yogurt or oat bowl and that no yogurt or oat bowl is in the ladder; drop or footnote the "5,000 above the median" comparison. |
| F4 | §4 Team B comparison, "does not contain a bowl at 85-110k ... appears to refer to a different range" | The claim is **correct** (checked: 06-menu.csv has no bowl at 85 to 110k). The "different range" can be named: the CSV benchmark table has "Common Grounds, Tobiko truffle pasta, 97,500, Dine-in (85-110k)". The plan's "bowl 85-110k" looks like a transposed pasta range. The raw note `data/raw/2026-10-17-price-points.md` §7 still says "Team B's bowl placeholder (85 to 110k) sits above every bowl price in this sample" and was not corrected. | Minor | Name the Common Grounds row as the likely origin. Add a correction note to price-points.md §7 (or mark it superseded). |
| F5 | §2.1 FY2025 loss row ("Total Rp369.24 bn (Rp366.04 bn attributable)", CMP-005) | The row cites CMP-005 for both figures. StockWatch (opened) carries 369.24 only. 366.04 comes from Detik (P4-W6-S1, row UC-N09 in plan4-origin-boycott.csv), which is also outside the P3BF input rows the report says it uses. The values are consistent (raw note: 366.04 attributable, 369.24 consolidated), so only the citation is wrong. | Minor | Cite "CMP-005 (369.24); UC-N09 / P4-W6-S1 (366.04 attributable)" or drop the attributable figure. Say that the row is outside the stated input rule. |
| F6 | §2.1 Analysis: "outlets fell at every reported date (715, 698, 695, 690, 686, 682; CMP-003, CMP-002, CMP-001)" | 698 (30 Jun 2025) and 695 (30 Sep 2025) are in none of the three cited sources. 698 appears only in the notes of P3BF-003 with no source named; 695 is from a CNBC piece (UC-N08, Plan 4). I could not trace 698. The decline claim still holds on the four traceable dates (715, 690, 686, 682). | Medium | Remove 698 and 695 from the list, or cite the source of each and label 698 "not traced". |
| F7 | §2.2 closures vs §3.1 Starbucks | Two Starbucks closure counts are given without a note that they differ: "11 outlets closed" (CNBC, 5 Nov 2025, period unstated) in §2.2 and "11 opened and 16 closed in H1 2025" (Investortrust, 30 Jun 2025, opened by me) in §3.1. They may cover different periods, but the lessons (rule e) call for storing the conflict. | Minor | Add one sentence: "closure counts differ across two single tier-3 outlets (11 vs 16); not reconciled". |
| F8 | §1 Summary "four are shrinking"; §7.5 "Mass-tier chains shrink (KFC, Burger King, Starbucks)" | The Summary count does not carry the caveat that two of the four (Starbucks, Mixue) rest on one relay each; §3.1 does. For Starbucks, MAPB revenue grew +9.9% in H1 2026 and no outlet total is printed, so "shrink" rests on one H1 2025 count. §7.5 drops the caveat. | Minor | Add "(two of the four rest on a single tier-3 relay)" to the Summary and "Starbucks: H1 2025 count only" to §7.5. |
| F9 | §5 H5 | The verdict PARTLY CONFIRMED is defensible and uses several operators. But the population is quick-service and coffee chains plus one casual-dining group (ENAK, single broker mirror, nine months to Sep 2025), while the hypothesis says "mid-market casual dining". The Fore counter-case is a coffee chain. The report says "mass and mid chains", which is accurate, but the verdict label does not say it. | Minor | Rename the row "H5 (applied to the listed chains, mostly QSR and coffee; one casual-dining group)". |
| F10 | §2.5 Analysis: "net profit growth in H1 2026 (+34.4%) is below its 70% target" | Compares a half-year YoY growth with a full-year target. Labelled Analysis and the target is flagged as management guidance, but the periods differ. | Minor | Add "half-year vs full-year target, not like-for-like". |
| F11 | §3.3 / §3 window rule | Detik 27 Jun 2026 (CMP-049) reports the Hard Rock, Fish & Co. and Mövenpick closures within the window, but the exits are 2020 to 2023. The report applies the owner rule by exit date, which is the right reading of "exits older than 2 years are historical only". Plan §6 words it as "exit or its reporting"; the report does not mention that difference. | Minor | Add one clause: "classified by exit date, not by the date of the article". |
| F12 | `sources/sources.md` CMP-040 (not the report) | Use column says "Domino's Indonesia closures and loss (franchisee)". The opened article is about the Australian-listed group and never names Indonesia (the report is right on this). The register description would mislead a later reader. | Minor | Correct the use text in sources.md. |

## 3. Hypothesis check against the plan's own criteria

| H | Report verdict | Plan criterion applied | My assessment |
| --- | --- | --- | --- |
| H1 | INCONCLUSIVE | Core bowl and latte above P60 (confirm), below P40 (disconfirm), above P90 (out of line) in Tier-1 districts | **Agree.** No Tier-1 cell reaches n>=4 (checked: only P3PB-26/28/33/50 carry a Tier-1-adjacent place; all are ranges or street pasta). The direction note on the latte is hedged ("if replicated"), but see F1 for the missing counter-evidence. |
| H2 | INCONCLUSIVE | 3+ chain outlets within 500 m and latte median <= 35k (confirm); under 2 chain outlets and independents above 45k (disconfirm) | **Agree on the label.** Price leg consistent (29k, 2 brands), density leg untested. The report does not mention that its own foreign-café rows show independents priced above 45k, which is the plan's disconfirmer (F1). |
| H3 | GAP | Density ratio 3x | **Agree.** No venue counts exist. |
| H4 | GAP | Fewer than 10 community venues | **Agree.** |
| H5 | PARTLY CONFIRMED | FAST net loss, closures, PZZA/ENAK weak margins (confirm); operators growing outlets and margin (disconfirm) | **Agree, with F9.** Confirm legs are met by FAST (original, loss and going-concern note, outlets 715 to 682), MAPB (original, loss widened) and, more weakly, ENAK (mirror) and PZZA (relay). Disconfirm leg is met by Fore (original filings), and PZZA outlets rose by 4 in H1 2026. Not resting on one source. |
| H6 | INCONCLUSIVE | Exits concentrate among solo/JV-weak entrants with stated reasons | **Agree.** No in-window exit; the report refuses a rate. See F2 for the historical Texas Chicken point. |
| H7 | GAP | OAK1 filings: negative cash flow, net loss | **Agree.** No Oakberry rows in the input; no `oakberry-reconciled.md` exists in the repo. |
| Saturation test | GAP | District x category counts with blind recall check | **Agree.** The report is honest that no counts exist. |

No verdict rests on a small difference: the report explicitly sets aside the 5,000 bowl gap and the single-brand latte comparison.

## 4. Team B placeholder check (06-menu.csv)

- Pasta placeholders: six items, net of 10% PBJT: Arrabbiata (vegan) 82,000; Cacio e pepe 89,000; Pesto genovese 95,000; Carbonara 98,000; Ragù bolognese 105,000; Truffle cream 135,000. Report "82,000 to 135,000, six items" is correct; "five of six at or below 109,000" is correct; the derived median of 96,500 is correct ((95,000 + 98,000) / 2).
- Latte / flat white 50,000: correct. 50,000 / 29,000 = 1.72, correctly rounded to "about 1.7".
- Bowl: **the claim that "bowl 85-110k" is not in the file is correct.** The only bowl item is "Yogurt / oat bowl" 65,000. See F3 and F4.
- Functional drinks 48,000 (Kombucha / ginger shot) and 55,000 (Matcha / protein shake): correct. The report says they "sit near" the Burgreens range 27,000 to 52,000; 55,000 is above that range, so "near the top of or just above" is more exact (included in F3 as a wording point).
- The CSV's own benchmark cells (S31 to S34, S46) were not tested; the report says so. The values themselves are not quoted, which feeds F1.
- Basis: the placeholders are net of PBJT; Burgreens is net of tax and service; the media prices are unstated. The report states this limit.

## 5. Bias guards and labels

| Check | Result |
| --- | --- |
| Fact separated from "Analysis:" | Met in §2.1, §2.5, §4 (placeholder paragraph) and §7 (opening line). §5 verdicts are analysis but not under the label; acceptable because the table header says "tested against the plan's criteria". |
| Derived values labelled | Met. Every percentage, difference, share and the 1.7x ratio carries "(derived)" or a formula. Not labelled: "five of six at or below 109,000" (a simple count) and the counts of 6, 6, 4 and 16 in §3.1 (all correct). |
| Historical cases excluded from every rate | Met. No rate is given at all (n<10). Hard Rock, Fish & Co., Mövenpick and Karen's Diner are in §3.3 only. Texas Chicken is the one exception, handled wrongly (F2). |
| Claims rejected by earlier verifiers (Domino's, Pizza Marzano exits) | Met. §3.4 says neither claim is made; Domino's is "no exit evidence found, provisional" and Pizza Marzano is a single Sep 2025 observation. The 22 vs 23 conflict is kept. I confirmed that the CNBC Domino's article never names Indonesia as a market. |
| Limits of the price ladder stated | Met. Approximate prices (17 of 67; I confirmed the 17 = 6 + 3 + 4 + 4), brand concentration (Burgreens 35.8%, Marzano 26.9%, Fore 20.9%, top three 83.6%; recomputed and correct), no district split, thin Italian and bowl evidence, tax basis, and missing items. |
| Lessons applied | Approximate flag and counts (rule d), brand shares and "fewer than 4 brands" marking (rule f), "no disconfirmed unless Indonesia named" (rule d, 2026-10-17 entry), derived values not stored as data. |
| Gaps not filled with estimates | Met. |
| One-source verdicts | None. |

## 6. Acceptance checklist (plan §9 and §8)

| Plan item | Status | Evidence |
| --- | --- | --- |
| Competitor dataset and venue master (at least 40 venues; 8 priced per category; 4 per category in each Tier-1 district) | **Not met** | No `competitors.csv` or venue master; the discovery phase was not run. Priced brands: pasta 8, coffee 6, bowl 2, functional drinks 1; none per Tier-1 district. The report states this as a gap (§6, §8.1). |
| Price ladder: four item classes, stats per district where n>=4, placeholders by percentile, app uplift with n | **Partly met** | Four classes with min, median, max, n, brands and approximate counts, recomputed correctly. No district cell reaches n>=4, no percentile placement (correctly refused), no app uplift (sites blocked). |
| Competitor map: heat table district x category x format, with a saturation and white-space verdict | **Not met** | No heat table and no verdict (§6 GAP). The title promises a map that the content cannot supply; the report is honest about it. |
| Listed-operator table: five operators, each figure traced to a filing page, FY and unit stated, press marked secondary | **Partly met** | FAST, MAPB and Fore are from original filings (opened by me) with period, unit and geography stated. PZZA is a relay and ENAK a broker mirror of the 9M 2025 filing, both marked tier 3. Page numbers are not given in the report; FY2025 and H1 2026 ENAK is a gap. |
| Foreign-entrant table: exit proof and stated reason (or "not documented"); counts, no rate if n<10 | **Met** (with F2) | 16 in-window rows, no rate, historical rows separate. Fix the Texas Chicken placement. |
| Oakberry reconciliation | **Not met** | No Oakberry rows and no `oakberry-reconciled.md`; H7 is reported as a gap. |
| Sources and verification: all sources registered; §8 thresholds | **Met for registration; thresholds apply to this review** | All 42 cited IDs are in sources.md with tier. All 20 sources I opened match; 0 value mismatches in the full-check set. Mismatches are in citations only (F5, F6), which is under the 5% sample limit; they should be fixed and rechecked per §8(8). |
| Gap list | **Met** | §8.1 lists every missing item; add nothing except the F2 correction. |
| Report content asked for in §4: read-across for Team B (inputs only) | **Met** | §4 and §7. No model changes proposed. |

## 7. What to do next

Apply F1 and F2 (the two that change what a reader will conclude), then F3, F5 and F6 (traceability); F4, F7 to F12 are wording. After the fixes, a short re-check of §3 and §7 against the cited rows is enough; no new source needs opening. Per CLAUDE.md §10, add a `tasks/lessons.md` entry for F1 (a price comparison used a mass-chain sample and left out the premium evidence held in another input file) and F2 (a case was called undated although the dropped-rows file held its date): rule "before calling a fact a gap, search the dropped-rows file and the raw notes".
