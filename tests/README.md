# Checks

`make check` copies current canonical data, web sources and Python code into a temporary
directory, rebuilds the catalogue without any previous output, and runs category,
ranking, publication, import and deployment regressions. It leaves the working
reader and canonical source files untouched. The deployment test uses a temporary
local bare Git repository.

Inactive card contents are excluded from the routine check snapshot and are not
reviewed or validated. Archival regressions use small isolated fixtures to check
lossless moves, explicit restoration, reserved IDs and removal from live exports.

`make check-web` exercises the reader under a project URL prefix, direct file
opening, category selection, community forms, mobile layout and live deletions.
It checks full-catalogue fallback after missed updates and safe retries while
publication files temporarily disagree about the current version.
It also tests the notes/proposals/votes/selection worker against real SQLite.
The final reader must not fetch or render archived feedback; its GitHub proposal
form preserves browser-local drafts. All test writes go to isolated databases.
`votes.cjs` also exercises two independent voters and multiple tabs, vote
cancellation and replacement, retries after lost responses, shared scores,
vote-driven Top selections with editorial ties, storage failures and mobile UI.
All test votes stay in an isolated SQLite database.
Install its dependencies with `npm ci --prefix tests`; Chrome is expected at
`/usr/bin/google-chrome`. These checks do not submit GitHub issues or deploy a site.

`simplified-ui.cjs` provides additional focused UI regressions against the server
specified by `ATLAS_URL`. `community.cjs` starts its own local reader server and checks feedback privacy
and the preserved problem-proposal form.
GitHub issue submissions are mocked.
Historical one-off checks and saved screenshots were removed during cleanup.

`node tests/map.cjs` checks the separate problem map under a project URL prefix
and `file://`: active nodes, relationship deduplication, verbatim saved summaries,
hover and pinned previews, drag/pan/zoom, search, category highlighting, keyboard
access, formula rendering, safe text, consistent live updates and node removal,
empty catalogues, reduced motion and mobile touch. It uses local snapshot fixtures,
performs no external writes and saves review screenshots in a temporary directory.

`math.cjs` validates every LaTeX expression on every active canonical card with
the bundled KaTeX and checks balanced delimiters and formula-safe excerpts.
`math-browser.cjs` renders every active card in both layouts, checks parse errors
and unrendered delimiters, then exercises excerpts, reference titles and mobile
width using local fixtures. Both run in `make check-web`.

`selection.cjs` bridges requests to the production worker with an isolated SQLite
database. It tests anonymous visitors, immediately visible controls, color and paired category
changes, counts beyond quota, lost replies, conflicts, reloads, publication, map
synchronization, mobile layout and outages. `final_selection.py` checks the initial
500-card proposal, coverage, paired categories and explicit editorial decisions.
