# Working summaries — large categories

435 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computational complexity (74)

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

The polynomial hierarchy adds successive alternating blocks of efficiently bounded existential and universal choices. Its first levels already include polynomial-time computation and ordinary NP verification. The question asks whether every additional fixed level strictly increases computational power. Equality of neighboring levels would collapse all higher finite levels as well. The project studies whether increasingly nested candidate-and-challenge reasoning creates an endless hierarchy of difficulty, a stronger issue than separating P from NP at the first step.

[Read in atlas](index.html#TCS-6532) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [The Polynomial-Time Hierarchy](https://research.ibm.com/publications/the-polynomial-time-hierarchy) · [The Polynomial Hierarchy, Random Oracles, and Boolean Circuits](https://www.cs.columbia.edu/~rocco/Public/sigact15.pdf) · [An Average-Case Depth Hierarchy Theorem for Boolean Circuits](https://arxiv.org/abs/1504.03398) · [Upper and Lower Bounds for the Linear Ordering Principle](https://eccc.weizmann.ac.il/report/2025/142/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0021 — NP versus P/poly

Nonuniform Boolean circuits may choose a separate computational design for each input length. The question asks whether some language in NP requires more than polynomially many gates despite that freedom. A uniform running-time lower bound would not automatically establish this stronger claim. Counting shows that most functions have large circuits but does not supply the necessary NP language. The project seeks explicit hardness robust to arbitrary length-specific preprocessing and would connect circuit lower bounds to the structure of the polynomial hierarchy.

[Read in atlas](index.html#TCS-0021) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Natural Proofs](https://doi.org/10.1006/jcss.1997.1494) · [Nonuniform ACC Circuit Lower Bounds](https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-6168 — Does NP-hardness of MCSP imply circuit lower bounds for EXP?

MCSP asks whether a fully listed Boolean function has a small circuit. The question concerns what proving its ordinary NP-hardness would force elsewhere in complexity theory. The proposed consequence is that some exponential-time language requires superpolynomial circuits. Existing consequences separate EXP from smaller intersections or randomized classes and do not yield that circuit lower bound. The target captures a major proposed connection between metacomplexity and nonuniform lower bounds.

[Read in atlas](index.html#TCS-6168) · [On the (Non) NP-Hardness of Computing Circuit Complexity](https://doi.org/10.4230/LIPIcs.CCC.2015.365) · [On the (Non) NP-Hardness of Computing Circuit Complexity](https://theoryofcomputing.org/articles/v013a004/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7159 — Hartmanis–Stearns conjecture

The question concerns a fixed machine that prints all digits of a real number with bounded delay between outputs. Every rational number permits this because its expansion is eventually periodic. The conjecture says that any irrational number generated this quickly must be transcendental. It quantifies over unrestricted deterministic multitape machines, beyond the restricted automata covered by known partial results. A proof would connect the arithmetic nature of numbers to a stringent computation bound and rule out linear-time integer multiplication.

[Read in atlas](index.html#TCS-7159) · [On the computational complexity of algebraic numbers: the Hartmanis–Stearns problem revisited](https://arxiv.org/abs/1601.02771) · [Time-Restricted Sequence Generation](https://people.csail.mit.edu/meyer/time-restricted-sequence-generation-jcss.pdf) · [On Transcendence of Numbers Related to Sturmian and Arnoux-Rauzy Words](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.144) · [Computing the base-b representation of quadratic irrationals using automata](https://doi.org/10.1016/j.tcs.2026.115843)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7243 — Linear-size circuits for stable ternary compaction

Stable ternary compaction moves every 2 to the end while preserving the order of all 0s and 1s. The question is whether every input length admits a Boolean circuit of size proportional to that length. The circuits use a fixed bounded-fan-in basis and may have arbitrary depth and fan-out. Stability retains the original binary sequence, so ordinary ternary sorting is insufficient. The target supplies a concrete function for studying the limits of linear-size circuits.

[Read in atlas](index.html#TCS-7243) · [Linear-size circuits for stable \(0,1 < 2\) sorting?](https://www.openproblemgarden.org/op/linear_size_circuits_for_stable_0_1_2_sorting) · [Sorting Short Keys in Circuits of Size \(o(n \log  n)\)](https://arxiv.org/abs/2010.09884)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0017 — Karchmer–Raz–Wigderson conjecture

Composing Boolean functions means applying one function to separate input blocks and feeding the results into another. A straightforward formula substitutes a copy of the inner formula for each outer input occurrence. The KRW conjecture asks whether formula complexity must essentially multiply under this operation. Unexpected sharing is unavailable in formulas, but alternate logical factorizations might still save size. The project seeks a composition lower bound powerful enough to separate efficient circuits from much larger formulas.

[Read in atlas](index.html#TCS-0017) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0019 — Polynomial formulas versus linear circuits

Circuits can reuse intermediate results, while formulas duplicate them whenever several later computations need them. The conjecture asks for functions with linear-size circuits but no polynomial-size formulas. Known polynomial gaps do not establish this superpolynomial separation. The source connects the goal to understanding formula complexity under repeated composition. The project asks whether a small directed computational graph can perform a task that every tree-shaped computation must express with vastly more repeated work.

[Read in atlas](index.html#TCS-0019) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6455 — Doubly efficient \(\mathrm{IP} = \mathrm{PSPACE}\) for the full time range

An interactive proof lets a verifier check a claim through conversation with a prover. The question asks whether polynomial-space computations taking time T can be verified in polynomial input time using an honest prover running in polynomial T time. The requirement extends across the full time range, beyond quasipolynomial computations. This would make proof generation efficient relative to the computation being certified, strengthening the resource content of \(\mathrm{IP}=\mathrm{PSPACE}\). The saved review stresses that soundness must still withstand arbitrarily powerful cheating provers, despite the efficiency requirement imposed on the honest one.

[Read in atlas](index.html#TCS-6455) · [Towards a Doubly Efficient \(\mathrm{IP}=\mathrm{PSPACE}\)](https://eccc.weizmann.ac.il/report/2026/102/)
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

### TCS-0310 — Polynomial-time weighted falsifiability of unambiguous DNFs

An unambiguous DNF has mutually disjoint satisfying terms, making some counting tasks straightforward. The question instead asks for a falsifying assignment with sufficiently large total variable weight. Weights and the threshold are binary encoded. Knowing how many assignments falsify the formula does not reveal whether one reaches the desired score. The project tests whether the strong disjointness promise still helps when every term must be defeated simultaneously while optimizing an additive objective over the complement.

[Read in atlas](index.html#TCS-0310) · [Is this problem on unambiguous DNFs hard?](https://cstheory.stackexchange.com/questions/53733/is-this-problem-on-unambiguous-dnfs-hard) · [Representation, Provenance, and Explanations in Database Theory and Logic (Dagstuhl Seminar 24032)](https://doi.org/10.4230/DagRep.14.1.49) · [List of open questions: Weighted falsifiability for unambiguous DNFs](https://a3nm.net/work/research/questions/#weighted-falsifiability-for-unambiguous-dnfs)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1035 — Cost of restricting linear circuits to depth two

A linear circuit shares partial sums to compute a matrix transformation over a specified operation system. Restricting it to depth two allows only one intermediate layer. The source asks how much this restriction can increase circuit complexity, with different behavior for OR, SUM, and XOR operations. Known separations leave room for stronger gaps, particularly over the binary field. The project seeks to quantify the value of additional computational layers even when the final transformation is algebraically simple.

[Read in atlas](index.html#TCS-1035) · [Complexity of Linear Boolean Operators](https://web.vu.lt/mif/s.jukna/Knizka/index.html)
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

### TCS-0297 — A counting characterization of P with NP access

A counting function in #P returns the number of accepting witnesses for an efficiently checkable relation. The question asks whether some such function gives a polynomial-time oracle machine exactly the power of polynomial time with an NP oracle. Ordinary complete counting functions provide substantially more apparent information than mere existence tests. The target therefore requires a specially controlled counting task. The project seeks a numerical oracle capturing NP access without unintentionally granting the full power of general witness counting.

[Read in atlas](index.html#TCS-0297) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0298 — SAT multi-prover proofs using efficient SAT-oracle provers

Multi-prover interactive proofs let a verifier question several provers that cannot coordinate their answers during the protocol. The source asks for such a proof system for SAT whose honest provers run in randomized polynomial time with SAT-oracle access. Unrestricted provers do not meet this efficiency requirement. The question is tied to whether SAT programs can be checked through suitable oracle interactions. The project seeks a verification protocol whose participants need no computational power beyond the problem they are supposed to certify.

[Read in atlas](index.html#TCS-0298) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/oracles.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1602 — Deterministic query complexity of tournament kings

A king in a tournament is a vertex that can reach every other vertex along a directed path of at most two edges. The graph is accessed by queries revealing the direction of individual edges. Every tournament has a king, so the challenge is to find one while inspecting as few edges as possible. The source asks for the deterministic query complexity, reporting an \(O(n^{3/2})\) algorithm and an \(\Omega (n^{4/3})\) lower bound. Closing this gap would quantify the information needed to locate a globally influential vertex in a completely oriented graph.

[Read in atlas](index.html#TCS-1602) · [Hardness of Finding Kings and Strong Kings](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2029 — FBPP versus negligible-error FBPP

For a relation, an algorithm may output any answer satisfying the input-output specification rather than one uniquely determined value. This makes the precise convention for reducing error more consequential than it is for ordinary decision problems. The source compares FBPP with a version requiring negligible error and gives a relation separating the classes in one direction. The remaining question is whether an inclusion holds in the other direction or whether the two classes are incomparable. An answer would clarify which amplification intuitions remain valid when success means producing an arbitrary valid output.

[Read in atlas](index.html#TCS-2029) · [A Qubit, a Coin, and an Advice String Walk into a Relational Problem](https://doi.org/10.4230/LIPIcs.ITCS.2024.1)
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

### TCS-3685 — Average-case formula hardness of the majority Andreev function

The majority Andreev function uses row majorities as an address into an input truth table. The source proposes almost cubic formula hardness even for inverse-polynomial agreement advantage under uniform input. In that literal model, one table-bit literal already has agreement at least \(1/2+1/(2n)\). This does not contradict the source’s worst-case formula theorem, but it prevents certifying the extracted average-case claim. The intended distribution, encoding or advantage threshold must be corrected from a source before the card becomes a complete open problem.

[Read in atlas](index.html#TCS-3685) · [Cubic Formula Size Lower Bounds Based on Compositions with Majority](https://doi.org/10.4230/LIPIcs.ITCS.2019.35) · [Cubic Formula Size Lower Bounds Based on Compositions with Majority](https://eccc.weizmann.ac.il/report/2018/160/)
Existing status: `uncertain` · Summary written: 2026-09-12

### TCS-3862 — Complete problems for search zero knowledge

Zero-knowledge protocols are usually framed around deciding whether a statement is true. Search zero knowledge instead concerns interactions that produce a valid solution while controlling what additional information is revealed. The selected problem asks whether these search classes have complete problems in either the computational or statistical security setting. A complete problem would serve as a universal representative to which other search-zero-knowledge tasks can be reduced under suitable definitions. Finding one would organize the new model and help transfer general techniques from the better-developed theory of decision zero knowledge.

[Read in atlas](index.html#TCS-3862) · [Brief Announcement: Zero-Knowledge Protocols for Search Problems](https://doi.org/10.4230/LIPIcs.ICALP.2018.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3886 — \(\exists \cdot \mathrm{BPP}\) versus MA

Merlin–Arthur verification combines a classical witness with an efficient randomized check. Applying an existential quantifier to an ordinary BPP language imposes an additional bounded-error condition on every witness-input pair. In an MA protocol, by contrast, unsuccessful witnesses on a yes-instance may have intermediate acceptance probabilities. This question asks whether those different promise conventions nevertheless define the same class. The distinction matters when building classical or quantum verification hierarchies, because moving quantifiers across probabilistic tests can silently strengthen the requirements on a verifier.

[Read in atlas](index.html#TCS-3886) · [Quantum Generalizations of the Polynomial Hierarchy with Applications to \(\mathrm{QMA}(2)\)](https://doi.org/10.4230/LIPIcs.MFCS.2018.58)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4468 — Subcube partition complexity versus query complexity

A subcube partition divides all Boolean inputs into monochromatic pieces, each specified by fixing some coordinates. Unlike a decision tree, the pieces need not arise from one sequential hierarchy of queries. The source separates this partition model from randomized decision trees and asks for the strongest possible gap between their complexities. Even the comparison with deterministic query complexity is included in the question. Determining the extremal separation would quantify how much harder it is to discover an input's certificate adaptively than merely to exhibit a globally consistent collection of certificates.

[Read in atlas](index.html#TCS-4468) · [Separating Decision Tree Complexity from Subcube Partition Complexity](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.915)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4746 — Effective enumeration of BPP

A randomized polynomial-time program belongs to BPP only if its answer is reliably biased toward correctness on every input. That semantic requirement is harder to recognize than a syntactic time bound. This problem asks whether there is an effective enumeration of algorithms covering exactly the languages in BPP. The cited work uses arithmetical theories to study how error guarantees can be expressed and justified. A successful characterization would connect feasible randomized computation with formal languages whose programs come with uniformly controlled error behavior.

[Read in atlas](index.html#TCS-4746) · [Enumerating Error Bounded Polytime Algorithms Through Arithmetical Theories](https://doi.org/10.4230/LIPIcs.CSL.2024.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4786 — Complexity of Minimum Circuit Size

The minimum circuit size problem asks whether a truth table can be implemented by a Boolean circuit below a given size threshold. A small circuit supplies an efficiently checkable witness, placing the problem in NP when input length is measured by the full truth table. The selected passage highlights the unresolved classification between efficient randomized algorithms and NP-hardness. It also notes that an efficient algorithm would enable average-case inversion of candidate one-way functions through known reductions. Understanding this problem would connect circuit minimization, obfuscation, and the computational assumptions that make cryptography possible.

[Read in atlas](index.html#TCS-4786) · [Synergy Between Circuit Obfuscation and Circuit Minimization](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4960 — Polynomial depth lower bounds for Transformers

The source analyzes the representational limits of multilayer decoder-only Transformers using communication-complexity methods. Its lower bounds constrain constant-depth architectures solving carefully defined compositional tasks. The selected question asks for a polynomial lower bound on the depth needed by Transformers. The authors allow either an unconditional result or one based on established computational complexity conjectures. This would identify tasks whose sequential compositional structure cannot be absorbed into a shallow attention architecture without violating the model's other resource constraints.

[Read in atlas](index.html#TCS-4960) · [Theoretical Limitations of Multi-Layer Transformer](https://doi.org/10.1109/FOCS63196.2025.00136)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4988 — Existence of TFNP-complete problems

TFNP consists of search problems with efficiently checkable solutions whose existence is guaranteed for every input. This project asks whether the entire class has a complete problem under the intended efficient search reductions. Such a problem would represent the difficulty of all total NP search tasks, rather than only a subclass with a particular existence principle. The source discusses oracle constructions and their connections with promise classes, which can expose barriers without settling the unrelativized question. A complete problem or a rigorous obstruction would reshape how total search problems are compared, including those studied as foundations for cryptography.

[Read in atlas](index.html#TCS-4988) · [An Oracle with no UP-Complete Sets, but \(\mathrm{NP} = \mathrm{PSPACE}\)](https://doi.org/10.4230/LIPIcs.MFCS.2024.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5593 — Black-Box Hypothesis

A property of Boolean functions can be tested either from a circuit description or by querying the function as a black box. The Black-Box Hypothesis says that efficient access to the circuit's internal representation does not help decide such semantic properties, given an appropriate circuit-size bound. The source studies what follows if this hypothesis fails. For several kinds of counterexample, it derives nontrivial circuit satisfiability algorithms. Resolving the hypothesis would clarify whether inspecting an implementation offers a fundamental computational advantage over observing its behavior, with consequences for major complexity separations.

[Read in atlas](index.html#TCS-5593) · [Does Looking Inside a Circuit Help?](https://doi.org/10.4230/LIPIcs.MFCS.2017.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6006 — Complexity of ARRIVAL

ARRIVAL describes a deterministic walk in a directed graph whose vertices alternate between two outgoing choices on successive visits. The decision task asks which designated destination the walk eventually reaches. The source notes efficiently verifiable certificates for either answer, placing the problem in NP intersect coNP. It improves exponential algorithms to a subexponential bound and gives a polynomial-time algorithm for almost acyclic graphs. The remaining project is to decide whether all instances can be solved in polynomial time without explicitly following a walk that may be exponentially long.

[Read in atlas](index.html#TCS-6006) · [A Subexponential Algorithm for ARRIVAL](https://doi.org/10.4230/LIPIcs.ICALP.2021.69)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6091 — Exponential depth-three \(\mathrm{AC}^{0}\) lower bounds for E

The class E contains decision problems solvable in deterministic time exponential with a linear exponent. The selected question asks whether some problem in E requires depth-three AC0 circuits of size \(2^{\Omega (n)}\). These circuits use AND, OR, and NOT gates but have only three layers of computation. The source raises this lower-bound target while proving NP-hardness for minimization in a different OR-AND-MOD circuit model. It explains that natural attempts to extend that hardness result to depth-three AC0 would also establish the strong uniform circuit lower bound.

[Read in atlas](index.html#TCS-6091) · [NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD Circuits](https://doi.org/10.4230/LIPIcs.CCC.2018.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6139 — Subexponential derandomization of multipass randomized logspace

A randomized logspace machine has very little working memory, but its power also depends on how it accesses random bits. Allowing two-way access lets it revisit its random tape instead of consuming each bit once. The source asks whether this model can be simulated deterministically in subexponential time. Its results for machines making a controlled number of passes do not settle unrestricted two-way access. Understanding the difference would clarify how reusable randomness affects small-space computation and why conventional logspace derandomization techniques do not automatically apply.

[Read in atlas](index.html#TCS-6139) · [A Note on the Advice Complexity of Multipass Randomized Logspace](https://doi.org/10.4230/LIPIcs.MFCS.2016.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6285 — Closure of UL under complement

UL consists of logarithmic-space computations with at most one accepting computation on each input. The cited passage asks whether this unambiguous class is closed under complement. Closure would mean that rejecting instances also admit an equally economical unambiguous decision procedure. The paper encounters the issue while defining functions and composing algorithms for planar depth-first search. The project addresses a structural complexity question whose answer affects how safely unambiguous subroutines can replace ordinary nondeterministic reachability tests.

[Read in atlas](index.html#TCS-6285) · [Depth-First Search in Directed Planar Graphs, Revisited](https://doi.org/10.4230/LIPIcs.MFCS.2021.7)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6488 — Grundy-value computation versus winner determination

The Grundy value of an impartial game contains more information than whether the current player can force a win. The imported question asks for a general efficient reduction from computing that value to determining a winner. The source exhibits a sharp separation for Undirected Geography, where winner determination is efficient but Grundy computation is PSPACE-complete. That result supplies a complexity-theoretic obstruction to the proposed general reduction. The project explains why composing individually tractable games may require information much harder to obtain than their separate win-loss outcomes.

[Read in atlas](index.html#TCS-6488) · [Winning the War by (Strategically) Losing Battles: Settling the Complexity of Grundy-Values in Undirected Geography](https://doi.org/10.1109/FOCS52979.2021.00119)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6712 — Nonuniform \(\mathrm{NC}^{1}\) versus P/poly

A polynomial-size Boolean circuit represents an efficient nonuniform computation, but its longest chain of dependent gates can be large. The question asks whether every such computation can be reorganized into logarithmic depth while retaining polynomial size. Logarithmic depth would permit much greater parallelism without allowing an excessive number of gates. Counting arguments and restricted circuit lower bounds do not settle this comparison for unrestricted Boolean circuits. Resolving it would determine whether polynomial-size circuits and the nonuniform version of NC1 have the same expressive power.

[Read in atlas](index.html#TCS-6712) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6714 — Nonuniform \(\mathrm{NC}^{1}\) perfect matching

Matching asks for edges with disjoint endpoints, with perfect matching requiring every vertex to be covered. Polynomial-time matching algorithms imply polynomial-size Boolean circuits for the decision problem. The question asks whether general circuits can achieve logarithmic depth as well. The cited source discusses a matching-size threshold and proves a strong depth lower bound when the circuit is required to be monotone. The project is to understand whether allowing negation permits substantially shallower matching computations, beyond the restrictions captured by that monotone lower bound.

[Read in atlas](index.html#TCS-6714) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6715 — Monotone circuits versus monotone span programs

A monotone span program accepts an input when vectors enabled by its one-bits span a designated target vector over a field. A monotone Boolean circuit instead combines input bits using AND and OR gates. The question asks for functions with polynomial-size monotone circuits that require superpolynomial-size monotone span programs. The source discusses a separation in the opposite direction, so this asks whether the two models can be incomparable in efficiency. Such an example would expose a limitation of linear-algebraic representations even for functions having short purely monotone logical computations.

[Read in atlas](index.html#TCS-6715) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6716 — General versus monotone span programs

Ordinary span programs may enable vectors using either positive or negative input literals. Monotone span programs use only positive literals, even when the function itself is monotone. The question asks for a monotone function with a polynomial-size ordinary span program but no polynomial-size monotone span program. The analogous distinction can be dramatic for Boolean circuits, but the source leaves it unsettled for span programs. A separation would show that negative tests can provide essential efficiency in linear-algebraic computation despite the monotonicity of the final answer.

[Read in atlas](index.html#TCS-6716) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6743 — Randomized evasiveness conjecture

A monotone graph property is preserved when edges are added, and a graph property ignores vertex labels. The randomized evasiveness conjecture asks whether every nontrivial such property on k vertices requires \(\Omega\)(k squared) adjacency queries for exact recognition with bounded error. The algorithm must distinguish every yes-instance from every no-instance, including graphs differing by very few edges. This differs fundamentally from property testing, which allows a gap between valid graphs and graphs far from validity. A quadratic lower bound would say that randomness cannot avoid inspecting a constant fraction of potential edges in the worst case.

[Read in atlas](index.html#TCS-6743) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6747 — Graph nonisomorphism in BPP

Graph nonisomorphism asks whether two graphs cannot be matched by any relabeling that preserves adjacency. The question asks for a randomized polynomial-time algorithm with bounded error for this decision problem. Interactive protocols can certify nonisomorphism efficiently using help from an untrusted prover, but that assistance is absent in BPP. Since BPP is closed under complement, the same algorithmic question can be phrased for graph isomorphism. Resolving it would clarify whether randomization alone can efficiently handle a central structural comparison problem that has distinctive behavior among complexity-theoretic examples.

[Read in atlas](index.html#TCS-6747) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6817 — Directed reachability in polynomial time and polylogarithmic space

Directed reachability asks whether a path exists from a specified start vertex to a specified target. A graph search can solve it in polynomial time using substantial memory, while recursive reachability methods save memory at a time cost. The question asks for one algorithm that simultaneously uses polynomial time and only polylogarithmic space. Obtaining the two resource bounds in separate algorithms does not meet this requirement. The problem is a basic test of whether reachability can combine efficient exploration with an extremely small working memory.

[Read in atlas](index.html#TCS-6817) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6832 — Separations among P, RP and NP

P consists of problems with deterministic polynomial-time algorithms, while RP permits randomized algorithms that can miss yes-instances but never falsely accept no-instances. Every RP algorithm can be viewed as an NP verification procedure by treating its random choices as a certificate. This gives the chain P contained in RP contained in NP. The question asks which of these inclusions are strict. The alternatives distinguish whether randomness adds power beyond deterministic computation and whether one-sided randomized search can capture the full strength of efficiently verifiable existence.

[Read in atlas](index.html#TCS-6832) · [Understanding Machine Learning: From Theory to Algorithms](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6934 — Unconditional SAT time lower bounds

SAT asks whether a Boolean formula admits a satisfying assignment. The source calls for unconditional superlinear time lower bounds in robust general computation models and ultimately stronger exponential bounds. Many known barriers depend on unproved hypotheses or restrictions on memory and algorithm structure. An unrestricted lower bound would directly demonstrate that a concrete fundamental problem requires more than near-input-reading work. The saved note intentionally states a research direction rather than one fixed exponent, so a finished card must select the encoding, machine model, and quantitative threshold it intends to resolve.

[Read in atlas](index.html#TCS-6934) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6977 — Super-near-linear SAT time lower bounds

SAT asks whether a Boolean formula has a satisfying assignment. The selected question seeks an unconditional lower bound excluding algorithms whose running time stays near the input length. This is a weaker objective than excluding every polynomial-time algorithm, but it must still account for all algorithms in the chosen model. Restrictions on working space can support different lower bounds and should not be silently added to the question. Progress would establish a concrete limit on efficient satisfiability algorithms without needing to settle the full P versus NP problem.

[Read in atlas](index.html#TCS-6977) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6978 — Separating space from comparable time bounds

Time measures how many computational steps an algorithm takes, while space measures how much working memory it uses. A computation can reuse the same memory through a very long sequence of steps. The question seeks a problem solvable within a given space bound that cannot be solved within roughly the same time bound. A precise version must specify the machine model, the resource function, and what slack is allowed by roughly the same. Such a separation would capture a basic advantage of reusable memory that ordinary time and space hierarchy theorems do not directly compare.

[Read in atlas](index.html#TCS-6978) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6979 — Independence of P versus NP

P versus NP asks whether every efficiently verifiable decision problem can also be solved efficiently. The independence question concerns the possibility that a chosen mathematical axiom system proves neither equality nor inequality. This is a question about formal provability, distinct from proposing either an algorithm or a complexity lower bound. Any precise claim must name the axiom system and the assumptions made about its consistency or soundness. Investigating independence could identify limitations of the available foundations or proof methods, without treating the difficulty of existing approaches as evidence that independence must hold.

[Read in atlas](index.html#TCS-6979) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-2464 — Six possibilities for locally sampled uniform symmetric distributions

Each output bit of a local sampler reads only a bounded number of independent random input bits. Suppose its output is close to a distribution uniform over a symmetric set of bit strings. The output must then be close to one of six possibilities: two point masses, their equal mixture, two parity classes, or the whole cube. The closeness loses only an absolute constant factor, independent of locality. The 2023 conjecture was resolved in work published at STOC 2025.

[Read in atlas](index.html#TCS-2464) · [Sampling and Certifying Symmetric Functions](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.36) · [Locally Sampleable Uniform Symmetric Distributions](https://arxiv.org/abs/2411.08183)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-3568 — Necessary logarithmic amplification when composing XOR with a total function

The task is to output the parity of n values of the same total Boolean function on separate input blocks. The source asks whether this can require n log n times the cost of computing one value. Cost is worst-case randomized bit queries with error at most one third on every input. A published 2023 corollary gives a growing family of total functions attaining the logarithmic overhead. This resolves the original XOR-or-majority existence question through its XOR alternative.

[Read in atlas](index.html#TCS-3568) · [When Is Amplification Necessary for Composition in Randomized Query Complexity?](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2020.28) · [Optimal Separation and Strong Direct Sum for Randomized Query Complexity](https://doi.org/10.4230/LIPIcs.CCC.2019.29) · [A Strong XOR Lemma for Randomized Query Complexity](https://doi.org/10.4086/toc.2023.v019a011)
Existing status: `resolved` · Summary written: 2026-09-12

## Algorithms (25)

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
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1141 — Near-linear-time approximation of reachability diameter

Reachability diameter measures the largest finite shortest-path distance in a directed graph. Unreachable ordered pairs are omitted so that disconnected directions do not make the answer automatically infinite. The question asks for a constant-factor estimate in near-linear time on every unweighted directed graph. Simple searches from arbitrary pivots can miss a long directed route. A successful method would summarize the extent of reachable routes without computing distances from every vertex or imposing strong connectivity.

[Read in atlas](index.html#TCS-1141) · [Revisiting Diameter in Directed Graphs](https://doi.org/10.4230/LIPIcs.ESA.2026.59)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6783 — Optimal size of four-additive graph spanners

An additive spanner keeps original graph edges while limiting the increase in every pairwise distance. This card fixes the increase to at most four and asks for the optimal worst-case number of edges. The target is the complete asymptotic function up to universal constant factors. The familiar candidate is \(n^{4/3}\), while recent constructions still have exponent \(7/5\) up to logarithmic factors. This gap is a fundamental unresolved regime of distance compression, and the variable-error linear-size tradeoff has its own card.

[Read in atlas](index.html#TCS-6783) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152) · [Finding 4-Additive Spanners: Faster, Stronger, and Simpler](https://arxiv.org/abs/2510.17262) · [The \(4/3\) Additive Spanner Exponent is Tight](https://arxiv.org/abs/1511.00700)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0809 — Mincost flow in planar graphs

Minimum-cost flow routes a prescribed amount of material through capacitated edges while minimizing total cost. The saved question focuses on planar input graphs, where an embedding may constrain the structure of feasible routes. The aim is to understand how that restriction can improve exact optimization. A faster planar algorithm would benefit network tasks requiring both conservation constraints and careful cost accounting. The index does not specify directedness, supply conventions, numerical encoding, or the running-time target, so it cannot yet distinguish a strongly polynomial question from a dependence on capacity magnitudes.

[Read in atlas](index.html#TCS-0809) · [Algorithms for Optimization Problems in Planar Graphs](https://doi.org/10.4230/DagRep.3.10.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1338 — Set-system sparsifiers of size proportional to chain length

A sparsifier retains and reweights a few coordinates while approximately preserving every set’s total weight. The conjecture asks for a support bound proportional to chain length divided by \(\varepsilon ^{2}\). Chain length is measured through the union-closure, so even an incomparable collection of singleton sets can have large chain length. The published upper bound has extra logarithmic factors, which are precisely the remaining loss in the question. A resolution would establish whether this structural parameter completely controls multiplicative sparsification up to a universal constant.

[Read in atlas](index.html#TCS-1338) · [Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction](https://doi.org/10.4230/LIPIcs.ICALP.2026.44)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1617 — Planarity dichotomy for induced subdivision detection

For a fixed graph H, induced-subdivision detection asks whether an input graph contains a subdivided copy of H as an induced subgraph. Extra edges between selected vertices are forbidden. The conjecture concerns patterns H of maximum degree three and predicts tractability exactly for planar patterns, assuming P differs from NP. Existing algorithms and hardness constructions motivate the proposed boundary. This would classify a natural family of pattern-detection problems by a geometric property of the fixed pattern itself.

[Read in atlas](index.html#TCS-1617) · [Induced Disjoint Paths Without an Induced Minor](https://doi.org/10.4230/LIPIcs.ICALP.2025.4)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2018 — Quadratic-size submodular hypergraph sparsifiers

A submodular hypergraph assigns each hyperedge a flexible submodular cost for being split by a cut. A sparsifier retains and reweights hyperedges so that every cut value remains approximately correct. The conjecture proposes a quadratic-in-vertices size bound with inverse-squared accuracy dependence in the source's size measure. Preserving exponentially many cuts simultaneously is the main obstacle identified there. The project seeks a compression theorem extending beyond ordinary all-or-nothing hyperedge cuts to richer models used in optimization and learning.

[Read in atlas](index.html#TCS-2018) · [Cut Sparsification and Succinct Representation of Submodular Hypergraphs](https://doi.org/10.4230/LIPIcs.ICALP.2024.97)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2822 — Complexity of directed detours

The input is an unweighted directed graph with specified endpoints. The problem asks whether any simple path between them is longer than their shortest-path distance. Only one extra edge is required, and no path may repeat a vertex. Planar graphs have polynomial algorithms, but the general directed classification remains open in the checked sources. The NP-completeness of exceeding graph diameter concerns a different problem.

[Read in atlas](index.html#TCS-2822) · [Detours in Directed Graphs](https://doi.org/10.4230/LIPIcs.STACS.2022.29) · [Detours in directed graphs — journal version](https://doi.org/10.1016/j.jcss.2023.05.001) · [Simpler and faster algorithms for detours in planar digraphs](https://arxiv.org/abs/2301.02421)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3263 — Polynomial-time minimum-total-length disjoint paths for fixed k

The graph is undirected and unweighted, with a fixed number k of prescribed terminal pairs. The task is to find vertex-disjoint routes with the smallest possible total number of edges, or report that routing is impossible. Individual routes may need to be longer than their own shortest paths to avoid the others. The source asks for polynomial time at every fixed \(k\ge 3\), allowing the exponent to depend on k. Recent grid and individually-shortest-path results do not settle the general problem, which a 2025 published paper still lists as open for three pairs.

[Read in atlas](index.html#TCS-3263) · [Using a Geometric Lens to Find k Disjoint Shortest Paths](https://doi.org/10.4230/LIPIcs.ICALP.2021.26) · [Packing Short Cycles](https://doi.org/10.1145/3765285) · [Shortest Disjoint Paths on a Grid](https://doi.org/10.1137/1.9781611977912.14) · [Planar Disjoint Shortest Paths is Fixed-Parameter Tractable](https://arxiv.org/abs/2505.03353)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3346 — Quasipolynomial dependence on vertices for hypergraph isomorphism

Hypergraph isomorphism compares set systems up to a relabeling of their underlying vertices. The saved question asks for running time quasipolynomial in the number of vertices and polynomial in the hypergraph's full size. Separating these two dependencies matters when many hyperedges are present over a comparatively small vertex set. Such an algorithm would extend efficient symmetry testing to richer relational objects. The excerpt does not define representation conventions or reproduce the cited baseline, so the requested asymptotic form is preserved without asserting which existing method is optimal.

[Read in atlas](index.html#TCS-3346) · [Graph Isomorphism in Quasipolynomial Time Parameterized by Treewidth](https://doi.org/10.4230/LIPIcs.ICALP.2020.103)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4417 — Linear-time directed bottleneck paths and trees

A bottleneck path minimizes its heaviest edge, and a rooted bottleneck tree minimizes the heaviest edge needed to reach all vertices. The open target is expected linear total time for exact solutions on arbitrary directed graphs using only comparisons of edge weights. The source already achieves a very slowly growing overhead and gives linear time in the stronger word-RAM model. The path and tree targets are equivalent at the expected-linear scale through the source reductions. An August 2026 preprint corrects a related graphical-games claim and continues to state the comparison-based path question as open.

[Read in atlas](index.html#TCS-4417) · [Bottleneck Paths and Trees and Deterministic Graphical Games](https://doi.org/10.4230/LIPIcs.STACS.2016.27) · [Bottleneck Paths Reduce to Deterministic Graphical Games and a Counterexample to a Claimed Linear-Time Algorithm](https://arxiv.org/abs/2608.04279)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5705 — Logarithmic adjacency labels for monotone graph classes

Adjacency labels encode a graph so that two vertex labels alone determine whether their vertices are adjacent. The relevant source passage concerns hereditary small graph classes, whose total number of labeled graphs grows only factorially times exponentially. It asks whether every such class admits logarithmic-size labels. A counting bound limits overall information but does not automatically make that information locally decodable. The project explores whether this stronger growth restriction can restore compact representations after broader implicit-representation conjectures fail.

[Read in atlas](index.html#TCS-5705) · [Tight Bounds on Adjacency Labels for Monotone Graph Classes](https://doi.org/10.4230/LIPIcs.ICALP.2024.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5969 — Complexity of planar 3-edge-colorability

Three-edge-colorability asks whether the edges of a graph can receive three colors with different colors on every pair meeting at a vertex. The selected question asks for the computational complexity of this decision problem on planar graphs. The source studies a sufficient route through augmentation to a planar cubic bridgeless supergraph, where three-edge-colorability follows from the Four-Color Theorem. It also discusses a conjectured characterization for two-connected planar graphs of maximum degree three. A full classification would determine whether the remaining planar cases admit an efficient coloring test or conceal an NP-hard obstruction.

[Read in atlas](index.html#TCS-5969) · [Efficient Recognition of Subgraphs of Planar Cubic Bridgeless Graphs](https://doi.org/10.4230/LIPIcs.ESA.2022.62)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6173 — Three disjoint directed shortest paths

The directed disjoint-shortest-paths problem asks for paths connecting prescribed source-target pairs, with each path individually shortest and the paths mutually vertex-disjoint. The source highlights the case of three pairs and asks whether it can be solved in polynomial time. Polynomial algorithms for each fixed number of pairs in undirected graphs do not immediately extend when edge directions constrain route choices. Its local-to-global structural results suggest tools for understanding how directed shortest paths can intersect, but do not settle the algorithmic question. Resolving this small case would clarify a basic obstacle in routing several optimal paths through a directed network.

[Read in atlas](index.html#TCS-6173) · [A Local-To-Global Theorem for Congested Shortest Paths](https://doi.org/10.4230/LIPIcs.ESA.2023.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6251 — Polynomial-time independent set under a forbidden forest

Fix a forest whose components are paths or subdivided three-leaf claws. Given a graph with no induced copy of that forest, find an independent vertex set of maximum total weight. The question asks for polynomial time for every fixed forbidden forest, with the polynomial allowed to depend on that forest. The input graph may have arbitrarily large degree, cliques and bicliques. Quasipolynomial algorithms now cover the whole family, but known general results still fall short of polynomial time.

[Read in atlas](index.html#TCS-6251) · [Max Weight Independent Set in Graphs with No Long Claws: An Analog of the Gyárfás' Path Argument](https://doi.org/10.4230/LIPIcs.ICALP.2022.93) · [Maximum Weight Independent Set in Graphs with no Long Claws in Quasi-Polynomial Time](https://doi.org/10.1145/3618260.3649791) · [Graphs with No Long Claws: An Improved Bound for the Analog of the Gyárfás’ Path Argument](https://doi.org/10.4230/LIPIcs.MFCS.2025.28)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6270 — Near-linear-query reconstruction of bounded-degree graphs

All vertices of a connected bounded-degree graph are known, but its edges are hidden. One query returns only the shortest-path distance between two named vertices. The goal is to recover every edge using a linear number of vertices times polylogarithmically many expected queries. The expectation is over the algorithm’s randomness for each fixed graph, and the returned answer must be exact. Near-linear results for random regular or bounded-treelength graphs do not cover every graph in the question.

[Read in atlas](index.html#TCS-6270) · [A Simple Algorithm for Graph Reconstruction](https://doi.org/10.4230/LIPIcs.ESA.2021.68) · [Cutwidth Versus BFS-Width with Applications to Graph Reconstruction from Distance Queries](https://doi.org/10.4230/LIPIcs.SWAT.2026.24) · [Reconstructing Bounded Treelength Graphs with Linearithmic Shortest Path Distance Queries](https://arxiv.org/abs/2603.10432)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6421 — Isomorphism dichotomy for finitely forbidden hereditary classes

Hereditary graph classes can be specified by finitely many forbidden induced subgraphs. The question asks whether graph isomorphism on such a class can have complexity intermediate between polynomial time and general graph-isomorphism completeness. The source establishes broad classifications and resolves most two-forbidden-pattern cases. Results for forbidden ordinary subgraphs do not immediately extend to induced exclusions. The project seeks a dichotomy explaining whether a finite structural prohibition always makes isomorphism substantially easier or leaves its full general difficulty intact.

[Read in atlas](index.html#TCS-6421) · [Towards an Isomorphism Dichotomy for Hereditary Graph Classes](https://doi.org/10.4230/LIPIcs.STACS.2015.689)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6433 — Polynomial-time Győri–Lovász partitions

The Gyori-Lovasz theorem guarantees connected graph partitions with prescribed part sizes and one prescribed root in each part. The graph's connectivity matches the number of requested parts. The source asks for a polynomial-time construction under the theorem's original assumptions, already for five parts. It obtains constructive results under stronger connectivity or additional graph structure. The project aims to extract an efficient algorithm from a powerful existence theorem while meeting all size, connectivity, and root constraints simultaneously.

[Read in atlas](index.html#TCS-6433) · [Connected Partitions via Connected Dominating Sets](https://doi.org/10.4230/LIPIcs.ESA.2025.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6784 — Spanners matching Thorup–Zwick emulator tradeoffs

An emulator may add weighted shortcut edges, whereas a spanner must use actual edges from the input graph. Thorup-Zwick style constructions offer useful distance-error and size tradeoffs in the more permissive setting. The source asks whether comparable tradeoffs can be realized by genuine spanners. Replacing each shortcut with a path may greatly increase the total number of retained edges. The project seeks shared path structure that can recover the emulator's compactness without relying on artificial metric connections.

[Read in atlas](index.html#TCS-6784) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6785 — Optimal additive error of linear-size spanners

A linear-size spanner retains only a constant number of edges per vertex on average. For arbitrary graphs, this severe sparsity budget can force shortest paths to become longer. The source asks for the smallest additive error that can always be guaranteed under that budget. The error may grow with graph size, unlike a fixed additive approximation target. The project seeks matching constructions and lower bounds describing the exact amount of metric accuracy necessarily lost when a graph is compressed to linear edge count.

[Read in atlas](index.html#TCS-6785) · [Graph spanners: a tutorial review](https://arxiv.org/abs/1909.03152)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7061 — Dichotomy for hereditary edge deletion

A hereditary graph class is closed under taking induced subgraphs. The survey proposes a polynomial-time versus NP-hard dichotomy for edge deletion into such classes. The task is to identify which target properties permit efficient optimal repair and which force classical intractability. A general criterion would unify many individually studied modification problems through the structure of their target classes. The saved record explicitly treats this as a research direction and does not specify representation or decidability assumptions for the hereditary classes under consideration.

[Read in atlas](index.html#TCS-7061) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7075 — Complexity of general vertex-connectivity augmentation

Vertex-connectivity measures how many vertex failures a graph can tolerate before becoming disconnected. Connectivity augmentation adds edges to raise that resilience level. The saved question asks for the complexity of unrestricted augmentation when the requested increase exceeds one. This probes whether techniques for a single increment can handle several interacting layers of required redundancy. The survey note does not specify edge costs or the optimization budget, so those conventions still need recovery before a precise polynomial-time or hardness statement can be formulated.

[Read in atlas](index.html#TCS-7075) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7146 — Polynomial-time detection of fixed pivot- and vertex-minors

Pivot-minor and vertex-minor containment ask whether a target graph can be obtained through their respective local transformations and deletions. The source asks for polynomial-time detection when the target graph is fixed. Fixing the target permits constants and exponents to depend on it while the host graph grows. An algorithm would make these structural relations useful as effectively testable graph-class restrictions. The saved formulation does not request a uniform fixed-parameter bound in target size, and the distinction matters when assessing whether a target-specific polynomial algorithm settles the intended question.

[Read in atlas](index.html#TCS-7146) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800)
Existing status: `source_open` · Summary written: 2026-09-11

## Automata and formal languages (35)

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

### TCS-0164 — Equivalence for unambiguous grammars

An unambiguous context-free grammar assigns at most one parse tree to each generated word. Given two grammars promised to have this property, the project asks whether equality of their languages is decidable. The promise limits competing derivations without making the grammars deterministic. Enumeration can expose a word accepted by only one grammar, but agreement on finitely many words does not certify equivalence. A decision procedure would locate an important boundary between deterministic language comparison and the unrestricted context-free equivalence problem.

[Read in atlas](index.html#TCS-0164) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#equivalence-of-unambiguous-context-free-grammars)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0146 — Complexity of universality for unambiguous context-free grammars

An unambiguous context-free grammar has at most one derivation tree for any particular word. Its universality problem asks whether it generates every word over its alphabet. The source places this decidable task between a polynomial-time lower bound and a polynomial-space upper bound and asks to tighten that gap. Unambiguity removes duplicate derivations but still permits dependencies that a deterministic pushdown presentation cannot express. Better bounds would measure how expensive exhaustive language coverage becomes when unique parsing replaces deterministic parsing as the structural promise.

[Read in atlas](index.html#TCS-0146) · [Automata Exchange](https://automata.exchange/19.05-on-unambiguous-grammars/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0135 — Zeroness problem

A machine with numerical outputs may compute zero on every input despite having nontrivial internal computations. The zeroness project asks when this universal identity is decidable and how expensive the decision is. The source highlights weighted grammars over fields, unary polynomial automata, weighted Parikh automata and weighted vector addition systems. These are separate representations whose algebraic operations and storage affect the available arguments. Understanding their zero tests would also provide building blocks for comparing quantitative descriptions, where cancellation can hide differences between runs.

[Read in atlas](index.html#TCS-0135) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
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

### TCS-0133 — Stronger versions of inclusion of probabilistic automata

Probabilistic automata assign acceptance probabilities through weighted choices among runs. The source asks for an unconditional decidability proof of language containment when the machines have bounded ambiguity. Its existing conditional route relies on Schanuel's conjecture, linking the comparison to difficult arithmetic questions. Bounded ambiguity limits accepting computations but does not immediately eliminate the numerical relationships involved in containment. Removing that conjectural assumption would establish that the relevant probabilistic language comparison has a terminating algorithm on the stated structural class.

[Read in atlas](index.html#TCS-0133) · [Unambiguity in Automata Theory](https://doi.org/10.4230/DagRep.11.10.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0154 — Separating words problem

Two distinct binary words may be separated by a finite automaton that accepts one and rejects the other. The project asks how many states always suffice when both words have length n. The source proposes a logarithmic target and also asks for improvements toward an n-to-the-one-third scale. A separating automaton may be tailored to the particular pair, so it need not recognize an entire difficult language. Sharp bounds would measure the finite-state resources required to detect just one difference between two long strings.

[Read in atlas](index.html#TCS-0154) · [Automata Exchange](https://automata.exchange/19.04-separating-words-problem/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0871 — Universality and inclusion of AC-recognizable languages

Associative-commutative tree automata recognize terms modulo the equations attached to designated function symbols. The source asks whether universality and language inclusion can be decided for the general automaton model. Its later remark reports undecidability of inclusion, leaving universality as the unresolved part of that original pair. Restricting transition forms yields a better-behaved subclass, but those procedures do not cover the full model. Understanding universality would determine whether exhaustive acceptance remains checkable despite the more powerful equational treatment of tree structure.

[Read in atlas](index.html#TCS-0871) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/101.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2243 — \(\mathrm{TC}^{0}/\mathrm{NC}^{1}\) complexity dichotomy

Visibly pushdown languages are recognized by automata whose input symbols determine whether the stack is pushed, popped, or left unchanged. The question asks whether their computational complexity has a dichotomy between membership in TC0 and NC1-completeness. TC0 allows constant-depth polynomial-size circuits with threshold gates, whereas NC1 allows logarithmic-depth bounded-fan-in circuits. The source studies effective low-depth classifications and identifies cases where existing algebraic methods leave significant uncertainty. A dichotomy would rule out intermediate behavior in this structured language family and clarify which stack computations inherently require greater parallel depth.

[Read in atlas](index.html#TCS-2243) · [The \(\mathrm{AC}^{0}\)-Complexity of Visibly Pushdown Languages](https://doi.org/10.4230/LIPIcs.STACS.2024.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3378 — Low-complexity aperiodic two-dimensional shifts of finite type

Two-dimensional shifts of finite type impose finitely many local constraints on tilings. The source conjectures that low pattern complexity rules out aperiodicity even when patterns are measured using arbitrary shapes. This extends a periodicity principle beyond the shapes handled by the cited corollaries. A proof would connect a numerical limit on local diversity with the existence of global repeating structure. The source's definition of low complexity and its quantification over shapes are missing from the excerpt, so those conditions must be recovered before asserting a universal tiling periodicity theorem.

[Read in atlas](index.html#TCS-3378) · [Decidability and Periodicity of Low Complexity Tilings](https://doi.org/10.4230/LIPIcs.STACS.2020.14)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3863 — Containment of finitely ambiguous automata

Quantitative containment compares two probabilistic automata pointwise over all input words. The project asks whether this comparison is decidable when both automata have uniformly bounded numbers of accepting runs. The source handles cases with one unambiguous side using conditional arithmetic decision procedures. Allowing bounded multiplicity on both sides requires comparing sums of exponential terms and removes useful geometric structure from that argument. A resolution would show whether finite ambiguity suffices to control exact probabilistic comparison even when neither machine has unique accepting behavior.

[Read in atlas](index.html#TCS-3863) · [When is Containment Decidable for Probabilistic Automata?](https://doi.org/10.4230/LIPIcs.ICALP.2018.121)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4575 — Universality of discounted-sum automata

A discounted-sum automaton assigns an infinite word a value in which later transition weights receive progressively less influence. Its universality problem asks whether every word satisfies the specified quantitative acceptance requirement. The source points to this decision question while studying strategies that force an exact discounted payoff. Exact equality and universal quantification are delicate because arbitrarily late contributions can still affect the final value. Decidability would strengthen the foundations of verification for quantitative specifications where future rewards are discounted but never entirely ignored.

[Read in atlas](index.html#TCS-4575) · [Quantitative Games with Interval Objectives](https://doi.org/10.4230/LIPIcs.FSTTCS.2014.365)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4636 — Decidability of definability with modular predicates

The source studies which regular languages can be described in logical fragments over ordered word positions. Its general question asks whether decidability of definability in a fragment using order survives the addition of modular numerical predicates. These predicates can test positions or word lengths modulo a fixed integer, increasing the language's expressive resources. The issue is recognizing whether a given regular language belongs to the logical fragment, rather than the satisfiability of an arbitrary formula. A preservation theorem would transfer existing classification algorithms to enriched logics, but the 2013 discussion leaves the necessary conditions on the fragment open.

[Read in atlas](index.html#TCS-4636) · [Two-variable first order logic with modular predicates over words](https://doi.org/10.4230/LIPIcs.STACS.2013.329)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4659 — Determinacy of Wadge games for Muller tree languages

Two players build infinite labeled trees and compare their membership in two regular tree languages. The second player may delay output but must eventually build a full infinite tree. The question asks whether ZFC proves that one player always has a winning strategy. Muller automata may recognize non-Borel languages, so the Borel theorem alone is insufficient. Known word-game independence and long regular-tree hierarchy constructions do not settle this universal tree question.

[Read in atlas](index.html#TCS-4659) · [The Determinacy of Context-Free Games](https://doi.org/10.4230/LIPIcs.STACS.2012.555) · [The Determinacy of Context-Free Games — journal version](https://doi.org/10.2178/jsl.7804050) · [On the topological complexity of tree languages](https://www.mimuw.edu.pl/~niwinski/Prace/lobo_d.pdf) · [Wadge-Wagner Hierarchy of Regular Tree Languages](https://www.ims.uni-stuttgart.de/events/TTATT2016/proceedings.pdf)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4677 — Deciding first-order definability of orbit-finite automata

Orbit-finite automata recognize data words using infinitely many states organized into finitely many symmetry classes. The project asks whether first-order definability of the recognized language can be decided. The source conjectures that aperiodicity of the syntactic monoid provides the correct criterion within this automaton class. Infinite-data languages outside the class show that aperiodicity alone is not a universal characterization. Proving an effective criterion would extend a central connection between finite automata, algebra and logic to a controlled infinite-alphabet setting.

[Read in atlas](index.html#TCS-4677) · [Data Monoids](https://doi.org/10.4230/LIPIcs.STACS.2011.105)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-0121 — Decidability of $(\min,+)$-weighted automata determinization

A min-plus weighted automaton assigns each finite word the minimum accumulated cost of its runs. The historical question asks whether the existence of an equivalent deterministic weighted automaton can be decided. Almagor, Arbel and Sheinvald settled this positively in a 2025 preprint published at SODA 2026. Their LICS 2026 follow-up supplies a primitive-recursive complexity upper bound. The card is retained as a resolved record, with unrestricted ambiguity and the endpoint-weight conventions included.

[Read in atlas](index.html#TCS-0121) · [Automata Exchange](https://automata.exchange/22.05-decidability-of-min-plus-weighted-automata-determinization/) · [Determinization of Min-Plus Weighted Automata is Decidable](https://arxiv.org/abs/2503.23826v1) · [Determinization of Min-Plus Weighted Automata is Decidable](https://epubs.siam.org/doi/10.1137/1.9781611978971.11) · [A Complexity Bound for Determinisation of Min-Plus Weighted Automata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.5)
Existing status: `resolved` · Summary written: 2026-09-11

### TCS-3553 — Computing measures of all regular languages of infinite trees

A tree language describes which labelled branching structures satisfy a specification. The source asks whether its probability can be computed for every regular language, beyond weak automata. The probability is over independent uniform labels, or more generally a finite rational branching process. A 2023 theorem computes an exact algebraic answer for arbitrary parity tree automata. The full version, published in JACM in 2026, resolves the original computability question.

[Read in atlas](index.html#TCS-3553) · [Computing Measures of Weak-MSO Definable Sets of Trees](https://doi.org/10.4230/LIPIcs.ICALP.2020.136) · [The Probabilistic Rabin Tree Theorem](https://doi.org/10.1109/LICS56636.2023.10175800) · [On the Computability of Measures of Regular Sets of Infinite Trees](https://arxiv.org/abs/2304.12158) · [On the Computability of Measures of Regular Sets of Infinite Trees](https://doi.org/10.1145/3819061)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-4673 — Collapse versus arbitrary higher-order stacks

Higher-order stacks consist of stacks nested inside other stacks. Collapse follows information recorded when a symbol was pushed. The historical question asks whether any number of ordinary nesting levels can always replace this operation. A later theorem proves that one deterministic order-two collapsible language defeats every deterministic ordinary order. The result concerns finite words over a finite alphabet and does not extend its claim to nondeterministic competitors.

[Read in atlas](index.html#TCS-4673) · [Collapse Operation Increases Expressive Power of Deterministic Higher Order Pushdown Automata](https://doi.org/10.4230/LIPIcs.STACS.2011.603) · [On the Expressive Power of Higher-Order Pushdown Systems](https://lmcs.episciences.org/6723)
Existing status: `resolved` · Summary written: 2026-09-12

## Semantics, logic and verification (41)

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

Parity games ask which player can force an infinite play whose minimum infinitely recurring priority has the desired parity. The target is a uniform deterministic polynomial-time decision algorithm for arbitrary finite arenas and binary-encoded priorities. Quasipolynomial algorithms and lower bounds for separating-automaton methods are known. A November 2025 preprint claims a polynomial-time solution, but this review did not establish its correctness. A separate April 2026 paper still treats the question as open, so the completed card explicitly records an unverified current status.

[Read in atlas](index.html#TCS-4245) · [Deciding Parity Games in Quasipolynomial Time](https://www.cs.auckland.ac.nz/~cristian/crispapers/paritygame-stoc.pdf) · [Universal trees grow inside separating automata: Quasi-polynomial lower bounds for parity games](https://arxiv.org/abs/1807.10546) · [Attractors Is All You Need: Parity Games In Polynomial Time](https://arxiv.org/abs/2511.03752v1) · [On the Complexity of Robust Markov Decision Processes and Bisimulation Metrics](https://arxiv.org/abs/2604.26748)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5773 — Skolem problem

The Skolem problem asks whether an integer linear recurrence ever has a zero term. Its order, coefficients and initial values form a finite binary input, with no restriction to simple or non-degenerate sequences. The classical structural theorem about zero sets does not provide an unconditional decision procedure for every recurrence. The reviewed July 2026 results establish stronger low-order bounds and a general conditional decidability theorem, leaving the unrestricted unconditional target unresolved. The completed card preserves the original identifier and source while spelling out the exact discrete recurrence model.

[Read in atlas](index.html#TCS-5773) · [Skolem Meets Schanuel](https://doi.org/10.4230/LIPIcs.MFCS.2022.20) · [On the Complexity of the Skolem Problem at Low Orders](https://arxiv.org/abs/2507.11234v3) · [Conjectural Decidability of the Skolem Problem](https://arxiv.org/abs/2607.15510)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6568 — Mean-payoff games in polynomial time

In a mean-payoff game, two players move a token through a finite weighted directed graph. The maximizing player wants the limiting lower average weight to be nonnegative against every opposing strategy. The project asks whether this threshold question has a deterministic algorithm polynomial in the full binary input length. Algorithms polynomial in the numerical magnitude of weights do not suffice because a large weight can have a short encoding. An efficient solution would settle a central exact optimization problem for systems with long-run rewards and adversarial control.

[Read in atlas](index.html#TCS-6568) · [The complexity of mean payoff games](https://link.springer.com/chapter/10.1007/BFb0030814) · [Faster Algorithms for Mean-Payoff Games](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf) · [Value Iteration Using Universal Graphs and the Complexity of Mean Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2020.34) · [Smoothed Analysis of Deterministic Discounted and Mean-Payoff Games](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.147) · [Strategy Improvement, the Simplex Algorithm and Lopsidedness](https://arxiv.org/abs/2509.16075) · [Set-defined graph classes: \(\chi\)-boundedness meets tropical algebra](https://arxiv.org/abs/2607.23754)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6566 — Continuous Skolem problem

A rational linear differential system evolves as a matrix exponential applied to its initial state. Continuous Skolem asks whether a specified linear observation of that trajectory is exactly zero at some nonnegative real time. The dimension is unrestricted, and the project seeks decidability without a time horizon. Approaching zero or changing sign are inadequate substitutes because trajectories may approach without hitting or touch zero without crossing it. A resolution would establish the limits of exact reachability verification even for continuous systems with linear, fully specified dynamics.

[Read in atlas](index.html#TCS-6566) · [The continuous Skolem-Pisot problem](https://perso.uclouvain.be/vincent.blondel/publications/10BDJ.pdf) · [On the Skolem Problem for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1506.00695) · [On Recurrent Reachability for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1507.03632) · [Axiomatization of Compact Initial Value Problems: Open Properties](https://publikationen.bibliothek.kit.edu/1000188295/170660770) · [A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7192 — Decidability of multiplicative-exponential linear logic

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

### TCS-0640 — Shortest runs in 3-D VASS

A three-dimensional VASS is a finite-state system with three nonnegative integer counters. The source asks whether some reachable instances require shortest runs longer than every single-exponential bound in their binary input length. Encoding a large initial counter in binary already permits exponentially many necessary steps, so a stronger growth rate is required. A July 2026 preprint states a doubly-exponential upper bound, improving the triple-exponential bound from 2025. The remaining threshold question measures how much reachability-witness complexity three counters can force.

[Read in atlas](index.html#TCS-0640) · [Shortest runs in 3-D VASS](https://automata.exchange/19.11-shortest-runs-in-3-d-vass/) · [Reachability in 3-VASS is Elementary](https://arxiv.org/abs/2502.13916) · [3-VASS Reachability is in EXPSPACE](https://arxiv.org/abs/2607.14983)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0913 — Word problem for the S-combinator

The S-combinator is governed by the single rule that rewrites S applied to x, y and z into the application of xz to yz. This project asks whether convertibility of two closed terms built only from S and application is decidable. Conversion allows the equivalence generated by the rule, rather than requiring one particular forward evaluation path. Knowing whether an individual term normalizes does not automatically compare arbitrary nonnormalizing terms. A decision procedure would show how far removing all other combinators simplifies symbolic equality.

[Read in atlas](index.html#TCS-0913) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/97.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0896 — Recursive normalizing strategies for Church–Rosser rewriting

A normalizing reduction strategy finds a normal form whenever the input term has one. The project asks whether every finitely generated, full Church-Rosser rewriting system admits a recursive strategy choosing one rewrite step at a time. Fullness includes every term constructible from the signature, while Church-Rosser ensures compatible reduction outcomes. The source notes that dropping any assumption permits counterexamples and that weakly orthogonal systems satisfy the claim. Resolving the general case would connect existence of confluent normal forms with an effective sequential way to reach them.

[Read in atlas](index.html#TCS-0896) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/10.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0901 — Decidability of one-rule linear rewriting termination

A rewrite system with one rule can still generate infinitely many terms through repeated substitution and rewriting. The project asks whether termination is decidable when the rule is linear on both its left and right sides. Linearity prevents repeated occurrences of a variable within either side, limiting copying and equality tests. The source emphasizes that left-linearity alone does not suffice and identifies one-rule string rewriting as a related restricted target. A procedure or undecidability construction would sharpen how little symbolic machinery can already encode unbounded computation.

[Read in atlas](index.html#TCS-0901) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/21.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0092 — Complete methods for fair almost-sure termination

Probabilistic programs with nondeterministic choices combine random transitions with decisions made by a scheduler. Here fairness requires every nondeterministic transition enabled infinitely often along an infinite execution to be taken infinitely often. The project asks the recursion-theoretic complexity of termination with probability one under every fair scheduler. It separately seeks sound and complete proof techniques for establishing that property. The interaction between fairness and probability makes this more subtle than either ordinary termination or almost-sure termination under an unrestricted scheduling convention.

[Read in atlas](index.html#TCS-0092) · [Automata Exchange](https://automata.exchange/25.19-complete-techniques-for-deducing-fair-almost-sure-termination/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1649 — Decidability of branching-VASS reachability

A branching vector addition system with states combines nonnegative counters with computations that can split into several branches. Reachability asks whether an initial configuration can produce an accepting computation satisfying the required final configurations. The problem is to determine whether this question is decidable when the counter dimension is arbitrary. The source develops a decision procedure in dimension two, while noting that its approach does not supply a complexity upper bound there. Extending decidability beyond this restricted dimension would explain how branching changes the algorithmic behavior of counter systems compared with ordinary Petri nets.

[Read in atlas](index.html#TCS-1649) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://doi.org/10.4230/LIPIcs.MFCS.2025.22)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1659 — Decidability of Bellman-operator reachability

Bellman operators of Markov decision processes define structured piecewise affine dynamics on probability vectors. The source studies whether iterating such an operator can reach a specified vector, including its fixed point. Its remaining semigroup question concerns systems in which a state can have several tight actions, producing multiple possible matrices in the associated reachability analysis. With a unique tight action at every state, stabilization of matrix kernels supplies a decision procedure, but this argument fails for products of different matrices. Resolving the multiple-action case would extend exact reachability analysis beyond the linear behavior of a single optimal policy.

[Read in atlas](index.html#TCS-1659) · [On Piecewise Affine Reachability with Bellman Operators](https://doi.org/10.4230/LIPIcs.MFCS.2025.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2033 — Complexity of one-dimensional grammar-controlled VAS

A one-dimensional grammar-controlled vector addition system combines a nonnegative counter with transition sequences generated by a context-free grammar. The problem asks for the computational complexity of reachability in this model. The source discusses a proposed decidability argument cautiously and separates that issue from obtaining useful upper and lower complexity bounds. One difficulty is that very small grammars can generate enormous finite reachable sets, while the source lacks examples forcing more than exponentially long shortest derivations. Understanding this mismatch could reveal whether compact derivations permit efficient reachability analysis despite the numerical growth of counter values.

[Read in atlas](index.html#TCS-2033) · [Challenges of the Reachability Problem in Infinite-State Systems (Invited Paper)](https://doi.org/10.4230/LIPIcs.MFCS.2024.2)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3031 — Consistency of excluded middle and Church’s thesis in Coq

Church's thesis, as a type-theoretic axiom, says that every total function from natural numbers to natural numbers has a computational realization. The law of excluded middle supplies classical reasoning about propositions, and its compatibility with that thesis depends on the surrounding logical rules. The source conjectures that both axioms can consistently coexist in Coq because elimination from general propositions into computational types is restricted. This restriction prevents some classical existence proofs from automatically producing data, especially without additional choice principles. A consistency model would clarify how classical propositional reasoning can be combined with a constructive account of all representable numerical functions.

[Read in atlas](index.html#TCS-3031) · [Church’s Thesis and Related Axioms in Coq’s Type Theory](https://doi.org/10.4230/LIPIcs.CSL.2021.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3344 — Decidability of rounded planar-rotation reachability

Rounded linear dynamics repeatedly applies a rational matrix and then rounds coordinates to a fixed digital grid. Point-to-point reachability asks whether the resulting orbit ever visits a specified target vector exactly. The source highlights the decidability problem even when the matrix is a rotation in two dimensions. Although unrounded rotation is simple, accumulated rounding errors can produce discrete orbits whose boundedness and eventual periodicity are difficult to control. Resolving this case, with the rounding rule specified as in the model, would clarify a basic limit of verification for numerical systems operating at fixed precision.

[Read in atlas](index.html#TCS-3344) · [Reachability in Dynamical Systems with Rounding](https://doi.org/10.4230/LIPIcs.FSTTCS.2020.36)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3655 — Inductive-inductive types from inductive types without UIP

Inductive-inductive types define several mutually dependent sorts, allowing later sorts to be indexed by earlier ones. They conveniently express structures such as contexts and the types that are well formed within those contexts. The question asks whether these types can be constructed from ordinary inductive types without assuming uniqueness of identity proofs. The source's reduction relies on settings where equality is simpler, and removing that assumption requires rebuilding signatures, semantics, and the term-model construction. A successful reduction would show that this useful dependent form of mutual induction does not require an additional primitive in a richer theory of equality.

[Read in atlas](index.html#TCS-3655) · [For Finitary Induction-Induction, Induction Is Enough](https://doi.org/10.4230/LIPIcs.TYPES.2019.6)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4017 — Axiomatizing positive relation calculus with transitive closure

The positive calculus of binary relations combines operations such as union, composition, and intersection without unrestricted complementation. Adding transitive closure makes it possible to express repeated transitions and reachability. The source asks for a sound and complete axiomatization, including whether Kleene algebra axioms suffice alongside a complete axiomatization of representable allegories. Intersection is the main obstacle, since fragments without it admit stronger existing algebraic completeness results. A satisfactory axiom system would support systematic equational proofs about relational programs and graph paths using a manageable collection of general reasoning principles.

[Read in atlas](index.html#TCS-4017) · [On the Positive Calculus of Relations with Transitive Closure](https://doi.org/10.4230/LIPIcs.STACS.2018.3)
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

### TCS-6036 — Decidability of restricted elementary real functions

First-order theories of the real numbers become more expressive when exponential and trigonometric functions are added. The selected question concerns decidability for restricted elementary functions, both with and without unrestricted exponentiation. Restricting sine and cosine to bounded intervals avoids the unrestricted oscillation that would immediately complicate logical descriptions. The source cites decidability conditional on Schanuel's conjecture and uses these theories to synthesize invariants of continuous linear systems. An unconditional decision procedure would remove a number-theoretic assumption from reasoning about these analytic descriptions and the safety properties they can certify.

[Read in atlas](index.html#TCS-6036) · [Invariants for Continuous Linear Dynamical Systems](https://doi.org/10.4230/LIPIcs.ICALP.2020.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6112 — Univalence, impredicativity and propositional resizing

An impredicative universe supports quantification over types without the usual increase in universe size, while univalence connects equivalence with equality. Propositional resizing adds the requirement that large propositions have equivalent small representatives. The source asks for a model of type theory supporting all three features together. Its cubical assembly construction provides univalence and impredicativity but fails resizing, and a related positive model weakens identity and dependent-product structure. Constructing a model with the intended ordinary type-theoretic rules would clarify whether these attractive foundational principles can coexist without sacrificing essential forms of dependent reasoning.

[Read in atlas](index.html#TCS-6112) · [Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing](https://doi.org/10.4230/LIPIcs.TYPES.2018.7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6245 — Exponential witness bounds for three-dimensional VAS

Reachability in a three-dimensional vector addition system asks for a legal counter run connecting an initial and a target configuration. The source highlights the gap in understanding how long the shortest such run may need to be. Its concrete question is whether existence of any run always guarantees one of at most exponential length in the input size. Known short-run arguments in two dimensions motivate this possibility, while much larger general upper bounds leave room for doubly exponential or faster growth. Settling the witness-length question would illuminate why adding a third counter changes the structure of exact reachability.

[Read in atlas](index.html#TCS-6245) · [Involved VASS Zoo (Invited Talk)](https://doi.org/10.4230/LIPIcs.CONCUR.2022.5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6279 — Milner’s completeness problem for regular expressions

Regular expressions can describe branching processes as well as word languages, and bisimulation compares their stepwise behavior. Milner's completeness question asks whether the proposed axiom system proves every equality between bisimilar regular-expression processes. This is stronger than checking that the axioms are sound and differs from the familiar equational theory of language equivalence. The 2021 source suggests using coequations and coalgebraic methods developed for Guarded Kleene Algebra with Tests to advance the completeness argument. The research project connects operational process semantics with a deductive account of iteration, choice, and sequential composition.

[Read in atlas](index.html#TCS-6279) · [Guarded Kleene Algebra with Tests: Coequations, Coinduction, and Completeness](https://doi.org/10.4230/LIPIcs.ICALP.2021.142)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-4640 — Reachability in piecewise-affine integer dynamics

Iterate a finite piecewise-affine integer map from a specified starting vector. Ask whether one specified integer target is ever reached. The source already states PSPACE-completeness in one dimension and undecidability in two. Its extracted question introduced this known task rather than an open problem. Separate questions about restricted universal mortality are not substituted here.

[Read in atlas](index.html#TCS-4640) · [Mortality of Iterated Piecewise Affine Functions over the Integers: Decidability and Complexity (Extended Abstract)](https://doi.org/10.4230/LIPIcs.STACS.2013.514)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-5600 — An elementary upper bound for vector-addition-system reachability

A vector addition system repeatedly adds permitted integer vectors while keeping every counter nonnegative. Exact reachability asks whether a given initial vector can reach a specified target after finitely many such steps. The historical question asks whether one algorithm can decide all instances within a fixed-height tower of exponentials in the input length. The non-elementary lower bound published at STOC 2019 and in JACM 2021 rules out every such bound. The card therefore records a resolved negative answer, with the general model kept separate from the polynomial-growth subclass named in the original paper.

[Read in atlas](index.html#TCS-5600) · [Polynomial Vector Addition Systems With States](https://doi.org/10.4230/LIPIcs.ICALP.2018.134) · [The Reachability Problem for Petri Nets Is Not Elementary](https://doi.org/10.1145/3422822) · [Reachability in Vector Addition Systems is Ackermann-complete](https://arxiv.org/abs/2104.13866v4) · [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.22)
Existing status: `resolved` · Summary written: 2026-09-11

## Distributed, parallel and sublinear algorithms (66)

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

### TCS-0998 — Sketching vs. Streaming

A streaming algorithm compresses an input while processing it sequentially, whereas a sketch supports computation from independently prepared summaries. The source asks whether efficient streaming for symmetric functions can generally be converted into efficient sketching. It frames the issue through one-way communication versus simultaneous messages to a referee. The concrete challenge is to find natural functions with a substantial gap or establish a transformation under suitable symmetry assumptions. This would clarify when the ability to adapt a summary to previously processed data offers more power than independently summarizing the pieces.

[Read in atlas](index.html#TCS-0998) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0515 — Deterministic volume gap

The VOLUME model measures how many graph vertices an adaptive local algorithm inspects to determine one requested output. Outputs from separate queries must still fit together into a single valid labeling. The conjecture says every deterministic locally checkable problem with sublinear worst-case volume actually has O(log-star n) volume. It concerns fixed bounded-degree graph families with exact size information and polynomially bounded identifiers. Proving the collapse would eliminate an entire intermediate range of deterministic local information complexity, despite the richer range available to randomized algorithms.

[Read in atlas](index.html#TCS-0515) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [The randomized local computation complexity of the Lovász local lemma](https://arxiv.org/abs/2103.16251v2) · [The Landscape of Distributed Complexities on Trees and Beyond](https://arxiv.org/abs/2202.04724v2) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [New Complexity Classes in Locally Checkable Labeling for Local Computation Algorithms](https://arxiv.org/abs/2607.09626v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0986 — Characterizing Sketchable Distances

Distance sketching compresses vectors so that their dissimilarity can be approximated from small summaries. The source asks which distances admit such sketches and whether sketchability essentially forces a norm-like dependence on the vector difference. It discusses separable distances and divergences, where linear-space obstructions exclude many familiar measures. The allowed stream updates matter because deletions can remove information that insertion-only sketches exploit. A broad characterization would explain which geometric properties make compression possible beyond the established norm setting and its embedding-based descriptions.

[Read in atlas](index.html#TCS-0986) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:5)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0469 — Maximum independent set in the congested clique

Maximum independent set asks for a largest collection of pairwise nonadjacent vertices. Here each vertex is a processor in a congested clique, whose communication links exist even between nonadjacent input vertices. The question asks for the optimal deterministic number of rounds, with unlimited local computation and storage. Collecting the full graph at one processor gives an elementary upper bound, after which even exhaustive local optimization costs no communication rounds. The challenge is to determine how much information must move to identify an exact optimum, independently of the usual centralized NP-hardness barrier.

[Read in atlas](index.html#TCS-0469) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1) · [On the Power of the Congested Clique Model](https://www.cs.tau.ac.il/~roshman/papers/podc14_clique.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0519 — Bipartite maximal matching with polynomial-in-degree volume

A maximal matching is a collection of disjoint edges to which no further edge can be added. The question asks for a deterministic local-query algorithm on bipartite graphs whose inspected volume is polynomial in the maximum degree and independent of graph size. A proper two-coloring identifying the bipartition is supplied. Simulating a distributed proposal algorithm by exploring whole neighborhoods can incur an exponential dependence on degree. The project is to follow a much smaller dependency structure while ensuring that separately answered vertex queries describe the same matching.

[Read in atlas](index.html#TCS-0519) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#volume) · [Seeing Far vs. Seeing Wide: Volume Complexity of Local Graph Problems](https://arxiv.org/abs/1907.08160v2) · [Truly Tight-in-\(\Delta\) Bounds for Bipartite Maximal Matching and Variants](https://arxiv.org/abs/2002.08216v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0940 — Lifting sketching resistance to sublinear streaming resistance

Streaming approximation for a constraint satisfaction problem estimates the best fraction of constraints that one assignment can satisfy. Sketches impose additional structure by requiring independently processed summaries to combine consistently. The conjecture asks whether resistance to nontrivial approximation by \(o(\sqrt{n})\)-space sketches implies resistance to all \(o(n)\)-space streaming algorithms. Thus the proposed implication both broadens the algorithm model and raises the memory threshold. A proof would greatly extend existing sketching classifications, while a simple counterexample would expose a useful algorithmic distinction between sketches and more general streams.

[Read in atlas](index.html#TCS-0940) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2997 — Triangle detection in CONGEST

Triangle detection asks a distributed network to report whether any three vertices are pairwise adjacent. In CONGEST, each edge transmits only \(O(\log  n)\) bits per round, even though vertices initially know all their own neighbors. The saved card asks for the optimal randomized round complexity between the stated doubly logarithmic lower bound and roughly \(n^{1/3}\) upper bound. Detection needs only one positive witness somewhere in the network, unlike listing every triangle. The challenge is to exploit that smaller output requirement while still communicating enough information to discover an edge between two neighbors.

[Read in atlas](index.html#TCS-2997) · [Distributed Subgraph Finding — ADGA 2025](https://adga-workshop.org/2025/keren.pdf) · [Distributed Triangle Detection is Hard in Few Rounds](https://arxiv.org/abs/2504.01802) · [Near-optimal Distributed Triangle Enumeration via Expander Decompositions](https://doi.org/10.1145/3446330)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0984 — “Ultimate” Deterministic Sparse Recovery

Sparse recovery reconstructs an approximation to a vector from a short list of linear measurements. The target is a deterministic measurement matrix with \(O(k \log (n/k))\) rows and recovery time \(O(n \operatorname{polylog} n)\). The reconstructed vector must have l2 error bounded by a constant times the best k-sparse l1 error divided by \(\sqrt{k}\). The source highlights that obtaining the measurement count or the decoding time separately does not provide both guarantees together. The project is to combine near-optimal compression with fast reconstruction while preserving this particular mixed-norm approximation guarantee.

[Read in atlas](index.html#TCS-0984) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6501 — Constant-round MIS in the congested clique

A maximal independent set is independent and places every excluded vertex next to a selected one. In the congested clique, processors can send separate short messages directly to every other processor. The question asks whether a randomized algorithm can solve this task in a constant number of rounds on every input graph with high probability. Collecting all edges at one leader is too expensive, but the algorithm need not reconstruct the entire graph to choose a valid set. The target is to replace repeated sparsification and degree-reduction phases with a bounded amount of globally coordinated communication.

[Read in atlas](index.html#TCS-6501) · [When MIS and Maximal Matching are Easy in the Congested Clique](https://arxiv.org/abs/2502.21031) · [Improved Massively Parallel Computation Algorithms for MIS, Matching, and Vertex Cover](https://arxiv.org/abs/1802.08237) · [Time and Space Optimal Massively Parallel Algorithm for the 2-Ruling Set Problem](https://doi.org/10.4230/LIPIcs.DISC.2023.11)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0994 — Graph Matchings

Maximum weighted matching chooses disjoint edges with the greatest total weight. The source asks for a streaming approximation arbitrarily close to optimal using \(O(n \log  n)\) space and a number of passes depending only on the accuracy. It also raises the corresponding question of a linear-time approximation scheme in the RAM model. Weighted improvement steps may require augmenting cycles, which are harder to locate through a stream than local edge exchanges. This historical formulation focuses on whether those global improvements can be organized without storing the entire graph or making many passes.

[Read in atlas](index.html#TCS-0994) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0524 — LOCAL coloring below square-root degree dependence

A proper coloring with Delta plus one colors always exists for a graph of maximum degree Delta. The question asks for a deterministic LOCAL algorithm running in O(\(Delta^{0.499}\) plus log-star n) rounds. The degree exponent deliberately lies just below one half, while the network-size dependence retains the small symmetry-breaking term. Processors must reduce a large identifier-based palette without causing conflicts among adjacent vertices acting simultaneously. Crossing this degree threshold would improve the coordination of dense local neighborhoods without paying a larger dependence on the total number of vertices.

[Read in atlas](index.html#TCS-0524) · [Open problems related to locality in distributed graph algorithms](https://jukkasuomela.fi/open/#local) · [Local Conflict Coloring Revisited: Linial for Lists](https://arxiv.org/abs/2007.15251) · [Faster Distributed Delta-Coloring via a Reduction to MIS](https://doi.org/10.1137/1.9781611978971.162)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0950 — Linear Sketching Over $F_2$

A linear sketch over F2 records selected parities of a Boolean input. The question compares the minimum randomized sketch length for f with randomized one-way communication for computing \(f(x \mathrm{XOR} y)\). Alice knows x and sends one message to Bob, who knows y and must determine the function value. An exact deterministic correspondence is known in the source, and the conjecture asks for a randomized correspondence up to polylogarithmic factors. A proof would show that arbitrary one-way messages offer little extra power over linear measurements for this broad class of XOR-based communication problems.

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

The project concerns streaming algorithms that approximate Max Cut increasingly close to the optimum. For every constant C, the conjecture predicts an accuracy parameter epsilon for which a (1-epsilon)-approximation requires either \(\Omega (n)\) memory or \(\Omega (n^{C})\) passes. The accuracy may depend on C, which is essential to the statement. This asks whether sublinear memory can support a full approximation scheme using only a fixed polynomial bound on scans. A proof would identify a severe time-space cost of approaching exact cut values beyond the more familiar constant-factor streaming barriers.

[Read in atlas](index.html#TCS-0943) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf)
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

### TCS-2689 — Deterministic safety and termination in hybrid synchrony

Permissionless consensus must accommodate processes joining and leaving without a fixed known membership. The source's hybrid synchronous model provides synchronously connected participation while retaining uncertainty about which messages a process should expect. The question asks whether consensus can have both deterministic safety and deterministic termination under that model's benign-failure assumptions. Sandglass supplies deterministic safety with a weaker termination guarantee, so the remaining issue is eliminating randomness from progress as well. A resolution would clarify whether the uncertainty created by open participation imposes a fundamental limit even when substantial synchrony is present.

[Read in atlas](index.html#TCS-2689) · [Safe Permissionless Consensus](https://doi.org/10.4230/LIPIcs.DISC.2022.33)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-3845 — Efficient distributed multicommodity routing

Multicommodity routing connects many source-destination demands while limiting both path length and the number of routes sharing an edge. The source considers low-width demand instances on random graphs that serve as communication infrastructure for parallel simulation. It asks for a distributed algorithm running in polylogarithmic rounds and producing routing with polylogarithmic congestion and dilation. Good routes exist by centralized arguments, but discovering them quickly with only local communication is the missing step. Such a construction would tighten the connection between efficient parallel computation and distributed computation on networks with rapid mixing.

[Read in atlas](index.html#TCS-3845) · [New Distributed Algorithms in Almost Mixing Time via Transformations from Parallel Algorithms](https://doi.org/10.4230/LIPIcs.DISC.2018.31)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4099 — Pseudodeterministic NC perfect matching in general graphs

A pseudodeterministic randomized algorithm returns the same canonical answer with high probability on repeated runs of a fixed input. For perfect matching, this demands reproducible selection of one matching rather than merely finding any valid matching. The question asks for such an algorithm on general nonbipartite graphs using polynomially many processors and polylogarithmic parallel depth. The source achieves this for bipartite graphs, but extending the selection mechanism must account for the additional structure of general matching. A solution would give stable outputs from efficient parallel randomization and advance the relationship between matching algorithms and derandomization.

[Read in atlas](index.html#TCS-4099) · [Bipartite Perfect Matching in Pseudo-Deterministic NC](https://doi.org/10.4230/LIPIcs.ICALP.2017.87)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-4299 — Collision detection in deterministic broadcast

In an ad-hoc radio network, a receiver normally obtains a message only when exactly one neighbor transmits to it. Collision detection additionally tells the receiver when simultaneous transmissions occurred instead of silence. The source asks whether this extra feedback can improve deterministic broadcast time in unknown network topologies. Randomized algorithms benefit from it, but deterministic scheduling must exploit the feedback without relying on random contention resolution. Establishing a speedup or an equivalence would identify the value of a basic physical-layer capability for reliably disseminating information through a network with initially unknown structure.

[Read in atlas](index.html#TCS-4299) · [Faster Deterministic Communication in Radio Networks](https://doi.org/10.4230/LIPIcs.ICALP.2016.139)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4763 — Work-efficient parallel approximate flow

Parallel flow algorithms seek small total work and short dependency depth while approximating an optimum flow value or cost. The question asks for nearly linear work and polylogarithmic depth for either edge-capacitated minimum-cost flow or vertex-capacitated maximum flow with approximation \(1 + \varepsilon\). The source works on undirected graphs and obtains almost-linear work with subpolynomial depth, leaving a gap between subpolynomial and polylogarithmic guarantees. Existing shortest-path and edge-capacitated maximum-flow results motivate trying to remove that gap. A solution would make richer capacity and cost models as parallelizable as these more established flow primitives.

[Read in atlas](index.html#TCS-4763) · [Parallel \((1+e)\)-Approximate Multi-Commodity Min-Cost Flow in Almost Optimal Depth and Work](https://doi.org/10.1109/FOCS63196.2025.00099)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5127 — Wait-free solvability of graph approximate agreement

Graph approximate agreement asks distributed processes to choose outputs satisfying proximity and validity conditions expressed on a graph. The source asks which graphs admit wait-free solutions using only registers. Wait-freedom requires each participating process to finish despite delays or failures of other processes. Classifying the admissible graphs would reveal how the geometry of permitted outputs interacts with the power of basic shared memory. The saved note preserves uncertainty for many graphs but does not state the exact validity condition or process count, so these cannot be supplied from ordinary real-valued agreement conventions.

[Read in atlas](index.html#TCS-5127) · [The Impossibility of Approximate Agreement on a Larger Class of Graphs](https://doi.org/10.4230/LIPIcs.OPODIS.2022.22)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-6125 — Exponential LOCAL–CONGEST separation for bounded-degree LCLs

Locally checkable labeling problems have solutions whose validity can be inspected within neighborhoods of constant radius. The source asks for a bounded-degree graph problem solvable in \(O(\log  n) \mathrm{LOCAL}\) rounds but requiring \(\Omega (n) \mathrm{CONGEST}\) rounds. The two models differ only in message-size restrictions, so such a separation would isolate the cost of bandwidth. The paper already separates them by a smaller gap on general graphs while showing matching complexities on trees. A stronger example would demonstrate that even a locally verifiable task can require nearly global communication time when short messages replace unrestricted exchanges.

[Read in atlas](index.html#TCS-6125) · [Locally Checkable Labelings with Small Messages](https://doi.org/10.4230/LIPIcs.DISC.2021.8)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6206 — Clique detection in CONGEST

In \(\mathrm{CONGEST}_{b}\), each graph edge carries at most b bits per communication round. The source studies detecting cliques with size at least four and up to order \(\sqrt{n}\), asking how far the round complexity exceeds its roughly \(\sqrt{n}/b\) lower-bound scale. A linear-round algorithm leaves a substantial gap, particularly for fixed clique sizes. The paper proves that its two-party vertex-partition method cannot establish the stronger lower bounds that would close that gap. The project therefore calls for improved detection algorithms or new communication-hardness techniques that capture interactions among more than the two partitioned views.

[Read in atlas](index.html#TCS-6206) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6380 — Load-optimal parallel natural joins

A natural join combines database relations by matching equal values on shared attributes. In massively parallel computation, the load measures how much data any one of p machines must handle. The question asks for algorithms matching the \(\Omega (m/p^{1/\rho})\) load bound for arbitrary join queries, where m is total input size and \(\rho\) is the fractional edge-cover number. The source achieves the target for binary-relation joins in a small constant number of rounds, but those graph-shaped queries do not cover arbitrary relation arities. A general construction would align parallel join execution with the structural lower bound of the query hypergraph.

[Read in atlas](index.html#TCS-6380) · [A Simple Parallel Algorithm for Natural Joins on Binary Relations](https://doi.org/10.4230/LIPIcs.ICDT.2020.25)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6418 — Simultaneously time- and message-optimal distributed MST

Distributed minimum spanning tree construction requires network vertices to agree on a minimum-weight spanning tree using messages along graph edges. The historical question in the 2011 source asks for one algorithm achieving both nearly linear message complexity and nearly optimal time. Its targets are \(\widetilde{O} (|E|)\) messages and \(\widetilde{O}\)\((\sqrt{n} + D)\) time, where D is the network diameter. The paper attains these simultaneous bounds for verifying a proposed tree and contrasts them with the separate construction guarantees available in its discussion. This frames the project as understanding whether communication economy and rapid global coordination can coexist in constructing an optimal network backbone.

[Read in atlas](index.html#TCS-6418) · [Tight Bounds For Distributed MST Verification](https://doi.org/10.4230/LIPIcs.STACS.2011.69) · [https://doi.org/10.4230/LIPIcs.DISC.2022.19](https://doi.org/10.4230/LIPIcs.DISC.2022.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7010 — Linear-sketch complexity of the nuclear norm

The nuclear norm of a matrix is the sum of its singular values and measures a different aspect of size from the Frobenius or spectral norm. A linear sketch compresses the matrix through linear measurements before estimating this norm. The source asks for the optimal sketch dimension needed for a constant-factor approximation. Its discussion places nuclear-norm sketching between neighboring norms with very different behavior: constant dimension for the Frobenius norm and essentially full matrix dimension for the spectral norm. Tight bounds would show whether low-dimensional linear summaries can preserve this important aggregate of singular-value information.

[Read in atlas](index.html#TCS-7010) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-2281 — Local first-order vertex marking in logarithmically many CONGEST rounds

A fixed local first-order formula asks a question about the neighborhood of each graph vertex. The historical problem was to mark all satisfying vertices using only short messages along graph edges. Blin and coauthors give a deterministic O(log n)-round algorithm for every fixed bounded-expansion class. Their theorem answers the exact question restated in the 2024 source and was published at STOC 2026. The global first-order model-checking extension has an additional diameter term and is a separate result.

[Read in atlas](index.html#TCS-2281) · [Distributed Model Checking on Graphs of Bounded Treedepth](https://doi.org/10.4230/LIPIcs.DISC.2024.25) · [What Can Be Computed Locally Revisited — First-Order Logic on Sparse Graphs in Distributed Computing](https://arxiv.org/abs/2411.14825v3) · [What Can Be Computed Locally Revisited: First-Order Logic on Sparse Graphs in Distributed Computing — STOC publication](https://doi.org/10.1145/3798129.3800849)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-3119 — Explicit dense robust graphs with efficient local self-ordering

A robustly self-ordered graph changes many edges whenever many vertex names are permuted. Local self-ordering recovers one vertex’s canonical name using only a few adjacency queries. The source asks for efficiently constructed dense graphs having both properties. Goldreich’s later Corollary 1.7 supplies both properties with polylogarithmic time bounds. The original construction question is resolved, while a universal implication for every robust dense graph is a different problem.

[Read in atlas](index.html#TCS-3119) · [Robustly Self-Ordered Graphs: Constructions and Applications to Property Testing](https://doi.org/10.4230/LIPIcs.CCC.2021.12) · [Robust Self-Ordering versus Local Self-Ordering](https://www.wisdom.weizmann.ac.il/~oded/COL3/rso-vs-lso.pdf) · [Robust Self-Ordering versus Local Self-Ordering — author page](https://www.wisdom.weizmann.ac.il/~oded/p_rso-lso.html) · [Computational Complexity and Local Algorithms](https://link.springer.com/book/10.1007/978-3-031-88946-2)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-3910 — Sublinear-round clique detection in CONGEST

Network processors seek a fixed-size clique while sending only logarithmically many bits per edge per round. The original question asked whether sublinear rounds suffice, especially for K₄. A later theorem lists all fixed p-cliques in Õ(n^{1−2/p}) rounds and therefore resolves detection affirmatively. For K₄ this matches the known lower bound up to logarithmic factors. A 2022 theorem also gives deterministic sublinear algorithms; growing clique size and global announcements are different requirements.

[Read in atlas](index.html#TCS-3910) · [Detecting Cliques in CONGEST Networks](https://doi.org/10.4230/LIPIcs.DISC.2018.16) · [Tight Distributed Listing of Cliques](https://doi.org/10.1137/1.9781611976465.171) · [Deterministic Near-Optimal Distributed Listing of Cliques](https://doi.org/10.1145/3519270.3538434)
Existing status: `resolved` · Summary written: 2026-09-12

## Optimization and numerical computation (22)

### TCS-0008 — Strongly polynomial linear programming

Linear programming optimizes a linear objective subject to linear equality and nonnegativity constraints. The question asks whether every rational instance can be solved using a number of arithmetic operations polynomial only in its numbers of variables and constraints. Intermediate numbers must also have encoding lengths bounded polynomially in the full input length. Existing polynomial-time guarantees may depend on how many bits describe the coefficients, which is the dependence this target seeks to remove. A solution must handle exact optima, infeasibility, and unbounded objectives within the same strongly polynomial framework.

[Read in atlas](index.html#TCS-0008) · [Problem 8: Linear Programming: Strongly Polynomial?](https://topp.openproblem.net/p8) · [A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs](https://doi.org/10.1287/opre.34.2.250) · [A strongly polynomial algorithm for linear programs with at most two non-zero entries per row or column](https://homepages.cwi.nl/~dadush/papers/genflow.pdf) · [No self-concordant barrier interior point method is strongly polynomial](https://arxiv.org/abs/2201.02186) · [Trust Region Interior Point Methods: Optimal l2- and Faster Wide-Neighborhood Path Following](https://homepages.cwi.nl/~dadush/papers/trust-region.pdf) · [A strongly polynomial-time algorithm for the general linear programming problem](https://arxiv.org/abs/2503.12041v10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6574 — Exact semidefinite feasibility in polynomial time

A semidefinite feasibility instance asks whether some real assignment makes an affine combination of rational symmetric matrices positive semidefinite. The target is an exact yes-or-no decision in polynomial time in the ordinary bit model. Numerical approximation does not settle this question because an infeasible affine space can approach the positive semidefinite cone arbitrarily closely. Feasible rational inputs can also require irrational or very large witnesses. The challenge is to decide arbitrary degenerate instances efficiently without adding regularity assumptions that make approximation algorithms easier to analyze.

[Read in atlas](index.html#TCS-6574) · [An exact duality theory for semidefinite programming and its complexity implications](https://link.springer.com/article/10.1007/BF02614433) · [On the Turing Model Complexity of Interior Point Methods for Semidefinite Programming](https://epubs.siam.org/doi/10.1137/15M103114X) · [Exact algorithms for semidefinite programs with degenerate feasible set](https://www.sciencedirect.com/science/article/pii/S0747717120301176) · [How Do Exponential Size Solutions Arise in Semidefinite Programming?](https://epubs.siam.org/doi/10.1137/21M1434945) · [A combinatorial approach to Ramana’s exact dual for semidefinite programming](https://arxiv.org/abs/2510.07271) · [Hesse’s Redemption: Efficient Convex Polynomial Programming](https://arxiv.org/abs/2511.03440)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-0491 — Log-squared query complexity for fixed-dimensional Tarski

A monotone function on a finite multidimensional grid is guaranteed to have a fixed point. The project asks whether one can find any such point using only a squared-logarithmic number of value queries in the grid side length. The dimension is fixed, and the multiplicative constant may depend arbitrarily on it. Incomparable grid points complicate the interval-discarding ideas that make one-dimensional search efficient. A positive answer would show that higher fixed dimensions need not increase the logarithmic query exponent, independently of the computation performed between queries.

[Read in atlas](index.html#TCS-0491) · [Finite and Algorithmic Model Theory (Dagstuhl Seminar 22051)](https://doi.org/10.4230/DagRep.12.1.101) · [A Faster Algorithm for Finding Tarski Fixed Points](https://doi.org/10.1145/3524044) · [Tarski Lower Bounds from Multi-Dimensional Herringbones](https://arxiv.org/abs/2502.16679v2) · [The Mystery Deepens: On the Query Complexity of Tarski Fixed Points](https://arxiv.org/abs/2604.00268v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0724 — Limited-memory convex optimization

First-order convex optimization learns about an objective through queries returning its value and a subgradient. The source asks how the number of queries needed for a prescribed accuracy changes when the algorithm has limited working memory. It highlights methods with strong oracle complexity whose stored geometric information can require quadratic space in dimension. The question is whether that memory cost is inherent or can be traded away without losing the optimal query rate. A sharp tradeoff would distinguish information acquired from the oracle from information that must remain available between optimization steps.

[Read in atlas](index.html#TCS-0724) · [COLT / PMLR](https://proceedings.mlr.press/v99/woodworth19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0728 — Smooth convex optimization in nonstandard oracle models

Smooth convex optimization is often analyzed when the objective's regularity and the feasible region use compatible norms. The source instead studies settings where these geometries differ, including vector norms and their matrix counterparts. It asks for the optimal oracle complexity of minimizing such functions using black-box first-order information. The stated gaps concern how smoothness, domain geometry, dimension, and target accuracy interact. Matching algorithms and lower bounds would show whether sparse and low-rank optimization models permit faster convergence than methods designed around a single common norm suggest.

[Read in atlas](index.html#TCS-0728) · [COLT / PMLR](https://proceedings.mlr.press/v40/Guzman15.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0722 — Polynomial-time linear convergence for geodesically convex optimization

Geodesically convex optimization replaces straight segments with shortest paths on a Riemannian manifold. The question asks for a deterministic first-order algorithm with query complexity polynomial in dimension and logarithmic in inverse accuracy. It also requires polynomial arithmetic work per query, so a powerful but computationally intractable geometric oracle would not suffice. The source develops an ellipsoid-like approach for constant-curvature spaces and identifies obstacles on more general manifolds. A solution would extend the efficient precision dependence of Euclidean convex optimization to curved spaces while respecting the cost of manipulating their geometry.

[Read in atlas](index.html#TCS-0722) · [COLT / PMLR](https://proceedings.mlr.press/v195/criscitiello23b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0344 — Additivity of extension complexity under Cartesian products

Extension complexity measures how many facets are needed in a higher-dimensional polytope projecting onto a given polytope. For a Cartesian product, describing the two factors separately gives a natural additive construction. The source asks whether a more economical extension can ever beat that sum. It notes that certain factor types, including pyramids, rule out the proposed saving. The question tests whether two independent feasible regions can share hidden inequalities in a lifted formulation, rather than merely combining their existing descriptions.

[Read in atlas](index.html#TCS-0344) · [Computational Geometry](https://doi.org/10.4230/DagRep.9.4.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0687 — Gap-entropy conjecture

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

### TCS-0673 — First-order convergence to local minimax optima

Minimax optimization models a player minimizing an objective against a second player who maximizes it. In nonconvex–nonconcave problems, stationary points need not represent the intended local minimax behavior. The selected question asks for a first-order method whose stable convergence targets are restricted to local minimax optima. Reversing the players' optimization order or merely driving both gradients toward zero can select inappropriate solutions. A method with the desired guarantee would clarify the dynamics needed for adversarial optimization, including the mathematical problems underlying some generative-model training procedures.

[Read in atlas](index.html#TCS-0673) · [COLT / PMLR](https://proceedings.mlr.press/v195/chae23a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3676 — Binary-horizon MDP reward-threshold complexity

The input is a finite MDP, an initial state, a binary-encoded horizon and an exact rational reward threshold. The question asks whether any policy attains at least that expected discounted reward and seeks the exact decision complexity. Policies may depend on time and state, and all first actions remain available. The source’s EXPTIME-completeness theorem instead concerns whether a specified first action is optimal. Exact value iteration gives an exponential-time upper bound, but the unrestricted threshold variant is separately left open.

[Read in atlas](index.html#TCS-3676) · [On the Complexity of Value Iteration (Track B: Automata, Logic, Semantics, and Theory of Programming)](https://doi.org/10.4230/LIPIcs.ICALP.2019.102) · [On the Complexity of Value Iteration](https://arxiv.org/abs/1807.04920)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4293 — PLS-completeness of k-means local minima

The k-means method repeatedly assigns points to centers and updates centers to improve a clustering objective. The source conjectures PLS-completeness of finding an arbitrary local minimum of this method. A locally stable clustering need not minimize the global objective, but searching for even such stability can be difficult. A classification would explain whether slow convergence reflects inherent local-search complexity rather than an unfortunate execution path. The saved statement does not specify point encoding, degeneracies, or the exact neighborhood, which must be fixed to define the relevant local-optimum search problem.

[Read in atlas](index.html#TCS-4293) · [The Complexity of the k-means Method](https://doi.org/10.4230/LIPIcs.ESA.2016.78)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5330 — Near-linear-query approximation schemes for matroid intersection

Matroid intersection seeks the largest set that is independent in each of two matroids accessed through independence tests. The source provides a deterministic nearly linear-query approximation approaching two thirds of optimum. It asks whether the same query scale can instead achieve a factor arbitrarily close to one for the general range of optimum ranks. Randomized algorithms reach this stronger approximation in the cited comparison. The challenge is to organize deterministic exchanges and information gathering without paying a superlinear query cost that random sampling can avoid.

[Read in atlas](index.html#TCS-5330) · [Deterministic \((2/3 - \varepsilon )\)-Approximation of Matroid Intersection Using Nearly-Linear Independence-Oracle Queries](https://doi.org/10.4230/LIPIcs.WADS.2025.50)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5494 — Oracle complexity of stochastic approximate stationarity

Stochastic optimization receives noisy information about an objective and often aims to find a point with small gradient. The extracted passage asks for a sharp account of the oracle complexity of reaching such approximate stationarity. Its surrounding discussion includes nonconvex functions, where global minimization is generally too demanding a target. The same paper develops nearly matching results for the convex setting, so those resolved cases must be separated from the broader motivation. The remaining research direction is to identify optimal stochastic information requirements under explicitly stated smoothness, noise, and function-class assumptions.

[Read in atlas](index.html#TCS-5494) · [The Complexity of Making the Gradient Small in Stochastic Convex Optimization](https://proceedings.mlr.press/v99/foster19b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6483 — Superlinear randomized query lower bounds for submodular minimization

Submodular function minimization seeks a minimum-value subset using queries to a value oracle. The source proves a superlinear query lower bound for deterministic algorithms. It asks whether any superlinear lower bound can also be established for randomized algorithms with a suitable success guarantee. The construction's deterministic difficulty can disappear when random queries quickly discover the relevant hidden structure. New lower-bound ideas would therefore be needed to show that randomization cannot always reduce the information needed for general submodular minimization back to essentially linear scale.

[Read in atlas](index.html#TCS-6483) · [Improved Lower Bounds for Submodular Function Minimization](https://doi.org/10.1109/FOCS54457.2022.00030)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7007 — Input-sparsity relative spectral low-rank approximation

Spectral low-rank approximation seeks a rank-k representation whose largest directional error is near the best possible. The source asks for a relative-error guarantee in time equal to reading the nonzero matrix entries plus a term linear in n and polynomial in k over epsilon. That speed is available in the cited comparison for Frobenius error, which aggregates squared errors instead of controlling the worst direction. The spectral target is therefore substantially stronger. A solution would make sparse-matrix compression fast while protecting against a large error concentrated in one singular direction.

[Read in atlas](index.html#TCS-7007) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7008 — Polynomial-time relative entrywise \(\ell\)\(_{1}\) low-rank approximation

Robust low-rank approximation measures reconstruction error by the sum of absolute entrywise differences. The source asks for a polynomial-time algorithm returning a rank-k factorization within a factor one plus epsilon of the best such approximation. This changes the geometry from the squared-error setting where singular values and standard sketching methods are especially effective. Approximating a sum of row norms is also a different guarantee and does not settle the entrywise objective. An algorithm or hardness classification would clarify whether near-optimal robust matrix compression admits the same broad computational tractability as classical low-rank approximation.

[Read in atlas](index.html#TCS-7008) · [Sketching as a Tool for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-3142 — Can full-batch first-order methods match SGD’s O(ε⁻²) generalization rate?

The task is to minimize population risk for arbitrary convex Lipschitz losses on a unit ball. A full-batch method sees only the value and averaged subgradient of one fixed empirical sample. The source asks whether such a method can generalize in O(ε⁻²) calls using dimension-independent samples. The later NeurIPS theorem requires Ω(ε⁻⁴) calls for general full-batch methods in this setting. The negative resolution does not apply to individual-example access, fixed low-dimensional regimes or extra regularity assumptions.

[Read in atlas](index.html#TCS-3142) · [SGD Generalizes Better Than GD (And Regularization Doesn’t Help)](https://proceedings.mlr.press/v134/amir21a.html) · [Never Go Full Batch (in Stochastic Convex Optimization)](https://proceedings.neurips.cc/paper/2021/hash/d27b95cac4c27feb850aaa4070cc4675-Abstract.html) · [Never Go Full Batch — complete author version](https://arxiv.org/abs/2107.00469)
Existing status: `resolved` · Summary written: 2026-09-12

## Geometry, topology and metric spaces (47)

### TCS-6523 — Kannan–Lovász–Simonovits conjecture

The KLS conjecture concerns log-concave probability distributions normalized to have mean zero and identity covariance. It asks whether every sufficiently regular function has variance bounded by a universal constant times its average squared gradient. That constant must work in every dimension and for every such distribution. Geometrically, this would exclude narrow bottlenecks that covariance normalization fails to reveal. The question connects high-dimensional convex geometry with the mixing of sampling algorithms, and control of particular observables alone does not settle it.

[Read in atlas](index.html#TCS-6523) · [The KLS Conjecture (problem 30)](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/) · [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf) · [Bourgain’s slicing problem and KLS isoperimetry up to polylog](https://arxiv.org/abs/2203.15551) · [Logarithmic bounds for isoperimetry and slices of convex sets](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/root_log.pdf) · [Thin-shell bounds via parallel coupling](https://arxiv.org/abs/2507.15495v2) · [The KLS constant is \(O(\log ^{1/4} n)\)](https://arxiv.org/abs/2607.24164v1)
Existing status: `source_open` · Summary written: 2026-09-11

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

[Read in atlas](index.html#TCS-6524) · [Research reference · web.math.princeton.edu](https://web.math.princeton.edu/~naor/homepage%20files/assouad-N%28K%29.pdf) · [Research reference · www.its.caltech.edu](https://www.its.caltech.edu/~sryoo/teaching/Syllabus_Ma191a_2024F.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7242 — Decidability of PL four-sphere recognition

The input is a finite triangulation promised to be a closed combinatorial four-dimensional manifold. The task is to recognize the standard piecewise-linear four-sphere. The question asks for a terminating decision algorithm, with no polynomial-time requirement. Recognizing a topological sphere or checking its homology would answer a different question. The problem marks the exceptional dimension between established decidability and undecidability results for sphere recognition.

[Read in atlas](index.html#TCS-7242) · [Frontiers of sphere recognition in practice](https://link.springer.com/article/10.1007/s41468-022-00092-8) · [Applied topology: sphere recognition research presentation](https://page.math.tu-berlin.de/~joswig/presentations/Joswig-Applied%2BTopology-250715.pdf) · [Is there an algorithm to recognize the combinatorial four-sphere?](https://www.openproblemgarden.org/op/is_there_an_algorithm_to_determine_if_a_triangulated_4_manifold_is_combinatorially_equivalent_to_the_4_sphere)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6526 — Optimal size of weak \(\varepsilon\)-nets for convex ranges

A weak \(\varepsilon\)-net places auxiliary points so that every convex set containing at least an \(\varepsilon\) fraction of a given point set contains an auxiliary point. The auxiliary points may lie anywhere in the ambient Euclidean space. For each fixed dimension, the task is to determine the smallest worst-case net size as \(\varepsilon\) decreases. The challenge comes from hitting all sufficiently populated convex regions simultaneously, regardless of the original configuration. Sharp bounds would quantify how economically a finite set can represent its large convex subsets.

[Read in atlas](index.html#TCS-6526) · [Research reference · arXiv 1808.02686](https://arxiv.org/abs/1808.02686)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0406 — Dürer’s conjecture

Take a convex polyhedron and cut selected edges while leaving its faces attached as one piece. The question is whether the resulting surface can always be flattened into a single polygon without overlapping interiors. Cuts through the middle of a face are disallowed, making the available choices depend on the polyhedron's edge structure. Convexity is central because the unrestricted nonconvex version has counterexamples. A solution would explain whether every convex solid has a conventional paper net using only its original faces.

[Read in atlas](index.html#TCS-0406) · [The Open Problems Project](https://topp.openproblem.net/p9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6527 — Constant-distortion Steiner point removal

Steiner point removal starts with a weighted graph and a designated set of terminals whose mutual distances matter. The goal is to delete the other vertices through graph-minor operations, leaving a graph on exactly those terminals. Its edges may be reweighted, but terminal distances should never shrink and should grow by at most a universal factor. The same guarantee must work regardless of how many terminals the input contains. This asks whether graph topology and useful terminal geometry can both survive an extreme reduction in representation size.

[Read in atlas](index.html#TCS-6527) · [Research reference · epubs.siam.org](https://epubs.siam.org/doi/10.1137/1.9781611977912.191)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6529 — Optimal \(\ell\)\(_{1}\) distortion of planar Earth Mover Distance

Earth Mover Distance measures the cheapest transportation of one probability distribution into another across a planar grid. The problem asks how well this entire metric can be embedded into \(\ell\)\(_{1}\) while preserving every pairwise distance. Its parameter is the side length of the grid, and the target is the optimal dependence of distortion on that size. A single coordinate representation must accommodate many different transportation patterns. Understanding this loss would clarify the limits of treating geometric transport as ordinary coordinatewise comparison or sketching.

[Read in atlas](index.html#TCS-6529) · [Research reference · www.weizmann.ac.il](https://www.weizmann.ac.il/math/gideon/sites/math.gideon/files/uploads/planar-earthmover.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7184 — Klee’s measure problem

Klee’s measure problem asks for the volume covered by a union of axis-aligned boxes. Overlapping regions count once, and only the exact total volume is required. For each fixed dimension at least three, the question seeks matching worst-case time bounds in a specified arithmetic real-RAM model. Chan’s general upper bound is \(O(n^{d/2})\), with no matching unconditional classification supplied by the checked later work. Recent approximation and dynamic advances answer different questions.

[Read in atlas](index.html#TCS-7184) · [Klee's measure problem made easy](https://doi.org/10.1109/FOCS.2013.51) · [Approximating Klee’s Measure Problem and a Lower Bound for Union Volume Estimation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.25) · [Near-Optimal Dynamic Data Structures for Maximum Depth and Klee’s Measure of Boxes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.34)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7182 — Simultaneous embedding with fixed edges for two graphs

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

### TCS-7189 — Minimum-weight triangulation in NP

The input gives rational planar points and a rational limit on the total length of a triangulation. Every input point must be used, no extra points may be added, and Euclidean edge lengths are compared exactly. The question asks whether every feasible instance has a short certificate that can be checked in polynomial bit time. NP-hardness is known, but the sum of potentially irrational edge lengths prevents the usual edge-list argument from establishing NP membership. Practical exact solutions and rounded-cost variants do not settle the certificate question for arbitrary exact inputs.

[Read in atlas](index.html#TCS-7189) · [Minimum-weight triangulation is NP-hard](https://arxiv.org/abs/cs/0601002) · [Solving Large-Scale Minimum-Weight Triangulation Instances to Provable Optimality](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.44) · [Taming Infinity One Chunk at a Time: Concisely Represented Strategies in One-Counter MDPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.138)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0410 — Output-sensitive Convex Hull in \(\mathbb{R}^{d}\)

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

### TCS-0432 — Polynomial flip-distance bounds for three-manifold triangulations

Triangulations of the same compact three-manifold are connected by local bistellar flips. The question asks whether two triangulations can always be connected using polynomially many such moves in their input sizes. The polynomial is initially allowed to depend on the fixed manifold. A path may temporarily use different numbers of tetrahedra, so connectivity alone provides no useful quantitative bound. The result would control the amount of local rewriting needed to pass between alternative finite descriptions of one topological space.

[Read in atlas](index.html#TCS-0432) · [Triangulations in Geometry and Topology](https://doi.org/10.4230/DagRep.14.2.120)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2529 — Polynomial-time ultrametric embedding

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

### TCS-0328 — Sparse \((1 + \epsilon )\)-emulator for Euclidean Point Sets

A near-isometric emulator is a weighted graph whose shortest paths approximate distances among Euclidean input points. Unlike a geometric Steiner spanner, its extra vertices need not themselves have Euclidean locations. The source asks how many edges are necessary when this greater freedom is allowed. Even points placed along two opposite sides of a square provide a concrete test instance. The question probes whether abstract auxiliary states can represent Euclidean distances more sparsely than any network constrained to live in the original geometric space.

[Read in atlas](index.html#TCS-0328) · [Metric Sketching and Dynamic Algorithms for Geometric and Topological Graphs](https://doi.org/10.4230/DagRep.15.5.134)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0340 — Average Distortion Embeddings

An average-distortion embedding controls aggregate squared distances while remaining nonexpansive for every pair. The source considers the square-root metric associated with a finite-dimensional normed space. An existence theorem supplies a Hilbert-space embedding with favorable dependence on dimension, but its duality proof does not provide an explicit map. The task is to construct and evaluate an embedding efficiently from the supplied point set. This would turn a structural geometric theorem into an algorithmic primitive for proximity search and related computations.

[Read in atlas](index.html#TCS-0340) · [Computational Geometry](https://doi.org/10.4230/DagRep.11.4.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0970 — Fast JL Transform for Sparse Vectors

A Johnson-Lindenstrauss transform maps a vector into fewer dimensions while approximately preserving its Euclidean length with high probability. The target dimension is O(\(\log (1/\mathrm{P})\) divided by epsilon squared) for failure probability P and error epsilon. The source asks for applying the transform to an s-sparse input in time roughly s plus the output dimension, up to polylogarithmic factors. It also asks for an explicit distribution generated from only \(O(\log (d/\mathrm{P}))\) random bits. The project combines fast multiplication, optimal dimensional reduction, and a compact random seed rather than optimizing any one resource alone.

[Read in atlas](index.html#TCS-0970) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0363 — Negative cycles on surface embedded graphs

Consider a directed graph drawn on a surface whose edges may have negative weights. The task is to decide whether there is a negative-total-weight closed walk that can be contracted to a point on that surface. Walks may revisit edges and vertices, so a witness need not resemble an ordinary simple cycle. The source asks both for algorithms and for a complexity classification, including whether short certificates always suffice. The challenge is to combine weight optimization with a global topological constraint on the whole walk.

[Read in atlas](index.html#TCS-0363) · [Computational Geometry](https://doi.org/10.4230/DagRep.7.4.107)
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

### TCS-3059 — Freedman’s conjecture

Place points in a unit square, including its lower-left corner. Each point may anchor the lower-left corner of an axis-aligned rectangle contained in the square, and the rectangles must not overlap. The conjecture asks whether rectangles can always cover at least half the square. The cited paper shows a limitation of a particular greedy packing approach and calls for different algorithms. The remaining challenge is to coordinate anchored rectangle choices globally so that wasted area never exceeds the proposed universal threshold.

[Read in atlas](index.html#TCS-3059) · [On Greedily Packing Anchored Rectangles](https://doi.org/10.4230/LIPIcs.ICALP.2021.61)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4454 — Half-snowflake embeddings into Wasserstein p-space

The question asks whether every finite metric becomes a bounded-distortion subset of Wasserstein p-space over R³ after taking square roots of its distances. The exponent p is fixed above two, and the distortion bound must depend only on p. The known theorem works at snowflake exponent 1/p, which is smaller than one half in this range. Almost-isometric embeddings and embedding the entire Wasserstein-2 space are separate stronger questions. The later planar results checked here do not settle this three-dimensional half-snowflake conjecture.

[Read in atlas](index.html#TCS-4454) · [Impossibility of Sketching of the 3D Transportation Metric with Quadratic Cost](https://doi.org/10.4230/LIPIcs.ICALP.2016.83) · [Snowflake universality of Wasserstein spaces](https://doi.org/10.24033/asens.2363) · [Coarse Embeddability of Wasserstein Space and the Space of Persistence Diagrams](https://doi.org/10.1007/s00454-024-00674-6)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4549 — Polynomial-time colorful choice with polynomially many colors

The input consists of colored point sets in dimension d, with the origin in the convex hull of every color class. A perfect colorful choice selects at most one point of each color while still containing the origin in its convex hull. The source asks whether polynomially many color classes in d suffice to find such a choice in polynomial time. This trades additional colors for computational tractability while preserving the exact one-point-per-color requirement. It would clarify whether redundant geometric choices can remove the computational difficulty behind the colorful Carathéodory theorem.

[Read in atlas](index.html#TCS-4549) · [Computational Aspects of the Colorful Carathéodory Theorem](https://doi.org/10.4230/LIPIcs.SOCG.2015.44)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-1679 — Does every point set admit an oriented t-spanner with t < 2?

An oriented spanner assigns at most one direction to each connection between two points. Its dilation compares the shortest directed round trip through each pair with the perimeter of that pair’s cheapest triangle. The historical question asks for one factor strictly below two that works for every point set. The published ESA 2026 theorem answers positively with factor five thirds, even in general finite metric spaces. Finding an orientation with the smallest possible dilation for a particular point set remains a separate question.

[Read in atlas](index.html#TCS-1679) · [Computing Oriented Spanners and Their Dilation](https://doi.org/10.4230/LIPIcs.SoCG.2025.27) · [Sparse Oriented Spanners in Metric Spaces](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.117)
Existing status: `resolved` · Summary written: 2026-09-11

## Learning theory (47)

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

### TCS-6544 — Distribution-free learning of intersections of two halfspaces

The intersection of two halfspaces labels a point positively only when it satisfies both linear inequalities. This project asks for efficient distribution-independent learning when examples have a positive margin from the separating boundaries. The learner may output a different kind of hypothesis, but its time must remain polynomial in dimension, inverse margin, and inverse error. The cited source achieves a polynomial-time result under a factorization assumption on the input distribution and leaves removal of that assumption as the broader challenge. Resolving it would determine whether two simple linear rules can be learned efficiently without requiring favorable structure in how examples are distributed.

[Read in atlas](index.html#TCS-6544) · [Learning Intersections of Two Margin Halfspaces under Factorizable Distributions](https://proceedings.mlr.press/v291/diakonikolas25a.html)
Existing status: `source_open` · Summary written: 2026-09-11

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

[Read in atlas](index.html#TCS-0677) · [Open Problem: Properly learning decision trees in polynomial time?](https://proceedings.mlr.press/v178/open-problem-blanc22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3787 — Proper unlabeled compression of ample classes

An ample class strongly shatters every set of coordinates that it shatters. A compressor selects at most d input points from any realizable labeled sample, where d is the class’s VC dimension. A reconstructor must recover a concept in the original class consistent with all sample labels while receiving only the selected points. Maximum classes satisfy this exact bound, and labeled compression is known more generally. The 2024 oriented-matroid results still leave proper unlabeled size-d compression for all ample classes open.

[Read in atlas](index.html#TCS-3787) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.4230/LIPIcs.ICALP.2019.34) · [Unlabeled Sample Compression Schemes and Corner Peelings for Ample and Maximum Classes](https://doi.org/10.1016/j.jcss.2022.01.003) · [Unlabeled Sample Compression Schemes for Oriented Matroids](https://doi.org/10.1016/j.disc.2024.114006)
Existing status: `open` · Summary written: 2026-09-12

### TCS-3689 — Non-clashing teaching dimension versus VC dimension

A teacher assigns correctly labeled examples to each concept in a finite class. No two different concepts may both fit each other’s assigned examples. The conjecture asks whether at most d examples per concept always suffice when the VC dimension is d. A quadratic general bound and exact bounds for certain special classes are known. The sharp signed-example inequality remains distinct from positive-only teaching, computational map-finding and sample-compression questions.

[Read in atlas](index.html#TCS-3689) · [Optimal Collusion-Free Teaching](https://proceedings.mlr.press/v98/kirkpatrick19a.html) · [On Batch Teaching Without Collusion](https://www.jmlr.org/papers/v24/22-0330.html) · [Non-Clashing Teaching Maps for Balls in Graphs](https://proceedings.mlr.press/v247/chalopin24a.html)
Existing status: `open` · Summary written: 2026-09-12

### TCS-0691 — Recursive Teaching Dimension Versus VC Dimension

Teaching dimension measures how many carefully selected labeled examples are needed to identify a target concept. Recursive teaching allows the class to be peeled apart through successive teaching stages, producing a more flexible complexity measure. The selected question asks whether this recursive teaching dimension is bounded by a universal linear function of VC dimension for finite concept classes. VC dimension instead governs learning from random examples, so the comparison connects two different ways information reaches a learner. A bound or a counterexample would clarify the relation between teaching and passive learning and has consequences for sample-compression questions.

[Read in atlas](index.html#TCS-0691) · [COLT / PMLR](https://proceedings.mlr.press/v40/Simon15b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0694 — Statistical-query complexity of sparse halfspaces

An r-sparse halfspace uses at most r of the n Boolean input coordinates. Statistical-query learning accesses approximate expectations instead of individual labeled examples. The source asks whether the worst-case number of nearly uncorrelated sparse halfspaces stays polynomial in n when correlation is inverse-polynomial in r log n. Both the sparsity dependence and the worst-case distribution are essential to the question. A resolution would clarify the informational limits of exploiting sparse structure through statistical queries.

[Read in atlas](index.html#TCS-0694) · [Open Problem: The Statistical Query Complexity of Learning Sparse Halfspaces](https://proceedings.mlr.press/v35/feldman14c.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0683 — Improper learning of mixtures of Gaussians

Mixtures of Gaussians are standard models for data containing several latent clusters. The selected question asks for efficient improper learning in an overcomplete setting, where the number of mixture components exceeds the ambient dimension. The source uses a compression-and-reconstruction notion of unsupervised learning rather than requiring recovery of the original Gaussian parameters. This flexibility matters because hardness of identifying the exact mixture does not automatically rule out a useful alternative representation. A construction would extend the paper's undercomplete approach and show whether low-reconstruction-error learning remains feasible despite the abundance of latent components.

[Read in atlas](index.html#TCS-0683) · [COLT / PMLR](https://proceedings.mlr.press/v75/hazan18a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0670 — Local regularization for multiclass learning

A local regularizer fixes a score for every hypothesis and test point before seeing the training sample. At prediction time it selects among the lowest-scored hypotheses consistent with the sample. The question asks whether every realizably PAC-learnable multiclass class admits such a rule that succeeds under every tie-breaking choice. Two preprints from July and August 2026 claim counterexamples under this definition. Their statements match the main question, while independent verification of the claimed negative resolution remains outstanding.

[Read in atlas](index.html#TCS-0670) · [Open Problem: Can Local Regularization Learn All Multiclass Problems?](https://proceedings.mlr.press/v247/asilis24b.html) · [Local Regularization Does Not Characterize Multiclass PAC Learnability](https://arxiv.org/abs/2607.23449) · [Algorithmic Principles For Multiclass Learning Are Hard To Come By: Limits of Regularization and Proper Learning](https://arxiv.org/abs/2608.26516)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0671 — Direct Sums in Learning Theory

Direct-sum questions study how learning resources change when several tasks are combined into a product class. This source asks how learning curves, uniform-convergence rates, and related complexity parameters scale relative to their single-task versions. For some realizable settings, learning components separately gives a simple additive error bound, but it is unclear when joint learning can improve it. Excess-risk and uniform-convergence quantities need separate analysis because their differences do not inherit the same elementary bound. Sharp product rules would explain when solving several learning problems together provides a statistical advantage over treating them independently.

[Read in atlas](index.html#TCS-0671) · [COLT / PMLR](https://proceedings.mlr.press/v247/hanneke24c.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0664 — Distribution dependence of deep-learning advantages

Neural networks can outperform linear predictors in some learning settings, but that advantage may depend on favorable input distributions. The selected problem asks whether distribution-independent statistical-query learning forces a class to have a low-dimensional linear representation. A related formulation asks whether learnability by gradient methods on suitable neural networks under every input distribution also implies learnability by a linear model. Sample-efficient learning alone does not guarantee such a representation, so computational restrictions and distributional quantifiers are central. Resolving the question would clarify whether broadly distribution-independent deep-learning advantages can survive outside the expressive reach of linear or kernel methods.

[Read in atlas](index.html#TCS-0664) · [COLT / PMLR](https://proceedings.mlr.press/v336/feldman26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0682 — Monotonicity of Learning

It is natural to expect that giving a learner one more training example should improve its predictions. This project asks when expected performance actually changes monotonically with sample size. The source focuses on empirical risk minimization and gives examples where monotonicity holds as well as examples where it fails. Asymptotic consistency or a decreasing upper bound on risk does not guarantee improvement at every finite sample size. Characterizing the learners and problems that do have this property would explain when the everyday intuition that more data helps is mathematically justified.

[Read in atlas](index.html#TCS-0682) · [COLT / PMLR](https://proceedings.mlr.press/v99/viering19a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0684 — Planning-horizon dependence of sample complexity

Long-horizon reinforcement learning appears difficult because useful actions may be separated from their eventual rewards by many steps. The selected problem asks for a sample-complexity lower bound with genuine polynomial dependence on the planning horizon. Total reward is normalized across an episode, preventing a larger reward scale from creating a merely artificial horizon factor. The source argues that some upper-bound assumptions hide difficult sparse-reward cases or restrict the accuracy regime too strongly. A suitable hard family would show when long-term planning itself requires more experience, beyond the difficulty already present in one-step bandit problems.

[Read in atlas](index.html#TCS-0684) · [COLT / PMLR](https://proceedings.mlr.press/v75/jiang18a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0689 — Property Elicitation and Elicitation Complexity

A statistical property is elicitable when minimizing an expected loss recovers that property of the underlying distribution. Familiar examples motivate asking which statistics admit such loss functions and how those functions can be characterized. The source also studies elicitation complexity, the number of intermediate real-valued reports needed to recover a desired statistic. Some properties that cannot be elicited directly may become accessible through a richer intermediate prediction. A general characterization would explain the expressive limits of empirical risk minimization and guide the design of objectives for estimating specific distributional quantities.

[Read in atlas](index.html#TCS-0689) · [COLT / PMLR](https://proceedings.mlr.press/v49/frongillo16.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1478 — Adversarial sequential prediction with abstentions for VC classes

Sequential prediction with abstentions permits a learner to decline to label suspicious instances in a partly adversarial data stream. Clean instances come independently from an unknown distribution, while corrupted instances may be inserted by an adaptive adversary. The source asks for sublinear misclassification and erroneous-abstention counts for every finite-VC class, with polynomial dependence on VC dimension. Existing adaptive-adversary guarantees require an additional finite reduction-dimension condition. Removing it would show that abstention can preserve the broad learnability of stochastic classification even when corruptions respond to the learner and the clean distribution is unknown.

[Read in atlas](index.html#TCS-1478) · [Distribution-Free Sequential Prediction with Abstentions](https://proceedings.mlr.press/v336/yu26a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1539 — VC-dimension bounds for adversarially robust compression

Sample compression stores a small part of a labeled sample and reconstructs a hypothesis consistent with the full sample. Adversarially robust compression must preserve correctness across every allowed perturbation of each example. The source asks whether a finite-VC class with a compression bound \(f(d)\) necessarily has a robust scheme of comparable size. Its positive construction uses stable compression, so the issue is removing that extra structural requirement. A nearby negative result for robust learnability alone does not automatically settle this stronger premise, making the distinction between learnability and compression assumptions essential.

[Read in atlas](index.html#TCS-1539) · [Sample Compression Scheme Reductions](https://proceedings.mlr.press/v272/attias25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1573 — NP-hardness of improper learning of P/poly

Improper learning allows a learner to output a hypothesis outside the representation class used by the target function. This project asks for NP-hardness of learning functions represented by polynomial-size circuits even with that freedom. Hardness arguments for proper learning can fail because they constrain the output representation, a restriction absent here. The source develops connections between strong formulations of learning hardness and cryptographic primitives such as witness encryption. A reduction with the required guarantees would sharpen the boundary between computational learning and worst-case complexity while clarifying those cryptographic consequences.

[Read in atlas](index.html#TCS-1573) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2111 — Fully polynomial learning of positive ReLU networks under Gaussian inputs

The target is a nonnegative weighted sum of k homogeneous ReLU units. Examples have standard Gaussian inputs and exact labels. The question asks for a learner polynomial in dimension, width and inverse prediction error simultaneously. It may output any efficiently evaluable predictor and need not recover the hidden parameters. The positive-weight upper bound still has a quasipolynomial dependence on width and accuracy.

[Read in atlas](index.html#TCS-2111) · [Efficiently Learning One-Hidden-Layer ReLU Networks via SchurPolynomials](https://proceedings.mlr.press/v247/diakonikolas24c.html) · [Small Covers for Near-Zero Sets of Polynomials and Learning Latent Variable Models](https://arxiv.org/abs/2012.07774)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2339 — Linear recursive teaching dimension versus VC dimension

A finite concept class can be studied through both its VC dimension and its recursive teaching dimension. VC dimension measures the ability to realize label patterns, while recursive teaching measures how examples can identify concepts through successive elimination. The question asks whether one universal constant always bounds recursive teaching dimension by that constant times VC dimension. The same constant must work for every finite class. The project seeks a direct quantitative link between the complexity of learning from samples and the information needed for structured teaching.

[Read in atlas](index.html#TCS-2339) · [Tournaments, Johnson Graphs and NC-Teaching](https://proceedings.mlr.press/v201/simon23a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2654 — Strong universal consistency in online learning

Universal online learning seeks vanishing average regret against every fixed measurable prediction function. The source permits responses to depend arbitrarily on the history and imposes assumptions only on the input process. It asks for one strongly consistent rule whenever that input process belongs to the class admitting universal online learning. This strengthens the deterministic-target version by allowing general response sequences. An answer would identify whether learnability of the inputs alone can support one universal predictor even when the relationship between inputs and observed responses is neither fixed nor conditionally independent.

[Read in atlas](index.html#TCS-2654) · [Universally Consistent Online Learning with Arbitrarily Dependent Responses](https://proceedings.mlr.press/v167/hanneke22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3113 — Finite VC dimension versus agnostic computable PAC learning

Finite VC dimension characterizes statistical PAC learnability without requiring the learner to be computable. The source asks whether a finite-VC class can fail computable agnostic learning even when the learner may output hypotheses outside the class. The agnostic setting allows labels that no member fits perfectly, so the learner must compete with the best available hypothesis. Known failures of proper computable learning do not settle this more permissive output model. A counterexample or positive theorem would locate how much computational difficulty can be removed by abandoning the requirement to return a member of the original class.

[Read in atlas](index.html#TCS-3113) · [Open Problem: Are all VC-classes CPAC learnable?](https://proceedings.mlr.press/v134/open-problem-agarwal21b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3114 — Thus, the case that remains open concerns uncountable X and general (random) sequences X.

An optimistically universal online learner succeeds whenever the observed input process admits any universally consistent learning rule. The source isolates the difficult case of random sequences on an uncountable instance space. Memorizing labels handles some simpler regimes, but fails when fresh inputs keep appearing without exact repetition. The historical problem asks whether one algorithm can adapt across all learnable processes in either the weak or strong consistency sense. Later progress must be checked against those precise variants, since a result for deterministic targets or one mode of convergence need not settle every formulation.

[Read in atlas](index.html#TCS-3114) · [Open Problem: Is There an Online Learning Algorithm That Learns Whenever Online Learning Is Possible?](https://proceedings.mlr.press/v134/open-problem-hanneke21b.html)
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

### TCS-5215 — Accuracy threshold for agnostic ReLU learning

A single ReLU predicts a real value by applying the positive-part function to a linear form. The source studies agnostic learning over arbitrary distributions on the unit sphere and gives a running time polynomial in dimension but exponential in inverse error. Consequently, its method remains polynomial-time for errors at least on the order of one over log n. A reduction from noisy parity learning supplies a conditional obstruction when the requested error becomes inverse polynomial in n. The question is to determine the accuracy threshold between these regimes, even for this elementary neural unit.

[Read in atlas](index.html#TCS-5215) · [Reliably Learning the ReLU in Polynomial Time](https://proceedings.mlr.press/v65/goel17a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-2827 — Optimistically universal online learning with bounded losses

Optimistically universal online learning asks for one rule that succeeds whenever any universally consistent rule can. For bounded losses and deterministic measurable target labels, the input process can have arbitrary temporal dependence. Blanchard’s COLT 2022 theorem supplies such a rule and proves that learnability is exactly sublinear measurable visits. The partition condition is stronger than a statement about visits to finitely many selected regions. Both historical questions in this card are therefore resolved in their intended noiseless setting.

[Read in atlas](index.html#TCS-2827) · [Universal Online Learning with Unbounded Losses: Memory Is All You Need](https://proceedings.mlr.press/v167/blanchard22a.html) · [Open Problem: Is There an Online Learning Algorithm That Learns Whenever Online Learning Is Possible?](https://proceedings.mlr.press/v134/hanneke21b.html) · [Universal Online Learning: an Optimistically Universal Learning Rule](https://proceedings.mlr.press/v178/blanchard22b.html)
Existing status: `resolved` · Summary written: 2026-09-12

### TCS-4074 — Sample complexity of proper PAC learning

A proper learner must always return a hypothesis from the known concept class. The historical question asks whether this restriction can force an additional logarithmic factor in sample complexity. The answer is yes for some classes, even with randomized learners and unlimited computation. The 2018 journal version acknowledges this, and a 2020 theorem supplies matching worst-case lower bounds with finite-domain constructions. Other classes, including halfspaces, can still attain the smaller proper-learning bound.

[Read in atlas](index.html#TCS-4074) · [Optimal Quantum Sample Complexity of Learning Algorithms](https://doi.org/10.4230/LIPIcs.CCC.2017.25) · [Optimal Quantum Sample Complexity of Learning Algorithms — journal version](https://www.jmlr.org/papers/v19/18-195.html) · [Proper Learning, Helly Number, and an Optimal SVM Bound](https://proceedings.mlr.press/v125/bousquet20a.html)
Existing status: `resolved` · Summary written: 2026-09-12

## Cryptography (24)

### TCS-6545 — Public-key encryption from one-way functions

A one-way function is easy to evaluate but hard to invert on a randomly generated input. Public-key encryption needs a further asymmetry: anyone can encrypt using public information, while only the secret-key holder can decrypt. This project asks whether the existence of one-way functions alone guarantees such an encryption scheme in the standard classical model. Symmetric encryption follows from one-way functions, but its initially shared secret does not supply the missing public-key structure. The question allows constructions that inspect the implementation of the underlying function, so limitations of black-box constructions do not settle it.

[Read in atlas](index.html#TCS-6545) · [Foundations of Cryptography, Lecture 10](https://mit6875.github.io/FA23SLIDES/lec10.pdf) · [The Complexity of Public-Key Cryptography](https://eprint.iacr.org/2017/365) · [Limits on the provable consequences of one-way permutations](https://doi.org/10.1145/73007.73012) · [A Pseudorandom Generator from any One-way Function](https://johanhastad.se/prgfromowf.pdf) · [Merkle Puzzles are Optimal — an \(O(n^{2})\)-query attack on any key exchange from a random oracle](https://www.boazbarak.org/Papers/merkle.pdf) · [Public-Key Encryption from the MinRank Problem](https://arxiv.org/abs/2510.03752)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-6454 — Low-noise LPN hardness from Nearest Codeword hardness

Learning parity with noise asks for information about hidden binary linear equations when some answers have been flipped. This project asks whether worst-case hardness of the binary nearest-codeword problem implies average-case hardness for a specified low-noise LPN distribution. The chosen regime uses quadratically many samples and a noise rate inversely proportional to the square root of the secret dimension. A reduction must produce that particular random-instance distribution rather than merely another hard coding problem or a different noise level. Such a connection would strengthen the theoretical foundation of low-noise LPN in the way worst-case reductions support lattice-based assumptions.

[Read in atlas](index.html#TCS-6454) · [Towards Worst-case Hardness for Low-Noise LPN](https://eccc.weizmann.ac.il/report/2026/095/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1138 — Polynomial-time computationally sound NP verification of #SAT

Counting satisfying assignments is harder to certify directly than showing that a single satisfying assignment exists. This project asks for a polynomial-time verifier for a claimed #SAT answer in the model called computationally sound NP by the source. Soundness is required against computationally bounded attempts to produce false proofs rather than against every possible proof string. That distinction allows the question to go beyond ordinary NP verification without asserting that #SAT has standard short certificates. A construction would expand the range of efficiently checkable counting claims and connect computational soundness with the source's broader study of derandomization.

[Read in atlas](index.html#TCS-1138) · [New ways of studying the \(\mathrm{BPP} = \mathrm{P}\) conjecture](https://eccc.weizmann.ac.il/report/2023/094/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2732 — Subpolynomial-key perfectly secure three-server DPFs

A distributed point function splits a vector that is nonzero at one hidden position into compact evaluation keys held by several servers. Combining their outputs recovers the point function while permitted individual views hide its location. The question asks for a perfectly secure three-server construction with key size \(N^{o}(1)\), subpolynomial in the domain size N. The source achieves statistical privacy with three servers and perfect privacy with four, leaving the simultaneous three-server and perfect-security target. Meeting it would improve information-theoretic private retrieval and aggregation by reducing server requirements without giving up exact privacy.

[Read in atlas](index.html#TCS-2732) · [Information-Theoretic Distributed Point Functions](https://doi.org/10.4230/LIPIcs.ITC.2022.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3025 — Exponentially hard weak versus strong one-way functions

A weak one-way function resists inversion on a noticeable fraction of inputs, while a strong one-way function resists almost every efficient inversion attempt. Standard hardness amplification connects the two at ordinary polynomial security scales. This project asks whether equivalence also holds when the starting and resulting functions must both withstand exponential-time attacks relative to their input length. The obstacle is that familiar amplification increases input length enough to weaken the resulting exponent. A tighter transformation would preserve fine-grained cryptographic hardness and strengthen connections between one-wayness and average-case complexity.

[Read in atlas](index.html#TCS-3025) · [Hardness of KT Characterizes Parallel Cryptography](https://doi.org/10.4230/LIPIcs.CCC.2021.35)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4754 — Unconditional zero knowledge for gap circuit complexity

The input is a complete truth table promised to have either a small or a much larger minimum circuit. The selected question asks for some fixed gap admitting an unconditional computational zero-knowledge proof. The verifier is efficient, while soundness must hold even against an unbounded cheating prover. All promised inputs and all input lengths must satisfy the guarantees. Average-case protocols and the later one-way-function characterization do not establish this membership.

[Read in atlas](index.html#TCS-4754) · [A Relativization Perspective on Meta-Complexity](https://doi.org/10.4230/LIPIcs.STACS.2022.54) · [Robustness of Average-Case Meta-Complexity via Pseudorandomness](https://doi.org/10.1145/3519935.3520051) · [One-Way Functions and Zero Knowledge](https://doi.org/10.1137/24M1689971)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5013 — Sublinear-communication secure computation with polynomial setup

Pre-distributed correlated randomness can reduce how much two parties need to communicate during secure computation. The selected problem asks whether communication can be sublinear in the circuit size while both running time and the correlated-randomness supply stay polynomial in the input length. The source proves strong setup lower bounds for protocols that push online communication all the way to its optimum. Those extreme-case lower bounds leave room between ordinary circuit-size communication and full communication optimality. Understanding that intermediate regime would identify whether practical preprocessing can buy a substantial communication saving under perfect security.

[Read in atlas](index.html#TCS-5013) · [Exponential Correlated Randomness Is Necessary in Communication-Optimal Perfectly Secure Two-Party Computation](https://doi.org/10.4230/LIPIcs.ITC.2023.18)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-6953 — Cryptographic primitives from worst-case or average-case hardness

Cryptographic hardness must occur on instances that honest users can efficiently generate, rather than only on a difficult exceptional input. The cited question asks whether \(\mathrm{P} \ne  \mathrm{NP}\), or a suitable average-case separation between distributional classes, already implies one-way functions. It also asks about the stronger possibility of trapdoor functions, where secret information enables inversion that remains hard publicly. These targets add progressively more structure to a bare claim that efficient algorithms cannot solve everything. Establishing the implications would connect cryptographic foundations to broad complexity assumptions instead of relying on individual number-theoretic or algebraic candidates.

[Read in atlas](index.html#TCS-6953) · [Mathematics and Computation](https://www.math.ias.edu/avi/book)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-3556 — Non-tight verifiable delay functions from a random oracle alone

A verifiable delay function must take sequential effort to evaluate while its unique output can be publicly checked quickly. The source asks whether a random oracle alone can provide this even with a weaker delay requirement such as half the honest time. Proofs of sequential work do not settle the issue because they need not have unique outputs. Published results in 2025 and 2026 rule out computationally unique VDFs, ultimately including private and expensive setup. The historical question is resolved in the parallel oracle query model, where internal computation is unrestricted.

[Read in atlas](index.html#TCS-3556) · [Can Verifiable Delay Functions Be Based on Random Oracles?](https://doi.org/10.4230/LIPIcs.ICALP.2020.83) · [Breaking Verifiable Delay Functions in the Random Oracle Model](https://eprint.iacr.org/2024/766) · [Impossibility of VDFs in the ROM: The Complete Picture](https://eprint.iacr.org/2025/1773)
Existing status: `resolved` · Summary written: 2026-09-12

## Quantum computation and information (54)

### TCS-6446 — Quantum PCP conjecture

The quantum PCP conjecture asks whether even a coarse estimate of a quantum system's lowest energy can capture the difficulty of verifying quantum proofs. The system is specified by local interactions, each involving only a bounded number of qubits. The target is hardness for distinguishing two possible ground energies separated by a constant after normalizing the total interaction strength. Normalization prevents a small gap from becoming a constant merely by multiplying the Hamiltonian by a large number. The problem connects robust quantum verification with entanglement, quantum codes, and the limits of approximation algorithms.

[Read in atlas](index.html#TCS-6446) · [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495) · [Private PCPs from Product Expansion](https://eccc.weizmann.ac.il/report/2026/150/)
Existing status: `source_open` · Summary written: 2026-09-11

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

### TCS-5021 — Limiting optimized QAOA energy in the SK model

QAOA is a widely studied quantum optimization ansatz using alternating objective and mixing operations. The SK model provides a canonical random quadratic objective with a known limiting optimum. The question asks for the best limiting energy reachable by finite-depth QAOA when depth is subsequently allowed to grow. Angles are optimized only after taking the infinite-size ensemble limit. The source conjectures that this limiting value reaches the Parisi optimum, and the card now accepts a proved numerical determination within 0.01.

[Read in atlas](index.html#TCS-5021) · [The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model](https://doi.org/10.4230/LIPIcs.TQC.2022.7)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-1882 — Optimal quantum query complexity of uniformity testing

Uniformity testing distinguishes a perfectly uniform distribution from one separated in total variation distance. The tester can coherently call a unitary preparing the distribution, its inverse and its controlled version. Its guarantee must hold for arbitrary garbage states and arbitrary valid unitary extensions. The target is the optimal query count jointly in domain size and distance, up to universal factors. The source supplies a candidate upper bound whose matching lower bound remains conjectural.

[Read in atlas](index.html#TCS-1882) · [Uniformity Testing When You Have the Source Code](https://doi.org/10.4230/LIPIcs.TQC.2025.7) · [Uniformity testing when you have the source code — version record](https://arxiv.org/abs/2411.04972v1)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0861 — \(\mathrm{QMA}(2)\) versus BQEXP

\(\mathrm{QMA}(2)\) allows a quantum verifier to receive two witnesses promised to be unentangled with each other. The question asks whether every problem with such a proof system can be decided by a bounded-error quantum algorithm in exponential time. The saved source contrasts this proposed BQEXP upper bound with a nondeterministic exponential-time upper bound. Exploiting the independence of the witnesses is difficult because it restricts possible proofs without turning them into ordinary classical certificates. A better upper bound would locate the computational power of unentangled quantum proofs more precisely among large complexity classes.

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

### TCS-0862 — Constant-round QRG versus PSPACE

Quantum refereed games model a verifier interacting with opposing provers, one trying to obtain acceptance and the other rejection. The number of interaction rounds can change the power of the resulting proof system. This problem asks whether every game with a fixed constant number of rounds can be decided using polynomial space. The saved source contrasts the one-round case with the stronger class obtained when polynomially many rounds are available. Understanding the intermediate regime would show how quickly repeated quantum interaction increases the complexity of adversarial verification.

[Read in atlas](index.html#TCS-0862) · [TCS Open Problems](https://tcsopenproblems.com/problem/13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0027 — Black-box unitary synthesis

An arbitrary unitary transformation may require an enormous circuit when described directly. This question asks whether access to a suitably chosen classical Boolean oracle can always make that transformation efficiently implementable by a quantum computer. The oracle may depend on the unitary, but the implementation must act correctly on arbitrary input states. Aaronson's survey distinguishes this from preparing one chosen state or reproducing the unitary on only a few basis vectors. The problem tests whether difficult quantum transformations can always be made easy by supplying enough classical black-box information.

[Read in atlas](index.html#TCS-0027) · [Open Problems Related to Quantum Query Complexity](https://www.scottaaronson.com/papers/open.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

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

### TCS-4238 — Sequential randomness certification against non-signaling adversaries

Sequential measurements can extract certified randomness from an entangled system while preserving some ability to use it again. The cited work analyzes this phenomenon against adversaries constrained by quantum mechanics. This question asks whether unbounded certified randomness remains possible against the broader class of adversaries constrained only by no-signaling. The geometry of the no-signaling correlation set differs from the quantum set used in the paper's argument. A bound or construction would determine how much repeated randomness certification depends on trusting quantum theory beyond the prohibition on faster-than-light signaling.

[Read in atlas](index.html#TCS-4238) · [A Single Entangled System Is an Unbounded Source of Nonlocal Correlations and of Certified Random Numbers](https://doi.org/10.4230/LIPIcs.TQC.2017.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4457 — Simulation or postselection universality for two-qubit interactions

The proposed dichotomy covers every fixed two-qubit interaction, including noncommuting ones. Circuits begin and end in the computational basis and have no freely supplied local gates. The alternatives are efficient classical simulation or universality under postselection. The source handles commuting interactions, while later analog Hamiltonian-universality results use a different model. The general easy-branch accuracy and numerical representation still need specification before the statement is complete.

[Read in atlas](index.html#TCS-4457) · [Complexity Classification of Two-Qubit Commuting Hamiltonians](https://doi.org/10.4230/LIPIcs.CCC.2016.28) · [The Space Around BQP](https://dspace.mit.edu/server/api/core/bitstreams/ad343002-e1d8-4966-96ac-7d32b3b215d4/content) · [General Conditions for Universality of Quantum Hamiltonians](https://doi.org/10.1103/PRXQuantum.3.010308)
Existing status: `uncertain` · Summary written: 2026-09-12

### TCS-4615 — Quantum entropy inequalities beyond strong subadditivity

For a multipartite quantum state, the entropies of all subsystems form a vector subject to universal inequalities. Positivity and strong subadditivity give basic constraints on those vectors. This question asks whether additional inequalities are needed to describe the quantum entropy cone for four or more parties. The cited stabilizer-state analysis relates the problem to classical non-Shannon inequalities and to states violating the Ingleton inequality. New constraints or counterexamples would sharpen the mathematical description of how quantum information can be shared among several systems.

[Read in atlas](index.html#TCS-4615) · [The Quantum Entropy Cone of Stabiliser States](https://doi.org/10.4230/LIPIcs.TQC.2013.270)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4715 — Succinct entangled proofs with efficient provers

Succinct quantum verification aims to check a large computation or witness using very little communication. In the entangled two-prover setting, making verifier questions short is more tractable than making prover answers short. The source explains that efficient honest provers and small communication must be achieved together, so powerful protocols with inefficient provers do not meet the intended target. It uses compiled nonlocal games to combine useful features of cryptographic and multiprover approaches. The remaining direction is to obtain fully succinct verification while overcoming the difficult answer-reduction step in a sound quantum setting.

[Read in atlas](index.html#TCS-4715) · [Succinct Arguments for QMA from Standard Assumptions via Compiled Nonlocal Games](https://doi.org/10.1109/FOCS61266.2024.00078)
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
