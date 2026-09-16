# Privacy card review — 15 September 2026

Worker `third-privacy-862815` uses the shared active-only queue and per-card
reservation tokens. The tokens stay in an unversioned temporary file. Every
completion checks the reserved input hash under the publication lock, records
an individual ledger entry, and publishes local exports. No staging, commit,
push, deployment, or review of pre-existing archived card bodies was performed.

## Checkpoint 1: four historical privacy questions

- **TCS-0507 — completed, active.** Recovered pure privacy of the full action
  transcript, full-information feedback, independent bounded stochastic losses,
  expected pseudo-regret, and the unique optimum. Defined an explicit minimax
  gap-promise convention and retained all four parameters, including finite
  horizons. The published ALT 2026 Wu–Wang result removes the horizon from the
  gap-dependent upper bound but leaves a logarithmic factor in the number of
  actions. Its deterministic-loss resolution does not answer this stochastic
  target. The existing score 76 is preserved.
- **TCS-3312 — completed, archived as resolved.** Recovered the missing
  parenthetical requirement that the sample threshold remain polynomial in
  dimension and grid bit length. STOC 2025 Kaplan–Mansour–Moran–Stemmer–Tur,
  full-version Corollary 25, supplies the matching existence result in an
  arithmetic/sampling model. The source explicitly leaves finite-precision
  implementation to a suggested discretization; the review does not assert a
  proved bit-complexity result. The previously unassessed importance was
  individually assessed at 78 before archival.
- **TCS-0510 — completed, archived as resolved with interpretation recorded.**
  The 2022 candidate theorem displays have defective quantifiers and parameter
  ranges. The main finite-mistake question was recovered using the subsequent
  literature's hypothesis-stream output, expected mistakes, constant privacy
  parameter, and privacy slack inverse-quadratic in the horizon. NeurIPS 2024
  Li–Wang–Ye Theorem 4.3 then applies even to a fixed two-hypothesis finite-domain
  class with nonprivate mistake bound one. It refutes a horizon-independent
  private bound; it does not prove the source's proposed square-root rate.
  The March 2025 arXiv revision retains that theorem. Score 80 is preserved.
- **TCS-6825 — completed, archived as conditionally resolved.** The original
  textbook expressly asks what computational assumptions buy a trusted curator.
  FOCS 2023 Ghazi–Ilango–Kamath–Kumar–Manurangsi Theorem 5 gives efficient utility
  tests and a separation against even unbounded statistical curators, under
  Assumptions 18, 22 and 26. The three assumptions are preserved; their truth is
  not asserted. This is stronger than the 2016 efficiency separation. The
  archived record explicitly does **not** certify a new self-contained active
  Lean prompt from abbreviated security-game names. Its archival disposition
  and model flags record that limitation. Importance was individually assessed
  at 88 before archival.

All four retain historical source provenance. The bibliographic pagination and
current authorship of TCS-0507 were corrected in hash-checked amendment entries.
TCS-6825's historical-disposition metadata was likewise amended under lock after
its immediate archival so that the completion helper's default active-model
certification does not misdescribe the archived record.

## Checkpoint 2: private learning, marginal release, unrestricted regret

Completed on 15–16 September 2026, with immediate publication after each card:

- **TCS-0506 — completed, active.** Retained the previously selected universal
  polynomial bound in VC dimension and iterated-logarithm Littlestone dimension.
  Defined finite classes, arbitrary improper learners, fixed accuracy/confidence,
  replacement privacy with inverse-quadratic slack, and the complete positive
  and negative quantifiers. The finite-domain reduction uses at most
  `2^{|C|}` label vectors. Checked the new COLT 2026 open-problem paper,
  Lyu's dimension-polynomial bound (and official STOC 2026 publication), and
  Yan's special VC-dimension-one result. The latter does not establish a
  polynomial of universal degree across arbitrary VC dimension. Score 88 and
  the previous target selection are preserved.
- **TCS-7236 — completed, active.** Retained the approved noninteractive,
  arbitrary-synopsis target for all marginal orders with polynomial records
  and error tending to zero. Specified query encoding, normalized absolute
  error, simultaneous success, uniform bit computation and evaluator access.
  Corrected broken mathematical delimiters. Checked Vadhan's actual privacy
  manuscript, the older interactive per-query theorem, and the December 2025
  weighted-Fourier result. Runtime polynomial in the explicit exponential
  workload, optimal variance within factorization mechanisms, and conditional
  synthetic-data hardness do not resolve arbitrary efficient synopses.
  Score 94 and previous selection provenance are preserved.
- **TCS-5031 — completed, active.** Restored the square root omitted by the
  import. Defined the ordinary adversarial binary prediction game on arbitrary
  sets, the exact regret infimum/supremum, tree dimension, universal constants
  and `T >= d >= 1`. No countability, topology, measurability or computational
  restriction was added. The 2023 multiclass paper's p. 9 footnote 4 and Raman's
  2025 thesis p. 15 footnote 4 explicitly retain the minimax-regularity gap.
  The randomized-Littlestone theorem's proof invokes the same 2021 upper bound;
  it is not an independent resolution. The May 2026 oracle tradeoff retains
  logarithmic regret factors. The formerly provisional score was individually
  assessed at 83.

## Checkpoint 3: related-card correction and two further reviews

Completed on 16 September 2026, with immediate publication after each card.

### TCS-2336 — targeted re-review completed, active

The active card's previous finite-label context said that the source obtains
`O(sqrt(d T log |Y|))` and that this gives the sharp rate for a fixed label count.
Its second progress item repeated that assertion without a qualification.
The checked source, *Multiclass Online Learning and Uniform Convergence*, PDF
p. 9 footnote 4, explicitly assumes the extra minimax condition for the results
in that section. The appropriate correction is to say that this finite-label
upper bound and its fixed-label consequence require the cited regularity
condition; even unrestricted binary classes retain the question in TCS-5031.

The initial reservation attempt failed because TCS-2336 was absent from the
pending review queue. The parent authorized adding a targeted re-review under
the publication lock after checking that neither a queue entry nor a foreign
claim had appeared. That checked addition, the normal fresh reservation and
completion are recorded in the ledger. Both affected claims are now qualified.
The rest of the active card was checked against the source; mathematical
notation, arbitrary-label probability distributions, the reconstruction of the
finite-sequence game and the Lean criterion were made explicit. The previously
authorized two-parameter quantitative target, score 88 and provenance remain.

### TCS-4672 — completed, archived as resolved

The original Open Question 20 explicitly defines the price as bandit Littlestone
dimension divided by ordinary Littlestone dimension. This is deterministic
realizable learning with worst-case, horizon-independent mistake bounds.
Long's upper bound together with Geneson's corrected lower-bound proof gives
the matching order `Theta(k log k)` for the worst ratio at `k` labels. The
NeurIPS 2024 Filmus–Hanneke–Mehalel–Moran paper, §1.1.1 equations (1)–(2),
explicitly states both bounds for every `k >= 2`. Its randomized `Theta(k)`
result is separately identified and does not replace the original target.
Both tree definitions, the excluded zero denominator, arbitrary deterministic
rules and asymptotic precision were recovered. Importance was individually
assessed at 82 before immediate archival. No exact finite-`k` formula or
independent Lean formalization is claimed.

### TCS-4792 — completed, active

The imported sentence omitted the universal binary-compression premise.
Restored the conditional transfer for arbitrary `f`, with a multiplicative
constant uniform over dimensions, classes, labels and sample sizes. Kept all
label sets in the stated question, exact realizable consistency, arbitrary
improper reconstruction, and the source's literal sequence/set-inclusion
convention. Both retained records and auxiliary bits count toward size;
original positions and sample length are not free decoder input. Proper,
majority-vote and stable binary schemes remain extra premises in partial
results. The 7 April 2025 revision retains the question as Open Problem 3.3.
Pabbaraju's impossibility concerns finite DS dimension, which does not refute
the target using finite graph dimension. Importance was individually assessed
at 85; the class and provenance were preserved.

## Checkpoint 4: computable learning and the general compression conjecture

- **TCS-5061 — completed, archived as resolved.** The source's unqualified
  CPAC and SCPAC mean proper agnostic learning. Its explicit Question 1 asks
  for a separation. COLT 2023 Delle Rose–Kozachinskiy–Rojas–Steifer Theorem 14
  gives precisely that separation, with finitely supported hypotheses, a
  decidable finite-support representation and VC dimension at most three.
  The active extraction's sentence without the word “proper” obscured this:
  the same paper proves equivalence for improper learning. Defined total
  Turing learners and output indices, risk infima, arbitrary distributions,
  the two sample-threshold quantifiers, and failure of every proper learner
  to have any computable bound. The result concerns sample complexity,
  not merely computation time or polynomial growth. Importance was
  individually assessed at 80 before archival.
- **TCS-6541 — completed, active.** Preserved the already selected strong card's
  exact target, score 97, unordered labeled kernels, counted side bits and
  arbitrary improper reconstruction. Rechecked primary size conventions and
  the 2016 exponential theorem, the 2024 embedding obstruction, and the April
  2026 graph-ball results. Repaired math boundaries, made quantifiers and
  the full Lean negation explicit, and clarified that variable-length side
  strings must encode their lengths. The 3 August 2026 version of the claimed
  breakthrough remains withdrawn with an incorrect Lemma 2 proof noted by
  the authors; stale search summaries are not used as a resolution.

## Checkpoint 5: conditional information and robust learnability

- **TCS-5153 — completed, archived as resolved.** Matched the original 2019
  existence-of-a-characterization question to Montasser–Hanneke–Srebro,
  NeurIPS 2022, Theorems 5–6 and 9. Defined robust loss, independent original
  training examples, improper unrestricted predictors, global knowledge of
  the perturbation rule, and the finite-subgraph orientation dimension.
  The realizable and agnostic learnability equivalences answer the original
  question; later conjectures about simpler dimensions are different targets.
  The 2019 footnote explicitly suppresses empirical-process measurability
  restrictions. Preserved that limitation and amended the newly archived
  metadata under a checked hash to `historical_disposition`,
  `model_self_contained=false`, and `requires_context=true`. Importance was
  individually assessed at 87. No unrestricted nonmeasurable theorem or
  completed Lean proof is claimed.
- **TCS-5847 — completed, active with uncertain status.** Recovered the source's
  main proper agnostic Conjecture 6: one universal constant, information at
  most `c d` for every labeled distribution, and expected empirical excess
  at most `c sqrt(d/n)` for every deterministic sample. Defined the complete
  output, supersample and selector, conditional entropy in bits, proper
  probability kernels, and an explicit measurable-interface convention.
  No finite/countable-domain restriction or existence-of-measurable-ERM
  premise was introduced. The 2020 negative result refutes the different
  realizable Conjectures 7–8 with `O(d/n)` or zero empirical error; chained
  generalization and projected-output bounds also do not match this target.
  A fresh exact-title search found Hanneke–Juexiao Wang's *The optimal
  information complexity of VC learning* on the official FOCS 2026 accepted
  list and the author's publication page. Neither supplies theorem text or
  a manuscript link, and bounded repository searches did not locate one.
  This concrete status-check gap is recorded prominently; the card does not
  assert current openness or infer a resolution from the title. Importance
  was individually assessed at 85.

Both cards were completed through the matching claim and input hash and
published immediately. The unsupported draft question-type value for 5153
was caught by schema validation before any write, then corrected to the
supported yes/no equivalence form. The checkpoint's active formula check
passed on 1,039 cards and 21,473 expressions.

## Checkpoint 6: computational learning and cryptographic implications

- **TCS-3177 — completed, active with uncertain status.** Preserved the
  NP/poly-to-PH/poly learning implication. Defined size-bounded circuits with
  each fixed alternating witness depth, a public target-size bound, one uniform
  learner per fixed level, ordinary Boolean output circuits, arbitrary example
  distributions, independent realizable labels and polynomial dependence on
  size and inverse accuracy/confidence. The target is not one algorithm with
  a common polynomial over unbounded alternation depth. Distinguished this
  learning question from small-circuit representation consequences,
  stronger-class equivalences and the source's separate relativization question.
  The full December 2021 manuscript retains the question. The 2025 journal
  metadata and abstract were checked; subscription full text was unavailable.
  Importance was individually assessed at 87.
- **TCS-5090 — completed, active with uncertain status.** Preserved the
  implication from unrestricted worst-case random-example circuit-learning
  failure to ordinary uniform strong one-way functions. Defined the full
  learning interface and polynomial costs, any valid inverse, negligible
  inversion probability and all-sufficiently-large security-length quantifiers.
  The source's conventional target-size dependence is explicit, and no
  efficiently samplable hard-target distribution or SAT reduction is added.
  Checked FOCS 2023 Hirahara–Nanashima's average-case and exponential-in-depth
  worst-case guarantees; ITCS 2025 Liu–Mazor–Pass Theorem 6's computational-
  shallowness promise and infinitely-often learning convention; and STOC 2026
  Hirahara–Nanashima Theorem 1.5's average-case GapLearn approximation task
  and infinitely-often one-way conclusion. None is substituted for the
  original unrestricted implication. Importance was individually assessed at 91.

Both records retain their separate source targets and provenance despite
sharing the same original paper. Each was reserved and hash-checked separately,
completed through the helper and immediately published. The current-status
qualifications reflect the bounded literature checks rather than a proof of
continued openness. A final citation pass corrected the ITCS 2025 page span
in TCS-5090 and split TCS-5847's 2021/2025 context paragraph so each theorem
cites its own primary source. These small follow-ups used fresh reservations,
checked queue re-entry and completion ledger records, then were republished.

## Checkpoint 7: agnostic circuit learning and uniform automata

- **TCS-5434 — completed, active with uncertain status.** Defined every fixed
  ACC⁰ depth, modulus and polynomial size exponent, arbitrary uniform-marginal
  stochastic labels, fresh conditional membership-query responses and an
  unrestricted finite evaluable predictor. Preserved the source's correlation
  slack `2^(-n^0.99)` and saving `sigma(n)=omega(log n)`, including query, output
  and bit costs. The source's full-learning display uses success `1-delta` and
  sets `delta=2/3`; preserved its literal success `1/3`, expressly distinguishing
  the weak-learner display's `2/3`. No typographical correction was assumed.
  Checked the prime-modulus multiplicative-error partial theorem and version
  history. Importance was individually assessed at 91.
- **TCS-5902 — completed, active with uncertain unconditional status.** Recovered
  the ordinary DFA question in the source's related-work paragraph, with
  fixed-length uniform words, every finite alphabet, state-count bounds,
  independent acceptance labels and one uniform polynomial-time improper
  predictor. The source's own infinite-word weighted-automaton results address
  another model. Checked Daniely–Vardi COLT 2021 Theorem 12 and Assumption 1:
  even inverse-polynomial-advantage weak improper learning on uniform binary
  words is impossible under a local-PRG assumption. ALT 2026 Table 1 explicitly
  retains that premise. The historical 2019 open-status summary is updated;
  the conditional theorem is not silently turned into an unconditional archive.
  Random-transition/state-information and active-query positive results are
  distinguished. Importance was individually assessed at 89.

Both cards had separate reservations and matching input hashes, helper
completion and immediate publication. Formula validation passed on 1,036 active
cards and 22,467 expressions. No Lean proof or independent verification of the
cited research proofs is claimed. The next reserved pair is TCS-6542 and TCS-6543.

## Checkpoint 8: noisy parity and junta learning

- **TCS-6542 — completed, active with uncertain status; score 96 preserved.**
  Retained exact recovery for every secret, separately for every fixed rational
  noise rate below one half. Repaired the polynomial-subscript notation and
  specified one uniform machine per fixed rate, unary dimensions, worst-case
  bit/sample/output costs and the full negation. Checked the distinction between
  BKW's subexponential sample count and Lyubashevsky's polynomial-sample theorem,
  the memory lower bound's noise-bias convention, and the 2026 amplification and
  conditional code/dual-code reductions. Split their citations correctly.
  A new 15 September 2026 optical-computing paper's publisher abstract describes
  a finite 512-variable experiment with at most two variables per constraint;
  this is not the requested uniform classical theorem. Full PDF retrieval hit
  the publisher gateway, and that limit is explicit.
- **TCS-6543 — completed, active with uncertain status; score 95 preserved.**
  Retained the previously approved full `poly(n,2^k,1/epsilon)` target and
  consolidation provenance. Repaired damaged projection/logarithmic-support
  formulas, included constant juntas, and defined one machine/universal
  exponent, independent noiseless samples and improper circuit output. Checked
  MOS, Valiant, the 2025 survey, distribution-learning and the May 2026
  random-walk theorem. Recovered the previously unverified OpenReview identity:
  Chandrasekaran–Klivans, *Learning Juntas under Markov Random Fields*, NeurIPS
  2025. The official full paper's Definition 1.2/Theorem 1.3 assumes positive
  external-field smoothing and its stated graph/width conditions; uniform
  input is an unperturbed special point and is not covered by probability over
  smoothing. The source bibliography now names the actual paper. Wigderson's
  weaker growing-support milestone remains distinct from the approved target.

Both cards were completed through their claims and input hashes and immediately
published. The next reserved pair is TCS-7294 and TCS-4592.

## Checkpoint 9: decision trees and Gaussian agnostic halfspaces

- **TCS-7294 — completed, active with uncertain status; score 91 preserved.**
  Retained hidden arbitrary trees, all-node size, passive independent uniform
  noiseless examples and improper circuit output. Defined a single learner and
  universal polynomial, reciprocal-integer accuracy and charged all bit costs.
  Checked Kalai–Teng's positive-probability smoothing, ITCS 2025's explicitly
  represented-tree backdoor defense, and the 2026 product-space paper's chosen-
  input label queries and depth-dependent output size. None replaces the
  requested fully polynomial passive learner. Consolidated-source provenance
  was preserved.
- **TCS-4592 — completed, active with uncertain status; provisional importance
  assessed at 88.** Retained the broad optimal joint running-time question,
  not just its historical `n^{O(log(1/epsilon))}` subquestion. Affine halfspaces
  follow the source introduction; deterministic Boolean target labels follow
  Definition 4. L1 loss is exactly twice disagreement. The explicit arithmetic
  convention charges Gaussian-coordinate loading, rational-code real operations,
  comparisons, output coefficients and evaluation, and supplies no general-real
  decision oracle. Attainable rate functions require one uniform learner and
  universal multiplicative constant; no pointwise hard-coding or existence of
  a fastest learner is assumed. The answer criterion requests matching rates
  with their full parameter regimes.

For 4592, source and later theorem limitations are prominent. COLT 2021 proves
SQ optimality in a general joint-label model. ICML 2023 Corollary 3.2 uses
subexponential LWE hardness, exponent
`(1/(epsilon*sqrt(log n)))^alpha` for fixed `alpha<2`, and the specified bounded
error range. Its hard labels retain residual randomness conditional on x;
this review did not prove a reduction to deterministic labels or an exact-real
arithmetic lower bound from a finite-bit cryptographic assumption. These gaps
are not hidden by a claim that the source is resolved. May 2026 Theorem 3.14
has a valid logical inclusion from all joint labels to fixed deterministic
targets and proper output to allowed improper output, but its accuracy-only
runtime term remains visible. The April homogeneous proper-hardness model is
also kept separate. No finite-bit equivalence or exact optimum is claimed.

Both completions used separate tokens and checked input hashes followed by
immediate publication. The next reserved pair is TCS-5088 and TCS-5119.

## Checkpoint 10: halfspace intersections and Gaussian graphs

- **TCS-5088 — completed, active with uncertain status; importance assessed
  at 92.** Recovered the selected paragraph's Gaussian and uniform-cube
  antecedents and corrected the misleading factorizable-distribution title.
  Retained both questions and required separate answers. Defined variable
  intersection size, affine thresholds, passive noiseless examples, improper
  outputs and universal polynomial resource bounds. The Gaussian arithmetic
  and discrete bit conventions remain distinct. Checked Alman–Patel–Servedio
  v2 (30 July 2026), the STOC bounded-geometric-width sparsification application
  and May proper agnostic learning; none of the displayed dependencies gives
  the requested fully polynomial guarantee.
- **TCS-5119 — completed, active with uncertain status; importance assessed
  at 90.** Distinguished the source's motivating abstract, its bounded-degree
  theorem and the final general computational question. Corrected the previous
  summary's unqualified claim of sample optimality: source p4 explicitly keeps
  a gap when degree and minimum edge strength vary together. Defined the
  information-theoretic minimum directly over all measurable estimators,
  keeping unknown means, arbitrary conditioning, variable confidence and a
  universal sample factor. The benchmark is not supplied as an oracle.
  Checked NeurIPS 2020 attractive/walk-summable subclasses, COLT 2024
  Conjecture 33/Theorem 41/Remark 43 and the 2026 Glauber-trajectory result.
  The conditional low-degree/spiked-Wishart separation remains conditional,
  and the trajectory theorem does not replace independent observations.

Both completions used claims and matching input hashes and immediate publish.
Math validation passed for 1,035 cards and 23,821 expressions; output hashes and
claim releases were checked. No finite-bit equivalence, unconditional hardness
or full minimax statistical formula is claimed. The next reserved pair is
TCS-3391 and TCS-5087.

## Checkpoint 11: Gaussian mixtures and robust spectral reconstruction

- **TCS-3391 — completed, active with uncertain status; importance assessed
  at 92.** Preserved the full unknown-weight and unequal-spherical-scale
  formulation of Theorem 9 and the selected end-to-end initialization question.
  Defined scaled mean error, relative weight error, relative standard-deviation
  error epsilon/sqrt(d), one matching permutation, public reciprocal-weight and
  scale-ratio bounds, and a universal separation constant. The resource goal
  remains polynomial samples and time, not the stronger sample-optimal time.
  Checked 2022 positive-c separation and low-dimensional Fourier results, the
  2026 Fourier family that explicitly excludes Gaussians, and COLT 2026's
  nonpolynomial inverse-weight factors.
- **TCS-5087 — completed, active with uncertain status; importance assessed
  at 86.** Recovered the selected spectral training-time guarantee from
  Proposition 27 and (71). The same projector must satisfy every eta, rank at
  most r, bounded induced q-to-2 norm, and the clean spectral-error tradeoff
  with its sqrt(m)*delta*kappa term. The output cannot merely certify poisoning.
  Preserved every fixed real q >= 2 and infinity using the parent-approved
  explicit exact-real model with fixed-q power primitives. The source's
  Frobenius, increased-rank, certification and Gaussian-covariance results do
  not silently replace this worst-case question. A separately claimed and
  hash-checked typography pass corrected source/prose spacing.

Both cards used helper completion and prompt publication. Math validation passed
for 1,035 active cards and 24,189 expressions; the later typography-only pass
changed no formulas. Output hashes and released claims were checked. This
finishes the then-available Learning theory queue. The next reserved pair is
TCS-6657 and TCS-6684, tensor PCA and fixed-community recovery thresholds.

## Sources and verification

[privacy-sources.json](privacy-sources.json) records checked primary PDFs and
SHA-256 hashes. The PDF/text cache is local and ignored by Git. Textbook §9.3
was read from the existing local Dwork–Roth author PDF/text and checked against
its live author page. Cards and ledger record precise theorem/definition locators
and publication metadata. Bounded later-work checks do not independently verify
all cited proofs.

Validation results are recorded in [privacy-verification.json](privacy-verification.json).
