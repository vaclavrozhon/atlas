# Approved graph and Chan problems

Applied on 13 September 2026 after the user approved all fifteen proposed targets.
The result is eleven new canonical cards and four updates to existing cards.
All cards have explicit mathematical targets, computational or representation
models, answer criteria, references, dated progress, individual formulation
reviews, importance assessments and five-sentence summaries.

The [original report](README.md) retains the researcher associations and source
discussion. [import-result.json](import-result.json) records the allocated stable
IDs. Canonical card files are the sole editable problem sources; this report is
provenance and is not part of the publication pipeline.

| Proposal | Canonical card | Action | Category |
| --- | --- | --- | --- |
| G1 | [TCS-7341: Strongly polynomial near-linear negative-weight shortest paths](../../data/cards/TCS-7341.json) | Added | Structural graph theory and graph algorithms |
| G2 | [TCS-7342: Steiner Shortcut Conjecture](../../data/cards/TCS-7342.json) | Added | Structural graph theory and graph algorithms |
| G3 | [TCS-7343: Deterministic almost-linear vertex connectivity](../../data/cards/TCS-7343.json) | Added | Structural graph theory and graph algorithms |
| G4 | [TCS-7344: Almost-linear exact directed global minimum cut](../../data/cards/TCS-7344.json) | Added | Structural graph theory and graph algorithms |
| G5 | [TCS-7345: Almost-linear directed vertex connectivity](../../data/cards/TCS-7345.json) | Added | Structural graph theory and graph algorithms |
| G6 | [TCS-7346: Strongly polynomial maximum flow below the mn barrier](../../data/cards/TCS-7346.json) | Added | Structural graph theory and graph algorithms |
| G7 | [TCS-7263: Linear-time directed shortest paths with nonnegative real weights](../../data/cards/TCS-7263.json) | Consolidated into existing card | Structural graph theory and graph algorithms |
| G8 | [TCS-7347: Directed unweighted APSP below the five-halves exponent](../../data/cards/TCS-7347.json) | Added | Fine-grained complexity |
| G9 | [TCS-7348: Single-exponential exact cut mimicking networks](../../data/cards/TCS-7348.json) | Added | Structural graph theory and graph algorithms |
| G10 | [TCS-7349: Almost-linear-work parallel exact maximum flow](../../data/cards/TCS-7349.json) | Added | Distributed, parallel and sublinear algorithms |
| C1 | [TCS-7350: Near-linear output-sensitive Subset Sum](../../data/cards/TCS-7350.json) | Added | Algorithms |
| C2 | [TCS-7351: Linear-time exact inversion counting](../../data/cards/TCS-7351.json) | Added; current status marked uncertain | Algorithms |
| C3 | [TCS-6598: Min-Plus Convolution Hypothesis](../../data/cards/TCS-6598.json) | Completed existing draft | Fine-grained complexity |
| C4 | [TCS-0388: Sorting X + Y](../../data/cards/TCS-0388.json) | Retained full formulation; recorded association and convolution relation | Algorithms |
| C5 | [TCS-4790: Subset Sum below the meet-in-the-middle exponent](../../data/cards/TCS-4790.json) | Completed existing draft | Parameterized complexity and algorithms |

The fifteen targets therefore occupy eight graph slots, three Algorithms slots,
two Fine-grained complexity slots, one parallel slot and one parameterized slot.
These are candidate-pool additions, not manual promotions into benchmark focus
prefixes. Existing assessed importance scores were retained; the previously
unassessed exponential Subset Sum draft received its first individual assessment.

## Formulation decisions

- G1 explicitly fixes arbitrary real weights, near-linear comparison-addition
  time, bounded-error randomization and a numerical-magnitude-independent bound.
  The added [February 2026 preprint](https://arxiv.org/abs/2602.16153) gives
  \(n^{2+o(1)}\) real-weight time, which does not settle this sparse-graph endpoint.
- G2 follows Conjecture 2, including polylogarithmic rather than merely
  subpolynomial diameter. It asks only for existence, permits arbitrarily long
  runs of Steiner vertices and preserves only the original reachability relation.
- G3 and G5 specify complete-graph, disconnected-graph and singleton conventions.
  G3 requires determinism in undirected graphs; G5 permits randomness in digraphs.
- G4 returns an exact global outgoing cut under polynomial integer weights.
  Approximation precision and unknown terminals distinguish it from fast
  approximation and single-pair flow results.
- G6 fixes finite rational capacities, bounded error, worst-case arithmetic
  operation count and polynomial intermediate bit space. Its fixed exponent
  improvement is explicitly posed in the cited SODA 2026 paper.
- G7 replaces the former positive-integer word-RAM target on TCS-7263 with the
  approved nonnegative-real comparison-addition target. This is a documented
  change of model, not an asserted equivalence. The prior formulation remains
  in the card's formulation history; the old ID and assessed score are preserved.
- G8 fixes the requested unconditional five-halves threshold; it does not assume
  matrix multiplication exponent two or the hypotheses of the 2026 equivalence.
- G9 asks specifically for \(2^{Ck}\) vertices for a universal constant, and allows
  arbitrary replacement graphs. Contraction-only lower bounds and pairwise
  Gomory–Hu preservation concern different targets.
- G10 uses a uniform priority CRCW word PRAM, worst-case work and depth on every
  random execution, bounded error and polynomially bounded integer capacities.
- C1 measures the explicit multiset input plus its distinct truncated sumset.
  Its Algorithms placement reflects the basic pseudopolynomial computation and
  convolution connection; it does not ask for the number of subsets.
- C2 uses deterministic exact counting on logarithmic words. Its formulation is
  complete, but current openness is marked uncertain: the direct evidence is
  mainly Chan–Pătraşcu (2010) and [Elmasry (2015)](https://arxiv.org/abs/1503.01192).
  No exact linear-time result was identified in the September 2026 search.
- C3 preserves the integer-word target and adds complete array indexing,
  magnitude quantifiers and error conventions. The 2026 monotone convolution
  result has restrictions absent from this target.
- C4 was already complete. Its real-RAM target, evidence and assessment were
  preserved; a substantive relation to min-plus convolution was added.
- C5 requires a fixed exponential saving on every classical input, with
  polynomial dependence on binary length. Quantum, average-case,
  pseudopolynomial and polynomial-factor improvements are distinguished.

The supplementary researcher and textbook matches mentioned in the original
report already have catalogue identities; no duplicates were created for them.
All new relationships have a structural or computational basis, and the
publisher derives their reverse links.

## Validation

The canonical importer accepted all fifteen records and reserved eleven new
stable IDs. A direct check confirmed that all fifteen current formulations
appear in the generated catalogue, have five-sentence summaries and belong to
the intended existing categories. `make check` passed the isolated rebuild,
ranking, taxonomy, related-card, import, publication and local deployment
regressions. `node tests/math.cjs` passed for all 1,041 active cards and 11,053
expressions, including balanced delimiters and formula-safe previews. During
the first run a concurrently edited card outside this batch had an unsupported
LaTeX command; its owning work corrected it and the complete rerun passed.
`git diff --check` passed, and `make publish` rebuilt the local reader and exports.
These checks validate the data pipeline and rendering, not the truth of open
conjectures or independent proof verification of cited papers.
