# Five GPT and five Claude additions

The user approved approximately five additions from each proposal set on
11 September 2026. Ten new completed cards were individually authored and
published, each with a precise target, definitions, answer criterion, primary
references, dated progress, status limits and an editorial importance assessment.
All mathematical content is in English.

## Selection

| Origin | Proposal | ID | New target | Current bucket |
|---|---|---|---|---|
| GPT | V4.3 | TCS-7228 | Exact maximum flow with polylogarithmic overhead | Structural graph theory and graph algorithms |
| GPT | V6.1 | TCS-7229 | Classical key agreement from one-way functions | Cryptography |
| GPT | V9.4 | TCS-7230 | Decidability of the real exponential field | Semantics, logic and verification |
| GPT | V10.2 | TCS-7231 | Polynomial-time rational P-matrix LCP | Optimization and numerical computation |
| GPT | M20 | TCS-7232 | Asser’s spectrum-complement problem | Database theory and finite model theory |
| Claude | M2 | TCS-7233 | General binary-weighted TSP below base two | Parameterized complexity and algorithms |
| Claude | M9 | TCS-7234 | Quantum polynomial-factor Euclidean SVP | Lattices and computational number theory |
| Claude | M11 | TCS-7235 | Near-exact edit distance in n^(1+o(1)) time | String algorithms and computational biology |
| Claude | M15 | TCS-7236 | Polynomial-time private release of all marginals | Differential privacy |
| Claude | M17 | TCS-7237 | NP-hardness of PCSP(K₃,K₆) | Constraint satisfaction |

The GPT selection spans graph optimization, cryptographic assumptions,
real-analytic decision, complementarity and finite-model-theoretic closure.
The Claude selection adds independently meaningful targets in exact algorithms,
quantum computation, sequence comparison, privacy and promise CSP. The sixth
Claude candidate, greedy CDCL without restarts, is not included in this batch;
private query release adds a different statistical-computational question, while
the catalogue already contains several central proof-system questions.

These are additions to the active candidate catalogue, not an automatic change
to the jointly selected Top 100 focus prefixes. Existing scores and the
`benchmark_selection.json` choices are preserved. New non-focus positions follow
the usual importance ordering. Current positions are in verification.json.

## Source checks and exact variants

- **Maximum flow:** the 2022 almost-linear result and
  [Li–Wice, August 2026](https://arxiv.org/abs/2608.17384) state m^(1+o(1)),
  not a fixed polylogarithmic overhead. The card allows randomized classical
  computation, polynomially bounded integer capacities and m+n input size.
  The current graph-category expansion governs placement.
- **Key agreement:** the [2021 black-box-uselessness paper](https://eprint.iacr.org/2021/016)
  states restricted black-box results. The new card asks the unrelativized
  classical existence implication under an explicit uniform passive-adversary
  definition. It is separate from the existing stronger PKE-from-OWF target.
- **Real exponential field:** the [June 2026 revision](https://arxiv.org/abs/2603.08365v2)
  still assumes Schanuel’s conjecture for decidability of the full theory.
  The new question is unconditional and does not restrict exp to an interval.
- **P-matrix LCP:** the [ETH 2025 report](https://ti.inf.ethz.ch/ew/report/2025.html)
  retains the general polynomial-time problem. The card asks for exact rational
  output under a P-matrix promise, not recognition of that promise.
- **Asser:** the [Durand–Jones–Makowsky–More survey](https://arxiv.org/abs/0907.5495)
  supplies the spectrum-complement question. The new sentence may change
  vocabulary; no effective transformation is required. Later-work searches found
  no general resolution, but are not claimed to be exhaustive.
- **TSP:** [Stoian 2024](https://arxiv.org/abs/2405.03018v2) improves a prefactor
  while retaining base two. The target permits bounded-error classical
  randomization and only polynomial dependence on weight encoding length.
- **Quantum SVP:** [Regev](https://arxiv.org/abs/2401.03703) establishes a
  directed implication involving specified GapSVP/SIVP and LWE parameters.
  The new approximate search target is not equated with arbitrary LWE breaking;
  rational-basis conventions match the existing classical approximation card.
- **Edit distance:** [Mao–Rubinstein 2026](https://arxiv.org/abs/2603.29702)
  does not establish the joint near-exact, near-linear target. The card defines
  one algorithm for each fixed accuracy and states the n^(1+o(1)) quantifiers.
  It preserves both earlier edit-distance targets.
- **Private marginals:** Vadhan’s Open Problem 7.8 and
  [Chandrasekaran–Thaler–Ullman–Wan](https://arxiv.org/abs/1304.3754) motivate
  the all-orders target. The card explicitly chooses replacement adjacency,
  (1,1/(100n²))-DP, n=d^C, vanishing simultaneous error, and a polynomial-size
  non-synthetic synopsis with a deterministic polynomial-time evaluator.
  This is one recorded interpretation, not a claim of equivalence among every
  interactive, fixed-k and synthetic-data formulation. The explicit open-problem
  reference is older, and status limits are stated on the card.
- **3-versus-6 colouring:** [Brandts–Živný 2021](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.121)
  explicitly discusses six-colouring promised three-colourable inputs.
  The new target is an unconditional deterministic polynomial many-one
  reduction from 3-SAT to the associated promise decision problem.

The primary statements and model boundaries were checked; this work does not
independently verify every cited proof or formally prove current openness.
No attempted solutions, recommended approaches or suggested intermediate
milestones are inserted into the problem statements.

## Correction to the earlier GPT audit

The earlier audit said that the connection between Matroid Secretary and the
saved universal contention-resolution question was not known to be an
equivalence. That assessment stopped at the 2020 source and was incomplete.
[Dughmi’s ITCS 2022 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.58/LIPIcs.ITCS.2022.58.pdf)
proves the equivalence in the known-matroid, random-order, fully-known-prior
setting. Its introduction explicitly identifies the missing converse from the
2020 paper. Therefore this batch does not add Matroid Secretary as another
independent question beside the saved TCS-5779 contention-resolution target.
Asser’s problem takes that proposed place. TCS-5779 remains a source record;
its historical content is preserved rather than silently promoted to a new
completed formulation.

## Verification

[added.json](added.json) records provenance and stable IDs.
verify.py checks ten genuinely new IDs, five per origin, precise-card
fields, reference consistency, active buckets, canonical/export agreement,
preservation of existing research content and the focus selection.
The baseline keeps hashes of the checked content fields after verification,
rather than duplicating the full catalogue.

The standard `make check` publication/ranking/taxonomy/import checks and a
browser check exercise the published reader. Results are
saved alongside this report.

Completed validation: `make check` passed, all ten cards rendered with definitions
and references, the mobile viewport had no horizontal overflow, and no browser
errors were recorded. The catalogue grew from 7,218 to 7,228 records; the saved
research fields of all previous records and the focus selection were unchanged.
See checks.json and make-check.log.
