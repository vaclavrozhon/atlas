# TCS Open Problems Atlas — UI demo

English-language working edition, 10 September 2026.

Open `index.html` directly in a browser. The reader works without a server or an
internet connection; following external references requires internet access.
For a local server, run `python3 -m http.server 8766 --bind 127.0.0.1` here.

## Selection categories

Use **Top 100** or **Top 1000** in the main toolbar. Top 100 takes the first
**5/2** places per large/small category; Top 1000 takes the first **50/20** from
the same order. The first 5/2 are explicitly selected for importance and topical
diversity; remaining places use importance scores and stable-ID tie-breaks.
Categories with fewer eligible candidates contribute only those candidates.
Archived, retired and resolved records are excluded. The reader shows actual
totals and unfilled places rather than silently reallocating quotas.
[Open Top 100](index.html?benchmark=top100) ·
[Open Top 1000](index.html?benchmark=top1000) ·
[Selection review](benchmark-selection.md) ·
[Top 100 JSON](top100.json) · [Top 1000 JSON](top1000.json).
Search, category filters
and sorting operate within that selection; they do not promote lower-ranked
matches into it. Category counts show the subbenchmark allocation. Live publication
refreshes membership when ranks change. **Export selection** downloads the visible
selection with notes, publication metadata and the subbenchmark quotas.

The reader implements **10 large groups × 50 + 24 small groups × 20**.
Online algorithms and scheduling/packing share one category. The remaining small
slot reserves 20 of the planned 1,000 places (two places in Top 100) for a future category.
[Current category sizes](category-sizes.md) are regenerated on each publication.
Counts are retained candidate records. The first large-category review archived 2,069 candidates and the second individually explained pass archived another 543. The separate small-category pass archived 1,835. Final quota selection and a comprehensive deduplication audit remain pending.

Selection inventory: 1,284 large-category and 1,472 small-category candidates; 4,472 archived records; 7,228 saved in total.

The sidebar separates large and small groups in the approved thematic order.
Names and order come from the single `../categories.json` registry, published in
`catalog.json` as `areas`. The reader uses these labels in filters, cards,
archive details, search and downloads. Current names and counts are in the
[category table](category-sizes.md).

`../taxonomy.py` maps original categories and applies specific topic rules to saved
questions and primary source titles. `../category_overrides.json` records explicit
corrections, scope decisions and borderline retentions. The last category holds
unclassified questions. General combinatorics outside the accepted scope is archived
with a reason: use **Selection scope** to browse the archive or all saved records.
This classification is not an individual research or open-status review.

Machine-readable exports preserve historical `area` keys for compatibility and
provide current labels through `areas`, `area_label` or `preliminary_category_label`.

The [11 September category review](category-review-20260911.md) reconsiders every
active candidate and lists individual moves with reasons and before/after counts.
Summary authoring files retain their original small/large cohorts, while reader
groups and summary collections follow each problem's current category.

Exports preserve stable IDs, original areas, statements, references, statuses and
importance assessments. `scope_exclusion.kind = preliminary_quality` marks reversible pruning across the three independent review batches; other scope exclusions concern subject boundaries. The independent review status is preserved. No source record is deleted. Personal
notes remain attached to the same IDs, including archived records. Full JSON/CSV
include the archive; `scope-excluded.json` also exposes it separately.

The frozen removal records, explanations and restoration tool are in
`../to_delete/large-buckets-20260910/`. Publication reads that directory’s manifest,
so a routine rebuild does not put quarantined candidates back into the default pool.

`../publish.py` reapplies these decisions and publishes matching JSON, CSV, offline
JavaScript, category counts, rankings and live-update snapshots.

## Review scope

Active small-category candidates now also have **five-sentence working summaries**,
written from their saved source material. Read them in
[Quick cards](index.html?group=small) or in the
[collected summaries](small-bucket-summaries.md). They explain the problem before
the full research-card stage; missing conditions in incomplete source fragments
remain explicit. The summaries preserve existing evidence, status, formal
statements and personal notes. They are searchable and included in JSON, CSV,
offline and live-update exports. This writing pass is not a new open-status review.

The catalogue contains **7,228 records** in **34 selection categories**. The candidate pool is immediately
available in the default **Quick cards** view; archived records use the scope filter: a saved question or topic label,
source links, draft status, and a personal note. The **Full cards** layout keeps
the extended research presentation. No research record was duplicated to create
the quick view.

- **241 detailed research cards**, individually written with mathematical
  statements, context, reasons for importance, and dated references to progress.
- **2,353 source notes**, linked to their sources; these include approved research proposals, dated textbook/survey questions and mechanically screened excerpts.
- **4,634 legacy index records**, retained for traceability.

The 2,353 source notes and 4,634 index records appear as **6,987 short drafts**.
Some contain only a topic label or an incomplete excerpt; this is marked on the
card. Expanded details retain the previously saved material. **Add a note** opens
the personal note directly, and notes remain associated with the stable problem
ID when a card is developed further.

After publishing the quick view, four more detailed data-structure cards were
completed: LZ77 pattern matching (an existing-record upgrade), splay traversal,
constant-factor smallest-grammar approximation, and optimal decrease-key for
pure pairing heaps. All completed cards include substantial context, model
distinctions, and explanations of the remaining gap.

Every completed card states a precise yes/no proposition, an asymptotic
complexity target, or an exact-value question with its model and required precision. A visible “What would
settle it” section explains the resolution criterion. These fields also appear
in JSON and CSV exports. Older index entries and source notes are unfinished
material and do not yet satisfy this standard.

There are 2,533 additions to the original 4,695-record index. The multi-thousand
expansion into individually developed cards remains work in progress.

## Live publication

On the local HTTP server, the reader checks for completed cards every four
seconds. It preserves filters, expanded details, personal notes, and the current
reading position. Reload once if the page was opened before this feature was
added, or to load the new resolution-criterion section. File-based offline copies
are snapshots and do not poll for changes.

Use `?view=compact` for all quick cards and `?detail=drafts` for unfinished cards.
The detailed-card filter is available at `?detail=reviewed` and defaults to the
full layout. A direct link to a
card has the form `#TCS-6446`. Other filters cover topic, date, status, selection
criterion, additions, and saved cards. Multiple selected areas are combined by OR;
different filter types are combined by AND. Search matches every whitespace-
separated search term across statements, saved excerpts, definitions, context,
resolution criteria, and reference metadata.

## Interpreting claims

“Open in the dated source” is not a claim of verified open status today. The build
date is not the date of a new mathematical result. New preprint results are
attributed claims; their proofs were not independently verified. The detailed
cards record the scope of their literature review. No comprehensive proof audit
or exhaustive search for solutions has been performed.

The bipartite Exact Matching card records a 2026 claimed solution with uncertain
verification status. It is retained for traceability rather than counted as an
unqualified open question.

The old multipass pairing-heap delete-min question (TCS-6330) is now marked
resolved based on the 2023 preprint / 2025 journal result by Sinnamon and Tarjan.
It retains its historical excerpt and is still a source draft, not a completed
research card. Dated corrections to unfinished records are preserved separately
from the detailed-card layer.

Source notes preserve at most 25 words from each newly quoted paper. Truncation is
explicit. Their generic area context and structural selection criteria are marked
as heuristic; these do not replace a self-contained mathematical explanation or
problem-specific importance assessment. This distinction is visible in the UI.

Earlier collection searches favored areas underrepresented in the comparison with STOC
2022–2026 and FOCS 2021–2025 (1,546 papers). Counts of papers and counts of open
questions are different quantities. The comparison is a collection guide, not a
measure of importance. Topic classification is editorial, not official.

Identical question text, close same-source duplicates, and repeated paper titles
are screened. Automatic selection admits at most one new note per paper title.
Collection-wide semantic deduplication remains incomplete. Existing identifiers
are preserved; new identifiers are stored in a persistent registry.

## Local data and exports

Saved cards and personal notes use browser local storage. They are not uploaded.
Export selection includes the current records, saved flags, and personal notes;
use it to keep a portable copy. Browser storage may be cleared by the browser.

`catalog.json` is the complete structured catalogue; `data.js` wraps the same data
for offline loading. `catalog.csv`, `sources.csv`, `areas.csv`, and `coverage.json`
provide tabular exports and review counts. Downloaded reference books and surveys
are kept outside the atlas UI and are not bundled. CSV includes a `question_excerpt` column for
the saved source wording. Raw extraction candidates that have not been selected
as catalogue records remain research material outside the reader.

## Interface validation

An additional live-publication test simulates a new card through the polling
endpoint and checks scroll position, notes, focus, filters, and opened details.
All detailed cards were checked for math-rendering errors, citation IDs, and
the presence and display of their resolution criteria. These structural checks
do not certify the mathematical correctness of a formulation or cited proof.

Quick-view checks cover the full record count, short-draft filter, excerpt search,
direct links, mobile layout, and note preservation through a draft-to-reviewed
replacement. Compact presentation does not change a card’s evidence level.

Browser checks cover search, topic and review filters, empty states, mathematical
rendering, saved cards, persistent notes, JSON export, incremental loading,
distant-card links, keyboard access, mobile layout, and offline operation.
The initial complete dataset loaded in approximately 2–4 seconds in the test
environment. This is an observation, not a cross-device performance guarantee.

KaTeX is bundled locally under its MIT license (`vendor/LICENSE.katex`). No
analytics, account, external font service, or external JavaScript dependency is
required by the reader.

## Importance ordering

Editorial selection is the default order, including within every category. The
first 5/2 places form the Top 100 prefix, chosen for importance and diversity.
The rest follows importance scores, with resolved records last. Scores remain
unchanged when a problem is promoted for the focus selection. Editorial
assessments consider foundational significance, breadth of consequences, and
influence on other problems. The card shows its category position, with a reason
in its details. This is a subjective research judgment, not an objective score.
Unassessed drafts share a provisional midpoint and use stable IDs to break ties;
their relative positions will be refined as they are individually reviewed.
Category positions refer to the complete category even when filters are active.
Source age and publication date do not affect importance. Recently updated cards,
source-year sorting, and alphabetical order remain available separately.

Importance assessments made before the category migration are preserved. The
category-wide pass uses shared priority
bands for questions of comparable scope. It assesses the saved question and its
reach, not the correctness of a proof or current open status. The live counts in
the reader and `importance-overview.md` report assessed versus provisional
records. Records marked resolved are placed last while retaining their score.

Download `importance-ranking.csv` for the full compact ordering with reasons,
or read `importance-overview.md` for the first ten candidates per group.
All ranking exports are regenerated by the normal publication pipeline.


## Approved fundamental-problem proposals

All 170 retained proposals from the September 2026 searches have been added: 72 in large categories and 98 in small categories. This includes the latest 26 additions across 24 small categories. They carry English questions, primary-source links, editorial importance assessments and stable IDs; they remain short drafts until individually developed to the full research-card standard. Shared questions have only one card each.

[Browse the latest 26](fundamental-small-second-additions.md) · [Browse all 170 additions](fundamental-additions.md) · [JSON](fundamental-additions.json) · [CSV](fundamental-additions.csv).



## Textbook and survey questions

All 555 retained source annotations have been incorporated into the main catalogue:
472 new short drafts, 82 annotations supplementing 75 existing cards, and one
additional formulation attached to a new draft. The resulting 547 cards preserve
424 questions, 58 conjectures and 73 research directions from 47 publications.
Confirmed overlaps retain their existing IDs, statuses and personal-note identity.

Use **More options → Textbook and survey questions**, or open
[the filtered catalogue](index.html?collection=textbooks).
[The question-to-card mapping](textbook-additions.json) is also available as
[CSV](textbook-additions.csv). Full catalogue and selection exports include the
source annotations. Search includes their summaries, authors and source locators.

New entries are dated paraphrases, with provisional importance and unverified
present open status. Expand a card to read the source location and preserved
caveats. An annotation from an old source does not override a later card review.
Research directions and grouped variants remain explicitly identified.

The independent source library is outside this reader. Its pages, inventories,
PDFs and local links are absent from the site and portable archive. Publication
uses frozen question records; it does not require access to the library. Card
citations lead to the original external publications.

Review progress: 245 completed reviews; 6,983 remaining. Completed reviews include 4 individually justified dispositions.
