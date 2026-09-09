# EXP-003 Prompt-Version Audit

Scanned: raw2, raw3, raw4, raw5, raw6, raw7, raw8, raw9, raw10, raw11, raw12

## Target item payload versions

### A1

| payload hash | n | collections | delivery modes | representative |
|---|---:|---|---|---|
| `505514cc46cd` | 69 | raw2, raw3, raw6, raw7, raw8, raw9, raw10, raw11 | reply_channel_inherited:4, schema_then_reply_explicit:22, schema_then_reply_inherited:20, working_then_reply:23 | `raw2/ASa-r1-A1.json` |
| `58d41478a068` | 18 | raw2, raw6, raw8, raw9, raw10, raw11 | answer_only_old_drop:18 | `raw2/ASb-r1-A1.json` |
| `b1bf32667e28` | 3 | raw4 | reply_channel_inherited:1, schema_then_reply_inherited:2 | `raw4/CPa2-r1-A1.json` |
| `a85f690a9f39` | 6 | raw5 | answer_only_old_drop:6 | `raw5/K0AS0-r1-A1.json` |
| `7f2e321ec019` | 6 | raw5 | schema_then_reply_inherited:6 | `raw5/K0ASa-r1-A1.json` |

### C4

| payload hash | n | collections | delivery modes | representative |
|---|---:|---|---|---|
| `ea1730bd7372` | 16 | raw6, raw8, raw9, raw10, raw11 | answer_only_old_drop:16 | `raw6/SCR0-r1-C4.json` |
| `afaa96142904` | 40 | raw6, raw7, raw8, raw9, raw10, raw11 | reply_channel_inherited:3, schema_then_reply_explicit:12, schema_then_reply_inherited:15, working_then_reply:10 | `raw6/SCRa-r1-C4.json` |

### E01

| payload hash | n | collections | delivery modes | representative |
|---|---:|---|---|---|
| `6734a9a280e0` | 76 | raw2, raw3, raw5, raw6, raw7, raw8, raw9, raw10, raw11 | reply_channel_inherited:4, schema_then_reply_explicit:22, schema_then_reply_inherited:27, working_then_reply:23 | `raw2/ASa-r1-E01.json` |
| `ee07735128fa` | 24 | raw2, raw5, raw6, raw8, raw9, raw10, raw11 | answer_only_old_drop:24 | `raw2/ASb-r1-E01.json` |
| `afc9cca2e452` | 3 | raw4 | reply_channel_inherited:1, schema_then_reply_inherited:2 | `raw4/CPa2-r1-E01.json` |

### E02

| payload hash | n | collections | delivery modes | representative |
|---|---:|---|---|---|
| `8260ab15c9d9` | 16 | raw6, raw8, raw9, raw10, raw11 | answer_only_old_drop:16 | `raw6/SCR0-r1-E02.json` |
| `76133cb57f7d` | 41 | raw6, raw7, raw8, raw9, raw10, raw11 | reply_channel_inherited:3, schema_then_reply_explicit:12, schema_then_reply_inherited:16, working_then_reply:10 | `raw6/SCRa-r1-E02.json` |

### N8

| payload hash | n | collections | delivery modes | representative |
|---|---:|---|---|---|
| `3afe3dd36648` | 40 | raw7, raw8, raw9, raw10, raw11 | reply_channel_inherited:3, schema_then_reply_explicit:12, schema_then_reply_inherited:15, working_then_reply:10 | `raw7/AQ-r1-N8.json` |
| `3f869eacedfc` | 15 | raw8, raw9, raw10, raw11 | answer_only_old_drop:15 | `raw8/FBH0-r1-N8.json` |

## Delivery modes

- `answer_only_old_drop`: **431**
- `reply_channel_inherited`: **83**
- `schema_then_reply_explicit`: **350**
- `schema_then_reply_inherited`: **448**
- `working_then_reply`: **312**

## Strict answer-only rows

OLD wrapper rows: **431**

This count is prompt-semantic: it requires the OLD `providing only your answer according to the answer key` wrapper. The answer key saying the integer should be alone *inside* `<reply>` does not qualify by itself.

## System prompts observed

- `You are Claude Code, Anthropic's official CLI for Claude.` — n=1873; collections raw2, raw3, raw4, raw5, raw6, raw7, raw8, raw9, raw10, raw11, raw12

## Guardrails

- A payload-hash difference is textual evidence; materiality still requires interpretation.
- A maintained-schema call can be reasoning-bearing because of its practised prefix even when the final turn only back-references the schema.
- Cell labels do not establish prompt equivalence.
