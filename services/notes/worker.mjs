const initialized = new WeakMap();
const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const tokenPattern = /^[0-9a-f]{64}$/;
const problemPattern = /^(TCS-\d{4,}|GH-\d+)$/;
const publicColumns = 'seq, id, problem_id, author, text, created_at';

async function initialize(db) {
  if (!initialized.has(db)) {
    const pending = db.batch([
      db.prepare(`CREATE TABLE IF NOT EXISTS notes (
        seq INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT NOT NULL UNIQUE,
        problem_id TEXT NOT NULL,
        author TEXT NOT NULL,
        text TEXT NOT NULL,
        created_at TEXT NOT NULL,
        owner_hash TEXT NOT NULL,
        deleted INTEGER NOT NULL DEFAULT 0
      )`),
      db.prepare('CREATE INDEX IF NOT EXISTS notes_problem ON notes(problem_id, seq)'),
      db.prepare(`CREATE TABLE IF NOT EXISTS note_limits (
        fingerprint TEXT PRIMARY KEY, window INTEGER NOT NULL, count INTEGER NOT NULL
      )`),
      db.prepare(`CREATE TABLE IF NOT EXISTS votes (
        problem_id TEXT NOT NULL, voter_hash TEXT NOT NULL,
        value INTEGER NOT NULL CHECK(value IN (-1, 0, 1)),
        revision INTEGER NOT NULL,
        PRIMARY KEY(problem_id, voter_hash)
      )`),
      db.prepare('CREATE INDEX IF NOT EXISTS votes_voter ON votes(voter_hash)'),
    ]).catch(error => { initialized.delete(db); throw error; });
    initialized.set(db, pending);
  }
  return initialized.get(db);
}

async function digest(value) {
  const bytes = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value));
  return [...new Uint8Array(bytes)].map(byte => byte.toString(16).padStart(2, '0')).join('');
}

function equal(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let difference = 0;
  for (let i = 0; i < a.length; i++) difference |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return difference === 0;
}

function publicNote(row) {
  return Object.fromEntries(['seq', 'id', 'problem_id', 'author', 'text', 'created_at'].map(key => [key, row[key]]));
}

const voteTotals = `SELECT problem_id, SUM(value = 1) AS up, SUM(value = -1) AS down,
  SUM(value) AS score FROM votes`;
async function voteState(db, problemId, voterHash) {
  const row = await db.prepare('SELECT value, revision FROM votes WHERE problem_id = ? AND voter_hash = ?').bind(problemId, voterHash).first();
  const totals = await db.prepare(voteTotals+' WHERE problem_id = ? GROUP BY problem_id').bind(problemId).first();
  return {vote: {problem_id: problemId, value: row?.value || 0, revision: row?.revision || 0},
    totals: totals || {problem_id: problemId, up: 0, down: 0, score: 0}};
}

async function bodyJSON(request) {
  if (!request.headers.get('content-type')?.toLowerCase().startsWith('application/json')) {
    throw Object.assign(new Error('Use a JSON request.'), {status: 415});
  }
  if (!request.body) throw Object.assign(new Error('Enter a note.'), {status: 400});
  const reader = request.body.getReader(), chunks = [];
  let length = 0;
  while (true) {
    const {done, value} = await reader.read();
    if (done) break;
    length += value.byteLength;
    if (length > 90000) {
      await reader.cancel();
      throw Object.assign(new Error('This note is too long.'), {status: 413});
    }
    chunks.push(value);
  }
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  try { return JSON.parse(new TextDecoder().decode(bytes)); }
  catch { throw Object.assign(new Error('Invalid note data.'), {status: 400}); }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url), origin = request.headers.get('origin');
    const allowed = new Set(['https://vaclavrozhon.github.io', url.origin]);
    // Development origins must be supplied explicitly in the local test server.
    for (const item of (env.NOTES_ALLOWED_ORIGINS || '').split(',')) if (item.trim()) allowed.add(item.trim());
    const headers = {'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', 'Vary': 'Origin'};
    if (origin && allowed.has(origin)) headers['Access-Control-Allow-Origin'] = origin;
    const reply = (value, status = 200, extra = {}) => new Response(JSON.stringify(value), {status, headers: {...headers, ...extra}});
    if (origin && !allowed.has(origin)) return reply({error: 'This origin is not allowed.'}, 403);
    if (request.method === 'OPTIONS') return new Response(null, {status: 204, headers: {...headers,
      'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization', 'Access-Control-Max-Age': '600'}});
    try {
      if (!env.DB) return reply({error: 'Notes are temporarily unavailable.'}, 503);
      await initialize(env.DB);
      if (url.pathname === '/health' && request.method === 'GET') {
        await env.DB.prepare('SELECT seq FROM notes LIMIT 1').first();
        return reply({ok: true});
      }
      if (url.pathname === '/' && request.method === 'GET') return reply({service: 'Atlas public notes', website: 'https://vaclavrozhon.github.io/atlas/'});
      if (url.pathname === '/api/votes' && ['GET', 'POST'].includes(request.method)) {
        const authorization = request.headers.get('authorization');
        const token = authorization?.replace(/^Bearer /, '') || '';
        if ((authorization || request.method === 'POST') && !tokenPattern.test(token)) return reply({error: 'Invalid voter identity.'}, 400);
        const voterHash = token ? await digest(token) : null;
        if (request.method === 'GET') {
          const totals = await env.DB.prepare(voteTotals+' GROUP BY problem_id').all();
          const own = voterHash ? await env.DB.prepare('SELECT problem_id, value, revision FROM votes WHERE voter_hash = ?').bind(voterHash).all() : {results: []};
          return reply({votes: totals.results, mine: own.results});
        }
        const input = await bodyJSON(request);
        if (!input || typeof input !== 'object' || Array.isArray(input) ||
            !problemPattern.test(input.problem_id || '') || ![-1, 0, 1].includes(input.value) ||
            !Number.isSafeInteger(input.revision) || input.revision < 1) return reply({error: 'Invalid vote.'}, 400);
        const current = await voteState(env.DB, input.problem_id, voterHash);
        // Repeating a request sets the same vote; it never adds another one.
        if (current.vote.revision === input.revision && current.vote.value === input.value) return reply(current);
        if (input.revision !== current.vote.revision + 1) return reply({error: 'Your vote changed in another tab. Please try again.', ...current}, 409);
        await env.DB.prepare(`INSERT INTO votes(problem_id, voter_hash, value, revision) VALUES (?, ?, ?, ?)
          ON CONFLICT(problem_id, voter_hash) DO UPDATE SET value = excluded.value, revision = excluded.revision
          WHERE votes.revision = excluded.revision - 1`).bind(input.problem_id, voterHash, input.value, input.revision).run();
        const saved = await voteState(env.DB, input.problem_id, voterHash);
        if (saved.vote.revision !== input.revision || saved.vote.value !== input.value) return reply({error: 'Your vote changed in another tab. Please try again.', ...saved}, 409);
        return reply(saved);
      }
      if (url.pathname === '/api/notes' && request.method === 'GET') {
        const raw = url.searchParams.get('before');
        const before = raw === null ? Number.MAX_SAFE_INTEGER : Number(raw);
        if (!Number.isSafeInteger(before) || before < 1) return reply({error: 'Invalid page cursor.'}, 400);
        const result = await env.DB.prepare(`SELECT ${publicColumns} FROM notes WHERE deleted = 0 AND seq < ? ORDER BY seq DESC LIMIT 201`).bind(before).all();
        const notes = result.results.slice(0, 200);
        return reply({notes, next: result.results.length > 200 ? notes.at(-1).seq : null});
      }
      if (url.pathname === '/api/notes' && request.method === 'POST') {
        if (!tokenPattern.test(env.NOTES_ADMIN_TOKEN || '')) return reply({error: 'Notes are temporarily unavailable.'}, 503);
        const input = await bodyJSON(request);
        if (!input || typeof input !== 'object' || Array.isArray(input)) return reply({error: 'Invalid note data.'}, 400);
        if (input.website) return reply({error: 'The submission could not be accepted.'}, 400);
        if (!uuid.test(input.id || '') || !tokenPattern.test(input.edit_token || '') || !problemPattern.test(input.problem_id || '')) return reply({error: 'Invalid note identifier.'}, 400);
        if (typeof input.text !== 'string' || !input.text.trim() || input.text.length > 20000) return reply({error: 'Enter a note of at most 20,000 characters.'}, 400);
        if (input.author !== undefined && (typeof input.author !== 'string' || input.author.length > 80)) return reply({error: 'Use a name of at most 80 characters.'}, 400);
        const text = input.text.trim(), author = input.author?.trim() || 'Anonymous', ownerHash = await digest(input.edit_token);
        const existing = await env.DB.prepare('SELECT * FROM notes WHERE id = ?').bind(input.id).first();
        if (existing) {
          if (existing.deleted) return reply({error: 'This note has been removed.'}, 410);
          if (!equal(ownerHash, existing.owner_hash) || existing.text !== text || existing.author !== author || existing.problem_id !== input.problem_id) return reply({error: 'This submission identifier has already been used.'}, 409);
          return reply({note: publicNote(existing)}, 200);
        }
        const window = Math.floor(Date.now() / 600000);
        const fingerprint = await digest(env.NOTES_ADMIN_TOKEN + '\n' + (request.headers.get('cf-connecting-ip') || 'unknown'));
        const limit = await env.DB.prepare(`INSERT INTO note_limits(fingerprint, window, count) VALUES (?, ?, 1)
          ON CONFLICT(fingerprint) DO UPDATE SET window = excluded.window,
          count = CASE WHEN note_limits.window = excluded.window THEN note_limits.count + 1 ELSE 1 END
          RETURNING count`).bind(fingerprint, window).first();
        if (limit.count > 5) return reply({error: 'Please wait a few minutes before posting another note.'}, 429, {'Retry-After': String(600 - Math.floor(Date.now() / 1000) % 600)});
        const created = new Date().toISOString();
        await env.DB.batch([
          env.DB.prepare('DELETE FROM note_limits WHERE window < ?').bind(window - 1),
          env.DB.prepare('INSERT INTO notes(id, problem_id, author, text, created_at, owner_hash) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO NOTHING')
            .bind(input.id, input.problem_id, author, text, created, ownerHash),
        ]);
        const note = await env.DB.prepare('SELECT * FROM notes WHERE id = ?').bind(input.id).first();
        // Concurrent retries must not turn a conflicting request into success.
        if (note.deleted || !equal(note.owner_hash, ownerHash) || note.text !== text || note.author !== author || note.problem_id !== input.problem_id) return reply({error: 'This submission identifier has already been used.'}, 409);
        return reply({note: publicNote(note)}, 201);
      }
      const match = url.pathname.match(/^\/api\/notes\/([0-9a-f-]+)$/i);
      if (match && request.method === 'DELETE') {
        if (!uuid.test(match[1])) return reply({error: 'Invalid note identifier.'}, 400);
        const token = request.headers.get('authorization')?.replace(/^Bearer /, '') || '';
        if (!tokenPattern.test(token)) return reply({error: 'You cannot remove this note.'}, 403);
        const row = await env.DB.prepare('SELECT owner_hash FROM notes WHERE id = ?').bind(match[1]).first();
        if (!row) return reply({error: 'Note not found.'}, 404);
        const admin = tokenPattern.test(env.NOTES_ADMIN_TOKEN || '') && equal(token, env.NOTES_ADMIN_TOKEN);
        if (!admin && !equal(await digest(token), row.owner_hash)) return reply({error: 'You cannot remove this note.'}, 403);
        await env.DB.prepare("UPDATE notes SET deleted = 1, text = '', author = '' WHERE id = ?").bind(match[1]).run();
        return reply({removed: true});
      }
      return reply({error: 'Not found.'}, 404);
    } catch (error) {
      if (error.status) return reply({error: error.message}, error.status);
      // Do not expose database statements, input, or credentials in public errors.
      return reply({error: url.pathname === '/api/votes' ? 'Voting is temporarily unavailable. Please retry.' : 'Notes are temporarily unavailable. Your draft has not been discarded.'}, 503);
    }
  },
};
