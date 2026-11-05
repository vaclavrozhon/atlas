import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {database} from './sqlite.mjs';
import worker from '../worker.mjs';
import {selectionManifest as manifest} from '../selection-manifest.mjs';

const editor='a'.repeat(64),admin='b'.repeat(64);
const [id,initial]=Object.entries(manifest.cards).find(([,c])=>c.color==='green'&&c.area_options.length===2);
const change=(extra={})=>({problem_id:id,color:'red',area:initial.area,revision:1,version:manifest.version,...extra});
const call=(db,method='GET',body,token,path='/api/selection')=>worker.fetch(new Request('https://notes.example'+path,{
  method,headers:{origin:'https://vaclavrozhon.github.io','content-type':'application/json',...(token?{authorization:'Bearer '+token}:{})},
  ...(body===undefined?{}:{body:JSON.stringify(body)})
}),{DB:db,SELECTION_EDITOR_TOKEN:editor,NOTES_ADMIN_TOKEN:admin});

test('selection writes require the editor key; reads expose neither keys nor individual votes',async()=>{
  const db=database();
  try{
    assert.deepEqual(await (await call(db)).json(),{version:manifest.version,choices:[]});
    for(const token of [undefined,admin,'x',editor.slice(1)])assert.equal((await call(db,'POST',change(),token)).status,403);
    assert.equal((await call(db,'POST',{},editor,'/api/selection/auth')).status,200);
    assert.equal((await call(db,'POST',{},undefined,'/api/selection/auth')).status,403);
    assert.equal((await call(db,'POST',change(),editor)).status,200);
    const result=await (await call(db)).json();
    assert.equal(result.choices.length,1);
    for(const secret of [editor,admin,'voter_hash'])assert(!JSON.stringify(result).includes(secret));
  }finally{db.close();}
});

test('colors and paired moves survive reconnects, preserve manual choices and allow quota deviations',async()=>{
  const dir=await mkdtemp(tmpdir()+'/atlas-selection-');let db=database(dir+'/db');
  try{
    const request=change();
    assert.equal((await call(db,'POST',request,editor)).status,200);
    db.close();db=database(dir+'/db');
    assert.equal((await (await call(db)).json()).choices[0].color,'red');
    // A reader/backend redeploy still sees the override even if the initial
    // editorial proposal is regenerated with the opposite choice.
    const old=initial.color;initial.color='green';
    try{assert.equal((await (await call(db)).json()).choices[0].color,'red');}finally{initial.color=old;}
    const moved=change({area:initial.area_options[1],revision:2});
    assert.equal((await call(db,'POST',moved,editor)).status,200);
    const saved=(await (await call(db)).json()).choices[0];
    assert.equal(saved.area,initial.area_options[1]);assert.equal(saved.color,'red');
    assert.equal((await call(db,'POST',change({color:'green',area:saved.area,revision:3}),editor)).status,200);
    assert.equal((await call(db,'POST',change({color:'green',revision:4}),editor)).status,200);
    // No quota enforcement: all previously red cards in one category can turn green.
    for(const [other,c] of Object.entries(manifest.cards).filter(([,c])=>c.area===initial.area&&c.color==='red'))
      assert.equal((await call(db,'POST',change({problem_id:other,color:'green',area:c.area}),editor)).status,200);
    assert.equal((await call(db,'POST',request,editor)).status,409,'Old retry cannot reverse a newer choice');
  }finally{db.close();await rm(dir,{recursive:true});}
});

test('exact retries are idempotent and concurrent editors cannot silently overwrite one another',async()=>{
  const db=database();
  try{
    await call(db);
    const results=await Promise.all([call(db,'POST',change(),editor),call(db,'POST',change({color:'green'}),editor)]);
    assert.deepEqual(results.map(r=>r.status).sort(),[200,409]);
    const saved=(await (await call(db)).json()).choices[0];
    const retries=await Promise.all(Array.from({length:8},()=>call(db,'POST',change({color:saved.color}),editor)));
    assert(retries.every(r=>r.status===200));
    assert.equal((await (await call(db)).json()).choices[0].revision,1);
    const stale=await call(db,'POST',change({color:saved.color==='green'?'red':'green'}),editor);
    assert.equal(stale.status,409);assert.deepEqual((await stale.json()).choice,saved);
  }finally{db.close();}
});

test('invalid IDs, colors, revisions, a third category and stale manifest versions are rejected',async()=>{
  const db=database();
  try{
    const third=Object.keys(manifest.categories).find(a=>!initial.area_options.includes(a));
    for(const bad of [null,[],change({problem_id:'TCS-99999999'}),change({problem_id:'__proto__'}),change({color:true}),change({color:'blue'}),change({revision:0}),change({revision:1.5}),change({area:third})])
      assert.equal((await call(db,'POST',bad,editor)).status,400);
    assert.equal((await call(db,'POST',change({version:'old'}),editor)).status,409);
    assert.equal((await call(db,'POST',change({revision:9}),editor)).status,409);
    assert.deepEqual((await (await call(db)).json()).choices,[]);
    const [unpaired,c]=Object.entries(manifest.cards).find(([,c])=>c.area_options.length===1);
    assert.equal((await call(db,'POST',change({problem_id:unpaired,area:third===c.area?initial.area:third}),editor)).status,400);
  }finally{db.close();}
});
