# TCS Open Problems Atlas — reader guide

Browse the published reader at https://vaclavrozhon.github.io/atlas/ or run
`make serve` from the repository root. The interface is in English.

## Browse problems

Use the search box to find problems, concepts, authors or stable problem IDs.
Select one or more categories from the single category list. Multiple categories
are combined by OR; search narrows the resulting list. Reset clears the selection
and search. On small screens, the Categories button opens the list.

All problems shows the active catalogue. Top 100 selects the first 5 problems in
each large category and 2 in each small category; Top 1000 selects the first 50/20
from the same order. Search and category filters narrow these fixed selections
without promoting other candidates into unfilled places. About describes the
allocation, reserved places and category counts.

Problems are always ordered by importance. The first 5/2 category positions are
editorial choices balancing importance and topical diversity. Remaining problems
follow importance scores with stable IDs breaking ties. A card shows only its
position within its category. Names and order come from `data/categories.json`,
published in the catalogue's `areas` array.

Compact displays a short presentation with expandable details. Full displays the
statement, context and significance, with progress, definitions and references in
the detail section. Both layouts show the same selected problems in the same
order. The layout and benchmark are preserved in the page URL. Direct problem
links use stable IDs, for example `#TCS-6575`.

Resolved, retired and scope-excluded records are not displayed, including through
old filter URLs or direct links. Records whose present open status is unverified
remain available for later review. Hiding a record in the reader does not delete
its underlying research data. Statements with missing conditions retain their
specific warnings. Sources and dates are evidence about the question, not proof
that it remains open today.

## Shared contributions

Choose Add public note on a card to share an observation, correction or source.
New problem opens a four-field form: title, category, statement and optional
sources. Include definitions, assumptions, the desired result and motivation in
the statement when needed.

Drafts save automatically in this browser. Continue on GitHub opens a prefilled
issue: sign in there and click Submit new issue to publish it. Long drafts offer
the complete text to copy into the GitHub issue description. Return to the form
and choose Refresh shared contributions after submitting. Drafts remain until
you explicitly discard them.

Public notes appear on their problem cards. Community contains proposed problems
with IDs such as `GH-123`; those proposals can receive public notes of their own.
They remain separate from curated catalogue records and Top 100/Top 1000 until
reviewed. Follow the contribution's GitHub link to reply or edit under GitHub's
permissions. GitHub issue comments remain on GitHub. Closing an issue hides that
contribution after refresh, and reopening it restores it.

The reader loads public issues from `vaclavrozhon/atlas`, caches successful reads
for five minutes and provides a manual refresh. Network failures and request
limits keep the last successful result and are reported in Community. The website
does not request or store a GitHub token.

## Updates and compatibility

The catalogue checks for updates in the background without an indicator or
notification. It preserves the reading position, expanded details, filters and
open contribution drafts. Newly resolved or removed records disappear from the
active list on update. File-based copies are offline snapshots.

The simplified interface has no private-note editor, saved problems, random
selection, statement-copy button, advanced filters, sort menu or download controls.
Previously stored private notes and saved flags are left intact in browser storage;
private text is never included in public contributions. Previously saved proposal
drafts keep their definitions, resolution criteria and motivation by incorporating
those old fields into the statement when the shorter form is opened.

Structured publication files remain available for development and archival use,
without download links in the reader. Original research files and source citations
are preserved. KaTeX is bundled under its MIT license in `vendor/`.

Review progress: 246 completed reviews; 2,513 remaining. Completed reviews include 2 individually justified dispositions.
