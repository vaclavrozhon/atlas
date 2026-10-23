# Source candidates from the supplied catalogue v16

Imported 135 new candidates (TCS-7377–TCS-7511) on 2026-10-23, bringing the active catalogue from 985 to 1,120 cards. All 985 previously active card files are byte-for-byte unchanged.

The source is the user-supplied raw.txt, containing 1,344 descriptions. Its historical cutoff is 2026-01-01; its preparation date is 2026-10-21. The source SHA-256 is cbd4d40c948d9da52fc5dca09047dd13df43b7ff1dc05eb7e933c0f3c39f7431.

## Editorial scope

The user requested 100–200 additions, prioritizing sparsely represented categories, as source candidates with citations and explicit gaps. Original area headings were treated as suggestions. Assignments follow the mathematical target: dynamic logical queries go to dynamic algorithms, private learning targets to differential privacy, and counting/enumeration targets to Counting and enumeration.

Each candidate has an individually written provisional statement, motivation, remaining specification issue, supplied bibliography, and traceable source location. Every new card has evidence=source, status=uncertain, statement_review=needs_specification, and an unassessed importance score. No candidate is certified as currently open, self-contained, or literature-reviewed. Four classification questions deliberately omit question_type rather than pretending to ask for a numeric curve. User-supplied researcher associations are editorial connections, not claims of authorship or personal research agendas.

Selection used comparisons with active cards and manual screening of titles, statements, and caveats. Known duplicates and full-resolution warnings noticed in this process were excluded. This is not an exhaustive semantic-deduplication or current-status audit of all 1,344 descriptions. Archived cards were not reconsidered. Closely related but distinct targets retain separate candidate cards with explicit gaps and selected related-problem links.

## Category coverage

Coverage counts describe active cards, not benchmark selection or importance rankings. Sparsity was a priority, not a quota: only two suitable new differential-privacy candidates were retained. No additions were placed in Miscellaneous.

| Category | Before | Added | After |
| --- | ---: | ---: | ---: |
| Differential privacy | 4 | 2 | 6 |
| Randomized algorithms and sampling | 9 | 8 | 17 |
| Beyond worst-case and average-case analysis | 13 | 5 | 18 |
| Automated reasoning and unification | 14 | 6 | 20 |
| Dynamic graph algorithms | 15 | 14 | 29 |
| Property testing and distribution learning | 16 | 4 | 20 |
| Computability and algorithmic information | 18 | 12 | 30 |
| Counting and enumeration | 18 | 5 | 23 |
| Data structures | 18 | 9 | 27 |
| Algorithmic game theory, mechanism design and fair division | 19 | 8 | 27 |
| Database theory and finite model theory | 19 | 3 | 22 |
| Online algorithms | 22 | 7 | 29 |
| Optimization and numerics | 24 | 11 | 35 |
| Algorithms & data structures | 27 | 1 | 28 |
| Cryptography | 30 | 10 | 40 |
| Automata and formal languages | 31 | 9 | 40 |
| Learning theory | 36 | 4 | 40 |
| Semantics, logic and verification | 38 | 13 | 51 |
| Computational geometry and metric spaces | 40 | 2 | 42 |
| Structural graph theory | 52 | 1 | 53 |
| Distributed, parallel and sublinear algorithms | 53 | 1 | 54 |

## Screening examples and source checks

Examples of excluded overlaps (input index → existing active ID): 42 → TCS-6625; 281 → TCS-7326; 310 → TCS-6626; 622 → TCS-0724; 1098 → TCS-5825; 1129 → TCS-7328; 1130 → TCS-0474; 1132 → TCS-7112. Input 193 was dropped because the existing adaptive-adversary formulation in TCS-0543 already permits the proposed deterministic special case.

Examples excluded because the supplied text flagged full resolutions or announcements: 608, 611, 630, 1068, 1070, 519, 548, 370, 393, 426, 1201, and 1203. Those warnings guided exclusion; they were not independently certified as proofs.

Limited independent primary-source checks were recorded for 14 selected entries (1048, 1055, 1056, 1071, 1072, 229, 230, 344, 524, 764, 805, 806, 1003, 1004). These checks establish specific source details only; they do not certify present-day openness. The other bibliographic labels and links are preserved from the supplied text and await individual verification.

A substantive correction was made to the Flowing conjecture (input 524): its third forbidden clutter is the complements of cuts of K5, following [Guenin's statement](https://www.math.uwaterloo.ca/~bguenin/covering.html). The input's blocker-of-the-latter wording was not adopted. Gray-code targets distinguish paths from cycles, and computable-categoricity targets retain topological rather than isometric equivalence.

## Reproduction and audit files

source-entries.json preserves the 135 selected source excerpts. curation.tsv contains the individual edited statements, motivations, and gaps. selection-groups.json records editorial category assignments. prepare_import.py creates new-cards.json and relations.json; scripts/import_cards.py allocates stable IDs and skips already-imported source keys. finalize_import.py resolves relations, checks old-file hashes and candidate metadata, and regenerates this report and import-result.json. baseline.json stores the original counts and file hashes. validation.json records the completed validation commands.

The canonical cards are in data/cards. Generated publication files stay in the ignored build directory. No publication or remote push is performed by these research scripts.

## Added cards

| ID | Candidate | Category | Source entry |
| --- | --- | --- | --- |
| [TCS-7377](../../data/cards/TCS-7377.json) | Truly subquadratic exact Euclidean bipartite matching | Computational geometry and metric spaces | Algorithms/7B |
| [TCS-7378](../../data/cards/TCS-7378.json) | Asymptotically optimal algorithms for random three-dimensional assignment | Beyond worst-case and average-case analysis | Algorithms/22A |
| [TCS-7379](../../data/cards/TCS-7379.json) | Polynomial-time exact optimization of random asymmetric TSP | Beyond worst-case and average-case analysis | Algorithms/22B |
| [TCS-7380](../../data/cards/TCS-7380.json) | Size-bounded approximate multicommodity-flow sparsifiers | Algorithms & data structures | Algorithms/24B |
| [TCS-7381](../../data/cards/TCS-7381.json) | Exact random-order ratio of Best Fit bin packing | Beyond worst-case and average-case analysis | Algorithms/27A |
| [TCS-7382](../../data/cards/TCS-7382.json) | Optimal distance oracles that also report paths | Data structures | Algorithms/43A |
| [TCS-7383](../../data/cards/TCS-7383.json) | Truly subquadratic preprocessing for stretch-3 distance oracles | Data structures | Algorithms/56A |
| [TCS-7384](../../data/cards/TCS-7384.json) | Complexity of tolerant monotonicity testing | Property testing and distribution learning | Algorithms/65A |
| [TCS-7385](../../data/cards/TCS-7385.json) | Efficient black-box testing of high-dimensional convexity | Property testing and distribution learning | Algorithms/65B |
| [TCS-7386](../../data/cards/TCS-7386.json) | General characterization of parallel random-walk cover time | Randomized algorithms and sampling | Algorithms/92A |
| [TCS-7387](../../data/cards/TCS-7387.json) | Fast constant-factor fully dynamic edit distance | Dynamic graph algorithms | Algorithms/94A |
| [TCS-7388](../../data/cards/TCS-7388.json) | Average-case optimality of standard Shellsort | Beyond worst-case and average-case analysis | Algorithms/96A |
| [TCS-7389](../../data/cards/TCS-7389.json) | Nearly quadratic oracle complexity for convex-body volume | Optimization and numerics | Algorithms/99B |
| [TCS-7390](../../data/cards/TCS-7390.json) | Additive privacy cost for adversarial bandits | Differential privacy | Algorithms/115A |
| [TCS-7391](../../data/cards/TCS-7391.json) | Optimal private sample complexity for nonsmooth nonconvex optimization | Differential privacy | Algorithms/115B |
| [TCS-7392](../../data/cards/TCS-7392.json) | Deterministic \(\widetilde O(n^{5/2})\) worst-case dynamic APSP | Dynamic graph algorithms | Algorithms/123A |
| [TCS-7393](../../data/cards/TCS-7393.json) | Deterministic worst-case polylogarithmic dynamic 2-edge-connectivity | Dynamic graph algorithms | Algorithms/123B |
| [TCS-7394](../../data/cards/TCS-7394.json) | Near-linear-space exact planar distance oracles with polylogarithmic queries | Structural graph theory | Algorithms/128B |
| [TCS-7395](../../data/cards/TCS-7395.json) | Polynomial accuracy dependence for sublinear LIS estimation | Property testing and distribution learning | Algorithms/131A |
| [TCS-7396](../../data/cards/TCS-7396.json) | Estimating sparse finite-field matrix rank with sublinear queries | Property testing and distribution learning | Algorithms/140A |
| [TCS-7397](../../data/cards/TCS-7397.json) | Truly linear-time Laplacian solving | Optimization and numerics | Algorithms/143A |
| [TCS-7398](../../data/cards/TCS-7398.json) | Polynomial lower bounds for adaptive dynamic data structures | Data structures | Algorithms/147A |
| [TCS-7399](../../data/cards/TCS-7399.json) | Nearly linear approximate counting for knapsack | Counting and enumeration | Algorithms/148B |
| [TCS-7400](../../data/cards/TCS-7400.json) | One-pass approximation scheme for random-order streaming matching | Distributed, parallel and sublinear algorithms | Algorithms/149B |
| [TCS-7401](../../data/cards/TCS-7401.json) | Computing optimal generalized binary split trees | Data structures | Algorithms/150A |
| [TCS-7402](../../data/cards/TCS-7402.json) | Instance-optimal outer approximation of convex polytopes | Beyond worst-case and average-case analysis | Algorithms/153A |
| [TCS-7403](../../data/cards/TCS-7403.json) | Optimal space–query tradeoff for approximate Voronoi diagrams | Computational geometry and metric spaces | Algorithms/153B |
| [TCS-7404](../../data/cards/TCS-7404.json) | Exact uniform spanning-tree sampling in linear time | Randomized algorithms and sampling | Algorithms/168A |
| [TCS-7405](../../data/cards/TCS-7405.json) | Madlener–Otto plain-group conjecture | Automated reasoning and unification | Automata and formal languages/2B |
| [TCS-7406](../../data/cards/TCS-7406.json) | Complement closure of conjunctive languages | Automata and formal languages | Automata and formal languages/3A |
| [TCS-7407](../../data/cards/TCS-7407.json) | Greibach normal form for conjunctive grammars | Automata and formal languages | Automata and formal languages/3B |
| [TCS-7408](../../data/cards/TCS-7408.json) | Deciding pattern avoidance over a prescribed alphabet | Automata and formal languages | Automata and formal languages/6B |
| [TCS-7409](../../data/cards/TCS-7409.json) | Dense periodic behavior in surjective one-dimensional cellular automata | Automata and formal languages | Automata and formal languages/7A |
| [TCS-7410](../../data/cards/TCS-7410.json) | Nondeterminism versus determinism with two two-way heads | Automata and formal languages | Automata and formal languages/8B |
| [TCS-7411](../../data/cards/TCS-7411.json) | NP membership of context unification | Automated reasoning and unification | Automata and formal languages/12A |
| [TCS-7412](../../data/cards/TCS-7412.json) | Isomorphism of tree-automatic ordinals without addition | Automata and formal languages | Automata and formal languages/17A |
| [TCS-7413](../../data/cards/TCS-7413.json) | Complement closure of deterministic finite-testable counter languages | Automata and formal languages | Automata and formal languages/20A |
| [TCS-7414](../../data/cards/TCS-7414.json) | Complementing unambiguous partially blind counter languages | Automata and formal languages | Automata and formal languages/20B |
| [TCS-7415](../../data/cards/TCS-7415.json) | Fagin’s binary-relation spectrum problem | Database theory and finite model theory | Semantics, logic and verification/3B |
| [TCS-7416](../../data/cards/TCS-7416.json) | Craig interpolation for Gödel logic with function symbols | Semantics, logic and verification | Semantics, logic and verification/4A |
| [TCS-7417](../../data/cards/TCS-7417.json) | Effective prenex normalization for countable Gödel truth-value sets | Semantics, logic and verification | Semantics, logic and verification/4B |
| [TCS-7418](../../data/cards/TCS-7418.json) | Deciding MSO-definable choice on the infinite binary tree | Semantics, logic and verification | Semantics, logic and verification/5A |
| [TCS-7419](../../data/cards/TCS-7419.json) | Continuous-time synthesis for Metric Interval Temporal Logic | Semantics, logic and verification | Semantics, logic and verification/5B |
| [TCS-7420](../../data/cards/TCS-7420.json) | Recognizing minimally false quantified formulas of fixed deficiency | Automated reasoning and unification | Semantics, logic and verification/7A |
| [TCS-7421](../../data/cards/TCS-7421.json) | Near-linear equivalence testing for propositional Horn theories | Automated reasoning and unification | Semantics, logic and verification/7B |
| [TCS-7422](../../data/cards/TCS-7422.json) | Effective syntax for order-invariant first-order queries | Database theory and finite model theory | Semantics, logic and verification/10B |
| [TCS-7423](../../data/cards/TCS-7423.json) | Polynomial-time quantitative stochastic parity verification | Semantics, logic and verification | Semantics, logic and verification/12B |
| [TCS-7424](../../data/cards/TCS-7424.json) | Probabilistic Newman lemma with ordinary local confluence | Automated reasoning and unification | Semantics, logic and verification/13A |
| [TCS-7425](../../data/cards/TCS-7425.json) | Fully abstract game semantics for pure call-by-value | Semantics, logic and verification | Semantics, logic and verification/13B |
| [TCS-7426](../../data/cards/TCS-7426.json) | Finite algebraic axiomatization of full guarded KAT | Semantics, logic and verification | Semantics, logic and verification/14B |
| [TCS-7427](../../data/cards/TCS-7427.json) | Cut elimination for \(\mu\mathrm{LK}_{p}^{+}\) | Semantics, logic and verification | Semantics, logic and verification/16B |
| [TCS-7428](../../data/cards/TCS-7428.json) | Commutativity of the full probabilistic powerdomain monad | Semantics, logic and verification | Semantics, logic and verification/17A |
| [TCS-7429](../../data/cards/TCS-7429.json) | Eliminating an invariant order on bounded-degree structures | Database theory and finite model theory | Semantics, logic and verification/18B |
| [TCS-7430](../../data/cards/TCS-7430.json) | Decidability of the infinite target discounted-sum problem | Semantics, logic and verification | Semantics, logic and verification/19B |
| [TCS-7431](../../data/cards/TCS-7431.json) | Decidability of the nondeterministic tree-automaton index problem | Automata and formal languages | Semantics, logic and verification/20B |
| [TCS-7432](../../data/cards/TCS-7432.json) | Satisfiability with two variables and one transitive relation | Semantics, logic and verification | Semantics, logic and verification/22A |
| [TCS-7433](../../data/cards/TCS-7433.json) | Decidability of the full alternating uniform one-dimensional fragment | Semantics, logic and verification | Semantics, logic and verification/22B |
| [TCS-7434](../../data/cards/TCS-7434.json) | Perpetual reduction for the \(\lambda\sigma\) calculus | Automated reasoning and unification | Semantics, logic and verification/23A |
| [TCS-7435](../../data/cards/TCS-7435.json) | Uniform cut elimination with digging and fixed points | Semantics, logic and verification | Semantics, logic and verification/25A |
| [TCS-7436](../../data/cards/TCS-7436.json) | DynProp maintenance of directed reachability | Dynamic graph algorithms | Semantics, logic and verification/26A |
| [TCS-7437](../../data/cards/TCS-7437.json) | Polynomial-time query outside DynFO | Dynamic graph algorithms | Semantics, logic and verification/26B |
| [TCS-7438](../../data/cards/TCS-7438.json) | Polynomial-time integer programming with bounded subdeterminants | Optimization and numerics | Optimization and numerical computation/3A |
| [TCS-7439](../../data/cards/TCS-7439.json) | Linear bound in the flatness theorem | Optimization and numerics | Optimization and numerical computation/3B |
| [TCS-7440](../../data/cards/TCS-7440.json) | Polynomial-size split closures in fixed dimension | Optimization and numerics | Optimization and numerical computation/6B |
| [TCS-7441](../../data/cards/TCS-7441.json) | Oertel’s mixed-integer centerpoint conjecture | Optimization and numerics | Optimization and numerical computation/7A |
| [TCS-7442](../../data/cards/TCS-7442.json) | Seymour’s dyadic packing conjecture | Optimization and numerics | Optimization and numerical computation/14A |
| [TCS-7443](../../data/cards/TCS-7443.json) | Flowing conjecture | Optimization and numerics | Optimization and numerical computation/14B |
| [TCS-7444](../../data/cards/TCS-7444.json) | Explicit matroids with exponentially large extended formulations | Optimization and numerics | Optimization and numerical computation/18B |
| [TCS-7445](../../data/cards/TCS-7445.json) | Polynomial-size constant-gap relaxation for minimum knapsack | Optimization and numerics | Optimization and numerical computation/23A |
| [TCS-7446](../../data/cards/TCS-7446.json) | Fully polynomial-size LP relaxation scheme for maximum knapsack | Optimization and numerics | Optimization and numerical computation/23B |
| [TCS-7447](../../data/cards/TCS-7447.json) | Characterizing agnostic online reinforcement learning | Learning theory | Learning theory/4A |
| [TCS-7448](../../data/cards/TCS-7448.json) | Polynomial-time proper learning of Poisson binomial distributions | Learning theory | Learning theory/8B |
| [TCS-7449](../../data/cards/TCS-7449.json) | Longest-example memory for automatic learning | Learning theory | Learning theory/25A |
| [TCS-7450](../../data/cards/TCS-7450.json) | Automatic iterative learning versus hypothesis-sized memory | Learning theory | Learning theory/25B |
| [TCS-7451](../../data/cards/TCS-7451.json) | Witness encryption from plain LWE | Cryptography | Cryptography/4B |
| [TCS-7452](../../data/cards/TCS-7452.json) | Dual pseudorandom functions from arbitrary one-way functions | Cryptography | Cryptography/5A |
| [TCS-7453](../../data/cards/TCS-7453.json) | General functional encryption from plain LWE | Cryptography | Cryptography/6B |
| [TCS-7454](../../data/cards/TCS-7454.json) | Efficient split-state non-malleable codes approaching capacity | Cryptography | Cryptography/8A |
| [TCS-7455](../../data/cards/TCS-7455.json) | Verifiable random functions from one-way functions alone | Cryptography | Cryptography/8B |
| [TCS-7456](../../data/cards/TCS-7456.json) | Compact general-circuit homomorphic secret sharing from DDH | Cryptography | Cryptography/9A |
| [TCS-7457](../../data/cards/TCS-7457.json) | Constant-round concurrent zero knowledge from LWE alone | Cryptography | Cryptography/12A |
| [TCS-7458](../../data/cards/TCS-7458.json) | Succinct noninteractive arguments for NP from LWE alone | Cryptography | Cryptography/16B |
| [TCS-7459](../../data/cards/TCS-7459.json) | Doubly efficient PIR with quasilinear server preprocessing | Cryptography | Cryptography/21B |
| [TCS-7460](../../data/cards/TCS-7460.json) | Blind signatures from one-way functions alone | Cryptography | Cryptography/25B |
| [TCS-7461](../../data/cards/TCS-7461.json) | Rigidity of the computably enumerable degrees | Computability and algorithmic information | Computability and algorithmic information theory/1A |
| [TCS-7462](../../data/cards/TCS-7462.json) | Deciding the two-quantifier theory of c.e. degrees | Computability and algorithmic information | Computability and algorithmic information theory/1B |
| [TCS-7463](../../data/cards/TCS-7463.json) | Low-\(n\) Boolean algebra conjecture | Computability and algorithmic information | Computability and algorithmic information theory/2A |
| [TCS-7464](../../data/cards/TCS-7464.json) | Low-two supersets lattice conjecture | Computability and algorithmic information | Computability and algorithmic information theory/5B |
| [TCS-7465](../../data/cards/TCS-7465.json) | Biinterpretability of computably enumerable degrees with arithmetic | Computability and algorithmic information | Computability and algorithmic information theory/11B |
| [TCS-7466](../../data/cards/TCS-7466.json) | Deciding finite-lattice embeddability into c.e. degrees | Computability and algorithmic information | Computability and algorithmic information theory/15A |
| [TCS-7467](../../data/cards/TCS-7467.json) | Two-quantifier theory of the local enumeration degrees | Computability and algorithmic information | Computability and algorithmic information theory/15B |
| [TCS-7468](../../data/cards/TCS-7468.json) | Classifying sets with countable infinite-time decision complexity | Computability and algorithmic information | Computability and algorithmic information theory/21A |
| [TCS-7469](../../data/cards/TCS-7469.json) | Admissibility of gaps in infinite-time decision times | Computability and algorithmic information | Computability and algorithmic information theory/21B |
| [TCS-7470](../../data/cards/TCS-7470.json) | Universality of recursive isomorphism on binary sequences | Computability and algorithmic information | Computability and algorithmic information theory/26B |
| [TCS-7471](../../data/cards/TCS-7471.json) | Topological computable categoricity of infinite Polish spaces | Computability and algorithmic information | Computability and algorithmic information theory/27A |
| [TCS-7472](../../data/cards/TCS-7472.json) | Degree of topological categoricity of Baire space | Computability and algorithmic information | Computability and algorithmic information theory/27B |
| [TCS-7473](../../data/cards/TCS-7473.json) | Optimal competitive ratio of online bin packing | Online algorithms | Online algorithms, scheduling and packing/1A |
| [TCS-7474](../../data/cards/TCS-7474.json) | Optimal stretch for online bin stretching | Online algorithms | Online algorithms, scheduling and packing/5A |
| [TCS-7475](../../data/cards/TCS-7475.json) | Optimal deterministic price of obligatory testing | Online algorithms | Online algorithms, scheduling and packing/6A |
| [TCS-7476](../../data/cards/TCS-7476.json) | Power of randomization in scheduling with obligatory tests | Online algorithms | Online algorithms, scheduling and packing/6B |
| [TCS-7477](../../data/cards/TCS-7477.json) | Three-competitive deterministic file migration | Online algorithms | Online algorithms, scheduling and packing/9A |
| [TCS-7478](../../data/cards/TCS-7478.json) | Polynomial-time constant approximation for the General Scheduling Problem | Online algorithms | Online algorithms, scheduling and packing/12A |
| [TCS-7479](../../data/cards/TCS-7479.json) | Optimal prophet-secretary constant | Online algorithms | Online algorithms, scheduling and packing/14B |
| [TCS-7480](../../data/cards/TCS-7480.json) | Stationary-start cover-time lower bound | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/1B |
| [TCS-7481](../../data/cards/TCS-7481.json) | Polynomial mixing at the four-state Potts critical point | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/5A |
| [TCS-7482](../../data/cards/TCS-7482.json) | Critical Swendsen–Wang spectral-gap exponent | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/5B |
| [TCS-7483](../../data/cards/TCS-7483.json) | Cluster sampling of graph colorings with \(\Delta+1\) colors | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/7A |
| [TCS-7484](../../data/cards/TCS-7484.json) | Rapid cluster sampling of three-colourings on the square torus | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/7B |
| [TCS-7485](../../data/cards/TCS-7485.json) | Hard-core phase transition on the square lattice | Randomized algorithms and sampling | Sampling, Markov chains and mixing times/11A |
| [TCS-7486](../../data/cards/TCS-7486.json) | Ranking and unranking a spanning-tree Gray code | Counting and enumeration | Counting and enumeration/1A |
| [TCS-7487](../../data/cards/TCS-7487.json) | Pivot-exchange Gray codes for spanning trees | Counting and enumeration | Counting and enumeration/2A |
| [TCS-7488](../../data/cards/TCS-7488.json) | Edge-exchange Gray codes for directed spanning trees | Counting and enumeration | Counting and enumeration/2B |
| [TCS-7489](../../data/cards/TCS-7489.json) | Polynomial-delay disjointness Gray codes for combinations | Counting and enumeration | Counting and enumeration/3A |
| [TCS-7490](../../data/cards/TCS-7490.json) | Rank error of MultiQueues under unrestricted insertion orders | Data structures | Data structures/1A |
| [TCS-7491](../../data/cards/TCS-7491.json) | Fast insertion arbitrarily close to bucketized-cuckoo thresholds | Data structures | Data structures/1B |
| [TCS-7492](../../data/cards/TCS-7492.json) | Polylogarithmic updates for bounded rank-width | Dynamic graph algorithms | Data structures/2A |
| [TCS-7493](../../data/cards/TCS-7493.json) | Splay traversal conjecture | Data structures | Data structures/9B |
| [TCS-7494](../../data/cards/TCS-7494.json) | Worst-case dynamic Courcelle theorem at bounded treewidth | Dynamic graph algorithms | Data structures/10A |
| [TCS-7495](../../data/cards/TCS-7495.json) | Worst-case polylogarithmic fully dynamic planarity testing | Dynamic graph algorithms | Data structures/11A |
| [TCS-7496](../../data/cards/TCS-7496.json) | Polylogarithmic updates for the exact arboricity value | Dynamic graph algorithms | Data structures/13A |
| [TCS-7497](../../data/cards/TCS-7497.json) | Sorting-bound external-memory breadth-first search | Data structures | Data structures/18A |
| [TCS-7498](../../data/cards/TCS-7498.json) | Sorting-bound external-memory weighted shortest paths | Data structures | Data structures/18B |
| [TCS-7499](../../data/cards/TCS-7499.json) | Faster approximate dynamic distances on monotone grids | Dynamic graph algorithms | Data structures/22B |
| [TCS-7500](../../data/cards/TCS-7500.json) | Fully dynamic linear programming with outliers | Dynamic graph algorithms | Data structures/24A |
| [TCS-7501](../../data/cards/TCS-7501.json) | Fast dynamic vertex colouring against adaptive updates | Dynamic graph algorithms | Data structures/25B |
| [TCS-7502](../../data/cards/TCS-7502.json) | Optimal-query fully dynamic text indexing | Dynamic graph algorithms | Data structures/26A |
| [TCS-7503](../../data/cards/TCS-7503.json) | Logarithmic dynamic convex-hull line intersection queries | Dynamic graph algorithms | Data structures/27B |
| [TCS-7504](../../data/cards/TCS-7504.json) | Optimal truthful pricing from one sample | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/9B |
| [TCS-7505](../../data/cards/TCS-7505.json) | Constant-factor welfare from posted item prices | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/11A |
| [TCS-7506](../../data/cards/TCS-7506.json) | Optimal randomized truthful two-facility location | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/13A |
| [TCS-7507](../../data/cards/TCS-7507.json) | Constant-factor truthful subadditive combinatorial auctions | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/15A |
| [TCS-7508](../../data/cards/TCS-7508.json) | Constant price of stability for undirected network design | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/17A |
| [TCS-7509](../../data/cards/TCS-7509.json) | Sharp selfishness threshold for manipulation-resistant tournaments | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/18A |
| [TCS-7510](../../data/cards/TCS-7510.json) | Black-box conversion to dominant-strategy truthfulness without expected-welfare loss | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/20A |
| [TCS-7511](../../data/cards/TCS-7511.json) | Optimal truthful approximation for multi-hospital kidney exchange | Algorithmic game theory, mechanism design and fair division | Game theory, social choice and fair division/21A |
