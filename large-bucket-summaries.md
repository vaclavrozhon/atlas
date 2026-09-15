# Working summaries — large categories

407 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computational complexity (71)

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

An unsatisfiable formula has no assignment that makes every clause true. The question asks whether one fixed efficient verifier can always check a polynomial-length certificate of that impossibility. The certificate format is unrestricted as long as it is sound for every formula. This is equivalent to asking whether NP equals coNP. The project concerns the possibility of universally concise explanations for the failure of all candidate solutions, rather than lower bounds for any one particular set of proof rules.

[Read in atlas](index.html#TCS-0002) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Circuits, Communication, and Proofs](https://www.icts.res.in/program/ccp)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0015 — Superlinear Boolean circuit lower bounds

A multi-output Boolean function can share intermediate computations among all its output bits. The question asks for one polynomial-time computable family whose unrestricted Boolean circuits exceed every fixed linear size bound. The saved formulation uses as many output bits as input bits. An arbitrary hard truth table does not satisfy the explicitness requirement. The project seeks a modest but fundamental lower bound demonstrating that some efficiently specified transformations intrinsically need more than a constant amount of circuit work per input bit.

[Read in atlas](index.html#TCS-0015) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [\(3.1n -  o(n)\) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://eccc.weizmann.ac.il/report/2025/033/) · [Convergent Gate Elimination and Constructive Circuit Lower Bounds](https://arxiv.org/abs/2602.17942) · [A Note on Natural-Proofs for Super-Linear Lower Bounds for Linear Functions](https://eccc.weizmann.ac.il/report/2026/008/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0016 — Exponential circuit lower bounds for 3-SAT

The saved 3-SAT family uses a fixed encoding of which clauses on n variables are present. The conjecture asks for circuit size exponential in n, even when every input length gets its own arbitrary circuit. Its scale is stronger than merely excluding polynomial-size circuits. The variable count differs from the total number of encoded clause bits, so the parameter must remain explicit. The project aims to prove that searching for a satisfying assignment retains essentially exponential difficulty even under nonuniform computation.

[Read in atlas](index.html#TCS-0016) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Which Problems Have Strongly Exponential Complexity?](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturiZane_2001_jcss.pdf) · [\(3.1n -  o(n)\) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7158 — PH versus PSPACE

Does every polynomial-space decision problem lie in the polynomial hierarchy? PH allows a fixed number of alternating quantifier blocks for each language. PSPACE also describes polynomial-time alternation with no fixed bound on the number of alternations. Equality would put TQBF in one finite level and hence collapse PH to that level. Completeness and oracle results illuminate the distinction without settling the ordinary class equality.

[Read in atlas](index.html#TCS-7158) · [Computational Complexity: A Modern Approach (Internet draft)](https://theory.cs.princeton.edu/complexity/book.pdf) · [Completeness in the Polynomial Hierarchy and PSPACE for many natural problems derived from NP](https://arxiv.org/abs/2602.12350) · [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](https://arxiv.org/abs/2602.02294)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7161 — NEXP versus nonuniform \(\mathrm{TC}^{0}\)

Does some NEXP language escape all polynomial-size constant-depth majority circuits? Majority gates make this circuit class substantially more powerful than constant-depth \(\mathrm{AND}/\mathrm{OR}\) circuits. Williams established the corresponding separation for ACC circuits with fixed-modulus gates. Recent threshold-circuit bounds still restrict depth or polynomial size and use different hard-language classes. The target requires one ordinary NEXP language outside the entire nonuniform class \(\mathrm{TC}^{0}\).

[Read in atlas](index.html#TCS-7161) · [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/) · [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and \(\mathrm{THR} \circ  \mathrm{THR}\)](https://eccc.weizmann.ac.il/report/2026/167/) · [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6533 — NL versus UL

An ordinary nondeterministic reachability algorithm can have many accepting paths of computation. UL requires at most one accepting computation for each input while retaining logarithmic workspace. The question asks whether this unambiguity restriction changes the class NL. The machine may still have many rejecting branches, so this is weaker than demanding determinism. The project seeks to isolate a unique successful witness efficiently, clarifying whether ambiguity itself is a source of computational power in small-space graph problems.

[Read in atlas](index.html#TCS-6533) · [Making Nondeterminism Unambiguous](https://people.cs.rutgers.edu/~allender/papers/nlul.pdf) · [Derandomizing Isolation in Space-Bounded Settings](https://pages.cs.wisc.edu/~dieter/Papers/r-ul-sicomp.pdf) · [When Connectivity Is Hard, Random Walks Are Easy With Non-Determinism](https://eccc.weizmann.ac.il/report/2025/077/download) · [Using Hardness vs Randomness to Design Low-Space Algorithms](https://eccc.weizmann.ac.il/report/2026/045/) · [Derandomizing Isolation In Catalytic Logspace](https://arxiv.org/abs/2512.09374) · [Deterministic, Oblivious Isolation for Space-Bounded Computation Requires Large Weights](https://eccc.weizmann.ac.il/report/2026/124/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0004 — L versus NL

Directed reachability asks whether a path leads from a specified source to a specified target. Nondeterminism solves it with logarithmic memory by guessing successive vertices. The question asks for a deterministic algorithm using the same tiny workspace on an explicitly stored graph. Repeated input scans are allowed, but a full visited array or search frontier is not. The project would settle L versus NL by showing whether all the essential information in directed exploration can be organized without guessing or substantial stored history.

[Read in atlas](index.html#TCS-0004) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Relationships between nondeterministic and deterministic tape complexities](https://doi.org/10.1016/S0022-0000(70)80006-X) · [Nondeterministic Space is Closed under Complementation](https://doi.org/10.1137/0217058) · [Undirected Connectivity in Log-Space](https://omereingold.wordpress.com/wp-content/uploads/2014/10/sl.pdf) · [When Connectivity Is Hard, Random Walks Are Easy with Non-determinism](https://doi.org/10.1145/3717823.3718303) · [Reachability in graphs having linear 2-arboricity two is NL-hard](https://doi.org/10.1016/j.ipl.2025.106611)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4988 — Existence of TFNP-complete problems

TFNP contains search problems with polynomially bounded, efficiently verifiable answers guaranteed to exist for every binary input. The question asks whether one problem in this class is complete for all the others under deterministic polynomial-time many-one search reductions. Each reduction makes one transformed instance and must decode every valid returned answer correctly. The complete relation is fixed universally, while the reduction and its polynomial bounds may vary with the source problem. Known subclass completeness and oracle results clarify the structure without settling this general existence question.

[Read in atlas](index.html#TCS-4988) · [An Oracle with no UP-Complete Sets, but \(\mathrm{NP}=\mathrm{PSPACE}\)](https://doi.org/10.4230/LIPIcs.MFCS.2024.50) · [Incompleteness in the finite domain](https://users.math.cas.cz/~pudlak/inco.pdf) · [Hierarchies within TFNP: building blocks and collapses](https://eccc.weizmann.ac.il/report/2025/123/revision/1/download/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7363 — \(\exists\mathbb{R}\) versus \(\mathrm{NP}\)

Existential real formulas ask whether polynomial constraints have a real solution. The input is a finite binary description of the constraints. The class contains NP and is contained in PSPACE. The question asks whether it is exactly NP. An oracle separation or a rational-coordinate obstruction alone does not answer that class comparison.

[Read in atlas](index.html#TCS-7363) · [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006) · [Some structural complexity results for \(\exists\mathbb R\)](https://arxiv.org/abs/2502.00680)
Existing status: `source_open` · Summary written: 2026-09-13

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

### TCS-6714 — Nonuniform \(\mathrm{NC}^{1}\) perfect matching

The question asks whether perfect-matching existence in every undirected graph has nonuniform polynomial-size circuits of logarithmic depth. The circuits use binary AND and OR with negation and return only an exact decision bit. This is equivalent to polynomial-size formulas and, under explicit graph transformations, to the matching-threshold question in the original source. Monotone lower bounds and broader polylogarithmic-depth algorithms do not decide the unrestricted NC-one target. The July 2026 bipartite NC result also has a different graph scope and depth guarantee.

[Read in atlas](index.html#TCS-6714) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html) · [The Matching Problem in General Graphs Is in Quasi-NC](https://doi.org/10.1109/FOCS.2017.70) · [Bipartite Matching is in NC](https://eccc.weizmann.ac.il/report/2026/100/revision/2/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7243 — Linear-size circuits for stable ternary compaction

Stable ternary compaction moves every 2 to the end while preserving the order of all 0s and 1s. The question is whether every input length admits a Boolean circuit of size proportional to that length. The circuits use a fixed bounded-fan-in basis and may have arbitrary depth and fan-out. Stability retains the original binary sequence, so ordinary ternary sorting is insufficient. The target supplies a concrete function for studying the limits of linear-size circuits.

[Read in atlas](index.html#TCS-7243) · [Linear-size circuits for stable \(0,1 < 2\) sorting?](https://www.openproblemgarden.org/op/linear_size_circuits_for_stable_0_1_2_sorting) · [Sorting Short Keys in Circuits of Size \(o(n \log  n)\)](https://arxiv.org/abs/2010.09884)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0017 — KRW formula-size conjecture with constant loss

The selected KRW variant asks whether minimum formula size under block composition is always within a constant factor of the product of the two minimum sizes. Both functions can be arbitrary nonconstant Boolean functions, and the inner one is applied to disjoint input blocks. Formulas use binary AND and OR with negation, count variable occurrences, and cannot share intermediate computations. The constant must work for every function and dimension, so dimension-dependent losses do not suffice. The original depth conjecture and recent results for strengthened communication tasks are related but distinct statements.

[Read in atlas](index.html#TCS-0017) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [Super-logarithmic Depth Lower Bounds via the Direct Sum in Communication Complexity](https://doi.org/10.1007/BF01206317) · [Shrinkage under Random Projections, and Cubic Formula Lower Bounds for \(AC^0\)](https://doi.org/10.4086/toc.2023.v019a007) · [Toward Better Depth Lower Bounds: Strong Composition of XOR and a Random Function](https://doi.org/10.4230/LIPIcs.STACS.2025.26)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6285 — Closure of UL under complement

UL contains languages decided with logarithmic work space and at most one accepting computation path per input. The question asks whether the complement of every such language also has an unambiguous logarithmic-space decider. The original and complement machines are uniform, exact and have no oracle or nonuniform advice. Ordinary nondeterministic logspace is closed under complement, but its complementing procedures need not preserve unambiguity. A resolution would clarify both the structure of small-space complexity classes and the use of unambiguous subroutines in graph algorithms.

[Read in atlas](index.html#TCS-6285) · [Depth-First Search in Directed Planar Graphs, Revisited](https://doi.org/10.4230/LIPIcs.MFCS.2021.7) · [Nondeterministic Space is Closed under Complementation](https://doi.org/10.1137/0217058) · [Parameterizing the Complexity of Finding Long Paths in DAGs](https://doi.org/10.4230/LIPIcs.MFCS.2026.73)
Existing status: `source_open` · Summary written: 2026-09-14

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

### TCS-6139 — Subexponential derandomization with two-way random-tape access

This question concerns randomized logspace algorithms that can reread a fixed polynomial-length random tape in either direction. It asks whether every language they decide has a uniform exact deterministic algorithm whose worst-case runtime has an exponent sublinear in input length. The deterministic algorithm has no separate space restriction and receives no advice. The source’s simulation for restricted passes with advice and later conditional promise-search results do not provide this algorithm. The formulation explicitly separates persistent randomness from the one-way coin access used in ordinary BPL.

[Read in atlas](index.html#TCS-6139) · [A Note on the Advice Complexity of Multipass Randomized Logspace](https://doi.org/10.4230/LIPIcs.MFCS.2016.31) · [Leakage-Resilient Hardness Equivalence to Logspace Derandomization](https://doi.org/10.4230/LIPIcs.MFCS.2024.83)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6455 — Doubly efficient \(\mathrm{IP} = \mathrm{PSPACE}\) for the full time range

An interactive proof lets a verifier check a claim through conversation with a prover. The question asks whether polynomial-space computations taking time T can be verified in polynomial input time using an honest prover running in polynomial T time. The requirement extends across the full time range, beyond quasipolynomial computations. This would make proof generation efficient relative to the computation being certified, strengthening the resource content of \(\mathrm{IP}=\mathrm{PSPACE}\). The saved review stresses that soundness must still withstand arbitrarily powerful cheating provers, despite the efficiency requirement imposed on the honest one.

[Read in atlas](index.html#TCS-6455) · [Towards a Doubly Efficient \(\mathrm{IP}=\mathrm{PSPACE}\)](https://eccc.weizmann.ac.il/report/2026/102/)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-0301 — Excluding one-sided randomized quasilinear-time log-space SAT

Randomized SAT algorithms may miss a satisfying assignment while never incorrectly declaring an unsatisfiable formula satisfiable. The question asks to rule out algorithms with that one-sided error using both quasilinear time and logarithmic space. The source emphasizes that reversing the permitted error direction changes what lower-bound methods can prove. Deterministic time-space tradeoffs do not automatically handle random choices. The project seeks a lower bound matching the error behavior of incomplete randomized search procedures under extremely small resource budgets.

[Read in atlas](index.html#TCS-0301) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0303 — Stronger log-space time lower bounds for SAT

Time-space lower bounds show that some combinations of fast running time and tiny memory cannot solve SAT. The source asks to strengthen the known limits for logarithmic-space algorithms. This differs from proving a general SAT time lower bound because the memory restriction supplies additional structure. Simulation and alternation-trading arguments are central tools in the cited discussion. The project seeks a sharper quantitative obstruction to deciding satisfiability while retaining only a few indices, even if the input can be revisited freely.

[Read in atlas](index.html#TCS-0303) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1602 — Deterministic query complexity of tournament kings

A king in a tournament reaches every other vertex along a directed path of at most two edges. A deterministic algorithm learns the orientation of one chosen edge per query and must output a king for every tournament. The target is its optimal worst-case query count up to constant factors as the number of vertices grows. The checked deterministic bounds remain \(\Omega(n^{4/3})\) and \(O(n^{3/2})\), whereas randomization permits linear expected query cost. Closing the deterministic gap would quantify how much pairwise information this total search task inherently requires.

[Read in atlas](index.html#TCS-1602) · [Hardness of Finding Kings and Strong Kings](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.36) · [Searching for Sorted Sequences of Kings in Tournaments](https://cis.temple.edu/~wu/research/publications/Publication_files/41005.pdf) · [Randomized and Quantum Query Complexities of Finding a King in a Tournament](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.30) · [From Donkeys to Kings in Tournaments](https://doi.org/10.4230/LIPIcs.ESA.2024.3) · [When You Come at the King You Best Not Miss](https://doi.org/10.4230/LIPIcs.FSTTCS.2022.25)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0310 — Polynomial-time weighted falsifiability of unambiguous DNFs

An unambiguous DNF has mutually disjoint satisfying terms, making some counting tasks straightforward. The question instead asks for a falsifying assignment with sufficiently large total variable weight. Weights and the threshold are binary encoded. Knowing how many assignments falsify the formula does not reveal whether one reaches the desired score. The project tests whether the strong disjointness promise still helps when every term must be defeated simultaneously while optimizing an additive objective over the complement.

[Read in atlas](index.html#TCS-0310) · [Is this problem on unambiguous DNFs hard?](https://cstheory.stackexchange.com/questions/53733/is-this-problem-on-unambiguous-dnfs-hard) · [Representation, Provenance, and Explanations in Database Theory and Logic (Dagstuhl Seminar 24032)](https://doi.org/10.4230/DagRep.14.1.49) · [List of open questions: Weighted falsifiability for unambiguous DNFs](https://a3nm.net/work/research/questions/#weighted-falsifiability-for-unambiguous-dnfs)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-0297 — A counting characterization of P with NP access

A counting function in #P returns the number of accepting witnesses for an efficiently checkable relation. The question asks whether some such function gives a polynomial-time oracle machine exactly the power of polynomial time with an NP oracle. Ordinary complete counting functions provide substantially more apparent information than mere existence tests. The target therefore requires a specially controlled counting task. The project seeks a numerical oracle capturing NP access without unintentionally granting the full power of general witness counting.

[Read in atlas](index.html#TCS-0297) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0298 — SAT multi-prover proofs using efficient SAT-oracle provers

Multi-prover interactive proofs let a verifier question several provers that cannot coordinate their answers during the protocol. The source asks for such a proof system for SAT whose honest provers run in randomized polynomial time with SAT-oracle access. Unrestricted provers do not meet this efficiency requirement. The question is tied to whether SAT programs can be checked through suitable oracle interactions. The project seeks a verification protocol whose participants need no computational power beyond the problem they are supposed to certify.

[Read in atlas](index.html#TCS-0298) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2215 — A real analogue of Toda’s theorem

Toda's theorem in discrete complexity relates alternating quantifiers to counting power. This source asks for an analogous relationship among real-algebraic complexity classes. The proposed target is to contain fixed levels of alternating real quantification in an existential real theory enhanced with summation operators. The exact operator language matters because unrestricted real exponentiation would change the setting substantially. A positive result would organize several real-feasibility hierarchies under one strengthened existential framework and illuminate the role of counting-like operations over real computation.

[Read in atlas](index.html#TCS-2215) · [The Existential Theory of the Reals with Summation Operators](https://doi.org/10.4230/LIPIcs.ISAAC.2024.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2333 — Downward self-reducibility of PLS-complete problems

A search problem is downward self-reducible if solutions can be computed efficiently using an oracle only on strictly smaller instances. PLS contains total search problems whose solutions can be found through a finite process of improving a locally evaluated objective. The source proves downward self-reducibility for familiar PLS-complete problems and places downward self-reducible total search in PLS. It asks whether every PLS-complete problem enjoys this recursive property. The issue is that general completeness reductions need not preserve input length, so self-reducibility cannot simply be transferred through an arbitrary reduction.

[Read in atlas](index.html#TCS-2333) · [Downward Self-Reducibility in TFNP](https://doi.org/10.4230/LIPIcs.ITCS.2023.67)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2425 — Closure of SZK under truth-table reductions

Statistical zero knowledge captures problems that can be verified interactively while revealing essentially no additional information even to a powerful observer. This project asks whether the class SZK is closed under polynomial-time truth-table reductions. Such a reduction prepares its oracle questions without depending on their answers and then combines the answers using polynomial-time computation. The source discusses closure under more restricted ways of combining answers, which do not automatically give this general closure property. A resolution would clarify whether nonadaptive composition preserves statistical zero knowledge across the full range of efficient postprocessing.

[Read in atlas](index.html#TCS-2425) · [Kolmogorov Complexity Characterizes Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.ITCS.2023.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2532 — Circuit lower bounds from indistinguishability obfuscation

Indistinguishability obfuscation hides which of two equivalent circuit implementations was supplied to an observer. The cited work shows that obfuscation secure against nonuniform polynomial-size circuits implies nontrivial circuit lower bounds. This project asks whether an analogous implication follows when security is assumed only against uniform efficient algorithms. Nonuniform attackers can use input-length-dependent advice, so the existing security hypothesis is stronger than the proposed replacement. Establishing lower bounds from uniform security would connect a more algorithmic cryptographic assumption with structural limitations on small circuits.

[Read in atlas](index.html#TCS-2532) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2681 — UEOPL versus EOPL

EOPL describes total search along succinct paths with potentials. UEOPL admits additional answers witnessing failures of uniqueness. The question asks whether both ordinary circuit-defined classes nevertheless have the same power. A published theorem separates them in the black-box model, which does not decide this equality. Resolving it would clarify the computational role of uniqueness in total search.

[Read in atlas](index.html#TCS-2681) · [Further Collapses in TFNP](https://doi.org/10.4230/LIPIcs.CCC.2022.33) · [Unique End of Potential Line](https://doi.org/10.1016/j.jcss.2020.05.007) · [Separations in Proof Complexity and TFNP](https://doi.org/10.1145/3663758)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3509 — Tarski in CLS or EOPL

Tarski's fixed-point theorem guarantees a fixed point for an order-preserving map on a suitable lattice. The source asks whether the associated computational search problem lies in CLS or EOPL. These classes organize total search problems through continuous local improvement or structured potential-guided paths. A containment would connect monotone fixed points with algorithmic approaches used for equilibrium and local optimization. The saved excerpt does not state the finite encoding or violation outputs, so the computational Tarski problem must be defined separately from the unrestricted mathematical existence theorem.

[Read in atlas](index.html#TCS-3509) · [Tarski’s Theorem, Supermodular Games, and the Complexity of Equilibria](https://doi.org/10.4230/LIPIcs.ITCS.2020.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3862 — Complete problems for search zero knowledge

Zero-knowledge protocols are usually framed around deciding whether a statement is true. Search zero knowledge instead concerns interactions that produce a valid solution while controlling what additional information is revealed. The selected problem asks whether these search classes have complete problems in either the computational or statistical security setting. A complete problem would serve as a universal representative to which other search-zero-knowledge tasks can be reduced under suitable definitions. Finding one would organize the new model and help transfer general techniques from the better-developed theory of decision zero knowledge.

[Read in atlas](index.html#TCS-3862) · [Brief Announcement: Zero-Knowledge Protocols for Search Problems](https://doi.org/10.4230/LIPIcs.ICALP.2018.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4468 — Subcube partition complexity versus query complexity

A subcube partition divides all Boolean inputs into monochromatic pieces, each specified by fixing some coordinates. Unlike a decision tree, the pieces need not arise from one sequential hierarchy of queries. The source separates this partition model from randomized decision trees and asks for the strongest possible gap between their complexities. Even the comparison with deterministic query complexity is included in the question. Determining the extremal separation would quantify how much harder it is to discover an input's certificate adaptively than merely to exhibit a globally consistent collection of certificates.

[Read in atlas](index.html#TCS-4468) · [Separating Decision Tree Complexity from Subcube Partition Complexity](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.915)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4786 — Complexity of Minimum Circuit Size

The minimum circuit size problem asks whether a truth table can be implemented by a Boolean circuit below a given size threshold. A small circuit supplies an efficiently checkable witness, placing the problem in NP when input length is measured by the full truth table. The selected passage highlights the unresolved classification between efficient randomized algorithms and NP-hardness. It also notes that an efficient algorithm would enable average-case inversion of candidate one-way functions through known reductions. Understanding this problem would connect circuit minimization, obfuscation, and the computational assumptions that make cryptography possible.

[Read in atlas](index.html#TCS-4786) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6006 — Complexity of ARRIVAL

ARRIVAL describes a deterministic walk in a directed graph whose vertices alternate between two outgoing choices on successive visits. The decision task asks which designated destination the walk eventually reaches. The source notes efficiently verifiable certificates for either answer, placing the problem in NP intersect coNP. It improves exponential algorithms to a subexponential bound and gives a polynomial-time algorithm for almost acyclic graphs. The remaining project is to decide whether all instances can be solved in polynomial time without explicitly following a walk that may be exponentially long.

[Read in atlas](index.html#TCS-6006) · [A Subexponential Algorithm for ARRIVAL](https://doi.org/10.4230/LIPIcs.ICALP.2021.69)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6715 — Monotone circuits versus monotone span programs

A monotone span program accepts an input when vectors enabled by its one-bits span a designated target vector over a field. A monotone Boolean circuit instead combines input bits using AND and OR gates. The question asks for functions with polynomial-size monotone circuits that require superpolynomial-size monotone span programs. The source discusses a separation in the opposite direction, so this asks whether the two models can be incomparable in efficiency. Such an example would expose a limitation of linear-algebraic representations even for functions having short purely monotone logical computations.

[Read in atlas](index.html#TCS-6715) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6716 — General versus monotone span programs

Ordinary span programs may enable vectors using either positive or negative input literals. Monotone span programs use only positive literals, even when the function itself is monotone. The question asks for a monotone function with a polynomial-size ordinary span program but no polynomial-size monotone span program. The analogous distinction can be dramatic for Boolean circuits, but the source leaves it unsettled for span programs. A separation would show that negative tests can provide essential efficiency in linear-algebraic computation despite the monotonicity of the final answer.

[Read in atlas](index.html#TCS-6716) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6832 — Separations among P, RP and NP

P consists of problems with deterministic polynomial-time algorithms, while RP permits randomized algorithms that can miss yes-instances but never falsely accept no-instances. Every RP algorithm can be viewed as an NP verification procedure by treating its random choices as a certificate. This gives the chain P contained in RP contained in NP. The question asks which of these inclusions are strict. The alternatives distinguish whether randomness adds power beyond deterministic computation and whether one-sided randomized search can capture the full strength of efficiently verifiable existence.

[Read in atlas](index.html#TCS-6832) · [Understanding Machine Learning: From Theory to Algorithms](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6934 — Unconditional exclusion of linear-time CNF satisfiability

CNF satisfiability asks whether an assignment makes every listed clause true. The input measure counts every written literal, identifier bit and delimiter. The selected question asks whether a deterministic multitape Turing machine can always decide it in linear time. No separate workspace restriction or conjectural hardness assumption is allowed. This precise modest milestone is distinguished from exponential lower bounds and from lower bounds for other computation models.

[Read in atlas](index.html#TCS-6934) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/) · [Time-space lower bounds for satisfiability](https://doi.org/10.1145/1101821.1101822) · [Simulating Time with Square-Root Space](https://doi.org/10.1145/3798104)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6977 — Super-near-linear SAT time lower bounds

SAT asks whether a Boolean formula has a satisfying assignment. The selected question seeks an unconditional lower bound excluding algorithms whose running time stays near the input length. This is a weaker objective than excluding every polynomial-time algorithm, but it must still account for all algorithms in the chosen model. Restrictions on working space can support different lower bounds and should not be silently added to the question. Progress would establish a concrete limit on efficient satisfiability algorithms without needing to settle the full P versus NP problem.

[Read in atlas](index.html#TCS-6977) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6979 — Independence of P versus NP from ZFC

P versus NP asks whether efficiently verifiable decisions can always be made efficiently. This card asks specifically whether ZFC proves neither the usual arithmetic statement P = NP nor its negation. It defines that statement through polynomial-time deterministic satisfiability and allows all finite ZFC proofs. Results for restricted theories and oracle machines do not establish the asserted independence from full ZFC. The question has a definite yes/no target once the axioms are fixed, and a positive answer would also imply their consistency.

[Read in atlas](index.html#TCS-6979) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf) · [Is P Versus NP Formally Independent?](https://www.scottaaronson.com/papers/indep.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

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

Reachability diameter measures the largest finite shortest-path distance in a directed graph. Unreachable ordered pairs are omitted so that disconnected directions do not make the answer automatically infinite. The question asks for a constant-factor estimate in near-linear time on every unweighted directed graph. Simple searches from arbitrary pivots can miss a long directed route. A successful method would summarize the extent of reachable routes without computing distances from every vertex or imposing strong connectivity.

[Read in atlas](index.html#TCS-1141) · [Revisiting Diameter in Directed Graphs](https://doi.org/10.4230/LIPIcs.ESA.2026.59)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7350 — Near-linear output-sensitive Subset Sum

The input is a multiset of positive integers and a threshold. The task is to enumerate the distinct attainable subset sums at most that threshold. The question asks for near-linear time in the explicit input and the actual number of output values. Known pseudopolynomial algorithms and output-sensitive improvements do not reach this endpoint. The target avoids spending linear time on a large numerical universe containing few attainable sums.

[Read in atlas](index.html#TCS-7350) · [Top-k-Convolution and the Quest for Near-Linear Output-Sensitive Subset Sum](https://arxiv.org/abs/2107.13206) · [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390)
Existing status: `source_open` · Summary written: 2026-09-13

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

A higher-order recursion scheme is a finite system of typed recursive rules that unfolds into a possibly infinite labeled tree. The project asks whether two deterministic schemes always admit an effective test for equality of their complete value trees. Equality includes divergence leaves and compares labels at every finite address, irrespective of internal evaluation steps. Functions passed as arguments make the generators much richer than finite-state descriptions. Solving this comparison problem would extend our ability to verify higher-order recursive behavior beyond properties of one generated tree at a time.

[Read in atlas](index.html#TCS-6582) · [Collapsible Pushdown Automata and Recursion Schemes](https://www.cs.rhul.ac.uk/home/uxac009/files/papers/tocl17.pdf) · [Higher-Order Recursion Schemes and Collapsible Pushdown Automata: Logical Properties](https://arxiv.org/abs/2010.06366v2) · [Reducing Higher-order Recursion Scheme Equivalence to Coinductive Higher-order Constrained Horn Clauses](https://arxiv.org/abs/2109.04632) · [Polyregular equivalence is undecidable in higher-order types](https://arxiv.org/abs/2604.11935) · [On Higher-Order Probabilistic Verification via the Weighted Relational Model of Linear Logic](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.34)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6564 — First-order definability of regular tree languages

Can one decide whether a regular language of finite ordered trees has a first-order definition? The automaton is finite input, while the sought sentence must describe its language on trees of every finite size. The logic can inspect labels, descendants and sibling order but cannot quantify over sets of nodes. Known fragment tests and separate necessary or sufficient algebraic conditions leave the full decision problem unresolved. Recent infinite-tree and restricted temporal-logic characterizations do not establish this finite ordered-tree test.

[Read in atlas](index.html#TCS-6564) · [Tree Languages Defined in First-Order Logic with One Quantifier Alternation](https://lmcs.episciences.org/699) · [Some Remarks on First-Order Definable Tree Languages](https://arxiv.org/abs/2407.01169) · [An Automaton-based Characterisation of First-Order Logic over Infinite Trees](https://arxiv.org/abs/2509.14090) · [Deciding the Common Fragment of CTL with past and LTL](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.29)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0164 — Decidability of equivalence for unambiguous context-free grammars

An unambiguous context-free grammar has at most one parse tree for every generated word. Two such grammars are given with the promise of unambiguity. The task is to decide whether they generate exactly the same finite words. No deterministic-pushdown or regular-language restriction is imposed. The question asks for a terminating decision procedure without any prescribed complexity bound.

[Read in atlas](index.html#TCS-0164) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#equivalence-of-unambiguous-context-free-grammars)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3863 — Containment of finitely ambiguous probabilistic automata

Two probabilistic automata assign acceptance probabilities to every finite input word. Each machine has a fixed finite bound on its positive accepting runs, but either bound can be greater than one. The question asks for an unconditional terminating test of whether the first probability never exceeds the second. Existing results with an unambiguous side do not settle the general case, and allowing linearly growing ambiguity already gives undecidability. The benchmark requires a Lean-checked decidability or undecidability proof for exact comparison without a gap promise.

[Read in atlas](index.html#TCS-3863) · [When is Containment Decidable for Probabilistic Automata?](https://doi.org/10.4230/LIPIcs.ICALP.2018.121) · [When are emptiness and containment decidable for probabilistic automata?](https://doi.org/10.1016/j.jcss.2021.01.006)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0167 — Primitive words and context-freeness

A primitive word is nonempty and is not a power of any shorter nonempty word. The language contains all such words over a fixed finite alphabet with at least two symbols. The conjecture says that no context-free grammar generates exactly this language. Grammars may be ambiguous, so unique-parse limitations would not settle the question. A 2026 paper still states this grammar-expressibility question as open.

[Read in atlas](index.html#TCS-0167) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#context-freeness-of-primitive-words) · [On the Complexity of Language Membership for Probabilistic Words](https://doi.org/10.4230/LIPIcs.STACS.2026.5)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0154 — Separating words problem

The problem measures the smallest deterministic automaton that distinguishes two binary words of equal length. A different automaton may be chosen for each pair and its behavior on other words is unrestricted. The target is the worst-case number of states as a function of the common word length. The original question proposes a logarithmic upper bound, while recent general bounds have a one-third power with logarithmic factors. The benchmark asks for matching constant-factor asymptotics across all pairs, not a random-input guarantee.

[Read in atlas](index.html#TCS-0154) · [Automata Exchange](https://automata.exchange/19.04-separating-words-problem/) · [Separating Words with Automata in the Half-adversarial Case](https://arxiv.org/abs/2608.28385) · [An Elementary Proof of the \(\widetilde O(n^{1/3})\) Bound for Separating Words](https://arxiv.org/abs/2609.08191)
Existing status: `source_open` · Summary written: 2026-09-13

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

### TCS-5651 — Recognizing good-for-games and good-for-MDP automata

Limited nondeterminism lets automata retain some branching while remaining suitable for composition with games or probabilistic systems. This project asks the exact complexity of recognizing good-for-games parity automata and good-for-MDPs Büchi automata. The former resolve choices from input history, while the latter preserve optimal satisfaction probabilities when combined with a Markov decision process. These are different semantic promises, so an algorithm for one does not establish the other. Sharper classifications would show the cost of checking that a compact specification supports the intended verification workflow.

[Read in atlas](index.html#TCS-5651) · [Word Automata with Limited Nondeterminism (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2026.3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5732 — Regular separability of VASS reachability languages

A reachability language of a vector addition system with states consists of finite words labeling accepting counter runs. In the source's convention, acceptance requires a final control state with all counters zero. Regular separability asks whether a finite automaton can recognize a language containing one such language and disjoint from another. The cited paper identifies decidability for general finite-word VASS languages as a separate question from its positive result for Büchi VASS over infinite words. Solving it would determine when finite-state separators can effectively distinguish behaviors of two unbounded counter systems under exact reachability acceptance.

[Read in atlas](index.html#TCS-5732) · [Regular Separability in Büchi VASS](https://doi.org/10.4230/LIPIcs.STACS.2023.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5738 — Recognizable separability of automatic relations

Automatic relations on words are recognized by finite automata reading their components synchronously. The project asks whether two such relations can be separated by a recognizable relation, a finite union of products of regular languages. The conjecture predicts that deciding existence of any such separator is impossible. The source relates this task to regular colorability and distinguishes it from versions with a fixed color bound. Settling the unrestricted question would identify a limit of simplifying synchronized relational specifications into independently recognizable components.

[Read in atlas](index.html#TCS-5738) · [Separating Automatic Relations](https://doi.org/10.4230/LIPIcs.MFCS.2023.17)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5863 — Decidability of stochastic resolvability for \(\omega\)-automata

A stochastic resolver chooses an automaton's transitions randomly while reading an infinite word prefix by prefix. Stochastic resolvability requires almost-sure acceptance of every word in the original language when the word is fixed independently of those choices. This project asks whether that property is decidable for Büchi and coBüchi automata. Checking one proposed resolver is already problematic in the source, but that does not decide whether some suitable resolver exists. An existence test would identify which finite nondeterministic specifications admit reliable randomized online execution.

[Read in atlas](index.html#TCS-5863) · [Resolving Nondeterminism with Randomness](https://doi.org/10.4230/LIPIcs.MFCS.2025.57)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5904 — Equivalence of discounted-sum automata

Discounted-sum automata assign values to infinite words by giving earlier transition weights more influence than later ones. The project asks whether equivalence of these quantitative functions is decidable for the source's automaton model. Agreement must hold on every word and in the exact numerical value, not just at a chosen threshold. The source distinguishes this from deciding whether one automaton computes a constant function, which it handles separately. A general comparison procedure would provide a fundamental correctness test for quantitative specifications with geometrically discounted future contributions.

[Read in atlas](index.html#TCS-5904) · [Safety and Liveness of Quantitative Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2023.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5959 — Complexity of the Game of Life limit set

Conway's Game of Life has a limit set consisting of configurations with arbitrarily long predecessor histories. The project asks the complexity of recognizing finite patterns that occur somewhere in this set. The source proves polynomial-space hardness and asks whether the full co-recursively-enumerable completeness bound is attained. Standard universality constructions do not settle this because surrounding cells must not be assumed harmless when testing arbitrary patterns. A matching hardness result would show that indefinitely possible past histories encode substantially more difficulty than ordinary finite-time simulation.

[Read in atlas](index.html#TCS-5959) · [What Can Oracles Teach Us About the Ultimate Fate of Life?](https://doi.org/10.4230/LIPIcs.ICALP.2022.131)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6064 — Characterizing cellular-automaton limit sets

A cellular automaton's limit set contains every configuration that can appear after arbitrarily many update steps. This project asks which subshifts can arise as such limit sets. The characterization concerns all possible initial configurations, including exceptional behaviors of negligible probability. The source's positive result instead addresses measure-based limit sets under random initial conditions and therefore answers a different question. An ordinary limit-set characterization would describe the full range of persistent global behavior that can emerge from a finite local update rule.

[Read in atlas](index.html#TCS-6064) · [Construction of mu-Limit Sets of Two-dimensional Cellular Automata](https://doi.org/10.4230/LIPIcs.STACS.2015.262)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6158 — Unique invariant measures versus cellular-automaton ergodicity

A deterministic cellular automaton induces a transformation on probability distributions over its configurations. Unique ergodicity means that exactly one distribution remains invariant under this transformation. The project asks whether that uniqueness forces every initial distribution to converge weakly to the invariant one. The latter is a stronger convergence requirement associated with Markov-chain ergodicity, rather than merely uniqueness of a stationary distribution. A proof or counterexample would clarify whether local deterministic dynamics can sustain nonconvergent distributional behavior despite having only one invariant measure.

[Read in atlas](index.html#TCS-6158) · [Probabilistic cellular automata, invariant measures, and perfect sampling](https://doi.org/10.4230/LIPIcs.STACS.2011.296)
Existing status: `uncertain` · Summary written: 2026-09-11

## Semantics, logic and verification (39)

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

In a mean-payoff game, two players move a token through a finite weighted directed graph. The maximizing player wants the limiting lower average weight to be nonnegative against every opposing strategy. The project asks whether this threshold question has a deterministic algorithm polynomial in the full binary input length. Algorithms polynomial in the numerical magnitude of weights do not suffice because a large weight can have a short encoding. An efficient solution would settle a central exact optimization problem for systems with long-run rewards and adversarial control.

[Read in atlas](index.html#TCS-6568) · [The complexity of mean payoff games](https://link.springer.com/chapter/10.1007/BFb0030814) · [Faster Algorithms for Mean-Payoff Games](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf) · [Value Iteration Using Universal Graphs and the Complexity of Mean Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2020.34) · [Smoothed Analysis of Deterministic Discounted and Mean-Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.147) · [Strategy Improvement, the Simplex Algorithm and Lopsidedness](https://arxiv.org/abs/2509.16075) · [Set-defined graph classes: \(\chi\)-boundedness meets tropical algebra](https://arxiv.org/abs/2607.23754)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7230 — Tarski’s exponential function problem

Tarski’s exponential function problem asks whether one terminating algorithm can decide every first-order sentence about the standard real numbers with their full exponential function. The input is finite symbolic syntax with no arbitrary real constants or real-number oracle, and quantifiers range over all reals. Acceptance requires a complete Lean-checked proof of total correct decidability or a proof of undecidability, with no time bound and no unresolved extra hypothesis. The question extends decidable polynomial real arithmetic and already controls conditional verification results for restricted weighted automata. Macintyre–Wilkie’s conditional theorem and the checked June2026 axiomatization still rely on the real Schanuel hypothesis; restricted model completeness is a different conclusion.

[Read in atlas](index.html#TCS-7230) · [On the elementary theory of the real exponential field](https://arxiv.org/abs/2603.08365v2) · [Schanuel’s Conjecture and the Decidability of the Real Exponential Field](https://link.springer.com/chapter/10.1007/978-94-015-8923-9_11) · [Algorithmic Applications of Schanuel’s Conjecture](https://people.mpi-sws.org/~joel/publications/algorithmic-schanuel25.pdf) · [The Big-O Problem for Labelled Markov Chains and Weighted Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2020.41)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6566 — Continuous Skolem problem

A rational linear differential system evolves as a matrix exponential applied to its initial state. Continuous Skolem asks whether a specified linear observation of that trajectory is exactly zero at some nonnegative real time. The dimension is unrestricted, and the project seeks decidability without a time horizon. Approaching zero or changing sign are inadequate substitutes because trajectories may approach without hitting or touch zero without crossing it. A resolution would establish the limits of exact reachability verification even for continuous systems with linear, fully specified dynamics.

[Read in atlas](index.html#TCS-6566) · [The continuous Skolem-Pisot problem](https://perso.uclouvain.be/vincent.blondel/publications/10BDJ.pdf) · [On the Skolem Problem for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1506.00695) · [On Recurrent Reachability for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1507.03632) · [Axiomatization of Compact Initial Value Problems: Open Properties](https://publikationen.bibliothek.kit.edu/1000188295/170660770) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7192 — Decidability of multiplicative-exponential linear logic

MELL asks whether provability in a resource-sensitive propositional logic can always be decided. Its multiplicative connectives combine resources, while exponential modalities permit controlled reuse. The card specifies the entire finite proof calculus, including units and the conditions on contraction and promotion. Proof checking alone does not guarantee that a search can terminate on an unprovable input. A July 2026 preprint claims a positive resolution through general branching vector addition systems, which is recorded here without independent proof verification.

[Read in atlas](index.html#TCS-7192) · [Handbook of Linear Logic](https://ll-handbook.pages.math.cnrs.fr/book/ll-handbook-public.pdf) · [On the Decision Problem for MELL](https://www.lix.polytechnique.fr/~lutz/papers/OnDeciMELL.pdf) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.22/LIPIcs.MFCS.2025.22.html) · [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear Inductive Invariants](https://arxiv.org/abs/2607.09558v1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7310 — Unconditional decidability of exact time-bounded CTMDP reachability

The input describes a finite controlled stochastic process whose transitions occur in continuous time. A policy chooses actions from the current state and elapsed time, including between jumps. The target is exact comparison of the optimal deadline-reachability probability with rational thresholds for every initial state. The cited theorem decides this question assuming Schanuel’s conjecture. The card asks whether the same strict-threshold language is decidable unconditionally.

[Read in atlas](index.html#TCS-7310) · [On Decidability of Time-Bounded Reachability in CTMDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.133)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6036 — Decidability of restricted elementary real functions

The problem asks whether exact first-order truth is decidable over the real field with exponential, sine and cosine restricted to the unit interval. It also includes the source’s extended language with unrestricted exponential, using a tag to make both signatures one decision problem. Inputs are finite sentences with only fixed primitive constants, while all quantified variables range over the standard real numbers. Known conditional results use Schanuel’s conjecture, and continuous-system invariant questions provide a computational motivation. A solution must give an unconditional total decision procedure for the joint truth set or prove that none exists.

[Read in atlas](index.html#TCS-6036) · [Invariants for Continuous Linear Dynamical Systems](https://doi.org/10.4230/LIPIcs.ICALP.2020.107) · [Algorithmic Applications of Schanuel’s Conjecture](https://people.mpi-sws.org/~joel/publications/algorithmic-schanuel25.pdf) · [Turing meets Schanuel](https://doi.org/10.1016/j.apal.2015.10.003) · [Integration in finite terms and exponentially algebraic functions](https://arxiv.org/abs/2510.26248v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0619 — TOWER-hard reachability with seven nonnegative counters

A VASS combines finite control with nonnegative integer counters updated by fixed transition vectors. The question asks for TOWER-hard reachability using only seven counters and unary-encoded numbers. Seven counters capture the source’s request for any improvement below the known eight-counter bound, by padding unused coordinates. TOWER-hardness uses elementary-time reductions and is stronger than a collection of unrelated fixed-height exponential lower bounds. Recent lower bounds with extra signed counters concern a different computational model.

[Read in atlas](index.html#TCS-0619) · [Automata Exchange](https://automata.exchange/25.9-reachability-in-low-dimensional-vass/) · [Lower Bounds for the Reachability Problem in Fixed Dimensional VASSes](https://arxiv.org/abs/2203.04243) · [Reachability in VASS Extended with Integer Counters](https://doi.org/10.4230/LIPIcs.LICS.2026.19)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-1649 — Decidability of branching-VASS reachability

A branching vector addition system combines finite control with nonnegative integer resources. Rules can combine several already derived configurations by adding their resource vectors and a fixed displacement. Reachability asks whether a finite valid derivation tree produces exactly a supplied target. The dimension is part of the input, and every branch must be fully justified. The 2025 two-dimensional decidability theorem does not settle the arbitrary-dimensional problem.

[Read in atlas](index.html#TCS-1649) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://doi.org/10.4230/LIPIcs.MFCS.2025.22)
Existing status: `source_open` · Summary written: 2026-09-13

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

### TCS-3655 — Inductive-inductive types from inductive types without UIP

Inductive-inductive types define several mutually dependent sorts, allowing later sorts to be indexed by earlier ones. They conveniently express structures such as contexts and the types that are well formed within those contexts. The question asks whether these types can be constructed from ordinary inductive types without assuming uniqueness of identity proofs. The source's reduction relies on settings where equality is simpler, and removing that assumption requires rebuilding signatures, semantics, and the term-model construction. A successful reduction would show that this useful dependent form of mutual induction does not require an additional primitive in a richer theory of equality.

[Read in atlas](index.html#TCS-3655) · [For Finitary Induction-Induction, Induction Is Enough](https://doi.org/10.4230/LIPIcs.TYPES.2019.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4302 — Strategy synthesis for multi-objective probabilistic LTL

Multi-objective probabilistic synthesis asks one strategy to satisfy several quantitative requirements simultaneously in a stochastic game. When the requirements are probabilistic LTL properties, each combines an infinite-run temporal condition with a probability constraint. The source identifies strategy synthesis for these objectives in general stochastic games as the missing case beyond its restricted algorithms. A controller may need to balance conflicting objectives while accounting for both random transitions and adversarial choices. Resolving the problem would extend automated construction of strategies that meet several reliability or performance requirements, with explicit control over their achievable tradeoffs.

[Read in atlas](index.html#TCS-4302) · [Model Checking and Strategy Synthesis for Stochastic Games: From Theory to Practice (Invited Talk)](https://doi.org/10.4230/LIPIcs.ICALP.2016.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5682 — One-dimensional piecewise-affine reachability

A piecewise affine map chooses among finitely many affine update rules according to the region containing the current point. In one dimension, its orbit is obtained by repeatedly applying this update to a rational starting value. The question asks whether exact reachability of a rational target is decidable in the general one-dimensional setting, even with only two pieces. The source contrasts this gap with decidable subclasses and with undecidability already available for unrestricted two-dimensional maps. Resolving the two-piece case would locate a basic boundary between simple numerical iteration and computations complicated enough to defeat algorithmic reachability analysis.

[Read in atlas](index.html#TCS-5682) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5817 — Computational interpretation of impredicativity with univalence

Univalent foundations treats equivalence of types as a form of equality while supporting constructive mathematical reasoning. Propositional impredicativity principles allow certain quantifications or size changes for propositions beyond ordinary predicative universe rules. The source identifies the challenge of giving these principles a computational interpretation compatible with univalence. Its domain-theoretic development avoids the resizing axioms, demonstrating that useful semantics can be built while the stronger computational foundation is unsettled. A successful interpretation would explain how proofs using impredicative propositions can retain meaningful computation and would broaden the foundational tools available for constructive domain theory.

[Read in atlas](index.html#TCS-5817) · [Domain Theory in Constructive and Predicative Univalent Foundations](https://doi.org/10.4230/LIPIcs.CSL.2021.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5915 — Constructive simplicial models with univalent universes

Simplicial sets describe spaces through points, edges, triangles, and their higher-dimensional analogues, making them natural models for homotopy type theory. The source recalls a univalent simplicial model and asks how to obtain a constructive simplicial model with univalent universes. Constructivity requires the semantic constructions to work without the classical principles used in the original account. Cubical models provide an encouraging comparison, since a constructive treatment of univalence is available there. Solving the simplicial problem would clarify whether the familiar simplex-based geometry can support the same constructive foundations and computational ambitions as the cubical approach.

[Read in atlas](index.html#TCS-5915) · [From Cubes to Twisted Cubes via Graph Morphisms in Type Theory](https://doi.org/10.4230/LIPIcs.TYPES.2019.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5975 — Decidability of decisiveness in probabilistic transition systems

A probabilistic transition system is decisive for a target when it almost surely eventually reaches either the target or states from which the target is unreachable. This property supports approximation of reachability probabilities in infinite-state models such as probabilistic Petri nets. The source discusses deciding decisiveness for finite targets and for transition weights that depend on the current marking. Its own results resolve a substantial dynamic-weight case negatively, proving undecidability for polynomial weights even with finite or upward-closed targets. The description therefore separates that established limitation from the more specific constant-weight and restricted-model questions motivating the paper.

[Read in atlas](index.html#TCS-5975) · [About Decisiveness of Dynamic Probabilistic Models](https://doi.org/10.4230/LIPIcs.CONCUR.2023.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5987 — Decidability of weak bisimulation for normed BPA

Basic Process Algebra describes recursive sequential processes with a stack-like arrangement of process variables. Weak bisimilarity compares their observable behavior while allowing silent transitions to be hidden. The question asks whether this equivalence is decidable even for normed BPA, where each process variable can eventually terminate. The source distinguishes this from branching bisimilarity, a finer equivalence for which decidability and complexity results are available in the normed setting. An answer would clarify whether arbitrary invisible computation can be handled effectively in one of the simplest infinite-state models of recursive behavior.

[Read in atlas](index.html#TCS-5987) · [Two Lower Bounds for BPA](https://doi.org/10.4230/LIPIcs.CONCUR.2017.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6245 — Exponential witness bounds for three-dimensional VAS

Reachability in a three-dimensional vector addition system asks for a legal counter run connecting an initial and a target configuration. The source highlights the gap in understanding how long the shortest such run may need to be. Its concrete question is whether existence of any run always guarantees one of at most exponential length in the input size. Known short-run arguments in two dimensions motivate this possibility, while much larger general upper bounds leave room for doubly exponential or faster growth. Settling the witness-length question would illuminate why adding a third counter changes the structure of exact reachability.

[Read in atlas](index.html#TCS-6245) · [Involved VASS Zoo (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2022.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6359 — Decidability and completeness of concurrent Kleene algebra

Concurrent Kleene algebra represents executions as partially ordered multisets of events, preserving distinctions between sequential and parallel behavior. Refinement compares such executions by allowing additional ordering, and the interchange law captures a basic relationship between sequential and parallel composition. The quoted question concerns decidability and completeness for refinement of expressions with iteration. The source itself settles the decision problem for series-rational expressions without parallel iteration, proving EXPSPACE-completeness, while the broader signature and axiomatization questions are distinct. This distinction matters when deciding whether a concurrent specification permits an implementation with a greater degree of sequentialization.

[Read in atlas](index.html#TCS-6359) · [On Decidability of Concurrent Kleene Algebra](https://doi.org/10.4230/LIPIcs.CONCUR.2017.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7153 — Ultimate Positivity problem

An integer linear recurrence generates each term as a fixed linear combination of a bounded number of preceding terms. Ultimate positivity asks whether all sufficiently late terms are nonnegative, permitting finitely many earlier exceptions. The cited survey identifies decidability for arbitrary recurrences as the central task and highlights the difficulty already at order six. Simple recurrences, whose characteristic roots are distinct, admit a different positive result, so repeated roots are an important part of the unresolved general setting described there. An algorithm would support reasoning about eventual sign behavior and termination conditions in linear dynamical programs.

[Read in atlas](index.html#TCS-7153) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7154 — Effective ultimate-positivity thresholds for simple recurrences

For simple linear recurrence sequences, the cited survey distinguishes deciding eventual nonnegativity from computing when it begins. The task asks for an effective threshold N after which every term is nonnegative, whenever such a threshold exists. Available general decidability arguments use noneffective Diophantine approximation bounds and therefore need not produce this numerical witness. Computing it would allow all earlier terms to be checked directly, giving a route to deciding positivity of the entire sequence beyond the established low-order cases. The problem exposes a concrete gap between proving an eventual property algorithmically and extracting a usable bound on its exceptional prefix.

[Read in atlas](index.html#TCS-7154) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7156 — Universal integer termination of affine linear loops

An affine linear loop repeatedly updates an integer vector by a matrix transformation and translation while a conjunction of linear inequalities holds. Universal integer termination asks whether every integer initial vector eventually leaves the guard. The 2015 survey's generalization target removes the assumption that the update matrix is diagonalizable. Its existing results exploit spectral and arithmetic structure in the diagonalizable case, while repeated eigenvalue blocks introduce additional polynomial factors into the trajectories. Understanding the general case would connect the algebra of linear updates with a complete termination analysis over discrete initial states, rather than real or rational starting spaces.

[Read in atlas](index.html#TCS-7156) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7157 — Termination of linear-constraint loops

A linear-constraint loop specifies its next state by a conjunction of linear inequalities relating the old and new variable values. This permits several possible successors, unlike a loop whose body is a single fixed affine assignment. The source asks for a decision procedure for termination in this more general relational model. It identifies octagonal constraints as a positive special case, where the transition relation has an effectively semilinear transitive closure. Extending beyond that fragment would show whether unbounded executions can still be characterized effectively when each iteration chooses among all numerical updates satisfying general linear constraints.

[Read in atlas](index.html#TCS-7157) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

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

A parallel reachability algorithm must identify every vertex reachable from a source in a directed graph. The target combines nearly linear total work in the input size with polylogarithmic depth, using randomization and high-probability correctness. Ordinary graph search does little work but can expose a long sequence of dependent frontiers. Highly parallel transitive-closure methods may perform far more work than this one-source task requires. The question is whether shortcuts or another representation can remove long dependencies while accounting for the cost of constructing all auxiliary information.

[Read in atlas](index.html#TCS-6507) · [Parallel Reachability and Shortest Paths on Non-Sparse Digraphs: Near-Linear Work and Sub-Square-Root Depth](https://doi.org/10.4230/LIPIcs.ICALP.2026.15) · [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841) · [Õ(1)-Depth Parallel Reachability Faster than Transitive Closure](https://arxiv.org/abs/2608.13231)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7172 — Depth-first search in NC

A depth-first-search forest records the parent choices of recursive graph exploration. For an undirected graph, it is a rooted spanning forest in which every graph edge joins a vertex to one of its ancestors. The problem asks for a deterministic, uniformly specified parallel computation that constructs any such forest with polynomial resources and polylogarithmic depth. Randomized NC algorithms and deterministic results for restricted graph classes are known, but those guarantees do not settle the general target. A solution would show whether this basic search structure can always be built efficiently in parallel without random choices.

[Read in atlas](index.html#TCS-7172) · [Parallel Complexity of Depth-First-Search and Maximal Path in Restricted Graph Classes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2025.23) · [A random NC algorithm for depth first search](https://doi.org/10.1007/BF02122548) · [Nearly Work-Efficient Parallel DFS in Undirected Graphs](https://arxiv.org/abs/2304.09774)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0522 — Quantum 3-coloring of cycles in \(o(\log * n)\) rounds

Processors arranged on an oriented cycle must choose three classical colors so that adjacent processors receive different colors. The question allows quantum communication and asks for a round bound asymptotically smaller than log-star n. Nodes have distinct identifiers and know the cycle size, while their initial quantum registers are unentangled. The complete coloring must be valid with probability at least one minus one over n. A successful algorithm would beat the classical symmetry-breaking threshold, whereas a lower bound must handle quantum correlations without relying only on coarse causality constraints.

[Read in atlas](index.html#TCS-0522) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#quantum-local) · [Locality in Distributed Graph Algorithms](https://doi.org/10.1137/0221015) · [A Lower Bound on Probabilistic Algorithms for Distributive Ring Coloring](https://doi.org/10.1137/0404036) · [Finitely Dependent Coloring](https://doi.org/10.1017/fmp.2016.7) · [No Distributed Quantum Advantage for 3-Coloring Rooted Trees and 2-Coloring Even Cycles](https://arxiv.org/abs/2607.04852v2) · [Distributed Quantum Algorithms Cannot Color Cycles with Probability 1](https://arxiv.org/abs/2608.11720v1)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-0998 — Fast merging of summaries for symmetric streaming computations

The input statistic is a total Boolean function invariant under reordering the stream. A streaming program computes it using polylogarithmic memory and time per item. The selected question asks for equally efficient local summaries and merging on every binary aggregation tree. A known simulation preserves small space but can use superpolynomial merge time. The target excludes promise and randomness separations and does not require identical intermediate summaries.

[Read in atlas](index.html#TCS-0998) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:19) · [On Distributing Symmetric Streaming Computations](https://research.google.com/pubs/archive/32614.pdf) · [Turnstile Streaming Algorithms Might (Still) as Well Be Linear Sketches, for Polynomial-Length Streams](https://arxiv.org/abs/2604.22052)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7336 — Common2 membership of FIFO queues

Several processes concurrently insert and remove items from a FIFO queue. Every continuing process must complete its own operation despite arbitrary delays of others. Only read/write registers and test-and-set primitives are available. Known restricted queue implementations do not cover the full interface. The question separates the synchronization power of a queue from that of weaker shared objects.

[Read in atlas](index.html#TCS-7336) · [Nontrivial and Universal Helping for Wait-Free Queues and Stacks](https://drops.dagstuhl.de/storage/00lipics/lipics-vol046-opodis2015/LIPIcs.OPODIS.2015.31/LIPIcs.OPODIS.2015.31.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0515 — Deterministic volume gap

The VOLUME model measures how many graph vertices an adaptive local algorithm inspects to determine one requested output. Outputs from separate queries must still fit together into a single valid labeling. The conjecture says every deterministic locally checkable problem with sublinear worst-case volume actually has O(log-star n) volume. It concerns fixed bounded-degree graph families with exact size information and polynomially bounded identifiers. Proving the collapse would eliminate an entire intermediate range of deterministic local information complexity, despite the richer range available to randomized algorithms.

[Read in atlas](index.html#TCS-0515) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [The randomized local computation complexity of the Lovász local lemma](https://arxiv.org/abs/2103.16251v2) · [The Landscape of Distributed Complexities on Trees and Beyond](https://arxiv.org/abs/2202.04724v2) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [New Complexity Classes in Locally Checkable Labeling for Local Computation Algorithms](https://arxiv.org/abs/2607.09626v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0986 — Characterizing separable distances approximable in small streaming space

A local nonnegative cost φ defines a dissimilarity by summing over corresponding frequency coordinates. The stream may insert and delete frequencies while keeping both vectors nonnegative. The selected task classifies exactly which effectively evaluable costs admit polylogarithmic-space relative approximations. The criterion must cover the entire specified domain and include both algorithms and impossibility proofs. Known offset obstructions, difference-based aggregate classifications and norm-sketching results cover only parts of this domain.

[Read in atlas](index.html#TCS-0986) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:5) · [Streaming Space Complexity of Nearly All Functions of One Variable on Frequency Vectors](https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/bcwy16.pdf) · [The Andoni–Krauthgamer–Razenshteyn Characterization of Sketchable Norms Fails for Sketchable Metrics](https://arxiv.org/abs/1810.04321)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0469 — Maximum independent set in the congested clique

An exact maximum independent set contains as many pairwise nonadjacent vertices as possible. Each vertex initially knows its incident edges and can exchange a logarithmic number of bits with every other processor in a round. The target is the optimal worst-case number of deterministic communication rounds, with local computation uncharged. A tight bound would measure the information exchange needed for exact graph optimization in a network without distance barriers. The source leaves bandwidth and randomness broader, while this card preserves its explicit deterministic logarithmic-bandwidth specialization.

[Read in atlas](index.html#TCS-0469) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume15/issue05/25191/html/DagRep.15.5.1/DagRep.15.5.1.html) · [On the Power of the Congested Clique Model](https://www.cs.tau.ac.il/~roshman/papers/podc14_clique.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0519 — Bipartite maximal matching with polynomial-in-degree volume

A maximal matching is a collection of disjoint edges to which no further edge can be added. The question asks for a deterministic local-query algorithm on bipartite graphs whose inspected volume is polynomial in the maximum degree and independent of graph size. A proper two-coloring identifying the bipartition is supplied. Simulating a distributed proposal algorithm by exploring whole neighborhoods can incur an exponential dependence on degree. The project is to follow a much smaller dependency structure while ensuring that separately answered vertex queries describe the same matching.

[Read in atlas](index.html#TCS-0519) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [Truly Tight-in-\(\Delta\) Bounds for Bipartite Maximal Matching and Variants](https://arxiv.org/abs/2002.08216v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6125 — Linear CONGEST lower bound with logarithmic LOCAL complexity

An LCL specifies legal output labels by a finite list of constant-radius neighborhoods. The question asks for one problem that is solvable in logarithmic deterministic LOCAL time but needs linear randomized CONGEST time. Both models communicate along the same bounded-degree graph, while CONGEST restricts each message to logarithmically many bits. Such a result would isolate an extreme cost of bandwidth despite local verifiability of solutions. The card requires all connected inputs without additional promises and states the identifiers, private randomness and global error convention explicitly.

[Read in atlas](index.html#TCS-6125) · [Locally Checkable Labelings with Small Messages](https://drops.dagstuhl.de/doi/10.4230/LIPIcs.DISC.2021.8) · [Locally Checkable Labelings with Small Messages](https://jukkasuomela.fi/doc/lcl-congest.pdf) · [It does not matter how you define locally checkable labelings](https://arxiv.org/abs/2602.18188) · [It does not matter how you define locally checkable labelings](https://jukkasuomela.fi/lcl-definitions/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0940 — Lifting CSP sketching resistance to sublinear streaming resistance

Each fixed predicate family defines a maximum constraint-satisfaction problem. A nontrivial approximation beats the best constant lower bound on the optimum by a fixed amount. The conjecture lifts resistance to small mergeable sketches into resistance to all sublinear-space streaming algorithms. Both the algorithm model and the space threshold change in the implication. The 2026 LP-gap lower bounds are recorded without claiming a verified resolution of this exact lifting statement.

[Read in atlas](index.html#TCS-0940) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf) · [Sketching Approximability of All Finite CSPs](https://arxiv.org/abs/2105.01161) · [Optimal Single-Pass Streaming Lower Bounds for Approximating CSPs](https://eccc.weizmann.ac.il/report/2026/054/)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7337 — Register space of obstruction-free set agreement

Processes must decide on at most k of their proposed values. A process is guaranteed to finish if it eventually runs alone. The resource being minimized is the number of shared read/write registers. Known lower and upper bounds are the ceiling of n/k and n-k+1. The benchmark requests the full register-space function over all n greater than k.

[Read in atlas](index.html#TCS-7337) · [Revisionist Simulations: A New Approach to Proving Space Lower Bounds](https://epubs.siam.org/doi/10.1137/20M1322923) · [Solving Tasks with Fewer Registers Than Processes](https://drops.dagstuhl.de/storage/00lipics/lipics-vol361-opodis2025/html/LIPIcs.OPODIS.2025.21/LIPIcs.OPODIS.2025.21.html)
Existing status: `source_open` · Summary written: 2026-09-13

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

A maximal independent set is independent and places every excluded vertex next to a selected one. In the congested clique, processors can send separate short messages directly to every other processor. The question asks whether a randomized algorithm can solve this task in a constant number of rounds on every input graph with high probability. Collecting all edges at one leader is too expensive, but the algorithm need not reconstruct the entire graph to choose a valid set. The target is to replace repeated sparsification and degree-reduction phases with a bounded amount of globally coordinated communication.

[Read in atlas](index.html#TCS-6501) · [When MIS and Maximal Matching are Easy in the Congested Clique](https://arxiv.org/abs/2502.21031) · [Improved Massively Parallel Computation Algorithms for MIS, Matching, and Vertex Cover](https://arxiv.org/abs/1802.08237) · [Time and Space Optimal Massively Parallel Algorithm for the 2-Ruling Set Problem](https://doi.org/10.4230/LIPIcs.DISC.2023.11)
Existing status: `open` · Summary written: 2026-09-11

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

### TCS-0993 — Graph Distances

A graph stream reveals edges in sequence while the algorithm keeps a small memory state. The task is to approximate the shortest-path distance between specified vertices. The source asks whether multiple passes or random edge order permit better approximations than approaches based on preserving many distances in a spanner. Following reachability one layer per pass computes the exact distance, but can require too many scans for distant vertices. The project is to exploit the single-pair objective or additional passes without storing a large global distance-preserving graph.

[Read in atlas](index.html#TCS-0993) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0954 — Metric TSP Cost Approximation

A metric traveling-salesperson query algorithm learns distances between pairs of points on demand. The source asks whether it can approximate the optimal tour length within a factor strictly below two using o(n squared) distance queries. Estimating a minimum spanning tree's weight gives a near-two approximation without recovering the tree itself. However, constructing a good spanning tree can already require quadratically many queries, obstructing a direct use of classical tour algorithms. The project is to estimate the tour's value more accurately while avoiding the information needed to output an explicit global structure.

[Read in atlas](index.html#TCS-0954) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:71)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0969 — Approximating LIS Length in the Streaming Model

The longest increasing subsequence of a sequence is its largest order-preserving selection of entries whose values increase. The question asks for the randomized streaming space needed to approximate its length within a factor of two. The algorithm may use one pass or a fixed constant number of passes. The source presents square-root-space deterministic bounds, but the communication problems underlying the deterministic lower bounds become easy with randomness. A resolution therefore needs either a better randomized summary or a lower-bound argument that survives the extra power of random choices.

[Read in atlas](index.html#TCS-0969) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0980 — Random Walks

The task is to simulate a long random walk on a graph presented as an edge stream. The source asks whether nearly linear memory can reduce the number of passes to a polylogarithmic function of graph size and walk length. It also asks for the complexity of approximating the walk's endpoint distribution and identifying its most likely vertices. These tasks may require less information than producing every step of the trajectory. A resolution would clarify how effectively repeated scans can substitute for direct access to the transition choices of a large graph.

[Read in atlas](index.html#TCS-0980) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0985 — Streaming space for additive \(L_\infty\) estimation

The output is a single estimate of the largest absolute coordinate of a streamed frequency vector. The allowed additive error is one over k times the final L1 or L2 norm. Insertion-only streams and signed differences of two streams are distinct modes of the same resource question. The target is a tight bit-space characterization in the domain size, update budget and accuracy. A 2016 paper reports resolving the insertion-only L1 part, while this review does not certify a complete characterization of all cases.

[Read in atlas](index.html#TCS-0985) · [Open Problem 3: L-infinity Estimation](https://sublinear.info/3) · [An Optimal Algorithm for l1-Heavy Hitters in Insertion Streams and Related Problems](https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/bdw16.pdf)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-0988 — Deterministic Summary Structures

A turnstile stream adds and subtracts from item frequencies, and the algorithm must later estimate individual frequencies with error proportional to the final l1 norm. Randomized summaries achieve small memory by hashing items into shared counters. The source asks whether a deterministic summary can match that space usage. It describes deterministic constructions with larger dependence on the accuracy parameters and conjectures that the gap may be necessary. An algorithm or lower bound would clarify whether randomness is essential for compact frequency summaries under cancellations and adversarial updates.

[Read in atlas](index.html#TCS-0988) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0834 — Estimating a Graph's Degree Distribution

A graph's degree distribution records how common vertices of different degrees are. The source entry asks how this distribution can be estimated without reading the entire graph. Sampling vertices uniformly and sampling endpoints of edges can produce different biases. An efficient estimator would summarize network structure while carefully accounting for the information supplied by the access model. The saved title does not specify allowed queries, additive or multiplicative accuracy, or how rare degrees are treated, so a precise sample-complexity target cannot yet be assigned.

[Read in atlas](index.html#TCS-0834) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:98)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0836 — Non-Adaptive Group Testing

Group testing identifies a small set of special items by querying whether selected pools contain any of them. A non-adaptive strategy chooses all pools before observing any answers. The saved question concerns the cost of achieving identification under that restriction. Determining the best constructions would clarify how much one loses by requiring tests to run simultaneously. The inherited label does not state whether answers are noisy, whether recovery is exact, or the number of special items, so the intended tradeoff among tests and error remains unspecified.

[Read in atlas](index.html#TCS-0836) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:95)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0849 — Group Testing

Group testing combines several items into one query to learn whether the pool contains a relevant item. The saved entry asks about the information and computation required to recover the hidden set. Pooling can dramatically reduce testing effort when few items are relevant, but overlapping answers must still identify them unambiguously. Sharper bounds would guide how efficiently one can learn sparse hidden structure. The source label does not specify adaptive versus fixed tests, noise, or recovery guarantees, so this working summary does not choose one of the many inequivalent testing models.

[Read in atlas](index.html#TCS-0849) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:33)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1588 — Characterizing robustly computable predicates and functions

Continuous chemical reaction networks represent inputs and outputs as nonnegative concentrations evolving under mass-action kinetics. Robust computation requires convergence to the correct answer for every positive choice of reaction-rate constants. The source constructs robust networks for multithreshold predicates and a specified class of piecewise floor-affine functions, where negative affine values are truncated to zero. It conjectures that these constructions describe exactly the predicates and functions the model can compute. A matching impossibility theorem would turn the positive constructions into a complete characterization of computation that is insensitive to kinetic parameters.

[Read in atlas](index.html#TCS-1588) · [Robust Predicate and Function Computation in Continuous Chemical Reaction Networks](https://doi.org/10.4230/LIPIcs.DISC.2025.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2233 — Superlinear local complexity of hereditary graph classes

Local certification gives each graph vertex a certificate that it verifies using only its nearby information. The source asks whether a hereditary graph class can require certificates of size growing faster than linearly in the number of vertices. It also asks for this phenomenon under the stronger requirement of closure under subgraphs. Existing linear lower bounds motivate seeking a larger information barrier. Such examples would show that even deletion-stable structural properties can demand exceptionally large local evidence for a globally correct decision.

[Read in atlas](index.html#TCS-2233) · [Local Certification of Geometric Graph Classes](https://doi.org/10.4230/LIPIcs.MFCS.2024.48)
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

### TCS-5795 — One-pass semi-streaming depth-first search

Depth-first-search tree construction is easy when a streaming algorithm can retain the complete graph. The semi-streaming restriction instead allows only \(\widetilde{O}\)\((n)\) memory for an n-vertex graph, potentially requiring repeated edge scans. The source asks whether more than one pass is inherently necessary to construct a DFS tree in this space regime. Its cited algorithms have pass counts depending on the height of the produced tree, leaving a large gap between simple upper bounds and the sought impossibility result. Resolving the one-pass question would determine whether the nested dependencies of depth-first search force repeated access under near-linear storage.

[Read in atlas](index.html#TCS-5795) · [Streaming Complexity of Spanning Tree Computation](https://doi.org/10.4230/LIPIcs.STACS.2020.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5797 — Linear scaling of local certificate size with verification radius

Local certification gives each graph vertex a short certificate and lets it verify a global claim by inspecting nearby information. Suppose the optimal certificate size is s when the verifier sees only distance-one neighborhoods. The conjecture asks whether allowing inspection to distance d always reduces the required size to at most a constant times \(s/d\). For local properties, the source stresses that the dependence must track their natural parameters, rather than merely asymptotic graph size. Resolving this tradeoff would show whether a wider view can universally substitute for stored proof information or whether some properties resist such compression.

[Read in atlas](index.html#TCS-5797) · [Local Certification of Local Properties: Tight Bounds, Trade-Offs and New Parameters](https://doi.org/10.4230/LIPIcs.STACS.2024.21)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6080 — Linear-round weighted APSP in CONGEST

Weighted all-pairs shortest paths requires every vertex to learn exact distances to all others in an edge-weighted network. The 2017 source asks whether this can be done in a linear number of CONGEST communication rounds. Straightforward repeated distance propagation is slower, while subquadratic algorithms suggest room for improvement. The paper also shows that a standard two-party communication framework cannot establish a superlinear lower bound for this task. The question therefore seeks either an algorithm coordinating many weighted searches within linear time or a different explanation of why their shared communication demands prevent it.

[Read in atlas](index.html#TCS-6080) · [Quadratic and Near-Quadratic Lower Bounds for the CONGEST Model](https://doi.org/10.4230/LIPIcs.DISC.2017.10)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6206 — Clique detection in CONGEST

In \(\mathrm{CONGEST}_{b}\), each graph edge carries at most b bits per communication round. The source studies detecting cliques with size at least four and up to order \(\sqrt{n}\), asking how far the round complexity exceeds its roughly \(\sqrt{n}/b\) lower-bound scale. A linear-round algorithm leaves a substantial gap, particularly for fixed clique sizes. The paper proves that its two-party vertex-partition method cannot establish the stronger lower bounds that would close that gap. The project therefore calls for improved detection algorithms or new communication-hardness techniques that capture interactions among more than the two partitioned views.

[Read in atlas](index.html#TCS-6206) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6380 — Load-optimal parallel natural joins

A natural join combines database relations by matching equal values on shared attributes. In massively parallel computation, the load measures how much data any one of p machines must handle. The question asks for algorithms matching the \(\Omega (m/p^{1/\rho})\) load bound for arbitrary join queries, where m is total input size and \(\rho\) is the fractional edge-cover number. The source achieves the target for binary-relation joins in a small constant number of rounds, but those graph-shaped queries do not cover arbitrary relation arities. A general construction would align parallel join execution with the structural lower bound of the query hypergraph.

[Read in atlas](index.html#TCS-6380) · [A Simple Parallel Algorithm for Natural Joins on Binary Relations](https://doi.org/10.4230/LIPIcs.ICDT.2020.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7010 — Linear-sketch complexity of the nuclear norm

The nuclear norm of a matrix is the sum of its singular values and measures a different aspect of size from the Frobenius or spectral norm. A linear sketch compresses the matrix through linear measurements before estimating this norm. The source asks for the optimal sketch dimension needed for a constant-factor approximation. Its discussion places nuclear-norm sketching between neighboring norms with very different behavior: constant dimension for the Frobenius norm and essentially full matrix dimension for the spectral norm. Tight bounds would show whether low-dimensional linear summaries can preserve this important aggregate of singular-value information.

[Read in atlas](index.html#TCS-7010) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

## Optimization and numerical computation (20)

### TCS-0008 — Strongly polynomial linear programming

Linear programming optimizes a linear objective subject to linear equality and nonnegativity constraints. The question asks whether every rational instance can be solved using a number of arithmetic operations polynomial only in its numbers of variables and constraints. Intermediate numbers must also have encoding lengths bounded polynomially in the full input length. Existing polynomial-time guarantees may depend on how many bits describe the coefficients, which is the dependence this target seeks to remove. A solution must handle exact optima, infeasibility, and unbounded objectives within the same strongly polynomial framework.

[Read in atlas](index.html#TCS-0008) · [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8) · [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250) · [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf) · [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186) · [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf) · [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6574 — Exact semidefinite feasibility in polynomial time

A semidefinite feasibility instance asks whether some real assignment makes an affine combination of rational symmetric matrices positive semidefinite. The target is an exact yes-or-no decision in polynomial time in the ordinary bit model. Numerical approximation does not settle this question because an infeasible affine space can approach the positive semidefinite cone arbitrarily closely. Feasible rational inputs can also require irrational or very large witnesses. The challenge is to decide arbitrary degenerate instances efficiently without adding regularity assumptions that make approximation algorithms easier to analyze.

[Read in atlas](index.html#TCS-6574) · [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433) · [On the Turing Model Complexity of Interior Point Methods for Semidefinite Programming](https://epubs.siam.org/doi/10.1137/15M103114X) · [Exact algorithms for semidefinite programs with degenerate feasible set](https://www.sciencedirect.com/science/article/pii/S0747717120301176) · [How Do Exponential Size Solutions Arise in Semidefinite Programming?](https://epubs.siam.org/doi/10.1137/21M1434945) · [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271) · [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7227 — Conforti–Cornuéjols conjecture

A clutter is a finite family of sets with no redundant containing member. Its packing property requires unweighted packing–covering equality in every deletion and contraction minor. The conjecture asks whether this already implies equality for every nonnegative integer capacity vector. Weighted packings may repeat members within those capacities. Recent source results cover finite ground-set sizes and restricted families, while retaining the general question.

[Read in atlas](index.html#TCS-7227) · [Combinatorial Optimization: Polyhedra and Efficiency](https://homepages.cwi.nl/~lex/co/) · [Testing the max-flow min-cut property and the replication conjecture](https://arxiv.org/abs/2606.16543v2) · [Equality of ordinary and symbolic powers and the Conforti–Cornuéjols conjecture for (n−2)-uniform clutters](https://arxiv.org/abs/2510.15864v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6585 — Nearly linear-time solution of general sparse linear systems

A sparse linear system stores only the nonzero entries of its coefficient matrix, making matrix-vector multiplication relatively cheap. The question asks whether solving every well-conditioned rational system approximately can take nearly linear time in that sparse input size. The saved formulation bounds coefficient lengths, conditioning, and requested residual accuracy to avoid hiding excessive numerical costs. It seeks an explicit solution vector with high enough success probability from a randomized classical algorithm. Such a result would extend the efficiency of structured Laplacian solvers to general sparse matrices, where sparsity alone currently provides much less algorithmic structure.

[Read in atlas](index.html#TCS-6585) · [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254) · [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430) · [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553) · [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53) · [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6578 — Smale’s seventh problem

Smale's seventh problem concerns placing N points on the unit sphere so that their logarithmic interaction energy is nearly minimal. The target is an algorithm running in time polynomial in N. Its output energy may exceed the global minimum by only a universal constant times log N. This is an additive energy guarantee, which requires more precise control than merely producing visually well-distributed points. A construction with a rigorous bound would connect efficient computation with the equilibrium behavior of many mutually repelling particles on a curved surface.

[Read in atlas](index.html#TCS-6578) · [Logarithmic energy for zeros of random polynomials](https://www.lebesgue.fr/sites/default/files/inline-files/Yakir.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6572 — Polynomial-time simplex pivot rule

The simplex method solves a linear program by moving between feasible bases through legal pivots. This question asks for a deterministic pivot algorithm whose total bit complexity is polynomial for every rational input and supplied feasible starting basis. Finding the optimum by another method does not suffice unless the required sequence of pivots can also be followed efficiently. Degenerate pivots complicate progress because they may change the basis without changing the objective value. A positive answer would provide a worst-case polynomial guarantee for simplex itself, without automatically establishing the stronger arithmetic bound of strongly polynomial linear programming.

[Read in atlas](index.html#TCS-6572) · [Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time](https://www.cs.yale.edu/homes/spielman/simplex/) · [An unconditional lower bound for the active-set method on the hypercube](https://arxiv.org/abs/2502.18019) · [An Unconditional Lower Bound for the Active-Set Method in Convex Quadratic Maximization](https://epubs.siam.org/doi/10.1137/1.9781611978971.14) · [Lower Bounds for Ranking-Based Pivot Rules](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.31/LIPIcs.STACS.2026.31.html) · [On the number of degenerate simplex pivots](https://link.springer.com/article/10.1007/s10107-026-02349-x)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7314 — Komlós conjecture

Komlós asks whether every collection of real vectors of Euclidean norm at most one can be assigned signs so that every coordinate of their sum is bounded by one universal constant. The dimensions and entries are arbitrary, and the same complete choice of signs must control all coordinates simultaneously. The positive answer requires some finite constant, without determining the best one or giving an efficient algorithm. Such a theorem would imply the Beck–Fiala discrepancy bound and strengthen rounding and optimization guarantees. A complete Lean proof must establish the universal bound or unbounded discrepancy; the 10 September 2026 preprint claims the full positive bound, but this review has not independently verified its proof.

[Read in atlas](index.html#TCS-7314) · [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961v2) · [An Algorithm for Komlós Conjecture Matching Banaszczyk’s Bound](https://doi.org/10.1137/17M1126795) · [An Exposition of the \(\widetilde O((\log n)^{1/4})\) Bound for the Komlós Problem](https://arxiv.org/abs/2608.28452v1) · [A \((\log n)^{1/4}\) Bound for the Komlós Problem](https://arxiv.org/abs/2609.08885v1) · [Algorithms for Standard-Form ILP Problems via Komlós’ Discrepancy Setting](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.25) · [Vector Balancing via Directional Total Variation](https://arxiv.org/abs/2609.11189v1)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-7315 — Beck–Fiala conjecture

The Beck–Fiala conjecture asks whether bounded participation of each element in a set system guarantees a coloring with square-root imbalance in every set. If each element belongs to at most t sets, one complete assignment of signs must achieve imbalance at most a universal constant times the square root of t. The constant must work for every number of elements and sets, with no lower restriction on t or requirement for an efficient algorithm. The question is a central sparsity principle for simultaneous rounding and is implied by the more general Komlós conjecture. A complete Lean proof must establish the universal bound or unbounded normalized discrepancy; a 10 September 2026 preprint claims the full positive bound, with its proof unverified in this review.

[Read in atlas](index.html#TCS-7315) · [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961v2) · [Online Beck–Fiala Down to Logarithmic Sparsity](https://arxiv.org/abs/2607.14238v1) · [Vector Balancing via Directional Total Variation](https://arxiv.org/abs/2609.11189v1)
Existing status: `uncertain` · Summary written: 2026-09-14

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

Minimax optimization models a player minimizing an objective against a second player who maximizes it. In nonconvex–nonconcave problems, stationary points need not represent the intended local minimax behavior. The selected question asks for a first-order method whose stable convergence targets are restricted to local minimax optima. Reversing the players' optimization order or merely driving both gradients toward zero can select inappropriate solutions. A method with the desired guarantee would clarify the dynamics needed for adversarial optimization, including the mathematical problems underlying some generative-model training procedures.

[Read in atlas](index.html#TCS-0673) · [COLT / PMLR](https://proceedings.mlr.press/v195/chae23a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

## Geometry, topology and metric spaces (40)

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

### TCS-0427 — NP certificates for homeomorphism of three-manifolds

Two triangulations can describe the same three-dimensional manifold while looking combinatorially unrelated. This question asks whether every homeomorphic pair has a certificate whose size and verification time are polynomial in the input. Such a certificate need not be found efficiently by the verifier itself. The challenge is to encode the necessary topological equivalence without an excessively long sequence of transformations. An NP upper bound would distinguish the difficulty of discovering a homeomorphism from the difficulty of checking convincing evidence that one exists.

[Read in atlas](index.html#TCS-0427) · [Triangulations in Geometry and Topology: Homeomorphism](https://doi.org/10.4230/DagRep.14.2.120) · [Algorithmic homeomorphism of 3-manifolds as a corollary of geometrization](https://doi.org/10.2140/pjm.2019.301.189) · [Some conditionally hard problems on links and 3-manifolds](https://arxiv.org/abs/1602.08427) · [Recognition of Seifert fibered spaces with boundary is in NP](https://doi.org/10.1007/s00208-024-02920-x) · [Computational Geometry: Treewidth of 3-Manifolds](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7189 — Minimum-weight triangulation in NP

The input gives rational planar points and a rational limit on the total length of a triangulation. Every input point must be used, no extra points may be added, and Euclidean edge lengths are compared exactly. The question asks whether every feasible instance has a short certificate that can be checked in polynomial bit time. NP-hardness is known, but the sum of potentially irrational edge lengths prevents the usual edge-list argument from establishing NP membership. Practical exact solutions and rounded-cost variants do not settle the certificate question for arbitrary exact inputs.

[Read in atlas](index.html#TCS-7189) · [Minimum-weight triangulation is NP-hard](https://arxiv.org/abs/cs/0601002) · [Solving Large-Scale Minimum-Weight Triangulation Instances to Provable Optimality](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.44) · [Taming Infinity One Chunk at a Time: Concisely Represented Strategies in One-Counter MDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.138)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0410 — Output-sensitive convex hull complexity

An output-sensitive convex hull algorithm charges for both its input points and the facets it actually produces. The question asks for the best such running time for point sets in fixed-dimensional Euclidean space. Small hulls should be cheaper than the worst-case hull complexity would suggest. The difficult target is to reconcile reading the input, identifying extreme structure, and listing the output with nearly optimal overhead. Progress would improve geometric optimization whenever many input points contribute little to the final convex boundary.

[Read in atlas](index.html#TCS-0410) · [The Open Problems Project: Output-sensitive Convex Hull](https://topp.openproblem.net/p15) · [Output-Sensitive Results on Convex Hulls, Extreme Points, and Related Problems](https://tmc.web.engr.illinois.edu/convj.pdf) · [A Combinatorial Proof of Universal Optimality for Computing a Planar Convex Hull](https://doi.org/10.4230/LIPIcs.ESA.2025.102)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0973 — Earth mover distance sketching complexity

Each planar grid subset must be compressed independently before the other input is available. The decoder uses the two bit strings to estimate the minimum Manhattan-cost matching of equal-size sets. The target is the optimal tradeoff between sketch length and multiplicative approximation, with constant success probability for every fixed pair. Known embedding and full transportation-norm results do not automatically characterize arbitrary decoders for these subset sketches. Sharp bounds would establish how much information optimal-transport comparisons must retain.

[Read in atlas](index.html#TCS-0973) · [Sketching Earth Mover Distance](https://sublinear.info/index.php?title=Open_Problems:49) · [Efficient Sketches for Earth-Mover Distance, with Applications](https://www.mit.edu/~andoni/papers/emdStream.pdf) · [Sketching and Embedding are Equivalent for Norms](https://arxiv.org/abs/1411.2577v3) · [Lower Estimates for L₁-Distortion of Transportation Cost Spaces](https://doi.org/10.1145/3798129.3800785)
Existing status: `source_open` · Summary written: 2026-09-14

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

Triangulations of the same compact three-manifold are connected by local bistellar flips. The question asks whether two triangulations can always be connected using polynomially many such moves in their input sizes. The polynomial is initially allowed to depend on the fixed manifold. A path may temporarily use different numbers of tetrahedra, so connectivity alone provides no useful quantitative bound. The result would control the amount of local rewriting needed to pass between alternative finite descriptions of one topological space.

[Read in atlas](index.html#TCS-0432) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0428 — NP recognition of closed hyperbolic three-manifolds

The input describes a compact connected three-manifold by gluing faces of finitely many tetrahedra. The question is whether being closed and admitting a hyperbolic metric always has a polynomial-size certificate. A single deterministic verifier must check such certificates in polynomial time for every input triangulation. Recognition is decidable, but this does not give the required certificate-size and verification-time bounds. A positive answer would connect a global geometric structure with short, efficiently verifiable combinatorial evidence.

[Read in atlas](index.html#TCS-0428) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0381 — Flip Graph Connectivity in 3D

Fix a set of points in three dimensions with no four coplanar and consider all its geometric tetrahedralizations. Two tetrahedralizations are adjacent when a local configuration of two tetrahedra is replaced by three, or conversely. The question asks whether these moves connect the entire collection. Results for topological triangulations, additional vertices, or higher dimensions do not answer this precise geometric case. Connectivity would justify navigating among all tetrahedralizations by local modifications alone, a principle underlying many mesh improvement procedures.

[Read in atlas](index.html#TCS-0381) · [The Open Problems Project](https://topp.openproblem.net/p28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0382 — General Unfoldings of Nonconvex Polyhedra

General unfolding allows a polyhedral surface to be cut through faces as well as along original edges. The target is a single connected planar piece whose interior does not overlap itself. The source asks whether every closed polyhedron admits such an unfolding, including nonconvex ones. Positive constructions for convex and certain orthogonal polyhedra motivate the broader question. It asks whether arbitrary surface cuts can always overcome the geometric obstructions that prevent more restrictive kinds of polyhedral nets.

[Read in atlas](index.html#TCS-0382) · [The Open Problems Project](https://topp.openproblem.net/p43)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0340 — Average Distortion Embeddings

An average-distortion embedding controls aggregate squared distances while remaining nonexpansive for every pair. The source considers the square-root metric associated with a finite-dimensional normed space. An existence theorem supplies a Hilbert-space embedding with favorable dependence on dimension, but its duality proof does not provide an explicit map. The task is to construct and evaluate an embedding efficiently from the supplied point set. This would turn a structural geometric theorem into an algorithmic primitive for proximity search and related computations.

[Read in atlas](index.html#TCS-0340) · [Computational Geometry](https://doi.org/10.4230/DagRep.11.4.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0970 — Fast JL Transform for Sparse Vectors

A Johnson-Lindenstrauss transform maps a vector into fewer dimensions while approximately preserving its Euclidean length with high probability. The target dimension is O(\(\log (1/\mathrm{P})\) divided by epsilon squared) for failure probability P and error epsilon. The source asks for applying the transform to an s-sparse input in time roughly s plus the output dimension, up to polylogarithmic factors. It also asks for an explicit distribution generated from only \(O(\log (d/\mathrm{P}))\) random bits. The project combines fast multiplication, optimal dimensional reduction, and a compact random seed rather than optimizing any one resource alone.

[Read in atlas](index.html#TCS-0970) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0398 — Planar Euclidean Maximum TSP

The maximum Euclidean traveling-salesman problem seeks the longest tour through a planar point set. Every point must be visited once before the tour closes, but long connections are rewarded rather than penalized. The source asks for the complexity of finding the exact optimum in the plane. Algorithms for polyhedral distance functions and hardness in higher-dimensional Euclidean space do not determine this intermediate case. The problem tests how the geometry of the distance function affects a familiar combinatorial optimization task.

[Read in atlas](index.html#TCS-0398) · [The Open Problems Project](https://topp.openproblem.net/p49)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0327 — Simple Polygonalizations

A simple polygonalization orders a given planar point set around a polygon without crossing its edges. The source asks whether the total number of such polygons can be computed in polynomial time. Finding one polygon is much easier than accounting for every valid cyclic ordering. The counting question is also related to generating a uniformly random polygon on the same vertices. A sharp algorithmic classification would clarify whether geometric noncrossing structure can overcome the large combinatorial space of candidate tours.

[Read in atlas](index.html#TCS-0327) · [The Open Problems Project](https://topp.openproblem.net/p16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0409 — Minimum-Link Path in 2D

A minimum-link path connects two locations among polygonal obstacles while using as few straight segments as possible. Its objective counts bends and segments rather than total Euclidean length. The source asks whether the planar problem admits a subquadratic algorithm. A short-distance path need not minimize links, so standard shortest-path techniques do not automatically achieve the target. The task would improve route simplification in environments where changing direction is costly even when travel along a straight segment is inexpensive.

[Read in atlas](index.html#TCS-0409) · [The Open Problems Project](https://topp.openproblem.net/p22)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-7006 — Optimal input-sparsity subspace embeddings

A subspace embedding compresses a matrix while approximately preserving the Euclidean norm of every vector in its column space. The source conjectures an embedding dimension proportional to dimension plus logarithmic inverse failure probability, divided by accuracy squared. At the same time, multiplying by the embedding should take input-sparsity time with only the specified logarithmic and inverse-accuracy overhead. The two requirements must hold together, since a small sketch can still be expensive to construct. Such a construction would improve the foundational compression step used by fast regression and other numerical linear-algebra algorithms.

[Read in atlas](index.html#TCS-7006) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

## Learning theory (38)

### TCS-6541 — Linear-size sample compression

Sample compression represents a labeled training set by retaining only a few examples and a bounded amount of extra information. A fixed reconstruction rule must recover a hypothesis agreeing with every original training label whenever the sample is realizable. This project asks whether every binary class of VC dimension d admits a scheme whose total charged size is proportional to d. The question concerns the number of retained examples and side-information bits, not the ordinary bit length of the examples themselves. A linear bound would connect the statistical capacity measured by VC dimension with a comparably small combinatorial explanation of every realizable sample.

[Read in atlas](index.html#TCS-6541) · [Sample compression schemes for VC classes](https://arxiv.org/abs/1503.06960v2) · [Dual VC Dimension Obstructs Sample Compression by Embeddings](https://proceedings.mlr.press/v247/chase24a.html) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html) · [Sample compression schemes for balls in structurally sparse graphs](https://arxiv.org/abs/2604.02949v1) · [The No-Clash Teaching Dimension is Bounded by VC Dimension (withdrawn)](https://arxiv.org/abs/2603.23561v4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6542 — Learning parity with noise in polynomial time

A parity function returns the XOR of a hidden subset of input coordinates. Without label noise, random examples produce linear equations that reveal the hidden subset efficiently. This project asks whether a polynomial-time classical algorithm can still recover it when each label is independently flipped at a fixed rate below one half. Polynomially many samples contain enough information, but searching all candidate subsets takes exponential time. An efficient learner must avoid that search using only ordinary random examples, without chosen noiseless queries or restrictions that make the unknown subset sparse.

[Read in atlas](index.html#TCS-6542) · [Noise-Tolerant Learning, the Parity Problem, and the Statistical Query Model](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2003-Noise-Tolerant_Learning.pdf) · [The Parity Problem in the Presence of Noise, Decoding Random Linear Codes, and the Subset Sum Problem](https://cseweb.ucsd.edu/~vlyubash/papers/parityproblem.pdf) · [Memory-Sample Lower Bounds for Learning Parity with Noise](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.60) · [Hardness Amplification for (Sparse) LPN](https://arxiv.org/abs/2605.10056) · [Towards Worst-case Hardness for Low-Noise LPN](https://eccc.weizmann.ac.il/report/2026/095/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6543 — Learning Boolean juntas from uniform random examples

A Boolean junta depends on only k coordinates even though its input contains n possible features. The project asks whether it can be learned from uniformly random labeled examples in time polynomial in n, the size of its k-variable truth table, and the inverse error tolerance. The allowed exponential dependence on k accommodates an arbitrary function of the relevant coordinates. The difficult step is locating useful coordinates without enumerating all possible subsets of the n features. A learner with this guarantee would turn hidden low-dimensional structure into efficient prediction even when the number of relevant variables grows logarithmically with n.

[Read in atlas](index.html#TCS-6543) · [Learning functions of k relevant variables; author manuscript titled Learning juntas](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf) · [Finding Correlations in Subquadratic Time, with Applications to Learning Parities and the Closest Pair Problem](https://theory.stanford.edu/~valiant/papers/corrFull.pdf) · [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791) · [New Statistical and Computational Results for Learning Junta Distributions](https://arxiv.org/abs/2505.05819) · [The Benefits of Temporal Correlations: SGD Learns k-Juntas from Random Walks Efficiently](https://arxiv.org/abs/2605.10237) · [Inherited OpenReview research pointer; bibliographic identity not verified](https://openreview.net/pdf?id=wszZlP1K14)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5358 — Polynomial-time distribution-free PAC learning of DNF

A DNF is an OR of conjunctions of Boolean literals, representing a union of rule-defined regions. The question asks whether an unknown DNF with at most s terms can be learned from independent labelled examples under every input distribution in time polynomial in n, s, inverse error and log inverse failure probability. The learner may output any efficiently evaluable Boolean hypothesis but cannot request labels for inputs of its choice. Polynomially many samples suffice information-theoretically, while known hardness for unrestricted hypotheses relies on explicit complexity assumptions. A solution would settle a foundational computational-learning barrier and would also yield an efficient learner for uniform-example juntas.

[Read in atlas](index.html#TCS-5358) · [Learning DNF Expressions from Fourier Spectrum](https://proceedings.mlr.press/v23/feldman12b.html) · [The Probably Approximately Correct Learning Model in Computational Learning Theory](https://arxiv.org/abs/2511.08791) · [Complexity Theoretic Limitations on Learning DNF’s](https://proceedings.mlr.press/v49/daniely16.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6544 — Distribution-free learning of two margin halfspaces

The intersection of two halfspaces labels a point positively when both linear inequalities hold. This question asks whether such labels can be learned in polynomial time from independent examples under any distribution with a margin from both boundaries. The learner may output a different kind of hypothesis, provided that predictions remain efficient. The 2025 source proves efficient learning under an extra factorization assumption, while two 2026 preprints report broader bounds that do not by themselves meet this polynomial target. A resolution would determine whether two linear rules can be learned efficiently without favorable structure in the example distribution.

[Read in atlas](index.html#TCS-6544) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html) · [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700v2) · [Tight Bounds for Learning Polyhedra with a Margin](https://arxiv.org/abs/2604.14614v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7293 — Distribution-free improper learning of two unrestricted halfspaces

One threshold is efficiently learnable from labeled examples, but the target here combines two thresholds. Examples follow any fixed distribution on the Boolean cube and no positive margin is promised. The learner receives a bound on target description length and may output any efficiently evaluable classifier. Hardness for proper learners or growing numbers of halfspaces does not settle this two-halfspace target. The question asks for a uniform polynomial-time guarantee across all distributions and permitted target descriptions.

[Read in atlas](index.html#TCS-7293) · [The Intersection of Two Halfspaces Has High Threshold Degree](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf) · [Improved Hardness Results for Learning Intersections of Halfspaces](https://theoretics.episciences.org/18105) · [Learning Functions of Halfspaces](https://arxiv.org/abs/2603.08700v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-2336 — Optimal multiclass regret versus Littlestone dimension

An online learner predicts a label and then sees the correct label on each round. Regret compares its cumulative prediction loss with the best hypothesis in a known class. Littlestone dimension measures which labeled binary trees that class can realize. The target is the worst minimax regret among all classes of dimension at most d over T rounds, with no bound on the label-space size. Determining the full tradeoff would settle whether the familiar square-root dT scale needs an extra factor in the multiclass setting.

[Read in atlas](index.html#TCS-2336) · [Multiclass Online Learning and Uniform Convergence](https://proceedings.mlr.press/v195/hanneke23b.html)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3117 — Memory–sample tradeoffs for noisy parity learning

A hidden binary vector is observed through uniformly random parity equations with independent noise. Each equation is correct with probability one half plus \(\varepsilon\). The proposed lower bound requires either \(\Omega (n^{2}/\varepsilon ^{2})\) stored bits or exponentially many samples. The source proves the weaker \(\Omega (n^{2}/\varepsilon )\) memory threshold and gives a matching-to-the-conjecture space upper bound. The card fixes bounded-error exact recovery and requires constants uniform in \(\varepsilon\).

[Read in atlas](index.html#TCS-3117) · [Memory-Sample Lower Bounds for Learning Parity with Noise](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.60) · [Toward Lower Bounds on Memory-Sample Tradeoffs for Learning Parity with Noise](https://dimacs.rutgers.edu/reu-project-detail/toward-lower-bounds-on-memory-sample-tradeoffs-for)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0677 — Proper decision-tree learning in polynomial time

Proper learning of decision trees requires the learner to output a decision tree, preserving the target representation's simple branching structure. The source asks for a polynomial-time algorithm under the uniform input distribution with membership queries available. Those queries let the learner choose inputs and observe their target labels, making this different from learning from random examples alone. Existing algorithms in the source are faster than earlier quasipolynomial approaches but still fall short of polynomial time. A solution would provide an efficient way to recover an interpretable tree hypothesis without abandoning the tree representation during learning.

[Read in atlas](index.html#TCS-0677) · [Open Problem: Properly learning decision trees in polynomial time?](https://proceedings.mlr.press/v178/open-problem-blanc22a.html) · [Properly Learning Decision Trees with Queries Is NP-Hard](https://arxiv.org/abs/2307.04093) · [Fast Decision Tree Learning Solves Hard Coding-Theoretic Problems](https://arxiv.org/abs/2409.13096)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1573 — NP-hardness of improper learning of \(\mathrm{P}/\mathrm{poly}\)

The question asks whether SAT reduces to agnostic learning of general polynomial-size Boolean circuits. The learning oracle receives a circuit sampling labeled examples and returns an approximately optimal hypothesis. The returned hypothesis may use an arbitrarily larger fixed polynomial size than the comparator circuits. The reduction must work with every valid oracle reply and without additional cryptographic assumptions. A June 2026 follow-up gives related conditional hardness, leaving the unconditional target unresolved.

[Read in atlas](index.html#TCS-1573) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34) · [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3787 — Proper unlabeled compression of ample classes

An ample class strongly shatters every set of coordinates that it shatters. A compressor selects at most d input points from any realizable labeled sample, where d is the class’s VC dimension. A reconstructor must recover a concept in the original class consistent with all sample labels while receiving only the selected points. Maximum classes satisfy this exact bound, and labeled compression is known more generally. The 2024 oriented-matroid results still leave proper unlabeled size-d compression for all ample classes open.

[Read in atlas](index.html#TCS-3787) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.4230/LIPIcs.ICALP.2019.34) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.1016/j.jcss.2022.01.003) · [Unlabeled Sample Compression Schemes for Oriented Matroids](https://doi.org/10.1016/j.disc.2024.114006)
Existing status: `open` · Summary written: 2026-09-12

### TCS-3689 — Non-clashing teaching dimension versus VC dimension

A teacher assigns correctly labeled examples to each concept in a finite class. No two different concepts may both fit each other’s assigned examples. The conjecture asks whether at most d examples per concept always suffice when the VC dimension is d. A quadratic general bound and exact bounds for certain special classes are known. The sharp signed-example inequality remains distinct from positive-only teaching, computational map-finding and sample-compression questions.

[Read in atlas](index.html#TCS-3689) · [Optimal Collusion-Free Teaching](https://proceedings.mlr.press/v98/kirkpatrick19a.html) · [On Batch Teaching Without Collusion](https://www.jmlr.org/papers/v24/22-0330.html) · [Non-Clashing Teaching Maps for Balls in Graphs](https://proceedings.mlr.press/v247/chalopin24a.html)
Existing status: `open` · Summary written: 2026-09-12

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

### TCS-0689 — Property Elicitation and Elicitation Complexity

A statistical property is elicitable when minimizing an expected loss recovers that property of the underlying distribution. Familiar examples motivate asking which statistics admit such loss functions and how those functions can be characterized. The source also studies elicitation complexity, the number of intermediate real-valued reports needed to recover a desired statistic. Some properties that cannot be elicited directly may become accessible through a richer intermediate prediction. A general characterization would explain the expressive limits of empirical risk minimization and guide the design of objectives for estimating specific distributional quantities.

[Read in atlas](index.html#TCS-0689) · [COLT / PMLR](https://proceedings.mlr.press/v49/frongillo16.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3177 — Learning PH/poly from learning NP/poly

Learning complexity asks whether examples can be converted efficiently into predictors for an entire class of computational functions. The source considers the nonuniform classes NP/poly and PH/poly, which permit polynomial-size advice. It asks whether polynomial-time learnability of the first would imply polynomial-time learnability throughout the polynomial hierarchy. The analogy is with structural collapse theorems, but the learning setting introduces distributional and oracle issues. A proof or barrier would clarify whether learning a nondeterministic level is powerful enough to handle repeated alternations, rather than merely yielding faster algorithms for isolated concept classes.

[Read in atlas](index.html#TCS-3177) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3391 — Efficient learning of well-separated Gaussian mixtures

Learning a well-separated spherical Gaussian mixture requires estimating the component parameters from unlabeled samples. The source establishes favorable sample complexity and local convergence of expectation maximization once initialization is sufficiently good. It asks for an algorithm with both polynomial running time and polynomial sample complexity under the stated separation regime. Local refinement does not by itself supply an efficient global initialization procedure. Closing this gap would show whether enough statistical separation to identify the mixture also suffices for efficient end-to-end recovery, without quasipolynomial dependence on the number of components.

[Read in atlas](index.html#TCS-3391) · [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3691 — Uniform convergence under Dobrushin dependence

A dependent training sample has identical marginal distributions and a bounded total influence on every coordinate. Uniform convergence requires every hypothesis’s empirical zero-one loss to approximate its population loss. The card asks whether every finite-VC class has the usual square-root rate when the ordinary Dobrushin coefficient stays below one. The source already proves learnability under that condition, but its uniform-convergence theorem requires stronger logarithmic influences. The formulation makes the iid-order rate and fixed dependence slack explicit, without claiming an optimal constant near the boundary.

[Read in atlas](index.html#TCS-3691) · [Learning from Weakly Dependent Data under Dobrushin’s Condition](https://proceedings.mlr.press/v99/dagan19a.html) · [Learning from Weakly Dependent Data under Dobrushin’s Condition](https://arxiv.org/abs/1906.09247)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4186 — Learning speedups from random examples

The question asks whether a weak passive learner with a superpolynomial saving over \(2^{n}\) must imply dramatically faster passive learners. Targets range over standard polynomial-size circuit classes, and all examples are independent and uniform. The desired learners attain every fixed inverse-polynomial error in time \(2^{n^{\varepsilon}}\) for every fixed \(\varepsilon >0\). The source establishes this implication when learners may choose membership queries. A later generalized speedup still permits such queries in its conclusion, leaving the passive implication unestablished by that result.

[Read in atlas](index.html#TCS-4186) · [Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness](https://doi.org/10.4230/LIPIcs.CCC.2017.18) · [Conspiracies between Learning Algorithms, Circuit Lower Bounds and Pseudorandomness — full preprint](https://arxiv.org/abs/1611.01190) · [Learning algorithms from circuit lower bounds](https://doi.org/10.1007/s00037-024-00261-4)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4592 — Time complexity of Gaussian agnostic halfspace learning

Agnostic halfspace learning seeks a classifier whose error nearly matches the best linear threshold rule, even when labels do not follow any halfspace. This question fixes the unlabeled distribution to be Gaussian and asks for the optimal running time as dimension and target excess error vary. The source specifically proposes a running time whose exponent in the dimension grows only logarithmically with inverse error. It supports that target with a conditional lower bound derived from learning sparse parities with noise. Matching the proposed rate would identify a precise computational price for handling arbitrary label noise under a highly regular input distribution.

[Read in atlas](index.html#TCS-4592) · [Embedding Hard Learning Problems Into Gaussian Space](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.793)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4672 — Price of bandit information in multiclass learning

In multiclass online learning, full feedback reveals the correct label after each prediction, while bandit feedback only says whether the prediction was correct. Littlestone dimension and bandit Littlestone dimension quantify the corresponding worst-case mistake complexities in the source's realizable model. The price of bandit information is their ratio for the same hypothesis class. For a label set of size k, the question asks how large this ratio can be across classes and domains. A sharp bound would isolate the cost of withholding the correct label from the underlying difficulty of predicting the class itself.

[Read in atlas](index.html#TCS-4672) · [Multiclass Learnability and the ERM principle](https://proceedings.mlr.press/v19/daniely11a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4792 — Multiclass sample compression from binary compression

A sample compression scheme stores a small subset of labeled examples and enough permitted auxiliary information to reconstruct a hypothesis consistent with the full sample. This problem compares compression for binary classes with compression for classes whose labels may take many values. Assuming every binary class of VC-dimension d admits compression of size \(f(d)\), it asks whether graph dimension gives the corresponding multiclass bound up to a constant factor. The source establishes stronger reductions under additional assumptions on the binary reconstruction procedure, including proper or majority-vote reconstruction. Removing those assumptions would transfer binary compression advances to multiclass learning through a general structural reduction.

[Read in atlas](index.html#TCS-4792) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5031 — Littlestone-dimension regret bounds for unrestricted classes

Online classification compares a learner's errors with the best hypothesis in a concept class. The cited result gives optimal square-root regret in the product of horizon and Littlestone dimension under an additional regularity condition. The extracted question asks whether that characterization holds for completely unrestricted classes. The restriction matters because it supports a minimax argument for an associated game. Removing it would show that the combinatorial dimension alone determines regret, even where the usual interchange between randomized strategies and adversarial choices cannot simply be assumed.

[Read in atlas](index.html#TCS-5031) · [The Dimension of Self-Directed Learning](https://proceedings.mlr.press/v237/devulapalli24a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5061 — Computable PAC learning versus effective sample bounds

Computable PAC learning requires an actual algorithm producing hypotheses with the usual distribution-free statistical guarantee. Strong computable PAC learning additionally requires a computable bound on the sample size needed for a requested accuracy and confidence. The source asks whether a hypothesis class can admit a proper computable PAC learner while admitting no proper learner with such an effective sample bound. Any separating class would force the necessary sample-complexity behavior beyond computable upper bounds in the sense developed there. The question tests whether effective prediction and effective knowledge of when prediction becomes reliable are distinct requirements.

[Read in atlas](index.html#TCS-5061) · [On characterizations of learnability with computable learners](https://proceedings.mlr.press/v178/sterkenburg22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5087 — Polynomial-time robust spectral estimation

Adversarially robust dimension reduction seeks a low-rank projection that both approximates a dataset and limits the effect of small perturbations to individual data points. Here even the training matrix is corrupted, so the approximation must be good for an unknown original matrix rather than merely the observed one. The source gives stronger recovery guarantees in Frobenius norm, while its efficient spectral-norm method may instead certify substantial poisoning. It asks for a polynomial-time estimator achieving the stronger spectral guarantee already available information theoretically. The difficulty is that many small coordinate changes can accumulate into a large matrix perturbation and obscure which subspace represents the clean data.

[Read in atlas](index.html#TCS-5087) · [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5088 — Learning halfspace intersections under factorizable distributions

An intersection of k halfspaces labels a point positively only when it satisfies all k linear inequalities. Even under a Gaussian input distribution or the uniform distribution on the Boolean cube, the source identifies a gap between learning algorithms and fully polynomial efficiency. The question asks whether the dependence on dimension, number of halfspaces, and inverse accuracy can all be polynomial under these distributional assumptions. The surrounding paper studies a restricted two-halfspace setting with margin and factorization assumptions, which illustrates how additional structure can help. Resolving the broader question would clarify whether simple input distributions make learning a growing conjunction of thresholds computationally feasible.

[Read in atlas](index.html#TCS-5088) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5090 — One-way functions from hardness of learning P/poly

The class P/poly consists of Boolean functions computable by polynomial-size circuits, and learning it would cover a broad range of efficiently represented prediction rules. This question asks whether worst-case hardness of efficient learning from random labeled examples already implies the existence of one-way functions. One-way functions require average-case resistance to inversion, making this a proposed bridge from learning hardness to a basic cryptographic assumption. The source obtains structural equivalences for stronger concept classes such as PSPACE/poly and EXP/poly, but does not extend this implication to P/poly. A resolution would explain whether difficult circuit learning necessarily contains the kind of average-case hardness needed for cryptography.

[Read in atlas](index.html#TCS-5090) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5119 — Sample-optimal Gaussian graphical model learning in polynomial time

A Gaussian graphical model encodes conditional dependencies through the nonzero entries of the inverse covariance matrix. The motivating question asks whether its underlying sparse graph can be recovered with the information-theoretically optimal sample count by a polynomial-time algorithm. The source's DICE procedure settles the sample-complexity component using only graph size, maximum degree, and minimum normalized edge strength in its bound. Its search cost still has an exponent depending on the degree, so the paper separately asks for computationally efficient sample-optimal recovery in general. This record therefore combines a statistical question answered in the source with a remaining algorithmic efficiency direction.

[Read in atlas](index.html#TCS-5119) · [Information Theoretic Optimal Learning of Gaussian Graphical Models](https://proceedings.mlr.press/v125/misra20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5153 — Characterizing adversarially robust PAC learnability

Adversarially robust PAC learning seeks a predictor that remains correct under every permitted test-time perturbation of a fresh example. The perturbation rule and the hypothesis class together determine this task, even though the training observations themselves are independent and uncorrupted. The source proves that finite VC-dimension suffices with improper learning and that a robust shattering dimension supplies a necessary condition. Neither observation yields the requested exact characterization, since ordinary VC-dimension need not be necessary and the sufficiency of the robust quantity is unresolved there. The question is to identify a complexity measure that precisely captures robust learnability and supports corresponding sample bounds.

[Read in atlas](index.html#TCS-5153) · [VC Classes are Adversarially Robustly Learnable, but Only Improperly](https://proceedings.mlr.press/v99/montasser19a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5434 — Nontrivial agnostic membership-query learning of \(\mathrm{ACC}^{0}\)

Agnostic membership-query learning must approximate an arbitrary target nearly as well as the best hypothesis in a specified circuit class. The source asks for a nontrivial learning-time saving for ACC0 circuits, even under uniformly distributed inputs. Membership queries allow the learner to choose labeled examples. The target must tolerate noise or mismatch between the target and the hypothesis class. The project seeks algorithmic progress beyond exhaustive truth-table processing while preserving a guarantee relative to the best available constant-depth modular circuit.

[Read in atlas](index.html#TCS-5434) · [Agnostic Membership Query Learning with Nontrivial Savings: New Results and Techniques](https://proceedings.mlr.press/v237/karchmer24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5847 — Linear conditional-information bounds for VC learning

The source studies how much information a learning algorithm reveals while learning a class of VC dimension d. Its conjecture seeks a learner with conditional mutual information bounded by \(O(d)\). The desired bound would make information usage depend linearly on the class's combinatorial capacity rather than on additional sample-related factors. This connects statistical learnability with a precise notion of how strongly the output depends on the training data. The excerpt ends before the learner's accuracy and sample guarantees, so those conditions must be recovered before an information bound can be interpreted as a full learning result.

[Read in atlas](index.html#TCS-5847) · [Open Problem: Information Complexity of VC Learning](https://proceedings.mlr.press/v125/steinke20b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5902 — PAC learning of finite automata under the uniform distribution

Learning a deterministic finite automaton from examples means producing a hypothesis that predicts its acceptance behavior. The cited question asks whether this can be done efficiently in the probably approximately correct framework under the specified uniform distribution. The learner should achieve low error with high confidence from randomly sampled labeled words. Results allowing membership and equivalence queries provide stronger information and therefore do not settle this sampling-only target. An answer would clarify whether a simple data distribution removes the computational obstacles to learning arbitrary finite-state languages.

[Read in atlas](index.html#TCS-5902) · [Approximate Learning of Limit-Average Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2019.17)
Existing status: `uncertain` · Summary written: 2026-09-11

## Cryptography (29)

### TCS-6545 — Public-key encryption from one-way functions

A one-way function is easy to evaluate and difficult for efficient classical algorithms to invert on a random input. Public-key encryption requires that anyone can encrypt with public information while a receiver can decrypt with a related secret key. The question asks whether the existence of any one-way function implies such a uniform classical scheme, allowing arbitrary non-black-box constructions. The scheme must have negligible average decryption error and hide an encrypted bit from every efficient chosen-plaintext observer. Oracle barriers do not settle the unrestricted implication, and a 2023 preprint claiming a positive solution remains unverified in this review.

[Read in atlas](index.html#TCS-6545) · [Foundations of Cryptography, Lecture 10](https://mit6875.github.io/FA23SLIDES/lec10.pdf) · [The Complexity of Public-Key Cryptography](https://eccc.weizmann.ac.il/report/2017/065/) · [Limits on the Provable Consequences of One-Way Permutations](https://www.cs.cmu.edu/~rudich/papers/oneway.ps) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [Merkle Puzzles are Optimal — an \(O(n^{2})\)-query attack on key exchange from a random oracle](https://www.boazbarak.org/Papers/merkle.pdf) · [Public-Key Encryption from the MinRank Problem](https://link.springer.com/chapter/10.1007/978-3-032-25327-9_16) · [Public-Key Encryption from Average Hard NP Language](https://eprint.iacr.org/2023/1260)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-0022 — One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)

The statement \(\mathrm{P} \ne  \mathrm{NP}\) guarantees that some efficiently verifiable problems cannot be solved efficiently on every input. Cryptographic one-way functions require a stronger kind of difficulty: efficient attackers must fail to invert outputs generated from random inputs. This project asks whether worst-case hardness alone forces that average-case cryptographic hardness to exist. A function that is hard only on an extremely rare set would not provide the required security. Resolving the implication would clarify whether the most familiar complexity assumption already contains the foundations of computational cryptography.

[Read in atlas](index.html#TCS-0022) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf) · [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6550 — Circuit obfuscation from polynomial-hard LWE

Indistinguishability obfuscation transforms equivalent programs so that an efficient observer cannot tell which implementation was supplied. This project asks whether ordinary polynomial-hard learning with errors is enough to construct obfuscation for all polynomial-size Boolean circuits. The question excludes extra assumptions about circular security, leakage resilience, or stronger hardness regimes. Its security notion compares programs with identical behavior rather than promising that arbitrary code reveals no information beyond black-box access. A construction under the stated LWE assumption would give this powerful primitive a substantially more economical foundation.

[Read in atlas](index.html#TCS-6550) · [On the \((Im)\)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007) · [Indistinguishability Obfuscation from LPN over \(F_{p}\), DLIN, and PRGs in \(\mathrm{NC}^{0}\)](https://eprint.iacr.org/2021/1334) · [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28)
Existing status: `source_open` · Summary written: 2026-09-11

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

Oblivious transfer lets a receiver obtain one of two secret messages while hiding which message it chose. At the same time, the receiver must remain unable to learn the unchosen message. This project asks whether ordinary public-key encryption alone is enough to construct such a protocol in the classical plain model. The specified target already restricts corruption to semi-honest parties, yet privacy must hold on both sides. A general implication would connect basic encryption to a central primitive for secure computation without assuming extra algebraic structure or setup.

[Read in atlas](index.html#TCS-6549) · [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf) · [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf) · [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882) · [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002) · [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://doi.org/10.1587/transfun.2025CIP0019)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6547 — Collision-resistant hashing from one-way functions

Collision-resistant hashing compresses a message while making it difficult to find two different messages with the same hash value. The selected problem asks whether the existence of one-way functions alone guarantees a publicly keyed family with this security property. Collisions necessarily exist because the output space is smaller, so the issue is computational difficulty after the hash key is revealed. Inverting a random function output and deliberately constructing a colliding pair are different challenges. Resolving their relationship would identify whether collision resistance is an additional cryptographic assumption or a consequence of basic one-wayness.

[Read in atlas](index.html#TCS-6547) · [One-Way Functions are Necessary and Sufficient for Secure Signatures](https://www.cs.princeton.edu/courses/archive/spr08/cos598D/Rompel.pdf) · [Finding collisions on a one-way street: Can secure hash functions be based on general assumptions?](https://link.springer.com/chapter/10.1007/BFb0054137) · [Cryptographic Hashing From Strong One-Way Functions: Or: One-Way Product Functions and their Applications](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f850.pdf) · [One-Way Functions vs. TFNP: Simpler and Improved](https://eprint.iacr.org/2023/945) · [Doubly-Efficient Interactive Arguments for Bounded-Space from One-Way Functions](https://eccc.weizmann.ac.il/report/2026/111/)
Existing status: `source_open` · Summary written: 2026-09-11

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

## Quantum computation and information (54)

### TCS-6446 — Quantum PCP conjecture with classical reductions

A local Hamiltonian describes a quantum system through bounded-strength interactions on a fixed number of qubits at a time. The question asks whether distinguishing two constant-separated ranges of its average ground energy is as hard as every problem with a quantum witness verifier. The saved variant requires deterministic classical reductions, a stronger requirement than the original survey’s formulation allowing quantum reductions. All global quantum states are allowed, and neither growing locality nor a vanishing normalized gap meets the target. Known low-energy state complexity, interactive verification and restricted gap-amplification results leave the stated hardness question unresolved in the checked sources.

[Read in atlas](index.html#TCS-6446) · [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495v1) · [NLTS Hamiltonians from good quantum codes](https://arxiv.org/abs/2206.13228v4) · [The status of the quantum PCP conjecture (games version)](https://arxiv.org/abs/2403.13084v1) · [Quantum PCPs: on Adaptivity, Multiple Provers and Reductions to Local Hamiltonians](https://arxiv.org/abs/2403.04841v3) · [Derandomised tensor product gap amplification for quantum Hamiltonians](https://arxiv.org/abs/2510.01333v1) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588v1) · [Gap Amplification for Local Hamiltonians with Combinatorial Soundness](https://simons.berkeley.edu/talks/quynh-t-nguyen-harvard-university-2026-07-23) · [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0036 — BPP versus BQP

This problem asks whether efficient quantum computation can decide something that efficient randomized classical computation cannot. BPP and BQP both require a reliable yes-or-no answer on every input, with bounded probability of error. Quantum interference gives promising candidate advantages, including the algorithms underlying factoring, but those examples do not establish an unconditional classical lower bound. Separations using special oracles or restricted classical circuits concern narrower comparisons. Settling the ordinary class separation would identify whether quantum computers enlarge the set of efficiently decidable problems at its most basic level.

[Read in atlas](index.html#TCS-0036) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027v2) · [Oracle Separation of BQP and PH](https://doi.org/10.1145/3530258) · [Unconditional Quantum Advantage for Sampling with Shallow Circuits](https://quantum-journal.org/papers/q-2026-08-12-2188/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6516 — Area law for gapped two-dimensional Hamiltonians

An area law says that entanglement between a region and its surroundings grows with the region's boundary rather than its volume. This problem asks for such a bound for the unique ground state of a general two-dimensional local Hamiltonian with a fixed positive spectral gap. Interaction strength, local dimension, and interaction range are held fixed as the lattice grows. Known routes involving frustration-free systems or additional conditions do not automatically establish the unrestricted statement recorded here. A solution would clarify how strongly locality and an energy gap constrain many-body quantum states, without by itself supplying an efficient algorithm to find them.

[Read in atlas](index.html#TCS-6516) · [An Area Law for One Dimensional Quantum Systems](https://arxiv.org/abs/0705.2024v4) · [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492v3) · [Entanglement spread area law in gapped ground states](https://doi.org/10.1038/s41567-022-01740-7) · [Area Laws and Tensor Networks for Maximally Mixed Ground States](https://doi.org/10.1007/s00220-026-05554-z) · [Quantum matter is weakly entangled at low energies](https://arxiv.org/abs/2604.14143v1) · [Two-dimensional local Hamiltonian problem with area laws is QMA-complete](https://doi.org/10.1016/j.jcp.2021.110534)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6580 — Information-theoretic classical verification of quantum computation

A classical user would like to check a computation performed by a single quantum device using only classical messages. The honest device must be able to carry out the verification protocol in quantum polynomial time. The difficult requirement is soundness against any cheating device, including a computationally unbounded one. Existing approaches may instead give the user limited quantum capabilities, use separated devices, or assume that a cryptographic problem is hard. The question isolates whether an entirely classical client can obtain unconditional trust in efficient quantum computation under this single-device model.

[Read in atlas](index.html#TCS-6580) · [Verification of quantum computation: An overview of existing approaches](https://arxiv.org/abs/1709.06984) · [\(\mathrm{IP} = \mathrm{PSPACE}\)](https://doi.org/10.1145/146585.146609) · [Interactive Proofs for Quantum Computations](https://arxiv.org/abs/1704.04487) · [A classical leash for a quantum system: Command of quantum systems via rigidity of CHSH games](https://arxiv.org/abs/1209.0448) · [Classical Verification of Quantum Computations](https://arxiv.org/abs/1804.01082) · [How to Classically Verify a Quantum Cat without Killing It](https://arxiv.org/abs/2602.09282) · [Verification of Quantum Computations Without Trusted Preparations or Measurements](https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202501018) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6518 — NPT bound entanglement

Entangled states can sometimes be converted into nearly perfect shared Bell pairs using many copies and local operations with classical communication. Bound entanglement means that this distillation remains impossible despite the presence of entanglement. The question asks whether such states can have a negative partial transpose, a spectral property associated with distillability in simpler settings. Failure of a protocol on one copy or any fixed number of copies does not establish the required obstruction for every number of copies. Resolving the question would sharpen the distinction between entanglement as a property and entanglement as a usable communication resource.

[Read in atlas](index.html#TCS-6518) · [Mixed-state entanglement and distillation: is there a “bound” entanglement in nature?](https://arxiv.org/abs/quant-ph/9801069) · [Evidence for Bound Entangled States with Negative Partial Transpose](https://arxiv.org/abs/quant-ph/9910026) · [A solution to 2-copy distillability of Werner states](https://arxiv.org/abs/2607.21367) · [On the two-copy distillability of Werner states and a new partial trace inequality](https://arxiv.org/abs/2607.24309) · [Two-copy nondistillability of Werner states: sharp partial-trace inequalities and finite-copy extensions](https://arxiv.org/abs/2607.24479) · [Sharp Plucker Geometry for Three-Copy Werner Distillation](https://arxiv.org/abs/2608.02647)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6515 — Asymptotically good quantum locally testable stabilizer codes

A locally testable quantum code should reveal a substantial error by checking only a few qubits. The desired family must also encode a linear amount of quantum information and tolerate errors on a linear number of physical qubits. Each check and each qubit's participation in checks must remain bounded as the code grows. These requirements strengthen ordinary good quantum LDPC codes by demanding a quantitative relation between distance from the code space and rejection probability. Such codes would connect robust quantum error detection with the complexity of low-energy states and the broader search for quantum PCP constructions.

[Read in atlas](index.html#TCS-6515) · [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/) · [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654) · [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8) · [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476) · [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228) · [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6517 — Passive quantum memory in three dimensions

Passive quantum memory aims to preserve an encoded qubit through the natural dynamics of a material without repeated active correction. The question here fixes a nonzero temperature and asks whether lifetime can grow without bound in a three-dimensional local stabilizer system. Protecting a qubit requires retaining phase information as well as distinguishing its classical basis states. The saved card records a May 2026 claimed affirmative construction, while distinguishing its proof claim from an independently verified conclusion. This makes the record a useful guide to the precise thermal model and remaining verification questions rather than an unqualified assertion that the original existence problem is still open.

[Read in atlas](index.html#TCS-6517) · [Thermodynamic stability criteria for a quantum memory based on stabilizer and subsystem codes](https://arxiv.org/abs/0907.2807) · [Quantum memories at finite temperature](https://arxiv.org/abs/1411.6643) · [Symmetry protected self correcting quantum memory in three space dimensions](https://arxiv.org/abs/2103.08622) · [Cored product codes for quantum self-correction in three dimensions](https://arxiv.org/abs/2510.05479) · [A passive self-correcting quantum memory in three dimensions](https://arxiv.org/abs/2605.10943) · [Partial Self-Correction in Layer Codes](https://journals.aps.org/prl/abstract/10.1103/mb89-8436)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6519 — Quantum capacity of the qubit depolarizing channel

A depolarizing channel models a qubit subjected to randomly chosen Pauli errors. Its quantum capacity measures how much unknown quantum information can be transmitted reliably per channel use when many uses are encoded together. The goal is the capacity curve throughout the noise range under the unassisted coding convention fixed in the card. Coding across several uses can behave differently from optimizing a single use, which complicates attempts to match achievable rates with impossibility bounds. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-6519) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Quantum cloning and the capacity of the Pauli channel](https://arxiv.org/abs/quant-ph/9803058) · [Quantum and private capacities of low-noise channels](https://arxiv.org/abs/1705.04335) · [Geometric optimization for quantum communication](https://arxiv.org/abs/2509.15106) · [Enhanced quantum capacity thresholds from symmetry](https://arxiv.org/abs/2605.09138) · [A certified lower bound on the quantum-capacity threshold of the depolarizing channel](https://arxiv.org/abs/2608.15870) · [Sharp Quantum Capacity Thresholds: Exponential Strong Converses for Degradable and Antidegradable Channels](https://arxiv.org/abs/2608.01308)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0037 — NP outside BQP

This problem asks whether quantum computers still face an unavoidable efficient-computation barrier on some NP problems. An equivalent target is to rule out a bounded-error polynomial-time quantum algorithm for every instance of Boolean satisfiability. Fast quantum algorithms for structured tasks do not imply an algorithm for general NP-complete search or decision problems. Likewise, a speedup for searching an unstructured list addresses a particular access model rather than the full complexity-class question. A resolution would delimit the reach of quantum computation on problems whose proposed solutions are easy to check classically.

[Read in atlas](index.html#TCS-0037) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027) · [A fast quantum mechanical algorithm for database search](https://arxiv.org/abs/quant-ph/9605043) · [Strengths and Weaknesses of Quantum Computing](https://arxiv.org/abs/quant-ph/9701001) · [Complexity of detecting large coefficients in the Pauli basis](https://arxiv.org/abs/2606.19545)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6448 — QMA versus QCMA

A quantum verifier may receive either a quantum state or a classical string as evidence that an input is a yes-instance. QMA permits the former kind of witness, while QCMA restricts the witness to classical information. The question asks whether this change in the form of the evidence changes what can be verified efficiently. Both models already allow quantum computation during verification, so the issue is the additional power of the witness itself. An answer would clarify whether quantum states can serve as fundamentally stronger proofs in the ordinary setting without an oracle.

[Read in atlas](index.html#TCS-6448) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6520 — Computability of quantum channel capacity

Quantum channel capacity describes the best asymptotic rate for transmitting quantum information through a noisy channel. This problem asks whether that number can always be approximated by an algorithm from an effective finite description of the channel. The algorithm may be slow, but it must halt and meet any requested rational accuracy. Optimizations involving arbitrarily many channel uses make the asymptotic definition harder to turn into a guaranteed finite computation. Establishing computability or an obstruction would separate the existence of an operational communication rate from our ability to calculate it even in principle.

[Read in atlas](index.html#TCS-6520) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Continuity of quantum channel capacities](https://arxiv.org/abs/0810.4931) · [Unbounded number of channel uses may be required to detect quantum capacity](https://www.nature.com/articles/ncomms7739) · [Undecidability in Physics: a Review](https://arxiv.org/abs/2410.16532) · [Undecidability in physics: A review — journal version](https://doi.org/10.1016/j.physrep.2025.06.004) · [On the undecidability of quantum channel capacities](https://arxiv.org/abs/2601.22471)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6521 — Dihedral hidden subgroup problem in BQP

The dihedral hidden subgroup problem presents a function that is constant on cosets of an unknown subgroup of a dihedral group. The task is to recover generators for that subgroup using quantum access to the function. The target is a uniform algorithm whose total running time is polynomial in the length of the group description and oracle values. Counting only a small number of oracle queries is insufficient if processing the resulting quantum information is expensive. An efficient solution would extend the reach of hidden-subgroup methods beyond the abelian setting and illuminate connections with lattice-related algorithmic problems.

[Read in atlas](index.html#TCS-6521) · [Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333) · [A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345) · [The dihedral hidden subgroup problem](https://arxiv.org/abs/2106.09907) · [A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with Polynomial Space](https://arxiv.org/abs/quant-ph/0406151) · [Quantum Computation and Lattice Problems](https://cims.nyu.edu/~regev/papers/quantum_average.pdf) · [A Quantum Polynomial-Time Solution to The Dihedral Hidden Subgroup Problem](https://arxiv.org/abs/2202.09697) · [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591) · [The ePrint:\(2026/1591\) Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693) · [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598) · [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6522 — Graph isomorphism in BQP

Two graphs are isomorphic when a relabeling of vertices preserves every edge. This question asks whether a quantum algorithm can decide that equivalence in polynomial time for every pair of explicitly given graphs. The algorithm must include all processing costs and achieve bounded error, rather than merely extract a small amount of information from an oracle. Symmetry makes graph isomorphism a natural testing ground for quantum methods, but quantum access to related group structure is not itself a complete algorithm. A resolution would clarify whether quantum computation can efficiently handle this central classification problem.

[Read in atlas](index.html#TCS-6522) · [Ten Semi-Grand Challenges for Quantum Computing Theory](https://www.scottaaronson.com/writings/qchallenge.html) · [A Quantum-Inspired Algorithm for Graph Isomorphism](https://arxiv.org/abs/2512.24423) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/update.html) · [Limitations of Quantum Coset States for Graph Isomorphism](https://arxiv.org/abs/quant-ph/0511148) · [Quantum state isomorphism problems for groups](https://arxiv.org/abs/2605.12615) · [NPA Hierarchy for Quantum Isomorphism and Homomorphism Indistinguishability](https://quantum-journal.org/papers/q-2026-01-28-1989/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0029 — Maximum randomized-versus-quantum gap for total functions

The question asks for the largest polynomial quantum query advantage over randomized algorithms on total Boolean functions. Both models must answer correctly with probability at least two thirds on every input. Only queries to input bits are counted, with other computation and workspace unrestricted. Known results put the optimal separation exponent between three and four. The target is to certify that exponent within one hundredth, without resolving finer logarithmic factors.

[Read in atlas](index.html#TCS-0029) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem](https://arxiv.org/abs/2010.12629) · [k-Forrelation Optimally Separates Quantum and Classical Query Complexity](https://arxiv.org/abs/2008.07003)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6449 — Quantum versus classical nonuniform advice

Advice is information supplied in advance that depends on input length but must work for every input of that length. A quantum algorithm might receive a polynomial-size quantum advice state or only a polynomial-length classical string. The question is whether quantum advice allows it to decide more languages efficiently than classical advice does. Advice is nonuniform and need not be efficiently generated, so the comparison concerns its information content rather than its preparation cost. A separation or simulation would reveal how much computational value can be carried by a reusable description of a length-specific quantum state.

[Read in atlas](index.html#TCS-6449) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/)
Existing status: `source_open` · Summary written: 2026-09-11

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

[Read in atlas](index.html#TCS-6447) · [Quantum Interactive Oracle Proofs](https://arxiv.org/abs/2601.12874)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-0860 — Complexity of Quantum Approximate Counting

Quantum approximate counting asks about the dimension of an accepting subspace of a quantum verifier. In the saved formulation, one counts eigenvectors of the acceptance operator whose eigenvalues are at least two thirds. The decision task distinguishes a dimension at least a threshold from one at most half that threshold, under the stated promise. The source asks for sharper upper or lower complexity bounds and for the behavior of the complementary problem. This would extend our understanding of witness counting from classical certificates to families of quantum states.

[Read in atlas](index.html#TCS-0860) · [TCS Open Problems](https://tcsopenproblems.com/problem/12)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-1961 — One-way state generators versus EFI pairs

One-way state generators produce quantum states whose generating secrets are hard to recover. EFI pairs and pseudorandom state generators express related forms of quantum indistinguishability. This question asks whether these search-type and decision-type cryptographic resources can be constructed from one another. The classical analogy between one-way functions and pseudorandom generators motivates the comparison, but quantum outputs introduce separate issues of verification and access to copies. Establishing equivalences or separations would organize the basic assumptions needed for computational quantum cryptography.

[Read in atlas](index.html#TCS-1961) · [One-Wayness in Quantum Cryptography](https://doi.org/10.4230/LIPIcs.TQC.2024.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2229 — QMA versus \(\mathrm{QMA}(2)\)

QMA uses a single quantum witness, while \(\mathrm{QMA}(2)\) permits two witnesses that must be unentangled across a specified division. This question asks how much verification power that unentanglement promise adds. The cited work studies proofs with restricted relative phases and finds that nearby models can have very different complexity. Those results do not directly establish equality or separation for ordinary QMA and \(\mathrm{QMA}(2)\). Understanding the relationship would isolate whether independently supplied quantum proofs provide an advantage unavailable to one unrestricted quantum certificate.

[Read in atlas](index.html#TCS-2229) · [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2408 — Remote state preparation from quantum-secure one-way functions

Remote state preparation lets a classical party induce useful quantum states at another device through an interactive protocol. The cited construction obtains this functionality from a Learning With Errors assumption and uses it to replace quantum communication in cryptographic protocols. This question asks whether quantum-secure one-way functions alone could support a sufficiently strong version of the same primitive. The source explains that such a construction would have further consequences for secure two-party computation with classical communication. The goal is to identify the minimum cryptographic assumptions behind remote preparation, including a possible impossibility result for the proposed weakening.

[Read in atlas](index.html#TCS-2408) · [Quantum Cryptography with Classical Communication: Parallel Remote State Preparation for Copy-Protection, Verification, and More](https://doi.org/10.4230/LIPIcs.ICALP.2023.67)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2707 — Quantum partition functions from zero-freeness

A quantum partition function aggregates contributions from a Hamiltonian describing the system's interactions. The source asks for a polynomial-time approximation algorithm assuming only the relevant zero-freeness condition. Zero-freeness supports analytic approximation methods, but quantum interaction terms need not commute with one another. Extending the guarantee to this setting would clarify how far analytic information alone can support efficient partition-function computation. The saved passage explicitly identifies noncommutativity as the obstacle, while leaving the precise zero-free region and Hamiltonian access assumptions to the cited paper.

[Read in atlas](index.html#TCS-2707) · [Polynomial-Time Approximation of Zero-Free Partition Functions](https://doi.org/10.4230/LIPIcs.ICALP.2022.108)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3275 — Completeness and soundness amplification in StoqMA

A StoqMA verifier uses classical reversible gates, special initial ancillas and one final measurement in the plus/minus basis. It accepts a suitable nonnegative quantum witness on yes instances and must reject arbitrary witnesses with the prescribed soundness bound on no instances. The question asks whether every inverse-polynomial gap can be amplified to completeness exponentially close to one and soundness exponentially close to one half. Soundness-only repetition is known, but it does not provide this simultaneous improvement. A published theorem makes full error reduction equivalent to StoqMA=MA, and July 2026 work still states the general problem as open.

[Read in atlas](index.html#TCS-3275) · [StoqMA Meets Distribution Testing](https://doi.org/10.4230/LIPIcs.TQC.2021.4) · [StoqMA vs. MA: the power of error reduction](https://doi.org/10.22331/q-2025-09-11-1853) · [The power of unentanglement without destructive interference](https://arxiv.org/abs/2604.27886) · [The Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems](https://arxiv.org/abs/2605.16249)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3709 — Lifting quantum query complexity to communication

A lifting theorem transfers a lower bound for querying one input into a lower bound for communication between parties holding separate inputs. The transfer usually composes the original function with a small communication gadget. This question asks for such theorems for bounded-error and zero-error quantum query complexity. Simulating a query algorithm by communication is often straightforward, but proving that every communication protocol pays the corresponding cost is much harder. A quantum lifting theorem would let techniques for black-box algorithms establish communication lower bounds for a much wider family of problems.

[Read in atlas](index.html#TCS-3709) · [Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.TQC.2019.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4457 — Simulation or postselection universality for algebraic two-qubit interactions

A fixed two-qubit interaction generates circuits by evolving selected ordered pairs for specified times. Every circuit begins in a computational-basis state and ends with computational-basis measurement. The chosen dichotomy asks for efficient classical approximate sampling or full PP decision power with postselection. The variant makes all matrix constants, time encodings, sampling accuracy and conditioning probabilities explicit. Commuting-interaction results and analog Hamiltonian simulations do not by themselves classify this unrestricted circuit model.

[Read in atlas](index.html#TCS-4457) · [Complexity Classification of Two-Qubit Commuting Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2016.28) · [The Space Around BQP](https://dspace.mit.edu/server/api/core/bitstreams/ad343002-e1d8-4966-96ac-7d32b3b215d4/content) · [General Conditions for Universality of Quantum Hamiltonians](https://doi.org/10.1103/PRXQuantum.3.010308)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4615 — Quantum entropy inequalities beyond strong subadditivity

For a multipartite quantum state, the entropies of all subsystems form a vector subject to universal inequalities. Positivity and strong subadditivity give basic constraints on those vectors. This question asks whether additional inequalities are needed to describe the quantum entropy cone for four or more parties. The cited stabilizer-state analysis relates the problem to classical non-Shannon inequalities and to states violating the Ingleton inequality. New constraints or counterexamples would sharpen the mathematical description of how quantum information can be shared among several systems.

[Read in atlas](index.html#TCS-4615) · [The Quantum Entropy Cone of Stabiliser States](https://doi.org/10.4230/LIPIcs.TQC.2013.270)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4734 — Locality-preserving quantum gap amplification

Gap amplification increases the separation between satisfiable and unsatisfiable instances in a verification problem. The cited quantum construction can amplify a Hamiltonian promise gap repeatedly, but its terms act on progressively more qubits. This growing locality obstructs the composition steps used in the classical PCP strategy. The question asks for a quantum analogue that retains the important structural features of Dinur's classical amplification procedure. Such an operation would address a concrete missing ingredient in efforts to make quantum proofs locally checkable with a constant gap.

[Read in atlas](index.html#TCS-4734) · [Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2026.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4737 — QMA versus \(\mathrm{QMA}_{1}\)

A perfectly complete quantum proof system accepts some valid witness with probability exactly one. This question asks whether every QMA proof system can achieve that guarantee without sacrificing efficient verification or soundness. Approximate gate synthesis creates a special difficulty because a tiny implementation error can destroy exact acceptance. The cited work therefore keeps the verifier's gate set explicit and studies the structure needed for QMA1. A solution would explain whether perfect reliability on yes-instances is merely a choice of protocol or an additional restriction on quantum proofs.

[Read in atlas](index.html#TCS-4737) · [Towards a Universal Gateset for QMA1](https://doi.org/10.4230/LIPIcs.MFCS.2026.98)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4753 — \(\mathrm{QMA}(2)\) versus NEXP

Two unentangled quantum proofs can impose structure that a single unrestricted witness does not provide. This record asks whether the resulting class \(\mathrm{QMA}(2)\) has the full power of nondeterministic exponential time. The source reviews protocols compressing satisfiability witnesses and amplification techniques that exploit product-state testing. Those achievements do not by themselves establish the proposed equality with NEXP. Determining the class would reveal how much complexity can be hidden in a promise that independently supplied quantum messages share no entanglement.

[Read in atlas](index.html#TCS-4753) · [Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement](https://doi.org/10.4230/LIPIcs.ITCS.2023.53)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4789 — Collapse of the quantum-classical polynomial hierarchy

The quantum-classical polynomial hierarchy alternates classical witnesses while retaining quantum verification. In the classical hierarchy, equality of suitable neighboring levels produces a collapse of all higher levels. This question asks whether equality of the second existential and universal levels has the analogous consequence here. Promise gaps in quantum verification make the usual quantifier manipulations more delicate. A collapse theorem or obstruction would determine whether this hierarchy shares the structural rigidity of its classical counterpart.

[Read in atlas](index.html#TCS-4789) · [Quantum Generalizations of the Polynomial Hierarchy with Applications to \(\mathrm{QMA}(2)\)](https://doi.org/10.4230/LIPIcs.MFCS.2018.58)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4811 — Dihedral coset problem versus Subset Sum

The dihedral coset problem is a quantum problem closely connected to hidden subgroup algorithms and certain lattice problems. This project asks how tightly its computational difficulty is related to subset sum, including which densities of subset-sum instances are relevant. A measurement that extracts information optimally need not be efficiently implementable, and its implementation leads to a quantum subset-sum sampling task. The cited reductions connect different density regimes and sometimes pass through unique shortest-vector problems. A sharper equivalence would clarify whether progress on subset sum can actually yield efficient dihedral algorithms, rather than only information-theoretically good measurements.

[Read in atlas](index.html#TCS-4811) · [How Hard Is Deciding Trivial Versus Nontrivial in the Dihedral Coset Problem?](https://doi.org/10.4230/LIPIcs.TQC.2016.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4835 — Characterizing nonunitary quantum space

Quantum space complexity asks what computations can be performed with a limited quantum workspace. The cited paper characterizes unitary quantum space and relates quantum verification with exponentially small completeness–soundness gaps to classical space complexity. Its closing questions ask what analogous characterizations hold when intermediate nonunitary operations are allowed. Another direction is to understand quantum interactive proofs with exponentially small gaps, between better-understood precision regimes. Progress would connect resource-bounded quantum computation to concrete matrix problems and clarify how measurement, interaction, and precision change its power.

[Read in atlas](index.html#TCS-4835) · [A Complete Characterization of Unitary Quantum Space](https://doi.org/10.4230/LIPIcs.ITCS.2018.4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4894 — Parity versus \(\mathrm{AC}^{0}\) with shallow quantum preprocessing

Parity is a basic function that small constant-depth classical circuits cannot approximate well on uniformly random inputs. This project asks whether a shallow quantum preprocessing stage can remove that limitation when its measured output is passed to a classical AC0 circuit. The conjecture concerns constant-depth quantum circuits with bounded-fan-in gates, followed by the specified classical postprocessing. Any approximation guarantee must account for both the random input and the randomness of quantum measurement. Establishing the conjecture would place a concrete limit on hybrid computation and help clarify the power of weak classical procedures that use shallow quantum devices.

[Read in atlas](index.html#TCS-4894) · [Parity vs. AC0 with Simple Quantum Preprocessing](https://doi.org/10.4230/LIPIcs.ITCS.2024.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4927 — Classification of quantum gate sets

A classification of reversible classical gates describes which transformations become possible when a gate set is composed repeatedly. The source uses that completed classical picture to motivate an analogous classification for quantum gates. The quantum question is whether known nonuniversal families, such as stabilizer operations and basis-preserving constructions, account for all relevant possibilities. Additional discrete families or intermediate computational behavior could make the quantum landscape substantially richer. A full classification would organize quantum gate resources by the computations they enable and identify exactly where universality appears.

[Read in atlas](index.html#TCS-4927) · [The Classification of Reversible Bit Operations](https://doi.org/10.4230/LIPIcs.ITCS.2017.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4952 — Quantum–classical communication gaps for total functions

Quantum communication can outperform randomized classical communication dramatically on some problems with restricted inputs. This project asks whether an exponential separation is possible for a total function, whose value is defined on every input pair. The cited work also emphasizes efficient local computation by the communicating parties, so a protocol's message length is not its only resource. Promise-problem separations do not by themselves answer the total-function question because their input restrictions may be essential. Resolving this would clarify how broadly quantum communication advantages survive when both the task specification and the players' computations are constrained.

[Read in atlas](index.html#TCS-4952) · [Quantum Versus Randomized Communication Complexity, with Efficient Players](https://doi.org/10.4230/LIPIcs.ITCS.2021.54)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4977 — Classical-witness versus quantum-witness hierarchies

Quantum polynomial hierarchies extend alternating proof systems by allowing quantum witnesses and different restrictions on their states. The source compares a hierarchy with classical witnesses, one with general quantum witnesses, and one with pure-state witnesses. The selected question is whether the classical-witness hierarchy is contained in the general quantum-witness hierarchy in the intended bounded-error sense. Simply replacing each classical proof by a measured quantum state can fail to preserve the behavior of alternating quantifiers. Establishing the containment, or identifying an obstruction, would clarify how classical information, mixed states, and quantifier order interact in quantum verification.

[Read in atlas](index.html#TCS-4977) · [Quantum Polynomial Hierarchies: Karp-Lipton, Error Reduction, and Lower Bounds](https://doi.org/10.4230/LIPIcs.MFCS.2024.7)
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

### TCS-6459 — Entanglement without distillable secret key

Shared quantum states can sometimes be converted into secret classical keys by local operations and public communication. This project asks whether there are entangled states from which no secret key can be distilled. Separable states provide a known class of useless resources, but entanglement alone does not immediately determine the distillable-key rate. The question is also different from asking whether an entangled state can produce maximally entangled pairs. Identifying an entangled key-undistillable state, or proving that none exists, would settle a basic boundary in the resource theory of private communication.

[Read in atlas](index.html#TCS-6459) · [Cost of quantum secret key](https://doi.org/10.22331/q-2026-05-06-2098)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6481 — Complexity of bosonic quantum computation

Continuous-variable quantum computation uses bosonic modes rather than a finite collection of two-level systems alone. This source studies a model with cubic phase gates and proves an exponential-space upper bound on its computational power. It asks whether that upper bound can be substantially improved, perhaps toward the classical counting classes that contain ordinary qubit quantum computation. Cubic phase gates can rapidly increase the degree and coefficient size of operator expressions, obstructing straightforward simulations. A tighter characterization would clarify which apparent extra power comes from the infinite-dimensional model and which reflects limitations of current analysis.

[Read in atlas](index.html#TCS-6481) · [Bosonic Quantum Computational Complexity](https://doi.org/10.22331/q-2026-05-20-2110)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6933 — Classical hardness of Boson Sampling

Boson sampling asks a device to sample the output pattern of photons passing through a linear-optical network. The cited overview presents the conjecture that classical computers cannot perform this sampling efficiently in the specified regime. The difficulty concerns reproducing a distribution, so computing one output probability is not by itself the same task. Exact sampling, approximate sampling, and experimental noise require different assumptions and must be separated when the conjecture is formalized. Resolving the relevant hardness claim would support a concrete route to quantum sampling advantage without requiring a universal quantum computer.

[Read in atlas](index.html#TCS-6933) · [Quantum Algorithms: An Overview](https://arxiv.org/abs/1511.04206)
Existing status: `source_open` · Summary written: 2026-09-11
