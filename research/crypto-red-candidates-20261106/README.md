# Major cryptography candidates — 6 November 2026

The owner requested new red cards in crypto, preferring major problems outside
the pattern “construct primitive X from primitive Y”, and an assessment of the
existing red cards that fit that pattern. The current working source is
`/home/vasek/atlas-categories-20261105`, matching the live 1,148-card catalogue
before this addition. The older `/home/vasek/atlas` checkout does not contain
the current shared color selection.

## Added as red

| Card | Target | Why it merits inclusion |
| --- | --- | --- |
| [TCS-7526](https://vaclavrozhon.github.io/atlas/#TCS-7526) | Exponential share-size lower bounds for unrestricted perfect secret sharing | A basic information/storage lower bound for arbitrary access-control policies, including nonlinear schemes and unlimited reconstruction computation. |
| [TCS-7527](https://vaclavrozhon.github.io/atlas/#TCS-7527) | Two-server private information retrieval with polylogarithmic total communication | A central communication gap with exact privacy and correctness and no hardness assumption. |
| [TCS-7528](https://vaclavrozhon.github.io/atlas/#TCS-7528) | A fixed improvement below the balanced two-thirds exponent in random-function inversion | A longstanding generic-cryptanalysis barrier with unrestricted preprocessing, short advice and adaptive oracle queries. |

All three have self-contained mathematical models, a binary answer criterion,
primary references, dated progress, a five-sentence summary, and individual
editorial importance assessments. Their default category is Cryptography.
The alternate small categories are Coding and information theory,
Communication complexity and Boolean function analysis, and Data structures,
respectively. No existing card's color or mathematical statement was changed.

The inversion question deliberately selects a fixed-exponent barrier from the
larger tradeoff problem. It does not ask for the full optimal curve. It counts
stored advice and oracle queries, not all working memory or elapsed time.
Its half-of-functions/half-of-inputs success convention follows Definition 1.1
of [Chawin, Haitner and Mazor](https://arxiv.org/abs/2105.00761).

## Current-status and duplicate checks

Only active cards were searched. The archive was not reviewed or reactivated.

- **Secret sharing:** [Larsen–Simkin](https://eprint.iacr.org/2019/174) state
  Beimel's exponential conjecture; their bound restricts reconstruction
  complexity. [Beimel's monograph](https://eprint.iacr.org/2025/518) discusses
  the general gap. The 2026 [multilinear](https://eprint.iacr.org/2026/1769)
  and [multislice](https://eccc.weizmann.ac.il/report/2026/213/) results still
  restrict the schemes covered. The October reverse-substitution paper was
  screened through its author abstract on the ePrint mirror; it describes a
  route to stronger bounds, not an unrestricted exponential theorem. The new
  lower-bound card is distinct from TCS-0465's sub-half-exponent upper bound:
  both statements may hold simultaneously. The new card's year 2019 records
  its directly checked problem source, not the original date of the conjecture.
- **PIR:** [Dvir–Gopi, Definition 1.1](https://arxiv.org/abs/1407.6692) fixes
  the one-round perfect model. [Ghasemi–Kopparty](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.68)
  explicitly leave polylogarithmic two-server communication possible. The
  [Gupte–Ragavan revision of 16 October 2026](https://arxiv.org/abs/2607.22033)
  does not reach this target. TCS-7459 instead concerns computational
  single-server PIR with fast preprocessing; TCS-2732 concerns three-server
  distributed point functions; TCS-1020 concerns locally decodable codes.
  These were inspected and are not duplicate targets. The year 2014 records
  the directly checked model/problem source, not the origin of PIR.
- **Inversion:** [Corrigan-Gibbs–Kogan](https://people.eecs.berkeley.edu/~henrycg/pubs/function-inversion/)
  state the balanced gap; their [ECCC introduction](https://eccc.weizmann.ac.il/report/2018/182/download)
  attributes the optimality question to Yao (1990). The
  [2026 Kuszmaul–Kuszmaul result](https://arxiv.org/abs/2609.20240)
  matches the lower bound in a small-query, nearly-linear-advice regime and
  does not settle this balanced target. Quantum permutation inversion has
  different oracle and computational conventions.

These are bounded searches for the new targets, not the deferred
whole-catalogue solvedness audit. No claimed theorem was independently
proof-verified. Existing source statements were read for classification only;
their current open status was not recertified.

## Existing red crypto cards in the requested pattern

Colors and categories come from the live catalogue combined with the durable
service choices in `selection-before.json`, fetched on 6 November 2026. Several
cards that are red in the original proposal have since been turned green;
they are intentionally absent from the table below.

There were **17 red cards**, of which **8 are explicit construction questions
from a cryptographic primitive or a standard cryptographic assumption**:

| Card | Construction question |
| --- | --- |
| TCS-6546 | One-way permutations from one-way functions |
| TCS-6692 | Linear-seed pseudorandom generators from one-way functions |
| TCS-7274 | Constant-depth local one-way functions from arbitrary one-way functions |
| TCS-7278 | Identity-based encryption from public-key encryption |
| TCS-7451 | Witness encryption from Learning With Errors (LWE) |
| TCS-7452 | Dual pseudorandom functions from one-way functions |
| TCS-7453 | General functional encryption from LWE |
| TCS-7457 | Constant-round concurrent zero knowledge from LWE |

Here LWE means the computational task of distinguishing noisy linear equations
from uniform samples, used as a hardness assumption rather than literally as
an encryption primitive. These three LWE entries are included because they
unambiguously fit the owner's broader construction-from-a-foundation concern.

Four further cards fit that broader concern through hardness transfer or
security amplification:

| Card | Type |
| --- | --- |
| TCS-5793 | Pseudorandom functions from worst-case learning hardness |
| TCS-6871 | Fully homomorphic encryption from worst-case lattice hardness |
| TCS-6953 | One-way functions from errorless average-case NP hardness |
| TCS-3025 | Strong exponential one-wayness from weak exponential one-wayness |

Thus the broad count is **12 of 17**. The other five are TCS-0507, TCS-6673,
TCS-7391, TCS-2732 and TCS-4754: respectively privacy/regret bounds, continual
counting error, private optimization sample complexity, information-theoretic
distributed-point-function key length, and unconditional zero knowledge for
gap circuit complexity. They are not implication questions of this type.

This classification does not recommend deleting the 12 cards: several are
major foundational questions despite sharing a formulation pattern. It only
identifies where additional thematic variety is useful.

## Validation and publication

Recorded after checks and deployment in `validation.json`.
