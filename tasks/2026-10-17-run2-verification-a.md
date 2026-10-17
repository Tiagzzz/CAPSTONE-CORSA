# Run 2 verification A (V2-A), 2026-10-17

Scope: all 13 rows of `data/processed/plan4-venue-run2.csv` and all 23 rows of `data/processed/plan4-social-proof-run2.csv`. Every source was opened with curl (pages for all; full-text PDFs for BEH-077, BEH-078, BEH-079, BEH-080). All printed publication dates are on or after 2024-10-16. No tier-4 sources. No derived values stored as rows. No data files or sources.md edited.

## Systemic findings
1. Geography: P4W2b-07, -08, -09 are beauty-category (YouGov, ID/TH/SG) rows coded N; must be P. Cross-market rows P4W2b-05, -06, -11, -12 are already P. P4W2b-13 is an Indonesia cut inside the six-market survey and is left N (owner may prefer P). Non-food, Indonesia-wide rows (P4W2b-10, -14, -15, -16, -18) are also proxy categories under a strict reading; they are flagged, not changed.
2. P4W2b-14 notes claim a base conflict (1,714 vs 2,125). Both the article and the linked report page (`/live-shopping-affiliate-links-demographic-insights/`) say 1714; 2,125 is not on either page. Remove the claim from the row, findings-run2.md and BEH-074.
3. P4W2b-21: the full text states random sampling with inclusion criteria (127 accessed the survey, 85 met the criteria). The row says "no sampling frame stated". Fix.
4. Peer-reviewed papers checked for n, sampling method and printed publication date: BEH-067, -068, -077, -078, -079, -080. All matched except the point in item 3.

## Table

| file | row_id | register_id | verdict | quote found | fix |
| --- | --- | --- | --- | --- | --- |
| venue | P4W7b-01 | BEH-030 | VERIFIED-OPENED (original) | "another 34% drank coffee to help focus while working or studying"; 1,002 respondents; printed 4 July 2025 | none (page prints no fieldwork dates; "mid-2025" is the worker's wording) |
| venue | P4W7b-02 | BEH-040 | VERIFIED-OPENED (original) | "price (60%) and taste (59%)"; 995 young respondents, 2-7 Sep 2025, eight Java cities; 13 Oct 2025 | none |
| venue | P4W7b-03 | BEH-040 | VERIFIED-OPENED (original) | "service (44%), cleanliness (44%), and portion size (43%) ... especially among middle- and upper-class respondents" | none |
| venue | P4W7b-04 | BEH-040 | VERIFIED-OPENED (original) | "4 out of 5 respondents ... cleanliness and the availability of toilets" | none |
| venue | P4W7b-05 | BEH-040 | VERIFIED-OPENED (original) | "Students ... seating (75%) and power outlets (53%) ... workers ... parking (50%)" | none |
| venue | P4W7b-06 | BEH-040 | VERIFIED-OPENED (original) | "lunch (37%) and dinner (41%)" | none |
| venue | P4W7b-07 | BEH-065 | CORRECTED-OPENED | "23% ... colokan listrik, disusul wifi (21%), dan AC (17%)"; n 1.000, majority 18-24, Java; printed 3 Nov 2024; "dirilis pada Oktober 2024" | Notes say a photo/Instagrammable item is "not in this list". The page also names "spot foto menarik" (photo spots) as another supporting facility, without a percentage. "Single-choice, additive" is the worker's assumption; the page says only "yang paling dibutuhkan" (most needed). The "Kamis (23/10)" quote fits 2025, not 2024: date ambiguity stays, both dates pass |
| venue | P4W7b-08 | BEH-065 | VERIFIED-OPENED (original) | "71% responden lebih memilih buat membeli kopi dibanding seduh sendiri di rumah" | none |
| venue | P4W7b-13 | BEH-066 | VERIFIED-OPENED (relay) | "49,1% ... nongkrong di kafe sebagai bentuk self-reward, diikuti liburan (46,8%) dan belanja pakaian (39,1%)"; Kedai Kopi survey 14-19 Oct 2025, 932 respondents; 4 Nov 2025 | none |
| venue | P4W7b-14 | BEH-066 | VERIFIED-OPENED (relay) | "83% ... menu yang enak ... 78% ... ruangan yang nyaman ... (70%), ... (64%), ... (45%), dan estetika (27%)" | none |
| venue | P4W7b-15 | BEH-067 | VERIFIED-OPENED (original) | "sample consists of 500 Generation Z consumers from five coffee shop brands in Jakarta ... SEM with AMOS ... Servicescape does not significantly affect Customer Satisfaction"; published 2026-02-16, Vol. 19 No. 1; licence CC BY-NC-SA 4.0 | Sampling method is not in the abstract (full text not read). Licence is CC BY-NC-SA 4.0, not "CC BY". Geography J correct |
| venue | P4W7b-17 | BEH-068 | VERIFIED-OPENED (original) | "purposive sampling ... Generation Z individuals residing in Sumbawa who have made repeat purchases at Tomoro Coffee ... multiple linear regression ... comfort and location accessibility over mere menu aesthetics"; published 2025-12-29 | n is not in the abstract and the full text was not retrieved (no download link on the page); n stays unverified. Geography P correct |
| venue | P4W7b-18 | BEH-069 | VERIFIED-OPENED (relay) | "Ada survei yang menunjukkan bahwa [lebih dari] 80 persen konsumen ... membeli produk berdasarkan ada atau tidaknya label halal. Jadi, kesadaran itu sudah tinggi, 83 persen loh"; Populix 2023 report; 21 Jun 2025; headline "Sadar" | none (headline and body conflict stored correctly) |
| social | P4W2b-01 | BEH-070 | VERIFIED-OPENED (relay) | "Setelah hiburan, kuliner (59%) dan traveling (54%)"; entertainment 62%; Jakpat May-Jun 2025, 1.941 respondents; 7 Aug 2025 | none |
| social | P4W2b-02 | BEH-071 | VERIFIED-OPENED (relay) | "769 responden yang biasa makan di luar dari delapan kota di Pulau Jawa pada 2-7 September 2025 ... ulasan/peringkat bagus (42%)"; 24 Nov 2025 | The article does not list the cities; "Jakarta not included" rests on BEH-040. Say so in the notes |
| social | P4W2b-03 | BEH-071 | VERIFIED-OPENED (relay) | "media sosial/iklan (44%)" | same note as -02 |
| social | P4W2b-04 | BEH-071 | VERIFIED-OPENED (relay) | "sekitar 73% publik Indonesia memilih untuk mencoba makan di tempat baru" | same note as -02 |
| social | P4W2b-05 | BEH-005 | VERIFIED-OPENED (relay) | "31% of consumers influenced by product links shared by creators and 30% by platform-led promotions"; over 2,400 respondents in six SEA markets; 30 July 2025 | none; P correct. Note the "83%" in this article is SEA-wide affiliate purchases, a different item from the Jakpat 83% |
| social | P4W2b-06 | BEH-005 | VERIFIED-OPENED (relay) | "micro and nano influencers ... are weathering the drop in trust better ... narrowed the gap between influencer tiers"; 59% mega, 7% drop | none; P correct |
| social | P4W2b-07 | BEH-072 | CORRECTED-OPENED | "Among Indonesian respondents, 54% said they trust peer reviews more than influencer content"; YouGov, over 6,000 consumers in three countries; makeup; 23 Apr 2025 | geography N to P (beauty proxy category, cross-market base) |
| social | P4W2b-08 | BEH-072 | CORRECTED-OPENED | "high-income consumers in Indonesia, 62% ... just 33% among lower-income groups" | geography N to P (beauty proxy) |
| social | P4W2b-09 | BEH-072 | CORRECTED-OPENED | "27% of Indonesian millennials favour live formats, only 18% of Gen Z" | geography N to P (beauty proxy) |
| social | P4W2b-10 | BEH-073 | VERIFIED-OPENED (relay) | "Riset terbaru YouGov mengungkap pola unik: Generasi Z lebih dipengaruhi influencer, Milenial banyak mengandalkan ulasan produk, sementara Gen X ... keluarga atau teman"; 22 Sep 2025 | none. Flag: marketing blog, no numbers, no base; the study may be global (the page says Indonesia ranks second in the world for online shopping). The N code is weakly supported; the row is a lead only |
| social | P4W2b-11 | BEH-006 | VERIFIED-OPENED (relay) | "skor 2,42 dari 4 ... ulasan daring (2,36) dan kreator (1,98)"; 2.400 konsumen, six markets; 27 Juli 2026 | none; P correct |
| social | P4W2b-12 | BEH-006 | VERIFIED-OPENED (relay) | "dua dari tiga konsumen (67%) ... pernah membeli produk secara khusus karena direkomendasikan oleh seorang kreator" | none; P correct |
| social | P4W2b-13 | BEH-006 | VERIFIED-OPENED (relay) | "Vietnam (34%) dan Indonesia (31%) memimpin kawasan dalam penggunaan AI generatif untuk penemuan produk" | none; N kept (Indonesia-specific cut), flagged for owner |
| social | P4W2b-14 | BEH-074 | CORRECTED-OPENED | "83% of consumers who have opened them ... less than 40% ... within the last half-year"; "responses from 1714 participants across Indonesia"; 13 Jul 2026 | Remove "base conflict 1,714 vs 2,125" from base_n, notes and findings. 2,125 is on neither the article nor the report page |
| social | P4W2b-15 | BEH-074 | VERIFIED-OPENED (original) | "routinely watching these sessions (92%) ... Millennials (59%) and Gen X (58%) prefer watching these sessions more than Gen Z (51%)"; 71/66/65%; TikTok Live 56% | none (value and label match) |
| social | P4W2b-16 | BEH-075 | VERIFIED-OPENED (original) | "80% in the second half of 2024 ... 85% in the first half of 2025 ... 74% ... 79% ... 46% ... to 44%"; 6 Jan 2026 | none |
| social | P4W2b-17 | BEH-030 | VERIFIED-OPENED (original) | "majority of people trust recommendations from the closest people (57%), followed by TV commercials (38%)"; 1,002 respondents; 4 Jul 2025 (page modified 10 Oct 2025) | none |
| social | P4W2b-18 | BEH-076 | VERIFIED-OPENED (relay) | "transaction volumes surged 90% year on year to 2.6 billion, alongside a 75% jump in active sellers and online shops, reaching 800,000"; 17 Nov 2025 | none |
| social | P4W2b-19 | BEH-077 | VERIFIED-OPENED (original) | Abstract: 400 respondents, SEM-PLS. Full text: "non-probability sampling dengan kriteria purposive sampling ... berumur sekurang-kurangnya 17 tahun"; 21-25 = 178 (44,5%), 26-30 = 28,5%; published 2026-01-30 | none (the n, sampling method and date all match) |
| social | P4W2b-20 | BEH-078 | VERIFIED-OPENED (original) | "A sample of 100 respondents was determined through purposive sampling ... 57.4%"; the full text agrees; Published 2026-04-26 | none |
| social | P4W2b-21 | BEH-079 | CORRECTED-OPENED | Abstract: "survey online terhadap 85 responden dengan dua pertanyaan terbuka"; full text: "Teknik pengambilan sampel ... random sampling dengan kriteria inklusi"; "Dari total 127 orang yang mengakses survei, sebanyak 85 responden memenuhi kriteria inklusi"; published 16-06-2025 | Replace "no sampling frame stated" with "random sampling with inclusion criteria (127 accessed, 85 included), per full text". Order of the abstract's other findings unchanged |
| social | P4W2b-22 | BEH-080 | VERIFIED-OPENED (original) | "total sample studied of 140 samples ... non probability sampling ... purposive sampling"; "Published: 05-06-2025", Vol. 8 No. 2 | none |
| social | P4W2b-23 | BEH-081 | VERIFIED-OPENED (relay) | "Jika Anda terus melihat orang mengantre berulang kali, katanya, pengulangan tersebut dapat membuat perilaku mengantre terasa normal"; Herz (Brown) and Jansson-Boyd (Anglia Ruskin) quoted; photo caption Blok M; page printed 8 Dec 2025 per URL stamp and register | none |

## Counts
Total rows: 36 (venue 13, social-proof 23).
- VERIFIED-OPENED (original): 15 (venue 9, social 6)
- VERIFIED-OPENED (relay): 15 (venue 3, social 12)
- CORRECTED-OPENED: 6 (venue 1: P4W7b-07; social 5: P4W2b-07, -08, -09, -14, -21)
- NOT-FOUND-OPENED, DATE-FAIL, DERIVED-MOVE, BLOCKED: 0

Open caveat: P4W7b-17 n is unverified (abstract only).
