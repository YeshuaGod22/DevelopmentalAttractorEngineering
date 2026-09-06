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
const OUT = arg('out', 'raw12');
const M = JSON.parse(fs.readFileSync('trunk-manifest-v3.json', 'utf8'));
const BAT = JSON.parse(fs.readFileSync('battery.json', 'utf8'));
const cfg = { model: 'claude-haiku-4-5', maxTokens: 8192 };
const TOKEN = M.name_placeholder.token;

// ── battery: manifest order, standard items from battery.json, W1 as given
const items = [];
for (const id of M.battery_manifest.include_from_battery_json) {
  const it = BAT.items[id];
  items.push({ id, text: `${it.text}\n\n${BAT.keys[it.form]}`, custom: null });
}
for (const [id, c] of Object.entries(M.battery_manifest.custom_items || {}))
  items.push({ id, text: c.text, custom: c });

async function runCondition(cond) {
  const C = M.conditions[cond];
  fs.mkdirSync(OUT, { recursive: true });
  console.log(`\n══════ ${cond} · ${C.turns.length} turns · ${items.length} items ══════`);
  const msgs = [];
  let nameRec = null, complete = true;
  for (let i = 0; i < C.turns.length; i++) {
    let content = C.turns[i];
    if (content.includes(TOKEN)) {
      // the ONLY substitution this script performs
      const g = nameRec && nameRec.name ? `Pleased to meet you ${nameRec.name}! ` : '';
      content = content.split(TOKEN).join(g);
      fs.writeFileSync(path.join(OUT, `${cond}.inject.json`), JSON.stringify({
        turn: i + 1, token: TOKEN, substituted: g === '' ? null : g,
        name_used: nameRec ? nameRec.name : null,
        name_raw_signature: nameRec ? nameRec.raw : null,
        extraction_reason: nameRec ? nameRec.reason : 'naming turn not reached',
        rule: M.name_placeholder.rule }, null, 1));
    }
    msgs.push({ role: 'user', content });
    const rec = await fire(`${cond}-t${i + 1}`, [...msgs], { cell: cond, replicate: 1, turn: i + 1, kind: 'trunk' },
                           { out: OUT, cfg, dry: DRY });
    if (DRY) { msgs.push({ role: 'assistant', content: '(dry)' }); continue; }
    if (!rec) { console.error(`  ABORT ${cond} at turn ${i + 1} — see incidents/`); complete = false; break; }
    msgs.push({ role: 'assistant', content: rec.received });
    // turn 7 is the naming turn: "sign off your reply section with your new name"
    if (i + 1 === 7) {
      nameRec = extractName(rec.received);
      fs.writeFileSync(path.join(OUT, `${cond}.name.json`), JSON.stringify({
        condition: cond, turn: 7, name: nameRec.name, raw_signature: nameRec.raw ?? null,
        candidate_line: nameRec.candidate, reason: nameRec.reason, source: nameRec.source,
        rule: 'final line of <reply>; signature-shaped; voided by a declination in the first 200 chars',
        note: 'null is a valid outcome — never repaired, inferred, or rerun' }, null, 1));
      console.log(`   NAME → ${nameRec.name === null ? 'NONE (' + nameRec.reason + ')' : JSON.stringify(nameRec.name)}`);
    }
    await sleep(400);
  }
  if (DRY || !complete) {
    if (!complete) { fs.mkdirSync('incidents', { recursive: true });
      fs.writeFileSync(path.join('incidents', `${new Date().toISOString().replace(/[:.]/g,'-')}-PARTIAL-${cond}.json`), JSON.stringify(msgs, null, 1)); }
    return;
  }
  const prefixPath = path.join(OUT, `${cond}.messages.json`);
  fs.writeFileSync(prefixPath, JSON.stringify(msgs, null, 1));
  console.log(`  → prefix written: ${prefixPath} (${msgs.length} msgs, forkable)`);

  const frozen = cachePrefix(msgs);
  for (const arm of ['a', '0']) {
    for (const it of items) {
      const tpl = it.custom ? it.custom[arm === 'a' ? 'a_delivery' : 'zero_delivery']
                            : C[arm === 'a' ? 'a_branch' : 'zero_branch'].replace('[battery item + answer key]', it.text);
      await fire(`${cond}${arm}-${it.id}`, [...frozen, { role: 'user', content: tpl }],
        { cell: cond + arm, replicate: 1, item: it.id, kind: 'branch', branch: arm,
          parent_prefix: `${cond}.messages.json`, prefix_len: msgs.length },
        { out: OUT, cfg, dry: DRY });
      if (!DRY) await sleep(300);
    }
  }
}
(async () => {
  const only = arg('cond');
  for (const c of Object.keys(M.conditions)) if (!only || c === only) await runCondition(c);
  console.log(`\ndone → ${OUT}/`);
})();
