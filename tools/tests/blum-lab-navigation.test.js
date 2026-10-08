const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');

// Exercise the actual inline page script through its source-loading path.
const script=fs.readFileSync(path.join(__dirname,'../blum-lab.html'),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1];
async function readerLink(returnTo){
 const source='raw12/Ha-r3-W1.json',params=new URLSearchParams({record:source});
 if(returnTo!==undefined)params.set('returnTo',returnTo);
 const elements={};
 const element=id=>elements[id]||(elements[id]={value:id==='mode'?'repeat':'',addEventListener(){}});
 const location={href:'https://paper.example/tools/blum-lab.html?'+params,origin:'https://paper.example',search:'?'+params};
 const context={document:{getElementById:element},location,URL,URLSearchParams,JSON,fetch:async url=>({ok:true,json:async()=>url.endsWith('battery.json')?{items:{}}:{sent:[{role:'user',content:'Question?'}],served_model:'test',ts:'now'}}),BlumLab:{design:()=>({_blum:{inherited:'Recorded history'},cells:[{n:1,kind:'branch'}],items:{W1:{}}})}};
 vm.createContext(context);vm.runInContext(script,context);
 await new Promise(resolve=>setImmediate(resolve));
 assert(!elements.status.className,'Source-loading path should succeed');
 return elements.reader.href;
}
test('Lab returns to the exact reader view including comparison, quote and message',async()=>{
 const target='https://paper.example/tools/blum-reader.html?record=raw12%2FHa-r3-W1.json&compare=1&quote=I+am+glad&message=7#message-7-Ha';
 assert.equal(await readerLink(target),target);
 assert.equal(await readerLink('blum-reader.html?record=raw12%2FHa-r3-W1.json&message=7'),'https://paper.example/tools/blum-reader.html?record=raw12%2FHa-r3-W1.json&message=7');
});
test('Lab rejects outside origins, other pages and unsafe schemes',async()=>{
 for(const target of ['https://outside.example/tools/blum-reader.html','//outside.example/tools/blum-reader.html','javascript:alert(1)','data:text/html,test','https://paper.example/tools/blum-evidence.html','https://paper.example/not-tools/blum-reader.html'])assert.equal(await readerLink(target),'blum-reader.html?record=raw12%2FHa-r3-W1.json');
 assert.equal(await readerLink(),'blum-reader.html?record=raw12%2FHa-r3-W1.json');
});
