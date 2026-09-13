# Reader simplification — approved decisions, 11 September 2026

The user reviewed 25 UI choices before authorizing the final batch. The completed
interface retains search, category selection, Whole catalogue / Top 100 / Top
1000, Compact / Full, public notes and new problem proposals.

| # | Approved result |
| --- | --- |
| 1 | Keep both Compact and Full layouts. |
| 2 | Remove private-note UI; preserve previously stored text. |
| 3 | Remove saved-problem controls. |
| 4 | Remove random problem selection. |
| 5 | Remove Copy statement. |
| 6 | Remove the New additions filter. |
| 7 | Remove the textbook/survey filter. |
| 8 | Remove the Card detail filter. |
| 9 | Remove the Group size filter. |
| 10 | Remove the Selection criterion filter. |
| 11 | Remove the source-year filter. |
| 12 | Remove the status filter; hide resolved/retired records, retain unverified ones. |
| 13 | Remove archive/scope browsing; preserve underlying retained records. |
| 14 | Always order by importance; remove the sort control. |
| 15 | Merge the selection plan into About. |
| 16 | Remove technical record-type badges; retain incomplete-statement warnings. |
| 17 | Show only the category position, without editorial/provisional labels. |
| 18 | Remove ranking and Top 100 selection explanations from cards; keep Why it matters. |
| 19 | Remove Export selection from the UI. |
| 20 | Remove all file/download/documentation links from About. |
| 21 | Remove category search. |
| 22 | Show a single category list without group headings or quota labels. |
| 23 | Move benchmark quota/reservation explanations into About. |
| 24 | Remove Live/update indicators; retain background publication. |
| 25 | Use four proposal fields: title, category, statement, optional sources. |

The obsolete controls, handlers and styles were removed rather than kept as hidden
controls. The remaining layout switch lives beside the catalogue selection.
Contribution export was also removed with the other download controls.

The active-record predicate is used for browsing, counts, direct links and live
publication. Historical records remain in the data. No problem statement or source
was rewritten for this UI task. Private browser notes are never modified. Old
unsent proposal fields are folded into the statement once, without losing text.
The original GitHub issue format remains readable for previously posted proposals.

## Validation

- `tests/simplified-ui.cjs`: approved controls, private text preservation, active
  counts, category order, both layouts, benchmark membership, search without
  backfilling, unverified records, exclusion through direct/legacy links, About,
  draft migration, 320–1440px layouts and actual silent publication while editing.
- `tests/community.cjs`: shared notes/proposals, independent visitors, pagination,
  escaped untrusted text, draft persistence, four-field submissions, long Unicode
  text, unavailable storage, cached API failures and closed issues. GitHub reads
  and submission pages are intercepted; no public test issue is created.
- `tests/pages.cjs`: project-subdirectory loading, static files, both layouts,
  contribution forms and mobile layout. Also run against the deployed Pages URL.

Browser reports and screenshots are stored in this directory.

## Deployment

The UI was deployed to https://vaclavrozhon.github.io/atlas/ in commit
`c4a8c1104579ce49003df23aa9d797d17bd88823`, followed by the narrow-mobile
layout adjustment in `970952a5612fb306a3fe2e223a90b471b4b7cbd5`. Only reader
assets were included in these pushes; the independent catalogue publication
`f5dac4d30b715009a0e7fe94f355a803f1605b6b` was retained between them.
The final GitHub Pages run `34594788258` succeeded. Both browser suites passed
on the public URL, with zero page/HTTP errors in the live Pages check.
Offline Top 100 and both layouts were also checked.

The local repository was reorganized concurrently into `web/`, `data/`,
`scripts/` and `tests/`; this UI work follows those paths. Historical QA scripts
that target removed controls describe the previous interface. The active
simplification, community and Pages suites listed above cover the current UI.
