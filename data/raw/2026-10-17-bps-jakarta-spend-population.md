# P1-C1: Jakarta population by age band, prepared-food spend, food share, expenditure class (run 2)

Collector P1-C1, access date 2026-10-17. Output: `data/processed/demand/population-spend.csv` (26 rows). Plan: `tasks/2026-10-16-plan-1-demand-economics.md` (Q1, Q2, section 4 bands, harmonisation rule 3).

## Access notes

- Opened: databoks.katadata.co.id (200), cnbcindonesia.com, data.goodstats.id, antaranews.com.
- Blocked, not bypassed: bps.go.id and jakarta.bps.go.id (403, Cloudflare). A URL that served a challenge page instead of a PDF: assets.dataindonesia.id (BPS "Ringkasan Eksekutif" March 2024) and satudata.pertanian.go.id (Buletin Konsumsi Pangan): both returned HTML, not PDF, so nothing was read from them. nu.or.id returned nothing.
- satudata.jakarta.go.id and data.jakarta.go.id load (200) but no relevant dataset was found via search; not further explored.
- Databoks "pdb" (single data) pages are premium: chart and source paywalled; only the free teaser text was read. Rows from those pages say "opened (teaser...)".
- The bps.go.id Susenas tables themselves were never opened, so every figure is a tier-3 relay of BPS (tier 1).

## DERIVED rows

- P1C1-P06 (DERIVED): Jakarta Pusat 25-39 = 81,880 + 81,020 + 81,700 = 244,600 persons (22.80% of the city).
- P1C1-S06 (DERIVED): Jakarta Selatan 25-39 = 179,370 + 178,390 + 178,160 = 535,920 persons (22.71% = 7.6 + 7.56 + 7.55, sum of printed shares).
- Components kept as rows P1C1-P02 to P04 and S02 to S04. These two are the only derived values (the plan's rule 3 overrides lesson (f) for this row).
- DKI-wide (province) 5-year bands were not found; only the two cities above. Jakarta Selatan + Pusat together 25-39 = 780,520 (my sum, not stored).

## Gaps

1. DKI province population by 5-year band (jakarta.bps.go.id table blocked).
2. Per-capita prepared-food spend by expenditure class or quintile: not found for DKI, Selatan or Pusat; BPS publishes only a 40/40/20 food split for some districts (seen on RRI Malinau, not Jakarta).
3. DKI prepared-food spend for 2024 and 2025 (only Mar 2026 found, and Selatan/Pusat/Utara/Barat for 2024). Jakarta Selatan 2025 prepared-food value not found (Databoks pdb page for Selatan not surfaced).
4. Distribution of the DKI population by expenditure class (poor, vulnerable, aspiring middle, middle, upper): not found. Only the poor share (4.14%, Sep 2024) is stored. National class shares exist only in search summaries.
5. Single-age or SCBD/Setiabudi/Tebet kecamatan-level splits: not found.

## Disconfirming and caution notes

- Jakarta Pusat prepared-food spend fell 2.5% in 2024 and Jakarta Barat fell 5.8% while Jakarta Selatan rose 25%: the premium is local to Selatan and Utara.
- Jakarta Selatan food share fell from 38.08% (2024) to 34.96% (2025) while total spend rose 15.6%; the extra spend went to non-food.
- Jakarta Pusat total spend fell in 2025 (Rp2.59m per Databoks headline, not stored).
- Population "June 2024" is Databoks' label; the 2024 city totals are described by Databoks as "lower than 2023" for Pusat and "a decrease" for Selatan.
- Date format: Databoks prints dd/mm/yyyy; the Pusat EN article is 03/12/2024 (3 Dec 2024) and the Selatan EN article 12/03/2025 (12 Mar 2025). The first Pusat article (7 Aug 2024) is before the cut-off and was not used.

## Sources

### P1-C1-S1
- Title: The Majority of Jakarta Pusat's Population in 2024 Will Be of Working Age
- Publisher: Katadata Insight Center (Databoks); original publisher BPS (stated "June 2024, sourced from the Central Bureau of Statistics (BPS) publication"). English page is an AI translation of the Indonesian article (disclosure on page).
- URL opened: https://databoks.katadata.co.id/en/demographics/statistics/7c056964f536090/the-majority-of-jakarta-pusats-population-in-2024-will-be-of-working-age
- Printed date: 03/12/2024 16:12 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (reputable data relay of a tier-1 source; original not opened)
- Access status: opened
- Quotes: "Age 25-29 years: 81,880 (7.63%) * Age 30-34 years: 81,020 (7.55%) * Age 35-39 years: 81,700 (7.62%)"; "Central Jakarta's population was recorded at 1.07 million in 2024."

### P1-C1-S2
- Title: 21.83% of South Jakarta's population in 2024 will be aged 0-14 years.
- Publisher: Katadata Insight Center (Databoks); original BPS (June 2024). AI translation disclosure on the page.
- URL opened: https://databoks.katadata.co.id/en/demographics/statistics/687652ae17582ab/2183-of-south-jakartas-population-in-2024-will-be-aged-0-14-years
- Printed date: 12/03/2025 16:05 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Age 25-29 years: 179,370 (7.6%) * Age 30-34 years: 178,390 (7.56%) * Age 35-39 years: 178,160 (7.55%)"; "South Jakarta's population was recorded at 2.36 million in 2024."

### P1-C1-S3
- Title: Pengeluaran per Kapita DKI Jakarta 2025: Kenaikan Jadi Rp2,96 Juta per Bulan
- Publisher: Katadata Insight Center (Databoks); original BPS Susenas
- URL opened: https://databoks.katadata.co.id/layanan-konsumen-kesehatan/statistik/e5b26141744c322/pengeluaran-per-kapita-dki-jakarta
- Printed date: 25/09/2026 07:40 WIB ("Terakhir diperbarui: 25 September 2026"; URL aliases carry 2026/08/03 and 2026/08/28)
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Rp1,15 juta (38,93%) dibelanjakan untuk makanan dan Rp1,81 juta (61,07%) untuk kebutuhan bukan makanan"; 2024 table "Porsi Makanan 39,66% 38,93%".

### P1-C1-S4
- Title: Pengeluaran per Kapita Kota Jakarta Selatan 2025: Lonjakan Jadi Rp4,08 Juta per Bulan
- Publisher: Katadata Insight Center (Databoks); original BPS Susenas
- URL opened: https://databoks.katadata.co.id/layanan-konsumen-kesehatan/statistik/721e41cd0521a99/pengeluaran-per-kapita-kota-jakarta-selatan
- Printed date: "Terakhir diperbarui: 20 Agustus 2026"
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Rp1,43 juta (34,96%) dibelanjakan untuk makanan dan Rp2,66 juta (65,04%) untuk kebutuhan bukan makanan"; "Rp4,08 juta (Rp4.083.229) sepanjang 2025".

### P1-C1-S5
- Title: Rata-Rata Pengeluaran Perkapita Sebulan untuk Makanan dan Minuman Jadi di Kota Jakarta Pusat 2018 - 2024
- Publisher: Katadata Insight Center (Databoks, PDB premium); data processed from BPS Susenas
- URL opened: https://databoks.katadata.co.id/pdb/statistik/303cd526232af5f/pengeluaran-perkapita-sebulan-untuk-makanan-dan-minuman-jadi-kota-jakarta-pusat-2024
- Printed date: 19/01/2026 08:12 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (premium page; free teaser only; chart and source field paywalled)
- Access status: opened (teaser only)
- Quotes: "Pengeluaran untuk makanan dan minuman jadi di Kota Jakarta Pusat pada tahun 2024 tercatat sebesar Rp 513.174 per kapita per bulan."; "Kota Jakarta Selatan bahkan mencatatkan pertumbuhan signifikan sebesar 25 persen dengan nilai pengeluaran Rp 548.413."; Utara 556.691 (+9,4%); Barat 454.710 (-5,8%).

### P1-C1-S6
- Title: Belanja Warga DKI Jakarta Rp 3,07 per Kapita/Bulan, Buat Apa Saja?
- Publisher: CNBC Indonesia (news); original BPS "Pengeluaran untuk Konsumsi Penduduk Indonesia Maret 2026", uploaded 5 Oct 2026
- URL opened: https://www.cnbcindonesia.com/news/20261007153057-4-774163/belanja-warga-dki-jakarta-rp-307-per-kapita-bulan-buat-apa-saja
- Printed date: 07 October 2026 17:35
- Access date: 2026-10-17
- Proposed tier: 3 (major outlet relaying BPS)
- Access status: opened (relay; BPS original not opened)
- Quote: "makanan dan minuman jadi yang mencapai Rp 524.958 per kapita per bulan"

### P1-C1-S7
- Title: Pengeluaran Makanan Jadi Capai Rp248 Ribu, Lampaui Komoditas Makanan Lain
- Publisher: GoodStats Data; original BPS March 2025 report
- URL opened: https://data.goodstats.id/statistic/pengeluaran-makanan-jadi-capai-rp248-ribu-lampaui-komoditas-makanan-lain-SgBeB
- Printed date: 28 Oktober 2025 13.00
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay)
- Quote: "Rata-rata pengeluaran per kapita masyarakat Indonesia untuk makanan dan minuman jadi mencapai Rp248.501 per bulan"
- Caution: page prints the same Rp834,093 for urban and rural food spend (error).

### P1-C1-S8
- Title: Jumlah penduduk miskin di Jakarta turun
- Publisher: ANTARA News; original BPS DKI Jakarta (Susenas Sep 2024)
- URL opened: https://www.antaranews.com/berita/4585326/jumlah-penduduk-miskin-di-jakarta-turun
- Printed date: Rabu, 15 Januari 2025 14:15 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened (relay)
- Quote: "Persentase penduduk miskin pada September 2024 sebesar 4,14 persen, turun 0,16 persen"

## Hypotheses touched

Spend capacity in Jakarta Selatan is high and rising (supports demand side); prepared-food spend is about 549k IDR per capita per month (about 15.5% of total Rp3.53m in 2024, by my division, not stored); the target-age core (25-39) is about 22.7-22.8% of residents in both cities.
