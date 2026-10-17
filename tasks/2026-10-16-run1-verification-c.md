# Run 1 verification C (V-C): plan4 community-sport, origin-boycott, venue

Verifier V-C, 2026-10-16. Hosts re-tested: WebFetch to antaranews.com failed (ENOTFOUND); all source hosts treated as blocked. All verdicts rest on my own WebSearch queries (different wording from the worker's). Search results are tool-written summaries, not raw pages; a "result" below means the summary named the listed URL(s) and gave the stated figure. Publication dates of Bisnis.com items still come from URL paths unless a second outlet gave a date.

Notes on dates: hex IDs in databoks URLs decode to Unix time (68e3153d = 2025-10-06; 690aa3ea = 2025-11-05; 686b637a = 2025-07-07); indotelko 1761172765 = 2025-10-22.

| file | row_id | claim | worker value | verdict | evidence (query / URL / publisher / date) | notes |
|---|---|---|---|---|---|---|
| community-sport | P4W5-01 | Avg weekly run distance, Indonesia, Jul-Sep 2025 | 16 km/week | CONFIRMED | Q: "Strava Indonesia pelari rata-rata 16 km per minggu Gen Z 14 km Boomers..." https://www.goodnewsfromindonesia.id/2025/11/03/gen-z-paling-suka-lari-tapi-yang-paling-rajin-lari-bukan-gen-z (GNFI, 2025-11-03 from URL); also data.goodstats.id, indotelko (2025-10-22) | Strava company data, tier 3; self-selected app users; age-fit D, geo N fine |
| community-sport | P4W5-02 | Gen Z avg weekly distance | 14 km/week | CONFIRMED | Same query/URLs; Boomers about 20 km+ also confirmed | Canonical band "Gen Z 18-28 (approx)" is a worker mapping, native band not stated; age-fit C ok |
| community-sport | P4W5-03 | Runners who supplement running with other exercise | 65% | UNCONFIRMED | Q: "Strava pelari Indonesia 65% menambah olahraga lain selain lari Juli September 2025 survei"; no result carried 65% | Gizmologi/GNFI results did not show the figure. Drop |
| community-sport | P4W5-04 | Jakarta Running Festival participants | 27,300 runners, 48 countries | CONFIRMED | Q: "Jakarta Running Festival 2025 27.300 pelari 48 negara..." investortrust.id, emitennews.com, metrotvnews.com, BNI release (bni.co.id); event 25-26 Oct 2025 | Company/organiser figure (BNI/KLAB). Also notes pre-event target nearly 30,000 / 50+ countries; ">1,000 foreign runners from 48 countries" so "48 countries" may refer to foreign runners only |
| community-sport | P4W5-05 | JRF growth vs prior edition | +70% | UNCONFIRMED | Q: "Jakarta Running Festival 2025 jumlah peserta meningkat 70 persen dari 2024 BNI KLAB"; no 2024 count or growth found in any result | Drop |
| community-sport | P4W5-06 | Padel GMV per court | >EUR 6,000/month (2023-24) | CONFIRMED | Q: "Playtomic Indonesia padel court revenue per month EUR 6,000 GMV per court Indonesia": goodnewsfromindonesia.id 2026-02-23 (URL date) and goodstats.id/article/indonesia-jadi-negara-dengan-popularitas-padel-tertinggi (date unseen) | GoodStats gives EUR 6,300 (2024) vs EUR 2,300 (2023), consistent with ">6,000". Original Playtomic report not opened. Low relevance for F&B; GMV is not net revenue. Date from URL only |
| community-sport | P4W5-07 | Padel GMV growth | +173% yoy 2023-24 | CONFIRMED | Same search; also Q: "Playtomic Global Padel Report 2025 Indonesia GMV per court 173%" (GoodStats: Indonesia largest GMV increase, 173%) | One of my searches framed 173% as total GMV growth, the other as per-court (2,300 to 6,300 = +174%). Metric basis (per court vs total) is ambiguous; keep the label "per-court GMV" only if the report is opened |
| community-sport | P4W5-08 | Padel courts sealed, North Jakarta | 2 courts, Mar 2026 | CONFIRMED | Q: "Sudin Satpol PP Jakarta Utara segel lapangan padel Ancol Penjaringan PBG 2026": metrotvnews.com, cna.id, merahputih.com, rri.co.id; sealed 4 Mar 2026 by Sudin Citata | Courts at Ancol and Pluit (Penjaringan); sealed for missing PBG. Context: 185 padel buildings lacked PBG as of 23 Feb 2026 (not in dataset) |
| origin-boycott | Q6-001 | FAST net loss 9M 2025 vs 9M 2024 | IDR 239.58bn vs 557.08bn | CONFIRMED | Q: "Fast Food Indonesia FAST rugi bersih Rp239,58 miliar September 2025 laporan keuangan"; Bisnis 20251103 (market.bisnis.com/read/20251103/192/1925531/...), databoks.katadata.co.id (690aa3ea, 2025-11-05), idnfinancials | Period is 9M (Jan-Sep), IDR billion, loss narrowed 56.99%/57%. Worker's cited URL (20251128) is a different article; figure holds. Date 2025-11-03/05 confirmed |
| origin-boycott | Q6-002 | FAST revenue 9M 2025 | -0.76% yoy; IDR 3.56 trn | CONFIRMED | Q: "Fast Food Indonesia KFC nine months 2025 net loss narrows revenue 3.56 trillion": idnfinancials, databoks | 9M 2024 was IDR 3.59trn. Period 9M confirmed |
| origin-boycott | Q6-003 | Management: boycott eased, still hurts regions | qualitative | CONFIRMED | Same results: management cites weaker purchasing power and lingering boycott impact; Bisnis 20251128 headline "...Tekanan Boikot Sudah Mengendur" listed in search | Qualitative, wording differs slightly; "eased" rests on Bisnis headline |
| origin-boycott | Q6-004 | FAST outlets closed / layoffs 2025 YTD | 19 outlets; 400 employees | CONFIRMED | Q: "KFC Indonesia tutup 19 gerai PHK 400 karyawan 2025": finance.detik.com d-8141221, wartaekonomi.co.id, kontan; public expose 2 Oct 2025 | 19 outlets / about 400 staff to Sep 2025. Caveat: another source says 25 stores / 1,400 workers for full year (People Matters), different period. Reasons: lease expiry/relocation as well as boycott |
| origin-boycott | Q6-005 | MAPB net loss 9M 2025 vs 9M 2024 | IDR 108.69bn vs 79.13bn | CONFIRMED | Q: "MAP Boga Adiperkasa MAPB kuartal III 2025 rugi Rp108,69 miliar penjualan Rp2,35 triliun": Bisnis 20251103 and Bisnis 20241031 "Berbalik Rugi Rp79,13 Miliar di Kuartal III/2024" (the prior-year article, dated 2024-10-31) | Cumulative Jan-Sep, not single quarter. FY2025 loss IDR 150.77bn (Bisnis 2026-03-31) is newer and could be added |
| origin-boycott | Q6-006 | MAPB sales 9M 2025 | -2.84% yoy; IDR 2.35 trn (vs 2.42) | CONFIRMED | Same query; search summary with beverages 1.31trn, food 910.79bn split | Only Bisnis seen (single outlet). Keep, but flag single-publisher |
| origin-boycott | Q6-007 | PZZA net profit FY2025 vs FY2024 | 24.75bn profit vs 72.83bn loss | CONFIRMED | Q: "Pizza Hut Indonesia PZZA full year 2025 net profit 2025 results March 2026": Bisnis 20260331 and receh.in 2026/06 | First search (different wording) could not find it; second did. Weak independence: Bisnis plus a reprint-style site. Units IDR billion, FY confirmed |
| origin-boycott | Q6-008 | PZZA sales FY2025 | +9.06%; IDR 3.05 trn | CONFIRMED | Same search as Q6-007 | Same caveat on independence |
| origin-boycott | Q6-009 | PZZA net profit 9M 2025 | IDR 15.91bn | CONFIRMED | Q: "Sarimelati Kencana PZZA laba kuartal III 2025 Rp15,91 miliar": Bisnis 20251028, emitennews.com, pintarsaham.id, kabarbursa | Prior-year 9M loss IDR 96.71bn. 9M period confirmed |
| origin-boycott | Q6-010 | Share price YTD change to 1 Dec 2025 | UNVR +38.99; MAPB +35.83; FAST +71.23; PZZA +100 (%) | CONFIRMED | Q: "saham FAST PZZA MAPB UNVR sepanjang tahun berjalan 2025 naik 71,23% 100%": Bisnis 20251202 (article date 2025-12-02) | Single publisher; FAST at IDR 500, PZZA IDR 226 (PZZA +100% is "dua kali lipat" per article). Sentiment proxy |
| origin-boycott | Q6-011 | FAST revenue H1 2025 | -3.22% yoy; IDR 2.40 trn | CORRECTED | Q: "KFC FAST semester I 2025 pendapatan turun 3,22% Rp2,40 triliun rugi": finance.detik.com d-8047534 and detik sumut d-8047583, wartaekonomi.co.id | Correct is -3.12% (from IDR 2.48 trn to IDR 2.40 trn); no source shows 3.22. Level 2.40 trn correct. Net loss H1 attributable IDR 138.75bn |
| origin-boycott | Q6-012 | Berjaya Food / Starbucks Malaysia revenue | -36% FY to Jun 2025 | CONFIRMED | Q: "Berjaya Food Starbucks Malaysia revenue fell 36% boycott financial year June 2025": malaymail.com 2025-08-28, bloomberg.com 2025-08-28, insideretail.asia 2025-09-02, FMT | Precise: -36.5% (RM476.77m from RM750.7m); net loss RM291.99m. Geo P proxy ok |
| origin-boycott | Q8-001 | Mandalika MotoGP total spectators | 140,324 | CONFIRMED | Q: "MotoGP Mandalika 2025 penonton 140.324 rekor ITDC": kontan, katadata, ekon.go.id, GNFI (2025-10-08); MGPA count; databoks 68e3153d (2025-10-06) | Source is MGPA (organiser) count. 2026 edition later reported 157,875 (+12.5%), so 140,324 is a 2025 value, not latest |
| origin-boycott | Q8-002 | Spectators, minister statement | 142,000 | CONFIRMED | Q: "Thohir Mandalika MotoGP 142,000 spectators Antara October 2025": mataram.antaranews.com, en.republika.co.id dated 2025-10-05 | Date now established (5 Oct 2025). Detik quotes Thohir saying "140 ribu", so wording varies; not independent of Q8-001 (rounded/ministerial) |
| origin-boycott | Q8-003 | Spectators 2024 and 2023 | 121,252 (2024); 102,929 (2023) | CONFIRMED | Q: "Mandalika MotoGP 2024 penonton 121.252 2023 102.929 naik 15,7 persen": goodstats.id infographic, detik oto d-7705317, mataram.antaranews.com 380275 | Values hold. Both events (Sep 2024, Oct 2023) predate 2024-10-16; kept only as trend context inside a post-cutoff series, as worker labelled. 2024->2023 growth about 18% |
| origin-boycott | Q8-004 | Spectator growth 2025 vs 2024 | +15.7% | CONFIRMED | Same results: +19,072 people, 15.73% (MGPA via kontan etc.) | Derivable from 140,324 vs 121,252 (15.73%) |
| venue | Q7-001 | Word of mouth main driver of coffee choice | qualitative, n=1,002 | CONFIRMED | Q: "Jakpat coffee survey 2025 word of mouth main driver choosing coffee 1,002 respondents": insight.jakpat.net/healthy-living-and-coffee-trends-in-2025/ and databoks.katadata.co.id/en/.../686b637ab0009 (hex = 2025-07-07) | Date now established as about July 2025 (databoks). Jakpat also reports 57% trust recommendations from close people vs TV ads 38% (usable quantitative value, not in the row). Coffee choice, not venue choice; age split not shown |

## Summary

Rows checked: 25 (community-sport 8, origin-boycott 16, venue 1).

| verdict | count |
|---|---|
| CONFIRMED | 22 |
| CORRECTED | 1 (Q6-011) |
| UNCONFIRMED | 2 (P4W5-03, P4W5-05) |
| DATE-FAIL | 0 |
| TIER-FAIL | 0 |
| DERIVED | 0 |

Row_ids to drop: P4W5-03, P4W5-05.

Row to correct: Q6-011 (value -3.12%, not -3.22%; level IDR 2.40 trn unchanged).

Systemic issues:
- Bisnis.com dates were taken from URL paths; I saw them corroborated by search results for Q6-001, 005, 009, 010 only. Q6-002, 003, 006, 007, 008 carry the same URL-date caveat, though other outlets support the period.
- Q6-001/Q6-003: the worker's cited Bisnis URL (20251128) is not the article that carries the figure (Bisnis 20251103 does). Fix source key/URL at registration.
- Q6-006, 007, 008, 010 have a single effective publisher (Bisnis.com) plus weak corroboration; flag as single-source.
- P4W5-06/07: Playtomic report not opened and the per-court vs total-GMV basis is inconsistent across secondary sources. Q8-001/002 are one underlying count in two forms.
- Worker findings for P4W5-S1 listed goodstats/gizmologi (tier 3-4 republishers); the tier-3 GNFI article independently carries 16 km / 14 km.
