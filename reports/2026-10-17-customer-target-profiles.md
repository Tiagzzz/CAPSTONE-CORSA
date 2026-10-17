# Customer target profiles: who CORSA should serve first in Jakarta, tested against verified rows

Date: 2026-10-17. Task: W-PROF (run 4, Pillar 1, `tasks/2026-10-17-run4-plan-pillar1.md`). Status: DRAFT for Team A; the team decides the final wording. Starting point: Tiago Reimann's six segment scores (`research/internal/corsa-jakarta-target-customer-condensed-v1.md`, 8 October 2026, and the scoring sheet in `research/internal/2026-10-08-customer-behaviour-extended-data.md`). Not yet independently verified (V-PROF follows).

**How to read the tags.** Every attribute carries a tag `[row ids; geography-agefit | confidence | status]`.
- Row ids point to `data/processed/plan4-*.csv`, `demand/*.csv`, `price-ladder.csv`, `listed-operators.csv`. `DISC-A<n>` points to row n of table A in `data/raw/2026-10-17-disconfirming-evidence.md`. `no row` means no verified row exists.
- Geography: J Jakarta (kota-level population and spend rows are coded J), J* Jabodetabek scope, U urban Indonesia (the Jakpat September 2025 sample is eight Java cities without Jakarta), N national, P proxy (other markets or categories), ns not stated. Age-fit against the canonical bands (Gen Z 18-28, Younger Millennials 29-35, Older Millennials 36-45, Gen X 46-61): A exact, B canonical band inside the native band, C partial, D no split or no usable overlap (definitions: `data/processed/README.md`).
- Confidence: high = the row measures this attribute for Jakarta or for this group, from an original or official source; med = it measures the attribute but with one gap (relay, proxy geography or age mismatch); low = two or more gaps, or no row.
- Status: evidenced = the row states the fact for Jakarta or for the group itself; proxy = the row is national, urban-Java, another category or another age group; hypothesis = no row, or a team judgement.
- Text starting "Analysis:" is interpretation. Arithmetic done by us is marked "(arithmetic)". Nothing is interpolated or scaled to Jakarta.

## Summary (for the investor reader)

- **Who first.** Evidence supports an order of attention, not a Jakarta customer count. (1) Young urban professionals aged about 25-39 who work or live in central and south Jakarta; (2) affluent upper-middle-class residents of South Jakarta; then, as secondary groups, (3) run and padel communities and (4) lifestyle-driven café-goers, the latter an attitude that cuts across (1) and (2). Students and creators are not customer segments for the launch; expats cannot be assessed because no verified row exists.
- **Evidence limit, stated plainly.** No verified row gives a Jakarta view for the 25-39 age group on any behaviour. Of the 159 distinct CSV rows cited (plus 6 rows of the disconfirming-evidence table), only the population rows (age-fit A) match the age band, and they count residents, not workers. Almost all attitudes and prices are national or urban-Java proxies with no age split; the Jakpat September 2025 survey behind the discovery figures excludes Jakarta. Findings are directional.
- **How many.** South Jakarta has 535,920 residents aged 25-39 and Central Jakarta 244,600 (sum of three five-year bands each, June 2024, arithmetic) [P1C1-S02, P1C1-S03, P1C1-S04; J-A | med | evidenced] [P1C1-P02, P1C1-P03, P1C1-P04; J-A | med | evidenced]. Worker and commuter counts in the brief are not verified.
- **Money.** South Jakarta residents spend IDR 4.08 million per person per month, about 38% above the Jakarta average of 2.96 million (arithmetic) [UE-N01, P1C3-05; J-D | med | evidenced]. The average Jakarta employee earns IDR 5.9 million, only about 3% above the provincial minimum wage of IDR 5,729,876 (arithmetic) [P1C2-23, P1C2-21; J-D | med | proxy].
- **Price is the hard test.** The model's placeholder guest spend (about IDR 100,000 net, about 110,000 with tax) is roughly 1.5 times the average delivery lunch order of Millennials (IDR 65,130) (arithmetic) [P4W9-05; N-C | med | proxy]. Price is the first reason cited for choosing where to eat (60%) and for trying a new place (64%) [UA-N65, UA-N58; U-D | med | proxy].
- **Channels.** Friends and family come first (44%), then TikTok food accounts (40%) [P4W1-R04, P4W1-R05; U-D | med | proxy]. Run and padel communities are large and growing, but no row shows that they change where members buy food.
- **Facts pointing the other way** are listed in their own section: a shrinking middle class, falling real wages for medium- and high-skilled workers, an upper tier that is small and not uniformly spending, price-first and frugal Gen Z, and a North Jakarta that out-spends South Jakarta on prepared food in the 2024 rows.
- **Next.** Five assumptions need a test before the 90-day roadmap commits money (last section): weekly price acceptance, size of the affluent group, community conversion, whether the brand layer adds value beyond taste and price, and discovery routes among Jakarta 25-39s.

| Rank | Profile | Canonical age band | Size evidence | Spend evidence | Main gap | Overall confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Primary 1 | Young urban professionals | 25-39 = top of Gen Z (25-28), Younger Millennials, start of Older Millennials (36-39) | Residents 25-39 counted (A); workers not | Average wage only; no segment spend | No 25-39 Jakarta behaviour row | low to med |
| Primary 2 (conditional) | Affluent upper-middle-class residents | 29-45 assumed (hypothesis) | None for Jakarta; national upper class 1.2 million | Area spend and upper-tier growth rows | Jakarta class share unknown; counter-evidence | low |
| Secondary 3 | Run and padel communities | 21-40 on one platform (partial overlap with Gen Z, Younger and Older Millennials) | Courts, events, clubs counted | F&B add-on about IDR 50,000 per visit | No purchase-influence row; permits | low |
| Secondary 4 | Lifestyle-driven café-goers (overlay) | Gen Z and Millennials (assumed) | Not sized | Stated motives only | Attitude, not a headcount | low |
| Dropped or deferred | Students; creators (as customers); expats; families | n/a | see section 5 | see section 5 | Expats: no rows | n/a |

## 1. Method and limits

Rows with verification VERIFIED-OPENED or CORRECTED-OPENED only. The 19 BLOCKED rows are excluded and named in section 7. Rows with open label flags use the corrected labels from `tasks/2026-10-17-run4-label-fixes.md`: P1C2-03 (upper class, Mandiri Institute classification, Susenas base not printed), P4W9-29 (takeout is not delivery), P4W4-06 (NIQ online adult consumers, Indonesia n not printed), P3PB-27 (Bastian is a European modern menu, not premium Italian), P3PB-06 (geography not stated), UA-N67 (base of the 33% unconfirmed). No new web research was done.

The shared mapping was used only to locate rows; its `segment_use` column is mechanical (no row tagged "expats"; P1C2-07, a 2018 middle-class count, is tagged "fitness; upper-middle"). Appendix C lists the labels of cited rows.

Reference prices from the CORSA model (`data/raw/2026-10-13-corsa-jakarta-financial-model-v0-5.md`, menu sheet) are team placeholders ("ILLUSTRATIVE placeholder menu"), not evidence; they appear only as the thing the market prices are compared against. The model's own benchmark sources (S31, S46) are not verified rows and are not used.

## 2. Testing Tiago's segment scores

**Why we looked.** The brief ranks six segments out of 30 on size, spending power, frequency, fit with CORSA, ease of reach and evidence. The scores are labelled team judgement "to be revalidated". The totals re-add (A 23, B 21, C 21, E 18, D 17, F 16). We tested each criterion against the verified rows.

**Data.** Verdict codes: S supported by rows; P partly supported; U untested (no verified row); X overstated or contradicted. Tiago's score in brackets.

| Criterion | A Young CBD professionals | B Affluent South Jakarta | C Run and padel | D Students | E Expats |
| --- | --- | --- | --- | --- | --- |
| Size | (4) P: residents 25-39 counted; workers not | (3) U: Jakarta share of upper class unknown | (2) P: counts exist, growth high | (4) U: 837,400 students is not a row | (1) U |
| Spending power | (3) P: wage near minimum, real wages falling | (5) P: area average high; Gini 0.435; upper tier mixed | (4) P: court cost high, F&B add-on small | (1) S: price-first, under IDR 10,000 per cup | (5) U |
| Frequency | (4) U: the brief itself lists visit frequency as missing | (3) U | (4) U | (3) P | (3) U |
| Fit with CORSA | (4) U (judgement) | (4) U | (5) U | (3) U | (4) U |
| Easy to reach | (5) U (district-level, no row) | (4) U | (4) P: clubs, events exist; permit risk | (3) U | (3) U |
| Evidence | (3) X: no 25-39 Jakarta row; we would say 2 | (2) S | (2) S | (3) P: Gen Z rows exist but are not students | (2) X: no rows, we would say 0 |

**Reading each verdict.**
- A, size: residents aged 25-39 in South and Central Jakarta total 780,520 (arithmetic) [P1C1-S02, P1C1-S03, P1C1-S04, P1C1-P02, P1C1-P03, P1C1-P04; J-A | med | evidenced]. The brief's 3.3 million formal workers, 0.94 million commuters and 360,000-540,000 desk workers are not in a verified row [no row (Tiago brief); n/a | low | hypothesis].
- A, spending power: Jakarta's average employee wage is IDR 5.9 million against a minimum wage of IDR 5,729,876 [P1C2-23, P1C2-21; J-D | med | proxy]; median real wages of medium- and high-skilled workers fell about 1% and 2% a year over 2018-2025 [P1C2-11; N-D | med | proxy]. The summary line that this group can "afford a premium meal more than once a week" is not tested.
- B, spending power: South Jakarta is first of six DKI cities on per-capita spend at IDR 4.08 million [UE-N01; J-D | med | evidenced]; the brief's "highest in Indonesia" is not supported by any row. Jakarta's expenditure Gini is 0.435, the highest of all provinces [P1C2-28; J-D | med | evidenced], so an area average says little about the affluent minority.
- C: DKI Jakarta has 326 of Indonesia's 947 padel courts, about 34% (arithmetic) [P4W10-01; J-D | med | evidenced] [P4W10-02; N-D | med | evidenced]. The F&B add-on per racquet visit is about IDR 50,000 on top of about IDR 400,000 for the court [P4W10-11; N-D | low | proxy].

**What it means for CORSA.** The ranking A > B = C is neither confirmed nor refuted: five of six criteria for A are untested. Where rows exist, they favour B over C on money (area spend, upper-tier growth) and C over B on observable scale (courts, events). We therefore rank A and B as primary, B conditional on the Jakarta size check, and C as secondary. Students and expats stay out of the core, as the brief also concludes.

**How to continue.** Re-score after the intercept survey (section 8, assumption 1). Tiago's own switch rule stays valid: if under about 1 in 5 CBD workers would pay weekly, shift weight to residents (B) [no row (Tiago brief); n/a | low | hypothesis].

## 3. Price reference used in all profiles

**Why we looked.** Pillar 2 needs to know whether the placeholder prices can work; every profile needs a price-tolerance statement against the same ladder.

**Data.** CORSA model v0.5 prices are net of the 10% restaurant tax (PBJT), placeholders only. Market prices are list prices as printed; tax and service bases differ (Burgreens prices exclude 10% tax and service; most media prices do not state the basis), so the comparison is indicative. Brand concentration is high: pasta references are mostly one brand, bowls are mostly Burgreens (`data/raw/2026-10-17-price-points.md`, section 6, derived).

| Item | CORSA model placeholder (net, IDR) | Verified references (IDR) |
| --- | --- | --- |
| Pasta main | 82,000-135,000; core 89,000-105,000 | Pizza Marzano list 69,000-109,000, one brand, 11 items [P3PB-02, P3PB-09; J-D | med | proxy]; Pepper Lunch teppan pasta about 74,000-81,000 [P3PB-23, P3PB-25; J-D | low | proxy]; kiosk pasta about 20,000-29,000 [P3PB-29, P3PB-32; J-D | low | proxy]; Gior Jakarta mains 100,000-250,000 (range) [P3PB-26; J-D | med | proxy]; Bastian (European modern menu) 155,000-380,000 (range) [P3PB-27; J-D | med | proxy] |
| Espresso, latte | espresso 32,000; latte or flat white 50,000; signature iced 58,000 | Pizza Marzano espresso 30,000, latte 38,000 [P3PB-12, P3PB-14; J-D | med | proxy]; Fore signature lattes 29,000-33,000 [P3PB-41, P3PB-40; J-D | med | proxy]; chain aren lattes about 10,000 (Kopi Tuku) to about 27,000 (Fore), approximate Google Maps and ordering-app prices [P3PB-34, P3PB-36; J-D | low | proxy] |
| Functional drink | matcha or protein shake 55,000; kombucha or ginger shot 48,000 | Burgreens protein shake 52,000, smoothie 45,000-47,000, herbal elixir 27,000-35,000, before 10% tax and service [P3PR-013, P3PR-016, P3PR-019; J-D | med | proxy] |
| Per guest | about 100,000 net (about 110,000 with tax); the brief's bowl range is 85,000-110,000 | Average delivery lunch order: Gen Z 58,609, Millennials 65,130 [P4W9-06; N-B | med | proxy] [P4W9-05; N-C | med | proxy]; typical delivery order under 50,000 for 42%, 50,000-100,000 for 42%, 100,000-150,000 for 11% [SD05, SD06, UD-N05; N-D | med | proxy]; salad bars from 40,000 to 100,000 per person [P3PB-57, P3PB-54; J-D | low | proxy]; SaladStop spend 100,000-200,000 per person at Senayan City [P3PB-59; J-D | low | proxy] |
| Gen Z cup spend | n/a | under 10,000 per cup 48%; 10,000-25,000 per cup 30% (includes home-made) [P1C3-01, UE-N04; N-B | med | proxy] |

Analysis: the placeholder core pasta (89,000-105,000 net) sits at the upper end of the casual-Italian chain list and below the restaurant ranges. The placeholder latte (50,000) is above every listed latte (maximum 38,000) and above both Gen Z cup-spend bands, and the model's per-guest spend is about 1.5 to 1.7 times a typical delivery lunch (arithmetic). Note a mismatch to resolve: the brief prices a bowl (85,000-110,000) while the model and the scope concept price pasta. Promotions shape what people actually pay: 67% check discounts before ordering and 55% name promotions the main reason to use delivery apps [SD02, SD01; N-D | med | proxy]; 70% pay attention to promotions when choosing a restaurant in the app [UD-N02; N-D | low | proxy].

**What it means for CORSA.** A full-price pasta lunch is a premium purchase in every profile except the affluent one. An entry item and a bundle are needed for the others (the brief also proposes this).

**How to continue.** Test three price levels in the intercept survey; scan app prices at 15-20 comparable venues, dine-in preferred; fill the missing pastry and snack references (no verified row).

## 4. The profiles

### 4.1 Primary 1: Young urban professionals (25-39)

**Why we looked.** Scope question: who are the most relevant CORSA customers, and is there a fit with young urban professionals? The brief's top-scoring segment.

**Data.**
- **Who.** Age 25-39: top of Gen Z (25-28), Younger Millennials (29-35), start of Older Millennials (36-39) [no row (Tiago brief); n/a | low | hypothesis]. Occupation: office and desk workers [no row (Tiago brief); n/a | low | hypothesis]. Income: the average Jakarta employee earns IDR 5.9 million a month (August 2025, all sectors and education levels), up only about IDR 100,000 in a year [P1C2-23; J-D | med | proxy]. Spend: prepared food and drink per person per month in South Jakarta IDR 548,413 (2024 round) [P1C1-E02; J-D | med | proxy], DKI Jakarta IDR 524,958 (March 2026) [P1C1-E01; J-D | med | proxy]; the per-person average includes children and the elderly. Confidence in the sentiment of this age: consumer confidence is highest for ages 20-30 (127.9) and lower at 31-40 [P1C2-17; U-C | med | proxy].
- **How many and how concentrated.** 535,920 residents aged 25-39 in South Jakarta (22.7% of its 2.36 million residents, arithmetic) [P1C1-S02, P1C1-S03, P1C1-S04; J-A | med | evidenced] [P1C1-S07; J-D | med | evidenced] and 244,600 in Central Jakarta [P1C1-P02, P1C1-P03, P1C1-P04; J-A | med | evidenced]. These are residents; where they work is unknown. Concentration at SCBD, Senopati and Kuningan level is not in a verified row [no row (Tiago brief); n/a | low | hypothesis]. Competition is dense: 202,983 restaurant and rumah makan establishments in DKI Jakarta in 2024 [P1C4-21; J-D | med | evidenced] and 149 Fore Coffee outlets in Jabodetabek at end 2025 [P3BF-033; U-D | med | evidenced].
- **Occasions.** Lunch and coffee on workdays (hypothesis). Rows: eating out for lunch 37% and dinner 41% among young urban Javanese [P4W7b-06; U-D | low | proxy]; coffee drunk daily by 46%, most often in the afternoon (35%) or after breakfast (34%) [UC-N14; N-D | low | proxy]; 74% of Millennials and 67% of Gen Z drank coffee in the last six months [P4W9-01b, P4W9-01a; N-D | med | proxy]; coffee to focus on work or study 34% [P4W7b-01; N-D | low | proxy]. Fast food is the most-ordered app lunch for Gen Z and Millennials [P4W9-08; N-C | med | proxy]; 56% of Millennials use delivery apps because they are "too lazy to leave the house" [UD-N03; N-C | med | proxy]. The brief's "87% in office on fixed days" is not a verified row [no row (Tiago brief); n/a | low | hypothesis].
- **Discovery and triggers.** First learned of a new place through friends and family 44%, TikTok food accounts 40%, social ads 39%, passing by 35% (multiple answers, Jakarta not in sample) [P4W1-R04, P4W1-R05, P4W1-R06, P4W1-R07; U-D | med | proxy]; good reviews or ratings attract 42% [P4W2b-02; U-D | med | proxy]. Triggers to try a new place: affordable price 64%, unique menu 49%, opening promotions 48%; 40% wait until reviews are in and only 16% come during the grand opening [UA-N58, UA-N59, UA-N60, UA-N61, UA-N64; U-D | med | proxy]. Most-used delivery app: Millennials GoFood 37% and GrabFood 34% [P4W1-R10, UA-N49; N-C | med | proxy]; Gen Z ShopeeFood 39% [P4W1-R11; N-C | med | proxy]. Social platform use differs by wave and is not trended: in 2026, Gen Z most often use TikTok 32.3%, Instagram 30.8%, Facebook 26.9% [UA-N18, UA-N19, UA-N20; N-B | med | proxy]; Millennials TikTok 31.9%, Facebook 31.1%, Instagram 28.7% [UA-N22, UA-N23, UA-N24; N-C | med | proxy].
- **Price tolerance versus the ladder.** The average delivery lunch order is IDR 65,130 for Millennials and 58,609 for Gen Z [P4W9-05; N-C | med | proxy] [P4W9-06; N-B | med | proxy]. A placeholder guest spend of about IDR 100,000 net is about 1.5 times the Millennial figure (arithmetic). One visit at IDR 110,000 with tax is 1.9% of the average monthly wage; four visits a month would be 7.5% (arithmetic, against the all-employee average). 49% of Millennials say they chose a frugal lifestyle and 66% cook at home as a saving strategy (fieldwork March-August 2024, urban Indonesia) [P4W9-18, P4W9-16; U-C | low | proxy]. Analysis: tolerance is medium at best for a full pasta lunch; the entry coffee and lunch-set range matters most here.
- **Concept fit.** Fits: coffee (high use), pasta as a lunch format (flour-based foodservice is growing, with middle-class and Gen Z consumers named as drivers [P1C4-23; N-D | low | proxy]), functional drinks (matcha drunk by 32% of Millennials and 34% of Gen Z [P4W9-03b, P4W9-03a; N-D | med | proxy]; 62% want clearer labels [UB-14; N-D | low | proxy]). Needs adapting: price architecture (entry item, bundle, delivery), health claim kept secondary (65% say healthy nutrition matters more than five years ago, but only 19% would pay 20% more for food with added nutrition, food products not restaurants) [P4W4-04, P4W4-02; N-D | low | proxy]; halal (a plan 2 entry condition); Italian origin and racing identity have no audience row (hypothesis).
- **Location fit (one line for Jonas).** Central and South Jakarta office belts with high lunch traffic (the brief names SCBD, Senopati, Kuningan) suit this profile, because residents aged 25-39 are 535,920 in South and 244,600 in Central Jakarta [P1C1-S02, P1C1-S03, P1C1-S04, P1C1-P02, P1C1-P03, P1C1-P04; J-A | med | proxy]; district-level worker counts are a gap.

ILLUSTRATIVE persona (not evidence, invented): Dewi, 31, works in an office tower in the central business district, takes an iced coffee at the lobby, orders lunch in an app on two days and walks to a lunch spot on the other days, and meets friends on Friday evening.

**What it means for CORSA.** The reach and coffee habit fit; the price and frequency do not yet have support. The concept can serve this group if it offers a lunch price point closer to the app-lunch range and uses friends, reviews and delivery promotions alongside creators.

**How to continue.** Intercept survey at Tier 1 sites (n at least 150-200, quota 18-28 / 29-35 / 36-45): weekly price acceptance, visits per week, last place visited and why. Lunchtime foot counts. Pull district-level worker and commuter statistics from an official source.

### 4.2 Primary 2 (conditional): Affluent upper-middle-class residents of South Jakarta

**Why we looked.** Scope names the upper-middle class; the brief ranks "affluent South Jakarta residents" second, weekend and evening, small and demanding.

**Data.**
- **Who.** Age assumed 29-45 (Younger and Older Millennials) with some Gen X [no row (Tiago brief); n/a | low | hypothesis]. Occupation: managers, professionals, business owners (hypothesis, no row). Income and spend: South Jakarta IDR 4.08 million per person per month against the Jakarta average of 2.96 million [UE-N01, P1C3-05; J-D | med | evidenced]; food is 34.96% of South Jakarta spend (2025) [P1C1-F03; J-D | med | evidenced]. Nationally the "upper class" (above 17 times the poverty line, Mandiri Institute classification) is 1.2 million people, 0.4% of the population, up from 1.1 million [P1C2-03; N-D | med | proxy]; the middle class (3.5-17 times the line) is 46.7 million, 16.6% [P1C2-01; N-D | med | proxy]. The upper class grew its per-capita consumption 6.8% in 2025 against 4.1% for the middle class [P1C2-08; N-D | med | proxy]; upper-group spending rose 5.3% in 2026 to early May against 3.1% in 2025 [P1C2-31; N-D | med | proxy]; BRI estimates the wealthy tier grew 8.0% against 3.5% for the middle class in Q1 2026 [P1C2-26; N-D | low | proxy]; bank accounts above IDR 2 billion grew 15.99% a year to April 2026 [P1C2-27; N-D | med | proxy]. Confidence is highest among households spending above IDR 5 million a month (index 123.5, September 2026) [P1C2-14; U-D | med | proxy], who also saved more (16.9% of income against 14.4% a year earlier) [P1C2-18; U-D | med | proxy].
- **How many and how concentrated.** No Jakarta class distribution is in a verified row; the Jakarta share of the national upper and middle class is unknown (gap) [P1C2-03; N-D | med | proxy]. Inequality is the highest of any province (expenditure Gini 0.435 against 0.368 nationally), so the affluent are a minority inside an average [P1C2-28; J-D | med | evidenced]. South Jakarta has 2.36 million residents [P1C1-S07; J-D | med | evidenced].
- **Occasions.** Weekend brunch, dinner and social visits (hypothesis). Rows: invitations from friends and family are the most significant external factor in mall visits (65%) and 68% name dining as the most common mall activity (Jabodetabek upscale and mid-range malls, 71% male, non-probability) [UE-N06, P1C3-02; J*-D | low | evidenced]; cafés as self-reward 49.1% (middle-class respondents of a café operator's survey) [P4W7b-13; N-D | low | proxy].
- **Discovery and triggers.** Beauty-category proxy: 62% of high-income consumers trust peer reviews over influencers against 33% of lower-income ones (three-country base, cut-offs not printed) [P4W2b-08; P-D | low | proxy]. Google Maps ratings raised trust at two Surakarta restaurants (qualitative) [P4W2b-19; U-D | low | proxy]. Word of mouth leads discovery in general [P4W1-R04; U-D | med | proxy]. Analysis: reviews and recommendations probably matter more than promotions here; no food-specific row.
- **Price tolerance versus the ladder.** Highest in the set. Restaurant references: Gior Jakarta mains IDR 100,000-250,000 [P3PB-26; J-D | med | proxy], Bastian IDR 155,000-380,000 [P3PB-27; J-D | med | proxy], SaladStop spend IDR 100,000-200,000 per person [P3PB-59; J-D | low | proxy]. A placeholder pasta at 89,000-105,000 net sits at the lower to middle end of this range. A per-capita monthly prepared-food spend of IDR 548,413 in South Jakarta means one 110,000 meal equals about 20% of an average resident's monthly prepared-food spend (arithmetic; the average includes everyone) [P1C1-E02; J-D | med | proxy].
- **Concept fit.** Fits: Italian heritage and premium coffee as an occasion product. Needs adapting: local-origin preference (77% prefer local culinary businesses in the Java survey; the item is about cuisine, not foreign brands) [UA-N66; U-D | low | proxy]; halal; a brand without evidence of foreign-brand pull (chain results are mixed: Starbucks licensee loss widened, Pizza Hut operator returned to profit) [Q6-005, Q6-007; N-D | med | proxy].
- **Location fit (one line for Jonas).** South Jakarta residential and mall catchments suit this profile because area spend per person is the highest of the six Jakarta cities in the rows [UE-N01; J-D | med | proxy]; North Jakarta reports a higher 2024 prepared-food spend per person (IDR 556,691 against 548,413) and is worth a check for PIK [P1C1-E04, P1C1-E02; J-D | med | proxy].

ILLUSTRATIVE persona (not evidence, invented): Arief, 41, a senior manager living in South Jakarta, eats out on weekends with his family or friends and picks places from recommendations and map reviews.

**What it means for CORSA.** The group can carry the premium price and the heritage story, but it is small and the evidence shows an upper tier that is not uniformly spending (see "facts pointing the other way"). It is a high-price anchor, not a volume base.

**How to continue.** Find a Jakarta class distribution (BPS Susenas by province); concept-card test with South Jakarta residents; intercept at two mall and two residential sites.

### 4.3 Secondary 3: Run and padel communities

**Why we looked.** Scope names fitness communities; the brief calls community "the engine" for reaching professionals cheaply and ranks it level with the affluent group.

**Data.**
- **Who.** Racquet-sport platform data (Liga.Tennis, about 100,000 users in seven clubs, one operator) show 58.30% of padel participation aged 21-40 [P4W10-10; N-C | low | proxy], and the largest user segment aged 31-40, 57.3% male [P4W10-12; N-C | low | proxy]. Canonical fit: 21-28 (Gen Z), 29-35 (Younger Millennials), 36-40 (Older Millennials); no split. Income is not in any row; the cost of the sport suggests above-average income (hypothesis). Strava users are self-selected and skew affluent (population note of the row) [P4W5-01; N-D | low | proxy].
- **How many and how concentrated.** DKI Jakarta has 326 padel courts of 947 in Indonesia (end 2025) [P4W10-01; J-D | med | evidenced] [P4W10-02; N-D | med | evidenced]; South Jakarta has 34 clubs and 61 more in preparation [P4W10-05, P4W10-06; J-D | med | evidenced]; Greater Jakarta had 95 venues in mid-August 2025 with 89 more confirmed (different unit, not comparable with courts) [P4W10-08; J*-D | low | evidenced]. Court occupancy at the platform's clubs is 75% [P4W10-13; N-D | low | proxy]. Jakarta Running Festival 2025 had 27,300 runners, 70% more than 2024 [P4W5-04, UC-N04; J-D | med | evidenced]; a PIK 2 run had 6,000 participants, 44% from Jakarta, 37% from Bodetabek, 19% from outside [P4W10-17; J-D | low | evidenced]. Strava running clubs in Indonesia grew about six-fold in a year [UC-N02; N-D | low | proxy].
- **Occasions.** After a run or padel session, event days, weekends. Rows: 33% of runners prefer running with others [UC-N01; N-D | low | proxy]; 65% add other exercise to running [UC-N03; N-D | low | proxy]; on-site consumption of about IDR 50,000 per racquet visit [P4W10-11; N-D | low | proxy]; one padel operator calls F&B essential to a venue (single qualitative statement) [P4W10-09; J-D | low | hypothesis].
- **Discovery and triggers.** Clubs, Strava, race events and venues; no row links these to a food purchase decision. Trust in closest people is the leading coffee information source (57%) [UC-N12; N-D | low | proxy].
- **Price tolerance versus the ladder.** A padel visit costs about IDR 400,000 for the court and the average hourly rental in DKI Jakarta is IDR 423,354 [P4W10-11; N-D | low | proxy] [P4W10-07; J-D | med | evidenced]. Observed F&B add-on (about 50,000) is half the placeholder per-guest spend, so an after-session drink and snack fits better than a pasta main: references are Burgreens protein shake 52,000 and smoothies 45,000-47,000 [P3PR-013, P3PR-016; J-D | med | proxy] against placeholder functional drinks at 48,000-55,000 net.
- **Concept fit.** Fits: functional drinks, performance culture, racing heritage as a sport-adjacent story, community as the brand's own model. Needs adapting: portable post-workout items, morning hours, partner-venue formats. Risk: 185 of 397 Jakarta padel sites lack a building permit (March 2026) and two North Jakarta courts were sealed in March 2026 [UC-N07, P4W5-08; J-D | med | evidenced].
- **Location fit (one line for Jonas).** Sports venues and clubs cluster in South Jakarta (34 clubs, 61 more to come), so a South Jakarta site near running routes or padel clubs suits this profile; North Jakarta carries a permit risk [P4W10-05, P4W10-06, P4W5-08; J-D | med | proxy].

ILLUSTRATIVE persona (not evidence, invented): Raka, 29, plays padel twice a week after work and runs with a club on Sunday morning; he picks a drink and a snack afterwards with the group.

**What it means for CORSA.** Scale and growth are real, but the group is a channel and an occasion more than a revenue base, and its spend per visit is small. It fits the Zurich community story.

**How to continue.** Six to eight organiser interviews; two tracked events with sales per participant; ask the platform operators for age mix and the share who consume on site.

### 4.4 Secondary 4: Lifestyle-driven café-goers (overlay across 4.1 and 4.2)

**Why we looked.** Scope names lifestyle-driven consumers and the café-culture premise of the Jakarta rationale. It is an attitude, so it has no headcount and no stand-alone age band.

**Data.**
- **Who.** Gen Z and Millennials who treat cafés as a social place (hypothesis). Rows: coffee as a place to gather with friends 44%, to focus on work or study 34% [UC-N13, P4W7b-01; N-D | low | proxy]; 49.1% spend leisure time in cafés as self-reward (middle-class respondents of a café operator's survey) [P4W7b-13; N-D | low | proxy]; 71% of respondents (majority aged 18-24) prefer buying ready-made coffee at a shop to brewing at home [P4W7b-08; N-C | low | proxy].
- **How many.** Not sized. Cafés and bars are 6% of Indonesian foodservice sales in 2024 against 79% full-service restaurants [P1C4-19; N-D | med | proxy]. Mall visitors who name dining as the most common activity: 68% [P1C3-02; J*-D | low | evidenced].
- **Occasions.** Meeting friends, work or study sessions, self-reward. 
- **Discovery and triggers.** Social proof and queues for viral food (qualitative, Blok M) [P4W2b-23; J-D | low | evidenced]; fear of missing out raises consumptive behaviour in a student sample in Ambon [P4W2b-22; U-D | low | proxy]; but only 7% call themselves early adopters, 52% are need-based shoppers [P4W3-04, P4W3-08; N-D | med | proxy], and pulse chasers who cut spending outnumber those who raised it (39% against 23%) [UB-07, UB-08; N-D | low | proxy].
- **What brings them back.** Tasty menu 83%, comfortable room 78%, good service 70%, clean room 64%, good facilities 45%, aesthetics 27% (café operator's survey of middle-class respondents) [P4W7b-14; N-D | low | proxy]. A Jakarta Gen Z study of five coffee brands finds the café environment's effect on satisfaction not significant, while service and food and beverage quality are significant [P4W7b-15; J-B | med | evidenced].
- **Price tolerance.** Follows the person: see 4.1 and 4.2.
- **Concept fit.** The brand world (racing, community, visual identity) is the part most likely to attract this group, and the rows say it does not by itself bring them back.
- **Location fit (one line for Jonas).** Mall and high-street sites in the same South and Central Jakarta belts as 4.1 and 4.2; no district-level row separates this attitude [P1C3-02; J*-D | low | proxy].

ILLUSTRATIVE persona (not evidence, invented): Nadia, 26, picks cafés she has seen on a friend's feed, stays two hours with a laptop and a friend, and does not return unless the coffee is good.

**What it means for CORSA.** Treat this as a design lens: taste, comfort and service first; atmosphere and heritage second.

**How to continue.** Add dwell-time counts and a "why did you choose this place" item to the intercept survey; concept-card test of the brand layer.

## 5. Groups dropped or deferred, and why

- **Students: deferred, entry-price role only.** National Gen Z is price-first: 48% spend under IDR 10,000 per cup and 47% name price the main factor [P1C3-01, UE-N03; N-B | med | proxy]; 56% of Gen Z choose a frugal lifestyle, 60% use promotions and 54% limit social outings [P4W9-19, P4W9-14, P4W9-15; U-C | low | proxy]. A survey of young Javanese finds students want comfortable seating (75%) and power outlets (53%), a long-stay need that does not match a lunch format (Jakarta not in sample) [P4W7b-05; U-D | low | proxy]. The count of 837,400 Jakarta students in the brief is not a verified row [no row (Tiago brief); n/a | low | hypothesis].
- **Creators: a channel, not a customer segment.** No verified row describes creators as buyers. As a channel: TikTok food accounts rank second for discovery (40%) [P4W1-R05; U-D | med | proxy]; creators rank last of three trust sources in six Southeast Asian markets (1.98 against 2.42 for family and friends) [P4W2b-11; P-D | low | proxy]; 67% bought something because a creator recommended it (same six markets, not food-specific) [P4W2b-12; P-D | low | proxy]; 83% opened an affiliate link but fewer than 40% bought through one in six months [P4W2b-14; N-D | low | proxy]; trust in food vloggers fell after a scandal (n=85, qualitative) [P4W2b-21; N-C | low | proxy]; micro and nano creators hold trust better [P4W2b-06; P-D | low | proxy]. Use creators as paid or ambassador channel inside profiles 4.1 to 4.3 and measure cost per acquisition; no cost data exist (gap).
- **Expats: gap.** No verified row sizes or describes expats in Jakarta. The brief's "about 15,000 foreign workers (2024)" is a Ministry of Manpower figure relayed by GoodStats and is not a row [no row (Tiago brief); n/a | low | hypothesis]. The only expat mention in the rows is a Playtomic remark about Bali padel clubs, a statement about other clubs and not about Jakarta [UC-N06; J-D | low | proxy]. The mapping has no row tagged expats. Continue: official foreign-worker statistics by province and a short expert call; until then do not plan around this group.

## 6. Facts pointing the other way

All verified rows in scope that run against the profiles or the brief are listed. Tags show which profile they touch. Rows marked BLOCKED are excluded (section 7).

| Fact | Row | Touches | Reading |
| --- | --- | --- | --- |
| Middle class fell from 47.9 million (2024) to 46.7 million (2025), 16.6% of the population (Mandiri Institute computation on BPS data). The brief's "57.3 million to 46.7 million" joins a BPS series (57.33 million 2019 to 47.85 million 2024) with this Mandiri series; the two agree at 2024 (47.9 and 47.85) | [P1C2-01, P1C2-05, P1C2-06; N-D | med | proxy] | 4.1, 4.2 | Shrinking base, national only |
| Share of workers earning a middle-class wage 14.5% (2018) to 7.1% (2025); formal wage share among tertiary-educated 74.1% to 67.8% | [P1C2-10, P1C2-12; N-D | med | proxy] | 4.1 | Fewer secure middle incomes |
| Median real wages of medium- and high-skilled workers -1% and -2% a year, 2018-2025 | [P1C2-11; N-D | med | proxy] | 4.1 | Office workers lose purchasing power |
| World Bank: real wages -1.1% a year 2018-2024 on average; middle-skilled employment hollowing out (deck; no consumption link on the slides) | [DISC-A16; N-D | med | proxy] | 4.1 | Same direction |
| Upper-income group spending -0.6% against the period before the June 2026 school holiday (Bank Mandiri chief economist office via Harian Jogja; +2.2% in 2025) | [DISC-A6; N-D | low | proxy] | 4.2 | Upper tier not uniformly spending |
| Ramadan-Lebaran 2026: middle +4.1%, upper +2.6%, Gen Z +4.4%, Millennials +3%, Gen X +1.4% (seasonal window) | [P1C2-32; N-C | med | proxy] | 4.2 | Counter-evidence to "upper leads" |
| Middle-class savings index 100.4 in February 2026, lowest since October 2023; economist view that the middle class stays under pressure in 2026 | [P1C2-33, P1C2-34; N-D | med | proxy] | 4.1, 4.2 | Pressure on the core |
| Consumer confidence mixed: national 116.8 (Jul 2026), 118.5 (Aug), 117.8 (Jun); Jakarta 146.8 (Sep 2026), 3.2 points below August | [DISC-A1, DISC-A2, DISC-A3; N-D | med | proxy] [P1C2-20; J-D | med | evidenced] | all | Confidence is optimistic but wobbling |
| Dining out among top categories cut by Gen X+ (23%); Millennials name takeout and international travel as retrenchment areas (qualitative); 66% of Millennials cook at home to save | [P4W9-28, P4W9-29; N-D | low | proxy] [P4W9-16; U-C | low | proxy] | 4.1 | Eating out is a cut item |
| Gen Z: 56% frugal, 54% limit social outings, 60% use promotions; 48% under IDR 10,000 per cup | [P4W9-19, P4W9-15, P4W9-14; U-C | low | proxy] [P1C3-01; N-B | med | proxy] | 4.4, students | Price-first |
| Nutrition: only 19% would pay 20% more; cost is a barrier for 43%; healthy options hard to find 48% | [P4W4-02, P4W4-06, P4W4-05; N-D | low | proxy] | 4.1 | Health premium capped |
| Friends and family (44%) lead TikTok (40%); price and promotions outrank social media as stated attractors | [P4W1-R04, UA-N58, UA-N60; U-D | med | proxy] | 4.1 | Creators are not the main route |
| Creators last in trust; affiliate links open 83% but buy under 40%; food-vlogger trust fell | [P4W2b-11; P-D | low | proxy] [P4W2b-14; N-D | low | proxy] [P4W2b-21; N-C | low | proxy] | creators | Channel cost unknown |
| Aesthetics ranked last (27%) of six revisit reasons; environment effect not significant for Jakarta Gen Z | [P4W7b-14; N-D | low | proxy] [P4W7b-15; J-B | med | evidenced] | 4.4 | The brand layer may not bring people back |
| Starbucks licensee nine-month sales -2.77% and loss widened (IDR 108.69 billion against 79.13 billion); Pizza Hut operator H1 2026 revenue -4.54% | [DISC-A13, Q6-006, Q6-005; N-D | med | proxy] [P3BF-022; N-D | med | proxy] | 4.2 | Premium foreign comparable under pressure; attribution to demand or boycott unproven |
| Prepared food and drink spend per person: North Jakarta IDR 556,691 above South Jakarta IDR 548,413 (2024 round); Central 513,174 | [P1C1-E04, P1C1-E02, P1C1-E03; J-D | med | proxy] | 4.2 | South Jakarta is not highest on prepared food in 2024 |
| 185 of 397 Jakarta padel sites lack a building permit; two North Jakarta courts sealed | [UC-N07, P4W5-08; J-D | med | evidenced] | 4.3 | Venue partners at risk |

Analysis: none of these rows has a Jakarta-by-age cut. They argue for conservative visit-frequency scenarios and a price entry point, not against the market.

## 7. Excluded BLOCKED rows (named)

These rows are not used. Source: `data/processed/2026-10-pillar1-mapping-excluded.csv`.
- P3B-17: Domino's outlets in Indonesia, 250 (28 June 2026).
- P3BF-030: ENAK FY2025 and H1 2026 results, gap row.
- P4W4-09: concern about additives and preservatives, 72%.
- P4W4-10: worry about ultra-processed products, 71%.
- P4W4-11: buy less or cheaper because of cost of living, 50%.
- P4W4-12: health goal longer and healthier life, 59%.
- P4W4-13: prioritise reducing stress, 51%.
- Q6-003: FAST management, boycott eased but persists regionally (qualitative).
- Q6-010: share price change of boycott-hit listed firms to 1 December 2025.
- P4W2-05: trust information from influencers, 59.61%.
- P4W2-06: strongly trust influencer information, 6.87%.
- P4W2-07: influencers significantly affect purchases, nearly 4 in 10.
- SD03: discounts top reason for choosing a delivery brand, 36%.
- SD04: low delivery cost as brand-choice reason, 28%.
- SD09: Indonesia food delivery GMV 2025, USD 6.4 billion.
- SD10: Grab share of food-delivery GMV, 46%.
- SD21: consumers more concerned about cost of living, buying less or cheaper, 50%.
- SD22: plan to buy cheaper alternatives, 63%.
- SD23: plan meals ahead to reduce impulse spending, 56%.

Also excluded as BLOCKED in the disconfirming table: row 5 (middle-class savings headline, February 2026), row 8 (eating out among the most-cut items, September-October 2026, anecdotal) and row 15 (Fore Coffee price band, conflicting ranges). Row 8 would have strengthened the section above; it stays out until opened. P4W4-11, SD21 and SD22 also point the same way.

## 8. The assumptions most needing a test

Input for the 90-day roadmap and the primary-research brief. Current evidence is in the profiles; the test column is what to run.

1. **Weekly price acceptance of the 25-39 core (profile 4.1).** Assumption: a meaningful share will pay about IDR 100,000 net (110,000 with tax) for a full CORSA visit at least weekly, or will trade up from a 58,000-65,000 delivery lunch. Evidence: only app-lunch averages and price-first stated drivers; visit frequency "missing" [P4W9-05; N-C | med | proxy] [UA-N65; U-D | med | proxy]. Change of course: under about 1 in 5 paying weekly means shifting toward residents or lowering the price architecture. Test: intercept survey (n at least 150-200) with three price levels, plus lunchtime foot counts at Tier 1 sites.
2. **Size and spending of the affluent group in Jakarta (profile 4.2).** Assumption: enough upper-middle-class households live within reach of a South Jakarta site and keep spending. Evidence: area spend average and national upper-tier growth, against a 0.4% national upper class and a -0.6% holiday reading [UE-N01; J-D | med | evidenced] [P1C2-03, DISC-A6; N-D | low | proxy]. Test: Jakarta class distribution from BPS, concept-card test with South Jakarta residents.
3. **Community converts into purchases (profile 4.3).** Assumption: run and padel members buy CORSA food and drink after sessions and bring friends. Evidence: scale and a 21-40 age share on one platform; F&B add-on about IDR 50,000; no purchase-influence row [P4W10-10; N-C | low | proxy] [P4W10-11; N-D | low | proxy]. Test: organiser interviews and two tracked events with sales per participant; check padel venue permits first.
4. **The brand layer adds value beyond taste and price.** Assumption: Italian racing heritage and the healthy-performance story lift visits and price tolerance. Evidence: none for racing or Italian origin; taste, price and comfort lead stated drivers; aesthetics rank last [P4W7b-14; N-D | low | proxy] [P4W7b-15; J-B | med | evidenced]. Test: concept-card test with spontaneous associations and perceived foreign ownership.
5. **Discovery routes among Jakarta 25-39s.** Assumption: friends, reviews and social video bring first visits, creators are one of several routes. Evidence: Java cities without Jakarta, no age split [P4W1-R04, P4W1-R05; U-D | med | proxy]. Test: add a "how did you hear" item to the same intercept survey; short interviews with local F&B creators on fees and conversion.

## Appendix A: register id, period and base of each cited row

Format: register id; reference period; base; rows covered. Generated from the CSVs by script (165 distinct rows incl. table-A rows).

- **BEH-003**; Fieldwork 13-14 Mar 2025; 1,343 (MoE <5%; sample 52% male/48% female; Gen X 12%, Millennials 46%: UA-N49
- **BEH-003**; Fieldwork 13-14 Mar 2025 (Jakpat article 2025-04-15; Databoks 2025-07-28); 1343 total; Gen Z is 42% of the sample: P4W1-R11
- **BEH-003**; Fieldwork 13-14 Mar 2025 (Jakpat article 2025-04-15; Databoks 2025-07-28); 1343 total; Millennials are 46% of the sample: P4W1-R10
- **BEH-004;BEH-040**; Fieldwork 2-7 Sep 2025 (Jakpat article 2025-10-13; GoodStats chart page 2025-10-23); 995 (MoE <5%): P4W1-R04, P4W1-R05, P4W1-R06, P4W1-R07
- **BEH-005**; impact.com x Cube 2025 edition; trade-press article 2025-07-30; Over 2,400 respondents in six SEA markets; Indonesia n not given: P4W2b-06
- **BEH-006**; impact.com x Cube x Dentsu 2026 edition; Pasardana article 2026-07-27; 2,400 consumers, six SEA markets (Indonesia n not given): P4W2b-11, P4W2b-12
- **BEH-010**; Sep 2024; not given: UB-08
- **BEH-010**; Sep 2024 (pub. 2024-11-06); not given (adults n=2,136): UB-07
- **BEH-010**; September 2024 (published 2024-11-06; the 26-30 Sep dates are not on the page); 2136 adults 18+: P4W3-08
- **BEH-010**; September 2024 (published 2024-11-06; the 26-30 Sep dates are not on the page); 2136 adults 18+ (subgroup base not given): P4W3-04
- **BEH-013**; 2025 survey (release 2025-07-08); not seen: P4W4-02, P4W4-04, P4W4-05
- **BEH-013**; Fieldwork Jan-Feb 2025; release 2025-07-08; not seen: P4W4-06
- **BEH-013**; Jan-Feb 2025; not seen: UB-14
- **BEH-016**; Jul-Sep 2025; n/a: UC-N01
- **BEH-016**; Mid-Year Year in Sport 2025 vs 2024; n/a: UC-N02
- **BEH-016;BEH-041**; Jul-Sep 2025 (IndoTelko 2025-10-23; Gizmologi 2025-10-25; GoodStats 2025-10-27); not published: P4W5-01
- **BEH-017**; Oct 2025 (25-26 Oct); 27300 runners (organiser figure): P4W5-04
- **BEH-017**; Oct 2025 vs Oct 2024; n/a: UC-N04
- **BEH-030**; Survey mid-2025 (Jakpat page printed 2025-07-04); 1,002: P4W7b-01
- **BEH-030**; mid-2025; 1002: UC-N12, UC-N13, UC-N14
- **BEH-038**; 2026; 8,700 (MoE +-1.1%): UA-N18, UA-N19, UA-N20, UA-N22, UA-N23, UA-N24
- **BEH-039**; early 2025; 1343: UD-N02
- **BEH-039**; early 2025; 1343 (total; generation base not stated): UD-N03
- **BEH-039;BEH-032**; Fieldwork 13-14 Mar 2025 (Jakpat article 2025-04-15); 1343: SD01
- **BEH-039;BEH-032**; Fieldwork 13-14 Mar 2025 (Jakpat article 2025-04-15); 1343 (survey total): SD02
- **BEH-040**; Fieldwork 2-7 Sep 2025; 995 (Jakpat, 2-7 Sep 2025; young respondents): UA-N58, UA-N59, UA-N60, UA-N61, UA-N64, UA-N65, UA-N66
- **BEH-040**; Fieldwork 2-7 Sep 2025 (Jakpat article printed 2025-10-13); 995: P4W7b-06
- **BEH-040**; Fieldwork 2-7 Sep 2025 (Jakpat article printed 2025-10-13); 995 (subgroup sizes not shown): P4W7b-05
- **BEH-041**; Jul-Sep 2025; n/a: UC-N03
- **BEH-042**; 2024/25; n/a: UC-N06
- **BEH-043;BEH-044;BEH-019**; 4 Mar 2026 (reports 2026-03-05 and 2026-03-06); 2: P4W5-08
- **BEH-044;BEH-019**; Mar 2026; 397: UC-N07
- **BEH-048;BEH-049;DEM-025;BEH-022**; Jan-Sep 2025 (filing 2025-10-31; CNBC 2025-11-05); not stated: Q6-006
- **BEH-048;BEH-049;DEM-025;BEH-022**; Jan-Sep 2025 vs Jan-Sep 2024 (nine months; CNBC 2025-11-05; Kompas 2025-11-06; filing 2025; not stated: Q6-005
- **BEH-052;BEH-053;BEH-054;BEH-023**; FY2025 vs FY2024 (Detik 2026-04-21; Kontan 2026-05-05); not stated: Q6-007
- **BEH-059**; Jan 2025; 4857: UD-N05
- **BEH-059;BEH-033**; Jan 2025 (Snapcart fieldwork; Databoks 2025-02-14); 4857: SD05, SD06
- **BEH-065**; GoodStats survey released October 2024; 1,000: P4W7b-08
- **BEH-066**; Survey 14-19 Oct 2025 (GoodStats article printed 2025-11-04); 932: P4W7b-13, P4W7b-14
- **BEH-067**; Peer-reviewed article, Vol. 19 No. 1, February 2026 (fieldwork dates not stated in abstrac; 500: P4W7b-15
- **BEH-071**; Fieldwork 2-7 Sep 2025; GoodStats article 2025-11-24; 769 (this article; other GoodStats/Jakpat pieces and rows P4W1-R04 to : P4W2b-02
- **BEH-072**; YouGov report (makeup category); trade-press article 2025-04-23; Over 6,000 consumers in three countries; group n and income cut-offs n: P4W2b-08
- **BEH-074**; Jakpat e-commerce trends 2H 2025 follow-up; article 2026-07-13; 1,714 (article and linked Jakpat report page both print 1714): P4W2b-14
- **BEH-077**; Published 2026-01-30 (journal issue Jan 2026); data collection date not checked; 400: P4W2b-19
- **BEH-079**; Published 2025-06-16 (Vol. 3 No. 4, Apr-Jun 2025); 85: P4W2b-21
- **BEH-080**; Published 2025-06-05 (Manis Vol. 8 No. 2, 2025); 140: P4W2b-22
- **BEH-081**; Article 2025-12-08; n/a: P4W2b-23
- **BEH-082**; fieldwork 22-24 Apr 2026 (consumed in the last six months); GoodStats Data printed 27 Jun ; 1,238 total (42% Gen Z, 44% Millennials, 14% Gen X); per-generation n : P4W9-01a, P4W9-01b, P4W9-03a, P4W9-03b
- **BEH-083**; fieldwork 13-14 Mar 2025; GoodStats printed 17 Apr 2025; 1,343 total (Millennials 46%, Gen Z 42%, Gen X 12%, mostly workers); p: P4W9-05, P4W9-06
- **BEH-083**; fieldwork 13-14 Mar 2025; GoodStats printed 17 Apr 2025; 1,343 total; per-generation n not printed: P4W9-08
- **BEH-086**; fieldwork Mar-Aug 2024 (profile slide: May 2024); GoodStats upload 27 Aug 2025; PDF Creati; 750 per generation (1,500 total); Jabodetabek 20% of each sample: P4W9-14, P4W9-15, P4W9-16, P4W9-18, P4W9-19
- **BEH-088**; fieldwork 17-21 Apr 2025; Marketing-Interactive printed 23 Jun 2025 (relay); 2,067 adults 18+ (per-generation n not printed): P4W9-28, P4W9-29
- **BEH-091**; end-2025 (stock); not published: P4W10-01
- **BEH-092**; 2025 (stock); not published: P4W10-05, P4W10-06
- **BEH-093**; end-2025 (stock); not published: P4W10-02
- **BEH-094**; 2025; not published: P4W10-07
- **BEH-095**; 2025; nearly 100,000 users in seven clubs: P4W10-13
- **BEH-095**; 2025 (Liga.Tennis platform data); nearly 100,000 users in seven clubs: P4W10-11
- **BEH-095**; 2025 (Liga.Tennis platform data); nearly 100,000 users in seven clubs (Liga.Tennis, all racquet sports): P4W10-10
- **BEH-096**; 2025 (Liga.Tennis platform data); nearly 100,000 users in seven clubs: P4W10-12
- **BEH-097**; Sep 2025; n=1 operator (WePadl, Pondok Indah): P4W10-09
- **BEH-097**; mid-August 2025 (stock); not published: P4W10-08
- **BEH-099**; 5 Oct 2025 (event); 6000: P4W10-17
- **CMP-010**; Jan-Jun 2026 vs Jan-Jun 2025 (six months); n/a: P3BF-022
- **CMP-014**; 31 Dec 2025; n/a: P3BF-033
- **CMP-052**; Menu PDF seen 2026-10-17; PDF metadata creation date 2025-08-19 (not printed on pages); pe; n/a: P3PR-013, P3PR-016, P3PR-019
- **CMP-054**; Article printed 17 Nov 2025, 11:20 WIB; price as of article date, period type: point-in-ti; n/a: P3PB-02, P3PB-09, P3PB-12, P3PB-14
- **CMP-056**; Article printed 16 Jul 2025, 13:28 WIB; price as of article date, period type: point-in-ti; n/a: P3PB-23, P3PB-25
- **CMP-057**; Article printed Selasa, 28 Okt 2025 12:00 WIB; price as of article date, period type: poin; n/a: P3PB-26, P3PB-27
- **CMP-058**; Article printed Rabu, 22 Jan 2025 17:00 WIB; price as of article date, period type: point-; n/a: P3PB-29, P3PB-32
- **CMP-059**; Article printed Diperbarui 20 April 2025, 15:41 WIB (updated-date, not original publicatio; n/a: P3PB-34, P3PB-36
- **CMP-060**; Article printed 19 Nov 2025, 11:50 WIB; price as of article date, period type: point-in-ti; n/a: P3PB-40, P3PB-41
- **CMP-063**; Article printed 24 Apr 2025, 19:50 WIB; price as of article date, period type: point-in-ti; n/a: P3PB-54, P3PB-57
- **CMP-065**; Article printed Diterbitkan 01 Oktober 2025, 15:00 WIB; price as of article date, period t; n/a: P3PB-59
- **DEM-001**; Fieldwork 6-9 Dec 2024; 896: UE-N03, UE-N04
- **DEM-001**; Fieldwork 6-9 Dec 2024; 896 coffee consumers (of 1,150 respondents): P1C3-01
- **DEM-002**; Jan-Apr 2025; 266: UE-N06
- **DEM-002**; Jan-Apr 2025; 266 (of 800 respondents): P1C3-02
- **DEM-004**; 2025 (Susenas, BPS; March round not named on page); Databoks page last updated 2026-07-19; not reported: P1C3-05
- **DEM-020**; 2025 (BPS Susenas); not reported: UE-N01
- **DEM-020**; 2025 (Susenas, annual figure as printed by Databoks); n/a (Susenas): P1C1-F03
- **DEM-021**; February 2026; Bank Mandiri deposit customers (middle = savings Rp1-10 million): P1C2-33
- **DEM-028**; June 2024 (as printed by Databoks, citing BPS); n/a (full population): P1C1-P02, P1C1-P03, P1C1-P04
- **DEM-029**; 2024 (as printed by Databoks, citing BPS); n/a: P1C1-S07
- **DEM-029**; June 2024 (as printed by Databoks, citing BPS); n/a (full population): P1C1-S02, P1C1-S03, P1C1-S04
- **DEM-030**; 2024 (Susenas, annual figure as printed by Databoks); n/a (Susenas): P1C1-E02, P1C1-E03, P1C1-E04
- **DEM-031**; March 2026 Susenas (BPS report "Pengeluaran untuk Konsumsi Penduduk Indonesia Maret 2026",; n/a (Susenas): P1C1-E01
- **DEM-034**; September 2026; about 4,600 households, 18 cities: P1C2-17
- **DEM-034**; September 2026 (monthly survey); about 4,600 households, 18 cities, stratified random sample: P1C2-14
- **DEM-034**; September 2026 (monthly); Jakarta households within the 4,600 sample (city n not stated): P1C2-20
- **DEM-034**; September 2026 vs September 2025 (monthly); about 4,600 households; >Rp5 juta class: P1C2-18
- **DEM-035**; calendar year 2025 vs 2024; national population (BPS Susenas data as classified by Mandiri Institu: P1C2-03
- **DEM-035**; calendar year 2025 vs 2024; national population (Susenas): P1C2-08
- **DEM-035**; calendar year 2025 vs 2024 (Susenas, annual); national population (Susenas): P1C2-01
- **DEM-037**; 2024 (Susenas March 2024); Kontan prints 2021 in error (it also prints 17.1% for 2024 and ; national population: P1C2-06
- **DEM-037**; calendar year 2019; national population: P1C2-05
- **DEM-038**; statement dated 2026-05-27; n/a: P1C2-34
- **DEM-039**; 2018 to 2025; employed persons: P1C2-11
- **DEM-039**; 2018 to 2025; tertiary-educated workers: P1C2-12
- **DEM-039**; 2018 to 2025 (annual); employed persons (labour force surveys): P1C2-10
- **DEM-040**; calendar year 2026 (effective 1 Jan 2026); workers with under one year of service: P1C2-21
- **DEM-042**; August 2025 (Sakernas, semester round); Sakernas employees (n not stated): P1C2-23
- **DEM-044**; April 2026; deposit accounts (LPS): P1C2-27
- **DEM-044**; Q1 2026 (quarter); report published July 2026; national, tiers as defined by BRI (not stated in article): P1C2-26
- **DEM-045**; March 2026 (Susenas March round); Susenas households: P1C2-28
- **DEM-047**; 2026 year to 5 May (Mandiri Macro and Market Brief Q2 2026, 11 May 2026); MSI transactions: P1C2-31
- **DEM-048**; Ramadan to Lebaran 2026 (seasonal window, reported 15 Apr 2026); MSI transactions: P1C2-32
- **DEM-060**; Calendar year 2024; n/a: P1C4-19
- **DEM-061**; Report of April 2026, reference period 2025; n/a: P1C4-23
- **DEM-062**; Calendar year 2024 (BPS Statistik Penyediaan Makanan dan Minuman 2024); n/a: P1C4-21
- **DISC table A** (`data/raw/2026-10-17-disconfirming-evidence.md`): DISC-A1, DISC-A13, DISC-A16, DISC-A2, DISC-A3, DISC-A6

## Appendix B: claims of the target-customer brief with no verified row

3.3 million formal workers; 0.94 million daily commuters into South Jakarta; 360,000-540,000 CBD desk workers (team estimate from CBRE floor space); 87% in the office on fixed days; about 15,000 expat workers; 837,400 Jakarta students; Jakarta household size 3.72 (North Jakarta); South Jakarta as "world leader in group runs"; 36 Italian and pasta venues with average rating 4.68. Status: unverified by this report; the cited originals sit outside the verified rows.

## Appendix C: shared-mapping `segment_use` against our assignment

Segment_use label of each cited row as tagged in the mapping (indicative only). Rows labelled only "all" or "upper-middle; lifestyle" etc. were reassigned by content in this report; the label was not used to include or exclude a row.

P1C1-E01 (all); P1C1-E02 (all); P1C1-E03 (all); P1C1-E04 (all); P1C1-F03 (all); P1C1-P02 (young pros); P1C1-P03 (young pros); P1C1-P04 (young pros); P1C1-S02 (young pros); P1C1-S03 (young pros); P1C1-S04 (young pros); P1C1-S07 (young pros); P1C2-01 (upper-middle); P1C2-03 (upper-middle); P1C2-05 (upper-middle); P1C2-06 (upper-middle); P1C2-08 (upper-middle); P1C2-10 (young pros; upper-middle); P1C2-11 (young pros; upper-middle); P1C2-12 (young pros; upper-middle); P1C2-14 (upper-middle); P1C2-17 (upper-middle); P1C2-18 (upper-middle); P1C2-20 (upper-middle); P1C2-21 (upper-middle); P1C2-23 (upper-middle); P1C2-26 (all); P1C2-27 (upper-middle); P1C2-28 (upper-middle); P1C2-31 (upper-middle); P1C2-32 (upper-middle); P1C2-33 (upper-middle); P1C2-34 (upper-middle); P1C3-01 (students; young pros; lifestyle); P1C3-02 (lifestyle); P1C3-05 (lifestyle; upper-middle); P1C4-19 (all); P1C4-21 (lifestyle); P1C4-23 (all); P3BF-022 (all); P3BF-033 (all); P3PB-02 (upper-middle; lifestyle); P3PB-09 (upper-middle; lifestyle); P3PB-12 (upper-middle; lifestyle); P3PB-14 (upper-middle; lifestyle); P3PB-23 (upper-middle; lifestyle); P3PB-25 (upper-middle; lifestyle); P3PB-26 (upper-middle; lifestyle); P3PB-27 (upper-middle; lifestyle); P3PB-29 (upper-middle; lifestyle); P3PB-32 (upper-middle; lifestyle); P3PB-34 (upper-middle; lifestyle); P3PB-36 (upper-middle; lifestyle); P3PB-40 (upper-middle; lifestyle); P3PB-41 (upper-middle; lifestyle); P3PB-54 (upper-middle; lifestyle); P3PB-57 (upper-middle; lifestyle); P3PB-59 (upper-middle; lifestyle); P3PR-013 (upper-middle; lifestyle); P3PR-016 (upper-middle; lifestyle); P3PR-019 (upper-middle; lifestyle); P4W1-R04 (young pros; lifestyle); P4W1-R05 (creators; young pros; lifestyle); P4W1-R06 (young pros; lifestyle); P4W1-R07 (young pros; lifestyle); P4W1-R10 (young pros); P4W1-R11 (students; young pros); P4W10-01 (fitness); P4W10-02 (fitness); P4W10-05 (fitness); P4W10-06 (fitness); P4W10-07 (fitness); P4W10-08 (fitness; lifestyle); P4W10-09 (fitness; lifestyle); P4W10-10 (fitness; lifestyle); P4W10-11 (fitness; upper-middle); P4W10-12 (fitness); P4W10-13 (fitness; lifestyle); P4W10-17 (fitness); P4W2b-02 (lifestyle); P4W2b-06 (creators); P4W2b-08 (creators; upper-middle); P4W2b-11 (creators); P4W2b-12 (creators); P4W2b-14 (creators); P4W2b-19 (lifestyle); P4W2b-21 (creators); P4W2b-22 (students; upper-middle); P4W2b-23 (all); P4W3-04 (all); P4W3-08 (all); P4W4-02 (fitness); P4W4-04 (fitness); P4W4-05 (fitness); P4W4-06 (fitness); P4W5-01 (fitness); P4W5-04 (fitness); P4W5-08 (fitness); P4W7b-01 (young pros; lifestyle); P4W7b-05 (students; young pros; lifestyle); P4W7b-06 (young pros; lifestyle); P4W7b-08 (lifestyle); P4W7b-13 (lifestyle; upper-middle); P4W7b-14 (lifestyle; upper-middle); P4W7b-15 (students; young pros; lifestyle); P4W9-01a (students; young pros; lifestyle); P4W9-01b (young pros; lifestyle); P4W9-03a (students; young pros; lifestyle); P4W9-03b (young pros; lifestyle); P4W9-05 (young pros); P4W9-06 (students; young pros); P4W9-08 (students; young pros; lifestyle); P4W9-14 (students; young pros); P4W9-15 (students; young pros; lifestyle); P4W9-16 (young pros; lifestyle); P4W9-18 (young pros); P4W9-19 (students; young pros); P4W9-28 (lifestyle); P4W9-29 (young pros; lifestyle); Q6-005 (all); Q6-006 (all); Q6-007 (all); SD01 (all); SD02 (all); SD05 (all); SD06 (all); UA-N18 (creators; students; young pros); UA-N19 (students; young pros); UA-N20 (students; young pros); UA-N22 (creators; young pros); UA-N23 (young pros); UA-N24 (young pros); UA-N49 (young pros); UA-N58 (young pros; lifestyle); UA-N59 (young pros; lifestyle); UA-N60 (young pros; lifestyle); UA-N61 (young pros; lifestyle); UA-N64 (young pros; lifestyle); UA-N65 (young pros); UA-N66 (young pros; lifestyle); UB-07 (upper-middle); UB-08 (upper-middle); UB-14 (all); UC-N01 (fitness); UC-N02 (fitness); UC-N03 (fitness); UC-N04 (all); UC-N06 (fitness); UC-N07 (fitness); UC-N12 (lifestyle); UC-N13 (lifestyle); UC-N14 (lifestyle); UD-N02 (lifestyle); UD-N03 (young pros); UD-N05 (upper-middle); UE-N01 (lifestyle; upper-middle); UE-N03 (students; young pros; lifestyle); UE-N04 (students; young pros; lifestyle); UE-N06 (all)
