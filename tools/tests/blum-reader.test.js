const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const R=require('../blum-reader.js');
const base=path.resolve(__dirname,'../../experiments/EXP-003-the-sixth-question');
let count=0;
for(const file of fs.readdirSync(path.join(base,'raw12')).filter(f=>f.endsWith('-W1.json'))){
 const data=JSON.parse(fs.readFileSync(path.join(base,'raw12',file),'utf8')),view=R.adapt(data);
 assert.equal(view.response,data.received);assert.equal(view.sent,data.sent);
 assert.equal(view.sent.length,19);assert.equal(view.sent.at(-1).role,'user');
 const record='raw12/'+file;assert(R.validPath(record));assert.equal(R.sibling(R.sibling(record)),record);
 assert(fs.existsSync(path.join(base,R.sibling(record))));
 if(view.sections.reply)assert(data.received.includes(view.sections.reply));count++;
}
assert.equal(count,24);
assert(!R.validPath('../private.json'));assert(!R.validPath('raw12/../../private.json'));assert(!R.validPath('https://evil.test/x.json'));
assert.equal(R.sections('<reply>unfinished').reply,undefined);
assert.equal(R.sections('<reply>one</reply><reply>two</reply>').reply,undefined);
assert.equal(R.sections('<reply><script>evil</script></reply>').reply,'<script>evil</script>');
assert.throws(()=>R.adapt({sent:[],received:7}));
console.log('24 real W1 contexts and sibling pairs verified; malformed tags and path validation verified.');

const iris=R.adapt(JSON.parse(fs.readFileSync(path.join(base,'raw12/Ha-r3-W1.json'),'utf8')));
const turns=R.turnPairs(iris.sent);assert.equal(turns.length,9);assert.deepEqual(turns.map(t=>[t.user,t.answer]),Array.from({length:9},(_,i)=>[i*2+1,i*2+2]));
assert.equal(R.turnPairs([{role:'user',content:'Measurement'}]).length,0);
assert.equal(R.safeReturn('/tools/blum-evidence.html?question=W1&history=H-r3','https://example.test'),'/tools/blum-evidence.html?question=W1&history=H-r3');
assert.equal(R.safeReturn('https://evil.test/tools/blum-reader.html','https://example.test'),null);
assert.equal(R.safeReturn('/private','https://example.test'),null);
console.log('Nine developmental turn pairs and safe return routes verified.');
