**Publication update — 10 September 2026:** The retained proposals below have now been added to the atlas as source-linked short drafts, following the user’s approval. The original research and novelty checks below describe the pre-publication stage. See [publication manifest](../import-fundamental-20260910/publication.json).

# Additional fundamental problems for the current small categories

Research date: **10 September 2026**. Scope: the **25 small categories in the current CATEGORY_PLAN.md**, not the earlier category list.

**72 new suggestions** survived this pass. **2 further strong problems are already in the large-category proposal** and are cross-referenced instead of counted twice. The request for **5–10 additions in every category was not met**. This is not a claim that no more qualifying problems exist; it records the limits of this research pass.

Entries are ordered within each category by editorial importance: foundational significance, breadth of consequences and centrality to the field. No routine follow-up was added to fill a numerical gap. Each entry supplies a concrete target, an importance rationale, primary sources and a novelty note. Statements below are proposal sketches, not completed self-contained benchmark cards.

Novelty was checked against all **6,513 catalogue records**, including source excerpts and differently classified entries, with full-source inspection for identified close matches. The final snapshot and limitations are recorded in [validation.json](validation.json); keyword hits are preserved in [final-novelty-audit.json](final-novelty-audit.json). Neither absence of a keyword nor a recent citation alone guarantees novelty or current open status.

## Coverage

| # | Current small category | New | Missing to reach 5 |
|---|---|---:|---:|
| 1 | Approximation algorithms and hardness of approximation | 5 | 0 |
| 2 | Parameterized and exact algorithms | 3 | 2 |
| 3 | Fine-grained complexity | 5 | 0 |
| 4 | Pseudorandomness and derandomization | 1 | 4 |
| 5 | Proof complexity | 2 | 3 |
| 6 | Communication complexity and Boolean function analysis | 3 | 2 |
| 7 | Coding and information theory | 5 | 0 |
| 8 | Algebraic computation | 6 | 0 |
| 9 | Lattices and computational number theory | 4 | 1 |
| 10 | Randomized algorithms and sampling | 2 | 3 |
| 11 | String algorithms and bioinformatics | 2 | 3 |
| 12 | Dynamic graph algorithms | 3 | 2 |
| 13 | Counting and enumeration | 2 | 3 |
| 14 | Property testing and distribution learning | 1 | 4 |
| 15 | Differential privacy | 1 | 4 |
| 16 | Algorithmic game theory, mechanism design and fair division | 3 | 2 |
| 17 | Constraint satisfaction | 3 | 2 |
| 18 | Scheduling and packing | 3 | 2 |
| 19 | Automated reasoning and unification | 4 | 1 |
| 20 | Database theory and finite model theory | 1 | 4 |
| 21 | Computability and algorithmic information | 4 | 1 |
| 22 | Knowledge representation and reasoning | 1 | 4 |
| 23 | Structural graph theory | 5 | 0 |
| 24 | Beyond worst-case and average-case analysis | 3 | 2 |
| 25 | Miscellaneous | 0 | 5 |

## 1. Approximation algorithms and hardness of approximation

**New suggestions: 5.**

**1. Constant-factor approximation for Densest k-Subgraph**

Does a polynomial-time algorithm always find k vertices inducing at least OPT/C edges, for one universal constant C? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.38).

**Why fundamental:** A central unresolved approximation barrier behind dense-subgraph optimization and many reductions.

**Novelty check:** TCS-1909 concerns ordinary densest subgraph in implicit geometric graphs, not the cardinality-constrained DkS problem.

**2. Polylogarithmic approximation for Directed Steiner Tree**

Is there a polynomial-time O(log^C k)-approximation, for some constant C, for connecting a root to k terminals in an arbitrary nonnegatively weighted directed graph? [Primary source 1](https://arxiv.org/abs/2412.10744).

**Why fundamental:** The defining gap in directed network-design approximation.

**Novelty check:** TCS-5442, TCS-5961 and TCS-5098 concern special graph classes or relaxations. Current v3 explicitly says the general problem remains unresolved; the earlier claimed solution was withdrawn.

**3. The 4/3 conjecture for the metric TSP subtour relaxation**

Is the supremum, over all finite symmetric metric TSP instances, of the optimal tour cost divided by the subtour-LP optimum exactly 4/3? [Primary source 1](https://arxiv.org/abs/2607.01536).

**Why fundamental:** A central conjecture about the principal relaxation of one of the canonical optimization problems.

**Novelty check:** The 4/3 keyword matches concern other optimization problems; no metric-TSP integrality-gap question was found.

**4. The factor-2 integrality-gap conjecture for the ATSP subtour LP**

For every directed metric, is the minimum Hamiltonian-tour cost at most twice the optimum of the standard subtour-elimination linear program? [Primary source 1](https://epubs.siam.org/doi/10.1137/20M1339313).

**Why fundamental:** Would identify the fundamental relaxation gap for asymmetric travelling salesman.

**Novelty check:** Distinct from the undirected 4/3 conjecture; these are the two classical TSP relaxation barriers.

**5. Constant-factor approximation for Directed Feedback Vertex Set**

Does a polynomial-time constant-factor approximation exist for minimum-weight directed feedback vertex set in arbitrary directed graphs? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.55).

**Why fundamental:** A defining approximation problem for directed cycle hitting.

**Novelty check:** TCS-6379 asks for a polynomial kernel, which is a different computational target; final search must also exclude another approximation record.

## 2. Parameterized and exact algorithms

**New suggestions: 3.**

**1. FPT versus W[1]**

Is there a computable f and a constant c such that k-Clique can be decided in f(k)n^c time? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73).

**Why fundamental:** The defining tractability-versus-intractability question of parameterized complexity.

**Novelty check:** Existing FPT/W[1] matches concern particular problems or deriving PIH from the class separation, not the separation itself.

**2. The Exponential Time Hypothesis**

Is there c>0 such that no deterministic algorithm solves all 3-CNF satisfiability instances with n variables and m clauses in 2^{cn}poly(n+m) time? [Primary source 1](https://epubs.siam.org/doi/10.1137/1.9781611977554.ch124).

**Why fundamental:** The principal hypothesis distinguishing polynomial, subexponential and genuinely exponential exact computation.

**Novelty check:** Existing ETH matches use it as an assumption for a different question. ETH is distinct from SETH, which concerns the limiting exponential base across clause widths.

**3. The Set Cover Conjecture**

For every epsilon>0, does some fixed d make it impossible to solve d-Set Cover on an n-element universe in (2-epsilon)^n poly(n) time? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.34).

**Why fundamental:** One of the few central exact-algorithm barriers not simply interchangeable with SAT hypotheses.

**Novelty check:** The formulation is for bounded set size, quantified after epsilon; it is not a parameterized approximation or an online geometric variant.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 3. Fine-grained complexity

**New suggestions: 5.**

**1. The Strong Exponential Time Hypothesis**

For every epsilon>0, is there a fixed k for which k-SAT has no deterministic (2-epsilon)^n poly(n+m)-time algorithm? [Primary source 1](https://epubs.siam.org/doi/10.1137/1.9781611977554.ch124).

**Why fundamental:** A central organizing hypothesis for tight running-time lower bounds throughout algorithms.

**Novelty check:** Existing entries ask about consequences, reductions, NSETH, or relations to other problems, not the main SETH statement.

**2. The Orthogonal Vectors Hypothesis**

Is it true that for every epsilon>0 there is a constant c such that no randomized bounded-error word-RAM algorithm decides whether two n-element sets in {0,1}^{c log n} contain an orthogonal pair in O(n^{2-epsilon}) time? [Primary source 1](https://arxiv.org/abs/1909.11068).

**Why fundamental:** One of the central foundations for conditional lower bounds for strings, geometry and data structures.

**Novelty check:** TCS-6094 concerns restricted computational models; the proposed target is unrestricted word-RAM complexity.

**3. The algebraic k-Clique Hypothesis**

Is the exponent omega*k/3 asymptotically optimal up to o(k) for deciding k-Clique on n-vertex graphs with unrestricted randomized algorithms? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2021.61).

**Why fundamental:** The principal algebraic fine-grained barrier for clique and many pattern problems.

**Novelty check:** TCS-5458 asks about k-Clique in memoryless communication. This proposal is about standard sequential computation; no informal 'combinatorial algorithm' restriction is used.

**4. The Min-Plus Convolution Hypothesis**

Is there an epsilon>0 and a randomized bounded-error algorithm computing the min-plus convolution of two length-n arrays of polynomially bounded integers in O(n^{2-epsilon}) time on a word RAM? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119).

**Why fundamental:** A central fine-grained hypothesis supporting quadratic barriers in knapsack and dynamic programming.

**Novelty check:** TCS-1522 concerns a particular knapsack application, not the general convolution barrier.

**5. The Hitting Set Conjecture**

Is it true that for every epsilon>0 there is c such that no randomized bounded-error word-RAM algorithm decides in O(n^{2-epsilon}) time whether some a in A intersects every b in B, given two n-element families A,B of subsets of [ceil(c log n)]? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2021.3).

**Why fundamental:** A standard hardness hypothesis behind fine-grained diameter and graph-distance barriers.

**Novelty check:** The existential-universal family problem, not the ordinary minimum hitting-set optimization problem.

## 4. Pseudorandomness and derandomization

**New suggestions: 1.**

**1. Optimal explicit pseudorandom generators for read-once branching programs**

Can one construct, in space O(log(nw/epsilon)), an epsilon-fooling pseudorandom generator for all length-n, width-w ordered read-once branching programs with seed length O(log(nw/epsilon))? [Primary source 1](https://eccc.weizmann.ac.il/report/2026/064/).

**Why fundamental:** The principal explicit pseudorandom-generator problem for space-bounded computation, going beyond merely deciding the same languages deterministically.

**Novelty check:** TCS-0026 is L versus BPL; TCS-1125 restricts to width four and only asks to beat log-squared seed length, while TCS-1132 restricts to regular programs. This is the full generator construction target.

**Selection limit:** P versus BPP, L versus BPL, general PIT, explicit Ramsey graphs, tree codes and prime construction already have catalogue records; their restatements are not new additions.

## 5. Proof complexity

**New suggestions: 2.**

**1. Superpolynomial Extended Frege lower bounds**

Does there exist a family of propositional tautologies whose shortest Extended Frege proofs are not bounded by any polynomial in their formula length? [Primary source 1](https://eccc.weizmann.ac.il/report/2026/098/).

**Why fundamental:** A defining barrier for lower bounds against strong propositional reasoning.

**Novelty check:** TCS-1100 is about what PV1 can prove concerning lower bounds; TCS-0025 asks about Frege, not Extended Frege.

**2. Superpolynomial AC0[p]-Frege lower bounds**

For a fixed prime p, exhibit polynomial-length tautologies requiring superpolynomial proofs even when proof lines are bounded-depth Boolean formulas with MOD_p gates. [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.8).

**Why fundamental:** The longstanding missing proof-complexity counterpart of the Razborov-Smolensky circuit lower bounds.

**Novelty check:** The general Frege lower-bound question TCS-0025 does not establish this distinct, classical bounded-depth frontier. Do not split different primes into additional entries. TCS-5933 was checked in full: its selected question concerns constant-depth Ideal Proof System, rather than AC0[p]-Frege.

**Selection limit:** Frege lower bounds and optimal proof-system questions already occur in the catalogue. Fixed-system variants were not multiplied to meet a quota.

## 6. Communication complexity and Boolean function analysis

**New suggestions: 3.**

**1. The Log-Rank Conjecture**

Is deterministic two-party communication complexity bounded by a fixed polynomial in the logarithm of the real rank of the Boolean communication matrix? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2026.7).

**Why fundamental:** One of the organizing conjectures of communication complexity, connecting protocols to linear algebra.

**Novelty check:** No question-level log-rank entry found in the catalogue.

**2. The Fourier Entropy-Influence Conjecture**

Is the Shannon entropy of the squared Fourier coefficients of every Boolean function at most a universal constant times its total influence, under the uniform measure? [Primary source 1](https://arxiv.org/abs/2502.13231).

**Why fundamental:** A central proposed link between spectral complexity and sensitivity, with consequences for learning and Boolean function structure.

**Novelty check:** TCS-6138 concerns Fourier granularity, not the entropy-influence inequality.

**3. The Aaronson-Ambainis Conjecture**

Does every degree-d multilinear polynomial f on the Boolean cube with values in [0,1] have a coordinate of influence at least (Var(f)/d)^C for a universal C? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17).

**Why fundamental:** A foundational question connecting bounded polynomials to the possible advantage of quantum queries.

**Novelty check:** No matching question found. The specific source is Bhattacharya, ITCS 2025, article 17.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 7. Coding and information theory

**New suggestions: 5.**

**1. The exact capacity region of the two-user Gaussian interference channel**

For arbitrary fixed channel gains and transmitter power constraints, determine all simultaneously achievable rate pairs in the memoryless two-user Gaussian interference channel. [Primary source 1](https://arxiv.org/abs/1508.05726).

**Why fundamental:** A defining unresolved multi-user information-theory problem; constant-gap approximations do not give its exact capacity region.

**Novelty check:** No interference-channel question was found. The broad target includes the unresolved mixed/weak-interference regimes, not the solved strong-interference case alone.

**2. The capacity of the binary deletion channel**

Determine the exact optimal asymptotic transmission rate C(delta), for each fixed independent deletion probability delta, by matching achievable-rate and converse bounds. [Primary source 1](https://arxiv.org/abs/1910.07199).

**Why fundamental:** The canonical unresolved channel-capacity problem caused by synchronization errors.

**Novelty check:** Adversarial deletion thresholds and trace reconstruction are different questions. Do not present the formal regularized definition of C as a solution.

**3. Decidability of unconditional information inequalities**

Is there an algorithm that decides whether an input rational linear inequality in the joint Shannon entropies of finitely many discrete random variables holds for every joint distribution? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2024.19).

**Why fundamental:** A fundamental decision problem governing entropy bounds, network information theory and database optimization.

**Novelty check:** Do not conflate unconditional inequality validity with known undecidability results for conditional independence implications.

**4. Constant-rate binary locally decodable codes with logarithmic query complexity**

Do binary codes of constant rate and constant error tolerance exist whose randomized local decoder recovers any requested message bit with O(log n) queries and success probability at least 2/3? [Primary source 1](https://eccc.weizmann.ac.il/report/2025/168/revision/1/download/).

**Why fundamental:** A central locality-versus-redundancy barrier with consequences for private information retrieval and matrix rigidity.

**Novelty check:** The April 2026 revision explicitly identifies the binary problem as a major open question; its construction uses large alphabets.

**5. The Shannon capacity of C7**

Determine Theta(C7)=sup_t alpha(C7 strong-product ... strong-product C7)^{1/t}. [Primary source 1](https://arxiv.org/abs/2608.30273).

**Why fundamental:** The smallest odd-cycle zero-error capacity left unresolved after Lovasz's pentagon theorem.

**Novelty check:** TCS-5034 asks whether Shannon capacity is computable in general. The August 2026 source explicitly says exact odd-cycle capacities beyond C5 remain unknown.

## 8. Algebraic computation

**New suggestions: 6.**

**1. Superpolynomial determinantal complexity of the permanent**

Over characteristic zero, does representing the n by n permanent as the determinant of a matrix of affine-linear forms require superpolynomial matrix dimension? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2021.4).

**Why fundamental:** The classical determinant-versus-permanent barrier and a central target of geometric complexity theory.

**Novelty check:** TCS-5432 instead asks whether equivariant determinantal complexity is polynomially related to ordinary determinantal complexity; its full source was read.

**2. VP versus VBP**

Can every polynomial-degree polynomial family with polynomial-size arithmetic circuits also be computed by polynomial-size algebraic branching programs? [Primary source 1](https://eccc.weizmann.ac.il/report/2025/083/).

**Why fundamental:** The central unresolved cost of restricting general algebraic computation to branching programs.

**Novelty check:** Search matches on arbitrary branching programs or special circuit families do not pose the general class equality.

**3. Polynomial-size arithmetic formulas for determinant**

Does the n by n symbolic determinant have arithmetic formulas of size n^{O(1)} over a fixed characteristic-zero field? [Primary source 1](https://eccc.weizmann.ac.il/report/2003/067/).

**Why fundamental:** The canonical explicit candidate separating arithmetic formulas from algebraic branching programs.

**Novelty check:** Multilinear-formula lower bounds are known; arbitrary arithmetic formulas remain the target. Do not separately count the equivalent VF-versus-VBP formulation.

**4. Deterministic polynomial-time polynomial factorization over finite fields**

Can every univariate polynomial of degree n over F_q be factored deterministically in time polynomial in n and log q? [Primary source 1](https://arxiv.org/abs/2509.12705).

**Why fundamental:** A basic unresolved derandomization problem in computational algebra.

**Novelty check:** No matching question found. The September 2025 result is amortized over many primes, not a solution for an arbitrary input field.

**5. Polynomial-time finite-group isomorphism in the Cayley-table model**

Can one decide in deterministic polynomial time whether two finite groups supplied by their full multiplication tables are isomorphic? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2024.4).

**Why fundamental:** The fundamental outstanding algorithmic isomorphism problem for finite algebraic structures in explicit representation.

**Novelty check:** TCS-4202 asks for a reduction to asymmetric groups, and TCS-5393 asks about a different complexity comparison.

**6. Breaking the 2^n barrier for exact permanent computation**

Is there epsilon>0 and an exact algorithm using O((2-epsilon)^n) arithmetic operations to compute the permanent of every n by n matrix over characteristic zero? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.36).

**Why fundamental:** A canonical exponential-time algebraic computation barrier dating to Ryser's formula.

**Novelty check:** TCS-0815 asks about the relation to SETH; TCS-4858 concerns adapting a particular technique. These must not be silently relabelled as the unrestricted arithmetic-operation question.

## 9. Lattices and computational number theory

**New suggestions: 4.**

**1. Classical polynomial-time integer factorization**

Can a randomized classical algorithm output the prime factorization of every positive binary integer N in poly(log N) time with success probability at least 2/3? [Primary source 1](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf).

**Why fundamental:** A defining computational-number-theory problem with major consequences for cryptographic assumptions.

**Novelty check:** TCS-5395 concerns recursion to smaller inputs and TCS-0656 reductions to lattices. They are not the main algorithm-existence problem.

**2. Classical polynomial-time discrete logarithms in prime fields**

Is there a randomized classical algorithm, polynomial in log p, that given a prime p, a generator g of F_p^*, and h in F_p^*, returns x with g^x=h? [Primary source 1](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf).

**Why fundamental:** A central computational number-theory problem and a foundation of public-key cryptography.

**Novelty check:** The general prime-field algorithmic problem; not a specialized cryptanalytic attack.

**3. Single-exponential-time, polynomial-space exact Euclidean SVP**

Does a randomized classical algorithm solve exact SVP in dimension n in 2^{O(n)} times a polynomial in the input bit length, using only polynomial space? [Primary source 1](https://eccc.weizmann.ac.il/report/2010/014/).

**Why fundamental:** A central time-space barrier separating enumeration from sieve and Voronoi methods in lattice algorithms.

**Novelty check:** Do not count heuristic sieving guarantees or quantum algorithms as a solution. This is distinct from a smaller exponential-time base with exponential memory.

**4. Vinogradov's least quadratic nonresidue conjecture**

For every epsilon>0, is the least positive quadratic nonresidue modulo an odd prime p bounded by p^epsilon for all sufficiently large p? [Primary source 1](https://arxiv.org/abs/1410.7073).

**Why fundamental:** A classical barrier in effective number theory governing the deterministic search for basic finite-field witnesses.

**Novelty check:** No matching question about least quadratic nonresidues was found; placement uses the computational number-theory scope.

**Already proposed elsewhere — not counted: Hilbert's tenth problem over the rationals.** Is there an algorithm deciding whether an input polynomial with integer coefficients has a zero with all coordinates in Q? See the [large-category proposal](../fundamental-additions-20260910/REPORT.md). Its natural small-category placement would be here.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 10. Randomized algorithms and sampling

**New suggestions: 2.**

**1. Rapid mixing of Glauber dynamics with Delta+2 colours**

Does single-vertex Glauber dynamics on proper q-colourings mix in polynomial time for every n-vertex graph of maximum degree Delta whenever q>=Delta+2? [Primary source 1](https://arxiv.org/abs/2010.16158). [Primary source 2](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134).

**Why fundamental:** A canonical test of whether local random updates sample throughout the full ergodic regime.

**Novelty check:** Keep separate from a merely polynomial recolouring diameter. The 2026 colouring-sampling paper still cites algorithms requiring substantially more colours.

**2. The Kannan-Tetali-Vempala switch-chain conjecture**

Does the lazy switch chain mix in polynomial time on every nonempty set of zero-one matrices with prescribed row and column sums? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2018.36).

**Why fundamental:** A central obstruction to a general theory of uniform sampling with fixed combinatorial marginals.

**Novelty check:** TCS-6254 and TCS-6412 concern degree-sequence realizability or modification, not mixing of the switch chain.

**Selection limit:** Many natural landmark candidates were either already solved in the stated model or belonged primarily to the large geometry/optimization groups.

## 11. String algorithms and bioinformatics

**New suggestions: 2.**

**1. Polynomial-sample worst-case trace reconstruction**

For each fixed deletion probability delta in (0,1), can every unknown n-bit string be reconstructed with probability at least 2/3 using n^{O(1)} independent deletion traces? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.3).

**Why fundamental:** A defining information-recovery question underlying reconstruction through synchronization errors.

**Novelty check:** TCS-4942 asks about improving an estimator from a few traces, not exact worst-case reconstruction.

**2. Constant-factor edit-distance approximation in O(n polylog n) time**

Does some universal constant C admit a randomized bounded-error algorithm that C-approximates edit distance of two length-n strings in O(n polylog n) time? [Primary source 1](https://epubs.siam.org/doi/10.1137/21M1392322).

**Why fundamental:** Would settle a main algorithmic frontier for the basic metric on strings.

**Novelty check:** TCS-4932's full source asks about a quantum advantage, not this classical target; near-linear-distance promises and n^{1+epsilon} algorithms do not settle the stated bound. Andoni-Nosatzki obtain n^{1+epsilon} time with epsilon-dependent constants; the target here fixes a polylogarithmic overhead.

**Selection limit:** The 2-approximate-superstring suggestion was withheld because the existing SCS source already includes the stronger greedy conjecture. General word equations with length constraints are cross-referenced below.

## 12. Dynamic graph algorithms

**New suggestions: 3.**

**1. Deterministic fully dynamic connectivity with polylogarithmic worst-case updates**

Can an undirected graph under edge insertions and deletions support connectivity queries and every individual update in polylog(n) deterministic time using polynomial space? [Primary source 1](https://arxiv.org/abs/2510.08297).

**Why fundamental:** A foundational unresolved worst-case guarantee for dynamic graph data structures.

**Novelty check:** The October 2025 breakthrough is randomized with expected worst-case update time. It gives a route to derandomization, not the required deterministic algorithm.

**2. Fully dynamic minimum spanning forest with polylogarithmic worst-case updates**

Can an exact minimum spanning forest of an undirected graph with polynomially bounded integer weights be maintained with polylogarithmic worst-case time per edge insertion or deletion and polynomial preprocessing and space? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.27).

**Why fundamental:** A longstanding worst-case barrier for one of the defining dynamic graph optimization problems.

**Novelty check:** TCS-0541 concerns low-stretch spanning trees, not minimum-weight spanning forests.

**3. Fully dynamic near-optimal matching with polylogarithmic updates**

For every fixed epsilon>0, can a (1+epsilon)-approximate maximum-cardinality matching be maintained in an arbitrary graph with polylogarithmic amortized update time, allowing randomization against an oblivious update sequence? [Primary source 1](https://pure.mpg.de/pubman/item/item_3527212_4/component/file_3527885/biennial-report-2023.pdf).

**Why fundamental:** The main approximation-versus-update-time barrier in dynamic matching.

**Novelty check:** TCS-0543 is about maximal matching; that is weaker than arbitrarily accurate maximum matching.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 13. Counting and enumeration

**New suggestions: 2.**

**1. An FPRAS for perfect matchings in general graphs**

Can the number of perfect matchings of every graph be approximated within relative error epsilon with success probability at least 3/4 in time polynomial in graph size and 1/epsilon? [Primary source 1](https://arxiv.org/abs/1712.07504).

**Why fundamental:** A central remaining frontier for approximate counting beyond the bipartite permanent.

**Novelty check:** Counting all matchings, exact planar perfect matching counting, and the bipartite FPRAS do not resolve the general perfect-matching problem.

**2. A deterministic FPTAS for the nonnegative permanent**

Does a deterministic algorithm approximate the permanent of any nonnegative rational matrix within relative error epsilon in time polynomial in the input bit length and 1/epsilon? [Primary source 1](https://arxiv.org/abs/2608.28031).

**Why fundamental:** A landmark derandomization challenge for approximate counting.

**Novelty check:** Distinguish exact 2^n-time permanent computation from deterministic multiplicative approximation.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 14. Property testing and distribution learning

**New suggestions: 1.**

**1. Characterizing polynomially testable hereditary graph properties**

Give a necessary-and-sufficient structural criterion on a finite forbidden-induced-subgraph family F for F-freeness to have a one-sided dense-model tester using poly(1/epsilon) sampled vertices. [Primary source 1](https://arxiv.org/html/2508.16878v1).

**Why fundamental:** An organizing classification problem for the efficient end of graph property testing.

**Novelty check:** Source Problem 3.14. Single forbidden graphs and a few restricted families have been classified; this is the full finite-family problem.

**Selection limit:** Recent progress essentially closes the main adaptivity exponent gap for Boolean monotonicity testing. Narrow residual improvements were excluded.

## 15. Differential privacy

**New suggestions: 1.**

**1. Optimal Euclidean error for pure-DP statistical-query release**

For every n,T,k and 0<epsilon<=1, does there exist an epsilon-differentially private mechanism answering any k queries f_j:[T]->[-1,1] on a database x in [T]^n with expected normalized Euclidean error E||M(x)-f(x)||_2/sqrt(k) at most C min{1,sqrt(log(2T)/(epsilon n))}, for a universal C? [Primary source 1](https://differentialprivacy.org/open-problem-optimal-query-release/). [Primary source 2](https://arxiv.org/abs/2607.20418).

**Why fundamental:** Would determine the fundamental worst-case accuracy of pure-private statistical-query release, independently of the number of queries.

**Novelty check:** No corresponding query-release question found. This is Nikolov-Ullman Open Problem 2 (Euclidean error), not Open Problem 1 (maximum-coordinate error), for which July 2026 brought a claimed solution.

**Selection limit:** The maximum-coordinate pure-DP query-release conjecture has a July 2026 claimed solution. The retained entry is the separate Euclidean-error problem. Several major private-learning questions are already present.

## 16. Algorithmic game theory, mechanism design and fair division

**New suggestions: 3.**

**1. Constant-factor truthful combinatorial auctions for submodular bidders**

Does a universally truthful randomized mechanism using polynomial communication achieve a universal constant expected approximation to optimal welfare for arbitrary normalized monotone submodular valuations? [Primary source 1](https://epubs.siam.org/doi/10.1137/20M1316068). [Primary source 2](https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf).

**Why fundamental:** The central question of whether incentive constraints destroy constant-factor welfare approximation in a standard multi-parameter auction model.

**Novelty check:** TCS-5229's selected source passage asks about a particular lower-bound construction; budget-feasible procurement is a different problem. Do not silently restrict to value queries.

**2. Polynomial query complexity of exact envy-free cake cutting**

Is there a deterministic Robertson-Webb protocol using polynomially many queries in n that completely allocates a cake envy-freely among n agents with arbitrary nonatomic additive valuations, allowing disconnected pieces? [Primary source 1](https://link.springer.com/article/10.1007/s00355-025-01633-7).

**Why fundamental:** The principal complexity question behind exact envy-free division of a divisible resource.

**Novelty check:** TCS-1110 asks about mixed divisible/indivisible EFM; the 2025 paper gives an average-case bound under random valuations, not a worst-case polynomial protocol.

**3. The optimal randomized metric distortion in social choice**

Determine the infimum universal constant D for which an ordinal voting rule always selects a lottery whose expected total metric cost is at most D times the optimal candidate cost, over all numbers of voters and candidates and all consistent metrics. [Primary source 1](https://arxiv.org/abs/2505.13630).

**Why fundamental:** A defining limit on how much welfare can be recovered from ordinal preferences.

**Novelty check:** Use unrestricted randomized ordinal rules; the old conjecture D=2 is false, and tournament-only rules are a different restricted model.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 17. Constraint satisfaction

**New suggestions: 3.**

**1. A complexity dichotomy for finite promise CSPs**

For every fixed pair of finite relational templates A,B of the same signature with A mapping homomorphically to B, is the decision promise CSP distinguishing X->A from X not->B either in P or NP-hard? [Primary source 1](https://arxiv.org/abs/2208.13538).

**Why fundamental:** The main extension of the finite CSP classification theorem to promise problems.

**Novelty check:** TCS-1978 and TCS-1907 concern particular algorithmic subclasses; this is the full finite-template decision dichotomy.

**2. The Bodirsky-Pinsker infinite-domain CSP dichotomy**

Is CSP(B) always either in P or NP-complete when B is a finite-signature first-order reduct of a countable finitely bounded homogeneous relational structure? [Primary source 1](https://arxiv.org/abs/2601.22691).

**Why fundamental:** The principal tractability classification conjecture for well-behaved infinite-domain CSPs.

**Novelty check:** TCS-3203 asks about GSO definability and TCS-5924 a particular meta-question, rather than the full P/NP-complete dichotomy.

**3. Constant-colour polynomial-time colouring of 3-colourable graphs**

Is there a fixed integer C and a polynomial-time algorithm that outputs a proper C-colouring of every input graph promised to be 3-colourable? [Primary source 1](https://arxiv.org/abs/2406.00357).

**Why fundamental:** The paradigmatic unresolved approximate graph-colouring problem within promise CSP.

**Novelty check:** The constant C is existential and unrestricted; this is not the already-hard 3-to-4 or 3-to-5 problem.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 18. Scheduling and packing

**New suggestions: 3.**

**1. Breaking factor 2 for unrelated-machine makespan**

Is there a polynomial-time (2-epsilon)-approximation for R||Cmax for some fixed epsilon>0? [Primary source 1](https://arxiv.org/abs/2307.08453).

**Why fundamental:** One of the defining approximation barriers in machine scheduling.

**Novelty check:** The existing unrelated-machine entries concern interval restrictions, job types or parameterized complexity.

**2. Constant-factor approximation for general Santa Claus allocation**

Can indivisible items with arbitrary nonnegative additive agent-specific values be allocated in polynomial time so that the least satisfied agent receives at least OPT/C, for a universal C? [Primary source 1](https://arxiv.org/abs/2307.08453).

**Why fundamental:** The central max-min allocation problem and a major boundary of scheduling approximation.

**Novelty check:** TCS-0738 concerns parameterized approximation. Restricted valuations already admit constants and must not replace the general target.

**3. Constant additive error for one-dimensional bin packing**

Can a polynomial-time algorithm pack every instance into at most OPT+C unit bins, where C is a universal constant? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2014.1).

**Why fundamental:** The longstanding gap between asymptotic approximation schemes and almost exact packing.

**Novelty check:** TCS-0931 concerns implementation of a particular Sum-of-Squares algorithm, not this universal additive guarantee.

**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.

## 19. Automated reasoning and unification

**New suggestions: 4.**

**1. The word problem for one-relation monoids**

Is there an algorithm which, given a finite monoid presentation with one defining relation and two words, decides whether the words represent the same element? [Primary source 1](https://link.springer.com/article/10.1007/s00233-021-10216-8).

**Why fundamental:** A century-old algorithmic decidability problem at the smallest nontrivial presentation size.

**Novelty check:** One-relator groups have a decidable word problem; the unresolved monoid problem is different. This belongs naturally with equational reasoning.

**2. The conjugacy problem for one-relator groups**

Is there an algorithm that, given a finite one-relator group presentation and two words, decides whether those words represent conjugate group elements? [Primary source 1](https://arxiv.org/abs/2501.18306).

**Why fundamental:** One of the classical Dehn decision problems in an exceptionally basic class of finitely presented groups.

**Novelty check:** TCS-0041 concerns embeddings of Baumslag-Solitar groups, and TCS-5506 inverse semigroups; neither is this conjugacy decision problem.

**3. Decidability of unification in the basic modal logic K**

Is there an algorithm deciding whether a given K-formula has a substitution instance that is valid in all Kripke frames? [Primary source 1](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=9592&wshow=paper).

**Why fundamental:** The basic unresolved decidability boundary in modal unification, already in the minimal normal modal logic.

**Novelty check:** Beklemishev's 2025 paper explicitly distinguishes the open K case from solved transitive modal logics.

**4. Decidability of termination for one-rule string rewriting**

Given two words l,r, is it decidable whether the rewrite rule l->r admits no infinite rewriting sequence starting from any finite word? [Primary source 1](https://epubs.siam.org/doi/10.1137/S009753979833297X).

**Why fundamental:** A minimal and longstanding unresolved termination problem in rewriting theory.

**Novelty check:** TCS-0874 asks about nontermination without loops; this target is decidability of uniform termination itself.

**Already proposed elsewhere — not counted: Decidability of word equations with linear length constraints.** Is satisfiability decidable for finite systems of word equations over a fixed finite alphabet combined with existential Presburger constraints on the lengths of their string variables? See the [large-category proposal](../fundamental-additions-20260910/REPORT.md). Its natural small-category placement would be here.

**Selection limit:** Word equations with linear length constraints are already in the large-category proposal and are cross-referenced, not counted again.

## 20. Database theory and finite model theory

**New suggestions: 1.**

**1. The full constant-delay conjunctive-query classification**

Classify fixed conjunctive queries, allowing self-joins, whose distinct answers can be enumerated with constant delay after preprocessing linear in database size. [Primary source 1](https://arxiv.org/abs/2206.04988).

**Why fundamental:** The missing general tractability classification for a fundamental database evaluation task.

**Novelty check:** TCS-1434 concerns a join-tree enumeration implementation; the source here concerns arbitrary conjunctive queries and the essential effect of self-joins.

**Selection limit:** Uniform tractable CSP and finite controllability already occur in the catalogue. A 2025 publication claims a logic capturing PTIME; that claim was not adjudicated in this pass, so the problem is held out.

## 21. Computability and algorithmic information

**New suggestions: 4.**

**1. Martin's conjecture on degree-invariant functions**

In ZF+DC+AD, does Martin's full conjecture hold for all Turing-invariant functions from 2^omega to 2^omega: below the identity they are constant or equal to the identity on a cone; the functions at least the identity on a cone are prewellordered by cone-wise Turing reducibility; and pointwise Turing jump increases their rank by one? [Primary source 1](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/on-the-hierarchy-of-natural-theories/FEF058E948E6E8B8A4F5F174E02AFCC9).

**Why fundamental:** A proposed structural account of why the Turing jump governs natural computability-theoretic constructions.

**Novelty check:** No matching Martin-conjecture question was found. Results for order-preserving or uniformly invariant functions do not settle the general conjecture.

**2. Rigidity of the Turing degrees**

Is every automorphism of the partial order of Turing degrees the identity? [Primary source 1](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/permutations-of-the-integers-induce-only-the-trivial-automorphism-of-the-turing-degrees/5BB556CF78395462F77181EA0C197797).

**Why fundamental:** A defining question about how much computational structure is determined by reducibility alone.

**Novelty check:** The existing rigidity keyword matches concern matrices or other structures, not the Turing degrees.

**3. Kolmogorov-Loveland randomness versus Martin-Lof randomness**

Is every infinite binary sequence on which no computable nonmonotonic Kolmogorov-Loveland betting strategy succeeds Martin-Lof random? [Primary source 1](https://arxiv.org/abs/2403.19817).

**Why fundamental:** A central unresolved equivalence between effective statistical tests and adaptive betting definitions of randomness.

**Novelty check:** The 2024 result rules out one approach to an equivalence proof; it does not separate the two randomness notions.

**4. The reverse-mathematical strength of Hindman's theorem**

Does Hindman's finite-sums theorem imply ACA_0^+ over RCA_0? [Primary source 1](https://iris.uniroma1.it/bitstream/11573/1393123/3/Carlucci_postprint_New-bounds_2020.pdf).

**Why fundamental:** The classical gap in the axiomatic strength of a central infinite combinatorial principle; this is a computability/logic question, not a new general-combinatorics category.

**Novelty check:** The theorem itself is known; the proposed target is equivalence with the established upper-bound system ACA_0^+.

**Selection limit:** The list separates general Martin's conjecture from solved restricted cases and does not turn the various randomness notions into a quota of nearby variants.

## 22. Knowledge representation and reasoning

**New suggestions: 1.**

**1. Deterministic polynomial-time equivalence testing for d-DNNFs**

Can one deterministically decide in polynomial time whether two given deterministic decomposable negation-normal-form Boolean circuits represent the same function? [Primary source 1](https://arxiv.org/html/2605.12378v1). [Primary source 2](https://www.auai.org/uai2013/prints/papers/165.pdf).

**Why fundamental:** A basic unresolved operation in knowledge compilation, with consequences for checking and comparing compiled knowledge.

**Novelty check:** TCS-0306 is efficient complementation; equivalence testing is a separate fundamental operation.

**Selection limit:** Complementation of d-DNNF already occurs in the catalogue, the SDD/d-DNNF succinctness separation is known, and finite SROIQ satisfiability is decidable. Unverified broad ontology questions were not padded into the list.

## 23. Structural graph theory

**New suggestions: 5.**

**1. Hadwiger's conjecture**

Does every finite graph with chromatic number at least t contain K_t as a minor? [Primary source 1](https://arxiv.org/abs/2609.06867).

**Why fundamental:** A central link between graph colouring and minor structure, directly governing structural algorithmic methods.

**Novelty check:** The 6 September 2026 preprint improves the general upper bound; it does not prove Hadwiger. The odd Hadwiger variant has a recent counterexample and is excluded.

**2. The Erdos-Hajnal conjecture for hereditary graph classes**

For each finite graph H, is there c(H)>0 such that every n-vertex graph with no induced H contains a clique or independent set of size at least n^{c(H)}? [Primary source 1](https://arxiv.org/abs/2606.06258).

**Why fundamental:** A foundational structural explanation for large homogeneous sets in hereditary classes.

**Novelty check:** The five-vertex cases were settled recently; the question here quantifies over all H.

**3. The Gyarfas-Sumner conjecture**

For every fixed tree T, is the class of graphs with no induced T chi-bounded: chi(G)<=f_T(omega(G)) for some function f_T? [Primary source 1](https://arxiv.org/abs/2302.08922).

**Why fundamental:** A central organizing conjecture for hereditary graph colouring.

**Novelty check:** TCS-6251 concerns independent-set algorithms for graphs without long claws, rather than this chi-boundedness conjecture. Nguyen-Scott-Seymour explicitly formulate the general conjecture in their 2024 paper.

**4. Seese's conjecture for MSO1 and clique-width**

Must every class of finite graphs with decidable monadic second-order theory using vertex-set quantification have bounded clique-width? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.167).

**Why fundamental:** A major proposed characterization connecting algorithmic logic with graph decomposition.

**Novelty check:** Do not confuse MSO1 with the edge-set version, or MSO with the stronger counting-MSO results already known.

**5. Cereceda's quadratic recolouring conjecture**

For every fixed d, does the reconfiguration graph of proper (d+2)-colourings of every n-vertex d-degenerate graph have diameter O_d(n^2), where one step recolours one vertex? [Primary source 1](https://www.sciencedirect.com/science/article/abs/pii/S0012365X26000798).

**Why fundamental:** The principal structural diameter conjecture in graph-colouring reconfiguration.

**Novelty check:** No matching Cereceda or general quadratic degenerate-recolouring question was found.

## 24. Beyond worst-case and average-case analysis

**New suggestions: 3.**

**1. The planted-clique computational threshold**

For every fixed epsilon in (0,1/2), is it impossible for a randomized polynomial-time algorithm to distinguish G(n,1/2) from G(n,1/2) with a uniformly planted clique of size floor(n^{1/2-epsilon}), with success probability at least 2/3? [Primary source 1](https://arxiv.org/abs/2506.13647).

**Why fundamental:** The foundational average-case hardness conjecture behind many proposed statistical-computational gaps.

**Novelty check:** TCS-1699/TCS-5257 use arbitrary base graphs, TCS-0422 a topological method, and TCS-5394 a low-degree model; the main unrestricted random-graph hypothesis is distinct.

**2. The computational threshold for dense tensor PCA**

For fixed k>=3 and 0<epsilon<(k-2)/4, let v be uniform on the unit sphere in R^n and let Z have iid standard Gaussian entries. Given lambda v^{tensor k}+Z at lambda=n^{k/4-epsilon}, is it impossible for a randomized polynomial-time algorithm to output a unit vector u with |<u,v>|>=c with probability >=2/3, for any fixed c>0? [Primary source 1](https://arxiv.org/abs/2605.30113).

**Why fundamental:** A canonical separation between information-theoretic estimation and efficient algorithms in high-dimensional statistics.

**Novelty check:** No matching dense tensor-PCA threshold question was found; lower bounds for low-degree polynomials alone do not settle unrestricted polynomial-time recovery.

**3. Polynomial smoothed complexity of FLIP for Max-Cut**

For every graph, after independent edge-weight perturbations with densities bounded by phi on a bounded interval, is every improving single-vertex-flip path of polynomial expected length in n and phi? [Primary source 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.98).

**Why fundamental:** A flagship unresolved explanation of why a canonical PLS local-search algorithm works efficiently on perturbed inputs.

**Novelty check:** Known polynomial bounds for complete or logarithmic-degree graphs do not cover arbitrary graphs.

**Selection limit:** Low-degree lower bounds are evidence about restricted algorithms, not resolutions of the unrestricted computational thresholds.

## 25. Miscellaneous

**New suggestions: 0.**

**Selection limit:** No additional orphan problem passed both the fundamental-importance test and the agreed scope policy. General combinatorics was not restored through Miscellaneous; a recent sunflower proof claim was held for separate adjudication.

## Important exclusions and status corrections

- Polynomial kernels for Directed Feedback Vertex Set and Vertex Planarization already occur as **TCS-6379/TCS-6441** and **TCS-5901/TCS-0813**, respectively.
- Core non-emptiness in approval elections is already in the full source of **TCS-4249**.
- Uniform algorithms for tractable CSPs are already **TCS-0504**.
- General additive-chores EFX has a [June 2026 counterexample claim](https://arxiv.org/abs/2606.08872); it is excluded.
- The maximum-coordinate pure-DP query-release conjecture has a [July 2026 solution claim](https://arxiv.org/abs/2607.20418); it is excluded. The retained Euclidean-error question is different.
- The [2025 monotonicity-testing lower bound](https://arxiv.org/abs/2511.04558) essentially closes the previously large adaptive-query exponent gap.
- The [2025 ICPT publication](https://arxiv.org/abs/2005.04598) claims a logic capturing PTIME; this pass did not independently assess the proof and does not present the general problem as unqualified open.
- [2026 sunflower proof claim](https://arxiv.org/abs/2606.02667): held for separate verification, not used as a confirmed-open Miscellaneous entry.

Other rejections and holds are in [rejections.json](rejections.json). Brainstorming files are not accepted problem lists.

## Deliverable and validation

The retained machine-readable list is [shortlist.json](shortlist.json); a compact export is [shortlist.csv](shortlist.csv). No new catalogue cards were published. The existing site, taxonomy, problem IDs and concurrent research work were preserved.
