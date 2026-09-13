# Atlas public notes

Small Cloudflare Worker with durable D1 storage, deployed through Sites. The
catalogue stays on GitHub Pages. This service accepts public notes without a
GitHub or ChatGPT account; GitHub issues remain the source of problem proposals
and older notes. Display names are optional and unverified.

Run `npm test` (Node 22+) and `npm run build`. Tests execute the worker against real
SQLite, including reconnecting to a file database, pagination, retries, deletion,
validation, and rate limits. The build output is `dist/server/index.js`.

The Sites project is recorded in `.openai/hosting.json`, with the D1 binding `DB`.
Tables are created on first access. Redeployments reuse the database. Package the
build output and `.openai/hosting.json`, push this directory's exact source to the
Sites source repository, then save and deploy the matching full commit SHA.
Do not include tests, credentials, or the Atlas catalogue in the deployment archive.
The service must have public access for visitors without an account.

Configure `NOTES_ADMIN_TOKEN` as a secret runtime variable: 32 random bytes encoded
as 64 lowercase hexadecimal characters. Never put it in hosting.json, client code,
or Git. It authorizes moderation and salts IP hashes. The owner's local copy is
outside this repository at `~/.config/atlas-notes/admin-token` (mode 0600).

`GET /api/notes` returns public notes, at most 200 per page. Follow `next` using
`?before=<next>`. `POST /api/notes` accepts `id` (UUID v4), `problem_id`, `text`
(1–20,000 characters), optional `author` (up to 80), and `edit_token` (64 hex).
Exact retries return the existing note. The browser persists this request before
sending, so a lost response cannot create a duplicate. Only the token hash is
stored in D1; public reads exclude it. Tokens stay in the submitting browser.

`DELETE /api/notes/<id>` requires `Authorization: Bearer <edit_token>` or the
administrator secret. It removes the public text and leaves a tombstone to prevent
retry resurrection. The UI exposes deletion to the submitting browser. To moderate,
use the administrator secret with this endpoint; never paste it into a public note.

Creation is limited to five notes per client IP in each ten-minute window, with an
empty honeypot field. Raw IPs are not stored; hashes expire from the rate table on
subsequent accepted posts. CORS allows the Atlas GitHub Pages origin and this
service's origin. `NOTES_ALLOWED_ORIGINS` is only needed for local development.
Notes are plain text, escaped by the reader. No login or cookies are required.

## Votes

The same database stores shared thumbs-up/down votes. `GET /api/votes` returns
`votes` (problem ID, up/down counts and net score) and `mine` (only the caller's
values and revisions). A browser creates and retains a random 64-hex identity;
it supplies it as `Authorization: Bearer <identity>`. Anonymous reads omit this
header and receive no individual votes. The database stores only the identity hash.

`POST /api/votes` takes `problem_id`, `value` (`1`, `-1`, or `0` to cancel), and
`revision` (the previous revision plus one). The unique problem/identity key
allows only one vote. Exact retries are idempotent; stale or conflicting revisions
return HTTP 409 with the current vote and totals. Cancelled votes retain their
revision so an older retry cannot resurrect them. The client persists an exact
pending request before sending and offers retry if the result is uncertain.

Votes persist across Worker and reader deployments. They need no administrator
secret. Reusing the existing `DB` binding preserves both notes and votes. New
browsers or cleared browser storage create a new identity, as intentionally chosen
for a small group without accounts. Unit tests and `node tests/votes.cjs` from the
repository root cover durability, retries, competing tabs and the browser UI.
