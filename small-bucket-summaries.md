# Working summaries — small categories

571 five-sentence working summaries, based on saved source material.
These intermediate explanations preserve each record's existing evidence and status; they do not constitute completed research cards or a new open-status review.

## Computability and algorithmic information theory (18)

### TCS-6646 — Martin’s conjecture

Turing-invariant functions send mutually computable reals to mutually computable outputs. Under determinacy and dependent choice, Martin’s conjecture predicts a rigid hierarchy for these operations when they are compared on Turing cones. Part I says every invariant function is constant in degree on a cone or computes its input on a cone. Part II says all operations above the identity are prewellordered, with the Turing jump increasing their ordinal rank by exactly one. Known uniform and order-preserving cases, choice-based counterexamples and conditional results for other output degrees leave the full stated conjecture unresolved in the checked sources.

[Read in atlas](index.html#TCS-6646) · [On the Hierarchy of Natural Theories](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/on-the-hierarchy-of-natural-theories/FEF058E948E6E8B8A4F5F174E02AFCC9) · [Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://arxiv.org/abs/1109.1875v2) · [Part 1 of Martin’s Conjecture for order-preserving and measure-preserving functions](https://arxiv.org/abs/2305.19646v3) · [Erratum — Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://math.berkeley.edu/~marks/errata/mss_errata.html) · [On a question of Slaman and Steel](https://arxiv.org/abs/2004.00174v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6648 — Kolmogorov–Loveland randomness versus Martin-Löf randomness

Kolmogorov–Loveland strategies make computable fair bets while adaptively querying previously unseen coordinates of an infinite binary sequence. The problem asks whether defeating every such strategy implies passing every uniform effective null test for fair-coin measure. Strategies may be partial and may omit coordinates forever, but they cannot borrow, revisit observed bits or inspect them through an oracle. A complete Lean answer must prove the implication or exhibit one non-Martin-Löf-random sequence on which every strategy has bounded capital. Known subsequence theorems, nonadaptive-order separations and the 2025 open-set obstruction leave that exact comparison unresolved.

[Read in atlas](index.html#TCS-6648) · [Kolmogorov-Loveland betting strategies lose the Betting game on open sets](https://arxiv.org/abs/2403.19817) · [Kolmogorov–Loveland randomness and stochasticity](https://people.math.wisc.edu/~jsmiller8/Papers/kl.pdf) · [Comparing notions of randomness](https://people.math.wisc.edu/~slempp/papers/injrandom.pdf) · [A universal pair of \(1/2\)-betting strategies](https://www.sciencedirect.com/science/article/pii/S0890540121000183) · [Key Developments in Algorithmic Randomness](https://arxiv.org/abs/2004.02851)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6647 — Rigidity of the Turing degrees

Turing degrees identify oracle sets that compute one another, and their order compares relative computational power. The question asks whether every bijection of all degrees that preserves and reflects this order fixes every degree. The target allows arbitrary set-theoretic automorphisms and requires a complete Lean proof of rigidity or of a nontrivial global automorphism. Known jump, cone, representation and local-structure results impose substantial restrictions without settling the entire order. Cooper’s historical full-solution claim remains explicitly separated from verified partial results, and the card records uncertain status because its construction was reported as unverified.

[Read in atlas](index.html#TCS-6647) · [Defining the Turing Jump](https://math.berkeley.edu/~slaman/papers/jump.pdf) · [Global Properties of the Turing Degrees and the Turing Jump](https://math.berkeley.edu/~slaman/papers/IMS_slaman.pdf) · [Permutations of the Integers Induce Only the Trivial Automorphism of the Turing Degrees](https://arxiv.org/abs/1603.00525) · [The \(\Delta^0_2\) Turing Degrees: Automorphisms and Definability](https://people.math.wisc.edu/~soskova/preprints/autdef.pdf) · [Sets of Real Numbers Closed under Turing Equivalence: Applications to Fields, Orders and Automorphisms](https://arxiv.org/abs/2106.12660) · [Upper Cones as Automorphism Bases](https://www.researchgate.net/publication/266363562_Upper_Cones_As_Automorphism_Bases)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-6685 — Busy Beaver \(\mathrm{BB}(6)\)

\(\mathrm{BB}(6)=S(6)\) is the maximum number of steps taken by a halting six-state binary Turing machine from the blank tape. The required answer supplies one complete transition table and Lean-checked proofs of its halting and universal runtime maximality. That proved-halting machine’s runtime names the exact integer without requiring a decimal expansion, closed form or execution trace. The five-state value is established, while six-state machines already exhibit enormous halting runtimes and unresolved arithmetic behavior. The September 2026 project pages still report the value as unknown; lower bounds, heuristics and a shrinking holdout list do not certify the requested maximum.

[Read in atlas](index.html#TCS-6685) · [Determination of the fifth Busy Beaver value](https://arxiv.org/abs/2509.12337v2) · [\(\mathrm{BB}(6)\)](https://wiki.bbchallenge.org/w/index.php?title=BB(6)&oldid=8519) · [Holdouts lists](https://wiki.bbchallenge.org/w/index.php?title=Holdouts_lists&oldid=8522) · [Antihydra](https://bbchallenge.org/antihydra) · [Story: Turing machines and the Busy Beaver function](https://bbchallenge.org/story)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6649 — Reversal of Hindman’s theorem to the \(\omega\)-jump

Hindman’s theorem finds an infinite set whose nonempty finite sums of distinct elements all have one color. This card asks whether that theorem forces every set’s complete sequence of finite Turing jumps over the weak base theory RCA0. The question concerns a formal implication between theories, not whether Hindman’s theorem is true in ordinary mathematics. A July 2026 result limits what one arithmetic coloring can force a solution to compute but explicitly leaves the full implication undecided. A complete Lean-checked proof must establish the stated formal derivation or its nonexistence, for example through a verified separating model.

[Read in atlas](index.html#TCS-6649) · [New bounds on the strength of some restrictions of Hindman’s Theorem](https://arxiv.org/abs/1701.06095v2) · [Hindman’s theorem does not code the omega-jump of the empty set in one application](https://arxiv.org/abs/2607.17666v1) · [The reverse mathematics of the Ordered Variable Word theorem](https://arxiv.org/abs/2606.12962v2) · [\(\Pi^0_4\) conservation of a Carlson-Simpson lemma for 1-variable words](https://arxiv.org/abs/2607.28116v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6679 — Universality of Turing equivalence

Turing equivalence groups all infinite binary sequences according to mutual oracle computability, without time or space restrictions. The question asks whether every Borel equivalence relation with countable classes can be encoded by Turing degrees using a Borel map. The encoding must preserve both equivalence and inequivalence for every input pair, but need not be computable, continuous or uniform on computation indices. The explicitly defined binary shift of the free group on two generators gives an equivalent single universal relation whose reducibility would settle the whole question. A complete Lean proof must establish or refute this exact universality statement; neighboring universality theorems and conditional Martin-conjecture or 2026 decomposition consequences do not suffice.

[Read in atlas](index.html#TCS-6679) · [The Fourteen Victoria Delfino Problems and Their Status in the Year 2019](https://preprint.math.uni-hamburg.de/public/papers/hbm/hbm770.pdf) · [The Theory of Countable Borel Equivalence Relations](https://www.pma.caltech.edu/documents/5921/CBER.pdf) · [Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://arxiv.org/abs/1109.1875) · [The universality of polynomial time Turing equivalence](https://arxiv.org/abs/1601.03343) · [Uniformity, Universality, and Computability Theory](https://arxiv.org/abs/1606.01976) · [On a question of Slaman and Steel](https://arxiv.org/abs/2004.00174) · [Erratum — Martin’s conjecture, arithmetic equivalence, and countable Borel equivalence relations](https://math.berkeley.edu/~marks/errata/mss_errata.html) · [Corrections to Uniformity, Universality, and Computability Theory](https://math.berkeley.edu/~marks/papers/322_fix.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7193 — Mortality of \(2\times 2\) integer matrix semigroups

A finite list of two-by-two integer matrices generates all nonempty products with arbitrary order and repetition. The question asks whether a terminating algorithm can decide if any such product is the zero matrix. Matrix entries and the number of generators are unrestricted. NP-hardness is known, while decidability results for restricted determinants do not cover the general case. Resolving the question would locate a basic computability boundary for products of small matrices.

[Read in atlas](index.html#TCS-7193) · [Mortality for \(2 \times  2\) Matrices is NP-hard](https://cgi.csc.liv.ac.uk/~igor/papers/paper_BHP_MFCS2012.pdf) · [On Affine Reachability Problems](https://arxiv.org/abs/1905.05114v3) · [The membership problem for subsemigroups of \(GL_{2}(\mathbb{Z} )\) is NP-complete](https://doi.org/10.1016/j.ic.2023.105132) · [On Word Representations and Embeddings in Complex Matrices](https://arxiv.org/abs/2604.15386v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6105 — Computability of the Mandelbrot set

The Mandelbrot set consists of complex parameters whose quadratic iteration starting at zero remains bounded. The question asks for one ordinary program that approximates the entire set to every requested accuracy. Its output must be a finite set of dyadic points with a proved Hausdorff error bound, and no running-time bound is imposed. Known positive results depend on a hyperbolicity conjecture, including the checked 2025 application to escape problems. The selected unconditional approximation question differs from exact real membership, computing area and producing images without certified error.

[Read in atlas](index.html#TCS-6105) · [Semicomputable Geometry](https://doi.org/10.4230/LIPIcs.ICALP.2018.129) · [Is the Mandelbrot set computable?](https://doi.org/10.1002/malq.200310124) · [Is the Mandelbrot set computable?](https://web.math.wisc.edu/logic/conf/OW21/questions/Hertling.pdf) · [Deciding Robust Instances of an Escape Problem for Dynamical Systems in Euclidean Space](https://doi.org/10.4230/LIPIcs.MFCS.2025.79)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2202 — NP-hardness of conditional polynomial-time pKt

Conditional probabilistic Kolmogorov complexity measures how short a program can be when it sees a conditional string and public random bits. The question asks for randomized NP-hardness even when decoding is allowed arbitrarily large polynomial time. The target is a promise decision problem with two success-probability thresholds, rather than an exact numerical evaluation. One reduction per error exponent must work across the time bounds through the permitted polynomial output-length padding. The known sublinear-time theorem and later conditional hardness statements do not establish this uniform polynomial-regime target.

[Read in atlas](index.html#TCS-2202) · [Impagliazzo’s Worlds Through the Lens of Conditional Kolmogorov Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2024.110) · [Impagliazzo’s Worlds Through the Lens of Conditional Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2024/085/) · [Kolmogorov’s Approach to P vs NP: Chain Rules for Time-Bounded Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2025/089/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5010 — Unconditional coding theorem for randomized Kolmogorov complexity

An efficient sampler assigns a probability to each string it can produce. The question asks whether every such string has a short randomized description close to its information content. One fixed description must reconstruct the string in polynomial time with probability at least two thirds using private random bits. The guarantee must cover the whole sampler support, while the encoder that finds a description may be inefficient. Known conditional, average-case and public-randomness coding results do not establish the stated unconditional theorem.

[Read in atlas](index.html#TCS-5010) · [Optimal Coding for Randomized Kolmogorov Complexity and Its Applications](https://doi.org/10.1109/FOCS61266.2024.00030) · [One-way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2025/202/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0250 — Scaling joint Kolmogorov-complexity profiles

Every tuple of strings has a profile of complexities of its nonempty subtuples. The question asks whether that whole profile can be multiplied by any fixed positive real factor. One new tuple must realize all the scaled quantities within logarithmic additive error. No fixed algorithm mapping the old tuple to the new one is required. The target concerns the homogeneous geometry of shared algorithmic information.

[Read in atlas](index.html#TCS-0250) · [SIGACT Open Problems Column](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Algebraic Barriers to Halving Algorithmic Information Quantities in Correlated Strings](https://doi.org/10.4230/LIPIcs.MFCS.2025.84)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0247 — Shannon feasibility from algorithmic network coding

Several correlated sources must be transmitted through a fixed directed acyclic network to designated recipients. Shannon coding chooses local encoding and decoding maps that work with high probability for random source blocks. Algorithmic coding instead allows each realized block to have its own short local programs and compatible edge messages. The question asks whether high-probability algorithmic feasibility with logarithmic overhead always implies Shannon feasibility at the same asymptotic rates. The target is this general converse, with vanishing error and rate slack defined explicitly, rather than a finite-block equivalence inferred from the title.

[Read in atlas](index.html#TCS-0247) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Multisource Algorithmic Information Theory](https://www.lirmm.fr/~ashen/multisource-dagstuhl.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4185 — Existence of strings without simple optimal hypotheses

The question asks whether some binary strings lack every simple probabilistic explanation satisfying a specified time-bounded likelihood comparison. For each polynomial sampling budget, a simple explanation must be sampled exactly by a logarithmically short randomized program that halts within that budget on every random choice. The selected target permits a larger polynomial time bound for describing the string and asks for strings without such explanations at infinitely many lengths. This is an explicit unconditional editorial formulation because the source did not fix the order of its polynomial time bounds. A complete Lean answer must prove the quantified existence statement or its full negation, clarifying how computational limits constrain statistical explanations of individual data.

[Read in atlas](index.html#TCS-4185) · [Stochasticity in Algorithmic Statistics for Polynomial Time](https://doi.org/10.4230/LIPIcs.CCC.2017.17) · [Stochasticity in Algorithmic Statistics for Polynomial Time](https://eccc.weizmann.ac.il/report/2017/043/) · [Stochasticity in Algorithmic Statistics for Polynomial Time: CCC 2017 presentation](https://computationalcomplexity.org/Archive/2017/slides/17_MV.pdf) · [Algorithmic Statistics and Prediction for Polynomial Time-Bounded Algorithms](https://doi.org/10.1007/978-3-319-94418-0_29) · [Prediction and MDL for infinite sequences](https://doi.org/10.1007/s00224-024-10180-0)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0287 — Strong extractors for infinite sequences

The question asks for one computable transformation of two independent infinite binary sequences of effective dimension one half. Its output must have effective dimension one even when either entire input is available as an oracle. Independence is the global oracle condition, which is stronger than comparing only finite input prefixes. The transformation may use unbounded computation but must produce every output bit on every promised input pair. Known ordinary extraction, finite-string strong extraction and finite-state impossibility results do not settle this stated target.

[Read in atlas](index.html#TCS-0287) · [Computability, Complexity and Randomness](https://doi.org/10.4230/DagRep.2.1.19) · [Algorithmically independent sequences](https://doi.org/10.1016/j.ic.2009.05.004) · [Two sources are better than one for increasing the Kolmogorov complexity of infinite sequences](https://arxiv.org/abs/0705.4658) · [Generating Kolmogorov random strings from sources with limited independence](https://doi.org/10.1093/logcom/exr053) · [Randomness Extraction Fails for Finite-State Dimension](https://doi.org/10.4230/LIPIcs.LICS.2026.78)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0238 — An algorithmic Ahlswede–Körner lemma

For individual binary strings x and y, side information z can shorten descriptions of either string and of their pair. The question asks whether another string \(z'\) can preserve those three conditional description lengths to logarithmic accuracy. The replacement must have a logarithmically short description when x and y are both given. It need not be easy to obtain from z, and no fast construction is required. The source establishes a special case for stochastic pairs, while the general question tests the scope of an algorithmic analogue of the Ahlswede–Körner lemma.

[Read in atlas](index.html#TCS-0238) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0254 — Algorithmic networks characterized by cut inequalities

A network distributes correlated finite strings through directed channels with limited capacities. Each cut imposes a necessary bound on the information that must enter its vertices to meet their demands. The question asks exactly which fixed network patterns make all of these bounds sufficient for a coding solution. Codes are existential per-instance assignments with logarithmic local descriptions, without an efficient uniform-encoder requirement. The source gives both positive examples and networks where the cut bounds fail, leaving the general structural characterization open.

[Read in atlas](index.html#TCS-0254) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Multisource Algorithmic Information Theory](https://doi.org/10.4230/DagSemProc.06051.9)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0240 — Communication rate for secret-key agreement at fixed Hamming distance

Alice and Bob hold binary strings at a specified Hamming distance and may communicate on a channel observed by an eavesdropper. The input pair must have nearly the largest Kolmogorov complexity possible in that distance layer, and its complexity profile is public. Using independent private randomness, they must agree on a key whose length is their mutual information up to logarithmic loss and which remains nearly incompressible given the transcript. The target is the smallest asymptotic worst-case number of communicated bits per input bit, as a function of relative distance. An answer must prove the whole rate function within absolute error 1/100 in Lean, with success guaranteed separately for every promised input pair.

[Read in atlas](index.html#TCS-0240) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Communication Complexity of the Secret Key Agreement in Algorithmic Information Theory](https://arxiv.org/abs/2004.13411v6) · [Common Information in Well-Mixing Graphs and Applications to Information-Theoretic Cryptography](https://arxiv.org/abs/2405.05831v3) · [Algebraic Barriers to Halving Algorithmic Information Quantities in Correlated Strings](https://doi.org/10.4230/LIPIcs.MFCS.2025.84)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0279 — Random-oracle invariance of fully extractable common information

Two words have fully extractable common information when a word containing almost all their mutual information has short descriptions from either one. The premise allows such an extraction for at least two thirds of independent infinite fair random oracles. The question is whether an extraction must then exist without any oracle, with losses still logarithmic in the input lengths. Oracle-dependent witnesses may vary and use arbitrarily many oracle positions, so finite auxiliary-word results do not directly supply the required bound. A complete Lean-checked proof or refutation must respect the uniform loss constants; a recent broader profile claim has not been verified to settle this statement.

[Read in atlas](index.html#TCS-0279) · [Extraction of mutual information about two strings, in Computability, Complexity and Randomness](https://doi.org/10.4230/DagRep.2.1.19) · [Stability of Properties of Kolmogorov Complexity under Relativization](https://www.lirmm.fr/~romashchen/ps/itp2010.pdf) · [27 Open Problems in Kolmogorov Complexity](https://www.cs.umd.edu/~gasarch/open/kolm.pdf) · [Extracting Common Information: Solutions to Q7, Q8, and Q9 of the 27 Open Problems](https://doi.org/10.2139/ssrn.7251558)
Existing status: `uncertain` · Summary written: 2026-09-17

## Proof complexity (26)

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

### TCS-7273 — Complete disjoint NP pairs

A disjoint NP pair consists of two nonoverlapping sets of binary strings, each with polynomially checkable certificates. The question asks whether one such pair can receive every other pair through a single total deterministic polynomial-time function. That function must map each source side to its corresponding target side, while its behavior outside the source promise is unrestricted apart from total polynomial time. Pudlák conjectures nonexistence and relates the question to the strength of propositional proof systems. The checked results through July 2026 include oracle separations but do not resolve the unrelativized existence target.

[Read in atlas](index.html#TCS-7273) · [Incompleteness in the finite domain](https://arxiv.org/abs/1601.01487v2) · [P-Optimal Proof Systems for Each NP-Set but no Complete Disjoint NP-Pairs Relative to an Oracle](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2019.47) · [Recursive Jump Operators and Optimal Proof Systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.88)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6759 — PSPACE-completeness of resolution clause space

Resolution clause space counts how many clauses must coexist while a contradiction is derived. The selected decision problem takes an arbitrary CNF formula and a binary space budget and asks whether any general resolution refutation fits that budget. Intermediate clauses may be reused and proof length is unrestricted. The problem is known to lie in PSPACE, while the established tree-like completeness result does not settle hardness for general resolution. A classification would explain the computational difficulty of predicting the intrinsic memory needed for proof search.

[Read in atlas](index.html#TCS-6759) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Game Characterizations and the PSPACE-Completeness of Tree Resolution Space](https://www.cs.toronto.edu/~ahertel/WebPageFiles/Papers/TCS%26PDGAME11.pdf) · [Proof Complexity and SAT Solving](https://doi.org/10.3233/FAIA200990) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6771 — Linear versus general resolution

General resolution refutes a Boolean CNF by combining and reusing clauses in an arbitrary acyclic proof. Linear resolution without restarts keeps one main chain, using the preceding clause together with an input clause or an earlier main clause at every inference. The question asks whether this restriction causes a superpolynomial increase in refutation length on some formulas, with length counted by resolution inferences. The source definition requires an explicit correction to exclude restarts, and the bounded later review found no verified resolution of the intended same-formula comparison. A complete Lean answer must prove either failure of every polynomial size bound or one universal polynomial simulation, without an extra requirement to find the converted proofs efficiently.

[Read in atlas](index.html#TCS-6771) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913v3) · [On Linear Resolution](https://www.ifi.lmu.de/institut/personen/jjohannsen/jj_papers/linres.pdf) · [The Complexity of Linear Resolution, in Proof Complexity (Dagstuhl Seminar 18051)](https://doi.org/10.4230/DagRep.8.1.124) · [A comment on the paper Linear and Negative Resolution are Weaker than Resolution](https://eccc.weizmann.ac.il/report/2001/074/comment/1/download/) · [Regular resolution effectively simulates resolution](https://arxiv.org/abs/2402.15871v1) · [Exponential Separation Between Powers of Regular and General Resolution over Parities](https://doi.org/10.4230/LIPIcs.CCC.2024.23)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1253 — Superpolynomial \(\mathrm{Res}(\oplus)\) lower bounds

Resolution over parities extends ordinary resolution by allowing disjunctions of linear equations modulo two. The question asks whether unsatisfiable CNF formulas can require more proof lines than every universal polynomial bound in their input size. Proofs may reuse earlier lines without any restriction on depth, width, regularity or space. Recent strong lower bounds for restricted proofs and the known unrestricted quadratic bound do not settle this question. A resolution would locate a central limitation, or unexpected strength, of propositional reasoning with parity.

[Read in atlas](index.html#TCS-1253) · [Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits](https://doi.org/10.4230/LIPIcs.ITCS.2026.111) · [Supercritical Tradeoff Between Size and Depth for Resolution over Parities](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.81) · [Lower Bounds for Regular Resolution over Parities](https://doi.org/10.1137/24M1696640) · [New Polynomial-Depth Res(+) Lower Bounds](https://eccc.weizmann.ac.il/report/2026/007/) · [Resolution Width Lifts to Near-Quadratic-Depth \(\mathrm{Res}(\oplus)\) Size](https://eccc.weizmann.ac.il/report/2026/018/) · [Strong ETH Holds for Bounded-Depth Resolution over Parities](https://doi.org/10.1145/3798129.3800804)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5333 — Linear-space Cutting Planes refutations

Cutting Planes refutes a Boolean CNF by deriving integer linear inequalities until it obtains a contradiction. Total space counts the binary digits of coefficients and right-hand constants stored simultaneously, with the source's convention that variable names and signs are not charged. The question is whether one constant times the number of variables always suffices, with no limit on proof length or coefficient magnitude. The source gives a quadratic universal upper bound, and the bounded later-source review found no resolution of the remaining linear-space question. An accepted answer must prove the universal linear bound or its fully quantified failure in Lean for the exact rules and space measure stated here.

[Read in atlas](index.html#TCS-5333) · [The Space Complexity of Cutting Planes Refutations](https://doi.org/10.4230/LIPIcs.CCC.2015.433) · [Proof Complexity and SAT Solving](https://jakobnordstrom.se/docs/publications/ProofComplexityChapter.pdf) · [How Limited Interaction Hinders Real Communication (and What It Means for Proof and Circuit Complexity)](https://eccc.weizmann.ac.il/report/2021/006/) · [Lifting with Simple Gadgets and Applications to Circuit and Proof Complexity](https://arxiv.org/abs/2001.02144v1) · [Truly Supercritical Trade-offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler-Leman](https://arxiv.org/abs/2411.14267v1) · [Average-Case Hardness of Binary-Encoded Clique in Proof and Communication Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2026.151)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7163 — Effective polynomial simulation of Extended Frege by Resolution

Resolution refutes inconsistent clauses, while Extended Frege permits named intermediate Boolean formulas. Ordinary proof-size comparisons keep the statement fixed and separate these systems. This question allows a polynomial-time transformation of the statement, given a unary bound on an EF proof’s length. Whenever that bound is sufficient, the transformed CNF must have a comparably short Resolution refutation, while correctness must be preserved for every input. An answer would clarify whether efficient preprocessing can overcome the proof-size gap between these systems.

[Read in atlas](index.html#TCS-7163) · [Effectively polynomial simulations](https://www.cs.toronto.edu/~toni/Papers/effsimulation.pdf) · [Regular resolution effectively simulates resolution](https://arxiv.org/abs/2402.15871)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6766 — Polynomial resolution length from logarithmic clause space

A resolution refutation certifies that no assignment satisfies a Boolean formula. Clause space counts how many clauses must be retained at once, and length counts how many clauses are downloaded or inferred. The question asks whether logarithmic minimum clause space always guarantees polynomial minimum length for formulas with bounded input-clause width. The short proof may use more memory than the small-space proof, so simultaneous time–space tradeoffs are a different question. Known results give polynomial length for constant space and quasipolynomial length for logarithmic space, leaving the requested improvement unresolved in the checked literature.

[Read in atlas](index.html#TCS-6766) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0024 — Frege lower bounds from circuit hardness

Some major lower-bound questions concern Boolean circuits, while others concern the size of propositional proofs. This card asks whether superpolynomial circuit hardness for an NP language forces superpolynomial Frege proof size. The premise allows fully nonuniform circuits, and the conclusion concerns ordinary unrestricted-depth Frege. A fixed complete proof calculus and explicit size conventions make both sides precise. Known connections for weaker systems, additional assumptions or different algebraic models do not settle this implication.

[Read in atlas](index.html#TCS-0024) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Towards P ≠ NP from Extended Frege Lower Bounds](https://eccc.weizmann.ac.il/report/2023/199/) · [Quasi-polynomial Frege Simulation of IPS beyond Noncommutativity](https://eccc.weizmann.ac.il/report/2026/166/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6768 — Simultaneous polynomial-length constant-space refutations

The question asks whether every fixed-width CNF family with constant-clause-space refutations also has refutations that are both polynomial-length and constant-clause-space. The same proof must meet both bounds, but its allowed constant space may exceed the original one. Space counts stored clauses regardless of their lengths, while proof length counts downloads and inferences. Known separate short-proof guarantees and results for constant total literal space do not provide the requested simultaneous clause-space bound. The later checked work still poses the question and proves only a polynomial lower bound for a restricted tree-like setting.

[Read in atlas](index.html#TCS-6768) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Space Characterizations of Complexity Measures and Size-Space Trade-Offs in Propositional Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.100) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6770 — Cutting Planes versus polynomial-coefficient Cutting Planes

Cutting Planes refutes Boolean formulas by deriving contradictions from integer linear inequalities. The question asks whether every such proof can be replaced by one whose length and coefficient magnitudes obey a single polynomial bound in input size plus original proof length. Proof lines may be reused and memory is unrestricted, so the target is an existential comparison of certificates rather than an efficient conversion algorithm. Known exponential-magnitude normalization and separations involving memory do not settle this polynomial-magnitude target. A resolution would clarify whether large numerical coefficients are an essential resource for short arithmetic proofs of Boolean inconsistency.

[Read in atlas](index.html#TCS-6770) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Proof Complexity and SAT Solving](https://doi.org/10.3233/FAIA200990) · [Cutting planes, connectivity, and threshold logic](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/cuttingplanes/paper.pdf) · [Lifting with Simple Gadgets and Applications to Circuit and Proof Complexity](https://eccc.weizmann.ac.il/report/2019/186/) · [Superpolynomial Length Lower Bounds for Tree-Like Semantic Proof Systems with Bounded Line Size](https://eccc.weizmann.ac.il/report/2026/078/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5114 — Lovász–Schrijver simulation of Cutting Planes

The question asks whether every Cutting Planes refutation has a polynomially longer Lovász–Schrijver refutation. Both systems start from the same real linear inequalities over Boolean variables. Length counts proof lines, with real coefficients unrestricted and earlier lines freely reusable. The reverse simulation is known to fail, and the failure of tree-like LS simulation does not settle the general DAG case. The user selected an existence theorem for short proofs, without requiring an efficient proof-conversion algorithm.

[Read in atlas](index.html#TCS-5114) · [Representations of Monotone Boolean Functions by Linear Programs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2017.3) · [Representations of Monotone Boolean Functions by Linear Programs](https://users.math.cas.cz/~pudlak/monotoneLP.pdf) · [Exponential Lower Bounds and Integrality Gaps for Tree-Like Lovász–Schrijver Procedures](https://www.cs.toronto.edu/~toni/Papers/matrix-cut.pdf) · [A Hereditary Property of Cutting Plane Procedures](https://arxiv.org/abs/2609.02038v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1099 — Separating levels of bounded arithmetic

The question asks whether two positive levels of Buss’s bounded-arithmetic hierarchy prove different sentences. Each level has the same basic arithmetic axioms but permits induction for a different class of bounded formulas. A solution may choose any two distinct positive levels and must prove an unconditional difference in their deductive strength. The full axiom list, formula grammar and induction scheme specify the theories without relying on an unstated standard model. Recent conditional separations do not provide the unconditional nonprovability witness required here.

[Read in atlas](index.html#TCS-1099) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416) · [Bounded Arithmetic, Propositional Logic, and Complexity Theory](https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf) · [Parallelism and Adaptivity in Student-Teacher Witnessing](https://arxiv.org/abs/2602.19934)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1096 — Unprovability of polynomial circuit upper bounds in \(S_2^1\)

For each fixed polynomial exponent, the question asks for a polynomial-time predicate whose corresponding circuit upper bounds cannot be proved in S-two-one. The same predicate must resist every fixed multiplicative coefficient in that exponent. Its function representation, the arithmetic theory, circuit encoding and length quantifiers are explicitly specified. The conclusion is nonprovability of upper bounds, not an asserted standard-model circuit lower bound. Recent weaker-theory results and EXP consistency results leave this particular target open in the checked sources.

[Read in atlas](index.html#TCS-1096) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416) · [Bounded Arithmetic, Propositional Logic, and Complexity Theory](https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf) · [Parallelism and Adaptivity in Student-Teacher Witnessing](https://arxiv.org/abs/2602.19934) · [From Gödel incompleteness to the consistency of circuit lower bounds](https://arxiv.org/abs/2604.25251)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1097 — Unprovability of NP circuit upper bounds in \(T_2^1\)

For each fixed polynomial exponent, the question asks for an NP predicate whose circuit upper bounds cannot be proved in T-two-one. One represented predicate must resist every fixed multiplicative coefficient at that exponent. The theory uses successor induction for NP formulas, and the card fixes its axioms and the precise circuit upper-bound sentence. Known results concern NP in a weaker theory or a larger complexity class in T-two-one. A resolution would clarify limits on formal proofs about efficient nonuniform computation without itself asserting a standard-model circuit lower bound.

[Read in atlas](index.html#TCS-1097) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416) · [Bounded Arithmetic, Propositional Logic, and Complexity Theory](https://www.karlin.mff.cuni.cz/~krajicek/kniha.pdf) · [Consistency of circuit lower bounds with bounded theories](https://lmcs.episciences.org/6576) · [LEARN-Uniform Circuit Lower Bounds and Provability in Bounded Arithmetic](https://eccc.weizmann.ac.il/report/2021/095/) · [Parallelism and Adaptivity in Student-Teacher Witnessing](https://arxiv.org/abs/2602.19934)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1098 — \(PV_1\) nonprovability of polynomial-time SAT solvers

A polynomial-time SAT search algorithm would return a satisfying assignment whenever one exists. The question asks whether the theory PV1 fails to prove correctness for every such polynomial-time function symbol. This is a statement about finite formal proofs, with the theory and formula encoding specified explicitly. It can hold even if a polynomial-time solver exists but its correctness has no proof in this particular theory. The benchmark requires a complete Lean proof of the nonprovability schema or a verified counterexample consisting of a symbol and a finite correctness proof.

[Read in atlas](index.html#TCS-1098) · [Meta-Mathematics of Computational Complexity Theory](https://arxiv.org/abs/2504.04416v1) · [The strength of sharply bounded induction](https://www.math.cas.cz/~jerabek/papers/t02.pdf) · [A Theory for Probabilistic Polynomial-Time Reasoning](https://arxiv.org/abs/2602.09302v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6767 — Sharp resolution length bounds at fixed width

Resolution width is the largest clause used in a refutation, and length counts its clause lines. The question asks for linear-size 3-CNF families whose narrow refutations coexist with an almost full-width exponent lower bound on every refutation length. One absolute exponent loss must work for all sufficiently large fixed widths, while family constants may depend on width. Known exponential dependence on width and newer restricted-proof tradeoffs do not by themselves give this sharper unrestricted lower bound. A resolution would sharpen the fundamental cost of narrow reasoning in propositional proof search.

[Read in atlas](index.html#TCS-6767) · [Pebble Games, Proof Complexity, and Time-Space Trade-offs](https://arxiv.org/abs/1307.3913) · [Narrow Proofs May Be Maximally Long](https://jakobnordstrom.se/docs/publications/LargeNarrowProofs_ToCL.pdf) · [A Tradeoff Between Length and Width in Resolution](https://www.theoryofcomputing.org/articles/v012a005/) · [Supercritical Size-Width Tree-Like Resolution Trade-Offs for Graph Isomorphism](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.18) · [Truly Supercritical Trade-Offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler–Leman](https://jakobnordstrom.se/docs/publications/TrulySupercriticalTrade-offs_STOC.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0071 — \(\mathrm{NC}^{0}\) proof systems for directed reachability

The target language consists of directed adjacency matrices with a path from vertex one to the last vertex. An NC⁰ proof system must generate exactly these matrices from arbitrary input bit strings. Each output edge depends on only constantly many proof bits, with one constant depth bound for all graph sizes. Such generators are known for undirected reachability and for directed unreachability. The selected directed-reachability existence question remains unresolved in the sources checked by this review.

[Read in atlas](index.html#TCS-0071) · [Circuits, Logic and Games: Proof systems computed by NC⁰ circuit families](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.5.9.105) · [Small Depth Proof Systems](https://people.iith.ac.in/karteek/assets/pdf/SmallDepthProofSystems.pdf) · [Small Depth Proof Systems](https://eccc.weizmann.ac.il/report/2013/102/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2889 — Short tree-like resolution from small proof space

The source compares working memory in refutations with the logarithm of minimum tree-like resolution size. Its two memory measures are stored clauses in resolution and distinct monomials in polynomial calculus with resolution. The comparison allows polynomial losses and powers of log n, so it is much coarser than a constant-factor identity. A length-penalized version of space is already known to satisfy the comparison. The unresolved issue is whether ordinary space can be substantially smaller on this scale.

[Read in atlas](index.html#TCS-2889) · [Space Characterizations of Complexity Measures and Size-Space Trade-Offs in Propositional Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.100) · [Space characterizations of complexity measures and size-space trade-offs in propositional proof systems](https://doi.org/10.1016/j.jcss.2023.04.006)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-4982 — Does uniform randomized circuit learning imply P equals NP?

The premise asks for one efficient learner for all Boolean circuits when it may make membership queries. Accuracy is measured on uniformly random Boolean inputs, and the output may be any suitably small Boolean circuit. The learner is uniform and randomized, with explicit polynomial dependence on target size, error and confidence. The chosen conclusion is the deterministic class equality P equals NP. This fixes the uniformity choices in the source’s broader converse question without treating randomized or nonuniform conclusions as equivalent.

[Read in atlas](index.html#TCS-4982) · [Learning Algorithms Versus Automatability of Frege Systems](https://doi.org/10.4230/LIPIcs.ICALP.2022.101) · [Learning algorithms versus automatability of Frege systems — full author version](https://arxiv.org/abs/2111.10626) · [On Basing Lower-Bounds for Learning on Worst-Case Assumptions](https://www.wisdom.weizmann.ac.il/~bennyap/pubs/ABX08Full.pdf) · [Pseudorandomness and the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.ITCS.2020.68) · [Witness Encryption and NP-Hardness of Learning](https://doi.org/10.4230/LIPIcs.CCC.2025.34) · [Learning algorithms versus automatability of Frege systems — journal version](https://doi.org/10.1142/S0219061325500023)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5292 — Optimal proof systems outside NP

The question asks whether any language outside NP has an optimal proof system. Each system is a polynomial-time algorithm that maps proofs to exactly the statements in its language. Optimality means that every competing system’s proofs can be matched with at most polynomial growth in length. A fast algorithm for translating proofs is a separate, stronger requirement. Recent oracle barriers and jump-operator results do not decide the ordinary existence question.

[Read in atlas](index.html#TCS-5292) · [Recursive Jump Operators and Optimal Proof Systems](https://doi.org/10.4230/LIPIcs.ICALP.2026.88) · [Optimal Proof Systems for Complex Sets Are Hard to Find](https://doi.org/10.1145/3717823.3718182) · [Recursive Jump Operators and Optimal Proof Systems — full version](https://arxiv.org/abs/2606.01242)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5332 — Weak automatability of Resolution

The input is a CNF formula and a proof-length budget written in unary. The algorithm must distinguish satisfiable formulas from those having a short general Resolution refutation. The proof is not supplied, and the algorithm need not produce a Resolution proof. Unsatisfiable formulas whose shortest refutations exceed the budget can receive either answer. Known hardness for finding Resolution proofs does not settle this weaker recognition problem.

[Read in atlas](index.html#TCS-5332) · [Proof Complexity and Its Relations to SAT Solving (Invited Talk)](https://doi.org/10.4230/LIPIcs.STACS.2025.1) · [Regular resolution effectively simulates resolution](https://doi.org/10.1016/j.ipl.2024.106489) · [Automating Resolution is NP-Hard](https://arxiv.org/abs/1904.02991) · [The Proof Analysis Problem](https://arxiv.org/abs/2506.16956)
Existing status: `open` · Summary written: 2026-09-12

## Communication complexity and Boolean function analysis (28)

### TCS-6603 — Log-rank conjecture

Alice and Bob must exactly evaluate a total Boolean function while each receives only one part of its input. The conjecture asks whether their minimum worst-case deterministic communication is bounded by one universal polynomial in logarithmic real matrix rank. The protocol may use arbitrary interaction and local computation, but all input pairs must be handled correctly. A refutation must defeat every universal polynomial, rather than a single proposed constant or exponent. Known square-root-rank upper bounds, nearly quadratic logarithmic lower bounds and signed-partition equivalences leave the central gap unresolved.

[Read in atlas](index.html#TCS-6603) · [The Log-Rank Conjecture: New Equivalent Formulations](https://arxiv.org/abs/2510.02583v3) · [Matrix discrepancy and the log-rank conjecture](https://doi.org/10.1007/s10107-024-02117-9) · [Deterministic Communication vs. Partition Number](https://doi.org/10.1137/16M1059369) · [Alphabet-Preserving Lifting for the Log-Rank Conjecture](https://arxiv.org/abs/2608.01812v1) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6604 — Fourier Entropy–Influence conjecture

A scalar Boolean function has a Fourier spectrum whose squared coefficients form a probability distribution on sets of input coordinates. The Fourier Entropy–Influence conjecture asks whether its Shannon entropy is at most a universal constant times the expected size of a spectral set. Every dimension and every Boolean function are included, with uniform inputs, base-two entropy and exactly normalized bit-flip influence. A complete Lean-checked answer must prove the universal bound or show that the ratio is unbounded over nonconstant Boolean functions. The conjecture would imply fixed-accuracy Fourier concentration for DNF formulas, while weaker coordinate-entropy estimates and quantum counterexamples leave its classical target unsettled.

[Read in atlas](index.html#TCS-6604) · [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.cs.cmu.edu/~jswright/papers/fei.pdf) · [A new bound for the Fourier-Entropy-Influence conjecture](https://arxiv.org/abs/2312.08271) · [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246) · [Dense Hamiltonians at the Parseval Limit: The Noncommutative BH Constant is Exponential and the Quantum FEI Conjecture is False](https://arxiv.org/abs/2608.01424) · [A Note on the Entropy/Influence Conjecture](https://arxiv.org/abs/1105.2651) · [Strengthening Han’s Fourier Entropy-Influence Inequality via an Information-Theoretic Proof](https://arxiv.org/abs/2512.03117) · [Tightness of and counterexamples to several quantum estimates](https://arxiv.org/abs/2608.04411)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6605 — Aaronson–Ambainis conjecture

The Aaronson–Ambainis conjecture concerns real multilinear polynomials whose values lie between zero and one on every point of the Boolean cube. It asks for a variable whose mean squared influence is bounded below by a fixed power of variance divided by degree, independent of the number of variables. The universal claim includes arbitrary real coefficients and arbitrarily small positive variance, with one normalization and one exponent throughout. A complete Lean proof must establish that claim or provide violations for every proposed exponent, rather than only a particular numerical power. The conjecture would imply almost-everywhere classical query simulation, while known random-restriction, bounded-round and completely bounded results leave its full scalar form unresolved.

[Read in atlas](index.html#TCS-6605) · [The Need for Structure in Quantum Speedups](https://arxiv.org/abs/0911.0996) · [Quantum speedups need structure — withdrawn](https://arxiv.org/abs/1911.03748) · [Influence in Completely Bounded Block-Multilinear Forms and Classical Simulation of Quantum Algorithms](https://ir.cwi.nl/pub/31883/31883.pdf) · [Random Restrictions of Bounded Low Degree Polynomials Are Juntas](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17) · [Aaronson-Ambainis Conjecture Is True For Random Restrictions](https://eccc.weizmann.ac.il/report/2024/035/) · [Quantum Speedups Require Structure or Depth](https://arxiv.org/abs/2608.19158) · [Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms](https://arxiv.org/abs/2609.05201)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6581 — Mansour’s conjecture

A short DNF describes a Boolean function using a small number of conjunctions. Mansour’s conjecture asks whether such a function can always be approximated by retaining only a small number of its ordinary Fourier coefficients. The permitted discarded squared mass is epsilon under uniformly random Boolean inputs. The retained number must be at most the term count raised to a universal constant times log of inverse epsilon, with no dependence on the ambient dimension. A complete Lean-checked answer must prove or refute this strong bound for all DNFs and all stated accuracies, without an algorithmic recovery requirement.

[Read in atlas](index.html#TCS-6581) · [The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions](https://www.cs.cmu.edu/~jswright/papers/fei.pdf) · [Mansour’s Conjecture is True for Random DNF Formulas](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/) · [Sharper bounds on the Fourier concentration of DNFs](https://arxiv.org/abs/2109.04525v2) · [Further evidence towards the Fourier Entropy-Influence conjecture](https://arxiv.org/abs/2606.00246v2) · [Learning DNF through Generalized Fourier Representations](https://arxiv.org/abs/2506.01075v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6664 — Maximum influence of polynomial threshold functions

A polynomial threshold function records the sign of a real polynomial on the uniformly distributed Boolean cube. Total influence is the expected number of individual coordinate flips that change the function’s value. The target is the largest influence possible as a joint function of dimension and degree bound, within constants independent of both parameters. A complete Lean proof must give a matching universal upper bound and a lower example for every parameter pair, including the regime where influence is of order the dimension. The disproved exact symmetric-extremizer conjecture, fixed-degree logarithmic bounds and the separate 2026 surface-area and rational-degree theorems do not determine this joint growth.

[Read in atlas](index.html#TCS-6664) · [The Gotsman–Linial Conjecture is False](https://arxiv.org/abs/2108.02288) · [A Dual Perspective on Computational Complexity](https://dspace.mit.edu/server/api/core/bitstreams/7f2e32fd-d615-4dba-97be-f26cd30ca234/content) · [The Correct Exponent for the Gotsman–Linial Conjecture](https://arxiv.org/abs/1210.1283) · [On Graphs and the Gotsman–Linial Conjecture for \(d = 2\)](https://arxiv.org/abs/1709.06650) · [The Boolean surface area of polynomial threshold functions](https://arxiv.org/abs/2604.08095) · [Rational degree is polynomially related to degree](https://arxiv.org/abs/2601.08727)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7219 — Aanderaa–Karp–Rosenberg conjecture

An algorithm learns an unknown graph by asking whether individual pairs of vertices are edges. The conjecture asks whether every nonconstant monotone property invariant under vertex relabeling has some input requiring all possible pairs to be queried. Queries may be adaptive and all computation between them is free. The example of looking for one edge illustrates how an easy positive instance can coexist with an empty graph that requires a complete scan. The exact claim is known for prime-power vertex counts, while results about quantum queries, infinite graphs and broader topological symmetry must be distinguished from the full finite deterministic question.

[Read in atlas](index.html#TCS-7219) · [A topological approach to evasiveness](https://doi.org/10.1007/BF02579140) · [Elusive properties of countably infinite graphs](https://arxiv.org/abs/2503.11798v3) · [Degree vs. Approximate Degree and Quantum Implications of Huang’s Sensitivity Theorem](https://arxiv.org/abs/2010.12629v1) · [The topological evasiveness conjecture — CATA IV talk abstract](https://indico.sns.it/event/134/timetable/?print=1&view=standard_numbered) · [Publications — On the Topological Evasiveness Conjecture](https://www.math.miami.edu/~bruno/publications.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-5326 — Interactive compression with logarithmic input-length overhead

The underlying question concerns two-party interactive communication, even though its source article studies multiparty protocols. A protocol can transmit many more bits than its internal information cost under the input distribution. The proposed precise target allows a logarithmic factor in input bit length and a fixed total-variation error when both parties reconstruct the transcript. Exact compression without loss is already known to fail, while results for external information or independent inputs address different targets. A complete Lean answer must prove this explicitly specified universal simulation bound or a lower bound refuting every proposed universal constant.

[Read in atlas](index.html#TCS-5326) · [Multi-Party Protocols, Information Complexity and Privacy](https://doi.org/10.4230/LIPIcs.MFCS.2016.57) · [Multi-Party Protocols, Information Complexity and Privacy](https://www.irif.fr/~adiro/publ/KRU.pdf) · [Information Complexity and the Quest for Interactive Compression](https://eccc.weizmann.ac.il/report/2015/060/) · [Simplified Separation of Information and Communication](https://eccc.weizmann.ac.il/report/2015/057/) · [Interactive Compression to External Information](https://par.nsf.gov/servlets/purl/10084450) · [Exponential Separation of Communication and External Information](https://eccc.weizmann.ac.il/report/2015/088/) · [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141v1)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6450 — Polynomial relation between classical and quantum communication

Two parties must evaluate a Boolean function when each holds one part of the input. The question asks whether randomized classical communication is polynomially bounded by quantum communication with shared entanglement for every total function. Both models allow bounded error on each input, and their costs count transmitted bits or qubits rather than local computation. August and September 2026 preprints claim total-function families with polylogarithmic quantum cost and polynomial randomized classical cost. Those stated results would refute the conjecture even with the quantum side allowed free entanglement, but their proofs are not independently certified in this review.

[Read in atlas](index.html#TCS-6450) · [Quantum–Classical Equivalence for AND-Functions](https://eccc.weizmann.ac.il/report/2026/013/) · [Constant-round quantum advantage in communication complexity for total functions](https://arxiv.org/abs/2608.19787v1) · [On the quantum communication complexity of total functions](https://arxiv.org/abs/2608.18784) · [Improved Separations between Quantum and Classical Communication Complexity of Total Functions](https://arxiv.org/abs/2609.16726)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6708 — Fourier Min-Entropy–Influence conjecture

The FMEI conjecture says that every Boolean function has a parity whose squared Fourier correlation is exponentially large in minus its total influence. Both influence and Fourier coefficients use the uniform distribution on the Boolean cube. One universal constant must cover every dimension and truth table, including constant and unbalanced functions. The conjecture is weaker than full Fourier entropy–influence and remains meaningful because of its connection to fundamental influence inequalities. Recent constructions force the universal constant to be at least four, while leaving the existence of any finite constant unresolved.

[Read in atlas](index.html#TCS-6708) · [Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386) · [Improved bounds on Fourier entropy and Min-entropy](https://eccc.weizmann.ac.il/report/2018/167/revision/1/download/) · [Improved Bounds on Fourier Entropy and Min-entropy](https://www.isical.ac.in/~sourav/papers/TOCT21.pdf) · [A Lower Bound on the Constant in the Fourier Min-Entropy/Influence Conjecture](https://eccc.weizmann.ac.il/report/2022/180/revision/1/download) · [A note on the FMEI of the Boolean functions in the Generalized Maiorana-McFarland construction](https://doi.org/10.1016/j.dam.2026.02.052) · [A New Bound for the Fourier-Entropy-Influence Conjecture](https://link.springer.com/article/10.1007/s00493-024-00133-z)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6710 — Number-on-forehead disjointness complexity

Each of k players sees all input sets except the one assigned to that player. The goal is to decide whether the intersection of all sets is empty using public randomized communication. The card asks for matching bounds in both universe size and player count, with absolute constant factors. Protocols may interact arbitrarily, and their cost is the maximum total number of broadcast bits. The regime with at least logarithmically many players is understood, but it does not determine the answer for all smaller player counts.

[Read in atlas](index.html#TCS-6710) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf) · [Boolean Function Complexity: Advances and Frontiers (author's early draft)](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Communication Lower Bounds Using Directional Derivatives](https://eccc.weizmann.ac.il/report/2013/005/) · [Inner Product and Set Disjointness: Beyond Logarithmically Many Parties](https://web.cs.ucla.edu/~sherstov/pdf/ip-disj-beyond-logn.pdf) · [Deterministic Lifting Theorems for One-Way Number-on-Forehead Communication](https://eccc.weizmann.ac.il/report/2025/073/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5272 — Multiparty Clique lower bounds in compression games

Alice sees a graph and a requested clique size, but her computation is limited to polynomial-size constant-depth Boolean circuits. She can exchange messages with polynomially many unrestricted helpers, each of whom sees only its own conversation. Alice must compute the correct final answer on every input. Communication cost sums the longest message from Alice in each round, and the question asks for a polynomial lower bound even under a growing round budget. The source shows that such a Clique lower bound would separate NP from nonuniform logarithmic-depth circuits.

[Read in atlas](index.html#TCS-5272) · [Majority is Incompressible by \(\mathrm{AC}^{0}(p)\) Circuits](https://doi.org/10.4230/LIPIcs.CCC.2015.124)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6707 — Zero-error query complexity of recursive majority-of-three

Recursive majority-of-three evaluates a complete ternary tree whose internal nodes take majority votes. An algorithm may adaptively inspect leaf bits in any order, but it must always return the exact root value. The cost is its largest expected number of queries over all possible inputs. The task is to determine that optimum as the tree grows, with upper and lower bounds matching up to constant factors. Known lower and upper exponential rates remain different, and a 2026 equality between composition limits does not determine the optimum.

[Read in atlas](index.html#TCS-6707) · [Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386) · [Improved bounds for the randomized decision tree complexity of recursive majority](https://doi.org/10.1002/rsa.20598) · [A Composition Theorem for Conical Juntas](https://doi.org/10.4230/LIPIcs.CCC.2016.5) · [Monte Carlo to Las Vegas for Recursively Composed Functions](https://arxiv.org/abs/2601.08073v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6705 — Sharp low-degree Fourier weight of halfspaces

A halfspace is the sign of a weighted sum of input bits and a threshold. Its degree-zero and degree-one Fourier coefficients measure its mean and coordinate correlations. The question asks whether their squared weight is always at least \(2/\pi\). Majority functions approach that proposed universal constant as dimension grows. The exact inequality is retained because a general algorithm for merely approximating the extremal constant is already known.

[Read in atlas](index.html#TCS-6705) · [Analysis of Boolean Functions (updated author edition)](https://arxiv.org/abs/2105.10386) · [A robust Khintchine inequality, and algorithms for computing optimal constants in Fourier analysis and high-dimensional geometry](https://arxiv.org/abs/1207.2229) · [A Two-regime Khintchine Inequality and an Improved Bound on the Degree-1 Fourier Weight for Linear Threshold Functions](https://arxiv.org/abs/2608.27908)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-2664 — Removing low-influence directions from convex sets

The problem concerns symmetric convex sets under standard Gaussian measure. A specified direction has small convex influence, measured by a normalized second-moment statistic. The conjecture asks whether the set is close to a symmetric convex cylinder that ignores this direction. The approximation error must tend to zero with influence independently of dimension. The exact zero-influence case is known, while the robust dimension-free statement remains the source’s Conjecture 2.

[Read in atlas](index.html#TCS-2664) · [Convex Influences](https://doi.org/10.4230/LIPIcs.ITCS.2022.53) · [Convex Influences — full version](https://arxiv.org/abs/2109.03107)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6711 — Deterministic communication versus monochromatic partition size

Alice and Bob must compute a Boolean function of their separate inputs by exchanging bits. A monochromatic partition divides its entire communication matrix into disjoint rectangles on which the output is constant. The question asks for the greatest possible deterministic communication cost when the logarithm of that partition size is at most t. A quadratic upper bound and nearly quadratic separations determine the optimal exponent, but do not by themselves settle all nonconstant factors. This card asks for upper and lower bounds on the full worst-case rate that match up to multiplicative constants.

[Read in atlas](index.html#TCS-6711) · [Communication Complexity (early author draft)](https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf) · [Nearly Optimal Separations Between Communication (or Query) Complexity and Partitions](https://doi.org/10.4230/LIPIcs.CCC.2016.4)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1845 — Optimal time exponent for truth-table decision-tree depth

Given the complete truth table of a Boolean function, the task is to compute the minimum worst-case depth of a decision tree evaluating it. The known sequential upper bound is polynomial in the table length but has an exponent larger than one. This card asks for the infimum deterministic time exponent in a fixed finite-word random-access model, allowing different uniform algorithms for different candidate exponents. That exponent separates the cost of optimizing query depth from the query depth itself and from parallel complexity. An accepted answer must give a real approximation within 1/100 and a complete Lean proof, without assuming that an algorithm attains the infimum.

[Read in atlas](index.html#TCS-1845) · [The Hardness of Decision Tree Complexity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2025.66) · [The hardness of decision tree complexity](https://eccc.weizmann.ac.il/report/2024/034/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4771 — Two-sided versus one-sided randomized communication

Two parties want to compute a total Boolean function using little communication. The question asks whether every efficient two-sided randomized protocol can be replaced by deterministic adaptive queries to one-sided randomized tests. Oracle answers are exact, and each query is charged the communication needed by its one-sided-error protocol. The total communication and query cost may grow polynomially in the logarithm of the input length. Known constant-query hierarchy separations and partial-function results do not resolve this total-function equality.

[Read in atlas](index.html#TCS-4771) · [Nondeterministic and Randomized Boolean Hierarchies in Communication Complexity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.92) · [Pseudodeterminism and \(\mathrm{MA}\ne\mathrm{NP}^{\mathrm{BPP}}\) in Communication Complexity](https://arxiv.org/abs/2608.26425v1) · [Constant-Cost Communication is not Reducible to k-Hamming Distance](https://arxiv.org/abs/2407.20204v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-2571 — A randomized-communication characterization of ordinary KW games

An ordinary Karchmer–Wigderson game asks two parties to find a coordinate where their differently classified Boolean inputs disagree. The selected candidate says these games capture exactly total search tasks with cheap answer verification and cheap randomized communication. Capture means deterministic mapping reductions in both directions, with polylogarithmic communication and at most quasipolynomially many target coordinates. Ordinary games have cheap randomized protocols, whereas the known monotone representation theorem covers a broader class of total search tasks. The exact equivalence is a user-selected editorial candidate whose current status remains uncertain, not a conjecture quoted from the source.

[Read in atlas](index.html#TCS-2571) · [TFNP Characterizations of Proof Systems and Monotone Circuits](https://doi.org/10.4230/LIPIcs.ITCS.2023.30) · [On Communication Complexity of Fixed Point Computation](https://arxiv.org/abs/1909.10958v3)
Existing status: `uncertain` · Summary written: 2026-09-18

### TCS-1047 — Formula size versus partition complexity

A De Morgan formula computes a Boolean function with an expression tree whose leaves are literals. Its partition measure counts disjoint rectangles pairing accepting and rejecting inputs, each certified by one differing coordinate. The question asks whether formula leaf size is always bounded by a fixed polynomial in that rectangle count. The partition need not already be organized as a recursive communication protocol, which is the source of the possible gap. Jukna’s author draft dated 14 September 2026 still lists the polynomial inverse as open and gives only a quasipolynomial general bound.

[Read in atlas](index.html#TCS-1047) · [Boolean Function Complexity: Advances and Frontiers — early author draft](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Boolean Function Complexity: Advances and Frontiers — Second Expanded Edition, author draft](https://web.vu.lt/mif/s.jukna/boolean-2nd/BFC-new.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1059 — Linearization conjecture for depth-two circuits

A depth-two Boolean circuit computes a linear transformation using shared middle-layer gates and direct input wires. The question asks whether all its gates can be made linear with only constant-factor increases in width and direct-input degree. Middle-layer gates may initially compute arbitrary Boolean functions, and every input vector must be handled exactly. The linear conclusion is equivalent to decomposing the matrix into a low-rank part and a part sparse in each row. The target is existence of such circuits, without a requirement to find the conversion efficiently.

[Read in atlas](index.html#TCS-1059) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Block Rigidity: Strong Multiplayer Parallel Repetition implies Super-Linear Lower Bounds for Turing Machines](https://eccc.weizmann.ac.il/report/2020/173/) · [Efficient Linearization Implies the Multiphase Conjecture](https://eccc.weizmann.ac.il/report/2022/122/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5189 — PSPACE-hardness of a factor-two gap in decision-tree depth

Given a Boolean circuit, decision-tree depth is the fewest input-bit queries needed in the worst case to compute its function exactly. The question asks whether distinguishing depth at most k from depth greater than 2k remains PSPACE-hard. The function is supplied by a circuit, whose binary description is the input-size measure. Exact computation and constant additive approximation are already hard in the cited source, while a multiplicative gap needs a stronger result. The card fixes a factor-two many-one promise and keeps this distinct from truth-table algorithms and tree-size minimization.

[Read in atlas](index.html#TCS-5189) · [The Hardness of Decision Tree Complexity](https://doi.org/10.4230/LIPIcs.STACS.2025.66)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0540 — Near-linear communication for exact maximum flow with local outputs

Alice and Bob hold disjoint parts of a directed graph and want an exact maximum flow between public terminals. For every fixed polynomial bound on integer capacities, the target is a protocol using n times a fixed power of log n communicated bits. Each party outputs the flow only on its own edges, using free local computation and storage, with joint success probability at least two thirds. The bit bound is worst-case over inputs and randomness, while the number of interactive rounds is unrestricted. The checked recent protocols use roughly n to the three-halves power bits; a complete Lean-checked near-linear protocol or refutation is required.

[Read in atlas](index.html#TCS-0540) · [Communication Complexity of Max-Flow, in Dynamic Graph Algorithms](https://doi.org/10.4230/DagRep.12.11.45) · [A Subquadratic Two-Party Communication Protocol for Minimum Cost Flow](https://arxiv.org/abs/2510.03427v1) · [Computing Flows in Subquadratic Space](https://doi.org/10.4230/LIPIcs.ICALP.2026.46)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0218 — Optimal one-bit cryptogenography success for every number of players

One uniformly chosen player knows a uniformly random secret bit and the group can communicate only in public. The players succeed when their public output is correct and an optimal observer accuses someone other than the original owner. The target is the best achievable success probability as a function of every number of players from two onward. Private randomness and arbitrarily long finite interaction are allowed, without computational secrecy or a private channel. A complete Lean-checked approximation within one hundredth is required at every player count, even though existing bounds already meet that precision for two players alone.

[Read in atlas](index.html#TCS-0218) · [Problem 79: Cryptogenography](https://sublinear.info/79) · [Cryptogenography](https://doi.org/10.1145/2554797.2554800) · [Improved Protocols and Hardness Results for the Two-Player Cryptogenography Problem](https://doi.org/10.4230/LIPIcs.ICALP.2016.150) · [Searching for Cryptogenography Upper Bounds via Sum of Square Programming](https://doi.org/10.4230/LIPIcs.ISAAC.2019.31)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0811 — Large zero rectangles in low-rank real matrices

The question concerns square real matrices with low rank and at least half their entries equal to zero. It asks for a Cartesian block consisting entirely of zeros whose area is a square-root-exponential fraction of the whole matrix. The constant in that guarantee must be the same for every matrix and dimension. The rank is over the real numbers, and entries may have arbitrary signs and magnitudes. Recent results establish related guarantees under additional entry restrictions, while the checked sources retain the general real-matrix question.

[Read in atlas](index.html#TCS-0811) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40) · [Disjoint pairs in set systems and combinatorics of low rank matrices](https://arxiv.org/abs/2411.13510v1) · [Extremal Combinatorics, Oberwolfach Report 42/2025](https://ems.press/content/serial-article-files/52246)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1061 — Quadratic decision-tree bounds from block sensitivity

The target is a universal quadratic upper bound on deterministic decision-tree depth in terms of block sensitivity. A decision tree adaptively reads individual bits and must compute a total Boolean function correctly on every input. Block sensitivity counts disjoint blocks whose separate flips all change the value at one common input. The known general bound is cubic, while quadratic bounds hold for several restricted classes. The proposed constant must work for every function and dimension, and recent results on tree size or counts of minimal blocks do not settle this depth question.

[Read in atlas](index.html#TCS-1061) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Decision Tree Complexity Versus Block Sensitivity and Degree](https://doi.org/10.4230/LIPIcs.FSTTCS.2023.27) · [Nearly Tight Bounds on the Block Number of Boolean Functions in Terms of Sensitivity](https://eccc.weizmann.ac.il/report/2026/010/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-2658 — Sign-rank bounds from constant margin

A sign matrix can be represented by points and separating hyperplanes. Its margin measures how far every point stays from every relevant hyperplane after normalization. Its sign-rank is the smallest dimension of any representation with the correct signs. The question asks whether a fixed positive margin forces a dimension bound independent of matrix size. Recent work disproves a proposed Hamming-distance counterexample but explicitly leaves the general question open.

[Read in atlas](index.html#TCS-2658) · [Lower Bound Methods for Sign-Rank and Their Limitations](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2022.22) · [Sign-Rank of k-Hamming Distance is Constant](https://eccc.weizmann.ac.il/report/2025/060/) · [A \(Z_{2}\)–Topological Framework for Sign-rank Lower Bounds](https://eccc.weizmann.ac.il/report/2026/056/)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-3153 — Fourier rank versus sparsity

A Boolean function has a Fourier expansion in parity characters. Its sparsity counts nonzero coefficients, while its rank is the \(F_{2}\) dimension spanned by their index sets. The question asks whether rank can exceed the square root of sparsity by an unbounded factor. Known addressing examples attain the square-root scale, and the published universal upper bound allows an additional logarithmic factor. The answer requires either an asymptotically separating family or a universal square-root bound with an absolute constant.

[Read in atlas](index.html#TCS-3153) · [Tight Chang’s-Lemma-Type Bounds for Boolean Functions](https://doi.org/10.4230/LIPIcs.FSTTCS.2021.10) · [Fourier Sparsity and Dimension](https://theoryofcomputing.org/articles/v015a011/) · [Spectral Norm, Economical Sieve, and Linear Invariance Testing of Boolean Functions](https://doi.org/10.4230/LIPIcs.STACS.2026.30)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-5892 — Constant-factor randomized direct sums for total Boolean functions

Alice and Bob must jointly compute a total Boolean function of their private inputs. The question compares the communication needed for one input pair with the communication needed for many pairs together. A single universal constant would force cost to grow proportionally with the number of copies. The protocol uses public randomness and must produce the entire answer vector correctly with probability at least two thirds on every input tuple. Recent claimed counterexamples for relations do not resolve the chosen total-function version.

[Read in atlas](index.html#TCS-5892) · [Lifting Theorems for Equality](https://doi.org/10.4230/LIPIcs.STACS.2019.50) · [Efficient Communication Using Partial Information](https://eccc.weizmann.ac.il/report/2010/083/) · [Zero-error information equals amortized communication complexity](https://arxiv.org/abs/2608.04141)
Existing status: `source_open` · Summary written: 2026-09-13

## Fine-grained complexity (28)

### TCS-6595 — Strong Exponential Time Hypothesis

SETH asks whether the optimal deterministic exponential rates for fixed-width satisfiability approach one as the allowed width grows. Every proposed constant saving from exhaustive search must fail at some fixed width. To refute it, one saving must work at every fixed width, although the algorithms and polynomial factors may vary with that width. Faster algorithms for width three, including recent randomized ones, do not meet that requirement. The hypothesis underlies many precise conditional lower bounds, including problems whose algorithms already run in polynomial time.

[Read in atlas](index.html#TCS-6595) · [On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [On some fine-grained questions in algorithms and complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6510 — Truly subcubic APSP

The input is a directed graph with arbitrary exact real edge weights and no negative cycle, and the output gives the shortest distance for every ordered vertex pair. The target is one uniform randomized algorithm with a fixed positive saving below the cubic exponent, correct on the entire output matrix with probability at least two thirds. Time is charged in a specified comparison-addition real RAM that also permits ordinary logarithmic-size word operations, including all preprocessing and output. Known general algorithms achieve subpolynomial savings, while faster restricted results concern node weights, few outgoing weights, or supplied predictions. Recent restrictions on black-box reductions do not rule out all APSP algorithms, and the inspected sources retain the full target as unresolved.

[Read in atlas](index.html#TCS-6510) · [Subcubic Equivalences Between Path, Matrix, and Triangle Problems](https://people.csail.mit.edu/virgi/tria-mmult-jv.pdf) · [Faster all-pairs shortest paths via circuit complexity](https://arxiv.org/abs/1312.6680v2) · [All-Pairs Shortest Paths with Few Weights per Node](https://arxiv.org/abs/2506.20017) · [Node-Weighted Triangles: Faster and Simpler](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.10) · [Warm-Starting All-Pairs Shortest Paths with Predictions](https://arxiv.org/abs/2607.00857) · [The Limits of Black-Box Reductions for All-Pairs Triangle Detection](https://arxiv.org/abs/2608.19092)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6935 — Randomized Strong Exponential Time Hypothesis

Randomized SETH asks whether every fixed positive saving in the exhaustive-search exponent fails at some fixed clause width. Inputs are arbitrary explicitly encoded \(k\)-CNF formulas, with the number of variables in the exponent and a polynomial factor in input length. The developed formulation uses uniform fair-coin Turing machines, error at most \(1/3\) on every input, and worst-case time over random bits. A refutation needs one positive exponent saving valid for every fixed width, although its algorithm and polynomial factor may depend on that width. The standard BPTIME model is explicitly sourced separately from the survey’s RAM convention, and recent fixed-width SAT improvements do not settle the hypothesis.

[Read in atlas](index.html#TCS-6935) · [On some fine-grained questions in algorithms and complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [On Problems as Hard as CNF-SAT](https://arxiv.org/abs/1112.2275v3) · [Local Proofs Approaching the Witness Length](https://eccc.weizmann.ac.il/report/2019/127/revision/2/download/) · [A Better Analysis For PPSZ For 3-SAT](https://arxiv.org/abs/2607.10697v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6937 — Randomized APSP hypothesis for polynomial integer weights

All-pairs shortest paths asks for the exact distance between every ordered pair of vertices in a directed graph. The graph has polynomially bounded signed integer edge weights and no negative-weight cycle. The hypothesis says that for every fixed improvement over the cubic exponent, some polynomial weight bound rules out every randomized algorithm with that running time. Computation uses logarithmic-size machine words, and the whole distance matrix must be correct with probability at least two thirds on every input. Known general algorithms save a subpolynomial factor, while recent restricted algorithms and conditional equivalences do not settle this hypothesis.

[Read in atlas](index.html#TCS-6937) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses](https://arxiv.org/abs/2603.27736v1) · [Faster All-Pairs Shortest Paths via Circuit Complexity](https://arxiv.org/abs/1312.6680v2) · [All-Pairs Shortest Paths with Few Weights per Node](https://arxiv.org/abs/2506.20017v1) · [The Limits of Black-Box Reductions for All-Pairs Triangle Detection](https://arxiv.org/abs/2608.19092v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6596 — Orthogonal Vectors Hypothesis

Bichromatic Orthogonal Vectors asks whether two explicit lists contain binary vectors with disjoint supports. The retained hypothesis says that every proposed fixed saving over quadratic time fails at some fixed logarithmic-dimension constant. It concerns uniform randomized word-RAM algorithms with all preprocessing charged, worst-case running time and bounded error on every input. A complete Lean refutation must provide one positive exponent saving valid for every dimension constant, although its individual programs and time constants may depend on that constant. Known deterministic and randomized dimension-dependent savings, average-case improvements and restricted-model lower bounds leave this full hypothesis unresolved.

[Read in atlas](index.html#TCS-6596) · [More Applications of the Polynomial Method to Algorithm Design](https://theory.stanford.edu/~yuhch123/files/faster-orthog-soda.pdf) · [Deterministic APSP, Orthogonal Vectors, and More: Quickly Derandomizing Razborov–Smolensky](https://people.csail.mit.edu/virgi/6.s078/papers/detapsp_soda.pdf) · [Conditional Hardness of Earth Mover Distance](https://arxiv.org/abs/1909.11068) · [Faster Algorithms for Average-Case Orthogonal Vectors and Closest Pair Problems](https://arxiv.org/abs/2410.22477) · [Faster Algorithms for k-Orthogonal Vectors in Low Dimension](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.85) · [New and Improved Concrete Lower Bounds for Orthogonal Vectors](https://arxiv.org/abs/2607.23799) · [Online Orthogonal Vectors Revisited](https://arxiv.org/abs/2605.04798)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6597 — Algebraic k-Clique Hypothesis

For each fixed clique size, the task is to decide whether an arbitrary graph contains that many pairwise adjacent vertices. The hypothesis compares the leading coefficient of the optimal randomized time exponent with one third of the true matrix-multiplication exponent. The graph algorithm uses logarithmic-size words, and its time bound must hold on every random tape. The graph size tends to infinity first, while the clique size is fixed; the outer limit then considers growing clique sizes. A complete Lean-checked proof or refutation must address that full asymptotic comparison, rather than only logarithmic savings or one fixed clique size.

[Read in atlas](index.html#TCS-6597) · [Dynamic Boolean Formula Evaluation](https://doi.org/10.4230/LIPIcs.ISAAC.2021.61) · [The Role of Regularity in (Hyper-)Clique Detection and Implications for Optimizing Boolean CSPs](https://doi.org/10.4230/LIPIcs.ICALP.2025.78) · [Faster Combinatorial k-Clique Algorithms](https://arxiv.org/abs/2401.13502v2) · [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6661 — Hyperclique Hypothesis

A k-clique in an h-uniform hypergraph is a set of k distinct vertices containing every possible h-element hyperedge. The hypothesis excludes a fixed positive improvement over the exhaustive-search exponent for every fixed uniformity at least three and every larger fixed clique size. The chosen model is a uniform classical randomized word-RAM on a dense membership table, with worst-case time and success probability at least two thirds for each input. A complete Lean proof must establish the full exclusion or give one fixed parameter pair and a proved exponent-saving algorithm that refutes it. Conditional reductions, sparse-input improvements and nonuniform algebraic circuit results from the 2026 literature do not settle this all-input randomized hypothesis.

[Read in atlas](index.html#TCS-6661) · [The Role of Regularity in (Hyper-)Clique Detection and Implications for Optimizing Boolean CSPs](https://arxiv.org/abs/2505.17314) · [Tight Hardness for Shortest Cycles and Paths in Sparse Graphs](https://arxiv.org/abs/1712.08147) · [Classifying Identities: Subcubic Distributivity Checking and Hardness from Arithmetic Progression Detection](https://arxiv.org/abs/2603.28843) · [When Does Sparsity Help for k-Independent Set in Hypergraphs and Other Boolean CSPs?](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.94) · [Beyond Bilinear Complexity: What Works and What Breaks with Many Modes?](https://eccc.weizmann.ac.il/report/2026/025/) · [Partition Rank and Algebraic Circuit Lower Bounds](https://arxiv.org/abs/2607.02241)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7179 — Truly subquadratic exact edit distance

Can exact edit distance between two length-n binary strings be computed in truly subquadratic time? Each insertion, deletion and substitution costs one, and the algorithm must always return the exact minimum. The requested deterministic worst-case bound has a fixed positive saving in the exponent of n. Known reductions rule out such an algorithm if SETH is true, but that hypothesis remains unproved. The 2026 approximation improvement has different accuracy and randomness guarantees.

[Read in atlas](index.html#TCS-7179) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348) · [Quadratic Conditional Lower Bounds for String Problems and Dynamic Time Warping](https://arxiv.org/abs/1502.01063v2) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6503 — Online matrix–vector multiplication conjecture

A fixed Boolean matrix is given first, followed by a sequence of Boolean vectors. The algorithm must return each Boolean product before it sees the next vector. The question asks for a fixed polynomial saving over cubic total time, including preprocessing, with a constant probability that every answer is correct. Known speedups, free-computation cell-probe bounds and faster structured-matrix queries do not resolve the unrestricted word-RAM target. A complete Lean-checked resolution would either refute or prove a central hypothesis behind dynamic-problem lower bounds.

[Read in atlas](index.html#TCS-6503) · [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://arxiv.org/abs/1511.06773v1) · [Faster Online Matrix-Vector Multiplication](https://arxiv.org/abs/1605.01695v2) · [Non-Boolean OMv: One More Reason to Believe Lower Bounds for Dynamic Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.54) · [The Structural Complexity of Matrix-Vector Multiplication](https://arxiv.org/abs/2502.21240v3)
Existing status: `source_open` · Summary written: 2026-09-17

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

### TCS-7313 — ETH versus Gap-ETH

ETH asserts a fixed positive exponential-time lower bound for exact 3-SAT. The selected Gap-ETH asserts such a lower bound for sparse formulas promised to be satisfiable or to leave a fixed fraction of clauses unsatisfied under every assignment. The question asks whether the deterministic exact hypothesis implies this deterministic gap hypothesis. All exponential rates and polynomial input-length factors have explicit quantifiers, and the YES case requires perfect satisfiability. A complete Lean-checked resolution must establish the implication or its actual logical negation, rather than hardness for a different approximation problem.

[Read in atlas](index.html#TCS-7313) · [Dot-Product Proofs and Their Applications](https://eccc.weizmann.ac.il/report/2024/114/revision/2/) · [Parameterized Inapproximability Hypothesis under ETH](https://doi.org/10.1145/3749982) · [Quasi-Linear Size PCPs with Small Soundness from HDX](https://dspace.mit.edu/entities/publication/9bbf3cdb-ea42-4d50-8d98-7b0f2c30432e) · [Mind the Gap? Not for SVP Hardness under ETH!](https://arxiv.org/abs/2504.02695v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6950 — Disjunction of randomized SETH, integer APSP and 3SUM hypotheses

The question asks whether at least one of three core fine-grained hardness hypotheses is true. They concern fixed-width Boolean satisfiability, exact shortest paths with polynomially bounded integer weights, and integer 3SUM. The selected variants allow classical randomized word-RAM algorithms with bounded error and worst-case running time. Refuting the disjunction requires a fixed positive exponent saving for all three tasks, with the clause-width and weight-range quantifiers respected. A complete Lean-checked proof or refutation is required; existing conditional reductions do not settle the assertion.

[Read in atlas](index.html#TCS-6950) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Matching Triangles and Basing Hardness on an Extremely Popular Conjecture](https://doi.org/10.1137/15M1050987) · [Hardness for Triangle Problems under Even More Believable Hypotheses: Reductions from Real APSP, Real 3SUM, and OV](https://arxiv.org/abs/2203.08356v1) · [Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses](https://arxiv.org/abs/2603.27736v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6944 — Min-Weight k-Clique hypothesis

The task finds a fixed-size clique minimizing the sum of its integer edge weights. The hypothesis says that no randomized algorithm saves a positive constant from the exponent k for the source’s full polynomial weight range. Its formal model charges uniform word-RAM computation and requires a correct complete answer with bounded error on every graph. A resolution would affect the fine-grained foundations of weighted graph, geometric and sequence optimization. The card preserves the fixed signed range and distinguishes newer conjectures whose weight exponent is quantified differently.

[Read in atlas](index.html#TCS-6944) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [More Consequences of Falsifying SETH and the Orthogonal Vectors Conjecture](https://www.mpi-inf.mpg.de/~kbringma/paper/2018STOC-1.pdf) · [Hardness of Dynamic Tree Edit Distance and Friends](https://drops.dagstuhl.de/doi/10.4230/LIPIcs.ITCS.2026.78)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7347 — Directed unweighted APSP below \(n^{5/2}\)

Every arc of the input directed graph has length one. The required output gives the exact distance for every ordered pair, including unreachable pairs. The target is any fixed positive saving in the exponent below five-halves. The algorithm may use randomness, but its full matrix must be jointly correct with probability at least two thirds. A complete Lean-checked answer must be unconditional; the recent APSP equivalences retain their stated assumptions.

[Read in atlas](index.html#TCS-7347) · [Algorithms, Reductions and Equivalences for Small Weight Variants of All-Pairs Shortest Paths](https://arxiv.org/abs/2102.06181v1) · [Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses](https://arxiv.org/abs/2603.27736v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7373 — Balanced dense NFA Acceptance Hypothesis

A binary word of length equal to the number of automaton states must be tested for acceptance. The automaton has quadratically many transitions and is supplied explicitly without preprocessing. The question excludes every fixed polynomial improvement over cubic running time for randomized word-RAM algorithms. The source relates a broader NFA Acceptance hypothesis to major static and dynamic complexity barriers. This card keeps the balanced dense binary specialization separate from sparse-automaton results and from simulation-density bounds for regular expressions.

[Read in atlas](index.html#TCS-7373) · [The NFA Acceptance Hypothesis: Non-Combinatorial and Dynamic Lower Bounds](https://theoretics.episciences.org/14397) · [Sparse Regular Expression Matching](https://arxiv.org/abs/1907.04752v7)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5422 — Consequences of linear-time Orthogonal Vectors

Orthogonal Vectors asks whether two lists of Boolean vectors contain a pair with no coordinate equal to one in both vectors. The premise asks for deterministic essentially-linear algorithms in every fixed polylogarithmic dimension regime. The question is whether that premise forces the Exponential Time Hypothesis to fail. Known implications to the stronger SETH assumption and recent low-dimensional algorithms do not settle this precise target. A complete answer must prove the implication or establish both its algorithmic premise and ETH as the full negation.

[Read in atlas](index.html#TCS-5422) · [Superlinear Lower Bounds Based on ETH](https://doi.org/10.4230/LIPIcs.STACS.2022.55) · [Effective Guessing Has Unlikely Consequences](https://doi.org/10.1007/s00224-023-10119-x) · [The Orthogonal Vectors Conjecture and Non-Uniform Circuit Lower Bounds](https://eccc.weizmann.ac.il/report/2024/142/) · [Kronecker Powers, Orthogonal Vectors, and the Asymptotic Spectrum](https://arxiv.org/abs/2509.14489v1) · [Faster Algorithms for \(k\)-Orthogonal Vectors in Low Dimension](https://doi.org/10.4230/LIPIcs.ICALP.2026.85)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6946 — A fine-grained reduction from integer APSP to 3SUM

The question asks whether integer all-pairs shortest paths can be reduced to integer 3SUM while preserving fixed exponent savings. Any subquadratic target saving should yield a subcubic source saving common to all fixed polynomial weight ranges. The reduction may be randomized and adaptive, but must charge its own work and every oracle query. A successful run must return every exact shortest-path distance, with probability at least two thirds on each input graph. Known reductions of both problems to triangle tasks do not give the direct reduction selected here.

[Read in atlas](index.html#TCS-6946) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Some Open Problems in Fine-Grained Complexity](https://www.cs.umd.edu/~gasarch/open/finegrain.pdf) · [Hardness for Triangle Problems under Even More Believable Hypotheses: Reductions from Real APSP, Real 3SUM, and OV](https://arxiv.org/abs/2203.08356v1)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-7270 — Linear-size Circuit-SAT below exhaustive search

The input is a Boolean circuit with a linear number of gates and no depth or sharing restriction. The algorithm must decide exactly whether some input assignment makes its output true. For every fixed gate density, the target is a deterministic algorithm with a fixed positive saving in the variable exponent. The algorithm and saving may depend on that density; small-density and bounded-treewidth results do not cover the full question. A complete Lean-checked proof of the quantified algorithmic claim or its unconditional negation is required.

[Read in atlas](index.html#TCS-7270) · [Beating Brute Force for (Quantified) Satisfiability of Circuits of Bounded Treewidth](https://sites.cs.ucsb.edu/~daniello/papers/boundedTreewidthCircuitSatSODA18.pdf) · [Correlation Bounds and #SAT Algorithms for Small Linear-Size Circuits](https://www2.cs.sfu.ca/~kabanets/papers/linsize-COCOON.pdf) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6949 — NC-SETH for polynomial-size, polylogarithmic-depth circuits

NC-SETH concerns satisfiability of bounded-fan-in circuits of polynomial size and polylogarithmic depth. For each fixed proposed exponential saving, the hypothesis requires some fixed size/depth exponent for which that saving is impossible. Algorithms are uniform within each fixed class, use the stated logarithmic-word RAM model and may err with probability at most one third on each input. A refutation needs one saving that works across every fixed class, though the algorithms and polynomial factors may vary with the class. A complete Lean-checked proof or refutation is required; arbitrary-depth and linear-depth circuit hypotheses are distinct targets.

[Read in atlas](index.html#TCS-6949) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Simulating Branching Programs with Edit Distance and Friends or: A Polylog Shaved is a Lower Bound Made](https://arxiv.org/abs/1511.06022v1) · [Circuits and Backdoors: Five Shades of the SETH](https://arxiv.org/abs/2407.09683v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6942 — Does logarithmic-dimension OV hardness imply Hitting Set hardness?

The question asks whether logarithmic-dimension Orthogonal Vectors hardness implies the corresponding Hitting Set hardness. Both hypotheses forbid one fixed subquadratic exponent saving that works across every fixed logarithmic dimension constant. Different uniform algorithms may be used for different constants, with bounded error on each input and worst-case running time. The equivalent algorithmic direction is from a general fast Hitting Set family to a general fast Orthogonal Vectors family, possibly losing some exponent saving. A complete Lean-checked answer must prove or refute the logical implication; conditional barriers to particular reductions do not settle it.

[Read in atlas](index.html#TCS-6942) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility](https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf) · [Complexity Framework for Forbidden Subgraphs I: The Framework](https://link.springer.com/article/10.1007/s00453-024-01289-2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6945 — Exact-Weight k-Clique hypothesis

The input is a simple graph with signed integer weights on its edges. The decision is whether exactly k vertices form a clique whose edge weights sum to zero. For every fixed k, the hypothesis excludes a randomized algorithm with a fixed positive improvement over the enumeration exponent. Weights have magnitude at most n to the power 100k, and time is measured on a uniform logarithmic-word RAM. The hypothesis supports conditional clique-listing lower bounds and remains distinct from ordinary unweighted clique detection.

[Read in atlas](index.html#TCS-6945) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Towards Optimal Output-Sensitive Clique Listing or: Listing Cliques from Smaller Cliques](https://arxiv.org/abs/2307.15871v2) · [A Note on the Conditional Optimality of Chiba and Nishizeki's Algorithms](https://arxiv.org/abs/2407.08562v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6025 — Subgraph detection with a sublinear treewidth exponent on some unbounded class

The generic subgraph-detection algorithm has a host-size exponent controlled by the pattern’s treewidth. The selected question asks whether some effective class with unbounded treewidth admits an exponent that is sublinear in that treewidth. The pattern-size multiplier may be any computable function, but one deterministic algorithm must handle the whole class. Copies are uncolored and need not be induced, in completely arbitrary host graphs. Known colorful lower bounds require care because their transfers need not preserve an arbitrarily selected uncolored pattern class.

[Read in atlas](index.html#TCS-6025) · [Current Algorithms for Detecting Subgraphs of Bounded Treewidth Are Probably Optimal](https://doi.org/10.4230/LIPIcs.ICALP.2021.40) · [Can You Beat Treewidth?](https://doi.org/10.4086/toc.2010.v006a005) · [Can You Link Up With Treewidth?](https://arxiv.org/abs/2410.02606v2)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0562 — Nondeterministic Strong Exponential Time Hypothesis

NSETH asks whether certifying unsatisfiability remains close to exhaustive search even with nondeterministic choices. The requested refutation needs one positive saving in the exponent for every fixed clause width. Each unsatisfiable formula must have an accepting branch, while every branch on a satisfiable formula must reject. The running-time guarantee applies to every branch of a uniform machine and includes polynomial input-processing overhead. Known randomized-verifier protocols and conditional circuit lower bounds do not settle this exact nondeterministic question.

[Read in atlas](index.html#TCS-0562) · [Some Open Problems in Fine-Grained Complexity](https://www.cs.umd.edu/~gasarch/open/finegrain.pdf) · [Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility](https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf) · [Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.28)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0560 — A fine-grained reduction from logarithmic-dimension Hitting Set to 3SUM

Hitting Set asks whether one supplied set intersects every set in a second supplied list. The target is a randomized reduction from its logarithmic-dimension version to exact integer 3SUM. Every fixed subquadratic target saving must yield a source saving common to all fixed logarithmic dimension constants. The cost bound charges both the reduction’s own work and the sum of all oracle-query costs. A complete answer must prove or refute this resource-preserving reduction rather than merely relate the problems by ordinary polynomial time.

[Read in atlas](index.html#TCS-0560) · [Some Open Problems in Fine-Grained Complexity](https://www.cs.umd.edu/~gasarch/open/finegrain.pdf) · [On Some Fine-Grained Questions in Algorithms and Complexity](https://people.csail.mit.edu/virgi/eccentri.pdf) · [Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility](https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0815 — Fine-grained comparability of permanent and SETH

The permanent of a binary matrix counts its perfect matchings exactly. The source asks whether its exponential-time difficulty can be related to SETH in either direction. This card makes that comparison precise using deterministic oracle reductions that preserve a constant saving in the exponential rate. A reduction from SAT must preserve a saving uniform across clause widths, while the reverse direction may choose a fixed width for each saving. The preferred binary-matrix case and exact counting oracle are distinguished from general matrix variants, ordinary completeness and counting SAT.

[Read in atlas](index.html#TCS-0815) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time — Relation between permanent computation and SETH](https://doi.org/10.4230/DagRep.3.8.40) · [Computations with Polynomial Evaluation Oracle: Ruling Out Superlinear SETH-Based Lower Bounds](https://doi.org/10.1137/1.9781611977912.73)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0761 — Time exponents for multiple-string LCS over fixed alphabets

Multiple-string LCS finds a longest string that occurs as a subsequence of every input. The target is the optimal deterministic time exponent for every fixed alphabet size and fixed number of strings. It makes the source’s question about a fractional exponent saving into an explicitly broader quantitative function. Resolving the function would identify how alphabet size changes the computational cost of coordinating many sequences. Acceptance requires a Lean-certified error of at most one hundredth at every parameter pair, while retaining the source question separately.

[Read in atlas](index.html#TCS-0761) · [Randomization in Parameterized Complexity (Dagstuhl Seminar 17041)](https://doi.org/10.4230/DagRep.7.1.103) · [Tight Hardness Results for LCS and other Sequence Similarity Measures](https://theory.stanford.edu/~virgi/LCS.pdf) · [Exploring the Gap Between LCS and LCStr](https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.27/LIPIcs.CPM.2026.27.html)
Existing status: `source_open` · Summary written: 2026-09-14

## Pseudorandomness and derandomization (40)

### TCS-0003 — P versus BPP

P contains total decision languages with a deterministic polynomial-time decider, while BPP allows fair random bits and error at most one third separately on every input. The randomized machine must obey one polynomial time bound on every random tape, and the deterministic decider must work correctly at every input length. The question is whether these classes are equal, allowing a different deterministic algorithm and a different polynomial exponent for each language. Nonuniform simulation and equality under strong circuit-hardness assumptions are established results, while recent insensitivity bounds retain additional hypotheses. A current preprint claims a full separation, but this review has not independently validated its proof and therefore retains uncertain status.

[Read in atlas](index.html#TCS-0003) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [P=BPP if E Requires Exponential Circuits: Derandomizing the XOR Lemma](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/IW97/proc.pdf) · [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](https://eccc.weizmann.ac.il/report/2026/082/) · [Probabilistic Computers (and Hence Quantum Computers) Are Rigorously More Powerful Than Classical Deterministic Computers, and Derandomization](https://arxiv.org/abs/2308.09549v9)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-6600 — Optimal explicit pseudorandom generators for read-once branching programs

An ordered read-once branching program reads each input bit in order while retaining one of a bounded number of states, with arbitrary merging transitions allowed. The question asks for one ordinary uniform-seed generator family that simultaneously approximates the acceptance probability of every such program. Seed length and worst-case workspace must be linear in the logarithms of length and width plus the error parameter, with a uniform polynomial-in-length,width,inverse-error time bound. Recent weighted generators, permutation-program PRGs and width-three hitting sets retain guarantees or hypotheses different from this unrestricted target. A solution requires a complete Lean proof constructing the uniform family with all resource and error bounds, or ruling out every such program and universal constants.

[Read in atlas](index.html#TCS-6600) · [Pseudorandom generators for space-bounded computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf) · [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2021.28) · [Hitting Sets Give Two-Sided Derandomization of Small Space](https://theoryofcomputing.org/articles/v018a021/) · [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://arxiv.org/abs/2502.08272v5) · [Improved Error Reduction for Weighted PRGs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.39) · [A Forward-Backward Weight Analysis of INW for Permutation Branching Programs](https://eccc.weizmann.ac.il/report/2026/123/) · [Optimal Hitting Set Generators via A Potential-Descent Framework](https://eccc.weizmann.ac.il/report/2026/178/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0026 — L versus BPL

L contains languages decided by one deterministic machine using logarithmic work space, while BPL permits fresh fair random bits and bounded error. Random bits are read once unless stored in counted memory, and the randomized machine obeys uniform logarithmic-space and polynomial-time bounds on every run. The question asks whether every BPL language has a deterministic logarithmic-space decider that is correct on every input. The best general simulation reviewed here uses more than logarithmic space, and recent weighted-generator and regular-program results retain distinct guarantees or restrictions. A solution requires a complete Lean proof of the inclusion or a single total language separating the two classes under the stated uniform model.

[Read in atlas](index.html#TCS-0026) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Better Pseudodistributions and Derandomization for Space-Bounded Computation](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf) · [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/) · [Weighted Pseudorandom Generators for Read-Once Branching Programs via Weighted Pseudorandom Reductions](https://arxiv.org/abs/2502.08272v5)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6686 — P versus RP

RP consists of languages decided in worst-case polynomial time using fair random bits, with no false acceptances. The question asks whether every such language also has a uniform deterministic polynomial-time decider. Each language may have its own fixed polynomial bound, but the exponent cannot vary with the input. Strong circuit-hardness assumptions imply derandomization, while deterministic algorithms for individual examples do not settle the whole class comparison. A resolution would determine whether one-sided-error randomness increases efficient decision power.

[Read in atlas](index.html#TCS-6686) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [\(\mathrm{P}=\mathrm{BPP}\) if \(\mathrm{E}\) Requires Exponential Circuits: Derandomizing the XOR Lemma](https://doi.org/10.1145/258533.258590) · [Probabilistic Computers (and Hence Quantum Computers) Are Rigorously More Powerful Than Classical Deterministic Computers, and Derandomization](https://arxiv.org/abs/2308.09549v9)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6662 — Optimal deterministic restricted-isometry matrices

A restricted-isometry matrix approximately preserves squared Euclidean norms of every vector with at most a specified number of nonzero coordinates. The question asks for one deterministic algorithm producing an explicit rational matrix with \(O(s\ln(eN/s))\) rows and distortion \(1/3\). Its bit running time and complete output length must be polynomial in the ambient dimension, with constants common to every dimension and sparsity. A complete Lean proof must establish the algorithm, its resource bounds and the simultaneous guarantee for all real sparse vectors, or prove unconditional nonexistence in the fixed model. Random optimal matrices, reduced random seeds and coherence-based constructions for restricted parameter families do not meet this uniform deterministic guarantee.

[Read in atlas](index.html#TCS-6662) · [Doubly transitive equiangular tight frames that contain regular simplices](https://www.sciencedirect.com/science/article/pii/S0024379525003143) · [The road to deterministic matrices with the restricted isometry property](https://www.math.ucdavis.edu/~strohmer/courses/270/road_to_rip.pdf) · [Explicit constructions of RIP matrices and related problems](https://arxiv.org/abs/1008.4535) · [Satisfying the restricted isometry property with the optimal number of rows and slightly less randomness](https://arxiv.org/abs/2311.07889) · [Compressed sensing matrices from orthogonal spaces over finite fields of odd characteristic](https://arxiv.org/abs/2608.23062)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6699 — AM versus NP

Arthur–Merlin protocols let a prover choose a polynomial-length reply after seeing the verifier’s public random challenge. The question asks whether every language with such a protocol also has ordinary NP certificates. The verifier must be uniform and polynomial time, with completeness and soundness on every input. Graph nonisomorphism would acquire static polynomially checkable certificates if the equality holds, but is not assumed complete for the whole question. Known conditional derandomization and weaker recent simulations leave the unconditional class comparison open.

[Read in atlas](index.html#TCS-6699) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [Derandomizing Arthur–Merlin Games using Hitting Sets](https://doi.org/10.1007/s00037-005-0197-7) · [Instance-Wise Hardness and Refutation versus Derandomization for Arthur–Merlin Protocols](https://doi.org/10.1007/s00037-025-00279-2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6696 — Uniform PRGs from exponential-time hardness

The hypothesis says that some exponential-time language resists randomized subexponential-time algorithms. The question asks whether this uniform hardness yields a single generator with only polylogarithmically many seed bits. Its output must fool each fixed linear-time probabilistic distinguisher on infinitely many output lengths. The generator may take quasipolynomial time, but it must be uniform and independent of the distinguisher. Known low-end and more structured high-end results leave this general hardness-to-randomness implication distinct.

[Read in atlas](index.html#TCS-6696) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Pseudorandomness and Average-Case Complexity via Uniform Reductions](https://people.seas.harvard.edu/~salil/research/uniform-cc.pdf) · [Unstructured Hardness to Average-Case Randomness](https://eccc.weizmann.ac.il/report/2022/097/) · [Derandomization vs. Lower Bounds for Arthur-Merlin Protocols](https://pages.cs.wisc.edu/~dieter/Papers/sdroievski-dissertation.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7271 — Two-source extraction at log n plus constant entropy

Two arbitrary independent distributions on n-bit strings each have min-entropy at least log base two of n plus one fixed additive constant. The question asks for one deterministic polynomial-time algorithm that turns one string from each source into a bit with bias at most one hundredth. The same program and time bound must work at every length without an extra seed, advice or descriptions of the distributions. Li’s checked theorem achieves a constant multiple of log n entropy, while his source explicitly leaves the additive threshold as a further question. Matching that threshold efficiently would sharpen a central randomness-extraction result and have consequences for explicit Ramsey graphs.

[Read in atlas](index.html#TCS-7271) · [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802v2) · [Two-Source and Affine Non-Malleable Extractors for Small Entropy](https://arxiv.org/abs/2404.17013v1) · [Extractors for Samplable Distributions from the Two-Source Extractor Recipe](https://eccc.weizmann.ac.il/report/2025/107/revision/3/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1005 — Unconditional subexponential simulation of BPP

BPP contains decision problems solved efficiently using random bits with bounded error on every input. The question asks whether all of them have exact deterministic simulations in the class SUBEXP. Here SUBEXP requires a simulation in time two to the n-to-epsilon power for every fixed positive epsilon. The simulator may depend on the chosen exponent, but it must work on every input without advice or assumptions. Known general brute-force simulations take larger exponential time, while stronger derandomization theorems rely on unproved hardness.

[Read in atlas](index.html#TCS-1005) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5287 — Does arithmetic formula hardness derandomize identity testing?

An arithmetic formula is a tree of additions and multiplications with rational constants and commuting variables. Assume a coefficient-explicit multilinear polynomial family eventually requires formulas larger than every fixed polynomial in its variable count. Must there then be deterministic identity testers for every unrestricted formula in time 2^{O(N^epsilon)} for every epsilon > 0? The selected target is the forward, subexponential branch of the original two-direction question. Known later results change the hardness assumption or restrict the formula model; the bounded review found no verified resolution of this implication.

[Read in atlas](index.html#TCS-5287) · [Hardness vs Randomness for Bounded Depth Arithmetic Circuits](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2018.13) · [Closure Results for Polynomial Factorization](https://theoryofcomputing.org/articles/v015a013/) · [Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds](https://www2.cs.sfu.ca/~kabanets/papers/poly_derand.pdf) · [Hardness-Randomness Tradeoffs for Algebraic Computation](https://mrinalkr.bitbucket.io/papers/hardness-randomness-survey.pdf) · [Polynomial-Time PIT from (Almost) Necessary Assumptions](https://eccc.weizmann.ac.il/report/2025/042/) · [Algebraic Pseudorandomness in VNC⁰](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.15) · [Polynomial Identity Testing for Read-4 Arithmetic Formulas](https://eccc.weizmann.ac.il/report/2026/076/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6879 — Explicit near-optimal vertex expanders

The goal is to construct arbitrarily large regular graphs by a deterministic polynomial-time procedure. Every sufficiently small set must have almost the largest possible number of distinct neighbors outside itself. The original survey asks for the sharp additive expansion factor of the degree minus two minus any fixed positive tolerance. The 2025 lossless-expander breakthrough gives an arbitrarily small fixed relative loss, with a degree threshold depending on that loss. Because these quantified guarantees differ, the precise original target is retained with uncertain current status rather than being marked solved from the relative theorem alone.

[Read in atlas](index.html#TCS-6879) · [Expander Graphs and Their Applications](https://www.math.ias.edu/~avi/BOOKS/expanderbookr1.pdf) · [Explicit Lossless Vertex Expanders](https://arxiv.org/abs/2504.15087)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5341 — Pseudorandom generators from hitting-set generators

A hitting-set generator produces strings that intersect every sufficiently dense set accepted by a polynomial-size Boolean circuit. A pseudorandom generator must instead approximate every such circuit’s acceptance probability when its seed is chosen uniformly. The selected cryptographic question asks whether the existence of the first kind of uniform polynomial-time generator entails the existence of the second, with negligible security bounds and any nontrivial stretch. The generators may have different parameters, and the known seed-extending result for logarithmic-depth circuits does not establish the unrestricted implication. A complete Lean proof must decide this existence implication, clarifying the relationship between two basic forms of computational randomness.

[Read in atlas](index.html#TCS-5341) · [Errorless Versus Error-Prone Average-Case Complexity](https://doi.org/10.4230/LIPIcs.ITCS.2022.84) · [Pseudorandomness and the Minimum Circuit Size Problem](https://doi.org/10.4230/LIPIcs.ITCS.2020.68) · [Capturing One-Way Functions via NP-Hardness of Meta-Complexity](https://eccc.weizmann.ac.il/report/2023/037/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6729 — Deterministic linear representations of transversal matroids

A bipartite graph defines a transversal matroid by declaring a subset on its first side independent when it can be matched to distinct vertices on the second side. The task is to construct one explicit rational matrix whose corresponding columns are linearly independent exactly for those subsets. The question asks for one uniform deterministic algorithm with polynomial bit running time, including the full binary output. Randomized polynomial-time representations and deterministic quasipolynomial-time representations are known, while polynomial-time derandomization would support important matroid and preprocessing algorithms. A complete Lean answer must prove such a construction works on every bipartite graph or prove that no deterministic algorithm meets the stated polynomial bound.

[Read in atlas](index.html#TCS-6729) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf) · [Quasipolynomial-Time Deterministic Kernelization and (Gammoid) Representation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.54)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6693 — Subpolynomial-seed pseudorandom generators for \(\mathrm{AC}^{0}[2]\)

The question asks for pseudorandom bits that fool constant-depth circuits built from AND, OR and parity gates. For each fixed depth, one generator family must work against every circuit with at most as many computation gates as output bits. The difference in acceptance probabilities must be at most one quarter for every permitted circuit. The seed length must eventually be smaller than every positive power of the output length. Uniform generation may take time polynomial in the number of seeds, and known restricted-circuit or larger-field results do not meet the whole target.

[Read in atlas](index.html#TCS-6693) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [New Pseudorandom Generators and Correlation Bounds Using Extractors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.68) · [Optimal PRGs for Low-Degree Polynomials over Polynomial-Size Fields](https://arxiv.org/abs/2602.10030v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1018 — Linear-seed hardness-to-randomness sampling

A hard Boolean function can provide pseudorandom bits by being evaluated at carefully correlated inputs. The question asks for a uniform sampler using only a constant multiple of one input length as its random seed. It must produce polynomially many bits in the hardness parameter, each from exactly one evaluation of the original function. Every function with the specified average-case circuit hardness must yield a generator fooling the stated circuits to inverse-output-length error. General short-seed transformations and newer results under stronger hardness assumptions do not automatically preserve this required evaluation form.

[Read in atlas](index.html#TCS-1018) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Nearly Optimal Pseudorandomness from Hardness](https://doi.org/10.1145/3555307)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1956 — Super-bits from demi-bits

A demi-bit is a polynomial-size generator that adds one output bit and resists nondeterministic tests rejecting every generated output. A super-bit also resists tests that accept generated outputs but accept uniformly random strings noticeably more often. Both notions here require hardness at least exponential in a fixed positive power of the seed length for every sufficiently large length. The question asks whether existence of the weaker generator guarantees existence of the stronger one, allowing different nonuniform circuit families. Known stretching and range-avoidance results give consequences of demi-bits without supplying this security upgrade.

[Read in atlas](index.html#TCS-1956) · [Stretching Demi-Bits and Nondeterministic-Secure Pseudorandomness](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2024.95) · [Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.111)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-3958 — Polynomial-stretch PRGs for depth-two threshold circuits with superlinear gate count

The circuit class has at most two layers of gates that compare weighted sums against thresholds. The question allows a fixed superlinear number of gates with arbitrary real weights and unrestricted fan-in. One uniform polynomial-time generator must produce n bits from at most n^(1−delta) random bits for a fixed positive delta. Every circuit in the class must distinguish that output from uniform with advantage at most one tenth. The target asks for polynomial stretch beyond the one-bit construction obtainable from known average-case hardness.

[Read in atlas](index.html#TCS-3958) · [Satisfiability and Derandomization for Small Polynomial Threshold Circuits](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2018.46) · [Fooling Constant-Depth Threshold Circuits](https://ieee-focs.org/FOCS-2021-Papers/pdfs/FOCS2021-5stbVHiOp5jRHWlSl41FkR/205500a104/205500a104.pdf) · [Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits](https://eccc.weizmann.ac.il/report/2026/039/) · [Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits](https://cseweb.ucsd.edu/~dakane/depth2LTF.pdf)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-4778 — Does exponential circuit hardness derandomize amplified relational computation?

The task is to find a valid output for a relation, even when validity cannot be efficiently checked. The randomized solver must reduce its error to 2^−t in time polynomial in the input length and t. Output lengths stay polynomial in the original input length, independently of t. The selected hypothesis gives exponential circuit hardness to a language computable in deterministic exponential time. The question is whether this hypothesis guarantees a uniform deterministic polynomial-time solver for every such relation.

[Read in atlas](index.html#TCS-4778) · [A Qubit, a Coin, and an Advice String Walk into a Relational Problem](https://doi.org/10.4230/LIPIcs.ITCS.2024.1)
Existing status: `uncertain` · Summary written: 2026-09-18

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

### TCS-6689 — Simultaneously optimal averaging samplers

An averaging sampler estimates a function’s global mean by taking the ordinary mean of a short list of sampled values. The question asks for one explicit construction with both a logarithmic randomness budget and the sample count of independent sampling. Each sample must be computable efficiently from the seed and its index, without generating the whole list first. The guarantee applies to every function valued in the unit interval and to all positive error and failure regimes. The 2025 constructions approach both targets, but retain either an extra exponent in sample count or extra logarithmic randomness.

[Read in atlas](index.html#TCS-6689) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Near-Optimal Averaging Samplers and Matrix Samplers](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.6) · [Near-Optimal Averaging Samplers and Matrix Samplers](https://eccc.weizmann.ac.il/report/2024/097/revision/5/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-2201 — A general oracle conversion from two-source extractors to non-malleable extractors

An ordinary two-source extractor produces a nearly uniform bit from two independent weak random strings. Non-malleability requires that bit to stay nearly uniform even after revealing the output on separately tampered strings. The selected question asks for one general conversion using only evaluation queries to the original extractor. It permits a constant-factor logarithmic entropy overhead, a fixed-power increase in error and polynomial time in inverse error. The exact conversion is an editorial candidate inspired by the source’s broader question, with its present status recorded separately.

[Read in atlas](index.html#TCS-2201) · [Two-Source and Affine Non-Malleable Extractors for Small Entropy](https://doi.org/10.4230/LIPIcs.ICALP.2024.108)
Existing status: `uncertain` · Summary written: 2026-09-18

### TCS-1021 — Promise-BPP derandomization implying EXP circuit hardness

Derandomization replaces efficient bounded-error randomized algorithms by deterministic ones. The question assumes this replacement for promise problems and asks whether it forces an exponential-time language to lack polynomial-size Boolean circuits. Known implications involving nondeterministic exponential time do not establish the deterministic-class target. The issue is a converse to hardness-based pseudorandomness constructions. The project seeks to explain whether eliminating randomness necessarily reveals an explicit source of circuit hardness at the corresponding deterministic computational scale.

[Read in atlas](index.html#TCS-1021) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-1022 — \(\mathrm{NEXP}\) circuit hardness from promise derandomization

Promise derandomization says that every efficiently randomized promise problem also has a deterministic polynomial-time solver. The question asks whether this forces a total language in NEXP to require Boolean circuits of size exponential in a positive power of input length. The circuits are ordinary deterministic nonuniform circuits, while nondeterminism belongs to the language class. Known superpolynomial lower bounds and later time-size or restricted-circuit refinements do not directly supply the requested quantitative conclusion. A resolution would sharpen a fundamental connection between eliminating randomness and proving circuit hardness.

[Read in atlas](index.html#TCS-1022) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [In search of an easy witness: Exponential time vs. probabilistic polynomial time](https://www.cs.sfu.ca/~kabanets/Research/ikw.html) · [Tighter Connections between Derandomization and Circuit Lower Bounds](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2015.645) · [Proving that \(\mathrm{prBPP}=\mathrm{prP}\) is as hard as proving that “almost NP” is not contained in \(\mathrm{P/poly}\)](https://eccc.weizmann.ac.il/report/2018/003/revision/5/download/) · [Almost-Everywhere Circuit Lower Bounds from Non-Trivial Derandomization](https://eccc.weizmann.ac.il/report/2020/150/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1125 — Sub-log-squared seeds for width-four ordered branching programs

The tests are branching programs that read each input bit once and keep at most four states. One uniform polynomial-time generator must preserve every test’s acceptance probability within one tenth. Its seed must be little-o of the square of the logarithm of the output length. Nearly logarithmic seeds are known for width three, while the general width-four bound remains log-squared in the checked sources. Recent weighted-generator results and restrictions on INW constructions do not resolve this ordinary-generator question.

[Read in atlas](index.html#TCS-1125) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/revision/2/) · [Pseudorandom Generators for Width-3 Branching Programs](https://arxiv.org/abs/1806.04256) · [On Sums of INW Pseudorandom Generators](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2025.67) · [Improved Error Reduction for Weighted PRGs](https://eccc.weizmann.ac.il/report/2026/064/revision/3/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1133 — Sub-log-squared seeds for polynomial-size CNFs and DNFs

A CNF is an AND of clauses, and a DNF is an OR of terms, with unrestricted reuse of variables. The target is one uniform polynomial-time generator that preserves satisfying fractions within one tenth. For every fixed polynomial formula-size bound, the seed must be little-o of log-squared input length. The checked general seed bound has log-squared length with an additional log-log factor. Bounded-read constructions and recent hitting-set results do not resolve the unrestricted probability-preservation target.

[Read in atlas](index.html#TCS-1133) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/revision/2/) · [Improved Pseudorandom Generators for AC⁰ Circuits](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2022.34) · [Pseudorandomness for read-k DNF formulas](https://www.cs.columbia.edu/~rocco/papers/soda19.html) · [Optimal Hitting Set Generators via A Potential-Descent Framework](https://eccc.weizmann.ac.il/report/2026/178/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1014 — Lossless condensers with constant output overhead

A lossless condenser compresses a weak random source while preserving its guaranteed entropy together with the seed entropy. This question asks for a logarithmic seed and an output only a constant number of bits longer than that preserved entropy. The output may be nonuniform, but it must be within one hundredth in statistical distance of a distribution with the required min-entropy. The equivalent graph target has nearly lossless expansion and only a constant factor more right vertices than the number of outgoing edges from a source set. Recent multiplicity-code and two-sided-expansion results improve related structure without meeting this constant-overhead target.

[Read in atlas](index.html#TCS-1014) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Unbalanced Expanders from Multiplicity Codes](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2022.12) · [Two-Sided Lossless Expanders in the Unbalanced Setting](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.34)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0854 — Promise-ZPP versus Promise-BPP derandomization

The question asks whether derandomizing every zero-error promise problem also derandomizes every bounded-error promise problem. Zero-error machines may abstain, but whenever a promised input receives a definite answer that answer is correct. Bounded-error machines instead distinguish acceptance probabilities at least two thirds from probabilities at most one third. Each randomized machine may have its own deterministic polynomial-time decider, which must halt on all inputs and be correct on the promise. The target is a general unrelativized implication; total-language equalities and specialized low-space results do not settle it.

[Read in atlas](index.html#TCS-0854) · [Open Problems In Honor of Luca Trevisan — ZPP and Promise-ZPP](https://www.cs.umd.edu/~gasarch/open/LUCA/luca.pdf) · [Using Hardness vs Randomness to Design Low-Space Algorithms](https://eccc.weizmann.ac.il/report/2026/045/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1135 — Promise-AM derandomization via targeted hitting sets

The question compares promise-Arthur–Merlin derandomization with the existence of targeted hitting sets. A generator receives a co-nondeterministic circuit and must hit its accepting ordinary inputs whenever they occupy at least half the domain. Nondeterministic generation must always have a successful branch, and every successful output must satisfy the required hitting guarantee. The source asks whether eliminating public randomness is equivalent to a uniform polynomial-time generator of this kind. The checked 2025 journal result establishes a weaker connection involving different time, advice and input-length guarantees.

[Read in atlas](index.html#TCS-1135) · [New ways of studying the \(\mathrm{BPP}=\mathrm P\) conjecture](https://eccc.weizmann.ac.il/report/2023/094/) · [Instance-Wise Hardness and Refutation versus Derandomization for Arthur-Merlin Protocols](https://pages.cs.wisc.edu/~dieter/Papers/r-am-instance-wise-cc.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1137 — Derandomization from almost-all-inputs uniform hardness

For every fixed time exponent, assume that some polynomial-time function defeats each faster randomized algorithm on all but finitely many inputs. The hard function outputs as many bits as its input, and success means computing the entire output correctly with probability at least two thirds. The question asks whether this assumption forces deterministic polynomial-time solutions to all bounded-error randomized promise problems. The hard function and its evaluation time may depend on the adversarial exponent, while the finite exceptional set may also depend on the adversary. A converse is known with a circuit-depth restriction; the target removes that restriction without weakening the derandomization conclusion.

[Read in atlas](index.html#TCS-1137) · [New ways of studying the \(\mathrm{BPP}=\mathrm P\) conjecture](https://eccc.weizmann.ac.il/report/2023/094/) · [Hardness vs. Randomness, Revised: Uniform, Non-Black-Box, and Instance-wise](https://epubs.siam.org/doi/10.1137/22M1475491) · [On the Complexity of Avoiding Heavy Elements](https://eccc.weizmann.ac.il/report/2024/115/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1008 — Fully explicit bipartite vertex expanders with constant additive loss

The target is a balanced bipartite graph family in which every sufficiently small left set has at least D minus C times as many distinct right neighbors. One universal additive loss C must work for arbitrarily large fixed degrees D, while the positive density of expanding sets may depend on D. For each fixed degree, one deterministic algorithm must compute each numbered neighbor in time polynomial in the bit length of the vertex labels. The user selected an infinite effective family of unbounded sizes, without requiring every size or a dense size sequence. The checked recent multiplicative-loss constructions do not settle this target, which requires a complete Lean-checked construction or refutation.

[Read in atlas](index.html#TCS-1008) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Explicit Lossless Vertex Expanders](https://arxiv.org/abs/2504.15087v1) · [Two-Sided Lossless Expanders in the Unbalanced Setting](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.34)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1013 — Optimal-size highly unbalanced lossless expanders

The problem asks for an explicit bipartite graph for every left-side size and every prescribed exact subset size. Each such subset must reach at least ninety-nine percent of the maximum number of distinct neighbors allowed by the left degree. The left degree must be polynomial in the logarithm of the left-side size, and the right side must have size at most a fixed constant times the subset size times that degree. A single deterministic construction must compute its parameters and any requested neighbor in polylogarithmic time, making the graphs useful as lossless condensers. A complete Lean proof must establish this uniform construction or its negation, while the checked later results do not meet all of its requirements.

[Read in atlas](index.html#TCS-1013) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf#page=162) · [Unbalanced Expanders from Multiplicity Codes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2022.12) · [Explicit Time and Space Efficient Encoders Exist Only with Random Access](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2024.5) · [Two-Sided Lossless Expanders in the Unbalanced Setting](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.34) · [Explicit unbalanced 1-expanders with small degree and right size](https://arxiv.org/abs/2609.14587v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1124 — Optimal PRGs for high-dimensional combinatorial rectangles

A combinatorial rectangle requires each of several disjoint input blocks to belong to an arbitrary chosen subset. The generator must preserve every rectangle’s probability to a prescribed additive error. The requested seed is proportional to block length plus logarithmic inverse error plus doubly logarithmic total length. The same polynomial-time algorithm and absolute seed constant must work in every dimension and accuracy regime. Checked near-optimal rectangle generators and recent optimal min-wise hashing results do not establish the full target.

[Read in atlas](index.html#TCS-1124) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/revision/2/) · [Concentration for Limited Independence via Inequalities for the Elementary Symmetric Polynomials](https://theoryofcomputing.org/articles/v016a017/) · [Explicit Min-wise Hash Families with Optimal Size](https://arxiv.org/abs/2510.10431v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1019 — Polynomial-time derandomization of randomized \(\mathrm{AC}^0\)

The question asks whether randomness can be removed from uniform shallow AND–OR computations using deterministic polynomial time. Each randomized circuit must answer correctly with probability at least two thirds on every input. A single polynomial-time procedure constructs the family’s circuit descriptions from the input length. The deterministic simulator may use arbitrary polynomial-time computation and need not remain a constant-depth circuit. Quasipolynomial simulation, correctness on most inputs and nonuniform deterministic circuits do not meet the full target.

[Read in atlas](index.html#TCS-1019) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [Weak derandomization of weak algorithms: explicit versions of Yao’s lemma](https://www.cs.haifa.ac.il/~ronen/online_papers/YaoLemma.pdf) · [Improved Pseudorandom Generators for \(\mathrm{AC}^0\) Circuits](https://doi.org/10.4230/LIPIcs.CCC.2022.34)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1122 — Nontrivial PRGs for logarithmic-degree binary polynomials

The tests are all binary polynomials of degree at most the floor of log₂ n, without a sparsity restriction. One uniform polynomial-time generator must preserve every test’s output probability within one tenth. The user-selected goal is to save at least one random bit at every sufficiently large output length. Known binary-field constructions in the checked sources retain exponential dependence on degree. The 2026 optimal-seed construction over larger-characteristic fields does not settle this binary-field target.

[Read in atlas](index.html#TCS-1122) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/revision/2/) · [The Sum of d Small-Bias Generators Fools Polynomials of Degree d](https://www.khoury.northeastern.edu/home/viola/papers/d.pdf) · [Fractional Pseudorandom Generators from Any Fourier Level](https://eccc.weizmann.ac.il/report/2020/121/revision/1/) · [Optimal PRGs for Low-Degree Polynomials over Polynomial-Size Fields](https://arxiv.org/abs/2602.10030v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1131 — Sublinear-seed generators for AC0 with parity gates

These shallow Boolean circuits may combine AND, OR and parity gates throughout the circuit, with arbitrary reuse of input variables. The question asks for one uniform generator that fools every circuit of each fixed depth and polynomial size with distinguishing error at most one tenth. The generator must write all its output bits in polynomial time and use a seed whose length divided by the output length tends to zero. The fixed error is an explicit interpretation of the source’s constant-error discussion because the numbered question does not specify an error value. Known linear-seed savings and generators for restricted gate patterns or large-field polynomials do not meet this unrestricted parity-circuit target.

[Read in atlas](index.html#TCS-1131) · [Theory of Unconditional Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2023/019/revision/2/download) · [On Beating the Hybrid Argument](https://doi.org/10.4086/toc.2013.v009a026) · [New Pseudorandom Generators and Correlation Bounds Using Extractors](https://arxiv.org/abs/2501.02653v1) · [Optimal PRGs for Low-Degree Polynomials over Polynomial-Size Fields](https://arxiv.org/abs/2602.10030v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1007 — Universal traversal sequences under arbitrary labels

A universal traversal sequence is one list of absolute local port numbers that visits every vertex of every graph of a specified size and degree. The graph may have parallel edges and self-loops, and its local port labels are arbitrary. The question asks for a deterministic polynomial-time constructor given only the size and degree parameters. Short sequences are known to exist, but incoming-port-based exploration and polynomial cover time with expensive local computation are different guarantees. An efficient construction would remove randomness from graph-independent traversal under severely restricted information.

[Read in atlas](index.html#TCS-1007) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Self-stabilizing Graph Exploration by a Single Agent](https://arxiv.org/abs/2010.08929v4) · [Self-stabilizing graph exploration by a single agent](https://doi.org/10.1016/j.tcs.2026.116085)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3986 — Circuit hardness from inverse-polynomial-error BPP heuristics

The premise permits deterministic polynomial-time simulation of each BPP language with inverse-polynomial error under uniformly random inputs. The guarantee holds at every sufficiently large length, with separate algorithms for different requested error powers. The selected conclusion is a standard disjunction of Boolean circuit hardness for NEXP and arithmetic circuit hardness for the permanent. An older theorem reaches this conclusion under much smaller exceptional sets. The card makes the source’s broad converse direction precise through an explicitly authorized editorial specialization.

[Read in atlas](index.html#TCS-3986) · [Fine-Grained Derandomization: From Problem-Centric to Resource-Centric Complexity](https://doi.org/10.4230/LIPIcs.ICALP.2018.27) · [Fine-Grained Derandomization: From Problem-Centric to Resource-Centric Complexity — full version](https://eccc.weizmann.ac.il/report/2018/092/) · [Pseudorandom generators, typically-correct derandomization, and circuit lower bounds](https://doi.org/10.1007/s00037-011-0019-z) · [On The Utility of Fine-Grained Complexity Theory](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2020/EECS-2020-165.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-5798 — Pseudodeterministic construction of primes at every length

Given a length in unary, generate a prime with exactly that many binary digits in polynomial time. For each length, independent runs must return the same fixed prime with probability at least two thirds. The fixed prime may depend on the algorithm; it is not prescribed in advance. The requirement must hold at every length of at least two bits. The known polynomial-time construction meets this requirement only on infinitely many lengths.

[Read in atlas](index.html#TCS-5798) · [Bipartite Perfect Matching in Pseudo-Deterministic NC](https://doi.org/10.4230/LIPIcs.ICALP.2017.87) · [Polynomial-Time Pseudodeterministic Construction of Primes](https://doi.org/10.1145/3803408)
Existing status: `open` · Summary written: 2026-09-12

## Parameterized complexity and algorithms (37)

### TCS-6592 — FPT versus \(\mathrm{W}[1]\)

A k-clique is a set of k graph vertices joined by every possible edge. The question asks for one exact deterministic algorithm whose input-size exponent is constant while a computable multiplier absorbs all dependence on k. Polynomial time separately for each fixed k does not establish that uniform bound. Clique completeness makes the question equivalent to FPT equalling W[1]. Conditional lower bounds and recent fixed-k or approximation results explain the conjecture’s significance without deciding it.

[Read in atlas](index.html#TCS-6592) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [On \(\mathrm{W}(1)\)-Hardness as Evidence for Intractability](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73) · [Constant Approximating k-Clique is \(\mathrm{W}(1)\)-hard](https://arxiv.org/abs/2102.04769) · [Simple Combinatorial Construction of the \(k^{o(1)}\)-Lower Bound for Approximating the Parameterized k-Clique](https://arxiv.org/abs/2304.07516) · [Faster Combinatorial k-Clique Algorithms](https://weizmann.elsevierpure.com/en/publications/faster-combinatorial-k-clique-algorithms-2/)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6593 — Exponential Time Hypothesis

ETH asks whether the optimal deterministic exponential rate for 3-SAT is strictly positive. The exponential parameter is the number of distinct variables, while polynomial factors account for the complete encoded input. One positive rate must obstruct every algorithm, and refutation permits different algorithms for arbitrarily small positive rates. Known exponential-time algorithms provide upper bounds but no positive lower bound on the optimum. The hypothesis supports quantitative lower bounds throughout exact and parameterized algorithms without being established by those conditional consequences.

[Read in atlas](index.html#TCS-6593) · [On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf) · [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) · [Exact Complexity and Satisfiability](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2013_ipec.pdf) · [Chain, Generalization of Covering Code, and Deterministic Algorithm for k-SAT](https://arxiv.org/abs/1804.07901) · [Mind the Gap? Not for SVP Hardness Under ETH!](https://doi.org/10.4230/LIPIcs.ICALP.2026.8)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7233 — Breaking the \(2^{n}\) barrier for weighted TSP

Exact weighted TSP asks for a cheapest tour through every vertex of a complete undirected graph. This question seeks a uniform classical algorithm with a fixed exponential time base below two. Weights are arbitrary nonnegative integers written in binary, and only polynomial dependence on their total encoding length is allowed. Bounded-error randomization and exponential memory are permitted, but every execution must satisfy the stated worst-case clock. Recent prefactor, structured-weight, time-space and quantum improvements do not establish the full classical guarantee.

[Read in atlas](index.html#TCS-7233) · [TSP Escapes the \(O(2^n n^2)\) Curse](https://arxiv.org/abs/2405.03018v2) · [Determinant Sums for Undirected Hamiltonicity](https://arxiv.org/abs/1008.0541) · [Mind the Gap. Doubling Constant Parametrization of Weighted Problems: TSP, Max-Cut, and More](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.79) · [Improved space-time tradeoff for TSP via extremal set systems](https://arxiv.org/abs/2604.05645) · [Optimal chain density, entropy, and space-time tradeoffs for the TSP](https://arxiv.org/abs/2607.11311) · [Quantum Space–Time Tradeoffs for TSP via Extremal Set Systems](https://arxiv.org/abs/2607.12374) · [Quantum Time-Space Tradeoffs for Exponential Dynamic Programming](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.37) · [A Near-Complete Resolution of the Exponential-Time Complexity of \(k\)-opt for the Traveling Salesman Problem](https://epubs.siam.org/doi/10.1137/1.9781611978971.208)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6594 — Set Cover conjecture

Set Cover asks whether a few supplied sets can cover a given universe. The conjecture concerns exact algorithms when each available set has a fixed maximum size. It says that no constant improvement over exponential base two works across all such size bounds. The target allows bounded-error randomization and polynomial factors that depend on the fixed bound. Recent results show that a major conjecture about tensor rank would refute SCC, but neither side is settled unconditionally.

[Read in atlas](index.html#TCS-6594) · [Fundamental Problems on Bounded-Treewidth Graphs: The Real Source of Hardness](https://doi.org/10.4230/LIPIcs.ICALP.2024.34) · [On Problems as Hard as CNF-SAT](https://arxiv.org/abs/1112.2275) · [The Asymptotic Rank Conjecture and the Set Cover Conjecture Are Not Both True](https://arxiv.org/abs/2310.11926) · [A Stronger Connection between the Asymptotic Rank Conjecture and the Set Cover Conjecture](https://arxiv.org/abs/2311.02774)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7241 — FPT approximation of twin-width

Twin-width measures how many mixed adjacency relations arise while vertex groups are merged. The desired algorithm receives a graph and a proposed width bound without an accompanying structural certificate. It must either reject that bound correctly or return a complete merge sequence whose width is bounded by a computable function of the parameter. Its running time may depend arbitrarily on the parameter but has one fixed polynomial exponent in the graph size. A complete Lean-checked resolution would settle whether these structural certificates are accessible in general fixed-parameter time.

[Read in atlas](index.html#TCS-7241) · [Open problems in twin-width](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) · [Twin-width one](https://arxiv.org/abs/2501.00991v1) · [Computing Twin-Width via Treedepth and Vertex Integrity](https://arxiv.org/abs/2606.20331v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6660 — Polynomial kernel for Edge Multiway Cut

Edge Multiway Cut removes a small number of edges so that no two designated terminals remain connected. The question asks whether polynomial-time preprocessing can reduce any instance to an equivalent instance of size polynomial in the deletion budget alone. The number of terminals is unrestricted, and the size exponent must not depend on it. Randomized preprocessing is allowed with a per-instance equivalence guarantee of at least two thirds. Known fixed-terminal kernels and quasipolynomial-size kernels leave the unrestricted polynomial-size target open in the checked sources.

[Read in atlas](index.html#TCS-6660) · [Quasipolynomial multicut-mimicking networks and kernels for multiway cut problems](https://arxiv.org/abs/2002.08825v3) · [Quasipolynomial-Time Deterministic Kernelization and (Gammoid) Representation](https://doi.org/10.4230/LIPIcs.MFCS.2025.54)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-4790 — Subset Sum below the meet-in-the-middle exponent

Subset Sum asks whether some subcollection of given positive integers adds to a target. The classical worst-case benchmark comes from the meet-in-the-middle exponent. The question asks for a fixed positive saving in that exponent with polynomial dependence on binary input length. Bounded-error classical randomization is allowed, with no random-instance promise. Quantum, pseudopolynomial and polynomial-factor improvements do not establish this fixed exponent saving.

[Read in atlas](index.html#TCS-4790) · [Subset Sum Quantumly in \(1.17^{n}\)](https://doi.org/10.4230/LIPIcs.TQC.2018.5) · [Derandomizing Pseudopolynomial Algorithms for Subset Sum](https://arxiv.org/abs/2601.01390)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6731 — Strictness of the W-hierarchy

The W-hierarchy groups parameterized decision problems by reductions to exact-weight satisfiability for restricted Boolean circuits. The question asks whether each positive level is strictly contained in the next. The circuit depth is fixed for each target problem, and reductions may spend arbitrary computable time in the parameter times a fixed polynomial in input length. Independent Set and Dominating Set illustrate the first two levels, whose known completeness does not itself separate them. A solution must prove all adjacent separations or prove equality at one particular adjacent pair; oracle-based evidence is insufficient.

[Read in atlas](index.html#TCS-6731) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf) · [On W(1)-Hardness as Evidence for Intractability](https://arxiv.org/abs/1712.05766v3)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6974 — General Formula-SAT with a fixed exponential saving

The input is any explicit Boolean formula tree, and the task is to decide exactly whether some assignment satisfies it. The time target is 2^((1-epsilon)n) times a fixed polynomial in the full formula length, for some fixed positive epsilon. One uniform deterministic algorithm must work for all sizes, depths and variable-occurrence patterns. Known faster algorithms for restricted-size formulas do not provide this full guarantee, and a positive answer would refute deterministic SETH. A complete Lean-checked proof or unconditional refutation is required; the precise saving is an editorial specification of the source’s qualitative question.

[Read in atlas](index.html#TCS-6974) · [The Status of the P versus NP Problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf) · [#SAT Algorithms from Shrinkage](https://eccc.weizmann.ac.il/report/2015/114/) · [Towards Stronger Depth Lower Bounds](https://doi.org/10.4230/LIPIcs.ITCS.2024.10)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7035 — Single-exponential Directed Feedback Vertex Set

A directed feedback vertex set meets every directed cycle by deleting its vertices. The question asks for an exact deterministic algorithm with a fixed exponential base in the allowed number of deletions. The remaining dependence on graph size must be polynomial with an exponent independent of the deletion budget. Known fixed-parameter algorithms retain a factorial-scale parameter cost, including the checked SOSA 2025 improvement. This card targets arbitrary digraphs, while the survey’s planar restriction and structural-parameter results remain distinct.

[Read in atlas](index.html#TCS-7035) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867v2) · [A Simplified Parameterized Algorithm for Directed Feedback Vertex Set](https://doi.org/10.1137/1.9781611978315.29) · [Data reduction for directed feedback vertex set on graphs without long induced cycles](https://doi.org/10.1007/s00236-025-00490-2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7181 — Exact recognition of bounded clique-width

Clique-width measures how many reusable vertex labels are needed to build a graph with four specified operations. Even a complete graph of arbitrary size needs only two labels. The question asks whether graphs of width at most k can be recognized in polynomial time for every fixed k. The polynomial exponent may depend on k, so known NP-completeness when k is input does not settle it. Small thresholds are understood, while approximate or supplied decompositions do not give exact recognition at every threshold.

[Read in atlas](index.html#TCS-7181) · [Clique-width is NP-complete](https://doi.org/10.1137/070687256) · [Polynomial-time recognition of clique-width \(\le 3\) graphs](https://doi.org/10.1016/j.dam.2011.03.020) · [Tight Bounds for Feedback Vertex Set Parameterized by Clique-Width](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.39)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7247 — Independent set algorithms from tropical circuit size

A tropical circuit combines vertex weights using only maximum and addition. For each graph, its minimum circuit size measures how compactly maximum independent-set weight can be represented for every nonnegative weight assignment. The question asks for one deterministic algorithm whose bit cost is polynomial in that circuit size and the input parameters. The algorithm receives only the graph and weights, and may use unrestricted computation to output the exact optimum value. The known construction for restricted graph classes leaves the author’s general polynomial-automatization question open in the sources checked.

[Read in atlas](index.html#TCS-7247) · [Lower Bounds on Dynamic Programming for Maximum Weight Independent Set](https://arxiv.org/abs/2102.06901v2) · [Open problems: Can dynamic programming for independent set be automated?](https://tuukkakorhonen.com/problems.html)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7312 — Fixed-parameter tractability of graph isomorphism by rank-width

Rank-width measures the ranks of adjacency cuts in an optimally chosen decomposition tree. Graph isomorphism asks whether a bijection of vertices preserves all edges. This card asks for one deterministic algorithm whose polynomial exponent is independent of the rank-width. The parameter-dependent multiplier may be any total computable function, and no decomposition is supplied. Known fixed-width polynomial algorithms and faster decomposition methods do not by themselves give the required uniform isomorphism bound.

[Read in atlas](index.html#TCS-7312) · [Parameterized complexity of graph isomorphism testing](https://epub.uni-regensburg.de/78630/1/1-s2.0-S1574013726000274-main.pdf) · [Canonisation and Definability for Graphs of Bounded Rank Width](https://arxiv.org/abs/1901.10330v2) · [Canonizing Graphs of Bounded Rank-Width in Parallel via Weisfeiler–Leman](https://doi.org/10.4230/LIPIcs.SWAT.2024.32) · [Branch-width of connectivity functions is fixed-parameter tractable](https://arxiv.org/abs/2601.04756v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6734 — Polynomial compression versus polynomial kernelization

A polynomial compression replaces an instance by a short string for a possibly different decision language. A polynomial kernel must instead return a short equivalent instance of the original parameterized problem. The selected question asks for an NP-complete unary source language with deterministic polynomial compression but a conditional obstruction to polynomial kernels. The obstruction must show that any such kernel would put every NP language in coNP with polynomial advice. The compression is unconditional, its target language is unrestricted, and the original informal naturalness requirement is replaced by the user-selected precise source class.

[Read in atlas](index.html#TCS-6734) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf) · [Kernelization: Theory of Parameterized Preprocessing](https://fedorvf.github.io/BookKer/book_kernels.pdf) · [Abusing the Tutte Matrix: An Algebraic Instance Compression for the K-set-cycle Problem](https://doi.org/10.4230/LIPIcs.STACS.2013.341) · [Preprocessing Complexity for Some Graph Problems Parameterized by Structural Parameters](https://arxiv.org/abs/2306.12655v1) · [Boundaried Kernelization via Representative Sets](https://doi.org/10.4230/LIPIcs.IPEC.2025.6)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6814 — Job-shop approximation parameterized only by machines and accuracy

Each job is a prescribed sequence of nonpreemptive operations on specified machines, with repeated machine visits allowed. The objective is to finish all jobs within a factor arbitrarily close to the optimum makespan. The requested running time is a fixed polynomial in the complete input length times a computable function of machine count and accuracy. Known schemes use the additional parameter of maximum operations per job, which must be removed here. A complete Lean-checked answer must establish or refute this uniform approximation scheme for arbitrarily long job routes.

[Read in atlas](index.html#TCS-6814) · [Parameterized complexity of machine scheduling: 15 open problems](https://arxiv.org/abs/1709.01670v3) · [Makespan Minimization in Job Shops: A Linear Time Approximation Scheme](https://doi.org/10.1137/S0895480199363908)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-4289 — \(\mathrm{W}[2]\)-hardness of bounded-VC-dimension Hitting Set

Hitting Set asks whether at most k elements can intersect every set in an explicitly supplied finite set system. The question is whether some fixed bound on the system's VC dimension still permits W[2]-hardness when only k is the parameter. Hardness means one uniform deterministic fixed-parameter many-one reduction from unrestricted Hitting Set, with every output satisfying that fixed VC bound. The 2016 source proves W[1]-hardness even when primal and dual dimensions are both two, but leaves the stronger W[2] classification open. The bounded review through September 2026 found related hardness and approximation results but no verified resolution of this question.

[Read in atlas](index.html#TCS-4289) · [Hitting Set for Hypergraphs of Low VC-dimension](https://doi.org/10.4230/LIPIcs.ESA.2016.23) · [The PACE 2025 Parameterized Algorithms and Computational Experiments Challenge: Dominating Set and Hitting Set](https://doi.org/10.4230/LIPIcs.IPEC.2025.32) · [The Parameterized Complexity of Independent Set and More when Excluding a Half-Graph, Co-Matching, or Matching](https://arxiv.org/abs/2602.07606v1) · [Fixed Budget vs. Covering Target: The Partial Set Cover Boundary for Bounded VC-Dimension](https://arxiv.org/abs/2608.03801v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6728 — Chromatic number in \(2^{n}\) time and polynomial space

The chromatic number is the minimum number of colors needed so that adjacent vertices receive different colors. The question asks for one deterministic algorithm computing it on every graph in base-two exponential time up to polynomial factors. The same algorithm must use only polynomially many bits of working memory. Known algorithms separately achieve base-two time with exponential memory or polynomial memory with a larger time base. Recent randomized algorithms for each fixed color count and improved exponential-space bounds do not meet the complete target.

[Read in atlas](index.html#TCS-6728) · [Parameterized Algorithms](https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf) · [Faster Graph Coloring in Polynomial Space](https://link.springer.com/article/10.1007/s00453-022-01034-7) · [A space improved algorithm for chromatic number](https://doi.org/10.1016/j.tcs.2025.115584) · [k-Coloring is Faster than Computing the Chromatic Number](https://arxiv.org/abs/2607.25973v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7022 — Polynomial kernel for Planar Edge Deletion

Planar Edge Deletion asks whether at most k edges can be removed from an arbitrary graph to make it planar. The question is whether deterministic polynomial-time preprocessing always produces one equivalent instance whose total size is polynomial in k. Both the deletion budget and the complete output encoding are bounded, with no randomness, approximation or oracle queries. Fixed-parameter algorithms and approximate vertex-deletion kernels have different guarantees and do not settle this exact edge problem. A complete Lean answer must establish such a uniform kernel or prove that every deterministic polynomial-time exact preprocessor fails a polynomial size bound.

[Read in atlas](index.html#TCS-7022) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867v2) · [A survey of parameterized algorithms and the complexity of edge modification](https://fedorvf.github.io/articles/2023/2023e.pdf) · [A Unified FPT Framework for Crossing Number Problems](https://arxiv.org/abs/2410.00206v4) · [Kernelization Dichotomies for Hitting Minors Under Structural Parameterizations](https://doi.org/10.4230/LIPIcs.STACS.2026.17)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3480 — Polynomial exact metric sparsifiers with a crossing-edge budget

A graph with terminals is queried by choosing labels for the terminals and a metric on the labels. The goal is a small retained edge set that supports an optimal extension for every such query. Only labelings with at most p crossing edges are compared, and the retained set must have size polynomial in p plus the number of terminals. The original claimed quasipolynomial metric-sparsifier result was explicitly retracted in the corrected paper. Ordinary multicut sparsifiers preserve a different collection of values and do not settle this universal metric question.

[Read in atlas](index.html#TCS-3480) · [On Quasipolynomial Multicut-Mimicking Networks and Kernelization of Multiway Cut Problems](https://doi.org/10.4230/LIPIcs.ICALP.2020.101) · [Quasipolynomial multicut-mimicking networks and kernelization of multiway cut problems — corrected full version](https://arxiv.org/abs/2002.08825v3) · [Quasipolynomial Multicut-mimicking Networks and Kernels for Multiway Cut Problems](https://doi.org/10.1145/3501304) · [Approximating Small Sparse Cuts](https://arxiv.org/abs/2403.08983)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-6749 — Deterministic polynomial kernels for Almost 2-SAT

Almost 2-SAT asks whether deleting at most a specified number of clauses can make a Boolean formula with at most two literals per clause satisfiable. The question asks for deterministic polynomial-time preprocessing that replaces any instance by an equivalent smaller instance of the same problem. The complete output size must be bounded by a fixed polynomial in the deletion budget alone. Randomized polynomial kernels are known, and a 2025 result obtains deterministic polynomial-size kernels with quasipolynomial preprocessing time. The remaining target requires both polynomial time and polynomial output size, with exact correctness for every input.

[Read in atlas](index.html#TCS-6749) · [Parameterized Constraint Satisfaction Problems: a Survey](https://drops.dagstuhl.de/entities/document/10.4230/DFU.Vol7.15301.179) · [Quasipolynomial-Time Deterministic Kernelization and (Gammoid) Representation](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.54)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7027 — Fixed-parameter tractability of Perfect Edge Deletion

A graph is perfect if every induced subgraph needs exactly as many colors as the size of its largest clique. The problem asks whether at most a given number of edges can be deleted to make an arbitrary graph perfect. The desired algorithm has a polynomial input-size exponent independent of that deletion budget, with a computable budget-dependent factor. The source concerns edge deletion, whereas the known parameterized hardness concerns deleting vertices. The question remains open in the checked survey, and recent work on essential vertices does not resolve this edge-deletion target.

[Read in atlas](index.html#TCS-7027) · [A survey of parameterized algorithms and the complexity of edge modification](https://doi.org/10.1016/j.cosrev.2023.100556) · [Parameterized complexity of vertex deletion into perfect graph classes](https://doi.org/10.1016/j.tcs.2012.03.013) · [Search-space reduction via essential vertices revisited: Vertex multicut and cograph deletion](https://doi.org/10.1016/j.jcss.2025.103730)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1945 — Tight ETH lower bounds for binary Nearest Codeword at every constant factor

Nearest Codeword asks how many bits separate a target from the nearest word in a binary linear code. The parameter k is the promised upper bound on that distance in yes instances. The target excludes time f(k) times an input-size power whose exponent grows slower than k. This lower bound must follow from ordinary deterministic ETH for every fixed approximation factor greater than one. A May 2026 result handles some constant factor, while its stated all-factor extension remains the selected question.

[Read in atlas](index.html#TCS-1945) · [Improved Lower Bounds for Approximating Parameterized Nearest Codeword and Related Problems Under ETH](https://doi.org/10.4230/LIPIcs.ICALP.2024.107) · [Tight Lower Bound for Approximating Parametrized Maximum Likelihood Decoding under ETH](https://arxiv.org/abs/2605.08797)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-7023 — Polynomial kernels for minor-free edge deletion

The problem deletes at most k edges so that the remaining graph excludes every member of a fixed forbidden-minor family. It asks whether every such family permits a polynomial-time reduction to one equivalent instance of polynomial size in k. The input graph is arbitrary, and all vertices remain available during edge deletion. A general kernel would provide a broad preprocessing guarantee for structural graph repair beyond known fixed-parameter algorithms. The card restores the family quantifier and distinguishes vertex deletion, promised minor-free inputs and more general compressions.

[Read in atlas](index.html#TCS-7023) · [A Survey of Parameterized Algorithms and the Complexity of Edge Modification](https://arxiv.org/abs/2001.06867v2) · [A survey of parameterized algorithms and the complexity of edge modification](https://fedorvf.github.io/articles/2023/2023e.pdf) · [Robust Contraction Decomposition for Minor-Free Graphs and Its Applications](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.17/LIPIcs.ICALP.2025.17.html)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0787 — ETH barrier to single-exponential treewidth computation

Treewidth is the smallest maximum bag size minus one among tree decompositions of a graph. The target asks whether ETH rules out exact decision in single-exponential time in the requested width and polynomial time in graph size. The algorithm must handle every input without receiving a decomposition or a promise that the width threshold is met. Resolving the question would clarify the cost of discovering the structural information used by many parameterized algorithms. The new exponential lower bound in the number of vertices is recorded separately because it does not exclude the requested parameter dependence.

[Read in atlas](index.html#TCS-0787) · [Optimality and Tight Results in Parameterized Complexity (Dagstuhl Seminar 14451)](https://doi.org/10.4230/DagRep.4.11.1) · [An Improved Parameterized Algorithm for Treewidth](https://arxiv.org/abs/2211.07154v2) · [Treewidth Inapproximability and Tight ETH Lower Bound](https://arxiv.org/abs/2406.11628v2) · [Treewidth Inapproximability and Tight ETH Lower Bound](https://doi.org/10.1145/3833387)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0801 — Directed Hamiltonicity

The question asks for a randomized test for a Hamiltonian cycle in every finite loopless directed graph. Its running time must be O(c^n) for one fixed c below two, as explicitly selected by the user. Success must be at least two thirds on each input, and the stated RAM time bound must hold on every random tape. The 2026 exact-counting improvement saves only a sublinear term in the exponent, while the September fixed-base improvement concerns parity alone. A complete Lean-checked solution must establish the full unrestricted detection guarantee or refute it; restricted graphs and modular counts do not finish the target.

[Read in atlas](index.html#TCS-0801) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time — Directed Hamiltonicity](https://doi.org/10.4230/DagRep.3.8.40) · [Directed Hamiltonicity and Out-Branchings via Generalized Laplacians](https://arxiv.org/abs/1607.04002v2) · [Counting Perfect Matchings and Hamiltonian Cycles Faster](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.138) · [A Deterministic \(O^*((3/2)^n)\) Algorithm for the Parity of Directed Hamiltonian Cycles](https://arxiv.org/abs/2609.11982v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0816 — Sub-base-two exact shortest common superstring

Shortest common superstring asks for a shortest string containing every input string as a contiguous substring. The parameter \(n\) counts input strings, while their full encoded lengths contribute only a fixed polynomial factor to running time. The question asks for a uniform deterministic classical algorithm running in \(O^*((2-\varepsilon)^n)\) time for some fixed \(\varepsilon>0\). Any constant improvement below base two qualifies, with unrestricted string lengths and alphabets and an exactly optimal output. Faster algorithms for bounded-length strings, quantum speedups and approximation advances concern different guarantees.

[Read in atlas](index.html#TCS-0816) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40) · [Solving SCS for bounded length strings in fewer than \(2^n\) steps](https://golovnev.org/papers/scs_exact.pdf) · [Collapsing Superstring Conjecture](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.26) · [Quantum Algorithm for the Shortest Superstring Problem](https://arxiv.org/abs/2112.13319v1) · [A Tight Cycle-Cover Inequality for Shortest Common Superstring](https://eccc.weizmann.ac.il/report/2026/157/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0800 — Cutwidth

The cutwidth of a graph is the smallest possible maximum number of edges crossing a boundary between consecutive vertices in a linear ordering. The question asks for one deterministic algorithm computing this value on every graph in exponential time with a fixed base below two. The running-time exponent is measured in the number of vertices, with no promise about a smaller structural parameter. Faster exact algorithms for bipartite graphs and for graphs with a small vertex cover do not meet the unrestricted target. The checked 2025 progress gives a faster factor-two approximation, which does not determine the exact optimum.

[Read in atlas](index.html#TCS-0800) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.3.8.40) · [On Cutwidth Parameterized by Vertex Cover](https://link.springer.com/article/10.1007/s00453-012-9707-6) · [Exponential-Time Approximation (Schemes) for Vertex-Ordering Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.15)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0808 — Sub-base-two exact maximum acyclic subgraph

Maximum acyclic subgraph retains as many arcs of a directed graph as possible without retaining a directed cycle. The source question asks for an exact algorithm whose running time has a fixed exponential base below two in the number of vertices. The card specifies deterministic bit complexity, arbitrary unweighted directed graphs and an actual optimum arc set as output. Known parameterized and approximation results do not automatically improve that worst-case vertex-count bound. A resolution would clarify whether this basic precedence-ordering problem can beat the longstanding base-two exact-algorithm benchmark.

[Read in atlas](index.html#TCS-0808) · [Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40) · [A Note on Exact Algorithms for Vertex Ordering Problems on Graphs](https://doi.org/10.1007/s00224-011-9312-0) · [Exploiting Spanning Trees for Directed Acyclicity](https://arxiv.org/abs/2607.07705v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0597 — Fixed-parameter tractability of coloring graphs with no induced P5

A graph is P5-free when no five vertices induce precisely a path. The input asks whether such a graph can be colored with at most k colors. The target is one deterministic algorithm with running time f(k) times a polynomial in the graph size. The polynomial exponent must be independent of the number of colors. Existing polynomial algorithms for each separately fixed k leave this stronger parameterized question open in the checked sources.

[Read in atlas](index.html#TCS-0597) · [Graph Colouring: from Structure to Algorithms (Dagstuhl Seminar 19271)](https://doi.org/10.4230/DagRep.9.6.125) · [Vertex Partitioning in Graphs: From Structure to Algorithms (Dagstuhl Seminar 22481)](https://doi.org/10.4230/DagRep.12.11.109)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0799 — Converting CNF to DNF

For each variable count n and clause width k, the target is the largest minimum number of DNF terms needed to represent an n-variable k-CNF function. The DNF must agree on every assignment using the same variables, while its terms may overlap and may have arbitrary width. The source leaves a gap between exponential upper and lower bounds, and later improvements for monotone formulas do not determine the general case. The card explicitly extends that asymptotic question to a real-valued description of the extremal function within one hundredth of a term at every admissible pair. A complete Lean proof must certify the universal upper and extremal lower bounds, thereby identifying the inherent representation cost rather than a conversion algorithm’s running time.

[Read in atlas](index.html#TCS-0799) · [Converting CNF to DNF, in Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time](https://doi.org/10.4230/DagRep.3.8.40) · [On converting CNF to DNF: BRICS RS-03-45](https://www.brics.dk/RS/03/45/BRICS-RS-03-45.pdf) · [On converting CNF to DNF](https://doi.org/10.1016/j.tcs.2005.07.029) · [A Generalization of the Satisfiability Coding Lemma and Its Applications](https://doi.org/10.4230/LIPIcs.SAT.2022.9) · [A Formalization of the Exponential Blowup in the Transformations between CNF and DNF](https://isa-afp.org/entries/CNF_DNF_Exp_Blowup.html)
Existing status: `source_open` · Summary written: 2026-09-16

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

### TCS-4440 — Expected FPT delay from small-witness decision

A self-contained witness is a k-element subset whose validity survives restriction to any universe containing it. An FPT decision algorithm can therefore test whether a chosen subset contains a witness. The selected question asks whether this always yields exact enumeration with expected FPT time between outputs, including startup and termination. The source already controls expected total work but leaves the stronger delay guarantee open. Incremental time, deterministic delay and enumeration with possible omissions are separate variants.

[Read in atlas](index.html#TCS-4440) · [Randomised Enumeration of Small Witnesses Using a Decision Oracle](https://doi.org/10.4230/LIPIcs.IPEC.2016.22) · [Randomised Enumeration of Small Witnesses Using a Decision Oracle](https://doi.org/10.1007/s00453-018-0404-y)
Existing status: `open` · Summary written: 2026-09-12

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

## Approximation algorithms and inapproximability (29)

### TCS-6587 — Constant-factor approximation for Densest k-Subgraph

Densest k-Subgraph asks which exactly k vertices contain the most internal edges. The target is one deterministic polynomial-time algorithm that always returns a k-set within one universal constant of optimum. The card fixes explicit graph encoding, bit cost, output cardinality and a guarantee on every input. ETH already excludes this guarantee conditionally, while ordinary NP-hardness of even a 1.001 approximation remains absent in the inspected 2026 source. Recent continuous-optimization and at-least-k density results address different guarantees and do not resolve this target.

[Read in atlas](index.html#TCS-6587) · [Detecting High Log-Densities — an \(O(n^{1/4})\) Approximation for Densest k-Subgraph](https://arxiv.org/abs/1001.2891) · [Polynomial integrality gaps for strong SDP relaxations of Densest k-subgraph](https://arxiv.org/abs/1110.1360) · [Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph](https://arxiv.org/abs/1611.05991) · [A New Conjecture on Hardness of 2-CSP’s with Implications to Hardness of Densest k-Subgraph and Other Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38) · [Sum-of-Squares Lower Bounds for Densest k-Subgraph](https://arxiv.org/abs/2303.17506) · [A Scalable and Exact Relaxation for Densest k-Subgraph via Error Bounds](https://ojs.aaai.org/index.php/AAAI/article/view/38562) · [A Note on Approximability of Densest At-Least-k-Subgraph](https://arxiv.org/abs/2605.25464) · [A Linear-Time Approximation Scheme for the Densest Subgraph Problem](https://arxiv.org/abs/2608.11094)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0006 — Unique Games Conjecture

A Unique Games instance consists of explicitly listed vertices and permutation constraints between pairs of labels. UGC asks for NP-hardness of distinguishing almost completely satisfiable instances from those with arbitrarily small optimum value. The alphabet and deterministic reduction may depend on the fixed gap parameters, but must be independent of the growing input formula. A complete Lean proof must establish the full reduction statement or its negation over every alphabet and polynomial-time candidate reduction. The September 2026 perfect-completeness 4-to-1 claim and the known half-completeness Unique Games theorem do not establish this near-one-completeness permutation-constraint conjecture.

[Read in atlas](index.html#TCS-0006) · [On the Unique Games Conjecture](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf) · [Optimal Algorithms and Inapproximability Results for Every CSP?](https://www.cs.cornell.edu/~abrahao/tdg/papers/p245.pdf) · [Subexponential Algorithms for Unique Games and Related Problems](https://www.boazbarak.org/Papers/ssesubexp.pdf) · [On the Proof of the 2-to-2 Games Conjecture](https://cs.nyu.edu/~khot/PCP-Spring-20/2-to-2-Exposition.pdf) · [Towards a Proof of the 2-to-1 Games Conjecture?](https://theoryofcomputing.org/articles/v021a011/) · [Tolerant Testing for Unique Games](https://arxiv.org/abs/2605.17760) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6588 — Polylogarithmic approximation for Directed Steiner Tree

Directed Steiner Tree seeks a minimum-cost directed subgraph connecting one root to every designated terminal. The target is one uniform randomized algorithm with a fixed polynomial bit running time and a fixed polylogarithmic approximation factor in the number of terminals. Every output must be feasible, and each input must achieve the cost guarantee with probability at least two thirds, including instances with zero optimum. A complete Lean proof must establish those guarantees or rule out all permitted randomized algorithms and all fixed logarithmic powers. The September 2026 published literature still leaves this general problem open; planar algorithms, quasipolynomial results and the corrected fractional-solution claim have additional restrictions.

[Read in atlas](index.html#TCS-6588) · [Approximation Algorithms for Directed Steiner Problems](https://chekuri.web.engr.illinois.edu/pub.html) · [\(O(\log ^{2} k/\log  \log  k)\)-Approximation Algorithm for Directed Steiner Tree: A Tight Quasi-Polynomial-Time Algorithm](https://people.idsia.ch/~grandoni/Pubblicazioni/GLL19stoc.pdf) · [An \(O(\log  k)\)-Approximation for Directed Steiner Tree in Planar Graphs](https://arxiv.org/abs/2302.04747) · [From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.42) · [On the Integrality Gap of Directed Steiner Tree LPs with Relatively Integral Solutions](https://arxiv.org/abs/2412.10744) · [Length-Constrained Network Design in Planar Digraphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.15)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7160 — Small-Set Expansion Hypothesis

Is it NP-hard to distinguish one poorly expanding small set from uniformly strong expansion at the same set size? The target set occupies a fixed fraction \(\delta\) of the graph, with \(\delta\) chosen after the gap parameter \(\eta\). Expansion is the fraction of incident edges that leave the set. A sparse cut of a larger size does not necessarily reveal any poorly expanding set of the target size. Known reductions connect the hypothesis to Unique Games and conditional hardness without resolving it.

[Read in atlas](index.html#TCS-7160) · [Graph Expansion and the Unique Games Conjecture](https://www.dsteurer.org/paper/expansion.pdf) · [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586) · [The Condition-Number Barrier in Sparse Least Squares](https://arxiv.org/abs/2608.02588)
Existing status: `open` · Summary written: 2026-09-11

### TCS-6589 — Subtour-LP integrality gap for metric TSP

The metric traveling-salesperson problem asks for a cheapest tour through all vertices. Its subtour linear program permits fractional edges while retaining degree and connectivity constraints. The target is the supremum of the tour optimum divided by the LP optimum over every finite symmetric metric. The four-thirds conjecture proposes an exact value, but this benchmark accepts absolute error at most 1/100. A complete Lean-checked answer must control the unrestricted supremum from both sides, without assuming it is attained or restricting the number of vertices.

[Read in atlas](index.html#TCS-6589) · [Maximum Entropy is a \(10/7\)-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances](https://arxiv.org/abs/2607.01536v2) · [A (Slightly) Improved Bound on the Integrality Gap of the Subtour LP for TSP](https://arxiv.org/abs/2105.10043v3) · [From Trees to Polynomials and Back Again: New Capacity Bounds with Applications to TSP](https://arxiv.org/abs/2311.09072v2) · [Extending Exact Integrality Gap Computations for the Metric TSP](https://arxiv.org/abs/2603.12995v5) · [A Sharper Explicit Bound on the Subtour-LP Integrality Gap for Metric TSP](https://www.preprints.org/manuscript/202609.0140/v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6659 — Breaking two for metric k-Median

Metric k-Median selects at most \(k\) supplied facilities and minimizes the sum of distances from clients to their nearest selected facility. The question asks for a uniform randomized polynomial-time approximation with factor \(2-\varepsilon\) for some fixed \(\varepsilon>0\). Every execution must return a feasible set within polynomial bit time, and the cost guarantee must hold with probability at least two thirds on each input. The same improvement must apply to all facility budgets and arbitrary finite rational metrics, however small the chosen positive constant is. Algorithms approaching two from above and the standard LP's gap approaching two do not supply such a strict improvement.

[Read in atlas](index.html#TCS-6659) · [A \((2+\varepsilon )\)-Approximation Algorithm for Metric k-Median](https://arxiv.org/abs/2503.10972) · [A threshold of ln n for approximating set cover](https://courses.cs.duke.edu/cps296.2/spring07/papers/p634-feige.pdf) · [A new greedy approach for facility location problems](https://cgi.di.uoa.gr/~vassilis/co/co-papers/jain02.pdf) · [Tight FPT Approximations for k-Median and k-Means](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.42) · [Almost-Optimal Upper and Lower Bounds for Clustering in Low Dimensional Euclidean Spaces](https://arxiv.org/abs/2603.09846) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654) · [\(k\)-Clustering via Iterative Randomized Rounding](https://arxiv.org/abs/2604.06046)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7282 — Vertex Cover approximation below factor two

A vertex cover selects at least one endpoint of every edge of a finite simple undirected graph. The problem asks whether one deterministic polynomial-time algorithm always finds a cover within a fixed factor strictly below two of the minimum size. The positive improvement must be independent of graph size, and the output and worst-case bit-time guarantees apply to every explicitly listed graph, including edgeless ones. A complete Lean proof must establish such an algorithm or unconditionally rule out every polynomial-time candidate, rather than assume an unproved hardness hypothesis. Known vanishing improvements, Unique-Games-based hardness, recent hypergraph results and the checked heuristic claims do not provide the required unconditional fixed-gap resolution.

[Read in atlas](index.html#TCS-7282) · [The Primal-Dual Schema for Approximation Algorithms: Where Does It Stand, and Where Can It Go?](https://algo.inria.fr/seminars/sem00-01/vazirani.html) · [A better approximation ratio for the Vertex Cover problem](https://www.cas.mcmaster.ca/~gk/papers/vc.pdf) · [Vertex Cover Might be Hard to Approximate to within \(2-\varepsilon\)](https://cims.nyu.edu/~regev/papers/vc_hard.pdf) · [On Independent Sets, 2-to-2 Games and Grassmann Graphs](https://theoryofcomputing.org/articles/v021a010/) · [An Approximate Solution to the Minimum Vertex Cover Problem: The Salvador Algorithm](https://www.preprints.org/manuscript/202605.2000/v3) · [An Approximate Solution to the Minimum Vertex Cover Problem: The Hallelujah Algorithm](https://www.preprints.org/manuscript/202510.2392/v2) · [Improved Multilayered PCPs and Hypergraph Vertex Cover](https://arxiv.org/abs/2609.06775) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5544 — Does a fixed d-to-1 Games conjecture imply Unique Games?

The question asks whether perfect-completeness d-to-one hardness for any fixed d implies the full Unique Games conjecture. Every game is an explicit finite classical constraint system, and hardness means deterministic polynomial reductions from Boolean satisfiability. Known direct conversion gives a fixed positive Unique Games completeness rather than a value arbitrarily close to one. A September 2026 preprint claims perfect-completeness four-to-one hardness, which would establish the antecedent if correct. The implication remains a separate target and, conditional on that theorem, is equivalent to proving full UGC.

[Read in atlas](index.html#TCS-5544) · [Near-Optimal UGC-hardness of Approximating Max \(k-\mathrm{CSP}_{R}\)](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.15) · [Towards a Proof of the 2-to-1 Games Conjecture?](https://theoryofcomputing.org/articles/v021a011/) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6590 — Subtour-LP integrality gap for asymmetric TSP

Asymmetric TSP finds a cheapest directed Hamiltonian tour in a directed metric. The subtour relaxation has fractional arcs with unit incoming and outgoing degree and at least one outgoing arc across each cut. The target is the supremum tour-to-LP ratio over all positive-LP finite instances. The familiar factor-two conjecture supplies one candidate for the value, and zero-LP metrics cause no division convention ambiguity. The Lean acceptance tolerance is absolute error 0.01 for the universal ratio.

[Read in atlas](index.html#TCS-6590) · [An Improved Approximation Algorithm for the Asymmetric Traveling Salesman Problem](https://epubs.siam.org/doi/10.1137/20M1339313) · [Approximation Algorithms for Traveling Salesman Problems](https://www.or.uni-bonn.de/tspbook/book.pdf) · [On the Integrality Gap of Small Asymmetric Traveling Salesman Problems: A Polyhedral and Computational Approach](https://arxiv.org/abs/2506.10671) · [The Cloven Traveling Salesman: Cycle Covers and the Integrality Gap of Small ATSP Instances](https://arxiv.org/abs/2511.05045v2)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7266 — Constant-factor approximation for uniform Sparsest Cut

Uniform Sparsest Cut minimizes the number of crossing edges divided by the number of separated vertex pairs. The input is an arbitrary explicitly given simple unweighted undirected graph. The question asks for one randomized polynomial-time algorithm returning a cut within an absolute constant factor of optimum. Success is required separately on every graph, including finding a zero-boundary cut with the required probability when the optimum is zero. A complete Lean-checked resolution must settle the all-graph algorithmic target rather than the performance of one relaxation or a special graph class.

[Read in atlas](index.html#TCS-7266) · [Lecture Notes on the ARV Algorithm for Sparsest Cut](https://arxiv.org/abs/1607.00854v1) · [A simpler and parallelizable O(√log n)-approximation algorithm for SPARSEST CUT](https://research-explorer.ista.ac.at/record/21007) · [Sparsest Cut and Eigenvalue Multiplicities on Low Degree Abelian Cayley Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2025.16) · [Integrality Gap Bounds for the Goemans-Linial SDP on Finite Abelian Cayley Graphs](https://arxiv.org/abs/2609.05368v1) · [Optimal Rounding for Sparsest Cut](https://doi.org/10.1145/3717823.3718285)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7281 — Unconditional NP-hardness at the Goemans–Williamson Max-Cut threshold

Max-Cut asks for a bipartition crossing as many edges of a graph as possible. The question asks for unconditional NP-hardness of approximation arbitrarily close to the Goemans–Williamson ratio. The requested proof must reduce every 3-SAT formula deterministically to a simple unweighted graph with a fixed satisfiable-versus-unsatisfiable gap. Matching known hardness uses Unique Games, while the checked newer cut results have different graph restrictions or objectives. A complete Lean-checked proof must establish the full reduction statement or its exact logical negation.

[Read in atlas](index.html#TCS-7281) · [Optimal Inapproximability Results for MAX-CUT and Other 2-Variable CSPs?](https://www.stat.berkeley.edu/~mossel/publications/max_cut_final.pdf) · [Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems Using Semidefinite Programming](https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf) · [Some optimal inapproximability results](https://people.kth.se/~johanh/optimalinap.pdf) · [Triangles Improve 0.878 Approximation for Maxcut](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2025.27) · [Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT](https://arxiv.org/abs/2608.00333v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7356 — Optimal polynomial-time approximation ratio for metric TSP

Metric TSP asks for a cheapest closed tour visiting every point in a finite metric. This card asks for the infimum of expected approximation ratios achieved by uniform randomized polynomial-time algorithms. All inputs are explicit rational metrics, every execution must finish in polynomial time, and every output must be a valid tour. Known improvements below three halves and conditional hardness results leave the unconditional optimal ratio undetermined. An answer needs a complete Lean-checked estimate within absolute error 1/100, controlling the algorithmic infimum on both sides.

[Read in atlas](index.html#TCS-7356) · [A (Slightly) Improved Approximation Algorithm for Metric TSP](https://arxiv.org/abs/2007.01409v6) · [New Inapproximability Bounds for TSP](https://arxiv.org/abs/1303.6437v2) · [A (Slightly) Improved Deterministic Approximation Algorithm for Metric TSP](https://arxiv.org/abs/2212.06296v1) · [From Trees to Polynomials and Back Again: New Capacity Bounds with Applications to TSP](https://arxiv.org/abs/2311.09072v2) · [Maximum Entropy is a \(10/7\)-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances](https://arxiv.org/abs/2607.01536v2) · [A Sharper Explicit Bound on the Subtour-LP Integrality Gap for Metric TSP](https://www.preprints.org/manuscript/202609.0140/v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6591 — Constant-factor approximation for Directed Feedback Vertex Set

A directed feedback vertex set deletes vertices so that no directed cycle remains. The question asks for one deterministic polynomial-time algorithm whose output weight is at most a fixed constant times the minimum possible weight. The guarantee must hold for every directed graph and every nonnegative rational assignment of vertex weights. General approximation remains polylogarithmic in the checked sources, and every constant factor faces a conditional Unique-Games hardness barrier. Recent constant-factor improvements apply to quasi-transitive digraphs and do not settle the unrestricted question.

[Read in atlas](index.html#TCS-6591) · [Polynomial Kernels for Deletion to Classes of Acyclic Digraphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.55) · [Hardness of Vertex Deletion and Project Scheduling](https://theoryofcomputing.org/articles/v009a024/) · [A 9/4-Approximation for Directed Feedback Vertex Sets in Quasi-Transitive Digraphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.96) · [A deterministic \((2+\varepsilon)\)-approximation for directed feedback vertex sets in tournaments](https://arxiv.org/abs/2609.16723v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7357 — Optimal polynomial-time approximation ratio for asymmetric TSP

An asymmetric metric TSP instance specifies positive rational directed distances and asks for a minimum-cost tour through all vertices. The target is the infimum of all expected approximation ratios achieved by uniform randomized algorithms that always return a tour and run in polynomial time on every execution. The algorithm and polynomial may depend on the ratio, and an algorithm attaining the infimum need not exist. Known constant-factor algorithms and conditional hardness results leave a substantial gap, even after the improvements reported in March 2026. The benchmark requires a supplied real estimate and a complete Lean proof of absolute error at most one hundredth for the unconditional constant.

[Read in atlas](index.html#TCS-7357) · [Better approximation guarantee for Asymmetric TSP](https://arxiv.org/abs/2603.14334v1) · [A Constant-Factor Approximation Algorithm for the Asymmetric Traveling Salesman Problem](https://arxiv.org/abs/1708.04215v4) · [New Inapproximability Bounds for TSP](https://www.lamsade.dauphine.fr/~mlampis/papers/TSP-ISAACj.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7380 — Better-than-two approximation for weighted 2ECSS

The task is to buy a minimum-cost spanning network that survives deletion of any single edge. Costs are arbitrary nonnegative rational numbers, and each input edge may be selected only once. The question asks for a deterministic polynomial-time approximation beating factor two by one fixed constant. Better unweighted and connectivity-augmentation guarantees concern different instance models. A solution would break a central barrier in approximation algorithms for survivable networks.

[Read in atlas](index.html#TCS-7380) · [A Better-Than-5/4-Approximation for Two-Edge Connectivity](https://arxiv.org/abs/2509.19655) · [A \((1.5+\varepsilon)\)-Approximation Algorithm for Weighted Connectivity Augmentation](https://arxiv.org/abs/2209.07860)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7353 — Optimal polynomial-time approximation ratio for Euclidean k-means

Euclidean k-means chooses k arbitrary centers to minimize the sum of squared distances from the input points. The dimension, number of clusters and rational coordinate lengths are all part of the input. The target is the infimum of expected ratios achievable by uniform randomized polynomial-time algorithms. The latest reviewed upper-bound improvement does not determine that unrestricted infimum. An accepted answer needs a complete Lean-checked value within 0.01, without silently assuming an unproved hardness hypothesis.

[Read in atlas](index.html#TCS-7353) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654v1) · [A (4 + epsilon)-Approximation for Euclidean k-Means via Non-Monotone Dual-Fitting](https://people.idsia.ch/~grandoni/Pubblicazioni/CCGGLW26stoc.pdf) · [Near-Optimal Bounds for Parameterized Euclidean k-Means](https://doi.org/10.4230/LIPIcs.SoCG.2026.33)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-5407 — Optimal approximation for nonmonotone submodular maximization over a matroid

The input is a nonnegative submodular set function and one matroid, accessed through exact value and independence oracles. The goal is to choose an independent set with a large objective value, even though adding elements can reduce that value. The target is the supremum of expected approximation factors achievable by a uniform randomized algorithm using polynomially many total oracle-model operations. The checked literature gives a 0.401 approximation and a 0.478 value-query barrier, with the general gap explicitly retained in a March 2026 source. A benchmark answer must determine that optimal real ratio within 1/100 and prove the claimed accuracy in Lean without assuming that the supremum is attained.

[Read in atlas](index.html#TCS-5407) · [On Maximizing Sums of Non-Monotone Submodular and Linear Functions](https://doi.org/10.4230/LIPIcs.ISAAC.2022.41) · [On Maximizing Sums of Non-monotone Submodular and Linear Functions](https://doi.org/10.1007/s00453-023-01183-3) · [Submodular Maximization by Simulated Annealing](https://theory.stanford.edu/~jvondrak/data/simulated-annealing.pdf) · [Constrained Submodular Maximization via New Bounds for DR-Submodular Functions](https://arxiv.org/abs/2311.01129v1) · [Deterministic Algorithm for Non-monotone Submodular Maximization under Matroid and Knapsack Constraints](https://arxiv.org/abs/2603.11996v2) · [Online Non-Monotone DR-Submodular Maximization Matching the Offline \(0.401\) Factor](https://arxiv.org/abs/2609.02145v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7358 — Optimal polynomial-time approximation ratio for Steiner Tree

Steiner Tree seeks a minimum-cost tree connecting a specified terminal set in an arbitrary undirected graph with nonnegative rational edge weights. The target is the infimum of approximation ratios achieved by uniform randomized algorithms that always output a feasible tree and run in polynomial time on every random tape. Each ratio bounds expected output cost on every instance, including those with zero optimum, while the algorithm may depend on the chosen ratio. Known algorithms approach \(\ln 4\), but the checked hardness bounds are conditional and the bounded later review found no determination of the optimal constant at the requested precision. An accepted answer supplies a real value with a complete Lean proof of absolute error at most \(1/100\), or a certified containing interval of width at most \(1/50\).

[Read in atlas](index.html#TCS-7358) · [Steiner Tree Approximation via Iterative Randomized Rounding](https://doi.org/10.1145/2432622.2432628) · [Local Search for Weighted Tree Augmentation and Steiner Tree](https://arxiv.org/abs/2107.07403v1) · [Better-Than-2 Approximations for Weighted Tree Augmentation and Applications to Steiner Tree](https://doi.org/10.1145/3722101) · [The Steiner tree problem on graphs: Inapproximability results](https://doi.org/10.1016/j.tcs.2008.06.046) · [The Bidirected Cut Relaxation for Steiner Tree has Integrality Gap Smaller than 2](https://arxiv.org/abs/2407.19905v2) · [Online Steiner Forest with Recourse](https://doi.org/10.4230/LIPIcs.ICALP.2026.141)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7354 — Optimal polynomial-time approximation ratio for metric k-means

Metric k-means chooses exactly k distinct centers from an explicit candidate set that includes every client. Its objective is the sum of squared metric distances to the nearest selected center. The target is the infimum of expected ratios achievable by uniform randomized polynomial-time algorithms. The July 2026 result reports an improved algorithmic ratio approaching 4.9 without determining the infimum. Acceptance requires a complete unconditional Lean-checked approximation to that constant within 0.01.

[Read in atlas](index.html#TCS-7354) · [Spectral Dual Fitting for k-Means](https://arxiv.org/abs/2607.14654v1) · [k-Clustering via Iterative Randomized Rounding](https://arxiv.org/abs/2604.06046v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7318 — Constant-factor approximation for Dasgupta’s hierarchical clustering objective

The input is an arbitrary graph whose nonnegative edge weights express pairwise similarities. A hierarchy repeatedly separates its vertices until every leaf contains one vertex. An edge pays its weight times the size of the smallest cluster containing both endpoints. The question asks for one deterministic polynomial-time algorithm with a fixed approximation factor on every such graph. Known general guarantees grow with the number of vertices, while Small-Set-Expansion hardness and results for richer inputs or different objectives do not unconditionally settle this question.

[Read in atlas](index.html#TCS-7318) · [A cost function for similarity-based hierarchical clustering](https://arxiv.org/abs/1510.05043v1) · [Approximate Hierarchical Clustering via Sparsest Cut and Spreading Metrics](https://arxiv.org/abs/1609.09548v1) · [Approximating Dasgupta Cost in Sublinear Time from a Few Random Seeds](https://doi.org/10.4230/LIPIcs.ICALP.2025.103) · [Hierarchical F-Clustering: Approximation and Hardness of Clustering into Trees and Bounded Diameter Graphs](https://arxiv.org/abs/2607.13217v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6757 — Min-CSP approximation at the SDP integrality gap

A minimization CSP assigns finite-domain values to variables to minimize the average of fixed local nonnegative costs. Its basic SDP can achieve a lower cost using consistent local distributions and vectors than any actual assignment. The question asks whether a randomized polynomial-time algorithm can match the SDP’s worst gap at each number of variables within every factor 1+ε. The multiplicative guarantee must also protect zero or very small optimum values, which existing additive universal rounding does not do. A resolution would clarify whether size-dependent SDP gaps universally predict achievable approximation for minimization CSPs.

[Read in atlas](index.html#TCS-6757) · [Approximation Algorithms for CSPs](https://doi.org/10.4230/DFU.Vol7.15301.287) · [How to Round Any CSP](https://www.dsteurer.org/paper/roundcsp.pdf) · [New Algorithms and Hardness Results for Robust Satisfiability of (Promise) CSPs](https://arxiv.org/abs/2602.10368v1)
Existing status: `source_open` · Summary written: 2026-09-16

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

## Online algorithms, scheduling and packing (27)

### TCS-6638 — Breaking two for unrelated-machine makespan

Jobs have machine-dependent processing times, and every job must be assigned wholly to one eligible machine. The objective is to minimize the maximum total load on any machine. The question asks whether a uniform deterministic polynomial-time algorithm can guarantee factor \(2-\varepsilon\) for some fixed \(\varepsilon>0\). The same improvement must hold for every input machine count and processing-time matrix, however small the chosen constant is. Instance-dependent savings and guarantees for restricted machine models do not establish this universal improvement.

[Read in atlas](index.html#TCS-6638) · [Approximation Algorithms for Scheduling Unrelated Parallel Machines](https://ir.cwi.nl/pub/18055) · [An Optimal Rounding Gives a Better Approximation for Scheduling Unrelated Machines](https://www.sciencedirect.com/science/article/abs/pii/S0167637704000690) · [On the Configuration-LP for Scheduling on Unrelated Machines](https://arxiv.org/abs/1011.4957) · [Santa Claus Meets Makespan and Matroids: Algorithms and Reductions](https://arxiv.org/abs/2307.08453) · [Learning-Augmented Approximation for Unrelated-Machines Makespan Scheduling](https://arxiv.org/abs/2606.13133) · [Proportionally Fair Makespan Approximation](https://arxiv.org/abs/2412.08572)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6676 — Breaking two for precedence-constrained makespan

The problem schedules positive-duration jobs on an input number of identical machines while respecting all precedences and minimizing the last completion time. The question asks whether a uniform deterministic polynomial-time algorithm can achieve approximation factor \(2-\varepsilon\) for some fixed \(\varepsilon>0\). Any positive constant improvement qualifies, and the same improvement must hold for all job counts, machine counts and precedence graphs. Graham's \(2-1/m\) guarantee approaches two as the machine count grows and therefore does not give the requested fixed saving. Known conditional hardness and restricted-instance algorithms do not themselves settle this unconditional existence question.

[Read in atlas](index.html#TCS-6676) · [Bounds for Certain Multiprocessing Anomalies](https://doi.org/10.1002/j.1538-7305.1966.tb01709.x) · [Complexity of Scheduling under Precedence Constraints](https://doi.org/10.1287/opre.26.1.22) · [Hardness of Precedence Constrained Scheduling on Identical Machines](https://theory.epfl.ch/osven/Ola%20Svensson_publications/SICOMP11b.pdf) · [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://doi.org/10.4230/LIPIcs.ESA.2022.40) · [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://arxiv.org/abs/2312.03495) · [Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs](https://arxiv.org/abs/2607.26590)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6640 — Constant additive error for one-dimensional bin packing

The input explicitly lists rational item sizes, and each item must be assigned whole to a unit-capacity bin. The question asks for a polynomial-time algorithm using at most a fixed constant more bins than the optimal integral packing. Randomization is allowed, but every output must be feasible and the quality guarantee must hold with probability at least two thirds on every input. All computation uses counted bit operations, and repeated items are listed rather than encoded by compressed multiplicities. A complete Lean-checked proof must establish the uniform algorithmic guarantee or rule it out; logarithmic losses and compressed-input lower bounds do not settle it.

[Read in atlas](index.html#TCS-6640) · [New Developments in Iterated Rounding (Invited Talk)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2014.1) · [A Logarithmic Additive Integrality Gap for Bin Packing](https://arxiv.org/abs/1503.08796v1) · [The Support of Bin Packing Is Exponential](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.48) · [A Tight Double-Exponential Lower Bound for High-Multiplicity Bin Packing](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.116)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6576 — Optimal competitive ratio for convex body chasing

Convex body chasing requires an online player to move into each newly revealed convex set. The player pays Euclidean movement while an offline comparator knows all future requests. This question asks for the optimal deterministic competitive ratio as dimension grows, up to universal constant factors. The strategy must work for arbitrary finite request sequences without knowing the horizon. The checked sources leave a gap between square-root and linear dimension dependence for general requests, with stronger results only in restricted settings.

[Read in atlas](index.html#TCS-6576) · [Online Algos: Old and New — Lecture 4: Search Problems](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf) · [Chasing Convex Bodies Optimally](https://arxiv.org/abs/1905.11968v3) · [Chasing Nested Convex Bodies Nearly Optimally](https://arxiv.org/abs/1811.00999)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6577 — Minimax dimension dependence in bandit convex optimization

What is the optimal expected regret for adversarial convex losses when only one value is observed per round? The learner competes with the best fixed point in hindsight over a known convex body. The losses lie in \([0,1]\) and are chosen before the learner’s random actions, with no smoothness assumption. General upper and lower bounds still have different polynomial dependence on dimension. Two-point, strongly convex, smooth-loss and computational-efficiency results address different guarantees.

[Read in atlas](index.html#TCS-6577) · [Bandit Convex Optimisation](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf) · [Improved Regret for Zeroth-Order Adversarial Bandit Convex Optimisation](https://arxiv.org/abs/2006.00475v3) · [Logarithmic High-Probability Regret for Online Convex Optimization with Two-Point Bandit Feedback](https://arxiv.org/abs/2603.25029v4) · [Adversarial Bandit Optimization with Globally Bounded Perturbations to Convex Losses](https://arxiv.org/abs/2606.19891v2)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7316 — Matroid secretary conjecture

Elements of a known matroid arrive in a uniformly random order with fixed nonnegative weights revealed only on arrival. The strategy must accept or reject each immediately while keeping its selected set independent. The target is one universal constant fraction of the offline optimum in expectation, with no running-time restriction. Singla’s September 2026 preprint claims a factor-four guarantee even with only arrived-element independence access. The claimed theorem matches this target, so the record is uncertain pending verification rather than still classified as an unchallenged open conjecture.

[Read in atlas](index.html#TCS-7316) · [Constant-Competitiveness for Random Assignment Matroid Secretary Without Knowing the Matroid](https://arxiv.org/abs/2305.05353) · [Matroid Secretary Is Equivalent to Contention Resolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.58) · [The Matroid Secretary Conjecture is True](https://arxiv.org/abs/2609.14555)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7317 — Randomized competitiveness of k-server

An online strategy moves k identical servers to serve requests in a finite metric space, paying total movement distance. The adversary fixes the request sequence independently of the strategy’s private randomness. The target is the universal optimal expected competitive ratio as a function of k, with matching upper and lower bounds up to constant factors. The metric and initial placement may affect the strategy and fixed additive cost, but the multiplicative ratio cannot depend on the number of metric points. The new deterministic factor-k claim leaves the randomized gap between squared-logarithmic and linear growth unresolved.

[Read in atlas](index.html#TCS-7317) · [Randomized k-Server in Polynomial Time](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.65) · [The Randomized k-Server Conjecture Is False!](https://arxiv.org/abs/2211.05753) · [On the k-Server Conjecture](https://doi.org/10.1145/210332.210337) · [The k-server conjecture is true](https://arxiv.org/abs/2609.15979)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5779 — Constant-factor online contention resolution for matroids

A random set of active elements is drawn from an arbitrary known distribution on a finite matroid. An offline map can inspect the whole active set before selecting an independent subset while preserving each element’s probability up to a factor alpha. The question asks whether an irrevocable strategy seeing activity in uniformly random arrival order can always match that balance within one universal extra constant. This known-prior correlated model is equivalent at the constant-factor level to the matroid secretary conjecture. A September 2026 secretary proof claim would settle the target with extra factor four, so its current status awaits independent verification.

[Read in atlas](index.html#TCS-5779) · [The Outer Limits of Contention Resolution on Matroids and Connections to the Secretary Problem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.42) · [Matroid Secretary Is Equivalent to Contention Resolution](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.58) · [The Matroid Secretary Conjecture is True](https://arxiv.org/abs/2609.14555)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6724 — Constant-factor related-machine precedence scheduling

The problem asks for a polynomial-time constant-factor approximation to the makespan of precedence-constrained jobs on machines with different speeds. Every job may use every machine, and its uninterrupted execution time is its processing requirement divided by the selected machine’s speed. The approximation factor must remain fixed as the number of machines and the range of speeds grow. The checked general upper bound grows logarithmically divided by an iterated logarithm, while known stronger hardness uses extra unproved hypotheses. A solution must cover arbitrary finite rational inputs in the explicitly stated deterministic bit model.

[Read in atlas](index.html#TCS-6724) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/book.pdf) · [Scheduling to Minimize Total Weighted Completion Time via Time-Indexed Linear Programming Relaxations](https://arxiv.org/abs/1707.08039) · [On the Hardness of Scheduling With Non-Uniform Communication Delays](https://par.nsf.gov/servlets/purl/10342245) · [Communication-aware scheduling of precedence-constrained tasks on related machines](https://doi.org/10.1016/j.orl.2023.11.001) · [Communication-Aware Scheduling of Precedence-Constrained Tasks on Related Machines](https://arxiv.org/abs/2004.14639v1)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-5030 — Optimal randomized competitive ratio of weighted k-server

Weighted k-server assigns a separate movement-cost multiplier to each server. All distinct locations are at unit distance, isolating uncertainty about which weight to move. The target is the optimal randomized competitive ratio as a function of the number of servers. It takes the worst case over finite metric sizes and arbitrary positive weights against oblivious requests. The recent \(\exp (O(k^{2}))\) upper bound removes the old doubly-exponential barrier but leaves a substantial gap above exponential lower bounds.

[Read in atlas](index.html#TCS-5030) · [A Decomposition Approach to the Weighted k-Server Problem](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.6) · [Weighted k-Server Admits an Exponentially Competitive Algorithm](https://doi.org/10.1137/1.9781611978971.154) · [The Randomized Competitive Ratio of Weighted k-server is at Least Exponential](https://doi.org/10.4086/toc.2022.v018a023)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5221 — Sublinear-in-q prophet inequalities for q-matroid intersection

Independent random element values arrive one at a time in a fixed known order. The selector must irrevocably choose a set that is independent in each of q given matroids. It knows the value distributions, while the offline comparator sees all realized values before making its choice. The question asks whether the ratio of their expected rewards can always be bounded by a function growing sublinearly in q. The checked source improves a square-root lower obstruction but corrects an earlier erroneous linear lower-bound claim and leaves the gap open.

[Read in atlas](index.html#TCS-5221) · [An Improved Lower Bound for Matroid Intersection Prophet Inequalities](https://doi.org/10.4230/LIPIcs.ITCS.2023.95) · [Online Stochastic Matching](https://simons.berkeley.edu/sites/default/files/2025-06/Sublinear%20Algorithms%20Open%20Problems%20Summer%202024.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1241 — Sublogarithmic competitiveness for online metric TSP

Points arrive with distances to earlier points and must immediately be inserted into an evolving order. Each insertion preserves the relative order of all previous arrivals, but there is no fixed array capacity or computational resource bound. The final cost is the sum of distances between consecutive points, compared with the best offline ordering. The question asks whether a deterministic algorithm can guarantee a competitive ratio smaller than logarithmic by an asymptotic factor on every metric input. This would isolate how much performance is lost through irreversible ordering alone, beyond the additional losses caused by limited storage.

[Read in atlas](index.html#TCS-1241) · [Online Metric TSP: Beyond the \(\sqrt{n}\) Barrier](https://doi.org/10.4230/LIPIcs.ICALP.2026.18) · [Online Sorting and Online TSP: Randomized, Stochastic, and High-Dimensional](https://doi.org/10.4230/LIPIcs.ESA.2024.5) · [Online Metric TSP: Beyond the \(\sqrt{n}\) Barrier](https://arxiv.org/abs/2608.07369v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0935 — Polynomial-time unit-job precedence scheduling on fixed machines

Every job takes one time slot, and a directed acyclic graph specifies which jobs must finish before others start. At most k jobs may run simultaneously on k identical machines. The question asks for polynomial-time computation of the minimum number of slots for every fixed k greater than two. The polynomial and algorithm may depend on k, but must handle all job counts and precedence graphs. The recent exact subexponential algorithm improves the general upper bound without establishing the requested polynomial time.

[Read in atlas](index.html#TCS-0935) · [List of open questions: Complexity of makespan scheduling of unit jobs with precedence constraints](https://a3nm.net/work/research/questions/#complexity-of-makespan-scheduling-of-unit-jobs-with-precedence-constraints) · [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://doi.org/10.1137/1.9781611978322.16) · [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://doi.org/10.4230/LIPIcs.ESA.2022.40) · [Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs](https://arxiv.org/abs/2607.26590v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7335 — Randomized competitive ratio of list update

An online list serves each request before seeing the next, and access costs the item’s position counted from one. The accessed item may move forward for free, while other adjacent exchanges cost one. Randomized performance is compared with an optimal offline schedule under the same rules and initial order. The checked full-cost bounds leave the optimal competitive factor between 1.5 and 1.6. The benchmark asks for a Lean-certified approximation of this factor to absolute error at most one hundredth.

[Read in atlas](index.html#TCS-7335) · [List Update with Prediction](https://ojs.aaai.org/index.php/AAAI/article/download/33694/35849) · [A New Lower Bound for the List Update Problem in the Partial Cost Model](https://people.inf.ethz.ch/gaertner/subdir/texts/own_work/lowerb.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6078 — Pinwheel Packing in NP

Pinwheel packing asks one machine to execute every recurring task often enough to meet all of its sliding-window deadlines. The input is an explicit list of positive recurrence limits written in binary, while the schedule extends indefinitely. The question is whether every feasible instance has a polynomial-length certificate checkable in polynomial time. A polynomial-space algorithm and finite periodic schedules are known, but the available period bound can be exponential in the input length. An April 2026 preprint proves NP-hardness, while the checked literature leaves membership in NP unresolved.

[Read in atlas](index.html#TCS-6078) · [Hardness and Fixed Parameter Tractability for Pinwheel Scheduling Problems](https://doi.org/10.4230/LIPIcs.ISAAC.2025.47) · [NP-Hardness and a PTAS for the Pinwheel Problem](https://arxiv.org/abs/2604.13974v1) · [Finite Pinwheel Covering](https://arxiv.org/abs/2607.28574v2)
Existing status: `source_open` · Summary written: 2026-09-17

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

### TCS-1529 — One forecaster with the optimal regret rate for every proper loss

One online forecaster must issue predictions before knowing which proper loss a downstream user cares about. The question asks it to match each loss’s own optimal regret rate up to logarithmic factors in the horizon. The benchmark is the best fixed probability prediction in hindsight, with expectation over the forecaster’s randomness. The source already combines logarithmic regret for smooth losses with nearly square-root regret for all bounded proper losses. The remaining task is to adapt to the individually optimal rate of every bounded proper loss.

[Read in atlas](index.html#TCS-1529) · [Toward Simultaneously Optimal Regret in U-Calibration](https://proceedings.mlr.press/v336/frongillo26a.html) · [Toward Simultaneously Optimal Regret in U-Calibration — version record](https://arxiv.org/abs/2606.18527)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-4983 — Sublinear competitive ratio for randomized k-server

The randomized k-server problem serves sequential metric requests while paying for movement of k available servers. The source asks whether arbitrary metrics admit a competitive ratio growing strictly slower than k. Bounds obtained through tree embeddings may depend on the number of metric points, so they do not automatically provide the requested dependence on k alone. The paper separately addresses implementing randomized strategies in polynomial time. The central question would establish a universal asymptotic advantage of randomization over the linear-in-k deterministic barrier, without restricting the metric's geometry or size.

[Read in atlas](index.html#TCS-4983) · [Randomized k-Server in Polynomial Time](https://doi.org/10.4230/LIPIcs.ICALP.2026.65)
Existing status: `uncertain` · Summary written: 2026-09-11

### TCS-5252 — Action-set-dependent regret in bandit combinatorial optimization

Bandit combinatorial optimization chooses structured subsets and observes only the total loss of the chosen subset. The source asks which properties of the particular action set determine its optimal regret. General bounds in ambient dimension and subset size may ignore substantial structure shared by the feasible actions. For shortest-path actions, the question becomes identifying graph properties that control learning difficulty, including on a simple directed grid. A characterization would replace worst-case guarantees over all action systems with bounds that explain why one specific combinatorial decision problem is easier than another.

[Read in atlas](index.html#TCS-5252) · [Tight Bounds for Bandit Combinatorial Optimization](https://proceedings.mlr.press/v65/cohen17a.html)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6721 — Additive-one approximation for bin packing

Bin packing assigns indivisible items of known sizes to bins of unit capacity. The goal is to find a packing that uses at most one bin more than the minimum possible. The algorithm must run in polynomial time in the complete binary input length. Known general algorithms achieve a logarithmic additive loss, while approximation schemes do not guarantee one extra bin. The question asks how closely efficient computation can approach the exact optimum of a fundamental packing problem.

[Read in atlas](index.html#TCS-6721) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/) · [A Logarithmic Additive Integrality Gap for Bin Packing](https://doi.org/10.1137/1.9781611974782.172)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6838 — Instance-optimal finite-time best-arm identification

Best-arm identification spends samples to recommend a good arm, rather than to maximize reward during exploration. The source asks for finite-time guarantees matching its information-theoretic lower bounds and for instance-dependent bounds on simple regret. Simple regret measures the reward gap of the final recommendation, making it sensitive to how costly a particular mistake is. The source also proposes understanding the distribution of that gap, beyond just its expectation. These questions would connect asymptotically optimal exploration rules with the quality and reliability of recommendations produced under an actual finite sampling budget.

[Read in atlas](index.html#TCS-6838) · [Bandit Algorithms](https://banditalgs.com/)
Existing status: `source_open` · Summary written: 2026-09-11

## Beyond worst-case and average-case analysis (13)

### TCS-6656 — Planted clique conjecture

A detector receives one random graph and must tell whether a uniformly chosen set of exactly k vertices was made into a clique. The selected conjecture excludes a uniform randomized polynomial-time detector with balanced success at least two thirds at all sufficiently large sizes when k is a fixed power below the square-root scale. The input, all sources of randomness, the complete bit-time clock and the precise order of quantifiers are specified. Known recovery algorithms reach the square-root scale, while sum-of-squares integrality gaps and other method restrictions do not exclude every detector. Conditional distinguishing results and newer inference reductions remain evidence about the hypothesis, with differing planting conventions and guarantees identified explicitly.

[Read in atlas](index.html#TCS-6656) · [Computational lower bounds in latent models: clustering, sparse-clustering, biclustering](https://arxiv.org/abs/2506.13647v1) · [Finding a Large Hidden Clique in a Random Graph](https://people.math.ethz.ch/~sudakovb/hidden-clique.pdf) · [A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem](https://doi.org/10.1137/17M1138236) · [Finding planted cliques using gradient descent](https://arxiv.org/abs/2311.07540v2) · [On optimal distinguishers for Planted Clique](https://arxiv.org/abs/2505.01990v2) · [Robust Algorithms for Finding Cliques in Random Intersection Graphs via Sum-of-Squares](https://proceedings.mlr.press/v336/gobel26a.html) · [Average-case hardness of Betti number estimation](https://arxiv.org/abs/2609.12777v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0012 — Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)

The premise P != NP only states a worst-case separation between efficient decision and verification. The conclusion asks for one fixed NP language and one strict polynomial-time sampler whose generated inputs defeat every deterministic exact decider under a positive-moment runtime bound. The ensemble parameter is supplied to the decider, while correctness is required even on inputs outside the sampler’s support. Known reduction barriers concern restricted proof methods, and recent description-complexity results retain specialized hardness premises or different average-case conventions. A solution requires a complete Lean proof of the implication from the stated premise alone or of its full negation in the ordinary uniform model.

[Read in atlas](index.html#TCS-0012) · [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [On Worst-Case to Average-Case Reductions for NP Problems](https://lucatrevisan.github.io/pubs/BT03.pdf) · [One-Way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.97) · [Cryptographic Implications of Worst-Case Hardness of Time-Bounded Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2026/051/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6657 — Computational threshold for tensor PCA

The card asks whether every efficient classical algorithm fails to recover constant correlation with a hidden spherical direction below a specified tensor-PCA signal scale. Its observation is one fully listed tensor with independent ordered Gaussian noise, fixed finite-precision rounding and no extra information. The statement precisely separates failure on arbitrarily large dimensions from the eventual-success counterexample needed to refute it. Recent low-degree, power-iteration, multiple-observation and threshold-refinement results retain model or resource restrictions. A Lean resolution must handle the full uniform bit model and its exact spherical recovery probability, preserving all normalization and precision choices.

[Read in atlas](index.html#TCS-6657) · [A statistical model for tensor PCA](https://arxiv.org/abs/1411.1076) · [Sharp analysis of power iteration for tensor PCA](https://www.jmlr.org/papers/v25/24-0006.html) · [Tensor cumulants for statistical inference on invariant distributions](https://arxiv.org/abs/2404.18735) · [Near-Optimal Tensor PCA via Normalized Stochastic Gradient Ascent with Overparameterization](https://arxiv.org/abs/2510.14329) · [Low-degree estimation thresholds in planted hypergraphs and tensor PCA](https://arxiv.org/abs/2605.30113) · [A Smooth Computational Transition in Tensor PCA](https://arxiv.org/abs/2509.09904) · [Average-Case Reductions for k-XOR and Tensor PCA](https://arxiv.org/abs/2601.19016) · [Accelerating Classical and Quantum Tensor PCA](https://arxiv.org/abs/2602.10366)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-6684 — Computational Kesten–Stigum threshold

A sparse stochastic block model hides a fixed number of equally likely community labels in a random graph. The question asks whether any fixed assortative parameters below the Kesten–Stigum threshold allow polynomial-time recovery with a constant expected advantage over chance. The algorithm receives one graph, and success is measured after the best permutation of the community names. Information can survive below the threshold, but known computational barriers retain conjectural or restricted-estimator assumptions. Recent algorithms with a growing number of communities do not supply the fixed-parameter example required here.

[Read in atlas](index.html#TCS-6684) · [Detection in the stochastic block model with multiple clusters: proof of the achievability conjectures, acyclic BP, and the information-computation gap](https://arxiv.org/abs/1512.09080) · [Information-theoretic thresholds for community detection in sparse networks](https://proceedings.mlr.press/v49/banks16.html) · [Low degree conjecture implies sharp computational thresholds in stochastic block model](https://arxiv.org/abs/2502.15024) · [Stochastic block models with many communities and the Kesten–Stigum bound](https://arxiv.org/abs/2503.03047)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7238 — Polynomial-time refutation of random 3-SAT at constant density

A random 3-SAT formula at sufficiently large constant clause density is almost surely unsatisfiable. The question asks for one polynomial-time randomized refuter that recognizes almost all such formulas while never rejecting a satisfiable formula. The density, algorithm and time bound must be fixed independently of the number of variables. Gap refutation, planted detection and lower bounds for particular proof systems do not settle this exact-sound unrestricted target. An accepted answer proves existence or impossibility with the full quantifiers in Lean.

[Read in atlas](index.html#TCS-7238) · [How to refute a random CSP](https://www.cs.cmu.edu/~odonnell/papers/random-csp-refutation.pdf) · [Proof vs. Truth in Computational Complexity](https://eccc.weizmann.ac.il/report/2012/120/revision/1/download/) · [Strongly Refuting Random CSP without Literals](https://arxiv.org/abs/2604.27336v1) · [Random \(3\)-CNF formulas are hard for \(k\)-DNF resolution up to \(k=O(\sqrt{\log n})\)](https://eccc.weizmann.ac.il/report/2026/158/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6453 — Infinitely-often one-way functions from average-case NP hardness

Some NP problems may remain hard to decide on inputs generated by an efficient sampler. This card asks whether such distributional hardness alone guarantees a polynomial-time function that is hard to invert at infinitely many lengths. The premise rules out one randomized heuristic scheme that works at every requested accuracy. The conclusion requires each polynomial-time inverter to have arbitrarily small inverse-polynomial success at arbitrarily large lengths, with those lengths allowed to depend on the inverter. A complete Lean-checked answer must settle the unrelativized implication, rather than a stronger eventual-hardness variant or an oracle-world separation.

[Read in atlas](index.html#TCS-6453) · [A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/revision/1/) · [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3) · [Quantum Pessiland](https://arxiv.org/abs/2608.29493v1) · [One-Way Functions and Polynomial-Time Dimension](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.44)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6658 — Polynomial smoothed complexity of FLIP for Max-Cut

Does FLIP for Max-Cut have polynomial expected path length on every graph under independent bounded-density edge weights? Each step moves just one vertex and must strictly increase the cut weight. The expectation controls the longest path after the weights are sampled, including all starting cuts and improving choices. Polynomial bounds for sparse graph families and a general high-probability bound do not finish this target. The known smoothed superpolynomial example permits three-vertex moves, while its single-vertex analogue is unperturbed.

[Read in atlas](index.html#TCS-6658) · [Local Max-Cut on Sparse Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.98) · [Smoothed complexity of local Max-Cut and binary Max-CSP](https://arxiv.org/abs/1911.10381) · [Superpolynomial smoothed complexity of 3-FLIP in Local Max-Cut](https://people.maths.ox.ac.uk/michel/Papers/smoothed-complexity-local-max-cut-3-flip.pdf)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7148 — Polynomial simplex complexity under zero-preserving perturbations

Smoothed analysis asks how a simplex algorithm behaves on a worst-case linear program after independent random perturbations. This version keeps every original zero coefficient fixed and adds Gaussian noise only to nonzero matrix and right-hand-side entries. The target asks whether some explicitly defined two-phase simplex algorithm solves every such family exactly in expected polynomially many arithmetic operations. The algorithm class and additive noise convention are disclosed editorial choices completing a broader source question. A complete Lean answer must prove the universal expected bound or refute it for every algorithm in the stated class.

[Read in atlas](index.html#TCS-7148) · [Beyond Worst-Case Analysis](https://arxiv.org/abs/1806.09817) · [Smoothed Analysis of Algorithms: Why the Simplex Algorithm Usually Takes Polynomial Time](https://arxiv.org/abs/cs/0111050v7) · [Beyond Smoothed Analysis: Analyzing the Simplex Method by the Book](https://arxiv.org/abs/2510.21613v2) · [Optimal Smoothed Analysis of the Simplex Method](https://arxiv.org/abs/2504.04197v2)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-5011 — Algorithmic threshold for the symmetric binary perceptron

The symmetric binary perceptron seeks a sign vector satisfying many random Gaussian two-sided constraints. The conjecture places the efficient-search density at the scale of the squared margin, allowing fixed powers of its reciprocal logarithm. The card defines a supremum over uniform polynomial-time algorithms and states its exact real-arithmetic convention. The input dimension tends to infinity at each fixed margin and density before the margin approaches zero. Stable-algorithm barriers, a sign-matrix algorithm and conditional lattice reductions each have limits that prevent treating them as a full resolution.

[Read in atlas](index.html#TCS-5011) · [Algorithms and Barriers in the Symmetric Binary Perceptron Model](https://doi.org/10.1109/FOCS54457.2022.00061) · [Symmetric Perceptrons, Number Partitioning and Lattices](https://arxiv.org/abs/2501.16517) · [Parametric RDT approach to computational gap of symmetric binary perceptron](https://arxiv.org/abs/2601.10628)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5406 — Optimization and certification of Max-Cut in random cubic graphs

The user has specialized the general random-CSP program to Max-Cut on uniform simple random cubic graphs. The target is the pair of best polynomial-time cut-construction and always sound certification thresholds, measured in crossing edges per vertex. Randomized uniform algorithms must meet their performance guarantees with probability tending to one, while certificates must remain sound on every graph. Known spectral values, true-optimum bounds, conditional hardness and a recent reported certification improvement do not establish both requested unconditional thresholds. A complete answer supplies approximations to both constants within absolute error one hundredth and proves their correctness in Lean.

[Read in atlas](index.html#TCS-5406) · [The SDP Value of Random 2CSPs](https://doi.org/10.4230/LIPIcs.ICALP.2022.97) · [The Ising antiferromagnet and max cut on random regular graphs](https://doi.org/10.1137/20M137999X) · [Computational hardness of detecting graph lifts and certifying lift-monotone properties of random regular graphs](https://arxiv.org/abs/2404.17012v1) · [Reinforced Generation of Combinatorial Structures: Hardness of Approximation](https://arxiv.org/abs/2509.18057v7)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-4876 — Algorithmic threshold for random k-SAT

The input is a random conjunction of fixed-width clauses, with all literal positions sampled independently. The algorithm must find an assignment satisfying every clause with probability tending to one. The conjectured leading threshold is two to the clause width times its natural logarithm, divided by the width. Known algorithms reach this scale, while satisfying assignments exist at substantially higher densities. Existing overlap-gap and low-degree barriers do not establish optimality against every polynomial-time algorithm.

[Read in atlas](index.html#TCS-4876) · [Sharp Thresholds for the Overlap Gap Property: Ising p-Spin Glass and Random k-SAT — full version](https://arxiv.org/abs/2309.09913) · [A Better Algorithm for Random k-SAT](https://doi.org/10.1137/09076516X) · [The Algorithmic Phase Transition of Random k-SAT for Low Degree Polynomials](https://arxiv.org/abs/2106.02129)
Existing status: `open` · Summary written: 2026-09-12

### TCS-6702 — Worst-case-to-average-case reductions within NP

Worst-case-to-average-case reductions aim to turn the difficulty of some inputs into difficulty on a substantial fraction of a samplable distribution. The source asks for suitable reductions that remain within NP. Staying inside NP preserves efficient verification of witnesses while attempting to distribute hardness more broadly. A successful construction would connect basic worst-case assumptions to the distributional hardness used in pseudorandomness and related areas. The saved survey note does not preserve the input distribution, reduction type, or hardness fraction, so those parameters must be recovered before the broad direction becomes one exact implication.

[Read in atlas](index.html#TCS-6702) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6703 — Optimal exponential-scale hardness amplification in NP

Hardness amplification strengthens a problem that is mildly hard on average into one that is hard on nearly all inputs. The source asks for optimal exponential-scale amplification while keeping the resulting problem in NP. The NP requirement constrains which encodings and combinations can be used without losing efficiently verifiable witnesses. An optimal result would sharpen the quantitative route from weak average-case hardness to strong pseudorandomness consequences. The saved note omits the starting advantage, output length, and target error exponent, so these must be restored before optimality can be judged against a specific amplification bound.

[Read in atlas](index.html#TCS-6703) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)
Existing status: `source_open` · Summary written: 2026-09-11

## Sampling, Markov chains and mixing times (9)

### TCS-6621 — Rapid mixing of Glauber dynamics with \(\Delta +2\) colours

The question concerns a local Markov chain that recolours one vertex uniformly from its currently available colours. It asks for one polynomial mixing bound for every graph and every palette with at least two more colours than the maximum degree. The stationary law is uniform on all proper labelled colourings and the bound must hold from the worst initial colouring. Known general-graph and recent near-threshold results retain larger palette slack, structural assumptions or parameter-dependent qualifications. Resolving the uniform additive-threshold conjecture would clarify the power of elementary local sampling for constrained spin systems.

[Read in atlas](index.html#TCS-6621) · [Glauber dynamics for colourings of chordal graphs and graphs of bounded treewidth](https://arxiv.org/abs/2010.16158) · [Sampling Colorings with Fixed Color Class Sizes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134) · [Flip Dynamics for Sampling Colorings: Improving \((11/6- \varepsilon )\) Using a Simple Metric](https://arxiv.org/abs/2407.04870) · [Sampling Colorings Close to the Maximum Degree: Non-Markovian Coupling and Local Uniformity](https://arxiv.org/abs/2604.11938) · [A Spectral Local-to-Global Principle for Spin Systems on Graphs with Girth At Least Five](https://arxiv.org/abs/2608.25491)
Existing status: `source_open` · Summary written: 2026-09-16

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

## Counting and enumeration (18)

### TCS-6628 — FPRAS for counting perfect matchings

A perfect matching pairs every vertex of a graph with exactly one neighbor. The question asks for one randomized algorithm giving arbitrarily accurate relative estimates of their number on every finite unweighted simple graph. Its worst-case running time must be polynomial in the full input length and inverse accuracy, with success probability at least three quarters for each input. Bipartite perfect matchings and all matchings have approximation schemes, but the checked 2026 dense-graph and permanent results retain restrictions absent from this target. A complete Lean proof must establish such a uniform scheme with exact zero behavior or prove that no scheme meeting all requirements exists.

[Read in atlas](index.html#TCS-6628) · [Approximating the Permanent](https://webspace.maths.qmul.ac.uk/m.jerrum/papers/SIAMperm.pdf) · [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://people.eecs.berkeley.edu/~sinclair/perm2.pdf) · [On Counting Perfect Matchings in General Graphs](https://arxiv.org/abs/1712.07504v1) · [Two-State Spin Systems with Negative Interactions](https://arxiv.org/abs/2309.04735v3) · [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599v1) · [Diffuse Gaussian Truncation For Deterministic Approximate Counting](https://arxiv.org/abs/2609.04079v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7221 — FPRAS for #BIS

The #BIS problem counts all independent vertex subsets of an arbitrary finite simple bipartite graph, including the empty set. The question asks for one uniform randomized bit algorithm with polynomial runtime in the complete input length and inverse requested relative accuracy, succeeding with probability at least three quarters on every instance. Acceptance requires a full Lean-checked construction with an every-random-tape runtime bound, or a proof excluding every such scheme without an unresolved extra assumption. The problem represents a central approximation class whose apparent intermediate complexity is not settled by hardness of exact counting. The checked2026 literature still leaves the total count open, while typical regular inputs, dense regular graphs and balanced or fixed-size counts have distinct known results.

[Read in atlas](index.html#TCS-7221) · [A Fixed-Parameter Perspective on #BIS](https://link.springer.com/article/10.1007/s00453-019-00606-4) · [Counting Independent Sets and Colorings on Random Regular Bipartite Graphs](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.34) · [A Spectral Approach to Approximately Counting Independent Sets in Dense Bipartite Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.35) · [Computational Thresholds for Balanced and Fixed-Slice Independent Sets in Bipartite Graphs](https://arxiv.org/abs/2608.02503v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6820 — FP versus #P

The question asks whether every polynomially verifiable witness count can be evaluated exactly in deterministic polynomial time. Witnesses are binary strings of a fixed polynomial length, and different witnesses retain their multiplicities. The exact count is output in binary, so even an exponentially large value needs only polynomially many output bits. An affirmative answer would imply P = NP, but efficient existence testing or relative approximation does not establish exact counting. A resolution would settle the basic computational boundary for counting satisfiability, permanents and all other functions in #P.

[Read in atlas](index.html#TCS-6820) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/book.pdf) · [Notes on Computational Complexity Theory](https://www.cs.yale.edu/homes/aspnes/classes/468/notes-2017.pdf) · [P ?= NP](https://www.scottaaronson.com/papers/pnp.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6629 — Deterministic FPTAS for the nonnegative permanent

The permanent of a nonnegative matrix sums the weights of all perfect matchings in its bipartite support graph. The question asks for one deterministic algorithm approximating this value to any requested relative accuracy on every nonnegative rational matrix. Its running time must be polynomial in the full binary input length and inverse accuracy, with a fixed exponent and exact output zero when the permanent is zero. Randomized approximation is established, while checked 2026 deterministic results have dimension-dependent error factors or fixed density and weight restrictions. A complete Lean proof must establish the unrestricted deterministic scheme or prove that none meets the stated guarantees.

[Read in atlas](index.html#TCS-6629) · [A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries](https://people.eecs.berkeley.edu/~sinclair/perm2.pdf) · [A Tight Analysis of Bethe Approximation for Permanent](https://arxiv.org/abs/1811.02933v2) · [Faster FPRAS for the Permanent via Restricted Poincaré Inequalities and Coupled Flows](https://arxiv.org/abs/2608.26599v1) · [Beyond the Bethe Approximation of the Permanent](https://arxiv.org/abs/2608.28031v2) · [Structural Corrections to the Bethe Approximation of the Permanent](https://arxiv.org/abs/2608.31061v1) · [Subexponential Approximation of the Permanent in Deterministic Polynomial Time](https://arxiv.org/abs/2609.10516v1) · [Diffuse Gaussian Truncation For Deterministic Approximate Counting](https://arxiv.org/abs/2609.04079v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7240 — Output-polynomial vertex enumeration

The input describes a bounded rational polyhedron by linear inequalities in variable dimension. The task is to list every distinct extreme point exactly once and then halt. The requested total time is polynomial in the combined binary lengths of the input and the required vertex list. Degeneracy, exponentially many bases per vertex and infeasible arrangement intersections obstruct straightforward enumeration strategies. An accepted answer proves existence or impossibility of the full uniform algorithm in Lean.

[Read in atlas](index.html#TCS-7240) · [Polynomial time vertex enumeration of convex polytopes of bounded branch-width](https://arxiv.org/abs/1404.5584v2) · [An Efficient Algorithm for Vertex Enumeration of Arrangement](https://arxiv.org/abs/2401.16675v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6671 — FPRAS for counting undirected Euler tours

An Euler tour traverses every edge of an undirected graph exactly once and returns to its start. This question asks whether the number of such tours can be approximated by a randomized algorithm in fully polynomial time. The count uses labelled edges and a fixed first traversal to remove rotation and reversal ambiguity. The accuracy is multiplicative, and the success probability must be at least three quarters on every input. Known orientation-counting algorithms and restricted graph results do not resolve the general tour-counting question.

[Read in atlas](index.html#TCS-6671) · [Euler-tours of low-height toroidal grids](https://sites.cs.st-andrews.ac.uk/scm2024/abstracts.html) · [The Complexity of Counting Eulerian Tours in 4-regular Graphs](https://www.cs.rochester.edu/~stefanko/Publications-new/J25.pdf) · [Sampling and counting notes (Mixingbook)](https://www.math.cmu.edu/~af1p/Mixingbook.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6821 — FP = #P from \(\mathrm{P} = \mathrm{NP}\)

The question asks whether P = NP forces exact polynomial-time computation of every #P witness count. Each counting function has its own uniform deterministic machine, and its exact value must be output in binary. Finding one witness or approximating an exponential count to inverse-polynomial relative accuracy does not give its exact value. The literal negative answer would require P = NP together with a counting function outside numerical FP. A 2026 preprint claims the implication, but a directly checked internal defect prevents this review from accepting it as a resolution.

[Read in atlas](index.html#TCS-6821) · [Computational Complexity: A Modern Approach](https://theory.cs.princeton.edu/complexity/book.pdf) · [P ?= NP](https://www.scottaaronson.com/papers/pnp.pdf) · [Topological Collapse: P = NP Implies #P = FP via Solution-Space Homology](https://arxiv.org/abs/2603.22211v1)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7112 — Output-polynomial hypergraph transversal enumeration

A transversal meets every edge of a hypergraph and is minimal if removing any selected vertex destroys that property. The required algorithm lists all such sets exactly once and detects when enumeration is finished. Its total time must be polynomial in the combined input and complete output length. The output may be exponentially large, and no separate bound on delay is requested. A 2026 lower bound excludes a particular practical algorithm while leaving the existence of a general output-polynomial algorithm open.

[Read in atlas](index.html#TCS-7112) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042) · [Minimal-to-Maximal Conversion Search Is Not Output-Polynomial](https://arxiv.org/abs/2608.02159)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7355 — Fully polynomial randomized approximation of mixed discriminants

The mixed discriminant is a fixed coefficient of a determinant polynomial built from positive semidefinite matrices. The question asks for one randomized algorithm giving arbitrary relative accuracy in time polynomial in the input size and inverse accuracy. The full rational-input model includes singular matrices, zero answers and badly conditioned matrices. Permanents and single squared determinants are special cases, while constrained determinantal sums illustrate why the general case matters. An accepted answer proves existence or impossibility of the full approximation scheme in Lean.

[Read in atlas](index.html#TCS-7355) · [Polynomial time algorithms to approximate mixed volumes within a simply exponential factor](https://eccc.weizmann.ac.il/report/2007/037/revision/1/) · [On the Complexity of Constrained Determinantal Point Processes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36) · [On the (In)tractability of Computing Normalizing Constants for the Product of Determinantal Point Processes](https://proceedings.mlr.press/v119/ohsaka20a.html)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7320 — #BIS-easiness of Boolean log-supermodular counting CSPs

A Boolean log-supermodular counting CSP sums products of nonnegative rational local weights over all Boolean assignments. The question asks whether every fixed finite family of these weights admits a randomized approximation-preserving reduction to counting independent sets in bipartite graphs. The reduction must control relative error, all oracle failures and polynomial bit cost, and must also handle zero total weight. Known classifications give #BIS upper bounds in important special cases, while a four-variable gadget obstruction does not rule out more general reductions. A resolution would determine whether the whole log-supermodular approximation region has #BIS as a common computational upper benchmark.

[Read in atlas](index.html#TCS-7320) · [Counting Constraint Satisfaction Problems](https://doi.org/10.4230/DFU.Vol7.15301.205) · [The complexity of approximating conservative counting CSPs](https://arxiv.org/abs/1208.1783v3) · [The expressibility of functions on the Boolean domain, with applications to Counting CSPs](https://arxiv.org/abs/1108.5288v4)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3037 — Parity subgraph-counting dichotomy

The problem asks which graph-pattern families make counting copies modulo two parameterized-hard. The proposed boundary is whether deleting a bounded number of pattern vertices always leaves only edges and isolated vertices. Every computable class on the unbounded side is conjectured equivalent to parity clique under deterministic fixed-parameter Turing reductions. Copies are ordinary unlabelled subgraphs, and the input pattern size is the parameter. The classification is known for hereditary classes and classes of trees, while the general class-wide assertion remains the target.

[Read in atlas](index.html#TCS-3037) · [Modular Counting of Subgraphs: Matchings, Matching-Splittable Graphs, and Paths](https://doi.org/10.4230/LIPIcs.ESA.2021.34) · [Parameterised and Fine-Grained Subgraph Counting, Modulo 2](https://doi.org/10.1007/s00453-023-01178-0)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1004 — Deterministic relative counting for DNF

A DNF formula describes a union of sets of Boolean assignments, one set for each conjunction. The question asks for deterministic relative approximation of the number of assignments in that union. One uniform algorithm must run in time polynomial in the explicit formula size and reciprocal error. The estimate must count assignments once despite overlapping terms and must be exactly zero for an unsatisfiable formula. Randomized schemes and deterministic algorithms for restricted formulas leave the general fully polynomial target unresolved in the checked sources.

[Read in atlas](index.html#TCS-1004) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [A Note on Deterministic Approximate Counting for k-DNF](https://eccc.weizmann.ac.il/report/2002/069/) · [Pseudorandomness for read-k DNF formulas](https://www.cs.columbia.edu/~rocco/Public/read-k.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7099 — Finite-domain enumeration-CSP dichotomy

Enumeration CSP asks for every satisfying assignment of a fixed finite constraint language, each printed once. Polynomial delay bounds the waiting time before, between and after complete outputs independently of their total number. The question seeks a structural classification of all finite languages admitting such enumeration, with the complementary exclusion stated under P≠NP. Boolean languages are classified, but larger-domain examples show that tractability after pinning variables does not characterize efficient enumeration. A full dichotomy would identify the boundary for regular generation of alternatives beyond the known satisfiability decision classification.

[Read in atlas](index.html#TCS-7099) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042v1) · [Enumerating all Solutions for Constraint Satisfaction Problems](https://doi.org/10.4230/DagSemProc.06401.6) · [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021v2) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914v11)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7084 — Does P ≠ NP imply both polynomial-space enumeration separations?

An enumeration problem has polynomial-length solutions whose validity can be checked in polynomial time. Polynomial delay bounds each wait for the next answer, while incremental polynomial time bounds the cost of every initial segment. The question asks whether P ≠ NP forces both timing classes to become strictly weaker when the same algorithm must also use input-polynomial space. Output order is unrestricted, and the two separations may have different witness problems. Known regularization and broader-framework results do not settle this precise implication, whose complete proof or refutation must be Lean-checked.

[Read in atlas](index.html#TCS-7084) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042v1) · [Space Complexity of Enumeration](https://yann-strozecki.github.io/space_complexity.pdf) · [From amortized to worst case delay in enumeration algorithms](https://doi.org/10.1007/s00037-026-00287-w)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7086 — Incremental polynomial-time binary-matroid circuit enumeration

A circuit of a binary matroid is a nonempty inclusion-minimal linearly dependent set of matrix columns. The question asks to enumerate all circuits exactly once in incremental polynomial time using memory polynomial only in the matrix input length. The running time for the first k circuits may be polynomial in k, but the memory bound must remain independent of the number already output. Incremental enumeration is known with large saturation storage, while polynomial-space regularization assumes that this memory problem has already been solved. A positive answer would expose all minimal binary dependencies efficiently without storing an exponentially large circuit history.

[Read in atlas](index.html#TCS-7086) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042v1) · [Space Complexity of Enumeration](https://yann-strozecki.github.io/space_complexity.pdf) · [On the Complexity of Some Enumeration Problems for Matroids](https://doi.org/10.1137/S0895480103428338) · [From amortized to worst case delay in enumeration algorithms](https://doi.org/10.1007/s00037-026-00287-w)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7082 — A natural OutputP versus IncP separation from clique-free domination

For a fixed forbidden clique size, the task is to list every inclusion-minimal dominating set of the input graph once. An algorithm with total running time polynomial in the input and the entire output is already known. The question asks whether TFNP ≠ FP forces some fixed clique size for which no algorithm produces every initial output segment in incremental polynomial time. This selects the concrete graph candidate suggested by the source instead of imposing an undefined condition of naturalness. The existing abstract separation and algorithms for smaller graph classes do not settle this implication, whose proof or refutation must be Lean-checked.

[Read in atlas](index.html#TCS-7082) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042v1) · [On The Complexity of Enumeration](https://arxiv.org/abs/1703.01928v2) · [Enumerating minimal dominating sets in K_t-free graphs and variants](https://arxiv.org/abs/1810.00789v3) · [Enumerating Minimal Dominating Sets and Variants in Chordal Bipartite Graphs](https://doi.org/10.4230/LIPIcs.WADS.2025.15)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-3635 — Treewidth classification of approximate counting CSP

The input asks how many homomorphisms map a source structure A from a fixed class C into an arbitrary target structure B. The conjecture says a fixed-parameter randomized approximation scheme exists exactly when C has bounded Gaifman treewidth. Relation arity is uniformly bounded, C is recursively enumerable, and the parameter is the size of A. The source proves this under a further fan-class condition and asks to remove it. The 2020 journal version retains that restriction, so exact-counting and fixed-target classifications do not settle the missing approximation direction.

[Read in atlas](index.html#TCS-3635) · [Approximate Counting CSP Seen from the Other Side](https://doi.org/10.4230/LIPIcs.MFCS.2019.60) · [Approximate Counting CSP Seen from the Other Side](https://doi.org/10.1145/3389390) · [Counting List Homomorphisms from Graphs of Bounded Treewidth: Tight Complexity Bounds](https://doi.org/10.1145/3640814)
Existing status: `open` · Summary written: 2026-09-12

### TCS-4671 — Decision versus approximate counting for fixed-width SAT

A fixed-width CNF formula has a finite number of satisfying assignments. Decision tests whether that number is positive; approximation estimates it to relative error. The question asks whether the optimal exponential rates in the variable count coincide for each fixed width. Polynomial accuracy costs and arbitrarily small losses in the exponential rate are allowed. Later all-width and subexponential equivalences do not settle this fixed-width comparison.

[Read in atlas](index.html#TCS-4671) · [An Approximation Algorithm for #k-SAT](https://doi.org/10.4230/LIPIcs.STACS.2012.78) · [Exploiting Independent Subformulas: A Faster Approximation Scheme for #k-SAT](https://doi.org/10.1016/j.ipl.2013.02.013) · [Fine-Grained Reductions from Approximate Counting to Decision](https://doi.org/10.1145/3442352)
Existing status: `open` · Summary written: 2026-09-12

## Graph algorithms (26)

### TCS-7222 — Graph isomorphism in polynomial time

Graph isomorphism asks whether two finite simple graphs agree after a bijective relabeling of their vertices. The target is a single deterministic algorithm that answers correctly on every explicitly encoded pair in polynomial time. A proposed relabeling is easy to verify, while ruling out all relabelings can require substantially more structure. The checked general upper bound is quasipolynomial, and efficient algorithms for restricted graph classes do not establish the unrestricted polynomial bound. A resolution would settle a central structural comparison problem whose position between P and NP-completeness remains unresolved.

[Read in atlas](index.html#TCS-7222) · [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547) · [Group, Graphs, Algorithms: The Graph Isomorphism Problem](https://people.cs.uchicago.edu/~laci/papers/icm18-babai.pdf) · [Parameterized complexity of graph isomorphism testing](https://doi.org/10.1016/j.cosrev.2026.100918) · [Graph Isomorphism update, January 9, 2017](https://people.cs.uchicago.edu/~laci/update.html) · [Fractional Homomorphism, Weisfeiler-Leman Invariance, and the Sherali-Adams Hierarchy for the Constraint Satisfaction Problem](https://doi.org/10.4230/LIPIcs.MFCS.2021.27) · [On the Relative Power of Linear Algebraic Approximations of Graph Isomorphism](https://doi.org/10.4230/LIPIcs.MFCS.2021.37)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6536 — Deterministic linear-time minimum spanning tree

The problem asks for an exact minimum spanning tree of every connected simple undirected graph with arbitrary real edge weights. The target is one uniform deterministic sequential algorithm whose worst-case total running time is linear in the explicitly listed vertices and edges. Weights are opaque comparison keys, while ordinary logarithmic-word computation, preprocessing and writing the output are all charged. A complete Lean proof must establish every correctness and running-time guarantee or rule out all correct algorithms in this model. Randomized linear time, integer-weight algorithms and uniform decision-tree optimality are known, but the checked 2026 literature does not settle deterministic linear time for arbitrary comparison weights.

[Read in atlas](index.html#TCS-6536) · [A Randomized Linear-Time Algorithm to Find Minimum Spanning Trees](https://people.csail.mit.edu/karger/Papers/mst.pdf) · [A Minimum Spanning Tree Algorithm with Inverse-Ackermann Type Complexity](https://www.cs.princeton.edu/~chazelle/pubs/mst.pdf) · [An Optimal Minimum Spanning Tree Algorithm](https://www.cs.princeton.edu/courses/archive/fall05/cos528/handouts/An%20Optimal%20Minimum.pdf) · [Trans-dichotomous algorithms for minimum spanning trees and shortest paths](https://www.sciencedirect.com/science/article/pii/S0022000005800649) · [Minimum Spanning Tree in Deterministic Linear Time For Graphs of High Girth](https://people.csail.mit.edu/dmoshkov/papers/mst/high-girth.pdf) · [Randomized minimum spanning tree algorithms using exponentially fewer random bits](https://doi.org/10.1145/1328911.1328916) · [Pseudorandomness Beating the Hybrid Argument for Insensitive Algorithms](https://eccc.weizmann.ac.il/report/2026/082/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6538 — Almost-linear-time exact maximum matching in general graphs

Maximum-cardinality matching selects as many pairwise vertex-disjoint edges as possible in an arbitrary finite simple undirected graph. The target is one uniform randomized word-RAM algorithm that constructs an optimum matching with probability at least two thirds on every input. It must halt almost surely, always return a valid matching when it halts, and have expected time within every fixed positive exponent slack above the full explicit input size. A complete Lean proof must establish the algorithm and all these guarantees or rule out every permitted randomized program with this expected-time behavior. Known almost-linear bipartite algorithms, approximation schemes and catalytic-space results do not settle the general exact target, and the older Glauber-dynamics claim has an acknowledged error.

[Read in atlas](index.html#TCS-6538) · [A Theory of Alternating Paths and Blossoms from the Perspective of Minimum Length](https://pubsonline.informs.org/doi/abs/10.1287/moor.2020.0388) · [Maximum Matchings via Gaussian Elimination](https://www.mimuw.edu.pl/~mucha/pub/mucha_sankowski_focs04.pdf) · [Scaling algorithms for approximate and exact maximum weight matching](https://arxiv.org/abs/1112.0790) · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671) · [Gabow’s Cardinality Matching Algorithm in General Graphs: Implementation and Experiments](https://arxiv.org/abs/2409.14849) · [Maximum Matching and Related Problems in Catalytic Logspace](https://eccc.weizmann.ac.il/report/2026/080/) · [Maximum Matchings via Glauber Dynamics](https://arxiv.org/abs/1107.2482)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6683 — Optimal bounds in the Excluded Grid Theorem

The excluded-grid threshold is the least treewidth that forces a square grid of a specified side length in every finite simple undirected graph. The question asks for its true asymptotic order up to universal constant factors, including logarithmic dependence. A complete answer needs a universal grid-forcing bound and grid-excluding examples of matching treewidth, certified in Lean. The known quadratic-logarithmic lower bound and exponent-nine upper bound leave a large gap in this fundamental structural theorem. Recent product-structure, fixed-minor, annotated-grid and disjoint-paths results refine related questions while leaving the all-graphs target open.

[Read in atlas](index.html#TCS-6683) · [Graph minors. V. Excluding a planar graph](https://doi.org/10.1016/0095-8956(86)90030-4) · [Quickly Excluding a Planar Graph](https://doi.org/10.1006/jctb.1994.1073) · [Polynomial Bounds for the Grid-Minor Theorem](https://arxiv.org/abs/1305.6577v5) · [Towards Tight(er) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944) · [The Grid-Minor Theorem Revisited](https://link.springer.com/article/10.1007/s00493-025-00168-w) · [Catching Rats in \(H\)-minor-free Graphs](https://doi.org/10.1137/1.9781611978971.169) · [Quickly Excluding an Annotated Planar Graph](https://doi.org/10.4230/LIPIcs.ICALP.2026.99) · [Optimal Bounds for the \(k\)-Disjoint Paths Problem](https://arxiv.org/abs/2605.14902)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6539 — Almost-linear triangle detection

The input is an explicit undirected graph, and the output says whether three distinct vertices are pairwise adjacent. One fixed randomized program must work on every graph and every adjacency-list order. Every execution must take almost linear time in the number of vertices plus edges, with a correct answer on each input with probability at least two thirds. A relevant local-sketching preprint remains unverified, so the card records current status as uncertain. A complete Lean-checked answer must supply this algorithm and its guarantees or prove that none exists in the specified model.

[Read in atlas](index.html#TCS-6539) · [Popular conjectures imply strong lower bounds for dynamic problems](https://arxiv.org/abs/1402.0054v1) · [Finding and Counting Given Length Cycles](https://www.math.tau.ac.il/~nogaa/PDFS/ayz4.pdf) · [Arboricity and Subgraph Listing Algorithms](https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Chiba-1985-arboricity.pdf) · [Node-Weighted Triangles: Faster and Simpler](https://doi.org/10.4230/LIPIcs.ICALP.2026.10) · [Equivalent Dichotomies for Triangle Detection in Subgraph, Induced, and Colored H-Free Graphs](https://doi.org/10.4230/LIPIcs.ESA.2026.64) · [Triangle Detection in Worst-Case Sparse Graphs via Local Sketching](https://arxiv.org/abs/2509.03215v1) · [A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications](https://arxiv.org/abs/2403.01085v2) · [A Linear-Time Solution to the Triangle Finding Problem: The Aegypti Algorithm](https://www.preprints.org/manuscript/202506.0875/v3) · [Aegypti: A Combinatorial Algorithm for Triangle Detection](https://www.preprints.org/manuscript/202511.2197/v11)
Existing status: `uncertain` · Summary written: 2026-09-17

### TCS-7228 — Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time

An exact maximum flow routes the largest possible integral amount between two terminals while obeying every arc capacity and intermediate conservation law. For each fixed polynomial bound on capacities, the question asks for one algorithm whose time is input size times a single fixed power of a logarithm. The specified randomized word-RAM must respect that total time on every execution and return a complete optimal flow with probability at least two thirds on each valid input. A complete Lean proof must supply the algorithm and both guarantees or rule out all such algorithms for some fixed capacity exponent. The checked exact almost-linear algorithms and undirected approximation results do not establish this fixed-polylogarithmic exact directed-flow target.

[Read in atlas](index.html#TCS-7228) · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671) · [A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow](https://arxiv.org/abs/2309.16629) · [Almost-Linear Time Algorithms for Decremental Graphs: Min-Cost Flow and More via Duality](https://arxiv.org/abs/2407.10830) · [Maximum Flow Without the Outer IPM](https://arxiv.org/abs/2608.17384) · [Faster Weak Expander Decompositions and Approximate Max Flow](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.91)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6655 — Cereceda’s conjecture

A proper graph coloring can be changed one vertex at a time while remaining proper after every step. Cereceda’s conjecture asks whether any two colorings of a d-degenerate n-vertex graph can be connected in at most C_d n squared steps using d+2 available colors. The constant may depend on d, but not on the graph, its size or the chosen colorings. A general polynomial bound is known, but its exponent can exceed two. Recent linear bounds use special graph classes or more colors and do not settle this threshold-palette target.

[Read in atlas](index.html#TCS-6655) · [Linear recoloring diameter of degenerate chordal graphs and bounded treewidth graphs](https://doi.org/10.1016/j.disc.2026.115055) · [A polynomial version of Cereceda’s conjecture](https://doi.org/10.1016/j.jctb.2022.01.006)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7341 — Strongly polynomial near-linear negative-weight shortest paths

The input is a directed graph with arbitrary real arc lengths and no negative directed cycle. The task is to output every exact distance from one source, marking unreachable vertices. The question asks for a uniform randomized comparison-addition algorithm with only polylogarithmic overhead over the graph size. Recent integer-weight improvements retain numerical dependence, and almost-quadratic real-weight algorithms do not give the sparse-graph target. An accepted answer must provide a complete Lean-checked resolution with worst-case operation bounds and polynomial rational encoding space.

[Read in atlas](index.html#TCS-7341) · [Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!](https://arxiv.org/abs/2304.05279v1) · [Negative-Weight Single-Source Shortest Paths in Near-linear Time](https://arxiv.org/abs/2203.03456v6) · [Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers](https://arxiv.org/abs/2511.08551v1) · [Deterministic Padded Decompositions and Negative-Weight Shortest Paths](https://arxiv.org/abs/2511.07859v2) · [Bellman-Ford in Almost-Linear Time for Dense Graphs](https://arxiv.org/abs/2602.16153v1) · [An \(n^{2+o(1)}\) Time Algorithm for Single-Source Negative Weight Shortest Paths](https://arxiv.org/abs/2602.16638v1) · [Size-Sensitive Padded Decompositions for Faster Deterministic Negative-Weight Shortest Paths](https://arxiv.org/abs/2609.05590v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7346 — Strongly polynomial maximum flow below the \(mn\) barrier

The task is to output an exact maximum flow on every arc of an arbitrary directed rational-capacity network. The question asks for one fixed polynomial improvement over the general mn arithmetic-operation bound. The operation count must be independent of capacity magnitudes and encoding lengths, while intermediate bit space remains polynomial. Randomization is allowed, but every execution must obey the resource bounds and each input must have success probability at least two thirds. A complete Lean-checked resolution must cover all graph densities; bounded-integer, structured-network and parallel-depth improvements alone do not settle it.

[Read in atlas](index.html#TCS-7346) · [From Incremental Transitive Cover to Strongly Polynomial Maximum Flow](https://arxiv.org/abs/2510.20368v1) · [Max flows in \(O(nm)\) time, or better](https://www.eecs.northwestern.edu/~haizhou/457/O%28nm%29MaxFlow.pdf) · [Strongly Polynomial Parallel Maximum Flow Revisited](https://doi.org/10.4230/LIPIcs.ESA.2026.147)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7377 — Strong thin tree conjecture

The conjecture asks for a spanning tree that occupies only a constant divided by the edge connectivity fraction of every cut. One tree must satisfy all cut inequalities simultaneously. The constant must work for all graph sizes, and parallel edges are counted separately. Known general bounds still depend on graph size, while a 2026 result handles only near-minimum cuts. A solution would settle a central structural rounding question connecting connectivity and network design.

[Read in atlas](index.html#TCS-7377) · [Effective-Resistance-Reducing Flows, Spectrally Thin Trees, and Asymmetric TSP](https://arxiv.org/abs/1411.4613) · [Thin Trees for Near Minimum Cuts](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.129)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6500 — Erdős girth conjecture

The Erdős girth conjecture asks for graphs with many edges and no short cycles. For each fixed integer k at least two, the graphs must avoid every cycle of length at most 2k. Their number of edges must be at least a positive k-dependent constant times n to the power one plus one over k, at unbounded graph orders. No efficient construction or coverage of every graph order is required. A complete Lean-checked resolution must prove all fixed parameters or refute the density scale eventually for at least one of them.

[Read in atlas](index.html#TCS-6500) · [Unconditional Lower Bounds for Degree Fault Tolerant Spanners](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.31) · [Extremal Numbers of Cycles Revisited](https://authors.library.caltech.edu/records/8w53p-t0j17)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6511 — Deterministic Exact Matching

Exact Matching asks whether a red/blue graph has a perfect matching with exactly the requested number of red edges. The target is one deterministic polynomial-time decision algorithm for all simple undirected graphs. Knowing only the minimum and maximum red counts does not determine which intermediate counts are attainable. The recent faster general algorithm remains randomized, while a separate claimed deterministic result is restricted to bipartite graphs. A complete Lean-checked solution must establish membership in P or prove its unconditional negation.

[Read in atlas](index.html#TCS-6511) · [Exact Matching: Algorithms and Related Problems](https://doi.org/10.4230/LIPIcs.STACS.2023.29) · [Matching is as easy as matrix inversion](https://doi.org/10.1145/28395.383347) · [Exact Matching in Matrix Multiplication Time](https://arxiv.org/abs/2508.04081v2) · [Bipartite Exact Matching in P](https://arxiv.org/abs/2604.01571v3)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7180 — Graph canonization versus graph isomorphism

Graph isomorphism recognizes when two labeled graphs have the same structure. Canonization assigns every presentation of that structure an identical representative. The question asks whether a polynomial-time algorithm can compute such representatives using only a graph-isomorphism decision oracle. General quasipolynomial canonization and efficient results for random graph families do not supply this reduction. A solution must handle every finite graph and keep its choices consistent across all relabelings.

[Read in atlas](index.html#TCS-7180) · [Canonical Form for Graphs in Quasipolynomial Time](https://par.nsf.gov/servlets/purl/10179675) · [Canonical Labelling of Random Regular Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.114)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7342 — Steiner Shortcut Conjecture

A directed graph may be augmented with new arcs and new Steiner vertices. Reachability between every pair of original vertices must remain exactly unchanged. The target permits near-linearly many new arcs and requires polylogarithmic paths for every reachable original pair. The earlier refutation and newer lower bounds impose restrictions absent from this conjecture. A complete Lean-checked answer concerns universal structural existence, without requiring a fast construction algorithm.

[Read in atlas](index.html#TCS-7342) · [Reviving Thorup's Shortcut Conjecture](https://arxiv.org/abs/2510.24954v2) · [Reviving Thorup’s Shortcut Conjecture](https://doi.org/10.1145/3798129.3800781)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7343 — Deterministic almost-linear vertex connectivity

Vertex connectivity is the smallest number of vertices whose deletion disconnects a graph or leaves at most one vertex. The input is an explicit unweighted undirected graph, including all isolated vertices. The task is to output the exact value and an attaining set in deterministic almost-linear worst-case time. Randomized almost-linear time is known, while the reviewed deterministic bound retains a connectivity factor. A complete Lean-checked answer must cover every connectivity value with the same algorithm and time bound.

[Read in atlas](index.html#TCS-7343) · [Deterministic Vertex Connectivity via Common-Neighborhood Clustering and Pseudorandomness](https://arxiv.org/abs/2503.20985v1) · [Vertex Connectivity in Poly-logarithmic Max-flows](https://arxiv.org/abs/2104.00104v2) · [Maximum Flow and Minimum-Cost Flow in Almost-Linear Time](https://arxiv.org/abs/2203.00671v2) · [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7263 — Linear-time directed shortest paths with nonnegative real weights

The input is a directed graph with arbitrary nonnegative real arc lengths and a specified source. The task is to output every exact source distance. The question asks for deterministic linear worst-case time using real addition and comparison. Recent algorithms break the sorting barrier while retaining superlinear overhead. A linear algorithm would match the cost of reading the graph and writing the distances.

[Read in atlas](index.html#TCS-7263) · [Breaking the Sorting Barrier for Directed Single-Source Shortest Paths](https://arxiv.org/abs/2504.17033) · [A Faster Directed Single-Source Shortest Path Algorithm](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.81)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7348 — Single-exponential exact cut mimicking networks

A terminal cut separates any selected group of labelled terminals from all the other terminals. One replacement graph must preserve the minimum cost of every such separation exactly. The question asks for at most 2^(Ck) vertices with a single absolute constant C. The replacement may use arbitrary new nonterminals and weights, so contraction lower bounds alone do not answer it. A complete Lean-checked proof must establish or refute this structural existence claim for all nonnegatively weighted undirected graphs.

[Read in atlas](index.html#TCS-7348) · [Cut-Preserving Vertex Sparsifiers for Planar and Quasi-Bipartite Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2025.53) · [On Mimicking Networks Representing Minimum Terminal Cuts](https://arxiv.org/abs/1207.6371v1) · [Lower Bounds on Flow Sparsifiers with Steiner Nodes](https://arxiv.org/abs/2602.12645v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7344 — Almost-linear exact directed global minimum cut

The input is a directed graph with positive polynomially bounded integer arc weights. The algorithm must find the cheapest outgoing cut over all nontrivial vertex partitions and output its exact value. The target is one uniform almost-linear randomized algorithm, with bounded error and a time limit on every execution. Recent almost-linear approximations pay for inverse precision, while threshold-dependent exact results retain an extra connectivity factor. A complete Lean-checked exact construction or unconditional refutation is required.

[Read in atlas](index.html#TCS-7344) · [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176v1) · [Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs](https://arxiv.org/abs/2512.09080v3) · [Incremental Directed Minimum Cut by Dynamizing Gabow’s Algorithm](https://arxiv.org/abs/2608.16382v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7345 — Almost-linear directed vertex connectivity

The input is any simple unweighted directed graph, with no connectivity or density promise. The output is the smallest number of vertices whose removal destroys strong connectivity, together with such a set. Leaving at most one vertex is allowed, so a complete bidirected graph has value n minus one. The target is exact almost-linear randomized computation on every input; known expected and approximation bounds have additional limitations. A complete Lean-checked construction or unconditional refutation must respect the worst-case time and bounded-error guarantees.

[Read in atlas](index.html#TCS-7345) · [Faster Algorithms for Global Minimum Vertex-Cut in Directed Graphs](https://arxiv.org/abs/2512.24355v1) · [Approximating Directed Connectivity in Almost-Linear Time](https://arxiv.org/abs/2512.00176v1) · [Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs](https://arxiv.org/abs/2512.09080v3)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7244 — Boolean dimension of posets with planar cover graphs

The cover graph records which pairs in a finite partial order are immediately comparable, with edge directions forgotten. The question asks whether planarity of that graph guarantees a universal constant number of total orders encoding every comparability. One Boolean function decodes the comparison bits for all distinct ordered pairs, and both that function and the auxiliary orders may vary with the poset. The orders need not extend the partial order, and no upward planar diagram or unique minimal element is assumed. Known bounds with additional structural hypotheses leave the general question open in the checked sources and motivate its connection to concise reachability labels.

[Read in atlas](index.html#TCS-7244) · [Boolean dimension and dim-boundedness: Planar cover graph with a zero](https://arxiv.org/abs/2206.06942v2) · [Cliquewidth and dimension](https://arxiv.org/abs/2308.11950v3) · [Cliquewidth and dimension](https://doi.org/10.1112/plms.70116) · [Boolean dimension of a Boolean lattice](https://arxiv.org/abs/2307.16671v2) · [List of open questions: Boolean dimension of planar posets](https://a3nm.net/work/research/questions/#boolean-dimension-of-planar-posets)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7285 — Strongly explicit Ramanujan families for every degree

A regular Ramanujan graph meets the optimal asymptotic bound on nontrivial adjacency eigenvalues. The question asks for an infinite family at every fixed degree at least three. One algorithm must compute each local port connection in time polynomial in the vertex-label length. The family may use only a decidable unbounded set of sizes and permits the stated multigraph conventions. Constructions with positive spectral slack or slower global access do not meet the exact strong-explicitness target.

[Read in atlas](index.html#TCS-7285) · [Explicit expanders of every degree and size](https://arxiv.org/abs/2003.11673)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-0611 — Bipartite Exact Matching: deterministic polynomial time

Bipartite Exact Matching asks whether a perfect matching can have exactly a specified number of red edges. The target is one deterministic algorithm with polynomial running time in an explicit bit encoding. Minimum and maximum red counts do not determine which intermediate counts are attainable. An April 2026 preprint claims a solution, but its stated Lean formalization retains eight structural hypotheses and the complete claim remains unaudited here. The card retains uncertain status and requires a complete Lean-checked proof of the historical algorithmic claim or its unconditional negation.

[Read in atlas](index.html#TCS-0611) · [Exact Matching: Algorithms and Related Problems](https://doi.org/10.4230/LIPIcs.STACS.2023.29) · [Bipartite Exact Matching in P](https://arxiv.org/abs/2604.01571v3) · [Exact Matching in Matrix Multiplication Time](https://arxiv.org/abs/2508.04081v2)
Existing status: `uncertain` · Summary written: 2026-09-17

### TCS-0771 — Polynomial-time computation of planar treewidth

Treewidth is the minimum largest-bag size minus one among all tree decompositions of a finite graph. The question asks whether one deterministic polynomial-time algorithm can compute that integer exactly for every planar graph. The input is only the finite graph, without a planar embedding, a tree decomposition or a bound on its width. Inspected results on cubic-graph hardness, polynomial-delay enumeration and planar grid bounds do not establish that polynomial-time algorithm or its nonexistence. A complete Lean answer must prove the stated uniform algorithm and its bound or prove the full negation for all candidate machines and polynomial bounds.

[Read in atlas](index.html#TCS-0771) · [Algorithms for Optimization Problems in Planar Graphs](https://doi.org/10.4230/DagRep.6.5.94) · [A Polynomial Delay Algorithm Generating All Potential Maximal Cliques in Triconnected Planar Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2025.21) · [Treewidth Is NP-Complete on Cubic Graphs](https://doi.org/10.4230/LIPIcs.IPEC.2023.7) · [An improved bound on the treewidth of planar graphs excluding a grid minor](https://arxiv.org/abs/2609.15596v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0594 — 3-colorability of diameter-two graphs

The problem asks whether three-colorability is decidable in deterministic polynomial time for every graph of diameter at most two. The graph is given explicitly, and it is not promised to be colorable. No sparsity, forbidden-cycle, degree or vertex-list restriction is imposed. The best general bound identified in the checked sources is subexponential, while a July 2026 polynomial-time result needs an additional four-cycle exclusion. The question isolates a precise structural boundary between easy complete graphs and the known hardness at diameter three.

[Read in atlas](index.html#TCS-0594) · [Colouring Graphs of Bounded Diameter, in Graph Colouring: from Structure to Algorithms](https://doi.org/10.4230/DagRep.9.6.125) · [Algorithms and Almost Tight Results for 3-Colorability of Small Diameter Graphs](https://doi.org/10.1007/s00453-014-9949-6) · [Faster 3-coloring of small-diameter graphs](https://arxiv.org/abs/2104.13860v1) · [List 3-coloring \(C_{4}\)-free graphs of diameter-2 in polynomial-time](https://arxiv.org/abs/2606.30282v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0775 — Optimal exact-distance label length for planar graphs

Each vertex receives a short binary label. The exact distance between two vertices must follow from their labels alone. The same decoder serves every graph of the chosen size. The target is the optimal asymptotic number of label bits. Current lower and upper bounds differ by a polynomial factor.

[Read in atlas](index.html#TCS-0775) · [Better Distance Labeling for Unweighted Planar Graphs](https://doi.org/10.1007/s00453-023-01133-z)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-2783 — Erdős girth conjecture

The girth conjecture asks for dense graphs with every short cycle forbidden. For each fixed k, the target is \(\Omega (n^{1+1/k})\) edges and girth at least \(2k+2\). The lower bound must hold for every sufficiently large n, with constants depending on k. The known cases are \(k=1,2,3,5\), as still recorded in July 2026. A resolution would sharpen fundamental lower bounds for routing and graph spanners.

[Read in atlas](index.html#TCS-2783) · [Space-Stretch Tradeoff in Routing Revisited](https://doi.org/10.4230/LIPIcs.DISC.2022.37) · [Unconditional Lower Bounds for Degree Fault Tolerant Spanners](https://arxiv.org/abs/2607.07576)
Existing status: `source_open` · Summary written: 2026-09-12

## Data structures (17)

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

A dictionary stores word-sized keys and values while keys are repeatedly inserted and deleted. Every lookup must return its answer in constant worst-case time, and updates share a constant amortized budget. The question asks whether a uniform deterministic program can achieve these bounds using space linear in a fixed capacity. Randomized hashing gives the basic benchmark, while restricted deterministic lower bounds do not cover every permitted program. A solution must give a complete Lean-checked construction or impossibility proof with the specified machine and online guarantees.

[Read in atlas](index.html#TCS-7331) · [Research Statement](https://people.csail.mit.edu/mip/docs/job-application07/statements.pdf) · [Dynamic Perfect Hashing: Upper and Lower Bounds](https://www.cs.princeton.edu/research/techreps/15) · [Uniform deterministic dictionaries](https://pure.itu.dk/en/publications/uniform-deterministic-dictionaries/) · [Optimal Static Dictionary with Worst-Case Constant Query Time](https://arxiv.org/abs/2412.10655v2) · [Compressing Dynamic Fully Indexable Dictionaries in Word-RAM](https://arxiv.org/abs/2603.23119v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7338 — Multiphase conjecture

First, a data structure receives a polynomial-size family of subsets of a finite universe. It later receives another subset, and only afterward learns which stored set must be tested for disjointness. The conjecture requires polynomial overhead in at least one of the three normalized expected phase costs. The model permits arbitrary adaptive memory access, and recent restricted or Inner Product lower bounds do not cover the full target. An accepted resolution must be unconditional and completely checked in Lean with the stated quantifiers and zero-error guarantees.

[Read in atlas](index.html#TCS-7338) · [Towards Polynomial Lower Bounds for Dynamic Problems](https://www.ccs.neu.edu/~viola/classes/papers/PatrascuTowards.pdf) · [An Adaptive Step Toward the Multiphase Conjecture](https://arxiv.org/abs/1910.13543v1) · [Lower Bounds for Linear Operators](https://eccc.weizmann.ac.il/report/2025/155/) · [Unifying the Landscape of Super-Logarithmic Dynamic Cell-Probe Lower Bounds](https://eccc.weizmann.ac.il/report/2025/156/) · [An \(\Omega((\log n/\log\log n)^2)\) Cell-Probe Lower Bound for Dynamic Boolean Data Structures](https://eccc.weizmann.ac.il/report/2026/047/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0949 — Superlinear cell-probe lower bounds for succinct Boolean matrix-vector products

The input is an arbitrary Boolean matrix, stored using only a vanishing fraction of extra bits beyond its n²-bit information content. A query asks for the entire Boolean product with one vector, charging only logarithmic-word memory probes. The target asks whether every deterministic exact adaptive structure needs a worst-case probe count growing faster than n. Known strong tradeoffs retain the original matrix layout and count individual entries, so their scope and word-size conversion matter. The card keeps arbitrary succinct encodings and all subquadratic redundancies rather than substituting a narrower solved model.

[Read in atlas](index.html#TCS-0949) · [Sublinear.info](https://sublinear.info/index.php?title=Open_Problems:75) · [Faster Online Matrix-Vector Multiplication](https://arxiv.org/abs/1605.01695) · [Tight Cell Probe Bounds for Succinct Boolean Matrix-Vector Multiplication](https://arxiv.org/abs/1711.04467)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0300 — Randomized complexity of online labeling

An ordered list is stored using a fixed range of numerical labels. Insertions and deletions must preserve label order while keeping spare labels available. The cost counts how many existing items receive a different label. Randomization achieves nearly logarithmic expected amortized cost in the cited result. The remaining task is to determine the optimal asymptotic rate for constant slack.

[Read in atlas](index.html#TCS-0300) · [Computational Complexity of Discrete Problems](https://doi.org/10.4230/DagRep.7.3.45) · [Nearly Optimal List Labeling](https://arxiv.org/abs/2405.00807)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7328 — Amortized decrease-key complexity of standard pairing heaps

The standard pairing heap performs a left-to-right pairing pass and a right-to-left assembly pass when deleting the minimum. The question asks for the tight asymptotic amortized cost of decrease-key while keeping the stated charges for all other operations. The bound must hold on every finite sequence from empty heaps, in terms of the maximum simultaneous live-item count. Different heap variants and operation charges from separate analyses cannot be substituted; a 2026 improvement for standard heaps is recorded as an announcement. A complete Lean-checked upper analysis and matching lower bound are required, not just another improvement.

[Read in atlas](index.html#TCS-7328) · [Pure Pairing Heaps](https://arxiv.org/abs/2607.23118v1) · [Improved Upper Bounds for Pairing Heaps](https://arxiv.org/abs/1110.4428v1) · [Towards a Final Analysis of Pairing Heaps](https://doi.org/10.4230/DagSemProc.06091.5) · [On the Efficiency of Pairing Heaps and Related Data Structures](https://doi.org/10.1145/320211.320214)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7333 — Space-query exponent curve of 3SUM indexing

Two integer sets are stored before membership queries arrive. A query asks whether its number belongs to their sumset. The target is the best query exponent at each allowed storage exponent. All retained information is charged even though preprocessing time is unrestricted. The numerical curve target is broader than the saved polylogarithmic-query existence question.

[Read in atlas](index.html#TCS-7333) · [Conditional Lower Bounds for Space/Time Tradeoffs](https://arxiv.org/abs/1706.05847) · [Improved Time-Space Tradeoffs for 3SUM-Indexing](https://arxiv.org/abs/2512.04258v2)
Existing status: `uncertain` · Summary written: 2026-09-13

### TCS-7334 — Strong SetDisjointness conjecture

A family of sets is stored before the queries arrive. Each query names two stored sets and asks whether their intersection is empty. The conjecture says that retained space times squared query time cannot beat the squared total input size by more than polylogarithmic factors. Known upper bounds attain that tradeoff, while recent work still uses its lower-bound direction as an assumption. Preprocessing time is unrestricted and remains a separate resource from retained storage.

[Read in atlas](index.html#TCS-7334) · [Conditional Lower Bounds for Space/Time Tradeoffs](https://arxiv.org/abs/1706.05847) · [On the Hardness of Set Disjointness and Set Intersection with Bounded Universe](https://doi.org/10.4230/LIPIcs.ISAAC.2019.7) · [Towards Optimal Set-Disjointness and Set-Intersection Data Structures](https://doi.org/10.4230/LIPIcs.ICALP.2020.74) · [Acyclic Join Sampling Under Selections: Dichotomy, Union Sampling, and Enumeration](https://doi.org/10.4230/LIPIcs.ICDT.2026.9)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5825 — Superconstant word-RAM time for prefix-\(U_1\)

The prefix-U-one problem maintains a fixed-length bit sequence under substitutions and returns the AND of any requested prefix. The conjecture rules out a deterministic data structure with linear preprocessing and constant worst-case time for both operations. Its machine has logarithmic-size words and explicitly charged arithmetic, bit operations and memory accesses. Amortized constant time, expected constant time and stronger predecessor queries are separate questions. A resolution would settle a basic dynamic set barrier underlying conditional classifications for regular word and tree languages.

[Read in atlas](index.html#TCS-5825) · [Dynamic Membership for Regular Languages](https://doi.org/10.4230/LIPIcs.ICALP.2021.116) · [Dynamic data structures for parameterized string problems](https://arxiv.org/abs/2205.00441) · [Dynamic Membership for Regular Tree Languages](https://doi.org/10.4230/LIPIcs.MFCS.2025.8)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7329 — Logarithmic fully retroactive priority queues

A fully retroactive priority queue permits inserting and erasing queue operations anywhere in its current history. Every edit changes the queue obtained by replaying later historical operations, and minimum queries may refer to any time. The target is one deterministic comparison pointer-machine implementation with logarithmic amortized time and linear storage in the currently maintained history. All temporary storage and counter manipulation are charged, and histories remain valid without a monotonicity promise. The 2026 logarithmic result covers monotonic priority queues in its stated comparison model and leaves the general question open in that dated source.

[Read in atlas](index.html#TCS-7329) · [Retroactive Data Structures](https://erikdemaine.org/papers/Retroactive_TALG/) · [Polylogarithmic Fully Retroactive Priority Queues via Hierarchical Checkpointing](https://erikdemaine.org/papers/FullyRetroactive_WADS2015/) · [Retroactive Monotonic Priority Queues via Range Searching](https://arxiv.org/abs/2508.09892v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7340 — Optimal randomized memory-reallocation overhead

Objects of different sizes share one nearly full memory array. Every object must occupy a contiguous interval. An insertion or deletion may require moving other live objects. Cost compares the total moved volume with the size of the updated object. The remaining problem is the tight expected overhead as the unused fraction tends to zero.

[Read in atlas](index.html#TCS-7340) · [A Nearly Quadratic Improvement for Memory Reallocation](https://arxiv.org/abs/2405.12152) · [Memory Reallocation with Polylogarithmic Overhead](https://arxiv.org/abs/2602.15417v1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-6508 — Deque conjecture

Start with any binary search tree and update only the minimum or maximum end. New extrema become roots, while deleting an extremum first moves it to the root by standard bottom-up splaying. The conjecture asks whether total search and rotation work is linear in the initial size plus the number of operations. A known bound has an extremely slowly growing extra factor, and the 2026 general competitiveness result does not remove it here. A complete Lean-checked proof of the linear bound or an unbounded family of counterexample ratios is required.

[Read in atlas](index.html#TCS-6508) · [Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture](https://arxiv.org/abs/0707.2160v1) · [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0474 — Constant-update working-set heaps on pointer machines

The queue must support insertion, minimum lookup, priority decrease and minimum extraction online. An extraction is charged logarithmically in the number of insertions since that item arrived. The target combines that adaptive extraction cost with constant amortized charges for every other operation. The computation uses pointers, constant auxiliary bits and key comparisons; the checked recent results retain a growing factor in an update bound. A complete Lean-checked construction or unconditional refutation must cover every finite operation sequence.

[Read in atlas](index.html#TCS-0474) · [Adaptive and Scalable Data Structures — Working set heaps with decrease-key](https://doi.org/10.4230/DagRep.15.5.1) · [Near-Optimal Working-Set Heaps and Dijkstra on Pointer Machines](https://doi.org/10.4230/LIPIcs.ESA.2026.45) · [Heaps and Their Working Sets](https://arxiv.org/abs/2607.24621v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7327 — Buffered fully persistent search trees

The data structure stores every version of an ordered set and permits a new immutable version to be created from any old one. The target combines buffered insertions and deletions, queries charged by the size of their accessed version, and constant worst-case I/O cost for explicit cloning. All operation bounds must hold jointly over every finite online history with only two blocks of internal memory required and space linear in updates and clones. The 2025 source achieves buffered partial persistence and leaves efficient full-persistence cloning open, while the exact numerical combination here is explicitly editorial. A solution would unite efficient historical branching and buffered storage access without charging an extra constant transfer to every update.

[Read in atlas](index.html#TCS-7327) · [Buffered Partially-Persistent External-Memory Search Trees](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.82) · [External Memory Fully Persistent Search Trees](https://cs.au.dk/~gerth/papers/stoc23.pdf) · [Scalable Algorithms and Persistent Data Structures using Geometric Techniques](https://cs.au.dk/~gerth/advising/thesis/rolf-svenning.pdf) · [An I/O-Efficient Retroactive Buffer Tree for Bulk Operations in Temporal Databases](https://doi.org/10.1007/s10796-026-10782-8)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7330 — Combined depth and size bounds for confluently persistent tries

Confluent persistence lets a subtree be copied between historical trie versions while retaining all old versions. The question asks for one functional representation combining a shallow-update bound with a logarithmic bound in logical version size. Navigation has its own worst-case time bound and may not extend permanent version history. An update must pay for any earlier navigation records that its new stored version retains. The model and parameters explicitly cover multiple fingers, logical sharing, subtree copies and temporary versus permanent memory.

[Read in atlas](index.html#TCS-7330) · [Confluently Persistent Tries for Efficient Version Control](https://erikdemaine.org/papers/ConfluentTries_Algorithmica/paper.pdf)
Existing status: `source_open` · Summary written: 2026-09-13

## Dynamic algorithms (15)

### TCS-6625 — Deterministic fully dynamic connectivity with polylogarithmic worst-case updates

The data structure receives edge insertions, deletions and connectivity queries one at a time on an initially empty undirected graph. The question asks for one finite deterministic word-RAM program with exact answers, polynomial space and polylogarithmic time for every individual operation. A complete Lean answer must establish all guarantees or rule out every program and every choice of the fixed constants. Known amortized, randomized expected-time and deterministic subpolynomial results illustrate distinct guarantees around this target. A newly announced FOCS 2026 paper may affect the current status, but the inspected title-only sources do not establish whether its theorem matches the deterministic target.

[Read in atlas](index.html#TCS-6625) · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf) · [Dynamic graph connectivity in polylogarithmic worst case time](https://epubs.siam.org/doi/10.1137/1.9781611973105.81) · [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297) · [Logarithmic Lower Bounds in the Cell-Probe Model](https://erikdemaine.org/papers/DynamicConnectivity_SICOMP/) · [FOCS 2026 Accepted Papers](https://focs.computer.org/2026/accepted-papers/) · [Maximilian Probst Gutenberg — publications](https://sites.google.com/view/maximilianprobst/)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-6627 — Fully dynamic near-optimal matching with polylogarithmic updates

The graph undergoes online edge insertions and deletions, and the algorithm must maintain the actual edges of a near-maximum matching. For every fixed accuracy it must have polylogarithmic expected amortized update time, including linear initialization in the total cost. The sequence is fixed independently of the algorithm’s randomness, and one high-probability event must guarantee correctness throughout each polynomial-length sequence. The matching is stored explicitly with constant-time mate and cardinality access, and every change to that representation is charged. A complete Lean-checked solution must establish all these guarantees or refute them; size estimation and maximal matching solve different tasks.

[Read in atlas](index.html#TCS-6627) · [Sixteenth Biennial Scientific Report: March 2021–March 2023](https://pure.mpg.de/rest/items/item_3527212_4/component/file_3527885/content) · [Fully Dynamic Matching: \((2-\sqrt2)\)-Approximation in Polylog Update Time](https://epubs.siam.org/doi/10.1137/1.9781611977912.109) · [Improved Bounds for Fully Dynamic Matching via Ordered Ruzsa-Szemerédi Graphs](https://arxiv.org/abs/2406.13573v2) · [On Approximate Fully-Dynamic Matching and Online Matrix-Vector Multiplication](https://arxiv.org/abs/2403.02582v1) · [A note on Ordered Ruzsa-Szemerédi graphs](https://arxiv.org/abs/2502.02455v1) · [A Faster Deterministic Algorithm for Fully Dynamic Maximal Matching](https://arxiv.org/abs/2605.00797v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6626 — Polylogarithmic worst-case updates for exact dynamic minimum spanning forests

The data structure receives insertions and deletions of weighted edges in an initially empty simple graph. After every update it must report the changes to the exact minimum spanning forest with fixed tie-breaking. The target combines a hard polylogarithmic update-time cap with simultaneous high-probability correctness over every polynomial-length oblivious sequence. A complete Lean proof must cover the charged word-RAM computation, polynomial initialization and space, and all program and probability quantifiers, or refute the full allowed class. Amortized bounds, subpolynomial worst-case bounds, approximate forests and logarithmic rank-query counts do not settle this exact maintenance question.

[Read in atlas](index.html#TCS-6626) · [Poly-Logarithmic Deterministic Fully-Dynamic Algorithms for Connectivity, Minimum Spanning Tree, 2-Edge, and Biconnectivity](https://u.cs.biu.ac.il/~rodittl/p723-holm.pdf) · [Faster Fully-Dynamic Minimum Spanning Forest](https://arxiv.org/abs/1407.6832) · [Dynamic Minimum Spanning Forest with Subpolynomial Worst-case Update Time](https://arxiv.org/abs/1708.03962) · [A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond](https://arxiv.org/abs/1910.08025) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297) · [Deterministic Rounding of Dynamic Fractional Matchings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.27) · [Dynamic Matroids: Base Packing and Covering](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.57)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6670 — Polylogarithmic maintenance of the exact global minimum cut

The global minimum cut is the minimum number of edges crossing any nonempty proper vertex subset, with value zero for a disconnected graph. The question asks for one randomized data structure returning that exact value while arbitrary legal edge insertions and deletions arrive online. It requires polylogarithmic expected amortized updates, polylogarithmic worst-case queries and polynomial space, with explicit initialization cost and uniform exponents. For each fixed oblivious polynomial-length operation sequence, all answers must be simultaneously correct with error probability at most \(n^{-3}\). A complete Lean proof must establish the whole guarantee or its unconditional impossibility; approximate, small-cut, insertion-only and fast-update/slow-query results do not suffice.

[Read in atlas](index.html#TCS-6670) · [Deterministic and Exact Fully-dynamic Minimum Cut of Superpolylogarithmic Size in Subpolynomial Time](https://arxiv.org/abs/2512.13105) · [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://people.csail.mit.edu/virgi/6.s078/papers/omv.pdf) · [Incremental Exact Min-Cut in Polylogarithmic Amortized Update Time](https://arxiv.org/abs/1611.06500) · [Fully Dynamic Exact Edge Connectivity in Sublinear Time](https://arxiv.org/abs/2302.05951) · [Tree-Packing Revisited: Faster Fully Dynamic Min-Cut and Arboricity](https://link.springer.com/article/10.1007/s00453-026-01394-4) · [Fully Dynamic Approximate Minimum Cut in Subpolynomial Time per Operation](https://arxiv.org/abs/2412.15069) · [Faster Pseudo-Deterministic Minimum Cut](https://arxiv.org/abs/2602.14550) · [Simple Algorithms for Fully Dynamic Edge Connectivity](https://epubs.siam.org/doi/abs/10.1137/1.9781611978964.31)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7332 — Logarithmic Las Vegas dynamic connectivity

An undirected graph changes by single-edge insertions and deletions. Connectivity queries must always return the exact answer. The target is logarithmic amortized expected update time and logarithmic worst-case query time. Known guarantees either retain an iterated-logarithm update overhead or use a larger polylogarithmic bound. A complete Lean-checked answer must respect online access, the fixed-sequence adversary and near-linear current-graph space.

[Read in atlas](index.html#TCS-7332) · [Fully Dynamic Connectivity in \(O(\log n(\log\log n)^2)\) Amortized Expected Time](https://theoretics.episciences.org/10791/pdf) · [Logarithmic Lower Bounds in the Cell-Probe Model](https://erikdemaine.org/papers/DynamicConnectivity_SICOMP/) · [Dynamic Connectivity with Expected Polylogarithmic Worst-Case Update Time](https://arxiv.org/abs/2510.08297v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0478 — Dynamic APSP with edge-linear updates

The data structure maintains exact directed distances while individual weighted edges change. The supplied capacity m bounds the number of live edges throughout an arbitrary online operation sequence. The requested update charge is m times a fixed polylogarithmic factor, with polylogarithmic worst-case distance queries. The deterministic model allows polynomial preprocessing and space but requires the operation bound after preprocessing for every finite prefix. The review separates this sparse exact target from near-quadratic, approximate and planar offline results.

[Read in atlas](index.html#TCS-0478) · [Scalable Data Structures — Dynamic All Pairs Shortest Paths](https://doi.org/10.4230/DagRep.11.1.1) · [A New Approach to Dynamic All Pairs Shortest Paths](https://www.diag.uniroma1.it/~demetres/docs/dapsp-full.pdf) · [Bootstrapping Dynamic APSP via Sparsification](https://doi.org/10.4230/LIPIcs.ESA.2025.113) · [A Near-Optimal Offline Algorithm for Dynamic All-Pairs Shortest Paths in Planar Digraphs](https://arxiv.org/abs/2606.01809v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7326 — Worst-case logarithmic dynamic planar convex hulls

Maintain an arbitrary changing set of exact points in the plane, starting from the empty set. Insertions and deletions may occur in any order, and a query asks for one point farthest in a supplied direction. The target is deterministic logarithmic worst-case time for each operation and linear total space. Known optimal amortized bounds and recent practical implementations do not provide that per-operation guarantee. The answer must be a complete Lean-checked construction or unconditional refutation in the specified real-arithmetic model.

[Read in atlas](index.html#TCS-7326) · [Dynamic Planar Convex Hull](https://arxiv.org/abs/1902.11169v1) · [Engineering Fully Dynamic Convex Hulls](https://doi.org/10.4230/LIPIcs.SEA.2026.22)
Existing status: `source_open` · Summary written: 2026-09-17

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

## String algorithms and computational biology (25)

### TCS-6623 — Worst-case sample complexity of trace reconstruction

A deletion trace keeps each bit of one unknown binary string independently and hides the original positions of surviving bits. The target is the minimum fixed number of traces permitting exact reconstruction with success probability at least two thirds for every string. Determine this number within multiplicative constant factors in length for each fixed deletion probability, allowing the constants to depend on that probability. The estimator may be any randomized statistical kernel, so the required Lean lower bound covers unrestricted computation as well as efficient algorithms. The July 2026 quasipolynomial upper bound improves general sample complexity but does not match the polynomial lower bound or determine the requested scale.

[Read in atlas](index.html#TCS-6623) · [New lower bounds for trace reconstruction](https://www.math.kent.edu/~zchase/tr_lower.pdf) · [New upper bounds for trace reconstruction](https://arxiv.org/abs/2009.03296) · [Trace Reconstruction from Local Statistical Queries](https://arxiv.org/abs/2407.11177) · [Near-Optimal Trace Reconstruction for Mildly Separated Strings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.3) · [New Bounds for Circular Trace Reconstruction](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.30) · [Quasipolynomial Trace Reconstruction](https://arxiv.org/abs/2607.04073) · [Degree Sequence Reconstruction from Subgraph Traces](https://arxiv.org/abs/2609.09397)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6624 — Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time

Edit distance is the minimum number of unit-cost insertions, deletions and substitutions transforming one string into another. The question asks for one randomized algorithm with a universal constant approximation factor and only a fixed polylogarithmic overhead beyond linear input length. Its runtime must hold on every execution and its probability of a correct multiplicative estimate must be at least two thirds separately on every pair. Known fixed-slack constant-factor algorithms and earlier subpolynomial or additive approximations do not meet all these requirements simultaneously. The target remains distinct from the two retained questions about arbitrarily accurate estimates at slower stated runtimes.

[Read in atlas](index.html#TCS-6624) · [Edit Distance in Near-Linear Time: It’s a Constant Factor](https://epubs.siam.org/doi/10.1137/21M1392322) · [Edit Distance in Near-Linear Time: it’s a Constant Factor — full manuscript](https://arxiv.org/abs/2005.07678v2) · [Approximating Edit Distance in Near-Linear Time](https://arxiv.org/abs/1109.5635v1) · [Constant factor approximations to edit distance on far input pairs in nearly linear time](https://arxiv.org/abs/1904.05459v2) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702v1) · [Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)](https://arxiv.org/abs/1412.0348v4)
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

LCS is the longest sequence obtainable by deleting symbols from each input while preserving their order. The card asks for an explicit common subsequence within one absolute constant factor of optimum. One randomized algorithm must work on every growing-alphabet input in almost-linear worst-case time. Known guarantees with a growing factor or a much larger time bound do not settle this endpoint. A complete Lean-checked answer must prove the precise existence claim or its unconditional negation.

[Read in atlas](index.html#TCS-7371) · [Exploring the Gap Between LCS and LCStr](https://doi.org/10.4230/LIPIcs.CPM.2026.27) · [Approximating the Longest Common Subsequence problem within a sub-polynomial factor in linear time](https://arxiv.org/abs/2112.08454v1) · [Deterministic Longest Common Subsequence Approximation in Near-Linear Time](https://arxiv.org/abs/2507.22486v1) · [Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time](https://arxiv.org/abs/2603.29702v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7367 — Text-to-pattern Hamming distances below the square-root barrier

The input is an explicit text and pattern over a polynomial-size integer alphabet. The output contains the exact number of mismatches at every alignment, in order. The target improves the square-root dependence on pattern length by one fixed positive exponent. Randomness may affect running time but must never produce an incorrect terminating answer. Acceptance requires a complete Lean-checked proof or refutation in the stated uniform word-RAM model.

[Read in atlas](index.html#TCS-7367) · [Faster Algorithms for Text-to-Pattern Hamming Distances](https://arxiv.org/abs/2310.13174v3) · [New Applications of 3SUM-Counting in Fine-Grained Complexity and Pattern Matching](https://arxiv.org/abs/2410.20764v1) · [Hamming Distance Oracles](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7366 — Linear-space k-mismatch indexing with fast queries

A fixed text is indexed so that later patterns can be searched with at most a fixed number of substitutions. Every matching starting position must be reported exactly, including overlaps. The user-selected target is linear word space with query cost O(m+log^k(n) log log(n)+occ) for each fixed k at least two. The guarantee must hold for all pattern lengths and an alphabet that can grow to the text length. A complete Lean-checked answer must prove or refute these simultaneous bounds; slower-query linear-space trade-offs do not suffice.

[Read in atlas](index.html#TCS-7366) · [Space-Efficient k-Mismatch Text Indexes](https://arxiv.org/abs/2510.26264v1) · [A Linear Size Index for Approximate String Matching](https://cpm.cs.helsinki.fi/cpm06/03-tam.pdf) · [A linear size index for approximate pattern matching](https://doi.org/10.1016/j.jda.2011.04.004) · [Lower bounds for text indexing with mismatches and differences](https://hal.science/hal-01960182)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7369 — Space-query exponent curve of gapped string indexing

A query supplies two patterns and an interval of allowed distances between their starting positions in a fixed text. The index must report every ordered pair of matching starts in the interval, including valid overlaps. The target is the optimal stored-space exponent throughout a fixed range of query-overhead exponents. Uniform programs have polynomial preprocessing, bounded error for each fixed query, and worst-case bounds counting query workspace. The original 2024 binary question was answered positively; this editorial curve requires certified real-valued accuracy of 1/100 at every point.

[Read in atlas](index.html#TCS-7369) · [Gapped String Indexing in Subquadratic Space and Sublinear Query Time](https://arxiv.org/abs/2211.16860v2) · [A General Technique for Searching in Implicit Sets via Function Inversion](https://arxiv.org/abs/2311.12471v2) · [Improved Time-Space Tradeoffs for 3SUM-Indexing](https://arxiv.org/abs/2512.04258v2)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7374 — Almost-quadratic unweighted tree edit distance

The inputs are two explicit rooted ordered trees with integer vertex labels. Unit-cost edits insert, delete or relabel individual vertices while preserving the order of surviving children. The target is the exact edit distance in almost-quadratic worst-case time using one deterministic program. Recent static and derandomization results improve the cubic bound but do not reach this target. A complete Lean-checked answer must prove or refute the proposition with the stated edit convention and quantifiers.

[Read in atlas](index.html#TCS-7374) · [Faster Weighted and Unweighted Tree Edit Distance and APSP Equivalence](https://arxiv.org/abs/2411.06502v3) · [Deterministic Monotone Min-Plus Product and Convolution](https://arxiv.org/abs/2605.07150v2) · [Hardness of Dynamic Tree Edit Distance and Friends](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.78) · [Faster Algorithm for Bounded Tree Edit Distance in the Low-Distance Regime](https://arxiv.org/abs/2507.02701v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6513 — Constant-factor approximation of the smallest grammar

The input is any explicit string over an integer alphabet that may grow with its length. The algorithm must output an acyclic grammar whose unique expansion is that string. Grammar size counts all symbols on production right-hand sides, and the target is one universal constant times the optimum. The algorithm must be deterministic and polynomial in the full input bit length; known small-factor hardness does not rule out every constant. A complete Lean-checked proof or unconditional refutation is required, with any conditional hardness result clearly distinguished.

[Read in atlas](index.html#TCS-6513) · [On the Complexity of the Smallest Grammar Problem over Fixed Alphabets](https://doi.org/10.1007/s00224-020-10013-w) · [The Smallest Grammar Problem](https://doi.org/10.1109/TIT.2005.850116) · [Assembly Theory and the Smallest Grammar Problem](https://arxiv.org/abs/2608.19228)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6928 — Linear-space encoding from smallest string attractors

A string attractor is a set of positions crossed by some occurrence of each distinct nonempty substring. Its minimum size gamma measures repetitiveness without selecting a particular compression format. The question asks whether every string has a lossless code using only O(gamma) logarithmic-size words, including all metadata. The encoder and decoder are uniform and must terminate, but there is no time bound or fast-query requirement. A complete Lean-checked proof or refutation must cover arbitrary allowed strings and arbitrary computable lossless representations.

[Read in atlas](index.html#TCS-6928) · [Indexing Highly Repetitive String Collections](https://arxiv.org/abs/2004.02781v10) · [Substring Complexity in Sublinear Space](https://doi.org/10.4230/LIPIcs.ISAAC.2023.12) · [Generalization of Repetitiveness Measures for Two-Dimensional Strings](https://doi.org/10.1007/s00224-025-10244-9)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7297 — Optimal \(\ell_{1}\) distortion of binary edit distance

Binary edit distance counts unit-cost insertions, deletions and substitutions. One map of all length-n strings into a finite-dimensional l1 space must preserve every distance within a common multiplicative distortion. The dimension, real coordinates and computation needed to obtain the map are unrestricted. Verified bounds range from logarithmic distortion to the Ostrovsky–Rabani subpolynomial upper bound. The retained question asks for matching bounds within universal constant factors; recent distance algorithms and similarity-measure embeddings give different guarantees.

[Read in atlas](index.html#TCS-7297) · [Low Distortion Embeddings for Edit Distance](https://web.cs.ucla.edu/~rafail/PUBLIC/68.pdf) · [Improved lower bounds for embeddings into L1](https://www.wisdom.weizmann.ac.il/~robi/papers/KR-EmbedLB-SODA06.pdf) · [Nonembeddability theorems via Fourier analysis](https://web.math.princeton.edu/~naor/homepage%20files/nonembed-final-new.pdf) · [Edit Distance in Near-Linear Time: it's a Constant Factor](https://arxiv.org/abs/2005.07678v2) · [Embeddings into Similarity Measures for Nearest Neighbor Search](https://doi.org/10.1109/FOCS63196.2025.00045)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7362 — Optimal top-k document retrieval in compact space

The task is a static index for an ordered collection of strings using space proportional to their packed text size. A query ranks documents by the exact number of occurrences of an arbitrary pattern, counting overlaps. It must output the requested best identifiers in frequency order in time proportional to the packed pattern length plus k. The 2025 compressed-index result has additional space costs and stronger guarantees only in restricted output or pattern regimes. Acceptance requires a complete Lean-checked proof or refutation with uniform deterministic algorithms and the full stated bounds.

[Read in atlas](index.html#TCS-7362) · [Top-k Document Retrieval in Compressed Space](https://users.dcc.uchile.cl/~gnavarro/ps/soda25.pdf) · [Time-Optimal Top-k Document Retrieval](https://doi.org/10.1137/140998949)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7365 — General-alphabet Hamming oracles with optimal preprocessing

Two strings are preprocessed before their substring comparisons are known. Each query requests the exact Hamming distance between equal-length intervals. A parameter controls the allowed query time. The proposed preprocessing bound matches the constant-alphabet regime. Current general-alphabet bounds have a square-root loss in that parameter.

[Read in atlas](index.html#TCS-7365) · [Hamming Distance Oracles](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7322 — Optimal approximation ratio for shortest common superstring

A common superstring contains every supplied string as a contiguous substring. The objective is to minimize its length over the input alphabet. The target is the infimum approximation ratio of uniform deterministic polynomial-time algorithms. The algorithm must return a feasible string, with input and output costs measured in the stated bit model. The Lean benchmark accepts a certified value of this ratio within absolute error 0.01.

[Read in atlas](index.html#TCS-7322) · [A Tight Cycle-Cover Inequality for Shortest Common Superstring](https://eccc.weizmann.ac.il/report/2026/157/) · [Disproving the Greedy Superstring Conjecture](https://arxiv.org/abs/2609.01365)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-7360 — Polyloglogarithmic suffix-array access in compact space

A suffix array orders all nonempty suffixes of a binary string lexicographically. A query asks for the starting position of the suffix with a specified rank. The target is one deterministic static index family with linear bit space, including query workspace, and polynomial preprocessing. Each query must return its exact answer in worst-case time bounded by one fixed power of the double logarithm of the string length. Recent inverse-access and nonconstant lower-bound claims concern nearby thresholds and do not establish this particular forward-access guarantee.

[Read in atlas](index.html#TCS-7360) · [Compressed Inverse Suffix Arrays](https://arxiv.org/abs/2607.17287v2) · [Constant-Time Inverse Suffix Array Queries in Compact Space and Sublinear-Time Construction of Suffix Array Indexes](https://arxiv.org/abs/2608.19123v1) · [Cell-Probe Lower Bounds and Complexity-Preserving Reductions for Suffix Array Queries](https://arxiv.org/abs/2608.19172v1) · [Text Indexing and Searching in Sublinear Time](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2020.24)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-7364 — Preprocessing exponent of binary jumbled indexing

A query asks whether a binary text contains a contiguous substring with two specified symbol counts. The index must use linear word space and answer every query exactly in constant worst-case time. The numerical target is the infimum of deterministic preprocessing exponents, allowing a separate program for each positive exponent slack. The 2026 construction gives an exponent upper bound of 1.5 without determining the optimal value. Acceptance requires a complete unconditional Lean-checked approximation to that exponent within 0.01.

[Read in atlas](index.html#TCS-7364) · [On Hardness of Jumbled Indexing](https://arxiv.org/abs/1405.0189v1) · [Deterministic Monotone Min-Plus Product and Convolution](https://arxiv.org/abs/2605.07150v2) · [Binary jumbled indexing: suffix tree histogram](https://doi.org/10.1007/s10878-026-01407-6) · [Improved Time-Space Tradeoffs for 3SUM-Indexing](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.78)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7370 — Polynomial-time construction of minimum-density DNA minimizers

A DNA minimizer is determined by a total order on all strings of one fixed length. Its density is the probability that the selected position changes between consecutive random windows. The question asks for an exactly optimal order in deterministic time polynomial in its explicit size and the window parameter. Known exact search remains exponential in the number of distinct short strings, while practical low-density schemes have different guarantees. A complete Lean-checked answer must prove or refute the uniform polynomial bit-time construction for every allowed pair of parameters.

[Read in atlas](index.html#TCS-7370) · [GreedyMini: generating low-density DNA minimizers](https://pmc.ncbi.nlm.nih.gov/articles/PMC12261476/) · [Generating minimum-density minimizers](https://doi.org/10.64898/2026.01.25.701585) · [On Minimizers of Minimum Density](https://arxiv.org/abs/2506.05277v1) · [The Anti-Lexicographic SUS-Anchor: An Empirically Optimal Selection Scheme](https://doi.org/10.4230/LIPIcs.WABI.2026.22)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0467 — Linear-space LZ77 random access

A greedy LZ77 parse stores a string as literals and references to earlier material, including overlapping copies. The task is to return any chosen character in logarithmic worst-case time while using only a constant number of words per phrase. All stored input, auxiliary tables and query memory count toward that space bound. One deterministic construction may use polynomial time in the uncompressed length, and queries cannot consult the uncompressed text. Results for grammars, LZ-End and LZBE use different compressed-size parameters and do not automatically meet this target.

[Read in atlas](index.html#TCS-0467) · [Adaptive and Scalable Data Structures — Two problems on Lempel-Ziv compression](https://doi.org/10.4230/DagRep.15.5.1) · [Balancing Straight-Line Programs](https://arxiv.org/abs/1902.03568v5) · [Random Access to LZ-End: Faster and Deterministic](https://arxiv.org/abs/2607.14923v1) · [Random Access in Grammar-Compressed Strings: Optimal Trade-Offs in Almost All Parameter Regimes](https://doi.org/10.4230/LIPIcs.ICALP.2026.86) · [LZBE: An LZ-Style Compressor Supporting O(log n)-Time Random Access](https://doi.org/10.4230/LIPIcs.CPM.2026.34)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7368 — A fixed exponent improvement for elastic-degenerate string intersection

Each input describes a language by concatenating one chosen string from each ordered segment of alternatives. The question asks whether the two languages contain a common entire string. The desired algorithm saves a fixed positive power below the matrix-multiplication-dependent length exponents while paying for both inputs. One bounded-error algorithm must satisfy the worst-case time bound for every combination of segment counts and explicit lengths. A complete Lean-checked answer must prove or refute this proposition; restricted pattern-matching results and conditional lower bounds alone do not settle it.

[Read in atlas](index.html#TCS-7368) · [Elastic-degenerate string comparison](https://doi.org/10.1016/j.ic.2025.105296) · [Elastic-Degenerate String Comparison](https://arxiv.org/abs/2411.07782v1) · [Pattern matching with Elastic-Degenerate strings and Elastic-Founder graphs](https://doi.org/10.1186/s13015-025-00289-3) · [Faster ED-String Matching with k Mismatches](https://arxiv.org/abs/2503.01388v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7361 — Input-optimal construction of compact inverse suffix arrays

The input is a binary text packed into machine words. The desired static index must answer the exact lexicographic rank of any suffix in constant worst-case time. All retained information and query workspace must occupy a linear number of bits. The question asks whether deterministic construction can take time proportional to the number of packed input words. An August 2026 preprint has a square-root-logarithmic construction gap and a conditional connection to faster Dictionary Matching, while this stronger endpoint remains status-uncertain.

[Read in atlas](index.html#TCS-7361) · [Constant-Time Inverse Suffix Array Queries in Compact Space and Sublinear-Time Construction of Suffix Array Indexes](https://arxiv.org/abs/2608.19123) · [Text Indexing and Searching in Sublinear Time](https://doi.org/10.4230/LIPIcs.CPM.2020.24)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-0468 — Linear-time LZ77 pattern matching

A text is supplied as literal and copy phrases, and the pattern is an explicit string. Copies may overlap themselves, so the decoded text can be much longer than the input representation. The question asks for exact deterministic occurrence detection in time and working space linear in the phrase count plus pattern length. The machine allows integer division, and all preprocessing is charged. Linear time for grammar input is known, but does not automatically give the required bound for LZ input; a complete Lean-checked answer is required.

[Read in atlas](index.html#TCS-0468) · [Adaptive and Scalable Data Structures](https://doi.org/10.4230/DagRep.15.5.1) · [Pattern matching in Lempel-Ziv compressed strings: fast, simple, and deterministic](https://arxiv.org/abs/1104.4203v1) · [Pattern Matching on Grammar-Compressed Strings in Linear Time](https://arxiv.org/abs/2111.05016v1) · [Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts](https://doi.org/10.1007/s00224-026-10266-x)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0470 — Grammar random access in \(O(g\log g)\) bits

A binary straight-line grammar may describe a string exponentially longer than its list of rules. The question asks for exact character access in logarithmic time using total persistent storage of O(g log g) bits. The representation must be constructed in polynomial time from the grammar itself. All retained lengths, tables and grammar bits are charged, while each query has explicitly bounded temporary workspace. The reviewed 2026 results retain a larger expansion-length space scale; a complete Lean-checked proof or refutation of this smaller-space target is required.

[Read in atlas](index.html#TCS-0470) · [Adaptive and Scalable Data Structures](https://doi.org/10.4230/DagRep.15.5.1) · [Space-Efficient SLP Encoding for \(O(\log N)\)-Time Random Access](https://doi.org/10.1007/s00224-025-10243-w) · [Random Access in Grammar-Compressed Strings: Optimal Trade-Offs in Almost All Parameter Regimes](https://doi.org/10.4230/LIPIcs.ICALP.2026.86)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7375 — Fully functional suffix trees in BWT-run-linear total space

A binary text with a sentinel determines a suffix tree and a run count in its Burrows–Wheeler transform. The target stores the entire specified navigation and direct-access interface in space proportional to that run count. Every query must be exact and take polylogarithmic worst-case time after deterministic polynomial-time construction. The space budget includes the text representation and any access oracle, which distinguishes the target from recent partial-interface results. A complete Lean-checked answer must establish or refute all of these guarantees simultaneously.

[Read in atlas](index.html#TCS-7375) · [Fully-Functional Suffix Trees and Optimal Text Searching in BWT-runs Bounded Space](https://arxiv.org/abs/1809.02792v2) · [Compressing Suffix Trees by Path Decompositions](https://doi.org/10.4230/LIPIcs.ICALP.2026.24) · [Output-Sensitive Construction of CDAWGs from BWT-Runs](https://arxiv.org/abs/2607.01636v1) · [Suffixient Arrays: A New Efficient Suffix Array Compression Technique](https://doi.org/10.1007/s00224-026-10287-6) · [Non-overlapping Indexing in BWT-Runs Bounded Space](https://doi.org/10.1007/978-3-031-43980-3_21) · [Non-overlapping indexing in BWT-runs bounded space](https://doi.org/10.1016/j.tcs.2025.115512)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0466 — Certifying Karp–Rabin fingerprints

The input is a string, its alphabet size and a fixed prime modulus. The algorithm must certify that unequal substrings of every common length have different polynomial fingerprints. The target is worst-case n log n time with all preprocessing included. A bad fingerprint must always be rejected, while every good fingerprint must be certified with probability at least two thirds. Verification of selected lengths or construction of a different fingerprint does not settle the target; a complete Lean-checked answer is required.

[Read in atlas](index.html#TCS-0466) · [Adaptive and Scalable Data Structures](https://doi.org/10.4230/DagRep.15.5.1) · [Longest Common Extensions in Sublinear Space](https://arxiv.org/abs/1504.02671v1) · [Compressed Index with Construction in Compressed Space](https://doi.org/10.4230/LIPIcs.CPM.2026.25)
Existing status: `source_open` · Summary written: 2026-09-17

## Game theory, social choice and fair division (24)

### TCS-6632 — Constant-factor universally truthful auctions for submodular bidders

The auction allocates indivisible items to bidders with private normalized monotone submodular bundle valuations. The question asks for a constant expected-welfare approximation with universal truthfulness and polynomial communication in bidders, items and per-value bit precision. Local computation is unrestricted, but every query description, price, reply, allocation and payment must fit the bit bound. A complete Lean proof must establish the fixed-random-tape incentive inequality and all-profile welfare guarantee, or rule out every protocol in this full class. Value-query impossibility, graph eligibility results, growing approximation factors and budget-feasible procurement do not settle the selected target.

[Read in atlas](index.html#TCS-6632) · [Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068) · [On the Power of Randomization in Algorithmic Mechanism Design](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf) · [An Impossibility Result for Truthful Combinatorial Auctions with Submodular Valuations](https://arxiv.org/abs/1011.1830) · [Improved Truthful Mechanisms for Subadditive Combinatorial Auctions: Breaking the Logarithmic Barrier](https://arxiv.org/abs/2010.01420) · [The Communication Complexity of Combinatorial Auctions in Graphs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.27) · [From Compensation Design to Budget-Feasible Mechanisms: A Constant Approximation for Subadditive Valuations](https://arxiv.org/abs/2608.04337)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0011 — Existence of complete EFX allocations for additive valuations

The problem asks whether every instance with at least four agents and nonnegative additive values admits a complete EFX allocation of indivisible goods. Complete means that each good is assigned to exactly one agent, with empty bundles allowed. For every potentially envious agent i and other bundle \(A_{j}\), removing any good that i values positively must leave a bundle worth at most i’s own bundle. The statement permits zero values and fixes the positive-good EFX convention, without requiring payments or an efficient algorithm. Universal existence would establish this fairness guarantee despite the inability to divide individual goods.

[Read in atlas](index.html#TCS-0011) · [Problem 3: Does EFX always exist?](https://tcsopenproblems.com/problem/3)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6639 — Constant-factor approximation for Santa Claus

General Santa Claus allocation distributes indivisible items with arbitrary nonnegative additive agent-specific values to maximize the least agent value. The target is one uniform randomized algorithm with a constant approximation factor and polynomial running time in the full binary input length. It must output a feasible allocation on every tape and meet the common value threshold for all agents simultaneously with probability at least two thirds. A complete Lean proof must establish that guarantee or refute the entire stated algorithm class, retaining any complexity assumptions explicitly. Restricted-assignment constants, identical-preference results, relaxation gaps and distributed round bounds leave the general heterogeneous problem open in the inspected sources.

[Read in atlas](index.html#TCS-6639) · [Santa Claus meets Makespan and Matroids: Algorithms and Reductions](https://arxiv.org/abs/2307.08453) · [On Allocating Goods to Maximize Fairness](https://arxiv.org/abs/0901.0205) · [The Submodular Santa Claus Problem](https://arxiv.org/abs/2407.04824) · [Improved Integrality Gap in Max–Min Allocation, or, Topology at the North Pole](https://link.springer.com/article/10.1007/s00493-025-00141-7) · [Submodular Max-Min Allocation under Identical Valuations](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2026.8) · [Distributed Santa Claus via Global Rounding](https://arxiv.org/abs/2604.27983)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6674 — Randomized truthful unrelated-machine scheduling

Machines privately know an unrelated processing time for each job and receive payments for their assigned work. The target is the asymptotic optimal expected-makespan ratio of mechanisms truthful in expectation, with no computational restriction. Every job count and every finite nonnegative real cost matrix is allowed, and the approximation compares the expected maximum load with the fully informed optimum. A complete Lean proof must give matching constant-factor bounds, accounting for the possibility that the infimum is not attained. Existing general bounds leave a constant-to-linear gap; deterministic, universal-truthfulness and small-instance results have narrower scope.

[Read in atlas](index.html#TCS-6674) · [A proof of the Nisan–Ronen conjecture](https://arxiv.org/abs/2301.11905) · [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408) · [Setting Lower Bounds on Truthfulness](https://arxiv.org/abs/1507.08708) · [Randomized Truthful Mechanisms for Scheduling Unrelated Machines](https://link.springer.com/chapter/10.1007/978-3-540-92185-1_46) · [An Improved Randomized Truthful Mechanism for Scheduling Unrelated Machines](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2008.1314) · [New Bounds for Truthful Scheduling on Two Unrelated Selfish Machines](https://link.springer.com/article/10.1007/s00224-019-09927-x) · [Universally truthful mechanisms for scheduling](https://arxiv.org/abs/2609.12621)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6633 — Polynomial query complexity of exact envy-free cake cutting

The cake is a continuous interval whose value may differ arbitrarily between agents. The task is to allocate all of it exactly without any agent preferring another agent’s piece. Preferences are learned only through exact value and cut queries, and disconnected pieces are allowed. One deterministic protocol must use polynomially many queries on every profile, although computation between queries is unrestricted. A complete Lean-checked solution must prove the full protocol guarantee or rule out every such polynomial query bound.

[Read in atlas](index.html#TCS-6633) · [Cutting Down the Tower: Single-Exponential Envy-Free Cake Cutting](https://arxiv.org/abs/2609.05191v1) · [The Query Complexity of Cake Cutting](https://proceedings.neurips.cc/paper_files/paper/2022/file/f7a7bb369e48f10e85fce85b67d8c516-Paper-Conference.pdf) · [Thou Shalt Covet Thy Neighbor’s Cake](https://www.cs.umd.edu/~gasarch/TOPICS/cake/lbenvyfreesq.pdf) · [Envy-free cake cutting: a polynomial number of queries with high probability](https://doi.org/10.1007/s00355-025-01633-7)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6634 — Randomized metric distortion in social choice

What is the smallest universal expected metric distortion achievable from full voter rankings? The voting rule selects a lottery without seeing the distances that produced those rankings. The former value-two conjecture is false, with a general lower bound around 2.11264. A preprint dated 8 September 2026 states an upper bound of 2.13713, leaving a nonzero gap. The Lean benchmark accepts a certified determination with absolute error at most 0.01 throughout the stated numerical domain.

[Read in atlas](index.html#TCS-6634) · [Metric Distortion for Tournament Voting and Beyond](https://arxiv.org/abs/2505.13630) · [Metric Distortion Bounds for Randomized Social Choice](https://arxiv.org/abs/2111.03694) · [An improved bound for the randomized metric distortion problem](https://arxiv.org/abs/2608.17863) · [Improving Randomized Metric Distortion to 2.1441](https://arxiv.org/abs/2608.29308v2) · [Stable Voting Rules on the Edge of Optimal Metric Distortion](https://arxiv.org/abs/2609.08259v1)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7379 — Nonemptiness of the approval core

Each voter approves some candidates, and exactly a prescribed number of candidates must be selected. A voter coalition blocks the selection if its proportional share of seats can buy a committee that every member strictly prefers. The question is whether an unblocked committee always exists. Candidates are indivisible, have unit cost and cannot be selected more than once. A positive answer would establish universal feasibility of proportional coalition stability in approval voting.

[Read in atlas](index.html#TCS-7379) · [Nash Core in Multiwinner Election](https://arxiv.org/abs/2609.00486)
Existing status: `source_open` · Summary written: 2026-09-17

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

### TCS-7383 — Universal Condorcet dimension

A Condorcet winning set is a committee that a strict majority prefers to any single outsider. Each voter may prefer a different committee member when making that comparison. The question asks for the smallest committee size that is sufficient for every finite ranked election. The checked bounds are three and five, improving on the six-candidate result presented at TCS+. An accepted answer supplies a Lean-certified numerical estimate within 0.01 candidates of the universal minimum.

[Read in atlas](index.html#TCS-7383) · [Six Candidates Suffice to Win a Voter Majority](https://arxiv.org/abs/2411.03390) · [A few good choices](https://arxiv.org/abs/2506.22133) · [Is Four Enough? Automated Reasoning Approaches and Dual Bounds for Condorcet Dimensions of Elections](https://arxiv.org/abs/2604.19851)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0056 — Universal maximin-share approximation for additive goods

Each agent’s maximin share is the best value they can secure by partitioning the goods and receiving a least-valued bundle. The target is the largest fraction of those personal shares that can always be met simultaneously for nonnegative additive valuations. It ranges over all finite numbers of agents and indivisible goods, with equal entitlements and no sharing. Determining this constant would quantify the inherent loss of fairness caused by indivisibility, independently of computational efficiency. The card requires a Lean-certified absolute error of at most one hundredth and records the precise versions and limits of the known bounds.

[Read in atlas](index.html#TCS-0056) · [Best α for α-MMS existence](https://tcsopenproblems.com/problem/4) · [A tight negative example for MMS fair allocations](https://arxiv.org/abs/2104.04977v2) · [Improved Maximin Share Guarantee for Additive Valuations](https://arxiv.org/abs/2510.10423v1) · [An FPTAS for 7/9-Approximation to Maximin Share Allocations](https://arxiv.org/abs/2511.13056v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1115 — Polynomial-time EF1 and Pareto-optimal goods allocation

The task is to divide indivisible goods among agents whose nonnegative values add across goods. EF1 allows each agent’s envy of another bundle to disappear after the hypothetical removal of at most one good. Pareto optimality forbids any reassignment that improves one agent without hurting another. Allocations satisfying both properties exist, but the card asks for one polynomial-time algorithm on explicitly encoded rational values and arbitrary numbers of agents. Known pseudo-polynomial and fixed-agent algorithms do not settle this general bit-time requirement.

[Read in atlas](index.html#TCS-1115) · [Fair Division of Indivisible Goods: A Survey](https://arxiv.org/abs/2202.07551v2) · [A Polynomial-Time Algorithm for Fair and Efficient Allocation with a Fixed Number of Agents](https://doi.org/10.1007/978-3-032-18660-7_22) · [Fair and Efficient Balanced Allocation for Indivisible Goods](https://arxiv.org/abs/2603.05956v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1109 — EF1 and Pareto optimality for additive mixed items

Each participant may value an indivisible item positively, negatively or at zero. Every item must be assigned, and the participants have additive utilities and equal entitlements. EF1 permits eliminating each envy comparison by removing at most one item from one of the two bundles. The question is whether an allocation with this fairness guarantee can always also be Pareto optimal for at least three agents. Recent results settle pure chores and some alternative mixed-item fairness guarantees, but the checked 2026 sources do not resolve the unrestricted combination.

[Read in atlas](index.html#TCS-1109) · [Mixed Fair Division: A Survey](https://arxiv.org/abs/2306.09564v4) · [Existence of Fair and Efficient Allocation of Indivisible Chores](https://arxiv.org/abs/2507.09544v2) · [Introspectively Envy-Free and Efficient Allocation of Indivisible Mixed Manna](https://arxiv.org/abs/2509.18673v3) · [Weighted Fair Division of Indivisible Mixed Manna](https://arxiv.org/abs/2609.01580v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1108 — EF1 existence for arbitrary mixed-item utilities

Agents divide a finite set of indivisible items, and each agent may assign an arbitrary real utility to every bundle. The question asks whether a complete EF1 allocation always exists for three or more agents. For each envy comparison, EF1 permits ignoring at most one item from either the envious agent’s own bundle or the other bundle. An item’s effect may depend on its companions, so the model does not assume a fixed division into goods and chores. The 2026 existence results allowing one removal from each bundle do not settle this stricter one-item question.

[Read in atlas](index.html#TCS-1108) · [Mixed Fair Division: A Survey](https://arxiv.org/abs/2306.09564) · [Approximately Envy-free and Equitable Allocations of Indivisible Items for Non-monotone Valuations](https://doi.org/10.1609/aaai.v40i20.38712)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0073 — Polynomial-time mixed equilibria in coordination polymatrix games

Each player uses one action across several pairwise interactions in a graph. The two endpoints of each edge receive equal payoffs from that interaction. The target is a deterministic polynomial-time algorithm returning any exact mixed Nash equilibrium. Pure equilibria are permitted outputs, but an algorithm may also use genuinely mixed profiles. Known pure-equilibrium and adversarial two-team hardness results do not settle this coordination-only mixed search task.

[Read in atlas](index.html#TCS-0073) · [Equilibrium Computation](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.4.8.73) · [On Minmax Theorems for Multiplayer Games](https://people.csail.mit.edu/costis/network2.pdf) · [The Complexity of Two-Team Polymatrix Games with Independent Adversaries](https://arxiv.org/abs/2409.07398)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0571 — Pure positional Nash equilibria in reachability games

Every player in a finite deterministic turn-based game wants to visit their own target set at least once. The question asks for a Nash equilibrium in which each player always makes the same choice at the same vertex. A player testing a unilateral improvement may remember the entire play history while all other players keep their original choices. Equilibrium is required from one designated start, targets need not be absorbing, and neither a particular winning vector nor randomized strategies are allowed. A complete Lean-checked solution must prove universal existence or verify a counterexample; the 2026 randomized theorem leaves this pure all-reachability target open.

[Read in atlas](index.html#TCS-0571) · [24.2 Positional Nash Equilibria](https://automata.exchange/24.02-positional-nash-equilibria/) · [Simple Nash Equilibria for Qualitative Multiplayer Games](https://arxiv.org/abs/2607.07151v1)
Existing status: `source_open` · Summary written: 2026-09-17

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

## Algebraic computation (60)

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

The permanent sums one product of matrix variables for each permutation of the columns. The question is whether exact division-free arithmetic circuits over the complex numbers compute these polynomials with one polynomial size bound for all matrix dimensions. The selected model permits arbitrary complex constants, cancellations, unrestricted reuse and a different circuit at each dimension without a uniform generator. A complete Lean proof must establish such circuits or rule out every polynomial size bound, equivalently settling VP versus VNP in this model. The checked August polynomial lower bounds, constant-depth separations and September numerical approximation result do not settle the required general exact-circuit question.

[Read in atlas](index.html#TCS-0005) · [Mathematics and Computation](https://www.math.ias.edu/files/mathandcomp.pdf) · [Completeness Classes in Algebra](https://doi.org/10.1145/800135.804419) · [Superpolynomial Lower Bounds Against Low-Depth Algebraic Circuits](https://doi.org/10.1145/3734215) · [Arithmetic circuit lower bounds from sumset expansion](https://eccc.weizmann.ac.il/report/2026/138/) · [Circuit and Formula Lower Bounds for the Permanent](https://cdn.openai.com/pdf/ten-proofs-oai.pdf#page=114) · [Subexponential Approximation of the Permanent in Deterministic Polynomial Time](https://arxiv.org/abs/2609.10516)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6613 — Polynomial-size arithmetic formulas for the determinant

The symbolic determinant has n² commuting input variables for an n-by-n matrix. The question asks whether its exact polynomial can be expressed by arithmetic trees of size bounded by one fixed polynomial in n. Every occurrence of a variable, constant or copied subexpression is charged, while arbitrary fixed complex constants and cancellations are allowed. A complete Lean proof must establish such formulas for all dimensions or refute every polynomial size bound in the full nonuniform model. Cubic unrestricted lower bounds and superpolynomial multilinear lower bounds do not settle this equivalent formulation of VF versus VBP over the complex field.

[Read in atlas](index.html#TCS-6613) · [On computing the determinant in small parallel time using a small number of processors](https://www.sciencedirect.com/science/article/pii/0020019084900188) · [A Lower Bound for the Formula Size of Rational Functions](https://epubs.siam.org/doi/10.1137/0214050) · [Multi-Linear Formulas for Permanent and Determinant are of Super-Polynomial Size](https://eccc.weizmann.ac.il/report/2003/067/) · [Schur Polynomials do not have small formulas if the Determinant doesn’t!](https://arxiv.org/abs/1911.12520) · [Multilinear Formula Lower Bounds for Sparse Determinants](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2026.33) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6641 — Word problem for one-relation monoids

An ordinary one-relation monoid identifies words using one fixed reversible literal replacement rule in arbitrary surrounding contexts. The question asks whether a single algorithm can decide equality of any two words when the alphabet and defining relation are also supplied. Empty words and length-changing relations are allowed, and the algorithm must halt on unequal pairs as well as equal ones. Recent undecidability results for inverse monoids, submonoid membership and equations with unknowns concern different or broader problems. A resolution would locate a central decidability boundary for equality under minimal finite algebraic presentations.

[Read in atlas](index.html#TCS-6641) · [The word problem for one-relation monoids: a survey](https://link.springer.com/article/10.1007/s00233-021-10216-8) · [Correction to: The word problem for one-relation monoids: a survey](https://link.springer.com/article/10.1007/s00233-022-10310-5) · [On the Dehn functions of a class of monadic one-relation monoids](https://arxiv.org/abs/2210.16123) · [The word problem for two-generator one-relator inverse monoids](https://arxiv.org/abs/2608.04650) · [Membership problems for positive one-relator groups and one-relation monoids](https://doi.org/10.4153/S0008414X24000798) · [Undecidability of the Diophantine problem for one-relator groups and one-relation monoids](https://arxiv.org/abs/2608.01983v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6888 — Superpolynomial arithmetic formula lower bounds

The question asks whether the permanent requires arithmetic expression trees larger than every fixed polynomial bound. The trees compute formal polynomials over the complex numbers using addition and multiplication with arbitrary constants and unrestricted cancellations. This is the explicitly selected standard separation between polynomial-size formulas and VNP, represented by the permanent through its completeness theorem. Known bounds for restricted models and the inspected recent polynomial lower-bound claim do not establish the required unrestricted superpolynomial separation. A complete Lean answer must rule out every polynomial formula bound or prove that one polynomial bound suffices in every dimension.

[Read in atlas](index.html#TCS-6888) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Multi-Quadratic Sum-Of-Squares Lower Bounds Imply \(\mathrm{VNC}^{1}\ne\mathrm{VNP}\)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.113) · [Low-Depth Algebraic Circuit Lower Bounds over Any Field](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2024.31) · [Ten Advances in Mathematics and Theoretical Computer Science, Chapter 5: Circuit and Formula Lower Bounds for the Permanent](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) · [On the Tension Between Full-Rankness and Self-Reducibility for Set-Multilinear Polynomials](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.69)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6614 — Deterministic polynomial-time factorization over finite fields

The input is a densely written polynomial over a finite field whose polynomial-basis representation is supplied. The requested output is every monic irreducible factor, its multiplicity, and the original leading scalar. One deterministic algorithm must run in time polynomial in the degree and the logarithm of the field size for all valid inputs. Randomized methods, special decoding instances, averages over primes and characteristic-dependent bounds do not provide that guarantee. A complete Lean-checked proof must establish both universal correctness and the uniform bit-time bound, or prove their impossibility.

[Read in atlas](index.html#TCS-6614) · [Deterministic polynomial factorisation modulo many primes](https://arxiv.org/abs/2509.12705v1) · [Deterministic polynomial factoring over finite fields: a uniform approach via P-schemes](https://zeyuguo.bitbucket.io/papers/pscheme.pdf) · [Deterministic list decoding of Reed-Solomon codes](https://eccc.weizmann.ac.il/report/2025/170/revision/1/) · [On Factorization of Sparse Polynomials of Bounded Individual Degree](https://eccc.weizmann.ac.il/report/2026/036/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6642 — Conjugacy problem for one-relator groups

A one-relator group is specified by finitely many generators and a single word required to equal the identity. Two input words are conjugate when an unrestricted finite word transforms one into the other by conjugation inside that group. The question asks for one always-terminating algorithm receiving both the presentation and the two words, with no efficiency bound. Known word algorithms and recent undecidability of more general equation systems do not decide this particular task. A complete Lean-checked solution must verify a uniform decision algorithm or prove that the full input language is undecidable.

[Read in atlas](index.html#TCS-6642) · [The theory of one-relator groups: history and recent progress](https://arxiv.org/abs/2501.18306v1) · [Undecidability of the Diophantine problem for one-relator groups and one-relation monoids](https://arxiv.org/abs/2608.01983v1) · [The word problem for two-generator one-relator inverse monoids](https://arxiv.org/abs/2608.04650v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6677 — Isomorphism problem for one-relator groups

A finite one-relator presentation describes a group using finitely many generators and one explicitly written relation. The question asks for one algorithm deciding whether any two such presentations define isomorphic abstract groups, even with different generator counts. The answer must be exact and the algorithm must always terminate, but there is no running-time bound or geometric promise. A complete Lean proof must establish this uniform decision procedure or prove undecidability for the exact input class. Known hyperbolic and center subclasses, generic rigidity algorithms and the 2026 undecidability result for equations in fixed groups do not resolve the all-input comparison.

[Read in atlas](index.html#TCS-6677) · [The theory of one-relator groups: history and recent progress](https://arxiv.org/abs/2501.18306) · [The isomorphism problem for all hyperbolic groups](https://arxiv.org/abs/1002.2590) · [Generic properties of Whitehead's Algorithm and isomorphism rigidity of random one-relator groups](https://arxiv.org/abs/math/0303386) · [Small Cancellation Stability and Isomorphism Rigidity for Generic Finitely Presented Groups](https://arxiv.org/abs/2608.17238) · [Undecidability of the Diophantine problem for one-relator groups and one-relation monoids](https://arxiv.org/abs/2608.01983)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7113 — Derandomizing polynomial identity testing

An arithmetic circuit may compute the zero polynomial even when cancellation is difficult to see from its graph. The question asks for an exact deterministic polynomial-time test given the entire circuit over binary-encoded integer constants. Circuits may reuse intermediate results, have arbitrary depth and compute polynomials of exponential degree. Randomized polynomial-time tests are known, while removing their randomness would have major circuit lower-bound consequences. Recent deterministic results for restricted circuit shapes do not provide the requested algorithm for all explicit circuits.

[Read in atlas](index.html#TCS-7113) · [Enumeration Complexity: Incremental Time, Delay and Space](https://arxiv.org/abs/2309.17042) · [Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds](https://www.cs.sfu.ca/~kabanets/Research/poly.html) · [Homomorphism Indistinguishability, Multiplicity Automata Equivalence, and Polynomial Identity Testing](https://doi.org/10.4230/LIPIcs.STACS.2026.25) · [Polynomial Identity Testing and Reconstruction for Depth-4 Powering Circuits of High Degree](https://arxiv.org/abs/2602.20832v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7174 — Bit complexity of integer multiplication

What is the optimal worst-case bit complexity of multiplying two n-bit integers? The model charges individual steps of a fixed deterministic multitape Turing machine. An \(O(n \log  n)\) algorithm is known, but only a linear general lower bound is established. A 2025 theorem connects the conjectured matching lower bound to the unresolved cost of matrix transposition. Bounds for restricted branching programs do not determine the optimal cost in this model.

[Read in atlas](index.html#TCS-7174) · [Integer multiplication in time \(O(n \log  n)\): publisher abstract](https://annals.math.princeton.edu/2021/193-2/p04) · [Integer multiplication is at least as hard as matrix transposition](https://arxiv.org/abs/2503.22848) · [Upper and lower bounds on the OBDD-width of a special integer multiplication](https://arxiv.org/abs/2608.30664)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7262 — Strassen’s asymptotic rank conjecture

A three-factor tensor can be decomposed into elementary products, and its rank is the least number of those products. The question asks whether every concise complex tensor of equal factor dimension has asymptotic rank exactly that dimension when corresponding factors of many copies are grouped. The dimension and tensor stay fixed during the limit, and no tightness, symmetry, computability or uniform convergence promise is imposed. A complete Lean proof must establish the equality for all such tensors or a counterexample whose grouped powers all require a strictly larger exponential base. The inspected 2026 structural, numerical, finite-rank and symmetry results do not settle this general asymptotic equality.

[Read in atlas](index.html#TCS-7262) · [Asymptotic tensor rank is characterized by polynomials](https://arxiv.org/abs/2411.15789) · [Asymptotic rank bounds: a numerical census](https://arxiv.org/abs/2601.08119) · [The edge of the asymptotic spectrum of tensors](https://arxiv.org/abs/2604.01386) · [New lower bounds on tensor rank of \((2,n,m)\) matrix multiplication with GPT-6](https://arxiv.org/abs/2609.14393) · [Border rank lower bounds beyond weak border apolarity](https://arxiv.org/abs/2609.12121) · [Concise tensors with maximal symmetries](https://arxiv.org/abs/2609.17280)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6615 — Polynomial-time finite-group isomorphism in the Cayley-table model

Two finite groups are isomorphic when one bijection of their elements preserves every product. The input supplies both complete multiplication tables, and the target is deterministic polynomial-time decision in their explicit bit length. The algorithm must cover all finite groups without additional structural information. Recent algorithms for restricted families and lower bounds for shallow circuits do not settle this general target. A separate claimed general solution remains unverified in this review, so the card stays active with uncertain resolution status.

[Read in atlas](index.html#TCS-6615) · [The Parallel Dynamic Complexity of the Abelian Cayley Group Membership Problem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2024.4) · [Polynomial-time isomorphism test for k-generated extensions of abelian groups](https://arxiv.org/abs/2602.15497v2) · [Group Isomorphism and the Polylogarithmic-Time Hierarchy: Depth-\(2\frac12\) Circuits and Lower Bounds](https://arxiv.org/abs/2608.26257v1) · [Polynomial-time isomorphism test for solvable groups with abelian Sylow subgroups](https://arxiv.org/abs/2605.26748v2) · [Polynomial-Time Algorithms for 0-1 Matrix Isomorphism, Graph Isomorphism and Latin Squares](https://www.preprints.org/manuscript/202510.0113/v4)
Existing status: `uncertain` · Summary written: 2026-09-17

### TCS-6895 — Explicit three-dimensional tensors of superlinear rank

A three-way tensor is a cubic array, and its ordinary rank is the fewest rank-one arrays whose sum equals it. The selected branch asks for rational entries written by one deterministic algorithm in polynomial time in the dimension. Rank is measured over the complex numbers, and its ratio to the side length must tend to infinity. The algorithm must produce every dimension without advice, symbolic number-field entries or uncharged output bits. Known explicit linear border-rank bounds and recent semi-explicit high-rank constructions do not meet this superlinear rational-output target.

[Read in atlas](index.html#TCS-6895) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Towards Finding Hay in a Haystack: Explicit Tensors of Border Rank Greater Than 2.02m in the Triple Tensor Product of m-Dimensional Complex Spaces](https://doi.org/10.4086/toc.2025.v021a013) · [Arithmetic circuit lower bounds from sumset expansion](https://arxiv.org/abs/2607.15848v1)
Existing status: `source_open` · Summary written: 2026-09-16

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

### TCS-6897 — Permanent lower bounds from black-box identity testing

A hitting set is a list of inputs on which every nonzero polynomial in a specified circuit class has a nonzero value somewhere. The card asks whether a uniform polynomial-time generator of such sets for general rational arithmetic circuits forces the permanent to require more than polynomially many arithmetic edges. Both sides allow arbitrary rational constants in the circuits, while the generator must write its rational points within a polynomial bit-time bound on unary variable, degree and size parameters. The published question isolates a missing permanent lower bound beyond established consequences involving other hard polynomials or a disjunction with Boolean circuit hardness. The general-circuit black-box instance is explicitly sourced, its field and encoding conventions are disclosed, and the bounded review found no later result meeting the full implication.

[Read in atlas](index.html#TCS-6897) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf#page=67) · [Hardness-Randomness Tradeoffs for Algebraic Computation](https://mrinalkr.bitbucket.io/papers/hardness-randomness-survey.pdf#page=8) · [On Circuit Lower Bounds from Derandomization](https://theoryofcomputing.org/articles/v007a012/) · [Marginal Hitting Sets Imply Super-Polynomial Lower Bounds for Permanent](https://eccc.weizmann.ac.il/report/2011/133/) · [Tighter Connections between Derandomization and Circuit Lower Bounds](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2015.645) · [Polynomial-Time PIT from (Almost) Necessary Assumptions](https://arxiv.org/abs/2504.06044v1) · [A Note on Deterministic PIT for depth-four circuits with top fan-in three and constant bottom fan-in](https://eccc.weizmann.ac.il/report/2026/168/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0481 — Cubic min-plus circuit lower bounds for shortest paths

The input gives nonnegative real weights on every edge of a complete undirected graph. A fixed circuit of minimum and addition gates must compute the exact distance between two designated vertices. The question is whether every such single-output circuit requires a cubic number of gates. The source records cubic upper and quadratic lower bounds; all-pairs and single-source results have different output requirements. A complete Lean-checked proof of the cubic lower bound or its exact logical negation is required.

[Read in atlas](index.html#TCS-0481) · [Semirings in Databases, Automata, and Logic — Circuit Size for Reachability](https://doi.org/10.4230/DagRep.15.2.89) · [Lower Bounds for Tropical Circuits and Dynamic Programs](https://web.vu.lt/mif/s.jukna/ftp/tropical-manuscript.pdf) · [Is Bellman-Ford-Moore single source shortest paths (min,+) circuit optimal?](https://web.vu.lt/mif/s.jukna/tropical/problem-setA2.html)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6890 — Superpolynomial noncommutative circuit lower bounds

The target is some polynomial-degree family with rational coefficients and ordered noncommuting variables. One deterministic polynomial-time algorithm must compute any requested word coefficient exactly. Every polynomial size bound must fail for unrestricted arithmetic circuits over the complex numbers at arbitrarily large input lengths. Depth, sharing, intermediate degrees and complex constants are unrestricted, so formula or restricted-circuit bounds are insufficient. The answer must provide complete Lean-checked explicitness and circuit lower-bound proofs or prove the exact negation.

[Read in atlas](index.html#TCS-6890) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Separating ABPs and Some Structured Formulas in the Non-Commutative Setting](https://doi.org/10.4230/LIPIcs.CCC.2021.7) · [Lower Bounds for Noncommutative Circuits with Low Syntactic Degree](https://doi.org/10.4230/LIPIcs.ITCS.2026.115) · [A Quadratic Lower Bound for Noncommutative Circuits](https://arxiv.org/abs/2604.20575v3) · [Polynomial Lower Bounds for Arithmetic Circuits over Non-Commutative Rings](https://eccc.weizmann.ac.il/report/2026/061/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6893 — Superpolynomial multilinear circuit lower bounds

The target is a multilinear polynomial family in VNP over the complex numbers. VNP membership is specified by a bounded-degree polynomial-size circuit summed over polynomially many Boolean witness coordinates. The family must require more than every polynomial size bound for circuits whose every intermediate polynomial is multilinear. No particular family such as the permanent is prescribed, and no small unrestricted output circuits are required. The answer must include complete Lean-checked membership and lower-bound proofs or prove that all such families have polynomial-size semantic multilinear circuits.

[Read in atlas](index.html#TCS-6893) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Unbalancing Sets and an Almost Quadratic Lower Bound for Syntactically Multilinear Arithmetic Circuits](https://web.math.princeton.edu/~nalon/PDFS/mult2.pdf) · [Multilinear Algebraic Branching Programs and the Min-Partition Rank Method](https://eccc.weizmann.ac.il/report/2026/001/) · [Withdrawal: An Unconditional Barrier for Proving Multilinear Algebraic Branching Program Lower Bounds](https://arxiv.org/abs/2604.00746v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7223 — Linear-size circuits for integer multiplication

The input consists of two unsigned binary integers of the same width. The circuit must output every bit of their exact product on every input. The question is whether a constant times the input width always suffices in AND, OR and NOT gates. Known near-linear constructions and a conditional lower bound leave the unrestricted linear-size question unresolved in the checked sources. A complete Lean-checked proof of the circuit-family existence claim or its unconditional negation is required.

[Read in atlas](index.html#TCS-7223) · [Computational Complexity: A Conceptual Perspective (May 2007 author draft)](https://www.wisdom.weizmann.ac.il/~oded/CC/r6.pdf) · [Mathematics of the Impossible (author manuscript)](https://www.ccs.neu.edu/home/viola/papers/moti.pdf) · [Lower Bounds for Multiplication via Network Coding](https://doi.org/10.4230/LIPIcs.ICALP.2019.10)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7269 — Optimal multilinear-formula size of the permanent

The permanent is evaluated by a binary tree of exact additions and multiplications over the complex numbers. Every intermediate polynomial must be multilinear, while sharing is forbidden and arbitrary complex constants are allowed. The question asks for the asymptotic growth of the logarithm of the minimum formula size, up to constant factors. The known lower and upper scales for that logarithm are quadratic in log n and linear in n, respectively. A complete Lean-checked answer must match the upper and lower exponents for every sufficiently large matrix dimension.

[Read in atlas](index.html#TCS-7269) · [P=?NP](https://eccc.weizmann.ac.il/report/2017/004/) · [Multi-Linear Formulas for Permanent and Determinant are of Super-Polynomial Size](https://eccc.weizmann.ac.il/report/2003/067/) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Multilinear Formula Lower Bounds for Sparse Determinants](https://eccc.weizmann.ac.il/report/2026/090/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6884 — Semantic versus syntactic multilinear circuits

A multilinear polynomial uses each variable with exponent at most one in every nonzero monomial. Semantic multilinearity requires this property at every arithmetic-circuit gate after cancellation. Syntactic multilinearity instead requires the variable-occurrence sets entering each multiplication to be disjoint. The question asks whether one polynomial family over a fixed field can have polynomial semantic circuits but no polynomial syntactic circuits. Formulas admit size-preserving conversion, while the checked 2026 discussion retains the possibility of greater semantic power for circuits with shared outputs.

[Read in atlas](index.html#TCS-6884) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Multilinear Algebraic Branching Programs and the Min-Partition Rank Method](https://eccc.weizmann.ac.il/report/2026/001/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1058 — Explicit rigidity at rank n over log log n

The target is a deterministic polynomial-time construction of one binary square matrix at each dimension. Reducing its rank over F_2 to any fixed multiple of n divided by log log n must require changing at least n^(1+epsilon) entries. One positive epsilon and the same family must work for all fixed multiples, with a separate sufficiently-large-length threshold allowed. Random matrices, conditional constructions and unselected lists of candidates do not meet the target. A complete Lean-checked construction and rigidity proof, or the precise negation, is required.

[Read in atlas](index.html#TCS-1058) · [Boolean Function Complexity: Advances and Frontiers (author’s early draft)](https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf) · [Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank](https://doi.org/10.4230/LIPIcs.STACS.2026.28) · [Spiky Rank and Its Applications to Rigidity and Circuits](https://eccc.weizmann.ac.il/report/2026/030/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-2039 — Decidability of freeness in automaton groups

A finite invertible Mealy machine describes bijections of all finite words, whose compositions and inverses form an automaton group. The question asks for an always-terminating algorithm deciding whether that whole group is isomorphic to a free group of some finite rank. The supplied states may be redundant or act trivially, so they are not required to form the free basis. Known undecidability of positive relations and of general automaton semigroup freeness does not settle this group property, which a March 2026 specialist presentation still lists as open. A resolution would locate a basic limit of structural recognition from finite automaton descriptions.

[Read in atlas](index.html#TCS-2039) · [The Freeness Problem for Automaton Semigroups](https://doi.org/10.4230/LIPIcs.MFCS.2024.44) · [Automata, Dynamical Systems, and Groups](https://ievgenbondarenko.wordpress.com/wp-content/uploads/2016/10/automata-dynamical-systems-and-groups.pdf) · [Automaton Semigroups and Groups: On the Undecidability of Problems Related to Freeness and Finiteness](https://arxiv.org/abs/1712.07408v3) · [The Freeness Problem for Automaton Semigroups — St Andrews seminar handout](https://jan-philipp-waechter.bitbucket.io/slides/StAndrews2026_handout.pdf)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6883 — Multilinear versus general arithmetic circuits

The outputs are multilinear polynomials over the complex numbers. The question asks whether polynomial-size unrestricted circuits can be superpolynomially smaller than circuits that remain multilinear at every gate. Circuits may share arbitrary intermediate computations and use arbitrary complex constants. Formula and syntactic multilinear lower bounds do not establish the requested semantic-circuit separation. The review records that a related April 2026 barrier claim was withdrawn and requires a complete Lean-checked proof of the precise comparison or its negation.

[Read in atlas](index.html#TCS-6883) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Unbalancing Sets and an Almost Quadratic Lower Bound for Syntactically Multilinear Arithmetic Circuits](https://web.math.princeton.edu/~nalon/PDFS/mult2.pdf) · [Multilinear Algebraic Branching Programs and the Min-Partition Rank Method](https://eccc.weizmann.ac.il/report/2026/001/) · [Withdrawal: An Unconditional Barrier for Proving Multilinear Algebraic Branching Program Lower Bounds](https://arxiv.org/abs/2604.00746v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6903 — Deterministic noncommutative circuit identity testing in polynomial size and degree

The input is a complete circuit whose variables multiply as ordered words over the rational numbers. The algorithm must decide exactly whether every word coefficient in its output vanishes. It may use time polynomial in circuit size and a supplied bound on the actual output degree. One deterministic uniform program must handle arbitrary sharing and depth in an exact arithmetic model that also charges control work. A complete Lean-checked algorithm and running-time proof, or the logical negation, is required.

[Read in atlas](index.html#TCS-6903) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [Randomized Polynomial-Time Identity Testing for Noncommutative Circuits](https://theoryofcomputing.org/articles/v015a007/) · [Matrix identities are hard: Fast blackbox PIT for noncommutative exponential-size constant-depth homogeneous circuits](https://eccc.weizmann.ac.il/report/2026/173/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0055 — Sum-of-square-roots problem

The input describes a signed integer combination of square roots of positive integers using binary encodings. The question is whether one deterministic algorithm can decide exactly whether its value is nonnegative in polynomial time. All input magnitudes count toward the bit length, and zero or extremely small values are included. The original separation-bound question, equality testing, unary inputs and nonuniform circuit results provide related context without settling this target. A complete Lean proof must establish the uniform algorithm and its bound or prove that no such algorithm exists.

[Read in atlas](index.html#TCS-0055) · [The Open Problems Project, Problem 33: Sum of Square Roots](https://topp.openproblem.net/p33) · [An Improved Bound on Sums of Square Roots via the Subspace Theorem](https://doi.org/10.4230/LIPIcs.SoCG.2024.54) · [USSR is in P/poly](https://arxiv.org/abs/2310.19335v2) · [On the Order of Power Series and the Sum of Square Roots Problem](https://arxiv.org/abs/2304.13605v1) · [PosSLP and Sum of Squares](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.13)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6493 — Tensor orbit-closure intersection in \(\mathrm{NP}\cap\mathrm{coAM}\)

The input consists of two triples of Gaussian-rational matrices, with two dimensions allowed to grow. Each triple is acted on by simultaneous conjugation using a Kronecker product of two invertible complex matrices, and the decision asks whether the two orbit closures intersect. The selected source subquestion asks whether yes-instances have short NP certificates and no-instances have a polynomial-time public-coin Arthur–Merlin protocol. This is a complete representative of the tensor orbit-closure class, which includes graph isomorphism and tensor-network indistinguishability problems. A complete Lean proof must establish both certificate guarantees for all inputs or refute their conjunction, while the broader original exact-complexity question remains distinct.

[Read in atlas](index.html#TCS-6493) · [Complexity Theory of Orbit Closure Intersection for Tensors: Reductions, Completeness, and Graph Isomorphism Hardness](https://doi.org/10.1109/FOCS63196.2025.00027) · [Complexity theory of orbit closure intersection for tensors: reductions, completeness, and graph isomorphism hardness](https://arxiv.org/abs/2411.04639v2) · [Vanishing Signatures, Orbit Closure, and the Converse of the Holant Theorem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.32) · [Fixed-Parameter Degree Bounds and Complexity of the Orbit Closure Intersection Problem for Tensors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2026.32)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0010 — Superlinear constant-degree arithmetic circuit lower bounds

The goal is an explicit rational polynomial family of one fixed total degree. One deterministic polynomial-time algorithm must print every coefficient exactly. Every linear size bound must fail at arbitrarily large lengths for arithmetic circuits with unrestricted depth, sharing and complex constants. Any unbounded improvement over linear size suffices, without a prescribed exponent gap. The answer must supply complete Lean-checked explicitness and lower-bound proofs or prove that all such families have linear-size circuits.

[Read in atlas](index.html#TCS-0010) · [Mathematics and Computation (27 March 2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [Arithmetic circuit lower bounds from sumset expansion](https://arxiv.org/abs/2607.15848) · [Partition Rank and Algebraic Circuit Lower Bounds](https://arxiv.org/abs/2607.02241v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-3959 — Approximate polynomial satisfiability in AM under GRH

Approximate polynomial satisfiability asks whether a rational polynomial system can have all residuals arbitrarily close to zero over the complex numbers. The approximating points may diverge, so an exact common root need not exist. Equivalently, every algebraic relation among the input polynomials must have zero constant term. The question asks whether a polynomial-time public-coin interactive verifier can decide this under GRH; APS is currently known to be NP-hard and in PSPACE. A February 2026 extension treats containment of approximate solution sets in PSPACE and does not supply the requested AM bound.

[Read in atlas](index.html#TCS-3959) · [Algebraic Dependencies and PSPACE Algorithms in Approximative Complexity](https://doi.org/10.4230/LIPIcs.CCC.2018.10) · [Algebraic Dependencies and PSPACE Algorithms in Approximative Complexity over Any Field](https://doi.org/10.4086/toc.2019.v015a016) · [When Hilbert approximates: A Strong Nullstellensatz for Approximate Polynomial Satisfiability](https://eccc.weizmann.ac.il/report/2026/026/)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5240 — Does explicit multivariate hardness imply univariate hardness over F₂?

Assume an explicit family of multilinear polynomials over F₂ requires circuits of exponential size in its number of variables. The question asks whether some explicit family of univariate polynomials must then require size polynomial in its degree. Coefficients must be computable uniformly in exponential time in the first parameter and polynomial time in the second. Circuit complexity concerns exact formal polynomials and permits unrestricted arithmetic circuits with constants in F₂. The requested transfer is an existence implication, not a claim about one substitution, and requires a complete Lean-checked proof or refutation.

[Read in atlas](index.html#TCS-5240) · [Algebraic Hardness Versus Randomness in Low Characteristic](https://arxiv.org/abs/2005.10885v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6882 — Homogeneous versus unrestricted arithmetic formulas

A homogeneous polynomial has all its nonzero monomials at one ordinary total degree. The question compares arbitrary complex arithmetic formula trees with trees whose every intermediate polynomial is homogeneous. It asks for outputs with polynomial-size general formulas but no polynomial-size homogeneous formulas. Weighted homogeneity, multilinearity, monotonicity and bounded depth impose different restrictions and their lower bounds do not settle this target. The requested answer is a complete Lean-checked nonuniform family separation or proof that polynomial formula size always survives homogenization.

[Read in atlas](index.html#TCS-6882) · [Arithmetic Circuits: A Survey of Recent Results and Open Questions](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf) · [On the Power of Homogeneous Algebraic Formulas](https://eccc.weizmann.ac.il/report/2023/191/) · [On Approximate Symmetric Polynomials and Tightness of Homogenization Results](https://doi.org/10.1007/s00037-026-00286-x)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1103 — Containment of presentable border VP in VNP over every field

The target asks whether presentable border VP is contained in VNP over every field. A small approximation circuit must generate its parameter-dependent coefficients using counted arithmetic gates. Its degree in the original variables is polynomial, while the degree in the approximation parameter may be much larger. The required exact representation is a Boolean-cube sum of a polynomial-size, polynomial-degree verifier over the same field. Finite fields are covered by a known theorem; the universal extension requires a complete Lean-checked proof or counterexample.

[Read in atlas](index.html#TCS-1103) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/) · [Learning the coefficients: A presentable version of border complexity and applications to circuit factoring](https://www.cse.iitk.ac.in/users/nitin/papers/PresentableVNP.pdf)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-5260 — Explicit rigid matrices over low-degree number fields

The target is a deterministic polynomial-time construction of rigid complex square matrices with algebraic entries. All entries must lie in one common number field of polynomial degree, supplied by an exact polynomial-size representation. Reducing rank to any fixed multiple of n divided by log log n must require at least n^(1+epsilon) changed entries for one fixed positive epsilon. The low-rank replacement may use arbitrary complex values, so its coefficients are not confined to the original number field. The answer must include complete Lean-checked construction, representation and rigidity proofs or prove the exact negation.

[Read in atlas](index.html#TCS-5260) · [Fourier and Circulant Matrices Are Not Rigid](https://doi.org/10.4230/LIPIcs.CCC.2019.17) · [Complexity Lower Bounds using Linear Algebra](https://www.cs.toronto.edu/~toni/Courses/CommComplexity/Papers/lokam-book.pdf) · [Arithmetic circuit lower bounds from sumset expansion](https://arxiv.org/abs/2607.15848)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7372 — Linear-time unit-Monge distance multiplication

Two permutations implicitly encode simple unit-Monge counting matrices. Their exact min-plus product is again encoded by a unique permutation. The question asks for one deterministic algorithm taking only linear worst-case time and space. The checked sequential algorithms retain a logarithmic factor, while constant-round parallel results use a different model. A complete Lean-checked answer must prove or refute the linear-time proposition for every pair of input permutations.

[Read in atlas](index.html#TCS-7372) · [Fast Distance Multiplication of Unit-Monge Matrices](https://doi.org/10.1007/s00453-013-9830-z) · [Core-Sparse Monge Matrix Multiplication: Improved Algorithm and Applications](https://arxiv.org/abs/2408.04613v2) · [An Optimal MPC Algorithm for Subunit-Monge Matrix Multiplication, with Applications to LIS](https://arxiv.org/abs/2404.13486v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7224 — Polynomial-time computation of addition-chain length

An addition chain starts at one and repeatedly forms a new integer by adding two earlier entries. Its shortest length is the fewest such additions needed to reach a specified positive target. The target is given in binary, and the requested algorithm must output the exact optimum in time polynomial in that bit length. This is a question about computing the minimum count, without additionally requiring an optimal chain as output. Known short chains, restricted families, heuristics and hardness for multiple targets do not establish the requested general deterministic algorithm or its impossibility.

[Read in atlas](index.html#TCS-7224) · [Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/book/01-recursion.pdf) · [On Fast Calculation of Addition Chains for Isogeny-Based Cryptography](https://faculty.eng.fau.edu/azarderakhsh/files/2016/11/Inscrypt2016.pdf) · [Assembly theory and its relationship with computational complexity](https://doi.org/10.1038/s44260-025-00049-9) · [The Decompressed Tree Size of k-Ary Chains](https://doi.org/10.1007/s00026-026-00816-y)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3318 — Arithmetic circuit closure under pth roots

For each fixed prime p, the question compares the circuit sizes of g and its p-th power over the algebraic closure of the prime field. The desired size overhead is polynomial in the original size and number of variables, with no degree dependence. Circuits may share arbitrary intermediate computations and use arbitrary constants, but may not use root gates. The target is formal polynomial computation and existence of small circuits, not equality of finite-field functions or efficient reconstruction. A complete Lean-checked universal size bound or a counterexample to every such bound in some fixed characteristic is required.

[Read in atlas](index.html#TCS-3318) · [Algebraic Hardness Versus Randomness in Low Characteristic](https://doi.org/10.4230/LIPIcs.CCC.2020.37) · [Factorization of Polynomials Given by Arithmetic Branching Programs](https://image.informatik.htw-aalen.de/~thierauf/Papers/ABP-factors.pdf) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-5921 — Membership in \(2\times 2\) integer matrix semigroups

The input is a finite list of integer matrices of size two by two and a target matrix of the same size. The question asks whether any nonempty finite product of the listed matrices equals the target exactly. Generators may repeat and may include both singular and nonsingular matrices with arbitrary determinants. The desired algorithm must terminate on every input, without any prescribed running-time bound. A complete Lean-checked decision procedure or undecidability proof must cover the unrestricted input class.

[Read in atlas](index.html#TCS-5921) · [On Reachability Problems for Low-Dimensional Matrix Semigroups](https://doi.org/10.4230/LIPIcs.ICALP.2019.44) · [Decidability of Membership Problems for Flat Rational Subsets of GL(2, Q) and Singular Matrices](https://doi.org/10.1137/22M1512612)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1544 — A qAC⁰ versus NL-complete dichotomy for Cayley semigroup membership

The input gives a finite semigroup by its complete multiplication table, a generator set and a target element. The promise places the generated subsemigroup in one fixed pseudovariety, and the task is to test whether it contains the target. The question asks whether every such class has either uniform shallow quasipolynomial circuits or an NL-complete membership problem. Hardness uses uniform constant-depth polynomial-size reductions that preserve the input promise. The September 2026 source retains this dichotomy as open; a complete Lean-checked universal proof or counterexample is required.

[Read in atlas](index.html#TCS-1544) · [Efficient Compression in Semigroups](https://arxiv.org/abs/2601.04747v2) · [Efficient Compression in Semigroups](https://doi.org/10.4230/LIPIcs.STACS.2026.80) · [Membership and Conjugacy in Inverse Semigroups](https://doi.org/10.4230/LIPIcs.ICALP.2025.156)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-4523 — Polynomial-time dimension expansion over finite fields

Dimension expansion measures how much a collection of linear maps enlarges every subspace of dimension at most half the ambient dimension. This card asks for exact evaluation on arbitrary matrices over an explicitly represented finite field. The desired algorithm must use polynomial time in the complete input bit length, including the field representation. The output is the minimum ratio of image-span dimension to original dimension over all eligible nonzero subspaces. Explicit constructions and spectral expansion tests remain distinct from a general exact evaluator.

[Read in atlas](index.html#TCS-4523) · [Dimension Expanders via Rank Condensers](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.800) · [On Linear-Algebraic Notions of Expansion](https://doi.org/10.4086/toc.2025.v021a001)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0009 — Explicit univariate arithmetic circuit lower bounds

The question asks for a family of one-variable integer polynomials whose smallest arithmetic circuits cannot all be bounded by a constant times the logarithm of their degree. Each polynomial must have polynomially many bits per coefficient, with any requested coefficient bit and sign computable by one uniform algorithm in time polynomial in the logarithm of the degree. The competing circuits may share intermediate computations and use arbitrary complex constants for free, while every wire into a binary addition or multiplication gate contributes to their size. This explicitness requirement is a disclosed specialization of the original question, whose wording did not fix a coefficient-generation model. A resolution would clarify how far efficiently specified coefficients can force arithmetic complexity beyond the elementary degree bound in a single variable.

[Read in atlas](index.html#TCS-0009) · [Mathematics and Computation (27 March 2018 draft)](https://www.math.ias.edu/files/mathandcomp.pdf) · [A Largish Sum-Of-Squares Implies Circuit Hardness and Derandomization](https://doi.org/10.4230/LIPIcs.ITCS.2021.23) · [Partial Derivatives in Arithmetic Complexity and Beyond](https://doi.org/10.1561/0400000043) · [Weighted Sum-of-Squares Lower Bounds for Univariate Polynomials Imply \(\mathrm{VP}\ne\mathrm{VNP}\)](https://doi.org/10.1007/s00037-024-00249-0) · [Polynomial Lower Bounds for Arithmetic Circuits over Non-Commutative Rings](https://eccc.weizmann.ac.il/report/2026/061/) · [Arithmetic circuit lower bounds from sumset expansion](https://arxiv.org/abs/2607.15848v1)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-1151 — Bounded-interval zero testing for exponential-trigonometric polynomials

The input specifies a linear differential equation with constant coefficients, initial values and a nonnegative rational endpoint. The task is to decide exactly whether its real solution has any zero in the closed bounded interval. The question ranges over every fixed computable real subfield with effective arithmetic, equality and rational approximation. A decider may depend on the field but must handle every equation order, including endpoint zeros and zeros without sign changes. A complete Lean-checked unconditional decidability proof or a field-specific undecidability counterexample is required.

[Read in atlas](index.html#TCS-1151) · [On Positivity of Exponential-Trigonometric Polynomials and Irrationality Exponents](https://doi.org/10.4230/LIPIcs.MFCS.2026.65) · [On the Zeros of Exponential Polynomials](https://doi.org/10.1145/3603543)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0046 — Polynomial-time feasibility of integer min-plus linear systems

Each input row equates two minima of integer coefficients plus unknown integer coordinates. The question asks whether a single deterministic algorithm can decide feasibility in polynomial time. Time is measured in the full binary input length, with both matrix dimensions allowed to grow. The problem is polynomial-time equivalent to mean-payoff games, while known pseudopolynomial bounds depend on coefficient magnitudes. An answer must include a complete Lean-checked polynomial-bit-time decider or a proof that none exists.

[Read in atlas](index.html#TCS-0046) · [Complexity of Symbolic and Numerical Problems: Complexity of solving tropical or min-plus linear systems](https://doi.org/10.4230/DagRep.5.6.28) · [Complexity of tropical and min-plus linear prevarieties](https://arxiv.org/abs/1204.4578) · [Set-defined graph classes: χ-boundedness meets tropical algebra](https://arxiv.org/abs/2607.23754)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1101 — VP factor closure in positive characteristic

VP consists of polynomial families whose variable count, output degree and algebraic circuit size are polynomially bounded. The question asks whether every factor family of a nonzero VP family also belongs to VP over each fixed field of positive characteristic. Circuits are nonuniform, may use arbitrary constants from that same field, and must compute the formal polynomials exactly. The target includes arbitrary factor multiplicities, whereas several known small-characteristic results compute only powers of factors or place the factors in a larger complexity class. A complete Lean proof must establish this universal closure or exhibit a fixed-field factor family without any polynomial circuit-size bound.

[Read in atlas](index.html#TCS-1101) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/) · [Algebraic Hardness versus Randomness in Low Characteristic](https://arxiv.org/abs/2005.10885v1) · [Learning the coefficients: A presentable version of border complexity and applications to circuit factoring](https://www.cse.iitk.ac.in/users/nitin/papers/PresentableVNP.pdf) · [Closure under factorization from a result of Furstenberg](https://eccc.weizmann.ac.il/report/2025/084/) · [Constant-depth circuits for polynomial GCD over any characteristic](https://eccc.weizmann.ac.il/report/2025/085/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1102 — VBP factor closure in positive characteristic

The question asks whether taking any factor preserves polynomial-size commutative arithmetic branching programs in every fixed field of positive characteristic. A branching program sums products of affine edge labels along its source-to-sink paths. The factor must have a small program over the original field, including when its multiplicity is divisible by the characteristic. This is a nonuniform existence question and does not require an efficient factorization algorithm. A complete Lean-checked polynomial size bound or a counterexample field and superpolynomial factor-size separation is required.

[Read in atlas](index.html#TCS-1102) · [A primer on the closure of algebraic complexity classes under factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/) · [Factorization of Polynomials Given by Arithmetic Branching Programs](https://image.informatik.htw-aalen.de/~thierauf/Papers/ABP-factors.pdf) · [Algebraic Hardness Versus Randomness in Low Characteristic](https://doi.org/10.4230/LIPIcs.CCC.2020.37)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-4490 — Polynomial-time sign testing of matrix powers in every fixed dimension

The input specifies an integer matrix, an integer linear functional and a nonnegative binary exponent. The task is to decide whether applying the functional to that matrix power gives a nonnegative integer. The question asks for deterministic polynomial bit time separately in every fixed matrix dimension. The polynomial bound may depend on the dimension, while all matrix and functional entries remain part of the binary input. A complete Lean-checked affirmative algorithmic proof or a fixed-dimensional impossibility proof is required.

[Read in atlas](index.html#TCS-4490) · [On Matrix Powering in Low Dimensions](https://doi.org/10.4230/LIPIcs.STACS.2015.329) · [Counting Problems for Parikh Images](https://doi.org/10.4230/LIPIcs.MFCS.2017.12)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0047 — Exact Kronecker-polytope membership in polynomial time

The input consists of three integer partitions of the same size, written as binary lists whose length may grow. The task is to decide exact membership of their normalized triple in the Kronecker polytope. Equivalently, the three lists must occur as spectra of the reduced matrices of some unit complex three-dimensional array. The desired algorithm is deterministic and polynomial in the full bit length, including arbitrarily close boundary cases. A complete Lean-checked complexity proof must go beyond known certificates and algorithms whose time depends polynomially on inverse approximation error.

[Read in atlas](index.html#TCS-0047) · [Complexity of Symbolic and Numerical Problems: Complexity of testing membership to Kronecker polytopes](https://doi.org/10.4230/DagRep.5.6.28) · [Membership in moment polytopes is in NP and coNP](https://arxiv.org/abs/1511.03675) · [Computing moment polytopes — with a focus on tensors, entanglement and matrix multiplication](https://arxiv.org/abs/2510.08336)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0095 — Efficient LRS evaluation

The input gives a rational linear recurrence, its initial values and an index written in binary. The target is one deterministic algorithm that decides whether exactly that indexed term is zero. Its running time must be polynomial in the combined input bit length, including the recurrence order and coefficient descriptions. Randomized testing of a compact arithmetic representation is known, while printing the full term may take exponentially many bits. An answer must provide a complete Lean-checked uniform algorithm and time analysis or prove that no such algorithm exists.

[Read in atlas](index.html#TCS-0095) · [25.4 Efficient LRS evaluation](https://automata.exchange/25.4-efficient-lrs-evaluation/) · [On the Complexity of the Skolem Problem at Low Orders](https://people.mpi-sws.org/~joel/publications/skolem-complexity25.pdf)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1069 — Does real Zariski-closure membership belong to ∃R?

The input describes a real semialgebraic set by a Boolean formula of explicitly written integer polynomial constraints. Its real Zariski closure consists of the points satisfying every real polynomial relation that vanishes on the set. The question asks whether testing that the origin lies in this closure belongs to the existential theory of the reals complexity class. A positive answer needs one polynomial-bit-time transformation to an equivalent existential real sentence for all input dimensions and degrees. The source leaves Zariski adherence open, and the known Euclidean result does not settle this target; a complete Lean-checked answer is required.

[Read in atlas](index.html#TCS-1069) · [The Existential Theory of the Reals as a Complexity Class: A Compendium](https://arxiv.org/abs/2407.18006v1) · [Exotic quantifiers, complexity classes, and complete problems](https://eccc.weizmann.ac.il/report/2005/138/)
Existing status: `source_open` · Summary written: 2026-09-17

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

### TCS-4350 — Uniform compressed word problem for graph groups

The input gives both a graph group and a compact straight-line program representing a word in its generators. The main question is whether one deterministic algorithm can test identity in polynomial time in the combined input size. Polynomial time for each fixed graph group does not provide that uniform guarantee. Randomized one-sided polynomial-time testing is known, while NP membership is a separate weaker target. A 2024 result handles uniform power words but explicitly leaves arbitrary straight-line programs open.

[Read in atlas](index.html#TCS-4350) · [Knapsack in Graph Groups, HNN-Extensions and Amalgamated Products](https://doi.org/10.4230/LIPIcs.STACS.2016.50) · [Knapsack in Graph Groups](https://doi.org/10.1007/s00224-017-9808-3) · [The Power Word Problem in Graph Products](https://doi.org/10.1007/s00224-024-10173-z)
Existing status: `open` · Summary written: 2026-09-12

### TCS-5739 — Collapse of rational recurrence systems to single recurrences

A rationally recursive sequence is one coordinate of a finite system whose next state is a rational function of its current state. The conjecture asks whether finitely many past values of that coordinate always suffice to generate its next value. All coefficients and initial values are rational, and every denominator must remain nonzero along the sequence. A scalar recurrence may depend on the particular initial vector, but must work at every step. The known theorem with symbolic initial values does not settle the numerical case because specialization can make its denominators vanish.

[Read in atlas](index.html#TCS-5739) · [On Rational Recursive Sequences](https://doi.org/10.4230/LIPIcs.STACS.2023.24) · [On Rational Recursive Sequences — full author version](https://arxiv.org/abs/2210.01635)
Existing status: `open` · Summary written: 2026-09-12

## Lattices and computational number theory (27)

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

An input basis generates a lattice by taking all integer combinations of its rational columns. The algorithm must output coordinates of an exactly shortest nonzero Euclidean lattice vector, with success probability at least two thirds. One uniform algorithm must use single-exponential time in the lattice rank and polynomial working space in the full input length simultaneously. Both resource bounds include preprocessing, arithmetic precision and unsuccessful random executions. A complete Lean-checked proof must establish those guarantees or their impossibility; exponential storage, approximation and heuristic memory savings do not meet the target.

[Read in atlas](index.html#TCS-6619) · [A Deterministic Single Exponential Time Algorithm for Most Lattice Problems based on Voronoi Cell Computations](https://eccc.weizmann.ac.il/report/2010/014/revision/1/) · [Shortest Vector Problem (SVP) — Lattice Links](https://cseweb.ucsd.edu/~daniele/LatticeLinks/SVP.html) · [Lattice Enumeration Algorithms](https://cseweb.ucsd.edu/~daniele/LatticeLinks/Enum.html) · [A Sheaf-Theoretic and Etalé Space Approach to the Shortest Vector Problem: Orthogonalization, Coboundary Maps, and Memory-Efficient Sieving](https://pphmjopenaccess.com/jpjgt/article/download/3968/1901/11504) · [Hardness of hinted ISIS from the space-time hardness of lattice problems](https://eprint.iacr.org/2026/187)
Existing status: `source_open` · Summary written: 2026-09-17

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

### TCS-6861 — A classical same-dimension reduction from SIVP to polynomial-modulus LWE

LWE hides a uniformly random modular vector behind noisy linear equations. The card asks for a classical reduction from worst-case short independent lattice vectors to polynomial-modulus LWE in the same dimension. The target approximation factor is n/α times a fixed power of a logarithm, with precise rounded Gaussian errors. Known quantum reductions achieve the relevant connection, while the reviewed classical route loses dimension and starts from a different lattice problem. A complete Lean-checked answer must settle the explicitly quantified reduction and its average-case oracle guarantees.

[Read in atlas](index.html#TCS-6861) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939) · [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) · [Classical Hardness of Learning with Errors](https://arxiv.org/abs/1306.0281v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6863 — Polynomial-factor approximation of cyclotomic ideal SVP

An ideal in a power-of-two cyclotomic ring is a full integer lattice closed under multiplication by the ring. The selected question asks for a classical randomized polynomial-time algorithm returning an actual nonzero vector within a fixed polynomial factor of the shortest length. One program and fixed exponents must work for every dimension and every explicitly supplied ideal basis, with all preprocessing and output charged. This is an expressly labeled specialization of Peikert’s broad question about algorithmic advantages of ideal-lattice structure. Conditional quantum algorithms, easy prime-ideal classes and the new exact-hardness claims in other rings do not determine this all-ideals target.

[Read in atlas](index.html#TCS-6863) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939) · [Mildly Short Vectors in Cyclotomic Ideal Lattices in Quantum Polynomial Time](https://ir.cwi.nl/pub/30736/) · [On the ideal shortest vector problem over random rational primes](https://par.nsf.gov/servlets/purl/10322409) · [Some Easy Instances of Ideal-SVP and Implications on the Partial Vandermonde Knapsack Problem](https://eprint.iacr.org/2022/709) · [Principal ideal problem and ideal shortest vector over rational primes in power-of-two cyclotomic fields](https://arxiv.org/abs/2601.07511) · [NP-hardness of ideal lattice problems](https://arxiv.org/abs/2609.15813) · [Euclidean SVP is NP-hard for Cyclic Lattices](https://arxiv.org/abs/2609.16711)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7265 — Deterministic polynomial-time construction of a prime of a given bit length

Given a requested bit length in unary, the task is to output the ordinary binary expansion of a prime with exactly that many bits. The question asks whether one fixed deterministic algorithm can do this for every length at least two in polynomial bit time. Primality testing is efficiently possible, while deterministic construction of a suitable candidate remains a central explicit-construction problem. Polynomial-time pseudodeterministic generation is known for infinitely many lengths, but that algorithm still uses randomness and does not meet the all-length deterministic requirement. A complete Lean answer must prove the existence of the required algorithm or prove that every deterministic program and polynomial bound fail at some requested length.

[Read in atlas](index.html#TCS-7265) · [Theory and Applications of Probabilistic Kolmogorov Complexity](https://eccc.weizmann.ac.il/report/2022/081/) · [On Pseudodeterministic Approximation Algorithms](https://doi.org/10.4230/LIPIcs.MFCS.2018.61) · [Polynomial-Time Pseudodeterministic Construction of Primes](https://doi.org/10.1145/3803408)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0659 — A classical SIS reduction from sublinear-factor GapSVP

A random SIS instance is a matrix modulo a polynomial-size integer, and the goal is a short nonzero integer vector in its modular kernel. The question asks for a classical reduction from every Euclidean GapSVP instance with approximation factor O(n^(1−ε)) for some fixed ε > 0. The chosen matrix dimensions ensure that a solution exists while excluding the trivial modulus-sized vector. The reduction must work even when its SIS oracle succeeds only on an inverse-polynomial fraction of uniformly random matrices. Polynomial overhead includes the inverse success probability, and a complete Lean-checked reduction or impossibility proof is required.

[Read in atlas](index.html#TCS-0659) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-5317 — NP-hardness of Euclidean covering radius

A lattice covering radius is the largest distance from a point in its span to the nearest lattice point. The input here is a rational basis and a positive rational threshold in the Euclidean norm. The exact decision problem accepts precisely when the covering radius is at most the threshold. The question asks whether satisfiability reduces to this decision problem by one deterministic polynomial-time map. A September 2026 paper proves hardness for sufficiently large norms while explicitly leaving the Euclidean case open.

[Read in atlas](index.html#TCS-5317) · [Hardness of the Binary Covering Radius Problem in Large \(\ell_p\) Norms](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.10)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6864 — Classical ideal-SVP hardness of ring-LWE in power-of-two cyclotomic rings

Ring-LWE consists of noisy multiplication samples in a finite polynomial quotient ring. The card asks for a classical reduction from finding a short vector in every ideal of a power-of-two cyclotomic ring. The target keeps the degree and polynomial modulus and seeks the known quantum approximation scale Õ(√n/α). Its oracle must solve the full bounded elliptical error family, with explicit dual-ring scaling and finite coefficient rounding. The classical connection remains unresolved in the checked sources, and a full Lean-checked reduction or refutation is required.

[Read in atlas](index.html#TCS-6864) · [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939) · [On Ideal Lattices and Learning with Errors Over Rings](https://cims.nyu.edu/~regev/papers/ideal-lwe.pdf) · [Classical Hardness of Learning with Errors](https://arxiv.org/abs/1306.0281v1) · [NP-hardness of ideal lattice problems](https://arxiv.org/abs/2609.15813v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0656 — A classical reduction from semiprime factoring to polynomial-gap SVP

The input is an integer promised to be the product of two distinct primes. The goal is to recover its factors with a classical randomized algorithm taking polynomial time in the integer’s bit length. The algorithm may query Euclidean GapSVP at approximation factor n^(2+ε), for some fixed ε > 0 and query rank n. It must succeed on every promised semiprime regardless of how the oracle answers inside its approximation gap. This would connect factoring to a lattice regime relevant for classical cryptographic reductions; a complete Lean-checked proof or refutation is required.

[Read in atlas](index.html#TCS-0656) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7171 — Baillie–PSW pseudoprimes

The Baillie–PSW combination checks a prime-like modular power pattern and a prime-like Lucas sequence pattern. The question asks whether any composite integer passes both strong tests with the specified Selfridge parameters. All recurrences, congruences and parameter-search rejection rules are fixed in the statement. Exhaustive verification through a large finite range and later experiments have produced no counterexample in the checked sources. A single rigorously verified composite would answer yes, while answering no requires a proof covering integers of every size.

[Read in atlas](index.html#TCS-7171) · [Strengthening the Baillie-PSW Primality Test](https://doi.org/10.1090/mcom/3616) · [U-Bit Collapse in Arnault Composites: Probing the Boundary of Strong Lucas Pseudoprimes](https://arxiv.org/abs/2601.19817v1)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-7170 — Scholz–Brauer conjecture

An addition chain starts at one and builds its target by repeatedly adding two already available values. Its length counts additions and corresponds to the number of multiplications in the associated repeated-power computation. The conjecture asks whether the minimum length for \(2^{n}- 1\) is always at most \(n- 1\) plus the minimum length for n. The analogous theorem for star chains and known infinite families leave the unrestricted universal inequality open in the checked sources. Resolving it would explain how efficiently optimal exponentiation plans can control the cost of all-ones binary exponents.

[Read in atlas](index.html#TCS-7170) · [The Decompressed Tree Size of k-Ary Chains](https://link.springer.com/article/10.1007/s00026-026-00816-y) · [The Scholz Conjecture on Addition Chains Is True for Infinitely Many Integers with \(\ell\)\((2n)=\ell (n)\)](https://math.colgate.edu/~integers/a17Proc23/a17Proc23.pdf) · [The Scholz Conjecture Is True for \(2^{n}- 1\) for Almost All n](https://vixra.org/pdf/2605.0012v1.pdf)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0655 — Polynomial-factor Euclidean SVP hardness assuming NP is not contained in RP

Euclidean GapSVP distinguishes lattices with a short nonzero vector from lattices whose shortest vector is longer by a promised approximation factor. The question asks whether NP ⊄ RP rules out a randomized polynomial-time algorithm for some fixed factor n^ε. The exponent is positive and independent of the input, and running time counts the complete binary representation. A 2026 theorem proves polynomial-factor hardness for p > 2, but it does not cover this Euclidean target. The card retains that precise open specialization and requires a complete Lean-checked implication or refutation.

[Read in atlas](index.html#TCS-0655) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Deterministic Hardness of Approximation For SVP in all Finite ℓ_p Norms](https://arxiv.org/abs/2604.01451v2) · [Euclidean SVP is deterministically NP-hard to approximate within any constant factor](https://arxiv.org/abs/2608.12664v2) · [Polynomial-Factor Deterministic NP-Hardness for SVP in Every ℓ_p Norm with p > 2](https://arxiv.org/abs/2608.14529v3)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-5395 — Downward self-reducibility of integer factoring

Factoring is a central arithmetic search problem whose complete output is a unique prime-power decomposition. The question asks whether one can factor an n-bit number in polynomial time given oracle answers only on shorter numbers. All queries must have fewer than n bits, not merely a smaller numerical value. The reducer is deterministic and uniform, with polynomially many ordinary computation steps. A positive answer would place factoring in a more structured total-search class and reveal a basic recursive property of the problem.

[Read in atlas](index.html#TCS-5395) · [Downward Self-Reducibility in TFNP](https://doi.org/10.4230/LIPIcs.ITCS.2023.67)
Existing status: `source_open` · Summary written: 2026-09-12

### TCS-0652 — Dimension-preserving search-to-decision reductions for SVP

The input is a rational lattice basis, and the search task is to produce a nonzero vector whose length approximates the shortest possible length. The available oracle only distinguishes short-vector lengths across a multiplicative gap. The question asks for a classical polynomial-time reduction that keeps every query in the original dimension and loses only a polynomial in dimension and approximation factor. Known exact and near-exact reductions do not supply this guarantee across the full approximation range. A resolution would clarify whether approximate lattice decision algorithms can be converted efficiently into search algorithms without an exponential dimensional penalty.

[Read in atlas](index.html#TCS-0652) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Search-to-Decision Reductions for Lattice Problems with Approximation Factors (Slightly) Greater Than One](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.19) · [Dimension-Preserving Reductions Between Lattice Problems](https://www.noahsd.com/latticeproblems.pdf) · [Open problems from the Summer 2022 Lattices Program](https://wiki.simons.berkeley.edu/doku.php?id=lat22:start)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0648 — NP-hardness of Euclidean unique SVP with a fixed gap greater than one

The input is an explicit integer lattice basis in Euclidean space. It promises that every independent direction is longer than a shortest vector by one fixed factor greater than one. The task is to recover an exact shortest vector, with either sign allowed. The question asks whether this promise search problem is NP-hard under classical randomized polynomial-time oracle reductions. Shrinking uniqueness gaps and hardness in other norms do not establish this target, whose full proof or refutation must be Lean-checked.

[Read in atlas](index.html#TCS-0648) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Improved hardness results for unique shortest vector problem](https://doi.org/10.1016/j.ipl.2016.05.003) · [Just how hard are rotations of Zⁿ? Algorithms and cryptography with the simplest lattice](https://eprint.iacr.org/2021/1548) · [Deterministic Hardness of Approximation of Unique-SVP and GapSVP in ℓ_p norms for p>2](https://arxiv.org/abs/2510.16991v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0661 — SVP hardness for fixed-rank cyclotomic modules

Cyclotomic module lattices combine integer lattice geometry with multiplication by an algebraic number ring. The question asks whether exact Euclidean shortest-vector decision is NP-hard at some fixed module rank while the conductor and field degree grow. The card specifies the canonical product norm, integral generators and a uniform deterministic polynomial-time many-one reduction. A September 2026 preprint claims this hardness already for rank two over a prime-conductor subfamily, matching the selected formulation. The complete new proof is independently unverified here, and its claim does not imply hardness for every ring family or cryptographic distribution.

[Read in atlas](index.html#TCS-0661) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [SVP Is NP-Hard for Some Rank-2 Cyclotomic Modules](https://arxiv.org/abs/2609.01469) · [On Module Unique-SVP and NTRU](https://eprint.iacr.org/2022/1203) · [Average hardness of SIVP for module lattices of fixed rank](https://arxiv.org/abs/2511.13659) · [Mildly Short Vectors in Cyclotomic Ideal Lattices in Quantum Polynomial Time](https://ir.cwi.nl/pub/30736/)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0662 — Unconditional exponential hardness of \(n^{1+\varepsilon}\)-GapSVP

The input is a rational basis for an n-dimensional lattice and a positive radius. The task distinguishes a nonzero vector within that radius from the promise that every nonzero vector is farther away by a factor \(n^{1+\varepsilon}\). The source asks for explicit \(c,\varepsilon >0\) and an unconditional lower bound excluding \(2^{cn}\)-time algorithms, up to polynomial input-processing factors. The bound must also exclude randomized and quantum computation with bounded error. Such a theorem would establish a powerful worst-case hardness foundation for lattice-based cryptography.

[Read in atlas](index.html#TCS-0662) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Lattice Problems Beyond Polynomial Time](https://arxiv.org/abs/2211.11693)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-0657 — coNP certificates for GapSVP at the square-root n/log n scale

GapSVP asks whether an input lattice has a vector of length at most a threshold or all nonzero vectors are longer by a promised factor. This card asks for short classical certificates of the second alternative at factor C√(n/log n). One deterministic verifier must check the certificates in polynomial time in the complete binary input length. Known certificates work at the larger scale C√n, while the smaller scale is known for an interactive randomized proof. The requested improvement and all promise guarantees require a complete Lean-checked proof or refutation.

[Read in atlas](index.html#TCS-0657) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [Lattice Problems in NP ∩ coNP](https://cims.nyu.edu/~regev/papers/cvpconp.pdf)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0653 — A quantum 2^(0.2075n) lower bound for exact Euclidean SVP from QSETH

Exact Euclidean SVP asks for a shortest nonzero vector of an explicitly given integer lattice. This card asks whether quantum SETH rules out time 2^(0.2075n) times a polynomial in the binary input length. The quantum SAT hypothesis uses the search baseline 2^(N/2), and both sides use the same uniform finite-gate model. Known barriers obstruct important families of reductions without resolving the full implication. A complete Lean-checked proof or refutation must establish the stated numerical exponent and computational guarantees.

[Read in atlas](index.html#TCS-0653) · [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) · [On the (Classical and Quantum) Fine-Grained Complexity of Approximate CVP and Max-Cut](https://doi.org/10.4230/LIPIcs.ICALP.2026.111)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-1170 — ETH hardness of constant-factor shortest-vector approximation for \(1\le p\le 2\)

The shortest-vector problem asks how short a nonzero lattice vector can be. This card asks for constant-factor gap hardness in every norm \(\ell p\) with \(1\le p\le 2\). The proposed lower bound excludes subexponential dependence on ambient dimension, with polynomial dependence on input encoding length. Its premise is ordinary deterministic ETH, and the approximation factor must stay bounded away from one as dimension grows. The source’s shortest-vector hardness theorem for \(p>2\) uses randomized ETH and does not settle this stated interval or premise.

[Read in atlas](index.html#TCS-1170) · [Mind the Gap? Not for SVP Hardness Under ETH!](https://doi.org/10.4230/LIPIcs.ICALP.2026.8)
Existing status: `source_open` · Summary written: 2026-09-11

## Coding and information theory (27)

### TCS-6606 — Capacity of the two-user Gaussian interference channel

Two separately informed transmitters communicate through real Gaussian noise while interfering with each other’s receivers. The target is the weighted support function of the capacity region for every real gain, nonnegative power budget and weight between zero and one. The model permits deterministic time sharing and averages each transmitter’s power over messages and time, with vanishing joint average decoding error. Known special cases and approximation results leave the general tradeoff unresolved in the checked sources, while a September 2026 weak-interference capacity claim remains unverified here. A complete Lean proof must certify one function within absolute error 1/100 bit per real channel use throughout the entire domain.

[Read in atlas](index.html#TCS-6606) · [Two-User Gaussian Interference Channels: An Information Theoretic Point of View](https://doi.org/10.1561/0100000071) · [Gaussian Interference Channel Capacity to Within One Bit](https://arxiv.org/abs/cs/0702045v2) · [Invariance of the Han–Kobayashi Region With Respect to Temporally-Correlated Gaussian Inputs](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/temp-corr.pdf) · [Proof of a conjecture on the Gaussian signaling region for the Gaussian Z-interference channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/GZ-Noi-con.pdf) · [On the Local Optimality of Gaussian distributions for the Han-Kobayashi Inner Bound for the Gaussian Z-interference channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/Gau-Her.pdf) · [A New Outer Bound for the Discrete Memoryless Two-User Interference Channel](https://chandra.ie.cuhk.edu.hk/pub/papers/IC/INT-OB-ITA-26.pdf) · [On the Optimality of Gaussian Code-books for Signaling over a Two-Users Weak Gaussian Interference Channel](https://arxiv.org/abs/2501.14941v12) · [Codewords With Memory Improve Achievable Rate Regions of the Memoryless Gaussian Interference Channel](https://arxiv.org/abs/1508.05726v2)
Existing status: `uncertain` · Summary written: 2026-09-14

### TCS-1010 — Optimal asymptotic binary rate–distance tradeoff

A binary code is any nonempty set of equal-length bit strings with a prescribed minimum pairwise Hamming distance. The function \(R_2(\delta)\) is the limsup of the maximum information rate at relative distance \(\delta\), allowing nonlinear codes and arbitrary subsequences of block lengths. Determine this function at every real distance strictly between zero and one half, with absolute error at most 0.01 information bits per transmitted bit. A complete Lean proof must establish both lower and upper guarantees throughout the domain, without any code-construction or evaluation-time bound. The checked 2026 papers improve the upper bounds but do not supply this certified whole-curve approximation; polynomial code-size improvements also leave the leading rate unchanged.

[Read in atlas](index.html#TCS-1010) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/) · [New upper bounds on the rate of a code via the Delsarte–MacWilliams inequalities](https://doi.org/10.1109/TIT.1977.1055688) · [Asymptotic Improvement of the Gilbert–Varshamov Bound on the Size of Binary Codes](https://arxiv.org/abs/math/0404325) · [Improvement of the Gilbert-Varshamov Bound for Linear Codes and Quantum Codes](https://arxiv.org/abs/2601.18590) · [Binary code rate bounds via classical–quantum channels](https://arxiv.org/abs/2608.09347) · [Comments on the recent improvements of the MRRW bounds](https://arxiv.org/abs/2609.01860)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6665 — Capacity of the general broadcast channel

One transmitter sends two independent private messages through a memoryless channel to receivers with different noisy observations. The target is the weighted support function of the average-error capacity region for every finite rational channel table and rational weight between zero and one. All rates are measured in bits per channel use, and the two individual capacities do not determine the joint tradeoff. Classical and recent work provides achievable regions, converse bounds and special cases, while the August 2026 Marton-suboptimality preprint is a narrower unverified claim. A complete Lean proof must certify a supplied function within absolute error 1/100 over the entire stated domain.

[Read in atlas](index.html#TCS-6665) · [A Coding Theorem for the Discrete Memoryless Broadcast Channel](https://www.seas.ucla.edu/csl/files/temp/DBCAchievability.pdf) · [Evaluation of Marton’s Inner Bound for the General Broadcast Channel](https://arxiv.org/abs/0904.4541v3) · [On Marton’s Inner Bound and Its Optimality for Classes of Product Broadcast Channels](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/proBC.pdf) · [Blahut–Arimoto Algorithms for Inner and Outer Bounds on Capacity Regions of Broadcast Channels](https://pmc.ncbi.nlm.nih.gov/articles/PMC10969477/) · [A Two Auxiliary Receiver Outer Bound to the Capacity Region of a Two-Receiver Discrete Memoryless Broadcast Channel](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/GK-outer.pdf) · [Sub-optimality of Marton’s Inner Bound for the Two-Receiver Broadcast Channel](https://arxiv.org/abs/2608.19869v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6584 — Li–Li conjecture

An undirected network carries independent messages, each from one source to one destination, with a common capacity budget for both directions of every edge. The Li–Li conjecture asks whether arbitrary causal zero-error network coding has exactly the same closed rate region as optimal fractional multicommodity routing. The card fixes independent finite uniform messages, deterministic encoding, exact decoding and the sum of the two whole-transcript entropies on each edge. A complete Lean proof must establish the universal equality or certify a finite coding instance whose supported rate is outside the fractional routing region. Recent restricted topology results and a corrected session-interaction framework leave the general question open, while undirected multicast separations rely on shared messages with multiple receivers.

[Read in atlas](index.html#TCS-6584) · [On the Capacity of Multiple Unicast Sessions in Undirected Graphs](https://ics.uci.edu/~vazirani/isit.pdf) · [Coding in Undirected Graphs Is Either Very Helpful or Not Helpful at All](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.18) · [Lower Bounds for Multiplication via Network Coding](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.10) · [On the Capacity of Undirected Multiple Unicast Layered Networks with Asymmetric Demands](https://ieeexplore.ieee.org/document/11195643/) · [Undirected Multicast Network Coding Gaps via Locally Decodable Codes](https://arxiv.org/abs/2510.18737) · [On the Multiple-Unicast Conjecture: Beyond Cut Metrics](https://arxiv.org/abs/2608.06070) · [A Session Interaction Framework for The Multiple-Unicast Conjecture](https://arxiv.org/abs/2608.06042)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6607 — Capacity of the binary deletion channel

The binary deletion channel independently removes input bits while hiding their original positions. Its operational capacity is the supremum of reliable transmission rates in bits per input bit for each fixed deletion probability. This benchmark asks for a function within absolute error 0.01 throughout the entire real interval from zero to one, with a complete Lean proof. The user deliberately retains a formalization task because a known uniform finite-block estimate already guarantees unrestricted approximation at that accuracy. The exact curve remains a separate scientific open problem, and recent claimed numerical and high-deletion bounds do not determine it.

[Read in atlas](index.html#TCS-6607) · [An Overview of Capacity Results for Synchronization Channels](https://arxiv.org/abs/1910.07199) · [A new bound on the capacity of the binary deletion channel with high deletion probabilities](https://marco-dalai.unibs.it/pub/D_ISIT_2011.pdf) · [Optimal Coding for the Binary Deletion Channel With Small Deletion Probability](https://ykanoria.github.io/Deletion_paper.pdf) · [Improved Upper and Lower Bounds on the Capacity of the Binary Deletion Channel](https://arxiv.org/abs/2305.07156) · [Improved Capacity Upper Bounds for the Deletion Channel using a Parallelized Blahut-Arimoto Algorithm](https://arxiv.org/abs/2604.05867) · [A Certified Multi-Run Capacity Lower Bound for the Binary Deletion Channel at \(d = 1/2\)](https://zenodo.org/records/21780666) · [A New Upper Bound on the Binary Deletion Channel Capacity](https://arxiv.org/abs/2609.13351) · [Binary deletion channel quarter-bound formalization and verification records](https://github.com/factoreminv/bdc)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7267 — Binary codes beyond the Gilbert–Varshamov bound

Binary error-correcting codes store information in words whose pairwise Hamming distances are large. The Gilbert–Varshamov bound guarantees a familiar asymptotic rate at each fixed relative distance. This question asks whether some fixed distance permits a fixed positive rate improvement for unbounded block lengths. Codes may be nonlinear and need not have an efficient construction or decoding algorithm. Known finite-length gains and recent explicit-construction or upper-bound papers do not settle that constant-gap existence question.

[Read in atlas](index.html#TCS-7267) · [Essential Coding Theory (draft of 26 August 2025)](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/web-coding-book.pdf) · [Asymptotic Improvement of the Gilbert–Varshamov Bound on the Size of Binary Codes](https://arxiv.org/abs/math/0404325) · [Higher-Order Delsarte Dual LPs: Lifting, Constructions and Completeness](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.44) · [Tracing AG Codes: Toward Meeting the Gilbert–Varshamov Bound](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.68) · [An Elementary Proof of the First LP Bound on the Rate of Binary Codes](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.48) · [Wide Replacement Products Meet Gray Codes: Toward Optimal Small-Bias Sets](https://eccc.weizmann.ac.il/report/2025/179/) · [Logarithmically larger deletion codes of all distances](https://arxiv.org/abs/2209.11882)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6608 — Decidability of unconditional entropy inequalities

The input is one rational linear inequality involving the Shannon entropies of subsets of variables. It must be tested against every joint distribution on arbitrary finite alphabets, with no conditional premises. The question asks whether one algorithm can always halt and decide exact validity, including equality cases. Decidability for restricted inequalities and undecidability for conditional statements concern different problems. A complete Lean-checked answer must provide a total decision procedure or prove undecidability of this precise input language.

[Read in atlas](index.html#TCS-6608) · [Information Inequality Problem over Set Functions](https://doi.org/10.4230/LIPIcs.ICDT.2024.19) · [Decision Problems in Information Theory](https://doi.org/10.4230/LIPIcs.ICALP.2020.106) · [Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication](https://arxiv.org/abs/2205.11461v3) · [Exploring the entropic region](https://arxiv.org/abs/2509.12439v2) · [Information Inequalities for Five Random Variables](https://arxiv.org/abs/2512.23316v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7210 — Capacity of the general two-user interference channel

Two independent senders communicate with their own receivers through one interfering channel. Each sender knows only its own message and receives no feedback. The capacity region contains the asymptotically reliable pairs of rates under average block error. Its weighted upper support values describe the entire tradeoff in bits per joint channel use. The benchmark asks for these values on every finite channel with a Lean-certified absolute error at most 0.01.

[Read in atlas](index.html#TCS-7210) · [A New Achievable Rate Region for the Interference Channel](https://doi.org/10.1109/TIT.1981.1056307) · [Wikipedia: List of unsolved problems in information theory](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_information_theory) · [Wikipedia revision used for discovery](https://en.wikipedia.org/w/index.php?oldid=1351195847) · [Lecture Notes on Network Information Theory](https://arxiv.org/abs/1001.3404v4)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-4524 — Positive-rate binary codes against adversarial deletions

A binary deletion code must identify every transmitted word after an adversary removes an allowed fraction of its bits without revealing their positions. Positive rate means that codebook size grows exponentially along infinitely many block lengths with one fixed positive exponent. The target is the supremum deletion fraction for which such zero-error uniquely decodable code families exist, with no efficiency requirement. The checked bounds run from the square root of two minus one to one half minus ten to the minus fortieth power, and are too far apart to supply the required approximation. An accepted answer must determine this real threshold within 1/100 and prove the accuracy in Lean, without requiring that the supremum be attained.

[Read in atlas](index.html#TCS-4524) · [Deletion Codes in the High-noise and High-rate Regimes](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2015.867) · [An improved bound on the fraction of correctable deletions](https://arxiv.org/abs/1507.01719v2) · [The zero-rate threshold for adversarial bit-deletions is less than \(1/2\)](https://arxiv.org/abs/2106.05250v2) · [Random Reed-Solomon Codes Achieve the Half-Singleton Bound for Insertions and Deletions over Linear-Sized Alphabets](https://doi.org/10.4230/LIPIcs.ICALP.2025.60)
Existing status: `source_open` · Summary written: 2026-09-16

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

A binary locally decodable code lets a decoder recover any requested message bit from a few bits of a corrupted codeword. The target is a fixed constant number of probes with a fixed positive fraction of arbitrary errors. The stored length may be any fixed polynomial in the message length, and nonlinear encodings are allowed. The question concerns existence, without an extra demand for an efficient uniform construction. A complete Lean-checked answer must establish this family or rule out all such constant-query polynomial-length families.

[Read in atlas](index.html#TCS-1020) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Improved Lower Bounds for all Odd-Query Locally Decodable Codes](https://arxiv.org/abs/2411.14361v1) · [Subexponential Upper Bounds for 3-Restricted Matching Vector Families](https://eccc.weizmann.ac.il/report/2026/141/) · [Improved Subexponential Upper Bounds for 3-Restricted Matching Vector Families](https://arxiv.org/abs/2608.27859v1) · [Relaxed vs. Full Local Decodability with Few Queries: Equivalence and Separations for Linear Codes](https://arxiv.org/abs/2511.02633) · [Amortized Relaxed Locally Decodable Codes](https://arxiv.org/abs/2609.16332v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-0013 — Efficient explicit constant-rate tree codes

A binary tree code assigns output labels to every possible input history as that history unfolds. After two histories first differ, their output suffixes must disagree on a fixed positive fraction of positions. A fixed output alphabet keeps the information rate bounded below by a positive constant. The requested uniform algorithms must encode efficiently and recover any received prefix satisfying the stated suffix-error promise. The checked 2026 literature still leaves this constant-rate construction open, and its new barrier concerns an additional restricted property.

[Read in atlas](index.html#TCS-0013) · [Mathematics and Computation, draft of 27 March 2018](https://www.math.ias.edu/files/mathandcomp.pdf) · [Explicit Capacity Approaching Coding for Interactive Communication](https://www.math.ias.edu/~avi/PUBLICATIONS/GellsHaKoRoWi_Oct2018.pdf) · [The Rate-Immediacy Barrier in Explicit Tree Code Constructions](https://arxiv.org/abs/2504.09388v2)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-1012 — Explicit binary codes with efficient list decoding up to capacity

The question asks for explicit binary codes with efficient list decoding throughout the binary capacity region. For each fixed error fraction and strictly smaller admissible rate, one deterministic pair of programs must work for every message length. The decoder must list all messages consistent with any adversarially corrupted received word in polynomial time. The inherited title and reversed printed rate inequality are corrected explicitly rather than interpreted as a request to exceed capacity. A complete Lean-checked proof must establish the full construction proposition or its logical negation.

[Read in atlas](index.html#TCS-1012) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf#page=154) · [Advances in List Decoding of Polynomial Codes](https://eccc.weizmann.ac.il/report/2026/032/) · [Time- and Space-Efficient List Decoding up to Capacity](https://arxiv.org/abs/2608.15937v1) · [Algorithmic List Decoding at Capacity and Optimal Proximity Gaps for Reed--Solomon Codes](https://eccc.weizmann.ac.il/report/2026/169/)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-6738 — Linear-length locally testable proofs for CircuitSAT

A locally testable proof can be checked by reading only a constant number of its bits. The question asks for such satisfiability proofs with length at most a constant times the number of circuit nodes. For every fixed distance threshold, the tester must reject proofs far from all valid proofs, including when the circuit is satisfiable. The original source also asked about locally testable codes, whose linear-length existence was resolved in 2021. Known quasi-linear PCP results provide related progress but do not meet the retained linear-length proof-testing requirement.

[Read in atlas](index.html#TCS-6738) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf) · [Introduction to Property Testing: updates to open problems](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html) · [Locally Testable Codes with constant rate, distance, and locality](https://eccc.weizmann.ac.il/report/2021/151/) · [Quasi-Linear Size PCPs with Small Soundness from HDX](https://arxiv.org/abs/2407.12762v2)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-3513 — Explicit positive-rate codes below the Plotkin point

A fixed adversarial channel restricts the types of transmitted words and noise words and transforms each input symbol through a specified table. The source gives a completely positive distribution criterion ensuring that positive-rate codes with a fixed list bound exist. The question asks whether every channel satisfying that criterion also admits deterministic encoders running in polynomial time in blocklength. The card fixes a finite-description channel model, preserves its alphabet and list bound, and specifies uniformity and the permitted infinite set of blocklengths. A resolution would connect a general information-theoretic feasibility criterion with explicit error-correcting constructions across many adversarial channel models.

[Read in atlas](index.html#TCS-3513) · [Generalized List Decoding](https://doi.org/10.4230/LIPIcs.ITCS.2020.51) · [Tight Bounds on List-Decodable and List-Recoverable Zero-Rate Codes](https://doi.org/10.4230/LIPIcs.ITCS.2025.82) · [Probabilistic Guarantees to Explicit Constructions: Local Properties of Linear Codes](https://arxiv.org/abs/2510.06185v2) · [From Random to Explicit via Subspace Designs With Applications to Local Properties and Matroids](https://arxiv.org/abs/2510.13777v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4968 — Do nonlinear binary codes have a strictly better asymptotic rate?

Binary linear codes are vector subspaces, while arbitrary codes can be any sets of binary words. At each fixed relative minimum distance, compare their largest possible asymptotic information rates. The question asks whether arbitrary codes have a strictly higher rate at even one distance between zero and one half. Any fixed positive rate gap counts, but a finite-block advantage or a comparison with one construction does not. The source motivates the comparison through linear-programming hierarchies, and the checked later bound does not resolve it.

[Read in atlas](index.html#TCS-4968) · [A Complete Linear Programming Hierarchy for Linear Codes](https://doi.org/10.4230/LIPIcs.ITCS.2022.51) · [An Elementary Proof of the First LP Bound on the Rate of Binary Codes](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.48)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-1011 — Full-length Reed–Solomon list decoding beyond Johnson

The question asks whether some infinite family of full-length Reed–Solomon codes has polynomially bounded lists beyond the Johnson threshold. The code evaluates every polynomial of degree at most a fixed fraction of the field size at every field element. One fixed pair of rate and agreement constants and one polynomial list bound must work for every received word along infinitely many field sizes. This is an information-theoretic existence question and does not demand an efficient decoding algorithm. Recent capacity theorems for randomly punctured codes and lower bounds for list recovery have different quantifiers or models and do not settle this target.

[Read in atlas](index.html#TCS-1011) · [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf) · [Random Reed–Solomon Codes Achieve List-Decoding Capacity With Linear-Sized Alphabets](https://arxiv.org/abs/2304.09445) · [Near-Optimal List-Recovery of Linear Code Families](https://drops.dagstuhl.de/storage/00lipics/lipics-vol353-approx-random2025/LIPIcs.APPROX-RANDOM.2025.53/LIPIcs.APPROX-RANDOM.2025.53.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0196 — Polyhedrality of linear-rank inequality cones

Linear rank inequalities constrain the dimensions of every nonempty sum in a collection of subspaces. The target cone contains the coefficient vectors of inequalities valid over every commutative field. The question asks whether this cone is polyhedral for each fixed number of subspaces at least six. A finite description is known through five subspaces, while increasing families of inequalities for larger collections do not themselves settle the fixed-dimension question. A resolution would determine whether linear information profiles admit a finite complete set of universal linear constraints at each fixed arity.

[Read in atlas](index.html#TCS-0196) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Linear rank inequalities on five or more variables](https://arxiv.org/abs/0910.0284v3) · [Interaction between skew-representability, tensor products, extension properties, and rank inequalities](https://arxiv.org/abs/2507.10709v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-4802 — The maximal error fraction for constant-rate binary two-way codes

Alice sends an arbitrary binary message to Bob, and Bob may send costly, corruptible feedback bits. The speaking order is fixed, and an adversary may flip a bounded fraction of all transmitted bits in both directions. The target is the largest tolerable fraction with linear total communication, to certified absolute error 1/100. A construction tolerates slightly more than one quarter, while the checked upper bound is 13/47. Those bounds still leave too wide an interval, and noiseless-feedback results do not settle this model.

[Read in atlas](index.html#TCS-4802) · [Binary Codes with Resilience Beyond 1/4 via Interaction](https://doi.org/10.1109/FOCS54457.2022.00008) · [Interactive Error Correcting Codes: New Constructions and Impossibility Bounds](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.32) · [Round-Vs-Resilience Tradeoffs for Binary Feedback Channels](https://doi.org/10.4230/LIPIcs.ITCS.2025.22)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0178 — Bounded-alphabet approximation of the β = 0 entropy face

A symmetric three-dimensional slice of the four-variable almost-entropic region has a distinguished face labeled β = 0. The question asks whether every point of that face is a limit of interior points represented by normalized entropy vectors of bounded-alphabet distributions. One finite bound on the alphabet size must work for the whole face and for every requested accuracy. The source reports small-alphabet points on the face but an apparent gap in numerical exploration of the interior. The card fixes the visualization’s coordinate convention and distinguishes actual entropy realizations from transformed almost-entropic samples.

[Read in atlas](index.html#TCS-0178) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Visualizing the entropy region](https://github.com/lcsirmaz/entropy-rules/blob/089f64bb/visual/DESCRIPTION.md) · [Entropy region and convolution](https://arxiv.org/abs/1310.5957v1)
Existing status: `source_open` · Summary written: 2026-09-18

### TCS-0184 — Entropic matroid approximations approaching unit ratio

The input is an integer-valued polymatroid exactly represented by the joint entropies of finite random variables. After multiplying its values by an integer, the free expansion replaces each coordinate by a block of independent matroid elements. The question asks whether an arbitrarily large fraction of every block can be retained so that the resulting matroid has an exact entropy representation up to one common scaling factor. This would connect entropy functions with exact combinatorial independence while preserving the specific expansion structure. A complete Lean proof must establish this approximation for every admissible input and every precision or give an input with a fixed positive retention gap.

[Read in atlas](index.html#TCS-0184) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [On entropic and almost multilinear representability of matroids](https://arxiv.org/abs/2206.03465v3) · [Partition-Symmetrical Entropy Functions](https://arxiv.org/abs/1407.7405v2) · [On the recognition problem for limits of entropy functions](https://arxiv.org/abs/2509.06302v1) · [Entropy approximations of algebraic matroids over finite fields](https://arxiv.org/abs/2509.15348v1) · [Four-Entropic Matroids Are Quaternary](https://arxiv.org/abs/2608.20553v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0187 — Are characteristic sets of linear-rank inequalities finite or cofinite?

Fix a rational homogeneous linear inequality in the dimensions of sums of finitely many subspaces. For each prime, test whether that inequality holds for every subspace configuration over its prime field, in every finite dimension. The question is whether the set of primes where it holds must be finite or have finite complement. Known characteristic-dependent constructions realize finite and cofinite sets but do not by themselves classify every inequality. This is an explicit specialization of the source’s broader field-dependence question, and its exact current status remains uncertain.

[Read in atlas](index.html#TCS-0187) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Characteristic-Dependent Linear Rank Inequalities via Complementary Vector Spaces](https://arxiv.org/abs/1903.11587v2) · [Access structures for finding characteristic-dependent linear rank inequalities](https://doi.org/10.14736/kyb-2023-2-0198)
Existing status: `uncertain` · Summary written: 2026-09-18

### TCS-0205 — The infimal normalized Ingleton score

The Ingleton score divides a particular linear combination of four-variable entropies by their joint entropy. Negative scores measure violations of an inequality satisfied by linear-rank configurations. The target is the infimum over all finite joint distributions, with no fixed alphabet bound, to certified absolute error 1/100. Known examples near −0.0925 disprove the four-atom conjecture but do not supply the needed global lower bound. A complete Lean-checked answer must certify both sides and need not prove algebraicity or attainment.

[Read in atlas](index.html#TCS-0205) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Entropy region and convolution](https://arxiv.org/abs/1310.5957v1) · [Violations of the Ingleton inequality and revising the four-atom conjecture](https://doi.org/10.14736/kyb-2020-5-0916) · [Optimizing Distributions for Associated Entropic Vectors via Generative Convolutional Neural Networks](https://doi.org/10.3390/e26080711)
Existing status: `source_open` · Summary written: 2026-09-17

## Property testing and distribution learning (16)

### TCS-6630 — Effective classification of polynomially testable hereditary graph properties

A finite family of forbidden induced graphs specifies a hereditary graph property. The question asks whether a total algorithm can decide from that family whether its canonical one-sided test has polynomial reciprocal-distance sample complexity. Every query is an adjacency check, while rejection must exhibit a forbidden pattern with both its edges and its nonedges. Known structural conditions and quantitative container equivalences do not give the total finite-input classifier required by this card. Algorithmic decidability is the inherited editorial specification, and its status is uncertain rather than attributed verbatim as a conjecture of the structural survey.

[Read in atlas](index.html#TCS-6630) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1) · [A Characterization of the (Natural) Graph Properties Testable with One-Sided Error](https://epubs.siam.org/doi/10.1137/06064888X) · [Removal Lemmas with Polynomial Bounds](https://arxiv.org/abs/1611.10315) · [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article) · [Efficient Removal without Efficient Regularity](https://www.math.tau.ac.il/~asafico/C4.pdf) · [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/)
Existing status: `uncertain` · Summary written: 2026-09-15

### TCS-1033 — Polynomial testability versus distance estimation

A dense-graph tester distinguishes membership in a property from graphs that require many edge changes to satisfy it. A distance estimator must approximate that repair cost on every input, including graphs close to the property. The question asks whether a query bound polynomial in reciprocal accuracy for testing always entails a polynomial bound for estimation. The algorithms may use unlimited local computation, but must be uniform and obey query bounds independent of graph order. Known general conversions and positive special cases leave the polynomial-preservation target unresolved in the checked sources, and the stronger source question remains separately recorded.

[Read in atlas](index.html#TCS-1033) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1) · [Testing versus Estimation of Graph Properties](https://epubs.siam.org/doi/10.1137/060652324) · [Testing versus estimation of graph properties, revisited](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.21221) · [On Efficient Distance Approximation for Graph Properties](https://arxiv.org/abs/2001.01452)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-6672 — Sublinear testing of bounded-degree graph isomorphism

The tester sees two sparse graphs only by asking for individual neighbors. It must accept isomorphic graphs and reject pairs that require many edge edits after every possible relabelling. The question asks for fewer than a linear number of queries at every fixed degree bound and proximity. Both graphs are unknown, and arbitrary disconnected or highly connected inputs must be covered. Known small-component testers and recent results for typical known targets do not establish this general two-input guarantee.

[Read in atlas](index.html#TCS-6672) · [Open Problems in Property Testing of Graphs](https://eccc.weizmann.ac.il/report/2021/088/) · [Testing Isomorphism in the Bounded-Degree Graph Model](https://www.wisdom.weizmann.ac.il/~/oded/VO/iso.pdf) · [On Testing Isomorphism to a Fixed Graph in the Bounded-Degree Graph Model](https://www.wisdom.weizmann.ac.il/~/oded/COL3/bdg-iso-fixed.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-1030 — Polynomial testing of induced four-cycle freeness

The question asks whether induced four-cycle freeness can be tested from a random sample whose size is polynomial in reciprocal proximity. An induced four-cycle has its four cycle edges and neither diagonal, and repairing the graph permits both edge additions and deletions. The canonical tester rejects when its sampled induced subgraph contains such a cycle and must reject every far graph with probability at least two thirds. An exponential removal bound is known, while the polynomial improvement remains explicitly conjectured in the checked 2025 source. This concrete target was selected with user authorization from the broader inherited classification question and would settle its remaining single-pattern case up to complementation.

[Read in atlas](index.html#TCS-1030) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf) · [Efficient Removal without Efficient Regularity](https://www.math.tau.ac.il/~asafico/C4.pdf) · [Easily Testable Graph Properties](https://www.cambridge.org/core/product/identifier/S0963548314000765/type/journal_article) · [A Quantitative Container Characterization of One-Sided Testability](https://eccc.weizmann.ac.il/report/2026/144/)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-4376 — Planar graphs from local neighborhoods

The question compares two planar graphs through the rooted neighborhoods around all their vertices. It asks whether a radius depending only on the allowed error makes identical neighborhood multisets imply closeness under edge edits and vertex relabeling. No maximum-degree bound is imposed, so even a small-radius neighborhood may be large. The source proves the analogous result for outerplanar graphs, while bounded-degree planar theorems allow the radius to depend on the degree bound. This specific structural question replaces the original broad classification target by an explicitly selected yes/no assertion.

[Read in atlas](index.html#TCS-4376) · [Every Property of Outerplanar Graphs is Testable](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2016.21) · [The complexity of testing all properties of planar graphs, and the role of isomorphism](https://arxiv.org/abs/2108.10547)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1029 — Sharp graph-removal bounds for fixed patterns

For each fixed connected graph pattern, the question asks how few ordinary copies a graph can contain while still being far from avoiding that pattern. Distance is the fraction of adjacency-matrix entries that must change, and each vertex subset supporting the pattern is counted once. The target is matching constant-factor bounds in both the graph order and the proximity parameter, with constants allowed to depend on the pattern. The removal lemma guarantees positive density at every fixed distance, but the general quantitative bounds remain widely separated. Sharp bounds would quantify the worst-case visibility of local violations and the sampling cost of detecting them.

[Read in atlas](index.html#TCS-1029) · [Introduction to Property Testing (April 2017 manuscript)](https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf) · [A new proof of the graph removal lemma](https://arxiv.org/abs/1006.1300) · [Minimum degree and the graph removal lemma](https://arxiv.org/abs/2105.09194) · [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1) · [Hypergraph removal with polynomial bounds](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/hypergraph-removal-with-polynomial-bounds/AA404A0C00FFA07E0E5C7CB03DBF1A6F)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-5443 — Polynomial-time density learning of Gaussian mixtures

The learner receives independent observations from a mixture of at most k nondegenerate Gaussians in d dimensions. It must output another such mixture whose whole distribution is close in total variation, without reconstructing the original components. The question asks for a uniform algorithm with time polynomial jointly in k and d for each fixed accuracy, using explicitly specified exact-real arithmetic. Polynomial sample sufficiency coexists with statistical-query lower bounds and conditional computational hardness, neither of which is silently treated as an unconditional resolution. Newer positive results with bounded parameters, fixed component counts or growing dimension exponents do not establish the full target.

[Read in atlas](index.html#TCS-5443) · [Mixtures of Gaussians are Privately Learnable with a Polynomial Number of Samples](https://proceedings.mlr.press/v237/afzali24a.html) · [Statistical Query Lower Bounds for Robust Estimation of High-dimensional Gaussians and Gaussian Mixtures](https://arxiv.org/abs/1611.03473) · [Continuous LWE is as Hard as LWE & Applications to Learning Gaussian Mixtures](https://arxiv.org/abs/2204.02550) · [Learning general Gaussian mixtures with efficient score matching](https://arxiv.org/abs/2404.18893v2) · [On Learning Parallel Pancakes with Mostly Uniform Weights](https://arxiv.org/abs/2504.15251v1) · [Sharp proper estimation of fixed-component Gaussian location mixtures in polynomial time](https://arxiv.org/abs/2608.12701v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-5085 — Query complexity of Max-CSP testing

A tester must distinguish constraint systems whose optimum satisfied fractions lie on opposite sides of a fixed gap. It can query variables to reveal incident constraint occurrences, with only a constant number of occurrences per variable. The target is the asymptotic query complexity for every finite predicate template, gap, degree bound and density regime. The actual number of constraints matters because value is normalized by constraints rather than by all possible incidence slots. Known linear lower bounds and related streaming results leave the complete query classification unresolved.

[Read in atlas](index.html#TCS-5085) · [Unbounded-Width CSPs Are Untestable in a Sublinear Number of Queries](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.31) · [Near-Optimal Space Lower Bounds for Streaming CSPs](https://arxiv.org/abs/2604.01400v1)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-3906 — Sample complexity of symmetric Markov-chain identity testing

The tester observes one trajectory from an unknown symmetric Markov chain and receives a complete known reference transition matrix. It must distinguish equality from positive spectral discrepancy for every uncontrolled starting state, without resets or chosen-state sampling. The target is matching joint dependence of the worst-case required trajectory length on the number of states and the proximity parameter. Later testing results remove hitting-time dependence under their stated irreducibility assumptions, but the checked bounds still leave a reciprocal-distance gap. The card preserves the full original symmetric model and distinguishes its transition discrepancy from stationary-distribution or matrix-norm testing.

[Read in atlas](index.html#TCS-3906) · [Testing Symmetric Markov Chains From a Single Trajectory](https://proceedings.mlr.press/v75/daskalakis18a.html) · [Testing Symmetric Markov Chains Without Hitting](https://proceedings.mlr.press/v99/cherapanamjeri19a.html) · [Identity testing of reversible Markov chains](https://arxiv.org/abs/2105.06347) · [A Geometric Reduction Approach for Identity Testing of Reversible Markov Chains](https://arxiv.org/abs/2302.08059)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-5210 — Polylogarithmic-query pattern-freeness testing

A permutation pattern specifies the strict relative order of values at increasing positions of a real-valued sequence. The question asks whether every fixed pattern has an adaptive one-sided tester using only a polylogarithmic number of queries in the sequence length. Distance is the fraction of entries that must change to remove all occurrences, and the query bound may depend arbitrarily on the fixed pattern and proximity. The checked general adaptive upper bound is subpolynomial but not polylogarithmic, while newer lower bounds on hypergrids concern a different domain. Resolving the conjecture would clarify how much adaptive observations can improve the testing of ordered obstructions.

[Read in atlas](index.html#TCS-5210) · [Strongly Sublinear Algorithms for Testing Pattern Freeness](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.98) · [Strongly Sublinear Algorithms for Testing Pattern Freeness](https://theoretics.episciences.org/12865/pdf) · [Testing forbidden order-pattern properties on hypergrids](https://epubs.siam.org/doi/10.1137/1.9781611978971.114)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0848 — Polynomial-query submodularity testing

Submodularity expresses diminishing returns for a real-valued function on all subsets of a finite ground set. The question asks whether a polynomial number of exact value queries can test this property with one-sided error. Distance is the fraction of table entries that must change to obtain a submodular function, regardless of change magnitude. Known general upper and lower bounds leave the polynomial-query question unresolved, and constant-query norm-distance results concern a different task. A resolution would determine how efficiently an oracle’s global diminishing-returns structure can be checked from limited access.

[Read in atlas](index.html#TCS-0848) · [Problem 37: Testing Submodularity](https://sublinear.info/index.php?title=Open_Problems:37) · [Is Submodularity Testable?](https://theory.stanford.edu/~jvondrak/data/submod-testing-alg.pdf) · [Testing Real-Valued Modularity and Submodularity](https://www.ias.edu/sites/default/files/math/csdm/15-16/HatamiVondrak.pdf) · [Testing Submodularity and Other Properties of Valuation Functions](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.33) · [Testing k-Submodularity](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.52)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0841 — Query complexity of conditional equivalence testing

Two unknown distributions must be distinguished as equal or separated by a fixed positive total variation distance. Each conditional query selects one distribution and a nonempty subset, then receives a fresh sample restricted to that subset. The target is matching constant-factor query bounds as the domain grows, allowing arbitrary adaptive queries and constants depending on the fixed proximity. The main gap was closed in 2024 up to iterated-logarithmic factors, which are not hidden by this card’s answer criterion. The result would pin down the remaining domain-size cost of comparing two unknown distributions under powerful conditional access.

[Read in atlas](index.html#TCS-0841) · [Problem 87: Equivalence Testing with Conditional Samples](https://sublinear.info/87) · [A Chasm Between Identity and Equivalence Testing with Conditional Queries](https://theoryofcomputing.org/articles/v014a019/) · [Faster Algorithms for Testing under Conditional Sampling](https://proceedings.mlr.press/v40/Falahatgar15.html) · [Tight Lower Bound on Equivalence Testing in Conditional Sampling Model](https://epubs.siam.org/doi/10.1137/1.9781611977912.153) · [Interactive Proofs for Distribution Testing with Conditional Oracles](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.18)
Existing status: `uncertain` · Summary written: 2026-09-15

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

### TCS-4259 — Optimal query cost of reducing testing adaptivity

A property tester probes bits in batches and may choose later batches using previous answers. The source counts one more batch than the number of adaptive rounds. The target is the largest query budget needed after reducing the number of rounds, among properties testable with the original budget. Both the property and its proximity and error guarantees remain fixed during the reduction. The benchmark asks for matching bounds with constants independent of all three resource parameters.

[Read in atlas](index.html#TCS-4259) · [An Adaptivity Hierarchy Theorem for Property Testing](https://doi.org/10.4230/LIPIcs.CCC.2017.27) · [An adaptivity hierarchy theorem for property testing — journal publication](https://doi.org/10.1007/s00037-018-0168-4) · [An adaptivity hierarchy theorem for property testing — institutional attachment](https://www.repository.cam.ac.uk/items/73b70279-d662-43f0-b591-98afd3ce529c)
Existing status: `source_open` · Summary written: 2026-09-13

## Differential privacy (4)

### TCS-0506 — Private PAC sample complexity from VC and Littlestone dimensions

A private PAC learner must predict a Boolean concept accurately while protecting every individual labeled example. The card asks for sample size polynomial in VC dimension and the iterated logarithm of Littlestone dimension for every finite class. It retains fixed accuracy and confidence and privacy slack shrinking quadratically with the actual sample size. The latest checked general upper bound is polynomial in Littlestone dimension itself, while the proposed much smaller dependence is known in important special cases. A solution must prove the universal bound or a superpolynomial obstruction for unrestricted improper private learners, with its full quantifiers checked in Lean.

[Read in atlas](index.html#TCS-0506) · [Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html) · [Private Learning of Littlestone Classes, Revisited](https://arxiv.org/abs/2510.00076) · [An Õptimal Differentially Private PAC Learner for Concept Classes with VC Dimension 1](https://arxiv.org/abs/2505.06581) · [STOC 2026 proceedings table of contents](https://acm-stoc.org/stoc2026/toc.html)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6673 — Optimal error for pure-DP continual counting

Continual counting releases prefix sums of a binary stream as its bits arrive. The target is the smallest worst-input expected maximum absolute error over all timestamps under pure differential privacy with privacy parameter one half. Every output prefix must depend only on the input prefix already observed, and privacy protects the whole transcript when one bit changes. The checked literature leaves a gap between logarithmic powers three halves and two, while newer matrix results concern different squared-error criteria. Matching bounds would quantify the unavoidable accuracy loss of this basic stream-release primitive.

[Read in atlas](index.html#TCS-6673) · [The Binary Tree Mechanism is Optimal for Approximate Differentially Private Continual Counting](https://arxiv.org/abs/2607.00876v2) · [The Price of Differential Privacy under Continual Observation](https://proceedings.mlr.press/v202/jain23b.html) · [Improved Error Bounds for Pure Differentially Private Continual Counting via Matrix Factorization](https://arxiv.org/abs/2607.08963) · [Costs of Arbitrary Real Matrix Factorizations for Pure-DP Continual Counting](https://arxiv.org/abs/2607.28703v2) · [A Near-Optimal Lower Bound for Prefix-Matrix Factorizations](https://arxiv.org/abs/2608.08238)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7236 — Polynomial-time private release of all marginals

A marginal query asks what fraction of database rows match a pattern on selected attributes. The card asks for one private synopsis that answers all exponentially many such queries with error tending to zero as the dimension grows. Both creating the synopsis and evaluating a short query must use polynomial time, with only polynomially many input rows. Known interactive, synthetic-data and Gaussian-factorization results impose different resource or output requirements and do not settle this target. A complete Lean answer must prove the specified uniform existence statement or rule out every mechanism and evaluator satisfying it.

[Read in atlas](index.html#TCS-7236) · [The Complexity of Differential Privacy](https://salil.seas.harvard.edu/publications/complexity-differential-privacy) · [Faster Private Release of Marginals on Small Databases](https://arxiv.org/abs/1304.3754) · [Weighted Fourier Factorizations: Optimal Gaussian Noise for Differentially Private Marginal and Product Queries](https://arxiv.org/abs/2512.21499)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0507 — Optimal regret for private stochastic online learning

A learner repeatedly chooses an action and then observes the losses of every action. The losses are independent draws from fixed unknown distributions, and one action has strictly smallest mean loss. The card asks for matching-order expected pseudo-regret under pure privacy protecting one entire round of observations. A published 2026 upper bound removes the time-horizon factor but leaves a logarithmic gap in the number of actions. A solution must identify the rate throughout the stated parameter domain and certify both achievable guarantees and unavoidable loss in Lean.

[Read in atlas](index.html#TCS-0507) · [Open Problem: Optimal Rates for Stochastic Decision-Theoretic Online Learning Under Differentially Privacy](https://proceedings.mlr.press/v247/hu24a.html) · [Improved Regret in Stochastic Decision-Theoretic Online Learning under Differential Privacy](https://proceedings.mlr.press/v313/wu26a.html) · [Near-Optimal Algorithms for Differentially Private Online Learning in a Stochastic Environment](https://arxiv.org/abs/2102.07929)
Existing status: `source_open` · Summary written: 2026-09-15

## Constraint satisfaction (19)

### TCS-6635 — Finite-domain promise CSP dichotomy

A finite promise CSP distinguishes inputs satisfying stronger local constraints from inputs failing even weaker constraints. The question asks whether every fixed finite template pair has a deterministic polynomial-time decision algorithm or is NP-hard under promise-preserving many-one reductions. The algorithm or reduction may depend on the pair, and no effective procedure for classifying input templates is required. The ordinary CSP dichotomy and several promise subclasses are known, but relaxing the constraints changes the classification problem substantially. The checked 2026 results concern restricted families and leave this full unconditional decision dichotomy open in the cited sources.

[Read in atlas](index.html#TCS-6635) · [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538v1) · [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021v2) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914v11) · [Promise Constraint Satisfaction: Algebraic Structure and a Symmetric Boolean Dichotomy](https://arxiv.org/abs/1704.01937v2) · [Dichotomy for Symmetric Boolean PCSPs](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.57) · [Promises Make Finite (Constraint Satisfaction) Problems Infinitary](https://www.karlin.mff.cuni.cz/~barto/Articles/DoNotPromise.pdf) · [Towards infinite PCSP: a dichotomy for monochromatic cliques](https://arxiv.org/abs/2605.09815v1) · [Approximating 1-In-3 SAT by Linearly Ordered Hypergraph 3-Colouring Is NP-Hard](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.184)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-6636 — Bodirsky–Pinsker conjecture

The conjecture asks for a P-versus-NP-complete dichotomy for all finite-signature first-order reducts of countable finitely bounded homogeneous structures. Inputs are finite constraint systems, while their possible values lie in a fixed domain that may be infinite. Homogeneity provides symmetry, and finitely many forbidden induced patterns provide polynomial-size certificates despite the infinite domain. Recent results simplify the conjecture’s scope or classify lower complexity boundaries, while the full tractability implication remains open in the checked sources. A resolution would determine whether this broad structural framework rules out intermediate NP complexity.

[Read in atlas](index.html#TCS-6636) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914) · [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf) · [Topology Is Irrelevant (In a Dichotomy Conjecture for Infinite Domain Constraint Satisfaction Problems)](https://doi.org/10.1137/18M1216213) · [Three Fundamental Questions in Modern Infinite-Domain Constraint Satisfaction](https://arxiv.org/abs/2502.06621v4) · [Constraint Satisfaction Problems over Finitely Bounded Homogeneous Structures: a Dichotomy between FO and L-hard](https://arxiv.org/abs/2601.22691v3) · [Decidability of Interpretability](https://arxiv.org/abs/2602.02302v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6637 — Constant-colour polynomial-time colouring of 3-colourable graphs

The input is a graph known to admit a three-colouring, without a supplied witness. The question asks whether one fixed larger palette permits a randomized polynomial-time algorithm on every such graph. Successful outputs must colour every vertex properly, with probability at least two thirds for each input. A14September2026 preprint claims all-constant decision hardness, which would still require NP different from RP to exclude the randomized algorithms in this question. A complete Lean-checked answer must establish such an algorithm or exclude every constant palette in the full randomized model.

[Read in atlas](index.html#TCS-6637) · [Better coloring of 3-colorable graphs](https://arxiv.org/abs/2406.00357v1) · [Algebraic Approach to Promise Constraint Satisfaction](https://arxiv.org/abs/1811.00970v3) · [d-To-1 Hardness of Coloring 3-Colorable Graphs with \(O(1)\) Colors](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.62) · [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904v1) · [Undefinability of Approximation of 2-to-2 Games](https://arxiv.org/abs/2504.03523v2) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6675 — Search-to-decision equivalence for finite promise CSPs

A finite promise CSP distinguishes strong constraints whose satisfiability is guaranteed from weaker constraints an output must satisfy. The decision problem separates strongly satisfiable inputs from those with no weak solution. The question asks whether every fixed template with a deterministic polynomial-time decider also permits deterministic polynomial-time construction on the original stronger promise. Hardness of rounding arbitrary relaxation-accepted inputs and undecidability of template recognition leave this implication unresolved. A resolution would clarify whether tractability of finite promise constraints always extends from recognizing feasibility to producing assignments.

[Read in atlas](index.html#TCS-6675) · [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538v1) · [Algebraic approach to promise constraint satisfaction](https://arxiv.org/abs/1811.00970v3) · [Ineffectiveness for Search and Undecidability of PCSP Meta-Problems](https://arxiv.org/abs/2504.04639v4) · [New Algorithms and Hardness Results for Robust Satisfiability of (Promise) CSPs](https://arxiv.org/abs/2602.10368v1) · [Publications — FOCS 2025 research summary](https://albertolarrauri.github.io/publications/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6725 — Logarithmic-color approximation of 3-colorable graphs

Every promised input graph admits a proper colouring with three colours, but that hidden colouring is not given. The question asks for a uniform polynomial-time algorithm using only logarithmically many colours in expectation. Randomness follows the source’s approximation convention while every produced colouring must be exactly proper. Recent growing-palette algorithms and fixed-palette hardness results leave this logarithmic guarantee unestablished. An accepted answer proves existence or impossibility of the full algorithmic guarantee in Lean.

[Read in atlas](index.html#TCS-6725) · [The Design of Approximation Algorithms](https://www.designofapproxalgs.com/book.pdf) · [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904v1) · [Algebraic approach to promise constraint satisfaction](https://arxiv.org/abs/1811.00970v3)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7237 — Hardness of 6-coloring 3-colorable graphs

The target is an unconditional polynomial-time reduction that maps satisfiable formulas to three-colourable graphs and unsatisfiable formulas to graphs requiring more than six colours. Graphs needing four, five or six colours are outside the promise and cannot be valid outputs of the reduction. Known unconditional hardness at five colours does not automatically extend to six. A14September2026 preprint claims the required gap for every fixed larger palette, but its complete proof has not been independently verified in this review. An accepted answer proves existence or nonexistence of the full reduction in Lean.

[Read in atlas](index.html#TCS-7237) · [Algebraic approach to promise constraint satisfaction](https://arxiv.org/abs/1811.00970v3) · [Beyond PCSP(1-in-3,NAE)](https://drops.dagstuhl.de/storage/00lipics/lipics-vol198-icalp2021/LIPIcs.ICALP.2021.121/LIPIcs.ICALP.2021.121.pdf) · [Improved SDP-Based Algorithm for Coloring 3-Colorable Graphs](https://arxiv.org/abs/2602.05904v1) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-1173 — NP-intermediate \(\omega\)-categorical CSPs

Assuming P differs from NP, the question asks whether an omega-categorical fixed-template CSP can have intermediate NP complexity. Omega-categoricity means finitely many symmetry orbits at each fixed tuple length, and the template has a finite relational signature. The CSP must lie in NP while being neither polynomial-time decidable nor NP-complete under polynomial-time many-one reductions. CoNP-intermediate examples and completeness at every polynomial-hierarchy level are known, but they do not supply the required NP-intermediate example. A resolution would determine whether this broad symmetry condition alone rules out intermediate complexity inside NP.

[Read in atlas](index.html#TCS-1173) · [The Polynomial Hierarchy and omega-Categorical CSPs](https://doi.org/10.4230/LIPIcs.MFCS.2026.96) · [Non-dichotomies in Constraint Satisfaction Complexity](https://www.lix.polytechnique.fr/~bodirsky/publications/nodich.pdf) · [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf) · [The Polynomial Hierarchy and omega-categorical CSPs](https://arxiv.org/abs/2604.24539v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1555 — VCSP tractability over the countable random graph

The question concerns valued constraint problems whose costs depend only on equality and adjacency patterns in the countable random graph. It asks whether every fixed finite-signature template is polynomial-time solvable whenever it cannot pp-construct a triangle. The expressive closure includes sums, projection, scaling, feasibility and optimality, and the construction can use arbitrary finite powers. The temporal classification proves an analogous result for ordered rationals but the January 2026 source still poses the random-graph case. An accepted answer proves the full implication or an unconditional counterexample with its complexity lower bound in Lean.

[Read in atlas](index.html#TCS-1555) · [Temporal Valued Constraint Satisfaction Problems](https://doi.org/10.4230/LIPIcs.MFCS.2025.24) · [A Complexity Dichotomy for Temporal Valued Constraint Satisfaction Problems](https://arxiv.org/abs/2409.07285v2) · [The Complexity of Resilience Problems via Valued Constraint Satisfaction](https://arxiv.org/abs/2309.15654v6)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3984 — Super-log-logarithmic colouring hardness for two-colourable triple systems

The question concerns colouring hypergraphs whose edges contain exactly three vertices and whose vertices admit a hidden two-colouring. It asks for a hardness reduction ruling out a palette that grows faster than log log of the output vertex count. A deterministic quasipolynomial reduction from Boolean satisfiability suffices, and a polynomial reduction is a stronger permitted answer. Known larger palette gaps often change the edge size or allow three colours in the completeness promise. The latest fixed-density independent-set hardness claim does not by itself give the required quantitative growing-palette gap.

[Read in atlas](index.html#TCS-3984) · [NP-Hardness of Coloring 2-Colorable Hypergraph with Poly-Logarithmically Many Colors](https://doi.org/10.4230/LIPIcs.ICALP.2018.15) · [Super-polylogarithmic hypergraph coloring hardness via low-degree long codes](https://arxiv.org/abs/1311.7407) · [On the Hardness of 4-to-1 Games with Perfect Completeness](https://eccc.weizmann.ac.il/report/2026/179/)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6748 — Boolean decision-Holant dichotomy

Boolean decision Holant asks whether edges of a graph can be assigned zero or one so that every local relation is satisfied. The question seeks a structural classification of all fixed finite relation families that admit polynomial-time decision. The source’s edge-CSP model makes each variable occur in exactly two distinct constraint scopes, without freely adding constants or unary relations. Known results handle the non-delta-matroid boundary, symmetric delta-matroids and even delta-matroids, while the arbitrary delta-matroid region remains the general obstacle. A complete answer would identify the full tractability boundary beyond ordinary Boolean CSP and matching.

[Read in atlas](index.html#TCS-6748) · [On the Complexity of Holant Problems](https://doi.org/10.4230/DFU.Vol7.15301.159) · [Even Delta-Matroids and the Complexity of Planar Boolean CSPs](https://arxiv.org/abs/1602.03124v6) · [A Strongly Polynomial-Time Algorithm for Weighted General Factors with Three Feasible Degrees](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2023.57)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-3585 — Exact exponential-time equivalence for nonnegative Boolean Max-CSP

A Boolean Max-CSP instance asks for an assignment satisfying constraints of maximum total nonnegative weight. Each fixed language has a degree defined by the real multilinear polynomials of its predicates. The question asks whether an exact algorithm with exponential base \(\alpha\) for any NP-hard degree-d language yields the same base for weighted Max d-CNF-SAT. The known classification allows negative weights or imposes closure properties on the language. The remaining issue is preserving the exponential base when removing the sign restriction; the 2024 journal article still asks it.

[Read in atlas](index.html#TCS-3585) · [Optimal Polynomial-Time Compression for Boolean Max CSP](https://doi.org/10.4230/LIPIcs.ESA.2020.63) · [Optimal Polynomial-Time Compression for Boolean Max CSP](https://doi.org/10.1145/3624704)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7116 — Universal representation of NP by \(\omega\)-categorical CSPs

The question asks whether every NP language is polynomial-time Turing equivalent to a CSP with a fixed omega-categorical template. Omega-categoricity means that each finite tuple length has only finitely many symmetry orbits, even when the domain is infinite. The reductions may use adaptive exact membership queries, and no uniform template-construction algorithm or effective template presentation is required. Universality is known for unrestricted infinite templates, while the known omega-categorical construction gives a weaker oracle upper bound. A resolution would determine whether this symmetry condition limits computational representation of NP problems.

[Read in atlas](index.html#TCS-7116) · [Constraint Satisfaction Problems with Infinite Templates](https://www.lix.polytechnique.fr/~bodirsky/publications/csp-survey.pdf) · [Non-dichotomies in Constraint Satisfaction Complexity](https://www.lix.polytechnique.fr/~bodirsky/publications/nodich.pdf) · [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf) · [Three Fundamental Questions in Modern Infinite-Domain Constraint Satisfaction](https://arxiv.org/abs/2502.06621v4)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1807 — Dichotomy for finite-domain restricted CSPs

A restricted CSP asks whether a finite input maps to a fixed finite target, under the promise that it maps to another fixed structure. The restriction structure may be infinite, but the source requires its finite-input CSP to be decidable. The question asks whether every such promise problem is polynomial-time solvable or NP-hard when P differs from NP. Hardness must hold for every decidable completion of the promised answers, and the known dichotomy only covers finite restrictions. A resolution would determine whether decidable homomorphism promises preserve the finite-domain dichotomy or allow intermediate behaviour.

[Read in atlas](index.html#TCS-1807) · [Restricted CSPs and F-Free Digraph Algorithmics](https://doi.org/10.4230/LIPIcs.ICALP.2025.158) · [Restricted CSPs and F-free Digraph Algorithmics](https://arxiv.org/abs/2502.17596v1) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914v11)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1978 — Search tractability of BLP-solvable promise CSPs

A finite promise CSP asks for weakly satisfying assignments when a strongly satisfying assignment is promised. BLP can recognize the decision gap using compatible local probability distributions. The question asks whether every fixed template solved by that relaxation also has a deterministic polynomial-time search algorithm on the original promise. The algorithm may depend on the template and need not round every feasible point of the relaxation. A resolution would determine whether this major decision tractability criterion always yields efficient construction of promised solutions.

[Read in atlas](index.html#TCS-1978) · [Promise and Infinite-Domain Constraint Satisfaction](https://doi.org/10.4230/LIPIcs.CSL.2024.41) · [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538v1) · [Ineffectiveness for Search and Undecidability of PCSP Meta-Problems](https://arxiv.org/abs/2504.04639v4)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0441 — Characterizing CSP languages with linear non-redundancy

Non-redundancy measures how many constraints can remain individually essential in a formula. The question asks which finite languages always allow a subformula with linearly many constraints and the identical set of satisfying assignments. The number of variables is the size parameter, and the linear constant may depend on the language. The classification includes all finite domains and does not require an efficient algorithm to find the subformula. A solution would identify the structural boundary for compact exact descriptions of constraint systems.

[Read in atlas](index.html#TCS-0441) · [PACS 2024: Workshop on Parameterized Algorithms and Constraint Satisfaction — Open problems](https://pacs2024.github.io/pacs2024-open-problems.pdf) · [On Redundancy in Constraint Satisfaction Problems](https://doi.org/10.4230/LIPIcs.CP.2022.11) · [Best-case and Worst-case Sparsifiability of Boolean CSPs](https://arxiv.org/abs/1809.06171) · [The Richness of CSP Non-redundancy](https://arxiv.org/abs/2507.07942v2) · [Super-linear Lower Bounds for CSP Non-Redundancy via Shrinking Instances](https://arxiv.org/abs/2605.19055v1) · [Classification of Non-Redundancy of Boolean Predicates of Arity 4](https://doi.org/10.4230/LIPIcs.CP.2026.8)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0504 — Common polynomial exponent for tractable digraph CSPs

Each fixed finite digraph defines a constraint satisfaction problem through graph homomorphisms. The question asks whether all polynomial-time cases can be solved with one common polynomial exponent. The algorithm and its multiplicative constant may still depend on the fixed target digraph. This is weaker than requiring one algorithm whose input includes an arbitrary target table. A resolution would determine whether qualitative fixed-template tractability admits a shared quantitative time bound.

[Read in atlas](index.html#TCS-0504) · [List of open questions: Uniform PTIME algorithm for tractable CSPs](https://a3nm.net/work/research/questions/#uniform-ptime-algorithm-for-tractable-csps) · [A dichotomy theorem for nonuniform CSPs](https://arxiv.org/abs/1703.03021v2) · [A Proof of the CSP Dichotomy Conjecture](https://arxiv.org/abs/1704.01914v11) · [The Complexity of Finding Coset-Generating Polymorphisms and the Promise Metaproblem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.169)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0444 — Polynomial kernels for Boolean MinCSP

Boolean MinCSP asks whether an assignment can violate at most a specified number of constraints. The question seeks all finite Boolean languages admitting polynomial kernels in that violation budget. A kernel must run in polynomial time and output a same-problem instance with polynomially many parameter-dependent bits. Randomization is allowed, and the recorded complexity assumption may support lower bounds for the excluded languages. A classification would reveal which nearly feasible constraint systems admit efficient compression beyond their known fixed-parameter algorithms.

[Read in atlas](index.html#TCS-0444) · [PACS 2024: Workshop on Parameterized Algorithms and Constraint Satisfaction — Open problems](https://pacs2024.github.io/pacs2024-open-problems.pdf) · [Flow-augmentation III: Complexity dichotomy for Boolean CSPs parameterized by the number of unsatisfied constraints](https://arxiv.org/abs/2207.07422v3) · [Representative Sets and Irrelevant Vertices: New Tools for Kernelization](https://doi.org/10.1145/3390887) · [Search-Space Reduction for Boolean MinCSPs via Essential Constraints](https://doi.org/10.4230/LIPIcs.SWAT.2026.22)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-3678 — Polynomial-time tractability testing for core crisp CSP languages

A crisp constraint language lists the allowed tuples over a finite domain, and the input is promised to be a core. The question asks for a polynomial-time test for an idempotent four-ary Siggers polymorphism. Both the domain and every relation are part of the input, so one uniform polynomial bound is required. The known finite-valued test and unrestricted-language NP-hardness do not answer this promised-core question. An ICALP 2026 article explicitly retains the relevant Siggers testing problem as open.

[Read in atlas](index.html#TCS-3678) · [Testing the Complexity of a Valued CSP Language](https://doi.org/10.4230/LIPIcs.ICALP.2019.77) · [Testing the complexity of a valued CSP language](https://arxiv.org/abs/1803.02289) · [The Complexity of Finding Coset-Generating Polymorphisms and the Promise Metaproblem](https://doi.org/10.4230/LIPIcs.ICALP.2026.169)
Existing status: `open` · Summary written: 2026-09-12

### TCS-7124 — SNP definability of CSPs in NP

The historical source asks which NP constraint satisfaction problems have an exact SNP definition. SNP guesses fixed-arity relations on the input and checks a fixed universal first-order condition. Known results translate such CSPs exactly into reducts of structures with finitely many forbidden induced patterns. The checked sources do not identify that reformulation as resolving the intended broader classification direction. The card remains pending until a substantive criterion beyond the known equivalence is specified.

[Read in atlas](index.html#TCS-7124) · [Constraint Satisfaction Problems with Infinite Templates](https://www.lix.polytechnique.fr/~bodirsky/publications/csp-survey.pdf) · [Complexity of Infinite-Domain Constraint Satisfaction](https://wwwpub.zih.tu-dresden.de/~bodirsky/Book.pdf) · [On the Computational Power of Extensional ESO](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.20)
Existing status: `uncertain` · Summary written: 2026-09-16

## Automated reasoning, rewriting and unification (14)

### TCS-6562 — Word equations with linear length constraints

Word equations require substitutions of finite strings that make all supplied concatenations identical. Here the same substitution must also satisfy a conjunction of integer linear constraints on total string lengths. The target is one always-terminating decision algorithm for arbitrary finite inputs, including empty substitutions and unrestricted variable occurrences. Known restricted decision results and partial termination criteria do not settle this combination, and stronger letter-count predicates describe a different problem. A resolution would establish whether complete exact solving is possible for this basic fragment of string constraints, before imposing efficiency requirements.

[Read in atlas](index.html#TCS-6562) · [Word equations, constraints, and formal languages](https://arxiv.org/abs/2406.02160v1) · [Word Equations with Length Constraints via Weak Arithmetics and Matrix Reachability Problems](https://link.springer.com/chapter/10.1007/978-3-032-09524-4_4) · [The Termination of Nielsen Transformations Applied to Word Equations with Length Constraints](https://link.springer.com/chapter/10.1007/978-3-032-32592-1_14) · [NEXP-Completeness and Exponential Coefficient Growth for Existential Presburger Arithmetic with Divisibility](https://arxiv.org/abs/2606.14167v3) · [The termination of Nielsen transformations applied to word equations with length constraints — full preprint](https://arxiv.org/abs/2501.11789v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6643 — Decidability of unification in the basic modal logic K

Basic modal logic K interprets formulas on arbitrary accessibility relations between possible worlds. The problem asks whether it is decidable that a finite formula has a substitution instance valid at every world of every such model. Substitutions act simultaneously on all input variables, may introduce new variables, and leave no designated parameters fixed. Frames may be finite or infinite, and no reflexivity or transitivity condition is imposed. The requested algorithm must halt on every input; its time and the size of a possible substitution have no prescribed bounds.

[Read in atlas](index.html#TCS-6643) · [On the unification problem for GLP](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=9592&wshow=paper)
Existing status: `open` · Summary written: 2026-09-11

### TCS-1992 — Decidability of Presburger arithmetic with primes

Presburger arithmetic describes the standard integers using addition and order and has a decidable first-order theory. This question adds a predicate for positive primes and asks for one algorithm deciding every sentence, with arbitrary quantifier alternation. The resulting language can express prime-pattern claims such as twin primes and Goldbach’s conjecture. A classical undecidability result is conditional on a prime-tuples conjecture, while a conditional decidability theorem concerns a different unordered structure. An unconditional resolution would locate a major boundary between effective additive arithmetic and quantified number-theoretic reasoning.

[Read in atlas](index.html#TCS-1992) · [An Introduction to the Theory of Linear Integer Arithmetic (Invited Paper)](https://doi.org/10.4230/LIPIcs.FSTTCS.2024.1) · [Decidability and undecidability of theories with a predicate for the primes](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/decidability-and-undecidability-of-theories-with-a-predicate-for-the-primes/58C09C04699689A1CFA6FB750600F298) · [Decidability and classification of the theory of integers with primes](https://shelah.logic.at/papers/1082/) · [Decidability and classification of the theory of integers with primes — author manuscript](https://arxiv.org/abs/1601.07099v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6650 — Deterministic polynomial-time equivalence testing for d-DNNFs

The problem asks whether two explicit d-DNNF circuits can be tested for exact Boolean equivalence in deterministic polynomial time. Decomposability requires disjoint variable sets at conjunctions, while determinism requires mutually exclusive inputs at disjunctions. The circuits may use unrelated internal decompositions and need not share a variable tree. Randomized polynomial-time equivalence testing is known, but its possibility of error does not satisfy this target. A resolution would clarify the cost of comparing and verifying succinct compiled Boolean representations.

[Read in atlas](index.html#TCS-6650) · [Proof Systems Based on Structured Circuits](https://arxiv.org/abs/2605.12378) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Testing Equivalence Probabilistically](https://users.cecs.anu.edu.au/~jinbo/02-d123.pdf)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-7239 — Greedy CDCL without restarts versus resolution

A resolution refutation derives the empty clause by repeatedly combining clauses on opposite literals. This card asks whether any such supplied proof can be translated in deterministic polynomial time into a greedy clause-learning search on the same formula without restarts. The legal search must process conflicts and unit clauses immediately and may backjump only as justified by a learned asserting clause. Known simulations with relaxed propagation or preprocessing, and newer generalized backtracking results, do not establish this exact claim. A resolution would show whether restarts change the polynomial proof-generating power of idealized greedy SAT search.

[Read in atlas](index.html#TCS-7239) · [Space in Proof Complexity](https://jakobnordstrom.se/docs/publications/MV_PhDthesis.pdf) · [CDCL vs Resolution](https://simons.berkeley.edu/sites/default/files/docs/21462/satreunionslides-marcvinyals.pdf) · [A Simple Supercritical Tradeoff between Size and Height in Resolution](https://eccc.weizmann.ac.il/report/2024/001/) · [Generalizing CDCL with Graph Backtracking](https://doi.org/10.4230/LIPIcs.SAT.2026.14)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6644 — Decidability of termination for one-rule string rewriting

A one-rule string system repeatedly replaces one fixed substring by another. The question is whether an algorithm can decide if every reduction sequence from every finite starting word eventually stops. Replacement positions are unrestricted, and the rule and alphabet are part of the input. Known decision procedures cover special rule families, while an August 2026 note still lists the arbitrary one-rule question as open. The answer must prove decidability or undecidability in Lean for global termination, rather than only termination from one supplied word.

[Read in atlas](index.html#TCS-6644) · [Decidability of Termination of Grid String Rewriting Rules](https://doi.org/10.1137/S009753979833297X) · [RTA Open Problem 21: Termination of one linear rule](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/21.html) · [String Rewriting Systems: Brief Introduction and Sample of Open Problems](https://arxiv.org/abs/2608.19397)
Existing status: `source_open` · Summary written: 2026-09-13

### TCS-7194 — Singly exponential shortest solutions of word equations

A word equation asks for consistent substitutions of finite strings that make two concatenations identical. The conjecture says that every satisfiable equation of size n has some solution whose variable images have length at most two to a fixed polynomial in n. The bound must hold uniformly over all finite alphabets and arbitrarily many variable occurrences, with empty substitutions allowed. Known compression results make this length conjecture sufficient for NP membership of general word-equation satisfiability. Doubly exponential bounds and newer results for restricted equation families do not meet the universal single-exponential target.

[Read in atlas](index.html#TCS-7194) · [Application of Lempel-Ziv Encodings to the Solution of Word Equations](https://ii.uni.wroc.pl/~aje/WordEq2015/papers/PlandowskiRytter.pdf) · [Recompression: a simple and powerful technique for word equations](https://arxiv.org/abs/1203.3705) · [An Improved Version of Hmelevskii’s Theorem on Three-Variable Word Equations](https://doi.org/10.4230/LIPIcs.STACS.2026.77)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0163 — NP membership of word-equation satisfiability

A word equation asks whether replacing each variable by a finite word can make its two sides identical. The selected target is whether satisfiability of unrestricted plain word equations belongs to NP. A positive answer needs polynomial-size certificates and one polynomial-time verifier, without prescribing how a solution is represented. The problem is NP-hard and has a nondeterministic linear-space algorithm, while a 2026 source still lists NP membership as open. The overlapping word-unification card is merged here, with its original record retained in the archive.

[Read in atlas](index.html#TCS-0163) · [Antoine Amarilli: research questions](https://a3nm.net/work/research/questions/#complexity-of-word-equation-satisfiability) · [Hardness Results for Constant-Free Pattern Languages and Word Equations](https://doi.org/10.4230/LIPIcs.ICALP.2020.140) · [An Improved Version of Hmelevskii’s Theorem on Three-Variable Word Equations](https://doi.org/10.4230/LIPIcs.STACS.2026.77) · [Solving Word Equations (And Other Unification Problems) by Recompression (Invited Talk)](https://doi.org/10.4230/LIPIcs.CSL.2020.3) · [RTA Open Problem 92: Complexity of word unification](https://www.cs.tau.ac.il/~nachum/rtaloop/problems/92.html) · [Word Equations in Nondeterministic Linear Space](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2017.95) · [Algebraic Circuits Over Sum and Shift and Existential Presburger Arithmetic with Divisibility](https://arxiv.org/abs/2606.14167v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-1595 — Decidability of fifth-order \(\beta\)-matching

Beta-matching asks whether a supplied simply typed lambda function maps some closed term to a fixed target up to beta conversion. This card bounds the unknown term’s type at order five, counting the ground type as order one. It asks for a total decision procedure over all finite inputs in this class. The August 2026 source retains this case between a reported decidable order-four case and mechanized undecidability at order six, while beta-eta matching is a different decidable problem. A resolution would locate the exact fixed-order boundary for beta-only higher-order matching.

[Read in atlas](index.html#TCS-1595) · [Mechanized Undecidability of Higher-Order Beta-Matching](https://doi.org/10.4230/LIPIcs.FSCD.2025.17) · [Mechanized Undecidability of Higher-order beta-Matching (Extended Version)](https://arxiv.org/abs/2602.02091v2) · [Decidability of higher-order matching](https://arxiv.org/abs/0907.3804)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7134 — Polynomial-time equivalence of free binary decision diagrams

A free binary decision diagram tests each Boolean variable at most once along a path while allowing the order to vary between paths. The question asks whether one deterministic algorithm can decide equivalence of any two such diagrams in polynomial time in their explicit encodings. Equivalence requires agreement on every assignment, even when the diagrams use unrelated variable orders. A one-sided randomized polynomial-time test is known, while hardness for more demanding diagram operations does not settle this exact comparison task. A deterministic resolution would clarify how much compact representation can be retained while supporting reliable exact comparison of Boolean functions.

[Read in atlas](index.html#TCS-7134) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Testing Equivalence Probabilistically](https://users.cecs.anu.edu.au/~jinbo/02-d123.pdf) · [Proof Systems Based on Structured Circuits](https://arxiv.org/abs/2605.12378v2)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-7125 — Two-sided distributive unification with a unit

Unification asks whether a common substitution can make every pair of supplied expressions equal under specified algebraic identities. Here the identities are both distributive laws together with a two-sided multiplicative unit. The expressions may also use uninterpreted symbols, and neither operation is assumed associative or commutative. Known algorithms handle neighboring fragments, while undecidability results with additional associativity do not settle this exact theory. A resolution would identify a longstanding boundary for symbolic equality reasoning under interacting algebraic laws.

[Read in atlas](index.html#TCS-7125) · [Unification Theory](https://www.cs.bu.edu/fac/snyder/publications/UnifChapter.pdf) · [An algorithm for distributive unification](https://link.springer.com/chapter/10.1007/3-540-61464-8_60) · [Decidability of Unification in the Theory of One-Sided Distributivity and a Multiplicative Unit](https://doi.org/10.1006/jsco.1996.0054) · [Unification problems with one-sided distributivity](https://doi.org/10.1016/S0747-7171(87)80026-3) · [On the Complexity of the Tiden-Arnborg Algorithm for Unification modulo One-Sided Distributivity](https://arxiv.org/abs/1012.4894)
Existing status: `uncertain` · Summary written: 2026-09-16

### TCS-0114 — Decidability of subsequence constraints with regular domains

Each variable denotes one finite word constrained to a specified regular language. A relational constraint requires that word to occur as a scattered subsequence of a concatenation of other assigned words. The question asks for total decidability over every fixed finite alphabet, allowing repeated variables and arbitrary dependency cycles. Known algorithms for acyclic systems and undecidability results with shuffle or transducers concern different input classes. A resolution would locate the decidability boundary of a basic language for relating incomplete and concatenated strings.

[Read in atlas](index.html#TCS-0114) · [Automata Exchange](https://automata.exchange/24.13-satisfiability-of-string-constraints-with-subsequence-relation/) · [Satisfiability of Context-Free String Constraints with Subword-Ordering and Transducers](https://drops.dagstuhl.de/storage/00lipics/lipics-vol289-stacs2024/LIPIcs.STACS.2024.5/LIPIcs.STACS.2024.5.pdf)
Existing status: `source_open` · Summary written: 2026-09-15

### TCS-0306 — Polynomial-time complementation of d-DNNFs

The problem asks for a uniform deterministic polynomial-time algorithm that complements any given d-DNNF circuit. Its output must remain decomposable and deterministic and agree with the Boolean complement on every assignment. The time bound includes constructing and writing a complete circuit over the original variables. A polynomial-size complement may conceivably exist without a known efficient construction, so that separate existence question is not the whole target. Known lower bounds for structured representations leave this general circuit operation unresolved.

[Read in atlas](index.html#TCS-0306) · [List of open questions: PTIME complementation of d-DNNF](https://a3nm.net/work/research/questions/#ptime-complementation-of-d-dnnf) · [A Knowledge Compilation Map](https://arxiv.org/abs/1106.1819) · [Structured d-DNNF Is Not Closed under Negation](https://doi.org/10.24963/ijcai.2024/398) · [On the Complexity of Language Membership for Probabilistic Words](https://doi.org/10.4230/LIPIcs.STACS.2026.5)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-5603 — Polynomial-time recognition of abelian cores

The input is an entire finite algebra specified by tables of its basic operations. It is promised to possess an idempotent Taylor term, although no witness is supplied. The task is to decide whether its smallest endomorphic image is abelian in the universal-algebraic sense. A quasipolynomial-time recognition algorithm is known. This is a classification problem for algebras, distinct from solving a particular list of term equations.

[Read in atlas](index.html#TCS-5603) · [On the Complexity Dichotomy for the Satisfiability of Systems of Term Equations over Finite Algebras](https://doi.org/10.4230/LIPIcs.MFCS.2023.66) · [Equations over finite algebras](https://www.algebra.uni-linz.ac.at/Slides/sl-aaa105-6.pdf)
Existing status: `open` · Summary written: 2026-09-12

## Database theory and finite model theory (21)

### TCS-6678 — FO model checking on hereditary monadically dependent graph classes

First-order model checking evaluates a vertex-quantified logical sentence on an explicitly given finite graph. The question asks for a uniform deterministic algorithm on each hereditary effectively monadically dependent class, with computable parameter dependence and a sentence-independent graph-size exponent. Effective monadic dependence bounds the powerset graphs obtainable through short formulas with arbitrary unary vertex markings. The algorithm receives no graph decomposition or class-membership certificate, and must work for all sentences on its fixed class. Hereditary independent classes have a hardness theorem and effectively stable classes have algorithms, while the July 2026 radius-one results leave the full positive direction open.

[Read in atlas](index.html#TCS-6678) · [Graph classes through the lens of logic](https://arxiv.org/abs/2501.04166) · [Monadically Stable and Monadically Dependent Graph Classes: Characterizations and Algorithmic Meta-Theorems](https://media-api.suub.uni-bremen.de/api/core/bitstreams/64278fff-a8bb-43a8-aa91-32469c6394ac/content) · [Flip-Breakability: A Combinatorial Dichotomy for Monadically Dependent Graph Classes](https://arxiv.org/abs/2403.15201v2) · [First-Order Model Checking on Monadically Stable Graph Classes](https://arxiv.org/abs/2311.18740) · [Merge-width and First-Order Model Checking](https://arxiv.org/abs/2502.18065v2) · [Near-Linear Time Computation of Welzl Orders on Graphs with Linear Neighborhood Complexity](https://arxiv.org/abs/2602.14625) · [Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes](https://arxiv.org/abs/2607.10941)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6645 — Constant-delay conjunctive-query classification

The input to the proposed classifier is any finite conjunctive query, allowing repeated relation symbols and existentially hidden variables. It must decide whether the query has a deterministic enumerator with linear preprocessing and constant worst-case delay on every database. Answers use set semantics, are printed without repetition, and the delay includes the first answer and final termination. The specified RAM permits polynomial address space without a separate linear-memory restriction, and all enumeration constants may depend on the fixed query. A complete Lean-checked answer must establish a total classifier or prove that none exists; partial or conditional classifications do not finish the target.

[Read in atlas](index.html#TCS-6645) · [Conjunctive Queries With Self-Joins, Towards a Fine-Grained Enumeration Complexity Analysis](https://www.di.ens.fr/~segoufin/Papers/Mypapers/enum-cq-selfjoin.pdf) · [Enumerating answers of acyclic conjunctive queries with self-joins (Report)](https://www.normalesup.org/~rouvroy/papers/Report_M1S1.pdf) · [Research page: Constant-Delay Enumeration of Conjunctive Queries with Self-Joins and Projections](https://www.normalesup.org/~rouvroy/research/index.html)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7195 — A logic capturing polynomial time

Is there an effective logic for all polynomial-time properties of finite unordered structures? Its sentences must describe properties unchanged by renaming domain elements. Each sentence must compile effectively to an evaluation algorithm with a polynomial time bound. Fixed-point logic captures polynomial time when an order is supplied, but that is a different input model. Current candidate and restricted-class results leave the general existence question open.

[Read in atlas](index.html#TCS-7195) · [The Quest for a Logic Capturing PTIME: LICS 2008 invited paper](https://lics.siglog.org/2008/Grohe-TheQuestforaLogicCa.html) · [Is Polynomial Time Choiceless?](https://logic.rwth-aachen.de/pub/graedel/cptYuri.pdf) · [The quest for a logic for Ptime](https://www.cl.cam.ac.uk/~btp26/esslli/lecture1.pdf) · [Choiceless Polynomial Time with Witnessed Symmetric Choice](https://arxiv.org/abs/2205.14003v3) · [Subgroup Accessibility in Group Order Logic](https://arxiv.org/abs/2609.00499)
Existing status: `open` · Summary written: 2026-09-11

### TCS-7232 — Asser’s problem

The spectrum of a first-order sentence is the set of positive sizes of its finite models. Asser’s problem asks whether the complement of every such set is again a first-order spectrum. The representing sentence may use a new vocabulary and must work at all sizes simultaneously, with no effective construction required. The general question is equivalent to closure of nondeterministic single-exponential time under complement for binary-encoded sizes. Two-variable counting spectra are understood, while reductions to three-variable graph inputs and later restricted-logic results leave the general question open.

[Read in atlas](index.html#TCS-7232) · [Fifty Years of the Spectrum Problem: Survey and New Results](https://arxiv.org/abs/0907.5495) · [Regular Graphs and the Spectra of Two-Variable Logic with Counting](https://arxiv.org/abs/1304.0829) · [On the Variable Hierarchy of First-Order Spectra](https://arxiv.org/abs/1403.2225) · [A Note on First-Order Spectra with Binary Relations](https://lmcs.episciences.org/3751) · [Two Variable Logic with Ultimately Periodic Counting](https://arxiv.org/abs/2006.01193)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-6680 — Decidability of conjunctive-query entailment in SROIQ

A SROIQ knowledge base describes incomplete information using concepts, individuals, relations, inverse relations, counting and restricted role chains. A Boolean conjunctive query asks whether one finite relational pattern must occur in every model, including infinite models and witnesses that have no individual name. The question is whether one ordinary algorithm can always decide that entailment for the complete specified language, with no running-time bound. A complete Lean proof must establish a sound, complete and universally terminating decision procedure or prove that no such procedure exists. The checked finite-model undecidability, simple-role and Horn decision procedures, practical reasoner and2026 S-fragment theorem do not settle this all-model SROIQ target.

[Read in atlas](index.html#TCS-6680) · [Absorption-Based Query Entailment Checking for Expressive Description Logics](https://ceur-ws.org/Vol-2373/paper-25.pdf) · [The Even More Irresistible SROIQ](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf) · [Nominals, Inverses, Counting, and Conjunctive Queries or: Why Infinity is your Friend!](https://www.cs.ox.ac.uk/files/2175/paper.pdf) · [Query Answering in the Horn Fragments of the Description Logics SHOIQ and SROIQ](https://www.ijcai.org/Proceedings/11/Papers/178.pdf) · [The Curse of Finiteness: Undecidability of Database-Inspired Reasoning Problems in Very Expressive Description Logics](https://ceur-ws.org/Vol-1577/paper_12.pdf) · [Revisiting Conjunctive Query Entailment for S](https://arxiv.org/abs/2511.07933)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0492 — Conjunctive-query containment under bag semantics

A conjunctive database query produces answer multiplicities by summing products of input multiplicities. Containment means that the first query never produces more copies of any answer than the second on any finite bag database. The question asks whether one total algorithm can decide this property from the two unrestricted queries alone. Restricted joins are decidable and nearby extensions are undecidable, while new equivalence results do not settle this one-sided comparison. A complete Lean-checked answer must prove a terminating exact decision procedure or unconditional undecidability.

[Read in atlas](index.html#TCS-0492) · [List of open questions: Decidability of conjunctive query containment under bag semantics](https://a3nm.net/work/research/questions/#decidability-of-conjunctive-query-containment-under-bag-semantics) · [Semirings in Databases, Automata, and Logic (Dagstuhl Seminar 25081)](https://doi.org/10.4230/DagRep.15.2.89) · [Bag Semantics Conjunctive Query Containment. Four Small Steps Towards Undecidability](https://doi.org/10.1145/3651604) · [Bag Containment of Join-On-Free Queries](https://doi.org/10.4230/LIPIcs.ICDT.2025.5) · [Bag Semantics Query Containment: The CQ vs. UCQ Case and Other Stories](https://arxiv.org/abs/2503.07219v3) · [Time to Move on: Querying without Nulls and Bags](https://arxiv.org/abs/2608.10863) · [Few Rows Tell Them Apart: Equivalence of Queries Mixing Set and Bag Semantics](https://arxiv.org/abs/2609.09978v1)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-3631 — A logic capturing logarithmic space

The input is a finite relational structure with no distinguished ordering of its elements. The question asks for an effective logic expressing exactly all isomorphism-invariant Boolean queries decidable in deterministic logarithmic space. Each sentence must compile to a halting evaluation algorithm with a certified logarithmic workspace bound. The proposed CLogspace logic is known to miss some such queries, while ordered structures and strings admit stronger capturing results. A solution would settle a broad descriptive-complexity question linking small-memory computation to the expressive power of logical queries.

[Read in atlas](index.html#TCS-3631) · [Choiceless Logarithmic Space](https://doi.org/10.4230/LIPIcs.MFCS.2019.31) · [Is Polynomial Time Choiceless?](https://logic.rwth-aachen.de/pub/graedel/cptYuri.pdf) · [FC-Datalog as a Framework for Efficient String Querying](https://arxiv.org/abs/2501.10344v2)
Existing status: `source_open` · Summary written: 2026-09-14

### TCS-0488 — Computability of entropic query-size bounds

Entropy bounds limit the number of tuples returned by a database join from constraints on conditional degrees. The entropic bound optimizes total entropy over the closure of all finite discrete entropy vectors. The question asks for one terminating algorithm that computes this value to every requested absolute accuracy in arbitrary dimension. Simple constraints admit effective special cases, while the general polymatroid relaxation can overestimate the desired value. Resolving computability would determine whether the strongest information-theoretic estimate is accessible to algorithms at all.

[Read in atlas](index.html#TCS-0488) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Applications of Information Inequalities to Database Theory Problems](https://arxiv.org/abs/2304.11996v4) · [Efficient Algorithms for Cardinality Estimation and Conjunctive Query Evaluation With Simple Degree Constraints](https://arxiv.org/abs/2504.02770v1) · [Size Bounds for CQs Under Acyclic Constraints](https://arxiv.org/abs/2608.26775v1)
Existing status: `source_open` · Summary written: 2026-09-16

### TCS-0482 — Linear-round convergence over stable semirings

The system consists of finitely many polynomial recurrences over a commutative semiring. Every round updates all coordinates from the previous vector, starting from zero. The question asks whether p-stability forces a fixed point within a universal constant times (p+1)n rounds. An announced optimal-convergence paper makes the current status uncertain because its precise theorem was not available in the inspected sources. The requested answer remains a complete Lean-checked universal convergence proof or refutation for the specified synchronous rule.

[Read in atlas](index.html#TCS-0482) · [Semirings in Databases, Automata, and Logic — Convergence rate of Datalogo over p-stable semirings](https://doi.org/10.4230/DagRep.15.2.89) · [Polynomial Time Convergence of the Iterative Evaluation of Datalogo Programs](https://arxiv.org/abs/2312.14063v2) · [Publication listing: Optimal Convergence of Iterative Methods for Datalogo](https://hung-q-ngo.github.io/publications.html) · [Publications by topic: Optimal Convergence of Iterative Methods for Datalogo](https://www.andrew.cmu.edu/user/moseleyb/bytopic.html)
Existing status: `uncertain` · Summary written: 2026-09-17

### TCS-0487 — Complexity of polymatroid query-size bounds

Polymatroid query bounds maximize a normalized monotone submodular function subject to supplied degree constraints. The obvious linear program has exponentially many coordinates even when its input constraint list is short. The source explicitly asks whether computing this general bound is NP-hard, formalized here through exact rational threshold comparisons. Simple constraints admit polynomial-time algorithms, while hardness for the smaller cone of normal functions leaves the general question unresolved. An answer would clarify whether this broad database estimation framework can be computed efficiently from compact dependency descriptions.

[Read in atlas](index.html#TCS-0487) · [Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)](https://doi.org/10.4230/DagRep.12.7.180) · [Optimizing Polymatroid Functions](https://arxiv.org/abs/2211.08381v1) · [Efficient Algorithms for Cardinality Estimation and Conjunctive Query Evaluation With Simple Degree Constraints](https://arxiv.org/abs/2504.02770v1)
Existing status: `source_open` · Summary written: 2026-09-16

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

Fix a Boolean query that remains true whenever its input database maps homomorphically to another database. Uniform reliability counts exactly how many subsets of an input database's facts satisfy that fixed query. Equivalently, each fact is retained independently with probability one half, and the resulting probability is rescaled to an integer count. The conjectured boundary is a finite union of conjunctive queries with tractable weighted evaluation; every other query should yield a #P-hard counting problem. Known results cover several query classes, including all unbounded queries of maximum arity two, while the full arbitrary-arity dichotomy remains unverified by this bounded review.

[Read in atlas](index.html#TCS-0505) · [List of open questions: Complexity of uniform reliability for homomorphism-closed queries](https://a3nm.net/work/research/questions/#complexity-of-uniform-reliability-for-homomorphism-closed-queries) · [Uniform Reliability for Unbounded Homomorphism-Closed Graph Queries](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2023.14) · [The Dichotomy of Probabilistic Inference for Unions of Conjunctive Queries](https://homes.cs.washington.edu/~suciu/jacm-dichotomy.pdf) · [Uniform Reliability of Self-Join-Free Conjunctive Queries](https://lmcs.episciences.org/10288/pdf) · [When is Shapley Value Computation a Matter of Counting?](https://www.labri.fr/perso/meghyn/papers/BieFigLaf-PODS24.pdf) · [Approximating Queries on Probabilistic Graphs](https://arxiv.org/abs/2309.13287v8)
Existing status: `source_open` · Summary written: 2026-09-16

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

## Miscellaneous (3)

### TCS-7177 — \(1/3\)–\(2/3\) conjecture

A partial order records known comparisons, and its linear extensions are all compatible complete rankings. The conjecture asks whether every finite non-total order has an incomparable pair that appears in either relative order in at least one third of all extensions. The extensions are weighted uniformly, and both endpoints of the interval are allowed. A three-element order with only one comparison shows that the constant one third cannot be improved universally. A resolution would identify the sharp balance guarantee for a comparison in sorting with partial information.

[Read in atlas](index.html#TCS-7177) · [Balancing pairs and the cross product conjecture](https://trotter.math.gatech.edu/papers/97.pdf) · [Linear extensions of finite posets](https://arxiv.org/abs/2311.02743) · [Balancing Extensions in Posets of Large Width](https://arxiv.org/abs/2509.11549) · [Balance Constants, Majority Cycles, and the Gold Partition Conjecture through Fourteen Elements](https://arxiv.org/abs/2607.23926v2)
Existing status: `source_open` · Summary written: 2026-09-11

### TCS-6654 — Seese’s conjecture

Seese’s conjecture concerns arbitrary classes of finite simple undirected graphs. Its premise is an algorithm deciding whether some graph in the class satisfies any input monadic second-order sentence over vertices and vertex sets. Its conclusion is one finite clique-width bound holding for all graphs in that class. The algorithm and bound may depend on the class, and parity predicates or edge-set quantifiers are excluded from the premise. A complete Lean-checked solution must prove the universal implication or verify a class with decidable satisfiability and unbounded clique-width.

[Read in atlas](index.html#TCS-6654) · [Forbidden Induced Subgraphs for Bounded Shrub-Depth and the Expressive Power of MSO](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.167) · [Vertex-minors, monadic second-order logic, and a conjecture by Seese](https://www.labri.fr/perso/courcell/Textes1/BC-Oum%282007%29.pdf) · [MSO undecidability for hereditary classes of unbounded clique-width](https://doi.org/10.1016/j.ejc.2023.103700) · [Hereditary 2-WQO Graph Classes Have Bounded Clique-Width](https://arxiv.org/abs/2607.10939v2)
Existing status: `source_open` · Summary written: 2026-09-17

### TCS-7290 — Extremal size of sunflower-free set families

A sunflower is a collection of distinct sets with one common pairwise intersection. For fixed r, the target is the maximum size of a family of k-element sets containing no r-member sunflower. Determine its growth as k increases within constant factors that may depend on r. The ground set is any finite universe and the question imposes no algorithmic restrictions. The sunflower conjecture predicts at most exponential growth, a weaker claim than determining the full extremal order.

[Read in atlas](index.html#TCS-7290) · [Improved sunflower bounds](https://arxiv.org/abs/1908.08483)
Existing status: `source_open` · Summary written: 2026-09-12
