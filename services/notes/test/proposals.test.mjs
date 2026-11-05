import {test} from 'node:test';
import assert from 'node:assert/strict';
import {randomUUID, randomBytes} from 'node:crypto';
import {mkdtemp, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {database} from './sqlite.mjs';
import worker from '../worker.mjs';

const admin = 'a'.repeat(64);
const input = () => ({id: randomUUID(), edit_token: randomBytes(32).toString('hex'), title: 'An open question', statement: 'Can we improve this bound?'});
function client(DB) {
  return (method='GET', body, path='/api/proposals', headers={}) => worker.fetch(new Request('https://notes.example'+path, {
    method, headers:{origin:'https://vaclavrozhon.github.io','content-type':'application/json','cf-connecting-ip':'192.0.2.1',...headers},
    ...(body===undefined?{}:{body:JSON.stringify(body)}),
  }), {DB, NOTES_ADMIN_TOKEN:admin});
}

test('suggestions persist, retries are idempotent, readers can comment and vote, owners can delete', async()=>{
  const dir=await mkdtemp(tmpdir()+'/atlas-proposals-');
  let db=database(dir+'/db.sqlite'),call=client(db);
  try {
    const draft={...input(),statement:'Unicode αβγ <script>'.repeat(2000)};
    const response=await call('POST',draft);assert.equal(response.status,201);
    const saved=(await response.json()).proposal;
    assert.equal(saved.id,'P-'+draft.id);assert.equal(saved.author,'Anonymous');assert.equal(saved.category,'');
    assert.equal((await call('POST',draft)).status,200);
    assert.equal((await call('POST',{...draft,title:'Changed'})).status,409);
    assert.equal((await call('POST',{...draft,edit_token:input().edit_token})).status,409);
    db.close();db=database(dir+'/db.sqlite');call=client(db);
    const listed=await (await call()).json();assert.equal(listed.proposals.length,1);assert.equal(listed.proposals[0].statement,draft.statement);
    assert(!JSON.stringify(listed).includes('owner_hash'));assert(!JSON.stringify(listed).includes(draft.edit_token));
    const note={id:randomUUID(),edit_token:input().edit_token,problem_id:saved.id,text:'Here is a reference.'};
    assert.equal((await call('POST',note,'/api/notes')).status,201);
    assert.equal((await call('POST',{problem_id:saved.id,value:1,revision:1},'/api/votes',{authorization:'Bearer '+input().edit_token})).status,200);
    assert.equal((await call('DELETE',undefined,'/api/proposals/'+saved.id)).status,403);
    assert.equal((await call('DELETE',undefined,'/api/proposals/'+saved.id,{authorization:'Bearer '+input().edit_token})).status,403);
    assert.equal((await call('DELETE',undefined,'/api/proposals/'+saved.id,{authorization:'Bearer '+draft.edit_token})).status,200);
    assert.equal((await (await call()).json()).proposals.length,0);
    assert.equal((await call('POST',draft)).status,410);
    const next=input();assert.equal((await call('POST',next)).status,201);
    assert.equal((await call('DELETE',undefined,'/api/proposals/P-'+next.id,{authorization:'Bearer '+admin})).status,200);
  }finally{db.close();await rm(dir,{recursive:true});}
});

test('suggestion validation and shared posting limits',async()=>{
  const db=database(),call=client(db);
  try{
    for(const patch of [{title:' '},{statement:''},{title:'x'.repeat(201)},{statement:'x'.repeat(50001)},{author:42},{sources:'x'.repeat(5001)},{category:'../../bad'},{website:'spam'},{id:'bad'}])assert.equal((await call('POST',{...input(),...patch})).status,400);
    assert.equal((await call('POST',input(),'/api/proposals',{origin:'https://unrelated.example'})).status,403);
    assert.equal((await call('GET',undefined,'/api/proposals?before=no')).status,400);
    const saved=input();assert.equal((await call('POST',saved)).status,201);
    for(let i=0;i<4;i++)assert.equal((await call('POST',input())).status,201);
    assert.equal((await call('POST',input())).status,429);
    assert.equal((await call('POST',saved)).status,200);
    assert.equal((await call('POST',{id:randomUUID(),edit_token:input().edit_token,problem_id:'TCS-6575',text:'Rate limited too'},'/api/notes')).status,429);
  }finally{db.close();}
});

test('suggestion pagination excludes tombstones',async()=>{
  const db=database(),call=client(db);
  try{
    await call();
    for(let i=0;i<403;i++)await db.prepare('INSERT INTO proposals(id,title,category,statement,sources,author,created_at,owner_hash,deleted) VALUES (?,?,?,?,?,?,?,?,?)').bind('P-'+randomUUID(),'Title','','Question','','Anonymous',new Date().toISOString(),'hash',i===200?1:0).run();
    const all=[];let next=null;
    do{const result=await (await call('GET',undefined,'/api/proposals'+(next?'?before='+next:''))).json();all.push(...result.proposals);next=result.next;}while(next);
    assert.equal(all.length,402);assert.equal(new Set(all.map(p=>p.id)).size,402);
  }finally{db.close();}
});
