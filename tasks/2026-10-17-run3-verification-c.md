# Run 3 verification C: price-ladder.csv (89 rows)

Verifier: V3-C (run3-c). Date: 2026-10-17. Scope: every row of `data/processed/price-ladder.csv`; findings file `data/raw/2026-10-17-price-points.md`. No data files, sources.md or commits touched.

## Method
- Opened all 14 sources myself with curl (browser UA), HTTP 200 each, saved under the scratchpad `run3-c/`. HTML converted to text with python3 -I; the CSV `snippet` of every non-Burgreens row (59 rows) was string-matched against the page text: 59/59 verbatim matches. Prices in `price_idr` were compared programmatically with the figures in the snippet: 0 mismatches. The 21 blank `price_idr` cells are all ranges, per-person spend or promo redemption prices (checked row by row).
- Burgreens PDF (32 pages, no text layer: pdftotext returns 43 bytes) rendered with pdftoppm and read visually. I checked all 24 prices (the brief asked for 10), pages 6, 8, 9, 12, 16, 22, 23, 24 plus the p.12 and p.25 footer "Prices exclude Government Tax & Service Charge". All 24 match the CSV (bare numbers x 1,000). The thousand-IDR unit remains an inference (unchanged flag).
- Bylines: date taken from the article byline block directly under the headline; sidebar dates (04 Sep 2026, 02 Nov 2023, 27 Apr 2024, 14 Nov 2025 on other IDN articles, 17/18 Okt 2026 horoscope links, etc.) ignored. Earliest byline date used: 22 Jan 2025. All dates are on or after 2024-10-16. Burgreens prints no date (PDF metadata creation 2025-08-19 only): not a DATE-FAIL by the CSV's own period type "current menu", but the date rule cannot be confirmed from print; flagged.
- Tax and service: no media page states a basis (grep for pajak/tax/service/++/PB1 on all 13 pages). The CSV says "not stated" for them, which is correct. Burgreens "excl. tax and service" is confirmed on p.12 and p.25. Liputan6 Pizza Hut ranges (e.g. 70,909 = 78,000 / 1.1) look like pre-PB1 amounts; the page says "sebelum pajak" only for the promo note. The CSV's "not stated (possibly before 10% tax, inference)" is acceptable.

## Findings (corrections and flags)
1. **P3PB-45 (Point Coffee, 25,000): CORRECTED-OPENED.** The article (MomsMoney 30 Mar 2026) gives one "harga normalnya Rp 25.000" for the Monday promo drinks and then lists Palm Sugar Latte Iced (promo 20,000), Signature Chocolate Iced (20,000), Cookies & Cream Frappe (18,000). The page does not say that 25,000 is the normal price of the Palm Sugar Latte; the assignment is the collector's reading (the row notes say so). It is a promo-article derived price and should not be a numeric item price. Fix: blank `price_idr`, move the 25,000 to notes, as for the other promo rows. Effect on DERIVED: coffee n 24 -> 23 (median stays 29,000, min 10,000, max 38,000, 6 brands); latte sub-cell n 8 -> 7, brands 3 -> 2 (Fore Coffee, Pizza Marzano), median stays 29,000, so latte becomes "n>=4 but brands<4" as before and Point Coffee drops out; coffee brand count 7 -> 6.
2. **Register mismatch for CMP-061:** sources.md describes it as "Fore Coffee normal price as an aside" but P3PB-45 is Point Coffee (the Fore item in that article is a 19,000 Americano promo, not stored). Fix the register text.
3. **Mixing of approximate / non-list prices in item statistics (not blank, so counted).** Rows whose page says "sekitar", "-an" or "ribuan" are counted as exact: P3PR-025 to 030, P3PB-23 to 25 (rounded "ribuan"), P3PB-30 to 33, P3PB-34 to 37 (Google Maps and one ordering-app price, may carry a platform markup). They are labelled in `price_basis`, which is right, but the DERIVED table gives no flag for them: coffee "ok" and "signature milk-coffee ok" rest partly on four Google Maps/app single rows (Tuku, Tomoro, Kopi Kenangan, Fore Cipete). Recommend a flag "approx" on those cells.
4. **Sub-cell label error:** "coffee, signature milk-coffee (aren etc.)" (n=10) includes P3PR-027 to 030 (Fore Manuka/Peach/Berry Americanos, espresso plus water or fruit, no milk). The label is wrong or the class `signature_coffee` is too broad. Values and counts are correct.
5. **Brand cap:** Burgreens 24 of 68 numeric rows (35%), Pizza Marzano 18 (26%), Fore Coffee 14 (21%). Raw file already says the 15% cap cannot be met; per-cell dominance is not shown (functional_drink and rice bowls are Burgreens only: n brands=1, flagged).
6. **Per-person, range, promo rows are NOT mixed into item statistics.** Confirmed: the 21 blank rows (P3PB-19 to 22 ranges, 26 to 28, 46 to 49 promo, 50 to 59 per-person/venue ranges) have no `price_idr` and are excluded from every cell.
7. Minor: P3PB-27 Bastian range 155,000 to 380,000 covers salad, pasta and steak; Gior and Bastian locations check out (Gior address Melawai, Kebayoran Baru; Bastian East Mall, Grand Indonesia). `verification` column is empty on all 89 rows. Pizza Marzano article does not say Jakarta in the item list; the CSV already says "outlets not stated".
8. Conflicts recorded in the raw file (SaladStop three ranges; Pasta Con Bistecca 105,000 vs 102,000) are accurate against the opened pages (102,000 confirmed; the 105,000 June article is not in scope here).

## DERIVED statistics re-computation (from the CSV, python3 -I)
89 rows, 68 numeric `price_idr`, 21 blank: matches the raw file. All 18 cells (4 category + 14 sub-class) reproduce exactly: n, brand count, brand lists, min, median, max, and the n<4 / brands<4 flags. Mismatches: none arithmetic. Only the issue in finding 1 (Point Coffee) changes cells (coffee n 23; latte n 7, 2 brands), plus the label/flag remarks in findings 3 and 4.

Flag check: n<4 flagged correctly for pepper lunch (3), plant-based pasta (1), cappuccino (1), smoothie bowls (3), protein shakes (3), smoothies (3), herbal elixirs (3). Brand counts per category: pasta 8, coffee 7 (6 after fix), bowl 2, functional_drink 1; all "brands<4" flags are right (bowl, functional_drink, and sub-cells). "ok" on pasta (all mixed) is formally n>=4 and brands>=4, but the cell mixes street kiosk (20,000), teppan, plant-based and Italian restaurant prices; the raw file labels it "all types mixed", so the flag is accurate but the median 86,500 is not a market median.

## Row table
Legend: VO-O = VERIFIED-OPENED (original); VO-R = VERIFIED-OPENED (relay); CO = CORRECTED-OPENED. Quote column: Burgreens rows are my own visual transcription of the page (page: printed number); media rows are the snippet that I found verbatim on the page.

| file | row_id | register_id | verdict | quote found | fix |
| --- | --- | --- | --- | --- | --- |
| price-ladder.csv | P3PR-001 | CMP-052 | VO-O | p.6: MIGHTY GREEN BOWL ... 68 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-002 | CMP-052 | VO-O | p.6: MOONLIGHT BERRY BOWL ... 68 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-003 | CMP-052 | VO-O | p.6: TROPICAL BLISS BOWL ... 68 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-004 | CMP-052 | VO-O | p.8: SWEET & SOUR CHICK'N SALAD BOWL ... 65 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-005 | CMP-052 | VO-O | p.9: BEEV SALAD ROLL ... 50 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-006 | CMP-052 | VO-O | p.9: MAX CHICK'N CAESAR SALAD ... 60 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-007 | CMP-052 | VO-O | p.9: BLACKPEPPER SALAD BOWL ... 65 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-008 | CMP-052 | VO-O | p.16: TERIYAKI BOWL ... 50 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-009 | CMP-052 | VO-O | p.16: SWEET AND SOUR CHICK'N BOWL ... 55 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-010 | CMP-052 | VO-O | p.16: NASI GURIH DENDENG BALADO ... 55 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-011 | CMP-052 | VO-O | p.16: RENDANG BOWL ... 59 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-012 | CMP-052 | VO-O | p.16: BLACKPEPPER BOWL ... 59 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-013 | CMP-052 | VO-O | p.22: WONDER GREEN ... 52 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-014 | CMP-052 | VO-O | p.22: BANANA CHOCO CARAMEL ... 52 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-015 | CMP-052 | VO-O | p.22: MOONLIGHT BERRY ... 52 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-016 | CMP-052 | VO-O | p.23: DETOX RED VELVET ... 45 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-017 | CMP-052 | VO-O | p.23: TROPICAL GLOW ... 45 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-018 | CMP-052 | VO-O | p.23: GREEN PUNK ... 47 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-019 | CMP-052 | VO-O | p.23: HAPPY JAMU ... 35 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-020 | CMP-052 | VO-O | p.23: FLU FIGHTER (HOT/COLD) ... 27 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-021 | CMP-052 | VO-O | p.23: SUPER IMMUNE BOOSTER (HOT/COLD) ... 27 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-022 | CMP-052 | VO-O | p.24: ES KOPI SUSU ABANG MAX ... 32 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-023 | CMP-052 | VO-O | p.24: LONG BLACK (HOT/COLD) ... 25 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-024 | CMP-052 | VO-O | p.12: TRUFFLE MUSHROOM PASTA ... 60 (seen on page image); footer "Prices exclude Government Tax & Service Charge" p.12/p.25 | none; unit thousand IDR is inference; no printed date |
| price-ladder.csv | P3PR-025 | CMP-053 | VO-R | Harganya sekitar Rp22 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PR-026 | CMP-053 | VO-R | Hot americano seharga Rp22 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PR-027 | CMP-053 | VO-R | Dengan harga sekitar Rp29 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PR-028 | CMP-053 | VO-R | hot manuka americano dibanderol Rp29 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PR-029 | CMP-053 | VO-R | Triple peach americano dari Fore dijual sekitar Rp29 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PR-030 | CMP-053 | VO-R | Harganya sekitar Rp31 ribu (byline 14 Nov 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-01 | CMP-054 | VO-R | Spaghetti Bolognese : Rp99.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-02 | CMP-054 | VO-R | Spaghetti Aglio Olio : Rp69.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-03 | CMP-054 | VO-R | Spaghetti Gambaretti: Rp92.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-04 | CMP-054 | VO-R | Spaghetti Pollo e Funghi : Rp95.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-05 | CMP-054 | VO-R | Spaghetti Tartufo : Rp105.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-06 | CMP-054 | VO-R | Penne Beef Formaggio : Rp92.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-07 | CMP-054 | VO-R | Legerra Pollo Arrabiatta : Rp92.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-08 | CMP-054 | VO-R | Fettuccine Carbonara : Rp95.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-09 | CMP-054 | VO-R | Fettuccine Salmon Pesto : Rp109.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-10 | CMP-054 | VO-R | Orecchiette Con Salsiccia e Funghi : Rp109.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-11 | CMP-054 | VO-R | Lasagna Classica : Rp109.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-12 | CMP-054 | VO-R | Espresso : Rp30.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-13 | CMP-054 | VO-R | Cafe Americano : Rp35.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-14 | CMP-054 | VO-R | Cafe Latte ( hot / ice ): Rp38.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-15 | CMP-054 | VO-R | Cappucino ( hot / ice ): Rp38.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-16 | CMP-054 | VO-R | Mixed Salad : Rp60.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-17 | CMP-054 | VO-R | Grand Chicken Caesar : Rp105.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-18 | CMP-054 | VO-R | Quinoa Superfood Salad : Rp105.000. (byline 17 Nov 2025) | none |
| price-ladder.csv | P3PB-19 | CMP-055 | VO-R | Salmon Aglio Olio / Mentaiko: Rp70.909 – Rp72.727 (byline 16 Mei 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-20 | CMP-055 | VO-R | Classic Fettuccine / Truffle / Arabbiata: Rp65.455 – Rp68.182 (byline 16 Mei 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-21 | CMP-055 | VO-R | Beef Lasagna: Rp60.000 – Rp62.727 (byline 16 Mei 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-22 | CMP-055 | VO-R | Soup & Salad: Rp50.909 – Rp53.636 (byline 16 Mei 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-23 | CMP-056 | VO-R | Beef Aglio Olio Rp74 ribuan (byline 16 Jul 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-24 | CMP-056 | VO-R | Salmon & Chicken Carbonara Rp79 ribuan (byline 16 Jul 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-25 | CMP-056 | VO-R | Salmon Cream Pasta Rp81 ribuan (byline 16 Jul 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-26 | CMP-057 | VO-R | Harga hidangan utama berkisar Rp 100.000-Rp 250.000 (byline 28 Okt 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-27 | CMP-057 | VO-R | kisaran harga Rp 155.000-Rp 380.000 (byline 28 Okt 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-28 | CMP-057 | VO-R | Harga rata-rata mulai dari kisaran Rp 200.000 ke atas per orang (byline 28 Okt 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-29 | CMP-058 | VO-R | Untuk harga seporsinya dibanderol Rp 20.000. (byline 22 Jan 2025) | none |
| price-ladder.csv | P3PB-30 | CMP-058 | VO-R | Harganya sekitar Rp 20.000-an. (byline 22 Jan 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-31 | CMP-058 | VO-R | Untuk harganya mulai dari Rp 25.000-an (byline 22 Jan 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-32 | CMP-058 | VO-R | Chicken Crispy Pasta Marinara yang dibanderol harga sekitar Rp 29.000-an (byline 22 Jan 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-33 | CMP-058 | VO-R | aglio olio dan cheesy pasta yang harga Rp 25.000-an (byline 22 Jan 2025) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-34 | CMP-059 | VO-R | varian reguler dibanderol sekitar Rp10 ribu, sementara ukuran besar sekitar Rp20 ribu (byline 20 Apr 2025 (Diperbarui)) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-35 | CMP-059 | VO-R | Google Maps mencatat harga reguler sekitar Rp18 ribu dan large Rp22 ribu (byline 20 Apr 2025 (Diperbarui)) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-36 | CMP-059 | VO-R | sekitar Rp27 ribu untuk reguler dan Rp34 ribu untuk ukuran besar (byline 20 Apr 2025 (Diperbarui)) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-37 | CMP-059 | VO-R | harga yang tercantum di aplikasi pemesanan online untuk cabang Cipete sekitar Rp23 ribu (byline 20 Apr 2025 (Diperbarui)) | none; approximate source figure (flag approx in DERIVED) |
| price-ladder.csv | P3PB-38 | CMP-060 | VO-R | Hanya Rp24.000, kamu sudah bisa menikmati (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-39 | CMP-060 | VO-R | cobain Iced Buttercream Latte dengan harga Rp31.000 (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-40 | CMP-060 | VO-R | Dengan harga Rp33.000, kamu sudah bisa menikmati (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-41 | CMP-060 | VO-R | dibanderol dengan harga Rp29.000 (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-42 | CMP-060 | VO-R | Cuma Rp29.000, menu spesial dari Fore (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-43 | CMP-060 | VO-R | Dibanderol Rp29.000, Hot Aren Latte (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-44 | CMP-060 | VO-R | Hanya dengan Rp29.000, kamu sudah mendapatkan Iced Aren Latte (byline 19 Nov 2025) | none |
| price-ladder.csv | P3PB-45 | CMP-061 | CO | Anda bisa menikmati minuman favorit dengan harga Rp 20.000 saja, dari harga normalnya Rp 25.000 [...] Palm Sugar Latte Iced (Rp 20.000) (byline 30 Mar 2026) | blank price_idr, move 25,000 to notes (not stated for this item); fix register CMP-061 text (Point Coffee, not Fore) |
| price-ladder.csv | P3PB-46 | CMP-062 | VO-R | Pasta Con Bistecca (Rp 102.000) (byline 06 Aug 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-47 | CMP-062 | VO-R | Spicy Arrabbiata (Rp 71.000) (byline 06 Aug 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-48 | CMP-062 | VO-R | Caesar Salad - Salmon (Rp 90.000) (byline 06 Aug 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-49 | CMP-062 | VO-R | Caesar Salad - Chicken (Rp 74.000) (byline 06 Aug 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-50 | CMP-063 | VO-R | 1. Bluezone [...] Harga: mulai dari Rp100 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-51 | CMP-063 | VO-R | 2. Hijoo [...] Harga: mulai dari Rp50 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-52 | CMP-063 | VO-R | 3. Kalegreen Salad Bar [...] Harga: mulai dari Rp50 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-53 | CMP-063 | VO-R | 6. Salad Hut [...] Harga: mulai dari Rp50.000 - Rp75.000 per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-54 | CMP-063 | VO-R | 7. SaladStop! [...] Harga: mulai dari Rp100 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-55 | CMP-063 | VO-R | 8. Salam Salads by Felam [...] Harga: mulai dari Rp70 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-56 | CMP-063 | VO-R | 9. Serasa Salad Bar [...] Harga: mulai dari Rp50 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-57 | CMP-063 | VO-R | 10. The Roots Salad [...] Harga: mulai dari Rp40 ribu per orang. (byline 24 Apr 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-58 | CMP-064 | VO-R | 2. SaladStop! [...] Harga: Rp25 ribu-Rp125 ribu. (byline 02 Feb 2025) | none (blank price_idr correct: range/per-person/promo) |
| price-ladder.csv | P3PB-59 | CMP-065 | VO-R | Dengan kisaran harga Rp 100.000–200.000 per orang (byline 01 Okt 2025) | none (blank price_idr correct: range/per-person/promo) |

## Summary counts
- VERIFIED-OPENED (original): 24 (Burgreens, all 24 prices re-read from the page images)
- VERIFIED-OPENED (relay): 64
- CORRECTED-OPENED: 1 (P3PB-45)
- NOT-FOUND-OPENED: 0
- DATE-FAIL: 0 (Burgreens has no printed date; metadata 2025-08-19)
- DERIVED-MOVE: 1 (P3PB-45: 25,000 from numeric price to notes; same row as the CORRECTED count)
- BLOCKED: 0
- Tier-4-only claims: none. Lesson rule (f), derived values in notes: only P3PB-45 violates it.
