# P1-C2 middle class and income (Plan 1 Q1, H1/H2): findings, run 2

Worker P1-C2, run 2, access date 2026-10-17. Method: pages opened with curl and a full browser user agent; PDFs read with pdftotext (page images rendered where a table had no text layer). Figures are in `data/processed/demand/middle-class-income.csv` (30 rows, ids P1C2-01 to P1C2-34 with gaps where rows were cut for the 30-row target). Quotes are copied from the opened pages (Indonesian originals, English where the source is English). No figure below duplicates the rows already in `data/raw/2026-10-17-disconfirming-evidence.md` (national IKK 116.8/118.5/117.8, MSI -0.6% school holiday, World Bank Dec 2025 deck) or `data/processed/demand/consumer-surveys.csv`.

## Summary of what was found

- National series (Mandiri Institute on BPS Susenas, World Bank classes): middle class 47.9M (2024) to 46.7M (2025), 16.6% of population; aspiring middle class 137.5M to 142.0M (50.4%); upper class 1.2M (0.4%). BPS-labelled 57.33M (2019) to 47.85M (year conflict: 2021 vs 2024 in the relay article). The Jakarta-level class count was NOT found.
- World Bank IEP June 2026 resolves the press conflict: the report prints 14.5% (2018) to 7.1% (2025) of workers earning middle-class wages (the "14% to 8%" variant is press-only).
- Jakarta: UMP 2026 Rp5,729,876 (+6.17%), UMP 2025 Rp5,396,761 (+6.5%); average employee wage Rp5.9M (Aug 2025, highest province, 1.8x national); Gini 0.435 (highest province, Mar 2026); BI consumer confidence Jakarta 146.8 (Sep 2026).
- K-shape evidence (disconfirms a broad middle-class story, supports a narrow affluent tier): BRI tier growth 8.0% vs 3.5%; deposits above Rp2bn +15.99%; MSI upper +5.3% vs middle and lower slower; real wages of medium/high-skilled -1/-2% a year 2018-2025. Counter-evidence: MSI Ramadan 2026 middle +4.1% (fastest); BI confidence optimistic in all expenditure classes; household consumption 54% of Q1 2026 growth.
- Gaps: Jakarta middle/upper class headcount; Jakarta wage by education or sector (BPS Jakarta blocked); LPEM UI headcount (52M, 18.8% end-2023, search summary only); official BPS 2025 class series; age 25-39 cut of class counts.

## Source blocks

### P1C2-S1
- Title: Survei Konsumen September 2026: Keyakinan Konsumen Tetap Terjaga (press release No.28/216/DKom) and full report SK-September-2026.pdf (14 pages)
- Publisher: Bank Indonesia (original)
- URL opened: https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2821626.aspx ; https://www.bi.go.id/id/publikasi/laporan/Documents/SK-September-2026.pdf
- Printed publication date: 10/8/2026 10:00 AM on the release page (month-first format, read as 8 October 2026; consistent with Kontan 2026-10-12 coverage)
- Access date: 2026-10-17
- Proposed tier: 1 (central bank, original publisher)
- Access status: opened (original). Tables 2, 5 and 6 are images in the PDF; values read visually from rendered pages 9, 12 and 13 and flagged in the CSV notes.
- Quotes: "keyakinan konsumen pada September 2026 tetap optimis pada seluruh kelompok pengeluaran, dengan IKK tertinggi tercatat pada responden kelompok >Rp5 juta sebesar 123,5 (Grafik 2). Berdasarkan usia, IKK tertinggi tercatat pada responden usia 20-30 tahun sebesar 127,9 (Grafik 3)." ; "Survei Konsumen merupakan survei bulanan ... kurang lebih 4.600 rumah tangga sebagai responden (stratified random sampling) di 18 kota". Used by rows 14, 17, 18, 20.

### P1C2-S2
- Title: Jumlah Kelas Menengah Turun Lebih Dalam di 2025 Tertekan Daya Beli dan Konsumsi
- Publisher: Kontan.co.id (relay); original: Mandiri Institute report "Demographic Insights: Dinamika Kelas Menengah di 2025" on BPS Susenas data
- URL opened: https://nasional.kontan.co.id/news/jumlah-kelas-menengah-turun-lebih-dalam-di-2025-tertekan-daya-beli-dan-konsumsi
- Printed publication date: Minggu, 08 Februari 2026 15:43 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (national business media relaying a tier 2 bank research unit computing from tier 1 BPS data; original report not opened)
- Access status: opened (relay)
- Quotes: "jumlah kelas menengah turun dari 47,9 juta orang pada 2024 menjadi 46,7 juta orang pada 2025, atau berkurang sekitar 1,1 juta orang. Penurunan ini lebih dalam dibandingkan tahun sebelumnya yang hanya turun 0,4 juta orang. Jumlah tersebut setara dengan 16,6% dari total penduduk nasional." ; "aspiring middle class meningkat dari 137,5 juta pada 2024 menjadi 142,0 juta orang pada 2025, atau setara dengan 50,4%" ; "upper class ... hanya sekitar 0,4% dari total penduduk, yakni 1,2 juta orang pada 2025, naik tipis dari 1,1 juta" ; consumption growth quotes as in rows 8 and 9. Rows 1, 2, 3, 8, 9.

### P1C2-S3
- Title: Komposisi Penduduk Indonesia Menurut Kelas Ekonomi 2025
- Publisher: GoodStats Data (relay; data from BPS processed by Mandiri Institute)
- URL opened: https://data.goodstats.id/statistic/komposisi-penduduk-indonesia-menurut-kelas-ekonomi-2025-QLCdE
- Printed publication date: 24 Februari 2026 pukul 13.00
- Access date: 2026-10-17
- Proposed tier: 3 (data portal relaying bank research on BPS data)
- Access status: opened (relay)
- Quotes: "Menuju kelas menengah: 1,5-3,5 kali dari garis kemiskinan Menengah: 3,5-17 kali dari garis kemiskinan Atas: lebih dari 17 kali dari garis kemiskinan" ; "kelas menengah mencakup 16,6% populasi ... kelas atas hanya menyumbang 0,4%". Row 4. A second GoodStats article (https://goodstats.id/article/jumlah-penduduk-kelas-menengah-indonesia-turun-pada-2025-iZPou, 1 Maret 2026) was also opened and prints "berkurang sekitar 1,2 juta orang" (cited in row 1 notes).

### P1C2-S4
- Title: Jumlah Kelas Menengah Turun, ADB Prediksi Ekonomi RI Terganggu, Siapa Kelas Menengah?
- Publisher: Kontan.co.id (relay; citing BPS and Asian Development Outlook April 2025)
- URL opened: https://nasional.kontan.co.id/news/jumlah-kelas-menengah-turun-adb-prediksi-ekonomi-ri-terganggu-siapa-kelas-menengah
- Printed publication date: Senin, 05 Mei 2025 05:40 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (relay; the article has internal year inconsistencies, see rows 5-6)
- Access status: opened (relay); BPS original and the Bisnis.com articles of 2026-02-09 (blocked 403) not opened
- Quotes: "Berdasarkan data Badan Pusat Statistik (BPS), pada tahun 2019 masyarakat kelas menengah mencapai 57,33 juta, kemudian jumlah tersebut turun menjadi 47,85 juta pada 2021. Penurunan tersebut membuat populasi kelas menengah ... yang tadinya mencapai 21,5% pada 2029, turun menjadi 17,1% pada 2024." Rows 5, 6.

### P1C2-S5
- Title: Daya Beli Kelas Menengah Tergerus: Ini Pemicu Ancaman PHK 2026
- Publisher: Kontan.co.id (relay of statements by CORE Indonesia and LPEM FEB UI economists)
- URL opened: https://nasional.kontan.co.id/news/daya-beli-kelas-menengah-tergerus-ini-pemicu-ancaman-phk-2026
- Printed publication date: Rabu, 27 Mei 2026 11:17 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (news; opinions of tier 2 research economists)
- Access status: opened (relay)
- Quotes: "Jika dibandingkan dengan 2018, penurunannya bahkan jauh lebih tajam karena saat itu jumlah kelas menengah masih mencapai sekitar 59,5 juta orang." ; "Nampaknya untuk kelas menengah masih akan tertekan di 2026 karena belum ada kebijakan pemerintah sejauh ini yang pro kelas menengah, seperti penciptaan lapangan kerja berkualitas," kata Riefky. Rows 7, 34.

### P1C2-S6
- Title: Indonesia Economic Prospects (IEP), June 2026: Managing Risks, Unlocking Productivity
- Publisher: World Bank (original)
- URL opened: https://documents1.worldbank.org/curated/en/099060926111525068/pdf/P513006-58b80446-5646-4a53-b39c-800d0fa99b73.pdf (found via worldbank.org search results; press release https://www.worldbank.org/en/news/press-release/2026/06/13/indonesia-s-growth-remains-resilient-but-productivity-reforms-are-key-to-creating also opened, dated June 13, 2026)
- Printed publication date: "June 2026" (cover and page footers); press release June 13, 2026
- Access date: 2026-10-17
- Proposed tier: 1 (international organisation, original report)
- Access status: opened (original, pdftotext of 1.7 MB PDF)
- Quotes: "Real wages for medium- and high-skilled workers have declined by approximately 1-2 percent per year since 2018, and the share of workers earning middle-class incomes has fallen sharply, from 14.5 percent in 2018 to just over 7 percent in 2025." ; Box A.2: "falling from 14.5 percent in 2018 to 7.1 percent in 2025 (Figure B.1.1). The share of middle-class population-using official definition-has followed the same trajectory, declining since 2018." ; footnote 18: "SUSENAS defines the middle class as households with per capita expenditure between 3.5 and 17 times the national poverty line." ; "Household consumption remained the main driver of growth, accounting for 54 percent of growth." Rows 4, 10, 11, 12, 13. Note: the figure for the share of the middle-class population in this report is shown only in a chart (no number in the text layer), so no official IEP middle-class headcount is stored.

### P1C2-S7
- Title: Daftar Lengkap UMP 2026 di Seluruh Provinsi, DKI Jakarta Tertinggi dengan Rp5.729.876
- Publisher: Kompas TV (relay of provincial announcement; regulation PP 49/2025 named in the article)
- URL opened: https://www.kompas.tv/info-publik/639870/daftar-lengkap-ump-2026-di-seluruh-provinsi-dki-jakarta-tertinggi-dengan-rp5-729-876
- Printed publication date: Kompas.tv - 26 Desember 2025, 12:55 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (news relay; the governor's decision itself, JDIH Jakarta, not opened)
- Access status: opened (relay)
- Quotes: "Besaran UMP Jakarta 2026 ditetapkan sebesar Rp5.729.876 atau naik 6,17 persen dibandingkan tahun sebelumnya." Row 21.

### P1C2-S8
- Title: Naik Rp 329.380, UMP Jakarta 2025 Jadi Rp 5.396.761
- Publisher: Kontan.co.id (republishing Kompas.com)
- URL opened: https://nasional.kontan.co.id/news/naik-rp-329380-ump-jakarta-2025-jadi-rp-5396761 (a second relay, Metro TV 2024-12-11, https://metrotvnews.com/read/NleCpDOz-upah-buruh-di-jakarta-2025-naik-jadi-rp5-396-juta-bulan, also opened and prints Rp5.396.761 and 6.5 percent)
- Printed publication date: Rabu, 11 Desember 2024 13:45 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (news relay)
- Access status: opened (relay)
- Quotes: "UMP Jakarta 2025 naik 6,5 persen atau setara Rp 329.380. Dengan begitu, besaran UMP DKI Jakarta 2025 menjadi Rp 5.396.761". Row 22.

### P1C2-S9
- Title: Jakarta Jadi Provinsi dengan Upah Buruh Tertinggi per Agustus 2025
- Publisher: GoodStats Data (relay of BPS Sakernas August 2025; BPS press release 5 Nov 2025 No. 103/11/Th. XXVIII not opened, bps.go.id Cloudflare)
- URL opened: https://data.goodstats.id/statistic/jakarta-jadi-provinsi-dengan-upah-buruh-tertinggi-per-agustus-2025-npvsb
- Printed publication date: 14 November 2025 pukul 09.00
- Access date: 2026-10-17
- Proposed tier: 3 (data portal relay of tier 1 BPS)
- Access status: opened (relay). Independent second page: infobanknews and CNBC Indonesia (2025-11-05) opened for national Rp3,33 juta (+1.94%) but do not give the Jakarta figure.
- Quotes: "rata-rata upah buruh yang didapatkan pekerja di Jakarta mencapai Rp5,9 juta per bulannya, tertinggi se-Indonesia pada Agustus 2025. ... Pada Agustus 2024, rata-rata upah buruh di Jakarta sebesar Rp5,81 juta per bulannya." Row 23.

### P1C2-S10
- Title: Rata-rata Upah Buruh Menurut Tingkat Pendidikan per Agustus 2025
- Publisher: GoodStats Data (relay of BPS Sakernas)
- URL opened: https://data.goodstats.id/statistic/rata-rata-upah-buruh-menurut-tingkat-pendidikan-per-agustus-2025-ML0Zn
- Printed publication date: 9 November 2025 pukul 11.00
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay); same figures also on gebrak.id (2025-12-17, tier 4, not used)
- Quotes: "buruh dengan gelar Diploma IV, S1, S2, S3 memiliki rata-rata upah sebesar Rp4,8 juta ... Diploma I/II/III ... Rp4,5 juta ... SD ke bawah ... Rp2,19 juta." Row 24.

### P1C2-S11
- Title: Indonesia's Wealthy Elite Drives Consumption Surge as Middle Class Faces Squeeze
- Publisher: Investortrust.id (relay); original: BRI Office of Chief Economist, Quarterly Economic Outlook Q2-2026 (July 2026), with LPS deposit data and BPS Gini
- URL opened: https://investortrust.id/macro/112261/indonesias-wealthy-elite-drives-consumption-surge-as-middle-class-faces-squeeze
- Printed publication date: SUNDAY, 9 AUGUST 2026, 19:10 GMT+7
- Access date: 2026-10-17
- Proposed tier: 3 (Dewan Pers verified outlet relaying a state bank's research unit; original not opened)
- Access status: opened (relay)
- Quotes: "economic expansion for the wealthy tier reached an estimated 8.0% year-on-year in the first quarter, up from 6.5% in 2025. By contrast, lower-tier growth decelerated to 3.6%, while middle-class growth slipped to 3.5%" ; "deposits in accounts holding over Rp 2 billion ... expanded 15.99% year-on-year in April 2026. Middle-tier accounts ... grew just 3.15%". Rows 26, 27.

### P1C2-S12
- Title: 7 Provinsi dengan Ketimpangan Pengeluaran Penduduk Tertinggi Maret 2026
- Publisher: GoodStats Data (relay of BPS Gini ratio March 2026; BPS press release 5 Aug 2026 blocked)
- URL opened: https://data.goodstats.id/statistic/7-provinsi-dengan-ketimpangan-pengeluaran-penduduk-tertinggi-maret-2026-URgif
- Printed publication date: 11 Agustus 2026 pukul 11.00
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay)
- Quotes: "DKI Jakarta menempati posisi teratas dengan gini ratio 0,435, diikuti Jawa Barat sebesar 0,413, dan DI Yogyakarta dengan 0,411." Row 28.

### P1C2-S13
- Title: Mandiri Spending Index: Belanja Masyarakat Melambat, Keuangan Kelas Bawah Tertekan
- Publisher: Kontan.co.id (relay of Bank Mandiri Chief Economist statements)
- URL opened: https://nasional.kontan.co.id/news/mandiri-spending-index-belanja-masyarakat-melambat-keuangan-kelas-bawah-tertekan
- Printed publication date: Senin, 12 Oktober 2026 13:32 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (news relay of tier 2 bank research; Mandiri Institute original not reachable)
- Access status: opened (relay)
- Quotes: "belanja restoran tumbuh 4,7% YoY. Meski masih mencatatkan pertumbuhan tertinggi ... lebih rendah dibandingkan pertumbuhan pada tahun lalu sebesar 6,1%." ; "indeks tabungan kelompok menengah relatif stabil di level 100,5, turun tipis 0,1% MoM. Adapun indeks tabungan kelompok atas meningkat menjadi 95,1, lebih tinggi dibandingkan posisi pada tahun lalu sebesar 94,0." Rows 29, 30. Page prints the lower-group saving index as both 68,7 and 687,1.

### P1C2-S14
- Title: Mandiri Spending Index Mei 2026 Melandai, Masyarakat Mulai Rem Belanja Pasca Lebaran
- Publisher: Kontan.co.id (relay; Mandiri Macro and Market Brief Q2 2026, Andre Simangunsong)
- URL opened: https://nasional.kontan.co.id/news/mandiri-spending-index-mei-2026-melandai-masyarakat-mulai-rem-belanja-pasca-lebaran
- Printed publication date: Senin, 11 Mei 2026 19:24 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay)
- Quotes: "pertumbuhan belanja kelompok upper secara tahunan mencapai 5,3% pada 2026, lebih tinggi dibandingkan tahun lalu yang sebesar 3,1%. Sementara kelompok lower dan middle justru mengalami perlambatan pertumbuhan belanja." Row 31.

### P1C2-S15
- Title: Mandiri Institute: Kelas menengah penggerak konsumsi di Ramadhan 2026
- Publisher: ANTARA (relay of Bank Mandiri press statement)
- URL opened: https://www.antaranews.com/berita/5528284/mandiri-institute-kelas-menengah-penggerak-konsumsi-di-ramadhan-2026
- Printed publication date: Rabu, 15 April 2026 21:48 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (national news agency; original Mandiri statement)
- Access status: opened (relay)
- Quotes: "Konsumsi kelompok menengah mencatat pertumbuhan sebesar 4,1 persen, lebih tinggi dari kelompok bawah (2,1 persen) dan atas (2,6 persen)." ; "tingkat konsumsi generasi Gen Z tumbuh 4,4 persen, lebih tinggi dibandingkan kelompok usia Milenial (3 persen) dan Gen X (1,4 persen)." Row 32.

### P1C2-S16
- Title: Kelas Menengah Royal Belanja Jelang Lebaran, Tapi Tabungannya Menipis
- Publisher: CNBC Indonesia Research (relay of Mandiri Institute MSI and BI Consumer Survey)
- URL opened: https://www.cnbcindonesia.com/research/20260317113109-128-719750/kelas-menengah-royal-belanja-jelang-lebaran-tapi-tabungannya-menipis
- Printed publication date: 17 March 2026 14:15
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay). Gives an opened source for BLOCKED row 5 of the disconfirming-evidence table (Bisnis 2026-02-26 MSI savings story).
- Quotes: "Mandiri Saving Index kelompok menengah pada Februari 2026 berada di level 100,4. Angka ini turun dari tahun sebelumnya dan menjadi yang terendah sejak Oktober 2023." ; "IKK kelompok pengeluaran Rp3,1-4 juta naik dari 120,7 menjadi 122,6, sedangkan kelompok Rp4,1-5 juta naik dari 124,2 menjadi 125,5." Row 33.

## Blocked or not opened

- bps.go.id (and jakarta.bps.go.id): Cloudflare challenge (403); BPS originals for the class series, Gini, Sakernas wage and the Jakarta class split not opened.
- Bisnis.com (ekonomi.bisnis.com): 403 on the 2026-02-09 middle-class articles; only titles/search summaries seen.
- voi.id (403) and krungsri.com (Incapsula block): the two secondary pages that summarise the IEP June 2026 text; the World Bank report itself was opened instead.
- worldbank.org country publication landing pages returned 404 at guessed URLs; the report PDF and press release were reached via search results.
- Not found (gaps): Jakarta middle/upper class headcount (a WebSearch result mentioned a Jakarta fall of 119,000 persons attributed to Mandiri Institute; it appears on no opened page and is not stored); LPEM UI's own series; Jakarta wage by education or sector; MSI by class for Jakarta; Mandiri Spending Index growth for the upper and middle groups for Aug-Sep 2026.
