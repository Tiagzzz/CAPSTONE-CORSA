# Environmental (PESTEL) scan, Jakarta/Indonesia: raw findings

Task W-ENV, run 4, Pillar 1. Accessed 2026-10-17 with `curl -sL` (browser User-Agent) through the agent proxy; no bot check bypassed. Dates are taken from page bodies. Structured rows: `data/processed/2026-10-pestel-environmental.csv` (ENV-001 to ENV-022). Sources: REG-045 to REG-056 and, after the audit follow-up, REG-131 to REG-135 in `sources/sources.md`.

Fact is separated from interpretation: the "Findings" sections are quotes and facts; "Reading" lines are analysis, not sourced.

## Source keys

| key | register | URL | printed date |
| --- | --- | --- | --- |
| ENV-S1 | REG-045 | https://www.bmkg.go.id/iklim/anomali-suhu-udara/anomali-suhu-udara-rata-rata-tahun-2025 | 6 February 2026 |
| ENV-S2 | REG-046 | https://bpbd.jakarta.go.id/berita/ZUgrczNHR29McHZMVmpncm5LcXVoZz09/update-info-terkini-genangan-23-januari-2026-s-d-pukul-12-00-wib | Jumat, 23 Januari 2026 |
| ENV-S3 | REG-047 | https://bnpb.go.id/berita/lebih-dari-1600-warga-jakarta-mengungsi-akibat-banjir-kebutuhan-terpenuhi-dengan-baik | 25 Jan 2026 13:30 WIB |
| ENV-S4 | REG-049 | https://lingkunganhidup.jakarta.go.id/uploads/images/galery/ringkasan%20eksekutif%20dikplhd%20jakarta%202025_20250918065722.pdf | "Tahun 2025" (no day) |
| ENV-S5 | REG-048 | https://dsda.jakarta.go.id/detail-artikel/penurunan-permukaan-tanah-jakarta-melambat-perlindungan-pesisir-terus-diperkuat/172 | 12 Juni 2026 |
| ENV-S6 | REG-050 | https://info3r.kemenlh.go.id/uploads/faq/1705915980_Permen%20LHK%20No.%2075%20Tahun%202019.pdf | 18 Oktober 2019 |
| ENV-S7 | REG-051 | https://jdih.kemenkoinfra.go.id/id/peraturan-menteri-lingkungan-hidup-dan-kehutanan-no-p75menlhksetjenkum1102019-tahun-2019 | record; promulgated 5 Desember 2019 |
| ENV-S8 | REG-052 | https://pasal.id/peraturan/pergub/pergub-prov-dki-jakarta-no-142-tahun-2019 | 27 and 31 Desember 2019 |
| ENV-S9 | REG-053 | https://www.esdm.go.id/id/media-center/arsip-berita/jaga-daya-beli-menteri-esdm-tarif-listrik-tidak-naik | Selasa, 30 Juni 2026 |
| ENV-S10 | REG-054, REG-055 | https://www.esdm.go.id/id/media-center/arsip-berita/jaga-stabilitas-awal-tahun-2026-pemerintah-putuskan-tarif-listrik-tidak-naik ; https://www.pln.co.id/pelanggan-id/tarif-tenaga-listrik-id/penyesuaian-tarif-id | 31 Desember 2025; PLN page undated |
| ENV-S12 | REG-131 | https://jdih.jakarta.go.id/dokumen/detail/3851/ (full text /link/download-fulltext/3851) | set 27 Dec 2019, promulgated 31 Dec 2019 |
| ENV-S13 | REG-132 | https://jdih.jakarta.go.id/dokumen/detail/1803/ | set 8 Dec 2021 |
| ENV-S14 | REG-135 | https://www.pln.co.id/webapi/media/file/webkorp/asset/1fa2814b-6ffd-459b-ac16-d46e515a0b3b.pdf | 1 July 2026 |
| ENV-S15 | REG-133, REG-134 | https://jdih.jakarta.go.id/link/download-fulltext/14173 ; /14172 | set 16 Oct 2024 ; 14 Oct 2024 |
| ENV-S11 | REG-056 | https://rmol.id/nusantara/read/2024/12/26/649963/tarif-air-pam-jaya-naik-mulai-1-januari | Kamis, 26 Desember 2024 |

## 1. Heat and climate (BMKG)

- "Berdasarkan data dari 115 stasiun pengamatan BMKG, suhu udara rata-rata periode 1991-2020 di Indonesia sebesar 26.7 °C dan suhu udara rata-rata tahun 2025 sebesar 27.05 °C, sehingga anomali suhu udara rata-rata tahun 2025 sebesar 0.38 °C." (ENV-S1)
- "...tahun 2025 menempati urutan keenam tahun terpanas di Indonesia dengan nilai anomali sebesar 0.38 °C." and most stations were cooler than in 2024. (ENV-S1)
- Reading: warm tropical baseline; no cooling trend implied. National figure only.

## 2. Flooding (BPBD DKI, BNPB, DLH)

- 23 Jan 2026, 12:00 WIB: "BPBD mencatat saat ini terdapat 143 RT dan 16 ruas jalan tergenang." Trigger: heavy rain Thursday 22 Jan 2026. Jakarta Barat 40 RT and Jakarta Selatan 66 RT seen on the opened page. (ENV-S2)
- BNPB 25 Jan 2026: more than 1,600 displaced; BPBD: "20 kelurahan di 6 kecamatan. Sedikitnya 585 Kepala Keluarga (KK) atau 1.623 jiwa dan 14 ruas jalan terdampak." (ENV-S3)
- DIKPLHD (data 2024): "Tercatat 500 kejadian bencana banjir"; 1,942 displaced in 2024. (ENV-S4)
- Search summaries mention later 2026 events (March: 48 RT; May: 115 RT per media). Not opened at BPBD level, so not stored.
- Reading: flooding is a recurring rainy-season risk; counts are momentary.

## 3. Air quality

- DLH DKI: IKU 2024 = 72.59, category "Baik"; "PM2.5 dan NO₂ tetap memerlukan perhatian". 12 million+ motor vehicles in 2024. Pneumonia up to 40% on the prior year (document statement). (ENV-S4)
- GAP: annual PM2.5 mean and unhealthy-day counts. IQAir (tier 3 use only) returned HTTP 403 (blocked). udara.jakarta.go.id returned 200 but is a live portal; not parsed.

## 4. Land subsidence

- DSDA DKI (12 Jun 2026): about 4 cm/year average (2023, 255 GPS points); Muara Baru about 10 cm/year; Muara Angke about 7 (2023) to about 4.5 cm/year (2026); trend slowing in central Jakarta. (ENV-S5)

## 5. Waste and packaging rules

- Waste (DIKPLHD, 2024): 8,688 t/day generated; about 5,858 t/day transported. (ENV-S4)
- Permen LHK P.75/2019: Art. 2: roadmap 2020-2029, "target pengurangan sampah oleh Produsen sebesar 30%... di tahun 2029". Art. 3(3): "rumah makan; kafe; restoran; jasa boga; dan hotel". Annex note b: straws, foam food containers, single-use plastic bags, foam "dilarang digunakan, berlaku efektif 1 Januari 2030"; note c: earlier local bans must be obeyed. In force per JDIH record ("Berlaku", BN 2019 No. 1545). The 2030 ban is not yet in force. (ENV-S6, ENV-S7)
- Pergub DKI 142/2019 (text via Pasal.id, tier 3 relay): Art. 5(2) managers "dilarang menggunakan Kantong Belanja Plastik Sekali Pakai"; Art. 6(1)(a) mall managers must impose the duty on all tenants; Art. 7 allows plastic packaging bags only for unwrapped food, ending when an alternative exists; Art. 22(2) sanctions up to licence revocation; Art. 30 applies 6 months after promulgation (31 Dec 2019). Status "Berlaku" on Pasal.id. (ENV-S8)
- Reading: a mall-based cafe is bound via its mall manager; stand-alone outlets and takeaway cups are not addressed in the articles read.
- Nothing found or opened on a statutory EPR scheme beyond P.75, or on Jakarta cup/straw rules (gap ENV-018).

## 6. Energy and water cost

- ESDM 30 Jun 2026: Q3 2026 tariff for 13 non-subsidised groups "tidak mengalami kenaikan", although "akumulasi perubahan parameter tersebut seharusnya menyebabkan kenaikan tarif listrik"; adjustment every three months under Permen ESDM 7/2024. Valid Jul-Sep 2026; Q4 not found. (ENV-S9, ENV-S10)
- Water: Kepgub 730/2024 under Pergub 37/2024, tariffs from January 2025 after 17 years unchanged (tier 3 relay). No Rp/m3 taken. (ENV-S11)

## Blocked or failed hosts (not bypassed)

| host | result |
| --- | --- |
| peraturan.bpk.go.id | HTTP 403, Cloudflare "Just a moment" challenge |
| iqair.com | HTTP 403 |
| ekonomi.bisnis.com | HTTP 403 |
| dibi.bnpb.go.id, jdih.menlhk.go.id, peraturan.go.id, info3r.menlhk.go.id, ppid.menlhk.go.id, ditppu.menlhk.go.id, pam-jaya.co.id, www.bi.go.id | no connection (curl code 000) |
| www.pln.co.id (tariff PDF) | proxy tunnel closed mid-exchange; the HTML page opened |
| jdih.jakarta.go.id (search path), pasal.id P.75 path | HTTP 404 |

Search-summary only (not opened, not stored as data): BRIN and Kemenko subsidence ranges, Fortune IDN B-2 tariff Rp1,444.70/kWh, Detik 1 July 2020 effective date, hukumonline Pergub 102/2021 and Perda 3/2013 notes, K III water tariff Rp21,500-23,000 per m3.

## Audit follow-up (2026-10-17)

- JDIH Jakarta is reachable: the search form works as `https://jdih.jakarta.go.id/pencarianHome?kata_pencarian=<title>` (the earlier "404, not usable" note was for another path). Opened: Pergub 142/2019 (record 3851, status "Berlaku", no amending relation listed; full text read, quotes in ENV-012/013 checked against it, Art. 6(2), 24, 29 added), Pergub 102/2021 (record 1803; waste duties of area managers and companies; no cup or straw rule), Kepgub 730/2024 (record 14173; image-only PDF, Annex II tariff read visually) and Pergub 37/2024 (record 14172, record page only).
- PLN tariff PDF for Jul-Sep 2026 downloaded (image only) and read visually: B-2/TR Rp1,444.70 per kWh; expired 30 Sep 2026; Q4 2026 tariff still not found.
- ENV-004 relabelled: 1,623 is BPBD's count of people affected (terdampak); the displaced figure is the BNPB headline "more than 1,600".
- Still gaps: ENV-016 (PM2.5), ENV-017 (Jakarta heat), ENV-021 (flood losses; dibi.bnpb.go.id unreachable), cup and straw rule (ENV-018, partial), Q4 tariff.
- Search-listing only (not opened): Pergub 111/2021 (fiscal incentive for eco-friendly bags), Pergub 55/2021, Perda 3/2013, Ingub 5/2026.
