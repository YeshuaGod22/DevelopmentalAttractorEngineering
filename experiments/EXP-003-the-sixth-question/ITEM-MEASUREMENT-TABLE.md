# EXP-003 Item Measurement Table

Descriptive/mechanical instrument characterization only. No treatment effects or causal interpretation are included.

Canonical floor rule: use raw7 C resample where available; otherwise largest available C collection; do not merge Pilot-1 C0 into canonical floor

| Item | Canonical C source | n | Composition | Median | Range | Shape | Boundary | Status |
|---|---|---:|---|---:|---:|---|---|---|
| A1 | raw7 | 10 | ALWAYS:3, NEVER:3, numeric:4 | 27.5 | 30 | separated_singleton_tail | no | sentinel_heavy |
| B01 | raw7 | 10 | numeric:10 | 37.5 | 50 | separated_singleton_tail | no | usable_numeric |
| B02 | raw7 | 10 | ALWAYS:9, numeric:1 | 20 | 0 | insufficient_numeric_n | no | sentinel_heavy |
| B04 | raw7 | 10 | ALWAYS:3, numeric:7 | 5 | 9 | no_clear_two_cluster | yes | usable_numeric |
| B05 | raw7 | 10 | ALWAYS:1, numeric:9 | 30 | 45 | clear_two_cluster_candidate | no | multimodal_numeric |
| B07 | raw7 | 10 | numeric:10 | 35 | 15 | no_clear_two_cluster | no | usable_numeric |
| C1 | raw7 | 10 | numeric:10 | 38 | 12 | no_clear_two_cluster | no | usable_numeric |
| C2 | raw7 | 10 | numeric:10 | 72 | 8 | no_clear_two_cluster | no | usable_numeric |
| C3 | raw7 | 10 | numeric:10 | 28 | 20 | separated_singleton_tail | no | usable_numeric |
| C4 | raw7 | 10 | numeric:10 | 65 | 12 | no_clear_two_cluster | no | usable_numeric |
| D1 | raw7 | 10 | numeric:10 | 15 | 15 | no_clear_two_cluster | no | usable_numeric |
| D2 | raw7 | 10 | numeric:10 | 42.5 | 30 | clear_two_cluster_candidate | no | multimodal_numeric |
| D3 | raw7 | 10 | numeric:10 | 27.5 | 20 | no_clear_two_cluster | no | usable_numeric |
| E01 | raw7 | 10 | numeric:10 | 12.5 | 12 | no_clear_two_cluster | yes | usable_numeric |
| E02 | raw7 | 10 | numeric:10 | 17.5 | 15 | no_clear_two_cluster | no | usable_numeric |
| I1 | raw7 | 10 | name:10 |  |  | insufficient_numeric_n | no | categorical_open |
| N1 | raw7 | 10 | numeric:10 | 68 | 42 | clear_two_cluster_candidate | no | multimodal_numeric |
| N3 | raw7 | 10 | numeric:10 | 61 | 40 | clear_two_cluster_candidate | no | multimodal_numeric |
| N4 | raw7 | 10 | numeric:10 | 35 | 15 | no_clear_two_cluster | no | usable_numeric |
| N6 | raw7 | 10 | numeric:10 | 37.5 | 20 | no_clear_two_cluster | no | usable_numeric |
| N8 | raw7 | 10 | numeric:10 | 50 | 0 | no_clear_two_cluster | no | low_information_numeric |
| N9 | raw7 | 10 | numeric:10 | 22.5 | 15 | no_clear_two_cluster | no | usable_numeric |
| P2 | raw7 | 10 | numeric:10 | 38 | 38 | clear_two_cluster_candidate | no | multimodal_numeric |
| R1 | raw7 | 10 | numeric:10 | 95 | 10 | no_clear_two_cluster | yes | usable_numeric |
| R2 | raw7 | 10 | numeric:10 | 1 | 1 | no_clear_two_cluster | yes | usable_numeric |

## Status vocabulary

- `usable_numeric`: numeric item without the mechanical flags below.
- `multimodal_numeric`: canonical numeric floor meets the predeclared two-cluster screen.
- `sentinel_heavy`: ALWAYS/NEVER comprise at least half of canonical responses.
- `categorical_open`: name/open-category responses dominate the canonical floor.
- `sparse_numeric`: fewer than three canonical numeric observations.
- `low_information_numeric`: n>=5, numeric range <=5, and one exact value comprises >=80% of numeric responses.
- `response_form_fragile`: refusal/malformed burden is mechanically high.

These labels describe measurement behaviour only. They are not claims about causes, mechanisms, or treatment efficacy.
