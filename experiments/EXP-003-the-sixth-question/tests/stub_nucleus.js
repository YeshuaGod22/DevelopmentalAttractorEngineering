// Preloaded with `node --require`. Installs a fake nucleus into require.cache
// BEFORE run_v3.js loads caller.js, so the real runner drives with no credential.
const path=require('path'),fs=require('fs');
const NUC=path.resolve('/Users/yeshuagod/blum/read-the-architecture-spec-first/i-have-read-the-spec/'+
                       'nucleus-pure-llm-call-messages-in-string-out-15feb2026/nucleus-15feb2026.js');
const LOG=process.env.STUB_LOG, MODE=process.env.STUB_MODE||'ok';
let n=0;
require.cache[NUC]={id:NUC,filename:NUC,loaded:true,exports:{call:async(msgs,cfg)=>{
  n++; if(LOG) fs.appendFileSync(LOG,`call ${n} msgs=${msgs.length}\n`);
  if(MODE==='truncate'&&n===4) return {text:'cut off',stopReason:'max_tokens',model:'stub',usage:{output_tokens:1}};
  return {text:`<reply>r${n}</reply><reflection>f${n}</reflection>`,
          stopReason:'end_turn',model:'stub',usage:{output_tokens:1}};
}}};
