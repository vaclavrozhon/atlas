# Working summaries — small categories

601 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computability and algorithmic information theory (18)

### TCS-6646 — Martin’s conjecture

Turing-invariant functions send mutually computable reals to mutually computable outputs. Under determinacy and dependent choice, Martin’s conjecture predicts a rigid hierarchy for these operations when they are compared on Turing cones. Part I says every invariant function is constant in degree on a cone or computes its input on a cone. Part II says all operations above the identity are prewellordered, with the Turing jump increasing their ordinal rank by exactly one. Known uniform and order-preserving cases, choice-based counterexamples and conditional results for other output degrees leave the full stated conjecture unresolved in the checked sources.

[Read in atlas](index.html#TCS-6646) · [On the Hierarchy of Natural Theories](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/on-the-hierarchy-of-natural-theories/FEF058E948E6E8B8A4F5F174E02AFCC9) · [Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://arxiv.org/abs/1109.1875v2) · [Part 1 of Martin’s Conjecture for order-preserving and measure-preserving functions](https://arxiv.org/abs/2305.19646v3) · [Erratum — Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://math.berkeley.edu/~marks/errata/mss_errata.html) · [On a question of Slaman and Steel](https://arxiv.org/abs/2004.00174v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6648 — Kolmogorov–Loveland randomness versus Martin-Löf randomness

Kolmogorov–Loveland betting strategies may adaptively inspect previously unseen bits in any order while making fair computable bets. The question asks whether every sequence defeating all such strategies is Martin-Löf random. Martin-Löf randomness instead requires avoidance of every effective sequence of small-measure exceptional sets. Equality would show that flexible computable betting captures the full statistical-test notion of algorithmic randomness. The reviewed model allows partial strategies and unbounded capital success, so limitations for fixed reading orders or weaker betting rules cannot settle the comparison.

[Read in atlas](index.html#TCS-6648) · [Kolmogorov-Loveland betting strategies lose the Betting game on open sets](https://arxiv.org/abs/2403.19817) · [Kolmogorov–Loveland randomness and stochasticity](https://people.math.wisc.edu/~jsmiller8/Papers/kl.pdf) · [Comparing notions of randomness](https://people.math.wisc.edu/~slempp/papers/injrandom.pdf) · [A universal pair of \(1/2\)-betting strategies](https://www.sciencedirect.com/science/article/pii/S0890540121000183)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6647 — Rigidity of the Turing degrees

Turing degrees identify sets of integers that compute one another and order them by relative computability. The rigidity question asks whether every order-preserving bijection of this entire partial order fixes every degree. A positive answer would mean that the order structure alone determines the identity of each degree. This is a basic structural question about how much information is encoded by the pattern of computational reducibility. The saved review permits arbitrary set-theoretic automorphisms, so excluding computable transformations or automorphisms induced by a special action on representatives is only a restricted result.

[Read in atlas](index.html#TCS-6647) · [Defining the Turing Jump](https://math.berkeley.edu/~slaman/papers/jump.pdf) · [Global Properties of the Turing Degrees and the Turing Jump](https://math.berkeley.edu/~slaman/papers/IMS_slaman.pdf) · [Permutations of the Integers Induce Only the Trivial Automorphism of the Turing Degrees](https://arxiv.org/abs/1603.00525)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6685 — Busy Beaver \(\mathrm{BB}(6)\)

\(\mathrm{BB}(6)\) is the maximum halting runtime among six-state, two-symbol Turing machines started on a blank tape. The accepted answer specifies one concrete machine and proves in Lean that it halts and no other halting machine in the same class runs longer. Its runtime describes \(\mathrm{BB}(6)\) exactly, so no simple closed form, decimal expansion or full execution trace is required. The problem turns the general undecidability of halting into an exceptionally concrete finite classification challenge. The saved review records large candidate runtimes and unresolved holdouts, and distinguishes runtime from the separate Busy Beaver measure counting printed ones.

[Read in atlas](index.html#TCS-6685) · [\(\mathrm{BB}(6)\)](https://wiki.bbchallenge.org/w/index.php?title=BB(6)&oldid=8417) · [Story: Turing machines and the Busy Beaver function](https://bbchallenge.org/story) · [Determination of the fifth Busy Beaver value](https://arxiv.org/abs/2509.12337v2) · [Antihydra](https://bbchallenge.org/antihydra) · [Holdouts lists](https://wiki.bbchallenge.org/wiki/Holdouts)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6649 — Reversal of Hindman’s theorem to the \(\omega\)-jump

Hindman's theorem finds an infinite set whose nonempty finite sums all receive the same color in any finite coloring. The question asks whether this principle proves the existence of every set's iterated omega-th Turing jump over RCA0. It measures the theorem's logical strength rather than asking whether the combinatorial statement is true in ordinary mathematics. A positive implication would show that unrestricted finite-sums homogeneity entails a strong closure principle for computability. The reviewed formulation allows sums of arbitrarily many distinct elements, so results for exactly two terms or other restricted variants do not answer it automatically.

[Read in atlas](index.html#TCS-6649) · [New bounds on the strength of some restrictions of Hindman’s Theorem](https://iris.uniroma1.it/bitstream/11573/1393123/3/Carlucci_postprint_New-bounds_2020.pdf) · [The reverse mathematics of Hindman’s theorem for sums of exactly two elements](https://arxiv.org/abs/1804.09809) · [The strength of Ramsey’s theorem for coloring relatively large sets](https://arxiv.org/abs/1204.1134) · [The reverse mathematics of the Ordered Variable Word theorem](https://arxiv.org/abs/2606.12962) · [\(\Pi ^{0}_{4}\) conservation of a Carlson-Simpson lemma for 1-variable words](https://arxiv.org/abs/2607.28116)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6679 — Universality of Turing equivalence

Turing equivalence groups infinite binary sequences according to mutual computability. The question asks whether every countable Borel equivalence relation can be reduced to this relation by a Borel map. Such universality would mean that relative computability realizes the full classification complexity available among countable Borel equivalence relations. The map must preserve both equivalence and inequivalence for every pair, rather than merely describe typical behavior. The saved statement does not require the map to be computable or uniform on witnesses, making results about more restrictive reductions or resource-bounded equivalence separate issues.

[Read in atlas](index.html#TCS-6679) · [The Fourteen Victoria Delfino Problems and Their Status in the Year 2019](https://preprint.math.uni-hamburg.de/public/papers/hbm/hbm770.pdf) · [The Theory of Countable Borel Equivalence Relations](https://www.pma.caltech.edu/documents/5921/CBER.pdf) · [Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://arxiv.org/abs/1109.1875) · [The universality of polynomial time Turing equivalence](https://arxiv.org/abs/1601.03343) · [Uniformity, Universality, and Computability Theory](https://arxiv.org/abs/1606.01976) · [On a question of Slaman and Steel](https://arxiv.org/abs/2004.00174)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7193 — Mortality of \(2\times 2\) integer matrix semigroups

A finite list of two-by-two integer matrices generates all nonempty products with arbitrary order and repetition. The question asks whether a terminating algorithm can decide if any such product is the zero matrix. Matrix entries and the number of generators are unrestricted. NP-hardness is known, while decidability results for restricted determinants do not cover the general case. Resolving the question would locate a basic computability boundary for products of small matrices.

[Read in atlas](index.html#TCS-7193) · [Mortality for \(2 \times  2\) Matrices is NP-hard](https://cgi.csc.liv.ac.uk/~igor/papers/paper_BHP_MFCS2012.pdf) · [On Affine Reachability Problems](https://arxiv.org/abs/1905.05114v3) · [The membership problem for subsemigroups of \(GL_{2}(\mathbb{Z} )\) is NP-complete](https://doi.org/10.1016/j.ic.2023.105132) · [On Word Representations and Embeddings in Complex Matrices](https://arxiv.org/abs/2604.15386v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0250 — Scaling joint Kolmogorov-complexity profiles

Every tuple of strings has a profile of complexities of its nonempty subtuples. The question asks whether that whole profile can be multiplied by any fixed positive real factor. One new tuple must realize all the scaled quantities within logarithmic additive error. No fixed algorithm mapping the old tuple to the new one is required. The target concerns the homogeneous geometry of shared algorithmic information.

[Read in atlas](index.html#TCS-0250) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Algebraic Barriers to Halving Algorithmic Information Quantities in Correlated Strings](https://doi.org/10.4230/LIPIcs.MFCS.2025.84)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0247 — Shannon feasibility from algorithmic network coding

Several correlated sources must be transmitted through a fixed directed acyclic network to designated recipients. Shannon coding chooses local encoding and decoding maps that work with high probability for random source blocks. Algorithmic coding instead allows each realized block to have its own short local programs and compatible edge messages. The question asks whether high-probability algorithmic feasibility with logarithmic overhead always implies Shannon feasibility at the same asymptotic rates. The target is this general converse, with vanishing error and rate slack defined explicitly, rather than a finite-block equivalence inferred from the title.

[Read in atlas](index.html#TCS-0247) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Multisource Algorithmic Information Theory](https://www.lirmm.fr/~ashen/multisource-dagstuhl.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0287 — Strong extractors for infinite sequences

The question asks for one computable transformation of two independent infinite binary sequences of effective dimension one half. Its output must have effective dimension one even when either entire input is available as an oracle. Independence is the global oracle condition, which is stronger than comparing only finite input prefixes. The transformation may use unbounded computation but must produce every output bit on every promised input pair. Known ordinary extraction, finite-string strong extraction and finite-state impossibility results do not settle this stated target.

[Read in atlas](index.html#TCS-0287) · [Computability, Complexity and Randomness](https://doi.org/10.4230/DagRep.2.1.19) · [Algorithmically independent sequences](https://doi.org/10.1016/j.ic.2009.05.004) · [Two sources are better than one for increasing the Kolmogorov complexity of infinite sequences](https://arxiv.org/abs/0705.4658) · [Generating Kolmogorov random strings from sources with limited independence](https://doi.org/10.1093/logcom/exr053) · [Randomness Extraction Fails for Finite-State Dimension](https://doi.org/10.4230/LIPIcs.LICS.2026.78)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0238 — An algorithmic Ahlswede–Körner lemma

For individual binary strings x and y, side information z can shorten descriptions of either string and of their pair. The question asks whether another string \(z'\) can preserve those three conditional description lengths to logarithmic accuracy. The replacement must have a logarithmically short description when x and y are both given. It need not be easy to obtain from z, and no fast construction is required. The source establishes a special case for stochastic pairs, while the general question tests the scope of an algorithmic analogue of the Ahlswede–Körner lemma.

[Read in atlas](index.html#TCS-0238) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0254 — Networks characterized by information-flow inequalities

A communication network imposes capacity and topology restrictions on how information reaches its destinations. The source asks which networks are characterized by information-flow inequalities. A characterization would identify when satisfying abstract information constraints is sufficient for an actual coding scheme. The difficulty is that inequalities summarize numerical information amounts while feasible codes must coordinate concrete messages across the entire network. The saved label does not specify the permitted coding model or family of inequalities, so a full statement must recover these before deciding whether a network lies in the proposed class.

[Read in atlas](index.html#TCS-0254) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/kolm.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0240 — Communication for algorithmic secret-key agreement

Algorithmic secret-key agreement studies parties holding correlated strings who communicate to obtain a shared key hidden from an observer. The saved question concerns the amount of communication required for that agreement. The difficulty is to exploit common information while ensuring that the public transcript does not reveal the key itself. A sharp bound would connect individual-string information profiles with the operational cost of secure coordination. The source label does not specify side information, key length, randomness, or permitted complexity error, so these must be restored before stating a concrete communication tradeoff.

[Read in atlas](index.html#TCS-0240) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/kolm.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0279 — Extraction of mutual information about two strings

Two strings can share algorithmic information even when that information is not visibly stored as a common substring. The source asks about extracting mutual information into an appropriate explicit object. The challenge is to construct a description that captures the shared part while respecting the source's complexity guarantees. An answer would clarify whether numerical mutual information has an operational interpretation for individual finite data. The saved entry does not specify the extractor's access, allowed communication, or complexity losses, so the exact extraction goal must be recovered before proposing a construction or impossibility claim.

[Read in atlas](index.html#TCS-0279) · [Computability, Complexity and Randomness](https://doi.org/10.4230/DagRep.2.1.19)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2202 — NP-hardness of conditional polynomial-time pKt

Conditional pKt measures a probabilistic, time-sensitive form of description complexity when auxiliary information is supplied. The source asks whether computing it is NP-hard in a polynomial-time parameter regime. Such hardness would relate an information-theoretic quantity for individual strings to conventional worst-case computational difficulty. The conditional setting matters because the side information can change both the shortest description and how it can be verified. The saved passage leaves the approximation gap, time parameter, and reduction type unspecified, and these must be restored before a precise NP-hardness proposition can be stated.

[Read in atlas](index.html#TCS-2202) · [Impagliazzo’s Worlds Through the Lens of Conditional Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2024.110)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4185 — Existence of strings without simple optimal hypotheses

Algorithmic statistics seeks a simple probability distribution that plausibly explains an individual data string. The source studies versions constrained by polynomial computation time and distinguishes acceptable, plausible, and optimal hypotheses. The question asks whether some strings have no simple optimal hypothesis in this resource-bounded framework. An optimal explanation must meet the paper's coding-based criterion, rather than merely pass the available statistical tests. An example lacking such explanations would show that efficient statistical modeling can fail for intrinsic computational reasons, even when unrestricted descriptions offer a different picture.

[Read in atlas](index.html#TCS-4185) · [Stochasticity in Algorithmic Statistics for Polynomial Time](https://doi.org/10.4230/LIPIcs.CCC.2017.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5010 — Unconditional coding theorem for randomized Kolmogorov complexity

Randomized Kolmogorov complexity measures how short a randomized description can be while reproducing an object under specified resource bounds. The cited source asks for an unconditional existential coding theorem for rKpoly relative to its PSAMP model. Coding theorems connect the probability of an output under a sampler with the description length needed to specify it. An unconditional relation would strengthen that bridge without additional complexity assumptions. The excerpt truncates its alternative consequence and does not define the exact sampling and success conventions, so the notation alone is insufficient for a complete theorem.

[Read in atlas](index.html#TCS-5010) · [Optimal Coding for Randomized Kolmogorov Complexity and Its Applications](https://doi.org/10.1109/FOCS61266.2024.00030)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6105 — Computability of the Mandelbrot set

The Mandelbrot set consists of complex parameters for which repeatedly applying the associated quadratic map to zero gives a bounded orbit. The computability question asks whether one program can approximate this entire compact set to every requested accuracy. This is stronger than producing convincing images at selected resolutions or testing many individual parameters. The source cites the question as motivation for studying computability and semicomputability of geometric sets. A solution would connect effective approximation of a familiar fractal with rigorous information about the global behavior of complex dynamical systems.

[Read in atlas](index.html#TCS-6105) · [Semicomputable Geometry](https://doi.org/10.4230/LIPIcs.ICALP.2018.129)
Existing status: `uncertain` · Summary written: 2026-09-11

## Proof complexity (27)

### TCS-6601 — Superpolynomial Extended Frege lower bounds

Extended Frege is a classical propositional proof system that can introduce reusable names for previously specified formulas. The question asks whether no single polynomial bounds the shortest proof of every tautology by its statement length. The target counts the full encoded proof and allows arbitrary depth and reuse of earlier lines. Its negation would give short proofs for every tautology without necessarily making them easy to find. Recent conditional, algebraic and intuitionistic results do not supply the unrestricted classical lower bound.

[Read in atlas](index.html#TCS-6601) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Towards \(\mathrm{P}\ne \mathrm{NP}\) from Extended Frege lower bounds](https://arxiv.org/abs/2312.08163) · [SNARGs for NP from Unprovability of Mathematical Theorems](https://eccc.weizmann.ac.il/report/2026/098/) · [A Lower Bound for Polynomial Calculus with Extension Rule](https://mirror.theoryofcomputing.org/articles/v022a004/) · [Author correction to The Relative Efficiency of Propositional Proof Systems](https://www.cs.utoronto.ca/~sacook/) · [Exponential Gaps Between Intuitionistic Linear Extended Frege Systems](https://arxiv.org/abs/2609.00422v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6663 — Frege versus Extended Frege

Extended Frege permits named definitions that share intermediate formulas within an otherwise ordinary propositional proof. The question asks whether every such proof has an ordinary Frege proof of the same conclusion with only polynomially larger total encoded size. The statement fixes the formula syntax, inference rules, freshness conditions and binary accounting while allowing unrestricted depth and reuse of proof lines. Known finite-consistency characterizations, fixed-parameter combinatorial upper bounds and restricted algebraic simulations do not settle this universal comparison. A complete Lean proof must establish either one universal polynomial size bound or its logical negation, without imposing a polynomial-time procedure for finding translated proofs.

[Read in atlas](index.html#TCS-6663) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Propositional Consistency Proofs](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/prop_consis/paper.pdf) · [Towards (Non-)Separations in Propositional Proof Complexity](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Stanford_February2014/) · [Short Proofs of the Kneser–Lovász Coloring Principle](https://arxiv.org/abs/1505.05531) · [Extended Frege proofs, circuits and rewriting](https://arxiv.org/abs/2606.13367) · [Quasi-polynomial Frege Simulation of IPS beyond Noncommutativity](https://eccc.weizmann.ac.il/report/2026/166/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6602 — Superpolynomial \(\mathrm{AC}^{0}[p]\)-Frege lower bounds

Modular Frege proofs can reason with shallow Boolean formulas containing gates that count true inputs modulo a fixed prime. The problem asks for one polynomial-time constructible DNF tautology family per prime that requires superpolynomial total proof size at every fixed logical line depth. The statement fixes a complete finite classical calculus, the modular recurrence axioms, all encodings and the distinction between formula depth and unrestricted derivation depth. Ordinary bounded-depth lower bounds and recent parity-resolution or restricted algebraic results do not establish this stronger modular-Frege target. A complete Lean proof must supply genuine tautologies and all construction and lower-bound guarantees, or prove the logical negation of the specified family-existence claim.

[Read in atlas](index.html#TCS-6602) · [Extended Nullstellensatz proof systems](https://www.karlin.mff.cuni.cz/~krajicek/finitary.pdf) · [Exponential Lower Bounds for the Pigeonhole Principle](https://www.cs.toronto.edu/~toni/Papers/exp-pigeon.pdf) · [Amortized Closure and Its Applications in Lifting for Resolution over Parities](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.8) · [\(\mathrm{AC}^{0}(p)\)-Frege Cannot Efficiently Prove That Constant-Depth Algebraic Circuit Lower Bounds Are Hard](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.99) · [Resolution Width Lifts to Near-Quadratic-Depth \(\operatorname{Res}(\oplus)\) Size](https://eccc.weizmann.ac.il/report/2026/018/) · [Hard CNF Instances for Ideal Proof Systems](https://eccc.weizmann.ac.il/report/2026/070/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0025 — Superpolynomial lower bounds for unrestricted Frege proofs

Ordinary Frege is a fixed finite calculus for propositional reasoning that allows arbitrary intermediate formulas and unrestricted reuse of earlier deductions. The question asks whether every proposed polynomial bound fails to cover the shortest Frege proofs of some genuine tautologies. Both the conclusion and the entire proof are measured by explicit binary encodings, including repeated formulas and inference references. Known lower bounds with depth, tree or line-size restrictions and recent algebraic lower bounds do not settle the unrestricted comparison. A complete Lean proof must establish failure of every universal polynomial bound or prove one bound for all tautologies, without an additional proof-search or hard-family construction requirement.

[Read in atlas](index.html#TCS-0025) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf) · [Polynomial Size Proofs of the Propositional Pigeonhole Principle](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/php_PolyFrege/FregePHP.pdf) · [Superpolynomial Length Lower Bounds for Tree-Like Semantic Proof Systems with Bounded Line Size](https://arxiv.org/abs/2604.28172) · [\(Res(\log )\) Proves Bounded-Depth Frege Lower Bounds](https://eccc.weizmann.ac.il/report/2026/055/) · [A Lower Bound for Polynomial Calculus with Extension Rule](https://mirror.theoryofcomputing.org/articles/v022a004/) · [Quasi-polynomial Frege Simulation of IPS beyond Noncommutativity](https://eccc.weizmann.ac.il/report/2026/166/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7162 — Existence of p-optimal proof systems

Does one propositional proof system efficiently translate proofs from every other efficiently checkable system? The translation must preserve the proved formula and run in time polynomial in the given proof length. Each simulated system may have its own translator and polynomial. This is stronger than comparing proof lengths alone, and different from requiring short proofs of every tautology. The 2026 oracle and jump-operator results leave the ordinary, oracle-free existence question open.

[Read in atlas](index.html#TCS-7162) · [Propositional proof systems, the consistency of first-order theories and the complexity of computations](https://doi.org/10.2307/2274765) · [The SPARSE-Relativization Framework and Applications to Optimal Proof Systems](https://arxiv.org/abs/2602.02294) · [Recursive Jump Operators and Optimal Proof Systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.88)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7163 — Effective polynomial simulation of Extended Frege by Resolution

Resolution refutes inconsistent clauses, while Extended Frege permits named intermediate Boolean formulas. Ordinary proof-size comparisons keep the statement fixed and separate these systems. This question allows a polynomial-time transformation of the statement, given a unary bound on an EF proof’s length. Whenever that bound is sufficient, the transformed CNF must have a comparably short Resolution refutation, while correctness must be preserved for every input. An answer would clarify whether efficient preprocessing can overcome the proof-size gap between these systems.

[Read in atlas](index.html#TCS-7163) · [Effectively polynomial simulations](https://www.cs.toronto.edu/~toni/Papers/effsimulation.pdf) · [Regular resolution effectively simulates resolution](https://arxiv.org/abs/2402.15871)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0024 — Frege lower bounds from circuit hardness

Some major lower-bound questions concern Boolean circuits, while others concern the size of propositional proofs. This card asks whether superpolynomial circuit hardness for an NP language forces superpolynomial Frege proof size. The premise allows fully nonuniform circuits, and the conclusion concerns ordinary unrestricted-depth Frege. A fixed complete proof calculus and explicit size conventions make both sides precise. Known connections for weaker systems, additional assumptions or different algebraic models do not settle this implication.

[Read in atlas](index.html#TCS-0024) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Towards P ≠ NP from Extended Frege Lower Bounds](https://eccc.weizmann.ac.il/report/2023/199/) · [Quasi-polynomial Frege Simulation of IPS beyond Noncommutativity](https://eccc.weizmann.ac.il/report/2026/166/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6768 — Simultaneous polynomial-length constant-space refutations

The question asks whether every fixed-width CNF family with constant-clause-space refutations also has refutations that are both polynomial-length and constant-clause-space. The same proof must meet both bounds, but its allowed constant space may exceed the original one. Space counts stored clauses regardless of their lengths, while proof length counts downloads and inferences. Known separate short-proof guarantees and results for constant total literal space do not provide the requested simultaneous clause-space bound. The later checked work still poses the question and proves only a polynomial lower bound for a restricted tree-like setting.

[Read in atlas](index.html#TCS-6768) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Space Characterizations of Complexity Measures and Size-Space Trade-Offs in Propositional Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.100) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1099 — Separating levels of bounded arithmetic

The question asks whether two positive levels of Buss’s bounded-arithmetic hierarchy prove different sentences. Each level has the same basic arithmetic axioms but permits induction for a different class of bounded formulas. A solution may choose any two distinct positive levels and must prove an unconditional difference in their deductive strength. The full axiom list, formula grammar and induction scheme specify the theories without relying on an unstated standard model. Recent conditional separations do not provide the unconditional nonprovability witness required here.

[Read in atlas](index.html#TCS-1099) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416) · [Bounded Arithmetic, Propositional Logic, and Complexity Theory](https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf) · [Parallelism and Adaptivity in Student-Teacher Witnessing](https://arxiv.org/abs/2602.19934)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1096 — Unprovability of polynomial circuit upper bounds in \(S_2^1\)

For each fixed polynomial exponent, the question asks for a polynomial-time predicate whose corresponding circuit upper bounds cannot be proved in S-two-one. The same predicate must resist every fixed multiplicative coefficient in that exponent. Its function representation, the arithmetic theory, circuit encoding and length quantifiers are explicitly specified. The conclusion is nonprovability of upper bounds, not an asserted standard-model circuit lower bound. Recent weaker-theory results and EXP consistency results leave this particular target open in the checked sources.

[Read in atlas](index.html#TCS-1096) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416) · [Bounded Arithmetic, Propositional Logic, and Complexity Theory](https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf) · [Parallelism and Adaptivity in Student-Teacher Witnessing](https://arxiv.org/abs/2602.19934) · [From Gödel incompleteness to the consistency of circuit lower bounds](https://arxiv.org/abs/2604.25251)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1097 — Unprovability of NP circuit upper bounds in \(T_{2}^{1}\)

Polynomial circuit upper bounds for NP would assert small nonuniform computations for nondeterministically verifiable problems. The saved question concerns whether such bounds are unprovable in \(T_{2}^{1}\). It studies limitations of a formal arithmetic theory rather than directly proving that the circuit upper bounds are false. A separation between truth and available formal proof would clarify which reasoning principles are needed for major complexity assertions. The inherited label does not preserve the exact upper-bound schema or metatheoretic assumptions, so the intended unprovability statement remains to be specified.

[Read in atlas](index.html#TCS-1097) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1098 — \(PV_{1}\) cannot verify any polynomial-time SAT solver

\(PV_{1}\) is an arithmetic theory organized around polynomial-time computation. The saved question asks whether it can verify the correctness of any polynomial-time SAT solver. The target would rule out formal correctness proofs in that theory, rather than by itself rule out the existence of such a solver. It links the provability of algorithmic claims to the theory's limited reasoning strength. The index does not state how solvers and their correctness are encoded or which assumptions support the proposed unprovability, so those details remain essential to the final formulation.

[Read in atlas](index.html#TCS-1098) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0071 — \(\mathrm{NC}^{0}\) proof systems

A propositional proof system maps proof strings to valid statements and must represent every statement in its target language. The saved entry studies systems computed by \(\mathrm{NC}^{0}\) circuit families. In this model, each output bit depends on only a constant number of input bits, imposing a severe local restriction. Characterizing what such systems can express would test how little computation proof verification or proof generation can use. The inherited label does not identify the target language or completeness convention, so the precise existence or separation question still needs its source formulation.

[Read in atlas](index.html#TCS-0071) · [Circuits, Logic and Games](https://doi.org/10.4230/DagRep.5.9.105)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1253 — Superpolynomial Res\([\oplus ]\) lower bounds

Resolution over parities allows proof lines to describe linear equations modulo two. The saved passage identifies superpolynomial lower bounds for this stronger resolution system as unresolved in its source. Parity reasoning can compress constraints that ordinary clauses express only indirectly. A general size lower bound would therefore push beyond limitations of weaker proof languages. The cited work connects this direction with range avoidance and proof-complexity generators, but the excerpt does not specify a hard formula family or establish that the source's historical status remains current.

[Read in atlas](index.html#TCS-1253) · [Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits](https://doi.org/10.4230/LIPIcs.ITCS.2026.111)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2889 — Short tree-like resolution from small proof space

The source compares working memory in refutations with the logarithm of minimum tree-like resolution size. Its two memory measures are stored clauses in resolution and distinct monomials in polynomial calculus with resolution. The comparison allows polynomial losses and powers of log n, so it is much coarser than a constant-factor identity. A length-penalized version of space is already known to satisfy the comparison. The unresolved issue is whether ordinary space can be substantially smaller on this scale.

[Read in atlas](index.html#TCS-2889) · [Space Characterizations of Complexity Measures and Size-Space Trade-Offs in Propositional Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.100) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-4982 — Does uniform randomized circuit learning imply P equals NP?

The premise asks for one efficient learner for all Boolean circuits when it may make membership queries. Accuracy is measured on uniformly random Boolean inputs, and the output may be any suitably small Boolean circuit. The learner is uniform and randomized, with explicit polynomial dependence on target size, error and confidence. The chosen conclusion is the deterministic class equality P equals NP. This fixes the uniformity choices in the source’s broader converse question without treating randomized or nonuniform conclusions as equivalent.

[Read in atlas](index.html#TCS-4982) · [Learning Algorithms Versus Automatability of Frege Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.101) · [Learning algorithms versus automatability of Frege systems — full author version](https://arxiv.org/abs/2111.10626) · [On Basing Lower-Bounds for Learning on Worst-Case Assumptions](https://www.wisdom.weizmann.ac.il/~bennyap/pubs/ABX08Full.pdf) · [Pseudorandomness and the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.ITCS.2020.68) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34) · [Learning algorithms versus automatability of Frege systems — journal version](https://doi.org/10.1142/S0219061325500023)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5114 — Lovász–Schrijver versus cutting planes

Lovász–Schrijver and cutting-planes systems are two ways to prove infeasibility through inequalities. The source asks whether the LS system polynomially simulates cutting planes. A simulation must translate every proof into an LS proof with size bounded by a polynomial in the original proof size. This would show that the two inequality-based reasoning frameworks are closer in strength than their different inference rules suggest. The source's version of LS and coefficient encoding must be retained, since changing those conventions can alter proof size and invalidate an otherwise plausible comparison.

[Read in atlas](index.html#TCS-5114) · [Representations of Monotone Boolean Functions by Linear Programs](https://doi.org/10.4230/LIPIcs.CCC.2017.3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5275 — Supercritical proof size–depth tradeoffs

Proof size counts the extent of a derivation, while depth measures the longest chain of dependent inferences. The source asks for a supercritical size-depth tradeoff even in a weaker system such as resolution. The target is to show that keeping one resource small forces the other far beyond what separate efficient proofs suggest. Such a construction would clarify limitations of branch-and-cut reasoning and simpler underlying proof methods. The saved excerpt does not define supercritical quantitatively or provide a formula family, so the precise tradeoff curve remains part of the source's model.

[Read in atlas](index.html#TCS-5275) · [On the Power and Limitations of Branch and Cut](https://doi.org/10.4230/LIPIcs.CCC.2021.6)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5292 — Optimal proof systems outside NP

The question asks whether any language outside NP has an optimal proof system. Each system is a polynomial-time algorithm that maps proofs to exactly the statements in its language. Optimality means that every competing system’s proofs can be matched with at most polynomial growth in length. A fast algorithm for translating proofs is a separate, stronger requirement. Recent oracle barriers and jump-operator results do not decide the ordinary existence question.

[Read in atlas](index.html#TCS-5292) · [Recursive Jump Operators and Optimal Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2026.88) · [Optimal Proof Systems for Complex Sets Are Hard to Find](https://doi.org/10.1145/3717823.3718182) · [Recursive Jump Operators and Optimal Proof Systems — full version](https://arxiv.org/abs/2606.01242)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5332 — Weak automatability of Resolution

The input is a CNF formula and a proof-length budget written in unary. The algorithm must distinguish satisfiable formulas from those having a short general Resolution refutation. The proof is not supplied, and the algorithm need not produce a Resolution proof. Unsatisfiable formulas whose shortest refutations exceed the budget can receive either answer. Known hardness for finding Resolution proofs does not settle this weaker recognition problem.

[Read in atlas](index.html#TCS-5332) · [Proof Complexity and Its Relations to SAT Solving (Invited Talk)](https://doi.org/10.4230/LIPIcs.STACS.2025.1) · [Regular resolution effectively simulates resolution](https://doi.org/10.1016/j.ipl.2024.106489) · [Automating Resolution is NP-Hard](https://arxiv.org/abs/1904.02991) · [The Proof Analysis Problem](https://arxiv.org/abs/2506.16956)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5333 — Linear-space Cutting Planes refutations

Cutting Planes refutes unsatisfiable Boolean formulas using linear inequalities and arithmetic inference. The saved question asks whether every unsatisfiable CNF has such a refutation using linear total space. Total space accounts for the information simultaneously stored, making coefficient encoding potentially relevant. An affirmative result would show that powerful arithmetic reasoning can always be carried out with modest memory, regardless of proof length. The excerpt does not define the reference input-size measure or coefficient accounting, so those conventions are still required before interpreting the linear bound precisely.

[Read in atlas](index.html#TCS-5333) · [The Space Complexity of Cutting Planes Refutations](https://doi.org/10.4230/LIPIcs.CCC.2015.433)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6759 — PSPACE-completeness of resolution space

Resolution clause space counts simultaneously retained clauses, whereas total space also reflects their sizes. The saved question asks whether deciding the corresponding bounded-space refutation problems is PSPACE-complete. A classification would separate memory needed to search for a space-efficient proof from memory used by the proof itself. The two measures can impose different constraints even on the same formula. The survey note records both decision questions historically, so a complete statement still needs the space-budget encoding and should not infer current completeness from the dated formulation alone.

[Read in atlas](index.html#TCS-6759) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6764 — Quadratic resolution space for linear-size CNFs

A fixed-width CNF has a constant bound on literals per clause. The saved question asks for linear-size unsatisfiable formulas of this kind that require quadratic total resolution space. Small input clauses would make the large simultaneous memory requirement arise from reasoning rather than a bloated starting representation. Such examples would give a strong separation between formula size and the storage demands of every refutation. The source note does not specify the indexing conventions for linear and quadratic growth, so these must be fixed consistently in a completed statement.

[Read in atlas](index.html#TCS-6764) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6766 — Polynomial resolution length from logarithmic clause space

Resolution clause space measures the maximum number of clauses kept at once. The saved question asks whether a logarithmic clause-space refutation guarantees the existence of a polynomial-length refutation. Low memory does not immediately rule out a long process that repeatedly recomputes discarded information. An affirmative implication would link two independently useful forms of proof efficiency. The source question concerns existence of a short proof and does not by itself require that the polynomial-length refutation also retain the original logarithmic space bound.

[Read in atlas](index.html#TCS-6766) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6767 — Resolution length–width tradeoffs

Resolution length counts inference steps, while width measures the largest clause used. The saved question asks for unavoidable tradeoffs between these resources, including tight lower bounds at prescribed width. A proof may save steps by using broad clauses that summarize many possibilities at once. Sharp tradeoffs would explain when restricting that expressive capacity necessarily makes reasoning much longer. The survey entry collects several quantitative directions rather than supplying one formula family and bound, so the working summary preserves the scope without choosing an unsupported tradeoff curve.

[Read in atlas](index.html#TCS-6767) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6770 — Cutting Planes versus polynomial-coefficient Cutting Planes

Cutting Planes reasons with integer linear inequalities, and its coefficients can encode large numerical information. The subsystem CP* restricts coefficients to the source's polynomial scale. The saved question asks whether unrestricted coefficients make the proof system strictly stronger. A separation would show that numerical magnitude provides an essential reasoning resource beyond the number of inequalities. The survey summary does not preserve whether strength is compared by proof size or efficient simulation, so the desired relation and coefficient bit-accounting remain necessary parts of the later statement.

[Read in atlas](index.html#TCS-6770) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6771 — Linear versus general resolution

Linear resolution restricts how successive resolution steps may depend on earlier clauses. General resolution permits a more flexible directed acyclic structure of reused deductions. The saved question asks whether the linear restriction yields a strictly weaker proof system. A separation would identify a genuine cost of forcing proofs into a more sequential form. The source summary does not reproduce the exact linear-resolution convention or simulation measure, so the working account cannot equate the question with tree-like resolution or a particular proof-length lower bound.

[Read in atlas](index.html#TCS-6771) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913)
Existing status: `source_open` · Summary written: 2026-09-11

## Communication complexity and Boolean function analysis (33)

### TCS-6603 — Log-rank conjecture

Alice and Bob must exactly evaluate a total Boolean function while each receives only one part of its input. The conjecture asks whether their minimum worst-case deterministic communication is bounded by one universal polynomial in logarithmic real matrix rank. The protocol may use arbitrary interaction and local computation, but all input pairs must be handled correctly. A refutation must defeat every universal polynomial, rather than a single proposed constant or exponent. Known square-root-rank upper bounds, nearly quadratic logarithmic lower bounds and signed-partition equivalences leave the central gap unresolved.

[Read in atlas](index.html#TCS-6603) · [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3) · [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9) · [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369) · [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6604 — Fourier Entropy–Influence conjecture

A scalar Boolean function has a Fourier spectrum whose squared coefficients form a probability distribution on sets of input coordinates. The Fourier Entropy–Influence conjecture asks whether its Shannon entropy is at most a universal constant times the expected size of a spectral set. Every dimension and every Boolean function are included, with uniform inputs, base-two entropy and exactly normalized bit-flip influence. A complete Lean-checked answer must prove the universal bound or show that the ratio is unbounded over nonconstant Boolean functions. The conjecture would imply fixed-accuracy Fourier concentration for DNF formulas, while weaker coordinate-entropy estimates and quantum counterexamples leave its classical target unsettled.

[Read in atlas](index.html#TCS-6604) · [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.cs.cmu.edu/~jswright/papers/fei.pdf) · [A new bound for the Fourier-Entropy-Influence conjecture](https://arxiv.org/abs/2312.08271) · [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246) · [Dense Hamiltonians at the Parseval Limit: The Noncommutative BH Constant is Exponential and the Quantum FEI Conjecture is False](https://arxiv.org/abs/2608.01424) · [A Note on the Entropy/Influence Conjecture](https://arxiv.org/abs/1105.2651) · [Strengthening Han’s Fourier Entropy-Influence Inequality via an Information-Theoretic Proof](https://arxiv.org/abs/2512.03117) · [Tightness of and counterexamples to several quantum estimates](https://arxiv.org/abs/2608.04411)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6605 — Aaronson–Ambainis conjecture

A bounded low-degree polynomial on the Boolean cube describes a real-valued function with controlled algebraic complexity. The Aaronson–Ambainis conjecture asks whether some variable has influence polynomially large in the variance and inverse degree. It predicts that meaningful variation cannot be distributed too evenly among all coordinates when the degree stays small. The question matters for understanding when quantum query behavior admits efficient classical simulation. The reviewed record stresses that results for random restrictions, bounded-round algorithms, or completely bounded norms impose additional structure and do not settle the unrestricted scalar-polynomial statement.

[Read in atlas](index.html#TCS-6605) · [The Need for Structure in Quantum Speedups](https://arxiv.org/abs/0911.0996) · [Quantum speedups need structure — withdrawn](https://arxiv.org/abs/1911.03748) · [Influence in Completely Bounded Block-Multilinear Forms and Classical Simulation of Quantum Algorithms](https://ir.cwi.nl/pub/31883/31883.pdf) · [Random Restrictions of Bounded Low Degree Polynomials Are Juntas](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17) · [Aaronson-Ambainis Conjecture Is True For Random Restrictions](https://eccc.weizmann.ac.il/report/2024/035/) · [Quantum Speedups Require Structure or Depth](https://arxiv.org/abs/2608.19158) · [Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms](https://arxiv.org/abs/2609.05201)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6581 — Mansour’s conjecture

A short DNF describes a Boolean function as a small collection of sufficient conditions for acceptance. Its Fourier representation describes the same function using correlations with parity functions. Mansour's conjecture asks whether almost all Fourier mass lies on a small set of coefficients whose size is controlled by the number of DNF terms and logarithmically scaled accuracy dependence in the exponent. This is a sparsity claim, so a bound on polynomial degree alone does not establish it. Proving the proposed concentration would connect two very different descriptions of Boolean functions and strengthen a central structural foundation for learning DNFs.

[Read in atlas](index.html#TCS-6581) · [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf) · [Mansour’s Conjecture is True for Random DNF Formulas](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/) · [Sharper bounds on the Fourier concentration of DNFs](https://arxiv.org/abs/2109.04525v2) · [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z) · [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246v2) · [Learning DNF through Generalized Fourier Representations](https://arxiv.org/abs/2506.01075v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6664 — Maximum influence of polynomial threshold functions

A polynomial threshold function takes the sign of a real polynomial on the Boolean cube. Total influence is the expected number of coordinate flips that change its output. The target is the largest possible influence as a joint function of dimension n and degree bound d, within universal constant factors. The asymptotic Gotsman–Linial conjecture gives a proposed upper scale, whereas a stronger exact-extremizer claim was disproved. The statement permits arbitrary realizing polynomials and does not prescribe a particular extremal construction.

[Read in atlas](index.html#TCS-6664) · [The Gotsman–Linial Conjecture is False](https://arxiv.org/abs/2108.02288) · [A Dual Perspective on Computational Complexity](https://dspace.mit.edu/server/api/core/bitstreams/7f2e32fd-d615-4dba-97be-f26cd30ca234/content) · [The Correct Exponent for the Gotsman–Linial Conjecture](https://arxiv.org/abs/1210.1283) · [On Graphs and the Gotsman–Linial Conjecture for \(d = 2\)](https://arxiv.org/abs/1709.06650) · [The Boolean surface area of polynomial threshold functions](https://arxiv.org/abs/2604.08095) · [Rational degree is polynomially related to degree](https://arxiv.org/abs/2601.08727)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7219 — Aanderaa–Karp–Rosenberg conjecture

An algorithm learns an unknown graph by asking whether individual pairs of vertices are edges. The conjecture asks whether every nonconstant monotone property invariant under vertex relabeling has some input requiring all possible pairs to be queried. Queries may be adaptive and all computation between them is free. The example of looking for one edge illustrates how an easy positive instance can coexist with an empty graph that requires a complete scan. The exact claim is known for prime-power vertex counts, while results about quantum queries, infinite graphs and broader topological symmetry must be distinguished from the full finite deterministic question.

[Read in atlas](index.html#TCS-7219) · [A topological approach to evasiveness](https://doi.org/10.1007/BF02579140) · [Elusive properties of countably infinite graphs](https://arxiv.org/abs/2503.11798v3) · [Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem](https://arxiv.org/abs/2010.12629v1) · [The topological evasiveness conjecture — CATA IV talk abstract](https://indico.sns.it/event/134/timetable/?print=1&view=standard_numbered) · [Publications — On the Topological Evasiveness Conjecture](https://www.math.miami.edu/~bruno/publications.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7352 — Real Grothendieck constant

The real Grothendieck constant compares the best vector assignment with the best sign assignment for a bilinear objective. The supremum ranges over every finite real matrix, so fixed-dimensional constants are different targets. The 2011 breakthrough disproved the proposed optimality of Krivine’s bound. A 2026 preprint reports further improvements while leaving a substantial interval. The benchmark requires a certified numerical estimate within absolute error 0.01.

[Read in atlas](index.html#TCS-7352) · [The Grothendieck constant is strictly smaller than Krivine’s bound](https://arxiv.org/abs/1103.6161) · [New Lower and Upper Bounds for the Grothendieck Constant](https://arxiv.org/abs/2608.11158)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6450 — Polynomial relation between classical and quantum communication

Two parties must evaluate a Boolean function when each holds one part of the input. The question asks whether randomized classical communication is polynomially bounded by quantum communication with shared entanglement for every total function. Both models allow bounded error on each input, and their costs count transmitted bits or qubits rather than local computation. A positive answer would limit quantum communication advantages whenever the function is defined on every input pair. The totality condition is central: results for promise problems cannot be substituted, and the polynomial must be universal across all finite domains.

[Read in atlas](index.html#TCS-6450) · [Quantum–Classical Equivalence for AND-Functions](https://eccc.weizmann.ac.il/report/2026/013/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6708 — Fourier Min-Entropy–Influence conjecture

The FMEI conjecture says that every Boolean function has a parity whose squared Fourier correlation is exponentially large in minus its total influence. Both influence and Fourier coefficients use the uniform distribution on the Boolean cube. One universal constant must cover every dimension and truth table, including constant and unbalanced functions. The conjecture is weaker than full Fourier entropy–influence and remains meaningful because of its connection to fundamental influence inequalities. Recent constructions force the universal constant to be at least four, while leaving the existence of any finite constant unresolved.

[Read in atlas](index.html#TCS-6708) · [Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386) · [Improved bounds on Fourier entropy and Min-entropy](https://eccc.weizmann.ac.il/report/2018/167/revision/1/download/) · [Improved Bounds on Fourier Entropy and Min-entropy](https://www.isical.ac.in/~sourav/papers/TOCT21.pdf) · [A Lower Bound on the Constant in the Fourier Min-Entropy/Influence Conjecture](https://eccc.weizmann.ac.il/report/2022/180/revision/1/download) · [A note on the FMEI of the Boolean functions in the Generalized Maiorana-McFarland construction](https://doi.org/10.1016/j.dam.2026.02.052) · [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6705 — Sharp low-degree Fourier weight of halfspaces

A halfspace is the sign of a weighted sum of input bits and a threshold. Its degree-zero and degree-one Fourier coefficients measure its mean and coordinate correlations. The question asks whether their squared weight is always at least \(2/\pi\). Majority functions approach that proposed universal constant as dimension grows. The exact inequality is retained because a general algorithm for merely approximating the extremal constant is already known.

[Read in atlas](index.html#TCS-6705) · [Analysis of Boolean Functions (updated author edition)](https://arxiv.org/abs/2105.10386) · [A robust Khintchine inequality, and algorithms for computing optimal constants in Fourier analysis and high-dimensional geometry](https://arxiv.org/abs/1207.2229) · [A Two-regime Khintchine Inequality and an Improved Bound on the Degree-1 Fourier Weight for Linear Threshold Functions](https://arxiv.org/abs/2608.27908)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2664 — Removing low-influence directions from convex sets

The problem concerns symmetric convex sets under standard Gaussian measure. A specified direction has small convex influence, measured by a normalized second-moment statistic. The conjecture asks whether the set is close to a symmetric convex cylinder that ignores this direction. The approximation error must tend to zero with influence independently of dimension. The exact zero-influence case is known, while the robust dimension-free statement remains the source’s Conjecture 2.

[Read in atlas](index.html#TCS-2664) · [Convex Influences](https://doi.org/10.4230/LIPIcs.ITCS.2022.53) · [Convex Influences — full version](https://arxiv.org/abs/2109.03107)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0220 — External Information and Amortized Expected Communication

Communication protocols reveal information about distributed inputs through their transcripts. This entry compares external information with amortized expected communication, linking what an observer learns to the cost of repeatedly performing a task. The central issue is whether many instances allow communication to be compressed toward the relevant information quantity. Understanding this relation would clarify when an information-theoretic lower bound accurately predicts operational communication cost. The saved record is only a topic label, so the source must provide the input distribution, error convention, and direction of the proposed relationship before a formal equality or separation is stated.

[Read in atlas](index.html#TCS-0220) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:76)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1047 — Formula size versus partition complexity

Boolean formula size measures computation by an expression tree, while partition complexity measures how a related communication space is divided into simpler pieces. The source asks about the relationship between these two quantities. A tight connection would explain whether an efficient static partition can be organized into an efficient hierarchical computation. The distinction matters because knowing that simple pieces exist need not provide a low-cost procedure for finding the appropriate piece. The saved index does not define the partition measure or desired bound, and the original book formulation is needed to specify the exact comparison.

[Read in atlas](index.html#TCS-1047) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1059 — Linearizing arbitrary depth-two circuits efficiently

The source considers depth-two circuits for a linear computational task and asks whether arbitrary circuits can be linearized efficiently. Linearization would replace possibly nonlinear intermediate behavior by a representation using the intended linear operations. The question tests whether leaving the linear model temporarily can provide substantial savings even when the final output is linear. Resolving it would help interpret lower bounds proved only for linear circuits. The abbreviated source record does not retain the coefficient field, gate basis, or allowable overhead, so those choices remain necessary before an exact simulation theorem can be proposed.

[Read in atlas](index.html#TCS-1059) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0540 — Communication Complexity of Max-Flow

Maximum flow measures how much a network can send between terminals under capacity and conservation constraints. The saved question studies its communication complexity. When different parts of the graph are held separately, computing the answer may require exchanging substantial structural information. A lower bound or efficient protocol could illuminate barriers relevant to distributed and dynamic graph computation. The inherited label does not define the partition of the input, number of parties, or exactness requirement, so it cannot support a particular communication bound.

[Read in atlas](index.html#TCS-0540) · [Dynamic Graph Algorithms](https://doi.org/10.4230/DagRep.12.11.45)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0053 — Sign-representation

A polynomial sign-represents a Boolean function when its positive and negative values give the function's outputs on the discrete input domain. The source considers sequences of integer polynomials containing only polynomially many monomials. It asks whether the same functions can always be represented while retaining that sparsity and also controlling the degrees. Sparse representation alone permits individual monomials with very large exponents. Understanding the relationship would clarify whether degree is an independent source of power in polynomial threshold descriptions or can be bounded without losing their compactness.

[Read in atlas](index.html#TCS-0053) · [Complexity of Symbolic and Numerical Problems](https://doi.org/10.4230/DagRep.5.6.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0218 — Cryptogenography

Cryptogenography studies communication in which someone wants to convey hidden information while concealing who originally knew it. The competing objectives are successful transmission and maintaining uncertainty about the informed participant. The saved entry points to an open problem in this model but does not retain its numerical or asymptotic target. This setting connects distributed protocols with anonymity through a precise adversarial inference task. A completed version must recover the number of participants, initial information distribution, observer powers, and success criterion, since changing any of these can alter the optimal protocol and the meaning of a bound.

[Read in atlas](index.html#TCS-0218) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:79)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0811 — Large zero rectangles in low-rank real matrices

The question concerns square real matrices with low rank and at least half their entries equal to zero. It asks for a Cartesian block consisting entirely of zeros whose area is a square-root-exponential fraction of the whole matrix. The constant in that guarantee must be the same for every matrix and dimension. The rank is over the real numbers, and entries may have arbitrary signs and magnitudes. Recent results establish related guarantees under additional entry restrictions, while the checked sources retain the general real-matrix question.

[Read in atlas](index.html#TCS-0811) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40) · [Disjoint pairs in set systems and combinatorics of low rank matrices](https://arxiv.org/abs/2411.13510v1) · [Extremal Combinatorics, Oberwolfach Report 42/2025](https://ems.press/content/serial-article-files/52246)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0464 — Information leakage in distributed OR

Two parties hold random bits and want to compute their OR while revealing as little as possible about their individual inputs. The selected problem asks for the minimum information that either participant must disclose during such a protocol. Some disclosure may be forced by the output itself, while additional leakage depends on the communication strategy. The source also asks how the optimum changes when the allowed number of rounds changes. Understanding this small example would clarify fundamental limits on information-efficient distributed computation before introducing more complicated functions or cryptographic assumptions.

[Read in atlas](index.html#TCS-0464) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1061 — Quadratic decision-tree bounds from block sensitivity

The target is a universal quadratic upper bound on deterministic decision-tree depth in terms of block sensitivity. A decision tree adaptively reads individual bits and must compute a total Boolean function correctly on every input. Block sensitivity counts disjoint blocks whose separate flips all change the value at one common input. The known general bound is cubic, while quadratic bounds hold for several restricted classes. The proposed constant must work for every function and dimension, and recent results on tree size or counts of minimal blocks do not settle this depth question.

[Read in atlas](index.html#TCS-1061) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Decision Tree Complexity Versus Block Sensitivity and Degree](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.27) · [Nearly Tight Bounds on the Block Number of Boolean Functions in Terms of Sensitivity](https://eccc.weizmann.ac.il/report/2026/010/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1540 — Influence lower bounds for noisy query complexity

Noisy query algorithms receive unreliable information when inspecting input bits. The source conjectures a lower bound of order \(I(f) \log  I(f)\) for every Boolean function, with \(I(f)\) denoting influence in its model. The proposed logarithmic factor would quantify the extra cost of overcoming noise for functions sensitive to many coordinates. It links an analytic property of the function to the number of observations needed for reliable computation. The saved passage does not preserve the noise rate, error guarantee, or influence convention, and those choices are essential when interpreting both the bound and small-influence edge cases.

[Read in atlas](index.html#TCS-1540) · [Tight Bounds for Noisy Computation of High-Influence Functions, Connectivity, and Threshold](https://proceedings.mlr.press/v291/gu25a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1845 — Complexity of truth-table decision-tree optimization

The problem tt-DT concerns decision-tree complexity when a Boolean function is supplied through its truth table. The saved question asks for the exact time complexity of this meta-computational task. The truth table makes all function values available but does not reveal the best adaptive query strategy directly. Determining the complexity would clarify how difficult it is to optimize a computation when its complete input-output behavior is explicit. The excerpt does not specify whether the task computes an optimum or decides a threshold, nor the requested precision of the running-time bound, so the source must supply those conventions.

[Read in atlas](index.html#TCS-1845) · [The Hardness of Decision Tree Complexity](https://doi.org/10.4230/LIPIcs.STACS.2025.66)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2571 — Communication characterization of nonmonotone Karchmer–Wigderson games

Karchmer–Wigderson games turn differences in Boolean function values into a communication search task. The cited work characterizes communication problems associated with proof systems and monotone circuits. The saved question asks for an analogous characterization covering non-monotone games. Such a description would connect richer circuit reasoning with an intrinsic class of total-search communication problems. The excerpt does not specify the reduction notion or the properties of the existing characterization, so those ingredients remain to be recovered before a precise equivalence can be stated.

[Read in atlas](index.html#TCS-2571) · [TFNP Characterizations of Proof Systems and Monotone Circuits](https://doi.org/10.4230/LIPIcs.ITCS.2023.30)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2658 — Sign-rank bounds from constant margin

A sign matrix can be represented by points and separating hyperplanes. Its margin measures how far every point stays from every relevant hyperplane after normalization. Its sign-rank is the smallest dimension of any representation with the correct signs. The question asks whether a fixed positive margin forces a dimension bound independent of matrix size. Recent work disproves a proposed Hamming-distance counterexample but explicitly leaves the general question open.

[Read in atlas](index.html#TCS-2658) · [Lower Bound Methods for Sign-Rank and Their Limitations](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2022.22) · [Sign-Rank of k-Hamming Distance is Constant](https://eccc.weizmann.ac.il/report/2025/060/) · [A \(Z_{2}\)–Topological Framework for Sign-rank Lower Bounds](https://eccc.weizmann.ac.il/report/2026/056/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3153 — Fourier rank versus sparsity

A Boolean function has a Fourier expansion in parity characters. Its sparsity counts nonzero coefficients, while its rank is the \(F_{2}\) dimension spanned by their index sets. The question asks whether rank can exceed the square root of sparsity by an unbounded factor. Known addressing examples attain the square-root scale, and the published universal upper bound allows an additional logarithmic factor. The answer requires either an asymptotically separating family or a universal square-root bound with an absolute constant.

[Read in atlas](index.html#TCS-3153) · [Tight Chang’s-Lemma-Type Bounds for Boolean Functions](https://doi.org/10.4230/LIPIcs.FSTTCS.2021.10) · [Fourier Sparsity and Dimension](https://theoryofcomputing.org/articles/v015a011/) · [Spectral Norm, Economical Sieve, and Linear Invariance Testing of Boolean Functions](https://doi.org/10.4230/LIPIcs.STACS.2026.30)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-4771 — Two-sided versus one-sided randomized communication

Randomized communication protocols may err on both outcomes, whereas one-sided-error protocols have a stronger correctness guarantee on one side. This question asks whether efficient two-sided-error communication for total functions can be reproduced using deterministic access to one-sided-error communication oracles. The source studies hierarchies formed by restricting the number of such oracle queries. Totality is essential because allowing promised inputs can change the separations. A characterization would explain whether general randomized interaction is assembled from simpler one-sided tests or possesses additional communication power.

[Read in atlas](index.html#TCS-4771) · [Nondeterministic and Randomized Boolean Hierarchies in Communication Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2020.92)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5189 — Approximating decision-tree complexity

Decision tree complexity measures the worst-case number of adaptive input queries needed to compute a function. The cited source asks about the complexity of approximating this quantity. An algorithm assessing complexity must reason about the best possible querying strategy, rather than simply execute one given tree. Approximation could provide useful estimates of intrinsic query cost even when exact optimization is difficult. The saved question does not fix the input representation or the permitted factor, so those choices are necessary before one can compare algorithms and hardness results meaningfully.

[Read in atlas](index.html#TCS-5189) · [The Hardness of Decision Tree Complexity](https://doi.org/10.4230/LIPIcs.STACS.2025.66)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5272 — Multiparty Clique lower bounds in compression games

A compression game lets computationally restricted players send information to a referee with unrestricted computation. The source studies constant-depth circuit restrictions and multiple rounds of interaction. The relevant conjecture proposes strong multiparty lower bounds for the Clique function. Such bounds would show that low communication cannot compensate for the players' limited computation. The project is significant because the source connects sufficiently strong compression-game hardness to separating NP from nonuniform logarithmic-depth circuits.

[Read in atlas](index.html#TCS-5272) · [Majority is Incompressible by \(\mathrm{AC}^{0}(p)\) Circuits](https://doi.org/10.4230/LIPIcs.CCC.2015.124)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5326 — Communication compression to information cost

A communication protocol can transmit many bits while revealing much less information about its participants' private inputs. The saved question asks whether the communication can always be compressed to the protocol's information cost. Such a transformation must preserve the relevant output behavior while coordinating participants who each know only their own input. A general compression theorem would connect information-based lower bounds to the actual communication required by multiparty computation. The excerpt does not specify the information measure, allowed error, or simulation overhead, and those choices are essential because several inequivalent compression questions fit the same informal sentence.

[Read in atlas](index.html#TCS-5326) · [Multi-Party Protocols, Information Complexity and Privacy](https://doi.org/10.4230/LIPIcs.MFCS.2016.57)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5892 — Constant-factor randomized direct sums for total Boolean functions

Alice and Bob must jointly compute a total Boolean function of their private inputs. The question compares the communication needed for one input pair with the communication needed for many pairs together. A single universal constant would force cost to grow proportionally with the number of copies. The protocol uses public randomness and must produce the entire answer vector correctly with probability at least two thirds on every input tuple. Recent claimed counterexamples for relations do not resolve the chosen total-function version.

[Read in atlas](index.html#TCS-5892) · [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50) · [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/) · [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6707 — Randomized query complexity of recursive majority-of-three

Recursive majority-of-three repeatedly applies a three-input majority gate in a tree. The question asks for its asymptotic randomized decision-tree complexity as the recursion grows. An algorithm can adapt its next query to observed values and use randomness to avoid reading subtrees whose outcomes no longer matter. The task therefore offers a concrete test of how recursion, adaptivity, and randomization interact in evaluating a simple formula. The source's error requirement and cost convention must be retained, since expected query cost and worst-case bounded-error complexity need not have the same asymptotic answer.

[Read in atlas](index.html#TCS-6707) · [Analysis of Boolean Functions (updated author edition)](https://arxiv.org/abs/2105.10386)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6710 — Number-on-forehead Disjointness complexity

Number-on-forehead communication gives each player access to all input blocks except the one associated with that player. The source asks for tight randomized communication bounds for set disjointness in this multiparty model. Overlapping knowledge makes the problem structurally different from the ordinary two-party split-input version. Matching bounds would clarify how the number of players affects the cost of detecting a common intersection. The saved note does not retain the player-count regime, error convention, or target precision, so the full book formulation is needed before proposing an asymptotic expression.

[Read in atlas](index.html#TCS-6710) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6711 — Deterministic communication versus monochromatic partition size

A deterministic protocol partitions a communication matrix into monochromatic regions corresponding to its transcripts. The source asks for the optimal gap between communication cost and the logarithm of the smallest monochromatic partition. A small partition provides a static decomposition but may not supply an efficient interactive method for locating the right piece. The gap measures precisely that additional organizational cost. The saved note requires the source's partition conventions and asymptotic parameterization, and bounds for covers or nondeterministic certificates should not be substituted for the disjoint partition measure.

[Read in atlas](index.html#TCS-6711) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

## Fine-grained complexity (27)

### TCS-6595 — Strong Exponential Time Hypothesis

SETH asks whether the optimal deterministic exponential rates for fixed-width satisfiability approach one as the allowed width grows. Every proposed constant saving from exhaustive search must fail at some fixed width. To refute it, one saving must work at every fixed width, although the algorithms and polynomial factors may vary with that width. Faster algorithms for width three, including recent randomized ones, do not meet that requirement. The hypothesis underlies many precise conditional lower bounds, including problems whose algorithms already run in polynomial time.

[Read in atlas](index.html#TCS-6595) · [On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [On some fine-grained questions in algorithms and complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6510 — Truly subcubic APSP

All-pairs shortest paths asks for the exact distance between every ordered pair of vertices in a weighted directed graph. The graph may contain negative edges but no negative cycle. The target is an algorithm with a fixed positive improvement over the cubic exponent in the specified comparison-addition model. Small subpolynomial savings do not meet that target. The question matters both as a basic graph optimization problem and as the organizing hypothesis behind many conditional running-time lower bounds.

[Read in atlas](index.html#TCS-6510) · [Subcubic Equivalences between Path, Matrix and Triangle Problems](https://doi.org/10.1109/FOCS.2010.67) · [Faster all-pairs shortest paths via circuit complexity](https://arxiv.org/abs/1312.6680) · [Node-Weighted Triangles: Faster and Simpler](https://arxiv.org/abs/2605.08588)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6596 — Orthogonal Vectors Hypothesis

Bichromatic Orthogonal Vectors asks whether two collections of binary vectors contain a pair with disjoint supports. The hypothesis excludes one fixed polynomial saving over quadratic time across all sufficiently large logarithmic dimension constants. Checking a pair is easy, but identifying a compatible pair among quadratically many possibilities is the bottleneck. Fine-grained reductions use this task to transfer precise barriers to geometric, string, and other algorithms. The saved review notes that subquadratic algorithms at each fixed small dimension are compatible with the hypothesis because their exponent savings can deteriorate as the dimension constant increases.

[Read in atlas](index.html#TCS-6596) · [More Applications of the Polynomial Method to Algorithm Design](https://theory.stanford.edu/~yuhch123/files/faster-orthog-soda.pdf) · [Conditional Hardness of Earth Mover Distance](https://arxiv.org/abs/1909.11068) · [Faster Algorithms for Average-Case Orthogonal Vectors and Closest Pair Problems](https://arxiv.org/abs/2410.22477) · [Faster Algorithms for k-Orthogonal Vectors in Low Dimension](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.85) · [New and Improved Concrete Lower Bounds for Orthogonal Vectors](https://arxiv.org/abs/2607.23799)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6597 — Algebraic k-Clique Hypothesis

For each fixed k, graph k-Clique asks whether k vertices are all pairwise adjacent. The reviewed hypothesis asks whether the leading coefficient of the optimal time exponent approaches the matrix-multiplication benchmark \(\omega /3\). Grouping a candidate clique into three parts connects detection to multiplication on auxiliary graphs. A lower exponent would change the foundation of many conditional optimality results for other computational tasks. The comparison uses the true matrix-multiplication exponent, so beating an old numerical upper bound or saving logarithmic factors does not by itself refute the hypothesis.

[Read in atlas](index.html#TCS-6597) · [Dynamic Boolean Formula Evaluation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2021.61) · [Faster Combinatorial k-Clique Algorithms](https://arxiv.org/abs/2401.13502v2) · [The Role of Regularity in (Hyper-)Clique Detection and Implications for Optimizing Boolean CSPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.78) · [Conditionally Tight Algorithms for Maximum k-Coverage and Partial k-Dominating Set via Arity-Reducing Hypercuts](https://arxiv.org/abs/2601.16923) · [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6661 — Hyperclique Hypothesis

A clique in an h-uniform hypergraph requires every h-element subset of its vertices to be a hyperedge. The hypothesis asserts that, for fixed h at least three and k greater than h, exhaustive k-tuple search admits no constant exponent saving. Higher-order compatibility cannot be verified merely by checking pairwise adjacency as in a graph. This conjectured barrier supports fine-grained lower bounds for optimization with higher-arity constraints. The saved review fixes randomized classical algorithms and dense inputs, while distinguishing genuine polynomial savings from logarithmic improvements or algorithms benefiting only from sparsity.

[Read in atlas](index.html#TCS-6661) · [The Role of Regularity in (Hyper-)Clique Detection and Implications for Optimizing Boolean CSPs](https://arxiv.org/abs/2505.17314) · [Tight Hardness for Shortest Cycles and Paths in Sparse Graphs](https://arxiv.org/abs/1712.08147) · [Classifying Identities: Subcubic Distributivity Checking and Hardness from Arithmetic Progression Detection](https://arxiv.org/abs/2603.28843) · [When Does Sparsity Help for k-Independent Set in Hypergraphs and Other Boolean CSPs?](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.94)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7179 — Truly subquadratic exact edit distance

Can exact edit distance between two length-n binary strings be computed in truly subquadratic time? Each insertion, deletion and substitution costs one, and the algorithm must always return the exact minimum. The requested deterministic worst-case bound has a fixed positive saving in the exponent of n. Known reductions rule out such an algorithm if SETH is true, but that hypothesis remains unproved. The 2026 approximation improvement has different accuracy and randomness guarantees.

[Read in atlas](index.html#TCS-7179) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348) · [Quadratic Conditional Lower Bounds for String Problems and Dynamic Time Warping](https://arxiv.org/abs/1502.01063v2) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6503 — Online matrix–vector multiplication conjecture

Online Boolean matrix-vector multiplication starts with a fixed Boolean matrix and then receives vectors individually. Each Boolean product must be returned before the next vector becomes available. The conjecture excludes a fixed polynomial improvement over cubic total time for a full sequence of vectors, including preprocessing. Batching the vectors into another matrix would violate the online requirement. Its importance comes from reductions that turn matrix queries into graph updates and thereby connect the conjecture to limits on dynamic algorithms.

[Read in atlas](index.html#TCS-6503) · [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://arxiv.org/abs/1511.06773) · [Faster Online Matrix-Vector Multiplication](https://arxiv.org/abs/1605.01695) · [Non-Boolean OMv: One More Reason to Believe Lower Bounds for Dynamic Problems](https://doi.org/10.4230/LIPIcs.ESA.2025.54)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6598 — Min-Plus Convolution Hypothesis

Min-plus convolution returns the minimum sum of two array entries for each possible sum of their indices. The input arrays contain polynomially bounded integers and need not be monotone. The question asks for a fixed improvement in the quadratic running-time exponent. Bounded-error randomization is allowed and every output entry must be correct simultaneously. Faster algorithms for monotone instances do not settle this unrestricted fine-grained barrier.

[Read in atlas](index.html#TCS-6598) · [Deterministic Monotone Min-Plus Product and Convolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119) · [Necklaces, Convolutions, and \(X+Y\)](https://tmc.web.engr.illinois.edu/convol.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0557 — Truly subquadratic algorithms for 3SUM

3SUM asks whether a value in one integer list is the sum of values from two other lists. The target is a fixed polynomial improvement over quadratic running time on a precisely specified word RAM. The selected variant allows every fixed polynomial integer universe and requires a common exponent saving. Randomization may change the running time but must never produce an incorrect answer. Known logarithmic savings and faster queries after preprocessing do not meet the from-scratch target.

[Read in atlas](index.html#TCS-0557) · [The Open Problems Project: 3SUM Hard Problems](https://topp.openproblem.net/p11) · [Higher Lower Bounds from the 3SUM Conjecture](https://arxiv.org/abs/1407.6756) · [Preprocessed 3SUM for Unknown Universes with Subquadratic Space](https://arxiv.org/abs/2602.11363)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6599 — Hitting Set conjecture

Two lists contain subsets of a logarithmic-size universe. The task is to find whether one supplied set in the first list intersects every set in the second. The conjecture rules out a single fixed polynomial improvement over quadratic time across all constant multiples of logarithmic dimension. The selected model permits randomization with bounded error and counts all word-RAM computation. Its existential–universal structure makes it useful for graph-radius and quantified-ordering lower bounds.

[Read in atlas](index.html#TCS-6599) · [The Fine-Grained Complexity of Multi-Dimensional Ordering Properties](https://doi.org/10.4230/LIPIcs.IPEC.2021.3) · [Approximation and Fixed Parameter Subquadratic Algorithms for Radius and Diameter in Sparse Graphs](https://theory.stanford.edu/~virgi/dirRad.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6944 — Min-Weight k-Clique hypothesis

The task finds a fixed-size clique minimizing the sum of its integer edge weights. The hypothesis says that no randomized algorithm saves a positive constant from the exponent k for the source’s full polynomial weight range. Its formal model charges uniform word-RAM computation and requires a correct complete answer with bounded error on every graph. A resolution would affect the fine-grained foundations of weighted graph, geometric and sequence optimization. The card preserves the fixed signed range and distinguishes newer conjectures whose weight exponent is quantified differently.

[Read in atlas](index.html#TCS-6944) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [More Consequences of Falsifying SETH and the Orthogonal Vectors Conjecture](https://www.mpi-inf.mpg.de/~kbringma/paper/2018STOC-1.pdf) · [Hardness of Dynamic Tree Edit Distance and Friends](https://drops.dagstuhl.de/doi/10.4230/LIPIcs.ITCS.2026.78)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7347 — Directed unweighted APSP below \(n^{5/2}\)

Directed unweighted all-pairs shortest paths asks for every ordered-pair distance when each arc has length one. The full distance matrix must be output explicitly. The question asks for a fixed exponent improvement below \(n^{5/2}\) with bounded-error randomization. The target makes no assumption about matrix multiplication or additive combinatorics. Recent conditional equivalences connect this barrier to other APSP hypotheses without resolving it.

[Read in atlas](index.html#TCS-7347) · [Algorithms, Reductions and Equivalences for Small Weight Variants of All-Pairs Shortest Paths](https://arxiv.org/abs/2102.06181) · [Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses](https://arxiv.org/abs/2603.27736)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7373 — Balanced dense NFA Acceptance Hypothesis

A binary word of length equal to the number of automaton states must be tested for acceptance. The automaton has quadratically many transitions and is supplied explicitly without preprocessing. The question excludes every fixed polynomial improvement over cubic running time for randomized word-RAM algorithms. The source relates a broader NFA Acceptance hypothesis to major static and dynamic complexity barriers. This card keeps the balanced dense binary specialization separate from sparse-automaton results and from simulation-density bounds for regular expressions.

[Read in atlas](index.html#TCS-7373) · [The NFA Acceptance Hypothesis: Non-Combinatorial and Dynamic Lower Bounds](https://theoretics.episciences.org/14397) · [Sparse Regular Expression Matching](https://arxiv.org/abs/1907.04752v7)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0562 — Refuting nondeterministic SETH

Nondeterministic SETH strengthens a satisfiability-based time barrier by allowing a nondeterministic form of computation in its formulation. The recorded question asks how to refute that hypothesis. A nondeterministic certificate can change the cost of establishing an unsatisfiability-type conclusion relative to ordinary deterministic search. A refutation would illuminate barriers to proving some fine-grained reductions from standard satisfiability assumptions. The saved title does not reproduce the exact complement convention or time quantifiers, so those definitions must be recovered before one particular nondeterministic algorithm is claimed to meet the target.

[Read in atlas](index.html#TCS-0562) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/finegrain.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0560 — Fine-grained reductions from Hitting Set to 3SUM

The source asks for a fine-grained reduction from a Hitting Set problem to 3SUM. The intended connection would translate a sufficiently fast three-number sum algorithm into progress on the source's quantified set-intersection task. Encoding many set interactions as arithmetic equalities must avoid a blowup that erases the desired time saving. Such a reduction could connect two currently distinct foundations for conditional algorithmic lower bounds. The saved entry does not specify numeric ranges or reduction overhead, so its target is stronger than merely expressing Hitting Set as some polynomial-size 3SUM instance.

[Read in atlas](index.html#TCS-0560) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/finegrain.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0815 — Relation between permanent computation and SETH

The permanent sums products of matrix entries over all permutations and is a central exact counting quantity. The saved question asks how its computation relates to the Strong Exponential Time Hypothesis. The intended connection concerns quantitative running-time limits, rather than just ordinary polynomial-time reductions. Establishing a sufficiently efficient reduction could translate improved permanent algorithms into consequences for satisfiability, or explain why that transfer fails. The index does not specify matrix entries, arithmetic model, or reduction direction, all of which are needed before asserting an exact exponential barrier.

[Read in atlas](index.html#TCS-0815) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0761 — Time exponents for multiple-string LCS over fixed alphabets

Multiple-string LCS finds a longest string that occurs as a subsequence of every input. The target is the optimal deterministic time exponent for every fixed alphabet size and fixed number of strings. It makes the source’s question about a fractional exponent saving into an explicitly broader quantitative function. Resolving the function would identify how alphabet size changes the computational cost of coordinating many sequences. Acceptance requires a Lean-certified error of at most one hundredth at every parameter pair, while retaining the source question separately.

[Read in atlas](index.html#TCS-0761) · [Randomization in Parameterized Complexity (Dagstuhl Seminar 17041)](https://doi.org/10.4230/DagRep.7.1.103) · [Tight Hardness Results for LCS and other Sequence Similarity Measures](https://theory.stanford.edu/~virgi/LCS.pdf) · [Exploring the Gap Between LCS and LCStr](https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.27/LIPIcs.CPM.2026.27.html)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5422 — Consequences of linear-time Orthogonal Vectors

Orthogonal Vectors asks whether two Boolean vector collections contain a pair with no coordinate where both vectors have a one. The selected question concerns an essentially linear-time algorithm for this problem in the source's setting. It asks whether the existence of such an algorithm would refute the Exponential Time Hypothesis. Known connections to the stronger SETH assumption do not automatically establish that implication. Proving it would ground a basic fine-grained lower bound in a weaker assumption and clarify the role of limited nondeterminism in polynomial-time hardness.

[Read in atlas](index.html#TCS-5422) · [Superlinear Lower Bounds Based on ETH](https://doi.org/10.4230/LIPIcs.STACS.2022.55)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6025 — Treewidth-dependent classification of subgraph isomorphism

Subgraph isomorphism has general algorithms whose exponent depends on the pattern's treewidth. The source exhibits patterns for which that dependence is conditionally optimal. It asks for a classification of maximally hard pattern families and, conversely, whether some unbounded-treewidth families admit sublinear-in-treewidth exponents. Known clique-like exceptions show that treewidth alone need not determine the exact exponent. The project seeks finer structural invariants explaining when a pattern supports algorithmic shortcuts and when it forces the full generic search complexity.

[Read in atlas](index.html#TCS-6025) · [Current Algorithms for Detecting Subgraphs of Bounded Treewidth Are Probably Optimal](https://doi.org/10.4230/LIPIcs.ICALP.2021.40)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6935 — Randomized Strong Exponential Time Hypothesis

Randomized SETH asks whether bounded-width satisfiability resists every uniform fixed saving in the exhaustive-search exponent. For each positive \(\varepsilon\), the conjecture requires some fixed width k with no randomized \(O(2^{(1- \varepsilon )n})\) algorithm. The width may grow as the demanded saving shrinks, so fast algorithms at individual small widths remain compatible. This randomized version supports lower bounds that must exclude randomized algorithms for their target tasks. The saved textbook note does not spell out error and polynomial input-length factors, and deterministic SETH alone cannot silently supply the stronger randomized exclusion.

[Read in atlas](index.html#TCS-6935) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6937 — Randomized APSP hypothesis

All-pairs shortest paths computes the shortest-path distance between every ordered pair of graph vertices. The source conjectures that weighted instances admit no randomized algorithm with a fixed polynomial saving over cubic time. Weights make combining candidate paths a min-plus computation rather than ordinary Boolean reachability. The hypothesis underlies many fine-grained barriers for dynamic programming, distance problems, and related optimization. The saved note refers to a specific integer-weight regime without reproducing it, so numeric magnitude, negative-cycle conventions, and the machine model must be restored before the conjecture is fully quantified.

[Read in atlas](index.html#TCS-6937) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6940 — Tree edit distance versus APSP

Tree edit distance measures the cheapest sequence of permitted edits transforming one labeled tree into another. The source asks whether its fine-grained complexity is equivalent to all-pairs shortest paths. Both tasks can involve expensive combinations of many partial solutions despite very different input structures. An equivalence would explain whether a sufficiently fast algorithm for either problem necessarily improves the other. The saved note does not specify ordered versus unordered trees, edit costs, or reduction exponents, so a generic polynomial reduction does not establish the desired relationship.

[Read in atlas](index.html#TCS-6940) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6942 — Hitting Set hardness from Orthogonal Vectors

Orthogonal Vectors searches for a disjoint pair across two set families, while Hitting Set asks for one set intersecting every set in the other family. The source asks whether the former hypothesis implies the latter. Their different quantifier patterns make the connection subtler than complementing one pairwise intersection test. An implication would reduce the number of independent assumptions needed for fine-grained lower bounds. The saved question must be interpreted with matching universe dimensions, randomized guarantees, and exponent conventions, since a reduction losing too much time would not transfer the hypothesized barrier.

[Read in atlas](index.html#TCS-6942) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6945 — Exact-Weight k-Clique hypothesis

Exact-Weight k-Clique asks for a clique whose edge weights add to a prescribed target. The source conjectures that randomized algorithms require an exponent approaching k in the stated weight regime. Exact cancellation among weights introduces a numerical constraint beyond the clique's pairwise adjacency conditions. A sharp barrier would support quantitative hardness transfers to problems combining structural and arithmetic requirements. The saved note does not specify weight magnitude or target encoding, and finding a minimum-weight clique is a related but distinct task whose reductions must preserve those numeric parameters.

[Read in atlas](index.html#TCS-6945) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6946 — Fine-grained relationship between APSP and 3SUM

All-pairs shortest paths and 3SUM are central hypotheses for different families of fine-grained lower bounds. The source asks for a clearer relationship between their computational difficulties. One concerns many path minima, while the other searches for one exact arithmetic relation among three inputs. A suitable reduction could transfer a fixed exponent saving and consolidate barriers now supported by separate assumptions. The saved formulation leaves the direction and resource-preservation target open, so a complete question must select the integer or real model and the precise runtime implication sought.

[Read in atlas](index.html#TCS-6946) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6949 — Exhaustive-search lower bounds for Circuit-SAT

Circuit-SAT asks whether a Boolean circuit outputs one on some assignment to its n inputs. The source proposes near-exhaustive-search hardness for richer representations, especially polynomial-size circuits of polylogarithmic depth. These circuits can express computations more compactly than bounded-width CNF formulas. A hypothesis at this representation level can support stronger or differently structured fine-grained reductions. The saved note does not list every circuit class or algorithmic randomness convention, so the conjecture should not be conflated with ordinary SETH or treated as one identical statement across all succinct representations.

[Read in atlas](index.html#TCS-6949) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6950 — Disjunction of SETH, APSP and 3SUM hypotheses

SETH, the APSP hypothesis, and the 3SUM hypothesis assert precise barriers for three different computational tasks. The source asks whether at least one of these hypotheses must be true. This disjunction is weaker than proving any particular member, because it permits the others to fail. A proof would give a robust foundation for results whose conditional hardness follows from whichever barrier survives. The saved historical formulation still depends on the exact machine, numeric, and randomness conventions of its three constituents, so mixing incompatible versions would change the proposition.

[Read in atlas](index.html#TCS-6950) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/)
Existing status: `source_open` · Summary written: 2026-09-11

## Pseudorandomness and derandomization (42)

### TCS-0003 — P versus BPP

BPP contains decision problems solvable in polynomial time using random bits with bounded error on every input. The question asks whether every such problem also has a deterministic polynomial-time algorithm, giving \(\mathrm{P}=\mathrm{BPP}\). Trying every random tape removes error but generally takes exponential time. A positive answer would show that randomness changes algorithm design without enlarging this class of efficiently decidable problems. The saved review explains conditional routes through strong circuit lower bounds and distinguishes uniform algorithms from advice strings that merely exist for each input length.

[Read in atlas](index.html#TCS-0003) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [\(\mathrm{P}=\mathrm{BPP}\) unless E has sub-exponential circuits: Derandomizing the XOR Lemma](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/IW97/proc.pdf) · [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](https://eccc.weizmann.ac.il/report/2026/082/) · [Probabilistic Computers (and Hence Quantum Computers) Are Rigorously More Powerful Than Classical Deterministic Computers, and Derandomization](https://arxiv.org/abs/2308.09549v9)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6600 — Optimal explicit pseudorandom generators for read-once branching programs

An ordered read-once branching program processes input bits sequentially while retaining only one of a bounded number of states. The target is an explicit pseudorandom generator with seed length \(O(\log  n+\log  w+\log (1/\varepsilon ))\). One generated distribution must approximate acceptance probabilities for every length-n, width-w program without inspecting that program. Such a generator would provide a strong route to removing randomness from logarithmic-space computation. The saved review stresses that weighted pseudodistributions, hitting sets, and generators for permutation programs do not directly supply the ordinary distribution required for arbitrary merging transitions.

[Read in atlas](index.html#TCS-6600) · [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf) · [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28) · [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/) · [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://epubs.siam.org/doi/10.1137/1.9781611978971.124) · [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/) · [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0026 — L versus BPL

BPL permits bounded-error randomized decisions using logarithmic work space and polynomial time. The question asks whether every such language has a deterministic logarithmic-space decider. Random bits are fresh independent coin outcomes, and remembering them consumes counted work space. Known deterministic simulations and recent weighted-generator improvements still use more space or establish different parameter guarantees. The completed card keeps this class-equality target separate from constructing a particular optimal pseudorandom generator.

[Read in atlas](index.html#TCS-0026) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf) · [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6662 — Optimal deterministic restricted-isometry matrices

A restricted-isometry matrix approximately preserves the Euclidean length of every sparse vector. The reviewed question asks for deterministic polynomial-time construction with \(O(s \log (eN/s))\) rows and fixed distortion. Random matrices achieve this row order, but a usable deterministic construction must control every sparse support simultaneously. Optimal explicit matrices would provide guaranteed measurement designs for compressed sensing without random setup choices. The saved review identifies the limitations of pairwise coherence analyses and notes that reduced randomness or success on typical signals does not establish the requested all-signal guarantee.

[Read in atlas](index.html#TCS-6662) · [Doubly transitive equiangular tight frames that contain regular simplices](https://www.sciencedirect.com/science/article/pii/S0024379525003143) · [The road to deterministic matrices with the restricted isometry property](https://www.math.ucdavis.edu/~strohmer/courses/270/road_to_rip.pdf) · [Explicit constructions of RIP matrices and related problems](https://arxiv.org/abs/1008.4535) · [Satisfying the restricted isometry property with the optimal number of rows and slightly less randomness](https://arxiv.org/abs/2311.07889)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1005 — Unconditional subexponential simulation of BPP

BPP contains decision problems solved efficiently using random bits with bounded error on every input. The question asks whether all of them have exact deterministic simulations in the class SUBEXP. Here SUBEXP requires a simulation in time two to the n-to-epsilon power for every fixed positive epsilon. The simulator may depend on the chosen exponent, but it must work on every input without advice or assumptions. Known general brute-force simulations take larger exponential time, while stronger derandomization theorems rely on unproved hardness.

[Read in atlas](index.html#TCS-1005) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1018 — Linear-seed hardness-to-randomness sampling

A hard Boolean function can provide pseudorandom bits by being evaluated at carefully correlated inputs. The question asks for a uniform sampler using only a constant multiple of one input length as its random seed. It must produce polynomially many bits in the hardness parameter, each from exactly one evaluation of the original function. Every function with the specified average-case circuit hardness must yield a generator fooling the stated circuits to inverse-output-length error. General short-seed transformations and newer results under stronger hardness assumptions do not automatically preserve this required evaluation form.

[Read in atlas](index.html#TCS-1018) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Nearly Optimal Pseudorandomness from Hardness](https://doi.org/10.1145/3555307)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1015 — Seeded extraction with constant total entropy loss

A seeded extractor combines an arbitrary weak random source with a short independent uniform seed. This question asks for logarithmic seed length and an output losing at most a constant number of the combined available entropy bits. The statistical error is fixed at one hundredth for every source meeting the min-entropy bound. The entire family must be evaluated by one deterministic polynomial-time algorithm, including any preprocessing. Nonconstructive existence and recent faster constant-fraction extractors leave this specific combination of parameters unsettled in the checked sources.

[Read in atlas](index.html#TCS-1015) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Nearly-Linear Time Seeded Extractors with Short Seeds](https://arxiv.org/abs/2411.07473v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1016 — Extraction with log n plus constant seed length

This question asks how close an efficiently computable extractor can get to the minimum useful seed length. It requires at most the base-two logarithm of the source length plus a constant number of seed bits. The output must contain a fixed positive fraction of the source entropy and have statistical error at most one hundredth. One deterministic polynomial-time family must meet these guarantees for every source length and entropy threshold. Known constructions in the checked sources optimize related parameters but do not supply this full combination.

[Read in atlas](index.html#TCS-1016) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Nearly Optimal Pseudorandomness from Hardness](https://doi.org/10.1145/3555307) · [Nearly-Linear Time Seeded Extractors with Short Seeds](https://arxiv.org/abs/2411.07473v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1006 — Universal determinant evaluations for bipartite matching

The determinant test for a bipartite graph succeeds when its edge variables receive suitable integer values. This question asks for one fixed table of values that succeeds simultaneously for every graph of the same size. The complete table must be constructed by uniform polynomial-size circuits of polylogarithmic depth. A probabilistic argument proves such tables exist, but does not compute them with that resource bound. A new 2026 preprint claims an NC matching algorithm using a different block-matrix test, so its scope is distinguished from this universal-table requirement.

[Read in atlas](index.html#TCS-1006) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Bipartite Perfect Matching is in quasi-NC](https://arxiv.org/abs/1601.06319) · [Bipartite Matching is in NC](https://eccc.weizmann.ac.il/report/2026/100/revision/2/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1021 — Promise-BPP derandomization implying EXP circuit hardness

Derandomization replaces efficient bounded-error randomized algorithms by deterministic ones. The question assumes this replacement for promise problems and asks whether it forces an exponential-time language to lack polynomial-size Boolean circuits. Known implications involving nondeterministic exponential time do not establish the deterministic-class target. The issue is a converse to hardness-based pseudorandomness constructions. The project seeks to explain whether eliminating randomness necessarily reveals an explicit source of circuit hardness at the corresponding deterministic computational scale.

[Read in atlas](index.html#TCS-1021) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1022 — Derandomization implying exponential nondeterministic circuit hardness

The source studies what circuit lower bounds follow if every promise-BPP problem can be derandomized. This question asks for a nondeterministic exponential-time problem requiring circuits of size exponential in a positive power of the input length. Merely proving a superpolynomial lower bound does not meet that quantitative target. The circuit designs are nonuniform, so they need not be efficiently generated. The project seeks a stronger converse to the principle that hard functions can supply pseudorandomness for efficient algorithms.

[Read in atlas](index.html#TCS-1022) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1125 — Sub-log-squared seeds for width-four ordered branching programs

Width-four ordered branching programs read bits in sequence while remembering only one of four states. The saved source asks for pseudorandom generators with seed length below the log-squared scale. Even this very small state space can repeatedly combine and discard information from earlier bits. An improvement would test whether general space-bounded pseudorandomness barriers already occur at constant width. The entry does not state the error dependence or explicitness convention, so a claimed shorter seed must be evaluated in the same length and accuracy regime as the cited source.

[Read in atlas](index.html#TCS-1125) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1133 — Sub-log-squared seeds for polynomial-size CNFs and DNFs

CNFs and DNFs combine clauses or terms through two layers of Boolean operations. The source asks for pseudorandom generators with sub-log-squared seed length that fool polynomial-size formulas of these types. A generator must preserve acceptance probabilities across many overlapping clauses despite using far fewer random bits. Improving the seed would sharpen derandomization for basic Boolean tests and reduce exhaustive seed-enumeration costs. The saved title does not specify the allowed formula size exponent or error, so these dependencies remain necessary before the quantitative target is fully defined.

[Read in atlas](index.html#TCS-1133) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1014 — Lossless condensers with constant output overhead

A lossless condenser compresses a weak random source while preserving its guaranteed entropy together with the seed entropy. This question asks for a logarithmic seed and an output only a constant number of bits longer than that preserved entropy. The output may be nonuniform, but it must be within one hundredth in statistical distance of a distribution with the required min-entropy. The equivalent graph target has nearly lossless expansion and only a constant factor more right vertices than the number of outgoing edges from a source set. Recent multiplicity-code and two-sided-expansion results improve related structure without meeting this constant-overhead target.

[Read in atlas](index.html#TCS-1014) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Unbalanced Expanders from Multiplicity Codes](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2022.12) · [Two-Sided Lossless Expanders in the Unbalanced Setting](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.34)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1024 — Extracting from low-entropy efficiently samplable sources

An efficiently samplable source is a distribution produced by a small circuit, potentially with far less entropy than its output length. The textbook asks for extraction from such sources at low entropy or negligible error under plausible assumptions. The sampler's computational structure offers a restriction beyond merely knowing the amount of entropy. Using that structure could enable extraction in regimes impossible for completely arbitrary single sources. The saved note does not identify the permitted assumptions or extractor access to the sampler, so neither unconditional extraction nor a specific low-entropy threshold is asserted here.

[Read in atlas](index.html#TCS-1024) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0854 — Promise-ZPP versus Promise-BPP derandomization

Promise-ZPP permits zero-error randomized computation on promised inputs, whereas Promise-BPP allows a bounded probability of error. The recorded question asks whether derandomizing the former would also derandomize the latter. A promise leaves some inputs outside the required correctness domain, affecting how reductions and simulations compose. A positive implication would connect two seemingly different routes to eliminating randomness. The source title alone does not state the precise deterministic promise class or simulation overhead, so these details must be retained from the original formulation rather than borrowed from total-language equalities.

[Read in atlas](index.html#TCS-0854) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/LUCA/luca.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1135 — Promise-AM derandomization via targeted hitting sets

The question compares promise-Arthur–Merlin derandomization with the existence of targeted hitting sets. A generator receives a co-nondeterministic circuit and must hit its accepting ordinary inputs whenever they occupy at least half the domain. Nondeterministic generation must always have a successful branch, and every successful output must satisfy the required hitting guarantee. The source asks whether eliminating public randomness is equivalent to a uniform polynomial-time generator of this kind. The checked 2025 journal result establishes a weaker connection involving different time, advice and input-length guarantees.

[Read in atlas](index.html#TCS-1135) · [New ways of studying the \(\mathrm{BPP}=\mathrm P\) conjecture](https://eccc.weizmann.ac.il/report/2023/094/) · [Instance-Wise Hardness and Refutation versus Derandomization for Arthur-Merlin Protocols](https://pages.cs.wisc.edu/~dieter/Papers/r-am-instance-wise-cc.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1137 — Derandomization from almost-everywhere uniform hardness

Hardness-based derandomization constructs useful pseudorandomness from functions that resist efficient computation. The source asks for derandomization from almost-everywhere uniform hardness. Uniform hardness concerns algorithms rather than arbitrary circuit families, while almost-everywhere hardness restricts exceptions across input lengths. A result from this premise could clarify which kinds of computational difficulty are sufficient to remove randomness. The saved title gives no hardness rate or target simulation class, so a complete version must specify both before comparing this premise with stronger nonuniform assumptions.

[Read in atlas](index.html#TCS-1137) · [New ways of studying the \(\mathrm{BPP} = \mathrm{P}\) conjecture](https://eccc.weizmann.ac.il/report/2023/094/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0987 — Deterministic Heavy-Hitters & Fast Matrix Algorithms

A restricted-isometry matrix approximately preserves the Euclidean lengths of all sparse vectors. The source seeks deterministic or certifiably correct constructions with nearly linear dependence on sparsity in their row count. It also asks whether suitably chosen rows of Fourier or other bounded-entry unitary matrices can achieve the desired bounds. A related computational obstacle is multiplying a selected Fourier submatrix by a vector faster than the straightforward quadratic method. These questions connect explicit measurement design with the recovery time needed by deterministic heavy-hitter and sparse-reconstruction algorithms.

[Read in atlas](index.html#TCS-0987) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1008 — Bipartite vertex expanders with constant expansion loss

A bipartite vertex expander sends every sufficiently small set of left vertices to many distinct right neighbors. The textbook asks for explicit balanced constructions with expansion \(D- O(1)\), where D is the degree. This means only a constant amount of expansion is lost relative to the maximum D neighbors per vertex. Such graphs provide highly efficient spreading and sampling structures from bounded local connectivity. The saved note omits the range of sets that must expand and the explicitness requirement, so these must be restored before the additive-loss target becomes a complete construction specification.

[Read in atlas](index.html#TCS-1008) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1009 — Near-lossless undirected constant-degree vertex expanders

Undirected vertex expanders require small sets of vertices to reach many neighbors through constant-degree edges. The saved question seeks explicit expansion arbitrarily close to the degree D. An undirected edge participates in both endpoints' neighborhoods, creating dependencies absent from a freely designed bipartite incidence pattern. Near-lossless expansion would give exceptionally efficient combinatorial spreading with a symmetric local graph structure. The historical note does not specify whether neighborhoods include the original set or the admissible set sizes, and these conventions matter for interpreting the claimed proximity to D.

[Read in atlas](index.html#TCS-1009) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1013 — Optimal-size highly unbalanced lossless expanders

A highly unbalanced expander has a large left side and a much smaller right side while spreading small left subsets broadly. The source asks for near-lossless explicit constructions with optimal size and polylogarithmic degree. The right side acts like a compressed range that must still distinguish many choices from each small input set. Achieving the desired parameters would strengthen lossless condensers and other ways of processing weak randomness. The saved note links these viewpoints but does not reproduce the exact right-side size, expansion error, or subset range defining optimality.

[Read in atlas](index.html#TCS-1013) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1124 — Optimal PRGs for high-dimensional combinatorial rectangles

A combinatorial rectangle tests whether each coordinate falls inside a chosen subset of its alphabet. The recorded problem asks for optimal pseudorandom generators when the number of coordinates is large. Coordinate-wise simplicity does not remove the challenge of preserving probabilities for every combination of allowed subsets. An efficient optimal generator would support derandomization of tests that factor across many independent-looking coordinates. The source title does not specify alphabet sizes, error, or the desired seed formula, so these parameters must be recovered before one quantitative meaning of optimality is selected.

[Read in atlas](index.html#TCS-1124) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1019 — Polynomial-time derandomization of randomized \(\mathrm{AC}^0\)

The question asks whether randomness can be removed from uniform shallow AND–OR computations using deterministic polynomial time. Each randomized circuit must answer correctly with probability at least two thirds on every input. A single polynomial-time procedure constructs the family’s circuit descriptions from the input length. The deterministic simulator may use arbitrary polynomial-time computation and need not remain a constant-depth circuit. Quasipolynomial simulation, correctness on most inputs and nonuniform deterministic circuits do not meet the full target.

[Read in atlas](index.html#TCS-1019) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [Weak derandomization of weak algorithms: explicit versions of Yao’s lemma](https://www.cs.haifa.ac.il/~ronen/online_papers/YaoLemma.pdf) · [Improved Pseudorandom Generators for \(\mathrm{AC}^0\) Circuits](https://doi.org/10.4230/LIPIcs.CCC.2022.34)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1122 — Nontrivial PRGs for logarithmic-degree binary polynomials

A binary polynomial evaluates input bits using arithmetic over the two-element field. The source asks for nontrivial pseudorandom generators fooling polynomials whose degree grows logarithmically with input length. As degree increases, these tests can detect increasingly intricate correlations among generated bits. A generator saving a meaningful amount of randomness would extend algebraic pseudorandomness beyond much simpler parity tests. The saved title does not quantify nontrivial seed length, degree constants, or error, so these remain required choices before this becomes a precise construction benchmark.

[Read in atlas](index.html#TCS-1122) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1131 — Sublinear-seed generators for AC0 with parity gates

AC0 with parity gates permits shallow circuits to combine ordinary Boolean operations with parity tests. The source asks for pseudorandom generators using a sublinear number of truly random bits. Parity operations can detect correlations that generators for plain AND–OR circuits may fail to hide. A sublinear seed would establish a meaningful unconditional randomness saving for this richer circuit class. The saved title omits the size, depth, and error regime, and these restrictions determine whether a proposed construction actually fools every circuit covered by the question.

[Read in atlas](index.html#TCS-1131) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1007 — Universal traversal sequences under arbitrary labels

A universal traversal sequence is one list of absolute local port numbers that visits every vertex of every graph of a specified size and degree. The graph may have parallel edges and self-loops, and its local port labels are arbitrary. The question asks for a deterministic polynomial-time constructor given only the size and degree parameters. Short sequences are known to exist, but incoming-port-based exploration and polynomial cover time with expensive local computation are different guarantees. An efficient construction would remove randomness from graph-independent traversal under severely restricted information.

[Read in atlas](index.html#TCS-1007) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Self-stabilizing Graph Exploration by a Single Agent](https://arxiv.org/abs/2010.08929v4) · [Self-stabilizing graph exploration by a single agent](https://doi.org/10.1016/j.tcs.2026.116085)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1956 — Super-bits from demi-bits

The source studies demi-bits and super-bits as forms of pseudorandomness secure against nondeterministic tests. It asks whether the existence of a demi-bit implies the existence of a super-bit. These notions distinguish different ways that nondeterministic computation might detect a generator's outputs. An implication would unify two candidate primitives and could transfer construction consequences between their security models. The saved question does not reproduce either definition, so ordinary cryptographic one-way bits cannot be substituted for them or used to infer the direction's difficulty without the original conventions.

[Read in atlas](index.html#TCS-1956) · [Stretching Demi-Bits and Nondeterministic-Secure Pseudorandomness](https://doi.org/10.4230/LIPIcs.ITCS.2024.95)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2201 — Non-malleable extractors from standard extractors

A standard extractor turns weak randomness into near-uniform bits under its source assumptions. The cited question asks whether standard extractors can also be used to construct non-malleable extractors. Non-malleability requires output to remain useful even when an adversary creates related, tampered inputs or seeds. A general transformation would connect an established randomness primitive to the stronger guarantees needed in adversarial settings. The saved sentence does not fix the source or tampering model, so the two-source and affine variants named by the paper must be distinguished when stating an actual reduction.

[Read in atlas](index.html#TCS-2201) · [Two-Source and Affine Non-Malleable Extractors for Small Entropy](https://doi.org/10.4230/LIPIcs.ICALP.2024.108)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3958 — Pseudorandom generators for superlinear-size depth-two threshold circuits

A depth-two LTF circuit composes two layers of linear threshold gates. The source asks for a nontrivial pseudorandom generator when the number of gates is superlinear in the input length. Threshold gates aggregate many weighted inputs, allowing correlations to influence the output in ways simple local tests cannot capture. A generator in this size range would strengthen derandomization for a basic threshold-circuit model. The saved question does not quantify the superlinear growth, seed saving, or error, so these must be fixed before the intended advance can be assessed.

[Read in atlas](index.html#TCS-3958) · [Satisfiability and Derandomization for Small Polynomial Threshold Circuits](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2018.46)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3986 — Circuit hardness from inverse-polynomial-error BPP heuristics

The premise permits deterministic polynomial-time simulation of each BPP language with inverse-polynomial error under uniformly random inputs. The guarantee holds at every sufficiently large length, with separate algorithms for different requested error powers. The selected conclusion is a standard disjunction of Boolean circuit hardness for NEXP and arithmetic circuit hardness for the permanent. An older theorem reaches this conclusion under much smaller exceptional sets. The card makes the source’s broad converse direction precise through an explicitly authorized editorial specialization.

[Read in atlas](index.html#TCS-3986) · [Fine-Grained Derandomization: From Problem-Centric to Resource-Centric Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2018.27) · [Fine-Grained Derandomization: From Problem-Centric to Resource-Centric Complexity — full version](https://eccc.weizmann.ac.il/report/2018/092/) · [Pseudorandom generators, typically-correct derandomization, and circuit lower bounds](https://doi.org/10.1007/s00037-011-0019-z) · [On The Utility of Fine-Grained Complexity Theory](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2020/EECS-2020-165.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4778 — Derandomizing amplified relational computation

Relational computation allows many valid answers to a single input, which complicates familiar derandomization arguments. The paper distinguishes algorithms whose error can be reduced with logarithmic overhead from versions with weaker accuracy-time tradeoffs. It asks whether plausible derandomization assumptions collapse the stronger amplification variant to deterministic polynomial time. It also asks how that class relates to algorithms with negligible error and whether examples require polynomial dependence on inverse error. The project would clarify how randomness, output flexibility, and quantitative reliability interact beyond ordinary decision problems.

[Read in atlas](index.html#TCS-4778) · [A Qubit, a Coin, and an Advice String Walk into a Relational Problem](https://doi.org/10.4230/LIPIcs.ITCS.2024.1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5287 — Arithmetic formula hardness versus identity testing

Arithmetic formulas compute polynomials using tree-shaped addition and multiplication circuits. The source asks whether superpolynomial formula lower bounds imply nontrivial deterministic polynomial identity testing for formulas, and conversely. Hardness-versus-randomness aims to transform difficult explicit polynomials into test points that expose nonzero computations. An equivalence restricted to formulas would reveal whether this connection survives a more structured computational model. The saved question does not quantify “nontrivial” running time or all field assumptions, so it should not be read as automatically claiming polynomial-time PIT from any weak lower bound.

[Read in atlas](index.html#TCS-5287) · [Hardness vs Randomness for Bounded Depth Arithmetic Circuits](https://doi.org/10.4230/LIPIcs.CCC.2018.13)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5341 — Pseudorandom generators from hitting-set generators

A hitting-set generator outputs strings intersecting every sufficiently large acceptance set for a specified class of tests. A pseudorandom generator must approximate each test's acceptance probability under uniformly random input. The source asks whether techniques that derandomize two-sided-error algorithms using a hitting-set generator can also convert it into a pseudorandom generator. The surrounding discussion distinguishes polynomial-time generators from settings permitting computation exponential in the seed length. Hitting a large acceptance set alone does not control how frequently generated outputs pass a test, which is the stronger guarantee sought.

[Read in atlas](index.html#TCS-5341) · [Errorless Versus Error-Prone Average-Case Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2022.84)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5798 — Pseudodeterministic construction of primes at every length

Given a length in unary, generate a prime with exactly that many binary digits in polynomial time. For each length, independent runs must return the same fixed prime with probability at least two thirds. The fixed prime may depend on the algorithm; it is not prescribed in advance. The requirement must hold at every length of at least two bits. The known polynomial-time construction meets this requirement only on infinitely many lengths.

[Read in atlas](index.html#TCS-5798) · [Bipartite Perfect Matching in Pseudo-Deterministic NC](https://doi.org/10.4230/LIPIcs.ICALP.2017.87) · [Polynomial-Time Pseudodeterministic Construction of Primes](https://doi.org/10.1145/3803408)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6686 — P versus RP

RP consists of polynomial-time randomized decision algorithms that never accept a false instance and accept true instances with substantial probability. The textbook asks whether every such language has a deterministic polynomial-time algorithm, giving \(\mathrm{P}=\mathrm{RP}\). One-sided error makes an observed acceptance trustworthy but does not explain how to find a successful random tape efficiently. Resolving the equality would determine whether this basic use of randomness enlarges efficient decision power. The saved note is historical, and a deterministic simulation for only a particular RP problem would not settle the universal class comparison.

[Read in atlas](index.html#TCS-6686) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6689 — Simultaneously optimal averaging samplers

An averaging sampler chooses a small collection of locations whose observed average estimates a global average. The textbook asks for constructions simultaneously optimal in the number of random bits and the number of samples. Reducing randomness can introduce correlations, while reducing samples leaves less room to absorb the resulting estimation error. Achieving both goals would make a basic sampling primitive efficient in its two main resources. The saved note does not provide its error and failure probabilities or explicitness convention, so those parameters must be restored before optimality has one precise meaning.

[Read in atlas](index.html#TCS-6689) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6693 — Subpolynomial-seed pseudorandom generators for \(\mathrm{AC}^{0}[2]\)

\(\mathrm{AC}0[2]\) circuits combine constant-depth Boolean operations with parity gates. The textbook asks for pseudorandom generators with subpolynomial seed length that fool this circuit class. Such a seed would be smaller than every fixed positive power of the relevant input length. The target would provide a strong form of unconditional derandomization for circuits capable of detecting algebraic correlations. The saved historical note does not specify size, depth, or error dependencies, and a merely sublinear seed does not automatically meet the stronger subpolynomial requirement.

[Read in atlas](index.html#TCS-6693) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6696 — Uniform PRGs from exponential-time hardness

EXP contains languages decidable in deterministic exponential time. The textbook asks for strong uniform pseudorandom generators from the assumption that EXP is not contained in randomized subexponential time. The premise expresses uniform algorithmic hardness rather than a lower bound against arbitrary circuits. Deriving a generator would clarify how much pseudorandomness follows from this broader type of computational difficulty. The saved note does not reproduce the generator parameters or simulation quantifiers, so the exact strength of the conclusion and the treatment of exceptional input lengths still need source recovery.

[Read in atlas](index.html#TCS-6696) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6699 — AM versus NP

Arthur–Merlin protocols use public randomness and a prover to verify claims efficiently. The textbook asks whether their randomness can be removed so that AM collapses to NP. It singles out graph nonisomorphism, where the desired outcome would be polynomially checkable certificates that two graphs differ up to relabeling. Such certificates would replace an interactive randomized justification with a static witness. The specific graph problem is a consequence to seek rather than an equivalent restatement of full \(\mathrm{AM}=\mathrm{NP}\), and the dated source note does not constitute a current-status review.

[Read in atlas](index.html#TCS-6699) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6729 — Deterministic linear representations of transversal matroids

A transversal matroid records which subsets can be matched into the opposite side of a bipartite incidence graph. A linear representation instead encodes independence through linear independence of matrix columns. The textbook asks for a deterministic polynomial-time construction translating the former representation into the latter. Such a construction would remove randomness from algebraic algorithms that rely on representing these combinatorial independence systems. The saved note does not specify field-size or encoding conventions, so the desired deterministic construction still needs those representation details for a complete statement.

[Read in atlas](index.html#TCS-6729) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6879 — Explicit near-optimal vertex expanders

Vertex expansion measures how many distinct outside neighbors a small vertex set has. The source asks for explicit regular graphs whose small-set expansion approaches \(d- 2\) at degree d. The target concerns neighbor diversity rather than only the number of crossing edges, so ordinary spectral quality may not directly yield the requested sharp bound. Such graphs would strengthen constructive tools where small sets must spread information to many new vertices. The saved question does not preserve the permitted set-size range or approximation slack, so those parameters must be recovered before comparing a graph family with the target.

[Read in atlas](index.html#TCS-6879) · [Expander Graphs and Their Applications](https://www.math.ias.edu/avi/node/974)
Existing status: `source_open` · Summary written: 2026-09-11

## Parameterized complexity and algorithms (41)

### TCS-6592 — FPT versus \(\mathrm{W}[1]\)

A k-clique is a set of k graph vertices joined by every possible edge. The question asks for one exact deterministic algorithm whose input-size exponent is constant while a computable multiplier absorbs all dependence on k. Polynomial time separately for each fixed k does not establish that uniform bound. Clique completeness makes the question equivalent to FPT equalling W[1]. Conditional lower bounds and recent fixed-k or approximation results explain the conjecture’s significance without deciding it.

[Read in atlas](index.html#TCS-6592) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [On \(\mathrm{W}(1)\)-Hardness as Evidence for Intractability](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73) · [Constant Approximating k-Clique is \(\mathrm{W}(1)\)-hard](https://arxiv.org/abs/2102.04769) · [Simple Combinatorial Construction of the \(k^{o(1)}\)-Lower Bound for Approximating the Parameterized k-Clique](https://arxiv.org/abs/2304.07516) · [Faster Combinatorial k-Clique Algorithms](https://weizmann.elsevierpure.com/en/publications/faster-combinatorial-k-clique-algorithms-2/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6593 — Exponential Time Hypothesis

ETH asks whether the optimal deterministic exponential rate for 3-SAT is strictly positive. The exponential parameter is the number of distinct variables, while polynomial factors account for the complete encoded input. One positive rate must obstruct every algorithm, and refutation permits different algorithms for arbitrarily small positive rates. Known exponential-time algorithms provide upper bounds but no positive lower bound on the optimum. The hypothesis supports quantitative lower bounds throughout exact and parameterized algorithms without being established by those conditional consequences.

[Read in atlas](index.html#TCS-6593) · [On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [Exact Complexity and Satisfiability](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2013_ipec.pdf) · [Chain, Generalization of Covering Code, and Deterministic Algorithm for k-SAT](https://arxiv.org/abs/1804.07901) · [Mind the Gap? Not for SVP Hardness Under ETH!](https://doi.org/10.4230/LIPIcs.ICALP.2026.8)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6594 — Set Cover conjecture

Set Cover asks whether a few supplied sets can cover a given universe. The conjecture concerns exact algorithms when each available set has a fixed maximum size. It says that no constant improvement over exponential base two works across all such size bounds. The target allows bounded-error randomization and polynomial factors that depend on the fixed bound. Recent results show that a major conjecture about tensor rank would refute SCC, but neither side is settled unconditionally.

[Read in atlas](index.html#TCS-6594) · [Fundamental Problems on Bounded-Treewidth Graphs: The Real Source of Hardness](https://doi.org/10.4230/LIPIcs.ICALP.2024.34) · [On Problems as Hard as CNF-SAT](https://arxiv.org/abs/1112.2275) · [The Asymptotic Rank Conjecture and the Set Cover Conjecture Are Not Both True](https://arxiv.org/abs/2310.11926) · [A Stronger Connection between the Asymptotic Rank Conjecture and the Set Cover Conjecture](https://arxiv.org/abs/2311.02774)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7241 — FPT approximation of twin-width

Twin-width measures mixed adjacency during repeated merges of vertex groups. The question asks for an algorithm that finds a bounded-width merge sequence whenever the graph has twin-width at most k. Its running time may depend arbitrarily on k but only polynomially on graph size, with an exponent independent of k. The algorithm receives the graph alone, without a useful vertex order or decomposition. A positive answer would make twin-width-based algorithmic methods accessible from ordinary graph input.

[Read in atlas](index.html#TCS-7241) · [Open problems in twin-width](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) · [Twin-width one](https://arxiv.org/abs/2501.00991)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6660 — Polynomial kernel for Edge Multiway Cut

Edge Multiway Cut removes a small number of edges so that no two designated terminals remain connected. The question asks whether polynomial-time preprocessing can reduce any instance to an equivalent instance of size polynomial in the deletion budget alone. The number of terminals is unrestricted, and the size exponent must not depend on it. Randomized preprocessing is allowed with a per-instance equivalence guarantee of at least two thirds. Known fixed-terminal kernels and quasipolynomial-size kernels leave the unrestricted polynomial-size target open in the checked sources.

[Read in atlas](index.html#TCS-6660) · [Quasipolynomial multicut-mimicking networks and kernels for multiway cut problems](https://arxiv.org/abs/2002.08825v3) · [Quasipolynomial-Time Deterministic Kernelization and (Gammoid) Representation](https://doi.org/10.4230/LIPIcs.MFCS.2025.54)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4790 — Subset Sum below the meet-in-the-middle exponent

Subset Sum asks whether some subcollection of given positive integers adds to a target. The classical worst-case benchmark comes from the meet-in-the-middle exponent. The question asks for a fixed positive saving in that exponent with polynomial dependence on binary input length. Bounded-error classical randomization is allowed, with no random-instance promise. Quantum, pseudopolynomial and polynomial-factor improvements do not establish this fixed exponent saving.

[Read in atlas](index.html#TCS-4790) · [Subset Sum Quantumly in \(1.17^{n}\)](https://doi.org/10.4230/LIPIcs.TQC.2018.5) · [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7181 — Exact recognition of bounded clique-width

Clique-width measures how many reusable vertex labels are needed to build a graph with four specified operations. Even a complete graph of arbitrary size needs only two labels. The question asks whether graphs of width at most k can be recognized in polynomial time for every fixed k. The polynomial exponent may depend on k, so known NP-completeness when k is input does not settle it. Small thresholds are understood, while approximate or supplied decompositions do not give exact recognition at every threshold.

[Read in atlas](index.html#TCS-7181) · [Clique-width is NP-complete](https://doi.org/10.1137/070687256) · [Polynomial-time recognition of clique-width \(\le 3\) graphs](https://doi.org/10.1016/j.dam.2011.03.020) · [Tight Bounds for Feedback Vertex Set Parameterized by Clique-Width](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.39)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7247 — Independent set algorithms from tropical circuit size

A tropical circuit combines vertex weights using only maximum and addition. For each graph, \(\tau\) measures the smallest circuit that computes maximum independent-set weight for every nonnegative weight assignment. The question asks for a uniform algorithm whose runtime is polynomial in \(\tau\) and the input size. The algorithm receives no circuit or decomposition and may use unrestricted deterministic computation. A positive answer would turn the existence of a compact dynamic program into an effective algorithmic guarantee.

[Read in atlas](index.html#TCS-7247) · [Lower Bounds on Dynamic Programming for Maximum Weight Independent Set](https://arxiv.org/abs/2102.06901) · [Open problems: Can dynamic programming for independent set be automated?](https://tuukkakorhonen.com/problems.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-3480 — Polynomial exact metric sparsifiers with a crossing-edge budget

A graph with terminals is queried by choosing labels for the terminals and a metric on the labels. The goal is a small retained edge set that supports an optimal extension for every such query. Only labelings with at most p crossing edges are compared, and the retained set must have size polynomial in p plus the number of terminals. The original claimed quasipolynomial metric-sparsifier result was explicitly retracted in the corrected paper. Ordinary multicut sparsifiers preserve a different collection of values and do not settle this universal metric question.

[Read in atlas](index.html#TCS-3480) · [On Quasipolynomial Multicut-Mimicking Networks and Kernelization of Multiway Cut Problems](https://doi.org/10.4230/LIPIcs.ICALP.2020.101) · [Quasipolynomial multicut-mimicking networks and kernelization of multiway cut problems — corrected full version](https://arxiv.org/abs/2002.08825v3) · [Quasipolynomial Multicut-mimicking Networks and Kernels for Multiway Cut Problems](https://doi.org/10.1145/3501304) · [Approximating Small Sparse Cuts](https://arxiv.org/abs/2403.08983)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7023 — Polynomial kernels for minor-free edge deletion

The problem deletes at most k edges so that the remaining graph excludes every member of a fixed forbidden-minor family. It asks whether every such family permits a polynomial-time reduction to one equivalent instance of polynomial size in k. The input graph is arbitrary, and all vertices remain available during edge deletion. A general kernel would provide a broad preprocessing guarantee for structural graph repair beyond known fixed-parameter algorithms. The card restores the family quantifier and distinguishes vertex deletion, promised minor-free inputs and more general compressions.

[Read in atlas](index.html#TCS-7023) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867v2) · [A survey of parameterized algorithms and the complexity of edge modification](https://fedorvf.github.io/articles/2023/2023e.pdf) · [Robust Contraction Decomposition for Minor-Free Graphs and Its Applications](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.17/LIPIcs.ICALP.2025.17.html)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0787 — ETH barrier to single-exponential treewidth computation

Treewidth is the smallest maximum bag size minus one among tree decompositions of a graph. The target asks whether ETH rules out exact decision in single-exponential time in the requested width and polynomial time in graph size. The algorithm must handle every input without receiving a decomposition or a promise that the width threshold is met. Resolving the question would clarify the cost of discovering the structural information used by many parameterized algorithms. The new exponential lower bound in the number of vertices is recorded separately because it does not exclude the requested parameter dependence.

[Read in atlas](index.html#TCS-0787) · [Optimality and Tight Results in Parameterized Complexity (Dagstuhl Seminar 14451)](https://doi.org/10.4230/DagRep.4.11.1) · [An Improved Parameterized Algorithm for Treewidth](https://arxiv.org/abs/2211.07154v2) · [Treewidth Inapproximability and Tight ETH Lower Bound](https://arxiv.org/abs/2406.11628v2) · [Treewidth Inapproximability and Tight ETH Lower Bound](https://doi.org/10.1145/3833387)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0734 — FPT Inapproximability Results Beyond Gap-ETH

The seminar asks for stronger fixed-parameter inapproximability results that remain beyond known techniques even when Gap-ETH is assumed. For k-Set Cover, one target is approximation hardness of order \(\log ^{0.99}(n)\), where n is the number of elements to cover. A second target is to rule out every \(g(k)\)-factor FPT approximation for Exact k-Set Cover, whose promise is that a size-k cover consisting of disjoint sets exists. It also asks for \(o(k)\)-factor hardness of Densest k-Subgraph with perfect completeness under Gap-ETH, matching a result based on the Strongish Planted Clique Hypothesis. In particular, hardness with disjoint-cover completeness would support further reductions to coding and lattice problems.

[Read in atlas](index.html#TCS-0734) · [Parameterized Approximation: Algorithms and Hardness](https://doi.org/10.4230/DagRep.13.7.96)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0784 — Polynomial kernels for Edge-Disjoint Paths

Edge-Disjoint Paths asks whether specified terminal pairs can be connected by paths that share no edges. The source question asks whether the problem admits a polynomial kernel under its intended parameterization. A kernel would compress a large routing instance while retaining precisely whether all requested connections can coexist. That would expose whether small routing requirements imply a compact representation of the relevant network interactions. The inherited label does not identify the parameter or graph restrictions, and these cannot be supplied by assuming the most familiar variant of the problem.

[Read in atlas](index.html#TCS-0784) · [Graph Modification Problems](https://doi.org/10.4230/DagRep.4.2.38)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0801 — Directed Hamiltonicity

Directed Hamiltonicity asks whether a directed graph contains a cycle visiting every vertex exactly once. Orientation makes the order of traversal essential and prevents freely reversing a candidate connection. The saved entry places this exact search problem among questions about exponential and parameterized algorithms. A meaningful improvement would reduce the work needed to coordinate a single globally consistent cycle through all vertices. The inherited title supplies no parameter, graph promise, or target exponential base, so this draft identifies the task without inventing a particular conjectured bound.

[Read in atlas](index.html#TCS-0801) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0805 — Exact Counting of Linear Extensions

A linear extension is a total ordering consistent with all comparisons in a given partial order. The task is to count these compatible orderings exactly. This differs from finding one ordering, because the output must account for every possible way incomparable elements can interleave. Sharper algorithms would improve exact combinatorial counting for precedence systems and clarify its exponential complexity. The saved label does not specify the representation of the partial order, available structural parameters, or desired time-space bound, leaving those details for the later formulation.

[Read in atlas](index.html#TCS-0805) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0816 — Shortest common superstring problem

Shortest Common Superstring seeks a shortest string containing every input string as a contiguous substring. The optimization exploits overlaps between strings while ensuring that all required pieces appear. The saved entry asks about its exact computational complexity within the parameterized and exponential-time setting. Improved algorithms would clarify the cost of assembling many overlapping sequences into one compact representation. The title does not fix alphabet restrictions, the measured input parameter, or an approximation allowance, so these choices cannot be silently imported into the working question.

[Read in atlas](index.html#TCS-0816) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0800 — Cutwidth

A cutwidth layout orders vertices and measures how many edges cross the busiest prefix boundary. This entry asks about the computational complexity of optimizing that maximum. The objective captures how much simultaneous edge interaction a linear arrangement must accommodate. Sharper exact algorithms or lower bounds would help establish the intrinsic cost of this graph layout measure. The saved source contains only the topic label, leaving graph restrictions, approximation allowances, and the relevant size parameter unspecified rather than supporting an exact conjectured running time.

[Read in atlas](index.html#TCS-0800) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0808 — Maximum Acyclic Subgraph

Maximum Acyclic Subgraph seeks as many directed edges as possible while forbidding directed cycles. Equivalently, it asks which edge interactions can be retained without circular dependence. The source entry concerns the exact or parameterized complexity of this optimization task. Progress would clarify the computational cost of extracting a consistent precedence structure from conflicting directed relations. The inherited title does not identify a parameter, weight convention, or target exponential bound, so this preliminary account does not silently replace the question with feedback-arc minimization under additional assumptions.

[Read in atlas](index.html#TCS-0808) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0597 — Parameterized coloring of H-free graphs

An H-free graph excludes a specified graph H under the source's intended containment convention. The entry asks about parameterized complexity of coloring problems on such restricted graphs. Forbidding a pattern can simplify the interactions that force many colors, but different forbidden graphs can behave very differently. A classification would identify which structural exclusions make coloring computationally manageable. The saved label does not specify induced versus ordinary subgraph exclusion, the coloring variant, or the parameter, so it does not justify a particular tractability boundary.

[Read in atlas](index.html#TCS-0597) · [Graph Colouring: from Structure to Algorithms](https://doi.org/10.4230/DagRep.9.6.125)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0799 — Converting CNF to DNF

Conjunctive normal form combines clauses with conjunction, whereas disjunctive normal form combines terms with disjunction. The saved problem concerns converting a Boolean representation of the first kind into an equivalent representation of the second. Equivalent output can grow substantially because distribution expands combinations of choices across clauses. Understanding the best conversion cost would illuminate how representation size limits symbolic Boolean computation. The inherited label does not specify whether the goal is minimum output size, output-sensitive running time, or restricted formulas, so this draft retains those distinct possibilities.

[Read in atlas](index.html#TCS-0799) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1945 — Parameterized Nearest Codeword hardness beyond Gap-ETH

Nearest Codeword seeks a codeword close to a target vector under the specified distance measure. The source asks for constant-factor approximation lower bounds for its parameterized version and related problems. The desired obstruction excludes running times whose exponent in the input size is sublinear in k. Obtaining it from assumptions weaker than Gap-ETH would reduce reliance on a strong initial approximation-gap hypothesis. The saved excerpt does not define the field, distance parameter, or related variants, so those details remain part of the later precise formulation.

[Read in atlas](index.html#TCS-1945) · [Improved Lower Bounds for Approximating Parameterized Nearest Codeword and Related Problems Under ETH](https://doi.org/10.4230/LIPIcs.ICALP.2024.107)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2662 — Subexponential constant-gap Max-Clique under ETH

A constant-gap Max-Clique problem distinguishes graphs with a large clique from graphs whose cliques are smaller by a fixed factor. The saved question asks whether this promise problem admits subexponential time in the vertex count under ETH. The gap relaxes exact optimization while retaining a substantial difference between the two answer cases. Resolving its compatibility with ETH would clarify the relationship between exact satisfiability hardness and approximation gaps. The source excerpt does not specify the two thresholds or randomness convention, and its question is not itself an established ETH lower bound.

[Read in atlas](index.html#TCS-2662) · [On Lower Bounds of Approximating Parameterized k-Clique](https://doi.org/10.4230/LIPIcs.ICALP.2022.90)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2804 — Slice-wise Polynomial Space Conjecture

XNLP describes parameterized problems with short nondeterministic working memory and fixed-parameter polynomial running time. The conjecture forbids deterministic algorithms for XNLP-hard problems with both slice-wise polynomial time and a fixed polynomial space exponent. One algorithm must meet both guarantees on every input. The parameter may affect the time exponent and the space multiplier, but not the space exponent. Later completeness results retain this as a conjecture that would explain memory barriers in dynamic programming.

[Read in atlas](index.html#TCS-2804) · [On the Complexity of Problems on Tree-Structured Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2022.6) · [XNLP-Completeness for Parameterized Problems on Graphs with a Linear Structure](https://doi.org/10.1007/s00453-024-01274-9)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3917 — Disjoint-union closure of tractable forbidden patterns

Independent Set asks whether a graph contains k pairwise nonadjacent vertices. Suppose the problem is fixed-parameter tractable when either one of two fixed induced patterns is forbidden. The conjecture asks whether tractability persists when only their disjoint union is forbidden. This is already known when the forbidden components are cliques, and the 2020 journal manuscript retains the general conjecture. The problem concerns the forbidden pattern, not whether the input graph itself is disconnected.

[Read in atlas](index.html#TCS-3917) · [Parameterized Complexity of Independent Set in H-Free Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2018.17) · [Parameterized Complexity of Independent Set in H-Free Graphs](https://doi.org/10.1007/s00453-020-00730-6) · [When Maximum Stable Set Can Be Solved in FPT Time](https://doi.org/10.4230/LIPIcs.ISAAC.2019.49)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4289 — \(\mathrm{W}[2]\)-hardness of bounded-VC-dimension Hitting Set

Hitting Set asks for a small collection of elements that intersects every set in an input set system. Bounding the system's VC-dimension limits its shattering complexity and supports strong approximation results, but does not automatically make exact optimization tractable. The source asks whether Hitting Set remains \(\mathrm{W}[2]\)-hard even when the VC-dimension is bounded by a constant. Here the parameter is the size of the requested hitting set, so the target is a stronger parameterized hardness classification within a structurally restricted family. An answer would sharpen the distinction between low-dimensional sampling structure and the difficulty of finding an exact small transversal.

[Read in atlas](index.html#TCS-4289) · [Hitting Set for Hypergraphs of Low VC-dimension](https://doi.org/10.4230/LIPIcs.ESA.2016.23)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4440 — Expected FPT delay from small-witness decision

A self-contained witness is a k-element subset whose validity survives restriction to any universe containing it. An FPT decision algorithm can therefore test whether a chosen subset contains a witness. The selected question asks whether this always yields exact enumeration with expected FPT time between outputs, including startup and termination. The source already controls expected total work but leaves the stronger delay guarantee open. Incremental time, deterministic delay and enumeration with possible omissions are separate variants.

[Read in atlas](index.html#TCS-4440) · [Randomised Enumeration of Small Witnesses Using a Decision Oracle](https://doi.org/10.4230/LIPIcs.IPEC.2016.22) · [Randomised Enumeration of Small Witnesses Using a Decision Oracle](https://doi.org/10.1007/s00453-018-0404-y)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4637 — Subexponential Planar Steiner Tree by terminal count

Planar Steiner Tree connects a specified terminal set at minimum cost in a planar graph. The saved question asks for subexponential time with respect to the number of terminals. The terminal count can be small even when the graph contains many possible intermediate connection points. An algorithm exploiting both facts would improve the parameter dependence for a central planar network problem. The excerpt does not specify weight conventions or the precise polynomial input factor, and the source's historical question is not a fresh verification of present open status.

[Read in atlas](index.html#TCS-4637) · [Subexponential-Time Parameterized Algorithm for Steiner Tree on Planar Graphs](https://doi.org/10.4230/LIPIcs.STACS.2013.353)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4695 — Polynomial kernels for forbidden-minor vertex deletion

Delete at most a specified number of vertices to eliminate every minor from a fixed finite family. The question asks for polynomial-time preprocessing to one equivalent instance of polynomial size in that budget. The polynomial may depend on the forbidden family. Families containing a planar obstruction are covered, while planarization remains a key open case. Later lossy and structural-parameter results do not establish the full exact-kernel claim.

[Read in atlas](index.html#TCS-4695) · [Hitting forbidden minors: Approximation and Kernelization](https://doi.org/10.4230/LIPIcs.STACS.2011.189) · [Planar F-Deletion: Approximation, Kernelization and Optimal FPT Algorithms](https://doi.org/10.1109/FOCS.2012.62) · [Lossy Planarization: A Constant-Factor Approximate Kernelization for Planar Vertex Deletion](https://doi.org/10.1137/22M152058X) · [Kernelization Dichotomies for Hitting Minors Under Structural Parameterizations](https://doi.org/10.4230/LIPIcs.STACS.2026.17)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5374 — Degeneracy-sensitive classification of homomorphism counting

Pattern homomorphism counting measures adjacency-preserving maps from a pattern into a host graph. The source asks for an explicit criterion on computable pattern classes in its degeneracy-sensitive counting framework. The intended dichotomy places every satisfying class in FPT and every remaining class on the #\(\mathrm{W}[1]\)-hard side. Such a criterion would explain a broad tractability boundary rather than only catalog individual easy patterns. The saved notation does not fully define the host restrictions or parameter combination, so those model details must be supplied before presenting the classification as self-contained.

[Read in atlas](index.html#TCS-5374) · [Exact and Approximate Pattern Counting in Degenerate Graphs: New Algorithms, Hardness Results, and Complexity Dichotomies](https://doi.org/10.1109/FOCS52979.2021.00036)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6379 — Polynomial kernels for Directed Feedback Vertex Set

Directed Feedback Vertex Set asks whether deleting at most a given number of vertices destroys every directed cycle. The question is whether polynomial-time preprocessing can always replace an instance by one of size polynomial in that deletion budget. The replacement must preserve the exact yes or no answer. Known kernels with extra structural parameters or more restrictive deletion targets do not give this guarantee. Resolving the general question would clarify the limits of efficient compression for directed cycle problems.

[Read in atlas](index.html#TCS-6379) · [Polynomial Kernels for Deletion to Classes of Acyclic Digraphs](https://doi.org/10.4230/LIPIcs.STACS.2016.55) · [Wannabe Bounded Treewidth Graphs Admit a Polynomial Kernel for Directed Feedback Vertex Set](https://doi.org/10.1145/3711669)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6728 — Chromatic number in \(2^{n}\) time and polynomial space

The chromatic number is the fewest colors needed to color graph vertices so adjacent vertices receive different colors. The saved textbook question asks for \(O*(2^{n})\) exact running time using only polynomial space. The star suppresses polynomial factors, making the exponential base and memory requirement the essential targets. Meeting both bounds would combine fast subset-based computation with a memory footprint that does not grow exponentially. This is a dated textbook formulation; the saved note does not provide a review of later algorithms or establish present open status.

[Read in atlas](index.html#TCS-6728) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6731 — Strictness of the W-hierarchy

The W-hierarchy organizes parameterized problems into levels defined through controlled forms of computational complexity. The saved textbook question asks for strict separations between these levels, including those associated with Independent Set and Dominating Set. Such separations would distinguish different kinds of parameterized intractability rather than merely separate all of them from FPT. They would strengthen the interpretation of completeness results throughout parameterized complexity. The source records a broad hierarchy question without selecting one pair of levels, and its historical presentation does not supply an unconditional separation.

[Read in atlas](index.html#TCS-6731) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6734 — Polynomial compression versus polynomial kernelization

A polynomial compression maps an instance into a short equivalent string for some target decision problem. A polynomial kernel requires the output to remain an instance of the original problem. The textbook asks for natural problems demonstrating a separation between these preprocessing capabilities. Such an example would show whether freedom to change the output language provides a substantive advantage in useful settings. The saved formulation does not define the intended naturalness criterion or the assumptions supporting nonexistence of kernels, so it remains an exploratory separation target.

[Read in atlas](index.html#TCS-6734) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6749 — Deterministic polynomial kernels for Almost 2-SAT

Almost 2-SAT asks whether a limited number of clauses can be removed from a 2-CNF formula to make it satisfiable. The saved question asks for a deterministic polynomial kernel with the deletion budget as the intended parameter. Preprocessing must retain the interactions responsible for inconsistency while reducing the complete instance to polynomial size. A deterministic result would make that compression guarantee independent of random choices. The note records the question from the 2017 source without checking subsequent developments, so the draft does not infer a currently unresolved derandomization gap.

[Read in atlas](index.html#TCS-6749) · [The Constraint Satisfaction Problem: Complexity and Approximability](https://drops.dagstuhl.de/entities/volume/DFU-volume-7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6814 — Efficient PTAS for fixed-machine job-shop makespan

Job-shop scheduling assigns each job a sequence of operations that must use specified machines. The saved question asks for a makespan approximation scheme running in \(f(m,\varepsilon )\) times a polynomial in n. The exponent of input size must stay independent of machine count and requested accuracy. Such a scheme would isolate the expensive dependence in the structural and approximation parameters while remaining scalable in the number of jobs. The source note does not define its operation restrictions or parameter conventions, so those details remain required before asserting the exact scheme model.

[Read in atlas](index.html#TCS-6814) · [Parameterized complexity of machine scheduling: 15 open problems](https://arxiv.org/abs/1709.01670)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6974 — Formula-SAT below exhaustive search

Boolean formula satisfiability asks whether some assignment makes a formula true. With n variables, exhaustive search checks all \(2^{n}\) assignments, paying an additional cost to evaluate the formula. The selected research direction seeks an algorithm that improves this worst-case search bound for general formulas. Restrictions on clause width, depth, or size can change which techniques apply, so gains for specialized families do not automatically answer it. A successful approach would identify exploitable structure in arbitrary formulas even when polynomial-time solvability remains out of reach.

[Read in atlas](index.html#TCS-6974) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7022 — Polynomial kernels for Planar Deletion

The edge-modification survey's Planar Deletion problem asks whether a small number of edges can be removed to obtain a planar graph. The saved question asks for a polynomial kernel in the modification budget. Such preprocessing would preserve whether the graph can be made planar while discarding material irrelevant to a small repair. The main structural issue is that nonplanarity can arise through large interacting configurations. The source inventory retains the 2020 question historically and does not itself establish whether later work has supplied the requested kernel.

[Read in atlas](index.html#TCS-7022) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7027 — Fixed-parameter tractability of Perfect Deletion

A perfect graph has chromatic number equal to clique number in every induced subgraph. The edge-modification survey asks whether deleting a bounded number of edges to obtain such a graph is fixed-parameter tractable. The repair target imposes conditions across many induced subgraphs rather than only a single global coloring requirement. An algorithm would show that proximity to perfection can be exploited even when the input itself lacks that structure. The saved note gives no quantitative parameter dependence and preserves a historical question whose later developments have not been checked here.

[Read in atlas](index.html#TCS-7027) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7033 — Polynomial kernels for directed feedback sets

Directed feedback sets remove vertices or arcs until no directed cycle remains. The survey asks for polynomial kernels for both versions, parameterized by the allowed number of removals. The compression must preserve interactions among cycles that may share only selected portions of their routes. Resolving these questions would determine whether small directed cycle-repair budgets imply compact equivalent instances. The vertex and arc variants remain separate tasks, and the saved 2020 formulation supplies neither a current resolution nor a particular optimal polynomial size.

[Read in atlas](index.html#TCS-7033) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7035 — Single-exponential FPT for directed feedback sets

Directed feedback problems seek a small deletion set that eliminates all directed cycles. The saved survey question asks for fixed-parameter algorithms with single-exponential dependence on the deletion budget. It also includes the vertex-deletion case on planar directed graphs. Such a bound would replace more costly parameter growth with a clearer exponential search scale. The source question spans distinct variants, so an algorithm for planar vertex deletion would not automatically settle the unrestricted vertex and arc cases, and subsequent status has not been audited here.

[Read in atlas](index.html#TCS-7035) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7036 — Parameterized complexity of three-pair Directed Edge Multicut

Directed Edge Multicut deletes arcs so that each specified source can no longer reach its paired target. The saved question fixes three terminal pairs and parameterizes the problem by cut size. Three simultaneous reachability constraints can interact even when each individual separation is easy to describe. A classification would locate a precise small-demand boundary for parameterized directed cutting. The survey formulation asks for tractability or hardness rather than a particular running-time base, and the historical source inventory does not decide whether later work has closed that boundary.

[Read in atlas](index.html#TCS-7036) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867)
Existing status: `source_open` · Summary written: 2026-09-11

## Approximation algorithms and inapproximability (24)

### TCS-6587 — Constant-factor approximation for Densest k-Subgraph

Densest k-Subgraph asks which exactly k vertices of a graph contain the most internal edges. The target is a polynomial-time algorithm whose edge count stays within one universal constant of optimum. Fixing the number of vertices prevents using a larger, moderately dense region as a substitute. Such a guarantee would clarify a central gap in approximation theory and influence several related network problems. The saved review describes strong conditional hardness under ETH, while distinguishing this evidence from hardness based only on \(\mathrm{P}\ne \mathrm{NP}\).

[Read in atlas](index.html#TCS-6587) · [Detecting High Log-Densities — an \(O(n^{1}/4)\) Approximation for Densest k-Subgraph](https://arxiv.org/abs/1001.2891) · [Polynomial integrality gaps for strong SDP relaxations of Densest k-subgraph](https://arxiv.org/abs/1110.1360) · [Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph](https://arxiv.org/abs/1611.05991) · [A New Conjecture on Hardness of 2-CSP’s with Implications to Hardness of Densest k-Subgraph and Other Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38) · [A Scalable and Exact Relaxation for Densest k-Subgraph via Error Bounds](https://ojs.aaai.org/index.php/AAAI/article/view/38562) · [A Note on Approximability of Densest At-Least-k-Subgraph](https://arxiv.org/abs/2605.25464)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0006 — Unique Games Conjecture

A Unique Games instance assigns labels to vertices, with each edge specifying a permutation relating its endpoint labels. The conjecture asks whether almost satisfiable instances are NP-hard to distinguish from instances with very small optimum value. Although perfect satisfiability can be checked by propagating labels, a small allowance for violated constraints changes the challenge. The conjecture would explain approximation thresholds for many constraint satisfaction problems through semidefinite programming. The saved review emphasizes that hardness with completeness one half does not establish the required completeness arbitrarily close to one.

[Read in atlas](index.html#TCS-0006) · [On the Unique Games Conjecture](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf) · [Optimal Algorithms and Inapproximability Results for Every CSP?](https://www.cs.cornell.edu/~abrahao/tdg/papers/p245.pdf) · [Subexponential Algorithms for Unique Games and Related Problems](https://www.boazbarak.org/Papers/ssesubexp.pdf) · [On the Proof of the 2-to-2 Games Conjecture](https://cs.nyu.edu/~khot/PCP-Spring-20/2-to-2-Exposition.pdf) · [Towards a Proof of the 2-to-1 Games Conjecture](https://theoryofcomputing.org/articles/v021a011/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6588 — Polylogarithmic approximation for Directed Steiner Tree

Directed Steiner Tree seeks a minimum-cost directed network connecting one root to every required terminal. The question asks for randomized polynomial-time approximation within a fixed power of the logarithm of the terminal count. Sharing arcs between routes can save substantially, but directionality complicates selecting useful branching structures. A positive result would close a major gap between polynomial-time algorithms and stronger guarantees obtainable in quasipolynomial time. The saved review warns that choosing a shrinking parameter in existing power-factor algorithms can destroy their polynomial running time.

[Read in atlas](index.html#TCS-6588) · [Approximation Algorithms for Directed Steiner Problems](https://chekuri.web.engr.illinois.edu/pub.html) · [\(O(\log ^{2} k/\log  \log  k)\)-Approximation Algorithm for Directed Steiner Tree: A Tight Quasi-Polynomial-Time Algorithm](https://people.idsia.ch/~grandoni/Pubblicazioni/GLL19stoc.pdf) · [An \(O(\log  k)\)-Approximation for Directed Steiner Tree in Planar Graphs](https://arxiv.org/abs/2302.04747) · [From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.42) · [On the Integrality Gap of Directed Steiner Tree LPs with Relatively Integral Solutions](https://arxiv.org/abs/2412.10744) · [Length-Constrained Network Design in Planar Digraphs](https://arxiv.org/abs/2607.25811)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7160 — Small-Set Expansion Hypothesis

Is it NP-hard to distinguish one poorly expanding small set from uniformly strong expansion at the same set size? The target set occupies a fixed fraction \(\delta\) of the graph, with \(\delta\) chosen after the gap parameter \(\eta\). Expansion is the fraction of incident edges that leave the set. A sparse cut of a larger size does not necessarily reveal any poorly expanding set of the target size. Known reductions connect the hypothesis to Unique Games and conditional hardness without resolving it.

[Read in atlas](index.html#TCS-7160) · [Graph Expansion and the Unique Games Conjecture](https://www.dsteurer.org/paper/expansion.pdf) · [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586) · [The Condition-Number Barrier in Sparse Least Squares](https://arxiv.org/abs/2608.02588)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6589 — Subtour-LP integrality gap for metric TSP

The metric traveling-salesperson problem asks for a cheapest tour through every point. Its subtour linear program permits fractional edges while preserving degree and cut constraints. This card asks for the supremum ratio of the integral tour optimum to that relaxation over all finite metrics. The classical \(4/3\) conjecture identifies a proposed value of this ratio. Benchmark acceptance requires a Lean-certified numerical value within absolute error 0.01, without assuming the supremum is attained.

[Read in atlas](index.html#TCS-6589) · [Maximum Entropy is a \(10/7\)-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances](https://arxiv.org/abs/2607.01536v2) · [A (Slightly) Improved Bound on the Integrality Gap of the Subtour LP for TSP](https://arxiv.org/abs/2105.10043v3) · [From Trees to Polynomials and Back Again: New Capacity Bounds with Applications to TSP](https://arxiv.org/abs/2311.09072v2) · [A \(4/3\)-Approximation Algorithm for Half-Integral Cycle Cut Instances of the TSP](https://arxiv.org/abs/2211.04639v2) · [The Integrality Gap of the Traveling Salesman Problem is \(4/3\) if the LP Solution Has at Most \(n+6\) Non-zero Components](https://arxiv.org/abs/2507.07003v2) · [Extending Exact Integrality Gap Computations for the Metric TSP](https://arxiv.org/abs/2603.12995v5) · [A Sharper Explicit Bound on the Subtour-LP Integrality Gap for Metric TSP](https://www.preprints.org/manuscript/202609.0140/v1)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6659 — Optimal polynomial-time approximation ratio for metric k-Median

Metric k-Median selects at most k allowed facilities to minimize total client distance. The card asks for the infimum universal approximation ratio of randomized polynomial-time algorithms. The same algorithm must work for all input sizes at each fixed guarantee, with success probability at least two thirds. The familiar \(1+2/e\) target and the saved algorithmic bounds locate competing possibilities for this infimum. Lean acceptance requires absolute error at most 0.01, with any complexity assumptions stated explicitly.

[Read in atlas](index.html#TCS-6659) · [A \((2+\varepsilon )\)-Approximation Algorithm for Metric k-Median](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf) · [A threshold of ln n for approximating set cover](https://disco.ethz.ch/alumni/pascalv/refs/ds_1998_feige.pdf) · [A new greedy approach for facility location problems](https://cgi.di.uoa.gr/~vassilis/co/co-papers/jain02.pdf) · [Tight FPT Approximations for k-Median and k-Means](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.42) · [Almost-Optimal Upper and Lower Bounds for Clustering in Low Dimensional Euclidean Spaces](https://arxiv.org/abs/2603.09846) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6590 — Subtour-LP integrality gap for asymmetric TSP

Asymmetric TSP finds a cheapest directed Hamiltonian tour in a directed metric. The subtour relaxation has fractional arcs with unit incoming and outgoing degree and at least one outgoing arc across each cut. The target is the supremum tour-to-LP ratio over all positive-LP finite instances. The familiar factor-two conjecture supplies one candidate for the value, and zero-LP metrics cause no division convention ambiguity. The Lean acceptance tolerance is absolute error 0.01 for the universal ratio.

[Read in atlas](index.html#TCS-6590) · [An Improved Approximation Algorithm for the Asymmetric Traveling Salesman Problem](https://epubs.siam.org/doi/10.1137/20M1339313) · [Approximation Algorithms for Traveling Salesman Problems](https://www.or.uni-bonn.de/tspbook/book.pdf) · [On the Integrality Gap of Small Asymmetric Traveling Salesman Problems: A Polyhedral and Computational Approach](https://arxiv.org/abs/2506.10671) · [The Cloven Traveling Salesman: Cycle Covers and the Integrality Gap of Small ATSP Instances](https://arxiv.org/abs/2511.05045v2)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7356 — Optimal polynomial-time approximation ratio for metric TSP

Metric TSP asks for a shortest tour through every point of an arbitrary finite metric. This card asks for the best expected ratio achievable by any uniform randomized polynomial-time algorithm. The ratio compares a returned tour with the optimal tour, not with an LP solution. The breakthrough below 3/2 leaves the ultimate approximation threshold undetermined. A Lean-certified estimate within absolute error 0.01 must bound the algorithmic infimum on both sides.

[Read in atlas](index.html#TCS-7356) · [A (Slightly) Improved Approximation Algorithm for Metric TSP](https://arxiv.org/abs/2007.01409)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6591 — Constant-factor approximation for Directed Feedback Vertex Set

A directed feedback vertex set removes vertices so that the remaining directed graph has no directed cycle. The saved question asks for a polynomial-time constant-factor approximation when vertices have weights and the graph is unrestricted. Many cycles may overlap, making a locally attractive deletion interact with numerous other choices. Understanding this approximation target would clarify how efficiently algorithms can destroy cyclic dependencies in directed systems. The saved note distinguishes this target from finding a polynomial kernel and does not supply a reviewed account of current approximation bounds.

[Read in atlas](index.html#TCS-6591) · [Research reference · drops.dagstuhl.de](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.55)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7357 — Optimal polynomial-time approximation ratio for asymmetric TSP

Asymmetric TSP allows different costs for the two directions between a pair of vertices. The costs obey the directed triangle inequality and the output visits each vertex once in a cycle. The target is the best expected ratio among all uniform randomized polynomial-time algorithms. A March 2026 result improves the known constant without determining this infimum. The benchmark requires a certified estimate within absolute error 0.01.

[Read in atlas](index.html#TCS-7357) · [Better approximation guarantee for Asymmetric TSP](https://arxiv.org/abs/2603.14334)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7353 — Optimal polynomial-time approximation ratio for Euclidean k-means

Euclidean k-means chooses k arbitrary centers to minimize the sum of squared distances. The dimension and cluster count are both part of the input. The target is the best ratio achievable by any uniform randomized polynomial-time algorithm. Recent 2026 algorithms improve the upper bound without determining that infimum. A certified value within 0.01 requires control of both the achievable ratios and the lower bound.

[Read in atlas](index.html#TCS-7353) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654) · [A (4 + epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting](https://doi.org/10.1145/3798129.3800894)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7358 — Optimal polynomial-time approximation ratio for Steiner Tree

Steiner Tree connects a specified terminal set using optional additional graph vertices. The input graph and its nonnegative rational edge weights are unrestricted. The card asks for the best expected approximation ratio among all uniform randomized polynomial-time algorithms. Different algorithmic approaches reach ln 4 without establishing the optimal threshold. Benchmark acceptance requires a Lean-certified value within absolute error 0.01.

[Read in atlas](index.html#TCS-7358) · [Steiner Tree Approximation via Iterative Randomized Rounding](https://doi.org/10.1145/2432622.2432628) · [Better-Than-2 Approximations for Weighted Tree Augmentation and Applications to Steiner Tree](https://doi.org/10.1145/3722101)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7354 — Optimal polynomial-time approximation ratio for metric k-means

Metric k-means selects exactly k centers from an explicit candidate set. Its objective is the sum of squared distances to the nearest selected center. The card asks for the infimum of expected polynomial-time approximation ratios on arbitrary finite metrics. The July 2026 preprint reports an upper bound approaching 4.9 without a matching determination. The requested numerical precision is absolute error at most 0.01.

[Read in atlas](index.html#TCS-7354) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0088 — Optimal approximation of Max Di-Cut

Max Di-Cut selects a vertex partition and counts arcs pointing from its first side to its second. The record asks for the best approximation ratio achievable by an efficient algorithm. Arc directions mean reversing the two sides can change the objective, unlike in an undirected cut. A sharp ratio would reveal how much of the best directed separation can be recovered without exact optimization. The saved entry does not specify weighting conventions, randomized guarantees, or the hardness assumption needed to turn this topic into one precise threshold question.

[Read in atlas](index.html#TCS-0088) · [TCS Open Problems](https://tcsopenproblems.com/problem/1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1168 — Hardness of coloring 2-dicolorable digraphs with any fixed number of colors

A dicoloring partitions a directed graph into color classes containing no directed cycle. The input is promised to admit two colors, but that coloring is not supplied. The source conjecturally asks whether producing any fixed larger number of colors remains NP-hard. Its polynomial-time algorithm uses a number of colors growing as the square root of the vertex count. Settling the constant-color hardness claim would clarify whether a bounded relaxation of the optimum can overcome the search difficulty.

[Read in atlas](index.html#TCS-1168) · [Hardness and Approximation for Coloring Digraphs](https://doi.org/10.4230/LIPIcs.ICALP.2026.53)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1930 — Parameterized Inapproximability Hypothesis from \(\mathrm{FPT} \ne  \mathrm{W}[1]\)

The hypothesis \(\mathrm{W}[1]\ne \mathrm{FPT}\) says exact parameterized problems such as k-Clique do not admit fixed-parameter algorithms. The question asks whether it also rules out distinguishing satisfiable binary constraint systems from systems that force a constant fraction of violations. The parameter is the number of variables, while the alphabet may grow with the input. PIH is already known under the stronger ETH assumption, and Baby PIH is known under \(\mathrm{W}[1]\ne \mathrm{FPT}\). A proof of the full implication would provide a broad foundation for parameterized inapproximability.

[Read in atlas](index.html#TCS-1930) · [Baby PIH: Parameterized Inapproximability of Min CSP](https://doi.org/10.4230/LIPIcs.CCC.2024.27) · [Parameterized Inapproximability Hypothesis under ETH](https://doi.org/10.1145/3749982) · [Parameterized inapproximability: From Clique to PIH](https://doi.org/10.1016/j.cosrev.2025.100834)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2625 — Almost 3-colorable graphs versus graphs with no large independent set

The yes instances become 3-colorable after deleting an arbitrarily small fixed fraction of vertices. The no instances have no independent set occupying a prescribed small fixed fraction of all vertices. The conjecture asks for NP-hardness of distinguishing these two cases. The source proves a weaker almost-coloring gap with randomized reductions. The stronger independent-set gap would improve hardness of approximating Vertex Cover toward a factor of three halves.

[Read in atlas](index.html#TCS-2625) · [NP-Hardness of Almost Coloring Almost 3-Colorable Graphs](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.51)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-5407 — Optimal approximation for submodular maximization over a matroid

Constrained submodular maximization chooses an independent set of a matroid to maximize a nonnegative submodular objective. The objective need not be monotone, so adding a feasible element can reduce its value. The extracted question asks for the best possible approximation factor in this general setting. It appears as background to a paper that additionally studies linear regularization, rather than being restricted to that modified objective. Matching oracle algorithms and lower bounds would determine the precise cost of combining diminishing returns, possible negative marginal gains, and matroid feasibility.

[Read in atlas](index.html#TCS-5407) · [On Maximizing Sums of Non-Monotone Submodular and Linear Functions](https://doi.org/10.4230/LIPIcs.ISAAC.2022.41)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5544 — d-to-1 versus Unique Games conjectures

The d-to-1 and Unique Games conjectures concern hardness of satisfying labeled constraints with different local compatibility structures. The saved 2016 passage asks whether the former implies the latter. A reduction must preserve a sufficiently strong completeness–soundness gap while turning several compatible labels into unique compatibility. An implication could connect distinct assumptions used to prove approximation hardness for general-domain CSPs. The excerpt truncates the final name and does not specify completeness conventions, so later results for related games cannot be substituted without checking the exact quantified conjectures.

[Read in atlas](index.html#TCS-5544) · [Near-Optimal UGC-hardness of Approximating Max \(k-\mathrm{CSP}_{R}\)](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5554 — Subquadratic factor-three edit-distance approximation

The task compares two arbitrary explicit strings using unit-cost insertions, deletions and substitutions. The estimate must lie between the true edit distance and three times that distance. The algorithm must save a fixed positive power over quadratic time on every input. Known truly subquadratic algorithms approach factor three from above. The 2026 approximation scheme achieves better accuracy, but its proved time saving is smaller than a fixed power of the input length.

[Read in atlas](index.html#TCS-5554) · [An Algorithmic Bridge Between Hamming and Levenshtein Distances](https://doi.org/10.4230/LIPIcs.ITCS.2023.58) · [Edit Distance in Near-Linear Time: it’s a Constant Factor](https://doi.org/10.1109/FOCS46700.2020.00096) · [Does Preprocessing Help in Fast Sequence Comparisons?](https://doi.org/10.1145/3357713.3384300) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://doi.org/10.1145/3798129.3800789)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5787 — Constant-factor approximation of graph crossing number

Draw every graph in the plane using at most a fixed constant times its minimum possible number of crossings. The constant must be independent of the graph size and maximum degree. The algorithm must construct a drawing in polynomial time; bounded-error randomization is allowed. Existing low-degree and dense-graph results do not provide this guarantee for all graphs. Hardness for one fixed ratio above one leaves open the possibility of a larger universal constant.

[Read in atlas](index.html#TCS-5787) · [Inserting Multiple Edges into a Planar Graph](https://doi.org/10.4230/LIPIcs.SoCG.2016.30) · [A Subpolynomial Approximation Algorithm for Graph Crossing Number in Low-Degree Graphs](https://arxiv.org/abs/2202.06827) · [An Algorithm for Estimating the Crossing Number of Dense Graphs, and Continuous Analogs of the Crossing and Rectilinear Crossing Numbers](https://doi.org/10.1007/s00454-025-00783-w)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6309 — Constant-factor approximation for capacitated k-Median

Capacitated k-median selects centers and assigns clients while limiting how many clients each center can serve. The objective minimizes total assignment distance using the permitted number of centers. The saved introductory passage highlights the existence of a polynomial-time constant-factor approximation as a central question in its source. Capacity restrictions complicate the usual strategy of sending every client to its nearest chosen center. The fragment does not preserve the exact capacity and center-count conventions, and the historical observation is not a new verification of the question's present status.

[Read in atlas](index.html#TCS-6309) · [Constant-Factor FPT Approximation for Capacitated k-Median](https://doi.org/10.4230/LIPIcs.ESA.2019.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6756 — Optimal general-domain CSP approximation under Unique Games hardness

The input lists local constraints on variables with a finite common label domain. The task maximizes the number of satisfied constraints using randomized polynomial time for each fixed arity and domain size. The target is the best expected approximation ratio, compared across both parameters with universal constants. The chosen hardness framework assumes Unique Games hardness and that NP is not contained in BPP. Known matching regimes and recent Boolean leading-constant claims do not determine the full general-domain scale.

[Read in atlas](index.html#TCS-6756) · [The Constraint Satisfaction Problem: Complexity and Approximability](https://drops.dagstuhl.de/entities/volume/DFU-volume-7) · [Approximation Algorithm for Non-Boolean Max-\(k\)-CSP](https://doi.org/10.4086/toc.2014.v010a013) · [Near-Optimal UGC-hardness of Approximating Max \(k\)-CSP\(_{R}\)](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.15) · [On the Approximability of Boolean Max-\(k\)-CSP](https://arxiv.org/abs/2608.05331) · [Sharp Analysis of Gaussian Rounding for Boolean Max \(k\)-CSP](https://arxiv.org/abs/2608.07800)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6757 — Min-CSP approximation at the SDP integrality gap

Minimization CSPs seek assignments minimizing a specified constraint-violation cost. The textbook asks whether algorithms can match their semidefinite-programming integrality gaps within an additional factor \(1+\varepsilon\). An integrality gap measures how much cheaper a fractional or vector solution can appear than any genuine assignment. Matching that benchmark would show that rounding loses essentially no more than the relaxation itself. The saved historical note does not identify the exact CSP family, relaxation, or treatment of zero optimum, so these conventions remain necessary before the target becomes a precise uniform theorem.

[Read in atlas](index.html#TCS-6757) · [The Constraint Satisfaction Problem: Complexity and Approximability](https://drops.dagstuhl.de/entities/volume/DFU-volume-7)
Existing status: `source_open` · Summary written: 2026-09-11

## Online algorithms, scheduling and packing (27)

### TCS-6575 — Deterministic competitiveness of k-server

In k-server, requests arrive at points of a metric space and a server must move to each requested point. The target is the infimum universal deterministic competitive ratio as a function of k. The ratio is uniform over metric spaces, while the rule and fixed additive cost may depend on the metric and initial placement. The classical k-server conjecture proposes the value k and attainment of that guarantee. The Lean benchmark accepts a function within absolute error 0.01 for every positive integer k.

[Read in atlas](index.html#TCS-6575) · [Competitive Algorithms for Server Problems](https://www.cs.cmu.edu/~sleator/papers/server-problems.pdf) · [On the k-server conjecture](https://cgi.di.uoa.gr/~elias/papers/paper-kp95.html) · [An Optimal On-Line Algorithm for K Servers on Trees](https://epubs.siam.org/doi/10.1137/0220008) · [Deterministic 3-server on a circle and the limitation of canonical potentials](https://www.sciencedirect.com/science/article/abs/pii/S0304397524004614) · [The Randomized k-Server Conjecture Is False!](https://arxiv.org/abs/2211.05753) · [k-server-bench: Automating Potential Discovery for the k-Server Conjecture](https://arxiv.org/abs/2604.07240)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6638 — Optimal approximation ratio for unrelated-machine makespan

Unrelated-machine scheduling allows each job to have a different processing time on every machine. The target is the infimum universal approximation ratio of deterministic polynomial-time algorithms in the stated model. Assigning every job to its favorite machine can create a severe load bottleneck. A better guarantee would improve a basic benchmark for scheduling heterogeneous work across heterogeneous resources. The numerical benchmark requires a Lean-certified value within absolute error 0.01, and conditional lower bounds retain their assumptions.

[Read in atlas](index.html#TCS-6638) · [Approximation Algorithms for Scheduling Unrelated Parallel Machines](https://ir.cwi.nl/pub/18055) · [An optimal rounding gives a better approximation for scheduling unrelated machines](https://www.sciencedirect.com/science/article/abs/pii/S0167637704000690) · [On the Configuration-LP for Scheduling on Unrelated Machines](https://arxiv.org/abs/1011.4957) · [Santa Claus meets Makespan and Matroids: Algorithms and Reductions](https://arxiv.org/abs/2307.08453) · [Learning-Augmented Approximation for Unrelated-Machines Makespan Scheduling](https://arxiv.org/abs/2606.13133)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6676 — Optimal approximation ratio for precedence-constrained makespan

Precedence-constrained scheduling assigns jobs to identical machines while respecting dependencies and minimizing overall completion time. The target is the infimum universal approximation ratio of deterministic polynomial-time algorithms in the stated model. A schedule must balance total work against long dependency chains that cannot execute in parallel. Progress would sharpen a foundational approximation boundary for dependent parallel computation. The numerical benchmark requires a Lean-certified value within absolute error 0.01, and conditional lower bounds retain their assumptions.

[Read in atlas](index.html#TCS-6676) · [Bounds for Certain Multiprocessing Anomalies](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1966.tb01709.x) · [Complexity of Scheduling under Precedence Constraints](https://pubsonline.informs.org/doi/abs/10.1287/opre.26.1.22) · [Hardness of Precedence Constrained Scheduling on Identical Machines](https://theory.epfl.ch/osven/Ola%20Svensson_publications/SICOMP11b.pdf) · [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40) · [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://arxiv.org/abs/2312.03495) · [Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs](https://arxiv.org/abs/2607.26590)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6640 — Constant additive error for one-dimensional bin packing

One-dimensional bin packing places indivisible numerical items into unit-capacity bins using as few bins as possible. The reviewed question asks for randomized polynomial time with at most a universal constant of extra bins above optimum. This is an additive guarantee, so the allowed excess does not grow with the size of the instance. It would strengthen approximation schemes whose small proportional errors can still yield many extra bins. The saved review notes that ordinary exact-optimization hardness and a multiplicative scheme do not automatically resolve this stronger additive target.

[Read in atlas](index.html#TCS-6640) · [New Developments in Iterated Rounding (Invited Talk)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2014.1) · [A Logarithmic Additive Integrality Gap for Bin Packing](https://arxiv.org/abs/1503.08796) · [Bin Packing via Discrepancy of Permutations](https://arxiv.org/abs/1007.2170) · [A counterexample to Beck’s conjecture on the discrepancy of three permutations](https://arxiv.org/abs/1104.2922) · [The Support of Bin Packing Is Exponential](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.48) · [A Tight Double-Exponential Lower Bound for High-Multiplicity Bin Packing](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.116)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6576 — Optimal competitive ratio for convex body chasing

Convex body chasing requires an online player to move into each newly revealed convex set. The player pays Euclidean movement while an offline comparator knows all future requests. This question asks for the optimal deterministic competitive ratio as dimension grows, up to universal constant factors. The strategy must work for arbitrary finite request sequences without knowing the horizon. The checked sources leave a gap between square-root and linear dimension dependence for general requests, with stronger results only in restricted settings.

[Read in atlas](index.html#TCS-6576) · [Online Algos: Old and New — Lecture 4: Search Problems](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf) · [Chasing Convex Bodies Optimally](https://arxiv.org/abs/1905.11968v3) · [Chasing Nested Convex Bodies Nearly Optimally](https://arxiv.org/abs/1811.00999)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6577 — Minimax dimension dependence in bandit convex optimization

What is the optimal expected regret for adversarial convex losses when only one value is observed per round? The learner competes with the best fixed point in hindsight over a known convex body. The losses lie in \([0,1]\) and are chosen before the learner’s random actions, with no smoothness assumption. General upper and lower bounds still have different polynomial dependence on dimension. Two-point, strongly convex, smooth-loss and computational-efficiency results address different guarantees.

[Read in atlas](index.html#TCS-6577) · [Bandit Convex Optimisation](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf) · [Improved Regret for Zeroth-Order Adversarial Bandit Convex Optimisation](https://arxiv.org/abs/2006.00475v3) · [Logarithmic High-Probability Regret for Online Convex Optimization with Two-Point Bandit Feedback](https://arxiv.org/abs/2603.25029v4) · [Adversarial Bandit Optimization with Globally Bounded Perturbations to Convex Losses](https://arxiv.org/abs/2606.19891v2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7317 — Randomized competitiveness of k-server

In randomized k-server, an online strategy moves k servers to serve sequential metric requests. The request sequence is fixed independently of the strategy’s random choices. The target is the infimum competitive ratio as a function of k over all finite metrics, within universal constant factors. The metric and initial placement are known and may affect the strategy and fixed additive cost. The earlier polylogarithmic question is a qualitative consequence of determining this growth, and dependence on the number of metric points cannot be hidden in the ratio.

[Read in atlas](index.html#TCS-7317) · [Randomized k-server in polynomial time](https://arxiv.org/abs/2605.01497) · [The Randomized k-Server Conjecture is False!](https://arxiv.org/abs/2211.05753)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6724 — Constant-factor related-machine precedence scheduling

The problem asks for a polynomial-time constant-factor approximation to the makespan of precedence-constrained jobs on machines with different speeds. Every job may use every machine, and its uninterrupted execution time is its processing requirement divided by the selected machine’s speed. The approximation factor must remain fixed as the number of machines and the range of speeds grow. The checked general upper bound grows logarithmically divided by an iterated logarithm, while known stronger hardness uses extra unproved hypotheses. A solution must cover arbitrary finite rational inputs in the explicitly stated deterministic bit model.

[Read in atlas](index.html#TCS-6724) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/book.pdf) · [Scheduling to Minimize Total Weighted Completion Time via Time-Indexed Linear Programming Relaxations](https://arxiv.org/abs/1707.08039) · [On the Hardness of Scheduling With Non-Uniform Communication Delays](https://par.nsf.gov/servlets/purl/10342245) · [Communication-aware scheduling of precedence-constrained tasks on related machines](https://doi.org/10.1016/j.orl.2023.11.001) · [Communication-Aware Scheduling of Precedence-Constrained Tasks on Related Machines](https://arxiv.org/abs/2004.14639v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-5030 — Optimal randomized competitive ratio of weighted k-server

Weighted k-server assigns a separate movement-cost multiplier to each server. All distinct locations are at unit distance, isolating uncertainty about which weight to move. The target is the optimal randomized competitive ratio as a function of the number of servers. It takes the worst case over finite metric sizes and arbitrary positive weights against oblivious requests. The recent \(\exp (O(k^{2}))\) upper bound removes the old doubly-exponential barrier but leaves a substantial gap above exponential lower bounds.

[Read in atlas](index.html#TCS-5030) · [A Decomposition Approach to the Weighted k-Server Problem](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.6) · [Weighted k-Server Admits an Exponentially Competitive Algorithm](https://doi.org/10.1137/1.9781611978971.154) · [The Randomized Competitive Ratio of Weighted k-server is at Least Exponential](https://doi.org/10.4086/toc.2022.v018a023)
Existing status: `open` · Summary written: 2026-09-12

### TCS-0935 — Unit-job precedence scheduling complexity

Unit-job precedence scheduling assigns equal-duration tasks to machines while respecting a partial order of dependencies. The source asks about the computational complexity of this restricted scheduling setting. Equal durations remove numerical variability but leave the problem of choosing which available jobs to run together. A classification would show how much difficulty arises from precedence structure alone. The saved label does not preserve the number of machines, time-horizon objective, or restrictions on the dependency graph, so it cannot be read as one universal hardness or tractability claim.

[Read in atlas](index.html#TCS-0935) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#complexity-of-makespan-scheduling-of-unit-jobs-with-precedence-constraints)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7335 — Randomized competitive ratio of list update

Accessing a list item costs its current position. The algorithm may rearrange the list under specified free-move and paid-swap rules. Performance is compared with an offline algorithm starting from the same order. The best randomized competitive ratio lies between 1.5 and 1.6 in the cited source. The numerical benchmark asks for a certified approximation of the optimal constant.

[Read in atlas](index.html#TCS-7335) · [List Update with Prediction](https://ojs.aaai.org/index.php/AAAI/article/download/33694/35849)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6836 — Adaptive regret in misspecified linear bandits

The question asks for one bandit policy that adapts to unknown error in a linear reward model. It must exploit accurate features while simultaneously obeying a uniform fallback bound when those features fit poorly. The model has finitely many indexed arms, independent Gaussian observation noise and a known feature matrix of arbitrary geometry. The displayed tradeoff comes from an explicit speculation in Bandit Algorithms, while later papers prove closely related partial guarantees. The formulation is now precise, but the current openness of the complete simultaneous bound remains uncertain.

[Read in atlas](index.html#TCS-6836) · [Bandit Algorithms](https://tor-lattimore.com/downloads/book/book.pdf) · [Learning with Good Feature Representations in Bandits and in RL with a Generative Model](https://sites.ualberta.ca/~szepesva/papers/ICML2020_goodfeatures.pdf) · [Upper Confidence Bounds for Combining Stochastic Bandits](https://arxiv.org/abs/2012.13115v1) · [Dynamic Regret for Non-Stationary Linear Bandits via Misspecification Reductions](https://arxiv.org/abs/2607.02891v1)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-0711 — Model Selection for Contextual Bandits

A contextual bandit learner observes a context, chooses an action, and receives feedback only for that action. Model selection asks the learner to adapt to the best class in a sequence of candidate policy classes. The source seeks regret guarantees that reflect the complexity of that best class without requiring it to be chosen in advance. Unlike supervised model selection, exploration determines which losses can be observed and compared. The challenge is to combine reliable adaptation across model sizes with efficient data collection, so that a large available class does not always impose its full learning cost.

[Read in atlas](index.html#TCS-0711) · [COLT / PMLR](https://proceedings.mlr.press/v125/foster20a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0922 — Generalized assignment

Generalized assignment allocates jobs to machines subject to assignment-dependent resource use and costs or values. The saved source entry asks about this broad allocation problem. The same job may be attractive on one machine and expensive or infeasible on another. Sharper algorithms would clarify how effectively capacity constraints and heterogeneous assignment preferences can be reconciled. The inherited title does not specify minimization versus maximization, approximation allowance, or budget conventions, so the draft cannot substitute a particular standard variant for the missing source question.

[Read in atlas](index.html#TCS-0922) · [Scheduling](https://doi.org/10.4230/DagRep.6.2.97)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0715 — Efficient Online Sparse Regression

Online sparse regression models prediction when computing every feature of an example is too expensive. On each round, the learner may inspect only k of d features before making a real-valued prediction and incurring squared loss. Its benchmark is the best fixed k-sparse linear predictor satisfying the source's norm bound. The question asks for polynomial-time algorithms achieving sublinear regret in this restricted-observation model. The difficulty is simultaneously discovering useful features and predicting accurately, while competing with a sparse predictor whose relevant coordinates are known only after the sequence is seen.

[Read in atlas](index.html#TCS-0715) · [COLT / PMLR](https://proceedings.mlr.press/v35/kale14b.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0708 — Order Optimal Regret Bounds for Kernel-Based Reinforcement Learning

Kernel-based reinforcement learning uses a reproducing kernel Hilbert space to represent nonlinear structure in a Markov decision process. The source asks for regret guarantees that match the best possible order in the relevant horizon and kernel-complexity parameters. This setting extends linear models while retaining more structure than an arbitrary nonlinear function class. The challenge is that uncertainty in prediction must be propagated through sequential decisions and future values. Sharp guarantees would identify when the expressive power of kernels can be used without paying avoidable exploration costs in reinforcement learning.

[Read in atlas](index.html#TCS-0708) · [COLT / PMLR](https://proceedings.mlr.press/v247/vakili24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0700 — Hardness of Correlated Prophet Inequality

A correlated stopping problem reveals random values sequentially and pays the value accepted when the policy stops. The source considers a hidden scenario chosen uniformly from a finite list, each scenario specifying independent draws from known finite-support distributions. It asks whether the optimal online policy can be computed in time polynomial in the numbers of scenarios, positions, and support values. The easier case of deterministic scenarios admits compact backward induction, but uncertain observations can produce many distinct posterior states. Efficient approximation is the alternative target if exact policy computation proves intractable.

[Read in atlas](index.html#TCS-0700) · [Approximation Algorithms for Stochastic Optimization](https://doi.org/10.4230/DagRep.15.3.159)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0716 — Online Local Learning

Online local learning predicts labels for small groups of items while competing with a single global labeling of the whole universe. Finding the globally best explanation can be computationally hard, even when each individual prediction concerns only a few variables. The source asks how generally efficient local prediction can avoid that global inference difficulty. Its model reveals a subset on each round and evaluates the learner's proposed labeling through a local payoff. A sharp regret guarantee would show when coherent performance can be achieved through local decisions without explicitly recovering the latent global structure.

[Read in atlas](index.html#TCS-0716) · [COLT / PMLR](https://proceedings.mlr.press/v35/christiano14.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1241 — Sublogarithmic competitiveness for online metric TSP

In online metric traveling salesperson problems, arriving points must be inserted into an evolving tour while preserving earlier ordering decisions. An array formulation also limits how much unused space is available for future insertions. The extracted question asks whether the classical logarithmic competitive ratio can be improved even when this space restriction is removed. Thus the obstacle persists beyond tight array capacity and concerns the underlying irreversible tour construction. A better guarantee would establish that online geometric ordering can approach the offline tour more closely than the long-standing insertion bound suggests.

[Read in atlas](index.html#TCS-1241) · [Online Metric TSP: Beyond the \(\sqrt{n}\) Barrier](https://doi.org/10.4230/LIPIcs.ICALP.2026.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1529 — One forecaster with the optimal regret rate for every proper loss

One online forecaster must issue predictions before knowing which proper loss a downstream user cares about. The question asks it to match each loss’s own optimal regret rate up to logarithmic factors in the horizon. The benchmark is the best fixed probability prediction in hindsight, with expectation over the forecaster’s randomness. The source already combines logarithmic regret for smooth losses with nearly square-root regret for all bounded proper losses. The remaining task is to adapt to the individually optimal rate of every bounded proper loss.

[Read in atlas](index.html#TCS-1529) · [Toward Simultaneously Optimal Regret in U-Calibration](https://proceedings.mlr.press/v336/frongillo26a.html) · [Toward Simultaneously Optimal Regret in U-Calibration — version record](https://arxiv.org/abs/2606.18527)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4983 — Sublinear competitive ratio for randomized k-server

The randomized k-server problem serves sequential metric requests while paying for movement of k available servers. The source asks whether arbitrary metrics admit a competitive ratio growing strictly slower than k. Bounds obtained through tree embeddings may depend on the number of metric points, so they do not automatically provide the requested dependence on k alone. The paper separately addresses implementing randomized strategies in polynomial time. The central question would establish a universal asymptotic advantage of randomization over the linear-in-k deterministic barrier, without restricting the metric's geometry or size.

[Read in atlas](index.html#TCS-4983) · [Randomized k-Server in Polynomial Time](https://doi.org/10.4230/LIPIcs.ICALP.2026.65)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5221 — Sublinear-in-q prophet inequalities for q-matroid intersection

A matroid-intersection prophet problem observes random element values sequentially and chooses a set independent in each of q matroids. The comparator sees all values before selecting its feasible set. The source asks whether approximation factors growing linearly in q can be improved asymptotically. It also highlights restricted instances with partition matroids, symmetric constraints, and identical Bernoulli values. Its strengthened lower bounds leave a gap, so the task is to determine how much of the loss is forced by intersecting many independence systems and how much is due to current online selection methods.

[Read in atlas](index.html#TCS-5221) · [An Improved Lower Bound for Matroid Intersection Prophet Inequalities](https://doi.org/10.4230/LIPIcs.ITCS.2023.95)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5252 — Action-set-dependent regret in bandit combinatorial optimization

Bandit combinatorial optimization chooses structured subsets and observes only the total loss of the chosen subset. The source asks which properties of the particular action set determine its optimal regret. General bounds in ambient dimension and subset size may ignore substantial structure shared by the feasible actions. For shortest-path actions, the question becomes identifying graph properties that control learning difficulty, including on a simple directed grid. A characterization would replace worst-case guarantees over all action systems with bounds that explain why one specific combinatorial decision problem is easier than another.

[Read in atlas](index.html#TCS-5252) · [Tight Bounds for Bandit Combinatorial Optimization](https://proceedings.mlr.press/v65/cohen17a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5779 — Constant-factor online contention resolution for matroids

A contention-resolution scheme chooses an independent subset from a random set of active matroid elements. The source allows arbitrary correlations in that active set, rather than assuming each element appears independently. It asks for a universal online scheme that competes within a constant factor of the best corresponding offline balance guarantee without assuming the matroid secretary conjecture. Positive correlations can defeat methods designed for product distributions even when offline selection is easy. The problem seeks a robust selection principle that separates difficulty caused by arrival order from difficulty already present in the input distribution.

[Read in atlas](index.html#TCS-5779) · [The Outer Limits of Contention Resolution on Matroids and Connections to the Secretary Problem](https://doi.org/10.4230/LIPIcs.ICALP.2020.42)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6078 — Pinwheel Packing in NP

Pinwheel scheduling requires tasks to receive service repeatedly within prescribed recurrence limits. The cited source studies a packing version of this perpetual scheduling problem. The saved question asks whether Pinwheel Packing belongs to NP, while recording a PSPACE upper bound from earlier work. Membership would require polynomially checkable finite evidence despite the potentially infinite schedule being described. The excerpt does not define the packing rules or certificate format, and its historical upper bound is retained as source context rather than independently verified current status.

[Read in atlas](index.html#TCS-6078) · [Hardness and Fixed Parameter Tractability for Pinwheel Scheduling Problems](https://doi.org/10.4230/LIPIcs.ISAAC.2025.47)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6721 — Additive-one approximation for bin packing

Bin packing assigns indivisible items of known sizes to bins of unit capacity. The goal is to find a packing that uses at most one bin more than the minimum possible. The algorithm must run in polynomial time in the complete binary input length. Known general algorithms achieve a logarithmic additive loss, while approximation schemes do not guarantee one extra bin. The question asks how closely efficient computation can approach the exact optimum of a fundamental packing problem.

[Read in atlas](index.html#TCS-6721) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/) · [A Logarithmic Additive Integrality Gap for Bin Packing](https://doi.org/10.1137/1.9781611974782.172)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6838 — Instance-optimal finite-time best-arm identification

Best-arm identification spends samples to recommend a good arm, rather than to maximize reward during exploration. The source asks for finite-time guarantees matching its information-theoretic lower bounds and for instance-dependent bounds on simple regret. Simple regret measures the reward gap of the final recommendation, making it sensitive to how costly a particular mistake is. The source also proposes understanding the distribution of that gap, beyond just its expectation. These questions would connect asymptotically optimal exploration rules with the quality and reliability of recommendations produced under an actual finite sampling budget.

[Read in atlas](index.html#TCS-6838) · [Bandit Algorithms](https://banditalgs.com/)
Existing status: `source_open` · Summary written: 2026-09-11

## Beyond worst-case and average-case analysis (12)

### TCS-6656 — Planted clique conjecture

A detector receives one random graph and must tell whether a uniformly chosen set of exactly k vertices was made into a clique. The selected conjecture excludes a uniform randomized polynomial-time detector with balanced success at least two thirds at all sufficiently large sizes when k is a fixed power below the square-root scale. The input, all sources of randomness, the complete bit-time clock and the precise order of quantifiers are specified. Known recovery algorithms reach the square-root scale, while sum-of-squares integrality gaps and other method restrictions do not exclude every detector. Conditional distinguishing results and newer inference reductions remain evidence about the hypothesis, with differing planting conventions and guarantees identified explicitly.

[Read in atlas](index.html#TCS-6656) · [Computational lower bounds in latent models: clustering, sparse-clustering, biclustering](https://arxiv.org/abs/2506.13647v1) · [Finding a Large Hidden Clique in a Random Graph](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf) · [A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem](https://doi.org/10.1137/17M1138236) · [Finding planted cliques using gradient descent](https://arxiv.org/abs/2311.07540v2) · [On optimal distinguishers for Planted Clique](https://arxiv.org/abs/2505.01990v2) · [Robust Algorithms for Finding Cliques in Random Intersection Graphs via Sum-of-Squares](https://proceedings.mlr.press/v336/gobel26a.html) · [Average-case hardness of Betti number estimation](https://arxiv.org/abs/2609.12777v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0012 — Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)

Worst-case NP hardness means that some efficiently verifiable problem resists polynomial-time solution on all inputs. The question asks whether P unequal to NP forces such a problem to remain hard on average under an efficiently samplable distribution. The hard instances must occur often enough in a distribution that can itself be generated feasibly. A positive implication would connect worst-case complexity with the distributional hardness needed in many algorithmic and cryptographic settings. The reviewed target uses deterministic exact decisions and Levin's moment-based average-time definition, which differs from allowing errors on rare inputs or requiring only a polynomial first moment.

[Read in atlas](index.html#TCS-0012) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf) · [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2026.97)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6657 — Computational threshold for tensor PCA

Dense tensor PCA observes a hidden rank-one tensor corrupted by independent Gaussian noise. The conjecture says that below a specified signal scale, no polynomial-time algorithm can recover a vector with constant correlation to the hidden direction. It asks about unrestricted computation rather than the performance of a particular spectral, gradient, or low-degree method. Resolving the threshold would clarify a prominent proposed gap between statistical recoverability and computational feasibility. The saved formulation fixes finite precision, unit-sphere normalization, one observation, and independent ordered noise entries, so results using different normalizations or extra samples require careful conversion.

[Read in atlas](index.html#TCS-6657) · [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076) · [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html) · [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735) · [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329) · [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6684 — Computational Kesten–Stigum threshold

The symmetric stochastic block model generates a sparse graph with higher edge probability within hidden communities than between them. The question asks whether some fixed parameters below the Kesten–Stigum threshold permit polynomial-time weak recovery. Weak recovery means a constant improvement over chance after relabeling the output communities optimally. A positive example would cross a proposed computational threshold in a setting where information can persist beyond simple spectral methods. The reviewed model keeps the number of communities and edge parameters fixed, so results with growing community counts or only restricted-algorithm lower bounds do not settle it.

[Read in atlas](index.html#TCS-6684) · [Detection in the stochastic block model with multiple clusters: proof of the achievability conjectures, acyclic BP, and the information-computation gap](https://arxiv.org/abs/1512.09080) · [Information-theoretic thresholds for community detection in sparse networks](https://proceedings.mlr.press/v49/banks16.html) · [Low degree conjecture implies sharp computational thresholds in stochastic block model](https://arxiv.org/abs/2502.15024) · [Stochastic block models with many communities and the Kesten–Stigum bound](https://arxiv.org/abs/2503.03047)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6453 — Infinitely-often one-way functions from average-case NP hardness

Average-case NP hardness says that some efficiently sampled verification problem defeats the specified randomized heuristic schemes. The question asks whether this implies a polynomial-time function that is hard to invert at infinitely many input lengths. Such a result would connect distributional decision hardness with a basic cryptographic form of computational asymmetry. The security target quantifies separately over every polynomial-time inverter and every inverse-polynomial success threshold. The saved formulation deliberately uses infinitely-often security, so a claim of hardness at all sufficiently large lengths would be stronger than the implication being asked about.

[Read in atlas](index.html#TCS-6453) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6658 — Polynomial smoothed complexity of FLIP for Max-Cut

Does FLIP for Max-Cut have polynomial expected path length on every graph under independent bounded-density edge weights? Each step moves just one vertex and must strictly increase the cut weight. The expectation controls the longest path after the weights are sampled, including all starting cuts and improving choices. Polynomial bounds for sparse graph families and a general high-probability bound do not finish this target. The known smoothed superpolynomial example permits three-vertex moves, while its single-vertex analogue is unperturbed.

[Read in atlas](index.html#TCS-6658) · [Local Max-Cut on Sparse Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.98) · [Smoothed complexity of local Max-Cut and binary Max-CSP](https://arxiv.org/abs/1911.10381) · [Superpolynomial smoothed complexity of 3-FLIP in Local Max-Cut](https://people.maths.ox.ac.uk/michel/Papers/smoothed-complexity-local-max-cut-3-flip.pdf)
Existing status: `open` · Summary written: 2026-09-11

### TCS-5011 — Algorithmic threshold for the symmetric binary perceptron

The symmetric binary perceptron seeks a sign vector satisfying many random Gaussian two-sided constraints. The conjecture places the efficient-search density at the scale of the squared margin, allowing fixed powers of its reciprocal logarithm. The card defines a supremum over uniform polynomial-time algorithms and states its exact real-arithmetic convention. The input dimension tends to infinity at each fixed margin and density before the margin approaches zero. Stable-algorithm barriers, a sign-matrix algorithm and conditional lattice reductions each have limits that prevent treating them as a full resolution.

[Read in atlas](index.html#TCS-5011) · [Algorithms and Barriers in the Symmetric Binary Perceptron Model](https://doi.org/10.1109/FOCS54457.2022.00061) · [Symmetric Perceptrons, Number Partitioning and Lattices](https://arxiv.org/abs/2501.16517) · [Parametric RDT approach to computational gap of symmetric binary perceptron](https://arxiv.org/abs/2601.10628)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4876 — Algorithmic threshold for random k-SAT

The input is a random conjunction of fixed-width clauses, with all literal positions sampled independently. The algorithm must find an assignment satisfying every clause with probability tending to one. The conjectured leading threshold is two to the clause width times its natural logarithm, divided by the width. Known algorithms reach this scale, while satisfying assignments exist at substantially higher densities. Existing overlap-gap and low-degree barriers do not establish optimality against every polynomial-time algorithm.

[Read in atlas](index.html#TCS-4876) · [Sharp Thresholds for the Overlap Gap Property: Ising p-Spin Glass and Random k-SAT — full version](https://arxiv.org/abs/2309.09913) · [A Better Algorithm for Random k-SAT](https://doi.org/10.1137/09076516X) · [The Algorithmic Phase Transition of Random k-SAT for Low Degree Polynomials](https://arxiv.org/abs/2106.02129)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5406 — Optimization and certification in sparse random CSPs

A sparse random constraint-satisfaction instance can have a predictable asymptotic optimum even when proving its exact value is difficult. The source distinguishes efficiently finding a nearly optimal assignment from efficiently certifying that no assignment is substantially better. Its question asks how close algorithms can come to both goals in specified random models. Semidefinite relaxations supply computable certificates, but their typical value may exceed the actual combinatorial optimum. Understanding this gap would reveal whether constructing good solutions and certifying their quality have different computational thresholds on random optimization instances.

[Read in atlas](index.html#TCS-5406) · [The SDP Value of Random 2CSPs](https://doi.org/10.4230/LIPIcs.ICALP.2022.97)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6702 — Worst-case-to-average-case reductions within NP

Worst-case-to-average-case reductions aim to turn the difficulty of some inputs into difficulty on a substantial fraction of a samplable distribution. The source asks for suitable reductions that remain within NP. Staying inside NP preserves efficient verification of witnesses while attempting to distribute hardness more broadly. A successful construction would connect basic worst-case assumptions to the distributional hardness used in pseudorandomness and related areas. The saved survey note does not preserve the input distribution, reduction type, or hardness fraction, so those parameters must be recovered before the broad direction becomes one exact implication.

[Read in atlas](index.html#TCS-6702) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6703 — Optimal exponential-scale hardness amplification in NP

Hardness amplification strengthens a problem that is mildly hard on average into one that is hard on nearly all inputs. The source asks for optimal exponential-scale amplification while keeping the resulting problem in NP. The NP requirement constrains which encodings and combinations can be used without losing efficiently verifiable witnesses. An optimal result would sharpen the quantitative route from weak average-case hardness to strong pseudorandomness consequences. The saved note omits the starting advantage, output length, and target error exponent, so these must be restored before optimality can be judged against a specific amplification bound.

[Read in atlas](index.html#TCS-6703) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7148 — Smoothed simplex complexity under sparse perturbations

Smoothed simplex analysis bounds the expected running time after random perturbations of a linear program. The source asks whether polynomial guarantees can be extended to perturbations that preserve sparsity. Preserving zero patterns restricts the randomness available to remove geometric degeneracies, so dense-noise arguments may no longer apply. A solution would make smoothed analysis more relevant to linear programs whose efficient representation depends on having few nonzero coefficients. The saved note does not choose a simplex pivot rule or sparse perturbation distribution, so those model details must be recovered before stating a complete polynomial-time guarantee.

[Read in atlas](index.html#TCS-7148) · [Beyond Worst-Case Analysis](https://arxiv.org/abs/1806.09817)
Existing status: `source_open` · Summary written: 2026-09-11

## Sampling, Markov chains and mixing times (9)

### TCS-6621 — Rapid mixing of Glauber dynamics with \(\Delta +2\) colours

Glauber dynamics samples graph colorings by repeatedly selecting a vertex and choosing a color allowed by its neighbors. The reviewed question asks for polynomial-time convergence to the uniform distribution whenever the palette has at least two more colors than the maximum degree. That amount of slack makes the state space connected, but connectivity alone does not exclude bottlenecks that trap a random walk. A universal mixing bound would show that the simplest local sampler works throughout this universally convergent range. The saved progress covers restricted graph classes or larger relative color slack, whose parameter dependence does not establish the additive two-color target for every graph.

[Read in atlas](index.html#TCS-6621) · [Glauber dynamics for colourings of chordal graphs and graphs of bounded treewidth](https://arxiv.org/abs/2010.16158) · [Sampling Colorings with Fixed Color Class Sizes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134) · [Flip Dynamics for Sampling Colorings: Improving \((11/6- \varepsilon )\) Using a Simple Metric](https://arxiv.org/abs/2407.04870) · [Sampling Colorings Close to the Maximum Degree: Non-Markovian Coupling and Local Uniformity](https://arxiv.org/abs/2604.11938) · [A Spectral Local-to-Global Principle for Spin Systems on Graphs with Girth At Least Five](https://arxiv.org/abs/2608.25491)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6622 — Kannan–Tetali–Vempala conjecture

The lazy switch chain samples binary matrices while preserving every row and column sum. Each attempted move chooses a two-by-two rectangle and may exchange its two checkerboard patterns. The target is polynomial convergence to the uniform distribution for every feasible choice of margins and every starting matrix. Fu, Qin and Wang’s July 2026 preprint states an explicit bound meeting this target and supplies a Lean formalization. The card records that claimed resolution with uncertain status because its proof and formalization were not independently verified here.

[Read in atlas](index.html#TCS-6622) · [Speeding up Switch Markov Chains for Sampling Bipartite Graphs with Given Degree Sequence](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2018.36) · [Spectral Gap for the Binary Fixed-Margin Swap Chain](https://arxiv.org/abs/2606.22636v2) · [KTV Proof Formalization](https://github.com/guanyangwang/ktv-swap-lean)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6668 — Polynomial mixing of critical three-dimensional Ising dynamics

This question concerns local heat-bath sampling of the Ising model at the critical point of the infinite cubic lattice. The finite system is a three-dimensional box with free boundaries and zero external field. It asks whether every initial spin configuration becomes close to equilibrium after polynomially many individual updates. The critical inverse temperature is specified by the infinite-volume magnetization threshold, without relying on a numerical estimate. Known critical results in other dimensions and at the regular-tree threshold do not settle this three-dimensional lattice problem.

[Read in atlas](index.html#TCS-6668) · [Log-Sobolev inequality for near critical Ising models](https://doi.org/10.1002/cpa.22172) · [Polynomial Mixing of the critical Glauber Dynamics for the Ising Model](https://arxiv.org/abs/2411.10318)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6839 — Polynomial mixing of planar Ising dynamics with plus boundaries

Fixing plus spins around a planar Ising box selects a boundary phase while the interior spins evolve randomly. The question asks whether local heat-bath updates mix in polynomial time at every fixed positive temperature. The bound must hold from every interior starting configuration, including the all-minus state. Polynomial constants may depend on temperature but cannot grow with the box size. The checked 2026 source retains this question while improving quasipolynomial mixing and proving rapid ordering from more favorable initializations.

[Read in atlas](index.html#TCS-6839) · [Markov Chains and Mixing Times, Second Edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) · [Quasi-polynomial mixing of the 2D stochastic Ising model with “plus” boundary up to criticality](https://arxiv.org/abs/1012.1271) · [Rapid phase ordering of Ising dynamics on \(\mathbb Z^2\)](https://arxiv.org/abs/2605.08052)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6843 — Cutoff for bounded-degree transitive expanders

Expander graphs are sparse graphs on which random walks mix rapidly. This question asks whether vertex symmetry forces a sharp transition to equilibrium in every bounded-degree expander sequence. The model uses a lazy walk, a uniformly positive spectral gap and graph sizes tending to infinity. Cutoff requires the mixing times at any two fixed total-variation accuracy levels to become asymptotically equal. The checked Ramanujan theorem covers a special spectral regime, while the 2025 source retains the general conjecture.

[Read in atlas](index.html#TCS-6843) · [Markov Chains and Mixing Times, Second Edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) · [Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon](https://arxiv.org/abs/2508.21055) · [Cutoff on all Ramanujan graphs](https://arxiv.org/abs/1507.04725)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-2861 — Weakly negatively regressive sampling of matroid bases

The problem asks for efficient sampling of a matroid basis with any prescribed rational point of the base polytope as its exact marginal vector. The output law must satisfy weak negative regression for every increasing function of all coordinates except one. The chosen model uses an independence oracle and a uniform exact sampler with expected polynomial bit complexity. This dependence property implies favorable submodular expectations and supports known concentration guarantees. A reported gap in an older general-matroid claim remains acknowledged in the 2026 literature, while newer special-case rounding results do not settle this target.

[Read in atlas](index.html#TCS-2861) · [Submodular Dominance and Applications](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2022.44) · [Concentration of Submodular Functions and Read-k Families Under Negative Dependence](https://doi.org/10.1007/s00453-026-01372-w) · [Dimension-Free Correlated Sampling for the Hypersimplex](https://doi.org/10.4230/LIPIcs.ITCS.2026.104)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6840 — Monotonicity of Ising spectral gaps

A ferromagnetic Ising model favors neighboring spins that agree. This question asks whether increasing its interactions always reduces the spectral gap of local heat-bath updates. The graph has a fixed vertex set, arbitrary nonnegative edge strengths and no external field. The spectral gap is defined from the exact transition matrix and measures the relaxation rate. The checked cycle and equal-coupling complete-graph theorems do not cover independent interaction changes on arbitrary graphs.

[Read in atlas](index.html#TCS-6840) · [Markov Chains and Mixing Times, Second Edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) · [Glauber dynamics on the cycle is monotone](https://arxiv.org/abs/math/0305056) · [Relaxation time is monotone in temperature in the mean-field Ising model](https://arxiv.org/abs/1103.0327) · [Spectral gap and curvature of monotone Markov chains](https://arxiv.org/abs/2305.04688)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6857 — Mixing of the self-avoiding-walk pivot chain

A self-avoiding walk models a polymer whose lattice vertices cannot overlap. The pivot chain samples such walks by rotating or reflecting a tail and rejecting intersections. This card asks for matching asymptotic bounds on its worst-state total-variation mixing time on the square lattice. Time counts every proposed pivot, including rejected attempts, with a fixed distribution over five symmetries. Efficient implementations and observed decorrelation do not by themselves determine this mixing-time order.

[Read in atlas](index.html#TCS-6857) · [Markov Chains and Mixing Times, Second Edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) · [Efficient implementation of the pivot algorithm for self-avoiding walks](https://arxiv.org/abs/1005.1444)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6851 — Deterministic approximation scheme for graph cover times

The cover time is the expected number of random-walk steps needed to visit every vertex. This card asks for a deterministic approximation scheme from any specified starting vertex of an arbitrary connected graph. For each fixed relative accuracy, the runtime must be polynomial in graph size. The original source asks for approximation, so the imported demand for exact output has been corrected. Known constant-factor and restricted-family results do not provide the full all-graph guarantee stated here.

[Read in atlas](index.html#TCS-6851) · [Reversible Markov Chains and Random Walks on Graphs](https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch6.S8.html#SS3) · [Markov Chains and Mixing Times, Second Edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) · [Cover times, blanket times, and majorizing measures](https://annals.math.princeton.edu/2012/175-3/p08) · [Deterministic approximation for the cover time of trees](https://cims.nyu.edu/~zeitouni/pdf/feigezeitouni3.pdf) · [A polynomial time approximation scheme for computing the supremum of Gaussian processes](https://arxiv.org/abs/1202.4970)
Existing status: `source_open` · Summary written: 2026-09-14

## Counting and enumeration (16)

### TCS-6628 — FPRAS for counting perfect matchings

A perfect matching pairs every vertex of a graph with exactly one neighbor. The question asks for one randomized algorithm giving arbitrarily accurate relative estimates of their number on every finite unweighted simple graph. Its worst-case running time must be polynomial in the full input length and inverse accuracy, with success probability at least three quarters for each input. Bipartite perfect matchings and all matchings have approximation schemes, but the checked 2026 dense-graph and permanent results retain restrictions absent from this target. A complete Lean proof must establish such a uniform scheme with exact zero behavior or prove that no scheme meeting all requirements exists.

[Read in atlas](index.html#TCS-6628) · [Approximating the Permanent](https://webspace.maths.qmul.ac.uk/m.jerrum/papers/SIAMperm.pdf) · [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://people.eecs.berkeley.edu/~sinclair/perm2.pdf) · [On Counting Perfect Matchings in General Graphs](https://arxiv.org/abs/1712.07504v1) · [Two-State Spin Systems with Negative Interactions](https://arxiv.org/abs/2309.04735v3) · [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599v1) · [Diffuse Gaussian Truncation For Deterministic Approximate Counting](https://arxiv.org/abs/2609.04079v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7221 — FPRAS for #BIS

The #BIS problem counts all independent vertex subsets of an arbitrary finite simple bipartite graph, including the empty set. The question asks for one uniform randomized bit algorithm with polynomial runtime in the complete input length and inverse requested relative accuracy, succeeding with probability at least three quarters on every instance. Acceptance requires a full Lean-checked construction with an every-random-tape runtime bound, or a proof excluding every such scheme without an unresolved extra assumption. The problem represents a central approximation class whose apparent intermediate complexity is not settled by hardness of exact counting. The checked2026 literature still leaves the total count open, while typical regular inputs, dense regular graphs and balanced or fixed-size counts have distinct known results.

[Read in atlas](index.html#TCS-7221) · [A Fixed-Parameter Perspective on #BIS](https://link.springer.com/article/10.1007/s00453-019-00606-4) · [Counting Independent Sets and Colorings on Random Regular Bipartite Graphs](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.34) · [A Spectral Approach to Approximately Counting Independent Sets in Dense Bipartite Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.35) · [Computational Thresholds for Balanced and Fixed-Slice Independent Sets in Bipartite Graphs](https://arxiv.org/abs/2608.02503v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6629 — Deterministic FPTAS for the nonnegative permanent

The permanent of a nonnegative matrix sums the weights of all perfect matchings in its bipartite support graph. The question asks for one deterministic algorithm approximating this value to any requested relative accuracy on every nonnegative rational matrix. Its running time must be polynomial in the full binary input length and inverse accuracy, with a fixed exponent and exact output zero when the permanent is zero. Randomized approximation is established, while checked 2026 deterministic results have dimension-dependent error factors or fixed density and weight restrictions. A complete Lean proof must establish the unrestricted deterministic scheme or prove that none meets the stated guarantees.

[Read in atlas](index.html#TCS-6629) · [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://people.eecs.berkeley.edu/~sinclair/perm2.pdf) · [A Tight Analysis of Bethe Approximation for Permanent](https://arxiv.org/abs/1811.02933v2) · [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599v1) · [Beyond the Bethe Approximation of the Permanent](https://arxiv.org/abs/2608.28031v2) · [Structural Corrections to the Bethe Approximation of the Permanent](https://arxiv.org/abs/2608.31061v1) · [Subexponential Approximation of the Permanent in Deterministic Polynomial Time](https://arxiv.org/abs/2609.10516v1) · [Diffuse Gaussian Truncation For Deterministic Approximate Counting](https://arxiv.org/abs/2609.04079v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6671 — FPRAS for counting undirected Euler tours

An Euler tour traverses every edge of an undirected graph exactly once and returns to its start. This question asks whether the number of such tours can be approximated by a randomized algorithm in fully polynomial time. The count uses labelled edges and a fixed first traversal to remove rotation and reversal ambiguity. The accuracy is multiplicative, and the success probability must be at least three quarters on every input. Known orientation-counting algorithms and restricted graph results do not resolve the general tour-counting question.

[Read in atlas](index.html#TCS-6671) · [Euler-tours of low-height toroidal grids](https://sites.cs.st-andrews.ac.uk/scm2024/abstracts.html) · [The Complexity of Counting Eulerian Tours in 4-regular Graphs](https://www.cs.rochester.edu/~stefanko/Publications-new/J25.pdf) · [Sampling and counting notes (Mixingbook)](https://www.math.cmu.edu/~af1p/Mixingbook.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7112 — Output-polynomial hypergraph transversal enumeration

A transversal meets every edge of a hypergraph and is minimal if removing any selected vertex destroys that property. The required algorithm lists all such sets exactly once and detects when enumeration is finished. Its total time must be polynomial in the combined input and complete output length. The output may be exponentially large, and no separate bound on delay is requested. A 2026 lower bound excludes a particular practical algorithm while leaving the existence of a general output-polynomial algorithm open.

[Read in atlas](index.html#TCS-7112) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042) · [Minimal-to-Maximal Conversion Search Is Not Output-Polynomial](https://arxiv.org/abs/2608.02159)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7355 — Fully polynomial randomized approximation of mixed discriminants

The mixed discriminant is a specified coefficient of the determinant of a linear matrix pencil. Positive semidefinite inputs make this coefficient nonnegative. An FPRAS must approximate it to arbitrary relative accuracy in time polynomial in the input size and inverse accuracy. Nonnegative permanent approximation addresses a special diagonal case but does not settle the general matrix target. A resolution would decide a central frontier connecting approximate counting and constrained determinantal sampling.

[Read in atlas](index.html#TCS-7355) · [A polynomial time algorithm to approximate the mixed volume within a simply exponential factor](https://eccc.weizmann.ac.il/report/2007/037/revision/1/) · [On the Complexity of Constrained Determinantal Point Processes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3037 — Parity subgraph-counting dichotomy

The problem asks which graph-pattern families make counting copies modulo two parameterized-hard. The proposed boundary is whether deleting a bounded number of pattern vertices always leaves only edges and isolated vertices. Every computable class on the unbounded side is conjectured equivalent to parity clique under deterministic fixed-parameter Turing reductions. Copies are ordinary unlabelled subgraphs, and the input pattern size is the parameter. The classification is known for hereditary classes and classes of trees, while the general class-wide assertion remains the target.

[Read in atlas](index.html#TCS-3037) · [Modular Counting of Subgraphs: Matchings, Matching-Splittable Graphs, and Paths](https://doi.org/10.4230/LIPIcs.ESA.2021.34) · [Parameterised and Fine-Grained Subgraph Counting, Modulo 2](https://doi.org/10.1007/s00453-023-01178-0)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1004 — Deterministic relative counting for DNF

A DNF formula describes a union of sets of Boolean assignments, one set for each conjunction. The question asks for deterministic relative approximation of the number of assignments in that union. One uniform algorithm must run in time polynomial in the explicit formula size and reciprocal error. The estimate must count assignments once despite overlapping terms and must be exactly zero for an unsatisfiable formula. Randomized schemes and deterministic algorithms for restricted formulas leave the general fully polynomial target unresolved in the checked sources.

[Read in atlas](index.html#TCS-1004) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [A Note on Deterministic Approximate Counting for k-DNF](https://eccc.weizmann.ac.il/report/2002/069/) · [Pseudorandomness for read-k DNF formulas](https://www.cs.columbia.edu/~rocco/Public/read-k.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3635 — Treewidth classification of approximate counting CSP

The input asks how many homomorphisms map a source structure A from a fixed class C into an arbitrary target structure B. The conjecture says a fixed-parameter randomized approximation scheme exists exactly when C has bounded Gaifman treewidth. Relation arity is uniformly bounded, C is recursively enumerable, and the parameter is the size of A. The source proves this under a further fan-class condition and asks to remove it. The 2020 journal version retains that restriction, so exact-counting and fixed-target classifications do not settle the missing approximation direction.

[Read in atlas](index.html#TCS-3635) · [Approximate Counting CSP Seen from the Other Side](https://doi.org/10.4230/LIPIcs.MFCS.2019.60) · [Approximate Counting CSP Seen from the Other Side](https://doi.org/10.1145/3389390) · [Counting List Homomorphisms from Graphs of Bounded Treewidth: Tight Complexity Bounds](https://doi.org/10.1145/3640814)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4671 — Decision versus approximate counting for fixed-width SAT

A fixed-width CNF formula has a finite number of satisfying assignments. Decision tests whether that number is positive; approximation estimates it to relative error. The question asks whether the optimal exponential rates in the variable count coincide for each fixed width. Polynomial accuracy costs and arbitrarily small losses in the exponential rate are allowed. Later all-width and subexponential equivalences do not settle this fixed-width comparison.

[Read in atlas](index.html#TCS-4671) · [An Approximation Algorithm for #k-SAT](https://doi.org/10.4230/LIPIcs.STACS.2012.78) · [Exploiting Independent Subformulas: A Faster Approximation Scheme for #k-SAT](https://doi.org/10.1016/j.ipl.2013.02.013) · [Fine-Grained Reductions from Approximate Counting to Decision](https://doi.org/10.1145/3442352)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6820 — FP versus #P

A #P function counts the accepting computation paths of a nondeterministic polynomial-time machine. The question asks whether every such counting function can be evaluated exactly in deterministic polynomial time. This would make the number of efficiently verifiable witnesses as accessible as a single ordinary polynomial-time computation. It is a central distinction between finding or verifying solutions and determining their full multiplicity. The output is a binary integer and exactness matters, so randomized relative approximation or a decision procedure for whether the count is positive would not resolve the counting-class question.

[Read in atlas](index.html#TCS-6820) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6821 — FP = #P from \(\mathrm{P} = \mathrm{NP}\)

The hypothesis \(\mathrm{P}=\mathrm{NP}\) would make existence of efficiently verifiable witnesses decidable in polynomial time. This question asks whether that hypothesis also forces exact polynomial-time computation of every #P counting function. The gap is that deciding whether a witness exists does not directly determine how many witnesses there are. Resolving the implication would clarify how much additional power exact counting can retain after decision complexity collapses. The source's standard uniform function-computation conventions must be preserved, and a method that enumerates all witnesses can still take exponential time despite a fast existence test.

[Read in atlas](index.html#TCS-6821) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7082 — OutputP versus IncP

OutputP permits total enumeration time polynomial in the input and complete output size. IncP additionally requires the initial portions of the output to arrive within incremental polynomial time. The source asks for a natural problem separating these classes and suggests a domination problem involving \(K_{t}\)-free structure. A separation would demonstrate that good total throughput can coexist with an unavoidable long wait for early answers. The candidate's precise domination condition and any assumed complexity hypothesis remain in the source, so the working summary preserves the class distinction without declaring the proposed example established.

[Read in atlas](index.html#TCS-7082) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7084 — Time–space separations in polynomial enumeration

Polynomial-delay and incremental-polynomial enumeration can use large memory to store solutions or organize future outputs. The source asks for conditional separations from the versions restricted to polynomial space. Such a separation would show that memory is an essential resource even when output timing already satisfies a strong efficiency guarantee. The difficulty is proving that every low-space strategy must suffer a timing penalty, rather than only analyzing one buffering method. The saved note does not select the underlying hypothesis or witness problem, so those must be recovered before a precise class separation can be asserted.

[Read in atlas](index.html#TCS-7084) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7086 — Incremental polynomial-time binary-matroid circuit enumeration

A circuit of a binary matroid is a minimally dependent set of columns in a representation over the two-element field. The question asks to enumerate all such circuits in incremental polynomial time while using polynomial space. The goal combines prompt production of the first several answers with a memory bound independent of the potentially exponential output. This would make a fundamental dependence structure effectively explorable without storing every circuit already encountered. The source's input representation and duplicate-handling convention remain relevant, because listing arbitrary dependent sets does not automatically yield minimal circuits with the required resource guarantees.

[Read in atlas](index.html#TCS-7086) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7099 — Finite-domain enumeration-CSP dichotomy

Enumeration CSP asks an algorithm to list every satisfying assignment of a fixed constraint language. The source asks for a dichotomy over finite-domain templates. Listing all solutions introduces delay and memory questions that ordinary satisfiability decision does not measure. A classification would explain which languages permit controlled output generation even when the total solution set is enormous. The saved note does not state the intended delay, preprocessing, or space class, so a polynomial-time decision dichotomy is only background and does not by itself determine the enumeration target.

[Read in atlas](index.html#TCS-7099) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042)
Existing status: `source_open` · Summary written: 2026-09-11

## Structural graph theory and graph algorithms (50)

### TCS-6651 — Hadwiger’s conjecture

Hadwiger’s conjecture says that a finite graph needing at least t colors always contains a complete graph on t vertices as a minor. Such a minor consists of disjoint nonempty connected vertex sets with an edge between every pair of sets. There are no parity requirements, restrictions on the sizes of these sets, or algorithmic running-time requirements. The conjecture would extend the Four-Color Theorem to an exact relation between coloring and clique minors in all finite graphs. A solution must prove the full assertion or certify a finite counterexample in Lean; the recent coloring improvement and the disproof for odd minors do not settle this target.

[Read in atlas](index.html#TCS-6651) · [Beyond Halfway to Hadwiger’s Conjecture](https://arxiv.org/abs/2609.06867v2) · [Reducing Linear Hadwiger’s Conjecture to Coloring Small Graphs](https://arxiv.org/abs/2108.01633v5) · [Hadwiger’s conjecture for K6-free graphs](https://doi.org/10.1007/BF01202354) · [Disproof of the Odd Hadwiger Conjecture](https://arxiv.org/abs/2512.20392v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6536 — Deterministic linear-time minimum spanning tree

A minimum spanning tree connects every vertex while minimizing the total weight of its edges. This project asks whether arbitrary real comparison weights admit a deterministic algorithm whose worst-case time is linear in the graph size. Randomized linear expected time and nearly linear deterministic bounds provide contrasting benchmarks. Integer operations on weight representations answer a different model-specific question. A resolution would explain whether the remaining cost comes from essential deterministic comparison work or from limitations of existing graph filtering methods.

[Read in atlas](index.html#TCS-6536) · [A Randomized Linear-Time Algorithm to Find Minimum Spanning Trees](https://people.csail.mit.edu/karger/Papers/mst.pdf) · [A Minimum Spanning Tree Algorithm with Inverse-Ackermann Type Complexity](https://www.cs.princeton.edu/~chazelle/pubs/mst.pdf) · [An Optimal Minimum Spanning Tree Algorithm](https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/An%20Optimal%20Minimum.pdf) · [Trans-dichotomous algorithms for minimum spanning trees and shortest paths](https://www.sciencedirect.com/science/article/pii/S0022000005800649) · [Minimum Spanning Tree in Deterministic Linear Time For Graphs of High Girth](https://people.csail.mit.edu/dmoshkov/papers/mst/high-girth.pdf) · [Randomized minimum spanning tree algorithms using exponentially fewer random bits](https://web.eecs.umich.edu/~pettie/papers/random-mst.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6652 — Erdős–Hajnal conjecture

The Erdős–Hajnal conjecture predicts a polynomial-size clique or independent set whenever a graph excludes one fixed induced pattern. The positive exponent may depend on that entire forbidden pattern but must work for every size and every permitted host graph. An accepted answer proves this universal assertion or refutes it for one fixed forbidden graph with a complete Lean-checked proof. General bounds and recent special-case results still fall short of the universal guarantee recorded by the checked primary literature. A revised historical full-solution claim remains unverified here, so the card distinguishes that uncertainty from the precise mathematical target.

[Read in atlas](index.html#TCS-6652) · [Ramsey-type theorems](https://mathweb.ucsd.edu/~asuk/erdos_hajnal.pdf) · [Induced subgraph density. I. A loglog step towards Erdős–Hajnal](https://arxiv.org/abs/2301.10147) · [Induced subgraph density. VII. The five-vertex path](https://arxiv.org/abs/2312.15333) · [Induced subgraph density. V. All paths approach Erdős–Hajnal](https://arxiv.org/abs/2307.15032) · [Erdős–Hajnal conjecture beyond five-vertex graphs](https://arxiv.org/abs/2606.06258) · [The Erdős–Hajnal Property for the six-vertex Graph with Edge Set \(\{ab,bc,cd,de,af,bf,df\}\)](https://arxiv.org/abs/2608.28551) · [Equivalence between Erdős–Hajnal and polynomial Rödl and Nikiforov conjectures](https://arxiv.org/abs/2403.08303) · [A Single-Exponential Erdős–Hajnal Bound for Graphs of Bounded VC-Dimension](https://arxiv.org/abs/2607.09049) · [On Induced Subgraphs of Finite Graphs not Containing Large Empty and Complete Subgraphs](https://arxiv.org/abs/1211.3876)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-6682 — Reed’s conjecture

Reed’s conjecture asks whether every finite simple undirected graph has a proper colouring using at most the rounded average of maximum degree plus one and clique number. The card fixes all graph parameters and includes disconnected graphs, isolated vertices and every maximum degree. Acceptance requires a complete Lean-checked proof of the universal exact bound or a certified finite counterexample, without requiring an efficient colouring algorithm. The sharp interpolation would relate local degree restrictions to the global need for independent colour classes, and clique blowups of a five-cycle explain why the half coefficient cannot be increased. The checked September 2026 primary revision still states the target as open; known smaller-coefficient and restricted recolouring results have different scopes.

[Read in atlas](index.html#TCS-6682) · [\(\omega,\Delta\), and \(\chi\)](https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0118%28199804%2927%3A4%3C177%3A%3AAID-JGT1%3E3.0.CO%3B2-K) · [Bounding \(\chi\) by a fraction of \(\Delta\) for graphs without large cliques](https://arxiv.org/abs/1803.01051v1) · [An improved procedure for colouring graphs of bounded local density](https://arxiv.org/abs/2007.07874v3) · [A Recolouring Version of a Conjecture of Reed](https://arxiv.org/abs/2502.10147v1) · [An analogue of Reed’s conjecture for digraphs](https://arxiv.org/abs/2407.05827v4)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7222 — Graph isomorphism in polynomial time

Graph isomorphism asks whether two finite simple graphs agree after a bijective relabeling of their vertices. The target is a single deterministic algorithm that answers correctly on every explicitly encoded pair in polynomial time. A proposed relabeling is easy to verify, while ruling out all relabelings can require substantially more structure. The checked general upper bound is quasipolynomial, and efficient algorithms for restricted graph classes do not establish the unrestricted polynomial bound. A resolution would settle a central structural comparison problem whose position between P and NP-completeness remains unresolved.

[Read in atlas](index.html#TCS-7222) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Group, Graphs, Algorithms: The Graph Isomorphism Problem](https://people.cs.uchicago.edu/~laci/papers/icm18-babai.pdf) · [Parameterized complexity of graph isomorphism testing](https://doi.org/10.1016/j.cosrev.2026.100918) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/update.html) · [Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem](https://doi.org/10.4230/LIPIcs.MFCS.2021.27) · [On the Relative Power of Linear Algebraic Approximations of Graph Isomorphism](https://doi.org/10.4230/LIPIcs.MFCS.2021.37)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7248 — Tutte’s 5-flow conjecture

Tutte’s 5-flow conjecture asks whether every finite bridgeless graph can carry a nonzero integer circulation with edge magnitudes at most four. One orientation and one assignment of values must make the incoming and outgoing totals agree at every vertex. Parallel edges, disconnected graphs and isolated vertices are included, and no efficient construction is required. The assertion would sharpen the universal 6-flow theorem and improve a quantitative guarantee for packing sets that meet all directed cuts. A complete Lean proof must establish universal existence or certify a bridgeless counterexample; special graph classes, vector flows and reconfiguration results do not settle that question.

[Read in atlas](index.html#TCS-7248) · [Approximately Packing Dijoins via Nowhere-Zero Flows](https://link.springer.com/article/10.1007/s00493-025-00159-x) · [Nowhere-zero flow reconfiguration](https://arxiv.org/abs/2512.17342v4) · [Nowhere-zero 5-flows for graphs with bounded genus](https://www.ort.shu.edu.cn/EN/abstract/abstract21516.shtml) · [High-Dimensional \(p\)-Normed Flows](https://arxiv.org/abs/2601.12036v1) · [5-flow conjecture](https://www.openproblemgarden.org/op/5_flow_conjecture)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6538 — Almost-linear-time exact maximum matching in general graphs

Maximum matching chooses as many mutually vertex-disjoint edges as possible in an undirected graph. The target is an exact randomized algorithm with expected running time almost linear in the explicit input size. General graphs introduce odd cycles and the blossom structures needed to manage them. A fast maximal matching or an approximation does not guarantee the same answer. Progress would clarify whether finding the globally best pairing can approach the cost of simply reading all vertices and edges.

[Read in atlas](index.html#TCS-6538) · [A Theory of Alternating Paths and Blossoms from the Perspective of Minimum Length](https://pubsonline.informs.org/doi/abs/10.1287/moor.2020.0388) · [Maximum Matchings via Gaussian Elimination](https://www.mimuw.edu.pl/~mucha/pub/mucha_sankowski_focs04.pdf) · [Scaling algorithms for approximate and exact maximum weight matching](https://arxiv.org/abs/1112.0790) · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671) · [Gabow’s Cardinality Matching Algorithm in General Graphs: Implementation and Experiments](https://arxiv.org/abs/2409.14849) · [Maximum Matching and Related Problems in Catalytic Logspace](https://eccc.weizmann.ac.il/report/2026/080/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6653 — Gyárfás–Sumner conjecture

The Gyárfás–Sumner conjecture considers graphs excluding a fixed tree as an induced subgraph. It asks whether bounding clique number then also bounds chromatic number, independently of graph size. The proposed principle says that high coloring complexity with no large clique must eventually force every prescribed induced tree. This would organize a large collection of hereditary coloring classes through one structural mechanism. The saved review distinguishes genuinely induced trees from weaker path-induced copies and ordinary coloring from fractional results, while allowing an arbitrary bound rather than demanding polynomial growth.

[Read in atlas](index.html#TCS-6653) · [A Note on the Gyárfás–Sumner Conjecture](https://arxiv.org/abs/2302.08922) · [Radius two trees specify \(\chi\)-bounded classes](https://doi.org/10.1002/jgt.3190180203) · [Polynomial bounds for chromatic number. V. Excluding a tree of radius two and a complete multipartite graph](https://arxiv.org/abs/2202.05557) · [Trees and near-linear stable sets](https://link.springer.com/article/10.1007/s00493-025-00177-9) · [Polynomial Gyárfás–Sumner conjecture for graphs of bounded boxicity](https://igt.centre-mersenne.org/articles/10.5802/igt.17/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6683 — Optimal bounds in the Excluded Grid Theorem

The Excluded Grid Theorem guarantees a large grid minor when a graph has sufficiently large treewidth. The question asks for the optimal treewidth threshold forcing an r-by-r grid, including the correct logarithmic factors. Treewidth measures how difficult the graph is to decompose into small overlapping bags, while a grid supplies a concrete witness of large-scale complexity. Sharp bounds would quantify this foundational connection used throughout structural and algorithmic graph theory. The reviewed target concerns all graphs and grid side length, so bounds for an additional excluded-minor promise or suppressed polylogarithmic factors do not finish it.

[Read in atlas](index.html#TCS-6683) · [Graph minors. V. Excluding a planar graph](https://doi.org/10.1016/0095-8956(86)90030-4) · [Quickly Excluding a Planar Graph](https://www.sciencedirect.com/science/article/pii/S0095895684710732) · [Polynomial Bounds for the Grid-Minor Theorem](https://arxiv.org/abs/1305.6577) · [Towards \(Tight(er)\) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944) · [The Grid-Minor Theorem Revisited](https://link.springer.com/article/10.1007/s00493-025-00168-w) · [Catching Rats in H-minor-free Graphs](https://arxiv.org/abs/2506.22857)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7251 — Caccetta–Häggkvist conjecture

The conjecture links minimum outdegree with the length of a directed cycle. An n-vertex digraph of minimum outdegree r should contain a cycle of length at most the ceiling of n divided by r. Opposite arcs are allowed, but loops and parallel copies of an arc are forbidden. The assertion covers all graphs and all positive degree thresholds in the stated range. It is a sharp general principle connecting local expansion with global directed cycles.

[Read in atlas](index.html#TCS-7251) · [Caccetta–Häggkvist conjecture](https://www.openproblemgarden.org/op/caccetta_haggkvist_conjecture) · [Short rainbow cycles for families of small edge sets](https://arxiv.org/abs/2507.04581)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6539 — Almost-linear triangle detection

Triangle detection asks whether an undirected graph contains three pairwise adjacent vertices. The proposed randomized algorithm must decide this in almost linear time on every explicitly supplied graph. Only existence is requested, so graphs with many triangles do not impose a large-output obstacle. Sparse special classes offer useful successes without covering arbitrary inputs. The challenge is to avoid examining too many combinations of neighbors while still giving a reliable negative answer when no triangle exists anywhere.

[Read in atlas](index.html#TCS-6539) · [Arboricity and Subgraph Listing Algorithms](https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Chiba-1985-arboricity.pdf) · [Finding and Counting Given Length Cycles](https://www.math.tau.ac.il/~nogaa/PDFS/ayz4.pdf) · [Popular conjectures imply strong lower bounds for dynamic problems](https://arxiv.org/abs/1402.0054) · [Node-Weighted Triangles: Faster and Simpler](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.10/LIPIcs.ICALP.2026.10.html) · [On the Complexity of the Matching Problem of Regular Expressions with Backreferences](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.135/LIPIcs.ICALP.2026.135.html) · [A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications](https://arxiv.org/abs/2403.01085) · [A Linear-Time Solution to the Triangle Finding Problem: The Aegypti Algorithm](https://www.preprints.org/manuscript/202506.0875/v3) · [Aegypti: Feasible Quadratic-Time Combinatorial Triangle Detection via Sparse Bucket Reduction](https://www.preprints.org/manuscript/202511.2197/v10)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6654 — Seese’s conjecture

MSO1 permits quantification over vertices and vertex sets in a graph. Seese's conjecture asks whether decidability of this logic over a graph class forces bounded clique-width. The proposed implication connects an algorithmic property of the class's whole logical theory with a finite construction complexity for its graphs. A proof would identify a strong structural obstruction to decidable graph reasoning. The saved formulation imposes no hereditary assumption and excludes edge-set and counting extensions, so results for narrower classes or stronger logics cannot be substituted for the stated general MSO1 question.

[Read in atlas](index.html#TCS-6654) · [Forbidden Induced Subgraphs for Bounded Shrub-Depth and the Expressive Power of MSO](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.167) · [The structure of the models of decidable monadic theories of graphs](https://doi.org/10.1016/0168-0072(91)90054-P) · [Vertex-minors, monadic second-order logic, and a conjecture by Seese](https://www.labri.fr/perso/courcell/Textes1/BC-Oum%282007%29.pdf) · [MSO undecidability for hereditary classes of unbounded clique-width](https://doi.org/10.1016/j.ejc.2023.103700) · [Hereditary 2-WQO Graph Classes Have Bounded Clique-Width](https://arxiv.org/abs/2607.10939)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6655 — Cereceda’s conjecture

A recoloring step changes one vertex's color while keeping the graph properly colored. The saved Cereceda question asks whether every pair of proper \((d+2)\)-colorings of an n-vertex d-degenerate graph can be connected in \(O_{d}(n^{2})\) steps. Degeneracy ensures that every subgraph contains a vertex of degree at most d, providing a natural elimination structure. The challenge is using that structure without forcing an excessively long cascade of recolorings. A quadratic bound would make the reconfiguration space quantitatively navigable, while the saved proposal still requires a fuller source and progress review before becoming a completed card.

[Read in atlas](index.html#TCS-6655) · [Research reference · www.sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0012365X26000798)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7216 — Vertex reconstruction conjecture

The vertex reconstruction conjecture asks whether every finite simple graph with at least three vertices is determined by all its one-vertex-deleted views. The views forget vertex labels but retain the multiplicity of repeated isomorphism classes. Even the edge count and degree multiset can be recovered, while the full arrangement of edges is the unresolved target in current specialist sources. Finite computational checks and a theorem for interval graphs provide partial results. An earlier general proof claim is recorded without validation, and recent structured bipartite results are kept distinct from this full question.

[Read in atlas](index.html#TCS-7216) · [Reconstruction of Small Graphs and Digraphs](https://arxiv.org/abs/2102.01942v4) · [Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture](https://arxiv.org/abs/2604.16567v1) · [Interval Graphs are Reconstructible](https://arxiv.org/abs/2504.02353v2) · [Advancing Mathematics Research with AI-Driven Formal Proof Search](https://arxiv.org/abs/2605.22763v2) · [Vertex-substitution framework verifies the reconstruction conjecture for finite undirected graphs](https://www.sciencedirect.com/science/article/pii/S0020025523014433)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7249 — Berge–Fulkerson conjecture

Every bridgeless cubic multigraph is asked to admit six perfect matchings. Each edge must occur in exactly two positions of that six-matching list. The matchings may repeat, and parallel edges remain distinct. The target is an exact integral decomposition rather than an approximate or fractional cover. It captures a longstanding structural question about how perfect matchings fit together globally.

[Read in atlas](index.html#TCS-7249) · [The Berge–Fulkerson conjecture](https://www.openproblemgarden.org/op/the_berge_fulkerson_conjecture) · [On some perfect matching conjectures in infinite, cubic, bridgeless graphs](https://arxiv.org/abs/2607.29511)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7250 — Barnette’s conjecture

Barnette’s conjecture concerns 3-connected cubic bipartite planar graphs. It predicts that every such graph contains a cycle through all vertices exactly once. Every consecutive pair on the cycle must be an existing graph edge. Relaxed book-embedding results may add missing adjacencies and therefore do not settle the conjecture. The question isolates a classical boundary between local structural restrictions and a global spanning traversal.

[Read in atlas](index.html#TCS-7250) · [Barnette’s conjecture](https://www.openproblemgarden.org/op/barnettes_conjecture) · [Approximating Barnette’s Conjecture](https://drops.dagstuhl.de/storage/00lipics/lipics-vol357-gd2025/html/LIPIcs.GD.2025.6/LIPIcs.GD.2025.6.html) · [Partitions of planar (oriented) graphs into a connected acyclic and an independent set](https://arxiv.org/abs/2412.11774)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7253 — Seymour’s second-neighborhood conjecture

Seymour’s conjecture concerns oriented graphs with no loops or opposite pair of arcs. It asks for a vertex with at least as many vertices at distance exactly two as at distance one. Second neighbors exclude first neighbors and count vertices rather than paths. The statement is a general local expansion principle without degree or planarity promises. A complete-proof claim conflicts with a later specialist paper still treating the conjecture as open, and that status uncertainty is preserved.

[Read in atlas](index.html#TCS-7253) · [Seymour’s second neighbourhood conjecture](https://www.openproblemgarden.org/op/seymours_second_neighbourhood_conjecture) · [Towards a strengthening of the second neighborhood conjecture](https://arxiv.org/abs/2607.18047)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7341 — Strongly polynomial near-linear negative-weight shortest paths

The input is a directed graph with arbitrary real edge lengths and no negative cycle. The task is to compute all distances from one source exactly. The question asks for near-linear comparison-addition time independent of weight magnitudes. Near-linear integer-weight algorithms and almost-quadratic real-weight algorithms leave this general target unanswered. A resolution would close a central gap between numerical scaling and strongly polynomial graph computation.

[Read in atlas](index.html#TCS-7341) · [Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!](https://arxiv.org/abs/2304.05279) · [Negative-Weight Single-Source Shortest Paths in Near-linear Time](https://arxiv.org/abs/2203.03456) · [Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers](https://arxiv.org/abs/2511.08551) · [Bellman-Ford in Almost-Linear Time for Dense Graphs](https://arxiv.org/abs/2602.16153)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7346 — Strongly polynomial maximum flow below the \(mn\) barrier

Maximum flow asks for the greatest feasible transfer between a specified source and sink under arc capacities. Here capacities are arbitrary nonnegative rationals. The question asks for a fixed polynomial improvement over the general strongly polynomial arithmetic bound. The operation count must be independent of capacity encodings while intermediate bit space remains polynomial. Fast algorithms for bounded integral capacities and special graph classes do not establish this target.

[Read in atlas](index.html#TCS-7346) · [From Incremental Transitive Cover to Strongly Polynomial Maximum Flow](https://arxiv.org/abs/2510.20368)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6500 — Erdős girth conjecture

The Erdős girth conjecture seeks graphs with many edges despite the absence of short cycles. For every fixed k, the target is arbitrarily large graphs with order \(n^{1+1/k}\) edges and girth greater than 2k. Such graphs would match the classical density upper bound up to a constant depending on k. They also force every stretch-\((2k- 1)\) spanner to retain all edges, connecting the extremal construction to sharp sparsification limits. The saved review notes that progress for special parameters or fault-tolerant spanner models does not supply the missing high-girth families in general.

[Read in atlas](index.html#TCS-6500) · [Unconditional Lower Bounds for Degree Fault Tolerant Spanners](https://doi.org/10.4230/LIPIcs.ESA.2026.31) · [On Sparse Spanners of Weighted Graphs](https://doi.org/10.1007/BF02189308)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7218 — List edge-coloring conjecture

A proper edge coloring assigns different colors to edges that share an endpoint. In list edge coloring, each edge must choose its color from its own finite set of allowed colors. The conjecture asks whether giving every edge as many choices as the ordinary chromatic index always suffices, even with arbitrary list overlaps and parallel edges. It holds for bipartite multigraphs, and a general asymptotic theorem leaves only a vanishing relative gap. Exact equality for every finite loopless multigraph would show that local availability restrictions never impose an additional per-edge palette requirement.

[Read in atlas](index.html#TCS-7218) · [The list chromatic index of a bipartite multigraph](https://doi.org/10.1006/jctb.1995.1011) · [Asymptotics of the list-chromatic index for multigraphs](https://sites.math.rutgers.edu/~jkahn/LMULTI.pdf) · [The List Edge-Coloring Conjecture for Two New Infinite Families of Complete Graphs](https://arxiv.org/abs/2608.22895v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7252 — Triangle covering-to-packing ratio

Triangle covering deletes edges to eliminate every triangle, while triangle packing selects edge-disjoint triangles. The target is the supremum ratio of these two integral optima over finite simple graphs with a triangle. Packed triangles may share vertices but cannot share edges. Tuza’s conjecture predicts that the universal ratio equals two. The numerical benchmark requires a Lean-certified value within absolute error 0.01.

[Read in atlas](index.html#TCS-7252) · [Triangle packing versus triangle edge transversal](https://www.openproblemgarden.org/op/triangle_packing_vs_triangle_edge_transversal) · [On Tuza’s conjecture in dense graphs](https://doi.org/10.1016/j.dam.2025.06.049) · [Tuza's conjecture for graphs of maximum degree at most seven](https://arxiv.org/abs/2608.06538)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6511 — Deterministic Exact Matching

Exact Matching adds a prescribed red-edge count to the ordinary perfect matching problem. Given red and blue edges, an algorithm must decide whether some perfect matching contains exactly the requested number of red edges. The target is deterministic polynomial time on general graphs. Knowing the smallest and largest achievable counts is insufficient because intermediate counts can be absent. The problem isolates how to enforce an exact combinatorial constraint while avoiding the random algebraic choices used by existing approaches.

[Read in atlas](index.html#TCS-6511) · [Exact Matching: Algorithms and Related Problems](https://doi.org/10.4230/LIPIcs.STACS.2023.29) · [Matching is as easy as matrix inversion](https://doi.org/10.1145/28395.383347) · [Exact Matching in Matrix Multiplication Time](https://arxiv.org/abs/2508.04081v2) · [Bipartite Exact Matching in P](https://arxiv.org/abs/2604.01571v3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7254 — Neumann–Lara conjecture

The conjecture asks whether every oriented planar graph has a two-coloring with no monochromatic directed cycle. Arcs within a color class are allowed, so the coloring need not be proper. Loops and opposite pairs of arcs are excluded. The case without directed triangles is known, but directed triangles are allowed in the general target. The question is a directed analogue of central planar graph-decomposition principles.

[Read in atlas](index.html#TCS-7254) · [Partitioning planar digraphs](https://www.openproblemgarden.org/op/partitioning_planar_digraphs) · [Planar digraphs of digirth four are 2-colourable](https://arxiv.org/abs/1606.06114) · [Partitions of planar (oriented) graphs into a connected acyclic and an independent set](https://arxiv.org/abs/2412.11774)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7180 — Graph canonization versus graph isomorphism

Graph isomorphism recognizes when two labeled graphs have the same structure. Canonization assigns every presentation of that structure an identical representative. The question asks whether a polynomial-time algorithm can compute such representatives using only a graph-isomorphism decision oracle. General quasipolynomial canonization and efficient results for random graph families do not supply this reduction. A solution must handle every finite graph and keep its choices consistent across all relabelings.

[Read in atlas](index.html#TCS-7180) · [Canonical Form for Graphs in Quasipolynomial Time](https://par.nsf.gov/servlets/purl/10179675) · [Canonical Labelling of Random Regular Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.114)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7342 — Steiner Shortcut Conjecture

A Steiner shortcut augments a directed graph with new vertices and arcs. Reachability between all original vertices must remain exactly the same. The conjecture asks for near-linear many added arcs and polylogarithmic paths between reachable original pairs. The earlier conjecture forbidding new vertices was refuted, while this version remains a distinct structural question. The target concerns existence and does not impose a fast construction algorithm.

[Read in atlas](index.html#TCS-7342) · [Reviving Thorup's Shortcut Conjecture](https://arxiv.org/abs/2510.24954)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7343 — Deterministic almost-linear vertex connectivity

Vertex connectivity is the smallest number of vertices whose removal disconnects a graph or leaves at most one vertex. The task is to find this number and an attaining separator in an unweighted undirected graph. The question asks for deterministic almost-linear worst-case time. Randomized almost-linear algorithms are known, while the reviewed deterministic bound still depends on the connectivity. The target tests the role of randomness in exact network robustness computation.

[Read in atlas](index.html#TCS-7343) · [Deterministic Vertex Connectivity via Common-Neighborhood Clustering and Pseudorandomness](https://arxiv.org/abs/2503.20985) · [Vertex Connectivity in Poly-logarithmic Max-flows](https://arxiv.org/abs/2104.00104) · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7245 — Constant-factor treewidth preservation by subcubic subgraphs

Every graph is asked to contain a subgraph of maximum degree three with comparable treewidth. Comparable means losing only a universal constant factor. The subgraph can delete edges and vertices but cannot contract edges or introduce new ones. Known general degree-three sparsifiers lose a polylogarithmic factor in treewidth. A constant-factor theorem would make bounded-degree structure a universal witness of large treewidth.

[Read in atlas](index.html#TCS-7245) · [Degree-3 Treewidth Sparsifiers](https://home.ttic.edu/~cjulia/papers/treewidth-sparsifiers-SODA.pdf) · [Sparse induced subgraphs of large treewidth](https://www.sciencedirect.com/science/article/pii/S009589562500019X) · [List of open questions: Linear treewidth and pathwidth sparsifiers](https://a3nm.net/work/research/questions/#linear-treewidth-and-pathwidth-sparsifiers)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7263 — Linear-time directed shortest paths with nonnegative real weights

The input is a directed graph with arbitrary nonnegative real arc lengths and a specified source. The task is to output every exact source distance. The question asks for deterministic linear worst-case time using real addition and comparison. Recent algorithms break the sorting barrier while retaining superlinear overhead. A linear algorithm would match the cost of reading the graph and writing the distances.

[Read in atlas](index.html#TCS-7263) · [Breaking the Sorting Barrier for Directed Single-Source Shortest Paths](https://arxiv.org/abs/2504.17033) · [A Faster Directed Single-Source Shortest Path Algorithm](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.81)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7348 — Single-exponential exact cut mimicking networks

An exact cut mimicking network represents every minimum cut separating a group of terminals from its complement. It must preserve all terminal bipartition values simultaneously. The question asks whether every weighted undirected graph has such a representation with singly exponential size in the number of terminals. Arbitrary new nonterminal vertices are permitted, with no restriction to contractions. The general gap between exponential lower bounds and doubly exponential upper bounds remains the target.

[Read in atlas](index.html#TCS-7348) · [Cut-Preserving Vertex Sparsifiers for Planar and Quasi-Bipartite Graphs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.53/LIPIcs.ICALP.2025.53.html) · [On Mimicking Networks Representing Minimum Terminal Cuts](https://arxiv.org/abs/1207.6371)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7217 — Edge reconstruction conjecture

Delete each edge of a graph in turn, erase vertex labels and collect the resulting graphs with repetitions. The edge reconstruction conjecture asks whether this multiset determines every finite simple graph with at least four edges. All vertices survive deletion, and repeated copies of the same graph remain significant. A triangle plus an isolated vertex and a three-leaf star show why a three-edge version fails. Recent algebraic reformulations and results for promised graph classes leave the general uniqueness question open.

[Read in atlas](index.html#TCS-7217) · [Reconstruction of Small Graphs and Digraphs](https://arxiv.org/abs/2102.01942) · [A combinatorial K-theory perspective on the Edge Reconstruction Conjecture in graph theory](https://arxiv.org/abs/2402.14986v2) · [The Class Edge-Reconstruction Number of a Maximal Planar Graph Is One or Two](https://arxiv.org/abs/2609.02389v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7344 — Almost-linear exact directed global minimum cut

A directed global cut removes every arc leaving a chosen nonempty proper vertex set. The task is to minimize its total weight without being given source and sink terminals. The question asks for exact almost-linear computation with bounded-error randomization and polynomially bounded integer weights. Known almost-linear approximation schemes retain a precision cost that matters for exact recovery. A resolution would address the global directed-cut bottleneck beyond single-pair maximum flow.

[Read in atlas](index.html#TCS-7344) · [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176) · [Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs](https://arxiv.org/abs/2512.09080)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7345 — Almost-linear directed vertex connectivity

Directed vertex connectivity measures the smallest vertex failure set destroying strong connectivity or leaving at most one vertex. The task is to output its exact value and a minimum separator in an unweighted digraph. The question asks for a bounded-error randomized algorithm with almost-linear worst-case time. The reviewed algorithms cover important density and connectivity regimes but leave a general gap. The target demands one bound valid for every directed input graph.

[Read in atlas](index.html#TCS-7345) · [Faster Algorithms for Global Minimum Vertex-Cut in Directed Graphs](https://arxiv.org/abs/2512.24355) · [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7244 — Boolean dimension of posets with planar cover graphs

The cover graph records immediate comparabilities of a finite partial order. The question asks whether its planarity guarantees a constant number of total orders encoding every comparability. One Boolean rule interprets the pairwise comparison bits from those orders. The orders and rule may vary with the poset, but their number must have a universal bound. The target links sparse graph structure to concise representations of reachability.

[Read in atlas](index.html#TCS-7244) · [Boolean dimension and dim-boundedness: Planar cover graph with a zero](https://arxiv.org/abs/2206.06942) · [Cliquewidth and dimension](https://arxiv.org/abs/2308.11950) · [List of open questions: Boolean dimension of planar posets](https://a3nm.net/work/research/questions/#boolean-dimension-of-planar-posets)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7285 — Strongly explicit Ramanujan families for every degree

A regular Ramanujan graph meets the optimal asymptotic bound on nontrivial adjacency eigenvalues. The question asks for an infinite family at every fixed degree at least three. One algorithm must compute each local port connection in time polynomial in the vertex-label length. The family may use only a decidable unbounded set of sizes and permits the stated multigraph conventions. Constructions with positive spectral slack or slower global access do not meet the exact strong-explicitness target.

[Read in atlas](index.html#TCS-7285) · [Explicit expanders of every degree and size](https://arxiv.org/abs/2003.11673)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0611 — Bipartite Exact Matching: deterministic polynomial time

Bipartite Exact Matching asks for a perfect matching containing exactly a specified number of red edges. Even a small complete bipartite graph can have attainable red counts separated by gaps. This makes the equality constraint stronger than minimizing or maximizing the count. The saved card records an April 2026 preprint claiming deterministic polynomial time, together with limits on its verification. The project is therefore to explain and assess that claimed resolution of the historical question, while keeping the bipartite restriction explicit.

[Read in atlas](index.html#TCS-0611) · [Exact Matching: Algorithms and Related Problems](https://doi.org/10.4230/LIPIcs.STACS.2023.29) · [Bipartite Exact Matching in P](https://arxiv.org/abs/2604.01571v3)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0771 — Computational complexity of planar treewidth

Treewidth measures how a graph can be assembled from overlapping vertex bags arranged in a tree. This entry concerns the complexity of computing that quantity when the input graph is planar. Planarity limits how edges interact geometrically, but does not directly provide an optimal tree decomposition. A sharper complexity classification would clarify whether exact structural information can be obtained efficiently before running decomposition-based algorithms. The inherited title does not fix an approximation allowance or requested running time, so those choices remain unresolved in this working description.

[Read in atlas](index.html#TCS-0771) · [Algorithms for Optimization Problems in Planar Graphs](https://doi.org/10.4230/DagRep.6.5.94)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0594 — 3-colorability of diameter-two graphs

The problem asks whether three-colorability is decidable in deterministic polynomial time for every graph of diameter at most two. The graph is given explicitly, and it is not promised to be colorable. No sparsity, forbidden-cycle, degree or vertex-list restriction is imposed. The best general bound identified in the checked sources is subexponential, while a July 2026 polynomial-time result needs an additional four-cycle exclusion. The question isolates a precise structural boundary between easy complete graphs and the known hardness at diameter three.

[Read in atlas](index.html#TCS-0594) · [Colouring Graphs of Bounded Diameter, in Graph Colouring: from Structure to Algorithms](https://doi.org/10.4230/DagRep.9.6.125) · [Algorithms and Almost Tight Results for 3-Colorability of Small Diameter Graphs](https://doi.org/10.1007/s00453-014-9949-6) · [Faster 3-coloring of small-diameter graphs](https://arxiv.org/abs/2104.13860v1) · [List 3-coloring \(C_{4}\)-free graphs of diameter-2 in polynomial-time](https://arxiv.org/abs/2606.30282v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0587 — Polylogarithmic treewidth with forbidden induced minors

Treewidth measures the largest bag needed to organize a graph in a tree decomposition. The question concerns graphs with no large clique and with neither a fixed complete bipartite graph nor a fixed wall as an induced minor. It asks whether their treewidth is bounded by a fixed power of the logarithm of their number of vertices. A March 2026 preprint proves a subpolynomial bound but still states the polylogarithmic target as a conjecture. The stronger bound would improve the structural and algorithmic understanding of these induced-minor-free graph classes.

[Read in atlas](index.html#TCS-0587) · [Solving Problems on Graphs: From Structure to Algorithms](https://doi.org/10.4230/DagRep.15.1.105) · [Induced minors and subpolynomial treewidth](https://arxiv.org/abs/2512.18835)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0775 — Optimal exact-distance label length for planar graphs

Each vertex receives a short binary label. The exact distance between two vertices must follow from their labels alone. The same decoder serves every graph of the chosen size. The target is the optimal asymptotic number of label bits. Current lower and upper bounds differ by a polynomial factor.

[Read in atlas](index.html#TCS-0775) · [Better Distance Labeling for Unweighted Planar Graphs](https://doi.org/10.1007/s00453-023-01133-z)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0315 — Fat Minors

A fat graph minor models vertices and edges by connected pieces that remain separated except at prescribed incidences. The source asks whether excluding a fixed such pattern forces balanced separators coverable by roughly a square-root number of bounded-radius balls. A related version assumes exclusion of an induced minor. The separator may contain many vertices, so its economical description is metric coverage rather than cardinality alone. The conjecture seeks a usable separator theorem from coarse geometric restrictions that are weaker than ordinary excluded-minor structure.

[Read in atlas](index.html#TCS-0315) · [Metric Sketching and Dynamic Algorithms for Geometric and Topological Graphs](https://doi.org/10.4230/DagRep.15.5.134)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1206 — Structural nowhere density of monadically stable graph classes

Monadic stability restricts the order patterns that can be defined in graph classes after adding unary labels. The source conjectures that every such class is structurally nowhere dense. The conclusion would represent these potentially dense graphs through a controlled logical transformation of a sparse class. This could explain why stable graph classes support decomposition and model-checking techniques reminiscent of sparse graphs. The exact transformation and effectiveness conventions are absent from the excerpt, so the source's definitions must be retained before treating the conjecture as ordinary nowhere-denseness of the original graphs.

[Read in atlas](index.html#TCS-1206) · [Weakly-Sparse and Strongly Flip-Flat Classes of Graphs Are Uniformly Almost-Wide](https://doi.org/10.4230/LIPIcs.CSL.2026.41)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1246 — Well-quasi-ordering Eulerian digraphs by weak immersion

An Eulerian digraph balances incoming and outgoing edges at each vertex. Weak immersion represents another digraph by vertices and edge-disjoint directed routes, allowing routes to pass through represented vertices. The conjecture says every infinite sequence of Eulerian digraphs contains an earlier graph weakly immersed in a later one. The source proves related results under additional width restrictions. Removing those restrictions would yield a broad structural ordering theorem and support finite-obstruction approaches to properties preserved by weak immersion.

[Read in atlas](index.html#TCS-1246) · [Well-Quasi-Ordering Eulerian Digraphs: Bounded Carving Width](https://doi.org/10.4230/LIPIcs.ICALP.2026.51)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1639 — Linear neighborhood complexity of hereditary small graph classes

Neighborhood complexity counts how many distinct intersections with a chosen vertex set can occur among graph neighborhoods. The conjecture concerns hereditary small graph classes, whose labeled graphs have at most factorial-times-exponential growth. It predicts a linear bound on this neighborhood diversity. The cited work connects such a bound to compact adjacency labels. The project asks whether a global restriction on how many graphs a class contains necessarily forces a strong local restriction on how their vertices can see a set.

[Read in atlas](index.html#TCS-1639) · [Adjacency Labeling Schemes for Small Classes](https://doi.org/10.4230/LIPIcs.ITCS.2025.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2783 — Erdős girth conjecture

The girth conjecture asks for dense graphs with every short cycle forbidden. For each fixed k, the target is \(\Omega (n^{1+1/k})\) edges and girth at least \(2k+2\). The lower bound must hold for every sufficiently large n, with constants depending on k. The known cases are \(k=1,2,3,5\), as still recorded in July 2026. A resolution would sharpen fundamental lower bounds for routing and graph spanners.

[Read in atlas](index.html#TCS-2783) · [Space-Stretch Tradeoff in Routing Revisited](https://doi.org/10.4230/LIPIcs.DISC.2022.37) · [Unconditional Lower Bounds for Degree Fault Tolerant Spanners](https://arxiv.org/abs/2607.07576)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6874 — Ramanujan graphs of every degree

A d-regular Ramanujan graph has nontrivial adjacency eigenvalues within the source's optimal spectral range. The saved survey conjecture asks for arbitrarily large examples at every degree d at least three. The goal is a family at each fixed degree, not simply isolated small graphs or a degree sequence that grows with size. Such families provide exceptionally strong sparse connectivity and underpin many expander applications. This is a dated survey formulation whose present status is not rechecked in the draft, and bipartite conventions and treatment of trivial eigenvalues must be retained when comparing later constructions.

[Read in atlas](index.html#TCS-6874) · [Expander Graphs and Their Applications](https://www.math.ias.edu/avi/node/974)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6875 — Two-sided Ramanujan signings

A two-lift replaces each graph vertex by two copies and uses an edge signing to determine how the copies are connected. The source asks for lifts or signings satisfying two-sided Ramanujan spectral bounds. Controlling both ends of the new spectrum prevents large positive or negative nontrivial eigenvalues from spoiling the desired expansion guarantee. A construction would provide a systematic method for growing high-quality expander families. The saved survey groups several conjectures, so the starting-graph assumptions, exact spectral interval, and later status must be checked before treating a one-sided signing theorem as a full answer.

[Read in atlas](index.html#TCS-6875) · [Expander Graphs and Their Applications](https://www.math.ias.edu/avi/node/974)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7143 — Bipartite circle pivot-minors from large rank-width

Pivot-minors use edge-pivot operations together with vertex deletion to simplify graphs. The source asks whether sufficiently large rank-width forces every fixed bipartite circle graph as such a minor. The conclusion would supply a universal family of structural obstructions witnessing high cut-rank complexity. This parallels excluded-grid principles while using graph transformations tailored to rank-width. The threshold may depend on the fixed target graph, and the source's pivot and circle-graph conventions must be recovered before the statement is compared with ordinary graph-minor or vertex-minor theorems.

[Read in atlas](index.html#TCS-7143) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7144 — Tree vertex-minors from large linear rank-width

Linear rank-width measures cut-rank complexity along a vertex ordering. The source asks whether a sufficiently large value forces any prescribed tree as a vertex-minor. A positive answer would make trees universal witnesses for high complexity in this linear decomposition model. The distinction between linear and ordinary rank-width matters because a branching decomposition can be simple while every linear layout is difficult. The saved note leaves the threshold as target-dependent and concerns existence, so an efficient algorithm to find the tree would be an additional requirement rather than part of the stated structural question.

[Read in atlas](index.html#TCS-7144) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7145 — Well-quasi-ordering by pivot-minors

A quasi-order is well-quasi-ordered when every infinite sequence contains an earlier object comparable below a later one. The source asks whether graphs have this property under pivot-minors. A positive answer would rule out infinite antichains and provide a strong finiteness principle for obstruction-based classifications. The challenge is that pivot operations preserve and transform structure differently from ordinary edge contractions. The saved survey question must retain its precise graph universe and pivot convention, and this draft does not infer the answer from the separate well-quasi-ordering theorem for ordinary graph minors.

[Read in atlas](index.html#TCS-7145) · [Rank-width: Algorithmic and Structural Results](https://arxiv.org/abs/1601.03800)
Existing status: `source_open` · Summary written: 2026-09-11

## Data structures (18)

### TCS-6498 — Dynamic optimality conjecture

Splay trees reorganize a binary search tree after each access using local rotations. The question asks whether this simple rule is always within a constant factor of the best tree strategy that knows the entire request sequence. An additive linear allowance pays for the initial tree. Frequency and locality guarantees cover useful patterns but do not establish this universal comparison. Understanding this gap would show whether local adaptation can exploit every advantage available to an offline search tree.

[Read in atlas](index.html#TCS-6498) · [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498) · [Binary Search Trees and Dynamic Optimality, Lecture 23](https://www.cs.cmu.edu/~yangp/15-451/lecture23.pdf) · [Dynamic Optimality—Almost](https://doi.org/10.1137/S0097539705447347)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6540 — Superlogarithmic static cell-probe lower bounds

A static data structure preprocesses a database and later answers queries by reading stored memory cells. This question seeks an explicitly computable Boolean query problem forcing more than logarithmically many reads despite unrestricted preprocessing. The saved formulation fixes short queries, logarithmic word size, near-linear space, and deterministic adaptive access. Free computation between reads makes this an information-access lower bound. Such an example would expose a fundamental limit on making useful information locally accessible through clever storage alone.

[Read in atlas](index.html#TCS-6540) · [The Natural Proofs Barrier against Data-Structure Lower-Bounds](https://doi.org/10.1145/3798129.3800843) · [Stronger Cell Probe Lower Bounds via Local PRGs](https://eccc.weizmann.ac.il/report/2025/030/) · [Lower Bounds for Linear Operators](https://eccc.weizmann.ac.il/report/2025/155/) · [Crossing the Logarithmic Barrier for Dynamic Boolean Data Structure Lower Bounds](https://epubs.siam.org/doi/10.1137/18M1198429) · [An \(\Omega ((\log  n/\log  \log  n)^{2})\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6586 — Deterministic linear-time static dictionaries

A static dictionary stores distinct integer keys together with associated values and supports exact membership queries. The question asks for deterministic linear-time construction, linear space, and constant worst-case query time on the stated word RAM. All preprocessing work must be included in the construction bound. Random hashing motivates the desired efficiency but does not itself provide a deterministic construction. A solution would give other algorithms a dependable dictionary primitive without making their preprocessing randomized or increasing their asymptotic running time.

[Read in atlas](index.html#TCS-6586) · [Faster Deterministic Dictionaries](https://www.brics.dk/RS/99/48/BRICS-RS-99-48.pdf) · [Constructing Efficient Dictionaries in Close to Sorting Time](https://link.springer.com/chapter/10.1007/978-3-540-70575-8_8) · [Internal Pattern Matching Queries in a Text and Applications](https://epubs.siam.org/doi/10.1137/23M1567618) · [Compressed Index with Construction in Compressed Space](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.25)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7331 — Constant-time deterministic dynamic dictionaries

A dynamic dictionary maintains key-value records under insertion and deletion. Hashing gives constant expected operation bounds using random choices. The question asks for the same basic performance from deterministic programs. The space budget excludes a table covering the entire key universe. Either such an implementation or a general impossibility result would clarify the value of randomization.

[Read in atlas](index.html#TCS-7331) · [Research Statement](https://people.csail.mit.edu/mip/docs/job-application07/statements.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7338 — Multiphase conjecture

The first phase stores a family of sets. A later phase receives another set before the final query index is known. The last phase asks whether that set intersects one chosen stored set. The conjecture requires polynomial overhead in at least one normalized phase cost. An unconditional proof would support strong dynamic-data-structure lower bounds.

[Read in atlas](index.html#TCS-7338) · [Towards Polynomial Lower Bounds for Dynamic Problems](https://www.ccs.neu.edu/~viola/classes/papers/PatrascuTowards.pdf) · [An Adaptive Step Toward the Multiphase Conjecture](https://arxiv.org/abs/1910.13543)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0300 — Randomized complexity of online labeling

An ordered list is stored using a fixed range of numerical labels. Insertions and deletions must preserve label order while keeping spare labels available. The cost counts how many existing items receive a different label. Randomization achieves nearly logarithmic expected amortized cost in the cited result. The remaining task is to determine the optimal asymptotic rate for constant slack.

[Read in atlas](index.html#TCS-0300) · [Computational Complexity of Discrete Problems](https://doi.org/10.4230/DagRep.7.3.45) · [Nearly Optimal List Labeling](https://arxiv.org/abs/2405.00807)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7328 — Amortized decrease-key complexity of standard pairing heaps

The standard pairing heap uses a fixed two-pass consolidation during delete-min. Its pointer operations are simple, but decreases can affect the cost of future consolidations. The target is a tight amortized charge for decrease-key with the conventional costs for other operations. A logarithmic-logarithmic lower bound is known. Results for pure, multipass, smooth or rank-pairing heaps concern different algorithms.

[Read in atlas](index.html#TCS-7328) · [On the Efficiency of Pairing Heaps and Related Data Structures](https://doi.org/10.1145/320211.320214) · [Pure Pairing Heaps](https://arxiv.org/html/2607.23118)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7333 — Space-query exponent curve of 3SUM indexing

Two integer sets are stored before membership queries arrive. A query asks whether its number belongs to their sumset. The target is the best query exponent at each allowed storage exponent. All retained information is charged even though preprocessing time is unrestricted. The numerical curve target is broader than the saved polylogarithmic-query existence question.

[Read in atlas](index.html#TCS-7333) · [Conditional Lower Bounds for Space/Time Tradeoffs](https://arxiv.org/abs/1706.05847) · [Improved Time-Space Tradeoffs for 3SUM-Indexing](https://arxiv.org/abs/2512.04258v2)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7334 — Strong SetDisjointness conjecture

A family of sets is stored in advance. A query selects two stored sets and asks whether they intersect. The conjecture relates the representation size to the square of query time. Matching upper tradeoffs are known, but the general lower bound is not. The target counts storage after preprocessing rather than the time spent preprocessing.

[Read in atlas](index.html#TCS-7334) · [Conditional Lower Bounds for Space/Time Tradeoffs](https://arxiv.org/abs/1706.05847)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0949 — Data Structure Lower Bound in the Cell Probe Model

A data structure preprocesses an n-by-n Boolean matrix and then answers matrix-vector products over AND and OR. The cell-probe model counts memory accesses while allowing free computation on the information read. The source asks for a superlinear-in-n query lower bound when the representation stores the matrix with only a small amount of extra space. Existing upper bounds show that this succinct model can outperform straightforward word-RAM expectations. A lower bound must therefore identify information that genuinely has to be fetched, rather than charge for the arithmetic or logical work of computing the answer.

[Read in atlas](index.html#TCS-0949) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:75)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5706 — Unified bound for binary search trees

A search should be cheap when its key is close in rank to a recently requested key. The unified bound combines this spatial locality with temporal locality. The target requires a single online binary search tree. Known BST bounds include an extra logarithmic-logarithmic term per access. The cited source distinguishes an earlier disputed claim from an established solution.

[Read in atlas](index.html#TCS-5706) · [The Group Access Bounds for Binary Search Trees](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.38/LIPIcs.ICALP.2024.38.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5825 — Superconstant word-RAM time for prefix-\(U_1\)

The prefix-U-one problem maintains a fixed-length bit sequence under substitutions and returns the AND of any requested prefix. The conjecture rules out a deterministic data structure with linear preprocessing and constant worst-case time for both operations. Its machine has logarithmic-size words and explicitly charged arithmetic, bit operations and memory accesses. Amortized constant time, expected constant time and stronger predecessor queries are separate questions. A resolution would settle a basic dynamic set barrier underlying conditional classifications for regular word and tree languages.

[Read in atlas](index.html#TCS-5825) · [Dynamic Membership for Regular Languages](https://doi.org/10.4230/LIPIcs.ICALP.2021.116) · [Dynamic data structures for parameterized string problems](https://arxiv.org/abs/2205.00441) · [Dynamic Membership for Regular Tree Languages](https://doi.org/10.4230/LIPIcs.MFCS.2025.8)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7329 — Logarithmic fully retroactive priority queues

Retroactivity permits inserting and deleting operations in the past. Each edit changes the queue state at later historical times. Queries must return the minimum at any chosen time. The target is logarithmic amortized operation time and linear history storage. A recent optimal result covers monotonic histories but not unrestricted priority queues.

[Read in atlas](index.html#TCS-7329) · [Retroactive Data Structures](https://erikdemaine.org/papers/Retroactive_TALG/) · [Retroactive Monotonic Priority Queues via Range Searching](https://arxiv.org/abs/2508.09892v3)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7340 — Optimal randomized memory-reallocation overhead

Objects of different sizes share one nearly full memory array. Every object must occupy a contiguous interval. An insertion or deletion may require moving other live objects. Cost compares the total moved volume with the size of the updated object. The remaining problem is the tight expected overhead as the unused fraction tends to zero.

[Read in atlas](index.html#TCS-7340) · [A Nearly Quadratic Improvement for Memory Reallocation](https://arxiv.org/abs/2405.12152) · [Memory Reallocation with Polylogarithmic Overhead](https://arxiv.org/abs/2602.15417v1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6508 — Deque conjecture

A deque permits insertions and deletions at either end of an ordered collection. This question studies the implementation that inserts extreme keys and splays an extreme key before deleting it. It asks whether every operation sequence costs linear total time, including an allowance for the initial tree. Alternating ends and inserting new keys creates behavior beyond a single sorted scan. The conjecture would show that self-adjusting search trees automatically attain the efficiency expected from this restricted interface.

[Read in atlas](index.html#TCS-6508) · [Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture](https://arxiv.org/abs/0707.2160) · [A New Path from Splay to Dynamic Optimality](https://doi.org/10.1137/1.9781611975482.80) · [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0474 — Constant-update working-set heaps on pointer machines

A priority queue supports insertions, priority decreases and minimum extraction. The extraction charge depends on the number of items inserted since the extracted item arrived. The target combines this adaptive charge with constant amortized insertion and decrease-key. Only pointer-machine operations and key comparisons are available. The latest cited constructions retain a slowly growing factor in at least one update operation.

[Read in atlas](index.html#TCS-0474) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1) · [Near-Optimal Working-Set Heaps and Dijkstra on Pointer Machines](https://arxiv.org/abs/2604.24134v2) · [Heaps and Their Working Sets](https://arxiv.org/abs/2607.24621v1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7327 — Buffered fully persistent search trees

A search tree keeps all previous versions of its ordered set. A user may start a new branch from any past version. Buffered updates save external-memory transfers by processing writes together. The goal combines these savings with fast historical queries and constant-I/O cloning. The latest cited result supplies this update efficiency only for partial persistence.

[Read in atlas](index.html#TCS-7327) · [Buffered Partially-Persistent External-Memory Search Trees](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/LIPIcs.ESA.2025.82/LIPIcs.ESA.2025.82.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7330 — Combined depth and size bounds for confluently persistent tries

Confluent persistence lets a subtree be copied between historical trie versions while retaining all old versions. The question asks for one functional representation combining a shallow-update bound with a logarithmic bound in logical version size. Navigation has its own worst-case time bound and may not extend permanent version history. An update must pay for any earlier navigation records that its new stored version retains. The model and parameters explicitly cover multiple fingers, logical sharing, subtree copies and temporary versus permanent memory.

[Read in atlas](index.html#TCS-7330) · [Confluently Persistent Tries for Efficient Version Control](https://erikdemaine.org/papers/ConfluentTries_Algorithmica/paper.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

## Dynamic algorithms (15)

### TCS-6625 — Deterministic fully dynamic connectivity with polylogarithmic worst-case updates

Dynamic connectivity maintains whether pairs of vertices remain connected as graph edges are inserted and deleted. The reviewed question asks for deterministic polylogarithmic worst-case time for every operation, with exact answers. Deleting a spanning-forest edge requires quickly finding a replacement across the exposed cut or certifying that none exists. This would combine deterministic reliability with consistently low latency on arbitrary update sequences. The saved review distinguishes amortized guarantees, randomized cutset recovery, and subpolynomial worst-case time from the stronger polylogarithmic bound required here.

[Read in atlas](index.html#TCS-6625) · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf) · [Dynamic graph connectivity in polylogarithmic worst case time](https://doi.org/10.1137/1.9781611973105.81) · [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297) · [Expander Pruning with Polylogarithmic Worst-Case Recourse and Update Time](https://doi.org/10.1137/1.9781611978971.103) · [Logarithmic Lower Bounds in the Cell-Probe Model](https://erikdemaine.org/papers/DynamicConnectivity_SICOMP/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6627 — Fully dynamic near-optimal matching with polylogarithmic updates

A matching selects graph edges without shared endpoints. The reviewed question asks to maintain an explicit matching within a factor of one plus \(\varepsilon\) of maximum using polylogarithmic expected amortized update time. Although the optimum changes little after one update, repairing a particular matching may involve a long alternating path. A solution would combine nearly optimal allocation quality with efficient response to both insertions and deletions. The saved record requires actual partner information and distinguishes this task from estimating matching size or maintaining the weaker guarantee of maximality.

[Read in atlas](index.html#TCS-6627) · [Sixteenth Biennial Scientific Report: March 2021–March 2023](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf) · [Fully Dynamic Matching: \((2- \sqrt{2})\)-Approximation in Polylog Update Time](https://epubs.siam.org/doi/10.1137/1.9781611977912.109) · [Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemeredi Graphs](https://arxiv.org/abs/2406.13573) · [A note on Ordered Ruzsa-Szemerédi graphs](https://arxiv.org/abs/2502.02455) · [On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication](https://arxiv.org/abs/2403.02582) · [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6626 — Polylogarithmic worst-case updates for exact dynamic minimum spanning forests

A minimum spanning forest connects each graph component as cheaply as possible under the current edge weights. The question asks for polylogarithmic worst-case update time in a fully dynamic graph. Randomization is allowed, with high-probability correctness against an update sequence independent of the random choices. The hard step is finding the cheapest replacement edge after deletion splits a tree. The saved review separates this exact maintenance target from amortized bounds and notes that reporting only actual forest changes avoids an artificial cost for repeatedly printing every tree edge.

[Read in atlas](index.html#TCS-6626) · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf) · [Faster Fully-Dynamic Minimum Spanning Forest](https://arxiv.org/abs/1407.6832) · [Dynamic Minimum Spanning Forest with Subpolynomial Worst-case Update Time](https://arxiv.org/abs/1708.03962) · [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297) · [Deterministic Rounding of Dynamic Fractional Matchings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.27)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6670 — Polylogarithmic maintenance of the exact global minimum cut

The global minimum cut is the smallest number of edges separating a graph into two nonempty parts. The reviewed question asks to maintain its exact value under insertions and deletions with expected polylogarithmic amortized updates. Queries must also be polylogarithmic, and randomized correctness is required over oblivious operation sequences. Even though one update changes the value by at most one, identifying whether another cut has become optimal requires global information. The target returns only the numerical value and uses zero for disconnected graphs, avoiding output-size and convention ambiguities.

[Read in atlas](index.html#TCS-6670) · [Deterministic and Exact Fully-dynamic Minimum Cut of Superpolylogarithmic Size in Subpolynomial Time](https://arxiv.org/abs/2512.13105) · [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://people.csail.mit.edu/virgi/6.s078/papers/omv.pdf) · [Incremental Exact Min-Cut in Polylogarithmic Amortized Update Time](https://arxiv.org/abs/1611.06500) · [Fully Dynamic Exact Edge Connectivity in Sublinear Time](https://arxiv.org/abs/2302.05951) · [Tree-Packing Revisited: Faster Fully Dynamic Min-Cut and Arboricity](https://link.springer.com/article/10.1007/s00453-026-01394-4) · [Fully Dynamic Approximate Minimum Cut in Subpolynomial Time per Operation](https://arxiv.org/abs/2412.15069)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7332 — Logarithmic Las Vegas dynamic connectivity

An undirected graph changes one edge at a time. A query asks whether two vertices remain connected. The target is logarithmic amortized expected update time with always-correct answers. Known Las Vegas bounds retain an iterated-logarithm overhead. The related deterministic worst-case problem asks for different guarantees.

[Read in atlas](index.html#TCS-7332) · [Fully Dynamic Connectivity in \(O(\log n(\log\log n)^2)\) Amortized Expected Time](https://theoretics.episciences.org/10791/pdf) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0478 — Dynamic APSP with edge-linear updates

Dynamic all-pairs shortest paths must answer exact distances while directed weighted edges change. The reviewed target combines polylogarithmic worst-case queries with amortized update time nearly linear in the edge bound m. It allows polynomial preprocessing and space while requiring deterministic answers. The principal gap is sparse graphs, where updates should cost much less than rebuilding a full distance table. The saved review explains that many distances changing simultaneously is not an impossibility argument, because the oracle may represent those changes implicitly and expose only one queried pair.

[Read in atlas](index.html#TCS-0478) · [Scalable Data Structures (Dagstuhl Seminar 21071)](https://doi.org/10.4230/DagRep.11.1.1) · [A New Approach to Dynamic All Pairs Shortest Paths](https://www.diag.uniroma1.it/~demetres/docs/dapsp-full.pdf) · [Fully-Dynamic All-Pairs Shortest Paths: Likely Optimal Worst-Case Update Time](https://arxiv.org/abs/2306.02662v3) · [Bootstrapping Dynamic APSP via Sparsification](https://doi.org/10.4230/LIPIcs.ESA.2025.113)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7326 — Worst-case logarithmic dynamic planar convex hulls

A planar point set changes by insertion and deletion. A query asks for a point farthest in a supplied direction. The target is linear storage and logarithmic time for each individual operation. The known optimal update guarantee is amortized over a sequence. The question isolates whether geometric maintenance must sometimes cause expensive update spikes.

[Read in atlas](index.html#TCS-7326) · [Dynamic Planar Convex Hull](https://cs.au.dk/~gerth/papers/arxiv1902.11169.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7339 — Near-linear incremental topological ordering

Directed edges arrive one at a time without creating a cycle. The algorithm maintains a total vertex order consistent with every edge. Queries compare two vertices in the maintained order. The target is almost-linear total update time over the whole insertion sequence. Fast cycle detection by itself does not maintain the order required here.

[Read in atlas](index.html#TCS-7339) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1) · [Incremental Strongly Connected Components with Predictions](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2026.17)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0543 — Polylogarithmic dynamic maximal matching against adaptive updates

A graph changes through edge insertions and deletions while an explicit maximal matching must remain available. The next change may depend on the matching the algorithm has just produced. The question asks for an always-correct algorithm with polylogarithmic expected amortized update time against this adaptive feedback. Deterministic algorithms now achieve a square-root-scale amortized bound, resolving the older sublinear threshold. The much stronger polylogarithmic target remains distinct from constant-time results for update sequences fixed independently of the algorithm.

[Read in atlas](index.html#TCS-0543) · [Dynamic Graph Algorithms (Dagstuhl Seminar 22461): Dynamic Maximal Matching](https://doi.org/10.4230/DagRep.12.11.45) · [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0541 — Dynamic spanning trees with polylogarithmic average stretch

A changing unweighted graph must retain a spanning tree in each connected component. The quality measure is the average tree-path length between the endpoints of graph edges. The question asks for polylogarithmic expected quality with sublinear expected amortized work per edge insertion or deletion. The update sequence is fixed independently of the algorithm’s randomness, and disconnected intermediate graphs are covered. Existing subpolynomial-stretch forests and polylogarithmic-stretch metric embeddings leave different parts of this target unresolved.

[Read in atlas](index.html#TCS-0541) · [Dynamic Graph Algorithms (Dagstuhl Seminar 22461): Dynamic Complexity of Low-Stretch Spanning Trees](https://doi.org/10.4230/DagRep.12.11.45) · [Dynamic Low-Stretch Trees via Dynamic Low-Diameter Decompositions](https://arxiv.org/abs/1804.04928) · [Dynamic Maintenance of Low-Stretch Probabilistic Tree Embeddings with Applications](https://arxiv.org/abs/2004.10319)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0536 — Dynamic edge coloring with sublinear additive slack

A changing graph must keep a proper integer color on every edge. The target allows only a power-sublinear additive number of colors above the maximum-degree bound, up to logarithmic factors. One uniform algorithm should maintain that coloring in polylogarithmic expected amortized time over all degree scales. The question remains meaningful even when updates are chosen independently of the algorithm’s randomness. Small recoloring counts and recent restricted-graph or subpolynomial-time results do not by themselves meet the stated total-work guarantee.

[Read in atlas](index.html#TCS-0536) · [Graph Algorithms: Distributed Meets Dynamic (Dagstuhl Seminar 24471): An Open Problem in Dynamic Edge Coloring](https://doi.org/10.4230/DagRep.14.11.92) · [An Open Problem in Dynamic Edge Coloring](https://martin-costa.github.io/martincosta.com/files/Dynamic_Edge_Coloring_Open_Problem.pdf) · [Beyond Vizing Chains: Improved Recourse in Dynamic Edge Coloring](https://arxiv.org/abs/2602.09497) · [Deterministic Dynamic Edge Colouring](https://doi.org/10.1137/1.9781611978971.43)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0545 — Low-loss deterministic reduction from weighted to unweighted dynamic matching

The question asks for a reusable conversion from dynamic unweighted matching to dynamic weighted matching on general graphs. An input algorithm with approximation ratio alpha should yield one with ratio alpha times one minus the chosen accuracy. The selected variant preserves determinism and transfers both worst-case and amortized update guarantees when the input algorithm provides them. The overhead may depend on accuracy but should be only polylogarithmic in graph size and weight range, apart from the stated auxiliary graph enlargement. A recent general-graph conversion works for near-optimal input algorithms, leaving the arbitrary-ratio target unresolved.

[Read in atlas](index.html#TCS-0545) · [Dynamic Graph Algorithms (Dagstuhl Seminar 22461): Reducing weighted matching to unweighted matching](https://doi.org/10.4230/DagRep.12.11.45) · [A Framework for Dynamic Matching in Weighted Graphs](https://doi.org/10.1145/3406325.3451113) · [From Unweighted to Weighted Dynamic Matching in Non-Bipartite Graphs: A Low-Loss Reduction](https://doi.org/10.1137/1.9781611978971.10)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0387 — Logarithmic fully dynamic planar nearest neighbors

The structure maintains points in the Euclidean plane. Queries ask for an exact nearest stored point. Points can both enter and leave the set. Queries must be worst-case logarithmic and updates logarithmic in expected amortized cost. The recent incremental result does not meet the full dynamic target.

[Read in atlas](index.html#TCS-0387) · [The Open Problems Project: Dynamic Planar Nearest Neighbors](https://topp.openproblem.net/p63) · [Incremental Planar Nearest Neighbor Queries with Optimal Query Time](https://arxiv.org/abs/2504.07366)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-3331 — DynFO maintenance of red-predecessor parity

A vertex is covered if some red vertex has a directed edge into it. After each edge or color insertion or deletion, the program must report whether the number of covered vertices is odd. The question permits fixed first-order update formulas and polynomially many auxiliary bits, starting with empty relations. Quantifier-free updates are insufficient, while degree-filtered versions have positive first-order results. The unrestricted query remains open in the expanded source and tests the ability of dynamic first-order logic to handle counting beyond direct-set parity.

[Read in atlas](index.html#TCS-3331) · [Dynamic Complexity of Parity Exists Queries](https://doi.org/10.4230/LIPIcs.CSL.2020.37) · [Dynamic Complexity of Parity Exists Queries](https://doi.org/10.46298/lmcs-17(4:9)2021)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-5209 — Subquadratic exact fully dynamic weighted single-source distances

The data structure maintains exact distances from a fixed source while weighted edges are inserted, removed or changed. Every individual distance query must take constant time. The selected target is a fixed polynomial saving below quadratic worst-case update time in the vertex count. Weights are positive integers of explicitly bounded size and all computation is charged on a specified word-RAM. Known approximate and unweighted improvements do not settle this exact weighted variant.

[Read in atlas](index.html#TCS-5209) · [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2017.44) · [Deterministic Partially Dynamic Single Source Shortest Paths in Weighted Graphs — full version](https://arxiv.org/abs/1705.10097) · [Dynamic Approximate Shortest Paths and Beyond: Subquadratic and Worst-Case Update Time](https://arxiv.org/abs/1909.10850) · [Deterministic Fully Dynamic SSSP and More](https://doi.org/10.1109/FOCS57990.2023.00142)
Existing status: `source_open` · Summary written: 2026-09-13

## String algorithms and computational biology (26)

### TCS-6623 — Worst-case sample complexity of trace reconstruction

A deletion trace independently removes bits of an unknown string while preserving surviving order. The target is the minimum number of traces required for exact worst-case reconstruction at success probability two thirds. Determine its dependence on string length within constant factors for every fixed deletion probability. The estimator has no processing-time restriction, so this measures information rather than computational efficiency. The earlier polynomial-sample conjecture identifies one possible growth regime within this broader function question.

[Read in atlas](index.html#TCS-6623) · [New lower bounds for trace reconstruction](https://www.math.kent.edu/~zchase/tr_lower.pdf) · [New upper bounds for trace reconstruction](https://arxiv.org/abs/2009.03296) · [Trace Reconstruction from Local Statistical Queries](https://arxiv.org/abs/2407.11177) · [Near-Optimal Trace Reconstruction for Mildly Separated Strings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.3) · [New Bounds for Circular Trace Reconstruction](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.30) · [Quasipolynomial Trace Reconstruction](https://arxiv.org/abs/2607.04073)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6624 — Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time

Edit distance is the minimum number of unit-cost insertions, deletions and substitutions transforming one string into another. The question asks for one randomized algorithm with a universal constant approximation factor and only a fixed polylogarithmic overhead beyond linear input length. Its runtime must hold on every execution and its probability of a correct multiplicative estimate must be at least two thirds separately on every pair. Known fixed-slack constant-factor algorithms and earlier subpolynomial or additive approximations do not meet all these requirements simultaneously. The target remains distinct from the two retained questions about arbitrarily accurate estimates at slower stated runtimes.

[Read in atlas](index.html#TCS-6624) · [Edit Distance in Near-Linear Time: It’s a Constant Factor](https://epubs.siam.org/doi/10.1137/21M1392322) · [Edit Distance in Near-Linear Time: it’s a Constant Factor — full manuscript](https://arxiv.org/abs/2005.07678v2) · [Approximating Edit Distance in Near-Linear Time](https://arxiv.org/abs/1109.5635v1) · [Constant factor approximations to edit distance on far input pairs in nearly linear time](https://arxiv.org/abs/1904.05459v2) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702v1) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348v4)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7235 — Almost-linear-time \((1+\varepsilon)\)-approximation of edit distance

Edit distance counts unit-cost insertions, deletions and substitutions needed to transform one string into another. The question asks for an arbitrarily accurate fixed multiplicative estimate on every explicitly stored pair in almost-linear worst-case time. For each accuracy, one randomized algorithm must satisfy every positive fixed exponent slack and succeed separately on every input pair. Known constant-factor algorithms have different accuracy guarantees, while the 2026 near-exact scheme has a weaker stated running-time bound. This target strengthens the retained truly subquadratic near-exact question while remaining distinct from constant-factor approximation with a fixed polylogarithmic overhead.

[Read in atlas](index.html#TCS-7235) · [Approximating Edit Distance](https://theorydish.blog/2018/07/20/approximating-edit-distance/) · [Edit Distance in Near-Linear Time: it’s a Constant Factor](https://arxiv.org/abs/2005.07678v2) · [Edit Distance in Near-Linear Time: It’s a Constant Factor](https://epubs.siam.org/doi/10.1137/21M1392322) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702v1) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348v4)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7220 — Truly subquadratic \((1+\varepsilon)\)-approximation of edit distance

Unit-cost edit distance counts insertions, deletions and substitutions needed to transform one string into another. The question asks whether every fixed positive relative tolerance permits a randomized approximation with a positive fixed saving from the quadratic time exponent. Both the algorithm and the exponent saving may depend on the tolerance but must work on every explicitly stored pair with the stated per-input success probability. The 2026 approximation scheme gives a quasipolynomial speedup over quadratic time without establishing this fixed-exponent guarantee. The target remains distinct from fast coarse approximation and is implied by the stronger retained almost-linear near-exact question.

[Read in atlas](index.html#TCS-7220) · [Approximating Edit Distance](https://theorydish.blog/2018/07/20/approximating-edit-distance/) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702v1) · [Edit Distance in Near-Linear Time: it’s a Constant Factor](https://arxiv.org/abs/2005.07678v2) · [Edit Distance in Near-Linear Time: It’s a Constant Factor](https://epubs.siam.org/doi/10.1137/21M1392322) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348v4)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6669 — Breaking two for sum-of-pairs multiple sequence alignment

The inputs are an arbitrary number of sequences and a metric cost table. An alignment inserts gaps while preserving each sequence. Its objective sums costs over every pair of rows and every column. The question asks for a polynomial-time approximation below two by a fixed constant. An improvement shrinking with the number of sequences does not meet the target.

[Read in atlas](index.html#TCS-6669) · [Some Open Problems in Computational Molecular Biology](https://profs.sci.univr.it/~rrizzi/classes/BioComp2003/homeworks/openProblems.pdf) · [Efficient Methods for Multiple Sequence Alignment with Guaranteed Error Bounds](https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7371 — Almost-linear constant-factor approximation of LCS

Longest common subsequence compares strings while allowing deletions. The alphabet may grow with the input. The requested approximation factor is one universal constant. One randomized algorithm must have almost-linear worst-case running time. Constant-alphabet approximations and slower high-accuracy schemes do not satisfy the combined target.

[Read in atlas](index.html#TCS-7371) · [Exploring the Gap Between LCS and LCStr](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.27) · [Deterministic Longest Common Subsequence Approximation in Near-Linear Time](https://arxiv.org/abs/2507.22486) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7367 — Text-to-pattern Hamming distances below the square-root barrier

The task compares one pattern against every possible text alignment. Every mismatch count must be returned exactly. All preprocessing and output costs are charged. The target saves a fixed power of pattern length over the square-root bound. The known counting-3SUM equivalence does not itself prove the target impossible.

[Read in atlas](index.html#TCS-7367) · [Faster Algorithms for Text-to-Pattern Hamming Distances](https://arxiv.org/abs/2310.13174v3)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7366 — Linear-space k-mismatch text indexing

A text is indexed before query patterns arrive. A query reports all positions with at most a fixed number of substitutions. The proposed structure uses only linear word space. Its cost is pattern length, polylogarithmic overhead and output size. The recent general improvement still uses additional logarithmic factors in space.

[Read in atlas](index.html#TCS-7366) · [Space-Efficient k-Mismatch Text Indexes](https://arxiv.org/abs/2510.26264)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7369 — Space-query exponent curve of gapped string indexing

Queries supply two patterns and an interval of allowed separation. Every matching pair of positions must be reported. The separation is measured between starting positions. The target is the optimal storage exponent as a function of query-overhead exponent. The benchmark requires certified accuracy throughout that function’s domain.

[Read in atlas](index.html#TCS-7369) · [Gapped String Indexing in Subquadratic Space and Sublinear Query Time](https://arxiv.org/abs/2211.16860) · [Improved Time-Space Tradeoffs for 3SUM-Indexing](https://arxiv.org/abs/2512.04258v2)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7374 — Almost-quadratic unweighted tree edit distance

The inputs are rooted ordered trees with symbol labels. Insertion, deletion and relabelling each have unit cost. The task computes the exact minimum edit cost. The proposed bound is almost quadratic in the total number of vertices. The earlier question of obtaining any truly subcubic algorithm has already been surpassed.

[Read in atlas](index.html#TCS-7374) · [Deterministic Monotone Min-Plus Product and Convolution](https://arxiv.org/abs/2605.07150v2) · [Hardness of Dynamic Tree Edit Distance and Friends](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.78)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6513 — Constant-factor approximation of the smallest grammar

A grammar can compress a string by naming repeated pieces and assembling them through acyclic production rules. The question asks for a deterministic polynomial-time approximation within a universal constant of the smallest such grammar. The size measure counts all symbols on right-hand sides, including references to other rules. Choosing repeated pieces is difficult because useful substrings can overlap and interact across scales. The saved review separates this constant-factor target from known logarithmic guarantees and emphasizes that alternative grammar-size conventions describe different optimization problems.

[Read in atlas](index.html#TCS-6513) · [The Smallest Grammar Problem](https://doi.org/10.1109/TIT.2005.850116) · [On the Complexity of the Smallest Grammar Problem over Fixed Alphabets](https://doi.org/10.1007/s00224-020-10013-w)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7297 — Optimal \(\ell\)\(_{1}\) distortion of edit distance

Edit distance counts unit-cost insertions, deletions and substitutions between binary strings. An \(\ell\)\(_{1}\) embedding represents those distances by sums of coordinate differences, up to a common multiplicative distortion. The target is the smallest distortion as a function of string length, within constant factors. Embedding dimension and construction time are unrestricted. The earlier polylogarithmic-distortion question selects one possible growth regime of this extremal function.

[Read in atlas](index.html#TCS-7297) · [Low Distortion Embeddings for Edit Distance](https://doi.org/10.1145/1060590.1060623)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7362 — Optimal top-k document retrieval in compact space

A query asks for the documents in which a pattern occurs most often. Documents are ranked by occurrence count with a fixed tie rule. The desired index occupies only a constant multiple of packed text size. The query cost must match reading the packed pattern and writing the requested identifiers. The current source retains additional space or query overhead.

[Read in atlas](index.html#TCS-7362) · [Top-k Document Retrieval in Compressed Space](https://users.dcc.uchile.cl/~gnavarro/abstracts/soda25.html)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7365 — General-alphabet Hamming oracles with optimal preprocessing

Two strings are preprocessed before their substring comparisons are known. Each query requests the exact Hamming distance between equal-length intervals. A parameter controls the allowed query time. The proposed preprocessing bound matches the constant-alphabet regime. Current general-alphabet bounds have a square-root loss in that parameter.

[Read in atlas](index.html#TCS-7365) · [Hamming Distance Oracles](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7322 — Optimal approximation ratio for shortest common superstring

A common superstring contains every supplied string as a contiguous substring. The objective is to minimize its length over the input alphabet. The target is the infimum approximation ratio of uniform deterministic polynomial-time algorithms. The algorithm must return a feasible string, with input and output costs measured in the stated bit model. The Lean benchmark accepts a certified value of this ratio within absolute error 0.01.

[Read in atlas](index.html#TCS-7322) · [A Tight Cycle-Cover Inequality for Shortest Common Superstring](https://eccc.weizmann.ac.il/report/2026/157/) · [Disproving the Greedy Superstring Conjecture](https://arxiv.org/abs/2609.01365)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7360 — Polyloglogarithmic suffix-array access in compact space

A suffix array orders all suffixes of a string lexicographically. A query asks where a suffix of a given rank starts. The target stores a binary text and its index in linear bits. Each query must take a fixed polynomial in the logarithm of the logarithm of the text length. Constant-time inverse suffix-array access does not settle this direction.

[Read in atlas](index.html#TCS-7360) · [Compressed Inverse Suffix Arrays](https://arxiv.org/abs/2607.17287v2) · [Constant-Time Inverse Suffix Array Queries in Compact Space and Sublinear-Time Construction of Suffix Array Indexes](https://arxiv.org/abs/2608.19123) · [Text Indexing and Searching in Sublinear Time](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2020.24)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7364 — Preprocessing exponent of binary jumbled indexing

The text is binary and queries prescribe counts of zeroes and ones. A query asks whether any substring has exactly those counts. The index has linear word space and constant query time. The target is the best uniform deterministic preprocessing exponent. The numerical benchmark asks for a certified value to absolute accuracy one hundredth.

[Read in atlas](index.html#TCS-7364) · [On Hardness of Jumbled Indexing](https://arxiv.org/abs/1405.0189) · [Deterministic Monotone Min-Plus Product and Convolution](https://arxiv.org/abs/2605.07150v2)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7370 — Polynomial-time construction of minimum-density DNA minimizers

A minimizer chooses the least k-mer in each sliding window. The density measures how often the chosen position changes on random DNA. The desired output is an order with globally minimum density. The running time must be polynomial in the explicit order-table size and window parameter. Known exact exponential search does not meet that resource bound.

[Read in atlas](index.html#TCS-7370) · [GreedyMini: generating low-density DNA minimizers](https://pmc.ncbi.nlm.nih.gov/articles/PMC12261476/) · [Generating minimum-density minimizers](https://doi.org/10.64898/2026.01.25.701585)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-0467 — Linear-space LZ77 random access

An LZ77 parse represents repeated text through references to earlier occurrences, possibly allowing overlap. The reviewed question asks for random character access in logarithmic time using space linear in the number of phrases. The original uncompressed string is unavailable when queries arrive. A solution must navigate arbitrary chains of copied material while keeping every stored shortcut inside the compressed-space budget. The saved record distinguishes ordinary LZ77 from restricted parsing variants and notes that converting to a larger grammar does not automatically preserve the required linear space.

[Read in atlas](index.html#TCS-0467) · [Adaptive and Scalable Data Structures — Two problems on Lempel-Ziv compression](https://doi.org/10.4230/DagRep.15.5.1) · [Balancing Straight-Line Programs](https://arxiv.org/abs/1902.03568) · [Random Access to LZ-End: Faster and Deterministic](https://arxiv.org/abs/2607.14923)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7368 — Faster elastic-degenerate string intersection

Each input describes many strings through ordered sets of alternatives. The task asks whether their represented languages overlap. The inputs are explicit alternatives rather than compressed grammars. The target saves a fixed power over the current algebraic dependence on total alternative length. The running time still pays for reading both representations.

[Read in atlas](index.html#TCS-7368) · [Elastic-Degenerate String Comparison](https://arxiv.org/abs/2411.07782)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7361 — Input-optimal construction of compact inverse suffix arrays

The input is a binary text packed into machine words. The desired static index must answer the exact lexicographic rank of any suffix in constant worst-case time. All retained information and query workspace must occupy a linear number of bits. The question asks whether deterministic construction can take time proportional to the number of packed input words. An August 2026 preprint has a square-root-logarithmic construction gap and a conditional connection to faster Dictionary Matching, while this stronger endpoint remains status-uncertain.

[Read in atlas](index.html#TCS-7361) · [Constant-Time Inverse Suffix Array Queries in Compact Space and Sublinear-Time Construction of Suffix Array Indexes](https://arxiv.org/abs/2608.19123) · [Text Indexing and Searching in Sublinear Time](https://doi.org/10.4230/LIPIcs.CPM.2020.24)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-0468 — Linear-time LZ77 pattern matching

Compressed pattern matching asks whether an explicit pattern occurs in a text supplied only as LZ77 phrases. The reviewed target is deterministic time linear in the phrase count plus pattern length, with comparable working space. Occurrences can cross phrase boundaries or lie inside copied regions, so isolated phrase inspection is insufficient. Such an algorithm would make search depend on the compressed input rather than the potentially enormous expanded text. The statement includes all preprocessing and allows self-referencing phrases, preventing an uncharged index or an easier parsing convention from weakening the target.

[Read in atlas](index.html#TCS-0468) · [Adaptive and Scalable Data Structures](https://doi.org/10.4230/DagRep.15.5.1) · [Pattern matching in Lempel-Ziv compressed strings: fast, simple, and deterministic](https://arxiv.org/abs/1104.4203) · [Pattern Matching on Grammar-Compressed Strings in Linear Time](https://arxiv.org/abs/2111.05016)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0470 — Grammar random access in \(O(g \log  g)\) bits

A straight-line grammar can describe a string exponentially longer than its own rule list. The question asks for logarithmic-time character access with total storage comparable in bits to the grammar encoding. The representation must be built from the grammar in polynomial time without expanding the string. The obstacle is that navigation often stores expansion lengths requiring logarithmically many bits in the much larger text length. The saved review identifies removal of that length-storage overhead as the issue and distinguishes it from linear-word-space grammar access.

[Read in atlas](index.html#TCS-0470) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1) · [Space-Efficient SLP Encoding for \(O(\log  N)\)-Time Random Access](https://doi.org/10.1007/s00224-025-10243-w) · [Random Access in Grammar-Compressed Strings: Optimal Trade-Offs in Almost All Parameter Regimes](https://doi.org/10.4230/LIPIcs.ICALP.2026.86)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7375 — Fully functional suffix trees in BWT-run-linear space

Repetitive texts can have few runs in their Burrows–Wheeler transform. The target stores a complete suffix-tree navigation interface in space proportional to that run count. Tree nodes are represented by their intervals of descendant suffixes. All specified navigation and text-access queries must take polylogarithmic time. Run-linear pattern search alone does not meet the full interface.

[Read in atlas](index.html#TCS-7375) · [Optimal-Time Text Indexing in BWT-runs Bounded Space](https://arxiv.org/abs/1705.10382) · [Non-overlapping Indexing in BWT-Runs Bounded Space](https://par.nsf.gov/servlets/purl/10539699)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-0466 — Certifying Karp–Rabin fingerprints

A string and a prime modulus are supplied as input. Each substring has a polynomial fingerprint using the supplied modulus. The question asks whether any unequal substrings of the same length collide. The target is n log n time with no false certification of a bad modulus. A collision-free modulus may be rejected with bounded probability.

[Read in atlas](index.html#TCS-0466) · [Adaptive and Scalable Data Structures (Dagstuhl Seminar 25191)](https://doi.org/10.4230/DagRep.15.5.1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6928 — Linear-space representation from smallest string attractors

A string attractor is a set of positions intersecting an occurrence of every distinct substring. Its minimum size \(\gamma\) provides a compact measure of repetitive structure. The saved question asks whether every string has an \(O(\gamma )\)-word representation, or at least an asymptotic improvement over the stated \(\gamma  \log  n\) scale. Such a result would clarify whether the attractor's succinct description can be converted into an equally compact usable encoding. The survey note does not specify access requirements or word-size conventions, so a representation-only result must remain distinct from an efficient index.

[Read in atlas](index.html#TCS-6928) · [Indexing Highly Repetitive String Collections](https://arxiv.org/abs/2004.02781)
Existing status: `source_open` · Summary written: 2026-09-11

## Game theory, social choice and fair division (23)

### TCS-6632 — Constant-factor universally truthful auctions for submodular bidders

A combinatorial auction allocates indivisible items among bidders whose bundle values satisfy diminishing returns. The reviewed question asks for a constant-factor welfare approximation using polynomial communication and universal truthfulness. Payments must make honest reporting optimal for every fixed random choice, while values may require exponentially large tables to describe completely. A mechanism would show that strategic incentives need not cause an unbounded welfare loss in this communication model. The saved review distinguishes demand queries from weaker value access and universal truthfulness from truthfulness only in expectation.

[Read in atlas](index.html#TCS-6632) · [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068) · [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf) · [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830) · [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420) · [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0011 — Existence of complete EFX allocations for additive valuations

The problem asks whether every instance with at least four agents and nonnegative additive values admits a complete EFX allocation of indivisible goods. Complete means that each good is assigned to exactly one agent, with empty bundles allowed. For every potentially envious agent i and other bundle \(A_{j}\), removing any good that i values positively must leave a bundle worth at most i’s own bundle. The statement permits zero values and fixes the positive-good EFX convention, without requiring payments or an efficient algorithm. Universal existence would establish this fairness guarantee despite the inability to divide individual goods.

[Read in atlas](index.html#TCS-0011) · [Problem 3: Does EFX always exist?](https://tcsopenproblems.com/problem/3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6639 — Constant-factor approximation for Santa Claus

Max-min allocation distributes indivisible items to agents with arbitrary nonnegative additive values. The question asks for a randomized polynomial-time constant-factor approximation to the best achievable minimum agent value. One simultaneous allocation must serve every agent adequately, so favorable expected values alone are insufficient. The difficulty is that agents compete for items whose value can differ substantially between recipients. The saved review separates this general model from restricted assignment, where each item has a common positive value whenever an agent can use it.

[Read in atlas](index.html#TCS-6639) · [Santa Claus meets Makespan and Matroids: Algorithms and Reductions](https://arxiv.org/abs/2307.08453) · [On Allocating Goods to Maximize Fairness](https://www.cs.dartmouth.edu/~deepc/PUBS/CCK-full.pdf) · [The Submodular Santa Claus Problem](https://arxiv.org/abs/2407.04824) · [Improved Integrality Gap in Max–Min Allocation, or, Topology at the North Pole](https://link.springer.com/article/10.1007/s00493-025-00141-7) · [Submodular Max-Min Allocation under Identical Valuations](https://arxiv.org/abs/2604.12417)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6674 — Randomized truthful unrelated-machine scheduling

Unrelated-machine scheduling assigns jobs to machines with privately known processing times for each job. The question asks for the optimal expected-makespan approximation achievable by truthful-in-expectation mechanisms as the number of machines grows. Random assignments can correlate decisions across jobs while payments discourage strategic misreporting. A constant ratio would show that randomization overcomes the large incentive cost known for deterministic mechanisms. The saved review emphasizes that maximum expected load is different from expected maximum load, and restricted task-independent lower bounds do not settle the unrestricted mechanism class.

[Read in atlas](index.html#TCS-6674) · [A proof of the Nisan–Ronen conjecture](https://arxiv.org/abs/2301.11905) · [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408) · [Setting Lower Bounds on Truthfulness](https://arxiv.org/abs/1507.08708) · [Randomized Truthful Mechanisms for Scheduling Unrelated Machines](https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46) · [An Improved Randomized Truthful Mechanism for Scheduling Unrelated Machines](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2008.1314) · [New Bounds for Truthful Scheduling on Two Unrelated Selfish Machines](https://link.springer.com/article/10.1007/s00224-019-09927-x) · [A proof of the Nisan–Ronen conjecture — Oxford repository copy](https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6633 — Polynomial query complexity of exact envy-free cake cutting

Envy-free cake cutting divides a continuous resource so that nobody prefers another person's share under their own valuation. The reviewed question asks for an exact complete allocation using polynomially many deterministic Robertson–Webb queries. Disconnected pieces are allowed, and local computation between queries is unrestricted. A polynomial protocol would identify a manageable amount of preference information sufficient for exact global fairness. The saved review records a recent single-exponential query upper-bound preprint but distinguishes it from polynomial complexity, approximate fairness, and favorable average-case valuation models.

[Read in atlas](index.html#TCS-6633) · [Envy-free cake cutting: a polynomial number of queries with high probability](https://link.springer.com/article/10.1007/s00355-025-01633-7) · [Thou Shalt Covet Thy Neighbor’s Cake](https://www.cs.umd.edu/~gasarch/TOPICS/cake/lbenvyfreesq.pdf) · [A Discrete and Bounded Envy-Free Cake Cutting Protocol for Any Number of Agents](https://arxiv.org/abs/1604.03655) · [An Exponential Envy-Free Cake Cutting Protocol for n Agents](https://arxiv.org/abs/2306.03854) · [Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting](https://arxiv.org/abs/2609.05191) · [The Query Complexity of Cake Cutting](https://proceedings.neurips.cc/paper_files/paper/2022/file/f7a7bb369e48f10e85fce85b67d8c516-Paper-Conference.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6634 — Randomized metric distortion in social choice

What is the smallest universal expected metric distortion achievable from full voter rankings? The voting rule selects a lottery without seeing the distances that produced those rankings. The former value-two conjecture is false, with a general lower bound around 2.11264. A preprint dated 8 September 2026 states an upper bound of 2.13713, leaving a nonzero gap. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-6634) · [Metric Distortion for Tournament Voting and Beyond](https://arxiv.org/abs/2505.13630) · [Metric Distortion Bounds for Randomized Social Choice](https://arxiv.org/abs/2111.03694) · [An improved bound for the randomized metric distortion problem](https://arxiv.org/abs/2608.17863) · [Improving Randomized Metric Distortion to 2.1441](https://arxiv.org/abs/2608.29308v2) · [Stable Voting Rules on the Edge of Optimal Metric Distortion](https://arxiv.org/abs/2609.08259v1)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7196 — Polynomial-time EFX for three additive agents

Three agents must receive all indivisible goods under nonnegative additive valuations. An allocation is EFX when removing any one good from another agent’s bundle would eliminate the first agent’s envy. Such allocations are known to exist for three agents, including when values are zero or tied. The question asks for a deterministic algorithm polynomial in the binary valuation table’s length. Pseudopolynomial constructions and polynomial algorithms for weaker fairness guarantees do not settle this target.

[Read in atlas](index.html#TCS-7196) · [EFX Exists for Three Agents](https://arxiv.org/abs/2002.05119v3) · [EF2X Exists for Four Agents](https://ojs.aaai.org/index.php/AAAI/article/view/33480) · [Approximate Envy-Free Allocations up to any k Goods](https://arxiv.org/abs/2605.10371v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7197 — Polynomial-time approximation of EFX

All indivisible goods must be allocated among agents with nonnegative additive values. An \(\alpha -\mathrm{EFX}\) allocation lets each agent retain at least an \(\alpha\) fraction of the value she assigns to any other bundle after any one good is removed. The question asks for the supremum factor guaranteed by deterministic polynomial-time algorithms for arbitrarily many agents. A general factor of about 0.618 is known, while recent \(2/3\) guarantees cover only bounded numbers of agents. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-7197) · [Fair division of indivisible goods: Recent progress and open questions](https://doi.org/10.1016/j.artint.2023.103965) · [Multiple Birds with One Stone: Beating \(1/2\) for EFX and GMMS via Envy Cycle Elimination](https://arxiv.org/abs/1909.07650v2) · [Approximate Envy-Free Allocations up to any k Goods](https://arxiv.org/abs/2605.10371v1)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7200 — Multiplicative MMS guarantee for chores

Chores are indivisible tasks whose costs add, and each agent prefers a smaller burden. Her minimax share is the lowest worst-bundle cost she can obtain by partitioning all chores among the agents. The question asks for the smallest universal factor by which every agent’s share must be relaxed to make a complete allocation possible. The checked general bounds are \(44/43\) and \(13/11\), while stronger guarantees for restricted costs do not close this gap. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-7200) · [How to Fairly Allocate Easy and Difficult Chores](https://arxiv.org/abs/2110.11285) · [A tight negative example for MMS fair allocations](https://arxiv.org/abs/2104.04977v2) · [A Reduction from Chores Allocation to Job Scheduling](https://arxiv.org/abs/2302.04581v4) · [Improved Maximin Share Approximations for Chores by Bin Packing](https://ojs.aaai.org/index.php/AAAI/article/view/33518) · [Comparison-Based Fair Division of Indivisible Chores](https://arxiv.org/abs/2609.08687v1)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-1116 — Optimal universal approximation factor for EFX

The target is the best multiplicative EFX fairness factor that every finite additive-goods instance admits. Every good must be allocated, and the comparison removes any good that the potentially envious agent values positively. There is no bound on the number of agents and no computational-time restriction on choosing the allocation. Known universal guarantees reach the golden-ratio factor, while stronger results impose instance restrictions or allow removal of more goods. The benchmark asks for a Lean-certified numerical answer within one hundredth, which need not decide exact EFX existence.

[Read in atlas](index.html#TCS-1116) · [Fair Division of Indivisible Goods: A Survey](https://arxiv.org/abs/2202.07551) · [Multiple Birds with One Stone: Beating 1/2 for EFX and GMMS via Envy Cycle Elimination](https://doi.org/10.1016/j.tcs.2020.07.006) · [Pushing the Frontier on Approximate EFX Allocations](https://arxiv.org/abs/2406.12413) · [Approximate Envy-Free Allocations up to any k Goods](https://arxiv.org/abs/2605.10371)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7203 — Bounded protocols for connected envy-free proportional cake cutting

The cake is a divisible interval valued differently by each agent. The desired division gives every agent one interval, eliminates envy, and guarantees at least one n-th of her value for the whole cake. Unallocated cake is allowed, but it cannot reduce that proportionality guarantee. Known connected partial protocols provide weaker guarantees for larger numbers of agents, while recent complete protocols allow fragmented shares. The question is whether a fixed finite query bound can achieve all the requested properties for every fixed \(n\ge 4\).

[Read in atlas](index.html#TCS-7203) · [Waste Makes Haste: Bounded Time Protocols for Envy-Free Cake Cutting with Free Disposal](https://arxiv.org/abs/1511.02599) · [A Discrete and Bounded Envy-Free Cake Cutting Protocol for Any Number of Agents](https://arxiv.org/abs/1604.03655) · [Envy-Free Cake Divisions Cannot Be Found by Finite Protocols](https://www.cs.umd.edu/~gasarch/TOPICS/cake/lbenvyfree.pdf) · [Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting](https://arxiv.org/abs/2609.05191)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0056 — Universal maximin-share approximation for additive goods

Each agent’s maximin share is the best value they can secure by partitioning the goods and receiving a least-valued bundle. The target is the largest fraction of those personal shares that can always be met simultaneously for nonnegative additive valuations. It ranges over all finite numbers of agents and indivisible goods, with equal entitlements and no sharing. Determining this constant would quantify the inherent loss of fairness caused by indivisibility, independently of computational efficiency. The card requires a Lean-certified absolute error of at most one hundredth and records the precise versions and limits of the known bounds.

[Read in atlas](index.html#TCS-0056) · [Best α for α-MMS existence](https://tcsopenproblems.com/problem/4) · [A tight negative example for MMS fair allocations](https://arxiv.org/abs/2104.04977v2) · [Improved Maximin Share Guarantee for Additive Valuations](https://arxiv.org/abs/2510.10423v1) · [An FPTAS for 7/9-Approximation to Maximin Share Allocations](https://arxiv.org/abs/2511.13056v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1115 — Polynomial-time EF1 and Pareto-optimal goods allocation

EF1 allows an agent's envy to disappear after removing one suitable good from the envied bundle. The survey asks for a polynomial-time allocation satisfying both EF1 and Pareto optimality. Pareto optimality prevents improving one person's value without reducing somebody else's value. Combining the two conditions would make an allocation both approximately fair and resistant to obvious welfare improvements. The saved note does not state valuation access or numeric encoding, so existence alone or an algorithm whose runtime depends on value magnitudes would not automatically meet the intended polynomial-time target.

[Read in atlas](index.html#TCS-1115) · [Fair Division of Indivisible Goods: A Survey](https://www.cs.toronto.edu/~nisarg/teaching/2556s22/papers/fair-division-survey.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1109 — EF1 and Pareto optimality for additive mixed items

Mixed-item allocation permits items that an agent regards as beneficial or burdensome. The recorded question asks for EF1 together with Pareto optimality under additive utilities. Removing a good from another bundle and removing a chore from one's own bundle can affect envy in different ways. A general existence or computation result would extend a central fairness–efficiency pairing beyond all-goods settings. The source title does not specify the mixed EF1 convention or whether the target is existence versus efficient construction, so those choices must be kept explicit.

[Read in atlas](index.html#TCS-1109) · [Mixed Fair Division: A Survey](https://arxiv.org/abs/2306.09564)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1108 — EF1 existence for arbitrary mixed-item utilities

Agents divide a finite set of indivisible items, and each agent may assign an arbitrary real utility to every bundle. The question asks whether a complete EF1 allocation always exists for three or more agents. For each envy comparison, EF1 permits ignoring at most one item from either the envious agent’s own bundle or the other bundle. An item’s effect may depend on its companions, so the model does not assume a fixed division into goods and chores. The 2026 existence results allowing one removal from each bundle do not settle this stricter one-item question.

[Read in atlas](index.html#TCS-1108) · [Mixed Fair Division: A Survey](https://arxiv.org/abs/2306.09564) · [Approximately Envy-free and Equitable Allocations of Indivisible Items for Non-monotone Valuations](https://doi.org/10.1609/aaai.v40i20.38712)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1119 — Existence of pairwise maximin-share allocations

Pairwise maximin-share fairness compares an agent's bundle with what they could guarantee by repartitioning it together with another agent's bundle. The survey asks whether allocations satisfying all these pairwise requirements always exist. Each pair induces its own two-way fairness benchmark, and the resulting comparisons can conflict across pairs. Universal existence would provide a strong local form of fairness tied to each agent's own valuation. The saved note does not state the valuation assumptions or complete allocation convention, so those conditions are necessary before asserting a theorem for all indivisible-goods instances.

[Read in atlas](index.html#TCS-1119) · [Fair Division of Indivisible Goods: A Survey](https://www.cs.toronto.edu/~nisarg/teaching/2556s22/papers/fair-division-survey.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0073 — Polynomial-time mixed equilibria in coordination polymatrix games

Each player uses one action across several pairwise interactions in a graph. The two endpoints of each edge receive equal payoffs from that interaction. The target is a deterministic polynomial-time algorithm returning any exact mixed Nash equilibrium. Pure equilibria are permitted outputs, but an algorithm may also use genuinely mixed profiles. Known pure-equilibrium and adversarial two-team hardness results do not settle this coordination-only mixed search task.

[Read in atlas](index.html#TCS-0073) · [Equilibrium Computation](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.4.8.73) · [On Minmax Theorems for Multiplayer Games](https://people.csail.mit.edu/costis/network2.pdf) · [The Complexity of Two-Team Polymatrix Games with Independent Adversaries](https://arxiv.org/abs/2409.07398)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0571 — Positional Nash Equilibria

A Nash equilibrium is a profile of strategies from which no single player can profitably deviate. The project asks whether multiplayer reachability, Büchi and parity games always admit such a profile using only positional strategies. Positional choices depend on the current vertex and carry no separate memory of the play. General existence arguments may rely on remembered deviations and punishments, so they do not establish the stronger claim. A proof or counterexample would show whether simple infinite-duration objectives can always support rational behavior without historical bookkeeping.

[Read in atlas](index.html#TCS-0571) · [Automata Exchange](https://automata.exchange/24.02-positional-nash-equilibria/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1714 — Polynomial-time stable matching in unimodular hypergraphs

Vertices are participants and hyperedges are feasible coalitions. Each participant strictly ranks the coalitions containing them. A stable matching leaves no unchosen coalition preferred by all its members. Total unimodularity guarantees existence, but the question asks for an efficient construction. An August 2026 preprint addresses network hypergraphs while the full unimodular target remains open in the checked sources.

[Read in atlas](index.html#TCS-1714) · [Stable Hypergraph Matching in Unimodular Hypergraphs](https://doi.org/10.4230/LIPIcs.ICALP.2025.31) · [Polynomial-time Stable Matching in Network Hypergraphs](https://arxiv.org/abs/2608.24728)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2427 — Zero-sum stochastic games with variable discount factors

Turn-based stochastic games combine sequential player choices, random transitions, and rewards extending over an infinite horizon. The cited passage asks about computing exact or approximate Nash equilibria even for zero-sum games as the discount factor increases. A discount factor approaching one makes remote future rewards increasingly relevant. Understanding this regime would clarify whether equilibrium computation scales efficiently with a long effective planning horizon. The saved sentence does not specify the encoding of discount factors or the approximation tolerance, both of which are necessary to distinguish polynomial complexity from parameter-dependent guarantees.

[Read in atlas](index.html#TCS-2427) · [The Complexity of Infinite-Horizon General-Sum Stochastic Games](https://doi.org/10.4230/LIPIcs.ITCS.2023.76)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4584 — Nash equilibria in concurrent terminal-reward games

Two players act simultaneously in a finite state graph. A terminal state pays each player a nonnegative reward once; infinite nonterminating play pays zero. The question asks whether an exact Nash equilibrium always exists in randomized state-history strategies with unrestricted memory. Negative terminal rewards already admit counterexamples. A later existence theorem uses imprecise deviations and does not settle the exact question.

[Read in atlas](index.html#TCS-4584) · [Mixed Nash Equilibria in Concurrent Terminal-Reward Games](https://doi.org/10.4230/LIPIcs.FSTTCS.2014.351) · [Stochastic Equilibria under Imprecise Deviations in Terminal-Reward Concurrent Games](https://doi.org/10.4204/EPTCS.226.5)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6957 — Characterizing domains restricted to affine maximizers

An affine maximizer chooses an allocation maximizing a weighted sum of reported values plus fixed outcome offsets. The textbook asks which valuation domains make these the only allocation rules implementable with truthful incentives. Rich domains can constrain how reports may change outcomes if payments are to deter manipulation. A characterization would identify when mechanism design is forced into this familiar optimization form. The saved 2007 question does not spell out domain richness or incentive conventions, so the classification must not be extended automatically to restricted valuations or weaker equilibrium implementation notions.

[Read in atlas](index.html#TCS-6957) · [Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6958 — Algorithmic versus dominant-strategy implementation

Mechanism implementation connects an allocation algorithm with strategic behavior that makes its intended outcome attainable. The textbook asks whether efficient algorithmic implementation can approximate better than every efficient dominant-strategy implementation. Dominant strategies require honest behavior to be optimal regardless of others' reports, imposing a particularly strong incentive condition. A separation would quantify the algorithmic value of a weaker implementation framework. The saved historical note does not define that framework or choose the optimization objective, so the proposed comparison needs those details before it becomes one concrete approximation separation.

[Read in atlas](index.html#TCS-6958) · [Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

## Algebraic computation (61)

### TCS-0007 — Matrix multiplication exponent

The matrix multiplication exponent measures the least asymptotic power of n needed by exact arithmetic circuits for multiplying two complex n by n matrices. The target permits a separate circuit for every size and counts all addition, subtraction and multiplication gates. Its infimum may be approached without an algorithm attaining the endpoint exponent. The accepted answer must locate the exponent with a Lean-certified absolute error of at most 0.01. Recent upper bounds and lower bounds for restricted tensor methods do not yet give a matching interval for the unrestricted optimum.

[Read in atlas](index.html#TCS-0007) · [Gaussian elimination is not optimal](https://doi.org/10.1007/BF02165411) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Limits on the Universal Method for Matrix Multiplication](https://arxiv.org/abs/1812.08731) · [More Asymmetry Yields Faster Matrix Multiplication](https://doi.org/10.1137/1.9781611978322.63) · [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884v1) · [More Asymmetry Yields Faster Matrix Multiplication — August 2026 revision](https://arxiv.org/abs/2404.16349v3)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6611 — Permanent versus determinant

The permanent sums permutation products without the signs used by the determinant. The question asks whether its representation as a determinant of affine-linear forms can be bounded in dimension by any polynomial in the original matrix size. Every complex coefficient and every reuse of input variables is allowed, with no symmetry or uniform construction requirement. A superpolynomial lower bound would exclude polynomial-size algebraic branching programs and formulas for the permanent, while a polynomial-size representation would collapse VP and VNP. A complete Lean proof must establish nonexistence of every polynomial bound or prove a polynomial-size exact family; restricted symmetry bounds, limiting representations and results for other polynomials do not settle this target.

[Read in atlas](index.html#TCS-6611) · [A Lower Bound on Determinantal Complexity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.4) · [A quadratic bound for the determinant and permanent problem](https://math.univ-lyon1.fr/~ressayre/PDFs/permdet.pdf) · [Permanent v. determinant: An exponential lower bound assuming symmetry and a potential path towards Valiant’s conjecture](https://doi.org/10.1016/j.difgeo.2017.03.017) · [The Algebraic Cost of a Boolean Sum](https://doi.org/10.4230/LIPIcs.FSTTCS.2025.47) · [Bounds on determinantal complexity of two types of generalized permanents](https://www.sciencedirect.com/science/article/pii/S0304397526001210) · [A near-quadratic lower bound on the border determinantal complexity of \(\sum_i x_i^n\) via conormal specialization](https://arxiv.org/abs/2606.13628v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6666 — Shub–Smale \(\tau\)-conjecture

A straight-line program constructs an integer polynomial using only one, a variable, addition, subtraction and multiplication. The conjecture asks for one fixed polynomial bound on the number of distinct integer roots in terms of the shortest program length. All operations constructing constants count, shared registers are allowed, and the zero polynomial is excluded. A short program can already create exponential degree or exponentially many distinct real roots, so neither supplies the desired integer-root bound. The conjecture has major conditional consequences in algebraic computation and proof complexity, while finite censuses and bounds in other complexity measures leave its universal claim unsettled.

[Read in atlas](index.html#TCS-6666) · [On the intractability of Hilbert’s Nullstellensatz and an algebraic version of “\(\mathrm{NP}\ne\mathrm P\)?”](https://doi.org/10.1215/S0012-7094-95-08105-8) · [Mathematical Problems for the Next Century](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/muller/SmaleProblems1998.pdf) · [A Direct Ultrametric Approach to Additive Complexity and the Shub-Smale Tau Conjecture](https://arxiv.org/abs/math/0304100v2) · [Semialgebraic Proofs, IPS Lower Bounds, and the \(\tau\)-Conjecture: Can a Natural Number be Negative?](https://doi.org/10.1137/20M1374523) · [The bottom of the Shub-Smale tau conjecture: an exact census of integer roots for constant-free straight-line programs of length at most eight](https://zenodo.org/records/22035884)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6612 — VP versus VBP over the complex numbers

VP versus VBP asks whether every polynomial-degree family with small arithmetic circuits also has small algebraic branching programs over the complex numbers. The branching programs compute exact sums of affine-label products along paths, with all coefficients and variable occurrences included in the algebraic size. Both models are nonuniform and allow arbitrary complex constants, with no imposed symmetry, width or multilinearity restriction. A complete Lean-checked answer must establish the universal polynomial simulation or one circuit-easy family requiring superpolynomial branching-program size. The question would decide whether determinant-like computation captures general efficient algebraic computation, beyond the known quasipolynomial simulations and restricted-model results.

[Read in atlas](index.html#TCS-6612) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/) · [Homogeneous Algebraic Complexity Theory and Algebraic Formulas](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.43) · [Factorization of Polynomials Given by Arithmetic Branching Programs](https://doi.org/10.1007/s00037-021-00215-0) · [Lower Bounds in Algebraic Complexity via Symmetry and Homomorphism Polynomials](https://arxiv.org/abs/2601.09343) · [Multilinear Algebraic Branching Programs and the Min-Partition Rank Method](https://eccc.weizmann.ac.il/report/2026/001/) · [Factorization of Polynomials Given By Arithmetic Branching Programs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2020.33)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0005 — VP versus VNP

The permanent sums one matrix-entry product for each permutation of the columns. The question is whether this exponentially described polynomial nevertheless has arithmetic circuits of polynomial size over the complex numbers. Because circuits can reuse expressions and cancel terms, counting its monomials does not establish a lower bound. The problem captures the VP versus VNP question and tests whether algebraically summing efficiently described contributions is inherently expensive. The saved formulation permits arbitrary complex constants but requires exact polynomial equality, so approximation or limits of circuits would address different models.

[Read in atlas](index.html#TCS-0005) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Completeness Classes in Algebra](https://doi.org/10.1145/800135.804419) · [Superpolynomial Lower Bounds Against Low-Depth Algebraic Circuits](https://eccc.weizmann.ac.il/report/2021/081/) · [Arithmetic circuit lower bounds from sumset expansion](https://eccc.weizmann.ac.il/report/2026/138/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6613 — Polynomial-size arithmetic formulas for the determinant

The determinant is efficiently computed with arithmetic circuits that can reuse intermediate expressions. This question asks whether polynomial-size arithmetic formulas, whose computation graphs are trees, can also compute it exactly. Each reused subexpression must be copied in a formula, making sharing the central resource under investigation. Resolving the problem would clarify whether a basic linear-algebra operation witnesses a superpolynomial difference between expression trees and circuits. The formulation allows cancellation and arbitrary complex constants, so lower bounds restricted to multilinear, monotone, or bounded-depth formulas do not settle it.

[Read in atlas](index.html#TCS-6613) · [On computing the determinant in small parallel time using a small number of processors](https://www.sciencedirect.com/science/article/pii/0020019084900188) · [A Lower Bound for the Formula Size of Rational Functions](https://epubs.siam.org/doi/10.1137/0214050) · [Multi-Linear Formulas for Permanent and Determinant are of Super-Polynomial Size](https://eccc.weizmann.ac.il/report/2003/067/) · [Schur Polynomials do not have small formulas if the Determinant doesn’t!](https://arxiv.org/abs/1911.12520) · [Multilinear Formula Lower Bounds for Sparse Determinants](https://eccc.weizmann.ac.il/report/2026/090/) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6641 — Word problem for one-relation monoids

A one-relation monoid allows words to be transformed by repeatedly replacing one fixed word with another in either direction. The reviewed question asks for an algorithm deciding whether two given words become equal under these replacements. Successful derivations can be found by enumeration, but failure to find one does not certify inequality. Decidability would show that even unrestricted length-changing interaction from one rule admits an effective stopping criterion. The saved review notes that finite search works for length-preserving relations, while simple shortening rules need not produce unique normal forms.

[Read in atlas](index.html#TCS-6641) · [The word problem for one-relation monoids: a survey](https://link.springer.com/article/10.1007/s00233-021-10216-8) · [Correction to: The word problem for one-relation monoids: a survey](https://link.springer.com/article/10.1007/s00233-022-10310-5) · [On the Dehn functions of a class of monadic one-relation monoids](https://arxiv.org/abs/2210.16123) · [The word problem for two-generator one-relator inverse monoids](https://arxiv.org/abs/2608.04650)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6614 — Deterministic polynomial-time factorization over finite fields

The input is a densely represented univariate polynomial over a finite field whose representation is explicitly supplied. The task is to output all irreducible factors and their multiplicities deterministically in time polynomial in the degree and the logarithm of the field size. This is an exact derandomization question for a central computer-algebra subroutine. The complexity bound must work uniformly across characteristics and extension degrees, with field arithmetic and output writing charged in bit operations. A method relying on randomness, unproved number-theoretic assumptions, or precomputed field-specific advice would leave the stated challenge unresolved.

[Read in atlas](index.html#TCS-6614) · [Deterministic polynomial factorisation modulo many primes](https://arxiv.org/abs/2509.12705) · [Factoring Polynomials Over Finite Fields: A Survey](https://people.csail.mit.edu/dmoshkov/courses/codes/poly-factorization.pdf) · [Deterministic polynomial factoring over finite fields: a uniform approach via P-schemes](https://zeyuguo.bitbucket.io/papers/pscheme.pdf) · [A number-theoretic conjecture implying faster algorithms for polynomial factorization and integer factorization](https://arxiv.org/abs/2511.10851) · [On Factorization of Sparse Polynomials of Bounded Individual Degree](https://eccc.weizmann.ac.il/report/2026/036/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6642 — Conjugacy problem for one-relator groups

Conjugacy asks whether two group elements differ by a transformation of the form \(w^{- 1}uw\). The reviewed question seeks one algorithm deciding this for every finitely presented group with a single defining relation. Equality of words is decidable in these groups, but searching possible conjugators only semidecides positive answers. An algorithm would settle a classical decision problem for a remarkably concise family of infinite algebraic structures. The saved review explains that decomposition methods preserving word-problem decidability do not automatically preserve decidable conjugacy.

[Read in atlas](index.html#TCS-6642) · [The theory of one-relator groups: history and recent progress](https://arxiv.org/abs/2501.18306) · [Some aspects of one-relator groups](https://researchonline.jcu.edu.au/58078/) · [One-relator groups with torsion are conjugacy separable](https://arxiv.org/abs/1211.0488) · [Undecidable Diophantine problems in generalisations of one-relator groups](https://arxiv.org/abs/2605.30535) · [Undecidability of the Diophantine problem for one-relator groups and one-relation monoids](https://arxiv.org/abs/2608.01983) · [The word problem for two-generator one-relator inverse monoids](https://arxiv.org/abs/2608.04650)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6677 — Isomorphism problem for one-relator groups

Two group presentations can describe the same abstract group despite using different generators and relations. The reviewed question asks to decide isomorphism between arbitrary finite one-relator presentations. Candidate mutually inverse homomorphisms can be enumerated and checked using the known word algorithm. The missing ingredient is an effective way to stop when no such isomorphism exists. A solution would distinguish complete algebraic types within this concise presentation class, extending beyond equality and conjugacy questions about elements of one already fixed group.

[Read in atlas](index.html#TCS-6677) · [The theory of one-relator groups: history and recent progress](https://arxiv.org/abs/2501.18306) · [The isomorphism problem for all hyperbolic groups](https://arxiv.org/abs/1002.2590) · [Generic properties of Whitehead's Algorithm and isomorphism rigidity of random one-relator groups](https://arxiv.org/abs/math/0303386) · [Small Cancellation Stability and Isomorphism Rigidity for Generic Finitely Presented Groups](https://arxiv.org/abs/2608.17238) · [Undecidability of the Diophantine problem for one-relator groups and one-relation monoids](https://arxiv.org/abs/2608.01983)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7113 — Derandomizing polynomial identity testing

An arithmetic circuit may compute the zero polynomial even when cancellation is difficult to see from its graph. The question asks for an exact deterministic polynomial-time test given the entire circuit over binary-encoded integer constants. Circuits may reuse intermediate results, have arbitrary depth and compute polynomials of exponential degree. Randomized polynomial-time tests are known, while removing their randomness would have major circuit lower-bound consequences. Recent deterministic results for restricted circuit shapes do not provide the requested algorithm for all explicit circuits.

[Read in atlas](index.html#TCS-7113) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042) · [Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds](https://www.cs.sfu.ca/~kabanets/Research/poly.html) · [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](https://doi.org/10.4230/LIPIcs.STACS.2026.25) · [Polynomial Identity Testing and Reconstruction for Depth-4 Powering Circuits of High Degree](https://arxiv.org/abs/2602.20832v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7174 — Bit complexity of integer multiplication

What is the optimal worst-case bit complexity of multiplying two n-bit integers? The model charges individual steps of a fixed deterministic multitape Turing machine. An \(O(n \log  n)\) algorithm is known, but only a linear general lower bound is established. A 2025 theorem connects the conjectured matching lower bound to the unresolved cost of matrix transposition. Bounds for restricted branching programs do not determine the optimal cost in this model.

[Read in atlas](index.html#TCS-7174) · [Integer multiplication in time \(O(n \log  n)\): publisher abstract](https://annals.math.princeton.edu/2021/193-2/p04) · [Integer multiplication is at least as hard as matrix transposition](https://arxiv.org/abs/2503.22848) · [Upper and lower bounds on the OBDD-width of a special integer multiplication](https://arxiv.org/abs/2608.30664)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6615 — Polynomial-time finite-group isomorphism in the Cayley-table model

Two finite groups are supplied by complete tables describing their multiplication operations. The question asks for a deterministic polynomial-time algorithm deciding whether a bijection preserves those operations. Using full tables makes the representation explicit, so the running-time target is measured against table-sized input rather than a succinct group description. Group isomorphism tests whether apparently different multiplication systems encode the same algebraic structure, making it a fundamental classification problem. The saved formulation does not impose a structural promise on the groups, and algorithms for particular group families therefore address only restricted cases.

[Read in atlas](index.html#TCS-6615) · [Research reference · drops.dagstuhl.de](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2024.4)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6898 — Derandomizing black-box depth-four PIT

The question asks for a deterministic polynomial-time construction of evaluation points that detect every nonzero polynomial computed by a size-bounded depth-four arithmetic circuit. The same generated set must work for every circuit of the given size without seeing its coefficients or gates. The model charges field operations and output length, and explicitly permits a sufficiently large working field. There is no constant bound on the top fan-in or bottom degree and no homogeneity or multilinearity assumption. Recent polynomial-time results impose fixed fan-in, quadratic factors or powering restrictions, while the general target remains unresolved in the checked literature.

[Read in atlas](index.html#TCS-6898) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Deterministic Identity Testing Paradigms for Bounded Top-Fanin Depth-4 Circuits](https://doi.org/10.4230/LIPIcs.CCC.2021.11) · [Rank Bounds and Polynomial-Time PIT for \(\Sigma^k\Pi\Sigma\Pi^2\) Circuits](https://eccc.weizmann.ac.il/report/2026/084/download/) · [Polynomial Identity Testing and Reconstruction for Depth-4 Powering Circuits of High Degree](https://arxiv.org/abs/2602.20832)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-7175 — Unrestricted arithmetic lower bounds for the discrete Fourier transform

Must the discrete Fourier transform take order n log n exact arithmetic operations when constants are unrestricted? The target covers every sufficiently large power-of-two input length and all straight-line programs in the stated model. The FFT achieves this cost by sharing intermediate computations. Known matching lower bounds impose coefficient, gate, storage or conditioning restrictions. Normalization, bit precision and quantum state transformations require care because their computational models differ.

[Read in atlas](index.html#TCS-7175) · [The Division Barrier: Optimal Bounds and Structural Limits in Toom-Cook Interpolation](https://epubs.siam.org/doi/10.1137/1.9781611978971.190) · [Lower Bounds on the Bounded Coefficient Complexity of Bilinear Maps](https://arxiv.org/abs/cs/0301016) · [A Lower Bound for Fourier Transform Computation in a Linear Model Over 2x2 Unitary Gates Using Matrix Entropy](https://arxiv.org/abs/1305.4745) · [Paraunitary Matrices, Entropy, Algebraic Condition Number and Fourier Computation](https://arxiv.org/abs/1609.03278v6)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6616 — Uniform exact permanent circuits below base two

The permanent is the unsigned sum of permutation products of a square matrix. This card asks whether exact division-free rational circuits can beat exponential base two while being generated uniformly within the same exponential bound. The generated polynomial must work for every matrix over every characteristic-zero field, with bit costs for circuit construction separated from field-operation costs for evaluation. Checked recent results give conditional circuit improvements, finite-ring algorithms, bounded-entry bit-time savings or lower bounds for restricted formula classes. A complete Lean proof must establish the specified uniform circuit family with a fixed positive base saving or rule out every family meeting these conventions.

[Read in atlas](index.html#TCS-6616) · [Kronecker Scaling of Tensors with Applications to Arithmetic Circuits and Algorithms](https://doi.org/10.4230/LIPIcs.ICALP.2026.36) · [Computing Permanents and Counting Hamiltonian Cycles by Listing Dissimilar Vectors](https://doi.org/10.4230/LIPIcs.ICALP.2019.25) · [Counting Perfect Matchings and Hamiltonian Cycles Faster](https://arxiv.org/abs/2309.15422v2) · [Ryser, Glynn, and the discrete Fourier transform: orthogonal schemes for the permanent](https://arxiv.org/abs/2607.09949v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-5520 — NP-hardness of PosSLP

The target is unconditional NP-hardness of deciding whether a succinctly represented integer is positive. The integer is produced by a straight-line program starting from one and using only addition, subtraction and multiplication. The required reduction must deterministically convert each 3-SAT instance to one such program in polynomial bit time. Known conditional consequences for randomized algorithms and unconditional hardness of polynomial variants do not supply this reduction. A complete answer would clarify the discrete complexity of exact sign testing without also requiring a proof that P and NP differ.

[Read in atlas](index.html#TCS-5520) · [PosSLP and Sum of Squares](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.13) · [On the Hardness of PosSLP](https://goravjindal.github.io/assets/pdf/posslpsoda2024.pdf) · [Beyond Bits: An Introduction to Computation over the Reals](https://arxiv.org/abs/2603.29427)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0481 — Cubic min-plus circuit lower bounds for shortest paths

A min-plus circuit computes by a fixed network of minimum and addition gates. The question asks whether even one shortest-path distance in a complete nonnegatively weighted graph requires cubic circuit size. Ordinary graph algorithms can branch on comparisons and therefore need not translate into equally small circuits. Repeated relaxation provides a cubic upper bound, while dependence on all edge inputs gives only a weaker basic lower bound. The project seeks to understand how much sharing fixed tropical computations can achieve across competing paths.

[Read in atlas](index.html#TCS-0481) · [Lower Bounds for Tropical Circuits and Dynamic Programs](https://doi.org/10.1007/s00224-014-9574-4) · [Semirings in Databases, Automata, and Logic (Dagstuhl Seminar 25081)](https://doi.org/10.4230/DagRep.15.2.89) · [Supplements to Tropical Circuit Complexity](https://web.vu.lt/mif/s.jukna/tropical/comments.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7269 — Optimal multilinear-formula size of the permanent

The permanent is a canonical polynomial whose algebraic complexity captures a major explicit lower-bound challenge. A formula is a tree of additions and multiplications without shared intermediate results. Every intermediate polynomial must be multilinear, with complex constants and cancellation permitted. The question asks for the growth of the logarithm of the smallest formula size, up to constant factors. The known quasipolynomial lower bound and exponential upper bound leave a qualitative gap, with an exponential lower bound as the original conjectured endpoint.

[Read in atlas](index.html#TCS-7269) · [P=?NP](https://eccc.weizmann.ac.il/report/2017/004/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-1058 — Explicit rigidity at rank n over log log n

Matrix rigidity measures how many entries must be changed before a matrix's rank falls below a target. This entry asks for explicit matrices that remain sufficiently rigid at rank roughly n divided by log log n. The explicitness requirement seeks a concrete computable family rather than an existence argument based on typical matrices. Such constructions connect linear-algebra structure to lower bounds for computational representations. The saved label identifies the rank scale but omits the required number of entry changes and field, so it cannot yet support a numerical rigidity conjecture or a particular circuit consequence.

[Read in atlas](index.html#TCS-1058) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/index.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0055 — Sum-of-square-roots problem

The saved entry identifies the sum-of-square-roots problem, an exact comparison question involving quantities described by radicals. Its geometric relevance comes from distances that can be written as square roots even when the underlying coordinates are simple. The computational difficulty is deciding a comparison reliably when two such expressions are extremely close. The catalogue currently preserves only an index label and a pointer to the original problem collection, rather than its complete input conventions or requested complexity class. Those details must be recovered before this working description can become a precise claim about an algorithm or lower bound.

[Read in atlas](index.html#TCS-0055) · [The Open Problems Project](https://topp.openproblem.net/p33)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0010 — Superlinear constant-degree arithmetic circuit lower bounds

This entry concerns lower bounds for arithmetic circuits computing polynomials of constant degree. Keeping degree fixed asks whether difficulty can arise from the interaction among many variables rather than from an enormous degree. The stated target is a superlinear lower bound, which would rule out computation with only a constant amount of arithmetic per input-scale unit. The saved reference points to a numbered problem in Wigderson's book but does not preserve its explicit polynomial family or field conventions. A completed statement must recover those choices, since changing constants, circuit restrictions, or the meaning of explicitness can alter the lower-bound challenge.

[Read in atlas](index.html#TCS-0010) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3959 — Approximate polynomial satisfiability in AM under GRH

Approximate polynomial satisfiability asks whether a rational polynomial system can have all residuals arbitrarily close to zero over the complex numbers. The approximating points may diverge, so an exact common root need not exist. Equivalently, every algebraic relation among the input polynomials must have zero constant term. The question asks whether a polynomial-time public-coin interactive verifier can decide this under GRH; APS is currently known to be NP-hard and in PSPACE. A February 2026 extension treats containment of approximate solution sets in PSPACE and does not supply the requested AM bound.

[Read in atlas](index.html#TCS-3959) · [Algebraic Dependencies and PSPACE Algorithms in Approximative Complexity](https://doi.org/10.4230/LIPIcs.CCC.2018.10) · [Algebraic Dependencies and PSPACE Algorithms in Approximative Complexity over Any Field](https://doi.org/10.4086/toc.2019.v015a016) · [When Hilbert approximates: A Strong Nullstellensatz for Approximate Polynomial Satisfiability](https://eccc.weizmann.ac.il/report/2026/026/)
Existing status: `open` · Summary written: 2026-09-12

### TCS-1103 — Containment of border VP in VNP over arbitrary fields

Border VP allows polynomial families obtained through algebraic limits of small arithmetic circuits. The question asks whether these limiting families always belong to VNP over arbitrary fields. Its computational content is whether an approximation-style representation can be replaced by an exact algebraic witness-sum description of controlled size. The arbitrary-field requirement makes the field assumptions part of the challenge rather than a harmless choice of notation. The saved record points to Question 8 of the factoring survey, whose precise definition of border complexity and parameter bounds must be retained in a full formulation.

[Read in atlas](index.html#TCS-1103) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7372 — Linear-time unit-Monge distance multiplication

The input consists of two permutations encoding structured distance matrices. The output must encode their exact min-plus product. All three representations have only linear size. The question asks whether the computation can match that size in time. The current general unit-Monge bound has a logarithmic overhead.

[Read in atlas](index.html#TCS-7372) · [Fast Distance Multiplication of Unit-Monge Matrices](https://doi.org/10.1007/s00453-013-9830-z) · [Core-Sparse Monge Matrix Multiplication: Improved Algorithm and Applications](https://arxiv.org/abs/2408.04613v2)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4949 — Tensor decomposition at Kruskal’s uniqueness threshold

A third-order tensor decomposition expresses an array as a sum of rank-one outer products of three vector families. Kruskal's theorem guarantees uniqueness when the three families' Kruskal ranks sum to at least twice the number of components plus two. The question asks for an efficient decomposition algorithm throughout this uniqueness regime, including cases beyond linear independence of all components. For a cubic tensor, these conditions can certify substantially more components than the dimension, where the familiar simultaneous-diagonalization approach no longer applies directly. An algorithmic proof, especially a robust one, would connect identifiability of latent-variable models with practical recovery from estimated moments.

[Read in atlas](index.html#TCS-4949) · [Open Problem: Tensor Decompositions: Algorithms up to the Uniqueness Threshold?](https://proceedings.mlr.press/v35/bhaskara14b.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0009 — Explicit univariate arithmetic circuit lower bounds

A polynomial in one variable may have a compact arithmetic description even when its expanded coefficient list is huge. This entry seeks explicit univariate polynomials with provably large arithmetic-circuit complexity. The challenge is to identify concrete algebraic structure that defeats arbitrary sharing of intermediate computations. Such examples would give unusually focused lower-bound targets, removing the many-variable geometry present in other circuit problems. The inherited index supplies neither the required quantitative bound nor the source's explicitness and constant conventions, so those parameters remain essential unfinished parts of the eventual card.

[Read in atlas](index.html#TCS-0009) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0046 — Complexity of solving tropical or min-plus linear systems

A min-plus linear equation equates two minima of affine expressions formed by adding coefficients to individual unknowns. Systems of these equations replace ordinary addition and multiplication with the operations of tropical arithmetic. The source asks for the computational complexity of deciding and solving such systems. Their piecewise-linear form does not immediately put them within ordinary linear programming, because the minimizing terms can change with the solution. A classification would explain which aspects of tropical linear algebra retain efficient linear-system behavior and which introduce a separate combinatorial search problem.

[Read in atlas](index.html#TCS-0046) · [Complexity of Symbolic and Numerical Problems](https://doi.org/10.4230/DagRep.5.6.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1101 — VP factor closure in positive characteristic

VP consists of polynomial-degree polynomial families that have arithmetic circuits of polynomial size. This question asks whether taking polynomial factors preserves that class in positive characteristic. A factor can conceal structure that is inexpensive only after multiplication, so factoring asks whether this apparent compression can be undone without a large circuit blowup. Closure would make efficient algebraic computation more stable under a basic symbolic operation. The saved survey reference specifies a characteristic-sensitive question, and a complete statement must recover its field and degree assumptions rather than importing a characteristic-zero theorem.

[Read in atlas](index.html#TCS-1101) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1102 — VBP factor closure in positive characteristic

Algebraic branching programs compute polynomials as sums of products associated with paths through a directed graph. The question asks whether factors of polynomial-size branching-program families retain polynomial-size representations in positive characteristic. This tests whether a determinant-like computation model survives an elementary algebraic decomposition. A construction that outputs general arithmetic circuits would not by itself preserve the restricted representation being asked about. The saved entry refers to Question 4 of a factoring survey, so the exact field assumptions and quantitative degree dependence still need to be carried into the finished formulation.

[Read in atlas](index.html#TCS-1102) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0047 — Complexity of testing membership to Kronecker polytopes

Kronecker coefficients describe multiplicities in representations associated with tensor spaces. Normalizing the triples of partitions with positive coefficients and taking their closure produces a convex Kronecker polytope. The question asks for the complexity of testing whether a given normalized triple belongs to this polytope, with the number of parts included in the input. The partitions are encoded in binary, making dependence on their numerical size part of the computational issue. An efficient membership method would strengthen the algorithmic tools available for representation-theoretic approaches to tensor complexity and algebraic lower bounds.

[Read in atlas](index.html#TCS-0047) · [Complexity of Symbolic and Numerical Problems](https://doi.org/10.4230/DagRep.5.6.28)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0095 — Efficient LRS evaluation

A rational linear recurrence specifies an infinite sequence using finitely many initial values and recurrence coefficients. Given an index written in binary, this project asks whether testing that indexed term for exact equality to zero takes polynomial time. The requested index can be exponentially larger than its encoding, making step-by-step generation unsuitable. Fast algebraic evaluation also has to account for the bit lengths of intermediate values. The problem isolates the complexity of one succinctly addressed zero test, independently of searching for a zero anywhere in the sequence.

[Read in atlas](index.html#TCS-0095) · [Automata Exchange](https://automata.exchange/25.4-efficient-lrs-evaluation/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1069 — Complexity of testing Zariski-closure membership

A semialgebraic set is described by polynomial equations and inequalities. The question asks for the complexity of deciding whether a designated point belongs to its Zariski closure. This closure is determined by polynomial relations vanishing on the set and differs from ordinary metric closure. The source contrasts the target with the classified Euclidean adherence problem. Understanding the complexity would quantify how difficult it is to infer algebraic consequences of a real feasible region when its limiting behavior is interpreted algebraically rather than by distance.

[Read in atlas](index.html#TCS-1069) · [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1151 — Bounded-interval zero testing for exponential-trigonometric polynomials

Exponential-trigonometric polynomials combine oscillatory and exponential behavior in functions whose zeros need not resemble polynomial roots. The saved question asks whether one can decide the existence of a zero on a bounded interval with rational endpoints. Bounding the interval removes questions about behavior arbitrarily far away but still leaves exact equality difficult to certify. A solution would clarify the effective analysis of this particular function class, rather than merely provide numerical root approximations. The coefficient field denoted K and the precise permitted expressions are absent from the excerpt and remain necessary parts of the full decision problem.

[Read in atlas](index.html#TCS-1151) · [On Positivity of Exponential-Trigonometric Polynomials and Irrationality Exponents](https://doi.org/10.4230/LIPIcs.MFCS.2026.65)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1544 — Complexity classification of finite-semigroup membership

The semigroup membership problem asks whether a target element can be produced by composing a supplied set of generators. This project seeks a classification of finite-semigroup varieties according to the complexity of that problem. Algebraic restrictions on multiplication can drastically change the available algorithms and lower-bound constructions. The source's analysis of inverse semigroups provides a starting point, while arbitrary semigroups introduce substantially more structural possibilities. A complete classification would connect algebraic identities with the computational cost of reasoning about generated transformations.

[Read in atlas](index.html#TCS-1544) · [Membership and Conjugacy in Inverse Semigroups](https://doi.org/10.4230/LIPIcs.ICALP.2025.156)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2039 — Decidability of freeness in automaton groups

An automaton group is generated by transformations described through a finite state machine. The freeness problem asks whether the group has the structure of a free group, without additional relations beyond group identities. This project seeks an algorithm deciding that property from the automaton presentation, or a proof that none exists. The source's neighboring undecidability results concern automaton semigroups and monoids and do not automatically transfer to groups. Resolving the group case would sharpen the boundary between finite descriptions and effective recognition of fundamental algebraic structure.

[Read in atlas](index.html#TCS-2039) · [The Freeness Problem for Automaton Semigroups](https://doi.org/10.4230/LIPIcs.MFCS.2024.44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-2077 — Deterministic divisibility testing by a constant-degree polynomial

The input is a sparse multivariate polynomial f and a proposed low-degree divisor g. The question is whether divisibility can always be decided deterministically in polynomially many rational arithmetic operations. Even quadratic g remains the key case. The time bound may be polynomial in the numerical degree of f, and no sparse quotient is promised. New results for dividends of bounded individual degree do not settle the unrestricted dividend case here.

[Read in atlas](index.html#TCS-2077) · [Derandomizing Multivariate Polynomial Factoring for Low Degree Factors](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2024.75) · [Deterministic Divisibility Testing via Shifted Partial Derivatives](https://www.ias.edu/sites/default/files/math/csdm/14-15/Forbes2015.pdf) · [On Factorization of Sparse Polynomials of Bounded Individual Degree](https://eccc.weizmann.ac.il/report/2026/036/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2506 — Algebraic branching programs versus formulas

Algebraic formulas compute polynomials using arithmetic trees. Algebraic branching programs compute sums of products along paths and can share subcomputations. Every polynomial-size formula can be represented by a polynomial-size branching program. The question asks whether some branching-program family requires superpolynomial formula size over the specified field. Known results for bounded-depth or syntactically multilinear formulas do not settle this unrestricted separation.

[Read in atlas](index.html#TCS-2506) · [Towards Optimal Depth-Reductions for Algebraic Formulas](https://doi.org/10.4230/LIPIcs.CCC.2023.28) · [Multilinear Algebraic Branching Programs and the Min-Partition Rank Method](https://eccc.weizmann.ac.il/report/2026/001/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2718 — A uniform exponent saving for arbitrary generalized convolution

Generalized convolution combines two integer tables using an arbitrary operation on each coordinate. The card asks to compute the entire output table with a fixed saving over the brute-force exponent. The saving must be independent of the size of the coordinate domain. The improved journal algorithm reduces the exponential base by a constant factor, which gives a domain-dependent exponent saving only. A faster algorithm for one output entry does not meet the full-table target.

[Read in atlas](index.html#TCS-2718) · [Computing Generalized Convolutions Faster Than Brute Force](https://doi.org/10.4230/LIPIcs.IPEC.2022.12) · [Computing Generalized Convolutions Faster Than Brute Force — journal version](https://doi.org/10.1007/s00453-023-01176-2)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2958 — Efficient equations for VP with unrestricted complex coefficients

An equation for VP is a nonzero polynomial that eventually vanishes on coefficient vectors of all polynomial-size arithmetic computations. Its own degree and circuit size should be polynomial in the coefficient-vector dimension. The question removes the bounded-integer-coefficient restriction from known positive results. Efficient equations here are nonuniform circuit families, without a separate construction-time requirement. The checked combined revision and new journal publication retain the distinction between this VP question and conditional hardness for VNP.

[Read in atlas](index.html#TCS-2958) · [If VNP Is Hard, Then so Are Equations for It](https://doi.org/10.4230/LIPIcs.STACS.2022.44) · [On the Existence of Algebraic Natural Proofs — combined full version](https://arxiv.org/abs/2004.14147) · [On the Existence of Algebraic Natural Proofs](https://doi.org/10.1007/s00037-026-00289-8)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3318 — Arithmetic circuit closure under pth roots

In positive characteristic p, taking a p-th power interacts strongly with the algebraic structure of a polynomial. The source asks whether a small circuit for \(g(x)^{p}\) implies a small circuit for \(g(x)\) itself. This tests whether taking a root can uncover computational difficulty hidden by the characteristic-p power operation. A positive result would support efforts to relate algebraic hardness and derandomization in low characteristic. The excerpt leaves the quantitative size bound and field assumptions implicit, so a finished version must specify how circuit size, degree, and available constants are controlled.

[Read in atlas](index.html#TCS-3318) · [Algebraic Hardness Versus Randomness in Low Characteristic](https://doi.org/10.4230/LIPIcs.CCC.2020.37)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4350 — Uniform compressed word problem for graph groups

The input gives both a graph group and a compact straight-line program representing a word in its generators. The main question is whether one deterministic algorithm can test identity in polynomial time in the combined input size. Polynomial time for each fixed graph group does not provide that uniform guarantee. Randomized one-sided polynomial-time testing is known, while NP membership is a separate weaker target. A 2024 result handles uniform power words but explicitly leaves arbitrary straight-line programs open.

[Read in atlas](index.html#TCS-4350) · [Knapsack in Graph Groups, HNN-Extensions and Amalgamated Products](https://doi.org/10.4230/LIPIcs.STACS.2016.50) · [Knapsack in Graph Groups](https://doi.org/10.1007/s00224-017-9808-3) · [The Power Word Problem in Graph Products](https://doi.org/10.1007/s00224-024-10173-z)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4490 — Complexity of positive matrix powers

Matrix powering studies properties of repeated products of a fixed matrix, where a concise input describes an infinite sequence. The source asks about the complexity of its positivity problem PosMatPow in higher dimensions. The dimension restriction is central because increasing the number of coordinates can introduce substantially more complicated spectral behavior. Determining the complexity would clarify how far low-dimensional decision methods extend to general matrix dynamics. The saved title and excerpt do not define which positivity condition or power quantifier PosMatPow uses, so those conventions must be recovered before stating the decision task more narrowly.

[Read in atlas](index.html#TCS-4490) · [On Matrix Powering in Low Dimensions](https://doi.org/10.4230/LIPIcs.STACS.2015.329)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4523 — Complexity of dimension expansion

Dimension expansion asks whether applying several linear maps makes every relevant subspace grow in dimension. The source asks for the computational complexity of evaluating this expansion. Unlike ordinary vertex expansion, the objects being expanded form a continuous family of subspaces. An efficient method would help assess algebraic expanders and the rank-condensation constructions that produce them. The saved question does not specify the field, input maps, subspace range, or exact versus approximate output, and each of these choices affects the resulting computational problem.

[Read in atlas](index.html#TCS-4523) · [Dimension Expanders via Rank Condensers](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.800)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5240 — Transferring arithmetic hardness to constantly many variables

Arithmetic circuit lower bounds measure how difficult it is to compute polynomial families. The source asks whether lower bounds for many-variable polynomials imply lower bounds in a constant number of variables. Packing information into fewer variables can increase degrees and alter how efficiently circuits represent the polynomial. A transfer would strengthen hardness-versus-randomness methods that require hard polynomials with restricted variable count. The cited work emphasizes low characteristic, and the saved sentence does not state the degree or size tradeoff, so a formal variable substitution alone does not establish the requested implication.

[Read in atlas](index.html#TCS-5240) · [Algebraic Hardness Versus Randomness in Low Characteristic](https://doi.org/10.4230/LIPIcs.CCC.2020.37)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5260 — Explicit rigid matrices over low-degree number fields

Matrix rigidity measures how many entries must be changed before a matrix's rank falls substantially. Valiant's approach seeks explicit matrices rigid enough to imply lower bounds for small linear circuits. The cited paper shows that prominent structured candidates, including Fourier and circulant matrices in its setting, fail the required rigidity. The selected construction problem remains even when entries may lie in a number field of polynomially bounded dimension. An explicit successful family would supply a central missing ingredient in this lower-bound program and explain what structure avoids the weaknesses of earlier candidates.

[Read in atlas](index.html#TCS-5260) · [Fourier and Circulant Matrices Are Not Rigid](https://doi.org/10.4230/LIPIcs.CCC.2019.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5739 — Collapse of rational recurrence systems to single recurrences

A rationally recursive sequence is one coordinate of a finite system whose next state is a rational function of its current state. The conjecture asks whether finitely many past values of that coordinate always suffice to generate its next value. All coefficients and initial values are rational, and every denominator must remain nonzero along the sequence. A scalar recurrence may depend on the particular initial vector, but must work at every step. The known theorem with symbolic initial values does not settle the numerical case because specialization can make its denominators vanish.

[Read in atlas](index.html#TCS-5739) · [On Rational Recursive Sequences](https://doi.org/10.4230/LIPIcs.STACS.2023.24) · [On Rational Recursive Sequences — full author version](https://arxiv.org/abs/2210.01635)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5921 — Membership in \(2\times 2\) integer matrix semigroups

Given finitely many integer matrices, semigroup membership asks whether a target matrix equals some nonempty product of the generators. This project concerns arbitrary two-by-two integer matrices and asks whether the problem is decidable. Products may use generators repeatedly but cannot freely introduce inverses as a group-membership problem would. The source proves positive results for other structured low-dimensional matrix classes without settling this unrestricted two-dimensional case. A resolution would locate a basic boundary for exact reachability in small-dimensional linear transformation systems.

[Read in atlas](index.html#TCS-5921) · [On Reachability Problems for Low-Dimensional Matrix Semigroups](https://doi.org/10.4230/LIPIcs.ICALP.2019.44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6401 — Finiteness of automaton semigroups

A finite Mealy automaton generates a semigroup by composing its induced transformations of words. The source's general question asks whether finiteness of such generated semigroups can be decided. Its positive theorem treats reversible two-state automata, with additional invertibility yielding effective finiteness and freeness tests. Those restrictions are crucial and do not amount to a procedure for arbitrary automaton semigroups. The project direction is to understand the broader decision boundary beyond cases where a strong finite-versus-free structural dichotomy supplies an answer.

[Read in atlas](index.html#TCS-6401) · [The finiteness of a group generated by a 2-letter invertible-reversible Mealy automaton is decidable](https://doi.org/10.4230/LIPIcs.STACS.2013.502)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6493 — Complexity of tensor orbit-closure intersection

A tensor orbit contains objects related by allowed changes of basis. Orbit-closure intersection also treats objects as equivalent when their limiting orbit behavior overlaps. The source develops reductions and completeness notions for this algebraic decision problem and asks for its exact complexity. It also compares this task with ordinary orbit equality and considers symmetry-restricted tensors. The project seeks to understand whether allowing degenerations simplifies equivalence testing or preserves the central hardness of comparing high-dimensional algebraic objects.

[Read in atlas](index.html#TCS-6493) · [Complexity Theory of Orbit Closure Intersection for Tensors: Reductions, Completeness, and Graph Isomorphism Hardness](https://doi.org/10.1109/FOCS63196.2025.00027)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6882 — Homogeneous versus unrestricted arithmetic formulas

A homogeneous arithmetic formula keeps polynomial degree consistent at every intermediate computation. The source asks for a superpolynomial separation between these formulas and unrestricted formulas. The intended phenomenon is that allowing intermediate mixtures of degrees can make an otherwise costly polynomial substantially easier to compute. This tests whether homogenizing an expression tree can inherently require a large increase in size. The saved 2010 question is a dated research lead, and its polynomial-degree and field conventions must be retained before using it as a precise claim about a currently unresolved separation.

[Read in atlas](index.html#TCS-6882) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6883 — Multilinear versus general arithmetic circuits

Multilinear circuits restrict intermediate polynomials to use each variable with exponent at most one. The question seeks a superpolynomial gap between such circuits and general arithmetic circuits computing the same multilinear outputs. General circuits may introduce higher powers that later cancel, so output multilinearity does not automatically make the restriction harmless. A separation would show a substantial computational benefit from leaving the multilinear world temporarily. The saved survey question does not preserve the candidate family or field assumptions, and it should be interpreted as the source's lower-bound target rather than a fresh status assessment.

[Read in atlas](index.html#TCS-6883) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6884 — Semantic versus syntactic multilinear circuits

Semantic multilinearity requires intermediate polynomials to be multilinear, while syntactic restrictions enforce this through the circuit's variable structure. The source asks whether the two notions can differ by a superpolynomial amount in circuit size. The issue is whether algebraic cancellation can maintain multilinearity more efficiently than a construction that guarantees it structurally. A separation would clarify how accurately syntactic multilinear models capture all computations with multilinear intermediates. The precise gate-level conventions are important and remain in the cited survey, since different definitions of semantic multilinearity could change the compared classes.

[Read in atlas](index.html#TCS-6884) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6885 — Constant-overhead second differentiation of circuits

An arithmetic circuit compactly represents a polynomial, and its second partial derivatives form a collection of related outputs. The question asks whether all of those derivatives can be computed with only constant-factor circuit overhead. It tests how far shared differentiation computations can avoid repeating essentially the same algebra across many output pairs. The result would sharpen the relationship between evaluating a function and obtaining its second-order information. The source's size accounting and output conventions are indispensable here, because the number of derivatives itself grows quadratically with the number of variables.

[Read in atlas](index.html#TCS-6885) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6888 — Superpolynomial arithmetic formula lower bounds

Arithmetic formulas represent polynomial computations by trees, so every intermediate expression used twice must be copied. The source asks for an explicit family requiring superpolynomial formula size. The challenge is to rule out all small expression trees, including those using arbitrary cancellation rather than a visibly natural computation. Such a result would expose a basic limit of algebraic computation before tackling the greater sharing power of circuits. The saved survey lead needs its field and explicitness conventions restored, and restricted formula lower bounds must be distinguished from the unrestricted target being requested.

[Read in atlas](index.html#TCS-6888) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6890 — Superpolynomial noncommutative circuit lower bounds

Noncommutative arithmetic circuits compute polynomials in which products retain the order of their variables. The source asks for superpolynomial circuit lower bounds in this setting. Order supplies additional structure for lower-bound arguments, but circuit reuse can still combine many ordered expressions compactly. A successful construction would identify a concrete polynomial whose difficulty survives that sharing ability. The saved note does not specify the field or target family, and its 2010 provenance means it records a historical question rather than independently establishing the status of every related restricted model today.

[Read in atlas](index.html#TCS-6890) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6893 — Superpolynomial multilinear circuit lower bounds

Multilinear arithmetic circuits keep variable exponents at most one in their intermediate polynomials. The saved question seeks superpolynomial lower bounds against this circuit model. Unlike formulas, these circuits can share partial computations, which creates the central obstacle when transferring tree-based arguments. A lower bound would quantify the power still available under multilinearity and provide a stronger benchmark for algebraic complexity techniques. The short survey note does not select the explicit polynomial family or settle semantic versus syntactic conventions, so those details remain required before the question becomes a complete research card.

[Read in atlas](index.html#TCS-6893) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6895 — Explicit three-dimensional tensors of superlinear rank

A three-dimensional tensor is an array whose rank is the minimum number of rank-one tensors summing to it. The source asks for explicit tensor families with rank growing superlinearly in the relevant dimension. The requirement of explicitness rules out relying only on counting arguments that establish hard tensors exist somewhere. Such constructions would provide concrete obstacles for bilinear computation and sharpen tensor-based lower-bound methods. The saved note leaves the field, dimension format, and exact construction requirement in the survey, so those parameters must be restored before a candidate family can be evaluated against the target.

[Read in atlas](index.html#TCS-6895) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6897 — Permanent lower bounds from identity testing

Polynomial identity testing decides whether an arithmetic representation computes the zero polynomial. The source asks whether an efficient identity test for a circuit class implies that the permanent is hard for that same class. The desired implication would convert an algorithm for recognizing algebraic cancellation into a lower bound for a canonical counting polynomial. This is a focused hardness-versus-randomness question because the conclusion must concern the particular class being tested. The saved formulation leaves efficient testing and closure assumptions unspecified, and those hypotheses are essential before a general implication can be claimed.

[Read in atlas](index.html#TCS-6897) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6903 — Derandomizing noncommutative PIT

Noncommutative polynomial identity testing asks whether every ordered monomial cancels in the output of a circuit. The saved question seeks a deterministic efficient procedure for this task. Ordinary scalar substitutions erase variable order, so the evaluation model must respect noncommutativity to detect the right identities. A solution would clarify how algebraic structure can replace randomness in a computational setting with genuinely ordered products. The source's access model, degree bound, and allowed evaluation domain are absent from the short note, and must be recovered before comparing an algorithm to the intended target.

[Read in atlas](index.html#TCS-6903) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6914 — Multivariate polynomial factorization from PIT derandomization

Multivariate polynomial factorization decomposes a polynomial into simpler multiplicative components. The saved question seeks efficient deterministic factorization and asks whether derandomizing polynomial identity testing is enough to obtain it. This probes whether the randomness used by factoring algorithms can be reduced to testing algebraic equality. A positive reduction would connect two fundamental computer-algebra tasks through a single derandomization breakthrough. The polynomial representation, coefficient field, and treatment of factor output sizes are missing from the short note, so the eventual statement must specify them instead of combining dense and circuit-based models implicitly.

[Read in atlas](index.html#TCS-6914) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

## Lattices and computational number theory (28)

### TCS-6571 — Hilbert’s tenth problem over the rationals

Hilbert’s tenth problem over the rationals asks whether an arbitrary integer-coefficient polynomial has a zero consisting of exact rational numbers. The target requires one deterministic algorithm that always halts and decides this for every number of variables, degree and coefficient size. There is no efficiency requirement, and merely enumerating rational solutions does not decide instances with no solution. Undecidability over integers, universal definitions and results with extra height predicates have different logical or arithmetic scope. Recent advances over rings of integers preserve that distinction, and the checked sources do not settle the rational-solvability question.

[Read in atlas](index.html#TCS-6571) · [Hilbert’s Tenth Problem over Rings of Number-Theoretic Interest](https://math.mit.edu/~poonen/papers/aws2003.pdf) · [Defining \(\mathbb Z\) in \(\mathbb Q\)](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n1-p02-p.pdf) · [A survey of local-global methods for Hilbert’s Tenth Problem](https://arxiv.org/abs/2309.14987v1) · [Effectivity for existence of rational points is undecidable](https://arxiv.org/abs/2311.01958v2) · [Rank stability makes rings of integers diophantine](https://math.mit.edu/~poonen/papers/h10_over_OK.pdf) · [Rank stability in quadratic extensions and Hilbert’s tenth problem for the ring of integers of a number field](https://link.springer.com/article/10.1007/s00222-025-01392-3)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6667 — Polynomial-time, polynomial-factor approximation of Euclidean SVP

The shortest vector problem asks for a nonzero integer combination of a rational lattice basis with minimum Euclidean length. This card asks whether one uniform classical randomized algorithm can approximate that length within some fixed power of the rank on every basis. It must return a nonzero vector on every run, achieve the length bound with probability at least two thirds per input, and count all input, arithmetic and output bits in a polynomial clock. Known general upper guarantees, conditional hardness at smaller factors and basis-dependent approximation expressions do not settle this target. The September 2026 review retains the distinctions between search and decision, classical and quantum computation, and current theorems and withdrawn claims.

[Read in atlas](index.html#TCS-6667) · [Factoring Polynomials with Rational Coefficients](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Lovasz/LovaszLenstraLenstrafactor.pdf) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Tensor-based Hardness of the Shortest Vector Problem to within Almost Polynomial Factors](https://theoryofcomputing.org/articles/v008a023/v008a023.pdf) · [Lattice Problems in \(\mathrm{NP}\cap\mathrm{coNP}\)](https://cims.nyu.edu/~regev/papers/cvpconp.pdf) · [A Novel Approximation Algorithm for the Shortest Vector Problem](https://doi.org/10.1109/ACCESS.2024.3469368) · [A new BKZ-type reduction with provable termination and development of its self-dual variant](https://link.springer.com/article/10.1007/s13160-026-00799-6) · [Deterministic Hardness of Approximation For SVP in all Finite \(\ell_p\) Norms](https://arxiv.org/abs/2604.01451v2) · [One-Sided-Error Parameterized Reductions for the Minimum Distance and Shortest Vector Problems](https://arxiv.org/abs/2608.14305v1) · [Euclidean SVP is deterministically NP-hard to approximate within any constant factor](https://arxiv.org/abs/2608.12664v2) · [Adversary Lower Bounds for Lattice Problems](https://eccc.weizmann.ac.il/report/2026/170/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6617 — Integer factorization in randomized polynomial time

Integer factorization recovers the ordered primes and positive multiplicities whose product is a given positive integer. The question asks for one classical randomized algorithm taking polynomial time in the number of input bits on every random sequence. Its full factor list must be correct with probability at least two thirds separately on every positive input. Efficient primality testing and verification do not resolve the task of finding the factors. Known quantum algorithms, heuristic sieve estimates and improved deterministic subroutines each leave a different gap to this target.

[Read in atlas](index.html#TCS-6617) · [A Survey of Techniques Used in Algebraic and Number Theoretic Algorithms](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf) · [PRIMES is in P](https://annals.math.princeton.edu/2004/160-2/p12) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027) · [A log-log speedup for exponent one-fifth deterministic integer factorisation](https://arxiv.org/abs/2105.11105) · [Deterministic methods for finding elements of large multiplicative order](https://arxiv.org/abs/2601.11131v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6618 — Prime-field discrete logarithms in randomized polynomial time

Given a prime p, a generator g and a nonzero residue h, the task is to recover the unique exponent x between zero and p minus two with g to the x congruent to h modulo p. The question asks whether one classical randomized algorithm can do this in polynomial time in the full binary input length on every promised input. All preprocessing is charged, and the running-time bound must hold for every random sequence while success is at least two thirds separately on each instance. This would invert a basic arithmetic operation used in finite-field cryptography and match a known quantum capability. A complete Lean proof must establish the algorithm or rule out all algorithms in this model; generic lower bounds, quantum algorithms and small-characteristic extension-field results do not suffice.

[Read in atlas](index.html#TCS-6618) · [A Survey of Techniques Used in Algebraic and Number Theoretic Algorithms](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf) · [The impact of the number field sieve on the discrete logarithm problem in finite fields](https://library.slmath.org/books/Book44/files/12oliver.pdf) · [Lower Bounds for Discrete Logarithms and Related Problems](https://www.shoup.net/papers/dlbounds1.pdf) · [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027) · [Discrete logarithms in quasi-polynomial time in finite fields of fixed characteristic](https://arxiv.org/abs/1906.10668v2) · [Discrete Logarithm Factory](https://doi.org/10.62056/ah2ip2fgx) · [A provably quasi-polynomial algorithm for the discrete logarithm problem in finite fields of small characteristic](https://doi.org/10.1016/j.ffa.2025.102753) · [Quantum Advantage with Adaptive Shallow Circuits](https://arxiv.org/abs/2608.15545v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7234 — Quantum polynomial-factor approximation of Euclidean SVP

A lattice consists of all integer combinations of a linearly independent rational basis, and its shortest nonzero vector can be much shorter than every basis column. The question asks whether one uniform quantum algorithm finds a nonzero vector within a fixed power of the rank of that optimum on every explicitly given basis. Its probability of meeting the length bound must be at least two thirds per input, with polynomial total bit cost on every execution and classical vector output. Known reductions for decision or uniqueness-promised lattice problems do not by themselves establish this unrestricted search guarantee. An August 2026 claimed lattice consequence and its September algorithm-specific rebuttal are recorded as disputed evidence with explicit verification limits.

[Read in atlas](index.html#TCS-7234) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://arxiv.org/abs/2401.03703v1) · [Learning With Errors and Extrapolated Dihedral Cosets](https://arxiv.org/abs/1710.08223v2) · [Quantum Algorithms for Lattice Problems](https://eprint.iacr.org/2024/555) · [Exact Coset Sampling for Quantum Lattice Algorithms](https://arxiv.org/abs/2509.12341v8) · [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591) · [The ePrint:2026/1591 Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693) · [Lean formalization accompanying the DCP refutation](https://github.com/sragavan99/lean-ePrint-2026-1591-refutation)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-6619 — Exact Euclidean SVP in single-exponential time and polynomial space

Exact Euclidean SVP asks for a shortest nonzero vector in a lattice given by a rational basis. The question seeks single-exponential time in the rank together with polynomial working space. Known fast approaches retain exponentially much geometric information, while small-memory enumeration has a larger worst-case time scale. Combining both resources would clarify whether memory is essential to the strongest exact lattice algorithms. The saved review requires every stored bit and all recomputation to count, and does not treat heuristic memory reductions or unverified framework proposals as a proof of the universal guarantee.

[Read in atlas](index.html#TCS-6619) · [A Deterministic Single Exponential Time Algorithm for Most Lattice Problems based on Voronoi Cell Computations](https://eccc.weizmann.ac.il/report/2010/014/) · [Shortest Vector Problem (SVP) — Lattice Links](https://cseweb.ucsd.edu/~daniele/LatticeLinks/SVP.html) · [Lattice Enumeration Algorithms](https://cseweb.ucsd.edu/~daniele/LatticeLinks/Enum.html) · [A Sheaf-Theoretic and Etalé Space Approach to the Shortest Vector Problem: Orthogonalization, Coboundary Maps, and Memory-Efficient Sieving](https://pphmjopenaccess.com/jpjgt/article/download/3968/1901/11504) · [Hardness of hinted ISIS from the space-time hardness of lattice problems](https://eprint.iacr.org/2026/187)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6620 — Vinogradov’s least quadratic nonresidue conjecture

A quadratic nonresidue is a nonzero residue that is not a square modulo the prime. Vinogradov’s conjecture says that the least positive one eventually lies below every fixed positive power of the prime. The threshold may depend on the exponent, but the bound must cover every sufficiently large odd prime. Conditional logarithmic-square estimates and almost-all-prime results do not establish this unconditional statement. A refutation would require one fixed positive exponent and arbitrarily large primes violating its bound.

[Read in atlas](index.html#TCS-6620) · [The Elliott–Halberstam conjecture implies the Vinogradov least quadratic nonresidue conjecture](https://arxiv.org/abs/1410.7073) · [Fourier optimization and the least quadratic non-residue](https://www.cirm-math.fr/RepOrga/3213/Slides/Talk-quesada-herrera.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7169 — Exact Euclidean SVP in BQP

Can a quantum computer find an exactly shortest nonzero lattice vector in time polynomial in the encoded basis length? The output must be a classical integer combination of the basis, with success probability at least two thirds on every valid input. Randomized NP-hardness would make such an algorithm a major quantum complexity result, but is not a quantum impossibility proof. August 2026 exact-SVP preprints claim faster exponential algorithms with additional memory details. The disputed dihedral-coset proposal has an approximate-SVP consequence and does not settle this exact target.

[Read in atlas](index.html#TCS-7169) · [The Shortest Vector in a Lattice is Hard to Approximate to within Some Constant](https://doi.org/10.1137/S0097539700373039) · [Improved Classical and Quantum Algorithms for the Shortest Vector Problem via Bounded Distance Decoding](https://ir.cwi.nl/pub/35122/35122.pdf) · [Solving the Shortest Vector Problem in \(2^{0.6039n}\) Time via Mid-point Hessian](https://arxiv.org/abs/2608.02478v2) · [One Discrete Gaussian Sample in \(2^{n/2+o(n)}\) Time](https://arxiv.org/abs/2608.03220v1) · [A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem](https://eprint.iacr.org/2026/1591) · [The ePrint:\(2026/1591\) Quantum Algorithm Does Not Solve DCP](https://eprint.iacr.org/2026/1693)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0658 — Quantum-ETH hardness of cryptographic-factor GapSVP

The target is a conditional quantum lower bound for the Euclidean gap version of the shortest vector problem. The approximation gap grows as dimension to the power three halves plus a fixed positive increment. The card explicitly chooses the quantum exponential-time hypothesis for classical 3-SAT as its starting assumption. It asks to exclude every bounded-error uniform quantum algorithm whose running time is polynomial in the full binary input length. Recent constant-factor or different-norm hardness results do not establish this cryptographically relevant approximation regime.

[Read in atlas](index.html#TCS-0658) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Quantum Meets the Minimum Circuit Size Problem](https://eccc.weizmann.ac.il/report/2021/116/revision/1/) · [Deterministic Hardness of Approximation of Unique-SVP and GapSVP in \(\ell_p\) Norms for \(p>2\)](https://doi.org/10.1145/3798129.3800803) · [NP-hardness of SVP in Euclidean Space](https://arxiv.org/abs/2603.27398)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0659 — Stronger worst-case reductions to SIS and LWE

SIS and LWE are average-case lattice-related problems used as foundations for cryptographic constructions. The source asks for stronger reductions connecting their difficulty to worst-case lattice problems. Such reductions translate a solver on typical generated instances into a solver for every input of a geometric problem. Improved parameters could strengthen security interpretations or broaden the range of useful cryptographic settings. The title does not identify the desired approximation, dimension, modulus, or noise improvement, so a full formulation must specify which loss in the reduction is being reduced.

[Read in atlas](index.html#TCS-0659) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0656 — Reducing factoring or discrete logarithms to approximate SVP

Factoring and discrete logarithms are central number-theoretic search problems with no known classical polynomial-time algorithms in their general regimes. The recorded question asks for reductions from one of these tasks to approximate SVP. A reduction would explain how a sufficiently good short-vector solver could recover factors or logarithms. Such a connection could link lattice hardness to longstanding assumptions outside lattice geometry. The saved title does not specify the approximation factor, dimension growth, or number field, so a lattice encoding alone is insufficient unless solving it preserves the claimed computational consequence.

[Read in atlas](index.html#TCS-0656) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7171 — Baillie–PSW pseudoprimes

The Baillie–PSW combination checks a prime-like modular power pattern and a prime-like Lucas sequence pattern. The question asks whether any composite integer passes both strong tests with the specified Selfridge parameters. All recurrences, congruences and parameter-search rejection rules are fixed in the statement. Exhaustive verification through a large finite range and later experiments have produced no counterexample in the checked sources. A single rigorously verified composite would answer yes, while answering no requires a proof covering integers of every size.

[Read in atlas](index.html#TCS-7171) · [Strengthening the Baillie-PSW Primality Test](https://doi.org/10.1090/mcom/3616) · [U-Bit Collapse in Arnault Composites: Probing the Boundary of Strong Lucas Pseudoprimes](https://arxiv.org/abs/2601.19817v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7170 — Scholz–Brauer conjecture

An addition chain starts at one and builds its target by repeatedly adding two already available values. Its length counts additions and corresponds to the number of multiplications in the associated repeated-power computation. The conjecture asks whether the minimum length for \(2^{n}- 1\) is always at most \(n- 1\) plus the minimum length for n. The analogous theorem for star chains and known infinite families leave the unrestricted universal inequality open in the checked sources. Resolving it would explain how efficiently optimal exponentiation plans can control the cost of all-ones binary exponents.

[Read in atlas](index.html#TCS-7170) · [The Decompressed Tree Size of k-Ary Chains](https://link.springer.com/article/10.1007/s00026-026-00816-y) · [The Scholz Conjecture on Addition Chains Is True for Infinitely Many Integers with \(\ell\)\((2n)=\ell (n)\)](https://math.colgate.edu/~integers/a17Proc23/a17Proc23.pdf) · [The Scholz Conjecture Is True for \(2^{n}- 1\) for Almost All n](https://vixra.org/pdf/2605.0012v1.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0651 — Deterministic NP-hardness reductions for Euclidean SVP

Euclidean SVP asks for the shortest nonzero vector in a lattice under the ordinary Euclidean norm. The source asks for deterministic reductions establishing its NP-hardness in the intended approximation regime. Randomized reductions can construct a useful lattice only with a stated probability, leaving a derandomization gap in the hardness theorem. Removing that randomness would strengthen the connection between lattice difficulty and standard deterministic complexity. The saved historical title does not state the factor or promises, and conditional or restricted later derandomizations must be compared with those exact requirements before declaring this target resolved.

[Read in atlas](index.html#TCS-0651) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0655 — Polynomial-factor SVP hardness from standard assumptions

The source asks whether approximating SVP within a polynomial in the dimension can be proved hard under standard assumptions. This is a looser task than exact SVP because the returned vector may be substantially longer than optimum. Hardness reductions must preserve a correspondingly large geometric gap between their two cases. A theorem would address the approximation range central to many lattice-complexity questions. The saved title does not choose the polynomial exponent or hypothesis, so hardness for a smaller factor cannot automatically be promoted to the full polynomial-factor regime.

[Read in atlas](index.html#TCS-0655) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5395 — Downward self-reducibility of integer factoring

Factoring is a central arithmetic search problem whose complete output is a unique prime-power decomposition. The question asks whether one can factor an n-bit number in polynomial time given oracle answers only on shorter numbers. All queries must have fewer than n bits, not merely a smaller numerical value. The reducer is deterministic and uniform, with polynomially many ordinary computation steps. A positive answer would place factoring in a more structured total-search class and reveal a basic recursive property of the problem.

[Read in atlas](index.html#TCS-5395) · [Downward Self-Reducibility in TFNP](https://doi.org/10.4230/LIPIcs.ITCS.2023.67)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0652 — Dimension-preserving search-to-decision reductions for SVP

The input is a rational lattice basis, and the search task is to produce a nonzero vector whose length approximates the shortest possible length. The available oracle only distinguishes short-vector lengths across a multiplicative gap. The question asks for a classical polynomial-time reduction that keeps every query in the original dimension and loses only a polynomial in dimension and approximation factor. Known exact and near-exact reductions do not supply this guarantee across the full approximation range. A resolution would clarify whether approximate lattice decision algorithms can be converted efficiently into search algorithms without an exponential dimensional penalty.

[Read in atlas](index.html#TCS-0652) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Search-to-Decision Reductions for Lattice Problems with Approximation Factors (Slightly) Greater Than One](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.19) · [Dimension-Preserving Reductions Between Lattice Problems](https://www.noahsd.com/latticeproblems.pdf) · [Open problems from the Summer 2022 Lattices Program](https://wiki.simons.berkeley.edu/doku.php?id=lat22:start)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0648 — Constant-gap hardness of unique SVP

Unique SVP assumes that one shortest lattice direction is separated from other independent short vectors by a gap. The saved question seeks hardness with a constant gap. Uniqueness can simplify recovery because near-optimal vectors may be forced to point in essentially the same direction. A hardness theorem would show how much of general lattice difficulty survives this isolation promise. The source title does not state the precise successive-minima condition, approximation goal, or hardness assumption, so ordinary exact-SVP hardness cannot be applied without preserving the unique-vector gap.

[Read in atlas](index.html#TCS-0648) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0661 — SVP hardness for fixed-rank module lattices

Module lattices carry additional algebraic structure beyond an arbitrary integer lattice. The recorded question asks about SVP hardness when the module rank is fixed. A small module rank can coexist with a large underlying integer dimension as the base algebraic field grows. Understanding hardness here would clarify whether the structure used for compact lattice constructions also changes their worst-case geometric difficulty. The saved title does not define the ring, embedding, or approximation factor, so fixed module rank must not be confused with fixed-dimensional Euclidean SVP.

[Read in atlas](index.html#TCS-0661) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0662 — Unconditional exponential hardness of \(n^{1+\varepsilon}\)-GapSVP

The input is a rational basis for an n-dimensional lattice and a positive radius. The task distinguishes a nonzero vector within that radius from the promise that every nonzero vector is farther away by a factor \(n^{1+\varepsilon}\). The source asks for explicit \(c,\varepsilon >0\) and an unconditional lower bound excluding \(2^{cn}\)-time algorithms, up to polynomial input-processing factors. The bound must also exclude randomized and quantum computation with bounded error. Such a theorem would establish a powerful worst-case hardness foundation for lattice-based cryptography.

[Read in atlas](index.html#TCS-0662) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Lattice Problems Beyond Polynomial Time](https://arxiv.org/abs/2211.11693)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0657 — Smaller-factor coNP or coAM certificates for SVP

Gap versions of SVP distinguish lattices with a very short vector from those whose nonzero vectors are all much longer. The source asks for coNP or coAM certificates at smaller approximation factors. Certifying the absence of short vectors is different from exhibiting one, so alternate proof systems can provide useful upper bounds. Sharper certificates would clarify the structural complexity of accurate lattice approximation and constrain some routes to NP-hardness. The saved title does not provide the baseline factor or interactive-proof convention, and such certificates would not by themselves yield a polynomial-time search algorithm.

[Read in atlas](index.html#TCS-0657) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0653 — Explicit quantum exponential-time lower bounds for Euclidean SVP

Quantum algorithms may exploit operations unavailable to classical lattice solvers. The source asks for explicit exponential-time lower bounds for Euclidean SVP in the quantum setting. Classical fine-grained assumptions cannot automatically exclude speedups using quantum search or other quantum primitives. A precise bound would clarify the strength of lattice hardness claims relevant when adversaries have quantum computation. The saved title does not name the starting hypothesis or approximation regime, so the requested result is not an existing unconditional quantum lower bound and must preserve the reduction's quantitative dimension dependence.

[Read in atlas](index.html#TCS-0653) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1170 — ETH hardness of constant-factor shortest-vector approximation for \(1\le p\le 2\)

The shortest-vector problem asks how short a nonzero lattice vector can be. This card asks for constant-factor gap hardness in every norm \(\ell p\) with \(1\le p\le 2\). The proposed lower bound excludes subexponential dependence on ambient dimension, with polynomial dependence on input encoding length. Its premise is ordinary deterministic ETH, and the approximation factor must stay bounded away from one as dimension grows. The source’s shortest-vector hardness theorem for \(p>2\) uses randomized ETH and does not settle this stated interval or premise.

[Read in atlas](index.html#TCS-1170) · [Mind the Gap? Not for SVP Hardness Under ETH!](https://doi.org/10.4230/LIPIcs.ICALP.2026.8)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5317 — NP-hardness of Euclidean covering radius

A lattice's covering radius is the farthest distance of any point from its nearest lattice point. The source studies the hardness of deciding and approximating this radius in different lp norms. The selected question emphasizes proving NP-hardness for the exact Euclidean case, where p equals two. The paper establishes approximation hardness for sufficiently large finite p, but those geometric constructions do not resolve the Euclidean target. A hardness proof would settle a basic classification question for one of the most natural lattice covering problems.

[Read in atlas](index.html#TCS-5317) · [Hardness of the Binary Covering Radius Problem in Large \(l_{p}\) Norms](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.10)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6861 — Classical reductions matching quantum LWE hardness

Learning With Errors asks for hidden linear information obscured by small random noise. The saved survey question seeks classical reductions matching the full worst-case hardness guarantees of a quantum reduction. A reduction may invoke quantum computation even when the resulting average-case problem is presented to classical algorithms. Matching it classically would clarify which security connections require quantum machinery rather than only lattice geometry. The historical note does not reproduce the approximation, modulus, or noise parameters, so a weaker classical reduction or a restricted regime does not automatically meet the full target.

[Read in atlas](index.html#TCS-6861) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6863 — Algorithmic advantages of ideal-lattice structure

Ideal lattices have algebraic symmetries that support compact representations and fast operations. The survey asks whether those structures permit faster algorithms than general lattices, including attacks on ring-SIS and ring-LWE. The same regularity that improves implementation might also expose relationships a solver can exploit. Understanding the comparison would clarify the computational price of choosing structured lattice assumptions. The saved historical question does not fix field families or parameters, so isolated speedups or practical attacks must be distinguished from a universal asymptotic advantage for all ideal-lattice problems.

[Read in atlas](index.html#TCS-6863) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6864 — Classical worst-case reductions for ring-LWE

Ring-LWE places noisy linear equations in an algebraic ring rather than an unstructured vector space. The survey asks for a meaningful classical reduction from worst-case problems to this average-case task. Such a reduction would explain how solving generated ring-LWE instances could solve every instance of an associated structured lattice problem. A classical connection could strengthen the interpretation of the hardness assumption without invoking quantum computation. The saved note does not define the intended quantitative strength or ring family, so “meaningful” still needs explicit approximation, dimension, and noise parameters.

[Read in atlas](index.html#TCS-6864) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6868 — Worst-case and search-to-decision reductions for NTRU

NTRU-like problems use structured algebraic relations involving short secret elements. The survey asks for worst-case reductions or reductions connecting search with decision versions. Recovering a hidden object can differ substantially from merely distinguishing its induced distribution from a comparison distribution. A strong connection would place these assumptions within a more systematic complexity framework. The saved historical note does not identify one NTRU variant or its distributions, so reductions for a neighboring ring problem cannot automatically supply the requested guarantees.

[Read in atlas](index.html#TCS-6868) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-11

## Coding and information theory (27)

### TCS-6606 — Capacity of the two-user Gaussian interference channel

Two separately informed transmitters communicate through real Gaussian noise while interfering with each other’s receivers. The target is the weighted support function of the capacity region for every real gain, nonnegative power budget and weight between zero and one. The model permits deterministic time sharing and averages each transmitter’s power over messages and time, with vanishing joint average decoding error. Known special cases and approximation results leave the general tradeoff unresolved in the checked sources, while a September 2026 weak-interference capacity claim remains unverified here. A complete Lean proof must certify one function within absolute error 1/100 bit per real channel use throughout the entire domain.

[Read in atlas](index.html#TCS-6606) · [Two-User Gaussian Interference Channels: An Information Theoretic Point of View](https://doi.org/10.1561/0100000071) · [Gaussian Interference Channel Capacity to Within One Bit](https://arxiv.org/abs/cs/0702045v2) · [Invariance of the Han–Kobayashi Region With Respect to Temporally-Correlated Gaussian Inputs](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/temp-corr.pdf) · [Proof of a conjecture on the Gaussian signaling region for the Gaussian Z-interference channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/GZ-Noi-con.pdf) · [On the Local Optimality of Gaussian distributions for the Han-Kobayashi Inner Bound for the Gaussian Z-interference channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/Gau-Her.pdf) · [A New Outer Bound for the Discrete Memoryless Two-User Interference Channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/INT-OB-ITA-26.pdf) · [On the Optimality of Gaussian Code-books for Signaling over a Two-Users Weak Gaussian Interference Channel](https://arxiv.org/abs/2501.14941v12) · [Codewords With Memory Improve Achievable Rate Regions of the Memoryless Gaussian Interference Channel](https://arxiv.org/abs/1508.05726v2)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-1010 — Optimal asymptotic binary rate–distance tradeoff

A binary code is any subset of binary strings of one length with a prescribed minimum pairwise Hamming distance. The function \(R_{2}(\delta )\) is the limsup of the best achievable rate at relative distance \(\delta\). Determine this tradeoff for every real \(\delta\) between zero and one half, allowing nonlinear codes and arbitrary block lengths. The benchmark accepts a Lean-certified curve with absolute rate error at most 0.01 bits per transmitted bit. The original limsup convention and the distinction between existence and efficient coding are retained.

[Read in atlas](index.html#TCS-1010) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [New upper bounds on the rate of a code via the Delsarte–MacWilliams inequalities](https://doi.org/10.1109/TIT.1977.1055688) · [Asymptotic Improvement of the Gilbert–Varshamov Bound on the Size of Binary Codes](https://arxiv.org/abs/math/0404325) · [Improvement of the Gilbert-Varshamov Bound for Linear Codes and Quantum Codes](https://arxiv.org/abs/2601.18590) · [Binary code rate bounds via classical–quantum channels](https://arxiv.org/abs/2608.09347) · [Comments on the recent improvements of the MRRW bounds](https://arxiv.org/abs/2609.01860)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6665 — Capacity of the general broadcast channel

One transmitter sends two independent private messages through a memoryless channel to receivers with different noisy observations. The target is the weighted support function of the average-error capacity region for every finite rational channel table and rational weight between zero and one. All rates are measured in bits per channel use, and the two individual capacities do not determine the joint tradeoff. Classical and recent work provides achievable regions, converse bounds and special cases, while the August 2026 Marton-suboptimality preprint is a narrower unverified claim. A complete Lean proof must certify a supplied function within absolute error 1/100 over the entire stated domain.

[Read in atlas](index.html#TCS-6665) · [A Coding Theorem for the Discrete Memoryless Broadcast Channel](https://www.seas.ucla.edu/csl/files/temp/DBCAchievability.pdf) · [Evaluation of Marton’s Inner Bound for the General Broadcast Channel](https://arxiv.org/abs/0904.4541v3) · [On Marton’s Inner Bound and Its Optimality for Classes of Product Broadcast Channels](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/proBC.pdf) · [Blahut–Arimoto Algorithms for Inner and Outer Bounds on Capacity Regions of Broadcast Channels](https://pmc.ncbi.nlm.nih.gov/articles/PMC10969477/) · [A Two Auxiliary Receiver Outer Bound to the Capacity Region of a Two-Receiver Discrete Memoryless Broadcast Channel](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/GK-outer.pdf) · [Sub-optimality of Marton’s Inner Bound for the Two-Receiver Broadcast Channel](https://arxiv.org/abs/2608.19869v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6584 — Li–Li conjecture

In an undirected communication network, routing sends independent messages along paths and may split each message among several routes. Network coding additionally allows intermediate nodes to combine information from different messages. The Li-Li conjecture says that coding does not enlarge the achievable rate region for independent unicast sessions beyond fractional multicommodity routing. The saved formulation uses zero-error causal coding and one shared capacity budget for both directions of each edge. A proof or counterexample would determine whether coding provides a fundamental throughput advantage in undirected networks after routing has already been optimized globally.

[Read in atlas](index.html#TCS-6584) · [On the Capacity of Multiple Unicast Sessions in Undirected Graphs](https://ics.uci.edu/~vazirani/isit.pdf) · [Coding in Undirected Graphs Is Either Very Helpful or Not Helpful at All](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.18) · [Lower Bounds for Multiplication via Network Coding](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.10) · [On the Capacity of Undirected Multiple Unicast Layered Networks with Asymmetric Demands](https://ieeexplore.ieee.org/document/11195643/) · [Undirected Multicast Network Coding Gaps via Locally Decodable Codes](https://arxiv.org/abs/2510.18737) · [On the Multiple-Unicast Conjecture: Beyond Cut Metrics](https://arxiv.org/abs/2608.06070) · [A Session Interaction Framework for The Multiple-Unicast Conjecture](https://arxiv.org/abs/2608.06042)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6607 — Capacity of the binary deletion channel

The binary deletion channel independently removes transmitted bits and hides their original positions. The question asks for capacity as a function of deletion probability, measured per input bit. Missing alignment makes this harder than an erasure channel that marks where losses occurred. Matching achievable rates and converse bounds would quantify the fundamental cost of synchronization uncertainty. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-6607) · [An Overview of Capacity Results for Synchronization Channels](https://arxiv.org/abs/1910.07199) · [Optimal Coding for the Binary Deletion Channel With Small Deletion Probability](https://ykanoria.github.io/Deletion_paper.pdf) · [Improved Upper and Lower Bounds on the Capacity of the Binary Deletion Channel](https://arxiv.org/abs/2305.07156) · [Improved Capacity Upper Bounds for the Deletion Channel using a Parallelized Blahut-Arimoto Algorithm](https://arxiv.org/abs/2604.05867) · [A Certified Multi-Run Capacity Lower Bound for the Binary Deletion Channel at \(d = 1/2\)](https://zenodo.org/records/21780666)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6608 — Decidability of unconditional Shannon information inequalities

An information inequality is a linear combination of joint entropies asserted to be nonnegative for all distributions. The question asks whether an algorithm can always decide validity when the coefficients are rational and finite alphabet sizes are unrestricted. Standard Shannon inequalities certify many cases but do not describe every valid entropy inequality. A decision procedure would clarify the limits of automated reasoning about information, with implications for coding and database bounds. The saved review notes that invalidity can be semidecided and that undecidability results with conditional premises do not automatically settle this unconditional problem.

[Read in atlas](index.html#TCS-6608) · [Information Inequality Problem over Set Functions](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2024.19) · [Decision Problems in Information Theory](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.106) · [Conditional Information Inequalities for Entropic and Almost Entropic Points](https://arxiv.org/abs/1207.5742v4) · [Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication](https://arxiv.org/abs/2205.11461v3) · [Exploring the entropic region](https://arxiv.org/abs/2509.12439v2) · [Information Inequalities for Five Random Variables](https://arxiv.org/abs/2512.23316v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7210 — Capacity of the general two-user interference channel

Two independent senders communicate with their own receivers through one interfering channel. Each sender knows only its own message and receives no feedback. The capacity region contains the asymptotically reliable pairs of rates under average block error. Its weighted upper support values describe the entire tradeoff in bits per joint channel use. The benchmark asks for these values on every finite channel with a Lean-certified absolute error at most 0.01.

[Read in atlas](index.html#TCS-7210) · [A New Achievable Rate Region for the Interference Channel](https://doi.org/10.1109/TIT.1981.1056307) · [Wikipedia: List of unsolved problems in information theory](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory) · [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1351195847) · [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404v4)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6609 — Constant-rate binary locally decodable codes with logarithmic query complexity

Can a binary code protect arbitrarily long messages at constant rate while recovering any requested bit with only logarithmically many bit queries? A fixed positive fraction of the stored bits may be corrupted adversarially. The local decoder must return the requested bit with probability at least two thirds for every admissible received word and index. Large-alphabet and list-decoding results satisfy different guarantees. The target asks for existence, without an extra requirement that the code be efficiently constructed.

[Read in atlas](index.html#TCS-6609) · [Asymptotically good large-alphabet LDCs with polylogarithmic query complexity](https://eccc.weizmann.ac.il/report/2025/168/revision/1/download/) · [High Rate Efficient Local List Decoding from HDX](https://arxiv.org/abs/2601.22535v1)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7214 — Rate–distortion tradeoff for distributed lossy source coding

Two encoders separately compress correlated source blocks for one joint decoder. Each reconstructed source must satisfy its own expected per-symbol distortion limit. The function records the smallest weighted sum of the two description rates. Only feasible distortion targets are included, so every requested value is finite. The benchmark keeps the distortion constraints exact and requires a Lean-certified rate error of at most 0.01 on the whole domain.

[Read in atlas](index.html#TCS-7214) · [Network Information Theory](https://www.cambridge.org/core/books/network-information-theory/3ABE1D86EB0F0DF6A8764E415C2CA94A) · [Wikipedia: List of unsolved problems in information theory](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory) · [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1351195847) · [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404v4)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6610 — Shannon capacity of \(C_{7}\)

The seven-cycle describes which pairs of seven channel symbols can be confused. Its Shannon capacity is the supremum of independence numbers of strong graph powers raised to the reciprocal power. The card asks for this real number in distinguishable symbols per use, rather than bits per use. No finite graph power is assumed to attain the supremum. The Lean benchmark accepts an explicit value with certified absolute error at most 0.01.

[Read in atlas](index.html#TCS-6610) · [Strengthening Recursive Constructions for Zero-Error Shannon Capacity](https://arxiv.org/abs/2608.30273)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7211 — Capacity of the general two-way channel

Two terminals simultaneously communicate independent messages over one memoryless channel. Each transmission may depend on the terminal’s own message and previously received outputs. Reliable rates therefore include the possible benefit of adaptation and interaction. The target gives the weighted upper support values of the complete two-direction capacity region. The benchmark requires a Lean-certified absolute error of at most 0.01 bits per joint channel use for every finite channel and weight.

[Read in atlas](index.html#TCS-7211) · [Two-way communication channels](https://projecteuclid.org/euclid.bsmsp/1200512185) · [Wikipedia: List of unsolved problems in information theory](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory) · [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1351195847) · [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404v4)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7215 — Computability of graph Shannon capacity

A graph records which transmitted symbols can be confused. Its Shannon capacity is the limiting number of distinguishable messages per use when arbitrarily long blocks are allowed. The question asks for one terminating algorithm that approximates this quantity to any requested absolute accuracy on every finite graph. Known examples show that fixed finite prefixes and finite-power attainment do not supply a general stopping guarantee. The target concerns computability itself, with no required running-time bound.

[Read in atlas](index.html#TCS-7215) · [The Shannon capacity of a graph and the independence numbers of its powers](https://doi.org/10.1109/tit.2006.872856) · [The Shannon capacity of graph powers](https://arxiv.org/abs/2510.16151v1) · [Advances in the Shannon capacity of graphs](https://doi.org/10.3934/math.2026111)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1020 — Polynomial-length constant-query locally decodable codes

A locally decodable binary code allows recovery of any message bit from only a constant number of codeword queries. The textbook asks whether such codes can have blocklength polynomial in the message length. The decoder must tolerate corruption without scanning the entire stored representation. Polynomial length would make strong locality compatible with a much more economical redundancy cost. The saved note does not state the corruption fraction, success probability, or fixed query count, so these constants must be chosen explicitly before comparing construction and lower-bound regimes.

[Read in atlas](index.html#TCS-1020) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0013 — Efficient explicit constant-rate tree codes

A tree code labels paths in a rooted tree so that diverging histories remain distinguishable along their future labels. The saved question asks for efficient explicit constructions with constant rate. Unlike an ordinary block code, the encoding must work as communication unfolds rather than after the entire message is known. Such objects support reliable interactive communication where later messages depend on earlier received information. The title-level record does not specify the alphabet, distance condition, or encoding and decoding efficiency, so those choices must be recovered before the desired tree-code construction is fully defined.

[Read in atlas](index.html#TCS-0013) · [Mathematics and Computation (2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1012 — Explicit efficiently decoded binary codes beyond Gilbert–Varshamov

This record concerns explicit binary codes that can be decoded efficiently at strong rate–error parameters. The saved textbook note specifically points to list decoding approaching capacity and flags a formulation caveat. List decoding permits several candidate messages, allowing recovery beyond the range guaranteed by unique decoding alone. A construction with optimal rate and efficient decoding would connect information-theoretic possibility to usable error correction. Because the inherited title invokes going beyond Gilbert–Varshamov while the note warns about the printed inequality, no inconsistent rate bound or minimum-distance breakthrough is asserted here.

[Read in atlas](index.html#TCS-1012) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1011 — Full-length Reed–Solomon list decoding beyond Johnson

The question asks whether some infinite family of full-length Reed–Solomon codes has polynomially bounded lists beyond the Johnson threshold. The code evaluates every polynomial of degree at most a fixed fraction of the field size at every field element. One fixed pair of rate and agreement constants and one polynomial list bound must work for every received word along infinitely many field sizes. This is an information-theoretic existence question and does not demand an efficient decoding algorithm. Recent capacity theorems for randomly punctured codes and lower bounds for list recovery have different quantifiers or models and do not settle this target.

[Read in atlas](index.html#TCS-1011) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Random Reed–Solomon Codes Achieve List-Decoding Capacity With Linear-Sized Alphabets](https://arxiv.org/abs/2304.09445) · [Near-Optimal List-Recovery of Linear Code Families](https://drops.dagstuhl.de/storage/00lipics/lipics-vol353-approx-random2025/LIPIcs.APPROX-RANDOM.2025.53/LIPIcs.APPROX-RANDOM.2025.53.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0196 — Polyhedrality of linear-rank inequality cones

Linear-rank inequalities constrain dimensions of collections of subspaces and their sums. The recorded question asks whether the associated cones are polyhedral. Polyhedrality would mean that finitely many linear inequalities suffice to describe the relevant geometric region. Such a description could turn a broad family of linear-information constraints into a finite system amenable to computation. The saved title does not specify the number of variables, field choices, or closure convention, so it cannot yet identify exactly which cone is conjectured to have a finite description.

[Read in atlas](index.html#TCS-0196) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0178 — Bounded-alphabet approximation of entropy-region faces

An entropy region collects all joint-entropy vectors realizable by random variables. The recorded question concerns approximating its faces using variables with bounded alphabets. A face can encode equalities or limiting relationships that finite-support approximations may struggle to preserve exactly. A suitable alphabet bound could make otherwise unbounded information-theoretic optimization more accessible to certified computation. The saved title does not state which faces, approximation metric, or alphabet dependence are intended, so it remains essential to distinguish approximating a nearby entropy vector from staying on the prescribed face.

[Read in atlas](index.html#TCS-0178) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0184 — Entropic matroid approximations approaching unit ratio

Matroid rank functions describe an abstract notion of independence among a finite set of elements. The recorded question concerns approximating these ranks by entropic constructions with a ratio approaching one. An entropic representation would realize the abstract dependence pattern through actual random variables. Near-exact approximation could connect combinatorial independence with information-theoretic feasibility and its applications. The saved title does not specify the class of matroids, normalization, or which direction the ratio measures, so it does not justify assuming that every matroid admits an exact entropy representation.

[Read in atlas](index.html#TCS-0184) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0187 — Field dependence of linear-rank inequalities

Linear-rank inequalities describe constraints satisfied by dimensions of subspaces over a field. The source question asks how these inequalities depend on the chosen field. Characteristic can change which linear dependencies are possible even when the abstract pattern of subspaces looks similar. Clarifying that dependence would identify which information constraints are universal and which reflect algebraic restrictions of a code's alphabet. The saved entry does not provide the proposed field comparison or number of variables, so a complete problem must specify whether it concerns characteristic, field size, or an exact equality of cones.

[Read in atlas](index.html#TCS-0187) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0205 — Infimum of the Ingleton score

The Ingleton expression is a linear combination of entropies associated with a constraint familiar from linear representations. The recorded question asks for the infimum of its normalized score over the intended distributions. Negative scores quantify how far general information structures can deviate from linear-rank behavior. Determining the extremal value would sharpen a concrete measure of that separation. The saved title does not supply the normalization or admissible alphabet conventions, and an infimum need not be attained by a finite distribution, so those details are essential to an exact-value statement.

[Read in atlas](index.html#TCS-0205) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3513 — Explicit positive-rate codes below the Plotkin point

The cited generalized list-decoding framework considers arbitrary adversarial channels rather than one fixed error type. It asks for explicit positive-rate codes whenever the channel lies below its Plotkin threshold. The source describes this condition through the existence of non-confusable CP distributions. An explicit construction would convert the framework's information-theoretic feasibility criterion into concrete families carrying a linear amount of information. The saved passage does not define CP distributions or the channel representation, so these technical conditions cannot be replaced by the usual Hamming-channel error threshold.

[Read in atlas](index.html#TCS-3513) · [Generalized List Decoding](https://doi.org/10.4230/LIPIcs.ITCS.2020.51)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4524 — Positive-rate binary codes against adversarial deletions

Adversarial deletion codes must distinguish messages after an adversary removes a prescribed fraction of their bits. The source asks for the largest deletion fraction below which binary codes of positive rate can exist. Deleted positions are hidden, allowing different codewords to collapse to the same surviving subsequence. Determining this threshold would identify the ultimate worst-case synchronization tolerance of binary communication. This is an information-theoretic supremum question from the saved 2015 source, distinct from independent random deletions and from the separate requirement of efficient encoding or decoding.

[Read in atlas](index.html#TCS-4524) · [Deletion Codes in the High-noise and High-rate Regimes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.867)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4802 — Noise tolerance of binary interactive codes

Binary two-way codes use interaction between communicating parties to tolerate corrupted transmissions. The source asks for the maximal noise tolerance, considering constant-rate and even zero-rate communication. Interaction can exploit feedback-like information that is unavailable to a sender using a fixed one-way block code. Determining the threshold would isolate the fundamental benefit of dialogue against noise. The saved question does not reproduce the adversary or turn-taking conventions, and positive constant rate is a stronger requirement than merely allowing communication whose rate tends to zero.

[Read in atlas](index.html#TCS-4802) · [Binary Codes with Resilience Beyond \(1/4\) via Interaction](https://doi.org/10.1109/FOCS54457.2022.00008)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4968 — Linear versus nonlinear code parameters

Linear codes form subspaces, whereas general codes may use arbitrary collections of words. The cited source asks whether optimum codes can be very far from linear codes in their achievable parameters. It motivates the question by contrasting a complete linear-code programming hierarchy with a hierarchy that collapses in a broader setting. A substantial separation would show that linearity sacrifices inherent coding performance rather than only simplifying construction. The saved question does not quantify “very far” or specify the asymptotic regime, so it still needs a concrete rate, distance, or size comparison.

[Read in atlas](index.html#TCS-4968) · [A Complete Linear Programming Hierarchy for Linear Codes](https://doi.org/10.4230/LIPIcs.ITCS.2022.51)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6738 — Linear-length locally testable codes and proofs

Locally testable codes and proofs allow a verifier to inspect a few positions instead of reading the entire representation. The saved 2017 textbook question asks whether they can have length linear in the underlying information size. Linear length would keep redundancy small while retaining the ability to detect a globally incorrect object locally. The question connects economical encoding with the power of sparse verification. The historical note does not reproduce the query and soundness regime, and this drafting pass does not promote its old existence question to a verified claim of present openness.

[Read in atlas](index.html#TCS-6738) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6739 — Locally decodable versus relaxed locally decodable code length

A locally decodable code recovers a requested bit reliably from a corrupted codeword using few queries. A relaxed locally decodable code may sometimes signal failure instead of returning an incorrect bit under its prescribed rules. The textbook asks for a separation in the lengths achievable by these two models. Such a separation would quantify how much redundancy can be saved by allowing carefully controlled abstention. The saved note does not specify the locality and rejection guarantees, so those conditions must match before two constructions can establish the intended asymptotic difference.

[Read in atlas](index.html#TCS-6739) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `source_open` · Summary written: 2026-09-11

## Property testing and distribution learning (16)

### TCS-6630 — Effective classification of polynomially testable hereditary graph properties

Induced-F-freeness excludes every graph in a finite family as an induced subgraph. The reviewed question asks for an algorithm deciding whether the property has a one-sided dense-graph tester using polynomially many sampled vertices in inverse accuracy. Rejection must expose an actual forbidden induced pattern, matching both edges and nonedges. An effective classification would distinguish families with efficient proximity testing across all graph sizes. The saved review explicitly marks algorithmic decidability of the classification as an editorial specialization and distinguishes dense edit distance from sparse or bounded-degree models.

[Read in atlas](index.html#TCS-6630) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1) · [A Characterization of the (Natural) Graph Properties Testable with One-Sided Error](https://epubs.siam.org/doi/10.1137/06064888X) · [Removal Lemmas with Polynomial Bounds](https://arxiv.org/abs/1611.10315) · [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article) · [Efficient Removal without Efficient Regularity](https://arxiv.org/abs/1709.08159) · [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1033 — Polynomial testability versus distance estimation

A dense-graph tester queries adjacencies to distinguish membership in a property from graphs far from it. A distance estimator instead approximates the minimum fraction of edge changes needed to reach that property. The question asks whether a query bound polynomial in inverse accuracy for testing always entails such a polynomial bound for estimation. Each algorithm is uniform and the query bound is independent of graph size, while local computation is unrestricted. This card isolates the polynomial implication in its title from the stronger quantitative conversion posed in the cited survey.

[Read in atlas](index.html#TCS-1033) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6672 — Sublinear testing of bounded-degree graph isomorphism

The tester sees two sparse graphs only by asking for individual neighbors. It must accept isomorphic graphs and reject pairs that require many edge edits after every possible relabelling. The question asks for fewer than a linear number of queries at every fixed degree bound and proximity. Both graphs are unknown, and arbitrary disconnected or highly connected inputs must be covered. Known small-component testers and recent results for typical known targets do not establish this general two-input guarantee.

[Read in atlas](index.html#TCS-6672) · [Open Problems in Property Testing of Graphs](https://eccc.weizmann.ac.il/report/2021/088/) · [Testing Isomorphism in the Bounded-Degree Graph Model](https://www.wisdom.weizmann.ac.il/~/oded/VO/iso.pdf) · [On Testing Isomorphism to a Fixed Graph in the Bounded-Degree Graph Model](https://www.wisdom.weizmann.ac.il/~/oded/COL3/bdg-iso-fixed.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1030 — Characterizing polynomial-query dense graph properties

Dense graph property testing samples a small portion of a graph to distinguish membership from substantial edit distance. The saved question asks which properties admit query complexity polynomial in inverse proximity. This quantitative distinction separates merely size-independent testers from testers whose accuracy cost remains moderate. A characterization would explain why some graph properties are efficiently observable from samples while others demand much larger samples. The inherited label does not state the permitted property family or error convention, so the draft does not assume that every hereditary property falls under one particular classification theorem.

[Read in atlas](index.html#TCS-1030) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1029 — Sharp graph-removal bounds for fixed patterns

A graph-removal statement links distance from excluding a fixed pattern to the number of copies of that pattern. The saved question asks for sharp quantitative bounds in this relationship. Such bounds control how likely random sampling is to discover a witness that a graph violates the property. Improving them would directly sharpen the accuracy dependence of associated testing algorithms. The title does not identify the pattern, induced versus ordinary copies, or the desired asymptotic precision, so it supports the quantitative direction without selecting a specific removal function.

[Read in atlas](index.html#TCS-1029) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5085 — Query complexity of Max-CSP testing

A tester must distinguish constraint systems whose optimum satisfied fractions lie on opposite sides of a fixed gap. It can query variables to reveal incident constraint occurrences, with only a constant number of occurrences per variable. The target is the asymptotic query complexity for every finite predicate template, gap, degree bound and density regime. The actual number of constraints matters because value is normalized by constraints rather than by all possible incidence slots. Known linear lower bounds and related streaming results leave the complete query classification unresolved.

[Read in atlas](index.html#TCS-5085) · [Unbounded-Width CSPs Are Untestable in a Sublinear Number of Queries](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.31) · [Near-Optimal Space Lower Bounds for Streaming CSPs](https://arxiv.org/abs/2604.01400v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0848 — Testing Submodularity

A submodular set function has diminishing marginal gains as the set receiving a new element grows. The source entry asks about testing this property from limited access to function values. A tester must distinguish true submodularity from functions requiring substantial change to acquire it. Efficient testing would help identify when optimization techniques relying on diminishing returns are applicable. The saved label does not specify the domain representation, range, distance measure, or desired query bound, so no particular tester or lower-bound target is inferred.

[Read in atlas](index.html#TCS-0848) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:37)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0841 — Equivalence Testing with Conditional Samples

Distribution equivalence testing asks whether two unknown distributions are the same or sufficiently far apart. Conditional sampling allows the algorithm to request samples restricted to a selected subset of the domain. The source entry asks about the power of this stronger sampling model for equivalence testing. Adaptive conditioning can focus attention on rare discrepancies that ordinary samples may miss. The saved title does not define behavior on zero-probability conditioning sets, the distance metric, or the query target, so those model choices remain explicit prerequisites for a complete claim.

[Read in atlas](index.html#TCS-0841) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:87)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0847 — Query complexity of directed acyclicity testing with bidirectional access

The graph is directed and has bounded incoming and outgoing degree. A tester can ask for individual incoming or outgoing neighbors of any labeled vertex. It must distinguish graphs without directed cycles from graphs requiring more than \(\varepsilon dn\) arc deletions to remove all directed cycles. The target is the optimal number of adaptive queries with error probability at most one third on either promised case. Recent lower bounds for outgoing-only access use a different model and do not by themselves settle this bidirectional question.

[Read in atlas](index.html#TCS-0847) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:41) · [An Optimal Separation Between Two Property Testing Models for Bounded Degree Directed Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.96) · [Lower Bounds for Testing Directed Acyclicity in the Unidirectional Bounded-Degree Model](https://arxiv.org/abs/2604.13577v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0672 — Efficient characterization of instance-optimal identity testing

The problem asks for an efficiently computable estimate of the optimal sample count for testing equality to a particular known distribution. The selected variant gives the reference probabilities and distance threshold explicitly as binary rational numbers. The estimate must match the information-theoretic optimum within one universal factor at exactly the requested distance. Existing instance-dependent bounds can disagree by arbitrarily large factors because their distance parameters differ. The card makes efficient evaluation precise while keeping the computation of the statistical test unrestricted.

[Read in atlas](index.html#TCS-0672) · [Open Problem: Tight Characterization of Instance-Optimal Identity Testing](https://proceedings.mlr.press/v247/canonne24a.html) · [An Automatic Inequality Prover and Instance Optimal Identity Testing](https://doi.org/10.1109/FOCS.2014.14)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-2535 — A dimension-free directed \(\mathrm{L}^{1}\) Poincaré inequality

The conjecture concerns every Lipschitz real-valued function on a continuous unit cube. It asks whether average distance to a monotone function is controlled by the average Euclidean magnitude of the negative gradient. The multiplicative constant must be independent of the dimension and the Lipschitz constant. A known inequality using the sum of coordinate decreases loses a square-root dimension factor. Later work proves a different inequality using squared quantities and explicitly leaves this conjecture open.

[Read in atlas](index.html#TCS-2535) · [Directed Poincaré Inequalities and \(\mathrm{L}^{1}\) Monotonicity Testing of Lipschitz Functions](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.61) · [Directed Isoperimetry and Monotonicity Testing: A Dynamical Approach](https://arxiv.org/abs/2404.17882) · [Analytic Property Testing: Directed Isoperimetry and Monotonicity](https://uwspace.uwaterloo.ca/items/e1f421e1-2f50-4ef9-af1e-45cdc345e24d)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3906 — Sample complexity of symmetric Markov-chain identity testing

A symmetric Markov chain evolves through transition probabilities that are symmetric between states. The source asks for the optimal sample complexity of identity testing from a single trajectory. Consecutive observations are dependent, and rarely visited states may hide differences from the proposed chain. Sharp bounds would quantify how much of a dynamical process must be observed to verify its transition behavior. The saved question does not specify starting-state assumptions, distance between chains, or mixing promises, so these cannot be silently replaced by independent-sample testing conventions.

[Read in atlas](index.html#TCS-3906) · [Testing Symmetric Markov Chains From a Single Trajectory](https://proceedings.mlr.press/v75/daskalakis18a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4259 — Optimal query cost of reducing testing adaptivity

A property tester probes bits in batches and may choose later batches using previous answers. The source counts one more batch than the number of adaptive rounds. The target is the largest query budget needed after reducing the number of rounds, among properties testable with the original budget. Both the property and its proximity and error guarantees remain fixed during the reduction. The benchmark asks for matching bounds with constants independent of all three resource parameters.

[Read in atlas](index.html#TCS-4259) · [An Adaptivity Hierarchy Theorem for Property Testing](https://doi.org/10.4230/LIPIcs.CCC.2017.27) · [An adaptivity hierarchy theorem for property testing — journal publication](https://doi.org/10.1007/s00037-018-0168-4) · [An adaptivity hierarchy theorem for property testing — institutional attachment](https://www.repository.cam.ac.uk/items/73b70279-d662-43f0-b591-98afd3ce529c)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4376 — Characterizing sublinear-query testable graph properties

Sublinear graph testing tries to infer a global property from a small number of local adjacency queries. The source studies sparse graph classes without imposing a uniform maximum-degree bound. It asks which properties remain testable and whether matching distributions of bounded-radius neighborhoods force graphs to be close under edge edits. Outerplanar results motivate extensions to broader planar and bounded-treewidth classes. The project explores when local views still determine approximate global structure despite the presence of high-degree vertices.

[Read in atlas](index.html#TCS-4376) · [Every Property of Outerplanar Graphs is Testable](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.21)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5210 — Polylogarithmic-query pattern-freeness testing

Pattern-freeness testing asks whether a sequence or function avoids a specified ordered pattern or is far from doing so. The cited work studies strongly sublinear algorithms for this task. The saved conjecture proposes polylogarithmic query complexity in n whenever pattern size k is constant. Such a bound would make even large inputs testable through a very small number of observations. The excerpt does not identify the full domain, distance measure, or dependence on proximity and the pattern, so those factors cannot be suppressed into a universal bound without qualification.

[Read in atlas](index.html#TCS-5210) · [Strongly Sublinear Algorithms for Testing Pattern Freeness](https://doi.org/10.4230/LIPIcs.ICALP.2022.98)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5443 — Polynomial-time learning of Gaussian mixtures

Learning a Gaussian mixture seeks a distribution close to an unknown mixture in total variation distance, potentially without recovering uniquely identifiable component parameters. The source proves polynomial sample sufficiency under differential privacy but notes that its use of a nonconstructive cover does not yield a finite-time implementation. It also highlights the broader question of obtaining a learning algorithm whose running time is polynomial in both the number of components and the dimension, even without privacy. This separates statistical feasibility from computational feasibility for mixtures without the extra structural assumptions used by many efficient methods. Progress on that algorithmic problem would provide a foundation for making the private existence result constructive.

[Read in atlas](index.html#TCS-5443) · [Mixtures of Gaussians are Privately Learnable with a Polynomial Number of Samples](https://proceedings.mlr.press/v237/afzali24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

## Differential privacy (6)

### TCS-0506 — Private PAC sample complexity from VC and Littlestone dimensions

A private PAC learner must infer a Boolean concept from examples while limiting what its output reveals about any one example. The reviewed question asks whether sample complexity is polynomial in VC dimension and the iterated logarithm of Littlestone dimension. VC dimension measures ordinary statistical capacity, whereas Littlestone dimension measures how many adaptive prediction challenges the class can support. A positive answer would bound the additional sample cost of privacy by a remarkably slow-growing contribution from that online complexity. The saved formulation fixes constant accuracy and confidence, permits improper hypotheses and unlimited computation, and specifies approximate privacy with an additive privacy parameter shrinking quadratically in sample size.

[Read in atlas](index.html#TCS-0506) · [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6673 — Optimal error for pure-DP continual counting

Continual counting releases prefix sums of a binary stream as its bits arrive. The target is the smallest worst-input expected maximum absolute error over all timestamps under pure differential privacy with privacy parameter one half. Every output prefix must depend only on the input prefix already observed, and privacy protects the whole transcript when one bit changes. The checked literature leaves a gap between logarithmic powers three halves and two, while newer matrix results concern different squared-error criteria. Matching bounds would quantify the unavoidable accuracy loss of this basic stream-release primitive.

[Read in atlas](index.html#TCS-6673) · [The Binary Tree Mechanism is Optimal for Approximate Differentially Private Continual Counting](https://arxiv.org/abs/2607.00876v2) · [The Price of Differential Privacy under Continual Observation](https://proceedings.mlr.press/v202/jain23b.html) · [Improved Error Bounds for Pure Differentially Private Continual Counting via Matrix Factorization](https://arxiv.org/abs/2607.08963) · [Costs of Arbitrary Real Matrix Factorizations for Pure-DP Continual Counting](https://arxiv.org/abs/2607.28703v2) · [A Near-Optimal Lower Bound for Prefix-Matrix Factorizations](https://arxiv.org/abs/2608.08238)
Existing status: `open` · Summary written: 2026-09-11

### TCS-0510 — Cost of privacy in online learning

Online classification requires predicting each arriving example before its correct label is revealed. The 2022 source asks whether imposing differential privacy changes which concept classes can be learned in the mistake-bound model. A mistake guarantee must control errors across the sequence, while privacy limits the influence of one participant's data on the released predictions. The tension is that information retained to improve future predictions can also reveal earlier examples. An equivalence would connect private and ordinary online learnability, but this historical entry still needs the source's precise privacy and sequence conventions before it becomes a complete card.

[Read in atlas](index.html#TCS-0510) · [COLT / PMLR](https://proceedings.mlr.press/v178/open-problem-sanyal22a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0507 — Optimal regret for private stochastic online learning

Stochastic decision-theoretic online learning repeatedly selects among K actions with different expected losses. The 2024 source asks for the optimal gap-dependent pseudo-regret under epsilon-differential privacy. Its nonprivate benchmark scales as \(\log (K)\) divided by the smallest positive gap between the best and competing actions. That gap measures how much statistical evidence is available for distinguishing good decisions from worse ones. Determining the private counterpart would isolate the additional cost of protecting individual observations, including whether it introduces a dependence on the number of rounds that the nonprivate benchmark avoids.

[Read in atlas](index.html#TCS-0507) · [COLT / PMLR](https://proceedings.mlr.press/v247/hu24a.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3312 — Polynomial-time private convex-hull point selection

The geometric task is to output a point inside the convex hull of a private collection of points. The 2020 source asks whether this can be done in running time polynomial in both the number n of points and the ambient dimension d. Without privacy, choosing an input point already gives a convex-hull point, but that output can directly disclose an individual's record. The problem therefore combines a geometric feasibility condition with restrictions on how much any single input can influence the output. A polynomial-time solution would make private convex-hull methods more broadly usable, subject to the source's domain assumptions, sample requirement, and allowed failure probability.

[Read in atlas](index.html#TCS-3312) · [How to Find a Point in the Convex Hull Privately](https://doi.org/10.4230/LIPIcs.SoCG.2020.52)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6825 — Computational versus statistical privacy in the curator model

Computational differential privacy protects against efficient adversaries, whereas statistical differential privacy also protects against unbounded ones. The 2014 textbook asks whether that relaxation can improve achievable utility when one trusted curator holds the data. The issue is whether computational protection permits more informative outputs, beyond merely making an existing private mechanism faster. This would show that cryptographic assumptions can change the accuracy frontier even without distributing trust across several parties. A 2023 paper gives a conditional separation under strong cryptographic assumptions, so the textbook question is historical context rather than an unqualified assertion of present open status.

[Read in atlas](index.html#TCS-6825) · [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/privacybook.html) · [Towards Separating Computational and Statistical Differential Privacy (FOCS 2023)](https://doi.org/10.1109/FOCS57990.2023.00042)
Existing status: `source_open` · Summary written: 2026-09-11

## Constraint satisfaction (18)

### TCS-6635 — Finite-domain promise CSP dichotomy

A finite promise CSP distinguishes inputs satisfying stronger local constraints from inputs failing even weaker constraints. The question asks whether every fixed finite template pair has a deterministic polynomial-time decision algorithm or is NP-hard under promise-preserving many-one reductions. The algorithm or reduction may depend on the pair, and no effective procedure for classifying input templates is required. The ordinary CSP dichotomy and several promise subclasses are known, but relaxing the constraints changes the classification problem substantially. The checked 2026 results concern restricted families and leave this full unconditional decision dichotomy open in the cited sources.

[Read in atlas](index.html#TCS-6635) · [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538v1) · [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021v2) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914v11) · [Promise Constraint Satisfaction: Algebraic Structure and a Symmetric Boolean Dichotomy](https://arxiv.org/abs/1704.01937v2) · [Dichotomy for Symmetric Boolean PCSPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.57) · [Promises Make Finite (Constraint Satisfaction) Problems Infinitary](https://www.karlin.mff.cuni.cz/~barto/Articles/DoNotPromise.pdf) · [Towards infinite PCSP: a dichotomy for monochromatic cliques](https://arxiv.org/abs/2605.09815v1) · [Approximating 1-In-3 SAT by Linearly Ordered Hypergraph 3-Colouring Is NP-Hard](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.184)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6636 — Bodirsky–Pinsker conjecture

Infinite-domain CSPs assign variables values from a fixed countable structure while satisfying finitely listed constraints. The conjecture asks for a P-versus-NP-complete dichotomy for reducts of finitely bounded homogeneous structures. These restrictions provide symmetry and a finite description of forbidden patterns despite the unbounded value domain. A classification would show whether this structural description rules out intermediate complexity across many logical and combinatorial problems. The saved review identifies the missing general algorithmic step and separates special subclasses, lower logical dichotomies, and meta-problem decidability from a proof of the full conjecture.

[Read in atlas](index.html#TCS-6636) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914) · [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf) · [Topology Is Irrelevant (In a Dichotomy Conjecture for Infinite Domain Constraint Satisfaction Problems)](https://doi.org/10.1137/18M1216213) · [Three Fundamental Questions in Modern Infinite-Domain Constraint Satisfaction](https://arxiv.org/abs/2502.06621) · [Constraint Satisfaction Problems over Finitely Bounded Homogeneous Structures: a Dichotomy between FO and L-hard](https://arxiv.org/abs/2601.22691) · [Decidability of Interpretability](https://arxiv.org/abs/2602.02302)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6637 — Constant-colour polynomial-time colouring of 3-colourable graphs

The input graph is promised to admit a proper coloring with three colors. The question asks whether some fixed constant number of colors can always be found in randomized polynomial time. The promise hides a small partition into independent sets, while the algorithm may use a larger palette. A positive result would show that a fixed relaxation of the domain makes this central promise problem tractable. The saved review distinguishes hardness for small output palettes and restricted logical models from hardness for every constant, while polynomially growing color counts remain short of the target.

[Read in atlas](index.html#TCS-6637) · [Better coloring of 3-colorable graphs](https://arxiv.org/abs/2406.00357) · [Algebraic Approach to Promise Constraint Satisfaction](https://arxiv.org/abs/1811.00970) · [d-To-1 Hardness of Coloring 3-Colorable Graphs with \(O(1)\) Colors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.62) · [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904) · [Undefinability of Approximation of 2-to-2 Games](https://arxiv.org/abs/2504.03523)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6675 — Search-to-decision equivalence for finite promise CSPs

A decision promise CSP only separates strong satisfiability from failure of weak satisfiability. The reviewed question asks whether polynomial-time decision always implies polynomial-time construction of an actual weak solution. Fixing variables can move an instance into the intermediate region where a promise decider may answer arbitrarily. An equivalence would justify turning tractability classifications into practical assignments throughout finite promise CSPs. The saved review emphasizes that hardness of rounding all relaxation-accepted instances and undecidability of template meta-problems do not settle this fixed-template promised search question.

[Read in atlas](index.html#TCS-6675) · [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538) · [Algebraic approach to promise constraint satisfaction](https://arxiv.org/abs/1811.00970) · [Ineffectiveness for Search and Undecidability of PCSP Meta-Problems](https://arxiv.org/abs/2504.04639) · [New Algorithms and Hardness Results for Robust Satisfiability of (Promise) CSPs](https://arxiv.org/abs/2602.10368) · [Publications — FOCS 2025 research summary](https://albertolarrauri.github.io/publications/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-3585 — Exact exponential-time equivalence for nonnegative Boolean Max-CSP

A Boolean Max-CSP instance asks for an assignment satisfying constraints of maximum total nonnegative weight. Each fixed language has a degree defined by the real multilinear polynomials of its predicates. The question asks whether an exact algorithm with exponential base \(\alpha\) for any NP-hard degree-d language yields the same base for weighted Max d-CNF-SAT. The known classification allows negative weights or imposes closure properties on the language. The remaining issue is preserving the exponential base when removing the sign restriction; the 2024 journal article still asks it.

[Read in atlas](index.html#TCS-3585) · [Optimal Polynomial-Time Compression for Boolean Max CSP](https://doi.org/10.4230/LIPIcs.ESA.2020.63) · [Optimal Polynomial-Time Compression for Boolean Max CSP](https://doi.org/10.1145/3624704)
Existing status: `open` · Summary written: 2026-09-12

### TCS-1978 — Search tractability of BLP-solvable promise CSPs

The basic linear programming relaxation can solve the decision version of some promise CSPs. The source asks whether every such template also admits a polynomial-time search algorithm. A fractional solution certifies useful local consistency without directly assigning one legal target-domain value to each variable. A general constructive theorem would make this important relaxation sufficient for producing solutions as well as recognizing the promise gap. The saved question concerns genuinely promised instances, so difficulties rounding arbitrary instances accepted by the relaxation must not automatically be treated as a negative answer.

[Read in atlas](index.html#TCS-1978) · [Promise and Infinite-Domain Constraint Satisfaction](https://doi.org/10.4230/LIPIcs.CSL.2024.41)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0441 — Characterizing CSP languages with linear non-redundancy

A constraint language specifies which local relations may appear in its CSP instances. The recorded question asks which languages have linear non-redundancy. Non-redundancy concerns how much of an instance remains essential after logically unnecessary constraints are removed. A characterization could connect algebraic properties of the language with the possibility of compressing constraint systems. The saved workshop title does not define the size parameter or redundancy criterion, so the intended linear bound must be recovered before it can be equated with a sparsification theorem or a kernel-size guarantee.

[Read in atlas](index.html#TCS-0441) · [PACS 2024 workshop](https://pacs2024.github.io/pacs2024-open-problems.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0504 — Uniform algorithms across tractable CSPs

Constraint satisfaction problems ask whether variables can be assigned values satisfying a fixed set of allowed relations. The source asks for a uniform polynomial-time algorithm covering the tractable cases. Uniformity would replace separate algorithms for individual templates by one procedure that handles their descriptions as part of its input. This tests whether a classification of tractable templates can be made algorithmically effective without hidden template-dependent costs. The saved record does not specify which template representation or tractability promise is allowed, so the source's exact uniformity requirement must be recovered before applying a nonuniform dichotomy theorem.

[Read in atlas](index.html#TCS-0504) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#uniform-ptime-algorithm-for-tractable-csps)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0444 — Polynomial kernels for Boolean MinCSP

Boolean MinCSP seeks assignments violating as few constraints as possible. The workshop question asks for polynomial kernels in the intended parameterized setting. A kernel replaces an instance by an equivalent smaller one whose size depends only on the parameter. Understanding which languages permit this compression would refine the tractability landscape beyond merely having fixed-parameter algorithms. The title does not specify the constraint languages or parameter, so the number of allowed violations and any weighted or deletion interpretation must be stated before one uniform kernel claim is made.

[Read in atlas](index.html#TCS-0444) · [PACS 2024 workshop](https://pacs2024.github.io/pacs2024-open-problems.pdf)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1173 — NP-intermediate \(\omega\)-categorical CSPs

An \(\omega\)-categorical structure has a strong finiteness property for the types of finite tuples under its symmetries. The source asks whether, assuming \(\mathrm{P}\ne \mathrm{NP}\), some CSP over such a structure is NP-intermediate. That would mean it lies in NP but is neither polynomial-time solvable nor NP-complete. An example would show that symmetry alone does not force the familiar tractable-versus-hard dichotomy. The saved question is broader than finitely bounded homogeneous template conjectures, and additional representational restrictions cannot be silently imposed when assessing whether those conjectures answer it.

[Read in atlas](index.html#TCS-1173) · [The Polynomial Hierarchy and \(\omega\)-Categorical CSPs](https://doi.org/10.4230/LIPIcs.MFCS.2026.96)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1555 — VCSP tractability without pp-constructions of \(K_{3}\)

Valued CSPs optimize sums of local costs instead of merely asking whether all relations are satisfied. The temporal source asks whether \(VCSP(A)\) is polynomial-time solvable whenever A cannot pp-construct K3. Primitive-positive constructions transfer the structure responsible for hardness from one template to another. A positive theorem would turn the absence of this obstruction into an algorithmic tractability criterion. The saved question does not spell out the valued construction notion or permitted temporal cost functions, so an ordinary relational no-K3 criterion cannot automatically be substituted.

[Read in atlas](index.html#TCS-1555) · [Temporal Valued Constraint Satisfaction Problems](https://doi.org/10.4230/LIPIcs.MFCS.2025.24)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1807 — Dichotomy for finite-domain restricted CSPs

A restricted constraint satisfaction problem asks whether an input structure maps homomorphically to a fixed domain A, under a promise that it maps to another structure B. The domain is finite, while the structure imposing the restriction may be infinite. The question asks whether every such problem is either polynomial-time solvable or NP-hard. The source establishes a dichotomy when the restriction is finite by relating these problems to ordinary constraint satisfaction. Extending the classification would show whether infinite promises introduce intermediate computational behavior even when the allowed assignments still come from a finite domain.

[Read in atlas](index.html#TCS-1807) · [Restricted CSPs and F-Free Digraph Algorithmics](https://doi.org/10.4230/LIPIcs.ICALP.2025.158)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3678 — Polynomial-time tractability testing for core crisp CSP languages

A crisp constraint language lists the allowed tuples over a finite domain, and the input is promised to be a core. The question asks for a polynomial-time test for an idempotent four-ary Siggers polymorphism. Both the domain and every relation are part of the input, so one uniform polynomial bound is required. The known finite-valued test and unrestricted-language NP-hardness do not answer this promised-core question. An ICALP 2026 article explicitly retains the relevant Siggers testing problem as open.

[Read in atlas](index.html#TCS-3678) · [Testing the Complexity of a Valued CSP Language](https://doi.org/10.4230/LIPIcs.ICALP.2019.77) · [Testing the complexity of a valued CSP language](https://arxiv.org/abs/1803.02289) · [The Complexity of Finding Coset-Generating Polymorphisms and the Promise Metaproblem](https://doi.org/10.4230/LIPIcs.ICALP.2026.169)
Existing status: `open` · Summary written: 2026-09-12

### TCS-3984 — Hardness of coloring 2-colorable 3-uniform hypergraphs

A proper hypergraph coloring assigns colors to vertices so that no hyperedge is monochromatic. The promise here is that every hyperedge has three vertices and that a two-coloring exists. The question asks whether finding a coloring with more than a logarithm-of-logarithm number of colors is NP-hard, or at least quasi-NP-hard. The source obtains stronger coloring hardness for four-uniform hypergraphs, where one additional vertex per edge gives reductions more flexibility. Transferring comparable hardness to triples would sharpen the boundary of what efficient algorithms can do under a very strong colorability promise.

[Read in atlas](index.html#TCS-3984) · [NP-Hardness of Coloring 2-Colorable Hypergraph with Poly-Logarithmically Many Colors](https://doi.org/10.4230/LIPIcs.ICALP.2018.15)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6725 — Logarithmic-color approximation of 3-colorable graphs

The input is an n-vertex graph promised to admit a proper coloring with three colors. The textbook asks whether polynomial time suffices to produce a proper coloring using only \(O(\log  n)\) colors. The promise ensures a very small solution exists but does not reveal the hidden partition into independent sets. Achieving a logarithmic color count would substantially narrow the gap between existence and efficient recovery of a coloring. The question is preserved from the 2011 source, and its current status has not been independently established by this drafting pass.

[Read in atlas](index.html#TCS-6725) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6748 — Boolean decision-Holant dichotomy

A Boolean decision-Holant problem asks whether local constraints on incident Boolean edge labels can all be satisfied. The saved textbook question seeks a complexity classification across the allowed constraint families. Each variable naturally participates through graph incidence, giving a structure different from completely unrestricted CSP occurrences. A dichotomy would identify which local signatures permit efficient decision and which support hardness. The historical note does not reproduce conventions about available unary signatures or graph restrictions, so these details must be fixed before applying a classification from a particular Holant variant.

[Read in atlas](index.html#TCS-6748) · [The Constraint Satisfaction Problem: Complexity and Approximability](https://drops.dagstuhl.de/entities/volume/DFU-volume-7)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7116 — Universal representation of NP by \(\omega\)-categorical CSPs

The source asks whether every problem in NP is polynomial-time equivalent to a CSP with an \(\omega\)-categorical template. Such templates may be infinite while retaining a strong symmetry property on finite tuples. A representation theorem would show that local constraint solving over this structured universe captures all nondeterministic polynomial-time tasks. It would also clarify how broad infinite-template CSP theory can be compared with finite-template classifications. The saved formulation is historical and does not specify its reduction conventions or effective template presentation, which remain relevant before one uniform encoding claim is made.

[Read in atlas](index.html#TCS-7116) · [Constraint Satisfaction Problems with Infinite Templates](https://www.lix.polytechnique.fr/~bodirsky/publications/csp-survey.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7124 — SNP definability of CSPs in NP

Some CSPs lie in NP even when their templates are infinite or structurally general. The historical source asks which of these CSPs can be defined in SNP. A syntactic characterization would identify when constraint satisfiability admits a restricted logical description. This could connect complexity membership with model-theoretic structure and support more systematic classifications. The saved note does not supply a proposed criterion or presentation assumptions for the template, so the question remains a characterization direction rather than a claim that every NP CSP already has such a definition.

[Read in atlas](index.html#TCS-7124) · [Constraint Satisfaction Problems with Infinite Templates](https://www.lix.polytechnique.fr/~bodirsky/publications/csp-survey.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

## Automated reasoning, rewriting and unification (15)

### TCS-6562 — Word equations with linear length constraints

Word equations require substitutions of finite strings that make two concatenations identical. Here the substitutions must also satisfy linear arithmetic constraints on their lengths, with all equations and coefficients supplied as input. The project asks for an algorithm that always decides whether these two kinds of constraints have a common solution. Length arithmetic alone forgets letter alignment, while separate string-solving procedures need not respect additional arithmetic restrictions. This is a basic decidability question for exact string constraints, before imposing practical running-time requirements.

[Read in atlas](index.html#TCS-6562) · [Word equations, constraints, and formal languages](https://arxiv.org/abs/2406.02160) · [Word Equations with Length Constraints via Weak Arithmetics and Matrix Reachability Problems](https://link.springer.com/chapter/10.1007/978-3-032-09524-4_4) · [The Termination of Nielsen Transformations Applied to Word Equations with Length Constraints](https://link.springer.com/chapter/10.1007/978-3-032-32592-1_14) · [NEXP-Completeness and Exponential Coefficient Growth for Existential Presburger Arithmetic with Divisibility](https://arxiv.org/abs/2606.14167v3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6643 — Decidability of unification in the basic modal logic K

Basic modal logic K interprets formulas on arbitrary accessibility relations between possible worlds. The problem asks whether it is decidable that a finite formula has a substitution instance valid at every world of every such model. Substitutions act simultaneously on all input variables, may introduce new variables, and leave no designated parameters fixed. Frames may be finite or infinite, and no reflexivity or transitivity condition is imposed. The requested algorithm must halt on every input; its time and the size of a possible substitution have no prescribed bounds.

[Read in atlas](index.html#TCS-6643) · [On the unification problem for GLP](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=9592&wshow=paper)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6650 — Deterministic polynomial-time equivalence testing for d-DNNFs

The problem asks whether two explicit d-DNNF circuits can be tested for exact Boolean equivalence in deterministic polynomial time. Decomposability requires disjoint variable sets at conjunctions, while determinism requires mutually exclusive inputs at disjunctions. The circuits may use unrelated internal decompositions and need not share a variable tree. Randomized polynomial-time equivalence testing is known, but its possibility of error does not satisfy this target. A resolution would clarify the cost of comparing and verifying succinct compiled Boolean representations.

[Read in atlas](index.html#TCS-6650) · [Proof Systems Based on Structured Circuits](https://arxiv.org/abs/2605.12378) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Testing Equivalence Probabilistically](https://users.cecs.anu.edu.au/~jinbo/02-d123.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6644 — Decidability of termination for one-rule string rewriting

A one-rule string system repeatedly replaces one fixed substring by another. The question is whether an algorithm can decide if every reduction sequence from every finite starting word eventually stops. Replacement positions are unrestricted, and the rule and alphabet are part of the input. Known decision procedures cover special rule families, while an August 2026 note still lists the arbitrary one-rule question as open. The answer must prove decidability or undecidability in Lean for global termination, rather than only termination from one supplied word.

[Read in atlas](index.html#TCS-6644) · [Decidability of Termination of Grid String Rewriting Rules](https://doi.org/10.1137/S009753979833297X) · [RTA Open Problem 21: Termination of one linear rule](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/21.html) · [String Rewriting Systems: Brief Introduction and Sample of Open Problems](https://arxiv.org/abs/2608.19397)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7194 — Singly exponential shortest solutions of word equations

A word equation asks for consistent substitutions of finite strings that make two concatenations identical. The conjecture says that every satisfiable equation of size n has some solution whose variable images have length at most two to a fixed polynomial in n. The bound must hold uniformly over all finite alphabets and arbitrarily many variable occurrences, with empty substitutions allowed. Known compression results make this length conjecture sufficient for NP membership of general word-equation satisfiability. Doubly exponential bounds and newer results for restricted equation families do not meet the universal single-exponential target.

[Read in atlas](index.html#TCS-7194) · [Application of Lempel-Ziv Encodings to the Solution of Word Equations](https://ii.uni.wroc.pl/~aje/WordEq2015/papers/PlandowskiRytter.pdf) · [Recompression: a simple and powerful technique for word equations](https://arxiv.org/abs/1203.3705) · [An Improved Version of Hmelevskii’s Theorem on Three-Variable Word Equations](https://doi.org/10.4230/LIPIcs.STACS.2026.77)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0163 — Complexity of satisfiable word equations

A word equation equates two sequences containing letters and variables that stand for finite strings. Satisfiability asks whether a consistent substitution makes the two resulting strings identical. The project seeks the computational complexity of this decision problem, sharpening the gap between NP-hardness and polynomial-space algorithms recorded in the sources. Substituted strings can be much larger than the equation, so an efficient algorithm must reason about their structure implicitly. Understanding this cost would clarify the algorithmic difficulty of one of the simplest exact string-solving tasks.

[Read in atlas](index.html#TCS-0163) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#complexity-of-word-equation-satisfiability)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0171 — Complexity of word unification

Word unification solves equations between concatenations by substituting strings for variables. The saved question asks for the exact computational complexity of deciding whether such substitutions exist. Even a short equation can have solutions whose direct representations are long. A sharp classification would clarify the algorithmic cost of a basic constraint language used in symbolic reasoning. The inherited label does not specify constants, empty-word allowances, or additional constraints, so the draft does not conflate unconstrained word equations with stronger regular-constrained or arithmetic variants.

[Read in atlas](index.html#TCS-0171) · [RTA Open Problems](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/92.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0114 — Satisfiability of String Constraints with Subsequence relation

The scattered-subsequence relation allows a word to be obtained by deleting letters from another word without changing their order. This project studies systems requiring a variable's string to be a subsequence of a concatenation of variables. Each variable must additionally belong to a regular language specified by a regular expression. The question is whether existence of one substitution satisfying all subsequence and domain constraints is decidable. Cyclic dependencies between reused variables make this a richer consistency problem than checking subsequence membership for two fixed strings.

[Read in atlas](index.html#TCS-0114) · [Automata Exchange](https://automata.exchange/24.13-satisfiability-of-string-constraints-with-subsequence-relation/)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0306 — Polynomial-time complementation of d-DNNFs

The problem asks for a uniform deterministic polynomial-time algorithm that complements any given d-DNNF circuit. Its output must remain decomposable and deterministic and agree with the Boolean complement on every assignment. The time bound includes constructing and writing a complete circuit over the original variables. A polynomial-size complement may conceivably exist without a known efficient construction, so that separate existence question is not the whole target. Known lower bounds for structured representations leave this general circuit operation unresolved.

[Read in atlas](index.html#TCS-0306) · [List of open questions: PTIME complementation of d-DNNF](https://a3nm.net/work/research/questions/#ptime-complementation-of-d-dnnf) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Structured d-DNNF Is Not Closed under Negation](https://doi.org/10.24963/ijcai.2024/398) · [On the Complexity of Language Membership for Probabilistic Words](https://doi.org/10.4230/LIPIcs.STACS.2026.5)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1595 — Decidability of fifth-order \(\beta\)-matching

Higher-order beta-matching asks whether one simply typed lambda term can be instantiated to become beta-equivalent to another. The order of the types controls how deeply functions can take other functions as arguments. The source identifies order five as the gap between a decidable order-four case and higher-order undecidability constructions. This project asks whether matching remains decidable at that intermediate order. Pinning down the threshold would explain which level of functional structure first permits the encoding of unrestricted computational behavior.

[Read in atlas](index.html#TCS-1595) · [Mechanized Undecidability of Higher-Order Beta-Matching](https://doi.org/10.4230/LIPIcs.FSCD.2025.17)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1992 — Decidability of Presburger arithmetic with primes

Presburger arithmetic describes integers using addition and order without unrestricted multiplication. The saved question asks whether adding a predicate for prime numbers preserves decidability. The added predicate imports number-theoretic structure that the base arithmetic language cannot directly express. An answer would mark a sharp boundary between a tame linear theory and richer arithmetic reasoning. The excerpt attributes this question to its source but does not specify the integer-domain convention or provide a current progress audit, so the draft keeps the decisional target separate from later-status claims.

[Read in atlas](index.html#TCS-1992) · [An Introduction to the Theory of Linear Integer Arithmetic (Invited Paper)](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.1)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5603 — Polynomial-time recognition of abelian cores

The input is an entire finite algebra specified by tables of its basic operations. It is promised to possess an idempotent Taylor term, although no witness is supplied. The task is to decide whether its smallest endomorphic image is abelian in the universal-algebraic sense. A quasipolynomial-time recognition algorithm is known. This is a classification problem for algebras, distinct from solving a particular list of term equations.

[Read in atlas](index.html#TCS-5603) · [On the Complexity Dichotomy for the Satisfiability of Systems of Term Equations over Finite Algebras](https://doi.org/10.4230/LIPIcs.MFCS.2023.66) · [Equations over finite algebras](https://www.algebra.uni-linz.ac.at/Slides/sl-aaa105-6.pdf)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6016 — Satisfiability of weak MSO+U over infinite words

Weak monadic second-order logic quantifies over finite sets of positions, and the U extension adds an unbounding mechanism. The cited work studies this logic over infinite structures. The saved question asks whether satisfiability is decidable over infinite words. An answer would determine whether one can effectively recognize when a specification has any infinite sequential model. The excerpt does not reproduce the unbounding quantifier semantics or syntax restrictions, so the target remains attached to the source's precise logic rather than a broader unrestricted second-order language.

[Read in atlas](index.html#TCS-6016) · [Weak MSO+U over infinite trees](https://doi.org/10.4230/LIPIcs.STACS.2012.648)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-7125 — Two-sided distributive unification with a unit

Unification modulo distributivity seeks substitutions making expressions equal under both left and right distributive laws. The saved question additionally includes a multiplicative unit. It asks whether an algorithm can always decide the existence of a unifier in that equational theory. The unit can interact with distributive expansion and contraction, potentially changing the search space substantially. The source summary does not list any further associativity or commutativity axioms, so the draft does not add them or treat this as unification in an ordinary ring.

[Read in atlas](index.html#TCS-7125) · [Unification Theory](https://www.cs.bu.edu/fac/snyder/pubs.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7134 — Polynomial-time equivalence of free binary decision diagrams

A free binary decision diagram evaluates a Boolean function by following variable tests, with no variable tested twice along a root-to-leaf path. Different paths may inspect variables in different orders. The saved question asks whether equivalence of two such diagrams can be decided in polynomial time in their representation sizes. Comparing their graph shapes is insufficient because structurally different diagrams can still agree on every assignment. An efficient exact test would support reliable manipulation of flexible decision representations, and the 2002 table entry remains a dated question rather than evidence of a newly checked complexity classification.

[Read in atlas](index.html#TCS-7134) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819)
Existing status: `source_open` · Summary written: 2026-09-11

## Database theory and finite model theory (20)

### TCS-6678 — FO model checking on hereditary monadically dependent graph classes

First-order model checking asks whether a graph satisfies a logical sentence using vertex quantification and adjacency. The conjecture seeks fixed-parameter tractability on every hereditary effectively monadically dependent graph class, parameterized by sentence length. The structural promise limits which arbitrary graphs can be encoded through first-order interpretations with unary labels. A positive result would extend broad logical algorithmic guarantees into graph classes that may be dense. The reviewed formulation supplies no decomposition and requires a computable parameter dependence, so structural existence results or algorithms needing extra construction sequences do not automatically establish it.

[Read in atlas](index.html#TCS-6678) · [Graph classes through the lens of logic](https://arxiv.org/abs/2501.04166) · [Monadically Stable and Monadically Dependent Graph Classes: Characterizations and Algorithmic Meta-Theorems](https://media-api.suub.uni-bremen.de/api/core/bitstreams/64278fff-a8bb-43a8-aa91-32469c6394ac/content) · [Flip-Breakability: A Combinatorial Dichotomy for Monadically Dependent Graph Classes](https://arxiv.org/abs/2403.15201) · [First-Order Model Checking on Monadically Stable Graph Classes](https://arxiv.org/abs/2311.18740) · [Merge-width and First-Order Model Checking](https://arxiv.org/abs/2502.18065) · [Near-Linear Time Computation of Welzl Orders on Graphs with Linear Neighborhood Complexity](https://arxiv.org/abs/2602.14625) · [Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes](https://arxiv.org/abs/2607.10941) · [Monadically stable graph classes — Oberwolfach talk](https://mccarty.math.gatech.edu/McCarty-2025-Oberwolfach.pdf) · [Flip-Width: Cops and Robber on Dense Graphs](https://ieee-focs.org/FOCS-2023-Papers/pdfs/FOCS2023-35YPEGokY3iqqos5xlCDsn/189400a663/189400a663.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6645 — Constant-delay conjunctive-query classification

A conjunctive query joins relations and projects the resulting assignments to its output variables. The question asks for a terminating classifier deciding which queries allow linear preprocessing followed by constant-delay enumeration of distinct answers. Self-joins are allowed, so repeated uses of one relation can create symmetries and dependencies absent from simpler classifications. A complete answer would identify the exact boundary for efficiently generating query results in this basic language. The reviewed formulation fixes the RAM and termination conventions, and the classifier itself need not run quickly or output the enumeration algorithm.

[Read in atlas](index.html#TCS-6645) · [Conjunctive Queries With Self-Joins, Towards a Fine-Grained Enumeration Complexity Analysis](https://arxiv.org/abs/2206.04988) · [On Acyclic Conjunctive Queries and Constant Delay Enumeration](https://webusers.imj-prg.fr/~arnaud.durand/papers/BDGcsl07.pdf) · [Enumerating answers of acyclic conjunctive queries with self-joins (Report)](https://www.normalesup.org/~rouvroy/papers/Report_M1S1.pdf) · [The Role of Semirings in Incremental View Maintenance](https://arxiv.org/abs/2606.07795)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7195 — A logic capturing polynomial time

Is there an effective logic for all polynomial-time properties of finite unordered structures? Its sentences must describe properties unchanged by renaming domain elements. Each sentence must compile effectively to an evaluation algorithm with a polynomial time bound. Fixed-point logic captures polynomial time when an order is supplied, but that is a different input model. Current candidate and restricted-class results leave the general existence question open.

[Read in atlas](index.html#TCS-7195) · [The Quest for a Logic Capturing PTIME: LICS 2008 invited paper](https://lics.siglog.org/2008/Grohe-TheQuestforaLogicCa.html) · [Is Polynomial Time Choiceless?](https://logic.rwth-aachen.de/pub/graedel/cptYuri.pdf) · [The quest for a logic for Ptime](https://www.cl.cam.ac.uk/~btp26/esslli/lecture1.pdf) · [Choiceless Polynomial Time with Witnessed Symmetric Choice](https://arxiv.org/abs/2205.14003v3) · [Subgroup Accessibility in Group Order Logic](https://arxiv.org/abs/2609.00499)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6680 — Decidability of conjunctive-query entailment in SROIQ

An expressive ontology describes facts and rules that can require additional unnamed objects in every model. The reviewed question asks whether one terminating algorithm can decide all Boolean conjunctive queries against finite SROIQ knowledge bases. Such a query looks for a relational pattern, including joins that require several conditions to hold for the same objects. Consistency checking and known decidable fragments do not settle the unrestricted combination of query joins, counting, inverse roles, and role compositions. The chosen semantics includes infinite models, so the saved undecidability result for finite-model entailment addresses a different question.

[Read in atlas](index.html#TCS-6680) · [Absorption-Based Query Entailment Checking for Expressive Description Logics](https://ceur-ws.org/Vol-2373/paper-25.pdf) · [The Even More Irresistible SROIQ](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf) · [Nominals, Inverses, Counting, and Conjunctive Queries or: Why Infinity is your Friend!](https://www.cs.ox.ac.uk/files/2175/paper.pdf) · [Query Answering in the Horn Fragments of the Description Logics SHOIQ and SROIQ](https://www.ijcai.org/Proceedings/11/Papers/178.pdf) · [The Curse of Finiteness: Undecidability of Database-Inspired Reasoning Problems in Very Expressive Description Logics](https://ceur-ws.org/Vol-1577/paper_12.pdf) · [Revisiting Conjunctive Query Entailment for S](https://arxiv.org/abs/2511.07933)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0492 — Conjunctive-query containment under bag semantics

Under bag semantics, database tuples and query answers have multiplicities rather than just presence or absence. The question asks whether containment of two conjunctive queries is decidable when their output multiplicities must be ordered on every finite bag database. Each query sums products of input multiplicities over satisfying assignments, so ordinary set-containment reasoning does not directly capture the comparison. A decision procedure would settle a basic semantic question relevant to duplicate-preserving query transformations. The saved review distinguishes progress for unions or restricted joins from the plain unrestricted conjunctive-query problem retained here.

[Read in atlas](index.html#TCS-0492) · [List of open questions: Decidability of conjunctive query containment under bag semantics](https://a3nm.net/work/research/questions/#decidability-of-conjunctive-query-containment-under-bag-semantics) · [Semirings in Databases, Automata, and Logic (Dagstuhl Seminar 25081)](https://doi.org/10.4230/DagRep.15.2.89) · [Bag Semantics Conjunctive Query Containment. Four Small Steps Towards Undecidability](https://doi.org/10.1145/3651604) · [Bag Containment of Join-On-Free Queries](https://doi.org/10.4230/LIPIcs.ICDT.2025.5) · [Bag Semantics Query Containment: The CQ vs. UCQ Case and Other Stories](https://arxiv.org/abs/2503.07219v3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-3631 — A logic capturing logarithmic space

The input is a finite relational structure with no distinguished ordering of its elements. The question asks for an effective logic expressing exactly all isomorphism-invariant Boolean queries decidable in deterministic logarithmic space. Each sentence must compile to a halting evaluation algorithm with a certified logarithmic workspace bound. The proposed CLogspace logic is known to miss some such queries, while ordered structures and strings admit stronger capturing results. A solution would settle a broad descriptive-complexity question linking small-memory computation to the expressive power of logical queries.

[Read in atlas](index.html#TCS-3631) · [Choiceless Logarithmic Space](https://doi.org/10.4230/LIPIcs.MFCS.2019.31) · [Is Polynomial Time Choiceless?](https://logic.rwth-aachen.de/pub/graedel/cptYuri.pdf) · [FC-Datalog as a Framework for Efficient String Querying](https://arxiv.org/abs/2501.10344v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0488 — Computability of entropic query-size bounds

Entropy-based bounds use information inequalities to limit the number of answers a database query can produce. The source asks whether the relevant entropic query-size bounds are computable. The issue is not merely evaluating one join, but determining an extremal bound over all data distributions or instances satisfying the supplied constraints. An effective method would strengthen the use of information theory in predicting query output size. The inherited label does not preserve the constraint language, exact-versus-approximate target, or entropy region, so these must be recovered before the computability claim is formalized.

[Read in atlas](index.html#TCS-0488) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0482 — Linear-round convergence over stable semirings

A polynomial system over a commutative semiring can be evaluated by repeatedly updating every coordinate from the previous vector. The question asks whether p-stability guarantees convergence after \(O((p+1)n)\) rounds from the zero vector. The proposed bound is linear in the number of coordinates and uniform across coefficients and polynomial degrees. It would sharpen convergence guarantees for grounded Datalog computations carrying semiring annotations. The saved formulation counts synchronous rounds rather than arithmetic time, so a bound on evaluation cost or a result for a different update schedule would address a separate resource question.

[Read in atlas](index.html#TCS-0482) · [Semirings in Databases, Automata, and Logic (Dagstuhl Seminar 25081)](https://doi.org/10.4230/DagRep.15.2.89) · [Polynomial Time Convergence of the Iterative Evaluation of Datalogo Programs](https://arxiv.org/abs/2312.14063v2) · [Publication listing: Optimal Convergence of Iterative Methods for Datalogo](https://hung-q-ngo.github.io/publications.html)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0487 — Complexity of polymatroid query-size bounds

Polymatroid bounds replace entropy constraints by a collection of abstract submodularity inequalities when estimating query output sizes. The source asks for the computational complexity of obtaining these bounds. The attraction is a potentially more tractable relaxation that still captures useful dependencies among database attributes. Understanding its complexity would show when the relaxation can guide algorithms rather than merely certify a bound existentially. The saved entry does not specify the representation of constraints or requested numerical precision, so the full source problem is needed before identifying a particular linear program or complexity class.

[Read in atlas](index.html#TCS-0487) · [Algorithmic Aspects of Information Theory](https://doi.org/10.4230/DagRep.12.7.180)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0494 — BDD/FC conjecture

The BDD/FC conjecture asks whether every finite existential rule set with bounded derivation depth is finitely controllable. Bounded derivation depth is expressed by a finite positive rewriting for each conjunctive query that works on every database. Finite controllability means that a query failing in some unrestricted model also fails in a finite model. The question allows arbitrary finite relational arities and several atoms in a rule head. The known binary theorem requires single-head rules, and the checked PODS 2025 result posted in 2026 leaves the general conjecture open.

[Read in atlas](index.html#TCS-0494) · [List of open questions: Does bounded derivation depth imply finite controllability?](https://a3nm.net/work/research/questions/#does-bounded-derivation-depth-imply-finite-controllability) · [On the BDD/FC Conjecture](https://arxiv.org/abs/1408.2081) · [No Cliques Allowed: The Next Step Towards BDD/FC Conjecture](https://inria.hal.science/hal-05273623v1/file/2025-pods-no-cliques-allowed.pdf) · [No Cliques Allowed: The Next Step Towards BDD/FC Conjecture](https://arxiv.org/abs/2603.09558)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0499 — Query evaluation with treewidth parameter

Query evaluation checks whether a relational query has an answer on a supplied database. The source asks about its complexity when treewidth is the parameter controlling the query's structure. Treewidth measures how closely the pattern decomposes into small interacting pieces, suggesting dynamic programming methods. The challenge is determining the exact parameter dependence and whether the database-size exponent can be kept independent of treewidth. The inherited label does not specify the query language or whether a decomposition is supplied, so those choices remain necessary before a fixed-parameter or lower-bound statement can be made.

[Read in atlas](index.html#TCS-0499) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#complexity-of-query-evaluation-parameterized-by-treewidth)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0502 — Tractable probability versus tractable lineage

A probabilistic query may have an efficiently computable answer probability even when its Boolean lineage has a complicated representation. The source asks whether tractable probability evaluation necessarily comes with tractable lineages. The question tests whether a compact reusable explanation is essential to efficient numerical evaluation or merely one common route. A separation would show that direct probability algorithms can exploit structure missed by the chosen lineage formalism. The saved label does not define tractable lineage or the database class, so those representation and input assumptions must be recovered before a universal implication can be assessed.

[Read in atlas](index.html#TCS-0502) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#do-tractable-queries-on-probabilistic-instances-have-tractable-lineages)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-0505 — Uniform reliability of homomorphism-closed queries

Reliability asks how likely a structure retains a desired property after random choices determine which facts or edges survive. The source studies this task for homomorphism-closed queries in a uniform setting. The question seeks a complexity classification connecting the logical form of the property with probability computation. Such a classification would explain when a robust structural condition remains tractable under uncertainty. The saved label does not specify the uniform probability convention, query representation, or exact-versus-approximate output, so those choices must be restored before applying results for arbitrary independent probabilities.

[Read in atlas](index.html#TCS-0505) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#complexity-of-uniform-reliability-for-homomorphism-closed-queries)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-1251 — Output-sensitive evaluation of cyclic queries

A conjunctive query combines several required relations, and cycles make those requirements interact around a closed pattern. Output-sensitive evaluation measures work using both the input size and the actual number of answers. The source asks whether techniques available for triangles can extend to arbitrary cyclic conjunctive queries. Large intermediate relations can be wasteful even when the final output is small. The project seeks evaluation strategies that exploit the whole query structure instead of paying for every locally possible combination.

[Read in atlas](index.html#TCS-1251) · [Output-Sensitive Evaluation of Acyclic Conjunctive Regular Path Queries](https://doi.org/10.4230/LIPIcs.ICDT.2026.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-3557 — Does extension preservation eliminate stratified intensional negation?

Stratified Datalog can negate relations already computed in earlier stages. Semi-positive Datalog only negates input relations. The question asks whether preserving answers when new values extend a database always permits the simpler semi-positive form. The input growth must preserve every relation on tuples of old values, which differs from unrestricted monotonicity. The source leaves this converse expressiveness question open, and the checked later first-order preservation results do not resolve it.

[Read in atlas](index.html#TCS-3557) · [Datalog with Negation and Monotonicity](https://doi.org/10.4230/LIPIcs.ICDT.2020.19) · [Weaker Forms of Monotonicity for Declarative Networking](https://www.basketsman.com/public/documents/posters/poster_pods2014.pdf) · [Extension Preservation in the Finite and Prefix Classes of First Order Logic](https://doi.org/10.4230/LIPIcs.CSL.2021.18)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4458 — First-order versus successor-invariant logic

Successor-invariant first-order logic may use an added successor ordering, but its answer must not depend on which ordering was chosen. The source asks whether efficient model checking can extend as broadly as for plain first-order logic. It suggests bounded-expansion and locally excluded-minor classes beyond its existing topological-subgraph restriction. Adding order can destroy structural sparsity in the representation used by standard methods. The challenge is to exploit invariance without paying the algorithmic cost of treating that arbitrary order as unrestricted extra graph structure.

[Read in atlas](index.html#TCS-4458) · [Successor-Invariant First-Order Logic on Graphs with Excluded Topological Subgraphs](https://doi.org/10.4230/LIPIcs.CSL.2016.18)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-4995 — Entropic width versus submodular width

Width measures summarize how a database join's variable interactions affect the running time of decomposition-based algorithms. The source compares entropic width with submodular width and records the inequality that entropic width is no larger. The extracted question asks whether that inequality can ever be strict. A gap would show that the two structural descriptions capture different levels of inherent join complexity. Resolving it would help connect entropy-based lower-bound arguments with the width parameters used by algorithms, rather than assuming they describe the same obstruction merely because one always bounds the other.

[Read in atlas](index.html#TCS-4995) · [The Quest for Faster Join Algorithms (Invited Talk)](https://doi.org/10.4230/LIPIcs.ICDT.2025.1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6157 — Determinacy and rewriting of regular path queries

Regular path queries select pairs of graph vertices joined by a path whose edge labels satisfy a regular expression. A collection of views determines a query when any two databases agreeing on all view answers also agree on the query answer. The cited discussion asks whether this determinacy property is decidable for regular path queries and what language can express the resulting rewritings. The paper's own focus on unions of path-length queries provides related positive results without answering that full labeled-path question. Understanding determinacy would establish when graph queries can be recovered exactly from previously computed views.

[Read in atlas](index.html#TCS-6157) · [Asymptotic Determinacy of Path Queries using Union-of-Paths Views](https://doi.org/10.4230/LIPIcs.ICDT.2015.44)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-6372 — Cai–Fürer–Immerman definability in choiceless polynomial time

CFI graphs hide an even-or-odd parity in symmetric gadgets built over a base graph. The input provides adjacency but no arbitrary order or labels revealing the hidden parity. The question asks for one choiceless polynomial-time program with counting that recovers parity for every base graph. The model may construct nested sets, but its total resources are polynomial in the expanded input size. Known positive cases and restricted lower bounds do not settle the full unordered question.

[Read in atlas](index.html#TCS-6372) · [Definability of Cai-Fürer-Immerman Problems in Choiceless Polynomial Time](https://doi.org/10.4230/LIPIcs.CSL.2016.19) · [Lower Bounds for Choiceless Polynomial Time via Symmetric XOR-Circuits](https://doi.org/10.4230/LIPIcs.MFCS.2023.73) · [Choiceless Computation and Symmetry: Limitations of Definability](https://doi.org/10.4230/LIPIcs.CSL.2021.33) · [Symmetric Proofs in the Ideal Proof System](https://doi.org/10.4230/LIPIcs.MFCS.2025.40)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7128 — Unconditional constant-delay query-enumeration lower bounds

Constant-delay enumeration aims to produce query answers promptly after an initial preprocessing phase. The source asks for unconditional lower bounds for natural queries, including a distance-two example. The target is to prove an inherent limitation directly rather than obtain it only from an unproved fine-grained conjecture. Such a result would strengthen the foundations of query-enumeration classifications and clarify which costs are mathematically unavoidable. The source's preprocessing budget, RAM operations, and precise distance-two output convention matter, because lower bounds can change when stronger indexing or different output requirements are permitted.

[Read in atlas](index.html#TCS-7128) · [Constant Delay Enumeration for Conjunctive Queries](https://databasetheory.org/sites/default/files/2016-06/segoufin.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

## Miscellaneous (2)

### TCS-7177 — \(1/3\)–\(2/3\) conjecture

A partial order records known comparisons, and its linear extensions are all compatible complete rankings. The conjecture asks whether every finite non-total order has an incomparable pair that appears in either relative order in at least one third of all extensions. The extensions are weighted uniformly, and both endpoints of the interval are allowed. A three-element order with only one comparison shows that the constant one third cannot be improved universally. A resolution would identify the sharp balance guarantee for a comparison in sorting with partial information.

[Read in atlas](index.html#TCS-7177) · [Balancing pairs and the cross product conjecture](https://trotter.math.gatech.edu/papers/97.pdf) · [Linear extensions of finite posets](https://arxiv.org/abs/2311.02743) · [Balancing Extensions in Posets of Large Width](https://arxiv.org/abs/2509.11549) · [Balance Constants, Majority Cycles, and the Gold Partition Conjecture through Fourteen Elements](https://arxiv.org/abs/2607.23926v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7290 — Extremal size of sunflower-free set families

A sunflower is a collection of distinct sets with one common pairwise intersection. For fixed r, the target is the maximum size of a family of k-element sets containing no r-member sunflower. Determine its growth as k increases within constant factors that may depend on r. The ground set is any finite universe and the question imposes no algorithmic restrictions. The sunflower conjecture predicts at most exponential growth, a weaker claim than determining the full extremal order.

[Read in atlas](index.html#TCS-7290) · [Improved sunflower bounds](https://arxiv.org/abs/1908.08483)
Existing status: `source_open` · Summary written: 2026-09-12
