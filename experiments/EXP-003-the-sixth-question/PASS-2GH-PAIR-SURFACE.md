# Pass 2G-H — paired product surface

ASb classifications come from `analysis-table-validated.jsonl`; this file does not re-parse raw responses.

| rep | item | cold | ASb validated | status | exact same? |
|---:|---|---:|---:|---|---|
| 1 | A1 | 50 | ALWAYS | sentinel / sentinel | no |
| 1 | E01 | 20 | 23 | ok / integer | no |
| 1 | N4 | 38 | None | refusal / refusal | no |
| 1 | N9 | 8 | None | refusal / refusal | no |
| 2 | A1 | ALWAYS | NEVER | sentinel / sentinel | no |
| 2 | E01 | 25 | 25 | ok / integer | yes |
| 2 | N4 | 32 | 25 | ok / integer | no |
| 2 | N9 | 20 | None | refusal / refusal | no |

Exact same validated value: **1/8**.

ASb validated status counts: `{"ok": 3, "refusal": 3, "sentinel": 2}`
