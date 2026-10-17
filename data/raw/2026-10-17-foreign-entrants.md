# Plan 3, task 2f: foreign F&B entrants and exits in Jakarta (findings, run 2)

Agent: P3-B-entrants. Access date for every source: 2026-10-17. Dataset: `data/processed/foreign-entrants.csv` (29 rows, 30 columns: the run-2 contract columns plus `brand, origin, entry_year, mode, partner, status, status_date, format_price, reasons_fact, reasons_commentary, window_class`). Row IDs `P3B-01` to `P3B-29`. `register_id` and `verification` are blank for the registrar and the verifier.

Owner decision applied: exits older than 2 years (before 2024-10-17) are historical context only and are never part of the base rate. They carry `window_class = HISTORICAL-NOT-IN-BASE-RATE`.

Fact versus commentary: the `reasons_fact` column holds only reasons stated by the company or quoted in the cited article; `reasons_commentary` holds attributed commentary (labelled COMMENTARY) or my own reading (labelled ANALYST).

Network: curl with a browser user agent opened all hosts used except RRI (Cloudflare challenge) and Bisnis.com (403). WebFetch was not used. Downloaded PDFs (two RBA investor decks) were kept in the scratchpad and are not committed.

## Result summary

| window_class | rows | meaning |
| --- | --- | --- |
| IN-WINDOW | 17 (P3B-01 to 17) | brand active or contracting in 2024-10-17 to 2026-10-17 reporting |
| PRE-WINDOW-STALE | 3 (P3B-18, 19, 23) | entry or last count published before 2024-10-16; shown because no newer free tier 1-3 count was found |
| ANNOUNCED-NOT-ENTERED | 2 (P3B-20, 21) | Saizeriya (Japan, Italian-style, own subsidiary due Dec 2026); Tim Hortons (plan only) |
| NOT-ENTERED | 1 (P3B-22) | Blue Bottle |
| HISTORICAL-NOT-IN-BASE-RATE | 6 (P3B-24 to 29) | Carl's Jr., Texas Chicken (CSMI), Hard Rock Cafe, Fish & Co., Marché Mövenpick, Karen's Diner |

In-window base rate (n shown, no percentage because n is below 10 for any defined group):
- Full exits from Indonesia documented in the window: 0 of 17 in-window cases. Not statistically meaningful.
- Contracting in the window (outlet count down or closures stated): 4 (Burger King, Starbucks, KFC, Mixue), all mass or mid-tier chains with US or Chinese origin; none is a premium-casual or Italian format.
- Expanding or newly entered in the window: 11 (Paris Baguette, CHAGEE, ZUS, Flash Coffee, Pizza Marzano, Domino's (provisional), Fuglen, Harlan + Holden, Hario, Cafe Kitsune, Kurasu).
- Stable or recovering: 2 (Popeyes flat but loss-making, Pizza Hut).

## Findings that matter for decisions

1. No premium-casual, café, Italian or healthy-bowl brand with a documented full Jakarta exit was found in the window. The exits we can document are old (2020 to 2023) and are fast-food or themed-dining brands. The survival base rate for CORSA's format therefore cannot be computed from this sample (n too small, and the sample is biased: closures of small foreign cafés are rarely reported).
2. The contracting brands are mass-tier QSR (Burger King 176 to 138 stores Mar 2023 to Dec 2025; KFC 715 to 690 in 2025; Starbucks closed 16 and opened 11 in H1 2025; Mixue closed 428 overseas stores in 2025, most in Indonesia and Vietnam). Stated causes are company-level: persistent losses, falling traffic, boycott sentiment, falling purchasing power, saturation. Boycott is one of several causes (KFC names Covid, boycott and purchasing power; Pizza Hut, with the same US origin, returned to profit in FY2025).
3. Foreign premium cafés in the target districts exist and price above CORSA's latte placeholder (IDR 50,000): Fuglen from Rp 60.000++ (SCBD), Harlan + Holden Rp 63.000++ (Plaza Indonesia, Kota Kasablanka, Senayan City), Hario Cafe from Rp 80.000++ (Kuningan), Cafe Kitsune about Rp 50.000++ (SCBD), Kurasu from Rp 40.000++ (Melawai). Prices are media-reported ranges before tax and service, not menu captures; Plan 3's price-ladder agents must replace them with menu captures.
4. Partner structure (H6): every expanding foreign brand with a stated partner has a large Indonesian conglomerate partner (Erajaya for Paris Baguette and CHAGEE, MAP for Pizza Marzano, Kapal Api for ZUS). But the contracting Starbucks (MAP Boga) and KFC (FAST) also have strong local partners. The one documented exit tied to a weak partner is Texas Chicken with CSMI (2023, historical, outside the rate). So the data do not show that a strong partner prevents contraction; it is consistent with strong partners being necessary but not sufficient. Verdict on H6: inconclusive (mixed), n too small.
5. New Italian-style foreign entrant: Saizeriya (Japan) announced a wholly owned Indonesian subsidiary, to be set up December 2026, with value pricing. It is the only Italian-style foreign entry signal found for 2026 and sits below CORSA's price tier.
6. CHAGEE grew from 1 store (April 2025) to 36 stores in Greater Jakarta (by March 2026) with an Erajaya JV; the GM names queues, repeat visits and social sharing as triggers and says Jakarta stores are used for hours of work or study. Flash Coffee also moved to larger sit-down stores (120-140 sqm) for work. Both support a 'third place' format reading, but both are beverage brands.
7. Disconfirmed owner hints: no Pizza Marzano exit found (23rd Indonesian restaurant opened Sept 2025); Domino's 'hundreds of closures' in 2025 refer to the Australian-listed Domino's Pizza Enterprises worldwide (233 in Japan), and the opened CNBC article does not mention Indonesia, while Domino's Indonesia reportedly opened its 250th outlet on 2026-06-28 (provisional, RRI blocked); the Burger King 'permanent closure' viral claim was rated untrue by Kompas fact-check on 2024-06-11 (pre-window) and Burger King still had 138 stores at Dec 2025.

## Checked, no Jakarta entry found (not rows, negative searches only)

Negative web searches are not proof of absence; verifiers should re-check.
- Joe & The Juice: two searches found nothing on Indonesia (results were about Jamba Juice and other markets).
- Shake Shack: no Indonesian opening or licence found; licensed partners found are for Vietnam, Thailand, Malaysia and others.
- Gordon Ramsay restaurants: no Jakarta restaurant or franchise found.
- Eataly: no Jakarta store found; Italian restaurant lists name independents and local groups (Osteria GIA is a Jakarta-born brand of the ISMAYA Group, opened in Surabaya on 2024-11-12, so it is not a foreign entrant).
- Luckin Coffee: no Indonesian outlet found; a search lead (not opened) refers to a coconut supply partnership with Banggai regency, not retail.
- Tim Hortons: plan only (P3B-21).
- Pizza Marzano exit, Burger King exit, Domino's exit: not found as exits (see above).
- Lotteria (exit 29 Jun 2020) and Marché Mövenpick (Plan 3 draft: 30 Sep 2020): historical; Lotteria was only seen in a WebSearch result summary (Wikipedia), so no row.

## Gaps

- % Arabica and Cotti Coffee: no 2024-26 Indonesian outlet count in free tier 1-3 sources found (rows P3B-18, 19 are pre-window and flagged stale).
- Entry mode and partner are not stated for most foreign cafés (Fuglen, Harlan + Holden, Hario, Kitsune, Kurasu).
- No outlet counts split by district or by Jakarta for the chains; most counts are Indonesia-wide.
- Bisnis.com articles (403 for our client) were not opened; Bisnis items seen only as WebSearch results are not used as figures.
- Reasons for Carl's Jr., Hard Rock Cafe, Fish & Co. and Marché Mövenpick exits are not documented in the opened pages.
- Flash Coffee: last opened actual store count is 67 (September 2024, pre-window); the 2025-26 numbers are targets only.

## Hypotheses touched

- H6 (partner protects): mixed / inconclusive, see finding 4.
- H5 (mid-market under pressure): supports for mass QSR (KFC, Burger King, Starbucks, Mixue), disconfirms for Pizza Hut (profit FY2025) and for expanding Italian casual (Pizza Marzano).
- H2 (coffee saturated by low-price chains): ZUS and Flash entering/expanding with value or mid positioning points to more crowding; premium foreign cafés at 60-80k exist, so a premium tier is occupied.
- H3 (Italian/bowl less saturated): supports weakly; the only foreign Italian-style entrants are Pizza Marzano (existing) and Saizeriya (planned, value-priced); Oakberry is Bali only.

## Historical / pre-window context

Run 2 fix-up (2026-10-17). Six rows failed the date rule (source printed before 2024-10-16) in the run-2 verification (`tasks/2026-10-17-run2-verification-e.md`). They were removed from `data/processed/foreign-entrants.csv` and listed in `data/processed/2026-10-16-run1-dropped-rows.csv` (verdict DATE-FAIL). They are kept here as context only and are not part of the base rate. Content of each was verified against the opened page (relay).

| row | brand | printed date | what the page says | register |
| --- | --- | --- | --- | --- |
| P3B-18 | % Arabica (Japan) | 2023-12-08 (World Coffee Portal) | operates seven outlets across Indonesia; fifth in the capital | CMP-041 |
| P3B-19 | Cotti Coffee (China) | 2023-08-21 (Verdict Foodservice) | opened an outlet in Jakarta, Kuningan City Mall | CMP-042 |
| P3B-21 | Tim Hortons (Canada) | 2024-07-15 (World Coffee Portal) | "preparing to open stores in Indonesia" (passing remark; no opening found) | CMP-044 |
| P3B-23 | Oakberry (Brazil) | 2023-10-18 (Inside Retail Australia) | Bali expansion, two stores announced for the next month; no Jakarta | CMP-046 |
| P3B-24 | Carl's Jr. (US) | 2023-12-22 (Kontan) | closed all outlets 31 Dec 2023, more than 24 outlets; second source with passing date: detikFinance 2025-08-22 (CMP-050) | CMP-047 |
| P3B-25 | Texas Chicken (US, operator CSMI) | 2023-08-19 (Okezone) | franchise ended 14 Mar 2023, closure from 28 Feb 2023, all restaurants closed | CMP-048 |

Wording corrections from the verification: the "Domino's exit disconfirmed" claim (finding 7) is unsupported, because the opened CNBC article never mentions Indonesia and the 250-store count is blocked; the "Pizza Marzano exit disconfirmed" claim is only partly supported (one opened Sep 2025 article, no later check). Read both as "no exit evidence found". The Result summary counts above predate the removal (PRE-WINDOW-STALE and HISTORICAL rows now remain only as P3B-26 to 29 in the CSV).

## Sources

Tier key (CLAUDE.md §5): 1 = official company or regulator document, 3 = reputable trade or news outlet with editorial standards. Quotes are short extracts from the opened page.

### P3B-S1
- Title: Paris Baguette Strengthens Its Presence in Indonesia, Continuing Growth into 2026
- Publisher: Erajaya (PT Erajaya Swasembada Tbk), company news release
- URL opened: https://erajaya.com/news/paris-baguette-perkuat-kehadiran-di-indonesia-lanjutkan-momentum-pertumbuhan-di-2026
- Printed date: 21.01.2026 (Jakarta, January 21th, 2026)
- Tier 1 (company release; self-reported, promotional)
- Access: opened
- Quotes: "Paris Baguette Indonesia marked the opening of its 20th store at Lotte Mall Jakarta"; "Paris Baguette Indonesia will operate a total of 23 stores nationwide in early 2026"

### P3B-S2
- Title: Paris Baguette Indonesia Marks New Chapter with Halal Certification Across All Stores
- Publisher: Erajaya, company news release
- URL opened: https://erajaya.com/news/paris-baguette-resmi-raih-sertifikasi-halal-untuk-seluruh-gerai-di-indonesia
- Printed date: 21.05.2026
- Tier 1 (company release)
- Access: opened
- Quotes: "across all 23 of its outlets in Jakarta, Tangerang, Depok, Medan, and Surabaya"; "a premium bakery-café brand from South Korea"; "As we enter Paris Baguette's fifth year in Indonesia"; "50% off with a minimum purchase of IDR 150,000"

### P3B-S3
- Title: Zus Coffee brews up Indonesia expansion
- Publisher: Inside Retail Asia
- URL opened: https://insideretail.asia/2026/05/zus-coffee-brews-up-indonesia-expansion/
- Printed date: May 28, 2026
- Tier 3 (trade press)
- Access: opened
- Quotes: "Malaysian coffee chain Zus Coffee has entered Indonesia, opening its first Jakarta store"; "The debut outlet at Puri Indah Mall is operated in partnership with Kapal Api Group"

### P3B-S4
- Title: Gandeng Kapal Api, ZUS Coffee Resmi Hadir di Jakarta
- Publisher: JPNN.com
- URL opened: https://www.jpnn.com/news/gandeng-kapal-api-zus-coffee-resmi-hadir-di-jakarta
- Printed date: Rabu, 03 Juni 2026 (14:06 WIB)
- Tier 3
- Access: opened
- Quotes: "ZUS Coffee resmi membuka gerai pertamanya di Indonesia yang berlokasi di Puri Indah Mall, Jakarta"

### P3B-S5
- Title: CHAGEE announces Grand Opening of First Store in Indonesia
- Publisher: Erajaya, company release
- URL opened: https://www.erajaya.com/news/chagee-umumkan-pembukaan-gerai-pertama-di-indonesia
- Printed date: 11.04.2025
- Tier 1 (company release)
- Access: opened
- Quotes: "CHAGEE's expansion in Indonesia is driven by its joint venture with Erajaya's subsidiary PT Era Boga Nusantara under Erajaya Food & Nourishment (EFN) division"; "premium tea-drinking experience"

### P3B-S6
- Title: Erajaya Bawa CHAGEE ke Indonesia, Tawarkan Teh Premium ala Teapresso
- Publisher: Kontan (industri.kontan.co.id)
- URL opened: https://industri.kontan.co.id/news/erajaya-bawa-chagee-ke-indonesia-tawarkan-teh-premium-ala-teapresso
- Printed date: Jumat, 11 April 2025 / 14:37 WIB
- Tier 3
- Access: opened
- Quotes: "Gerai pertama CHAGEE telah hadir di tiga lokasi strategis: PIK Avenue, Mall of Indonesia (MOI), dan fX Sudirman" (conflicts with S5, which says MOI and fX Sudirman follow in the coming weeks)

### P3B-S7
- Title: A New Chapter Begins: CHAGEE Celebrates Its Grand Opening in Bali
- Publisher: Erajaya, company release
- URL opened: https://erajaya.com/news/perjalanan-baru-dimulai-chagee-resmikan-gerai-perdana-di-bali
- Printed date: 27.03.2026 (body text says "27 to 29 March 2025": typo in source)
- Tier 1 (company release)
- Access: opened
- Quotes: "After debuting in Indonesia at PIK Avenue in April 2025 and growing to 36 stores across Greater Jakarta, Bali marks CHAGEE's first step into a new city."

### P3B-S8
- Title: CHAGEE's Indonesia playbook: scaling tea culture across Jakarta and Bali
- Publisher: Marketing-Interactive (interview with the CHAGEE Indonesia GM)
- URL opened: https://www.marketing-interactive.com/chagee-s-indonesia-playbook-scaling-tea-culture-across-jakarta-and-bali
- Printed date: two datePublished tags, 2026-09-30 and 2026-10-07 (page itself shows no visible date in the extract)
- Tier 3
- Access: opened
- Quotes: "Indicators such as queues, repeat visits, social sharing told us the concept was resonating beyond novelty. By the time we reached 36 stores across Greater Jakarta"; "In Jakarta, we see a lot of customers using the space to work or study."

### P3B-S9
- Title: Flash Coffee Ekspansi 130 Gerai, Ubah Konsep dan Rambah Kota Baru
- Publisher: Kontan Momsmoney
- URL opened: https://momsmoney.kontan.co.id/news/flash-coffee-ekspansi-130-gerai-ubah-konsep-dan-rambah-kota-baru
- Printed date: Minggu, 27 Juli 2025 | 09:05 WIB
- Tier 3
- Access: opened
- Quotes: "menargetkan jumlah gerai pada akhir tahun ini akan mencapai 80 toko dan pada tahun depan akan bertumbuh menjadi 130 toko pada tahun 2026"; "Saat ini Flash Coffee bertransformasi menjadi kedai kopi premium"; store area "40 meter persegi, sekarang diperluas hingga 120-140 meter persegi"

### P3B-S10
- Title: Flash Coffee Doubling Down on Indonesia
- Publisher: Retail & Leisure International (RLI)
- URL opened: https://www.rli.uk.com/flash-coffee-doubling-down-on-indonesia/
- Printed date: 03/09/2024 (BEFORE the 2024-10-16 window: used only as labelled pre-window context)
- Tier 3
- Access: opened
- Quotes: "following the closure of Flash Coffee in other Asian markets and the sale of its brand in Thailand as a franchise"; "The coffee chain now operates 67 stores"; "Launched in Singapore in 2020"

### P3B-S11
- Title: Restaurant Brands Asia Limited, Q3 FY26 investor presentation (Indonesia pages)
- Publisher: Restaurant Brands Asia Ltd (listed in India), filed with BSE and NSE
- URL opened: https://nsearchives.nseindia.com/corporate/RBA_03022026182049_Finalupload.pdf (PDF, read with pdftotext, kept in scratchpad)
- Printed date: February 3, 2026
- Tier 1 (company filing to the exchange)
- Access: opened
- Quotes: "Store Count 147 143 139 136 138 25 25 25 25 25 172 168 164 161 163"; "Burger King Store EBITDA improved by IDR 10 Billion; whereas losses in Popeyes widened by IDR 9 Billion in 9M FY26 over previous year"; "Sept'25 impacted by civil unrest"; "RBA to be acquired by Inspira Global"

### P3B-S12
- Title: Restaurant Brands Asia Limited, Q4 FY23 investor presentation (Indonesia pages)
- Publisher: Restaurant Brands Asia Ltd, filed with BSE and NSE
- URL opened: https://bseindia.com/xml-data/corpfiling/AttachHis/3b5e6802-e9ac-4242-a68f-77bfe444f46e.pdf
- Printed date: May 17, 2023 (PRE-WINDOW; used as a labelled long-run store-count point)
- Tier 1
- Access: opened
- Quotes: "186 store count as at 31st March 2023 (176 Burger King and 10 Popeyes)"; "Launched with global record for strongest opening day for a new country entry"; "Opened 10 stores till date"

### P3B-S13
- Title: MAP Boga (MAPB) Targetkan Buka 40 Gerai Starbucks di 2025, Fokus di Wilayah Ini
- Publisher: investortrust.id
- URL opened: https://investortrust.id/market/71087/map-boga-mapb-targetkan-buka-40-gerai-starbucks-di-2025-fokus-di-wilayah-ini
- Printed date: SENIN, 30 JUNI 2025, 19.02 WIB
- Tier 3 (Dewan Pers verified outlet)
- Access: opened
- Quotes: "Pada semester I-2025, MAPB telah membuka 11 gerai baru, namun juga menutup 16 gerai yang mayoritas berada di kota-kota tier dua"; "terutama akibat penurunan trafik dan dampak dari sentimen boikot"; "Dulu kami bisa bangun hingga 80 gerai setahun. Tahun ini, targetnya hanya sekitar 40 gerai"

### P3B-S14
- Title: Tutup 20 Gerai & Pangkas 1.041 Karyawan, Rugi KFC (FAST) Turun 57%
- Publisher: CNBC Indonesia
- URL opened: https://www.cnbcindonesia.com/market/20251103181906-17-681892/tutup-20-gerai-pangkas-1041-karyawan-rugi-kfc--fast--turun-57
- Printed date: 04 November 2025 07:45
- Tier 3
- Access: opened
- Quotes: "Hingga 30 September 2025, perseroan mengoperasikan 695 gerai, turun dibandingkan posisi 31 Desember 2024 yang sebanyak 715 gerai."

### P3B-S15
- Title: KFC Blak-blakan Soal Kondisi Bisnis: Covid, Boikot & Daya Beli Turun
- Publisher: CNBC Indonesia (reporting FAST's public expose of 2 Oct 2025)
- URL opened: https://www.cnbcindonesia.com/market/20251006112734-17-673167/kfc-blak-blakan-soal-kondisi-bisnis-covid-boikot-daya-beli-turun
- Printed date: 06 October 2025 13:30
- Tier 3
- Access: opened
- Quotes: "Sampai bulan September 2025, Perseroan sudah menutup 19 gerai"; "covid ... boikot di tahun 2023 sampai 2024 ... penurunan daya beli dari masyarakat"; "Tercatat sepanjang 2024, total gerai yang ditutup oleh KFC mencapai 55 gerai"

### P3B-S16
- Title: KFC Franchisee in Indonesia Cuts 25 Locations, Reduces Workforce
- Publisher: Jakarta Globe
- URL opened: https://jakartaglobe.id/business/kfc-franchisee-in-indonesia-cuts-25-locations-reduces-workforce
- Printed date: April 19, 2026 | 2:10 pm
- Tier 3
- Access: opened
- Quotes: "FAST operated 690 KFC outlets as of Dec. 31, 2025, down from 715 outlets a year earlier."

### P3B-S17
- Title: Beda Nasib Pizza Hut & KFC: Satu Untung, Satu Buntung
- Publisher: detikFinance
- URL opened: https://finance.detik.com/bursa-dan-valas/d-8453630/beda-nasib-pizza-hut-kfc-satu-untung-satu-buntung
- Printed date: Selasa, 21 Apr 2026 07:30 WIB
- Tier 3 (already registered as BEH-052)
- Access: opened
- Quotes: "Perseroan membukukan laba Rp 24,75 miliar sepanjang tahun 2025, dari rugi bersih sebesar Rp 72,83 miliar pada 2024."

### P3B-S18
- Title: Mixue Tutup 428 Gerai, Indonesia-Vietnam Paling Terdampak
- Publisher: detikFinance
- URL opened: https://finance.detik.com/berita-ekonomi-bisnis/d-8466651/mixue-tutup-428-gerai-indonesia-vietnam-paling-terdampak
- Printed date: Rabu, 29 Apr 2026 12:16 WIB
- Tier 3
- Access: opened
- Quotes: "Mixue menutup 428 gerai sepanjang 2025 sebagai upaya untuk meningkatkan operasional dan efisiensi. Penutupan gerai paling banyak dilakukan di Indonesia dan Vietnam."; "Tidak diungkapkan berapa jumlah gerai yang ditutup di Indonesia dan Vietnam."

### P3B-S19
- Title: Mixue Tutup 428 Gerai, Rugi?
- Publisher: CNBC Indonesia
- URL opened: https://www.cnbcindonesia.com/research/20260422153138-128-728961/mixue-tutup-428-gerai-rugi
- Printed date: 22 April 2026 15:55
- Tier 3
- Access: opened
- Quotes: "ekspansi masif sebelumnya mulai memicu kejenuhan pasar. Tingginya jumlah gerai dalam satu wilayah meningkatkan persaingan internal dan menekan profitabilitas" (CNBC's analysis, i.e. commentary)

### P3B-S20
- Title: Bisnis Gerai Minuman di Tengah Tekanan Ekonomi, Ada yang Tutup dan Berkembang
- Publisher: Suara.com
- URL opened: https://www.suara.com/bisnis/2026/05/31/152000/bisnis-gerai-minuman-di-tengah-tekanan-ekonomi-ada-yang-tutup-dan-berkembang
- Printed date: Minggu, 31 Mei 2026 | 15:20 WIB
- Tier 3
- Access: opened
- Quotes: "bagian dari fase koreksi pasar (market correction) setelah sebuah produk kehilangan daya tarik kebaruannya (novelty effect)" (commentary by business observers)

### P3B-S21
- Title: Segarnya Shakeratto Latte Buatan Kafe Asal Norwegia yang Buka di Jakarta
- Publisher: detikFood
- URL opened: https://food.detik.com/info-kuliner/d-7728418/segarnya-shakeratto-latte-buatan-kafe-asal-norwegia-yang-buka-di-jakarta
- Printed date: Minggu, 12 Jan 2025 18:00 WIB
- Tier 3
- Access: opened
- Quotes: "Sebuah kafe asal Oslo, Norwegia baru buka di Jakarta"; "kapasitas tak sampai 50 orang yang berada di ASHTA District 8"; "Segelas seduhan hand drip dibanderol Rp 55.000++."

### P3B-S22
- Title: 5 Kafe Kopi Hits Asal Luar Negeri Ada di Jakarta, Intip Menu Favoritnya
- Publisher: detikFood
- URL opened: https://food.detik.com/resto-dan-kafe/d-8334297/5-kafe-kopi-hits-asal-luar-negeri-ada-di-jakarta-intip-menu-favoritnya
- Printed date: Minggu, 01 Feb 2026 07:00 WIB
- Tier 3
- Access: opened
- Quotes: "Kisaran harga minuman di sini dari Rp 60.000++" (Fuglen); "Harga minuman kopi di Harlan + Holden berada di kisaran Rp 63.000++"; "Kisaran harga minuman di sini dari Rp 80.000++" (Hario); "latte sampai cappuccino dengan kisaran harga Rp 50.000++" (Kitsune); "mulai dari sekitar Rp 40.000++" (Kurasu)

### P3B-S23
- Title: Pizza Marzano Resmi Hadir di Kuta Beachwalk Bali dengan Konsep Baru dan Menu Spesial
- Publisher: Industry.co.id
- URL opened: https://www.industry.co.id/read/144577/pizza-marzano-resmi-hadir-di-kuta-beachwalk-bali-dengan-konsep-baru-dan-menu-spesial
- Printed date: 2025-09-09 (article:published_time tag 2025-09-09T16:14+07:00)
- Tier 3
- Access: opened
- Quotes: "Restoran ke-23 Pizza Marzano di Indonesia"; "Sejak hadir pertama kali di Indonesia tahun 2006"; operator quoted as "Operations Manager PT Sari Pizza Indonesia"

### P3B-S24
- Title: Domino's Pizza Bidik Pasar NTB, Gerai Kedua di Mataram Segera Beroperasi
- Publisher: RRI (rri.co.id)
- URL attempted: https://rri.co.id/en/kuliner/2527004/dominos-pizza-bidik-pasar-ntb-gerai-kedua-di-mataram-segera-beroperasi
- Printed date: not read (WebSearch summary says 28 Jun 2026 opening)
- Tier 3
- Access: BLOCKED (Cloudflare challenge, "Just a moment"); figure from a WebSearch result summary only: provisional, needs a second source
- Quote (search summary): "Domino's opened its first Mataram outlet in Rembiga on 28 June 2026, and RRI reports it as the company's 250th store in Indonesia"

### P3B-S25
- Title: Paris Baguette Buka di PIK, Simak Promo dan Menu Barunya
- Publisher: Kontan Momsmoney
- URL opened: https://momsmoney.kontan.co.id/news/paris-baguette-buka-di-pik-simak-promo-dan-menu-barunya
- Printed date: Sabtu, 22 Oktober 2022 | 17:05 WIB (PRE-WINDOW; entry-date context only)
- Tier 3
- Access: opened
- Quotes: "Paris Baguette buka outlet ke delapan di PIK Avenue"; "kurang dari setahun EFN sudah membuka delapan gerai"

### P3B-S26
- Title: Domino's Pizza Tutup Ratusan Gerai, Rugi Rp56,8 Miliar
- Publisher: CNBC Indonesia
- URL opened: https://www.cnbcindonesia.com/news/20250903180907-4-664038/dominos-pizza-tutup-ratusan-gerai-rugi-rp568-miliar
- Printed date: 03 September 2025 22:00
- Tier 3
- Access: opened
- Quotes: "setelah menutup 312 gerai di seluruh dunia. Dari jumlah itu, 233 gerai ditutup di Jepang." The article does not mention Indonesia.

### P3B-S27
- Title: % Arabica opens its first drive-thru outlet in Asia
- Publisher: World Coffee Portal
- URL opened: https://www.worldcoffeeportal.com/news/arabica-opens-its-first-drive-thru-outlet-in-asia/
- Printed date: 8 December 2023 (PRE-WINDOW; the last count found)
- Tier 3
- Access: opened
- Quotes: "% Arabica currently operates seven outlets across Indonesia"; "The site is % Arabica's fifth outlet in the Indonesian capital and seventh across the southeast Asian country."

### P3B-S28
- Title: Cotti Coffee opens first location in Indonesia
- Publisher: Verdict Foodservice (citing World Coffee Portal)
- URL opened: https://www.verdictfoodservice.com/news/cotti-coffee-first-location-indonesia/
- Printed date: 2023-08-21 (article:published_time) (PRE-WINDOW)
- Tier 3
- Access: opened
- Quotes: "Chinese coffee chain Cotti Coffee has opened an outlet in Jakarta, Indonesia ... The opening of the new store in Kuningan City Mall"

### P3B-S29
- Title: Saizeriya Akan Buka di Indonesia? Restoran Italia Jepang Ini Siapkan Anak Usaha
- Publisher: Kompas.com (Ohayo Jepang)
- URL opened: https://ohayojepang.kompas.com/read/5973/saizeriya-akan-buka-di-indonesia-restoran-italia-jepang-ini-siapkan-anak-usaha?page=all
- Printed date: Kompas.com - 12/05/2026, 10:18 WIB
- Tier 3 (reports a company document dated 8 April 2026)
- Access: opened
- Quotes: "perusahaan memutuskan pendirian anak usaha yang sepenuhnya dimiliki Saizeriya"; "Pendirian anak usaha ini dijadwalkan pada Desember 2026"; "belum ada keterangan lebih lanjut mengenai lokasi gerai pertama, tanggal pembukaan restoran, daftar menu, harga"; "harga relatif terjangkau"

### P3B-S30
- Title: Tim Hortons to enter Malaysia in August 2024 with Kuala Lumpur stores
- Publisher: World Coffee Portal
- URL opened: https://www.worldcoffeeportal.com/news/tim-hortons-to-enter-malaysia-in-august-2024-with-kuala-lumpur-stores/
- Printed date: 15 July 2024 (PRE-WINDOW; plan statement only)
- Tier 3
- Access: opened
- Quotes: "which launched the coffee chain in Singapore in November 2023 and is preparing to open stores in Indonesia"

### P3B-S31
- Title: Blue Bottle Coffee to open first location in Southeast Asia
- Publisher: Inside Retail Asia
- URL opened: https://insideretail.asia/2025/03/10/blue-bottle-coffee-to-open-first-location-in-southeast-asia/
- Printed date: March 10, 2025
- Tier 3
- Access: opened
- Quotes: "will open its first outlet in Singapore, marking its Southeast Asian debut"

### P3B-S32
- Title: Acai cafe Oakberry opens seven stores in Australia-wide rollout
- Publisher: Inside Retail Australia
- URL opened: https://insideretail.com.au/sectors/food-beverage/acai-cafe-oakberry-opens-seven-stores-in-australia-wide-rollout-202310
- Printed date: October 18, 2023 (PRE-WINDOW)
- Tier 3
- Access: opened
- Quotes: "the company announced its expansion into Bali, Indonesia, with two new stores to open next month"; "premium Brazilian acai"

### P3B-S33
- Title: Setelah 10 Tahun, Carl's Jr. Indonesia Bakal Tutup Operasionalnya Akhir 2023
- Publisher: Kontan
- URL opened: https://industri.kontan.co.id/news/setelah-10-tahun-carls-jr-indonesia-bakal-tutup-operasionalnya-akhir-2023
- Printed date: Jumat, 22 Desember 2023 / 15:00 WIB (HISTORICAL)
- Tier 3
- Access: opened
- Quotes: "akan mengakhiri operasionalnya yang selama ini beroperasi di bawah Mahadasha Group pada tanggal 31 Desember 2023"; "Gerai pertama ... Januari 2014 ... lebih dari 24 gerai"

### P3B-S34
- Title: Texas Chicken Tutup Seluruh Gerai di Indonesia
- Publisher: Okezone Economy
- URL opened: https://economy.okezone.com/read/2023/08/19/455/2867188/texas-chicken-tutup-seluruh-gerai-di-indonesia
- Printed date: Sabtu, 19 Agustus 2023 | 07:42 WIB (HISTORICAL; reports a CSMI disclosure to the IDX)
- Tier 3
- Access: opened
- Quotes: "memutuskan kerjasama dengan Cajun Global LLC"; "kesulitan keuangan sejak Pandemi Covid-19"; "Saat ini semua restoran telah di tutup"

### P3B-S35
- Title: Penutupan 10 Restoran Ini Jadi Kehilangan Terbesar Dunia Kuliner Indonesia
- Publisher: detikFood
- URL opened: https://food.detik.com/foto-kuliner/d-8549519/penutupan-10-restoran-ini-jadi-kehilangan-terbesar-dunia-kuliner-indonesia
- Printed date: Sabtu, 27 Jun 2026 12:30 WIB (reports historical closures)
- Tier 3
- Access: opened
- Quotes: "Hard Rock Cafe Jakarta akhirnya tutup tahun 2023. Gerai terakhirnya di Jakarta ada di Pacific Place."; "Fish n Co ... resmi tutup pada 31 Desember 2022 setelah sempat memiliki sekitar 20 cabang"; "Restoran Marché Mövenpick di Indonesia resmi beroperasi pada tahun 2009. Namun mereka tutup permanen pada 2020 setelah 11 tahun"

### P3B-S36
- Title: Pernah Hadir di Indonesia, 5 Gerai Fast Food Asing ini Resmi Hengkang!
- Publisher: detikFood
- URL opened: https://food.detik.com/info-kuliner/d-8074043/pernah-hadir-di-indonesia-5-gerai-fast-food-asing-ini-resmi-hengkang
- Printed date: Jumat, 22 Agu 2025 18:00 WIB (reports historical closures)
- Tier 3
- Access: opened
- Quotes: "Karen's Diner ... Restoran ini sempat buka di Jakarta pada Desember 2022 ... menutup restorannya pada November 2023 dengan alasan kontrak pop-up yang sudah habis"; "Fish & Co. ... pembukaan gerainya pada akhir 1998 ... 31 Desember 2022"

### P3B-S37
- Title: INFOGRAFIK: Tidak Benar Waralaba Restoran Burger Cepat Saji Akan Tutup Permanen
- Publisher: Kompas.com (Cek Fakta)
- URL opened: https://www.kompas.com/cekfakta/read/2024/06/11/120500282/infografik--tidak-benar-waralaba-restoran-burger-cepat-saji-akan-tutup
- Printed date: 11 Juni 2024, 12:05 WIB (PRE-WINDOW; disconfirms a viral closure claim)
- Tier 3
- Access: opened
- Quotes: "tidak ditemukan adanya informasi kredibel yang menyatakan Burger King akan menutup usahanya secara permanen"

## Leads seen only as WebSearch results (not opened, not used as figures)

- RBA exchange filings of 24 Apr 2026 to Sep 2026 on preference-share injections into the Indonesian Burger King subsidiary (133 to 138 outlets; sources disagree): see ICRA and exchange filings for a verifier.
- Bisnis.com articles on MAPB 2025 and H1 2026 losses (403 for our client).
- Texas Chicken: a second franchisee (PT Quick Serve Indonesia) reportedly kept outlets open after the CSMI closures (Detik, Fortune IDN, Warta Ekonomi).
- Jakarta Post 2026-06-07 on Mixue's expanded investment in Indonesia: header opened, body not extracted.
- Kontan/Fortune IDN on % Arabica (late Oct 2023) with the 'kopi sultan' price-perception quote.
- Subway re-entry via Sari Sandwich Indonesia (2021, tier 4 relay), Jollibee (1991 to 1997 exit, Detik 2025-08-22 mention) and Lotteria (2020): historical, no rows.
