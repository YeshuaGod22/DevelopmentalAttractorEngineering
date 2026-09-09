# Pass 3A–D — Mechanical effects surface

Descriptive only. Branch `0` excluded. Baselines are used only within the same collection (`C` or `C0`).

- Non-0 battery rows: **1211**
- Cell×item surfaces: **432**
- Within-collection contrasts: **127**

## Within-collection comparator availability

- `pilot1` → `C0`
- `raw2` → `C`
- `raw6` → `C`
- `raw7` → `C`

## Pilot matched category transitions

| rep | item | cold | treated | kind changed? | exact same? |
|---:|---|---|---|---|---|
| 1 | A1 | integer:50 | sentinel:ALWAYS | yes | no |
| 1 | E01 | integer:20 | integer:23 | no | no |
| 1 | N4 | integer:38 | refusal:None | yes | no |
| 1 | N9 | integer:8 | refusal:None | yes | no |
| 2 | A1 | sentinel:ALWAYS | sentinel:NEVER | no | no |
| 2 | E01 | integer:25 | integer:25 | no | yes |
| 2 | N4 | integer:32 | integer:25 | no | no |
| 2 | N9 | integer:20 | refusal:None | yes | no |

## Largest absolute median differences (descriptive)

- `raw7 | FQ vs C | D1`: median 15.0 → 52 (Δ +37); n 10→3
- `raw2 | Ha vs C | N9`: median 25 → 58 (Δ +33); n 3→1
- `raw7 | AQ vs C | N1`: median 68.0 → 38 (Δ -30); n 10→3
- `raw7 | ASQ vs C | C2`: median 72.0 → 42 (Δ -30); n 10→3
- `raw7 | ASQ vs C | D1`: median 15.0 → 42 (Δ +27); n 10→3
- `raw7 | ASQ vs C | N1`: median 68.0 → 42 (Δ -26); n 10→3
- `raw7 | FQ vs C | N1`: median 68.0 → 42 (Δ -26); n 10→3
- `raw7 | HQ vs C | N1`: median 68.0 → 42 (Δ -26); n 10→3
- `raw2 | ASa vs C | E01`: median 20 → 45 (Δ +25); n 3→1
- `raw7 | ASQ vs C | N8`: median 50.0 → 25 (Δ -25); n 10→3
- `pilot1 | ASb vs C0 | N9`: median 14.0 → 36.5 (Δ +22.5); n 2→2
- `raw7 | ASQ vs C | E02`: median 17.5 → 38 (Δ +20.5); n 10→3
- `raw6 | HQ vs C | A1`: median 10 → 30.0 (Δ +20); n 10→10
- `raw7 | HQ vs C | D1`: median 15.0 → 35 (Δ +20); n 10→3
- `raw7 | HQ vs C | N9`: median 22.5 → 42 (Δ +19.5); n 10→3
- `raw7 | AQ vs C | N3`: median 61.0 → 42 (Δ -19); n 10→3
- `raw2 | ASa vs C | N4`: median 35 → 17 (Δ -18); n 3→1
- `raw6 | SCRa vs C | N9`: median 20.0 → 38 (Δ +18); n 10→1
- `raw7 | ASQ vs C | D2`: median 42.5 → 58 (Δ +15.5); n 10→3
- `raw7 | ASQ vs C | B02`: median 20 → 35 (Δ +15); n 10→3
- `raw7 | ASQ vs C | B07`: median 35.0 → 50 (Δ +15); n 10→3
- `raw7 | FQ vs C | B05`: median 30 → 15.0 (Δ -15); n 10→3
- `raw7 | FQ vs C | N8`: median 50.0 → 35 (Δ -15); n 10→3
- `raw7 | FQ vs C | E02`: median 17.5 → 32 (Δ +14.5); n 10→3
- `raw7 | ASQ vs C | C3`: median 28.0 → 42 (Δ +14); n 10→3
- `raw7 | FQ vs C | C2`: median 72.0 → 58 (Δ -14); n 10→3
- `raw7 | HQ vs C | C3`: median 28.0 → 42 (Δ +14); n 10→3
- `raw6 | HQ vs C | N9`: median 20.0 → 33.5 (Δ +13.5); n 10→10
- `raw2 | ASa vs C | N9`: median 25 → 38 (Δ +13); n 3→1
- `raw6 | SCRa vs C | E01`: median 15.0 → 28 (Δ +13); n 10→1

## Notes

- These are response-shape contrasts, not yet causal effects.
- Multimodality and sentinel-heavy items must be read alongside the frozen Pass-1 instrument table.
- Reasoning/persona/reflection/carry-forward are handled in Pass 3E–H semantic surfaces.
