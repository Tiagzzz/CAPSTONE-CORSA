# Wave 5 verification (appendix and phase-2 plan)

| Item | Result | Note | Exact fix |
|---|---|---|---|
| A: columns, team files, model sheets | PASS | A.1 has ID/title/publisher/tier/date/URL/sections/claims (123 rows = header count); A.3 lists 3 team files; A.4 lists 12 model sheets | none |
| A: sample of 5 ids cited (DEM-046, BEH-043, DEM-020, REG-121, REG-030) | PASS | all in claim ledger source_ids (report text carries no ids; ledger is the citation record) | none |
| B: coverage (16 NC/UNREACH, 47 if_used, 32 dropped, BLOCKED) | PASS | all 16 and 47 ids present; B.4 has 32 rows; B.3 has 33 BLOCKED/GAP rows; summary counts reconcile with section counts | none |
| B: valid codes | PASS | every row carries one of the spec codes plus UNVERIFIED-NOT-USED (added, defined in table); GAP appears only as Status, not as code | none |
| B: sample reasons (8) | FAIL (1 of 8) | REG-037, BEH-074, CMP-003, REG-055 CONDENSED-OUT: id found in the named long reports. CAGE-034, R3-REG-128, R3-S11 accurate. REG-117 DUPLICATE reason wrong: "Same Zurich table as REG-116", but REG-116 is the Jakarta station (96749); REG-117 is Zurich (06660), a different table | In `analysis/appendix_reason_overrides.json` change REG-117 to code OFF-SCOPE (or CONDENSED-OUT), reason "Zurich companion table to REG-116 (Jakarta); not needed for the report's questions (CAGE climate)"; rerun verify_report.py. Also fix the DUPLICATE count 4 -> 3 and B.4 DUPLICATE unaffected (script regenerates) |
| No HSG staff names | PASS | no hits for Bergmann, Heiko, Rflect, HSG staff, course credit, grading in appendix | none |
| Part C placeholder | PASS | header, intro and empty table at ~line 573 | none |
| Phase-2 plan covers spec 7 bullet | PASS | run_all on new model, diff, register with tier, batch pre-verification, map to claims, rerun, v1.1 changelog all present | none |
| Plan commands and paths exist | PASS | run_all.py --help has --model-path, --skip-links; v0.6 xlsx, tasks/lessons.md, verify_report.py lines 317/326/736/~808 match | none |
| Plan numbers | FAIL (minor) | plan says 74 of 152 ledger rows depend on model_v0.6 and 6 team_unverified; ledger has 77 and 5 | In phase2-update-plan.md replace "74 of 152" with "77 of 152" and "6 ledger claims have `depends_on=team_unverified`" with "5" |
| Plan acceptance keys | FAIL (minor) | "words, unsourced, forbidden_hits" are not keys of verify_report_summary.json | Name the real keys: `word_counts`, `unsourced_numeric_statements_count`, `forbidden_string_hits_report` and `forbidden_string_hits_appendix` |
