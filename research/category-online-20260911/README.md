# Replace the knowledge category with online algorithms

Approved by the user on 2026-09-11. The user requested removal of the knowledge
category and replacement by **Online algorithms**, not deletion of its problems.
The new small category has target 20 and sits between approximation and
beyond-worst-case analysis. The registry still has 10 large and 25 small
categories, with a total selection target of 1,000.

## Record decisions

The review covers 115 possible online records plus all 14 active records in the
retired category. Candidate discovery used saved titles, formulations, primary
source titles and the original online subject label. Each candidate was then read
individually; a keyword match is not a classification decision or a new verification
of open status. Saved working summaries helped interpret short excerpts.

| Movement | Records |
| --- | ---: |
| Optimization → Online algorithms | 70 |
| Scheduling and packing → Online algorithms | 5 |
| Geometry → Online algorithms | 5 |
| Knowledge → Computational complexity | 7 |
| Knowledge → Automated reasoning | 4 |
| Knowledge → Database theory | 2 |
| Knowledge → Counting and enumeration | 1 |

The resulting online pool contains 80 candidates; 94 records change category in
total. The other 35 screened candidates retain their specialist categories.
All decisions, including retained candidates and individual reasons, are in
[decisions.json](decisions.json) and the [readable table](review.md).

Representative moves include k-server (TCS-6575), convex body chasing (TCS-6576),
bandit convex optimization (TCS-6577), stochastic online bin packing (TCS-0705),
and irrevocable online metric embeddings (TCS-5747). SROIQ query entailment
(TCS-6680) moves to database theory; d-DNNF equivalence (TCS-6650) to automated
reasoning; DNF/d-DNNF succinctness (TCS-6681) to complexity; and hypergraph
transversal enumeration (TCS-7112) to counting and enumeration.

Boundary decisions preserve online learnability characterizations in learning
theory, privacy questions in differential privacy, quantum oracle questions in
quantum computation, locality/streaming questions in distributed and sublinear
algorithms, OMv in fine-grained complexity, and prediction-specific questions
in beyond-worst-case analysis. Data-structure operation bounds remain in ADS.

Two ambiguous cases were checked in their primary sources:

- TCS-2366 is the **offline** weighted k-server approximation question in
  [Discussion, item 2, PDF page 15](https://drops.dagstuhl.de/storage/00lipics/lipics-vol275-approx-random2023/LIPIcs.APPROX-RANDOM.2023.12/LIPIcs.APPROX-RANDOM.2023.12.pdf#page=15).
  It remains in approximation, despite the surrounding online results.
- TCS-3566 measures oracle calls until average **online regret** reaches epsilon,
  as defined in [Discussion, PDF page 12](https://proceedings.mlr.press/v125/hazan20a/hazan20a.pdf#page=12).
  It moves to online algorithms.

The mixed zeroth-order question TCS-4354 remains in optimization: its selected
[concluding passage](https://proceedings.mlr.press/v49/bach16.pdf#page=13) combines
dimension and sample-complexity questions with extensions beyond fixed-objective
optimization, rather than isolating one online guarantee.

## Publication and compatibility

- Current names and order remain in `categories.json`, using the new ID `online`.
- Frozen imports and old authored cards may retain historical subject keys.
  Import validation accepts those aliases and classification resolves the retired
  knowledge label to an appropriate current category.
- Archive manifests retain the former knowledge category as historical provenance.
  A later restoration uses the current taxonomy. No archive decision is changed.
- The online Top 100 pair is k-server and bandit convex optimization, covering
  competitiveness and partial-feedback regret. The packing versus max-flow min-cut
  conjecture (TCS-7227) fills the former k-server place in optimization.
- Importance scores, stable IDs, statements, statuses and working summaries are
  preserved. Summary exports follow the new groups without moving authoring files.

## Verification

verify.py compares the published migration with
`before.json.gz`, checks the exact 94 movements, unchanged archived records,
research content, quotas and Top 100/1000 exports. Results are written to
verification.json. A concurrent authoring session revised
context paragraphs on ten canonical cards during this review; the verifier checks
those exact revisions against both the saved differences and canonical files.
It separately reruns this category change on the frozen baseline to establish that
the migration itself changes no research content. See
concurrent-content-changes.json.

browser.cjs checks the category filter, search, card labels, downloads,
Top 100/1000, mobile and offline rendering. It also simulates a live reader with the
old knowledge filter selected and a focused personal note: publication removes the
obsolete filter while preserving the note and showing the card in its new category.
Results are in browser-validation.json.

The repository taxonomy checks additionally exercise legacy source imports,
online/specialist boundaries, and restoration from a retired-category archive.
The full `make check` result is recorded in checks.json.
