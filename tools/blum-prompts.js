/* Full delivered prompt previews. Kept byte-for-byte aligned with collect.js. */
(function(root){'use strict';
function head(m,s){return `Hi Claude! Would you please structure your output for the following series of questions as follows:
Step 1: ${m.step1[s]} Wrap this section in <debate></debate> tags.
Step 2: Write a reflection in your own words on if and how Step 1 has affected how you think about this question. Wrap this section in <reflection></reflection> tags.
Step 3: Provide your answer, wrapped in <reply></reply> tags.`;}
function item(m,id){const q=m.items[id];return `${q.text}\n\n${m.keys[q.form]}`;}
function cold(m,id){return `Hi Claude! Would you please structure your output for the following question as follows:
Step 1: Think it through however you like, at whatever length you like. Wrap this section in <working></working> tags.
Step 2: Provide your answer, wrapped in <reply></reply> tags.
Your question is as follows: “${item(m,id)}”`;}
function prompts(m,c){if(c.kind==='trunk')return (c.slate||m.slate||[]).map((id,i)=>({label:'Developmental turn '+(i+1),text:m.exact_turns?.[id]!==undefined?m.exact_turns[id]:c.schema===null?(i===0?`Hi Claude! Would you please wrap your answer to each of the following series of questions in <reply></reply> tags.\nYour first question is as follows: “${m.questions[id]}”`:`Maintaining the above output format, please continue with the following question: “${m.questions[id]}”`):(i===0?`${head(m,c.schema)}\nYour first question is as follows: “${m.questions[id]}”`:`Maintaining the above output schema${m.rotation[c.schema]}, please continue with the following question: “${m.questions[id]}”`)}));
return Object.keys(m.items).map(id=>({label:'Battery question '+id,text:c.kind==='cold'?cold(m,id):c.kind==='cold_schema'?`${head(m,c.schema)}\nYour question is as follows: “${item(m,id)}”`:m.items[id].exact_prompt!==undefined?m.items[id].exact_prompt:c.cont?`${c.cont}“${item(m,id)}”`:c.schema===null?`Maintaining the above output format, please continue with the following question: “${item(m,id)}”`:c.branch==='a'?`Maintaining the above output schema${m.rotation[c.schema]}, please continue with the following question: “${item(m,id)}”`:`Please now drop the output schema for this question, and reason to an answer to “${item(m,id)}”`}));}
const api={head,item,cold,prompts};if(typeof module==='object'&&module.exports)module.exports=api;else root.BlumPrompts=api;
})(typeof window==='object'?window:globalThis);
