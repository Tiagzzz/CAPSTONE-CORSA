# Run 3 verification V4 (figures, hypotheses, bias, matrix, acceptance, length): Plan 4 report

Date: 2026-10-17. Verifier: V4 (independent; did not write the report). Objects checked: `reports/2026-10-17-purchase-triggers-and-channels.md` (6,598 words) and `data/processed/plan4-trigger-matrix.csv` (20 rows). Against: CLAUDE.md §5 and §7, plan 4 §2, §7 (V1/V2/V4) and §8, gap analysis §6, `data/processed/README.md`. The report was not edited. Nothing was committed.

## Verdict: ACCEPT WITH FIXES

No blocker. Every figure traces and no fabrication was found. There are six majors, mostly overstated interpretation and one acceptance-criterion breach (conversion figures used in conclusions). All fixes are wording or relocation; none needs new research.

## 1. Method and trace results

- **Row trace (100%, not a 50% sample).** All 230 citation tags in the report (132 unique) were checked by script against the cited row in `data/processed/plan4-*.csv` and `demand/*.csv`: row id exists, register id appears in the row's `register_id`, geography code, age-fit code, base and ref_period match, and `verification` is VERIFIED-OPENED or CORRECTED-OPENED. Result: 0 mismatches on value, unit, geography, age-fit or register id. The 7 BLOCKED rows appear only in the boxed provisional list. Two cosmetic differences, F9 and F11.
- **Summary and hypothesis figures (100%).** All were checked against the rows and then against the live source (see below). All match.
- **Matrix.** All 219 non-empty cell entries (172 distinct rows) parsed; register id, age-fit, geography and verification agree with the source rows in every case. All 59 register ids exist in `sources/sources.md`, none is tier 4, none is snippet-only.
- **Sources opened by me (curl -sL, browser UA, saved to `/tmp/claude-0/-home-user-CAPSTONE-CORSA/c8401b57-6bf2-5305-9a01-f1d1e4e31e77/scratchpad/v4/`; no bot check bypassed).** 33 opened, all values matched the rows.
  - Jakpat local F&B (BEH-040): 64, 49, 48, 40, 35, 26, 16, 77, 60, 59, 44, 44, 43.
  - GoodStats discovery chart (BEH-004): 44, 40, 39, 35.
  - NIQ (BEH-013): 65, 48, 19, 46, 77, 62, 43.
  - YouGov (BEH-010): 7, 52, 39, 23.
  - Jakpat live vs affiliate (BEH-074): 83, under 40, 92, n=1,714.
  - Jakpat live-shopping series (BEH-075): 46 to 44.
  - GoodStats cafe revisit (BEH-066): 83, 78, 70, 64, 45, 27, 49.1, n=932.
  - Polri MotoGP (BEH-027): 140,324 and 15.7%.
  - Jakpat coffee (BEH-030): 44 and 34.
  - Marketing-Interactive 76% (BEH-005).
  - Pasardana (BEH-006): 2.42, 2.36, 1.98, 67%.
  - Playtomic PDF (BEH-042): +173%, "Jakarta has +50 clubs".
  - Merdeka (BEH-017): 27,300 and 70%.
  - CNN halal (BEH-069): 83%.
  - Jakpat delivery (BEH-039): 67% and 55%.
  - GoodStats reasons (BEH-071): 73, 44, 42, 49, 48, n=769.
  - CNBC KFC (BEH-045), CNBC Starbucks (BEH-048), Detik Pizza Hut (BEH-052).
  - Kontan MSI (DEM-046).
  - BI consumer survey Sept 2026, Jakarta CCI table (DEM-034; image table read visually: 146.8, Aug 150.0, Sep 2025 145.5).
  - Populix relay (BEH-009).
  - Journal BEH-067.
  - APJII 2025 (BEH-037): 42.27, 25.33, 33.4, 12.74, 28.58, 7.15, 17.33.
  - APJII 2026 (BEH-038, page 94 read visually): 32.3, 30.8, 31.9, 28.7, 31.2, 24.4.
  - Databoks/GoodStats (BEH-003, BEH-083, BEH-082, BEH-087): GoFood 38 and 43, ShopeeFood 39, lunch spend 58,609 / 65,130 / 63,250, matcha 34 and 32, jamu 17 and 27.
  - Jakpat coffee Gen Z (DEM-001): 47%, taste 46%, n=896 of 1,150.
  - Databoks mall survey (DEM-002), Strava relay (BEH-016), CNA padel permits (BEH-044), journal BEH-079 (n=85).
- **Evidence profile (counting unique tags).** Geography N 87, U 32, J 10, P 3. Age-fit D 93 (70%), C 28, B 11, A 0. No figure is a 25-39 cut. The report says this in the Summary.

## 2. Findings table

| # | Location | Issue | Severity | Fix |
| --- | --- | --- | --- | --- |
| F1 | "CAC and unit-economics items for Team B" (line 241: "none is used in the findings above"); Summary; lines 24, 27, 61, 114, 117-118, 213 (Disconfirming #6) | Plan §8 CAC note: any CAC or conversion figure is "only listed for Team B, not used in conclusions". The report uses conversion figures in conclusions: opened 83 vs bought under 40 (affiliate-link conversion), the live-shopping purchase-rate series 46/44, delivery order-value bands, promo reach. They drive the Analysis ("creator-link headline overstates conversion"), Disconfirming #6 and the basket-size reading. The statement "none is used" is false. | major | Either move these conclusions out (keep the figures only in the Team B list), or delete the "none is used" sentence and record in the plan a deliberate exception (conversion shown as disconfirming evidence, not CAC). Recommended: keep the numbers as sourced context but drop the Disconfirming #6 and basket-size conclusions. |
| F2 | H1 verdict (lines 130-136), Summary | The verdict "not supported" rests on 44% vs 40%, the report's own words "within the margin of error", in a Java-urban sample (U), no age split, one source (GoodStats relay of Jakpat). By the standard used for H2, H4 and H5 (no 25-39, no Jakarta), this is "insufficient evidence, nominally against". The entry change (move creator-seeding budget to peer referral, Maps, apps) is an operational call made on a non-significant gap. The other plan disconfirmers (promos lead; 29+ rely on Maps or apps; creator trust falling) are not tested one by one. BEH-005's own headline "declining trust" is not cited for the "trust falling" prong. The trust ranking (2.42/2.36/1.98) is a six-market regional relay (P). | major | Re-label "insufficient evidence (nominally against H1)". Soften the entry change to "test peer referral and Maps/review presence alongside creators". Test each plan disconfirmer in one line, including the promo prong (price 64%, opening promos 48% are higher-ranked trial attractors than social). |
| F3 | H3 verdict "supported" (lines 146-152), Summary | The only "supported" verdict rests on one NIQ press release (Indonesia n not on the page; food products with added nutrition, not restaurants), stated WTP only, no age or Jakarta. The hypothesis is about purchases ("changes purchases only modestly"); no purchase row exists. "Intent is high 65%" mislabels the item (65% = healthy nutrition more important than five years ago, not purchase intent). 48% willing to pay over 10% more is nearly half, which is not obviously "modest". | major | Re-label "partly supported at the stated level; observed purchases untested" (or insufficient evidence). Replace "intent is high 65%" with "importance rose vs five years ago 65%". Keep the NIQ product-category caveat in the Summary line, not only in the section. |
| F4 | H5 evidence and Disconfirming #7 (lines 162-168, 214); Analysis line 78 | Company financials are framed as boycott evidence. (a) FAST's loss narrowed 57% (239.58 vs 557.08); the CNBC article says "Meski rugi membaik" (loss improving) and revenue fell 0.76%. The report calls it "continuing net losses ... against" H5 and a "boycott spillover" without saying it narrowed. (b) No opened source attributes the FAST or Pizza Hut results to the boycott (the Pizza Hut row notes attribution to boycott fade or efficiency was not verified; MAPB management blames boycott narratives). (c) Closures "19 outlets; 400 employees" (Oct 2025) are older than the 20 outlets / 1,041 employees in the same CNBC article cited for Q6-001. (d) 77% "prefer local culinary businesses" comes from an item about local cuisine and local businesses (Padang, noodles, geprek); it has no foreign-brand comparison, so "Local preference and boycott spillover" overreaches. | major | Add "loss narrowed 57%" and the revenue direction. Label causal links as management claims or not established. Cite the later 20 / 1,041 figures or state the difference in measure. Rename #7 to "Stated local-cuisine preference; chain results unexplained", or move it out of the disconfirming list. |
| F5 | "Analysis, ranked by strength of evidence", item 1 (line 118) | "Price and promotion ... also compress the basket" is an unsupported causal claim. No row links promotions to basket size (the Snapcart bands are a distribution only), and line 53 says "the rows do not show that [a promotion] raises spend per order". The two statements pull in different directions. | major | Delete "they also compress the basket" or relabel as hypothesis; keep "conversion lever with a margin cost" only if marked as an assumption. |
| F6 | Disconfirming #5 "Atmosphere is not the return reason" (line 212); Summary; H2, H7 | (a) "Aesthetics 27" is one of six prompted items. Comfortable room 78%, clean 64%, facilities 45% are atmosphere-adjacent, so the heading overreaches. (b) The survey was run by Kedai Kopi (a cafe vendor, middle class, non-probability, GoodStats relay), but the tag reads "N, D" with no vendor flag. (c) BEH-067's abstract tests servicescape → satisfaction only; it also finds brand attachment and brand characteristics significantly drive brand attitude and revisit intention, which is relevant to CORSA's identity and is omitted while the same row is used as disconfirming. | major | Retitle "Aesthetics ranks last of six listed revisit reasons". Add "vendor-run survey, sampling not stated". Mention the brand-attachment finding in H7 and the identity section. |
| F7 | Tags throughout (about 6 occurrences: P4W7b-18, P4W7b-15, in Summary-linked H8, gap table, Method) | Reference periods are truncated at 48 characters: "Cited on 2025-06-21 from a Populix report fielde" (hides "fielded 2023"); "Peer-reviewed article, Vol. 19 No. 1, February 2" (the year 2026 is cut). | minor | Shorten the stored ref_period in the tag ("fieldwork 2023, cited 2025-06-21"; "Feb 2026") rather than cutting mid-word. |
| F8 | Summary, Findings, Hypotheses (e.g. "83, 78, 70", "27", "46, 44", "92", "33") | Many bare numbers have no unit or %. The tag convention promises value and unit. | minor | Add % or the unit next to every number, especially ranked lists. |
| F9 | Title; Summary | The title promises "what the opened evidence shows for CORSA in Jakarta", but 119 of 132 unique tags are N, U or P. Only 10 are J, and J includes a Jabodetabek mall survey and DKI per-capita spend. The Summary is honest ("not Jakarta estimates"). | minor | Retitle (for example "...: national and urban-Java evidence for a Jakarta launch"). State the geography counts in the Summary (J 10, U 32, N 87, P 3). |
| F10 | Third place (line 84), line 220, Analysis | The J code on the mall survey (DEM-002: Jabodetabek, upscale and mid-range malls, 71% male, non-probability, n=266 of 800, odd wording per row note) overstates Jakarta fit. It is then used as the single example of a group effect ("invitations 65%"). The matrix and report also copy a free-text geography for P1C1-E01 and P1C1-E06 where the tag letters are J and N. | minor | Code it "J*/U (Jabodetabek, non-probability, male-skewed)" or flag in-line. |
| F11 | Basket size (line 114), Disconfirming #3 (line 210) | The Mandiri period "Q3 2026 vs 2025" is inferred (row note, Run 2 verification). The Kontan article calls restaurants the fastest-growing monitored category and Q3 2026 growth 5.9% higher than Q3 2025 (5.4%). The report omits both and files an aggregate-spend figure under "basket size". | minor | State "period inferred". Add the "still the fastest-growing category" caveat. Move the line out of basket size. |
| F12 | Findings by age group (lines 101-106) | APJII 2025 and 2026 values sit side by side, and the Analysis contrasts the waves ("2025 TikTok and Instagram fall with age, 2026 the generations are close"). The report warns only about YouTube, but the 2026 option list changed (WhatsApp and Threads added; WhatsApp scores 1.1% as "most accessed"), and the 2026 sample slide uses 14-29 for Gen Z. Facebook (31.1% Millennial, 31.0% Gen X, at par with TikTok in 2026) is omitted entirely. | minor | Extend the do-not-compare warning to all platform items. Present each wave separately. Add Facebook. |
| F13 | Disconfirming #2 "Price first" (line 209), line 49 | 60% vs 59% (price vs taste) and 47% vs 46% (Gen Z coffee) are ties within the survey's margin of error (<5%). The report applies the margin to H1 but not here. Taste 46% is dropped from the DEM-001 sentence. | minor | "Price and taste lead jointly"; include 46%. |
| F14 | H7 (lines 178-184), Identity table | (a) 62% "want clearer labels" is a transparency demand, not scepticism toward functional drinks. (b) Matcha (a trend drink) stands in for functional drinks with no "proxy" label. (c) The plan's confirming item "hours" of third-place use is absent (no dwell row), yet "third place supported" is stated. | minor | Rename (a) "label transparency wanted". Label (b) as a proxy. Say "gathering and work motives documented; dwell time not". |
| F15 | H4 evidence for (line 156), Community analysis | "Participation is large and growing" cites padel GMV per court (platform revenue) and the Strava club count, neither of which is participation. "+50 clubs for 25M inhabitants" is ambiguous (the slide says Jakarta has +50 clubs, underserving 25M). | minor | Restate as "event entrants; club count; court revenue" and quote the slide wording. |
| F16 | Creator-link lines (24, 243) | The 76% headline is a mixed population (consumers, creators and experts per the row note) coded N with no flag, repeated in the Team B list. The 67% is a six-market regional figure (P). | minor | Add "mixed respondents" to the tag text. |
| F17 | Conversion and promo lines (110, 246, 245) | Order bands are unnamed ("lowest band", "middle band", "next band"); the IDR bands (<50k, 50-100k, 100-150k) are missing. "Opening promos 48%" (attractor) and "26%" (UA-N63, timing question) sit in different sections without reconciling. | minor | Name the bands. Add one line explaining the two opening-promo figures. |
| F18 | Method line 258 and §8 date rule | Several figures have fieldwork before 2024-10-16: IMGR Mar-Aug 2024 (about 14 matrix entries), YouGov Sep 2024, halal 2023. Plan §8 permits this only for long-run trends with a recent latest point. The Method note says "some rows predate the window" but does not mark them per cell. | minor | Mark them "pre-window fieldwork; published after" in the tag or a footnote, and state the §8 reasoning. |
| F19 | Matrix `plan4-trigger-matrix.csv` | (a) "GAP: GAP:" duplicated prefix in every GAP cell. (b) Hypotheses column maps "Price and taste" to H3 and "Delivery-app channel" to H1 (loose). (c) Millennial values are repeated in the Younger and Older columns (documented and flagged, not aggregated). | minor | Strip the duplicate prefix. Remap or label "context". |
| F20 | `data/processed/README.md` | No entry for `plan4-trigger-matrix.csv` or `plan4-misc-run3.csv` (the §8 method-note criterion). The README defines age-fit B as "canonical band fully inside native"; plan §4 defines B as overlap above 75%, C 50-75%, D below 50%. The report follows the README, so the definitions diverge. | minor | Add the matrix and misc-run3 sections. State which age-fit definition governs. |
| F21 | Provisional box (line 95); Gaps table (lines 226-237) | The box reproduces seven BLOCKED figures with numbers in the body. Harmless but long, and the report says "do not rely". The gap table has no explicit "why desk research could not answer" column (plan §8/§9 wording). | minor | Move the box to the CSV or an appendix. Add the reason column or fold it into "Still missing". |
| F22 | Fact bullets that carry interpretation (lines 104 "a likely questionnaire break"; 164 "consistent with brand-specific boycotts"; 75 and 164 management claims) | Small interpretive phrases sit inside fact bullets and "Evidence for" lists, outside "Analysis:". The separation is otherwise good. | minor | Move them under "Analysis:", or tag "(company claim)". |
| F23 | Summary "only direct channel comparison" (line 11) | Not strictly the only one: reasons to try (social 44% vs reviews 42%, BEH-071) and the trust ranking (BEH-006) are also comparisons. | minor | "The only comparison of first-learned-of routes". |

## 3. Hypothesis verdict test (against plan §2 disconfirmers)

| H | Report verdict | V4 reading | Flag |
| --- | --- | --- | --- |
| H1 | not supported as stated | The "friends lead" disconfirmer is met only nominally (within MoE). The confirming test (≥2 sources, 25-39) is unmet. The promo and Maps/app prongs are not tested. | Over-stated (F2). Should be "insufficient, nominally against". |
| H2 | insufficient evidence | The weak-repeat disconfirmer is untestable (gap, correctly so). The age pattern runs against "especially Gen Z" in one qualitative D row. The Jakarta FoMO study is correctly not used. | Fair. |
| H3 | supported (stated, price-capped) | The plan's own confirming criterion (stated intent plus price-capped behaviour) is technically met by NIQ 48% to 19%. The purchase claim is untested. Single vendor release. | Over-stated (F3). |
| H4 | insufficient evidence | Participation is evidenced. Age mix and purchase influence are absent. The report calls this a gap, not a negative. | Fair. Wording issue F15. |
| H5 | insufficient evidence | Origin and COO evidence is absent. The financials are not a test. | Verdict fair. The evidence lists are misframed (F4). |
| H6 | insufficient evidence | Attendance only, no demographics. | Fair. |
| H7 | insufficient evidence (split) | Third-place half is partly documented (motives only). The functional-drink half has no growth series. | Fair. Wording F14. |
| H8 | insufficient evidence | One relayed 2023 vendor figure, with the headline/quote conflict disclosed. | Fair. |

## 4. Bias guards (gap analysis §6; plan B1, B2, B7, B14)

| Guard | Result |
| --- | --- |
| Fact vs "Analysis:" separated | Mostly met: 14 "Analysis:" blocks, sourced bullets elsewhere. Leaks in F22, and F5 (an unsupported causal claim inside an Analysis block). |
| No Hofstede-to-behaviour or collectivism-as-opportunity claim | Met. Grep for Hofstede, collectivism, culture finds only the explicit disclaimers (lines 220, 259). Group effects are tied to survey items. |
| "No data" reported as a gap, not "no effect" | Met in the report ("absence of a row, not proof..."; H4 and H5 sections). Exceptions: F2 and the label "not supported" for H1; F6's "Atmosphere is not the return reason" reads a ranking as a negative. |
| National or Java-urban not presented as Jakarta | Largely met (tags, Method, Summary). Weak points: the title (F9) and the J coding of the Jabodetabek mall survey (F10). |
| Proxy categories (beauty, fashion) labelled | Met. No beauty or fashion figure appears in the report. The matrix labels the YouGov makeup rows as proxy (P). Residual: matcha for functional drinks is unlabelled (F14). |
| Stated vs observed | Mostly met ("stated" is repeated; "all stated, none age-specific" in the ranked list). Exceptions: F3 (intent vs importance), F5 (basket compression). |

## 5. Matrix check (plan §8 row 1)

| Criterion | Result |
| --- | --- |
| Every non-empty cell has value, source id, period, base, age-fit, geography | Met: 219 of 219 entries parse with all fields and match their rows. Geography free text for 2 spend rows (F10, F19). |
| Empty cells say GAP with reason | Met: no empty cell; every GAP carries a reason (cosmetic double prefix, F19). |
| No D-coded cell aggregated | Met: no sums, averages or pooling. D-coded generation-labelled rows (for example matcha Gen Z) appear in band cells, flagged D. The Millennial band is duplicated, not split, and flagged. |
| Every cell has a registered tier 1-3 source | Met: 59 of 59 ids registered, tiers 1-3, none snippet-only or BLOCKED. |
| 25-39 derived column | All GAP with reason ("no source reports 25-39"). Correct. |
| 0 figures older than 2024-10-16 unless long-run | Partly met: about 23 entries with 2024 or 2023 fieldwork (IMGR, YouGov, halal), published after the cutoff but not marked per cell (F18). |

## 6. Plan §8 acceptance checklist

| Criterion | Status | Note |
| --- | --- | --- |
| Matrix cells complete (id, value, year, base, age-fit, geography) | Met | Section 5. |
| GAP cells have reasons; no tier-4-only cell | Met | |
| 0 figures older than 2024-10-16 unless marked long-run | Partly met | F18. |
| `plan4-*.csv` per theme plus README method note, reproducible from `data/raw/` | Partly met | The theme CSVs exist and `data/raw/plan4-*/findings.md` exist. The README has no entry for the matrix or `plan4-misc-run3.csv`, and age-fit definitions diverge (F20). |
| 100% of cited sources registered with all fields | Met | All 55 ids in the report are registered with ID, title, publisher, URL, date, access date, tier, use. |
| Report sections: by age group, channel evidence, identity-transfer tests with verdict and entry change, fact/interpretation labelled, explicit disconfirming section | Met | Present. Quality issues F1 to F6. |
| Report about 6-8 pages | Not met | About 6,600 words, roughly 13-15 pages; see section 7. |
| Gap list and primary-research brief: every §9 question with the reason desk research could not answer it | Partly met | All §9 items are covered (the racing and Italian gaps are merged). There is no explicit "why desk research failed" column (F21). Two gaps were added. |
| CAC note: figures only listed for Team B, not used in conclusions | Not met | F1. |
| Verification report (V1-V4 pass; unresolved items listed) | Pending | This file is V4. V1 to V3 were not available to me. All majors above are unresolved items. |
| Verdict of supported / not supported / insufficient for each identity element | Met | The table lists all four; H1 and H3 labels need correction (F2, F3). |

## 7. Length: recommended cuts (not made)

Current: 6,598 words. 230 citation tags account for about 1,935 words (29%); prose is about 4,660 words. Target for 6 to 8 pages is roughly 3,500 to 4,000 words. Recommended, in order of saving:

1. **Compact the tags** (about 1,200 to 1,400 words). Inline show only `[row id; geo-age-fit]` (for example `[P4W1-R04; U-D]`), with the full tag (register, period, base) in the CSV or one appendix table. Keep the full tag only in the Summary and hypothesis verdicts.
2. **Merge "Conversion and higher-spend drivers" (about 380 words) into the trigger sections**, and delete the duplicate figures (trial list, basket list). Add the F1 fix at the same time.
3. **Fold "Disconfirming evidence" (about 505 words) into the hypothesis sections** or keep only a 9-line list with no figures repeated. Most items duplicate H1, H2, H3, H5 and H7.
4. **Delete the "Identity-transfer tests" table (about 200 words)**, or delete H5, H6 and H7 prose that repeats it.
5. **Move the provisional BLOCKED box (about 130 words) and the Team B list (about 290 words)** to a separate appendix file or the CSV.
6. **Cut low-value trigger content (about 250 words):** QRIS and PayLater infrastructure (a baseline, not a trigger); Strava weekly km; the full delivery-app share list; reference-year detail of Mandiri; the qualitative micro-influencer and student-sample bullets (n=85, n=100, n=400).
7. **Method and limits (about 296 words):** reduce to about 100 words, because the "How to read the citations" paragraph already states most of it.

Expected result: about 3,800 to 4,200 words with the evidence preserved in the CSVs.

## 8. Required before the Product Owner reviews

F1 to F6 (majors). F7 to F9 and F18 to F20 are quick edits. The rest are optional polish. Re-run my trace after the edits; the figures do not need re-opening unless values change.

---

# Re-check (revision 2)

Date: 2026-10-17. Re-verified: revised `reports/2026-10-17-purchase-triggers-and-channels.md` (now 4,489 words, about 600 of them in the new Appendix) and `data/processed/plan4-trigger-matrix.csv` (21 rows; new row "Price context"). The report and the matrix were not edited by me. No commits.

## Overall verdict: ACCEPT WITH MINOR FIXES

No blocker and no major remains. F1 to F6 are fixed. Residual items R1 to R6 are minor. F20 (README) is handled separately and is still open.

## R0. Trace results

- **Tags.** 128 tags in the new compact format `[row id; geography-agefit]` (multi-id tags expanded), 132 distinct rows. For every row: the row exists, geography code and age-fit match, and verification is VERIFIED-OPENED or CORRECTED-OPENED. 0 mismatches. A value check on every single-row tag found no wrong number (14 script flags were false positives caused by years or units preceding the tag; I checked each by hand).
- **Summary counts.** The report's "14 J, 2 J*, 22 U, 91 N, 3 P" matches my count from the rows (J 16 including the two mall rows, U 22, N 91, P 3). Age-fit: D 94, C 24, B 14, A 0. This reconciles with the earlier stated 70% D.
- **Appendix.** Every cited row appears in the Appendix. Register ids and bases agree with the rows (0 mismatches).
- **Summary and hypothesis figures (100%).** 44, 40, 64, 83, 65, 48, 19, 146.8, 4.7 and 6.1, 83 (halal), 77, 35/16/40 and others all match their rows.
- **Live sources reopened (new or changed rows).**
  - Databoks padel (BEH-091): 326 courts in DKI Jakarta, 947 national.
  - Kontan Liga.Tennis (BEH-095): padel 21-40 share 58.30%; about IDR 400,000 per session plus IDR 50,000.
  - Databoks GMV (BEH-102): GrabFood USD 2.94 bn, GoFood 1.98.
  - GoTo release (BEH-103): Delivery GTV 41.8 trillion, +8%; net revenue 9.463, +16%.
  - Okezone (BEH-104): 157,875 spectators.
  - Kontan Isoplus (BEH-099): 44% Jakarta, 37% Bodetabek, 19% elsewhere.
  - Earlier re-opened: APJII 2025 and 2026 tables for the new Facebook cells (UA-N09, N11, N15, N20, N23, N27 agree with the rows and the 2026 slide I read visually: Facebook 26.9, 31.1, 31.0).
  - All values match.
- **Price medians.** I recomputed from `price-ladder.csv`: coffee 23 items, median 29,000; bowl 15 items, median 60,000. These match the report and the matrix.

## R1. Status of F1 to F19

| # | Status | Evidence in revision |
| --- | --- | --- |
| F1 | Fixed | Conversion figures now labelled "Context on conversion (used in no verdict or entry change)"; the Disconfirming #6 and basket-size conclusions are gone; the Team B text says no verdict rests on them. |
| F2 | Fixed | H1 "insufficient evidence, nominally against"; all four disconfirmers tested, including the promo prong; entry change softened ("do not move budget on this evidence alone"); "declining trust" mentioned. |
| F3 | Fixed | H3 "partly supported at the stated level; purchases untested"; 65% restated as importance vs five years ago; "not modest by itself" noted; the product caveat is in the Summary. |
| F4 | Fixed | FAST loss "narrowed (about 57% lower)"; 20 outlets and 1,041 employees cited as a different measure; no source attributes results to the boycott; 77% flagged as a local-cuisine item; "boycott spillover" heading removed. |
| F5 | Fixed | The ranked Analysis block and "compress the basket" are gone; the Analysis says the rows do not show what a promotion does to spend. |
| F6 | Fixed | "Aesthetics ranks last of six prompted items; comfort, cleanliness and facilities ... in between"; Kedai Kopi vendor survey flagged; brand-attitude finding added; the "Atmosphere is not the return reason" heading is gone. |
| F7 | Fixed | The Appendix holds full periods ("fielded 2023 (pre-window)", "February 2026"). |
| F8 | Fixed | Percent signs and units present on every figure I checked. |
| F9 | Fixed | New title ("national and urban-Java evidence for a Jakarta launch"); geography counts stated in the Summary. |
| F10 | Fixed in the report | J* code with in-line caveat for the mall rows. Residual: P4W10-08 ("95 venues in Greater Jakarta", J), and the matrix still carries free-text geography for the two Susenas rows. See R5. |
| F11 | Fixed | "period labels inferred", "still the fastest-growing monitored category but slowing"; moved out of basket size. |
| F12 | Fixed | Wave-by-wave table, Facebook added, explicit "never trended across waves". |
| F13 | Fixed | "tie within the surveys' margin of error"; taste 46% named. |
| F14 | Fixed | Labels called a "transparency demand"; matcha called a proxy; "dwell time is not [documented]". |
| F15 | Fixed | Platform revenue is not called participation; "+50 clubs" flagged as ambiguous slide wording. |
| F16 | Fixed | Mixed sample stated for the 76%. |
| F17 | Fixed | Order bands named in IDR; 48% vs 26% opening-promo figures reconciled in one sentence. |
| F18 | Fixed as disclosure | "pre-window" marks in the Appendix; the Method states the departure from the plan 8 date rule. The criterion itself stays "partly met". |
| F19 | Mostly fixed | "GAP: GAP:" prefix gone; hypotheses column remapped to "context" for price and delivery. Two cells now read only "GAP: same" (see R4). The Millennial duplication is documented. |

## R2. New residual findings (all minor)

| # | Location | Issue | Severity | Fix |
| --- | --- | --- | --- | --- |
| R1 | Summary (H4: "scale and age skew documented"), Community analysis, H4, entry change | The 21-40 "skew" is one operator's platform (Liga.Tennis, about 100,000 users, seven clubs, all racquet sports, location not stated, no population baseline), so "documented" overstates. The entry change "consider padel venues' own cafes" rests on one operator's quote (n=1) and an IDR 50,000 consumption average that covers all racquet sports. | minor | Say "one platform shows 58% aged 21-40; no baseline". Mark the cafes idea a hypothesis for the organiser interviews. |
| R2 | Matrix, new row "Price context (Plan 3 cross-reference)" | The cell is a derived median across items (coffee: 23 items, 6 brands, mixed bases including app and Google Maps approximate prices; bowls: 2 brands) with register ids CMP-xxx and a "row set" reference instead of a row id, D-coded, geography "J / U" mixed. It is not a trigger by age cell, and a strict reading of "no D-coded cell aggregated" applies. The medians reproduce, and the limits are stated in the cell. | minor | Move it to a separate context file or the report text only, or keep it and add the row ids; state that it is not an age cell. |
| R3 | Price, promotions and delivery: Plan 3 cross-reference and Analysis ("the listed coffee median lies above the two largest per-cup spend bands") | Listed menu prices (signature drinks, a mix of media and in-store prices) are set against Gen Z national cup-spend bands (including home-made coffee). The report labels this "indications only", which is adequate, but the comparison sentence reads as a finding. | minor | Delete the comparison sentence, or add "different bases" to it. |
| R4 | Matrix: two cells read "GAP: same" | The reason points to a neighbouring cell, so it is not self-contained. | minor | Write the reason out. |
| R5 | Matrix geography strings (P1C1-E01 "DKI Jakarta (province)", E06 "National - benchmark") and P4W10-08 "95 venues in Greater Jakarta" coded J | Free text instead of a J/U/N/P code; Greater Jakarta is not DKI. | minor | Code as J / N, with "Greater Jakarta" in the note (J* if consistent with the mall rows). |
| R6 | Length | About 3,900 words of body plus the Appendix (about 600): roughly 8-9 pages. This is much improved from 6,598 words but still at or above the top of the 6-8 page target. | minor | Optional cuts: the Delivery GMV and GoTo bullet (about 90 words), the Isoplus origin bullet, the padel stock bullet details, and the Appendix into the CSV. |

## R3. Bias-guard read of the new sections

| Section | Result |
| --- | --- |
| Racing and Italian origin | Good: counts only, "circuit in Lombok, not Jakarta", explicit documented gaps (GAP-Q8-1, GAP-Q8-2) rather than "no effect". The Analysis says attendance is growing but who attends is unknown. |
| Padel and community | Original not opened for the Core & Court count is stated; units flagged as not comparable (326 courts, 397 per CNA, 95 venues); "one operator's platform, not a market". The skew claim is slightly overstated (R1). |
| Delivery GMV | Estimates flagged (include cancelled orders); "growth rates are not shares". No causal claim. |
| Plan 3 price cross-reference | Limits stated; no verdict depends on it. See R2 and R3. |
| Fact vs Analysis; Hofstede and collectivism; "no data" vs "no effect"; Jakarta vs national; proxy labels; stated vs observed | All met in the revision. Matcha is labelled as a proxy. Group effects appear only where a survey measures them. The mall survey is caveated (J*). |

## R4. Updated acceptance checklist (plan §8)

| Criterion | Status | Note |
| --- | --- | --- |
| Matrix cells complete (id, value, year, base, age-fit, geography) | Met | 249 of 249 entries parse and match their rows (200 distinct rows). The new price row uses CMP ids and a derived statistic (R2). |
| GAP cells with reasons; no tier-4 or BLOCKED cell | Met | Two "GAP: same" cells (R4). |
| 0 figures older than 2024-10-16 unless long-run | Partly met | Pre-window fieldwork is disclosed per row in the Appendix and in the Method, but it is a departure from the rule. |
| `plan4-*.csv` per theme plus README method note | Partly met | README still has no entry for the matrix or `plan4-misc-run3.csv` (F20; handled separately). The Method admits this. |
| 100% of cited sources registered with all fields | Met | The new BEH-091 to BEH-104 and CMP rows are registered (14 new BEH ids found). |
| Report sections and verdicts (age, channel, identity tests, labelling, disconfirmers) | Met | The identity table was replaced by H5 to H7 prose and the new Racing and Italian section; each hypothesis has a verdict and an entry change. The standalone disconfirming-evidence section is now merged into H1 to H5 and "Assumptions most at risk"; this satisfies the intent. |
| Report about 6-8 pages | Partly met | R6. |
| Gap list and primary-research brief with reasons | Met | The "Why desk research could not answer" column was added. |
| CAC note: listed for Team B, not used in conclusions | Met | F1 fixed. |
| Verification report | Pending | V1 to V3 not seen by me; this file now covers V4 twice. The open items are R1 to R6, the F20 README entry and the V1 to V3 findings. |

## R5. Required next

1. Fix R1 (wording). The rest of R2 to R6 are optional polish.
2. Complete F20 (README entries for the matrix and `plan4-misc-run3.csv`; state which age-fit definition governs).
3. No re-opening of sources is needed unless values change; my trace scripts are in the scratchpad `v4/` folder.
