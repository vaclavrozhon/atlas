# Fundamentality screen — 11 September 2026

Removed **498 cards** in five published batches after a quick editorial screen
covering **1,731 distinct entries**. The user requested approximately 500 further
removals of insufficiently fundamental problems and explicitly excluded category
counts from the selection decision. This run is separate from the earlier
source-status and formulation pruning runs.

The canonical catalogue contained **2,266 cards** at final validation. Other work
added, reviewed and removed cards concurrently, so this count is not simply the
initial count minus 498. Two screened entries, TCS-0475 and TCS-0513, were removed
by another process and are excluded from this run's removal count.

## What was removed

Each card has one primary reason type for reporting. These types describe the
editorial reason for exclusion, not the card's subject category. Individual
reasons, including distinctions within a type, are in [removals.json](removals.json).

| Primary reason | Cards | Typical scope and example |
| --- | ---: | --- |
| Specialized model | 121 | A particular model, objective or logical variant without enough demonstrated wider consequences. TCS-5220: Weighted All-Or-One Paging with heterogeneous cache eligibility. |
| Research direction | 102 | A topic collection, open-ended extension or search for a model/method instead of one fixed consequential target. TCS-0955: designing models combining streaming and online algorithms. |
| Restricted instance | 89 | A narrow combination of graph class, parameter or representation restrictions. TCS-5884: a minimum isometric-universal graph for two outerplanar graphs. |
| Parameter refinement | 68 | A local improvement to an exponent, constant, parameter dependence or asymptotic estimate. TCS-0480: the expected redundancy constant of alphabetic trees under Dirichlet weights. |
| Construction variant | 54 | An extra constraint or modification of one algorithm, representation or proof method. TCS-4484: geodesic star unfolding using a source curve. |
| Technical subproblem | 44 | An auxiliary estimate, reduction or construction whose saved significance remains tied to another result. TCS-6131: a path-decomposition construction supporting a parameterized-completeness argument. |
| Combinatorial side question | 20 | Extremal or enumerative questions with insufficient computational motivation for this atlas. TCS-0404: comparing counts of pointed pseudotriangulations and triangulations. |
| **Total** | **498** | |

These are judgments under the user's stricter selection threshold. A removal
does not assert that the problem is solved, uninteresting, easy, or unimportant
to its specialist community. Detailed prior review did not automatically protect
a card from this selection screen.

## What was preserved

Precise nonbinary questions remained eligible when their scope and consequences
were substantial. Examples retained in the screened set include TCS-6577
(optimal dimension dependence for convex-bandit regret) and TCS-6610
(the Shannon capacity of C7). General barriers such as TCS-6510 (truly subcubic
APSP), TCS-6600 (optimal generators for read-once branching programs), and
TCS-6541 (linear-size sample compression) were also retained.

Restrictions and technical wording were reading cues, not deletion rules.
TCS-4461 was retained for its foundational relationship between extensionality
and univalence. TCS-2519 was retained after reading the wider secret-sharing
target, despite its appearance as a supporting construction question.
Incomplete formalization alone did not determine exclusion.

## Scope and execution

This was a quick selection pass using saved statements, working summaries and
significance notes. It was not a fresh literature search, current-status review,
or full mathematical formulation review. The text-based reading order brought
potentially local questions forward; it did not select removals. No category
counts, category quotas, provisional scores or formalization effort were used
to decide exclusions.

[ledger.json](ledger.json) records the 1,731 screened IDs: 498 removed here,
1,231 with no removal selected, and two removed concurrently. A retained
disposition does not certify formulation, importance or present openness.
This targeted pass does not claim a new review of every catalogue card.

A temporary helper applied the individually selected IDs and reasons, checked
card hashes before deletion, preserved the canonical ID-and-reason deletion log,
and regenerated publication outputs. It stopped when TCS-0475 had already been
removed; that entry was excluded from this run before continuing. No selected
focus choices needed removal, and no choices or quotas were automatically refilled.
Historical ID mappings were left intact. No restoration archive of card records
was created.

## Validation and audit files

`make check` and `make check-web` passed on publication version
`cd925196b4a88ab8a663`. These checks include publication and export consistency,
reserved deleted IDs, stale-import protection, nested selections and browser
deletion behavior. Deployment checks used a temporary local test repository.

After concurrent publication changes, a direct audit on version
`0ad5f2145f3839f9b7be` confirmed that all 498 IDs were absent from canonical card
files, catalogue JSON/CSV, offline JavaScript, ranking CSV, all three benchmark
exports, the statement export and textbook card references. Every saved removal
reason matched the canonical deletion log. Full tests were not repeated for
unrelated concurrent edits.

- [applied.json](applied.json): exact applied reasons with date and saved source provenance.
- [removals.json](removals.json): individual editorial reasons and report types.
- [batches.json](batches.json): five applied batches, IDs, counts and publication versions.
- [concurrent-removals.json](concurrent-removals.json): exclusions from this run's count.
- [ledger.json](ledger.json): quick-screen dispositions.
- [validation.json](validation.json): counts, versions and verification results.

The canonical removal register remains
[data/deleted_records.json](../../data/deleted_records.json).
