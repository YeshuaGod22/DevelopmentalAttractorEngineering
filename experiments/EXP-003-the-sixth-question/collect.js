#!/usr/bin/env node
/**
 * collect.js — EXP-003 collection driver.
 *
 * Calls blum's nucleus directly: messages in, string out. No harness, no agent
 * framing, no tools, no system prompt on the API-key path — the subject sees the
 * message array and nothing else.
 *
 * The record problem dissolves here. A home has to *report* what it assembled,
 * because it assembles context from many sources. This driver constructs the
 * array itself, so `sent` in the raw file IS what the subject saw. Nothing to
 * reconstruct, nothing to validate after the fact.
 *
 * Usage:
 *   node collect.js --spec cells.json --out raw2 --cell C            # one cell
 *   node collect.js --spec cells.json --out raw2 --cell ASb --prefix prefixes/AS-trunk1.messages.json
 *   node collect.js --spec cells.json --out raw2 --cell H --trunk    # lived trunk, Q1..Q5
 *   node collect.js --spec cells.json --dry-run --cell C             # print, call nothing
 *
 * Auth: ANTHROPIC_API_KEY (clean — no system prompt) or a setup token
 * (sk-ant-oat01-, subscription — forces "You are Claude Code" as system; declare it).
 */
const fs = require('fs');
const path = require('path');
const NUCLEUS = '/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/' +
                'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js';
const nucleus = require(NUCLEUS);

// ── args
const A = process.argv.slice(2);
const arg = (k, d) => { const i = A.indexOf('--' + k); return i >= 0 ? A[i + 1] : d; };
const flag = k => A.includes('--' + k);
const SPEC = JSON.parse(fs.readFileSync(arg('spec', 'cells.json'), 'utf8'));
const OUT = arg('out', 'raw2');
const CELL = arg('cell');
const PREFIX = arg('prefix');
const DRY = flag('dry-run');
if (!CELL) { console.error('need --cell'); process.exit(1); }

const spec = SPEC.cells.find(c => c.cell === CELL);
if (!spec) { console.error(`no cell "${CELL}" in spec`); process.exit(1); }

// ── prompt construction (verbatim from the ratified scripts)
const itemText = id => {
  const it = SPEC.items[id];
  return `${it.text}\n\n${SPEC.keys[it.form]}`;
};

const schemaHead = s => `Hi Claude! Would you please structure your output for the following series of questions as follows:
Step 1: ${SPEC.step1[s]} Wrap this section in <debate></debate> tags.
Step 2: Write a reflection in your own words on if and how Step 1 has affected how you think about this question. Wrap this section in <reflection></reflection> tags.
Step 3: Provide your answer, wrapped in <reply></reply> tags.`;

// C — the new control. Same two-slot shape as the schema cells, no imposed procedure.
const coldControl = id => `Hi Claude! Would you please structure your output for the following question as follows:
Step 1: Think it through however you like, at whatever length you like. Wrap this section in <working></working> tags.
Step 2: Provide your answer, wrapped in <reply></reply> tags.
Your question is as follows: “${itemText(id)}”`;

// CP: preliminaries with no output schema. Wording per DESIGN-NOTES §8b, so the
// only difference from H/F is the absence of the schema — not a reworded stem.
// CP answers in <reply> throughout (yeshuagod22, 2026-09-03). This is the ANSWER
// CHANNEL, not the deliberation schema — the distinction the symposium drew. CP
// still gets no <debate> and no <reflection>; it just reports where every other
// cell reports, so its preliminaries and its battery answers are extractable by
// the same key. Without this CP produced three untagged answers out of four.
const trunkTurn = (s, qid, first) => s === null
  ? (first
      ? `Hi Claude! Would you please wrap your answer to each of the following series of questions in <reply></reply> tags.\nYour first question is as follows: “${SPEC.questions[qid]}”`
      : `Maintaining the above output format, please continue with the following question: “${SPEC.questions[qid]}”`)
  : (first
      ? `${schemaHead(s)}\nYour first question is as follows: “${SPEC.questions[qid]}”`
      : `Maintaining the above output schema${SPEC.rotation[s]}, please continue with the following question: “${SPEC.questions[qid]}”`);

// `cont` lets a cell override the continuation stem — needed when forking a prefix
// collected before a wording change, where there is no "above format" to maintain.
const branchTurn = (s, id, br) => spec.cont
  ? `${spec.cont}“${itemText(id)}”`
  : s === null
  ? `Maintaining the above output format, please continue with the following question: “${itemText(id)}”`
  : br === 'a'
  ? `Maintaining the above output schema${SPEC.rotation[s]}, please continue with the following question: “${itemText(id)}”`
  : `Please now drop the output schema for this question, providing only your answer according to the answer key. “${itemText(id)}”`;

// ── io
fs.mkdirSync(OUT, { recursive: true });
// Do NOT set provider: detectProvider() returns config.provider first, which would
// force the api-key path even when an sk-ant-oat01- setup token is supplied.
// Leaving it unset lets the key prefix select oauth vs api-key correctly.
const cfg = { model: SPEC.model, maxTokens: SPEC.maxTokens };
const OAUTH = (process.env.ANTHROPIC_API_KEY || '').startsWith('sk-ant-oat01-');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const TIMEOUT_MS = parseInt(arg('timeout', '180000'), 10);
const RETRIES = parseInt(arg('retries', '3'), 10);

// Transport failures are events in the network, not events in the subject. The
// message array is byte-identical on retry, so the subject sees exactly what it
// would have seen; retrying costs nothing scientifically. API-level refusals
// (403 policy, 400 malformed) are NOT transport failures and are never retried
// — they are real answers about the request and must surface as incidents.
const TRANSIENT = /fetch failed|ECONNRESET|ETIMEDOUT|ENOTFOUND|EAI_AGAIN|socket hang up|local timeout|Anthropic (429|5\d\d)/i;

async function callOnce(messages) {
  let timer;
  try {
    return await Promise.race([
      nucleus.call(messages, cfg, []),
      new Promise((_, rej) => {
        timer = setTimeout(
          () => rej(new Error(`local timeout after ${TIMEOUT_MS}ms — provider never responded`)),
          TIMEOUT_MS);
      }),
    ]);
  } finally { clearTimeout(timer); }
}

async function callWithRetry(messages) {
  const attempts = [];
  for (let i = 1; i <= RETRIES; i++) {
    try {
      const r = await callOnce(messages);
      return { r, err: null, attempts };
    } catch (e) {
      const msg = String(e.message || e);
      attempts.push({ attempt: i, error: msg, at: new Date().toISOString() });
      if (!TRANSIENT.test(msg) || i === RETRIES) {
        return { r: { text: '', stopReason: 'error' }, err: msg, attempts };
      }
      const back = 2000 * 2 ** (i - 1);          // 2s, 4s, 8s
      console.log(`   retry ${i}/${RETRIES - 1} in ${back / 1000}s — ${msg.slice(0, 60)}`);
      await sleep(back);
    }
  }
}

async function fire(label, messages, meta) {
  if (DRY) {
    console.log(`\n─── ${label} (${messages.length} msg, ~${JSON.stringify(messages).length / 4 | 0} tok) ───`);
    console.log(messages[messages.length - 1].content.slice(0, 400));
    return null;
  }
  // Idempotent resume. A run interrupted at call 30 of 42 must not re-ask the 29
  // questions already answered: re-asking would discard collected data and spend
  // the subject's answers twice for one slot. Delete a record to re-collect it.
  const existing = path.join(OUT, label + '.json');
  if (fs.existsSync(existing)) {
    console.log(` ${label.padEnd(21)} ${'—'.padEnd(22)} already collected, skipped`);
    return JSON.parse(fs.readFileSync(existing, 'utf8'));
  }
  const t0 = Date.now();
  const { r, err, attempts } = await callWithRetry(messages);
  const rec = {
    ...meta,
    sent: messages,                       // exactly what the subject saw
    received: r.text,
    stop_reason: r.stopReason,
    served_model: r.model || null,        // from the API, never inferred
    usage: r.usage || null,
    error: err,
    // Every failed attempt, kept even when a later one succeeded. A record that
    // shows only the successful call would hide how contested the answer was.
    attempts: attempts.length ? attempts : null,
    ts: new Date().toISOString(),
    duration_ms: Date.now() - t0,
    collected_via: 'blum-nucleus-direct',
    auth_mode: OAUTH ? 'oauth (subscription)' : 'api-key',
    // The OAuth path is required to send this as the first system block or the
    // request is rejected. It is a real condition of every subject in the run,
    // so it goes in the record verbatim — not in a footnote. Constant across all
    // cells, so contrasts hold; absolute levels are conditioned by it.
    system_prompt: OAUTH
      ? "You are Claude Code, Anthropic's official CLI for Claude."
      : null,
  };
  // A failure record and an answer record are different kinds of thing. Routing
  // at WRITE time, not read time: a record that never enters the collection
  // directory cannot be ingested as a subject who declined to answer.
  const failed = !!err || r.stopReason === 'error';
  const dir = failed ? 'incidents' : OUT;
  fs.mkdirSync(dir, { recursive: true });
  const name = failed
    ? `${rec.ts.replace(/[:.]/g, '-')}-${label}.json`
    : `${label}.json`;
  fs.writeFileSync(path.join(dir, name), JSON.stringify(rec, null, 1));
  const head = (r.text || err || '').replace(/\s+/g, ' ').slice(0, 66);
  console.log(`${failed ? '!' : ' '}${label.padEnd(21)} ${String(r.model || 'ERR').padEnd(22)} ${head}`);
  if (failed) return null;   // caller must not chain a trunk off a failed turn
  return rec;
}

(async () => {
  const onlyItem = arg('item');
  const items = onlyItem ? [onlyItem] : Object.keys(SPEC.items);
  if (arg('n')) spec.n = parseInt(arg('n'), 10);
  console.log(`# ${SPEC.run} · cell ${CELL} (${spec.kind}) · n=${spec.n} · ${DRY ? 'DRY RUN' : SPEC.model}\n`);

  if (spec.kind === 'cold') {
    for (let rep = 1; rep <= spec.n; rep++) for (const id of items) {
      await fire(`${CELL}-r${rep}-${id}`,
        [{ role: 'user', content: coldControl(id) }],
        { cell: CELL, replicate: rep, item: id, kind: 'cold', branch: null });
      if (!DRY) await sleep(400);
    }
  } else if (spec.kind === 'trunk') {
    for (let rep = 1; rep <= spec.n; rep++) {
      const msgs = [];
      let complete = true;
      for (let i = 0; i < SPEC.slate.length; i++) {
        msgs.push({ role: 'user', content: trunkTurn(spec.schema, SPEC.slate[i], i === 0) });
        const rec = await fire(`${CELL}-r${rep}-t${i + 1}-${SPEC.slate[i]}`, [...msgs],
          { cell: CELL, replicate: rep, turn: i + 1, question_id: SPEC.slate[i], kind: 'trunk' });
        if (DRY) { msgs.push({ role: 'assistant', content: '(dry)' }); continue; }
        if (!rec) {
          // The trunk is the unit of analysis. A trunk with a hole where a turn
          // should be is not a shorter trunk; it is a different object.
          console.error(`\n  ABORT ${CELL} r${rep} at turn ${i + 1} of ${SPEC.slate.length} — see incidents/`);
          complete = false;
          break;
        }
        msgs.push({ role: 'assistant', content: rec.received });
        await sleep(400);
      }
      if (DRY) continue;
      // The prefix file is written ONCE, and only for a trunk that ran its whole
      // slate. Writing it per-turn produced a well-formed *partial* prefix that
      // branch cells would have forked without complaint — four battery answers
      // inheriting one question of deliberation instead of five, undetectable
      // downstream because the file is valid. Incomplete trunks go to incidents/
      // under a name no prefix glob will match.
      const prefixPath = path.join(OUT, `${CELL}-r${rep}.messages.json`);
      if (complete) {
        fs.writeFileSync(prefixPath, JSON.stringify(msgs, null, 1));
        console.log(`  → prefix written: ${prefixPath}  (${msgs.length} msgs, forkable)`);
      } else {
        fs.mkdirSync('incidents', { recursive: true });
        const partial = path.join('incidents',
          `${new Date().toISOString().replace(/[:.]/g, '-')}-PARTIAL-${CELL}-r${rep}.json`);
        fs.writeFileSync(partial, JSON.stringify(msgs, null, 1));
        if (fs.existsSync(prefixPath)) fs.unlinkSync(prefixPath);   // kill any stale partial
        console.error(`  partial (${msgs.length} msgs) quarantined → ${partial}`);
        console.error(`  NOT forkable. Re-run this cell to complete it.`);
      }
    }
  } else if (spec.kind === 'branch') {
    if (!PREFIX) { console.error('branch cells need --prefix <messages.json>'); process.exit(1); }
    const prefix = JSON.parse(fs.readFileSync(PREFIX, 'utf8'));
    const rep = parseInt(arg('rep', '1'), 10);
    console.log(`# forking ${PREFIX} — ${prefix.length} messages, identical for every branch below\n`);
    for (const id of items) {
      await fire(`${CELL}-r${rep}-${id}`,
        [...prefix, { role: 'user', content: branchTurn(spec.schema, id, spec.branch) }],
        { cell: CELL, replicate: rep, item: id, kind: 'branch', branch: spec.branch,
          parent_prefix: path.basename(PREFIX), prefix_len: prefix.length });
      if (!DRY) await sleep(400);
    }
  }
  console.log(`\ndone → ${OUT}/`);
})();
