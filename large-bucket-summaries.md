# Working summaries — large categories

696 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computational complexity (130)

### TCS-0001 — Does P equal NP?

P versus NP asks whether every problem with efficiently checkable solutions also has an efficient deterministic decision algorithm. Boolean satisfiability is a representative test case because all NP problems reduce to it. Checking one assignment is easy, while deciding whether any assignment works requires accounting for all possibilities. The target concerns worst-case polynomial time on arbitrarily large inputs. A resolution would establish a fundamental relationship between searching and verifying, without by itself determining practical exponents or average-case difficulty.

[Read in atlas](index.html#TCS-0001) · [The P versus NP Problem](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Algebrization: A New Barrier in Complexity Theory](https://www.scottaaronson.com/papers/alg.pdf) · [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [P vs NP — Millennium Prize Problem](https://www.claymath.org/millennium/p-vs-np/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6530 — Does P equal PSPACE?

Polynomial space permits a computation to reuse its memory while exploring potentially enormous collections of possibilities. The question asks whether every problem solvable with that memory budget is also solvable in polynomial time. Truth of quantified Boolean formulas supplies a concrete complete problem. Alternating existential and universal choices describe strategies that can be much larger than one ordinary certificate. The project tests whether repeated reuse of a modest workspace gives strictly more decision power than any polynomial-time computation.

[Read in atlas](index.html#TCS-6530) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Alternation](https://doi.org/10.1145/322234.322243) · [IP = PSPACE](https://doi.org/10.1145/146585.146609) · [Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779v1) · [Some Recent Developments in Space Complexity](https://doi.org/10.4230/LIPIcs.MFCS.2026.3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6531 — Can every polynomial-time decision problem be solved in logarithmic space?

Logarithmic-space computation can retain only a few input indices and counters while repeatedly rereading the input. The question asks whether that memory always suffices for every polynomial-time decision problem. Evaluating a supplied Boolean circuit is a representative complete task. Shared dependencies make naive recomputation expensive, while storing all intermediate gate values exceeds the space budget. The project tests whether efficient computation fundamentally needs substantial working memory or can always reorganize its information into an extremely small state.

[Read in atlas](index.html#TCS-6531) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Limits to Parallel Computation: P-Completeness Theory](https://homes.cs.washington.edu/~ruzzo/papers/limits.pdf) · [Undirected Connectivity in Log-Space](https://omereingold.wordpress.com/wp-content/uploads/2014/10/sl.pdf) · [Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779v1) · [Logarithmic Space](https://cs.uwaterloo.ca/~eblais/cs365/w26/L-and-NL)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6535 — Is nonuniform TC⁰ strictly smaller than nonuniform NC¹?

TC0 circuits use a constant number of layers of powerful majority gates. NC1 circuits use logarithmically many layers of ordinary bounded-input Boolean gates. The question asks whether the former nonuniform class is strictly weaker than the latter. Many arithmetic tasks already fit in TC0, so their familiar sequential implementations do not provide separating examples. The project seeks a function whose nested logical dependencies cannot be compressed into a fixed-depth network even when each gate can aggregate many inputs at once.

[Read in atlas](index.html#TCS-6535) · [Bootstrapping Results for Threshold Circuits “Just Beyond” Known Lower Bounds](https://eccc.weizmann.ac.il/report/2018/199/) · [Uniform constant-depth threshold circuits for division and iterated multiplication](https://doi.org/10.1016/S0022-0000(02)00025-9) · [Characterizing NC¹ with Typed Monoids](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.26) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6534 — The Berman–Hartmanis isomorphism conjecture

Polynomial-time reductions show that NP-complete problems can simulate each other, but may erase information. The Berman-Hartmanis conjecture asks whether every pair instead admits a polynomial-time computable bijection with a polynomial-time inverse. That bijection must preserve yes and no instances across the entire string space. Padding provides evidence for familiar complete problems without covering all possible complete languages. The project asks whether completeness forces one efficiently reversible organization of instances, reaching beyond ordinary mutual reducibility.

[Read in atlas](index.html#TCS-6534) · [On Isomorphisms and Density of NP and Other Complete Sets](https://epubs.siam.org/doi/10.1137/0206023) · [The ismorphism conjecture fails relative to a random oracle](https://doi.org/10.1145/73007.73022) · [The Isomorphism Conjecture Holds Relative to an Oracle](https://epubs.siam.org/doi/10.1137/S0097539793248305) · [Reductions in Circuit Complexity: An Isomorphism Theorem and a Gap Theorem](https://www.cse.iitk.ac.in/users/manindra/isomorphism/non-uniform-ac0-iso.pdf) · [One-Way Functions and the Isomorphism Conjecture](https://eccc.weizmann.ac.il/report/2009/019/) · [Open Problems by or Inspired by Juris Hartmanis](https://www.cs.umd.edu/~gasarch/open/juris.pdf) · [The Isomorphism Conjecture for NP](https://cse.iitk.ac.in/users/manindra/survey/Isomorphism-Conjecture.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6532 — Is the polynomial hierarchy strict at every finite level?

The polynomial hierarchy adds successive alternating blocks of efficiently bounded existential and universal choices. Its first levels already include polynomial-time computation and ordinary NP verification. The question asks whether every additional fixed level strictly increases computational power. Equality of neighboring levels would collapse all higher finite levels as well. The project studies whether increasingly nested candidate-and-challenge reasoning creates an endless hierarchy of difficulty, a stronger issue than separating P from NP at the first step.

[Read in atlas](index.html#TCS-6532) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [The Polynomial-Time Hierarchy](https://research.ibm.com/publications/the-polynomial-time-hierarchy) · [The Polynomial Hierarchy, Random Oracles, and Boolean Circuits](https://www.cs.columbia.edu/~rocco/Public/sigact15.pdf) · [An Average-Case Depth Hierarchy Theorem for Boolean Circuits](https://arxiv.org/abs/1504.03398) · [Upper and Lower Bounds for the Linear Ordering Principle](https://eccc.weizmann.ac.il/report/2025/142/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0021 — Does NP contain a language without polynomial-size Boolean circuits?

Nonuniform Boolean circuits may choose a separate computational design for each input length. The question asks whether some language in NP requires more than polynomially many gates despite that freedom. A uniform running-time lower bound would not automatically establish this stronger claim. Counting shows that most functions have large circuits but does not supply the necessary NP language. The project seeks explicit hardness robust to arbitrary length-specific preprocessing and would connect circuit lower bounds to the structure of the polynomial hierarchy.

[Read in atlas](index.html#TCS-0021) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Natural Proofs](https://doi.org/10.1006/jcss.1997.1494) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0002 — Does every unsatisfiable Boolean formula have a short efficiently checkable certificate?

An unsatisfiable formula has no assignment that makes every clause true. The question asks whether one fixed efficient verifier can always check a polynomial-length certificate of that impossibility. The certificate format is unrestricted as long as it is sound for every formula. This is equivalent to asking whether NP equals coNP. The project concerns the possibility of universally concise explanations for the failure of all candidate solutions, rather than lower bounds for any one particular set of proof rules.

[Read in atlas](index.html#TCS-0002) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Circuits, Communication, and Proofs](https://www.icts.res.in/program/ccp)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0015 — An explicit function with no linear-size Boolean circuits

A multi-output Boolean function can share intermediate computations among all its output bits. The question asks for one polynomial-time computable family whose unrestricted Boolean circuits exceed every fixed linear size bound. The saved formulation uses as many output bits as input bits. An arbitrary hard truth table does not satisfy the explicitness requirement. The project seeks a modest but fundamental lower bound demonstrating that some efficiently specified transformations intrinsically need more than a constant amount of circuit work per input bit.

[Read in atlas](index.html#TCS-0015) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [3.1n − o(n) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://eccc.weizmann.ac.il/report/2025/033/) · [Convergent Gate Elimination and Constructive Circuit Lower Bounds](https://arxiv.org/abs/2602.17942) · [A Note on Natural-Proofs for Super-Linear Lower Bounds for Linear Functions](https://eccc.weizmann.ac.il/report/2026/008/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0016 — Exponential circuit lower bounds for 3-SAT

The saved 3-SAT family uses a fixed encoding of which clauses on n variables are present. The conjecture asks for circuit size exponential in n, even when every input length gets its own arbitrary circuit. Its scale is stronger than merely excluding polynomial-size circuits. The variable count differs from the total number of encoded clause bits, so the parameter must remain explicit. The project aims to prove that searching for a satisfying assignment retains essentially exponential difficulty even under nonuniform computation.

[Read in atlas](index.html#TCS-0016) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Which Problems Have Strongly Exponential Complexity?](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturiZane_2001_jcss.pdf) · [3.1n − o(n) Circuit Lower Bounds for Explicit Functions](https://eccc.weizmann.ac.il/report/2021/023/) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7158 — Does PH equal PSPACE?

Does every polynomial-space decision problem lie in the polynomial hierarchy? PH allows a fixed number of alternating quantifier blocks for each language. PSPACE also describes polynomial-time alternation with no fixed bound on the number of alternations. Equality would put TQBF in one finite level and hence collapse PH to that level. Completeness and oracle results illuminate the distinction without settling the ordinary class equality.

[Read in atlas](index.html#TCS-7158) · [Computational Complexity: A Modern Approach (Internet draft)](https://theory.cs.princeton.edu/complexity/book.pdf) · [Completeness in the Polynomial Hierarchy and PSPACE for many natural problems derived from NP](https://arxiv.org/abs/2602.12350) · [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](https://arxiv.org/abs/2602.02294)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7161 — Does NEXP require superpolynomial constant-depth threshold circuits?

Does some NEXP language escape all polynomial-size constant-depth majority circuits? Majority gates make this circuit class substantially more powerful than constant-depth AND/OR circuits. Williams established the corresponding separation for ACC circuits with fixed-modulus gates. Recent threshold-circuit bounds still restrict depth or polynomial size and use different hard-language classes. The target requires one ordinary NEXP language outside the entire nonuniform class TC⁰.

[Read in atlas](index.html#TCS-7161) · [Non-Uniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-ccc.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/) · [Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM ∘ THR and THR ∘ THR](https://eccc.weizmann.ac.il/report/2026/167/) · [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6533 — NL versus UL

An ordinary nondeterministic reachability algorithm can have many accepting paths of computation. UL requires at most one accepting computation for each input while retaining logarithmic workspace. The question asks whether this unambiguity restriction changes the class NL. The machine may still have many rejecting branches, so this is weaker than demanding determinism. The project seeks to isolate a unique successful witness efficiently, clarifying whether ambiguity itself is a source of computational power in small-space graph problems.

[Read in atlas](index.html#TCS-6533) · [Making Nondeterminism Unambiguous](https://people.cs.rutgers.edu/~allender/papers/nlul.pdf) · [Derandomizing Isolation in Space-Bounded Settings](https://pages.cs.wisc.edu/~dieter/Papers/r-ul-sicomp.pdf) · [When Connectivity Is Hard, Random Walks Are Easy With Non-Determinism](https://eccc.weizmann.ac.il/report/2025/077/download) · [Using Hardness vs Randomness to Design Low-Space Algorithms](https://eccc.weizmann.ac.il/report/2026/045/) · [Derandomizing Isolation In Catalytic Logspace](https://arxiv.org/abs/2512.09374) · [Deterministic, Oblivious Isolation for Space-Bounded Computation Requires Large Weights](https://eccc.weizmann.ac.il/report/2026/124/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0004 — Can directed reachability be decided in deterministic logarithmic space?

Directed reachability asks whether a path leads from a specified source to a specified target. Nondeterminism solves it with logarithmic memory by guessing successive vertices. The question asks for a deterministic algorithm using the same tiny workspace on an explicitly stored graph. Repeated input scans are allowed, but a full visited array or search frontier is not. The project would settle L versus NL by showing whether all the essential information in directed exploration can be organized without guessing or substantial stored history.

[Read in atlas](index.html#TCS-0004) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Relationships between nondeterministic and deterministic tape complexities](https://doi.org/10.1016/S0022-0000(70)80006-X) · [Nondeterministic Space is Closed under Complementation](https://doi.org/10.1137/0217058) · [Undirected Connectivity in Log-Space](https://omereingold.wordpress.com/wp-content/uploads/2014/10/sl.pdf) · [When Connectivity Is Hard, Random Walks Are Easy with Non-determinism](https://doi.org/10.1145/3717823.3718303) · [Reachability in graphs having linear 2-arboricity two is NL-hard](https://doi.org/10.1016/j.ipl.2025.106611)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6681 — DNF versus d-DNNF succinctness

A DNF formula describes satisfying assignments as a union of conjunctions, whose cases may overlap. The proposal asks whether some polynomial-size DNFs require superpolynomial-size deterministic decomposable circuits for the same Boolean function. Determinism requires disjoint alternatives, while decomposability requires conjunctions to separate their variables. A separation would show that imposing these useful structural restrictions can force an inherent representation-size increase. The question is about the existence of compact equivalent circuits, so hardness of efficiently finding a conversion or a separation for unrestricted DNNFs does not by itself answer this more specific size comparison.

[Read in atlas](index.html#TCS-6681) · [Florent Capelli — Habilitation manuscript](https://capelli.me/publi/hdr.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0020 — Polynomial-size circuits for EXP

EXP contains problems solvable in deterministic exponential time. The question asks whether every such problem could nevertheless have polynomial-size Boolean circuits chosen separately for each input length. The circuits need not be efficiently constructible, making this different from a polynomial-time simulation. Time hierarchy theorems alone do not eliminate that nonuniform possibility. The project seeks a lower bound strong enough to defeat arbitrary length-specific circuit designs for some language with an explicit exponential-time decision procedure.

[Read in atlas](index.html#TCS-0020) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1056 — Majority outside constant-depth modular circuits

Constant-depth modular circuits combine ordinary Boolean gates with gates that inspect counts modulo specified integers. The saved question asks for a lower bound excluding majority from the relevant class. Majority depends on an overall threshold, so it provides a concrete test of whether modular counting and shallow composition capture ordinary counting strength. Proving the separation would sharpen the boundary between basic Boolean circuit models. The inherited book pointer does not preserve the allowed moduli, gate basis, or size target, and those details must be recovered before this becomes one precise majority lower-bound claim.

[Read in atlas](index.html#TCS-1056) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0018 — P versus NP intersect coNP

A language in NP intersect coNP has short efficiently checkable certificates for both yes and no instances. The question asks whether some such language still lies outside deterministic polynomial time. Having two kinds of witnesses does not automatically tell an algorithm how to find either one. The separation would identify difficulty independent of the asymmetric certification typical of NP-complete problems. The project explores whether efficiently verifiable certainty on both sides can coexist with an intrinsically hard decision process.

[Read in atlas](index.html#TCS-0018) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1054 — Exponential lower bounds for unrestricted threshold-of-threshold circuits

A threshold-of-threshold circuit applies threshold gates in two successive layers. The saved question seeks exponential lower bounds without imposing additional restrictions on those gates. Arbitrary weights and hidden-layer combinations can encode substantially more than a single threshold, making simple geometric arguments insufficient. A lower bound would expose a strong limitation of a shallow model related to weighted voting and classification. The inherited source label does not identify the explicit function, weight conventions, or measured size, so the full book problem is needed before specifying the exponential target more sharply.

[Read in atlas](index.html#TCS-1054) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7159 — The Hartmanis–Stearns conjecture

The question concerns a fixed machine that prints all digits of a real number with bounded delay between outputs. Every rational number permits this because its expansion is eventually periodic. The conjecture says that any irrational number generated this quickly must be transcendental. It quantifies over unrestricted deterministic multitape machines, beyond the restricted automata covered by known partial results. A proof would connect the arithmetic nature of numbers to a stringent computation bound and rule out linear-time integer multiplication.

[Read in atlas](index.html#TCS-7159) · [On the computational complexity of algebraic numbers: the Hartmanis–Stearns problem revisited](https://arxiv.org/abs/1601.02771) · [Time-Restricted Sequence Generation](https://people.csail.mit.edu/meyer/time-restricted-sequence-generation-jcss.pdf) · [On Transcendence of Numbers Related to Sturmian and Arnoux-Rauzy Words](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.144) · [Computing the base-b representation of quadratic irrationals using automata](https://doi.org/10.1016/j.tcs.2026.115843)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7243 — Do stable ternary compaction functions have linear-size Boolean circuits?

Stable ternary compaction moves every 2 to the end while preserving the order of all 0s and 1s. The question is whether every input length admits a Boolean circuit of size proportional to that length. The circuits use a fixed bounded-fan-in basis and may have arbitrary depth and fan-out. Stability retains the original binary sequence, so ordinary ternary sorting is insufficient. The target supplies a concrete function for studying the limits of linear-size circuits.

[Read in atlas](index.html#TCS-7243) · [Linear-size circuits for stable 0,1 < 2 sorting?](https://www.openproblemgarden.org/op/linear_size_circuits_for_stable_0_1_2_sorting) · [Sorting Short Keys in Circuits of Size o(n log n)](https://arxiv.org/abs/2010.09884)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0017 — Karchmer–Raz–Wigderson formula composition conjecture

Composing Boolean functions means applying one function to separate input blocks and feeding the results into another. A straightforward formula substitutes a copy of the inner formula for each outer input occurrence. The KRW conjecture asks whether formula complexity must essentially multiply under this operation. Unexpected sharing is unavailable in formulas, but alternate logical factorizations might still save size. The project seeks a composition lower bound powerful enough to separate efficient circuits from much larger formulas.

[Read in atlas](index.html#TCS-0017) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0019 — Polynomial formulas versus linear circuits

Circuits can reuse intermediate results, while formulas duplicate them whenever several later computations need them. The conjecture asks for functions with linear-size circuits but no polynomial-size formulas. Known polynomial gaps do not establish this superpolynomial separation. The source connects the goal to understanding formula complexity under repeated composition. The project asks whether a small directed computational graph can perform a task that every tree-shaped computation must express with vastly more repeated work.

[Read in atlas](index.html#TCS-0019) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6455 — Doubly efficient IP = PSPACE for the full time range

An interactive proof lets a verifier check a claim through conversation with a prover. The question asks whether polynomial-space computations taking time T can be verified in polynomial input time using an honest prover running in polynomial T time. The requirement extends across the full time range, beyond quasipolynomial computations. This would make proof generation efficient relative to the computation being certified, strengthening the resource content of IP=PSPACE. The saved review stresses that soundness must still withstand arbitrarily powerful cheating provers, despite the efficiency requirement imposed on the honest one.

[Read in atlas](index.html#TCS-6455) · [Towards a Doubly Efficient IP=PSPACE](https://eccc.weizmann.ac.il/report/2026/102/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0305 — Supercubic uniform formula lower bounds for SAT

A De Morgan formula computes with binary AND and OR gates and input negations, without sharing internal computations. Its size counts leaf occurrences, and the target function is SAT on n bits encoding a 3-CNF formula. The source asks whether a fixed positive exponent can raise the required size beyond the cubic scale when the formula family is LOGTIME-uniform. Later NAND depth lower bounds use a different gate basis and cost measure, so they do not directly settle this question. The problem seeks a concrete improvement in uniform formula lower bounds for a central NP-complete language.

[Read in atlas](index.html#TCS-0305) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Towards Stronger Depth Lower Bounds](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.10)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1052 — Depth-three lower bounds beyond the switching-lemma barrier

Depth-three Boolean circuits compute through only three layers of gates but may have many gates within each layer. The source asks for lower bounds exceeding the reach of the stated switching-lemma approach. Switching arguments simplify restricted circuits, so the challenge is to prove hardness that survives limitations of that simplification method. Progress would strengthen explicit circuit lower bounds at a very small depth. The short inherited label does not preserve the gate basis, target function, or quantitative barrier, and those source details are needed before identifying exactly what improvement would answer the question.

[Read in atlas](index.html#TCS-1052) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1053 — Depth-three size bounds beyond exponential square root

The saved problem concerns size lower bounds for Boolean circuits of depth three. Its target lies beyond an exponential-in-square-root scale, asking for a stronger obstruction than the source's reference bound. Depth is fixed, so the sought improvement must come from showing that many parallel gates cannot compensate for limited composition. Such a result would clarify the expressive power of very shallow Boolean computation. The book pointer does not include the underlying input parameter, basis, or function family, so the notation for the exponential threshold must be recovered instead of guessed from the abbreviated title.

[Read in atlas](index.html#TCS-1053) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1039 — Explicit superlinear in-place XOR lower bounds

An in-place XOR computation updates a fixed collection of registers by exclusive-or operations. It must compute an explicitly described binary linear transformation without freely introducing new storage for intermediate values. The source asks for a superlinear lower bound on this restricted computational cost. General counting arguments give hard transformations without necessarily supplying the required explicit family. The project seeks to show that some concrete reversible-looking linear tasks need more than a constant number of register updates per input coordinate.

[Read in atlas](index.html#TCS-1039) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0293 — Subquadratic deterministic simulation of nondeterministic space

Savitch’s theorem simulates nondeterministic space s with deterministic space O(s²). This card asks whether every at-least-logarithmic space-constructible bound admits an improvement to o(s²). The machine is deterministic and all ordinary working memory is charged, with no restriction on running time. A constant-factor improvement does not suffice, while no fixed polynomial saving is required. A resolution would sharpen the general memory cost of eliminating nondeterminism, including for logarithmic-space computation.

[Read in atlas](index.html#TCS-0293) · [Improving SPACE versus NSPACE via Tree Evaluation, in Computational Complexity of Discrete Problems](https://doi.org/10.4230/DagRep.15.3.56)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0301 — Excluding one-sided randomized quasilinear-time log-space SAT

Randomized SAT algorithms may miss a satisfying assignment while never incorrectly declaring an unsatisfiable formula satisfiable. The question asks to rule out algorithms with that one-sided error using both quasilinear time and logarithmic space. The source emphasizes that reversing the permitted error direction changes what lower-bound methods can prove. Deterministic time-space tradeoffs do not automatically handle random choices. The project seeks a lower bound matching the error behavior of incomplete randomized search procedures under extremely small resource budgets.

[Read in atlas](index.html#TCS-0301) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0302 — Excluding quasilinear-time log-space Max Clique

Maximum Clique seeks a largest set of mutually adjacent vertices. The source asks to exclude algorithms using both quasilinear time in the number of edges and logarithmic workspace. The intended model permits random access to the input. A lower bound for sequential tape access is weaker, while ordinary reductions from SAT may inflate the input too much. The project seeks a resource lower bound sensitive to sparse encoding size and robust against an algorithm's ability to inspect arbitrary edges directly.

[Read in atlas](index.html#TCS-0302) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0303 — Stronger log-space time lower bounds for SAT

Time-space lower bounds show that some combinations of fast running time and tiny memory cannot solve SAT. The source asks to strengthen the known limits for logarithmic-space algorithms. This differs from proving a general SAT time lower bound because the memory restriction supplies additional structure. Simulation and alternation-trading arguments are central tools in the cited discussion. The project seeks a sharper quantitative obstruction to deciding satisfiability while retaining only a few indices, even if the input can be revisited freely.

[Read in atlas](index.html#TCS-0303) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0304 — Stronger uniform depth-three majority lower bounds for SAT

A depth-three majority circuit aggregates Boolean inputs through at most three majority layers and may use negations. The source asks for a SAT lower bound exceeding n^(5/2) wires by a fixed positive exponent under LOGTIME-uniformity. The input length counts bits encoding the SAT instance, while wire count charges every connection into a gate. Known explicit-function wire bounds near the 5/2 exponent motivate the question but do not supply the requested uniform SAT bound. A resolution would improve quantitative understanding of shallow majority computation on an NP-complete language.

[Read in atlas](index.html#TCS-0304) · [Some Open Problems Regarding Lower Bounds For NP](https://www.cs.umd.edu/~gasarch/open/lbfornp.pdf) · [Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits](https://doi.org/10.1145/2897518.2897636)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0308 — Formula versus circuit succinctness

A Boolean circuit may send one intermediate result to many later gates. An equivalent formula must arrange its reasoning as a tree and can be forced to duplicate that result. The source question asks how large the resulting succinctness gap can become. A superpolynomial separation would show that small circuits cannot always be unfolded or reorganized into polynomial-size formulas. The project investigates whether computational sharing provides an intrinsically stronger representation, rather than only a convenient optimization of one chosen expression.

[Read in atlas](index.html#TCS-0308) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#conciseness-gap-between-formulae-and-circuits)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0310 — Is weighted falsifiability of unambiguous DNFs in polynomial time?

An unambiguous DNF has mutually disjoint satisfying terms, making some counting tasks straightforward. The question instead asks for a falsifying assignment with sufficiently large total variable weight. Weights and the threshold are binary encoded. Knowing how many assignments falsify the formula does not reveal whether one reaches the desired score. The project tests whether the strong disjointness promise still helps when every term must be defeated simultaneously while optimizing an additive objective over the complement.

[Read in atlas](index.html#TCS-0310) · [Is this problem on unambiguous DNFs hard?](https://cstheory.stackexchange.com/questions/53733/is-this-problem-on-unambiguous-dnfs-hard) · [Representation, Provenance, and Explanations in Database Theory and Logic (Dagstuhl Seminar 24032)](https://doi.org/10.4230/DagRep.14.1.49) · [List of open questions: Weighted falsifiability for unambiguous DNFs](https://a3nm.net/work/research/questions/#weighted-falsifiability-for-unambiguous-dnfs)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1035 — Cost of restricting linear circuits to depth two

A linear circuit shares partial sums to compute a matrix transformation over a specified operation system. Restricting it to depth two allows only one intermediate layer. The source asks how much this restriction can increase circuit complexity, with different behavior for OR, SUM, and XOR operations. Known separations leave room for stronger gaps, particularly over the binary field. The project seeks to quantify the value of additional computational layers even when the final transformation is algebraically simple.

[Read in atlas](index.html#TCS-1035) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1037 — Asymmetry of XOR complexity under matrix inversion

An invertible binary matrix defines a linear transformation and its inverse. Both can be computed using XOR gates, but the smallest circuits need not follow the same construction. The question asks whether the ratio between their unrestricted XOR complexities can grow without bound. Separations at fixed depth do not settle the unrestricted model. The project seeks an algebraic analogue of directional computational difficulty, testing whether one exact linear change of coordinates can be fundamentally easier than undoing it.

[Read in atlas](index.html#TCS-1037) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1040 — Nonlinear-gate advantages for binary linear operators

A binary linear operator outputs parity combinations of its input bits. XOR circuits stay linear at every intermediate step, while general Boolean circuits may temporarily compute nonlinear functions. The question asks whether those nonlinear intermediates can provide an unbounded size advantage. The source relates this to rank-based conjectures for partially specified matrices. The project tests whether matching the algebraic form of the output is essentially optimal, or whether leaving that form during computation can lead to substantially more efficient circuits.

[Read in atlas](index.html#TCS-1040) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1034 — Largest separation between SUM and OR circuits

The same zero-one matrix can define a transformation using ordinary addition or Boolean OR. OR is idempotent, so repeated contributions can collapse, while SUM must count them accurately. The source asks for the largest possible circuit-size gap between these two computation systems. Depth restrictions lead to additional versions with different known bounds. The project aims to quantify how much the ability to ignore duplicate contributions changes the cost of computing many related linear-looking outputs at once.

[Read in atlas](index.html#TCS-1034) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1036 — Unbounded XOR-over-OR complexity separations

For one zero-one matrix, OR circuits and XOR circuits combine the same selected input positions using different operations. OR ignores repeated positive contributions, whereas XOR can cancel them modulo two. The question asks whether unrestricted XOR complexity can exceed OR complexity by an unbounded factor. Results for restricted depth do not automatically extend to arbitrary circuits. The project seeks a concrete matrix family showing that cancellation is not always an advantage when many outputs must share intermediate computations.

[Read in atlas](index.html#TCS-1036) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1051 — Logarithmic negation-depth lower bounds for monotone functions

A monotone Boolean function never changes from true to false when input bits are increased coordinatewise. The saved problem asks for logarithmic lower bounds on negation depth in the source's circuit setting. Although the output is monotone, using negations internally can alter how efficiently the function is computed. The question therefore probes how deeply nonmonotone behavior must be nested to obtain the relevant computational savings. The source's size restriction and definition of negation depth are absent from the label, and they are essential because an unrestricted monotone representation would contain no negation gates at all.

[Read in atlas](index.html#TCS-1051) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0014 — Cubic monotone formulas for majority

Majority decides whether more than half the input bits are one. A monotone formula computes it using AND and OR without negations or shared intermediate gates. The source asks for a cubic-size construction at the stated asymptotic scale. Efficient monotone circuits are easier because they can reuse partial computations. The project seeks an economical tree-shaped counting construction and a sharper understanding of how much repetition is unavoidable when formulas must aggregate many interchangeable input bits.

[Read in atlas](index.html#TCS-0014) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0068 — AC0 on trees

The source proposes Boolean circuit families indexed by unlabeled binary-tree shapes rather than only by input length. Input valuations then label the tree nodes with bits. The question asks which regular tree languages are recognizable by constant-depth polynomial-size circuits in this setting. A conjectured logical characterization uses label predicates, ancestry, and shape-only definable predicates. The project extends the well-studied connection between circuit complexity and regular word languages to inputs with branching structure.

[Read in atlas](index.html#TCS-0068) · [Circuits, Logic and Games](https://doi.org/10.4230/DagRep.5.9.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0295 — Sampling modular distributions locally

A local sampler produces each output bit from only a bounded number of independent random input bits. The desired distribution is uniform over strings whose Hamming weight is divisible by a fixed modulus. Parity has a simple exact local sampler. The source conjectures that moduli larger than two cannot be sampled with arbitrarily small variation error using locality depending only on that error. The project seeks to explain why one global modular constraint is compatible with local generation while others may require genuinely nonlocal dependence.

[Read in atlas](index.html#TCS-0295) · [Computational Complexity of Discrete Problems](https://doi.org/10.4230/DagRep.13.3.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0297 — A counting function capturing exactly P with NP access

A counting function in #P returns the number of accepting witnesses for an efficiently checkable relation. The question asks whether some such function gives a polynomial-time oracle machine exactly the power of polynomial time with an NP oracle. Ordinary complete counting functions provide substantially more apparent information than mere existence tests. The target therefore requires a specially controlled counting task. The project seeks a numerical oracle capturing NP access without unintentionally granting the full power of general witness counting.

[Read in atlas](index.html#TCS-0297) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0298 — SAT multi-prover proofs using efficient SAT-oracle provers

Multi-prover interactive proofs let a verifier question several provers that cannot coordinate their answers during the protocol. The source asks for such a proof system for SAT whose honest provers run in randomized polynomial time with SAT-oracle access. Unrestricted provers do not meet this efficiency requirement. The question is tied to whether SAT programs can be checked through suitable oracle interactions. The project seeks a verification protocol whose participants need no computational power beyond the problem they are supposed to certify.

[Read in atlas](index.html#TCS-0298) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0126 — The Parity Language

The parity language separates binary words with an even number of ones from those with an odd number. This project asks for robust subsets whose opposite-parity witnesses remain coordinatewise compatible after polynomial-density thinning. Compatibility means that each coordinate of a chosen even-parity word is matched by some word in the surviving odd-parity set. The order of subset choices matters because the witness set may depend on the selected even-parity subset. Proving this combinatorial property would support structural lower-bound arguments for shallow Boolean circuits and related regular-language classifications.

[Read in atlas](index.html#TCS-0126) · [Automata Exchange](https://automata.exchange/22.10-the-parity-language/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1144 — Is it true that spr(IPn ) = ω(n) or spr(Disjn ) = ω(n)?

Spiky rank measures how many block-structured matrices are needed to express a matrix as a sum. Each summand consists of disjoint rank-one blocks, combining a combinatorial partition with flexible real coefficients. The question asks whether the inner-product matrix or the disjointness matrix on n-bit inputs has spiky rank growing faster than n. The source introduces this parameter as a possible way to capture complexity that ordinary rank or rigid block decompositions miss. A superlinear lower bound for either standard matrix would demonstrate that the new measure detects a substantial obstruction on central communication problems.

[Read in atlas](index.html#TCS-1144) · [Spiky Rank and Its Applications to Rigidity and Circuits](https://doi.org/10.4230/LIPIcs.ICALP.2026.106)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1235 — Do unrestricted weights make polynomial-size linear decision lists stronger?

A linear decision list evaluates weighted threshold tests and returns the bit attached to the first successful test. The question asks whether polynomially bounded weights are weaker than unrestricted weights when both kinds of list have polynomial size. Polynomial weight magnitude is a stronger restriction than polynomial encoding length. The source proves separations when the number of output alternations is restricted. The open comparison removes that restriction and asks whether large weights still provide additional expressive power.

[Read in atlas](index.html#TCS-1235) · [Alternation Depth of Threshold Decision Lists](https://doi.org/10.4230/LIPIcs.ICALP.2026.148)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1442 — Is there an algebrizing barrier to proving MA ̸⊆ SIZE[nk ]?

Algebrization barriers describe limitations of proof techniques that remain valid when computation receives particular algebraic oracle access. The source asks whether such a barrier prevents proving MA is outside circuits of size n^k. The target concerns a circuit lower bound for a class with randomized verification and advice from a prover. A barrier would explain why a broad style of argument cannot establish that separation, rather than refute the separation itself. The saved excerpt does not specify the quantification over k or oracle framework, so these must be restored before stating the exact limitation theorem sought.

[Read in atlas](index.html#TCS-1442) · [New Algebrization Barriers to Circuit Lower Bounds via Communication Complexity of Missing-String](https://doi.org/10.4230/LIPIcs.ITCS.2026.37)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1494 — The main problem left open by this work is to exhibit a natural problem in TFZPPdt which is not reducible to Lossy-Code; we conjecture that […]

Total search problems guarantee that every valid input has some acceptable output. The cited paper studies a zero-error randomized decision-tree class denoted TFZPPdt. The saved question asks for a natural problem in that class that does not reduce to Lossy-Code. Such an example would show that one proposed search task does not capture the entire class under the intended reductions. The excerpt truncates the authors' conjectured candidate and omits the reduction model, so neither the candidate nor the precise separation criterion is reconstructed here.

[Read in atlas](index.html#TCS-1494) · [Total Search Problems in ZPP](https://doi.org/10.4230/LIPIcs.ITCS.2026.60)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1510 — Are there properties of finite mathematical objects that can only be certified efficiently to a high degree of confidence by probabilistic algorithms, but that we […]

A randomized computation can give extremely high confidence in a finite mathematical fact without providing an ordinary short proof. The source motivates this issue through bounds on the diameter of Rubik's Cube and related vertex-transitive graphs. It asks whether some properties admit efficient probabilistic certification while resisting comparably efficient certain certification. The distinction concerns evidence for a fixed deterministic fact, not randomness in the fact itself. The project explores the boundary between trustworthy computational experiments and concise deductive verification.

[Read in atlas](index.html#TCS-1510) · [A Demigod’s Number for the Rubik’s Cube](https://doi.org/10.4230/LIPIcs.FUN.2026.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1553 — Construct an explicit family of boolean functions fn : {0, 1}n → {0, 1} such that there exist constants δ1 , δ2 > 0 such […]

The selected question asks for an explicit Boolean function family that defeats circuits of mildly superlinear size and polynomially bounded depth. The circuit gates have constant fan-in and fan-out, and the target fixes positive exponents for both resource bounds. The source raises this circuit lower-bound problem as a barrier to proving stronger distributed graph-detection lower bounds. It shows that certain polynomial CONGEST lower bounds for ordered paths or induced cycles would already solve the circuit challenge. The connection warns that apparently local network problems can require progress on a major unrestricted circuit lower-bound frontier.

[Read in atlas](index.html#TCS-1553) · [Distributed Complexity of P_k-Freeness: Decision and Certification](https://doi.org/10.4230/LIPIcs.ISAAC.2025.51)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1602 — The most interesting question that remains open is to determine the deterministic query complexity of finding a king in an n-vertex tournament.

A king in a tournament is a vertex that can reach every other vertex along a directed path of at most two edges. The graph is accessed by queries revealing the direction of individual edges. Every tournament has a king, so the challenge is to find one while inspecting as few edges as possible. The source asks for the deterministic query complexity, reporting an O(n^(3/2)) algorithm and an Ω(n^(4/3)) lower bound. Closing this gap would quantify the information needed to locate a globally influential vertex in a completely oriented graph.

[Read in atlas](index.html#TCS-1602) · [Hardness of Finding Kings and Strong Kings](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1936 — Does n2 -Ramsey belong to TFAP?

The Ramsey search problem receives a succinctly represented graph on 2^n vertices and seeks a clique or independent set of size n/2. Ramsey's theorem guarantees a solution, placing the task in the landscape of total search problems. The question asks whether this problem belongs to TFAP, a class designed to capture search tasks with abundant solutions. The source also proposes the weaker target of finding a homogeneous set of size n/10. Membership would connect Ramsey search to abundance-based principles and yield consequences for oracle separations from classes whose hard instances can have very few solutions.

[Read in atlas](index.html#TCS-1936) · [Total NP Search Problems with Abundant Solutions](https://doi.org/10.4230/LIPIcs.ITCS.2024.75)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2029 — In the other direction, we leave open whether FBPP ⊂ FBPPnegl or whether the two classes are incomparable.

For a relation, an algorithm may output any answer satisfying the input-output specification rather than one uniquely determined value. This makes the precise convention for reducing error more consequential than it is for ordinary decision problems. The source compares FBPP with a version requiring negligible error and gives a relation separating the classes in one direction. The remaining question is whether an inclusion holds in the other direction or whether the two classes are incomparable. An answer would clarify which amplification intuitions remain valid when success means producing an arbitrary valid output.

[Read in atlas](index.html#TCS-2029) · [A Qubit, a Coin, and an Advice String Walk into a Relational Problem](https://doi.org/10.4230/LIPIcs.ITCS.2024.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2093 — It is an open problem to give an unconditional depth hierarchy theorem that separates NDepth [a log n] from NDepth [b log n] for any […]

Circuit-depth hierarchies ask whether allowing more layers necessarily lets a circuit family compute additional functions. Here the source's NDepth notation refers specifically to uniform NAND formulas of logarithmic depth. The question asks for an unconditional separation between depth bounds with any two distinct constant coefficients of log n. The paper obtains a conditional hierarchy useful for its SAT lower-bound argument, but that assumption-dependent result is weaker than the requested theorem. Removing the assumption would sharpen the understanding of how much computational power each constant-factor increase in uniform formula depth provides.

[Read in atlas](index.html#TCS-2093) · [Towards Stronger Depth Lower Bounds](https://doi.org/10.4230/LIPIcs.ITCS.2024.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2215 — Can we prove a real version of Toda’s theorem [30]?

Toda's theorem in discrete complexity relates alternating quantifiers to counting power. This source asks for an analogous relationship among real-algebraic complexity classes. The proposed target is to contain fixed levels of alternating real quantification in an existential real theory enhanced with summation operators. The exact operator language matters because unrestricted real exponentiation would change the setting substantially. A positive result would organize several real-feasibility hierarchies under one strengthened existential framework and illuminate the role of counting-like operations over real computation.

[Read in atlas](index.html#TCS-2215) · [The Existential Theory of the Reals with Summation Operators](https://doi.org/10.4230/LIPIcs.ISAAC.2024.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2244 — Does Constant Degree Hypothesis hold?

The Constant Degree Hypothesis concerns restricted circuits that combine bounded-fan-in conjunctions with two layers of modular counting gates. For fixed parameters d and m and prime p, it rules out subexponential-size AND_d composed with MOD_m and MOD_p circuits computing conjunctions of arbitrarily many inputs. The source asks whether this circuit lower-bound hypothesis holds. It connects the hypothesis to algorithms for satisfiability and equivalence of circuits over finite nilpotent algebras. A proof would justify an important assumption in that algebraic complexity program, while a counterexample would reveal unexpectedly efficient interactions between modular gates.

[Read in atlas](index.html#TCS-2244) · [Circuit Equivalence in 2-Nilpotent Algebras](https://doi.org/10.4230/LIPIcs.STACS.2024.45)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2319 — Can we reduce explicit construction problems to solving NC03 -Avoid?

Range avoidance asks for an output string outside the image of a Boolean circuit with more output bits than input bits. In NC0_3-Avoid, each output bit depends on at most three input bits. The source asks whether explicit construction problems can be reduced to this highly local version of range avoidance. General avoidance is already connected to constructing objects such as rigid matrices and functions requiring large formulas. Establishing comparable reductions at locality three would locate the computational power of a sharply restricted search task; the accompanying alternative is that this case admits a polynomial-time algorithm.

[Read in atlas](index.html#TCS-2319) · [Range Avoidance for Constant Depth Circuits: Hardness and Algorithms](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.65)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2331 — Is there a BPPNP certification algorithm that returns certificates of length O(Cert(f ))?

A certificate for a Boolean function at an input is a set of fixed input bits that forces the function's value. The quantity Cert(f) is the largest minimum certificate size over all inputs. The source gives a randomized polynomial-time algorithm with an NP oracle that finds certificates of size O(Cert(f)^5). The question asks whether the same computational resources suffice to return certificates of length O(Cert(f)). This would make certification nearly optimal relative to the function's global certificate complexity, without requiring structural assumptions such as monotonicity.

[Read in atlas](index.html#TCS-2331) · [Certification with an NP Oracle](https://doi.org/10.4230/LIPIcs.ITCS.2023.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2333 — Is every PLS-complete problem downward self-reducible?

A search problem is downward self-reducible if solutions can be computed efficiently using an oracle only on strictly smaller instances. PLS contains total search problems whose solutions can be found through a finite process of improving a locally evaluated objective. The source proves downward self-reducibility for familiar PLS-complete problems and places downward self-reducible total search in PLS. It asks whether every PLS-complete problem enjoys this recursive property. The issue is that general completeness reductions need not preserve input length, so self-reducibility cannot simply be transferred through an arbitrary reduction.

[Read in atlas](index.html#TCS-2333) · [Downward Self-Reducibility in TFNP](https://doi.org/10.4230/LIPIcs.ITCS.2023.67)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2425 — Notably, it is still an open question if SZK is closed under ≤Ptt reducibility.

Statistical zero knowledge captures problems that can be verified interactively while revealing essentially no additional information even to a powerful observer. This project asks whether the class SZK is closed under polynomial-time truth-table reductions. Such a reduction prepares its oracle questions without depending on their answers and then combines the answers using polynomial-time computation. The source discusses closure under more restricted ways of combining answers, which do not automatically give this general closure property. A resolution would clarify whether nonadaptive composition preserves statistical zero knowledge across the full range of efficient postprocessing.

[Read in atlas](index.html#TCS-2425) · [Kolmogorov Complexity Characterizes Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.ITCS.2023.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2434 — Establishing a super-polynomial separation between randomness and pseudo-determinism remains open for Parity decision trees.

A parity decision tree queries the XOR of a chosen subset of input bits at each step. For a search relation, a randomized algorithm may return different valid answers, while a pseudodeterministic algorithm must usually return one canonical answer for each input. The question asks for a superpolynomial separation between the query costs of these two forms of computation. The source establishes other separations involving deterministic and pseudodeterministic parity trees, but those do not resolve this comparison. Such an example would show that requiring reproducible output can be dramatically more expensive even when each query accesses a global parity.

[Read in atlas](index.html#TCS-2434) · [Query Complexity of Search Problems](https://doi.org/10.4230/LIPIcs.MFCS.2023.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2464 — For every d ∈ N, ε ∈ (0, 1) for all large enough n, if X is samplable by a d-local function and is ε-close […]

A d-local sampler produces each output bit from at most d independent random input bits. The conjecture considers samplers whose output is close in statistical distance to the uniform distribution on strings with allowed Hamming weights S. It predicts that, for fixed locality and sufficiently large dimension, the output must also be close to one of a short list of simple symmetric distributions. These are concentrated on all-zero strings, all-one strings, their pair, even weights, odd weights, or the full Boolean cube. Proving this structural restriction would sharply characterize which symmetric distributions constant-locality classical circuits can approximately generate.

[Read in atlas](index.html#TCS-2464) · [Sampling and Certifying Symmetric Functions](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2532 — Can one prove circuit lower bounds from the assumption that a (uniform) computationally-secure IO exists?

Indistinguishability obfuscation hides which of two equivalent circuit implementations was supplied to an observer. The cited work shows that obfuscation secure against nonuniform polynomial-size circuits implies nontrivial circuit lower bounds. This project asks whether an analogous implication follows when security is assumed only against uniform efficient algorithms. Nonuniform attackers can use input-length-dependent advice, so the existing security hypothesis is stronger than the proposed replacement. Establishing lower bounds from uniform security would connect a more algorithmic cryptographic assumption with structural limitations on small circuits.

[Read in atlas](index.html#TCS-2532) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2537 — Is the total search version of UniqueTarski in the class UEOPL (Unique-EOPL) [6]?

Tarski-style search finds a fixed point of an order-preserving map on a finite lattice. The source asks whether the total-search version of UniqueTarski belongs to UEOPL. A total formulation must specify valid outputs even when an input fails the intended uniqueness promise. A containment would connect this fixed-point task with search problems governed by a unique improving path. The saved excerpt does not define the map representation or violation witnesses, so the total version cannot be replaced by simply promising that exactly one fixed point exists.

[Read in atlas](index.html#TCS-2537) · [Reducing Tarski to Unique Tarski (In the Black-Box Model)](https://doi.org/10.4230/LIPIcs.CCC.2023.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2681 — As mentioned in the introduction, it remains open whether UEOPL = EOPL.

EOPL studies total search through implicitly represented paths equipped with a potential that increases along each path. UEOPL imposes a uniqueness structure, with suitable witnesses allowed when that structure fails. The source identifies EOPL with the intersection of PLS and PPAD and asks whether UEOPL has the same power. A first proposed step is a separation in the black-box model, where algorithms learn the paths through queries. Understanding the role of uniqueness would help classify natural problems in UEOPL and assess whether they could be complete for the broader intersection.

[Read in atlas](index.html#TCS-2681) · [Further Collapses in TFNP](https://doi.org/10.4230/LIPIcs.CCC.2022.33)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2914 — Namely, can one find a distribution that cannot be sampled in AC0 but can be sampled by ROBPs?

Sampling complexity measures the resources needed to generate a probability distribution from independent random bits. This problem compares constant-depth Boolean circuits with oblivious read-once branching programs, which process their random inputs sequentially with limited memory. The source asks for a distribution efficiently sampled by such branching programs that cannot be sampled in AC0. It suggests constructing an extractor or disperser for AC0 sources that itself has a small-width branching program. A separation in this direction would distinguish the generative power of shallow parallel computation from that of a memory-limited sequential process.

[Read in atlas](index.html#TCS-2914) · [The Space Complexity of Sampling](https://doi.org/10.4230/LIPIcs.ITCS.2022.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3095 — We conjecture that even G3 might be tractable, but again the only known general upper bound is PSPACE.

In the unordered CNF game, two players alternately choose unassigned variables and give them Boolean values. One player wants the final formula to be true, while the other wants it false. The problem G3 restricts every clause to at most three literals and asks which player has a winning strategy. The source conjectures tractability for this width, while reporting only a general PSPACE upper bound and algorithms under additional restrictions. A classification would locate the transition from manageable local clauses to difficult strategic interaction in games where the order of assignments is itself a choice.

[Read in atlas](index.html#TCS-3095) · [6-Uniform Maker-Breaker Game Is PSPACE-Complete](https://doi.org/10.4230/LIPIcs.STACS.2021.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3181 — More difficult question: can we prove a lower bound on random ∆-CNF formulas?

An unsatisfied-clause search problem receives an assignment to an unsatisfiable CNF formula and must identify a clause that it falsifies. The source studies branching programs for this task with a controlled number of repeated variable queries. Its lower-bound construction uses a specially modified formula, leaving open whether comparable bounds hold for random constant-width CNFs. Random formulas are a natural candidate because their hardness should not depend on an artificial amplification gadget. Establishing such bounds would extend the connection between restricted branching programs and proof complexity to a canonical probabilistic family of unsatisfiable instances.

[Read in atlas](index.html#TCS-3181) · [Branching Programs with Bounded Repetitions and Flow Formulas](https://doi.org/10.4230/LIPIcs.CCC.2021.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3228 — Is Sparse Complexity complete for SAPEPP?

SAPEPP consists of sparse total search tasks defined by a fixed polynomial-time map that stretches its input length. Given the length in unary, the task is to construct a string outside that map's image. The selected question asks whether Sparse Complexity is complete for SAPEPP, as explicitly proposed in the source. That candidate seeks explicit truth tables for Boolean functions requiring large circuits. Completeness would organize several explicit-construction challenges around one representative task, while the sparse input format makes standard methods of transferring hardness less straightforward.

[Read in atlas](index.html#TCS-3228) · [Total Functions in the Polynomial Hierarchy](https://doi.org/10.4230/LIPIcs.ITCS.2021.44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3308 — For example, here is an open question that we have not addressed: for (say) the game Hex, does there necessarily exist a polynomial-size circuit that […]

Strategy-stealing arguments can prove that a player has a winning strategy without revealing how to execute it. For Hex, the source asks whether optimal play can always be represented by a circuit whose size is polynomial in the board size. The circuit would take a position and supply the appropriate move, even if constructing that circuit were computationally difficult. This separates the existence of a compact strategy from the algorithmic task of discovering one. Understanding this distinction would clarify how much constructive content can be extracted from nonconstructive proofs about combinatorial games.

[Read in atlas](index.html#TCS-3308) · [Strategy-Stealing Is Non-Constructive](https://doi.org/10.4230/LIPIcs.ITCS.2020.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3509 — Is Tarski in CLS (or in EOPL)?

Tarski's fixed-point theorem guarantees a fixed point for an order-preserving map on a suitable lattice. The source asks whether the associated computational search problem lies in CLS or EOPL. These classes organize total search problems through continuous local improvement or structured potential-guided paths. A containment would connect monotone fixed points with algorithmic approaches used for equilibrium and local optimization. The saved excerpt does not state the finite encoding or violation outputs, so the computational Tarski problem must be defined separately from the unrestricted mathematical existence theorem.

[Read in atlas](index.html#TCS-3509) · [Tarski’s Theorem, Supermodular Games, and the Complexity of Equilibria](https://doi.org/10.4230/LIPIcs.ITCS.2020.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3568 — Is there a total function g : {0, 1}m → {0, 1} such that BPP(Xor ◦ g n ) ≥ Ω(n log n · BPP(g)) […]

Composing parity or majority with n copies of a function creates a natural randomized query algorithm that solves each copy separately. Reducing the chance of any harmful error introduces a logarithmic amplification overhead. The question asks for a total Boolean function g for which this overhead is necessary, giving complexity Ω(n log n times BPP(g)). The source demonstrates the phenomenon with partial functions, but the promise-free requirement resists those constructions. A total-function example would show that the extra logarithm reflects an inherent cost of reliable composition, even when every possible input must be handled.

[Read in atlas](index.html#TCS-3568) · [When Is Amplification Necessary for Composition in Randomized Query Complexity?](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2020.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3685 — We conjecture that getting a much better agreement with Mn , say 1/2 + 1/ poly(n), or even 2 1/2 + 2−o(log n) , requires […]

Boolean formula lower bounds measure how large a tree of logical operations must be to compute a function. This source studies a generalized Andreev function whose components use majority and asks how hard it is to approximate on random inputs. A simple linear-size formula already achieves a small advantage over random guessing, so extremely strong average-case hardness is impossible. The conjecture is that substantially improving that advantage requires almost cubic formula size. A proof would connect worst-case formula lower bounds with a sharper understanding of how approximation quality increases with available computation.

[Read in atlas](index.html#TCS-3685) · [Cubic Formula Size Lower Bounds Based on Compositions with Majority](https://doi.org/10.4230/LIPIcs.ITCS.2019.35)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3718 — Formally, is NP 6⊂ SIZE[nk ] for all k equivalent to (NP ⊂ P/poly =⇒ PH ⊂ i.o.-NP/n )?

Fixed-polynomial circuit lower bounds for NP assert that no single exponent k bounds circuit size for every NP problem. The source asks whether obtaining all these lower bounds is equivalent to a particular conditional collapse of the polynomial hierarchy. The proposed collapse assumes NP has polynomial-size circuits and places PH in nondeterministic polynomial time with linear advice on infinitely many lengths. Related equivalences in the paper connect lower bounds to Karp-Lipton-style implications for other classes. An equivalence here would explain whether two apparently different routes toward stronger NP circuit lower bounds are fundamentally the same.

[Read in atlas](index.html#TCS-3718) · [Relations and Equivalences Between Circuit Lower Bounds and Karp-Lipton Theorems](https://doi.org/10.4230/LIPIcs.CCC.2019.30)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3743 — Can we show that either NQP 6⊆ P/poly or MCSP 6∈ ACC0 ?

The Minimum Circuit Size Problem receives a truth table and asks whether its function has a circuit smaller than a given threshold. The source proves lower bounds for this problem against constant-depth circuits with prime-modulus gates. It asks for a stronger disjunction: either nondeterministic quasipolynomial time lacks polynomial-size circuits, or MCSP is outside ACC0. ACC0 permits modular gates beyond one fixed prime, making this a substantial extension of the proved result. The proposed connection would let progress on circuit minimization force a lower bound for a broader computational class, or vice versa.

[Read in atlas](index.html#TCS-3743) · [AC^0(p) Lower Bounds Against MCSP via the Coin Problem](https://doi.org/10.4230/LIPIcs.ICALP.2019.66)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3832 — Is SZK ⊆ ZPPMKTP , or equivalently, is Entropy Approximation in ZPPMKTP ?

Statistical zero knowledge captures problems admitting protocols that reveal essentially no extra statistical information to the verifier. The source asks whether SZK is contained in zero-error randomized polynomial time with an MKTP oracle. It gives Entropy Approximation in the same oracle class as an equivalent target. A positive answer would connect entropy estimation and zero-knowledge complexity to a concrete minimum-description-length decision problem. The oracle is an essential resource in the question, and the saved excerpt does not supply the encoding and approximation conventions needed to make the equivalence self-contained.

[Read in atlas](index.html#TCS-3832) · [Minimum Circuit Size, Graph Isomorphism, and Related Problems](https://doi.org/10.4230/LIPIcs.ITCS.2018.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3862 — The question of whether search-ZK has complete problems in the computational and statistical setting remains open.

Zero-knowledge protocols are usually framed around deciding whether a statement is true. Search zero knowledge instead concerns interactions that produce a valid solution while controlling what additional information is revealed. The selected problem asks whether these search classes have complete problems in either the computational or statistical security setting. A complete problem would serve as a universal representative to which other search-zero-knowledge tasks can be reduced under suitable definitions. Finding one would organize the new model and help transfer general techniques from the better-developed theory of decision zero knowledge.

[Read in atlas](index.html#TCS-3862) · [Brief Announcement: Zero-Knowledge Protocols for Search Problems](https://doi.org/10.4230/LIPIcs.ICALP.2018.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3873 — Or is it impossible, which could solve the open question [11] of separating SDDs and d-SDNNFs?

Sentential decision diagrams and deterministic structured DNNFs are circuit languages for storing Boolean knowledge through organized variable decompositions. The 2018 passage points to a possible separation between their succinctness, meaning the size needed to represent the same functions. Such a separation would explain whether the additional organization of sentential decisions has an unavoidable storage cost. The paper approaches the issue through connections between circuit width and structural restrictions. The excerpt's opening alternative refers to a missing construction, so the exact family and size bound remain unspecified even though the intended comparison between representation languages is visible.

[Read in atlas](index.html#TCS-3873) · [Connecting Width and Structure in Knowledge Compilation](https://doi.org/10.4230/LIPIcs.ICDT.2018.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3886 — Indeed, whether ∃ · BPP = MA remains an open question [11].

Merlin–Arthur verification combines a classical witness with an efficient randomized check. Applying an existential quantifier to an ordinary BPP language imposes an additional bounded-error condition on every witness-input pair. In an MA protocol, by contrast, unsuccessful witnesses on a yes-instance may have intermediate acceptance probabilities. This question asks whether those different promise conventions nevertheless define the same class. The distinction matters when building classical or quantum verification hierarchies, because moving quantifiers across probabilistic tests can silently strengthen the requirements on a verifier.

[Read in atlas](index.html#TCS-3886) · [Quantum Generalizations of the Polynomial Hierarchy with Applications to QMA(2)](https://doi.org/10.4230/LIPIcs.MFCS.2018.58)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3962 — Does SAT ∈ P/poly imply that NP ⊆ ZPPMCSP ?

The Minimum Circuit Size Problem asks whether an explicitly given truth table has a sufficiently small circuit. The saved question assumes SAT has polynomial-size circuits and asks whether NP then lies in zero-error randomized polynomial time with an MCSP oracle. This connects a nonuniform upper-bound hypothesis with the power of a concrete circuit-minimization oracle. A positive implication would clarify how much algorithmic usefulness follows from small circuits existing. The excerpt does not specify oracle encoding or reduction conventions, so those details remain needed for a fully formal class inclusion.

[Read in atlas](index.html#TCS-3962) · [The Power of Natural Properties as Oracles](https://doi.org/10.4230/LIPIcs.CCC.2018.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4076 — We leave open the question of whether MLP gates (of any type) can polynomially simulate monotone real circuits. n I Theorem 19.

Monotone linear-programming circuits use gates defined through linear-programming feasibility to compute partial Boolean functions. The source compares their expressive efficiency with monotone real circuits. It proves a separation in one direction and leaves open whether suitable linear-programming gates can simulate every monotone real circuit with polynomial overhead. The direction of simulation matters because a model can outperform another on one task without containing it efficiently on all tasks. Answering the question would clarify the hierarchy of monotone computation models that connect optimization formulations with proof-complexity lower bounds.

[Read in atlas](index.html#TCS-4076) · [Representations of Monotone Boolean Functions by Linear Programs](https://doi.org/10.4230/LIPIcs.CCC.2017.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4205 — What is the maximum gap, if any, between U -invariant [depth d] formula size and non-invariant [depth d] formula size?

A Boolean function may be invariant under a group of transformations even when the formula computing it does not visibly respect that symmetry. The source studies formulas whose syntax is invariant under a subspace U acting by toggling input negations. It asks how much larger the smallest U-invariant formula can be than an unrestricted formula for the same function, including comparisons at fixed depth. Its parity lower bounds show that imposing syntactic symmetry can make sharper analysis possible. Determining the largest gap would reveal whether those stronger bounds measure inherent computation or a significant cost of enforcing symmetry.

[Read in atlas](index.html#TCS-4205) · [Subspace-Invariant AC^0 Formulas](https://doi.org/10.4230/LIPIcs.ICALP.2017.93)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4219 — What are the tradeoffs, if any, between the number of gates and the number of ancilla bits?

A reversible Boolean circuit implements a permutation of bit strings using gates from a specified reversible gate set. Ancilla bits provide temporary workspace, and the classification in the source treats their availability as free when deciding which transformations are expressible. This question asks how the number of gates needed for a transformation trades off against the number of ancillas allowed. The source also seeks constructions approaching the circuit-size limits suggested by counting arguments. Such tradeoffs would turn an expressibility classification into a resource-sensitive account of reversible computation, where both circuit length and workspace matter.

[Read in atlas](index.html#TCS-4219) · [The Classification of Reversible Bit Operations](https://doi.org/10.4230/LIPIcs.ITCS.2017.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4268 — Is there evidence that Gap MCSP has intermediate complexity when is a fixed constant, similar to the evidence that we present for the case when […]

Gap MCSP approximates the smallest circuit computing a function presented by its full truth table. In the source's parameterization, the permitted multiplicative error is N^(1-epsilon), where N is the truth-table length. The paper gives evidence for intermediate complexity when epsilon tends to zero, under modest cryptographic assumptions. The question asks for comparable evidence when epsilon is a fixed positive constant and the approximation is therefore more accurate. This would broaden the case that natural circuit-minimization problems can lie between efficient computation and NP-hardness.

[Read in atlas](index.html#TCS-4268) · [New Insights on the (Non-)Hardness of Circuit Minimization and Related Problems](https://doi.org/10.4230/LIPIcs.MFCS.2017.54)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4412 — Can gate elimination prove non-linear bounds here?

Gate elimination proves circuit lower bounds by restricting inputs and counting the gates that each restriction removes. The source examines limitations of this method for ordinary Boolean functions and then turns to linear maps from n bits to n bits. It asks whether gate elimination can prove superlinear lower bounds for explicit linear maps. A further restricted version permits only linear circuit operations and linear substitutions in the argument. The distinction matters because the source's existing obstruction gadgets are nonlinear and do not automatically explain the power of elimination in this algebraically structured setting.

[Read in atlas](index.html#TCS-4412) · [On the Limits of Gate Elimination](https://doi.org/10.4230/LIPIcs.MFCS.2016.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4466 — We leave open the question whether one can come up with an explicit and efficient transformation from any formula to a formula with few negations.

Negation complexity measures how many NOT gates a Boolean formula or circuit uses. The source develops structural decompositions for formulas with few negations and transformations that reduce negations in related circuit models. It asks for an explicit, efficient transformation taking an arbitrary formula to a formula with few negations. Known existence arguments rely on a short monotone threshold construction that does not directly provide the desired explicit procedure. A constructive transformation would make negation-reduction results algorithmically usable while preserving the tree structure that distinguishes formulas from circuits with shared subcomputations.

[Read in atlas](index.html#TCS-4466) · [Negation-Limited Formulas](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.850)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4468 — The best separation between subcube partition complexity and query complexity remains open, even in the deterministic case.

A subcube partition divides all Boolean inputs into monochromatic pieces, each specified by fixing some coordinates. Unlike a decision tree, the pieces need not arise from one sequential hierarchy of queries. The source separates this partition model from randomized decision trees and asks for the strongest possible gap between their complexities. Even the comparison with deterministic query complexity is included in the question. Determining the extremal separation would quantify how much harder it is to discover an input's certificate adaptively than merely to exhibit a globally consistent collection of certificates.

[Read in atlas](index.html#TCS-4468) · [Separating Decision Tree Complexity from Subcube Partition Complexity](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.915)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4746 — Enumerating Error Bounded Polytime Algorithms Through Arithmetical Theories — Explicit open question on PDF page 2

A randomized polynomial-time program belongs to BPP only if its answer is reliably biased toward correctness on every input. That semantic requirement is harder to recognize than a syntactic time bound. This problem asks whether there is an effective enumeration of algorithms covering exactly the languages in BPP. The cited work uses arithmetical theories to study how error guarantees can be expressed and justified. A successful characterization would connect feasible randomized computation with formal languages whose programs come with uniformly controlled error behavior.

[Read in atlas](index.html#TCS-4746) · [Enumerating Error Bounded Polytime Algorithms Through Arithmetical Theories](https://doi.org/10.4230/LIPIcs.CSL.2024.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4786 — Synergy Between Circuit Obfuscation and Circuit Minimization — Explicit open question on PDF page 3

The minimum circuit size problem asks whether a truth table can be implemented by a Boolean circuit below a given size threshold. A small circuit supplies an efficiently checkable witness, placing the problem in NP when input length is measured by the full truth table. The selected passage highlights the unresolved classification between efficient randomized algorithms and NP-hardness. It also notes that an efficient algorithm would enable average-case inversion of candidate one-way functions through known reductions. Understanding this problem would connect circuit minimization, obfuscation, and the computational assumptions that make cryptography possible.

[Read in atlas](index.html#TCS-4786) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4960 — Theoretical Limitations of Multi-Layer Transformer — Open Question 2

The source analyzes the representational limits of multilayer decoder-only Transformers using communication-complexity methods. Its lower bounds constrain constant-depth architectures solving carefully defined compositional tasks. The selected question asks for a polynomial lower bound on the depth needed by Transformers. The authors allow either an unconditional result or one based on established computational complexity conjectures. This would identify tasks whose sequential compositional structure cannot be absorbed into a shallow attention architecture without violating the model's other resource constraints.

[Read in atlas](index.html#TCS-4960) · [Theoretical Limitations of Multi-Layer Transformer](https://doi.org/10.1109/FOCS63196.2025.00136)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4961 — Range Avoidance and Remote Point: New Algorithms and Hardness — Open Problem 1

Range avoidance asks for a string outside the outputs of a circuit that maps n input bits to a longer string. The selected question restricts each output bit to depend on at most k inputs and sets output length to n^(1+epsilon). The source obtains subexponential algorithms with an exponent depending on locality and stretch. It asks whether the running time can be improved to 2^(n^o(1)) for some positive epsilon. Reaching this much faster scale would help determine the search complexity of local range avoidance and its connections to circuit lower bounds.

[Read in atlas](index.html#TCS-4961) · [Range Avoidance and Remote Point: New Algorithms and Hardness](https://doi.org/10.4230/LIPIcs.ITCS.2026.79)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4988 — An Oracle with no UP-Complete Sets, but NP = PSPACE — Explicit open question on PDF page 3

TFNP consists of search problems with efficiently checkable solutions whose existence is guaranteed for every input. This project asks whether the entire class has a complete problem under the intended efficient search reductions. Such a problem would represent the difficulty of all total NP search tasks, rather than only a subclass with a particular existence principle. The source discusses oracle constructions and their connections with promise classes, which can expose barriers without settling the unrelativized question. A complete problem or a rigorous obstruction would reshape how total search problems are compared, including those studied as foundations for cryptography.

[Read in atlas](index.html#TCS-4988) · [An Oracle with no UP-Complete Sets, but NP = PSPACE](https://doi.org/10.4230/LIPIcs.MFCS.2024.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5149 — String Matching: Communication, Circuits, and Learning — Explicit open question on PDF page 4

String matching determines whether a pattern occurs as a contiguous part of a text. The cited work studies communication, circuit, and learning perspectives on that task. The saved passage leaves a threshold-circuit lower bound, or a sublinear-size construction, unresolved. A sharp result would explain how compactly matching can be represented when gates perform threshold comparisons. The excerpt does not specify depth, input partition, or the meaning of n, so the draft cannot promote the alternative into a general lower bound for unrestricted threshold circuits.

[Read in atlas](index.html#TCS-5149) · [String Matching: Communication, Circuits, and Learning](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.56)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5246 — Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem — Explicit open question on PDF page 1

Graph isomorphism asks whether a bijection between two vertex sets preserves adjacency. The saved introductory question asks whether this can always be decided in polynomial time. The cited CSP paper studies fractional homomorphisms and refinement hierarchies that provide related ways to compare graph structure. Understanding their power helps explain which structural information supports isomorphism testing. This entry is an inherited reference to the general graph-isomorphism question rather than a distinct new conjecture about the Sherali–Adams hierarchy, and it does not assert that the surrounding relaxation methods resolve it.

[Read in atlas](index.html#TCS-5246) · [Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem](https://doi.org/10.4230/LIPIcs.MFCS.2021.27)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5312 — Simple Circuit Extensions for XOR in PTIME — Explicit open question on PDF page 2

The Minimum Circuit Size Problem takes a Boolean truth table and asks whether some circuit below a specified size computes it. The selected passage asks whether this problem is NP-hard. The source studies this question through simple extensions of functions and compares total truth tables with partially specified ones. Hardness results for partial circuit minimization do not immediately extend because the corresponding total extension problems can become easy. Understanding this obstacle could clarify why minimizing unrestricted Boolean circuits has resisted the reductions that succeed for several specialized variants.

[Read in atlas](index.html#TCS-5312) · [Simple Circuit Extensions for XOR in PTIME](https://doi.org/10.4230/LIPIcs.STACS.2026.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5315 — Forrelation Is Extremally Hard — Conjecture 8

Forrelation measures the correlation of one Boolean function with the Fourier transform of another. The extremal problem promises that this quantity is exactly positive one or negative one and asks for its sign. The conjecture restricts the input functions to degree-d polynomials over F2 and predicts randomized query complexity n^(Ω(d)). A quantum algorithm can exploit the Fourier structure, while a classical algorithm can always learn the low-degree polynomials before computing the answer. The lower bound would show that the promise of a simple polynomial description does not remove the essential classical difficulty.

[Read in atlas](index.html#TCS-5315) · [Forrelation Is Extremally Hard](https://doi.org/10.4230/LIPIcs.ITCS.2026.72)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5342 — Direct Sums for Parity Decision Trees — Explicit open question on PDF page 4

A parity decision tree may query the XOR of any subset of its input bits. A direct sum theorem would say that computing k independent copies of a function costs k times the resources needed for one copy. The source asks whether such a perfect theorem holds for deterministic parity decision trees. Its proved bounds lose factors depending on the single-copy complexity or Fourier sparsity. The challenge is to rule out savings from parity queries that mix bits belonging to different copies, even though all k answers must ultimately be produced.

[Read in atlas](index.html#TCS-5342) · [Direct Sums for Parity Decision Trees](https://doi.org/10.4230/LIPIcs.CCC.2025.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5397 — New Sampling Lower Bounds via the Separator — Explicit open question on PDF page 4

For a uniformly random bit string, the Rank distribution records every prefix sum of its bits. Generating one sample therefore means producing a mutually consistent sequence of counts rather than answering one isolated rank query. The source asks whether polynomial-size AC0 circuits can sample this distribution. It proves sampling lower bounds for decision forests and notes a quasipolynomial-size shallow-circuit construction from related results. Resolving the polynomial-size case would compare the power of constant-depth sampling with the global dependencies in even a simple random walk of prefix sums.

[Read in atlas](index.html#TCS-5397) · [New Sampling Lower Bounds via the Separator](https://doi.org/10.4230/LIPIcs.CCC.2023.26)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5501 — Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem — Explicit open question on PDF page 1

The Minimum Circuit Size Problem asks whether a Boolean function given by its truth table has a circuit below a supplied size threshold. The saved passage identifies NP-hardness of this task as unresolved in its source. The cited work approaches the problem through sums-of-squares lower bounds. An NP-hardness result would connect circuit minimization with the broad landscape of efficiently verifiable search and decision problems. The excerpt does not specify the reduction convention, and lower bounds for a restricted relaxation do not themselves prove the requested classical hardness statement.

[Read in atlas](index.html#TCS-5501) · [Sum-Of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.CCC.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5593 — Does Looking Inside a Circuit Help? — Explicit open question on PDF page 4

A property of Boolean functions can be tested either from a circuit description or by querying the function as a black box. The Black-Box Hypothesis says that efficient access to the circuit's internal representation does not help decide such semantic properties, given an appropriate circuit-size bound. The source studies what follows if this hypothesis fails. For several kinds of counterexample, it derives nontrivial circuit satisfiability algorithms. Resolving the hypothesis would clarify whether inspecting an implementation offers a fundamental computational advantage over observing its behavior, with consequences for major complexity separations.

[Read in atlas](index.html#TCS-5593) · [Does Looking Inside a Circuit Help?](https://doi.org/10.4230/LIPIcs.MFCS.2017.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5617 — On the Complexity of Modulo-q Arguments and the Chevalley - Warning Theorem — Explicit open question on PDF page 3

PPAq classifies total search problems whose solutions are guaranteed by counting arguments modulo q. The source places problems from algebra, topology, and cryptography in these classes and proposes completeness as a possible classification for some of them. Its main theorem already proves PPAp-completeness for an explicit search problem based on the Chevalley-Warning theorem when p is prime. The imported passage is a broader research direction asking which additional natural problems capture the full power of modular counting principles. Developing those classifications would distinguish algorithmic difficulty arising from different moduli and connect abstract total-search classes to concrete mathematical tasks.

[Read in atlas](index.html#TCS-5617) · [On the Complexity of Modulo-q Arguments and the Chevalley - Warning Theorem](https://doi.org/10.4230/LIPIcs.CCC.2020.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5750 — On the Relative Power of Linear Algebraic Approximations of Graph Isomorphism — Explicit open question on PDF page 1

Graph isomorphism asks whether two graphs become identical after consistently renaming their vertices. The cited source compares the power of linear-algebraic methods that approximate this distinction. Its saved introductory passage mentions unresolved complexity questions but truncates the exact target. Understanding the relative strength of such methods could identify which structural differences they can detect and which remain invisible. The fragment does not identify the specific problem or algebraic hierarchy being questioned, so it cannot yet distinguish a general graph-isomorphism question from a narrower comparison of relaxations.

[Read in atlas](index.html#TCS-5750) · [On the Relative Power of Linear Algebraic Approximations of Graph Isomorphism](https://doi.org/10.4230/LIPIcs.MFCS.2021.37)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6006 — A Subexponential Algorithm for ARRIVAL — Explicit open question on PDF page 4

ARRIVAL describes a deterministic walk in a directed graph whose vertices alternate between two outgoing choices on successive visits. The decision task asks which designated destination the walk eventually reaches. The source notes efficiently verifiable certificates for either answer, placing the problem in NP intersect coNP. It improves exponential algorithms to a subexponential bound and gives a polynomial-time algorithm for almost acyclic graphs. The remaining project is to decide whether all instances can be solved in polynomial time without explicitly following a walk that may be exponentially long.

[Read in atlas](index.html#TCS-6006) · [A Subexponential Algorithm for ARRIVAL](https://doi.org/10.4230/LIPIcs.ICALP.2021.69)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6091 — NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD Circuits — Explicit open question on PDF page 3

The class E contains decision problems solvable in deterministic time exponential with a linear exponent. The selected question asks whether some problem in E requires depth-three AC0 circuits of size 2^(Ω(n)). These circuits use AND, OR, and NOT gates but have only three layers of computation. The source raises this lower-bound target while proving NP-hardness for minimization in a different OR-AND-MOD circuit model. It explains that natural attempts to extend that hardness result to depth-three AC0 would also establish the strong uniform circuit lower bound.

[Read in atlas](index.html#TCS-6091) · [NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD Circuits](https://doi.org/10.4230/LIPIcs.CCC.2018.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6139 — A Note on the Advice Complexity of Multipass Randomized Logspace — Explicit open question on PDF page 2

A randomized logspace machine has very little working memory, but its power also depends on how it accesses random bits. Allowing two-way access lets it revisit its random tape instead of consuming each bit once. The source asks whether this model can be simulated deterministically in subexponential time. Its results for machines making a controlled number of passes do not settle unrestricted two-way access. Understanding the difference would clarify how reusable randomness affects small-space computation and why conventional logspace derandomization techniques do not automatically apply.

[Read in atlas](index.html#TCS-6139) · [A Note on the Advice Complexity of Multipass Randomized Logspace](https://doi.org/10.4230/LIPIcs.MFCS.2016.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6168 — On the (Non) NP-Hardness of Computing Circuit Complexity — Explicit open question on PDF page 4

MCSP asks whether a function given by its truth table has a Boolean circuit below a specified size. The source investigates what standard NP-hardness reductions to MCSP would imply for circuit lower bounds. It conjectures that polynomial-time NP-hardness would force EXP to lack polynomial-size circuits, strengthening its proved consequence. It also conjectures that MCSP is not NP-hard under uniform AC0 reductions. These questions aim to explain why proving hardness for circuit minimization appears to require understanding the very circuit lower bounds that the problem measures.

[Read in atlas](index.html#TCS-6168) · [On the (Non) NP-Hardness of Computing Circuit Complexity](https://doi.org/10.4230/LIPIcs.CCC.2015.365)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6285 — Depth-First Search in Directed Planar Graphs, Revisited — Explicit open question on PDF page 3

UL consists of logarithmic-space computations with at most one accepting computation on each input. The cited passage asks whether this unambiguous class is closed under complement. Closure would mean that rejecting instances also admit an equally economical unambiguous decision procedure. The paper encounters the issue while defining functions and composing algorithms for planar depth-first search. The project addresses a structural complexity question whose answer affects how safely unambiguous subroutines can replace ordinary nondeterministic reachability tests.

[Read in atlas](index.html#TCS-6285) · [Depth-First Search in Directed Planar Graphs, Revisited](https://doi.org/10.4230/LIPIcs.MFCS.2021.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6488 — Winning the War by (Strategically) Losing Battles: Settling the Complexity of Grundy-Values in Undirected Geography — Open Question 4

The Grundy value of an impartial game contains more information than whether the current player can force a win. The imported question asks for a general efficient reduction from computing that value to determining a winner. The source exhibits a sharp separation for Undirected Geography, where winner determination is efficient but Grundy computation is PSPACE-complete. That result supplies a complexity-theoretic obstruction to the proposed general reduction. The project explains why composing individually tractable games may require information much harder to obtain than their separate win-loss outcomes.

[Read in atlas](index.html#TCS-6488) · [Winning the War by (Strategically) Losing Battles: Settling the Complexity of Grundy-Values in Undirected Geography](https://doi.org/10.1109/FOCS52979.2021.00119)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6496 — Polynomial-Time Pseudodeterministic Construction of Primes — Explicit open question on PDF page 3

The cited prime-construction paper uses relationships between pseudodeterminism and strong circuit lower bounds. Its saved passage discusses known lower bounds for a higher exponential-time class and begins a stronger unresolved target. Circuit-size growth at sub-half-exponential scales can influence which hardness assumptions suffice for constructive number theory. A sharper bound could strengthen the complexity foundations of pseudodeterministic algorithms. The extraction stops before the target class or conclusion is stated, so this record must not be mistaken for the paper's already-announced prime-construction result or a fully specified circuit lower-bound conjecture.

[Read in atlas](index.html#TCS-6496) · [Polynomial-Time Pseudodeterministic Construction of Primes](https://doi.org/10.1109/FOCS57990.2023.00074)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6712 — Can every polynomial-size Boolean circuit be replaced by a polynomial-size, logarithmic-depth circuit?

A polynomial-size Boolean circuit represents an efficient nonuniform computation, but its longest chain of dependent gates can be large. The question asks whether every such computation can be reorganized into logarithmic depth while retaining polynomial size. Logarithmic depth would permit much greater parallelism without allowing an excessive number of gates. Counting arguments and restricted circuit lower bounds do not settle this comparison for unrestricted Boolean circuits. Resolving it would determine whether polynomial-size circuits and the nonuniform version of NC1 have the same expressive power.

[Read in atlas](index.html#TCS-6712) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6714 — Are there polynomial-size logarithmic-depth general Boolean circuits for perfect matching?

Matching asks for edges with disjoint endpoints, with perfect matching requiring every vertex to be covered. Polynomial-time matching algorithms imply polynomial-size Boolean circuits for the decision problem. The question asks whether general circuits can achieve logarithmic depth as well. The cited source discusses a matching-size threshold and proves a strong depth lower bound when the circuit is required to be monotone. The project is to understand whether allowing negation permits substantially shallower matching computations, beyond the restrictions captured by that monotone lower bound.

[Read in atlas](index.html#TCS-6714) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6715 — Separate polynomial-size monotone circuits from superpolynomial monotone span-program size.

A monotone span program accepts an input when vectors enabled by its one-bits span a designated target vector over a field. A monotone Boolean circuit instead combines input bits using AND and OR gates. The question asks for functions with polynomial-size monotone circuits that require superpolynomial-size monotone span programs. The source discusses a separation in the opposite direction, so this asks whether the two models can be incomparable in efficiency. Such an example would expose a limitation of linear-algebraic representations even for functions having short purely monotone logical computations.

[Read in atlas](index.html#TCS-6715) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6716 — Separate ordinary and monotone span-program size for monotone functions.

Ordinary span programs may enable vectors using either positive or negative input literals. Monotone span programs use only positive literals, even when the function itself is monotone. The question asks for a monotone function with a polynomial-size ordinary span program but no polynomial-size monotone span program. The analogous distinction can be dramatic for Boolean circuits, but the source leaves it unsettled for span programs. A separation would show that negative tests can provide essential efficiency in linear-algebraic computation despite the monotonicity of the final answer.

[Read in atlas](index.html#TCS-6716) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6717 — Strengthen monotone perfect-matching circuit lower bounds to stretched exponential.

The perfect-matching function takes a graph's edge indicators and reports whether every vertex can be covered by disjoint edges. It is monotone because adding edges cannot destroy a perfect matching. The source presents a quasipolynomial monotone-circuit lower bound of the form m^(Ω(log m)). The question asks to strengthen this to 2^(Ω(m^epsilon)) for some positive constant epsilon. Reaching stretched-exponential size would substantially widen the demonstrated gap between ordinary polynomial-time matching algorithms and computations restricted to monotone gates.

[Read in atlas](index.html#TCS-6717) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6718 — Prove exponential lower bounds for weakly read-once nondeterministic branching programs.

A nondeterministic branching program accepts when some path consistent with the input reaches its accepting sink. The weakly read-once restriction requires variables to appear at most once on each consistent accepting path, while allowing repetition on inconsistent paths. The source asks for an exponential size lower bound against this model. It shows that permitting those inconsistent paths can make programs much smaller than more strictly read-once counterparts. A lower bound must therefore handle the extra structural freedom without treating every syntactic path as a possible computation.

[Read in atlas](index.html#TCS-6718) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6743 — Every nontrivial monotone property of k-vertex graphs requires Ω(k²) randomized adjacency queries for exact recognition.

A monotone graph property is preserved when edges are added, and a graph property ignores vertex labels. The randomized evasiveness conjecture asks whether every nontrivial such property on k vertices requires Ω(k squared) adjacency queries for exact recognition with bounded error. The algorithm must distinguish every yes-instance from every no-instance, including graphs differing by very few edges. This differs fundamentally from property testing, which allows a gap between valid graphs and graphs far from validity. A quadratic lower bound would say that randomness cannot avoid inspecting a constant fraction of potential edges in the worst case.

[Read in atlas](index.html#TCS-6743) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6747 — Is graph nonisomorphism in BPP?

Graph nonisomorphism asks whether two graphs cannot be matched by any relabeling that preserves adjacency. The question asks for a randomized polynomial-time algorithm with bounded error for this decision problem. Interactive protocols can certify nonisomorphism efficiently using help from an untrusted prover, but that assistance is absent in BPP. Since BPP is closed under complement, the same algorithmic question can be phrased for graph isomorphism. Resolving it would clarify whether randomization alone can efficiently handle a central structural comparison problem that has distinctive behavior among complexity-theoretic examples.

[Read in atlas](index.html#TCS-6747) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6817 — Is directed reachability solvable simultaneously in polynomial time and polylogarithmic space?

Directed reachability asks whether a path exists from a specified start vertex to a specified target. A graph search can solve it in polynomial time using substantial memory, while recursive reachability methods save memory at a time cost. The question asks for one algorithm that simultaneously uses polynomial time and only polylogarithmic space. Obtaining the two resource bounds in separate algorithms does not meet this requirement. The problem is a basic test of whether reachability can combine efficient exploration with an extremely small working memory.

[Read in atlas](index.html#TCS-6817) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6832 — Which inclusions among P, RP and NP are strict?

P consists of problems with deterministic polynomial-time algorithms, while RP permits randomized algorithms that can miss yes-instances but never falsely accept no-instances. Every RP algorithm can be viewed as an NP verification procedure by treating its random choices as a certificate. This gives the chain P contained in RP contained in NP. The question asks which of these inclusions are strict. The alternatives distinguish whether randomness adds power beyond deterministic computation and whether one-sided randomized search can capture the full strength of efficiently verifiable existence.

[Read in atlas](index.html#TCS-6832) · [Understanding Machine Learning: From Theory to Algorithms](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6934 — Prove superlinear unconditional SAT time lower bounds in robust unrestricted computation models; establish stronger exponential lower bounds.

SAT asks whether a Boolean formula admits a satisfying assignment. The source calls for unconditional superlinear time lower bounds in robust general computation models and ultimately stronger exponential bounds. Many known barriers depend on unproved hypotheses or restrictions on memory and algorithm structure. An unrestricted lower bound would directly demonstrate that a concrete fundamental problem requires more than near-input-reading work. The saved note intentionally states a research direction rather than one fixed exponent, so a finished card must select the encoding, machine model, and quantitative threshold it intends to resolve.

[Read in atlas](index.html#TCS-6934) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6977 — Prove that SAT requires more than near-linear time.

SAT asks whether a Boolean formula has a satisfying assignment. The selected question seeks an unconditional lower bound excluding algorithms whose running time stays near the input length. This is a weaker objective than excluding every polynomial-time algorithm, but it must still account for all algorithms in the chosen model. Restrictions on working space can support different lower bounds and should not be silently added to the question. Progress would establish a concrete limit on efficient satisfiability algorithms without needing to settle the full P versus NP problem.

[Read in atlas](index.html#TCS-6977) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6978 — Separate a given space bound from roughly the same time bound.

Time measures how many computational steps an algorithm takes, while space measures how much working memory it uses. A computation can reuse the same memory through a very long sequence of steps. The question seeks a problem solvable within a given space bound that cannot be solved within roughly the same time bound. A precise version must specify the machine model, the resource function, and what slack is allowed by roughly the same. Such a separation would capture a basic advantage of reusable memory that ordinary time and space hierarchy theorems do not directly compare.

[Read in atlas](index.html#TCS-6978) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6979 — Could P versus NP be independent of standard mathematical axioms?

P versus NP asks whether every efficiently verifiable decision problem can also be solved efficiently. The independence question concerns the possibility that a chosen mathematical axiom system proves neither equality nor inequality. This is a question about formal provability, distinct from proposing either an algorithm or a complexity lower bound. Any precise claim must name the axiom system and the assumptions made about its consistency or soundness. Investigating independence could identify limitations of the available foundations or proof methods, without treating the difficulty of existing approaches as evidence that independence must hold.

[Read in atlas](index.html#TCS-6979) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7129 — Can prime-implicate representations always be expressed as polynomial-size DNNF?

A prime-implicate representation lists the minimal clauses logically forced by a Boolean function. The 2002 compilation map asks whether every such representation has an equivalent DNNF of polynomially related size. DNNF permits disjunctions but restricts each conjunction to subcircuits using disjoint variable sets. The comparison asks whether compact logical consequences can always be reorganized into that decomposable structure without a superpolynomial size increase. This is a representation-size question measured against the supplied prime-implicate description; the historical table entry does not itself provide an efficient conversion algorithm or a current-status review.

[Read in atlas](index.html#TCS-7129) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7130 — Can prime-implicate representations always be expressed as polynomial-size deterministic DNNF?

This historical comparison starts from a Boolean function represented by all its prime implicates, the minimal clauses it entails. It asks whether an equivalent deterministic DNNF can always have size polynomial in that representation. Alongside variable-disjoint conjunctions, determinism requires alternative branches of each disjunction to have no common satisfying assignment. The additional condition makes this target stronger than merely finding a small decomposable circuit. A positive size comparison would limit the cost of arranging logical information into disjoint cases, while the saved source groups smooth and nonsmooth variants through their polynomial relationship.

[Read in atlas](index.html#TCS-7130) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7131 — Can prime-implicant representations always be expressed as polynomial-size deterministic DNNF?

A prime-implicant representation lists minimal conjunctions of literals sufficient to make a Boolean function true. The saved 2002 question asks whether these potentially overlapping witnesses always admit a polynomial-size deterministic DNNF representation. Each individual term has simple variable structure, but several terms can describe the same satisfying assignment. The challenge is therefore to organize the union into disjoint alternatives while retaining decomposability and avoiding excessive duplication. The input-size benchmark is the complete prime-implicant representation, and this historical succinctness comparison should not be silently replaced by a claim about arbitrary small DNF formulas or efficient compilation.

[Read in atlas](index.html#TCS-7131) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7132 — Is prime-implicate representation polynomially succinct relative to explicit model enumeration?

Explicit model enumeration lists every satisfying assignment of a Boolean function. The question recorded in the compilation map asks whether the function's prime-implicate representation is always polynomially bounded by that explicit description. Prime implicates encode the same function through minimal necessary clauses rather than through its individual models. The comparison measures whether switching between these views of the satisfying assignments can require a superpolynomial increase in representation size. Keeping the direction of the comparison matters: the historical entry starts with an explicit model list and asks about the size of its equivalent prime-implicate form.

[Read in atlas](index.html#TCS-7132) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819)
Existing status: `source_open` · Summary written: 2026-09-11

## Algorithms (41)

### TCS-6537 — Expected linear-time integer sorting for every word length

Integer sorting can inspect the bits of keys instead of treating them only as objects to compare. The question asks for one always-correct randomized word-RAM algorithm taking expected linear time for every permitted word length. The constant must remain uniform when keys occupy much more than logarithmically many bits. Ordinary radix sorting handles smaller universes but its number of passes can grow. This tests whether powerful word operations can completely remove the asymptotic overhead of ordering an arbitrary list of machine words.

[Read in atlas](index.html#TCS-6537) · [Integer sorting in O(n√(log log n)) expected time and linear space](https://doi.org/10.1109/SFCS.2002.1181890) · [Deterministic sorting in O(n log log n) time and linear space](https://www.sciencedirect.com/science/article/pii/S019667740300155X) · [Expected Linear Time Sorting for Word Size Ω(log² n log log n)](https://cs.au.dk/~gerth/papers/swat14sort.pdf) · [Integer models of computation and integer sorting](https://www.cs.cmu.edu/~15451-s25/slides/lecture03.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0388 — Can all pairwise sums X+Y be sorted in quadratic time?

Given two lists of n numbers, form every sum consisting of one number from each list. The task is to sort these quadratically many sums as quickly as possible. They have substantial inherited order, so they are not an arbitrary collection of unrelated values. The source distinguishes having few comparisons from implementing those comparisons with equally small total running time. Removing avoidable overhead would improve both structured sorting and geometric problems whose events are ordered by pairwise sums.

[Read in atlas](index.html#TCS-0388) · [The Open Problems Project](https://topp.openproblem.net/p41)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0946 — Does every hypergraph have a cut sparsifier with O(n/ε²) hyperedges?

A hypergraph cut counts the total weight of hyperedges meeting both sides of a vertex partition. A cut sparsifier replaces the hypergraph by a smaller weighted hypergraph that approximately preserves every cut at once. The question asks whether O(n/epsilon squared) hyperedges always suffice for multiplicative error epsilon. This matches the natural target from ordinary graphs, while a hyperedge can involve arbitrarily many vertices. The size measure counts hyperedges rather than their total incidence size, making the project specifically about how many distinct multiway interactions must be retained.

[Read in atlas](index.html#TCS-0946) · [Problem 91: Cut-Sparsification of Hypergraphs](https://sublinear.info/index.php?title=Open_Problems:91)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1141 — Can reachability diameter be approximated within a constant in near-linear time?

Reachability diameter measures the largest finite shortest-path distance in a directed graph. Unreachable ordered pairs are omitted so that disconnected directions do not make the answer automatically infinite. The question asks for a constant-factor estimate in near-linear time on every unweighted directed graph. Simple searches from arbitrary pivots can miss a long directed route. A successful method would summarize the extent of reachable routes without computing distances from every vertex or imposing strong connectivity.

[Read in atlas](index.html#TCS-1141) · [Revisiting Diameter in Directed Graphs](https://doi.org/10.4230/LIPIcs.ESA.2026.59)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0809 — Mincost flow in planar graphs

Minimum-cost flow routes a prescribed amount of material through capacitated edges while minimizing total cost. The saved question focuses on planar input graphs, where an embedding may constrain the structure of feasible routes. The aim is to understand how that restriction can improve exact optimization. A faster planar algorithm would benefit network tasks requiring both conservation constraints and careful cost accounting. The index does not specify directedness, supply conventions, numerical encoding, or the running-time target, so it cannot yet distinguish a strongly polynomial question from a dependence on capacity magnitudes.

[Read in atlas](index.html#TCS-0809) · [Algorithms for Optimization Problems in Planar Graphs](https://doi.org/10.4230/DagRep.3.10.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1292 — It is unknown whether there exists a deterministic algorithm to reconstruct bounded-degree graphs in o(n2 ) queries.

Hidden-graph reconstruction learns a graph by asking for shortest-path distances between chosen vertex pairs. This question assumes bounded maximum degree and seeks a deterministic algorithm using fewer than quadratically many queries. Extra restrictions such as bounded cutwidth give useful reconstruction algorithms in the source. Bounded degree alone does not expose the same global layout. The challenge is to choose informative probes without random sampling while ensuring that every possible edge and every absent edge can eventually be determined.

[Read in atlas](index.html#TCS-1292) · [Cutwidth Versus BFS-Width with Applications to Graph Reconstruction from Distance Queries](https://doi.org/10.4230/LIPIcs.SWAT.2026.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1338 — Set-system sparsifiers of size proportional to chain length

A sparsifier retains and reweights a few coordinates while approximately preserving every set’s total weight. The conjecture asks for a support bound proportional to chain length divided by ε². Chain length is measured through the union-closure, so even an incomparable collection of singleton sets can have large chain length. The published upper bound has extra logarithmic factors, which are precisely the remaining loss in the question. A resolution would establish whether this structural parameter completely controls multiplicative sparsification up to a universal constant.

[Read in atlas](index.html#TCS-1338) · [Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction](https://doi.org/10.4230/LIPIcs.ICALP.2026.44)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1617 — For any subcubic graph H, H-ISC is in P if and only if H is planar.

For a fixed graph H, induced-subdivision detection asks whether an input graph contains a subdivided copy of H as an induced subgraph. Extra edges between selected vertices are forbidden. The conjecture concerns patterns H of maximum degree three and predicts tractability exactly for planar patterns, assuming P differs from NP. Existing algorithms and hardness constructions motivate the proposed boundary. This would classify a natural family of pattern-detection problems by a geometric property of the fixed pattern itself.

[Read in atlas](index.html#TCS-1617) · [Induced Disjoint Paths Without an Induced Minor](https://doi.org/10.4230/LIPIcs.ICALP.2025.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1664 — We do not know yet if temporal cliques admit O(n) spanners, thus the latter result might not appear very decisive.

A temporal clique has an edge between every vertex pair, but each edge is available only at its assigned time. Paths must respect chronological order. The question asks whether a linear number of retained edges always suffices to preserve temporal connectivity. The source discusses logarithmic-factor upper bounds and structural reductions based on removable vertices. The difficulty is that complete static connectivity does not ensure that a small collection of edges supports all required time-respecting journeys.

[Read in atlas](index.html#TCS-1664) · [Dismountability in Temporal Cliques Revisited](https://doi.org/10.4230/LIPIcs.SAND.2025.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1934 — Does every n-node undirected graph have a constant-stretch shortestpaths preserving graph of aspect ratio poly(n)?

Edge-weight aspect ratio measures the spread between the largest and smallest positive weights in a graph. The source studies alternative weightings or representations that preserve shortest-path behavior while reducing this spread. The question asks whether every undirected graph admits the prescribed constant-stretch preservation with only polynomial aspect ratio. Near-exact preservation has obstructions that do not automatically exclude a constant-factor relaxation. The project tests whether weighted shortest-path algorithms can discard extreme numerical scales while retaining the routes they need.

[Read in atlas](index.html#TCS-1934) · [Are There Graphs Whose Shortest Path Structure Requires Large Edge Weights?](https://doi.org/10.4230/LIPIcs.ITCS.2024.12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2018 — Every submodular hypergraph admits a (1+ϵ)-sparsifier of size O(ϵ−2 n2 ), which is in fact a reweighted sub-hypergraph.

A submodular hypergraph assigns each hyperedge a flexible submodular cost for being split by a cut. A sparsifier retains and reweights hyperedges so that every cut value remains approximately correct. The conjecture proposes a quadratic-in-vertices size bound with inverse-squared accuracy dependence in the source's size measure. Preserving exponentially many cuts simultaneously is the main obstacle identified there. The project seeks a compression theorem extending beyond ordinary all-or-nothing hyperedge cuts to richer models used in optimization and learning.

[Read in atlas](index.html#TCS-2018) · [Cut Sparsification and Succinct Representation of Submodular Hypergraphs](https://doi.org/10.4230/LIPIcs.ICALP.2024.97)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2103 — For every integers t, r there exists a polynomial-time algorithm that, given an St,t,t -free and Kr -free vertex-weighted graph (G, w) computes the maximum […]

Maximum Weight Independent Set selects mutually nonadjacent vertices of maximum total weight. The conjecture restricts graphs by excluding both a fixed clique and a fixed long subdivided claw as induced subgraphs. For every fixed pair of forbidden patterns, it asks for a polynomial-time algorithm. The source already handles additional structural restrictions through decomposition techniques. Removing those extra assumptions would show that excluding large cliques together with one branching induced pattern suffices to control the global optimization problem.

[Read in atlas](index.html#TCS-2103) · [Max Weight Independent Set in Sparse Graphs with No Long Claws](https://doi.org/10.4230/LIPIcs.STACS.2024.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2247 — Is it true that all graphs of, say, bounded flip-width admit a linear-size dag compression?

A directed acyclic compression shares repeated pieces of a graph's adjacency structure. The cited work shows that several standard graph algorithms can run directly on such a compressed representation. The question asks whether bounded flip-width always guarantees a representation of linear size. Dense graphs make this meaningful because their explicit edge lists can be quadratic. The project seeks a structural reason why a broad dense graph class might support basic computation in time close to its vertex count.

[Read in atlas](index.html#TCS-2247) · [Faster Graph Algorithms Through DAG Compression](https://doi.org/10.4230/LIPIcs.STACS.2024.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2316 — Finally, we end this paper by leaving the biggest open problem concerning mim-width: Given a graph G, is there a polynomial-time algorithm that computes a […]

Mim-width measures induced matchings across the cuts of a branch decomposition. Many graph algorithms become efficient when a suitable small-width decomposition is supplied. The source asks whether one can recognize width at most one and construct such a decomposition in polynomial time. The alternative output must correctly certify that no width-one decomposition exists. This is a basic access problem for the parameter: structural algorithms are much less usable if their required decomposition cannot itself be found efficiently.

[Read in atlas](index.html#TCS-2316) · [Finding Induced Subgraphs from Graphs with Small Mim-Width](https://doi.org/10.4230/LIPIcs.SWAT.2024.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2822 — Even the complexity (P versus NP) of deciding whether a directed graph contains an (s, t)-path longer than distG (s, t) (the case of k […]

The directed Longest Detour problem asks whether a simple path from s to t exceeds the shortest-path distance by at least k edges. Even the first nontrivial case asks whether any s-to-t path is longer than a shortest one. The source leaves the polynomial-time versus NP-hard classification unresolved for this case on general directed graphs. Its positive results for planar directed graphs do not settle the unrestricted problem. Resolving the k=1 case would determine whether a seemingly tiny deviation from shortest paths already introduces the complexity associated with finding long simple paths.

[Read in atlas](index.html#TCS-2822) · [Detours in Directed Graphs](https://doi.org/10.4230/LIPIcs.STACS.2022.29)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3263 — Thus, if there are no k disjoint shortest paths, then computing k disjoint paths minimizing their total length in polynomial time is still an open […]

Several terminal pairs in an undirected graph need mutually vertex-disjoint connecting paths. This question minimizes their total length even when the individually shortest routes cannot be chosen disjointly. The source asks for polynomial-time algorithms for a fixed number of pairs at least three. Methods deciding whether disjoint individual shortest paths exist rely on structure that disappears when detours are permitted. The project studies how global congestion constraints alter length optimization once the ideal independent routes are incompatible.

[Read in atlas](index.html#TCS-3263) · [Using a Geometric Lens to Find k Disjoint Shortest Paths](https://doi.org/10.4230/LIPIcs.ICALP.2021.26)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3291 — This motivates the following natural question: is there a notion of spectral sparsification that generalizes cut sparsification in directed graphs?

Undirected spectral sparsifiers preserve all quadratic forms and therefore also preserve cut values. Directed graphs lack an immediately equivalent formulation with the same implication. The source asks for a useful notion of directed spectral sparsification that genuinely extends directed cut sparsification. It suggests preserving a family of one-sided difference energies and studies the role of graph balance. The project must identify both the right analytic quantity and sparse representations that preserve it, rather than simply reuse an undirected Laplacian definition.

[Read in atlas](index.html#TCS-3291) · [Sparsification of Directed Graphs via Cut Balance](https://doi.org/10.4230/LIPIcs.ICALP.2021.45)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3346 — Indeed, it is an open problem whether the running time for the hypergraph isomorphism problem can be improved to 2polylog ∣V ∣ ⋅ ∣H∣O(1) [2].

Hypergraph isomorphism compares set systems up to a relabeling of their underlying vertices. The saved question asks for running time quasipolynomial in the number of vertices and polynomial in the hypergraph's full size. Separating these two dependencies matters when many hyperedges are present over a comparatively small vertex set. Such an algorithm would extend efficient symmetry testing to richer relational objects. The excerpt does not define representation conventions or reproduce the cited baseline, so the requested asymptotic form is preserved without asserting which existing method is optimal.

[Read in atlas](index.html#TCS-3346) · [Graph Isomorphism in Quasipolynomial Time Parameterized by Treewidth](https://doi.org/10.4230/LIPIcs.ICALP.2020.103)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4261 — The following basic question is still open though: is there a lower bound of Ω(n3/2+ ) edges for some ∈ (0, 1] for 2-additive spanners […]

A two-additive spanner preserves every relevant shortest-path distance up to two extra edges. The fault-tolerant version must keep that guarantee after one edge or vertex failure in the source's model. The question asks for examples requiring polynomially more than the familiar three-halves-power edge scale. The source's stronger failure lower bounds do not automatically cover a single fault. The project seeks a concrete demonstration that just one possible failure substantially raises the storage cost of tight additive distance preservation.

[Read in atlas](index.html#TCS-4261) · [Preserving Distances in Very Faulty Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2017.73)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4417 — Is there an O(m)-time algorithm for the BP and BST problems?

A bottleneck path minimizes its largest edge weight instead of the sum of all weights. The analogous directed spanning-tree problem minimizes the heaviest edge needed to reach every vertex from a root. The question asks for linear-time algorithms for these two tasks. The source improves very slowly growing overhead factors but does not eliminate them. The project investigates whether threshold connectivity can expose the optimum without sorting weights or repeatedly reexamining a substantial part of the graph.

[Read in atlas](index.html#TCS-4417) · [Bottleneck Paths and Trees and Deterministic Graphical Games](https://doi.org/10.4230/LIPIcs.STACS.2016.27)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5637 — Computing Flows in Subquadratic Space — Explicit open question on PDF page 2

A graph flow can assign nonzero values to quadratically many edges, making full output storage intrinsically expensive. The narrower task asks only for the exact maximum-flow value or minimum-flow cost. The source asks whether weighted graphs permit this scalar answer in subquadratic space in the considered model. Approximate values and unweighted special cases provide partial benchmarks. The project seeks to exploit the small output while retaining enough information to certify an exact global optimum with limited working memory.

[Read in atlas](index.html#TCS-5637) · [Computing Flows in Subquadratic Space](https://doi.org/10.4230/LIPIcs.ICALP.2026.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5705 — Tight Bounds on Adjacency Labels for Monotone Graph Classes — Explicit open question on PDF page 4

Adjacency labels encode a graph so that two vertex labels alone determine whether their vertices are adjacent. The relevant source passage concerns hereditary small graph classes, whose total number of labeled graphs grows only factorially times exponentially. It asks whether every such class admits logarithmic-size labels. A counting bound limits overall information but does not automatically make that information locally decodable. The project explores whether this stronger growth restriction can restore compact representations after broader implicit-representation conjectures fail.

[Read in atlas](index.html#TCS-5705) · [Tight Bounds on Adjacency Labels for Monotone Graph Classes](https://doi.org/10.4230/LIPIcs.ICALP.2024.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5845 — A Polynomial Delay Algorithm Generating All Potential Maximal Cliques in Triconnected Planar Graphs — Explicit open question on PDF page 2

Treewidth measures how closely a graph can be organized into a tree of overlapping vertex bags. The selected question asks whether computing exact treewidth on planar graphs is polynomial-time solvable or NP-hard. The source develops a polynomial-delay enumeration algorithm for potential maximal cliques in triconnected planar graphs and uses it in exact treewidth computation. The number of objects enumerated can still be large, so this does not provide a general polynomial-time classification. The question contrasts with planar branchwidth, for which the related optimization problem has a polynomial-time algorithm.

[Read in atlas](index.html#TCS-5845) · [A Polynomial Delay Algorithm Generating All Potential Maximal Cliques in Triconnected Planar Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2025.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5926 — Treewidth Is NP-Complete on Cubic Graphs — Unresolved-question passage on page 12

Exact treewidth asks for the smallest possible maximum bag size, minus one, in a tree decomposition. The source proves NP-completeness on cubic graphs and on certain subgraphs of the three-dimensional grid. It separately emphasizes the unresolved classification for planar graphs. Planarity offers stronger global structure than bounded degree, and a polynomial-time algorithm for the related branchwidth parameter does not immediately transfer. Settling this case would determine whether two prominent graph decomposition measures differ fundamentally in their exact computational behavior on planar inputs.

[Read in atlas](index.html#TCS-5926) · [Treewidth Is NP-Complete on Cubic Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2023.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5969 — Efficient Recognition of Subgraphs of Planar Cubic Bridgeless Graphs — Unresolved-question passage on page 13

Three-edge-colorability asks whether the edges of a graph can receive three colors with different colors on every pair meeting at a vertex. The selected question asks for the computational complexity of this decision problem on planar graphs. The source studies a sufficient route through augmentation to a planar cubic bridgeless supergraph, where three-edge-colorability follows from the Four-Color Theorem. It also discusses a conjectured characterization for two-connected planar graphs of maximum degree three. A full classification would determine whether the remaining planar cases admit an efficient coloring test or conceal an NP-hard obstruction.

[Read in atlas](index.html#TCS-5969) · [Efficient Recognition of Subgraphs of Planar Cubic Bridgeless Graphs](https://doi.org/10.4230/LIPIcs.ESA.2022.62)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6150 — Graph Inference with Effective Resistance Queries — Explicit open question on PDF page 4

Effective-resistance queries reveal global electrical measurements of an unknown graph. The source develops reconstruction methods that trade the number of queries against the computation needed to interpret them. The question asks whether polynomial running time and subquadratic query complexity can be achieved simultaneously. An information-efficient search may still require expensive combinatorial inference. The project seeks to combine the strongest separate guarantees, turning a small set of resistance observations into an efficiently recoverable graph rather than only proving that the observations are sufficient.

[Read in atlas](index.html#TCS-6150) · [Graph Inference with Effective Resistance Queries](https://proceedings.mlr.press/v313/warton26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6173 — A Local-To-Global Theorem for Congested Shortest Paths — Explicit open question on PDF page 5

The directed disjoint-shortest-paths problem asks for paths connecting prescribed source-target pairs, with each path individually shortest and the paths mutually vertex-disjoint. The source highlights the case of three pairs and asks whether it can be solved in polynomial time. Polynomial algorithms for each fixed number of pairs in undirected graphs do not immediately extend when edge directions constrain route choices. Its local-to-global structural results suggest tools for understanding how directed shortest paths can intersect, but do not settle the algorithmic question. Resolving this small case would clarify a basic obstacle in routing several optimal paths through a directed network.

[Read in atlas](index.html#TCS-6173) · [A Local-To-Global Theorem for Congested Shortest Paths](https://doi.org/10.4230/LIPIcs.ESA.2023.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6237 — PACE Solver Description: Touiouidth — Explicit open question on PDF page 1

Computing twin-width means finding a contraction sequence minimizing its worst intermediate conflict degree. The source's solver searches these sequences exactly with branch-and-bound reductions. Its cited open boundary concerns polynomial-time recognition at widths two and three. Width-one recognition and width-four hardness bracket these cases in the source. The project seeks the structural or algorithmic distinction between neighboring small thresholds, which could guide both better exact solvers and more useful promises for graph algorithms based on twin-width.

[Read in atlas](index.html#TCS-6237) · [PACE Solver Description: Touiouidth](https://doi.org/10.4230/LIPIcs.IPEC.2023.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6251 — Max Weight Independent Set in Graphs with No Long Claws: An Analog of the Gyárfás' Path Argument — Explicit open question on PDF page 3

Maximum Weight Independent Set is difficult even though checking a proposed set is simple. The source exploits the exclusion of a fixed long subdivided claw to obtain subexponential algorithms and quasipolynomial approximation. Its broader direction is to improve the relevant bounds toward polynomial time across the remaining forbidden-pattern families. Methods based on small separators must also accommodate line-graph-like regions with different structure. The project seeks a unified decomposition that combines branching and matching-style techniques instead of forcing one method to handle every region.

[Read in atlas](index.html#TCS-6251) · [Max Weight Independent Set in Graphs with No Long Claws: An Analog of the Gyárfás' Path Argument](https://doi.org/10.4230/LIPIcs.ICALP.2022.93)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6254 — On the Role of the High-Low Partition in Realizing a Degree Sequence by a Bipartite Graph — Explicit open question on PDF page 2

A degree sequence specifies desired vertex degrees without assigning vertices to the two sides of a bipartite graph. If that partition were supplied, classical criteria could test realizability. The question asks for the complexity and a useful characterization when the partition itself must be found. The source studies high-low partitions as one structured route to the problem. The project isolates the difficulty of choosing compatible sides, separating it from the comparatively well-understood task of realizing a fixed bipartite degree specification.

[Read in atlas](index.html#TCS-6254) · [On the Role of the High-Low Partition in Realizing a Degree Sequence by a Bipartite Graph](https://doi.org/10.4230/LIPIcs.MFCS.2022.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6270 — A Simple Algorithm for Graph Reconstruction — Explicit open question on PDF page 5

Distance-query reconstruction learns every edge of a hidden connected bounded-degree graph. The source analyzes a simple sampling-based method that is especially efficient on random regular graphs. The question asks for nearly linear queries on every graph with the degree promise. Specific tree-shaped examples show why the analyzed method does not achieve that general guarantee. The project needs a more adaptive way to discover distinguishing vertices, avoiding repeated queries to regions that reveal little about uncertain adjacency elsewhere.

[Read in atlas](index.html#TCS-6270) · [A Simple Algorithm for Graph Reconstruction](https://doi.org/10.4230/LIPIcs.ESA.2021.68)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6421 — Towards an Isomorphism Dichotomy for Hereditary Graph Classes — Explicit open question on PDF page 2

Hereditary graph classes can be specified by finitely many forbidden induced subgraphs. The question asks whether graph isomorphism on such a class can have complexity intermediate between polynomial time and general graph-isomorphism completeness. The source establishes broad classifications and resolves most two-forbidden-pattern cases. Results for forbidden ordinary subgraphs do not immediately extend to induced exclusions. The project seeks a dichotomy explaining whether a finite structural prohibition always makes isomorphism substantially easier or leaves its full general difficulty intact.

[Read in atlas](index.html#TCS-6421) · [Towards an Isomorphism Dichotomy for Hereditary Graph Classes](https://doi.org/10.4230/LIPIcs.STACS.2015.689)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6433 — Connected Partitions via Connected Dominating Sets — Explicit open question on PDF page 1

The Gyori-Lovasz theorem guarantees connected graph partitions with prescribed part sizes and one prescribed root in each part. The graph's connectivity matches the number of requested parts. The source asks for a polynomial-time construction under the theorem's original assumptions, already for five parts. It obtains constructive results under stronger connectivity or additional graph structure. The project aims to extract an efficient algorithm from a powerful existence theorem while meeting all size, connectivity, and root constraints simultaneously.

[Read in atlas](index.html#TCS-6433) · [Connected Partitions via Connected Dominating Sets](https://doi.org/10.4230/LIPIcs.ESA.2025.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6492 — Folklore Sampling is Optimal for Exact Hopsets: Confirming the $\sqrt{n}$ Barrier — Open Question 1

Shortcut sets add edges that reduce the number of hops needed for reachability, while exact hopsets must also preserve shortest-path distances. The source studies how small these augmentations can make the relevant hop diameter in directed graphs. The selected question allows O(m) additional edges for an n-vertex graph with m original edges. It asks for a diameter exponent strictly better than the exponent available when only O(n) additional edges are allowed. This isolates whether dense graphs can use an edge-budget proportional to their original size to overcome barriers for sparse augmentations.

[Read in atlas](index.html#TCS-6492) · [Folklore Sampling is Optimal for Exact Hopsets: Confirming the $\sqrt{n}$ Barrier](https://doi.org/10.1109/FOCS57990.2023.00046)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6782 — Maximize the pair count admitting linear-size pairwise spanners with constant additive error.

A pairwise additive spanner preserves distances only for a specified collection of vertex pairs. Restricting the pairs can make much sparser subgraphs possible than preserving every distance. The source asks how large that collection may be while still guaranteeing linear-size spanners with constant additive error. The guarantee must cover arbitrary graphs and pair sets in the stated regime. The project seeks the boundary between the amount of requested metric information and the storage needed to preserve it accurately.

[Read in atlas](index.html#TCS-6782) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6783 — Does every unweighted graph admit a +4 spanner with O(n^(4/3)) edges?

A four-additive spanner retains graph edges so that every distance increases by at most four. The question asks whether every unweighted graph has such a subgraph with O(n^(4/3)) edges. It fixes both the additive error and the desired sparsity exponent. A structure allowed to insert new weighted shortcut edges would be an emulator and would not meet the same requirement. The project targets a precise point in the tradeoff between compact graph storage and uniformly accurate all-pairs distances.

[Read in atlas](index.html#TCS-6783) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6784 — Match Thorup–Zwick emulator tradeoffs using actual spanners.

An emulator may add weighted shortcut edges, whereas a spanner must use actual edges from the input graph. Thorup-Zwick style constructions offer useful distance-error and size tradeoffs in the more permissive setting. The source asks whether comparable tradeoffs can be realized by genuine spanners. Replacing each shortcut with a path may greatly increase the total number of retained edges. The project seeks shared path structure that can recover the emulator's compactness without relying on artificial metric connections.

[Read in atlas](index.html#TCS-6784) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6785 — Determine optimal additive error for linear-size spanners.

A linear-size spanner retains only a constant number of edges per vertex on average. For arbitrary graphs, this severe sparsity budget can force shortest paths to become longer. The source asks for the smallest additive error that can always be guaranteed under that budget. The error may grow with graph size, unlike a fixed additive approximation target. The project seeks matching constructions and lower bounds describing the exact amount of metric accuracy necessarily lost when a graph is compressed to linear edge count.

[Read in atlas](index.html#TCS-6785) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7061 — Find a polynomial-time/NP-hard dichotomy for hereditary edge-deletion problems.

A hereditary graph class is closed under taking induced subgraphs. The survey proposes a polynomial-time versus NP-hard dichotomy for edge deletion into such classes. The task is to identify which target properties permit efficient optimal repair and which force classical intractability. A general criterion would unify many individually studied modification problems through the structure of their target classes. The saved record explicitly treats this as a research direction and does not specify representation or decidability assumptions for the hereditary classes under consideration.

[Read in atlas](index.html#TCS-7061) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7075 — Determine complexity of unrestricted vertex-connectivity augmentation beyond increasing connectivity by one.

Vertex-connectivity measures how many vertex failures a graph can tolerate before becoming disconnected. Connectivity augmentation adds edges to raise that resilience level. The saved question asks for the complexity of unrestricted augmentation when the requested increase exceeds one. This probes whether techniques for a single increment can handle several interacting layers of required redundancy. The survey note does not specify edge costs or the optimization budget, so those conventions still need recovery before a precise polynomial-time or hardness statement can be formulated.

[Read in atlas](index.html#TCS-7075) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7146 — Detect any fixed pivot-minor or vertex-minor in polynomial time.

Pivot-minor and vertex-minor containment ask whether a target graph can be obtained through their respective local transformations and deletions. The source asks for polynomial-time detection when the target graph is fixed. Fixing the target permits constants and exponents to depend on it while the host graph grows. An algorithm would make these structural relations useful as effectively testable graph-class restrictions. The saved formulation does not request a uniform fixed-parameter bound in target size, and the distinction matters when assessing whether a target-specific polynomial algorithm settles the intended question.

[Read in atlas](index.html#TCS-7146) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800)
Existing status: `source_open` · Summary written: 2026-09-11

## Automata and formal languages (55)

### TCS-6558 — Černý conjecture: a reset word of length at most (n−1)²

A reset word drives a finite automaton to one common state, regardless of where it started. The project asks whether every synchronizing complete deterministic automaton with n states has such a word of length at most (n−1)². Explicit automata attain this length, so the proposed bound cannot be reduced. The difficulty is coordinating successive mergers of possible states without paying a cubic total cost. A solution would identify the exact worst-case effort required to regain control of an unknown finite-state system.

[Read in atlas](index.html#TCS-6558) · [Synchronizing Automata: Open Problems](https://arxiv.org/abs/2608.24245) · [Synchronization of finite automata](https://doi.org/10.4213/rm10005e) · [List of Results on the Černý Conjecture and Reset Thresholds for Synchronizing Automata](https://arxiv.org/abs/2508.15655) · [Improving the Upper Bound on the Length of the Shortest Reset Word](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2018.56) · [An Improvement to a Recent Upper Bound for Synchronizing Words of Finite Automata](https://doi.org/10.25596/jalc-2019-367) · [The Černý Conjecture for One-Cluster Automata via Annular Spectral Descent](https://arxiv.org/abs/2607.19675)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6560 — Can every two-way NFA be determinized with polynomially many states?

Two-way finite automata can reread their input by moving their head in either direction. This project asks whether every n-state nondeterministic machine has an equivalent deterministic two-way machine with polynomially many states. Both machines must agree on all finite words, with no restriction on input length. Rereading sometimes replaces exponentially much one-way memory, but that observation does not supply a general simulation. Resolving the question would quantify how much finite-state succinctness comes from nondeterministic choice once unrestricted revisiting of the input is available.

[Read in atlas](index.html#TCS-6560) · [Nondeterminism and the size of two way finite automata](https://doi.org/10.1145/800133.804357) · [Two-Way Finite Automata: Old and Recent Results](https://arxiv.org/abs/1208.2755) · [Two-way automata versus logarithmic space](https://www.andrew.cmu.edu/user/cak/reads/2014-TOCS/main.pdf) · [Two-Way Automata and Bounded Languages](https://air.unimi.it/handle/2434/1183476) · [Polynomial Complementation of Nondeterministic Two-Way Finite Automata by 1-Limited Automata](https://doi.org/10.4230/LIPIcs.STACS.2026.48)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6559 — Does any regular language require generalized star height greater than one?

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

### TCS-0164 — Equivalence for unambiguous grammars

An unambiguous context-free grammar assigns at most one parse tree to each generated word. Given two grammars promised to have this property, the project asks whether equality of their languages is decidable. The promise limits competing derivations without making the grammars deterministic. Enumeration can expose a word accepted by only one grammar, but agreement on finitely many words does not certify equivalence. A decision procedure would locate an important boundary between deterministic language comparison and the unrestricted context-free equivalence problem.

[Read in atlas](index.html#TCS-0164) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#equivalence-of-unambiguous-context-free-grammars)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0146 — Complexity of universality for unambiguous context-free grammars

An unambiguous context-free grammar has at most one derivation tree for any particular word. Its universality problem asks whether it generates every word over its alphabet. The source places this decidable task between a polynomial-time lower bound and a polynomial-space upper bound and asks to tighten that gap. Unambiguity removes duplicate derivations but still permits dependencies that a deterministic pushdown presentation cannot express. Better bounds would measure how expensive exhaustive language coverage becomes when unique parsing replaces deterministic parsing as the structural promise.

[Read in atlas](index.html#TCS-0146) · [Automata Exchange](https://automata.exchange/19.05-on-unambiguous-grammars/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0135 — The zeroness problem

A machine with numerical outputs may compute zero on every input despite having nontrivial internal computations. The zeroness project asks when this universal identity is decidable and how expensive the decision is. The source highlights weighted grammars over fields, unary polynomial automata, weighted Parikh automata and weighted vector addition systems. These are separate representations whose algebraic operations and storage affect the available arguments. Understanding their zero tests would also provide building blocks for comparing quantitative descriptions, where cancellation can hide differences between runs.

[Read in atlas](index.html#TCS-0135) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0156 — Universality for unambiguous automata

An unambiguous finite automaton may branch, but each accepted word has only one accepting run. Universality asks whether every finite word over its alphabet is accepted. The project seeks a sharper complexity classification within the efficient algorithms recorded by the source, rather than a new decidability proof. Its stated gap lies between nondeterministic-logspace hardness and a parallel NC² upper bound. Closing that gap would identify how much computational power is needed to certify complete language coverage when accepting witnesses are unique.

[Read in atlas](index.html#TCS-0156) · [Automata Exchange](https://automata.exchange/19.03-universality-for-unambiguous-automata/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0167 — Primitive words and context-freeness

A primitive word cannot be obtained by repeating a shorter word two or more times. The project asks whether the collection of all primitive words over an alphabet with at least two letters is non-context-free. This tests whether a context-free grammar can describe the absence of every possible global repetition pattern. Ruling out narrower grammar classes does not rule out arbitrary context-free grammars, which may exploit ambiguous derivations. The question connects elementary word periodicity with the expressive limits of recursive language descriptions.

[Read in atlas](index.html#TCS-0167) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#context-freeness-of-primitive-words)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0136 — Universality of register automata over ordered domains

Register automata process data words while remembering selected input values in finitely many registers. Here data come from the integers, and transitions may use order tests and constants. The source asks whether universality is decidable under the promise that each accepted word has a unique accepting run. If it is decidable, the next target is the complexity of a complete procedure. This would determine whether unique acceptance sufficiently controls the infinite ordered data domain to make exhaustive coverage of all input words algorithmically checkable.

[Read in atlas](index.html#TCS-0136) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0138 — Deterministic separability of nondeterministic timed languages

Two nondeterministic timed automata specify collections of words whose events carry timing information. The project asks whether some deterministic timed automaton accepts all words in the first collection while rejecting all words in the second. The separator may have any finite number of clocks, with no bound supplied beforehand. The source gives decidability when that clock count is fixed, leaving unbounded separator resources as the main obstacle. An unrestricted test would characterize when timed behaviors admit a deterministic classifier despite nondeterministic input descriptions.

[Read in atlas](index.html#TCS-0138) · [Automata Exchange](https://automata.exchange/20.02-deterministic-separability-of-nondeterministic-timed-languages/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0128 — Better bounds on complementing unambiguous automata

Complementation replaces a finite automaton's language by the set of words it rejects. Starting from an unambiguous automaton, the project asks how large a nondeterministic automaton for the complement must become. The source particularly seeks to close the gap for binary and larger alphabets, where its upper bound remains exponential. Unique accepting runs simplify the original language without automatically providing short certificates of rejection. Tight conversion bounds would quantify the representation cost of negating specifications whose positive witnesses are unambiguous.

[Read in atlas](index.html#TCS-0128) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0137 — What is the complexity of constructing unambiguous automata

A nondeterministic finite automaton may describe a language far more compactly than a more restricted equivalent machine. The project asks the complexity of deciding whether an equivalent deterministic or unambiguous automaton exists below a supplied state threshold. That threshold is encoded in binary, allowing candidate representations much larger than the threshold's written description. The task combines language equivalence with a search over possible state structures. A classification would clarify the computational cost of finding concise representations with deterministic or uniquely accepting behavior.

[Read in atlas](index.html#TCS-0137) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0111 — Lower bounds for determinizability of weighted automata over \(\mathbb Q\)

A rational weighted automaton combines weighted runs to associate numerical values with input words. Its determinizability problem asks whether the same function has a deterministic weighted representation. This project seeks computational lower bounds for that decision problem, following the decidability and upper bounds cited by the source. It also distinguishes general automata from the polynomially ambiguous subclass, where fewer competing runs permit a better upper bound. Hardness results would show which parts of the cost of testing deterministic representability are unavoidable.

[Read in atlas](index.html#TCS-0111) · [Automata Exchange](https://automata.exchange/24.18-lower-bounds-for-determinizability-of-weighted-automata-over-Q/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0133 — Stronger versions of inclusion of probabilistic automata

Probabilistic automata assign acceptance probabilities through weighted choices among runs. The source asks for an unconditional decidability proof of language containment when the machines have bounded ambiguity. Its existing conditional route relies on Schanuel's conjecture, linking the comparison to difficult arithmetic questions. Bounded ambiguity limits accepting computations but does not immediately eliminate the numerical relationships involved in containment. Removing that conjectural assumption would establish that the relevant probabilistic language comparison has a terminating algorithm on the stated structural class.

[Read in atlas](index.html#TCS-0133) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0624 — Language Equivalence between Nondeterministic and Deterministic One-Counter Machines

One-counter language models differ in whether they can test zero and whether their transitions may be nondeterministic. The project asks whether a deterministic one-counter automaton and a nondeterministic one-counter net recognize the same language. It also identifies the narrower case where both machines are nets, so neither has zero tests. The comparison combines a simple deterministic reference with a more flexible source of accepting runs. Decidability would show whether that asymmetric setup avoids the obstacles encountered in general nondeterministic infinite-state equivalence.

[Read in atlas](index.html#TCS-0624) · [Automata Exchange](https://automata.exchange/24.04-language-equivalence-between-nondeterministic-and-deterministic-one-counter-machines/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0094 — Do probabilities matter for resolving nondeterminism?

A memoryless stochastic resolver replaces each nondeterministic transition choice of a parity automaton by a fixed probability distribution. Successful resolution means almost-sure acceptance of every infinite word the original automaton accepts. The project asks whether existence of such a resolver always implies existence using uniform distributions over the available successors. All transitions keep the same state space, and no extra history-dependent memory is introduced. A positive answer would show that the support of randomized choices suffices, making finely tuned transition probabilities unnecessary for this form of resolution.

[Read in atlas](index.html#TCS-0094) · [Automata Exchange](https://automata.exchange/25.25-do-probabilities-matter-for-resolving-nondeterminism-/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0109 — Functions Weakly-Computable by Vector Addition Systems

A vector addition system weakly computes a function when some terminating run achieves its value and no terminating run exceeds it. Inputs and outputs occupy designated nonnegative counters, while auxiliary counters may retain arbitrary residual values. This project seeks a sharper characterization of the functions representable under that convention. The source highlights growth near 2 raised to the square root of the input and asks which linear recurrence sequences are representable. These examples probe how monotone counter dynamics constrain both growth rates and arithmetic regularity.

[Read in atlas](index.html#TCS-0109) · [Automata Exchange](https://automata.exchange/24.10-functions-weakly-computable-by-vector-addition-systems/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0154 — Separating words problem

Two distinct binary words may be separated by a finite automaton that accepts one and rejects the other. The project asks how many states always suffice when both words have length n. The source proposes a logarithmic target and also asks for improvements toward an n-to-the-one-third scale. A separating automaton may be tailored to the particular pair, so it need not recognize an entire difficult language. Sharp bounds would measure the finite-state resources required to detect just one difference between two long strings.

[Read in atlas](index.html#TCS-0154) · [Automata Exchange](https://automata.exchange/19.04-separating-words-problem/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0168 — Word-automaton recognition of tree languages

A regular tree language can be presented by a tree automaton and serialized using matching opening and closing tags. The project asks whether some ordinary word automaton can recognize exactly the valid serializations belonging to that language. Inputs are promised to encode trees, so the word automaton does not have to check tag matching itself. The issue is whether any remaining tree property genuinely requires memory of nesting. Deciding this would characterize which structured-document constraints can be checked with constant memory once well-formedness is guaranteed.

[Read in atlas](index.html#TCS-0168) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#which-regular-tree-languages-can-be-recognized-by-a-word-automaton)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0871 — Are universality and inclusion of AC-recognizable languages decidable?

Associative-commutative tree automata recognize terms modulo the equations attached to designated function symbols. The source asks whether universality and language inclusion can be decided for the general automaton model. Its later remark reports undecidability of inclusion, leaving universality as the unresolved part of that original pair. Restricting transition forms yields a better-behaved subclass, but those procedures do not cover the full model. Understanding universality would determine whether exhaustive acceptance remains checkable despite the more powerful equational treatment of tree structure.

[Read in atlas](index.html#TCS-0871) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/101.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1670 — The hierarchy is strict, that is, Σn ⊊ Σn+1 for all n (and the same is true for all combinations of Π, Σ and ∆).

Alternating plane-walking automata inspect infinite two-dimensional words using finite control and existential or universal branching. Bounding alternations of these choices yields a hierarchy of recognizable subshifts. The conjecture asks whether every additional level strictly increases expressive power, with corresponding distinctions among its existential, universal and intersection forms. Separations at the first level do not automatically repeat at higher levels because alternating computations can reorganize information. Establishing the hierarchy would quantify how nested choices increase the descriptive power of finite-state exploration in the plane.

[Read in atlas](index.html#TCS-1670) · [Subshifts Defined by Nondeterministic and Alternating Plane-Walking Automata](https://doi.org/10.4230/LIPIcs.STACS.2025.48)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2243 — Is there is a TC0 /NC1 complexity dichotomy?

Visibly pushdown languages are recognized by automata whose input symbols determine whether the stack is pushed, popped, or left unchanged. The question asks whether their computational complexity has a dichotomy between membership in TC0 and NC1-completeness. TC0 allows constant-depth polynomial-size circuits with threshold gates, whereas NC1 allows logarithmic-depth bounded-fan-in circuits. The source studies effective low-depth classifications and identifies cases where existing algebraic methods leave significant uncertainty. A dichotomy would rule out intermediate behavior in this structured language family and clarify which stack computations inherently require greater parallel depth.

[Read in atlas](index.html#TCS-2243) · [The AC⁰-Complexity of Visibly Pushdown Languages](https://doi.org/10.4230/LIPIcs.STACS.2024.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2851 — We conjecture that the techniques introduced in this paper can be extended to show that any continuous regular function is deterministic regular.

Regular transformations of infinite words may use descriptions whose output depends on arbitrarily distant input information. This conjecture asks whether continuity is sufficient to realize every such transformation by a deterministic regular machine. Continuity means that each finite output prefix is determined after seeing a sufficiently long finite input prefix. The source proves an analogous construction for rational functions and proposes extending its buffering techniques to the broader regular class. A proof would connect topological realizability of infinite-output behavior with an explicit deterministic transducer representation.

[Read in atlas](index.html#TCS-2851) · [Continuous Rational Functions Are Deterministic Regular](https://doi.org/10.4230/LIPIcs.MFCS.2022.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3030 — However, the complexity of UBA universality is an open problem [30]; only membership in PSPACE is known.

An unambiguous Büchi automaton reads infinite words and permits at most one accepting run for each word. Universality asks whether every infinite word over its alphabet is accepted. The cited source asks for the complexity of this decision problem, recording a PSPACE upper bound without a matching classification. Unambiguity helps with probabilistic verification, but it does not immediately make universal quantification over all words easy. Resolving this gap would also clarify the complexity of almost-sure model checking for branching processes, where a simple fixed transition structure can already encode the automaton universality question.

[Read in atlas](index.html#TCS-3030) · [Linear-Time Model Checking Branching Processes](https://doi.org/10.4230/LIPIcs.CONCUR.2021.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3325 — For regular functions, we conjecture that 2DFT characterise the computable ones, but we have not been able to show it yet.

Regular functions on infinite words can be specified by finite-state devices that inspect future input through look-ahead. Such specifications may describe noncomputable functions, because producing an output symbol can require information unavailable after any finite input prefix. The source conjectures that deterministic two-way transducers without that look-ahead characterize exactly the computable regular functions. Its equivalence between computability and continuity supplies a semantic criterion, while the desired result would give a concrete machine model. Proving the characterization would turn an abstract implementability condition into a finite-state description of how input can be revisited while output is produced.

[Read in atlas](index.html#TCS-3325) · [Synthesis of Computable Regular Functions of Infinite Words](https://doi.org/10.4230/LIPIcs.CONCUR.2020.43)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3378 — We conjecture that Corollaries 5 and 6 hold for arbitrary shapes, that is, that there does not exist a two-dimensional low complexity aperiodic SFT.

Two-dimensional shifts of finite type impose finitely many local constraints on tilings. The source conjectures that low pattern complexity rules out aperiodicity even when patterns are measured using arbitrary shapes. This extends a periodicity principle beyond the shapes handled by the cited corollaries. A proof would connect a numerical limit on local diversity with the existence of global repeating structure. The source's definition of low complexity and its quantification over shapes are missing from the excerpt, so those conditions must be recovered before asserting a universal tiling periodicity theorem.

[Read in atlas](index.html#TCS-3378) · [Decidability and Periodicity of Low Complexity Tilings](https://doi.org/10.4230/LIPIcs.STACS.2020.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3553 — Whether our techniques can be extended beyond weak automata – hopefully to all tree automata or, equivalently, full MSO logic, or full µ-calculus – remains […]

A regular language of infinite trees defines an event under a random tree-generating process. This project asks whether its probability measure can be computed for general tree automata, extending the source's result for weak automata. General acceptance allows alternation between least and greatest fixed points, bringing more complicated limiting behavior. The corresponding logical target includes full monadic second-order logic and the modal mu-calculus. A general algorithm would enable exact probabilistic analysis of branching specifications whose recurring obligations exceed the weak acceptance fragment.

[Read in atlas](index.html#TCS-3553) · [Computing Measures of Weak-MSO Definable Sets of Trees](https://doi.org/10.4230/LIPIcs.ICALP.2020.136)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3594 — We leave open the question of whether alternating GFG automata of stronger acceptance conditions allow for doubly-exponential succinctness compared to deterministic automata.

Alternating good-for-games automata combine existential and universal branching while retaining choices compatible with game composition. The project asks whether stronger infinite-word acceptance conditions allow them to be doubly exponentially smaller than equivalent deterministic automata. Existing transformations for Büchi acceptance provide context but do not settle these richer conditions. Both the language and the good-for-games requirement must be preserved when constructing separating families. A tight succinctness result would measure how much alternating branching can compress specifications while maintaining their usefulness in interactive verification.

[Read in atlas](index.html#TCS-3594) · [Good for Games Automata: From Nondeterminism to Alternation](https://doi.org/10.4230/LIPIcs.CONCUR.2019.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3801 — Can the long-standing Ω(n log n) lower bound [20] be improved, for example by a combination of the full-automata technique of Yan [23] and the […]

Alternating parity word automata can be translated into weaker acceptance models at a cost in their number of states. This project asks for lower bounds improving the source's longstanding n-log-n barrier for such translations. Candidate techniques combine carefully chosen full automata with structural arguments based on universal trees or graphs. Upper bounds alone do not show that their added states are necessary, particularly when both kinds of alternation can cooperate. Stronger lower bounds would identify the unavoidable representation cost of simplifying recurring-priority acceptance.

[Read in atlas](index.html#TCS-3801) · [Alternating Weak Automata from Universal Trees](https://doi.org/10.4230/LIPIcs.CONCUR.2019.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3863 — Decidability of the containment problem when both automata are allowed to be finitely ambiguous remains open.

Quantitative containment compares two probabilistic automata pointwise over all input words. The project asks whether this comparison is decidable when both automata have uniformly bounded numbers of accepting runs. The source handles cases with one unambiguous side using conditional arithmetic decision procedures. Allowing bounded multiplicity on both sides requires comparing sums of exponential terms and removes useful geometric structure from that argument. A resolution would show whether finite ambiguity suffices to control exact probabilistic comparison even when neither machine has unique accepting behavior.

[Read in atlas](index.html#TCS-3863) · [When is Containment Decidable for Probabilistic Automata?](https://doi.org/10.4230/LIPIcs.ICALP.2018.121)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3865 — The question about exponential separation in the case of a general alphabet remains open.

An unambiguous finite automaton has only one accepting run for each word it recognizes. The project asks whether complementing such a language can force an exponential increase in the states of a nondeterministic representation. The source already constructs a superpolynomial increase over a unary alphabet and asks for a stronger separation over general alphabets. Dropping unambiguity from the target makes the desired lower bound particularly robust. An exponential family would show that short unique positive witnesses can coexist with inherently much larger descriptions of all negative instances.

[Read in atlas](index.html#TCS-3865) · [A Superpolynomial Lower Bound for the Size of Non-Deterministic Complement of an Unambiguous Automaton](https://doi.org/10.4230/LIPIcs.ICALP.2018.138)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4251 — Beyond these two points, we do not know how to show decidability for Gnil (which is the join of the Gp ), and the surprising […]

A word transduction is continuous for a language class when inverse images of languages in that class remain in the class. This project studies decidability of that property for classes defined through algebraic varieties. The source singles out nilpotent-group languages as a case not covered by the available methods. It also suggests that some Burnside varieties may resist a uniform decidability approach because their equalizer sets are more complex. Understanding these boundaries would link the algebra of target languages to the structural behavior of finite transducers.

[Read in atlas](index.html#TCS-4251) · [Continuity and Rational Functions](https://doi.org/10.4230/LIPIcs.ICALP.2017.115)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4288 — Regarding the case of words we leave some open questions, the most important of which is if F1 is more succinct than FO2 .

The one-dimensional fragment of first-order logic restricts quantifier blocks to leave at most one free variable. Over words, the source proves it has the same expressive power as two-variable first-order logic. The question asks whether it can nevertheless describe some properties substantially more compactly. Equal expressiveness guarantees translations but says nothing about their size. The project would identify whether allowing larger local quantifier blocks gives a real succinctness advantage for word properties despite not adding any new definable languages.

[Read in atlas](index.html#TCS-4288) · [One-Dimensional Logic over Words](https://doi.org/10.4230/LIPIcs.CSL.2016.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4491 — Without the assumption that CA(n) = CA2 (n), it is still unknown whether CA(n) is closed under concatenation.

A one-dimensional cellular automaton recognizes a word through many identical cells updating in parallel. This project asks whether its real-time language class is closed under concatenation. Given two languages with real-time recognizers, their concatenation requires selecting a split position and validating both pieces within the same timing budget. The source links closure to a possible collapse between one-dimensional and two-dimensional real-time recognition. An unconditional closure proof or separating pair would clarify how tightly spatial dimension and exact running time constrain parallel language composition.

[Read in atlas](index.html#TCS-4491) · [Comparing 1D and 2D Real Time on Cellular Automata](https://doi.org/10.4230/LIPIcs.STACS.2015.367)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4503 — It thus remains open to show whether one can decide, given any automaton B and any ordinal 0 < α < ϕ2 (0), whether B […]

Wadge comparison orders languages by the continuous transformations that reduce one membership problem to another. The source constructs a transfinite family of unambiguous infinite-tree automata with increasing topological complexity. The project asks whether an arbitrary automaton can be compared effectively with a supplied family member indexed below the specified ordinal bound. Constructing the hierarchy and strategies between its own members does not provide this general decision procedure. An algorithm would make a substantial part of the topological classification of regular tree languages computationally accessible.

[Read in atlas](index.html#TCS-4503) · [On Unambiguous Regular Tree Languages of Index (0,2)](https://doi.org/10.4230/LIPIcs.CSL.2015.534)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4575 — The problem is related to the universality problem for discount sum automata [2], a well-known problem for which decidability remains open [1].

A discounted-sum automaton assigns an infinite word a value in which later transition weights receive progressively less influence. Its universality problem asks whether every word satisfies the specified quantitative acceptance requirement. The source points to this decision question while studying strategies that force an exact discounted payoff. Exact equality and universal quantification are delicate because arbitrarily late contributions can still affect the final value. Decidability would strengthen the foundations of verification for quantitative specifications where future rewards are discounted but never entirely ignored.

[Read in atlas](index.html#TCS-4575) · [Quantitative Games with Interval Objectives](https://doi.org/10.4230/LIPIcs.FSTTCS.2014.365)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4636 — Further if F[<] is decidable, does it imply that F[<, MOD] is also decidable?

The source studies which regular languages can be described in logical fragments over ordered word positions. Its general question asks whether decidability of definability in a fragment using order survives the addition of modular numerical predicates. These predicates can test positions or word lengths modulo a fixed integer, increasing the language's expressive resources. The issue is recognizing whether a given regular language belongs to the logical fragment, rather than the satisfiability of an arbitrary formula. A preservation theorem would transfer existing classification algorithms to enriched logics, but the 2013 discussion leaves the necessary conditions on the fragment open.

[Read in atlas](index.html#TCS-4636) · [Two-variable first order logic with modular predicates over words](https://doi.org/10.4230/LIPIcs.STACS.2013.329)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4659 — Notice that it is still unknown whether the determinacy of Wadge games W (L(A), L(B)), where A and B are Muller tree automata (reading infinite […]

Wadge games compare two languages by asking players to construct objects whose membership outcomes correspond. This project concerns languages of infinite labeled trees recognized by Muller tree automata. It asks whether determinacy of all such games can be proved within ordinary ZFC set theory or requires stronger assumptions. The source establishes independence phenomena for related counter-automaton word games, which do not automatically cover regular tree languages. Resolving the tree case would locate the set-theoretic strength hidden in games defined by finite automata.

[Read in atlas](index.html#TCS-4659) · [The Determinacy of Context-Free Games](https://doi.org/10.4230/LIPIcs.STACS.2012.555)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4673 — The following question remains open: is there a language recognized by a collapsible deterministic higher order pushdown automaton which is not recognized by any deterministic […]

Collapsible higher-order pushdown automata enrich nested stacks with links that support a collapse operation. The project asks for a language recognized by a deterministic collapsible machine but by no deterministic noncollapsible machine of any finite order. A separation at the same stack order is insufficient because raising the noncollapsible order might simulate the missing operation. The source supplies a second-order candidate language and leaves the unrestricted-order separation as the target. Such a result would establish that collapse adds expressive power beyond simply increasing stack nesting depth.

[Read in atlas](index.html#TCS-4673) · [Collapse Operation Increases Expressive Power of Deterministic Higher Order Pushdown Automata](https://doi.org/10.4230/LIPIcs.STACS.2011.603)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4677 — Therefore, one can ask: is it decidable if an orbit finite automaton recognizes a language that can be defined in first-order logic?

Orbit-finite automata recognize data words using infinitely many states organized into finitely many symmetry classes. The project asks whether first-order definability of the recognized language can be decided. The source conjectures that aperiodicity of the syntactic monoid provides the correct criterion within this automaton class. Infinite-data languages outside the class show that aperiodicity alone is not a universal characterization. Proving an effective criterion would extend a central connection between finite automata, algebra and logic to a controlled infinite-alphabet setting.

[Read in atlas](index.html#TCS-4677) · [Data Monoids](https://doi.org/10.4230/LIPIcs.STACS.2011.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5651 — Word Automata with Limited Nondeterminism (Invited Talk) — Unresolved-question passage on page 16

Limited nondeterminism lets automata retain some branching while remaining suitable for composition with games or probabilistic systems. This project asks the exact complexity of recognizing good-for-games parity automata and good-for-MDPs Büchi automata. The former resolve choices from input history, while the latter preserve optimal satisfaction probabilities when combined with a Markov decision process. These are different semantic promises, so an algorithm for one does not establish the other. Sharper classifications would show the cost of checking that a compact specification supports the intended verification workflow.

[Read in atlas](index.html#TCS-5651) · [Word Automata with Limited Nondeterminism (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2026.3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5701 — Complexity of Boolean Automata Networks Under Block-Parallel Update Modes — Conjecture 16

Boolean automata networks update many local bits according to a schedule that can substantially alter their dynamics. The imported claim proposes that problems already NP-hard or coNP-hard under block-sequential schedules become PSPACE-complete under block-parallel schedules. The cited source explicitly labels this conjecture false, using recognition of bijective dynamics to defeat the proposed general transfer. Bijectivity can be checked through individual substeps and does not exhibit the claimed automatic increase. This record therefore explains a failed organizing principle and the need for property-specific complexity arguments.

[Read in atlas](index.html#TCS-5701) · [Complexity of Boolean Automata Networks Under Block-Parallel Update Modes](https://doi.org/10.4230/LIPIcs.SAND.2024.19)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5732 — Regular Separability in Büchi VASS — Explicit open question on PDF page 1

A reachability language of a vector addition system with states consists of finite words labeling accepting counter runs. In the source's convention, acceptance requires a final control state with all counters zero. Regular separability asks whether a finite automaton can recognize a language containing one such language and disjoint from another. The cited paper identifies decidability for general finite-word VASS languages as a separate question from its positive result for Büchi VASS over infinite words. Solving it would determine when finite-state separators can effectively distinguish behaviors of two unbounded counter systems under exact reachability acceptance.

[Read in atlas](index.html#TCS-5732) · [Regular Separability in Büchi VASS](https://doi.org/10.4230/LIPIcs.STACS.2023.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5738 — Separating Automatic Relations — Conjecture 7.1

Automatic relations on words are recognized by finite automata reading their components synchronously. The project asks whether two such relations can be separated by a recognizable relation, a finite union of products of regular languages. The conjecture predicts that deciding existence of any such separator is impossible. The source relates this task to regular colorability and distinguishes it from versions with a fixed color bound. Settling the unrestricted question would identify a limit of simplifying synchronized relational specifications into independently recognizable components.

[Read in atlas](index.html#TCS-5738) · [Separating Automatic Relations](https://doi.org/10.4230/LIPIcs.MFCS.2023.17)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5861 — Universality Problem for Unambiguous VASS — Explicit open question on PDF page 4

A vector addition system with states recognizes words while updating nonnegative counters and accepting by final control state. The project asks whether adding transitions that consume no input letter enlarges the language class. Silent transitions allow extra counter manipulation between visible events without lengthening the recognized word. The source leaves this expressiveness question unresolved even without the unambiguity restriction studied elsewhere in the paper. A simulation or separating language would determine whether timing of internal counter work is an essential resource for this recognition model.

[Read in atlas](index.html#TCS-5861) · [Universality Problem for Unambiguous VASS](https://doi.org/10.4230/LIPIcs.CONCUR.2020.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5863 — Resolving Nondeterminism with Randomness — Unresolved-question passage on page 16

A stochastic resolver chooses an automaton's transitions randomly while reading an infinite word prefix by prefix. Stochastic resolvability requires almost-sure acceptance of every word in the original language when the word is fixed independently of those choices. This project asks whether that property is decidable for Büchi and coBüchi automata. Checking one proposed resolver is already problematic in the source, but that does not decide whether some suitable resolver exists. An existence test would identify which finite nondeterministic specifications admit reliable randomized online execution.

[Read in atlas](index.html#TCS-5863) · [Resolving Nondeterminism with Randomness](https://doi.org/10.4230/LIPIcs.MFCS.2025.57)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5904 — Safety and Liveness of Quantitative Automata — Explicit open question on PDF page 7

Discounted-sum automata assign values to infinite words by giving earlier transition weights more influence than later ones. The project asks whether equivalence of these quantitative functions is decidable for the source's automaton model. Agreement must hold on every word and in the exact numerical value, not just at a chosen threshold. The source distinguishes this from deciding whether one automaton computes a constant function, which it handles separately. A general comparison procedure would provide a fundamental correctness test for quantitative specifications with geometrically discounted future contributions.

[Read in atlas](index.html#TCS-5904) · [Safety and Liveness of Quantitative Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2023.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5959 — What Can Oracles Teach Us About the Ultimate Fate of Life? — Explicit open question on PDF page 5

Conway's Game of Life has a limit set consisting of configurations with arbitrarily long predecessor histories. The project asks the complexity of recognizing finite patterns that occur somewhere in this set. The source proves polynomial-space hardness and asks whether the full co-recursively-enumerable completeness bound is attained. Standard universality constructions do not settle this because surrounding cells must not be assumed harmless when testing arbitrary patterns. A matching hardness result would show that indefinitely possible past histories encode substantially more difficulty than ordinary finite-time simulation.

[Read in atlas](index.html#TCS-5959) · [What Can Oracles Teach Us About the Ultimate Fate of Life?](https://doi.org/10.4230/LIPIcs.ICALP.2022.131)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6064 — Construction of mu-Limit Sets of Two-dimensional Cellular Automata — Explicit open question on PDF page 1

A cellular automaton's limit set contains every configuration that can appear after arbitrarily many update steps. This project asks which subshifts can arise as such limit sets. The characterization concerns all possible initial configurations, including exceptional behaviors of negligible probability. The source's positive result instead addresses measure-based limit sets under random initial conditions and therefore answers a different question. An ordinary limit-set characterization would describe the full range of persistent global behavior that can emerge from a finite local update rule.

[Read in atlas](index.html#TCS-6064) · [Construction of mu-Limit Sets of Two-dimensional Cellular Automata](https://doi.org/10.4230/LIPIcs.STACS.2015.262)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6158 — Probabilistic cellular automata, invariant measures, and perfect sampling — Explicit open question on PDF page 5

A deterministic cellular automaton induces a transformation on probability distributions over its configurations. Unique ergodicity means that exactly one distribution remains invariant under this transformation. The project asks whether that uniqueness forces every initial distribution to converge weakly to the invariant one. The latter is a stronger convergence requirement associated with Markov-chain ergodicity, rather than merely uniqueness of a stationary distribution. A proof or counterexample would clarify whether local deterministic dynamics can sustain nonconvergent distributional behavior despite having only one invariant measure.

[Read in atlas](index.html#TCS-6158) · [Probabilistic cellular automata, invariant measures, and perfect sampling](https://doi.org/10.4230/LIPIcs.STACS.2011.296)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0121 — Decidability of $(\min,+)$-weighted automata determinization

A min-plus weighted automaton assigns each finite word the minimum accumulated cost of its runs. The historical question asks whether the existence of an equivalent deterministic weighted automaton can be decided. Almagor, Arbel and Sheinvald settled this positively in a 2025 preprint published at SODA 2026. Their LICS 2026 follow-up supplies a primitive-recursive complexity upper bound. The card is retained as a resolved record, with unrestricted ambiguity and the endpoint-weight conventions included.

[Read in atlas](index.html#TCS-0121) · [Automata Exchange](https://automata.exchange/22.05-decidability-of-min-plus-weighted-automata-determinization/) · [Determinization of Min-Plus Weighted Automata is Decidable](https://arxiv.org/abs/2503.23826v1) · [Determinization of Min-Plus Weighted Automata is Decidable](https://epubs.siam.org/doi/10.1137/1.9781611978971.11) · [A Complexity Bound for Determinisation of Min-Plus Weighted Automata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.5)
Existing status: `resolved` · Summary written: 2026-09-11

## Semantics, logic and verification (77)

### TCS-6565 — Is positivity of integer linear recurrences decidable?

An integer linear recurrence gives a finite rule for generating an infinite sequence. The positivity problem asks whether every term is nonnegative, with the recurrence order included in the input. Computing a long prefix cannot certify the answer because a negative term may appear arbitrarily late. Characteristic roots can combine growth and oscillation, making exact sign control depend on subtle arithmetic relationships. A terminating decision procedure would provide a basic verification tool for linear discrete dynamics, while a negative result would establish limits even in this elementary setting.

[Read in atlas](index.html#TCS-6565) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26abs.html) · [Positivity Problems for Low-Order Linear Recurrence Sequences](https://arxiv.org/abs/1307.2779) · [On the Positivity Problem for Simple Linear Recurrence Sequences](https://arxiv.org/abs/1309.1550) · [Ultimate Positivity is Decidable for Simple Linear Recurrence Sequences](https://arxiv.org/abs/1309.1914) · [Positivity Problems for Reversible Linear Recurrence Sequences](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.130)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6567 — Can simple stochastic games be solved in polynomial time?

A simple stochastic game combines choices of a maximizing player, choices of a minimizing player and fair random branching. The project asks for a deterministic polynomial-time algorithm deciding whether the optimal probability of reaching a target exceeds a given rational threshold. Optimal positional strategies provide short certificates, but finding them may require navigating exponentially many combinations. Cycles also mean that solving local value equations without the correct reachability interpretation can give misleading answers. Progress would clarify the computational cost of exact planning against both adversarial and random uncertainty.

[Read in atlas](index.html#TCS-6567) · [The Complexity of Stochastic Games](https://www.sciencedirect.com/science/article/pii/089054019290048K) · [A Subexponential Randomized Algorithm for the Simple Stochastic Game Problem](https://www.sciencedirect.com/science/article/pii/S0890540185710358) · [A Direct Reduction from Stochastic Parity Games to Simple Stochastic Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CONCUR.2025.9) · [Sound Value Iteration for Simple Stochastic Games](https://arxiv.org/abs/2509.14112) · [Sinks and Ladders: ARRIVAL and SSG with Two Vertices per Level](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/html/LIPIcs.FUN.2026.19/LIPIcs.FUN.2026.19.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6569 — An internal tower of semisimplicial types in ordinary HoTT

Semisimplicial types organize vertices, edges, triangles and higher-dimensional fillers with compatible shared boundaries. Ordinary homotopy type theory can describe any fixed finite collection of these stages externally. The project asks for one internal family indexed by natural numbers, together with compatible maps forgetting the highest stage. Higher identities carry data, so specifying all coherence requirements uniformly is harder than listing equations in ordinary set-based mathematics. Such a construction would provide an internal foundation for important higher-dimensional structures without extending the stated type theory.

[Read in atlas](index.html#TCS-6569) · [On the Role of Semisimplicial Types](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf) · [Homotopy Type Theory: Univalent Foundations of Mathematics](https://homotopytypetheory.org/book/) · [Two-level type theory and applications](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/twolevel-type-theory-and-applications/4914DB4F8E8305DFC68F9CDCA9D0C8D0) · [Two-Level Type Theory and Applications — revised manuscript](https://arxiv.org/abs/1705.03307v5) · [Displayed type theory and semi-simplicial types](https://doi.org/10.1017/S096012952510025X) · [Internal Constructions in Homotopical Type Theory](https://www.joshchen.io/pdf/thesis-phd.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6570 — Can a Scott-continuous lambda model validate exactly beta-conversion?

Scott's continuous semantics interprets untyped lambda terms using mathematical domains and continuous functions. The project asks whether some model identifies exactly the pairs of terms related by beta-conversion. Beta-conversion expresses equality generated by applying functions to arguments and substituting those arguments into their bodies. Many semantic constructions validate additional equations, so soundness for beta-reduction alone does not answer the question. An exact model would show whether this influential notion of continuous meaning can distinguish every pair of terms that the basic operational equations keep separate.

[Read in atlas](index.html#TCS-6570) · [Continuously complete CPO models with minimal theory — TLCA Problem 22](https://tlca.di.unito.it/opltlca/opltlcasu29.html) · [Lambda theories of effective lambda models](https://arxiv.org/abs/math/0701684)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6583 — Does weak normalization imply strong normalization for every pure type system?

A pure type system specifies a typed lambda calculus through a uniform collection of formation rules. Weak normalization means that every well-typed term has some terminating reduction path. The conjecture asks whether that global property forces every reduction path of every well-typed term to terminate. A term may have both a normalizing route and a divergent route in less constrained rewriting settings, so the type-system hypothesis is essential. A proof would connect existence of normal forms with unrestricted evaluation termination across a broad family of typed calculi.

[Read in atlas](index.html#TCS-6583) · [Weak versus strong normalization for pure type systems — TLCA Problem 9](https://tlca.di.unito.it/opltlca/problem9.pdf) · [An Irrelevancy-Eliminating Translation of Pure Type Systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TYPES.2022.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4245 — Can parity games be solved in deterministic polynomial time?

Parity games ask which player can force an infinite play whose minimum infinitely recurring priority has the desired parity. The target is a uniform deterministic polynomial-time decision algorithm for arbitrary finite arenas and binary-encoded priorities. Quasipolynomial algorithms and lower bounds for separating-automaton methods are known. A November 2025 preprint claims a polynomial-time solution, but this review did not establish its correctness. A separate April 2026 paper still treats the question as open, so the completed card explicitly records an unverified current status.

[Read in atlas](index.html#TCS-4245) · [Deciding Parity Games in Quasipolynomial Time](https://www.cs.auckland.ac.nz/~cristian/crispapers/paritygame-stoc.pdf) · [Universal trees grow inside separating automata: Quasi-polynomial lower bounds for parity games](https://arxiv.org/abs/1807.10546) · [Attractors Is All You Need: Parity Games In Polynomial Time](https://arxiv.org/abs/2511.03752v1) · [On the Complexity of Robust Markov Decision Processes and Bisimulation Metrics](https://arxiv.org/abs/2604.26748)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5773 — Is the Skolem problem for integer linear recurrences decidable?

The Skolem problem asks whether an integer linear recurrence ever has a zero term. Its order, coefficients and initial values form a finite binary input, with no restriction to simple or non-degenerate sequences. The classical structural theorem about zero sets does not provide an unconditional decision procedure for every recurrence. The reviewed July 2026 results establish stronger low-order bounds and a general conditional decidability theorem, leaving the unrestricted unconditional target unresolved. The completed card preserves the original identifier and source while spelling out the exact discrete recurrence model.

[Read in atlas](index.html#TCS-5773) · [Skolem Meets Schanuel](https://doi.org/10.4230/LIPIcs.MFCS.2022.20) · [On the Complexity of the Skolem Problem at Low Orders](https://arxiv.org/abs/2507.11234v3) · [Conjectural Decidability of the Skolem Problem](https://arxiv.org/abs/2607.15510)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6568 — Can mean-payoff games be solved in polynomial time?

In a mean-payoff game, two players move a token through a finite weighted directed graph. The maximizing player wants the limiting lower average weight to be nonnegative against every opposing strategy. The project asks whether this threshold question has a deterministic algorithm polynomial in the full binary input length. Algorithms polynomial in the numerical magnitude of weights do not suffice because a large weight can have a short encoding. An efficient solution would settle a central exact optimization problem for systems with long-run rewards and adversarial control.

[Read in atlas](index.html#TCS-6568) · [The complexity of mean payoff games](https://link.springer.com/chapter/10.1007/BFb0030814) · [Faster Algorithms for Mean-Payoff Games](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf) · [Value Iteration Using Universal Graphs and the Complexity of Mean Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2020.34) · [Smoothed Analysis of Deterministic Discounted and Mean-Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.147) · [Strategy Improvement, the Simplex Algorithm and Lopsidedness](https://arxiv.org/abs/2509.16075) · [Set-defined graph classes: χ-boundedness meets tropical algebra](https://arxiv.org/abs/2607.23754)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6566 — Decidability of unbounded Continuous Skolem

A rational linear differential system evolves as a matrix exponential applied to its initial state. Continuous Skolem asks whether a specified linear observation of that trajectory is exactly zero at some nonnegative real time. The dimension is unrestricted, and the project seeks decidability without a time horizon. Approaching zero or changing sign are inadequate substitutes because trajectories may approach without hitting or touch zero without crossing it. A resolution would establish the limits of exact reachability verification even for continuous systems with linear, fully specified dynamics.

[Read in atlas](index.html#TCS-6566) · [The continuous Skolem-Pisot problem](https://perso.uclouvain.be/vincent.blondel/publications/10BDJ.pdf) · [On the Skolem Problem for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1506.00695) · [On Recurrent Reachability for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1507.03632) · [Axiomatization of Compact Initial Value Problems: Open Properties](https://publikationen.bibliothek.kit.edu/1000188295/170660770) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7192 — Is multiplicative-exponential linear logic decidable?

MELL asks whether provability in a resource-sensitive propositional logic can always be decided. Its multiplicative connectives combine resources, while exponential modalities permit controlled reuse. The card specifies the entire finite proof calculus, including units and the conditions on contraction and promotion. Proof checking alone does not guarantee that a search can terminate on an unprovable input. A July 2026 preprint claims a positive resolution through general branching vector addition systems, which is recorded here without independent proof verification.

[Read in atlas](index.html#TCS-7192) · [Handbook of Linear Logic](https://ll-handbook.pages.math.cnrs.fr/book/ll-handbook-public.pdf) · [On the Decision Problem for MELL](https://www.lix.polytechnique.fr/~lutz/papers/OnDeciMELL.pdf) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.22/LIPIcs.MFCS.2025.22.html) · [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear Inductive Invariants](https://arxiv.org/abs/2607.09558v1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0619 — Reachability in Low-Dimensional VASS

A vector addition system with states combines finite control with counters that must remain nonnegative. Reachability asks whether an exact target configuration can be reached from a supplied source. The project seeks to establish tower-level hardness using fewer than the eight counters cited by the source. It also proposes lowering geometric dimension, which measures the span of cycle effects rather than simply counting counters. Stronger reductions would identify how little numerical freedom already suffices to encode extremely complex infinite-state verification problems.

[Read in atlas](index.html#TCS-0619) · [Automata Exchange](https://automata.exchange/25.9-reachability-in-low-dimensional-vass/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0632 — Complexity of fixed VAS reachability

A fixed vector addition system supplies a finite collection of updates on nonnegative integer vectors. The conjecture asks whether every reachable source-target pair has a path whose length is linear in the magnitudes of those endpoints. The multiplicative constant may depend on the entire fixed update system. This is a structural short-witness claim, not a uniform linear-time algorithm measured in binary input length. Proving it would show that arbitrarily complicated detours cannot force superlinear path growth once the transition rules themselves remain fixed.

[Read in atlas](index.html#TCS-0632) · [Automata Exchange](https://automata.exchange/22.01-complexity-fixed-vas-reachability/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0575 — Tighten the complexity of solving random-turn games

In a random-turn game, a biased coin decides which player chooses the next move of a graph token. The project asks the complexity of deciding whether the optimal winning probability exceeds one half. The source places the problem in NP and coNP but leaves both a polynomial-time solution and hardness comparable to general stochastic games unresolved. Randomly assigning control creates additional symmetry that might make this subclass easier. A classification would also inform bidding games, whose optimal strategies can be connected to random-turn values.

[Read in atlas](index.html#TCS-0575) · [Automata Exchange](https://automata.exchange/20.10-random-turn-games/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0640 — Shortest runs in 3-D VASS

A three-dimensional VASS is a finite-state system with three nonnegative integer counters. The source asks whether some reachable instances require shortest runs longer than every single-exponential bound in their binary input length. Encoding a large initial counter in binary already permits exponentially many necessary steps, so a stronger growth rate is required. A July 2026 preprint states a doubly-exponential upper bound, improving the triple-exponential bound from 2025. The remaining threshold question measures how much reachability-witness complexity three counters can force.

[Read in atlas](index.html#TCS-0640) · [Shortest runs in 3-D VASS](https://automata.exchange/19.11-shortest-runs-in-3-d-vass/) · [Reachability in 3-VASS is Elementary](https://arxiv.org/abs/2502.13916) · [3-VASS Reachability is in EXPSPACE](https://arxiv.org/abs/2607.14983)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0869 — Give a complete (resource free) characterisation of rewrite systems with polynomial derivational complexity.

A term rewriting system has polynomial derivational complexity when all reduction sequences are polynomially bounded in the initial term size. The project seeks a complete structural characterization that does not mention that complexity bound directly. This mirrors semantic characterizations of termination while demanding control of how long termination takes. The source explains that ordinary matrix interpretations are insufficient because some simple linear-complexity systems admit no compatible interpretation. A broader complete method would connect implicit complexity with the practical task of proving efficient symbolic evaluation.

[Read in atlas](index.html#TCS-0869) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/107.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0913 — Is the word problem for the S -combinator decidable?

The S-combinator is governed by the single rule that rewrites S applied to x, y and z into the application of xz to yz. This project asks whether convertibility of two closed terms built only from S and application is decidable. Conversion allows the equivalence generated by the rule, rather than requiring one particular forward evaluation path. Knowing whether an individual term normalizes does not automatically compare arbitrary nonnormalizing terms. A decision procedure would show how far removing all other combinators simplifies symbolic equality.

[Read in atlas](index.html#TCS-0913) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/97.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0875 — Does every automatic group have a presentation through some finite convergent string-rewriting system? Does every automatic monoid have an automatic structure such that the set of representatives is a prefix-closed cross-section?

Automatic groups and monoids use finite automata to describe representatives and multiplication relations. The project asks whether every automatic group also has a finite terminating confluent string-rewriting presentation. It separately asks whether every automatic monoid admits unique representatives forming a prefix-closed language. Uniqueness and prefix closure can be obtained separately in the source's discussion, but their simultaneous availability is the issue. Resolving these representation questions would connect automata-based algebraic computation with canonical simplification and structured normal forms.

[Read in atlas](index.html#TCS-0875) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/91.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0877 — Is strong sequentiality decidable for arbitrary rewrite systems?

Strong sequentiality is a structural condition on rewriting systems that supports optimal choices of reductions. The project asks whether this condition is decidable for arbitrary term-rewriting systems. It also seeks the computational complexity for linear and orthogonal subclasses. Existing procedures for restricted rule patterns do not necessarily handle overlap or repeated-variable interactions in the general case. A classification would clarify when a symbolic evaluator can determine in advance that its rule system supports a disciplined strategy for avoiding unnecessary reductions.

[Read in atlas](index.html#TCS-0877) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/80.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0896 — Has any full, finitely-generated and Church-Rosser term-rewriting system (or system with bound variables) a recursive, one-step, normalizing reduction strategy?

A normalizing reduction strategy finds a normal form whenever the input term has one. The project asks whether every finitely generated, full Church-Rosser rewriting system admits a recursive strategy choosing one rewrite step at a time. Fullness includes every term constructible from the signature, while Church-Rosser ensures compatible reduction outcomes. The source notes that dropping any assumption permits counterexamples and that weakly orthogonal systems satisfy the claim. Resolving the general case would connect existence of confluent normal forms with an effective sequential way to reach them.

[Read in atlas](index.html#TCS-0896) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/10.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0901 — Is termination of one linear rule decidable?

A rewrite system with one rule can still generate infinitely many terms through repeated substitution and rewriting. The project asks whether termination is decidable when the rule is linear on both its left and right sides. Linearity prevents repeated occurrences of a variable within either side, limiting copying and equality tests. The source emphasizes that left-linearity alone does not suffice and identifies one-rule string rewriting as a related restricted target. A procedure or undecidability construction would sharpen how little symbolic machinery can already encode unbounded computation.

[Read in atlas](index.html#TCS-0901) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/21.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0092 — Complete techniques for deducing Fair Almost-Sure Termination

Probabilistic programs with nondeterministic choices combine random transitions with decisions made by a scheduler. Here fairness requires every nondeterministic transition enabled infinitely often along an infinite execution to be taken infinitely often. The project asks the recursion-theoretic complexity of termination with probability one under every fair scheduler. It separately seeks sound and complete proof techniques for establishing that property. The interaction between fairness and probability makes this more subtle than either ordinary termination or almost-sure termination under an unrestricted scheduling convention.

[Read in atlas](index.html#TCS-0092) · [Automata Exchange](https://automata.exchange/25.19-complete-techniques-for-deducing-fair-almost-sure-termination/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0120 — Constructive Zermelo's Problem

An MSO-definable choice function selects one element from every nonempty subset of a structure. The conjecture asks whether existence of such a function forces existence of an MSO-definable well-order on the same structure. A well-order already gives a choice function by selecting each set's least element. The stronger constructive version asks for a procedure translating the choice formula into a well-order formula uniformly across structures of the signature. This would give a definability-preserving counterpart to the relationship between abstract choice and well-ordering.

[Read in atlas](index.html#TCS-0120) · [Automata Exchange](https://automata.exchange/22.09-constructive-zermelo-s-problem/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1167 — Is the existence of a fully universal representation for a given finite relation algebra effectively decidable?

A finite relation algebra describes abstract binary relations and operations such as composition and converse. The project asks whether one can decide that it has a fully universal representation by actual relations. Such a representation realizes the consistent atomic networks needed in the source's connection between network consistency and satisfaction. Merely checking a finite network does not establish a representation that works uniformly for all of them. An effective criterion would connect finite algebraic specifications with the existence of a suitably comprehensive relational model.

[Read in atlas](index.html#TCS-1167) · [The Network Satisfaction Problem for Relation Algebras with at Most 4 Atoms](https://doi.org/10.4230/LIPIcs.ICALP.2026.168)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1420 — Let us conclude by restating the main open problem: is Cantor-Łukasiewicz set theory Łset consistent?

Cantor-Lukasiewicz set theory combines naive set comprehension with a restricted logical framework. The project asks whether the resulting theory is consistent. Its approach retains broad comprehension while weakening the logic that would otherwise produce familiar set-theoretic paradoxes. The source develops related substructural proof systems but leaves the full Lukasiewicz-based theory as the principal target. A consistency proof or derivation of contradiction would show whether this balance between set formation and logical inference can support a coherent foundation.

[Read in atlas](index.html#TCS-1420) · [On the Consistency of Naive Set Theories over Substructural and Fuzzy Logics](https://doi.org/10.4230/LIPIcs.FSCD.2026.30)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1497 — Finally, we recall that we do not know if the games studied in this paper are determined, namely if one of the players has always […]

Timed Büchi-Landweber-style games let players generate behavior subject to timing choices and a nondeterministic timed-automaton winning condition. The project asks whether these games are determined, meaning that one player always has a winning strategy. Undecidability of computing strategies does not itself imply failure of their mathematical existence. Continuous time and the specified information structure complicate direct use of ordinary finite-state game arguments. A determinacy theorem or counterexample would clarify the foundations on which timed synthesis problems in this framework are posed.

[Read in atlas](index.html#TCS-1497) · [One-Clock Synthesis Problems](https://doi.org/10.4230/LIPIcs.STACS.2026.64)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1649 — The decidability status of the reachability problem for d-BVASS remains open in arbitrary dimension.

A branching vector addition system with states combines nonnegative counters with computations that can split into several branches. Reachability asks whether an initial configuration can produce an accepting computation satisfying the required final configurations. The problem is to determine whether this question is decidable when the counter dimension is arbitrary. The source develops a decision procedure in dimension two, while noting that its approach does not supply a complexity upper bound there. Extending decidability beyond this restricted dimension would explain how branching changes the algorithmic behavior of counter systems compared with ordinary Petri nets.

[Read in atlas](index.html#TCS-1649) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://doi.org/10.4230/LIPIcs.MFCS.2025.22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1656 — Yet, we do not know if there are polynomial time algorithms that decide explicitly given McNaughton games.

McNaughton games are infinite games on directed graphs whose winner depends on which designated vertices recur indefinitely. The input representation matters because a winning condition can encode a large family of recurrent vertex sets. This question asks for a polynomial-time decision algorithm when the McNaughton game is given explicitly in the representation used by the source. The motivation comes from a polynomial-time result for explicitly represented Muller games that does not immediately settle this variant. Resolving the gap would distinguish genuine game-solving difficulty from the cost of representing the winning condition.

[Read in atlas](index.html#TCS-1656) · [Deciding Regular Games: a Playground for Exponential Time Algorithms](https://doi.org/10.4230/LIPIcs.MFCS.2025.66)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1659 — The decidability remains open for general semigroups – that is, when there are states with non-unique tight actions.

Bellman operators of Markov decision processes define structured piecewise affine dynamics on probability vectors. The source studies whether iterating such an operator can reach a specified vector, including its fixed point. Its remaining semigroup question concerns systems in which a state can have several tight actions, producing multiple possible matrices in the associated reachability analysis. With a unique tight action at every state, stabilization of matrix kernels supplies a decision procedure, but this argument fails for products of different matrices. Resolving the multiple-action case would extend exact reachability analysis beyond the linear behavior of a single optimal policy.

[Read in atlas](index.html#TCS-1659) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2033 — Even if it is correct the complexity of the problem for 1-GVAS remains open.

A one-dimensional grammar-controlled vector addition system combines a nonnegative counter with transition sequences generated by a context-free grammar. The problem asks for the computational complexity of reachability in this model. The source discusses a proposed decidability argument cautiously and separates that issue from obtaining useful upper and lower complexity bounds. One difficulty is that very small grammars can generate enormous finite reachable sets, while the source lacks examples forcing more than exponentially long shortest derivations. Understanding this mismatch could reveal whether compact derivations permit efficient reachability analysis despite the numerical growth of counter values.

[Read in atlas](index.html#TCS-2033) · [Challenges of the Reachability Problem in Infinite-State Systems (Invited Paper)](https://doi.org/10.4230/LIPIcs.MFCS.2024.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2824 — We conjecture that if c(A1 , . . . , An ) is a formula defined in terms of the standard connectives, and we derive […]

Truth-table natural deduction derives introduction and elimination rules for a connective from its Boolean truth table. In constructive logic, those derived rules need not recover the meaning of a formula originally built from standard connectives. The source conjectures a sufficient syntactic condition for equivalence: the indicated disjuncts, implication antecedents, and negated subformulas must contain neither negation nor implication. Thus the sensitive positions are restricted to expressions built from monotone connectives, preventing some classical truth-table identifications from changing constructive meaning. Proving the conjecture would clarify which defined connectives can safely be reconstructed by this generic proof-rule generation method.

[Read in atlas](index.html#TCS-2824) · [Classical Natural Deduction from Truth Tables](https://doi.org/10.4230/LIPIcs.TYPES.2022.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3031 — We conjecture that Coq’s restriction preventing large elimination principles for non-sub-singleton propositions makes LEM and CT consistent in Coq.

Church's thesis, as a type-theoretic axiom, says that every total function from natural numbers to natural numbers has a computational realization. The law of excluded middle supplies classical reasoning about propositions, and its compatibility with that thesis depends on the surrounding logical rules. The source conjectures that both axioms can consistently coexist in Coq because elimination from general propositions into computational types is restricted. This restriction prevents some classical existence proofs from automatically producing data, especially without additional choice principles. A consistency model would clarify how classical propositional reasoning can be combined with a constructive account of all representable numerical functions.

[Read in atlas](index.html#TCS-3031) · [Church’s Thesis and Related Axioms in Coq’s Type Theory](https://doi.org/10.4230/LIPIcs.CSL.2021.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3152 — The characterization of the class of types satisfying this property is an open problem (a partial characterization is described in [46]).

The cited paper studies decidability questions about atomic polymorphism in a type-theoretic setting. The saved passage asks for a characterization of the types satisfying a particular property. A classification would explain which syntactic type forms permit the behavior established in the surrounding results. The source mentions a partial characterization, suggesting a gap between known sufficient conditions and the full class. The excerpt does not preserve the property itself, so it cannot safely be interpreted as a CSP polymorphism question merely because the same word appears in both subjects.

[Read in atlas](index.html#TCS-3152) · [What’s Decidable About (Atomic) Polymorphism?](https://doi.org/10.4230/LIPIcs.FSCD.2021.27)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3324 — The decidability of Th(Rexp ) is an open problem and hinges upon Schanuel’s conjecture [24].

The first-order theory of the real exponential field allows quantified arithmetic formulas containing the exponential function. The project asks whether truth of every sentence in that theory can be decided by an algorithm. Adding exponentiation moves beyond the polynomial real arithmetic handled by classical elimination methods. The source explains how Schanuel's conjecture would imply decidability and uses that connection for weighted-automaton comparison problems. An unconditional answer would settle a basic computational question about real transcendental arithmetic with consequences for several verification reductions.

[Read in atlas](index.html#TCS-3324) · [The Big-O Problem for Labelled Markov Chains and Weighted Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2020.41)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3332 — It is an open problem whether an analogous result can be proved for accessible set functors in general.

Free completely iterative algebras give canonical solutions to recursive equations described by a functor. For finitary set functors, the source relates these solutions to ordered sequences of finite approximations in the corresponding free algebra. Its principal approximation theorem expresses solutions as joins of canonically defined ascending chains. The question is whether an analogous construction can be established for accessible set functors in general, where operations need not be finitary. Such an extension would explain how recursive semantics can still be recovered from approximations when the underlying descriptions admit larger arities and require a broader notion of accessibility.

[Read in atlas](index.html#TCS-3332) · [On Free Completely Iterative Algebras](https://doi.org/10.4230/LIPIcs.CSL.2020.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3344 — In particular we emphasize that even decidability of the Rounded P2P Problem in the case of a 2D rotation matrix remains open.

Rounded linear dynamics repeatedly applies a rational matrix and then rounds coordinates to a fixed digital grid. Point-to-point reachability asks whether the resulting orbit ever visits a specified target vector exactly. The source highlights the decidability problem even when the matrix is a rotation in two dimensions. Although unrounded rotation is simple, accumulated rounding errors can produce discrete orbits whose boundedness and eventual periodicity are difficult to control. Resolving this case, with the rounding rule specified as in the model, would clarify a basic limit of verification for numerical systems operating at fixed precision.

[Read in atlas](index.html#TCS-3344) · [Reachability in Dynamical Systems with Rounding](https://doi.org/10.4230/LIPIcs.FSTTCS.2020.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3401 — We leave the decidability status open for Dsum, but nevertheless show decidability for a large class, namely when the discount factor is of N the […]

Quantitative synthesis seeks a reactive transducer whose finite executions achieve values specified by a weighted automaton. In approximate synthesis, the output must remain within the prescribed tolerance of the best achievable value for the relevant input. The problem asks for decidability when execution values are discounted sums with a general permitted discount factor. The source handles the special factors 1/n using determinization results, but its techniques do not settle the full discounted-sum setting. A general decision procedure would determine when controllers can be synthesized to make uniformly near-optimal choices despite the differing influence of early and late actions.

[Read in atlas](index.html#TCS-3401) · [Synthesis from Weighted Specifications with Partial Domains over Finite Words](https://doi.org/10.4230/LIPIcs.FSTTCS.2020.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3479 — Can Markov chains with continuous emissions be model-checked efficiently?

A hidden Markov model can emit real-valued observations drawn from continuous distributions that depend on its hidden state. Such emissions describe measurements like durations or sensor readings more naturally than a fixed finite output alphabet. The source asks whether Markov chains with these continuous emissions admit efficient model-checking algorithms. Its framework for representing and comparing emission profiles provides a possible starting point, but the choice of distribution representation and specification language remains central. Developing suitable algorithms would extend probabilistic verification to observation models where enumerating all possible emitted values is impossible.

[Read in atlas](index.html#TCS-3479) · [Equivalence of Hidden Markov Models with Continuous Observations](https://doi.org/10.4230/LIPIcs.FSTTCS.2020.43)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3530 — Can the set of all winning strategies be described by finite-state automata?

Imperfect-information games can specify indistinguishable histories through synchronous two-tape automata. This is more general than giving the player observations produced by a sequential finite-state device. The project asks whether the entire collection of winning strategies against Nature can still be represented by finite-state automata. Strategies must respect the prescribed indistinguishability relation while satisfying a regular winning condition. Such a representation would extend automata-based synthesis beyond conventional observation models and provide a systematic way to describe all legal successful controllers.

[Read in atlas](index.html#TCS-3530) · [Observation and Distinction. Representing Information in Infinite Games](https://doi.org/10.4230/LIPIcs.STACS.2020.48)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3547 — It appears fairly straightforward to obtain results of this kind in semantics, but syntactic results are much murkier; similar conservativity questions for homotopy and cubical […]

Parametric cubical type theory combines computational paths and univalence with principles expressing uniform behavior of polymorphic functions. Those additional principles can prove statements unavailable in ordinary type theory, so unrestricted conservativity is not expected. The source proposes that proofs may still translate back when their assumptions and conclusions contain no function types. It identifies a gap between obtaining semantic conservativity results and constructing a corresponding translation or theorem at the level of syntax. Resolving that gap would explain which ordinary statements retain the same proof strength after adding powerful parametric and higher-dimensional reasoning tools.

[Read in atlas](index.html#TCS-3547) · [Internal Parametricity for Cubical Type Theory](https://doi.org/10.4230/LIPIcs.CSL.2020.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3655 — As mentioned in Section 4.2.2, it also remains an open problem whether IITs are reducible to inductive types in a UIP-free setting.

Inductive-inductive types define several mutually dependent sorts, allowing later sorts to be indexed by earlier ones. They conveniently express structures such as contexts and the types that are well formed within those contexts. The question asks whether these types can be constructed from ordinary inductive types without assuming uniqueness of identity proofs. The source's reduction relies on settings where equality is simpler, and removing that assumption requires rebuilding signatures, semantics, and the term-model construction. A successful reduction would show that this useful dependent form of mutual induction does not require an additional primitive in a richer theory of equality.

[Read in atlas](index.html#TCS-3655) · [For Finitary Induction-Induction, Induction Is Enough](https://doi.org/10.4230/LIPIcs.TYPES.2019.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3839 — We do not know whether an exponential bound on kMV k holds for any class of afmp-Z-VASS.

Affine integer vector addition systems update counters by matrix transformations followed by translations. When the transition matrices generate a finite monoid, reachability can be reduced to an ordinary integer counter system whose size depends on the monoid's representation. The source asks whether an exponential bound on that representation measure holds uniformly across all such finite-monoid systems. Its examined subclasses satisfy the bound, but the general argument available there gives a much larger tower bound. Settling the issue would determine whether the finite-monoid restriction supports uniform efficient representations and stronger general upper bounds for affine reachability.

[Read in atlas](index.html#TCS-3839) · [Affine Extensions of Integer Vector Addition Systems with States](https://doi.org/10.4230/LIPIcs.CONCUR.2018.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3904 — It remains an open question whether the predicative universes in the cubical assembly model satisfy the propositional resizing axiom.

Propositional resizing says that a proposition living in a large universe has an equivalent representative in a smaller universe. The cubical assembly model combines realizability-style computational information with a semantics for cubical type theory and univalence. The source disproves a resizing principle for its impredicative universe and separately asks whether its predicative universes satisfy resizing. These predicative universes are available under the stated metatheoretic assumption of Grothendieck universes, so the earlier counterexample does not automatically decide their behavior. Resolving the question would distinguish which size principles are compatible with this computational interpretation of higher-dimensional type theory.

[Read in atlas](index.html#TCS-3904) · [Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing](https://doi.org/10.4230/LIPIcs.TYPES.2018.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4017 — Is it possible to axiomatise the positive calculus of relations with transitive closure?

The positive calculus of binary relations combines operations such as union, composition, and intersection without unrestricted complementation. Adding transitive closure makes it possible to express repeated transitions and reachability. The source asks for a sound and complete axiomatization, including whether Kleene algebra axioms suffice alongside a complete axiomatization of representable allegories. Intersection is the main obstacle, since fragments without it admit stronger existing algebraic completeness results. A satisfactory axiom system would support systematic equational proofs about relational programs and graph paths using a manageable collection of general reasoning principles.

[Read in atlas](index.html#TCS-4017) · [On the Positive Calculus of Relations with Transitive Closure](https://doi.org/10.4230/LIPIcs.STACS.2018.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4072 — We also leave it as an open problem to characterize the functors that admit a disjunctive basis.

Coalgebraic modal logic uses a functor to specify the kind of transition structure being described, such as nondeterministic or weighted behavior. A disjunctive basis supplies normal forms that organize modal formulas in a way useful for automata constructions and completeness arguments. The problem is to characterize exactly which functors admit such a basis. The source studies properties and constructions of disjunctive bases, but these examples do not yet amount to a general structural criterion. A characterization would make it possible to predict when broad modal and fixpoint-logic techniques apply directly from the underlying transition model.

[Read in atlas](index.html#TCS-4072) · [Disjunctive Bases: Normal Forms for Modal Logics](https://doi.org/10.4230/LIPIcs.CALCO.2017.11)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4078 — However, the important question about whether finite-memory suffices for the infinite-horizon optimal path problem or infinite memory is needed remains open.

A reward-collecting robot moves through a graph where rewards appear randomly and may disappear before collection. Its best route depends on past visits and the changing prospects at different locations. The source asks whether an optimal infinite-horizon strategy always needs only finite memory. Remembering just the most recent visit times is already insufficient in its analysis. The project aims to determine whether exact long-term optimization has a finite-state representation or requires an unbounded history-dependent policy.

[Read in atlas](index.html#TCS-4078) · [The Robot Routing Problem for Collecting Aggregate Stochastic Rewards](https://doi.org/10.4230/LIPIcs.CONCUR.2017.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4081 — Finally, we leave open the problem of finding a sound and complete axiomatization for ITLe .

The intuitionistic temporal logic ITL^e combines an information ordering with a monotone next-time function on its models. Its implication respects growth of information, while temporal modalities describe how states evolve. The source proves decidability of satisfiability and validity using a strong finite-model property, then asks for a sound and complete axiomatization. The goal is a proof system deriving exactly the formulas valid in these models, with rules reflecting the interaction between temporal evolution and constructive implication. Such an axiomatization would complement semantic decision procedures with a transparent deductive foundation for reasoning about constructive temporal specifications.

[Read in atlas](index.html#TCS-4081) · [A Decidable Intuitionistic Temporal Logic](https://doi.org/10.4230/LIPIcs.CSL.2017.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4093 — The complexity of reachability for two-dimensional branching VASS

A branching counter-system run combines two child configurations by adding their counters and a transition displacement. Reachability asks whether a given configuration has a finite run tree rooted there and ending in allowed zero-counter leaves. The 2017 question concerns the complexity of this task with two counters and binary numerical data. Decidability was proved in 2025, but the checked sources leave an explicit complexity classification open. This revision preserves that remaining question and marks the source’s unspecified requirement for matching time or space bounds.

[Read in atlas](index.html#TCS-4093) · [Polynomial-Space Completeness of Reachability for Succinct Branching VASS in Dimension One](https://doi.org/10.4230/LIPIcs.ICALP.2017.119) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.22) · [Bridging the Gap Between Plain VASS and Branching VASS](https://link.springer.com/chapter/10.1007/978-3-032-22730-0_4) · [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear Inductive Invariants](https://arxiv.org/abs/2607.09558v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4124 — While the problem of modular separability is ExpSpace-hard, we do not know whether it is as hard as the VAS reachability problem.

A modular set of integer vectors is a union of coordinatewise residue classes for some common modulus. Modular separability asks whether such a set can contain one vector-addition-system reachability set while staying disjoint from another. The source proves EXPSPACE-hardness and asks whether this problem is as hard as the full VAS reachability problem. A straightforward singleton-separation argument works for richer unary separators, but modular sets cannot isolate configurations in the same way. Resolving the comparison would measure how much computational difficulty remains when the separating invariant is restricted to periodic arithmetic information.

[Read in atlas](index.html#TCS-4124) · [Separability of Reachability Sets of Vector Addition Systems](https://doi.org/10.4230/LIPIcs.STACS.2017.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4138 — It is an open problem whether coalgebraic type functors of interest on convex sets are proper, e.g. the functor F X = [0, 1] × […]

Coalgebraic systems over convex sets represent behaviors that respect probabilistic mixing. Properness is a structural property ensuring that equivalence of finitely generated behaviors can be witnessed through suitable finite algebraic coalgebras. The source asks whether important functors on convex sets are proper, highlighting F(X) = [0,1] × X^Σ as a concrete example. Its existing sufficient conditions encounter trouble because finitely generated convex sets are not closed under the kernel-pair constructions they require. A proof or counterexample would clarify when the rational fixed point faithfully captures finite probabilistic behavior inside the final behavioral model.

[Read in atlas](index.html#TCS-4138) · [Proper Functors and their Rational Fixed Point](https://doi.org/10.4230/LIPIcs.CALCO.2017.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4302 — However, the strategy synthesis problem for multi-objective probabilistic LTL properties in general stochastic games remains open.

Multi-objective probabilistic synthesis asks one strategy to satisfy several quantitative requirements simultaneously in a stochastic game. When the requirements are probabilistic LTL properties, each combines an infinite-run temporal condition with a probability constraint. The source identifies strategy synthesis for these objectives in general stochastic games as the missing case beyond its restricted algorithms. A controller may need to balance conflicting objectives while accounting for both random transitions and adversarial choices. Resolving the problem would extend automated construction of strategies that meet several reliability or performance requirements, with explicit control over their achievable tradeoffs.

[Read in atlas](index.html#TCS-4302) · [Model Checking and Strategy Synthesis for Stochastic Games: From Theory to Practice (Invited Talk)](https://doi.org/10.4230/LIPIcs.ICALP.2016.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4461 — The converse holds at least assuming function extensionality; we do not know whether this assumption is necessary.)

Propositional extensionality identifies logically equivalent propositions, whereas propositional univalence identifies equality with the appropriate notion of equivalence between propositions. The source observes that propositional univalence implies extensionality and obtains the converse when function extensionality is assumed. The question is whether that extra assumption is necessary for the converse. This is a foundational dependency problem about the exact strength of equality principles in intensional dependent type theory. Removing the assumption or constructing a separating model would clarify how much information about functions is needed to turn logical equivalence of propositions into the univalent account of their identity.

[Read in atlas](index.html#TCS-4461) · [Parametricity, Automorphisms of the Universe, and Excluded Middle](https://doi.org/10.4230/LIPIcs.TYPES.2016.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4478 — The decidability status of 1cSL1 [BG] (and of 1cSL[BG]) model checking remains open.

One-counter Strategy Logic extends strategic temporal reasoning with assertions about an unbounded numerical counter. Its Boolean-goal fragment can combine several properties under explicitly quantified and assigned strategies. The source asks whether model checking is decidable, already for the indicated single-level fragment and consequently for the full Boolean-goal logic. It establishes eventual periodicity of satisfying counter values, but does not obtain an effective procedure that computes the necessary periodic sets. Bridging this effectiveness gap would turn a structural description of winning configurations into an algorithm for verifying strategic behavior in counter-based systems.

[Read in atlas](index.html#TCS-4478) · [Weighted Strategy Logic with Boolean Goals Over One-Counter Games](https://doi.org/10.4230/LIPIcs.FSTTCS.2015.69)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4564 — We conjecture that it has a presheaf model in a univalent metatheory (as some equations are only validated up to isomorphism – note that this […]

The source proposes a cubical type theory in which equality is defined recursively from type structure and geometric cubes arise from those definitions. This differs from introducing an interval object first and interpreting paths as interval-indexed functions. The conjecture asks for a presheaf model of the proposed theory within a univalent metatheory. The intended role of univalence is to address equations that the construction naturally validates only up to isomorphism. Establishing the model would provide a semantic foundation for this alternative account of equality and clarify whether its coherence requirements can be met.

[Read in atlas](index.html#TCS-4564) · [Towards a Cubical Type Theory without an Interval](https://doi.org/10.4230/LIPIcs.TYPES.2015.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4577 — While smaller instances have been shown to be decidable, the full decidability of Skolem’s problem is still an open question [15].

A linear recurrence generates each term from a fixed linear combination of preceding terms. Skolem's problem asks whether an integer recurrence ever takes the value zero. The saved textbook note highlights the general decision problem and the unresolved order-five case in its source inventory. An algorithm would need to certify absence of a zero across an infinite sequence, not merely inspect a long prefix. The historical notes distinguish results for smaller instances from the full problem and do not amount to a fresh verification of subsequent decidability progress.

[Read in atlas](index.html#TCS-4577) · [Information Leakage of Non-Terminating Processes](https://doi.org/10.4230/LIPIcs.FSTTCS.2014.517)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4640 — The problem: does the sequence beginning with x0 reach a given value y?

An orbit problem asks whether repeated application of a given transformation to an initial value ever reaches a specified target. The retained sentence appears in a discussion of piecewise-affine integer dynamics and its connections to program termination. The 2013 source reports decidability and complexity results that change sharply with the transformation class and dimension. It also recalls a polynomial-time solution for linear transformations over rational vector spaces, illustrating why those model distinctions matter. The extracted sentence introduces the orbit problem rather than specifying one of the paper's subsequent open questions, so this working summary does not turn it into an unsupported open-status claim.

[Read in atlas](index.html#TCS-4640) · [Mortality of Iterated Piecewise Affine Functions over the Integers: Decidability and Complexity (Extended Abstract)](https://doi.org/10.4230/LIPIcs.STACS.2013.514)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5682 — On Piecewise Affine Reachability with Bellman Operators — Explicit open question on PDF page 2

A piecewise affine map chooses among finitely many affine update rules according to the region containing the current point. In one dimension, its orbit is obtained by repeatedly applying this update to a rational starting value. The question asks whether exact reachability of a rational target is decidable in the general one-dimensional setting, even with only two pieces. The source contrasts this gap with decidable subclasses and with undecidability already available for unrestricted two-dimensional maps. Resolving the two-piece case would locate a basic boundary between simple numerical iteration and computations complicated enough to defeat algorithmic reachability analysis.

[Read in atlas](index.html#TCS-5682) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5737 — A Lambda Calculus Satellite (Invited Talk) — Explicit open question on PDF page 5

The S-only fragment of combinatory logic builds terms from application and the single combinator satisfying Sxyz = xz(yz). Interconvertibility asks whether two such terms can be connected by forward or backward uses of the weak reduction rule. The source distinguishes this equality problem from normalization and head-reduction termination, for which decision procedures are available in the fragment. It also notes that identical Berarducci trees need not imply interconvertibility, so a natural infinite-tree semantics does not immediately decide equality. An algorithm or undecidability proof would establish the remaining computational strength of this particularly small rewriting language.

[Read in atlas](index.html#TCS-5737) · [A Lambda Calculus Satellite (Invited Talk)](https://doi.org/10.4230/LIPIcs.FSCD.2023.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5817 — Domain Theory in Constructive and Predicative Univalent Foundations — Explicit open question on PDF page 5

Univalent foundations treats equivalence of types as a form of equality while supporting constructive mathematical reasoning. Propositional impredicativity principles allow certain quantifications or size changes for propositions beyond ordinary predicative universe rules. The source identifies the challenge of giving these principles a computational interpretation compatible with univalence. Its domain-theoretic development avoids the resizing axioms, demonstrating that useful semantics can be built while the stronger computational foundation is unsettled. A successful interpretation would explain how proofs using impredicative propositions can retain meaningful computation and would broaden the foundational tools available for constructive domain theory.

[Read in atlas](index.html#TCS-5817) · [Domain Theory in Constructive and Predicative Univalent Foundations](https://doi.org/10.4230/LIPIcs.CSL.2021.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5823 — Scope-Bounded Reachability in Valence Systems — Explicit open question on PDF page 8

Valence systems combine finite-state transitions with algebraic storage operations. The source studies bounded forms of execution that recover decidability from otherwise difficult reachability problems. Its cited question concerns unrestricted reachability for the particular graph family denoted SCm. These storage graphs are expressive enough to represent a broad range of other decidable cases through reductions. The project asks whether their shared algebraic structure still permits an effective reachability procedure, making them a significant boundary family for infinite-state verification.

[Read in atlas](index.html#TCS-5823) · [Scope-Bounded Reachability in Valence Systems](https://doi.org/10.4230/LIPIcs.CONCUR.2021.29)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5876 — Reachability in Dynamical Systems with Rounding — Unresolved-question passage on page 14

Repeatedly rotating a point and rounding it back to a fixed grid produces a discrete approximation of planar rotation. The source conjectures that the rounded orbits in its setting eventually become periodic. Experiments exhibit several geometric orbit shapes but do not produce an orbit that continues visiting new grid points forever. The challenge is to control accumulated errors when rounding may move coordinates either upward or downward, unlike simpler monotone truncation effects. Proving eventual periodicity under the intended rounding assumptions would also provide a route to deciding exact reachability by detecting repetition during orbit exploration.

[Read in atlas](index.html#TCS-5876) · [Reachability in Dynamical Systems with Rounding](https://doi.org/10.4230/LIPIcs.FSTTCS.2020.36)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5911 — Decidability of Graph Neural Networks via Logical Characterizations — Unresolved-question passage on page 19

Graph neural networks compute classifications by repeatedly aggregating information from neighboring vertices and applying activation functions. The source connects restricted network architectures with decidable logics to analyze whether a specified classification is achievable. The selected passage broadens this into verification under logical assumptions on the input graph, rather than stating a single new isolated conjecture. For example, one can ask whether the network produces a target label on any graph satisfying an additional formula expressible in the same decidable logic. Developing this direction would turn expressiveness characterizations into tools for checking structured requirements on learned graph computations.

[Read in atlas](index.html#TCS-5911) · [Decidability of Graph Neural Networks via Logical Characterizations](https://doi.org/10.4230/LIPIcs.ICALP.2024.127)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5915 — From Cubes to Twisted Cubes via Graph Morphisms in Type Theory — Explicit open question on PDF page 2

Simplicial sets describe spaces through points, edges, triangles, and their higher-dimensional analogues, making them natural models for homotopy type theory. The source recalls a univalent simplicial model and asks how to obtain a constructive simplicial model with univalent universes. Constructivity requires the semantic constructions to work without the classical principles used in the original account. Cubical models provide an encouraging comparison, since a constructive treatment of univalence is available there. Solving the simplicial problem would clarify whether the familiar simplex-based geometry can support the same constructive foundations and computational ambitions as the cubical approach.

[Read in atlas](index.html#TCS-5915) · [From Cubes to Twisted Cubes via Graph Morphisms in Type Theory](https://doi.org/10.4230/LIPIcs.TYPES.2019.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5975 — About Decisiveness of Dynamic Probabilistic Models — Explicit open question on PDF page 3

A probabilistic transition system is decisive for a target when it almost surely eventually reaches either the target or states from which the target is unreachable. This property supports approximation of reachability probabilities in infinite-state models such as probabilistic Petri nets. The source discusses deciding decisiveness for finite targets and for transition weights that depend on the current marking. Its own results resolve a substantial dynamic-weight case negatively, proving undecidability for polynomial weights even with finite or upward-closed targets. The description therefore separates that established limitation from the more specific constant-weight and restricted-model questions motivating the paper.

[Read in atlas](index.html#TCS-5975) · [About Decisiveness of Dynamic Probabilistic Models](https://doi.org/10.4230/LIPIcs.CONCUR.2023.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5987 — Two Lower Bounds for BPA — Explicit open question on PDF page 1

Basic Process Algebra describes recursive sequential processes with a stack-like arrangement of process variables. Weak bisimilarity compares their observable behavior while allowing silent transitions to be hidden. The question asks whether this equivalence is decidable even for normed BPA, where each process variable can eventually terminate. The source distinguishes this from branching bisimilarity, a finer equivalence for which decidability and complexity results are available in the normed setting. An answer would clarify whether arbitrary invisible computation can be handled effectively in one of the simplest infinite-state models of recursive behavior.

[Read in atlas](index.html#TCS-5987) · [Two Lower Bounds for BPA](https://doi.org/10.4230/LIPIcs.CONCUR.2017.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6036 — Invariants for Continuous Linear Dynamical Systems — Explicit open question on PDF page 4

First-order theories of the real numbers become more expressive when exponential and trigonometric functions are added. The selected question concerns decidability for restricted elementary functions, both with and without unrestricted exponentiation. Restricting sine and cosine to bounded intervals avoids the unrestricted oscillation that would immediately complicate logical descriptions. The source cites decidability conditional on Schanuel's conjecture and uses these theories to synthesize invariants of continuous linear systems. An unconditional decision procedure would remove a number-theoretic assumption from reasoning about these analytic descriptions and the safety properties they can certify.

[Read in atlas](index.html#TCS-6036) · [Invariants for Continuous Linear Dynamical Systems](https://doi.org/10.4230/LIPIcs.ICALP.2020.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6107 — A Decidable Intuitionistic Temporal Logic — Unresolved-question passage on page 15

Intuitionistic temporal logic combines constructive implication with operators describing the evolution of information over time. The persistent-model version ITL^p imposes stronger compatibility conditions between the information order and temporal transition than the expanding version. The source shows that persistent models lack the finite-model property and asks whether the resulting logic is undecidable. Failure of finite models alone does not settle this, because a different algorithm could still reason effectively about infinite structures. Resolving the question would show whether stronger persistence makes this temporal semantics fundamentally harder to analyze than its decidable expanding counterpart.

[Read in atlas](index.html#TCS-6107) · [A Decidable Intuitionistic Temporal Logic](https://doi.org/10.4230/LIPIcs.CSL.2017.14)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6112 — Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing — Unresolved-question passage on page 16

An impredicative universe supports quantification over types without the usual increase in universe size, while univalence connects equivalence with equality. Propositional resizing adds the requirement that large propositions have equivalent small representatives. The source asks for a model of type theory supporting all three features together. Its cubical assembly construction provides univalence and impredicativity but fails resizing, and a related positive model weakens identity and dependent-product structure. Constructing a model with the intended ordinary type-theoretic rules would clarify whether these attractive foundational principles can coexist without sacrificing essential forms of dependent reasoning.

[Read in atlas](index.html#TCS-6112) · [Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing](https://doi.org/10.4230/LIPIcs.TYPES.2018.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6245 — Involved VASS Zoo (Invited Talk) — Explicit open question on PDF page 3

Reachability in a three-dimensional vector addition system asks for a legal counter run connecting an initial and a target configuration. The source highlights the gap in understanding how long the shortest such run may need to be. Its concrete question is whether existence of any run always guarantees one of at most exponential length in the input size. Known short-run arguments in two dimensions motivate this possibility, while much larger general upper bounds leave room for doubly exponential or faster growth. Settling the witness-length question would illuminate why adding a third counter changes the structure of exact reachability.

[Read in atlas](index.html#TCS-6245) · [Involved VASS Zoo (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2022.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6259 — On the Skolem Problem for Reversible Sequences — Explicit open question on PDF page 2

Skolem's problem asks whether a linear recurrence has a zero term. The cited source focuses on reversible sequences and recalls structural theorems describing zero sets. The saved passage emphasizes that known proofs of the Skolem–Mahler–Lech theorem are nonconstructive. A constructive decision procedure would need an effective way to turn that qualitative structure into a finite stopping test. The excerpt truncates its conclusion and does not state reversibility conventions, so it cannot itself establish a new decidability claim for either the general or restricted problem.

[Read in atlas](index.html#TCS-6259) · [On the Skolem Problem for Reversible Sequences](https://doi.org/10.4230/LIPIcs.MFCS.2022.61)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6279 — Guarded Kleene Algebra with Tests: Coequations, Coinduction, and Completeness — Explicit open question on PDF page 12

Regular expressions can describe branching processes as well as word languages, and bisimulation compares their stepwise behavior. Milner's completeness question asks whether the proposed axiom system proves every equality between bisimilar regular-expression processes. This is stronger than checking that the axioms are sound and differs from the familiar equational theory of language equivalence. The 2021 source suggests using coequations and coalgebraic methods developed for Guarded Kleene Algebra with Tests to advance the completeness argument. The research project connects operational process semantics with a deductive account of iteration, choice, and sequential composition.

[Read in atlas](index.html#TCS-6279) · [Guarded Kleene Algebra with Tests: Coequations, Coinduction, and Completeness](https://doi.org/10.4230/LIPIcs.ICALP.2021.142)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6343 — Characterizing Omega-Regularity Through Finite-Memory Determinacy of Games on Infinite Graphs — Explicit open question on PDF page 6

Strategies in infinite graph games may remember either general play information or only the sequence of observed colors. These give different notions of finite memory. The source asks whether some winning condition needs only finite general memory but unbounded chromatic memory on infinite arenas. Conversions known for other settings do not settle this case. The project would clarify whether remembering arena-specific details can fundamentally outperform color-based memory, affecting how strategy complexity characterizes classes of infinite-word objectives.

[Read in atlas](index.html#TCS-6343) · [Characterizing Omega-Regularity Through Finite-Memory Determinacy of Games on Infinite Graphs](https://doi.org/10.4230/LIPIcs.STACS.2022.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6359 — On Decidability of Concurrent Kleene Algebra — Explicit open question on PDF page 2

Concurrent Kleene algebra represents executions as partially ordered multisets of events, preserving distinctions between sequential and parallel behavior. Refinement compares such executions by allowing additional ordering, and the interchange law captures a basic relationship between sequential and parallel composition. The quoted question concerns decidability and completeness for refinement of expressions with iteration. The source itself settles the decision problem for series-rational expressions without parallel iteration, proving EXPSPACE-completeness, while the broader signature and axiomatization questions are distinct. This distinction matters when deciding whether a concurrent specification permits an implementation with a greater degree of sequentialization.

[Read in atlas](index.html#TCS-6359) · [On Decidability of Concurrent Kleene Algebra](https://doi.org/10.4230/LIPIcs.CONCUR.2017.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7153 — Decide eventual nonnegativity for arbitrary linear recurrences, already unresolved at order six.

An integer linear recurrence generates each term as a fixed linear combination of a bounded number of preceding terms. Ultimate positivity asks whether all sufficiently late terms are nonnegative, permitting finitely many earlier exceptions. The cited survey identifies decidability for arbitrary recurrences as the central task and highlights the difficulty already at order six. Simple recurrences, whose characteristic roots are distinct, admit a different positive result, so repeated roots are an important part of the unresolved general setting described there. An algorithm would support reasoning about eventual sign behavior and termination conditions in linear dynamical programs.

[Read in atlas](index.html#TCS-7153) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7154 — Compute eventual-positivity thresholds for simple recurrences beyond the established low-order cases.

For simple linear recurrence sequences, the cited survey distinguishes deciding eventual nonnegativity from computing when it begins. The task asks for an effective threshold N after which every term is nonnegative, whenever such a threshold exists. Available general decidability arguments use noneffective Diophantine approximation bounds and therefore need not produce this numerical witness. Computing it would allow all earlier terms to be checked directly, giving a route to deciding positivity of the entire sequence beyond the established low-order cases. The problem exposes a concrete gap between proving an eventual property algorithmically and extracting a usable bound on its exceptional prefix.

[Read in atlas](index.html#TCS-7154) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7156 — Decide termination over all integer starting states for general affine linear loops with nondiagonalizable updates.

An affine linear loop repeatedly updates an integer vector by a matrix transformation and translation while a conjunction of linear inequalities holds. Universal integer termination asks whether every integer initial vector eventually leaves the guard. The 2015 survey's generalization target removes the assumption that the update matrix is diagonalizable. Its existing results exploit spectral and arithmetic structure in the diagonalizable case, while repeated eigenvalue blocks introduce additional polynomial factors into the trajectories. Understanding the general case would connect the algebra of linear updates with a complete termination analysis over discrete initial states, rather than real or rational starting spaces.

[Read in atlas](index.html#TCS-7156) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7157 — Decide termination for loops whose updates are general linear constraints between successive states.

A linear-constraint loop specifies its next state by a conjunction of linear inequalities relating the old and new variable values. This permits several possible successors, unlike a loop whose body is a single fixed affine assignment. The source asks for a decision procedure for termination in this more general relational model. It identifies octagonal constraints as a positive special case, where the transition relation has an effectively semilinear transitive closure. Extending beyond that fragment would show whether unbounded executions can still be characterized effectively when each iteration chooses among all numerical updates satisfying general linear constraints.

[Read in atlas](index.html#TCS-7157) · [On Linear Recurrence Sequences and Loop Termination](https://people.mpi-sws.org/~joel/publications/lrs-survey15abs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5600 — An elementary upper bound for vector-addition-system reachability

A vector addition system repeatedly adds permitted integer vectors while keeping every counter nonnegative. Exact reachability asks whether a given initial vector can reach a specified target after finitely many such steps. The historical question asks whether one algorithm can decide all instances within a fixed-height tower of exponentials in the input length. The non-elementary lower bound published at STOC 2019 and in JACM 2021 rules out every such bound. The card therefore records a resolved negative answer, with the general model kept separate from the polynomial-growth subclass named in the original paper.

[Read in atlas](index.html#TCS-5600) · [Polynomial Vector Addition Systems With States](https://doi.org/10.4230/LIPIcs.ICALP.2018.134) · [The Reachability Problem for Petri Nets Is Not Elementary](https://doi.org/10.1145/3422822) · [Reachability in Vector Addition Systems is Ackermann-complete](https://arxiv.org/abs/2104.13866v4) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.22)
Existing status: `resolved` · Summary written: 2026-09-11

## Distributed, parallel and sublinear algorithms (111)

### TCS-6553 — Can every polynomial-time decision problem be efficiently parallelized?

NC describes computations with polynomial total circuit size and only polylogarithmic dependency depth, under a uniformity requirement. The question asks whether every problem solvable in polynomial sequential time belongs to this parallel class. Circuit Value is a concrete complete problem: given a circuit and its input, compute the designated output. An NC algorithm for circuit evaluation would therefore parallelize every problem in P. The challenge is to distinguish a long chain in the supplied circuit from an unavoidable chain in every possible algorithm for evaluating its behavior.

[Read in atlas](index.html#TCS-6553) · [Limits to Parallel Computation: P-Completeness Theory](https://homes.cs.washington.edu/~ruzzo/papers/limits.pdf) · [The circuit value problem is log space complete for P](https://doi.org/10.1145/990518.990519) · [Separation of the monotone NC hierarchy](https://weizmann.esploro.exlibrisgroup.com/esploro/outputs/journalArticle/Separation-of-the-monotone-NC-hierarchy/993263130303596) · [Monotone Circuit Complexity of Matching](https://arxiv.org/abs/2507.16105v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6556 — Directed reachability with nearly linear memory and polylogarithmic passes

Directed reachability in a stream asks whether one vertex can reach another when graph edges arrive in an adversarial order. Nearly linear memory in the vertex count cannot store every edge of a dense graph. The question asks for a randomized algorithm using only polylogarithmically many passes and n times a polylogarithmic number of memory bits. Simple repeated scans can propagate reachability one step at a time, taking many passes on badly ordered paths. The project is to combine a small memory footprint with far fewer scans without relying on favorable edge order.

[Read in atlas](index.html#TCS-6556) · [Recent Advances in Multi-Pass Graph Streaming Lower Bounds](https://par.nsf.gov/servlets/purl/10488812) · [Superlinear lower bounds for multipass graph processing](https://eccc.weizmann.ac.il/report/2013/002/revision/3/download/) · [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841) · [Semi-Streaming Bipartite Matching in Fewer Passes and Optimal Space](https://arxiv.org/abs/2011.03495) · [Almost Optimal Super-Constant-Pass Streaming Lower Bounds for Reachability](https://par.nsf.gov/servlets/purl/10315017) · [Streaming Algorithms for Monotonicity Testing](https://arxiv.org/abs/2608.07073v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6504 — Is perfect matching in general graphs in deterministic NC?

Perfect matching seeks pairwise disjoint edges that cover every vertex of a graph. The question asks for a deterministic parallel algorithm on general graphs with polynomially many processors and polylogarithmic running time. Sequential polynomial-time algorithms do not supply this bound because their matching updates may depend on earlier choices. General graphs also contain odd cycles, which require coordination beyond the constraints that suffice in bipartite graphs. The saved card distinguishes this target from the nearby bipartite advance and asks whether compatible matching decisions can be organized efficiently in parallel without randomness.

[Read in atlas](index.html#TCS-6504) · [The Matching Problem in General Graphs Is in Quasi-NC](https://doi.org/10.1109/FOCS.2017.70) · [Bipartite Matching is in NC](https://eccc.weizmann.ac.il/report/2026/100/)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6554 — Distributed Lovász Local Lemma in O(log log n) rounds

The distributed Lovasz Local Lemma seeks an assignment avoiding many bad events, each depending on only a bounded number of other events. Processors know local portions of this dependency structure and communicate in synchronous LOCAL rounds. The question asks for O(log log n) rounds with high probability when the dependency degree is constant and the probability criterion has sufficiently strong constant polynomial slack. The guarantee must bound the worst finishing time over all nodes. An algorithm that achieves only a small average finishing time would leave the central coordination issue unresolved for the last remaining bad events.

[Read in atlas](index.html#TCS-6554) · [Sublogarithmic Distributed Algorithms for Lovász Local Lemma, and the Complexity Hierarchy](https://arxiv.org/abs/1705.04840) · [On the Locality of the Lovász Local Lemma](https://arxiv.org/abs/2502.11690)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6555 — Optimal exact single-source shortest paths in CONGEST

Single-source shortest paths asks every vertex to learn its exact distance from one source in a weighted network. In CONGEST, each edge carries only a logarithmic number of bits per communication round. The target is a randomized algorithm using roughly sqrt(n) plus the hop diameter D rounds, ignoring polylogarithmic factors. The graph is undirected and connected, with nonnegative polynomially bounded integer edge weights. Achieving this bound would combine global distance propagation with the bandwidth limits of the network at the scale identified by the saved problem statement.

[Read in atlas](index.html#TCS-6555) · [Polylogarithmic time algorithms for shortest path forests in programmable matter](https://link.springer.com/article/10.1007/s00446-026-00505-2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6557 — Explicit superconstant lower bounds in the congested clique

Can a graph predicate that is easy to compute centrally require a number of congested-clique rounds tending to infinity? Each processor initially knows its incident graph edges and can send a different logarithmic-size message to every other processor in each round. Only one decision bit is required, and local computation is unrestricted. Known hard-function counting and hierarchy arguments do not provide the required centrally polynomial-time predicate. Broadcast bounds and the known two-round MST limitation do not resolve this unicast one-bit target.

[Read in atlas](index.html#TCS-6557) · [On the Power of the Congested Clique Model](https://people.csail.mit.edu/andyd/cong_clique_podc14.pdf) · [Towards a complexity theory for the congested clique](https://jukkasuomela.fi/doc/clique-complexity.pdf) · [What Can We Compute in a Single Round of the Congested Clique?](https://arxiv.org/abs/2210.02638v4)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6507 — Can directed reachability have near-linear work and polylogarithmic depth?

A parallel reachability algorithm must identify every vertex reachable from a source in a directed graph. The target combines nearly linear total work in the input size with polylogarithmic depth, using randomization and high-probability correctness. Ordinary graph search does little work but can expose a long sequence of dependent frontiers. Highly parallel transitive-closure methods may perform far more work than this one-source task requires. The question is whether shortcuts or another representation can remove long dependencies while accounting for the cost of constructing all auxiliary information.

[Read in atlas](index.html#TCS-6507) · [Parallel Reachability and Shortest Paths on Non-Sparse Digraphs: Near-Linear Work and Sub-Square-Root Depth](https://doi.org/10.4230/LIPIcs.ICALP.2026.15) · [Parallel Reachability in Almost Linear Work and Square Root Depth](https://arxiv.org/abs/1905.08841) · [Õ(1)-Depth Parallel Reachability Faster than Transitive Closure](https://arxiv.org/abs/2608.13231)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7172 — Is finding a depth-first-search tree in deterministic NC?

A depth-first-search forest records the parent choices of recursive graph exploration. For an undirected graph, it is a rooted spanning forest in which every graph edge joins a vertex to one of its ancestors. The problem asks for a deterministic, uniformly specified parallel computation that constructs any such forest with polynomial resources and polylogarithmic depth. Randomized NC algorithms and deterministic results for restricted graph classes are known, but those guarantees do not settle the general target. A solution would show whether this basic search structure can always be built efficiently in parallel without random choices.

[Read in atlas](index.html#TCS-7172) · [Parallel Complexity of Depth-First-Search and Maximal Path in Restricted Graph Classes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2025.23) · [A random NC algorithm for depth first search](https://doi.org/10.1007/BF02122548) · [Nearly Work-Efficient Parallel DFS in Undirected Graphs](https://arxiv.org/abs/2304.09774)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0522 — Quantum 3-coloring of cycles in o(log* n) rounds

Processors arranged on an oriented cycle must choose three classical colors so that adjacent processors receive different colors. The question allows quantum communication and asks for a round bound asymptotically smaller than log-star n. Nodes have distinct identifiers and know the cycle size, while their initial quantum registers are unentangled. The complete coloring must be valid with probability at least one minus one over n. A successful algorithm would beat the classical symmetry-breaking threshold, whereas a lower bound must handle quantum correlations without relying only on coarse causality constraints.

[Read in atlas](index.html#TCS-0522) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#quantum-local) · [Locality in Distributed Graph Algorithms](https://doi.org/10.1137/0221015) · [A Lower Bound on Probabilistic Algorithms for Distributive Ring Coloring](https://doi.org/10.1137/0404036) · [Finitely Dependent Coloring](https://doi.org/10.1017/fmp.2016.7) · [No Distributed Quantum Advantage for 3-Coloring Rooted Trees and 2-Coloring Even Cycles](https://arxiv.org/abs/2607.04852v2) · [Distributed Quantum Algorithms Cannot Color Cycles with Probability 1](https://arxiv.org/abs/2608.11720v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6499 — Can distributed MIS be solved in sublogarithmic time on every graph?

A maximal independent set contains no adjacent vertices and leaves every unselected vertex next to a selected one. The question asks for a randomized LOCAL algorithm that finds such a set in o(log n) rounds on every graph with high probability. Message sizes and local computation are unrestricted, so the resource measures the distance over which decisions must be coordinated. The running-time improvement must hold uniformly even for graphs of very large degree. Degree-sensitive algorithms already improve some cases, but the target requires a mechanism that also avoids logarithmically many phases on unrestricted graphs.

[Read in atlas](index.html#TCS-6499) · [Breaking Barriers for Distributed MIS by Faster Degree Reduction](https://arxiv.org/abs/2505.15652) · [An Improved Distributed Algorithm for Maximal Independent Set](https://arxiv.org/abs/1506.05093) · [Round Elimination via Self-Reduction: Closing Gaps for Distributed Maximal Matching](https://arxiv.org/abs/2505.15654)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6505 — One cycle versus two: is logarithmic time necessary in low-memory MPC?

The one-cycle-versus-two problem distinguishes a single n-vertex cycle from two disjoint cycles of half that size. In the low-memory MPC model, edges are spread across machines with sublinear local memory and linear total memory. The conjecture says randomized algorithms require Ω(log n) communication rounds under these resource bounds. Both input types have identical vertex counts, edge counts, and degrees, so only their global connectivity distinguishes them. A lower bound must handle arbitrary communication between machines and arbitrary encodings, rather than assuming information can travel only along graph edges.

[Read in atlas](index.html#TCS-6505) · [O(1)-Round MPC Algorithms for Multi-Dimensional Grid Graph Connectivity, Euclidean MST and DBSCAN](https://doi.org/10.4230/LIPIcs.ICDT.2025.7) · [Equivalence classes and conditional hardness in massively parallel computations](https://doi.org/10.1007/s00446-021-00418-2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6506 — Can deterministic LOCAL algorithms find an MIS in O(log n) rounds?

Deterministic maximal independent set algorithms must coordinate their choices using the graph and vertex identifiers alone. The question asks whether O(log n) LOCAL rounds suffice on every graph and every valid identifier assignment. The output must be independent and dominate all unselected vertices, without requiring maximum cardinality. Network decomposition already supports polylogarithmic deterministic algorithms, so the target is a sharper dependence on network size. Reaching the logarithmic bound would require organizing deterministic progress efficiently even when identifier patterns defeat simple greedy local rules.

[Read in atlas](index.html#TCS-6506) · [Near-Optimal Deterministic Network Decomposition and Ruling Set, and Improved MIS](https://arxiv.org/abs/2410.19516) · [Lower Bounds for Maximal Matchings and Maximal Independent Sets](https://arxiv.org/abs/1901.02441) · [Polylogarithmic-Time Deterministic Network Decomposition and Distributed Derandomization](https://arxiv.org/abs/1907.10937) · [Faster Distributed Δ-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0998 — Sketching vs. Streaming

A streaming algorithm compresses an input while processing it sequentially, whereas a sketch supports computation from independently prepared summaries. The source asks whether efficient streaming for symmetric functions can generally be converted into efficient sketching. It frames the issue through one-way communication versus simultaneous messages to a referee. The concrete challenge is to find natural functions with a substantial gap or establish a transformation under suitable symmetry assumptions. This would clarify when the ability to adapt a summary to previously processed data offers more power than independently summarizing the pieces.

[Read in atlas](index.html#TCS-0998) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0515 — Does sublinear deterministic volume always collapse to O(log* n)?

The VOLUME model measures how many graph vertices an adaptive local algorithm inspects to determine one requested output. Outputs from separate queries must still fit together into a single valid labeling. The conjecture says every deterministic locally checkable problem with sublinear worst-case volume actually has O(log-star n) volume. It concerns fixed bounded-degree graph families with exact size information and polynomially bounded identifiers. Proving the collapse would eliminate an entire intermediate range of deterministic local information complexity, despite the richer range available to randomized algorithms.

[Read in atlas](index.html#TCS-0515) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [The randomized local computation complexity of the Lovász local lemma](https://arxiv.org/abs/2103.16251v2) · [The Landscape of Distributed Complexities on Trees and Beyond](https://arxiv.org/abs/2202.04724v2) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [New Complexity Classes in Locally Checkable Labeling for Local Computation Algorithms](https://arxiv.org/abs/2607.09626v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0986 — Characterizing Sketchable Distances

Distance sketching compresses vectors so that their dissimilarity can be approximated from small summaries. The source asks which distances admit such sketches and whether sketchability essentially forces a norm-like dependence on the vector difference. It discusses separable distances and divergences, where linear-space obstructions exclude many familiar measures. The allowed stream updates matter because deletions can remove information that insertion-only sketches exploit. A broad characterization would explain which geometric properties make compression possible beyond the established norm setting and its embedding-based descriptions.

[Read in atlas](index.html#TCS-0986) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0469 — What is the deterministic round complexity of maximum independent set in the congested clique?

Maximum independent set asks for a largest collection of pairwise nonadjacent vertices. Here each vertex is a processor in a congested clique, whose communication links exist even between nonadjacent input vertices. The question asks for the optimal deterministic number of rounds, with unlimited local computation and storage. Collecting the full graph at one processor gives an elementary upper bound, after which even exhaustive local optimization costs no communication rounds. The challenge is to determine how much information must move to identify an exact optimum, independently of the usual centralized NP-hardness barrier.

[Read in atlas](index.html#TCS-0469) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1) · [On the Power of the Congested Clique Model](https://www.cs.tau.ac.il/~roshman/papers/podc14_clique.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0519 — Bipartite maximal matching with polynomial-in-degree volume

A maximal matching is a collection of disjoint edges to which no further edge can be added. The question asks for a deterministic local-query algorithm on bipartite graphs whose inspected volume is polynomial in the maximum degree and independent of graph size. A proper two-coloring identifying the bipartition is supplied. Simulating a distributed proposal algorithm by exploring whole neighborhoods can incur an exponential dependence on degree. The project is to follow a much smaller dependency structure while ensuring that separately answered vertex queries describe the same matching.

[Read in atlas](index.html#TCS-0519) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [Truly Tight-in-Δ Bounds for Bipartite Maximal Matching and Variants](https://arxiv.org/abs/2002.08216v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0940 — Lifting sketching resistance to sublinear streaming resistance

Streaming approximation for a constraint satisfaction problem estimates the best fraction of constraints that one assignment can satisfy. Sketches impose additional structure by requiring independently processed summaries to combine consistently. The conjecture asks whether resistance to nontrivial approximation by o(sqrt(n))-space sketches implies resistance to all o(n)-space streaming algorithms. Thus the proposed implication both broadens the algorithm model and raises the memory threshold. A proof would greatly extend existing sketching classifications, while a simple counterexample would expose a useful algorithmic distinction between sketches and more general streams.

[Read in atlas](index.html#TCS-0940) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2997 — How many rounds does triangle detection require in CONGEST?

Triangle detection asks a distributed network to report whether any three vertices are pairwise adjacent. In CONGEST, each edge transmits only O(log n) bits per round, even though vertices initially know all their own neighbors. The saved card asks for the optimal randomized round complexity between the stated doubly logarithmic lower bound and roughly n^(1/3) upper bound. Detection needs only one positive witness somewhere in the network, unlike listing every triangle. The challenge is to exploit that smaller output requirement while still communicating enough information to discover an edge between two neighbors.

[Read in atlas](index.html#TCS-2997) · [Distributed Subgraph Finding — ADGA 2025](https://adga-workshop.org/2025/keren.pdf) · [Distributed Triangle Detection is Hard in Few Rounds](https://arxiv.org/abs/2504.01802) · [Near-optimal Distributed Triangle Enumeration via Expander Decompositions](https://doi.org/10.1145/3446330)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0984 — “Ultimate” Deterministic Sparse Recovery

Sparse recovery reconstructs an approximation to a vector from a short list of linear measurements. The target is a deterministic measurement matrix with O(k log(n/k)) rows and recovery time O(n polylog n). The reconstructed vector must have l2 error bounded by a constant times the best k-sparse l1 error divided by sqrt(k). The source highlights that obtaining the measurement count or the decoding time separately does not provide both guarantees together. The project is to combine near-optimal compression with fast reconstruction while preserving this particular mixed-norm approximation guarantee.

[Read in atlas](index.html#TCS-0984) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6501 — Can a congested clique find a maximal independent set in constant rounds?

A maximal independent set is independent and places every excluded vertex next to a selected one. In the congested clique, processors can send separate short messages directly to every other processor. The question asks whether a randomized algorithm can solve this task in a constant number of rounds on every input graph with high probability. Collecting all edges at one leader is too expensive, but the algorithm need not reconstruct the entire graph to choose a valid set. The target is to replace repeated sparsification and degree-reduction phases with a bounded amount of globally coordinated communication.

[Read in atlas](index.html#TCS-6501) · [When MIS and Maximal Matching are Easy in the Congested Clique](https://arxiv.org/abs/2502.21031) · [Improved Massively Parallel Computation Algorithms for MIS, Matching, and Vertex Cover](https://arxiv.org/abs/1802.08237) · [Time and Space Optimal Massively Parallel Algorithm for the 2-Ruling Set Problem](https://doi.org/10.4230/LIPIcs.DISC.2023.11)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0994 — Graph Matchings

Maximum weighted matching chooses disjoint edges with the greatest total weight. The source asks for a streaming approximation arbitrarily close to optimal using O(n log n) space and a number of passes depending only on the accuracy. It also raises the corresponding question of a linear-time approximation scheme in the RAM model. Weighted improvement steps may require augmenting cycles, which are harder to locate through a stream than local edge exchanges. This historical formulation focuses on whether those global improvements can be organized without storing the entire graph or making many passes.

[Read in atlas](index.html#TCS-0994) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0524 — Can deterministic (Delta+1)-coloring beat square-root dependence on degree?

A proper coloring with Delta plus one colors always exists for a graph of maximum degree Delta. The question asks for a deterministic LOCAL algorithm running in O(Delta^0.499 plus log-star n) rounds. The degree exponent deliberately lies just below one half, while the network-size dependence retains the small symmetry-breaking term. Processors must reduce a large identifier-based palette without causing conflicts among adjacent vertices acting simultaneously. Crossing this degree threshold would improve the coordination of dense local neighborhoods without paying a larger dependence on the total number of vertices.

[Read in atlas](index.html#TCS-0524) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#local) · [Local Conflict Coloring Revisited: Linial for Lists](https://arxiv.org/abs/2007.15251) · [Faster Distributed Delta-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0950 — Linear Sketching Over $F_2$

A linear sketch over F2 records selected parities of a Boolean input. The question compares the minimum randomized sketch length for f with randomized one-way communication for computing f(x XOR y). Alice knows x and sends one message to Bob, who knows y and must determine the function value. An exact deterministic correspondence is known in the source, and the conjecture asks for a randomized correspondence up to polylogarithmic factors. A proof would show that arbitrary one-way messages offer little extra power over linear measurements for this broad class of XOR-based communication problems.

[Read in atlas](index.html#TCS-0950) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:78)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0968 — “For All” Guarantee for Computationally Bounded Adversaries

Compressed sensing reconstructs a vector approximately from linear measurements determined by a sensing matrix. A guarantee for every vector chosen after seeing the matrix is stronger than a guarantee for a fixed vector independent of its random choice. The source asks whether computationally bounded adversaries permit the stronger l2-to-l2 recovery quality in the former setting. An unrestricted adversary can defeat that combination, so the proposed protection relies on difficulty in finding a bad signal. The project is to construct a public sensing matrix and decoder that remain reliable against efficiently generated adaptive inputs.

[Read in atlas](index.html#TCS-0968) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:51)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0993 — Graph Distances

A graph stream reveals edges in sequence while the algorithm keeps a small memory state. The task is to approximate the shortest-path distance between specified vertices. The source asks whether multiple passes or random edge order permit better approximations than approaches based on preserving many distances in a spanner. Following reachability one layer per pass computes the exact distance, but can require too many scans for distant vertices. The project is to exploit the single-pair objective or additional passes without storing a large global distance-preserving graph.

[Read in atlas](index.html#TCS-0993) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0943 — Polynomial-pass barriers to near-exact streaming Max-Cut

The project concerns streaming algorithms that approximate Max Cut increasingly close to the optimum. For every constant C, the conjecture predicts an accuracy parameter epsilon for which a (1-epsilon)-approximation requires either Ω(n) memory or Ω(n^C) passes. The accuracy may depend on C, which is essential to the statement. This asks whether sublinear memory can support a full approximation scheme using only a fixed polynomial bound on scans. A proof would identify a severe time-space cost of approaching exact cut values beyond the more familiar constant-factor streaming barriers.

[Read in atlas](index.html#TCS-0943) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0517 — Can deterministic LOCAL coloring use a near-linear palette in log-star n rounds?

Distributed graph coloring can run faster when it is allowed more than the minimum useful number of colors. The question asks for a deterministic LOCAL algorithm using O(Delta^1.001) colors in O(log-star n) rounds. Both hidden constants must be independent of maximum degree Delta and graph size n. Classical color reduction reaches a palette quadratic in the degree within that round budget. Reducing the palette to nearly linear size would improve extremely fast symmetry breaking without hiding additional degree-dependent communication in the running time.

[Read in atlas](index.html#TCS-0517) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#local) · [Locality in Distributed Graph Algorithms](https://doi.org/10.1137/0221015) · [Local Conflict Coloring Revisited: Linial for Lists](https://arxiv.org/abs/2007.15251)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0954 — Metric TSP Cost Approximation

A metric traveling-salesperson query algorithm learns distances between pairs of points on demand. The source asks whether it can approximate the optimal tour length within a factor strictly below two using o(n squared) distance queries. Estimating a minimum spanning tree's weight gives a near-two approximation without recovering the tree itself. However, constructing a good spanning tree can already require quadratically many queries, obstructing a direct use of classical tour algorithms. The project is to estimate the tour's value more accurately while avoiding the information needed to output an explicit global structure.

[Read in atlas](index.html#TCS-0954) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:71)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0967 — TSP in the Streaming Model

The input is a one-pass stream of points in a two-dimensional integer grid. The task is to estimate the length of the shortest traveling-salesperson tour using space only polylogarithmic in the grid side length. The source asks for a constant approximation factor strictly below two. A minimum-spanning-tree-based estimate reaches the two-approximation benchmark but does not capture all the savings available to a tour. Improving it would show that a very small spatial summary can retain useful information about cyclic routing beyond what a tree-weight estimate provides.

[Read in atlas](index.html#TCS-0967) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:52)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0969 — Approximating LIS Length in the Streaming Model

The longest increasing subsequence of a sequence is its largest order-preserving selection of entries whose values increase. The question asks for the randomized streaming space needed to approximate its length within a factor of two. The algorithm may use one pass or a fixed constant number of passes. The source presents square-root-space deterministic bounds, but the communication problems underlying the deterministic lower bounds become easy with randomness. A resolution therefore needs either a better randomized summary or a lower-bound argument that survives the extra power of random choices.

[Read in atlas](index.html#TCS-0969) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0512 — Constant-locality non-signaling versus quantum LCL separation

Non-signaling locality allows joint output distributions that obey causality without requiring a quantum or classical implementation. Quantum-LOCAL algorithms must realize their correlations through actual local quantum operations and communication. The question asks for a locally checkable labeling problem with constant non-signaling locality but superconstant quantum round complexity. Local checkability ensures that validity itself can be verified from bounded neighborhoods. Such a separation would identify an algorithmic coordination task where causal consistency permits more than quantum mechanics can achieve within a constant communication radius.

[Read in atlas](index.html#TCS-0512) · [Jukka Suomela: locality problems](https://jukkasuomela.fi/open/#non-signaling)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0535 — Vertex Connectivity in the LOCAL Model

The local vertex-connectivity task starts from a vertex v and searches for a small set with a small external vertex boundary. The parameters nu and k specify the size threshold and desired boundary bound. An algorithm may instead report that no set containing v with at most nu vertices has boundary smaller than k. The source gives an O(nu times k) query bound but asks whether the actual running time can match it. Achieving this would remove computational overhead from finding local separators, making the cost proportional to the information inspected.

[Read in atlas](index.html#TCS-0535) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:101)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0962 — Coding Theory in the Streaming Model

Streaming codeword testing reads a received word and distinguishes being close to a code from being substantially farther away. The code is available through a succinct description, while the algorithm should use very little memory and ideally one pass. The source seeks efficient algorithms for good error-correcting codes or lower bounds applying across all such codes. It also highlights tolerant testing for Reed-Solomon codes, where the distance thresholds can be positive. The central issue is whether a stream can retain enough global algebraic consistency information without performing a full stored-word decoding computation.

[Read in atlas](index.html#TCS-0962) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0980 — Random Walks

The task is to simulate a long random walk on a graph presented as an edge stream. The source asks whether nearly linear memory can reduce the number of passes to a polylogarithmic function of graph size and walk length. It also asks for the complexity of approximating the walk's endpoint distribution and identifying its most likely vertices. These tasks may require less information than producing every step of the trajectory. A resolution would clarify how effectively repeated scans can substitute for direct access to the transition choices of a large graph.

[Read in atlas](index.html#TCS-0980) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0985 — $L_\infty$ Estimation

The infinity norm of a frequency vector is the largest absolute frequency. Multiplicative approximation is expensive in general, so the source instead allows additive error scaled by epsilon times the l1 or l2 norm. It asks whether estimating just this numerical value needs less space than finding the identities of heavy items. In particular, the domain-size dependence may be avoidable because the output contains no item name. The project is to separate the memory needed to estimate the largest magnitude from the extra information required to locate its contributing coordinates.

[Read in atlas](index.html#TCS-0985) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:3)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-0957 — Approximating Rank in the Bounded-Degree Model

The input is a finite-field matrix with only constantly many nonzero entries in each row and column. Queries reveal the sparse neighborhoods of chosen rows or columns. The task is to estimate matrix rank within additive error epsilon times the number of columns. The source conjectures that general instances require linearly many queries, despite efficient estimation for graph-incidence matrices over F2. A lower bound must vary the matrix itself, since hardness constructions that keep the matrix fixed and randomize only a right-hand side do not address rank.

[Read in atlas](index.html#TCS-0957) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:68)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0959 — RNA Folding

The simplified RNA folding problem matches complementary nucleotides while forbidding crossing pairs. The goal is to estimate the largest possible number of such pairs in a sequence. The source asks how accurately this value can be approximated using polylogarithmic streaming memory and few passes. A simple two-approximation handles the two complementary letter pairs separately, but better accuracy must account for their interactions. The project is to summarize the nested pairing structure without storing the quadratic dynamic-programming table used by the classical exact algorithm.

[Read in atlas](index.html#TCS-0959) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:61)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1169 — What is the smallest number of passes required for computing O(∆)-colorings deterministically in the semi-streaming setting?

Semi-streaming graph coloring reads an edge stream using memory nearly linear in the number of vertices. The question asks for the minimum number of deterministic passes needed to use O(Delta) colors. The source improves the upper bound to roughly the square root of log Delta passes, with a palette close to Delta up to a constant factor. Randomized one-pass coloring provides a contrasting benchmark, while deterministic one-pass algorithms face a much larger palette requirement. The remaining tradeoff measures how effectively repeated scans can replace randomization when memory is too small to retain the entire graph.

[Read in atlas](index.html#TCS-1169) · [Faster Deterministic Streaming Vertex Coloring](https://doi.org/10.4230/LIPIcs.ICALP.2026.56)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1234 — We also leave as an open problem characterizing the exact trade-off between the number of passes and memory required for exactly computing a stream’s histogram.

An exact stream histogram records the occurrence counts needed to characterize the stream's frequencies. The source asks for the precise tradeoff between the number of passes and working memory needed to compute it. It gives a two-pass algorithm using O(n log log n) bits, while the stated lower bound is Ω(n log log log n). More generally, its bounds involve iterated logarithms whose detailed dependence on the pass count is not pinned down. Closing the gap would sharpen an unusual regime where additional scans reduce the cost of exact information, not merely improve an approximation.

[Read in atlas](index.html#TCS-1234) · [Tight Bounds for Low-Error Frequency Moment Estimation and the Power of Multiple Passes](https://doi.org/10.4230/LIPIcs.ICALP.2026.102)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1588 — We conjecture the positive results are tight, i.e., exactly the multithreshold predicates and robustly piecewise floor-affine functions are robustly computable.

Continuous chemical reaction networks represent inputs and outputs as nonnegative concentrations evolving under mass-action kinetics. Robust computation requires convergence to the correct answer for every positive choice of reaction-rate constants. The source constructs robust networks for multithreshold predicates and a specified class of piecewise floor-affine functions, where negative affine values are truncated to zero. It conjectures that these constructions describe exactly the predicates and functions the model can compute. A matching impossibility theorem would turn the positive constructions into a complete characterization of computation that is insensitive to kinetic parameters.

[Read in atlas](index.html#TCS-1588) · [Robust Predicate and Function Computation in Continuous Chemical Reaction Networks](https://doi.org/10.4230/LIPIcs.DISC.2025.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1784 — Second, could a lower bound on any deterministic local broadcast algorithm, better than Ω(∆ log n), be proved?

In a beeping network, simultaneous one-bit transmissions from neighbors combine through an OR operation. Local broadcast must deliver neighborhood information despite this severe inability to distinguish overlapping transmissions. The source gives deterministic simulation methods with roughly quadratic dependence on maximum degree. The selected question asks for a lower bound stronger than Ω(Delta log n) for every deterministic local-broadcast algorithm. A stronger bound would determine whether the remaining degree gap reflects an inherent collision-resolution cost or room for a substantially faster communication schedule.

[Read in atlas](index.html#TCS-1784) · [Beeping Deterministic CONGEST Algorithms in Graphs](https://doi.org/10.4230/LIPIcs.ESA.2025.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1965 — A question that we leave open is whether any problem that admits a O(t)-round algorithm in the LOCAL model, for any t ≤ D, can […]

A distributed algorithm can minimize its round count while still sending many messages across the network. The source studies whether both costs can be near-optimal simultaneously when nodes initially know their neighbors, as in KT1. It asks whether every O(t)-round LOCAL problem with t at most the diameter admits roughly O(t) rounds and O(n) messages, up to polylogarithmic factors. The paper establishes this kind of simultaneous efficiency for global tasks at the diameter scale. The remaining question is whether faster local tasks can also avoid redundant communication without sacrificing their round complexity.

[Read in atlas](index.html#TCS-1965) · [The Singular Optimality of Distributed Computation in LOCAL](https://doi.org/10.4230/LIPIcs.OPODIS.2024.26)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2097 — We conjecture that the lower bound of 3/2, which has been shown for a specific class of algorithms, holds more generally, i.e., with one or […]

Byzantine reliable broadcast distributes a sender's message despite nodes that may behave arbitrarily. The source measures communication overhead relative to the basic cost of delivering the message throughout the network. It proves a three-halves lower bound for a restricted algorithm class with limited initial communication and a three-round requirement. The conjecture asks whether the same bound holds after removing one or both restrictions. Extending it would identify an intrinsic redundancy cost of reliable dissemination, beyond the particular coding patterns and timing assumptions covered by the existing proof.

[Read in atlas](index.html#TCS-2097) · [Byzantine Reliable Broadcast with Low Communication and Time Complexity](https://doi.org/10.4230/LIPIcs.OPODIS.2024.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2233 — Are there hereditary (or even monotone) classes of local complexity Ω(nc ) for c > 1?

Local certification gives each graph vertex a certificate that it verifies using only its nearby information. The source asks whether a hereditary graph class can require certificates of size growing faster than linearly in the number of vertices. It also asks for this phenomenon under the stronger requirement of closure under subgraphs. Existing linear lower bounds motivate seeking a larger information barrier. Such examples would show that even deletion-stable structural properties can demand exceptionally large local evidence for a globally correct decision.

[Read in atlas](index.html#TCS-2233) · [Local Certification of Geometric Graph Classes](https://doi.org/10.4230/LIPIcs.MFCS.2024.48)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2281 — We restate the open question of [59]: Given a local FO formula φ(x), i.e., a formula where φ(x) depends on a fixed-radius neighborhood of vertex […]

A local first-order formula evaluated at a graph vertex depends only on a neighborhood of fixed radius around that vertex. The task is to make every vertex determine whether it satisfies a given local formula on the bounded-expansion graph classes considered by the source. The requested running time is O(log n) rounds in the CONGEST model, where messages along edges have bounded size. Local dependence alone does not make gathering an entire neighborhood cheap, because even a small-radius neighborhood can contain many vertices. Such an algorithm would strengthen distributed logical model checking from deciding global properties to identifying all satisfying vertices simultaneously.

[Read in atlas](index.html#TCS-2281) · [Distributed Model Checking on Graphs of Bounded Treedepth](https://doi.org/10.4230/LIPIcs.DISC.2024.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2470 — While there has been progress on solving the natural list and defective coloring variants of O(β 2 ) coloring, it is still unknown if a […]

An orientation with maximum outdegree β gives each vertex a bounded number of outgoing neighbors even when its total degree is large. Distributed coloring algorithms exploit this structure to obtain palettes related to β rather than maximum degree. The source asks whether some constant ε > 0 permits O(β^(2−ε)) colors in f(β) + O(log* n) rounds. Existing quadratic-palette techniques and progress on defective list coloring motivate the target, but do not establish this improved exponent with such weak dependence on network size. Achieving it would strengthen a basic building block for deterministic symmetry breaking on sparsely oriented graphs.

[Read in atlas](index.html#TCS-2470) · [List Defective Colorings: Distributed Algorithms and Applications](https://doi.org/10.4230/LIPIcs.DISC.2023.22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2540 — Is there an MSO2 property requiring certificates of Ω(nϵ ) bits, for some ϵ > 0, on graphs of bounded clique-width?

Proof-labeling schemes certify graph properties by assigning short labels that neighboring vertices can check locally. On graphs of bounded clique-width, the source asks whether some MSO₂ property necessarily requires Ω(n^ε) certificate bits per vertex for a fixed positive ε. MSO₂ can quantify over edge sets as well as vertices, making it richer than the vertex-set logic behind many compact certification results. Familiar examples such as Hamiltonicity still admit logarithmic certificates, so their centralized difficulty does not provide the desired lower bound. Finding a separating property would expose a real limit of generic compact distributed certification on these dense structured graphs.

[Read in atlas](index.html#TCS-2540) · [Distributed Certification for Classes of Dense Graphs](https://doi.org/10.4230/LIPIcs.DISC.2023.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2688 — The problem of designing a rendezvous algorithm working for arbitrary connected graphs in optimal time remains open.

Rendezvous asks two independently operating agents to meet at one vertex of an initially unknown connected graph. The agents have distinct labels and may start at different times and locations. The source asks for optimal running time in a model allowing arbitrary connected graphs, including infinite ones. Exploring successively larger finite graphs does not automatically guarantee progress in an infinite graph. The project must balance symmetry breaking, delayed wakeups, and local exploration without assuming knowledge of the network's total size.

[Read in atlas](index.html#TCS-2688) · [How to Meet at a Node of Any Connected Graph](https://doi.org/10.4230/LIPIcs.DISC.2022.11)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2689 — Regardless, whether there exists a protocol that achieves deterministic safety and termination in a hybrid synchronous model remains an open question.

Permissionless consensus must accommodate processes joining and leaving without a fixed known membership. The source's hybrid synchronous model provides synchronously connected participation while retaining uncertainty about which messages a process should expect. The question asks whether consensus can have both deterministic safety and deterministic termination under that model's benign-failure assumptions. Sandglass supplies deterministic safety with a weaker termination guarantee, so the remaining issue is eliminating randomness from progress as well. A resolution would clarify whether the uncertainty created by open participation imposes a fundamental limit even when substantial synchrony is present.

[Read in atlas](index.html#TCS-2689) · [Safe Permissionless Consensus](https://doi.org/10.4230/LIPIcs.DISC.2022.33)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2735 — We leave the understanding of the uniform complexity landscape in the regime Ω(log 1/ε) as an exciting open problem.

Uniform distributed local algorithms determine each vertex's output from an almost surely finite neighborhood without relying on a known network size. Their complexity can be measured by the radius needed to finish with probability at least one minus ε. The source asks for the complexity landscape on regular trees in the regime Ω(log(1/ε)). Below that scale, uniform complexity aligns closely with randomized finite-network complexity, but the relationship breaks down for examples such as three-coloring. A classification would explain which locally checkable tasks remain possible with uniform stopping behavior and connect distributed algorithms with finitary factors of independent randomness.

[Read in atlas](index.html#TCS-2735) · [Local Problems on Trees from the Perspectives of Distributed Algorithms, Finitary Factors, and Descriptive Combinatorics](https://doi.org/10.4230/LIPIcs.ITCS.2022.29)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2753 — The question of whether a fully adaptive strong BA with optimal resilience exists or not remains open.

Strong Byzantine agreement requires correct processes to agree while preserving the strong validity condition even when some participants behave arbitrarily. Here adaptivity refers to communication that scales with the actual number f of faulty processes, rather than only the tolerated maximum t. The source asks for a fully adaptive strong-agreement algorithm with optimal resilience n = 2t + 1. Its constructions achieve O(n(f+1)) communication for broadcast and weak agreement, but the strong version becomes quadratic once failures occur. Closing that gap would retain optimal fault tolerance while making communication economical in executions with only a few faults.

[Read in atlas](index.html#TCS-2753) · [Make Every Word Count: Adaptive Byzantine Agreement with Fewer Words](https://doi.org/10.4230/LIPIcs.OPODIS.2022.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2816 — It remains an open question whether it is possible to implement an exact wait-free linearizable FIFO queue with worst-case logarithmic step complexity without restriction on […]

A concurrent FIFO queue should return items in insertion order while allowing many processes to enqueue and dequeue simultaneously. Wait-freedom requires each operation to finish after a bounded number of its own steps regardless of interference. The question asks for an exact linearizable queue with O(log n) worst-case step complexity and no restriction on which of the n processes may perform either operation. The source reaches logarithmic bounds by relaxing semantics or limiting dequeuers, leaving the unrestricted exact version separate. An implementation would reconcile strong progress and ordering guarantees with low latency under arbitrary concurrent access.

[Read in atlas](index.html#TCS-2816) · [Efficient Wait-Free Queue Algorithms with Multiple Enqueuers and Multiple Dequeuers](https://doi.org/10.4230/LIPIcs.OPODIS.2022.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2896 — We leave it as an open problem whether a constant-factor approximation in sublinear (in n = 2k) space is possible

Euclidean Steiner forest connects every specified pair of terminals while allowing extra junction points to reduce total geometric length. In the paired-terminal setting, there are exactly two points in each color class, so n = 2k for k demands. The source asks whether a constant-factor approximation can be maintained in geometric streams using space sublinear in n. Its lower bound for classes of size at most two relies on singleton classes and therefore does not cover this exact-pairs restriction. Resolving the gap would show whether uniform pair demands permit meaningful geometric compression despite the difficulty of more general connectivity requirements.

[Read in atlas](index.html#TCS-2896) · [Streaming Algorithms for Geometric Steiner Forest](https://doi.org/10.4230/LIPIcs.ICALP.2022.47)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3075 — In particular, for the list of problems with determinant-based counting in Section 1, designing RNC sampling algorithms remains open.

Several combinatorial families admit determinant formulas that make counting possible in efficient parallel complexity classes. Producing a random object from those families is harder to parallelize because standard counting-to-sampling reductions make sequential choices. After giving an RNC sampler for directed rooted spanning trees, the source asks for analogous samplers for the remaining determinant-counted structures. Examples include planar perfect matchings, determinantal point processes, and Eulerian tours, whose connection to arborescences does not immediately yield a parallel reduction. Resolving these cases would explain whether fast parallel counting can generally be converted into equally parallel random generation.

[Read in atlas](index.html#TCS-3075) · [Sampling Arborescences in Parallel](https://doi.org/10.4230/LIPIcs.ITCS.2021.83)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3119 — Specifically, note that Y ′ (resp., Y ′′ ) is o(1)-close to being uniformly distributed over S ′ (resp., {0, 1}ℓ+4−t ). 45 Unlike in […]

Robustly self-ordered graphs provide graph constructions whose structural identifications remain constrained under perturbation. The cited paper applies these constructions to property testing. The saved passage discusses random variables that are close to uniform over specified supports. That distributional control appears relevant to transferring information between the construction and a testing argument. The excerpt omits the definitions of the variables and ends before the unresolved issue, so the draft cannot identify the remaining question as an extractor guarantee, a testing bound, or another precise claim.

[Read in atlas](index.html#TCS-3119) · [Robustly Self-Ordered Graphs: Constructions and Applications to Property Testing](https://doi.org/10.4230/LIPIcs.CCC.2021.12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3134 — For example, the complexity of k-independent set detection in CONGEST remains open, whereas in the centralized setting, it is equivalent to k-clique – a correspondence […]

Detecting a k-vertex independent set means determining whether a graph contains k mutually nonadjacent vertices. The question asks for the round complexity of this task in CONGEST, where processors communicate only along actual graph edges with bounded-size messages. In centralized computation, complementing the graph converts the task to clique detection. That conversion does not preserve a distributed communication network, because absent edges cannot simply become communication links. Understanding the complexity would expose how distributed pattern detection depends on the difference between information about missing edges and the physical routes available for exchanging that information.

[Read in atlas](index.html#TCS-3134) · [Beyond Distributed Subgraph Detection: Induced Subgraphs, Multicolored Problems and Graph Parameters](https://doi.org/10.4230/LIPIcs.OPODIS.2021.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3192 — First, is it possible to obtain near singularly optimal bounds using a deterministic algorithm?

Leader election requires all vertices of an asynchronous network to agree on a single designated process. The source constructs a randomized algorithm whose running time and number of messages are both within polylogarithmic factors of the appropriate lower bounds. Its question asks whether a deterministic algorithm can achieve the same simultaneous near-optimality. Randomized selection helps limit redundant exploration and coordination, so eliminating it must preserve both resource guarantees at once. A positive result would show that efficient global symmetry breaking in asynchronous networks does not depend on random choices.

[Read in atlas](index.html#TCS-3192) · [Singularly Near Optimal Leader Election in Asynchronous Networks](https://doi.org/10.4230/LIPIcs.DISC.2021.27)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3381 — The question of whether protocols with poly(|ϕ|) states exist for every PA formula ϕ, possibly with quantifiers, also remains open.

Population protocols compute through repeated interactions of finite-state agents. Presburger arithmetic describes exactly the predicates expressible by these protocols, but equivalent representations can have very different sizes. The question asks whether every arithmetic formula, including quantified ones, has a protocol with only polynomially many states in its formula length. The source distinguishes existence of such a compact protocol from the complexity of constructing it. The project studies representational succinctness at the interface between logical specifications and distributed computation.

[Read in atlas](index.html#TCS-3381) · [Succinct Population Protocols for Presburger Arithmetic](https://doi.org/10.4230/LIPIcs.STACS.2020.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3384 — We do not know whether it is possible to compute approximate matchings, let alone set packings, using AC0 -circuits.

Constant-depth AC⁰ circuits offer a highly parallel but weak model of computation with unbounded-fan-in Boolean gates. The source asks whether they can output useful approximate matchings, and more generally approximate set packings. This is a search question about producing disjoint edges or sets, rather than merely estimating the optimum value. The paper obtains shallow-circuit approximations of packing size but explains why extracting an actual packing is a different obstacle, even on simple bipartite inputs. Resolving the search problem would distinguish numerical approximation from constructing compatible choices under severe limits on computational depth.

[Read in atlas](index.html#TCS-3384) · [Kernelizing the Hitting Set Problem in Linear Sequential and Constant Parallel Time](https://doi.org/10.4230/LIPIcs.SWAT.2020.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3416 — As there are only non-blocking linearizable (not relaxed) queue implementations using objects with consensus number two, it is an open question if there is such […]

Linearizable queues must behave like a single exact FIFO queue even when operations from many processes overlap. The question asks whether such a queue has a wait-free implementation using only objects with consensus number two. Wait-freedom strengthens nonblocking progress by requiring every correct process's operation to finish despite the behavior of others. The source obtains a wait-free implementation for a relaxed queue and contrasts it with nonblocking exact implementations based on primitives of the same consensus power. An exact construction or impossibility result would clarify the synchronization strength needed to combine FIFO semantics with individual progress guarantees.

[Read in atlas](index.html#TCS-3416) · [Relaxed Queues and Stacks from Read/Write Operations](https://doi.org/10.4230/LIPIcs.OPODIS.2020.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3436 — Based on this, we conjecture that probability-1 leader election using O(1) messages requires Ω(n) time to stabilize.

Population protocols consist of many small agents that repeatedly interact in randomly selected pairs. The source separates each agent's private state from its externally visible message and considers a constant-size message alphabet. Its conjecture says that leader election stabilizing correctly with probability one requires Ω(n) time under this communication restriction. A constant number of message types does not require constant private memory, so existing lower bounds for constant-state protocols do not directly settle the claim. Proving it would identify a fundamental speed limit caused by limited visible information even when agents can retain richer internal histories.

[Read in atlas](index.html#TCS-3436) · [Message Complexity of Population Protocols](https://doi.org/10.4230/LIPIcs.DISC.2020.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3662 — We conjecture that in the low-dimensional setting of both (weakly-)smooth d and nonsmooth optimization the correct answer should be Ω( ln(K/γ) ln(1/ε)).

Parallel oracle optimization allows an algorithm to query several points at once before receiving the next batch of local information. The source asks for sharper lower bounds when the dimension is small relative to the demanded accuracy. Its conjecture combines linear dimension dependence, logarithmic inverse-accuracy dependence, and a logarithmic allowance for batch size and failure probability. The claim spans nonsmooth and suitably smooth convex objectives in the specified oracle setting. A tight result would quantify the limited benefit of parallel exploration after high-dimensional lower-bound constructions cease to capture the relevant regime.

[Read in atlas](index.html#TCS-3662) · [Lower Bounds for Parallel and Randomized Convex Optimization](https://proceedings.mlr.press/v99/diakonikolas19c.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3726 — Is it possible to obtain a deterministic message-reduction scheme with no degradation of time?

Message-reduction schemes simulate a distributed LOCAL algorithm while avoiding unnecessary communication along many network edges. Sparse spanners provide a way to route the original information through a smaller set of links. The question asks whether this reduction can be made deterministic without worsening the original algorithm's asymptotic round complexity. The source achieves strong savings using randomized neighbor sampling, which is the part that resists direct derandomization. A deterministic scheme would give many local graph algorithms communication savings automatically while preserving their time guarantees on every input and execution.

[Read in atlas](index.html#TCS-3726) · [Message Reduction in the LOCAL Model Is a Free Lunch](https://doi.org/10.4230/LIPIcs.DISC.2019.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3762 — What if the output is required to be perfectly random, i.e., ε = 0?

A graph-streaming random-walk simulator sees edges once and later outputs the sequence of vertices visited by a walk of specified length. For undirected insertion-only streams, the source gives a low-space algorithm whose output distribution is close to the true walk distribution. The question asks what can be achieved when the output must instead have exactly the correct distribution, with approximation error zero. Approximate sampling can discard rare troublesome events, while an exact simulator must account for every event with its proper probability. Understanding the additional space cost would distinguish statistical approximation from perfect simulation in streamed graph access.

[Read in atlas](index.html#TCS-3762) · [Simulating Random Walks on Graphs in the Streaming Model](https://doi.org/10.4230/LIPIcs.ITCS.2019.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3792 — We conjecture that for all n > k > 2 there is no deterministic linearizable (n, k)-set agreement object that is equivalent to the (n, […]

An (n,k)-set agreement task permits n processes to decide at most k distinct proposed values. The question asks whether any deterministic linearizable object can have exactly the same implementation power as that task when n > k > 2. The source conjectures that no such object exists because enforcing deterministic sequential behavior gives the object stronger agreement power. It proves a related impossibility for k = 2 and n at least four, but the number of possible sequential behaviors grows rapidly for larger k. A general proof would clarify the gap between one-shot coordination tasks and reusable objects with deterministic linearizable semantics.

[Read in atlas](index.html#TCS-3792) · [On Deterministic Linearizable Set Agreement Objects](https://doi.org/10.4230/LIPIcs.OPODIS.2019.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3806 — Can we reduce the number of passes to poly(k), or instead show that we need passes which are superpolynomial in k if we restrict space […]

A parameterized streaming vertex-cover algorithm asks whether a graph has a cover of at most k vertices while scanning its edges. The source gives an insertion-only algorithm using O(k log n) bits, but it may require exponentially many passes in k. The question is whether polynomially many passes suffice at that same space bound or whether a superpolynomial pass lower bound can be proved. Available lower bounds leave a large gap, so optimal memory alone does not determine practical efficiency. Resolving the tradeoff would show whether compact storage of a small candidate solution can coexist with a manageable number of complete input scans.

[Read in atlas](index.html#TCS-3806) · [Towards a Theory of Parameterized Streaming Algorithms](https://doi.org/10.4230/LIPIcs.IPEC.2019.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3845 — In other words, while there exist good multicommodity routing solutions, we do not know how to find them efficiently in a distributed fashion.

Multicommodity routing connects many source-destination demands while limiting both path length and the number of routes sharing an edge. The source considers low-width demand instances on random graphs that serve as communication infrastructure for parallel simulation. It asks for a distributed algorithm running in polylogarithmic rounds and producing routing with polylogarithmic congestion and dilation. Good routes exist by centralized arguments, but discovering them quickly with only local communication is the missing step. Such a construction would tighten the connection between efficient parallel computation and distributed computation on networks with rapid mixing.

[Read in atlas](index.html#TCS-3845) · [New Distributed Algorithms in Almost Mixing Time via Transformations from Parallel Algorithms](https://doi.org/10.4230/LIPIcs.DISC.2018.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3892 — Finding a lower bound for the construction of all-pairs spanners in the congest model is still an open question.

An all-pairs spanner is a sparse subgraph that approximately preserves distances between every pair of vertices. In CONGEST, vertices must construct it through bounded-size messages on the original graph. The source asks for construction-time lower bounds beyond the unavoidable dependence on network diameter, especially for sparse additive spanners. Existing bounds for selected-pair spanners do not automatically extend to the all-pairs task with its different output freedom. A stronger lower bound would identify whether current distributed constructions are close to optimal or whether their time cost reflects techniques that could still be improved.

[Read in atlas](index.html#TCS-3892) · [The Sparsest Additive Spanner via Multiple Weighted BFS Trees](https://doi.org/10.4230/LIPIcs.OPODIS.2018.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3894 — We conjecture that systems of linear inequalities can be computed by leaderless protocols with a polynomial number of states.

Leaderless population protocols begin with only the ordinary input agents, without a specially initialized coordinator. They can compute predicates about input counts through repeated finite-state pairwise interactions. The source conjectures that systems of linear inequalities admit such protocols with only polynomially many states in the description size of the predicate. Expressibility alone does not guarantee this compact representation, since numerical coefficients and combinations of constraints can inflate straightforward constructions. Proving the conjecture would show that a basic class of arithmetic specifications can be implemented by small anonymous agents without spending states to emulate an initial leader.

[Read in atlas](index.html#TCS-3894) · [Large Flocks of Small Birds: on the Minimal Size of Population Protocols](https://doi.org/10.4230/LIPIcs.STACS.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3910 — We leave as a great open question whether the complexity of clique detection in the CONGEST model is sublinear, or one needs Θ(n) e communication […]

Distributed clique detection asks whether the communication graph contains a complete subgraph of a prescribed constant size. In CONGEST, learning the necessary adjacency information competes for limited bandwidth on the same graph being inspected. The 2018 source asks whether detecting a four-clique can take sublinear time or requires nearly linear rounds. Its two-party communication lower-bound method reaches a barrier, while improved triangle algorithms suggest that faster detection might be possible. The question focuses on whether the additional pairwise relationships inside four vertices create a fundamentally larger distributed coordination cost than triangle detection.

[Read in atlas](index.html#TCS-3910) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4006 — Are there deterministic context-free languages where the optimal space bound (for the variable-size or the fixed-size model) is in o(n) ∩ ω((log n)2 )?

A sliding-window algorithm checks membership of only the most recent portion of an input stream. This project asks whether some deterministic context-free language has optimal memory strictly above squared logarithmic space but below linear space in window length. The source considers both fixed-size and variable-size windows. Standard regular-language classifications leave no such intermediate regime, while stack-based languages permit more complicated behavior. A separating example or gap theorem would map how recursive language structure changes the possible memory costs of continuously forgetting old input.

[Read in atlas](index.html#TCS-4006) · [Sliding Windows over Context-Free Languages](https://doi.org/10.4230/LIPIcs.MFCS.2018.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4039 — We leave it as an open problem to separate these two notions – i.e., find functions which have low bottleneck complexity protocols, but do not […]

Bottleneck complexity measures the communication burden placed on the busiest participant in a distributed protocol. A small-memory streaming algorithm gives one way to achieve a low burden by passing its state between participants. This project asks for a function with a low-bottleneck protocol that nevertheless requires large memory in the corresponding streaming model. General communication networks can aggregate information through structures richer than the chain or repeated cycle used by a streaming simulation. A separation would demonstrate that balanced distributed communication enables computations beyond those explained by small streaming state alone.

[Read in atlas](index.html#TCS-4039) · [The Bottleneck Complexity of Secure Multiparty Computation](https://doi.org/10.4230/LIPIcs.ICALP.2018.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4099 — It remains open to find a pseudo-deterministic NC algorithm for perfect matching in general (non-bipartite) graphs.

A pseudodeterministic randomized algorithm returns the same canonical answer with high probability on repeated runs of a fixed input. For perfect matching, this demands reproducible selection of one matching rather than merely finding any valid matching. The question asks for such an algorithm on general nonbipartite graphs using polynomially many processors and polylogarithmic parallel depth. The source achieves this for bipartite graphs, but extending the selection mechanism must account for the additional structure of general matching. A solution would give stable outputs from efficient parallel randomization and advance the relationship between matching algorithms and derandomization.

[Read in atlas](index.html#TCS-4099) · [Bipartite Perfect Matching in Pseudo-Deterministic NC](https://doi.org/10.4230/LIPIcs.ICALP.2017.87)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4102 — 1 The problem of communication lower bounds for general functions under the cash-register model remains open.

Distributed function monitoring tracks a condition on a global data vector whose updates arrive at separate sites. Communication can be reduced by letting each site remain silent while its local state stays within a certified safe region. The source identifies the problem of proving communication lower bounds for general monitored functions in the cash-register model, where updates only increase coordinates. This monotonic input restriction prevents direct transfer of every lower-bound argument designed for arbitrary positive and negative updates. General bounds would help determine when communication savings from local safe zones are close to the best possible monitoring strategy.

[Read in atlas](index.html#TCS-4102) · [Distributed Query Monitoring through Convex Analysis: Towards Composable Safe Zones](https://doi.org/10.4230/LIPIcs.ICDT.2017.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4121 — First, can we get efficient distributed algorithms for TAP with an approximation ratio better than 2?

Tree augmentation starts with a spanning tree and adds graph edges until the resulting network remains connected after any single edge failure. The optimization objective minimizes the cost or number of added edges in the relevant version. The source asks whether an efficient distributed algorithm can achieve an approximation ratio strictly better than two. Coordinating which tree edges are protected by the same added link is difficult when information must travel through a bandwidth-limited network. Improving the ratio would strengthen distributed construction of resilient network infrastructure and clarify which centralized augmentation techniques admit efficient communication-based implementations.

[Read in atlas](index.html#TCS-4121) · [Fast Distributed Approximation for TAP and 2-Edge-Connectivity](https://doi.org/10.4230/LIPIcs.OPODIS.2017.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4143 — We do not know whether there exists a distributed language admitting error-sensitive proof-labeling schemes, but such that all error-sensitive proof-labeling schemes for that language use […]

An error-sensitive proof-labeling scheme makes many vertices reject when a network configuration is far from satisfying the claimed property. Ordinary proof-labeling schemes need only ensure that at least one vertex detects an invalid configuration. The source asks whether some property admits error-sensitive certification only with certificates larger than its most compact ordinary certificates. All examples examined there either lack error-sensitive schemes entirely or obtain them without increasing certificate size. A separating language would reveal a genuine storage cost for making rejection proportional to the amount of error, beyond the mere existence of local verification.

[Read in atlas](index.html#TCS-4143) · [Error-Sensitive Proof-Labeling Schemes](https://doi.org/10.4230/LIPIcs.DISC.2017.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4193 — First, can the MIS lower bounds in the Local model shown by Kuhn et al. [15] be extended to 2-ruling sets?

A two-ruling set is an independent set such that every graph vertex lies within distance two of a selected vertex. This relaxes maximal independent set, which requires domination already at distance one. The question asks whether established LOCAL-model round lower bounds for maximal independent set extend to two-ruling sets. Extra domination distance gives algorithms more freedom, so a lower bound must survive that relaxation rather than simply reuse an MIS instance. Resolving the comparison would show whether much of the symmetry-breaking difficulty lies in independence itself or in the stronger requirement to dominate immediate neighbors.

[Read in atlas](index.html#TCS-4193) · [Symmetry Breaking in the Congest Model: Time- and Message-Efficient Algorithms for Ruling Sets](https://doi.org/10.4230/LIPIcs.DISC.2017.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4210 — A final open question concerns routing schemes in general: what is the time needed by a data packet to travel through the graph?

A compact routing scheme stores labels and local tables so that a packet can choose its next vertex without a global map. The source's geometric construction controls route stretch in a polygonal visibility graph. It asks how much computation the packet needs at each forwarding step and over its full journey. Small tables and short geometric paths do not automatically imply fast next-hop decisions. The research direction adds processing time to the usual tradeoff between routing memory and path quality.

[Read in atlas](index.html#TCS-4210) · [Routing in Polygonal Domains](https://doi.org/10.4230/LIPIcs.ISAAC.2017.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4231 — What is the complexity of general subgraph detection?

Distributed subgraph detection asks whether a network contains a fixed constant-size graph H as a subgraph. The source asks whether every such target can be detected in O(n) CONGEST rounds or whether some targets require superlinear time. A linear bound is easy for cliques, despite their prominence as hard patterns in centralized computation. Other patterns can distribute their relevant edges across distant parts of the communication network in different ways, so centralized hardness is a poor guide. A general upper bound or a superlinear example would establish a basic classification boundary for exact distributed pattern detection.

[Read in atlas](index.html#TCS-4231) · [Deterministic Subgraph Detection in Broadcast CONGEST](https://doi.org/10.4230/LIPIcs.OPODIS.2017.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4271 — Do these complexities capture all possibilities, when natural global graph problems are concerned?

Global graph problems in CONGEST have markedly different costs even though every processor starts with only local information. The source highlights diameter-time problems, problems taking roughly diameter plus square-root time, near-linear problems, and problems needing nearly quadratic rounds. It asks whether these scales capture all possibilities for natural global graph tasks. The word natural leaves this as a classification program rather than a formally exhaustive theorem over an explicitly specified set of problems. Finding intermediate examples or structural gap theorems would explain why communication bottlenecks place familiar optimization tasks at particular points on the distributed complexity spectrum.

[Read in atlas](index.html#TCS-4271) · [Quadratic and Near-Quadratic Lower Bounds for the CONGEST Model](https://doi.org/10.4230/LIPIcs.DISC.2017.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4274 — In our view, the main open question raised by our work is the following: is there a 2-connected graph H such that H-freeness can be […]

Subgraph-freeness asks whether a network avoids a fixed graph H while communicating through bounded-size messages. The source asks whether any two-connected H admits a subpolynomial-round algorithm, or whether every such target forces a polynomial lower bound. Two-connectivity isolates patterns whose cycles cannot be separated by deleting a single vertex. The paper's reductions would turn hardness for all these patterns into a broad distinction between trees and connected graphs containing cycles. Resolving the question would therefore organize many individual detection bounds into a structural explanation of when local patterns require substantial global communication.

[Read in atlas](index.html#TCS-4274) · [Lower Bounds for Subgraph Detection in the CONGEST Model](https://doi.org/10.4230/LIPIcs.OPODIS.2017.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4299 — It is unknown whether the capacity for collision detection improves deterministic broadcast time, as it does for randomized algorithms [12].

In an ad-hoc radio network, a receiver normally obtains a message only when exactly one neighbor transmits to it. Collision detection additionally tells the receiver when simultaneous transmissions occurred instead of silence. The source asks whether this extra feedback can improve deterministic broadcast time in unknown network topologies. Randomized algorithms benefit from it, but deterministic scheduling must exploit the feedback without relying on random contention resolution. Establishing a speedup or an equivalence would identify the value of a basic physical-layer capability for reliably disseminating information through a network with initially unknown structure.

[Read in atlas](index.html#TCS-4299) · [Faster Deterministic Communication in Radio Networks](https://doi.org/10.4230/LIPIcs.ICALP.2016.139)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4763 — Parallel (1+e)-Approximate Multi-Commodity Min-Cost Flow in Almost Optimal Depth and Work — Open Problem 1

Parallel flow algorithms seek small total work and short dependency depth while approximating an optimum flow value or cost. The question asks for nearly linear work and polylogarithmic depth for either edge-capacitated minimum-cost flow or vertex-capacitated maximum flow with approximation 1 + ε. The source works on undirected graphs and obtains almost-linear work with subpolynomial depth, leaving a gap between subpolynomial and polylogarithmic guarantees. Existing shortest-path and edge-capacitated maximum-flow results motivate trying to remove that gap. A solution would make richer capacity and cost models as parallelizable as these more established flow primitives.

[Read in atlas](index.html#TCS-4763) · [Parallel (1+e)-Approximate Multi-Commodity Min-Cost Flow in Almost Optimal Depth and Work](https://doi.org/10.1109/FOCS63196.2025.00099)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5127 — The Impossibility of Approximate Agreement on a Larger Class of Graphs — Explicit open question on PDF page 2

Graph approximate agreement asks distributed processes to choose outputs satisfying proximity and validity conditions expressed on a graph. The source asks which graphs admit wait-free solutions using only registers. Wait-freedom requires each participating process to finish despite delays or failures of other processes. Classifying the admissible graphs would reveal how the geometry of permitted outputs interacts with the power of basic shared memory. The saved note preserves uncertainty for many graphs but does not state the exact validity condition or process count, so these cannot be supplied from ordinary real-valued agreement conventions.

[Read in atlas](index.html#TCS-5127) · [The Impossibility of Approximate Agreement on a Larger Class of Graphs](https://doi.org/10.4230/LIPIcs.OPODIS.2022.22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5382 — An Exponential Lower Bound for Spectral Density Estimation on Unweighted Graphs — Explicit open question on PDF page 3

Spectral density estimation approximates the distribution of eigenvalues of a graph's normalized adjacency matrix, with error measured in Wasserstein distance. The source proves an exponential dependence on inverse accuracy for estimating this distribution from nonadaptive random walks on unweighted graphs. The question asks whether an exponential lower bound also holds in the random-neighbor model, where exploration can restart from a chosen vertex. That adaptive access can reuse information about previously encountered graph structure, so the existing indistinguishability construction does not directly settle it. Resolving the gap would determine whether adaptive local exploration can fundamentally improve the accuracy cost of estimating a global spectrum.

[Read in atlas](index.html#TCS-5382) · [An Exponential Lower Bound for Spectral Density Estimation on Unweighted Graphs](https://proceedings.mlr.press/v336/peng26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5410 — Strong Linearizability Without Compare&Swap: The Case of Bags — Explicit open question on PDF page 5

Concurrent queues let many processes insert and remove items while presenting behavior consistent with a sequential queue. The source asks for a wait-free linearizable implementation using its class of interfering base objects. Every operation must finish despite arbitrary delays of other processes. The question permits any number of enqueuers and dequeuers, which distinguishes it from easier restricted interfaces. The project probes whether relatively weak shared-memory primitives can support a fully general queue with both progress guarantees and a coherent observable order.

[Read in atlas](index.html#TCS-5410) · [Strong Linearizability Without Compare&Swap: The Case of Bags](https://doi.org/10.4230/LIPIcs.DISC.2025.29)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5425 — Parallel and Distributed Algorithms for the Housing Allocation Problem — Explicit open question on PDF page 8

A housing market assigns houses to agents with strict preferences and an initial ownership allocation. Individual rationality prevents an agent from becoming worse off, while Pareto optimality rules out improvements that help someone without hurting anyone. The source asks for NC algorithms computing such an allocation or the market's core, with polynomial work and polylogarithmic depth. It shows that a proposed allocation can be verified for these properties efficiently in parallel, leaving construction as the additional challenge. A solution would reveal whether the sequential dependencies of trading-cycle procedures are essential or can be replaced by highly parallel allocation methods.

[Read in atlas](index.html#TCS-5425) · [Parallel and Distributed Algorithms for the Housing Allocation Problem](https://doi.org/10.4230/LIPIcs.OPODIS.2019.23)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5427 — New Characterizations in Turnstile Streams with Applications — Explicit open question on PDF page 2

Turnstile streaming algorithms process positive and negative updates to an underlying vector while storing a compact state. For one pass, the source discusses a characterization showing that general algorithms can be replaced by suitable linear sketches under stated correctness assumptions. The question asks whether a comparable characterization exists when several passes over the stream are allowed. Later passes can adapt to information gathered earlier, so a fixed linear summary may no longer capture all useful interactions. A structural theorem would simplify lower bounds and explain whether repeated access fundamentally expands the kinds of compact information a streaming algorithm needs.

[Read in atlas](index.html#TCS-5427) · [New Characterizations in Turnstile Streams with Applications](https://doi.org/10.4230/LIPIcs.CCC.2016.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5473 — Distributed Computation with Local Advice — Explicit open question on PDF page 7

Local advice gives each network vertex externally prepared bits that help it solve a graph problem in a number of rounds depending only on maximum degree. The source asks for a concrete locally checkable labeling problem with an unconditional lower bound on this advice requirement. Its negative result assumes the Exponential-Time Hypothesis and rules out constant advice per node for some problems on general graphs. Positive constructions on restricted graphs and for familiar tasks show that even one sparse advice bit can be powerful. An unconditional hard example would establish an intrinsic information barrier independent of unproved assumptions about centralized computation.

[Read in atlas](index.html#TCS-5473) · [Distributed Computation with Local Advice](https://doi.org/10.4230/LIPIcs.DISC.2025.12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5537 — Sublinear-Round Parallel Matroid Intersection — Explicit open question on PDF page 7

A matroid independence oracle answers whether a selected subset belongs to an abstract family of feasible sets. The specific gap cited here concerns finding a basis of one matroid using parallel batches of only polynomially many independence queries. The source records an Ω̃(n^(1/3)) round lower bound and an O(√n) round upper bound and asks to close the gap. Although the surrounding paper studies matroid intersection, this footnote refers to the single-matroid basis subroutine. A tighter bound would quantify the adaptivity needed to construct a maximal independent set and improve understanding of a primitive used in more complicated matroid algorithms.

[Read in atlas](index.html#TCS-5537) · [Sublinear-Round Parallel Matroid Intersection](https://doi.org/10.4230/LIPIcs.ICALP.2022.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5591 — Explicit Space-Time Tradeoffs for Proof Labeling Schemes in Graphs with Small Separators — Explicit open question on PDF page 4

A t-round proof-labeling scheme lets each vertex inspect a wider neighborhood when checking a distributed certificate. On graph families with useful separators, certificate information can be spread across nearby vertices to reduce storage. The source conjectures that this advantage does not hold uniformly on good expander graphs: some predicates cannot gain substantially smaller certificates merely by allowing more rounds. The claim is about limitations of a general space-time tradeoff, rather than saying every property becomes hard on expanders. Resolving it would connect local proof compression with the structural ability to separate a graph into manageable pieces.

[Read in atlas](index.html#TCS-5591) · [Explicit Space-Time Tradeoffs for Proof Labeling Schemes in Graphs with Small Separators](https://doi.org/10.4230/LIPIcs.OPODIS.2021.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5670 — The Singular Optimality of Distributed Computation in LOCAL — Unresolved-question passage on page 14

In the KT₁ LOCAL model, each vertex initially knows its neighbors' identities and can send messages of unrestricted size. This knowledge permits algorithms whose total message count is close to the number of vertices even on dense graphs. The source asks whether breadth-first-search tree construction can be performed in O(D) rounds while using Õ(n) messages, with analogous targets for leader election and broadcast. Its nearly optimal results leave extra logarithmic time factors, and the question seeks to remove those while preserving message savings. Achieving the bound would make global coordination run at the network's natural diameter scale with very little total communication.

[Read in atlas](index.html#TCS-5670) · [The Singular Optimality of Distributed Computation in LOCAL](https://doi.org/10.4230/LIPIcs.OPODIS.2024.26)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5677 — Complexity Landscape for Local Certification — Explicit open question on PDF page 8

Local certification uses labels whose consistency can be checked within a small neighborhood. Even paths can support properties requiring nonconstant certificate sizes. The source asks whether a gap exists between doubly logarithmic and logarithmic label complexity on paths. A gap theorem would exclude every intermediate asymptotic regime, while a construction would exhibit one. The project seeks a finer description of how much distributed proof information can be necessary on the simplest connected graph topology.

[Read in atlas](index.html#TCS-5677) · [Complexity Landscape for Local Certification](https://doi.org/10.4230/LIPIcs.DISC.2025.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5795 — Streaming Complexity of Spanning Tree Computation — Explicit open question on PDF page 1

Depth-first-search tree construction is easy when a streaming algorithm can retain the complete graph. The semi-streaming restriction instead allows only Õ(n) memory for an n-vertex graph, potentially requiring repeated edge scans. The source asks whether more than one pass is inherently necessary to construct a DFS tree in this space regime. Its cited algorithms have pass counts depending on the height of the produced tree, leaving a large gap between simple upper bounds and the sought impossibility result. Resolving the one-pass question would determine whether the nested dependencies of depth-first search force repeated access under near-linear storage.

[Read in atlas](index.html#TCS-5795) · [Streaming Complexity of Spanning Tree Computation](https://doi.org/10.4230/LIPIcs.STACS.2020.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5797 — Local Certification of Local Properties: Tight Bounds, Trade-Offs and New Parameters — Open problem 2

Local certification gives each graph vertex a short certificate and lets it verify a global claim by inspecting nearby information. Suppose the optimal certificate size is s when the verifier sees only distance-one neighborhoods. The conjecture asks whether allowing inspection to distance d always reduces the required size to at most a constant times s/d. For local properties, the source stresses that the dependence must track their natural parameters, rather than merely asymptotic graph size. Resolving this tradeoff would show whether a wider view can universally substitute for stored proof information or whether some properties resist such compression.

[Read in atlas](index.html#TCS-5797) · [Local Certification of Local Properties: Tight Bounds, Trade-Offs and New Parameters](https://doi.org/10.4230/LIPIcs.STACS.2024.21)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5939 — A Time and Space Optimal Stable Population Protocol Solving Exact Majority — Unresolved-question passage on page 11

Exact-majority population protocols must eventually make all agents stably report which of two initial opinions was more numerous. The source asks whether every stable monotone protocol achieving polylogarithmic time needs Ω(log n) states without assuming output dominance. Existing lower bounds require that additional condition, which restricts how configurations retaining a reported answer may evolve. The alternative would be a protocol with o(log n) states that reaches stable majority quickly by violating output dominance. Settling this would determine whether the source's logarithmic-state construction is optimal because of the task itself or because of a technical restriction in the lower-bound argument.

[Read in atlas](index.html#TCS-5939) · [A Time and Space Optimal Stable Population Protocol Solving Exact Majority](https://doi.org/10.1109/FOCS52979.2021.00104)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6022 — Sampling Arborescences in Parallel — Unresolved-question passage on page 17

An Eulerian tour of a directed graph traverses every edge exactly once before returning to its start. The intended question in this parallel-sampling paper is whether such tours can be sampled uniformly using an RNC algorithm. Determinant-based counting and the BEST theorem connect Eulerian tours with rooted directed spanning trees. Although the source gives a parallel sampler for those trees, the familiar reduction to tours is only known there as a polynomial-time construction, leaving its parallel implementation unsettled. A fast sampler would convert a structural counting relationship into an efficient method for generating random global edge traversals.

[Read in atlas](index.html#TCS-6022) · [Sampling Arborescences in Parallel](https://doi.org/10.4230/LIPIcs.ITCS.2021.83)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6039 — Local Certification of Geometric Graph Classes — Unresolved-question passage on page 12

Local certification distributes short certificates to graph vertices, which verify a property using only their own and neighboring information. The source studies the certificate size required to recognize geometric graph classes in this model. It asks whether hardness for the existential theory of the reals necessarily entails a polynomial lower bound on local certificate size. Segment and string intersection graphs motivate the proposed connection between centralized recognition difficulty and local verification. A resolution would need to explain why algebraic complexity can or cannot force large distributed witnesses, rather than relying only on expensive coordinate representations.

[Read in atlas](index.html#TCS-6039) · [Local Certification of Geometric Graph Classes](https://doi.org/10.4230/LIPIcs.MFCS.2024.48)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6080 — Quadratic and Near-Quadratic Lower Bounds for the CONGEST Model — Unresolved-question passage on page 12

Weighted all-pairs shortest paths requires every vertex to learn exact distances to all others in an edge-weighted network. The 2017 source asks whether this can be done in a linear number of CONGEST communication rounds. Straightforward repeated distance propagation is slower, while subquadratic algorithms suggest room for improvement. The paper also shows that a standard two-party communication framework cannot establish a superlinear lower bound for this task. The question therefore seeks either an algorithm coordinating many weighted searches within linear time or a different explanation of why their shared communication demands prevent it.

[Read in atlas](index.html#TCS-6080) · [Quadratic and Near-Quadratic Lower Bounds for the CONGEST Model](https://doi.org/10.4230/LIPIcs.DISC.2017.10)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6125 — Locally Checkable Labelings with Small Messages — Explicit open question on PDF page 4

Locally checkable labeling problems have solutions whose validity can be inspected within neighborhoods of constant radius. The source asks for a bounded-degree graph problem solvable in O(log n) LOCAL rounds but requiring Ω(n) CONGEST rounds. The two models differ only in message-size restrictions, so such a separation would isolate the cost of bandwidth. The paper already separates them by a smaller gap on general graphs while showing matching complexities on trees. A stronger example would demonstrate that even a locally verifiable task can require nearly global communication time when short messages replace unrestricted exchanges.

[Read in atlas](index.html#TCS-6125) · [Locally Checkable Labelings with Small Messages](https://doi.org/10.4230/LIPIcs.DISC.2021.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6206 — Detecting Cliques in CONGEST Networks — Explicit open question on PDF page 4

In CONGEST_b, each graph edge carries at most b bits per communication round. The source studies detecting cliques with size at least four and up to order √n, asking how far the round complexity exceeds its roughly √n/b lower-bound scale. A linear-round algorithm leaves a substantial gap, particularly for fixed clique sizes. The paper proves that its two-party vertex-partition method cannot establish the stronger lower bounds that would close that gap. The project therefore calls for improved detection algorithms or new communication-hardness techniques that capture interactions among more than the two partitioned views.

[Read in atlas](index.html#TCS-6206) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6324 — Hardness of Computing and Approximating Predicates and Functions with Leaderless Population Protocols — Unresolved-question passage on page 12

Leaderless population protocols compute predicates and numerical functions of input counts through interactions among finite-state agents. The source proves stabilization-time lower bounds for broad semilinear functions and predicates, but its hypotheses exclude some eventual behaviors. It asks for optimal time bounds on the remaining eventually natural-linear functions and eventually constant predicates. Examples include a function that equals its input above a small threshold and a predicate that becomes true once at least two inputs are present. A classification would explain whether these simple asymptotic forms permit faster stable computation than the more expressive semilinear cases covered by the lower bounds.

[Read in atlas](index.html#TCS-6324) · [Hardness of Computing and Approximating Predicates and Functions with Leaderless Population Protocols](https://doi.org/10.4230/LIPIcs.ICALP.2017.141)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6380 — A Simple Parallel Algorithm for Natural Joins on Binary Relations — Explicit open question on PDF page 3

A natural join combines database relations by matching equal values on shared attributes. In massively parallel computation, the load measures how much data any one of p machines must handle. The question asks for algorithms matching the Ω(m/p^(1/ρ)) load bound for arbitrary join queries, where m is total input size and ρ is the fractional edge-cover number. The source achieves the target for binary-relation joins in a small constant number of rounds, but those graph-shaped queries do not cover arbitrary relation arities. A general construction would align parallel join execution with the structural lower bound of the query hypergraph.

[Read in atlas](index.html#TCS-6380) · [A Simple Parallel Algorithm for Natural Joins on Binary Relations](https://doi.org/10.4230/LIPIcs.ICDT.2020.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6418 — Tight Bounds For Distributed MST Verification — Explicit open question on PDF page 2

Distributed minimum spanning tree construction requires network vertices to agree on a minimum-weight spanning tree using messages along graph edges. The historical question in the 2011 source asks for one algorithm achieving both nearly linear message complexity and nearly optimal time. Its targets are Õ(|E|) messages and Õ(√n + D) time, where D is the network diameter. The paper attains these simultaneous bounds for verifying a proposed tree and contrasts them with the separate construction guarantees available in its discussion. This frames the project as understanding whether communication economy and rapid global coordination can coexist in constructing an optimal network backbone.

[Read in atlas](index.html#TCS-6418) · [Tight Bounds For Distributed MST Verification](https://doi.org/10.4230/LIPIcs.STACS.2011.69) · [https://doi.org/10.4230/LIPIcs.DISC.2022.19](https://doi.org/10.4230/LIPIcs.DISC.2022.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6918 — Separate constant-time algorithms using identifier values from order-invariant algorithms, without consecutive-ID promises.

Distributed identifiers can be used either as numerical data or merely to compare the relative order of vertices. The question asks for a problem solvable in constant time by exploiting actual identifier values but impossible for every order-invariant constant-time algorithm. The source explains that locally checkable labeling problems cannot provide the desired example under the classical equivalence result. It also excludes the artificial promise that identifiers are exactly consecutive integers, which would make selecting identifier one a trivial separation. A meaningful example would reveal computational information carried by arbitrary unique names beyond their ability to break symmetry through comparisons.

[Read in atlas](index.html#TCS-6918) · [Survey of Local Algorithms](https://www.cs.helsinki.fi/local-survey/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7010 — Determine optimal linear-sketch dimension for constant-factor approximation of the nuclear norm.

The nuclear norm of a matrix is the sum of its singular values and measures a different aspect of size from the Frobenius or spectral norm. A linear sketch compresses the matrix through linear measurements before estimating this norm. The source asks for the optimal sketch dimension needed for a constant-factor approximation. Its discussion places nuclear-norm sketching between neighboring norms with very different behavior: constant dimension for the Frobenius norm and essentially full matrix dimension for the spectral norm. Tight bounds would show whether low-dimensional linear summaries can preserve this important aggregate of singular-value information.

[Read in atlas](index.html#TCS-7010) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

## Optimization and numerical computation (34)

### TCS-0008 — Does general rational linear programming have a strongly polynomial algorithm?

Linear programming optimizes a linear objective subject to linear equality and nonnegativity constraints. The question asks whether every rational instance can be solved using a number of arithmetic operations polynomial only in its numbers of variables and constraints. Intermediate numbers must also have encoding lengths bounded polynomially in the full input length. Existing polynomial-time guarantees may depend on how many bits describe the coefficients, which is the dependence this target seeks to remove. A solution must handle exact optima, infeasibility, and unbounded objectives within the same strongly polynomial framework.

[Read in atlas](index.html#TCS-0008) · [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8) · [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250) · [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf) · [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186) · [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf) · [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6574 — Is exact semidefinite feasibility in polynomial time?

A semidefinite feasibility instance asks whether some real assignment makes an affine combination of rational symmetric matrices positive semidefinite. The target is an exact yes-or-no decision in polynomial time in the ordinary bit model. Numerical approximation does not settle this question because an infeasible affine space can approach the positive semidefinite cone arbitrarily closely. Feasible rational inputs can also require irrational or very large witnesses. The challenge is to decide arbitrary degenerate instances efficiently without adding regularity assumptions that make approximation algorithms easier to analyze.

[Read in atlas](index.html#TCS-6574) · [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433) · [On the Turing Model Complexity of Interior Point Methods for Semidefinite Programming](https://epubs.siam.org/doi/10.1137/15M103114X) · [Exact algorithms for semidefinite programs with degenerate feasible set](https://www.sciencedirect.com/science/article/pii/S0747717120301176) · [How Do Exponential Size Solutions Arise in Semidefinite Programming?](https://epubs.siam.org/doi/10.1137/21M1434945) · [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271) · [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6585 — Nearly linear-time solution of general sparse linear systems

A sparse linear system stores only the nonzero entries of its coefficient matrix, making matrix-vector multiplication relatively cheap. The question asks whether solving every well-conditioned rational system approximately can take nearly linear time in that sparse input size. The saved formulation bounds coefficient lengths, conditioning, and requested residual accuracy to avoid hiding excessive numerical costs. It seeks an explicit solution vector with high enough success probability from a randomized classical algorithm. Such a result would extend the efficiency of structured Laplacian solvers to general sparse matrices, where sparsity alone currently provides much less algorithmic structure.

[Read in atlas](index.html#TCS-6585) · [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254) · [Nearly Linear Time Algorithms for Preconditioning and Solving Symmetric, Diagonally Dominant Linear Systems](https://epubs.siam.org/doi/10.1137/090771430) · [Matrix anti-concentration inequalities with applications](https://arxiv.org/abs/2111.05553) · [Hardness Results for Laplacians of Simplicial Complexes via Sparse-Linear Equation Complete Gadgets](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53) · [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6578 — Smale’s seventh problem: efficient near-minimal logarithmic energy on the sphere

Smale's seventh problem concerns placing N points on the unit sphere so that their logarithmic interaction energy is nearly minimal. The target is an algorithm running in time polynomial in N. Its output energy may exceed the global minimum by only a universal constant times log N. This is an additive energy guarantee, which requires more precise control than merely producing visually well-distributed points. A construction with a rigorous bound would connect efficient computation with the equilibrium behavior of many mutually repelling particles on a curved surface.

[Read in atlas](index.html#TCS-6578) · [Logarithmic energy for zeros of random polynomials](https://www.lebesgue.fr/sites/default/files/inline-files/Yakir.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6572 — Is there a polynomial-time simplex pivot rule?

The simplex method solves a linear program by moving between feasible bases through legal pivots. This question asks for a deterministic pivot algorithm whose total bit complexity is polynomial for every rational input and supplied feasible starting basis. Finding the optimum by another method does not suffice unless the required sequence of pivots can also be followed efficiently. Degenerate pivots complicate progress because they may change the basis without changing the objective value. A positive answer would provide a worst-case polynomial guarantee for simplex itself, without automatically establishing the stronger arithmetic bound of strongly polynomial linear programming.

[Read in atlas](index.html#TCS-6572) · [Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time](https://www.cs.yale.edu/homes/spielman/simplex/) · [An unconditional lower bound for the active-set method on the hypercube](https://arxiv.org/abs/2502.18019) · [An Unconditional Lower Bound for the Active-Set Method in Convex Quadratic Maximization](https://epubs.siam.org/doi/10.1137/1.9781611978971.14) · [Lower Bounds for Ranking-Based Pivot Rules](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.31/LIPIcs.STACS.2026.31.html) · [On the number of degenerate simplex pivots](https://link.springer.com/article/10.1007/s10107-026-02349-x)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0491 — Can every fixed-dimensional Tarski problem be solved with O(log² n) queries?

A monotone function on a finite multidimensional grid is guaranteed to have a fixed point. The project asks whether one can find any such point using only a squared-logarithmic number of value queries in the grid side length. The dimension is fixed, and the multiplicative constant may depend arbitrarily on it. Incomparable grid points complicate the interval-discarding ideas that make one-dimensional search efficient. A positive answer would show that higher fixed dimensions need not increase the logarithmic query exponent, independently of the computation performed between queries.

[Read in atlas](index.html#TCS-0491) · [Finite and Algorithmic Model Theory (Dagstuhl Seminar 22051)](https://doi.org/10.4230/DagRep.12.1.101) · [A Faster Algorithm for Finding Tarski Fixed Points](https://doi.org/10.1145/3524044) · [Tarski Lower Bounds from Multi-Dimensional Herringbones](https://arxiv.org/abs/2502.16679v2) · [The Mystery Deepens: On the Query Complexity of Tarski Fixed Points](https://arxiv.org/abs/2604.00268v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0724 — The Oracle Complexity of Convex Optimization with Limited Memory

First-order convex optimization learns about an objective through queries returning its value and a subgradient. The source asks how the number of queries needed for a prescribed accuracy changes when the algorithm has limited working memory. It highlights methods with strong oracle complexity whose stored geometric information can require quadratic space in dimension. The question is whether that memory cost is inherent or can be traded away without losing the optimal query rate. A sharp tradeoff would distinguish information acquired from the oracle from information that must remain available between optimization steps.

[Read in atlas](index.html#TCS-0724) · [COLT / PMLR](https://proceedings.mlr.press/v99/woodworth19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0728 — The Oracle Complexity of Smooth Convex Optimization in Nonstandard Settings

Smooth convex optimization is often analyzed when the objective's regularity and the feasible region use compatible norms. The source instead studies settings where these geometries differ, including vector norms and their matrix counterparts. It asks for the optimal oracle complexity of minimizing such functions using black-box first-order information. The stated gaps concern how smoothness, domain geometry, dimension, and target accuracy interact. Matching algorithms and lower bounds would show whether sparse and low-rank optimization models permit faster convergence than methods designed around a single common norm suggest.

[Read in atlas](index.html#TCS-0728) · [COLT / PMLR](https://proceedings.mlr.press/v40/Guzman15.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0722 — Polynomial linearly-convergent method for g-convex optimization?

Geodesically convex optimization replaces straight segments with shortest paths on a Riemannian manifold. The question asks for a deterministic first-order algorithm with query complexity polynomial in dimension and logarithmic in inverse accuracy. It also requires polynomial arithmetic work per query, so a powerful but computationally intractable geometric oracle would not suffice. The source develops an ellipsoid-like approach for constant-curvature spaces and identifies obstacles on more general manifolds. A solution would extend the efficient precision dependence of Euclidean convex optimization to curved spaces while respecting the cost of manipulating their geometry.

[Read in atlas](index.html#TCS-0722) · [COLT / PMLR](https://proceedings.mlr.press/v195/criscitiello23b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0344 — Additivity of extension complexity under Cartesian products

Extension complexity measures how many facets are needed in a higher-dimensional polytope projecting onto a given polytope. For a Cartesian product, describing the two factors separately gives a natural additive construction. The source asks whether a more economical extension can ever beat that sum. It notes that certain factor types, including pyramids, rule out the proposed saving. The question tests whether two independent feasible regions can share hidden inequalities in a lifted formulation, rather than merely combining their existing descriptions.

[Read in atlas](index.html#TCS-0344) · [Computational Geometry](https://doi.org/10.4230/DagRep.9.4.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0687 — Best Arm Identification: Almost Instance-Wise Optimality and the Gap Entropy Conjecture

Best-arm identification tries to find the option with the largest expected reward while minimizing the number of samples. The source asks for an algorithm whose sample complexity is close to optimal for each individual configuration of reward gaps. Exact instance optimality already faces an obstruction for two arms, so the proposal allows a separate additive term reflecting that difficulty. Its gap-entropy conjecture uses the distribution of arms across gap scales to describe the remaining cost. Establishing this characterization would explain how an instance's detailed structure affects exploration beyond a single worst-gap or total-inverse-gap summary.

[Read in atlas](index.html#TCS-0687) · [COLT / PMLR](https://proceedings.mlr.press/v49/chen16b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0725 — Second-order cone representability of semialgebraic convex hulls

A semialgebraic set is described by polynomial equalities and inequalities, while its convex hull collects all convex combinations of its points. The source asks when that convex hull can be represented using second-order cone constraints and auxiliary variables. It also asks how many additional variables such a representation requires. Representability is stronger than having a useful numerical relaxation, because the projected feasible region must agree exactly with the desired hull. A structural answer would identify nonlinear models that can be converted into a tractable conic formulation and quantify the cost of that conversion.

[Read in atlas](index.html#TCS-0725) · [Designing and Implementing Algorithms for Mixed-Integer Nonlinear Optimization](https://doi.org/10.4230/DagRep.8.2.64)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0914 — Deterministic min-cost matching with delays

Matching with delays pairs arriving requests while charging both pairing cost and the time requests wait. The saved question seeks deterministic algorithms for the minimum-cost version. Waiting can reveal better future partners but increases the cost already incurred by unmatched requests. Understanding deterministic performance would show how much useful anticipation can be achieved without randomized decisions. The inherited label does not specify the metric, online model, or competitive-ratio target, so it cannot yet support a particular bound or be identified with offline matching.

[Read in atlas](index.html#TCS-0914) · [Scheduling](https://doi.org/10.4230/DagRep.10.2.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0673 — Is There a First-Order Method that Only Converges to Local Minimax Optima?

Minimax optimization models a player minimizing an objective against a second player who maximizes it. In nonconvex–nonconcave problems, stationary points need not represent the intended local minimax behavior. The selected question asks for a first-order method whose stable convergence targets are restricted to local minimax optima. Reversing the players' optimization order or merely driving both gradients toward zero can select inappropriate solutions. A method with the desired guarantee would clarify the dynamics needed for adversarial optimization, including the mathematical problems underlying some generative-model training procedures.

[Read in atlas](index.html#TCS-0673) · [COLT / PMLR](https://proceedings.mlr.press/v195/chae23a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0643 — Permutation structure in two-dimensional discrepancy minimization

A permutation point set puts one point in each row and column of a uniform square grid. The source asks which such permutations have low discrepancy and when exact minimizers must have this structure. The identity permutation illustrates that balanced coordinate projections alone can still leave a linear counting error. A 2026 journal result gives a four-point periodic L2 minimizer whose coordinate projections are not equally spaced. The source’s remaining norm, configuration domain and single mathematical target still need to be specified.

[Read in atlas](index.html#TCS-0643) · [Algorithms and Complexity for Continuous Problems](https://doi.org/10.4230/DagRep.13.8.106) · [Minimizing Point Configurations for Tensor Product Energies on the Torus](https://doi.org/10.1007/s00365-026-09764-5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0645 — Standard information versus linear information for Lp -approximation

Approximating a continuous function can use either sampled function values or arbitrary continuous linear measurements. The source compares the best worst-case convergence rates of these two information models over compact, convex, symmetric function classes. It asks how much polynomial convergence exponent is lost by restricting access to point evaluations when error is measured in an Lp norm. A concrete conjecture proposes a loss of one half for p at least two and sufficiently fast linear-information convergence. This would quantify the extra sample cost of using experimentally accessible observations instead of unrestricted linear information.

[Read in atlas](index.html#TCS-0645) · [Algorithms and Complexity for Continuous Problems](https://doi.org/10.4230/DagRep.13.8.106)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1512 — A central open question remains: can we design size-independent sparsifiers for general integer linear programs, with degree depending only on 1/p, 1/ϵ, and intrinsic structural […]

Stochastic packing problems may require probing items before learning which ones are available or useful. The source measures sparsifier size through containment in a scaled feasibility polytope, rather than simply counting queried items. It asks whether general integer linear programs admit sparsifiers whose degree is independent of total instance size. The allowed dependence is on availability and accuracy parameters together with intrinsic structural features of the constraints. Such a theorem would show when near-optimal solutions can be recovered from a bounded amount of structurally relevant information across much broader packing models.

[Read in atlas](index.html#TCS-1512) · [Near-Optimal Sparsifiers for Stochastic Knapsack and Assignment Problems](https://doi.org/10.4230/LIPIcs.ITCS.2026.51)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2277 — There exists an algorithm that on input M ∈ Zd×n such that 0 ∈ int(P ), a vector v ∈ (Q(i)× )n , and ε […]

The cited paper studies robust orbit problems for torus actions, where algebraic transformations act on vectors. Its saved conjecture begins an algorithmic statement using an integer matrix, nonzero Gaussian-rational coordinates, and an accuracy parameter. The promise that zero lies inside a specified polytope signals geometric structure relevant to the orbit. An effective algorithm could connect numerical robustness with algebraic orbit questions and the number-theoretic bounds studied in the paper. The excerpt omits the output, runtime, and definition of the polytope, so no precise algorithmic guarantee can be reconstructed safely.

[Read in atlas](index.html#TCS-2277) · [Complexity of Robust Orbit Problems for Torus Actions and the abc-Conjecture](https://doi.org/10.4230/LIPIcs.CCC.2024.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2675 — This open problem is whether there is an algorithm other than uniform sampling itself that performs uniformly no worse than uniform sampling in the fixed-budget […]

Uniform sampling allocates the same number of observations to each arm before recommending the best one. In fixed-budget best-arm identification, the source asks whether another algorithm can perform asymptotically no worse on every instance. The comparison uses the decay rate of recommendation error, rather than cumulative reward during sampling. Adaptive allocation can improve selected instances, but it may pay for those improvements on other reward configurations. A uniformly dominating method would give a principled alternative to equal allocation without requiring advance knowledge of which instance-specific exploration pattern is favorable.

[Read in atlas](index.html#TCS-2675) · [Open Problem: Optimal Best Arm Identification with Fixed-Budget](https://proceedings.mlr.press/v178/open-problem-qin22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3142 — Nevertheless we leave it as an open problem if there is some first-order optimization method that achieves rate of 𝑇 = 𝑂 (1/ε2 ) (see […]

Stochastic convex optimization seeks small population risk from a finite sample of convex loss functions. The source separates the generalization behavior of stochastic gradient descent from full-batch gradient descent on the empirical risk. Its remaining question asks whether another first-order method using empirical-risk information can reach excess risk epsilon in order epsilon to the minus two iterations. The target is population accuracy, so rapidly minimizing training loss alone is insufficient. A solution would identify whether the observed disadvantage belongs specifically to gradient descent or extends to the broader full-batch first-order information model.

[Read in atlas](index.html#TCS-3142) · [SGD Generalizes Better Than GD (And Regularization Doesn’t Help)](https://proceedings.mlr.press/v134/amir21a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3429 — We conjecture that the optimal complexity of monotone inclusion is: (i) Θ( LD 1 L LD ) when the operator is either L-Lipschitz or L […]

Monotone inclusion seeks a point where a monotone operator satisfies an appropriate zero or feasibility condition. The source connects this task with variational inequalities, nonexpansive fixed points, and proximal methods. Its question asks to close the remaining gaps between oracle upper and lower bounds. The conjectured rates distinguish Lipschitz or cocoercive operators from operators that are also strongly monotone. Matching results would determine exactly how regularity and the initial distance scale control the number of operator evaluations needed for an approximate solution, rather than only showing that particular iterative methods converge.

[Read in atlas](index.html#TCS-3429) · [Halpern Iteration for Near-Optimal and Parameter-Free Monotone Inclusion and Strong Solutions to Variational Inequalities](https://proceedings.mlr.press/v125/diakonikolas20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3676 — The exact complexity of the following variant of the problem remains open: given an MDP and a horizon encoded in binary, determine whether there exists […]

A finite-horizon Markov decision process asks a controller to maximize expected accumulated reward over a prescribed number of steps. Here the horizon is encoded in binary and can greatly exceed the written input size. The project asks the exact complexity of deciding whether any policy reaches a supplied expected-reward threshold. No restriction is imposed on which actions the policy may use, distinguishing the target from related value-iteration questions. Understanding this version would reveal the cost of planning across a very long but succinctly specified time interval.

[Read in atlas](index.html#TCS-3676) · [On the Complexity of Value Iteration (Track B: Automata, Logic, Semantics, and Theory of Programming)](https://doi.org/10.4230/LIPIcs.ICALP.2019.102)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4293 — We conjecture that the following problem is P LS-complete: given an instance of k-means, compute an arbitrary local minimum of the k-means method.

The k-means method repeatedly assigns points to centers and updates centers to improve a clustering objective. The source conjectures PLS-completeness of finding an arbitrary local minimum of this method. A locally stable clustering need not minimize the global objective, but searching for even such stability can be difficult. A classification would explain whether slow convergence reflects inherent local-search complexity rather than an unfortunate execution path. The saved statement does not specify point encoding, degeneracies, or the exact neighborhood, which must be fixed to define the relevant local-optimum search problem.

[Read in atlas](index.html#TCS-4293) · [The Complexity of the k-means Method](https://doi.org/10.4230/LIPIcs.ESA.2016.78)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4661 — Then we conjecture that the following two inequalities always hold:     Yk Yk Ewo  Aij  ≤ Ewr  Aij  […]

Sampling data without replacement changes the matrix products that arise in incremental optimization and randomized linear-system solvers. The source formulates two conjectured inequalities comparing products of positive semidefinite matrices under sampling with and without replacement. One concerns the operator norm of an averaged product, while the other uses the paired product relevant to squared error. The paper develops special cases and connects the proposed comparisons to the progress of incremental gradient and Kaczmarz iterations. The central task is to determine the validity and necessary assumptions of these noncommutative arithmetic-geometric mean comparisons.

[Read in atlas](index.html#TCS-4661) · [Toward a Noncommutative Arithmetic-geometric Mean Inequality: Conjectures, Case-studies, and Consequences](https://proceedings.mlr.press/v23/recht12.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5005 — Gradient Methods with Online Scaling — Explicit open question on PDF page 2

Adaptive scaling changes the geometry of gradient updates through a learned positive-definite preconditioner. The source introduces the question of matching a convergence rate controlled by the best available scaling, with logarithmic dependence on inverse accuracy. The same paper then answers this motivating question affirmatively through its online scaled gradient framework, with the stated asymptotic qualification. Its guarantee compares with scaling optimized for the observed trajectory and includes stronger behavior on quadratic objectives. This record therefore captures a motivating problem and the source's claimed resolution, rather than an independently established remaining open case.

[Read in atlas](index.html#TCS-5005) · [Gradient Methods with Online Scaling](https://proceedings.mlr.press/v291/gao25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5330 — Deterministic (2/3 - ε)-Approximation of Matroid Intersection Using Nearly-Linear Independence-Oracle Queries — Explicit open question on PDF page 2

Matroid intersection seeks the largest set that is independent in each of two matroids accessed through independence tests. The source provides a deterministic nearly linear-query approximation approaching two thirds of optimum. It asks whether the same query scale can instead achieve a factor arbitrarily close to one for the general range of optimum ranks. Randomized algorithms reach this stronger approximation in the cited comparison. The challenge is to organize deterministic exchanges and information gathering without paying a superlinear query cost that random sampling can avoid.

[Read in atlas](index.html#TCS-5330) · [Deterministic (2/3 - ε)-Approximation of Matroid Intersection Using Nearly-Linear Independence-Oracle Queries](https://doi.org/10.4230/LIPIcs.WADS.2025.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5494 — The Complexity of Making the Gradient Small in Stochastic Convex Optimization — Explicit open question on PDF page 2

Stochastic optimization receives noisy information about an objective and often aims to find a point with small gradient. The extracted passage asks for a sharp account of the oracle complexity of reaching such approximate stationarity. Its surrounding discussion includes nonconvex functions, where global minimization is generally too demanding a target. The same paper develops nearly matching results for the convex setting, so those resolved cases must be separated from the broader motivation. The remaining research direction is to identify optimal stochastic information requirements under explicitly stated smoothness, noise, and function-class assumptions.

[Read in atlas](index.html#TCS-5494) · [The Complexity of Making the Gradient Small in Stochastic Convex Optimization](https://proceedings.mlr.press/v99/foster19b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5635 — On the Complexity of Robust Markov Decision Processes and Bisimulation Metrics — Explicit open question on PDF page 5

Policy iteration solves a discounted Markov decision process by repeatedly evaluating a policy and switching to better actions. Each policy evaluation reduces to a linear system, but the number of improvement steps can dominate the computation. The source asks whether the algorithm runs in polynomial time with a bound independent of the discount factor when that factor is part of the input. Its stated iteration bound contains an inverse dependence on one minus the discount factor, which becomes large near one. Removing that dependence would give a stronger explanation for the efficiency of this widely used optimization procedure.

[Read in atlas](index.html#TCS-5635) · [On the Complexity of Robust Markov Decision Processes and Bisimulation Metrics](https://doi.org/10.4230/LIPIcs.CONCUR.2026.48)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6024 — The Niceness of Unique Sink Orientations — Explicit open question on PDF page 2

Random Edge is a simplex pivot rule that chooses an outgoing improving edge uniformly at random. The source studies its behavior through unique-sink orientations, an abstraction of optimization over cube-like structures. The extracted question asks for a subexponential upper bound on Random Edge for linear programming. Existing lower bounds exclude a polynomial guarantee, while known combinatorial analyses still leave a substantial gap. A sharper upper bound would deepen understanding of how local random moves navigate optimization landscapes, even though other algorithms already achieve subexponential complexity by different means.

[Read in atlas](index.html#TCS-6024) · [The Niceness of Unique Sink Orientations](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.30)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6034 — Node-Connectivity Terminal Backup, Separately-Capacitated Multiflow, and Discrete Convexity — Explicit open question on PDF page 2

The edge-connectivity terminal backup problem buys a minimum-cost network so that each terminal has its required connectivity to the other terminals collectively. The selected version allows general edge capacities and places no finite capacity restriction on internal vertices. The source asks whether this integer optimization problem is polynomial-time solvable or NP-hard. Its algorithms address fractional relaxations and support approximation results for a broader node-capacitated problem. An exact classification would determine whether the strong flow and discrete-convex structure of the relaxation can overcome the remaining integrality constraints.

[Read in atlas](index.html#TCS-6034) · [Node-Connectivity Terminal Backup, Separately-Capacitated Multiflow, and Discrete Convexity](https://doi.org/10.4230/LIPIcs.ICALP.2020.65)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6319 — Maintaining Perfect Matchings at Low Cost — Explicit open question on PDF page 4

Online matching on the line assigns arriving requests to available partners using distance as cost. Future requests are unknown, so a locally attractive assignment can force expensive later choices. The cited passage asks whether any algorithm has a constant competitive ratio in this metric. The surrounding work studies robustness and recourse as related ways to manage changing matchings. The project concerns whether the one-dimensional ordering alone provides enough structure to overcome the uncertainty inherent in irrevocable online allocation.

[Read in atlas](index.html#TCS-6319) · [Maintaining Perfect Matchings at Low Cost](https://doi.org/10.4230/LIPIcs.ICALP.2019.82)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6483 — Improved Lower Bounds for Submodular Function Minimization — Unresolved-question passage on page 5

Submodular function minimization seeks a minimum-value subset using queries to a value oracle. The source proves a superlinear query lower bound for deterministic algorithms. It asks whether any superlinear lower bound can also be established for randomized algorithms with a suitable success guarantee. The construction's deterministic difficulty can disappear when random queries quickly discover the relevant hidden structure. New lower-bound ideas would therefore be needed to show that randomization cannot always reduce the information needed for general submodular minimization back to essentially linear scale.

[Read in atlas](index.html#TCS-6483) · [Improved Lower Bounds for Submodular Function Minimization](https://doi.org/10.1109/FOCS54457.2022.00030)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7007 — Obtain relative spectral low-rank approximation in O(nnz(A))+n·poly(k/ε) time.

Spectral low-rank approximation seeks a rank-k representation whose largest directional error is near the best possible. The source asks for a relative-error guarantee in time equal to reading the nonzero matrix entries plus a term linear in n and polynomial in k over epsilon. That speed is available in the cited comparison for Frobenius error, which aggregates squared errors instead of controlling the worst direction. The spectral target is therefore substantially stronger. A solution would make sparse-matrix compression fast while protecting against a large error concentrated in one singular direction.

[Read in atlas](index.html#TCS-7007) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7008 — Obtain polynomial-time relative low-rank approximation in entrywise ℓ₁ error.

Robust low-rank approximation measures reconstruction error by the sum of absolute entrywise differences. The source asks for a polynomial-time algorithm returning a rank-k factorization within a factor one plus epsilon of the best such approximation. This changes the geometry from the squared-error setting where singular values and standard sketching methods are especially effective. Approximating a sum of row norms is also a different guarantee and does not settle the entrywise objective. An algorithm or hardness classification would clarify whether near-optimal robust matrix compression admits the same broad computational tractability as classical low-rank approximation.

[Read in atlas](index.html#TCS-7008) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

## Geometry, topology and metric spaces (65)

### TCS-6523 — Does every isotropic log-concave measure have a dimension-free Poincaré constant?

The KLS conjecture concerns log-concave probability distributions normalized to have mean zero and identity covariance. It asks whether every sufficiently regular function has variance bounded by a universal constant times its average squared gradient. That constant must work in every dimension and for every such distribution. Geometrically, this would exclude narrow bottlenecks that covariance normalization fails to reveal. The question connects high-dimensional convex geometry with the mixing of sampling algorithms, and control of particular observables alone does not settle it.

[Read in atlas](index.html#TCS-6523) · [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/) · [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf) · [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551) · [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf) · [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2) · [The KLS constant is O(log^{1/4} n)](https://arxiv.org/abs/2607.24164v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6525 — Gupta–Newman–Rabinovich–Sinclair conjecture

The GNRS conjecture asks how faithfully shortest-path distances in graphs excluding a fixed minor can be represented in ℓ₁. The graph may have arbitrary positive edge lengths, and every pair of vertices must be preserved within a constant factor. This constant may depend on the excluded minor but cannot grow with the graph. Because ℓ₁ metrics decompose into weighted cuts, the question also governs multicommodity flow–cut gaps. Even the planar case tests whether a strong topological restriction is enough to remove all growing distortion.

[Read in atlas](index.html#TCS-6525) · [Cuts, Trees and ℓ₁-Embeddings of Graphs](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf) · [Pathwidth, trees, and random embeddings](https://arxiv.org/abs/0910.1409) · [Approximating Sparsest Cut in Graphs of Bounded Treewidth](https://www.wisdom.weizmann.ac.il/~robi/papers/CKR-TreewidthSparsestCut-APPROX10.pdf) · [A face cover perspective to ℓ₁ embeddings of planar graphs](https://arxiv.org/abs/1903.02758) · [The exact value of c₁(K₂,ₙ)](https://arxiv.org/abs/2602.23745) · [CS 583: Approximation Algorithms](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6528 — Unknot recognition in polynomial time

Unknot recognition asks whether a closed loop represented by a finite crossing diagram can be deformed into a circle without cutting. A complicated drawing may still represent an unknot, so simplifying visible crossings is not a complete decision method. The target here is a deterministic algorithm whose bit complexity is polynomial in the diagram encoding. The saved card records a September 2026 preprint claiming such an algorithm, with its proof not independently validated. This description therefore preserves the uncertainty around that claim while explaining the computational target.

[Read in atlas](index.html#TCS-6528) · [The Computational Complexity of Knot and Link Problems](https://arxiv.org/abs/math/9807016) · [A polynomial upper bound on Reidemeister moves](https://annals.math.princeton.edu/2015/182-2/p03) · [The efficient certification of knottedness and Thurston norm](https://arxiv.org/abs/1604.00290) · [Unknot recognition in quasi-polynomial time](https://www.maths.ox.ac.uk/node/60914) · [A Practical Algorithm for Knot Factorisation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.55/LIPIcs.SoCG.2025.55.html) · [Incompressible surfaces, hierarchies and unknot recognition](https://arxiv.org/abs/2607.23350) · [Locally Minimal Bridge Presentations of Knots](https://arxiv.org/abs/2609.06492)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6573 — Polynomial Hirsch conjecture for edge-path diameter

The vertex-edge graph of a convex polyhedron records which feasible vertices can be joined by a single edge move. Its diameter is the largest shortest-path distance between any two vertices. The polynomial Hirsch conjecture asks for one polynomial bound in the number of facets and dimension that works uniformly for every pointed polyhedron. Counterexamples to the original linear Hirsch bound do not refute this weaker polynomial target. Resolving it would constrain the combinatorial geometry of linear programs, although short undirected paths would still not supply an efficient improving simplex rule.

[Read in atlas](index.html#TCS-6573) · [Geometry: Combinatorics and Algorithms 2025 — Chapter 10, Convex Polytopes](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf) · [A counterexample to the Hirsch Conjecture](https://annals.math.princeton.edu/2012/176-1/p07) · [An improved Kalai–Kleitman bound for the diameter of a polyhedron](https://arxiv.org/abs/1402.3579) · [An Asymptotically Improved Upper Bound on the Diameter of Polyhedra](https://link.springer.com/article/10.1007/s00454-018-0016-y) · [Computing the Polytope Diameter is Even Harder than NP-hard (Already for Perfect Matchings)](https://arxiv.org/abs/2502.16398v3) · [Circuit Diameter of Polyhedra is Strongly Polynomial](https://arxiv.org/abs/2602.06958v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0318 — How many k-element subsets can a line separate from a planar point set?

A k-set is a selection of k points that a line strictly separates from all remaining points of a planar configuration. The problem asks for the largest possible number of distinct k-sets among n points in general position. The desired estimate must remain sharp when k grows with n, including nearly balanced cuts. Duality turns this into a question about levels in arrangements of lines. Closing the gap between constructions and upper bounds would clarify the complexity of geometric selection and related optimization problems.

[Read in atlas](index.html#TCS-0318) · [The Open Problems Project: Problem 7, k-sets](https://topp.openproblem.net/p7) · [Improved Bounds for Planar k-Sets and Related Problems](https://courses.cs.duke.edu/cps234/fall08/handouts/dey.pdf) · [Point Sets with Many k-Sets](https://link.springer.com/article/10.1007/s004540010022) · [An Improved, Simple Construction of Many Halving Edges](https://rangevoting.org/many_halving_edges.pdf) · [An Improvement of the Upper Bound for the Number of Halving Lines of Planar Sets](https://oa.upm.es/89576/1/10302927.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6524 — Lang–Plaut problem

A doubling metric has uniformly limited local branching: each ball can be covered by a bounded number of smaller balls. The Lang–Plaut problem considers such a metric when it already sits inside a Hilbert space. It asks whether the points can be represented in some finite-dimensional Euclidean space while changing all distances by only a bounded factor. Both dimension and distortion should depend only on the doubling constant. The issue is whether intrinsic metric simplicity suffices to eliminate an infinite-dimensional ambient representation.

[Read in atlas](index.html#TCS-6524) · [Research reference · web.math.princeton.edu](https://web.math.princeton.edu/~naor/homepage%20files/assouad-N%28K%29.pdf) · [Research reference · www.its.caltech.edu](https://www.its.caltech.edu/~sryoo/teaching/Syllabus_Ma191a_2024F.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7242 — Is PL four-sphere recognition decidable?

The input is a finite triangulation promised to be a closed combinatorial four-dimensional manifold. The task is to recognize the standard piecewise-linear four-sphere. The question asks for a terminating decision algorithm, with no polynomial-time requirement. Recognizing a topological sphere or checking its homology would answer a different question. The problem marks the exceptional dimension between established decidability and undecidability results for sphere recognition.

[Read in atlas](index.html#TCS-7242) · [Frontiers of sphere recognition in practice](https://link.springer.com/article/10.1007/s41468-022-00092-8) · [Applied topology: sphere recognition research presentation](https://page.math.tu-berlin.de/~joswig/presentations/Joswig-Applied%2BTopology-250715.pdf) · [Is there an algorithm to recognize the combinatorial four-sphere?](https://www.openproblemgarden.org/op/is_there_an_algorithm_to_determine_if_a_triangulated_4_manifold_is_combinatorially_equivalent_to_the_4_sphere)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6526 — Optimal size of weak ε-nets for convex ranges

A weak ε-net places auxiliary points so that every convex set containing at least an ε fraction of a given point set contains an auxiliary point. The auxiliary points may lie anywhere in the ambient Euclidean space. For each fixed dimension, the task is to determine the smallest worst-case net size as ε decreases. The challenge comes from hitting all sufficiently populated convex regions simultaneously, regardless of the original configuration. Sharp bounds would quantify how economically a finite set can represent its large convex subsets.

[Read in atlas](index.html#TCS-6526) · [Research reference · arXiv 1808.02686](https://arxiv.org/abs/1808.02686)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0406 — Edge-Unfolding Convex Polyhedra

Take a convex polyhedron and cut selected edges while leaving its faces attached as one piece. The question is whether the resulting surface can always be flattened into a single polygon without overlapping interiors. Cuts through the middle of a face are disallowed, making the available choices depend on the polyhedron's edge structure. Convexity is central because the unrestricted nonconvex version has counterexamples. A solution would explain whether every convex solid has a conventional paper net using only its original faces.

[Read in atlas](index.html#TCS-0406) · [The Open Problems Project](https://topp.openproblem.net/p9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6527 — Constant-distortion Steiner point removal

Steiner point removal starts with a weighted graph and a designated set of terminals whose mutual distances matter. The goal is to delete the other vertices through graph-minor operations, leaving a graph on exactly those terminals. Its edges may be reweighted, but terminal distances should never shrink and should grow by at most a universal factor. The same guarantee must work regardless of how many terminals the input contains. This asks whether graph topology and useful terminal geometry can both survive an extreme reduction in representation size.

[Read in atlas](index.html#TCS-6527) · [Research reference · epubs.siam.org](https://epubs.siam.org/doi/10.1137/1.9781611977912.191)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6529 — Optimal ℓ₁ distortion of planar Earth Mover Distance

Earth Mover Distance measures the cheapest transportation of one probability distribution into another across a planar grid. The problem asks how well this entire metric can be embedded into ℓ₁ while preserving every pairwise distance. Its parameter is the side length of the grid, and the target is the optimal dependence of distortion on that size. A single coordinate representation must accommodate many different transportation patterns. Understanding this loss would clarify the limits of treating geometric transport as ordinary coordinatewise comparison or sketching.

[Read in atlas](index.html#TCS-6529) · [Research reference · www.weizmann.ac.il](https://www.weizmann.ac.il/math/gideon/sites/math.gideon/files/uploads/planar-earthmover.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7184 — The optimal complexity of Klee's measure problem in higher dimensions

Klee’s measure problem asks for the volume covered by a union of axis-aligned boxes. Overlapping regions count once, and only the exact total volume is required. For each fixed dimension at least three, the question seeks matching worst-case time bounds in a specified arithmetic real-RAM model. Chan’s general upper bound is O(n^(d/2)), with no matching unconditional classification supplied by the checked later work. Recent approximation and dynamic advances answer different questions.

[Read in atlas](index.html#TCS-7184) · [Klee's measure problem made easy](https://doi.org/10.1109/FOCS.2013.51) · [Approximating Klee’s Measure Problem and a Lower Bound for Union Volume Estimation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.25) · [Near-Optimal Dynamic Data Structures for Maximum Depth and Klee’s Measure of Boxes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.34)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7182 — The complexity of SEFE for two graphs

Two planar graphs share labeled vertices and possibly some edges. The question asks whether the existence of compatible planar drawings can be decided in polynomial time. Each shared vertex and edge must look identical in both drawings, while edges exclusive to different graphs may cross. The case with connected common graph is known to be efficiently solvable. The remaining target covers arbitrary common graphs and is distinct from straight-line or three-graph variants.

[Read in atlas](index.html#TCS-7182) · [Simultaneous Embedding of Planar Graphs](https://arxiv.org/abs/1204.5853) · [Constrained Planarity in Practice: Engineering the Synchronized Planarity Algorithm](https://doi.org/10.7155/jgaa.v29i1.2923) · [Structural Parameterizations of Simultaneous Planarity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2025.25) · [Simultaneous Embedding of Two Paths on the Grid](https://arxiv.org/abs/2603.09750v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0403 — Euclidean Minimum Spanning Tree

The Euclidean minimum spanning tree connects a collection of points with minimum total edge length and no cycles. The source asks for an exact algorithm close to the sorting-scale lower bound as the ambient dimension increases. Treating all point pairs as explicit graph edges loses the advantage of the geometric input representation. The algorithm must instead identify enough useful short connections without examining the complete graph. This is a basic test of how effectively geometry can accelerate a standard graph optimization problem.

[Read in atlas](index.html#TCS-0403) · [The Open Problems Project](https://topp.openproblem.net/p5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0408 — Minimum Euclidean Matching in 2D

Given an even number of planar points, a perfect matching pairs every point with exactly one other point. The Euclidean objective minimizes the sum of the lengths of all chosen segments. The question is the optimal complexity of computing that minimum exactly, with bipartite matching as a related restricted variant. Approximation algorithms can exploit geometry differently and do not by themselves settle the exact problem. Sharper algorithms would improve a central geometric pairing primitive whose implicit complete graph contains quadratically many candidate edges.

[Read in atlas](index.html#TCS-0408) · [The Open Problems Project](https://topp.openproblem.net/p6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0427 — NP certificates for homeomorphism of three-manifolds

Two triangulations can describe the same three-dimensional manifold while looking combinatorially unrelated. This question asks whether every homeomorphic pair has a certificate whose size and verification time are polynomial in the input. Such a certificate need not be found efficiently by the verifier itself. The challenge is to encode the necessary topological equivalence without an excessively long sequence of transformations. An NP upper bound would distinguish the difficulty of discovering a homeomorphism from the difficulty of checking convincing evidence that one exists.

[Read in atlas](index.html#TCS-0427) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7183 — Find a simple closed quasigeodesic in polynomial time

The goal is to find a simple closed route on a convex polyhedron that is straight after local unfolding except for allowed turns at vertices. At every visited vertex, at most π of surface angle may lie on either side of the route. Classical existence theorems and finite algorithms do not supply a polynomial-time construction in the full requested setting. Recent results distinguish numerical computation models and sometimes permit degenerate or weakly simple curves. The geometric target is explicit, while the exact numerical input and output conventions still need specification.

[Read in atlas](index.html#TCS-7183) · [Finding Weakly Simple Closed Quasigeodesics on Polyhedral Spheres](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2022.27) · [Finding Closed Quasigeodesics on Convex Polyhedra](https://arxiv.org/abs/2008.00589v3) · [Quasigeodesics on the Cube](https://cccg-wads-2025.eecs.yorku.ca/cccg-papers/32.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7189 — Is minimum-weight triangulation in NP?

The input gives rational planar points and a rational limit on the total length of a triangulation. Every input point must be used, no extra points may be added, and Euclidean edge lengths are compared exactly. The question asks whether every feasible instance has a short certificate that can be checked in polynomial bit time. NP-hardness is known, but the sum of potentially irrational edge lengths prevents the usual edge-list argument from establishing NP membership. Practical exact solutions and rounded-cost variants do not settle the certificate question for arbitrary exact inputs.

[Read in atlas](index.html#TCS-7189) · [Minimum-weight triangulation is NP-hard](https://arxiv.org/abs/cs/0601002) · [Solving Large-Scale Minimum-Weight Triangulation Instances to Provable Optimality](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.44) · [Taming Infinity One Chunk at a Time: Concisely Represented Strategies in One-Counter MDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.138)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0410 — Output-sensitive Convex Hull in \R^d

An output-sensitive convex hull algorithm charges for both its input points and the facets it actually produces. The question asks for the best such running time for point sets in fixed-dimensional Euclidean space. Small hulls should be cheaper than the worst-case hull complexity would suggest. The difficult target is to reconcile reading the input, identifying extreme structure, and listing the output with nearly optimal overhead. Progress would improve geometric optimization whenever many input points contribute little to the final convex boundary.

[Read in atlas](index.html#TCS-0410) · [The Open Problems Project](https://topp.openproblem.net/p15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0973 — Sketching Earth Mover Distance

A sketch compresses each planar point set independently into a short randomized bit string. Given sketches of two equal-size sets, the decoder should estimate their minimum-cost transportation matching. The source asks for the tradeoff between sketch length and multiplicative approximation, highlighting constant approximation with polylogarithmic length. Success is required with a fixed constant probability for every pair of inputs. Unlike computing one matching from full data, the same compressed representation must remain useful against a subsequently chosen comparison set.

[Read in atlas](index.html#TCS-0973) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:49)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0417 — Voronoi Diagram of Lines in 3D

The Voronoi diagram of lines in three dimensions partitions space according to which input line is nearest. The problem asks for its worst-case combinatorial size under Euclidean distance, with line segments as a related version. The source conjectures growth close to quadratic in the number of objects. A bound for one distance level, such as a union of equal-radius cylinders, does not control the entire diagram automatically. Resolving the complexity would sharpen a basic proximity structure for extended objects in space.

[Read in atlas](index.html#TCS-0417) · [The Open Problems Project](https://topp.openproblem.net/p3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0419 — coNP certificates for three-manifold homeomorphism

The homeomorphism problem asks whether two triangulated three-manifolds represent the same topological space. Here the target is a short, efficiently checkable certificate when the answer is no. Proving membership in coNP requires such evidence for every nonhomeomorphic pair, not just pairs distinguished by a convenient invariant. The source relates the difficulty to graph isomorphism through a reduction into manifold homeomorphism. The project seeks a systematic way to certify topological difference even when the triangulations hide the relevant obstruction.

[Read in atlas](index.html#TCS-0419) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0411 — Point Location in 3D Subdivision

A three-dimensional subdivision divides space into cells bounded by faces. After preprocessing it, a point-location query asks which cell contains a supplied point. The source targets a data structure using linear space and answering queries in logarithmic time, measured against the number of faces. Both requirements must hold together across arbitrary inputs in the stated setting. This would make geometric navigation through a spatial partition as economical as familiar search structures despite the much richer adjacency and boundary geometry.

[Read in atlas](index.html#TCS-0411) · [The Open Problems Project](https://topp.openproblem.net/p13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0430 — NP-hardness of three-manifold homeomorphism

Deciding whether two triangulated three-manifolds are homeomorphic has algorithms, but decidability alone says little about feasible running time. This question seeks an NP-hardness lower bound for the general decision problem. A reduction would have to encode arbitrary instances of a known hard problem into pairs of manifolds. Hardness of related knot or triangulation optimization tasks does not immediately supply that encoding. Such a result would locate manifold equivalence more precisely among familiar computational problems and constrain expectations for general-purpose recognition algorithms.

[Read in atlas](index.html#TCS-0430) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0416 — Visibility Graph Recognition

A polygon's visibility graph records which pairs of vertices can be joined by a segment lying inside the polygon. The source supplies both a candidate graph and a Hamiltonian cycle specifying the intended polygon boundary. It asks for an efficient decision procedure for whether a simple polygon realizes exactly that information. Choosing coordinates must satisfy visibility and obstruction requirements simultaneously. The problem tests whether a combinatorial record of sight lines contains enough accessible structure to reconstruct a genuine geometric environment.

[Read in atlas](index.html#TCS-0416) · [The Open Problems Project](https://topp.openproblem.net/p17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0990 — Estimating Earth-Mover Distance

A stream presents red and blue points on a planar grid, with equally many points of each color. Their Earth Mover Distance is the minimum total cost of matching each red point to a blue point. The source asks which approximation guarantees are possible when the stream can be retained only through a small memory state. A central target is constant-factor approximation with space polynomial in the logarithms of the input and grid sizes. Transportation structure must be captured without storing all points or the matching itself.

[Read in atlas](index.html#TCS-0990) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0377 — Smallest Universal Set of Points for Planar Graphs

A universal point set must support a crossing-free straight-line drawing of every planar graph with n vertices. For each graph, its vertices may use a different subset of the same fixed points. The question asks how small this common geometric host can be, especially whether a linear number of points suffices. Rectangular grid drawings give a useful construction but impose additional structure on the host. The target measures how much geometric freedom is needed to realize all planar combinatorial structures of one size.

[Read in atlas](index.html#TCS-0377) · [The Open Problems Project](https://topp.openproblem.net/p45)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0423 — Efficient algorithms for multiparameter persistence

Computing two-parameter persistence can require changing basis in matrices whose rows carry pairs of filtration labels. The cited construction minimizes the resulting column labels but can turn a few sparse columns into very dense ones. The source asks for an algorithm that avoids this fill-in in typical instances while retaining the required algebraic outcome. A small number of dense columns can dominate memory and computation across millions of columns. The concrete project is therefore sparse matrix control inside persistence computation, rather than an unspecified faster topology algorithm.

[Read in atlas](index.html#TCS-0423) · [Applied and Combinatorial Topology](https://doi.org/10.4230/DagRep.14.2.206)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0326 — Similarity of Curves (Fréchet Distance)

Fréchet distance compares curves while respecting the order in which their points are traversed. This source focuses on data structures that compare a short query curve with stored curves efficiently. It asks whether constant-factor approximation can avoid space exponential in the query's number of vertices. Near-exact approximation and continuous versus discrete traversal impose additional tradeoffs. The project is to make repeated curve comparison economical without discarding the sequential shape information that distinguishes Fréchet distance from an unordered point-set metric.

[Read in atlas](index.html#TCS-0326) · [Metric Sketching and Dynamic Algorithms for Geometric and Topological Graphs](https://doi.org/10.4230/DagRep.15.5.134)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0412 — Polygonal Curve Simplification

Curve simplification replaces a polygonal chain by a shorter chain chosen from its original vertices. The objective in this source is to use as few retained vertices as possible while meeting a prescribed approximation error. The algorithmic question is whether an optimum can be found in nearly linear time. The answer depends on the precise geometric error criterion and cannot be inferred from a fast heuristic alone. Efficient exact simplification would compress trajectory or shape data while making its quality and representation size explicitly accountable.

[Read in atlas](index.html#TCS-0412) · [The Open Problems Project](https://topp.openproblem.net/p24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0432 — Polynomial flip-distance bounds for three-manifold triangulations

Triangulations of the same compact three-manifold are connected by local bistellar flips. The question asks whether two triangulations can always be connected using polynomially many such moves in their input sizes. The polynomial is initially allowed to depend on the fixed manifold. A path may temporarily use different numbers of tetrahedra, so connectivity alone provides no useful quantitative bound. The result would control the amount of local rewriting needed to pass between alternative finite descriptions of one topological space.

[Read in atlas](index.html#TCS-0432) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2529 — First, is there an exact polynomial time algorithm for embedding into ultrametrics or even a PTAS?

A probabilistic ultrametric embedding represents a metric by a distribution over hierarchical distance structures. The optimization objective controls expected distortion for every original pair of points. The cited work gives a constant-factor approximation to the best distortion achievable on the particular input. Its question is whether that instance-dependent optimum can instead be computed exactly or approximated arbitrarily closely in polynomial time. Improving this optimization would choose hierarchical representations more effectively when a metric is easier than worst-case embedding bounds suggest.

[Read in atlas](index.html#TCS-2529) · [Probabilistic Metric Embedding via Metric Labeling](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0414 — Surface Reconstruction

Surface reconstruction begins with points sampled from an unknown surface and seeks a finite surface representation with the same topology. The source distinguishes established smooth-surface guarantees from the difficulty of sharp edges and corners. Those singular features can confuse local geometric estimates that work well in smooth regions. The project asks for a reconstruction guarantee under a suitable density promise that accommodates such features. A successful method would recover connectivity and holes reliably instead of producing only a visually close collection of patches.

[Read in atlas](index.html#TCS-0414) · [The Open Problems Project](https://topp.openproblem.net/p26)
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

### TCS-0328 — Sparse (1 + ϵ)-emulator for Euclidean Point Sets

A near-isometric emulator is a weighted graph whose shortest paths approximate distances among Euclidean input points. Unlike a geometric Steiner spanner, its extra vertices need not themselves have Euclidean locations. The source asks how many edges are necessary when this greater freedom is allowed. Even points placed along two opposite sides of a square provide a concrete test instance. The question probes whether abstract auxiliary states can represent Euclidean distances more sparsely than any network constrained to live in the original geometric space.

[Read in atlas](index.html#TCS-0328) · [Metric Sketching and Dynamic Algorithms for Geometric and Topological Graphs](https://doi.org/10.4230/DagRep.15.5.134)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0340 — Average Distortion Embeddings

An average-distortion embedding controls aggregate squared distances while remaining nonexpansive for every pair. The source considers the square-root metric associated with a finite-dimensional normed space. An existence theorem supplies a Hilbert-space embedding with favorable dependence on dimension, but its duality proof does not provide an explicit map. The task is to construct and evaluate an embedding efficiently from the supplied point set. This would turn a structural geometric theorem into an algorithmic primitive for proximity search and related computations.

[Read in atlas](index.html#TCS-0340) · [Computational Geometry](https://doi.org/10.4230/DagRep.11.4.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0965 — Low Expansion Encoding of Edit Distance

The problem seeks an injective encoding of binary strings of length at most n into polynomial-length bit strings. A single insertion, deletion, or substitution in the original string should alter only o(log n) encoded bits. This is a low-expansion requirement from edit distance to Hamming distance, without asking for a full constant-distortion embedding. Randomized encodings are allowed if distinct strings remain distinct with high probability. An efficient encoding and decoder would make string representations much more stable under edits that ordinarily shift every later character position.

[Read in atlas](index.html#TCS-0965) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:59)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0970 — Fast JL Transform for Sparse Vectors

A Johnson-Lindenstrauss transform maps a vector into fewer dimensions while approximately preserving its Euclidean length with high probability. The target dimension is O(log(1/P) divided by epsilon squared) for failure probability P and error epsilon. The source asks for applying the transform to an s-sparse input in time roughly s plus the output dimension, up to polylogarithmic factors. It also asks for an explicit distribution generated from only O(log(d/P)) random bits. The project combines fast multiplication, optimal dimensional reduction, and a compact random seed rather than optimizing any one resource alone.

[Read in atlas](index.html#TCS-0970) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0363 — Negative cycles on surface embedded graphs

Consider a directed graph drawn on a surface whose edges may have negative weights. The task is to decide whether there is a negative-total-weight closed walk that can be contracted to a point on that surface. Walks may revisit edges and vertices, so a witness need not resemble an ordinary simple cycle. The source asks both for algorithms and for a complexity classification, including whether short certificates always suffice. The challenge is to combine weight optimization with a global topological constraint on the whole walk.

[Read in atlas](index.html#TCS-0363) · [Computational Geometry](https://doi.org/10.4230/DagRep.7.4.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0331 — Treewidth of 3-Manifolds

The treewidth of a three-manifold minimizes dual-graph treewidth over all its triangulations. This differs from computing treewidth for one triangulation already supplied as input. The source asks for the complexity of finding this manifold invariant and even its exact value on the three-torus. Bounded treewidth supports efficient algorithms for several otherwise difficult topological tasks. Understanding the minimum would reveal whether poor algorithmic behavior belongs to the manifold itself or merely to an unfortunate choice of finite representation.

[Read in atlas](index.html#TCS-0331) · [Computational Geometry](https://doi.org/10.4230/DagRep.15.5.64)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0398 — Planar Euclidean Maximum TSP

The maximum Euclidean traveling-salesman problem seeks the longest tour through a planar point set. Every point must be visited once before the tour closes, but long connections are rewarded rather than penalized. The source asks for the complexity of finding the exact optimum in the plane. Algorithms for polyhedral distance functions and hardness in higher-dimensional Euclidean space do not determine this intermediate case. The problem tests how the geometry of the distance function affects a familiar combinatorial optimization task.

[Read in atlas](index.html#TCS-0398) · [The Open Problems Project](https://topp.openproblem.net/p49)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4194 — More generally, does an approximate Voronoi diagram of size O(nk+1 ) exist for a set of k-dimensional flats in Rd , for d > k?

An approximate Voronoi diagram partitions query space into regions associated with approximately nearest input objects. The objects here are k-dimensional affine flats in a fixed higher-dimensional Euclidean space. The question asks whether the diagram can have size on the scale of n raised to the power k+1. A nearest-neighbor data structure with comparable storage need not explicitly produce such a geometric partition. The task distinguishes economical query answering from an equally economical global description of all approximate answers.

[Read in atlas](index.html#TCS-4194) · [Approximate Nearest Neighbor Search Amid Higher-Dimensional Flats](https://doi.org/10.4230/LIPIcs.ESA.2017.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0327 — Simple Polygonalizations

A simple polygonalization orders a given planar point set around a polygon without crossing its edges. The source asks whether the total number of such polygons can be computed in polynomial time. Finding one polygon is much easier than accounting for every valid cyclic ordering. The counting question is also related to generating a uniformly random polygon on the same vertices. A sharp algorithmic classification would clarify whether geometric noncrossing structure can overcome the large combinatorial space of candidate tours.

[Read in atlas](index.html#TCS-0327) · [The Open Problems Project](https://topp.openproblem.net/p16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0409 — Minimum-Link Path in 2D

A minimum-link path connects two locations among polygonal obstacles while using as few straight segments as possible. Its objective counts bends and segments rather than total Euclidean length. The source asks whether the planar problem admits a subquadratic algorithm. A short-distance path need not minimize links, so standard shortest-path techniques do not automatically achieve the target. The task would improve route simplification in environments where changing direction is costly even when travel along a straight segment is inexpensive.

[Read in atlas](index.html#TCS-0409) · [The Open Problems Project](https://topp.openproblem.net/p22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1356 — Diameter-∆ of the intersection graph of low-complexity geometric objects (regardless of the dimension) can be solved in truly-subquadratic time if the VC dimension of ∆-neighborhoods […]

Graph diameter becomes expensive when a geometric intersection graph has many implicit edges. This conjecture proposes bounded VC dimension of the relevant distance neighborhoods as a sufficient structural condition for truly subquadratic diameter-threshold algorithms. The geometric objects should have low descriptive complexity, but their ambient dimension need not be two. The source's examples suggest a common explanation for several otherwise separate algorithmic successes. The task is to turn that observed relationship between set-system structure and distance computation into a general theorem.

[Read in atlas](index.html#TCS-1356) · [Charting the Diameter Computation Landscape of Intersection Graphs in 3D and Above](https://doi.org/10.4230/LIPIcs.SoCG.2026.29)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1762 — We conjecture that tight instances exist in these spaces, i.e., the spanner bounds obtained in [25, 22] are optimal for every stretch t.

A geometric spanner preserves distances in a normed space using fewer edges than the complete graph. For ℓₚ spaces with p between one and two, the source conjectures that existing sparsity guarantees are optimal at every stretch level. Proving this requires point configurations forcing matching lower bounds for unrestricted-hop spanners. Bounds for two-hop routes or for norms whose parameter grows with input size do not settle the fixed-norm target. The question would identify the true compression limits of these high-dimensional geometric metrics.

[Read in atlas](index.html#TCS-1762) · [Lipschitz Decompositions of Finite 𝓁_{p} Metrics](https://doi.org/10.4230/LIPIcs.SoCG.2025.66)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2356 — What is the complexity of computing the treewidth of a 3-manifold?

A triangulated three-manifold has a dual graph whose treewidth controls many dynamic-programming algorithms. The treewidth of the manifold minimizes this graph parameter over all its triangulations. The question asks for the computational complexity of determining that minimum. Topological decompositions can force every triangulation to remain complicated, providing lower-bound intuition. The project distinguishes optimizing one supplied combinatorial representation from finding the simplest possible representation of the underlying topological space.

[Read in atlas](index.html#TCS-2356) · [On the Width of Complicated JSJ Decompositions](https://doi.org/10.4230/LIPIcs.SoCG.2023.42)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3059 — We leave as a major open question to find new algorithms for LLARP that might tackle the 50% conjecture.

Place points in a unit square, including its lower-left corner. Each point may anchor the lower-left corner of an axis-aligned rectangle contained in the square, and the rectangles must not overlap. The conjecture asks whether rectangles can always cover at least half the square. The cited paper shows a limitation of a particular greedy packing approach and calls for different algorithms. The remaining challenge is to coordinate anchored rectangle choices globally so that wasted area never exceeds the proposed universal threshold.

[Read in atlas](index.html#TCS-3059) · [On Greedily Packing Anchored Rectangles](https://doi.org/10.4230/LIPIcs.ICALP.2021.61)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4061 — Does UGC imply that for all c > 1, it is hard to c-approximate 1-Homology Localization on triangulations of 2-manifolds (over Zk for k = […]

One-dimensional homology localization seeks a smallest representative of a prescribed homology class on a triangulated surface. The source asks whether the Unique Games Conjecture implies hardness of approximation within every constant factor greater than one. The coefficient group may grow with the requested hardness factor. Existing reductions lose too much of their approximation gap to establish this target directly. The problem would connect an influential conjecture about constraint satisfaction with the limits of simplifying topological cycles on two-dimensional manifolds.

[Read in atlas](index.html#TCS-4061) · [Computational Topology and the Unique Games Conjecture](https://doi.org/10.4230/LIPIcs.SoCG.2018.43)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4236 — Is there an algorithm to construct or detect combinatorial immersions that have a realization in the configuration of geodesics for some hyperbolic metric?

A combinatorial immersion records how curves run across a surface and intersect. The source asks whether one can recognize or construct those configurations realizable by geodesics for some hyperbolic metric. A general Riemannian metric can realize more minimal-crossing configurations than a hyperbolic one. Consequently, minimizing crossings within a homotopy class does not settle the target. The question seeks an algorithmic description of the extra geometric restrictions imposed when the surface metric must have constant negative curvature.

[Read in atlas](index.html#TCS-4236) · [Computing the Geometric Intersection Number of Curves](https://doi.org/10.4230/LIPIcs.SoCG.2017.35)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4269 — What is the complexity of the following flip distance problem for labelled triangulations: Given two labelled triangulations and a number k, is there a flip […]

In a labelled triangulation, every edge has an identity that transfers to the new diagonal when an edge is flipped. The question asks whether one labelled triangulation can reach another in at most a given number of flips. Knowing which initial edge must become which final edge changes the problem from ordinary unlabelled flip distance. A criterion for eventual reachability does not determine the shortest transformation. The task measures the complexity of reconfiguring geometric structure while faithfully transporting identities through local moves.

[Read in atlas](index.html#TCS-4269) · [A Proof of the Orbit Conjecture for Flipping Edge-Labelled Triangulations](https://doi.org/10.4230/LIPIcs.SoCG.2017.49)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4353 — It is an open problem to decide efficiently whether a drawing of a graph H is weakly simple, i.e., whether a drawing P of H […]

A graph drawing may contain overlaps or degeneracies while remaining arbitrarily close to a genuine embedding. The source calls such a drawing weakly simple and asks for an efficient recognition algorithm. Closeness is measured by a Fréchet-style correspondence respecting the drawn graph. Algorithms for a single polygonal cycle do not automatically handle branching vertices and their incidence constraints. The project determines whether all apparent crossings can be removed by arbitrarily small perturbations that preserve the intended graph structure.

[Read in atlas](index.html#TCS-4353) · [Recognizing Weakly Simple Polygons](https://doi.org/10.4230/LIPIcs.SoCG.2016.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4427 — Can it be decided efficiently if a polyomino has a k-isohedral tiling?

An isohedral tiling has symmetries that map any tile copy to any other. The k-isohedral generalization allows several symmetry orbits among copies of the same polyomino. The source asks how efficiently one can decide whether a given polyomino admits such a tiling. It highlights fixed-parameter tractability in the orbit count as a possible stronger target. The problem asks for a finite algorithmic handle on an infinite periodic-looking arrangement whose copies need not all play the same geometric role.

[Read in atlas](index.html#TCS-4427) · [A Quasilinear-Time Algorithm for Tiling the Plane Isohedrally with a Polyomino](https://doi.org/10.4230/LIPIcs.SoCG.2016.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4454 — Specifically, we conjecture that there exist Dp ∈ [1, ∞) such that for every finite metric space (X, dX ) we have p cPp (R3 […]

Wasserstein spaces measure distances between probability distributions by the cost of transporting mass in Euclidean space. For each fixed p greater than two, the source conjectures that the square-root metric of every finite metric space embeds into Wp over three-dimensional Euclidean space with distortion bounded only by p. Its results establish the corresponding universality at p = 2 but leave room for improvement for larger p. An embedding of W₂ itself into Wp would provide one route to the proposed conclusion. The conjecture would strengthen the geometric obstructions explaining why compact sketches and simple normed-space representations of transportation distances are difficult.

[Read in atlas](index.html#TCS-4454) · [Impossibility of Sketching of the 3D Transportation Metric with Quadratic Cost](https://doi.org/10.4230/LIPIcs.ICALP.2016.83)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4505 — We leave open the question whether any two straight-line drawings of the same plane graph G can be morphed so that every intermediate drawing has […]

A planar morph continuously transforms one straight-line drawing into another while keeping the same embedding. The source gives efficient morphs preserving convexity under its drawing assumptions. This question asks whether intermediate drawings can also maintain polynomially controlled geometric size. A short sequence of motion steps can still create extremely tiny edges or enormous scale differences. The project must control numerical geometry throughout the transformation, making the resulting animations both structurally valid and representable with reasonable precision.

[Read in atlas](index.html#TCS-4505) · [Optimal Morphs of Convex Drawings](https://doi.org/10.4230/LIPIcs.SOCG.2015.126)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4549 — Can a perfect colorful choice be computed in polynomial time if we have poly(d) color classes?

The input consists of colored point sets in dimension d, with the origin in the convex hull of every color class. A perfect colorful choice selects at most one point of each color while still containing the origin in its convex hull. The source asks whether polynomially many color classes in d suffice to find such a choice in polynomial time. This trades additional colors for computational tractability while preserving the exact one-point-per-color requirement. It would clarify whether redundant geometric choices can remove the computational difficulty behind the colorful Carathéodory theorem.

[Read in atlas](index.html#TCS-4549) · [Computational Aspects of the Colorful Carathéodory Theorem](https://doi.org/10.4230/LIPIcs.SOCG.2015.44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5133 — Strong Hanani-Tutte for the Torus — Conjecture 18

Consider a graph drawn on a surface so that edges with no common endpoint never cross. Edges meeting at a vertex may still cross elsewhere in the drawing. The conjecture asks whether the existence of such a drawing guarantees an embedding without any crossings on the same surface. The source distinguishes this condition from requiring independent edges to cross an even number of times, whose surface behavior is different. A resolution would explain whether adjacent-edge crossings alone can ever conceal a genuine obstruction to embedding.

[Read in atlas](index.html#TCS-5133) · [Strong Hanani-Tutte for the Torus](https://doi.org/10.4230/LIPIcs.SoCG.2021.38)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5875 — Between Shapes, Using the Hausdorff Distance — Explicit open question on PDF page 2

The Hausdorff distance compares two sets by taking the worst nearest-neighbor distance in both directions. The extracted question asks for the complexity of computing this distance when both inputs are general semialgebraic sets, described by polynomial conditions. Algorithms for finite point sets or polygonal objects do not settle that broader representation model. The surrounding paper studies intermediate shapes and cites polynomial-time computation for general semialgebraic inputs as an unresolved background issue. A precise solution would need to specify the dimension, algebraic input encoding, and output representation as well as control the running time.

[Read in atlas](index.html#TCS-5875) · [Between Shapes, Using the Hausdorff Distance](https://doi.org/10.4230/LIPIcs.ISAAC.2020.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6199 — Parametrized Complexity of Expansion Height — Explicit open question on PDF page 4

Simple-homotopy equivalence transforms simplicial complexes through elementary expansions and collapses. The source discusses low-dimensional complexes, where bounds on intermediate dimension and the ability to decide equivalence become delicate. Its extracted question concerns decidability in the setting related to triviality of balanced group presentations. Nearby existence statements for contractible complexes do not by themselves provide a decision procedure for recognizing the relevant inputs. Clarifying this distinction is essential before turning the passage into a precise computational problem with explicit promises on the complexes and permitted intermediate dimensions.

[Read in atlas](index.html#TCS-6199) · [Parametrized Complexity of Expansion Height](https://doi.org/10.4230/LIPIcs.ESA.2019.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6286 — Kernelization for H-Coloring — Explicit open question on PDF page 5

H-Coloring asks for an adjacency-preserving map from an input graph into a fixed target H. The cited work studies how such instances can be compressed through kernelization. The saved passage discusses faithful orthogonal representations of H, linking graph adjacency to vector geometry. That connection may provide a structural tool for preprocessing or for identifying the limits of compression. The extraction stops inside a recalled theorem and does not contain its unresolved continuation, so it cannot support a specific new representation dimension or kernel-size conjecture.

[Read in atlas](index.html#TCS-6286) · [Kernelization for H-Coloring](https://doi.org/10.4230/LIPIcs.IPEC.2025.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6880 — Approximate the cut cone within constant distortion using a cone with efficient separation.

The cut cone consists of nonnegative combinations of cut metrics and provides a geometric formulation of several graph-cut optimization problems. Direct membership testing is difficult, so the source asks for a tractable approximating cone. The preferred guarantee is constant distortion together with membership and separation algorithms polynomial in the dimension. A separation algorithm must either recognize membership or produce a hyperplane certifying exclusion. Such a cone could support efficient convex optimization for cut problems, while the source explicitly notes that its proposed negative-type-metric candidate does not achieve the desired constant-distortion guarantee.

[Read in atlas](index.html#TCS-6880) · [Expander Graphs and Their Applications](https://www.math.ias.edu/avi/node/974)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7006 — Achieve optimal subspace-embedding dimension with the conjectured input-sparsity running time and failure dependence.

A subspace embedding compresses a matrix while approximately preserving the Euclidean norm of every vector in its column space. The source conjectures an embedding dimension proportional to dimension plus logarithmic inverse failure probability, divided by accuracy squared. At the same time, multiplying by the embedding should take input-sparsity time with only the specified logarithmic and inverse-accuracy overhead. The two requirements must hold together, since a small sketch can still be expensive to construct. Such a construction would improve the foundational compression step used by fast regression and other numerical linear-algebra algorithms.

[Read in atlas](index.html#TCS-7006) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1679 — Does every point set admit an oriented t-spanner with t < 2?

An oriented spanner assigns at most one direction to each connection between two points. Its dilation compares the shortest directed round trip through each pair with the perimeter of that pair’s cheapest triangle. The historical question asks for one factor strictly below two that works for every point set. The published ESA 2026 theorem answers positively with factor five thirds, even in general finite metric spaces. Finding an orientation with the smallest possible dilation for a particular point set remains a separate question.

[Read in atlas](index.html#TCS-1679) · [Computing Oriented Spanners and Their Dilation](https://doi.org/10.4230/LIPIcs.SoCG.2025.27) · [Sparse Oriented Spanners in Metric Spaces](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.117)
Existing status: `resolved` · Summary written: 2026-09-11

## Learning theory (67)

### TCS-6541 — Does every VC class admit linear-size sample compression?

Sample compression represents a labeled training set by retaining only a few examples and a bounded amount of extra information. A fixed reconstruction rule must recover a hypothesis agreeing with every original training label whenever the sample is realizable. This project asks whether every binary class of VC dimension d admits a scheme whose total charged size is proportional to d. The question concerns the number of retained examples and side-information bits, not the ordinary bit length of the examples themselves. A linear bound would connect the statistical capacity measured by VC dimension with a comparably small combinatorial explanation of every realizable sample.

[Read in atlas](index.html#TCS-6541) · [Sample compression schemes for VC classes](https://arxiv.org/abs/1503.06960v2) · [Dual VC Dimension Obstructs Sample Compression by Embeddings](https://proceedings.mlr.press/v247/chase24a.html) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html) · [Sample compression schemes for balls in structurally sparse graphs](https://arxiv.org/abs/2604.02949v1) · [The No-Clash Teaching Dimension is Bounded by VC Dimension (withdrawn)](https://arxiv.org/abs/2603.23561v4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6542 — Polynomial-time learning parity with constant random noise

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

### TCS-6544 — Distribution-free learning of intersections of two halfspaces

The intersection of two halfspaces labels a point positively only when it satisfies both linear inequalities. This project asks for efficient distribution-independent learning when examples have a positive margin from the separating boundaries. The learner may output a different kind of hypothesis, but its time must remain polynomial in dimension, inverse margin, and inverse error. The cited source achieves a polynomial-time result under a factorization assumption on the input distribution and leaves removal of that assumption as the broader challenge. Resolving it would determine whether two simple linear rules can be learned efficiently without requiring favorable structure in how examples are distributed.

[Read in atlas](index.html#TCS-6544) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0677 — Properly learning decision trees in polynomial time?

Proper learning of decision trees requires the learner to output a decision tree, preserving the target representation's simple branching structure. The source asks for a polynomial-time algorithm under the uniform input distribution with membership queries available. Those queries let the learner choose inputs and observe their target labels, making this different from learning from random examples alone. Existing algorithms in the source are faster than earlier quasipolynomial approaches but still fall short of polynomial time. A solution would provide an efficient way to recover an interpretable tree hypothesis without abandoning the tree representation during learning.

[Read in atlas](index.html#TCS-0677) · [Open Problem: Properly learning decision trees in polynomial time?](https://proceedings.mlr.press/v178/open-problem-blanc22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0691 — Recursive Teaching Dimension Versus VC Dimension

Teaching dimension measures how many carefully selected labeled examples are needed to identify a target concept. Recursive teaching allows the class to be peeled apart through successive teaching stages, producing a more flexible complexity measure. The selected question asks whether this recursive teaching dimension is bounded by a universal linear function of VC dimension for finite concept classes. VC dimension instead governs learning from random examples, so the comparison connects two different ways information reaches a learner. A bound or a counterexample would clarify the relation between teaching and passive learning and has consequences for sample-compression questions.

[Read in atlas](index.html#TCS-0691) · [COLT / PMLR](https://proceedings.mlr.press/v40/Simon15b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0694 — The Statistical Query Complexity of Learning Sparse Halfspaces

An r-sparse halfspace uses at most r of the n Boolean input coordinates. Statistical-query learning accesses approximate expectations instead of individual labeled examples. The source asks whether the worst-case number of nearly uncorrelated sparse halfspaces stays polynomial in n when correlation is inverse-polynomial in r log n. Both the sparsity dependence and the worst-case distribution are essential to the question. A resolution would clarify the informational limits of exploiting sparse structure through statistical queries.

[Read in atlas](index.html#TCS-0694) · [Open Problem: The Statistical Query Complexity of Learning Sparse Halfspaces](https://proceedings.mlr.press/v35/feldman14c.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0683 — Improper learning of mixtures of Gaussians

Mixtures of Gaussians are standard models for data containing several latent clusters. The selected question asks for efficient improper learning in an overcomplete setting, where the number of mixture components exceeds the ambient dimension. The source uses a compression-and-reconstruction notion of unsupervised learning rather than requiring recovery of the original Gaussian parameters. This flexibility matters because hardness of identifying the exact mixture does not automatically rule out a useful alternative representation. A construction would extend the paper's undercomplete approach and show whether low-reconstruction-error learning remains feasible despite the abundance of latent components.

[Read in atlas](index.html#TCS-0683) · [COLT / PMLR](https://proceedings.mlr.press/v75/hazan18a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0670 — Can Local Regularization Learn All Multiclass Problems?

A local regularizer fixes a score for every hypothesis and test point before seeing the training sample. At prediction time it selects among the lowest-scored hypotheses consistent with the sample. The question asks whether every realizably PAC-learnable multiclass class admits such a rule that succeeds under every tie-breaking choice. Two preprints from July and August 2026 claim counterexamples under this definition. Their statements match the main question, while independent verification of the claimed negative resolution remains outstanding.

[Read in atlas](index.html#TCS-0670) · [Open Problem: Can Local Regularization Learn All Multiclass Problems?](https://proceedings.mlr.press/v247/asilis24b.html) · [Local Regularization Does Not Characterize Multiclass PAC Learnability](https://arxiv.org/abs/2607.23449) · [Algorithmic Principles For Multiclass Learning Are Hard To Come By: Limits of Regularization and Proper Learning](https://arxiv.org/abs/2608.26516)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0671 — Direct Sums in Learning Theory

Direct-sum questions study how learning resources change when several tasks are combined into a product class. This source asks how learning curves, uniform-convergence rates, and related complexity parameters scale relative to their single-task versions. For some realizable settings, learning components separately gives a simple additive error bound, but it is unclear when joint learning can improve it. Excess-risk and uniform-convergence quantities need separate analysis because their differences do not inherit the same elementary bound. Sharp product rules would explain when solving several learning problems together provides a statistical advantage over treating them independently.

[Read in atlas](index.html#TCS-0671) · [COLT / PMLR](https://proceedings.mlr.press/v247/hanneke24c.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0664 — Is the Power of Deep Learning over Linear Models Inherently Distribution Dependent?

Neural networks can outperform linear predictors in some learning settings, but that advantage may depend on favorable input distributions. The selected problem asks whether distribution-independent statistical-query learning forces a class to have a low-dimensional linear representation. A related formulation asks whether learnability by gradient methods on suitable neural networks under every input distribution also implies learnability by a linear model. Sample-efficient learning alone does not guarantee such a representation, so computational restrictions and distributional quantifiers are central. Resolving the question would clarify whether broadly distribution-independent deep-learning advantages can survive outside the expressive reach of linear or kernel methods.

[Read in atlas](index.html#TCS-0664) · [COLT / PMLR](https://proceedings.mlr.press/v336/feldman26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0682 — Monotonicity of Learning

It is natural to expect that giving a learner one more training example should improve its predictions. This project asks when expected performance actually changes monotonically with sample size. The source focuses on empirical risk minimization and gives examples where monotonicity holds as well as examples where it fails. Asymptotic consistency or a decreasing upper bound on risk does not guarantee improvement at every finite sample size. Characterizing the learners and problems that do have this property would explain when the everyday intuition that more data helps is mathematically justified.

[Read in atlas](index.html#TCS-0682) · [COLT / PMLR](https://proceedings.mlr.press/v99/viering19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0663 — Is Interaction Necessary for Order-Optimal 1-bit Mean Estimation?

One-bit mean estimation restricts each observed sample to a single communicated bit before the estimator sees it. This project asks whether nonadaptive quantizers can achieve the optimal estimation rate for the source's finite-moment distribution classes. Adaptive protocols can attain that rate, and the source explains that one adaptive transition already suffices with general queries. Lower bounds for fixed threshold or interval queries do not cover every possible nonadaptive one-bit quantizer. Resolving the general case would determine whether interaction is inherently necessary for optimal estimation or only compensates for overly restricted message designs.

[Read in atlas](index.html#TCS-0663) · [COLT / PMLR](https://proceedings.mlr.press/v336/lau26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0668 — Optimal Instance-Dependent Sample Complexity for finding Nash Equilibrium in Two Player Zero-Sum Matrix games

A zero-sum matrix game models two players whose gains and losses are directly opposed. Here the payoff matrix is unknown and can only be explored through noisy observations of its entries. The selected question asks for the optimal sample complexity of finding an approximate Nash equilibrium as a function of the particular payoff matrix. Worst-case bounds can hide large differences between easy games with clear strategic gaps and games containing nearly tied alternatives. A matching algorithm and lower bound would extend instance-sensitive exploration theory from choosing one best arm to discovering stable strategies for two competing players.

[Read in atlas](index.html#TCS-0668) · [COLT / PMLR](https://proceedings.mlr.press/v291/maiti25b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0681 — How fast can a multiclass test set be overfit?

Repeatedly checking models on the same test set lets later choices exploit information from earlier accuracy reports. This project asks how quickly such adaptive queries can overfit a multiclass test set. The desired characterization depends on the number of classes, the test-set size, and the number of accuracy queries. The source identifies a gap between attainable attacks and upper bounds, even when computational efficiency is not required. Closing that gap would explain how label multiplicity affects the statistical reliability of a benchmark that is repeatedly reused during model development.

[Read in atlas](index.html#TCS-0681) · [COLT / PMLR](https://proceedings.mlr.press/v99/feldman19b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0684 — The Dependence of Sample Complexity Lower Bounds on Planning Horizon

Long-horizon reinforcement learning appears difficult because useful actions may be separated from their eventual rewards by many steps. The selected problem asks for a sample-complexity lower bound with genuine polynomial dependence on the planning horizon. Total reward is normalized across an episode, preventing a larger reward scale from creating a merely artificial horizon factor. The source argues that some upper-bound assumptions hide difficult sparse-reward cases or restrict the accuracy regime too strongly. A suitable hard family would show when long-term planning itself requires more experience, beyond the difficulty already present in one-step bandit problems.

[Read in atlas](index.html#TCS-0684) · [COLT / PMLR](https://proceedings.mlr.press/v75/jiang18a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0689 — Property Elicitation and Elicitation Complexity

A statistical property is elicitable when minimizing an expected loss recovers that property of the underlying distribution. Familiar examples motivate asking which statistics admit such loss functions and how those functions can be characterized. The source also studies elicitation complexity, the number of intermediate real-valued reports needed to recover a desired statistic. Some properties that cannot be elicited directly may become accessible through a richer intermediate prediction. A general characterization would explain the expressive limits of empirical risk minimization and guide the design of objectives for estimating specific distributional quantities.

[Read in atlas](index.html#TCS-0689) · [COLT / PMLR](https://proceedings.mlr.press/v49/frongillo16.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1157 — Is ERM relatively smart in the distribution-free setting?

Semi-supervised learners can exploit knowledge of the unlabeled input distribution that an ordinary supervised learner does not receive. Relatively smart learning asks a supervised learner to compete with the best such guarantee that can itself be certified from unlabeled data. The source proves that a one-inclusion-graph learner achieves this comparison in the distribution-free setting with a quadratic sample overhead. The selected question asks whether empirical risk minimization, or another simpler natural learner, can obtain a comparable guarantee with some finite overhead. A positive result would turn the framework's existence theorem into a more familiar learning principle without assuming exact knowledge of the input distribution.

[Read in atlas](index.html#TCS-1157) · [Relatively Smart: A New Approach for Instance-Optimal Learning](https://proceedings.mlr.press/v336/dughmi26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1343 — Can membership queries always be removed from agnostic testable learning?

A testable learner must return a near-optimal predictor or reject data whose distribution it cannot safely handle. Membership queries let it choose extra inputs whose labels it wants to see. The conjecture says that independent labeled examples always suffice with only polynomial extra time. The source already relates query-based testable learning to ordinary learning, but ordinary learning does not include the required rejection guarantee. A resolution would establish whether testing the distributional assumption removes large speedups from chosen-label queries.

[Read in atlas](index.html#TCS-1343) · [Limitations of Membership Queries in Testable Learning](https://doi.org/10.4230/LIPIcs.ITCS.2026.91) · [Limitations of Membership Queries in Testable Learning — full version](https://arxiv.org/abs/2512.02279v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1361 — We leave open √the problem of whether there is an efficient algorithm that uses n = Õ(dε2 κ2 ) samples when κ ⩽ d and […]

Robust linear regression must estimate a predictor despite adversarially corrupted observations. This source studies Gaussian covariates with unknown covariance and tracks how the covariance condition number interacts with the corruption rate. The selected question asks for an efficient algorithm matching a proposed subquadratic sample scale while obtaining nontrivial error in the less favorable conditioning regime. Statistical-query and low-degree lower bounds provide evidence about the tradeoff but do not supply the missing general algorithm. A matching construction would identify how far efficient robust estimation can improve on a trivial predictor when corruption and ill-conditioning reinforce each other.

[Read in atlas](index.html#TCS-1361) · [On efficient robust regression with subquadratic samples](https://proceedings.mlr.press/v336/adil26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1478 — It remains open whether one can remove such constraints and achieve successful learning for all VC classes, which leads to the following open question:

Sequential prediction with abstentions permits a learner to decline to label suspicious instances in a partly adversarial data stream. Clean instances come independently from an unknown distribution, while corrupted instances may be inserted by an adaptive adversary. The source asks for sublinear misclassification and erroneous-abstention counts for every finite-VC class, with polynomial dependence on VC dimension. Existing adaptive-adversary guarantees require an additional finite reduction-dimension condition. Removing it would show that abstention can preserve the broad learnability of stochastic classification even when corruptions respond to the learner and the clean distribution is unknown.

[Read in atlas](index.html#TCS-1478) · [Distribution-Free Sequential Prediction with Abstentions](https://proceedings.mlr.press/v336/yu26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1539 — Does there exist an adversarially robust compression scheme of size O(f (dVC )) for C?

Sample compression stores a small part of a labeled sample and reconstructs a hypothesis consistent with the full sample. Adversarially robust compression must preserve correctness across every allowed perturbation of each example. The source asks whether a finite-VC class with a compression bound f(d) necessarily has a robust scheme of comparable size. Its positive construction uses stable compression, so the issue is removing that extra structural requirement. A nearby negative result for robust learnability alone does not automatically settle this stronger premise, making the distinction between learnability and compression assumptions essential.

[Read in atlas](index.html#TCS-1539) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1573 — Lastly, of course, the NP-hardness of improper learning for P/poly remains open.

Improper learning allows a learner to output a hypothesis outside the representation class used by the target function. This project asks for NP-hardness of learning functions represented by polynomial-size circuits even with that freedom. Hardness arguments for proper learning can fail because they constrain the output representation, a restriction absent here. The source develops connections between strong formulations of learning hardness and cryptographic primitives such as witness encryption. A reduction with the required guarantees would sharpen the boundary between computational learning and worst-case complexity while clarifying those cryptographic consequences.

[Read in atlas](index.html#TCS-1573) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2111 — The existence of a fully-polynomial time algorithm remains open even for the special case of positive weights, where the best known algorithm (Diakonikolas and Kane, […]

A one-hidden-layer ReLU network is a linear combination of k rectified linear functions of a d-dimensional input. The source studies learning its predictions from Gaussian examples under squared error. It asks for running time polynomial jointly in dimension, network width, and inverse accuracy, even when all output weights are positive. Its existing algorithms and correlational-query lower bounds leave open whether stronger learning methods can avoid exponential parameter dependence. A fully polynomial learner would show that expressive interactions among a modest number of ReLU units need not create an inherent computational barrier under Gaussian inputs.

[Read in atlas](index.html#TCS-2111) · [Efficiently Learning One-Hidden-Layer ReLU Networks via SchurPolynomials](https://proceedings.mlr.press/v247/diakonikolas24c.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2336 — Is it true that, for any concept class H, the optimal regret is Θ L(H)T ?

Multiclass online classification predicts one of several labels before observing the correct answer. The Littlestone dimension measures the sequential complexity of the competing concept class. The source asks whether optimal regret has the sharp square-root dependence on dimension times horizon suggested by its lower bound, with no extra logarithmic factor. It points to the removal of an analogous factor in binary classification as motivation. A proof would identify whether multiple labels introduce an intrinsic additional penalty or whether the remaining logarithm is a limitation of the existing analysis.

[Read in atlas](index.html#TCS-2336) · [Multiclass Online Learning and Uniform Convergence](https://proceedings.mlr.press/v195/hanneke23b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2339 — Is there a universal constant c > 0 such that, for each finite concept class C, we have that RTD(C) ≤ c · VCD(C)?

A finite concept class can be studied through both its VC dimension and its recursive teaching dimension. VC dimension measures the ability to realize label patterns, while recursive teaching measures how examples can identify concepts through successive elimination. The question asks whether one universal constant always bounds recursive teaching dimension by that constant times VC dimension. The same constant must work for every finite class. The project seeks a direct quantitative link between the complexity of learning from samples and the information needed for structured teaching.

[Read in atlas](index.html#TCS-2339) · [Tournaments, Johnson Graphs and NC-Teaching](https://proceedings.mlr.press/v201/simon23a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2422 — It remains open whether learning sparse parities by small programs is NP-hard.

A sparse parity predicts a binary label by adding only a small number of input bits modulo two. The source asks whether learning such targets using small programs is NP-hard in the intended representation model. Its motivating approach uses regularized probabilistically checkable proofs, but regularizing the proof queries is not enough to establish the learning reduction. Allowing a program as the output can give the learner more flexibility than requiring an explicit sparse parity. A hardness result must therefore control that richer output representation rather than only proving that finding the best sparse parity is difficult.

[Read in atlas](index.html#TCS-2422) · [Regularization of Low Error PCPs and an Application to MCSP](https://doi.org/10.4230/LIPIcs.ISAAC.2023.39)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2654 — Does there exist an online learning rule that is strongly universally consistent for the family {(X, Y) : X ∈ SUOL}?

Universal online learning seeks vanishing average regret against every fixed measurable prediction function. The source permits responses to depend arbitrarily on the history and imposes assumptions only on the input process. It asks for one strongly consistent rule whenever that input process belongs to the class admitting universal online learning. This strengthens the deterministic-target version by allowing general response sequences. An answer would identify whether learnability of the inputs alone can support one universal predictor even when the relationship between inputs and observed responses is neither fixed nor conditionally independent.

[Read in atlas](index.html#TCS-2654) · [Universally Consistent Online Learning with Arbitrarily Dependent Responses](https://proceedings.mlr.press/v167/hanneke22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2827 — In the case of bounded losses, both the question of the existence of optimistically universal online learning rules, and of concisely characterizing the set SUOL, […]

Optimistically universal online learning asks for one rule that succeeds on every input process for which universal learning is possible. For bounded losses, the source also proposes characterizing those processes by how slowly they visit new cells of every countable measurable partition. The required number of visited cells grows sublinearly with time. The passage frames both the algorithm and characterization as questions in its historical setting. Later work cited elsewhere in the collection reports progress on the algorithmic question, so developing this record further requires separating that history from the exact remaining process-characterization task.

[Read in atlas](index.html#TCS-2827) · [Universal Online Learning with Unbounded Losses: Memory Is All You Need](https://proceedings.mlr.press/v167/blanchard22a.html) · [https://proceedings.mlr.press/v167/hanneke22a.html](https://proceedings.mlr.press/v167/hanneke22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3113 — Whether hypothesis classes of finite VC dimension exist which are not improperly CPAC learnable in the agnostic case remains an open question.

Finite VC dimension characterizes statistical PAC learnability without requiring the learner to be computable. The source asks whether a finite-VC class can fail computable agnostic learning even when the learner may output hypotheses outside the class. The agnostic setting allows labels that no member fits perfectly, so the learner must compete with the best available hypothesis. Known failures of proper computable learning do not settle this more permissive output model. A counterexample or positive theorem would locate how much computational difficulty can be removed by abandoning the requirement to return a member of the original class.

[Read in atlas](index.html#TCS-3113) · [Open Problem: Are all VC-classes CPAC learnable?](https://proceedings.mlr.press/v134/open-problem-agarwal21b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3114 — Thus, the case that remains open concerns uncountable X and general (random) sequences X.

An optimistically universal online learner succeeds whenever the observed input process admits any universally consistent learning rule. The source isolates the difficult case of random sequences on an uncountable instance space. Memorizing labels handles some simpler regimes, but fails when fresh inputs keep appearing without exact repetition. The historical problem asks whether one algorithm can adapt across all learnable processes in either the weak or strong consistency sense. Later progress must be checked against those precise variants, since a result for deterministic targets or one mode of convergence need not settle every formulation.

[Read in atlas](index.html#TCS-3114) · [Open Problem: Is There an Online Learning Algorithm That Learns Whenever Online Learning Is Possible?](https://proceedings.mlr.press/v134/open-problem-hanneke21b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3117 — Any learner that tries to learn x ∈ {0, 1}n from a stream of samples of the form (a, b), where a ∈ {0, 1}n […]

Learning parity with noise observes random linear equations whose labels are only slightly more likely to be correct than incorrect. The source studies learners restricted to a small working memory while processing a stream of these equations. It conjectures that avoiding exponentially many samples requires memory of order n squared divided by epsilon squared, where epsilon is the bias toward correct labels. The proved lower bound has a weaker dependence on that bias. Matching it would quantify how little per-sample information forces a learner to retain increasingly large state, beyond noiseless parity-learning barriers.

[Read in atlas](index.html#TCS-3117) · [Memory-Sample Lower Bounds for Learning Parity with Noise](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.60)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3177 — In other words, does polynomial time learnability of NP/poly imply polynomial time learnability of PH/poly?

Learning complexity asks whether examples can be converted efficiently into predictors for an entire class of computational functions. The source considers the nonuniform classes NP/poly and PH/poly, which permit polynomial-size advice. It asks whether polynomial-time learnability of the first would imply polynomial-time learnability throughout the polynomial hierarchy. The analogy is with structural collapse theorems, but the learning setting introduces distributional and oracle issues. A proof or barrier would clarify whether learning a nondeterministic level is powerful enough to handle repeated alternations, rather than merely yielding faster algorithms for isolated concept classes.

[Read in atlas](index.html#TCS-3177) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3391 — However, it is still unknown whether it is possible to learn a mixture of well-separated Gaussians in polynomial time with polynomial sample complexity.

Learning a well-separated spherical Gaussian mixture requires estimating the component parameters from unlabeled samples. The source establishes favorable sample complexity and local convergence of expectation maximization once initialization is sufficiently good. It asks for an algorithm with both polynomial running time and polynomial sample complexity under the stated separation regime. Local refinement does not by itself supply an efficient global initialization procedure. Closing this gap would show whether enough statistical separation to identify the mixture also suffices for efficient end-to-end recovery, without quasipolynomial dependence on the number of components.

[Read in atlas](index.html#TCS-3391) · [The EM Algorithm gives Sample-Optimality for Learning Mixtures of Well-Separated Gaussians](https://proceedings.mlr.press/v125/kwon20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3450 — We conjecture that for some a > 0 even (na )-local queries won’t lead to efficient distribution free algorithms for these classes.

Local membership queries let a learner request labels near examples already sampled from the input distribution. On the Boolean cube, locality is measured by Hamming distance. The source conjectures that allowing a polynomial-radius neighborhood still fails to give efficient distribution-free learners for classes such as decision trees, juntas, and sparse polynomials covered by its weaker lower bounds. This goes beyond the established barriers for constant or mildly logarithmic radii. A proof would show how far targeted local exploration can expand before it gains the power of unrestricted label queries.

[Read in atlas](index.html#TCS-3450) · [Distribution Free Learning with Local Queries](https://proceedings.mlr.press/v117/bary-weisberg20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3689 — While the general relationship between NCTD and VCD remains open, it is now known that NCTD(C) is upper-bounded by VCD(C) when C is a finite […]

Non-clashing teaching assigns each concept a small labeled witness so that distinct concepts cannot mutually agree with both witnesses. The minimum largest witness size defines the non-clashing teaching dimension. The source asks how this measure relates in general to VC dimension. It records an upper bound by VC dimension for finite maximum classes, using special representation maps. Extending or separating that relationship would explain whether the information needed to teach individual concepts is controlled by the same combinatorial complexity that governs learning them from randomly sampled examples.

[Read in atlas](index.html#TCS-3689) · [Optimal Collusion-Free Teaching](https://proceedings.mlr.press/v98/kirkpatrick19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3691 — We could not derive such bounds for distributions satisfying Dobruhsin’s condition and we do not know if such bounds apply for all classes of finite […]

Uniform convergence requires empirical losses to approximate population losses simultaneously over an entire hypothesis class. The source studies data whose coordinates are dependent but satisfy weak-influence conditions. It asks whether Dobrushin's condition alone supports suitable uniform convergence bounds for every finite-VC class. The paper proves results under a stronger logarithmic-influence condition and uses other techniques for some learning guarantees. Resolving the question would determine whether a standard notion of weak dependence is enough to recover the broad statistical control normally supplied by independent samples.

[Read in atlas](index.html#TCS-3691) · [Learning from Weakly Dependent Data under Dobrushin’s Condition](https://proceedings.mlr.press/v99/dagan19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3787 — We leave as open whether our unlabeled compression scheme extends to ample (a.k.a. lopsided or extremal) classes, which represent a natural and far-reaching generalization of […]

An unlabeled sample compression scheme stores selected input points without their labels and reconstructs a consistent concept. The source gives an optimal-size construction for maximum classes, whose size attains the VC counting bound. It asks whether this construction extends to the broader family of ample classes. Earlier corner-peeling arguments do not settle the question because the source exhibits maximum classes without the required corners. A solution would generalize compression through the cubical geometry and unique-sink-orientation structure of these classes, rather than relying on that invalid simplification.

[Read in atlas](index.html#TCS-3787) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.4230/LIPIcs.ICALP.2019.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4031 — On the other hand, we do not know if AC 0 is self-learnable by quasi-polynomial size AC 0 circuits.10 A natural approach here is to […]

The source asks whether AC0 can be self-learned by AC0 circuits of quasipolynomial size. Here both the target functions and the proposed learning machinery are restricted by shallow circuit structure. A learner may need computations more complex than evaluating any one member of the class it learns. Understanding this restriction would connect learnability with pseudoderandomization and representation complexity. The saved sentence does not define the learning access model or success guarantee, so examples, membership queries, and other forms of information cannot be treated as interchangeable resources.

[Read in atlas](index.html#TCS-4031) · [Pseudo-Derandomizing Learning and Approximation](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2018.55)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4074 — Classically, it is still an open question whether the log(1/ε)-factor in the upper bound of [17] for (ε, δ)-proper PAC learning is necessary.

A proper PAC learner must return a hypothesis belonging to the original concept class. The sample-complexity question asks whether proper learning requires an extra logarithmic factor in inverse accuracy. The cited quantum-learning work proposes removing that factor with quantum examples as a potentially easier intermediate target. The properness restriction matters because allowing hypotheses outside the class can change the best achievable sample bound. An improved learner or a lower bound would explain whether the statistical cost comes from identifying a good prediction rule or from expressing that rule inside the prescribed class.

[Read in atlas](index.html#TCS-4074) · [Optimal Quantum Sample Complexity of Learning Algorithms](https://doi.org/10.4230/LIPIcs.CCC.2017.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4134 — A related question which remains open, originally posed by Ben-David and Eiron Ben-David and Eiron (1998), is that of computing the self-directed learning4 mistake bound.

In self-directed learning, a learner chooses which unlabeled example to predict next and then observes its correct label. For a finite concept class, the associated mistake bound measures the smallest worst-case number of errors achievable by choosing examples and predictions adaptively. The question is how difficult it is to compute this combinatorial parameter from a representation of the class. The source raises it beside hardness results for other learning dimensions and also suggests studying approximation and recursive teaching dimension. A complexity classification would distinguish the existence of a good teaching order from the ability to find or evaluate one efficiently.

[Read in atlas](index.html#TCS-4134) · [Inapproximability of VC Dimension and Littlestone’s Dimension](https://proceedings.mlr.press/v65/manurangsi17a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4186 — In particular, is there an analogous result for learning under the uniform distribution using random examples?

The cited source connects learning algorithms, circuit lower bounds, and pseudorandomness. Its saved question asks whether an analogous result holds for learning from random examples under the uniform distribution. Random examples provide less control than models allowing the learner to choose exactly which inputs it observes. An extension would show that the source's complexity connection survives this more passive information model. The excerpt omits the original theorem and target concept class, so the consequence being sought and the required learning accuracy still need to be recovered.

[Read in atlas](index.html#TCS-4186) · [Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness](https://doi.org/10.4230/LIPIcs.CCC.2017.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4592 — What is the optimal time complexity for agnostically learning halfspaces on the Gaussian distribution?

Agnostic halfspace learning seeks a classifier whose error nearly matches the best linear threshold rule, even when labels do not follow any halfspace. This question fixes the unlabeled distribution to be Gaussian and asks for the optimal running time as dimension and target excess error vary. The source specifically proposes a running time whose exponent in the dimension grows only logarithmically with inverse error. It supports that target with a conditional lower bound derived from learning sparse parities with noise. Matching the proposed rate would identify a precise computational price for handling arbitrary label noise under a highly regular input distribution.

[Read in atlas](index.html#TCS-4592) · [Embedding Hard Learning Problems Into Gaussian Space](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2014.793)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4604 — However, establishing tight information theoretic lower bound on n (w.r.t. `, r) is still an open problem. 2

The model is a mixture of r product distributions on n discrete coordinates, each taking one of a fixed number of possible values. Within a component the coordinates are independent, but the hidden component creates dependence in the observed samples. The source's spectral recovery method requires the number of coordinates to be at least on the order of the cube of the number of components. The question asks for tight information-theoretic lower bounds on the number of coordinates in terms of the alphabet size and component count. This concerns identifiability of the latent mixture, rather than simply collecting more observations of an insufficiently informative model.

[Read in atlas](index.html#TCS-4604) · [Learning Mixtures of Discrete Product Distributions using Spectral Decompositions](https://proceedings.mlr.press/v35/jain14.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4621 — We conjecture that the optimal bounds are that for every class H, B-ErrrH (T ) = O(k · L(H)) a p and B-ErrH (T ) […]

Bandit multiclass classification tells a learner only whether its predicted label was correct, rather than revealing the correct label after every mistake. The source conjectures sharper error bounds in terms of the number of labels and the ordinary Littlestone dimension. Its proposed realizable bound is linear in their product, while the agnostic regret has the corresponding square-root dependence on the horizon. These targets would tighten the known price of restricted label feedback. A proof would clarify whether bandit information introduces only the expected label-count penalty or requires additional structural complexity measures.

[Read in atlas](index.html#TCS-4621) · [The price of bandit information in multiclass online classification](https://proceedings.mlr.press/v30/Daniely13.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4672 — How large can P BI(H) be when H is a class of functions from a domain X to a range Y of cardinality k?

In multiclass online learning, full feedback reveals the correct label after each prediction, while bandit feedback only says whether the prediction was correct. Littlestone dimension and bandit Littlestone dimension quantify the corresponding worst-case mistake complexities in the source's realizable model. The price of bandit information is their ratio for the same hypothesis class. For a label set of size k, the question asks how large this ratio can be across classes and domains. A sharp bound would isolate the cost of withholding the correct label from the underlying difficulty of predicting the class itself.

[Read in atlas](index.html#TCS-4672) · [Multiclass Learnability and the ERM principle](https://proceedings.mlr.press/v19/daniely11a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4792 — Sample Compression Scheme Reductions — Open Problem 5

A sample compression scheme stores a small subset of labeled examples and enough permitted auxiliary information to reconstruct a hypothesis consistent with the full sample. This problem compares compression for binary classes with compression for classes whose labels may take many values. Assuming every binary class of VC-dimension d admits compression of size f(d), it asks whether graph dimension gives the corresponding multiclass bound up to a constant factor. The source establishes stronger reductions under additional assumptions on the binary reconstruction procedure, including proper or majority-vote reconstruction. Removing those assumptions would transfer binary compression advances to multiclass learning through a general structural reduction.

[Read in atlas](index.html#TCS-4792) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4972 — Backdoor Defense, Learnability and Obfuscation — Unresolved-question passage on page 13

Decision trees represent a Boolean function by branching on input variables until reaching an output. The selected question asks whether polynomial-size decision trees can be learned efficiently from ordinary examples drawn uniformly at random. The source contrasts this with efficient learning when membership queries allow the learner to choose additional inputs. In its backdoor-defense setting, access to a tree's representation makes those chosen evaluations easy, enabling defenses without resolving the example-only learning question. Understanding the latter would clarify the gap between learning an unknown tree and checking the behavior of a tree already available as code.

[Read in atlas](index.html#TCS-4972) · [Backdoor Defense, Learnability and Obfuscation](https://doi.org/10.4230/LIPIcs.ITCS.2025.38)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5017 — Learning with Monotone Adversarial Corruptions — Open Question 1

A monotone adversary first observes a clean independent training sample and then inserts additional points that are all labeled correctly by the same target hypothesis. The learner receives the shuffled combined sample and is evaluated on fresh points from the original distribution. For a binary class of VC-dimension d and n clean examples, the question asks for the best achievable expected error. The source retains the empirical-risk-minimization guarantee with its logarithmic factor, but its lower bounds for familiar optimal learners do not rule out every algorithm attaining order d/n. The obstacle is that truthful additions can still destroy the independence used by sharper generalization arguments.

[Read in atlas](index.html#TCS-5017) · [Learning with Monotone Adversarial Corruptions](https://proceedings.mlr.press/v313/larsen26a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5031 — The Dimension of Self-Directed Learning — Unresolved-question passage on page 16

Online classification compares a learner's errors with the best hypothesis in a concept class. The cited result gives optimal square-root regret in the product of horizon and Littlestone dimension under an additional regularity condition. The extracted question asks whether that characterization holds for completely unrestricted classes. The restriction matters because it supports a minimax argument for an associated game. Removing it would show that the combinatorial dimension alone determines regret, even where the usual interchange between randomized strategies and adversarial choices cannot simply be assumed.

[Read in atlas](index.html#TCS-5031) · [The Dimension of Self-Directed Learning](https://proceedings.mlr.press/v237/devulapalli24a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5060 — Learning to Control Linear Systems can be Hard — Explicit open question on PDF page 9

Learning to stabilize an unknown linear dynamical system means using observed trajectories to construct feedback that prevents unstable growth. The source shows that the required number of samples can grow exponentially with state dimension for certain systems with too few control inputs. Its stabilization lower-bound construction relies on noise that excites only a lower-dimensional part of the state space. The question asks whether a comparable failure of polynomial sample complexity can occur when the noise has full rank. This would separate difficulty caused by missing excitation from difficulty intrinsic to identifying and controlling an underactuated system.

[Read in atlas](index.html#TCS-5060) · [Learning to Control Linear Systems can be Hard](https://proceedings.mlr.press/v178/tsiamis22a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5061 — On characterizations of learnability with computable learners — Explicit open question on PDF page 6

Computable PAC learning requires an actual algorithm producing hypotheses with the usual distribution-free statistical guarantee. Strong computable PAC learning additionally requires a computable bound on the sample size needed for a requested accuracy and confidence. The source asks whether a hypothesis class can admit a proper computable PAC learner while admitting no proper learner with such an effective sample bound. Any separating class would force the necessary sample-complexity behavior beyond computable upper bounds in the sense developed there. The question tests whether effective prediction and effective knowledge of when prediction becomes reliable are distinct requirements.

[Read in atlas](index.html#TCS-5061) · [On characterizations of learnability with computable learners](https://proceedings.mlr.press/v178/sterkenburg22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5087 — Adversarially Robust Low Dimensional Representations — Explicit open question on PDF page 7

Adversarially robust dimension reduction seeks a low-rank projection that both approximates a dataset and limits the effect of small perturbations to individual data points. Here even the training matrix is corrupted, so the approximation must be good for an unknown original matrix rather than merely the observed one. The source gives stronger recovery guarantees in Frobenius norm, while its efficient spectral-norm method may instead certify substantial poisoning. It asks for a polynomial-time estimator achieving the stronger spectral guarantee already available information theoretically. The difficulty is that many small coordinate changes can accumulate into a large matrix perturbation and obscure which subspace represents the clean data.

[Read in atlas](index.html#TCS-5087) · [Adversarially Robust Low Dimensional Representations](https://proceedings.mlr.press/v134/awasthi21a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5088 — Learning Intersections of Two Margin Halfspaces under Factorizable Distributions — Explicit open question on PDF page 5

An intersection of k halfspaces labels a point positively only when it satisfies all k linear inequalities. Even under a Gaussian input distribution or the uniform distribution on the Boolean cube, the source identifies a gap between learning algorithms and fully polynomial efficiency. The question asks whether the dependence on dimension, number of halfspaces, and inverse accuracy can all be polynomial under these distributional assumptions. The surrounding paper studies a restricted two-halfspace setting with margin and factorization assumptions, which illustrates how additional structure can help. Resolving the broader question would clarify whether simple input distributions make learning a growing conjunction of thresholds computationally feasible.

[Read in atlas](index.html#TCS-5088) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5090 — On the Structure of Learnability Beyond P/Poly — Explicit open question on PDF page 4

The class P/poly consists of Boolean functions computable by polynomial-size circuits, and learning it would cover a broad range of efficiently represented prediction rules. This question asks whether worst-case hardness of efficient learning from random labeled examples already implies the existence of one-way functions. One-way functions require average-case resistance to inversion, making this a proposed bridge from learning hardness to a basic cryptographic assumption. The source obtains structural equivalences for stronger concept classes such as PSPACE/poly and EXP/poly, but does not extend this implication to P/poly. A resolution would explain whether difficult circuit learning necessarily contains the kind of average-case hardness needed for cryptography.

[Read in atlas](index.html#TCS-5090) · [On the Structure of Learnability Beyond P/Poly](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5118 — Majority-of-Three: The Simplest Optimal Learner? — Explicit open question on PDF page 4

Majority-of-Three trains three empirical risk minimizers on independent samples from the same realizable binary classification problem and predicts by their majority vote. The conjecture asks whether this simple procedure always achieves error of order (d + log(1/delta))/n with confidence at least one minus delta. Here d is the class's VC-dimension and each component learner receives n examples, with the claim covering any choice of empirical risk minimizer. The source proves optimal behavior in some confidence regimes but leaves an extra iterated logarithm in its general bound. Removing that term would establish an especially simple optimal learner across the full range of confidence parameters.

[Read in atlas](index.html#TCS-5118) · [Majority-of-Three: The Simplest Optimal Learner?](https://proceedings.mlr.press/v247/aden-ali24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5119 — Information Theoretic Optimal Learning of Gaussian Graphical Models — Explicit open question on PDF page 1

A Gaussian graphical model encodes conditional dependencies through the nonzero entries of the inverse covariance matrix. The motivating question asks whether its underlying sparse graph can be recovered with the information-theoretically optimal sample count by a polynomial-time algorithm. The source's DICE procedure settles the sample-complexity component using only graph size, maximum degree, and minimum normalized edge strength in its bound. Its search cost still has an exponent depending on the degree, so the paper separately asks for computationally efficient sample-optimal recovery in general. This record therefore combines a statistical question answered in the source with a remaining algorithmic efficiency direction.

[Read in atlas](index.html#TCS-5119) · [Information Theoretic Optimal Learning of Gaussian Graphical Models](https://proceedings.mlr.press/v125/misra20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5153 — VC Classes are Adversarially Robustly Learnable, but Only Improperly — Explicit open question on PDF page 10

Adversarially robust PAC learning seeks a predictor that remains correct under every permitted test-time perturbation of a fresh example. The perturbation rule and the hypothesis class together determine this task, even though the training observations themselves are independent and uncorrupted. The source proves that finite VC-dimension suffices with improper learning and that a robust shattering dimension supplies a necessary condition. Neither observation yields the requested exact characterization, since ordinary VC-dimension need not be necessary and the sufficiency of the robust quantity is unresolved there. The question is to identify a complexity measure that precisely captures robust learnability and supports corresponding sample bounds.

[Read in atlas](index.html#TCS-5153) · [VC Classes are Adversarially Robustly Learnable, but Only Improperly](https://proceedings.mlr.press/v99/montasser19a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5215 — Reliably Learning the ReLU in Polynomial Time — Explicit open question on PDF page 2

A single ReLU predicts a real value by applying the positive-part function to a linear form. The source studies agnostic learning over arbitrary distributions on the unit sphere and gives a running time polynomial in dimension but exponential in inverse error. Consequently, its method remains polynomial-time for errors at least on the order of one over log n. A reduction from noisy parity learning supplies a conditional obstruction when the requested error becomes inverse polynomial in n. The question is to determine the accuracy threshold between these regimes, even for this elementary neural unit.

[Read in atlas](index.html#TCS-5215) · [Reliably Learning the ReLU in Polynomial Time](https://proceedings.mlr.press/v65/goel17a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5247 — Learning Multinomial Logits in O(n log n) Time — Explicit open question on PDF page 1

A multinomial logit model assigns positive weights to items and selects from any offered slate with probabilities proportional to those weights. The learning goal is to estimate weights whose induced choice distribution is close to the true distribution on every slate simultaneously. The source introduces this query-complexity question and then supplies adaptive and nonadaptive algorithms using only pairs of items. Its adaptive result is optimal in its dependence on the number of items, while other parameter dependencies and the nonadaptive gap require separate comparison with the lower bounds. The entry therefore concerns a concrete model-learning problem substantially answered by its cited paper, rather than an untouched existence question.

[Read in atlas](index.html#TCS-5247) · [Learning Multinomial Logits in O(n log n) Time](https://doi.org/10.4230/LIPIcs.ICALP.2026.63)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5434 — Agnostic Membership Query Learning with Nontrivial Savings: New Results and Techniques — Explicit open question on PDF page 6

Agnostic membership-query learning must approximate an arbitrary target nearly as well as the best hypothesis in a specified circuit class. The source asks for a nontrivial learning-time saving for ACC0 circuits, even under uniformly distributed inputs. Membership queries allow the learner to choose labeled examples. The target must tolerate noise or mismatch between the target and the hypothesis class. The project seeks algorithmic progress beyond exhaustive truth-table processing while preserving a guarantee relative to the best available constant-depth modular circuit.

[Read in atlas](index.html#TCS-5434) · [Agnostic Membership Query Learning with Nontrivial Savings: New Results and Techniques](https://proceedings.mlr.press/v237/karchmer24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5478 — Reaching Goals is Hard: Settling the Sample Complexity of the Stochastic Shortest Path — Explicit open question on PDF page 13

A stochastic shortest-path problem asks a learner to reach a goal while minimizing accumulated cost, with no fixed horizon imposed in advance. The source studies how many transition observations are needed to identify a nearly optimal policy and shows that unrestricted instances can be statistically intractable. Its remaining questions concern sharp sample bounds when comparison policies have bounded hitting time and when learning proceeds through actual interaction rather than a generative simulator. For the latter setting it studies an assumption allowing the goal to be reached directly at a fixed cost and asks for weaker alternatives. The central issue is how controllable access to the goal changes the statistical difficulty of planning.

[Read in atlas](index.html#TCS-5478) · [Reaching Goals is Hard: Settling the Sample Complexity of the Stochastic Shortest Path](https://proceedings.mlr.press/v201/chen23a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5847 — Open Problem: Information Complexity of VC Learning — Explicit open question on PDF page 2

The source studies how much information a learning algorithm reveals while learning a class of VC dimension d. Its conjecture seeks a learner with conditional mutual information bounded by O(d). The desired bound would make information usage depend linearly on the class's combinatorial capacity rather than on additional sample-related factors. This connects statistical learnability with a precise notion of how strongly the output depends on the training data. The excerpt ends before the learner's accuracy and sample guarantees, so those conditions must be recovered before an information bound can be interpreted as a full learning result.

[Read in atlas](index.html#TCS-5847) · [Open Problem: Information Complexity of VC Learning](https://proceedings.mlr.press/v125/steinke20b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5902 — Approximate Learning of Limit-Average Automata — Explicit open question on PDF page 3

Learning a deterministic finite automaton from examples means producing a hypothesis that predicts its acceptance behavior. The cited question asks whether this can be done efficiently in the probably approximately correct framework under the specified uniform distribution. The learner should achieve low error with high confidence from randomly sampled labeled words. Results allowing membership and equivalence queries provide stronger information and therefore do not settle this sampling-only target. An answer would clarify whether a simple data distribution removes the computational obstacles to learning arbitrary finite-state languages.

[Read in atlas](index.html#TCS-5902) · [Approximate Learning of Limit-Average Automata](https://doi.org/10.4230/LIPIcs.CONCUR.2019.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6040 — Learning Coverage Functions and Private Release of Marginals — Explicit open question on PDF page 4

Coverage functions measure the value of the union of objects selected from a family and arise in learning and private release of database marginals. The cited passage asks how to compute a strong approximation in the learning setting studied by the paper. It emphasizes difficulty even with value-query access and a restricted input distribution. An algorithm could strengthen the connection between learning these structured functions and publishing useful private statistics. However, the saved quotation cuts off both the distribution restriction and the approximation target, so this working explanation cannot responsibly supply a numerical guarantee or identify the entire unresolved variant.

[Read in atlas](index.html#TCS-6040) · [Learning Coverage Functions and Private Release of Marginals](https://proceedings.mlr.press/v35/feldman14a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6135 — Mitigating Covariate Shift in Misspecified Regression with Applications to Reinforcement Learning — Unresolved-question passage on page 8

Covariate shift changes the distribution of inputs between training and evaluation, while model misspecification prevents the hypothesis class from representing the truth exactly. The source develops regression guarantees that avoid excessive amplification of that misspecification. It asks for the optimal approximation factor and whether improving that factor necessarily worsens the statistical convergence term. Its own improved constant comes with such a deterioration, but does not prove it unavoidable. Resolving the tradeoff would show how accurately shifted data can be handled when both finite samples and imperfect models contribute to error.

[Read in atlas](index.html#TCS-6135) · [Mitigating Covariate Shift in Misspecified Regression with Applications to Reinforcement Learning](https://proceedings.mlr.press/v247/amortila24a.html)
Existing status: `source_open` · Summary written: 2026-09-11

## Cryptography (31)

### TCS-6545 — Do one-way functions imply public-key encryption in the standard model?

A one-way function is easy to evaluate but hard to invert on a randomly generated input. Public-key encryption needs a further asymmetry: anyone can encrypt using public information, while only the secret-key holder can decrypt. This project asks whether the existence of one-way functions alone guarantees such an encryption scheme in the standard classical model. Symmetric encryption follows from one-way functions, but its initially shared secret does not supply the missing public-key structure. The question allows constructions that inspect the implementation of the underlying function, so limitations of black-box constructions do not settle it.

[Read in atlas](index.html#TCS-6545) · [Foundations of Cryptography, Lecture 10](https://mit6875.github.io/FA23SLIDES/lec10.pdf) · [The Complexity of Public-Key Cryptography](https://eprint.iacr.org/2017/365) · [Limits on the provable consequences of one-way permutations](https://doi.org/10.1145/73007.73012) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [Merkle Puzzles are Optimal — an O(n²)-query attack on any key exchange from a random oracle](https://www.boazbarak.org/Papers/merkle.pdf) · [Public-Key Encryption from the MinRank Problem](https://arxiv.org/abs/2510.03752)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0022 — Does P≠NP imply the existence of one-way functions?

The statement P ≠ NP guarantees that some efficiently verifiable problems cannot be solved efficiently on every input. Cryptographic one-way functions require a stronger kind of difficulty: efficient attackers must fail to invert outputs generated from random inputs. This project asks whether worst-case hardness alone forces that average-case cryptographic hardness to exist. A function that is hard only on an extremely rare set would not provide the required security. Resolving the implication would clarify whether the most familiar complexity assumption already contains the foundations of computational cryptography.

[Read in atlas](index.html#TCS-0022) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf) · [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6550 — Does ordinary polynomial-hard LWE suffice for circuit obfuscation?

Indistinguishability obfuscation transforms equivalent programs so that an efficient observer cannot tell which implementation was supplied. This project asks whether ordinary polynomial-hard learning with errors is enough to construct obfuscation for all polynomial-size Boolean circuits. The question excludes extra assumptions about circular security, leakage resilience, or stronger hardness regimes. Its security notion compares programs with identical behavior rather than promising that arbitrary code reveals no information beyond black-box access. A construction under the stated LWE assumption would give this powerful primitive a substantially more economical foundation.

[Read in atlas](index.html#TCS-6550) · [On the (Im)possibility of Obfuscating Programs](https://www.wisdom.weizmann.ac.il/~oded/p_obfuscate.html) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Indistinguishability Obfuscation from Well-Founded Assumptions](https://doi.org/10.1145/3785007) · [Indistinguishability Obfuscation from LPN over F_p, DLIN, and PRGs in NC^0](https://eprint.iacr.org/2021/1334) · [Factoring and Pairings Are Not Necessary for IO: Circular-Secure LWE Suffices](https://doi.org/10.4230/LIPIcs.ICALP.2022.28)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6551 — Unleveled fully homomorphic encryption from LWE alone

Fully homomorphic encryption lets a server evaluate computations on encrypted data and return a compact encrypted answer. Leveled schemes choose their keys after fixing a maximum computation depth. This project asks whether ordinary polynomial-modulus LWE can support keys generated without such a depth bound while preserving compactness. It specifically excludes additional circular-security or key-dependent-message assumptions often associated with bootstrapping. A solution would establish whether unrestricted encrypted computation follows from the stated LWE assumption with no extra security hypothesis.

[Read in atlas](index.html#TCS-6551) · [Efficient Fully Homomorphic Encryption from (Standard) LWE](https://epubs.siam.org/doi/10.1137/120868669) · [Quantum FHE (Almost) As Secure As Classical](https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf) · [Fully Homomorphic Encryption: definitional issues and open problems](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf) · [Bootstrapping Homomorphic Encryption via Functional Encryption](https://eprint.iacr.org/2023/1376.pdf) · [Bootstrapping Homomorphic Encryption via Functional Encryption — conference version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.17/LIPIcs.ITCS.2023.17.pdf) · [Dynamic multi-key FHE without CRS from LWE](https://link.springer.com/article/10.1186/s42400-025-00431-z) · [Efficient Quantum Fully Homomorphic Encryption](https://arxiv.org/abs/2604.23490)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0465 — Can every perfect secret-sharing access structure use shares below exponent one half?

Secret sharing lets authorized groups reconstruct a secret while unauthorized groups learn nothing. The target asks for a universal bound K·2^(cn) bits per share for every n-party access structure, with c<1/2 and a one-bit secret. Perfect reconstruction and privacy are required, and nonlinear schemes are allowed. Nir’s August 2026 preprint states a 2^{0.496n+o(n)} bound that would meet this target. The claimed resolution is recorded with uncertain status because its proof has not been independently verified in this review.

[Read in atlas](index.html#TCS-0465) · [Algorithmic Aspects of Information Theory: open problems in secret sharing](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.12.7.180) · [The Share Size of Secret-Sharing Schemes for Almost All Access Structures and Graphs](https://eprint.iacr.org/2020/664) · [Resolving the Complexity of Linear Secret Sharing](https://eccc.weizmann.ac.il/report/2026/146/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7167 — Do classical one-way functions exist?

Do classical one-way functions exist without an unproved hardness assumption? A polynomial-time function with negligible inversion success against every uniform classical polynomial-time adversary, or a proof that none exists. Complete candidates and complexity-theoretic equivalences are known; their required hardness has not been proved. An unconditional existence or impossibility theorem. Would establish or rule out the basic computational asymmetry behind many cryptographic primitives.

[Read in atlas](index.html#TCS-7167) · [The Tale of One-Way Functions](https://doi.org/10.1023/A:1023634616182) · [The Tale of One-way Functions](https://arxiv.org/abs/cs/0012023v5) · [On One-way Functions and Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2020/052/) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/) · [Research Interests: Randomness and Computation](https://www.cs.bu.edu/fac/lnd/research/ps-r.htm)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7168 — Does computationally secure public-key encryption exist?

Can public-key encryption be proved computationally secure without an unproved hardness assumption? An efficient correct scheme with negligible IND-CPA advantage against every uniform classical PPT adversary, or a proof that none exists. Constructions from lattice and other hardness assumptions are known. No checked result proves an appropriate hardness assumption or establishes unconditional existence. Would give a mathematical foundation for secret communication using only an authenticated public key.

[Read in atlas](index.html#TCS-7168) · [Foundations of Cryptography, Volume 2: Basic Applications](https://www.wisdom.weizmann.ac.il/~oded/foc-vol2.html) · [Encryption Schemes: draft chapter for Foundations of Cryptography](https://www.wisdom.weizmann.ac.il/~oded/PSBookFrag/enc.ps) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Post-Quantum Cryptography from Quantum Stabilizer Decoding](https://arxiv.org/abs/2603.19110)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6549 — Does public-key encryption imply oblivious transfer?

Oblivious transfer lets a receiver obtain one of two secret messages while hiding which message it chose. At the same time, the receiver must remain unable to learn the unchosen message. This project asks whether ordinary public-key encryption alone is enough to construct such a protocol in the classical plain model. The specified target already restricts corruption to semi-honest parties, yet privacy must hold on both sides. A general implication would connect basic encryption to a central primitive for secure computation without assuming extra algebraic structure or setup.

[Read in atlas](index.html#TCS-6549) · [The Relationship between Public Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf) · [Black-Box Constructions of Protocols for Secure Computation](https://iftachh.github.io/MyHomepage/papers/BlackBoxMPC/black-box-mpc.pdf) · [Computational Hardness of Optimal FairComputation: Beyond Minicrypt](https://eprint.iacr.org/2021/882) · [Oblivious Transfer from Rerandomizable PKE](https://eprint.iacr.org/2023/1002) · [On the Implications from Updatable Encryption to Public-Key Cryptographic Primitives](https://doi.org/10.1587/transfun.2025CIP0019)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6547 — Does one-wayness suffice for collision-resistant hashing?

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

[Read in atlas](index.html#TCS-6552) · [Commitment Schemes and Zero-Knowledge Protocols (2011)](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf) · [Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors](https://web.eecs.umich.edu/~cpeikert/pubs/nizk-lwe.pdf) · [Batch Arguments to NIZKs from One-Way Functions](https://eprint.iacr.org/2023/1938) · [Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash](https://eprint.iacr.org/2024/1514) · [Fiat-Shamir in the Plain Model from Derandomization (Or: Do Efficient Algorithms Believe that NP = PSPACE?)](https://eccc.weizmann.ac.il/report/2024/116/) · [Non-Trivial Zero-Knowledge Implies One-Way Functions](https://arxiv.org/abs/2602.17651) · [Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way](https://doi.org/10.1007/978-3-032-35424-2_6)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6454 — Does worst-case Nearest Codeword hardness imply low-noise LPN hardness?

Learning parity with noise asks for information about hidden binary linear equations when some answers have been flipped. This project asks whether worst-case hardness of the binary nearest-codeword problem implies average-case hardness for a specified low-noise LPN distribution. The chosen regime uses quadratically many samples and a noise rate inversely proportional to the square root of the secret dimension. A reduction must produce that particular random-instance distribution rather than merely another hard coding problem or a different noise level. Such a connection would strengthen the theoretical foundation of low-noise LPN in the way worst-case reductions support lattice-based assumptions.

[Read in atlas](index.html#TCS-6454) · [Towards Worst-case Hardness for Low-Noise LPN](https://eccc.weizmann.ac.il/report/2026/095/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1138 — Polynomial-time computationally sound NP verification of #SAT

Counting satisfying assignments is harder to certify directly than showing that a single satisfying assignment exists. This project asks for a polynomial-time verifier for a claimed #SAT answer in the model called computationally sound NP by the source. Soundness is required against computationally bounded attempts to produce false proofs rather than against every possible proof string. That distinction allows the question to go beyond ordinary NP verification without asserting that #SAT has standard short certificates. A construction would expand the range of efficiently checkable counting claims and connect computational soundness with the source's broader study of derandomization.

[Read in atlas](index.html#TCS-1138) · [New ways of studying the BPP = P conjecture](https://eccc.weizmann.ac.il/report/2023/094/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1929 — Are there SIPs with statistical (or even perfect) zero-knowledge?

Streaming interactive proofs let a verifier process a long input with limited memory while relying on a more powerful prover. Adding zero knowledge should keep the interaction from disclosing information beyond the statement being checked. The selected question asks whether such protocols can achieve statistical or even perfect zero knowledge in the source's streaming setting. Its existing guarantees instead limit the distinguishing power of streaming adversaries, leaving stronger security and smaller distinguishing advantages as further targets. A construction would show that severe memory restrictions are compatible with substantially stronger privacy during interactive verification.

[Read in atlas](index.html#TCS-1929) · [Streaming Zero-Knowledge Proofs](https://doi.org/10.4230/LIPIcs.CCC.2024.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2519 — Every linear SSS has this property but it remains open whether every access structure in mP admits a randomness simulatable SSS.

Some secret-sharing applications need authorized participants to recover not only the secret but also the randomness used when creating the shares. The source proposes a construction using encryption of that randomness, but its security proof needs an extra property called randomness simulatability. Linear secret-sharing schemes have the required property. The open question is whether every access structure computable in monotone polynomial time admits an efficient scheme with the same feature. A positive answer would extend the randomness-recoverable construction beyond the algebraic cases where its proof currently applies directly.

[Read in atlas](index.html#TCS-2519) · [Randomness Recoverable Secret Sharing Schemes](https://doi.org/10.4230/LIPIcs.ITC.2023.12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2732 — Is there a perfectly secure 3-server DPF with key size N o(1) ?

A distributed point function splits a vector that is nonzero at one hidden position into compact evaluation keys held by several servers. Combining their outputs recovers the point function while permitted individual views hide its location. The question asks for a perfectly secure three-server construction with key size N^o(1), subpolynomial in the domain size N. The source achieves statistical privacy with three servers and perfect privacy with four, leaving the simultaneous three-server and perfect-security target. Meeting it would improve information-theoretic private retrieval and aggregation by reducing server requirements without giving up exact privacy.

[Read in atlas](index.html#TCS-2732) · [Information-Theoretic Distributed Point Functions](https://doi.org/10.4230/LIPIcs.ITC.2022.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2813 — Improving the gap in Theorem 19 requires proving better lower-bounds of ω(n2 / log n) for secret sharing schemes – a task that remains open […]

An access structure can be easy to compute yet expensive to realize through information-theoretic secret sharing. This source compares the total size of shares with the size of monotone real formulas computing the corresponding authorization function. It gives a separation using a linear-size formula and a total-share lower bound near the quadratic scale. The selected problem asks for a larger separation, which requires improving general secret-sharing lower bounds that the existing argument cannot surpass. A stronger result would reveal a deeper gap between recognizing authorized groups and distributing information so that only those groups can reconstruct the secret.

[Read in atlas](index.html#TCS-2813) · [Secret Sharing, Slice Formulas, and Monotone Real Circuits](https://doi.org/10.4230/LIPIcs.ITCS.2022.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3025 — Indeed, it is an open problem whether the existence of exponentially-hard weak one-way functions is equivalent to the existence of exponentially-hard strong one-way functions [31].

A weak one-way function resists inversion on a noticeable fraction of inputs, while a strong one-way function resists almost every efficient inversion attempt. Standard hardness amplification connects the two at ordinary polynomial security scales. This project asks whether equivalence also holds when the starting and resulting functions must both withstand exponential-time attacks relative to their input length. The obstacle is that familiar amplification increases input length enough to weaken the resulting exponent. A tighter transformation would preserve fine-grained cryptographic hardness and strengthen connections between one-wayness and average-case complexity.

[Read in atlas](index.html#TCS-3025) · [Hardness of KT Characterizes Parallel Cryptography](https://doi.org/10.4230/LIPIcs.CCC.2021.35)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3556 — We note, however, that since (even publicly-verifiable) PoSW satisfying weaker notions of sequentiality (e.g., σ = T /2) are known to exist in the ROM […]

A verifiable delay function should require sequential work to evaluate while allowing an answer to be checked much faster. The source proves limitations on constructing such primitives from random oracles when the required sequentiality is tightly matched to honest evaluation time. It asks whether impossibility can also be established for non-tight verifiable delay functions that tolerate a larger gap between those quantities. Weaker proofs of sequential work exist in the random-oracle model, so their known behavior prevents a direct extension of the tight lower bound. Resolving the question would clarify whether structured assumptions are necessary throughout the delay-function landscape or only for its strongest parameter regimes.

[Read in atlas](index.html#TCS-3556) · [Can Verifiable Delay Functions Be Based on Random Oracles?](https://doi.org/10.4230/LIPIcs.ICALP.2020.83)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4703 — Streaming Zero-Knowledge Proofs — Open problem 2

Streaming zero-knowledge proofs combine small-memory verification with protection of information revealed during the interaction. In the source's construction, the main proof phase uses very little communication, but preparing a reusable random string costs almost linear communication. The selected question asks whether total communication, including that setup, can become sublinear in the input length. Counting only the short post-setup exchange would hide the resource responsible for the open gap. Reducing it would make the protocols more attractive for large data streams and clarify the communication cost of obtaining zero knowledge with limited memory.

[Read in atlas](index.html#TCS-4703) · [Streaming Zero-Knowledge Proofs](https://doi.org/10.4230/LIPIcs.CCC.2024.2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4754 — A Relativization Perspective on Meta-Complexity — Question 12

Meta-complexity problems ask how much computational description is needed to represent a function or a string. The selected question asks whether an appropriate gap version of minimum circuit size or time-bounded description complexity admits a computational zero-knowledge proof system unconditionally. There is a tempting argument that an easy problem needs little proof, while a hard one might supply the one-way functions used to build zero knowledge. The missing case is worst-case hardness without the average-case hardness needed for that cryptographic implication. Closing this gap would connect structural complexity of descriptions with the ability to verify claims without revealing their witnesses.

[Read in atlas](index.html#TCS-4754) · [A Relativization Perspective on Meta-Complexity](https://doi.org/10.4230/LIPIcs.STACS.2022.54)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4803 — Limits on the Power of Private Constrained PRFs — Explicit open question on PDF page 3

Private constrained pseudorandom functions restrict evaluations to an authorized set while also hiding information about the predicate describing that set. The selected question asks whether security for a single constrained key is enough to construct public-key-style primitives such as secret-key agreement. The source proves a black-box separation: an oracle can support these constrained functions while still preventing key agreement. That result limits a broad class of generic constructions but does not settle every possible non-black-box implication. The record therefore concerns both the underlying relationship between primitives and the specific construction barrier established in the cited paper.

[Read in atlas](index.html#TCS-4803) · [Limits on the Power of Private Constrained PRFs](https://doi.org/10.4230/LIPIcs.ITC.2026.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4950 — Towards Separating Computational and Statistical Differential Privacy — Unresolved-question passage on page 20

Differing-inputs obfuscation aims to hide which circuit was encoded when finding an input that distinguishes the circuits is computationally difficult. The cited 2023 passage asks whether the existence assumptions called plain-diO and public-coin diO imply one another. They impose different conditions on the circuit sampler and the auxiliary information available to an adversary. Comparing these assumptions would clarify which cryptographic foundations suffice for applications, including separations between computational and statistical differential privacy. The distinction is subtle because restricting the sampler and revealing its random coins affect different parts of the security requirement.

[Read in atlas](index.html#TCS-4950) · [Towards Separating Computational and Statistical Differential Privacy](https://doi.org/10.1109/FOCS57990.2023.00042)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4974 — Detecting and Correcting Computationally Bounded Errors: A Simple Construction Under Minimal Assumptions — Explicit open question on PDF page 6

Error-correcting codes can exploit the assumption that an adversary modifying transmitted data has limited computation. The cited source achieves strong detection and correction guarantees over sufficiently large constant alphabets using minimal cryptographic assumptions. The selected direction asks for comparably optimal results over the binary alphabet. Existing binary constructions use stronger assumptions or a supplied seed, leaving randomized and self-seeded variants as distinct challenges. Resolving these cases would show how much of the computational advantage against errors can be retained in the most basic bit-based communication setting.

[Read in atlas](index.html#TCS-4974) · [Detecting and Correcting Computationally Bounded Errors: A Simple Construction Under Minimal Assumptions](https://doi.org/10.4230/LIPIcs.ITCS.2025.88)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5013 — Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation — Explicit open question on PDF page 2

Pre-distributed correlated randomness can reduce how much two parties need to communicate during secure computation. The selected problem asks whether communication can be sublinear in the circuit size while both running time and the correlated-randomness supply stay polynomial in the input length. The source proves strong setup lower bounds for protocols that push online communication all the way to its optimum. Those extreme-case lower bounds leave room between ordinary circuit-size communication and full communication optimality. Understanding that intermediate regime would identify whether practical preprocessing can buy a substantial communication saving under perfect security.

[Read in atlas](index.html#TCS-5013) · [Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation](https://doi.org/10.4230/LIPIcs.ITC.2023.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5015 — On the Computational Hardness Needed for Quantum Cryptography — Explicit open question on PDF page 1

Classical computational cryptography is organized around one-way functions as a basic necessary resource for many tasks. Quantum cryptography may rely on different forms of hardness, motivating the search for an analogous minimal primitive. The cited paper studies pairs of efficiently generated quantum states that are statistically far apart but computationally difficult to distinguish. It shows that these EFI pairs follow from many quantum cryptographic tasks and can also support significant zero-knowledge constructions. The entry introduces this foundational question together with that partial characterization, without asserting a universal equivalence covering every conceivable quantum primitive.

[Read in atlas](index.html#TCS-5015) · [On the Computational Hardness Needed for Quantum Cryptography](https://doi.org/10.4230/LIPIcs.ITCS.2023.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5793 — Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness — Explicit open question on PDF page 7

Learning algorithms and pseudorandom functions express competing possibilities for understanding an unknown efficiently computable function. The selected question asks whether the ordinary failure of efficient learning already implies pseudorandom functions within the same circuit class. Earlier implications require a hard distribution over targets, which is stronger than saying that every learner fails on some target. The cited paper establishes a general equivalence in a nonuniform exponential-security regime, leaving those qualifications essential to its result. Extending the connection beyond that regime would explain when learning hardness alone supplies cryptographic pseudorandomness.

[Read in atlas](index.html#TCS-5793) · [Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness](https://doi.org/10.4230/LIPIcs.CCC.2017.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6692 — Construct cryptographic PRGs from arbitrary one-way functions with seed length linear in input length.

Pseudorandom generators expand a short random seed into a longer string that efficient observers cannot distinguish from uniform randomness. General one-way functions are known to imply such generators, but the quantitative loss in seed length can be substantial. This problem asks for a fully explicit construction whose seed is only linear in the input length of the underlying one-way function while retaining the specified security dependence. The source contrasts arbitrary one-way functions with one-way permutations, where the desired kind of construction is already available. A tighter reduction would preserve much more of the original function's hardness when converting it into pseudorandomness.

[Read in atlas](index.html#TCS-6692) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6871 — Base unbounded FHE solely on worst-case complexity assumptions.

Unbounded fully homomorphic encryption supports arbitrarily deep permitted computations on ciphertexts. The source asks to base such a scheme solely on worst-case complexity assumptions. Some constructions require additional assumptions about encryptions of secret-key-related information to enable repeated refresh operations. Removing those extra premises would connect the security guarantee more directly to foundational hard problems. The saved 2016 note does not name the precise extra assumptions or compactness conventions, so its current status and exact target require separate review rather than treating any lattice-based FHE scheme as a resolution.

[Read in atlas](index.html#TCS-6871) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6953 — Do worst-case or average-case hardness assumptions imply one-way functions, or trapdoor functions?

Cryptographic hardness must occur on instances that honest users can efficiently generate, rather than only on a difficult exceptional input. The cited question asks whether P ≠ NP, or a suitable average-case separation between distributional classes, already implies one-way functions. It also asks about the stronger possibility of trapdoor functions, where secret information enables inversion that remains hard publicly. These targets add progressively more structure to a bare claim that efficient algorithms cannot solve everything. Establishing the implications would connect cryptographic foundations to broad complexity assumptions instead of relying on individual number-theoretic or algebraic candidates.

[Read in atlas](index.html#TCS-6953) · [Mathematics and Computation](https://www.math.ias.edu/avi/book)
Existing status: `source_open` · Summary written: 2026-09-11

## Quantum computation and information (85)

### TCS-6446 — Quantum PCP: a constant promise gap for local Hamiltonians

The quantum PCP conjecture asks whether even a coarse estimate of a quantum system's lowest energy can capture the difficulty of verifying quantum proofs. The system is specified by local interactions, each involving only a bounded number of qubits. The target is hardness for distinguishing two possible ground energies separated by a constant after normalizing the total interaction strength. Normalization prevents a small gap from becoming a constant merely by multiplying the Hamiltonian by a large number. The problem connects robust quantum verification with entanglement, quantum codes, and the limits of approximation algorithms.

[Read in atlas](index.html#TCS-6446) · [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495) · [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0036 — Does BPP differ from BQP?

This problem asks whether efficient quantum computation can decide something that efficient randomized classical computation cannot. BPP and BQP both require a reliable yes-or-no answer on every input, with bounded probability of error. Quantum interference gives promising candidate advantages, including the algorithms underlying factoring, but those examples do not establish an unconditional classical lower bound. Separations using special oracles or restricted classical circuits concern narrower comparisons. Settling the ordinary class separation would identify whether quantum computers enlarge the set of efficiently decidable problems at its most basic level.

[Read in atlas](index.html#TCS-0036) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027v2) · [Oracle Separation of BQP and PH](https://doi.org/10.1145/3530258) · [Unconditional Quantum Advantage for Sampling with Shallow Circuits](https://quantum-journal.org/papers/q-2026-08-12-2188/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6516 — An entanglement entropy area law for general gapped two-dimensional Hamiltonians

An area law says that entanglement between a region and its surroundings grows with the region's boundary rather than its volume. This problem asks for such a bound for the unique ground state of a general two-dimensional local Hamiltonian with a fixed positive spectral gap. Interaction strength, local dimension, and interaction range are held fixed as the lattice grows. Known routes involving frustration-free systems or additional conditions do not automatically establish the unrestricted statement recorded here. A solution would clarify how strongly locality and an energy gap constrain many-body quantum states, without by itself supplying an efficient algorithm to find them.

[Read in atlas](index.html#TCS-6516) · [An Area Law for One Dimensional Quantum Systems](https://arxiv.org/abs/0705.2024v4) · [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492v3) · [Entanglement spread area law in gapped ground states](https://doi.org/10.1038/s41567-022-01740-7) · [Area Laws and Tensor Networks for Maximally Mixed Ground States](https://doi.org/10.1007/s00220-026-05554-z) · [Quantum matter is weakly entangled at low energies](https://arxiv.org/abs/2604.14143v1) · [Two-dimensional local Hamiltonian problem with area laws is QMA-complete](https://doi.org/10.1016/j.jcp.2021.110534)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6580 — Information-theoretic classical verification of quantum computation

A classical user would like to check a computation performed by a single quantum device using only classical messages. The honest device must be able to carry out the verification protocol in quantum polynomial time. The difficult requirement is soundness against any cheating device, including a computationally unbounded one. Existing approaches may instead give the user limited quantum capabilities, use separated devices, or assume that a cryptographic problem is hard. The question isolates whether an entirely classical client can obtain unconditional trust in efficient quantum computation under this single-device model.

[Read in atlas](index.html#TCS-6580) · [Verification of quantum computation: An overview of existing approaches](https://arxiv.org/abs/1709.06984) · [IP = PSPACE](https://doi.org/10.1145/146585.146609) · [Interactive Proofs for Quantum Computations](https://arxiv.org/abs/1704.04487) · [A classical leash for a quantum system: Command of quantum systems via rigidity of CHSH games](https://arxiv.org/abs/1209.0448) · [Classical Verification of Quantum Computations](https://arxiv.org/abs/1804.01082) · [How to Classically Verify a Quantum Cat without Killing It](https://arxiv.org/abs/2602.09282) · [Verification of Quantum Computations Without Trusted Preparations or Measurements](https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202501018) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6518 — Does NPT bound entanglement exist?

Entangled states can sometimes be converted into nearly perfect shared Bell pairs using many copies and local operations with classical communication. Bound entanglement means that this distillation remains impossible despite the presence of entanglement. The question asks whether such states can have a negative partial transpose, a spectral property associated with distillability in simpler settings. Failure of a protocol on one copy or any fixed number of copies does not establish the required obstruction for every number of copies. Resolving the question would sharpen the distinction between entanglement as a property and entanglement as a usable communication resource.

[Read in atlas](index.html#TCS-6518) · [Mixed-state entanglement and distillation: is there a “bound” entanglement in nature?](https://arxiv.org/abs/quant-ph/9801069) · [Evidence for Bound Entangled States with Negative Partial Transpose](https://arxiv.org/abs/quant-ph/9910026) · [A solution to 2-copy distillability of Werner states](https://arxiv.org/abs/2607.21367) · [On the two-copy distillability of Werner states and a new partial trace inequality](https://arxiv.org/abs/2607.24309) · [Two-copy nondistillability of Werner states: sharp partial-trace inequalities and finite-copy extensions](https://arxiv.org/abs/2607.24479) · [Sharp Plucker Geometry for Three-Copy Werner Distillation](https://arxiv.org/abs/2608.02647)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6515 — Asymptotically good quantum locally testable stabilizer codes

A locally testable quantum code should reveal a substantial error by checking only a few qubits. The desired family must also encode a linear amount of quantum information and tolerate errors on a linear number of physical qubits. Each check and each qubit's participation in checks must remain bounded as the code grows. These requirements strengthen ordinary good quantum LDPC codes by demanding a quantitative relation between distance from the code space and rejection probability. Such codes would connect robust quantum error detection with the complexity of low-energy states and the broader search for quantum PCP constructions.

[Read in atlas](index.html#TCS-6515) · [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/) · [Asymptotically Good Quantum and Locally Testable Classical LDPC Codes](https://arxiv.org/abs/2111.03654) · [Local testability of distance-balanced quantum codes](https://www.nature.com/articles/s41534-024-00908-8) · [Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes](https://arxiv.org/abs/2402.07476) · [NLTS Hamiltonians from Good Quantum Codes](https://arxiv.org/abs/2206.13228) · [Transversal non-Clifford gates on almost-good quantum LDPC and quantum locally testable codes](https://arxiv.org/abs/2604.01874) · [Probabilistically Checking Quantum Proofs, with Interaction](https://arxiv.org/abs/2606.09588)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6517 — Passive quantum memory in three dimensions — claimed resolution

Passive quantum memory aims to preserve an encoded qubit through the natural dynamics of a material without repeated active correction. The question here fixes a nonzero temperature and asks whether lifetime can grow without bound in a three-dimensional local stabilizer system. Protecting a qubit requires retaining phase information as well as distinguishing its classical basis states. The saved card records a May 2026 claimed affirmative construction, while distinguishing its proof claim from an independently verified conclusion. This makes the record a useful guide to the precise thermal model and remaining verification questions rather than an unqualified assertion that the original existence problem is still open.

[Read in atlas](index.html#TCS-6517) · [Thermodynamic stability criteria for a quantum memory based on stabilizer and subsystem codes](https://arxiv.org/abs/0907.2807) · [Quantum memories at finite temperature](https://arxiv.org/abs/1411.6643) · [Symmetry protected self correcting quantum memory in three space dimensions](https://arxiv.org/abs/2103.08622) · [Cored product codes for quantum self-correction in three dimensions](https://arxiv.org/abs/2510.05479) · [A passive self-correcting quantum memory in three dimensions](https://arxiv.org/abs/2605.10943) · [Partial Self-Correction in Layer Codes](https://journals.aps.org/prl/abstract/10.1103/mb89-8436)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6519 — Exact quantum capacity of the qubit depolarizing channel

A depolarizing channel models a qubit subjected to randomly chosen Pauli errors. Its quantum capacity measures how much unknown quantum information can be transmitted reliably per channel use when many uses are encoded together. The goal is an exact capacity formula throughout the noise range under the unassisted coding convention fixed in the card. Coding across several uses can behave differently from optimizing a single use, which complicates attempts to match achievable rates with impossibility bounds. Understanding this basic symmetric noise model would provide a benchmark for quantum communication and the value of collective error correction.

[Read in atlas](index.html#TCS-6519) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Quantum cloning and the capacity of the Pauli channel](https://arxiv.org/abs/quant-ph/9803058) · [Quantum and private capacities of low-noise channels](https://arxiv.org/abs/1705.04335) · [Geometric optimization for quantum communication](https://arxiv.org/abs/2509.15106) · [Enhanced quantum capacity thresholds from symmetry](https://arxiv.org/abs/2605.09138) · [A certified lower bound on the quantum-capacity threshold of the depolarizing channel](https://arxiv.org/abs/2608.15870) · [Sharp Quantum Capacity Thresholds: Exponential Strong Converses for Degradable and Antidegradable Channels](https://arxiv.org/abs/2608.01308)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0037 — NP outside BQP

This problem asks whether quantum computers still face an unavoidable efficient-computation barrier on some NP problems. An equivalent target is to rule out a bounded-error polynomial-time quantum algorithm for every instance of Boolean satisfiability. Fast quantum algorithms for structured tasks do not imply an algorithm for general NP-complete search or decision problems. Likewise, a speedup for searching an unstructured list addresses a particular access model rather than the full complexity-class question. A resolution would delimit the reach of quantum computation on problems whose proposed solutions are easy to check classically.

[Read in atlas](index.html#TCS-0037) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027) · [A fast quantum mechanical algorithm for database search](https://arxiv.org/abs/quant-ph/9605043) · [Strengths and Weaknesses of Quantum Computing](https://arxiv.org/abs/quant-ph/9701001) · [Complexity of detecting large coefficients in the Pauli basis](https://arxiv.org/abs/2606.19545)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6448 — Does a quantum witness have more power than a classical witness?

A quantum verifier may receive either a quantum state or a classical string as evidence that an input is a yes-instance. QMA permits the former kind of witness, while QCMA restricts the witness to classical information. The question asks whether this change in the form of the evidence changes what can be verified efficiently. Both models already allow quantum computation during verification, so the issue is the additional power of the witness itself. An answer would clarify whether quantum states can serve as fundamentally stronger proofs in the ordinary setting without an oracle.

[Read in atlas](index.html#TCS-6448) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6520 — Computability of quantum channel capacity

Quantum channel capacity describes the best asymptotic rate for transmitting quantum information through a noisy channel. This problem asks whether that number can always be approximated by an algorithm from an effective finite description of the channel. The algorithm may be slow, but it must halt and meet any requested rational accuracy. Optimizations involving arbitrarily many channel uses make the asymptotic definition harder to turn into a guaranteed finite computation. Establishing computability or an obstruction would separate the existence of an operational communication rate from our ability to calculate it even in principle.

[Read in atlas](index.html#TCS-6520) · [The private classical capacity and quantum capacity of a quantum channel](https://arxiv.org/abs/quant-ph/0304127) · [Continuity of quantum channel capacities](https://arxiv.org/abs/0810.4931) · [Unbounded number of channel uses may be required to detect quantum capacity](https://www.nature.com/articles/ncomms7739) · [Undecidability in Physics: a Review](https://arxiv.org/abs/2410.16532) · [Undecidability in physics: A review — journal version](https://doi.org/10.1016/j.physrep.2025.06.004) · [On the undecidability of quantum channel capacities](https://arxiv.org/abs/2601.22471)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7166 — Polynomial-time quantum algorithms for the general hidden subgroup problem

Can a quantum algorithm recover a hidden subgroup of any finite group in polynomial total time? The oracle gives the same value exactly on each left coset of the hidden subgroup. The output must generate the entire subgroup. Polynomially many oracle calls are known to suffice, but their processing may be inefficient. The broad import still needs a precise group representation and access model before it is a complete computational statement.

[Read in atlas](index.html#TCS-7166) · [The quantum query complexity of the hidden subgroup problem is polynomial](https://arxiv.org/abs/quant-ph/0401083) · [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6521 — A polynomial-time quantum algorithm for the dihedral hidden subgroup problem

The dihedral hidden subgroup problem presents a function that is constant on cosets of an unknown subgroup of a dihedral group. The task is to recover generators for that subgroup using quantum access to the function. The target is a uniform algorithm whose total running time is polynomial in the length of the group description and oracle values. Counting only a small number of oracle queries is insufficient if processing the resulting quantum information is expensive. An efficient solution would extend the reach of hidden-subgroup methods beyond the abelian setting and illuminate connections with lattice-related algorithmic problems.

[Read in atlas](index.html#TCS-6521) · [Another subexponential-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333) · [A Subexponential-Time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345) · [The dihedral hidden subgroup problem](https://arxiv.org/abs/2106.09907) · [A Subexponential Time Algorithm for the Dihedral Hidden Subgroup Problem with Polynomial Space](https://arxiv.org/abs/quant-ph/0406151) · [Quantum Computation and Lattice Problems](https://cims.nyu.edu/~regev/papers/quantum_average.pdf) · [A Quantum Polynomial-Time Solution to The Dihedral Hidden Subgroup Problem](https://arxiv.org/abs/2202.09697) · [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591) · [The ePrint:2026/1591 Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693) · [Rigorous Statements and Proofs of the Lemmas in Simon's Algorithm for the Dihedral Coset Problem and Their Underlying Hypothesis](https://arxiv.org/abs/2608.16598) · [The Hidden Subgroup Problem in Semidirect Products and Quasi-Hamiltonian Groups](https://arxiv.org/abs/2608.05321)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6522 — Graph isomorphism in BQP

Two graphs are isomorphic when a relabeling of vertices preserves every edge. This question asks whether a quantum algorithm can decide that equivalence in polynomial time for every pair of explicitly given graphs. The algorithm must include all processing costs and achieve bounded error, rather than merely extract a small amount of information from an oracle. Symmetry makes graph isomorphism a natural testing ground for quantum methods, but quantum access to related group structure is not itself a complete algorithm. A resolution would clarify whether quantum computation can efficiently handle this central classification problem.

[Read in atlas](index.html#TCS-6522) · [Ten Semi-Grand Challenges for Quantum Computing Theory](https://www.scottaaronson.com/writings/qchallenge.html) · [A Quantum-Inspired Algorithm for Graph Isomorphism](https://arxiv.org/abs/2512.24423) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/update.html) · [Limitations of Quantum Coset States for Graph Isomorphism](https://arxiv.org/abs/quant-ph/0511148) · [Quantum state isomorphism problems for groups](https://arxiv.org/abs/2605.12615) · [NPA Hierarchy for Quantum Isomorphism and Homomorphism Indistinguishability](https://quantum-journal.org/papers/q-2026-01-28-1989/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7165 — The no low-energy sampleable states conjecture

Can a family of local Hamiltonians keep every classically accessible state a fixed normalized energy above the ground energy? The source’s access model requires exact amplitude queries, exact measurement sampling and a succinct description with recognizable validity. Matching measurement distributions alone does not control quantum energy because phases matter. Known exclusions for stabilizer and fermionic Gaussian states address restricted classes. The mathematical family quantifiers are now explicit, while a complete numerical machine specification remains unfinished.

[Read in atlas](index.html#TCS-7165) · [Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture](https://doi.org/10.1137/22M1513721) · [Local Hamiltonians with No Low-Energy Stabilizer States](https://arxiv.org/abs/2302.14755) · [Constructing Fermionic Hamiltonians with Non-Gaussianic low-energy states](https://arxiv.org/abs/2502.15368v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0029 — Maximum randomized-versus-quantum gap for total functions

Query complexity measures how many input bits an algorithm needs to inspect, while allowing other computation for free. This problem compares bounded-error randomized and quantum query complexity for Boolean functions defined on every input. Aaronson's saved survey describes examples approaching a cubic separation and an upper bound with exponent four. The target is the largest possible separation, so finding either more extreme functions or a sharper universal upper bound would address the gap. Requiring total functions distinguishes this question from promise problems, where special input structure can permit much larger quantum advantages.

[Read in atlas](index.html#TCS-0029) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6449 — Quantum versus classical nonuniform advice

Advice is information supplied in advance that depends on input length but must work for every input of that length. A quantum algorithm might receive a polynomial-size quantum advice state or only a polynomial-length classical string. The question is whether quantum advice allows it to decide more languages efficiently than classical advice does. Advice is nonuniform and need not be efficiently generated, so the comparison concerns its information content rather than its preparation cost. A separation or simulation would reveal how much computational value can be carried by a reusable description of a length-specific quantum state.

[Read in atlas](index.html#TCS-6449) · [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0033 — Quantum query complexity versus bounded approximate degree

The polynomial method bounds quantum query complexity using low-degree polynomials that approximate a function's output. This problem considers partial Boolean functions, whose inputs are subject to a promise. The approximating polynomial must still remain bounded on all Boolean inputs, including those outside the promise. The question asks how large the gap between this bounded approximate degree and actual quantum query complexity can become, potentially even exponentially large. Such a gap would expose a limitation of representing the behavior of a quantum algorithm by its acceptance polynomial alone.

[Read in atlas](index.html#TCS-0033) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0861 — Is QMA(2) in BQEXP?

QMA(2) allows a quantum verifier to receive two witnesses promised to be unentangled with each other. The question asks whether every problem with such a proof system can be decided by a bounded-error quantum algorithm in exponential time. The saved source contrasts this proposed BQEXP upper bound with a nondeterministic exponential-time upper bound. Exploiting the independence of the witnesses is difficult because it restricts possible proofs without turning them into ordinary classical certificates. A better upper bound would locate the computational power of unentangled quantum proofs more precisely among large complexity classes.

[Read in atlas](index.html#TCS-0861) · [TCS Open Problems](https://tcsopenproblems.com/problem/9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6447 — Strong quantum IOPs with polynomial communication

Interactive oracle proofs let a verifier inspect only selected parts of much larger prover messages. This question asks for constant-round quantum versions that verify all QMA promise problems with polynomial total communication and only constantly many queries. The strong quantum access model is part of the target, because different ways of querying quantum messages permit different verification strategies. Soundness must cover arbitrary prover behavior, while the verifier remains efficient and has a constant completeness-soundness gap. The project probes how far proof compression and local checking can extend when the evidence itself is quantum.

[Read in atlas](index.html#TCS-6447) · [Quantum Interactive Oracle Proofs](https://arxiv.org/abs/2601.12874)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0031 — Oracle separation of BQP from IP

A classical interactive proof lets a verifier check answers supplied by a prover through a polynomial-length conversation. This problem asks for one oracle relative to which a quantum polynomial-time language has no such proof, even with an unrestricted prover. The quantum algorithm may query the oracle in superposition, whereas the classical verifier queries ordinary strings. The 2026 relativizing containment in the multiple-prover class MIP leaves the single-prover question open in that source. A separation would demonstrate a limit on classical verification of quantum computations through arbitrary oracle interfaces.

[Read in atlas](index.html#TCS-0031) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0034 — Quantum query–space tradeoffs for collisions and distinctness

Collision and element distinctness problems ask whether an input function repeats an output, under different promises on the input. Quantum algorithms can reduce the number of queries, but their best query performance may require substantial stored information. This project asks for the optimal tradeoff between queries and memory, separating quantum workspace from classical memory where relevant. The source specifically raises whether nearly optimal query bounds remain possible with little memory and whether coherently accessible classical storage can replace qubits. Matching algorithms and lower bounds would make quantum speedups more meaningful under realistic storage constraints.

[Read in atlas](index.html#TCS-0034) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0862 — Is QRG with constant rounds in PSPACE?

Quantum refereed games model a verifier interacting with opposing provers, one trying to obtain acceptance and the other rejection. The number of interaction rounds can change the power of the resulting proof system. This problem asks whether every game with a fixed constant number of rounds can be decided using polynomial space. The saved source contrasts the one-round case with the stronger class obtained when polynomially many rounds are available. Understanding the intermediate regime would show how quickly repeated quantum interaction increases the complexity of adversarial verification.

[Read in atlas](index.html#TCS-0862) · [TCS Open Problems](https://tcsopenproblems.com/problem/13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0866 — Learning Quantum Circuits with Queries

The learning task is to predict the behavior of an unknown quantum circuit by making specially permitted queries to it. Kun and Reyzin formulate a model using value-injection queries, which allow interventions in the circuit rather than only ordinary input-output examples. The challenge is to determine how efficiently a learner can identify the relevant behavior under that access model. Their preliminary analysis suggests that a test-path argument used for classical circuits does not transfer directly to the quantum setting. The project studies how interference changes the relationship between experimentally probing a computational device and learning a usable description of it.

[Read in atlas](index.html#TCS-0866) · [COLT / PMLR](https://proceedings.mlr.press/v40/Kun15.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0027 — Black-box unitary synthesis

An arbitrary unitary transformation may require an enormous circuit when described directly. This question asks whether access to a suitably chosen classical Boolean oracle can always make that transformation efficiently implementable by a quantum computer. The oracle may depend on the unitary, but the implementation must act correctly on arbitrary input states. Aaronson's survey distinguishes this from preparing one chosen state or reproducing the unitary on only a few basis vectors. The problem tests whether difficult quantum transformations can always be made easy by supplying enough classical black-box information.

[Read in atlas](index.html#TCS-0027) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0858 — Complexity of the EPR Hamiltonian

The EPR Hamiltonian problem studies a graph of qubits with Bell-state interactions on its edges. The intended research direction is to understand the computational complexity of optimizing the energy when entangled states are allowed. The saved discussion contrasts simple product-state strategies with potentially more powerful collective quantum states. Its ground-energy wording and projector convention need to be checked against the underlying Hamiltonian reference before turning this outline into a precise decision problem. Resolving the correctly specified model would clarify whether this structured interaction family is easier than general quantum Hamiltonian optimization.

[Read in atlas](index.html#TCS-0858) · [TCS Open Problems](https://tcsopenproblems.com/problem/2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0860 — Find the complexity of Quantum Approximate Counting (QXC)

Quantum approximate counting asks about the dimension of an accepting subspace of a quantum verifier. In the saved formulation, one counts eigenvectors of the acceptance operator whose eigenvalues are at least two thirds. The decision task distinguishes a dimension at least a threshold from one at most half that threshold, under the stated promise. The source asks for sharper upper or lower complexity bounds and for the behavior of the complementary problem. This would extend our understanding of witness counting from classical certificates to families of quantum states.

[Read in atlas](index.html#TCS-0860) · [TCS Open Problems](https://tcsopenproblems.com/problem/12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0030 — Oracle separation of BQP from efficient-prover interactive proofs

An efficient quantum computation can have a classical interactive proof whose honest prover is too expensive for the quantum device to execute. This problem asks for an oracle relative to which some quantum polynomial-time language has no classical interactive proof with a quantum polynomial-time honest prover. The verifier and honest prover access the same classical oracle, with quantum queries available only to the quantum computation. Soundness must hold even against an unbounded dishonest prover, so computationally sound cryptographic arguments have a different guarantee. A separation would expose an oracle obstruction to classical verification using only the computational power of an efficient quantum device.

[Read in atlas](index.html#TCS-0030) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf) · [A Relativizing MIP for BQP](https://arxiv.org/abs/2604.11952)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0028 — Injective quantum oracles: standard versus erasing access

A standard quantum oracle keeps the query input while writing the function value into another register. An erasing oracle for an injective function instead replaces the input register by its image. This problem asks whether some properties are easy to learn with standard access but hard with erasing access. Retaining the input can enable an algorithm to reverse a computation and remove unwanted auxiliary information, a capability that may be lost in the erasing model. A separation would show that apparently minor choices in the oracle interface can fundamentally change quantum query power.

[Read in atlas](index.html#TCS-0028) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1259 — Exact quantum fanout in constant depth with unrestricted circuit size

Quantum fanout coherently flips every target qubit according to one control qubit. The problem asks whether one constant depth bound can implement it exactly using arbitrary one-qubit and generalized Toffoli gates. The circuit may have any finite size and any finite number of clean ancillas. Superposition inputs must be handled correctly and the ancillas must return to zero. An exact construction or an impossibility theorem would determine whether this basic operation lies beyond the expressive power of the shallow gate model.

[Read in atlas](index.html#TCS-1259) · [Random Unitaries in Constant (Quantum) Time](https://doi.org/10.4230/LIPIcs.ITCS.2026.61)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1298 — Every element of the Clifford hierarchy is generalized semi-Clifford.

The Clifford hierarchy organizes quantum gates by how conjugation transforms simpler Pauli operations. A generalized semi-Clifford form expresses a gate using Clifford changes of basis together with permutation and diagonal structure. This conjecture asks whether every gate anywhere in the hierarchy admits such a representation. The cited work studies permutation gates in the third level, providing a concrete setting in which to examine the broader structural claim. A characterization would make the hierarchy more explicit and help explain which algebraic ingredients underlie useful fault-tolerant quantum operations.

[Read in atlas](index.html#TCS-1298) · [Characterization of Permutation Gates in the Third Level of the Clifford Hierarchy](https://doi.org/10.4230/LIPIcs.TQC.2026.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1324 — Quantum games PCP with efficient honest provers and short messages

The question asks whether every quantum-verifiable problem has a short classical game with entangled provers. Both questions and answers must have polylogarithmic length, with a constant completeness–soundness gap. Honest provers must prepare their entanglement and answer in polynomial time given copies of a polynomial-size witness. Soundness must hold even against computationally unrestricted cheating provers. Existing unrestricted entangled proof systems and the source’s streaming Hamiltonian result do not establish this efficient-prover communication target.

[Read in atlas](index.html#TCS-1324) · [Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2026.15) · [The status of the quantum PCP conjecture (games version)](https://arxiv.org/abs/2403.13084v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1341 — Are symmetric quantum circuits universal for every finite group action?

A unitary can respect a symmetry even when a chosen gate decomposition does not. This question asks whether every symmetry-preserving unitary has a circuit whose layers themselves preserve the symmetry. The model permits threshold gates, arbitrary one-qubit gates and clean workspace that may also be permuted. Universality is known for independent full permutations within blocks, including the full permutation group. The open target is exact full-space implementation for every finite group action, without a size or depth bound.

[Read in atlas](index.html#TCS-1341) · [Symmetric Quantum Computation](https://doi.org/10.4230/LIPIcs.ITCS.2026.35) · [Symmetric quantum computation — full version](https://arxiv.org/abs/2501.01214v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1342 — Cloning random-circuit states without first learning their circuits

An unknown random circuit prepares a quantum state, and the algorithm receives only polynomially many copies of that state. The task is to output one more copy while keeping the whole joint output close to the desired tensor product. Universal cloning has global fidelity (k+1)/(2ⁿ+k), which is exponentially small for polynomially many input copies. The source asks whether circuit structure permits better direct cloning, even in subexponential time. A concrete circuit ensemble, fidelity and success target, and comparison with learning-based algorithms still need to be specified.

[Read in atlas](index.html#TCS-1342) · [The Hardness of Learning Quantum Circuits and Its Cryptographic Applications](https://doi.org/10.4230/LIPIcs.ITCS.2026.56) · [Optimal cloning of pure states](https://doi.org/10.1103/PhysRevA.58.1827)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1490 — Our protocol moreover relies on the no-PE assumption for soundness; if malicious provers are allowed to share unbounded prior entanglement, known techniques for instantaneous non-local […]

Position-based proof systems use constraints on where participants are located and when they can communicate. The cited quantum protocol obtains additional power under a restriction forbidding shared prior entanglement among malicious provers. This question asks whether allowing unbounded prior entanglement collapses the relevant protocol's power to the polynomial-space regime identified in the classical comparison. Instantaneous nonlocal computation suggests a cheating strategy, but the source leaves the corresponding collapse proof unfinished. The issue separates benefits of quantum communication from benefits that depend on a physical limitation on the adversaries' initial resources.

[Read in atlas](index.html#TCS-1490) · [Quantum Advantage in Proof Systems Without Entanglement](https://doi.org/10.4230/LIPIcs.ICALP.2026.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1882 — Any algorithm that distinguishes p = ud from dTV (p, ud ) > ε with success probability at least .99 requires Ω(min{d1/3 /ε4/3 , d1/2 […]

Uniformity testing asks whether an unknown distribution is exactly uniform or noticeably far from uniform. Here the algorithm receives access to the code that generates the distribution, enabling quantum operations beyond ordinary independent sampling. The conjecture proposes a lower bound matching the paper's algorithm across both domain size and distance parameter. It further asks for that obstruction in a stronger quantum string-oracle model. Proving the joint parameter dependence would determine how much useful information quantum access to a sampler can provide for this basic statistical test.

[Read in atlas](index.html#TCS-1882) · [Uniformity Testing When You Have the Source Code](https://doi.org/10.4230/LIPIcs.TQC.2025.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1955 — Then we ask, is W≥t [F ] ∈ O(exp(−t))?

The circuit model first performs shallow quantum processing and then applies a constant-depth classical Boolean circuit. Its randomized output can be averaged to obtain a real-valued function on classical inputs. This question asks whether the Fourier weight on high-degree terms decays exponentially, in the spirit of classical low-degree concentration theorems. Such decay would constrain how strongly the combined computation can depend on complicated global input correlations. The project seeks a structural explanation of the limits of shallow quantum preprocessing, extending beyond a lower bound for one particular function such as parity.

[Read in atlas](index.html#TCS-1955) · [Parity vs. AC0 with Simple Quantum Preprocessing](https://doi.org/10.4230/LIPIcs.ITCS.2024.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1961 — Are OWSGs and EFI pairs (or PRSGs) equivalent?

One-way state generators produce quantum states whose generating secrets are hard to recover. EFI pairs and pseudorandom state generators express related forms of quantum indistinguishability. This question asks whether these search-type and decision-type cryptographic resources can be constructed from one another. The classical analogy between one-way functions and pseudorandom generators motivates the comparison, but quantum outputs introduce separate issues of verification and access to copies. Establishing equivalences or separations would organize the basic assumptions needed for computational quantum cryptography.

[Read in atlas](index.html#TCS-1961) · [One-Wayness in Quantum Cryptography](https://doi.org/10.4230/LIPIcs.TQC.2024.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2229 — What is the relationship of QMA and QMA(2)?

QMA uses a single quantum witness, while QMA(2) permits two witnesses that must be unentangled across a specified division. This question asks how much verification power that unentanglement promise adds. The cited work studies proofs with restricted relative phases and finds that nearby models can have very different complexity. Those results do not directly establish equality or separation for ordinary QMA and QMA(2). Understanding the relationship would isolate whether independently supplied quantum proofs provide an advantage unavailable to one unrestricted quantum certificate.

[Read in atlas](index.html#TCS-2229) · [Quantum Merlin-Arthur and Proofs Without Relative Phase](https://doi.org/10.4230/LIPIcs.ITCS.2024.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2408 — For instance, would it be possible to perform an RSP-like protocol assuming only the existence of quantum-secure one-way functions?

Remote state preparation lets a classical party induce useful quantum states at another device through an interactive protocol. The cited construction obtains this functionality from a Learning With Errors assumption and uses it to replace quantum communication in cryptographic protocols. This question asks whether quantum-secure one-way functions alone could support a sufficiently strong version of the same primitive. The source explains that such a construction would have further consequences for secure two-party computation with classical communication. The goal is to identify the minimum cryptographic assumptions behind remote preparation, including a possible impossibility result for the proposed weakening.

[Read in atlas](index.html#TCS-2408) · [Quantum Cryptography with Classical Communication: Parallel Remote State Preparation for Copy-Protection, Verification, and More](https://doi.org/10.4230/LIPIcs.ICALP.2023.67)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2451 — It is worth mentioning that it is unknown whether the adaptive postselection can be efficiently done in PostBQP as discussed in [2].

Postselection permits a computation to condition on a specified measurement outcome, even when that outcome is unlikely. Adaptive postselection additionally allows later choices of conditioning to depend on earlier measurement results. This question asks whether ordinary PostBQP can efficiently reproduce the adaptive version considered in the paper. The distinction appears alongside formal models of quantum rewinding and cloning, where changing the permitted operation can change computational power. A simulation or separation would clarify whether adaptivity adds a resource beyond the usual idealized power of quantum postselection.

[Read in atlas](index.html#TCS-2451) · [Rewindable Quantum Computation and Its Equivalence to Cloning and Adaptive Postselection](https://doi.org/10.4230/LIPIcs.TQC.2023.9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2650 — Assuming QETH or QSETH, is MQCSP, UMCSP, or SMCSP quantumly hard?

Quantum variants of the minimum circuit size problem ask whether a given object has a small quantum implementation. The source distinguishes tasks involving Boolean computations, unitary transformations, and quantum state preparation. This question asks whether quantum exponential-time hypotheses can yield hardness results for these minimization problems. The reductions must connect the assumed hardness of quantum satisfiability-related computation with detecting a short circuit description. Such results would place quantum circuit minimization within fine-grained complexity and explain whether succinctness itself remains difficult to recognize on a quantum computer.

[Read in atlas](index.html#TCS-2650) · [Quantum Meets the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.ITCS.2022.47)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2707 — The main obstacle comes from the non-commutativity of Hamiltonians and it remains open to design a polynomial-time algorithm for such partition function assuming only zero-freeness.

A quantum partition function aggregates contributions from a Hamiltonian describing the system's interactions. The source asks for a polynomial-time approximation algorithm assuming only the relevant zero-freeness condition. Zero-freeness supports analytic approximation methods, but quantum interaction terms need not commute with one another. Extending the guarantee to this setting would clarify how far analytic information alone can support efficient partition-function computation. The saved passage explicitly identifies noncommutativity as the obstacle, while leaving the precise zero-free region and Hamiltonian access assumptions to the cited paper.

[Read in atlas](index.html#TCS-2707) · [Polynomial-Time Approximation of Zero-Free Partition Functions](https://doi.org/10.4230/LIPIcs.ICALP.2022.108)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3275 — Error reduction of StoqMA remains open since this class was defined in 2006 [9] because this class does not permit amplification of gap between thresholds […]

StoqMA is a restricted quantum proof class motivated by Hamiltonians with nonnegative structure after the appropriate representation. Its verifier accepts valid and invalid inputs with probabilities separated by at least an inverse-polynomial gap. The question is whether that gap can be amplified efficiently while remaining within the same restricted verifier model. The usual strategy of repeating a test and taking a majority is not automatically an allowed StoqMA computation. A solution would clarify the robustness of the class definition and whether weakly distinguishable stoquastic proofs can be converted into strongly reliable ones.

[Read in atlas](index.html#TCS-3275) · [StoqMA Meets Distribution Testing](https://doi.org/10.4230/LIPIcs.TQC.2021.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3379 — The complexity of k-LH on a 1D line remains open for local dimension 2 ≤ d ≤ 7.

The local Hamiltonian problem asks whether the minimum energy of a quantum system lies below or above specified thresholds separated by a promise gap. Restricting interactions to a one-dimensional line greatly limits the geometry, but quantum states can still encode complicated computation. The source identifies local dimensions from two through seven as a gap in the complexity classification it surveys. It contrasts this range with a QMA-completeness result using eight-dimensional sites. The project is to determine how much local quantum state space is needed for hard ground-energy problems under the source's one-dimensional interaction restrictions.

[Read in atlas](index.html#TCS-3379) · [Oracle Complexity Classes and Local Measurements on Physical Hamiltonians](https://doi.org/10.4230/LIPIcs.STACS.2020.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3573 — Can we prove the conjecture that the purified and discrete query input models are equivalent for classical distributions, with respect to the query complexity of […]

Quantum distribution testing depends on exactly how an algorithm accesses the distribution. One model supplies a purification through a quantum preparation operation, while another supplies discrete query access to a classical description or sampling mechanism. This conjecture asks whether the two models have equivalent query power for testing properties of classical distributions. Algorithms and lower bounds proved in one interface need not transfer automatically to the other. An equivalence would unify complexity results across access conventions, while a separation would identify information provided by one oracle but absent from the other.

[Read in atlas](index.html#TCS-3573) · [Distributional Property Testing in a Quantum World](https://doi.org/10.4230/LIPIcs.ITCS.2020.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3709 — We do not know how to lift Q or Q0 to their analogous communication measures; this is likely to be significantly harder.

A lifting theorem transfers a lower bound for querying one input into a lower bound for communication between parties holding separate inputs. The transfer usually composes the original function with a small communication gadget. This question asks for such theorems for bounded-error and zero-error quantum query complexity. Simulating a query algorithm by communication is often straightforward, but proving that every communication protocol pays the corresponding cost is much harder. A quantum lifting theorem would let techniques for black-box algorithms establish communication lower bounds for a much wider family of problems.

[Read in atlas](index.html#TCS-3709) · [Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.TQC.2019.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4238 — Or, on the contrary, is the amount of certified randomness against no-signaling adversaries bounded also in the sequential scenario?

Sequential measurements can extract certified randomness from an entangled system while preserving some ability to use it again. The cited work analyzes this phenomenon against adversaries constrained by quantum mechanics. This question asks whether unbounded certified randomness remains possible against the broader class of adversaries constrained only by no-signaling. The geometry of the no-signaling correlation set differs from the quantum set used in the paper's argument. A bound or construction would determine how much repeated randomness certification depends on trusting quantum theory beyond the prohibition on faster-than-light signaling.

[Read in atlas](index.html#TCS-4238) · [A Single Entangled System Is an Unbounded Source of Nonlocal Correlations and of Certified Random Numbers](https://doi.org/10.4230/LIPIcs.TQC.2017.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4457 — We conjecture that the power of any two-qubit Hamiltonian obeys a dichotomy: either H is efficiently classicaly simulable in this model,

A fixed two-qubit interaction can be repeatedly applied to build a larger quantum computation. This conjecture asks whether every such interaction falls into one of two computational regimes in the source's model. One regime permits efficient classical simulation, while the other becomes universal when postselection is allowed. The cited classification proves this dichotomy for commuting Hamiltonians, but ancillary qubits and encoded subspaces complicate the general case. A complete classification would organize elementary interactions by computational power and rule out intermediate behavior between the proposed alternatives.

[Read in atlas](index.html#TCS-4457) · [Complexity Classification of Two-Qubit Commuting Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2016.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4469 — Is qq-QAM contained in BP · PP?

Generalized quantum Arthur–Merlin games allow different patterns of classical and quantum messages. This question concerns the class qq-QAM and asks whether it has an upper bound in BP·PP. The target would sharpen the broader two-message quantum interactive-proof upper bound cited in the paper. It requires translating the power of quantum exchanges into randomized access to a counting-related complexity class. Such a containment would help distinguish which parts of an interactive proof's power come from its message types and which from ordinary probabilistic verification.

[Read in atlas](index.html#TCS-4469) · [Generalized Quantum Arthur-Merlin Games](https://doi.org/10.4230/LIPIcs.CCC.2015.488)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4509 — A polynomial number of verifications is optimal for unconditionally secure schemes, nevertheless, a natural question that still remains open is whether we can have computationally […]

A quantum money token should survive legitimate verification while remaining difficult to counterfeit. This problem asks whether a secret-key scheme can support exponentially many verifications carried out through classical communication. The source contrasts that ambition with a polynomial limit for unconditionally secure schemes. Computational assumptions might allow more reuse, but the verification process must avoid gradually revealing or consuming enough information to defeat security. A construction or impossibility theorem would clarify the tradeoff between a token's lifetime, the verifier's interface, and the assumptions protecting it.

[Read in atlas](index.html#TCS-4509) · [New Constructions for Quantum Money](https://doi.org/10.4230/LIPIcs.TQC.2015.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4586 — While the query complexity of oracle identification in terms of M and N has been fully characterized, finding an optimal quantum algorithm for oip(C) remains […]

Oracle identification starts with a known candidate set of functions and asks which candidate an unknown oracle implements. General bounds in terms of the number of candidates and input length can hide major differences between particular candidate sets. This question asks for an optimal quantum identification algorithm tailored to a specified set C. The source also distinguishes optimal query use from a time-efficient implementation, since deciding which query to make may itself be expensive. Understanding the instance-specific optimum would connect the structure of a hypothesis family with the information and computation needed to learn its member.

[Read in atlas](index.html#TCS-4586) · [An optimal quantum algorithm for the oracle identification problem](https://doi.org/10.4230/LIPIcs.STACS.2014.482)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4615 — The difficult question of whether or not the quantum entropy satisfies inequalities beyond positivity and SSA remains open for four or more parties.

For a multipartite quantum state, the entropies of all subsystems form a vector subject to universal inequalities. Positivity and strong subadditivity give basic constraints on those vectors. This question asks whether additional inequalities are needed to describe the quantum entropy cone for four or more parties. The cited stabilizer-state analysis relates the problem to classical non-Shannon inequalities and to states violating the Ingleton inequality. New constraints or counterexamples would sharpen the mathematical description of how quantum information can be shared among several systems.

[Read in atlas](index.html#TCS-4615) · [The Quantum Entropy Cone of Stabiliser States](https://doi.org/10.4230/LIPIcs.TQC.2013.270)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4696 — Quantum Merkle Trees — Open Problem 2

Quantum Merkle trees are a proposed way to commit succinctly to a large quantum object. This question asks whether they can support a noninteractive succinct argument for a gapped local-Hamiltonian problem. The inspiration is Micali's classical construction, which compresses verification for NP into a short argument. Quantum commitments and the quantum oracle model require their own security reasoning, rather than a direct replacement of classical data by qubits. A successful construction would reduce interaction in the verification of quantum evidence while keeping the proof much shorter than the underlying object.

[Read in atlas](index.html#TCS-4696) · [Quantum Merkle Trees](https://doi.org/10.22331/q-2024-06-18-1380)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4707 — Quantum channel coding: Approximation algorithms and strong converse exponents — Unresolved-question passage on page 28

Channel coding studies how reliably information can be transmitted through a noisy quantum channel when shared entanglement is available. The cited work compares achievable coding performance with non-signaling and meta-converse relaxations that are easier to analyze. Its open direction asks whether the corresponding error exponents agree, extending an equality obtained for strong-converse exponents. It also identifies the need for tighter approximation guarantees in the fully quantum setting. Resolving these gaps would show how closely tractable relaxations capture the true reliability and algorithmic difficulty of entanglement-assisted communication.

[Read in atlas](index.html#TCS-4707) · [Quantum channel coding: Approximation algorithms and strong converse exponents](https://doi.org/10.22331/q-2025-10-06-1877)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4712 — Single-qubit gate teleportation provides a quantum advantage — Unresolved-question passage on page 31

Gate teleportation provides small quantum circuits whose possible outputs are difficult for certain shallow classical circuits to reproduce. The cited work obtains a separation against NC0 using local quantum operations arranged in one dimension. This question asks whether one-dimensional local circuits can demonstrate an advantage against stronger classical computation. The paper's light-cone argument becomes a bottleneck even when the associated group word problem has greater classical complexity. Progress would require a way to turn the quantum circuit's algebraic structure into lower bounds that extend beyond the limited reach of local-dependence arguments.

[Read in atlas](index.html#TCS-4712) · [Single-qubit gate teleportation provides a quantum advantage](https://doi.org/10.22331/q-2024-12-04-1548)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4715 — Succinct Arguments for QMA from Standard Assumptions via Compiled Nonlocal Games — Explicit open question on PDF page 3

Succinct quantum verification aims to check a large computation or witness using very little communication. In the entangled two-prover setting, making verifier questions short is more tractable than making prover answers short. The source explains that efficient honest provers and small communication must be achieved together, so powerful protocols with inefficient provers do not meet the intended target. It uses compiled nonlocal games to combine useful features of cryptographic and multiprover approaches. The remaining direction is to obtain fully succinct verification while overcoming the difficult answer-reduction step in a sound quantum setting.

[Read in atlas](index.html#TCS-4715) · [Succinct Arguments for QMA from Standard Assumptions via Compiled Nonlocal Games](https://doi.org/10.1109/FOCS61266.2024.00078)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4718 — Low-Stabilizer-Complexity Quantum States Are Not Pseudorandom — Question 27

Clifford circuits have strong algebraic structure, while T gates supply a resource that moves computation beyond that regime. This question asks how many T gates are needed to generate computationally pseudorandom quantum states. Such states should resist efficient attempts to distinguish them from genuinely random states despite being efficiently generated. The cited work detects states with low stabilizer complexity and obtains a logarithmic T-count obstruction. Improving the bound would quantify how much non-Clifford structure is necessary to hide an efficiently prepared state's origin.

[Read in atlas](index.html#TCS-4718) · [Low-Stabilizer-Complexity Quantum States Are Not Pseudorandom](https://doi.org/10.4230/LIPIcs.ITCS.2023.64)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4734 — Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians — Explicit open question on PDF page 4

Gap amplification increases the separation between satisfiable and unsatisfiable instances in a verification problem. The cited quantum construction can amplify a Hamiltonian promise gap repeatedly, but its terms act on progressively more qubits. This growing locality obstructs the composition steps used in the classical PCP strategy. The question asks for a quantum analogue that retains the important structural features of Dinur's classical amplification procedure. Such an operation would address a concrete missing ingredient in efforts to make quantum proofs locally checkable with a constant gap.

[Read in atlas](index.html#TCS-4734) · [Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2026.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4737 — Towards a Universal Gateset for QMA1 — Explicit open question on PDF page 2

A perfectly complete quantum proof system accepts some valid witness with probability exactly one. This question asks whether every QMA proof system can achieve that guarantee without sacrificing efficient verification or soundness. Approximate gate synthesis creates a special difficulty because a tiny implementation error can destroy exact acceptance. The cited work therefore keeps the verifier's gate set explicit and studies the structure needed for QMA1. A solution would explain whether perfect reliability on yes-instances is merely a choice of protocol or an additional restriction on quantum proofs.

[Read in atlas](index.html#TCS-4737) · [Towards a Universal Gateset for QMA1](https://doi.org/10.4230/LIPIcs.MFCS.2026.98)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4753 — Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement — Explicit open question on PDF page 12

Two unentangled quantum proofs can impose structure that a single unrestricted witness does not provide. This record asks whether the resulting class QMA(2) has the full power of nondeterministic exponential time. The source reviews protocols compressing satisfiability witnesses and amplification techniques that exploit product-state testing. Those achievements do not by themselves establish the proposed equality with NEXP. Determining the class would reveal how much complexity can be hidden in a promise that independently supplied quantum messages share no entanglement.

[Read in atlas](index.html#TCS-4753) · [Quantum Space, Ground Space Traversal, and How to Embed Multi-Prover Interactive Proofs into Unentanglement](https://doi.org/10.4230/LIPIcs.ITCS.2023.53)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4789 — Quantum Generalizations of the Polynomial Hierarchy with Applications to QMA(2) — Explicit open question on PDF page 6

The quantum-classical polynomial hierarchy alternates classical witnesses while retaining quantum verification. In the classical hierarchy, equality of suitable neighboring levels produces a collapse of all higher levels. This question asks whether equality of the second existential and universal levels has the analogous consequence here. Promise gaps in quantum verification make the usual quantifier manipulations more delicate. A collapse theorem or obstruction would determine whether this hierarchy shares the structural rigidity of its classical counterpart.

[Read in atlas](index.html#TCS-4789) · [Quantum Generalizations of the Polynomial Hierarchy with Applications to QMA(2)](https://doi.org/10.4230/LIPIcs.MFCS.2018.58)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4811 — How Hard Is Deciding Trivial Versus Nontrivial in the Dihedral Coset Problem? — Explicit open question on PDF page 2

The dihedral coset problem is a quantum problem closely connected to hidden subgroup algorithms and certain lattice problems. This project asks how tightly its computational difficulty is related to subset sum, including which densities of subset-sum instances are relevant. A measurement that extracts information optimally need not be efficiently implementable, and its implementation leads to a quantum subset-sum sampling task. The cited reductions connect different density regimes and sometimes pass through unique shortest-vector problems. A sharper equivalence would clarify whether progress on subset sum can actually yield efficient dihedral algorithms, rather than only information-theoretically good measurements.

[Read in atlas](index.html#TCS-4811) · [How Hard Is Deciding Trivial Versus Nontrivial in the Dihedral Coset Problem?](https://doi.org/10.4230/LIPIcs.TQC.2016.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4835 — A Complete Characterization of Unitary Quantum Space — Unresolved-question passage on page 12

Quantum space complexity asks what computations can be performed with a limited quantum workspace. The cited paper characterizes unitary quantum space and relates quantum verification with exponentially small completeness–soundness gaps to classical space complexity. Its closing questions ask what analogous characterizations hold when intermediate nonunitary operations are allowed. Another direction is to understand quantum interactive proofs with exponentially small gaps, between better-understood precision regimes. Progress would connect resource-bounded quantum computation to concrete matrix problems and clarify how measurement, interaction, and precision change its power.

[Read in atlas](index.html#TCS-4835) · [A Complete Characterization of Unitary Quantum Space](https://doi.org/10.4230/LIPIcs.ITCS.2018.4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4882 — Quantum 2-SAT on Low Dimensional Systems Is QMAsubscript{1}-Complete: Direct Embeddings and Black-Box Simulation — Explicit open question on PDF page 1

Quantum satisfiability asks whether local constraints have a common zero-energy quantum state. This project studies where two-body quantum satisfiability changes from efficiently solvable to computationally hard as local dimensions and interaction geometry vary. The source establishes hardness for some mixed-dimension systems while contrasting them with the tractable qubit case. It leaves a broader classification problem involving smaller dimensions, one-dimensional layouts, and the kinds of entangled states that constraints can force. Filling that boundary would explain how little local quantum structure is sufficient to encode hard verification problems.

[Read in atlas](index.html#TCS-4882) · [Quantum 2-SAT on Low Dimensional Systems Is QMAsubscript{1}-Complete: Direct Embeddings and Black-Box Simulation](https://doi.org/10.4230/LIPIcs.ITCS.2025.85)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4894 — Parity vs. AC0 with Simple Quantum Preprocessing — Explicit open question on PDF page 3

Parity is a basic function that small constant-depth classical circuits cannot approximate well on uniformly random inputs. This project asks whether a shallow quantum preprocessing stage can remove that limitation when its measured output is passed to a classical AC0 circuit. The conjecture concerns constant-depth quantum circuits with bounded-fan-in gates, followed by the specified classical postprocessing. Any approximation guarantee must account for both the random input and the randomness of quantum measurement. Establishing the conjecture would place a concrete limit on hybrid computation and help clarify the power of weak classical procedures that use shallow quantum devices.

[Read in atlas](index.html#TCS-4894) · [Parity vs. AC0 with Simple Quantum Preprocessing](https://doi.org/10.4230/LIPIcs.ITCS.2024.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4927 — The Classification of Reversible Bit Operations — Explicit open question on PDF page 2

A classification of reversible classical gates describes which transformations become possible when a gate set is composed repeatedly. The source uses that completed classical picture to motivate an analogous classification for quantum gates. The quantum question is whether known nonuniversal families, such as stabilizer operations and basis-preserving constructions, account for all relevant possibilities. Additional discrete families or intermediate computational behavior could make the quantum landscape substantially richer. A full classification would organize quantum gate resources by the computations they enable and identify exactly where universality appears.

[Read in atlas](index.html#TCS-4927) · [The Classification of Reversible Bit Operations](https://doi.org/10.4230/LIPIcs.ITCS.2017.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4952 — Quantum Versus Randomized Communication Complexity, with Efficient Players — Explicit open question on PDF page 2

Quantum communication can outperform randomized classical communication dramatically on some problems with restricted inputs. This project asks whether an exponential separation is possible for a total function, whose value is defined on every input pair. The cited work also emphasizes efficient local computation by the communicating parties, so a protocol's message length is not its only resource. Promise-problem separations do not by themselves answer the total-function question because their input restrictions may be essential. Resolving this would clarify how broadly quantum communication advantages survive when both the task specification and the players' computations are constrained.

[Read in atlas](index.html#TCS-4952) · [Quantum Versus Randomized Communication Complexity, with Efficient Players](https://doi.org/10.4230/LIPIcs.ITCS.2021.54)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4954 — The Power of One Clean Qubit in Communication Complexity — Conjecture 25

The one-clean-qubit model starts with a single pure qubit and otherwise highly mixed quantum memory. The cited conjecture asks whether this restricted model can achieve a strong communication advantage over classical simulation. It proposes a protocol using logarithmic communication whose classical simulation with constant additive error requires polynomially more communication. A three-party promise problem involving products of orthogonal matrices is presented as a candidate setting for this separation. Proving such a lower bound would demonstrate that a large communication advantage need not require a large supply of clean initial qubits.

[Read in atlas](index.html#TCS-4954) · [The Power of One Clean Qubit in Communication Complexity](https://doi.org/10.4230/LIPIcs.MFCS.2021.69)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4977 — Quantum Polynomial Hierarchies: Karp-Lipton, Error Reduction, and Lower Bounds — Explicit open question on PDF page 3

Quantum polynomial hierarchies extend alternating proof systems by allowing quantum witnesses and different restrictions on their states. The source compares a hierarchy with classical witnesses, one with general quantum witnesses, and one with pure-state witnesses. The selected question is whether the classical-witness hierarchy is contained in the general quantum-witness hierarchy in the intended bounded-error sense. Simply replacing each classical proof by a measured quantum state can fail to preserve the behavior of alternating quantifiers. Establishing the containment, or identifying an obstruction, would clarify how classical information, mixed states, and quantifier order interact in quantum verification.

[Read in atlas](index.html#TCS-4977) · [Quantum Polynomial Hierarchies: Karp-Lipton, Error Reduction, and Lower Bounds](https://doi.org/10.4230/LIPIcs.MFCS.2024.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4991 — Universality of EPR Pairs in Entanglement-Assisted Communication Complexity, and the Communication Cost of State Conversion — Explicit open question on PDF page 2

Entanglement-assisted communication protocols may begin with a large shared quantum state that does not count toward their communication cost. This project asks for a quantum analogue of reducing shared randomness in classical communication. The central issue is whether the amount of prior entanglement can be reduced while allowing the protocol itself to change and preserving comparable communication and error. Limitations on replacing the shared state inside a fixed protocol do not settle that more flexible question. A positive result would bound a currently separate resource and make comparisons between entanglement-assisted protocols more informative.

[Read in atlas](index.html#TCS-4991) · [Universality of EPR Pairs in Entanglement-Assisted Communication Complexity, and the Communication Cost of State Conversion](https://doi.org/10.4230/LIPIcs.CCC.2019.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4992 — Bounding Quantum-Classical Separations for Classes of Nonlocal Games — Explicit open question on PDF page 3

In a nonlocal XOR game, separated players try to satisfy a parity condition without communicating after receiving their inputs. Shared entanglement can improve their success bias over the best classical strategy, and some games already exhibit an unbounded ratio between those biases. The source asks for a stronger separation in which the entangled bias stays bounded away from zero while the classical bias tends to zero. Existing ratio separations may let both biases vanish, which weakens their usefulness for related communication tasks. Constructing a robust separation would turn a large relative advantage into a reliably detectable quantum advantage.

[Read in atlas](index.html#TCS-4992) · [Bounding Quantum-Classical Separations for Classes of Nonlocal Games](https://doi.org/10.4230/LIPIcs.STACS.2019.12)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5021 — The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model — Explicit open question on PDF page 3

The quantum approximate optimization algorithm uses alternating quantum operations to search for good solutions to combinatorial optimization problems. This source analyzes its MaxCut performance on regular graphs whose local neighborhoods resemble trees. It conjectures that increasing the algorithm's depth can reach the asymptotically optimal cut fraction on large random regular graphs. The proposed limiting performance is connected to the Parisi value from the Sherrington–Kirkpatrick spin-glass model. Proving the conjecture would establish a precise optimization capability for this quantum algorithm and justify a new, potentially expensive route to computing the same statistical-physics constant.

[Read in atlas](index.html#TCS-5021) · [The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model](https://doi.org/10.4230/LIPIcs.TQC.2022.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5047 — Quantum Time-Space Tradeoff for Finding Multiple Collision Pairs — Explicit open question on PDF page 3

Finding repeated outputs of a function is a basic search task whose cost depends on how much information an algorithm can retain. This project asks for a stronger quantum time–space lower bound when the goal is to find many distinct collision pairs. The source conjectures that the square of the query time times the workspace must grow with the square of the requested number of collisions and the domain-size parameter. Its reduction would convert that improvement into an optimal tradeoff for the related element-distinctness problem. Proving the conjecture would explain why quantum query savings cannot always be combined with very small memory.

[Read in atlas](index.html#TCS-5047) · [Quantum Time-Space Tradeoff for Finding Multiple Collision Pairs](https://doi.org/10.4230/LIPIcs.TQC.2021.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5077 — A Parallel Repetition Theorem for All Entangled Games — Explicit open question on PDF page 3

Parallel repetition tries to reduce the success probability of a game by asking players to win many independent instances simultaneously. Entangled players can correlate their strategies across instances, making this amplification harder to analyze than independent play suggests. The extracted passage describes the historical question of whether a game with entangled value below one could retain a success probability bounded away from zero under arbitrarily many repetitions. The same paper then rules out that behavior for the setting it studies, while distinguishing this result from stronger quantitative decay claims and transformations of the game. This entry therefore introduces a source-resolved question and the surrounding amplification issue rather than treating the quoted historical uncertainty as a fresh unresolved claim.

[Read in atlas](index.html#TCS-5077) · [A Parallel Repetition Theorem for All Entangled Games](https://doi.org/10.4230/LIPIcs.ICALP.2016.77)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5079 — Pointer Quantum PCPs and Multi-Prover Games — Explicit open question on PDF page 3

The quantum PCP program asks whether quantum proofs remain hard to verify even when only a small part of the proof is inspected. Pointer quantum PCPs introduce a more structured proof system and a conjecture weaker than the original quantum PCP conjecture. The source gives equivalent formulations using a Hamiltonian problem and a polynomial-size multiprover game. It asks whether this intermediate conjecture can be established or shown equivalent to the original one, with adaptive access posing a specific obstacle. Understanding that relationship could provide a more manageable route to quantum proof hardness while revealing which verification features are essential.

[Read in atlas](index.html#TCS-5079) · [Pointer Quantum PCPs and Multi-Prover Games](https://doi.org/10.4230/LIPIcs.MFCS.2016.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5106 — A Simple Protocol for Verifiable Delegation of Quantum Computation in One Round — Explicit open question on PDF page 4

Verifiable delegation lets a limited client outsource quantum computation while checking that the returned answer is trustworthy. The selected question asks whether a protocol can provide this verification and also hide the delegated computation using only one round of interaction. The source's setting uses two provers and already obtains a one-round verification protocol, so blindness is an additional requirement. Its discussion also identifies the large resource overhead of the existing construction as a related obstacle. A construction or an impossibility result would clarify the tradeoff between interaction, privacy, and efficient quantum verification in this model.

[Read in atlas](index.html#TCS-5106) · [A Simple Protocol for Verifiable Delegation of Quantum Computation in One Round](https://doi.org/10.4230/LIPIcs.ICALP.2019.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5136 — Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge — Explicit open question on PDF page 4

Quantum distinguishing complexity measures the queries needed to produce quantum states that separate inputs with different function values. Approximate degree instead measures the degree of a real polynomial that approximates the function on its allowed inputs. This project asks for an exponential separation between these measures on a partial Boolean function. The source gives polynomial separations for total functions but explains that even the corresponding exponential gap for ordinary quantum query complexity is not established there. A construction would show a strong limitation of polynomial approximation as a guide to the quantum information needed for distinguishing inputs.

[Read in atlas](index.html#TCS-5136) · [Quantum Distinguishing Complexity, Zero-Error Algorithms, and Statistical Zero Knowledge](https://doi.org/10.4230/LIPIcs.TQC.2019.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5170 — Another Subexponential-time Quantum Algorithm for the Dihedral Hidden Subgroup Problem — Explicit open question on PDF page 5

Hidden subgroup algorithms query a function whose equal-value classes encode an unknown subgroup. In standard approaches to the dihedral problem, the function's output labels are discarded and the algorithm processes the remaining quantum state. The selected question asks whether retaining or otherwise using those labels can help when the output set has no additional structure. Merely saying that the output is measured does not exploit it if the measurement result is never used. An algorithmic benefit or a rigorous limitation would clarify whether the usual coset-state viewpoint loses useful information at subexponential query scales.

[Read in atlas](index.html#TCS-5170) · [Another Subexponential-time Quantum Algorithm for the Dihedral Hidden Subgroup Problem](https://doi.org/10.4230/LIPIcs.TQC.2013.20)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5202 — Quantum-Proof Multi-Source Randomness Extractors in the Markov Model — Explicit open question on PDF page 2

Randomness extractors turn weakly random inputs into nearly uniform bits, often for use as cryptographic keys. Their guarantees must account for information an adversary already holds about the input. The selected passage asks whether general seeded extractors with multiple output bits remain secure against quantum side information with suitable parameter losses. The source contrasts this with more established one-bit guarantees and with specific multibit constructions already known to be quantum-proof. Resolving the general question would determine how freely classical extractor designs can be reused when an adversary stores quantum information.

[Read in atlas](index.html#TCS-5202) · [Quantum-Proof Multi-Source Randomness Extractors in the Markov Model](https://doi.org/10.4230/LIPIcs.TQC.2016.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6459 — Cost of quantum secret key — Explicit open question on PDF page 3

Shared quantum states can sometimes be converted into secret classical keys by local operations and public communication. This project asks whether there are entangled states from which no secret key can be distilled. Separable states provide a known class of useless resources, but entanglement alone does not immediately determine the distillable-key rate. The question is also different from asking whether an entangled state can produce maximally entangled pairs. Identifying an entangled key-undistillable state, or proving that none exists, would settle a basic boundary in the resource theory of private communication.

[Read in atlas](index.html#TCS-6459) · [Cost of quantum secret key](https://doi.org/10.22331/q-2026-05-06-2098)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6461 — Quantum complexity phase transitions in monitored random circuits — Unresolved-question passage on page 30

Monitored quantum circuits alternate unitary evolution with measurements, which can strongly change the complexity of their output states. The source constructs special outputs with growing approximate circuit complexity by exploiting paths that avoid measurement. The selected unresolved step is to establish comparable growth for generic outputs of the monitored random circuit. The special construction fixes other gates to identities, and even perturbing them is delicate because measurement and renormalization can magnify changes. A robust lower bound would distinguish a typical complexity phase from behavior exhibited only by carefully chosen circuit realizations.

[Read in atlas](index.html#TCS-6461) · [Quantum complexity phase transitions in monitored random circuits](https://doi.org/10.22331/q-2025-02-10-1627)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6481 — Bosonic Quantum Computational Complexity — Explicit open question on PDF page 10

Continuous-variable quantum computation uses bosonic modes rather than a finite collection of two-level systems alone. This source studies a model with cubic phase gates and proves an exponential-space upper bound on its computational power. It asks whether that upper bound can be substantially improved, perhaps toward the classical counting classes that contain ordinary qubit quantum computation. Cubic phase gates can rapidly increase the degree and coefficient size of operator expressions, obstructing straightforward simulations. A tighter characterization would clarify which apparent extra power comes from the infinite-dimensional model and which reflects limitations of current analysis.

[Read in atlas](index.html#TCS-6481) · [Bosonic Quantum Computational Complexity](https://doi.org/10.22331/q-2026-05-20-2110)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6828 — Construct explicit quantum channels witnessing non-additivity of Holevo information; existence is established nonconstructively.

A channel's Holevo capacity optimizes how much classical information can be encoded in an ensemble of quantum inputs. Non-additivity means that using quantum channels together can outperform the value predicted by adding their separate Holevo capacities. The source already establishes that such behavior exists, so the selected direction is to obtain explicit channels exhibiting it. A useful construction should expose the mechanism and admit a direct verification rather than rely only on a nonconstructive existence argument. This is an exploratory construction problem whose eventual formal card still needs to specify the desired notion of explicitness and quantitative separation.

[Read in atlas](index.html#TCS-6828) · [The Theory of Quantum Information](https://cs.uwaterloo.ca/~watrous/TQI/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6933 — Classical computers cannot efficiently sample the Boson Sampling distribution in the regime described in the source.

Boson sampling asks a device to sample the output pattern of photons passing through a linear-optical network. The cited overview presents the conjecture that classical computers cannot perform this sampling efficiently in the specified regime. The difficulty concerns reproducing a distribution, so computing one output probability is not by itself the same task. Exact sampling, approximate sampling, and experimental noise require different assumptions and must be separated when the conjecture is formalized. Resolving the relevant hardness claim would support a concrete route to quantum sampling advantage without requiring a universal quantum computer.

[Read in atlas](index.html#TCS-6933) · [Quantum Algorithms: An Overview](https://arxiv.org/abs/1511.04206)
Existing status: `source_open` · Summary written: 2026-09-11
