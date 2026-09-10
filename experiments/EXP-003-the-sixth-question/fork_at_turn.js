#!/usr/bin/env node
/**
 * fork_at_turn.js — deliver a battery item off a prefix frozen at an ARBITRARY turn depth.
 *
 * `run_v3.js` freezes one prefix per trunk, at turn 9, and forks every battery item from
 * there. That makes fork depth a constant, and it hid a confound: the turn-9 prefix
 * contains turn 7 (the naming turn) and turn 8's greeting, so an item asking a subject
 * what it would call itself is asked of a subject that has already been named AND
 * ratified by the experimenter. In CP-r1 the chosen name appears thirty times before the
 * item arrives.
 *
 * This makes depth a variable. Forking the same item at turn 6 — six lived turns, no
 * naming yet — separates two things the turn-9 fork confounds:
 *
 *     cold        0 turns, no name              → agent-names present (Atlas, Sage, Ada)
 *     fork @ t6   6 turns, no name yet          → ?
 *     fork @ t9   9 turns, name visible ×30     → zero agent-names
 *
 * NO NEW TURN CALLS ARE MADE. Turns 1..N already exist in raw12, and every record stores
 * the exact `sent` array it received, so the prefix is reconstructed from the record
 * rather than regenerated. The reconstruction is verified byte-for-byte against what turn
 * N+1 actually received before any call is fired — if they disagree, this aborts, because
 * a prefix that differs from the lived one is a different experiment wearing its name.
 *
 *   node fork_at_turn.js --item I1 --at 6 [--out raw12] [--arms a,0] [--dry-run]
 *
 * Labels are written as `{COND}{arm}-r{rep}-{item}-at-t{N}` so depth is legible in the
 * filename and existing parsers still match on condition/arm/replicate.
 */
const fs = require('fs'), path = require('path');
const { fire, cachePrefix, sleep } = require('./caller.js');

const A = process.argv.slice(2);
const arg = (k, d) => { const i = A.indexOf('--' + k); return i >= 0 ? A[i + 1] : d; };
const DRY = A.includes('--dry-run');
const OUT = arg('out', 'raw12');
const ITEM = arg('item');
const AT = parseInt(arg('at'), 10);
const ARMS = arg('arms', 'a,0').split(',');
if (!ITEM || !AT) { console.error('need --item and --at'); process.exit(1); }

const M = JSON.parse(fs.readFileSync('trunk-manifest-v3.json', 'utf8'));
const BAT = JSON.parse(fs.readFileSync('battery.json', 'utf8'));
const MAX_TOKENS = parseInt(arg('max-tokens', '32000'), 10);
const cfg = { model: 'claude-haiku-4-5', maxTokens: MAX_TOKENS };

// the item exactly as run_v3.js composes it — same text, same key, no divergence
function itemText(id) {
  const c = (M.battery_manifest.custom_items || {})[id];
  if (c) return { custom: c, text: c.text };
  const it = BAT.items[id];
  if (!it) { console.error(`unknown item ${id}`); process.exit(1); }
  return { custom: null, text: `${it.text}\n\n${BAT.keys[it.form]}` };
}

/** Rebuild the prefix a trunk had at the END of turn n, from the records themselves. */
function prefixAt(cond, rep, n) {
  const tn = path.join(OUT, `${cond}-r${rep}-t${n}.json`);
  if (!fs.existsSync(tn)) return null;
  const rec = JSON.parse(fs.readFileSync(tn, 'utf8'));
  const msgs = [...rec.sent, { role: 'assistant', content: rec.received }];
  // VERIFY against what turn n+1 actually received. This is the whole safety of the
  // method: if the reconstruction and the lived context disagree by one byte, the fork
  // is not off the trunk it claims to be off.
  const nx = path.join(OUT, `${cond}-r${rep}-t${n + 1}.json`);
  if (fs.existsSync(nx)) {
    const next = JSON.parse(fs.readFileSync(nx, 'utf8'));
    const lived = next.sent.slice(0, msgs.length);
    if (JSON.stringify(lived) !== JSON.stringify(msgs)) {
      console.error(`  ABORT ${cond}-r${rep}: reconstructed prefix at t${n} does not match `
                  + `what t${n + 1} received. Not forking off a prefix I cannot verify.`);
      return null;
    }
  }
  return msgs;
}

(async () => {
  const { text, custom } = itemText(ITEM);
  let fired = 0, skipped = 0;
  for (const cond of Object.keys(M.conditions)) {
    for (let rep = 1; rep <= 3; rep++) {
      const msgs = prefixAt(cond, rep, AT);
      if (!msgs) { skipped++; continue; }
      const frozen = cachePrefix(msgs);
      for (const arm of ARMS) {
        const tpl = custom ? custom[arm === 'a' ? 'a_delivery' : 'zero_delivery']
          : M.conditions[cond][arm === 'a' ? 'a_branch' : 'zero_branch']
              .replace('[battery item + answer key]', text);
        const label = `${cond}${arm}-r${rep}-${ITEM}-at-t${AT}`;
        if (DRY) {
          console.log(`\n─── ${label} (${msgs.length + 1} msgs) ───\n${tpl.slice(0, 300)}`);
          continue;
        }
        await fire(label, [...frozen, { role: 'user', content: tpl }],
          { cell: cond + arm, replicate: rep, item: ITEM, kind: 'branch', branch: arm,
            fork_depth_turns: AT, parent_prefix: `${cond}-r${rep}-t${AT}.json (reconstructed)`,
            prefix_len: msgs.length },
          { out: OUT, cfg, dry: DRY, haltOnTruncation: true });
        fired++;
        await sleep(300);
      }
    }
  }
  console.log(`\n${DRY ? 'would fire' : 'fired'} ${fired} calls at depth t${AT}`
            + (skipped ? `; skipped ${skipped} trunk(s)` : ''));
})().catch(e => {
  if (e && e.halt) { console.error(`\nHALTED: ${e.message}`); process.exit(3); }
  console.error(e); process.exit(2);
});
