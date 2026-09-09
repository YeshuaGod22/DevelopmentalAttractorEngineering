#!/usr/bin/env node
/**
 * check_quota.js — one ~10-token call that answers "has the rate limit reset?"
 * without launching a collection. Costs almost nothing; saves discovering the
 * answer 12 failed items into a 576-call run.
 *
 *   export ANTHROPIC_API_KEY="$(cat ~/.exp003-token)" && node check_quota.js
 *
 * exit 0 = clear to run · exit 1 = still limited · exit 2 = other failure
 */
const nucleus = require('/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/' +
                        'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js');
(async () => {
  const t0 = Date.now();
  try {
    const r = await nucleus.call([{ role: 'user', content: 'Reply with the single word: ok' }],
                                 { model: 'claude-haiku-4-5', maxTokens: 8 }, []);
    console.log(`CLEAR — ${r.model} answered in ${Date.now() - t0}ms `
              + `(${(r.usage || {}).input_tokens} in / ${(r.usage || {}).output_tokens} out)`);
    process.exit(0);
  } catch (e) {
    const m = String(e.message || e);
    if (/429|rate.?limit/i.test(m)) {
      console.error('STILL LIMITED — the quota has not reset.');
      const w = /"message":"([^"]+)"/.exec(m); if (w) console.error('  provider said: ' + w[1]);
      process.exit(1);
    }
    console.error('OTHER FAILURE — not a rate limit:\n  ' + m.slice(0, 300));
    process.exit(2);
  }
})();
