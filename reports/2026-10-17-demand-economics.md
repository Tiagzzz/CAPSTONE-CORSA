# Demand economics for CORSA Jakarta: target pool, spend, and hypotheses H1-H8

Plan 1 synthesis (Team A). Date: 2026-10-17. Status: DRAFT, awaiting independent verification. Inputs: only VERIFIED-OPENED or CORRECTED-OPENED rows of `data/processed/demand/*.csv` and the disconfirming-evidence table; Plan 4 spend rows and listed-operator rows for cross-reference. No new research.

**How to read this report.** Facts are cited as [row_id; register_id; period; base; geography]. Geography codes: J = Jakarta, U = urban Indonesia, N = national. "Analysis:" marks our reading, not sourced data. "Relay" rows are news or data-portal copies of an unopened original (tier 3). CONFIRMED and DISCONFIRMED apply only when the plan's criterion is met; NOT CONFIRMED means evidence leans against but the criterion is unmet; UNDETERMINED means the data cannot test it.

## 1. Summary

1. **No hypothesis is cleanly confirmed.** H2 leans against the team's view, H7 is mixed, and six cannot be decided with public data (H1, H3, H4, H5, H6, H8; H1 and H8 matter most for the model). The plan's funnel acceptance criterion (low/central/high guests per day against 128 and 200) is not met: class share, frequency and capture rate are GAPs, and we did not build a funnel from assumptions.
2. **The "growing middle class" wording cannot be supported, but a shrinking Jakarta middle class is not shown either.** The national middle class fell from 57.33 million (2019) to 47.85 million (2024) [P1C2-05, P1C2-06; DEM-037; N] and from 47.9 to 46.7 million in 2025 [P1C2-01; DEM-035; N]. No Jakarta class series was found. Jakarta nominal per-capita spend rose 6.01% in DKI and 15.57% in South Jakarta in 2025 [P1C3-05; DEM-004; P1C1-F05; DEM-020; J; not deflated]. The upper tier outgrows the middle in several bank datasets (section 2.3), but the numbers are relays.
3. **H3 is undetermined, and the owner's 4-bowl threshold cannot be tested.** The threshold is the owner's flagged assumption, not a sourced figure, and the model menu has no bowl at the plan's Rp85,000-110,000 (that range is a planner assumption). The only prepared-food figure is one city mean, not an upper-class median (section 5, H3).
4. **H1 and H8 are undetermined.** Residents aged 25-39: 244,600 in Jakarta Pusat and 535,920 in Jakarta Selatan (June 2024, DERIVED) [P1C1-P06, P1C1-S06; DEM-028, DEM-029; J]. The class share and capture rate are GAPs, and no public source gives guests per day for a comparable venue.
5. **Wheat is not shrinking** (USDA food use 9.4 to 9.8 million tonnes) [P1C4-04; DEM-050; N], but restaurant pasta is not separated and 88% of households still consume rice [P1C4-14; DEM-057; N].
6. **Balance check (run 4):** section 2.4 lists all 43 verified downside or mixed rows in scope (20 were cited before, 23 added). No verdict changes; the added rows are national or regional, none is a DKI series.
7. **For Team B:** the UMP input matches its source (Rp5,729,876) and wage growth has a sourced range (6.17-6.5%). Guests per day, visit frequency and dine-in tickets are **GAP**.

## 2. Target pool

### 2.1 Population aged 25-39 (facts)

BPS data as printed by Databoks (relay; the BPS table was not opened). DKI-wide population aged 25-39 is a **GAP**: no DKI-wide row was found. The two city rows below are the only DERIVED rows.

| Row | Age band | Persons | Period | Base | Geography | register_id |
| --- | --- | --- | --- | --- | --- | --- |
| P1C1-P02 | 25-29 | 81,880 | June 2024 | full population | Jakarta Pusat | DEM-028 |
| P1C1-P03 | 30-34 | 81,020 | June 2024 | full population | Jakarta Pusat | DEM-028 |
| P1C1-P04 | 35-39 | 81,700 | June 2024 | full population | Jakarta Pusat | DEM-028 |
| P1C1-P06 (DERIVED) | 25-39 | 244,600 | June 2024 | sum of three bands | Jakarta Pusat | DEM-028 |
| P1C1-S02 | 25-29 | 179,370 | June 2024 | full population | Jakarta Selatan | DEM-029 |
| P1C1-S03 | 30-34 | 178,390 | June 2024 | full population | Jakarta Selatan | DEM-029 |
| P1C1-S04 | 35-39 | 178,160 | June 2024 | full population | Jakarta Selatan | DEM-029 |
| P1C1-S06 (DERIVED) | 25-39 | 535,920 | June 2024 | sum of three bands | Jakarta Selatan | DEM-029 |


Analysis: these are residents of all income classes. They exclude commuters (probably a large part of the lunch trade) and give no district split.

### 2.2 Income, wages and spend levels (facts)

| Indicator | Value | Row; register_id | Period; base; geography |
| --- | --- | --- | --- |
| Total spend per person per month, South Jakarta | Rp4,083,229 (rank 1 of 514 districts) | P1C1-F05; DEM-020 | 2025; per capita; J |
| Total spend per person per month, DKI | Rp2,962,412 (2025); Rp3.07 million (Mar 2026, CNBC relay) | P1C1-F01; DEM-004; P1C1-E01; DEM-031 | 2025 and Mar 2026; per capita; J |
| Food share of spend, DKI | 38.93% (2025); 39.66% (2024) | P1C1-F01, P1C1-F02; DEM-004 | annual; per capita; J |
| Food share of spend, South Jakarta | 34.96% (2025); 38.08% (2024) | P1C1-F03, P1C1-F04; DEM-020 | annual; per capita; J |
| Expenditure Gini, DKI vs national | 0.435 (highest province) vs 0.368 | P1C2-28; DEM-045 | Mar 2026; households; J/N |
| Average monthly wage of employees, Jakarta | Rp5.9 million; national Rp3.33 million | P1C2-23; DEM-042 | Aug 2025; Sakernas employees; J/N |
| UMP DKI | Rp5,729,876 (+6.17%); 2025: Rp5,396,761 (+6.5%) | P1C2-21; DEM-040; P1C2-22; DEM-041 | 2026 and 2025; workers under one year of service; J |
| Consumer Confidence Index, Jakarta | 146.8 (national 118.1) | P1C2-20; DEM-034 | Sep 2026; households in 18-city sample; J |

Analysis: South Jakarta spends 1.4 times the DKI average per head (4,083,229 / 2,962,412, 2025). Its food share fell 3.1 points in a year while total spend rose, so extra income went mostly to non-food items [P1C1-F04 notes]. The Gini and the rank-1 position point to a concentrated top tier that a middle-class headcount understates. The Jakarta wage is an all-sector mean; a Jakarta wage table by education is a GAP.

### 2.3 Middle-class trend (facts)

| Series | Value | Row; register_id | Period; base; geography |
| --- | --- | --- | --- |
| Middle class (BPS) | 57.33 million (21.5%) | P1C2-05; DEM-037 | 2019; population; N |
| Middle class (BPS Susenas) | 47.85 million (17.13%) | P1C2-06; DEM-037 | Mar 2024; population; N |
| Middle class (Mandiri from Susenas) | 47.9 million (2024) to 46.7 million (2025; 16.6%) | P1C2-01; DEM-035 | annual; population; N |
| Upper class (above 17x poverty line) | 1.1 to 1.2 million (0.4%) | P1C2-03; DEM-035 | 2024 to 2025; N |
| Workers on middle-class wages (World Bank) | 14.5% (2018) to 7.1% (2025) | P1C2-10; DEM-039 | annual; employed persons; N |
| Real wage change, medium and high skilled | about -1 and -2% a year, vs +1.7% for low-skilled | P1C2-11; DEM-039 | 2018-2025; N |
| Per-capita consumption growth by class | upper 6.8%, middle 4.1%, national 4.6% | P1C2-08; DEM-035 | 2025 vs 2024; N |
| Growth by tier (BRI) | wealthy 8.0% (estimate), middle 3.5%, lower 3.6% | P1C2-26; DEM-044 | Q1 2026; tiers not defined; N |
| Upper-group spend growth (MSI) | +5.3% yoy vs +3.1% in 2025 | P1C2-31; DEM-047 | 2026 to 5 May; card data; N |

Definitions: middle class is 3.5-17 times the poverty line per person per month, upper class above 17 times [P1C2-04; DEM-036; N]. The 57.33 to 47.85 million fall uses BPS figures relayed by Kontan; the 47.9 to 46.7 million step is Mandiri Institute using the same Susenas data, so these are one underlying source and not two. The plan's "57.3M to 46.7M" combines the BPS 2019 point with the Mandiri 2025 point. 

Counter-evidence: in the 2026 Ramadan to Lebaran window the middle group grew fastest (+4.1% vs upper +2.6%; seasonal) [P1C2-32; DEM-048; N]. Upper-group spending fell 0.6% against the pre-holiday period in the June 2026 school holidays [disconfirming-evidence row 6; DEM-022;DEM-009; N], one outlet.

Analysis: the "growing middle class" claim fails nationally; the 2025 decline of about 2.5% exceeds the rounding of the figures (47.9 vs 46.7). The upper-class change (1.1 to 1.2 million) is within one-decimal rounding and is not growth. Mandiri and BRI both show the upper group outgrowing the middle, but both are relays and national. Wording that survives: "a narrower middle and a concentrated upper tier whose Jakarta size is not measured".

### 2.4 Facts pointing the other way: verified downside and mixed rows (balance check, run 4)

**Selection rule.** A script listed every row of `demand/*.csv`, `plan4-spend-drivers.csv` (spend rows only) and `listed-operators.csv` (operators used for H8) coded VERIFIED-OPENED or CORRECTED-OPENED whose value, notes or direction text matched a decline, loss, slowdown, price-resistance, "disconfirms" or "mixed" marker, plus table A of `data/raw/2026-10-17-disconfirming-evidence.md` rows marked disconfirms or mixed. Each full row (notes, gaps, in-force and amendment columns where present) was then read and kept or dropped. Result: 43 rows (35 CSV rows, 8 disconfirming-table rows). The earlier text cited 20 of them (18 CSV rows, 2 table rows); this section adds the other 23. Excluded as BLOCKED: disconfirming-table rows 5 (middle-class saving headline; the opened replacement is P1C2-33), 8 (eating-out cuts, anecdotal) and 15 (Fore price band, conflicting ranges). Dropped as not downside after reading: UE-N07 (the 2025 layoff base, which makes 2026 layoffs lower), P1C1-C01 (poverty share, no direction), P1C4-10 (a conflict of totals), SD19 and UD-N12 (PayLater arrears falling).

Added rows (all Analysis-free facts; geography N unless stated; relays are tier 3):

| Row | Fact | Period; base | register_id |
| --- | --- | --- | --- |
| Table row 1 (mixed) | Consumer Confidence Index 116.8, optimistic but the expectations index (IEK) was 125.7 and the current-conditions index 107.9, both lower than June [UE-N09] | Jul 2026; national | DEM-005 |
| Table row 2 (mixed) | Index 118.5, up 1.7 points from July (computed) | Aug 2026; national | DEM-006 |
| Table row 3 (mixed) | Index 117.8; the May value of 120.9 is from a regional paper (Harian Jogja), so the fall of 3.1 points is computed | Jun 2026; national | DEM-007 |
| Table row 9 (mixed) | 23,470 workers laid off (JKP participants only; Jan-May 2025: 46,015, so about 49% fewer, computed) [UE-N07] | Jan-May 2026; national | DEM-023; DEM-024; DEM-012 |
| Table row 16 (disconfirms) | Real wages declined 1.1% a year on average (World Bank Dec 2025 deck, 14 slides); the consumption link is not on the slides; updated by P1C2-11 | 2018-2024; national | DEM-018 |
| Table row 17 (mixed) | GDP +5.29% yoy; context only, not segment demand | Q2 2026; national | DEM-027; DEM-019 |
| UE-N08 | 26.9% of households call themselves poor (August 2024: 19.5%) | Aug 2025 monthly point; national | DEM-018 |
| P1C2-02 | Aspiring middle class 142.0 million (2025) vs 137.5 million (2024), 50.4% of population: the pool below the middle grows | 2025 vs 2024; Susenas | DEM-035 |
| P1C2-09 | Middle-class food consumption +0.9% vs non-food +6.4% (2024: food 4.6%, non-food 3.2%); Susenas food group, not restaurants | 2025 vs 2024 | DEM-035 |
| P1C2-12 | Formal wage employment of tertiary-educated workers 74.1% to 67.8% | 2018 to 2025 | DEM-039 |
| P1C2-13 | World Bank: consumption 54% of Q1 growth, but weak job quality and falling real wages "could also constrain household consumption"; Q1 helped by early Eid and stimulus | Q1 2026 | DEM-039 |
| P1C2-14 | Highest expenditure class (above Rp5 million): confidence 123.5 (Sep 2026) vs 124.8 (Sep 2025), slightly down; household bands, 18 cities (U) | Sep 2026 | DEM-034 |
| P1C2-27 | Purchasing-power index April 2026: high income -0.1, middle -0.9, lower -1.0; deposits over Rp2 billion +15.99% vs Rp100-500 million +3.15% (relay of BRI) | Apr 2026 | DEM-044 |
| P1C2-29 | Mandiri card data: restaurants +4.7% yoy vs +6.1% the year before; overall MSI growth 5.5% in September, lowest since Nov 2025; period labels inferred from the paragraph | Q3 2026 (to 27 Sep) | DEM-046 |
| P1C2-30 | Mandiri Saving Index by savings-balance group (not expenditure class): middle 100.5 (-0.1% mom), upper 95.1 vs 94.0; the lower group value is printed two ways and not used | 27 Sep 2026 | DEM-046 |
| P1C2-33 | Middle-group Mandiri saving index 100.4, lowest since Oct 2023 | Feb 2026 | DEM-021 |
| P1C2-34 | LPEM FEB UI: the middle class "masih akan tertekan di 2026" (opinion, tier 3) | statement of 27 May 2026 | DEM-038 |
| SD07 | Delivery average order value "trending down slightly" in Southeast Asia; growth from frequency, not basket size (relay of Momentum Works; region, not Jakarta) | 2025 | BEH-060; BEH-034 |
| P3BF-015 | MAPB net loss Rp121,506 million vs Rp80,206 million | Jan-Jun 2026 vs 2025; unaudited | CMP-006 |
| P3BF-022 | PZZA revenue Rp1.47 trillion vs Rp1.54 trillion (-4.54%), relay | Jan-Jun 2026 vs 2025 | CMP-010 |
| P3BF-028 | ENAK (Champ Resto) loss Rp37.04 billion vs profit Rp19.74 billion | Jan-Sep 2025 vs 2024 | CMP-012 |
| P3BF-029 | ENAK Jabodetabek sales Rp636.0 billion of Rp1.082 trillion, 58.8% (J), down 10.6% on 9M 2024 (computed), the largest regional fall | Jan-Sep 2025 | CMP-012 |

Already cited elsewhere in this report (18 CSV rows): UE-N03, P1C3-01, P1C2-01, -03, -08, -10, -11, -18, -26, -31, -32, P1C1-F04, P1C1-E03, P1C1-E05, P1C4-08, P1C4-11, P3BF-016, P3BF-027; and table rows 6 and 13.

Reading of the added rows. Fact: they lean the same way as the existing section 2.3 and the H2 verdict: weaker national confidence in June and July, falling middle-class savings and food spending, real wages and formal employment down, restaurant card spend slowing, three listed chains with falling sales or losses. Two rows are mixed in the other direction (confidence rose in August; layoffs were about half the 2025 level). Analysis: no verdict changes. No added row is a DKI series (ENAK's Jabodetabek cut is Greater Jakarta), so the Jakarta half of the H2 disconfirmation criterion stays unmet. Row P1C2-30 and P1C2-33 define groups by savings balance and must not be read as the BPS middle class.

## 3. Food away from home and café spend

### 3.1 Prepared-food spend per person

| Geography | Rp per person per month | Row; register_id | Period; base |
| --- | --- | --- | --- |
| DKI Jakarta | 524,958 | P1C1-E01; DEM-031 | Mar 2026 Susenas; per capita |
| Jakarta Selatan | 548,413 (+25% vs 2023) | P1C1-E02; DEM-030 | 2024 annual; per capita |
| Jakarta Pusat | 513,174 (-2.5% vs 2023) | P1C1-E03; DEM-030 | 2024 annual; per capita |
| Jakarta Utara; Jakarta Barat (comparators) | 556,691; 454,710 | P1C1-E04, P1C1-E05; DEM-030 | 2024 annual; per capita |
| Indonesia | 248,501 | P1C1-E06; DEM-032 | Mar 2025; per capita; N |
| Indonesia | 261,543 (32.5% of food spend Rp804,430) | P1C4-17; DEM-059 | Sep 2025; per capita; N |

"Prepared food and drink" covers everything bought ready to eat, from warung to cafés. The café share and per-class values are **GAP**.

Period mismatches: DKI is March 2026, the cities are 2024 annual (Databoks teasers), national is March and September 2025. Cross-row comparisons (DKI vs national, 2.1 times) mix periods and are indicative only. South Jakarta +25% against Pusat -2.5% in the same year is unexplained; treat the 2024 city values with caution.

### 3.2 Coffee, lunch and frequency

| Metric | Value | Row; register_id | Period; base; geography |
| --- | --- | --- | --- |
| Gen Z coffee consumers spending under Rp10,000 per cup (bought or made) | 48% | P1C3-01; DEM-001 | Dec 2024 fieldwork; n=896; N online panel |
| Gen Z coffee drinkers spending Rp10,000-25,000 per cup | 30% | UE-N04; DEM-001 | Dec 2024; n=896; N |
| Price as main factor when buying coffee | 47% | UE-N03; DEM-001 | Dec 2024; n=896; N |
| Average delivery lunch order: Millennials; Gen Z; Gen X | Rp65,130; Rp58,609; Rp63,250 | P4W9-05, P4W9-06, P4W9-07; BEH-083 | 13-14 Mar 2025; n=1,343 delivery-app users; N |
| Delivery order size: under Rp50,000; Rp50,000-100,000; Rp100,000-150,000 | 42%; 42%; 11% | SD05, SD06, UD-N05; BEH-059 | Jan 2025; n=4,857; N |
| Usually eat out for dinner; lunch | 41%; 37% | P1C3-03, P1C3-04; DEM-003 | Sep 2025; n=769 (base conflict 955/995); age 15-25, eight Java cities, Jakarta not separated; U |
| Mall visitors naming dining as most common activity | 68% (a second article gives 64%) | P1C3-02; DEM-002 | Jan-Apr 2025; 266 of 800; non-probability, Jabodetabek malls; J |

**Frequency: GAP.** No opened source gives visits per month for ages 25-39 in Jakarta. The closest rows are younger (15-25), national or delivery-only, and no row isolates the 25-39 core. The coffee survey counts cups "bought or made", so it includes home coffee.

Analysis: a Jakarta Selatan resident spends about Rp548,000 a month on all prepared food (2024). Divided by the model's weighted average spend of about Rp103,400 per guest (derived from the model weights, not an input), this is a ceiling of about 5.3 visits a month if every prepared-food rupiah went to CORSA-priced meals. The real figure for an average resident is far lower; the ceiling only shows that "4+ visits a month" is not demonstrated.

## 4. Wheat, pasta and food service context

| Metric | Value | Row; register_id | Period; base; geography |
| --- | --- | --- | --- |
| Wheat used for food (FSI), USDA | 9.4 to 9.8 million tonnes (+4.3%); 10 million forecast 2026/27 | P1C4-04; DEM-050 | Jul-Jun 2024/25 to 2025/26; N |
| Wheat imports, USDA PSD | 10,452 to 13,023 thousand tonnes | P1C4-01; DEM-049 | Jul-Jun trade years; N |
| Instant noodle demand, WINA | 14,680 to 14,540 million servings (-0.9%) | P1C4-11; DEM-054 | 2024 to 2025; N |
| Households consuming rice; instant noodles; wheat flour | 88%; 71%; 32% | P1C4-14; DEM-057 | Susenas 2024; 341,802 households; N |
| Food service sector (HRI) | US$29 billion (2024); US$30 billion (2025) | P1C4-18; DEM-060; P1C4-20; DEM-061 | 2024; 2025; N |
| Foodservice sales split: full-service; fast food; cafes/bars; street stalls | 79%; 7%; 6%; 5% | P1C4-19; DEM-060 | 2024; N |
| Restaurants and rumah makan, DKI vs national | 202,983 vs 2,511,128 | P1C4-21; DEM-062 | 2024; establishments; J/N |

Conflicts: USDA imports (up) and BPS calendar-2025 imports (down 7.5%, 11.72 to 10.84 million tonnes) [P1C4-08; DEM-051;DEM-063] differ in period and are unreconciled. USDA food use rests on USDA alone. Instant noodles are down 0.9% in one table and up 1.0% in USDA text, with a unit error [P1C4-11 notes]. Cafes and bars are the smallest named formal segment [P1C4-19]. USDA names Tous Les Jours, Monsieur Spoon and Paris Baguette as growth chains; pasta is not a named foodservice segment [P1C4-23; DEM-061].

Analysis: the data show wheat is mainstream (71% of households use instant noodles) but do not measure restaurant pasta, taste or repeat purchase. Rice remains the norm.

## 5. Hypotheses H1-H8

Verdicts follow the plan's own criteria (section 2 of the plan). Three rules from the run-3 verification apply: no verdict on a difference within rounding or margin of error, no verdict on a single source, and no over-claiming of conversion.

| ID | Verdict | One-line reason |
| --- | --- | --- |
| H1 | UNDETERMINED | Funnel cannot be built; capture rate and class share are GAPs |
| H2 | NOT CONFIRMED (national: disconfirmed) | National series fall; Jakarta series missing |
| H3 | UNDETERMINED | One city mean, no upper-class median; arithmetic only |
| H4 | UNDETERMINED | Only a national grocery WTP proxy; no café or Jakarta WTP |
| H5 | UNDETERMINED | No visit-frequency data for ages 25-39 |
| H6 | UNDETERMINED | One survey, younger age, additivity unknown |
| H7 | MIXED, not decided | Wheat food use up, but pasta chains not evidenced |
| H8 | UNDETERMINED | No guest counts; sales per outlet only |

**H1 Target pool large enough for one flagship.** Criterion: funnel central case at least the model break-even of 128 guests a day (per the plan). Evidence: 244,600 (Pusat) and 535,920 (Selatan) residents aged 25-39 [P1C1-P06, P1C1-S06; DEM-028, DEM-029; June 2024; J]. Class share, frequency and capture rate are GAPs, so no funnel (Q9) can be run. Analysis: 128 guests a day over 30 days is 3,840 guest-visits a month, 0.7% of the Selatan 25-39 population visiting once a month. The pool alone is unlikely to bind; frequency and a 15-minute catchment do. This is arithmetic, not a funnel. Verdict: UNDETERMINED.

**H2 "Growing middle class" supports Jakarta.** Criterion: confirmed if an official Jakarta series is stable or growing; disconfirmed if national and Jakarta both fall. Evidence: national middle class 57.33 to 47.85 million (2019 to 2024) and 47.9 to 46.7 million (2025) [P1C2-05, P1C2-06, P1C2-01]; workers on middle-class wages 14.5% to 7.1% [P1C2-10]. No Jakarta series was found, so the Jakarta half of the disconfirming criterion is unmet. Jakarta nominal per-capita spend rose 6.01% (DKI) and 15.57% (South Jakarta) in 2025 [P1C3-05; DEM-004; P1C1-F05; DEM-020; J; not CPI-deflated], and Jakarta confidence is flat at 146.8 [P1C2-20]. Verdict: NOT CONFIRMED (disconfirmed nationally). The growing-middle-class wording is unsupported, a shrinking Jakarta middle class is also not shown, and the Jakarta class size is a GAP.

**H3 Segment A can afford more than one premium meal a week.** Criterion: median upper-class Jakarta prepared-food spend covers a premium bowl 4 or more times a month; disconfirmed if it cannot. The 4-bowl threshold is the owner's flagged assumption, not a sourced figure, and the plan's Rp85,000-110,000 bowl is a planner assumption absent from the model menu. Evidence: South Jakarta mean Rp548,413 per person per month (2024) [P1C1-E02; DEM-030; J]. Analysis, using the model's weighted ticket of Rp103,400 (net of 10% PBJT): 4 x 103,400 = 413,600, which is 75% of the mean (about 83% with PBJT). This is arithmetic on a mean, not a test. Caveats: the mean is per capita over all residents including children, so an adult mean is higher; a mean exceeds a median in a skewed distribution (Gini 0.435 [P1C2-28]), which cuts the other way; the figure is one paywalled teaser whose +25% change is unexplained; and household spend includes tax. No upper-class figure exists. Against: the top spending class saves more (16.9% vs 14.4%) [P1C2-18; U; household band]; one outlet reports upper-group spend -0.6% in the June 2026 holidays [disconfirming-evidence row 6]. For: South Jakarta total spend ranks 1 of 514 districts [P1C1-F05]. The disconfirming criterion (cannot cover 4 meals) is not met by the mean and the confirming one is untested. Verdict: UNDETERMINED.

**H4 Healthy or specialty coffee earns a price premium.** Criterion: stated willingness to pay (WTP) of 20% or more from several independent sources; disconfirmed if public data stay at 10% or below. Evidence: NielsenIQ, Indonesian consumers, 2025 release: 48% would pay more than 10% extra for food with enhanced nutrition, 19% would pay 20% more [P4W4-01, P4W4-02; BEH-013; 2025; base not seen; N; single vendor release, stated intent, grocery-type food]. That is one source, national, not café and not Jakarta. Related only: 47% of Gen Z coffee buyers name price as the main factor and 48% pay under Rp10,000 a cup [UE-N03, P1C3-01; DEM-001; Dec 2024; n=896; N]. Verdict: UNDETERMINED. The reason is a single national proxy and no café or Jakarta WTP, not an absence of rows. The 19% at +20% is the disconfirming marker named in the plan, but one source cannot decide it. Q4 is logged in section 7.

**H5 Weekly or better visit frequency.** Criterion: revealed data imply 4 or more visits a month; disconfirmed at 1-2. No frequency for ages 25-39 exists in the inputs, and the 5.3-visit ceiling (section 3.2) is not an estimate. The row on cutting eating out (Kompas, 2026-09-30) is BLOCKED and anecdotal, so it is not used. Verdict: UNDETERMINED.

**H6 Lunch and dinner dominate.** Criterion: lunch plus evening at 65% or more of occasions. Evidence: dinner 41%, lunch 37% of those who usually eat out then [P1C3-03, P1C3-04; DEM-003; Sep 2025; n=769; age 15-25, Java urban; U]. Whether the categories are additive is not stated, so 78% cannot be derived. Breakfast, afternoon and delivery share are absent. Verdict: UNDETERMINED, direction consistent.

**H7 The rice norm is a barrier to pasta.** Criterion: disconfirmed if wheat consumption and imports for food are rising and pasta or noodle chains are present and expanding. For: wheat food use +4.3% [P1C4-04; DEM-050], flour use +4.87% Jan-Nov 2025 [P1C4-07], rice per head falling since 2022 [P1C4-15]. Against: BPS imports fell in 2025 [P1C4-08], instant noodle servings -0.9% [P1C4-11], 88% of households use rice [P1C4-14]. The chain half is unmet: Champ Resto (Gokana, Monsieur Spoon and others) had 347 outlets against 331 but nine-month net sales fell [P3BF-026, P3BF-027; CMP-012; N], and no pasta chain is isolated. Verdict: MIXED, not decided; keep the rice-norm risk until a taste test.

**H8 200 guests a day is attainable.** Criterion: public sales per store imply 150 or more guests a day; disconfirmed at about 100 or fewer. No source gives guest counts or ticket size. Fore sales were Rp1,497,134,772,364 (FY2025) against Rp1,038,659,233,501 (FY2024) [P3BF-034; CMP-015; N], with 322 against 232 outlets [P3BF-032; CMP-014]. Analysis: dividing by 322 outlets or by their mean with 232 (277) gives about Rp12.7-14.8 million of sales per outlet per day (derived; the group includes Singapore and doughnut outlets). Without a ticket this is not a guest count. MAP Boga (Starbucks) sales were flat: Rp3,236,043 million vs Rp3,228,133 million [P3BF-016; CMP-007; FY2025 vs FY2024; N]; nine-month 2025 sales fell 2.77% [disconfirming-evidence row 13; DEM-025]. Verdict: UNDETERMINED.

## 6. What to tell Team B

Rule: no invented ranges. "Sourced range" means observed values in the cited rows; it is not a CORSA estimate. CAC and conversion items are context only. Values are from the model v0.5 `03-inputs.csv`, Base case.

| Model input | Current value (Base) | Evidence | Sourced range or GAP | register_id |
| --- | --- | --- | --- | --- |
| Guests per day, all dayparts (cov_*) | 200 (45 / 75 / 35 / 45) | No guest counts in any source; Fore sales per outlet per day Rp12.7-14.8 million is a proxy for revenue, not guests | GAP | CMP-014; CMP-015 |
| Daypart split (cov_*) | lunch 75 of 200 | Lunch 37%, dinner 41% of 15-25s who usually eat out then; additivity unknown | GAP (direction only, younger group) | DEM-003 |
| Visit frequency (no input) | none | No source for ages 25-39 | GAP | none |
| Morning ticket (tkt_morning) | Rp65,000 | 48% of Gen Z coffee consumers pay under Rp10,000 per cup, 30% Rp10,000-25,000 (bought or made) | GAP for café ticket; context only | DEM-001 |
| Lunch ticket (tkt_lunch) | Rp120,000 | Average delivery lunch order: Rp58,609 (Gen Z), Rp63,250 (Gen X), Rp65,130 (Millennials); delivery channel | Rp58,609-65,130 observed for delivery lunch, not dine-in; dine-in GAP | BEH-083 |
| Delivery order value (del_tkt) | Rp115,000 | Orders: 42% under Rp50,000, 42% Rp50,000-100,000, 11% Rp100,000-150,000 | Distribution as stated; the model value sits in the bracket 11% report | BEH-059 |
| Delivery orders per day (del_orders) | 25 | 73% of respondents used food delivery by Jan 2025; no orders-per-outlet data | GAP | BEH-059 |
| Marketing share (mkt_pct) | 3% | 55% cite promos as main reason to use delivery apps; 67% check discounts first | CONTEXT ONLY, not CAC or conversion; CAC GAP | BEH-039;BEH-032 |
| Minimum wage (ump) | Rp5,729,876 | Matches UMP DKI 2026 exactly | Rp5,729,876 (2026) | DEM-040 |
| Wage growth (wage_g) | 6.2% (cons. 7%, opt. 5%) | UMP +6.17% (2026), +6.5% (2025) | 6.17-6.5% (two annual observations) | DEM-040; DEM-041 |
| Seasonality Feb / Mar | 0.92 / 0.95 | MSI card spend rose in the Ramadan to Lebaran 2026 window: middle +4.1%, upper +2.6%, lower +2.1% against pre-Ramadan; all categories, THR-driven | Context only; café seasonality GAP | DEM-048 |
| Target pool (funnel input, not in model) | none | Residents 25-39: Pusat 244,600; Selatan 535,920 (June 2024, derived); class share and capture rate not found | Counts as stated; class share and capture GAP | DEM-028; DEM-029 |
| Prepared-food budget (ticket check; no bowl input) | model average about Rp103,400 per guest (derived, net of PBJT) | Prepared-food spend per person per month: Selatan Rp548,413 (2024), Pusat Rp513,174 (2024), DKI Rp524,958 (Mar 2026) | Rp513,174-548,413 (city 2024) and Rp524,958 (DKI Mar 2026); upper-class value GAP | DEM-030; DEM-031 |

Analysis: the evidence moves no guest-volume case. Team B should keep 200 guests a day as an unsourced assumption tested against the 128 break-even, not cite a "growing middle class", and validate tickets in the section 7 work before using delivery lunch values as a dine-in proxy. Afternoon and dinner tickets have no source (GAP).

## 7. Gaps and primary-research brief

| Gap | Why desk research cannot fill it | Primary question |
| --- | --- | --- |
| DKI-wide population 25-39; population by kecamatan | Only city rows were opened; BPS blocked | Closed by the BPS WebAPI key (see section 8) |
| Class distribution (middle/upper) and prepared food by class, DKI | Only means and national classes found | BPS WebAPI key, or a short income-band block in the survey below |
| Jakarta middle-class and wage-by-education series | Not found in any opened source | BPS WebAPI key (Sakernas, Susenas tables) |
| Visit frequency, ages 25-39, three districts | Not published | Intercept survey at lunch hour, n=150 or more: visits in the last 30 days, average spend, daypart |
| Q4 WTP for the actual bowl and coffee | Public WTP is one national NIQ proxy (BEH-013) | Price-ladder card test (3 price points) and a pop-up counter test |
| Capture rate and daytime population | Footfall and tenant headcounts not public | Foot-traffic counts per daypart at 3 candidate sites; broker headcounts; delivery-app order sampling |
| Real guest counts per outlet | Not public | 2-3 operator or broker interviews through Samuel (no direct contact with restaurants without his release) |
| Q3 Eating-out and café spend by age band (25-39 vs 15-24 and 40+) | No opened source splits spend by age; rows are generation-based and national | Add an age band and spend question to the intercept survey |
| Q6 Daypart split and delivery share against the model's 45/75/35/45 | One youth survey (lunch 37%, dinner 41%); no breakfast, afternoon or delivery share | Daypart and channel question in the intercept survey; delivery-app order sampling |
| Q2 Café vs warung share of prepared-food spend | Susenas prepared food is not split by outlet type | Survey question on venue type; BPS WebAPI cannot split it |
| Q9 Funnel (low/central/high guests per day vs 128 and 200) | Class share, frequency and capture rate are GAPs; not built | Fill the rows above, then run the funnel |
| Pasta and grain-bowl acceptance | Statistics do not measure taste | Blind taste test, 20-30 participants of the target age |

## 8. Method and limits

- **Relays dominate.** Of 92 input rows in the four demand files, 64 are VERIFIED-OPENED (relay), 20 VERIFIED-OPENED (original) and 8 CORRECTED-OPENED. Most population, spend and class rows are BPS data copied by Databoks, GoodStats, Kontan or CNBC Indonesia (tier 3).
- **BPS itself is blocked.** `bps.go.id` and `jakarta.bps.go.id` returned access errors (403) and no bypass was used. The original-source rows are mostly Bank Indonesia, World Bank, USDA and company filings.
- **The BPS WebAPI key would close some gaps:** DKI-wide and kecamatan population by age band, Susenas expenditure classes for DKI, prepared-food spend by class, and Jakarta wage tables. It would not close frequency, WTP, capture rate or guest counts.
- **Samples.** Survey rows are online panels (Jakpat, Snapcart), mostly younger than the target and not Jakarta-only. No source splits out ages 25-39.
- **Conflicts kept,** not resolved: base sizes (955/995 vs 769), 68% vs 64% mall figure, import series by period, Kontan typos.
- **Derived values** in this report are labelled Analysis or DERIVED, with the formula in the text. Run-3 lessons applied: no verdict on rounding-sized differences (upper class 1.1 to 1.2 million), none on a single source (USDA food use, -0.6% holiday spend), and no conversion or CAC claims.
- **Next step:** independent verifier (CLAUDE.md section 7) must re-open each cited row before this report is accepted.

## Appendix: balance check of downside and mixed rows (run 4, 2026-10-18)

- Rule: section 2.4. Scripted candidate list from `demand/*.csv`, `plan4-spend-drivers.csv`, `listed-operators.csv` and table A of `data/raw/2026-10-17-disconfirming-evidence.md`; every row read in full before it was kept.
- Counts: downside or mixed rows in scope 43; cited before 20; added 23; cited after 43. Distinct row ids cited in the report rose from 67 to 87 (5 of them are rows named as excluded).
- Excluded: BLOCKED table rows 5, 8, 15; not-downside rows UE-N07, P1C1-C01, P1C4-10, SD19, UD-N12.
- Conclusions changed: none. Details in `tasks/2026-10-17-run4-balance-check.md`.
