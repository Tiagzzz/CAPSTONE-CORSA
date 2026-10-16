# Plan: Markdown versions of all PDFs (2026-10-16)

**Goal:** Every PDF in the repo has a faithful Markdown version next to it (`same-name.md`). Agents read the `.md` instead of the PDF unless the owner says otherwise. Reorganized folder structure is kept.

## Acceptance criteria
1. Each of the 9 PDFs has a `.md` file with the same basename in the same folder.
2. Each `.md` starts with a header naming the source PDF, page count and conversion date, and notes that the PDF is authoritative.
3. Content is complete: no summarizing or omissions. Word count of the `.md` body is ≥ 90% of the `pdftotext` word count (page headers/footers/page numbers removed are the only allowed loss).
4. Structure is readable: headings, lists and tables converted to Markdown; figures noted as `[Figure: …]`.
5. A verifier spot-checks ≥ 5 passages per file against `pdftotext` output and confirms numbers, names and dates match exactly.
6. CLAUDE.md states the "read the .md version" rule.

## Work split (parallel workers, Sonnet: needs reliable long-text fidelity; Haiku risks dropping content)
- W1: `docs/scope/2026-capstone-x-corsa-scope.pdf`, `research/internal/*.pdf` (38 pp)
- W2: `meetings/2026-09-23-kickoff-meeting-recap.pdf`, `meetings/2026-10-01-meeting-3-recap.pdf` (72 pp)
- W3: `meetings/2026-10-05-meeting-4-recap.pdf`, `meetings/2026-10-05-meeting-4-recap-v2.pdf` (51 pp)
- W4: `meetings/2026-10-07-market-entry-meeting-recap.pdf`, `meetings/2026-10-12-meeting-5-recap.pdf` (47 pp)

## Verification
- V1 (Sonnet, independent of workers): checks criteria 1–5 for all 9 files and reports per-file pass/fail with word-count ratios and spot-check results.

## Deliverables
9 `.md` files, CLAUDE.md rule update, README update, commit + PR + merge.

## Result
Verifier V1: PASS on all criteria for all 9 files (word ratios 0.97–1.08; Paul brief 0.864 raw due to pdftotext number fragmentation, 1.14 on ≥3-letter words; timestamp lists identical in all 6 meeting files; rebuilt tables checked against page images; no discrepancies).
