# Plan 4 W9 (P4-W9): age and generation splits for purchase triggers and spend (run 2)

Agent P4-W9, access date 2026-10-17. All sources opened with curl (browser user agent), no bot challenge bypassed. Companion CSV: `data/processed/plan4-age-splits.csv` (36 rows, row_ids P4W9-01a to P4W9-32). `access_status` is `opened` for every row; `register_id` and `verification` are blank for the registrar and verifier. Downloaded files (the IMGR 2025 PDF, 37 MB) stay in the scratchpad, not in the repository.

## Headline

- No source opened gives an age cut in a 25-34, 25-39 or 26-35 band for any of the eight topics. The only splits that are free are by **generation label** (Gen Z / Millennials / Gen X), printed with bands that are 15-28 / 29-44 (Jakpat Mar 2025), 12-27 / 28-43 (IMGR 2025), or not printed at all (Jakpat Apr 2026, YouGov, Jakpat Korean street food).
- The derived "25-39" row (harmonisation rule 3) **cannot be built** from any of these without interpolation or re-weighting, which is forbidden. Reported as a gap, not a row. Closest proxy: Millennials (29-44 or 28-43), coded C.
- Age-fit coding used (Plan 4 section 4): B where the native band is printed and covers more than 75% of the canonical band (Gen Z 15-28 vs 18-28), C where the native band overlaps partly or the sources contradict each other on the band (Millennials 29-44 vs Younger 29-35 / Older 36-45; IMGR), D where no band is printed. Rows with D are shown but must not be aggregated. Note: the run-1 convention coded "Millennial (range not stated)" as C; here no-band rows are coded D, which is stricter.
- Nothing is Jakarta-specific. Geography is N (Jakpat, YouGov) or U (IMGR, 12 cities, Jabodetabek 20% of each sample).
- Most decision-relevant: Millennials in IMGR 2025 name **cooking at home** (66%) and **home-cooked lunches** (53%) as their top money-saving moves, and in YouGov April 2025 dining out is not among the Millennials' three printed priority categories (groceries 39%, electricity 19%, housing 16%). Both go against a "Millennials trade up to dine out" thesis. On the other side, Millennials order the largest lunch basket by app (Rp65,130 vs Rp58,609 Gen Z, Jakpat Mar 2025) and have the highest coffee reach (74% vs 67% Gen Z, Jakpat Apr 2026).

## Sources

### P4W9-S1 Jakpat "Indonesia Beverage Consumption" (Apr 2026 fieldwork) via GoodStats Data
- Title: "Ini Minuman yang Sering Dikonsumsi Gen Z dan Milenial 2026" (GoodStats Data).
- Publisher: GoodStats (Good News From Indonesia network), relay. Original publisher: Jakpat (survey company).
- URL opened: https://data.goodstats.id/statistic/ini-minuman-yang-sering-dikonsumsi-gen-z-dan-milenial-2026-3m1im ; Jakpat report page also opened: https://insight.jakpat.net/indonesia-beverage-consumption/ (printed June 19, 2026; preview images only, no figures in the text).
- Printed publication date: 27 Juni 2026 pukul 09.30 (GoodStats); fieldwork 22-24 April 2026 (separate from publication date).
- Access date: 2026-10-17. Access status: opened (relay); original report not downloaded (Jakpat "Download Report", not attempted).
- Proposed tier: 3. Relay of a tier-3 online-panel survey (non-probability sample, n=1,238, disclosed composition 42% Gen Z / 44% Millennials / 14% Gen X).
- Quotes: "Survei Jakpat yang melibatkan 1.238 responden dengan proporsi 42% Gen Z, 44% Milenial, dan 14% Gen X pada 22-24 April 2026"; "kopi menjadi minuman dengan persentase tertinggi yang dikonsumsi masyarakat Indonesia, dengan rincian 67% Gen Z dan 74% Milenial"; "Teh ... 65% Gen Z dan 75% Milenial"; "matcha (34% Gen Z dan 32% Milenial)"; "jamu (17% Gen Z dan 27% Milenial)". Also in the same article (not stored): milk 69% Gen Z / 65% Millennials, juice 47% / 54%, soda 30% / 33%.
- Rows: P4W9-01a to P4W9-04b.

### P4W9-S2 Jakpat "Consumer Behaviour in Online Food Delivery" (lunch spend by generation) via GoodStats
- Title: "Makanan Cepat Saji Tempati Urutan Pertama untuk Pilihan Menu Makan Siang" (GoodStats).
- Publisher: GoodStats, relay. Original: Jakpat.
- URL opened: https://goodstats.id/article/makanan-cepat-saji-tempati-urutan-pertama-untuk-pilihan-menu-makan-siang-ezXmH
- Printed publication date: 17 April 2025 pukul 11.00 WIB; fieldwork 13-14 March 2025 (Jakpat; the article says "dirilis Jakpat (April, 2025)").
- Access date 2026-10-17. Status: opened (relay).
- Proposed tier: 3 (relay of tier-3 survey; same survey also carried by Databoks, source S4, an independent relay by Katadata, which prints the generation bands).
- Quotes: "survei ... melibatkan 1.343 responden dengan komposisi Milenial sebanyak 46%, Gen Z 42% dan Gen X 12% serta mayoritas pekerja"; "Rata-rata pengeluaran Generasi Z mencapai Rp58.609, Gen X sebesar Rp63.250 dan Milenial sebesar Rp65.130, menjadi yang terbesar."; "makanan cepat saji jadi pilihan menu makan siang utama yang dipesan daring via aplikasi oleh Gen Z dan Milenial. Sedangkan Gen X memilih makanan Padang".
- Rows: P4W9-05 to P4W9-08.

### P4W9-S3 Jakpat online food delivery, Gen Z snack orders via GoodStats
- Title: "Camilan Favorit Gen Z saat Order Online, 41% Suka Jajanan Sunda".
- Publisher: GoodStats, relay of Jakpat.
- URL opened: https://goodstats.id/article/camilan-favorit-gen-z-saat-order-online-41-suka-jajanan-sunda-di-2025-gUjJ4
- Printed date: 17 April 2025 pukul 08.00 WIB; fieldwork 13-14 March 2025, n=1,343 (659 snack orderers).
- Access date 2026-10-17. Status: opened (relay). Tier 3.
- Quotes: "rata-rata anggaran yang dihabiskan Gen Z untuk setiap pesanan camilan online adalah sekitar Rp50.130."; also (not stored as a row, qualitative promo split, already in the dataset as UD-N04): "Gen Z lebih mengutamakan promo, sedangkan Milenial dan Gen X cenderung menyeimbangkan harga dan kualitas rasa" (Jakpat Lead Researcher Farida Hasna).
- Row: P4W9-09.

### P4W9-S4 Databoks (Katadata Insight Center) "Most Popular Snack Foods Ordered on Indonesian Online Food Delivery Apps"
- Publisher: Databoks / Katadata Insight Center, relay of Jakpat. Free summary text only (chart paywalled).
- URL opened: https://databoks.katadata.co.id/en/technology-telecommunications/statistics/688782781f63f/most-popular-snack-foods-ordered-on-indonesian-online-food-delivery-apps
- Printed date: 29/07/2025 08:00 WIB (the text says "quoted on Monday (July 28, 2025)"); fieldwork 13-14 March 2025.
- Access date 2026-10-17. Status: opened (relay, partial/paywalled chart). Tier 3.
- Quotes: "Broken down by generation, this is most common among millennials (58%), Gen X (48%), and Gen Z (43%)."; "Gen Z ordered these most frequently (41%), followed by Gen X (35%) and millennials (32%)."; "Gen X (45-49 years old) comprised 12%; millennials (29-44 years old) 46%; and Gen Z (15-28 years old) 42%."
- Rows: P4W9-10 to P4W9-13. Bread by generation (Gen X 44, Millennials 42, Gen Z 29) printed in the same text, not stored (low decision value).

### P4W9-S5 IDN Research Institute, "Indonesia Millennial and Gen Z Report 2025" (IMGR 2025), full PDF
- Publisher: IDN Research Institute (research arm of IDN Media; Populix named as research partner by IDN). Relay for the file: GoodStats publications.
- URL opened: https://goodstats.id/publication/indonesia-millennial-and-gen-z-report-2025-qpLaH (publication page) and PDF https://cdn.gnfi.net/goodstats/uploads/publications/files/2025/08/27/indonesia-millennial-and-gen-z-report-2025-vvhOWWB6M6.pdf (88 pages, free, no login).
- Printed publication date: "Tanggal Terbit 27 Agustus 2025" (GoodStats page; "Tahun 2024"); the PDF itself is undated. Fieldwork: "From March to August 2024" (methodology page); the profile slides say "May 2024".
- Access date 2026-10-17. Status: opened (PDF text with pdftotext; chart labels read from rendered pages 20, 28 and 48).
- Proposed tier: 3. Disclosed method (n=1,500, 750 per generation, 12 cities, quota by city, random sampling plus interviews); commercial and media-affiliated publisher with an interest in the generations it sells to. Not tier 2: no peer review, sample is urban online.
- Quotes: "we surveyed 1,500 respondents-750 Millennials and 750 Gen Z-across 12 major cities and regions which are Jabodetabek, Bandung, ..."; "Millennials are defined as those aged 28 to 43, while Gen Z includes individuals aged 12 to 27 as of 2024"; "Sixty percent of Gen Z respondents actively seek out promotions and discounts"; "54% of Gen Z is reducing social activities, such as hanging out with friends"; "Sixty-six percent of Millennials prioritize cooking at home, making it the most common money-saving strategy within this group."; "the 53% who prefer home-cooked lunches over snacks"; "Millennials show a slightly lower inclination towards frugality, with 49% embracing" / "Gen Z is leading the way in adopting a frugal lifestyle, with 56% actively implementing"; PayLater: "Their lower spending on fashion (12%) and entertainment (33%)", "(54%) allocated towards travel and entertainment", "Millennials have a mean borrowing amount of approximately 1.475 million IDR", "Gen Z has a slightly lower mean borrowing amount of approximately 1.275 million IDR".
- Internal inconsistencies recorded: (1) the profile slides print "17 - 29" for both generations and "May 2024", against the methodology page (Millennials 28-43, Gen Z 12-27, Mar-Aug 2024); (2) the PayLater text calls Gen Z "slightly lower" yet claims "marginally greater willingness" to take larger instalments. Rows carry age fit C for this reason.
- Rows: P4W9-14 to P4W9-19, P4W9-22 to P4W9-25.

### P4W9-S5b GoodStats article on IMGR 2025 QRIS usage by generation
- Title: "QRIS Jadi Metode Bayar Andalan Gen Z dan Milenial, Ini Frekuensi Penggunaannya".
- Publisher: GoodStats, relay of IDN Research Institute (IMGR 2025).
- URL opened: https://goodstats.id/article/qris-metode-pembayaran-andalan-gen-z-dan-milenial-54Cpb
- Printed date: 4 November 2024 pukul 12.30 WIB (so IMGR 2025 data were public by Nov 2024, before the GoodStats publication-page date of 27 Aug 2025).
- Access date 2026-10-17. Status: opened (relay); original PDF page 48 also read (chart labels 38/30 Gen Z, 25/35 Millennials, daily/weekly).
- Tier 3.
- Quotes: "Sebanyak 38% Gen Z menggunakan QRIS dalam kehidupan sehari-hari. Milenial berada di posisi selanjutnya dengan angka mencapai 25%."; "Dalam penggunaan mingguannya, 35% Milenilal lebih sering menggunakan QRIS dari Gen Z yang hanya mencapai 30%." (weekly values not stored as rows); "37% menilai promosi dan diskon eksklusif" (pooled Gen Z + Millennials, not split).
- Rows: P4W9-20, P4W9-21.

### P4W9-S6 YouGov Indonesia, "Rising expense prompt shifts in how Indonesians save, borrow and invest" (original publisher)
- Publisher: YouGov (market research firm). Original of the "Indonesia Personal Finance Outlook 2025 - Rising Costs, Resilient Minds".
- URL opened: https://yougov.com/articles/52426-rising-expense-prompt-shifts-in-how-indonesians-save-borrow-and-invest (report landing page also opened: https://yougov.com/reports/52419-rising-costs-resilient-minds-indonesia-2025, no figures, report is a gated download).
- Printed publication date: "YouGov - June 24, 2025". Fieldwork 17-21 April 2025.
- Access date 2026-10-17. Status: opened (original article; the generation tables are in the gated report).
- Proposed tier: 3. Established research firm, weighted online-representative sample, but the generation numbers used in rows come from relays (S7, S8).
- Quotes: "an online representative sample of 2,067 Indonesians aged 18 and older. The data was weighted by gender, age, socioeconomic class, and region"; "Spending also shifted, with half reporting higher expenses, mainly for groceries (34%), education (25%), and savings (24%). Younger respondents were more likely to cut back on essentials, while older generations reduced spending on lifestyle-related items." No row keyed to S6 because the generation percentages are only in S7/S8.

### P4W9-S7 Marketing-Interactive, "Study: 68% of Indonesians hopeful amid financial strains, but spending splits by generation"
- Publisher: Marketing-Interactive (trade press), relay of YouGov.
- URL opened: https://www.marketing-interactive.com/study-68-of-indonesians-hopeful-amid-financial-strains-but-spending-splits-by-generation
- Printed date: 23 June 2025. Fieldwork 17-21 April 2025.
- Access date 2026-10-17. Status: opened. Tier 3 (trade press with its own byline; carries the YouGov GM's quote).
- Quotes: "Dining out (23%) and entertainment (19%) were among the top categories reduced by Gen X+, while Millennials cited takeout and international travel as their main areas of retrenchment."; "Gen Z ... significantly more likely to have upped their spending on beauty (21%) and fashion (20%)".
- Rows: P4W9-28, P4W9-29.

### P4W9-S8 Campaign Indonesia, "Gen Z Indonesia prioritaskan identitas dan gaya hidup di tengah ekonomi lesu"
- Publisher: Campaign Indonesia (trade press), relay of YouGov.
- URL opened: https://www.campaignindonesia.id/article/gen-z-indonesia-prioritaskan-identitas-dan-gaya-hidup-di-tengah-ekonomi-lesu/1927729
- Printed date: "August 04 2025". Fieldwork 17-21 April 2025 (from S6).
- Access date 2026-10-17. Status: opened. Tier 3. **Single outlet for the 14% Gen Z dining-out figure and for the Millennial top-three list**; the YouGov original with the generation table was not opened (gated).
- Quotes: "Tiga besar pengeluaran Gen Z adalah kecantikan dan perawatan pribadi (21%), busana (20%), serta makan di luar (14%)."; "untuk Milenial, adalah bahan makanan (39%), listrik (19%), dan hal-hal yang terkait perumahan (16%). Gen X mendahulukan pengeluaran untuk sektor bahan makanan (40%), pendidikan (36%), dan listrik (20%)."; "Gen Z rela mengurangi kebutuhan primer seperti kesehatan (7%) dan bahan makanan (6%)".
- Label conflict stored in row notes: Campaign calls the three Gen Z categories spending "priorities" (pengeluaran), Marketing-Interactive calls beauty 21% and fashion 20% categories where Gen Z "upped" spending. Another outlet (Viva, 25 Jun 2025, tier 4, not used) puts 21% on cafe visits, which appears to be a mix-up.
- Rows: P4W9-26, P4W9-27, P4W9-30.

### P4W9-S9 Detik Finance, "Keuangan Generasi X hingga Gen Z Lagi Tertekan, Ini Datanya"
- Publisher: detikFinance (major news outlet), reporting a YouGov Indonesia media briefing.
- URL opened: https://finance.detik.com/berita-ekonomi-bisnis/d-7971787/keuangan-generasi-x-hingga-gen-z-lagi-tertekan-ini-datanya
- Printed date: "Kamis, 19 Jun 2025 12:07 WIB". Fieldwork April 2025, n=2,067 (printed).
- Access date 2026-10-17. Status: opened. Tier 3. Used only in notes of P4W9-28 and P4W9-29 (no row keyed to S9).
- Quotes: "gen X yang lebih tua mengurangi makan-makan di luar, beli-beli baju, atau hiburan-hiburan di luar ... gen Z, justru mengeluarkan yang lebih-lebih esensial nih, mereka mengurangi untuk health care, untuk belanja sehari-hari, atau makan di luar" (YouGov Indonesia GM Edward Hutasoit); "gen millennial ... lebih sedikit mengeluarkan uang untuk menabung dan liburan". This differs from S7 on what Millennials cut, and says Gen Z also cut eating out without a figure.

### P4W9-S10 Jakpat article, "Korean Street Food Is Trending, But Are Our Hearts Still With Local Snacks?" (original publisher)
- Publisher: Jakpat (survey company), own insight site.
- URL opened: https://insight.jakpat.net/korean-street-food-is-trending-but-are-our-hearts-still-with-local-snacks/
- Printed publication date: August 31, 2026. Fieldwork dates not printed. n=1,836.
- Access date 2026-10-17. Status: opened (original). Tier 3.
- Quotes: "Gen Z is the most dominant group trying Korean street food (48.9% of those who’ve tried it), followed by Gen Y (41.8%), with Gen X far behind at just 9.3%."; also not split by generation: "44.6% prefer to wait for others’ reviews before trying something themselves, while only 11.9% would immediately seek it out and try it as soon as it goes viral"; "74.9% of those who’ve tried Korean street food still say local snacks remain their top favorite".
- Rows: P4W9-31, P4W9-32 (composition of triers, not trial rates).

## Disconfirming evidence recorded
- P4W9-16, P4W9-17: Millennials' top money-saving actions are cooking at home (66%) and home-cooked lunches (53%).
- P4W9-27: dining out is not in the Millennials' printed top three priorities; P4W9-28: Gen X+ cut dining out (23%).
- P4W9-18/19: Millennials less frugal than Gen Z (49% vs 56%) in IMGR, but 49% is still nearly half.
- S10: only 11.9% of respondents (all generations) go straight to a viral food; 44.6% wait for reviews. Novelty-seeking is not the norm.
- P4W9-31/32: Gen Z and Gen Y account for 90.7% of Korean street food triers in that sample, but this is composition, and the sample is online and young-skewed.

## Dead ends, excluded and blocked (not used as figures)
- **Jakpat premium/gated reports with generation tables** (opened pages show previews only): "Gen Z, Millennials, Gen X Trend on Coffee 2025 vs 2023" (printed May 21, 2025, IDR 499,000), "Gen Z, Millennials, Gen X on Health Trend 2025 vs 2023" (May 15, 2025, n=601), "Consumer Behavior in Online Food Delivery" (April 11, 2025), "Consumer Insights: Local Food & Beverage Market" (October 8, 2025, eight Java cities, no Jakarta), "E-Wallet Consumer Patterns by Generation" (April 7, 2026). The free article of the local F&B report (https://insight.jakpat.net/strong-traditional-tastes-in-the-local-fb-market/, October 13, 2025) has gender, student vs worker and class splits but no generation split.
- **PwC Voice of the Consumer 2025 Indonesia** (HTML and PDF): HTTP 403 Akamai, not bypassed. A search summary says Gen Z buys fewer fresh ingredients than Millennials (41% vs 48%); not used (no opened source).
- **Bisnis.com** YouGov article (20250617/9/1885810): HTTP 403, not bypassed. **Medcom** Jakpat coffee article: expired TLS certificate, not bypassed (no `-k`). **Kumparan**: 403. **Scribd** IMGR 2026 one-pager: gated; the IDN Times IMGR 2026 pieces opened (27 Aug 2025) carry only content-curation and activism splits, no food.
- **Katadata/Databoks Gen Z coffee, eating-out frequency, Populix youth spending** pages opened: summary only, and pooled (Populix Feb 2025: 74% basic needs, Gen Z 18-28 and Millennials 29-44 mixed) or Gen Z 15-25 only (Jakpat Sep 2025 eating-out frequency, eight Java cities). Already in the dataset.
- **Populix**: reports are marketing pages (Exploring Coffee Market Sizing 2026) with no figures; the 2022-2023 Populix food trend report (media coverage dated 2 Jun 2023) is pooled Gen Z + Millennials and outside the date window.
- **Date fails (published before 2024-10-16)**: Jakpat "At the Restaurant: ... Indonesian Millennials Restaurant Habit" (June 13, 2016) and "It's Lunch Time" (Millennials); Jakpat food delivery habit (Sep 16, 2015); GoodStats Jakpat cooking by generation (Gen X 51% cook daily vs Gen Z 38%; GoodStats printed 5 September 2024).
- **GoodStats/GNFI student surveys** (coffee shop habits Nov 2024, n=203 and n=1,000, 91% aged 18-24): no generation split; not used.
- **Academic** (JUPSIM May 2025, 12 informants in Semarang; IPB JCS 2024): qualitative or Gen Z/zoomer samples outside Jakarta; no figures taken.
- A Gen Z-only fast-food frequency (GoodStats, 12 Jan 2025, Jakpat Dec 2024) and Gen Z average coffee spend (Databoks, Dec 2024) exist but have no Millennial counterpart; skipped as not splits.

## Gaps (needs a gated report or a direct data request)
- A 25-34 / 25-39 / 26-35 cut for any topic. Candidates: the Jakpat coffee and health reports (IDR 499,000 each, buy or request quote), the YouGov generation tables (gated), Kantar Dining in the Digital Age (gated, no numbers), Populix custom data.
- Millennial-specific values for: café visit frequency, spend per visit, willingness to pay for healthy food, new-restaurant trial, discovery channel (only Gen Z-heavy or pooled figures are free).
- Any Jakarta or Jabodetabek cut by age. IMGR 2025 samples 20% Jabodetabek per generation but prints no Jabodetabek splits.
- Population context (Plan 1, not a row here): Databoks 2025 (SUPAS 2025 via BPS) says Millennials are 24.82% and Gen Z 24.12% of DKI Jakarta's 10.72 million residents (Millennials 29-44, Gen Z 13-28 in 2025); URL https://databoks.katadata.co.id/en/demographics/statistics/69fd6222a67e4/millennials-and-gen-z-dominate-jakartas-population-in-2025 (opened, free text). Passed to Plan 1 as a lead.
