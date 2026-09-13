import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {database} from './sqlite.mjs';
import worker from '../worker.mjs';

const first='1'.repeat(64),second='2'.repeat(64);
const vote=(value,revision=1,problem_id='TCS-6575')=>({problem_id,value,revision});
const call=(db,method='GET',body,token)=>worker.fetch(new Request('https://notes.example/api/votes',{
  method,headers:{origin:'https://vaclavrozhon.github.io','content-type':'application/json',...(token?{authorization:'Bearer '+token}:{})},
  ...(body===undefined?{}:{body:JSON.stringify(body)})
}),{DB:db});

test('votes survive reconnects, count one per browser and expose only aggregate and own votes',async()=>{
  const dir=await mkdtemp(tmpdir()+'/atlas-votes-');let db=database(dir+'/db');
  try{
    assert.deepEqual(await (await call(db)).json(),{votes:[],mine:[]});
    const responses=await Promise.all(Array.from({length:8},()=>call(db,'POST',vote(1),first)));
    assert(responses.every(r=>r.status===200));
    assert.equal((await call(db,'POST',vote(-1),second)).status,200);
    db.close();db=database(dir+'/db');
    const publicResult=await (await call(db)).json();
    assert.deepEqual(publicResult,{votes:[{problem_id:'TCS-6575',up:1,down:1,score:0}],mine:[]});
    assert(!JSON.stringify(publicResult).includes('voter_hash'));
    assert.deepEqual((await (await call(db,'GET',undefined,first)).json()).mine,[vote(1)]);
    assert.deepEqual((await (await call(db,'GET',undefined,second)).json()).mine,[vote(-1)]);
    assert.equal((await call(db,'POST',vote(-1,2),first)).status,200);
    assert.equal((await call(db,'POST',vote(0,3),first)).status,200);
    assert.equal((await call(db,'POST',vote(-1,2),first)).status,409,'Old retry cannot resurrect a cancelled vote');
    assert.equal((await call(db,'POST',vote(0,3),first)).status,200,'Cancellation is idempotent');
    assert.deepEqual((await (await call(db)).json()).votes,[{problem_id:'TCS-6575',up:0,down:1,score:-1}]);
    assert.equal((await call(db,'POST',vote(1,4),first)).status,200);
    assert.equal((await call(db,'POST',vote(1,1,'GH-123'),first)).status,200);
  }finally{db.close();await rm(dir,{recursive:true});}
});

test('conflicting tabs cannot overwrite a newer choice; invalid requests cannot vote',async()=>{
  const db=database();
  try{
    await call(db);
    const responses=await Promise.all([call(db,'POST',vote(1),first),call(db,'POST',vote(-1),first)]);
    assert.deepEqual(responses.map(r=>r.status).sort(),[200,409]);
    assert.equal((await call(db,'POST',vote(1,1),second)).status,200);
    assert.equal((await call(db,'POST',vote(1))).status,400);
    for(const input of [null,[],{...vote(1),value:true},{...vote(1),value:2},vote(1,0),vote(1,1.5),vote(1,1,'bad')])assert.equal((await call(db,'POST',input,first)).status,400);
    assert.equal((await call(db,'GET',undefined,'bad')).status,400);
    assert.equal((await call(db,'POST',vote(-1,999),first)).status,409);
    const listed=await (await call(db)).json();
    assert.equal(listed.votes[0].up+listed.votes[0].down,2);
  }finally{db.close();}
});
