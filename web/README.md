# Reader sources

This directory contains `index.html`, `app.js`, `community.js`, `votes.js`, `math.js`, `style.css`,
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
preserving positions while removing deleted or resolved nodes and their links.
The locally bundled D3 version and license are documented in `vendor/D3.md`.

Run `make serve` from the repository root to build and view the reader.
`make publish` produces the complete site in ignored `build/`; its `index.html`
also opens directly offline. Generated JSON, CSV, `data.js` and reports belong
only in `build/` and are rebuilt from canonical data.

The reader supports search, categories, Compact and Full layouts, Top 100,
Top 500 and a legacy Top 1000 view, public notes and proposed community
problems. Top 500 is the primary goal; Top 100 is its priority subset.
All three views use prefixes of the same ranking within each
category and preserve the category order. Shared votes determine this ranking:
thumbs up minus thumbs down first, then the existing catalogue priority. This
also determines membership in Top 100, Top 500 and the legacy Top 1000 view,
using the existing category quotas before search filters. A browser retains one
identity without login. Click the selected thumb to cancel, or the other to switch.
Both layouts display shared counts and highlight the current browser's vote.
Counts refresh every 30 seconds and on returning to the page; cached counts are
retained during an outage. Without cached counts the reader uses catalogue priority.
Static exports continue to record the reproducible editorial ranking; shared votes
are stored independently in the service. Public notes post directly to the
[notes service](../services/notes/README.md) without an account; names are optional
and unverified. Problem proposals and older notes use GitHub. The catalogue and
mathematical rendering work offline. Live publication
uses `version.json`, `updates-delta.json` and `catalog.json` as the full fallback.
Resolved and retired records are hidden. See [the rules](../docs/RULES.md).

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
LaTeX command names. Public reader notes retain their plain-text format.
