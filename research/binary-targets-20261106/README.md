# Green-card targets, 6 November 2026

The owner requested meaningful binary questions for green cards about optimal
algorithmic and asymptotic bounds, with exact Euclidean MST and edit-distance
distortion as examples. They subsequently clarified that a numerical optimum
without a natural conjectural endpoint should remain an optimum to absolute
accuracy 0.01. Polynomial-growth questions should request a finite exponent
to that accuracy, without matching logarithmic factors. Direct capacities,
values and the exact witness-based BB(6) criterion remain unchanged.

The initial shared-selection snapshot had 508 effective green cards. Screening
identified 62 numerical, asymptotic or classification candidates. Thirteen
additional cards turned green during the session and were checked before
publication. Of these 75 individually recorded decisions, 38 revise statements
and 37 retain their existing targets. Already binary cards outside this
candidate set did not need rewriting. This was a formulation review, not the
deferred catalogue-wide search for newly solved problems.

The final live-selection check also inspected six subsequently green cards:
TCS-6612, TCS-6613, TCS-7220, TCS-7223 and TCS-7507 already have binary targets;
TCS-7210 is a direct interference-channel capacity function with the approved
0.01 criterion. No further statement edits were needed for these six.

## Revised targets

Thirty-one cards now ask a concrete yes/no question. These include matrix
multiplication exponent two, logarithmic separating automata, near-linear
exact Euclidean MST and planar matching, the Cerny conjecture, polynomial-sample
trace reconstruction, factor-two superstring approximation, and matching
log-log decrease-key charges for the standard two-pass pairing heap.
`decisions.json` records every target, model choice and source URL.

Seven cards request finite exponents to absolute error 1/100:

| Card | Exponent |
| --- | --- |
| TCS-0318 | Uniform k-set dependence after factoring out the linear number-of-points term |
| TCS-6526 | Weak epsilon-net size in inverse accuracy, for each fixed dimension |
| TCS-6683 | Excluded-grid treewidth threshold in grid side length |
| TCS-6710 | Number-on-forehead disjointness communication in universe size, for each fixed player count |
| TCS-6785 | Additive-spanner error for each fixed genuinely linear edge budget |
| TCS-7184 | Exact Klee-measure deterministic real-RAM time, for each fixed dimension |
| TCS-7319 | Ordinary sequential calibration error in the horizon |

These are infima of power upper bounds. Their definitions do not assume an
ordinary growth limit, attainment of an infimum, or exact logarithmic factors.
In TCS-6710, fixed player counts replace the former request for a uniformly
sharp growing-player tradeoff; that specialization is explicit. In TCS-7184,
each bound must come from one uniform algorithm, rather than pointwise
hardcoding separate input sizes. The owner had turned TCS-7319 red during the
review; its authorized wording change is retained without restoring its color.

No arbitrary 0.45 approximation or cubic randomized-versus-quantum exponent
was selected. Existing numerical optima, including submodular approximation
ratios and online bin packing, keep their 0.01 acceptance criteria. Structural
classification questions remain classifications. TCS-0724, TCS-1029,
TCS-5651 and TCS-7447 retain their broader targets: a finite scalar replacement
would require choosing a parameter regime, a pattern, one of two recognition
tasks, or a policy-class family. Those choices were not invented in this pass.

## Explicit follow-up requests

TCS-6500 was removed from the active catalogue at the owner's request, retaining
the green TCS-2783 as the Erdős girth conjecture card. The archived record and
reason remain in `data/archive/`. The two saved statements differed in graph
order quantifiers (all sufficiently large orders versus an unbounded sequence),
so the archival reason records overlapping coverage rather than claiming
literal equivalence. The source selection default for TCS-6500 was removed.
Its historical shared override is left in storage and ignored as inactive.

TCS-7328 asks for a single total-work bound with constant make-heap, insert,
meld and find-min charges, logarithmic delete-min, and log-log decrease-key.
It fixes the standard two-pass algorithm and counts links, cuts and operation
overhead. Fredman's 1999 lower bound is checked through Iacono's primary paper
(arXiv:1110.4428v3, Introduction and Figure 1), which states its dependence on
the other-operation charges. No new audit of Fredman's complete proof is
claimed. Results for pure, smooth, slim or other modified heaps do not settle
this card.

## State preservation and reproducibility

`selection-before.json` is the initial shared snapshot;
`selection-before-publication.json` records the later choices, including the
subsequently archived card. `scope.json` records the approved scope and its
clarifications. `before/` preserves prior card bodies. `revise.py` and its
supporting scripts reproduce the statement edits from those before-images;
they deliberately do not modify shared selection state or archive cards.

The source defaults remain 504 green and 644 red across 1,148 active cards,
with 35 categories and 480 two-category pairs. Effective shared counts may
differ as the owners edit them. No green replacement, quota rebalancing,
manual vote transfer or automatic recoloring accompanies the deletion.

The selection-service change only removes the archived ID from its manifest.
It introduces no database migration, API change or access change. Public
editing, card revisions and retry behavior remain in place.

Validation and production identifiers are recorded in `verification.json`.
