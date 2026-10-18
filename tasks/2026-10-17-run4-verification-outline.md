# V-OUT: verification of reports/2026-10-17-pillar1-framework-outline.md

Date: 2026-10-17. Verifier: independent (did not write the outline). No edits made to the outline.

## Verdict: ACCEPT WITH FIXES

The structure and the PESTEL/CAGE/profiles roles are correct and the meeting-5 content is faithfully reported. Three claims or omissions need fixing: an unsupported Singapore/Dubai/Hong Kong claim (F1), the date conflict wording (F2), and an evidence line that is too thin and omits the interim-draft status (F3). None changes the structure.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | One page | 438 words by `wc -w` (header and file paths included), 33 lines. Fits one page; no length fix needed. |
| 2 | Accuracy of report descriptions | Mostly correct, see F1, F4, F5. |
| 3 | Maps to scope §6 | Yes. Sections 1 to 4 match "strategic fit assessment", "target customer overview", "cultural fit considerations", "clear strategic implications" (scope §6 Expected Output). Omitted on purpose: competitor and benchmark map, and Singapore/Dubai/Hong Kong comparison (see F1). |
| 4 | Roles as owner asked | Correct: PESTEL "how is it there", CAGE "what do the differences mean for us", profiles "who CORSA serves". Same wording as the reports' own headers. |
| 5 | Date conflict | See F2. |
| 6 | Plan mapping | See F4. |
| 7 | Evidence approach line | See F3. |

## Verified as correct

- PESTEL report has all six dimensions (sections 1 Political to 6 Legal), plus risk section, gaps and appendix. Title "how is it there?" matches.
- CAGE report covers the four dimensions (sections 3 to 6: administrative, cultural, geographic, economic), each with "What it means for CORSA", plus an investor summary. It credits Matthieu Normand (header; Appendix A, 174 claims: 161 verified, 5 corrected, 8 unverified). The outline never mentions Matthieu or his work, so no false claim, but see F5.
- Profiles report ranking: Primary 1 young urban professionals, Primary 2 (conditional) affluent upper-middle-class South Jakarta residents, Secondary 3 run and padel communities, Secondary 4 lifestyle café-goers (overlay). Students, creators (as customers), expats, families, nightlife are dropped, deferred or a gap.
- Meeting 5: the framework choice was left open (Tiago to report by next night). Samuel said CAGE "includes most of the discoveries we would have had in the PESTEL" and PESTEL would be a good "summary or addition" (recap section 04 "Consider PESTEL"; transcript 17:01). The outline's sentence "PESTEL serves as a summary or addition and does not repeat CAGE" is supported as Samuel's suggestion. 3 to 5 bullets per page, 10 to 15 pages, 10 minutes, "order is guidance": all supported (19:46, 26:23).
- Scope §6 sources: "interpretation, not generic country facts" is a direct paraphrase of scope §6.

## Findings

| ID | Severity | Finding | Suggested wording |
|---|---|---|---|
| F1 | Must fix | Section 1 says the strategic fit assessment covers "how it compares with Singapore, Dubai and Hong Kong" and cites pestel, competitor-map and demand-economics. None of the reports contains a Singapore, Dubai or Hong Kong comparison (grep of all reports: no match). The outline promises content that no source delivers. Also the scope's competitor and benchmark map (Oakberry) is not mentioned. | "1. **Strategic fit assessment.** Is Jakarta a sound first flagship, and which assumptions are strong or weak. Gap: the scope's brief comparison with Singapore, Dubai and Hong Kong is not yet covered by any report and needs a separate short piece. Source: ..." Optionally add "Competitor map: `reports/2026-10-17-competitor-map-and-price-ladder.md`." |
| F2 | Must fix | Date. Meeting 5 supports **21 Oct**: Decision 1 "interim presentation will be on October 21", Key points, Interim Presentation Date section (Samuel: "the 22nd is not possible for me", 24:42 "let's do the 21st", Jonas to confirm slot with Heiko). The scope supports **22 Oct** (§ timeline, "Interim presentation, 08:00-12:00"; also lines 70, 215, 219). The 08:00 start is from the scope, not from meeting 5. Meeting 5's own PDF recap carries a caution: its decision 4 ("framework and document outlook by 21 Oct") is flagged by the auto-check as imprecise, and Samuel himself said "I think the 22nd" at 17:01 before the discussion. The meeting is later and team-internal; the scope is the client document. They conflict and the outline cannot resolve it. The outline's heading currently asserts 22 Oct (08:00) as fact and the open point is only at the bottom. | Heading: "Proposed structure for the interim presentation (22 Oct per scope, 08:00-12:00; meeting 5 on 12 Oct settled 21 Oct; date to be confirmed with Heiko)". Open point: "Date conflict: scope says 22 Oct 08:00-12:00; meeting 5 (decision 1, 24:42) settled 21 Oct and Jonas was to confirm the slot with Heiko. Confirm the final slot before fixing the delivery date." Also: scope time window is 08:00-12:00, not an open end. |
| F3 | Must fix | Evidence approach is one line and does not say the reports are interim drafts. All three framework reports are "DRAFT for Team A"; the CAGE report was "awaiting independent verification (V-CAGE)" in its header; the profiles report states "Not yet independently verified". The profiles report also says "Findings are directional", no Jakarta 25-39 row exists, and expats cannot be assessed. Outline says "Only verified rows", which is accurate for rows but could be read as if the reports themselves are verified and investor-ready. It also does not mention that the branded investor PDF does not exist yet. | "Evidence approach. Facts come only from verified register rows, tagged `[row; geo-agefit]`; national or proxy evidence is flagged and gaps are named. The reports linked here are interim Markdown drafts, not the final branded investor PDF. Findings on Jakarta customers are directional: no verified row gives a Jakarta 25-39 view, and expats cannot be assessed." (Check the verification state of each draft on 19 Oct before sending, since V-CAGE and V-PROF rechecks exist in `tasks/`.) |
| F4 | Should fix | Plan mapping. The outline says "Plan 1 to 4 reports" without saying which is which, and "the three reports above" in section 4 is unclear (five-plus are named). Correct mapping from report headers: demand-economics = Plan 1; regulatory-entry-pathway = Plan 2; competitor-map-and-price-ladder = Plan 3; purchase-triggers-and-channels = Plan 4 (also matches `tasks/2026-10-16-plan-1..4`). The outline's use of each is sensible (Plan 3 and 1 for fit, Plan 4 for triggers, Plan 2 for halal/legal). | "Evidence base: Plan 1 `demand-economics`, Plan 2 `regulatory-entry-pathway`, Plan 3 `competitor-map-and-price-ladder`, Plan 4 `purchase-triggers-and-channels`, cited through the Evidence and Validation Appendix." Section 4 source: "synthesis of sections 1 to 3 and the three Pillar 1 reports (PESTEL, CAGE, profiles)." |
| F5 | Should fix | Matthieu is not credited. Meeting 5 and the CAGE report treat the CAGE structure as Matthieu's work (about 30% remaining, to be verified). The outline says "CAGE" without noting it builds on Team A's culture research. | In the CAGE bullet add: "built on Matthieu Normand's CAGE and culture research, now checked claim by claim." |
| F6 | Should fix | Profile bullet lists the scope groups as if all fit ("creators, students, expats") but the profiles report ranks only four and drops students and creators as customers and cannot assess expats. A reader would not learn the ranking. | "Customer profiles say who CORSA serves: first young urban professionals (25-39), then conditionally affluent South Jakarta residents, then run and padel communities and lifestyle café-goers; students and creators are not launch customers and expats cannot be assessed yet." |
| F7 | Minor | Header says "Samuel said the order is guidance" and the Summary says "Samuel noted that CAGE already covers much of what PESTEL would capture, so PESTEL serves as a summary or addition". Supported, but it is Samuel's suggestion, and he left the choice to the team ("it doesn't have to be PESTEL"). Last open point says framework choice "left open ... this outline proposes using both". Fine; make it clear who decides. | "Samuel suggested PESTEL as a summary or addition to CAGE and left the choice to the team (meeting 5)." |
| F8 | Minor | "Due 19 Oct 2026" in the status line comes from the run-4 plan, not meeting 5 (meeting 5: item 8 by the 19th, outlook by the 21st). Harmless, but not a meeting-5 deadline. | Keep, or write "internal deadline 19 Oct". |

## Verification notes

- Read: CLAUDE.md, scope §6 and timeline, meeting-5 recap (including the transcript), headers and section lists of PESTEL, CAGE, profiles, and the four evidence reports.
- Not done: I did not open the cited sources behind individual figures. The outline cites no figures, so no figure check was needed.
- No tier-4-only claims in the outline (it states no data).
