# Shared web contributions — 11 September 2026

The user requested notes on problems and new problems through the website, and
chose shared GitHub storage over browser-only contributions. The existing private
notes remain available as a separate editor.

The website provides public-note and new-problem forms, saves unsent drafts
locally, and opens GitHub with the complete title and body. The author confirms
submission on GitHub. Long URL payloads have a complete-text copy/paste fallback.
Public issues are loaded through GitHub's API, including pagination, with a
five-minute cache and manual refresh. Failed reads retain the last successful
result. Closed contributions disappear on refresh. New problems use `GH-` IDs
and appear as unreviewed community drafts outside the curated benchmark.

The repository setting was checked: `vaclavrozhon/atlas` is public with Issues
enabled. No test issue or comment was posted to the public repository.

## Verification

- `qa/community.cjs`: browser flows use intercepted GitHub reads and submission
  pages. Checks include an independent browser seeing shared data, stable-ID
  notes, proposal parsing, private-note isolation, unsent draft persistence,
  unavailable browser storage, required fields, long Unicode text, safe rendering
  of untrusted content, pagination, cached reads after API failure, issue closure,
  mobile layout and unchanged curated selection membership.
- `qa/live.cjs`: publication polling preserves the private note, caret/focus,
  reading position, expanded details and filters.
- `qa/top100.cjs`: selection membership, category quotas, exports with private
  notes, filtering, mobile layouts, offline loading and live updates pass.
- `qa/test_pages.py`: temporary Git remotes verify first/unchanged/incremental
  deployments, removed files, preservation of the source worktree and staged
  changes, and rejection of incomplete publications.
- `qa/pages.cjs`: project-subdirectory assets, public-note/new-problem forms,
  downloads, export, mobile layout, browser and HTTP errors.

The browser report and desktop/mobile form screenshots are saved alongside this
file. GitHub remains responsible for authentication and issue permissions. Its
API limits or unavailability may delay new contributions until the next successful
refresh; the Community section reports this rather than claiming an empty list.

## Live deployment

Published to https://vaclavrozhon.github.io/atlas/ in commit
`1fcc153b0c8ca50f3764a8ca84d4ceb372b45f35`. GitHub Pages run
`34592531738` succeeded. The live browser check passed, including both forms,
all 34 category options, mobile layout, static exports and a successful read from
the actual public GitHub Issues API. See `deployment.json` and `live-browser.json`.
