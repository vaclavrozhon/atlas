# Benchmark selection review

Reviewed on 2026-09-18 across 35 categories.

Our primary goal is a benchmark of 500 problems. Top 100 is a priority subset of those same 500, with secondary editorial attention. Both use the same category order and the same ranking within each category. The existing Top 1000 view is not an active benchmark goal.

Individual category-wide review of every active card, reading its title, formal target and significance, with additional saved context where needed. Scientific importance is primary: foundational scope, breadth of consequences and influence on other questions. Topical diversity distinguishes comparably important candidates in the focus prefix. Every card receives a fresh score assessment and an individual reason; the remaining order follows these scores. Nearby scores are editorial priorities rather than precise measurements. In the live reader, shared vote scores remain primary and the editorial order only breaks ties. This review does not recertify open status or formulation quality.

Top 100 takes the first 5/2 places in each large/small category. Top 500 takes the first 25/10 and the legacy Top 1000 view takes the first 50/20 places from the same order. Top 100 is contained in Top 500, which is contained in Top 1000. Focus places prioritize scientific importance, using topical diversity among comparably important candidates; remaining places retain score order. None of these subsets certifies current open status.

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

## Computational complexity

Foundational barriers lead: efficient verification, unrestricted nonuniform lower bounds, polynomial space, logarithmic-space nondeterminism, and metacomplexity. Diversity only separates nearby priorities; related P-versus-NP and circuit questions remain high in the full ranking. General resource simulations and total-search structure precede narrower representation and closure questions.

Previous prefix: TCS-0001, TCS-6530, TCS-6531, TCS-6535, TCS-6534.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NP](index.html#TCS-0001) (TCS-0001) | Nondeterministic computation | 100 | The defining question about efficient computation and verification, with consequences across the entire catalogue. |
| 2 | [NP versus P/poly](index.html#TCS-0021) (TCS-0021) | Unrestricted circuit lower bounds | 99 | The central unrestricted circuit separation for NP, strengthening the uniform tractability barrier. |
| 3 | [P versus PSPACE](index.html#TCS-6530) (TCS-6530) | Time versus space | 98 | A foundational time-versus-space separation governing quantified reasoning, games and verification. |
| 4 | [L versus NL](index.html#TCS-0004) (TCS-0004) | Logarithmic-space nondeterminism | 97 | The canonical deterministic-versus-nondeterministic memory question, expressed by directed reachability. |
| 5 | [Minimum Circuit Size Problem](index.html#TCS-4786) (TCS-4786) | Metacomplexity | 96 | A central metacomplexity classification connecting circuit lower bounds, learning and cryptography. |

Candidates considered: TCS-0001, TCS-0021, TCS-6530, TCS-0004, TCS-4786, TCS-0002, TCS-0015, TCS-6532, TCS-6531, TCS-6535, TCS-0020, TCS-4988, TCS-6977, TCS-0016, TCS-7158, TCS-0017, TCS-7161, TCS-7286, TCS-7363, TCS-1056, TCS-6534, TCS-6743, TCS-6817, TCS-7321, TCS-0018, TCS-0293, TCS-2333, TCS-6533, TCS-7256, TCS-7268, TCS-1054, TCS-6934, TCS-6979, TCS-7382, TCS-0019, TCS-6747, TCS-7378, TCS-7381, TCS-5593, TCS-6091, TCS-6168, TCS-6455, TCS-7159, TCS-1053, TCS-6714, TCS-7257, TCS-0303, TCS-1052, TCS-6006, TCS-6285, TCS-0297, TCS-0298, TCS-0301, TCS-2681, TCS-4746, TCS-6681, TCS-7243, TCS-1040, TCS-2532, TCS-3886, TCS-2425, TCS-7260, TCS-0305, TCS-2215, TCS-3862, TCS-6139, TCS-1602, TCS-2029, TCS-1035, TCS-1036, TCS-1034, TCS-0310.

## Algorithms

Lead with basic algorithmic primitives and broad compression principles. Sorting, output-sensitive Subset Sum, hypergraph cuts, additive distances and implicit representations provide distinct high-value directions. Structural classification questions remain ahead of specialized runtime refinements; historical scores of 50 do not discount substantial routing and reconstruction problems.

Previous prefix: TCS-6537, TCS-0388, TCS-0946, TCS-1141.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Expected linear-time integer sorting for every word length](index.html#TCS-6537) (TCS-6537) | Integer sorting | 96 | A foundational uniform linear-time sorting endpoint across all machine word lengths. |
| 2 | [Near-linear output-sensitive Subset Sum](index.html#TCS-7350) (TCS-7350) | Pseudopolynomial exact algorithms | 92 | Tests whether exact dynamic programming can attain input-plus-output complexity. |
| 3 | [Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges](index.html#TCS-0946) (TCS-0946) | Combinatorial sparsification | 91 | A general optimal compression principle for all hypergraph cuts. |
| 4 | [Optimal size of four-additive graph spanners](index.html#TCS-6783) (TCS-6783) | Distance-preserving sparse graphs | 90 | The central constant-additive distance sparsity gap. |
| 5 | [Small Implicit Graph Conjecture](index.html#TCS-5705) (TCS-5705) | Implicit graph representations | 89 | Connects global graph compressibility with local adjacency decoding. |

Candidates considered: TCS-6537, TCS-7350, TCS-0946, TCS-6783, TCS-5705, TCS-0388, TCS-1338, TCS-6251, TCS-6785, TCS-2018, TCS-4417, TCS-6421, TCS-1617, TCS-5969, TCS-7351, TCS-3263, TCS-3346, TCS-6270, TCS-6784, TCS-7075, TCS-7146, TCS-1141, TCS-7061, TCS-6173, TCS-2822, TCS-0538, TCS-0809.

## Automata and formal languages

The principal finite-state and language-expression landmarks lead. Higher-order recursive equivalence joins synchronization, two-way nondeterminism, star height and dot depth in the prefix. Tree transformations, logical definability and unique parsing follow closely; quantitative, timed and cellular models broaden the rest without displacing stronger foundational questions.

Previous prefix: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6563.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Maximum reset threshold of synchronizing automata](index.html#TCS-6558) (TCS-6558) | Synchronization | 98 | The central extremal synchronization problem for finite-state control. |
| 2 | [Sakoda–Sipser problem](index.html#TCS-6560) (TCS-6560) | Two-way nondeterminism | 97 | A principal succinctness barrier for nondeterminism and two-way input access. |
| 3 | [Generalized star-height problem](index.html#TCS-6559) (TCS-6559) | Regular-expression complexity | 96 | A fundamental unresolved depth boundary for regular expressions with complement. |
| 4 | [Decidability of every level of the dot-depth hierarchy](index.html#TCS-6561) (TCS-6561) | Logical language hierarchies | 95 | Effective recognition throughout a central logical alternation hierarchy. |
| 5 | [Equivalence of deterministic higher-order recursion schemes](index.html#TCS-6582) (TCS-6582) | Higher-order language equivalence | 94 | Exact behavioral equivalence for unrestricted finite higher-order recursive descriptions. |

Candidates considered: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6582, TCS-6563, TCS-6564, TCS-0164, TCS-7261, TCS-5904, TCS-7309, TCS-3863, TCS-0135, TCS-0154, TCS-0167, TCS-6064, TCS-4575, TCS-5959, TCS-0146, TCS-5651, TCS-2243, TCS-0138, TCS-5863, TCS-5738, TCS-0128, TCS-4677, TCS-3378, TCS-0136, TCS-4636, TCS-4659, TCS-0133.

## Semantics, logic and verification

Parity games, Skolem decidability, real exponentiation and stochastic games are the broadest algorithmic landmarks. Internal semisimplicial types represents foundational expressiveness among nearby priorities. Positivity and mean-payoff games remain immediately below rather than filling the prefix with related dynamics and game variants; general logical and program-equivalence boundaries precede dimension-specific refinements.

Previous prefix: TCS-6565, TCS-6567, TCS-6569, TCS-6570, TCS-6583.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Parity games in polynomial time](index.html#TCS-4245) (TCS-4245) | Game solving and verification | 99 | A central efficient-verification barrier linking parity games and modal fixed-point logic. |
| 2 | [Skolem problem](index.html#TCS-5773) (TCS-5773) | Recurrence reachability | 98 | A canonical exact arithmetic reachability problem underlying many verification reductions. |
| 3 | [Tarski’s exponential function problem](index.html#TCS-7230) (TCS-7230) | Decidability of real arithmetic | 97 | The fundamental decidability boundary obtained by adding real exponentiation. |
| 4 | [Simple stochastic games in polynomial time](index.html#TCS-6567) (TCS-6567) | Stochastic game solving | 96 | A canonical efficient decision problem combining adversarial control and randomness. |
| 5 | [Internal semisimplicial types in ordinary HoTT](index.html#TCS-6569) (TCS-6569) | Dependent type theory | 95 | Tests ordinary homotopy type theory's ability to express unbounded coherent structure. |

Candidates considered: TCS-4245, TCS-5773, TCS-7230, TCS-6567, TCS-6569, TCS-6565, TCS-6568, TCS-7192, TCS-6570, TCS-7157, TCS-6566, TCS-6583, TCS-1649, TCS-7153, TCS-5915, TCS-5682, TCS-5987, TCS-4302, TCS-6245, TCS-3655, TCS-6359, TCS-5817, TCS-7154, TCS-0632, TCS-7310, TCS-6036, TCS-3031, TCS-6112, TCS-5975, TCS-2033, TCS-4017, TCS-0913, TCS-0896, TCS-0901, TCS-1659, TCS-0619, TCS-0092.

## Distributed, parallel and sublinear algorithms

General parallelizability leads, followed by deterministic matching, distributed locality, streaming reachability and unconditional bandwidth lower bounds. Work-efficient reachability and flow remain very high. The full selection also represents MPC, shared-memory synchronization, local computation and sketches; small logarithmic or model-specific refinements follow broader barriers.

Previous prefix: TCS-6553, TCS-6556, TCS-6504, TCS-6554, TCS-6555.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NC](index.html#TCS-6553) (TCS-6553) | Parallelizability | 99 | The defining question of whether efficient computation can be inherently sequential. |
| 2 | [Perfect matching in NC](index.html#TCS-6504) (TCS-6504) | Parallel algebraic derandomization | 96 | A central derandomization barrier for parallel combinatorial optimization. |
| 3 | [Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds](index.html#TCS-6554) (TCS-6554) | Local distributed symmetry breaking | 95 | A widely reusable locality primitive governing distributed complexity scales. |
| 4 | [Directed reachability with nearly linear memory and polylogarithmic passes](index.html#TCS-6556) (TCS-6556) | Streaming reachability | 94 | A fundamental memory-versus-passes question for global directed connectivity. |
| 5 | [Explicit superconstant lower bounds in the congested clique](index.html#TCS-6557) (TCS-6557) | Distributed communication lower bounds | 94 | A basic unconditional lower-bound barrier in a powerful communication model. |

Candidates considered: TCS-6553, TCS-6504, TCS-6554, TCS-6556, TCS-6557, TCS-6507, TCS-7349, TCS-6505, TCS-6499, TCS-6555, TCS-7172, TCS-6506, TCS-7336, TCS-0984, TCS-0998, TCS-0515, TCS-0954, TCS-0950, TCS-0969, TCS-4274, TCS-0940, TCS-0986, TCS-7010, TCS-0522, TCS-3792, TCS-5795, TCS-0980, TCS-6501, TCS-5797, TCS-7259, TCS-7337, TCS-0519, TCS-3075, TCS-7376, TCS-0524, TCS-0993, TCS-2233, TCS-6380, TCS-0469, TCS-4763, TCS-1588, TCS-3381, TCS-6080, TCS-6206, TCS-0994, TCS-3384, TCS-0985, TCS-0834, TCS-0849.

## Optimization and numerical computation

Strongly polynomial LP, general sparse linear systems, exact SDP, Komlos discrepancy and simplex complexity form the strongest distinct optimization barriers. Broad integer and complementarity primitives follow. Named constructions do not automatically outrank general optimization principles, and refined runtime or oracle tradeoffs are ordered by the scope of their consequences.

Previous prefix: TCS-0008, TCS-6574, TCS-7227, TCS-6585, TCS-6578.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strongly polynomial linear programming](index.html#TCS-0008) (TCS-0008) | Linear programming complexity | 99 | The defining arithmetic-complexity question for general linear optimization. |
| 2 | [Nearly linear-time solution of general sparse linear systems](index.html#TCS-6585) (TCS-6585) | Numerical linear algebra | 97 | A ubiquitous numerical primitive at near-input cost under moderate conditioning. |
| 3 | [Exact semidefinite feasibility in polynomial time](index.html#TCS-6574) (TCS-6574) | Exact semidefinite optimization | 96 | The fundamental exact bit-complexity boundary for semidefinite constraints. |
| 4 | [Komlós conjecture](index.html#TCS-7314) (TCS-7314) | Vector balancing and discrepancy | 96 | A central dimension-independent rounding principle with broad discrepancy consequences. |
| 5 | [Polynomial-time simplex pivot rule](index.html#TCS-6572) (TCS-6572) | Simplex algorithm complexity | 95 | A polynomial simplex method would reconcile a central algorithm with worst-case guarantees. |

Candidates considered: TCS-0008, TCS-6585, TCS-6574, TCS-7314, TCS-6572, TCS-7264, TCS-7231, TCS-7315, TCS-7283, TCS-7227, TCS-6483, TCS-0722, TCS-6578, TCS-7226, TCS-7298, TCS-0724, TCS-7007, TCS-5330, TCS-0491, TCS-0728, TCS-0687, TCS-0725, TCS-0914, TCS-0673.

## Geometry, topology and metric spaces

The prefix spans convex concentration, metric distortion, polyhedral paths, planar extremal geometry and algorithmic topology. Basic topology decidability questions formerly carrying low scores move near the top. Broad geometric primitives and compression principles precede finer certificate variants and specialized representation targets.

Previous prefix: TCS-6523, TCS-6525, TCS-6528, TCS-6573, TCS-0318.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Kannan–Lovász–Simonovits conjecture](index.html#TCS-6523) (TCS-6523) | Convex concentration | 99 | A central dimension-free principle governing convex concentration, sampling and optimization. |
| 2 | [Gupta–Newman–Rabinovich–Sinclair conjecture](index.html#TCS-6525) (TCS-6525) | Metric embeddings | 96 | A major metric-embedding and flow-cut principle for excluded-minor families. |
| 3 | [Polynomial Hirsch conjecture](index.html#TCS-6573) (TCS-6573) | Polytope geometry | 95 | A universal structural barrier underlying routes through linear-programming feasible regions. |
| 4 | [Planar k-set extremal function](index.html#TCS-0318) (TCS-0318) | Planar extremal geometry | 94 | A defining planar extremal gap controlling geometric levels and algorithmic complexity. |
| 5 | [Unknot recognition in polynomial time](index.html#TCS-6528) (TCS-6528) | Computational topology | 94 | A foundational efficient-recognition problem for topological triviality. |

Candidates considered: TCS-6523, TCS-6525, TCS-6573, TCS-0318, TCS-6528, TCS-7242, TCS-6199, TCS-6524, TCS-6526, TCS-7292, TCS-6527, TCS-0406, TCS-7184, TCS-0403, TCS-6880, TCS-0973, TCS-7006, TCS-0408, TCS-0410, TCS-0381, TCS-0411, TCS-7182, TCS-0417, TCS-0970, TCS-0382, TCS-0427, TCS-0377, TCS-0416, TCS-0990, TCS-0398, TCS-0419, TCS-0327, TCS-0430, TCS-7189, TCS-0432, TCS-0428, TCS-0340, TCS-4454, TCS-3059, TCS-0409.

## Learning theory

Distribution-free DNF learning, universal sample compression and noisy parity are the defining landmarks. The prefix also includes the learning-to-cryptography bridge and statistically separated Gaussian mixtures; these broaden the leading questions without excluding juntas and halfspaces from the next positions. General computational and statistical principles precede narrower compression conventions or model-specific refinements.

Previous prefix: TCS-6541, TCS-6542, TCS-6543, TCS-5358.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Polynomial-time distribution-free PAC learning of DNF](index.html#TCS-5358) (TCS-5358) | Distribution-free Boolean rule learning | 98 | A defining computational PAC-learning problem covering many compact Boolean representations. |
| 2 | [Linear-size sample compression](index.html#TCS-6541) (TCS-6541) | Sample compression | 98 | A universal principle connecting statistical dimension with lossless sample representation. |
| 3 | [Learning parity with noise in polynomial time](index.html#TCS-6542) (TCS-6542) | Learning with noise | 97 | A canonical noise-induced computational barrier linking learning, decoding and cryptography. |
| 4 | [One-way functions from hardness of learning P/poly](index.html#TCS-5090) (TCS-5090) | Learning hardness and cryptography | 94 | A broad converse linking general learning hardness to one-way functions. |
| 5 | [Efficient learning of well-separated Gaussian mixtures](index.html#TCS-3391) (TCS-3391) | Computational mixture learning | 93 | A central statistical-versus-computational gap for growing latent-variable models. |

Candidates considered: TCS-5358, TCS-6541, TCS-6542, TCS-5090, TCS-3391, TCS-6543, TCS-7293, TCS-1573, TCS-5088, TCS-2336, TCS-7294, TCS-5119, TCS-6544, TCS-4592, TCS-5847, TCS-2339, TCS-5087, TCS-5902, TCS-3117, TCS-4186, TCS-1539, TCS-5031, TCS-4792, TCS-5434, TCS-0670, TCS-3177, TCS-3691, TCS-0677, TCS-3787, TCS-0664, TCS-0683, TCS-0682, TCS-3689, TCS-0671, TCS-0694, TCS-0689.

## Cryptography

Start with the existence and minimal foundations of cryptography. Public-key encryption from one-wayness, worst-case-to-average-case hardness, obfuscation and oblivious transfer are comparably consequential distinct barriers. Related existence and encryption-strengthening variants remain high; information-theoretic primitives add diversity only after the stronger general assumption questions.

Previous prefix: TCS-6545, TCS-0022, TCS-6550, TCS-6551, TCS-0465.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Existence of one-way functions](index.html#TCS-7167) (TCS-7167) | Existence of cryptographic hardness | 100 | The unconditional existence of cryptography's basic computational asymmetry. |
| 2 | [Public-key encryption from one-way functions](index.html#TCS-6545) (TCS-6545) | Public-key foundations | 98 | The central gap between minimal symmetric hardness and public-key confidentiality. |
| 3 | [One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0022) (TCS-0022) | Complexity foundations of cryptography | 98 | Connects worst-case verification hardness to average-case cryptographic security. |
| 4 | [Circuit obfuscation from polynomial-hard LWE](index.html#TCS-6550) (TCS-6550) | Program obfuscation | 97 | Grounds general-purpose obfuscation in one standard quantitative lattice assumption. |
| 5 | [Oblivious transfer from public-key encryption](index.html#TCS-6549) (TCS-6549) | Foundations of secure computation | 96 | Tests whether secure communication already supports general private computation. |

Candidates considered: TCS-7167, TCS-6545, TCS-0022, TCS-6550, TCS-6549, TCS-7168, TCS-7229, TCS-6547, TCS-6551, TCS-6552, TCS-6548, TCS-7277, TCS-6546, TCS-6953, TCS-7359, TCS-7272, TCS-7276, TCS-5793, TCS-6871, TCS-0465, TCS-6692, TCS-7274, TCS-6454, TCS-7225, TCS-3025, TCS-7278, TCS-5013, TCS-2732, TCS-4754, TCS-1138.

## Quantum computation and information

Quantum computational advantage leads, followed by robust quantum verification, ground-state structure, classical verification and distillability. Quantum coding, witness power and channel computability stay close. The Top 500 prefix spans algorithms, information, proofs, communication and storage; multiple oracle or proof-system variants come after their broader underlying barriers.

Previous prefix: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6518.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [BPP versus BQP](index.html#TCS-0036) (TCS-0036) | Quantum computational advantage | 99 | The defining unconditional separation between efficient quantum and classical randomized computation. |
| 2 | [Quantum PCP conjecture with classical reductions](index.html#TCS-6446) (TCS-6446) | Local Hamiltonian hardness | 98 | A central robust quantum-verification conjecture for local energy estimation. |
| 3 | [Area law for gapped two-dimensional Hamiltonians](index.html#TCS-6516) (TCS-6516) | Ground-state entanglement | 97 | A universal structural principle for entanglement in gapped two-dimensional matter. |
| 4 | [Information-theoretic classical verification of quantum computation](index.html#TCS-6580) (TCS-6580) | Classical verification | 96 | Determines whether classical users can verify one efficient quantum server without computational assumptions. |
| 5 | [NPT bound entanglement](index.html#TCS-6518) (TCS-6518) | Entanglement distillation | 96 | A defining all-copy boundary between entanglement and distillable quantum resources. |

Candidates considered: TCS-0036, TCS-6446, TCS-6516, TCS-6580, TCS-6518, TCS-0037, TCS-6448, TCS-6515, TCS-4615, TCS-6517, TCS-6520, TCS-6519, TCS-6521, TCS-2229, TCS-4952, TCS-6522, TCS-7308, TCS-3709, TCS-5077, TCS-6459, TCS-0029, TCS-4737, TCS-6933, TCS-1961, TCS-6449, TCS-0027, TCS-3275, TCS-4753, TCS-0034, TCS-4991, TCS-0033, TCS-2408, TCS-4457, TCS-4734, TCS-5202, TCS-1882, TCS-6481, TCS-1259, TCS-1324, TCS-4715, TCS-4894, TCS-0861, TCS-5021, TCS-4927, TCS-6447, TCS-0031, TCS-0862, TCS-4238, TCS-0030, TCS-4811, TCS-2707, TCS-0860.

## Computability and algorithmic information theory

Martin's conjecture and the equivalence of foundational randomness notions lead, with rigidity immediately adjacent in importance. Exact Busy Beaver and major definability and decidability questions precede resource-bounded information variants. Diversity distinguishes the two focus topics without demoting the central structure of Turing degrees.

Previous prefix: TCS-6646, TCS-6648.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Martin’s conjecture](index.html#TCS-6646) (TCS-6646) | Invariant degree-theoretic functions | 98 | A central structural classification of invariant operations on computational degrees. |
| 2 | [Kolmogorov–Loveland randomness versus Martin-Löf randomness](index.html#TCS-6648) (TCS-6648) | Algorithmic randomness | 96 | Compares two foundational definitions of effective unpredictability. |

Candidates considered: TCS-6646, TCS-6648, TCS-6647, TCS-6685, TCS-6679, TCS-6649, TCS-6105, TCS-7193, TCS-5010, TCS-2202, TCS-0250, TCS-0247, TCS-0254, TCS-0238, TCS-0287, TCS-0279, TCS-4185, TCS-0240.

## Proof complexity

Strong proof lower bounds and the existence of a universal efficiently translatable proof system are the two leading themes. Frege and modular-Frege barriers stay immediately below. Proof search, bounded arithmetic and arithmetic-system strength diversify the Top 500 before narrower resolution resource refinements.

Previous prefix: TCS-6601, TCS-6663.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Superpolynomial Extended Frege lower bounds](index.html#TCS-6601) (TCS-6601) | Proof-length lower bounds | 99 | A defining lower-bound barrier for powerful propositional reasoning with reusable definitions. |
| 2 | [Existence of p-optimal proof systems](index.html#TCS-7162) (TCS-7162) | Universal proof systems | 97 | Tests whether one efficient proof formalism can absorb all others. |

Candidates considered: TCS-6601, TCS-7162, TCS-0025, TCS-6602, TCS-6663, TCS-5332, TCS-1099, TCS-7273, TCS-0024, TCS-6770, TCS-1253, TCS-7163, TCS-1098, TCS-5333, TCS-5114, TCS-6771, TCS-4982, TCS-6766, TCS-5292, TCS-6759, TCS-1097, TCS-1096, TCS-2889, TCS-6768, TCS-6767, TCS-0071.

## Communication complexity and Boolean function analysis

Log-rank and Fourier entropy-influence remain the strongest complementary anchors. Universal structure theorems, randomized direct sums and interactive compression rank above fine quantitative refinements. Several formerly low-scored cards express general principles and move substantially upward after reading their exact targets.

Previous prefix: TCS-6603, TCS-6604.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Log-rank conjecture](index.html#TCS-6603) (TCS-6603) | Communication versus rank | 99 | The central proposed algebraic characterization of efficient exact communication. |
| 2 | [Fourier Entropy–Influence conjecture](index.html#TCS-6604) (TCS-6604) | Fourier information and influence | 98 | A universal relation between Boolean spectral information and sensitivity. |

Candidates considered: TCS-6603, TCS-6604, TCS-6605, TCS-6581, TCS-5892, TCS-7219, TCS-6450, TCS-5326, TCS-6664, TCS-6710, TCS-1061, TCS-6708, TCS-1047, TCS-6707, TCS-2658, TCS-4771, TCS-1059, TCS-0540, TCS-3153, TCS-5272, TCS-6705, TCS-6711, TCS-2664, TCS-0811, TCS-2571, TCS-1845, TCS-5189, TCS-0218.

## Fine-grained complexity

SETH and the cubic APSP barrier remain the two anchors. The next positions cover independent foundations in 3SUM, OV, online products, convolution and gap hardness. Randomized or integer-weight variants retain substantial priority but follow the first representatives of similarly important barriers, so the Top 500 does not concentrate on repeated formulations.

Previous prefix: TCS-6595, TCS-6510.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strong Exponential Time Hypothesis](index.html#TCS-6595) (TCS-6595) | Satisfiability exponents | 99 | A principal foundation of tight conditional algorithmic lower bounds. |
| 2 | [Truly subcubic APSP](index.html#TCS-6510) (TCS-6510) | Weighted graph distances | 98 | A central exact graph-distance barrier with a wide equivalence network. |

Candidates considered: TCS-6595, TCS-6510, TCS-0557, TCS-6596, TCS-6503, TCS-6598, TCS-6597, TCS-7313, TCS-6935, TCS-7179, TCS-6661, TCS-6937, TCS-6599, TCS-7270, TCS-0562, TCS-6946, TCS-5422, TCS-7373, TCS-6944, TCS-7347, TCS-6950, TCS-0815, TCS-6949, TCS-6025, TCS-6942, TCS-6945, TCS-0761, TCS-0560.

## Pseudorandomness and derandomization

The two fundamental resource equalities, P versus BPP and L versus BPL, lead. Explicit branching-program generators remain close, followed by independent construction frontiers in extraction, restricted isometries and expanders. General hardness-randomness principles outrank narrower parameter improvements; low historical scores do not hide canonical prime construction.

Previous prefix: TCS-0003, TCS-6600.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus BPP](index.html#TCS-0003) (TCS-0003) | General derandomization | 99 | The defining question of whether randomness adds efficient decision power. |
| 2 | [L versus BPL](index.html#TCS-0026) (TCS-0026) | Space-bounded derandomization | 98 | The defining derandomization question under logarithmic memory. |

Candidates considered: TCS-0003, TCS-0026, TCS-6600, TCS-7271, TCS-6662, TCS-6699, TCS-6686, TCS-6879, TCS-6696, TCS-1021, TCS-5341, TCS-6693, TCS-1005, TCS-5798, TCS-6689, TCS-6729, TCS-5287, TCS-1137, TCS-1956, TCS-1015, TCS-1125, TCS-1019, TCS-1022, TCS-1133, TCS-3958, TCS-1006, TCS-1016, TCS-0854, TCS-3986, TCS-1013, TCS-1014, TCS-1122, TCS-1131, TCS-1008, TCS-1018, TCS-4778, TCS-2201, TCS-1135, TCS-1124, TCS-1007.

## Parameterized complexity and algorithms

FPT versus W[1] and ETH remain the foundational anchors. Exact TSP, Subset Sum and Set Cover provide distinct exponential-time barriers. Structural recognition and general kernelization principles fill out the primary selection, including substantial preprocessing questions previously left at 50; specialized deletion and representation variants follow.

Previous prefix: TCS-6592, TCS-6593.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FPT versus \(\mathrm{W}[1]\)](index.html#TCS-6592) (TCS-6592) | Parameterized tractability | 99 | The defining tractability boundary for algorithms parameterized by solution size. |
| 2 | [Exponential Time Hypothesis](index.html#TCS-6593) (TCS-6593) | Exact exponential algorithms | 98 | The foundational quantitative hardness hypothesis for exact and parameterized computation. |

Candidates considered: TCS-6592, TCS-6593, TCS-7233, TCS-4790, TCS-6594, TCS-7241, TCS-6731, TCS-4695, TCS-6379, TCS-6660, TCS-0787, TCS-7035, TCS-2804, TCS-6974, TCS-6734, TCS-7312, TCS-0801, TCS-7181, TCS-6749, TCS-7023, TCS-0816, TCS-6728, TCS-3480, TCS-4289, TCS-5374, TCS-7022, TCS-7247, TCS-2662, TCS-6814, TCS-3917, TCS-4440, TCS-7027, TCS-1945, TCS-0808, TCS-0800, TCS-0597, TCS-0799.

## Approximation algorithms and inapproximability

Unique Games leads as a general organizing conjecture, with Densest k-Subgraph the complementary algorithmic flagship. Directed design, sparse cuts, routing, covering, submodularity and clustering populate the next priorities. Universal hardness and rounding principles precede narrower variants; LP gaps remain distinguished from the true approximation limits of all algorithms.

Previous prefix: TCS-6587, TCS-0006.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Unique Games Conjecture](index.html#TCS-0006) (TCS-0006) | Hardness of approximation | 99 | A central organizing conjecture for sharp approximation hardness and general SDP algorithms. |
| 2 | [Constant-factor approximation for Densest k-Subgraph](index.html#TCS-6587) (TCS-6587) | Approximation algorithms for dense subgraphs | 97 | A defining gap between approximation algorithms and established hardness foundations. |

Candidates considered: TCS-0006, TCS-6587, TCS-6588, TCS-7266, TCS-7282, TCS-7356, TCS-7160, TCS-5407, TCS-6659, TCS-1930, TCS-7281, TCS-6589, TCS-6591, TCS-7353, TCS-7358, TCS-6309, TCS-7357, TCS-5544, TCS-6757, TCS-5787, TCS-7380, TCS-7287, TCS-7318, TCS-6590, TCS-7354, TCS-6756, TCS-2625, TCS-0922, TCS-1168, TCS-5554.

## Online algorithms, scheduling and packing

The matroid secretary conjecture and unrelated-machine scheduling lead as complementary central problems in the merged category. Precedence, additive packing, server movement, geometric chasing and limited feedback stay near the top. Equivalent contention resolution follows its secretary representative; specialized regret and scheduling refinements do not dominate the prefix.

Previous prefix: TCS-6638.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Matroid secretary conjecture](index.html#TCS-7316) (TCS-7316) | Online selection under matroid constraints | 98 | A defining universal random-order selection conjecture under independence constraints. |
| 2 | [Breaking two for unrelated-machine makespan](index.html#TCS-6638) (TCS-6638) | Heterogeneous-machine scheduling | 97 | A central approximation barrier for heterogeneous scheduling. |

Candidates considered: TCS-7316, TCS-6638, TCS-6676, TCS-6640, TCS-7317, TCS-6576, TCS-6577, TCS-0935, TCS-7319, TCS-6721, TCS-6724, TCS-1529, TCS-7335, TCS-5779, TCS-5221, TCS-5030, TCS-6078, TCS-1241, TCS-6836, TCS-0700, TCS-5252.

## Beyond worst-case and average-case analysis

Worst-case-to-average-case hardness and planted clique lead. Canonical inference, random satisfiability and smoothed local search follow, with the random-SAT search threshold restored to a priority reflecting its actual scope. Closely related hardness-amplification and specially chosen distribution variants follow these broad representatives.

Previous prefix: TCS-6656, TCS-0012.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0012) (TCS-0012) | Worst-case versus average-case hardness | 99 | The foundational implication from worst-case NP hardness to feasibly generated average hardness. |
| 2 | [Planted clique conjecture](index.html#TCS-6656) (TCS-6656) | Planted inference | 98 | The canonical statistical-computational gap supporting many average-case reductions. |

Candidates considered: TCS-0012, TCS-6656, TCS-7238, TCS-6657, TCS-6658, TCS-6684, TCS-4876, TCS-6453, TCS-6702, TCS-6703, TCS-5011, TCS-7148, TCS-5406.

## Sampling, Markov chains and mixing times

General coloring and fixed-margin sampling remain the complementary anchors. Critical dynamics, universal matroid rounding and cutoff follow; related Ising refinements are interleaved with other substantial sampling questions only within nearby importance levels. All nine active candidates remain within the category's Top 500 quota.

Previous prefix: TCS-6621, TCS-6622.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Rapid mixing of Glauber dynamics with \(\Delta +2\) colours](index.html#TCS-6621) (TCS-6621) | Colouring-chain mixing | 96 | A central general-graph local-sampling frontier at the connectivity threshold. |
| 2 | [Kannan–Tetali–Vempala conjecture](index.html#TCS-6622) (TCS-6622) | Sampling prescribed-degree graphs | 94 | Universal rapid switch-chain mixing would justify a basic sampler for arbitrary feasible bipartite degree sequences. |

Candidates considered: TCS-6621, TCS-6622, TCS-6668, TCS-2861, TCS-6843, TCS-6839, TCS-6857, TCS-6840, TCS-6851.

## Counting and enumeration

Exact counting complexity and #BIS lead. General perfect matchings, permanent derandomization and the two canonical output-sensitive enumeration problems follow closely. The primary selection also represents structural counting classifications and the decision-counting gap, rather than consisting entirely of individual FPRAS targets.

Previous prefix: TCS-6628, TCS-7221.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FP versus #P](index.html#TCS-6820) (TCS-6820) | Exact counting complexity | 99 | The fundamental exact-counting analogue of the efficient-verification boundary. |
| 2 | [FPRAS for #BIS](index.html#TCS-7221) (TCS-7221) | Approximate counting | 97 | The canonical unresolved approximate-counting degree shared by many problems. |

Candidates considered: TCS-6820, TCS-7221, TCS-6628, TCS-6629, TCS-7112, TCS-7240, TCS-6821, TCS-7355, TCS-7320, TCS-7099, TCS-6671, TCS-1004, TCS-3635, TCS-4671, TCS-3037, TCS-7084, TCS-7086, TCS-7082.

## Graph algorithms

Lead with graph isomorphism and unrestricted exact matching. Rank broad algorithmic and structural barriers ahead of polylogarithmic refinements; the second girth formulation adds limited breadth beside the main conjecture.

Previous prefix: TCS-7222, TCS-6536.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Graph isomorphism in polynomial time](index.html#TCS-7222) (TCS-7222) | Graph isomorphism | 99 | Polynomial-time graph isomorphism would settle the central complexity question for equivalence of finite structures. |
| 2 | [Almost-linear-time exact maximum matching in general graphs](index.html#TCS-6538) (TCS-6538) | Exact general graph optimization | 98 | Almost-linear general matching would remove a major remaining polynomial overhead in exact graph optimization. |

Candidates considered: TCS-7222, TCS-6538, TCS-6539, TCS-6683, TCS-6536, TCS-6500, TCS-6511, TCS-7341, TCS-7346, TCS-2783, TCS-7377, TCS-7228, TCS-7263, TCS-7342, TCS-7343, TCS-7344, TCS-7345, TCS-7180, TCS-7348, TCS-0771, TCS-6655, TCS-7285, TCS-0775, TCS-0611, TCS-7244, TCS-0594.

## Data structures

Keep dynamic optimality and general static lower bounds at the front. Broad dictionary and lower-bound questions precede analyses of particular implementations and specialized persistence guarantees.

Previous prefix: TCS-6498, TCS-6540.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Dynamic optimality conjecture](index.html#TCS-6498) (TCS-6498) | Adaptive search trees | 99 | Dynamic optimality would settle whether a simple adaptive search tree matches every offline access strategy. |
| 2 | [Superlogarithmic static cell-probe lower bounds](index.html#TCS-6540) (TCS-6540) | Static data-structure lower bounds | 98 | Superlogarithmic static cell-probe bounds would break a general unconditional data-structure lower-bound barrier. |

Candidates considered: TCS-6498, TCS-6540, TCS-7338, TCS-7331, TCS-6586, TCS-7334, TCS-0949, TCS-7333, TCS-5825, TCS-0300, TCS-7328, TCS-7340, TCS-7329, TCS-6508, TCS-0474, TCS-7327, TCS-7330.

## Dynamic algorithms

Connectivity remains the clearest foundational target. Near-optimal matching takes the second focus slot on comparable importance while adding a distinct optimization challenge; exact distances outrank narrower dynamic refinements.

Previous prefix: TCS-6625, TCS-6627.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Deterministic fully dynamic connectivity with polylogarithmic worst-case updates](index.html#TCS-6625) (TCS-6625) | Dynamic connectivity | 98 | Deterministic worst-case polylogarithmic connectivity would settle a foundational latency and randomness gap in dynamic graphs. |
| 2 | [Fully dynamic near-optimal matching with polylogarithmic updates](index.html#TCS-6627) (TCS-6627) | Dynamic matching | 97 | Near-optimal explicit matching with polylogarithmic updates would overcome a major dynamic optimization barrier. |

Candidates considered: TCS-6625, TCS-6627, TCS-6626, TCS-6670, TCS-0478, TCS-5209, TCS-0543, TCS-7332, TCS-7339, TCS-0541, TCS-0387, TCS-7326, TCS-0545, TCS-0536, TCS-3331.

## String algorithms and computational biology

Use trace reconstruction and near-exact edit-distance approximation for the leading statistical and computational barriers. Compression and assembly rise above specialized indexing refinements; related edit-distance variants remain high without taking both focus slots.

Previous prefix: TCS-6623, TCS-6624.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Worst-case sample complexity of trace reconstruction](index.html#TCS-6623) (TCS-6623) | Reconstruction from noisy strings | 98 | Worst-case trace reconstruction determines the intrinsic information cost of recovering sequences after unlocated deletions. |
| 2 | [Truly subquadratic \((1+\varepsilon)\)-approximation of edit distance](index.html#TCS-7220) (TCS-7220) | Near-exact sequence alignment | 97 | Subquadratic near-exact edit distance would cross a central accuracy-versus-runtime barrier in general sequence comparison. |

Candidates considered: TCS-6623, TCS-7220, TCS-6624, TCS-6513, TCS-6669, TCS-7322, TCS-7371, TCS-7297, TCS-7367, TCS-6928, TCS-7374, TCS-7360, TCS-0467, TCS-0468, TCS-7366, TCS-7362, TCS-7369, TCS-7375, TCS-0470, TCS-7365, TCS-7364, TCS-7368, TCS-7370, TCS-7361, TCS-0466.

## Game theory, social choice and fair division

Put unrestricted EFX existence and truthful submodular auctions first: they are foundational feasibility and incentive barriers. Broad scheduling, allocation and representation questions follow before special-agent cases and narrower protocol variants.

Previous prefix: TCS-6632, TCS-0011.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Existence of complete EFX allocations for additive valuations](index.html#TCS-0011) (TCS-0011) | Existence of fair allocations | 98 | Complete EFX existence is a central feasibility question for fairness with indivisible goods and unrestricted agent counts. |
| 2 | [Constant-factor universally truthful auctions for submodular bidders](index.html#TCS-6632) (TCS-6632) | Truthful mechanisms | 98 | Constant-factor truthful submodular auctions would determine whether exact incentives impose an unbounded welfare loss. |

Candidates considered: TCS-0011, TCS-6632, TCS-6674, TCS-6639, TCS-6633, TCS-7379, TCS-6634, TCS-1115, TCS-0056, TCS-7197, TCS-7200, TCS-1116, TCS-1109, TCS-7196, TCS-1108, TCS-4584, TCS-7383, TCS-7203, TCS-0073, TCS-0571, TCS-1714.

## Algebraic computation

VP versus VNP leads, with matrix multiplication providing an equally consequential algorithmic direction. General PIT remains immediately behind; the next tier balances major lower-bound barriers with fundamental arithmetic and decidability questions before restricted models and overlapping formulations.

Previous prefix: TCS-0007, TCS-6611.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [VP versus VNP](index.html#TCS-0005) (TCS-0005) | Unrestricted arithmetic circuit complexity | 100 | VP versus VNP is the central unrestricted arithmetic-circuit complexity question, with the permanent as a complete target. |
| 2 | [Matrix multiplication exponent](index.html#TCS-0007) (TCS-0007) | Matrix multiplication | 99 | The matrix multiplication exponent governs a fundamental operation and propagates to a broad range of algorithms. |

Candidates considered: TCS-0005, TCS-0007, TCS-7113, TCS-6611, TCS-6666, TCS-6612, TCS-6613, TCS-6614, TCS-6641, TCS-7174, TCS-7262, TCS-0010, TCS-6888, TCS-7175, TCS-0055, TCS-6642, TCS-6677, TCS-6895, TCS-6615, TCS-6898, TCS-7223, TCS-1058, TCS-6890, TCS-6893, TCS-0009, TCS-2506, TCS-6616, TCS-5520, TCS-6897, TCS-1101, TCS-6883, TCS-6903, TCS-0481, TCS-3318, TCS-5260, TCS-2958, TCS-6884, TCS-7269, TCS-0046, TCS-5921, TCS-6882, TCS-2718, TCS-5240, TCS-1102, TCS-3959, TCS-6493, TCS-0047, TCS-7224, TCS-1103, TCS-1151, TCS-0095, TCS-2039, TCS-4523, TCS-1544, TCS-5739, TCS-2077, TCS-4350, TCS-4490, TCS-7372, TCS-1069.

## Lattices and computational number theory

Hilbert's tenth problem over the rationals and classical factoring are the leading landmarks. General lattice approximation follows closely; foundational algorithmic and hardness boundaries precede parameter-specific security reductions and refinements.

Previous prefix: TCS-6571, TCS-6667.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Hilbert’s tenth problem over the rationals](index.html#TCS-6571) (TCS-6571) | Diophantine decidability | 99 | Rational Diophantine decidability is a landmark boundary between arithmetic, computability and algebraic geometry. |
| 2 | [Integer factorization in randomized polynomial time](index.html#TCS-6617) (TCS-6617) | Classical arithmetic inversion | 99 | Classical polynomial-time factoring is a central arithmetic complexity question with broad cryptographic and quantum-computing consequences. |

Candidates considered: TCS-6571, TCS-6617, TCS-6667, TCS-6618, TCS-7234, TCS-0655, TCS-7169, TCS-7265, TCS-6619, TCS-6620, TCS-6861, TCS-6863, TCS-0656, TCS-0658, TCS-0659, TCS-0662, TCS-0661, TCS-6864, TCS-5317, TCS-0652, TCS-0648, TCS-1170, TCS-5395, TCS-0657, TCS-7171, TCS-7170, TCS-0653.

## Coding and information theory

Lead with the binary rate-distance frontier and general broadcast capacity, covering coding and network information at comparable landmark importance. Rank actual targets: the retained deletion-channel card asks for formalizing a known finite approximation, rather than discovering the exact capacity curve.

Previous prefix: TCS-6606, TCS-1010.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Optimal asymptotic binary rate–distance tradeoff](index.html#TCS-1010) (TCS-1010) | Coding rate versus distance | 99 | The binary rate-distance frontier is a foundational worst-case coding limit, even at the stated approximate acceptance precision. |
| 2 | [Capacity of the general broadcast channel](index.html#TCS-6665) (TCS-6665) | Network information capacity | 98 | General broadcast capacity is a defining unresolved law for communicating independent information to multiple receivers. |

Candidates considered: TCS-1010, TCS-6665, TCS-7210, TCS-1020, TCS-6584, TCS-6606, TCS-6608, TCS-7267, TCS-0013, TCS-6609, TCS-7211, TCS-7214, TCS-7215, TCS-1012, TCS-6738, TCS-4524, TCS-4968, TCS-1011, TCS-6610, TCS-3513, TCS-0196, TCS-4802, TCS-0184, TCS-0187, TCS-0205, TCS-0178, TCS-6607.

## Property testing and distribution learning

The general testing-versus-estimation implication leads. Unrestricted Gaussian-mixture density learning takes the second slot at comparable importance to graph-testing classification, adding the category's major statistical-computational frontier rather than a second graph-only focus.

Previous prefix: TCS-6630, TCS-1033.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Polynomial testability versus distance estimation](index.html#TCS-1033) (TCS-1033) | Testing versus distance estimation | 97 | Polynomial testing versus estimation asks for a general relationship between two fundamental forms of sublinear information access. |
| 2 | [Polynomial-time density learning of Gaussian mixtures](index.html#TCS-5443) (TCS-5443) | Computational distribution learning | 96 | Jointly polynomial Gaussian-mixture density learning would resolve a broad statistical-computational gap without separation assumptions. |

Candidates considered: TCS-1033, TCS-5443, TCS-6630, TCS-1029, TCS-6672, TCS-0848, TCS-5085, TCS-2535, TCS-1030, TCS-4259, TCS-5210, TCS-3906, TCS-4376, TCS-0672, TCS-0847, TCS-0841.

## Differential privacy

Prioritize general private-learning sample bounds and efficient release of all marginals. They address broader statistical and computational limits than sharp rates for a single continual or online primitive.

Previous prefix: TCS-0506, TCS-6673.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Private PAC sample complexity from VC and Littlestone dimensions](index.html#TCS-0506) (TCS-0506) | Private learnability | 97 | VC/Littlestone sample bounds would quantify the privacy overhead uniformly across all finite concept classes. |
| 2 | [Polynomial-time private release of all marginals](index.html#TCS-7236) (TCS-7236) | Efficient private query release | 96 | Efficient release of all marginals targets a central statistical-computational gap in private high-dimensional data analysis. |

Candidates considered: TCS-0506, TCS-7236, TCS-6673, TCS-0507.

## Constraint satisfaction

Retain finite promise-CSP and infinite-domain CSP dichotomies as the broadest organizing questions. General search, expressibility and classification frontiers precede individual colouring gaps and restricted relaxations.

Previous prefix: TCS-6635, TCS-6636.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Finite-domain promise CSP dichotomy](index.html#TCS-6635) (TCS-6635) | Finite promise constraints | 99 | A finite promise-CSP dichotomy would extend a central complexity-classification principle across relaxed local constraints. |
| 2 | [Bodirsky–Pinsker conjecture](index.html#TCS-6636) (TCS-6636) | Infinite-domain constraints | 98 | The infinite-domain dichotomy would connect algorithms, algebra and model theory across a major class of rich templates. |

Candidates considered: TCS-6635, TCS-6636, TCS-6637, TCS-6675, TCS-6748, TCS-7116, TCS-1173, TCS-6725, TCS-3678, TCS-1807, TCS-0504, TCS-1555, TCS-0441, TCS-1978, TCS-7237, TCS-3984, TCS-3585, TCS-0444.

## Automated reasoning, rewriting and unification

Lead with length-constrained word equations and Presburger arithmetic with primes, two broad decidability boundaries with distinct string and arithmetic content. General complexity and solver-power questions precede narrower matching orders and representation variants.

Previous prefix: TCS-6562, TCS-6643.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Word equations with linear length constraints](index.html#TCS-6562) (TCS-6562) | Word equations with arithmetic | 98 | Length-constrained word equations are a foundational decidability boundary for combining string concatenation and arithmetic. |
| 2 | [Decidability of Presburger arithmetic with primes](index.html#TCS-1992) (TCS-1992) | Arithmetic definability and decidability | 97 | Presburger arithmetic with primes links complete symbolic reasoning to deep arithmetic definability and prime-pattern questions. |

Candidates considered: TCS-6562, TCS-1992, TCS-6643, TCS-0163, TCS-6644, TCS-7239, TCS-6650, TCS-7194, TCS-0306, TCS-7125, TCS-1595, TCS-7134, TCS-0114, TCS-5603.

## Database theory and finite model theory

A logic capturing P and Asser's spectrum problem lead as foundational descriptive-complexity questions. Broad model-checking and database-query boundaries follow closely; specific width, representation and convergence refinements come later.

Previous prefix: TCS-6678, TCS-6645.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [A logic capturing polynomial time](index.html#TCS-7195) (TCS-7195) | Descriptive characterization of polynomial time | 99 | A logic capturing polynomial time is the central question of describing feasible computation on unordered finite structures. |
| 2 | [Asser’s problem](index.html#TCS-7232) (TCS-7232) | Finite spectra and complementation | 98 | Asser's problem connects finite spectra with nondeterministic exponential-time closure under complement. |

Candidates considered: TCS-7195, TCS-7232, TCS-6678, TCS-6645, TCS-0492, TCS-6680, TCS-6372, TCS-3631, TCS-0488, TCS-0505, TCS-0494, TCS-7128, TCS-4458, TCS-0499, TCS-4995, TCS-0502, TCS-3557, TCS-0487, TCS-0482.

## Miscellaneous

The sunflower conjecture leads for its broad combinatorial and complexity consequences. Seese's conjecture follows as a distinct logic-structure boundary; the comparison-balance conjecture remains substantial but narrower.

Previous prefix: TCS-7177, TCS-6654.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Sunflower conjecture](index.html#TCS-7290) (TCS-7290) | Extremal set systems | 97 | The sunflower conjecture is a broad extremal principle with major consequences for computational lower bounds and parameterized reductions. |
| 2 | [Seese’s conjecture](index.html#TCS-6654) (TCS-6654) | Logical decidability and graph structure | 96 | Seese's conjecture would connect logical decidability with a universal graph-structural restriction. |

Candidates considered: TCS-7290, TCS-6654, TCS-7177.
