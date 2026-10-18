# Run 4 label fixes (W-LBL, 2026-10-17)

Scope: 11 open label rows from `tasks/2026-10-17-main-session-audit.md`. Only label, geography, base or date cells changed; no figure changed. Each row's `notes` got an 'Audit follow-up (2026-10-17)' entry. Sources reopened with curl and a Chrome user agent through the proxy (all HTTP 200). Validity: every edited CSV re-parsed with the python csv module; a diff against backups shows only the 11 target rows changed.

| Row | File | Issue | Old cell | New cell | Source reopened |
|---|---|---|---|---|---|
| P1C4-16 | data/processed/demand/wheat-foodservice.csv | `trigger_or_metric` label | Contribution of rice vs instant noodles vs bread to the food poverty line, urban vs rural (BPS, Susenas September 2025) | Contribution of rice vs instant noodles vs bread to the overall poverty line (garis kemiskinan, not a separate food poverty line), urban vs rural (BPS, Susenas September 2025) | Y |
| P1C4-16 | data/processed/demand/wheat-foodservice.csv | `ref_period` label | Susenas September 2025 (published 4 Mar 2026) | Susenas September 2025 (BPS release 5 Feb 2026; GoodStats relay page dated 4 Mar 2026) | Y |
| P3PB-06 | data/processed/price-ladder.csv | `geography` label | J | not stated (page names no city or outlet; brand-wide) | Y |
| P3PB-27 | data/processed/price-ladder.csv | `trigger_or_metric` label | menu price, range_premium_italian_main | menu price, range_european_modern_menu | Y |
| P3PB-27 | data/processed/price-ladder.csv | `item_class` label | range_premium_italian_main | range_european_modern_menu | Y |
| UA-N12 | data/processed/plan4-media-by-age.csv | `base_n` label | 8,700 (MoE +-1.1%) | 8,700 = whole APJII 2025 sample (MoE +-1.1%); Millennial subgroup n not printed | Y |
| UA-N67 | data/processed/plan4-media-by-age.csv | `base_n` label | 995 (Jakpat, 2-7 Sep 2025; young respondents) | 995 respondents per the GoodStats page (Jakpat, 2-7 Sep 2025, eight urban areas of Java); base for the 33% itself unconfirmed (a different Databoks page gives 955 narrowed to 769) | Y |
| Q8-001 | data/processed/plan4-origin-boycott.csv | `trigger_or_metric` label | Mandalika MotoGP total spectators (official count; minister statement 142,000 merged) | Mandalika MotoGP total spectators: 140,324 per Polri (repeating the organiser count, not an official Polri count); minister statement of about 142,000 noted separately | Y |
| Q8-003 | data/processed/plan4-origin-boycott.csv | `ref_period` label | Oct 2024; Oct 2023 (Databoks 2025-10-06) | Sep 2024 (race 27-29 Sep 2024); Oct 2023 (Databoks 2025-10-06) | Y |
| Q8-003 | data/processed/plan4-origin-boycott.csv | `geography` label | N | Lombok, NTB (single event; neither Jakarta nor national) | Y |
| H-04 | data/processed/2026-10-p2-entry-requirements.csv | `article` label | n/a (press statement); basis UU 33/2014 and PP 42/2024 | n/a (press statement); the BPJPH page cites UU 33/2014 only; PP 42/2024 is not named on the page (PP 42/2024 is the general implementing regulation, cited from other rows) | Y |
| P4W9-29 | data/processed/plan4-age-splits.csv | `question` label | A1 eating-out / A7 delivery | A1 eating-out (takeout is not delivery; not an A7 row) | Y |
| P4W9-29 | data/processed/plan4-age-splits.csv | `population` label | Indonesian online adults 18+, nationally representative of the online population | Indonesian online adults 18+ (weighting by gender, age, SES class and region is from the YouGov original per notes; representativeness is not stated on the relay page) | Y |
| P4W4-06 | data/processed/plan4-health.csv | `population` label | Indonesian consumers | Online adult consumers who are grocery/health shoppers per NIQ survey (adults interviewed online, Jan-Feb 2025); Indonesia n not printed | Y |
| P4W4-06 | data/processed/plan4-health.csv | `ref_period` label | 2025 survey (release 2025-07-08) | Fieldwork Jan-Feb 2025; release 2025-07-08 | Y |
| P1C2-03 | data/processed/demand/middle-class-income.csv | `trigger_or_metric` label | Upper class (>17x poverty line) population | Upper class (>17x poverty line, Mandiri Institute classification) population | Y |
| P1C2-03 | data/processed/demand/middle-class-income.csv | `base_n` label | national population (Susenas) | national population (BPS Susenas data as classified by Mandiri Institute; Susenas base not printed on the relay page) | Y |

## Caveats
- Q8-003: the 27-29 Sep 2024 race dates and P4W4-06 'grocery shoppers' wording come from the audit; the reopened Databoks and NIQ pages do not print them.
- UA-N67: the Databoks page with 955 narrowed to 769 was not reopened in this run; the base of the 33% stays unconfirmed.
- P1C4-16: the BPS release date (5 Feb 2026) is not on the GoodStats page; it is in the register entry DEM-058.
- H-04, P1C2-03: the reopened pages simply lack the cited item (PP 42/2024; the >17x definition); no outside confirmation was searched.
- No row was left unresolved.
