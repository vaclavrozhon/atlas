import {test} from 'node:test';
import assert from 'node:assert/strict';
import {randomBytes, randomUUID} from 'node:crypto';
import {mkdtemp, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {database} from './sqlite.mjs';
import worker from '../worker.mjs';

const admin = randomBytes(32).toString('hex');
const input = () => ({id: randomUUID(), edit_token: randomBytes(32).toString('hex'), problem_id: 'TCS-6575', text: 'An observation: řetězec <script>.'});
function client(DB, collection = 'notes') {
  return (method = 'GET', body, path = '/api/'+collection, headers = {}) => worker.fetch(new Request('https://notes.example'+path, {
    method, headers: {origin: 'https://vaclavrozhon.github.io', 'content-type': 'application/json', 'cf-connecting-ip': '192.0.2.1', ...headers},
    ...(body === undefined ? {} : {body: JSON.stringify(body)}),
  }), {DB, NOTES_ADMIN_TOKEN: admin});
}

for (const collection of ['notes', 'comments']) {
const endpoint = '/api/'+collection;
const table = collection === 'comments' ? 'public_comments' : 'notes';
test(collection + ': durable public notes, retry safety and author/admin deletion', async () => {
  const dir = await mkdtemp(tmpdir()+'/atlas-notes-test-');
  let db = database(dir+'/notes.sqlite'); let call = client(db, collection);
  try {
    const note = input();
    assert.equal((await call('OPTIONS')).status, 204);
    const posted = await call('POST', note);
    assert.equal(posted.status, 201);
    assert.equal(posted.headers.get('access-control-allow-origin'), 'https://vaclavrozhon.github.io');
    assert.equal((await posted.json()).note.author, 'Anonymous');
    assert.equal((await call('POST', note)).status, 200);
    assert.equal((await call('POST', {...note, text: 'Different'})).status, 409);
    assert.equal((await call('POST', {...note, edit_token: randomBytes(32).toString('hex')})).status, 409);
    db.close(); db = database(dir+'/notes.sqlite'); call = client(db, collection);
    const listed = await (await call()).json();
    assert.equal(listed.notes.length, 1, 'Survives a new process/database connection without duplication');
    assert.equal(listed.notes[0].text, note.text);
    assert(!JSON.stringify(listed).includes(note.edit_token));
    assert(!JSON.stringify(listed).includes('owner_hash'));
    assert.equal((await call('DELETE', undefined, endpoint+'/'+note.id)).status, 403);
    assert.equal((await call('DELETE', undefined, endpoint+'/'+note.id, {authorization: 'Bearer '+input().edit_token})).status, 403);
    assert.equal((await call('DELETE', undefined, endpoint+'/'+note.id, {authorization: 'Bearer '+note.edit_token})).status, 200);
    assert.equal((await (await call()).json()).notes.length, 0);
    assert.equal((await call('POST', note)).status, 410, 'Retry cannot resurrect a removed note');
    const second = {...input(), author: 'Ada'};
    assert.equal((await call('POST', second)).status, 201);
    assert.equal((await call('DELETE', undefined, endpoint+'/'+second.id, {authorization: 'Bearer '+admin})).status, 200);
  } finally { db.close(); await rm(dir, {recursive: true}); }
});

test(collection + ': validation, origin restrictions and per-address posting limit', async () => {
  const db = database(), call = client(db, collection);
  try {
    for (const change of [{text: '   '}, {text: 'x'.repeat(20001)}, {author: 'x'.repeat(81)}, {problem_id: '../bad'}, {website: 'spam'}]) {
      assert.equal((await call('POST', {...input(), ...change})).status, 400);
    }
    assert.equal((await call('POST', input(), endpoint, {origin: 'https://unrelated.example'})).status, 403);
    assert.equal((await call('GET', undefined, endpoint+'?before=no')).status, 400);
    const notes = Array.from({length: 6}, input);
    for (const note of notes.slice(0, 5)) assert.equal((await call('POST', note)).status, 201);
    const limited = await call('POST', notes[5]);
    assert.equal(limited.status, 429); assert(Number(limited.headers.get('retry-after')) > 0);
    assert.equal((await call('POST', notes[0])).status, 200, 'Retry is not rate limited');
    assert.equal((await call('POST', notes[5], endpoint, {'cf-connecting-ip': '192.0.2.2'})).status, 201);
    assert.equal((await (await call()).json()).notes.length, 6);
  } finally { db.close(); }
});

test(collection + ': pagination returns every note once without exposing deleted notes', async () => {
  const db = database(), call = client(db, collection);
  try {
    await call();
    for (let i=0; i<403; i++) await db.prepare(`INSERT INTO ${table}(id, problem_id, author, text, created_at, owner_hash, deleted) VALUES (?, ?, ?, ?, ?, ?, ?)`)
      .bind(randomUUID(), 'TCS-6575', 'Anonymous', String(i), new Date().toISOString(), 'hash', i === 200 ? 1 : 0).run();
    const all=[]; let next=null;
    do {
      const result=await (await call('GET', undefined, endpoint+(next?'?before='+next:''))).json();
      all.push(...result.notes); next=result.next;
    } while (next);
    assert.equal(all.length, 402); assert.equal(new Set(all.map(n=>n.id)).size, 402);
    assert(!all.some(n=>n.text==='200'));
  } finally { db.close(); }
});

}

test('public comments are separate from legacy/internal notes, including deletion', async () => {
  const db = database(), legacy = client(db, 'notes'), comments = client(db, 'comments');
  try {
    const internal = {...input(), text: 'Internal editorial feedback'};
    assert.equal((await legacy('POST', internal)).status, 201);
    assert.deepEqual((await (await comments()).json()).notes, []);
    assert.equal((await comments('DELETE', undefined, '/api/comments/'+internal.id, {authorization: 'Bearer '+internal.edit_token})).status, 404);
    const publicComment = {...input(), text: 'Public discussion'};
    assert.equal((await comments('POST', publicComment)).status, 201);
    assert.deepEqual((await (await comments()).json()).notes.map(n=>n.text), ['Public discussion']);
    assert.deepEqual((await (await legacy()).json()).notes.map(n=>n.text), ['Internal editorial feedback']);
  } finally { db.close(); }
});
