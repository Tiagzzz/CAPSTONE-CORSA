# Pre-verification batch 4f (P2-53 to P2-65)

Verifier: claude-sonnet-V1d. Date: 2026-10-19. Sources and fetch status: World Bank API (GOV_WGI_PV.SC, lastupdated 2026-09-25) HTTP 200; transparency.org/en/cpi/2025 HTTP 200; transparency.org/en/countries/indonesia HTTP 200; bpjph.halal.go.id article HTTP 200; imf.org PR 26/010 HTTP 403 (UNREACHABLE); reuters.com HTTP 401 (UNREACHABLE). checked_by=claude-sonnet-V1d, checked_on=2026-10-19.

| item_id | verdict | evidence_quote | corrected_value | page/anchor checked | note |
|---|---|---|---|---|---|
| P2-53 | CONFIRMED | date 2025, value 52.6601047 (GOV_WGI_PV.SC) | | API JSON record 2025 | 52.66 matches after rounding. |
| P2-54 | CONFIRMED | 2024: 54.8866958; 2023: 55.399219; 2022: 52.2810427; 2021: 54.426469; 2020: 56.1226411 | | API JSON records 2020-2024 | All five match after rounding to 2 dp. |
| P2-55 | CONFIRMED | 2022: 52.2810427; 2025: 52.6601047 (all other 2012-2025 values 54.89 or higher) | | API JSON records 2012-2025 | 14 annual values; 2025 is second-lowest, only 2022 lower. Computed from returned data. |
| P2-56 | CONFIRMED | Indonesia has a score of 34 this year, with a change of -3 since last year, meaning it ranks 109 out of 182 countries. | | Country page, CPI section | Page says "this year" without stating the year; CPI 2025 edition inferred from the press list (10.02.2026 CPI 2025 releases) and "Score changes 2012 - 2025". |
| P2-57 | CONFIRMED | The global average has fallen to a new low of 42, while more than two-thirds of countries score below 50. | | cpi/2025 intro | Also: "ranks 182 countries"; "scale of 0 (highly corrupt) to 100 (very clean)". Edition 2025 confirmed (page title and releases). |
| P2-58 | CONFIRMED | Corruption Perceptions Index 2025: Stalling anti-corruption progress in Asia Pacific while public anger surges. Press • 10.02.2026 | | cpi/2025 press list | Headline and date match. Indonesia score not seen in the text extract of the cpi/2025 page (no grep hit for Indonesia checked beyond intro); consistent with the claim. |
| P2-59 | CONFIRMED | kebijakan Wajib Halal Oktober 2026 yang akan mulai berlaku pada 18 Oktober 2026 ... Undang-Undang Nomor 33 Tahun 2014 ... Peraturan Pemerintah Nomor 42 Tahun 2024 | | Opening paragraph | "Second phase" backed by "Cakupan penahapan kedua ini sangat luas". |
| P2-60 | CONFIRMED | kelanjutan dari penahapan kewajiban sertifikasi halal bagi produk usaha menengah dan besar yang dimulai pada Oktober 2024 | | Paragraph "Lebih lanjut, Babe Haikal" | Also: "diperluas cakupan jenis produknya bagi produk usaha mikro, kecil, dan juga produk luar negeri atau impor." |
| P2-61 | CONFIRMED | (1) Produk makanan dan minuman; (2) Hasil sembelihan dan jasa penyembelihan; ... (6) Bahan baku, bahan tambahan pangan, serta bahan penolong untuk produk makanan dan minuman | | Category list (1)-(7) | Others (3) cosmetics, (4) chemical/GMO, (5) natural medicines/supplements, (7) consumer goods also match. Authority is the article's citation of PP 42/2024. |
| P2-62 | CONFIRMED | sanksi administratif ... mulai dari peringatan tertulis, denda administratif, pencabutan sertifikat halal, hingga penarikan produk dari peredaran | | Sanctions paragraph | Matches. |
| P2-63 | CONFIRMED | Sosialisasi Nasional Wajib Halal Oktober 2026 serentak di 1.183 titik lokasi pada 4 Juni 2026 | | Second paragraph, page header | Head of BPJPH Ahmad Haikal Hasan, Mall Pakuwon Bekasi, Kamis (4/6/2026) all match; header shows "5 bulan yang lalu"; no restaurant/food-service treatment in text. |
| P2-64 | UNREACHABLE | | | imf.org PR 26/010 URL | HTTP 403 on one try; not retried. Placeholder statement unverified; no new candidates possible. |
| P2-65 | UNREACHABLE | | | reuters.com URL | HTTP 401 on one try; not retried. Placeholder (and slug-derived title/date) unverified; no new candidates possible. |

## New candidates (unverified, for a second verifier)

None: both placeholder sources (REG-138, REG-143) were blocked.
