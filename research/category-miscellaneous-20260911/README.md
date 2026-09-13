# Miscellaneous: review of all active categories

User-requested on 2026-09-11. Rename the final category from **Unclassified problems**
to **Miscellaneous** and use it for worthwhile problems that are difficult to place
in the named disciplines. The stable ID/key, last position, target 20 and two
focus places are preserved.

## Coverage

The first pass screened the titles and category assignments of **all 2,747 active
records across 35 categories**. It reused the immediately preceding full ADS and
graph-category inventory, then inspected every remaining active title. It also
checked historical source categories and saved-question signals for unconventional
computing models and combinatorial boundary topics.

Sixteen boundary cases received a closer reading of their saved formulations,
source excerpts, working summaries and source metadata. This is a category audit,
not a claim to have reread every source paper or freshly verified current open status.
Incomplete statements alone do not justify a move to Miscellaneous.

The complete [CSV inventory](inventory.csv) and [JSON inventory](inventory.json)
record every screened ID, original current category, decision and destination.
[Detailed decisions](decisions.json) preserve prior overrides and focus choices.

## Transfers

| ID | Problem | Previous category | New category |
| --- | --- | --- | --- |
| TCS-7177 | The 1/3–2/3 conjecture | Algorithms & data structures | Miscellaneous |
| TCS-7178 | The gold partition conjecture | Algorithms & data structures | Miscellaneous |
| TCS-7176 | Determine the pancake numbers | Algorithms & data structures | Miscellaneous |
| TCS-1951 | Can execution bounded CRNs compute semilinear functions and predicates within polylogarithmic time? | Computational complexity | Miscellaneous |
| TCS-3520 | Does every class C with unbounded grid-width contain arbitrarily large connected monotone grid subclasses? | String algorithms and bioinformatics | Miscellaneous |
| TCS-7222 | Is graph isomorphism solvable in polynomial time? | Miscellaneous | Structural graph theory |

Miscellaneous now has five records: three extremal questions involving partial
orders or permutations, one structural question about permutation classes, and
one question about execution-bounded chemical reaction networks. Classical graph
isomorphism has a clear home alongside graph canonization in the expanded graph
category, so it moves out.

## Boundary decisions

| ID | Decision | Reason |
| --- | --- | --- |
| TCS-7177 | move | An extremal balance statement about all finite partial orders. Its sorting application motivates retention, but the target is a combinatorial existence theorem rather than a data structure or running-time bound. |
| TCS-7178 | move | An extremal guarantee on two successive partitions of the linear extensions of a partial order. Keep this beside the 1/3–2/3 question as a computationally motivated combinatorial boundary case. |
| TCS-7176 | move | The requested output is the exact extremal prefix-reversal distance over all permutations, rather than an efficient sorting implementation. It spans permutation combinatorics and restricted operations without requiring an algorithmic target. |
| TCS-1951 | move | Execution-bounded chemical reaction networks use stochastic molecular timing and require all reaction sequences to cease. This unconventional computing model crosses complexity, distributed protocols and chemistry without a dedicated specialist category. |
| TCS-3520 | move | The target is a structural containment theorem for permutation classes of unbounded grid-width. Its pattern-matching application does not make it a string algorithm, and its grid parameter is not an ordinary graph-width question. |
| TCS-7222 | move | Classical polynomial-time graph-isomorphism testing has a clear home in the newly expanded static graph-algorithm category, alongside graph canonization. |
| TCS-3308 | retain | The Hex question asks for polynomial-size strategy circuits, so circuit complexity directly defines the target despite the game application. |
| TCS-4219 | retain | The target is a gate-count versus workspace tradeoff for reversible Boolean circuits, directly within computational complexity. |
| TCS-4927 | retain | The saved question concerns quantum gate sets and intermediate quantum complexity classes, despite the classical-sounding paper title. |
| TCS-5103 | retain | The saved source asks for optimal static search trees in polynomial time. The associahedron title does not replace this direct data-structure target. |
| TCS-5959 | retain | The saved question is the complexity of the limit language of a cellular automaton; it has a defined automata-theoretic target. |
| TCS-7159 | retain | A real-time multitape Turing-machine restriction is the defining hypothesis. Keep the digit-generation/transcendence question in computational complexity. |
| TCS-6064 | retain | Characterizing limit sets of cellular automata is directly about a specified automaton model. |
| TCS-6158 | retain | The implication between invariant-measure uniqueness and convergence is posed specifically for deterministic cellular automata. |
| TCS-0312 | retain | The target is enumeration and asymptotic counting of finite polyominoes, which fits Counting and enumeration. |
| TCS-0117 | retain | A simultaneous edge decomposition of cubic graphs is directly structural graph theory. |

## Focus and verification

The Miscellaneous Top 100 pair is **TCS-7177 (1/3–2/3)** and
**TCS-7176 (pancake numbers)**. Gold partition remains in the larger pool to avoid
using both focus places for partial-order balance. The chemical-network and
permutation-grid records remain provisional drafts with their original scores.

The migration neither restores archives nor adds records. Statements, references,
statuses, evidence, importance scores and original source categories are preserved.
The 12 graph transfers and the graph focus pair from the preceding request remain
in effect. Verification covers exact movements, preservation,
category counts and focus/export consistency. Browser checks
cover labels, filtering, downloads, Top 100/1000 and mobile layout.
