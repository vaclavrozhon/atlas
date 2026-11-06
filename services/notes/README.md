# Atlas public notes

Small Cloudflare Worker with durable D1 storage, deployed through Sites. The
catalogue stays on GitHub Pages. This service accepts public notes without a
GitHub or ChatGPT account; It also accepts problem suggestions directly; GitHub issues remain the source of
older proposals and notes. Display names are optional and unverified.

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

## Current public comments

The restored reader uses `GET/POST /api/comments` and
`DELETE /api/comments/<id>`, with the same request, response, pagination,
retry, moderation and rate-limit rules as notes above. The response keys remain
`notes` (list) and `note` (submission). These endpoints use a separate
`public_comments` table. No legacy note, GitHub issue, editorial review or archived
feedback is imported. The original `/api/notes` API and its stored records remain
unchanged for compatibility; they are not a source for the current reader.

The browser also uses separate comment cache, ownership and draft keys. Local
private notes and old note drafts are never prefilled into the public form.

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

## Problem suggestions

`GET /api/proposals` returns `proposals` and `next`, with the same cursor pagination
as comments. `POST /api/proposals` accepts `id` (UUID v4), `edit_token` (64 hex),
`title` (1–200 characters), `statement` (1–50,000), optional `category` (a category
slug, at most 80), `sources` (up to 5,000), `author` (up to 80), and the empty
`website` honeypot. A blank category means undecided. Names default to Anonymous.
The returned `proposal.id` is `P-<UUID>` and can be used as the `problem_id` for
comments and votes. Suggestions are public immediately but are not catalogue cards.

The separate `proposals` table is created without modifying existing notes or votes.
Exact retries are idempotent and do not consume the shared five-posts-per-ten-minutes
limit. `DELETE /api/proposals/P-<UUID>` accepts the author's deletion token or the
existing administrator secret. It clears the public fields and keeps a tombstone;
retries cannot recreate a deleted suggestion. Public responses exclude credentials.
Use the existing site and D1 binding when deploying this extension.

## Shared final selection

`selection-manifest.mjs` is generated from the Atlas source with
`python3 scripts/final_selection.py --manifest services/notes/selection-manifest.mjs`.
It contains the initial green/red proposal and each card's one or two allowed
categories. Regenerating defaults never updates or deletes saved manual choices.

Selection editing is public by explicit owner request. Every reader sees color
and paired-category buttons immediately, with no login or editor key. The former
`SELECTION_EDITOR_TOKEN` is no longer used. Moderation of notes and proposals
continues to require their existing author or administrator token.

`GET /api/selection` returns the manifest version and durable overrides from
`selection_choices`. `POST /api/selection` accepts anonymous JSON requests with
`problem_id`, `color`, `area`, and `revision` (previous + 1). The reader also
sends `previous: {color, area}` for the state it displayed, and a service
`version` for compatibility with older deployments.
`POST /api/selection/auth` remains a compatibility endpoint returning `can_edit: true`;
the current reader does not call it or send an Authorization header for selection.
Only the configured categories are allowed, but green counts may exceed or fall
short of targets. Exact retries are idempotent. A conflicting edit returns HTTP
409 with the current choice instead of overwriting it. When `previous` is supplied,
it must match the current card state; this also protects a changed editorial
default before the first manual edit. Legacy requests without `previous` retain
revision checks. Global manifest versions do not lock editing: unrelated catalogue
changes can deploy independently of the service. Card IDs, allowed categories,
revisions and previous states are checked on every write. The reader also retries
one version-only rejection from an older service without changing the requested
color, category or revision. The existing origin policy still applies.
Retired card rows remain in storage, but disappear from public reads until restored.

Deployment preserves the existing site, D1 binding, notes, proposals and votes.
The final catalogue reader displays only the separate public-comment stream.
The preserved feedback archive remains in the Atlas research directory and is
excluded from reader exports.
