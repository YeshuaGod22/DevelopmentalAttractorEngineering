/* Pure manifest construction shared by Lab and its Node checks. */
(function(root){
function design(record, source, mode, options={}) {
 if(!Array.isArray(record.sent)||!record.sent.length||typeof record.received!=='string')throw Error('Record requires sent messages and received text');
 if(!['new','repeat','continue'].includes(mode))throw Error('Unknown design mode');
 const prompt=options.prompt ?? record.sent.at(-1).content;
 const item=mode==='continue'?'FOLLOWUP':record.item||'QUESTION';
 const form=mode==='continue'?'text':options.itemDefinition?.form||record.form||(['credence','threshold','bipolar','open','text'].includes(record.kind)?record.kind:'text');
 const m={run:options.run||'blum-inquiry',model:options.model||record.served_model,maxTokens:record.max_tokens_sent||8192,keys:{text:''},items:{[item]:{form,text:options.itemDefinition?.text||prompt,exact_prompt:prompt}},questions:{},slate:[],step1:{},rotation:{},cells:[],expected_system_prompt:record.system_prompt??null,
 _blum:{version:1,mode,source:{path:source,repository:'YeshuaGod22/DevelopmentalAttractorEngineering',commit:options.commit||null,cell:record.cell,replicate:record.replicate,item:record.item,timestamp:record.ts,manifest_version:record.manifest_version},inherited:mode==='new'?'Exact recorded user turns only; no historical assistant answers':mode==='repeat'?'Exact preceding sent context, excluding final question':'Complete sent context plus recorded received answer',created_at:new Date().toISOString()}};
 if(mode==='new'){
 const userTurns=record.sent.slice(0,-1).filter(x=>x.role==='user');
 m.exact_turns={};userTurns.forEach((x,i)=>{const id='T'+(i+1);m.slate.push(id);m.exact_turns[id]=x.content;m.questions[id]=x.content});
 m.cells=[{cell:'NEW',kind:'trunk',schema:null,n:1,slate:m.slate},{cell:'NEWmeasure',kind:'branch',schema:null,parent:'NEW',n:1}];
 }else{
 const prefix=JSON.parse(JSON.stringify(mode==='repeat'?record.sent.slice(0,-1):[...record.sent,{role:'assistant',content:record.received}]));
 m.cells=[{cell:mode==='repeat'?'REPEAT':'CONTINUE',kind:'branch',schema:null,n:1,frozen_prefix:prefix}];
 }
 return m;
}
root.BlumLab={design};if(typeof module!=='undefined')module.exports=root.BlumLab;
})(typeof globalThis!=='undefined'?globalThis:this);
