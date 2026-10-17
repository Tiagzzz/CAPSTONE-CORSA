# Price points, Jakarta (P3-PRICE, run 2, 2026-10-17)

Collector: P3-PRICE. Plan: `tasks/2026-10-16-plan-3-competitors-price-ladder.md` (Q2, Q3, Q4, H1, H2, H8-style questions on the price ladder). Rows: `data/processed/price-ladder.csv` (30 rows in the first pass; 59 rows added in Run 3b, see the "Run 3b" section at the end). Access date for all sources: 2026-10-17.

**Headline result of the first pass (superseded in part by Run 3b at the end of this file): target not met.** 30 price points (target 40-80) and only 2 brands with usable published prices (Burgreens, Fore Coffee) instead of at least 4 per category. Almost every official brand site in scope shows menus without prices (prices sit only in the apps), the Grab and GoFood listings were not reachable without login or a bot challenge, and most media price lists found are pre-window. Nothing was estimated or filled in. Gaps are listed in section 5.

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

Recomputed after Run 3b (P3-PRICE-b), 89 rows in the CSV (30 first pass + 59 Run 3b), of which 68 carry a numeric `price_idr`. Rows with a blank `price_idr` (ranges, per-person spend, promo redemption prices) are excluded from every cell below.

| Category / subset | n items | n brands | Min | Median | Max | Flags |
| --- | --- | --- | --- | --- | --- | --- |
| pasta (all numeric item prices, all types mixed) | 20 | 8 (Burgreens, Casa Pasta, Fish Lab, Fish Streat, Halo Pasta, Pepper Lunch, Pizza Marzano, Sky Pasta) | 20,000 | 86,500 | 109,000 | ok |
| coffee (all numeric item prices) | 24 | 7 (Burgreens, Fore Coffee, Kopi Kenangan, Kopi Tuku, Pizza Marzano, Point Coffee, Tomoro Coffee) | 10,000 | 29,000 | 38,000 | ok |
| bowl (bowls and salads) | 15 | 2 (Burgreens, Pizza Marzano) | 50,000 | 60,000 | 105,000 | brands<4 |
| functional_drink | 9 | 1 (Burgreens) | 27,000 | 45,000 | 52,000 | brands<4 |

**Sub-class cells** (same numeric rows; n<4 and brand count <4 flagged; a median over fewer than 4 brands is not a market median):

| Category / subset | n items | n brands | Min | Median | Max | Flags |
| --- | --- | --- | --- | --- | --- | --- |
| pasta, Italian-restaurant list price (Pizza Marzano only) | 11 | 1 (Pizza Marzano) | 69,000 | 95,000 | 109,000 | brands<4 |
| pasta, Japanese-style teppan (Pepper Lunch) | 3 | 1 (Pepper Lunch) | 74,000 | 79,000 | 81,000 | n<4; brands<4 |
| pasta, plant-based (Burgreens) | 1 | 1 (Burgreens) | 60,000 | 60,000 | 60,000 | n<4; brands<4 |
| pasta, low-end street/kiosk (Detik 22 Jan 2025, approximate) | 5 | 5 (Casa Pasta, Fish Lab, Fish Streat, Halo Pasta, Sky Pasta) | 20,000 | 25,000 | 29,000 | ok |
| coffee, espresso + americano + long black | 5 | 3 (Burgreens, Fore Coffee, Pizza Marzano) | 22,000 | 25,000 | 35,000 | brands<4 |
| coffee, latte (cafe latte and signature lattes) | 8 | 3 (Fore Coffee, Pizza Marzano, Point Coffee) | 25,000 | 29,000 | 38,000 | brands<4 |
| coffee, signature milk-coffee (aren etc.) | 10 | 5 (Burgreens, Fore Coffee, Kopi Kenangan, Kopi Tuku, Tomoro Coffee) | 10,000 | 28,000 | 32,000 | ok |
| coffee, cappuccino (Pizza Marzano) | 1 | 1 (Pizza Marzano) | 38,000 | 38,000 | 38,000 | n<4; brands<4 |
| bowl, salads (Burgreens salads + Marzano salads) | 7 | 2 (Burgreens, Pizza Marzano) | 50,000 | 65,000 | 105,000 | brands<4 |
| bowl, rice bowls (Burgreens) | 5 | 1 (Burgreens) | 50,000 | 55,000 | 59,000 | brands<4 |
| bowl, smoothie bowls (Burgreens) | 3 | 1 (Burgreens) | 68,000 | 68,000 | 68,000 | n<4; brands<4 |
| functional_drink, protein shake (Burgreens) | 3 | 1 (Burgreens) | 52,000 | 52,000 | 52,000 | n<4; brands<4 |
| functional_drink, smoothie (Burgreens) | 3 | 1 (Burgreens) | 45,000 | 45,000 | 47,000 | n<4; brands<4 |
| functional_drink, herbal elixir (Burgreens) | 3 | 1 (Burgreens) | 27,000 | 27,000 | 35,000 | n<4; brands<4 |

Not comparable without adjustment: Burgreens prices exclude 10% tax and service charge ("++"), Fore media prices do not state a basis. Do not mix them in a district median.

## 7. Hypotheses touched (direction)

- H1 (CORSA placeholder at or above the median, premium): not testable; only one brand's bowl prices (IDR 50,000 to 68,000 before tax and service) and no Italian benchmark. Team B's bowl placeholder (85 to 110k) sits above every bowl price in this sample, but n=12 is from one plant-based brand: mixed or no evidence, not a percentile.
- H2 (coffee saturated by low-price chains): weak support. Fore Americano about 22,000 and signature Americano drinks 29,000 to 31,000 (Nov 2025 media); a Kontan promo (Jun 2026) states a normal price of Rp 38,000 for two Kopi Kenangan Mantan. Starbucks, Tomoro prices not obtained, so no latte median.
- H3, H4: not touched.

## Run 3b (P3-PRICE-b, 2026-10-17): new strategy, brand pages then dated media price articles

Collector: P3-PRICE-b. Rows `P3PB-01` to `P3PB-59` in `data/processed/price-ladder.csv` (59 rows). Temp source keys `P3PB-S1` to `P3PB-S12`. Access date for all sources: 2026-10-17. All pages were opened with curl and a browser user agent; dates below are the dates printed in each article's own byline block (sidebar and "related article" dates, many of them 2026, were ignored). Quotes are copied from the opened page text (Indonesian, verbatim, including the article's own spelling).

**Result against target.** 59 rows (target 40 or more), but only 38 are numeric item prices; the other 21 are ranges, per-person spend or promo redemption prices with `price_idr` left blank. Brands per category (new rows only, year = article date): see section R3b-5. The target of at least 4 brands per category with item-level list prices is met for coffee only; Italian/pasta has one Italian restaurant brand with item prices (Pizza Marzano 2025), and healthy bowls and salads has none new at item level (only Pizza Marzano restaurant salads); the healthy-bowl brand coverage is per-person ranges.

### R3b-1. Sources (one block per source)

### P3PB-S1
- Title: 99 Menu Pizza Marzano Lengkah beserta Harganya
- Publisher: IDN Times (Dining Guide)
- Author / editor line: Tamara Febriyanti (page footer: "written by our community writers ... reviewed by our editorial team")
- URL opened: https://www.idntimes.com/food/dining-guide/menu-pizza-marzano-c1c2-01-b9stm-lbb9kf
- Printed publication date: 17 Nov 2025, 11:20 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: community-writer content; no tax basis stated; photos credited to the brand Instagram)
- Access status: opened (HTTP 200)
- Rows: P3PB-01 to P3PB-18 (18 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S2
- Title: Daftar Harga Pizza Hut 2025, Ada Promo Menarik di Bulan Mei
- Publisher: Liputan6.com (Hot)
- Author / editor line: Fitriyani Puspa Samodra (Tim Redaksi: Fadila Adelin)
- URL opened: https://www.liputan6.com/hot/read/6024340/daftar-harga-pizza-hut-2025-ada-promo-menarik-di-bulan-mei
- Printed publication date: Diterbitkan 16 Mei 2025, 22:00 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (staff-written; says it compiled the prices from pizzahut.co.id on 16/5/2025, so the original is the brand site)
- Access status: opened (HTTP 200)
- Rows: P3PB-19 to P3PB-22 (4 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S3
- Title: 44 Menu Pepper Lunch 2025 Beserta Harganya
- Publisher: IDN Times (Dining Guide)
- Author / editor line: Putri Intan Nur Fauziah
- URL opened: https://www.idntimes.com/food/dining-guide/pepper-lunch-menu-1-00-cqkqh-cw26mv
- Printed publication date: 16 Jul 2025, 13:28 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: prices printed as rounded "ribuan"; no tax basis stated)
- Access status: opened (HTTP 200)
- Rows: P3PB-23 to P3PB-25 (3 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S4
- Title: 5 Resto Italia Lezat di Jakarta Buat Pilihan Makan Siang Spesial
- Publisher: detikFood (detik.com)
- Author / editor line: Riska Fitria
- URL opened: https://food.detik.com/resto-dan-kafe/d-8181724/5-resto-italia-lezat-di-jakarta-buat-pilihan-makan-siang-spesial
- Printed publication date: Selasa, 28 Okt 2025 12:00 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (staff-written; price ranges only, not item prices)
- Access status: opened (HTTP 200)
- Rows: P3PB-26 to P3PB-28 (3 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S5
- Title: 5 Pasta Murah di Jakarta, Harganya Mulai Rp 20.000
- Publisher: detikFood (detik.com)
- Author / editor line: Yenny Mustika Sari
- URL opened: https://food.detik.com/info-kuliner/d-7744610/5-pasta-murah-di-jakarta-harganya-mulai-rp-20-000
- Printed publication date: Rabu, 22 Jan 2025 17:00 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (staff-written; prices approximate, "-an")
- Access status: opened (HTTP 200)
- Rows: P3PB-29 to P3PB-33 (5 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S6
- Title: Harga Kopi Gula Aren di Fore, Tuku, Tomoro dan Gerai Kopi Lainnya
- Publisher: Liputan6.com (Lifestyle, Culinary)
- Author / editor line: Rizka Nur Laily Muallifa (Tim Redaksi: Nisa Mutia Sari)
- URL opened: https://www.liputan6.com/lifestyle/read/5999756/harga-kopi-gula-aren-di-fore-tuku-tomoro-dan-gerai-kopi-lainnya
- Printed publication date: Diperbarui 20 April 2025, 15:41 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: the article takes three of the four prices from Google Maps listings and one from an ordering app; only a "Diperbarui" date is printed)
- Access status: opened (HTTP 200)
- Rows: P3PB-34 to P3PB-37 (4 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S7
- Title: Menu Signature Fore dan Harganya untuk Sesi Ngopimu
- Publisher: IDN Times (Dining Guide)
- Author / editor line: Tamara Febriyanti (page footer: "written by our community writers ... reviewed by our editorial team")
- URL opened: https://www.idntimes.com/food/dining-guide/menu-signature-fore-c1c2-01-b9stm-2rb915
- Printed publication date: 19 Nov 2025, 11:50 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: community-writer content; size and tax basis not stated)
- Access status: opened (HTTP 200)
- Rows: P3PB-38 to P3PB-44 (7 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S8
- Title: 5 Promo Kopi Spesial Senin Akhir di Bulan Maret, Tomoro hingga Fore Coffee Hemat
- Publisher: MomsMoney (Kontan group)
- Author / editor line: Widya Oktaviana (Penulis and Editor); relays the brands' Instagram posts
- URL opened: https://momsmoney.kontan.co.id/news/5-promo-kopi-spesial-senin-akhir-di-bulan-maret-tomoro-hingga-fore-coffee-hemat
- Printed publication date: Senin, 30 Maret 2026 | 09:44 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak for list prices: a promo article; the "normal" price is an aside)
- Access status: opened (HTTP 200)
- Rows: P3PB-45 to P3PB-45 (1 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S9
- Title: Promo Pizza Hut Tebus Murah 1-31 Agustus 2025, Diskon 17% untuk 17 Menu Tiap Harinya
- Publisher: MomsMoney (Kontan group)
- Author / editor line: Widya Oktaviana (Penulis and Editor); relays the Pizza Hut Indonesia Instagram post
- URL opened: https://momsmoney.kontan.co.id/news/promo-pizza-hut-tebus-murah-1-31-agustus-2025-diskon-17-untuk-17-menu-tiap-harinya
- Printed publication date: Rabu, 06 Agustus 2025 | 09:19 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (promo article; prices are redemption prices, see notes)
- Access status: opened (HTTP 200)
- Rows: P3PB-46 to P3PB-49 (4 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S10
- Title: 10 Tempat Makan Salad di Jakarta, Banyak Pilihan Dressing
- Publisher: IDN Times (Dining Guide)
- Author / editor line: Kim Caca (byline) / Penulis: Nisrina Putri Dayani (footer)
- URL opened: https://www.idntimes.com/food/dining-guide/tempat-makan-salad-di-jakarta-00-r95nh-598f7h
- Printed publication date: 24 Apr 2025, 19:50 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: "mulai dari ... per orang" ranges, not item prices; no tax basis)
- Access status: opened (HTTP 200)
- Rows: P3PB-50 to P3PB-57 (8 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S11
- Title: 10 Tempat Makan di Senayan City yang Wajib Kamu Coba
- Publisher: IDN Times (Dining Guide)
- Author / editor line: Fasrinisyah Suryaningtyas
- URL opened: https://www.idntimes.com/food/dining-guide/rekomendasi-tempat-makan-di-senayan-city-00-mk1yf-vz2mhp
- Printed publication date: 02 Feb 2025, 13:35 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (weak: one price range per venue)
- Access status: opened (HTTP 200)
- Rows: P3PB-58 to P3PB-58 (1 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### P3PB-S12
- Title: Jelajahi 11 Tempat Makan Enak di Foodcourt Senayan City, Kuliner Lokal hingga Internasional
- Publisher: Liputan6.com (Lifestyle)
- Author / editor line: Mabruri Pudyas Salim (Tim Redaksi: Rizky Mandasari)
- URL opened: https://www.liputan6.com/lifestyle/read/6173407/jelajahi-11-tempat-makan-enak-di-foodcourt-senayan-city-kuliner-lokal-hingga-internasional
- Printed publication date: Diterbitkan 01 Oktober 2025, 15:00 WIB (read from the article's own byline block)
- Access date: 2026-10-17
- Proposed tier: 3 (staff-written; one per-person range)
- Access status: opened (HTTP 200)
- Rows: P3PB-59 to P3PB-59 (1 rows)
- Quotes: in the `snippet` column of the CSV rows above (verbatim Indonesian).

### R3b-2. Opened, no row (reason)

| Source | URL opened | Finding | Why no row |
| --- | --- | --- | --- |
| Tomoro Coffee Indonesia | https://www.tomoro-coffee.id/ (HTTP 200, 2.7 KB) | Script shell, no menu or prices | No prices |
| Starbucks Indonesia | https://www.starbucks.co.id/ (HTTP 200) | No prices on the page (beverage pages checked in the first pass) | No prices |
| Kopi Kenangan | https://www.kopikenangan.com/menu | HTTP 404; home page has no prices (first pass) | No prices |
| SaladStop! Indonesia | https://saladstop.co.id/ (HTTP 200) and /menu (HTTP 404) | No prices in the HTML | No prices |
| Crunchaus | https://www.crunchaus.com/ | Login panel ("Selamat Datang Di Admin Panel") | Not a menu |
| Boga Group | https://www.bogagroup.com/ | Domain for sale (HugeDomains) | Not the group's site; Pepper Lunch, Bensu and Kimukatsu official menu pages were not located |
| Pizza Hut Indonesia | https://www.pizzahut.co.id/menu (HTTP 200, 11 KB) | Script shell ("Order Now!"), menu loads from an API (not pursued, as instructed) | No prices; the Liputan6 article of 16 May 2025 (P3PB-S2) relays the brand site |
| Pizza Marzano Indonesia | https://www.pizzamarzano.co.id/menu/pasta/ and /menu/main-menu/ | Pasta page is a single PNG image of a dish; menu pages list names only | No prices on the official site (only the April 2021 PDF, out of window). The 2025 prices come from IDN Times (P3PB-S1) |
| Domino's Indonesia | https://www.dominos.co.id/menu | HTTP 403 | Blocked, not bypassed |
| Union Group | https://uniongroup.co.id and https://www.uniongroup.co.id | No connection (curl 000). https://uniongroup.com answers but is a textile group (Union Limited), not the restaurant group | No menu located |
| Ismaya | https://www.ismaya.com/ (HTTP 200, 634 KB) | No prices and no menu PDF links found | No prices |
| Four Seasons, hotel and premium menu PDFs (SCBD, Senopati, Kuningan) | web search only | Searches for downloadable menu PDFs returned listicles and blogs (NOW! Jakarta, Chope, Nibble, Lemon8, Wanderlog), no PDF | No tier 1-3 priced menu found; strategy (3) yielded no rows |
| Kontan MomsMoney, Pizza Hut Extra Deals 8 Jul 2025 | https://momsmoney.kontan.co.id/news/promo-pizza-hut-extra-deals-7-20-juli-regular-pizza-pastarice-cuma-rp-99000 | "1 Pan Regular Pizza + 1 Pasta/Rice (Rp 99.000)" and "1 Pasta + 1 Rice (Rp 89.000)" | Set offers, not item prices |
| Kontan MomsMoney, 9.9 promos 9 Sep 2026 | https://momsmoney.kontan.co.id/news/9-promo-99-minuman-kekinian-2026-diskon-hemat-di-tomoro-koi-th%C3%A9-hingga-starbucks | Bundle and promo prices ("dari harga normalnya Rp 60.000" for two drinks) | Bundles, no single-item normal price |
| Kontan MomsMoney, payday promos 26 Jan 2026 | https://momsmoney.kontan.co.id/news/7-promo-kopi-payday-januari-2026-nikmati-diskon-hingga-70-di-starbucks | Starbucks two drinks Rp 29.000 each with BCA, Rp 33.000 each otherwise (promo, 26-28 Jan 2026) | Promo price, size not stated; context only |

### R3b-3. Historical / pre-window context (opened, printed date before 2024-10-16, not in the CSV)

- IDN Times "55 Menu Kopi Kenangan 2025 Lengkap" (URL slug says 2025; the printed byline date is 25 Sep 2023, 15:11 WIB; the title shows 2024 and 2025 variants). Not used.
- IDN Times "33 Menu di Starbucks Paling Favorit Beserta Harganya" 23 Aug 2023; "7 Menu Starbuck di Bawah 50 Ribu" 10 Mar 2023. Not used.
- IDN Times "Daftar Menu Lengkap Tomoro Coffee" 16 Jan 2024; "Menu Fore Coffee Beserta Harganya" 02 Nov 2023; "Daftar Menu Djournal Coffee" 27 Oct 2023; "55 Daftar Menu Excelso" 13 Jun 2023.
- IDN Times "64 Menu Pizza Hut 2024" 27 Apr 2024; "47 Menu Domino's Pizza 2024" 29 Apr 2024; "Daftar Menu Sec Bowl" 30 Sep 2024 (16 days before the window starts); "4 Tempat Makan Sehat di Kawasan SCBD" 13 Sep 2024; "7 Restoran Vegetarian di Jakarta Selatan" 13 Nov 2023 (displayed date); "5 Rekomendasi Restoran Healthy Food Terenak di Jaksel" 24 Aug 2021; "Anti Gagal Diet, 5 Rekomendasi Restoran Sehat" 16 Dec 2021.
- Not opened (snippet-only from search results, so not used as figures): Kompas "6 Tempat Makan Salad" 03 Jan 2024 (Honu Central salads Rp 65.000 to 85.000), Kompas Chipotle series SaladStop June 2023, Liputan6 SaladStop warm protein bowls 2019 (Rp 80.000 to 110.000). All pre-window.

### R3b-4. Leads only (tier 4 or undated; not in the CSV, not to be used as figures)

From search-result text only, not opened: Majoo (Kopi Kenangan 2026, Starbucks "estimasi" Sept 2025: Caffe Latte Tall Rp 52.000, Grande Rp 57.000); Tokopedia blog (Pizza Hut, Pepper Lunch 2026 list, Kimukatsu Tokyo Ball Katsu Rp 64.000, SaladStop bowl about Rp 95.000, undated); Mamikos 2024 (Starbucks Americano Tall Rp 34.000); Shopee Inspirasi (Point Coffee, Starbucks 2023); Kumparan (Excelso, Tomoro, Starbucks, Kopi Kenangan 2024; fetch returned a blank page); Nibble.id, Lemon8 and Wanderlog (The Garden Osteria Tagliatelle Bistecca 195K, Acta Brasserie Fettuccine Mushroom 145K, William's Creamy Mushroom Spaghetti 115K; Osteria Gia Spaghetti Aglio Olio Rp 160.000 and Burro e Pepe Rp 210.000 from an undated IDN Times article); Time Out, Mojok (undated). The Tempo Starbucks lists (HTTP 403 in the first pass) were not retried. These show where Italian fine-dining pasta sits (Rp 115.000 to 225.000) but cannot be stored as figures.

### R3b-5. Brands per category (Run 3b rows, year = printed article year)

| Category | Brands with numeric item prices (n rows) | Brands with range / spend / promo only | Meets 4 brands? |
| --- | --- | --- | --- |
| (a) Italian / pasta mains | Pizza Marzano 2025 (11 pasta); Pepper Lunch 2025 (3, Japanese-style teppan pasta, rounded "ribuan"); 5 low-end street pasta kiosks 2025 (Casa Pasta, Sky Pasta, Halo Pasta, Fish Streat, Fish Lab; approximate) | Pizza Hut Indonesia 2025 (3 pasta ranges); Pizza Hut Ristorante 2025 (Pasta Con Bistecca, Spicy Arrabbiata, promo); Gior Jakarta, Bastian, Rosa Osteria 2025 (ranges or spend) | Only 1 Italian restaurant brand with item prices (Pizza Marzano). 4 or more counting the street kiosks, which are not comparable Italian restaurants. |
| (b) Coffee | Pizza Marzano 2025 (espresso, americano, latte, cappuccino); Fore Coffee 2025 (7 signature items; Americano rows already in P3PR-025 to 030); Kopi Tuku 2025, Tomoro Coffee 2025, Kopi Kenangan 2025 (gula aren regular, one row each); Point Coffee 2026 (1 row, weak) | none | Yes, 6 brands (but only Pizza Marzano and Fore give espresso, americano or latte list prices; the rest are one signature milk-coffee each) |
| (c) Healthy bowls and salads | Pizza Marzano 2025 (3 restaurant salads) | Pizza Hut (salad range) 2025; Pizza Hut Ristorante (2 Caesar salads, promo) 2025; per-person "from" spend 2025 for Bluezone, Hijoo, Kalegreen, Salad Hut, SaladStop!, Salam Salads, Serasa Salad Bar, The Roots (IDN Times 24 Apr 2025); SaladStop! ranges (IDN Times 02 Feb 2025, Liputan6 01 Oct 2025) | No at item level (the only healthy-bowl chain with item prices remains Burgreens from the first pass); yes at the level of 8 brands with per-person "from" spend |

### R3b-6. Findings that bear on the price position (facts separate from reading)

Facts (all tier 3, dated in the window):
- Pizza Marzano Jakarta menu list, IDN Times 17 Nov 2025: pasta Rp 69.000 (Aglio Olio) to Rp 109.000 (Fettuccine Salmon Pesto, Orecchiette, Lasagna), median Rp 95.000 over 11 pasta; Cafe Latte Rp 38.000, Cafe Americano Rp 35.000, Espresso Rp 30.000; restaurant salads Rp 60.000 to Rp 105.000. Tax and service basis not stated.
- Fore Coffee signature lattes Rp 29.000 to Rp 33.000 (IDN Times 19 Nov 2025); Fore kopi susu gula aren about Rp 27.000 at Cipete versus Tomoro about Rp 18.000, Kopi Kenangan about Rp 23.000 and Kopi Tuku about Rp 10.000 (Liputan6 20 Apr 2025, Google Maps and app prices).
- Italian fine dining ranges (detikFood 28 Oct 2025): Gior Jakarta main dishes Rp 100.000 to Rp 250.000; Rosa Osteria (Senopati) average from Rp 200.000 per person.
- Low-end pasta floor: about Rp 20.000 to Rp 29.000 (detikFood 22 Jan 2025).

Reading (collector's analysis, not sourced data): against the Team B placeholders (pasta Rp 82.000 to 135.000, latte Rp 50.000, bowl Rp 85.000 to 110.000), the pasta placeholder overlaps the Pizza Marzano item range (Rp 69.000 to 109.000) and the lower end of Italian fine-dining mains; the latte placeholder (Rp 50.000) is above every latte list price found (maximum Rp 38.000 at Pizza Marzano, Rp 33.000 at Fore); the bowl placeholder is above every bowl and salad item found (maximum Rp 105.000 for a Pizza Marzano restaurant salad, Rp 68.000 for Burgreens bowls). Starbucks and Tomoro list prices for latte could not be obtained for the window, so the coffee-chain upper end (Starbucks) is missing and the latte reading is weak. This is direction only (H1: mixed for pasta, premium-looking for latte and bowl); n and brand counts are too small for a percentile.

Disconfirming or conflicting evidence recorded: SaladStop! Senayan City is given as Rp 25.000 to 125.000 (IDN Times, 02 Feb 2025), Rp 100.000 per person from (IDN Times, 24 Apr 2025) and Rp 100.000 to 200.000 per person (Liputan6, 01 Oct 2025): three different statements for the same venue. Pizza Hut Ristorante Pasta Con Bistecca appears as Rp 105.000 (Kontan, 10 Jun 2025 anniversary promo, first pass) and Rp 102.000 (Kontan, 06 Aug 2025 redemption promo): both promos, no list price. Liputan6 Pizza Hut prices (Rp 60.000 to 72.727) are far below Pizza Marzano and Ristorante, so "pasta" spans Rp 20.000 to Rp 109.000 in the item-level rows before any premium Italian venue is added.

### R3b-7. Gaps and blocked hosts

- Blocked or unusable hosts (not bypassed): dominos.co.id (HTTP 403), tempo.co (HTTP 403, first pass), uniongroup.co.id (no connection), pizzahut.co.id menu (API only), tomoro-coffee.id and saladstop.co.id (no prices in HTML), kumparan.com (blank page to curl). Grab and GoFood were not retried, as instructed.
- No tier 1-3 priced menu for: Starbucks, Kopi Kenangan, Tomoro (normal list), SaladStop!, Crunchaus, Union Group, Ismaya, Boga Group (Bensu, Kimukatsu), hotel menus in SCBD, Senopati or Kuningan.
- No outlet-level split by district for most rows (brand-wide lists). Pizza Marzano and Pizza Hut tax and service basis unknown for 2025.
- Primary-research route (plan section 10): photograph menus and capture app prices on the Jakarta visit for the missing chains.
