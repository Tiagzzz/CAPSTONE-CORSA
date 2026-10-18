# Wave 4 spot-audit of Codex pre-verification (2026-10-18)

Auditor: independent Claude subagent. Pages fetched 2026-10-18 via curl. No CSV/report edited.

| item_id | codex verdict | my verdict | evidence (quote) | report usage OK? | note |
|---|---|---|---|---|---|
| R2-TIME-02 | CONFIRMED | AGREE | "Wajib Halal tetap kita implementasikan mulai 18 Oktober 2026. Tidak ada penundaan." Dateline "Jumat (9/10/2026)"; "ketentuan khusus ... UMK dan produk impor" | Yes (report cites BPJPH, R2-TIME-02, phase started 18 Oct 2026) | Quote, date, drafting of special provisions all on page. |
| R2-LBL-01 | CONFIRMED | AGREE | "Data Survei Sosial Ekonomi Nasional (Susenas) September 2025 menunjukkan bahwa garis kemiskinan ... dipengaruhi komoditas pangan." | Not cited in report (id absent); source row P1C4-16 consistent | Rice 21.10/24.62, noodles 2.35/2.04, bread 2.02/1.84 all present. GoodStats is a tier-3 relay of BPS, dated 4 Mar 2026. |
| R1-C09 | CORRECTED | AGREE | "11月19日、チャングー...26日には2号店がウブド" (Canggu 19 Nov, Ubud 26 Nov; article dated 2023.12.05) | Yes (report: Canggu 19 Nov 2023, Ubud 26 Nov 2023, Bali) | No tourist-circuit or Jakarta/Surabaya plans on page, so correction is right. Minor: corrected_value says "stated addresses" but page lacks "near Batu Bolong" and "~700m"; Ubud address is "Jl.Wanawarna Jl. Monkey Forest". Year 2023 inferred from publish date. Report wording unaffected. |
| R1-C12 | CORRECTED | AGREE | "Average payback time is 24 – 36 months"; "ranges from IDR 1.5 – 2.5 billion" | Yes (report: IDR1.5-2.5bn, 24-36 months, "does not evidence" footprint) | No m2 footprint or CHF figure on page; also notes figure excludes land/construction and payback is "depending on location, operations..." (report could add caveat; not an error). |

Summary: 4 items checked (2 CONFIRMED, 2 CORRECTED): 4 AGREE, 0 DISAGREE, 0 UNREACHABLE. No re-check batch needed.

Limitation: only R2-TIME-02, R1-C09 (and C08, C12-C14) appear in the report among Codex CONFIRMED/CORRECTED rows; the second CONFIRMED item (R2-LBL-01) is not report-cited.
