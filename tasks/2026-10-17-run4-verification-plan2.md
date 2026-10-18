# Run 4 verification V-P2b: Plan 2 report after fixes

Date: 2026-10-17. Verifier: V-P2b (independent; did not write the report). Object: `reports/2026-10-17-regulatory-entry-pathway.md` (5,173 words). Read first: CLAUDE.md §5 and §7, `tasks/lessons.md` (last entry: full rows incl. notes, in_force_confirmation, amendment_check, gaps), `tasks/2026-10-17-run3-report-verification-plan2.md` (F1-F16), `tasks/2026-10-17-main-session-audit.md`. Every CSV row I judged was read in full (all columns). The report was not edited. Nothing was committed.

## Verdict: ACCEPT WITH FIXES

No blocker and no mismatch of value, unit, period or article number against an opened source. All 16 earlier findings and the three audit fixes are applied. Residual items are wording and traceability: two article statements that no CSV row records (Art. 37(5); Art. 3(b)-(d)), one of them imprecise, a misplaced +0.1% figure, a few untagged or mis-tagged table cells, and report length. None changes a conclusion.

## 1. Check 1: F1-F16 and audit fixes

| Item | Status | Evidence in the report |
| --- | --- | --- |
| F1 | Applied | §2.4: Text paragraph keeps only definition and STPW; the no-PMA-threshold claim is under "Analysis:" and says it "rests on a worker note in F-07, not on Art. 1(1)", conditional on Indonesian ownership (question 3). Royalty wording is "may be" (question 17). |
| F2 | Applied (CHF rate half-fixed) | Summary and §3 separate plan (above IDR 10bn) from paid-up capital (IDR 2.5bn); Art. 37(4)(a)-(e), 37(5) added; question 4b added. The CHF rate is still only "Plan 2 rate, not re-verified" (no date or source); see N8. |
| F3 | Applied (Art. 26 wording imprecise) | Art. 4(6) audit exemption in deal-breaker 3, §2.0, handoff. Art. 26 conditional wording added, but see N2. |
| F4 | Applied | "Analysis: if a PMA also counts as large ... question 12"; "from 18 Oct 2024" tagged as BPJPH's reading (H-02 · REG-010). |
| F5 | Applied | Paragraph renamed "Street mobilisation"; §7 lists Aug 2025 unrest, buy-local, ratings, partial policy list as GAP. |
| F6 | Applied (see N5) | §2.0 comparison table (4 columns incl. licence), §2.0b handoff table, T16/T17/T28 named. |
| F7 | Applied | H1 "Not supported ... questions 1-5"; H2 "Not supported; medium confidence" with Hukumonline as second source. H5 still "Refuted" (not required by F7). |
| F8 | Applied | "(risk level and lead time unconfirmed, section 7)". |
| F9 | Applied | LPH bullet: unit cost x mandays, operational ceiling, transport/allowance, "total needs an LPH quote (GAP)". Matches H-09. |
| F10 | Applied | "withdrawal of the product from circulation". |
| F11 | Applied (see N3) | FAST attributable vs total labelled; PZZA flagged as relay with conflict; Starbucks "reported ... as MAPB's view (speaker and date not shown)"; +0.1% added but misplaced. |
| F12 | Applied | 1b, 4b, labour, Art. 23(12), Art. 40, VAT on packaged goods, supervision, owner line added. |
| F13 | Applied | Summary heading has as-of date and "re-check BPJPH on 19-20 Oct 2026"; Art. 197 in the Kepkaban row. |
| F14 | Applied | "as summarised by DJP; law text not opened" on all three T-08 tag clusters. Same qualifier is missing on T-09 (N6). |
| F15 | Not resolved | Summary still prose; length rose from about 3,550 to 5,173 words (N7). |
| F16 | Applied | "the 5 days do not cover the central STPW ... (question 9)". |
| H-03 | Applied | Report §2.2 and the CSV row: SEHATI "ran 'Sepanjang tahun 2025 selama kuota masih tersedia' ... not assumed to be running now". I re-opened the FAQ (below): the wording matches. |
| H-12 | Applied | Row article widened to Art. 147-154 with the FAQ named as fee source; the report keeps Art. 160(3) for the deadline and tags the fee to the FAQ. FAQ answer "Rp800.000 per registrasi sertifikat" confirmed. |
| F-05 | Applied | Report cites Kontan (REG-901, tier 3) and keeps the test a lawyer question; row `amendment_check` holds the Kontan evidence and the Tempo 403. See N4 for two small precision points. |

## 2. Check 2: mechanical tag trace

Script (`/tmp/claude-0/-home-user/553641e4-6cbd-5274-9017-111a78c63f8c/scratchpad/trace.py`) matched every `[row · register_id · instrument]` tag to the CSVs in `data/processed/` (the three `2026-10-p2-*.csv`, `listed-operators.csv`, `plan4-origin-boycott.csv`) and to `sources/sources.md`.

- 145 tag occurrences, 104 unique tags.
- Row id exists: 104/104. Register id found in the row's `register_id`: 104/104. `verification` is VERIFIED-OPENED or CORRECTED-OPENED: 104/104 (several are "(relay)" and are marked in the report). Register id present in `sources/sources.md`: 104/104, including REG-901.
- Not traceable to a row (correct against the opened text, but in no CSV `article`/`quote`): Art. 37(5) of Permen 5/2025 (E-06 lists Art. 37(3)-(4) only) and Art. 3(b)-(d) of PP 35/2024 (F-06 lists Art. 26-27, F-07 lists Art. 3(a), (e)). The report attributes both to "the V-P2 verification" instead of a row (N1, N2).

## 3. Check 3: sources behind the new content, re-opened

All fetched with `curl -sL` and a browser user agent; no bot check bypassed (all HTTP 200). Files in `/tmp/claude-0/-home-user/553641e4-6cbd-5274-9017-111a78c63f8c/scratchpad/dl/`.

| Claim in report | Source opened | Result |
| --- | --- | --- |
| Art. 26(2): total investment above IDR 10bn excluding land and building, per 5-digit KBLI per project location | REG-001 PDF (698 pp, pdftotext), "Pasal 26" | MATCH |
| Art. 26(3)(b), 26(4): F&B per first 2 KBLI digits per 1 location point; point applies per kabupaten/kota | same | MATCH |
| Art. 26(10): paid-up capital at least IDR 2.5bn per PT, "kecuali ditentukan lain" | same | MATCH |
| Art. 27(1): 12-month lock, except asset purchase, building construction and/or operations | same | MATCH (text cross-refers to "Pasal 26 ayat (6)", the slip noted in E-03) |
| Art. 26(1): PMA is usaha besar | same | MATCH |
| Art. 37(3): OSS validates the planned investment for a PMA | same | MATCH |
| Art. 37(4)(a)-(e): plan covers at least land, building, machinery/equipment, other investment incl. operating costs during construction, working capital for one turnover (wages, rent, operating costs) | same, "Pasal 37" | MATCH. Wording is "paling sedikit" (at least). |
| Art. 37(5): financing sources are own capital, loans, retained profit, share premium | same | MATCH as a list of financing sources in the OSS entry (Art. 37(1)(c)). The text does not say a loan-funded plan satisfies the Art. 26 test; the report says this is open (question 4b), which is right. |
| Art. 23(9), 23(11), 23(12); Art. 364(3)(h) | same | MATCH |
| PP 35/2024 Art. 3(b)-(d) | REG-029 JDIH PDF (45 pp) | Art. 3(b) domestic franchisor, (c) sub-franchisor from a foreign franchise, (d) sub-franchisor from a domestic franchise. See N2. |
| Art. 26(1), (3), (5) bind Art. 3(b)-(d); 26(2), (4) bind Art. 3(e)-(h); (2) conditional on the franchisor's written quality standards; (4) and (5) conditional on franchisor requirements; no quota; (6) refers to other rules | same | MATCH on content; wording of the report's scope is imprecise (N2). |
| Art. 4(5): 3 consecutive years plus 2 audited profit years; Art. 4(6): audit exempt for micro and small franchisors | same | MATCH. The 4(6) exemption is of the auditor requirement only, as the report says. |
| Kontan (REG-901): 30 Jun 2025, minister Budi Santoso says four Permendag revoked (36/2007, "22 Tahun 2006" as amended by 6/2019, 25/2020, 4/2023), replaced by Permendag 26/2025; Permendag 25/2025 governs regional STPW; 71/2019 not mentioned | `nasional.kontan.co.id/news/empat-permendag-dicabut-...` | MATCH on date, list and numbers. See N4. |
| BPJPH FAQ: SEHATI "Sepanjang tahun 2025 selama kuota masih tersedia"; code SEHATI25 for TA 2025; RSHLN fee "Rp800.000 per registrasi sertifikat" | `bpjph.halal.go.id/faq` (answers are in the page's embedded JSON) | MATCH on all three. The FAQ is undated, as the report says. |

Rows quoted in the report but not re-opened by me this run: tax and halal rows already opened by V-P2 (run 3), news relays and filings. I read their rows in full and compared every figure in the report to the row (S-03 to S-11, UC-N09, UC-N11, Q6-007, T-01 to T-15, H-02 to H-12, F-02 to F-09): no value, period or unit mismatch.

## 4. Findings table

| # | Location | Issue | Severity | Fix |
| --- | --- | --- | --- | --- |
| N1 | Summary deal-breaker 1; §3; §6 question 4b (Art. 37(5)) | Art. 37(5) is correct in the opened text but is in no CSV row (E-06 `article` and `quote` stop at Art. 37(3)-(4)). The report cites "the V-P2 verification" for the article number, a process reference rather than a row. This is the traceability the lessons rule on full rows is meant to prevent. | minor | Add Art. 37(1)(c), 37(5) with a quote to E-06 (`article`, `quote`, `notes`) and tag the sentences `[E-06 · REG-001 · Permen 5/2025 Art. 37(5)]`; delete "article number from the V-P2 verification". |
| N2 | §2.2 Franchise last two bullets (line 112) | (a) "Art. 26(1), (3), (5) bind domestic franchisors only (Art. 3(b)-(d))" is imprecise: Art. 3(b)-(d) covers domestic franchisors and also sub-franchisors (Pemberi Waralaba Lanjutan) of foreign and domestic franchises. A local master licensee who sub-franchises a foreign (Swiss) franchise is Art. 3(c) and would carry the domestic-goods, local-MSME-supplier and MSME-franchisee duties; the report's route (b) does not mention this. Foreign franchisors (3(a)) and franchisees (3(e)-(h)) are correctly outside (1), (3), (5). (b) Art. 3(b)-(d) is in no CSV row (F-06 lists Art. 26-27; F-07 lists Art. 3(a), (e)). (c) "(Art. 26(2), (4))" for the quality-standard condition: only (2) is about quality standards; (4) and (5) are conditional on the franchisor's requirements. | minor (substantive nuance for the master-licence route) | Reword: "Art. 26(1), (3), (5) bind domestic franchisors and sub-franchisors (Art. 3(b)-(d)), not a foreign franchisor (3(a))". Add Art. 3(b)-(d) to F-06 `article`/`notes`. Say "(2) quality-standard condition; (4) and (5) depend on the franchisor's requirements". Note the sub-franchisor effect for a master licence under route (b). |
| N3 | §5 Investment climate | "PMA realisation was flat (+0.1%, relay-only rate)" follows the Jan-Jun 2026 sentence and has no tag, so it reads as an H1 2026 figure. The +0.1% is FY2025 (S-09: PMA IDR 900.9tn vs 900.2tn; relay-only rate). The DKI share sentence has no period (H1 2026, cumulative; PMA+PMDN combined). | minor | Write "FY2025 PMA realisation was flat (+0.1%, relay-only rate)" and tag `[S-09 · REG-043 ...]`. Add "H1 2026" and "PMA+PMDN combined" to the Jakarta sentence. |
| N4 | §1 deal-breaker 3 (Kontan) | The report lists "22/2016" as what Kontan reports. Kontan prints "Permendag 22 Tahun 2006" (the F-05 row records the misprint; the report does not). The "71/2019 is not among them" statement rests on absence from a list in a news article, a minister's oral statement. | minor | Write "Kontan prints 22/2006 (the instrument appears to be 22/2016, per the F-05 row)" and "Kontan does not mention 71/2019". |
| N5 | §2.0 comparison table | Most cells are tagged facts, GAP or "(analysis)". Exceptions: (i) "Not applicable" for franchisor test in (a), (c); (ii) "Same, at the operator / at the PT" in the tax row, (b)-(d); (iii) "Royalty or service fee; question 17" in (d); (iv) halal duty (a) "Mandatory certificate" is tagged to the tariff row H-08, not to a row for the duty (H-01/H-02); (v) paid-up capital (c) is a flat fact although the PMA status of a JV PT is open (Art. 23(9)); (vi) the tax row heading says "outlet sales" but includes CIT. | minor | Label (i)-(iii) "Analysis:" or tag; add `[H-01 · REG-009 · PP 42/2024 Art. 2(1)]` in (iv); in (v) write "IDR 2.5bn per PT if the PT is a PMA (question 3)". |
| N6 | §2.0b, §2.2 Tax (T-09 tags) | `[T-09 · REG-026 · UU PPh Art. 26(1)]` lacks "as cited by DJP; law text not opened" (row: article "as cited by DJP"). Same pattern as F14 for T-08. VAT (T-15): "12% statutory, effective 11%" is given in the present tense; the row says the 2026 status was not re-verified and PMK 11/2025 may have revised parts of the package; the report says only "relay; PMK not opened". | minor | Add the qualifier to T-09 tags; add "2026 status not re-verified" to the VAT lines. |
| N7 | Whole report; Summary | Plan §8 caps the report at 8 pages, tables first. The report grew from about 3,550 to 5,173 words (about 11 to 12 pages at this layout); the Summary is still prose and tables begin at §2.0. F15 not resolved. | minor | Owner call: either accept as an extended draft, or lead with the §2.0 table and the §2.0b handoff table, and move §2.2 and §6 to an appendix. |
| N8 | Summary deal-breaker 1; §3 (CHF figures) | "About CHF 116k" and "about CHF 463k / 2.3 times" are derived from an unsourced Plan 2 rate; F2 asked for the rate to be dated and sourced. Labelled "not re-verified", so no fabrication, but it is a derived value in the body (lessons rule f). | minor | Give the rate and its date from plan 2 or an official source, or state the figures as "plan's conversion" in notes. |
| N9 | §6 question 4 | Question 4 still asks whether "pre-opening costs" count, but §3 and Art. 37(4)(d) say pre-opening operating costs during construction count. The open points are leasehold fit-out, deposits, and operating costs outside the construction period. | minor | Narrow question 4 accordingly. |
| N10 | §2.2 Halal sanctions bullet | Tag `Art. 170(2), 170(7), 171(3)` omits Art. 171(2), (4), (5), which carry the warning, withdrawal and the non-attachment of revocation. "BPJPH says closure ..." is tagged only to REG-009 (H-11 notes: BPJPH reading, REG-010/013). | minor | Cite Art. 171(2)-(5) and add `[H-11 · REG-010 ...]` for the BPJPH closure statement. |
| N11 | §2 "Contradictions" and §3 second paragraph | T17 "resolved on the text" includes the judgement "larger barrier"; the "Three options" paragraph (route to test first, "small next to the threshold") is analysis without a label. The route is framed as to be tested, so no overstatement. | minor | Prefix with "Analysis:". |

## 5. Check 4: fact versus analysis; time-limited rules

- Tagged sentences report their rows, apart from N2 (scope wording), N3 (period) and N10 (article set). The F-07-based threshold claim is correctly moved to "Analysis:" and conditioned.
- Time-limited rules carry their period: SEHATI "Sepanjang tahun 2025" and "not assumed to be running now" (H-03); 20% PBJT reduction Aug-Dec 2025, expired 31 Jan 2026 (T-06); Keppres 38/2025 one-year programme from 22 Dec 2025 (E-02); halal phases with dates (H-02); 9 Oct 2026 BPJPH statement (H-04); Minister deadline 17 Oct 2026 (H-12). The VAT line (N6) and the Jakarta H1 figure (N3) are the only ones without a period or a currency check.
- "Analysis:" use is consistent in Summary, §2.3 to §2.5, §3, hypotheses and §5, apart from N11.

## 6. Check 5: tables

- **§2.0 comparison table.** Cells are tagged facts, GAP, or labelled analysis, except N5 (i)-(vi). All tagged cells trace to rows (section 2). Licence-outside-Waralaba column is mostly GAP, which is honest.
- **§2.0b handoff table (numbers against rows).** All match: IDR 10bn (E-04), IDR 2.5bn and 12 months (E-03), PBJT 10% and IDR 42m (T-01, T-04), CIT 22% and 11% up to IDR 4.8bn per DJP (T-08), royalty 10% and 20% (T-11, T-09), service fee 5% (T-13), dividend 10% at 25% direct or 15% (T-10), BPJPH tariffs 12.5m / 5m / 300k (H-08), foreign registration 800k (H-12), LPH IDR 3,687,500 x 4-7 mandays row 17 (H-09), halal maxima 5 / 15 (+10) / 3 / 1 (H-10), VAT 12% / 11% relay (T-15). Open items: N6 (T-09 qualifier, VAT currency).
- **§2.1 in-force table.** Statuses match the rows (E-08, F-01, F-05, F-09, H-01, H-07, H-08, T-05). Wording "no amendment found, not 'confirmed none'" is correct.

## 7. Claims checked and results (summary)

| Group | Checked | Result |
| --- | --- | --- |
| Permen 5/2025 Art. 23, 26, 27, 37, 364 | against the opened PDF | all match; Art. 37(5) not in a row (N1) |
| PP 35/2024 Art. 3, 4(5)-(6), 26, 27 | against the opened PDF | content matches; scope wording imprecise (N2) |
| Kontan REG-901 | opened | matches; two precision points (N4) |
| BPJPH FAQ (SEHATI period, SEHATI25, RSHLN 800k) | opened | matches |
| 104 unique tags | script | 0 failures |
| Handoff table values | against rows | 0 mismatches |
| Sentiment and operator figures | against rows | 0 mismatches; N3 on placement |
| F1-F16, H-03, H-12, F-05 | against the revised report | all applied; F15 open |

## 8. Fix list (priority)

1. N2 (reword Art. 26 scope; add the sub-franchisor effect for route (b); add Art. 3(b)-(d) to F-06).
2. N1 (record Art. 37(5) in E-06; tag the sentences).
3. N3, N4, N5, N6, N10 in one wording pass (no new research).
4. N7, N8, N9, N11 at the owner's discretion.

After these, re-verification of N1, N2 and N5 only is enough.
