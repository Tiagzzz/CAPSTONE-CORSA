# Wheat-based food demand and food-service market, Indonesia (P1-C4, run 2)

Collector: P1-C4. Access date for all sources: 2026-10-17. Dataset: `data/processed/demand/wheat-foodservice.csv` (23 rows, ids P1C4-01 to P1C4-23). Plan: `tasks/2026-10-16-plan-1-demand-economics.md` (Q5, Q7, H7). Source keys are temporary (P1-C4-Sn) for the registrar.

Method notes. Pages were opened with curl and a browser user agent; HTML text was extracted locally and every quote below was checked as an exact string against the extracted text (whitespace-normalised). Dates are the byline or printed report date, never sidebar dates. Numbers printed in Indonesian format (comma decimal) are converted in the `value` column; the quote keeps the printed form.

## Hypothesis direction (H7: rice norm is a barrier to pasta)

* Wheat food use and imports are rising on USDA's data (rows 1-5): food wheat 9.4 to 9.8 Mt 2024/25 to 2025/26; imports 10.452 to 12.3 (Apr 2026 forecast) and 13.023 (Oct 2026 estimate) kt-basis. Direction: against "wheat flat or falling", i.e. disconfirms the rice-norm barrier at national level.
* Disconfirming nuance: BPS calendar-year imports fell 7.5% in 2025 (row 8); WINA instant noodle servings fell 0.9% in 2025 (row 11); APTINDO 2025 flour totals are unresolved (rows 7, 9, 10).
* Rice stays dominant: 88% of households eat rice vs 71% instant noodles and 32% wheat flour (row 14); rice falls from 6.81 to 6.49 kg per capita per month 2022-2024 and is lower in cities (6.09) than villages (7.07) (row 15). Pasta itself is not measured in any opened source.

## Sources

### P1-C4-S1
* Title: Grain: World Markets and Trade (October 2026), wheat tables
* Publisher: USDA Foreign Agricultural Service (Global Market Analysis); PSD data
* Original publisher (if relay): same (original)
* URL opened: https://apps.fas.usda.gov/psdonline/circulars/grain.pdf
* Printed publication date: October 2026 (printed in page header; wheat tables updated in the October 2026 WASDE cycle)
* Access date: 2026-10-17
* Proposed tier: 1. US government statistical agency, original PDF
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-01] "Indonesia 9,446 13,015 10,452 13,023 12,500 12,500"
  * [P1C4-02] "Indonesia 9,800 11,400 10,800 12,200 12,700 12,700"

### P1-C4-S2
* Title: Indonesia: Grain and Feed Annual, report ID2026-0010
* Publisher: USDA FAS Jakarta (GAIN); host is the APEDA AgriExchange mirror (Indian government)
* Original publisher (if relay): USDA FAS (original document, mirror copy; fas.usda.gov returned 403)
* URL opened: https://agriexchange.apeda.gov.in/MarketReport/101870605202646154731148.pdf
* Printed publication date: April 01, 2026 (printed "Date:" on page 1)
* Access date: 2026-10-17
* Proposed tier: 1. US government report; content is the original GAIN PDF, host is a government mirror; USDA staff assessment, not official statistics
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-03] "Wheat imports for 2025/26 are forecast to rebound to 12.3 MMT compared to 10.452 MMT in 2024/25"
  * [P1C4-04] "wheat consumption for food is forecast to increase by 4.3 percent to 9.8 MMT in 2025/26 compared to 9.4 MMT in 2024/25"
  * [P1C4-05] "During the period of July 2025 to January 2026, Indonesia imported a total of 7.8 MMT of wheat, an increase of 30.4 percent from 6.0 MMT imported during the same period of 2024/25."
  * [P1C4-06] "Small and medium enterprises (SMEs) consume about two-thirds (71 percent) of Indonesian wheat flour production."
  * [P1C4-07] "APTINDO reported that Indonesian wheat flour consumption during January to November 2025 grew by 4.87 percent to 7.09 MMT of wheat flour (equivalent to 9.089 MMT of wheat) compared to the same period in 2024."
  * [P1C4-22] "APTINDO reported that the high rice prices in the domestic market continue to increase the consumption of instant noodles, especially by lower income families."

### P1-C4-S3
* Title: Australia, Negara Pemasok Biji Gandum Terbesar untuk Indonesia pada 2025
* Publisher: Databoks (Katadata), author Nabilah Muhamad
* Original publisher (if relay): BPS (import statistics, HS gandum dan meslin)
* URL opened: https://databoks.katadata.co.id/perdagangan/statistik/6a868a6a4f38a/australia-negara-pemasok-biji-gandum-terbesar-untuk-indonesia-pada-2025
* Printed publication date: 20/08/2026 17:49 WIB (byline under title)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS data; article body is partly premium-gated, summary paragraphs and table text opened
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-08] "Indonesia mengimpor biji gandum dan meslin seberat 10,84 juta ton pada 2025. [...] Volumenya berkurang 7,5% dibanding 2024"

### P1-C4-S4
* Title: Impor Gandum Indonesia Masih Tinggi, Negara Mana yang Jadi Pemasok Utama?
* Publisher: GoodStats, author Insi Faiqoh
* Original publisher (if relay): BPS
* URL opened: https://goodstats.id/article/impor-gandum-indonesia-masih-tinggi-negara-mana-yang-jadi-pemasok-utama-6WGss
* Printed publication date: 18 September 2026 pukul 08.20 WIB (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS; used as second publisher for S3 (different outlet, own text)
* Access status: opened (full text read).
* Quotes (exact):
  * [(cross-check)] "Pada 2025, volume impor kembali turun menjadi 10,84 juta ton."
  * [(cross-check)] "mencapai titik tertinggi dalam periode tersebut pada 2024, yakni 11,72 juta ton."

### P1-C4-S5
* Title: BPS Lapor Impor Gandum Cs Nyaris Nol, Bos Pengusaha Terigu Buka Suara
* Publisher: CNBC Indonesia (Arrijal Rachman and Martyasari Rizky)
* Original publisher (if relay): APTINDO (data released to press)
* URL opened: https://www.cnbcindonesia.com/news/20250318151755-4-619666/bps-lapor-impor-gandum-cs-nyaris-nol-bos-pengusaha-terigu-buka-suara
* Printed publication date: 18 March 2025 18:20 (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Major news outlet relaying industry-association data
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-09] "Tahun 2024: Konsumsi melonjak cukup signifikan menjadi 7,41 juta MMT, setara gandum 9,5 MMT, atau tumbuh 8,04% dibanding tahun sebelumnya."

### P1-C4-S6
* Title: Sokong Industri Bakery Asia, Zeelandia Bangun Pabrik di Indonesia
* Publisher: Fortune Indonesia
* Original publisher (if relay): APTINDO (as cited by the outlet; no original opened)
* URL opened: https://www.fortuneidn.com/business/sokong-industri-bakery-asia-zeelandia-bangun-pabrik-di-indonesia-00-ccw2k-ygrxf2
* Printed publication date: 09 Oct 2026, 19:37 WIB (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Business news outlet; single-outlet, APTINDO figure not confirmed elsewhere; label weak
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-10] "memperkirakan konsumsi tepung terigu nasional pada 2026 mencapai 7,82 juta ton [...] naik 5 persen secara tahunan dibandingkan dengan realisasi 2025 yang sebesar 7,41 juta ton"

### P1-C4-S7
* Title: Demand Rankings, Global Demand table (instant noodles)
* Publisher: World Instant Noodles Association (WINA)
* Original publisher (if relay): same (original)
* URL opened: https://instantnoodles.org/en/noodles/demand/table/
* Printed publication date: Updated on August 6, 2026 (page statement)
* Access date: 2026-10-17
* Proposed tier: 2. Industry association statistics, original table; members compile national data
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-11] "Indonesia 13,270 14,260 14,540 14,680 14,540"

### P1-C4-S8
* Title: RI Jadi Raksasa Baru Mi Instan Global: Konsumsi Tembus 14 Miliar Porsi
* Publisher: CNBC Indonesia Research
* Original publisher (if relay): WINA ranking data and Macquarie report
* URL opened: https://www.cnbcindonesia.com/research/20251119114153-128-686534/ri-jadi-raksasa-baru-mi-instan-global-konsumsi-tembus-14-miliar-porsi
* Printed publication date: 19 November 2025 14:30 (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Major news outlet relaying WINA per-capita figure
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-12] "Indonesia berada di urutan kelima dunia pada 2024 dengan 51,7 porsi per kapita per tahun"

### P1-C4-S9
* Title: Rata-Rata Anggaran Penduduk Kota Jakarta Pusat untuk Membeli Mie Instan Rp3.615,26 per Kapita per Minggu
* Publisher: Databoks (Katadata)
* Original publisher (if relay): BPS Susenas (spending per capita per week)
* URL opened: https://databoks.katadata.co.id/ekonomi-makro/statistik/ea7f69a2dbc30d3/rata-rata-anggaran-penduduk-kota-jakarta-pusat-untuk-membeli-mie-instan-rp3-615-26-per-kapita-per-minggu
* Printed publication date: 29/12/2024 15:21 WIB (byline; the tag listing shows 31/12/2024 15:29 for the same title, article byline used)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS Susenas by data portal
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-13] "Rata-rata pengeluaran masyarakat di Kota Jakarta Pusat untuk membeli mie instan pada 2023 sebesar Rp3.615,26 per kapita per minggu."

### P1-C4-S10
* Title: Preferensi Konsumsi Rumah Tangga terhadap Pangan Sumber Karbohidrat di Indonesia (SEAGRI Vol. 14 No. 1)
* Publisher: Universitas Islam Malang, journal SEAGRI (Fatimah, Khoiriyah, Saputro)
* Original publisher (if relay): BPS Susenas 2024 (authors tabulate 341,802 households)
* URL opened: https://jim.unisma.ac.id/index.php/SEAGRI/article/download/30157/22843
* Printed publication date: Volume 14 Nomor 1 Tahun 2026 (only year printed, no month)
* Access date: 2026-10-17
* Proposed tier: 2. Peer-reviewed-style university journal using BPS microdata; small journal, secondary tabulation; rice kg table is cited as "Data Susenas, 2025 (diolah)"
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-14] "rice with a consumption percentage of 88%, followed by instant noodles at 71%, wheat flour at 32%"
  * [P1C4-15] "2024 6,09 7,07 6,49"

### P1-C4-S11
* Title: 10 Komoditas Penyumbang Garis Kemiskinan Terbesar di Indonesia 2025
* Publisher: GoodStats Data
* Original publisher (if relay): BPS press release 5 Feb 2026 (Susenas September 2025, poverty line)
* URL opened: https://data.goodstats.id/statistic/10-komoditas-penyumbang-garis-kemiskinan-terbesar-di-indonesia-2025-nxyIJ
* Printed publication date: 4 Maret 2026 pukul 10.30 (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS poverty-line commodity shares
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-16] "Di perkotaan, kontribusinya mencapai 21.10%, sedangkan di perdesaan lebih tinggi lagi, yakni 24.62%. [...] Mie instan berkontribusi 2.35% di perkotaan dan 2.04% di perdesaan. [...] roti 2.02% dan 1.84%"

### P1-C4-S12
* Title: Pengeluaran Warga RI untuk Rokok Melampaui Belanja Beras pada September 2025
* Publisher: Databoks (Katadata), author Nabilah Muhamad
* Original publisher (if relay): BPS Susenas September 2025
* URL opened: https://databoks.katadata.co.id/en/infographics/2026/06/05/pengeluaran-warga-ri-untuk-rokok-melampaui-belanja-beras-pada-september-2025
* Printed publication date: 05/06/2026 11:09 WIB (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-17] "masyarakat perkotaan rata-rata mengeluarkan Rp860.540 per orang untuk membeli makanan bulanan, sedangkan di perdesaan Rp720.742 per kapita per bulan."

### P1-C4-S13
* Title: Indonesia: Food Service - Hotel Restaurant Institutional Annual, report ID2025-0049
* Publisher: USDA FAS Jakarta (GAIN); host is the APEDA AgriExchange mirror
* Original publisher (if relay): USDA FAS (original document, mirror copy; fas.usda.gov returned 403)
* URL opened: https://agriexchange.apeda.gov.in/MarketReport/10187050820261515222144.pdf
* Printed publication date: December 31, 2025 (printed "Date:" on page 1)
* Access date: 2026-10-17
* Proposed tier: 1. US government report, USDA staff assessment; HRI value is a post estimate, method not stated on the pages read
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-18] "hotel, restaurant, and institutional (HRI) sector reached a value of $29 billion in 2024"
  * [P1C4-19] "Full-service restaurants accounted for 79 percent of total foodservice sales, followed by fast food (7 percent), cafés/bars (6 percent) and street stalls (5 percent)."

### P1-C4-S14
* Title: Indonesia: Food Processing Ingredients Annual, report ID2026-0011
* Publisher: USDA FAS Jakarta (GAIN); host is the APEDA AgriExchange mirror
* Original publisher (if relay): USDA FAS (original document, mirror copy)
* URL opened: https://agriexchange.apeda.gov.in/MarketReport/10187050820264615463220.pdf
* Printed publication date: April 02, 2026 (printed "Date:" on page 1)
* Access date: 2026-10-17
* Proposed tier: 1. US government report, USDA staff assessment
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-20] "Food Service $30"
  * [P1C4-23] "middle-class and Gen Z consumers are fueling growth in bakery and foodservice applications, including bread, pastries, and innovative concepts"

### P1-C4-S15
* Title: 10 Provinsi dengan Jumlah Restoran/Rumah Makan Terbanyak (Tahun 2024)
* Publisher: GoodStats Data, author Annisa Rendanianti
* Original publisher (if relay): BPS, Statistik Penyediaan Makanan dan Minuman 2024 (BPS page not opened: bps.go.id connection reset)
* URL opened: https://data.goodstats.id/statistic/10-provinsi-dengan-jumlah-restoranrumah-makan-terbanyak-5R8BM
* Printed publication date: 6 Januari 2026 pukul 15.00 (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of BPS; unit definition not verifiable at BPS
* Access status: opened (full text read).
* Quotes (exact):
  * [P1C4-21] "DKI Jakarta berada di urutan keempat dengan 202.983 restoran dan rumah makan."

### P1-C4-S16
* Title: Indonesia Peringkat Kedua Konsumsi Mi Instan Terbanyak di Dunia
* Publisher: CNBC Indonesia
* Original publisher (if relay): WINA
* URL opened: https://www.cnbcindonesia.com/lifestyle/20251223094843-33-696566/indonesia-peringkat-kedua-konsumsi-mi-instan-terbanyak-di-dunia
* Printed publication date: 23 December 2025 10:25 (byline)
* Access date: 2026-10-17
* Proposed tier: 3. Relay of WINA; not independent of S7/S8; used only as a cross-check
* Access status: opened (full text read).
* Quotes (exact):
  * [(cross-check)] "Warga Indonesia rata-rata mengonsumsi 52 porsi per orang setiap tahunnya"

## Conflicts recorded (headline vs body or source vs source)

1. Wheat imports 2025: BPS calendar-year 2025 = 10.84 Mt (S3, S4) vs USDA trade-year 2025/26 = 13.023 Mt (S1) and 12.3 Mt forecast (S2). Different periods (Jan-Dec vs Jul-Jun) and scope (grain vs wheat plus flour and products). Both stored; no reconciliation attempted.
2. APTINDO flour 7.41 Mt: attributed to 2024 (CNBC, S5, Mar 2025) and to 2025 (Fortune IDN, S6, Oct 2026); USDA gives Jan-Nov 2025 = 7.09 Mt (S2). Unresolved; S6 marked weak (single outlet).
3. WINA instant noodles 2025: table updated 6 Aug 2026 shows 14,540 vs 14,680 in 2024 (down 0.9%, S7); USDA GAIN (S2) says WINA reported +1.0% to "14.7 million servings" from "14.5 million" (units are billions; reflects an earlier release). The WINA table is the original and is preferred.
4. National instant noodle spending per capita per week printed as Rp257.5 (S9, 2023) and Rp254 (2025 Databoks article, not stored): inconsistent with Jakarta Pusat at Rp3,615 ranking 54th; not stored as a data point.
5. USDA S2 text: SMEs "about two-thirds (71 percent)"; 71% is not two-thirds. Value 71 stored with the flag.

## Historical / pre-window context (not in CSV)

* Kontan, 15 Feb 2019 (URL industri.kontan.co.id/news/aptindo-serapan-konsumsi-terigu-segmen-umkm-mencapai-65): APTINDO chair said UMKM take about 65% of flour and instant noodle, bread, biscuit and cookie industries about 35%; flour consumption grew about 5% a year over 10 years, about 4% in 2018. Pre-window; consistent with the 71/29 split in S2.
* Fortune IDN 27 Jun 2023 (Cerestar article, opened): APTINDO projected 2022 flour consumption at 6.7 Mt and USDA put 2020/21 per capita at 32 kg. Pre-window.
* Search-snippet only, not opened, pre-window or paywalled: Research and Markets "Pasta and Noodles in Indonesia" (USD 2.70 billion in 2023, CAGR 7.6% forecast 2023-2028; combined pasta and noodles).

## Leads only (tier 4 or not opened; not data rows)

* IMARC Group, "Indonesia foodservice market": USD 50.3 billion in 2025, CAGR 11.08% 2026-2034 (vendor marketing, snippet only; scope broader than HRI, not comparable to USDA USD 29-30 billion).
* Research and Markets and Euromonitor pasta pages; IndexBox pasta pages (free pages show placeholder "X" values).
* A Threads post quoting 51.7 servings per capita (social media; the figure is already in S8 from WINA via CNBC).

## Gaps

* Pasta market size or growth: no free tier 1-3 source found with 2024-26 data. Pasta is not separated from noodles in any opened source.
* Per-capita consumption of wheat flour, bread and pasta in kg: Kementan "Statistik Konsumsi Pangan 2025" and "Buletin Konsumsi Pangan Smtr1 2025" (satudata.pertanian.go.id) returned 403 to curl. Only instant noodles per capita (servings, WINA) was obtained.
* Jakarta-level wheat or noodle consumption: only Jakarta Pusat noodle spending (2023). BPS DKI "Pola Konsumsi Penduduk Provinsi DKI Jakarta 2025" returned 403; Databoks Jakarta Selatan noodle/bread pages not found.
* Number of cafes in DKI: only restaurants and rumah makan (202,983, 2024, relay). BPS publication page unreachable (connection reset), katalog.data.go.id returned 502; DKI government (Disparekraf) data not obtained.
* Rice vs wheat by income class: no opened source gives wheat products by income decile; only poverty-line shares (row 16) and urban/rural rice (row 15).
* HRI growth rate 2025: USDA gives only 2024 (USD 29 billion, +about 1%) and a 2025 channel figure (USD 30 billion) on a different basis.

## Blocked hosts

* www.fas.usda.gov (403 Access Denied; USDA GAIN content obtained through the APEDA mirror agriexchange.apeda.gov.in).
* satudata.pertanian.go.id (403, Kementan Pusdatin publications and the book page).
* jakarta.bps.go.id (403) and www.bps.go.id (connection reset by proxy).
* katalog.data.go.id (502 from proxy).
* apps.fas.usda.gov/psdonline: the Grain circular PDF opened; the interactive PSD query pages were not tried.
