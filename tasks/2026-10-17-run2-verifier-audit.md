# Run 2 spot-audit of the verifiers (2026-10-17)

Method: for each of 14 sampled rows that the verifier marked VERIFIED-OPENED, the auditor opened the cited source itself (curl with a browser user agent; pdftotext, grep, or a rendered page image for image tables). It checked value, unit, period, base and publication date. Downloads went to the audit scratchpad only. Data files were read, never written.

## Results

| # | Verifier | Row | Source opened | What the auditor found | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | F | E-04 (REG-001) | Permen Investasi dan Hilirisasi/BKPM 5/2025, jdih-storage PDF (original) | Art. 26(2): total investment > Rp10,000,000,000 excl. land and building per 5-digit KBLI per project location. Art. 26(3)(b): F&B is per 2-digit KBLI per 1 location point. Art. 26(4): location point is per kabupaten/kota. Signed 1 Oct 2025. Matches. | AGREE |
| 2 | F | E-05 (REG-002) | Salinan PP 28/2025, jdih-storage PDF (original) | Art. 212(2) and (3)(b): same IDR 10bn rule and the F&B exception "sepanjang terbuka untuk Penanaman Modal Asing", per 2-digit KBLI per 1 location point. Set and promulgated 5 Jun 2025. Matches. | AGREE |
| 3 | F | H-01 (REG-009, REG-010) | PP 42/2024 (Sumut JDIH mirror PDF) and the BPJPH page of 24 Oct 2024 | Art. 155: goods and services must be halal-certified. Phase one covers food and drink products. The BPJPH statement names "restoran, dapur hotel, rumah makan, dan kafe untuk skala usaha menengah dan besar" and business closure. Matches. | AGREE |
| 4 | D | P3BF-009 (CMP-001, FAST going concern) | FAST consolidated FS 30 Jun 2026, kfcku.com PDF (original) | The note prints: "present uncertainties that require consideration in evaluating the Group's ability to continue as a going concern ... conditions are highly challenging ... prepared on a going concern basis ... continued financial support from the Group's shareholders". Outlets: 682 at 30 Jun 2026, 690 at 31 Dec 2025. | AGREE |
| 5 | D | P3BF-015 (CMP-006, MAPB loss) | MAPB FS 1H 2026, mbai.co.id PDF (original) | "RUGI BERSIH PERIODE BERJALAN (121.506) (80.206)", i.e. Jan-Jun 2026 vs Jan-Jun 2025, unit IDR million. Matches. | AGREE |
| 6 | D | P3BF-033 (CMP-014, Fore outlets) | Fore Annual Report 2025, outlet map (original); cross-check Fore 1H26 FS | The map prints "Jabodetabek: 149 Fore Coffee, 2 Fore Donut". 1H26 FS note: 363 coffee stores and 10 donut stores at 30 Jun 2026 vs 316 and 2 at 31 Dec 2025, plus 4 in Singapore (377 in the lease note). Matches. Note: the source region is Jabodetabek, while the row metric is labelled "outlets_jakarta". The geography column should say Jabodetabek. | AGREE (label caveat) |
| 7 | C | P1C1-F05 (DEM-020, Jakarta Selatan spend) | Databoks page, Kota Jakarta Selatan (relay of BPS Susenas) | Rp4,083,229 per capita per month in 2025, +15.57% vs 2024 (Rp3.53m). Food Rp1,427,470 (34.96%). Rank 1 of 6 DKI areas and 1 of 514 districts. "Last updated 20 Agustus 2026". Matches. | AGREE |
| 8 | C | P1C2-20 (DEM-034, BI CCI Jakarta) | BI Survei Konsumen September 2026 PDF, Table 6 (rendered image, original) | Jakarta IKK: Sep 2025 145.5, Aug 2026 150.0, Sep 2026 146.8, change -3.2. Matches. | AGREE |
| 9 | C | P1C2-01 (DEM-035, middle class) | Kontan, 8 Feb 2026 15:43 WIB (relay of Mandiri Institute) | Middle class fell from 47.9m (2024) to 46.7m (2025), "sekitar 1,1 juta"; 16.6% of the national population. Matches. | AGREE |
| 10 | B | P4W9-16 (BEH-086, cooking at home 66%) | IMGR 2025 PDF (original) | Text: "Sixty-six percent of Millennials prioritize cooking at home". Chart: Cook Food at Home 66%. Multiple-response note present. | AGREE |
| 11 | B | P4W9-14 (BEH-086, promotions 60%, Gen Z) | IMGR 2025 PDF (original) | Text: "Sixty percent of Gen Z respondents actively seek out promotions and discounts". Chart: 66, 60, 54, 53, 44, 37, 30. Matches. | AGREE |
| 12 | A | P4W7b-02 (BEH-040, price 60% / taste 59%) | Jakpat Insight article, 13 Oct 2025 (original) | "price (60%) and taste (59%)"; 995 young respondents; fieldwork 2-7 Sep 2025; eight Java cities, no Jakarta. Matches. | AGREE |
| 13 | A | P4W7b-03 (BEH-040, service / cleanliness / portion) | Same Jakpat article | "service (44%), cleanliness (44%), and portion size (43%) ... especially among middle- and upper-class respondents". Matches. | AGREE |
| 14 | E | P3B-05 (CMP-028 / CMP-029, Burger King) | RBA Q3 FY26 deck of 3 Feb 2026 and the Q4 FY23 deck of 17 May 2023 (originals) | Q3 FY26 deck: Burger King store count 147, 143, 139, 136, 138 (Q3'25 to Q3'26). The FY23 deck prints "186 store count as at 31st March 2023 (176 Burger King and 10 Popeyes)". So 176 to 138 holds. It spans Mar 2023 to Dec 2025, and the CSV row itself records only 138 vs 147. | AGREE |

## Agreement rate per verifier

| Verifier | Rows sampled | AGREE | DISAGREE | CANNOT-OPEN | Rate |
| --- | --- | --- | --- | --- | --- |
| A | 2 | 2 | 0 | 0 | 100% |
| B | 2 | 2 | 0 | 0 | 100% |
| C | 3 | 3 | 0 | 0 | 100% |
| D | 3 | 3 | 0 | 0 | 100% |
| E | 1 | 1 | 0 | 0 | 100% |
| F | 3 | 3 | 0 | 0 | 100% |
| Total | 14 | 14 | 0 | 0 | 100% |

## Observations (none changes a verdict)

- P3BF-033 is labelled "outlets_jakarta" but the source gives Jabodetabek (Greater Jakarta). The geography label should match.
- The "176 Burger King" figure sits in the Q4 FY23 deck (CMP-029). The CSV row itself holds only 138 vs 147, and the 176 to 138 comparison appears in the findings file. A consumer of the 176-to-138 claim should cite both decks.
- The sample is small (14 rows, weighted to decision-relevant rows). A 100% agreement rate here does not prove the rest of the rows are correct.
- Caveat on the spot-audit: the auditor did not independently re-check the other rows in the same verifier reports, for example the image-table rows other than Table 6 of the BI report.
