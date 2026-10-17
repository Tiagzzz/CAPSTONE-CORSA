# Listed operators: filings extraction (Plan 3, task 2e, run 2)

Agent P3-B-filings, access date 2026-10-17. Dataset: `data/processed/listed-operators.csv` (41 rows, ids P3BF-001 to P3BF-041). Temp source keys `P3-B-S<n>`; the registrar assigns CMP- ids.

Method. idx.co.id returns HTTP 403 (Cloudflare) and was not bypassed. Instead the companies' own investor-relations hosts were opened with curl: kfcku.com (FAST), mbai.co.id (MAPB statements, hosted by its auditor's site and linked from the IDX filing), fore.coffee (FORE), plus Detik, Okezone, Stockwatch, Kontan, CNBC Indonesia, Investor.id and EmitenNews. PDFs were saved only in the scratchpad (not committed) and read with pdftotext. Derived values (growth, shares, revenue per outlet) are written only in the notes column with the formula, not as data rows. Revenue per outlet, same-store sales growth and average ticket are NOT printed by any of the five companies in the opened documents; revenue per outlet is DERIVED in notes (revenue / average of opening and closing outlets, not same-store).

## Reconciliation with data/processed/plan4-origin-boycott.csv

No duplicate rows were written. Existing rows already cover: Q6-001/002 (FAST 9M 2025), Q6-004 (FAST 19 closures to Sep 2025), Q6-005/006 (MAPB 9M 2025), Q6-007/008 (PZZA FY2025), Q6-009 and UC-N10 (PZZA 9M 2025), Q6-011 (FAST H1 2025), UC-N08 (FAST outlets 695 at 30 Sep 2025), UC-N09 (FAST FY2025 loss and revenue), UC-N11 (MAPB management). New rows add outlet series, H1/Q1 2026, FY2025 outlets, geography, going concern. Consistency and conflicts:

1. FAST FY2025 net loss Rp366.04 bn (Kontan, Detik) vs Rp369.24 bn (Stockwatch) vs Rp369 bn (Okezone): not a conflict. 366.04 is attributable to owners, 369.24 the consolidated loss. Plan 3 note "366-369" is explained. UC-N09 is correct.
2. FAST closures: "19 closed" (2 Oct 2025 expose, Q6-004), "20 closed" (Bisnis/CNBC to Sep, UC-N08), "25 closed" (headline of a relay, FY2025). Net outlet change is 715 to 695 (Sep) to 690 (Dec). The three counts use different cut-offs; gross closures vs net change not resolved. Outlet counts themselves agree across the FAST filing (690, 686, 682), Detik and Okezone.
3. MAPB: filing values match Q6-005/006 (9M 2025 sales 2,354,383 m, loss 108.69 bn from CNBC). MAPB FY2025 loss Rp150.767 bn (filing) vs Rp150.765 bn (press snippet): rounding. H1 2026 foods Rp644.88 bn (Harian Energi) vs Rp638.841 bn (filing): the filing is used.
4. PZZA: FY2025 profit and sales in Q6-007/008 unchanged; the plan's "Rp24.75 bn, Rp3.05 trn" confirmed by Detik and Investor.id. New: H1 2026 profit Rp8.27 bn vs EmitenNews headline Rp8.4 bn and a lead sentence that calls the prior-year profit "nihil" (body and Investor.id say Rp15.56 bn); body used, conflict recorded in the notes.
5. FORE: the plan has no outlet series; the annual report gives 232 (Dec 2024) and 322 (Dec 2025), and the H1 2026 FS gives 377 (30 Jun 2026). The annual report map prints "Grand Total 324", text says 322; text used.
6. ENAK: plan said "latest filing not found". Q3 2025 (9M) FS opened via an Indopremier-hosted copy of the IDX filing; FY2025 and later are on IDX only (403).

## Hypotheses touched

- H5 (mid-market casual dining under pressure): MIXED. Supports: FAST outlets down for six straight reporting dates (715 to 682), going-concern uncertainty in H1 2026 FS, Q2 2026 stand-alone loss about Rp73.8 bn (derived) after a Q1 profit; MAPB losses widening (FY2025 Rp150.8 bn, H1 2026 Rp121.5 bn); ENAK 9M 2025 swing to a Rp37.0 bn loss with Jabodetabek sales -10.6% (derived); PZZA H1 2026 revenue -4.5% and profit halved. Disconfirms: FAST H1 2026 revenue +16.1% and loss cut by more than half; PZZA outlets rising again (575 to 579) and profitable for six quarters; MAPB sales +9.9% in H1 2026; Fore revenue +44% (FY2025) and +51.7% (H1 2026) with profit; the MAPI group H1 2026 net profit +26.9%.
- H2 (specialty coffee saturation by low-price chains): MIXED-TO-DISCONFIRMING on profitability. Fore, the low-price chain leader, is profitable and still adding about 55 outlets per half-year, 47% of its network in Jabodetabek; this says the chain segment is crowded in Jakarta but not unprofitable. Venue density is for the Plan 3 venue-count work to test.
- H7 not touched.

## Gaps

- Same-store sales growth, average ticket, transactions: not disclosed in any opened FS or annual report (Fore annual report names SSSG as a goal but prints no number).
- Outlet counts in Jakarta only (DKI): not disclosed by any of the five. Closest: FAST Jakarta RSC revenue Rp980.0 bn of Rp2,789.9 bn in H1 2026 (region); ENAK Jabodetabek sales share 58.8% (9M 2025); Fore Jabodetabek 149 Fore Coffee + 2 Fore Donut (Dec 2025).
- MAPB total and Starbucks outlet count (any date in 2025-2026): not in the FS; the official Starbucks Indonesia page says 500+ outlets in 59 cities at end 2023 (undated, historical). Bisnis.com (403) and mapboga.co.id (no response) not opened.
- ENAK FY2025, Q1 2026 and H1 2026 results and outlet counts: IDX files found by search (202605/04f6561fde_d800dd309f.pdf; ENAK_LK Q1 2026.pdf) but HTTP 403; row P3BF-040 records the gap.
- PZZA H1 2026 and FY2025: statements themselves not opened (IDX 403; sarimelati.co.id no response); only relays. FY2024 net loss Rp72.83 bn comes via Detik/Q6-007.
- Kopi Kenangan, Tomoro, Starbucks-level private chains: no public filing found in this run (not listed). Kopi Kenangan was not pursued further.
- FAST Jakarta outlet count and per-brand (KFC vs Taco Bell) split: not printed.

## Blocked hosts

idx.co.id (403, all StaticData PDFs), bisnis.com (403), tempo.co (403), mapboga.co.id and sarimelati.co.id (no response), investor.fore.coffee (no response; fore.coffee itself works), stockwatch.id MAPB Q1 2026 page (404).

## Sources

### P3-B-S1
- Title: Fast Food Indonesia Tbk consolidated interim financial statements as of 30 June 2026 (unaudited), six months
- Publisher: PT Fast Food Indonesia Tbk (company IR page https://kfcku.com/financial-report; the IDX filing is the original)
- URL opened: https://files.kfcku.com/uploads/media/fast-food-indonesia-tbk_consolidation_30jun26.pdf
- Printed publication date: statements authorised for issue by the Board on 13 August 2026 (printed in the notes)
- Access date: 2026-10-17
- Proposed tier: 1 (company filing, official regulatory disclosure)
- Access status: opened (PDF, 20 pages in the extract; read with pdftotext; not committed)
- Quotes: "As of June 30, 2026, the Company operates 682 restaurant outlets (December 31, 2025: 690 restaurant outlets) (unaudited)." "PENDAPATAN 2.789.865.271 ... 2.403.271.439 REVENUES"; "RUGI PERIODE BERJALAN (61.146.624) (142.312.383) LOSS FOR THE PERIOD"; segment table "Pendapatan 979.989.184 [RSC Jakarta] ..."; going-concern paragraph "present uncertainties ... going concern".

### P3-B-S2
- Title: Fast Food Indonesia Tbk consolidated financial statements as of 31 March 2026 (unaudited)
- Publisher: PT Fast Food Indonesia Tbk (https://kfcku.com/financial-report)
- URL opened: https://files.kfcku.com/uploads/media/fast-food-indonesia-tbk_consolidation_31_mar_26_1.pdf
- Printed publication date: Jakarta, 22 May 2026 (printed on the cover/signature page)
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: opened
- Quotes: "mengoperasikan 686 gerai restoran (31 Desember 2025: 690 gerai restoran) (tidak diaudit)"; "PENDAPATAN 1.423.117.899 ... 1.199.965.514"; "LABA (RUGI) PERIODE BERJALAN 12.664.192) (40.079.596)".

### P3-B-S3
- Title: KFC vs CFC vs Pizza Hut, Siapa Paling Laku?
- Publisher: Detik (detikFinance), relaying IDX Keterbukaan Informasi filings
- URL opened: https://finance.detik.com/bursa-dan-valas/d-8452609/kfc-vs-cfc-vs-pizza-hut-siapa-paling-laku
- Printed publication date: Senin, 20 Apr 2026 13:52 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (major news outlet reporting the filing; original not opened)
- Access status: opened
- Quotes: "FAST mengoperasikan 690 gerai restoran KFC hingga akhir Desember 2025, turun dibanding posisi akhir 2024 yakni sebanyak 715 gerai."; "Per tanggal 31 Desember 2025, perseroan mengoperasikan gerai Pizza Hut sebanyak 575. Angka tersebut turun dibanding posisi akhir 2024, yakni sebanyak 591 gerai Pizza Hut"; "laba tahun berjalan ... Rp 19,38 miliar sepanjang tahun 2025 dari Rp 21,03 miliar di tahun 2024"; "CSMI membukukan rugi bersih sebesar Rp 955,25 juta".

### P3-B-S4
- Title: KFC Masih Rugi Rp369 Miliar di 2025, Tutup Puluhan Gerai
- Publisher: Okezone Economy, relaying IDX disclosure
- URL opened: https://economy.okezone.com/read/2026/04/20/278/3213518/kfc-masih-rugi-rp369-miliar-di-2025-tutup-puluhan-gerai?page=all
- Printed publication date: Senin, 20 April 2026 13:31 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Berkurangnya beban itu juga sejalan dengan jumlah gerai yang turun dari 715 menjadi 690 gerai."; "FAST mempunyai 11.664 karyawan, turun dari posisi akhir 2024 yakni sebanyak 13.106 karyawan."; "Rugi operasional turun tajam hingga 60 persen menjadi Rp312 miliar."

### P3-B-S5
- Title: Pengelola KFC (FAST) Sukses Pangkas Rugi Bersih Hingga 53,74% pada 2025
- Publisher: StockWatch
- URL opened: https://stockwatch.id/pengelola-kfc-fast-sukses-pangkas-rugi-bersih-hingga-5374-pada-2025/
- Printed publication date: April 19, 2026
- Access date: 2026-10-17
- Proposed tier: 3 (financial news site, clear editorial identity; single outlet for the auditor note, treat as weak until the FY2025 audit report is opened)
- Access status: opened
- Quotes: "auditor independen dari KAP Purwanto, Susanti dan Surja memberikan catatan terkait ketidakpastian material kelangsungan usaha ... akumulasi kerugian FAST mencapai Rp507,63 miliar"; "rugi sebesar Rp369,24 miliar ... Rp798,25 miliar".

### P3-B-S6
- Title: Pengelola Gerai KFC (FAST) Catat Rugi Rp 366 Miliar pada Tahun 2025
- Publisher: Kontan (investasi.kontan.co.id)
- URL opened: https://investasi.kontan.co.id/news/pengelola-gerai-kfc-fast-catat-rugi-rp-366-miliar-pada-tahun-2025
- Printed publication date: Minggu, 19 April 2026 15:09 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "FAST melaporkan rugi bersih sebesar Rp 366,04 miliar di tahun 2025 ... Rp 796,711 miliar"; "Penjualan dan pendapatan usaha FAST tercatat sebesar Rp 4,88 triliun ... naik tipis 0,11% yoy ... Rp 4,87 triliun". Used for reconciliation notes only (the FY2025 loss row already exists as UC-N09).

### P3-B-S7
- Title: PT MAP Boga Adiperkasa Tbk and subsidiaries, interim consolidated financial statements 30 June 2026 (unaudited)
- Publisher: PT MAP Boga Adiperkasa Tbk; copy hosted by mbai.co.id (auditor/IR host linked from the MAPB IDX filing)
- URL opened: https://www.mbai.co.id/wp-content/uploads/2026/07/FS-MAPB-1H-2026.pdf
- Printed publication date: approved for issue 27 July 2026 (printed in the notes)
- Access date: 2026-10-17
- Proposed tier: 1 (company filing; host is a third-party mirror, content is the company's statements)
- Access status: opened
- Quotes: "PENJUALAN 23 1.670.827 1.520.542 SALES"; "RUGI BERSIH PERIODE BERJALAN (121.506) (80.206) NET LOSS FOR THE PERIOD"; "Minuman 934.485 850.939; Makanan 638.841 589.162; Lain-lain 97.501 80.441".

### P3-B-S8
- Title: PT MAP Boga Adiperkasa Tbk and subsidiaries, consolidated financial statements 31 December 2025 (audited)
- Publisher: PT MAP Boga Adiperkasa Tbk; copy at mbai.co.id
- URL opened: https://www.mbai.co.id/wp-content/uploads/2026/03/PT-MAP-BOGA-ADIPERKASA-Tbk-31-DECEMBER-2025LR.pdf
- Printed publication date: authorised for issue 26 March 2026
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: opened
- Quotes: "PENJUALAN 24 3.236.043 3.228.133 SALES"; "RUGI BERSIH TAHUN BERJALAN (150.767) (146.148) NET LOSS FOR THE YEAR".

### P3-B-S9
- Title: Semester I/2026, Rugi Pengelola Starbucks MAPB Naik Jadi Rp121,50 Miliar
- Publisher: Harian Energi (relay of Bisnis.com report)
- URL opened: https://harianenergi.com/detail/1435008/semester-i2026-rugi-pengelola-starbucks-mapb-naik-jadi-rp12150-miliar
- Printed publication date: Kamis, 30 Juli 2026 03:17 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (weak: small outlet; used only to corroborate S7 and to record the foods-sales discrepancy)
- Access status: opened
- Quotes: "rugi periode berjalan ... melonjak naik hingga mencapai Rp121,50 miliar"; "pendapatan ... 9,88% YoY menjadi Rp1,67 triliun".

### P3-B-S10
- Title: Rugi MAPB Bengkak Jadi Rp108 M, Starbucks Sudah Ditinggal Warga RI?
- Publisher: CNBC Indonesia
- URL opened: https://www.cnbcindonesia.com/market/20251105153124-17-682591/rugi-mapb-bengkak-jadi-rp108-m-starbucks-sudah-ditinggal-warga-ri
- Printed publication date: 05 November 2025 15:43
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Atas kondisi tersebut, Starbucks menutup 11 gerainya. Selain itu, perseroan juga mengerem ekspansi gerainya menjadi 10-15 gerai per tahun"; "sejak tahun lalu, Starbucks secara resmi sudah dihapus dari daftar boikot".

### P3-B-S11
- Title: MAP Delivers Resilient Growth in H1'26 (2Q 2026 Financial Report Press Release)
- Publisher: PT Mitra Adiperkasa Tbk (map.co.id)
- URL opened: https://www.map.co.id/corporate-en/2q-2026-financial-report-press-release/
- Printed publication date: Jul 29, 2026
- Access date: 2026-10-17
- Proposed tier: 1 (company press release; parent group, context)
- Access status: opened
- Quotes: "For the first half of 2026, MAP reported a 23.4% growth in net revenue to Rp24.2 trillion ... Net profit for the period increased by 26.9% to Rp1.5 trillion."

### P3-B-S12
- Title: Starbucks in Indonesia (about us)
- Publisher: Starbucks Coffee Indonesia (starbucks.co.id)
- URL opened: https://www.starbucks.co.id/about-us/our-heritage/starbucks-in-indonesia
- Printed publication date: none printed (page text refers to end of 2023; treated as historical)
- Access date: 2026-10-17
- Proposed tier: 1 for the company's own statement, but undated; no CSV row relies on it (gap only)
- Access status: opened
- Quotes: "Jaringan Starbucks Coffee Indonesia telah berkembang di lebih dari 500 gerai di 59 kota besar di Indonesia pada akhir tahun 2023."

### P3-B-S13
- Title: Gerai Pizza Hut di Indonesia, Nasibnya Sekarang
- Publisher: Investor.id (Beritasatu group)
- URL opened: https://investor.id/market/455625/gerai-pizza-hut-di-indonesia-nasibnyasekarang
- Printed publication date: 26 Sep 2026 15:32 WIB
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "Sampai dengan 30 Juni 2026, PZZA mengoperasikan 579 gerai Pizza Hut. Sedangkan, per 31 Desember 2025, perusahaan mengoperasikan 575 gerai"; "laba bersih perseroan juga menyusut ke Rp 8,27 miliar dari Rp 15,56 miliar"; "per tanggal 30 Juni 2026 Grup PZZA memiliki 4.085 karyawan tetap".

### P3-B-S14
- Title: Akhiri Episode Negatif, PZZA Tabulasi Laba Rp8,4 Miliar
- Publisher: EmitenNews
- URL opened: https://www.emitennews.com/news/akhiri-episode-negatif-pzza-tabulasi-laba-rp84-miliar
- Printed publication date: 08/08/2026, 17:00 WIB
- Access date: 2026-10-17
- Proposed tier: 3 (financial news; headline and lead conflict with body, see notes)
- Access status: opened
- Quotes: "Pendapatan Rp1,47 triliun, merosot 4,54 persen dari fase sama tahun sebelumnya Rp1,54 triliun."; "Laba bersih tahun berjalan Rp8,27 miliar, anjlok dari Rp15,56 miliar."

### P3-B-S15
- Title: Konsisten Raih Cuan, Pizza Hut Cetak Laba Rp6 M di Kuartal I-2026
- Publisher: CNBC Indonesia (company statement, Kamis 7 May 2026)
- URL opened: https://www.cnbcindonesia.com/market/20260508151832-17-733517/konsisten-raih-cuan-pizza-hut-cetak-laba-rp6-m-di-kuartal-i-2026
- Printed publication date: 08 May 2026 15:42
- Access date: 2026-10-17
- Proposed tier: 3
- Access status: opened
- Quotes: "PZZA berhasil membukukan laba bersih sebesar Rp6 miliar di kuartal pertama 2026 ... penjualan bersih sebesar Rp727 miliar, atau tumbuh 2,8% secara tahunan"; "membuka 6 outlet baru ... renovasi 21 outlet".

### P3-B-S16
- Title: PT Champ Resto Indonesia Tbk financial statements 30 September 2025 (unaudited)
- Publisher: PT Champ Resto Indonesia Tbk (IDX filing; copy hosted by Indopremier)
- URL opened: https://indopremier.com/xdir/news/LAPORAN%20KEUANGAN/2025/q3///ENAK_Q3_2025.pdf
- Printed publication date: approved for issue 31 October 2025
- Access date: 2026-10-17
- Proposed tier: 1 (company filing; host is a broker mirror of the IDX file)
- Access status: opened
- Quotes: "Jumlah gerai ... Gerai 347 331"; "PENJUALAN BERSIH 32 1.082.249.545.982 1.165.071.929.910"; "LABA (RUGI) TAHUN BERJALAN (37.038.719.349) 19.743.258.088"; geography segment "Penjualan 636.036.718.113 290.388.250.090 155.824.577.779 1.082.249.545.982".

### P3-B-S17
- Title: PT Fore Kopi Indonesia Tbk interim consolidated financial statements 30 June 2026 (unaudited)
- Publisher: PT Fore Kopi Indonesia Tbk (https://fore.coffee/investors-annual-report/)
- URL opened: https://fore.coffee/wp-content/uploads/2026/07/FORE-Financial-Report-1H26-Unaudited.pdf
- Printed publication date: authorised for issue 17 July 2026
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: opened
- Quotes: "Kedai kopi 363 316; Gerai donat 10 2; Singapura Kedai kopi 4 4"; "PENJUALAN NETO 1.004.934.782.303 18 662.372.756.900"; "LABA PERIODE BERJALAN 56.488.819.450 42.031.093.163".

### P3-B-S18
- Title: Annual Report 2025, PT Fore Kopi Indonesia Tbk (outlet map)
- Publisher: PT Fore Kopi Indonesia Tbk
- URL opened: https://fore.coffee/wp-content/uploads/2026/04/Annual-Report-FORE-2025.pdf
- Printed publication date: not printed on the pages read; URL path 2026/04 (URL-inferred); the AGMS 2026 was announced in April 2026
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: opened
- Quotes: "Jabodetabek • 149 Fore Coffee • 2 Fore Donut"; "Jumlah outlet Fore Coffee Indonesia yang aktif dan dimiliki Perseroan di Indonesia pada akhir tahun 2025 berjumlah 316, yang terdiri dari 98 Satellite outlet, 204 Medium outlet, dan 14 Flagship outlet ... 57 kota dan 22 provinsi"; "pertumbuhan pendapatan sebesar 44% (YoY) ... pertumbuhan laba bersih ... 55% (YoY)".

### P3-B-S19
- Not used (key withdrawn: the 322-outlet statement was read in the Annual Report 2025, S18). Kept as a placeholder so S20 to S22 keep their numbers.

### P3-B-S20
- Title: PT Fore Kopi Indonesia Tbk consolidated financial statements 31 December 2025 (audited)
- Publisher: PT Fore Kopi Indonesia Tbk
- URL opened: https://fore.coffee/wp-content/uploads/2026/03/FORE-Financial-Report-FY-2025-Audited.pdf
- Printed publication date: authorised for issue 30 March 2026
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: opened
- Quotes: "PENJUALAN NETO 1.497.134.772.364 18 1.038.659.233.501 NET SALES"; "LABA TAHUN BERJALAN 90.133.042.112 58.219.108.464 INCOME FOR THE YEAR"; "harga penawaran sebesar Rp188 per lembar saham. Pada tanggal 14 April 2025, saham Perusahaan telah dicatatkan di Bursa Efek Indonesia."

### P3-B-S21
- Title: IDX filings for ENAK (annual report 2025; Q1 2026 financial statements)
- Publisher: Indonesia Stock Exchange (idx.co.id)
- URLs attempted: https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/From_EREP/202605/04f6561fde_d800dd309f.pdf and .../202604/20260430220814-62259-0/ENAK_LK%20Q1%202026.pdf
- Printed publication date: not seen (file names suggest April-May 2026, URL-inferred)
- Access date: 2026-10-17
- Proposed tier: 1
- Access status: BLOCKED (HTTP 403, Cloudflare); not bypassed; no figure taken from them
- Quotes: none.

### P3-B-S22
- Title: Laporan Hasil Paparan Publik Tahunan 2026 (Q&A with Kontan)
- Publisher: PT Fore Kopi Indonesia Tbk
- URL opened: https://fore.coffee/wp-content/uploads/2026/05/Laporan-Hasil-Public-Expose-FORE-2026.pdf
- Printed publication date: Senin, 11 Mei 2026
- Access date: 2026-10-17
- Proposed tier: 1 (company statement of intent, management guidance)
- Access status: opened
- Quotes: "target pembukaan gerai baru akan sedikit lebih banyak, yakni mencapai 100 outlet"; "CAPEX tahun ini direncanakan sebesar kurang lebih Rp250 miliar"; "Ekspektasi pertumbuhan top line Perseroan pada tahun ini adalah sekitar 50% ... net profit ... sekitar 70%".
