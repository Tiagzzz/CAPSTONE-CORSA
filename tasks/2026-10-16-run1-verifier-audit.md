# Run 1 verifier spot-audit (16 rows)

Auditor: spot-auditor run 1, 2026-10-16. Method: own WebSearch with new wording; WebFetch not used (hosts blocked, per run log). All evidence is search-result level (not opened pages). Read-only; no data files edited.
Verdicts: AGREE-STRONG = different outlet or original publisher confirms value/unit/period/base/date (on/after 2024-10-16). AGREE-WEAK = only the same outlet(s) as worker/verifier, or press text only. DISAGREE = differs / unsupported.

## Table

| verifier | file | row_id | claim | value | audit verdict | evidence (query, URL, publisher, date) |
|---|---|---|---|---|---|---|
| V-D | plan4-spend-drivers.csv | SD09 | Indonesia food delivery GMV 2025 | US$6.4B | AGREE-WEAK | Q: "Indonesia food delivery market 2025 Momentum Works Grab GoTo ShopeeFood market share US$6.4 billion". e27.co/the-subsidy-wars-are-ending-and-only-two-will-survive-20260128/ (2026-01-28), Bisnis 2026-01-28. Same outlets as verifier/worker; Momentum Works 2025 original not found; Databoks (Katadata) page paywalled |
| V-D | plan4-spend-drivers.csv | SD11 | QRIS transactions 2025 | 15.51 bn | AGREE-WEAK (conflict flagged) | Q: "BI transaksi QRIS sepanjang 2025 tumbuh 148 persen nominal Rp1.420 triliun Gubernur Perry" returned no full-year support: 148.5% was Q2 2025 volume growth (Warta Ekonomi, wartaekonomi.co.id/read575029); Rp1,420.66 tn not found. Q: "QRIS full year 2025 total transactions billion..." gave 13.66 bn for 2025 (expatlifeindonesia.com, secondary, may be a cut-off before year end) and no full-year value. Q: "volume transaksi QRIS Januari 2026 ... infobanknews" repeated 15.51 bn / 148.54% as 2025 context (Infobanknews/Kontan, 2026). Only Kontan/Infobank-type press supports 15.51 bn; no BI original. The 148.54% sits very close to the Q2 figure 148.50%. Re-check SD11-SD13 against BI |
| V-D | plan4-spend-drivers.csv | SD14 | QRIS transactions Jan 2026 | 1.83 bn, +131.47% YoY | AGREE-STRONG | Q: "volume transaksi QRIS Januari 2026 tumbuh 131 persen infobanknews pengguna merchant". Warta Ekonomi (wartaekonomi.co.id/read601669, "tumbuh 131"), Infobanknews, Kontan (Rp164.48 tn, +103.35%); users 59.98 m, merchants 43.06 m. Warta Ekonomi is a different outlet, Feb-Mar 2026 |
| V-D | plan4-spend-drivers.csv | SD17 | Bank PayLater outstanding Jun 2026 | IDR 30.71 tn, +33.54% | AGREE-STRONG | Q: "OJK ... outstanding BNPL perbankan Juni 2026 tumbuh 33,54 persen Rp30,71 triliun". CNBC Indonesia (cnbcindonesia.com/market/20260804..., 2026-08-04), Tirto, IDXChannel, Warta Ekonomi, Kontan; 32.80 m accounts, 0.34% of bank credit, OJK's Dian Ediana Rae |
| V-D | plan4-spend-drivers.csv | SD18 | Finance-co PayLater financing Jun 2026 | IDR 13.4 tn, +57% (57.02%) | AGREE-STRONG | Q: "multifinance paylater financing June 2026 Rp13,4 triliun NPF 3,09 persen OJK Agusman". Bisnis.com finansial.bisnis.com/read/20260810/89/1994925 (2026-08-10), Kontan, Infobanknews; NPF 3.09% (May 3.44%) also confirmed (covers SD19) |
| V-D | plan4-spend-drivers.csv | SD21 | Concerned about cost of living, buy less/cheaper | 50% (global 44, APAC 42) | AGREE-STRONG | Q: "PwC Indonesia consumer survey 2025 half of consumers 50% worry cost of living buy less". PwC Indonesia press release (original publisher), 2025-07-08, pwc.com/id/en/media-centre/press-release/2025/english/economic-instability-... |
| V-B | plan4-health.csv | P4W4-01 | WTP over 10% more for enhanced nutrition | 48% | AGREE-STRONG | Q: "NielsenIQ Indonesia health wellness 2025 consumers willing to pay more enhanced nutrition ...". NIQ original release nielseniq.com/global/en/news-center/2025/niq-indonesian-consumers-reassess-health-priorities-..., 2025-07-08: "Nearly half or 48% ... over 10% more"; 19% for 20% (P4W4-02). Base not shown |
| V-B | plan4-health.csv | P4W4-08 | Medical specialist recommendation top influence | 77% | AGREE-STRONG | Same query and NIQ original release (also Indonesian-language version nielseniq.com/global/id/...); 69% and 65% for next items match verifier's note. Upgrades V-B's own "one search only" flag |
| V-B | plan4-novelty.csv | P4W3-04 | Self-identified early adopters | 7% of Indonesians | AGREE-STRONG | Q: "YouGov Indonesia 2024 early adopters 7% trend followers shoppers survey Indonesians shopping personas". YouGov original yougov.com/articles/50874-beyond-the-purchase-..., Marketech APAC 2024-11-19, Campaign Asia. Also 7% trend-driven, 12% impulse, 52% need-based, 51% pulse-chaser regret |
| V-B | plan4-health.csv | P4W4-11 | Buy less / cheaper due to economic instability | 50% | AGREE-STRONG | PwC original press release 2025-07-08 (same search as SD21); fieldwork Jan-Feb 2025 |
| V-A | plan4-media-by-age.csv | P4W1-R01 | Gen Z internet penetration (APJII 2025) | 87.8% | AGREE-WEAK | Q: "APJII survei penetrasi internet Indonesia 2025 per generasi Gen Z 87,8 persen Milenial". Only GoodStats (data.goodstats.id/statistic/penetrasi-internet-indonesia-menurut-generasi-2025-...) carries the by-generation split; Selular.id, Bisnis 2025-08-06, Kontan, Gizmologi give only national 80.66% (survey 10 Apr-16 Jul 2025, n=8,700). Same outlet as worker/verifier; APJII original not found |
| V-A | plan4-social-proof.csv | P4W2-01 | Share shopping via creator-linked content | 76% | AGREE-WEAK | Q: "impact.com Cube Southeast Asia creator economy report 2025 Indonesia 76% purchase through creator affiliate links". Only Marketing Interactive (same as verifier); Cube/impact.com pages and Hellopartner give regional 80-83% affiliate-link purchase, no Indonesia split. Base >2,400 includes creators/experts; metric is affiliate links (verifier's caveat holds) |
| V-C | plan4-origin-boycott.csv | Q6-001 | FAST net loss 9M 2025 vs 9M 2024 | IDR 239.58 bn vs 557.08 bn | AGREE-WEAK | Q: "Fast Food Indonesia KFC rugi bersih kuartal III 2025 turun 56,99 persen sembilan bulan pendapatan Rp3,56 triliun". Bisnis 2025-11-03 (market.bisnis.com/read/20251103/192/1925531) and Katadata tag pages; Bisnis is the verifier's outlet. Values, -56.99%, revenue -0.76% to Rp3.56 tn match |
| V-C | plan4-origin-boycott.csv | Q6-007 | PZZA net profit FY2025 vs FY2024 | IDR 24.75 bn profit vs 72.83 bn loss | AGREE-STRONG | Q: "Sarimelati Kencana laporan keuangan 2025 laba bersih Rp24,75 miliar rugi 2024 Rp72,83 miliar penjualan Rp3,05 triliun". Stockwatch.id (2026-03-31; different outlet) plus Bisnis 2026-03-31. Sales Rp3.05 tn: Bisnis +9.06%, Stockwatch +8.93% (small source gap; Q6-008 growth figure should note it). No IDX filing seen |
| V-E | disconfirming-evidence.md | E17 (P1-C6-S16) | GDP growth Q2 2026 | 5.29% YoY | AGREE-STRONG | Q: "ekonomi Indonesia triwulan II 2026 BPS tumbuh 5,29 persen year on year". Tirto, Kontan, Katadata, JawaPos, Bisnis 2026-08-05 (BPS release date); H1 5.45%, Q1 5.61%; household consumption +5.06% |
| V-E | consumer-surveys.csv | P1C3-01 | Gen Z spend under Rp10,000 per cup | 48% (n=1,155, 6-9 Dec 2024) | AGREE-WEAK | Q: "Jakpat survei kopi Gen Z pengeluaran per cup di bawah Rp10.000 48 persen Desember 2024". Databoks/Katadata 2025-01-07 (same outlet as verifier); Jakpat insight pages surfaced but text not shown. Katadata wording "mayoritas" (48% is a plurality); base of the 48% behind paywall |

## Agreement rate per verifier

| verifier | sampled | AGREE-STRONG | AGREE-WEAK | DISAGREE | any agreement | strong rate |
|---|---|---|---|---|---|---|
| V-D | 6 | 4 | 2 | 0 | 6/6 | 67% |
| V-B | 4 | 4 | 0 | 0 | 4/4 | 100% |
| V-A | 2 | 0 | 2 | 0 | 2/2 | 0% |
| V-C | 2 | 1 | 1 | 0 | 2/2 | 50% |
| V-E | 2 | 1 | 1 | 0 | 2/2 | 50% |
| Total | 16 | 10 | 6 | 0 | 16/16 | 63% |

No row was a hard DISAGREE. One row carries an open conflict: SD11 (see table).

## Recommendation per verifier

- V-B: reliable. All four sampled rows trace to the original publishers (NIQ, YouGov, PwC), and the verifier's own flags (one-search P4W4-08, ref-period correction for P4W3) were accurate.
- V-D: needs stricter rule. Figures match, but 23 of 23 CONFIRMED with zero corrections and snippet-only evidence is too clean. SD11-SD13 (full-year 2025 QRIS: 15.51 bn, +148.54%, Rp1,420.66 tn) could not be reproduced here: 148.5% appears as the Q2 2025 volume growth and a secondary source gives 13.66 bn for 2025. Rule: a headline figure may be CONFIRMED only when two outlets besides the worker's or an original publisher show it; otherwise mark PROVISIONAL-SINGLE-SOURCE. Re-verify SD11-SD13 specifically; SD09/SD10 should wait for the Momentum Works original.
- V-A: needs stricter rule. Both sampled rows rest on one outlet (GoodStats for the generation split, Marketing Interactive for 76%). Rule: do not mark CONFIRMED when the verifier only reaches the same single outlet as the worker; use SINGLE-SOURCE. Its own caveats on P4W2-01 were correct.
- V-C: reliable, with the same single-outlet caveat on Bisnis-only company results (Q6-001 and similar); prefer IDX filing or a second outlet.
- V-E: reliable. E17 is solid; P1C3-01 is a single outlet (Databoks) and the "majority vs plurality" and paywalled base notes were correctly raised.
