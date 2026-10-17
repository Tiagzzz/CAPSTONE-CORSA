# Main-session reliability audit of runs 1 to 3 (2026-10-17)

Independent check of the research on `claude/great-ramanujan-mcp2e3`, requested by the Product Owner. Done from a separate session that had not produced the data.

## Method

1. **Mechanical checks on all 614 CSV rows** (`data/processed/**`):
   - verification labels;
   - tiers and geography codes;
   - register ids that resolve in `sources/sources.md`;
   - value present in the row's own quote.
2. **HTTP check of all 276 register URLs** (curl with a browser user agent, redirects followed, no bot-challenge bypass).
3. **Random re-check of 54 rows** (stratified across the 20 files, weighted to price, legal, tax and competitor files; BLOCKED rows excluded). Four independent checkers re-opened every cited source and compared value, unit, period, base and geography.
   - Limitation: the checkers saw value, period, base, population, geography and quote, but **not** the `notes`, `in_force_confirmation`, `amendment_check` and `gaps` columns. Several flags below were already handled there; each was re-read against the full row before any change.
4. **Traceability check** of `reports/2026-10-17-purchase-triggers-and-channels.md` against the CSVs.

## Results

| Check | Result |
| --- | --- |
| Rows | 614: 228 VERIFIED-OPENED (original), 299 (relay), 47 CORRECTED-OPENED, 19 BLOCKED, 21 matrix cells (no label) |
| Row tiers (first register id) | tier 1: 121, tier 2: 59, tier 3: 413 |
| Geography | about half N (national); 425 rows have age-fit D (no age split) |
| Register URLs | 251 of 276 return HTTP 200; 21 return 403 (Bisnis.com, PwC, IDX bot protection) and 4 time out (jdih.kemendag.go.id, bi.go.id); no 404 |
| 54-row re-check | 37 MATCH, 17 MINOR, **0 WRONG**, 0 unreachable |
| Report (version ad3e996) | all 132 cited rows exist and match, no BLOCKED row used; "facts pointing the other way" omitted seven verified downside rows (fixed, see below) |

## The 17 MINOR findings

The figures are correct in all 17; the issues are labels, framing or dates.

**Fixed in this commit**
- **H-03:** the free halal scheme was worded in the present tense. The BPJPH FAQ, reopened, says SEHATI ran "Sepanjang tahun 2025 selama kuota masih tersedia" (code SEHATI25), so the wording is now past tense.
- **H-12:** the article range was widened to PP 42/2024 Art. 147-154, the section Registrasi Sertifikat Halal Luar Negeri, after reading the PP text. Art. 151(2) leaves the fee to other rules, and the Rp800,000 fee comes from the BPJPH FAQ.

**Already handled in the row (no change)**
- **T-06:** the finding already says the 20% cut expired and is not a standing relief. T-07 holds the March 2026 cut.
- **P1C1-F04:** a 2024 row. The 2025 food share (34.96%) is P1C1-F03 and the 2025 total spend is P1C1-F05.
- **P4W5-04:** the notes already say "48 countries" may refer only to the roughly 1,000 foreign runners.
- **P4W9-21:** n, cities and fieldwork come from the IMGR PDF methodology page cited in the notes, not from the GoodStats page.

**Open (figures correct; fix the label when the row is used)**
- **P1C4-16:** labelled "food poverty line", but the source is the overall poverty line. "Published 4 Mar 2026" is GoodStats' date; BPS released it on 5 Feb 2026.
- **P3PB-06:** coded geography J, but the page names no city or outlet.
- **P3PB-27:** class `premium_italian_main` overreaches. detikFood calls Bastian "konsep Eropa modern", and the range runs from starter to steak.
- **UA-N12:** base_n 8,700 is the whole APJII sample; the Millennial subgroup base is not printed.
- **UA-N67:** the eight-city base comes from a different Databoks page (955 respondents narrowed to 769). The base for the 33% is unconfirmed.
- **Q8-001:** the Polri count (140,324) and the minister's figure (about 142,000) sit in one row, and Polri does not call its figure the organiser's count.
- **Q8-003:** ref_period should be Sep 2024 (race on 27-29 Sep 2024), not Oct 2024. It is a single Lombok event coded N.
- **H-04:** PP 42/2024, named in `article`, is not on the cited BPJPH page, which cites UU 33/2014.
- **P4W9-29:** "nationally representative of the online population" is not on the relay page. "Takeout" is coded under delivery.
- **P4W4-06:** the population is online adult grocery shoppers (fieldwork Jan-Feb 2025), not all consumers, and no Indonesia n is given.
- **P1C2-03:** the "more than 17x poverty line" definition and the Susenas base are Mandiri Institute's classification, confirmed only by other outlets.

**Also checked (MATCH rows, no change)**
- **P1C2-22:** the 2025 minimum wage. The 2026 UMP (Rp5,729,876) is its own row, P1C2-21.
- **F-05:** franchise experience conflict. Kontan (30 Jun 2025, REG-901) reports that Permendag 26/2025 revoked four Permendag, and 71/2019 is not one of them. A Tempo item said to report a revocation could not be opened. The point stays a lawyer question, and the evidence is added to `amendment_check`.

## Report fix

`reports/2026-10-17-purchase-triggers-and-channels.md`, "Assumptions most at risk": the paragraph now cites seven verified rows it had left out:
- P1C2-09: middle-class food consumption +0.9%;
- P1C2-10: middle-class-income workers 14.5% to 7.1%;
- P1C2-11: medium- and high-skilled real wages -1% and -2% a year;
- P1C2-33: middle savings index at its lowest since Oct 2023;
- P4W9-28: dining out among the categories Gen X+ cut;
- P4W9-29: Millennial retrenchment areas;
- Q6-006: MAPB nine-month sales -2.77%.

It also brings in the existing P4W9-16 and adds the August comparison to P1C2-20. The fix is applied on top of the cloud session's final version (1bc7cc3, whose own re-check had already changed the counts to 130 and softened the 21-40 wording). The summary counts (130 to 137 rows, N 90 to 97) and the Appendix are updated, and all 137 cited ids resolve in the CSVs and the Appendix.

## Not checked

- Relay rows were compared with the relay page only, not with the BPS, BI or IDX originals.
- The 19 BLOCKED rows were not re-checked.
- The gap analysis (`reports/2026-10-16-existing-research-gap-analysis.md`) and the imported team files were not checked.
