# Shared problem votes — 12 September 2026

Readers can vote with thumbs up/down in Compact and Full cards and on community
proposals. A random identity is persisted in each browser without login. Clicking
the selected thumb cancels the vote; the opposite thumb replaces it. A physical
double-click is a single action. The API stores one row per problem and identity
hash, with revision checks and exact retries to avoid duplicate or stale votes.
Pending requests are saved before sending. Independent browsers see shared totals;
counts refresh every 30 seconds and on returning to the page.

The live catalogue groups problems in the established category order. Within each
category it sorts by thumbs up minus thumbs down, then the existing editorial
priority. This determines both displayed order and membership in Top 100, Top 500
and legacy Top 1000, with unchanged category quotas and nested selections. Search
narrows each already selected set. Rank badges follow this live ranking. Votes are
stored in the existing notes service database, independently of static publication;
canonical editorial assessments and generated exports remain reproducible.

Implementation: `web/votes.js`, reader integration, and `services/notes/worker.mjs`.
The API uses the existing service project and DB binding without changing access.
Browser identity is intentionally only a convenience: a different browser or cleared
storage gets a new identity. When browser storage is blocked, counts remain readable
and voting is disabled. Outages retain cached counts and disclose that they are stale.

## Verification

- Worker tests use real SQLite: durable votes, one vote under concurrent retries,
  switching/cancellation, no resurrection by old retries, competing tab revisions,
  input validation and aggregate-only public reads. Existing notes tests pass.
- `tests/votes.cjs` uses independent Playwright visitors sharing an isolated local
  SQLite database. It checks double-clicks, reloads, shared counts, changing and
  cancelling votes, retrying lost responses, multiple tabs, vote-driven Top 100/500
  membership, subset nesting, category ordering, editorial ties, filters, both
  layouts, outage handling, unavailable storage and mobile overflow.
- `make check` passes isolated catalogue, taxonomy, publication, export and Pages
  deployment regressions. UI checks cover existing notes, proposals and deletions.
- Desktop and mobile screenshots are saved alongside this report. Test votes never
  touch the public database.

## Deployment

- Notes/votes service: Sites version 2, source commit
  `637fed09a80c3ee8c63a820ff75f0fdc2b92f343`; deployment
  `appgdep_6aa514260e748191b149b9a63ad3173f` succeeded.
- GitHub Pages: `ec867b5ed3eb110c961538c6ce4bf10a6e6563a1`, catalogue version
  `da81c21879edaddac9cb`. Published JS, HTML and CSS were compared byte-for-byte
  with the checked local source.
- `make check` and `make check-web` passed. The live browser verification reads
  actual shared votes without login, checks the KLS controls and mobile layout,
  and records its results in `live.json`; it does not cast a public test vote.
