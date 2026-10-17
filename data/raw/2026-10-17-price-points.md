# Price points, Jakarta (P3-PRICE, run 2, 2026-10-17)

Collector: P3-PRICE. Plan: `tasks/2026-10-16-plan-3-competitors-price-ladder.md` (Q2, Q3, Q4, H1, H2, H8-style questions on the price ladder). Rows: `data/processed/price-ladder.csv` (30 rows). Access date for all sources: 2026-10-17.

**Headline result: target not met.** 30 price points (target 40-80) and only 2 brands with usable published prices (Burgreens, Fore Coffee) instead of at least 4 per category. Almost every official brand site in scope shows menus without prices (prices sit only in the apps), the Grab and GoFood listings were not reachable without login or a bot challenge, and most media price lists found are pre-window. Nothing was estimated or filled in. Gaps are listed in section 5.

## 1. Sources used (one block per source)

### P3-PRICE-S1
- Title: Burgreens menu book ("BUKU_MENU_BURGREENS.pdf"), linked from the "Our Menu / Download our menu" page
- Publisher: Burgreens (PT Hijau Adil Bahagia), official brand site
- URL opened: https://www.burgreens.com/files/BUKU_MENU_BURGREENS.pdf (linked from https://www.burgreens.com/restaurant_menu)
- Printed publication date: none printed on the pages. PDF metadata: CreationDate 2025-08-19, ModDate 2025-08-19 (metadata only, not a printed date). The "Milestones" page lists 2025 openings, consistent with a 2025 or later menu. Menu seen on the live site 2026-10-17. Footer on pages: "Prices & menu are subject to change without prior notice".
- Proposed tier: 1 (the brand's own official menu). Caveat: brand-wide menu, no outlet-level prices; the page does not say which outlets use it.
- Access status: opened (download 34.8 MB, 32 pages). The PDF has no text layer (pdftotext returns nothing), so prices were read visually from rendered page images; each row carries a transcription, not a copy-paste quote.
- Tax basis: footer on pp. 12 and 25 reads "Prices exclude Government Tax & Service Charge" (so "++").
- Unit: item prices are printed as bare numbers (for example 68). Reading them as thousand IDR is an inference (same PDF p.3 prints "Rp 35.000/pax" for catering). Flagged in each row's notes.
- Outlets listed on the site page: Jakarta: Darmawangsa, Menteng, Pacific Place, Oakwood, Mall of Indonesia; Tangerang: The Breeze, Bintan. (Site text.)
- Quotes (page: transcription): see the `snippet` column of the CSV (rows P3PR-001 to P3PR-024).

### P3-PRICE-S2
- Title: "Daftar Menu Americano Fore Lengkap dengan Harganya"
- Publisher: IDN Times (Dining Guide), author Annisa Nur Fitriani; the page says it is written by community writers and reviewed by the editorial team
- URL opened: https://www.idntimes.com/food/dining-guide/menu-americano-fore-c1c2-01-3kz8p-0pt5h4
- Printed publication date: 14 Nov 2025, 09:20 WIB (read from the article's own byline block; the other dates on the page, such as 04 Sep 2026 and 02 Nov 2023, belong to sidebar and related articles and were ignored)
- Proposed tier: 3, weak (major outlet, but community-writer content and "sekitar" approximations; size, outlet, tax basis not stated)
- Access status: opened
- Quotes: in the CSV `snippet` column (rows P3PR-025 to P3PR-030), verbatim Indonesian.

## 2. Opened but yielded no row (reason)

| Source | URL opened | Finding | Why no row |
| --- | --- | --- | --- |
| Pizza Marzano Indonesia, home page | https://www.pizzamarzano.co.id/ | Offer text: "LUNCH PACKAGE 1 Starter + 1 Classic Pizza/Pasta + 1 Drink for only Rp. 115.000++" (no printed date) | Set-menu offer, not an item price; dated 2026-10-17 only by access. Kept here as context (a "++" basis: tax and service are added on top). |
| Pizza Marzano menu pages (main menu, pasta) | https://www.pizzamarzano.co.id/menu/main-menu/ | Lists pasta names (Penne Ricotta & Beef Sausage, Spaghetti Gambaretti, Fettuccini Salmone Pesto, Lasagna Classica, Spaghetti Tartufo, Spaghetti Bolognese, Fettucini Carbonara, ...) with no prices | No prices on the page |
| Pizza Marzano "Download Our Full Menu" PDF (Google Drive link on the site) | linked via the menu page; downloaded | Printed title "prev rev FA_2021.04.PM_MAIN MENU_April 2021", prices in thousand IDR, "subject to 10% PB 1 government tax & 5.5% service charged" | April 2021, outside the date window. Not used. |
| Oakberry Indonesia | https://oakberry.id/menu/ , /locations/ | Menu page has no item prices; states "*All prices are subject to 5% service charge & 10% government tax." and add-on surcharges (+10K, +20K, +30K); locations are Canggu, Ubud, Uluwatu, Seminyak (Bali) only | No base bowl price; no Jakarta outlet. Context for plan Q7: this official site lists Bali outlets only. Add-ons are not item prices. |
| Starbucks Indonesia | https://www.starbucks.co.id/menu/beverage-list/espresso-beverages | Beverage pages with no prices | No prices |
| Fore Coffee | https://fore.coffee/ , /menu/ | No prices on the page | No prices |
| Kopi Kenangan | https://kopikenangan.com/ and campaign pages | No prices; ordering is via the app | No prices |
| SaladStop Indonesia | https://saladstop.co.id/ and menu pages (signatures, super protein bowls, functional smoothies, matcha, locations) | No prices; ordering via app | No prices |
| Tanamera, Common Grounds, Anomali, Crunchaus | brand sites | Retail bean shops or login pages; no drink prices | No prices |
| Kontan MomsMoney, 10 Jun 2025 (Pizza Hut Ristorante 3rd anniversary) | https://momsmoney.kontan.co.id/news/promo-pizza-hut-ristorante-3rd-anniversary-ragam-menu-spesial-mulai-rp-30-000-an | "Pasta Con Bistecca (Rp 105.000)", "Caesar Salad Salmon (Rp 93.000)", "Hana Galaxy (Rp 34.000)", quoting Pizza Hut Indonesia's Instagram | Anniversary promo menu (9 Jun to 31 Jul 2025), not clearly list prices. Excluded from the CSV (promo). |
| Kontan MomsMoney, 5 Jun 2026 (Kopi Kenangan promo) | https://momsmoney.kontan.co.id/news/promo-kopi-kenangan-juni-nikmati-2-kopi-mantan-hanya-rp-29-ribuan-cek-caranya | "dua kopi Kenangan Mantan ukuran Regular dengan harga Rp 29.000-an saja, dari harga normalnya Rp 38.000" | Two-drink bundle; no single-item price stated. Context only: low-price local chain (disconfirming evidence for a premium coffee position, H2). |
| Kontan MomsMoney, 19 Jan 2026 (Starbucks) | https://momsmoney.kontan.co.id/news/promo-starbucks-hari-ini-19-januari-nikmati-2-kopi-favorit-hanya-rp-55-ribu | "Tall Caffe Latte (Hot/Iced) dan Cinnamon Roll hanya Rp 55.000" (GrabFood bundle) | Bundle promo, not an item price |
| IDN Times promo bundling Feb 2026 / May 2026 | https://www.idntimes.com/food/dining-guide/promo-bundling-kopi-mei-2026-00-z5hk4-ybm1xw | Bundle prices with "harga normal" for bundles only | Bundles, not items |

## 3. Excluded: pre-window or not tier 1-3 (leads only, not in the CSV)

Pre-window (printed date before 2024-10-16): IDN Times Fore menu list (02 Nov 2023, 14:30 WIB; 21 to 49 ribu range), IDN Times Starbucks list (23 Aug 2023), IDN Times Tomoro list (16 Jan 2024), Pizza Marzano PDF (April 2021).

Not opened (blocked): Tempo "Daftar Menu Fore Coffee dan Harganya" and Tempo Starbucks list (HTTP 403 from tempo.co, not bypassed). Four Seasons Alto menu page (HTTP 403).

**Leads (tier 4 or undated; not in the CSV, not to be used as figures):**
- Majoo (POS vendor blog, "2026"): Kopi Kenangan Mantan regular Rp18,000 / large Rp24,000; Starbucks Caffe Latte Tall Rp52,000, Grande Rp57,000 ("estimasi 2025").
- Tokopedia blog (undated): SaladStop wrap or bowl Rp95,000.
- Mojok (undated): % Arabica caffe latte 354 ml Rp59 ribu, Spanish latte Rp65 ribu, americano Rp49 ribu; Starbucks Tall americano Rp37 ribu.
- Time Out (undated): Common Grounds espresso IDR 35,000.
- Wanderlog / blog reviews: Osteria Gia Spaghetti Al Burro e Pepe IDR 225K.
- Gramedia (undated): Kopi Kenangan Mantan Rp18,000.

## 4. Grab and other app prices: not captured

- food.grab.com public pages are client-rendered. The restaurant list page returned "We're Coming For You / Sorry, we don't deliver here yet" (location gate); chain pages (Starbucks, Kopi Kenangan) returned HTTP 500; the pasta cuisine page returned HTTP 401 "Session Expired"; the page HTML for a restaurant (Spagetindo) contained no menu prices. The Grab web-menu API returned HTTP 502 without login. No prices were read. No login attempted, no challenge bypassed.
- gofood.co.id returned a WAF block page (HTTP 403, Tencent Cloud WAF). Not bypassed.
- Pizza Hut Indonesia's ordering site (pizzahut.co.id) loads its menu from an API that answers "Missing request header" (HTTP 400). Not pursued (would need app headers).
- Therefore the app-versus-store uplift (Q4, FIN assumption about 15.6%) cannot be computed. No "app price (may include markup)" rows exist.

## 5. Gaps and problems

1. Pasta/Italian: no Italian-restaurant item price from an official source was reachable. The one pasta row is a plant-based pasta from a healthy chain (Burgreens) and should not stand as an Italian benchmark. Pizza Marzano, Pizza Hut, Osteria Gia, Pizza e Birra, Gioi, Sopra, Union: no in-window official prices obtained.
2. Specialty coffee: Fore (media-reported, weak) and two Burgreens coffee items only. Starbucks, Kopi Kenangan, Tomoro, Common Grounds, % Arabica, Djournal, Anomali, Tanamera: no in-window tier 1-3 price opened.
3. Bowls/functional drinks: Burgreens only. SaladStop, Crunchaus, Oakberry (Bali only), Green Rebel: no prices.
4. District split is not possible: prices are brand-wide menus or chain list prices, not outlet-level. Outlets are only known at brand-site level.
5. Primary-research route (plan section 10): photograph physical menus and capture app prices on the Jakarta visit.

## 6. DERIVED: summary statistics (min, median, max, with n)

Method: computed with python3 from `data/processed/price-ladder.csv` (column `price_idr`). Median is the standard median (mean of the two middle values when n is even). One row per distinct menu item; no deduplication across channels needed (all rows in-store or media reports of in-store menus, no app rows). IDR, as listed, tax and service basis differs by source (see below). Flag: n<4 = insufficient, do not use as a distribution; "brand cap" = share of rows from one brand above the plan's 15% cap (the cap cannot be met with these data).

| Category | n items | n brands | Min | Median | Max | Flags |
| --- | --- | --- | --- | --- | --- | --- |
| pasta | 1 | 1 (Burgreens) | 60,000 | 60,000 | 60,000 | n<4; one plant-based pasta, not Italian; single brand |
| coffee (espresso and signature drinks) | 8 | 2 (Fore 6, Burgreens 2) | 22,000 | 29,000 | 32,000 | brand count below 4; Fore rows are media-reported "about" prices, tax basis not stated; Burgreens rows exclude tax and service |
| bowl (bowls and salads) | 12 | 1 (Burgreens) | 50,000 | 59,500 | 68,000 | single brand = 100%; excludes tax and service |
| functional_drink | 9 | 1 (Burgreens) | 27,000 | 45,000 | 52,000 | single brand = 100%; excludes tax and service |

Sub-class cells (all from the same rows): espresso n=3 (22,000 / 22,000 / 25,000); signature_coffee n=5 (29,000 / 29,000 / 32,000); rice_bowl n=5 (50,000 / 55,000 / 59,000); salad and salad_bowl together n=4 (50,000 / 62,500 / 65,000); smoothie_bowl n=3 (68,000 / 68,000 / 68,000, n<4); protein_shake n=3 (all 52,000, n<4); smoothie n=3 (45,000 / 45,000 / 47,000, n<4); herbal_elixir n=3 (27,000 / 27,000 / 35,000, n<4).

Not comparable without adjustment: Burgreens prices exclude 10% tax and service charge ("++"), Fore media prices do not state a basis. Do not mix them in a district median.

## 7. Hypotheses touched (direction)

- H1 (CORSA placeholder at or above the median, premium): not testable; only one brand's bowl prices (IDR 50,000 to 68,000 before tax and service) and no Italian benchmark. Team B's bowl placeholder (85 to 110k) sits above every bowl price in this sample, but n=12 is from one plant-based brand: mixed or no evidence, not a percentile.
- H2 (coffee saturated by low-price chains): weak support. Fore Americano about 22,000 and signature Americano drinks 29,000 to 31,000 (Nov 2025 media); a Kontan promo (Jun 2026) states a normal price of Rp 38,000 for two Kopi Kenangan Mantan. Starbucks, Tomoro prices not obtained, so no latte median.
- H3, H4: not touched.
