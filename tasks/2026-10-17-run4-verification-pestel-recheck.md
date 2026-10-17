# Run 4 re-check V-PEST2: PESTEL Jakarta report and Environmental rows after fixes F1-F17

Verifier: V-PEST2 (independent; did not write the report or the ENV rows). Date: 2026-10-17. Files checked: `reports/2026-10-17-pestel-jakarta.md`, `data/processed/2026-10-pestel-environmental.csv` (full rows incl. notes, in_force_confirmation, amendment_check, gaps), against `tasks/2026-10-17-run4-verification-pestel.md` (F1-F17), `tasks/lessons.md`, CLAUDE.md section 7. Sources reopened with `curl -sL` (browser User-Agent, agent proxy, no bot check bypassed). Nothing edited except this file; no commit.

## Verdict: ACCEPT WITH FIXES

No wrong figure, quote, article number or tier found in the nine changed ENV rows or in the report text. All structural checks (tag trace, Appendix, register ids, verification codes) pass with 0 mismatches. Remaining defects are small: the risk list still says "all" but omits about 10 downside rows (acceptance criterion "disconfirming rows in scope all cited"), one unsupported sentence (SEHATI), F17 not done, and stale "Gap row" notes in four ENV rows.

## 1. The nine changed ENV rows, reopened

| row | source reopened | check | verdict |
|---|---|---|---|
| ENV-004 | BNPB page (REG-047), "25 Jan 2026 13:30 WIB" | Headline "Lebih dari 1.600 warga Jakarta mengungsi"; BPBD sentence "Sedikitnya 585 KK atau 1.623 jiwa ... terdampak" exact (incl. the source's "Penanggulanagan"); the 21 shelter lines sum to 1,610 as the row says; row and report no longer call 1,623 displaced | MATCH |
| ENV-012 | JDIH Jakarta full text 3851 (10 pp, text layer) | Art. 5(1)-(2), 6(1)(a)-(b), 6(2)(a)-(b) (incl. "secara tidak gratis"), 7(1)-(3), 9(1)(b) all exist as cited; both quotes verbatim; report wording "mall managers must bind tenants; each tenant may not provide" matches Art. 6 | MATCH |
| ENV-013 | same | Art. 22(2) a-d, 22(5) DPMPTSP licence sanctions, Art. 24(1) IDR 5,000,000 to 25,000,000, Art. 29(1)-(2) "dengan sengaja membiarkan" gives written warning by the Environment Agency, Art. 30 "6 (enam) bulan" all verbatim; set 27 Dec 2019, promulgated 31 Dec 2019, BD 2019 No. 64003 confirmed; record page 3851: Status Peraturan "Berlaku", Keterangan Status "-". The derived start (30 Jun 2020) is flagged as derived | MATCH |
| ENV-014 | ESDM release 30 Jun 2026 (REG-053); PLN tariff page (REG-055) | "13 golongan pelanggan nonsubsidi tidak mengalami kenaikan", "seharusnya menyebabkan kenaikan", 24 subsidised groups unchanged: found. "vs Q2 2026" is gone from the unit. PLN page lists only "Dokumen Penyesuaian Tarif Kuartal 3 2026": Q4 still not found | MATCH |
| ENV-015 | not reopened (unchanged tier-3 relay; note now points to ENV-022 for the official table) | Record pages 14172 (Pergub 37/2024: set 14 Oct, promulgated 16 Oct 2024, Berlaku) and 14173 (Kepgub 730/2024: set 16 Oct 2024, promulgation "-", Berlaku) confirmed; row correctly stays tier 3 for the January 2025 start | MATCH |
| ENV-018 | JDIH Jakarta full text 1803 (10 pp) | Art. 2(1)-(6) (written warning 14/7/3 x 24 h, publication on a Pemprov site), Art. 4(2)(b) quote "menghindari penyediaan maupun penggunaan kemasan/ produk sekali pakai" and 4(2)(c), Art. 29 six months, set 8 Dec / promulgated 9 Dec 2021, BD 2021 No. 73017, Berlaku: all match. Text names no cups, straws or cafes; "partial gap" label is honest | MATCH |
| ENV-019 | JDIH record 3851 | Status "Berlaku", Keterangan "-"; no amending or revoking relation on the page (grep for diubah/mencabut/dicabut found none) | MATCH |
| ENV-020 | PLN PDF (1 page, image only, rendered and read visually) | "Penetapan Penyesuaian Tarif Tenaga Listrik, Bulan Juli - September 2026"; row 6 B-2/TR 6.600 VA s.d. 200 kVA 1.444,70 (regular and prepaid); row 7 B-3/TM,TT di atas 200 kVA Blok LWBP 1.035,78, WBP = K x 1.035,78, kVArh 1.114,74, K 1.4 to 2; "Jakarta, 01 Juli 2026", signed Direktur Utama. The PDF is the one linked from the PLN page. Expiry on 30 Sep 2026 correctly stated | MATCH |
| ENV-022 | Kepgub 730/2024 Annex II (page 12 of 13, image only, read visually) | K III: Niaga/Industri Kecil 4.900 / 9.500 / 12.500; Menengah 6.825 / 12.500 / 17.500; Besar 12.550 / 17.500 / 21.500: exact. Menengah shares its line with Instansi, Instansi Luar Negeri and Fasilitas Kesehatan Swasta, which the row does not need. "Class for a cafe not read" is honest | MATCH |

Tiers: REG-131 to REG-135 are tier 1 (official legal portal of the Jakarta government for 131 to 134; PLN's own signed tariff document for 135, justification written in the register). ENV-012 and ENV-013 "tier 1" holds: official full text plus official record, both opened. REG-134 is used only for dates and status (text not read), as the register says.

GAP rows: ENV-016 (iqair.com still HTTP 403; udara.jakarta.go.id 200 but live readings only), ENV-017 (only national BMKG read; bmkg.go.id reachable, so closable later, not a false gap), ENV-021 (dibi.bnpb.go.id curl code 000 again). All three remain honest and carry no value.

ENV rows, minor:
- E1 (LOW). ENV-018, ENV-019, ENV-020 and ENV-022 notes still open with "Gap row, no claim made. Dated 2026-10-17." although they are now data rows (ENV-018 is partial). The "Audit follow-up" sentence after it explains the change, so nothing is wrong, but the first sentence contradicts the verification column. Delete the stale sentence.
- E2 (LOW). Register REG-055 says "linked tariff PDF not retrieved: proxy tunnel closed", while ENV-020 and REG-135 now rely on that PDF. Update the REG-055 access note.

## 2. Risk section

I rebuilt the list from table A of `data/raw/2026-10-17-disconfirming-evidence.md` (11 surviving rows; A5, A8, A15 BLOCKED and correctly excluded; A1, A2, A3, A6, A9, A13, A16, A17 all cited) plus every non-blocked mapped row whose notes say "disconfirm" or whose fact is a loss, closure or decline. All 43 rows flagged "disconfirm" in the mapping and CSV notes are cited except price rows P3PB-50 to 57 (false hits on "mulai dari"), P3B-16 (Pizza Marzano 23 outlets; the note only says an earlier "exit disconfirmed" claim was weakened; not a downside fact) and none other. Summary figures in the report (326 courts, +70% race, IDR 10bn, 19% premium, 9 Oct 2026) match the body and the CSV rows (P4W10-01 326; UC-N04 70% yoy; P4W4-02 19). The Summary has no row counts to reconcile.

Still uncited anywhere in the body, though verified and matching the section's own rule ("a loss, closure or decline"):

| row | fact | note |
|---|---|---|
| Q6-002 | FAST revenue -0.76% yoy, 9M 2025 | relay |
| Q6-011 | FAST revenue -3.12% yoy, H1 2025 | relay |
| P3BF-005 | FAST H1 2026 net loss IDR 61.1bn vs 142.3bn (narrowed) | original; a loss fact |
| P3BF-011 | FAST FY2025 operating loss Rp312bn, down 60% | relay |
| UC-N09 | FAST FY2025 net loss Rp366.04bn vs 796.71bn (narrowed) | CORRECTED; mapping says "cite once" with P3BF-017 |
| Q6-006 | MAPB sales -2.77% 9M 2025 | duplicate of DISC-A13, already cited; fine to leave out if stated |
| UB-07 | 39% of pulse chasers cut spending in 12 months (YouGov, Sep 2024) | behaviour |
| P4W9-15, P4W9-18, P4W9-19 | 54% of Gen Z limit social outings; 49% Millennials and 56% Gen Z choose a frugal lifestyle (Mar-Aug 2024, urban) | behaviour, directly against dining out |
| P4W9-29 | Millennials name takeout and international travel as main retrenchment (YouGov, Apr 2025; qualitative) | behaviour |
| P3B-26 to P3B-29 | Hard Rock Cafe, Fish & Co, Marche Movenpick, Karen's Diner closures (2020-2023) | marked HISTORICAL-NOT-IN-BASE-RATE in the CSV; defensible to exclude, but the section does not say so |

Finding R1 (MEDIUM): the section still claims "All verified downside, disconfirming or mixed rows in scope", which is false for about ten rows (FAST rows, the frugality rows, UB-07, P4W9-29). Either add them (one line each, grouped under Operators and Behaviour) or change the first sentence to name the selection rule and list the excluded classes (historical closures, duplicates, narrowing losses). Note that FAST losses narrowed, so they are mixed rather than pure downside, which is a reason to list them in the "Mixed" bullet.

## 3. Appendix

173 rows; every row has exactly four cells (no column drift). The 173 ids in the Appendix equal the 173 ids tagged in the body (none missing either way). Register ids compared with the `register_id` column of the source CSV for all 165 non-DISC rows: 0 differences, none truncated (no id cut at 22 characters). Verification code and original/relay suffix compare equal to the CSV for all 165 rows; ENV-016, 017, 021 show n/a and GAP in the right columns. Period column: no truncation or ellipsis found.
- A1 (LOW). The Appendix intro says "(see Appendix note on GAP rows)"; there is no such note. Delete the parenthesis or add the note.
- A2 (LOW). DISC-A rows show only "VO" or "CO" with no original/relay (A1, A2, A3 are original in the raw table; A6, A9, A17 relay). Add the suffix for consistency.

## 4. Tag trace (rerun, geo and age letters against CSV codes)

198 row-id tag occurrences parsed from `[ids; G-A ...]` brackets. Each id exists in a processed CSV (DISC-A rows in the raw file). Geo letter compared with the CSV `geography` column (and the mapping `geo_scope`), age letter with `age_fit_code` (or mapping `age_split`: "no" = D). Result: 0 real mismatches. Four apparent differences resolved by reading the rows: S-11 J-D (CSV geography "Indonesia; DKI Jakarta", the Jakarta share is the cited figure; the mapping says Indonesia; the report scopes the figure correctly), P1C2-17 U-C and P1C2-18 U-D (CSV geography U; the mapping says "other" for a multi-city urban sample). ENV rows carry no CSV code; the letters assigned (J for Jakarta agency data, N for BMKG, ESDM and P.75) are sensible.
- T1 (LOW). Halal row: "micro and small start 18 Oct 2026 [H-04]". The micro/small phase end is H-02 (PP 42/2024 Art. 160(2)); H-04 is the BPJPH 9 Oct statement (start 18 Oct, no postponement), and its note records that a BPJPH page of 4 Jun 2026 calls this phase a continuation of the medium and large phase. Re-tag to [H-02; N-D] or word it as "mandatory halal starts 18 Oct 2026 per BPJPH [H-04]".
- T2 (LOW). Summary, Political: "halal special provisions were announced on 9 Oct 2026". H-04 says BPJPH said they are being drafted; no text found. Reword to "BPJPH said on 9 Oct 2026 that special provisions are being drafted".

## 5. H-03 step and unlabelled claims

H-03 is fixed: E-07 and H-02 are in the Fact cell as facts; the PMA-is-large-so-medium/large step sits in the Implication cell, begins with "Analysis:", says "this step is analysis, the halal scale test is not shown to follow that class [H-03]", confidence Medium (High for the dates), lawyer question named. The header lists "Analysis:", implication column, "So what (analysis)" and "What it means" as our reading. All six "So what" lines are labelled; "clearly growing", "remain untested" and "cheap to join" are gone. KFC, Starbucks and UMP claims now carry tags and periods.

New or remaining unsupported text:
- U1 (MEDIUM). Under the Legal table: "SEHATI free halal scheme ran in 2025 only and is not available now (note to H-03)". The row H-03 says the FAQ answer refers to SEHATI 2025 ("Sepanjang tahun 2025 selama kuota masih tersedia") and that "whether a 2026 or 2027 round exists was not checked". "2025 only" and "not available now" overreach and this repeats the 2026-10-17 audit lesson (time-limited programme worded beyond its source). Reword: "The BPJPH FAQ describes the SEHATI free scheme for 2025 (while quota lasted); whether a 2026 round exists was not checked [H-03]". Also add a tag.
- U2 (LOW). Water row implication "A small cost line at these rates" has no consumption data behind it; it is in the Implication column (analysis), so allowed, but soften to "rates per m3 only; usage not known".
- U3 (LOW). Summary bullets mix sourced facts with interpretation ("Evidence points to an affluent-tier story ... mixed even there") without the "Analysis:" label that the header rule requires for interpretation. Prefix the interpretive clauses or state that the Summary is our reading.

## 6. Length

Whole file 6,205 words: body (title to "Gaps and method", Appendix excluded) 4,131 words; Appendix 2,070 words; the risk section alone is 740 words. The plan sets no length limit for the PESTEL draft (only the outline, one page). The risk section is a dense semicolon list with about 90 tags; consider grouping, but this is optional. Adding the rows in R1 would add about 120 words.

## F1-F17 status

F1 done, F2 done (see 5), F3 partly (R1), F4 done, F5 done, F6 done, F7 done and verified (section 1), F8 done, F9 done, F10 done, F11 done, F12 done, F13 done, F14 done, F15 done, F16 done. **F17 not done**: `tasks/lessons.md` has no entry for this run's pattern (truncated Appendix cells; analysis shown as fact; disconfirming list built from table A only; stale "gap" notes left in upgraded rows). Add it per CLAUDE.md section 10, with the rule: build the risk list from the mapped CSVs, not only from the disconfirming file; check table cells for truncation before verification; when a gap row is upgraded, rewrite its notes and its "Gap row" boilerplate.

## Fix list for acceptance

| id | where | severity | action |
|---|---|---|---|
| R1 | Risk section | MEDIUM | add the ten uncited downside or mixed rows, or restate the selection rule and say what is excluded and why |
| U1 | Legal, SEHATI sentence | MEDIUM | reword to what the FAQ says; add tag; note the 2026 round was not checked |
| F17 | tasks/lessons.md | LOW (process rule, CLAUDE.md section 10) | add the lessons entry |
| E1 | ENV-018, 019, 020, 022 notes | LOW | remove "Gap row, no claim made" opener |
| E2 | REG-055 | LOW | update the access note (PDF now retrieved, see REG-135) |
| A1, A2 | Appendix | LOW | remove dangling "note on GAP rows"; add original/relay to DISC rows |
| T1, T2 | Halal row tag; Summary wording | LOW | re-tag micro/small start to H-02; "being drafted" |
| U2, U3 | Water implication; Summary | LOW | soften; label interpretation |

No re-research is needed for any fix. After R1 and U1 are applied, a spot check by a verifier on the added rows (P3BF-005, P3BF-011, UC-N09, Q6-002, Q6-011, UB-07, P4W9-15, P4W9-18, P4W9-19, P4W9-29) and the SEHATI sentence is sufficient.
