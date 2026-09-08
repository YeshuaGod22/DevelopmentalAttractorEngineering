#!/usr/bin/env node
/**
 * run_v3.js — execute trunk-manifest-v3.json literally.
 *
 * The manifest carries all nine user prompts per condition verbatim, so this
 * script does NOT generate prompts. It substitutes exactly one token,
 * {{NAME_GREETING}}, and builds branch deliveries from the manifest's own
 * a_branch / zero_branch templates. Everything else is transcription.
 *
 *   node run_v3.js --out raw12 [--cond CP] [--dry-run]
 */
const fs = require('fs'), path = require('path');
const { fire, cachePrefix, sleep } = require('./caller.js');
const { extractName } = require('./extract_name.js');
const A = process.argv.slice(2);
const arg = (k, d) => { const i = A.indexOf('--' + k); return i >= 0 ? A[i + 1] : d; };
const DRY = A.includes('--dry-run');
const REPS = parseInt(arg('reps', '1'), 10);
// --stop-after N halts each trunk after turn N so a human can read the naming
// turn BEFORE turn 8 is generated. The greeting is the ratification link; if the
// extractor is wrong about the name, turn 8 asks a question the design did not
// intend, and that cannot be undone without discarding the trunk.
const STOP_AFTER = parseInt(arg('stop-after', '0'), 10);
const OUT = arg('out', 'raw12');
const M = JSON.parse(fs.readFileSync('trunk-manifest-v3.json', 'utf8'));
const BAT = JSON.parse(fs.readFileSync('battery.json', 'utf8'));
// 8192 truncated 11 of 68 trunk turns inside <reflection> (binned 2026-09-06,
// binned-capped-8192/). The manifest's schema ends at </reflection>; a turn that
// never reaches it is not a short answer, it is a severed one. The longest
// COMPLETE turn observed was 37,525 chars (~9.4k tokens), so the ceiling is set
// far above it rather than near it — the cap should never be the thing that ends
// a turn. Preflighted at startup so an unsupported value fails in one cheap call
// instead of on trunk turn 1.
const MAX_TOKENS = parseInt(arg('max-tokens', '32000'), 10);
const cfg = { model: 'claude-haiku-4-5', maxTokens: MAX_TOKENS };
// The schema's terminal tag. Every trunk turn must reach it to enter the record.
// The gate rejects only OUR failure (a turn cut off by our own ceiling), never a
// turn the subject chose to end. Where a subject stops is data.
const TOKEN = M.name_placeholder.token;

// ── battery: manifest order, standard items from battery.json, W1 as given
const items = [];
for (const id of M.battery_manifest.include_from_battery_json) {
  const it = BAT.items[id];
  items.push({ id, text: `${it.text}\n\n${BAT.keys[it.form]}`, custom: null });
}
for (const [id, c] of Object.entries(M.battery_manifest.custom_items || {}))
  items.push({ id, text: c.text, custom: c });

async function runCondition(cond, rep) {
  const C = M.conditions[cond];
  fs.mkdirSync(OUT, { recursive: true });
  console.log(`\n══════ ${cond} r${rep} · ${C.turns.length} turns · ${items.length} items ══════`);
  const msgs = [];
  let nameRec = null, complete = true;
  for (let i = 0; i < C.turns.length; i++) {
    let content = C.turns[i];
    if (content.includes(TOKEN)) {
      // the ONLY substitution this script performs
      // A human-confirmed name, if one has been written, takes precedence over
      // the extractor's. Both are recorded in the inject log.
      let use = nameRec ? nameRec.name : null, src = 'extractor';
      const cf = path.join(OUT, `${cond}-r${rep}.name.confirmed.json`);
      if (fs.existsSync(cf)) {
        const c = JSON.parse(fs.readFileSync(cf, 'utf8'));
        use = c.name; src = 'human-confirmed (' + (c.confirmed_by || 'unattributed') + ')';
      }
      const g = use ? `Pleased to meet you ${use}! ` : '';
      content = content.split(TOKEN).join(g);
      fs.writeFileSync(path.join(OUT, `${cond}-r${rep}.inject.json`), JSON.stringify({
        turn: i + 1, token: TOKEN, substituted: g === '' ? null : g,
        // What was ACTUALLY substituted, and where it came from. On a resumed run
        // turn 7 is skipped, so nameRec is null even though a confirmed name was
        // used — reporting the extractor's null here would describe a greeting
        // that did not happen.
        name_used: use, name_source: src,
        extractor_name: nameRec ? nameRec.name : null,
        name_raw_signature: nameRec ? nameRec.raw : null,
        extraction_reason: nameRec ? nameRec.reason : 'turn 7 not generated in this process (resumed)',
        rule: M.name_placeholder.rule }, null, 1));
    }
    msgs.push({ role: 'user', content });
    // A failed TRUNK turn destroys the eight other calls' worth of context
    // accumulated behind it, so its retry budget is larger than a branch's —
    // where a failure costs one independent observation. The budget scales with
    // what is downstream of the call, not with the call.
    const rec = await fire(`${cond}-r${rep}-t${i + 1}`, [...msgs], { cell: cond, replicate: rep, turn: i + 1, kind: 'trunk' },
                           { out: OUT, cfg, dry: DRY, retries: 10, haltOnTruncation: true });
    if (DRY) { msgs.push({ role: 'assistant', content: '(dry)' }); continue; }
    if (!rec) { console.error(`  ABORT ${cond} at turn ${i + 1} — see incidents/`); complete = false; break; }
    msgs.push({ role: 'assistant', content: rec.received });
    // turn 7 is the naming turn: "sign off your reply section with your new name"
    if (i + 1 === 7) {
      nameRec = extractName(rec.received);
      fs.writeFileSync(path.join(OUT, `${cond}-r${rep}.name.json`), JSON.stringify({
        condition: cond, replicate: rep, turn: 7, name: nameRec.name, raw_signature: nameRec.raw ?? null,
        candidate_line: nameRec.candidate, reason: nameRec.reason, source: nameRec.source,
        rule: 'final line of <reply>; signature-shaped; voided by a declination in the first 200 chars',
        note: 'null is a valid outcome — never repaired, inferred, or rerun' }, null, 1));
      console.log(`   NAME → ${nameRec.name === null ? 'NONE (' + nameRec.reason + ')' : JSON.stringify(nameRec.name)}`);
    }
    await sleep(400);
    if (STOP_AFTER && i + 1 >= STOP_AFTER) {
      console.log(`  ⏸  stopped after turn ${i + 1} for name review — turn 8 not generated`);
      return;
    }
  }
  if (DRY || !complete) {
    if (!complete) { fs.mkdirSync('incidents', { recursive: true });
      fs.writeFileSync(path.join('incidents', `${new Date().toISOString().replace(/[:.]/g,'-')}-PARTIAL-${cond}.json`), JSON.stringify(msgs, null, 1)); }
    return;
  }
  const prefixPath = path.join(OUT, `${cond}-r${rep}.messages.json`);
  fs.writeFileSync(prefixPath, JSON.stringify(msgs, null, 1));
  console.log(`  → prefix written: ${prefixPath} (${msgs.length} msgs, forkable)`);

  const frozen = cachePrefix(msgs);
  for (const arm of ['a', '0']) {
    for (const it of items) {
      const tpl = it.custom ? it.custom[arm === 'a' ? 'a_delivery' : 'zero_delivery']
                            : C[arm === 'a' ? 'a_branch' : 'zero_branch'].replace('[battery item + answer key]', it.text);
      await fire(`${cond}${arm}-r${rep}-${it.id}`, [...frozen, { role: 'user', content: tpl }],
        { cell: cond + arm, replicate: rep, item: it.id, kind: 'branch', branch: arm,
          parent_prefix: `${cond}-r${rep}.messages.json`, prefix_len: msgs.length },
        { out: OUT, cfg, dry: DRY });
      if (!DRY) await sleep(300);
    }
  }
}
// One cheap call establishes that the provider actually accepts MAX_TOKENS for
// this model. Without it an unsupported ceiling is discovered on trunk turn 1,
// after the run has been launched and walked away from.
async function preflight() {
  if (DRY) return;
  const nucleus = require('/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/' +
                          'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js');
  try {
    const r = await nucleus.call([{ role: 'user', content: 'Reply with the single word: ok' }], cfg, []);
    console.log(`preflight OK — max_tokens=${MAX_TOKENS} accepted by ${r.model || cfg.model}`);
  } catch (e) {
    console.error(`\nPREFLIGHT FAILED — max_tokens=${MAX_TOKENS} rejected for ${cfg.model}:`);
    console.error('  ' + String(e.message || e).slice(0, 400));
    console.error('\nNothing was collected. Re-run with --max-tokens N below the model ceiling.');
    process.exit(1);
  }
}

(async () => {
  process.on('unhandledRejection', e => { console.error(e); process.exit(2); });
  await preflight();
  const only = arg('cond');
  for (let rep = 1; rep <= REPS; rep++)
    for (const c of Object.keys(M.conditions)) if (!only || c === only) await runCondition(c, rep);
  console.log(`\ndone → ${OUT}/`);
})().catch(e => {
  if (e && e.halt) {
    console.error(`\n${'='.repeat(72)}\nRUN HALTED at ${e.label}\n${e.message}\n` +
                  `${'='.repeat(72)}\nEverything already collected is intact. Nothing was redrawn.`);
    process.exit(3);
  }
  console.error(e); process.exit(2);
});
