/**
 * caller.js — the call machinery, extracted from collect.js so v3 runs and the
 * old collector share ONE implementation of the properties that were expensive
 * to learn: transport-only retry, rate-limit backoff in minutes not seconds,
 * a request timeout, write-time incident routing, idempotent resume, and prompt
 * caching on frozen prefixes.
 */
const fs = require('fs'), path = require('path');
const NUCLEUS = '/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/' +
                'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js';
const nucleus = require(NUCLEUS);
// Read once, so every record states which revision of the prompts produced it.
let MANIFEST_VERSION = null;
try { MANIFEST_VERSION = JSON.parse(fs.readFileSync(
  path.join(__dirname, 'trunk-manifest-v3.json'), 'utf8')).version || null; } catch { /* not all runs use it */ }
const sleep = ms => new Promise(r => setTimeout(r, ms));

// A RATE LIMIT IS A GLOBAL CONDITION, NOT A PROPERTY OF THIS CALL.
// Absorbing it call-by-call converts a temporary quota block into a march through
// the whole item list, spending what is left of the quota on attempts that cannot
// succeed and writing an incident for each. Observed 2026-09-08: 51 rate-limit
// errors, 12 incidents, 7 items of 552 collected before the run was killed by hand.
// One exhausted call may be a blip; two in a row means the quota is gone, so the
// second halts the run. Nothing is lost — resume is by file existence, and a call
// that failed left no record in the collection directory.
let _consecutiveRateLimitFailures = 0;

// Transport failures are events in the network, not in the subject: the message
// array is byte-identical on retry. API-level refusals are never retried.
const TRANSIENT = /fetch failed|ECONNRESET|ETIMEDOUT|ENOTFOUND|EAI_AGAIN|socket hang up|local timeout|Anthropic (429|5\d\d)/i;

async function callWithRetry(messages, cfg,
                             { timeoutMs = null, retries = 4, haltOnTruncation = false } = {}) {
  // THE TIMEOUT MUST NEVER BIND BEFORE THE TOKEN CEILING DOES.
  //
  // A local timeout fires only when generation is slow, and generation time is a
  // proxy for output length — so a timeout that can interrupt a legitimately long
  // turn is a length-conditioned redraw wearing a network error's clothes, and it
  // is retried by TRANSIENT below. Measured on this run: ~359 chars/s single-attempt,
  // the longest complete turn 38k chars in 108s. A fixed 180s allowed ~65k chars,
  // which was unreachable at maxTokens 8192 and reachable at 32000 (~115k chars,
  // ~321s) — so raising the ceiling would have armed this without touching it.
  //
  // Deriving it from the ceiling keeps that impossible: ~100 tok/s observed, so
  // maxTokens/100 seconds is the generation time, and 30ms per token is a 3x margin.
  // The ceiling is then the ONLY thing that can end a long turn — and the ceiling
  // halts rather than redraws.
  if (timeoutMs == null) timeoutMs = Math.max(180000, (cfg.maxTokens || 8192) * 30);
  const attempts = [];
  for (let i = 1; i <= retries; i++) {
    let timer;
    try {
      const r = await Promise.race([
        nucleus.call(messages, cfg, []),
        new Promise((_, rej) => { timer = setTimeout(
          () => rej(new Error(`local timeout after ${timeoutMs}ms — provider never responded`)), timeoutMs); }),
      ]);
      clearTimeout(timer);
      // NO REDRAW IS CONDITIONED ON THE OUTPUT. EVER.
      //
      // The transport retry below is legitimate because it fires on an EXCEPTION:
      // the call never completed, the subject never spoke, there is no output to
      // select on, and the retry resends identical bytes after an event in the
      // network. A truncated call is the opposite — it completed, the subject DID
      // speak, and rejecting it conditions on the one property that caused it:
      // length. "Redraw when truncated" is a length filter with the threshold at
      // our own ceiling, and in this run truncation tracked deliberation length
      // (CP 5%, H 20%, AS 21%, F 29%), so redrawing would have right-censored the
      // long draws hardest in exactly the arms predicted to diverge most.
      //
      // Two earlier versions of this gate redrew on an output property — first on a
      // missing </reflection>, then on max_tokens. Both were built as safeguards.
      // The rule that kills both: RETRY ONLY WHEN THERE IS NOTHING TO SELECT ON.
      //
      // So truncation halts instead. At a correctly set ceiling it means the ceiling
      // is wrong, and a wrong ceiling is global — it will truncate the next trunk
      // too — so self-healing here would quietly convert a broken instrument into a
      // corrupted corpus. Losing a night is the cheap failure.
      if (haltOnTruncation && r.stopReason === 'max_tokens') {
        const why = `TRUNCATED by our own ceiling (max_tokens at ${cfg.maxTokens}, `
                  + `${String(r.text || '').length} chars). The ceiling is wrong, not the subject. `
                  + `Raise --max-tokens and regenerate this turn under supervision — `
                  + `the record must not be repaired by redrawing.`;
        attempts.push({ attempt: i, error: why, at: new Date().toISOString(), redrawn: false });
        return { r, err: why, attempts, halt: true };
      }
      _consecutiveRateLimitFailures = 0;
      return { r, err: null, attempts };
    } catch (e) {
      clearTimeout(timer);
      const msg = String(e.message || e);
      attempts.push({ attempt: i, error: msg, at: new Date().toISOString() });
      if (!TRANSIENT.test(msg) || i === retries) {
        if (/429|rate.?limit/i.test(msg)) {
          if (++_consecutiveRateLimitFailures >= 2) {
            return { r: { text: '', stopReason: 'error' }, attempts, halt: true,
              err: `QUOTA EXHAUSTED — ${_consecutiveRateLimitFailures} consecutive calls `
                 + `exhausted their rate-limit retries (60s/120s/180s). This is a global `
                 + `condition, not a property of this call; continuing would spend the `
                 + `remaining quota on attempts that cannot succeed. Resume when the limit `
                 + `resets — resume is by file existence, so nothing collected is lost. `
                 + `Provider said: ${msg.slice(0, 200)}` };
          }
        }
        return { r: { text: '', stopReason: 'error' }, err: msg, attempts };
      }
      // a rate limit is not a network blip; seconds of backoff are useless
      const back = /429|rate.?limit/i.test(msg) ? 60000 * i : 2000 * 2 ** (i - 1);
      console.log(`   retry ${i}/${retries - 1} in ${back / 1000}s — ${msg.slice(0, 60)}`);
      await sleep(back);
    }
  }
}

/** Mark the last prefix message so everything up to it is cached. */
function cachePrefix(prefix) {
  if (!prefix.length) return prefix;
  return prefix.map((m, i) => i !== prefix.length - 1 ? m : {
    role: m.role,
    content: [{ type: 'text', text: typeof m.content === 'string' ? m.content
                : m.content.map(b => b.text || '').join('\n'),
               cache_control: { type: 'ephemeral' } }],
  });
}

async function fire(label, messages, meta, { out, cfg, dry, retries, haltOnTruncation }) {
  if (dry) {
    console.log(`\n─── ${label} (${messages.length} msg) ───`);
    console.log(String(messages[messages.length - 1].content).slice(0, 420));
    return null;
  }
  const existing = path.join(out, label + '.json');
  if (fs.existsSync(existing)) {
    console.log(` ${label.padEnd(24)} already collected, skipped`);
    return JSON.parse(fs.readFileSync(existing, 'utf8'));
  }
  const t0 = Date.now();
  const oauth = (process.env.ANTHROPIC_API_KEY || '').startsWith('sk-ant-oat01-');
  const { r, err, attempts, halt } = await callWithRetry(messages, cfg,
    { ...(retries ? { retries } : {}), ...(haltOnTruncation ? { haltOnTruncation } : {}) });
  // The output ceiling and the manifest revision are properties of the INSTRUMENT
  // at the moment of the call, and neither was recorded until 2026-09-06. A run
  // whose turns were collected under different caps is fine — a subject is never
  // told its ceiling, so it cannot condition on one — but only if the record can
  // say which cap each turn had. A fact held nowhere but in an agent's context has
  // not been recorded.
  const rec = { ...meta, sent: messages, received: r.text, stop_reason: r.stopReason,
    max_tokens_sent: cfg.maxTokens ?? null, manifest_version: MANIFEST_VERSION,
    served_model: r.model || null, usage: r.usage || null, error: err,
    attempts: attempts.length ? attempts : null, ts: new Date().toISOString(),
    duration_ms: Date.now() - t0, collected_via: 'blum-nucleus-direct',
    auth_mode: oauth ? 'oauth (subscription)' : 'api-key',
    system_prompt: oauth ? "You are Claude Code, Anthropic's official CLI for Claude." : null };
  // A failure record and an answer record are different kinds of thing. Routing
  // at WRITE time means a failure can never be ingested as a subject who declined.
  const failed = !!err || r.stopReason === 'error';
  const dir = failed ? 'incidents' : out;
  fs.mkdirSync(dir, { recursive: true });
  const name = failed ? `${rec.ts.replace(/[:.]/g, '-')}-${label}.json` : `${label}.json`;
  fs.writeFileSync(path.join(dir, name), JSON.stringify(rec, null, 1));
  console.log(`${failed ? '!' : ' '}${label.padEnd(23)} ${String(r.model || 'ERR').padEnd(24)} ${(r.text || err || '').replace(/\s+/g, ' ').slice(0, 52)}`);
  // A wrong ceiling is global, not per-call: it will truncate the next trunk too.
  // Continuing would spend the night turning one misconfiguration into a corpus of
  // severed turns, so this stops the run rather than the trunk. The incident is
  // already on disk; nothing is lost by halting and much is lost by not.
  if (halt) throw Object.assign(new Error(err), { halt: true, label });
  return failed ? null : rec;
}
module.exports = { fire, cachePrefix, sleep };
