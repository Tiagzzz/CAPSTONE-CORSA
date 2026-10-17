# Plan 3: Competitive landscape and price ladder (Jakarta target districts)

Date: 2026-10-16. Planner: planner-3. Status: DRAFT for owner approval. No data collected yet. Feeds gap-analysis §4 gaps 3 and 4 and tensions T18, T21, T22, T23.

## 1. Goal, decisions fed, research questions

**Goal.** Deliver (a) the scope's required competitor and benchmark map (SCOPE §6), (b) one reconciled, dated price ladder that Team B can load (FIN §8 L294-295 waits for it), (c) listed-operator performance and foreign-entrant base rates, (d) Oakberry facts reconciled.

**Decisions fed.** CORSA price position ("premium" SCOPE §10 vs "middle, affordable" M5 50:44); whether the districts show white space or saturation; which of SCBD / Senopati / Kuningan / Kemang / PIK (plus Senopati side streets, FIN) to prioritise on competition; format (street / mall / hybrid); how much weight to put on foreign-entrant failure risk.

| # | Research question (testable) |
| --- | --- |
| Q1 | How many comparable venues (per category) operate in each target district, by format (street / mall / hybrid) and size class? |
| Q2 | What are the dated 2026 dine-in menu prices (IDR, with/without 10% PBJT stated) of a reference basket: pasta main, healthy bowl, latte (regular), functional drink? What are P25 / median / P75 per category and district? |
| Q3 | Where does the Team B placeholder (pasta IDR 82-135k, latte 50k, bowl 85-110k) fall in that distribution (percentile), and in each of the three price tiers (mass chain, mid, premium)? |
| Q4 | What is the delivery-app price uplift vs the official dine-in menu for a sample of items (FIN assumes about 15.6%)? |
| Q5 | What do listed operators' filings show on outlet counts, average revenue per outlet, margin, closures (FAST, MAPB, PZZA, ENAK, FORE)? Is the mid-market contracting or growing? |
| Q6 | How many foreign F&B brands entered Jakarta since 2015, how many exited, and why (tier 1-3 evidence)? What is the survival base rate in the sample? |
| Q7 | Which Oakberry facts (units, store capex, Indonesia footprint, profitability) are supported by filings or official sources, and which claims (3,000 units, USD 50k) are refuted? |
| Q8 | Do local chains (Fore, Kopi Kenangan, Tomoro, Janji Jiwa) already occupy the "affordable specialty" position, leaving only a premium or community niche? |

## 2. Hypotheses

| # | Hypothesis | Confirmed if | Disconfirmed (and implication) |
| --- | --- | --- | --- |
| H1 | CORSA's placeholder prices sit at or above the district median, i.e. premium, not "middle" | Core bowl and latte above P60 of the sourced distribution in Tier-1 districts | Below P40: "middle" is feasible, FIN "headroom" claim holds. If above P90: price out of line, test at lower tier or smaller portions before entry |
| H2 | The specialty-coffee segment is saturated by low-price chains | Per district, 3+ chain outlets (Fore, Kopi Kenangan, Tomoro, Starbucks) within 500 m of any candidate street, latte median <= IDR 35k | Fewer than 2 chain outlets and independents above IDR 45k: white space for a premium coffee. If saturated: coffee must be a traffic driver, not the profit core |
| H3 | Healthy-bowl and Italian-casual formats are less saturated than coffee | Bowl/pasta venue density < coffee density by 3x or more | Equal or higher density: differentiate on community/lifestyle, not on food category |
| H4 | Lifestyle/community concepts (run-club cafés) are few and small | Fewer than 10 documented venues with a recurring public community programme in the 5 districts | Many: community is not a differentiator; treat it as table stakes |
| H5 | Mid-market casual dining in Jakarta is under pressure | Filings: FAST net loss, outlet closures; PZZA/ENAK weak margins | Listed operators growing outlets and margin: market healthy |
| H6 | Foreign entrants without a strong local partner fail more often than with one | In the case set, exits concentrate among solo/JV-weak entrants with stated reasons (rent, boycott, unit economics) | Exits unrelated to partner: partner structure is not protective |
| H7 | Oakberry shows replicability, not profitability (OAK1 §04) | Filings: negative operating cash flow, net loss 2025 | Positive: strengthen benchmark |

## 3. Competitor selection method

**Universe and inclusion rule (applied per district x category).** Systematic, not brand-led: build the list from neutral directories first (OpenStreetMap / Google Maps category search recorded as leads, mall directories of Plaza Senayan, Senayan City, Pacific Place, SCBD Suites/Sudirman Central, Kuningan City, Pondok Indah/PIK Avenue, plus brand store-locator pages), then include every venue that meets the rule, regardless of fame.

| Category | Inclusion rule (within a 1.5 km radius of the district anchor, plus the district polygon) |
| --- | --- |
| Italian / pasta casual | Pasta is >= 30% of the menu mains; dine-in; mid to upper price. Includes Italian chains, hotel and independent restaurants. Excludes pizza-only delivery |
| Specialty coffee | Espresso-based, dine-in or grab-and-go; chains (Fore, Kopi Kenangan, Tomoro, Janji Jiwa, Starbucks, % Arabica, Common Grounds) and independents with own roasting or a published specialty menu |
| Healthy bowls / functional drinks | Menu positioned as healthy (bowl, salad, acai, juice, functional shots): SaladStop, Fedwell, Burgreens, Oakberry-type, Grains of Glory etc. |
| Lifestyle / community | Venue hosting a recurring community programme (run club, padel, "third place" café) documented on the brand's official pages |

**Sample size.** Target full census of qualifying venues per district-category where fewer than 15, otherwise stratified sample. Floor: at least 8 priced venues per category (pasta, bowl, coffee) across all districts and at least 4 in each Tier-1 district; at least 40 venues in total; at least 20 with a full basket price.
**Bias controls.** (1) Directory-first discovery with counts of both known and unknown brands; (2) stratify by price tier and by format (chain / independent; mall / street); (3) cap any one brand at 15% of rows in a price statistic; (4) log excluded venues with the reason; (5) a blind second searcher (verifier) lists 5 venues per district independently and we report the overlap (recall check); (6) closures and recent openings noted (Google Maps "permanently closed" is a tier 4 lead, confirm with a tier 1-3 source or leave it as "unconfirmed").
**Format and size.** Format (street / mall / hybrid) from the official address or mall directory. Size is rarely published: record seats or m² only if the official source states it, else "n/a" (gap).

## 4. Data schema

**`data/processed/competitors.csv`** (one row per venue-item; venue master in `competitors_venues.csv`)

| Column | Content |
| --- | --- |
| venue_id, brand, operator | ID, brand, legal operator (if known) |
| category | pasta / coffee / bowl_drink / community |
| ownership | local chain / international chain / independent / hotel |
| district, address, lat_lon | One of SCBD, Senopati, Senopati-side, Kuningan, Kemang, PIK, other |
| format | street / mall / hybrid; size_m2, seats (nullable) |
| status, status_date | open / closed / unconfirmed |
| item, item_class | Exact menu name; reference class (pasta_main, bowl, latte_regular, functional_drink) |
| size_note, price_idr, tax_basis | Portion/size; price; "excl./incl. 10% PBJT and service" |
| channel | dine_in_official / app_gofood / app_grabfood |
| price_date, access_time | Date of menu (if shown) and capture date+time (WIB) |
| source_url, source_id, source_tier | URL, ID in `sources/sources.md`, tier 1-3 |
| cross_check_id, delta_pct, note | Second source and difference |

Rule: a row's price must come from the official menu (tier 1). An app price is a separate row (tier 3) and never stands alone if the official menu exists. Tier-4 leads are kept in a separate `leads.csv`.

**`data/processed/price-ladder.csv`** (built by script from the above)

| Column | Content |
| --- | --- |
| item_class, district (or "all"), tier_band | e.g. latte_regular x SCBD x mass/mid/premium |
| n_venues, n_brands, min, P25, median, P75, max | Statistics; no stat if n < 4 (then "insufficient") |
| dine_in_vs_app_uplift_pct | From paired rows |
| corsa_placeholder_idr, corsa_percentile | Team B values compared (read-only) |
| reference_date, sources | Capture window, source IDs |

Plus `reports/2026-10-XX-competitor-map-and-price-ladder.md` with a district x category heat table (venue counts), the ladder, and a one-page "read-across" for Team B (inputs only, no model changes).

## 5. Source map

"Checked" = quick scan on 2026-10-16 (12 searches). IDX is where audited filings sit; searches returned press reports of them, so direct availability on idx.co.id still has to be confirmed by the executor.

| Data item | Candidate source | Tier | Free/public? | Latest edition / date | Within 2 y? | Availability checked |
| --- | --- | --- | --- | --- | --- | --- |
| FORE prospectus, FY2024/25 reports | IDX (idx.co.id, "Laporan Keuangan dan Tahunan"); Fore press release fore.coffee/id/press-release-fore-coffee- | 1 | Yes (IDX public; fore.coffee unreachable from this sandbox) | IPO 14 Apr 2025; price Rp188, raised ~Rp353bn (press) | Yes | Partly: IPO facts confirmed via idnfinancials / idxchannel; filing itself not opened |
| MAPB (Starbucks Indonesia) FY2025 and H1 2026 | IDX filings | 1 | Yes | FY2025 sales ~Rp3.24tn, net loss ~Rp150.8bn; H1 2026 loss ~Rp121.5bn (Bisnis.com, 31 Mar and 30 Jul 2026) | Yes | Press confirmed; IDX file to open |
| FAST (KFC) FY2025 | IDX | 1 | Yes | FY2025 loss ~Rp366-369bn (figures differ across press), outlets 715 to 690, going-concern note | Yes | Press only; verify in filing |
| PZZA / Sarimelati (Pizza Hut) FY2025 | IDX | 1 | Yes | Net profit ~Rp24.75bn, sales ~Rp3.05tn (31 Mar 2026 press) | Yes | Press only |
| ENAK / Champ Resto FY2025 | IDX | 1 | Yes | Listed Feb 2022 (not 2025); latest filing not found in scan | To check | IPO fact confirmed; no 2025 filing seen |
| Official menus with prices | Brand sites and apps (Fore, Kopi Kenangan, Tomoro, Starbucks, SaladStop, Fedwell, Italian restaurants) | 1 | Yes where posted; many are app-only | Unknown per brand | Capture 2026 | NOT confirmed: Kopi Kenangan price found only on majoo.id (Jun 2026, third-party, latte Rp19k/24k) and SaladStop only on an undated Tokopedia blog (tier 4 leads). Official menus must be located |
| Delivery prices | GoFood / GrabFood public listings | 3 | Public, variable | Captured at time of use | Yes | Not checked (item-by-item only, no bulk) |
| Store counts / locator | Brand store-locators, mall directories | 1 | Yes | 2026 | Yes | Not checked |
| Tomoro outlets, strategy | Press (World Coffee Portal) | 3 | Yes | Oct 2024 about 600 stores in Indonesia (borderline, 2 y limit); CEO change Feb 2025 | Borderline | Confirmed; need a 2026 figure |
| Foreign entrant cases | IDX/company filings, Jakarta Post, Bisnis.com, Kontan, franchisor press | 1-3 | Mostly (paywall limits on Bisnis Pro) | Marché Mövenpick closed 30 Sep 2020 (Jakarta Post, Bisnis) | No (2020) | Confirmed; outside the window, see §6 |
| Oakberry | OAK Holding 2025 financial statements (982 units), official US franchise guide, Oakberry site (OAK1, OAK2) | 1 | Yes | 2025-26 | Yes | Scan found no Jakarta store as of 2026 (only Bali 2023); existing repo facts to be re-opened |
| District context (rent, mall tenant mix) | CBRE / Colliers / JLL public Indonesia reports | 3 | Free summaries | Q2-Q3 2026 | Yes | Not checked |

## 6. Foreign-entrant case-study method

- **Case list (draft, from tier 1-3 leads, to be confirmed):** exits: Lotteria (2020), Marché Mövenpick (Sep 2020), Starbucks-style retrenchment (MAPB) and KFC closures (boycott, FAST) as stress cases; successes/expansions: Starbucks, Oakberry (Bali only), Tomoro (Indonesian-founded, so a local control), Korean and Japanese chains to be discovered. The executor builds the list by a structured search (brand + "tutup semua gerai" / "exit Indonesia" / "masuk Indonesia" for 2015-2026) and logs all found, not only memorable ones.
- **Window rule conflict.** The owner's recency rule (published on/after 2024-10-16) excludes older exits. Proposed handling: a case enters the base rate only if the exit or its reporting is dated within the window; older cases (Lotteria, Marché Mövenpick) are shown separately as "historical, outside window, labelled" and not used in the rate. **Owner to confirm** (small sample otherwise).
- **Establishing an exit:** two of: (1) company or operator statement / IDX disclosure (tier 1); (2) mall or franchisor notice; (3) major outlet report (Jakarta Post, Bisnis, Kontan, Kompas; tier 3). Google Maps "closed" is tier 4 and insufficient.
- **Establishing a reason:** only as stated by the company, or attributed in tier 3 reporting; otherwise "reason not documented" (gap). No inference. Record: entry year, entry mode (franchise / JV / owned / master franchise), format, exit year, stated reason, local partner, source IDs.
- **Base rate:** entrants/exits with the n shown; no percentage if n < 10 (report counts and flag "not statistically meaningful").

## 7. Sub-agent work breakdown

Models follow CLAUDE.md §4: Haiku for fetch/extract/format/link check; Sonnet for evaluation, synthesis, verification; no Opus (no judgement task needs it).

| Phase | Agent | Responsibility | Model | Owned files | Parallel? |
| --- | --- | --- | --- | --- | --- |
| 0 | A0 source-prep | Locate IDX filing URLs and official menu URLs; confirm free access; seed `sources/sources.md` rows | Haiku | `sources/sources.md` (append) | first, single |
| 1 | A1 discovery | Directory-first venue list per district x category with inclusion log | Sonnet (rule application) | `data/raw/2026-10-XX-venue-discovery.csv` | single, then fans out |
| 2a | B-pasta | Menu prices, Italian/pasta | Haiku | `data/raw/..-prices-pasta.csv` | parallel |
| 2b | B-coffee | Menu prices, coffee (local/intl chains, independents) | Haiku | `..-prices-coffee.csv` | parallel |
| 2c | B-bowl | Menu prices, bowls and functional drinks | Haiku | `..-prices-bowl.csv` | parallel |
| 2d | B-community | Lifestyle/community concepts, programmes | Haiku | `..-community.csv` | parallel |
| 2e | B-filings | IDX filings: outlets, revenue per outlet, margin, closures (FORE, MAPB, FAST, PZZA, ENAK) | Sonnet (financial reading) | `data/processed/listed-operators.csv` | parallel |
| 2f | B-entrants | Foreign-entrant case table (§6) | Sonnet | `data/processed/foreign-entrants.csv` | parallel |
| 2g | B-oakberry | Reconcile T23 facts | Haiku (extract) | `data/processed/oakberry-reconciled.md` | parallel |
| 3 | C-app | Item-by-item app uplift sample (max 20 items, date/time stamped) | Haiku | `data/raw/..-app-sample.csv` | after 2a-c |
| 4 | D-build | Merge, clean, compute ladder; flags for n < 4 | Haiku (script) | `data/processed/competitors*.csv`, `price-ladder.csv`, README | after 2-3 |
| 5 | E-synth | Report: map, ladder, hypotheses H1-H7 verdicts, saturation test, implications | Sonnet | `reports/2026-10-XX-competitor-map-and-price-ladder.md` | after 4 |
| 6 | V-verify | Independent verification (§8) | Sonnet | `tasks/2026-10-XX-plan-3-verification.md` | after 5; V-links (Haiku) in parallel |
| 7 | F-fix | Corrections, lessons entry | Haiku | as needed, `tasks/lessons.md` | after 6 |

Main agent only orchestrates (CLAUDE.md §2). Each worker prompt carries objective, owned files, §5 rules, verification steps, report fields.

## 8. Verification (CLAUDE.md §7)

Separate verifier (Sonnet V-verify, plus Haiku V-links): (1) re-open the source for **all** filings figures and **every** FAST/MAPB/FORE number (full); (2) re-check prices: all anchors for pasta/latte/bowl in Tier-1 districts, and a random 25% of other rows (min 30 rows), tolerance 0 (exact), flag mismatches in value / size / tax basis / date; (3) every source in `sources/sources.md` has all fields (title, publisher, URL, pub date, access date, tier, use) and a justified tier; (4) all links resolve; (5) flag any claim resting on tier 4 only; any row from an app without official-menu comparison where the official menu exists; (6) recall check from §3 bias control (blind second list); (7) ladder statistics recomputed from CSV; (8) pass threshold: zero unresolved mismatches in the full-check set, <= 5% in the sample, and all failures fixed and rechecked.

## 9. Deliverables and acceptance criteria

| Deliverable | Acceptance test |
| --- | --- |
| Competitor dataset + venue master | >= 40 venues, >= 8 priced venues per category, >= 4 per category in each Tier-1 district (or documented gap); every row has all mandatory columns, price_date within 2026, tier 1-3 |
| Price ladder | Four item classes, stats per district where n >= 4; Team B placeholders placed by percentile; app uplift reported with n |
| Competitor map (report) | Heat table district x category x format; saturation and white-space verdict per district with disconfirming evidence shown |
| Listed-operator table | Five operators, each figure traced to a filing page, FY and unit stated; press numbers marked as secondary |
| Foreign-entrant table | Each case: exit proof and stated reason from tier 1-3 or "not documented"; counts, no rate if n < 10 |
| Oakberry reconciliation | Each of the contested facts (units, cost, Indonesia, profitability) marked supported / refuted / unresolved with source |
| Sources + verification | All sources registered; verifier report shows thresholds in §8 met |
| Gap list | Every missing item logged in the report (not filled with estimates) |

## 10. Gaps desk research cannot fill, and primary-research questions

| Gap | Why unfillable | Primary-research question (store visits; Samuel's Jakarta trip, early Nov) |
| --- | --- | --- |
| Footfall and covers per venue | Not published | Count guests entering 3 comparable venues in 30-min slots, weekday lunch/evening and weekend (SCBD, Senopati, Kuningan) |
| Sales volumes per store | Only chain averages in filings | Ask (via Samuel, who alone contacts restaurants, M4) operators/landlords for typical covers: only if the owner lifts the no-contact rule |
| Dine-in vs app price in practice, current promos | Menus change, promos hide net price | Photograph physical menus, note the tax and service line, compare with app on the same day |
| Seat count / m² for competitors | Rarely stated | Visual count on visit |
| Willingness to pay for CORSA's premium | No reliable public measure | Short intercept survey (price points IDR 85/100/120k) in the districts |
| Real vacancies / closures on the street | Maps data is tier 4 | Walk the Senopati and Kemang strips and log shuttered units |

## 11. Risks, effort, order of work

| Risk | Mitigation |
| --- | --- |
| Official menus are in apps only, not on the web | Capture item by item in the app on the visit; if only apps exist, label tier 3 and mark gap |
| Press-only filing numbers conflict (FAST Rp366 vs 369bn) | Use the IDX PDF; log the discrepancy |
| Site terms / blocking | No bulk scraping; manual item capture with date/time; stop when blocked and report (§11) |
| Small n per district-category | Pool by tier, show "insufficient", do not extrapolate |
| 2-year window removes useful entrant cases | Owner decision requested (§6) |
| Price drift / promotions | Record capture date, list price, not promo price |

**Effort.** About 12-16 Haiku agent-runs and 5 Sonnet runs; roughly 2 working days elapsed with parallel phases.
**Order given interim deadline (21/22 Oct):** 16-17 Oct phases 0-1; 17-18 Oct phase 2 (a-d priority: prices; e: FAST/MAPB/FORE; g: Oakberry); 19 Oct phases 3-4 and first ladder to Team B (the 19th internal goal, M5 25:19); 20 Oct phase 5 draft + phase 6 verification of Tier-1 anchors; 21 Oct fixes. Lower priority (2f foreign entrants complete set, community 2d depth, ENAK/PZZA) may slip to Phase 2 (to 11 Dec) and appear as "preliminary" in the interim.

## Appendix: plan checks against CLAUDE.md §6

Goal, questions and acceptance (§1, §9); files (§7); verification (§8); models and rationale (§7); deliverables (§9). Tier rules, no fabrication, gaps logged, fact vs analysis separated in the report, public data only.
