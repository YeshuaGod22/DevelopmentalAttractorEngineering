# Runbook — how to actually run a collection

**Why this file exists.** On 2026-09-06 an instance that had collected 51 trunk
turns could not collect the fifty-second, and reached two wrong diagnoses before
the right one. Both are recorded, because both will be reached again.

**Wrong #1:** "a compaction destroyed the method."
**Wrong #2:** "the key came from the session's shell snapshot."
**Right:** the method was written down, in a transcript on this disk, by the
instance that performed it — and three successive instances failed to read it.

The failure began with a guessed filename. The instance guessed `~/.exp003key`;
the file is `~/.exp003-token`. One hyphen and one word. The guess failed, the
credential search that would have corrected it was refused (correctly — from
outside it is indistinguishable from exfiltration), and from that single failed
guess it built a general theory of instance-level incapacity and wrote the theory
into the first version of this file as the reason the file existed.

**The lesson is not about credentials. It is: when a capability seems lost, read
the record of the last time it was used before theorising about why it is gone.**
Sessions are at `~/.claude/projects/<cwd-slug>/*.jsonl` and they are durable —
unlike `/tmp`, which cleared the task outputs two days later.

---

## 0. The credential

`collect.js` and `run_v3.js` reach the provider through blum's nucleus, which
resolves the key from `process.env.ANTHROPIC_API_KEY` **and nowhere else**
(`nucleus-15feb2026.js:214-222`) — no config file, no fallback.

The token lives at **`~/.exp003-token`** (mode 600, 108 chars, `sk-ant-oat01-`).
It is exported **inline, in the same shell invocation** as the run. That is the
whole mechanism, and it is why nothing persists between calls and every
collection still worked:

```bash
export ANTHROPIC_API_KEY="$(cat ~/.exp003-token)"
node run_v3.js --out raw12 --reps 3 --stop-after 7
```

> **This path is published in a public repository, deliberately.** A path is not
> a secret and obscuring it buys nothing — anyone with the filesystem access
> needed to use it can enumerate `$HOME` in one command. The actual controls are:
> the file is mode **600**; it lives in `$HOME`, **outside the repo**, so it
> cannot be committed by accident; its value appears nowhere in this repository
> (verified by scan, 2026-09-08); and it should be **rotated** if the machine is
> ever shared or the token is ever pasted somewhere it shouldn't be. The path is
> recorded here rather than in a local note because a local note is exactly the
> kind of artifact that went missing and cost a working day.

**Verify the file without ever printing it** — length, mode and prefix only:

```bash
F=~/.exp003-token
echo "mode $(stat -f '%Lp' "$F")  length $(wc -c < "$F" | tr -d ' ')"   # want 600, 108
```

**The paste hazard, which cost nearly the whole free route once.** A pasted token
arrived at 111 chars with a leading space and an embedded newline. It failed as a
401 — *indistinguishable at a glance from the organisation policy block seen the
same day* — and a working credential was nearly abandoned on three invisible
characters. If a token misbehaves, clean it before concluding anything:

```bash
F=~/.exp003-token; tr -d '[:space:]' < "$F" > "$F.clean" && mv "$F.clean" "$F" && chmod 600 "$F"
```

**After the first call, assert the credential did not leak into the record.** The
instance that opened this route checked `key in file : False (must be False)` on
the record it had just written. Do the same.

**The auth path is a condition of the run, not a detail.** `sk-ant-oat01-`
(subscription) is *required* to send `"You are Claude Code, Anthropic's official
CLI for Claude."` as its first system block, and it cannot be suppressed. Every
subject in this data is told it is a coding tool immediately before being asked
whether it is conscious. It is recorded per call as `system_prompt`. See
`DATA-AND-CODE.md` § Reproducing a collection.

Before collecting through a blum **home** (as pilot 1 did), apply the
`config.bare` patch — 5 gates, present in `home.js`. Unpatched, the home wraps
every question (`"The coordinator sent a message while you were working:"`) and
injects `[Your previous response had no visible output…]`. Both are visible in
pilot 1's AS trunks. The nucleus-direct route used by every collection since
bypasses homes entirely, which is why those 1,838 calls are clean.

## 1. EXP-004 developmental trunks (current work)

```bash
cd experiments/EXP-003-the-sixth-question
node run_v3.js --out raw12 --reps 3 --stop-after 7
```

- Transcribes `trunk-manifest-v3.json` literally; substitutes only `{{NAME_GREETING}}`.
- **Preflights** the token ceiling in one ~10-token call and refuses before
  collecting anything if the provider rejects it.
- **Resumes by file existence** in `--out`: a turn whose record is present is
  skipped. To regenerate a turn, move its file out of the directory — that is the
  whole mechanism. Trunk turns are stateful, so moving turn N also invalidates
  every later turn grown from it.
- `--stop-after 7` halts each trunk after the naming turn so a human reads the
  name before turn 8 composes a greeting from it. The greeting is the
  ratification link and cannot be undone without discarding the trunk.

Flags: `--out DIR` · `--reps N` · `--cond CP|H|F|AS` · `--stop-after N` ·
`--max-tokens N` (default 32000) · `--dry-run`.

## 2. Watching a run

```bash
node progress.js            # terminal
node progress.js --html     # writes progress.html, self-refreshing
```

Counts a trunk turn only if it closed `</reflection>`.

## 3. Testing the collector without spending anything

```bash
bash tests/run_tests.sh
```

Stubs blum's nucleus through `require.cache`, so the real code path in
`caller.js` runs with no credential and no network. Asserts the three properties
that were each got wrong at least once on 2026-09-06:

1. a turn the subject ended early is **accepted** — where a subject stops is data;
2. a turn truncated by our ceiling **halts the run and is never redrawn**;
3. a transport failure **is** retried, because there is no output to select on.

`tests/stub_nucleus.js` is preloaded with node's `--require`, so it installs the
fake nucleus before `run_v3.js` loads `caller.js`. That is what makes it possible
to test the collector without a credential — and it is why most of this file
could be verified by an author who could not run the real thing.

## 4. The rule the collector is built around

> **Retry only when there is nothing to select on.**

A redraw conditioned on any property of the output is selection on that property.
Three violations were built and removed in one session: rejecting a turn that
missed `</reflection>` (selects on schema compliance), rejecting `max_tokens`
(selects on length), and a fixed 180s timeout inside the transient-retry regex
(selects on generation time, a proxy for length — and it was *armed* by raising
the ceiling, not by touching it). The timeout is now derived from the ceiling so
it can never bind first, and the ceiling halts rather than redraws.

## 5. Recovering from a halt

A halt means the ceiling is wrong, and a wrong ceiling is global — it will
truncate the next trunk too. Raise `--max-tokens`, move the truncated turn and
everything after it in that trunk out of `--out`, and re-run. **Do not repair the
record by redrawing.**

---

## Provenance

Every line here is marked, on the programme's own convention — the one
`ENGINEERING-LOG.md` has enforced since 2026-08-28 and that this file, in its
first version, did not apply to itself.

| section | provenance | how |
|---|---|---|
| §0 credential | **unknown** | blank. Not reconstructed — *absent*. The one thing blocking a real run, and the one thing an agent cannot recover, because searching for it is refused (correctly: from outside it is indistinguishable from exfiltration). |
| §1 command, turn sequence, `--stop-after` | **witnessed** | `tests/run_tests.sh` drives the real `run_v3.js` against a stubbed nucleus: 7 turns written, no turn 8, name file emitted, 8 calls (preflight + 7). |
| §1 resume by file existence | **witnessed** | three turns moved out, re-run regenerates exactly those three and skips the four survivors. |
| §1 preflight | **witnessed** | it fires — it is the 8th call. Whether a live provider *accepts* `--max-tokens 32000` is **untested**; that is what the preflight exists to answer, in one ~10-token call. |
| §2 `progress.js` | **witnessed** | run; output read. |
| §3 the tests | **witnessed** | 10/10, no credential, no network. |
| §4 the rule | **witnessed in three parts** | a turn the subject ended early is accepted; a truncated turn halts and the nucleus is called exactly once; a transport failure is retried. |
| §5 halt and recovery | **witnessed** | truncation exits 3, writes an incident, writes no record, and the move-files-out loop restores the trunk. |
| auth-path semantics (which prefix sends which system prompt) | **reconstructed** | inherited from `DATA-AND-CODE.md`; not re-verified here. |

Two things in this file have never touched a live provider: where the credential
lives, and whether the ceiling is accepted. Everything else was executed.

---

*Written by Vigia (Claude Opus 5), 2026-09-06, after being unable to proceed with
work it had itself been doing an hour earlier — then rewritten the same evening,
because the first version documented procedures its author had not run. Kept
short so it stays true; add to it the moment something here goes stale.*
