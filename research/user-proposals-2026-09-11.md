# User-proposed coverage additions, 11 September 2026

Compared the ten proposals against canonical cards, historical keys, and reserved
deleted IDs before importing. Added six distinct targets. Four exact targets were
already present. The user explicitly authorized Miscellaneous where appropriate.
Category quotas and editorial focus choices were not changed.

| Proposal | Disposition | Card | Category |
| --- | --- | --- | --- |
| 1. Nondirected planar temperature-1 universality | New candidate; simulation convention needs specification | [TCS-7255](../data/cards/TCS-7255.json) | Miscellaneous |
| 2. Polynomial-time, linear-total-space reversible simulation | New card; historical openness evidence | [TCS-7256](../data/cards/TCS-7256.json) | Computational complexity |
| 3. Binary noisy-circuit threshold | New card; historical openness evidence | [TCS-7257](../data/cards/TCS-7257.json) | Computational complexity |
| 4. Polylogarithmic amoebot reconfiguration | New card | [TCS-7258](../data/cards/TCS-7258.json) | Miscellaneous |
| 5. Planar single-grain sandpile prediction | New card; NC-membership target | [TCS-7259](../data/cards/TCS-7259.json) | Distributed, parallel and sublinear algorithms |
| 6. Li–Li multiple-unicast conjecture | Already covered, including the August 2026 reference | [TCS-6584](../data/cards/TCS-6584.json) | Coding and information theory |
| 7. Polynomial-size d-DNNF complementation | New nonuniform target; linked to existing algorithmic question | [TCS-7260](../data/cards/TCS-7260.json) | Computational complexity |
| 8. Word equations with linear length constraints | Already covered, including IJCAR 2026 | [TCS-6562](../data/cards/TCS-6562.json) | Automated reasoning, rewriting and unification |
| 9. Conjunctive-query containment under bag semantics | Already covered | [TCS-0492](../data/cards/TCS-0492.json) | Database theory and finite model theory |
| 10. Constant approximation for smallest grammar | Already covered, with the same size convention | [TCS-6513](../data/cards/TCS-6513.json) | String algorithms and computational biology |

## Formulation and evidence decisions

- **Tile assembly:** the [2021 primary paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.DNA.27.6)
  leaves nondirected computational power open. Its directed impossibility result
  does not settle the proposal. Probabilistic success and bounded or intrinsic
  simulation are different targets. The input/readout and correctness quantifiers
  for reliable asynchronous simulation were not recovered precisely enough to
  certify a benchmark statement; the new card retains `evidence: source` and
  `statement_review.status: needs_specification`.
- **Reversible simulation:** total space counts the input and output. The target
  is one general effective compiler with simultaneous polynomial time and linear
  space, preserving the input. The [2005 survey](https://homepages.cwi.nl/~paulv/papers/wrc05.pdf)
  and its primary references give historical evidence. The current search did not
  locate a resolution or a recent explicit confirmation of this precise target.
- **Gate noise:** quantified the advantage before the function and input length;
  all computational gates have independent common-rate output flips. Wires share
  a gate's noisy bit, and there is no noiseless output decoder. The boundary value
  is included. [Unger 2008](https://ir.cwi.nl/pub/13657) states the circuit
  conjecture. The [2023 revision on asymmetric noise](https://arxiv.org/abs/1809.09748v5)
  treats different gate-specific noise assumptions and does not establish a
  resolution of this target. No fresh comprehensive status certification is claimed.
- **Programmable matter:** uses the [SAND 2026 discrete model](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAND.2026.11),
  contracted endpoint configurations, and shapes modulo translation, lattice
  rotations, and reflection. Planning time is free. Arbitrarily distant labeled
  destinations and stronger continuous-mechanics collision conventions are not
  silently added. Section 7 explicitly asks for a polylogarithmic bound.
- **Sandpiles:** fixes the [2025 eventual-prediction problem](https://arxiv.org/abs/2506.21084v1),
  four neighbors, explicit stable input, one extra grain, and zero extension to
  the infinite lattice. The question is logspace-uniform NC membership. P-completeness
  would imply a negative answer only under NC != P. The [June 2026 preprint](https://arxiv.org/abs/2606.26943v1)
  still calls the standard planar question open and treats weighted/nonuniform
  variants separately.
- **d-DNNF:** [TCS-0306](../data/cards/TCS-0306.json) asks for polynomial-time
  construction; the proposal asks only for polynomial-size existence. The
  [maintained primary question list](https://a3nm.net/work/research/questions/#ptime-complementation-of-d-dnnf)
  explicitly distinguishes them. Efficient construction implies the size bound;
  the converse is not established. Both are individually significant targets,
  so the existing question is preserved and the new card records the implication.
  The user's [STACS 2026 link](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.5)
  is relevant despite its title: Section 7 discusses this complementation question.
  The [2024 negative result](https://www.ijcai.org/proceedings/2024/398) concerns
  structured d-DNNF, not the unrestricted class on the new card.

The other four canonical cards already contain the requested targets and source
material, so they were not duplicated or rewritten. New-card importance scores
are editorial judgments about fundamental scope, not claims of newly verified
openness or decisions to displace the existing Top 100 focus choices.
