# Ingest log (2026-10-18)

Files provided by Tiago on 2026-10-18, plus a check of the shared Google Drive folder (`1ZdIT3RJRcRrjaVmce6j72oap86LNyeuV`) for new team uploads.

## Inventory

| Source | Type | Provided / modified | Result | Repo path |
|---|---|---|---|---|
| Local file `CORSA_Jakarta_Financial_Model_v0.6.xlsx` (model by Jonas and Marius, per Tiago) | xlsx, 20 sheets | file saved 2026-10-18 13:03 UTC; README v0.6 note dated 16 Oct 2026 | Imported byte-identical. One CSV of cached values per sheet, plus an index with a completeness check | `data/raw/2026-10-18-corsa-jakarta-financial-model-v0-6.xlsx`, `.md`, `...-v0-6-csv/` (20 CSVs) |
| Local file `OAKBERRY_Benchmark.pdf` | pdf, 6 pages | printed from Word 2026-10-18 | Imported. A shortened, edited version of Ana's `2026-10-14-oakberry-benchmark-research1.docx` (98% of its words appear there), so it is kept as a new version, not a duplicate | `research/internal/2026-10-18-oakberry-benchmark.pdf` + `.md` |

## Drive check: new team uploads

- Searched files uploaded after 2026-10-14 (upload date, not modified date, because uploads keep their original modified date) that are not owned by Tiago. Found only Matthieu's five "Matthieu2"/CAGE files and Ana's two Oakberry documents, all already in the repo.
- **Paul: no files uploaded.** The only Paul file on the Drive is "02_Paul Report 1.pdf", uploaded by Tiago on 2026-10-09. It is already in the repo as `research/internal/corsa-first-research-paul.pdf`.
- No other CORSA, Jakarta or Oakberry file was created on the Drive after 2026-10-16. The two local files above are not on the Drive.

## Verification

- Workbook: `cmp` shows it is byte-identical to the source. All 20 sheets are exported in full. The completeness check is in the `.md`, with its figures read from the workbook by script.
- Oakberry `.md`: 100% word coverage against `pdftotext -layout` (1,327 words). The 11 PDF hyperlinks are listed at the end.

## Owner decisions recorded

- 2026-10-18: the scope's brief Singapore, Dubai and Hong Kong comparison is dropped. `reports/2026-10-17-pillar1-framework-outline.md` is updated so no agent works on it.
- Model v0.6 is not edited. Its 13-month P&L gap and the placeholder inputs are for Jonas and Marius (see the completeness check in the `.md`).
