# Run 2 verification C: population-spend.csv and middle-class-income.csv

Verifier V2-C, 2026-10-17. All sources were opened with curl (original BI SK-September-2026.pdf and World Bank IEP June 2026 PDF read with pdftotext; BI tables 2, 5, 6 rendered to images and read, Jakarta row zoomed). No data files or sources.md were edited. Publication dates of all registered sources are on or after 2024-10-16 (earliest: Kontan 2024-12-11, Databoks 2024-12-03).

## Key findings

1. **47.85M year conflict:** 2024 is correct (BPS Susenas March 2024, 17.13%, down from 57.33M in 2019). Kontan's 2021 is a typo (the same sentence also prints 17.1% for 2024 and 21.5% for 2029 instead of 2019). Evidence opened: detikFinance 30 Aug 2024 and Katadata (both pre-cutoff, notes use only). Row P1C2-06 CORRECTED-OPENED.
2. **DERIVED 25-39 rows:** both re-added correctly (244,600 and 535,920), formulas in notes, labelled DERIVED. P1C1-P07 (total 1,072,640) is a derived worker sum, not printed (page says 1.07 million), and its arithmetic is off by 10 (bands give 1,072,650; 60+ is 128,630 not 128,620): DERIVED-MOVE.
3. **BI image-table values** (rows 14, 18, 20 and the notes of 14): all re-read and match (Table 2 >Rp5m 123.5/123.9/124.8; Table 5 >Rp5m saving 16.9 vs 14.4, consumption 72.0 vs 71.8; Table 6 Jakarta 146.8, Aug 2026 150.0, Sep 2025 145.5).
4. **Periods:** E01 (DKI prepared food, March 2026) and E06 (national, March 2025) are labelled with different periods and no ratio is computed; DKI F01 (2025) and E02-E05 (2024) are also separately labelled. No cross-period comparison found. Row 26 is Q1 2026 (not Q2). P1C2-29 and -31 have period wording inferred from the article (see fixes).
5. **Systemic:** all but 8 rows are tier-3 relays of BPS/Mandiri/BRI originals (BPS, Mandiri, BRI not opened). Databoks E02-E05 are teaser-only premium pages. MSI group definitions (savings balance, not expenditure class) must not be mixed with BPS expenditure classes in analysis (rows 30-33). No tier-4 source found.

## Row table

| file | row_id | register_id | verdict | quote found | fix |
|---|---|---|---|---|---|
| population-spend.csv | P1C1-P01 | DEM-028 | VERIFIED-OPENED (relay) | Age 20-24 years: 85,450 (7.97%) | none |
| population-spend.csv | P1C1-P02 | DEM-028 | VERIFIED-OPENED (relay) | Age 25-29 years: 81,880 (7.63%) | none |
| population-spend.csv | P1C1-P03 | DEM-028 | VERIFIED-OPENED (relay) | Age 30-34 years: 81,020 (7.55%) | none |
| population-spend.csv | P1C1-P04 | DEM-028 | VERIFIED-OPENED (relay) | Age 35-39 years: 81,700 (7.62%) | none |
| population-spend.csv | P1C1-P05 | DEM-028 | VERIFIED-OPENED (relay) | Age 40-44 years: 89,140 (8.31%) | none |
| population-spend.csv | P1C1-S01 | DEM-029 | VERIFIED-OPENED (relay) | Age 20-24 years: 190,740 (8.09%) | none |
| population-spend.csv | P1C1-S02 | DEM-029 | VERIFIED-OPENED (relay) | Age 25-29: 179,370 (7.6%) | none |
| population-spend.csv | P1C1-S03 | DEM-029 | VERIFIED-OPENED (relay) | Age 30-34: 178,390 (7.56%) | none |
| population-spend.csv | P1C1-S04 | DEM-029 | VERIFIED-OPENED (relay) | Age 35-39: 178,160 (7.55%) | none |
| population-spend.csv | P1C1-S05 | DEM-029 | VERIFIED-OPENED (relay) | Age 40-44: 201,240 (8.53%) | none |
| population-spend.csv | P1C1-S07 | DEM-029 | VERIFIED-OPENED (relay) | South Jakarta's population was recorded at 2.36 million in 2024 | none |
| population-spend.csv | P1C1-E01 | DEM-031 | VERIFIED-OPENED (relay) | makanan dan minuman jadi ... Rp 524.958 per kapita per bulan (Maret 2026; CNBC 7 Oct 2026) | none |
| population-spend.csv | P1C1-E02 | DEM-030 | VERIFIED-OPENED (relay) | Selatan ... pertumbuhan 25 persen dengan nilai pengeluaran Rp 548.413 (teaser, 2024) | none |
| population-spend.csv | P1C1-E03 | DEM-030 | VERIFIED-OPENED (relay) | Jakarta Pusat 2024 Rp 513.174 (teaser) | none |
| population-spend.csv | P1C1-E04 | DEM-030 | VERIFIED-OPENED (relay) | Utara Rp 556.691 (+9,4%) (teaser) | none |
| population-spend.csv | P1C1-E05 | DEM-030 | VERIFIED-OPENED (relay) | Barat -5,8% Rp 454.710 (teaser) | none |
| population-spend.csv | P1C1-E06 | DEM-032 | VERIFIED-OPENED (relay) | Rp248.501 per bulan (GoodStats 28 Oct 2025; BPS Maret 2025 report named) | none |
| population-spend.csv | P1C1-F01 | DEM-004 | VERIFIED-OPENED (relay) | Rp1.153.404 (38,93%) makanan; total Rp2.962.412 (2025) | none |
| population-spend.csv | P1C1-F02 | DEM-004 | VERIFIED-OPENED (relay) | Porsi Makanan 39,66% (2024) 38,93% (2025) | none |
| population-spend.csv | P1C1-F03 | DEM-020 | VERIFIED-OPENED (relay) | Porsi makanan 34,96% (2025) | none |
| population-spend.csv | P1C1-F04 | DEM-020 | VERIFIED-OPENED (relay) | Porsi Makanan 38,08% (2024) | none |
| population-spend.csv | P1C1-F05 | DEM-020 | VERIFIED-OPENED (relay) | Rp4.083.229 per kapita/bulan (2025) | none |
| population-spend.csv | P1C1-C01 | DEM-033 | VERIFIED-OPENED (relay) | penduduk miskin September 2024 sebesar 4,14 persen (449,07 ribu orang), Antara 15 Jan 2025 | none |
| population-spend.csv | P1C1-P06 | DEM-028 | VERIFIED-OPENED (relay) (DERIVED, label kept) | Components 81,880 + 81,020 + 81,700 re-added = 244,600 (correct); formula is in notes | none; formula present; plan-required derived row (lesson f exception) |
| population-spend.csv | P1C1-S06 | DEM-029 | VERIFIED-OPENED (relay) (DERIVED, label kept) | 179,370 + 178,390 + 178,160 re-added = 535,920 (correct); formula in notes | none; formula present; plan-required derived row |
| population-spend.csv | P1C1-P07 | DEM-028 | DERIVED-MOVE | Page prints only "Central Jakarta's population was recorded at 1.07 million in 2024"; 1,072,640 is a worker sum. Page bands sum to 1,072,650; the notes cite 128,620 for age 60+ but bands give 49,520+34,470+22,260+22,380 = 128,630, and 128,620 is not printed | Move to notes; value row = 1.07 million (printed, rounded). Fix P06 note share base accordingly (22.80% unchanged) |
| middle-class-income.csv | P1C2-14 | DEM-034 | VERIFIED-OPENED (original) | IKK tertinggi ... kelompok >Rp5 juta sebesar 123,5 (Grafik 2); Tabel 2 image p9: >Rp5 juta Sep 2026 123,5, Aug 2026 123,9, Sep 2025 124,8; Rp4,1-5 juta 122,2; Rp1-2 juta 107,1 | none |
| middle-class-income.csv | P1C2-17 | DEM-034 | VERIFIED-OPENED (original) | IKK ... usia 20-30 tahun sebesar 127,9 (Grafik 3); IPDG 116,1 and 109,2 (Grafik 10, text) | optional: split IKK (127.9) and IPDG (116.1/109.2) into two rows; the value cell mixes two indices (labelled) |
| middle-class-income.csv | P1C2-18 | DEM-034 | VERIFIED-OPENED (original) | Tabel 5 image p12, >Rp5 juta: Konsumsi Sep 2025 71,8 / Sep 2026 72,0; Tabungan 14,4 / 16,9 (Aug 2026 17,4, change -0,5) | none |
| middle-class-income.csv | P1C2-20 | DEM-034 | VERIFIED-OPENED (original) | Tabel 6 image p13, Jakarta IKK: Sep 2025 145,5; Aug 2026 150,0; Sep 2026 146,8; change -3,2 (zoomed at 220 dpi) | none |
| middle-class-income.csv | P1C2-01 | DEM-035 | VERIFIED-OPENED (relay) | turun dari 47,9 juta (2024) menjadi 46,7 juta (2025) ... 16,6%; Kontan 8 Feb 2026 15:43 | none (GoodStats 1 Mar 2026 prints -1,2 juta; note kept in worker notes) |
| middle-class-income.csv | P1C2-02 | DEM-035 | VERIFIED-OPENED (relay) | aspiring middle class 137,5 juta (2024) -> 142,0 juta (2025), 50,4% | none |
| middle-class-income.csv | P1C2-03 | DEM-035 | VERIFIED-OPENED (relay) | upper class 0,4% ... 1,2 juta (2025), naik tipis dari 1,1 juta | none |
| middle-class-income.csv | P1C2-04 | DEM-036 | VERIFIED-OPENED (relay) | Menengah: 3,5-17 kali garis kemiskinan; Menuju: 1,5-3,5; Atas >17 (GoodStats 24 Feb 2026); World Bank IEP fn 18 also confirms 3.5-17x (original) | none |
| middle-class-income.csv | P1C2-05 | DEM-037 | VERIFIED-OPENED (relay) | 57,33 juta (2019) ... 21,5% "pada 2029" (printed typo for 2019); Kontan 5 May 2025 | none (typo already recorded) |
| middle-class-income.csv | P1C2-06 | DEM-037 | CORRECTED-OPENED | Kontan prints "47,85 juta pada 2021" but also "17,1% pada 2024". Opened detikFinance (Fri 30 Aug 2024 21:15) "BPS mencatat jumlah kelas menengah ... 47,85 juta jiwa pada 2024 ... 17,13% ... dari 57,33 juta" and Katadata (Susenas Maret 2024, 57,33 -> 47,85 juta). Mandiri 47,9m (2024) agrees | Set year to 2024 (Susenas March 2024, 17.13%); keep Kontan "2021" as a recorded printed typo. detik/Katadata pages are dated 2024-08/30, before the 2024-10-16 cut-off: use them only in notes as year evidence, not as the row source. Do not use the 2021 BPS figure (53.83m per other outlets) |
| middle-class-income.csv | P1C2-07 | DEM-038 | VERIFIED-OPENED (relay) | jumlah kelas menengah masih mencapai sekitar 59,5 juta orang (2018 comparison), Kontan 27 May 2026 | none |
| middle-class-income.csv | P1C2-08 | DEM-035 | VERIFIED-OPENED (relay) | konsumsi per kapita kelas menengah 4,1% yoy vs nasional 4,6%; upper 6,8% (2025) | none |
| middle-class-income.csv | P1C2-09 | DEM-035 | VERIFIED-OPENED (relay) | non-food 6,4% yoy (3,2% in 2024); food 0,9% (4,6% in 2024) | none |
| middle-class-income.csv | P1C2-10 | DEM-039 | VERIFIED-OPENED (original) | WB IEP June 2026: "from 14.5 percent in 2018 to 7.1 percent in 2025 (Figure B.1.1)" | none |
| middle-class-income.csv | P1C2-11 | DEM-039 | VERIFIED-OPENED (original) | WB: medium and high-skilled fell about 1 and 2 percent per year; overall -0.5 (CAGR median real wage); low-skilled about 1.7 a year | none |
| middle-class-income.csv | P1C2-12 | DEM-039 | VERIFIED-OPENED (original) | WB: formal wage employment tertiary 74.1 percent (2018) to 67.8 percent (2025) | none |
| middle-class-income.csv | P1C2-13 | DEM-039 | VERIFIED-OPENED (original) | WB: "Household consumption remained the main driver of growth, accounting for 54 percent of growth" (Q1 2026, GDP 5.6% yoy); Table A.2 Private Consumption 5.0 (2026f) | none (54% is share of Q1 growth, not a growth rate; label already says so) |
| middle-class-income.csv | P1C2-21 | DEM-040 | VERIFIED-OPENED (relay) | UMP Jakarta 2026 ditetapkan sebesar Rp5.729.876 atau naik 6,17 persen; Kompas TV 26 Dec 2025; 5,729,876/5,396,761 = +6.17% consistent | none |
| middle-class-income.csv | P1C2-22 | DEM-041 | VERIFIED-OPENED (relay) | UMP Jakarta 2025 naik 6,5 persen atau setara Rp 329.380 ... Rp 5.396.761; Kontan 11 Dec 2024 13:45 (photo caption 21/10/2024 is not the article date) | none |
| middle-class-income.csv | P1C2-23 | DEM-042 | VERIFIED-OPENED (relay) | Jakarta Rp5,9 juta Agustus 2025; Rp5,81 juta Agustus 2024; nasional Rp3,33 juta; GoodStats 14 Nov 2025 | none |
| middle-class-income.csv | P1C2-24 | DEM-043 | VERIFIED-OPENED (relay) | Diploma IV/S1-S3 Rp4,8 juta; Dipl I-III 4,5; SMK 3,26; SMA 3,15; SMP 2,48; SD 2,19 (GoodStats 9 Nov 2025) | none |
| middle-class-income.csv | P1C2-26 | DEM-044 | VERIFIED-OPENED (relay) | wealthy 8.0% yoy Q1 2026 (est.), middle 3.5%, lower 3.6%; Investortrust 9 Aug 2026; period Q1 2026 not Q2 | none |
| middle-class-income.csv | P1C2-27 | DEM-044 | VERIFIED-OPENED (relay) | deposits over Rp 2 billion +15.99% yoy April 2026; Rp100-500 million +3.15% | none |
| middle-class-income.csv | P1C2-28 | DEM-045 | VERIFIED-OPENED (relay) | DKI Jakarta gini ratio 0,435, nasional 0,368 (Maret 2026); GoodStats 11 Aug 2026 | none (March 2026 vs March 2026, same period) |
| middle-class-income.csv | P1C2-29 | DEM-046 | VERIFIED-OPENED (relay) | belanja restoran tumbuh 4,7% YoY ... tahun lalu 6,1%; MSI Q3-2026 5,9%; Sep 5,5% terendah sejak November 2025; Kontan 12 Oct 2026 | Note only: the article does not print that 4,7% is Q3 (it sits in the Q3 paragraph) or that 6,1% is Q3 2025 vs full 2025 ("tahun lalu"); mark period "Q3 2026 (inferred from paragraph)" |
| middle-class-income.csv | P1C2-30 | DEM-046 | VERIFIED-OPENED (relay) | tabungan menengah 100,5 (-0,1% MoM); atas 95,1 vs 94,0; bawah 68,7 and 687,1 both printed | none; add to notes that MSI groups are defined by savings balance (middle Rp1-10m), already stated |
| middle-class-income.csv | P1C2-31 | DEM-047 | VERIFIED-OPENED (relay) | pertumbuhan belanja kelompok upper ... 5,3% pada 2026, ... tahun lalu 3,1%; Kontan 11 May 2026; MSI "hingga 5 Mei 2026" | Note only: "to 5 May" comes from the MSI level sentence, not the 5,3% sentence; the opened article does not define the upper/middle/lower groups (savings-based per DEM-046 context) |
| middle-class-income.csv | P1C2-32 | DEM-048 | VERIFIED-OPENED (relay) | menengah 4,1 persen, bawah 2,1, atas 2,6; Gen Z 4,4, Milenial 3, Gen X 1,4; baseline "dibandingkan periode pra-Ramadhan" (overall 2,9); Antara 15 Apr 2026 | none; seasonal window, not comparable with full-period yoy rows (note already says so) |
| middle-class-income.csv | P1C2-33 | DEM-021 | VERIFIED-OPENED (relay) | MSI kelompok menengah Februari 2026 level 100,4 ... terendah sejak Oktober 2023; CNBC 17 Mar 2026; middle = average savings Rp1-10 juta | none |
| middle-class-income.csv | P1C2-34 | DEM-038 | VERIFIED-OPENED (relay) | "masih akan tertekan di 2026 karena belum ada kebijakan pemerintah ... pro kelas menengah"; Kontan 27 May 2026 11:17 (Riefky, LPEM) | none |

## Summary counts

- VERIFIED-OPENED (original): 8
- VERIFIED-OPENED (relay): 46
- CORRECTED-OPENED: 1
- DERIVED-MOVE: 1
- NOT-FOUND-OPENED: 0
- DATE-FAIL: 0
- BLOCKED: 0
- Total rows: 56 (population-spend 26, middle-class-income 30). Note: P1C1-P06 and S06 are counted under relay and remain labelled DERIVED.
