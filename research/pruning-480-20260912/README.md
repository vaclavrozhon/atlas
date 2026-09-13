# Applying the 500-card pruning proposal: retain 20, remove 480

The user authorized deletion of the previous 500 candidates except approximately twenty of the most important, allowing useful generalizations. This review retains exactly twenty and removes the other 480. Scientific significance was primary; category totals, age and old numerical scores did not determine the selection.

The scope is the exact ID set in [the previous proposal](../pruning-proposal-500-20260912/decisions.json). The earlier rescues outside that set were not reconsidered for deletion. The full original review was reused, the strongest candidates were compared again, and all twenty retained formulations were read in full. Nine proposal cards revised concurrently since the original review were reread: TCS-3928, TCS-3945, TCS-3959, TCS-4003, TCS-4009, TCS-4031, TCS-4039, TCS-4061 and TCS-4076. TCS-4061 was reread again after its surface convention changed.

The final comparison favored TCS-3959, the general algebraic-closure decision problem, over TCS-3514, whose learning/natural-property equivalence additionally depends on the Universality Conjecture. TCS-3514 remains scientifically interesting but did not enter this small rescue set. Neither choice used a category quota.

## Formulation decisions

- TCS-0250 now asks for arbitrary fixed positive scaling of all joint Kolmogorov complexities. Its original half-scaling question and logarithmic length normalization remain explicit; the 2025 obstruction for conditioning on one string is a different statement.
- TCS-1882 and TCS-2336 ask for the full optimal query and regret functions, with uniform multiplicative-constant precision over the stated parameter domains.
- TCS-5021 asks for the limiting optimized QAOA energy to absolute error 0.01. Instance size tends to infinity before angles are optimized and depth grows. Its exact Parisi-value conjecture is retained as context.
- TCS-5030 asks for the optimal randomized weighted-k-server competitive ratio. The SODA 2026 exp(O(k²)) upper bound supersedes the old qualitative doubly-exponential barrier. TCS-5514 was merged into this surviving question.
- TCS-5395 fixes downward self-reduction to strictly shorter binary inputs, deterministic uniform computation and complete prime-power output.
- TCS-6168 isolates ordinary polynomial-time many-one NP-hardness of MCSP implying EXP⊄P/poly, distinguishing the weaker known consequences.
- TCS-6705 retains the exact universal Fourier-weight inequality. A general approximation algorithm for its extremal constant is already known, so replacing it with numerical estimation would discard the genuinely unresolved sharp target. The August 2026 lower-bound claim is labeled as a preprint claim.
- TCS-6783, item 468 in the previous chat list, asks for the optimal +4 additive-spanner size s₄(n). This is the classical constant-error exponent gap. The more general variable-error question for linear-size spanners already has a surviving representative, TCS-6785. Weighted, fault-tolerant and emulator models are not bundled into this question.
- TCS-7269 asks for log₂ of the minimum multilinear permanent formula size up to constant factors, retaining the original exponential endpoint and its unrestricted cancellation convention.
- The other ten retain their complete structural or complexity propositions. TCS-7253 remains marked uncertain because of unverified full-proof claims; later 2026 work still presents the general conjecture as open.

Asymptotic targets state their own multiplicative precision; numerical 0.01 tolerance is not imposed on big-O bounds. A reformulated determination task is not declared logically equivalent to a source conjecture.

## Retained questions

1. [TCS-0250: Scaling joint Kolmogorov-complexity profiles](../../data/cards/TCS-0250.json)
   - Target: For every fixed integer k≥1 and real λ>0, does there exist a constant c>0 such that, for every integer n≥2 and every tuple of binary strings a₁,…,a_k of length at most n, there are finite binary strings b₁,…,b_k satisfying |C(b_S)−λ C(a_S)|≤c log₂ n for every nonempty S⊆{1,…,k}? The same tuple b must satisfy all 2^k−1 inequalities simultaneously.
   - Significance: Scaling complete algorithmic-information profiles asks whether shared information has a universal homogeneous geometry, across arbitrary tuples rather than one example.

2. [TCS-1882: Optimal quantum query complexity of uniformity testing](../../data/cards/TCS-1882.json)
   - Target: Determine Q(d,ε), the optimal worst-case quantum query complexity of distinguishing p=u_d from d_TV(p,u_d)>ε with success probability at least 0.99, up to universal constant factors jointly for all integers d≥2 and real 0<ε≤1/4. Access is to an arbitrary distribution synthesizer with the precise oracle convention below.
   - Significance: Uniformity is a canonical statistical testing task; its full quantum query tradeoff measures a fundamental advantage of coherent sample access.

3. [TCS-2336: Optimal multiclass regret versus Littlestone dimension](../../data/cards/TCS-2336.json)
   - Target: Determine R(d,T)=sup{R_T(H): H is a nonempty multiclass hypothesis class with L(H)≤d}, up to universal constant factors, for integers T≥d≥1. The supremum ranges over arbitrary instance and label sets, including infinite label sets. R_T(H) is the full-label online minimax regret defined below; learners have no computational-efficiency restriction.
   - Significance: The minimax regret of every multiclass hypothesis family tests whether Littlestone dimension alone captures online prediction difficulty, even with infinitely many labels.

4. [TCS-2664: Removing low-influence directions from convex sets](../../data/cards/TCS-2664.json)
   - Target: Does there exist a function τ:(0,1)→[0,1] with lim_{ε→0⁺}τ(ε)=0 such that the following holds for every n≥1, every centrally symmetric convex Borel set K⊆ℝⁿ, every unit vector v and every ε∈(0,1)? If Inf_v[K]≤ε, then there exists a centrally symmetric convex Borel set C⊆v⊥ such that γₙ(K △ (C+ℝv))≤τ(ε). The same τ must work in all dimensions and for all such sets and directions.
   - Significance: Dimension-free stability of negligible Gaussian influence would give a general geometric meaning to an irrelevant direction in a convex set.

5. [TCS-3117: Memory–sample tradeoffs for noisy parity learning](../../data/cards/TCS-3117.json)
   - Target: Do there exist absolute constants c₁,c₂>0 and n₀ such that, for every integer n≥n₀, every 0<ε<1/2 and every one-pass learner recovering a uniformly random x∈{0,1}^n with probability at least 2/3 from the noisy parity samples defined below, its worst-case memory S and maximum sample count T satisfy S≥c₁n²/ε² or T≥2^{c₂n}? Constants are independent of n, ε and the learner, and ε may tend to zero with n. This states the bounded-error recovery interpretation of Conjecture 1; it does not additionally require a lower bound at exponentially small success probability.
   - Significance: The memory cost of noisy parity learning separates information retained from samples from computation time and exposes a basic resource cost of noise.

6. [TCS-3480: Polynomial exact metric sparsifiers with a crossing-edge budget](../../data/cards/TCS-3480.json)
   - Target: Do there exist absolute constants C,c>0 such that the following holds? For every finite simple undirected unweighted graph G=(V,E), terminal set T⊆V of size r, and integer p≥0, there is a set Z⊆E with |Z|≤C(1+p+r)^c having this universal property: for every finite nonempty label set D, every metric μ:D×D→R_{≥0}, and every terminal labeling τ:T→D, if there exists a labeling λ:V→D extending τ with at most p crossing edges, then some labeling λ* of minimum μ-cost among all such budget-feasible extensions has all its crossing edges in Z. The same Z must work simultaneously for every D,μ,τ and depends only on G,T,p. This is the polynomial-size version of the contraction-based metric-sparsifier property in the source’s Theorem 22; that theorem’s earlier quasipolynomial upper-bound claim was later retracted.
   - Significance: One small edge set preserving every metric-labeling query is a broad graph-compression principle, with substantially more content than a bound for one cut objective.

7. [TCS-3585: Exact exponential-time equivalence for nonnegative Boolean Max-CSP](../../data/cards/TCS-3585.json)
   - Target: Does the following extension of the source’s degree-based classification hold? For every fixed finite Boolean constraint language Γ that is neither 0-valid, 1-valid, nor 2-monotone, let d=deg(Γ). For every fixed real α>1, if Max CSP(Γ,N,c) has an exact deterministic algorithm running in αⁿn^{O(1)} time for every fixed constant c≥1, must Max d-CNF-SAT with nonnegative integer weights of total weight at most nᶜ also have an exact deterministic αⁿn^{O(1)}-time algorithm for every fixed c≥1? The same base α is required. Algorithms and polynomial factors may depend on Γ,α,c. This formulates the conclusion’s speedup question as extending Theorem 6.2 to all NP-hard nonnegative-weight languages; tractable languages are explicitly excluded.
   - Significance: A degree-based exact-time classification would organize all finite NP-hard Boolean Max-CSP languages with nonnegative weights under one invariant.

8. [TCS-3689: Non-clashing teaching dimension versus VC dimension](../../data/cards/TCS-3689.json)
   - Target: For every finite set X and every nonempty concept class C⊆2ˣ, is NCTD(C)≤VC(C)? Equivalently, if C has VC dimension d, does there exist a teaching map assigning at most d correctly labeled examples to each concept such that no two distinct concepts are mutually consistent with one another’s assigned examples? Both positive and negative examples are allowed. The target constant is exactly one, not merely a bound O(d).
   - Significance: The sharp universal relation between VC dimension and non-clashing teaching compares two basic notions of information needed to identify concepts.

9. [TCS-3787: Proper unlabeled compression of ample classes](../../data/cards/TCS-3787.json)
   - Target: Does every nonempty ample concept class C⊆{0,1}ᵁ on a finite domain U admit a proper unlabeled sample compression scheme of size at most d=VC(C)? Precisely, do there exist maps κ:RS(C)→{A⊆U:|A|≤d} and ρ:{A⊆U:|A|≤d}→C such that, for every realizable labeled partial sample s, κ(s)⊆dom(s) and ρ(κ(s)) agrees with every label in s? The stored object is only an unordered subset of the sample’s input points. The bound is d, not an unspecified multiple of d.
   - Significance: Optimal proper unlabeled compression of every ample class is a substantial structural case of the central sample-compression programme.

10. [TCS-3959: Approximate polynomial satisfiability in AM under GRH](../../data/cards/TCS-3959.json)
   - Target: Assuming the Generalized Riemann Hypothesis, is approximate polynomial satisfiability for rational-coefficient arithmetic circuits in AM? An instance consists of division-free circuits computing f₁,…,f_m∈ℚ[x₁,…,x_n]. It is a YES instance if, for every real η>0, there is a point a∈ℂⁿ with max_i |f_i(a)|<η; otherwise it is a NO instance. Equivalently, for every polynomial A∈ℚ[y₁,…,y_m], the identity A(f₁,…,f_m)=0 must imply A(0,…,0)=0. This equivalent decision predicate is AnnAtZero. Ask for one uniform public-coin protocol with verifier time, random-tape length and prover-message length polynomial in the full binary input length, with completeness at least 2/3 and soundness at most 1/3 on every instance.
   - Significance: The complexity of approaching a common polynomial zero is a basic question about algebraic closure and border computation; AM versus the known polynomial-space bound is a qualitative gap.

11. [TCS-5021: Limiting optimized QAOA energy in the SK model](../../data/cards/TCS-5021.json)
   - Target: Determine A=sup_{p≥1} sup_{γ,β∈ℝ^p} a_p(γ,β), where a_p(γ,β)=lim_{n→∞} n^{−1} E_J[⟨ψ_{p,J}(γ,β)|H_J|ψ_{p,J}(γ,β)⟩] for the Gaussian Sherrington–Kirkpatrick Hamiltonian and QAOA state defined below. The benchmark requires absolute error at most 1/100 in energy per spin.
   - Significance: The limiting optimized energy of QAOA asks whether a central quantum optimization ansatz can reach the statistical-mechanics optimum after taking the infinite-instance limit.

12. [TCS-5030: Optimal randomized competitive ratio of weighted k-server](../../data/cards/TCS-5030.json)
   - Target: Determine the asymptotic growth of R_w(k), the optimal randomized competitive ratio of the weighted k-server problem over all finite uniform metrics, up to universal multiplicative constants as the integer k tends to infinity. Use an oblivious request adversary and expected online cost, as defined below.
   - Significance: The optimal randomized cost of heterogeneous servers is a central online resource-allocation question; the recent singly-exponential breakthrough leaves a substantial quantitative frontier.

13. [TCS-5395: Downward self-reducibility of integer factoring](../../data/cards/TCS-5395.json)
   - Target: Is there one deterministic oracle Turing machine A and a polynomial p such that, for every integer N≥2 of binary length n, A outputs the complete prime factorization of N within p(n) steps, using a factoring oracle only on integers M≥2 whose binary length is strictly less than n?
   - Significance: Downward self-reducibility of integer factoring asks whether a canonical arithmetic search problem has the recursive structure common to complete problems.

14. [TCS-6168: Does NP-hardness of MCSP imply circuit lower bounds for EXP?](../../data/cards/TCS-6168.json)
   - Target: If the Minimum Circuit Size Problem is NP-hard under deterministic polynomial-time many-one reductions, must EXP⊄P/poly? The hypothesis uses unrestricted ordinary polynomial-time reductions, with no locality, uniform-AC⁰ or naturalness promise.
   - Significance: Whether ordinary NP-hardness of circuit minimization entails exponential-time circuit lower bounds is a central connection between metacomplexity and nonuniform lower bounds.

15. [TCS-6705: Sharp low-degree Fourier weight of halfspaces](../../data/cards/TCS-6705.json)
   - Target: For every integer n≥1 and every linear threshold function f:{−1,1}^n→{−1,1}, is W^{≤1}(f)=f̂(∅)²+Σ_{i=1}^n f̂({i})²≥2/π?
   - Significance: A sharp universal low-degree Fourier inequality for all halfspaces describes the spectral structure of a foundational Boolean function class.

16. [TCS-6783: Optimal size of four-additive graph spanners](../../data/cards/TCS-6783.json)
   - Target: Determine s₄(n)=max_G min_H |E(H)| up to universal multiplicative constants for integers n≥2, where G ranges over connected simple undirected unweighted graphs on n vertices and H ranges over their spanning subgraphs satisfying d_H(u,v)≤d_G(u,v)+4 for all vertices u,v.
   - Significance: The +4 additive-spanner regime is the classical remaining constant-error sparsity-exponent gap, making it a central distance-compression problem rather than a peripheral parameter choice.

17. [TCS-7170: Scholz–Brauer conjecture](../../data/cards/TCS-7170.json)
   - Target: For every positive integer n, is ℓ(2ⁿ−1)≤n−1+ℓ(n), where ℓ(m) is the minimum length of an addition chain for m?
   - Significance: The Scholz–Brauer conjecture is a longstanding universal law proposed for optimal addition chains, linking a basic arithmetic complexity measure across all exponents.

18. [TCS-7244: Boolean dimension of posets with planar cover graphs](../../data/cards/TCS-7244.json)
   - Target: Does there exist an integer d≥1 such that every finite poset P=(V,<) with a planar undirected cover graph admits strict total orders L_1,...,L_d on V and a Boolean function φ:{0,1}^d→{0,1} satisfying, for all distinct x,y∈V, x<y if and only if φ(1[x<_(L_1)y],...,1[x<_(L_d)y])=1?
   - Significance: A constant-size Boolean description of every order with a planar cover graph would explain how planar local structure controls global order information.

19. [TCS-7253: Seymour’s second-neighborhood conjecture](../../data/cards/TCS-7253.json)
   - Target: Does every finite nonempty oriented graph D contain a vertex v for which |N⁺⁺(v)|≥|N⁺(v)|, where N⁺(v) consists of vertices at directed distance one from v and N⁺⁺(v) consists of vertices at directed distance exactly two?
   - Significance: Seymour’s second-neighborhood conjecture is a classical universal expansion principle for arbitrary oriented graphs, with broad extremal significance.

20. [TCS-7269: Optimal multilinear-formula size of the permanent](../../data/cards/TCS-7269.json)
   - Target: Determine the growth of log₂ F(n) up to universal multiplicative constants as n→∞, where F(n) is the minimum size of a multilinear arithmetic formula over ℂ computing perm_n. Equivalently, find a positive function g(n) and constants a,A>0,n₀ such that 2^{a g(n)}≤F(n)≤2^{A g(n)} for every integer n≥n₀.
   - Significance: The optimal multilinear formula size of the permanent concerns a canonical explicit algebraic lower bound with a qualitative quasipolynomial-to-exponential gap.

## Application and audit

Canonical card edits, tombstones and removals were applied while holding `.publish.lock`, with optimistic hashes of all 520 scoped input cards checked before mutation. Exactly 480 card files were removed. All deleted IDs remain reserved. No focus selection pointed to a deleted ID. No other card was deleted. Twenty other surviving cards received transferred source references and scoped context; the deterministic no-recourse convention of TCS-5158 was made explicit to align its two source occurrences.

The active quality queue was reconciled, and 55 live review backups of deleted cards were removed. No new full-card deletion archive was created. Historical proposal reports remain historical evidence rather than active card definitions.

- [Twenty retained targets and reasons](retained.json)
- [480 removed IDs and reasons](deletions.json)
- [Source consolidation map](consolidations.json)
- [Source checks and status qualifications](source-checks.json)
- [Input hashes](input-hashes.json)
- [Application receipt](receipt.json)
- [Verification](verification.json)

`make publish` and `make check` passed for catalogue version `42943762f821df3fbda9`. The full check includes export parity and protection against resurrecting deleted IDs. The first run exposed null versus empty-string review metadata; that was corrected before the successful complete rerun.
