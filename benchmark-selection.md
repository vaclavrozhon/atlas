# Benchmark selection review

Reviewed on 2026-09-12 across 35 categories.

Our primary goal is a benchmark of 500 problems. Top 100 is a priority subset of those same 500, with secondary editorial attention. Both use the same category order and the same ranking within each category. The existing Top 1000 view is not an active benchmark goal.

Individual category-wide review of every active card, reading its title, formal target and significance, with additional saved context where needed. Scientific importance is primary: foundational scope, breadth of consequences and influence on other questions. Topical diversity distinguishes comparably important candidates in the focus prefix. Every card receives a fresh score assessment and an individual reason; the remaining order follows these scores. Nearby scores are editorial priorities rather than precise measurements. In the live reader, shared vote scores remain primary and the editorial order only breaks ties. This review does not recertify open status or formulation quality.

Top 100 takes the first 5/2 places in each large/small category. Top 500 takes the first 25/10 and the legacy Top 1000 view takes the first 50/20 places from the same order. Top 100 is contained in Top 500, which is contained in Top 1000. Focus places balance scientific importance and topical diversity; remaining places retain score order. None of these subsets certifies current open status.

| Benchmark | Target | Available | Missing |
| --- | ---: | ---: | ---: |
| [Top 100](index.html?benchmark=top100) | 100 | 100 | 0 |
| [Top 500](index.html?benchmark=top500) | 500 | 485 | 15 |
| [Top 1000 (legacy view)](index.html?benchmark=top1000) | 1000 | 798 | 202 |

## Unfilled places

- top500: Optimization and numerical computation has 24/25 places.
- top500: Sampling, Markov chains and mixing times has 9/10 places.
- top500: Differential privacy has 4/10 places.
- top500: Miscellaneous has 3/10 places.
- top1000: Algorithms has 27/50 places.
- top1000: Automata and formal languages has 31/50 places.
- top1000: Semantics, logic and verification has 37/50 places.
- top1000: Distributed, parallel and sublinear algorithms has 49/50 places.
- top1000: Optimization and numerical computation has 24/50 places.
- top1000: Geometry, topology and metric spaces has 40/50 places.
- top1000: Learning theory has 36/50 places.
- top1000: Cryptography has 30/50 places.
- top1000: Computability and algorithmic information theory has 18/20 places.
- top1000: Beyond worst-case and average-case analysis has 13/20 places.
- top1000: Sampling, Markov chains and mixing times has 9/20 places.
- top1000: Counting and enumeration has 18/20 places.
- top1000: Data structures has 17/20 places.
- top1000: Dynamic algorithms has 15/20 places.
- top1000: Property testing and distribution learning has 16/20 places.
- top1000: Differential privacy has 4/20 places.
- top1000: Constraint satisfaction has 18/20 places.
- top1000: Automated reasoning, rewriting and unification has 14/20 places.
- top1000: Database theory and finite model theory has 19/20 places.
- top1000: Miscellaneous has 3/20 places.

## Review needed after catalogue changes

- Unreviewed focus places in Algorithms: 1
- Unreviewed focus places in Learning theory: 1
- Unreviewed focus places in Online algorithms, scheduling and packing: 1

## Computational complexity

Foundational barriers lead: efficient verification, unrestricted nonuniform lower bounds, polynomial space, logarithmic-space nondeterminism, and metacomplexity. Diversity only separates nearby priorities; related P-versus-NP and circuit questions remain high in the full ranking. General resource simulations and total-search structure precede narrower representation and closure questions.

Previous prefix: TCS-0001, TCS-6530, TCS-6531, TCS-6535, TCS-6534.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NP](index.html#TCS-0001) (TCS-0001) | Nondeterministic computation | 100 | The central boundary between efficient verification and efficient computation, with implications throughout TCS. It is the highest-priority landmark in the complexity category. |
| 2 | [P versus PSPACE](index.html#TCS-6530) (TCS-6530) | Time versus space | 100 | A defining question about the relationship between the two basic computational resources, time and working memory. It is a top-priority foundational class separation. |
| 3 | [L versus P](index.html#TCS-6531) (TCS-6531) | Space-efficient computation | 98 | A canonical unresolved boundary between time and memory, asking whether any polynomial-time decision problem intrinsically needs more than logarithmic workspace. |
| 4 | [Nonuniform \(\mathrm{TC}^{0}\) versus \(\mathrm{NC}^{1}\)](index.html#TCS-6535) (TCS-6535) | Shallow threshold circuits | 97 | A flagship unresolved containment between basic circuit classes, with explicit complete problems and connections to arithmetic, algebraic automata theory, and lower-bound amplification. |
| 5 | [Berman–Hartmanis conjecture](index.html#TCS-6534) (TCS-6534) | Structure of complete problems | 96 | A defining structural-complexity conjecture about the entire NP-complete degree, stronger than P≠NP and supported by substantial restricted-model theorems and oracle barriers. |

Candidates considered: TCS-0001, TCS-0021, TCS-6530, TCS-0004, TCS-4786, TCS-0002, TCS-0015, TCS-6532, TCS-6531, TCS-6535, TCS-0020, TCS-4988, TCS-6977, TCS-0016, TCS-7158, TCS-0017, TCS-7161, TCS-7286, TCS-7363, TCS-1056, TCS-6534, TCS-6743, TCS-6817, TCS-7321, TCS-0018, TCS-0293, TCS-2333, TCS-6533, TCS-7256, TCS-7268, TCS-1054, TCS-6934, TCS-6979, TCS-7382, TCS-0019, TCS-6747, TCS-7378, TCS-7381, TCS-5593, TCS-6091, TCS-6168, TCS-6455, TCS-7159, TCS-1053, TCS-6714, TCS-7257, TCS-0303, TCS-1052, TCS-6006, TCS-6285, TCS-0297, TCS-0298, TCS-0301, TCS-2681, TCS-4746, TCS-6681, TCS-7243, TCS-1040, TCS-2532, TCS-3886, TCS-2425, TCS-7260, TCS-0305, TCS-2215, TCS-3862, TCS-6139, TCS-1602, TCS-2029, TCS-1035, TCS-1036, TCS-1034, TCS-0310.

## Algorithms

Lead with basic algorithmic primitives and broad compression principles. Sorting, output-sensitive Subset Sum, hypergraph cuts, additive distances and implicit representations provide distinct high-value directions. Structural classification questions remain ahead of specialized runtime refinements; historical scores of 50 do not discount substantial routing and reconstruction problems.

Previous prefix: TCS-6537, TCS-0388, TCS-0946, TCS-1141.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Expected linear-time integer sorting for every word length](index.html#TCS-6537) (TCS-6537) | Integer sorting | 96 | A foundational algorithmic primitive whose optimal complexity tests the computational power of the word RAM and would affect many tasks built on ordering integer keys. |
| 2 | [Sorting \(X + Y\)](index.html#TCS-0388) (TCS-0388) | Structured comparison sorting | 79 | Sorting all pairwise sums is a classical structured comparison problem: the output is quadratic, but exploiting the inherited order with equally efficient total computation remains the target. It adds real-key comparison algorithms alongside word-RAM integer sorting and data structures. |
| 3 | [Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges](index.html#TCS-0946) (TCS-0946) | Combinatorial sparsification | 76 | A universal cut-preserving reduction of hypergraphs to few weighted hyperedges is a broad compression target supporting many downstream algorithms. Its focus is the size of a combinatorial sparsifier, with no query-interface guarantee. |
| 4 | [Near-linear-time approximation of reachability diameter](index.html#TCS-1141) (TCS-1141) | Directed reachability distance | 75 | A constant-factor estimate of the largest finite directed distance in near-linear time is a broad algorithmic target alongside sorting, sparsification and offline comparisons. It is the highest-ranked remaining candidate in this category; its saved importance score and statement are preserved. |
| 5 | [Near-linear output-sensitive Subset Sum](index.html#TCS-7350) (TCS-7350) | Needs review | 90 | Unreviewed replacement |

Candidates considered: TCS-6537, TCS-7350, TCS-0946, TCS-6783, TCS-5705, TCS-0388, TCS-1338, TCS-6251, TCS-6785, TCS-2018, TCS-4417, TCS-6421, TCS-1617, TCS-5969, TCS-7351, TCS-3263, TCS-3346, TCS-6270, TCS-6784, TCS-7075, TCS-7146, TCS-1141, TCS-7061, TCS-6173, TCS-2822, TCS-0538, TCS-0809.

## Automata and formal languages

The principal finite-state and language-expression landmarks lead. Higher-order recursive equivalence joins synchronization, two-way nondeterminism, star height and dot depth in the prefix. Tree transformations, logical definability and unique parsing follow closely; quantitative, timed and cellular models broaden the rest without displacing stronger foundational questions.

Previous prefix: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6563.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Maximum reset threshold of synchronizing automata](index.html#TCS-6558) (TCS-6558) | Synchronization | 98 | The flagship quantitative question about synchronizing automata, connecting finite-state control, extremal combinatorics, and linear-algebraic methods. |
| 2 | [Sakoda–Sipser problem](index.html#TCS-6560) (TCS-6560) | Two-way nondeterminism | 97 | The flagship state-complexity problem for two-way finite automata, open since 1978, with unusually direct connections between finite-state descriptions and logarithmic-space complexity. |
| 3 | [Generalized star-height problem](index.html#TCS-6559) (TCS-6559) | Regular-expression complexity | 96 | A longstanding foundational problem connecting regular expressions, finite automata, algebraic language theory and logical descriptions. |
| 4 | [Decidability of every level of the dot-depth hierarchy](index.html#TCS-6561) (TCS-6561) | Logical language hierarchies | 95 | A longstanding structural decision problem linking finite automata, logical definability and finite monoids; a full solution would explain much more than the known low-level algorithms. |
| 5 | [Equivalence of deterministic macro tree transducers](index.html#TCS-6563) (TCS-6563) | Tree-transducer equivalence | 95 | A central longstanding transducer-equivalence problem, connecting functional program verification with finite-state methods, algebraic invariants and structural recursion. |

Candidates considered: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6582, TCS-6563, TCS-6564, TCS-0164, TCS-7261, TCS-5904, TCS-7309, TCS-3863, TCS-0135, TCS-0154, TCS-0167, TCS-6064, TCS-4575, TCS-5959, TCS-0146, TCS-5651, TCS-2243, TCS-0138, TCS-5863, TCS-5738, TCS-0128, TCS-4677, TCS-3378, TCS-0136, TCS-4636, TCS-4659, TCS-0133.

## Semantics, logic and verification

Parity games, Skolem decidability, real exponentiation and stochastic games are the broadest algorithmic landmarks. Internal semisimplicial types represents foundational expressiveness among nearby priorities. Positivity and mean-payoff games remain immediately below rather than filling the prefix with related dynamics and game variants; general logical and program-equivalence boundaries precede dimension-specific refinements.

Previous prefix: TCS-6565, TCS-6567, TCS-6569, TCS-6570, TCS-6583.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Positivity problem for linear recurrences](index.html#TCS-6565) (TCS-6565) | Linear recurrence verification | 97 | A longstanding foundational decision problem with an elementary input model, strong links to verification, and consequences for the separate Skolem problem; unrestricted decidability is unknown before any efficiency requirement is imposed. |
| 2 | [Simple stochastic games in polynomial time](index.html#TCS-6567) (TCS-6567) | Stochastic game solving | 97 | An elementary game model with broad consequences for synthesis and stochastic verification; short optimal strategies and efficiently checkable certificates coexist with an unresolved polynomial-time search problem. |
| 3 | [Internal semisimplicial types in ordinary HoTT](index.html#TCS-6569) (TCS-6569) | Dependent type theory | 95 | A central expressiveness problem for homotopy type theory; precise internal construction would remove a major obstacle to formalizing higher structures without enriching the theory. |
| 4 | [Scott-continuous lambda models with theory \(\lambda \beta\)](index.html#TCS-6570) (TCS-6570) | Denotational semantics | 94 | The classical completeness question of whether denotational semantics can capture exactly the syntactic equality of a basic programming model. |
| 5 | [Barendregt–Geuvers–Klop conjecture](index.html#TCS-6583) (TCS-6583) | Consistency of type systems | 94 | Asks whether the existence of a terminating reduction for every typable term forces every reduction of every such term to terminate. |

Candidates considered: TCS-4245, TCS-5773, TCS-7230, TCS-6567, TCS-6569, TCS-6565, TCS-6568, TCS-7192, TCS-6570, TCS-7157, TCS-6566, TCS-6583, TCS-1649, TCS-7153, TCS-5915, TCS-5682, TCS-5987, TCS-4302, TCS-6245, TCS-3655, TCS-6359, TCS-5817, TCS-7154, TCS-0632, TCS-7310, TCS-6036, TCS-3031, TCS-6112, TCS-5975, TCS-2033, TCS-4017, TCS-0913, TCS-0896, TCS-0901, TCS-1659, TCS-0619, TCS-0092.

## Distributed, parallel and sublinear algorithms

General parallelizability leads, followed by deterministic matching, distributed locality, streaming reachability and unconditional bandwidth lower bounds. Work-efficient reachability and flow remain very high. The full selection also represents MPC, shared-memory synchronization, local computation and sketches; small logarithmic or model-specific refinements follow broader barriers.

Previous prefix: TCS-6553, TCS-6556, TCS-6504, TCS-6554, TCS-6555.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NC](index.html#TCS-6553) (TCS-6553) | Parallelizability | 99 | The foundational tractability question for parallel computation: whether every polynomial-time task admits polylogarithmic dependency depth with polynomial work. |
| 2 | [Directed reachability with nearly linear memory and polylogarithmic passes](index.html#TCS-6556) (TCS-6556) | Streaming reachability | 95 | A basic directed-graph primitive with a polynomial-versus-polylogarithmic pass gap, connections to communication lower bounds and consequences for other streaming tasks. |
| 3 | [Perfect matching in NC](index.html#TCS-6504) (TCS-6504) | Parallel algebraic derandomization | 94 | A canonical deterministic parallel-algorithm and derandomization question for a basic graph optimization problem. |
| 4 | [Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds](index.html#TCS-6554) (TCS-6554) | Local distributed symmetry breaking | 94 | A canonical obstacle to resolving local conflicts rapidly, with consequences for many distributed graph algorithms. |
| 5 | [Optimal exact single-source shortest paths in CONGEST](index.html#TCS-6555) (TCS-6555) | Bandwidth-limited distributed paths | 94 | A basic distributed graph primitive with an unresolved gap between algorithms and communication lower bounds. |

Candidates considered: TCS-6553, TCS-6504, TCS-6554, TCS-6556, TCS-6557, TCS-6507, TCS-7349, TCS-6505, TCS-6499, TCS-6555, TCS-7172, TCS-6506, TCS-7336, TCS-0984, TCS-0998, TCS-0515, TCS-0954, TCS-0950, TCS-0969, TCS-4274, TCS-0940, TCS-0986, TCS-7010, TCS-0522, TCS-3792, TCS-5795, TCS-0980, TCS-6501, TCS-5797, TCS-7259, TCS-7337, TCS-0519, TCS-3075, TCS-7376, TCS-0524, TCS-0993, TCS-2233, TCS-6380, TCS-0469, TCS-4763, TCS-1588, TCS-3381, TCS-6080, TCS-6206, TCS-0994, TCS-3384, TCS-0985, TCS-0834, TCS-0849.

## Optimization and numerical computation

Strongly polynomial LP, general sparse linear systems, exact SDP, Komlos discrepancy and simplex complexity form the strongest distinct optimization barriers. Broad integer and complementarity primitives follow. Named constructions do not automatically outrank general optimization principles, and refined runtime or oracle tradeoffs are ordered by the scope of their consequences.

Previous prefix: TCS-0008, TCS-6574, TCS-7227, TCS-6585, TCS-6578.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strongly polynomial linear programming](index.html#TCS-0008) (TCS-0008) | Linear programming complexity | 97 | A leading open question in optimization, separating ordinary polynomial-time solvability from a dimension-only arithmetic bound. Its reach includes general linear programming and many combinatorial optimization problems. |
| 2 | [Exact semidefinite feasibility in polynomial time](index.html#TCS-6574) (TCS-6574) | Exact semidefinite optimization | 97 | A foundational complexity gap in a widely used convex optimization model; exact decision remains open despite powerful approximation algorithms, exact duality and symbolic decidability. |
| 3 | [Conforti–Cornuéjols conjecture](index.html#TCS-7227) (TCS-7227) | Integral packing and covering | 90 | The packing versus max-flow min-cut conjecture adds a fundamental combinatorial integrality question alongside continuous optimization and numerical computation. |
| 4 | [Nearly linear-time solution of general sparse linear systems](index.html#TCS-6585) (TCS-6585) | Numerical linear algebra | 97 | A fundamental input-size complexity question for one of the most widely used computational primitives, with meaningful positive results for structured classes and general reductions from apparently special systems. |
| 5 | [Smale’s seventh problem](index.html#TCS-6578) (TCS-6578) | Geometric energy optimization | 94 | Smale's seventh problem asks for efficient construction of globally near-optimal configurations. |

Candidates considered: TCS-0008, TCS-6585, TCS-6574, TCS-7314, TCS-6572, TCS-7264, TCS-7231, TCS-7315, TCS-7283, TCS-7227, TCS-6483, TCS-0722, TCS-6578, TCS-7226, TCS-7298, TCS-0724, TCS-7007, TCS-5330, TCS-0491, TCS-0728, TCS-0687, TCS-0725, TCS-0914, TCS-0673.

## Geometry, topology and metric spaces

The prefix spans convex concentration, metric distortion, polyhedral paths, planar extremal geometry and algorithmic topology. Basic topology decidability questions formerly carrying low scores move near the top. Broad geometric primitives and compression principles precede finer certificate variants and specialized representation targets.

Previous prefix: TCS-6523, TCS-6525, TCS-6528, TCS-6573, TCS-0318.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Kannan–Lovász–Simonovits conjecture](index.html#TCS-6523) (TCS-6523) | Convex concentration | 98 | A foundational high-dimensional geometry conjecture with substantial consequences for sampling, integration, optimization, and concentration inequalities. |
| 2 | [Gupta–Newman–Rabinovich–Sinclair conjecture](index.html#TCS-6525) (TCS-6525) | Metric embeddings | 95 | A central link between graph minor structure, metric embeddings and the quality of the basic sparsest-cut relaxation, already open in the planar case. |
| 3 | [Unknot recognition in polynomial time](index.html#TCS-6528) (TCS-6528) | Computational topology | 95 | A central algorithmic topology problem in NP∩coNP; a fresh claimed polynomial-time solution makes precise formulation and validation especially valuable. |
| 4 | [Polynomial Hirsch conjecture](index.html#TCS-6573) (TCS-6573) | Polytope geometry | 95 | The surviving fundamental diameter question after the original Hirsch bound failed; it separates geometric existence of short routes from algorithmic navigation and the newly resolved circuit analogue. |
| 5 | [Planar k-set extremal function](index.html#TCS-0318) (TCS-0318) | Planar extremal geometry | 94 | A defining two-parameter extremal problem underlying levels and geometric selection; its source-defined asymptotic function is admissible under the restored numerical/function policy. |

Candidates considered: TCS-6523, TCS-6525, TCS-6573, TCS-0318, TCS-6528, TCS-7242, TCS-6199, TCS-6524, TCS-6526, TCS-7292, TCS-6527, TCS-0406, TCS-7184, TCS-0403, TCS-6880, TCS-0973, TCS-7006, TCS-0408, TCS-0410, TCS-0381, TCS-0411, TCS-7182, TCS-0417, TCS-0970, TCS-0382, TCS-0427, TCS-0377, TCS-0416, TCS-0990, TCS-0398, TCS-0419, TCS-0327, TCS-0430, TCS-7189, TCS-0432, TCS-0428, TCS-0340, TCS-4454, TCS-3059, TCS-0409.

## Learning theory

Distribution-free DNF learning, universal sample compression and noisy parity are the defining landmarks. The prefix also includes the learning-to-cryptography bridge and statistically separated Gaussian mixtures; these broaden the leading questions without excluding juntas and halfspaces from the next positions. General computational and statistical principles precede narrower compression conventions or model-specific refinements.

Previous prefix: TCS-6541, TCS-6542, TCS-6543, TCS-5358.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Linear-size sample compression](index.html#TCS-6541) (TCS-6541) | Sample compression | 97 | A longstanding general conjecture asking whether VC dimension controls sample representation up to a constant factor; it reaches far beyond any one learning algorithm or geometric example. |
| 2 | [Learning parity with noise in polynomial time](index.html#TCS-6542) (TCS-6542) | Learning with noise | 96 | A fundamental boundary between information-theoretic learnability and efficient learning, with broad consequences for noise-tolerant algorithms and cryptographic assumptions. |
| 3 | [Learning Boolean juntas from uniform random examples](index.html#TCS-6543) (TCS-6543) | Sparse Boolean structure | 95 | A central unresolved task in computational learning theory, isolating feature selection and serving as a prerequisite for efficient learning of general decision trees and DNF formulas. |
| 4 | [Polynomial-time distribution-free PAC learning of DNF](index.html#TCS-5358) (TCS-5358) | Distribution-free Boolean rule learning | 97 | A defining improper PAC-learning question for compact Boolean rules under arbitrary input distributions, with broad consequences for decision-tree and junta learning. The general target and its conditional-hardness evidence are now stated precisely. |
| 5 | [Efficient learning of well-separated Gaussian mixtures](index.html#TCS-3391) (TCS-3391) | Needs review | 92 | Unreviewed replacement |

Candidates considered: TCS-5358, TCS-6541, TCS-6542, TCS-5090, TCS-3391, TCS-6543, TCS-7293, TCS-1573, TCS-5088, TCS-2336, TCS-7294, TCS-5119, TCS-6544, TCS-4592, TCS-5847, TCS-2339, TCS-5087, TCS-5902, TCS-3117, TCS-4186, TCS-1539, TCS-5031, TCS-4792, TCS-5434, TCS-0670, TCS-3177, TCS-3691, TCS-0677, TCS-3787, TCS-0664, TCS-0683, TCS-0682, TCS-3689, TCS-0671, TCS-0694, TCS-0689.

## Cryptography

Start with the existence and minimal foundations of cryptography. Public-key encryption from one-wayness, worst-case-to-average-case hardness, obfuscation and oblivious transfer are comparably consequential distinct barriers. Related existence and encryption-strengthening variants remain high; information-theoretic primitives add diversity only after the stronger general assumption questions.

Previous prefix: TCS-6545, TCS-0022, TCS-6550, TCS-6551, TCS-0465.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Public-key encryption from one-way functions](index.html#TCS-6545) (TCS-6545) | Public-key foundations | 98 | A central minimal-assumption question in cryptographic foundations, separating the known reach of generic one-wayness from public-key communication. |
| 2 | [One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0022) (TCS-0022) | Complexity foundations of cryptography | 97 | A foundational question about the weakest assumptions supporting cryptography, linking NP hardness, average-case complexity, inversion, and pseudorandomness. |
| 3 | [Circuit obfuscation from polynomial-hard LWE](index.html#TCS-6550) (TCS-6550) | Program obfuscation | 97 | A central assumption-minimization problem for general obfuscation, with consequences throughout cryptography and a crucial distinction between ordinary LWE and strengthened LWE-based assumptions. |
| 4 | [Unleveled fully homomorphic encryption from LWE alone](index.html#TCS-6551) (TCS-6551) | Computation on encrypted data | 95 | A central foundational gap in fully homomorphic encryption, separating established leveled LWE constructions from reusable fixed-depth-independent keys and their extra security assumptions. |
| 5 | [Sub-square-root share-size exponents in perfect secret sharing](index.html#TCS-0465) (TCS-0465) | Information-theoretic secret sharing | 88 | The share size needed for general secret sharing is a fundamental efficiency limit for realizing arbitrary access structures. |

Candidates considered: TCS-7167, TCS-6545, TCS-0022, TCS-6550, TCS-6549, TCS-7168, TCS-7229, TCS-6547, TCS-6551, TCS-6552, TCS-6548, TCS-7277, TCS-6546, TCS-6953, TCS-7359, TCS-7272, TCS-7276, TCS-5793, TCS-6871, TCS-0465, TCS-6692, TCS-7274, TCS-6454, TCS-7225, TCS-3025, TCS-7278, TCS-5013, TCS-2732, TCS-4754, TCS-1138.

## Quantum computation and information

Quantum computational advantage leads, followed by robust quantum verification, ground-state structure, classical verification and distillability. Quantum coding, witness power and channel computability stay close. The Top 500 prefix spans algorithms, information, proofs, communication and storage; multiple oracle or proof-system variants come after their broader underlying barriers.

Previous prefix: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6518.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Quantum PCP conjecture with classical reductions](index.html#TCS-6446) (TCS-6446) | Local Hamiltonian hardness | 98 | A defining quantum-complexity conjecture connecting robust verification, approximation hardness, and the structure of many-body Hamiltonians. |
| 2 | [BPP versus BQP](index.html#TCS-0036) (TCS-0036) | Quantum computational advantage | 97 | A central foundational separation between classical and quantum efficient computation, with consequences for algorithms, simulation, and the computational interpretation of quantum mechanics. |
| 3 | [Area law for gapped two-dimensional Hamiltonians](index.html#TCS-6516) (TCS-6516) | Ground-state entanglement | 97 | A fundamental unresolved link between spectral gaps, geometric locality, entanglement, and the resources needed to describe quantum many-body ground states. |
| 4 | [Information-theoretic classical verification of quantum computation](index.html#TCS-6580) (TCS-6580) | Classical verification | 97 | A central quantum-complexity question connecting interactive proofs, delegation and the minimum resources needed to verify computations beyond classical simulation. |
| 5 | [NPT bound entanglement](index.html#TCS-6518) (TCS-6518) | Entanglement distillation | 96 | A central structural boundary in entanglement theory, with canonical finite-dimensional candidates and consequences for what quantum correlations can accomplish under local operations. |

Candidates considered: TCS-0036, TCS-6446, TCS-6516, TCS-6580, TCS-6518, TCS-0037, TCS-6448, TCS-6515, TCS-4615, TCS-6517, TCS-6520, TCS-6519, TCS-6521, TCS-2229, TCS-4952, TCS-6522, TCS-7308, TCS-3709, TCS-5077, TCS-6459, TCS-0029, TCS-4737, TCS-6933, TCS-1961, TCS-6449, TCS-0027, TCS-3275, TCS-4753, TCS-0034, TCS-4991, TCS-0033, TCS-2408, TCS-4457, TCS-4734, TCS-5202, TCS-1882, TCS-6481, TCS-1259, TCS-1324, TCS-4715, TCS-4894, TCS-0861, TCS-5021, TCS-4927, TCS-6447, TCS-0031, TCS-0862, TCS-4238, TCS-0030, TCS-4811, TCS-2707, TCS-0860.

## Computability and algorithmic information theory

Martin's conjecture and the equivalence of foundational randomness notions lead, with rigidity immediately adjacent in importance. Exact Busy Beaver and major definability and decidability questions precede resource-bounded information variants. Diversity distinguishes the two focus topics without demoting the central structure of Turing degrees.

Previous prefix: TCS-6646, TCS-6648.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Martin’s conjecture](index.html#TCS-6646) (TCS-6646) | Invariant degree-theoretic functions | 98 | A flagship conjecture about the global structure of Turing degrees and the classification of invariant computational operations. |
| 2 | [Kolmogorov–Loveland randomness versus Martin-Löf randomness](index.html#TCS-6648) (TCS-6648) | Algorithmic randomness | 96 | A defining open question linking computability, adaptive information access, fair betting and effective null tests; a resolution would settle the relationship between two foundational randomness notions. |

Candidates considered: TCS-6646, TCS-6648, TCS-6647, TCS-6685, TCS-6679, TCS-6649, TCS-6105, TCS-7193, TCS-5010, TCS-2202, TCS-0250, TCS-0247, TCS-0254, TCS-0238, TCS-0287, TCS-0279, TCS-4185, TCS-0240.

## Proof complexity

Strong proof lower bounds and the existence of a universal efficiently translatable proof system are the two leading themes. Frege and modular-Frege barriers stay immediately below. Proof search, bounded arithmetic and arithmetic-system strength diversify the Top 500 before narrower resolution resource refinements.

Previous prefix: TCS-6601, TCS-6663.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Superpolynomial Extended Frege lower bounds](index.html#TCS-6601) (TCS-6601) | Proof-length lower bounds | 99 | A defining open lower-bound problem for strong propositional reasoning, closely connected to bounded arithmetic, circuit complexity, and the limits of efficiently checkable certificates. |
| 2 | [Frege versus Extended Frege](index.html#TCS-6663) (TCS-6663) | Relative strength of proof systems | 97 | A canonical strong-system simulation problem, directly tied to Frege lower bounds, finite consistency and circuit-based reasoning. |

Candidates considered: TCS-6601, TCS-7162, TCS-0025, TCS-6602, TCS-6663, TCS-5332, TCS-1099, TCS-7273, TCS-0024, TCS-6770, TCS-1253, TCS-7163, TCS-1098, TCS-5333, TCS-5114, TCS-6771, TCS-4982, TCS-6766, TCS-5292, TCS-6759, TCS-1097, TCS-1096, TCS-2889, TCS-6768, TCS-6767, TCS-0071.

## Communication complexity and Boolean function analysis

Log-rank and Fourier entropy-influence remain the strongest complementary anchors. Universal structure theorems, randomized direct sums and interactive compression rank above fine quantitative refinements. Several formerly low-scored cards express general principles and move substantially upward after reading their exact targets.

Previous prefix: TCS-6603, TCS-6604.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Log-rank conjecture](index.html#TCS-6603) (TCS-6603) | Communication versus rank | 98 | A flagship structural conjecture linking deterministic protocols and matrix rank, with many equivalent combinatorial formulations and a large quantitative gap. |
| 2 | [Fourier Entropy–Influence conjecture](index.html#TCS-6604) (TCS-6604) | Fourier information and influence | 97 | A longstanding, broadly consequential conjecture in Boolean function analysis, with direct learning-theory implications and active 2026 progress that still leaves the universal classical inequality open. |

Candidates considered: TCS-6603, TCS-6604, TCS-6605, TCS-6581, TCS-5892, TCS-7219, TCS-6450, TCS-5326, TCS-6664, TCS-6710, TCS-1061, TCS-6708, TCS-1047, TCS-6707, TCS-2658, TCS-4771, TCS-1059, TCS-0540, TCS-3153, TCS-5272, TCS-6705, TCS-6711, TCS-2664, TCS-0811, TCS-2571, TCS-1845, TCS-5189, TCS-0218.

## Fine-grained complexity

SETH and the cubic APSP barrier remain the two anchors. The next positions cover independent foundations in 3SUM, OV, online products, convolution and gap hardness. Randomized or integer-weight variants retain substantial priority but follow the first representatives of similarly important barriers, so the Top 500 does not concentrate on repeated formulations.

Previous prefix: TCS-6595, TCS-6510.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strong Exponential Time Hypothesis](index.html#TCS-6595) (TCS-6595) | Satisfiability exponents | 99 | A principal organizing hypothesis of fine-grained complexity, connecting exact SAT complexity to tight running-time barriers across many algorithmic areas. |
| 2 | [Truly subcubic APSP](index.html#TCS-6510) (TCS-6510) | Weighted graph distances | 97 | Truly subcubic exact weighted APSP is a central fine-grained benchmark with consequences for a large family of graph and matrix problems. |

Candidates considered: TCS-6595, TCS-6510, TCS-0557, TCS-6596, TCS-6503, TCS-6598, TCS-6597, TCS-7313, TCS-6935, TCS-7179, TCS-6661, TCS-6937, TCS-6599, TCS-7270, TCS-0562, TCS-6946, TCS-5422, TCS-7373, TCS-6944, TCS-7347, TCS-6950, TCS-0815, TCS-6949, TCS-6025, TCS-6942, TCS-6945, TCS-0761, TCS-0560.

## Pseudorandomness and derandomization

The two fundamental resource equalities, P versus BPP and L versus BPL, lead. Explicit branching-program generators remain close, followed by independent construction frontiers in extraction, restricted isometries and expanders. General hardness-randomness principles outrank narrower parameter improvements; low historical scores do not hide canonical prime construction.

Previous prefix: TCS-0003, TCS-6600.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus BPP](index.html#TCS-0003) (TCS-0003) | General derandomization | 97 | The main general derandomization question for polynomial-time decision algorithms, with broad consequences for the role of randomness and for hardness-versus-randomness techniques. |
| 2 | [Optimal explicit pseudorandom generators for read-once branching programs](index.html#TCS-6600) (TCS-6600) | Space-bounded pseudorandomness | 97 | A central constructive route to L=BPL, with optimal nonconstructive seed length known and a persistent gap for uniform space-efficient generators despite advances in restricted and weighted models. |

Candidates considered: TCS-0003, TCS-0026, TCS-6600, TCS-7271, TCS-6662, TCS-6699, TCS-6686, TCS-6879, TCS-6696, TCS-1021, TCS-5341, TCS-6693, TCS-1005, TCS-5798, TCS-6689, TCS-6729, TCS-5287, TCS-1137, TCS-1956, TCS-1015, TCS-1125, TCS-1019, TCS-1022, TCS-1133, TCS-3958, TCS-1006, TCS-1016, TCS-0854, TCS-3986, TCS-1013, TCS-1014, TCS-1122, TCS-1131, TCS-1008, TCS-1018, TCS-4778, TCS-2201, TCS-1135, TCS-1124, TCS-1007.

## Parameterized complexity and algorithms

FPT versus W[1] and ETH remain the foundational anchors. Exact TSP, Subset Sum and Set Cover provide distinct exponential-time barriers. Structural recognition and general kernelization principles fill out the primary selection, including substantial preprocessing questions previously left at 50; specialized deletion and representation variants follow.

Previous prefix: TCS-6592, TCS-6593.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FPT versus \(\mathrm{W}[1]\)](index.html#TCS-6592) (TCS-6592) | Parameterized tractability | 99 | The defining unresolved tractability separation of parameterized complexity, with Clique as a precise and widely used complete problem. |
| 2 | [Exponential Time Hypothesis](index.html#TCS-6593) (TCS-6593) | Exact exponential algorithms | 98 | A foundational quantitative hardness hypothesis underlying exact, parameterized, graph, and geometric algorithm lower bounds. |

Candidates considered: TCS-6592, TCS-6593, TCS-7233, TCS-4790, TCS-6594, TCS-7241, TCS-6731, TCS-4695, TCS-6379, TCS-6660, TCS-0787, TCS-7035, TCS-2804, TCS-6974, TCS-6734, TCS-7312, TCS-0801, TCS-7181, TCS-6749, TCS-7023, TCS-0816, TCS-6728, TCS-3480, TCS-4289, TCS-5374, TCS-7022, TCS-7247, TCS-2662, TCS-6814, TCS-3917, TCS-4440, TCS-7027, TCS-1945, TCS-0808, TCS-0800, TCS-0597, TCS-0799.

## Approximation algorithms and inapproximability

Unique Games leads as a general organizing conjecture, with Densest k-Subgraph the complementary algorithmic flagship. Directed design, sparse cuts, routing, covering, submodularity and clustering populate the next priorities. Universal hardness and rounding principles precede narrower variants; LP gaps remain distinguished from the true approximation limits of all algorithms.

Previous prefix: TCS-6587, TCS-0006.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Constant-factor approximation for Densest k-Subgraph](index.html#TCS-6587) (TCS-6587) | Approximation algorithms for dense subgraphs | 97 | A flagship approximation problem with a simple objective, a large algorithmic gap, strong conditional and relaxation barriers, and consequences for several other optimization problems. |
| 2 | [Unique Games Conjecture](index.html#TCS-0006) (TCS-0006) | Hardness of approximation | 96 | An organizing conjecture for approximation thresholds, with consequences for whole families of constraint satisfaction problems and strong connections to SDP algorithms, PCPs, and analysis. |

Candidates considered: TCS-0006, TCS-6587, TCS-6588, TCS-7266, TCS-7282, TCS-7356, TCS-7160, TCS-5407, TCS-6659, TCS-1930, TCS-7281, TCS-6589, TCS-6591, TCS-7353, TCS-7358, TCS-6309, TCS-7357, TCS-5544, TCS-6757, TCS-5787, TCS-7380, TCS-7287, TCS-7318, TCS-6590, TCS-7354, TCS-6756, TCS-2625, TCS-0922, TCS-1168, TCS-5554.

## Online algorithms, scheduling and packing

The matroid secretary conjecture and unrelated-machine scheduling lead as complementary central problems in the merged category. Precedence, additive packing, server movement, geometric chasing and limited feedback stay near the top. Equivalent contention resolution follows its secretary representative; specialized regret and scheduling refinements do not dominate the prefix.

Previous prefix: TCS-6638.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Breaking two for unrelated-machine makespan](index.html#TCS-6638) (TCS-6638) | Heterogeneous-machine scheduling | 97 | A decades-old central scheduling problem with a large hardness gap, robust LP barriers and formal consequences for fair allocation. |
| 2 | [Breaking two for precedence-constrained makespan](index.html#TCS-6676) (TCS-6676) | Needs review | 96 | Unreviewed replacement |

Candidates considered: TCS-7316, TCS-6638, TCS-6676, TCS-6640, TCS-7317, TCS-6576, TCS-6577, TCS-0935, TCS-7319, TCS-6721, TCS-6724, TCS-1529, TCS-7335, TCS-5779, TCS-5221, TCS-5030, TCS-6078, TCS-1241, TCS-6836, TCS-0700, TCS-5252.

## Beyond worst-case and average-case analysis

Worst-case-to-average-case hardness and planted clique lead. Canonical inference, random satisfiability and smoothed local search follow, with the random-SAT search threshold restored to a priority reflecting its actual scope. Closely related hardness-amplification and specially chosen distribution variants follow these broad representatives.

Previous prefix: TCS-6656, TCS-0012.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Planted clique conjecture](index.html#TCS-6656) (TCS-6656) | Planted inference | 98 | A canonical computational threshold with broad consequences in average-case complexity, statistical inference, and the study of algorithmic lower-bound frameworks. |
| 2 | [Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0012) (TCS-0012) | Worst-case versus average-case hardness | 97 | One of the central missing implications in complexity theory, connecting worst-case lower bounds to feasible instance generation and the limits of algorithms on typical inputs. |

Candidates considered: TCS-0012, TCS-6656, TCS-7238, TCS-6657, TCS-6658, TCS-6684, TCS-4876, TCS-6453, TCS-6702, TCS-6703, TCS-5011, TCS-7148, TCS-5406.

## Sampling, Markov chains and mixing times

General coloring and fixed-margin sampling remain the complementary anchors. Critical dynamics, universal matroid rounding and cutoff follow; related Ising refinements are interleaved with other substantial sampling questions only within nearby importance levels. All nine active candidates remain within the category's Top 500 quota.

Previous prefix: TCS-6621, TCS-6622.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Rapid mixing of Glauber dynamics with \(\Delta +2\) colours](index.html#TCS-6621) (TCS-6621) | Colouring-chain mixing | 95 | A longstanding general-graph conjecture linking local algorithms, approximate counting and spin systems; recent near-threshold results still require structural restrictions. |
| 2 | [Kannan–Tetali–Vempala conjecture](index.html#TCS-6622) (TCS-6622) | Sampling prescribed-degree graphs | 94 | A central obstruction to a general theory of uniform sampling with fixed combinatorial marginals. |

Candidates considered: TCS-6621, TCS-6622, TCS-6668, TCS-2861, TCS-6843, TCS-6839, TCS-6857, TCS-6840, TCS-6851.

## Counting and enumeration

Exact counting complexity and #BIS lead. General perfect matchings, permanent derandomization and the two canonical output-sensitive enumeration problems follow closely. The primary selection also represents structural counting classifications and the decision-counting gap, rather than consisting entirely of individual FPRAS targets.

Previous prefix: TCS-6628, TCS-7221.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FPRAS for counting perfect matchings](index.html#TCS-6628) (TCS-6628) | Approximate counting | 97 | The major missing generalization of the permanent FPRAS, with an established obstruction to the direct Markov-chain approach and consequences beyond matchings. |
| 2 | [FPRAS for #BIS](index.html#TCS-7221) (TCS-7221) | Approximate counting | 97 | #BIS is the canonical intermediate approximate-counting problem: an FPRAS would resolve a central boundary shared by many spin-system and combinatorial counting tasks. |

Candidates considered: TCS-6820, TCS-7221, TCS-6628, TCS-6629, TCS-7112, TCS-7240, TCS-6821, TCS-7355, TCS-7320, TCS-7099, TCS-6671, TCS-1004, TCS-3635, TCS-4671, TCS-3037, TCS-7084, TCS-7086, TCS-7082.

## Graph algorithms

Lead with graph isomorphism and unrestricted exact matching. Rank broad algorithmic and structural barriers ahead of polylogarithmic refinements; the second girth formulation adds limited breadth beside the main conjecture.

Previous prefix: TCS-7222, TCS-6536.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Graph isomorphism in polynomial time](index.html#TCS-7222) (TCS-7222) | Graph isomorphism | 97 | A central unresolved graph decision problem whose polynomial-time complexity remains a foundational algorithmic target. |
| 2 | [Deterministic linear-time minimum spanning tree](index.html#TCS-6536) (TCS-6536) | Static graph algorithms | 96 | A foundational graph-algorithm question about the necessity of randomness and the relationship between comparison complexity and actual computation. |

Candidates considered: TCS-7222, TCS-6538, TCS-6539, TCS-6683, TCS-6536, TCS-6500, TCS-6511, TCS-7341, TCS-7346, TCS-2783, TCS-7377, TCS-7228, TCS-7263, TCS-7342, TCS-7343, TCS-7344, TCS-7345, TCS-7180, TCS-7348, TCS-0771, TCS-6655, TCS-7285, TCS-0775, TCS-0611, TCS-7244, TCS-0594.

## Data structures

Keep dynamic optimality and general static lower bounds at the front. Broad dictionary and lower-bound questions precede analyses of particular implementations and specialized persistence guarantees.

Previous prefix: TCS-6498, TCS-6540.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Dynamic optimality conjecture](index.html#TCS-6498) (TCS-6498) | Adaptive search trees | 97 | Dynamic optimality is a central benchmark for adaptive data structures: one simple online BST would compete with every offline BST on every access sequence. |
| 2 | [Superlogarithmic static cell-probe lower bounds](index.html#TCS-6540) (TCS-6540) | Static data-structure lower bounds | 96 | A model-wide challenge connecting algorithms, communication complexity, pseudorandomness and circuit lower bounds, with implications beyond any single geometric or graph problem. |

Candidates considered: TCS-6498, TCS-6540, TCS-7338, TCS-7331, TCS-6586, TCS-7334, TCS-0949, TCS-7333, TCS-5825, TCS-0300, TCS-7328, TCS-7340, TCS-7329, TCS-6508, TCS-0474, TCS-7327, TCS-7330.

## Dynamic algorithms

Connectivity remains the clearest foundational target. Near-optimal matching takes the second focus slot on comparable importance while adding a distinct optimization challenge; exact distances outrank narrower dynamic refinements.

Previous prefix: TCS-6625, TCS-6627.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Deterministic fully dynamic connectivity with polylogarithmic worst-case updates](index.html#TCS-6625) (TCS-6625) | Dynamic connectivity | 97 | A foundational dynamic-graph frontier directly relevant to data structures, with a new randomized breakthrough and an explicit remaining deterministic bottleneck. |
| 2 | [Fully dynamic near-optimal matching with polylogarithmic updates](index.html#TCS-6627) (TCS-6627) | Dynamic matching | 95 | A central dynamic graph problem connecting approximation, explicit solution maintenance and extremal induced-matching structure. |

Candidates considered: TCS-6625, TCS-6627, TCS-6626, TCS-6670, TCS-0478, TCS-5209, TCS-0543, TCS-7332, TCS-7339, TCS-0541, TCS-0387, TCS-7326, TCS-0545, TCS-0536, TCS-3331.

## String algorithms and computational biology

Use trace reconstruction and near-exact edit-distance approximation for the leading statistical and computational barriers. Compression and assembly rise above specialized indexing refinements; related edit-distance variants remain high without taking both focus slots.

Previous prefix: TCS-6623, TCS-6624.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Worst-case sample complexity of trace reconstruction](index.html#TCS-6623) (TCS-6623) | Reconstruction from noisy strings | 96 | A defining worst-case recovery problem for synchronization noise, linking string algorithms, information theory, statistics and complex-analytic methods. |
| 2 | [Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time](index.html#TCS-6624) (TCS-6624) | Sequence distance algorithms | 95 | A central remaining precision–runtime boundary for edit distance, distinct from the established n^{1+ε} constant-factor algorithms and from exact-computation hardness. |

Candidates considered: TCS-6623, TCS-7220, TCS-6624, TCS-6513, TCS-6669, TCS-7322, TCS-7371, TCS-7297, TCS-7367, TCS-6928, TCS-7374, TCS-7360, TCS-0467, TCS-0468, TCS-7366, TCS-7362, TCS-7369, TCS-7375, TCS-0470, TCS-7365, TCS-7364, TCS-7368, TCS-7370, TCS-7361, TCS-0466.

## Game theory, social choice and fair division

Put unrestricted EFX existence and truthful submodular auctions first: they are foundational feasibility and incentive barriers. Broad scheduling, allocation and representation questions follow before special-agent cases and narrower protocol variants.

Previous prefix: TCS-6632, TCS-0011.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Constant-factor universally truthful auctions for submodular bidders](index.html#TCS-6632) (TCS-6632) | Truthful mechanisms | 96 | A central multi-parameter mechanism-design problem linking truthful incentives, submodular optimization, information elicitation and the communication cost of welfare approximation. |
| 2 | [Existence of complete EFX allocations for additive valuations](index.html#TCS-0011) (TCS-0011) | Existence of fair allocations | 92 | A central existence question for a strong and widely studied fairness guarantee for indivisible goods. |

Candidates considered: TCS-0011, TCS-6632, TCS-6674, TCS-6639, TCS-6633, TCS-7379, TCS-6634, TCS-1115, TCS-0056, TCS-7197, TCS-7200, TCS-1116, TCS-1109, TCS-7196, TCS-1108, TCS-4584, TCS-7383, TCS-7203, TCS-0073, TCS-0571, TCS-1714.

## Algebraic computation

VP versus VNP leads, with matrix multiplication providing an equally consequential algorithmic direction. General PIT remains immediately behind; the next tier balances major lower-bound barriers with fundamental arithmetic and decidability questions before restricted models and overlapping formulations.

Previous prefix: TCS-0007, TCS-6611.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Matrix multiplication exponent](index.html#TCS-0007) (TCS-0007) | Matrix multiplication | 98 | One of the main questions in algebraic algorithms, governing a widely used primitive and many dependent complexity bounds. Both faster constructions and a superquadratic lower bound would have broad consequences. |
| 2 | [Permanent versus determinant](index.html#TCS-6611) (TCS-6611) | Algebraic representation lower bounds | 98 | The principal permanent-versus-determinant lower-bound problem, connecting algebraic computation, branching programs, geometry, and symmetry. |

Candidates considered: TCS-0005, TCS-0007, TCS-7113, TCS-6611, TCS-6666, TCS-6612, TCS-6613, TCS-6614, TCS-6641, TCS-7174, TCS-7262, TCS-0010, TCS-6888, TCS-7175, TCS-0055, TCS-6642, TCS-6677, TCS-6895, TCS-6615, TCS-6898, TCS-7223, TCS-1058, TCS-6890, TCS-6893, TCS-0009, TCS-2506, TCS-6616, TCS-5520, TCS-6897, TCS-1101, TCS-6883, TCS-6903, TCS-0481, TCS-3318, TCS-5260, TCS-2958, TCS-6884, TCS-7269, TCS-0046, TCS-5921, TCS-6882, TCS-2718, TCS-5240, TCS-1102, TCS-3959, TCS-6493, TCS-0047, TCS-7224, TCS-1103, TCS-1151, TCS-0095, TCS-2039, TCS-4523, TCS-1544, TCS-5739, TCS-2077, TCS-4350, TCS-4490, TCS-7372, TCS-1069.

## Lattices and computational number theory

Hilbert's tenth problem over the rationals and classical factoring are the leading landmarks. General lattice approximation follows closely; foundational algorithmic and hardness boundaries precede parameter-specific security reductions and refinements.

Previous prefix: TCS-6571, TCS-6667.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Hilbert’s tenth problem over the rationals](index.html#TCS-6571) (TCS-6571) | Diophantine decidability | 99 | A central unsolved decidability problem for an elementary, pervasive constraint language. A resolution would locate the computability boundary for rational polynomial feasibility. |
| 2 | [Polynomial-time, polynomial-factor approximation of Euclidean SVP](index.html#TCS-6667) (TCS-6667) | Lattice approximation | 97 | A fundamental worst-case algorithm question at the heart of lattice reduction, with a wide gap between current methods and the target and connections to cryptographic hardness. |

Candidates considered: TCS-6571, TCS-6617, TCS-6667, TCS-6618, TCS-7234, TCS-0655, TCS-7169, TCS-7265, TCS-6619, TCS-6620, TCS-6861, TCS-6863, TCS-0656, TCS-0658, TCS-0659, TCS-0662, TCS-0661, TCS-6864, TCS-5317, TCS-0652, TCS-0648, TCS-1170, TCS-5395, TCS-0657, TCS-7171, TCS-7170, TCS-0653.

## Coding and information theory

Lead with the binary rate-distance frontier and general broadcast capacity, covering coding and network information at comparable landmark importance. Rank actual targets: the retained deletion-channel card asks for formalizing a known finite approximation, rather than discovering the exact capacity curve.

Previous prefix: TCS-6606, TCS-1010.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Capacity of the two-user Gaussian interference channel](index.html#TCS-6606) (TCS-6606) | Multiuser channel capacity | 97 | A central continuous-alphabet interference tradeoff, with a fully specified weighted-capacity target and the saved uncertainty about recent claims preserved. |
| 2 | [Optimal asymptotic binary rate–distance tradeoff](index.html#TCS-1010) (TCS-1010) | Coding rate versus distance | 96 | The fundamental asymptotic binary coding tradeoff; its well-defined rate curve is restored as a distinct coding-theory focus alongside multiuser communication. |

Candidates considered: TCS-1010, TCS-6665, TCS-7210, TCS-1020, TCS-6584, TCS-6606, TCS-6608, TCS-7267, TCS-0013, TCS-6609, TCS-7211, TCS-7214, TCS-7215, TCS-1012, TCS-6738, TCS-4524, TCS-4968, TCS-1011, TCS-6610, TCS-3513, TCS-0196, TCS-4802, TCS-0184, TCS-0187, TCS-0205, TCS-0178, TCS-6607.

## Property testing and distribution learning

The general testing-versus-estimation implication leads. Unrestricted Gaussian-mixture density learning takes the second slot at comparable importance to graph-testing classification, adding the category's major statistical-computational frontier rather than a second graph-only focus.

Previous prefix: TCS-6630, TCS-1033.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Effective classification of polynomially testable hereditary graph properties](index.html#TCS-6630) (TCS-6630) | Graph property classification | 95 | An effective formulation of the major finite-family classification problem; it separates polynomial sampling from mere testability and abstract quantitative equivalences. |
| 2 | [Polynomial testability versus distance estimation](index.html#TCS-1033) (TCS-1033) | Testing versus distance estimation | 96 | A universal polynomial tester-to-estimator implication would convert robust graph-property recognition into quantitative distance measurement across the dense model. |

Candidates considered: TCS-1033, TCS-5443, TCS-6630, TCS-1029, TCS-6672, TCS-0848, TCS-5085, TCS-2535, TCS-1030, TCS-4259, TCS-5210, TCS-3906, TCS-4376, TCS-0672, TCS-0847, TCS-0841.

## Differential privacy

Prioritize general private-learning sample bounds and efficient release of all marginals. They address broader statistical and computational limits than sharp rates for a single continual or online primitive.

Previous prefix: TCS-0506, TCS-6673.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Private PAC sample complexity from VC and Littlestone dimensions](index.html#TCS-0506) (TCS-0506) | Private learnability | 88 | Seeks a quantitative sample-complexity characterization of private learnability in terms of two basic dimensions, with consequences across hypothesis classes. |
| 2 | [Optimal error for pure-DP continual counting](index.html#TCS-6673) (TCS-6673) | Private continual counting | 94 | The saved target asks for optimal worst-time error when releasing every prefix sum under pure differential privacy. It complements sample-complexity bounds for private learning with a fundamental sequential data-release problem. |

Candidates considered: TCS-0506, TCS-7236, TCS-6673, TCS-0507.

## Constraint satisfaction

Retain finite promise-CSP and infinite-domain CSP dichotomies as the broadest organizing questions. General search, expressibility and classification frontiers precede individual colouring gaps and restricted relaxations.

Previous prefix: TCS-6635, TCS-6636.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Finite-domain promise CSP dichotomy](index.html#TCS-6635) (TCS-6635) | Finite promise constraints | 98 | A broad structural question extending the finite CSP dichotomy into approximation and promise problems, with connections to algebra, topology, and optimization. |
| 2 | [Bodirsky–Pinsker conjecture](index.html#TCS-6636) (TCS-6636) | Infinite-domain constraints | 97 | A central unifying conjecture about the boundary of polynomial-time constraint solving, with broad logical scope and active links to promise CSPs. |

Candidates considered: TCS-6635, TCS-6636, TCS-6637, TCS-6675, TCS-6748, TCS-7116, TCS-1173, TCS-6725, TCS-3678, TCS-1807, TCS-0504, TCS-1555, TCS-0441, TCS-1978, TCS-7237, TCS-3984, TCS-3585, TCS-0444.

## Automated reasoning, rewriting and unification

Lead with length-constrained word equations and Presburger arithmetic with primes, two broad decidability boundaries with distinct string and arithmetic content. General complexity and solver-power questions precede narrower matching orders and representation variants.

Previous prefix: TCS-6562, TCS-6643.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Word equations with linear length constraints](index.html#TCS-6562) (TCS-6562) | Word equations with arithmetic | 97 | A longstanding decidability question at the intersection of formal languages, number-theoretic constraints and automated verification; even unrestricted termination is unknown, before asking for efficient algorithms. |
| 2 | [Decidability of unification in the basic modal logic K](index.html#TCS-6643) (TCS-6643) | Modal unification | 94 | The basic unresolved decidability boundary in modal unification, already in the minimal normal modal logic. |

Candidates considered: TCS-6562, TCS-1992, TCS-6643, TCS-0163, TCS-6644, TCS-7239, TCS-6650, TCS-7194, TCS-0306, TCS-7125, TCS-1595, TCS-7134, TCS-0114, TCS-5603.

## Database theory and finite model theory

A logic capturing P and Asser's spectrum problem lead as foundational descriptive-complexity questions. Broad model-checking and database-query boundaries follow closely; specific width, representation and convergence refinements come later.

Previous prefix: TCS-6678, TCS-6645.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FO model checking on hereditary monadically dependent graph classes](index.html#TCS-6678) (TCS-6678) | Finite-model-theoretic tractability | 96 | The central proposed tractability boundary for first-order model checking on hereditary graph classes, connecting database queries, model theory, sparsity and dense graph structure. |
| 2 | [Constant-delay conjunctive-query classification](index.html#TCS-6645) (TCS-6645) | Database query enumeration | 95 | A central database-theory classification question: identify exactly which fixed queries permit optimal preprocessing and delay, including the self-joins excluded by classical dichotomies. |

Candidates considered: TCS-7195, TCS-7232, TCS-6678, TCS-6645, TCS-0492, TCS-6680, TCS-6372, TCS-3631, TCS-0488, TCS-0505, TCS-0494, TCS-7128, TCS-4458, TCS-0499, TCS-4995, TCS-0502, TCS-3557, TCS-0487, TCS-0482.

## Miscellaneous

The sunflower conjecture leads for its broad combinatorial and complexity consequences. Seese's conjecture follows as a distinct logic-structure boundary; the comparison-balance conjecture remains substantial but narrower.

Previous prefix: TCS-7177, TCS-6654.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [\(1/3\)–\(2/3\) conjecture](index.html#TCS-7177) (TCS-7177) | Partial-order balance | 90 | Would provide a universally informative comparison for sorting with partial-order information; retained as a computationally motivated combinatorial exception. |
| 2 | [Seese’s conjecture](index.html#TCS-6654) (TCS-6654) | Logical decidability and graph structure | 95 | Seese directly connects decidability of monadic second-order satisfiability with bounded clique-width; retain this major computability/structure boundary question as a cross-disciplinary exception. |

Candidates considered: TCS-7290, TCS-6654, TCS-7177.
