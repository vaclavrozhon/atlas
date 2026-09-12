# Benchmark selection review

Reviewed on 2026-09-11 across 35 categories.

We aim for benchmarks of 100 and 500 problems, with a possible expansion to 1,000. All three use the same category order and the same ranking within each category.

Individual editorial review of saved titles, importance rationales, problem statements, source notes and working summaries. This is a review of importance and topical diversity, not a fresh verification of open status or completion of draft formulations. Importance scores are preserved.

Top 100 takes the first 5/2 places in each large/small category. Top 500 takes the first 25/10 and the possible Top 1000 expansion takes the first 50/20 places from the same order. Top 100 is contained in Top 500, which is contained in Top 1000. Focus places balance scientific importance and topical diversity; remaining places retain score order. None of these subsets certifies current open status.

| Benchmark | Target | Available | Missing |
| --- | ---: | ---: | ---: |
| [Top 100](index.html?benchmark=top100) | 100 | 100 | 0 |
| [Top 500](index.html?benchmark=top500) | 500 | 493 | 7 |
| [Top 1000 (possible expansion)](index.html?benchmark=top1000) | 1000 | 934 | 66 |

## Unfilled places

- top500: Differential privacy has 9/10 places.
- top500: Miscellaneous has 4/10 places.
- top1000: Algorithms has 41/50 places.
- top1000: Optimization and numerical computation has 41/50 places.
- top1000: Cryptography has 43/50 places.
- top1000: Sampling, Markov chains and mixing times has 14/20 places.
- top1000: Data structures has 15/20 places.
- top1000: Dynamic algorithms has 17/20 places.
- top1000: Differential privacy has 9/20 places.
- top1000: Miscellaneous has 4/20 places.

## Review needed after catalogue changes

- Unreviewed focus places in Algorithms: 1
- Unreviewed focus places in Learning theory: 1
- Unreviewed focus places in Miscellaneous: 1

## Computational complexity

Keep the central P versus NP question and major time/space questions, but replace polynomial-hierarchy strictness and NP circuit lower bounds with shallow-circuit separation and the structure of complete sets. This avoids spending all five places on variants of the same NP separation barrier.

Previous prefix: TCS-0001, TCS-6530, TCS-6532, TCS-0021, TCS-6531.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does P equal NP?](index.html#TCS-0001) (TCS-0001) | Nondeterministic computation | 100 | The central boundary between efficient verification and efficient computation, with implications throughout TCS. It is the highest-priority landmark in the complexity category. |
| 2 | [Does P equal PSPACE?](index.html#TCS-6530) (TCS-6530) | Time versus space | 100 | A defining question about the relationship between the two basic computational resources, time and working memory. It is a top-priority foundational class separation. |
| 3 | [Can every polynomial-time decision problem be solved in logarithmic space?](index.html#TCS-6531) (TCS-6531) | Space-efficient computation | 98 | A canonical unresolved boundary between time and memory, asking whether any polynomial-time decision problem intrinsically needs more than logarithmic workspace. |
| 4 | [Is nonuniform TC⁰ strictly smaller than nonuniform NC¹?](index.html#TCS-6535) (TCS-6535) | Shallow threshold circuits | 97 | A flagship unresolved containment between basic circuit classes, with explicit complete problems and connections to arithmetic, algebraic automata theory, and lower-bound amplification. |
| 5 | [The Berman–Hartmanis isomorphism conjecture](index.html#TCS-6534) (TCS-6534) | Structure of complete problems | 96 | A defining structural-complexity conjecture about the entire NP-complete degree, stronger than P≠NP and supported by substantial restricted-model theorems and oracle barriers. |

Candidates considered: TCS-0001, TCS-6530, TCS-6532, TCS-0021, TCS-6531, TCS-6535, TCS-0002, TCS-0015, TCS-0016, TCS-6534, TCS-6533, TCS-0004, TCS-0020, TCS-1056, TCS-0018, TCS-1054, TCS-6681, TCS-3873, TCS-7129, TCS-7130, TCS-7131, TCS-7132.

## Algorithms

The focus spans integer sorting, structured real-key sorting, hypergraph cut sparsification, offline comparison complexity and directed reachability distance. These choices balance saved importance and distinct algorithmic tasks without changing statements, evidence or importance scores. The September 11 interest screen removed TCS-0477; replacement focus choices remain unreviewed.

Previous prefix: TCS-6498, TCS-6537, TCS-6540, TCS-6586, TCS-0388.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Expected linear-time integer sorting for every word length](index.html#TCS-6537) (TCS-6537) | Integer sorting | 96 | A foundational algorithmic primitive whose optimal complexity tests the computational power of the word RAM and would affect many tasks built on ordering integer keys. |
| 2 | [Can all pairwise sums X+Y be sorted in quadratic time?](index.html#TCS-0388) (TCS-0388) | Structured comparison sorting | 79 | Sorting all pairwise sums is a classical structured comparison problem: the output is quadratic, but exploiting the inherited order with equally efficient total computation remains the target. It adds real-key comparison algorithms alongside word-RAM integer sorting and data structures. |
| 3 | [Does every hypergraph have a cut sparsifier with O(n/ε²) hyperedges?](index.html#TCS-0946) (TCS-0946) | Combinatorial sparsification | 76 | A universal cut-preserving reduction of hypergraphs to few weighted hyperedges is a broad compression target supporting many downstream algorithms. Its focus is the size of a combinatorial sparsifier, with no query-interface guarantee. |
| 4 | [Can reachability diameter be approximated within a constant in near-linear time?](index.html#TCS-1141) (TCS-1141) | Directed reachability distance | 75 | A constant-factor estimate of the largest finite directed distance in near-linear time is a broad algorithmic target alongside sorting, sparsification and offline comparisons. It is the highest-ranked remaining candidate in this category; its saved importance score and statement are preserved. |
| 5 | [Mincost flow in planar graphs](index.html#TCS-0809) (TCS-0809) | Needs review | 62 | Unreviewed replacement |

Candidates considered: TCS-6498, TCS-6536, TCS-6537, TCS-6538, TCS-6540, TCS-6539, TCS-6586, TCS-6511, TCS-0949, TCS-0611, TCS-6508, TCS-0388, TCS-0771, TCS-0946, TCS-1141.

## Automata and formal languages

Keep synchronization, succinctness, expression complexity, logical classification and transducer equivalence. Generalized star height and dot depth both concern regular languages but measure different structural questions.

Previous prefix: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6563.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Černý conjecture: a reset word of length at most (n−1)²](index.html#TCS-6558) (TCS-6558) | Synchronization | 98 | The flagship quantitative question about synchronizing automata, connecting finite-state control, extremal combinatorics, and linear-algebraic methods. |
| 2 | [Can every two-way NFA be determinized with polynomially many states?](index.html#TCS-6560) (TCS-6560) | Two-way nondeterminism | 97 | The flagship state-complexity problem for two-way finite automata, open since 1978, with unusually direct connections between finite-state descriptions and logarithmic-space complexity. |
| 3 | [Does any regular language require generalized star height greater than one?](index.html#TCS-6559) (TCS-6559) | Regular-expression complexity | 96 | A longstanding foundational problem connecting regular expressions, finite automata, algebraic language theory and logical descriptions. |
| 4 | [Decidability of every level of the dot-depth hierarchy](index.html#TCS-6561) (TCS-6561) | Logical language hierarchies | 95 | A longstanding structural decision problem linking finite automata, logical definability and finite monoids; a full solution would explain much more than the known low-level algorithms. |
| 5 | [Equivalence of deterministic macro tree transducers](index.html#TCS-6563) (TCS-6563) | Tree-transducer equivalence | 95 | A central longstanding transducer-equivalence problem, connecting functional program verification with finite-state methods, algebraic invariants and structural recursion. |

Candidates considered: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6563, TCS-6582, TCS-6564, TCS-0164, TCS-0121, TCS-0146, TCS-0135, TCS-0156, TCS-0167, TCS-0136.

## Semantics, logic and verification

Retain one recurrence problem and one quantitative-game problem; use the other places for dependent types, denotational models and type-system consistency. Continuous Skolem and mean-payoff games remain highly ranked outside the prefix instead of duplicating its two initial strands.

Previous prefix: TCS-6565, TCS-6567, TCS-6568, TCS-6566, TCS-6569.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Is positivity of integer linear recurrences decidable?](index.html#TCS-6565) (TCS-6565) | Linear recurrence verification | 97 | A longstanding foundational decision problem with an elementary input model, strong links to verification, and consequences for the separate Skolem problem; unrestricted decidability is unknown before any efficiency requirement is imposed. |
| 2 | [Can simple stochastic games be solved in polynomial time?](index.html#TCS-6567) (TCS-6567) | Stochastic game solving | 97 | An elementary game model with broad consequences for synthesis and stochastic verification; short optimal strategies and efficiently checkable certificates coexist with an unresolved polynomial-time search problem. |
| 3 | [An internal tower of semisimplicial types in ordinary HoTT](index.html#TCS-6569) (TCS-6569) | Dependent type theory | 95 | A central expressiveness problem for homotopy type theory; precise internal construction would remove a major obstacle to formalizing higher structures without enriching the theory. |
| 4 | [Can a Scott-continuous lambda model validate exactly beta-conversion?](index.html#TCS-6570) (TCS-6570) | Denotational semantics | 94 | The classical completeness question of whether denotational semantics can capture exactly the syntactic equality of a basic programming model. |
| 5 | [Does weak normalization imply strong normalization for every pure type system?](index.html#TCS-6583) (TCS-6583) | Consistency of type systems | 94 | Asks whether the existence of a terminating reduction for every typable term forces every reduction of every such term to terminate. |

Candidates considered: TCS-6565, TCS-6567, TCS-6568, TCS-6566, TCS-6569, TCS-6570, TCS-6583, TCS-5773, TCS-0619, TCS-0632, TCS-0575.

## Distributed, parallel and sublinear algorithms

Keep the existing five: they cover general parallel computation, streaming, deterministic parallel matching, locality and bandwidth. General parallelizability and matching are related, but the derandomization problem has its own central motivation.

Previous prefix: TCS-6553, TCS-6556, TCS-6504, TCS-6554, TCS-6555.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Can every polynomial-time decision problem be efficiently parallelized?](index.html#TCS-6553) (TCS-6553) | Parallelizability | 99 | The foundational tractability question for parallel computation: whether every polynomial-time task admits polylogarithmic dependency depth with polynomial work. |
| 2 | [Directed reachability with nearly linear memory and polylogarithmic passes](index.html#TCS-6556) (TCS-6556) | Streaming reachability | 95 | A basic directed-graph primitive with a polynomial-versus-polylogarithmic pass gap, connections to communication lower bounds and consequences for other streaming tasks. |
| 3 | [Is perfect matching in general graphs in deterministic NC?](index.html#TCS-6504) (TCS-6504) | Parallel algebraic derandomization | 94 | A canonical deterministic parallel-algorithm and derandomization question for a basic graph optimization problem. |
| 4 | [Distributed Lovász Local Lemma in O(log log n) rounds](index.html#TCS-6554) (TCS-6554) | Local distributed symmetry breaking | 94 | A canonical obstacle to resolving local conflicts rapidly, with consequences for many distributed graph algorithms. |
| 5 | [Optimal exact single-source shortest paths in CONGEST](index.html#TCS-6555) (TCS-6555) | Bandwidth-limited distributed paths | 94 | A basic distributed graph primitive with an unresolved gap between algorithms and communication lower bounds. |

Candidates considered: TCS-6553, TCS-6556, TCS-6504, TCS-6554, TCS-6555, TCS-6557, TCS-6507, TCS-0522, TCS-6499, TCS-6505, TCS-6506, TCS-0998, TCS-0515.

## Optimization and numerical computation

The prefix spans linear programming, exact semidefinite feasibility, integral packing and covering, sparse numerical linear algebra and geometric energy optimization. The k-server conjecture now represents the dedicated online category; the packing versus max-flow min-cut conjecture fills its former place without duplicating the LP algorithm question.

Previous prefix: TCS-0008, TCS-6572, TCS-6574, TCS-6575, TCS-6585.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does general rational linear programming have a strongly polynomial algorithm?](index.html#TCS-0008) (TCS-0008) | Linear programming complexity | 97 | A leading open question in optimization, separating ordinary polynomial-time solvability from a dimension-only arithmetic bound. Its reach includes general linear programming and many combinatorial optimization problems. |
| 2 | [Is exact semidefinite feasibility in polynomial time?](index.html#TCS-6574) (TCS-6574) | Exact semidefinite optimization | 97 | A foundational complexity gap in a widely used convex optimization model; exact decision remains open despite powerful approximation algorithms, exact duality and symbolic decidability. |
| 3 | [Does the packing property imply the max-flow min-cut property?](index.html#TCS-7227) (TCS-7227) | Integral packing and covering | 90 | The packing versus max-flow min-cut conjecture adds a fundamental combinatorial integrality question alongside continuous optimization and numerical computation. |
| 4 | [Nearly linear-time solution of general sparse linear systems](index.html#TCS-6585) (TCS-6585) | Numerical linear algebra | 97 | A fundamental input-size complexity question for one of the most widely used computational primitives, with meaningful positive results for structured classes and general reductions from apparently special systems. |
| 5 | [Smale’s seventh problem: efficient near-minimal logarithmic energy on the sphere](index.html#TCS-6578) (TCS-6578) | Geometric energy optimization | 94 | Smale's seventh problem asks for efficient construction of globally near-optimal configurations. |

Candidates considered: TCS-0008, TCS-6572, TCS-6574, TCS-6575, TCS-6585, TCS-6576, TCS-6577, TCS-6578, TCS-0491, TCS-0711, TCS-0724, TCS-0715, TCS-0728, TCS-0708, TCS-0722, TCS-7227, TCS-7226.

## Geometry, topology and metric spaces

The existing leaders cover concentration, embeddings, topology, polytope diameter and planar incidence structure. Keep this mix; the saved claimed-solution caveat on unknot recognition remains visible.

Previous prefix: TCS-6523, TCS-6525, TCS-6528, TCS-6573, TCS-0318.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does every isotropic log-concave measure have a dimension-free Poincaré constant?](index.html#TCS-6523) (TCS-6523) | Convex concentration | 98 | A foundational high-dimensional geometry conjecture with substantial consequences for sampling, integration, optimization, and concentration inequalities. |
| 2 | [Gupta–Newman–Rabinovich–Sinclair conjecture](index.html#TCS-6525) (TCS-6525) | Metric embeddings | 95 | A central link between graph minor structure, metric embeddings and the quality of the basic sparsest-cut relaxation, already open in the planar case. |
| 3 | [Unknot recognition in polynomial time](index.html#TCS-6528) (TCS-6528) | Computational topology | 95 | A central algorithmic topology problem in NP∩coNP; a fresh claimed polynomial-time solution makes precise formulation and validation especially valuable. |
| 4 | [Polynomial Hirsch conjecture for edge-path diameter](index.html#TCS-6573) (TCS-6573) | Polytope geometry | 95 | The surviving fundamental diameter question after the original Hirsch bound failed; it separates geometric existence of short routes from algorithmic navigation and the newly resolved circuit analogue. |
| 5 | [How many k-element subsets can a line separate from a planar point set?](index.html#TCS-0318) (TCS-0318) | Discrete geometric complexity | 94 | A defining extremal-complexity question for geometric algorithms, already unresolved in the plane and connected to levels, geometric selection, and parametric optimization. |

Candidates considered: TCS-6523, TCS-6525, TCS-6528, TCS-6573, TCS-0318, TCS-6524, TCS-6526, TCS-0406, TCS-6527, TCS-6529, TCS-0403, TCS-0408, TCS-0427, TCS-0410.

## Learning theory

Retain sample compression, noisy learning, junta learning and the information complexity of VC learning. After source correction and a full review, select distribution-free improper PAC learning of DNF in place of the narrower two-halfspace question: DNF is a foundational general rule-learning target. Its implication for uniform-example junta learning is documented; both remain individually significant. TCS-0023 is a retired, mislabelled junta-source pointer and is not another DNF problem. The September 11 interest screen removed TCS-0679; replacement focus choices remain unreviewed.

Previous prefix: TCS-6541, TCS-6542, TCS-6543, TCS-6544, TCS-0023.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does every VC class admit linear-size sample compression?](index.html#TCS-6541) (TCS-6541) | Sample compression | 97 | A longstanding general conjecture asking whether VC dimension controls sample representation up to a constant factor; it reaches far beyond any one learning algorithm or geometric example. |
| 2 | [Polynomial-time learning parity with constant random noise](index.html#TCS-6542) (TCS-6542) | Learning with noise | 96 | A fundamental boundary between information-theoretic learnability and efficient learning, with broad consequences for noise-tolerant algorithms and cryptographic assumptions. |
| 3 | [Learning Boolean juntas from uniform random examples](index.html#TCS-6543) (TCS-6543) | Sparse Boolean structure | 95 | A central unresolved task in computational learning theory, isolating feature selection and serving as a prerequisite for efficient learning of general decision trees and DNF formulas. |
| 4 | [Polynomial-time distribution-free PAC learning of DNF](index.html#TCS-5358) (TCS-5358) | Distribution-free Boolean rule learning | 97 | A defining improper PAC-learning question for compact Boolean rules under arbitrary input distributions, with broad consequences for decision-tree and junta learning. The general target and its conditional-hardness evidence are now stated precisely. |
| 5 | [Distribution-free learning of intersections of two halfspaces](index.html#TCS-6544) (TCS-6544) | Needs review | 92 | Unreviewed replacement |

Candidates considered: TCS-6541, TCS-6542, TCS-6543, TCS-6544, TCS-0677, TCS-0691, TCS-0694, TCS-0683, TCS-0670, TCS-0671, TCS-0664, TCS-0682, TCS-5358.

## Cryptography

Balance public-key existence, worst-case foundations, obfuscation, homomorphic computation and perfect secret sharing. Move oblivious transfer and collision resistance below the focus prefix to avoid filling it with neighboring primitive-implication questions. General secret-sharing efficiency contributes a distinct information-theoretic barrier.

Previous prefix: TCS-6545, TCS-0022, TCS-6549, TCS-6550, TCS-6547.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Do one-way functions imply public-key encryption in the standard model?](index.html#TCS-6545) (TCS-6545) | Public-key foundations | 98 | A central minimal-assumption question in cryptographic foundations, separating the known reach of generic one-wayness from public-key communication. |
| 2 | [Does P≠NP imply the existence of one-way functions?](index.html#TCS-0022) (TCS-0022) | Complexity foundations of cryptography | 97 | A foundational question about the weakest assumptions supporting cryptography, linking NP hardness, average-case complexity, inversion, and pseudorandomness. |
| 3 | [Does ordinary polynomial-hard LWE suffice for circuit obfuscation?](index.html#TCS-6550) (TCS-6550) | Program obfuscation | 97 | A central assumption-minimization problem for general obfuscation, with consequences throughout cryptography and a crucial distinction between ordinary LWE and strengthened LWE-based assumptions. |
| 4 | [Unleveled fully homomorphic encryption from LWE alone](index.html#TCS-6551) (TCS-6551) | Computation on encrypted data | 95 | A central foundational gap in fully homomorphic encryption, separating established leveled LWE constructions from reusable fixed-depth-independent keys and their extra security assumptions. |
| 5 | [Can every perfect secret-sharing access structure use shares below exponent one half?](index.html#TCS-0465) (TCS-0465) | Information-theoretic secret sharing | 88 | The share size needed for general secret sharing is a fundamental efficiency limit for realizing arbitrary access structures. |

Candidates considered: TCS-6545, TCS-0022, TCS-6549, TCS-6550, TCS-6547, TCS-6546, TCS-6548, TCS-6551, TCS-6552, TCS-0465, TCS-6454, TCS-1138.

## Quantum computation and information

Keep computational hardness, algorithmic power, many-body structure and verification; use NPT bound entanglement for the fifth place instead of a second local-testability question alongside quantum PCP.

Previous prefix: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6515.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Quantum PCP: a constant promise gap for local Hamiltonians](index.html#TCS-6446) (TCS-6446) | Local Hamiltonian hardness | 98 | A defining quantum-complexity conjecture connecting robust verification, approximation hardness, and the structure of many-body Hamiltonians. |
| 2 | [Does BPP differ from BQP?](index.html#TCS-0036) (TCS-0036) | Quantum computational advantage | 97 | A central foundational separation between classical and quantum efficient computation, with consequences for algorithms, simulation, and the computational interpretation of quantum mechanics. |
| 3 | [An entanglement entropy area law for general gapped two-dimensional Hamiltonians](index.html#TCS-6516) (TCS-6516) | Ground-state entanglement | 97 | A fundamental unresolved link between spectral gaps, geometric locality, entanglement, and the resources needed to describe quantum many-body ground states. |
| 4 | [Information-theoretic classical verification of quantum computation](index.html#TCS-6580) (TCS-6580) | Classical verification | 97 | A central quantum-complexity question connecting interactive proofs, delegation and the minimum resources needed to verify computations beyond classical simulation. |
| 5 | [Does NPT bound entanglement exist?](index.html#TCS-6518) (TCS-6518) | Entanglement distillation | 96 | A central structural boundary in entanglement theory, with canonical finite-dimensional candidates and consequences for what quantum correlations can accomplish under local operations. |

Candidates considered: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6515, TCS-6517, TCS-6518, TCS-6519, TCS-0037, TCS-6448, TCS-6520, TCS-6521, TCS-6522, TCS-0029, TCS-6449, TCS-0033.

## Computability and algorithmic information theory

Pair Martin’s conjecture with Kolmogorov–Loveland randomness. Move rigidity of the Turing degrees below the prefix to avoid using both places for degree structure.

Previous prefix: TCS-6646, TCS-6647.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Martin’s full conjecture for Turing-invariant functions under determinacy](index.html#TCS-6646) (TCS-6646) | Invariant degree-theoretic functions | 98 | A flagship conjecture about the global structure of Turing degrees and the classification of invariant computational operations. |
| 2 | [Kolmogorov–Loveland randomness versus Martin-Löf randomness](index.html#TCS-6648) (TCS-6648) | Algorithmic randomness | 96 | A defining open question linking computability, adaptive information access, fair betting and effective null tests; a resolution would settle the relationship between two foundational randomness notions. |

Candidates considered: TCS-6646, TCS-6647, TCS-6648, TCS-6685, TCS-6649, TCS-6679, TCS-0247.

## Proof complexity

Pair Extended Frege lower bounds with Frege versus Extended Frege simulation. Replace a second nested lower-bound target with a distinct comparison of proof systems.

Previous prefix: TCS-6601, TCS-6602.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Do some tautologies require superpolynomial Extended Frege proofs?](index.html#TCS-6601) (TCS-6601) | Proof-length lower bounds | 99 | A defining open lower-bound problem for strong propositional reasoning, closely connected to bounded arithmetic, circuit complexity, and the limits of efficiently checkable certificates. |
| 2 | [Does Frege simulate Extended Frege with polynomial proof size?](index.html#TCS-6663) (TCS-6663) | Relative strength of proof systems | 97 | A canonical strong-system simulation problem, directly tied to Frege lower bounds, finite consistency and circuit-based reasoning. |

Candidates considered: TCS-6601, TCS-6602, TCS-6663, TCS-0025, TCS-0024, TCS-1099, TCS-1096, TCS-1097.

## Communication complexity and Boolean function analysis

Keep the log-rank and Fourier Entropy–Influence conjectures, representing the communication and Boolean-analysis sides of the category.

Previous prefix: TCS-6603, TCS-6604.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Log-rank conjecture for deterministic two-party communication](index.html#TCS-6603) (TCS-6603) | Communication versus rank | 98 | A flagship structural conjecture linking deterministic protocols and matrix rank, with many equivalent combinatorial formulations and a large quantitative gap. |
| 2 | [The Fourier Entropy–Influence conjecture](index.html#TCS-6604) (TCS-6604) | Fourier information and influence | 97 | A longstanding, broadly consequential conjecture in Boolean function analysis, with direct learning-theory implications and active 2026 progress that still leaves the universal classical inequality open. |

Candidates considered: TCS-6603, TCS-6604, TCS-6605, TCS-6581, TCS-6664, TCS-6450, TCS-1043, TCS-0220.

## Fine-grained complexity

Keep SETH and APSP. This avoids choosing SETH together with its closely related Orthogonal Vectors formulation for both places.

Previous prefix: TCS-6595, TCS-6510.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does the Strong Exponential Time Hypothesis hold?](index.html#TCS-6595) (TCS-6595) | Satisfiability exponents | 99 | A principal organizing hypothesis of fine-grained complexity, connecting exact SAT complexity to tight running-time barriers across many algorithmic areas. |
| 2 | [Can exact weighted all-pairs shortest paths be computed in truly subcubic time?](index.html#TCS-6510) (TCS-6510) | Weighted graph distances | 97 | Truly subcubic exact weighted APSP is a central fine-grained benchmark with consequences for a large family of graph and matrix problems. |

Candidates considered: TCS-6595, TCS-6510, TCS-6596, TCS-6597, TCS-6661, TCS-6503, TCS-6598, TCS-0557.

## Pseudorandomness and derandomization

Keep general polynomial-time derandomization and explicit generators for read-once branching programs. The second adds a concrete space-bounded construction target rather than another general BPP simulation claim.

Previous prefix: TCS-0003, TCS-6600.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Can randomness always be removed from polynomial-time decision algorithms?](index.html#TCS-0003) (TCS-0003) | General derandomization | 97 | The main general derandomization question for polynomial-time decision algorithms, with broad consequences for the role of randomness and for hardness-versus-randomness techniques. |
| 2 | [Optimal explicit pseudorandom generators for read-once branching programs](index.html#TCS-6600) (TCS-6600) | Space-bounded pseudorandomness | 97 | A central constructive route to L=BPL, with optimal nonconstructive seed length known and a persistent gap for uniform space-efficient generators despite advances in restricted and weighted models. |

Candidates considered: TCS-0003, TCS-6600, TCS-6662, TCS-1005, TCS-0026, TCS-1018, TCS-1015, TCS-1016.

## Parameterized complexity and algorithms

Keep the two central perspectives of this bucket: dependence on a parameter and the exponential rate of exact satisfiability algorithms.

Previous prefix: TCS-6592, TCS-6593.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Is k-Clique fixed-parameter tractable, equivalently FPT=W[1]?](index.html#TCS-6592) (TCS-6592) | Parameterized tractability | 99 | The defining unresolved tractability separation of parameterized complexity, with Clique as a precise and widely used complete problem. |
| 2 | [Does deterministic 3-SAT have a positive optimal exponential rate?](index.html#TCS-6593) (TCS-6593) | Exact exponential algorithms | 98 | A foundational quantitative hardness hypothesis underlying exact, parameterized, graph, and geometric algorithm lower bounds. |

Candidates considered: TCS-6592, TCS-6593, TCS-6594, TCS-6660, TCS-0787.

## Approximation algorithms and inapproximability

Keep an algorithmic approximation frontier and a general hardness conjecture. Their relationship to NP hardness does not erase the distinct algorithmic and hardness roles.

Previous prefix: TCS-6587, TCS-0006.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Constant-factor approximation for Densest k-Subgraph](index.html#TCS-6587) (TCS-6587) | Approximation algorithms for dense subgraphs | 97 | A flagship approximation problem with a simple objective, a large algorithmic gap, strong conditional and relaxation barriers, and consequences for several other optimization problems. |
| 2 | [Unique Games: is near-satisfiability NP-hard to distinguish from low value?](index.html#TCS-0006) (TCS-0006) | Hardness of approximation | 96 | An organizing conjecture for approximation thresholds, with consequences for whole families of constraint satisfaction problems and strong connections to SDP algorithms, PCPs, and analysis. |

Candidates considered: TCS-6587, TCS-0006, TCS-6588, TCS-6589, TCS-6659, TCS-6590, TCS-6591, TCS-0088.

## Online algorithms, scheduling and packing

The user merged the online and scheduling/packing categories with one small-category quota. Pair the deterministic k-server conjecture with unrelated-machine makespan to represent competitive analysis and offline scheduling. Bandit convex optimization and bin packing remain active candidates below this two-problem focus prefix; importance scores are preserved.

Previous prefix: TCS-6575, TCS-6577, TCS-6638, TCS-6640.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [The deterministic k-server conjecture](index.html#TCS-6575) (TCS-6575) | Online algorithms | 97 | A foundational conjecture about online decision-making, with an optimal lower bound, one broadly applicable candidate algorithm, and a persistent gap on general metrics despite many resolved special cases. |
| 2 | [A constant improvement over factor 2 for unrelated-machine makespan](index.html#TCS-6638) (TCS-6638) | Heterogeneous-machine scheduling | 97 | A decades-old central scheduling problem with a large hardness gap, robust LP barriers and formal consequences for fair allocation. |

Candidates considered: TCS-0700, TCS-0708, TCS-0711, TCS-0715, TCS-0716, TCS-1241, TCS-1529, TCS-3314, TCS-3392, TCS-3566, TCS-3690, TCS-3878, TCS-4132, TCS-4393, TCS-4449, TCS-4581, TCS-4655, TCS-4983, TCS-5004, TCS-5030, TCS-5126, TCS-5158, TCS-5182, TCS-5186, TCS-5221, TCS-5252, TCS-5349, TCS-5514, TCS-5747, TCS-5779, TCS-6575, TCS-6576, TCS-6577, TCS-6833, TCS-6836, TCS-6838, TCS-6638, TCS-6676, TCS-6640, TCS-0924, TCS-0935, TCS-0922.

## Beyond worst-case and average-case analysis

Keep planted clique and the worst-case-to-average-case NP question. This balances a canonical average-case model with a general complexity-foundations question instead of choosing two planted-inference thresholds.

Previous prefix: TCS-6656, TCS-0012.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Planted clique: can polynomial time detect a clique below the square-root scale?](index.html#TCS-6656) (TCS-6656) | Planted inference | 98 | A canonical computational threshold with broad consequences in average-case complexity, statistical inference, and the study of algorithmic lower-bound frameworks. |
| 2 | [Does P≠NP imply a samplable NP problem outside AvgP?](index.html#TCS-0012) (TCS-0012) | Worst-case versus average-case hardness | 97 | One of the central missing implications in complexity theory, connecting worst-case lower bounds to feasible instance generation and the limits of algorithms on typical inputs. |

Candidates considered: TCS-6656, TCS-0012, TCS-6657, TCS-6684, TCS-6453, TCS-6658.

## Sampling, Markov chains and mixing times

Keep two central sampling problems on different state spaces: colourings and graphs with prescribed degrees. Both involve mixing, which is intrinsic to this bucket; another spin-system question would be a closer repeat.

Previous prefix: TCS-6621, TCS-6622.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Rapid mixing of Glauber dynamics with Δ+2 colours](index.html#TCS-6621) (TCS-6621) | Colouring-chain mixing | 95 | A longstanding general-graph conjecture linking local algorithms, approximate counting and spin systems; recent near-threshold results still require structural restrictions. |
| 2 | [The Kannan–Tetali–Vempala switch-chain conjecture for binary matrices](index.html#TCS-6622) (TCS-6622) | Sampling prescribed-degree graphs | 94 | A central obstruction to a general theory of uniform sampling with fixed combinatorial marginals. |

Candidates considered: TCS-6621, TCS-6622, TCS-6668, TCS-1693.

## Counting and enumeration

Pair approximate counting of perfect matchings with the general #BIS approximation frontier. Minimal-hypergraph-transversal enumeration returns to this category after the knowledge bucket is retired; the existing two focus selections are retained.

Previous prefix: TCS-6628, TCS-6629, TCS-7112.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [An FPRAS for perfect matchings in general graphs](index.html#TCS-6628) (TCS-6628) | Approximate counting | 97 | The major missing generalization of the permanent FPRAS, with an established obstruction to the direct Markov-chain approach and consequences beyond matchings. |
| 2 | [Does #BIS admit an FPRAS?](index.html#TCS-7221) (TCS-7221) | Approximate counting | 97 | #BIS is the canonical intermediate approximate-counting problem: an FPRAS would resolve a central boundary shared by many spin-system and combinatorial counting tasks. |

Candidates considered: TCS-6628, TCS-6629, TCS-6671, TCS-0553, TCS-1004, TCS-0556, TCS-7221, TCS-7112.

## Structural graph theory and graph algorithms

The expanded category covers both graph structure and graph algorithms. Hadwiger represents structural graph theory; deterministic linear-time MST represents a foundational static algorithm. Erdős–Hajnal and general maximum matching remain important candidates beyond the two-place focus prefix.

Previous prefix: TCS-6651, TCS-6652.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Hadwiger’s conjecture: high chromatic number forces a clique minor](index.html#TCS-6651) (TCS-6651) | Graph minors and colouring | 98 | One of the central graph-theoretic conjectures, with an exact extremal target and consequences across coloring and minor structure. |
| 2 | [Deterministic linear-time minimum spanning tree](index.html#TCS-6536) (TCS-6536) | Static graph algorithms | 96 | A foundational graph-algorithm question about the necessity of randomness and the relationship between comparison complexity and actual computation. |

Candidates considered: TCS-6651, TCS-6652, TCS-6682, TCS-6653, TCS-6683, TCS-6654, TCS-6655, TCS-6500, TCS-6536, TCS-6538, TCS-6539, TCS-6511, TCS-0611, TCS-7180, TCS-0771, TCS-0594, TCS-0775.

## Data structures

The user approved a small Data structures category with dynamic optimality of splay trees and general static cell-probe lower bounds as its two focus topics. Together they represent adaptive upper bounds and unconditional information-access lower bounds. Dictionaries, heaps, ordered sequences, external-memory structures, history independence and static query representations remain active below the focus pair with unchanged importance scores.

Previous prefix: empty.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Are splay trees dynamically optimal?](index.html#TCS-6498) (TCS-6498) | Adaptive search trees | 97 | Dynamic optimality is a central benchmark for adaptive data structures: one simple online BST would compete with every offline BST on every access sequence. |
| 2 | [An explicit static problem requiring superlogarithmically many cell probes](index.html#TCS-6540) (TCS-6540) | Static data-structure lower bounds | 96 | A model-wide challenge connecting algorithms, communication complexity, pseudorandomness and circuit lower bounds, with implications beyond any single geometric or graph problem. |

Candidates considered: TCS-6498, TCS-6540, TCS-6586, TCS-0949, TCS-6508, TCS-6514, TCS-4997, TCS-5706, TCS-5768, TCS-5103, TCS-1798, TCS-0300, TCS-2730, TCS-3788, TCS-5825.

## Dynamic algorithms

Retain deterministic connectivity and near-optimal matching as the strongest reviewed focus candidates after expanding to non-graph dynamic algorithms. The new maintenance questions broaden the pool; their saved importance scores and evidence do not displace this pair. Minimum spanning forests remain outside the pair to avoid duplicating its connectivity strand.

Previous prefix: TCS-6625, TCS-6626.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Deterministic fully dynamic connectivity with polylogarithmic worst-case updates](index.html#TCS-6625) (TCS-6625) | Dynamic connectivity | 97 | A foundational dynamic-graph frontier directly relevant to data structures, with a new randomized breakthrough and an explicit remaining deterministic bottleneck. |
| 2 | [Fully dynamic near-optimal matching with polylogarithmic updates](index.html#TCS-6627) (TCS-6627) | Dynamic matching | 95 | A central dynamic graph problem connecting approximation, explicit solution maintenance and extremal induced-matching structure. |

Candidates considered: TCS-6625, TCS-6626, TCS-6627, TCS-6670, TCS-0478, TCS-0543, TCS-0541, TCS-0300, TCS-2730, TCS-3788, TCS-5825, TCS-0387, TCS-5612, TCS-3331, TCS-4307.

## String algorithms and computational biology

Keep trace reconstruction and constant-factor edit-distance approximation in the two focus places, covering statistical recovery from deletions and fast sequence comparison. The separately approved near-exact approximation scheme (TCS-7220) is retained immediately beyond this prefix by importance: it studies a different accuracy–runtime boundary, while selecting both edit-distance variants here would remove trace-reconstruction coverage.

Previous prefix: TCS-6623, TCS-6624.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Polynomial-sample worst-case trace reconstruction](index.html#TCS-6623) (TCS-6623) | Reconstruction from noisy strings | 96 | A defining worst-case recovery problem for synchronization noise, linking string algorithms, information theory, statistics and complex-analytic methods. |
| 2 | [Constant-factor edit-distance approximation in O(n polylog n) time](index.html#TCS-6624) (TCS-6624) | Sequence distance algorithms | 95 | A central remaining precision–runtime boundary for edit distance, distinct from the established n^{1+ε} constant-factor algorithms and from exact-computation hardness. |

Candidates considered: TCS-6623, TCS-6624, TCS-6669, TCS-6513, TCS-0467, TCS-0468, TCS-0470, TCS-7220.

## Game theory, social choice and fair division

Pair truthful submodular auctions with EFX existence. This represents both incentive constraints and a central fairness existence question; algorithmic Santa Claus allocation remains in the wider benchmark.

Previous prefix: TCS-6632, TCS-6639.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Constant-factor universally truthful auctions for submodular bidders](index.html#TCS-6632) (TCS-6632) | Truthful mechanisms | 96 | A central multi-parameter mechanism-design problem linking truthful incentives, submodular optimization, information elicitation and the communication cost of welfare approximation. |
| 2 | [Existence of complete EFX allocations for additive valuations](index.html#TCS-0011) (TCS-0011) | Existence of fair allocations | 92 | A central existence question for a strong and widely studied fairness guarantee for indivisible goods. |

Candidates considered: TCS-6632, TCS-6639, TCS-6674, TCS-6633, TCS-6634, TCS-0011, TCS-1116, TCS-0056.

## Algebraic computation

Keep matrix multiplication and permanent-versus-determinant complexity: algorithmic bilinear computation and algebraic representation lower bounds.

Previous prefix: TCS-0007, TCS-6611.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Is the matrix multiplication exponent equal to two?](index.html#TCS-0007) (TCS-0007) | Matrix multiplication | 98 | One of the main questions in algebraic algorithms, governing a widely used primitive and many dependent complexity bounds. Both faster constructions and a superquadratic lower bound would have broad consequences. |
| 2 | [Does the permanent require determinants of superpolynomial dimension?](index.html#TCS-6611) (TCS-6611) | Algebraic representation lower bounds | 98 | The principal permanent-versus-determinant lower-bound problem, connecting algebraic computation, branching programs, geometry, and symmetry. |

Candidates considered: TCS-0007, TCS-6611, TCS-6666, TCS-6612, TCS-0005, TCS-6613, TCS-6641, TCS-6614.

## Lattices and computational number theory

Pair rational polynomial solvability with polynomial-factor Euclidean SVP. This retains a major number-theoretic decision frontier while giving lattices a leading place; factoring and discrete logarithms remain outside the two-place prefix.

Previous prefix: TCS-6571, TCS-6617.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Is rational solvability of polynomial equations decidable?](index.html#TCS-6571) (TCS-6571) | Diophantine decidability | 99 | A central unsolved decidability problem for an elementary, pervasive constraint language. A resolution would locate the computability boundary for rational polynomial feasibility. |
| 2 | [Polynomial-time, polynomial-factor approximation of Euclidean SVP](index.html#TCS-6667) (TCS-6667) | Lattice approximation | 97 | A fundamental worst-case algorithm question at the heart of lattice reduction, with a wide gap between current methods and the target and connections to cryptographic hardness. |

Candidates considered: TCS-6571, TCS-6617, TCS-6618, TCS-6667, TCS-6619, TCS-6620, TCS-0658, TCS-0659.

## Coding and information theory

Pair Gaussian interference capacity with the binary rate–distance tradeoff. Move the second multiuser capacity question below the prefix so that coding theory has a leading representative. Preserve the existing uncertainty around the Gaussian-capacity claim.

Previous prefix: TCS-6606, TCS-6665.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [The exact capacity region of the two-user Gaussian interference channel](index.html#TCS-6606) (TCS-6606) | Network channel capacity | 97 | A foundational multi-user capacity frontier with a simple channel model, strong approximate results and unresolved exact tradeoffs. Recent disputed claims make the precise formulation and status record especially valuable. |
| 2 | [The optimal asymptotic binary rate–distance tradeoff](index.html#TCS-1010) (TCS-1010) | Error-correcting code limits | 96 | A foundational coding-theory limit with a precise extremal target, a large gap between existence and converse bounds, and connections to combinatorics, information theory and quantum methods. |

Candidates considered: TCS-6606, TCS-6665, TCS-1010, TCS-6584, TCS-6607, TCS-6608, TCS-6609, TCS-6610.

## Property testing and distribution learning

Keep the graph-testing classification and add the universal testing-versus-distance-estimation frontier. The reviewed formulation is the explicit Problem 5.4 from the 2025 survey and replaces the former underspecified tolerant-testing index note in the focus prefix.

Previous prefix: TCS-6630, TCS-6672, TCS-0672.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Effective classification of polynomially testable hereditary graph properties](index.html#TCS-6630) (TCS-6630) | Graph property classification | 95 | An effective formulation of the major finite-family classification problem; it separates polynomial sampling from mere testability and abstract quantitative equivalences. |
| 2 | [Does polynomial testability imply polynomial distance estimation for dense graph properties?](index.html#TCS-1033) (TCS-1033) | Testing versus distance estimation | 96 | A universal polynomial tester-to-estimator implication would convert robust graph-property recognition into quantitative distance measurement across the dense model. |

Candidates considered: TCS-6630, TCS-6672, TCS-1030, TCS-1029, TCS-1033, TCS-0672, TCS-1033.

## Differential privacy

Pair sample complexity of private PAC learning with optimal error in private continual counting. The saved review marks TCS-6631 resolved, making the former query-release focus ineligible. TCS-6673 is an active, previously considered replacement covering sequential private release; its statement, evidence and importance score are unchanged.

Previous prefix: TCS-6631, TCS-0506.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Is private PAC sample complexity polynomial in VC dimension and log-star Littlestone dimension?](index.html#TCS-0506) (TCS-0506) | Private learnability | 88 | Seeks a quantitative sample-complexity characterization of private learnability in terms of two basic dimensions, with consequences across hypothesis classes. |
| 2 | [Optimal error for pure-DP continual counting](index.html#TCS-6673) (TCS-6673) | Private continual counting | 94 | The saved target asks for optimal worst-time error when releasing every prefix sum under pure differential privacy. It complements sample-complexity bounds for private learning with a fundamental sequential data-release problem. |

Candidates considered: TCS-6631, TCS-6673, TCS-0506, TCS-0510, TCS-0507.

## Constraint satisfaction

Keep the finite promise-CSP and infinite-domain CSP dichotomies. Their common classification form is justified by fundamentally different domain and promise structures; a special graph-colouring case would add less breadth.

Previous prefix: TCS-6635, TCS-6636.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Does every finite-template decision promise CSP have a P/NP-hard dichotomy?](index.html#TCS-6635) (TCS-6635) | Finite promise constraints | 98 | A broad structural question extending the finite CSP dichotomy into approximation and promise problems, with connections to algebra, topology, and optimization. |
| 2 | [The Bodirsky–Pinsker infinite-domain CSP dichotomy](index.html#TCS-6636) (TCS-6636) | Infinite-domain constraints | 97 | A central unifying conjecture about the boundary of polynomial-time constraint solving, with broad logical scope and active links to promise CSPs. |

Candidates considered: TCS-6635, TCS-6636, TCS-6637, TCS-6675, TCS-1978, TCS-0441, TCS-0504, TCS-0444.

## Automated reasoning, rewriting and unification

Keep word equations with length constraints and modal-K unification, spanning symbolic strings with arithmetic and logical substitution.

Previous prefix: TCS-6562, TCS-6643.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Are word equations with linear length constraints decidable?](index.html#TCS-6562) (TCS-6562) | Word equations with arithmetic | 97 | A longstanding decidability question at the intersection of formal languages, number-theoretic constraints and automated verification; even unrestricted termination is unknown, before asking for efficient algorithms. |
| 2 | [Decidability of unification in the basic modal logic K](index.html#TCS-6643) (TCS-6643) | Modal unification | 94 | The basic unresolved decidability boundary in modal unification, already in the minimal normal modal logic. |

Candidates considered: TCS-6562, TCS-6643, TCS-6644, TCS-0163, TCS-0171, TCS-0173, TCS-6650, TCS-0306, TCS-7134, TCS-7135.

## Database theory and finite model theory

Keep FO model checking and conjunctive-query enumeration. The pair covers structural logical tractability and output-sensitive database evaluation.

Previous prefix: TCS-6678, TCS-6645.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FO model checking on hereditary monadically dependent graph classes](index.html#TCS-6678) (TCS-6678) | Finite-model-theoretic tractability | 96 | The central proposed tractability boundary for first-order model checking on hereditary graph classes, connecting database queries, model theory, sparsity and dense graph structure. |
| 2 | [The full constant-delay conjunctive-query classification](index.html#TCS-6645) (TCS-6645) | Database query enumeration | 95 | A central database-theory classification question: identify exactly which fixed queries permit optimal preprocessing and delay, including the self-joins excluded by classical dichotomies. |

Candidates considered: TCS-6678, TCS-6645, TCS-0492, TCS-0488, TCS-0482, TCS-0487, TCS-0494, TCS-6680, TCS-4206.

## Miscellaneous

After reviewing active records for the restored Miscellaneous scope, select the 1/3–2/3 conjecture and pancake numbers as distinct foundational boundary questions. Keep gold partition outside the pair to avoid two partial-order balance questions; molecular computation and structural permutation classes remain provisional candidates. Graph isomorphism now has an explicit graph-algorithm home. The September 11 interest screen removed TCS-7176; replacement focus choices remain unreviewed.

Previous prefix: TCS-7222.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [The 1/3–2/3 conjecture](index.html#TCS-7177) (TCS-7177) | Partial-order balance | 90 | Would provide a universally informative comparison for sorting with partial-order information; retained as a computationally motivated combinatorial exception. |
| 2 | [The sunflower conjecture](index.html#TCS-7290) (TCS-7290) | Needs review | 89 | Unreviewed replacement |

Candidates considered: TCS-7222, TCS-7177, TCS-3520.
