# Working summaries — large categories

404 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computational complexity (68)

### TCS-0001 — P versus NP

P versus NP asks whether every problem with efficiently checkable solutions also has an efficient deterministic decision algorithm. Boolean satisfiability is a representative test case because all NP problems reduce to it. Checking one assignment is easy, while deciding whether any assignment works requires accounting for all possibilities. The target concerns worst-case polynomial time on arbitrarily large inputs. A resolution would establish a fundamental relationship between searching and verifying, without by itself determining practical exponents or average-case difficulty.

[Read in atlas](index.html#TCS-0001) · [The P versus NP Problem](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Algebrization: A New Barrier in Complexity Theory](https://www.scottaaronson.com/papers/alg.pdf) · [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [P vs NP — Millennium Prize Problem](https://www.claymath.org/millennium/p-vs-np/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6530 — P versus PSPACE

Polynomial space permits a computation to reuse its memory while exploring potentially enormous collections of possibilities. The question asks whether every problem solvable with that memory budget is also solvable in polynomial time. Truth of quantified Boolean formulas supplies a concrete complete problem. Alternating existential and universal choices describe strategies that can be much larger than one ordinary certificate. The project tests whether repeated reuse of a modest workspace gives strictly more decision power than any polynomial-time computation.

[Read in atlas](index.html#TCS-6530) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Alternation](https://doi.org/10.1145/322234.322243) · [\(\mathrm{IP} = \mathrm{PSPACE}\)](https://doi.org/10.1145/146585.146609) · [Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779v1) · [Some Recent Developments in Space Complexity](https://doi.org/10.4230/LIPIcs.MFCS.2026.3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6531 — L versus P

Logarithmic-space computation can retain only a few input indices and counters while repeatedly rereading the input. The question asks whether that memory always suffices for every polynomial-time decision problem. Evaluating a supplied Boolean circuit is a representative complete task. Shared dependencies make naive recomputation expensive, while storing all intermediate gate values exceeds the space budget. The project tests whether efficient computation fundamentally needs substantial working memory or can always reorganize its information into an extremely small state.

[Read in atlas](index.html#TCS-6531) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Limits to Parallel Computation: P-Completeness Theory](https://homes.cs.washington.edu/~ruzzo/papers/limits.pdf) · [Undirected Connectivity in Log-Space](https://omereingold.wordpress.com/wp-content/uploads/2014/10/sl.pdf) · [Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779v1) · [Logarithmic Space](https://cs.uwaterloo.ca/~eblais/cs365/w26/L-and-NL)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6535 — Nonuniform \(\mathrm{TC}^{0}\) versus \(\mathrm{NC}^{1}\)

TC0 circuits use a constant number of layers of powerful majority gates. NC1 circuits use logarithmically many layers of ordinary bounded-input Boolean gates. The question asks whether the former nonuniform class is strictly weaker than the latter. Many arithmetic tasks already fit in TC0, so their familiar sequential implementations do not provide separating examples. The project seeks a function whose nested logical dependencies cannot be compressed into a fixed-depth network even when each gate can aggregate many inputs at once.

[Read in atlas](index.html#TCS-6535) · [Bootstrapping Results for Threshold Circuits “Just Beyond” Known Lower Bounds](https://eccc.weizmann.ac.il/report/2018/199/) · [Uniform constant-depth threshold circuits for division and iterated multiplication](https://doi.org/10.1016/S0022-0000(02)00025-9) · [Characterizing \(\mathrm{NC}^{1}\) with Typed Monoids](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.26) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6534 — Berman–Hartmanis conjecture

Polynomial-time reductions show that NP-complete problems can simulate each other, but may erase information. The Berman-Hartmanis conjecture asks whether every pair instead admits a polynomial-time computable bijection with a polynomial-time inverse. That bijection must preserve yes and no instances across the entire string space. Padding provides evidence for familiar complete problems without covering all possible complete languages. The project asks whether completeness forces one efficiently reversible organization of instances, reaching beyond ordinary mutual reducibility.

[Read in atlas](index.html#TCS-6534) · [On Isomorphisms and Density of NP and Other Complete Sets](https://epubs.siam.org/doi/10.1137/0206023) · [The ismorphism conjecture fails relative to a random oracle](https://doi.org/10.1145/73007.73022) · [The Isomorphism Conjecture Holds Relative to an Oracle](https://epubs.siam.org/doi/10.1137/S0097539793248305) · [Reductions in Circuit Complexity: An Isomorphism Theorem and a Gap Theorem](https://www.cse.iitk.ac.in/users/manindra/isomorphism/non-uniform-ac0-iso.pdf) · [One-Way Functions and the Isomorphism Conjecture](https://eccc.weizmann.ac.il/report/2009/019/) · [Open Problems by or Inspired by Juris Hartmanis](https://www.cs.umd.edu/~gasarch/open/juris.pdf) · [The Isomorphism Conjecture for NP](https://cse.iitk.ac.in/users/manindra/survey/Isomorphism-Conjecture.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6532 — Strictness of the polynomial hierarchy

The polynomial hierarchy classifies decision languages by a fixed number of alternating existential and universal blocks. Each block chooses polynomially many bits, followed by a uniform polynomial-time check. The question asks whether every added block strictly increases the class of expressible languages. Equality of any neighboring levels would make the entire hierarchy stabilize at a finite level. Known oracle separations and conditional collapses reveal consequences and barriers while leaving this unrelativized conjecture unresolved.

[Read in atlas](index.html#TCS-6532) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [The Polynomial-Time Hierarchy](https://research.ibm.com/publications/the-polynomial-time-hierarchy) · [The Polynomial Hierarchy, Random Oracles, and Boolean Circuits](https://www.cs.columbia.edu/~rocco/Public/sigact15.pdf) · [An Average-Case Depth Hierarchy Theorem for Boolean Circuits](https://arxiv.org/abs/1504.03398) · [Upper and Lower Bounds for the Linear Ordering Principle](https://eccc.weizmann.ac.il/report/2025/142/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0021 — NP versus P/poly

A nonuniform Boolean circuit family may choose a completely different circuit for each input length without any computable construction rule. The question asks whether one fixed language in NP nevertheless exceeds every polynomial bound on the number of Boolean gates. The card specifies the verifier model, exact circuit evaluation and the required arbitrarily large violating lengths. Counting arguments produce hard truth tables but do not by themselves supply the required polynomially verifiable language. Karp–Lipton, natural proofs and newer restricted-circuit lower bounds explain the surrounding landscape while leaving the full NP versus P/poly target unresolved.

[Read in atlas](index.html#TCS-0021) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Natural Proofs](https://doi.org/10.1006/jcss.1997.1494) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0002 — NP versus coNP

NP asks for short efficiently checkable evidence that an input is a yes instance. coNP describes the corresponding evidence for no instances of NP problems. The concrete target asks whether every unsatisfiable CNF formula has a polynomial-length certificate accepted by one fixed sound verifier. The verifier may use any proof format, and the question does not require efficiently finding a certificate. Separating the classes requires excluding all such verifiers, beyond lower bounds for individual proof systems.

[Read in atlas](index.html#TCS-0002) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Circuits, Communication, and Proofs](https://www.icts.res.in/program/ccp)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0015 — Superlinear Boolean circuit lower bounds

The question asks for a polynomial-time computable function with as many output bits as input bits that needs more than linear circuit size. Competing circuits may use every two-input Boolean operation and share intermediate work without depth or fan-out restrictions. The lower-bound ratio must be unbounded at arbitrarily large input lengths, not necessarily tend to infinity at every length. Known explicit full-basis lower bounds improve fixed linear constants, and recent conditional barriers apply only to specified proof classes. A complete answer must prove or refute the existence of one uniformly computable function satisfying the entire claim.

[Read in atlas](index.html#TCS-0015) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [\(3.1n-o(n)\) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://eccc.weizmann.ac.il/report/2025/033/) · [Convergent Gate Elimination and Constructive Circuit Lower Bounds](https://arxiv.org/abs/2602.17942) · [A Note on Natural-Proofs for Super-Linear Lower Bounds for Linear Functions](https://eccc.weizmann.ac.il/report/2026/008/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0016 — Exponential circuit lower bounds for 3-SAT

The question asks whether n-variable 3-SAT requires Boolean circuits of size at least two to a positive constant times n at every sufficiently large n. Inputs are complete incidence vectors for all clauses of width at most three, giving Theta(n cubed) input bits. The circuit model permits every two-input Boolean gate, arbitrary sharing and independent nonuniform designs at each length. Known restricted-circuit lower bounds and randomized exponential-time improvements do not settle this unrestricted lower-bound target. A complete answer must prove the eventual exponential bound or its exact quantified negation in Lean.

[Read in atlas](index.html#TCS-0016) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Which Problems Have Strongly Exponential Complexity?](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturiZane_2001_jcss.pdf) · [\(3.1n-o(n)\) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7158 — PH versus PSPACE

Does every polynomial-space decision problem lie in the polynomial hierarchy? PH allows a fixed number of alternating quantifier blocks for each language. PSPACE also describes polynomial-time alternation with no fixed bound on the number of alternations. Equality would put TQBF in one finite level and hence collapse PH to that level. Completeness and oracle results illuminate the distinction without settling the ordinary class equality.

[Read in atlas](index.html#TCS-7158) · [Computational Complexity: A Modern Approach (Internet draft)](https://theory.cs.princeton.edu/complexity/book.pdf) · [Completeness in the Polynomial Hierarchy and PSPACE for many natural problems derived from NP](https://arxiv.org/abs/2602.12350) · [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](https://arxiv.org/abs/2602.02294)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7161 — NEXP versus nonuniform \(\mathrm{TC}^{0}\)

Does some NEXP language escape all polynomial-size constant-depth majority circuits? Majority gates make this circuit class substantially more powerful than constant-depth \(\mathrm{AND}/\mathrm{OR}\) circuits. Williams established the corresponding separation for ACC circuits with fixed-modulus gates. Recent threshold-circuit bounds still restrict depth or polynomial size and use different hard-language classes. The target requires one ordinary NEXP language outside the entire nonuniform class \(\mathrm{TC}^{0}\).

[Read in atlas](index.html#TCS-7161) · [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/) · [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/) · [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/)
Existing status: `open` · Summary written: 2026-09-11

### TCS-4786 — Minimum Circuit Size Problem

The Minimum Circuit Size Problem asks whether a complete Boolean truth table can be computed by a circuit below a given size threshold. The card fixes AND, OR and NOT gates, counts all gates, and measures input length by the full truth table. The target is NP-completeness under uniform deterministic polynomial-time many-one reductions. Known results for restricted proof systems, conditional quasipolynomial reductions and implicit representations do not settle that target. A complete answer must prove or refute the existence of a SAT reduction with exactly these guarantees.

[Read in atlas](index.html#TCS-4786) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2023.31) · [Simple Circuit Extensions for XOR in PTIME](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.23) · [Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31) · [NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf) · [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6533 — NL versus UL

NL permits many accepting computation branches while using only logarithmic workspace. UL requires exactly one accepting branch on a yes input and none on a no input. The question asks whether one uniform unambiguous small-space machine can decide reachability in every directed graph. Known general simulations need more workspace or extra resources, while recent lower bounds and algorithms concern restricted models or graph families. The uniqueness guarantee concerns the machine’s computations, not a promise that the input graph already has a unique path.

[Read in atlas](index.html#TCS-6533) · [Making Nondeterminism Unambiguous](https://people.cs.rutgers.edu/~allender/papers/nlul.pdf) · [Derandomizing Isolation in Space-Bounded Settings](https://pages.cs.wisc.edu/~dieter/Papers/r-ul-sicomp.pdf) · [When Connectivity Is Hard, Random Walks Are Easy With Non-Determinism](https://eccc.weizmann.ac.il/report/2025/077/download) · [Using Hardness vs Randomness to Design Low-Space Algorithms](https://eccc.weizmann.ac.il/report/2026/045/) · [Derandomizing Isolation In Catalytic Logspace](https://arxiv.org/abs/2512.09374v3) · [Deterministic, Oblivious Isolation for Space-Bounded Computation Requires Large Weights](https://eccc.weizmann.ac.il/report/2026/124/) · [Space Complexity of Reachability in Simple Path Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.87)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0004 — L versus NL

Directed reachability asks whether a path follows the arrows from a specified source to a target. Nondeterministic logarithmic space can recognize it, and the problem captures the whole class NL. The target is one always-correct deterministic algorithm with only logarithmic writable memory on every explicit input. Savitch’s larger-space simulation and Reingold’s undirected algorithm do not settle this directed logarithmic-space target. A solution requires either a uniform algorithm with all resource guarantees or a lower bound excluding every eligible deterministic decider.

[Read in atlas](index.html#TCS-0004) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Relationships between nondeterministic and deterministic tape complexities](https://doi.org/10.1016/S0022-0000(70)80006-X) · [Nondeterministic Space is Closed under Complementation](https://doi.org/10.1137/0217058) · [Undirected Connectivity in Log-Space](https://omereingold.wordpress.com/wp-content/uploads/2014/10/sl.pdf) · [When Connectivity Is Hard, Random Walks Are Easy with Non-determinism](https://doi.org/10.1145/3717823.3718303) · [Reachability in graphs having linear 2-arboricity two is NL-hard](https://doi.org/10.1016/j.ipl.2025.106611)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4988 — Existence of TFNP-complete problems

TFNP contains search problems with polynomially bounded, efficiently verifiable answers guaranteed to exist for every binary input. The question asks whether one problem in this class is complete for all the others under deterministic polynomial-time many-one search reductions. Each reduction makes one transformed instance and must decode every valid returned answer correctly. The complete relation is fixed universally, while the reduction and its polynomial bounds may vary with the source problem. Known subclass completeness and oracle results clarify the structure without settling this general existence question.

[Read in atlas](index.html#TCS-4988) · [An Oracle with no UP-Complete Sets, but \(\mathrm{NP}=\mathrm{PSPACE}\)](https://doi.org/10.4230/LIPIcs.MFCS.2024.50) · [Incompleteness in the finite domain](https://users.math.cas.cz/~pudlak/inco.pdf) · [Hierarchies within TFNP: building blocks and collapses](https://eccc.weizmann.ac.il/report/2025/123/revision/1/download/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6977 — Ruling out quasilinear-time SAT without a space restriction

SAT asks whether an explicitly written Boolean formula has a satisfying assignment. The target excludes every deterministic running time n times a fixed polynomial in log n in a uniform random-access model. There is no independent restriction on working memory. Known small-space lower bounds and either/or resource alternatives do not establish this time-only statement. The user explicitly selected the quasilinear interpretation of the source’s informal near-linear goal.

[Read in atlas](index.html#TCS-6977) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Time-Space Tradeoffs for Counting NP Solutions Modulo Integers](https://eccc.weizmann.ac.il/report/2007/036/) · [Bounded Relativization](https://eccc.weizmann.ac.il/report/2023/070/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7321 — \(\mathrm P_{\mathbb R}\) versus \(\mathrm{NP}_{\mathbb R}\)

The BSS model computes exactly with arbitrary real inputs using unit-cost arithmetic and comparisons. Each machine has one fixed finite program and finitely many fixed real constants for all input dimensions. The question asks whether polynomial-time verification with real witnesses always yields polynomial-time deterministic decision. Real polynomial feasibility is complete for the nondeterministic class, while Boolean-input PosSLP results concern different restrictions. A complete answer must prove equality or separation in the full model; a claimed separation was withdrawn in July 2026.

[Read in atlas](index.html#TCS-7321) · [A survey on real structural complexity theory](https://www.emis.de/journals/BBMS/Bulletin/bul971/meer.pdf) · [On the Complexity of Numerical Analysis](https://doi.org/10.1137/070697926) · [Some structural complexity results for \(\exists\mathbb R\)](https://arxiv.org/abs/2502.00680) · [Scheme-theoretic Approach to Computational Complexity II. The Separation of P and NP over \(\mathbb C\), \(\mathbb R\), and \(\mathbb Z\)](https://arxiv.org/abs/2107.07387)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7363 — \(\exists\mathbb{R}\) versus \(\mathrm{NP}\)

The existential theory of the reals asks whether a finite system of polynomial conditions has an exact real solution. Its input is a binary formula, with all coefficient and exponent bits counted in the running-time measure. The question is whether every yes-instance has a polynomial-length binary certificate checked in ordinary polynomial time. Known containments, oracle results and real-valued proof systems leave that discrete-certificate question unresolved in the checked sources. A complete answer must establish or refute ETR membership in NP without restricting possible certificate representations.

[Read in atlas](index.html#TCS-7363) · [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006) · [Some structural complexity results for \(\exists\mathbb R\)](https://arxiv.org/abs/2502.00680) · [Beyond Bits: An Introduction to Computation over the Reals](https://arxiv.org/abs/2603.29427) · [Probabilistically checkable proofs for the Existential Theory of the Reals](https://arxiv.org/abs/2605.23517)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6681 — DNF versus d-DNNF succinctness

A DNF formula describes satisfying assignments as a union of conjunctions, whose cases may overlap. The proposal asks whether some polynomial-size DNFs require superpolynomial-size deterministic decomposable circuits for the same Boolean function. Determinism requires disjoint alternatives, while decomposability requires conjunctions to separate their variables. A separation would show that imposing these useful structural restrictions can force an inherent representation-size increase. The question is about the existence of compact equivalent circuits, so hardness of efficiently finding a conversion or a separation for unrestricted DNNFs does not by itself answer this more specific size comparison.

[Read in atlas](index.html#TCS-6681) · [Algorithmic Applications of Knowledge Compilation](https://capelli.me/publi/hdr.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7286 — CLS versus FP

CLS describes total search tasks motivated by continuous local improvement. The source proves that it is exactly the intersection of PPAD and PLS, two classes based on different existence principles. The equivalent discrete question gives one succinct path problem and one succinct local-search problem and asks for a solution to either. The requested algorithm must be deterministic and polynomial in the length of both circuit descriptions. A resolution would determine whether the common part of these two search classes is computationally tractable.

[Read in atlas](index.html#TCS-7286) · [The Complexity of Gradient Descent: CLS = PPAD ∩ PLS](https://arxiv.org/abs/2011.01929)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0020 — Polynomial-size circuits for EXP

EXP contains problems solvable in deterministic exponential time. The question asks whether every such problem could nevertheless have polynomial-size Boolean circuits chosen separately for each input length. The circuits need not be efficiently constructible, making this different from a polynomial-time simulation. Time hierarchy theorems alone do not eliminate that nonuniform possibility. The project seeks a lower bound strong enough to defeat arbitrary length-specific circuit designs for some language with an explicit exponential-time decision procedure.

[Read in atlas](index.html#TCS-0020) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6091 — Exponential depth-three \(\mathrm{AC}^{0}\) lower bounds for E

The question asks for one language decidable in deterministic time exponential in input length but requiring exponential-size depth-three Boolean circuits. The circuits use arbitrary-fan-in AND and OR gates with input negations, sharing and either top-gate orientation. A fixed positive lower-bound exponent must hold at infinitely many lengths for the same E language. There is no uniformity requirement on the competing circuits and no restriction on bottom fan-in or literal polarity. Recent exponential results for monotone circuits with bounded bottom fan-in do not establish this unrestricted lower bound.

[Read in atlas](index.html#TCS-6091) · [NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD Circuits](https://doi.org/10.4230/LIPIcs.CCC.2018.5) · [Optimal Monotone Depth-Three Circuit Lower Bounds for Majority](https://arxiv.org/abs/2601.04072v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6743 — Randomized evasiveness conjecture

A monotone graph property is invariant under vertex renaming and cannot be destroyed by adding edges. The conjecture says every nonconstant such property needs a quadratic number of adjacency queries even with randomized error at most one third. The query bound is worst-case over graphs and random choices, while the error guarantee holds separately for each graph. Zero-error expected-cost lower bounds and the solved quantum analogue concern distinct computational models. A resolution would establish or refute a universal information barrier for randomized exact graph recognition.

[Read in atlas](index.html#TCS-6743) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html) · [Complexity Measures and Decision Tree Complexity: A Survey](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf) · [Instance Complexity and Unlabeled Certificates in the Decision Tree Model](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/instance_complexity.pdf) · [Improved Lower Bounds on the Randomized Complexity of Graph Properties](https://www.cs.dartmouth.edu/~ac/Pubs/rsa-randglb.pdf) · [The Influence Lower Bound Via Query Elimination](https://theoryofcomputing.org/articles/v007a010/v007a010.pdf) · [Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem](https://arxiv.org/abs/2010.12629v1) · [CS 860: Introduction — Graph Properties](https://cs.uwaterloo.ca/~eblais/cs860/w25/intro)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6979 — Independence of P versus NP from ZFC

P versus NP asks whether efficiently verifiable decisions can always be made efficiently. This card fixes the usual arithmetic SAT formulation and asks whether ZFC proves neither it nor its negation. All finite proofs in full ZFC are allowed, without any limit on their length. Restricted-theory results and oracle computations do not settle this specified independence question. A positive answer would establish actual syntactic independence and would therefore also imply consistency of ZFC.

[Read in atlas](index.html#TCS-6979) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf) · [Is P Versus NP Formally Independent?](https://www.scottaaronson.com/papers/indep.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1056 — Majority outside constant-depth modular circuits

Majority returns one when at least half of its input bits are one. ACC⁰ circuits combine Boolean operations and modular-counting gates using constant depth and polynomial size. The question asks whether every fixed choice of modulus and depth fails to compute majority within polynomial size. Known results for prime moduli or additional circuit restrictions do not settle the full composite-modulus question. A separation would show that this shallow modular model cannot express a basic threshold operation efficiently.

[Read in atlas](index.html#TCS-1056) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [Optimal Lower Bounds for Symmetric Modular Circuits](https://arxiv.org/abs/2604.04760)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6747 — Graph nonisomorphism in BPP

Graph nonisomorphism asks whether two graphs have no adjacency-preserving vertex bijection. The target is one randomized polynomial-time algorithm with error at most one third on every encoded input. Because BPP is closed under complement, the same question can be phrased for ordinary graph isomorphism. Interactive proofs, quasipolynomial algorithms and algorithms for restricted graph classes do not provide the required decider. A resolution would clarify whether random computation alone suffices for this central structural comparison problem.

[Read in atlas](index.html#TCS-6747) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/update.html) · [Group, Graphs, Algorithms: The Graph Isomorphism Problem](https://people.cs.uchicago.edu/~laci/papers/icm18-babai.pdf) · [Parameterized complexity of graph isomorphism testing](https://doi.org/10.1016/j.cosrev.2026.100918)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6817 — Directed reachability in polynomial time and polylogarithmic space

The problem asks for directed reachability to be decided simultaneously in polynomial time and polylogarithmic space. One uniform deterministic machine must meet both bounds on every explicitly encoded graph and marked vertex pair. No graph restrictions, randomness, advice or additional catalytic memory are allowed. Separate efficient-time and small-space algorithms do not satisfy the joint requirement. The target is equivalently inclusion of nondeterministic logspace in SC, and is weaker than L equaling NL.

[Read in atlas](index.html#TCS-6817) · [Computational Complexity: A Modern Approach (web draft)](https://theory.cs.princeton.edu/complexity/book.pdf) · [A Sublinear Space, Polynomial Time Algorithm for Directed s-t Connectivity](https://doi.org/10.1137/S0097539793283151) · [Directed st-Connectivity with Few Paths Is in Quantum Logspace](https://doi.org/10.4230/LIPIcs.CCC.2025.18) · [A Space-space Trade-off for Directed st-Connectivity](https://arxiv.org/abs/2602.21088v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0018 — P versus NP intersect coNP

A language in NP intersect coNP has short efficiently checkable certificates for both yes and no instances. The question asks whether some such language still lies outside deterministic polynomial time. Having two kinds of witnesses does not automatically tell an algorithm how to find either one. The separation would identify difficulty independent of the asymmetric certification typical of NP-complete problems. The project explores whether efficiently verifiable certainty on both sides can coexist with an intrinsically hard decision process.

[Read in atlas](index.html#TCS-0018) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1054 — Exponential lower bounds for unrestricted threshold-of-threshold circuits

A threshold gate decides whether a weighted sum of Boolean inputs reaches a specified threshold. This question asks for an NP function family requiring exponentially many gates in every two-layer threshold circuit. All weights are unrestricted real numbers, and size counts gates rather than their weights. The book’s definition of explicitness means a uniform polynomial-time verifier, while known bounds with extra weight restrictions do not settle this target. A resolution would reveal a strong computational limitation of two layers of weighted decisions.

[Read in atlas](index.html#TCS-1054) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [Toward Super-Polynomial Size Lower Bounds for Depth-Two Threshold Circuits](https://arxiv.org/abs/1805.10698)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5593 — Black-Box Hypothesis

The Black-Box Hypothesis compares access to a Boolean circuit’s code with access to its input-output behavior. It concerns total semantic properties that a uniform randomized polynomial-time algorithm decides correctly on every circuit representation. The proposed black-box algorithm receives unary input length and circuit-size bounds and may make adaptive evaluations of the function. Its total running time, including queries, must be polynomial in those bounds with error at most one third on each input. Known restricted-model results and promise-property counterexamples do not settle this general hypothesis.

[Read in atlas](index.html#TCS-5593) · [Does Looking Inside a Circuit Help?](https://doi.org/10.4230/LIPIcs.MFCS.2017.1) · [Black-Box Hypotheses and Lower Bounds](https://doi.org/10.4230/LIPIcs.MFCS.2021.29)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6168 — Does NP-hardness of MCSP imply circuit lower bounds for EXP?

MCSP asks whether a fully listed Boolean function has a small circuit. The question concerns what proving its ordinary NP-hardness would force elsewhere in complexity theory. The proposed consequence is that some exponential-time language requires superpolynomial circuits. Existing consequences separate EXP from smaller intersections or randomized classes and do not yield that circuit lower bound. The target captures a major proposed connection between metacomplexity and nonuniform lower bounds.

[Read in atlas](index.html#TCS-6168) · [On the (Non) NP-Hardness of Computing Circuit Complexity](https://doi.org/10.4230/LIPIcs.CCC.2015.365) · [On the (Non) NP-Hardness of Computing Circuit Complexity](https://theoryofcomputing.org/articles/v013a004/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7159 — Hartmanis–Stearns conjecture

The question concerns a fixed machine that prints all digits of a real number with bounded delay between outputs. Every rational number permits this because its expansion is eventually periodic. The conjecture says that any irrational number generated this quickly must be transcendental. It quantifies over unrestricted deterministic multitape machines, beyond the restricted automata covered by known partial results. A proof would connect the arithmetic nature of numbers to a stringent computation bound and rule out linear-time integer multiplication.

[Read in atlas](index.html#TCS-7159) · [On the computational complexity of algebraic numbers: the Hartmanis–Stearns problem revisited](https://arxiv.org/abs/1601.02771) · [Time-Restricted Sequence Generation](https://people.csail.mit.edu/meyer/time-restricted-sequence-generation-jcss.pdf) · [On Transcendence of Numbers Related to Sturmian and Arnoux-Rauzy Words](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.144) · [Computing the base-b representation of quadratic irrationals using automata](https://doi.org/10.1016/j.tcs.2026.115843)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0298 — UNSAT multi-prover proofs with efficient SAT-oracle provers

The actual source asks for interactive proofs of unsatisfiability, with several noncommunicating classical provers. Honest provers must run in randomized polynomial time with SAT-oracle access, while the verifier is polynomial-time and has no oracle. Soundness must hold against all computationally unbounded classical cheating strategies. The target is tied to checking a purported SAT solver and remains distinct from ordinary interactive proofs with unrestricted honest provers. The imported SAT label lost a complement bar; the card restores UNSAT and records the correction explicitly.

[Read in atlas](index.html#TCS-0298) · [Worlds to Die Harder For: Open Oracle Questions for the 21st Century](https://www.cs.umd.edu/~gasarch/open/oracles.pdf) · [On the Power of Randomized Reductions and the Checkability of SAT](https://www.irif.fr/~dxiao/docs/satcheck.pdf) · [Range avoidance, Arthur-Merlin, and TFNP](https://eccc.weizmann.ac.il/report/2025/210/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0301 — Excluding one-sided randomized quasilinear-time log-space SAT

The input is an arbitrary explicitly written satisfiability instance. A candidate algorithm may use fresh random bits, logarithmic working memory and time n times a fixed polynomial in log n. It must never accept an unsatisfiable formula and must accept each satisfiable formula with constant probability. Both resource bounds hold for the same machine on every sequence of random choices. The target is an unconditional lower bound against every such algorithm; known opposite-error and larger-class results do not settle it.

[Read in atlas](index.html#TCS-0301) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Time-Space Lower Bounds for the Polynomial-Time Hierarchy on Randomized Machines](https://drops.dagstuhl.de/entities/document/10.4230/DagSemProc.06111.20) · [Time-Space Lower Bounds for Simulating Proof Systems with Quantum and Randomized Verifiers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.50)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2215 — Real quantifier alternation versus summation

The question asks whether all fixed levels of alternating real quantification reduce to one strengthened existential theory. That target theory permits nested sums over Boolean dummy variables inside arithmetic terms. Its real variables must remain explicitly listed, and it has no compact product binder. The reductions operate on finite binary descriptions and may have a different polynomial bound for each fixed alternation level. A positive answer would supply the specific counting-versus-alternation principle proposed in the 2024 source, distinct from earlier topological Toda analogues.

[Read in atlas](index.html#TCS-2215) · [The Existential Theory of the Reals with Summation Operators](https://doi.org/10.4230/LIPIcs.ISAAC.2024.13) · [Beyond the Existential Theory of the Reals](https://doi.org/10.1007/s00224-023-10151-x) · [Polynomial Hierarchy, Betti Numbers, and a Real Analogue of Toda’s Theorem](https://arxiv.org/abs/0812.1200v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2333 — Downward self-reducibility of PLS-complete problems

The target asks whether every PLS-complete total search relation can be solved using only shorter instances of itself. Shorter means fewer bits in the full input encoding, and the reduction must work for every valid solution oracle. The original paper proves the property for a canonical complete problem and places downward self-reducible total NP search in PLS. A SODA 2026 result proves that the universal statement holds exactly when every PLS problem is solvable in polynomial time. Its conditional negative result is recorded as progress; the card retains the unconditional yes/no question.

[Read in atlas](index.html#TCS-2333) · [Downward Self-Reducibility in TFNP](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.67) · [Downward self-reducibility in the total function polynomial hierarchy](https://doi.org/10.1137/1.9781611978971.185) · [Downward self-reducibility in the total function polynomial hierarchy — full manuscript](https://eccc.weizmann.ac.il/report/2025/121/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6714 — Nonuniform \(\mathrm{NC}^{1}\) perfect matching

The question asks whether perfect-matching existence in every undirected graph has nonuniform polynomial-size circuits of logarithmic depth. The circuits use binary AND and OR with negation and return only an exact decision bit. This is equivalent to polynomial-size formulas and, under explicit graph transformations, to the matching-threshold question in the original source. Monotone lower bounds and broader polylogarithmic-depth algorithms do not decide the unrestricted NC-one target. The July 2026 bipartite NC result also has a different graph scope and depth guarantee.

[Read in atlas](index.html#TCS-6714) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [The Matching Problem in General Graphs Is in Quasi-NC](https://doi.org/10.1109/FOCS.2017.70) · [Bipartite Matching is in NC](https://eccc.weizmann.ac.il/report/2026/100/revision/2/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7243 — Linear-size circuits for stable ternary compaction

Stable ternary compaction moves every 2 to the end while preserving the order of all zeros and ones. The question asks whether each input length admits an exact Boolean circuit of size proportional to that length. Circuits may have arbitrary depth and fan-out and may compute freely on the fixed two-bit alphabet encoding. Non-stable compaction and ordinary ternary sorting do not retain the binary sequence required in the answer. The checked short-key sorting advances and conditional or restricted lower bounds do not resolve this nonuniform linear-size question.

[Read in atlas](index.html#TCS-7243) · [Linear-size circuits for stable \(0,1<2\) sorting?](https://www.openproblemgarden.org/op/linear_size_circuits_for_stable_0_1_2_sorting) · [Sorting Short Keys in Circuits of Size \(o(n\log n)\)](https://doi.org/10.1137/20M1380983) · [Optimal Sorting Circuits for Short Keys](https://doi.org/10.1137/1.9781611977073.142)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0017 — KRW formula-size conjecture with constant loss

The selected KRW variant asks whether minimum formula size under block composition is always within a constant factor of the product of the two minimum sizes. Both functions can be arbitrary nonconstant Boolean functions, and the inner one is applied to disjoint input blocks. Formulas use binary AND and OR with negation, count variable occurrences, and cannot share intermediate computations. The constant must work for every function and dimension, so dimension-dependent losses do not suffice. The original depth conjecture and recent results for strengthened communication tasks are related but distinct statements.

[Read in atlas](index.html#TCS-0017) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [Super-logarithmic Depth Lower Bounds via the Direct Sum in Communication Complexity](https://doi.org/10.1007/BF01206317) · [Shrinkage under Random Projections, and Cubic Formula Lower Bounds for \(AC^0\)](https://doi.org/10.4086/toc.2023.v019a007) · [Toward Better Depth Lower Bounds: Strong Composition of XOR and a Random Function](https://doi.org/10.4230/LIPIcs.STACS.2025.26)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0297 — A counting characterization of P with NP access

The target asks for one #P counting function whose polynomial-time oracle power is exactly P with an NP oracle. The count is an exact nonnegative integer returned in binary, and oracle queries may be adaptive. The same function must allow SAT decisions while itself being computable using SAT queries. Complete counting can already capture the whole polynomial hierarchy, so choosing a weaker count is a substantive requirement. The question concerns ordinary complexity classes, separately from the source’s request for a relativized counterexample.

[Read in atlas](index.html#TCS-0297) · [Worlds to Die Harder For: Open Oracle Questions for the 21st Century](https://www.cs.umd.edu/~gasarch/open/oracles.pdf) · [A Simple Proof of Toda’s Theorem](https://theoryofcomputing.org/articles/v005a007/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0303 — Improving the log-space SAT time exponent beyond 2 cos(π/7)

The input is a Boolean satisfiability formula measured by its complete binary length. The proposed lower bound applies to deterministic algorithms that use only logarithmic writable memory and can query any input location. The goal is to exclude some time exponent strictly larger than 2 cos(π/7), with the same machine subject to both resource bounds. Known lower bounds approach the threshold from below, and a theorem limits a formalized proof method at that threshold. A refutation must provide algorithms for every larger exponent, possibly different algorithms for different exponents.

[Read in atlas](index.html#TCS-0303) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Time-Space Tradeoffs for Counting NP Solutions Modulo Integers](https://eccc.weizmann.ac.il/report/2007/036/) · [Limits on Alternation Trading Proofs for Time–Space Lower Bounds](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/npProofLimits/paper-journal.pdf) · [Time-Space Lower Bounds for Simulating Proof Systems with Quantum and Randomized Verifiers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.50) · [Bounded Relativization](https://eccc.weizmann.ac.il/report/2023/070/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2532 — NEXP circuit lower bounds from uniform obfuscation

The card asks whether uniformly secure perfectly correct indistinguishability obfuscation implies NEXP is not contained in P/poly. The obfuscator preserves every circuit’s function exactly and hides equivalent equal-size representations from uniform randomized polynomial-time distinguishers. The security definition follows the source and gives distinguishers no auxiliary input or nonuniform advice. The source proves the desired circuit lower bound under stronger nonuniform security and a different uniform-time separation under uniform security. The user selected this precise implication, and a complete answer must establish or refute it without adding hypotheses.

[Read in atlas](index.html#TCS-2532) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2023.31) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6006 — Is ARRIVAL solvable in polynomial time?

ARRIVAL asks which of two destinations is reached by one token following deterministic alternating switches. The graph and both successor choices are explicit, and every vertex can reach at least one sink in the underlying graph. The target is one deterministic polynomial-time decision algorithm, without requiring it to list the token trajectory. General subexponential algorithms and newer bounded-treewidth or ladder results leave that all-instance target open. Short certificates for both outcomes make this a basic unresolved question at the boundary of efficient decision and total search.

[Read in atlas](index.html#TCS-6006) · [A Subexponential Algorithm for ARRIVAL](https://doi.org/10.4230/LIPIcs.ICALP.2021.69) · [ARRIVAL: Recursive Framework & ℓ₁-Contraction](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.95) · [Sinks and Ladders: ARRIVAL and SSG with Two Vertices per Level](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2026.19)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6285 — Closure of UL under complement

UL contains languages decided with logarithmic work space and at most one accepting computation path per input. The question asks whether the complement of every such language also has an unambiguous logarithmic-space decider. The original and complement machines are uniform, exact and have no oracle or nonuniform advice. Ordinary nondeterministic logspace is closed under complement, but its complementing procedures need not preserve unambiguity. A resolution would clarify both the structure of small-space complexity classes and the use of unambiguous subroutines in graph algorithms.

[Read in atlas](index.html#TCS-6285) · [Depth-First Search in Directed Planar Graphs, Revisited](https://doi.org/10.4230/LIPIcs.MFCS.2021.7) · [Nondeterministic Space is Closed under Complementation](https://doi.org/10.1137/0217058) · [Parameterizing the Complexity of Finding Long Paths in DAGs](https://doi.org/10.4230/LIPIcs.MFCS.2026.73)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7256 — Reversible simulation in polynomial time and linear space

The question asks whether every deterministic computation can be compiled into a reversible one with polynomial time overhead and only a constant-factor space increase. The simulator preserves the input and exact output, clears auxiliary storage and retains nontermination on divergent inputs. Time and space are compared on the same input, and input, output and history storage all count. Known general simulations attain the two desired efficiencies separately or with a tradeoff, while catalytic-space results use a different resource model. A complete answer must prove or refute one computable compiler meeting all of these guarantees simultaneously.

[Read in atlas](index.html#TCS-7256) · [Time, Space, and Energy in Reversible Computing](https://homepages.cwi.nl/~paulv/papers/wrc05.pdf) · [Time/Space Trade-Offs for Reversible Computation](https://doi.org/10.1137/0218053) · [Time and Space Bounds for Reversible Simulation](https://arxiv.org/abs/quant-ph/0101133) · [Reversible Space Equals Deterministic Space](https://doi.org/10.1006/jcss.1999.1672) · [Fully Characterizing Lossy Catalytic Computation](https://link.springer.com/article/10.1007/s00453-026-01376-6)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2425 — Closure of SZK under truth-table reductions

The question asks whether statistical zero knowledge is closed under arbitrary polynomial-time nonadaptive truth-table reductions. The reduction prepares all queries first and combines their answers with a polynomial-size Boolean circuit. Promise-violating queries are handled by the source’s explicit gate-by-gate three-valued logic. Closure is known for Boolean formulas and logarithmic-depth circuits, leaving general circuit composition unresolved in the source. The card defines SZK through Statistical Difference and requires a complete proof or counterexample to the full closure statement.

[Read in atlas](index.html#TCS-2425) · [Kolmogorov Complexity Characterizes Statistical Zero Knowledge](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.3) · [A Complete Problem for Statistical Zero Knowledge](https://www.cs.ucla.edu/~sahai/work/web/2003%20Publications/J.ACM2003.pdf) · [Robustness for Space-Bounded Statistical Zero Knowledge](https://doi.org/10.1145/3708508)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3886 — \(\exists\!\cdot\!\mathrm{BPP}\) versus MA

The question asks whether existential quantification over an ordinary BPP language has exactly the power of Merlin–Arthur verification. Both settings use a polynomial-size witness chosen before a uniform randomized polynomial-time check. Existential BPP additionally requires a bounded-error gap for every input-witness pair, even for unsuccessful witnesses on yes-instances. Equality permits changing the verifier, so one verifier with intermediate probabilities is not a counterexample. An oracle separation is known, while the ordinary class equality remains the source’s unresolved target.

[Read in atlas](index.html#TCS-3886) · [Quantum Generalizations of the Polynomial Hierarchy with Applications to QMA(2)](https://doi.org/10.4230/LIPIcs.MFCS.2018.58) · [An Oracle Builder’s Toolkit](https://lance.fortnow.com/papers/files/obt.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4746 — Effective enumeration of BPP

The problem asks for a computable list of randomized polynomial-time algorithms covering every language in BPP. Each listed algorithm must have the required error gap on every input, but the list may repeat languages and omit alternative implementations. The enumerator itself has no efficiency requirement, and the listed programs may have different polynomial time bounds that need not be supplied effectively. Recognizing all bounded-error program codes is a different task from finding a representative family with complete language coverage. Known arithmetical characterizations give useful enumerable subclasses, while a negative answer would separate BPP from deterministic polynomial time.

[Read in atlas](index.html#TCS-4746) · [Enumerating Error Bounded Polytime Algorithms Through Arithmetical Theories](https://doi.org/10.4230/LIPIcs.CSL.2024.10) · [Enumerating Error Bounded Polytime Algorithms Through Arithmetical Theories](https://arxiv.org/abs/2311.15003)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0019 — Polynomial formulas versus linear circuits

The conjecture asks for Boolean functions with linear-size circuits but no polynomial-size formulas. Circuits may reuse intermediate results, while formulas have a tree structure and count repeated variable occurrences separately. The computational basis is binary AND and OR with unary negation, and correctness is exact on every input. The nonuniform separation is equivalent to NC-one being strictly smaller than P/poly, and arbitrarily large violating lengths are sufficient. Known nearly cubic gaps and recent composition results do not yet give the required superpolynomial separation.

[Read in atlas](index.html#TCS-0019) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [Shrinkage under Random Projections, and Cubic Formula Lower Bounds for \(AC^0\)](https://doi.org/10.4086/toc.2023.v019a007) · [Toward Better Depth Lower Bounds: Strong Composition of XOR and a Random Function](https://doi.org/10.4230/LIPIcs.STACS.2025.26) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#conciseness-gap-between-formulae-and-circuits)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3862 — Complete problem for Search-SZK

The question asks whether the authors’ statistical zero-knowledge search class has one complete promise search problem. Protocols output a legal solution with perfect completeness and retain the source’s two soundness conditions. A universal simulator receives one sample of the honest protocol’s output distribution and must reproduce any efficient verifier’s view up to negligible statistical distance. Reductions must preserve yes and no promises and decode every legal target answer into a valid source answer. Completeness is known for the Prefix-SZK subclass, while this card retains the full Search-SZK question selected by the user.

[Read in atlas](index.html#TCS-3862) · [Brief Announcement: Zero-Knowledge Protocols for Search Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2018.105) · [Zero-Knowledge Protocols for Search Problems](https://eprint.iacr.org/2018/437)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6139 — Subexponential derandomization with two-way random-tape access

This question concerns randomized logspace algorithms that can reread a fixed polynomial-length random tape in either direction. It asks whether every language they decide has a uniform exact deterministic algorithm whose worst-case runtime has an exponent sublinear in input length. The deterministic algorithm has no separate space restriction and receives no advice. The source’s simulation for restricted passes with advice and later conditional promise-search results do not provide this algorithm. The formulation explicitly separates persistent randomness from the one-way coin access used in ordinary BPL.

[Read in atlas](index.html#TCS-6139) · [A Note on the Advice Complexity of Multipass Randomized Logspace](https://doi.org/10.4230/LIPIcs.MFCS.2016.31) · [Leakage-Resilient Hardness Equivalence to Logspace Derandomization](https://doi.org/10.4230/LIPIcs.MFCS.2024.83)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6455 — Doubly efficient \(\mathrm{IP}=\mathrm{PSPACE}\)

An interactive proof lets a verifier check a computation through a conversation with one prover. The question asks for a verifier polynomial in input length and an honest prover polynomial in the specified computation time for every polynomial-space decider. The protocol must be uniform across input lengths and must remain sound against arbitrarily powerful cheating strategies. The checked June 2026 theorem covers quasipolynomial computation times, while the card asks for the full time range. A resolution would strengthen IP = PSPACE by controlling proof-generation overhead without replacing information-theoretic soundness with a cryptographic assumption.

[Read in atlas](index.html#TCS-6455) · [Towards a Doubly Efficient \(\mathrm{IP}=\mathrm{PSPACE}\)](https://eccc.weizmann.ac.il/report/2026/102/) · [Doubly-Efficient Interactive Arguments for Bounded-Space from One-Way Functions](https://eccc.weizmann.ac.il/report/2026/111/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7257 — Formula versus circuit noise thresholds

Each gate of a Boolean circuit independently flips its computed output with the same probability. The circuit may reuse noisy intermediate values and may be arbitrarily large. The question asks whether universal reliable computation is possible exactly below the known two-input formula threshold. Reliability requires one positive correctness advantage that works for every Boolean function and input length at the chosen noise level. A resolution would determine whether sharing intermediate computations changes the fundamental tolerance to gate errors.

[Read in atlas](index.html#TCS-7257) · [Noise Threshold for Universality of Two-Input Gates](https://ir.cwi.nl/pub/13657) · [Tight Limits on Nonlocality from Nontrivial Communication Complexity; a.k.a. Reliable Computation with Asymmetric Gate Noise](https://arxiv.org/abs/1809.09748v5) · [Noise Quantification and Control in Circuits via Strong Data-Processing Inequalities](https://arxiv.org/abs/2507.15108v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7260 — Polynomial-size closure of d-DNNF under negation

The question asks whether every d-DNNF has a polynomial-size d-DNNF representing its Boolean complement. One polynomial must bound the size increase for every circuit and every finite variable set. The complement may use entirely different decompositions, provided that decomposability and determinism are retained. No efficient procedure for finding the complement is required in this representational question. The published failure of closure for structured circuits does not settle closure for general d-DNNFs.

[Read in atlas](index.html#TCS-7260) · [List of open questions: PTIME complementation of d-DNNF](https://a3nm.net/work/research/questions/#ptime-complementation-of-d-dnnf) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Structured d-DNNF Is Not Closed under Negation](https://doi.org/10.24963/ijcai.2024/398) · [On the Complexity of Language Membership for Probabilistic Words](https://doi.org/10.4230/LIPIcs.STACS.2026.5)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0305 — Supercubic uniform formula lower bounds for SAT

A De Morgan formula computes with binary AND and OR gates and input negations, without sharing internal computations. Its size counts leaf occurrences, and the target function is SAT on n bits encoding a 3-CNF formula. The source asks whether a fixed positive exponent can raise the required size beyond the cubic scale when the formula family is LOGTIME-uniform. Later NAND depth lower bounds use a different gate basis and cost measure, so they do not directly settle this question. The problem seeks a concrete improvement in uniform formula lower bounds for a central NP-complete language.

[Read in atlas](index.html#TCS-0305) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Towards Stronger Depth Lower Bounds](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.10)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1052 — Depth-three lower bounds beyond the log-depth simulation threshold

The target is an explicit Boolean family requiring extremely large depth-three AND/OR circuits. The required exponent must grow faster than input length divided by its iterated logarithm. Both top-gate orientations, arbitrary sharing and unbounded bottom fan-in are included. Such a lower bound would exclude the joint possibility of linear circuit size and logarithmic depth for that family. Recent stronger-looking bounds impose additional circuit restrictions or assumptions and do not answer this question.

[Read in atlas](index.html#TCS-1052) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [Optimal Monotone Depth-Three Circuit Lower Bounds for Majority](https://arxiv.org/abs/2601.04072) · [Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank Under NSETH and Beyond](https://eccc.weizmann.ac.il/report/2025/038/revision/3/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1053 — Depth-three circuit lower bounds beyond the square-root exponent

The question asks for an explicit family that is harder for depth-three AND/OR circuits than the known square-root exponent scale. The circuits have top OR gates, allow negated inputs and unrestricted fan-in, and may share gates. Explicitness means a single polynomial-time verifier with polynomial-length certificates, following the book. The exponent must improve by an unbounded factor, so increasing a fixed coefficient does not suffice. Recent exponential bounds in more restricted depth-three models leave this general frontier unresolved.

[Read in atlas](index.html#TCS-1053) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [Optimal Monotone Depth-Three Circuit Lower Bounds for Majority](https://arxiv.org/abs/2601.04072) · [Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank Under NSETH and Beyond](https://eccc.weizmann.ac.il/report/2025/038/revision/3/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-2029 — FBPP versus negligible-error FBPP

The question compares two error requirements for randomized algorithms that may return any valid answer to a relation. FBPP here allows a unary precision parameter and running time polynomial in reciprocal error. The negligible-error class instead requires one algorithm with a fixed polynomial time bound and error eventually below every inverse polynomial. Relations may be partial and need not have an effective test for valid answers. The source proves noninclusion in the reverse direction, leaving this inclusion versus incomparability unresolved.

[Read in atlas](index.html#TCS-2029) · [A Qubit, a Coin, and an Advice String Walk into a Relational Problem](https://doi.org/10.4230/LIPIcs.ITCS.2024.1) · [A Qubit, a Coin, and an Advice String Walk Into a Relational Problem](https://arxiv.org/abs/2302.10332)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0293 — Subquadratic deterministic simulation of nondeterministic space

Savitch’s theorem simulates nondeterministic space s with deterministic space \(O(s^{2})\). This card asks whether every at-least-logarithmic space-constructible bound admits an improvement to \(o(s^{2})\). The machine is deterministic and all ordinary working memory is charged, with no restriction on running time. A constant-factor improvement does not suffice, while no fixed polynomial saving is required. A resolution would sharpen the general memory cost of eliminating nondeterminism, including for logarithmic-space computation.

[Read in atlas](index.html#TCS-0293) · [Improving SPACE versus NSPACE via Tree Evaluation, in Computational Complexity of Discrete Problems](https://doi.org/10.4230/DagRep.15.3.56)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1602 — Deterministic query complexity of tournament kings

A king in a tournament reaches every other vertex along a directed path of at most two edges. A deterministic algorithm learns the orientation of one chosen edge per query and must output a king for every tournament. The target is its optimal worst-case query count up to constant factors as the number of vertices grows. The checked deterministic bounds remain \(\Omega(n^{4/3})\) and \(O(n^{3/2})\), whereas randomization permits linear expected query cost. Closing the deterministic gap would quantify how much pairwise information this total search task inherently requires.

[Read in atlas](index.html#TCS-1602) · [Hardness of Finding Kings and Strong Kings](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.36) · [Searching for Sorted Sequences of Kings in Tournaments](https://cis.temple.edu/~wu/research/publications/Publication_files/41005.pdf) · [Randomized and Quantum Query Complexities of Finding a King in a Tournament](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30) · [From Donkeys to Kings in Tournaments](https://doi.org/10.4230/LIPIcs.ESA.2024.3) · [When You Come at the King You Best Not Miss](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.25)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0310 — Polynomial-time weighted falsifiability of unambiguous DNFs

The question asks whether an unambiguous DNF has a falsifying assignment whose additive integer score meets a threshold. Every weight is encoded in binary, and the requested deterministic running time is polynomial in the entire bit representation. Unambiguity makes the satisfying regions disjoint and ordinary falsifiability easy. Unary-weight algorithms and hardness for exact-score equality leave the binary threshold question unsettled in the checked sources. A complete answer must establish or refute polynomial-time decidability with the stated representation and guarantee.

[Read in atlas](index.html#TCS-0310) · [Is this problem on unambiguous DNFs hard?](https://cstheory.stackexchange.com/questions/53733/is-this-problem-on-unambiguous-dnfs-hard) · [Representation, Provenance, and Explanations in Database Theory and Logic (Dagstuhl Seminar 24032)](https://doi.org/10.4230/DagRep.14.1.49) · [List of open questions: Weighted falsifiability for unambiguous DNFs](https://a3nm.net/work/research/questions/#weighted-falsifiability-for-unambiguous-dnfs)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1035 — Cost of restricting linear circuits to depth two

The problem asks how much more expensive a matrix transformation can become when its circuit is restricted to two addition layers. It compares the minimum wire count at depth two with the unrestricted minimum for the same matrix and operation. Boolean OR, ordinary addition and addition modulo two have separate extremal penalty functions. A 2017 result already gives a polynomial penalty for XOR, resolving a narrower earlier question. The remaining target is the optimal asymptotic order of each penalty, with upper and lower bounds matching within constants.

[Read in atlas](index.html#TCS-1035) · [Complexity of Linear Boolean Operators](https://doi.org/10.1561/0400000063) · [Solution of Problem 7.7](https://web.vu.lt/mif/s.jukna/Knizka/problem-7.7.html)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1040 — Nonlinear-gate advantages for binary linear operators

The problem asks whether nonlinear intermediate computation can save an unbounded number of wires when the final output map is linear over the two-element field. The comparison is between XOR-only circuits and circuits with arbitrary Boolean gate functions. Both have unrestricted depth and fan-in and must compute the same map exactly on every input. Correctness only on basis vectors and results restricted to shallow circuits do not answer this question. A positive answer establishes arbitrarily large savings, while a negative answer gives one simulation factor for every matrix.

[Read in atlas](index.html#TCS-1040) · [Complexity of Linear Boolean Operators](https://doi.org/10.1561/0400000063) · [Lower Bounds for Linear Operators](https://arxiv.org/abs/2509.02730)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1034 — Largest separation between SUM and OR circuits

The problem asks for the largest circuit-size advantage of Boolean OR over ordinary nonnegative addition on the same zero-one matrix. Both models must compute all output sums exactly and are charged for wires. The card asks separately for unrestricted depth and for exactly two addition layers. Known constructions show growing gaps, but agreement of separate worst-case matrix complexities does not settle these ratios. The answer must determine both extremal growth rates with matching constant-factor bounds.

[Read in atlas](index.html#TCS-1034) · [Complexity of Linear Boolean Operators](https://doi.org/10.1561/0400000063) · [Separating OR, SUM, and XOR Circuits](https://doi.org/10.1016/j.jcss.2016.01.001)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1036 — Unbounded XOR-over-OR complexity separations

The question asks whether some zero-one matrices are arbitrarily more costly to evaluate with XOR gates than with OR gates. Cost is the minimum number of wires, and both circuits may have unrestricted depth. The same coefficient matrix specifies parity outputs in one model and union outputs in the other. Known shallow-circuit gaps and hardness of rewriting representations do not establish this unrestricted size separation. A proof needs arbitrarily large ratios, while a refutation needs one universal constant bound.

[Read in atlas](index.html#TCS-1036) · [Complexity of Linear Boolean Operators](https://doi.org/10.1561/0400000063) · [Separating OR, SUM, and XOR Circuits](https://doi.org/10.1016/j.jcss.2016.01.001)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-2681 — UEOPL versus EOPL

EOPL describes total search along succinct paths with potentials. UEOPL admits additional answers witnessing failures of uniqueness. The question asks whether both ordinary circuit-defined classes nevertheless have the same power. A published theorem separates them in the black-box model, which does not decide this equality. Resolving it would clarify the computational role of uniqueness in total search.

[Read in atlas](index.html#TCS-2681) · [Further Collapses in TFNP](https://doi.org/10.4230/LIPIcs.CCC.2022.33) · [Unique End of Potential Line](https://doi.org/10.1016/j.jcss.2020.05.007) · [Separations in Proof Complexity and TFNP](https://doi.org/10.1145/3663758)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6934 — Unconditional exclusion of linear-time CNF satisfiability

CNF satisfiability asks whether an assignment makes every listed clause true. The input measure counts every written literal, identifier bit and delimiter. The selected question asks whether a deterministic multitape Turing machine can always decide it in linear time. No separate workspace restriction or conjectural hardness assumption is allowed. This precise modest milestone is distinguished from exponential lower bounds and from lower bounds for other computation models.

[Read in atlas](index.html#TCS-6934) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/) · [Time-space lower bounds for satisfiability](https://doi.org/10.1145/1101821.1101822) · [Simulating Time with Square-Root Space](https://doi.org/10.1145/3798104)
Existing status: `source_open` · Summary written: 2026-09-13

## Algorithms (27)

### TCS-6537 — Expected linear-time integer sorting for every word length

Integer sorting can inspect the bits of keys instead of treating them only as objects to compare. The question asks for one always-correct randomized word-RAM algorithm taking expected linear time for every permitted word length. The constant must remain uniform when keys occupy much more than logarithmically many bits. Ordinary radix sorting handles smaller universes but its number of passes can grow. This tests whether powerful word operations can completely remove the asymptotic overhead of ordering an arbitrary list of machine words.

[Read in atlas](index.html#TCS-6537) · [Integer sorting in \(O(n\sqrt{\log  \log  n})\) expected time and linear space](https://doi.org/10.1109/SFCS.2002.1181890) · [Deterministic sorting in \(O(n \log  \log  n)\) time and linear space](https://www.sciencedirect.com/science/article/pii/S019667740300155X) · [Expected Linear Time Sorting for Word Size \(\Omega (\log ^{2} n \log  \log  n)\)](https://cs.au.dk/~gerth/papers/swat14sort.pdf) · [Integer models of computation and integer sorting](https://www.cs.cmu.edu/~15451-s25/slides/lecture03.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0388 — Sorting \(X + Y\)

Given two lists of n numbers, form every sum consisting of one number from each list. The task is to sort these quadratically many sums as quickly as possible. They have substantial inherited order, so they are not an arbitrary collection of unrelated values. The source distinguishes having few comparisons from implementing those comparisons with equally small total running time. Removing avoidable overhead would improve both structured sorting and geometric problems whose events are ordered by pairwise sums.

[Read in atlas](index.html#TCS-0388) · [The Open Problems Project](https://topp.openproblem.net/p41)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0946 — Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges

A hypergraph cut counts the total weight of hyperedges meeting both sides of a vertex partition. A cut sparsifier replaces the hypergraph by a smaller weighted hypergraph that approximately preserves every cut at once. The question asks whether O(n/epsilon squared) hyperedges always suffice for multiplicative error epsilon. This matches the natural target from ordinary graphs, while a hyperedge can involve arbitrarily many vertices. The size measure counts hyperedges rather than their total incidence size, making the project specifically about how many distinct multiway interactions must be retained.

[Read in atlas](index.html#TCS-0946) · [Problem 91: Cut-Sparsification of Hypergraphs](https://sublinear.info/index.php?title=Open_Problems:91)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1141 — Near-linear-time approximation of reachability diameter

Reachability diameter is the largest finite shortest-path distance in an unweighted directed graph. Ignoring unreachable pairs makes this statistic informative even when directions are disconnected. The question asks for one randomized algorithm that gives a constant-factor estimate on every graph in near-linear worst-case time. Known additive and polynomial-factor approximations, special graph classes and conditional small-factor barriers leave this target unresolved in the cited source. A complete Lean proof must establish the universal algorithmic guarantee or rule it out in the stated model.

[Read in atlas](index.html#TCS-1141) · [Revisiting Diameter in Directed Graphs](https://doi.org/10.4230/LIPIcs.ESA.2026.59) · [Revisiting Diameter in Directed Graphs](https://arxiv.org/abs/2606.08217v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7350 — Near-linear output-sensitive Subset Sum

The input is an explicit list of positive integers, allowing repetitions, together with an integer threshold. The task is to list every distinct attainable subset sum at most that threshold exactly once, including zero. The question asks for one uniform randomized word-RAM algorithm whose time on every random execution is near-linear in input size plus output size and whose whole output is correct with probability at least two thirds. Known output-sensitive improvements and their 2026 derandomization do not attain this endpoint, which would avoid paying for a large unused numerical range. A complete Lean answer must prove such an algorithm and its guarantees exist or prove their full logical negation in the specified model.

[Read in atlas](index.html#TCS-7350) · [Top-k-Convolution and the Quest for Near-Linear Output-Sensitive Subset Sum](https://arxiv.org/abs/2107.13206v2) · [Beating Bellman's Algorithm for Subset Sum](https://arxiv.org/abs/2410.21942v1) · [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5705 — Small Implicit Graph Conjecture

An adjacency labeling scheme assigns each vertex a short binary string from which adjacency can be determined using only two labels. The conjecture asks for logarithmic labels in every hereditary class with at most a factorial times a fixed exponential number of labeled graphs. Hereditary means closed under induced subgraphs, and is weaker than closure under all subgraphs. The monotone case is known, and a 2025 follow-up proves logarithmic-cubed labels for all hereditary small classes. The question isolates when low total information content permits efficient storage in locally decodable vertex descriptions.

[Read in atlas](index.html#TCS-5705) · [Tight Bounds on Adjacency Labels for Monotone Graph Classes](https://doi.org/10.4230/LIPIcs.ICALP.2024.31) · [Adjacency Labeling Schemes for Small Classes](https://doi.org/10.4230/LIPIcs.ITCS.2025.21)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6783 — Optimal size of four-additive graph spanners

An additive spanner keeps original graph edges while limiting the increase in every pairwise distance. This card fixes the increase to at most four and asks for the optimal worst-case number of edges. The target is the complete asymptotic function up to universal constant factors. The familiar candidate is \(n^{4/3}\), while recent constructions still have exponent \(7/5\) up to logarithmic factors. This gap is a fundamental unresolved regime of distance compression, and the variable-error linear-size tradeoff has its own card.

[Read in atlas](index.html#TCS-6783) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152) · [Finding 4-Additive Spanners: Faster, Stronger, and Simpler](https://arxiv.org/abs/2510.17262) · [The \(4/3\) Additive Spanner Exponent is Tight](https://arxiv.org/abs/1511.00700)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3346 — Quasipolynomial dependence on vertices for hypergraph isomorphism

Hypergraph isomorphism asks whether a relabeling of vertices makes two explicitly listed set systems identical. The target running time is quasipolynomial in the number of vertices and polynomial in the full input size. The exponent on input size must be a fixed constant even when many hyperedges are listed. The source explains why a quasipolynomial bound in the larger incidence representation does not automatically provide this guarantee. A resolution would extend efficient symmetry testing to rich set systems over comparatively small universes.

[Read in atlas](index.html#TCS-3346) · [Graph Isomorphism in Quasipolynomial Time Parameterized by Treewidth](https://doi.org/10.4230/LIPIcs.ICALP.2020.103)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5969 — Complexity of planar 3-edge-colorability

Three-edge-colorability asks whether the edges of a graph can receive three colors with different colors on every pair meeting at a vertex. The selected question asks for the computational complexity of this decision problem on planar graphs. The source studies a sufficient route through augmentation to a planar cubic bridgeless supergraph, where three-edge-colorability follows from the Four-Color Theorem. It also discusses a conjectured characterization for two-connected planar graphs of maximum degree three. A full classification would determine whether the remaining planar cases admit an efficient coloring test or conceal an NP-hard obstruction.

[Read in atlas](index.html#TCS-5969) · [Efficient Recognition of Subgraphs of Planar Cubic Bridgeless Graphs](https://doi.org/10.4230/LIPIcs.ESA.2022.62)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1617 — Planarity dichotomy for induced subdivision detection

For a fixed graph H, induced-subdivision detection asks whether an input graph contains a subdivided copy of H as an induced subgraph. Extra edges between selected vertices are forbidden. The conjecture concerns patterns H of maximum degree three and predicts tractability exactly for planar patterns, assuming P differs from NP. Existing algorithms and hardness constructions motivate the proposed boundary. This would classify a natural family of pattern-detection problems by a geometric property of the fixed pattern itself.

[Read in atlas](index.html#TCS-1617) · [Induced Disjoint Paths Without an Induced Minor](https://doi.org/10.4230/LIPIcs.ICALP.2025.4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6421 — Isomorphism dichotomy for finitely forbidden hereditary classes

Hereditary graph classes can be specified by finitely many forbidden induced subgraphs. The question asks whether graph isomorphism on such a class can have complexity intermediate between polynomial time and general graph-isomorphism completeness. The source establishes broad classifications and resolves most two-forbidden-pattern cases. Results for forbidden ordinary subgraphs do not immediately extend to induced exclusions. The project seeks a dichotomy explaining whether a finite structural prohibition always makes isomorphism substantially easier or leaves its full general difficulty intact.

[Read in atlas](index.html#TCS-6421) · [Towards an Isomorphism Dichotomy for Hereditary Graph Classes](https://doi.org/10.4230/LIPIcs.STACS.2015.689)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-2018 — Quadratic-size submodular hypergraph sparsifiers

A submodular hypergraph assigns each hyperedge a flexible submodular cost for being split by a cut. A sparsifier retains and reweights hyperedges so that every cut value remains approximately correct. The conjecture proposes a quadratic-in-vertices size bound with inverse-squared accuracy dependence in the source's size measure. Preserving exponentially many cuts simultaneously is the main obstacle identified there. The project seeks a compression theorem extending beyond ordinary all-or-nothing hyperedge cuts to richer models used in optimization and learning.

[Read in atlas](index.html#TCS-2018) · [Cut Sparsification and Succinct Representation of Submodular Hypergraphs](https://doi.org/10.4230/LIPIcs.ICALP.2024.97)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6173 — Three disjoint directed shortest paths

The input specifies three source-target pairs in a directed graph with positive arc lengths. Each selected path must be shortest for its own pair in the original graph, and no vertex may belong to two paths. The question asks for a deterministic algorithm polynomial in the full binary input length. A 2026 paper improves randomized two-pair algorithms but explicitly leaves three pairs unresolved. A resolution would explain whether several individually optimal directed routes can be selected efficiently while avoiding all conflicts.

[Read in atlas](index.html#TCS-6173) · [A Local-To-Global Theorem for Congested Shortest Paths](https://doi.org/10.4230/LIPIcs.ESA.2023.8) · [Efficient Algorithms for the Disjoint Shortest Paths Problem and Its Extensions](https://doi.org/10.4230/LIPIcs.ITCS.2026.39)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6785 — Optimal additive error of linear-size spanners

A linear-size spanner retains only a constant number of edges per vertex on average. For arbitrary graphs, this severe sparsity budget can force shortest paths to become longer. The source asks for the smallest additive error that can always be guaranteed under that budget. The error may grow with graph size, unlike a fixed additive approximation target. The project seeks matching constructions and lower bounds describing the exact amount of metric accuracy necessarily lost when a graph is compressed to linear edge count.

[Read in atlas](index.html#TCS-6785) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7146 — Polynomial-time detection of fixed pivot- and vertex-minors

The target is to detect a fixed graph after specified local graph transformations and vertex deletions. Vertex-minors permit local complementation, while pivot-minors permit the more restricted edge-pivot operation. The host graph is arbitrary and the target’s vertices may be placed anywhere. For each fixed target and relation, one deterministic algorithm must run in polynomial time in host size. The question does not require a common polynomial exponent or a uniform algorithm for all target sizes.

[Read in atlas](index.html#TCS-7146) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800) · [Vertex-minors of graphs: A survey](https://doi.org/10.1016/j.dam.2024.03.011)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7075 — Complexity of general vertex-connectivity augmentation

Vertex-connectivity measures how many vertex deletions a graph can withstand before disconnecting. The problem asks for the fewest unit-cost edges that raise this connectivity to an input target. Every missing edge is available, and the target may grow with the graph. Known one-increment algorithms and 2026 parameterized progress do not provide polynomial time for every target. A resolution would clarify the complexity of optimal vertex-failure resilience in the simplest unrestricted augmentation model.

[Read in atlas](index.html#TCS-7075) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867) · [Connectivity augmentation is fixed-parameter tractable](https://arxiv.org/abs/2605.11757)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7061 — A dichotomy for edge deletion with finitely many forbidden induced subgraphs

The target graph property is specified by a fixed finite list of forbidden induced subgraphs. An instance asks whether deleting at most a supplied number of edges can achieve that property. The question is whether every such fixed-family problem is polynomial-time solvable or NP-complete. The finite-list domain is an explicit specialization of the survey’s broader hereditary-class research direction. A complete dichotomy must cover every finite forbidden family, rather than only single forbidden graphs or parameterized variants.

[Read in atlas](index.html#TCS-7061) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867) · [A survey of parameterized algorithms and the complexity of edge modification](https://doi.org/10.1016/j.cosrev.2023.100556)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7351 — Linear-time exact inversion counting

An inversion is a pair of permutation positions whose values appear in decreasing order. The task is to return the exact total number of such pairs as one integer. The question asks whether one deterministic program can do this in linear worst-case time on a word RAM with logarithmic words. Known approximation and adaptive algorithms do not provide that exact guarantee for every permutation. A STOC 2025 result links faster exact inversion counting to faster packed Dictionary Matching, giving the question broader algorithmic significance.

[Read in atlas](index.html#TCS-7351) · [Counting Inversions, Offline Orthogonal Range Counting, and Related Problems](https://tmc.web.engr.illinois.edu/inv_7_7_09.pdf) · [Counting Inversions Adaptively](https://arxiv.org/abs/1503.01192) · [On the Hardness Hierarchy for the \(O(n\sqrt{\log n})\) Complexity in the Word RAM](https://arxiv.org/abs/2503.21049)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0538 — Near-linear constant-factor minimum-degree spanning trees

The input is one connected graph, and the output is a spanning tree with small maximum degree. The source asks whether a universal constant approximation can be constructed in near-linear time. This is a static algorithmic question, despite its inherited placement among dynamic graph problems. A July 2026 preprint states a stronger deterministic guarantee that would settle the target. The card records that reported resolution and the exact model while keeping independent proof verification separate.

[Read in atlas](index.html#TCS-0538) · [Graph Algorithms: Distributed Meets Dynamic (Dagstuhl Seminar 24471)](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume14/issue11/24471/DagRep.14.11.92/DagRep.14.11.92.pdf) · [Additive One Approximation for Minimum Degree Spanning Tree: Breaking the O(mn) Time Barrier](https://doi.org/10.1145/3798129.3800832) · [Minimum Degree Spanning Tree: \((1+\varepsilon,1)\)-Approximation in Near-Linear Time](https://arxiv.org/abs/2607.11413v1) · [Research publications](https://www.ermiyafr.com/)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-0809 — Strongly polynomial planar minimum-cost flow

Minimum-cost flow assigns capacity-respecting arc flows that meet prescribed supplies and minimize total cost. The question asks for an asymptotic improvement over the quadratic-times-logarithmic bound on planar graphs. The algorithm must be strongly polynomial, so numerical magnitudes cannot enter its arithmetic-operation bound. A later nearly linear algorithm for polynomially bounded integer data does not by itself meet that requirement. A resolution would show whether planar structure yields a faster exact algorithm independently of the size of the input numbers.

[Read in atlas](index.html#TCS-0809) · [Algorithms for Optimization Problems in Planar Graphs: Mincost flow in planar graphs](https://doi.org/10.4230/DagRep.3.10.36) · [Nested Dissection Meets IPMs: Planar Min-Cost Flow in Nearly-Linear Time](https://arxiv.org/abs/2205.01562)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-1338 — Set-system sparsifiers of size proportional to chain length

A sparsifier retains and reweights a few coordinates while approximately preserving every set’s total weight. The conjecture asks for a support bound proportional to chain length divided by \(\varepsilon ^{2}\). Chain length is measured through the union-closure, so even an incomparable collection of singleton sets can have large chain length. The published upper bound has extra logarithmic factors, which are precisely the remaining loss in the question. A resolution would establish whether this structural parameter completely controls multiplicative sparsification up to a universal constant.

[Read in atlas](index.html#TCS-1338) · [Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction](https://doi.org/10.4230/LIPIcs.ICALP.2026.44)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-2822 — Complexity of directed detours

The input is an unweighted directed graph with specified endpoints. The problem asks whether any simple path between them is longer than their shortest-path distance. Only one extra edge is required, and no path may repeat a vertex. Planar graphs have polynomial algorithms, but the general directed classification remains open in the checked sources. The NP-completeness of exceeding graph diameter concerns a different problem.

[Read in atlas](index.html#TCS-2822) · [Detours in Directed Graphs](https://doi.org/10.4230/LIPIcs.STACS.2022.29) · [Detours in directed graphs — journal version](https://doi.org/10.1016/j.jcss.2023.05.001) · [Simpler and faster algorithms for detours in planar digraphs](https://arxiv.org/abs/2301.02421)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3263 — Polynomial-time minimum-total-length disjoint paths for fixed k

The graph is undirected and unweighted, with a fixed number k of prescribed terminal pairs. The task is to find vertex-disjoint routes with the smallest possible total number of edges, or report that routing is impossible. Individual routes may need to be longer than their own shortest paths to avoid the others. The source asks for polynomial time at every fixed \(k\ge 3\), allowing the exponent to depend on k. Recent grid and individually-shortest-path results do not settle the general problem, which a 2025 published paper still lists as open for three pairs.

[Read in atlas](index.html#TCS-3263) · [Using a Geometric Lens to Find k Disjoint Shortest Paths](https://doi.org/10.4230/LIPIcs.ICALP.2021.26) · [Packing Short Cycles](https://doi.org/10.1145/3765285) · [Shortest Disjoint Paths on a Grid](https://doi.org/10.1137/1.9781611977912.14) · [Planar Disjoint Shortest Paths is Fixed-Parameter Tractable](https://arxiv.org/abs/2505.03353)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-4417 — Linear-time directed bottleneck paths and trees

A bottleneck path minimizes its heaviest edge, and a rooted bottleneck tree minimizes the heaviest edge needed to reach all vertices. The open target is expected linear total time for exact solutions on arbitrary directed graphs using only comparisons of edge weights. The source already achieves a very slowly growing overhead and gives linear time in the stronger word-RAM model. The path and tree targets are equivalent at the expected-linear scale through the source reductions. An August 2026 preprint corrects a related graphical-games claim and continues to state the comparison-based path question as open.

[Read in atlas](index.html#TCS-4417) · [Bottleneck Paths and Trees and Deterministic Graphical Games](https://doi.org/10.4230/LIPIcs.STACS.2016.27) · [Bottleneck Paths Reduce to Deterministic Graphical Games and a Counterexample to a Claimed Linear-Time Algorithm](https://arxiv.org/abs/2608.04279)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6251 — Polynomial-time independent set under a forbidden forest

Fix a forest whose components are paths or subdivided three-leaf claws. Given a graph with no induced copy of that forest, find an independent vertex set of maximum total weight. The question asks for polynomial time for every fixed forbidden forest, with the polynomial allowed to depend on that forest. The input graph may have arbitrarily large degree, cliques and bicliques. Quasipolynomial algorithms now cover the whole family, but known general results still fall short of polynomial time.

[Read in atlas](index.html#TCS-6251) · [Max Weight Independent Set in Graphs with No Long Claws: An Analog of the Gyárfás' Path Argument](https://doi.org/10.4230/LIPIcs.ICALP.2022.93) · [Maximum Weight Independent Set in Graphs with no Long Claws in Quasi-Polynomial Time](https://doi.org/10.1145/3618260.3649791) · [Graphs with No Long Claws: An Improved Bound for the Analog of the Gyárfás’ Path Argument](https://doi.org/10.4230/LIPIcs.MFCS.2025.28)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6270 — Near-linear-query reconstruction of bounded-degree graphs

All vertices of a connected bounded-degree graph are known, but its edges are hidden. One query returns only the shortest-path distance between two named vertices. The goal is to recover every edge using a linear number of vertices times polylogarithmically many expected queries. The expectation is over the algorithm’s randomness for each fixed graph, and the returned answer must be exact. Near-linear results for random regular or bounded-treelength graphs do not cover every graph in the question.

[Read in atlas](index.html#TCS-6270) · [A Simple Algorithm for Graph Reconstruction](https://doi.org/10.4230/LIPIcs.ESA.2021.68) · [Cutwidth Versus BFS-Width with Applications to Graph Reconstruction from Distance Queries](https://doi.org/10.4230/LIPIcs.SWAT.2026.24) · [Reconstructing Bounded Treelength Graphs with Linearithmic Shortest Path Distance Queries](https://arxiv.org/abs/2603.10432)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6784 — Spanners matching Thorup–Zwick emulator tradeoffs

A spanner keeps a subset of the original graph’s edges while approximately preserving all distances. An emulator may instead use weighted shortcut edges. The question asks whether spanners can match the precise size and sublinear distance-error tradeoffs of Thorup–Zwick emulators. A later construction gets arbitrarily close in the edge exponent, but its constants depend on the remaining slack. The target requires the exact exponent and fixed error constants at every fixed level of the hierarchy.

[Read in atlas](index.html#TCS-6784) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152) · [Spanners and emulators with sublinear distance errors](https://researchprofiles.ku.dk/en/publications/spanners-and-emulators-with-sublinear-distance-errors/) · [A Hierarchy of Lower Bounds for Sublinear Additive Spanners](https://doi.org/10.1137/16M1105815) · [Almost-Optimal Sublinear Additive Spanners](https://doi.org/10.1137/23M1581078)
Existing status: `open` · Summary written: 2026-09-12

## Automata and formal languages (31)

### TCS-6558 — Maximum reset threshold of synchronizing automata

A reset word drives a finite automaton to one common state regardless of its initial state. The target is the maximum shortest reset-word length among all complete synchronizing n-state automata. A real-valued approximation with Lean-certified absolute error at most 0.01 for every n meets the benchmark criterion. The Černý conjecture proposes the formula \((n- 1)^{2}\). Arbitrary finite alphabets are permitted, and no endpoint, connectivity or algorithmic restriction is added.

[Read in atlas](index.html#TCS-6558) · [Synchronizing Automata: Open Problems](https://arxiv.org/abs/2608.24245) · [Synchronization of finite automata](https://doi.org/10.4213/rm10005e) · [List of Results on the Černý Conjecture and Reset Thresholds for Synchronizing Automata](https://arxiv.org/abs/2508.15655) · [Improving the Upper Bound on the Length of the Shortest Reset Word](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2018.56) · [An Improvement to a Recent Upper Bound for Synchronizing Words of Finite Automata](https://doi.org/10.25596/jalc-2019-367) · [The Černý Conjecture for One-Cluster Automata via Annular Spectral Descent](https://arxiv.org/abs/2607.19675)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6560 — Sakoda–Sipser problem

Two-way finite automata can reread their input by moving their head in either direction. This project asks whether every n-state nondeterministic machine has an equivalent deterministic two-way machine with polynomially many states. Both machines must agree on all finite words, with no restriction on input length. Rereading sometimes replaces exponentially much one-way memory, but that observation does not supply a general simulation. Resolving the question would quantify how much finite-state succinctness comes from nondeterministic choice once unrestricted revisiting of the input is available.

[Read in atlas](index.html#TCS-6560) · [Nondeterminism and the size of two way finite automata](https://doi.org/10.1145/800133.804357) · [Two-Way Finite Automata: Old and Recent Results](https://arxiv.org/abs/1208.2755) · [Two-way automata versus logarithmic space](https://www.andrew.cmu.edu/user/cak/reads/2014-TOCS/main.pdf) · [Two-Way Automata and Bounded Languages](https://air.unimi.it/handle/2434/1183476) · [Polynomial Complementation of Nondeterministic Two-Way Finite Automata by 1-Limited Automata](https://doi.org/10.4230/LIPIcs.STACS.2026.48)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6559 — Generalized star-height problem

Generalized regular expressions describe regular languages using concatenation, Boolean operations and arbitrary finite repetition. Their star height counts nested repetitions while allowing complementation without an additional height charge. The question asks for a language whose every such description needs at least two nested stars. Ordinary examples with complicated repetitions may simplify drastically when complements are allowed, so inspecting one expression proves little. Establishing a separation beyond height one would reveal a further intrinsic layer of repetition complexity within regular languages.

[Read in atlas](index.html#TCS-6559) · [The star-height problem](https://www.irif.fr/~jep/Problemes/starheight.html) · [Some results on the generalized star-height problem](https://hal.science/hal-00019978) · [On the star-height of factor counting languages and their relationship to Rees zero-matrix semigroups](https://arxiv.org/abs/1603.06236) · [Classes of languages generated by the Kleene star of a word](https://wrap.warwick.ac.uk/id/eprint/104953/) · [Data Compression Meets Automata Theory](https://bulletin.eatcs.org/index.php/beatcs/article/view/824)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6561 — Decidability of every level of the dot-depth hierarchy

The dot-depth hierarchy sorts star-free regular languages by how repeatedly concatenation and Boolean operations must be combined. Given a finite automaton and a fixed level, the project asks whether membership in that level can always be decided. The relevant level concerns the simplest possible description of the language, rather than the syntax initially supplied. Deciding star-freeness only establishes membership somewhere in the hierarchy and does not identify a prescribed level. An effective test for every level would connect automaton behavior to precise bounds on logical descriptive complexity.

[Read in atlas](index.html#TCS-6561) · [Dot-depth three, return of the J-class](https://arxiv.org/abs/2401.16195) · [Generic Results for Concatenation Hierarchies](https://arxiv.org/abs/1710.04313) · [Separation for dot-depth two](https://lmcs.episciences.org/8489) · [The Alternation Hierarchy of First-Order Logic on Words is Decidable — withdrawn](https://arxiv.org/abs/2501.14899v2) · [In Orbit with MeSCaL: Higher in Concatenation and Navigational Hierarchies of Regular Languages](https://www.labri.fr/perso/zeitoun/research/pdf/pzmescal2.pdf) · [A Family of Effective Methods for Decompiling Canonical Acceptors, Instantiated for Languages of Dot-Depth One and Tier-Based Extensions](https://aclanthology.org/2026.scil-main.3/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6563 — Equivalence of deterministic macro tree transducers

Deterministic macro tree transducers are recursive programs that turn finite ordered trees into other trees. Parameters carry intermediate output pieces, which rules may pass onward or duplicate during processing. The project asks whether two such programs define exactly the same partial transformation on every finite input tree. Testing examples can reveal a disagreement but cannot certify universal agreement without a completeness argument. A general decision procedure would provide an exact equivalence test for an expressive model of structured-data transformation, including cases with very large outputs.

[Read in atlas](index.html#TCS-6563) · [Deciding origin equivalence of weakly self-nesting macro tree transducers](https://doi.org/10.1016/j.ipl.2022.106332) · [Equivalence Problems for Tree Transducers: A Brief Survey](https://arxiv.org/abs/1405.5597) · [Equivalence of Deterministic Top-Down Tree-to-String Transducers is Decidable](https://arxiv.org/abs/1503.09163) · [Shape Preserving Tree Transducers](https://arxiv.org/abs/2506.22047) · [The structure of polynomial growth for tree automata/transducers and MSO set queries](https://arxiv.org/abs/2501.10270v4) · [Tree transducers of linear size-to-height increase (and the additive conjunction of linear logic)](https://arxiv.org/abs/2605.03928)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6582 — Equivalence of deterministic higher-order recursion schemes

A deterministic higher-order recursion scheme is a finite typed system of recursive rules that generates a possibly infinite ordered constructor tree. The question asks for one terminating algorithm deciding equality of the complete value trees of any two such schemes. The input orders are arbitrary finite numbers, and equality includes divergence leaves while ignoring internal unfolding steps. Order-one equivalence is decidable, but conditional logical reductions and recent results for other higher-order models do not settle this unrestricted target. A resolution would establish the boundary of exact behavioral comparison for higher-order recursive tree generators.

[Read in atlas](index.html#TCS-6582) · [Collapsible Pushdown Automata and Recursion Schemes](https://www.cs.rhul.ac.uk/home/uxac009/files/papers/tocl17.pdf) · [Higher-Order Recursion Schemes and Collapsible Pushdown Automata: Logical Properties](https://arxiv.org/abs/2010.06366v2) · [Reducing Higher-order Recursion Scheme Equivalence to Coinductive Higher-order Constrained Horn Clauses](https://arxiv.org/abs/2109.04632) · [Polyregular equivalence is undecidable in higher-order types](https://arxiv.org/abs/2604.11935) · [On Higher-Order Probabilistic Verification via the Weighted Relational Model of Linear Logic](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.34)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6564 — First-order definability of regular tree languages

Can one decide whether a regular language of finite ordered trees has a first-order definition? The automaton is finite input, while the sought sentence must describe its language on trees of every finite size. The logic can inspect labels, descendants and sibling order but cannot quantify over sets of nodes. Known fragment tests and separate necessary or sufficient algebraic conditions leave the full decision problem unresolved. Recent infinite-tree and restricted temporal-logic characterizations do not establish this finite ordered-tree test.

[Read in atlas](index.html#TCS-6564) · [Tree Languages Defined in First-Order Logic with One Quantifier Alternation](https://lmcs.episciences.org/699) · [Some Remarks on First-Order Definable Tree Languages](https://arxiv.org/abs/2407.01169) · [An Automaton-based Characterisation of First-Order Logic over Infinite Trees](https://arxiv.org/abs/2509.14090) · [Deciding the Common Fragment of CTL with past and LTL](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.29)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0164 — Decidability of equivalence for unambiguous context-free grammars

An unambiguous context-free grammar has at most one parse tree for every generated word. Two such grammars are given with the promise of unambiguity. The task is to decide whether they generate exactly the same finite words. No deterministic-pushdown or regular-language restriction is imposed. The question asks for a terminating decision procedure without any prescribed complexity bound.

[Read in atlas](index.html#TCS-0164) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#equivalence-of-unambiguous-context-free-grammars)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7309 — Decidability with two parametric clocks and arbitrarily many integer parameters

A discrete-time parametric timed automaton compares integer-valued clocks with constants and with unknown nonnegative integer parameters. The question asks whether some fixed assignment of all parameters allows a finite run to a designated target location. Only two clocks may be compared with parameters, but both the number of parameters and the number of other clocks are unrestricted. The one-parameter case is EXPSPACE-complete, while nearby real-time infinite-word results do not settle this arbitrary-parameter reachability question. A resolution would close the central two-parametric-clock gap between known decidable and undecidable timing models.

[Read in atlas](index.html#TCS-7309) · [Reachability in Two-Parametric Timed Automata with one Parameter is EXPSPACE-Complete](https://link.springer.com/article/10.1007/s00224-023-10121-3) · [Reachability in Two-Parametric Timed Automata with One Parameter Is EXPSPACE-Complete](https://drops.dagstuhl.de/storage/00lipics/lipics-vol187-stacs2021/LIPIcs.STACS.2021.36/LIPIcs.STACS.2021.36.pdf) · [On Decidability Timed Automata with 2 Parametric Clocks](https://arxiv.org/abs/2503.04374v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5959 — Complexity of the Game of Life limit set

The limit set of Conway’s Game of Life contains the configurations that have predecessor histories of every finite length. The question asks whether recognizing finite patterns occurring in that set is complete for the co-computably-enumerable languages. The pattern is finite, but its surroundings are arbitrary configurations of the infinite plane and are not required to be blank. The source proves polynomial-space hardness and nonsoficity, neither of which settles the stronger computability-theoretic completeness target. A resolution would determine whether this canonical cellular automaton attains the general complexity upper bound for limit-set pattern languages.

[Read in atlas](index.html#TCS-5959) · [What Can Oracles Teach Us About the Ultimate Fate of Life?](https://doi.org/10.4230/LIPIcs.ICALP.2022.131)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3863 — Containment of finitely ambiguous probabilistic automata

Two probabilistic automata assign acceptance probabilities to every finite input word. Each machine has a fixed finite bound on its positive accepting runs, but either bound can be greater than one. The question asks for an unconditional terminating test of whether the first probability never exceeds the second. Existing results with an unambiguous side do not settle the general case, and allowing linearly growing ambiguity already gives undecidability. The benchmark requires a Lean-checked decidability or undecidability proof for exact comparison without a gap promise.

[Read in atlas](index.html#TCS-3863) · [When is Containment Decidable for Probabilistic Automata?](https://doi.org/10.4230/LIPIcs.ICALP.2018.121) · [When are emptiness and containment decidable for probabilistic automata?](https://doi.org/10.1016/j.jcss.2021.01.006)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5651 — Recognizing good-for-games and good-for-MDP automata

Good-for-games automata admit one online deterministic resolution that accepts every word in their language. Good-for-MDP automata preserve optimal acceptance probabilities when composed with every finite Markov decision process. The project asks matching complexity classifications for GFG parity recognition with unbounded priority count and GFM Büchi recognition. The checked gaps are NP-hardness versus PSPACE and PSPACE-hardness versus EXPTIME, respectively. Closing these gaps would identify the cost of certifying that compact specifications support adversarial or probabilistic composition.

[Read in atlas](index.html#TCS-5651) · [Word Automata with Limited Nondeterminism (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2026.3) · [Deciding What Is Good-For-MDPs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol279-concur2023/LIPIcs.CONCUR.2023.35/LIPIcs.CONCUR.2023.35.pdf) · [The 2-Token Theorem: Recognising History-Deterministic Parity Automata Efficiently](https://arxiv.org/abs/2503.24244) · [History-Deterministic Parity Automata: Games, Complexity, and the 2-Token Theorem](https://arxiv.org/abs/2501.12302)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5904 — Equivalence of discounted-sum automata

A discounted-sum automaton assigns a convergent weighted value to each infinite run, with later weights geometrically discounted. Its value on an infinite word is the supremum over all runs carrying that word. The question asks for exact decidability of equality of two such functions for every input rational discount factor shared by the automata. Known results for constant functions, reciprocal-integer factors, finite words and transition-dependent discounting have different scopes. A resolution would determine whether arbitrary nondeterministic quantitative specifications in this basic model can be compared algorithmically.

[Read in atlas](index.html#TCS-5904) · [Safety and Liveness of Quantitative Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2023.17) · [Discounted-Sum Automata with Real-Valued Discount Factors](https://faculty.runi.ac.il/udiboker/files/RealValuedNDAs.pdf) · [Discounted-Sum Automata with Multiple Discount Factors](https://lmcs.episciences.org/15802/pdf) · [The Target Discounted-Sum Problem](https://faculty.runi.ac.il/udiboker/files/tds.pdf) · [Target Discounted Sum Problem on Markov Chains with Applications to Markov Decision Processes](https://arxiv.org/html/2609.03670v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0167 — Primitive words and context-freeness

A primitive word is nonempty and is not a power of any shorter nonempty word. The language contains all such words over a fixed finite alphabet with at least two symbols. The conjecture says that no context-free grammar generates exactly this language. Grammars may be ambiguous, so unique-parse limitations would not settle the question. A 2026 paper still states this grammar-expressibility question as open.

[Read in atlas](index.html#TCS-0167) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#context-freeness-of-primitive-words) · [On the Complexity of Language Membership for Probabilistic Words](https://doi.org/10.4230/LIPIcs.STACS.2026.5)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7261 — Linear-time minimization of deterministic finite automata

A deterministic finite automaton can be minimized by merging reachable states that accept exactly the same continuation words. The question asks whether every complete automaton over any fixed alphabet of at least two letters can be minimized in deterministic linear worst-case word-RAM time. The output must be an explicit smallest automaton recognizing exactly the original language, and all preprocessing and output work count. Classical algorithms take O(n log n) time, while known logarithmic-factor lower bounds concern partition refinement rather than every algorithm in the stated model. A resolution would determine whether the extra logarithmic cost reflects the general problem or the structure of its classical algorithms.

[Read in atlas](index.html#TCS-7261) · [Minimization of Symbolic Automata](https://cseweb.ucsd.edu/~ldantoni/papers/popl14.pdf) · [Lowerbounds for Bisimulation by Partition Refinement](https://doi.org/10.46298/lmcs-19(2:10)2023) · [Description and analysis of a bottom-up DFA minimization algorithm](https://doi.org/10.1016/j.ipl.2008.01.003)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5863 — Decidability of stochastic resolvability for \(\omega\)-automata

A finite-memory stochastic resolver selects an automaton transition using the current letter, current state and a finite memory state. One resolver must produce an accepting run with probability one for every accepted infinite word fixed independently of its random choices. The question asks separately whether existence of such a resolver is decidable for Büchi and coBüchi automata. Undecidability of verifying a supplied resolver and results for memoryless thresholds below one concern different decision problems. A resolution would determine whether reliable randomized online execution can be recognized from a finite nondeterministic specification.

[Read in atlas](index.html#TCS-5863) · [Resolving Nondeterminism with Randomness](https://doi.org/10.4230/LIPIcs.MFCS.2025.57) · [Resolving Nondeterminism by Chance](https://arxiv.org/abs/2504.10234v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6064 — Two-dimensional cellular-automaton limit sets

A cellular automaton updates every site of an infinite grid using one finite local rule. Its ordinary limit set contains configurations that can occur after arbitrarily many update steps from some initial configurations. The question classifies exactly which two-dimensional subshifts can arise in this way, allowing finitely many transient auxiliary states. The classification is represented by a realizability indicator on the full domain of subshifts, without assuming an effective decision procedure. Results for typical initial states, computational degrees or a different notion of limit set do not determine this exact ordinary-limit-set class.

[Read in atlas](index.html#TCS-6064) · [Construction of \(\mu\)-Limit Sets of Two-dimensional Cellular Automata](https://doi.org/10.4230/LIPIcs.STACS.2015.262) · [Turing degrees of limit sets of cellular automata](https://arxiv.org/abs/1402.3766v1) · [Limit dynamics of elementary cellular automaton 18](https://doi.org/10.1017/etds.2026.10300)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0154 — Separating words problem

The problem measures the smallest deterministic automaton that distinguishes two binary words of equal length. A different automaton may be chosen for each pair and its behavior on other words is unrestricted. The target is the worst-case number of states as a function of the common word length. The original question proposes a logarithmic upper bound, while recent general bounds have a one-third power with logarithmic factors. The benchmark asks for matching constant-factor asymptotics across all pairs, not a random-input guarantee.

[Read in atlas](index.html#TCS-0154) · [Automata Exchange](https://automata.exchange/19.04-separating-words-problem/) · [Separating Words with Automata in the Half-adversarial Case](https://arxiv.org/abs/2608.28385) · [An Elementary Proof of the \(\widetilde O(n^{1/3})\) Bound for Separating Words](https://arxiv.org/abs/2609.08191)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5738 — Recognizable separability of automatic relations

Binary automatic relations are recognized by finite automata reading padded pairs of words synchronously. The question asks whether it is undecidable to separate two such relations by a finite union of products of regular languages. The number of products is existentially chosen with no prescribed upper bound. Fixed-bound separation is already undecidable, but the unrestricted problem remains explicitly open in the checked later thesis. A resolution would clarify when synchronized infinite relations admit effective separation by finitely many independent regular tests.

[Read in atlas](index.html#TCS-5738) · [Separating Automatic Relations](https://doi.org/10.4230/LIPIcs.MFCS.2023.17) · [Homomorphism Problems in Graph Databases and Automatic Structures](https://www.morvan.xyz/thesis/thesis-morvan-2025-05-22.pdf) · [A Dichotomy Theorem for Automatic Structures](https://arxiv.org/html/2602.18238v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0146 — Polynomial-time universality for unambiguous context-free grammars

An unambiguous context-free grammar gives each accepted word a unique parse tree. This card asks whether a deterministic polynomial-time algorithm can test if such a grammar generates every finite word over its alphabet. Unambiguity is promised for the supplied grammar, and the alphabet and complete production rules are part of the input. The checked upper bound uses randomized polynomial time with a PP oracle; it does not yield the unconditional deterministic polynomial-time procedure sought here. The polynomial-time endpoint is an explicit editorial specialization of the source’s broader complexity question, with either answer requiring a Lean-checked proof.

[Read in atlas](index.html#TCS-0146) · [On unambiguous grammars](https://automata.exchange/19.05-on-unambiguous-grammars/) · [On the Complexity of the Universality and Inclusion Problems for Unambiguous Context-Free Grammars](https://doi.org/10.4204/EPTCS.320.2) · [Multiplicity Problems on Algebraic Series and Context-Free Grammars](https://doi.org/10.1109/LICS56636.2023.10175707)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4575 — Decidability of discounted-sum universality over infinite words

The input is a finite nondeterministic automaton whose transitions carry rational discounted costs. Each infinite word receives the minimum cost among its runs, using one rational discount multiplier. The problem asks whether every infinite word has value at most a supplied rational threshold. The chosen run may depend on the entire word, and threshold equality must be decided exactly. Known restricted discount factors and recent finite-word functional results do not supply the general algorithm requested here.

[Read in atlas](index.html#TCS-4575) · [Quantitative Games with Interval Objectives](https://doi.org/10.4230/LIPIcs.FSTTCS.2014.365) · [Determinizing Discounted-Sum Automata](https://doi.org/10.4230/LIPIcs.CSL.2011.82) · [The Target Discounted-Sum Problem](https://arxiv.org/abs/2511.22979)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0135 — Zeroness of rational weighted context-free grammars

A weighted context-free grammar assigns each word the sum of the weights of its parse trees. This card asks whether an algorithm can always decide if that value is zero for every finite word. Production weights are signed rationals, and an explicit normal form ensures every word has only finitely many parses. The challenge is cancellation for each ordered word; results on commuting-variable series and weighted parallel processes address different models. The rational grammar variant is an explicit editorial choice from a broader source agenda, with decidability or undecidability to be proved in Lean.

[Read in atlas](index.html#TCS-0135) · [Unambiguity in Automata Theory — The zeroness problem](https://doi.org/10.4230/DagRep.11.10.57) · [Weighted Basic Parallel Processes and Combinatorial Enumeration](https://doi.org/10.4230/LIPIcs.CONCUR.2024.18) · [Multiplicity Problems on Algebraic Series and Context-Free Grammars](https://doi.org/10.1109/LICS56636.2023.10175707)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-2243 — A \(\mathrm{TC}^{0}/\mathrm{NC}^{1}\) dichotomy for visibly pushdown languages

A visibly pushdown automaton reads finite words whose letters prescribe its stack operations. The target concerns well-matched inputs and nonuniform Boolean circuit families. It asks whether every recognized language is either in constant-depth threshold circuits or complete for logarithmic-depth bounded-fan-in circuits. Hardness uses constant-depth truth-table reductions, and the alternatives may overlap. The source’s partial classification for the weaker class AC0 does not settle this dichotomy.

[Read in atlas](index.html#TCS-2243) · [The \(\mathrm{AC}^{0}\)-Complexity of Visibly Pushdown Languages](https://doi.org/10.4230/LIPIcs.STACS.2024.38)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0136 — Universality of unambiguous register automata over ordered integers

A register automaton reads letters paired with integer data and retains finitely many integer values. Its transitions may compare stored values, input values and named constants, and may guess new values. Unambiguity promises at most one accepting run for every word. The question asks whether one can decide that every finite data word is accepted. Known algorithms over equality or dense rational order do not by themselves settle the selected discrete-integer model.

[Read in atlas](index.html#TCS-0136) · [Unambiguity in Automata Theory (Dagstuhl Seminar 21452)](https://doi.org/10.4230/DagRep.11.10.57) · [New Techniques for Universality in Unambiguous Register Automata](https://doi.org/10.4230/LIPIcs.ICALP.2021.129) · [Orbit-Finite-Dimensional Vector Spaces and Weighted Register Automata](https://arxiv.org/abs/2104.02438)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0138 — Deterministic separability of nondeterministic timed languages

The input is a pair of nondeterministic timed automata describing finite event sequences with real timestamps. The question is whether a terminating algorithm can decide the existence of a deterministic timed separator accepting the first language and rejecting the second. Input automata may use invisible epsilon steps, while the separator has no such steps and may use any finite number of clocks. The known decidability theorem fixes the separator’s clock count and therefore does not answer this unrestricted question. Either a general decision procedure or an undecidability proof must be checked in Lean for the stated timed-word model.

[Read in atlas](index.html#TCS-0138) · [Deterministic separability of nondeterministic timed languages](https://automata.exchange/20.02-deterministic-separability-of-nondeterministic-timed-languages/) · [Timed Games and Deterministic Separability](https://doi.org/10.4230/LIPIcs.ICALP.2020.121)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4677 — Deciding first-order definability of orbit-finite automata

The alphabet consists of infinitely many data values that can only be compared for equality. The deterministic automaton has finitely many kinds of state up to renaming stored data. The target is an algorithm deciding whether a sentence about position order and data equality defines its entire language. The known orbit-finite-monoid characterization applies to a smaller class than the automata in this question. A proposed aperiodicity characterization would need an effective test before it could establish decidability.

[Read in atlas](index.html#TCS-4677) · [Data Monoids](https://doi.org/10.4230/LIPIcs.STACS.2011.105) · [Nominal Monoids](https://doi.org/10.1007/s00224-013-9464-1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3378 — Periodic configurations in low-complexity two-dimensional shifts of finite type

A finite list of local patterns defines all legal colorings of the integer plane. The list is low-complexity when it has at most as many patterns as cells in its finite shape. The question asks whether every nonempty such system admits at least one coloring with a nonzero translation period. Rectangular and convex shapes are covered by the cited theorem, while arbitrary scattered shapes remain the stated target. This asks for one periodic global coloring, rather than requiring every legal coloring to be periodic.

[Read in atlas](index.html#TCS-3378) · [Decidability and Periodicity of Low Complexity Tilings](https://doi.org/10.4230/LIPIcs.STACS.2020.14) · [Do low-complexity aperiodic SFTs exist?](https://siamak.isoperimetric.info/talks/jarkko-problem.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0128 — State complexity of complementing unambiguous automata

An unambiguous finite automaton has at most one accepting run for each word. For a binary alphabet, this card asks for the worst-case number of states in a smallest nondeterministic automaton accepting its complement. The input has at most n states, while the output may be ambiguous and may have multiple initial states. Known binary lower bounds are quasipolynomial and known general upper bounds are exponential; stronger unary results concern a different alphabet. The requested answer gives matching multiplicative constant-factor bounds on the state count, proved in Lean.

[Read in atlas](index.html#TCS-0128) · [Unambiguity in Automata Theory — Better bounds on complementing unambiguous automata](https://doi.org/10.4230/DagRep.11.10.57) · [A Superpolynomial Lower Bound for the Size of Non-Deterministic Complement of an Unambiguous Automaton](https://doi.org/10.4230/LIPIcs.ICALP.2018.138) · [Lower Bounds for Unambiguous Automata via Communication Complexity](https://arxiv.org/abs/2109.09155) · [On complementing unambiguous automata and graphs with many cliques and cocliques](https://doi.org/10.1016/j.ipl.2022.106270) · [Languages given by finite automata over the unary alphabet](https://doi.org/10.1016/j.jcss.2025.103634)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4636 — Does adding modular predicates preserve decidable first-order definability?

The input is a deterministic finite automaton for a regular language of finite words. The base decision problem asks whether some sentence in a fixed first-order fragment defines that language. The enriched fragment may also inspect position and word-length congruences for any finite choice of moduli. The card asks whether base decidability always transfers, using an explicitly specified effective and substitution-closed fragment framework. Known transfer theorems for stronger separation problems or additional local predicates do not directly establish this membership-only implication.

[Read in atlas](index.html#TCS-4636) · [Two-variable first order logic with modular predicates over words](https://doi.org/10.4230/LIPIcs.STACS.2013.329) · [Covering and separation for logical fragments with modular predicates](https://lmcs.episciences.org/5441)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0133 — Unconditional containment of unambiguous probabilistic automata

A probabilistic automaton assigns each finite word an acceptance probability. The left automaton here has at most one positive accepting run per word, while the right one has a fixed finite bound on that number. The task is to decide whether the left probability is at most the right probability for every word, with exact comparison and no numerical gap promise. The known result for this direction assumes Schanuel’s conjecture; the reversed direction already has an unconditional algorithm. An accepted answer proves decidability or undecidability in Lean without retaining the conjectural arithmetic assumption.

[Read in atlas](index.html#TCS-0133) · [Unambiguity in Automata Theory — Stronger versions of inclusion of probabilistic automata](https://doi.org/10.4230/DagRep.11.10.57) · [When are emptiness and containment decidable for probabilistic automata?](https://doi.org/10.1016/j.jcss.2021.01.006)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4659 — Determinacy of Wadge games for Muller tree languages

Two players build infinite labeled trees and compare their membership in two regular tree languages. The second player may delay output but must eventually build a full infinite tree. The question asks whether ZFC proves that one player always has a winning strategy. Muller automata may recognize non-Borel languages, so the Borel theorem alone is insufficient. Known word-game independence and long regular-tree hierarchy constructions do not settle this universal tree question.

[Read in atlas](index.html#TCS-4659) · [The Determinacy of Context-Free Games](https://doi.org/10.4230/LIPIcs.STACS.2012.555) · [The Determinacy of Context-Free Games — journal version](https://doi.org/10.2178/jsl.7804050) · [On the topological complexity of tree languages](https://www.mimuw.edu.pl/~niwinski/Prace/lobo_d.pdf) · [Wadge-Wagner Hierarchy of Regular Tree Languages](https://www.ims.uni-stuttgart.de/events/TTATT2016/proceedings.pdf)
Existing status: `open` · Summary written: 2026-09-12

## Semantics, logic and verification (38)

### TCS-6565 — Positivity problem for linear recurrences

An integer linear recurrence gives a finite rule for generating an infinite sequence. The positivity problem asks whether every term is nonnegative, with the recurrence order included in the input. Computing a long prefix cannot certify the answer because a negative term may appear arbitrarily late. Characteristic roots can combine growth and oscillation, making exact sign control depend on subtle arithmetic relationships. A terminating decision procedure would provide a basic verification tool for linear discrete dynamics, while a negative result would establish limits even in this elementary setting.

[Read in atlas](index.html#TCS-6565) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26abs.html) · [Positivity Problems for Low-Order Linear Recurrence Sequences](https://arxiv.org/abs/1307.2779) · [On the Positivity Problem for Simple Linear Recurrence Sequences](https://arxiv.org/abs/1309.1550) · [Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences](https://arxiv.org/abs/1309.1914) · [Positivity Problems for Reversible Linear Recurrence Sequences](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.130)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6567 — Simple stochastic games in polynomial time

A simple stochastic game combines choices of a maximizing player, choices of a minimizing player and fair random branching. The project asks for a deterministic polynomial-time algorithm deciding whether the optimal probability of reaching a target exceeds a given rational threshold. Optimal positional strategies provide short certificates, but finding them may require navigating exponentially many combinations. Cycles also mean that solving local value equations without the correct reachability interpretation can give misleading answers. Progress would clarify the computational cost of exact planning against both adversarial and random uncertainty.

[Read in atlas](index.html#TCS-6567) · [The Complexity of Stochastic Games](https://www.sciencedirect.com/science/article/pii/089054019290048K) · [A Subexponential Randomized Algorithm for the Simple Stochastic Game Problem](https://www.sciencedirect.com/science/article/pii/S0890540185710358) · [A Direct Reduction from Stochastic Parity Games to Simple Stochastic Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CONCUR.2025.9) · [Sound Value Iteration for Simple Stochastic Games](https://arxiv.org/abs/2509.14112) · [Sinks and Ladders: ARRIVAL and SSG with Two Vertices per Level](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/html/LIPIcs.FUN.2026.19/LIPIcs.FUN.2026.19.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6569 — Internal semisimplicial types in ordinary HoTT

Semisimplicial types organize vertices, edges, triangles and higher-dimensional fillers with compatible shared boundaries. Ordinary homotopy type theory can describe any fixed finite collection of these stages externally. The project asks for one internal family indexed by natural numbers, together with compatible maps forgetting the highest stage. Higher identities carry data, so specifying all coherence requirements uniformly is harder than listing equations in ordinary set-based mathematics. Such a construction would provide an internal foundation for important higher-dimensional structures without extending the stated type theory.

[Read in atlas](index.html#TCS-6569) · [On the Role of Semisimplicial Types](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf) · [Homotopy Type Theory: Univalent Foundations of Mathematics](https://homotopytypetheory.org/book/) · [Two-level type theory and applications](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/twolevel-type-theory-and-applications/4914DB4F8E8305DFC68F9CDCA9D0C8D0) · [Two-Level Type Theory and Applications — revised manuscript](https://arxiv.org/abs/1705.03307v5) · [Displayed type theory and semi-simplicial types](https://doi.org/10.1017/S096012952510025X) · [Internal Constructions in Homotopical Type Theory](https://www.joshchen.io/pdf/thesis-phd.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6570 — Scott-continuous lambda models with theory \(\lambda \beta\)

Scott's continuous semantics interprets untyped lambda terms using mathematical domains and continuous functions. The project asks whether some model identifies exactly the pairs of terms related by beta-conversion. Beta-conversion expresses equality generated by applying functions to arguments and substituting those arguments into their bodies. Many semantic constructions validate additional equations, so soundness for beta-reduction alone does not answer the question. An exact model would show whether this influential notion of continuous meaning can distinguish every pair of terms that the basic operational equations keep separate.

[Read in atlas](index.html#TCS-6570) · [Continuously complete CPO models with minimal theory — TLCA Problem 22](https://tlca.di.unito.it/opltlca/opltlcasu29.html) · [Lambda theories of effective lambda models](https://arxiv.org/abs/math/0701684)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6583 — Barendregt–Geuvers–Klop conjecture

A pure type system specifies a typed lambda calculus through a uniform collection of formation rules. Weak normalization means that every well-typed term has some terminating reduction path. The conjecture asks whether that global property forces every reduction path of every well-typed term to terminate. A term may have both a normalizing route and a divergent route in less constrained rewriting settings, so the type-system hypothesis is essential. A proof would connect existence of normal forms with unrestricted evaluation termination across a broad family of typed calculi.

[Read in atlas](index.html#TCS-6583) · [Weak versus strong normalization for pure type systems — TLCA Problem 9](https://tlca.di.unito.it/opltlca/problem9.pdf) · [An Irrelevancy-Eliminating Translation of Pure Type Systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TYPES.2022.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4245 — Parity games in polynomial time

A parity game is a finite arena in which two players choose an infinite path, and the least priority recurring infinitely often decides the winner. The target asks whether one uniform deterministic polynomial-time algorithm decides the winner from every specified starting vertex. The card specifies arbitrary vertex ownership, full-history strategies, binary priorities and the complete bit-cost model. Quasipolynomial algorithms are established, while known separating-automaton lower bounds concern restricted methods. A November 2025 preprint claims a polynomial-time solution, but its correctness remains unverified in this review despite later literature continuing to call the problem open.

[Read in atlas](index.html#TCS-4245) · [The Model-Theoretic Expressiveness of Propositional Proof Systems](https://doi.org/10.4230/LIPIcs.CSL.2017.27) · [Deciding Parity Games in Quasipolynomial Time](https://www.cs.auckland.ac.nz/~cristian/crispapers/paritygame-stoc.pdf) · [Universal trees grow inside separating automata: Quasi-polynomial lower bounds for parity games](https://arxiv.org/abs/1807.10546v2) · [Attractors Is All You Need: Parity Games In Polynomial Time](https://arxiv.org/abs/2511.03752v1) · [On the Complexity of Robust Markov Decision Processes and Bisimulation Metrics](https://arxiv.org/abs/2604.26748v2)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-5773 — Skolem problem

The Skolem problem asks whether one terminating algorithm can decide if any given integer linear recurrence ever has a zero term. The input lists its order, coefficients and initial values in binary, with no restriction on order or repeated characteristic roots and no upper bound on the index. Every single term can be computed, but a decision procedure must also finish when the infinite sequence has no zero. The question is a basic exact reachability problem in linear dynamics with connections to program verification and automata. A complete Lean proof must establish decidability or undecidability for all inputs; conditional termination, low-order algorithms and density-one index sets do not settle that target.

[Read in atlas](index.html#TCS-5773) · [Skolem Meets Schanuel](https://doi.org/10.4230/LIPIcs.MFCS.2022.20) · [On the Complexity of the Skolem Problem at Low Orders](https://arxiv.org/abs/2507.11234v3) · [Conjectural Decidability of the Skolem Problem](https://arxiv.org/abs/2607.15510v1) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6568 — Mean-payoff games in polynomial time

Two players control different vertices of a finite integer-weighted graph and choose an infinite path from a specified start. Max wins when the lower limit of the average weight is nonnegative against every history-dependent strategy of Min, including exact equality zero. The question is whether the resulting binary-input winner language has one deterministic decider running in polynomial bit time on all inputs. Positional certificates and pseudopolynomial algorithms are known, but large binary weights leave a gap to the required complexity. Recent recursive, smoothed and linear-programming connections retain runtime, distributional or encoding limitations and do not settle the full target.

[Read in atlas](index.html#TCS-6568) · [The complexity of mean payoff games](https://link.springer.com/chapter/10.1007/BFb0030814) · [Faster Algorithms for Mean-Payoff Games](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf) · [Value Iteration Using Universal Graphs and the Complexity of Mean Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2020.34) · [Smoothed Analysis of Deterministic Discounted and Mean-Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.147) · [Strategy Improvement, the Simplex Algorithm and Lopsidedness](https://arxiv.org/abs/2509.16075) · [A symmetric recursive algorithm for mean-payoff games](https://arxiv.org/abs/2603.07555) · [Set-defined graph classes: χ-boundedness meets tropical algebra](https://arxiv.org/abs/2607.23754)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7230 — Tarski’s exponential function problem

Tarski’s exponential function problem asks whether one terminating algorithm can decide every first-order sentence about the standard real numbers with their full exponential function. The input is finite symbolic syntax with no arbitrary real constants or real-number oracle, and quantifiers range over all reals. Acceptance requires a complete Lean-checked proof of total correct decidability or a proof of undecidability, with no time bound and no unresolved extra hypothesis. The question extends decidable polynomial real arithmetic and already controls conditional verification results for restricted weighted automata. Macintyre–Wilkie’s conditional theorem and the checked June2026 axiomatization still rely on the real Schanuel hypothesis; restricted model completeness is a different conclusion.

[Read in atlas](index.html#TCS-7230) · [On the elementary theory of the real exponential field](https://arxiv.org/abs/2603.08365v2) · [Schanuel’s Conjecture and the Decidability of the Real Exponential Field](https://link.springer.com/chapter/10.1007/978-94-015-8923-9_11) · [Algorithmic Applications of Schanuel’s Conjecture](https://people.mpi-sws.org/~joel/publications/algorithmic-schanuel25.pdf) · [The Big-O Problem for Labelled Markov Chains and Weighted Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2020.41)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6566 — Continuous Skolem problem

A rational linear differential system evolves as a matrix exponential applied to its initial state. Continuous Skolem asks whether a specified rational linear observation is exactly zero at some finite nonnegative real time. The dimension is unrestricted, and the target is an unconditional always-halting Turing decision procedure or an undecidability proof. Conditional bounded-time and low-order recurrence results do not settle this question, and numerical proximity cannot distinguish a tangency from a near miss. A resolution would establish a basic limit of exact reachability verification for fully specified continuous linear dynamics.

[Read in atlas](index.html#TCS-6566) · [The continuous Skolem-Pisot problem](https://perso.uclouvain.be/vincent.blondel/publications/10BDJ.pdf) · [On the Skolem Problem for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1506.00695) · [On Recurrent Reachability for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1507.03632) · [Axiomatization of Compact Initial Value Problems: Open Properties](https://publikationen.bibliothek.kit.edu/1000188295/170660770) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7153 — Ultimate Positivity problem

A rational linear recurrence describes an infinite sequence using finitely many initial terms and constant coefficients. Ultimate Positivity asks whether every sufficiently late term is nonnegative, allowing a finite negative prefix and infinitely many zero terms. The target is one uniform decision procedure for arbitrary recurrence lengths, including repeated characteristic roots. The general problem is decidable through order five and the simple-root subclass is decidable at every order, while the July 2026 survey retains the unrestricted problem as open. Its resolution would connect algorithmic eventual sign analysis with central questions about linear dynamics and Diophantine approximation.

[Read in atlas](index.html#TCS-7153) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html) · [Positivity Problems for Low-Order Linear Recurrence Sequences](https://www.cs.ox.ac.uk/james.worrell/pos12.pdf) · [Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences](https://www.cs.ox.ac.uk/james.worrell/ultimate4.pdf) · [Termination Analysis of Linear-Constraint Programs](https://arxiv.org/abs/2509.06752v3) · [Positivity of arbitrary-order P-recursive sequences with a unique dominant root](https://arxiv.org/abs/2605.17013v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7157 — Termination of linear-constraint loops

A single-path linear-constraint loop permits exactly those successive state pairs satisfying one finite conjunction of rational linear inequalities. Termination means that no infinite execution exists from any initial state under any allowed sequence of choices. The question asks for the decidability status separately over integer, rational and real state spaces, with unrestricted dimension. Affine subclasses and the two-variable real case are decidable, while a 2026 result for one integer variable remains conditional on a generalized Collatz conjecture. A resolution would locate the algorithmic boundary between deterministic affine dynamics and more general nondeterministic linear programs.

[Read in atlas](index.html#TCS-7157) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html) · [Termination Analysis of Linear-Constraint Programs](https://arxiv.org/abs/2509.06752v3) · [Loop Termination and Generalized Collatz Sequences](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/LIPIcs.ICALP.2026.175/LIPIcs.ICALP.2026.175.pdf) · [The 2-Dimensional Constraint Loop Problem is Decidable](https://arxiv.org/abs/2405.12992v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7192 — Decidability of multiplicative-exponential linear logic

MELL asks whether provability in a resource-sensitive propositional logic can always be decided. Its multiplicative connectives combine resources, while exponential modalities permit controlled reuse. The card specifies the entire finite proof calculus, including units and the conditions on contraction and promotion. Proof checking alone does not guarantee that a search can terminate on an unprovable input. A July 2026 preprint claims a positive resolution through general branching vector addition systems, which is recorded here without independent proof verification.

[Read in atlas](index.html#TCS-7192) · [Handbook of Linear Logic](https://ll-handbook.pages.math.cnrs.fr/book/ll-handbook-public.pdf) · [On the Decision Problem for MELL](https://www.lix.polytechnique.fr/~lutz/papers/OnDeciMELL.pdf) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.22/LIPIcs.MFCS.2025.22.html) · [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear Inductive Invariants](https://arxiv.org/abs/2607.09558v1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7154 — Effective ultimate-positivity thresholds for simple recurrences

A simple rational linear recurrence has a characteristic polynomial with distinct roots and a finite exact description. The question asks for an algorithm that produces an index beyond which every term is nonnegative whenever such an index exists. Any sufficient index is accepted, with no requirement that it be minimal or small. Ultimate Positivity itself is already decidable for this class, but the checked general algorithm does not compute the threshold and later cardinality bounds do not locate the final exception. A general effective threshold would close a gap between eventual guarantees and finite witnesses and would decide all-time Positivity for simple recurrences.

[Read in atlas](index.html#TCS-7154) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html) · [Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences](https://www.cs.ox.ac.uk/james.worrell/ultimate4.pdf) · [On the Positivity Problem for Simple Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/simple_positivity14.pdf) · [Quantitative growth of linear recurrences](https://arxiv.org/abs/2504.09519v1) · [Positivity of arbitrary-order P-recursive sequences with a unique dominant root](https://arxiv.org/abs/2605.17013v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5915 — Constructive simplicial model with univalent universes

The question asks for a constructive simplicial interpretation of dependent type theory with univalent universes. The selected metatheory is CZF with a sequence of constructive inaccessible sets and the explicit principle that every subset of a small set is small. The model must interpret the stated dependent type formers and make all operations commute strictly with substitution. Existing constructive simplicial work provides substantial weakly stable structure but leaves the strict coherence issue open in the checked sources. A full construction would connect simplicial homotopy theory with constructive univalent foundations without importing excluded middle or choice.

[Read in atlas](index.html#TCS-5915) · [From Cubes to Twisted Cubes via Graph Morphisms in Type Theory](https://doi.org/10.4230/LIPIcs.TYPES.2019.5) · [Towards a constructive simplicial model of Univalent Foundations](https://doi.org/10.1112/jlms.12532) · [Towards a constructive simplicial model of Univalent Foundations — author version](https://arxiv.org/abs/1905.06281v3) · [The equivariant model structure on cartesian cubical sets](https://doi.org/10.1016/j.aim.2026.110965) · [The equivariant model structure on cartesian cubical sets — published full text](https://research.chalmers.se/publication/551789/file/551789_Fulltext.pdf) · [A constructive model of infinity-groupoids — TYPES 2025 slides](https://msp.cis.strath.ac.uk/types2025/slides/TYPES2025-slidesSattler.pdf) · [Constructive higher sheaf models with applications to synthetic mathematics](https://arxiv.org/abs/2605.15126v2) · [Notes on Constructive Set Theory](https://michrathjen.github.io/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6245 — Exponential witness bounds for three-dimensional VASS

A three-dimensional vector addition system with states combines a finite control graph with three nonnegative integer counters. The question asks whether every reachable pair of configurations has an actual run whose length is singly exponential in the binary input size. The same exponent bound must work for all inputs, including unbounded control graphs and arbitrary binary counter values. Published triply-exponential and subsequently claimed doubly-exponential witness bounds leave this stronger target unresolved. A resolution would clarify the structural and algorithmic change between exact reachability with two counters and with three.

[Read in atlas](index.html#TCS-6245) · [Involved VASS Zoo (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2022.5) · [Reachability in 3-VASS Is Elementary](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/LIPIcs.ICALP.2025.153/LIPIcs.ICALP.2025.153.pdf) · [3-VASS Reachability is in EXPSPACE](https://arxiv.org/abs/2607.14983v1) · [Reachability in 3-VAS](https://arxiv.org/abs/2608.04786v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4302 — Exact multi-objective LTL achievability in stochastic games

A finite stochastic game combines controller choices, adversary choices and rational chance transitions. The selected question asks whether one randomized strategy can meet all supplied rational probability bounds for LTL properties against every adversary. Both players may depend on the whole history, and the existential strategy need not have an effective finite representation. The decision must distinguish actual exact threshold attainment from approximate or limit-sure guarantees. This user-selected decision subproblem makes one part of the broader multi-objective synthesis programme precise.

[Read in atlas](index.html#TCS-4302) · [Model Checking and Strategy Synthesis for Stochastic Games: From Theory to Practice (Invited Talk)](https://doi.org/10.4230/LIPIcs.ICALP.2016.4) · [Solving Qualitative Multi-Objective Stochastic Games](https://arxiv.org/abs/2602.12927v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5817 — Effective homotopy canonicity with propositional resizing

The selected question adds individual propositional resizing to a fixed univalent De Morgan cubical calculus. Each homotopy proposition in one universe must have an equivalent representative in the adjacent smaller universe. The requested result combines consistency with an algorithm that turns every closed natural-number derivation into a numeral and an object-theory path proof. Existing canonicity theorems for the base calculus and models separating resizing principles do not establish this extension’s computational guarantee. A resolution would clarify whether this useful size principle can retain effective natural-number observations without demanding full normalization.

[Read in atlas](index.html#TCS-5817) · [Domain Theory in Constructive and Predicative Univalent Foundations](https://doi.org/10.4230/LIPIcs.CSL.2021.28) · [Continuous and algebraic domains in univalent foundations](https://doi.org/10.1016/j.jpaa.2025.108072) · [Continuous and algebraic domains in univalent foundations — accepted manuscript](https://martinescardo.github.io/papers/continuous-algebraic-domains-in-uf.pdf) · [Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing](https://doi.org/10.4230/LIPIcs.TYPES.2018.7) · [Cubical Type Theory: a constructive interpretation of the univalence axiom](https://arxiv.org/abs/1611.02108v1) · [Canonicity and homotopy canonicity for cubical type theory](https://lmcs.episciences.org/9043) · [A Modal Deconstruction of Löb Induction](https://doi.org/10.1145/3704866)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5987 — Decidability of weak bisimulation for normed BPA

Basic Process Algebra represents recursive sequential processes by finite words whose leftmost variable is rewritten using a finite rule system. Normedness requires each variable to have some terminating execution and permits both silent termination and silent divergence. The question asks whether weak bisimilarity of two such processes is decidable when finite silent paths may surround every matched visible action. Known decision procedures for branching bisimilarity or totally normed subclasses do not cover the full weak equivalence defined here. A resolution would locate the algorithmic limit of hiding internal computation during exact comparison of simple infinite-state processes.

[Read in atlas](index.html#TCS-5987) · [Two Lower Bounds for BPA](https://doi.org/10.4230/LIPIcs.CONCUR.2017.20) · [Checking Equality and Regularity for Normed BPA with Silent Moves](https://basics.sjtu.edu.cn/~yuxi/papers/ICALP-2013-Final-Version.pdf) · [Branching Bisimilarity of Normed BPA Processes as a Rational Monoid](https://lmcs.episciences.org/4097/pdf) · [Deciding Weak Bisimilarity of Normed Context-Free Processes Using Tableau](https://link.springer.com/chapter/10.1007/978-3-540-75292-9_23)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7310 — Unconditional decidability of exact time-bounded CTMDP reachability

The input describes a finite controlled stochastic process whose transitions occur in continuous time. A policy chooses actions from the current state and elapsed time, including between jumps. The target is exact comparison of the optimal deadline-reachability probability with rational thresholds for every initial state. The cited theorem decides this question assuming Schanuel’s conjecture. The card asks whether the same strict-threshold language is decidable unconditionally.

[Read in atlas](index.html#TCS-7310) · [On Decidability of Time-Bounded Reachability in CTMDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.133)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3655 — Inductive-inductive types from inductive types without UIP

Inductive-inductive types define mutually dependent sorts, such as contexts together with the types valid in each context. The selected question asks whether every finitary signature can be implemented uniformly in intensional MLTT using indexed W-types and function extensionality, without UIP or equality reflection. The implementation must include full dependent eliminators whose later motives can use the results of earlier eliminators, with propositional constructor equations. The generic published reduction uses an extensional foundation, while the checked UIP-free constructions cover more restricted settings or signatures. A resolution would determine whether this important form of dependent datatype needs a new primitive in the explicitly chosen intensional foundation.

[Read in atlas](index.html#TCS-3655) · [For Finitary Induction-Induction, Induction Is Enough](https://doi.org/10.4230/LIPIcs.TYPES.2019.6) · [Constructing Inductive-Inductive Types in Cubical Type Theory](https://jashug.github.io/papers/ConstructingII.pdf) · [ConTyWithoutK.agda: Constructing a simple closed finitary inductive-inductive type without UIP](https://gist.github.com/szumixie/cf092edec50ad11b91c2d7d086582b15/fc32088bd31bcc59e3266dde2ab00c184a025820) · [Saint Nicholas HOTT workshop programme, 5 December 2025](https://types.elte.hu/)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5682 — One-dimensional piecewise-affine reachability

A one-dimensional rational piecewise-affine map repeatedly updates one number using the affine expression selected by its interval guards. The question asks whether exact reachability of a rational target from a rational starting point is decidable for every finite description. The number of pieces is unrestricted, all boundary choices are explicit, and any finite number of iterations including zero is allowed. Injective two-piece maps and certain Bellman operators admit decision procedures, but the checked source retains the general question as open. A resolution would locate a basic boundary between finite descriptions of numerical dynamics and algorithmic reachability analysis.

[Read in atlas](index.html#TCS-5682) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92) · [Reachability in Injective Piecewise Affine Maps](https://arxiv.org/abs/2301.09752v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6359 — Decidability and completeness of concurrent Kleene algebra with parallel iteration

Concurrent Kleene algebra describes finite partially ordered executions using choice, sequential and parallel composition, and iteration. The card asks both whether refinement is decidable and whether its valid inequalities follow from the stated axioms when both sequential and parallel iteration are allowed. Refinement preserves events and labels while permitting extra ordering, and parallel iteration allows arbitrarily many concurrent copies. Decision and completeness results for expressions without parallel iteration do not settle the full-signature questions retained here. A resolution would establish the algorithmic and proof-theoretic limits of algebraic reasoning about unbounded finite concurrency.

[Read in atlas](index.html#TCS-6359) · [On Decidability of Concurrent Kleene Algebra](https://doi.org/10.4230/LIPIcs.CONCUR.2017.28) · [Concurrent Kleene Algebra: Free Model and Completeness](https://doi.org/10.1007/978-3-319-89884-1_30) · [Completeness Theorems for Pomset Languages and Concurrent Kleene Algebras](https://arxiv.org/abs/1705.05896v1) · [A note on commutative Kleene algebra](https://arxiv.org/abs/1910.14381v1) · [Concurrent Kleene Algebra: Completeness and Decidability](https://discovery.ucl.ac.uk/id/eprint/10109361/13/main.pdf) · [Continuous Algebras with Hypotheses](https://drops.dagstuhl.de/storage/00lipics/lipics-vol391-concur2026/LIPIcs.CONCUR.2026.42/LIPIcs.CONCUR.2026.42.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6036 — Decidability of restricted elementary real functions

The problem asks whether exact first-order truth is decidable over the real field with exponential, sine and cosine restricted to the unit interval. It also includes the source’s extended language with unrestricted exponential, using a tag to make both signatures one decision problem. Inputs are finite sentences with only fixed primitive constants, while all quantified variables range over the standard real numbers. Known conditional results use Schanuel’s conjecture, and continuous-system invariant questions provide a computational motivation. A solution must give an unconditional total decision procedure for the joint truth set or prove that none exists.

[Read in atlas](index.html#TCS-6036) · [Invariants for Continuous Linear Dynamical Systems](https://doi.org/10.4230/LIPIcs.ICALP.2020.107) · [Algorithmic Applications of Schanuel’s Conjecture](https://people.mpi-sws.org/~joel/publications/algorithmic-schanuel25.pdf) · [Turing meets Schanuel](https://doi.org/10.1016/j.apal.2015.10.003) · [Integration in finite terms and exponentially algebraic functions](https://arxiv.org/abs/2510.26248v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0619 — TOWER-hard reachability with seven nonnegative counters

A VASS combines finite control with nonnegative integer counters updated by fixed transition vectors. The question asks for TOWER-hard reachability using only seven counters and unary-encoded numbers. Seven counters capture the source’s request for any improvement below the known eight-counter bound, by padding unused coordinates. TOWER-hardness uses elementary-time reductions and is stronger than a collection of unrelated fixed-height exponential lower bounds. Recent lower bounds with extra signed counters concern a different computational model.

[Read in atlas](index.html#TCS-0619) · [Automata Exchange](https://automata.exchange/25.9-reachability-in-low-dimensional-vass/) · [Lower Bounds for the Reachability Problem in Fixed Dimensional VASSes](https://arxiv.org/abs/2203.04243) · [Reachability in VASS Extended with Integer Counters](https://doi.org/10.4230/LIPIcs.LICS.2026.19)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-1649 — Decidability of branching-VASS reachability

A branching vector addition system combines finite control with nonnegative integer resources. Rules can combine several already derived configurations by adding their resource vectors and a fixed displacement. Reachability asks whether a finite valid derivation tree produces exactly a supplied target. The dimension is part of the input, and every branch must be fully justified. The September 2026 structural and low-dimensional results explicitly leave arbitrary-dimensional reachability open.

[Read in atlas](index.html#TCS-1649) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://doi.org/10.4230/LIPIcs.MFCS.2025.22) · [Bridging the Gap Between Plain VASS and Branching VASS](https://arxiv.org/abs/2609.15869)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5975 — Decisiveness of static probabilistic Petri nets for finite targets

A static probabilistic Petri net randomly chooses an enabled transition according to its fixed positive weight. Decisiveness for a finite target means that almost every run eventually reaches either the target or a marking from which the target is unreachable. The question asks whether this property is decidable from the net, one initial marking and an explicit finite target set. Known upward-closed-target guarantees and undecidability with marking-dependent weights do not settle this constant-weight finite-target case. A resolution would clarify when a general guarantee supporting certified probability approximation can be recognized in an ordinary probabilistic counter model.

[Read in atlas](index.html#TCS-5975) · [About Decisiveness of Dynamic Probabilistic Models](https://doi.org/10.4230/LIPIcs.CONCUR.2023.14) · [Tightening the Frontier of Decidability for Decisiveness](https://home.lmf.cnrs.fr/downloads/SergeHaddad/A25-QEST.pdf) · [Tightening the Frontier of Decidability for Decisiveness — presentation](https://lmf.cnrs.fr/downloads/Perso/talkqf.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0632 — Linear-length witnesses for reachability in each fixed vector addition system

A fixed vector addition system supplies a finite collection of updates on nonnegative integer vectors. The conjecture asks whether every reachable pair has a run linear in the numerical sizes of its endpoints. The multiplicative constant may depend on the entire fixed system, while the endpoints vary freely. The non-strict bound includes the zero-length run from zero to itself. This structural witness bound would have complexity consequences, but it is not a linear-time algorithm in binary input length.

[Read in atlas](index.html#TCS-0632) · [Automata Exchange](https://automata.exchange/22.01-complexity-fixed-vas-reachability/) · [Reachability in Fixed VASS: Expressiveness and Lower Bounds](https://doi.org/10.1007/978-3-031-57231-9_9)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-2033 — Elementary-time reachability for one-dimensional grammar-controlled VAS

A context-free grammar specifies integer update sequences for a single nonnegative counter. Reachability requires a generated sequence that stays nonnegative at every prefix and ends at the exact target value. General decidability is now established, and this card selects the still-open elementary-time boundary. The algorithm must have one fixed-height exponential bound for all binary-encoded grammars and endpoints. A later reduction preserves this elementary-time question between general and thin grammars.

[Read in atlas](index.html#TCS-2033) · [Challenges of the Reachability Problem in Infinite-State Systems (Invited Paper)](https://doi.org/10.4230/LIPIcs.MFCS.2024.2) · [Reachability in One-Dimensional Pushdown Vector Addition Systems is Decidable](https://arxiv.org/abs/2411.02386) · [On the Reachability Problem for One-Dimensional Thin Grammar Vector Addition Systems](https://arxiv.org/abs/2602.05315)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3031 — Consistency of excluded middle and Church’s thesis in Coq

Church’s thesis says that every internal function from natural numbers to natural numbers is computable. The law of excluded middle gives classical reasoning about propositions. The question asks whether adding both propositional axioms to Coq’s ordinary cumulative inductive core can produce a contradiction. The distinction between propositional existence and computable witness extraction is essential. A 2023 thesis proves consistency for a restricted fragment, leaving the selected full-calculus target beyond that result.

[Read in atlas](index.html#TCS-3031) · [Church’s Thesis and Related Axioms in Coq’s Type Theory](https://doi.org/10.4230/LIPIcs.CSL.2021.21) · [Coq 8.11 Reference Manual: Calculus of Inductive Constructions](https://docs.rocq-prover.org/v8.11/refman/language/cic.html) · [Consistency of Classical Synthetic Computability Theory](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=153088&lang=eng)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6112 — Univalence, impredicativity and propositional resizing

An impredicative universe supports quantification over types without the usual increase in universe size, while univalence connects equivalence with equality. Propositional resizing adds the requirement that large propositions have equivalent small representatives. The source asks for a model of type theory supporting all three features together. Its cubical assembly construction provides univalence and impredicativity but fails resizing, and a related positive model weakens identity and dependent-product structure. Constructing a model with the intended ordinary type-theoretic rules would clarify whether these attractive foundational principles can coexist without sacrificing essential forms of dependent reasoning.

[Read in atlas](index.html#TCS-6112) · [Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TYPES.2018.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0640 — Shortest runs in 3-D VASS

A three-dimensional VASS is a finite-state system with three nonnegative integer counters. The source asks whether some reachable instances require shortest runs longer than every single-exponential bound in their binary input length. Encoding a large initial counter in binary already permits exponentially many necessary steps, so a stronger growth rate is required. A July 2026 preprint states a doubly-exponential upper bound, improving the triple-exponential bound from 2025. The remaining threshold question measures how much reachability-witness complexity three counters can force.

[Read in atlas](index.html#TCS-0640) · [Shortest runs in 3-D VASS](https://automata.exchange/19.11-shortest-runs-in-3-d-vass/) · [Reachability in 3-VASS is Elementary](https://arxiv.org/abs/2502.13916) · [3-VASS Reachability is in EXPSPACE](https://arxiv.org/abs/2607.14983)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4017 — Relative completeness of Kleene induction for the positive calculus of relations

Expressions denote binary relations using positive operations, converse and finite-path closure. The target asks whether every relationally valid equation follows from a specified proof system. That system contains all valid closure-free equations and ordinary left and right Kleene induction. The closure-free base is an explicit editorial choice that fixes interactions among the operations. The later EXPSPACE validity algorithm and completeness of smaller fragments do not prove this relative-completeness claim.

[Read in atlas](index.html#TCS-4017) · [On the Positive Calculus of Relations with Transitive Closure](https://doi.org/10.4230/LIPIcs.STACS.2018.3) · [Derivatives on Graphs for the Positive Calculus of Relations with Transitive Closure](https://lmcs.episciences.org/17069)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0913 — Word problem for the S-combinator

Closed S-terms are finite application trees using only the combinator S. The rule sends S applied to x, y and z to the application of xz to yz, and can be used inside any subterm. The word problem asks whether two such trees are connected by finitely many forward or backward rule applications. Normalization is decidable for this fragment, but the 2023 source still leaves general convertibility open. A solution supplies a Lean-checked decidability or undecidability proof covering nonnormalizing terms as well.

[Read in atlas](index.html#TCS-0913) · [RTA Open Problem 97: The word problem for the S-combinator](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/97.html) · [A Lambda Calculus Satellite (Invited Talk)](https://doi.org/10.4230/LIPIcs.FSCD.2023.3)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-1659 — Exact finite-iteration reachability for Bellman operators

The input describes a finite rational Markov decision process and two rational value vectors. Its Bellman operator updates each coordinate by the best available affine probability expression. The question asks whether exact iteration reaches the target vector after finitely many steps. The source assumes no end components but allows several actions tight at the fixed point. Convergence and the known two-dimensional decision procedure do not settle the general finite-attainment problem.

[Read in atlas](index.html#TCS-1659) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0896 — Computable one-step normalization for finite confluent term rewriting

The system has finitely many first-order rewrite rules and admits every term over its finite signature. Confluence makes normal forms unique when they exist. The question asks for a computable strategy that chooses exactly one available contraction from the current term. The next-step computation must halt even on terms that never reach a normal form, without retaining an external history. The strategy must nevertheless normalize every term for which some terminating reduction exists.

[Read in atlas](index.html#TCS-0896) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/10.html)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0901 — Decidability of termination for one left- and right-linear term rule

The input is one first-order rewrite rule whose left and right sides each use every variable at most once. The rule may be applied at any position in any finite term, with ordinary syntactic substitutions. The question asks whether an algorithm can decide absence of every infinite reduction sequence. Left-linearity alone and the smaller string-rewriting subclass have different known boundaries. Recent undecidability for linear-interpretation proof methods must not be confused with linearity of the rule itself.

[Read in atlas](index.html#TCS-0901) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/21.html) · [Linear Termination is Undecidable](https://doi.org/10.1145/3661814.3662081)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0092 — A coanalytic upper bound for fair almost-sure termination

The machine combines finite nondeterministic choices with rational probabilistic choices and unbounded tape memory. Schedulers may use arbitrary histories, but must satisfy strong fairness on every supported infinite execution. FAST requires probability-one termination under each such fair scheduler, without an expected-runtime bound. This card selects the precise question of a computable reduction to well-foundedness of primitive-recursive trees. Known results for positive almost-sure termination and weakly fair distributed protocols have different hypotheses.

[Read in atlas](index.html#TCS-0092) · [Automata Exchange](https://automata.exchange/25.19-complete-techniques-for-deducing-fair-almost-sure-termination/) · [Positive Almost-Sure Termination — Complexity and Proof Rules](https://arxiv.org/abs/2310.16145) · [Verifying Almost-Sure Termination for Randomized Distributed Algorithms](https://sigplan.org/OpenTOC/popl26.html)
Existing status: `source_open` · Summary written: 2026-09-13

## Distributed, parallel and sublinear algorithms (58)

### TCS-6553 — P versus NC

NC describes computations with polynomial total circuit size and only polylogarithmic dependency depth, under a uniformity requirement. The question asks whether every problem solvable in polynomial sequential time belongs to this parallel class. Circuit Value is a concrete complete problem: given a circuit and its input, compute the designated output. An NC algorithm for circuit evaluation would therefore parallelize every problem in P. The challenge is to distinguish a long chain in the supplied circuit from an unavoidable chain in every possible algorithm for evaluating its behavior.

[Read in atlas](index.html#TCS-6553) · [Limits to Parallel Computation: P-Completeness Theory](https://homes.cs.washington.edu/~ruzzo/papers/limits.pdf) · [The circuit value problem is log space complete for P](https://doi.org/10.1145/990518.990519) · [Separation of the monotone NC hierarchy](https://weizmann.esploro.exlibrisgroup.com/esploro/outputs/journalArticle/Separation-of-the-monotone-NC-hierarchy/993263130303596) · [Monotone Circuit Complexity of Matching](https://arxiv.org/abs/2507.16105v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6556 — Directed reachability with nearly linear memory and polylogarithmic passes

Directed reachability in a stream asks whether one vertex can reach another when graph edges arrive in an adversarial order. Nearly linear memory in the vertex count cannot store every edge of a dense graph. The question asks for a randomized algorithm using only polylogarithmically many passes and n times a polylogarithmic number of memory bits. Simple repeated scans can propagate reachability one step at a time, taking many passes on badly ordered paths. The project is to combine a small memory footprint with far fewer scans without relying on favorable edge order.

[Read in atlas](index.html#TCS-6556) · [Recent Advances in Multi-Pass Graph Streaming Lower Bounds](https://par.nsf.gov/servlets/purl/10488812) · [Superlinear lower bounds for multipass graph processing](https://eccc.weizmann.ac.il/report/2013/002/revision/3/download/) · [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841) · [Semi-Streaming Bipartite Matching in Fewer Passes and Optimal Space](https://arxiv.org/abs/2011.03495) · [Almost Optimal Super-Constant-Pass Streaming Lower Bounds for Reachability](https://par.nsf.gov/servlets/purl/10315017) · [Streaming Algorithms for Monotonicity Testing](https://arxiv.org/abs/2608.07073v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6504 — Perfect matching in NC

Perfect matching seeks pairwise disjoint edges that cover every vertex of a graph. The question asks for a deterministic parallel algorithm on general graphs with polynomially many processors and polylogarithmic running time. Sequential polynomial-time algorithms do not supply this bound because their matching updates may depend on earlier choices. General graphs also contain odd cycles, which require coordination beyond the constraints that suffice in bipartite graphs. The saved card distinguishes this target from the nearby bipartite advance and asks whether compatible matching decisions can be organized efficiently in parallel without randomness.

[Read in atlas](index.html#TCS-6504) · [The Matching Problem in General Graphs Is in Quasi-NC](https://doi.org/10.1109/FOCS.2017.70) · [Bipartite Matching is in NC](https://eccc.weizmann.ac.il/report/2026/100/)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6554 — Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds

The distributed Lovasz Local Lemma seeks an assignment avoiding many bad events, each depending on only a bounded number of other events. Processors know local portions of this dependency structure and communicate in synchronous LOCAL rounds. The question asks for \(O(\log  \log  n)\) rounds with high probability when the dependency degree is constant and the probability criterion has sufficiently strong constant polynomial slack. The guarantee must bound the worst finishing time over all nodes. An algorithm that achieves only a small average finishing time would leave the central coordination issue unresolved for the last remaining bad events.

[Read in atlas](index.html#TCS-6554) · [Sublogarithmic Distributed Algorithms for Lovász Local Lemma, and the Complexity Hierarchy](https://arxiv.org/abs/1705.04840) · [On the Locality of the Lovász Local Lemma](https://arxiv.org/abs/2502.11690)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6555 — Optimal exact single-source shortest paths in CONGEST

Single-source shortest paths asks every vertex to learn its exact distance from one source in a weighted network. In CONGEST, each edge carries only a logarithmic number of bits per communication round. The target is a randomized algorithm using roughly \(\sqrt{n}\) plus the hop diameter D rounds, ignoring polylogarithmic factors. The graph is undirected and connected, with nonnegative polynomially bounded integer edge weights. Achieving this bound would combine global distance propagation with the bandwidth limits of the network at the scale identified by the saved problem statement.

[Read in atlas](index.html#TCS-6555) · [Polylogarithmic time algorithms for shortest path forests in programmable matter](https://link.springer.com/article/10.1007/s00446-026-00505-2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6557 — Explicit superconstant lower bounds in the congested clique

Can a graph predicate that is easy to compute centrally require a number of congested-clique rounds tending to infinity? Each processor initially knows its incident graph edges and can send a different logarithmic-size message to every other processor in each round. Only one decision bit is required, and local computation is unrestricted. Known hard-function counting and hierarchy arguments do not provide the required centrally polynomial-time predicate. Broadcast bounds and the known two-round MST limitation do not resolve this unicast one-bit target.

[Read in atlas](index.html#TCS-6557) · [On the Power of the Congested Clique Model](https://people.csail.mit.edu/andyd/cong_clique_podc14.pdf) · [Towards a complexity theory for the congested clique](https://jukkasuomela.fi/doc/clique-complexity.pdf) · [What Can We Compute in a Single Round of the Congested Clique?](https://arxiv.org/abs/2210.02638v4)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7349 — Almost-linear-work parallel exact maximum flow

The task is exact maximum flow in a directed graph with polynomially bounded integer capacities. The question asks for almost-linear total parallel work and subpolynomial depth. Bounded-error randomization is allowed in a uniform shared-memory parallel model. Sequential almost-linear algorithms do not provide the requested bound on dependent stages. DAG projection reductions connect several versions of this open parallel flow problem.

[Read in atlas](index.html#TCS-7349) · [DAG Projections: Reducing Distance and Flow Problems to DAGs](https://arxiv.org/abs/2604.04752)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6507 — Work-efficient parallel directed reachability

Given a directed graph and a source, the task is to mark exactly all vertices reachable from that source. The question asks for a uniform randomized CREW parallel algorithm with nearly linear total work in the input size and polylogarithmic depth on every input. Correctness of the complete output and both resource bounds must hold together with high probability for each fixed graph. The 2026 density improvement retains polynomial depth, while the August polylogarithmic-depth result measures work by a potentially quadratic transitive closure. A complete Lean proof must decide whether the two desired resource guarantees can be achieved simultaneously in the specified model.

[Read in atlas](index.html#TCS-6507) · [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841v4) · [Parallel Reachability and Shortest Paths on Non-Sparse Digraphs: Near-Linear Work and Sub-Square-Root Depth](https://doi.org/10.4230/LIPIcs.ICALP.2026.15) · [Parallel Reachability and Shortest Paths on Non-sparse Digraphs: Near-linear Work and Sub-square-root Depth, full version](https://arxiv.org/abs/2605.03892v1) · [\(\widetilde O(1)\)-Depth Parallel Reachability Faster than Transitive Closure](https://arxiv.org/abs/2608.13231v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7172 — Depth-first search in NC

A depth-first-search forest records the parent choices of recursive graph exploration. For an undirected graph, it is a rooted spanning forest in which every graph edge joins a vertex to one of its ancestors. The problem asks for a deterministic, uniformly specified parallel computation that constructs any such forest with polynomial resources and polylogarithmic depth. Randomized NC algorithms and deterministic results for restricted graph classes are known, but those guarantees do not settle the general target. A solution would show whether this basic search structure can always be built efficiently in parallel without random choices.

[Read in atlas](index.html#TCS-7172) · [Parallel Complexity of Depth-First-Search and Maximal Path in Restricted Graph Classes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2025.23) · [A random NC algorithm for depth first search](https://doi.org/10.1007/BF02122548) · [Nearly Work-Efficient Parallel DFS in Undirected Graphs](https://arxiv.org/abs/2304.09774)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0522 — Quantum 3-coloring of cycles in \(o(\log^{*}n)\) rounds

Processors on an oriented cycle must choose three classical colors with different colors at every edge. They may perform finite local quantum computations and communicate qubits with both neighbors in synchronous rounds. One uniform protocol must work for every cycle size and every distinct identifier assignment, starting without shared randomness or entanglement. The target is worst-case communication below the log-star scale with global success probability at least one minus one over the number of nodes. Recent zero-error and one-way one-round lower bounds cover restricted models and do not resolve this high-probability question.

[Read in atlas](index.html#TCS-0522) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#quantum-local) · [Locality in Distributed Graph Algorithms](https://doi.org/10.1137/0221015) · [A Lower Bound on Probabilistic Algorithms for Distributive Ring Coloring](https://doi.org/10.1137/0404036) · [Finitely Dependent Coloring](https://doi.org/10.1017/fmp.2016.7) · [No Distributed Quantum Advantage for 3-Coloring Rooted Trees and 2-Coloring Even Cycles](https://arxiv.org/abs/2607.04852v2) · [Distributed Quantum Algorithms Cannot Color Cycles with Probability 1](https://arxiv.org/abs/2608.11720v1) · [Finitely Dependent Cycle Coloring](https://arxiv.org/abs/1707.09374v1) · [Impossibility of One-Way One-Round Quantum 4-Coloring via Matrix-Space Stability](https://arxiv.org/abs/2609.09091v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0969 — Optimal one-pass randomized space for LIS length

The problem asks for optimal bit space to estimate the longest strictly increasing subsequence in one streaming pass. Inputs are arbitrary length-n sequences of numbers from one to n, fixed before the algorithm chooses its random bits. The final estimate must lie between half the true length and the true length with probability at least two thirds. Deterministic upper bounds and recent lower bounds against a stronger adaptive adversary leave the ordinary randomized optimum unresolved. The requested answer must match upper and lower bounds up to constants, including every logarithmic factor.

[Read in atlas](index.html#TCS-0969) · [Problem 44: Approximating LIS Length in the Streaming Model](https://sublinear.info/index.php?title=Open_Problems:44) · [Estimating the Sortedness of a Data Stream](https://www.wisdom.weizmann.ac.il/~robi/papers/GJKK-stream-SODA07.pdf) · [A Note on Randomized Streaming Space Bounds for the Longest Increasing Subsequence Problem](https://doi.org/10.1016/j.ipl.2011.12.008) · [Optimal White-Box Adversarial Streaming Lower Bounds for Approximating LIS Length](https://doi.org/10.4230/LIPIcs.ITCS.2026.64)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6499 — Sublogarithmic distributed MIS

A maximal independent set contains no adjacent vertices and leaves every unselected vertex next to a selected one. The question asks for a randomized LOCAL algorithm that finds such a set in \(o(\log  n)\) rounds on every graph with high probability. Message sizes and local computation are unrestricted, so the resource measures the distance over which decisions must be coordinated. The running-time improvement must hold uniformly even for graphs of very large degree. Degree-sensitive algorithms already improve some cases, but the target requires a mechanism that also avoids logarithmically many phases on unrestricted graphs.

[Read in atlas](index.html#TCS-6499) · [Breaking Barriers for Distributed MIS by Faster Degree Reduction](https://arxiv.org/abs/2505.15652) · [An Improved Distributed Algorithm for Maximal Independent Set](https://arxiv.org/abs/1506.05093) · [Round Elimination via Self-Reduction: Closing Gaps for Distributed Maximal Matching](https://arxiv.org/abs/2505.15654)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6505 — One-cycle versus two-cycles conjecture

The one-cycle-versus-two problem distinguishes a single n-vertex cycle from two disjoint cycles of half that size. In the low-memory MPC model, edges are spread across machines with sublinear local memory and linear total memory. The conjecture says randomized algorithms require \(\Omega (\log  n)\) communication rounds under these resource bounds. Both input types have identical vertex counts, edge counts, and degrees, so only their global connectivity distinguishes them. A lower bound must handle arbitrary communication between machines and arbitrary encodings, rather than assuming information can travel only along graph edges.

[Read in atlas](index.html#TCS-6505) · [\(O(1)\)-Round MPC Algorithms for Multi-Dimensional Grid Graph Connectivity, Euclidean MST and DBSCAN](https://doi.org/10.4230/LIPIcs.ICDT.2025.7) · [Equivalence classes and conditional hardness in massively parallel computations](https://doi.org/10.1007/s00446-021-00418-2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6506 — Deterministic LOCAL MIS in \(O(\log  n)\) rounds

Deterministic maximal independent set algorithms must coordinate their choices using the graph and vertex identifiers alone. The question asks whether \(O(\log  n) \mathrm{LOCAL}\) rounds suffice on every graph and every valid identifier assignment. The output must be independent and dominate all unselected vertices, without requiring maximum cardinality. Network decomposition already supports polylogarithmic deterministic algorithms, so the target is a sharper dependence on network size. Reaching the logarithmic bound would require organizing deterministic progress efficiently even when identifier patterns defeat simple greedy local rules.

[Read in atlas](index.html#TCS-6506) · [Near-Optimal Deterministic Network Decomposition and Ruling Set, and Improved MIS](https://arxiv.org/abs/2410.19516) · [Lower Bounds for Maximal Matchings and Maximal Independent Sets](https://arxiv.org/abs/1901.02441) · [Polylogarithmic-Time Deterministic Network Decomposition and Distributed Derandomization](https://arxiv.org/abs/1907.10937) · [Faster Distributed \(\Delta\)-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0954 — Subquadratic metric TSP cost estimation below factor two

A metric TSP cost query algorithm asks for distances between selected pairs of labeled points. The question asks whether some fixed approximation factor below two is achievable with a subquadratic number of queries on every metric. The algorithm is randomized and only needs to output a cost estimate, with success probability at least two thirds. Nearly linear MST-weight estimation gives the factor-two baseline, while stronger TSP estimates are known for special metrics or with extra spanning-tree information. The target separates sparse access to a global optimum value from the information needed to construct an explicit tour.

[Read in atlas](index.html#TCS-0954) · [Open Problems in Sublinear Algorithms, Problem 71: Metric TSP Cost Approximation](https://sublinear.info/index.php?title=Open_Problems:71) · [Estimating the Weight of Metric Minimum Spanning Trees in Sublinear Time](https://doi.org/10.1137/060672121) · [Sublinear Algorithms and Lower Bounds for Metric TSP Cost Estimation](https://doi.org/10.4230/LIPIcs.ICALP.2020.30) · [Sublinear Algorithms and Lower Bounds for Estimating MST and TSP Cost in General Metrics](https://doi.org/10.4230/LIPIcs.ICALP.2023.37)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0998 — Fast merging of summaries for symmetric streaming computations

The input statistic is a total Boolean function invariant under reordering the stream. A streaming program computes it using polylogarithmic memory and time per item. The selected question asks for equally efficient local summaries and merging on every binary aggregation tree. A known simulation preserves small space but can use superpolynomial merge time. The target excludes promise and randomness separations and does not require identical intermediate summaries.

[Read in atlas](index.html#TCS-0998) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:19) · [On Distributing Symmetric Streaming Computations](https://research.google.com/pubs/archive/32614.pdf) · [Turnstile Streaming Algorithms Might (Still) as Well Be Linear Sketches, for Polynomial-Length Streams](https://arxiv.org/abs/2604.22052)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7336 — Common2 membership of FIFO queues

Several named processes repeatedly insert arbitrary items into a first-in-first-out queue and remove the oldest remaining item. Only atomic read/write registers and initially unused test-and-set bits are available, with no fixed memory-capacity limit. For every fixed process count, the question asks for a deterministic implementation in which every continuing process finishes each operation despite arbitrary interference or crashes. Correctness requires ordinary linearizability, allowing a legal sequential explanation of every history without demanding one prefix-preserving choice across histories. Known restricted-role queues and impossibility theorems under strong linearizability do not settle this unrestricted target.

[Read in atlas](index.html#TCS-7336) · [Nontrivial and Universal Helping for Wait-Free Queues and Stacks](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2015.31) · [Common2 Extended to Stacks and Unbounded Concurrency](https://www.cs.tau.ac.il/~mad/publications/podc06.pdf) · [Two-enqueuer queue in Common2](https://arxiv.org/abs/0805.0444v2) · [Efficient Wait-Free Queue Algorithms with Multiple Enqueuers and Multiple Dequeuers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2022.4) · [Preserving hyperproperties of programs using primitives with consensus number 2](https://doi.org/10.1007/s00236-025-00500-3) · [Impossibility Results for Strong Linearizability: The Difficulty of Consistent Refereeing](https://arxiv.org/abs/2506.18401v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0515 — Deterministic volume gap

The VOLUME model measures how many graph vertices an adaptive local algorithm inspects to determine one requested output. Outputs from separate queries must still fit together into a single valid labeling. The conjecture says every deterministic locally checkable problem with sublinear worst-case volume actually has O(log-star n) volume. It concerns fixed bounded-degree graph families with exact size information and polynomially bounded identifiers. Proving the collapse would eliminate an entire intermediate range of deterministic local information complexity, despite the richer range available to randomized algorithms.

[Read in atlas](index.html#TCS-0515) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [The randomized local computation complexity of the Lovász local lemma](https://arxiv.org/abs/2103.16251v2) · [The Landscape of Distributed Complexities on Trees and Beyond](https://arxiv.org/abs/2202.04724v2) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [New Complexity Classes in Locally Checkable Labeling for Local Computation Algorithms](https://arxiv.org/abs/2607.09626v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0993 — Factor-two graph distances in logarithmically many passes

The problem asks for a factor-two estimate of one specified distance in an undirected unweighted graph stream. The source and target are known in advance, and every pass sees the same arbitrary edge order. The algorithm may use n times a fixed polylogarithmic number of bits but only logarithmically many passes. Published 2026 bounds leave this target between a near-logarithmic lower bound and a larger upper bound. A resolution would clarify how repeated sequential access recovers global graph distances with limited memory.

[Read in atlas](index.html#TCS-0993) · [Problem 14: Graph Distances](https://sublinear.info/index.php?title=Open_Problems:14) · [Better Bounds for Semi-Streaming Single-Source Shortest Paths](https://doi.org/10.1137/1.9781611978971.184)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7010 — Linear-sketch complexity of the nuclear norm

The nuclear norm of a matrix is the sum of its singular values. The question asks for the smallest number of randomized exact real linear measurements that suffice to approximate this norm for every fixed input matrix. The requested answer must give matching upper and lower bounds up to constant factors for each fixed relative accuracy. Published results separate this matrix problem from ordinary vector norms, bilinear sketches and finite-bit streaming complexity. An August 2026 preprint claims near-quadratic bounds but leaves logarithmic factors unresolved, and its proof is not independently verified by this review.

[Read in atlas](index.html#TCS-7010) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357) · [On Approximating Matrix Norms in Data Streams](https://doi.org/10.1137/17M1152255) · [Near-Optimal Bounds for Sketching the Schatten Norms](https://arxiv.org/abs/2608.22247v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5795 — One-pass semi-streaming depth-first search

The input is an arbitrary-order stream of edges of a connected undirected graph. The task is to output any DFS spanning tree in one pass using nearly linear bit memory. The tree must place the endpoints of every graph edge in an ancestor relationship, beyond ordinary connectivity. The original paper gives many-pass tradeoffs, while practical one-pass observations apply only to evaluated or special inputs. Current status remains uncertain because a later introductory lower-bound assertion was not substantiated by its cited results.

[Read in atlas](index.html#TCS-5795) · [Streaming Complexity of Spanning Tree Computation](https://doi.org/10.4230/LIPIcs.STACS.2020.34) · [Engineering Semi-streaming DFS algorithms](https://arxiv.org/abs/2406.03922) · [Constructing Long Paths in Graph Streams](https://doi.org/10.4230/LIPIcs.ESA.2025.22) · [Sublinear Algorithms for \((\Delta+1)\) Vertex Coloring](https://arxiv.org/abs/1807.08886) · [Independent Sets in Vertex-Arrival Streams](https://doi.org/10.4230/LIPIcs.ICALP.2019.45)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5797 — Local certificate size versus verification radius

Local certification assigns a short proof string to every vertex so that a global graph property can be checked from nearby information. The selected model has no identifiers or input labels, and certificate bounds must hold uniformly over all finite graphs. For each initial bit budget and verification radius, the target is the largest minimum certificate size among properties certifiable within that budget at radius one. The source asks whether certificate size always scales inversely with radius; this card explicitly asks for the full underlying worst-case function. Determining the function would quantify when greater local visibility can replace stored proof information, with a Lean-certified error of at most one hundredth of a bit at every parameter pair.

[Read in atlas](index.html#TCS-5797) · [Local Certification of Local Properties: Tight Bounds, Trade-Offs and New Parameters](https://doi.org/10.4230/LIPIcs.STACS.2024.21) · [Decreasing verification radius in local certification](https://doi.org/10.1016/j.tcs.2025.115520) · [Complexity Landscape for Local Certification](https://doi.org/10.4230/LIPIcs.DISC.2025.18)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7259 — Two-dimensional sandpile prediction in NC

A stable rectangular array contains at most three grains at each cell and is surrounded by an infinite empty lattice. Adding one grain triggers simultaneous topplings, each sending one grain in each of the four cardinal directions. The question asks whether a specified cell ever topples, without giving a time bound in the input. The desired computation uses one uniform family of polynomial-size, polylogarithmic-depth Boolean circuits on the full explicit input. Known results for other dimensions, weighted grids, boundary sinks or alternating update schemes do not settle this precisely specified planar question.

[Read in atlas](index.html#TCS-7259) · [Timed Prediction Problem for Sandpile Models](https://arxiv.org/abs/2506.21084v1) · [The Computational Complexity of Sandpiles](https://arxiv.org/abs/cond-mat/9808183) · [Non-Uniform and Weighted Crossing Gates in Two-Dimensional Sandpiles](https://arxiv.org/abs/2606.26943v1) · [Embedding arbitrary Boolean circuits into fungal automata with arbitrary update sequences](https://arxiv.org/abs/2602.19477v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0986 — Characterizing separable distances approximable in small streaming space

A local nonnegative cost φ defines a dissimilarity by summing over corresponding frequency coordinates. The stream may insert and delete frequencies while keeping both vectors nonnegative. The selected task classifies exactly which effectively evaluable costs admit polylogarithmic-space relative approximations. The criterion must cover the entire specified domain and include both algorithms and impossibility proofs. Known offset obstructions, difference-based aggregate classifications and norm-sketching results cover only parts of this domain.

[Read in atlas](index.html#TCS-0986) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:5) · [Streaming Space Complexity of Nearly All Functions of One Variable on Frequency Vectors](https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/bcwy16.pdf) · [The Andoni–Krauthgamer–Razenshteyn Characterization of Sketchable Norms Fails for Sketchable Metrics](https://arxiv.org/abs/1810.04321)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6080 — Linear-round weighted APSP in CONGEST

Every node in a weighted network must learn its exact distance to every other node. Messages are limited to logarithmically many bits per edge and round, with communication only along the input network. The target is a uniform randomized algorithm using a truly linear number of rounds and succeeding globally with constant probability. A linear lower bound and a randomized near-linear upper bound are known, leaving factors hidden by polylogarithmic notation. A complete answer must prove the literal linear bound or rule it out in this same model.

[Read in atlas](index.html#TCS-6080) · [Quadratic and Near-Quadratic Lower Bounds for the CONGEST Model](https://doi.org/10.4230/LIPIcs.DISC.2017.10) · [Distributed Exact Weighted All-Pairs Shortest Paths in Near-Linear Time](https://arxiv.org/abs/1811.03337) · [Message Optimality and Message-Time Trade-offs for APSP and Beyond](https://arxiv.org/abs/2504.21781)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0469 — Maximum independent set in the congested clique

An exact maximum independent set contains as many pairwise nonadjacent vertices as possible. Each vertex initially knows its incident edges and can exchange a logarithmic number of bits with every other processor in a round. The target is the optimal worst-case number of deterministic communication rounds, with local computation uncharged. A tight bound would measure the information exchange needed for exact graph optimization in a network without distance barriers. The source leaves bandwidth and randomness broader, while this card preserves its explicit deterministic logarithmic-bandwidth specialization.

[Read in atlas](index.html#TCS-0469) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume15/issue05/25191/html/DagRep.15.5.1/DagRep.15.5.1.html) · [On the Power of the Congested Clique Model](https://www.cs.tau.ac.il/~roshman/papers/podc14_clique.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0519 — Bipartite maximal matching with polynomial-in-degree volume

A maximal matching is a collection of disjoint edges to which no additional edge can be added. A vertex query may inspect the graph only by following ports from vertices it has already visited. The input supplies the two sides of the bipartite graph, and separate queries must describe one consistent matching. The question asks for one deterministic algorithm whose visited volume is polynomial in the degree bound and independent of graph size. The February 2026 primary list retains this question between known linear and superpolynomial degree-dependent bounds.

[Read in atlas](index.html#TCS-0519) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [Truly Tight-in-\(\Delta\) Bounds for Bipartite Maximal Matching and Variants](https://arxiv.org/abs/2002.08216v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-2233 — Superlinear local certificates for hereditary graph classes

A prover gives each vertex a binary certificate, and each vertex checks only its immediate certified neighborhood. The question asks for a hereditary graph class requiring a fixed polynomial factor more than linear certificate length at some vertex. The lower bound must hold against every correct proof-labeling verifier and every sufficiently large graph size. Known geometric examples require linear certificates, while a quadratic upper bound applies to all graph classes in the source model. The February 2026 revision still asks whether any hereditary class crosses this polynomially superlinear threshold.

[Read in atlas](index.html#TCS-2233) · [Local Certification of Geometric Graph Classes](https://doi.org/10.4230/LIPIcs.MFCS.2024.48) · [Local certification of geometric graph classes](https://arxiv.org/abs/2311.16953)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6125 — Linear CONGEST lower bound with logarithmic LOCAL complexity

An LCL specifies legal output labels by a finite list of constant-radius neighborhoods. The question asks for one problem that is solvable in logarithmic deterministic LOCAL time but needs linear randomized CONGEST time. Both models communicate along the same bounded-degree graph, while CONGEST restricts each message to logarithmically many bits. Such a result would isolate an extreme cost of bandwidth despite local verifiability of solutions. The card requires all connected inputs without additional promises and states the identifiers, private randomness and global error convention explicitly.

[Read in atlas](index.html#TCS-6125) · [Locally Checkable Labelings with Small Messages](https://drops.dagstuhl.de/doi/10.4230/LIPIcs.DISC.2021.8) · [Locally Checkable Labelings with Small Messages](https://jukkasuomela.fi/doc/lcl-congest.pdf) · [It does not matter how you define locally checkable labelings](https://arxiv.org/abs/2602.18188) · [It does not matter how you define locally checkable labelings](https://jukkasuomela.fi/lcl-definitions/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0940 — Lifting CSP sketching resistance to sublinear streaming resistance

Each fixed predicate family defines a maximum constraint-satisfaction problem. A nontrivial approximation beats the best constant lower bound on the optimum by a fixed amount. The conjecture lifts resistance to small mergeable sketches into resistance to all sublinear-space streaming algorithms. Both the algorithm model and the space threshold change in the implication. The 2026 LP-gap lower bounds are recorded without claiming a verified resolution of this exact lifting statement.

[Read in atlas](index.html#TCS-0940) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf) · [Sketching Approximability of All Finite CSPs](https://arxiv.org/abs/2105.01161) · [Optimal Single-Pass Streaming Lower Bounds for Approximating CSPs](https://eccc.weizmann.ac.il/report/2026/054/)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7337 — Register space of obstruction-free set agreement

Each process proposes a value and must decide one of the values proposed by participating processes. At most k distinct values may be decided, and a process must finish if it continues alone long enough. The resource is the number of atomic read/write registers, whose individual capacities are unrestricted. Known bounds range from the ceiling of n/k to n-k+1; consensus and (n-1)-set agreement have exact values. The target is the full register-space function for all n>k>=1, with the atlas's pointwise 1/100-register acceptance tolerance.

[Read in atlas](index.html#TCS-7337) · [Revisionist Simulations: A New Approach to Proving Space Lower Bounds](https://epubs.siam.org/doi/10.1137/20M1322923) · [Revisionist Simulations: A New Approach to Proving Space Lower Bounds (preprint)](https://arxiv.org/abs/1711.02455v5) · [Anonymous Obstruction-Free \((n,k)\)-Set Agreement with \(n-k+1\) Atomic Read/Write Registers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2015.18) · [Solving Tasks with Fewer Registers Than Processes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2025.21) · [How Exhaustive Does an Extension-Based Proof Need to Be?](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2025.29)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2997 — Triangle detection in CONGEST

Triangle detection asks a distributed network to report whether any three vertices are pairwise adjacent. In CONGEST, each edge transmits only \(O(\log  n)\) bits per round, even though vertices initially know all their own neighbors. The saved card asks for the optimal randomized round complexity between the stated doubly logarithmic lower bound and roughly \(n^{1/3}\) upper bound. Detection needs only one positive witness somewhere in the network, unlike listing every triangle. The challenge is to exploit that smaller output requirement while still communicating enough information to discover an edge between two neighbors.

[Read in atlas](index.html#TCS-2997) · [Distributed Subgraph Finding — ADGA 2025](https://adga-workshop.org/2025/keren.pdf) · [Distributed Triangle Detection is Hard in Few Rounds](https://arxiv.org/abs/2504.01802) · [Near-optimal Distributed Triangle Enumeration via Expander Decompositions](https://doi.org/10.1145/3446330)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7376 — Polylogarithmic-space streaming Euclidean MST estimation

Points arrive one at a time in Euclidean space, and the goal is to estimate the cost of connecting them by a minimum spanning tree. The algorithm gets one insertion-only pass and may keep only memory polynomial in the dimension and the logarithmic input parameters. It should return a constant-factor estimate with probability at least two thirds for every input order. The cited paper leaves a gap between its sublinear-space constant-factor result and this smaller memory budget. The question asks how compactly one can summarize global geometric connectivity, without requiring the summary to output the tree itself.

[Read in atlas](index.html#TCS-7376) · [Community proposal: Streaming Euclidean MST to constant factor in space polylogarithmic in the number of points](https://github.com/vaclavrozhon/atlas/issues/2) · [Streaming Euclidean MST to a Constant Factor](https://doi.org/10.1145/3564246.3585168)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0984 — Optimal measurements and near-linear decoding for universal ℓ₂/ℓ₁ sparse recovery

A fixed matrix compresses every real signal to a short vector of linear measurements. The decoder must work for all signals with error controlled by the best k-sparse ℓ₁ tail divided by √k. The conjecture combines O(k log(en/k)) measurements with near-linear deterministic decoding. The arithmetic model permits input-independent polynomial preprocessing but charges decoding accesses. Faster results with an ℓ₁ reconstruction error or only per-input randomized success do not meet this target.

[Read in atlas](index.html#TCS-0984) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:24) · [For-all Sparse Recovery in Near-Optimal Time](https://arxiv.org/abs/1402.1726)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6501 — Constant-round MIS in the congested clique

A maximal independent set contains no adjacent selected vertices and gives every unselected vertex a selected neighbor. Each processor starts with its own incident input edges and can send separate short messages to every other processor. The target is a uniform randomized algorithm using a constant number of rounds on every graph. Its output must be globally correct with an arbitrarily requested fixed polynomially small failure probability. The checked literature gives constant rounds for restricted graph classes and for distance-two coverage, leaving the general MIS target unresolved.

[Read in atlas](index.html#TCS-6501) · [When MIS and Maximal Matching are Easy in the Congested Clique](https://arxiv.org/abs/2502.21031) · [Improved Massively Parallel Computation Algorithms for MIS, Matching, and Vertex Cover](https://arxiv.org/abs/1802.08237v4) · [Time and Space Optimal Massively Parallel Algorithm for the 2-Ruling Set Problem](https://doi.org/10.4230/LIPIcs.DISC.2023.11)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0994 — Constant-pass weighted matching with O(n log n) bits

The input is an arbitrary-order insertion stream of a positively weighted general graph. The algorithm must output a nearly maximum-weight matching after a number of passes independent of graph size. The retained space target is O(n log n) bits with polynomially bounded integer weights. Linear-time RAM approximation and broader constant-pass semi-streaming results are already known. The card distinguishes those achievements from the exact bit-space endpoint it asks to settle.

[Read in atlas](index.html#TCS-0994) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:16) · [Linear-Time Approximation for Maximum Weight Matching](https://web.eecs.umich.edu/~pettie/papers/ApproxMWM-JACM.pdf) · [Weighted Matchings via Unweighted Augmentations](https://arxiv.org/abs/1811.02760) · [(1−ε)-Approximate Maximum Weighted Matching in Distributed, Parallel, and Semi-Streaming Settings](https://arxiv.org/abs/2212.14425) · [A Simple (1−ε)-Approximation Semi-Streaming Algorithm for Maximum (Weighted) Matching](https://theoretics.episciences.org/16269)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0524 — LOCAL coloring below square-root degree dependence

A proper coloring with Delta plus one colors always exists for a graph of maximum degree Delta. The question asks for a deterministic LOCAL algorithm running in O(\(Delta^{0.499}\) plus log-star n) rounds. The degree exponent deliberately lies just below one half, while the network-size dependence retains the small symmetry-breaking term. Processors must reduce a large identifier-based palette without causing conflicts among adjacent vertices acting simultaneously. Crossing this degree threshold would improve the coordination of dense local neighborhoods without paying a larger dependence on the total number of vertices.

[Read in atlas](index.html#TCS-0524) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#local) · [Local Conflict Coloring Revisited: Linial for Lists](https://arxiv.org/abs/2007.15251) · [Faster Distributed Delta-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0950 — Randomized parity sketches versus one-way communication for XOR functions

The input is an arbitrary Boolean function on a binary vector space. A parity sketch measures a fixed random collection of linear forms and then decodes their bits. A one-way protocol may instead send any randomized message about Alice’s vector to Bob. The conjecture asks whether parity sketches lose only a universal polylogarithmic factor for the associated XOR function. Known deterministic and uniform-input comparisons do not establish the required worst-input randomized bound.

[Read in atlas](index.html#TCS-0950) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:78) · [Linear Sketching over F₂](https://doi.org/10.4230/LIPIcs.CCC.2018.8) · [Turnstile Streaming Algorithms Might (Still) as Well Be Linear Sketches, for Polynomial-Length Streams](https://arxiv.org/abs/2604.22052)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0849 — Two-stage group testing with arithmetic progressions

A hidden set of at most k positions must be identified by noiseless yes/no tests. Every first-stage pool must be an arithmetic progression fixed before any answers are seen. After receiving those answers, the scheme may query only O(k) individual positions in one final stage. The question asks whether O(k log n) first-stage tests suffice for every hidden set, improving the bound reported in the 2009 source by one logarithmic factor. The restriction models regularly spaced queries motivated by pattern matching, and unrestricted pooling results do not settle it.

[Read in atlas](index.html#TCS-0849) · [Problem 33: Group Testing](https://sublinear.info/index.php?title=Open_Problems:33) · [Optimal Two-Stage Algorithms for Group Testing Problems](https://doi.org/10.1137/S0097539703428002)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0980 — Random Walks

The task is to simulate a long random walk on a graph presented as an edge stream. The source asks whether nearly linear memory can reduce the number of passes to a polylogarithmic function of graph size and walk length. It also asks for the complexity of approximating the walk's endpoint distribution and identifying its most likely vertices. These tasks may require less information than producing every step of the trajectory. A resolution would clarify how effectively repeated scans can substitute for direct access to the transition choices of a large graph.

[Read in atlas](index.html#TCS-0980) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0985 — Streaming space for additive \(L_\infty\) estimation

The output is a single estimate of the largest absolute coordinate of a streamed frequency vector. The allowed additive error is one over k times the final L1 or L2 norm. Insertion-only streams and signed differences of two streams are distinct modes of the same resource question. The target is a tight bit-space characterization in the domain size, update budget and accuracy. A 2016 paper reports resolving the insertion-only L1 part, while this review does not certify a complete characterization of all cases.

[Read in atlas](index.html#TCS-0985) · [Open Problem 3: L-infinity Estimation](https://sublinear.info/3) · [An Optimal Algorithm for l1-Heavy Hitters in Insertion Streams and Related Problems](https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/bdw16.pdf)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-0834 — Estimating a Graph's Degree Distribution

A graph's degree distribution records how common vertices of different degrees are. The source entry asks how this distribution can be estimated without reading the entire graph. Sampling vertices uniformly and sampling endpoints of edges can produce different biases. An efficient estimator would summarize network structure while carefully accounting for the information supplied by the access model. The saved title does not specify allowed queries, additive or multiplicative accuracy, or how rare degrees are treated, so a precise sample-complexity target cannot yet be assigned.

[Read in atlas](index.html#TCS-0834) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:98)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0836 — Non-Adaptive Group Testing

Group testing identifies a small set of special items by querying whether selected pools contain any of them. A non-adaptive strategy chooses all pools before observing any answers. The saved question concerns the cost of achieving identification under that restriction. Determining the best constructions would clarify how much one loses by requiring tests to run simultaneously. The inherited label does not state whether answers are noisy, whether recovery is exact, or the number of special items, so the intended tradeoff among tests and error remains unspecified.

[Read in atlas](index.html#TCS-0836) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:95)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1588 — Characterizing robustly computable predicates and functions

Continuous chemical reaction networks represent inputs and outputs as nonnegative concentrations evolving under mass-action kinetics. Robust computation requires convergence to the correct answer for every positive choice of reaction-rate constants. The source constructs robust networks for multithreshold predicates and a specified class of piecewise floor-affine functions, where negative affine values are truncated to zero. It conjectures that these constructions describe exactly the predicates and functions the model can compute. A matching impossibility theorem would turn the positive constructions into a complete characterization of computation that is insensitive to kinetic parameters.

[Read in atlas](index.html#TCS-1588) · [Robust Predicate and Function Computation in Continuous Chemical Reaction Networks](https://doi.org/10.4230/LIPIcs.DISC.2025.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2470 — Breaking the quadratic color bound for bounded outdegree

The network comes with an orientation having at most \(\beta\) outgoing edges at every vertex. A deterministic distributed algorithm can already color it with \(O(\beta ^{2})\) colors in \(O(\log * n)\) rounds. The question is whether \(\beta ^{2}\) can be replaced by \(\beta ^{2- \varepsilon}\) for one fixed \(\varepsilon >0\). Additional time may depend arbitrarily on \(\beta\), but the dependence on n must remain additive \(O(\log * n)\). New results for list and defective colorings have not supplied this proper-coloring guarantee.

[Read in atlas](index.html#TCS-2470) · [List Defective Colorings: Distributed Algorithms and Applications](https://doi.org/10.4230/LIPIcs.DISC.2023.22) · [Greedy-Like Defective Coloring: Distributed Algorithms and Applications](https://arxiv.org/abs/2608.02386)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2753 — Fully adaptive strong Byzantine agreement with optimal resilience

Strong Byzantine agreement requires correct processes to agree while preserving the strong validity condition even when some participants behave arbitrarily. Here adaptivity refers to communication that scales with the actual number f of faulty processes, rather than only the tolerated maximum t. The source asks for a fully adaptive strong-agreement algorithm with optimal resilience \(n = 2t + 1\). Its constructions achieve \(O(n(f+1))\) communication for broadcast and weak agreement, but the strong version becomes quadratic once failures occur. Closing that gap would retain optimal fault tolerance while making communication economical in executions with only a few faults.

[Read in atlas](index.html#TCS-2753) · [Make Every Word Count: Adaptive Byzantine Agreement with Fewer Words](https://doi.org/10.4230/LIPIcs.OPODIS.2022.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3075 — RNC sampling for determinant-counted objects

Several combinatorial families admit determinant formulas that make counting possible in efficient parallel complexity classes. Producing a random object from those families is harder to parallelize because standard counting-to-sampling reductions make sequential choices. After giving an RNC sampler for directed rooted spanning trees, the source asks for analogous samplers for the remaining determinant-counted structures. Examples include planar perfect matchings, determinantal point processes, and Eulerian tours, whose connection to arborescences does not immediately yield a parallel reduction. Resolving these cases would explain whether fast parallel counting can generally be converted into equally parallel random generation.

[Read in atlas](index.html#TCS-3075) · [Sampling Arborescences in Parallel](https://doi.org/10.4230/LIPIcs.ITCS.2021.83)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3381 — Polynomial-state protocols for Presburger arithmetic

Population protocols compute through repeated interactions of finite-state agents. Presburger arithmetic describes exactly the predicates expressible by these protocols, but equivalent representations can have very different sizes. The question asks whether every arithmetic formula, including quantified ones, has a protocol with only polynomially many states in its formula length. The source distinguishes existence of such a compact protocol from the complexity of constructing it. The project studies representational succinctness at the interface between logical specifications and distributed computation.

[Read in atlas](index.html#TCS-3381) · [Succinct Population Protocols for Presburger Arithmetic](https://doi.org/10.4230/LIPIcs.STACS.2020.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3384 — Approximate matching and set packing in \(\mathrm{AC}^{0}\)

Constant-depth \(\mathrm{AC}^{0}\) circuits offer a highly parallel but weak model of computation with unbounded-fan-in Boolean gates. The source asks whether they can output useful approximate matchings, and more generally approximate set packings. This is a search question about producing disjoint edges or sets, rather than merely estimating the optimum value. The paper obtains shallow-circuit approximations of packing size but explains why extracting an actual packing is a different obstacle, even on simple bipartite inputs. Resolving the search problem would distinguish numerical approximation from constructing compatible choices under severe limits on computational depth.

[Read in atlas](index.html#TCS-3384) · [Kernelizing the Hitting Set Problem in Linear Sequential and Constant Parallel Time](https://doi.org/10.4230/LIPIcs.SWAT.2020.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3416 — Wait-free exact FIFO queues in Common\(_{2}\)

The question asks for an exact FIFO queue shared by any fixed finite number of processes. Every process may enqueue and dequeue, and each operation must finish in finitely many of its own steps despite other processes stopping. Only read/write registers and Test&Set bits are supplied. Relaxed queues and algorithms that merely guarantee system-wide progress do not meet this requirement. The checked 2026 impossibility concerns strong linearizability, so the ordinary Common\(_{2}\) question remains open in the cited sources.

[Read in atlas](index.html#TCS-3416) · [Relaxed Queues and Stacks from Read/Write Operations](https://doi.org/10.4230/LIPIcs.OPODIS.2020.13) · [Nontrivial and Universal Helping for Wait-Free Queues and Stacks](https://doi.org/10.4230/LIPIcs.OPODIS.2015.31) · [Set-Linearizable Implementations from Read/Write Operations: Sets, Fetch &Increment, Stacks and Queues with Multiplicity](https://doi.org/10.1007/s00446-022-00440-y) · [Impossibility Results for Strong Linearizability: The Difficulty of Consistent Refereeing](https://doi.org/10.1145/3796701.3815906)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3792 — Deterministic linearizable objects for set agreement

Set agreement lets n processes decide at most k proposed values. Its task has an equivalent linearizable object and an equivalent deterministic object, but these known objects do not possess both properties. The conjecture says no object can possess both properties while retaining exactly the task’s implementation power whenever \(n>k>2\). Equivalence uses deterministic wait-free reductions with registers and allows repeated operations through n ports. The source proves the analogous separation for \(k=2\) and \(n\ge 4\); later existential object separations do not settle the universal higher-k question.

[Read in atlas](index.html#TCS-3792) · [On Deterministic Linearizable Set Agreement Objects](https://doi.org/10.4230/LIPIcs.OPODIS.2019.16) · [On the Number of Objects with Distinct Power and the Linearizability of Set Agreement Objects](https://doi.org/10.4230/LIPIcs.DISC.2017.12) · [Life beyond set agreement](https://doi.org/10.1007/s00446-020-00372-5)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4193 — LOCAL lower bounds for 2-ruling sets

A two-ruling set is an independent set such that every graph vertex lies within distance two of a selected vertex. This relaxes maximal independent set, which requires domination already at distance one. The question asks whether established LOCAL-model round lower bounds for maximal independent set extend to two-ruling sets. Extra domination distance gives algorithms more freedom, so a lower bound must survive that relaxation rather than simply reuse an MIS instance. Resolving the comparison would show whether much of the symmetry-breaking difficulty lies in independence itself or in the stronger requirement to dominate immediate neighbors.

[Read in atlas](index.html#TCS-4193) · [Symmetry Breaking in the Congest Model: Time- and Message-Efficient Algorithms for Ruling Sets](https://doi.org/10.4230/LIPIcs.DISC.2017.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4231 — Complexity of general subgraph detection

Distributed subgraph detection asks whether a network contains a fixed constant-size graph H as a subgraph. The source asks whether every such target can be detected in \(O(n) \mathrm{CONGEST}\) rounds or whether some targets require superlinear time. A linear bound is easy for cliques, despite their prominence as hard patterns in centralized computation. Other patterns can distribute their relevant edges across distant parts of the communication network in different ways, so centralized hardness is a poor guide. A general upper bound or a superlinear example would establish a basic classification boundary for exact distributed pattern detection.

[Read in atlas](index.html#TCS-4231) · [Deterministic Subgraph Detection in Broadcast CONGEST](https://doi.org/10.4230/LIPIcs.OPODIS.2017.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4274 — Subpolynomial detection of two-connected patterns

The question asks whether any fixed 2-vertex-connected graph can be detected in subpolynomial CONGEST rounds. Nodes can exchange only logarithmically many bits per edge per round. Exact detection requires one node to signal an existing copy and all nodes to stay negative when none exists. Trees have constant-round algorithms, while many cyclic patterns have polynomial lower bounds. The newer logarithmic lower bound for triangles leaves the requested subpolynomial-versus-harder boundary unresolved.

[Read in atlas](index.html#TCS-4274) · [Lower Bounds for Subgraph Detection in the CONGEST Model](https://doi.org/10.4230/LIPIcs.OPODIS.2017.6) · [Distributed Subgraph Finding: Progress and Challenges](https://arxiv.org/abs/2203.06597) · [Distributed Triangle Detection is Hard in Few Rounds](https://arxiv.org/abs/2504.01802)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4763 — Work-efficient parallel approximate flow

Parallel flow algorithms seek small total work and short dependency depth while approximating an optimum flow value or cost. The question asks for nearly linear work and polylogarithmic depth for either edge-capacitated minimum-cost flow or vertex-capacitated maximum flow with approximation \(1 + \varepsilon\). The source works on undirected graphs and obtains almost-linear work with subpolynomial depth, leaving a gap between subpolynomial and polylogarithmic guarantees. Existing shortest-path and edge-capacitated maximum-flow results motivate trying to remove that gap. A solution would make richer capacity and cost models as parallelizable as these more established flow primitives.

[Read in atlas](index.html#TCS-4763) · [Parallel \((1+e)\)-Approximate Multi-Commodity Min-Cost Flow in Almost Optimal Depth and Work](https://doi.org/10.1109/FOCS63196.2025.00099)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5427 — Characterizing multipass turnstile streaming

Turnstile streaming algorithms process positive and negative updates to an underlying vector while storing a compact state. For one pass, the source discusses a characterization showing that general algorithms can be replaced by suitable linear sketches under stated correctness assumptions. The question asks whether a comparable characterization exists when several passes over the stream are allowed. Later passes can adapt to information gathered earlier, so a fixed linear summary may no longer capture all useful interactions. A structural theorem would simplify lower bounds and explain whether repeated access fundamentally expands the kinds of compact information a streaming algorithm needs.

[Read in atlas](index.html#TCS-5427) · [New Characterizations in Turnstile Streams with Applications](https://doi.org/10.4230/LIPIcs.CCC.2016.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6206 — Clique detection in CONGEST

In \(\mathrm{CONGEST}_{b}\), each graph edge carries at most b bits per communication round. The source studies detecting cliques with size at least four and up to order \(\sqrt{n}\), asking how far the round complexity exceeds its roughly \(\sqrt{n}/b\) lower-bound scale. A linear-round algorithm leaves a substantial gap, particularly for fixed clique sizes. The paper proves that its two-party vertex-partition method cannot establish the stronger lower bounds that would close that gap. The project therefore calls for improved detection algorithms or new communication-hardness techniques that capture interactions among more than the two partitioned views.

[Read in atlas](index.html#TCS-6206) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6380 — Load-optimal parallel natural joins

A natural join combines database relations by matching equal values on shared attributes. In massively parallel computation, the load measures how much data any one of p machines must handle. The question asks for algorithms matching the \(\Omega (m/p^{1/\rho})\) load bound for arbitrary join queries, where m is total input size and \(\rho\) is the fractional edge-cover number. The source achieves the target for binary-relation joins in a small constant number of rounds, but those graph-shaped queries do not cover arbitrary relation arities. A general construction would align parallel join execution with the structural lower bound of the query hypergraph.

[Read in atlas](index.html#TCS-6380) · [A Simple Parallel Algorithm for Natural Joins on Binary Relations](https://doi.org/10.4230/LIPIcs.ICDT.2020.25)
Existing status: `uncertain` · Summary written: 2026-09-11

## Optimization and numerical computation (23)

### TCS-0008 — Strongly polynomial linear programming

A rational linear program minimizes a linear objective subject to linear equalities and nonnegative variables. The question asks for one deterministic exact solver using polynomially many scalar arithmetic operations depending only on the numbers of variables and constraints. Intermediate rational values must have bit lengths polynomial in the full input length, and the computation must admit an exact polynomial-time bit implementation. The solver must distinguish infeasibility, an objective unbounded below and a finite attained optimum on every input, without matrix or conditioning promises. Strongly polynomial algorithms are established for major special classes, while current claims of a general solution remain unverified in this review.

[Read in atlas](index.html#TCS-0008) · [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8) · [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250) · [A Strongly Polynomial Algorithm for Linear Programs with At Most Two Nonzero Entries per Row or Column](https://ir.cwi.nl/pub/34290/34290.pdf) · [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186v1) · [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf) · [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10) · [Validation of a recently proposed strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2310.05855v5) · [Linear Programming Problem Solved By a Special Substitution Method](https://arxiv.org/abs/2604.06726v4)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6574 — Exact semidefinite feasibility in polynomial time

The input is a fully listed rational affine symmetric matrix whose dimension and number of real variables are both unbounded. The target is a deterministic polynomial bit-time decision of whether some real substitution makes the matrix positive semidefinite. Singular feasible points, irrational-only feasible parameters, unbounded sets and infeasible instances at zero distance from the cone are included. Known approximation and exact-duality results retain assumptions or model distinctions, and the September 2026 source still states the unrestricted exact complexity as open. A complete Lean proof must establish one polynomial-time decider or exclude all such deciders; it need not output a feasible point or optimization value.

[Read in atlas](index.html#TCS-6574) · [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433) · [On the Turing model complexity of interior point methods for semidefinite programming](https://arxiv.org/abs/1507.03549v2) · [Exact algorithms for semidefinite programs with degenerate feasible set](https://arxiv.org/abs/1802.02834v2) · [How do exponential size solutions arise in semidefinite programming?](https://arxiv.org/abs/2103.00041v2) · [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271v1) · [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440v1) · [Further analysis and extension of the higher-order Newton method of Ahmadi, Chaudhry, and Zhang](https://arxiv.org/abs/2609.01001v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7227 — Conforti–Cornuéjols conjecture

A clutter is a finite family of sets with no redundant containing member. Its packing property requires unweighted packing–covering equality in every deletion and contraction minor. The conjecture asks whether this already implies equality for every nonnegative integer capacity vector. Weighted packings may repeat members within those capacities. Recent source results cover finite ground-set sizes and restricted families, while retaining the general question.

[Read in atlas](index.html#TCS-7227) · [Combinatorial Optimization: Polyhedra and Efficiency](https://homepages.cwi.nl/~lex/co/) · [Testing the max-flow min-cut property and the replication conjecture](https://arxiv.org/abs/2606.16543v2) · [Equality of ordinary and symbolic powers and the Conforti–Cornuéjols conjecture for (n−2)-uniform clutters](https://arxiv.org/abs/2510.15864v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6585 — Nearly linear-time solution of general sparse linear systems

A sparse linear system explicitly stores only the nonzero matrix entries and its right-hand side. The question asks whether every nonsingular rational system with polynomial conditioning can be approximately solved in nearly linear time in the number of nonzeros. Coefficient lengths and residual accuracy are bounded on a logarithmic scale, and the output must list every rational coordinate. The fixed word-RAM model charges preprocessing, precision, randomness and output, with a worst-case time bound and success probability at least two thirds. Known structured solvers and general improvements over matrix multiplication motivate the target but do not provide its universal near-linear guarantee.

[Read in atlas](index.html#TCS-6585) · [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254) · [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430) · [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553) · [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53) · [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6578 — Smale’s seventh problem

Smale's seventh problem concerns placing N points on the unit sphere so that their logarithmic interaction energy is nearly minimal. The target is an algorithm running in time polynomial in N. Its output energy may exceed the global minimum by only a universal constant times log N. This is an additive energy guarantee, which requires more precise control than merely producing visually well-distributed points. A construction with a rigorous bound would connect efficient computation with the equilibrium behavior of many mutually repelling particles on a curved surface.

[Read in atlas](index.html#TCS-6578) · [Logarithmic energy for zeros of random polynomials](https://www.lebesgue.fr/sites/default/files/inline-files/Yakir.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6572 — Polynomial-time simplex pivot rule

Primal simplex maximizes a rational linear objective by exchanging one entering and one leaving basis column at a time. The question asks for one deterministic rule that reaches an optimality-certifying basis from every supplied feasible basis in polynomial total bit time. Each pivot must have positive entering reduced cost and follow the exact minimum-ratio test, with tied and zero-length degenerate pivots included. The rule may inspect all numerical data and use history, but every computation and basis exchange must fit the same polynomial input-length bound. Smoothed guarantees, local antistalling results, restricted-information lower bounds and hardness of shortest pivot paths do not settle this unrestricted rule-existence target.

[Read in atlas](index.html#TCS-6572) · [Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time](https://www.cs.yale.edu/homes/spielman/simplex/) · [An unconditional lower bound for the active-set method on the hypercube](https://arxiv.org/abs/2502.18019v1) · [An unconditional lower bound for the active-set method in convex quadratic maximization](https://arxiv.org/abs/2507.16648v2) · [Lower bounds for ranking-based pivot rules](https://arxiv.org/abs/2512.16684v2) · [On the number of degenerate simplex pivots](https://link.springer.com/article/10.1007/s10107-026-02349-x) · [Finding Short Paths on Simple Polytopes](https://arxiv.org/abs/2603.05482v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7314 — Komlós conjecture

Komlós asks whether every collection of real vectors of Euclidean norm at most one can be assigned signs so that every coordinate of their sum is bounded by one universal constant. The dimensions and entries are arbitrary, and the same complete choice of signs must control all coordinates simultaneously. The positive answer requires some finite constant, without determining the best one or giving an efficient algorithm. Such a theorem would imply the Beck–Fiala discrepancy bound and strengthen rounding and optimization guarantees. A complete Lean proof must establish the universal bound or unbounded discrepancy; the 10 September 2026 preprint claims the full positive bound, but this review has not independently verified its proof.

[Read in atlas](index.html#TCS-7314) · [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961v2) · [An Algorithm for Komlós Conjecture Matching Banaszczyk’s Bound](https://doi.org/10.1137/17M1126795) · [An Exposition of the \(\widetilde O((\log n)^{1/4})\) Bound for the Komlós Problem](https://arxiv.org/abs/2608.28452v1) · [A \((\log n)^{1/4}\) Bound for the Komlós Problem](https://arxiv.org/abs/2609.08885v1) · [Algorithms for Standard-Form ILP Problems via Komlós’ Discrepancy Setting](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.25) · [Vector Balancing via Directional Total Variation](https://arxiv.org/abs/2609.11189v1)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-7231 — P-matrix linear complementarity in polynomial time

The problem asks for nonnegative rational vectors linked by a linear equation, with at least one zero in each paired coordinate. The input matrix is promised to have every nonempty principal minor strictly positive, which guarantees a unique solution for every right-hand side. The question is whether one deterministic algorithm always finds that exact solution in polynomial time measured in the full binary input length. A complete Lean proof must supply that uniform algorithm and bound or rule out every such polynomial-time algorithm without adding a promise-recognition task. The checked 2026 handicap-dependent algorithm and earlier restricted-matrix and reduction results do not establish this general polynomial-time guarantee.

[Read in atlas](index.html#TCS-7231) · [On the number of solutions to the complementarity problem and spanning properties of complementary cones](https://doi.org/10.1016/0024-3795(72)90019-5) · [A Polynomial-Time Algorithm for the Tridiagonal and Hessenberg P-Matrix Linear Complementarity Problem](https://arxiv.org/abs/1112.0217) · [Activity Report 2025: Theory of Combinatorial Algorithms](https://ti.inf.ethz.ch/ew/report/2025.html) · [On the computational equivalence of co-NP refutations of a matrix being a P-matrix](https://arxiv.org/abs/2110.05644) · [Unique End of Potential Line](https://arxiv.org/abs/1811.03841) · [Two Choices Are Enough for P-LCPs, USOs, and Colorful Tangents](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.32) · [Handicap reduction for linear complementarity problems](https://arxiv.org/abs/2605.10701)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7315 — Beck–Fiala conjecture

The Beck–Fiala conjecture asks whether bounded participation of each element in a set system guarantees a coloring with square-root imbalance in every set. If each element belongs to at most t sets, one complete assignment of signs must achieve imbalance at most a universal constant times the square root of t. The constant must work for every number of elements and sets, with no lower restriction on t or requirement for an efficient algorithm. The question is a central sparsity principle for simultaneous rounding and is implied by the more general Komlós conjecture. A complete Lean proof must establish the universal bound or unbounded normalized discrepancy; a 10 September 2026 preprint claims the full positive bound, with its proof unverified in this review.

[Read in atlas](index.html#TCS-7315) · [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961v2) · [Online Beck–Fiala Down to Logarithmic Sparsity](https://arxiv.org/abs/2607.14238v1) · [Vector Balancing via Directional Total Variation](https://arxiv.org/abs/2609.11189v1)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-7283 — Superpolynomial semidefinite extension complexity of perfect matching

The perfect-matching polytope is the convex hull of the incidence vectors of perfect matchings in a complete graph of even order. A semidefinite lift represents that polytope exactly as an affine image of an affine slice of a real positive semidefinite cone. The question asks whether the required matrix order is unbounded by every polynomial in the number of graph vertices, allowing arbitrary real coefficients and separate representations at each size. Exponential bounds for linear lifts and coordinate-symmetric semidefinite formulations leave this unrestricted representation question unresolved in the checked sources. A complete Lean proof must establish the full lower-bound assertion or prove that one polynomial bounds exact semidefinite lifts for the entire family.

[Read in atlas](index.html#TCS-7283) · [Lower Bounds for Interactive Compression and Linear Programs](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content) · [Lifting for Simplicity: Concise Descriptions of Convex Sets](https://arxiv.org/abs/2002.09788v2) · [The matching polytope has exponential extension complexity](https://arxiv.org/abs/1311.2369v4) · [The Matching Problem Has No Small Symmetric SDP](https://arxiv.org/abs/1504.00703v5) · [Lower bounds on the size of semidefinite programming relaxations](https://arxiv.org/abs/1411.6317v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7226 — Woodall’s conjecture

A dicut is a nonempty one-way boundary in a directed graph, and a dijoin is a set of arcs meeting every dicut. The smallest dicut bounds how many pairwise disjoint dijoins can exist. Woodall’s conjecture states that this bound is always attained in the unweighted setting. The card allows parallel arcs, fixes the nontrivial connectivity regime and keeps the statement separate from the false weighted generalization. A proof or counterexample would settle a longstanding integral packing–covering equality beyond known constant-factor and graph-class results.

[Read in atlas](index.html#TCS-7226) · [Combinatorial Optimization: Polyhedra and Efficiency](https://homepages.cwi.nl/~lex/co/) · [Approximately Packing Dijoins via Nowhere-Zero Flows](https://doi.org/10.1007/s00493-025-00159-x) · [A Min-Max Relation on Dicuts and Dijoins in Weighted Chordal Digraphs](https://arxiv.org/abs/2501.10918v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0491 — Log-squared query complexity of fixed-dimensional Tarski fixed points

The input is oracle access to a monotone function on a finite grid of fixed dimension. Each query reveals one full function value, and any exact fixed point is acceptable. The question asks whether the worst-case deterministic query count is bounded by a squared logarithm of side length in every fixed dimension. A March 2026 result establishes that bound in dimension four while leaving the general fixed-dimension question unresolved. Resolving the target would clarify the information needed for monotone fixed-point search without also requiring fast internal computation.

[Read in atlas](index.html#TCS-0491) · [Can the current bounds for computing a Tarski fixed point on a finite (grid) lattice be improved?](https://doi.org/10.4230/DagRep.12.1.101) · [Tarski Lower Bounds from Multi-Dimensional Herringbones](https://arxiv.org/abs/2502.16679) · [The Mystery Deepens: On the Query Complexity of Tarski Fixed Points](https://arxiv.org/abs/2604.00268) · [Quantum Query Complexity of Finding a Tarski Fixed Point on a High-Dimensional Grid](https://arxiv.org/abs/2609.03802)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7298 — Constant-factor entrywise \(\ell_1\) rank-\(k\) approximation with variable \(k\)

The task compresses a rational matrix while measuring error by the sum of absolute entrywise differences. The output must have rank at most the supplied rank and approximate the best real matrix of that rank. Both the approximation factor and polynomial-time exponent must remain independent of the rank. Known fixed-rank approximation schemes do not meet this joint polynomial-time requirement. The question asks whether an absolute constant-factor guarantee is possible with explicit rational output.

[Read in atlas](index.html#TCS-7298) · [A PTAS for ℓp-Low Rank Approximation](https://epubs.siam.org/doi/10.1137/1.9781611975482.47) · [A PTAS for ℓp-Low Rank Approximation](https://arxiv.org/abs/1807.06101v3) · [Entrywise Low-Rank Approximation and Matrix \(p \to  q\) Norms via Global Correlation Rounding](https://arxiv.org/abs/2604.22699v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7007 — Input-sparsity relative spectral low-rank approximation

Spectral low-rank approximation seeks a rank-k representation whose largest directional error is near the best possible. The source asks for a relative-error guarantee in time equal to reading the nonzero matrix entries plus a term linear in n and polynomial in k over epsilon. That speed is available in the cited comparison for Frobenius error, which aggregates squared errors instead of controlling the worst direction. The spectral target is therefore substantially stronger. A solution would make sparse-matrix compression fast while protecting against a large error concentrated in one singular direction.

[Read in atlas](index.html#TCS-7007) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6483 — Superlinear randomized query lower bounds for submodular minimization

A value oracle answers exact evaluations of an unknown submodular set function. The randomized algorithm must find a true global minimizer on every input with constant success probability. The question asks whether the worst-case query requirement grows faster than every constant multiple of the ground-set size. Neither numeric evaluation cost nor local computation is charged. Known deterministic and parallel-round lower bounds do not settle this randomized total-query question.

[Read in atlas](index.html#TCS-6483) · [Improved Lower Bounds for Submodular Function Minimization](https://doi.org/10.1109/FOCS54457.2022.00030) · [New Query Lower Bounds for Submodular Function Minimization](https://arxiv.org/abs/1911.06889)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0724 — Limited-memory convex optimization

First-order convex optimization learns about an objective through queries returning its value and a subgradient. The source asks how the number of queries needed for a prescribed accuracy changes when the algorithm has limited working memory. It highlights methods with strong oracle complexity whose stored geometric information can require quadratic space in dimension. The question is whether that memory cost is inherent or can be traded away without losing the optimal query rate. A sharp tradeoff would distinguish information acquired from the oracle from information that must remain available between optimization steps.

[Read in atlas](index.html#TCS-0724) · [Open Problem: The Oracle Complexity of Convex Optimization with Limited Memory](https://proceedings.mlr.press/v99/woodworth19a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0728 — Smooth convex optimization with different domain and smoothness norms

Smooth convex optimization is often analyzed when the objective's regularity and the feasible region use compatible norms. The source instead studies settings where these geometries differ, including vector norms and their matrix counterparts. It asks for the optimal oracle complexity of minimizing such functions using black-box first-order information. The stated gaps concern how smoothness, domain geometry, dimension, and target accuracy interact. Matching algorithms and lower bounds would show whether sparse and low-rank optimization models permit faster convergence than methods designed around a single common norm suggest.

[Read in atlas](index.html#TCS-0728) · [Open Problem: The Oracle Complexity of Smooth Convex Optimization in Nonstandard Settings](https://proceedings.mlr.press/v40/Guzman15.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5330 — Deterministic near-linear-query approximation schemes for matroid intersection

Two unknown matroids are accessed only by tests of whether a proposed subset is independent. The algorithm must output a large set independent in both matroids. The target is deterministic approximation arbitrarily close to optimum with near-linear query complexity. The guarantee must cover every common rank, without stronger rank queries or matrix representations. Randomized near-linear schemes and a deterministic two-thirds approximation are known.

[Read in atlas](index.html#TCS-5330) · [Deterministic \((2/3 - \varepsilon )\)-Approximation of Matroid Intersection Using Nearly-Linear Independence-Oracle Queries](https://doi.org/10.4230/LIPIcs.WADS.2025.50) · [Efficient Matroid Intersection via a Batch-Update Auction Algorithm](https://doi.org/10.1137/1.9781611978315.18) · [Faster Approximate Linear Matroid Intersection](https://doi.org/10.4230/LIPIcs.SWAT.2026.39)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0722 — Polynomial-time linear convergence for geodesically convex optimization

Geodesically convex optimization replaces straight segments with shortest paths on a Riemannian manifold. The question asks for a deterministic first-order algorithm with query complexity polynomial in dimension and logarithmic in inverse accuracy. It also requires polynomial arithmetic work per query, so a powerful but computationally intractable geometric oracle would not suffice. The source develops an ellipsoid-like approach for constant-curvature spaces and identifies obstacles on more general manifolds. A solution would extend the efficient precision dependence of Euclidean convex optimization to curved spaces while respecting the cost of manipulating their geometry.

[Read in atlas](index.html#TCS-0722) · [Open Problem: Polynomial linearly-convergent method for geodesically convex optimization?](https://proceedings.mlr.press/v195/criscitiello23b.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0687 — Gap-entropy conjecture

The arms have independent Gaussian rewards with unit variance and a unique best mean. The benchmark averages expected sample cost over arm relabelings and takes an infimum over globally correct algorithms. The conjecture predicts that cost from the total inverse-square gaps and the entropy of their scale distribution. It differs from asking one algorithm to attain the benchmark on all instances without an adaptation cost. A 9 September 2026 preprint claims the precise formula; its proof has not been independently certified in this review.

[Read in atlas](index.html#TCS-0687) · [COLT / PMLR](https://proceedings.mlr.press/v49/chen16b.html) · [Towards Instance Optimal Bounds for Best Arm Identification](https://proceedings.mlr.press/v65/chen17b.html) · [A Positive Resolution of the Gap-Entropy Conjecture](https://arxiv.org/abs/2609.10529)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-0725 — Second-order cone lift dimension of semialgebraic convex hulls

A semialgebraic set is described by polynomial equalities and inequalities, while its convex hull collects all convex combinations of its points. The source asks when that convex hull can be represented using second-order cone constraints and auxiliary variables. It also asks how many additional variables such a representation requires. Representability is stronger than having a useful numerical relaxation, because the projected feasible region must agree exactly with the desired hull. A structural answer would identify nonlinear models that can be converted into a tractable conic formulation and quantify the cost of that conversion.

[Read in atlas](index.html#TCS-0725) · [Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization](https://doi.org/10.4230/DagRep.8.2.64)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0914 — Deterministic competitive ratio for matching with delays

Matching with delays pairs arriving requests while charging both the distance between partners and the time each request waits. The selected question asks for the optimal deterministic competitive ratio as a function of the number of points in a known metric. The guarantee must hold for any finite even request sequence, with no bound on its length or advance notice of its end. A SODA 2026 algorithm gives a polylogarithmic ratio in the number of requests, which does not alone determine the ratio uniformly in metric size. Matching bounds in the metric-size parameter would clarify the value of randomization in balancing spatial cost against waiting.

[Read in atlas](index.html#TCS-0914) · [Scheduling](https://doi.org/10.4230/DagRep.10.2.50) · [A Deterministic Polylogarithmic Competitive Algorithm for Matching with Delays](https://doi.org/10.1137/1.9781611978971.144) · [Online Matching with Size-Based and Convex Delays](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.25)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0673 — First-order convergence to local minimax optima

In sequential minimax optimization, one player minimizes a smooth function of x while a second player maximizes it in y. A local minimax point respects this order using shrinking neighborhoods whose radii may differ for the two players. The selected variant asks for one deterministic method with exact function-value and gradient queries whose finite limits are local minimax points for almost every initialization. The same method must converge locally to every strict local minimax point, so avoiding convergence everywhere is not a valid answer. Existing convergence theorems retain extra hypotheses or weaker derivative-based targets, and the exact variant and limits of the current source review are explicitly recorded.

[Read in atlas](index.html#TCS-0673) · [Open Problem: Is There a First-Order Method that Only Converges to Local Minimax Optima?](https://proceedings.mlr.press/v195/chae23a.html) · [What is Local Optimality in Nonconvex-Nonconcave Minimax Optimization?](https://proceedings.mlr.press/v119/jin20e.html) · [Two-timescale Extragradient for Finding Local Minimax Points](https://arxiv.org/abs/2305.16242v2) · [Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements](https://proceedings.mlr.press/v235/kim24m.html) · [On Solving Minimax Optimization Locally: A Follow-the-Ridge Approach](https://arxiv.org/abs/1910.07512v2) · [A first-order method for constrained nonconvex-nonconcave minimax optimization](https://link.springer.com/article/10.1007/s10107-026-02415-4)
Existing status: `uncertain` · Summary written: 2026-09-16

## Geometry, topology and metric spaces (41)

### TCS-6523 — Kannan–Lovász–Simonovits conjecture

The KLS conjecture asks for a universal Poincaré inequality for every log-concave probability distribution with zero mean and identity covariance. Every locally Lipschitz function of finite variance and gradient energy must have its variance bounded by that energy times one constant independent of the dimension and distribution. The target includes uniform distributions on convex bodies and requires no symmetry, independence or positive curvature assumption. Its equivalent expansion principle connects high-dimensional geometry and concentration with the analysis of sampling algorithms. A complete Lean proof must establish the universal bound or its unbounded-counterexample negation; radial, quadratic and dimension-dependent improvements do not settle the full target.

[Read in atlas](index.html#TCS-6523) · [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/) · [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf) · [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551v2) · [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf) · [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2) · [Digesting the proof of the sharp thin-shell inequality](https://arxiv.org/abs/2607.23307v1) · [The KLS constant is \(O((\log n)^{1/4})\)](https://arxiv.org/abs/2607.24164v1) · [Hit-and-Run Mixes as Fast as the Ball Walk](https://arxiv.org/abs/2608.13487v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6525 — Gupta–Newman–Rabinovich–Sinclair conjecture

The GNRS conjecture asks how faithfully shortest-path distances in graphs excluding a fixed minor can be represented in \(\ell\)\(_{1}\). The graph may have arbitrary positive edge lengths, and every pair of vertices must be preserved within a constant factor. This constant may depend on the excluded minor but cannot grow with the graph. Because \(\ell\)\(_{1}\) metrics decompose into weighted cuts, the question also governs multicommodity flow–cut gaps. Even the planar case tests whether a strong topological restriction is enough to remove all growing distortion.

[Read in atlas](index.html#TCS-6525) · [Cuts, Trees and \(\ell\)\(_{1}\)-Embeddings of Graphs](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf) · [Pathwidth, trees, and random embeddings](https://arxiv.org/abs/0910.1409) · [Approximating Sparsest Cut in Graphs of Bounded Treewidth](https://www.wisdom.weizmann.ac.il/~robi/papers/CKR-TreewidthSparsestCut-APPROX10.pdf) · [A face cover perspective to \(\ell\)\(_{1}\) embeddings of planar graphs](https://arxiv.org/abs/1903.02758) · [The exact value of \(c_{1}(K_{2},_{n})\)](https://arxiv.org/abs/2602.23745) · [CS 583: Approximation Algorithms](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6528 — Unknot recognition in polynomial time

Unknot recognition asks whether a closed loop represented by a finite crossing diagram can be deformed into a circle without cutting. A complicated drawing may still represent an unknot, so simplifying visible crossings is not a complete decision method. The target here is a deterministic algorithm whose bit complexity is polynomial in the diagram encoding. The saved card records a September 2026 preprint claiming such an algorithm, with its proof not independently validated. This description therefore preserves the uncertainty around that claim while explaining the computational target.

[Read in atlas](index.html#TCS-6528) · [The Computational Complexity of Knot and Link Problems](https://arxiv.org/abs/math/9807016) · [A polynomial upper bound on Reidemeister moves](https://annals.math.princeton.edu/2015/182-2/p03) · [The efficient certification of knottedness and Thurston norm](https://arxiv.org/abs/1604.00290) · [Unknot recognition in quasi-polynomial time](https://www.maths.ox.ac.uk/node/60914) · [A Practical Algorithm for Knot Factorisation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.55/LIPIcs.SoCG.2025.55.html) · [Incompressible surfaces, hierarchies and unknot recognition](https://arxiv.org/abs/2607.23350) · [Locally Minimal Bridge Presentations of Knots](https://arxiv.org/abs/2609.06492)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6573 — Polynomial Hirsch conjecture

The vertex-edge graph of a convex polyhedron records which feasible vertices can be joined by a single edge move. Its diameter is the largest shortest-path distance between any two vertices. The polynomial Hirsch conjecture asks for one polynomial bound in the number of facets and dimension that works uniformly for every pointed polyhedron. Counterexamples to the original linear Hirsch bound do not refute this weaker polynomial target. Resolving it would constrain the combinatorial geometry of linear programs, although short undirected paths would still not supply an efficient improving simplex rule.

[Read in atlas](index.html#TCS-6573) · [Geometry: Combinatorics and Algorithms 2025 — Chapter 10, Convex Polytopes](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf) · [A counterexample to the Hirsch Conjecture](https://annals.math.princeton.edu/2012/176-1/p07) · [An improved Kalai–Kleitman bound for the diameter of a polyhedron](https://arxiv.org/abs/1402.3579) · [An Asymptotically Improved Upper Bound on the Diameter of Polyhedra](https://link.springer.com/article/10.1007/s00454-018-0016-y) · [Computing the Polytope Diameter is Even Harder than NP-hard (Already for Perfect Matchings)](https://arxiv.org/abs/2502.16398v3) · [Circuit Diameter of Polyhedra is Strongly Polynomial](https://arxiv.org/abs/2602.06958v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0318 — Planar k-set extremal function

A planar k-set is a k-element subset of a point set that one line strictly separates from all remaining points. The target is the maximum number of such subsets over n points with no three collinear. Determine its growth within universal constant factors jointly in n and k, for \(1\le k\le \lfloor n/2\rfloor\). The problem counts subsets rather than separating lines and asks for combinatorial complexity rather than an enumeration algorithm. Both a uniform bound for every point set and matching examples throughout the parameter range are required.

[Read in atlas](index.html#TCS-0318) · [The Open Problems Project: Problem 7, k-sets](https://topp.openproblem.net/p7) · [Improved Bounds for Planar k-Sets and Related Problems](https://courses.cs.duke.edu/cps234/fall08/handouts/dey.pdf) · [Point Sets with Many k-Sets](https://link.springer.com/article/10.1007/s004540010022) · [An Improved, Simple Construction of Many Halving Edges](https://rangevoting.org/many_halving_edges.pdf) · [An Improvement of the Upper Bound for the Number of Halving Lines of Planar Sets](https://oa.upm.es/89576/1/10302927.pdf)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6524 — Lang–Plaut problem

A doubling metric has uniformly limited local branching: each ball can be covered by a bounded number of smaller balls. The Lang–Plaut problem considers such a metric when it already sits inside a Hilbert space. It asks whether the points can be represented in some finite-dimensional Euclidean space while changing all distances by only a bounded factor. Both dimension and distortion should depend only on the doubling constant. The issue is whether intrinsic metric simplicity suffices to eliminate an infinite-dimensional ambient representation.

[Read in atlas](index.html#TCS-6524) · [Assouad’s theorem with dimension independent of the snowflaking](https://web.math.princeton.edu/~naor/homepage%20files/assouad-N%28K%29.pdf) · [Bilipschitz embeddings of metric spaces into space forms](https://doi.org/10.1023/A:1012093209450) · [A doubling subset of \(L_p\) for \(p>2\) that is inherently infinite dimensional](https://web.math.princeton.edu/~naor/homepage%20files/Lp-doubling.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7242 — Decidability of PL four-sphere recognition

The input is a finite triangulation promised to be a closed combinatorial four-dimensional manifold. The task is to recognize the standard piecewise-linear four-sphere. The question asks for a terminating decision algorithm, with no polynomial-time requirement. Recognizing a topological sphere or checking its homology would answer a different question. The problem marks the exceptional dimension between established decidability and undecidability results for sphere recognition.

[Read in atlas](index.html#TCS-7242) · [Frontiers of sphere recognition in practice](https://link.springer.com/article/10.1007/s41468-022-00092-8) · [Applied topology: sphere recognition research presentation](https://page.math.tu-berlin.de/~joswig/presentations/Joswig-Applied%2BTopology-250715.pdf) · [Is there an algorithm to recognize the combinatorial four-sphere?](https://www.openproblemgarden.org/op/is_there_an_algorithm_to_determine_if_a_triangulated_4_manifold_is_combinatorially_equivalent_to_the_4_sphere)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6526 — Optimal size of weak \(\varepsilon\)-nets for convex ranges

A weak \(\varepsilon\)-net places auxiliary points so that every convex set containing at least an \(\varepsilon\) fraction of a given point set contains an auxiliary point. The auxiliary points may lie anywhere in the ambient Euclidean space. For each fixed dimension, the task is to determine the smallest worst-case net size as \(\varepsilon\) decreases. The challenge comes from hitting all sufficiently populated convex regions simultaneously, regardless of the original configuration. Sharp bounds would quantify how economically a finite set can represent its large convex subsets.

[Read in atlas](index.html#TCS-6526) · [An Improved Bound for Weak Epsilon-Nets in the Plane](https://arxiv.org/abs/1808.02686)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0406 — Dürer’s conjecture

The input is a convex three-dimensional polytope. Its faces may be separated only along original edges. The output sought is one connected planar net. Distinct face interiors must not overlap. Allowing cuts across faces or disconnected pieces gives a different problem.

[Read in atlas](index.html#TCS-0406) · [The Open Problems Project: Edge-Unfolding Convex Polyhedra](https://topp.openproblem.net/p9)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6527 — Constant-distortion Steiner point removal

Steiner point removal starts with a weighted graph and a designated set of terminals whose mutual distances matter. The goal is to delete the other vertices through graph-minor operations, leaving a graph on exactly those terminals. Its edges may be reweighted, but terminal distances should never shrink and should grow by at most a universal factor. The same guarantee must work regardless of how many terminals the input contains. This asks whether graph topology and useful terminal geometry can both survive an extreme reduction in representation size.

[Read in atlas](index.html#TCS-6527) · [Shortcut Partitions in Minor-Free Graphs: Steiner Point Removal, Distance Oracles, Tree Covers, and More](https://doi.org/10.1137/1.9781611977912.191)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7184 — Klee’s measure problem

Klee’s measure problem asks for the volume covered by a union of axis-aligned boxes. Overlapping regions count once, and only the exact total volume is required. For each fixed dimension at least three, the question seeks matching worst-case time bounds in a specified arithmetic real-RAM model. Chan’s general upper bound is \(O(n^{d/2})\), with no matching unconditional classification supplied by the checked later work. Recent approximation and dynamic advances answer different questions.

[Read in atlas](index.html#TCS-7184) · [Klee's measure problem made easy](https://doi.org/10.1109/FOCS.2013.51) · [Approximating Klee’s Measure Problem and a Lower Bound for Union Volume Estimation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.25) · [Near-Optimal Dynamic Data Structures for Maximum Depth and Klee’s Measure of Boxes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.34)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7292 — Polynomial-time recognition of the 3-sphere

The input is an explicit finite simplicial complex promised to triangulate a closed connected PL three-manifold. The question asks whether one deterministic algorithm can recognize the standard three-sphere in time polynomial in the total input bit length. The polynomial bound must hold on all binary inputs, while correct answers are required on the promised manifold inputs. Sphere recognition is decidable and has polynomially verifiable positive certificates, with the checked negative-certificate result depending on the generalized Riemann hypothesis. The 2026 K3 problem list retains the polynomial-time question, whose resolution would also affect the complexity of unknot recognition.

[Read in atlas](index.html#TCS-7292) · [Sphere recognition lies in NP](https://sschleimer.warwick.ac.uk/Maths/2011sphere_recog_NP.pdf) · [Integer homology 3-spheres admit irreducible representations in \(\mathrm{SL}(2,\mathbb C)\)](https://arxiv.org/abs/1605.08530v4) · [The efficient certification of knottedness and Thurston norm](https://arxiv.org/abs/1604.00290v3) · [K3: A New Problem List in Low-Dimensional Topology](https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/b/22144/files/2026/04/K3-problem-list-watermarked.pdf) · [The foundations of four-manifold theory in the topological category](https://nyjm.albany.edu/m/2025/6v.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0382 — General unfolding of nonconvex polyhedra

A general unfolding cuts a polyhedral surface along finitely many segments, including segments through faces. The goal is one connected planar piece with no overlap of its uncut surface. The question asks whether every closed embedded polyhedral surface admits such an unfolding, including nonconvex surfaces and surfaces with handles. Convex surfaces and genus-zero orthogonal polyhedra have positive results, while restrictions to original edges or inputs with boundary have counterexamples. A 2025 refolding theorem permits overlap and therefore does not settle this nonoverlapping existence question.

[Read in atlas](index.html#TCS-0382) · [The Open Problems Project, Problem 43: General Unfoldings of Nonconvex Polyhedra](https://topp.openproblem.net/p43) · [Ununfoldable Polyhedra with Convex Faces](https://erikdemaine.org/papers/Ununfoldable/) · [Epsilon-Unfolding Orthogonal Polyhedra](https://scholarworks.smith.edu/csc_facpubs/50/) · [Geometric Folding Algorithms, Spring 2025, Lecture 16](https://courses.csail.mit.edu/6.5310/spring25/lectures/L16.html) · [All Polyhedral Manifolds are Connected by a 2-Step Refolding](https://doi.org/10.2197/ipsjjip.33.981)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7006 — Optimal input-sparsity subspace embeddings

An oblivious subspace embedding chooses a random linear map without knowing the subspace it must preserve. With high probability, the map must preserve the norms of all vectors in each fixed target subspace at once. The question asks for optimal output dimension together with a precise logarithmic-over-accuracy bound on nonzeros per column. These two parameters control compression quality and the arithmetic cost of applying the embedding to sparse data. The checked 2026 result approaches the target with remaining sub-polylogarithmic factors and does not settle the exact conjecture.

[Read in atlas](index.html#TCS-7006) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357v3) · [Optimal Oblivious Subspace Embeddings with Near-Optimal Sparsity](https://doi.org/10.4230/LIPIcs.ICALP.2025.55) · [Optimal Subspace Embeddings: Resolving Nelson-Nguyen Conjecture Up to Sub-Polylogarithmic Factors](https://arxiv.org/abs/2508.14234v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7182 — Simultaneous embedding with fixed edges for two graphs

Two planar graphs share labeled vertices and possibly some edges. The question asks whether the existence of compatible planar drawings can be decided in polynomial time. Each shared vertex and edge must look identical in both drawings, while edges exclusive to different graphs may cross. The case with connected common graph is known to be efficiently solvable. The remaining target covers arbitrary common graphs and is distinct from straight-line or three-graph variants.

[Read in atlas](index.html#TCS-7182) · [Simultaneous Embedding of Planar Graphs](https://arxiv.org/abs/1204.5853) · [Constrained Planarity in Practice: Engineering the Synchronized Planarity Algorithm](https://doi.org/10.7155/jgaa.v29i1.2923) · [Structural Parameterizations of Simultaneous Planarity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2025.25) · [Simultaneous Embedding of Two Paths on the Grid](https://arxiv.org/abs/2603.09750v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0403 — Euclidean minimum spanning tree complexity

A Euclidean minimum spanning tree connects the input points with minimum total edge length. The input gives coordinates, while the complete graph of candidate edges is implicit. The card asks for the optimal deterministic arithmetic running time in every fixed dimension at least three. Exact computation must be distinguished from approximation and from algorithms with predictions or random-input promises. A resolution would determine how much low-dimensional geometry can reduce the cost of this basic connectivity problem.

[Read in atlas](index.html#TCS-0403) · [The Open Problems Project: Euclidean Minimum Spanning Tree](https://topp.openproblem.net/p5) · [Euclidean minimum spanning trees and bichromatic closest pairs](https://doi.org/10.1007/BF02574698) · [Delaunay Triangulations with Predictions](https://arxiv.org/abs/2601.08106)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0408 — Exact planar Euclidean matching

Given an even number of planar points, a perfect matching pairs every point with exactly one other point. The Euclidean objective minimizes the sum of the lengths of all chosen segments. The question is the optimal complexity of computing that minimum exactly, with bipartite matching as a related restricted variant. Approximation algorithms can exploit geometry differently and do not by themselves settle the exact problem. Sharper algorithms would improve a central geometric pairing primitive whose implicit complete graph contains quadratically many candidate edges.

[Read in atlas](index.html#TCS-0408) · [The Open Problems Project: Minimum Euclidean Matching in 2D](https://topp.openproblem.net/p6) · [A divide-and-conquer algorithm for min-cost perfect matching in the plane](https://homepage.divms.uiowa.edu/~kvaradar/paps/main-focs.pdf) · [Fast Approximation Algorithms for Euclidean Minimum Weight Perfect Matching](https://doi.org/10.1007/s00224-025-10254-7)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0381 — Flip graph connectivity in three dimensions

A tetrahedralization divides the convex hull of a fixed three-dimensional point set into tetrahedra. A local flip replaces two tetrahedra by three, or reverses that replacement, while retaining the same five vertices. The question asks whether every pair of tetrahedralizations can be joined by such moves when no four input points are coplanar. All intermediate meshes must keep every original point as a vertex at its original coordinates. Regular tetrahedralizations are known to be connected, but the unrestricted geometric question remains open in the checked sources.

[Read in atlas](index.html#TCS-0381) · [The Open Problems Project, Problem 28: Flip Graph Connectivity in 3D](https://topp.openproblem.net/p28) · [Constrained paths in the flip-graph of regular triangulations](https://doi.org/10.1016/j.comgeo.2006.07.001) · [Connectivity of Triangulation Flip Graphs in the Plane](https://doi.org/10.1007/s00454-022-00436-2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0427 — NP certificates for homeomorphism of three-manifolds

Two triangulations can describe the same three-dimensional manifold while looking combinatorially unrelated. This question asks whether every homeomorphic pair has a certificate whose size and verification time are polynomial in the input. Such a certificate need not be found efficiently by the verifier itself. The challenge is to encode the necessary topological equivalence without an excessively long sequence of transformations. An NP upper bound would distinguish the difficulty of discovering a homeomorphism from the difficulty of checking convincing evidence that one exists.

[Read in atlas](index.html#TCS-0427) · [Triangulations in Geometry and Topology: Homeomorphism](https://doi.org/10.4230/DagRep.14.2.120) · [Algorithmic homeomorphism of 3-manifolds as a corollary of geometrization](https://doi.org/10.2140/pjm.2019.301.189) · [Some conditionally hard problems on links and 3-manifolds](https://arxiv.org/abs/1602.08427) · [Recognition of Seifert fibered spaces with boundary is in NP](https://doi.org/10.1007/s00208-024-02920-x) · [Computational Geometry: Treewidth of 3-Manifolds](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7189 — Minimum-weight triangulation in NP

The input gives rational planar points and a rational limit on the total length of a triangulation. Every input point must be used, no extra points may be added, and Euclidean edge lengths are compared exactly. The question asks whether every feasible instance has a short certificate that can be checked in polynomial bit time. NP-hardness is known, but the sum of potentially irrational edge lengths prevents the usual edge-list argument from establishing NP membership. Practical exact solutions and rounded-cost variants do not settle the certificate question for arbitrary exact inputs.

[Read in atlas](index.html#TCS-7189) · [Minimum-weight triangulation is NP-hard](https://arxiv.org/abs/cs/0601002) · [Solving Large-Scale Minimum-Weight Triangulation Instances to Provable Optimality](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.44) · [Taming Infinity One Chunk at a Time: Concisely Represented Strategies in One-Counter MDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.138)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0398 — Exact planar Euclidean maximum TSP

The problem asks for an exactly longest closed Euclidean tour through rational points in the plane. The output is an ordering of all points, and edge crossings are allowed. One deterministic algorithm must run in time polynomial in the full binary length of all coordinates. Approximation schemes and exact algorithms for polygonal norms do not settle this Euclidean bit-complexity question. A resolution would clarify how the choice of geometry and exact arithmetic affects optimization complexity.

[Read in atlas](index.html#TCS-0398) · [Problem 49: Planar Euclidean Maximum TSP](https://topp.openproblem.net/p49) · [The Geometric Maximum Traveling Salesman Problem](https://doi.org/10.1145/876638.876640) · [Two Algorithmic Results for the Traveling Salesman Problem](https://doi.org/10.1287/moor.21.1.65) · [Noncrossing Longest Paths and Cycles](https://doi.org/10.1007/s00373-025-02985-8)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0410 — Output-sensitive convex hull complexity

An output-sensitive convex hull algorithm charges for both its input points and the facets it actually produces. The question asks for the best such running time for point sets in fixed-dimensional Euclidean space. Small hulls should be cheaper than the worst-case hull complexity would suggest. The difficult target is to reconcile reading the input, identifying extreme structure, and listing the output with nearly optimal overhead. Progress would improve geometric optimization whenever many input points contribute little to the final convex boundary.

[Read in atlas](index.html#TCS-0410) · [The Open Problems Project: Output-sensitive Convex Hull](https://topp.openproblem.net/p15) · [Output-Sensitive Results on Convex Hulls, Extreme Points, and Related Problems](https://tmc.web.engr.illinois.edu/convj.pdf) · [A Combinatorial Proof of Universal Optimality for Computing a Planar Convex Hull](https://doi.org/10.4230/LIPIcs.ESA.2025.102)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0973 — Earth mover distance sketching complexity

Each planar grid subset must be compressed independently before the other input is available. The decoder uses the two bit strings to estimate the minimum Manhattan-cost matching of equal-size sets. The target is the optimal tradeoff between sketch length and multiplicative approximation, with constant success probability for every fixed pair. Known embedding and full transportation-norm results do not automatically characterize arbitrary decoders for these subset sketches. Sharp bounds would establish how much information optimal-transport comparisons must retain.

[Read in atlas](index.html#TCS-0973) · [Sketching Earth Mover Distance](https://sublinear.info/index.php?title=Open_Problems:49) · [Efficient Sketches for Earth-Mover Distance, with Applications](https://www.mit.edu/~andoni/papers/emdStream.pdf) · [Sketching and Embedding are Equivalent for Norms](https://arxiv.org/abs/1411.2577v3) · [Lower Estimates for L₁-Distortion of Transportation Cost Spaces](https://doi.org/10.1145/3798129.3800785)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0327 — Counting simple polygonalizations

A simple polygonalization connects all points of a planar set into one noncrossing closed polygon. The question asks whether its exact number can be computed in deterministic polynomial time from binary rational coordinates. Starting-point changes and reverse traversals count as the same polygon, and collinear input points are allowed. Subexponential counting in general position and output-polynomial enumeration are known, but neither gives a polynomial-time exact count for every input. The problem tests whether geometric noncrossing structure can make a large family of Hamiltonian cycles efficiently countable.

[Read in atlas](index.html#TCS-0327) · [The Open Problems Project, Problem 16: Simple Polygonalizations](https://topp.openproblem.net/p16) · [Peeling and Nibbling the Cactus: Subexponential-Time Algorithms for Counting Triangulations and Related Problems](https://doi.org/10.4230/LIPIcs.SoCG.2016.52) · [Non-crossing Hamiltonian Paths and Cycles in Output-Polynomial Time](https://doi.org/10.1007/s00453-024-01255-y)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0417 — Near-quadratic Voronoi complexity of lines in three dimensions

Each point in three-dimensional space has a set of nearest input lines. Connected regions with the same nearest-line set form the diagram’s cells. The question counts cells of all dimensions. The proposed bound is arbitrarily close to quadratic. The Euclidean metric and the specified nondegeneracy convention are essential parts of this formulation.

[Read in atlas](index.html#TCS-0417) · [The Open Problems Project: Voronoi Diagram of Lines in 3D](https://topp.openproblem.net/p3)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0419 — coNP certificates for three-manifold homeomorphism

The homeomorphism problem asks whether two triangulations represent the same three-dimensional space. This card asks for short certificates precisely when those spaces are not homeomorphic. Every nonhomeomorphic pair must have verifiable evidence, including pairs that agree on familiar invariants. A general positive result would imply polynomial certificates for graph nonisomorphism through a known reduction. It would clarify whether topological distinction has a uniformly efficient theory of verification.

[Read in atlas](index.html#TCS-0419) · [Triangulations in Geometry and Topology: Homeomorphism](https://doi.org/10.4230/DagRep.14.2.120) · [Algorithmic homeomorphism of 3-manifolds as a corollary of geometrization](https://doi.org/10.2140/pjm.2019.301.189) · [Some conditionally hard problems on links and 3-manifolds](https://arxiv.org/abs/1602.08427) · [Recognition of Seifert fibered spaces with boundary is in NP](https://doi.org/10.1007/s00208-024-02920-x) · [Computational Geometry: Treewidth of 3-Manifolds](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0411 — Point location in three-dimensional subdivisions

A three-dimensional subdivision divides space into labelled polyhedral regions. After preprocessing the boundary representation, a query asks for the region containing an arbitrary supplied point. The target is simultaneous linear storage and logarithmic worst-case query time, measured in the total representation size. Queries on boundaries may return any incident region, and neither random queries nor convex cells are assumed. A resolution would determine whether arbitrary spatial partitions can support exact search as economically as planar ones.

[Read in atlas](index.html#TCS-0411) · [The Open Problems Project: Point Location in 3D Subdivision](https://topp.openproblem.net/p13) · [Point location](https://www.csun.edu/~ctoth/Handbook/chap38.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0430 — NP-hardness of three-manifold homeomorphism

Deciding whether two triangulated three-manifolds are homeomorphic has algorithms, but decidability alone says little about feasible running time. This question seeks an NP-hardness lower bound for the general decision problem. A reduction would have to encode arbitrary instances of a known hard problem into pairs of manifolds. Hardness of related knot or triangulation optimization tasks does not immediately supply that encoding. Such a result would locate manifold equivalence more precisely among familiar computational problems and constrain expectations for general-purpose recognition algorithms.

[Read in atlas](index.html#TCS-0430) · [Triangulations in Geometry and Topology: Homeomorphism](https://doi.org/10.4230/DagRep.14.2.120) · [Algorithmic homeomorphism of 3-manifolds as a corollary of geometrization](https://doi.org/10.2140/pjm.2019.301.189) · [Some conditionally hard problems on links and 3-manifolds](https://arxiv.org/abs/1602.08427) · [Recognition of Seifert fibered spaces with boundary is in NP](https://doi.org/10.1007/s00208-024-02920-x) · [Computational Geometry: Treewidth of 3-Manifolds](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3059 — Lower-left anchored rectangle packing constant

The target is the worst possible optimal coverage by rectangles anchored at their lower-left corners at arbitrary points of the unit square. Every finite point set must include the origin, and each point receives a positive-area rectangle with no interior overlap. The numerical answer must locate the universal coverage constant within one percentage point, with a complete Lean proof. Freedman’s exact half-coverage conjecture remains the source question and is stronger than satisfying this approximation criterion. The checked universal bounds are 39 and 50 percent, while the smaller upper bound in the 2021 paper concerns only its particular greedy algorithm.

[Read in atlas](index.html#TCS-3059) · [On Greedily Packing Anchored Rectangles](https://doi.org/10.4230/LIPIcs.ICALP.2021.61) · [An Existential Proof of the Conjecture on Packing Anchored Rectangles](https://arxiv.org/abs/1310.8403) · [Matching and Packing Problems – Optimization Under Uncertainty in Theory and Practice](https://media-api.suub.uni-bremen.de/api/core/bitstreams/070d2aba-8991-4dd5-a008-1c348fdf8c8f/content)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0416 — Polygon visibility graph recognition

A polygon's visibility graph records which pairs of vertices can be joined by a segment lying inside the polygon. The source supplies both a candidate graph and a Hamiltonian cycle specifying the intended polygon boundary. It asks for an efficient decision procedure for whether a simple polygon realizes exactly that information. Choosing coordinates must satisfy visibility and obstruction requirements simultaneously. The problem tests whether a combinatorial record of sight lines contains enough accessible structure to reconstruct a genuine geometric environment.

[Read in atlas](index.html#TCS-0416) · [The Open Problems Project: Visibility Graph Recognition](https://topp.openproblem.net/p17) · [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006) · [Complexity Aspects of Visibility Graphs](https://doi.org/10.1142/S0218195995000179)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0990 — Estimating Earth-Mover Distance

A stream presents red and blue points on a planar grid, with equally many points of each color. Their Earth Mover Distance is the minimum total cost of matching each red point to a blue point. The source asks which approximation guarantees are possible when the stream can be retained only through a small memory state. A central target is constant-factor approximation with space polynomial in the logarithms of the input and grid sizes. Transportation structure must be captured without storing all points or the matching itself.

[Read in atlas](index.html#TCS-0990) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0377 — Linear-size universal point sets for planar graphs

One point set is selected for each graph size. Every planar graph of that size must have a straight-line drawing using some of those points. Vertex assignments may depend on the graph. The question asks whether only linearly many points suffice. Results for subclasses do not settle the universal requirement.

[Read in atlas](index.html#TCS-0377) · [The Open Problems Project: Smallest Universal Set of Points for Planar Graphs](https://topp.openproblem.net/p45) · [Linear Size Universal Point Sets for Classes of Planar Graphs](https://arxiv.org/abs/2303.00109)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0432 — Polynomial flip-distance bounds for three-manifold triangulations

A compact connected three-manifold can be represented by many finite simplicial triangulations. The question asks whether each fixed manifold admits a polynomial bound, in the two endpoint tetrahedron counts, on the number of local moves connecting any pair of its triangulations. The specified convention permits both interior bistellar flips and elementary boundary shellings and their inverses, explicitly repairing the boundary ambiguity in the original source. Such a bound would give short certificates connecting finite descriptions of the same space without requiring an efficient method to find them or a single polynomial for every manifold. A complete Lean answer must prove the bound for every fixed manifold type or exhibit one fixed type whose triangulation distances defeat every polynomial.

[Read in atlas](index.html#TCS-0432) · [The homeomorphism problem, in Triangulations in Geometry and Topology (Dagstuhl Seminar 24072)](https://doi.org/10.4230/DagRep.14.2.120) · [K3: A New Problem List in Low-Dimensional Topology, Problem 3.28](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf) · [An upper bound on Pachner moves relating geometric triangulations](https://arxiv.org/abs/1902.02163v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0428 — NP recognition of closed hyperbolic three-manifolds

The input describes a compact connected three-manifold by gluing faces of finitely many tetrahedra. The question is whether being closed and admitting a hyperbolic metric always has a polynomial-size certificate. A single deterministic verifier must check such certificates in polynomial time for every input triangulation. Recognition is decidable, but this does not give the required certificate-size and verification-time bounds. A positive answer would connect a global geometric structure with short, efficiently verifiable combinatorial evidence.

[Read in atlas](index.html#TCS-0428) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0340 — Efficient average-distortion embeddings of polyhedral norms

The average John theorem preserves squared distances on average after taking the square root of a norm metric. The algorithmic question asks for an efficiently constructed map that is nonexpanding on the entire space, including future query points. This card explicitly selects rational polyhedral norms and rational data points so that the input and computational cost have finite bit encodings. The output must describe one continuous Euclidean map that can be evaluated to any requested precision in polynomial time. This would turn a structural existence theorem into an algorithmic object, while the present review keeps the current status of the selected computational specialization uncertain.

[Read in atlas](index.html#TCS-0340) · [Computational Geometry](https://doi.org/10.4230/DagRep.11.4.1) · [An average John theorem](https://doi.org/10.2140/gt.2021.25.1631) · [Near Neighbor Search via Efficient Average Distortion Embeddings](https://doi.org/10.4230/LIPIcs.SoCG.2021.50) · [Average-Distortion Sketching](https://arxiv.org/abs/2411.05156v3)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0970 — Fast JL Transform for Sparse Vectors

A Johnson-Lindenstrauss transform maps a vector into fewer dimensions while approximately preserving its Euclidean length with high probability. The target dimension is O(\(\log (1/\mathrm{P})\) divided by epsilon squared) for failure probability P and error epsilon. The source asks for applying the transform to an s-sparse input in time roughly s plus the output dimension, up to polylogarithmic factors. It also asks for an explicit distribution generated from only \(O(\log (d/\mathrm{P}))\) random bits. The project combines fast multiplication, optimal dimensional reduction, and a compact random seed rather than optimizing any one resource alone.

[Read in atlas](index.html#TCS-0970) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0409 — Minimum-Link Path in 2D

A minimum-link path connects two given points through closed planar free space while using the fewest straight segments. The environment may contain many polygonal holes, and the path may bend at arbitrary interior or boundary points and use arbitrary directions. The question asks for one exact deterministic algorithm whose worst-case real-RAM operation count divided by the square of the total boundary size tends to zero. This interpretation includes logarithmic-factor savings, and known 3SUM-hardness does not by itself rule them out. The checked approximation results and hardness results for boundary bends or three-dimensional paths do not settle this planar exact-path target.

[Read in atlas](index.html#TCS-0409) · [The Open Problems Project: Minimum-Link Path in 2D](https://topp.openproblem.net/p22) · [Minimum-Link Paths Among Obstacles in the Plane](https://doi.org/10.1007/BF01758855) · [Minimum-Link Paths Revisited](https://arxiv.org/abs/1302.3091v1) · [Threesomes, Degenerates, and Love Triangles](https://arxiv.org/abs/1404.0799v3) · [On the Complexity of Minimum-Link Path Problems](https://arxiv.org/abs/1603.06972v1) · [Computational Geometry: Report from Dagstuhl Seminar 25201](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4454 — Half-snowflake embeddings into Wasserstein p-space

The question asks whether every finite metric becomes a bounded-distortion subset of Wasserstein p-space over R³ after taking square roots of its distances. The exponent p is fixed above two, and the distortion bound must depend only on p. The known theorem works at snowflake exponent 1/p, which is smaller than one half in this range. Almost-isometric embeddings and embedding the entire Wasserstein-2 space are separate stronger questions. The later planar results checked here do not settle this three-dimensional half-snowflake conjecture.

[Read in atlas](index.html#TCS-4454) · [Impossibility of Sketching of the 3D Transportation Metric with Quadratic Cost](https://doi.org/10.4230/LIPIcs.ICALP.2016.83) · [Snowflake universality of Wasserstein spaces](https://doi.org/10.24033/asens.2363) · [Coarse Embeddability of Wasserstein Space and the Space of Persistence Diagrams](https://doi.org/10.1007/s00454-024-00674-6)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5875 — Hausdorff distance between semialgebraic sets

The Hausdorff distance compares two sets by taking the worst nearest-neighbor distance in both directions. The extracted question asks for the complexity of computing this distance when both inputs are general semialgebraic sets, described by polynomial conditions. Algorithms for finite point sets or polygonal objects do not settle that broader representation model. The surrounding paper studies intermediate shapes and cites polynomial-time computation for general semialgebraic inputs as an unresolved background issue. A precise solution would need to specify the dimension, algebraic input encoding, and output representation as well as control the running time.

[Read in atlas](index.html#TCS-5875) · [Between Shapes, Using the Hausdorff Distance](https://doi.org/10.4230/LIPIcs.ISAAC.2020.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6199 — Decidability of contractibility for finite two-dimensional complexes

The input is a finite simplicial complex made of vertices, edges and triangles. Decide whether expansions and collapses can transform it into a single vertex. Intermediate complexes may be larger and higher-dimensional than the input. The algorithm must halt with a correct answer on every input, but no efficiency bound is imposed. This recognition problem differs from limiting expansions to dimension three or using collapses alone.

[Read in atlas](index.html#TCS-6199) · [Parametrized Complexity of Expansion Height](https://doi.org/10.4230/LIPIcs.ESA.2019.13) · [Random simple-homotopy theory](https://doi.org/10.1007/s41468-023-00139-4)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6880 — Efficient constant-distortion cut-cone approximation

The cut cone consists of nonnegative combinations of cut metrics and provides a geometric formulation of several graph-cut optimization problems. Direct membership testing is difficult, so the source asks for a tractable approximating cone. The preferred guarantee is constant distortion together with membership and separation algorithms polynomial in the dimension. A separation algorithm must either recognize membership or produce a hyperplane certifying exclusion. Such a cone could support efficient convex optimization for cut problems, while the source explicitly notes that its proposed negative-type-metric candidate does not achieve the desired constant-distortion guarantee.

[Read in atlas](index.html#TCS-6880) · [Expander Graphs and Their Applications](https://www.math.ias.edu/avi/node/974)
Existing status: `source_open` · Summary written: 2026-09-11

## Learning theory (36)

### TCS-6541 — Linear-size sample compression

Sample compression keeps labeled examples and a short side message from which a fixed decoder recovers every original training label. The conjecture asks for a bound linear in VC dimension, uniformly across all Boolean concept classes. This card counts both retained examples and side bits, and permits arbitrary predictors and unlimited computation. The general known upper bound is exponential, while recent structured results and an embedding obstruction do not close that gap. A complete Lean answer must prove the universal linear bound or rule it out for some classes, and the withdrawn 2026 claim supplies no resolution.

[Read in atlas](index.html#TCS-6541) · [Sample compression schemes for VC classes](https://arxiv.org/abs/1503.06960v2) · [Dual VC Dimension Obstructs Sample Compression by Embeddings](https://proceedings.mlr.press/v247/chase24a.html) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html) · [Sample compression schemes for balls in structurally sparse graphs](https://arxiv.org/abs/2604.02949v1) · [The No-Clash Teaching Dimension is Bounded by VC Dimension (withdrawn)](https://arxiv.org/abs/2603.23561v4)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6542 — Learning parity with noise in polynomial time

The card asks whether a hidden parity vector can be recovered efficiently from uniform examples whose labels are independently flipped. The noise rate is any fixed rational below one half, with a separate uniform polynomial-time learner allowed for each rate. Success requires the entire secret vector with probability at least two thirds for every secret and dimension. Known subexponential algorithms, storage bounds, conditional reductions and structured physical experiments do not establish the unrestricted polynomial-time assertion or its negation. The completed card preserves the assessed importance and gives exact computation, sampling and Lean proof requirements.

[Read in atlas](index.html#TCS-6542) · [Noise-Tolerant Learning, the Parity Problem, and the Statistical Query Model](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2003-Noise-Tolerant_Learning.pdf) · [The Parity Problem in the Presence of Noise, Decoding Random Linear Codes, and the Subset Sum Problem](https://cseweb.ucsd.edu/~vlyubash/papers/parityproblem.pdf) · [Memory-Sample Lower Bounds for Learning Parity with Noise](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.60) · [Hardness Amplification for (Sparse) LPN](https://arxiv.org/abs/2605.10056) · [Towards Worst-case Hardness for Low-Noise LPN](https://eccc.weizmann.ac.il/report/2026/095/) · [Solving Learning Parity with Noise on an Optical Coherent Ising Machine](https://www.nature.com/articles/s42005-026-02868-1)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6543 — Learning Boolean juntas from uniform random examples

A Boolean junta depends on at most k hidden coordinates of an n-bit input. The card asks for a single learner with time polynomial in n, 2^k and inverse prediction error from independent uniform noiseless examples. The output may be any efficient Boolean circuit and need not recover the exact relevant set. Known faster-exponent algorithms and results using smoothing, monotonicity, membership queries or correlated examples do not meet this full guarantee. The completed card preserves its earlier approved target and importance, identifies the original source, and specifies the exact uniform quantifiers for a Lean proof or refutation.

[Read in atlas](index.html#TCS-6543) · [Learning functions of k relevant variables; author manuscript titled Learning juntas](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf) · [Finding Correlations in Subquadratic Time, with Applications to Learning Parities and the Closest Pair Problem](https://theory.stanford.edu/~valiant/papers/corrFull.pdf) · [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791) · [New Statistical and Computational Results for Learning Junta Distributions](https://arxiv.org/abs/2505.05819) · [The Benefits of Temporal Correlations: SGD Learns k-Juntas from Random Walks Efficiently](https://arxiv.org/abs/2605.10237) · [Learning Juntas under Markov Random Fields](https://openreview.net/forum?id=wszZlP1K14) · [Mathematics and Computation (March 27, 2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5358 — Polynomial-time distribution-free PAC learning of DNF

A DNF is a disjunction of conjunctions of possibly negated Boolean variables, with the number of terms bounded by the supplied size parameter. The learner sees only independent noiseless labeled examples from an arbitrary unknown distribution and must run in one polynomial in dimension, term bound and the stated accuracy/confidence parameters. Its output may be any explicitly written deterministic Boolean circuit whose predictions have small distributional error with high probability. Polynomial sample complexity is available, while known improper-learning lower bounds remain conditional and recent positive results use restricted distributions, stronger query access or different output guarantees. A solution needs a complete Lean proof of the full uniform learner guarantee or a negation covering every allowed learner and polynomial bound.

[Read in atlas](index.html#TCS-5358) · [Learning DNF Expressions from Fourier Spectrum](https://proceedings.mlr.press/v23/feldman12b.html) · [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791v1) · [Complexity Theoretic Limitations on Learning DNF’s](https://proceedings.mlr.press/v49/daniely16.html) · [From Local Pseudorandom Generators to Hardness of Learning](https://proceedings.mlr.press/v134/daniely21a.html) · [Faster exact learning of k-term DNFs with membership and equivalence queries](https://arxiv.org/abs/2507.20336v1) · [Iterative Chow Filtering for Learning with Distribution Shift](https://arxiv.org/abs/2605.17251v1) · [DNF formulas are efficiently testable with relative error](https://arxiv.org/abs/2601.16076v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3391 — Efficient learning of well-separated Gaussian mixtures

The card asks for globally learning well-separated spherical Gaussian mixtures with both polynomial samples and polynomial computation. The weights, centers and unequal component scales are hidden, and all must be recovered to the source’s stated relative accuracy up to one permutation. The source’s efficient local refinement requires initialization that its sample-efficient procedure does not find in polynomial time. Later algorithms improve separation or dimension dependence but retain assumptions or parameter costs that do not meet the full target. A Lean resolution must establish or refute one uniform end-to-end learner under the explicit separation, access and arithmetic-cost conventions.

[Read in atlas](index.html#TCS-3391) · [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html) · [Clustering Mixtures with Almost Optimal Separation in Polynomial Time](https://arxiv.org/abs/2112.00706) · [A Fourier Approach to Mixture Learning](https://arxiv.org/abs/2210.02415) · [Learning Mixture Models via Efficient High-dimensional Sparse Fourier Transforms](https://arxiv.org/abs/2601.05157) · [Dimension Reduction via Sum-of-Squares and Improved Clustering Algorithms for Non-Spherical Mixtures](https://proceedings.mlr.press/v336/anderson26a.html)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5088 — Fully polynomial learning of halfspace intersections under Gaussian and uniform inputs

The card asks separately whether intersections of a variable number of affine halfspaces can be learned efficiently under Gaussian and uniform Boolean-cube inputs. The desired polynomial bounds cover dimension, intersection size, inverse accuracy, training and prediction. Labels come only from independent noiseless examples, and the output predictor may lie outside the target class. The surrounding margin theorem and newer subexponential, bounded-width and proper-learning results do not supply the requested uniform polynomial guarantee. A Lean resolution must prove or refute the full learner-existence statement in each explicitly defined computational model.

[Read in atlas](index.html#TCS-5088) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html) · [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700) · [Sparsifying Suprema of Gaussian Processes](https://arxiv.org/abs/2411.14664) · [Proper Agnostic Learning of Functions of Halfspaces under Gaussian Marginals](https://arxiv.org/abs/2605.27594)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6544 — Distribution-free learning of two margin halfspaces

The intersection of two halfspaces labels a point positively when both linear inequalities hold. This question asks whether such labels can be learned in polynomial time from independent examples under any distribution with a margin from both boundaries. The learner may output a different kind of hypothesis, provided that predictions remain efficient. The 2025 source proves efficient learning under an extra factorization assumption, while two 2026 preprints report broader bounds that do not by themselves meet this polynomial target. A resolution would determine whether two linear rules can be learned efficiently without favorable structure in the example distribution.

[Read in atlas](index.html#TCS-6544) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html) · [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700v2) · [Tight Bounds for Learning Polyhedra with a Margin](https://arxiv.org/abs/2604.14614v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5090 — One-way functions from hardness of learning P/poly

The card asks whether failure of efficient worst-case circuit learning already implies ordinary one-way functions. The learner receives independent noiseless examples under any input distribution and must output a small ordinary Boolean predictor. A one-way function is uniformly easy to evaluate but has negligible inversion probability for every efficient uniform adversary at all sufficiently large lengths. Known reverse connections impose efficiently sampled targets, low computational depth, different learning-length quantifiers or a different description-approximation problem. The completed card preserves the unrestricted implication and records those distinctions while leaving its current status uncertain.

[Read in atlas](index.html#TCS-5090) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46) · [On the Structure of Learnability beyond P/poly](https://eccc.weizmann.ac.il/report/2021/173/) · [Learning in Pessiland via Inductive Inference](https://eccc.weizmann.ac.il/report/2023/100/) · [On White-Box Learning and Public-Key Encryption](https://doi.org/10.4230/LIPIcs.ITCS.2025.73) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/) · [On the Structure of Learnability beyond P/poly](https://link.springer.com/article/10.1007/s00037-024-00260-5)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5434 — Nontrivial agnostic membership-query learning of \(\mathrm{ACC}^{0}\)

The card asks whether constant-depth modular circuits admit agnostic membership-query learning with a superpolynomial-factor saving over exponential time. Inputs are uniform, labels may be arbitrary and stochastic, and each chosen query receives a fresh conditional label. The target keeps the source’s exponentially small correlation slack and its literal one-third full-learning success guarantee. Known positive results restrict the circuit class or relax the optimum-error comparison and do not establish the full ACC⁰ target. A Lean answer must prove the complete uniform algorithmic assertion or its unconditional negation under these exact resource and accuracy conventions.

[Read in atlas](index.html#TCS-5434) · [Agnostic Membership Query Learning with Nontrivial Savings: New Results and Techniques](https://proceedings.mlr.press/v237/karchmer24a.html) · [Agnostic Learning from Tolerant Natural Proofs](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.35) · [Agnostic Membership Query Learning with Nontrivial Savings: New Results, Techniques](https://arxiv.org/abs/2311.06690)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7294 — Learning decision trees from uniform random examples in polynomial time

The card asks for a polynomial-time learner for every small Boolean decision tree from independent uniform labeled examples. The tree is hidden and the learner receives neither chosen-input labels nor its representation. A successful learner may return any efficient Boolean circuit with the requested prediction error and two-thirds confidence. Known smoothed, query-based and representation-aware results provide different guarantees and do not settle this passive learning target. The completed card preserves its importance and scope while making the accuracy encoding, resource bounds and full Lean proof criterion explicit.

[Read in atlas](index.html#TCS-7294) · [Decision trees are PAC-learnable from most product distributions: a smoothed analysis](https://arxiv.org/abs/0812.0933) · [Backdoor Defense, Learnability and Obfuscation](https://doi.org/10.4230/LIPIcs.ITCS.2025.38) · [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791) · [Decision Tree Learning on Product Spaces](https://arxiv.org/abs/2605.12983)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5119 — Sample-optimal Gaussian graphical model learning in polynomial time

The problem asks whether sparse Gaussian conditional-independence graphs can be recovered in polynomial time with an information-theoretically optimal number of independent samples. The statement allows arbitrary means and condition numbers and requires every edge and nonedge to be identified correctly. Sample optimality is defined by a minimax benchmark that retains degree, normalized edge strength and confidence without assuming a universally sharp formula. Known degree-dependent algorithms, structural-subclass results, conditional hardness and trajectory-based algorithms each address a different part of the question. A Lean resolution must establish or refute one uniform algorithm with both a universal sample factor and a fixed polynomial arithmetic-time bound.

[Read in atlas](index.html#TCS-5119) · [Information Theoretic Optimal Learning of Gaussian Graphical Models](https://proceedings.mlr.press/v125/misra20a.html) · [Learning Some Popular Gaussian Graphical Models without Condition Number Bounds](https://proceedings.neurips.cc/paper_files/paper/2020/hash/7cc980b0f894bd0cf05c37c246f215f3-Abstract.html) · [Lasso with Latents: Efficient Estimation, Covariate Rescaling, and Computational-Statistical Gaps](https://proceedings.mlr.press/v247/kelner24a.html) · [Learning Gaussian Graphical Models from a Glauber Trajectory Without Mixing](https://arxiv.org/abs/2606.31230)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7293 — Distribution-free improper learning of two unrestricted halfspaces

One threshold is efficiently learnable from labeled examples, but the target here combines two thresholds. Examples follow any fixed distribution on the Boolean cube and no positive margin is promised. The learner receives a bound on target description length and may output any efficiently evaluable classifier. Hardness for proper learners or growing numbers of halfspaces does not settle this two-halfspace target. The question asks for a uniform polynomial-time guarantee across all distributions and permitted target descriptions.

[Read in atlas](index.html#TCS-7293) · [The Intersection of Two Halfspaces Has High Threshold Degree](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf) · [Improved Hardness Results for Learning Intersections of Halfspaces](https://theoretics.episciences.org/18105) · [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5902 — PAC learning of finite automata under the uniform distribution

The card asks whether every finite automaton can be learned efficiently from uniformly sampled words labeled only by acceptance. The learner knows the word length, alphabet and state bound and may return any efficient predictor. It must achieve every requested accuracy and confidence using polynomial time without membership queries or state information. A published local-pseudorandom-generator assumption rules out even weak improper learning on uniform binary words, and a 2026 source retains that premise. The completed card records this conditional negative answer while preserving the original unconditional question and its exact Lean decision criterion.

[Read in atlas](index.html#TCS-5902) · [Approximate Learning of Limit-Average Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2019.17) · [From Local Pseudorandom Generators to Hardness of Learning](https://proceedings.mlr.press/v134/daniely21a.html) · [On the Hardness of Learning Regular Expressions](https://proceedings.mlr.press/v313/attias26a.html) · [Learning a Random DFA from Uniform Strings and State Information](https://www.cs.yale.edu/homes/dongqu/alt15.pdf)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-2336 — Optimal multiclass regret versus Littlestone dimension

An online learner predicts a label distribution and then sees the correct label on each round. Regret compares its expected cumulative mistakes with the best fixed hypothesis on the same sequence. The card asks for the worst minimax regret among all classes of Littlestone dimension at most d, including infinite label spaces. The general upper and lower bounds differ by a square-root logarithm, while the sharper finite-label theorem needs an extra regularity condition. A complete Lean answer must give matching universal bounds on the two-parameter regret function under the unrestricted model.

[Read in atlas](index.html#TCS-2336) · [Multiclass Online Learning and Uniform Convergence](https://proceedings.mlr.press/v195/hanneke23b.html) · [Topics in Learning Theory: Prediction, Estimation, and Partial Information](https://www.ambujtewari.com/theses/Vinod_Raman_Thesis_2025.pdf) · [Regret-Oracle Complexity Tradeoffs in Agnostic Online Learning](https://arxiv.org/abs/2605.07155)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4592 — Time complexity of Gaussian agnostic halfspace learning

The card asks for optimal dimension and accuracy dependence when matching the best affine halfspace under Gaussian inputs. It preserves the original deterministic Boolean target-function model and permits any finite evaluable predictor. The statement explicitly counts exact real-arithmetic sampling, computation, output and evaluation and distinguishes this from finite-bit complexity. Modern statistical-query, cryptographic and proper-learning results have different assumptions or interfaces whose transfer is not silently presumed. A Lean resolution must characterize the attainable uniform time rates with matching bounds under the same label, resource and parameter conventions.

[Read in atlas](index.html#TCS-4592) · [Embedding Hard Learning Problems Into Gaussian Space](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.793) · [The Optimality of Polynomial Regression for Agnostic Learning under Gaussian Marginals in the SQ Model](https://proceedings.mlr.press/v134/diakonikolas21c.html) · [Near-Optimal Cryptographic Hardness of Agnostically Learning Halfspaces and ReLU Regression under Gaussian Marginals](https://proceedings.mlr.press/v202/diakonikolas23b.html) · [Proper Agnostic Learning of Functions of Halfspaces under Gaussian Marginals](https://arxiv.org/abs/2605.27594) · [Near-Optimal Cryptographic Hardness of Learning With Homogeneous Halfspaces Under Gaussian Marginals](https://arxiv.org/abs/2604.26446)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-3117 — Memory–sample tradeoffs for noisy parity learning

A hidden binary vector is observed through uniformly random parity equations with independent noise. Each equation is correct with probability one half plus \(\varepsilon\). The proposed lower bound requires either \(\Omega (n^{2}/\varepsilon ^{2})\) stored bits or exponentially many samples. The source proves the weaker \(\Omega (n^{2}/\varepsilon )\) memory threshold and gives a matching-to-the-conjecture space upper bound. The card fixes bounded-error exact recovery and requires constants uniform in \(\varepsilon\).

[Read in atlas](index.html#TCS-3117) · [Memory-Sample Lower Bounds for Learning Parity with Noise](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.60) · [Toward Lower Bounds on Memory-Sample Tradeoffs for Learning Parity with Noise](https://dimacs.rutgers.edu/reu-project-detail/toward-lower-bounds-on-memory-sample-tradeoffs-for)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3177 — Learning PH/poly from learning NP/poly

The question asks whether efficient PAC learning of NP/poly would imply efficient PAC learning at every fixed level of the polynomial hierarchy. Targets are small circuits with alternating witness tests, while the learner sees only independent labeled examples from an arbitrary unknown distribution. The output must be an ordinary efficiently evaluatable Boolean circuit, with polynomial time also accounting for samples, randomness and the public target-size bound. Known structural equivalences for stronger classes and ordinary circuit-representation collapses do not establish this learning implication. The full 2021 source explicitly asks the question, while the bounded later-status review supplies no matching resolution and leaves present status uncertain.

[Read in atlas](index.html#TCS-3177) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46) · [On the Structure of Learnability beyond P/poly](https://eccc.weizmann.ac.il/report/2021/173/) · [On the Structure of Learnability beyond P/poly](https://link.springer.com/article/10.1007/s00037-024-00260-5)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0677 — Proper decision-tree learning in polynomial time

Proper learning of decision trees requires the learner to output a decision tree, preserving the target representation's simple branching structure. The source asks for a polynomial-time algorithm under the uniform input distribution with membership queries available. Those queries let the learner choose inputs and observe their target labels, making this different from learning from random examples alone. Existing algorithms in the source are faster than earlier quasipolynomial approaches but still fall short of polynomial time. A solution would provide an efficient way to recover an interpretable tree hypothesis without abandoning the tree representation during learning.

[Read in atlas](index.html#TCS-0677) · [Open Problem: Properly learning decision trees in polynomial time?](https://proceedings.mlr.press/v178/open-problem-blanc22a.html) · [Properly Learning Decision Trees with Queries Is NP-Hard](https://arxiv.org/abs/2307.04093) · [Fast Decision Tree Learning Solves Hard Coding-Theoretic Problems](https://arxiv.org/abs/2409.13096)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1573 — NP-hardness of improper learning of \(\mathrm{P}/\mathrm{poly}\)

The question asks whether SAT reduces to agnostic learning of general polynomial-size Boolean circuits. The learning oracle receives a circuit sampling labeled examples and returns an approximately optimal hypothesis. The returned hypothesis may use an arbitrarily larger fixed polynomial size than the comparator circuits. The reduction must work with every valid oracle reply and without additional cryptographic assumptions. A June 2026 follow-up gives related conditional hardness, leaving the unconditional target unresolved.

[Read in atlas](index.html#TCS-1573) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34) · [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5087 — Polynomial-time robust spectral estimation

The card asks for polynomial-time recovery of a robust low-rank representation when every training point may have been adversarially perturbed. The output must approximate the unknown clean matrix in spectral norm while respecting the rank budget and induced-norm robustness bound. The source proves that such recovery is information-theoretically possible but its efficient spectral method may only certify severe poisoning. The statement preserves the full range of fixed norm exponents and the same-output error tradeoff in an explicit real-arithmetic model. A Lean resolution must prove or refute guaranteed recovery with the stated approximation and computational costs, without extra distributional assumptions.

[Read in atlas](index.html#TCS-5087) · [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html) · [Estimating Principal Components under Adversarial Perturbations](https://proceedings.mlr.press/v125/awasthi20a.html) · [Adversarially Robust Low Dimensional Representations: manuscript history](https://arxiv.org/abs/1911.13268)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-3787 — Proper unlabeled compression of ample classes

An ample class strongly shatters every set of coordinates that it shatters. A compressor selects at most d input points from any realizable labeled sample, where d is the class’s VC dimension. A reconstructor must recover a concept in the original class consistent with all sample labels while receiving only the selected points. Maximum classes satisfy this exact bound, and labeled compression is known more generally. The 2024 oriented-matroid results still leave proper unlabeled size-d compression for all ample classes open.

[Read in atlas](index.html#TCS-3787) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.4230/LIPIcs.ICALP.2019.34) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.1016/j.jcss.2022.01.003) · [Unlabeled Sample Compression Schemes for Oriented Matroids](https://doi.org/10.1016/j.disc.2024.114006)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4792 — Multiclass sample compression from binary compression

A compression scheme stores labeled examples and auxiliary bits so a fixed decoder can reproduce all labels of a realizable sample. The question assumes a universal binary compression bound f in terms of VC dimension. It asks whether every multiclass class then has compression of the same order in f of its graph dimension, independently of its label set. Known reductions either pay an extra label-count factor or require additional structure of the binary scheme. A complete Lean answer must establish the full conditional transfer or give an admissible binary bound for which that transfer fails.

[Read in atlas](index.html#TCS-4792) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html) · [Sample Compression Scheme Reductions](https://arxiv.org/abs/2410.13012) · [Supervised learning through the lens of compression](https://papers.neurips.cc/paper_files/paper/2016/hash/59f51fd6937412b7e56ded1ea2470c25-Abstract.html) · [Multiclass Learnability Does Not Imply Sample Compression](https://proceedings.mlr.press/v237/pabbaraju24a.html)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5847 — Linear conditional-information bounds for VC learning

The card asks whether every finite-VC binary class has a proper learner whose whole output has conditional information only linear in the dimension. The same learner must achieve expected training error within a universal square-root dimension-to-sample-size term of the best hypothesis on every sample. The information experiment reveals two candidates per training position and measures what the output says about the hidden choices. Known negative results concern stricter realizable training guarantees, while other optimal generalization analyses use different information bounds. A directly relevant FOCS 2026 paper is accepted but its theorem text was not located, so the completed formulation retains uncertain current status.

[Read in atlas](index.html#TCS-5847) · [Open Problem: Information Complexity of VC Learning](https://proceedings.mlr.press/v125/steinke20b.html) · [On the Information Complexity of Proper Learners for VC Classes in the Realizable Case](https://arxiv.org/abs/2011.02970) · [PAC-Bayes, MAC-Bayes and Conditional Mutual Information: Fast rate bounds that handle general VC classes](https://proceedings.mlr.press/v134/grunwald21a.html) · [Tighter CMI-Based Generalization Bounds via Stochastic Projection and Quantization](https://arxiv.org/abs/2510.23485) · [FOCS 2026 accepted papers: The optimal information complexity of VC learning](https://focs.computer.org/2026/accepted-papers/) · [The Optimal Information Complexity of VC Learning — author publication entry](https://stevehanneke.com/)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-3689 — Non-clashing teaching dimension versus VC dimension

A teacher assigns correctly labeled examples to each concept in a finite class. No two different concepts may both fit each other’s assigned examples. The conjecture asks whether at most d examples per concept always suffice when the VC dimension is d. A quadratic general bound and exact bounds for certain special classes are known. The sharp signed-example inequality remains distinct from positive-only teaching, computational map-finding and sample-compression questions.

[Read in atlas](index.html#TCS-3689) · [Optimal Collusion-Free Teaching](https://proceedings.mlr.press/v98/kirkpatrick19a.html) · [On Batch Teaching Without Collusion](https://www.jmlr.org/papers/v24/22-0330.html) · [Non-Clashing Teaching Maps for Balls in Graphs](https://proceedings.mlr.press/v247/chalopin24a.html)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5031 — Littlestone-dimension regret bounds for unrestricted classes

A learner predicts binary labels while an adversary supplies instances and then labels. Its regret is the expected number of errors beyond those of the best fixed concept on the same sequence. The question asks whether every class of finite Littlestone dimension has regret of square-root order in dimension times horizon, with universal constants. The sharp known theorem uses a minimax regularity assumption, and later primary sources explicitly leave removal of that assumption open. A complete Lean answer must establish the universal two-sided bound for arbitrary classes or refute it under the same prediction model.

[Read in atlas](index.html#TCS-5031) · [The Dimension of Self-Directed Learning](https://proceedings.mlr.press/v237/devulapalli24a.html) · [Multiclass Online Learning and Uniform Convergence](https://proceedings.mlr.press/v195/hanneke23b.html) · [Adversarial Laws of Large Numbers and Optimal Regret in Online Classification](https://arxiv.org/abs/2101.09054) · [Topics in Learning Theory: Prediction, Estimation, and Partial Information](https://www.ambujtewari.com/theses/Vinod_Raman_Thesis_2025.pdf) · [Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension](https://proceedings.mlr.press/v195/filmus23a.html) · [Regret-Oracle Complexity Tradeoffs in Agnostic Online Learning](https://arxiv.org/abs/2605.07155)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2339 — Recursive teaching dimension conjecture

A finite concept class can be studied through both its VC dimension and its recursive teaching dimension. VC dimension measures the ability to realize label patterns, while recursive teaching measures how examples can identify concepts through successive elimination. The question asks whether one universal constant always bounds recursive teaching dimension by that constant times VC dimension. The same constant must work for every finite class. The project seeks a direct quantitative link between the complexity of learning from samples and the information needed for structured teaching.

[Read in atlas](index.html#TCS-2339) · [Tournaments, Johnson Graphs and NC-Teaching](https://proceedings.mlr.press/v201/simon23a.html) · [Open Problem: Recursive Teaching Dimension Versus VC Dimension](https://proceedings.mlr.press/v40/Simon15b.html) · [Quadratic Upper Bound for Recursive Teaching Dimension of Finite VC Classes](https://proceedings.mlr.press/v65/hu17a.html) · [RTD-Conjecture and Concept Classes Induced by Graphs](https://arxiv.org/abs/2502.09453) · [Lower Bounds for Greedy Teaching Set Constructions](https://arxiv.org/abs/2505.03223)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0694 — Statistical-query complexity of sparse halfspaces

An r-sparse halfspace uses at most r of the n Boolean input coordinates. Statistical-query learning accesses approximate expectations instead of individual labeled examples. The source asks whether the worst-case number of nearly uncorrelated sparse halfspaces stays polynomial in n when correlation is inverse-polynomial in r log n. Both the sparsity dependence and the worst-case distribution are essential to the question. A resolution would clarify the informational limits of exploiting sparse structure through statistical queries.

[Read in atlas](index.html#TCS-0694) · [Open Problem: The Statistical Query Complexity of Learning Sparse Halfspaces](https://proceedings.mlr.press/v35/feldman14c.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0683 — Improper compression for Gaussian-mixture reconstruction

The task is to learn short pointwise encodings that reconstruct bounded Euclidean data almost as well as the best k centers. It concerns the overcomplete regime, where the number of comparator centers exceeds the ambient dimension. The decoder may be improper and share a learned model, but each new point receives only polynomial-in-logarithms many bits. The card explicitly fixes unit-ball normalization, squared reconstruction loss and polynomial real-arithmetic training and evaluation. Density-estimation compression results use a different objective and do not by themselves settle this task.

[Read in atlas](index.html#TCS-0683) · [Open Problem: Improper Learning of Mixtures of Gaussians](https://proceedings.mlr.press/v75/hazan18a.html) · [A Non-generative Framework and Convex Relaxations for Unsupervised Learning](https://proceedings.neurips.cc/paper/2016/hash/be3e9d3f7d70537357c67bb3f4086846-Abstract.html) · [Near-optimal Sample Complexity Bounds for Robust Learning of Gaussian Mixtures via Compression Schemes](https://www.cs.ubc.ca/~nickhar/papers/MixtureOfGaussians/MixtureOfGaussians.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1539 — Compression overhead for adversarial robustness

The question asks whether ordinary sample compression can be made adversarially robust with only a universal constant factor in size. A message contains original labeled examples and a counted auxiliary bitstring. The reconstructed predictor must label every allowed perturbation correctly whenever the full sample is robustly realizable. Known reductions impose a perturbation-cardinality factor or a stability assumption on the ordinary scheme. The general question permits infinite perturbation sets and asks whether that overhead can be avoided.

[Read in atlas](index.html#TCS-1539) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html) · [Research publications](https://arvindr9.github.io/research)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0670 — Local regularization for multiclass learning

A local regularizer fixes a score for every hypothesis and test point before seeing the training sample. At prediction time it selects among the lowest-scored hypotheses consistent with the sample. The question asks whether every realizably PAC-learnable multiclass class admits such a rule that succeeds under every tie-breaking choice. Two preprints from July and August 2026 claim counterexamples under this definition. Their statements match the main question, while independent verification of the claimed negative resolution remains outstanding.

[Read in atlas](index.html#TCS-0670) · [Open Problem: Can Local Regularization Learn All Multiclass Problems?](https://proceedings.mlr.press/v247/asilis24b.html) · [Local Regularization Does Not Characterize Multiclass PAC Learnability](https://arxiv.org/abs/2607.23449) · [Algorithmic Principles For Multiclass Learning Are Hard To Come By: Limits of Regularization and Proper Learning](https://arxiv.org/abs/2608.26516)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0671 — Agnostic direct-sum learning rates

The question asks whether comparable single-instance agnostic learning rates force comparable rates for every number of simultaneous tasks. The learning curve is minimax expected excess zero-one error, with arbitrary distributions and improper deterministic learners. For a Cartesian power, each example is a complete tuple and any wrong coordinate makes the tuple prediction incorrect. The comparison constants must be independent of both sample size and number of tasks. An August 2026 preprint claims a finite binary counterexample, so the card records an unresolved verification status for that claimed refutation.

[Read in atlas](index.html#TCS-0671) · [Open problem: Direct Sums in Learning Theory](https://proceedings.mlr.press/v247/hanneke24c.html) · [A Rate Separation for Agnostic Direct Sums](https://arxiv.org/abs/2608.06951)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-0664 — Dimension complexity of distribution-independent SQ learning

The question asks whether successful distribution-independent statistical-query learning forces low dimension complexity. The learner may adapt bounded expectation queries to previous noisy answers. Its guarantee must hold for every distribution, target and valid response rule. The desired conclusion is one deterministic feature map representing the entire class exactly in dimension proportional to the query count divided by squared tolerance. Recent conditional results impose additional structure and do not establish the unrestricted implication.

[Read in atlas](index.html#TCS-0664) · [Invited Open Problem: Is the Power of Deep Learning over Linear Models Inherently Distribution Dependent?](https://proceedings.mlr.press/v336/feldman26a.html) · [VALG: An Agentic System for ML Theory Research](https://arxiv.org/abs/2608.13060)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0682 — Monotone empirical risk minimization

Expected prediction error can increase when a learner receives an additional independent training example. This card asks whether every finite-VC Boolean class on a countable domain nevertheless admits a monotone empirical risk minimizer. The learner may randomize and resolve ties, but must always output an empirically optimal hypothesis from the original class. Monotonicity is required for every data distribution and every consecutive positive sample size, using actual population error. A resolution would clarify whether exact empirical fitting can always be reconciled with monotone learning curves.

[Read in atlas](index.html#TCS-0682) · [Open Problem: Monotonicity of Learning](https://proceedings.mlr.press/v99/viering19a.html) · [Monotone Learning](https://proceedings.mlr.press/v178/bousquet22a.html) · [Monotonic Learning in the PAC Framework: A New Perspective](https://arxiv.org/abs/2501.05493)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0689 — Identifiable elicitation complexity

The question asks how many real-valued reports are needed to recover an arbitrary statistic by minimizing expected loss. The intermediate prediction must have a unique expected-loss minimizer and an identification function whose expected value vanishes exactly at the correct report. An unrestricted link may then turn that intermediate prediction into the desired statistic. The target covers every finite-dimensional property of a nonempty convex family of real-outcome distributions, with infinity meaning that no finite report dimension works. A full classification would determine the expressive limits of single-observation loss-based prediction beyond the statistic families whose complexities are already known.

[Read in atlas](index.html#TCS-0689) · [Open Problem: Property Elicitation and Elicitation Complexity](https://proceedings.mlr.press/v49/frongillo16.html) · [Elicitation Complexity of Statistical Properties](https://doi.org/10.1093/biomet/asaa093) · [Recent Trends in Information Elicitation](https://sigecom.org/exchanges/volume_22/1/FRONGILLO.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3691 — Uniform convergence under Dobrushin dependence

A dependent training sample has identical marginal distributions and a bounded total influence on every coordinate. Uniform convergence requires every hypothesis’s empirical zero-one loss to approximate its population loss. The card asks whether every finite-VC class has the usual square-root rate when the ordinary Dobrushin coefficient stays below one. The source already proves learnability under that condition, but its uniform-convergence theorem requires stronger logarithmic influences. The formulation makes the iid-order rate and fixed dependence slack explicit, without claiming an optimal constant near the boundary.

[Read in atlas](index.html#TCS-3691) · [Learning from Weakly Dependent Data under Dobrushin’s Condition](https://proceedings.mlr.press/v99/dagan19a.html) · [Learning from Weakly Dependent Data under Dobrushin’s Condition](https://arxiv.org/abs/1906.09247)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4186 — Learning speedups from random examples

The question asks whether a weak passive learner with a superpolynomial saving over \(2^{n}\) must imply dramatically faster passive learners. Targets range over standard polynomial-size circuit classes, and all examples are independent and uniform. The desired learners attain every fixed inverse-polynomial error in time \(2^{n^{\varepsilon}}\) for every fixed \(\varepsilon >0\). The source establishes this implication when learners may choose membership queries. A later generalized speedup still permits such queries in its conclusion, leaving the passive implication unestablished by that result.

[Read in atlas](index.html#TCS-4186) · [Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness](https://doi.org/10.4230/LIPIcs.CCC.2017.18) · [Conspiracies between Learning Algorithms, Circuit Lower Bounds and Pseudorandomness — full preprint](https://arxiv.org/abs/1611.01190) · [Learning algorithms from circuit lower bounds](https://doi.org/10.1007/s00037-024-00261-4)
Existing status: `open` · Summary written: 2026-09-12

## Cryptography (30)

### TCS-6545 — Public-key encryption from one-way functions

A one-way function is easy to evaluate and difficult for efficient classical algorithms to invert on a random input. Public-key encryption requires that anyone can encrypt with public information while a receiver can decrypt with a related secret key. The question asks whether the existence of any one-way function implies such a uniform classical scheme, allowing arbitrary non-black-box constructions. The scheme must have negligible average decryption error and hide an encrypted bit from every efficient chosen-plaintext observer. Oracle barriers do not settle the unrestricted implication, and a 2023 preprint claiming a positive solution remains unverified in this review.

[Read in atlas](index.html#TCS-6545) · [Foundations of Cryptography, Lecture 10](https://mit6875.github.io/FA23SLIDES/lec10.pdf) · [The Complexity of Public-Key Cryptography](https://eccc.weizmann.ac.il/report/2017/065/) · [Limits on the Provable Consequences of One-Way Permutations](https://www.cs.cmu.edu/~rudich/papers/oneway.ps) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [Merkle Puzzles are Optimal — an \(O(n^{2})\)-query attack on key exchange from a random oracle](https://www.boazbarak.org/Papers/merkle.pdf) · [Public-Key Encryption from the MinRank Problem](https://link.springer.com/chapter/10.1007/978-3-032-25327-9_16) · [Public-Key Encryption from Average Hard NP Language](https://eprint.iacr.org/2023/1260)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-0022 — One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)

The question asks whether P != NP alone guarantees a total efficiently computable function that is hard to invert on images of uniform inputs. One fixed function must defeat every fixed uniform classical polynomial-time inverter, even when finding any same-length preimage counts as success. Success must eventually be smaller than every inverse polynomial, with probability over the sampled input and the inverter’s independent coins. Current description-complexity characterizations and conditional-generator results retain specialized hardness premises or different guarantees. A complete Lean proof must establish the implication or its full negation, whose inversion guarantee is at arbitrarily large lengths rather than necessarily every sufficiently large length.

[Read in atlas](index.html#TCS-0022) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf) · [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.97) · [Cryptographic Implications of Worst-Case Hardness of Time-Bounded Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2026/051/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6550 — Circuit obfuscation from polynomial-hard LWE

Indistinguishability obfuscation hides which of two equally sized implementations of the same function was supplied. This card asks whether one fixed ordinary polynomial-hard LWE assumption implies such obfuscation for every polynomial circuit size. It specifies classical nonuniform security, exact noisy-equation parameters, a uniform polynomial-time obfuscator and simultaneous correctness on all inputs. Known cited constructions require several assumptions, stronger security regimes, or additional circular and leakage-related properties. Recent lattice candidates and iO-dependent applications do not establish the selected implication; an oracle or black-box barrier would not prove its full negation either.

[Read in atlas](index.html#TCS-6550) · [On the (Im)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007) · [Indistinguishability Obfuscation from LPN over \(\mathbb F_p\), DLIN, and PRGs in \(\mathrm{NC}^0\)](https://eprint.iacr.org/2021/1334) · [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.28) · [Lattice-Based Post-Quantum iO from Circular Security with Random Opening Assumption](https://eprint.iacr.org/2025/390) · [Lattice-based Obfuscation from NTRU and Equivocal LWE](https://eprint.iacr.org/2025/1129) · [How to Authenticate a Non-Deterministic Computation](https://eprint.iacr.org/2026/741) · [Trapdoor Functions with Secure Key Leasing and Copy Protection](https://arxiv.org/abs/2609.08423)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6551 — Unleveled fully homomorphic encryption from LWE alone

Fully homomorphic encryption lets a server evaluate computations on encrypted data and return a compact encrypted answer. Leveled schemes choose their keys after fixing a maximum computation depth. This project asks whether ordinary polynomial-modulus LWE can support keys generated without such a depth bound while preserving compactness. It specifically excludes additional circular-security or key-dependent-message assumptions often associated with bootstrapping. A solution would establish whether unrestricted encrypted computation follows from the stated LWE assumption with no extra security hypothesis.

[Read in atlas](index.html#TCS-6551) · [Efficient Fully Homomorphic Encryption from (Standard) LWE](https://epubs.siam.org/doi/10.1137/120868669) · [Quantum FHE (Almost) As Secure As Classical](https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf) · [Fully Homomorphic Encryption: definitional issues and open problems](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf) · [Bootstrapping Homomorphic Encryption via Functional Encryption](https://eprint.iacr.org/2023/1376.pdf) · [Bootstrapping Homomorphic Encryption via Functional Encryption — conference version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.17/LIPIcs.ITCS.2023.17.pdf) · [Dynamic multi-key FHE without CRS from LWE](https://link.springer.com/article/10.1186/s42400-025-00431-z) · [Efficient Quantum Fully Homomorphic Encryption](https://arxiv.org/abs/2604.23490)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0465 — Sub-square-root share-size exponents in perfect secret sharing

Secret sharing lets authorized groups reconstruct a secret while unauthorized groups learn nothing. The target asks for a universal bound \(K\cdot 2^{cn}\) bits per share for every n-party access structure, with \(c<1/2\) and a one-bit secret. Perfect reconstruction and privacy are required, and nonlinear schemes are allowed. Nir’s August 2026 preprint states a \(2^{0.496n+o(n)}\) bound that would meet this target. The claimed resolution is recorded with uncertain status because its proof has not been independently verified in this review.

[Read in atlas](index.html#TCS-0465) · [Algorithmic Aspects of Information Theory: open problems in secret sharing](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.12.7.180) · [The Share Size of Secret-Sharing Schemes for Almost All Access Structures and Graphs](https://eprint.iacr.org/2020/664) · [Resolving the Complexity of Linear Secret Sharing](https://eccc.weizmann.ac.il/report/2026/146/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7167 — Existence of one-way functions

Do classical one-way functions exist without an unproved hardness assumption? A polynomial-time function with negligible inversion success against every uniform classical polynomial-time adversary, or a proof that none exists. Complete candidates and complexity-theoretic equivalences are known; their required hardness has not been proved. An unconditional existence or impossibility theorem. Would establish or rule out the basic computational asymmetry behind many cryptographic primitives.

[Read in atlas](index.html#TCS-7167) · [The Tale of One-Way Functions](https://doi.org/10.1023/A:1023634616182) · [The Tale of One-way Functions](https://arxiv.org/abs/cs/0012023v5) · [On One-way Functions and Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2020/052/) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/) · [Research Interests: Randomness and Computation](https://www.cs.bu.edu/fac/lnd/research/ps-r.htm)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7168 — Existence of public-key encryption

Can public-key encryption be proved computationally secure without an unproved hardness assumption? An efficient correct scheme with negligible IND-CPA advantage against every uniform classical PPT adversary, or a proof that none exists. Constructions from lattice and other hardness assumptions are known. No checked result proves an appropriate hardness assumption or establishes unconditional existence. Would give a mathematical foundation for secret communication using only an authenticated public key.

[Read in atlas](index.html#TCS-7168) · [Foundations of Cryptography, Volume 2: Basic Applications](https://www.wisdom.weizmann.ac.il/~oded/foc-vol2.html) · [Encryption Schemes: draft chapter for Foundations of Cryptography](https://www.wisdom.weizmann.ac.il/~oded/PSBookFrag/enc.ps) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Post-Quantum Cryptography from Quantum Stabilizer Decoding](https://arxiv.org/abs/2603.19110)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7229 — Key agreement from one-way functions

A one-way function is easy to compute and hard for every efficient classical algorithm to invert on a random input. Key agreement asks two initially independent parties to produce the same secret by exchanging only public messages. The target asks whether the existence of any one-way function already implies such a uniform classical protocol, allowing arbitrary non-black-box constructions. The keys must agree with negligible error and remain indistinguishable from independent uniform keys even when an efficient observer sees the whole transcript. Oracle barriers do not refute this unrestricted implication, while a claimed positive construction of public-key encryption from 2023 remains unverified in this review.

[Read in atlas](index.html#TCS-7229) · [Limits on the Provable Consequences of One-Way Permutations](https://www.cs.cmu.edu/~rudich/papers/oneway.ps) · [Black-Box Uselessness: Composing Separations in Cryptography](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.47) · [On Bounded Storage Key Agreement and One-Way Functions](https://link.springer.com/chapter/10.1007/978-3-031-78011-0_10) · [Impossibility of Perfectly Complete Many-Round Key Agreement in the QROM](https://arxiv.org/abs/2608.03824v1) · [Public-Key Encryption from Average Hard NP Language](https://eprint.iacr.org/2023/1260)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-6549 — Oblivious transfer from public-key encryption

Oblivious transfer lets a receiver obtain one of two bits while hiding its choice from the sender. The receiver’s full view must reveal no more than its choice and the selected bit. The question asks whether ordinary public-key encryption alone implies such a classical protocol with static semi-honest standalone security. The card permits polynomial interaction and use of algorithm code, while fixing uniform simulators and nonuniform polynomial-size distinguishers. Oracle barriers and recent constructions with extra sampling, rerandomization or decoding assumptions do not settle the unrestricted implication.

[Read in atlas](index.html#TCS-6549) · [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf) · [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf) · [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882) · [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002) · [How to Steal Oblivious Transfer from Minicrypt](https://eprint.iacr.org/2026/113) · [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://www.jstage.jst.go.jp/article/transfun/E109.A/3/E109.A_2025CIP0019/_article/-char/en) · [Post-Quantum Cryptography from Quantum Stabilizer Decoding](https://arxiv.org/abs/2603.19110)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6547 — Collision-resistant hashing from one-way functions

The problem asks whether the existence of ordinary one-way functions implies a publicly keyed collision-resistant hash family. Honest algorithms are uniform and polynomial-time, while security must hold against every polynomial-size nonuniform classical circuit family. The hash compresses two security-parameter lengths to one, and an attacker chooses both colliding messages after seeing the freshly sampled public key. A complete Lean proof must establish the unrestricted existence implication or prove its negation, including the existence of a one-way function and the failure of every eligible hash family. Known oracle separations, stronger product-hardness constructions and the 2026 multicollision and interactive-argument results leave this ordinary-model implication unresolved.

[Read in atlas](index.html#TCS-6547) · [One-Way Functions are Necessary and Sufficient for Secure Signatures](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf) · [Finding collisions on a one-way street: Can secure hash functions be based on general assumptions?](https://link.springer.com/chapter/10.1007/BFb0054137) · [Cryptographic Hashing From Strong One-Way Functions: Or: One-Way Product Functions and their Applications](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f850.pdf) · [One-Way Functions vs. TFNP: Simpler and Improved](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.50) · [Doubly-Efficient Interactive Arguments for Bounded-Space from One-Way Functions](https://eccc.weizmann.ac.il/report/2026/111/) · [Black-Box Separation Between Multi-Collision Resistance and Collision Resistance](https://eccc.weizmann.ac.il/report/2026/046/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6546 — One-way permutations from one-way functions

A one-way permutation is an efficiently computable bijection that remains hard to invert on a random input. Unlike a general one-way function, it loses no information and gives each output exactly one preimage. This project asks whether arbitrary one-way functions imply an efficiently generated family of such permutations on full Boolean domains. The domain and security conventions matter because restricted-domain or differently keyed variants can express different requirements. A general construction would show that the unique-preimage structure comes for free from one-wayness rather than requiring a stronger assumption.

[Read in atlas](index.html#TCS-6546) · [Limits on the Provable Consequences of One-way Functions](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html) · [A Pseudorandom Generator from any One-way Function](https://epubs.siam.org/doi/10.1137/S0097539793244708) · [On Black-Box Separations among Injective One-Way Functions](https://link.springer.com/chapter/10.1007/978-3-642-19571-6_36) · [On Constructing One-Way Permutations from Indistinguishability Obfuscation](https://eprint.iacr.org/2015/752.pdf) · [On One-Shot Signatures, Quantum vs Classical Binding, and Obfuscating Permutations](https://arxiv.org/abs/2507.12456)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6548 — Chosen-ciphertext security from ordinary public-key encryption

Chosen-plaintext security protects an encrypted message even when an attacker can generate other encryptions. Chosen-ciphertext security additionally permits the attacker to obtain decryptions of adaptively chosen ciphertexts other than the challenge itself. This project asks whether any ordinary secure public-key encryption scheme can be upgraded to this stronger guarantee in the plain model. The upgrade must introduce no new computational assumption and may use techniques beyond black-box access to the original scheme. Establishing it would show that resistance to active decryption attacks is a general consequence of public-key encryption rather than a separate structural resource.

[Read in atlas](index.html#TCS-6548) · [CS 276 — Projects](https://theory.stanford.edu/~trevisan/cs276/projects.html) · [Towards a Separation of Semantic and CCA Security for Public Key Encryption](https://www.iacr.org/archive/tcc2007/43920433/43920433.pdf) · [Black-Box Construction of a Non-malleable Encryption Scheme from Any Semantically Secure One](https://www.cs.columbia.edu/~dglasner/MyPapers/non-mal.pdf) · [Realizing Chosen Ciphertext Security Generically in Attribute-Based Encryption and Predicate Encryption](https://www.iacr.org/archive/crypto2019/116940363/116940363.pdf) · [Chosen Ciphertext Security from Injective Trapdoor Functions](https://par.nsf.gov/servlets/purl/10295635) · [Chosen Ciphertext Security via BARGs](https://eprint.iacr.org/2023/1957) · [Threshold Public-Key Encryption: Definitions, Relations, and CPA-to-CCA Transforms](https://eprint.iacr.org/2025/1665)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6552 — Noninteractive zero knowledge from one-way functions

Noninteractive zero knowledge lets a prover demonstrate an NP statement with one message without revealing its witness. This project asks whether one-way functions suffice for reusable, adaptively secure arguments of this kind after an honest common-reference-string setup. Reusability means that the same public parameters must remain suitable as many statements are selected and proved. The target uses computational soundness and computational zero knowledge, so both guarantees are formulated against efficient adversaries. A construction would show that the setup model can support powerful noninteractive privacy guarantees from the basic assumption underlying symmetric cryptography.

[Read in atlas](index.html#TCS-6552) · [Commitment Schemes and Zero-Knowledge Protocols (2011)](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf) · [Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors](https://web.eecs.umich.edu/~cpeikert/pubs/nizk-lwe.pdf) · [Batch Arguments to NIZKs from One-Way Functions](https://eprint.iacr.org/2023/1938) · [Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash](https://eprint.iacr.org/2024/1514) · [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that \(\mathrm{NP} = \mathrm{PSPACE}\)?)](https://eccc.weizmann.ac.il/report/2024/116/) · [Non-Trivial Zero-Knowledge Implies One-Way Functions](https://arxiv.org/abs/2602.17651) · [Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way](https://doi.org/10.1007/978-3-032-35424-2_6)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6953 — One-way functions from errorless average-case NP hardness

This card selects the average-case-to-one-way-function branch of a broader question in Wigderson’s book. The hardness assumption concerns exact deterministic decision under an efficiently samplable distribution, with average polynomial time defined by a runtime moment. The conclusion requires a polynomial-time function that every uniform probabilistic inverter fails to invert with more than negligible probability at all sufficiently large lengths. Recent heuristic-hardness characterizations, infinitely-often security results and oracle separations use different guarantees. A resolution would clarify whether broad distributional hardness already forces the computational structure underlying classical one-wayness.

[Read in atlas](index.html#TCS-6953) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [On Building Fine-Grained One-Way Functions from Strong Average-Case Hardness](https://doi.org/10.1007/s00145-024-09518-1) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/) · [Quantum Pessiland](https://arxiv.org/abs/2608.29493)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7359 — Public-key quantum money from LWE alone

Public-key quantum money consists of a classical serial number and a reusable quantum note. Anyone can verify with the public key, but k honest notes must not enable production of k+1 accepted notes. This card fixes the decisional LWE parameters and asks for security under that assumption alone. Existing stronger-assumption constructions and restricted black-box barriers leave this implication unsettled. A complete answer must preserve both reusable correctness and security against polynomial-size quantum adversaries.

[Read in atlas](index.html#TCS-7359) · [Anonymous Public-Key Quantum Money and Quantum Voting](https://arxiv.org/abs/2411.04482) · [On Quantum Money and Evasive Obfuscation](https://eprint.iacr.org/2025/325) · [A General Quantum Duality for Representations of Groups with Applications to Quantum Money, Lightning, and Fire](https://mzhandry.github.io/pubs.quantum.html)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7276 — Average-case RSA inversion versus factoring for exponent 65537

Factoring an RSA modulus permits inversion of its encryption permutation. This card asks for a converse implication with exponent 65537 on a specified ensemble of balanced prime products. Both inversion and factoring are measured by inverse-polynomial average success of uniform polynomial-time algorithms. The implication allows unrestricted use of an inverter’s code and is not confined to black-box reductions. The fixed-exponent average-case question is an explicit specialization of the broader oracle question in Boneh’s survey.

[Read in atlas](index.html#TCS-7276) · [Twenty Years of Attacks on the RSA Cryptosystem](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7272 — Noninteractive SZK versus SZK

Statistical zero knowledge studies proofs whose verifier learns no statistically distinguishable information beyond the assertion being proved. The question is whether every such interactive proof can be replaced by a noninteractive proof with public randomness. The primary source expresses the same issue as a reduction between two promise problems on sampling circuits. The reduction must transform close or far pairs into distributions respectively close to or far from uniform. A deterministic polynomial-time reduction with the specified promises would establish NISZK equals SZK.

[Read in atlas](index.html#TCS-7272) · [Can Statistical Zero-Knowledge Be Made Non-Interactive? or On the Relationship of SZK and NISZK](https://doi.org/10.1007/3-540-48405-1_30) · [Can Statistical Zero-Knowledge Be Made Non-Interactive? or On the Relationship of SZK and NISZK](https://eccc.weizmann.ac.il/report/1999/013/download)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7277 — Fully homomorphic encryption from public-key encryption

Fully homomorphic encryption permits evaluating Boolean circuits over encrypted input bits. The question asks whether its existence follows from ordinary public-key encryption alone. Key generation must work without a supplied circuit-depth bound, and decryption cost must remain independent of the evaluated circuit. The scheme must remain secure with its evaluation key public. Known black-box barriers and implications from additional primitives do not settle this unrestricted existence implication.

[Read in atlas](index.html#TCS-7277) · [On the Power of Hierarchical Identity-Based Encryption](https://eprint.iacr.org/2015/815.pdf) · [Lecture 15: Fully Homomorphic Encryption](https://mit6875.github.io/LECNOTES/lec15.pdf) · [Bootstrapping Homomorphic Encryption via Functional Encryption](https://doi.org/10.4230/LIPIcs.ITCS.2023.17)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6454 — Low-noise LPN hardness from Nearest Codeword hardness

Learning parity with noise asks for information about hidden binary linear equations when some answers have been flipped. This project asks whether worst-case hardness of the binary nearest-codeword problem implies average-case hardness for a specified low-noise LPN distribution. The chosen regime uses quadratically many samples and a noise rate inversely proportional to the square root of the secret dimension. A reduction must produce that particular random-instance distribution rather than merely another hard coding problem or a different noise level. Such a connection would strengthen the theoretical foundation of low-noise LPN in the way worst-case reductions support lattice-based assumptions.

[Read in atlas](index.html#TCS-6454) · [Towards Worst-case Hardness for Low-Noise LPN](https://eccc.weizmann.ac.il/report/2026/095/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7274 — One-way functions in \(\mathrm{NC}^{0}\) from one-way functions

A one-way function is easy to evaluate but resists inversion on a uniformly chosen input by every polynomial-size adversary. The question asks whether the existence of any such function guarantees one whose Boolean circuits have a single constant depth bound. The circuits must be generated deterministically in polynomial time, while inversion security is required against nonuniform polynomial-size classical circuits. Known theorems establish this implication under restricted computational assumptions, and a 2025 source still explicitly lists the general implication as open. A complete Lean proof must establish the implication or prove both that general one-way functions exist and that every eligible local family is insecure.

[Read in atlas](index.html#TCS-7274) · [Cryptography in \(\mathrm{NC}^{0}\)](https://doi.org/10.1137/S0097539705446950) · [Hardness of KT Characterizes Parallel Cryptography](https://eccc.weizmann.ac.il/report/2021/057/) · [Non-Adaptive Universal One-Way Hash Functions from Arbitrary One-Way Functions](https://eccc.weizmann.ac.il/report/2022/049/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7278 — Identity-based encryption from arbitrary public-key encryption

Identity-based encryption lets a single public setup support exponentially many recipient identities. A trusted key generator derives the secret key for each requested identity. The adversary may obtain other identities’ keys before and after selecting the challenge recipient. The question asks whether such a scheme follows from ordinary public-key encryption alone. The cited generic-group limitation does not exclude arbitrary constructions outside that restricted model.

[Read in atlas](index.html#TCS-7278) · [Generic-Group Identity-Based Encryption: A Tight Impossibility Result](https://eprint.iacr.org/2021/745.pdf) · [Identity-Based Encryption from the Weil Pairing](https://crypto.stanford.edu/~dabo/pubs/papers/bfibe.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3025 — Exponentially hard weak versus strong one-way functions

The premise is a polynomial-time function that defeats exponential-size inversion circuits on an inverse-polynomial fraction of inputs. The question asks whether this already guarantees a function whose inversion success is negligible for exponential-size circuits. An attacker succeeds by finding any preimage of a challenge sampled from a uniform input. Ordinary repetition enlarges the input and can lose hardness exponential in the new length. Security-preserving results for regular functions do not settle the general case, which remains open in a 2025 revision.

[Read in atlas](index.html#TCS-3025) · [Hardness of KT Characterizes Parallel Cryptography](https://doi.org/10.4230/LIPIcs.CCC.2021.35) · [Hardness of KT Characterizes Parallel Cryptography — revision 2](https://eccc.weizmann.ac.il/report/2021/057/revision/2/download/) · [Security Preserving Amplification of Hardness](https://www.cs.utexas.edu/~diz/pubs/gilvz.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-2732 — Subpolynomial-key perfectly secure three-server DPFs

A distributed point function gives three servers compact shares of a vector supported at one secret location. Each server can evaluate its own share, and the three outputs must add to the requested point function. A single key must reveal exactly no information about either the location or the stored value. The target is a key length smaller than every positive power of the domain size over some fixed nontrivial finite Abelian group. Known subpolynomial constructions achieve perfect privacy with four servers or statistical privacy with three, a distinction retained in a 2026 survey.

[Read in atlas](index.html#TCS-2732) · [Information-Theoretic Distributed Point Functions](https://doi.org/10.4230/LIPIcs.ITC.2022.17) · [Efficient Information-Theoretic Distributed Point Function with General Output Groups](https://eprint.iacr.org/2023/625) · [Distributed Point Functions and Function Secret Sharing](https://arxiv.org/abs/2607.27696)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5013 — Sublinear communication for perfectly secure two-party computation

Two parties want to compute a Boolean circuit while keeping each input perfectly private. A trusted dealer can distribute correlated randomness before either input is supplied. The question asks whether polynomial setup and computation can give online communication sublinear in the circuit size, apart from the input-length cost. Such savings are known for layered circuits, while completely optimal communication can require exponential setup. The unresolved target covers arbitrary circuits with perfect passive privacy and shared outputs.

[Read in atlas](index.html#TCS-5013) · [Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation](https://doi.org/10.4230/LIPIcs.ITC.2023.18) · [A Note on the Communication Complexity of Multiparty Computation in the Correlated Randomness Model](https://eprint.iacr.org/2018/465) · [Correlated Pseudorandomness in Secure Computation](https://geoffroycouteau.github.io/assets/pdf/hdr.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1138 — Polynomial-time computationally sound verification of \(\#\mathrm{SAT}\)

The task is to check the exact number of satisfying assignments to a Boolean formula in polynomial time. An exponential-time honest prover supplies a short proof to a fully deterministic verifier. Even adversaries running in any polynomial in the honest prover’s time must almost never find a false counting claim that the verifier accepts. A 2025 theorem gives such verification for polynomial-space claims under strong hardness assumptions. This card asks whether the specified counting-verification system exists without those unproved assumptions.

[Read in atlas](index.html#TCS-1138) · [New ways of studying the BPP = P conjecture](https://eccc.weizmann.ac.il/report/2023/094/) · [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that NP = PSPACE?)](https://eccc.weizmann.ac.il/report/2024/116/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4754 — Unconditional zero knowledge for gap circuit complexity

The input is a complete truth table promised to have either a small or a much larger minimum circuit. The selected question asks for some fixed gap admitting an unconditional computational zero-knowledge proof. The verifier is efficient, while soundness must hold even against an unbounded cheating prover. All promised inputs and all input lengths must satisfy the guarantees. Average-case protocols and the later one-way-function characterization do not establish this membership.

[Read in atlas](index.html#TCS-4754) · [A Relativization Perspective on Meta-Complexity](https://doi.org/10.4230/LIPIcs.STACS.2022.54) · [Robustness of Average-Case Meta-Complexity via Pseudorandomness](https://doi.org/10.1145/3519935.3520051) · [One-Way Functions and Zero Knowledge](https://doi.org/10.1137/24M1689971)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5015 — Foundations of quantum cryptography from EFI pairs

Classical computational cryptography is organized around one-way functions as a basic necessary resource for many tasks. Quantum cryptography may rely on different forms of hardness, motivating the search for an analogous minimal primitive. The cited paper studies pairs of efficiently generated quantum states that are statistically far apart but computationally difficult to distinguish. It shows that these EFI pairs follow from many quantum cryptographic tasks and can also support significant zero-knowledge constructions. The entry introduces this foundational question together with that partial characterization, without asserting a universal equivalence covering every conceivable quantum primitive.

[Read in atlas](index.html#TCS-5015) · [On the Computational Hardness Needed for Quantum Cryptography](https://doi.org/10.4230/LIPIcs.ITCS.2023.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5793 — Pseudorandom functions from hardness of learning

Learning algorithms and pseudorandom functions express competing possibilities for understanding an unknown efficiently computable function. The selected question asks whether the ordinary failure of efficient learning already implies pseudorandom functions within the same circuit class. Earlier implications require a hard distribution over targets, which is stronger than saying that every learner fails on some target. The cited paper establishes a general equivalence in a nonuniform exponential-security regime, leaving those qualifications essential to its result. Extending the connection beyond that regime would explain when learning hardness alone supplies cryptographic pseudorandomness.

[Read in atlas](index.html#TCS-5793) · [Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness](https://doi.org/10.4230/LIPIcs.CCC.2017.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6692 — Linear-seed pseudorandom generators from one-way functions

Pseudorandom generators expand a short random seed into a longer string that efficient observers cannot distinguish from uniform randomness. General one-way functions are known to imply such generators, but the quantitative loss in seed length can be substantial. This problem asks for a fully explicit construction whose seed is only linear in the input length of the underlying one-way function while retaining the specified security dependence. The source contrasts arbitrary one-way functions with one-way permutations, where the desired kind of construction is already available. A tighter reduction would preserve much more of the original function's hardness when converting it into pseudorandomness.

[Read in atlas](index.html#TCS-6692) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6871 — Fully homomorphic encryption from worst-case hardness

Unbounded fully homomorphic encryption supports arbitrarily deep permitted computations on ciphertexts. The source asks to base such a scheme solely on worst-case complexity assumptions. Some constructions require additional assumptions about encryptions of secret-key-related information to enable repeated refresh operations. Removing those extra premises would connect the security guarantee more directly to foundational hard problems. The saved 2016 note does not name the precise extra assumptions or compactness conventions, so its current status and exact target require separate review rather than treating any lattice-based FHE scheme as a resolution.

[Read in atlas](index.html#TCS-6871) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

## Quantum computation and information (52)

### TCS-6446 — Quantum PCP conjecture with classical reductions

A local Hamiltonian describes a quantum system through bounded-strength interactions on a fixed number of qubits at a time. The question asks whether distinguishing two constant-separated ranges of its average ground energy is as hard as every problem with a quantum witness verifier. The saved variant requires deterministic classical reductions, a stronger requirement than the original survey’s formulation allowing quantum reductions. All global quantum states are allowed, and neither growing locality nor a vanishing normalized gap meets the target. Known low-energy state complexity, interactive verification and restricted gap-amplification results leave the stated hardness question unresolved in the checked sources.

[Read in atlas](index.html#TCS-6446) · [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495v1) · [NLTS Hamiltonians from good quantum codes](https://arxiv.org/abs/2206.13228v4) · [The status of the quantum PCP conjecture (games version)](https://arxiv.org/abs/2403.13084v1) · [Quantum PCPs: on Adaptivity, Multiple Provers and Reductions to Local Hamiltonians](https://arxiv.org/abs/2403.04841v3) · [Derandomised tensor product gap amplification for quantum Hamiltonians](https://arxiv.org/abs/2510.01333v1) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588v1) · [Gap Amplification for Local Hamiltonians with Combinatorial Soundness](https://simons.berkeley.edu/talks/quynh-t-nguyen-harvard-university-2026-07-23) · [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0036 — BPP versus BQP

BPP and BQP are classes of total decision languages with bounded error separately on every input, using classical randomness and quantum circuits respectively. The quantum model uses one polynomial-time classical generator for finite H, T and CNOT circuits with auxiliary qubits initialized to zero and one final measured bit. The question asks whether some quantum polynomial-time language has no classical randomized polynomial-time decider; the alternative is equality of the classes. Factoring algorithms, oracle separations and shallow sampling lower bounds retain assumptions or output/resource differences that do not establish this full separation. A September 2026 oracle result further distinguishes total-language equality from promise-class equality, while the ordinary total-language target remains unresolved in the inspected sources.

[Read in atlas](index.html#TCS-0036) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [On Universal and Fault-Tolerant Quantum Computing](https://arxiv.org/abs/quant-ph/9906054) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027v2) · [Oracle Separation of BQP and PH](https://doi.org/10.1145/3530258) · [Unconditional Quantum Advantage for Sampling with Shallow Circuits](https://quantum-journal.org/papers/q-2026-08-12-2188/) · [Promises should be taken seriously: On relativization with promise problems](https://arxiv.org/abs/2609.07945)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6516 — Area law for gapped two-dimensional Hamiltonians

An area law says that entanglement between a region and its surroundings grows with the region's boundary rather than its volume. This problem asks for such a bound for the unique ground state of a general two-dimensional local Hamiltonian with a fixed positive spectral gap. Interaction strength, local dimension, and interaction range are held fixed as the lattice grows. Known routes involving frustration-free systems or additional conditions do not automatically establish the unrestricted statement recorded here. A solution would clarify how strongly locality and an energy gap constrain many-body quantum states, without by itself supplying an efficient algorithm to find them.

[Read in atlas](index.html#TCS-6516) · [An Area Law for One Dimensional Quantum Systems](https://arxiv.org/abs/0705.2024v4) · [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492v3) · [Entanglement spread area law in gapped ground states](https://doi.org/10.1038/s41567-022-01740-7) · [Area Laws and Tensor Networks for Maximally Mixed Ground States](https://doi.org/10.1007/s00220-026-05554-z) · [Quantum matter is weakly entangled at low energies](https://arxiv.org/abs/2604.14143v1) · [Two-dimensional local Hamiltonian problem with area laws is QMA-complete](https://doi.org/10.1016/j.jcp.2021.110534)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6580 — Information-theoretic classical verification of quantum computation

A classical user wants to check whether an explicitly given quantum circuit accepts with high probability. One uniform quantum polynomial-time honest prover must convince the user on every YES circuit using only classical messages. The verifier must reject NO circuits with high probability even against an unbounded adaptive cheating strategy. Known positive results use limited quantum verifier resources, separated provers, or computational hardness assumptions. The inspected 2026 literature retains the full single-prover information-theoretic question as open; narrower new protocols and barriers do not settle it.

[Read in atlas](index.html#TCS-6580) · [Verification of quantum computation: An overview of existing approaches](https://arxiv.org/abs/1709.06984) · [Interactive Proofs for Quantum Computations](https://arxiv.org/abs/1704.04487) · [A classical leash for a quantum system: Command of quantum systems via rigidity of CHSH games](https://arxiv.org/abs/1209.0448) · [Classical Verification of Quantum Computations](https://arxiv.org/abs/1804.01082) · [How to Classically Verify a Quantum Cat without Killing It](https://arxiv.org/abs/2602.09282) · [Separating Non-Interactive Classical Verification of Quantum Computation from Falsifiable Assumptions](https://arxiv.org/abs/2602.18034) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952) · [Verification of Quantum Computations Without Trusted Preparations or Measurements](https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202501018)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6518 — NPT bound entanglement

Entangled states can sometimes be converted into nearly perfect shared Bell pairs using many copies and local operations with classical communication. Bound entanglement means that this distillation remains impossible despite the presence of entanglement. The question asks whether such states can have a negative partial transpose, a spectral property associated with distillability in simpler settings. Failure of a protocol on one copy or any fixed number of copies does not establish the required obstruction for every number of copies. Resolving the question would sharpen the distinction between entanglement as a property and entanglement as a usable communication resource.

[Read in atlas](index.html#TCS-6518) · [Mixed-state entanglement and distillation: is there a “bound” entanglement in nature?](https://arxiv.org/abs/quant-ph/9801069) · [Evidence for Bound Entangled States with Negative Partial Transpose](https://arxiv.org/abs/quant-ph/9910026) · [A solution to 2-copy distillability of Werner states](https://arxiv.org/abs/2607.21367) · [On the two-copy distillability of Werner states and a new partial trace inequality](https://arxiv.org/abs/2607.24309) · [Two-copy nondistillability of Werner states: sharp partial-trace inequalities and finite-copy extensions](https://arxiv.org/abs/2607.24479) · [Sharp Plucker Geometry for Three-Copy Werner Distillation](https://arxiv.org/abs/2608.02647)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6515 — Asymptotically good quantum locally testable stabilizer codes

A locally testable quantum code should reveal a substantial error by checking only a few qubits. The desired family must also encode a linear amount of quantum information and tolerate errors on a linear number of physical qubits. Each check and each qubit's participation in checks must remain bounded as the code grows. These requirements strengthen ordinary good quantum LDPC codes by demanding a quantitative relation between distance from the code space and rejection probability. Such codes would connect robust quantum error detection with the complexity of low-energy states and the broader search for quantum PCP constructions.

[Read in atlas](index.html#TCS-6515) · [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/) · [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654) · [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8) · [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476) · [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228) · [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588) · [Robust Local Testability of Tensor Products of Constant-Rate Algebraic Geometry Codes](https://eccc.weizmann.ac.il/report/2025/136/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6517 — Passive quantum memory in three dimensions

Passive quantum memory aims to preserve an encoded qubit through the natural dynamics of a material without repeated active correction. The question here fixes a nonzero temperature and asks whether lifetime can grow without bound in a three-dimensional local stabilizer system. Protecting a qubit requires retaining phase information as well as distinguishing its classical basis states. The saved card records a May 2026 claimed affirmative construction, while distinguishing its proof claim from an independently verified conclusion. This makes the record a useful guide to the precise thermal model and remaining verification questions rather than an unqualified assertion that the original existence problem is still open.

[Read in atlas](index.html#TCS-6517) · [Thermodynamic stability criteria for a quantum memory based on stabilizer and subsystem codes](https://arxiv.org/abs/0907.2807) · [Quantum memories at finite temperature](https://arxiv.org/abs/1411.6643) · [Symmetry protected self correcting quantum memory in three space dimensions](https://arxiv.org/abs/2103.08622) · [Cored product codes for quantum self-correction in three dimensions](https://arxiv.org/abs/2510.05479) · [A passive self-correcting quantum memory in three dimensions](https://arxiv.org/abs/2605.10943) · [Partial Self-Correction in Layer Codes](https://journals.aps.org/prl/abstract/10.1103/mb89-8436)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6519 — Quantum capacity of the qubit depolarizing channel

A depolarizing channel models a qubit subjected to randomly chosen Pauli errors. Its quantum capacity measures how much unknown quantum information can be transmitted reliably per channel use when many uses are encoded together. The goal is the capacity curve throughout the noise range under the unassisted coding convention fixed in the card. Coding across several uses can behave differently from optimizing a single use, which complicates attempts to match achievable rates with impossibility bounds. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-6519) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Quantum cloning and the capacity of the Pauli channel](https://arxiv.org/abs/quant-ph/9803058) · [Quantum and private capacities of low-noise channels](https://arxiv.org/abs/1705.04335) · [Geometric optimization for quantum communication](https://arxiv.org/abs/2509.15106) · [Enhanced quantum capacity thresholds from symmetry](https://arxiv.org/abs/2605.09138) · [A certified lower bound on the quantum-capacity threshold of the depolarizing channel](https://arxiv.org/abs/2608.15870) · [Sharp Quantum Capacity Thresholds: Exponential Strong Converses for Degradable and Antidegradable Channels](https://arxiv.org/abs/2608.01308)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0037 — NP outside BQP

NP consists of total decision languages with polynomial-length classical certificates checkable in deterministic polynomial time. The question is whether at least one such language has no uniform bounded-error quantum polynomial-time decider, equivalently whether full 3-SAT is outside BQP. The quantum model has a fixed finite universal gate set, polynomially many zero-initialized auxiliary qubits and a final membership-bit measurement, with no supplied witness or oracle. Structured quantum algorithms and unstructured-search or oracle lower bounds do not settle the unrestricted explicit-input comparison. Recent Pauli-coefficient hardness remains conditional on this noncontainment, while nonlinear quantum computation adds operations outside the model.

[Read in atlas](index.html#TCS-0037) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [On Universal and Fault-Tolerant Quantum Computing](https://arxiv.org/abs/quant-ph/9906054) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027v2) · [A fast quantum mechanical algorithm for database search](https://arxiv.org/abs/quant-ph/9605043) · [Strengths and Weaknesses of Quantum Computing](https://arxiv.org/abs/quant-ph/9701001) · [Complexity of detecting large coefficients in the Pauli basis](https://arxiv.org/abs/2606.19545) · [Quantum algorithm for Valiant-Vazirani reduction](https://arxiv.org/abs/2606.18428v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6448 — QMA versus QCMA

QMA and QCMA use efficient quantum verifiers but allow quantum and classical witnesses respectively. A witness can depend on the entire input and is untrusted, so soundness must hold against every permitted message. The question is equality of the ordinary uniform promise classes without oracle access or shared advice. Quantum-oracle and, more recently, classical-oracle separations give evidence about the role of quantum witnesses without separating the ordinary classes. The revised card fixes the finite-circuit model and requires a complete Lean proof of containment or a universally valid separating problem.

[Read in atlas](index.html#TCS-6448) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/) · [Quantum Versus Classical Proofs and Advice](https://theoryofcomputing.org/articles/v003a007/) · [Separating QMA from QCMA with a classical oracle](https://arxiv.org/abs/2511.09551v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6520 — Computability of quantum channel capacity

Quantum channel capacity describes the best asymptotic rate for transmitting quantum information through a noisy channel. This problem asks whether that number can always be approximated by an algorithm from an effective finite description of the channel. The algorithm may be slow, but it must halt and meet any requested rational accuracy. Optimizations involving arbitrarily many channel uses make the asymptotic definition harder to turn into a guaranteed finite computation. Establishing computability or an obstruction would separate the existence of an operational communication rate from our ability to calculate it even in principle.

[Read in atlas](index.html#TCS-6520) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Continuity of quantum channel capacities](https://arxiv.org/abs/0810.4931) · [Unbounded number of channel uses may be required to detect quantum capacity](https://www.nature.com/articles/ncomms7739) · [Undecidability in Physics: a Review](https://arxiv.org/abs/2410.16532) · [Undecidability in physics: A review — journal version](https://doi.org/10.1016/j.physrep.2025.06.004) · [On the undecidability of quantum channel capacities](https://arxiv.org/abs/2601.22471)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3709 — Quantum query-to-communication lifting

A lifting theorem would turn the quantum query complexity of a Boolean promise problem into the communication complexity of a composed two-party problem. The question asks for one gadget per input length that works for every partial outer function. Both complexity measures should agree up to common polylogarithmic factors. The communication model allows arbitrary prior entanglement and an unrestricted number of rounds. Known bounded-round, adversary and hybrid lifting results leave this general bounded-error transfer open in the checked 2026 source.

[Read in atlas](index.html#TCS-3709) · [Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.TQC.2019.2) · [CS 860: Quantum Lower Bounds — Week 8, Communication Complexity Basics](https://cs.uwaterloo.ca/~s4bendav/CS860/CS860S20week8.pdf) · [On Query-To-Communication Lifting for Adversary Bounds](https://doi.org/10.4230/LIPIcs.CCC.2021.30) · [A Lifting Theorem for Hybrid Classical-Quantum Communication Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2026.155)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4737 — QMA versus \(\mathrm{QMA}_1\) over Clifford+T

A perfectly complete quantum proof system accepts some valid witness with probability exactly one. This question asks whether every QMA proof system can achieve that guarantee without sacrificing efficient verification or soundness. Approximate gate synthesis creates a special difficulty because a tiny implementation error can destroy exact acceptance. Two September 2026 preprints now claim finite-register perfect completeness with fixed gates that cover this card’s exact Clifford+T model. Their stated results match the target, whose status is uncertain pending independent proof verification.

[Read in atlas](index.html#TCS-4737) · [Towards a Universal Gateset for QMA1](https://doi.org/10.4230/LIPIcs.MFCS.2026.98) · [On Perfect Completeness for QMA](https://arxiv.org/abs/0806.0450) · [Quantum-Merlin-Arthur Problems Have Perfect Completeness with an Infinite Counter](https://journals.aps.org/prl/abstract/10.1103/pwdd-htbf) · [QMA has perfect completeness](https://arxiv.org/abs/2609.13032) · [Achieving perfect completeness for one- and two-message quantum proof systems](https://arxiv.org/abs/2609.15926)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-4952 — Quantum–classical communication gaps for total functions

Alice and Bob must compute a Boolean function defined on every pair of their binary inputs. The target is an infinite family requiring polynomial randomized classical communication but only polylogarithmic quantum communication in the input length. Local computation is free, classical public randomness and arbitrary interaction are allowed, and the quantum side may share input-independent entanglement. The 2021 source’s separate efficient-player result concerns partial functions and does not impose an additional runtime condition here. August and September 2026 preprints make matching total-function separation claims whose complete proofs remain unverified in this review.

[Read in atlas](index.html#TCS-4952) · [Quantum Versus Randomized Communication Complexity, with Efficient Players](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.54) · [On the quantum communication complexity of total functions](https://arxiv.org/abs/2608.18784) · [Improved Separations between Quantum and Classical Communication Complexity of Total Functions](https://arxiv.org/abs/2609.16726)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6459 — Entanglement without distillable secret key

Shared quantum states can sometimes be converted into secret classical keys by local operations and public communication. This project asks whether there are entangled states from which no secret key can be distilled. Separable states provide a known class of useless resources, but entanglement alone does not immediately determine the distillable-key rate. The question is also different from asking whether an entangled state can produce maximally entangled pairs. Identifying an entangled key-undistillable state, or proving that none exists, would settle a basic boundary in the resource theory of private communication.

[Read in atlas](index.html#TCS-6459) · [Cost of quantum secret key](https://doi.org/10.22331/q-2026-05-06-2098) · [Secure key from bound entanglement](https://arxiv.org/abs/quant-ph/0309110) · [No-go theorem for heralded exact one-way key distillation](https://doi.org/10.22331/q-2026-03-10-2020) · [Bipartite Bound Information Exists](https://arxiv.org/abs/2607.25838)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6521 — Dihedral hidden subgroup problem in BQP

The dihedral hidden subgroup problem presents a function that is constant on cosets of an unknown subgroup of a dihedral group. The task is to recover generators for that subgroup using quantum access to the function. The target is a uniform algorithm whose total running time is polynomial in the length of the group description and oracle values. Counting only a small number of oracle queries is insufficient if processing the resulting quantum information is expensive. An efficient solution would extend the reach of hidden-subgroup methods beyond the abelian setting and illuminate connections with lattice-related algorithmic problems.

[Read in atlas](index.html#TCS-6521) · [Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333) · [A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345) · [The dihedral hidden subgroup problem](https://arxiv.org/abs/2106.09907) · [A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with Polynomial Space](https://arxiv.org/abs/quant-ph/0406151) · [Quantum Computation and Lattice Problems](https://cims.nyu.edu/~regev/papers/quantum_average.pdf) · [A Quantum Polynomial-Time Solution to The Dihedral Hidden Subgroup Problem](https://arxiv.org/abs/2202.09697) · [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591) · [The ePrint:2026/1591 Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693) · [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598) · [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6522 — Graph isomorphism in BQP

Two graphs are isomorphic when a relabeling of vertices preserves every edge. This question asks whether a quantum algorithm can decide that equivalence in polynomial time for every pair of explicitly given graphs. The algorithm must include all processing costs and achieve bounded error, rather than merely extract a small amount of information from an oracle. Symmetry makes graph isomorphism a natural testing ground for quantum methods, but quantum access to related group structure is not itself a complete algorithm. A resolution would clarify whether quantum computation can efficiently handle this central classification problem.

[Read in atlas](index.html#TCS-6522) · [Ten Semi-Grand Challenges for Quantum Computing Theory](https://www.scottaaronson.com/writings/qchallenge.html) · [A Quantum-Inspired Algorithm for Graph Isomorphism](https://arxiv.org/abs/2512.24423) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/) · [Limitations of Quantum Coset States for Graph Isomorphism](https://arxiv.org/abs/quant-ph/0511148) · [Quantum state isomorphism problems for groups](https://arxiv.org/abs/2605.12615) · [NPA Hierarchy for Quantum Isomorphism and Homomorphism Indistinguishability](https://quantum-journal.org/papers/q-2026-01-28-1989/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6933 — Classical hardness of approximate Boson Sampling

Boson Sampling records the occupations of indistinguishable photons after an ideal passive optical network. The selected question asks whether no uniform classical randomized algorithm can reproduce every such distribution to any requested total-variation error in time polynomial in the input size and inverse error. The distribution includes collisions and is defined by squared permanents with factorial normalization. Known hierarchy-collapse consequences and newer average-case results have explicit assumptions or use different error guarantees. An unconditional answer would establish or refute a fundamental classical limitation for a restricted quantum sampling experiment.

[Read in atlas](index.html#TCS-6933) · [Quantum Algorithms: An Overview](https://arxiv.org/abs/1511.04206) · [The Computational Complexity of Linear Optics](https://theoryofcomputing.org/articles/v009a004/) · [Exponential improvements to the average-case hardness of BosonSampling](https://arxiv.org/abs/2411.04566)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2229 — QMA versus \(\mathrm{QMA}(2)\)

QMA(2) receives two quantum witnesses that are promised unentangled across a specified division, whereas QMA receives one unrestricted quantum witness. Both use uniform polynomial-time quantum verification with constant completeness and soundness error. The question is whether the promise of unentanglement adds power for ordinary promise problems without an oracle. Known amplification and restricted-phase results do not resolve this comparison, and concatenating honest witnesses does not preserve soundness automatically. A September 2026 manuscript separates the classes relative to a unitary oracle while explicitly leaving their ordinary relationship unresolved.

[Read in atlas](index.html#TCS-2229) · [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9) · [Testing Product States, Quantum Merlin-Arthur Games and Tensor Optimization](https://doi.org/10.1145/2432622.2432625) · [A quantum oracle separation between QMA(2) and QMA](https://arxiv.org/abs/2609.02865v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4615 — Quantum entropy inequalities beyond strong subadditivity

For a multipartite quantum state, the entropies of all subsystems form a vector subject to universal inequalities. Positivity and strong subadditivity give basic constraints on those vectors. This question asks whether additional inequalities are needed to describe the quantum entropy cone for four or more parties. The cited stabilizer-state analysis relates the problem to classical non-Shannon inequalities and to states violating the Ingleton inequality. New constraints or counterexamples would sharpen the mathematical description of how quantum information can be shared among several systems.

[Read in atlas](index.html#TCS-4615) · [The Quantum Entropy Cone of Stabiliser States](https://doi.org/10.4230/LIPIcs.TQC.2013.270) · [Quantum Entropy Prover](https://arxiv.org/abs/2501.16025) · [Exploring the holographic entropy cone via reinforcement learning](https://arxiv.org/abs/2601.19979)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7308 — Bell nonlocality from finitely many copies of every entangled state

Entanglement and Bell nonlocality are distinct properties of quantum states and measurement correlations. The question asks whether every entangled bipartite state becomes Bell-nonlocal after local filtering of some finite number of copies. The filter must succeed before measurement settings are selected, and no extra shared entangled state is provided. Single-copy counterexamples, auxiliary-state activation and four-party broadcast results address different resource models. A full answer would determine whether repeated copies of the state itself always make its entanglement observable through a conventional bipartite Bell violation.

[Read in atlas](index.html#TCS-7308) · [All entangled states display some hidden nonlocality](https://arxiv.org/abs/1210.0548) · [Entanglement without hidden nonlocality](https://arxiv.org/abs/1606.02215) · [All Entangled States are Nonlocal and Self-Testable in the Broadcast Scenario](https://arxiv.org/abs/2512.15656)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4753 — \(\mathrm{QMA}(2)\) versus NEXP

The question asks whether polynomial-time verification of two unentangled polynomial-length quantum proofs captures nondeterministic exponential time. It compares ordinary promise classes with a fixed constant acceptance gap and no oracle or advice. NEXP already contains QMA(2), so the unresolved direction is verification of every NEXP promise problem by the two-proof model. Exponentially small-gap and nonnegative-amplitude variants have stronger known characterizations that do not automatically transfer to this model. Recent amplification and oracle results retain those distinctions and do not establish ordinary QMA(2) equals NEXP.

[Read in atlas](index.html#TCS-4753) · [Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement](https://doi.org/10.4230/LIPIcs.ITCS.2023.53) · [Testing Product States, Quantum Merlin-Arthur Games and Tensor Optimization](https://doi.org/10.1145/2432622.2432625) · [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9) · [Near-Optimal Gap Amplification for Nonnegative Unentangled Quantum Proofs](https://arxiv.org/abs/2608.07986v1) · [A quantum oracle separation between QMA(2) and QMA](https://arxiv.org/abs/2609.02865v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0029 — Maximum randomized-versus-quantum gap for total functions

The question asks for the largest polynomial quantum query advantage over randomized algorithms on total Boolean functions. Both models must answer correctly with probability at least two thirds on every input. Only queries to input bits are counted, with other computation and workspace unrestricted. Known results put the optimal separation exponent between three and four. The target is to certify that exponent within one hundredth, without resolving finer logarithmic factors.

[Read in atlas](index.html#TCS-0029) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem](https://arxiv.org/abs/2010.12629) · [k-Forrelation Optimally Separates Quantum and Classical Query Complexity](https://arxiv.org/abs/2008.07003)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1961 — One-way state generators versus EFI pairs

EFI pairs are easy to generate quantum states that are statistically different but computationally difficult to distinguish. One-way state generators instead hide a classical key while allowing an efficient quantum verifier to check candidate keys. This card asks whether existence of EFI pairs already guarantees such an efficiently verifiable generator in the ordinary model. The adversary may have polynomial classical advice and polynomially many independently generated copies of the hidden-key state. Known equivalence with unlimited verification and separation relative to a quantum oracle leave distinct issues from this precisely selected implication.

[Read in atlas](index.html#TCS-1961) · [One-Wayness in Quantum Cryptography](https://doi.org/10.4230/LIPIcs.TQC.2024.4) · [Commitments are equivalent to statistically-verifiable one-way state generators](https://arxiv.org/abs/2404.03220v4) · [A New World in the Depths of Microcrypt: Separating OWSGs and Quantum Money from QEFID](https://arxiv.org/abs/2410.03453v3) · [Equivalence Between Average-Case Hardness of Learning and Cryptography for Mixed Quantum States](https://arxiv.org/abs/2608.14331v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6481 — Bosonic quantum computation in PP

The selected question asks whether Gaussian-and-cubic bosonic computation is contained in the classical counting class PP. The model uses coherent input states, polynomial evolution time and a final number measurement with separated acceptance intervals. No exponential bound on intermediate energy is added to the original formal decision model. Later PSPACE and PP simulations require additional energy assumptions and therefore do not settle this target. A resolution would clarify the computational significance of high photon numbers in infinite-dimensional quantum computation.

[Read in atlas](index.html#TCS-6481) · [Bosonic Quantum Computational Complexity](https://doi.org/10.22331/q-2026-05-20-2110) · [Bounding the computational power of bosonic systems](https://doi.org/10.1038/s41534-026-01255-6) · [Energy, Bosons and Computational Complexity](https://arxiv.org/abs/2510.08545)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2408 — Remote state preparation from quantum-secure one-way functions

Remote state preparation lets a classical client use classical messages to leave a quantum server holding states whose descriptions are known to the client. This card asks whether quantum-advice-secure classical one-way functions suffice for the source’s parallel BB84 protocol guarantee. Its accepted output must resemble independent uniformly valued BB84 states up to an efficient server-side isometry, with tunable inverse-polynomial computational error and advice independent of the hidden basis. Known constructions use more structured trapdoor assumptions, while later papers distinguish this rigidity guarantee from basis hiding and composable simulation. The selected model is an explicit editorial interpretation of the broad source question, and checked oracle barriers do not refute its full standard-model existence implication.

[Read in atlas](index.html#TCS-2408) · [Quantum Cryptography with Classical Communication: Parallel Remote State Preparation for Copy-Protection, Verification, and More](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.67) · [Quantum cryptography with classical communication: parallel remote state preparation for copy-protection, verification, and more — full version](https://arxiv.org/abs/2201.13445v2) · [Formulations and Constructions of Remote State Preparation with Verifiability, with Applications](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.96) · [On the Power of Oblivious State Preparation](https://link.springer.com/chapter/10.1007/978-3-032-01878-6_19) · [A Modular Approach to Succinct Arguments for QMA](https://arxiv.org/abs/2606.10408v1) · [Impossibility of Perfectly Complete Many-Round Key Agreement in the QROM](https://arxiv.org/abs/2608.03824v1) · [Towards the Impossibility of Imperfectly Complete Key Agreement in the QROM](https://arxiv.org/abs/2608.17610v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4811 — Efficient approximation of the optimal dihedral measurement

The selected question asks for efficient approximation of one explicitly defined optimal quantum measurement. Its input space contains several dihedral coset-state registers, and its outcomes are candidate hidden shifts plus a complementary outcome. The measurement is defined by the inverse square root of the sum of the ensemble states, with an explicit convention on its kernel. The required circuit must reproduce its outcome distribution uniformly on valid inputs to any requested inverse-polynomial accuracy. Known subset-sum connections constrain particular unitary implementations and do not establish hardness for every measurement circuit.

[Read in atlas](index.html#TCS-4811) · [How Hard Is Deciding Trivial Versus Nontrivial in the Dihedral Coset Problem?](https://doi.org/10.4230/LIPIcs.TQC.2016.6) · [Optimal measurements for the dihedral hidden subgroup problem](https://arxiv.org/abs/quant-ph/0501044) · [The dihedral hidden subgroup problem](https://doi.org/10.1515/jmc-2022-0029) · [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4894 — Parity versus \(\mathrm{AC}^{0}\) with shallow quantum preprocessing

Parity is a basic function that small constant-depth classical circuits cannot approximate well on uniformly random inputs. This project asks whether a shallow quantum preprocessing stage can remove that limitation when its measured output is passed to a classical AC0 circuit. The conjecture concerns constant-depth quantum circuits with bounded-fan-in gates, followed by the specified classical postprocessing. Any approximation guarantee must account for both the random input and the randomness of quantum measurement. Establishing the conjecture would place a concrete limit on hybrid computation and help clarify the power of weak classical procedures that use shallow quantum devices.

[Read in atlas](index.html#TCS-4894) · [Parity vs. AC0 with Simple Quantum Preprocessing](https://doi.org/10.4230/LIPIcs.ITCS.2024.92) · [Unconditional Pseudorandomness Against Shallow Quantum Circuits](https://doi.org/10.4230/LIPIcs.ITCS.2026.70)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6449 — Quantum versus classical nonuniform advice

Quantum and classical advice supply information fixed for an entire input length to an efficient quantum computation. The selected advice must decide every binary input of that length correctly with bounded error, and can be arbitrarily hard to prepare. The question asks whether quantum advice increases the resulting ordinary class of total languages. A known simulation by PP with classical advice uses a different error and computation model, while successive oracle separations retain their black boxes. The latest standard classical-oracle separation does not resolve the ordinary equality, and fresh-copy advice remains distinct from untrusted per-instance witnesses.

[Read in atlas](index.html#TCS-6449) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/) · [Limitations of Quantum Advice and One-Way Communication](https://arxiv.org/abs/quant-ph/0402095) · [Quantum Versus Classical Proofs and Advice](https://theoryofcomputing.org/articles/v003a007/) · [Classical vs Quantum Advice and Proofs Under Classically-Accessible Oracle](https://doi.org/10.4230/LIPIcs.ITCS.2024.72)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0033 — Quantum query complexity versus bounded approximate degree

The question compares quantum query complexity with polynomials that approximate a promised Boolean function. The polynomial must remain between zero and one even on inputs outside the promise. The target is the largest quantum query complexity possible at each input length and bounded-degree budget. A 2023 theorem already proves that the gap can be exponential, so that subquestion is no longer open. The remaining task is to determine the full extremal bound up to universal multiplicative constants.

[Read in atlas](index.html#TCS-0033) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [An Exponential Separation Between Quantum Query Complexity and the Polynomial Degree](https://doi.org/10.4230/LIPIcs.CCC.2023.24) · [Separations in Query Complexity for Total Search Problems](https://arxiv.org/abs/2410.16245)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5021 — Limiting optimized QAOA energy in the SK model

QAOA is a widely studied quantum optimization ansatz using alternating objective and mixing operations. The SK model provides a canonical random quadratic objective with a known limiting optimum. The question asks for the best limiting energy reachable by finite-depth QAOA when depth is subsequently allowed to grow. Angles are optimized only after taking the infinite-size ensemble limit. The source conjectures that this limiting value reaches the Parisi optimum, and the card now accepts a proved numerical determination within 0.01.

[Read in atlas](index.html#TCS-5021) · [The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model](https://doi.org/10.4230/LIPIcs.TQC.2022.7)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-1882 — Optimal quantum query complexity of uniformity testing

Uniformity testing distinguishes a perfectly uniform distribution from one separated in total variation distance. The tester can coherently call a unitary preparing the distribution, its inverse and its controlled version. Its guarantee must hold for arbitrary garbage states and arbitrary valid unitary extensions. The target is the optimal query count jointly in domain size and distance, up to universal factors. The source supplies a candidate upper bound whose matching lower bound remains conjectural.

[Read in atlas](index.html#TCS-1882) · [Uniformity Testing When You Have the Source Code](https://doi.org/10.4230/LIPIcs.TQC.2025.7) · [Uniformity testing when you have the source code — version record](https://arxiv.org/abs/2411.04972v1)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0861 — \(\mathrm{QMA}(2)\) versus \(\mathrm{BQEXP}\)

The question asks whether every problem with two unentangled quantum proofs can be decided in quantum exponential time without proofs. The verifier is polynomial-time and may process both proofs jointly, but the proofs must initially be a product state. The deciding algorithm must be uniform and have bounded error on every promised input. The standard upper bound uses nondeterministic exponential time, which does not give the requested algorithm. Recent quantified and stoquastic results concern different upper-bound models and leave this inclusion unresolved.

[Read in atlas](index.html#TCS-0861) · [Is QMA(2) in BQEXP?](https://tcsopenproblems.com/problem/9) · [Testing Product States, Quantum Merlin-Arthur Games and Tensor Optimisation](https://arxiv.org/abs/1001.0017) · [On the Pure Quantum Polynomial Hierarchy and Quantified Hamiltonian Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2026.103) · [The Power of Unentanglement Without Destructive Interference](https://arxiv.org/abs/2604.27886)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4715 — Succinct entangled proofs with efficient provers

The question asks a classical verifier to check a quantum circuit’s acceptance using two separated quantum provers. Both the questions and answers together must use only polylogarithmically many bits in the circuit description length. Honest provers must prepare and execute their shared strategy efficiently from polynomially many copies of a valid quantum witness. Cheating provers may use arbitrary finite-dimensional entanglement and unlimited computation, but cannot communicate while answering. Known succinct computational arguments and entangled proofs without efficient honest preparation do not supply all of these requirements.

[Read in atlas](index.html#TCS-4715) · [Succinct Arguments for QMA from Standard Assumptions via Compiled Nonlocal Games](https://doi.org/10.1109/FOCS61266.2024.00078) · [The status of the quantum PCP conjecture (games version)](https://arxiv.org/abs/2403.13084) · [Succinct Perfect Zero-knowledge for MIP*](https://arxiv.org/abs/2503.04517v2) · [A Modular Approach to Succinct Arguments for QMA](https://arxiv.org/abs/2606.10408v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6447 — Strong quantum IOPs with polynomial communication

Interactive oracle proofs let a verifier inspect only selected parts of much larger prover messages. This question asks for constant-round quantum versions that verify all QMA promise problems with polynomial total communication and only constantly many queries. The strong quantum access model is part of the target, because different ways of querying quantum messages permit different verification strategies. Soundness must cover arbitrary prover behavior, while the verifier remains efficient and has a constant completeness-soundness gap. The project probes how far proof compression and local checking can extend when the evidence itself is quantum.

[Read in atlas](index.html#TCS-6447) · [Quantum Interactive Oracle Proofs](https://arxiv.org/abs/2601.12874) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0031 — Oracle separation of BQP from IP

A classical interactive proof lets a verifier check answers supplied by a prover through a polynomial-length conversation. This problem asks for one oracle relative to which a quantum polynomial-time language has no such proof, even with an unrestricted prover. The quantum algorithm may query the oracle in superposition, whereas the classical verifier queries ordinary strings. The 2026 relativizing containment in the multiple-prover class MIP leaves the single-prover question open in that source. A separation would demonstrate a limit on classical verification of quantum computations through arbitrary oracle interfaces.

[Read in atlas](index.html#TCS-0031) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0034 — Quantum query–space tradeoffs for collisions and distinctness

The question asks for the optimal quantum query cost of collision testing and element distinctness at every allowed memory budget. The oracle returns an output symbol, and the algorithm must decide the answer with bounded worst-case error. All retained storage counts, including classical tables and query registers. Recent lower bounds concern nested collision tasks or search algorithms restricted by label symmetry. The target remains matching upper and lower bounds for unrestricted algorithms solving the two decision problems.

[Read in atlas](index.html#TCS-0034) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [On the Need for (Quantum) Memory with Short Outputs](https://arxiv.org/abs/2602.23763) · [Tight Time-Space Lower Bounds for Collision Finding and Element Distinctness under Label Symmetry](https://arxiv.org/abs/2609.10808)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4238 — Sequential randomness certification against non-signaling adversaries

A single entangled pair of qubits is measured once by Alice and repeatedly by Bob. The question asks whether the certified unpredictability of Bob’s entire outcome string has a universal finite bound against an adversary constrained only by no-signaling and causal order. The honest experiment uses just one qubit per wing, but the adversary is not assumed to be quantum or dimension-limited. Alice may have more possible measurement choices as the sequence grows, and the full observed correlations are assumed known. Unbounded randomness against quantum adversaries and general repeated Bell-test accumulation do not by themselves settle this fixed-resource post-quantum question.

[Read in atlas](index.html#TCS-4238) · [A Single Entangled System Is an Unbounded Source of Nonlocal Correlations and of Certified Random Numbers](https://doi.org/10.4230/LIPIcs.TQC.2017.1) · [Secure and robust randomness with sequential quantum measurements](https://doi.org/10.1038/s41534-024-00879-w) · [Accumulation of Device-Independent Quantum Randomness against Time-Ordered No-Signalling Adversaries](https://arxiv.org/abs/2506.17020v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0862 — Constant-round quantum refereed games versus \(\mathrm{PSPACE}\)

A quantum refereed game has two competing provers trying to make an efficient verifier accept or reject. The provers exchange private quantum messages with the verifier and may keep private memory. The question asks whether every game with a constant number of interaction cycles can be simulated in deterministic polynomial space. Polynomial-space simulations are known for specific patterns in which interaction switches from one prover to the other only once. Polynomially many general rounds capture exponential time, leaving the full constant-round boundary open.

[Read in atlas](index.html#TCS-0862) · [Is QRG with Constant Rounds in PSPACE?](https://tcsopenproblems.com/problem/13) · [Quantum Interactive Proofs with Competing Provers](https://arxiv.org/abs/cs/0412102) · [Parallel Approximation of Min-Max Problems with Applications to Classical and Quantum Zero-Sum Games](https://arxiv.org/abs/1011.2787) · [Toward a General Theory of Quantum Games](https://arxiv.org/abs/quant-ph/0611234)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0027 — Black-box unitary synthesis

The problem asks whether every quantum unitary can be implemented efficiently using an appropriately chosen Boolean oracle. One fixed circuit family must work for all unitaries, with the desired unitary encoded only in the oracle. The implementation must work on arbitrary inputs, including states entangled with an untouched reference. Both total computation and coherent oracle access must remain polynomial in the number of input qubits. Known exponential-time implementations and restricted-query lower bounds leave the general question unresolved.

[Read in atlas](index.html#TCS-0027) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [A One-Query Lower Bound for Unitary Synthesis and Breaking Quantum Cryptography](https://people.eecs.berkeley.edu/~jswright/papers/one-query-unitary-synthesis.pdf) · [Query and Depth Upper Bounds for Quantum Unitaries via Grover Search](https://arxiv.org/abs/2111.07992) · [Explicit Separations for One-Query Unitary Synthesis](https://arxiv.org/abs/2607.26478)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0860 — Complement of quantum approximate counting in \(\mathrm{QMA}(2)\)

The selected task asks whether two unentangled quantum witnesses can certify a small accepting eigenspace. The input is an explicitly described quantum verification circuit and a binary threshold for its spectral count. A low count at acceptance threshold one third must be distinguished from a count at least twice as large at threshold two thirds. The spectral buffer permits intermediate eigenvalues and avoids treating the source’s shortened one-threshold description as the full model. The target is ordinary QMA(2) membership of the complementary promise problem; known quantum-oracle lower bounds concern different models.

[Read in atlas](index.html#TCS-0860) · [TCS Open Problems](https://tcsopenproblems.com/problem/12) · [On the Complexity of Unique Quantum Witnesses and Quantum Approximate Counting](https://doi.org/10.4230/LIPIcs.ITCS.2026.10)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0030 — Oracle separation of BQP from efficient-prover interactive proofs

An efficient quantum computation can have a classical interactive proof whose honest prover is too expensive for the quantum device to execute. This problem asks for an oracle relative to which some quantum polynomial-time language has no classical interactive proof with a quantum polynomial-time honest prover. The verifier and honest prover access the same classical oracle, with quantum queries available only to the quantum computation. Soundness must hold even against an unbounded dishonest prover, so computationally sound cryptographic arguments have a different guarantee. A separation would expose an oracle obstruction to classical verification using only the computational power of an efficient quantum device.

[Read in atlas](index.html#TCS-0030) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1259 — Exact quantum fanout in constant depth with unrestricted circuit size

Quantum fanout coherently flips every target qubit according to one control qubit. The problem asks whether one constant depth bound can implement it exactly using arbitrary one-qubit and generalized Toffoli gates. The circuit may have any finite size and any finite number of clean ancillas. Superposition inputs must be handled correctly and the ancillas must return to zero. An exact construction or an impossibility theorem would determine whether this basic operation lies beyond the expressive power of the shallow gate model.

[Read in atlas](index.html#TCS-1259) · [Random Unitaries in Constant (Quantum) Time](https://doi.org/10.4230/LIPIcs.ITCS.2026.61)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1324 — Quantum games PCP with efficient honest provers and short messages

The question asks whether every quantum-verifiable problem has a short classical game with entangled provers. Both questions and answers must have polylogarithmic length, with a constant completeness–soundness gap. Honest provers must prepare their entanglement and answer in polynomial time given copies of a polynomial-size witness. Soundness must hold even against computationally unrestricted cheating provers. Existing unrestricted entangled proof systems and the source’s streaming Hamiltonian result do not establish this efficient-prover communication target.

[Read in atlas](index.html#TCS-1324) · [Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2026.15) · [The status of the quantum PCP conjecture (games version)](https://arxiv.org/abs/2403.13084v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-2707 — Quantum partition functions from zero-freeness

A quantum partition function aggregates contributions from a Hamiltonian describing the system's interactions. The source asks for a polynomial-time approximation algorithm assuming only the relevant zero-freeness condition. Zero-freeness supports analytic approximation methods, but quantum interaction terms need not commute with one another. Extending the guarantee to this setting would clarify how far analytic information alone can support efficient partition-function computation. The saved passage explicitly identifies noncommutativity as the obstacle, while leaving the precise zero-free region and Hamiltonian access assumptions to the cited paper.

[Read in atlas](index.html#TCS-2707) · [Polynomial-Time Approximation of Zero-Free Partition Functions](https://doi.org/10.4230/LIPIcs.ICALP.2022.108)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3275 — Completeness and soundness amplification in StoqMA

A StoqMA verifier uses classical reversible gates, special initial ancillas and one final measurement in the plus/minus basis. It accepts a suitable nonnegative quantum witness on yes instances and must reject arbitrary witnesses with the prescribed soundness bound on no instances. The question asks whether every inverse-polynomial gap can be amplified to completeness exponentially close to one and soundness exponentially close to one half. Soundness-only repetition is known, but it does not provide this simultaneous improvement. A published theorem makes full error reduction equivalent to StoqMA=MA, and July 2026 work still states the general problem as open.

[Read in atlas](index.html#TCS-3275) · [StoqMA Meets Distribution Testing](https://doi.org/10.4230/LIPIcs.TQC.2021.4) · [StoqMA vs. MA: the power of error reduction](https://doi.org/10.22331/q-2025-09-11-1853) · [The power of unentanglement without destructive interference](https://arxiv.org/abs/2604.27886) · [The Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems](https://arxiv.org/abs/2605.16249)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-4457 — Simulation or postselection universality for algebraic two-qubit interactions

A fixed two-qubit interaction generates circuits by evolving selected ordered pairs for specified times. Every circuit begins in a computational-basis state and ends with computational-basis measurement. The chosen dichotomy asks for efficient classical approximate sampling or full PP decision power with postselection. The variant makes all matrix constants, time encodings, sampling accuracy and conditioning probabilities explicit. Commuting-interaction results and analog Hamiltonian simulations do not by themselves classify this unrestricted circuit model.

[Read in atlas](index.html#TCS-4457) · [Complexity Classification of Two-Qubit Commuting Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2016.28) · [The Space Around BQP](https://dspace.mit.edu/server/api/core/bitstreams/ad343002-e1d8-4966-96ac-7d32b3b215d4/content) · [General Conditions for Universality of Quantum Hamiltonians](https://doi.org/10.1103/PRXQuantum.3.010308)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4734 — Locality-preserving quantum gap amplification

Gap amplification increases the separation between satisfiable and unsatisfiable instances in a verification problem. The cited quantum construction can amplify a Hamiltonian promise gap repeatedly, but its terms act on progressively more qubits. This growing locality obstructs the composition steps used in the classical PCP strategy. The question asks for a quantum analogue that retains the important structural features of Dinur's classical amplification procedure. Such an operation would address a concrete missing ingredient in efforts to make quantum proofs locally checkable with a constant gap.

[Read in atlas](index.html#TCS-4734) · [Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2026.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4927 — Classification of quantum gate sets

A classification of reversible classical gates describes which transformations become possible when a gate set is composed repeatedly. The source uses that completed classical picture to motivate an analogous classification for quantum gates. The quantum question is whether known nonuniversal families, such as stabilizer operations and basis-preserving constructions, account for all relevant possibilities. Additional discrete families or intermediate computational behavior could make the quantum landscape substantially richer. A full classification would organize quantum gate resources by the computations they enable and identify exactly where universality appears.

[Read in atlas](index.html#TCS-4927) · [The Classification of Reversible Bit Operations](https://doi.org/10.4230/LIPIcs.ITCS.2017.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4991 — Reducing shared entanglement in communication protocols

Entanglement-assisted communication protocols may begin with a large shared quantum state that does not count toward their communication cost. This project asks for a quantum analogue of reducing shared randomness in classical communication. The central issue is whether the amount of prior entanglement can be reduced while allowing the protocol itself to change and preserving comparable communication and error. Limitations on replacing the shared state inside a fixed protocol do not settle that more flexible question. A positive result would bound a currently separate resource and make comparisons between entanglement-assisted protocols more informative.

[Read in atlas](index.html#TCS-4991) · [Universality of EPR Pairs in Entanglement-Assisted Communication Complexity, and the Communication Cost of State Conversion](https://doi.org/10.4230/LIPIcs.CCC.2019.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5077 — Exponential repetition of two-player entangled games

Two quantum players must win every copy of a fixed game repeated independently by the referee. They may use arbitrary finite-dimensional entanglement and joint local measurements across the copies. The target is exponential decay whenever the original optimal value is below one. The original paper establishes only polynomial decay, while game transformations give a different amplification guarantee. An August 2026 manuscript claims the full exponential theorem, but this review has not independently verified its proof.

[Read in atlas](index.html#TCS-5077) · [A Parallel Repetition Theorem for All Entangled Games](https://doi.org/10.4230/LIPIcs.ICALP.2016.77) · [Exponential Parallel Repetition for All Two-Player Entangled Games](https://cdn.openai.com/pdf/ten-proofs-oai.pdf)
Existing status: `uncertain` · Summary written: 2026-09-12

### TCS-5202 — Quantum security of general seeded extractors

Randomness extractors turn weakly random inputs into nearly uniform bits, often for use as cryptographic keys. Their guarantees must account for information an adversary already holds about the input. The selected passage asks whether general seeded extractors with multiple output bits remain secure against quantum side information with suitable parameter losses. The source contrasts this with more established one-bit guarantees and with specific multibit constructions already known to be quantum-proof. Resolving the general question would determine how freely classical extractor designs can be reused when an adversary stores quantum information.

[Read in atlas](index.html#TCS-5202) · [Quantum-Proof Multi-Source Randomness Extractors in the Markov Model](https://doi.org/10.4230/LIPIcs.TQC.2016.2)
Existing status: `uncertain` · Summary written: 2026-09-11
