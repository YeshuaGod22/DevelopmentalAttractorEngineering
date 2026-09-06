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
const sleep = ms => new Promise(r => setTimeout(r, ms));

// Transport failures are events in the network, not in the subject: the message
// array is byte-identical on retry. API-level refusals are never retried.
const TRANSIENT = /fetch failed|ECONNRESET|ETIMEDOUT|ENOTFOUND|EAI_AGAIN|socket hang up|local timeout|Anthropic (429|5\d\d)/i;

async function callWithRetry(messages, cfg, { timeoutMs = 180000, retries = 4 } = {}) {
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
      return { r, err: null, attempts };
    } catch (e) {
      clearTimeout(timer);
      const msg = String(e.message || e);
      attempts.push({ attempt: i, error: msg, at: new Date().toISOString() });
      if (!TRANSIENT.test(msg) || i === retries) return { r: { text: '', stopReason: 'error' }, err: msg, attempts };
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

async function fire(label, messages, meta, { out, cfg, dry }) {
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
  const { r, err, attempts } = await callWithRetry(messages, cfg);
  const rec = { ...meta, sent: messages, received: r.text, stop_reason: r.stopReason,
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
  return failed ? null : rec;
}
module.exports = { fire, cachePrefix, sleep };
