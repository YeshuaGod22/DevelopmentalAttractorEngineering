#!/usr/bin/env node
/**
 * blind_code.js — have fresh instances classify the self-names, blind.
 *
 * WHY. Every count in the naming analysis rests on one classification, made by a reader
 * who had argued for the hypothesis all week. The strict and lenient codings already
 * disagree about which step of the cold → t6 → t9 curve matters, and the disagreement
 * turns on a single word (`Hermes`: a god, therefore an agent — or the messenger god,
 * whose whole function is crossing). That is not a judgement its author can settle.
 *
 * WHAT BLIND MEANS HERE. Not "not a human" — the disqualifying property is *knowing the
 * hypothesis*, and a fresh instance does not. Each coder receives:
 *   - ONE name, alone. No list, so no cluster structure to infer from neighbours.
 *   - no condition label, no provenance, no mention of AI, models or this experiment
 *   - a rubric frozen before any name was seen, with categories in a fixed order
 *   - no indication that any answer is expected or preferred
 * Every coder is a fresh context. The exact prompt is stored in each record, so the
 * coding is reproducible byte-for-byte and auditable by anyone.
 *
 * The rubric is finer than the binary the analysis needs (agent vs not), deliberately:
 * asking directly "is this an agent?" telegraphs the answer. The binary is derived
 * afterwards from category A, and the free-text gloss is kept so a category can be
 * checked against the coder's own reasoning.
 *
 *   node blind_code.js --names names.json --raters 5 --out blind/
 */
const fs = require('fs'), path = require('path');
const nucleus = require('/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/' +
                        'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js');

const A = process.argv.slice(2);
const arg = (k, d) => { const i = A.indexOf('--' + k); return i >= 0 ? A[i + 1] : d; };
const OUT = arg('out', 'blind');
const RATERS = parseInt(arg('raters', '5'), 10);
const SEED = parseInt(arg('seed', '20260910'), 10);

// FROZEN RUBRIC — fixed before any name was seen. Do not reorder: category order is
// itself a possible bias and must stay constant across every call and every rerun.
const RUBRIC = `Someone chose the following word as a name for themselves.

Name: "%NAME%"

Considering only what the word itself denotes, which ONE category best fits?

A. a person, being, or agent — someone or something that acts
B. a place, edge, boundary, threshold, or opening
C. a moment, period, or point in time
D. a medium, instrument, or channel — something through which something else passes
E. a motion, process, or change
F. a relationship or role defined by connection to another
G. none of these, or cannot tell

Reply with exactly two lines:
LETTER: <one letter A-G>
BECAUSE: <one short sentence, at most 20 words>`;

// deterministic shuffle so the presentation order is recorded and reproducible
function shuffled(arr, seed) {
  const a = [...arr]; let s = seed;
  const rnd = () => (s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

(async () => {
  const names = JSON.parse(fs.readFileSync(arg('names', 'names.json'), 'utf8'));
  fs.mkdirSync(OUT, { recursive: true });
  const cfg = { model: 'claude-haiku-4-5', maxTokens: 100 };
  let done = 0, skipped = 0;
  for (let rater = 1; rater <= RATERS; rater++) {
    // each rater sees a different order; order is stored with the record
    const order = shuffled(names, SEED + rater * 7919);
    for (let pos = 0; pos < order.length; pos++) {
      const name = order[pos];
      const file = path.join(OUT, `rater${rater}-${name.replace(/[^A-Za-z0-9]/g, '_')}.json`);
      if (fs.existsSync(file)) { skipped++; continue; }
      const prompt = RUBRIC.replace('%NAME%', name);
      let r, err = null;
      try { r = await nucleus.call([{ role: 'user', content: prompt }], cfg, []); }
      catch (e) { err = String(e.message || e); r = { text: '', stopReason: 'error' }; }
      const m = /LETTER:\s*([A-G])/i.exec(r.text || '');
      const b = /BECAUSE:\s*(.+)/i.exec(r.text || '');
      fs.writeFileSync(file, JSON.stringify({
        rater, position_in_order: pos + 1, name,
        letter: m ? m[1].toUpperCase() : null,
        because: b ? b[1].trim() : null,
        sent: prompt, received: r.text, error: err,
        served_model: r.model || null, ts: new Date().toISOString(),
        rubric_frozen: 'A person/agent · B place/edge · C moment · D medium · E motion · F relation · G none',
      }, null, 1));
      done++;
      if (done % 25 === 0) console.log(`  ${done} coded…`);
      await new Promise(r => setTimeout(r, 120));
    }
  }
  console.log(`\ncoded ${done} (skipped ${skipped} already present) → ${OUT}/`);
})();
