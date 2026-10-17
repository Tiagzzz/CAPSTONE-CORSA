# Plan 4 Q7 (third place, venue attributes, halal) - worker P4-W7b findings, run 2

Access date for all sources: 2026-10-17. Opened with curl (browser user agent), text extracted with a local script and python3 -I. Output rows: `data/processed/plan4-venue-run2.csv` (18 rows, IDs P4W7b-01 to P4W7b-18). Rows already in `plan4-venue.csv` or in other plan-4 files (price 60%, new-place rows, local-culinary 77%) were not repeated.

## Source blocks

### P4-W7b-S1
- Title: Healthy living and coffee trends in 2025
- Publisher: Jakpat (Jakpat Insight)
- URL opened: https://insight.jakpat.net/healthy-living-and-coffee-trends-in-2025/
- Printed publication date: 2025-07-04 (page markup; as resolved in run 1b)
- Proposed tier: 3 (survey vendor, online panel; method note on the page only gives n)
- Access status: opened
- Quote: "another 34% drank coffee to help focus while working or studying" (n = 1,002). Existing source (P4-W7-S1); only a new row added.

### P4-W7b-S2
- Title: Strong Traditional Tastes in the Local F&B Market
- Publisher: Jakpat (Jakpat Insight)
- URL opened: https://insight.jakpat.net/strong-traditional-tastes-in-the-local-fb-market/
- Printed publication date: 2025-10-13 (page markup datePublished); fieldwork 2-7 Sep 2025, n = 995, eight Java cities, no Jakarta
- Proposed tier: 3 (survey vendor)
- Access status: opened
- Quotes: "Consumers generally choose where to eat based on price (60%) and taste (59%). Other factors such as service (44%), cleanliness (44%), and portion size (43%) also influence decisions"; "Students tend to prioritize comfortable seating (75%) and power outlets (53%), while workers focus more on practical amenities such as parking (50%)."; "Most people eat out around lunch (37%) and dinner (41%)."

### P4-W7b-S3
- Title: Fasilitas yang Paling Dibutuhkan di Kedai Kopi untuk Gen Z
- Publisher: GoodStats (reporting its own survey "Pola Konsumsi Kopi Orang Indonesia", October 2024, n = 1,000, majority 18-24, mostly Java)
- URL opened: https://goodstats.id/article/fasilitas-yang-paling-dibutuhkan-di-kedai-kopi-untuk-gen-z-26CoT
- Printed publication date: 2024-11-03 (page markup); the body quotes the managing editor on "Kamis (23/10)", so the page may have been updated on 23 Oct 2025. Both are after 2024-10-16.
- Proposed tier: 3 (data-journalism outlet running its own survey; sampling method not described)
- Access status: opened
- Quotes: "Sebanyak 23% responden menganggap bahwa fasilitas yang paling dibutuhkan adalah colokan listrik, disusul wifi (21%), dan AC (17%)."; "71% responden lebih memilih buat membeli kopi dibanding seduh sendiri di rumah"

### P4-W7b-S4
- Title: Daya Tarik Kedai Kopi di Mata Anak Muda 2024
- Publisher: GoodStats, republishing a student project (GNFI MSIB internship programme), Google Form survey 26 Oct-11 Nov 2024, n = 203, 91% aged 18-24
- URL opened: https://goodstats.id/article/daya-tarik-kedai-kopi-di-mata-anak-muda-2024-kebiasaan-pengeluaran-dan-alasan-mereka-ZTfhp
- Printed publication date: 2024-11-23 (page markup)
- Proposed tier: 4 (convenience sample, coursework survey). Rows are labelled TIER-4-LEAD and must not carry a figure alone. They are the only free source with spend per visit and dwell time.
- Access status: opened
- Quotes: see rows 9 to 12 (comfortable place 84%, taste 75%, price 73%, WiFi 45%; spend IDR 20,000-50,000 for 1-2 hours; 23.1% stay longer).

### P4-W7b-S5
- Title: Hampir 50% Publik RI Pilih Nongkrong di Kafe Sebagai Self-Reward
- Publisher: GoodStats, reporting a survey by Kedai Kopi (kedaikopi.co), "Survei Pergeseran Perilaku Konsumsi dan Daya Beli Masyarakat Kelas Menengah", 14-19 Oct 2025, n = 932. The Kedai Kopi report page (https://kedaikopi.co/flipbook/survei-perilaku-konsumsi-daya-beli-masyarakat-kelas-menengah/) was opened (markup date 2025-10-28) but only a flipbook shell; no figures extracted from it.
- URL opened: https://goodstats.id/article/hampir-50-publik-ri-pilih-nongkrong-di-kafe-sebagai-self-reward-2HFQJ
- Printed publication date: 2025-11-04 (page markup)
- Proposed tier: 3 (media-outlet survey; sampling and city split not stated)
- Access status: opened
- Quotes: "Sebanyak 49,1% responden mengaku menyukai kegiatan nongkrong di kafe sebagai bentuk self-reward"; revisit reasons 83 / 78 / 70 / 64 / 45 / 27 (see row 14).

### P4-W7b-S6
- Title: Antecedents of Revisit Intention of Generation Z at Coffee Shops in Indonesia
- Publisher: Jurnal Riset Bisnis dan Manajemen (Universitas Pasundan), Vol. 19 No. 1, February 2026, DOI 10.23969/jrbm.v19i1.38365, CC BY
- URL opened: https://journal.unpas.ac.id/index.php/jrbm/article/view/38365
- Printed publication date: page metadata 2026/02/16; issue "February Edition" 2026
- Proposed tier: 2 (peer-reviewed open-access journal; indexing level not checked)
- Access status: opened (abstract page; full text not read)
- Quote: "The sample consists of 500 Generation Z consumers from five coffee shop brands in Jakarta." and "Servicescape does not significantly affect Customer Satisfaction among Generation Z consumers."

### P4-W7b-S7
- Title: Pengaruh Halal Awareness, Product Quality dan Store Atmosphere terhadap Keputusan Pembelian Kopi di Coffee Shop (Studi Kasus pada Gen Z di DKI Jakarta)
- Publisher: Politeknik Negeri Jakarta repository (D4 thesis, Syifa Aulia Azzahra)
- URL opened: https://repository.pnj.ac.id/30994/
- Printed publication date: 2025-08-04 (eprints.date, submitted); deposited 2025-08-05
- Proposed tier: 4 (undergraduate thesis; abstract open, full text restricted)
- Access status: opened (abstract); the SNAM 2025 conference version at prosiding.pnj.ac.id returned HTTP 403 (Cloudflare challenge, not bypassed)
- Quote: "survei kepada 140 responden yang dipilih melalui teknik purposive sampling" and "ketiga variabel independen Halal Awareness, Product Quality, dan Store Atmosphere memiliki pengaruh positif dan signifikan terhadap keputusan pembelian"

### P4-W7b-S8
- Title: How Lifestyle, Cafe Atmosphere Shape, and Customer Experience and Revisit Intention among Gen Z: Evidence from Tomoro Coffee Sumbawa
- Publisher: Prosiding dan Call Paper Widya Wiwaha (STIE Widya Wiwaha), DOI 10.32477/semnas.v4i1.1323
- URL opened: https://jurnal.stieww.ac.id/index.php/semnas/article/view/1323
- Printed publication date: page metadata 2025/12/29
- Proposed tier: 3 (conference proceedings; proxy city, not Jakarta)
- Access status: opened (abstract)
- Quote: "customer preferences prioritize comfort and location accessibility over mere menu aesthetics"

### P4-W7b-S9
- Title: BPJPH Ungkap 83 Persen Konsumen RI Sadar Produk Halal
- Publisher: CNN Indonesia (relay of a BPJPH official's statement, who cites a Populix report from 2023)
- URL opened: https://www.cnnindonesia.com/ekonomi/20250621151902-92-1242248/bpjph-ungkap-83-persen-konsumen-ri-sadar-produk-halal
- Printed publication date: 2025-06-21 (Sabtu, 21 Jun 2025 15:35 WIB)
- Proposed tier: 3 (major news outlet; official quoting a vendor survey, so not tier 1 data)
- Access status: opened
- Quote: "Jadi, kesadaran itu sudah tinggi, 83 persen loh" (headline: 83% "sadar"; body: they buy based on the halal label; both stored). Underlying survey 2023, outside the date window.

## Direction of evidence
- H7 (third place): Supported in part. Comfort and a work-friendly setting are widely cited (comfortable place 84% in a student sample; 78% revisit for a comfortable room; WiFi, power outlets, AC top facility needs in the GoodStats n=1,000 sample). Disconfirming: price and taste lead overall venue choice (60% / 59%); aesthetics rank last as a revisit reason (27%); servicescape not significant for Gen Z satisfaction in the 500-person Jakarta SEM study; only 34% drink coffee to focus on work or study (Jakpat). Power outlets are a student priority; workers' top stated amenity was parking (50%).
- H8 (halal): Only weak, indirect evidence in this run. A tier-4 Jakarta Gen Z thesis (n=140) finds halal awareness significant; BPJPH's 83% cited figure is a 2023 all-category number. No free 2024-2026 figure was found for the share who check halal certification at cafes, nor for willingness to visit a non-certified venue.

## Gaps
- Share who check halal certification at restaurants and cafes, and willingness to visit without it, by generation: not found in any opened free source dated on or after 2024-10-16. Leads not opened: Populix 2024 (53% would choose food with a "No Pork No Lard" label without certification, via a PNJ SNAM paper that returned 403); Populix 2023 halal report (39% would buy without a halal logo; out of window; page at indonesiabusinesspost.com dated 2023-04-19); IHATEC 2022 (93% say halal label matters at cafes and restaurants; out of window).
- Instagrammable design, ambience by generation, and any Jakarta-only cut: no opened source. Jakpat's "Gen Z, Millennials, Gen X Trend on Coffee 2025 vs 2023" (2025-05-21) and "Indonesia Beverage Consumption" (2026-06-19, n=1,238) were opened but their figures sit in paywalled or image-only previews (IDR 499,000 report), nothing extractable.
- Dwell time and spend per visit beyond the tier-4 student sample.
- Toffin/MAJA coffee reports: no free 2024-2026 report found. Databoks: no relevant halal or café chart found by search. LPPOM MUI and BPJPH: no consumer survey found (only compliance news; BPJPH deadline items not in scope).
- Out-of-window items seen and not used as rows: Jakpat "Become a lifestyle: coffee drinking habits across different generations" (2024-04-22); IPB Madiun millennials vs Zoomers study (January 2024, n=180, judgmental sampling); Trunojoyo work-from-cafe literature review (May 2024).

## Blocked or unreachable hosts
- prosiding.pnj.ac.id (Cloudflare, HTTP 403 on article and download URLs; no bypass tried).
- jurnaluniv45sby.ac.id (HTTP 403).
- journal.univetbantara.ac.id (HTTP 404 on the article link).
- sarimelati.co.id was refused by the proxy (side effect of a Jakpat search page; not needed).
