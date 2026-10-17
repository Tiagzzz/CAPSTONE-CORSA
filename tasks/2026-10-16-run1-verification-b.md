# Run 1 verification B (V-B): plan4-novelty.csv and plan4-health.csv

Verifier V-B, 2026-10-16. Method: WebFetch to pwc.com failed (DNS ENOTFOUND, host blocked), so every row was checked by my own WebSearch with wording different from the workers'. Search tool returns model-written summaries of result pages; quotes below are as returned. No data file was edited.

Queries used (Q-codes):
- Q1: Indonesian-language query on "14 persen responden laki-laki ... 29 persen ... sebulan sekali" (Populix)
- Q2: Populix laporan milenial Gen Z kuliner kekinian Agustus 2025 survei 1.100 responden ... perempuan 30%
- Q3: YouGov Indonesia pulse chasers 51% regret ... need-based 52%
- Q4: YouGov Indonesia shopping personality early adopters 7% trend 7% impulse buyers 12% need-based 52% September 2024
- Q5: PwC Voice of the Consumer 2025 Indonesia 48% willing to pay more nutrition 19% pay 20% more
- Q6: NielsenIQ Indonesia health wellness 2025 medical specialist 77% ... 48% 65%
- Q7: NIQ Indonesia 2025 "take active steps" health 46% medical specialists 77%
- Q8: PwC VoC 2025 Indonesia 72% additives 71% ultra-processed 50% economic instability
- Q9: PwC VoC 2026 Indonesia 503 respondents 59% / 51% (English), plus Indonesian-language variant and a global-report variant
- Q10: Mercu Buana Jurnal MIX 2025 viral marketing FOMO ... 209 responden
- Q11: RANS Nusantara Hebat tutup 28 Februari 2025 diresmikan 30 Maret 2024 BSD

## Verification table

| file | row_id | claim | worker value | verdict | evidence | notes |
| --- | --- | --- | --- | --- | --- | --- |
| novelty | P4W3-01 | Male respondents who try every new food trend | 14% of male respondents | CONFIRMED | Q1, Q2. Populix survey, n=1,100 Millennials/Gen Z, Feb 2025; reported by mediaasuransinews.co.id and indotelko.com/read/1755180339; coverage dated about Aug 2025 (quote dated 16 Aug 2025) | Populix original (premium) not seen; both outlets are republishers. Date >= 2024-10-16. Tier 3 OK for Populix; republisher outlets are not independent of each other, so confirmation is of the figure as published, not of the source data. Male base n not seen. |
| novelty | P4W3-02 | Male respondents exploring new flavours at least monthly | 29% of male respondents | CONFIRMED | Q1, Q2 as above | Same caveats. |
| novelty | P4W3-03 | Women trying new food due to social-media trend | 30% (about) of female respondents | CONFIRMED | Q1 returned "sekitar 30 persen responden perempuan ... tertarik pada tren di media sosial". Q2 did not surface the 30% figure | Weakest Populix row: seen in one of two searches only. Keep as provisional and keep "sekitar". |
| novelty | P4W3-04 | Self-identified early adopters | 7% of Indonesians | CONFIRMED | Q3, Q4. YouGov Surveys, fielded 26-30 Sep 2024; YouGov original article (yougov.com/articles/50874) in results; Marketech APAC dated 19 Nov 2024; Campaign Asia | Date OK (Nov 2024). Fieldwork was Sep 2024, so ref_period should say "fieldwork 26-30 Sep 2024, published Nov 2024". Sample n not seen. |
| novelty | P4W3-05 | Trend-driven shoppers | 7% | CONFIRMED | Q4, Marketech APAC | As above. |
| novelty | P4W3-06 | Impulse buyers | 12% | CONFIRMED | Q4, Marketech APAC | As above. Gender split exists (men 13%, women 10%) if wanted. |
| novelty | P4W3-07 | Pulse chasers regretting trend/impulse purchases past 12 months | 51% of pulse chasers | CONFIRMED | Q3, Q4. Campaign Asia and datawrapper chart "51% of pulse chasers in Indonesia often regret..." | As above. |
| novelty | P4W3-08 | Need-based shoppers | 52% of Indonesians | CONFIRMED | Q4. Marketech APAC headline "more than half ... need based shoppers", 52% stated; Q3 found headline only | 52% appeared in one search with explicit number. Men 49%, women 54%. |
| novelty | P4W3-09 | Sample size, Jakarta Gen Z viral marketing/FoMO study | 209 | CONFIRMED | Q10. publikasi.mercubuana.ac.id/index.php/Jurnal_Mix/article/view/32233; MIX: Jurnal Ilmiah Manajemen 15(3), 2025; Khalid, De Silva, Maulana, Utami; 209 Gen Z students, purposive snowball, PLS-SEM | Month of publication not seen (worker says Oct 2025), but vol. 15(3) 2025 is after the cutoff. This is a sample size, not a behavioural finding; consider moving to notes. |
| novelty | P4W3-10 | Months of operation of RANS Nusantara Hebat before closure | 11 months | DERIVED | Q11. CNN Indonesia 25 Feb 2025 (cnnindonesia.com/ekonomi/20250225184612-...), Okezone 26 Feb 2025, Emitennews: opened 30 Mar 2024 (soft opening 22 Mar 2024), operations stop 28 Feb 2025 | Date arithmetic by the worker, not a sourced figure. Move to notes. Dates themselves are confirmed. Note several outlets call the closure "sementara" (temporary), pending a new concept; the snippet says "resmi menghentikan operasionalnya". Do not state it as a permanent closure. |
| health | P4W4-01 | WTP over 10% more for enhanced-nutrition food | 48% | CONFIRMED | Q5, Q6. NIQ press release 2025-07-08 (nielseniq.com/global/en/news-center/2025/niq-indonesian-consumers-reassess-health-priorities-...), Global State of Health & Wellness 2025, fieldwork Jan-Feb 2025, 19 countries | Note: Q5's summary says "over 10%", as the worker has it. Indonesia n not seen. Tier 3 OK. Date OK. |
| health | P4W4-02 | WTP 20% more | 19% | CONFIRMED | Q5, NIQ release | |
| health | P4W4-03 | Take proactive steps for health | 46% | CONFIRMED | Q7, NIQ release: "Nearly half (46%) report taking proactive steps..." | Worker snippet says "active steps"; the release wording is "proactive". Fix the quote. |
| health | P4W4-04 | Healthy nutrition more important than 5 years ago | 65% | CONFIRMED | Q6, NIQ release | Wording is "has become more important now than five years ago". |
| health | P4W4-05 | Barrier: healthy options hard to find | 48% | CONFIRMED | Q6, NIQ release ("difficulty accessing healthy alternatives (48%)") | |
| health | P4W4-06 | Barrier: high costs | 43% | CONFIRMED | Q6, NIQ release | |
| health | P4W4-07 | Barrier: doubts products work | 43% | CONFIRMED | Q6, NIQ release | |
| health | P4W4-08 | Medical specialist recommendation as top influence on wellness purchases | 77% | CONFIRMED | Q7, NIQ release: "rank medical health specialist recommendations (77%) as the top influence on wellness-related purchases", then product information 69%, ability to ask experts 65%. Q6 did not surface it | One search only. Unit is share rating it an influence, not a share who buy on advice. |
| health | P4W4-09 | Concern about additives and preservatives | 72% | CONFIRMED | Q8. PwC Indonesia press release 8 Jul 2025 (pwc.com/id/en/media-centre/press-release/2025/english/economic-instability-...), VoC 2025, 21,075 consumers in 28 territories | Figures are Indonesia-specific (APAC 62% for additives, per a secondary source). Fieldwork period Jan-Feb 2025 not re-verified; not shown in my result. Indonesia n not seen. |
| health | P4W4-10 | Worry about ultra-processed products | 71% | CONFIRMED | Q8, same release | APAC 67%, global figures higher or lower not checked. |
| health | P4W4-11 | Buy less or trade down due to economic instability | 50% | CONFIRMED | Q5, Q8, same release; global 44%, APAC 42% | |
| health | P4W4-12 | Primary health goal: longer and healthier life | 59% | CONFIRMED | Q9 (Indonesian-language query). PwC Indonesia press release dated 3 Sep 2026 (pwc.com/id/en/media-centre/press-release/2026/english/voice-of-the-consumer-2026-survey.html); VoC 2026: 21,808 consumers, 27 territories, Indonesia n=503, fieldwork Feb-Mar 2026 | Indonesia-specificity is not fully proven. The English quote reads "59% of consumers" and the global-report query could not find 59% on the global pages (which would favour an Indonesia-only figure). The attribution rests on the Indonesia press release. Keep flagged provisional. The Indonesia PDF could not be opened. |
| health | P4W4-13 | Prioritise reducing stress and improving mental wellbeing | 51% | CONFIRMED | Q9, same release | Same Indonesia-specificity caveat as P4W4-12. |

## Summary

| verdict | count | row_ids |
| --- | --- | --- |
| CONFIRMED | 22 | P4W3-01 to P4W3-09; P4W4-01 to P4W4-13 |
| CORRECTED | 0 | none (wording fixes only: P4W3-04 to -08 ref period should read "fieldwork 26-30 Sep 2024, published Nov 2024"; P4W4-03 quote should read "proactive") |
| UNCONFIRMED | 0 | none |
| DATE-FAIL | 0 | none |
| TIER-FAIL | 0 | none |
| DERIVED | 1 | P4W3-10 |

Row_ids to drop from the data CSVs: none for verification failure.
Row_ids to move to notes: P4W3-10 (derived: 11 months). Optional: P4W3-09 (a sample size, not a behaviour figure).

Row_ids to keep flagged as weakly confirmed (do not upgrade beyond provisional): P4W3-03 (seen in one of two searches), P4W4-08 (one search), P4W4-12 and P4W4-13 (Indonesia base not proven).

## Systemic issues

1. All 19 non-derived provisional rows rest on search-result text, not on opened pages. Confirmation is of the published figure, not of the underlying dataset; hosts remain blocked (pwc.com gives DNS ENOTFOUND).
2. The Populix rows (P4W3-01 to -03) come only from republishers (mediaasuransinews.co.id, indotelko.com). Both carry the same press text, so the "independent" confirmation is weak. Reliability tier 3 applies to Populix, not to the republishers.
3. Base n for the Indonesia subsamples is missing for YouGov, NIQ and PwC 2025 rows; male/female bases in the Populix rows are missing.
4. Reference period vs publication date: YouGov rows were published Nov 2024 with fieldwork Sep 2024; the NIQ and PwC 2025 rows were released 2025-07-08 with fieldwork Jan-Feb 2025. Workers should record both.
5. The search summaries are model-written and sometimes disagree between runs (the Populix 30% figure; the 52% figure). Re-check these four rows when hosts open.
