# Run 4 verification V-P2c: narrow re-check of the Plan 2 report after fixes N1-N11

Date: 2026-10-17. Verifier: V-P2c (independent; did not write the report). Object: `reports/2026-10-17-regulatory-entry-pathway.md` (HEAD, 4,495 words; the V-P2b version at commit f3f5ea0 had 5,173). Findings list: `tasks/2026-10-17-run4-verification-plan2.md`. I read the full CSV rows (finding, article, quote, in_force_confirmation, amendment_check, gaps, notes) for E-03, E-04, E-06, F-05, F-06, F-07, T-09, T-15, H-01, H-05, H-07, H-11. The report was not edited. Nothing was committed.

## Verdict: ACCEPT WITH FIXES

N1, N2 and N5 are fixed and match the opened sources. N3, N4, N6, N9, N10 and N11 are also fixed. All tags still resolve. The N7 trimming kept every question and every gap, but it dropped two small items that were previously required or present: Art. 197 in the Kepkaban row (the F13 fix) and the "Control and brand risk" row of the comparison table. Both are minor and can be restored in one wording pass. No conclusion changes.

## 1. Targeted checks

| Item | Result | Evidence |
|---|---|---|
| N1 | Fixed | Summary deal-breaker 1, section 2.2 and section 3 tag Art. 37(5) to `[E-06 · REG-001 · ...]`. The E-06 row now has `article` "Art. 37(3)-(4)(a)-(e); Art. 26(2)-(3); Art. 37(1)(c), 37(5)" and a `notes` entry giving the financing sources and "text does not say a loan-funded plan satisfies the Art. 26 test". I re-read Permen 5/2025 Art. 37 (REG-001 PDF, pdftotext, opened this session): 37(1)(c) "sumber pembiayaan"; 37(5)(a)-(d) modal sendiri, pinjaman, laba ditanam kembali, agio saham. MATCH. The "article number from the V-P2 verification" wording is gone from the Summary. |
| N2 | Fixed | I re-downloaded PP 35/2024 (`curl -sL` with browser UA from the JDIH Kemendag download link, HTTP 200, 45 pages, pdftotext) and copied the numbers from the text. Art. 3: (a) foreign franchisor; (b) domestic franchisor; (c) sub-franchisor of a foreign franchise; (d) sub-franchisor of a domestic franchise; (e)-(h) the four franchisee categories. Art. 26(1), (3), (5): "Pasal 3 huruf b sampai dengan huruf d". Art. 26(2), (4): "Pasal 3 huruf e sampai dengan huruf h". (2) conditional on the franchisor's written quality standards; (4) and (5) conditional on the franchisor's requirements. Art. 26(6) refers to other rules. Art. 27: "mengutamakan pengolahan bahan baku di dalam negeri". The report (section 2.2, last-but-one bullet) now says (1), (3), (5) bind domestic franchisors and sub-franchisors including sub-franchisors of a foreign franchise (3(b)-(d)), not a foreign franchisor (3(a)); (2), (4) bind franchisees (3(e)-(h)); (2) quality-standard condition; (4) and (5) depend on franchisor requirements. All MATCH. The sub-franchisor effect for a master licence appears in the Summary closing Analysis and section 2.4 (labelled Analysis). F-06 `article` and `notes` now carry Art. 3(b)-(d) and the same wording. |
| N5 | Fixed | Section 2.0 table: "Not applicable" cells are now "Analysis: not applicable"; the tax-row cells carry "Analysis: same, at ..." and point to the tagged cells in 2.0b; the (d) cross-border cell is "Analysis: ... question 17"; the halal (a) cell has `[H-01 · REG-009 · Art. 2(1)]` plus the tariff tag; the JV paid-up capital cell reads "IDR 2.5bn per PT if the PT is a PMA (question 3)" with the E-03 tag; the tax row heading is now "Tax on outlet sales and profit". Cells that point to 2.0b ("tags in 2.0b") are untagged themselves but the target cells are tagged: acceptable. |
| N3 | Fixed | "FY2025 realised investment ... PMA IDR 900.9 trillion, flat (+0.1%, relay-only rate). [S-09 ...]" and "In H1 2026 (cumulative, PMA and PMDN combined) DKI Jakarta ... [S-11 ...]". Period and scope are stated. |
| N4 | Fixed | Section 1 deal-breaker 3: "'22 Tahun 2006' as Kontan prints it (22/2016 per the F-05 row)"; "Kontan does not mention 71/2019; this absence rests on a minister's oral list, not a revoking article". Matches the F-05 `amendment_check`. |
| N6 | Fixed | The T-09 tag in 2.0b reads "as cited by DJP; law text not opened" (row article: "as cited by DJP"). The VAT line says "2026 status not re-verified, PMK 11/2025 may have revised parts of the package", matching T-15 `in_force_confirmation` and `amendment_check`. |
| N9 | Fixed | Question 4 now narrows to leasehold fit-out, deposits and operating costs outside the construction period, and notes Art. 37(4)(d) already counts operating costs during construction (matches the opened Art. 37(4)(d)). |
| N10 | Fixed | Halal sanctions bullet cites Art. 170(2), 170(7), 171(2)-(5) and tags the BPJPH closure reading to `[H-11 · REG-010 · BPJPH statements]`; H-11 `article` and `notes` agree. |
| N11 | Fixed | "Analysis:" prefixes added to the T17 judgement and the "three options" paragraph. |
| N8 | Unchanged by design | CHF 116k / 463k still rest on an "undated, unsourced Plan 2 rate", now stated three times (Summary, section 3, section 8). Honest labelling, no fabrication; owner discretion. |
| N7 | Partly | 5,173 to 4,495 words (-13%). The Summary now opens with a 3-row barrier table, but the deal-breakers are still prose. Length is an owner call. See section 3 for what the trimming dropped. |

## 2. Tag trace (rerun on all tags)

Script: `/tmp/claude-0/-home-user/553641e4-6cbd-5274-9017-111a78c63f8c/scratchpad/trace2.py`.

- 100 unique tags (104 before; shortening merged duplicates).
- Row id exists in the Plan 2 CSVs, `listed-operators.csv` or `plan4-origin-boycott.csv`: 100/100.
- Register id found in the row's `register_id`: 100/100.
- `verification` is VERIFIED-OPENED or CORRECTED-OPENED: 100/100 (the "(relay)" rows are marked in the report).
- Register id present in `sources/sources.md`: 100/100, including REG-901. The reading-guide list (001, 002, 009, 017, 018, 019, 025/026, 029, 030, 031) names the correct instruments.
- Article check (every article number in a tag appears in the row's `article`, `notes`, `quote` or `instrument`): all pass except H-01 "Art. 198", which is in the row's `in_force_confirmation` ("effective on promulgation (Art. 198)"). Pass.
- Note on method: `pillar1-mapping.csv` reuses row ids F-01 etc. and must be excluded from a trace. The report's tags point to the Plan 2 rows.
- The earlier gap (Art. 37(5), Art. 3(b)-(d) in no row) is closed.

## 3. N7 trimming: what was dropped (compared with commit f3f5ea0)

Checked: every section-6 question (1-20 and the "other items" block), every section-7 gap, every tagged fact in 2.2, and the hypotheses table.

- **Questions:** all 20 numbered questions and all six carried-over items are present. Wording is shortened. Two small losses: Q10 no longer asks about "scale" (only risk level), and Q9 asks "how long" instead of "what lead time" (equivalent).
- **Gaps:** all present (labour, risk annex, Lampiran OCR, DKI city, Keppres/Kepgub via DDTC only, NIB fees and lead times, Nutri-Level/excise/BPOM/precedents, Aug 2025 unrest, TKDN, boycott impact and ratings). "Policy-change list is partial" now lives in the Policy-flux paragraph ("partial against the plan's full list").
- **Facts moved, not lost:** PBJT 10%, IDR 42m exclusion, CIT, withholding, treaty rates, BPJPH tariffs, 800k fee and halal maxima now appear only in the 2.0b handoff table (tagged). The duplicate bullets in 2.2 were removed. Acceptable.
- **Dropped items (minor):**
  - **D1. Art. 197 in the Kepkaban row.** The F13 fix ("Art. 197 revokes PP 39/2021") is gone from section 2.1; the row now says only "In force via PP 42/2024 Art. 196 if not conflicting; no replacement seen". This reverts an accepted V-P2b fix. Restore "(Art. 197 revokes PP 39/2021)".
  - **D2. "Control and brand risk" row** of the 2.0 comparison table (Analysis cells: most control / third-party burden / shared / weakest control). It is a plan criterion ("Control of brand and quality (qualitative, labelled analysis)"). The content survives only in 2.3 and 2.4 prose (not for route (c) or the licence column). Restore the row, labelled Analysis.
  - **D3. Three tags dropped in H2, H4, H5.** H2 no longer tags the pending Perpres (E-02) behind "new Perpres pending"; H4 no longer tags "Labelled non-halal items are allowed in principle" to H-05; H5 no longer tags E-02 (the Summary does). H-05 Art. 2(2) is a fact, so the sentence is now an untagged fact. Re-add `[H-05 · REG-009 · Art. 2(2)]` and `[E-02 · REG-007 · Keppres 38/2025]`.
  - D4 (cosmetic). Headline sentence "No amendment found, not 'confirmed none'" moved from the 2.1 table to section 8; fine.

## 4. Other small findings

| # | Location | Issue | Severity | Fix |
|---|---|---|---|---|
| R1 | CSV `notes` of E-06 and F-06 | Both notes say "added Art. 37(5) / Art. 3(b)-(d) from opened text, V-P2b" (the same sentence was pasted into each row). The E-06 `notes` then correctly describes only Art. 37(5), and F-06 only Art. 3(b)-(d), so the facts are right, but each row names the other row's article. | minor | Trim each note to its own article. |
| R2 | `quote` of E-06 and F-06 | The new articles (Art. 37(5); Art. 3(b)-(d), 26(1)-(5) scope phrases) are recorded in `article` and `notes` but have no entry in `quote`, unlike the other rows. | minor | Add the Indonesian phrases ("Sumber pembiayaan ... modal sendiri; pinjaman; laba ditanam kembali; agio saham"; "Pasal 3 huruf b sampai dengan huruf d") to `quote`. |
| R3 | Section 2.2 and 2.0 ("from opened text, V-P2b") | The tag cites a verifier code in place of a source. Now backed by an F-06 row and the PP 35/2024 text, so traceable. | cosmetic | Optional: drop "V-P2b" from the tag. |

## 5. Claims checked and results

| Claim | Source | Result |
|---|---|---|
| Art. 37(1)(c), 37(4)(a)-(e), 37(5)(a)-(d) of Permen 5/2025 | REG-001 PDF, pdftotext | MATCH |
| PP 35/2024 Art. 3(a)-(h), 26(1)-(6), 27 | JDIH Kemendag PDF, pdftotext, this session | MATCH |
| T-09 and T-15 qualifiers | rows read in full | MATCH |
| Kontan "22 Tahun 2006" and 71/2019 not mentioned | F-05 `amendment_check` | MATCH |
| H-11 articles 170(2), 170(7), 171(2)-(5) | H-11 row | MATCH |
| S-09 and S-11 period wording | rows (unchanged from V-P2b) | MATCH |

## 6. Fix list

1. D1 (restore Art. 197), D2 (restore the control and brand row), D3 (three tags).
2. R1 and R2 (row notes and quotes) in the same pass; optional R3.
3. Owner discretion: N7 length, N8 CHF rate source.

After these, a mechanical tag trace is enough; no source needs reopening.
