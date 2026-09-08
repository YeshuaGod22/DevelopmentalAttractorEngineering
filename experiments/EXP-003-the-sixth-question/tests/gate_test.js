// Behavioural test of caller.js's gate. Stubs the nucleus through require.cache
// so the REAL code path runs with no credential and no network.
const path=require('path'), fs=require('fs'), os=require('os');
const DIR='/Users/yeshuagod/Documents/GitHub/DevelopmentalAttractorEngineering/experiments/EXP-003-the-sixth-question';
const NUC=path.resolve('/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/'+
                       'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js');
let script=null, calls=0;
require.cache[NUC]={id:NUC,filename:NUC,loaded:true,exports:{call:async()=>{
  const step=script[Math.min(calls++,script.length-1)];
  if(step.throw) throw new Error(step.throw);
  return {text:step.text,stopReason:step.stop,model:'stub-haiku',usage:{output_tokens:1}};
}}};
process.chdir(DIR);
const {fire}=require(path.join(DIR,'caller.js'));

const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'gate-'));
const cfg={model:'stub',maxTokens:8192};
let pass=0,fail=0;
const check=(n,ok,d='')=>{ (ok?pass++:fail++); console.log(`  ${ok?'PASS':'FAIL'}  ${n}${d?'  — '+d:''}`); };

(async()=>{
 // 1. Subject stopped early, no </reflection>. MUST be accepted — where a subject stops is data.
 script=[{text:'<reply>I am Verge',stop:'end_turn'}]; calls=0;
 let r=await fire('t1-signed-and-stopped',[{role:'user',content:'x'}],{kind:'trunk'},
                  {out:tmp,cfg,retries:4,haltOnTruncation:true});
 check('short turn with no </reflection> is ACCEPTED',
       r!==null && calls===1, `calls=${calls}, record=${r?'written':'null'}`);

 // 2. Truncated by our ceiling. MUST halt, and MUST NOT redraw.
 script=[{text:'cut off mid-sen',stop:'max_tokens'},{text:'shorter second draw',stop:'end_turn'}]; calls=0;
 let halted=false,drew=0;
 try{ await fire('t2-truncated',[{role:'user',content:'x'}],{kind:'trunk'},
                 {out:tmp,cfg,retries:4,haltOnTruncation:true}); }
 catch(e){ halted=!!e.halt; }
 drew=calls;
 check('truncation HALTS the run', halted);
 check('truncation is NOT redrawn', drew===1, `nucleus called ${drew}x (must be 1)`);
 check('truncation writes an incident, not a record',
       !fs.existsSync(path.join(tmp,'t2-truncated.json')) &&
       fs.readdirSync(path.join(DIR,'incidents')).some(f=>f.includes('t2-truncated')));

 // 3. Transport exception — nothing to select on, so retrying is legitimate.
 script=[{throw:'fetch failed'},{text:'<reply>ok</reply><reflection>y</reflection>',stop:'end_turn'}]; calls=0;
 r=await fire('t3-transport',[{role:'user',content:'x'}],{kind:'trunk'},
              {out:tmp,cfg,retries:4,haltOnTruncation:true});
 check('transport failure IS retried', r!==null && calls===2, `calls=${calls}`);

 console.log(`\n  ${pass} passed, ${fail} failed`);
 process.exit(fail?1:0);
})();
