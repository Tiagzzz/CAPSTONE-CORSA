# P2-TFS findings: tax (T-*), franchise (F-*), sentiment indicators (S-*)

Agent P2-TFS, run 2, collected 2026-10-17. Access date for all sources: 2026-10-17. Opened with curl (browser user agent) unless stated. Downloads were kept in the session scratchpad (not committed). Rows: `data/processed/2026-10-p2-tax-franchise.csv` (15 T, 9 F) and `data/processed/2026-10-p2-sentiment-indicators.csv` (11 S). Every quote in both CSVs was machine-checked against the opened text (whitespace-normalised), except the Kepgub 722/2025 PDF (image only, read visually). Decimal commas in sources (73,1) appear as points in value cells.

## Sources (one block per source)

### P2-TFS-S1
- Title: Perda Provinsi DKI Jakarta 1/2024 tentang Pajak Daerah dan Retribusi Daerah (SALINAN, 20 pages in the file)
- Publisher: Bapenda Provinsi DKI Jakarta (copy of the Pemprov DKI Perda)
- URL opened: https://bapenda.jakarta.go.id/peraturan-perpajakan/unduh/perda-nomor-1-tahun-2024-tentang-pajak-dan-retribusi-daerah
- Printed date: set and promulgated 5 Januari 2024
- Tier: 1 (official legal text on the tax authority site)
- Access: opened (PDF text layer)
- Quotes: Art. 53(1) rate 10%; Art. 45(1)-(3); Art. 51; Art. 117-118.

### P2-TFS-S2
- Title: PBJT Makanan dan Minuman (Jenis Pajak page)
- Publisher: Bapenda DKI Jakarta
- URL opened: https://bapenda.jakarta.go.id/jenis/pajak-restoran
- Printed date: none on the page
- Tier: 1
- Access: opened
- Quotes: tarif 10%; Rp42.000.000 per bulan; legal basis PP 35/2023 and Perda 1/2024.

### P2-TFS-S3
- Title: Keputusan Gubernur DKI 722/2025 tentang Pengurangan PBJT atas Jasa Perhotelan dan Makanan dan/atau Minuman
- Publisher: JDIH Provinsi DKI Jakarta (Biro Hukum)
- URL opened: https://jdih.jakarta.go.id/dokumen/detail/14574/... and PDF https://jdih.jakarta.go.id/dokumenPeraturanDirectory/0031/2025KEPGUB0031722.pdf
- Printed date: Tanggal Penetapan 25 Agustus 2025
- Tier: 1
- Access: page opened; PDF is image-only, read visually (3 pages)
- Quotes: Status Peraturan Berlaku; F&B 20% for tax periods Aug to Dec 2025; validity to 31 Januari 2026; E-TRAPT condition.

### P2-TFS-S4
- Title: Gubernur DKI Beri Diskon Pajak Restoran dan Hotel hingga 20 Persen
- Publisher: DDTCNews (relaying a Bapenda statement)
- URL opened: https://news.ddtc.co.id/berita/daerah/1818539/gubernur-dki-beri-diskon-pajak-restoran-dan-hotel-hingga-20-persen
- Printed date: Selasa, 07 April 2026, 12.00 WIB
- Tier: 3
- Access: opened
- Quotes: Kepgub 310/2026, 20%, masa pajak Maret 2026, until 30 April 2026.

### P2-TFS-S5
- Title: Tax Treaty Rates
- Publisher: Direktorat Jenderal Pajak (pajak.go.id)
- URL opened: https://pajak.go.id/index.php/en/tax-treaty-rates
- Printed date: none on the page
- Tier: 1
- Access: opened
- Quotes: Switzerland row (BPT 10%; dividend 15% portfolio / 10% direct; interest 10%; royalty 10%); footnote 6 (5% services, Art. 13).

### P2-TFS-S6
- Title: Agreement between the Republic of Indonesia and the Swiss Confederation for the Avoidance of Double Taxation (file name "Tax Treaty Swiss (Modified by MLI) - EN")
- Publisher: DJP (hosted at pajak.go.id/sites/default/files/2025-05/)
- URL opened: https://pajak.go.id/sites/default/files/2025-05/Tax%20Treaty%20Swiss%20%28Modified%20by%20MLI%29%20-%20EN%20.pdf
- Printed date: signed Berne 29 August 1988 (upload folder 2025-05)
- Tier: 1
- Access: opened. The file is only the 1988 text and protocol; it does not contain the 2007 amending protocol, despite the "Modified by MLI" file name.
- Quotes: Art. 10(2); Art. 12(2) 12.5%; Art. 13(2) 5%.

### P2-TFS-S7
- Title: Switzerland - Indonesia Tax Treaty (page reproducing the Agreement, Protocol and the 2007 amending Protocol)
- Publisher: investinasia.id (commercial investment-advisory site; not an official publisher)
- URL opened: https://investinasia.id/education/tax-treaty/switzerland/
- Printed date: protocol signed Jakarta 8 February 2007; the page has no publication date
- Tier: 4 (reproduction of an official text; used for the protocol wording only and for the mechanism, the 10% rate is corroborated by the tier-1 DJP table S5)
- Access: opened
- Quotes: Protocol Art. 2 replacing the 12.5% with 10%.
- Not opened: Perpres 8/2009 (ratification) via peraturan.bpk.go.id (403) and peraturan.go.id (connection reset).

### P2-TFS-S8
- Title: Aspek Perpajakan Wajib Pajak Badan (DJP education deck, 162 slides)
- Publisher: DJP
- URL opened: https://pajak.go.id/sites/default/files/2026-07/Aspek%20Perpajakan%20WP%20Baru%20Terdaftar%20%28Badan%20dan%20OP%29.pdf
- Printed date: none on slides; upload folder 2026-07; PDF creation date 2026-07-20 (metadata)
- Tier: 1
- Access: opened; the text layer is partial
- Quotes: 22% general; Rp50 miliar; 50% x 22% = 11% under Art. 31E; 19% for listed companies.

### P2-TFS-S9
- Title: Pemotongan Pajak Penghasilan Pasal 26
- Publisher: DJP
- URL opened: https://www.pajak.go.id/id/pemotongan-pajak-penghasilan-pasal-26
- Printed date: none (long-run statutory rule)
- Tier: 1
- Access: opened
- Quotes: 20% where treaty conditions are not met; table lists dividends, royalties, rent, services.

### P2-TFS-S10
- Title: Makan di Restoran Tidak Kena PPN
- Publisher: DJP
- URL opened: https://www.pajak.go.id/id/artikel/makan-di-restoran-tidak-kena-ppn
- Printed date: Kamis, 19 Mei 2022 (pre-window, kept as a statutory long-run rule)
- Tier: 1
- Access: opened
- Quotes: Pasal 4A UU PPN; "tidak dikenakan PPN, namun dikenakan PBJT sebesar 10%".

### P2-TFS-S11
- Title: PMK Terbaru soal PPN 12% Akhirnya Terbit, Begini Perinciannya
- Publisher: DDTCNews
- URL opened: https://news.ddtc.co.id/berita/nasional/1807939/pmk-terbaru-soal-ppn-12-akhirnya-terbit-begini-perinciannya
- Printed date: Rabu, 01 Januari 2025, 12.52 WIB
- Tier: 3
- Access: opened
- Quotes: tarif 12% with DPP nilai lain 11/12. A second DDTC article (https://news.ddtc.co.id/review/konsultasi/1807964/..., 02 Januari 2025) was opened and lists the PMK 131/2024 title (including intangible goods and services from outside the customs area).

### P2-TFS-S12
- Title: Peraturan Pemerintah 35/2024 tentang Waralaba
- Publisher: JDIH Kementerian Perdagangan
- URL opened: https://jdih.kemendag.go.id/peraturan/peraturan-pemerintah-nomor-35-tahun-2024-tentang-waralaba-1 and its PDF (download link file_peraturan)
- Printed date: set and promulgated 2 September 2024 (LN 2024/188)
- Tier: 1
- Access: opened; PDF text layer is OCR with character errors (quotes were chosen from clean passages)
- Quotes: Art. 41 revokes PP 42/2007; Art. 42; Art. 4(5); Art. 12-15; Art. 26-27.

### P2-TFS-S13
- Title: Permendag 71/2019 tentang Penyelenggaraan Waralaba
- Publisher: JDIH Kementerian Perdagangan
- URL opened: https://jdih.kemendag.go.id/peraturan/peraturan-menteri-perdagangan-nomor-71-tahun-2019-penyelenggaraan-waralaba and PDF
- Printed date: 03 September 2019 / 04 September 2019 (BN 2019 No. 1007)
- Tier: 1
- Access: opened
- Quotes: Art. 2(3) five years; Art. 5-8; Art. 18-19; JDIH status Berlaku.

### P2-TFS-S14
- Title: Permendag 25/2025 tentang Tata Cara Penerbitan STPW oleh Pemerintah Daerah
- Publisher: JDIH Kementerian Perdagangan
- URL opened: https://jdih.kemendag.go.id/peraturan/peraturan-menteri-perdagangan-republik-indonesia-nomor-25-tahun-2025-tentang-tata-cara-penerbitan-surat-tanda-pendaftaran-waralaba-oleh-pemerintah-daerah-1 and PDF
- Printed date: 30 June 2025 (BN 2025 No. 458)
- Tier: 1
- Access: opened
- Quotes: Art. 4(11)-(12); Art. 2(1).

### P2-TFS-S15
- Title: Fatwa MUI Nomor 83 Tahun 2023 tentang Hukum Dukungan Terhadap Perjuangan Palestina (PDF)
- Publisher: Komisi Fatwa MUI; hosted by fatwamui.com (third-party host)
- URL opened: https://fatwamui.com/storage/554/Fatwa-MUI-Nomor-83-Tahun-2023-tentang-Hukum-Dukungan-Terhadap-Perjuangan-Palestina.pdf
- Printed date: 8 November 2023 (instrument date)
- Tier: 3 (relay of a tier-1 instrument; mui.or.id unreachable, proxy 502)
- Access: opened
- Quotes: Pertama 4 (haram); Kedua 3 (diimbau).

### P2-TFS-S16
- Title: Survei: Publik Sadar Ada Pihak Diuntungkan di Balik Boikot Produk Terafiliasi Israel
- Publisher: RMOL (relaying a PKAEN survey)
- URL opened: https://rmol.id/nusantara/read/2025/05/15/666584/...
- Printed date: Kamis, 15 Mei 2025, 20:33 WIB
- Tier: 3 (weak: single outlet, unfamiliar survey institute)
- Access: opened
- Quotes: 73,1 persen; 810 responden; MUI has no official list (PKAEN director).

### P2-TFS-S17
- Title: Kenapa Publik RI Setuju untuk Boikot Produk Israel?
- Publisher: GoodStats (relaying Median survey; Median original at median.or.id/2025/09/22/... returned 404)
- URL opened: https://goodstats.id/article/kenapa-publik-ri-setuju-untuk-boikot-produk-israel-n84Sj
- Printed date: 5 Oktober 2025 pukul 09.30 WIB; fieldwork 8-13 September 2025
- Tier: 3
- Access: opened
- Quotes: 80,2% setuju (50,5 + 29,7), 12,8% tidak setuju; n=643; Google Form via Meta.

### P2-TFS-S18
- Title: Gerakan boikot produk diduga terafiliasi Israel jadi momentum kebangkitan brand lokal
- Publisher: Infobanknews
- URL opened: https://infobanknews.com/gerakan-boikot-produk-diduga-terafiliasi-israel-jadi-momentum-kebangkitan-brand-lokal/
- Printed date: Kamis, 06 Maret 2025, 15:55 WIB
- Tier: 3
- Access: opened
- Quotes: 89 persen (Inventure, IMMO 2025).

### P2-TFS-S19
- Title: Massa Aksi Bela Palestina Geruduk Kedubes AS ... (Jawa Pos)
- URL opened: https://www.jawapos.com/nasional/015571966/massa-aksi-bela-palestina-geruduk-kedubes-as-rekayasa-lalin-disiapkan-ribuan-aparat-polisi-dikerahkan
- Printed date: Minggu, 26 Januari 2025, 19.54 WIB
- Tier: 3
- Access: opened

### P2-TFS-S20
- Title: Massa aksi bela Palestina mulai bubarkan diri (Antara)
- URL opened: https://www.antaranews.com/berita/5169289/massa-aksi-bela-palestina-mulai-bubarkan-diri/
- Printed date: Minggu, 12 Oktober 2025 10:52 WIB
- Tier: 3
- Access: opened

### P2-TFS-S21
- Title: Naik 12,7%, Realisasi Investasi Tahun 2025 Tembus Rp 1.931,2 Triliun
- Publisher: Kontan (relaying a Kementerian Investasi dan Hilirisasi/BKPM press conference)
- URL opened: https://nasional.kontan.co.id/news/naik-127-realisasi-investasi-tahun-2025-tembus-rp-19312-triliun
- Printed date: Kamis, 15 Januari 2026 / 14:41 WIB
- Tier: 3
- Access: opened. Metro TV (https://www.metrotvnews.com/read/bmRCY0RP-..., printed 15 July 2026) carries the same PMA and PMDN figures.

### P2-TFS-S22
- Title: Realisasi Investasi Semester I Tembus Rp1.010 T, Mayoritas dari Modal Asing
- Publisher: Katadata
- URL opened: https://katadata.co.id/amp/berita/nasional/6a588db0af3cf/realisasi-investasi-semester-i-tembus-rp1010-t-mayoritas-dari-modal-asing
- Printed date: 16/7/2026, 14.52 WIB
- Tier: 3
- Access: opened

### P2-TFS-S23
- Title: Realisasi Investasi Semester I/2026 Tembus Rp1.010,6 Triliun
- Publisher: DDTCNews
- URL opened: https://news.ddtc.co.id/berita/nasional/1820896/realisasi-investasi-semester-i2026-tembus-rp10106-triliun
- Printed date: Kamis, 16 Juli 2026, 16.30 WIB
- Tier: 3
- Access: opened (independent of S22 as a publisher; both relay the minister's statement)

## Historical / pre-window context (not in the CSVs)
- Populix survey (Infobanknews, Rabu 21 Februari 2024, opened): 65% of Muslim respondents say they comply with Fatwa 83/2023; 26% hesitant; 9% oppose; 94% awareness of the fatwa.
- Compas data (Industry.co.id, 2 Juli 2024, opened): 156 of 206 Israel-affiliated brands showed falling e-commerce sales value in the two-week comparison; F&B 74% of 75 brands fell.
- MUI statements of March 2024 (Bisnis, 10 and 12 March 2024) came up in search results only (not opened).

## Findings that change earlier assumptions
- PP 42/2007 was revoked on 2 Sep 2024 by PP 35/2024. The 5-year experience test of Permendag 71/2019 now conflicts with PP 35/2024 (3 years of operation plus 2 audited profitable years). See F-01, F-04, F-05.
- The DJP-hosted treaty PDF is the 1988 text (royalties 12.5%); the 2007 protocol and the DJP table give 10%. See T-11, T-12.
- PBJT is 10% and statutory. Temporary 20% reductions applied for Aug-Dec 2025 (to 31 Jan 2026) and March 2026. See T-06, T-07.

## Gaps and blocked hosts
- Not done: Q8 labour (time).
- Blocked or unreachable: peraturan.bpk.go.id (403), peraturan.go.id (connection reset), mui.or.id (proxy 502), perpustakaan.dpr.go.id (Access Denied), estv.admin.ch and sif.admin.ch treaty pages (404). median.or.id original 404.
- Official JDIH Jakarta record for Perda 1/2024 not located (the JDIH search endpoint did not return it).
- No 2025-2026 MUI statement and no 2025-2026 brand-outlet protest in Jakarta were found; both are logged as gap rows (S-02, S-08), not as confirmed absences.
- The pure-licence versus franchise boundary (F-07) and the PMK 131/2024 treatment of foreign royalties (T-15) need a tax/legal adviser.
