# Public selection editing — 5 November 2026

The owner requested that everyone be able to edit, with color and applicable
category controls visible directly on each card. The reader now renders these
buttons immediately in Compact and Full views. There is no edit-mode toggle,
login dialog, editor key or selection Authorization header.

The existing service accepts anonymous selection writes. Card IDs, colors,
paired categories, manifest versions, revision conflicts and exact retries are
still validated. Existing saved choices, votes, notes and proposals are preserved.
The obsolete selection secret was removed from runtime configuration; moderation
of notes and proposals retains its existing credentials. Catalogue content and
the deferred scientific/numerical audit are unchanged.

Validation: all 12 service tests passed against real SQLite; selection browser
checks passed for anonymous visitors, direct controls, color/category changes,
shared persistence, concurrent edits, retries, publication and mobile widths.
The page integration check also passed. The backend (version 5) and reader are
published. A clean browser changed a real card without credentials, a second
anonymous visitor observed it, and the original color was restored and confirmed
after reload. Both controls were visible on desktop and mobile. Deployment
details and live verification are recorded in deployment.json and ui/live.json.
