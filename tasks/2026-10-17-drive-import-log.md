# Google Drive import log (2026-10-17)

Source folder: https://drive.google.com/drive/folders/1ZdIT3RJRcRrjaVmce6j72oap86LNyeuV (ID 1ZdIT3RJRcRrjaVmce6j72oap86LNyeuV), listed with the Google Drive MCP tools. Goal of this import: add every data file or report that the student team (Tiago Reimann, Ana, Matthieu, Jonas, Paul Berkmann, Marius) added to the folder and that is not yet in the repo, and leave out everything owned by the CORSA founders (Samuel Leu, Joshua).

Result in one line: the folder holds the same 22 files as on 2026-10-16 (no new file, no file modified after its logged date). Two of them were only partly imported on 2026-10-16 (Markdown text without the DOCX); their DOCX files are added now. Everything else is skipped as "already imported" or "founder-owned".

## Method

- All subfolders were listed with `search_files` (`parentId = ...`), following every `nextPageToken` until none was returned. Folders with no files: 99-Musterordner, 06_Abnahme & Archiv, 2025, 3_Bildwelt_Mood_Stilrichtlinien, 1_Brandbook_Manual, 2_Logo, 02_Financial.
- Cross-checks: a search for files modified after 2026-10-16 (none inside the folder tree) and a search for files owned by the team accounts (nomatt03, alessianaclara, j.vuillaume2003) returned nothing outside the 22 files below.
- Ownership: the Drive MCP exposes only the `owner` field (plus permissions); it does not expose the uploader or `lastModifyingUser`. "Owner" below is therefore the Drive owner account. Account to person: `info@samotion.ch` = CORSA / Samuel's account (owns the client folder structure and the briefing files, excluded); `nomatt03@gmail.com` = Matthieu; `j.vuillaume2003@bluewin.ch` = Jonas (PDF byline "Jonas Vuillaume", README of the model "Note from Jonas"); `tiago.p.reimann@gmail.com` = Tiago; `alessianaclara@gmail.com` = presumably Ana (the Drive shows only the address; the Oakberry files name no author).
- "Already imported" means: listed in `tasks/2026-10-16-drive-import-log.md` on the unmerged branch `claude/great-ramanujan-mcp2e3` with the same Drive modified date. Those files are on that branch, **not on `main`**, and are not copied again here.
- DOCX to Markdown: `pandoc -f docx -t gfm --wrap=none`, plus the DOCX title paragraph (pandoc keeps it as metadata) as the first heading, plus a header naming the source file, Drive path, owner, modified date and stating that the DOCX is authoritative. The DOCX files were downloaded from Drive (public link of the file, size identical to the Drive `fileSize`) and checked with `unzip -t`.

## Inventory

Drive path is relative to the root folder. Dates are Drive `modifiedTime`.

| Drive path / name | Type | Modified | Owner (uploader not exposed) | Drive ID | Result | Repo path |
|---|---|---|---|---|---|---|
| 00_HSG Team / 01_Market Entry / 04_Economic / CORSA_CAGE_Economic_Matthieu.docx | docx | 2026-10-12 | Matthieu (nomatt03@gmail.com) | 11cfLz0F1wj-RHYXA2YTKT_wolnJHXp4H | **IMPORTED (this PR).** On 2026-10-16 only the text was imported (DOCX could not be saved); the DOCX is now added and the `.md` is regenerated from it | `research/internal/2026-10-12-corsa-cage-economic-matthieu.docx` + `.md` |
| ... / 02_Administrative / CORSA_CAGE_Administrative_Matthieu.docx | docx | 2026-10-12 | Matthieu (nomatt03@gmail.com) | 1e7_Ep7cJipVM6q81vbNa4Ep4VjqMGeIZ | **IMPORTED (this PR).** Same situation as the Economic file | `research/internal/2026-10-12-corsa-cage-administrative-matthieu.docx` + `.md` |
| 00_HSG Team / 01_Market Entry / 00_General Reports / 01_Customer Behaviour Report | pdf | 2026-10-08 | Tiago | 1uAr4etXsTLdhmsSsFtc_BUHURGU-89S2 | Already imported (branch only) | `research/internal/2026-10-08-customer-behaviour-report.pdf` + `.md` |
| ... / 00_General Reports / 02_Paul Report 1.pdf | pdf | 2026-10-09 | Tiago (author Paul) | 18JxuhiUvFkFfUbpgcgaheYzLw4QoTtXd | Already in repo on `main` as a duplicate (99.8% word match) | `research/internal/corsa-first-research-paul.pdf` + `.md` |
| ... / 00_General Reports / 03_Matthieu_Geography&Culture.docx | docx | 2026-10-12 | Matthieu | 1c3YJW8SaqdVbfooB3zCooXOKMIiZMpo1 | Already imported (branch only) | `research/internal/2026-10-12-matthieu-geography-culture.docx` + `.md` |
| ... / 00_General Reports / 01_Customer Behaviour Research Data / 01.1_Customer Behaviour Extended Data (pdf) | pdf | 2026-10-08 | Tiago | 1DYVKnasIy4UgD0hSHc_vgzD0qfy__cQ_ | Already imported (branch only) | `research/internal/2026-10-08-customer-behaviour-extended-data.pdf` |
| ... / 01_Customer Behaviour Research Data / 01.1_Customer Behaviour Extended Data (docx) | docx | 2026-10-08 | Tiago | 1FVEyfvfx8gxLXZia7gS2xujbSGNbcMhW | Already imported (branch only) | `research/internal/2026-10-08-customer-behaviour-extended-data.docx` + `.md` |
| ... / 04_Economic / CORSA_Economic_Matthieu2.docx | docx | 2026-10-15 | Matthieu | 1IHdj56L0pD4FV83I61vQFeqToA0PZCgw | Already imported (branch only) | `research/internal/2026-10-15-corsa-economic-matthieu2.docx` + `.md` |
| ... / 01_Culture / CORSA_CAGE_Culture_Matthieu.docx | docx | 2026-10-12 | Matthieu | 11JmnOW-KtT7L-oUWjJBfw_-Q5BnflXI1 | Already imported (branch only) | `research/internal/2026-10-12-corsa-cage-culture-matthieu.docx` + `.md` |
| ... / 01_Culture / CORSA_Culture_Matthieu2.docx | docx | 2026-10-15 | Matthieu | 1dNsMmh8z63ibm1E7Qtu2SQLir_B1qvvS | Already imported (branch only) | `research/internal/2026-10-15-corsa-culture-matthieu2.docx` + `.md` |
| ... / 02_Administrative / CORSA_Administrative_Matthieu2.docx | docx | 2026-10-15 | Matthieu | 1dkRPRlgrr-weRhlGgggSwDGPFOTHhN6p | Already imported (branch only) | `research/internal/2026-10-15-corsa-administrative-matthieu2.docx` + `.md` |
| ... / 03_Geographic / CORSA_CAGE_Geographic_Matthieu2.docx | docx | 2026-10-14 | Matthieu | 1lihPnNDYcJXwna-qiI9QohwVY1jsG2OR | Already imported (branch only) | `research/internal/2026-10-14-corsa-cage-geographic-matthieu2.docx` + `.md` |
| ... / 03_Geographic / CORSA_Geographic_Matthieu2.docx | docx | 2026-10-15 | Matthieu | 18OCJBy-1lPrsKr80UcpEo6uz8XXsIc9k | Already imported (branch only) | `research/internal/2026-10-15-corsa-geographic-matthieu2.docx` + `.md` |
| ... / 05_Benchmark / OAKBERRY_Benchmark_CORSA_locations.docx | docx | 2026-10-14 | alessianaclara@gmail.com (presumably Ana) | 17skV-9CcLBFDGL7bETXtvd_G4rKDGSyl | Already imported (branch only) | `research/internal/2026-10-14-oakberry-benchmark-corsa-locations.docx` + `.md` |
| ... / 05_Benchmark / OAKBERRY_Benchmark_Research1.docx | docx | 2026-10-14 | alessianaclara@gmail.com (presumably Ana) | 1znJw9qRQpQ4EDD37y8OyeLaORxI8ySaB | Already imported (branch only) | `research/internal/2026-10-14-oakberry-benchmark-research1.docx` + `.md` |
| 05_Finanzen / CORSA Finance overivew 09.10.pdf | pdf | 2026-10-09 | Jonas (j.vuillaume2003@bluewin.ch); sits in the client-owned folder 05_Finanzen | 1IZoyWb3PGopnR_hgIgj1ukJ0AVub9iwb | Already imported (branch only). Team file: the PDF is bylined "Jonas Vuillaume, 9 October 2026" | `research/internal/2026-10-09-corsa-finance-overview.pdf` + `.md` |
| 05_Finanzen / Jonas Playground / CORSA_Jakarta_Financial_Model_v0.5_1 - Copy.xlsx | xlsx | 2026-10-13 | Jonas (j.vuillaume2003@bluewin.ch) | 1Q-FbkLoMUwUo3V1VtqG7DAfJwPESJaAV | Already imported (branch only). Team file: Jonas's folder, README "Note from Jonas" | `data/raw/2026-10-13-corsa-jakarta-financial-model-v0-5.xlsx`, `.md`, `...-csv/` |
| 02_Briefing & Kommunikation / CAPSTONE X CORSA SCOPE 2026 .docx | docx | 2026-10-01 | Samuel's account (info@samotion.ch) | 1iikE3TTc9XWrNvsShiZzP83aR7qfYt-- | SKIPPED: founder-owned (also a duplicate of `docs/scope/2026-capstone-x-corsa-scope`, already on `main`) | - |
| 02_Briefing & Kommunikation / CORSA Jakarta: Market Entry, Business Case & 90-Day Execution Roadmap | Google Doc | 2026-09-22 | Samuel's account (info@samotion.ch) | 1bGBbUL5jyRkpFRlFPMFvpTQin3iANcjI9cHYAdFrhFw | SKIPPED: founder-owned. Note: the 2026-10-16 import put it on the unmerged branch as `docs/scope/2026-09-22-corsa-jakarta-market-entry-roadmap-scope-v1.*` | - |
| 02_Briefing & Kommunikation / CORSA x HSG Capstone Project | Google Doc | 2026-08-13 | Samuel's account (info@samotion.ch) | 1VQG-li_7HU_dVt_bvZYwT8qtxsyZM0qBY5uF8RmO0NY | SKIPPED: founder-owned. Note: on the unmerged branch as `docs/scope/2026-08-13-corsa-x-hsg-capstone-project-execution-blueprint.*` | - |
| 02_Briefing & Kommunikation / Anfrage Capstone X CORSA | Google Doc | 2026-07-20 | Samuel's account (info@samotion.ch) | 1GrxAhaxNn1QfVjACY_GokhwekuvJsTZPJ_029e-crZI | SKIPPED: founder-owned. Note: on the unmerged branch as `docs/scope/2026-07-20-anfrage-capstone-x-corsa.*` | - |
| 01_Angebote & Verträge / capstone-praxispartner (2).pdf | pdf | 2026-10-01 | Samuel's account (info@samotion.ch) | 1UBYBbq0CVdEZE61ZhP57iAWr0SHXF5Qs | SKIPPED: founder-owned. Note: on the unmerged branch as `docs/scope/2026-10-01-capstone-praxispartner.*` | - |

22 files found: 2 imported now, 15 team files already imported on the unmerged branch (or, for Paul Report 1, already on `main`), 5 founder-owned files skipped. No Joshua-owned file was found. No file has ambiguous ownership.

## Verification (2026-10-17)

Each new `.md` was compared with its DOCX (all text from `word/document.xml`, footnotes, headers and footers, ordered word-sequence coverage and a bag-of-words check, plus every number):

- `2026-10-12-corsa-cage-economic-matthieu.md`: ordered coverage 99.8% of 1,220 source words; 2 words not matched (the title line break and the page number "1" from the DOCX footer); all numbers present; last body sentence present.
- `2026-10-12-corsa-cage-administrative-matthieu.md`: ordered coverage 99.9% of 946 source words; 1 word not matched (title line break); all numbers present; last sentence present.
- The two DOCX files open (`unzip -t` clean) and have exactly the Drive `fileSize` (34,789 and 23,990 bytes).
- The body text of the new `.md` files is word-for-word the same as the text-only `.md` files on the unmerged branch (the differences are only the header and `<u>` underline tags around links), so the branch's stopgap versions were complete.
- Not done: no independent verifier agent; this is a copy of team documents, not new research, so no source or fact checking.

## Merge note

`claude/great-ramanujan-mcp2e3` contains `.md` files at the same two paths (text-only versions). If both branches are merged, git reports an add/add conflict on those two `.md` files; take the version from this import, which also has the DOCX next to it.
