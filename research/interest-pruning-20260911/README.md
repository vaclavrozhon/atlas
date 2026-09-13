# First interest screen toward approximately 800 cards

Completed on September 11, 2026. The user requested a first removal of a few
hundred insufficiently interesting problems, without protecting early ranks or
balancing the resulting category sizes.

**300 cards removed; 2,277 → 1,977 canonical cards.** These counts exclude earlier
pruning passes. The removals were applied in groups of 131, 110 and 59.

## Decisions and scope

[decisions.tsv](decisions.tsv) records all 300 IDs with individually authored
English reasons. The corresponding permanent reasons are in
[data/deleted_records.json](../../data/deleted_records.json). The removed card
files are absent; this review contains no full-card restoration copies.

The content screen covered 493 distinct cards. Of these, 193 were read without
being selected for removal in this batch. That is not a certification that they
belong in the eventual 800. The remaining cards have not received this batch's
content review.

The main removal grounds were narrow refinements of a stronger retained target,
questions about one particular proof or algorithmic method, specialized model
and parameter combinations, and topic-level research directions without a
selected major proposition. Redundant formulations of an already represented
problem were also removed. Incomplete wording alone did not disqualify a strong
problem; important targets with unfinished statements remain for later work.

The review used saved questions, available definitions, substantive motivation
and importance notes, working summaries, and source titles and locators. The
reading aid displayed at most the first 800 characters of definitions. It did
not systematically reopen papers or freshly verify present-day open status.
Removal reasons are editorial judgments, not resolution claims.

## Early-ranked removals

Ranks below are the within-category positions at the start of this batch,
before deletions changed the ordering. The thresholds are cumulative.

| Original position | Removed |
| --- | ---: |
| First 5 | 4 |
| First 10 | 23 |
| First 15 | 49 |
| First 25 | 99 |

Removals span 26 categories. Category counts were measured after selection;
they were not quotas or selection criteria. Examples include final-survivor
queries for offline heaps (TCS-0477, originally fourth), the specific
conditional-information guarantee for proper agnostic learning (TCS-0679,
fifth), pancake numbers (TCS-7176, second), fixed-method Shellsort bounds
(TCS-7173, ninth), and monotonicity path-tester characterization (TCS-1026,
seventh).

Three explicit focus choices were removed: TCS-0477, TCS-0679 and TCS-7176.
Their positions require new editorial review; no replacements were certified.
The existing rank-based Top 100 export still contains 100 cards and reports
three unreviewed focus places. Category quotas and the nested selection rules
were preserved. Top 500 currently contains 495 cards; the possible Top 1000
export contains 966.

The approximately 800-card candidate-pool target and the lack of protection for
early ranks are recorded in [docs/RULES.md](../../docs/RULES.md). This target is
separate from the existing benchmark export quotas.

## Validation

- `make publish` completed and refreshed the local reader and exports.
- `make check` passed: ranking, taxonomy, clean rebuild, publication stability,
  export parity, deleted-ID protection, deletion deltas and deployment fixtures.
- `make check-web` passed: browser navigation, nested selections, live removal,
  missed-delta recovery, contribution-state preservation and the notes service.
- A direct membership audit verified that exactly these 300 baseline identities
  are absent, their permanent reasons match, and no removed identity remains as
  an active record in the catalogue, CSVs, offline JavaScript, benchmark exports
  or solver-facing statements.

The first offline check exposed an old test assumption that every focus place
must be filled. [tests/ranking.py](../../tests/ranking.py) now accepts only
accurately reported vacancies while still rejecting invalid surviving choices
and unexpected issues. Its invalidation tests check the specific new issue,
so existing vacancies cannot mask a regression. The subsequent full check passed.

One pending card, TCS-7188, changed during the review. The hash check stopped the
pending batch before any deletion; the revised statement and summary were read
again, and the editorial removal decision was retained.

## Supporting files

- [validation.json](validation.json): counts, rank statistics and verification results.
- [applied.json](applied.json): applied IDs, full removal reasons and batch boundaries.
- [baseline.json](baseline.json): initial IDs, category ranks, scores and focus flags.
- [read-ledger.json](read-ledger.json): reading scope and hashes, including retained candidates.
- [review.py](review.py): local reading aid and checked deletion application; it does not restore cards.
