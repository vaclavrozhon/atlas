# Proposal: 300 additional card removals

**Application update:** [Six example cards were removed or consolidated after user approval](applied-examples.md). The review below records the original proposal; 294 recommendations remain unapplied by this change.

Prepared 12 September 2026. **Proposal only. No canonical card or selection registry was edited, and nothing was deleted or published.**

Open the [searchable review table](proposal.html), the [spreadsheet-ready list](proposal.tsv), or the [structured decisions](decisions.json). All 300 individual reasons also appear below.

The proposal contains **84 stronger recommendations** and **216 judgment-sensitive recommendations**. It is an editorial selection for a smaller, more consequential TCS research benchmark, not a finding that all these questions lack scientific value. There are **18 proposed consolidations** and **282 other removals**. Two consolidations need an explicit scope check before removal: formula/circuit conventions in TCS-0308 and randomness conventions in TCS-6319.

The initial snapshot contained **1,582 records**. At rendering, the catalogue contains **1,588 records**: 1,567 not marked resolved and 21 marked resolved. None of the latter are used to fill this batch. Accepting all 300 proposals would leave **1,288 stored records**, including **1,267 not marked resolved**. These are catalogue status counts, not independent certifications of openness.

## Criteria and scope

The selection follows [Atlas rules](../../docs/RULES.md), [the project purpose](../../README.md), and the earlier [importance calibration](../importance-pruning-20260911/CALIBRATION.md), [fundamentality review](../fundamentality-second-300-20260911/README.md), and [specification cleanup](../specification-cleanup-20260912/README.md).

I screened all 1,582 cards by title and statement, expanding saved excerpts and opening summary sentences where needed. I read complete saved working summaries, substantive significance fields and source titles/locators for 688 cards, including every proposed removal and the comparison cards used for consolidation. These were individual editorial decisions, not an automatic score, category-quota or keyword filter. The read ledger records the content hash and displayed fields; it does not claim that every external paper was read.

Of the 6 records added after the initial snapshot, 6 also received a detailed read matching their rendering-time content. Those additional reads are recorded separately from the initial screening.

The main considerations were narrower model variants, additional parameter regimes, particular constructions, and intermediate methods whose independent contribution to this smaller benchmark is less compelling. Logical dependence alone, difficult formalization, incomplete prose, age, source prestige, a high score and a previous formulation repair were not decision rules. No category-balancing target was used. The ordering is confidence followed by stable ID, not a scientific ranking of the 300 problems.

This pass is **not a fresh literature audit of open status**. Old bounds, claimed source resolutions and model ambiguities remain subject to the catalogue's separate status/formulation review. Reasons referring to a theorem or algorithm describe the saved source context. The current-card hashes in the decisions make later changes detectable. At rendering, 35 baseline records had changed during this review; every selected card has a detailed read matching its current hash.

## Calibration and reconsidered cases

- [TCS-0464](../../data/cards/TCS-0464.json) stays: the two-bit OR information problem is a small canonical question, and the earlier user discussion did not establish an exclusion reason.
- [TCS-7196](../../data/cards/TCS-7196.json) stays: polynomial-time exact EFX for three agents is a meaningful canonical computational frontier, despite its fixed population.
- [TCS-3689](../../data/cards/TCS-3689.json) stays: the clarified non-clashing teaching conjecture is a general sharp relation for all finite concept classes. Its breadth outweighs the argument that it is just another teaching convention.
- [TCS-4110](../../data/cards/TCS-4110.json) stays in this batch: the general real-stability recognition barrier deserves more careful significance review before treating it as merely an algorithmic follow-up.
- [TCS-3685](../../data/cards/TCS-3685.json) is held for separate formulation/status review. The concurrent review identified a literal-statement inconsistency; it is not used to meet this 300-card importance cut.
- [TCS-0306](../../data/cards/TCS-0306.json) and [TCS-7260](../../data/cards/TCS-7260.json) both stay: polynomial-time negation and nonconstructive polynomial-size negation are different targets.
- [TCS-2783](../../data/cards/TCS-2783.json) and [TCS-6500](../../data/cards/TCS-6500.json) both stay: their saved girth and graph-size quantifiers differ. Only the redundant source occurrence TCS-5770 is proposed for consolidation.
- [TCS-7008](../../data/cards/TCS-7008.json) and [TCS-7298](../../data/cards/TCS-7298.json) both stay: relative-error approximation and a constant-factor guarantee with variable rank should not be called duplicates.

## Consolidations

These removals are conditional on preserving useful references and the stated target in the retained record. The proposal performs no transfer. Consolidation must not silently broaden a target or count a narrower result as solving a broader one. The four `cluster_overlap` entries elsewhere are lower-priority related questions, **not claims of mathematical equivalence**.

| Remove after consolidation | Retain | Review requirement |
| --- | --- | --- |
| [TCS-2356](../../data/cards/TCS-2356.json) | [TCS-0331](../../data/cards/TCS-0331.json) | The invariant minimizes dual-graph treewidth over all triangulations, the same general complexity target already covered by TCS-0331. Preserve the JSJ-decomposition reference there. |
| [TCS-3324](../../data/cards/TCS-3324.json) | [TCS-7230](../../data/cards/TCS-7230.json) | Decidability of the real exponential field is stated explicitly in TCS-7230. Preserve the weighted-automaton application reference there and remove the redundant occurrence. |
| [TCS-3484](../../data/cards/TCS-3484.json) | [TCS-0163](../../data/cards/TCS-0163.json) | This repeats the NP-membership frontier of ordinary word-equation satisfiability represented by TCS-0163. Consolidation must retain the plain-equation convention and must not add regular constraints or inversion. |
| [TCS-4577](../../data/cards/TCS-4577.json) | [TCS-5773](../../data/cards/TCS-5773.json) | This is another occurrence of the unrestricted Skolem decision problem already specified in TCS-5773. Preserve the nonterminating-process information-leakage reference there. |
| [TCS-4972](../../data/cards/TCS-4972.json) | [TCS-7294](../../data/cards/TCS-7294.json) | Learning polynomial-size decision trees from uniform random labeled examples is already stated explicitly in TCS-7294. Preserve the backdoor-defense reference and the distinction from membership-query learning there. |
| [TCS-5034](../../data/cards/TCS-5034.json) | [TCS-7215](../../data/cards/TCS-7215.json) | This is the same computability question for graph Shannon capacity stated precisely in TCS-7215. Transfer the additional reference to that card and remove the redundant occurrence. |
| [TCS-5246](applied-examples.md#tcs-5246) | [TCS-7222](../../data/cards/TCS-7222.json) | The selected passage asks ordinary graph isomorphism in polynomial time, already represented by TCS-7222. Preserve its refinement-hierarchy reference in that card. |
| [TCS-5312](applied-examples.md#tcs-5312) | [TCS-4786](../../data/cards/TCS-4786.json) | The NP-hardness question for ordinary truth-table MCSP is already part of TCS-4786. Preserve this paper's total-versus-partial circuit-extension context in the retained card. |
| [TCS-5314](../../data/cards/TCS-5314.json) | [TCS-0163](../../data/cards/TCS-0163.json) | This is another statement of ordinary word-equation satisfiability in NP. Preserve the explicit NP frontier and this source under the general complexity card TCS-0163. |
| [TCS-5453](../../data/cards/TCS-5453.json) | [TCS-2680](../../data/cards/TCS-2680.json) | This source pointer and TCS-2680 refer to the same paper and page containing the heuristic-average-case implication for UP. Retain the explicit conjecture in TCS-2680 and combine the references. |
| [TCS-5501](applied-examples.md#tcs-5501) | [TCS-4786](../../data/cards/TCS-4786.json) | This repeats the NP-hardness frontier for ordinary MCSP represented by TCS-4786. Transfer the sums-of-squares reference without confusing restricted-method lower bounds with NP-hardness. |
| [TCS-5737](../../data/cards/TCS-5737.json) | [TCS-0913](../../data/cards/TCS-0913.json) | Weak convertibility for closed S-only combinator terms is the word problem already covered by TCS-0913. Preserve the normalization and infinite-tree-semantics context from this source. |
| [TCS-5770](../../data/cards/TCS-5770.json) | [TCS-2783](../../data/cards/TCS-2783.json) | This is the introductory girth-conjecture occurrence from the same routing paper used by the precise TCS-2783. Consolidate there; do not collapse TCS-2783 with TCS-6500 without checking their different girth and graph-size quantifiers. |
| [TCS-5845](../../data/cards/TCS-5845.json) | [TCS-0771](../../data/cards/TCS-0771.json) | The saved target is exact treewidth on planar graphs, also represented by TCS-0771. Consolidate this occurrence and preserve its potential-maximal-clique reference there. |
| [TCS-5926](../../data/cards/TCS-5926.json) | [TCS-0771](../../data/cards/TCS-0771.json) | The saved target is exact treewidth on planar graphs, also represented by TCS-0771. Preserve this paper's cubic-graph hardness context in the retained card rather than keeping another occurrence of the planar question. |
| [TCS-7135](../../data/cards/TCS-7135.json) | [TCS-0306](../../data/cards/TCS-0306.json) | Polynomial-time negation of deterministic DNNF is already represented by TCS-0306. Transfer the survey reference and its smooth-variant note; retain the separate nonconstructive polynomial-size question TCS-7260. |
| [TCS-0308](../../data/cards/TCS-0308.json) | [TCS-6712](../../data/cards/TCS-6712.json) | The general polynomial formula-versus-circuit gap is represented by nonuniform NC1 versus P/poly in TCS-6712 under the standard bounded-fan-in Boolean convention. Preserve the formula viewpoint and align the basis and size conventions when consolidating. |
| [TCS-6319](../../data/cards/TCS-6319.json) | [TCS-5158](../../data/cards/TCS-5158.json) | The saved target repeats constant-competitive irrevocable online matching on the line in TCS-5158. Transfer the reference and align the deterministic/randomized convention before any deletion. |

## Reasons across the proposal

Counts describe the result; they were not quotas.

| Reason | Cards |
| --- | ---: |
| Additional model or representation | 126 |
| Quantitative refinement | 59 |
| Specific method or reduction | 53 |
| Specific construction or family | 19 |
| Consolidate with retained card | 18 |
| Specialized target | 15 |
| Unselected bundle of directions | 6 |
| Lower marginal value within a cluster | 4 |

## Individual recommendations

### 1. TCS-0126 — Parity language

[TCS-0126](../../data/cards/TCS-0126.json) · Computational complexity · **high confidence** · Specific method or reduction

The parity-subset compatibility property under thinning is a technical combinatorial ingredient for shallow-circuit arguments. Keep the underlying circuit and regular-language lower-bound questions.

Saved sources: Automata Exchange.

### 2. TCS-0194 — Maximum entropy versus the Copy lemma

[TCS-0194](applied-examples.md#tcs-0194) · Coding and information theory · **high confidence** · Specific method or reduction

Comparing the maximum-entropy method with the Copy lemma concerns the relative power of two proof frameworks. The entropy-cone and information-inequality validity targets themselves provide broader coverage.

Saved sources: Algorithmic Aspects of Information Theory.

### 3. TCS-0423 — Efficient algorithms for multiparameter persistence

[TCS-0423](applied-examples.md#tcs-0423) · Computational geometry and metric spaces · **high confidence** · Specific method or reduction

The concrete target is preventing sparse-matrix fill-in during a particular persistence basis-change procedure. The broad title overstates its scope; general multiparameter-persistence complexity is a stronger representative.

Saved sources: Applied and Combinatorial Topology.

### 4. TCS-0866 — Learning Quantum Circuits with Queries

[TCS-0866](../../data/cards/TCS-0866.json) · Quantum computation · **high confidence** · Additional model or representation

Quantum-circuit learning through value-injection queries uses a specialized intervention interface motivated by a classical test-path method. General quantum learnability and information-access barriers take priority.

Saved sources: COLT / PMLR.

### 5. TCS-0959 — RNA Folding

[TCS-0959](../../data/cards/TCS-0959.json) · Distributed, parallel and sublinear algorithms · **high confidence** · Additional model or representation

Approximating simplified RNA folding with polylogarithmic streaming memory combines one application model with a severe access restriction. Core sequence-comparison and general streaming barriers take priority.

Saved sources: Sublinear.info.

### 6. TCS-1039 — Explicit superlinear in-place XOR lower bounds

[TCS-1039](../../data/cards/TCS-1039.json) · Computational complexity · **high confidence** · Additional model or representation

Superlinear lower bounds for in-place XOR updates add a fixed-register restriction to explicit linear-circuit complexity. The unrestricted explicit linear-map lower bounds are broader representatives.

Saved sources: Complexity of Linear Boolean Operators.

### 7. TCS-1144 — Superlinear spiky rank for Inner Product or Disjointness

[TCS-1144](../../data/cards/TCS-1144.json) · Computational complexity · **high confidence** · Specific method or reduction

Superlinear spiky rank for Inner Product or Disjointness tests one newly introduced lower-bound measure. Prefer the main rigidity, circuit and communication barriers to an additional measure-specific witness target.

Saved sources: Spiky Rank and Its Applications to Rigidity and Circuits.

### 8. TCS-1157 — Relative smartness of distribution-free ERM

[TCS-1157](../../data/cards/TCS-1157.json) · Learning theory · **high confidence** · Specific method or reduction

Whether ERM achieves the source's relative-smartness benchmark is a follow-up about a preferred learner after another learner establishes feasibility. The general learnability and instance-optimality targets take priority.

Saved sources: Relatively Smart: A New Approach for Instance-Optimal Learning.

### 9. TCS-1234 — Pass–space tradeoffs for exact streaming histograms

[TCS-1234](../../data/cards/TCS-1234.json) · Distributed, parallel and sublinear algorithms · **high confidence** · Quantitative refinement

The remaining exact-histogram pass-space tradeoff distinguishes closely spaced iterated-logarithm bounds. Prefer larger qualitative streaming memory and pass barriers.

Saved sources: Tight Bounds for Low-Error Frequency Moment Estimation and the Power of Multiple Passes.

### 10. TCS-1424 — Simulating formulas by bounded-width algebraic branching programs

[TCS-1424](../../data/cards/TCS-1424.json) · Algebraic computation · **high confidence** · Additional model or representation

Bounded-width formula simulation over two min-plus semirings adds a specialized representation comparison alongside the broader circuit, formula and branching-program separations.

Saved sources: VP, VNP and Algebraic Branching Programs over Min-Plus Semirings.

### 11. TCS-1444 — Improving the MRRW bound

[TCS-1444](../../data/cards/TCS-1444.json) · Coding and information theory · **high confidence** · Specific method or reduction

The saved target specifically asks for choices in a higher-order Delsarte framework that improve MRRW. Retain the general rate-distance bound questions; this proposal makes no new claim about their current best bounds.

Saved sources: Higher-Order Delsarte Dual LPs: Lifting, Constructions and Completeness.

### 12. TCS-1670 — Strictness of the plane-walking alternation hierarchy

[TCS-1670](../../data/cards/TCS-1670.json) · Automata and formal languages · **high confidence** · Additional model or representation

Strictness at every alternation level concerns plane-walking automata on two-dimensional subshifts, a specialized computation model. The saved motivation establishes an internal hierarchy rather than wider computational consequences.

Saved sources: Subshifts Defined by Nondeterministic and Alternating Plane-Walking Automata.

### 13. TCS-1784 — Deterministic local broadcast beyond the Δ log n lower bound

[TCS-1784](../../data/cards/TCS-1784.json) · Distributed, parallel and sublinear algorithms · **high confidence** · Additional model or representation

Improving the Delta log n lower bound for deterministic beeping local broadcast is a model-specific collision-resolution gap. Broader broadcast and distributed communication barriers take priority.

Saved sources: Beeping Deterministic CONGEST Algorithms in Graphs.

### 14. TCS-1823 — Shallow decision trees for finding influential coordinates

[TCS-1823](../../data/cards/TCS-1823.json) · Communication complexity and Boolean function analysis · **high confidence** · Specific method or reduction

A shallow tree that locates influential coordinates under restrictions is a particular proposed route to the Aaronson–Ambainis conjecture. Retain that conjecture before a separate card for this search subproblem.

Saved sources: Random Restrictions of Bounded Low Degree Polynomials Are Juntas.

### 15. TCS-2010 — Exponential permanent lower bounds from the τ-conjecture

[TCS-2010](../../data/cards/TCS-2010.json) · Algebraic computation · **high confidence** · Specific method or reduction

An exponential permanent lower bound conditional on a particular tau conjecture is a quantitative consequence of one conjectural route; retain the tau conjecture and the permanent lower-bound targets themselves.

Saved sources: Exponential Lower Bounds via Exponential Sums.

### 16. TCS-2356 — Complexity of three-manifold treewidth

[TCS-2356](../../data/cards/TCS-2356.json) · Computational geometry and metric spaces · **high confidence** · Consolidate with retained card

The invariant minimizes dual-graph treewidth over all triangulations, the same general complexity target already covered by TCS-0331. Preserve the JSJ-decomposition reference there.

Retain: [TCS-0331](../../data/cards/TCS-0331.json). Transfer and check scope before removal.

Saved sources: On the Width of Complicated JSJ Decompositions.

### 17. TCS-2371 — Growing Ramanujan graphs with bounded edge updates

[TCS-2371](../../data/cards/TCS-2371.json) · Structural graph theory · **high confidence** · Specific construction or family

Growing exact Ramanujan graphs with only constantly many edge changes adds bounded rewiring to an already demanding spectral target. The source achieves every positive slack; general explicit Ramanujan construction takes priority.

Saved sources: Spectral Expanding Expanders; Quantitative Results on Super-Ramanujan Graphs.

### 18. TCS-2644 — Deterministic NP-oracle range avoidance at near-linear stretch

[TCS-2644](../../data/cards/TCS-2644.json) · Pseudorandomness and derandomization · **high confidence** · Additional model or representation

Deterministic NP-oracle avoidance at locality three and near-linear stretch adds several resource restrictions to the range-avoidance cluster. Prefer its general computational and explicit-construction barriers.

Saved sources: Range Avoidance for Low-Depth Circuits and Connections to Pseudorandomness.

### 19. TCS-2824 — Truth-table reconstruction of intuitionistic connectives

[TCS-2824](../../data/cards/TCS-2824.json) · Semantics, logic and verification · **high confidence** · Specific method or reduction

The syntactic sufficient condition for reconstructing intuitionistic connectives concerns one truth-table-to-proof-rule procedure. More general constructive semantics and proof-system barriers take priority.

Saved sources: Classical Natural Deduction from Truth Tables.

### 20. TCS-3007 — Maximal rational rigidity despite a quadratic-field diagonal correction

[TCS-3007](../../data/cards/TCS-3007.json) · Algebraic computation · **high confidence** · Specific construction or family

The quadratic rational rigidity target is restricted to matrices admitting a particular quadratic-field diagonal correction. Its extreme field separation is interesting, but the construction-specific target is lower priority than general explicit rigidity.

Saved sources: Matrix Rigidity Depends on the Target Field.

### 21. TCS-3095 — Complexity of unordered width-three CNF games

[TCS-3095](../../data/cards/TCS-3095.json) · Computational complexity · **high confidence** · Additional model or representation

The exact width-three threshold for unordered CNF games is a clause-width classification inside a specialized strategic assignment model. Its saved reach is narrower than the general game-solving barriers.

Saved sources: 6-Uniform Maker-Breaker Game Is PSPACE-Complete.

### 22. TCS-3317 — Logspace-completeness of the Grigorchuk word problem

[TCS-3317](../../data/cards/TCS-3317.json) · Algebraic computation · **high confidence** · Specialized target

Locating the word problem of the single Grigorchuk group exactly at LOGSPACE is a fine classification within algorithmic group theory rather than a broad solvability barrier.

Saved sources: Groups with ALOGTIME-Hard Word Problems and PSPACE-Complete Circuit Value Problems.

### 23. TCS-3324 — Tarski’s exponential function problem

[TCS-3324](../../data/cards/TCS-3324.json) · Semantics, logic and verification · **high confidence** · Consolidate with retained card

Decidability of the real exponential field is stated explicitly in TCS-7230. Preserve the weighted-automaton application reference there and remove the redundant occurrence.

Retain: [TCS-7230](../../data/cards/TCS-7230.json). Transfer and check scope before removal.

Saved sources: The Big-O Problem for Labelled Markov Chains and Weighted Automata.

### 24. TCS-3332 — Finite approximations for accessible completely iterative algebras

[TCS-3332](../../data/cards/TCS-3332.json) · Semantics, logic and verification · **high confidence** · Additional model or representation

Extending a finite-approximation theorem from finitary to accessible set functors concerns a specialized categorical semantics framework. Its saved rationale gives limited independent computational consequences.

Saved sources: On Free Completely Iterative Algebras.

### 25. TCS-3484 — Word-equation satisfiability in NP

[TCS-3484](../../data/cards/TCS-3484.json) · Automated reasoning and unification · **high confidence** · Consolidate with retained card

This repeats the NP-membership frontier of ordinary word-equation satisfiability represented by TCS-0163. Consolidation must retain the plain-equation convention and must not add regular constraints or inversion.

Retain: [TCS-0163](../../data/cards/TCS-0163.json). Transfer and check scope before removal.

Saved sources: Hardness Results for Constant-Free Pattern Languages and Word Equations.

### 26. TCS-3617 — Small deterministic parsimonious universal families

[TCS-3617](../../data/cards/TCS-3617.json) · Pseudorandomness and derandomization · **high confidence** · Specific construction or family

Reducing the leading size base of parsimonious universal families focuses on balanced set pairs and controlled multiplicities for one approximate-counting construction. Broader explicit randomness tools take priority.

Saved sources: Approximate Counting of k-Paths: Deterministic and in Polynomial Space; Approximate Counting of k-Paths: Simpler, Deterministic, and in Polynomial Space.

### 27. TCS-3731 — Inseparable degree in algebraic-independence testing

[TCS-3731](../../data/cards/TCS-3731.json) · Algebraic computation · **high confidence** · Specific method or reduction

The question asks how essential inseparable degree is to an algebraic-independence testing method. Its saved significance remains a dependency of that algorithmic framework rather than an independent major target.

Saved sources: Constructing Faithful Homomorphisms over Fields of Finite Characteristic.

### 28. TCS-3745 — Approximation of parameterized Set Cover in n^(k−ε) time

[TCS-3745](../../data/cards/TCS-3745.json) · Parameterized and exact algorithms · **high confidence** · Quantitative refinement

Approximation at an n^(k−epsilon) Set Cover budget focuses on an almost-exhaustive parameterized running-time slice. Retain the main Set Cover approximability and parameterized-hardness questions.

Saved sources: A Simple Gap-Producing Reduction for the Parameterized Set Cover Problem.

### 29. TCS-3788 — Randomized partitioning data structures

[TCS-3788](../../data/cards/TCS-3788.json) · Data structures · **high confidence** · Specific method or reduction

Randomized acceleration of partitioning is an internal route to faster approximate ordered-set operations. Retain the principal data-structure performance targets rather than this specific implementation primitive.

Saved sources: Dynamic Ordered Sets with Approximate Queries, Approximate Heaps and Soft Heaps.

### 30. TCS-3866 — Polynomial slide distances between graphs of groups

[TCS-3866](../../data/cards/TCS-3866.json) · Algebraic computation · **high confidence** · Specific method or reduction

Polynomial slide distance concerns certificates obtained through one transformation system for graphs of groups. Prefer the underlying isomorphism problems over a separate bound for this particular witness mechanism.

Saved sources: The Isomorphism Problem for Finite Extensions of Free Groups Is In PSPACE.

### 31. TCS-3867 — Polynomial-time black-box cost-sharing reductions

[TCS-3867](../../data/cards/TCS-3867.json) · Algorithmic game theory, mechanism design and fair division · **high confidence** · Specific method or reduction

Polynomial running time for the source's separable cost-sharing black-box reduction evaluates one transformation procedure rather than the intrinsic possibility of efficient truthful mechanisms.

Saved sources: Efficient Black-Box Reductions for Separable Cost Sharing.

### 32. TCS-3878 — Logarithmic randomized competitiveness of convex matching with delays

[TCS-3878](../../data/cards/TCS-3878.json) · Online algorithms · **high confidence** · Additional model or representation

Logarithmic randomized competitiveness for matching with convex delays on a uniform metric combines a specific impatience model with a restricted geometry. Broader matching-with-delay and online metric barriers take priority.

Saved sources: Impatient Online Matching.

### 33. TCS-3904 — Propositional resizing in cubical assemblies

[TCS-3904](../../data/cards/TCS-3904.json) · Semantics, logic and verification · **high confidence** · Additional model or representation

Propositional resizing specifically in predicative universes of cubical assemblies is a consistency property of one semantic construction. General computational univalence and type-theory foundations remain represented.

Saved sources: Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing.

### 34. TCS-3928 — Greedy versus bit-optimal LZ77 over arbitrary alphabets

[TCS-3928](../../data/cards/TCS-3928.json) · String algorithms and bioinformatics · **high confidence** · Quantitative refinement

The joint n,z,alphabet-size gap between greedy and bit-optimal LZ77 refines a particular encoding comparison. General compression approximation and information limits have broader coverage.

Saved sources: Relations Between Greedy and Bit-Optimal LZ77 Encodings.

### 35. TCS-3961 — Hardness of orthogonal-matrix permanents modulo primes

[TCS-3961](../../data/cards/TCS-3961.json) · Counting and enumeration · **high confidence** · Additional model or representation

Permanent hardness simultaneously restricted to orthogonal matrices and prime modular arithmetic adds a specialized algebraic input regime. General counting and permanent barriers are stronger representatives.

Saved sources: New Hardness Results for the Permanent Using Linear Optics.

### 36. TCS-4003 — Prover complexity of public-coin pseudodeterministic proofs

[TCS-4003](../../data/cards/TCS-4003.json) · Pseudorandomness and derandomization · **high confidence** · Additional model or representation

Prover complexity for the public-coin version of pseudodeterministic proofs adds a protocol-convention question to a particular canonical-output framework.

Saved sources: Pseudo-Deterministic Proofs.

### 37. TCS-4009 — Decidability of balance in integer circuits

[TCS-4009](../../data/cards/TCS-4009.json) · Computability and algorithmic information · **high confidence** · Additional model or representation

Undecidability of balance for selected integer-circuit operation sets classifies a specialized set-arithmetic model. Broader arithmetic and recurrence decision problems are stronger representatives.

Saved sources: Balance Problems for Integer Circuits.

### 38. TCS-4031 — Quasipolynomial AC⁰ self-learning

[TCS-4031](../../data/cards/TCS-4031.json) · Learning theory · **high confidence** · Additional model or representation

Quasipolynomial self-learning by AC0 circuits constrains both targets and learners to the same shallow model. General efficient learnability of circuit classes has broader marginal coverage.

Saved sources: Pseudo-Derandomizing Learning and Approximation.

### 39. TCS-4076 — Simulating monotone real circuits with MLP gates

[TCS-4076](../../data/cards/TCS-4076.json) · Computational complexity · **high confidence** · Additional model or representation

Polynomial simulation of monotone real circuits by MLP gates compares two specialized gate semantics. The saved motivation gives less independent reach than the principal monotone and unrestricted circuit targets.

Saved sources: Representations of Monotone Boolean Functions by Linear Programs.

### 40. TCS-4078 — Finite memory for infinite-horizon optimal paths

[TCS-4078](../../data/cards/TCS-4078.json) · Semantics, logic and verification · **high confidence** · Additional model or representation

Finite memory for a robot collecting expiring stochastic rewards concerns a particular reward-generation and routing model. General policy-memory and stochastic-control barriers have broader coverage.

Saved sources: The Robot Routing Problem for Collecting Aggregate Stochastic Rewards.

### 41. TCS-4084 — Unbounded-round hardness of INBA in M2

[TCS-4084](../../data/cards/TCS-4084.json) · Communication complexity and Boolean function analysis · **high confidence** · Specific method or reduction

Unbounded-round hardness of the source-defined INBA problem in M2 is an intermediate lower-bound target for a direct-sum programme. Prefer the general direct-sum questions over another framework-specific witness problem.

Saved sources: Two-Party Direct-Sum Questions Through the Lens of Multiparty Communication Complexity.

### 42. TCS-4138 — Properness of coalgebraic functors on convex sets

[TCS-4138](../../data/cards/TCS-4138.json) · Semantics, logic and verification · **high confidence** · Additional model or representation

Properness of specific coalgebraic functors on convex sets tests a technical condition for one rational-fixed-point framework. General behavioral equivalence and probabilistic verification barriers take priority.

Saved sources: Proper Functors and their Rational Fixed Point.

### 43. TCS-4151 — Rational versus real strategies in flow games

[TCS-4151](../../data/cards/TCS-4151.json) · Algorithmic game theory, mechanism design and fair division · **high confidence** · Additional model or representation

Rational sufficiency for strategies in the source's flow game adds a numerical-representation distinction inside one specialized game model, without a demonstrated wider computational consequence.

Saved sources: Flow Games.

### 44. TCS-4187 — Polynomial-calculus lower bounds for roots-of-unity 3-coloring

[TCS-4187](../../data/cards/TCS-4187.json) · Proof complexity · **high confidence** · Specific construction or family

Polynomial-calculus lower bounds for graph coloring specifically in the roots-of-unity encoding are an encoding-sensitive version of algebraic proof hardness. Prefer broader proof-system lower bounds.

Saved sources: Graph Colouring is Hard for Algorithms Based on Hilbert's Nullstellensatz and Gröbner Bases.

### 45. TCS-4205 — Invariant versus unrestricted bounded-depth formulas

[TCS-4205](../../data/cards/TCS-4205.json) · Computational complexity · **high confidence** · Additional model or representation

Imposing syntactic subspace invariance at fixed formula depth creates an additional symmetry restriction. Its maximal overhead is lower priority than the underlying unrestricted formula lower-bound questions.

Saved sources: Subspace-Invariant AC^0 Formulas.

### 46. TCS-4208 — Truly subquadratic LCWIS over fixed alphabets

[TCS-4208](../../data/cards/TCS-4208.json) · String algorithms and bioinformatics · **high confidence** · Additional model or representation

Truly subquadratic longest common weakly increasing subsequence for each fixed alphabet adds both monotonicity and alphabet restrictions to sequence comparison. Core edit and subsequence barriers take priority.

Saved sources: Tight Conditional Lower Bounds for Longest Common Increasing Subsequence.

### 47. TCS-4210 — Packet traversal time in compact routing

[TCS-4210](../../data/cards/TCS-4210.json) · Distributed, parallel and sublinear algorithms · **high confidence** · Specific method or reduction

The selected question adds packet-processing time to the source's compact geometric routing framework. It concerns making one representation operationally efficient rather than a separately selected general routing barrier.

Saved sources: Routing in Polygonal Domains.

### 48. TCS-4251 — Decidability for nilpotent group pseudovarieties

[TCS-4251](../../data/cards/TCS-4251.json) · Automata and formal languages · **high confidence** · Additional model or representation

Deciding transducer continuity specifically for nilpotent-group language varieties isolates one algebraic subclass of a specialized continuity framework. The general language-definability barriers are stronger representatives.

Saved sources: Continuity and Rational Functions.

### 49. TCS-4288 — F₁ versus FO² succinctness over words

[TCS-4288](../../data/cards/TCS-4288.json) · Automata and formal languages · **high confidence** · Additional model or representation

The succinctness comparison between F1 and FO2 over words is a restricted syntactic representation question after their expressive powers coincide. Its saved motivation does not show broader consequences beyond that comparison.

Saved sources: One-Dimensional Logic over Words.

### 50. TCS-4318 — Explicit quadratic dispersers at near-full entropy

[TCS-4318](../../data/cards/TCS-4318.json) · Pseudorandomness and derandomization · **high confidence** · Specific construction or family

The requested quadratic F2 disperser at r=n−o(n) is a particular construction ingredient for a circuit/#SAT framework. General extraction and circuit lower-bound targets are stronger representatives.

Saved sources: Circuit Size Lower Bounds and #SAT Upper Bounds Through a General Framework.

### 51. TCS-4330 — Density bounds in Karchmer–Raz–Wigderson communication arguments

[TCS-4330](../../data/cards/TCS-4330.json) · Communication complexity and Boolean function analysis · **high confidence** · Specific method or reduction

The density conjecture for X inside X0 concerns a technical step in a particular approach to KRW composition. The main composition conjecture is the stronger representative for the reduced catalogue.

Saved sources: Toward the KRW Composition Conjecture: Cubic Formula Lower Bounds via Communication Complexity.

### 52. TCS-4412 — Gate-elimination lower bounds for linear maps

[TCS-4412](../../data/cards/TCS-4412.json) · Computational complexity · **high confidence** · Specific method or reduction

The target asks what gate elimination can prove for linear maps. Retain explicit linear-map circuit lower bounds themselves before this separate limitation-or-success question for one proof method.

Saved sources: On the Limits of Gate Elimination.

### 53. TCS-4503 — Decidability of Wadge comparisons for tree automata

[TCS-4503](../../data/cards/TCS-4503.json) · Automata and formal languages · **high confidence** · Specific construction or family

Effective Wadge comparisons against the source's ordinal-indexed family of unambiguous tree automata concern one constructed hierarchy. Prefer the broader decidability and definability questions for tree languages.

Saved sources: On Unambiguous Regular Tree Languages of Index (0,2).

### 54. TCS-4519 — Axiom strength of inductive inference

[TCS-4519](../../data/cards/TCS-4519.json) · Computability and algorithmic information · **high confidence** · Specific method or reduction

Removing an extra axiom requirement from the source's inductive-inference arguments concerns the strength of a particular proof. General learning and computability principles take priority over this follow-up.

Saved sources: Inductive Inference and Reverse Mathematics.

### 55. TCS-4564 — Univalent presheaf models of cubical type theory

[TCS-4564](../../data/cards/TCS-4564.json) · Semantics, logic and verification · **high confidence** · Specific construction or family

A univalent presheaf model for the proposed interval-free cubical type theory is a foundation for one alternative formalism. General computational type-theory and univalence questions take priority.

Saved sources: Towards a Cubical Type Theory without an Interval.

### 56. TCS-4577 — Skolem problem

[TCS-4577](../../data/cards/TCS-4577.json) · Semantics, logic and verification · **high confidence** · Consolidate with retained card

This is another occurrence of the unrestricted Skolem decision problem already specified in TCS-5773. Preserve the nonterminating-process information-leakage reference there.

Retain: [TCS-5773](../../data/cards/TCS-5773.json). Transfer and check scope before removal.

Saved sources: Information Leakage of Non-Terminating Processes.

### 57. TCS-4582 — Complexity of robust appointment scheduling

[TCS-4582](../../data/cards/TCS-4582.json) · Online algorithms · **high confidence** · Specialized target

Joint robust appointment timing and ordering is a specialized scheduling model whose saved motivation has limited wider theoretical consequences compared with the principal scheduling objectives.

Saved sources: Robust Appointment Scheduling.

### 58. TCS-4599 — Blanket time of local-search load balancing

[TCS-4599](../../data/cards/TCS-4599.json) · Randomized algorithms and sampling · **high confidence** · Additional model or representation

Blanket time for local-search balls-into-bins on vertex-transitive graphs combines one allocation dynamics, one graph symmetry and one load-uniformity criterion. Broader random-walk and load-balancing barriers take priority.

Saved sources: Balls into bins via local search: cover time and maximum load.

### 59. TCS-4666 — Smoothed Pareto lower bounds for arbitrary feasible sets

[TCS-4666](../../data/cards/TCS-4666.json) · Beyond worst-case and average-case analysis · **high confidence** · Specific method or reduction

Extending the paper's Pareto lower bounds to every sufficiently large feasible set generalizes one construction-based result. Its saved significance remains a follow-up to that bound rather than a broad computational barrier.

Saved sources: Lower Bounds for the Average and Smoothed Number of Pareto Optima.

### 60. TCS-4696 — Succinct quantum arguments from Quantum Merkle trees

[TCS-4696](../../data/cards/TCS-4696.json) · Quantum computation · **high confidence** · Specific method or reduction

Succinct noninteractive local-Hamiltonian arguments specifically through Quantum Merkle trees ask for one construction route. Retain the broader succinct quantum-verification targets.

Saved sources: Quantum Merkle Trees.

### 61. TCS-4972 — Learning decision trees from uniform examples

[TCS-4972](../../data/cards/TCS-4972.json) · Learning theory · **high confidence** · Consolidate with retained card

Learning polynomial-size decision trees from uniform random labeled examples is already stated explicitly in TCS-7294. Preserve the backdoor-defense reference and the distinction from membership-query learning there.

Retain: [TCS-7294](../../data/cards/TCS-7294.json). Transfer and check scope before removal.

Saved sources: Backdoor Defense, Learnability and Obfuscation.

### 62. TCS-5034 — Computability of graph Shannon capacity

[TCS-5034](../../data/cards/TCS-5034.json) · Coding and information theory · **high confidence** · Consolidate with retained card

This is the same computability question for graph Shannon capacity stated precisely in TCS-7215. Transfer the additional reference to that card and remove the redundant occurrence.

Retain: [TCS-7215](../../data/cards/TCS-7215.json). Transfer and check scope before removal.

Saved sources: Dimension Reduction for Polynomials over Gaussian Space and Applications.

### 63. TCS-5118 — Optimality of Majority-of-Three learning

[TCS-5118](../../data/cards/TCS-5118.json) · Learning theory · **high confidence** · Specific method or reduction

Optimality of Majority-of-Three for every confidence level is about one simple ERM-combination procedure after optimal general learning rates are available. Its simplicity is appealing, but the algorithm-analysis follow-up has lower priority.

Saved sources: Majority-of-Three: The Simplest Optimal Learner?.

### 64. TCS-5170 — Using output labels in dihedral hidden subgroup algorithms

[TCS-5170](../../data/cards/TCS-5170.json) · Quantum computation · **high confidence** · Specific method or reduction

Using otherwise unstructured output labels in dihedral hidden-subgroup algorithms tests whether a particular discarded data source helps. Retain the hidden-subgroup algorithmic target itself.

Saved sources: Another Subexponential-time Quantum Algorithm for the Dihedral Hidden Subgroup Problem.

### 65. TCS-5182 — Square-root competitive ratio for online metric tours

[TCS-5182](../../data/cards/TCS-5182.json) · Online algorithms · **high confidence** · Additional model or representation

Online metric tours defined by irreversible placement into a fixed-size array impose a particular packing-and-ordering convention. The general online routing and matching barriers provide broader coverage.

Saved sources: Online Sorting and Online TSP: Randomized, Stochastic, and High-Dimensional.

### 66. TCS-5236 — Noninteractive private parity learning in the multiserver model

[TCS-5236](../../data/cards/TCS-5236.json) · Differential privacy · **high confidence** · Additional model or representation

Parity learning simultaneously constrained to noninteraction, multiple servers and computational differential privacy is a narrow escape case for one protocol framework. General private-learning and privacy-model separations provide broader coverage.

Saved sources: Necessary Conditions in Multi-Server Differential Privacy.

### 67. TCS-5246 — Graph isomorphism in polynomial time

[TCS-5246](applied-examples.md#tcs-5246) · Computational complexity · **high confidence** · Consolidate with retained card

The selected passage asks ordinary graph isomorphism in polynomial time, already represented by TCS-7222. Preserve its refinement-hierarchy reference in that card.

Retain: [TCS-7222](../../data/cards/TCS-7222.json). Transfer and check scope before removal.

Saved sources: Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem.

### 68. TCS-5312 — NP-hardness of Minimum Circuit Size

[TCS-5312](applied-examples.md#tcs-5312) · Computational complexity · **high confidence** · Consolidate with retained card

The NP-hardness question for ordinary truth-table MCSP is already part of TCS-4786. Preserve this paper's total-versus-partial circuit-extension context in the retained card.

Retain: [TCS-4786](../../data/cards/TCS-4786.json). Transfer and check scope before removal.

Saved sources: Simple Circuit Extensions for XOR in PTIME.

### 69. TCS-5314 — Word-equation satisfiability in NP

[TCS-5314](../../data/cards/TCS-5314.json) · Automated reasoning and unification · **high confidence** · Consolidate with retained card

This is another statement of ordinary word-equation satisfiability in NP. Preserve the explicit NP frontier and this source under the general complexity card TCS-0163.

Retain: [TCS-0163](../../data/cards/TCS-0163.json). Transfer and check scope before removal.

Saved sources: An Improved Version of Hmelevskii’s Theorem on Three-Variable Word Equations.

### 70. TCS-5329 — Superlinear bivariate noncommutative circuit lower bounds

[TCS-5329](../../data/cards/TCS-5329.json) · Algebraic computation · **high confidence** · Additional model or representation

The target simultaneously fixes two noncommuting variables and homogeneous circuits, seeking a superlinear degree bound. Retain unrestricted noncommutative lower bounds before this narrower model threshold.

Saved sources: New Lower Bounds Against Homogeneous Non-Commutative Circuits.

### 71. TCS-5453 — Subexponential UP from average-case NP tractability

[TCS-5453](../../data/cards/TCS-5453.json) · Beyond worst-case and average-case analysis · **high confidence** · Consolidate with retained card

This source pointer and TCS-2680 refer to the same paper and page containing the heuristic-average-case implication for UP. Retain the explicit conjecture in TCS-2680 and combine the references.

Retain: [TCS-2680](../../data/cards/TCS-2680.json). Transfer and check scope before removal.

Saved sources: Finding Errorless Pessiland in Error-Prone Heuristica.

### 72. TCS-5501 — NP-hardness of Minimum Circuit Size

[TCS-5501](applied-examples.md#tcs-5501) · Computational complexity · **high confidence** · Consolidate with retained card

This repeats the NP-hardness frontier for ordinary MCSP represented by TCS-4786. Transfer the sums-of-squares reference without confusing restricted-method lower bounds with NP-hardness.

Retain: [TCS-4786](../../data/cards/TCS-4786.json). Transfer and check scope before removal.

Saved sources: Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem.

### 73. TCS-5617 — Complete problems for modular total-search classes

[TCS-5617](../../data/cards/TCS-5617.json) · Computational complexity · **high confidence** · Unselected bundle of directions

The selected passage proposes PPAq-completeness for several unspecified additional natural problems. It is a programme of classifications rather than one chosen major total-search target.

Saved sources: On the Complexity of Modulo-q Arguments and the Chevalley - Warning Theorem.

### 74. TCS-5711 — Sparse polynomial approximation of OR-of-SUM functions

[TCS-5711](../../data/cards/TCS-5711.json) · Communication complexity and Boolean function analysis · **high confidence** · Specific construction or family

Sparse polynomial representations of the source's OR-of-SUM family are a particular algebraic simulation challenge. Retain broader circuit representation and lower-bound targets before this family-specific construction.

Saved sources: Limits on Representing Boolean Functions by Linear Combinations of Simple Functions: Thresholds, ReLUs, and Low-Degree Polynomials.

### 75. TCS-5737 — Word problem for the S-combinator

[TCS-5737](../../data/cards/TCS-5737.json) · Semantics, logic and verification · **high confidence** · Consolidate with retained card

Weak convertibility for closed S-only combinator terms is the word problem already covered by TCS-0913. Preserve the normalization and infinite-tree-semantics context from this source.

Retain: [TCS-0913](../../data/cards/TCS-0913.json). Transfer and check scope before removal.

Saved sources: A Lambda Calculus Satellite (Invited Talk).

### 76. TCS-5770 — Erdős girth conjecture

[TCS-5770](../../data/cards/TCS-5770.json) · Structural graph theory · **high confidence** · Consolidate with retained card

This is the introductory girth-conjecture occurrence from the same routing paper used by the precise TCS-2783. Consolidate there; do not collapse TCS-2783 with TCS-6500 without checking their different girth and graph-size quantifiers.

Retain: [TCS-2783](../../data/cards/TCS-2783.json). Transfer and check scope before removal.

Saved sources: Space-Stretch Tradeoff in Routing Revisited.

### 77. TCS-5845 — Complexity of planar treewidth

[TCS-5845](../../data/cards/TCS-5845.json) · Algorithms & data structures · **high confidence** · Consolidate with retained card

The saved target is exact treewidth on planar graphs, also represented by TCS-0771. Consolidate this occurrence and preserve its potential-maximal-clique reference there.

Retain: [TCS-0771](../../data/cards/TCS-0771.json). Transfer and check scope before removal.

Saved sources: A Polynomial Delay Algorithm Generating All Potential Maximal Cliques in Triconnected Planar Graphs.

### 78. TCS-5926 — Complexity of planar treewidth

[TCS-5926](../../data/cards/TCS-5926.json) · Algorithms & data structures · **high confidence** · Consolidate with retained card

The saved target is exact treewidth on planar graphs, also represented by TCS-0771. Preserve this paper's cubic-graph hardness context in the retained card rather than keeping another occurrence of the planar question.

Retain: [TCS-0771](../../data/cards/TCS-0771.json). Transfer and check scope before removal.

Saved sources: Treewidth Is NP-Complete on Cubic Graphs.

### 79. TCS-6324 — Time complexity of leaderless population protocols

[TCS-6324](../../data/cards/TCS-6324.json) · Distributed, parallel and sublinear algorithms · **high confidence** · Additional model or representation

Optimal leaderless-protocol time for eventually natural-linear functions and eventually constant predicates classifies exceptional cases outside the source's main theorem. Its scope is narrower than the general stable-computation barriers.

Saved sources: Hardness of Computing and Approximating Predicates and Functions with Leaderless Population Protocols.

### 80. TCS-6497 — Fast single-exponential constant-factor treewidth approximation

[TCS-6497](../../data/cards/TCS-6497.json) · Parameterized and exact algorithms · **high confidence** · Quantitative refinement

The source already achieves a single-exponential constant-factor treewidth approximation; its remaining question is a smaller exponential base. Do not retain a second card whose title can suggest the broader existence question is still open.

Saved sources: A Single-Exponential Time 2-Approximation Algorithm for Treewidth.

### 81. TCS-6755 — Optimal leading constant for Boolean k-CSP approximation

[TCS-6755](../../data/cards/TCS-6755.json) · Approximation algorithms and hardness of approximation · **high confidence** · Quantitative refinement

The leading coefficient in the optimal Boolean k-CSP approximation scale refines an already established quantitative regime. Prefer qualitative approximability classifications and larger unresolved approximation gaps.

Saved sources: The Constraint Satisfaction Problem: Complexity and Approximability.

### 82. TCS-6961 — Equilibrium efficiency in connection and cost-sharing games

[TCS-6961](../../data/cards/TCS-6961.json) · Algorithmic game theory, mechanism design and fair division · **high confidence** · Unselected bundle of directions

The saved target combines undirected connection and generalized cost-sharing games without choosing an equilibrium-efficiency measure. More importantly for selection, it is a cluster of model-specific bound questions rather than one major shared proposition.

Saved sources: Algorithmic Game Theory.

### 83. TCS-7132 — Prime implicates versus explicit model enumeration

[TCS-7132](../../data/cards/TCS-7132.json) · Computational complexity · **high confidence** · Additional model or representation

Prime-implicate size relative to explicit model enumeration compares two exhaustive descriptions. Its saved significance is narrower than the principal succinct-circuit representation barriers.

Saved sources: A Knowledge Compilation Map.

### 84. TCS-7135 — Polynomial-time negation of deterministic DNNF

[TCS-7135](../../data/cards/TCS-7135.json) · Automated reasoning and unification · **high confidence** · Consolidate with retained card

Polynomial-time negation of deterministic DNNF is already represented by TCS-0306. Transfer the survey reference and its smooth-variant note; retain the separate nonconstructive polynomial-size question TCS-7260.

Retain: [TCS-0306](../../data/cards/TCS-0306.json). Transfer and check scope before removal.

Saved sources: A Knowledge Compilation Map.

### 85. TCS-0028 — Injective quantum oracles: standard versus erasing access

[TCS-0028](../../data/cards/TCS-0028.json) · Quantum computation · **medium confidence** · Additional model or representation

Standard versus erasing access for injective quantum oracles isolates an interface convention. Its saved consequences are narrower than the principal quantum-query and computational-power separations.

Saved sources: Open Problems Related to Quantum Query Complexity.

### 86. TCS-0042 — Computing stable images of free-group endomorphisms

[TCS-0042](../../data/cards/TCS-0042.json) · Algebraic computation · **medium confidence** · Specialized target

Computing the stable image of a free-group endomorphism is a particular infinitary subgroup operation; the saved motivation does not establish consequences comparable to the retained general word, conjugacy and isomorphism barriers.

Saved sources: Algorithmic Problems in Group Theory.

### 87. TCS-0064 — Condorcet outcome for m independent binary issues

[TCS-0064](../../data/cards/TCS-0064.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Additional model or representation

The saved problem isolates Condorcet outcomes for independent binary issues. Its source-specific preference structure has less demonstrated reach than the retained general distortion and implementability questions.

Saved sources: Computational Social Dynamics.

### 88. TCS-0068 — AC0 on trees

[TCS-0068](../../data/cards/TCS-0068.json) · Computational complexity · **medium confidence** · Additional model or representation

The proposed AC0 characterization uses circuits indexed by individual unlabeled tree shapes. This adds a specialized nonuniform indexing convention beyond the principal circuit-versus-logic classifications.

Saved sources: Circuits, Logic and Games.

### 89. TCS-0094 — Uniform versus arbitrary stochastic resolvers

[TCS-0094](../../data/cards/TCS-0094.json) · Automata and formal languages · **medium confidence** · Additional model or representation

Uniform versus tuned probabilities for memoryless stochastic automaton resolvers isolates a probability-choice convention within one resolver model. The general existence and decidability of stochastic resolution are broader representatives.

Saved sources: Automata Exchange.

### 90. TCS-0096 — Fine-grained complexity of language emptiness for deterministic PDA

[TCS-0096](../../data/cards/TCS-0096.json) · Fine-grained complexity · **medium confidence** · Quantitative refinement

The subcubic-versus-superquadratic gap for deterministic PDA emptiness with fixed alphabets refines an efficiently decidable language task. Broader pushdown and reachability barriers take priority.

Saved sources: Automata Exchange.

### 91. TCS-0111 — Lower bounds for determinizability of weighted automata over \(\mathbb Q\)

[TCS-0111](../../data/cards/TCS-0111.json) · Automata and formal languages · **medium confidence** · Quantitative refinement

Hardness after decidability of rational weighted-automaton determinization is a finer classification of this representation conversion, with an additional ambiguity subclass. Prioritize the broader quantitative-language decision barriers.

Saved sources: Automata Exchange.

### 92. TCS-0168 — Word-automaton recognition of tree languages

[TCS-0168](../../data/cards/TCS-0168.json) · Automata and formal languages · **medium confidence** · Additional model or representation

Recognizing serialized tree properties by a word automaton under a well-formedness promise is a specialized constant-memory definability question. Its saved reach is narrower than the main automata equivalence and decidability barriers.

Saved sources: Antoine Amarilli: research questions.

### 93. TCS-0222 — Merlin–Arthur Communication Complexity of Connectivity

[TCS-0222](../../data/cards/TCS-0222.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Merlin–Arthur communication specifically for graph connectivity adds a certificate-and-randomness convention to one graph-property task. Broader communication and distributed verification barriers take priority.

Saved sources: Sublinear.info.

### 94. TCS-0292 — Low-degree Sherali–Adams proofs of rwPHP(PLS)

[TCS-0292](../../data/cards/TCS-0292.json) · Proof complexity · **medium confidence** · Additional model or representation

Low-degree Sherali–Adams proofs of rwPHP(PLS) concern one composed totality principle in a particular proof system. The main total-search and proof-system separation targets take priority.

Saved sources: Computational Complexity of Discrete Problems.

### 95. TCS-0302 — Excluding quasilinear-time log-space Max Clique

[TCS-0302](../../data/cards/TCS-0302.json) · Computational complexity · **medium confidence** · Additional model or representation

Excluding quasilinear-time logarithmic-space Max Clique under random access adds a problem-specific time-space target alongside the central SAT time-space barriers.

Saved sources: SIGACT Open Problems Column.

### 96. TCS-0304 — Stronger uniform depth-three majority lower bounds for SAT

[TCS-0304](../../data/cards/TCS-0304.json) · Computational complexity · **medium confidence** · Quantitative refinement

Crossing the n^(5/2) wire exponent for LOGTIME-uniform depth-three majority circuits on SAT fixes several resource restrictions at once. Prefer the broader threshold-circuit and formula lower-bound barriers.

Saved sources: Some Open Problems Regarding Lower Bounds For NP; Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits.

### 97. TCS-0308 — Formula versus circuit succinctness

[TCS-0308](../../data/cards/TCS-0308.json) · Computational complexity · **medium confidence** · Consolidate with retained card

The general polynomial formula-versus-circuit gap is represented by nonuniform NC1 versus P/poly in TCS-6712 under the standard bounded-fan-in Boolean convention. Preserve the formula viewpoint and align the basis and size conventions when consolidating.

Retain: [TCS-6712](../../data/cards/TCS-6712.json). Transfer and check scope before removal.

Saved sources: Antoine Amarilli: research questions.

### 98. TCS-0309 — Recognizing evasive Boolean functions

[TCS-0309](../../data/cards/TCS-0309.json) · Communication complexity and Boolean function analysis · **medium confidence** · Specialized target

Recognizing evasiveness of a represented Boolean function is an extra meta-complexity task for one decision-tree property. Prefer the main evasiveness conjectures and general circuit-minimization barriers.

Saved sources: Antoine Amarilli: research questions.

### 99. TCS-0517 — Near-linear-palette LOCAL coloring in O(log* n) rounds

[TCS-0517](../../data/cards/TCS-0517.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Quantitative refinement

The fixed Delta^1.001 palette at O(log-star n) rounds is an additional precise point in the distributed coloring tradeoff. Retain the main coloring and symmetry-breaking barriers before this palette refinement.

Saved sources: Open problems related to locality in distributed graph algorithms; Locality in Distributed Graph Algorithms; Local Conflict Coloring Revisited: Linial for Lists.

### 100. TCS-0535 — Vertex Connectivity in the LOCAL Model

[TCS-0535](../../data/cards/TCS-0535.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Specific method or reduction

The selected task matches actual local-separator running time to an existing O(nu k) query guarantee. It removes computational overhead in one search framework rather than addressing general vertex-connectivity complexity.

Saved sources: Sublinear.info.

### 101. TCS-0633 — Eventual non-negativity of Matrices

[TCS-0633](../../data/cards/TCS-0633.json) · Algebraic computation · **medium confidence** · Specialized target

The saved target is a hardness transfer from ultimate positivity to the nonnegative-power problem for one matrix. Prefer the underlying recurrence and linear-dynamics decision barriers over this additional reduction target.

Saved sources: Automata Exchange.

### 102. TCS-0646 — All-constant-factor parameterized approximation hardness of SVP in l1

[TCS-0646](../../data/cards/TCS-0646.json) · Lattices and computational number theory · **medium confidence** · Additional model or representation

All-constant-factor parameterized hardness specifically for l1-SVP adds a norm-and-parameter restriction to the lattice-hardness programme. General SVP approximation and cryptographic-factor barriers take priority.

Saved sources: SIGACT Open Problems Column.

### 103. TCS-0660 — Sub-square-root approximation in coMA for SVP

[TCS-0660](../../data/cards/TCS-0660.json) · Lattices and computational number theory · **medium confidence** · Additional model or representation

Sub-square-root SVP approximation in coMA adds a particular randomized-certificate convention to the lattice-certification cluster. Broader approximation hardness and certificate frontiers take priority.

Saved sources: SIGACT Open Problems Column.

### 104. TCS-0668 — Instance-optimal equilibrium identification in zero-sum matrix games

[TCS-0668](../../data/cards/TCS-0668.json) · Learning theory · **medium confidence** · Additional model or representation

Instance-dependent sample-optimal equilibrium identification in a noisy zero-sum matrix fixes a particular exploration model. General equilibrium computation and sequential-learning barriers have broader coverage.

Saved sources: COLT / PMLR.

### 105. TCS-0681 — Multiclass test-set overfitting

[TCS-0681](../../data/cards/TCS-0681.json) · Learning theory · **medium confidence** · Quantitative refinement

The speed of overfitting a reused multiclass test set refines the dependence on label count and adaptive accuracy queries. Prefer the broader adaptive-data-analysis and learning-characterization barriers.

Saved sources: COLT / PMLR.

### 106. TCS-0839 — AM vs. NP for Proofs of Proximity in Distribution Testing

[TCS-0839](../../data/cards/TCS-0839.json) · Property testing and distribution learning · **medium confidence** · Additional model or representation

AM-versus-NP assistance specifically in distribution proximity testing adds another proof-and-access model comparison. The broader interactive-proof and distribution-testing barriers remain represented.

Saved sources: Sublinear.info.

### 107. TCS-0855 — Query efficiency of PRGs constructed from arbitrary OWFs

[TCS-0855](../../data/cards/TCS-0855.json) · Pseudorandomness and derandomization · **medium confidence** · Specific method or reduction

Optimizing oracle evaluations in the generic OWF-to-PRG construction is an efficiency refinement of an established foundational implication. Broader assumption and derandomization questions take priority.

Saved sources: SIGACT Open Problems Column.

### 108. TCS-0967 — TSP in the Streaming Model

[TCS-0967](../../data/cards/TCS-0967.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

A factor below two for one-pass planar Euclidean TSP estimation fixes geometry, memory and accuracy simultaneously. It adds less coverage than the principal TSP and streaming optimization targets.

Saved sources: Sublinear.info.

### 109. TCS-1044 — Explicit matrices with large robust rectangle covers

[TCS-1044](../../data/cards/TCS-1044.json) · Communication complexity and Boolean function analysis · **medium confidence** · Specific method or reduction

Explicit robust rectangle-cover matrices are a combinatorial witness target for a particular lower-bound technique. General communication and explicit circuit lower bounds provide broader coverage.

Saved sources: Boolean Function Complexity: Advances and Frontiers (author's early draft).

### 110. TCS-1050 — Explicit input pairs resistant to partial monotone separation

[TCS-1050](../../data/cards/TCS-1050.json) · Communication complexity and Boolean function analysis · **medium confidence** · Specific method or reduction

The requested input families must resist partial monotone separation in both directions at a specified thinning scale. This is a strong technical ingredient for limited-negation lower bounds; the underlying circuit separations are broader targets.

Saved sources: Boolean Function Complexity: Advances and Frontiers (author's early draft); Lower Bounds for DeMorgan Circuits of Bounded Negation Width.

### 111. TCS-1051 — Logarithmic negation-depth lower bounds for monotone functions

[TCS-1051](../../data/cards/TCS-1051.json) · Computational complexity · **medium confidence** · Quantitative refinement

Logarithmic negation depth for efficient monotone-function computation isolates one nesting resource within limited-negation circuits. More general circuit separations provide broader coverage.

Saved sources: Boolean Function Complexity: Advances and Frontiers (author's early draft).

### 112. TCS-1062 — Balancing tree-like cutting-planes proofs

[TCS-1062](../../data/cards/TCS-1062.json) · Proof complexity · **medium confidence** · Specific method or reduction

Balancing tree-like Cutting Planes proofs is a structural transformation inside one restricted proof format. Principal arithmetic-proof lower bounds and encoded-size questions take priority.

Saved sources: Boolean Function Complexity: Advances and Frontiers (author's early draft).

### 113. TCS-1161 — Conondeterministic MAX-3-SAT below 2ⁿ time

[TCS-1161](../../data/cards/TCS-1161.json) · Fine-grained complexity · **medium confidence** · Specific method or reduction

A conondeterministic sub-2^n MAX-3-SAT algorithm is a particular certificate-based route to conditional circuit, rigidity and tensor consequences. Retain the main exact-SAT and lower-bound targets.

Saved sources: Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank.

### 114. TCS-1169 — Pass complexity of deterministic semi-streaming coloring

[TCS-1169](../../data/cards/TCS-1169.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Quantitative refinement

The exact deterministic pass count for semi-streaming O(Delta)-coloring refines one palette-memory regime. General streaming derandomization and distributed coloring barriers take priority.

Saved sources: Faster Deterministic Streaming Vertex Coloring.

### 115. TCS-1192 — Worst-case symmetry of information

[TCS-1192](../../data/cards/TCS-1192.json) · Computability and algorithmic information · **medium confidence** · Additional model or representation

Worst-case symmetry of information for the source's nondeterministic Kolmogorov measure adds another resource-bounded information identity. Broader symmetry-of-information and meta-complexity barriers take priority.

Saved sources: Hardness of Computing Nondeterministic Kolmogorov Complexity.

### 116. TCS-1201 — Model-checking classification for quantifier-free dependence logic

[TCS-1201](../../data/cards/TCS-1201.json) · Database theory and finite model theory · **medium confidence** · Additional model or representation

The classification fixes quantifier-free dependence logic and its team semantics. It adds a specialist logical-fragment boundary beside broader query-evaluation and definability classifications.

Saved sources: Disjunctions of Two Dependence Atoms.

### 117. TCS-1292 — Deterministic subquadratic-query graph reconstruction

[TCS-1292](../../data/cards/TCS-1292.json) · Algorithms & data structures · **medium confidence** · Additional model or representation

Deterministic distance-query reconstruction for bounded-degree graphs is an extra algorithm-and-oracle restriction beside the broader reconstruction targets. Its saved motivation gives limited reason to allocate a separate place to removing randomness in this setting.

Saved sources: Cutwidth Versus BFS-Width with Applications to Graph Reconstruction from Distance Queries.

### 118. TCS-1538 — Queue number versus mixed number

[TCS-1538](../../data/cards/TCS-1538.json) · Structural graph theory · **medium confidence** · Additional model or representation

Mixed stack-and-queue layouts versus queue-only layouts add an intermediate representation parameter to the broader stack/queue relationship. That extra comparison has lower marginal priority.

Saved sources: Transforming Stacks into Queues: Mixed and Separated Layouts of Graphs.

### 119. TCS-1610 — A quadratic barrier for counting the four-edge hypergraph H△

[TCS-1610](../../data/cards/TCS-1610.json) · Counting and enumeration · **medium confidence** · Specific construction or family

The proposed quadratic hardness assumption singles out one four-edge hypergraph to support a sparse-pattern counting classification. Its broader consequences are narrower than those of the established central counting and fine-grained hypotheses.

Saved sources: Subgraph Counting in Subquadratic Time for Bounded Degeneracy Graphs; Subgraph Counting in Subquadratic Time for Bounded Degeneracy Graphs — version record.

### 120. TCS-1656 — Polynomial-time McNaughton games

[TCS-1656](../../data/cards/TCS-1656.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Polynomial-time solving of explicitly represented McNaughton games adds a winning-condition representation case next to the general regular-game barriers.

Saved sources: Deciding Regular Games: a Playground for Exponential Time Algorithms.

### 121. TCS-1762 — Optimal spanner sparsity in ℓₚ spaces

[TCS-1762](../../data/cards/TCS-1762.json) · Computational geometry and metric spaces · **medium confidence** · Quantitative refinement

Exact spanner-sparsity optimality for each stretch in fixed lp spaces between l1 and l2 sharpens a particular geometric tradeoff. General metric compression and spanner barriers provide broader coverage.

Saved sources: Lipschitz Decompositions of Finite 𝓁_{p} Metrics.

### 122. TCS-1798 — Sparse fault-tolerant pairwise distance oracles

[TCS-1798](../../data/cards/TCS-1798.json) · Data structures · **medium confidence** · Additional model or representation

Fault-tolerant distance oracles for arbitrary requested pairs combine failure handling with another query-set restriction. The saved exact-or-approximate direction has less marginal coverage than the main distance-oracle barriers.

Saved sources: Fault-Tolerant Approximate Distance Oracles with a Source Set.

### 123. TCS-1846 — Edge Coloring below 2ᵐ time

[TCS-1846](../../data/cards/TCS-1846.json) · Parameterized and exact algorithms · **medium confidence** · Quantitative refinement

A fixed improvement below the 2^m edge-coloring search scale is a quantitative exact-algorithm target. Broader coloring and exponential-time barriers take priority in this batch.

Saved sources: Faster Edge Coloring by Partition Sieving.

### 124. TCS-1929 — Statistical zero-knowledge streaming interactive proofs

[TCS-1929](../../data/cards/TCS-1929.json) · Cryptography · **medium confidence** · Additional model or representation

Statistical or perfect zero knowledge specifically for streaming interactive proofs adds a verifier-memory restriction to the general zero-knowledge existence questions.

Saved sources: Streaming Zero-Knowledge Proofs.

### 125. TCS-1934 — Bounded-aspect-ratio shortest-path-preserving graphs

[TCS-1934](../../data/cards/TCS-1934.json) · Algorithms & data structures · **medium confidence** · Specific construction or family

Polynomial aspect ratio under constant-stretch shortest-path preservation asks for a particular numerical normalization of graph representations. Prefer the principal shortest-path and metric-preservation barriers.

Saved sources: Are There Graphs Whose Shortest Path Structure Requires Large Edge Weights?.

### 126. TCS-1955 — Fourier concentration after shallow quantum preprocessing

[TCS-1955](../../data/cards/TCS-1955.json) · Quantum computation · **medium confidence** · Specific method or reduction

Exponential Fourier-tail decay for shallow quantum preprocessing is a structural route to hybrid-circuit lower bounds. Retain the central parity-versus-hybrid-circuit target before this stronger analytic ingredient.

Saved sources: Parity vs. AC0 with Simple Quantum Preprocessing.

### 127. TCS-2076 — Optimal mixing of global Kawasaki dynamics on bounded-degree graphs

[TCS-2076](../../data/cards/TCS-2076.json) · Randomized algorithms and sampling · **medium confidence** · Quantitative refinement

Improving global Kawasaki mixing from quadratic to n log n in the stated fast-mixing regime sharpens the rate of one sampling dynamics. General sampling tractability and phase boundaries have broader coverage.

Saved sources: Fast and Slow Mixing of the Kawasaki Dynamics on Bounded-Degree Graphs; Fast and Slow Mixing of the Kawasaki Dynamics on Bounded-Degree Graphs — final version.

### 128. TCS-2097 — A general 3/2 communication lower bound for reliable broadcast

[TCS-2097](../../data/cards/TCS-2097.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Quantitative refinement

The unrestricted 3/2 leading bandwidth coefficient is practically meaningful, but remains a sharp-constant target for one Byzantine broadcast model after protocols reach the proposed scale. Marked borderline rather than trivial.

Saved sources: Byzantine Reliable Broadcast with Low Communication and Time Complexity; MiniCast: Minimizing the Communication Complexity of Reliable Broadcast; Towards Reliable Broadcast with Optimal Communication and Round Complexity; Efficient Byzantine Reliable Broadcast in the Failure Case.

### 129. TCS-2126 — Polynomial smoothed complexity of value iteration

[TCS-2126](../../data/cards/TCS-2126.json) · Beyond worst-case and average-case analysis · **medium confidence** · Specific method or reduction

Polynomial smoothed complexity evaluates value iteration under the source's perturbation model. Prefer the intrinsic game-solving barriers over an additional analysis target for this particular algorithm.

Saved sources: Smoothed Analysis of Deterministic Discounted and Mean-Payoff Games.

### 130. TCS-2244 — Constant Degree Hypothesis

[TCS-2244](../../data/cards/TCS-2244.json) · Computational complexity · **medium confidence** · Additional model or representation

The Constant Degree Hypothesis fixes a particular AND/MOD/MOD architecture motivated by nilpotent-algebra algorithms. Broader modular-circuit lower bounds cover the central computational obstacle.

Saved sources: Circuit Equivalence in 2-Nilpotent Algebras.

### 131. TCS-2247 — Linear-size DAG compression from bounded flip-width

[TCS-2247](../../data/cards/TCS-2247.json) · Algorithms & data structures · **medium confidence** · Specific method or reduction

Linear-size DAG compression is one proposed representation for exploiting bounded flip-width. The target is narrower than the underlying graph-class algorithmic questions, even though successful compression could support several algorithms.

Saved sources: Faster Graph Algorithms Through DAG Compression.

### 132. TCS-2319 — Explicit constructions from NC⁰₃ range avoidance

[TCS-2319](../../data/cards/TCS-2319.json) · Computational complexity · **medium confidence** · Specific method or reduction

Reducing explicit constructions to range avoidance at locality three is a particular reduction route within the avoidance programme. General avoidance and explicit-construction targets have broader marginal coverage.

Saved sources: Range Avoidance for Constant Depth Circuits: Hardness and Algorithms.

### 133. TCS-2331 — Optimal-size certification in BPPᴺᴾ

[TCS-2331](../../data/cards/TCS-2331.json) · Computational complexity · **medium confidence** · Quantitative refinement

Improving NP-oracle certification from a polynomial overhead in Cert(f) to constant-factor length is an additional quantitative optimization of an existing certification guarantee.

Saved sources: Certification with an NP Oracle.

### 134. TCS-2336 — Sharp multiclass online regret without logarithmic factors

[TCS-2336](../../data/cards/TCS-2336.json) · Learning theory · **medium confidence** · Quantitative refinement

Removing the remaining square-root logarithmic factor from multiclass Littlestone regret sharpens an established learnability characterization. The infinite-label uniformity matters, so this is a borderline quantitative cut.

Saved sources: Multiclass Online Learning and Uniform Convergence.

### 135. TCS-2422 — NP-hardness of small-space sparse parity learning

[TCS-2422](../../data/cards/TCS-2422.json) · Learning theory · **medium confidence** · Additional model or representation

Hardness of learning sparse parities using small-program outputs adds a representation restriction motivated by a particular PCP-to-learning route. General noisy-parity and computational-learning barriers take priority.

Saved sources: Regularization of Low Error PCPs and an Application to MCSP.

### 136. TCS-2434 — Randomized versus pseudodeterministic parity decision trees

[TCS-2434](../../data/cards/TCS-2434.json) · Computational complexity · **medium confidence** · Additional model or representation

A randomness-versus-pseudodeterminism separation specifically for parity decision trees adds a query-model restriction to the broader reproducible-computation question.

Saved sources: Query Complexity of Search Problems.

### 137. TCS-2537 — UniqueTarski in UEOPL

[TCS-2537](../../data/cards/TCS-2537.json) · Computational complexity · **medium confidence** · Specialized target

Placing the total version of UniqueTarski in UEOPL is one further membership relation within fixed-point search classes. Prefer the main fixed-point and total-search structural barriers.

Saved sources: Reducing Tarski to Unique Tarski (In the Black-Box Model).

### 138. TCS-2540 — MSO₂ certificate lower bounds on bounded-clique-width graphs

[TCS-2540](../../data/cards/TCS-2540.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Polynomial certificate lower bounds specifically for MSO2 on bounded-clique-width graphs combine a logical-fragment restriction with a structural promise. General local-certification barriers give broader coverage.

Saved sources: Distributed Certification for Classes of Dense Graphs.

### 139. TCS-2650 — Quantum meta-complexity hardness from QETH and QSETH

[TCS-2650](../../data/cards/TCS-2650.json) · Quantum computation · **medium confidence** · Specific method or reduction

Deriving quantum circuit/state minimization hardness from QETH or QSETH is a particular conditional reduction programme. The principal quantum meta-complexity and quantum-hardness targets provide broader coverage.

Saved sources: Quantum Meets the Minimum Circuit Size Problem.

### 140. TCS-2688 — Optimal-time rendezvous on arbitrary connected graphs

[TCS-2688](../../data/cards/TCS-2688.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Specialized target

Optimal rendezvous time on arbitrary possibly infinite graphs is a specialized mobile-agent coordination problem with asynchronous starts and labels. The saved reach is narrower than the main distributed symmetry-breaking targets.

Saved sources: How to Meet at a Node of Any Connected Graph.

### 141. TCS-2730 — Thus, even in the non-succinct case, designing worst-case update operations is an open problem.

[TCS-2730](../../data/cards/TCS-2730.json) · Data structures · **medium confidence** · Quantitative refinement

Worst-case updates for indexed lists ask to remove amortization in one order-maintenance structure. Broader dynamic-data-structure limits take priority.

Saved sources: Succinct List Indexing in Optimal Time.

### 142. TCS-2744 — Existence of values in all-pay bidding games

[TCS-2744](../../data/cards/TCS-2744.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Additional model or representation

Value existence for all-pay graph bidding concerns a specialized payment-and-control convention. General stochastic-game and equilibrium barriers are stronger representatives for this smaller pool.

Saved sources: An Updated Survey of Bidding Games on Graphs (Invited Talk).

### 143. TCS-2896 — Sublinear-space constant-factor Euclidean Steiner forest

[TCS-2896](../../data/cards/TCS-2896.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Sublinear-space Euclidean Steiner forest with exactly paired terminals isolates a promise that escapes an existing lower bound. It is lower priority than the broader connectivity and streaming approximation frontiers.

Saved sources: Streaming Algorithms for Geometric Steiner Forest.

### 144. TCS-3038 — Linear-space finger search with logarithmic distance cost

[TCS-3038](../../data/cards/TCS-3038.json) · String algorithms and bioinformatics · **medium confidence** · Additional model or representation

Logarithmic-distance finger movement in linear grammar space is an additional locality-sensitive navigation guarantee for compressed strings. General compressed random access and grammar-compression barriers take priority.

Saved sources: Compression by Contracting Straight-Line Programs.

### 145. TCS-3146 — Adaptive linear-sketch query complexity of planted-clique detection

[TCS-3146](../../data/cards/TCS-3146.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Exact bounded-coefficient linear queries to planted-clique instances impose a specialist access model with unrestricted computation. Prefer the primary planted-clique computational and statistical barriers over this additional query tradeoff.

Saved sources: Average-Case Communication Complexity of Statistical Problems; Average-Case Communication Complexity of Statistical Problems — author version record.

### 146. TCS-3162 — Phase transitions in erasure-resilient connectivity testing

[TCS-3162](../../data/cards/TCS-3162.json) · Property testing and distribution learning · **medium confidence** · Quantitative refinement

The second erasure threshold for connectivity testing refines the phase diagram between known testing and impossibility regimes. It has lower marginal priority than the general missing-data and graph-testing questions.

Saved sources: Erasure-Resilient Sublinear-Time Graph Algorithms.

### 147. TCS-3181 — Branching-program lower bounds for random CNF search

[TCS-3181](../../data/cards/TCS-3181.json) · Computational complexity · **medium confidence** · Specific construction or family

Transferring bounded-repetition branching-program lower bounds from a modified formula to random CNFs improves the hard-instance family for one restricted proof model.

Saved sources: Branching Programs with Bounded Repetitions and Flow Formulas.

### 148. TCS-3183 — Coefficient size in short Res-LinB refutations

[TCS-3183](../../data/cards/TCS-3183.json) · Proof complexity · **medium confidence** · Additional model or representation

Coefficient-size necessity in short Res-LinB refutations adds a numerical-encoding tradeoff within a specialized proof calculus. Broader encoded-size and arithmetic-proof barriers remain represented.

Saved sources: A Lower Bound for Polynomial Calculus with Extension Rule.

### 149. TCS-3339 — FPT recovery of graph incidence matrices under low-rank binary perturbations

[TCS-3339](../../data/cards/TCS-3339.json) · Parameterized and exact algorithms · **medium confidence** · Additional model or representation

FPT recovery of graph-incidence matrices under binary low-rank perturbations fixes both a representation and a corruption model across several graph classes. Its marginal reach is narrower than general low-rank recovery and graph-recognition barriers.

Saved sources: On the Complexity of Recovering Incidence Matrices.

### 150. TCS-3363 — Recognizing instance-optimizable functions

[TCS-3363](../../data/cards/TCS-3363.json) · Beyond worst-case and average-case analysis · **medium confidence** · Additional model or representation

Testing whether a represented function admits an instance-optimal decision tree is a recognition problem internal to a particular optimality benchmark. It adds less coverage than the principal decision-tree and instance-optimal algorithm targets.

Saved sources: Instance Complexity and Unlabeled Certificates in the Decision Tree Model.

### 151. TCS-3392 — Constant lifetime recourse for competitive online matching on the line

[TCS-3392](../../data/cards/TCS-3392.json) · Online algorithms · **medium confidence** · Additional model or representation

Constant lifetime recourse for every request adds an individual-stability constraint to online matching on the line. General online matching remains represented; this additional recourse convention is a borderline cut.

Saved sources: Online Minimum Cost Matching with Recourse on the Line; Online Metric Matching on the Line with Recourse; On the Stability of Minimum-Weight Perfect Matching on the Line.

### 152. TCS-3436 — Time lower bounds for constant-message leader election

[TCS-3436](../../data/cards/TCS-3436.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

The time lower bound fixes constant visible-message alphabets while allowing larger private population-protocol state. It adds another communication convention to the leader-election resource cluster.

Saved sources: Message Complexity of Population Protocols.

### 153. TCS-3450 — Hardness of distribution-free learning with local queries

[TCS-3450](../../data/cards/TCS-3450.json) · Learning theory · **medium confidence** · Quantitative refinement

Extending local-query hardness to polynomial Hamming radii moves the threshold in a particular label-access model. Prefer the principal membership-query and example-only learning comparisons.

Saved sources: Distribution Free Learning with Local Queries.

### 154. TCS-3512 — Universal versus weakly universal simultaneous-message protocols

[TCS-3512](../../data/cards/TCS-3512.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Universal versus weakly universal simultaneous-message protocols compare two function-family information conventions. This extra model conversion is lower priority than the main communication-power comparisons.

Saved sources: Universal Communication, Universal Graphs, and Graph Labeling.

### 155. TCS-3514 — PAC-learning hardness versus natural-proof barriers under universality

[TCS-3514](../../data/cards/TCS-3514.json) · Pseudorandomness and derandomization · **medium confidence** · Specific method or reduction

The PAC-hardness versus natural-properties equivalence is conditional on the particular Universality Conjecture. It is an additional organizing implication beside the main learning, pseudorandomness and natural-proof barriers.

Saved sources: Pseudorandomness and the Minimum Circuit Size Problem; On Basing Lower-Bounds for Learning on Worst-Case Assumptions; Witness Encryption and NP-Hardness of Learning.

### 156. TCS-3530 — Finite-state representation of all winning strategies

[TCS-3530](../../data/cards/TCS-3530.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Finite-state descriptions of all winning strategies under synchronous-automaton observation equivalence extend a particular imperfect-information presentation model. General strategy-existence and synthesis barriers take priority.

Saved sources: Observation and Distinction. Representing Information in Infinite Games.

### 157. TCS-3594 — Double-exponential succinctness of alternating good-for-games automata

[TCS-3594](../../data/cards/TCS-3594.json) · Automata and formal languages · **medium confidence** · Quantitative refinement

Doubly exponential succinctness for stronger acceptance conditions adds another conversion gap inside alternating good-for-games automata. General recognition and resolution questions have broader marginal value.

Saved sources: Good for Games Automata: From Nondeterminism to Alternation.

### 158. TCS-3609 — #Wfunc[2]-complete conjunctive-query classes

[TCS-3609](../../data/cards/TCS-3609.json) · Counting and enumeration · **medium confidence** · Lower marginal value within a cluster

A #Wfunc[2]-complete query class is one proposed witness for the broader intermediate query-counting question in TCS-6083. Keep the broader target and record this candidate route there; these formulations are not asserted equivalent.

Saved sources: Counting Answers to Existential Questions (Track B: Automata, Logic, Semantics, and Theory of Programming).

### 159. TCS-3717 — Constant-round distribution-free junta testing

[TCS-3717](../../data/cards/TCS-3717.json) · Property testing and distribution learning · **medium confidence** · Additional model or representation

Constant-round distribution-free junta testing with polynomial queries adds an adaptivity cap to an already specialized testing model. General junta and adaptivity barriers take priority.

Saved sources: Almost Optimal Distribution-Free Junta Testing.

### 160. TCS-3718 — NP circuit bounds versus infinitely-often hierarchy collapse

[TCS-3718](../../data/cards/TCS-3718.json) · Computational complexity · **medium confidence** · Specific method or reduction

Equating fixed-polynomial NP circuit lower bounds with a particular infinitely-often Karp–Lipton collapse is an additional conditional characterization. The main lower-bound and hierarchy questions already represent the intended consequences.

Saved sources: Relations and Equivalences Between Circuit Lower Bounds and Karp-Lipton Theorems.

### 161. TCS-3726 — Deterministic message reduction without time loss

[TCS-3726](../../data/cards/TCS-3726.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Specific method or reduction

A deterministic message-reduction scheme with no time loss is a derandomization target for one generic simulation method. Prioritize the main time-and-message limits of distributed computation.

Saved sources: Message Reduction in the LOCAL Model Is a Free Lunch.

### 162. TCS-3743 — NQP circuit lower bounds or MCSP outside ACC⁰

[TCS-3743](../../data/cards/TCS-3743.json) · Computational complexity · **medium confidence** · Specific method or reduction

The NQP-or-MCSP disjunction is a particular route to stronger circuit lower bounds. The independent circuit-separation and MCSP-hardness targets already represent its main intended outcomes.

Saved sources: AC^0[p] Lower Bounds Against MCSP via the Coin Problem.

### 163. TCS-3761 — Private conditional-disclosure lower bounds for easy communication tasks

[TCS-3761](../../data/cards/TCS-3761.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

ppCDS lower bounds specifically for predicates with easy randomized communication refine one conditional-secret-release model. General secret-sharing and privacy-versus-communication barriers take priority.

Saved sources: Placing Conditional Disclosure of Secrets in the Communication Complexity Universe.

### 164. TCS-3762 — Exact random-walk simulation in graph streams

[TCS-3762](../../data/cards/TCS-3762.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Perfect rather than approximate graph-streaming random-walk simulation adds an exact-sampling requirement to a restricted-access model. More general sampling and streaming barriers take priority.

Saved sources: Simulating Random Walks on Graphs in the Streaming Model.

### 165. TCS-3787 — Unlabeled compression of ample classes

[TCS-3787](../../data/cards/TCS-3787.json) · Learning theory · **medium confidence** · Specific construction or family

Extending the source's unlabeled compression construction from maximum to ample classes is a structured-family route. Retain the general compression barriers before this additional geometric subclass target.

Saved sources: Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes.

### 166. TCS-3799 — Large-error approximate-degree lower bounds for AC⁰

[TCS-3799](../../data/cards/TCS-3799.json) · Communication complexity and Boolean function analysis · **medium confidence** · Quantitative refinement

The large-error approximate-degree target fixes a linked depth, advantage and exponent regime for AC0. It contributes another quantitative slice beside the broader polynomial-approximation and circuit lower-bound questions.

Saved sources: The Large-Error Approximate Degree of AC^0.

### 167. TCS-3801 — State lower bounds for alternating parity translations

[TCS-3801](../../data/cards/TCS-3801.json) · Automata and formal languages · **medium confidence** · Quantitative refinement

Improving the state lower bound for translating alternating parity automata to weaker acceptance conditions is an additional representation-cost target within the automata translation cluster.

Saved sources: Alternating Weak Automata from Universal Trees.

### 168. TCS-3806 — Polynomial-pass parameterized streaming Vertex Cover

[TCS-3806](../../data/cards/TCS-3806.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Polynomially many passes for Vertex Cover at O(k log n) bits fixes both parameterized storage and a streaming access convention. This additional three-resource tradeoff has lower marginal coverage.

Saved sources: Towards a Theory of Parameterized Streaming Algorithms.

### 169. TCS-3821 — Separating SoML from PPA in communication

[TCS-3821](../../data/cards/TCS-3821.json) · Communication complexity and Boolean function analysis · **medium confidence** · Quantitative refinement

Replacing the PPADS communication separation by a SoML separation strengthens one relation inside the total-search class landscape. It is lower priority than the principal class-separation questions.

Saved sources: Adventures in Monotone Complexity and TFNP.

### 170. TCS-3839 — Exponential matrix-monoid bounds for affine integer VASS

[TCS-3839](../../data/cards/TCS-3839.json) · Semantics, logic and verification · **medium confidence** · Quantitative refinement

An exponential bound on finite matrix-monoid representations improves a reduction's size in affine integer VASS. The principal affine reachability and counter-system decidability barriers take priority.

Saved sources: Affine Extensions of Integer Vector Addition Systems with States.

### 171. TCS-3865 — Exponential complementation cost for unambiguous automata

[TCS-3865](../../data/cards/TCS-3865.json) · Automata and formal languages · **medium confidence** · Lower marginal value within a cluster

Exponential unambiguous-automaton complementation cost is the proposed hard endpoint of the broader gap-closing target TCS-0128. Keep that endpoint and source as context there, rather than another card for the same conversion programme; no equality of the two propositions is claimed.

Saved sources: A Superpolynomial Lower Bound for the Size of Non-Deterministic Complement of an Unambiguous Automaton.

### 172. TCS-3871 — Private randomness in algorithmic mutual-information protocols

[TCS-3871](../../data/cards/TCS-3871.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Replacing shared randomness by private randomness in the source's algorithmic mutual-information protocol adds a resource-convention variant of one operational characterization.

Saved sources: An Operational Characterization of Mutual Information in Algorithmic Information Theory.

### 173. TCS-3873 — SDD versus d-SDNNF succinctness

[TCS-3873](../../data/cards/TCS-3873.json) · Computational complexity · **medium confidence** · Additional model or representation

SDD versus deterministic structured-DNNF succinctness compares two closely related compiled representations. More general knowledge-compilation closure and representation barriers take priority.

Saved sources: Connecting Width and Structure in Knowledge Compilation.

### 174. TCS-3892 — CONGEST lower bounds for all-pairs spanner construction

[TCS-3892](../../data/cards/TCS-3892.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

CONGEST construction lower bounds for all-pairs additive spanners add another bandwidth-restricted realization of the spanner programme. Prefer its main sparsity limits and broader distributed graph barriers.

Saved sources: The Sparsest Additive Spanner via Multiple Weighted BFS Trees.

### 175. TCS-3894 — Polynomial-state leaderless protocols for linear inequalities

[TCS-3894](../../data/cards/TCS-3894.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Polynomial-state leaderless population protocols for systems of inequalities ask for succinct implementation in a particular initialization model. General population-protocol and arithmetic-computation limits take priority.

Saved sources: Large Flocks of Small Birds: on the Minimal Size of Population Protocols.

### 176. TCS-3915 — Transductions of bounded-expansion relational classes

[TCS-3915](../../data/cards/TCS-3915.json) · Structural graph theory · **medium confidence** · Additional model or representation

Extending a bounded-expansion transduction characterization from graphs to general relational structures broadens one structural framework by signature arity. Other core graph-structure and finite-model-theory barriers have greater marginal coverage.

Saved sources: First-Order Interpretations of Bounded Expansion Classes.

### 177. TCS-3945 — MA versus AM proofs of proximity

[TCS-3945](../../data/cards/TCS-3945.json) · Property testing and distribution learning · **medium confidence** · Quantitative refinement

Matching a particular quadratic MA-versus-AM proximity-proof separation sharpens the size of an already studied interaction gap. Broader proof-model separations have greater marginal coverage.

Saved sources: An Exponential Separation Between MA and AM Proofs of Proximity.

### 178. TCS-3960 — Earthmover-resilient testing versus tolerant testing

[TCS-3960](../../data/cards/TCS-3960.json) · Property testing and distribution learning · **medium confidence** · Additional model or representation

Separating ordinary and tolerant testing specifically under earthmover resilience introduces a specialized robustness condition on ordered structures. General tolerant-testing boundaries take priority.

Saved sources: Earthmover Resilience and Testing in Ordered Structures.

### 179. TCS-3962 — MCSP-oracle algorithms for NP from SAT in P/poly

[TCS-3962](../../data/cards/TCS-3962.json) · Computational complexity · **medium confidence** · Specific method or reduction

The implication from small SAT circuits to NP algorithms with an MCSP oracle is a conditional algorithmic route. Prefer the primary circuit-minimization and nonuniform-complexity barriers.

Saved sources: The Power of Natural Properties as Oracles.

### 180. TCS-4006 — Intermediate sliding-window space for context-free languages

[TCS-4006](../../data/cards/TCS-4006.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Quantitative refinement

The target fills the interval between squared-logarithmic and linear sliding-window space for deterministic context-free languages. This is a finer landscape question inside a specialized access model.

Saved sources: Sliding Windows over Context-Free Languages.

### 181. TCS-4030 — Sample optimality of log-concave maximum likelihood

[TCS-4030](../../data/cards/TCS-4030.json) · Property testing and distribution learning · **medium confidence** · Specific method or reduction

Sample optimality of the log-concave MLE in dimensions at least four evaluates a particular estimator. General density-learning limits and computational tractability are broader targets.

Saved sources: Near-Optimal Sample Complexity Bounds for Maximum Likelihood Estimation of Multivariate Log-concave Densities.

### 182. TCS-4061 — UGC hardness of homology localization

[TCS-4061](../../data/cards/TCS-4061.json) · Computational geometry and metric spaces · **medium confidence** · Additional model or representation

UGC-based constant-factor hardness for surface homology localization with a factor-dependent coefficient group combines a specific topological objective and algebraic convention. Broader approximation and topology barriers take priority.

Saved sources: Computational Topology and the Unique Games Conjecture.

### 183. TCS-4072 — Characterizing functors with disjunctive bases

[TCS-4072](../../data/cards/TCS-4072.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Classifying coalgebraic functors that admit a disjunctive basis asks when one modal normal-form framework applies. Broader modal expressiveness, equivalence and decidability principles have greater marginal coverage.

Saved sources: Disjunctive Bases: Normal Forms for Modal Logics.

### 184. TCS-4081 — Complete axiomatization of expanding intuitionistic temporal logic

[TCS-4081](../../data/cards/TCS-4081.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Complete axiomatization of the decidable expanding intuitionistic temporal logic adds a deduction-system target for one temporal semantics. Broader logical decidability and constructive-proof barriers take priority.

Saved sources: A Decidable Intuitionistic Temporal Logic.

### 185. TCS-4121 — Distributed Tree Augmentation below factor two

[TCS-4121](../../data/cards/TCS-4121.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Additional model or representation

Beating factor two for distributed Tree Augmentation adds a communication-model restriction to a particular approximation objective. Broader approximation and resilient-network barriers are stronger representatives.

Saved sources: Fast Distributed Approximation for TAP and 2-Edge-Connectivity.

### 186. TCS-4124 — Modular separability versus VAS reachability

[TCS-4124](../../data/cards/TCS-4124.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Comparing modular-separator hardness with full VAS reachability studies one restricted periodic invariant language. The main reachability and invariant-synthesis barriers take priority.

Saved sources: Separability of Reachability Sets of Vector Addition Systems.

### 187. TCS-4132 — Regret for online full permutations

[TCS-4132](../../data/cards/TCS-4132.json) · Online algorithms · **medium confidence** · Quantitative refinement

The exact regret rate for full-permutation bandit ranking fills one boundary case of a combinatorial-feedback analysis. Broader combinatorial bandit and online assignment targets have greater marginal coverage.

Saved sources: Tight Bounds for Bandit Combinatorial Optimization.

### 188. TCS-4134 — Computing the self-directed learning mistake bound

[TCS-4134](../../data/cards/TCS-4134.json) · Learning theory · **medium confidence** · Specialized target

Computing the self-directed mistake bound is another meta-problem for a particular learning dimension. Prefer the main statistical and computational learnability characterizations.

Saved sources: Inapproximability of VC Dimension and Littlestone’s Dimension.

### 189. TCS-4194 — Small approximate Voronoi diagrams of flats

[TCS-4194](../../data/cards/TCS-4194.json) · Computational geometry and metric spaces · **medium confidence** · Specific construction or family

An O(n^(k+1))-size approximate Voronoi diagram for affine flats asks for one global representation at a precise size scale. Broader nearest-neighbor and geometric-search barriers take priority.

Saved sources: Approximate Nearest Neighbor Search Amid Higher-Dimensional Flats.

### 190. TCS-4202 — Group isomorphism via asymmetric groups

[TCS-4202](../../data/cards/TCS-4202.json) · Algebraic computation · **medium confidence** · Specific method or reduction

Reducing group isomorphism to asymmetric instances investigates one normalization route. The unrestricted finite-group isomorphism target is a stronger representative of the main computational obstacle.

Saved sources: A Polynomial-Time Randomized Reduction from Tournament Isomorphism to Tournament Asymmetry.

### 191. TCS-4203 — Cycle Packing in 2^(O(k log k)) time

[TCS-4203](../../data/cards/TCS-4203.json) · Parameterized and exact algorithms · **medium confidence** · Quantitative refinement

The 2^(O(k log k)) Cycle Packing target sharpens parameter growth for one exact graph problem. Larger tractability and directed-cycle barriers take priority.

Saved sources: Packing Cycles Faster Than Erdos-Posa.

### 192. TCS-4221 — Sum-of-squares automatability on the Boolean cube

[TCS-4221](../../data/cards/TCS-4221.json) · Proof complexity · **medium confidence** · Additional model or representation

Sum-of-squares automatability specifically after replacing interval constraints by Boolean equalities isolates a domain restriction within a proof-search framework. Broader automatability barriers provide more coverage.

Saved sources: SOS Is Not Obviously Automatizable, Even Approximately.

### 193. TCS-4236 — Hyperbolic-geodesic realizability of combinatorial immersions

[TCS-4236](../../data/cards/TCS-4236.json) · Computational geometry and metric spaces · **medium confidence** · Specialized target

Recognizing curve immersions realizable as geodesics for some hyperbolic metric is a specialized geometric realization problem. The saved motivation has less computational reach than the main geometric primitives.

Saved sources: Computing the Geometric Intersection Number of Curves.

### 194. TCS-4249 — Existence of committees with justified representation

[TCS-4249](../../data/cards/TCS-4249.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Additional model or representation

Existence for the paper's particular justified-representation variant adds another fairness axiom to the allocation and voting cluster; the saved motivation does not show why this variant deserves a separate benchmark place.

Saved sources: Justified Representation in Multiwinner Voting: Axioms and Algorithms.

### 195. TCS-4261 — Super-n^(3/2) lower bounds for fault-tolerant additive spanners

[TCS-4261](../../data/cards/TCS-4261.json) · Algorithms & data structures · **medium confidence** · Quantitative refinement

The requested super-n^(3/2) bound fixes additive error two and one failure. It is another precise point in the fault-tolerant spanner tradeoff, with less marginal coverage than the principal spanner questions.

Saved sources: Preserving Distances in Very Faulty Graphs.

### 196. TCS-4268 — Intermediate complexity of constant-gap MCSP

[TCS-4268](../../data/cards/TCS-4268.json) · Computational complexity · **medium confidence** · Quantitative refinement

Extending intermediate-complexity evidence to a fixed epsilon in the source's Gap MCSP parameterization refines a particular approximation regime. Retain the main MCSP classification and hardness questions.

Saved sources: New Insights on the (Non-)Hardness of Circuit Minimization and Related Problems.

### 197. TCS-4269 — Flip distance of labeled triangulations

[TCS-4269](../../data/cards/TCS-4269.json) · Computational geometry and metric spaces · **medium confidence** · Additional model or representation

Shortest flip sequences that transport edge labels add an identity-preservation constraint to triangulation reconfiguration. Prefer the more general geometric and topological transformation barriers.

Saved sources: A Proof of the Orbit Conjecture for Flipping Edge-Labelled Triangulations.

### 198. TCS-4307 — Dynamic maintenance of ECRPQs

[TCS-4307](../../data/cards/TCS-4307.json) · Dynamic graph algorithms · **medium confidence** · Additional model or representation

Dynamic maintenance of extended conjunctive regular path queries adds a specialized navigational query language to the dynamic-logic cluster. Broader dynamic reachability and query-maintenance principles have greater marginal coverage.

Saved sources: Dynamic Graph Queries.

### 199. TCS-4317 — Subexponential reductions from Feedback Vertex Set to 3-SAT

[TCS-4317](../../data/cards/TCS-4317.json) · Fine-grained complexity · **medium confidence** · Specific method or reduction

A subexponential reduction family from Feedback Vertex Set to 3-SAT is a particular transfer within ETH-based graph algorithms. The principal graph-cycle and hypothesis-relationship questions have broader coverage.

Saved sources: On Existential MSO and its Relation to ETH.

### 200. TCS-4320 — Weak versus Lutz PSPACE randomness

[TCS-4320](../../data/cards/TCS-4320.json) · Computability and algorithmic information · **medium confidence** · Additional model or representation

Weak versus Lutz polynomial-space randomness compares two resource-bounded randomness definitions. The saved motivation is primarily internal to the analysis-inspired weak definition.

Saved sources: Polynomial Space Randomness in Analysis.

### 201. TCS-4336 — Characterizing large token-reconfiguration thresholds

[TCS-4336](../../data/cards/TCS-4336.json) · Structural graph theory · **medium confidence** · Additional model or representation

The converse characterization for large token-addition/removal thresholds concerns a specific independent-set reconfiguration measure. General reconfiguration complexity and structural tractability barriers take priority.

Saved sources: Independent-Set Reconfiguration Thresholds of Hereditary Graph Classes.

### 202. TCS-4339 — Planar subgraph isomorphism without treewidth dependence

[TCS-4339](../../data/cards/TCS-4339.json) · Parameterized and exact algorithms · **medium confidence** · Additional model or representation

Removing host-treewidth dependence from a planar subgraph-isomorphism bound fills a structural case left by the source's embedding algorithm. General subgraph-isomorphism and planar complexity barriers have broader coverage.

Saved sources: Subexponential Time Algorithms for Embedding H-Minor Free Graphs.

### 203. TCS-4365 — Decidability of strong homomorphisms and embeddings

[TCS-4365](../../data/cards/TCS-4365.json) · Database theory and finite model theory · **medium confidence** · Additional model or representation

Strong homomorphisms and embeddings between first-order definable structures add map-preservation conventions to the source's decidable injective case. General homomorphism and definability barriers have broader coverage.

Saved sources: Homomorphism Problems for First-Order Definable Structures.

### 204. TCS-4369 — Tractable enumeration for well-designed pattern trees

[TCS-4369](../../data/cards/TCS-4369.json) · Counting and enumeration · **medium confidence** · Additional model or representation

The conjecture fills one remaining tractability case for well-designed pattern-tree enumeration. Its saved motivation is a specialist query-model classification rather than a wider enumeration principle.

Saved sources: On the Complexity of Enumerating the Answers to Well-designed Pattern Trees.

### 205. TCS-4393 — Online nonpreemptive scheduling without speed augmentation

[TCS-4393](../../data/cards/TCS-4393.json) · Online algorithms · **medium confidence** · Specific method or reduction

Replacing speed augmentation by a new rejection rule asks how to extend the source's nonpreemptive scheduling guarantees. The main scheduling approximability and online feasibility barriers take priority.

Saved sources: Online Non-Preemptive Scheduling in a Resource Augmentation Model Based on Duality.

### 206. TCS-4404 — Linear-size cylindrical grids from planar directed treewidth

[TCS-4404](../../data/cards/TCS-4404.json) · Structural graph theory · **medium confidence** · Quantitative refinement

Removing a polylogarithmic loss in planar directed grid/crossbar size sharpens a routing-oriented structural theorem. General directed grid and disjoint-path barriers provide broader coverage.

Saved sources: Constant Congestion Routing of Symmetric Demands in Planar Directed Graphs.

### 207. TCS-4427 — Recognizing k-isohedral polyomino tilings

[TCS-4427](../../data/cards/TCS-4427.json) · Computational geometry and metric spaces · **medium confidence** · Additional model or representation

Efficient recognition of k-isohedral polyomino tilings fixes a particular symmetry-orbit convention. General tiling decidability and geometric recognition questions have broader coverage.

Saved sources: A Quasilinear-Time Algorithm for Tiling the Plane Isohedrally with a Polyomino.

### 208. TCS-4449 — Instance-wise adaptation cost in fixed-budget best-arm identification

[TCS-4449](../../data/cards/TCS-4449.json) · Online algorithms · **medium confidence** · Quantitative refinement

Adapting to easier gap profiles after a worst-case best-arm adaptation lower bound is an additional instance-level refinement. General finite-budget identification and optimal exploration remain represented.

Saved sources: Tight (Lower) Bounds for the Fixed Budget Best Arm Identification Bandit Problem.

### 209. TCS-4466 — Efficiently reducing negations in Boolean formulas

[TCS-4466](../../data/cards/TCS-4466.json) · Computational complexity · **medium confidence** · Specific method or reduction

An efficient negation-reduction transformation for formulas is a constructive follow-up to the source's existence arguments. Broader formula power and limited-negation lower bounds take priority.

Saved sources: Negation-Limited Formulas.

### 210. TCS-4469 — qq-QAM versus BP·PP

[TCS-4469](../../data/cards/TCS-4469.json) · Quantum computation · **medium confidence** · Additional model or representation

The BP·PP upper bound for qq-QAM is a further containment for a specific two-quantum-message proof convention. Broader quantum interactive-proof class comparisons take priority.

Saved sources: Generalized Quantum Arthur-Merlin Games.

### 211. TCS-4478 — Decidability of one-counter strategy-logic model checking

[TCS-4478](../../data/cards/TCS-4478.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Decidability of the Boolean-goal one-counter Strategy Logic fragments adds a specialized strategic logic to the infinite-state verification cluster. Broader counter-system and game-solving barriers have greater marginal coverage.

Saved sources: Weighted Strategy Logic with Boolean Goals Over One-Counter Games.

### 212. TCS-4491 — Concatenation closure of real-time cellular-automaton languages

[TCS-4491](../../data/cards/TCS-4491.json) · Automata and formal languages · **medium confidence** · Additional model or representation

Concatenation closure under the exact real-time budget of one-dimensional cellular automata adds a timing-and-dimension-specific closure question to broader automata and parallel-computation targets.

Saved sources: Comparing 1D and 2D Real Time on Cellular Automata.

### 213. TCS-4505 — Geometric constraints in planar morphing

[TCS-4505](../../data/cards/TCS-4505.json) · Computational geometry and metric spaces · **medium confidence** · Quantitative refinement

Polynomial geometric size throughout a planar morph adds numerical control to an existing transformation programme. It is lower priority than the main feasibility and complexity barriers for geometric transformations.

Saved sources: Optimal Morphs of Convex Drawings.

### 214. TCS-4509 — Quantum money with exponentially many classical verifications

[TCS-4509](../../data/cards/TCS-4509.json) · Quantum computation · **medium confidence** · Quantitative refinement

Exponentially many classical verifications of secret-key quantum money optimizes lifetime under a particular verification interface and security convention. General quantum-money existence and verification barriers have broader coverage.

Saved sources: New Constructions for Quantum Money.

### 215. TCS-4515 — Existence of weak subgame-perfect equilibria

[TCS-4515](../../data/cards/TCS-4515.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Additional model or representation

The selected target weakens permitted deviations for a particular infinite-game class. Prefer broad equilibrium-existence and computation barriers over this additional stability convention.

Saved sources: Weak Subgame Perfect Equilibria and their Application to Quantitative Reachability.

### 216. TCS-4522 — Quantum–classical communication gaps at I = 0

[TCS-4522](../../data/cards/TCS-4522.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

The maximum quantum–classical gap under the source's zero-information distribution restriction adds a specialized distributional convention to the general communication-separation targets.

Saved sources: Correlation in Hard Distributions in Communication Complexity.

### 217. TCS-4528 — Constant-space Cutting Planes with polynomial coefficients

[TCS-4528](../../data/cards/TCS-4528.json) · Proof complexity · **medium confidence** · Additional model or representation

Constant Cutting Planes line space with polynomial coefficients combines two restrictions on proof storage. The broader total-space and encoded-proof-size questions give better marginal coverage.

Saved sources: The Space Complexity of Cutting Planes Refutations.

### 218. TCS-4535 — Conjunctive positive query evaluation on finite groups

[TCS-4535](../../data/cards/TCS-4535.json) · Database theory and finite model theory · **medium confidence** · Additional model or representation

Evaluating conjunctive positive queries on finite groups fixes both a logical fragment and an algebraic input class. General group computation and query-evaluation barriers take priority.

Saved sources: First-Order Queries on Finite Abelian Groups.

### 219. TCS-4551 — Superpolynomial multi-k-ic formula lower bounds

[TCS-4551](../../data/cards/TCS-4551.json) · Algebraic computation · **medium confidence** · Additional model or representation

Multi-k-ic formulas interpolate between restricted arithmetic models. Keep broad formula and multilinear-circuit lower bounds before adding another syntactic individual-degree restriction.

Saved sources: Multi-k-ic Depth Three Circuit Lower Bound.

### 220. TCS-4563 — Containment of Datalog in regular queries

[TCS-4563](../../data/cards/TCS-4563.json) · Database theory and finite model theory · **medium confidence** · Additional model or representation

Containment of Datalog inside regular graph queries is a specific cross-language verification target. Broader query-rewritability and recursive-language decision barriers provide more coverage.

Saved sources: Regular Queries on Graph Databases.

### 221. TCS-4572 — Efficient list decoding of general Gabidulin codes

[TCS-4572](../../data/cards/TCS-4572.json) · Coding and information theory · **medium confidence** · Specific construction or family

List decoding unrestricted Gabidulin codes, conditional on manageable list size, is a code-family-specific algorithmic target. General list-decoding and coding-rate barriers take priority in the smaller pool.

Saved sources: Evading Subspaces Over Large Fields and Explicit List-decodable Rank-metric Codes.

### 222. TCS-4586 — Instance-optimal quantum oracle identification

[TCS-4586](../../data/cards/TCS-4586.json) · Quantum computation · **medium confidence** · Quantitative refinement

Instance-optimal quantum oracle identification refines worst-case candidate-count and input-length bounds for a particular known hypothesis set. General quantum learnability and query-power barriers have broader coverage.

Saved sources: An optimal quantum algorithm for the oracle identification problem.

### 223. TCS-4621 — Optimal Littlestone-dimension bounds for multiclass bandits

[TCS-4621](../../data/cards/TCS-4621.json) · Learning theory · **medium confidence** · Quantitative refinement

Sharp realizable and agnostic bandit bounds in terms of label count and Littlestone dimension refine an existing feedback-cost programme. The broader price-of-bandit-information target remains represented.

Saved sources: The price of bandit information in multiclass online classification.

### 224. TCS-4647 — Approximate-degree lower bounds for depth-two AC⁰[⊕]

[TCS-4647](../../data/cards/TCS-4647.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Approximate-degree lower bounds specifically for depth-two AC0 with parity add both depth and gate restrictions to the polynomial-method cluster. Broader circuit and approximation barriers take priority.

Saved sources: Certifying polynomials for AC^0(parity) circuits, with applications.

### 225. TCS-4664 — Subquadratic deterministic communication for general matching

[TCS-4664](../../data/cards/TCS-4664.json) · Communication complexity and Boolean function analysis · **medium confidence** · Quantitative refinement

Extending the bipartite matching communication upper bound to general graphs is an additional graph-property bound under deterministic split-input access. General matching and communication barriers have broader coverage.

Saved sources: New bounds on the classical and quantum communication complexity of some graph properties.

### 226. TCS-4679 — Strong balance versus graph isomorphism

[TCS-4679](../../data/cards/TCS-4679.json) · Constraint satisfaction · **medium confidence** · Quantitative refinement

The cost of recognizing strong balance sharpens the meta-complexity of an existing counting-CSP classification. Prefer the unresolved classification principles themselves before this additional GI-equivalence frontier.

Saved sources: The #CSP Dichotomy is Decidable.

### 227. TCS-4703 — Sublinear-communication streaming zero knowledge

[TCS-4703](../../data/cards/TCS-4703.json) · Cryptography · **medium confidence** · Quantitative refinement

Reducing setup-inclusive communication below linear for streaming zero knowledge is an additional resource optimization within the same restricted-verifier programme.

Saved sources: Streaming Zero-Knowledge Proofs.

### 228. TCS-4710 — Separations between certificate-game complexities

[TCS-4710](../../data/cards/TCS-4710.json) · Communication complexity and Boolean function analysis · **medium confidence** · Unselected bundle of directions

The card asks for any separation among a chain of several certificate-game measures. This is a collection of possible model comparisons; the saved rationale does not select one major separation to represent independently.

Saved sources: Certificate Games.

### 229. TCS-4712 — One-dimensional quantum advantage beyond NC⁰

[TCS-4712](../../data/cards/TCS-4712.json) · Quantum computation · **medium confidence** · Additional model or representation

Quantum advantage beyond NC0 specifically from one-dimensional local circuits adds a geometry restriction to shallow-quantum separation questions.

Saved sources: Single-qubit gate teleportation provides a quantum advantage.

### 230. TCS-4718 — T-gate complexity of pseudorandom quantum states

[TCS-4718](../../data/cards/TCS-4718.json) · Quantum computation · **medium confidence** · Quantitative refinement

The necessary T-gate count for computationally pseudorandom states quantifies one gate resource after a logarithmic obstruction. Broader pseudorandom-state and quantum computational-power questions take priority.

Saved sources: Low-Stabilizer-Complexity Quantum States Are Not Pseudorandom.

### 231. TCS-4734 — Locality-preserving quantum gap amplification

[TCS-4734](../../data/cards/TCS-4734.json) · Quantum computation · **medium confidence** · Specific method or reduction

A locality-preserving quantization of Dinur gap amplification is one technical strategy for quantum PCP. Keep the main conjecture before a separate card demanding the features of this particular classical route.

Saved sources: Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians.

### 232. TCS-4769 — Query-complexity separations under uncertainty

[TCS-4769](../../data/cards/TCS-4769.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

Linear versus polynomial query separations for uncertainty-extended functions are tied to an additional input-semantics model. Prefer the principal deterministic, randomized and quantum comparisons for ordinary total functions.

Saved sources: Sensitivity and Query Complexity Under Uncertainty.

### 233. TCS-4823 — Query reduction for good locally testable codes

[TCS-4823](../../data/cards/TCS-4823.json) · Coding and information theory · **medium confidence** · Specific method or reduction

A general query-reduction transformation for good LTCs is one route to better local testers. The principal existence and parameter limits for locally testable codes are stronger representatives.

Saved sources: Good Locally Testable Codes with Small Alphabet and Small Query Size.

### 234. TCS-4867 — AC⁰ classification of semigroup membership

[TCS-4867](../../data/cards/TCS-4867.json) · Algebraic computation · **medium confidence** · Lower marginal value within a cluster

The AC0 slice of semigroup-membership classification is a narrower component of the retained full finite-semigroup classification; it need not occupy another place alongside that target and the qAC0/NL dichotomy.

Saved sources: Efficient Compression in Semigroups.

### 235. TCS-4954 — Communication advantage with one clean qubit

[TCS-4954](../../data/cards/TCS-4954.json) · Quantum computation · **medium confidence** · Additional model or representation

A communication separation with one clean qubit adds a mixed-state initialization restriction to the general quantum-communication advantage question.

Saved sources: The Power of One Clean Qubit in Communication Complexity.

### 236. TCS-4961 — Range avoidance for bounded-locality circuits

[TCS-4961](../../data/cards/TCS-4961.json) · Computational complexity · **medium confidence** · Quantitative refinement

The requested faster range-avoidance algorithm fixes bounded locality and polynomial output stretch. It is an additional running-time regime within a programme already represented by more general avoidance targets.

Saved sources: Range Avoidance and Remote Point: New Algorithms and Hardness.

### 237. TCS-4992 — Constant entangled bias with vanishing classical bias

[TCS-4992](../../data/cards/TCS-4992.json) · Quantum computation · **medium confidence** · Quantitative refinement

Keeping entangled bias constant while classical bias vanishes strengthens an existing ratio-separation programme for multiparty XOR games. General nonlocal-game and communication separations have broader marginal coverage.

Saved sources: Bounding Quantum-Classical Separations for Classes of Nonlocal Games.

### 238. TCS-5021 — Asymptotic optimality of QAOA for random regular Max-Cut

[TCS-5021](../../data/cards/TCS-5021.json) · Quantum computation · **medium confidence** · Specific method or reduction

Asymptotic Max-Cut optimality of QAOA on random regular graphs analyzes one quantum optimization algorithm in a particular random-instance limit. Its physics connection matters, but general quantum optimization barriers take priority.

Saved sources: The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model.

### 239. TCS-5079 — Pointer quantum PCP conjecture

[TCS-5079](../../data/cards/TCS-5079.json) · Quantum computation · **medium confidence** · Additional model or representation

Pointer quantum PCP adds a structured proof format and an intermediate conjecture to the quantum-PCP cluster. It is distinct from the main conjecture, but has lower marginal priority as another proposed route.

Saved sources: Pointer Quantum PCPs and Multi-Prover Games.

### 240. TCS-5100 — Robust monotone-circuit lower bounds from Newton polytopes

[TCS-5100](../../data/cards/TCS-5100.json) · Algebraic computation · **medium confidence** · Specific construction or family

The robust Newton-polytope obstruction asks for hardness persisting under a source-specific relation between polynomials. General monotone and unrestricted arithmetic lower-bound targets provide broader representatives.

Saved sources: Shadows of Newton Polytopes.

### 241. TCS-5106 — One-round blind verifiable quantum computation

[TCS-5106](../../data/cards/TCS-5106.json) · Quantum computation · **medium confidence** · Additional model or representation

Adding blindness to one-round two-prover quantum delegation combines three protocol constraints. The principal efficient verification and private delegation barriers provide broader coverage.

Saved sources: A Simple Protocol for Verifiable Delegation of Quantum Computation in One Round.

### 242. TCS-5108 — Amplification cost in randomized query composition

[TCS-5108](../../data/cards/TCS-5108.json) · Communication complexity and Boolean function analysis · **medium confidence** · Specific method or reduction

Separating amplification costs for gap-majority and gap-OR composition probes two specific gadgets. The general randomized-composition barriers give broader coverage.

Saved sources: When Is Amplification Necessary for Composition in Randomized Query Complexity?.

### 243. TCS-5136 — Quantum distinguishing complexity versus approximate degree

[TCS-5136](../../data/cards/TCS-5136.json) · Quantum computation · **medium confidence** · Additional model or representation

An exponential gap between quantum distinguishing complexity and approximate degree introduces a specialized state-output measure for partial functions. More general quantum-query and polynomial-method barriers take priority.

Saved sources: Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge.

### 244. TCS-5149 — Threshold-circuit complexity of string matching

[TCS-5149](../../data/cards/TCS-5149.json) · Computational complexity · **medium confidence** · Additional model or representation

Threshold-circuit size specifically for string matching adds a function-specific restricted-circuit target. General threshold-circuit lower bounds and the main string-algorithm barriers have broader coverage.

Saved sources: String Matching: Communication, Circuits, and Learning.

### 245. TCS-5173 — Factor closure of constant-depth arithmetic circuits

[TCS-5173](../../data/cards/TCS-5173.json) · Algebraic computation · **medium confidence** · Additional model or representation

Factor closure for constant-depth circuits adds a depth-restricted closure question to an already represented factoring and circuit-class programme. Prefer the more general closure and derandomization barriers.

Saved sources: Deterministic Factorization of Constant-Depth Algebraic Circuits in Subexponential Time.

### 246. TCS-5186 — Unrestricted regret lower bounds for multi-task reinforcement learning

[TCS-5186](../../data/cards/TCS-5186.json) · Online algorithms · **medium confidence** · Additional model or representation

Extending a cluster-then-learn regret lower bound to unrestricted algorithms remains tied to the source's adversarial multitask RL model. Broader representation and exploration barriers take priority.

Saved sources: Adversarial Online Multi-Task Reinforcement Learning.

### 247. TCS-5253 — Noisy query complexity versus GapMaj composition

[TCS-5253](../../data/cards/TCS-5253.json) · Communication complexity and Boolean function analysis · **medium confidence** · Specific method or reduction

Uniform equivalence between noisy queries and GapMaj composition for arbitrary block size asks whether one gadget captures the full cost model. Broader noisy-computation and randomized-composition barriers take priority.

Saved sources: On the Composition of Randomized Query Complexity and Approximate Degree.

### 248. TCS-5304 — Randomized parity decision trees versus approximate sparsity

[TCS-5304](../../data/cards/TCS-5304.json) · Communication complexity and Boolean function analysis · **medium confidence** · Additional model or representation

The optimal gap between randomized parity decision trees and approximate sparsity adds a particular query-and-representation comparison to the communication lower-bound cluster.

Saved sources: Towards Stronger Counterexamples to the Log-Approximate-Rank Conjecture.

### 249. TCS-5315 — Randomized query complexity of extremal low-degree Forrelation

[TCS-5315](../../data/cards/TCS-5315.json) · Computational complexity · **medium confidence** · Specific construction or family

The target restricts extremal Forrelation to low-degree F2-polynomial inputs and seeks a degree-dependent randomized bound. Prefer the more general quantum–classical query barriers over this additional hard-family refinement.

Saved sources: Forrelation Is Extremally Hard.

### 250. TCS-5420 — Testing versus recovery in community detection

[TCS-5420](../../data/cards/TCS-5420.json) · Beyond worst-case and average-case analysis · **medium confidence** · Specific method or reduction

The selected task is a planted-clique reduction to one community-testing model. Prefer the principal average-case detection-versus-recovery barriers before adding this particular hardness-transfer route.

Saved sources: Is It Easier to Count Communities Than Find Them?.

### 251. TCS-5425 — Housing allocation in NC

[TCS-5425](../../data/cards/TCS-5425.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Specialized target

Parallel construction of a housing allocation or core is a problem-specific NC frontier beyond already parallel verification. The main allocation and parallel-computation barriers have broader coverage.

Saved sources: Parallel and Distributed Algorithms for the Housing Allocation Problem.

### 252. TCS-5478 — Sample complexity of stochastic shortest paths

[TCS-5478](../../data/cards/TCS-5478.json) · Learning theory · **medium confidence** · Unselected bundle of directions

The saved remainder combines bounded hitting-time sample complexity, interactive access and weaker goal-reaching assumptions for stochastic shortest paths. It is a collection of model-specific extensions rather than one selected main planning barrier.

Saved sources: Reaching Goals is Hard: Settling the Sample Complexity of the Stochastic Shortest Path.

### 253. TCS-5490 — Tandem-duplication reachability

[TCS-5490](../../data/cards/TCS-5490.json) · String algorithms and bioinformatics · **medium confidence** · Specialized target

Reachability under tandem duplications is a specialized string-rewriting model motivated by duplication histories. General word-equation, rewriting and sequence-algorithm barriers have broader coverage.

Saved sources: The Tandem Duplication Distance Is NP-Hard.

### 254. TCS-5492 — Space-efficient search-to-decision reductions for pseudorandomness

[TCS-5492](../../data/cards/TCS-5492.json) · Pseudorandomness and derandomization · **medium confidence** · Specific method or reduction

A space-efficient search-to-decision reduction for partial pseudorandomness would extend one equivalence to CL and L. Prefer the principal space-bounded derandomization questions before this specific reduction route.

Saved sources: Distinguishing, Predicting, and Certifying: On the Long Reach of Partial Notions of Pseudorandomness.

### 255. TCS-5571 — Subspace approximation of rank-one binary matrices

[TCS-5571](../../data/cards/TCS-5571.json) · Algebraic computation · **medium confidence** · Specialized target

Approximating the family of rank-one binary matrices by a linear subspace is tied to systematic linear bilinear-query structures. Its scope is narrower than the retained general matrix-rigidity and data-structure barriers.

Saved sources: Equivalence of Systematic Linear Data Structures and Matrix Rigidity.

### 256. TCS-5594 — Lower bounds for multi-output Karchmer–Wigderson games

[TCS-5594](../../data/cards/TCS-5594.json) · Communication complexity and Boolean function analysis · **medium confidence** · Quantitative refinement

Extending generalized Karchmer–Wigderson lower bounds beyond logarithmic output length fills the output-dimension range of a specific communication formulation. Prefer principal formula and composition lower bounds.

Saved sources: Super-Cubic Lower Bound for Generalized Karchmer-Wigderson Games.

### 257. TCS-5618 — Hitting sets for determinant and matrix-product orbits

[TCS-5618](../../data/cards/TCS-5618.json) · Pseudorandomness and derandomization · **medium confidence** · Specific construction or family

Hitting sets for affine orbits of determinant and iterated matrix multiplication concern two structured polynomial families under hidden coordinates. General identity testing and arithmetic-circuit derandomization barriers take priority.

Saved sources: Hitting Sets for Orbits of Circuit Classes and Polynomial Families.

### 258. TCS-5632 — Conditional-query complexity of support-size estimation

[TCS-5632](../../data/cards/TCS-5632.json) · Property testing and distribution learning · **medium confidence** · Additional model or representation

Support-size estimation with combined conditional-sampling and evaluation access fixes an unusually strong oracle. Broader distribution-learning and conditional-testing barriers provide more coverage.

Saved sources: Support Size Estimation: The Power of Conditioning.

### 259. TCS-5677 — Local certification gap on paths

[TCS-5677](../../data/cards/TCS-5677.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Quantitative refinement

A gap between log-log n and log n certificate size on paths refines one interval of the local-certification landscape. General certificate-size and locality tradeoffs take priority.

Saved sources: Complexity Landscape for Local Certification.

### 260. TCS-5706 — Unified bound for binary search trees

[TCS-5706](applied-examples.md#tcs-5706) · Data structures · **medium confidence** · Lower marginal value within a cluster

The unified locality bound is a distinct BST guarantee, but adds another specialist access-sequence criterion to an already well-represented adaptive-search cluster. Prioritize dynamic optimality and the canonical independent conjectures.

Saved sources: The Group Access Bounds for Binary Search Trees.

### 261. TCS-5768 — Sublogarithmic competitiveness of splay trees

[TCS-5768](../../data/cards/TCS-5768.json) · Data structures · **medium confidence** · Quantitative refinement

Sublogarithmic competitiveness of splay trees is an intermediate quantitative milestone within the dynamic-optimality programme. Preserve it as context for TCS-6498 instead of a separate benchmark card.

Saved sources: What Does Dynamic Optimality Mean in External Memory?.

### 262. TCS-5911 — Graph neural network verification under logical constraints

[TCS-5911](../../data/cards/TCS-5911.json) · Semantics, logic and verification · **medium confidence** · Unselected bundle of directions

Verification of GNNs under further logical input assumptions is an extension programme of a source's logic-based verification framework. The saved passage does not isolate a major new barrier within it.

Saved sources: Decidability of Graph Neural Networks via Logical Characterizations.

### 263. TCS-5941 — Complexity of dynamic persuasion with forward-looking agents

[TCS-5941](../../data/cards/TCS-5941.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Specialized target

The saved target bundles complexity classifications for forward-looking agents across dynamic persuasion and mechanism design. It supplies a specialist programme rather than one independently selected major barrier.

Saved sources: Sequential Decision Making With Information Asymmetry (Invited Talk).

### 264. TCS-6022 — Uniform sampling of directed Euler tours in RNC

[TCS-6022](../../data/cards/TCS-6022.json) · Distributed, parallel and sublinear algorithms · **medium confidence** · Specialized target

Uniform directed Euler-tour sampling in RNC is a parallelization frontier for one combinatorial distribution. General parallel sampling and graph-algorithm barriers take priority.

Saved sources: Sampling Arborescences in Parallel.

### 265. TCS-6026 — Isomorphism of automatically presented finitely generated groups

[TCS-6026](../../data/cards/TCS-6026.json) · Algebraic computation · **medium confidence** · Additional model or representation

The target compares automatic presentations of finitely generated virtually abelian groups. It adds a specialized presentation-effectivity problem beyond the broader group-isomorphism questions already retained.

Saved sources: Automatic Equivalence Structures of Polynomial Growth.

### 266. TCS-6034 — Capacitated edge-connectivity terminal backup

[TCS-6034](../../data/cards/TCS-6034.json) · Optimization and numerics · **medium confidence** · Additional model or representation

Exact classification of edge-capacitated terminal backup isolates one capacity convention within network design. More general flow, connectivity and approximation barriers provide broader coverage.

Saved sources: Node-Connectivity Terminal Backup, Separately-Capacitated Multiflow, and Discrete Convexity.

### 267. TCS-6040 — Strong approximation in learning coverage functions

[TCS-6040](../../data/cards/TCS-6040.json) · Learning theory · **medium confidence** · Additional model or representation

Strong approximation in coverage-function learning under the source's query and distribution restrictions is a specialist function-family target. Broader computational learning and private-release barriers take priority.

Saved sources: Learning Coverage Functions and Private Release of Marginals.

### 268. TCS-6074 — USBP versus SBP communication complexity

[TCS-6074](../../data/cards/TCS-6074.json) · Communication complexity and Boolean function analysis · **medium confidence** · Quantitative refinement

A larger USBP-versus-SBP communication separation sharpens a distinction between two very weak acceptance-probability conventions after a small separation is already supplied by the source.

Saved sources: Communication Complexity of Set-Disjointness for All Probabilities.

### 269. TCS-6089 — First-order rewritability of consistent query answering

[TCS-6089](../../data/cards/TCS-6089.json) · Database theory and finite model theory · **medium confidence** · Additional model or representation

First-order rewritability for the two named consistent-answer frameworks adds another mapping-and-repair-specific recognition question. Broader query rewritability and CSP classification barriers take priority.

Saved sources: On the Relationship between Consistent Query Answering and Constraint Satisfaction Problems.

### 270. TCS-6107 — Decidability of intuitionistic temporal logic with persistent models

[TCS-6107](../../data/cards/TCS-6107.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Decidability for persistent rather than expanding intuitionistic temporal models adds another semantic compatibility convention. General temporal and constructive-logical barriers take priority.

Saved sources: A Decidable Intuitionistic Temporal Logic.

### 271. TCS-6135 — Approximation–estimation tradeoffs under covariate shift

[TCS-6135](../../data/cards/TCS-6135.json) · Learning theory · **medium confidence** · Quantitative refinement

Optimizing the approximation constant against the statistical term in misspecified regression under covariate shift refines one error decomposition. More general learning-under-shift barriers have broader coverage.

Saved sources: Mitigating Covariate Shift in Misspecified Regression with Applications to Reinforcement Learning.

### 272. TCS-6150 — Efficient graph reconstruction from resistance queries

[TCS-6150](../../data/cards/TCS-6150.json) · Algorithms & data structures · **medium confidence** · Additional model or representation

Combining polynomial computation with subquadratic resistance queries is a reconstruction target in a particular electrical-measurement interface. General graph reconstruction and inverse-problem barriers take priority.

Saved sources: Graph Inference with Effective Resistance Queries.

### 273. TCS-6168 — EXP circuit lower bounds from NP-hardness of MCSP

[TCS-6168](../../data/cards/TCS-6168.json) · Computational complexity · **medium confidence** · Specific method or reduction

Strengthening the circuit consequences of MCSP NP-hardness, together with excluding one restricted reduction type, adds another conditional route around the same main meta-complexity barrier.

Saved sources: On the (Non) NP-Hardness of Computing Circuit Complexity.

### 274. TCS-6287 — Optimal local recovery in labeled block models

[TCS-6287](../../data/cards/TCS-6287.json) · Beyond worst-case and average-case analysis · **medium confidence** · Additional model or representation

Optimal local recovery for two communities with a positive revealed-label fraction adds a supervised-model restriction to the broader community-detection and local-versus-global inference questions.

Saved sources: Global and Local Information in Clustering Labeled Block Models.

### 275. TCS-6319 — Constant-competitive online matching on the line

[TCS-6319](../../data/cards/TCS-6319.json) · Optimization and numerics · **medium confidence** · Consolidate with retained card

The saved target repeats constant-competitive irrevocable online matching on the line in TCS-5158. Transfer the reference and align the deterministic/randomized convention before any deletion.

Retain: [TCS-5158](../../data/cards/TCS-5158.json). Transfer and check scope before removal.

Saved sources: Maintaining Perfect Matchings at Low Cost.

### 276. TCS-6343 — Finite versus chromatic memory in infinite games

[TCS-6343](../../data/cards/TCS-6343.json) · Semantics, logic and verification · **medium confidence** · Additional model or representation

Finite general memory versus chromatic memory on infinite arenas isolates what strategy updates may observe. This extra memory convention has lower marginal coverage than the main finite-memory determinacy questions.

Saved sources: Characterizing Omega-Regularity Through Finite-Memory Determinacy of Games on Infinite Graphs.

### 277. TCS-6393 — Lower bounds for conditional equivalence testing

[TCS-6393](../../data/cards/TCS-6393.json) · Property testing and distribution learning · **medium confidence** · Quantitative refinement

Strengthening a log-logarithmic lower bound for conditional equivalence testing is an additional quantitative refinement of a restricted-access comparison.

Saved sources: A Chasm Between Identity and Equivalence Testing with Conditional Queries.

### 278. TCS-6461 — Complexity growth in monitored random circuits

[TCS-6461](../../data/cards/TCS-6461.json) · Quantum computation · **medium confidence** · Specific construction or family

Approximate complexity growth for generic monitored random-circuit outputs extends specially engineered instances within a particular measurement model. Broader explicit quantum complexity and simulation barriers take priority.

Saved sources: Quantum complexity phase transitions in monitored random circuits.

### 279. TCS-6514 — Optimal decrease-key in pure pairing heaps

[TCS-6514](../../data/cards/TCS-6514.json) · Data structures · **medium confidence** · Additional model or representation

The decrease-key target concerns the specifically defined pure pairing-heap discipline. Its minimal-bookkeeping appeal is real, but this additional heap variant has lower priority than general priority-queue and dynamic-data-structure barriers.

Saved sources: Pure Pairing Heaps; A Tight Lower Bound for Decrease-Key in the Pure Heap Model; Efficiency of Self-Adjusting Heaps.

### 280. TCS-6718 — Exponential weakly read-once branching-program lower bounds

[TCS-6718](../../data/cards/TCS-6718.json) · Computational complexity · **medium confidence** · Additional model or representation

Exponential lower bounds for weakly read-once nondeterministic branching programs focus on the distinction between consistent and inconsistent paths. Broader branching-program and circuit separations take priority.

Saved sources: Boolean Function Complexity: Advances and Frontiers (author's early draft).

### 281. TCS-6736 — Nearly quadratic adaptive-testing gaps

[TCS-6736](../../data/cards/TCS-6736.json) · Property testing and distribution learning · **medium confidence** · Quantitative refinement

Nearly quadratic adaptive-versus-nonadaptive testing gaps seek a particular separation scale. General adaptivity characterizations and stronger model-power barriers take priority.

Saved sources: Introduction to Property Testing (April 2017 manuscript).

### 282. TCS-6772 — Resolution variable-space complexity in PSPACE

[TCS-6772](../../data/cards/TCS-6772.json) · Proof complexity · **medium confidence** · Quantitative refinement

A PSPACE upper bound for deciding resolution variable-space requirements sharpens recognition complexity for one of several proof-memory measures. Principal proof-space and automatability barriers take priority.

Saved sources: Pebble Games, Proof Complexity, and Time-Space Trade-offs.

### 283. TCS-6782 — Pair capacity of linear-size additive spanners

[TCS-6782](../../data/cards/TCS-6782.json) · Algorithms & data structures · **medium confidence** · Quantitative refinement

Maximum supported pair count for linear-size constant-additive spanners is a further parameter slice of the size-versus-distance tradeoff. The main all-pairs and spanner-versus-emulator barriers give broader coverage.

Saved sources: Graph spanners: a tutorial review.

### 284. TCS-6783 — Four-additive spanners with O(n^(4/3)) edges

[TCS-6783](../../data/cards/TCS-6783.json) · Algorithms & data structures · **medium confidence** · Quantitative refinement

Exactly +4 additive error and n^(4/3) edges form a single precise point of the spanner tradeoff. Main spanner-size and spanner-versus-emulator questions give broader coverage.

Saved sources: Graph spanners: a tutorial review.

### 285. TCS-6833 — Asymptotically optimal nonparametric bandit policies

[TCS-6833](../../data/cards/TCS-6833.json) · Online algorithms · **medium confidence** · Quantitative refinement

Leading-constant asymptotic optimality for further nonparametric reward classes sharpens rate-level robust bandit results. General finite-time exploration and heavy-tail learning limits have broader coverage.

Saved sources: Bandit Algorithms.

### 286. TCS-6875 — Two-sided Ramanujan signings

[TCS-6875](../../data/cards/TCS-6875.json) · Structural graph theory · **medium confidence** · Specific construction or family

Two-sided Ramanujan signings and two-lifts demand one particular family-building mechanism. General existence and efficient explicit construction of Ramanujan graphs take priority; no one-sided theorem is treated as resolving this target.

Saved sources: Expander Graphs and Their Applications.

### 287. TCS-6912 — Permanent lower bounds from learning

[TCS-6912](../../data/cards/TCS-6912.json) · Algebraic computation · **medium confidence** · Specific method or reduction

Deriving permanent lower bounds from arithmetic learning is a particular algorithms-to-hardness implication. Prefer the lower-bound targets and the more general identity-testing connections before this extra route.

Saved sources: Arithmetic Circuits: A Survey of Recent Results and Open Questions.

### 288. TCS-6952 — Unconditional space-restricted 3SUM lower bounds

[TCS-6952](../../data/cards/TCS-6952.json) · Fine-grained complexity · **medium confidence** · Additional model or representation

Strong lower bounds for suitably space-restricted 3SUM add a restricted-resource direction beyond the main unrestricted hypothesis. Its saved motivation does not pick an independently consequential tradeoff.

Saved sources: On Some Fine-Grained Questions in Algorithms and Complexity.

### 289. TCS-6985 — Complexity of polycyclic conjugacy search

[TCS-6985](../../data/cards/TCS-6985.json) · Algebraic computation · **medium confidence** · Additional model or representation

Polycyclic conjugacy search is motivated by a particular family of nonabelian cryptographic platforms; its saved rationale is less general than the retained foundational cryptographic assumptions and group decision barriers.

Saved sources: Aspects of Nonabelian Group Based Cryptography: A Survey and Open Problems.

### 290. TCS-7087 — Polynomial-space conversion from incremental to polynomial delay

[TCS-7087](../../data/cards/TCS-7087.json) · Counting and enumeration · **medium confidence** · Specific method or reduction

Smoothing an unknown incremental-delay bound in polynomial space is a particular simulation task with an extra lack-of-advice condition. Retain the principal enumeration time-space and delay-class comparisons.

Saved sources: Enumeration Complexity: Incremental Time, Delay and Space.

### 291. TCS-7088 — Strong polynomial-delay lower bounds for DNF enumeration

[TCS-7088](../../data/cards/TCS-7088.json) · Counting and enumeration · **medium confidence** · Specialized target

A strong-delay lower bound specifically for DNF-model enumeration is one proposed witness for refined delay limitations. The broader strong-versus-ordinary delay question remains available.

Saved sources: Enumeration Complexity: Incremental Time, Delay and Space.

### 292. TCS-7126 — Complexity of two-sided distributive unification with constants

[TCS-7126](../../data/cards/TCS-7126.json) · Automated reasoning and unification · **medium confidence** · Quantitative refinement

Tight complexity for two-sided distributive unification with constants adds a signature-specific refinement beside the more basic decidability questions for distributive unification.

Saved sources: Unification Theory.

### 293. TCS-7127 — Enumeration complexity under bag semantics

[TCS-7127](../../data/cards/TCS-7127.json) · Database theory and finite model theory · **medium confidence** · Unselected bundle of directions

Bag multiplicities and aggregate-query enumeration combine several output semantics and query extensions. The saved direction has no independently selected central barrier beyond this specialist enumeration programme.

Saved sources: Constant Delay Enumeration for Conjunctive Queries.

### 294. TCS-7129 — Prime implicates versus DNNF succinctness

[TCS-7129](../../data/cards/TCS-7129.json) · Computational complexity · **medium confidence** · Additional model or representation

Prime-implicate descriptions versus polynomial-size DNNF form one particular entry of the compilation succinctness map. The main decomposition and closure barriers provide broader coverage than this extra representation pair.

Saved sources: A Knowledge Compilation Map.

### 295. TCS-7130 — Prime implicates versus d-DNNF succinctness

[TCS-7130](../../data/cards/TCS-7130.json) · Computational complexity · **medium confidence** · Additional model or representation

Prime-implicate descriptions versus deterministic DNNF add a second closely related comparison from the same compilation map. This is a distinct stronger question, but has lower marginal priority in the smaller pool.

Saved sources: A Knowledge Compilation Map.

### 296. TCS-7131 — Prime implicants versus d-DNNF succinctness

[TCS-7131](../../data/cards/TCS-7131.json) · Computational complexity · **medium confidence** · Additional model or representation

Compiling complete prime-implicant lists into deterministic DNNF is another specific representation comparison. It should not displace broader questions about determinism, decomposability and complement closure.

Saved sources: A Knowledge Compilation Map.

### 297. TCS-7201 — Ordinal MMS guarantee for goods

[TCS-7201](../../data/cards/TCS-7201.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Quantitative refinement

The exact ordinal MMS denominator adds a second quantitative relaxation of the same goods-allocation fairness programme. Prefer the principal MMS guarantee and EFX barriers in the reduced pool.

Saved sources: Envy-free matchings in bipartite graphs and their applications to fair division; Wikipedia: Maximin share; Wikipedia revision used for discovery; Improving Approximation Guarantees for Maximin Share; Simultaneous Ordinal Maximin Share and Envy-Based Guarantees.

### 298. TCS-7202 — Envy-free proportional cake cutting with free disposal

[TCS-7202](../../data/cards/TCS-7202.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Additional model or representation

Sharp query complexity after allowing disposal is an additional cake-cutting convention beside the retained complete exactly envy-free allocation target; its distinct resource-relaxation question is lower priority for this batch.

Saved sources: A discrete and bounded envy-free cake cutting protocol for any number of agents; Wikipedia: List of unsolved problems in fair division; Wikipedia revision used for discovery; Waste Makes Haste: Bounded Time Protocols for Envy-Free Cake Cutting with Free Disposal; Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting.

### 299. TCS-7204 — Minimum cuts for finite envy-free cake-cutting protocols

[TCS-7204](../../data/cards/TCS-7204.json) · Algorithmic game theory, mechanism design and fair division · **medium confidence** · Quantitative refinement

The minimum final-cut count of finite envy-free protocols optimizes fragmentation separately from query cost. This is a meaningful geometric resource, but an additional quantitative cake-cutting frontier beside the main complete-allocation target.

Saved sources: Envy-free cake divisions cannot be found by finite protocols; Wikipedia: List of unsolved problems in fair division; Wikipedia revision used for discovery; Envy-Free Cake Divisions Cannot Be Found by Finite Protocols; A Discrete and Bounded Envy-Free Cake Cutting Protocol for Any Number of Agents; Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting; Exact Cut Complexity of Equal-Length Proportional Cake Cutting.

### 300. TCS-7269 — Exponential multilinear-formula lower bounds for the permanent

[TCS-7269](../../data/cards/TCS-7269.json) · Algebraic computation · **medium confidence** · Quantitative refinement

Upgrading the existing multilinear-formula permanent separation to an exponential bound is substantial, but remains a quantitative strengthening in a restricted model alongside broader unresolved formula and circuit separations.

Saved sources: P=?NP.

