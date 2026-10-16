# Plan 1 C3: Consumer surveys on eating out and café spend (findings, staging)

Worker: P1-C3 (Plan 1 Q3–Q6). Date of run: 2026-10-16 (run 1). Staging only: the registrar assigns final IDs and the register (`sources/sources.md`) is not edited here.

## Access and method

- **Network test:** WebFetch on `insight.jakpat.net` (Jakpat "At the restaurant" report) failed with `getaddrinfo ENOTFOUND`. All other sources were reached through WebSearch only, under the owner-approved fallback in `tasks/2026-10-16-execution-run-log.md`. Every figure below is therefore `snippet-only (not opened)`.
- **Snippet caveat:** WebSearch returns summary text, not verbatim page text. The "snippet" column is the exact wording of the search result. Any figure not literally present in that text was not used.
- **Date rule:** a figure is staged only when a publication date is literally shown (or the search result states it). Figures with fieldwork dates but no publication date are listed under "Excluded" below.
- **Queries used (all WebSearch, mode standard):** Jakpat millennials restaurant frequency; Jakpat coffee 2025 frequency; Databoks eat-out factors 2025; BPS DKI food spend; Databoks Gen Z coffee spend; Katadata mall survey; Databoks young eat-out 2025; Jakpat "Indonesia 2025" coffee; BPS Pola Konsumsi DKI 2025; e-Conomy SEA 2025 food delivery; Jakarta café visit frequency (Indonesian query).

## Sources staged (in CSV)

### P1-C3-S1: Gen Z coffee spend per cup (Jakpat via Databoks)
- Title: "How much do Gen Z spend on coffee? This survey reveals" (Databoks)
- Publisher: Jakpat survey, republished by Katadata Databoks
- URL: https://databoks.katadata.co.id/en/consumer-services/statistics/677cd50372d4a/how-much-do-gen-z-spend-on-coffee-this-survey-reveals
- Publication date: 2025-01-07 (per search summary: "published January 7, 2025")
- Fieldwork: 6–9 Dec 2024, national online panel, n=1,155 Gen Z respondents (born 1997–2012)
- Access date: 2026-10-16
- Proposed tier: 3 (vendor survey via a republisher; figure is public). Justification: Jakpat is a commercial panel; the Databoks summary is public; no primary source found.
- Access status: snippet-only (not opened). Article is paywalled beyond the summary.
- Search query: "Databoks how much do Gen Z spend on coffee this survey reveals Rp10,000 cup"
- Figure and exact snippet: **48%** of Gen Z respondents spend less than Rp10,000 on buying or making a cup of coffee. Snippet: "a JakPat survey reveals that the majority (48%) of Indonesian Gen Z respondents spend less than Rp10,000 on buying or making a cup of coffee."
- Note: the search summary says "majority (48%)", which is not a majority. The value 48% is the literal figure; the wording is the republisher's.
- Second independent source: none found. Provisional until a verifier confirms it.

### P1-C3-S2: Mall visitors' main activity (Katadata Insight Center and tSurvey)
- Title: "Mall-visiting Behavior of Indonesian Respondents in Early 2025" (Databoks)
- Publisher: Katadata Insight Center and tSurvey, republished by Databoks
- URL: https://databoks.katadata.co.id/en/consumer-services/statistics/68786fdf28828/mall-visiting-behavior-of-indonesian-respondents-in-early-2025
- Publication date: 2025-07-17 (per search summary)
- Fieldwork: Jan–Apr 2025, online; 266 of 800 respondents; 71% male; upscale and mid-range malls in Jabodetabek; non-probability sampling
- Access date: 2026-10-16
- Proposed tier: 3 (industry study via a republisher; sampling is non-probability, so it is weak)
- Access status: snippet-only (not opened)
- Search query: "Databoks mall visitors Katadata Insight Center tSurvey 2025 restaurant cafe 68% Jabodetabek"
- Figure and exact snippet: **68%**. Snippet: "Dining at restaurants or cafes was the most common activity, reported by 68% of respondents at the beginning of the year."
- Note: this measures participation in one visit type, not visit frequency or spend.

### P1-C3-S3: Young Indonesians' eat-out occasions (Jakpat via Databoks)
- Title: "How Often Do Young Indonesians Eat Out? Here's the 2025 Survey" (Databoks)
- Publisher: Jakpat, republished by Katadata Databoks
- URL: https://databoks.katadata.co.id/en/consumer-services/statistics/690475fe722ca/how-often-do-young-indonesians-eat-out-heres-the-2025-survey
- Publication date: 2025-10-31 (per a related Databoks article dated 31 Oct 2025 in the search results; **not confirmed to be this article**. Verifier must open the page and check the date.)
- Fieldwork: 2–7 Sep 2025, online Jakpat app; 955 respondents, 769 frequent diners; 8 urban cities on Java (Bogor, Depok, Bandung, Yogyakarta, Surakarta, Semarang, Malang, Surabaya); Jakarta not separated; age 15–19 (36%), 20–25 (64%)
- Access date: 2026-10-16
- Proposed tier: 3 (vendor panel via a republisher). Age mismatch with the 25–39 target.
- Access status: snippet-only (not opened)
- Search queries: "How Often Do Young Indonesians Eat Out Databoks 2025 survey lunch dinner percent"; "Databoks what Indonesians consider when eating out price taste survey 2025 date"
- Figures and exact snippets:
  - **41%** dinner (both Databoks pieces agree). Snippet: "the majority of young Indonesians tend to eat out for lunch and dinner, at 23% and 41% respectively."
  - **23%** lunch (conflicting value; see below). Same snippet as above.
- Conflict: a second Databoks piece on the same Jakpat report gives **37%** lunch and 41% dinner. Its publication date is not shown, so the 37% is excluded. The 23% is staged with the conflict noted. The registrar should not pick one value without opening the source.

### P1-C3-S4: Jakarta per-capita spend 2025 (BPS Susenas via Databoks)
- Title: "Pengeluaran per Kapita DKI Jakarta 2025: Kenaikan Jadi Rp2,96 Juta per Bulan" (Databoks)
- Primary publisher: BPS (Badan Pusat Statistik), Susenas March 2025; republished by Katadata Databoks
- URL (republisher): https://databoks.katadata.co.id/datapublish/2026/08/28/pengeluaran-per-kapita-dki-jakarta
- Primary URL to confirm: https://jakarta.bps.go.id (BPS DKI Jakarta; not reached)
- Publication date: 2026-08-28 (taken from the Databoks URL path; the verifier must confirm it on the page)
- Access date: 2026-10-16
- Proposed tier: 1 (BPS primary figures). Cite BPS, not Databoks.
- Access status: snippet-only (not opened)
- Search query: "Indonesia BPS pengeluaran makanan jadi kopi restoran per kapita Jakarta 2025 persen"
- Figures and exact snippets:
  - **Rp2.96 million** per capita per month, 2025, DKI Jakarta. Snippet (title): "Pengeluaran per Kapita DKI Jakarta 2025: Kenaikan Jadi Rp2,96 Juta per Bulan". Search summary: "sekitar Rp2,96 juta pada 2025, naik sekitar 6% dari 2024."
  - **38.93%** food share of per-capita spend, DKI Jakarta, 2025. Snippet: "Porsi makanan tercatat sekitar 38,93%".
- Note: all consumption, all ages, per capita. It is not café or restaurant spend. Used only as a context ceiling.

## Excluded (not in CSV): figures found but not staged

Each item below failed the rule (no publication date, tier 4, or wrong population). They are kept so the registrar can pick them up once a date or primary is found.

| # | Figure (exact snippet) | Source and reason excluded | Priority to date |
| --- | --- | --- | --- |
| E1 | "64% of our respondents who often go to a restaurant less than once in a month"; "30% go one to five times a month"; "48% of our respondents spend about IDR 50,000 to IDR 100,000 every time they visit a restaurant, while 32% of them spend more than IDR 100,000, and 19% of them spend less than IDR 50,000" | Jakpat "At the Restaurant: Survey Report on Indonesian Millennials Restaurant Habit", n=1,623, smartphone users aged 18–36, national. **No publication date shown** ("likely older than 2 years"). | **Highest.** Most direct frequency and ticket data for H5 and H3, and it disconfirms both. Find the date. |
| E2 | "Cost ranked first, picked by 60% of respondents"; "food taste 59%"; "service (44%)"; "cleanliness (43%)"; "Portion size (43%), location (42%)" | Databoks "What Indonesians consider when eating out" (Jakpat, fieldwork 2–7 Sep 2025, n=769 frequent diners, 8 Java cities). **Publication date not shown.** | **High.** Price criteria (Q5). Date needed. |
| E3 | "31% of respondents ... 1–2 times a week"; "22% not consuming coffee" | Jakpat Gen Z coffee (Dec 2024 fieldwork, n=1,155). **Publication date not shown.** | High (frequency). |
| E4 | "35%" cafe coffee vs "57%" instant coffee (Gen Z preference) | Same Jakpat Gen Z survey, Dec 2024. **Publication date not shown.** | Medium. |
| E5 | "43.23%" answered less than once a week; "32.34% ... more than 3 times a week" | Jakpat older coffee study (n=303, aged 20–35, 10 cities). **Undated**; not split by generation. | Low (old, likely pre-window). |
| E6 | "54%" of online drink orders were coffee-based beverages (March 2025, n=1,343) | Databoks, Jakpat March 2025 survey. **Publication date not shown.** | Medium. |
| E7 | "an average cost of a cup at about Rp13,000"; Gen Z spends more than other generations | Separate Jakpat report, n=1,008 respondents across generations. **Date not shown.** | Medium. |
| E8 | "Rp4.83 juta" food spend and "Rp11,97 juta" total spend per month for Gen Z in Jakarta, 2025 | CNA Indonesia, citing BPS. **Publication date and unit (per capita vs household) not confirmed.** Tier 3 media, citing BPS. | High once the BPS primary is found. |
| E9 | "Pengeluaran per Kapita Kota Jakarta Selatan 2025: Lonjakan Jadi Rp4,08 Juta per Bulan" | Databoks, BPS data for South Jakarta. **Date not shown** in the search result. | Medium (catchment context). |
| E10 | "37%" lunch (conflicting value, see P1-C3-S3) | Databoks second piece on the same Jakpat survey. **Date not shown.** | Medium (conflict). |
| E11 | "31% eat out 2 to 3 times a week and 9% once a month" | Snapcart. **Tier 4** (method unclear, not a recognised survey publisher). | Not usable as a figure. |
| E12 | "Respondents drink coffee 2–3 times per week" (search summary wording) | Academic study, Surakarta (not Jakarta), n=30, date not shown. Indicative only. | Not usable for Jakarta. |
| E13 | "Pengeluaran ... Kota Jakarta Selatan" food share 34.96% | Databoks. Date not shown. | Low. |
| E14 | "Bain e-Conomy SEA 2025: food delivery GMV about $23 billion in 2025 (regional)" | Bain / Google / Temasek press release, 2025-11-11 (per search summary). **Regional SEA, no Indonesia split** found. Out of scope for consumer frequency (goes to Q6 delivery share). | Refer to Plan 1 Q6 owner. |

Also excluded: the Databoks "Indonesian coffee consumption preferences in 2025" article (publication 2025-07-07 per byline). It states that instant coffee is preferred, with **no value** in the search result, so there is no figure to stage.

## Disconfirming and conflicting evidence (for the hypothesis review)

- **Low frequency (H5 disconfirmed, not staged):** E1 (Jakpat millennials) shows 64% visiting a restaurant less than once a month and 30% one to five times a month. If it is dated before 2026, it counts strongly against weekly visits for the core. This is the most important gap.
- **Low ticket (H3 disconfirmed, not staged):** E1 shows 48% spending IDR 50,000–100,000 per visit and 19% under IDR 50,000. The planned IDR 85–110k bowl sits in the top band. E1 is a restaurant survey of all restaurants, not cafés.
- **Price ceiling for coffee (H4, mixed):** P1-C3-S1 shows 48% of Gen Z spending under Rp10,000 per cup (bought or made). This is a national figure for home-made and bought coffee, not café price. It disconfirms a premium cup price for the mass segment.
- **Lunch vs dinner (H6, mixed):** P1-C3-S3 shows dinner 41% and lunch 23%, or lunch 37% in the other source. The lunch share is conflicting, so H6's "lunch + evening ≥ 65%" test cannot be decided. Dinner dominance is consistent across both pieces.
- **Dining as a common activity (supporting, weak):** P1-C3-S2 shows 68% of a mall sample naming dining as their main activity. Non-probability sample, 71% male, Jabodetabek malls.

## Gaps (not found in any search result)

- **Age 25–39 split:** no staged source reports eating-out frequency, spend or café visits for 25–39 separately. Every age cut found is 15–25 (Jakpat/Databoks) or 18–36 (Jakpat millennials, undated). The age-fit codes are D for every staged row.
- **Jakarta café frequency and ticket size:** not found in an open, dated, tier 1–3 source. The Indonesian-language search returned no survey on café visits per month in Jakarta.
- **BPS Jakarta consumption pattern (2025):** the BPS publication page is listed (published 2026-05-26) but the food share and prepared-food breakdown were not in the search text. Needs opening.
- **IPB / UI / academic 2024–2026 papers on Jakarta eating out:** not searched in this run (only one Surakarta academic study surfaced). Not in scope for the snippet route without a dated result.
- **Price criteria with dates:** E2 is the only price-criteria source, and it is undated.
- **Indonesia food-delivery split:** e-Conomy SEA 2025 gives a regional figure only (E14).

## Problems

- Source hosts blocked: WebFetch failed on `insight.jakpat.net` (ENOTFOUND). Databoks, BPS and Bain were reached only through search summaries, so none of the figures are opened.
- Most candidate figures lack a publication date in the search result, so most candidate figures were excluded (see the Excluded table).
- The Databoks "How often do young Indonesians eat out" date (2025-10-31) is inferred from a related article in the search result, not confirmed.
- The Databoks "48% majority" wording is the republisher's, and 48% is not a majority. Recorded as the figure, flagged.
