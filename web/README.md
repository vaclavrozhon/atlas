# Reader sources

This directory contains `index.html`, `app.js`, `community.js`, `votes.js`, `selection.js`, `math.js`, `style.css`,
`.nojekyll` and local KaTeX assets in `vendor/`.

`map.html`, `map.js` and `map.css` provide the separate interactive problem map.
It reads the same `data.js`, keeps all active records (including isolated nodes),
and draws each related-problem pair once. D3's local force simulation combines
relationship springs, repulsion, collision avoidance and a weaker category
attraction. The category force is the normalized sum of pairwise attractions,
computed through category centroids; it does not add invented relationship edges.
Search and category selection highlight the existing layout. Drag nodes or pan
the background, zoom, pause, and use Fit map to return to the whole graph.
Hover previews reuse the complete saved working summary, falling back to the
existing question excerpt when no summary exists. Clicking, tapping or keyboard
selection keeps a preview open, with a link to the original catalogue card.
Arrow keys browse problems and Enter focuses the full-card link; Escape dismisses
the preview. Reduced-motion preferences pause the simulation after initial layout.
The map also opens offline and checks consistent live catalogue snapshots online,
preserving positions while removing inactive nodes and their links. Shared category moves and selection
labels are also reflected in map previews.
The locally bundled D3 version and license are documented in `vendor/D3.md`.

Run `make serve` from the repository root to build and view the reader.
`make publish` produces the complete site in ignored `build/`; its `index.html`
also opens directly offline. Generated JSON, CSV, `data.js` and reports belong
only in `build/` and are rebuilt from canonical data.

The reader supports search, categories, Compact and Full layouts, and All/Green/Red
filters. `selection.js` loads public overrides from the existing service and
applies them to the canonical initial proposal. The sidebar displays actual green
counts against 25/10 targets, regardless of filters. Every reader sees the color and category buttons immediately; selection writes
require no login, edit mode or editor key. Exactly one large/small category
pair is offered on suitable cards; moving preserves color. Revisions prevent
silent overwrite by stale editors, and exact pending requests survive lost replies.
The initial proposal and last loaded choices remain visible during an outage.

Votes continue to order each category: thumbs up minus thumbs down, then catalogue
priority. They do not change green/red decisions. The previous Top 100/500/1000
ranking filters remain in About, with visible filter chips when active. Mathematical
rendering and the initial catalogue also work offline. Live publication uses
`version.json`, `updates-delta.json` and `catalog.json` as the full fallback.
Resolved cards with documented January 1, 2026 eligibility remain visible; inactive
cards do not. See [the rules](../docs/RULES.md).

Community feedback is preserved separately and is neither fetched nor rendered
by the final reader. Publication strips `community_reviews` from reader exports
without changing the canonical source or archive. `community.js` retains the
GitHub problem proposal form and its browser-local draft migration. Existing notes,
proposals, votes and deletion ownership remain intact in the separate service.

Both layouts show related active problems by title and stable ID, without inline
explanations. The first five are visible and longer lists can be expanded.
Navigation reveals the target even outside current filters or pagination. Live
updates refresh incoming titles, remove retired targets, and preserve expanded
related lists.

Mathematical expressions use explicit LaTeX delimiters and the bundled KaTeX.
`math.js` shares formula boundaries between paragraph rendering and compact
previews, so blank lines or excerpt limits cannot split a formula. Source excerpts
and reference titles render math too. Long inline expressions scroll within the
card on small screens. Search uses readable mathematical text rather than requiring
LaTeX command names.
