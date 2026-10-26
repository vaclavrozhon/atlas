# Benchmark selection review

Reviewed on 2026-10-23 across 35 categories.

Our primary goal is a benchmark of 500 problems. Top 100 is a priority subset of those same 500, with secondary editorial attention. Both use the same category order and the same ranking within each category. The existing Top 1000 view is not an active benchmark goal.

Subjective editorial preference requested by the user, based on saved titles and statement excerpts, with expanded summaries for sparse drafts. Scientific interest, breadth, conceptual clarity and topic diversity guide the explicit choices in research/editorial-ranking-20261023/decisions.json. This is not a new literature, formulation or current-open-status review. Formalization effort, prose length and publication date do not affect scores. Scores and focus prefixes were reconsidered. Equal scores express comparable preference; stable IDs break ties outside the focus prefix.

Top 100 takes the first 5/2 places in each large/small category. Top 500 takes the first 25/10 and the legacy Top 1000 view takes the first 50/20 places from the same order. Top 100 is contained in Top 500, which is contained in Top 1000. Focus places balance scientific importance and topical diversity; remaining places retain score order. None of these subsets certifies current open status.

| Benchmark | Target | Available | Missing |
| --- | ---: | ---: | ---: |
| [Top 100](index.html?benchmark=top100) | 100 | 100 | 0 |
| [Top 500](index.html?benchmark=top500) | 500 | 489 | 11 |
| [Top 1000 (legacy view)](index.html?benchmark=top1000) | 1000 | 887 | 113 |

## Unfilled places

- top500: Differential privacy has 6/10 places.
- top500: Miscellaneous has 3/10 places.
- top1000: Algorithms has 28/50 places.
- top1000: Automata and formal languages has 40/50 places.
- top1000: Optimization and numerical computation has 35/50 places.
- top1000: Geometry, topology and metric spaces has 42/50 places.
- top1000: Learning theory has 40/50 places.
- top1000: Cryptography has 40/50 places.
- top1000: Beyond worst-case and average-case analysis has 18/20 places.
- top1000: Sampling, Markov chains and mixing times has 17/20 places.
- top1000: Differential privacy has 6/20 places.
- top1000: Constraint satisfaction has 18/20 places.
- top1000: Miscellaneous has 3/20 places.

## Computational complexity

Favor foundational separations, concrete circuit lower bounds and meta-complexity. Keep time, space and circuits visible rather than filling the prefix with NP variants.

Previous prefix: TCS-0001, TCS-6530, TCS-6531, TCS-6535, TCS-6534.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NP](index.html#TCS-0001) (TCS-0001) | P versus NP | 100 | This is the basic test of whether efficient verification entails efficient solution. It organizes the complexity of optimization, search, logical reasoning, and many graph problems, while motivating the development of general algorithmic lower-bound techniques. |
| 2 | [Superlinear Boolean circuit lower bounds](index.html#TCS-0015) (TCS-0015) | Superlinear Boolean circuit lower bounds | 96 | A superlinear lower bound would establish a basic limitation on unrestricted nonuniform computation for an efficiently computable function. It would surpass every fixed linear gate count, even when a circuit can reuse work freely across outputs, and expose structure that simple counting does not identify. |
| 3 | [L versus NL](index.html#TCS-0004) (TCS-0004) | L versus NL | 96 | Directed reachability is the canonical model of exploring possible computational states. Its space complexity determines whether nondeterministic logarithmic memory can be replaced by deterministic logarithmic memory, with consequences for low-memory graph algorithms and complexity theory. |
| 4 | [Minimum Circuit Size Problem](index.html#TCS-4786) (TCS-4786) | Minimum Circuit Size Problem | 94 | MCSP asks how hard it is to recognize computational simplicity from complete data. Its classification connects NP-completeness with circuit lower bounds, learning and cryptography. A proof or refutation of standard NP-hardness would settle a central question about whether circuit minimization has the same reduction-based difficulty as general NP search. |
| 5 | [P versus PSPACE](index.html#TCS-6530) (TCS-6530) | P versus PSPACE | 98 | This asks whether reusing a feasible amount of memory can provide computational power beyond feasible running time. It is a central unresolved separation even when the allowed language class is enlarged from NP to all of PSPACE, and it organizes the complexity of quantified reasoning, games, and verification. |

Candidates considered: TCS-0001, TCS-0015, TCS-0004, TCS-4786, TCS-6530, TCS-0002, TCS-0021, TCS-6532, TCS-0020, TCS-6531, TCS-6535, TCS-7161, TCS-0016, TCS-0017, TCS-1054, TCS-1056, TCS-6534, TCS-6817, TCS-6977, TCS-7158, TCS-0018, TCS-0293, TCS-4988, TCS-6091, TCS-6533, TCS-6714, TCS-7268, TCS-7321, TCS-7363, TCS-0019, TCS-0305, TCS-1052, TCS-1053, TCS-6455, TCS-6743, TCS-6979, TCS-7286, TCS-1040, TCS-5593, TCS-6006, TCS-6168, TCS-6747, TCS-7159, TCS-7256, TCS-0298, TCS-0301, TCS-1035, TCS-2333, TCS-2532, TCS-6285, TCS-6934, TCS-7257, TCS-0297, TCS-0303, TCS-1034, TCS-1036, TCS-2215, TCS-2425, TCS-3862, TCS-6139, TCS-2029, TCS-2681, TCS-3886, TCS-4746, TCS-7243, TCS-0310, TCS-1602, TCS-6681, TCS-7260.

## Algorithms

Favor basic primitives and reusable compression principles: sorting, terminal flow representation, sparsification and output-sensitive computation, before narrow graph-class classifications.

Previous prefix: TCS-6537, TCS-0388, TCS-0946, TCS-1141.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Expected linear-time integer sorting for every word length](index.html#TCS-6537) (TCS-6537) | Expected linear-time integer sorting for every word length | 96 | A basic limit on what word-level arithmetic can accomplish beyond comparisons. The challenge is a uniform bound across all word lengths, rather than the already solved polynomial-universe or sufficiently-large-word cases. |
| 2 | [Sorting \(X + Y\)](index.html#TCS-0388) (TCS-0388) | Sorting \(X + Y\) | 92 | This is a basic test of whether algebraic dependence among many sortable objects can be exploited with no overhead beyond writing them down. It also makes the distinction between short comparison decision trees and fast uniform algorithms unusually concrete. |
| 3 | [Size-bounded approximate multicommodity-flow sparsifiers](index.html#TCS-7380) (TCS-7380) | Size-bounded approximate multicommodity-flow sparsifiers | 90 | This tests whether terminal flow behavior admits an arbitrarily accurate finite summary independent of the original network. |
| 4 | [Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges](index.html#TCS-0946) (TCS-0946) | Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges | 92 | Tests whether preserving all cuts of a multiway interaction system requires any more hyperedges than the graph sparsification upper bound. It separates the number of retained interactions from their incidence storage and from the cost of computing them. |
| 5 | [Near-linear output-sensitive Subset Sum](index.html#TCS-7350) (TCS-7350) | Near-linear output-sensitive Subset Sum | 90 | The question tests whether a basic dynamic-programming problem can be solved at essentially the cost of reading its input and writing its distinct answers. A positive resolution would avoid paying for a large unused numerical range even when the input contains repeated items. A negative resolution would establish an additional computational cost beyond input and output size for a fundamental exact problem. This is a general algorithmic endpoint, not a request to count solutions or to improve one implementation. |

Candidates considered: TCS-6537, TCS-0388, TCS-7380, TCS-0946, TCS-7350, TCS-5705, TCS-2018, TCS-3346, TCS-6783, TCS-6785, TCS-0809, TCS-6421, TCS-6784, TCS-7075, TCS-7351, TCS-1141, TCS-1338, TCS-5969, TCS-6173, TCS-7146, TCS-1617, TCS-3263, TCS-6251, TCS-7061, TCS-0538, TCS-2822, TCS-4417, TCS-6270.

## Automata and formal languages

Favor canonical barriers in synchronization, nondeterminism, expressive power and equivalence. Broad characterizations outrank model-specific closure questions.

Previous prefix: TCS-6558, TCS-6560, TCS-6559, TCS-6561, TCS-6563.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Maximum reset threshold of synchronizing automata](index.html#TCS-6558) (TCS-6558) | Maximum reset threshold of synchronizing automata | 96 | A central extremal problem in automata theory, with a simple finite-state formulation and a sharp explicit candidate bound. It tests whether local compression and algebraic structure can force globally short control sequences in every synchronizing system. |
| 2 | [Sakoda–Sipser problem](index.html#TCS-6560) (TCS-6560) | Sakoda–Sipser problem | 96 | A principal unresolved measure of the succinctness provided by nondeterminism. It isolates the issue in finite-state machines, connects to nonuniform space complexity, and asks whether revisiting read-only data can replace a large internal record of possible computations. |
| 3 | [Generalized star-height problem](index.html#TCS-6559) (TCS-6559) | Generalized star-height problem | 92 | A basic unresolved expressive-depth question for regular languages: determine whether Boolean operations eliminate every need for nested iteration, or whether a genuine second level exists. |
| 4 | [Decidability of equivalence for unambiguous context-free grammars](index.html#TCS-0164) (TCS-0164) | Decidability of equivalence for unambiguous context-free grammars | 90 | This basic equivalence problem tests the algorithmic power of unique parsing beyond deterministic context-free language descriptions. |
| 5 | [First-order definability of regular tree languages](index.html#TCS-6564) (TCS-6564) | First-order definability of regular tree languages | 90 | The tree analogue of effective first-order definability for regular word languages. |

Candidates considered: TCS-6558, TCS-6560, TCS-6559, TCS-0164, TCS-6564, TCS-6561, TCS-6563, TCS-6582, TCS-7261, TCS-7431, TCS-0154, TCS-0167, TCS-6064, TCS-7406, TCS-7409, TCS-0128, TCS-0146, TCS-2243, TCS-5904, TCS-5959, TCS-7408, TCS-7410, TCS-0135, TCS-3378, TCS-4575, TCS-5651, TCS-7412, TCS-0138, TCS-3863, TCS-4636, TCS-4677, TCS-5738, TCS-5863, TCS-7309, TCS-0133, TCS-0136, TCS-4659, TCS-7407, TCS-7413, TCS-7414.

## Semantics, logic and verification

Favor compact decidability boundaries, algorithmic games, and foundations of proof assistants and program logic. Represent several foundations rather than only recurrence variants.

Previous prefix: TCS-6565, TCS-6567, TCS-6569, TCS-6570, TCS-6583.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Skolem problem](index.html#TCS-5773) (TCS-5773) | Skolem problem | 96 | Skolem asks whether exact reachability of zero is decidable for the simplest class of discrete linear recurrences with finite integer descriptions. The question connects arithmetic with verification of linear loops, matrix dynamics, automata and stochastic systems, and serves as a common unresolved decision problem to which other verification tasks are compared. |
| 2 | [Parity games in polynomial time](index.html#TCS-4245) (TCS-4245) | Parity games in polynomial time | 94 | Parity games are a central algorithmic component of model checking and reactive synthesis: they express recurring obligations in infinite executions by a finite arena. Their winner problem is polynomial-time equivalent to model checking the modal \(\mu\)-calculus. Determining whether general parity games admit polynomial time would resolve a basic complexity boundary for these verification tasks and for a natural problem in \(\mathrm{UP}\cap\mathrm{coUP}\). |
| 3 | [Tarski’s exponential function problem](index.html#TCS-7230) (TCS-7230) | Tarski’s exponential function problem | 96 | A central boundary in exact algorithmic reasoning over real numbers: polynomial real arithmetic is decidable, while adding one standard analytic function connects logical truth to unresolved transcendence questions. Its resolution would determine whether a uniform symbolic decision procedure can handle all finite first-order specifications involving real exponentiation, with consequences for verification problems already reducible to this theory. |
| 4 | [Internal semisimplicial types in ordinary HoTT](index.html#TCS-6569) (TCS-6569) | Internal semisimplicial types in ordinary HoTT | 90 | Determine whether ordinary HoTT can express a fundamental unbounded coherent structure internally, a basic issue for higher categories and foundational proof languages. |
| 5 | [Decidability of multiplicative-exponential linear logic](index.html#TCS-7192) (TCS-7192) | Decidability of multiplicative-exponential linear logic | 90 | MELL combines resource-sensitive composition with controlled reuse. Its decision problem connects automated proof search to branching counter systems and tests a fundamental boundary of algorithmic reasoning about resources. |

Candidates considered: TCS-5773, TCS-4245, TCS-7230, TCS-6569, TCS-7192, TCS-6565, TCS-6567, TCS-6568, TCS-6566, TCS-6570, TCS-6583, TCS-7153, TCS-7157, TCS-7428, TCS-1649, TCS-3031, TCS-3655, TCS-5915, TCS-6112, TCS-6359, TCS-7418, TCS-7432, TCS-0913, TCS-5682, TCS-5817, TCS-7419, TCS-7423, TCS-7425, TCS-7426, TCS-7430, TCS-0901, TCS-4017, TCS-4302, TCS-5987, TCS-6036, TCS-7310, TCS-7416, TCS-0632, TCS-0896, TCS-2033, TCS-6245, TCS-7154, TCS-7417, TCS-7427, TCS-0092, TCS-0619, TCS-0640, TCS-1659, TCS-5975, TCS-7433, TCS-7435.

## Distributed, parallel and sublinear algorithms

Favor the limits of parallelism and locality, derandomization of matching, and lower bounds for powerful communication models. General primitives and streaming characterizations precede individual tradeoff improvements.

Previous prefix: TCS-6553, TCS-6556, TCS-6504, TCS-6554, TCS-6555.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus NC](index.html#TCS-6553) (TCS-6553) | P versus NC | 98 | This asks whether a feasible computation can require intrinsically many sequential stages even when polynomially many processors are available. It is the central unresolved premise behind P-completeness as an explanation for resistance to parallelization, spanning graph algorithms, simulation, optimization, and language processing. |
| 2 | [Perfect matching in NC](index.html#TCS-6504) (TCS-6504) | Perfect matching in NC | 96 | I include this because perfect matching is a basic polynomial-time graph problem for which randomization and parallelism interact in a particularly sharp way. The question asks whether randomness is needed to find globally compatible choices quickly, and whether the structural tools for odd cycles can be made as parallel as the algebraic ones. |
| 3 | [Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds](index.html#TCS-6554) (TCS-6554) | Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds | 92 | The question asks whether sparse dependencies can always be resolved within a log-logarithmic communication radius under fixed polynomial slack. This would determine the complexity of a widely used distributed primitive and clarify a central scale in the LOCAL complexity hierarchy. |
| 4 | [One-cycle versus two-cycles conjecture](index.html#TCS-6505) (TCS-6505) | One-cycle versus two-cycles conjecture | 92 | I include this because the input removes most graph-theoretic complications and leaves the cost of assembling global connectivity information. It is a standard conditional-hardness benchmark for massively parallel algorithms, and a resolution would clarify whether limited memory creates an inherent logarithmic coordination cost even on degree-two graphs. |
| 5 | [Explicit superconstant lower bounds in the congested clique](index.html#TCS-6557) (TCS-6557) | Explicit superconstant lower bounds in the congested clique | 92 | A central unbroken barrier in unconditional lower bounds for a powerful distributed model. |

Candidates considered: TCS-6553, TCS-6504, TCS-6554, TCS-6505, TCS-6557, TCS-6507, TCS-6499, TCS-6506, TCS-7349, TCS-0515, TCS-0522, TCS-6555, TCS-6556, TCS-7172, TCS-7259, TCS-0940, TCS-0984, TCS-0986, TCS-0998, TCS-3416, TCS-7336, TCS-7400, TCS-0524, TCS-0950, TCS-0969, TCS-0980, TCS-5797, TCS-6080, TCS-6501, TCS-7010, TCS-0954, TCS-0993, TCS-0994, TCS-1588, TCS-4763, TCS-5795, TCS-6206, TCS-6380, TCS-7337, TCS-0519, TCS-2233, TCS-3075, TCS-3384, TCS-3792, TCS-4193, TCS-6125, TCS-7376, TCS-0469, TCS-0985, TCS-2470, TCS-3381, TCS-4274, TCS-0834, TCS-0849.

## Optimization and numerical computation

Favor universal optimization and discrepancy barriers, exact feasibility, and dimension dependence. Fundamental geometric obstructions outrank refinements of one relaxation.

Previous prefix: TCS-0008, TCS-6574, TCS-7227, TCS-6585, TCS-6578.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strongly polynomial linear programming](index.html#TCS-0008) (TCS-0008) | Strongly polynomial linear programming | 100 | Linear programming is a basic language for optimization across combinatorics, algorithms and applications. The question asks whether exact optimization needs a number of arithmetic decisions that grows with numerical precision, or whether the dimensions alone suffice. A positive answer would extend a central efficiency property of several combinatorial optimization problems to every rational linear program. |
| 2 | [Komlós conjecture](index.html#TCS-7314) (TCS-7314) | Komlós conjecture | 96 | Komlós asks whether controlling the Euclidean size of each vector is enough to balance all coordinates by signs with a dimension-independent error. This is a central link between vector geometry and simultaneous rounding of linear constraints. It would imply the Beck–Fiala bound for sparse set systems and strengthen discrepancy-based guarantees in optimization. |
| 3 | [Nearly linear-time solution of general sparse linear systems](index.html#TCS-6585) (TCS-6585) | Nearly linear-time solution of general sparse linear systems | 96 | This tests whether sparsity and moderate conditioning suffice for solving linear equations at essentially the cost of reading them. A resolution would clarify the limits of graph-based solvers, preconditioning and numerical subroutines used throughout algorithms and optimization. |
| 4 | [Exact semidefinite feasibility in polynomial time](index.html#TCS-6574) (TCS-6574) | Exact semidefinite feasibility in polynomial time | 94 | Semidefinite constraints underlie many successful optimization relaxations, yet their unrestricted exact decision complexity is still unsettled. This problem isolates whether finite rational input admits a polynomial-time decision even when numerical separation and small explicit witnesses are unavailable. |
| 5 | [Single-exponential dependence on dimension for integer programming](index.html#TCS-7264) (TCS-7264) | Single-exponential dependence on dimension for integer programming | 92 | Integer feasibility is a general optimization primitive. A fixed exponential base in the number of variables would sharpen the dimension dependence of a widely used fixed-parameter algorithmic tool without restricting the coefficients or constraint structure. |

Candidates considered: TCS-0008, TCS-7314, TCS-6585, TCS-6574, TCS-7264, TCS-6572, TCS-7315, TCS-7227, TCS-7231, TCS-7397, TCS-7438, TCS-7439, TCS-0724, TCS-6578, TCS-7226, TCS-7283, TCS-7389, TCS-0722, TCS-5330, TCS-6483, TCS-7007, TCS-7443, TCS-7444, TCS-0687, TCS-7298, TCS-7441, TCS-7442, TCS-0491, TCS-0673, TCS-0728, TCS-7445, TCS-7446, TCS-0725, TCS-0914, TCS-7440.

## Geometry, topology and metric spaces

Favor broad isoperimetric and embedding principles, algorithmic topology, and clean extremal geometric barriers. Representation costs follow general structural questions.

Previous prefix: TCS-6523, TCS-6525, TCS-6528, TCS-6573, TCS-0318.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Kannan–Lovász–Simonovits conjecture](index.html#TCS-6523) (TCS-6523) | Kannan–Lovász–Simonovits conjecture | 98 | KLS asks whether covariance normalization alone controls the relation between global variation and local change for every log-concave distribution. Its equivalent geometric expansion principle is central to concentration inequalities and the analysis of random walks used for sampling, integration and convex optimization. |
| 2 | [Gupta–Newman–Rabinovich–Sinclair conjecture](index.html#TCS-6525) (TCS-6525) | Gupta–Newman–Rabinovich–Sinclair conjecture | 94 | Determine whether excluded graph minors exactly prevent unbounded \(\ell\)\(_{1}\) distortion and multicommodity flow–cut gaps in proper minor-closed graph families. |
| 3 | [Unknot recognition in polynomial time](index.html#TCS-6528) (TCS-6528) | Unknot recognition in polynomial time | 94 | Determine whether triviality of an explicitly given knot can be decided efficiently, a foundational test of the gap between topological certificates and algorithms. |
| 4 | [Planar k-set extremal function](index.html#TCS-0318) (TCS-0318) | Planar k-set extremal function | 90 | A central unresolved counting problem in computational geometry, it controls the complexity of levels and line-separated ranges. Its persistent gap tests the strength of crossing-number methods and geometric constructions, with consequences for output-sensitive and parametric algorithms. |
| 5 | [Polynomial Hirsch conjecture](index.html#TCS-6573) (TCS-6573) | Polynomial Hirsch conjecture | 94 | Determine whether all polyhedral feasible regions have uniformly short edge routes, a central structural question underlying linear programming. |

Candidates considered: TCS-6523, TCS-6525, TCS-6528, TCS-0318, TCS-6573, TCS-6524, TCS-6526, TCS-7242, TCS-0403, TCS-0406, TCS-0408, TCS-6199, TCS-6527, TCS-7292, TCS-0377, TCS-0381, TCS-0427, TCS-7006, TCS-7184, TCS-0382, TCS-0410, TCS-0973, TCS-6880, TCS-7182, TCS-7377, TCS-0416, TCS-0417, TCS-0419, TCS-0432, TCS-0970, TCS-0340, TCS-0398, TCS-0411, TCS-0428, TCS-0990, TCS-4454, TCS-7189, TCS-0327, TCS-0409, TCS-0430, TCS-7403, TCS-3059.

## Learning theory

Favor the relation between information and computation: compression, noise, expressive concept classes, statistical structure and cryptographic hardness. General learnability principles precede specialized models.

Previous prefix: TCS-6541, TCS-6542, TCS-6543, TCS-5358.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Linear-size sample compression](index.html#TCS-6541) (TCS-6541) | Linear-size sample compression | 96 | A central question connecting the combinatorial complexity of prediction with how many observations suffice to represent all training decisions. Its universality across concept classes, and its links to learning, extremal set systems and graph geometry, make the linear-versus-exponential gap fundamental. |
| 2 | [Learning parity with noise in polynomial time](index.html#TCS-6542) (TCS-6542) | Learning parity with noise in polynomial time | 96 | A canonical computational learning problem where a tiny amount of independent label noise defeats the obvious algebraic method, connecting efficient learning, random-code decoding and cryptographic hardness. |
| 3 | [Polynomial-time distribution-free PAC learning of DNF](index.html#TCS-5358) (TCS-5358) | Polynomial-time distribution-free PAC learning of DNF | 94 | DNF learning is a central question about whether compact Boolean rules can be inferred efficiently from observations. Polynomial sample complexity is available, but achieving polynomial computation for arbitrary input distributions remains the difficulty. A positive answer would also cover important target classes such as decision trees and juntas through their DNF representations. |
| 4 | [Efficient learning of well-separated Gaussian mixtures](index.html#TCS-3391) (TCS-3391) | Efficient learning of well-separated Gaussian mixtures | 90 | Identifiable clusters need not be easy to locate. This problem asks whether the separation that makes parameter recovery statistically feasible also permits an efficient global algorithm. It is a basic test of the computational cost of fitting latent-variable models when the number of components grows. |
| 5 | [One-way functions from hardness of learning P/poly](index.html#TCS-5090) (TCS-5090) | One-way functions from hardness of learning P/poly | 90 | One-way functions provide the basic computational ingredient for much of classical private-key cryptography. The question asks whether failure of a general-purpose circuit learner is already enough to supply that ingredient, without assuming that hard target functions can be efficiently generated at random. |

Candidates considered: TCS-6541, TCS-6542, TCS-5358, TCS-3391, TCS-5090, TCS-6543, TCS-7294, TCS-1573, TCS-4592, TCS-5088, TCS-6544, TCS-7293, TCS-2336, TCS-5031, TCS-5119, TCS-5434, TCS-5847, TCS-5902, TCS-7447, TCS-0664, TCS-0677, TCS-2339, TCS-3117, TCS-3787, TCS-4792, TCS-5087, TCS-0670, TCS-1539, TCS-3177, TCS-3689, TCS-4186, TCS-0671, TCS-0682, TCS-0683, TCS-0694, TCS-3691, TCS-7448, TCS-7449, TCS-7450, TCS-0689.

## Cryptography

Favor minimal assumptions for central cryptographic capabilities and information-theoretic limits. Keep secret sharing beside computational assumptions; place specialized efficiency improvements after broad primitive separations.

Previous prefix: TCS-6545, TCS-0022, TCS-6550, TCS-6551, TCS-0465.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0022) (TCS-0022) | One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\) | 98 | One-way functions are a basic foundation for computational pseudorandomness and cryptography. This question asks whether a worst-case separation between decision and verification already forces a function whose efficiently generated outputs resist inversion on average, without a separate cryptographic assumption. |
| 2 | [Public-key encryption from one-way functions](index.html#TCS-6545) (TCS-6545) | Public-key encryption from one-way functions | 96 | This asks whether the minimal generic assumption supporting private-key cryptography also supports encryption to a receiver whose encryption key is public. It tests whether the apparent need for additional structure in public-key constructions reflects a true difference in existence or only the known reductions. The distinction controls the foundational assumptions needed for confidential communication without a pre-existing shared secret. |
| 3 | [Circuit obfuscation from polynomial-hard LWE](index.html#TCS-6550) (TCS-6550) | Circuit obfuscation from polynomial-hard LWE | 94 | General indistinguishability obfuscation supports cryptographic capabilities well beyond ordinary encryption. Deriving it from one standard noisy-linear-equation assumption would connect that broad power to a much simpler foundation. The precise quantitative premise matters: an implication from stronger security or from secret-dependent hints does not determine the power of ordinary polynomial-hard LWE. |
| 4 | [Unleveled fully homomorphic encryption from LWE alone](index.html#TCS-6551) (TCS-6551) | Unleveled fully homomorphic encryption from LWE alone | 94 | Determine whether ordinary LWE alone supports compact encrypted computation at arbitrary polynomial depth with one fixed key set. |
| 5 | [Sub-square-root share-size exponents in perfect secret sharing](index.html#TCS-0465) (TCS-0465) | Sub-square-root share-size exponents in perfect secret sharing | 92 | A worst-case storage benchmark for information-theoretic access control, separating the power of general secret sharing from linear schemes. The newly reported bound directly addresses its strict exponential threshold. |

Candidates considered: TCS-0022, TCS-6545, TCS-6550, TCS-6551, TCS-0465, TCS-7167, TCS-7168, TCS-6549, TCS-7229, TCS-6546, TCS-6547, TCS-6552, TCS-7277, TCS-7458, TCS-6548, TCS-6953, TCS-7276, TCS-7359, TCS-7451, TCS-7453, TCS-5793, TCS-6454, TCS-6871, TCS-7272, TCS-7274, TCS-7455, TCS-7460, TCS-7225, TCS-7278, TCS-7452, TCS-7456, TCS-7457, TCS-7459, TCS-1138, TCS-3025, TCS-6692, TCS-7454, TCS-2732, TCS-4754, TCS-5013.

## Quantum computation and information

Favor quantum computational power, local Hamiltonian complexity, entanglement and verification. Keep coding and capacity prominent without letting nearby QMA variants crowd out distinct phenomena.

Previous prefix: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6518.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Quantum PCP conjecture with classical reductions](index.html#TCS-6446) (TCS-6446) | Quantum PCP conjecture with classical reductions | 98 | This asks whether coarse average-energy estimation retains the full difficulty of verification with an arbitrary quantum witness. The per-term normalization prevents a numerical rescaling from creating the required gap. A positive result would give a robust quantum analogue of classical constraint-satisfaction hardness, with consequences for the computational structure of low-energy states. The saved classical-reduction version additionally requires that the hard physical instance be produced without quantum computation. |
| 2 | [BPP versus BQP](index.html#TCS-0036) (TCS-0036) | BPP versus BQP | 98 | This asks whether quantum computation expands the set of efficiently decidable total problems beyond classical randomization. It identifies the exact classical lower bound needed to turn an efficient quantum decision algorithm into an unconditional separation of computational power. |
| 3 | [Area law for gapped two-dimensional Hamiltonians](index.html#TCS-6516) (TCS-6516) | Area law for gapped two-dimensional Hamiltonians | 96 | A central problem in quantum Hamiltonian complexity: whether locality plus a uniform gap controls the quantum information in ground states in two dimensions. It would sharpen the structural foundations of tensor-network methods and separate the task of bounding entanglement from the further task of computing the state. |
| 4 | [Information-theoretic classical verification of quantum computation](index.html#TCS-6580) (TCS-6580) | Information-theoretic classical verification of quantum computation | 96 | The question isolates the resources needed for a classical user to trust a quantum answer. Known protocols obtain trust by giving the verifier some quantum capability, separating several devices, or assuming that particular computations are hard for an attacker. Resolving the stated conjunction would determine whether any of those additional resources is necessary when the honest server itself remains efficient. |
| 5 | [NPT bound entanglement](index.html#TCS-6518) (TCS-6518) | NPT bound entanglement | 94 | A defining question about whether partial-transpose negativity completely captures the possibility of converting bipartite entanglement into useful Bell pairs. Its precise all-copy quantifier connects quantum resource theory to tensor-stable matrix inequalities. |

Candidates considered: TCS-6446, TCS-0036, TCS-6516, TCS-6580, TCS-6518, TCS-6515, TCS-6517, TCS-0037, TCS-6448, TCS-6519, TCS-6520, TCS-2229, TCS-4615, TCS-5077, TCS-6521, TCS-6522, TCS-7308, TCS-0029, TCS-3709, TCS-4734, TCS-4737, TCS-4952, TCS-6449, TCS-6933, TCS-0033, TCS-1961, TCS-2408, TCS-4457, TCS-4753, TCS-4991, TCS-6459, TCS-0027, TCS-1324, TCS-3275, TCS-4715, TCS-4811, TCS-4927, TCS-5202, TCS-0861, TCS-0862, TCS-1882, TCS-4894, TCS-5021, TCS-6447, TCS-6481, TCS-0030, TCS-0031, TCS-0034, TCS-0860, TCS-1259, TCS-2707, TCS-4238.

## Computability and algorithmic information theory

Favor structural laws of computation and explicit frontiers of mathematical knowledge. BB(6) supplies a concrete target alongside degree-theoretic structure; broad randomness and computable-analysis questions precede specialized definability fragments.

Previous prefix: TCS-6646, TCS-6648.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Martin’s conjecture](index.html#TCS-6646) (TCS-6646) | Martin’s conjecture | 96 | Turing degrees encode relative computational power and have a highly non-linear structure. Martin’s conjecture asks whether invariance under mutual computability nevertheless forces every nontrivial operation into an ordered hierarchy once behaviour is compared on cones under determinacy. It gives a precise structural target behind the observed regularity of many degree operators, and connects computability with descriptive set theory and analogous hierarchies of logical strength. |
| 2 | [Busy Beaver \(\mathrm{BB}(6)\)](index.html#TCS-6685) (TCS-6685) | Busy Beaver \(\mathrm{BB}(6)\) | 92 | The halting behavior of a finite set of exceptionally short programs is still beyond complete classification. This problem makes the boundary of current computability knowledge concrete: one additional nonhalting state separates the established five-state maximum from an unresolved maximum with enormous certified examples and difficult residual halting questions. A solution would give a universal exact upper bound for every halting program in this precisely fixed class. |

Candidates considered: TCS-6646, TCS-6685, TCS-6647, TCS-6648, TCS-6105, TCS-6649, TCS-6679, TCS-2202, TCS-5010, TCS-7193, TCS-7461, TCS-7465, TCS-0238, TCS-0247, TCS-0250, TCS-7463, TCS-7470, TCS-0254, TCS-7462, TCS-7466, TCS-7471, TCS-7472, TCS-0287, TCS-4185, TCS-7464, TCS-7468, TCS-0240, TCS-0279, TCS-7467, TCS-7469.

## Proof complexity

Favor limits on general proof systems and the existence of a universally efficient proof formalism. Put central lower bounds and arithmetic strength before refinements of a single proof resource.

Previous prefix: TCS-6601, TCS-6663.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Superpolynomial Extended Frege lower bounds](index.html#TCS-6601) (TCS-6601) | Superpolynomial Extended Frege lower bounds | 98 | Extended Frege captures a powerful form of efficient propositional reasoning with reusable definitions. A superpolynomial lower bound would cross one of the central barriers in proof complexity and clarify whether a standard, highly expressive certificate language necessarily fails on some short true statements. |
| 2 | [Existence of p-optimal proof systems](index.html#TCS-7162) (TCS-7162) | Existence of p-optimal proof systems | 94 | Asks whether one efficiently checkable proof formalism can efficiently absorb every other such formalism. |

Candidates considered: TCS-6601, TCS-7162, TCS-0025, TCS-6663, TCS-5332, TCS-6602, TCS-0024, TCS-1099, TCS-1253, TCS-7273, TCS-1096, TCS-1097, TCS-1098, TCS-5114, TCS-6770, TCS-5333, TCS-6759, TCS-6766, TCS-6768, TCS-6771, TCS-2889, TCS-5292, TCS-6767, TCS-7163, TCS-0071, TCS-4982.

## Communication complexity and Boolean function analysis

Favor structural relations between algebra, information and communication. General compression, lifting and direct-sum principles precede exact costs of particular predicates.

Previous prefix: TCS-6603, TCS-6604.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Log-rank conjecture](index.html#TCS-6603) (TCS-6603) | Log-rank conjecture | 98 | One of the central organizing conjectures of communication complexity. It asks whether a basic linear-algebraic quantity characterizes efficient exact communication, and connects protocols to rectangle partitions, discrepancy, graph structure, and cancellation in matrix decompositions. |
| 2 | [Fourier Entropy–Influence conjecture](index.html#TCS-6604) (TCS-6604) | Fourier Entropy–Influence conjecture | 96 | A central structural conjecture connecting sensitivity to spectral information. Its resolution would sharpen our understanding of Boolean functions and spectral learning, while testing a relation that fails without the Boolean constraint. |

Candidates considered: TCS-6603, TCS-6604, TCS-6581, TCS-6605, TCS-5326, TCS-6450, TCS-6664, TCS-7219, TCS-1047, TCS-1059, TCS-1061, TCS-5892, TCS-6710, TCS-0811, TCS-2658, TCS-3153, TCS-6708, TCS-6711, TCS-2571, TCS-4771, TCS-5272, TCS-6705, TCS-6707, TCS-0540, TCS-2664, TCS-5189, TCS-0218, TCS-1845.

## Fine-grained complexity

Favor the main fine-grained barriers and reductions that connect seemingly different primitives. Prefer a distinct algorithmic bottleneck to another variant of the same hypothesis.

Previous prefix: TCS-6595, TCS-6510.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Strong Exponential Time Hypothesis](index.html#TCS-6595) (TCS-6595) | Strong Exponential Time Hypothesis | 96 | SETH is one of the main assumptions used to explain why specific polynomial running-time exponents resist improvement. Settling it would test the foundation of a broad network of tight conditional bounds in strings, graphs, data structures, and exact exponential-time algorithms. |
| 2 | [Truly subcubic APSP](index.html#TCS-6510) (TCS-6510) | Truly subcubic APSP | 96 | All-pairs distances are a basic graph primitive. A fixed improvement over the cubic exponent would also change the complexity of several equivalent path, matrix and weighted-triangle problems. Their reductions make the exact weight and machine assumptions essential to interpreting claimed improvements. |

Candidates considered: TCS-6595, TCS-6510, TCS-0557, TCS-6503, TCS-7179, TCS-6596, TCS-6597, TCS-6598, TCS-6935, TCS-6937, TCS-7313, TCS-6661, TCS-6946, TCS-6950, TCS-7270, TCS-0562, TCS-0815, TCS-6599, TCS-6944, TCS-6949, TCS-7347, TCS-5422, TCS-6942, TCS-6945, TCS-7373, TCS-0560, TCS-0761, TCS-6025.

## Pseudorandomness and derandomization

Favor removing randomness as a general computational resource and constructing objects at their natural information limits. Broad hardness-randomness principles precede a particular seed-length improvement.

Previous prefix: TCS-0003, TCS-6600.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [P versus BPP](index.html#TCS-0003) (TCS-0003) | P versus BPP | 100 | This asks whether independent random bits increase the set of total decision problems solvable efficiently. An equality would identify deterministic and randomized polynomial-time decision power; a separation would exhibit an inherent benefit of randomness even when a different deterministic algorithm is allowed. |
| 2 | [L versus BPL](index.html#TCS-0026) (TCS-0026) | L versus BPL | 96 | This asks whether randomness adds computational power when an algorithm can remember only logarithmically many bits of an arbitrarily long input. An equality would permit deterministic bounded-memory decision whenever bounded-error randomized decision is possible; a separation would show an inherent memory advantage of randomness. |

Candidates considered: TCS-0003, TCS-0026, TCS-6600, TCS-6686, TCS-6662, TCS-6699, TCS-1005, TCS-5287, TCS-5341, TCS-6696, TCS-6879, TCS-7271, TCS-1015, TCS-1016, TCS-1021, TCS-1022, TCS-5798, TCS-6693, TCS-6729, TCS-1006, TCS-1013, TCS-1014, TCS-1122, TCS-1125, TCS-1133, TCS-6689, TCS-1008, TCS-1124, TCS-1131, TCS-1956, TCS-2201, TCS-3958, TCS-4778, TCS-0854, TCS-1007, TCS-1018, TCS-1019, TCS-1135, TCS-1137, TCS-3986.

## Parameterized complexity and algorithms

Favor whether parameterization truly enables tractability and whether iconic exact algorithms can break long-standing exponential barriers. Broad kernelization and width principles precede individual deletion variants.

Previous prefix: TCS-6592, TCS-6593.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FPT versus \(\mathrm{W}[1]\)](index.html#TCS-6592) (TCS-6592) | FPT versus \(\mathrm{W}[1]\) | 98 | This is the principal boundary question for algorithms whose exponential difficulty is confined to a small parameter. It determines the force of thousands of parameterized hardness reductions and separates efficient small-solution search from algorithms whose input-size exponent grows with the solution size. |
| 2 | [Breaking the \(2^{n}\) barrier for weighted TSP](index.html#TCS-7233) (TCS-7233) | Breaking the \(2^{n}\) barrier for weighted TSP | 94 | Exact weighted TSP is a basic test of whether optimization over all orders of a set fundamentally requires base-two exponential time. A fixed reduction of that base would save an exponential factor for every sufficiently large instance, even when costs have arbitrary binary representations. Understanding this boundary would distinguish the difficulty of selecting an optimal tour from the already faster task of merely detecting a tour. |

Candidates considered: TCS-6592, TCS-7233, TCS-6593, TCS-4790, TCS-6594, TCS-6731, TCS-6660, TCS-6734, TCS-6974, TCS-7035, TCS-7181, TCS-7241, TCS-0801, TCS-4695, TCS-6379, TCS-6728, TCS-6749, TCS-7312, TCS-0787, TCS-2662, TCS-4289, TCS-5374, TCS-7023, TCS-0597, TCS-0816, TCS-1945, TCS-2804, TCS-6814, TCS-7022, TCS-7247, TCS-0799, TCS-0800, TCS-0808, TCS-3480, TCS-3917, TCS-4440, TCS-7027.

## Approximation algorithms and inapproximability

Favor principles that organize approximation hardness and prominent problems resisting even coarse guarantees. General thresholds and integrality phenomena precede narrow ratio improvements.

Previous prefix: TCS-6587, TCS-0006.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Unique Games Conjecture](index.html#TCS-0006) (TCS-0006) | Unique Games Conjecture | 98 | UGC would turn many conditional approximation thresholds into NP-hardness theorems and explain the optimality of a general SDP framework. Its very simple permutation constraints isolate a fundamental boundary between exact consistency, approximate consistency, and hardness amplification. |
| 2 | [Constant-factor approximation for Densest k-Subgraph](index.html#TCS-6587) (TCS-6587) | Constant-factor approximation for Densest k-Subgraph | 96 | Densest k-Subgraph asks whether a prescribed number of vertices can capture a constant fraction of the greatest possible internal connectivity. Its approximation landscape is a central gap between available algorithms, conditional hardness and what follows from the usual P-versus-NP assumption. The answer also matters for several graph optimization objectives linked to its approximability. |

Candidates considered: TCS-0006, TCS-6587, TCS-7160, TCS-6588, TCS-7266, TCS-7282, TCS-6589, TCS-6591, TCS-6659, TCS-7281, TCS-7356, TCS-6590, TCS-6756, TCS-6757, TCS-7357, TCS-7358, TCS-1930, TCS-5407, TCS-5544, TCS-7318, TCS-7353, TCS-2625, TCS-5787, TCS-6309, TCS-7287, TCS-7354, TCS-0922, TCS-1168, TCS-5554.

## Online algorithms, scheduling and packing

Favor canonical online-information barriers and general selection principles. Keep scheduling and packing prominent in the remainder; narrower model-specific constants come later.

Previous prefix: TCS-6575, TCS-6638.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Deterministic competitiveness of k-server](index.html#TCS-6575) (TCS-6575) | Deterministic competitiveness of k-server | 96 | The k-server problem measures the movement cost of responding to demand without knowing future requests. It includes paging and serves as a basic problem in competitive analysis, with the same number of resources available to the online rule and the offline optimum. |
| 2 | [Matroid secretary conjecture](index.html#TCS-7316) (TCS-7316) | Matroid secretary conjecture | 96 | This is a central question about the power of random arrival order in online selection under general independence constraints. A universal bound would apply across all matroids and is equivalent, through established reductions, to a general random-order contention-resolution guarantee. |

Candidates considered: TCS-6575, TCS-7316, TCS-6576, TCS-6638, TCS-7317, TCS-6577, TCS-6640, TCS-6676, TCS-6721, TCS-5779, TCS-7319, TCS-7473, TCS-7478, TCS-0935, TCS-5030, TCS-6724, TCS-7479, TCS-1529, TCS-5221, TCS-7335, TCS-7474, TCS-1241, TCS-6078, TCS-6836, TCS-7477, TCS-0700, TCS-5252, TCS-7475, TCS-7476.

## Beyond worst-case and average-case analysis

Favor the worst-case/average-case bridge and statistical-computational gaps over the performance of one heuristic. Random combinatorial optimization is attractive when it exposes a genuine algorithmic threshold.

Previous prefix: TCS-6656, TCS-0012.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)](index.html#TCS-0012) (TCS-0012) | Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\) | 98 | Worst-case hardness alone does not explain whether feasible procedures can generate instances that remain difficult on average. Resolving this implication would connect the central decision-class separation to robust limits on exact computation under efficiently generated inputs. |
| 2 | [Planted clique conjecture](index.html#TCS-6656) (TCS-6656) | Planted clique conjecture | 94 | A foundational average-case hardness hypothesis, planted clique isolates a gap between statistical information and efficient computation. The hidden clique is far larger than cliques arising by chance, yet no unrestricted polynomial-time detector is established in this regime. Related assumptions support hardness results for estimation, clustering and other inference tasks. Proving this formulation would imply Boolean \(\mathrm P\ne\mathrm{NP}\): a polynomial-time general clique decider would distinguish these distributions once \(k_n\) exceeds the typical null clique size. |

Candidates considered: TCS-0012, TCS-6656, TCS-6657, TCS-6684, TCS-7238, TCS-4876, TCS-6453, TCS-6702, TCS-5011, TCS-5406, TCS-6658, TCS-6703, TCS-7148, TCS-7378, TCS-7379, TCS-7388, TCS-7402, TCS-7381.

## Sampling, Markov chains and mixing times

Favor mixing at natural uniqueness or criticality boundaries and general principles of random exploration. Critical physical dynamics and combinatorial sampling take precedence over a specialized implementation improvement.

Previous prefix: TCS-6621, TCS-6622.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Rapid mixing of Glauber dynamics with \(\Delta +2\) colours](index.html#TCS-6621) (TCS-6621) | Rapid mixing of Glauber dynamics with \(\Delta +2\) colours | 94 | This tests whether the simplest local update rule samples proper colourings efficiently throughout the full range where it is guaranteed to move between all solutions. It connects random sampling, approximate counting and antiferromagnetic spin systems at a longstanding boundary for general graphs. |
| 2 | [Polynomial mixing of critical three-dimensional Ising dynamics](index.html#TCS-6668) (TCS-6668) | Polynomial mixing of critical three-dimensional Ising dynamics | 90 | This is a basic question about whether a standard local sampling dynamics remains efficient at a phase transition in three dimensions. The equilibrium system has correlations on many scales, so high-temperature mixing guarantees do not directly apply. A polynomial bound or a superpolynomial obstruction would clarify the computational cost of critical fluctuations in one of the central lattice models. |

Candidates considered: TCS-6621, TCS-6668, TCS-6622, TCS-6843, TCS-7480, TCS-7485, TCS-6839, TCS-6840, TCS-6857, TCS-7481, TCS-7483, TCS-2861, TCS-7386, TCS-7404, TCS-6851, TCS-7482, TCS-7484.

## Counting and enumeration

Favor canonical approximate-counting barriers and the decision/counting distinction. General enumeration principles come before Gray-code variants and refinements of one counting algorithm.

Previous prefix: TCS-6628, TCS-7221.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [FPRAS for counting perfect matchings](index.html#TCS-6628) (TCS-6628) | FPRAS for counting perfect matchings | 94 | A canonical unresolved problem in approximate counting, separating efficient existence testing from estimating the number of solutions. It also controls the approximability of other counting and partition-function problems through reductions. |
| 2 | [FPRAS for #BIS](index.html#TCS-7221) (TCS-7221) | FPRAS for #BIS | 94 | The canonical unresolved boundary in approximate counting: many counting problems share its approximation difficulty, while exact counting hardness does not settle whether a randomized relative approximation is efficient. A general scheme would transfer to problems reducible to it with preserved approximation guarantees; an impossibility proof would separate this central family from the counting problems with known fully polynomial schemes. |

Candidates considered: TCS-6628, TCS-7221, TCS-6820, TCS-6629, TCS-6821, TCS-1004, TCS-7112, TCS-7240, TCS-4671, TCS-6671, TCS-7320, TCS-7355, TCS-3037, TCS-3635, TCS-7099, TCS-7084, TCS-7086, TCS-7399, TCS-7488, TCS-7082, TCS-7487, TCS-7486, TCS-7489.

## Structural graph theory and graph algorithms

Favor global structural conjectures and the complexity of graph identity. Exact matching, flow and sparsity barriers lead the algorithmic remainder; close variants and specialized class restrictions follow.

Previous prefix: TCS-6651, TCS-6536.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Hadwiger’s conjecture](index.html#TCS-6651) (TCS-6651) | Hadwiger’s conjecture | 98 | Hadwiger’s conjecture proposes an exact relation between two basic graph parameters: the number of colors needed and the size of a complete graph obtainable by contraction. It extends the Four-Color Theorem and would turn exclusion of a complete minor into the sharp universal coloring bound. Its significance comes from this structural connection across all finite graphs, rather than from an algorithmic requirement in the question. |
| 2 | [Graph isomorphism in polynomial time](index.html#TCS-7222) (TCS-7222) | Graph isomorphism in polynomial time | 96 | Tests whether the central equivalence problem for finite combinatorial structures can be recognized in deterministic polynomial time after the quasipolynomial barrier was broken. |

Candidates considered: TCS-6651, TCS-7222, TCS-6652, TCS-6536, TCS-6538, TCS-7248, TCS-2783, TCS-6500, TCS-6653, TCS-6682, TCS-7216, TCS-7218, TCS-7251, TCS-6511, TCS-6654, TCS-6683, TCS-7228, TCS-7249, TCS-7250, TCS-7253, TCS-7289, TCS-6874, TCS-6875, TCS-0315, TCS-1206, TCS-6539, TCS-6655, TCS-7145, TCS-7180, TCS-7252, TCS-7285, TCS-7341, TCS-7346, TCS-1639, TCS-7143, TCS-7144, TCS-7217, TCS-7245, TCS-7254, TCS-7263, TCS-7342, TCS-7343, TCS-7348, TCS-7394, TCS-0611, TCS-0771, TCS-0775, TCS-1246, TCS-7244, TCS-7344, TCS-7345, TCS-0587, TCS-0594.

## Data structures

Favor universal adaptivity and strong data-structure lower bounds, followed by deterministic basic primitives. Long-standing structural conjectures precede improvements tied to one queue or hashing implementation.

Previous prefix: TCS-6498, TCS-6540.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Dynamic optimality conjecture](index.html#TCS-6498) (TCS-6498) | Dynamic optimality conjecture | 98 | It asks whether a simple local adjustment rule can match every legal strategy with complete knowledge of the future. The issue is fundamental to instance-sensitive data structures: success would replace a growing competitive penalty by a constant for all access patterns. A counterexample would identify a limitation of splaying that its many separate locality guarantees fail to reveal. |
| 2 | [Superlogarithmic static cell-probe lower bounds](index.html#TCS-6540) (TCS-6540) | Superlogarithmic static cell-probe lower bounds | 96 | A central unconditional lower-bound bottleneck for data structures: establish that a short, explicitly defined static query fundamentally needs more than logarithmically many memory accesses despite unrestricted preprocessing. |

Candidates considered: TCS-6498, TCS-6540, TCS-6586, TCS-7331, TCS-7338, TCS-7398, TCS-0949, TCS-5825, TCS-7333, TCS-7334, TCS-0300, TCS-5706, TCS-6508, TCS-7328, TCS-7493, TCS-7329, TCS-7382, TCS-7383, TCS-7497, TCS-7498, TCS-0474, TCS-7327, TCS-7340, TCS-7330, TCS-7401, TCS-7491, TCS-7490.

## Dynamic algorithms

Favor robustness under arbitrary updates for core graph primitives and general limits of dynamic expressiveness. Broader dynamic metatheorems precede improvements for a particular data representation.

Previous prefix: TCS-6625, TCS-6627.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Deterministic fully dynamic connectivity with polylogarithmic worst-case updates](index.html#TCS-6625) (TCS-6625) | Deterministic fully dynamic connectivity with polylogarithmic worst-case updates | 94 | Exact dynamic connectivity is a basic test of whether a graph data structure can guarantee uniformly low latency without randomness. The question separates efficient processing of a long sequence from a fast response after every individual change, and is relevant to graph algorithms that call connectivity as a subroutine. |
| 2 | [Fully dynamic near-optimal matching with polylogarithmic updates](index.html#TCS-6627) (TCS-6627) | Fully dynamic near-optimal matching with polylogarithmic updates | 94 | A single insertion or deletion can change which edges should be used together in a large matching. The question asks whether a near-optimal explicit solution can be kept current at a cost that grows only polylogarithmically with graph size, combining approximation quality with efficient dynamic maintenance. |

Candidates considered: TCS-6625, TCS-6627, TCS-0478, TCS-6626, TCS-6670, TCS-7339, TCS-7437, TCS-7494, TCS-7495, TCS-0541, TCS-0543, TCS-7332, TCS-7387, TCS-7393, TCS-7496, TCS-0387, TCS-5209, TCS-7326, TCS-7436, TCS-7492, TCS-7502, TCS-0536, TCS-3331, TCS-7392, TCS-7501, TCS-0545, TCS-7500, TCS-7503, TCS-7499.

## String algorithms and computational biology

Favor recovering strings from noise and fast comparison of sequences. General compression principles and metric structure precede specialized indexing tradeoffs.

Previous prefix: TCS-6623, TCS-6624.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Worst-case sample complexity of trace reconstruction](index.html#TCS-6623) (TCS-6623) | Worst-case sample complexity of trace reconstruction | 94 | Determine the intrinsic amount of information needed to recover an arbitrary string when repeated observations lose the positions of deleted symbols. This separates the statistical cost of hidden alignment from the computational cost of processing the observations. |
| 2 | [Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time](index.html#TCS-6624) (TCS-6624) | Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time | 94 | This asks whether allowing one universal constant loss of alignment accuracy reduces worst-case sequence comparison to the cost of reading the input, apart from a fixed polylogarithmic overhead. The result would locate a basic computational boundary that remains beyond the known fast constant-factor algorithms. Even a large universal factor would resolve this existence question. |

Candidates considered: TCS-6623, TCS-6624, TCS-6513, TCS-7235, TCS-7297, TCS-6669, TCS-7220, TCS-7322, TCS-7371, TCS-6928, TCS-7367, TCS-7374, TCS-0467, TCS-0468, TCS-7366, TCS-7369, TCS-7375, TCS-0470, TCS-7360, TCS-7364, TCS-7365, TCS-0466, TCS-7361, TCS-7362, TCS-7370, TCS-7368.

## Game theory, social choice and fair division

Favor whether fairness and truthful efficiency are achievable at all. Broad existence and black-box mechanism questions precede exact constants for specialized markets.

Previous prefix: TCS-6632, TCS-0011.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Existence of complete EFX allocations for additive valuations](index.html#TCS-0011) (TCS-0011) | Existence of complete EFX allocations for additive valuations | 96 | Asks whether an indivisible allocation can always control every agent’s envy after the removal of any positively valued good, while distributing all goods. It tests a stronger fairness guarantee than EF1 even before imposing computational efficiency. |
| 2 | [Constant-factor universally truthful auctions for submodular bidders](index.html#TCS-6632) (TCS-6632) | Constant-factor universally truthful auctions for submodular bidders | 92 | Determine whether exact truthful incentives inherently cause an unbounded loss of allocative efficiency, even when arbitrary compact communication and unlimited local optimization are available. |

Candidates considered: TCS-0011, TCS-6632, TCS-6639, TCS-6674, TCS-7507, TCS-7510, TCS-0056, TCS-6633, TCS-7505, TCS-7508, TCS-0571, TCS-1108, TCS-1109, TCS-1115, TCS-1116, TCS-7197, TCS-7200, TCS-0073, TCS-4584, TCS-6634, TCS-7196, TCS-7203, TCS-1714, TCS-7504, TCS-7506, TCS-7511, TCS-7509.

## Algebraic computation

Favor the cost of basic algebraic computation and general lower-bound/derandomization barriers. Keep broad algebraic decidability questions high, while placing restricted circuit refinements below the central separations.

Previous prefix: TCS-0007, TCS-6611.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Matrix multiplication exponent](index.html#TCS-0007) (TCS-0007) | Matrix multiplication exponent | 100 | This exponent measures the asymptotic arithmetic cost of a fundamental operation and governs many other algebraic and graph algorithms. Determining its value would locate the limit of savings from shared computation. |
| 2 | [VP versus VNP](index.html#TCS-0005) (TCS-0005) | VP versus VNP | 100 | This is the central equality question for general arithmetic computation. It asks whether a polynomial-size algebraic computation can always absorb a sum over exponentially many Boolean witnesses, with the permanent serving as a complete concrete target. A separation would establish a general limitation despite arbitrary constants, cancellations and reuse; equality would give polynomial-size circuits for every polynomial family in VNP. |

Candidates considered: TCS-0007, TCS-0005, TCS-6611, TCS-7113, TCS-6612, TCS-6613, TCS-6614, TCS-6666, TCS-6888, TCS-0009, TCS-0010, TCS-6641, TCS-6895, TCS-7174, TCS-7262, TCS-0055, TCS-1058, TCS-6615, TCS-6642, TCS-6677, TCS-6890, TCS-6893, TCS-6898, TCS-7175, TCS-7223, TCS-2039, TCS-2506, TCS-5520, TCS-5921, TCS-6616, TCS-6883, TCS-6884, TCS-6897, TCS-6903, TCS-7269, TCS-0046, TCS-0481, TCS-1101, TCS-1102, TCS-1103, TCS-3318, TCS-5260, TCS-6493, TCS-6882, TCS-0047, TCS-1151, TCS-1544, TCS-2958, TCS-3959, TCS-4523, TCS-5240, TCS-7224, TCS-7372, TCS-0095, TCS-1069, TCS-2077, TCS-2718, TCS-4350, TCS-4490, TCS-5739.

## Lattices and computational number theory

Favor computability of rational arithmetic and central number-theoretic algorithms. Broad lattice approximation and cryptographic foundations precede sharper constants in a particular reduction.

Previous prefix: TCS-6571, TCS-6667.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Hilbert’s tenth problem over the rationals](index.html#TCS-6571) (TCS-6571) | Hilbert’s tenth problem over the rationals | 98 | This asks whether exact rational polynomial constraints admit any general terminating solver. It connects the computability of arithmetic, logical definability and the existence of rational points on algebraic varieties. The unresolved boundary persists despite undecidability over the integers and decidability of polynomial feasibility over the reals and algebraically closed fields; allowing fractions fundamentally changes the permitted witnesses. |
| 2 | [Integer factorization in randomized polynomial time](index.html#TCS-6617) (TCS-6617) | Integer factorization in randomized polynomial time | 96 | Integer factorization is a basic inverse problem in arithmetic and a central test case for the potential power of quantum computation. Its classical complexity has direct consequences for factoring-based cryptography and for algorithms that currently require access to a factoring subroutine. |

Candidates considered: TCS-6571, TCS-6617, TCS-6618, TCS-6667, TCS-6620, TCS-7169, TCS-7234, TCS-7265, TCS-0655, TCS-0658, TCS-6619, TCS-6863, TCS-0656, TCS-6861, TCS-6864, TCS-7170, TCS-7171, TCS-0648, TCS-0652, TCS-0659, TCS-5317, TCS-5395, TCS-0657, TCS-0661, TCS-1170, TCS-0653, TCS-0662.

## Coding and information theory

Favor fundamental coding tradeoffs and multiuser information limits. Local decoding and computability of capacity remain central; already-known approximation targets rank lower as research questions while remaining eligible formalization tasks.

Previous prefix: TCS-6606, TCS-1010.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Optimal asymptotic binary rate–distance tradeoff](index.html#TCS-1010) (TCS-1010) | Optimal asymptotic binary rate–distance tradeoff | 98 | This function is the intrinsic packing limit for binary information protected against worst-case substitutions. Determining it to a certified rate accuracy would quantify the necessary redundancy independently of how a code is represented, constructed or decoded. Exact determination would settle a foundational coding-theory question; the selected tolerance is a distinct, weaker benchmark target. |
| 2 | [Capacity of the two-user Gaussian interference channel](index.html#TCS-6606) (TCS-6606) | Capacity of the two-user Gaussian interference channel | 96 | A defining problem in network information theory: even two interfering sender–receiver pairs expose limits of our ability to characterize optimal communication. An exact solution would distinguish which forms of message splitting, interference decoding and power allocation are fundamentally necessary. |

Candidates considered: TCS-1010, TCS-6606, TCS-6665, TCS-6584, TCS-7210, TCS-7267, TCS-1020, TCS-6608, TCS-6609, TCS-6610, TCS-7211, TCS-7215, TCS-0013, TCS-1012, TCS-4524, TCS-4968, TCS-6738, TCS-7214, TCS-0196, TCS-1011, TCS-0184, TCS-3513, TCS-4802, TCS-0178, TCS-0187, TCS-0205, TCS-6607.

## Property testing and distribution learning

Favor general characterizations of what can be learned from local access and the gap between testing and estimation. Strong structural properties follow before specialized query-model refinements.

Previous prefix: TCS-6630, TCS-1033.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Effective classification of polynomially testable hereditary graph properties](index.html#TCS-6630) (TCS-6630) | Effective classification of polynomially testable hereditary graph properties | 92 | Asks whether the efficient sampling regime of hereditary graph testing can be recognized from a finite description, turning a broad classification programme into a precise decidability target. |
| 2 | [Polynomial testability versus distance estimation](index.html#TCS-1033) (TCS-1033) | Polynomial testability versus distance estimation | 92 | A decision tester recognizes only a large violation, whereas a distance estimator measures the minimum repair needed at every distance scale. A general polynomial implication would transfer efficient sampling guarantees to quantitative assessment across the dense-graph model. A separating property would establish an information-cost distinction between these two basic tasks even when unlimited local computation is allowed. |

Candidates considered: TCS-6630, TCS-1033, TCS-1029, TCS-5443, TCS-0848, TCS-4376, TCS-6672, TCS-7384, TCS-1030, TCS-5085, TCS-7385, TCS-7396, TCS-0672, TCS-2535, TCS-3906, TCS-7395, TCS-0841, TCS-0847, TCS-4259, TCS-5210.

## Differential privacy

Favor general private learnability and the computational limits of releasing rich statistical information. Sequential privacy costs remain important but follow these broader boundaries.

Previous prefix: TCS-0506, TCS-6673.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Private PAC sample complexity from VC and Littlestone dimensions](index.html#TCS-0506) (TCS-0506) | Private PAC sample complexity from VC and Littlestone dimensions | 92 | The theorem characterizing whether private learning is possible leaves an enormous quantitative gap. This question asks whether the extra data needed for privacy is controlled by ordinary statistical complexity and an exceptionally slowly growing function of sequential complexity. A positive answer would put a uniform bound on that privacy overhead across all finite concept classes. |
| 2 | [Polynomial-time private release of all marginals](index.html#TCS-7236) (TCS-7236) | Polynomial-time private release of all marginals | 88 | Marginals are basic summaries of relationships among attributes. The question asks whether the large information-theoretic usefulness of private high-dimensional data can be captured by a compact, efficiently evaluated object using polynomially many records. It isolates a statistical-versus-computational gap for a concrete query family while allowing outputs more flexible than synthetic datasets. |

Candidates considered: TCS-0506, TCS-7236, TCS-6673, TCS-7390, TCS-0507, TCS-7391.

## Constraint satisfaction

Favor general tractability classifications and the elementary promise of coloring an already three-colorable graph. Structural explanations and search/decision equivalences precede more restricted meta-problems.

Previous prefix: TCS-6635, TCS-6636.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Finite-domain promise CSP dichotomy](index.html#TCS-6635) (TCS-6635) | Finite-domain promise CSP dichotomy | 96 | This asks whether finite local constraint descriptions force a sharp complexity classification even when the accepted and rejected instances are separated by a promise. It encompasses approximate graph colouring and many relaxed feasibility problems. A resolution would determine whether the organizing principle of the finite CSP dichotomy extends beyond exact satisfaction, or whether a fixed finite promise can have intermediate decision complexity. |
| 2 | [Constant-colour polynomial-time colouring of 3-colourable graphs](index.html#TCS-6637) (TCS-6637) | Constant-colour polynomial-time colouring of 3-colourable graphs | 94 | A defining promise-CSP problem: determine whether relaxing an NP-hard colouring task to any fixed larger palette permits efficient construction of a valid solution. |

Candidates considered: TCS-6635, TCS-6637, TCS-6636, TCS-6675, TCS-6725, TCS-7237, TCS-1173, TCS-1807, TCS-6748, TCS-7116, TCS-0504, TCS-1555, TCS-1978, TCS-3984, TCS-0441, TCS-0444, TCS-3585, TCS-3678.

## Automated reasoning, rewriting and unification

Favor the basic decidability and complexity of symbolic equations. General rewriting and unification principles follow; implementation-level refinements of restricted representations come later.

Previous prefix: TCS-6562, TCS-6643.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Word equations with linear length constraints](index.html#TCS-6562) (TCS-6562) | Word equations with linear length constraints | 94 | A fundamental boundary for reasoning about concatenation and numerical size simultaneously. It governs whether a complete terminating solver can exist for a basic fragment of string constraints used in verification, while connecting free-monoid equations, arithmetic and reachability. |
| 2 | [NP membership of word-equation satisfiability](index.html#TCS-0163) (TCS-0163) | NP membership of word-equation satisfiability | 90 | Word equations are a basic model of string constraints and associative unification. Their decidability is established, but the gap between NP-hardness and polynomial-space algorithms leaves the complexity of short verifiable evidence unresolved. NP membership would place the unrestricted satisfiability problem at the familiar NP-complete boundary. |

Candidates considered: TCS-6562, TCS-0163, TCS-1992, TCS-6643, TCS-6644, TCS-7194, TCS-7239, TCS-7405, TCS-7411, TCS-1595, TCS-6650, TCS-7125, TCS-7424, TCS-0114, TCS-7134, TCS-7434, TCS-0306, TCS-5603, TCS-7421, TCS-7420.

## Database theory and finite model theory

Favor a syntax for efficient computation and structural characterizations of tractable model checking. General query semantics and enumeration principles precede specialized representation gaps.

Previous prefix: TCS-6678, TCS-6645.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [A logic capturing polynomial time](index.html#TCS-7195) (TCS-7195) | A logic capturing polynomial time | 98 | The central descriptive-complexity question of characterizing feasible computation without supplying an arbitrary order. |
| 2 | [FO model checking on hereditary monadically dependent graph classes](index.html#TCS-6678) (TCS-6678) | FO model checking on hereditary monadically dependent graph classes | 92 | First-order formulas express a broad family of graph queries, but direct evaluation lets the graph-size exponent grow with the query. The proposed structural condition aims to explain when that dependence can be confined to a computable function of the query alone, even on dense graph classes. Settling this tractability direction would complement the established hardness of hereditary classes that can logically encode arbitrary graphs. |

Candidates considered: TCS-7195, TCS-6678, TCS-7232, TCS-3631, TCS-6645, TCS-0492, TCS-6680, TCS-7415, TCS-7422, TCS-0488, TCS-0494, TCS-4458, TCS-6372, TCS-7429, TCS-0482, TCS-0499, TCS-0505, TCS-4995, TCS-0487, TCS-0502, TCS-3557, TCS-7128.

## Miscellaneous

Both are compact, striking combinatorial conjectures. Prefer the sunflower question for its broader complexity connections, followed by the balanced-comparison principle for partial orders.

Previous prefix: TCS-7177.

| Position | Problem | Topic | Saved importance score | Selection rationale |
| ---: | --- | --- | ---: | --- |
| 1 | [Sunflower conjecture](index.html#TCS-7290) (TCS-7290) | Sunflower conjecture | 94 | A general combinatorial principle with established applications to computational lower bounds and parameterized reductions. |
| 2 | [\(1/3\)–\(2/3\) conjecture](index.html#TCS-7177) (TCS-7177) | \(1/3\)–\(2/3\) conjecture | 88 | Asks for the sharp universal quality of a comparison when sorting with partial information. It connects uncertainty among compatible rankings to an extremal property of every finite partial order. |

Candidates considered: TCS-7290, TCS-7177.
