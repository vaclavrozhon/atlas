"""Hand-written, source-grounded reading notes. Page numbers are PDF pages (1-based)."""
NOTES = {}

def note(key, reason, coverage, rows, caution=''):
    NOTES[key] = dict(selection_reason=reason, coverage=coverage, caution=caution,
        problems=[dict(pdf_page=p, locator=loc, kind=kind, summary=summary)
                  for p,loc,kind,summary in rows])

note('raoyehudayoff', 'A foundational communication-complexity text linking protocols, rank and circuits.',
     'Explicit questions in the downloaded early draft; the draft is only 120 pages.', [
 (16,'Introduction, multiparty disjointness','question','Determine tight randomized communication bounds for number-on-forehead set disjointness.'),
 (21,'Open Problem 1.12','question','Determine the optimal gap between deterministic communication and logarithmic monochromatic partition size.'),
 (37,'Conjecture 2.12','conjecture','Is deterministic communication bounded by a fixed power of the logarithm of real matrix rank?'),
 (99,'Open Problem 8.3','question','Can every polynomial-size Boolean circuit be replaced by a polynomial-size, logarithmic-depth circuit?')
 ], 'Problem 2.19 requests a more direct proof of an established lemma; it is an expository request, not an unresolved theorem. Publication year 2020 does not date this early draft.')

note('dwork_roth','A central reference for the mathematical foundations of differential privacy.',
     'The three explicit research discussions located in the text; these include broad modeling directions.',[
 (27,'§2.3.2','research_direction','Which robustness and composition properties characterize differential privacy, and which can be weakened?'),
 (191,'§9.3','question','Can computational privacy improve achievable utility in the trusted-curator model?'),
 (214,'§10.3.2','research_direction','Find satisfactory models for purchasing private data that avoid the stated participation impossibility.')
 ])

note('watrous','A comprehensive mathematical textbook on quantum states, entanglement and channel capacities.',
     'Explicit unresolved observations located in the textbook, rather than a dedicated problem list.',[
 (133,'§3.1, introduction','research_direction','Find useful closed-form optimal discrimination probabilities for ensembles of three or more states.'),
 (547,'§8.5, discussion of non-additivity','question','Construct explicit quantum channels witnessing non-additivity of Holevo information; existence is established nonconstructively.')
 ],'The book already disproves minimum-output-entropy additivity. It is not listed as open. A generic closed-form request is a research direction, not a precise benchmark question.')

note('understanding_ml','A standard introduction to PAC learning, generalization and learning algorithms.',
     'Explicit unresolved learning questions; routine exercises and unknown input parameters were excluded.',[
 (150,'§11.2.4','research_direction','Characterize when cross-validation reliably estimates generalization error beyond the established special cases.'),
 (408,'Conjecture 29.10','conjecture','Does realizable multiclass sample complexity depend on Natarajan dimension without a label-count factor?'),
 (414,'§30.1','question','Does every finite-VC-dimension class admit a finite-size sample-compression scheme?')
 ],'These are statements of the 2014 text, including historically open questions. Later resolution is not audited here.')

note('bandit_algorithms','A substantial reference on stochastic, adversarial, linear and Bayesian bandits.',
     'Selected explicit questions from the chapter notes; related linear-bandit questions are grouped.',[
 (220,'§16.5, bibliographic discussion','research_direction','Obtain asymptotically optimal policies for broader nonparametric reward classes, including bounded-kurtosis distributions.'),
 (259,'Chapter 19 notes; also p.311','question','Design practical linear-bandit algorithms that are both asymptotically optimal and nearly minimax optimal.'),
 (271,'§20.2, notes','research_direction','Make sequential-design confidence bounds adapt to dependence in the design.'),
 (304,'§24.4–24.5','research_direction','Determine optimal regret under linear-model misspecification and for different action-set geometries.'),
 (369,'Chapter 30, convex bandits','question','Determine optimal dimension dependence for convex-bandit regret and computationally practical algorithms.'),
 (424,'§33.4, notes 7–9','research_direction','Match finite-time best-arm identification lower bounds and characterize instance-dependent simple regret.')
 ])

note('coding_theory','An extensive open author textbook on codes, bounds and decoding.',
     'The explicit numbered question found in the currently released draft chapters.',[
 (181,'Open Question 8.2.14','question','Can general Reed–Solomon codes of rate R be efficiently list-decoded beyond an error fraction of 1−√R?')
 ],'The PDF is a partial draft and contains dangling references. The unresolved construction reference on p.148 is not reconstructed into a new problem.')

note('peikert','A foundational account of SIS/LWE hardness and modern lattice cryptography.',
     'All twelve numbered questions in Chapter 7, grouped exactly as in the source.',[
 (76,'Question 1','question','Classically obtain the full worst-case LWE hardness guarantees of the quantum reduction.'),
 (76,'Question 2','question','Prove LWR and LWE-based PRF hardness with polynomial modulus and unbounded samples.'),
 (76,'Question 3','question','Do ideal-lattice algorithms outperform general-lattice algorithms, including attacks on ring-SIS/LWE?'),
 (77,'Question 4','question','Give a meaningful classical worst-case reduction for ring-LWE.'),
 (77,'Question 5','question','Prove decisional ring-LWE hardness in fields with few automorphisms.'),
 (77,'Question 6','question','Prove ring-LWE hardness with narrow spherical error independent of sample count.'),
 (77,'Question 7','question','Obtain sample-preserving search-to-decision equivalence for ring-LWE.'),
 (77,'Question 8','question','Give worst-case or search-to-decision reductions for NTRU-like problems.'),
 (78,'Question 9','question','Achieve efficient, adaptively secure lattice IBE/ABE/predicate encryption in the standard model.'),
 (78,'Question 10','question','Obtain unbounded FHE without bootstrapping, or with substantially lighter bootstrapping.'),
 (78,'Question 11','question','Base unbounded FHE solely on worst-case complexity assumptions.'),
 (78,'Question 12','question','Obtain unbounded ABE, predicate encryption and homomorphic signatures; can they be bootstrapped?')
 ])

note('local_algorithms','A systematic reference on constant-round distributed algorithms and their limitations.',
     'All four questions in §10.',[
 (37,'Problem 1','question','Give coefficient-independent local approximation schemes for packing or covering LPs on bounded-degree graphs.'),
 (37,'Problem 2','research_direction','Find natural combinatorial packing problems admitting nontrivial deterministic local approximation.'),
 (37,'Problem 3','question','Separate constant-time algorithms using identifier values from order-invariant algorithms, without consecutive-ID promises.'),
 (37,'Problem 4','research_direction','Determine the dependence of local running time on maximum degree, closing polynomial versus polylogarithmic gaps.')
 ])

note('repetitive_strings','A major synthesis of compressed indexing for repetitive texts and genomic collections.',
     'Explicit theoretical gaps plus the two principal challenges in §8.',[
 (20,'§3, BWT runs','question','Support fast random access to a string using O(r) words, where r counts BWT runs.'),
 (31,'§4.1','question','Can run-length grammars be balanced with the guarantees available for ordinary grammars?'),
 (57,'§7, alignment-based indexes','conjecture','Extend the cited alignment-based representation to support most suffix-tree operations.'),
 (57,'§8.1','research_direction','Turn the surveyed theoretical compressed indexes into competitive practical implementations.'),
 (58,'§8.2, continues pp.59–60','research_direction','Build indexes for very large repetitive collections using resources proportional to compressed size.')
 ],'The broad implementation challenges have no single fixed mathematical resolution criterion. The BWT conjecture mentioned in the bibliography is already identified there as resolved.')

note('quantum_algorithms','A widely used overview of quantum algorithmic techniques and applications.',
     'The outlook identifies broad research directions, rather than a numbered conjecture list.',[
 (12,'§9, Outlook','research_direction','Find exploitable structure yielding quantum speedups for further practically relevant problems.'),
 (12,'§9, Outlook','research_direction','Develop genuinely new quantum algorithmic techniques beyond the recurring primitives in known algorithms.')
 ],'These are source-level research directions; they should not be mistaken for precisely specified open propositions.')

note('temporal2015','An early systematic algorithmic introduction to graphs with time-dependent edges.',
     'The explicit open question located in the survey.',[
 (21,'§4, temporality; continues on p.22','research_direction','Which structural features besides large edge-kernels force many temporal labels per edge when preserving all paths?')
 ],'Preserving all paths differs from preserving reachability. The following page already proves a two-label reachability guarantee.')

note('bubeck_convex','A foundational synthesis of oracle complexity and convex-optimization methods.',
     'Full-text marker scan and introductory/concluding material reviewed.',[],
     'No explicit unresolved mathematical question was identified in this edition. Unknown oracle inputs and a bibliography title containing “open questions” are not open-problem statements. Retained as a foundational reference, not evidence of an empty research field.')

note('online_convex','A core text on regret minimization and online convex optimization.',
     'Full-text marker scan and chapter discussions reviewed in the 2023 second edition.',[],
     'No explicit unresolved mathematical question was identified. Unknown future losses and exercises asking for algorithms are not automatically research problems. Retained as background; this finding is not a claim that online optimization has no open questions.')

note('markov_mixing','A standard textbook connecting Markov-chain theory with randomized algorithms.',
     'Questions 1–9 in Chapter 26, plus two explicitly remaining parts of the historical-update section.',[
 (375,'Question 1','question','Prove polynomial mixing for grid Ising Glauber dynamics with all-plus boundaries at every temperature.'),
 (375,'Question 2','question','Establish the proposed monotonicity of Ising spectral gaps in temperature and interaction strengths.'),
 (375,'Question 3, continues p.376','question','Compare systematic and random Glauber updates with the stated constant and logarithmic losses.'),
 (376,'Question 4','question','On transitive graphs, is Ising relaxation Θ(n) equivalent to mixing Θ(n log n)?'),
 (376,'Question 5','question','Do bounded-degree transitive expanders necessarily exhibit cutoff?'),
 (376,'Question 6(a–c)','question','Establish cutoff for the three listed cyclic/random transposition and insertion shuffles.'),
 (376,'Question 7','question','Does coloring Glauber dynamics mix in O(n log n) for q>Δ+2?'),
 (377,'Question 8','question','Is lazy transitive-graph mixing bounded by a universal constant times degree times squared diameter?'),
 (377,'Question 9','question','Determine the mixing-time exponent for random row additions on GL_n(F₂).'),
 (377,'§26.4, former Question 4','question','Compare bounded-block and single-site mixing for other spin systems, including Potts.'),
 (378,'§26.4, former Question 14','question','Prove cutoff for the upper-triangular Gaussian-elimination chain.')
 ],'Questions explicitly marked solved in §26.4 are excluded. Current status after this edition is not checked.')

note('vadhan2012','A central monograph connecting derandomization, expanders, extractors and coding.',
     'Selected major numbered questions throughout the monograph; related derandomization questions are grouped.',[
 (22,'Open Problems 2.10, 2.14, 2.17; pp.22–24','question','Which of P, ZPP, RP and BPP coincide?'),
 (34,'Open Problem 2.36','question','Deterministically approximate the number of satisfying assignments of a DNF in polynomial time.'),
 (38,'Open Problem 2.47','question','Do RL and BPL collapse to deterministic logarithmic space?'),
 (57,'Open Problem 3.7','question','Explicitly construct isolation weights for perfect matching, ideally in deterministic NC.'),
 (104,'Open Problem 4.24','question','Construct averaging samplers simultaneously optimizing randomness and sample complexity.'),
 (119,'Open Problems 4.42–4.44','question','Obtain the stated optimal combinatorial spectral and vertex-expander constructions.'),
 (124,'Open Problem 4.48','question','Construct polynomial-length universal traversal sequences for arbitrarily labeled undirected graphs.'),
 (140,'Open Problem 5.9','question','Determine the optimal asymptotic rate–distance tradeoff for binary codes.'),
 (146,'Open Problem 5.20','question','Can Reed–Solomon codes admit polynomial lists beyond the stated square-root decoding barrier?'),
 (162,'Open Problem 5.36; reformulated as 6.35','question','Construct highly unbalanced near-lossless expanders with polylogarithmic degree and nearly optimal right-side size.')
 ])

note('odonnell2021','A foundational textbook on Fourier methods for Boolean functions and their TCS applications.',
     'Selected substantive unresolved questions in the corrected 2021 edition.',[
 (96,'§4.1, Mansour’s conjecture','conjecture','Is the Fourier spectrum of a small DNF concentrated on a correspondingly small set?'),
 (115,'Conjecture 5.3','conjecture','Does every linear threshold function have degree-at-most-one Fourier weight at least 2/π?'),
 (156,'§6.4','question','Can growing-size juntas be learned from uniformly random examples in polynomial time?'),
 (163,'§6.5, after Viola’s theorem','question','Improve the error dependence when sums of independent small-bias distributions fool low-degree polynomials.'),
 (231,'§8.4, Example 8.64','question','Determine the asymptotic randomized decision-tree complexity of recursive majority-of-three.'),
 (246,'§8.7, Aaronson–Ambainis conjecture','conjecture','Must a bounded low-degree polynomial have an influence polynomially large in variance divided by degree?'),
 (270,'§9.6','question','Must some squared Fourier coefficient be at least exp(−O(total influence))?'),
 (305,'§10.4, Friedgut’s conjecture','conjecture','Approximate biased-measure monotone functions of bounded influence by bounded-width monotone DNFs.')
 ],'The edition explicitly gives a counterexample to Majority Is Least Stable; that formulation is excluded.')

note('jukna2012','A major reference for Boolean circuit lower-bound methods.',
     'Selected research problems from an early draft with more than forty marked problems.',[
 (51,'Research Problem 1.33; also 11.17','question','Prove polynomial CNF-complexity lower bounds from average degree for bipartite K₂,₂-free graphs.'),
 (110,'Research Problem 4.15','question','Exhibit graphs with superlogarithmic nondeterministic clique-versus-independent-set communication complexity.'),
 (183,'Research Problem 6.24','question','Is formula size polynomially bounded by the stated monochromatic partition measure?'),
 (236,'Research Problem 8.7','question','Separate polynomial-size monotone circuits from superpolynomial monotone span-program size.'),
 (239,'Research Problem 8.12','question','Separate ordinary and monotone span-program size for monotone functions.'),
 (283,'Research Problem 9.39','question','Strengthen monotone perfect-matching circuit lower bounds to stretched exponential.'),
 (306,'Research Problems 11.2 and 11.15','question','Strengthen explicit depth-three Boolean circuit lower bounds beyond the stated barriers.'),
 (334,'Research Problem 11.40','question','Prove exponential lower bounds for unrestricted depth-two threshold circuits.'),
 (359,'Research Problem 12.28','question','Prove or refute that Majority lies outside ACC⁰.'),
 (461,'Research Problem 16.12','question','Prove exponential lower bounds for weakly read-once nondeterministic branching programs.')
 ],'The draft contains unresolved cross-references and repeated problem numbering; PDF pages disambiguate the entries.')

note('williamson2011','A standard advanced textbook covering the principal approximation-algorithm paradigms.',
     'All eleven entries, numbered 0–10, in Chapter 17. Statements are historical to this edition.',[
 (447,'Problem 0','conjecture','Resolve the Unique Games Conjecture.'),
 (447,'Problem 1; continues p.448','question','Improve metric TSP approximation; specifically seek a 4/3 guarantee through the subtour LP.'),
 (448,'Problem 2','question','Give a constant-factor approximation for asymmetric metric TSP.'),
 (448,'Problem 3; continues p.449','question','Pack using OPT+1 bins; a constant additive error is a highlighted intermediate goal.'),
 (449,'Problem 4','question','Give a primal-dual 2-approximation for general survivable network design.'),
 (449,'Problem 5','question','Obtain a relaxation-based approximation for capacitated facility location.'),
 (449,'Problem 6; continues p.450','question','Beat factor two for generalized Steiner tree, also called Steiner forest.'),
 (450,'Problem 7','question','Beat factor two for makespan scheduling on unrelated machines.'),
 (450,'Problem 8','question','Give a constant approximation for precedence-constrained scheduling on related machines.'),
 (450,'Problem 9','question','Color a promised 3-colorable graph with O(log n) colors in polynomial time.'),
 (450,'Problem 10; continues p.451','question','Match the Goemans–Williamson Max-Cut guarantee with a direct primal-dual algorithm.')
 ])

note('cygan2015','A principal modern textbook on fixed-parameter algorithms and lower bounds.',
     'Selected unresolved algorithmic gaps and central conjectures across the text.',[
 (245,'Chapter 7, branchwidth discussion','question','Determine the complexity of computing treewidth exactly on planar graphs.'),
 (259,'Chapter 7 bibliographic notes','question','Does planar Minimum Bisection admit a polynomial-time algorithm?'),
 (343,'§10.2','question','Compute chromatic number in O*(2ⁿ) time using only polynomial space.'),
 (399,'§12.1.4','question','Construct linear representations of transversal matroids deterministically in polynomial time.'),
 (402,'§12.2','question','Find matroid circuits of size at least k, parameterized by k, for integer representations.'),
 (451,'§13.3','question','Separate levels of the W-hierarchy, including the Independent Set and Dominating Set levels.'),
 (472,'§13.5, Even Set','question','Determine fixed-parameter tractability of finding a small nonempty even set.'),
 (485,'Conjectures 14.1–14.2','conjecture','Resolve the Exponential-Time Hypothesis and its strong version.'),
 (505,'Chapter 14, Subgraph Isomorphism','question','Remove the logarithmic loss from the stated ETH-based exponent lower bound.'),
 (523,'Conjecture 14.36','conjecture','Resolve the Set Cover Conjecture.'),
 (549,'§15.1.2','question','Separate polynomial compression from polynomial kernelization for natural problems.')
 ],'Historical questions are retained as posed; later developments are outside this source inventory.')

note('goldreich2017','A comprehensive foundational text on testing properties with few queries.',
     'The numbered open problems and closely adjacent conjectures; statements are compressed summaries.',[
 (72,'Open Problem 2.4','question','Determine the exact rejection-versus-distance curve of the homomorphism tester.'),
 (101,'Open Problem 4.5','question','Identify path distributions giving the stated near-square-root-dimensional monotonicity-testing guarantee.'),
 (124,'Open Problem 5.8','question','Test monotone k-monomials with one-sided error and dimension-independent query complexity.'),
 (204,'Open Problem 8.9; Conjecture 8.10','question','Improve dense-graph bipartiteness testing below quadratic reciprocal-distance dependence.'),
 (210,'Open Problem 8.17','question','Sharply bound copies of H in graphs far from H-free.'),
 (221,'Open Problem 8.26','question','Characterize dense-graph properties testable with polynomial reciprocal-distance queries.'),
 (223,'Open Problem 8.27','question','Establish nearly quadratic adaptive versus nonadaptive testing gaps.'),
 (266,'Open Problem 9.23','question','Obtain the proposed cleaner local reductions from cycle-freeness to bipartiteness.'),
 (268,'Open Problem 9.26','question','Test minor-closed bounded-degree graph properties with polynomial dependence on degree and proximity.'),
 (366,'Open Problem 12.4','question','Relate ordinary and tolerant testing complexity for natural dense-graph property classes.'),
 (414,'Open Problem 13.12','question','Determine existence of linear-length locally testable codes and proofs.'),
 (423,'§13.4 discussion','question','Separate lengths achievable by locally decodable and relaxed locally decodable codes.')
 ])

note('fair2022','A concentrated survey of the main fairness notions for indivisible goods.',
     'All ten numbered open problems in the downloaded March 2022 version.',[
 (4,'Open Problem 1','question','Compute an EF1 and Pareto-optimal allocation in polynomial time.'),
 (5,'Open Problem 2','question','Do EFX allocations exist for at least four agents with unrestricted additive valuations?'),
 (5,'Open Problem 3','question','Determine the best universally guaranteed multiplicative EFX approximation.'),
 (6,'Open Problem 4','question','Achieve exact EFX while donating only a sublinear number of goods.'),
 (7,'Open Problem 5','question','Improve the stated additive-valuation maximin-share approximation and impossibility bounds.'),
 (7,'Open Problem 6','research_direction','Identify further structured valuation classes guaranteeing exact maximin-share allocations.'),
 (7,'Open Problem 7','question','Does envy-freeness up to a random good always exist?'),
 (8,'Open Problem 8','question','Do pairwise maximin-share allocations always exist?'),
 (8,'Open Problem 9','question','Determine the best universal approximation to groupwise maximin-share fairness.'),
 (9,'Open Problem 10','question','Design mechanisms whose pure Nash equilibria guarantee fairness stronger than EF1.')
 ])

note('reconfig2020','A systematic survey connecting recoloring, domination and reconfiguration graphs.',
     'All eight numbered question groups and two conjectures; multipart questions are grouped.',[
 (5,'Question 3.1','question','For fixed r,k, do k-mixing P_r-free graphs have recoloring diameter O(n)?'),
 (6,'Conjecture 3.1','conjecture','Is k-coloring reconfiguration diameter O(n³) whenever k exceeds the coloring number?'),
 (6,'Question 3.2','question','Resolve the stated Hamiltonicity, connectivity and color-increase questions for coloring graphs.'),
 (9,'Question 3.3','question','Is circular mixing rational, and is its ratio to the ordinary mixing parameter bounded?'),
 (13,'Question 4.1','question','Characterize domination-reconfiguration thresholds, Hamiltonicity and how diameters change with allowed set size.'),
 (13,'Question 4.2','question','Which induced hypercube subgraphs occur as domination reconfiguration graphs?'),
 (14,'Question 4.3','research_direction','Understand total-domination reconfiguration: large threshold gaps, realizable graphs and fixed points.'),
 (15,'Question 4.4','question','Characterize γ-graphs of trees; can every bipartite graph arise from bipartite domination reconfiguration?'),
 (16,'Conjecture 4.1','conjecture','Exclude paths P_n, n≥3, and cycles C_n, n≥5, from IR-graphs.'),
 (16,'Question 4.5','question','Are complete graphs and C₄ the only claw-free IR-graphs?')
 ],'Some questions concern structural graph theory beyond the atlas selection scope. This independent library preserves the source’s scope.')

note('scheduling2017','A focused survey organizing central parameterized machine-scheduling questions.',
     'All fifteen numbered problems. Scheduling notation and parameter conventions are defined in the PDF.',[
 (4,'Open Problem 1','question','Single-machine weighted tardiness: FPT in maximum processing time?'),
 (4,'Open Problem 2','question','Precedence-constrained weighted completion: polynomial kernel in the excess over the LP bound?'),
 (4,'Open Problem 3','question','Release-date late-job objectives: W[1]-hard in maximum processing time?'),
 (4,'Open Problem 4','question','Single-machine makespan: FPT in forbidden start/end times?'),
 (5,'Open Problem 5','question','High-multiplicity identical-machine makespan: FPT in distinct processing times?'),
 (5,'Open Problem 6','question','Three-machine unit-job precedence scheduling: FPT in partial-order width?'),
 (5,'Open Problem 7','question','Equal-length, release-date late-job objectives: FPT in machine count?'),
 (6,'Open Problem 8','question','Eligible-machine, just-in-time weighted scheduling: FPT in machine count?'),
 (6,'Open Problem 9','question','The three preemptive objectives in §4.5: FPT in distinct processing times?'),
 (6,'Open Problem 10','question','Two-machine preemptive equal-length weighted tardiness: W[1]-hard in job length?'),
 (6,'Open Problem 11','question','Three-machine flow-shop makespan: FPT in maximum operation length?'),
 (7,'Open Problem 12','question','Three-machine job-shop makespan: FPT in maximum length and operations per job?'),
 (7,'Open Problem 13','question','Job-shop makespan: approximation scheme running in f(m,ε)poly(n)?'),
 (7,'Open Problem 14','question','Unit-operation open shops with sequence-dependent batch setups: FPT in batch count?'),
 (7,'Open Problem 15','question','Unit-operation open-shop weighted late jobs with release dates: FPT in machine count?')
 ])

note('nordstrom2013','A substantial survey connecting pebbling, SAT solving and proof-space lower bounds.',
     'Selected numbered questions, checked against the author’s updates in §7.',[
 (23,'Open Problem 1','research_direction','Do practical DPLL-based solvers exhibit the time–space tradeoffs predicted by pebbling contradictions?'),
 (25,'Open Problems 2–3','question','Are resolution total-space and clause-space decision problems PSPACE-complete?'),
 (25,'Open Problem 4','question','Find combinatorial characterizations of clause space for resolution and k-DNF resolution.'),
 (30,'Open Problem 6','question','Refute substituted pebbling contradictions using total space proportional to black–white pebbling price.'),
 (31,'Open Problem 7','question','Simulate black–white pebblings by bounded labeled pebblings without asymptotic space loss.'),
 (36,'Open Problem 8','question','Translate resolution refutations back into black–white pebblings with controlled time and space.'),
 (50,'Open Problem 10','question','Exhibit linear-size fixed-width CNFs requiring quadratic total resolution space.'),
 (50,'Open Problem 11','question','Asymptotically separate resolution clause space from polynomial-calculus-resolution space.'),
 (51,'Open Problem 13','question','Does logarithmic resolution clause space imply polynomial proof length?'),
 (51,'Open Problems 14–15','question','Determine unavoidable length–width tradeoffs, including tight fixed-width length lower bounds.'),
 (52,'Open Problem 16','question','Can constant-space refutations always be made simultaneously polynomial-length and constant-space?'),
 (53,'Open Problem 18','question','Preserve pebbling-derived space lower bounds when converting contradictions to 3-CNF.')
 ],'Problems 5 and 17 are resolved by updates inside this same PDF; Problem 12 asks for another proof of a known result. They are excluded.')

note('spanners2020','A broad reference on spanner constructions, extremal bounds and algorithmic variants.',
     'Selected questions from the dedicated open-problem sections; related construction directions are grouped.',[
 (11,'§2.5, item 1','research_direction','Study spanners with discontinuous distortion functions.'),
 (11,'§2.5, item 2','conjecture','Resolve the remaining cases of the Erdős girth conjecture.'),
 (13,'§3.5','question','Classify minimum t-spanner hardness for the eight listed bounded-degree parameter pairs.'),
 (20,'§4.7','research_direction','Develop reverse-greedy and generalized greedy spanner constructions.'),
 (27,'§5.5','research_direction','Turn standard clustering methods into spanners with provable quality.'),
 (29,'§6.2','research_direction','Improve spanner sampling distributions and the Elkin–Neiman construction’s size guarantee.'),
 (33,'§7.5','question','Maximize the pair count admitting linear-size pairwise spanners with constant additive error.'),
 (37,'§8.4, item 1','question','Does every unweighted graph admit a +4 spanner with O(n^(4/3)) edges?'),
 (37,'§8.4, item 2','question','Match Thorup–Zwick emulator tradeoffs using actual spanners.'),
 (37,'§8.4, item 3','question','Determine optimal additive error for linear-size spanners.'),
 (37,'§8.4, item 4','question','Construct O(n^(4/3))-edge weighted spanners with additive error 6W.'),
 (55,'§12.1','question','Close the bounds for fault-tolerant sourcewise distance preservers.')
 ],'The practical polynomial-size pairwise-spanner ILP question is already answered within the survey and is excluded.')

note('cspbook2017','A major edited reference connecting CSP algorithms, universal algebra and approximation.',
     'Selected explicit questions across the contributed chapters; not an exhaustive inventory of this volume.',[
 (176,'Chapter 6, Holant discussion','question','Classify the complexity of Boolean decision-Holant problems.'),
 (213,'Chapter 7, §8','question','Give a deterministic polynomial kernel for Almost 2-SAT.'),
 (213,'Chapter 7, §8','question','Give Max-Lin2 above average a polynomial-size kernel measured in constraints.'),
 (269,'Chapter 9, §7','question','Is bounded-arity submodular VCSP minimization easier than general oracle submodular minimization?'),
 (270,'Chapter 9, §8','research_direction','Sharpen tractability criteria and improve algorithms for valued CSPs.'),
 (271,'Chapter 9, §8','research_direction','Classify Boolean, minimal and fixed-support weighted clones.'),
 (292,'Chapter 10, §7, items 1–5','question','Classify tractable oriented-tree CSPs, linear-Datalog list homomorphisms and the specified digraph polymorphisms.'),
 (333,'Chapter 11, §7, Problem 1','question','Close approximation gaps for Max 2-And, Max SAT and Multiway Cut.'),
 (333,'Chapter 11, §7, Problem 2','question','Determine the leading constant in optimal Boolean k-CSP approximation.'),
 (334,'Chapter 11, §7, Problem 3','question','Determine whether the stated general-domain k-CSP approximation is asymptotically optimal.'),
 (334,'Chapter 11, §7, Problem 4','question','Can minimization-CSP algorithms match their SDP integrality gaps up to 1+ε?')
 ],'Different chapters use independent numbering. Some foundational conjectures in this historical volume have later resolutions; this is not a current-status catalogue.')

note('arora_barak','A standard broad introduction to modern computational complexity.',
     'Selected central questions explicitly discussed in the January 2007 draft.',[
 (57,'§2.1','question','Does P equal NP?'),
 (95,'§4.2','question','Does deterministic logspace suffice for directed reachability, equivalently L=NL?'),
 (105,'Chapter 4 exercises','question','Is directed reachability solvable simultaneously in polynomial time and polylogarithmic space?'),
 (126,'§6.5.2','question','Does NC equal P?'),
 (178,'Chapter 8, prover complexity','question','Can the discussed interactive proofs use weaker provers than their counting-based implementations?'),
 (188,'§9.1','question','Can all #P counting functions be computed in polynomial time?'),
 (202,'§9.4','question','Would P=NP imply polynomial-time exact computation of every #P function?'),
 (243,'Conjecture 12.17','conjecture','Is deterministic communication polynomially bounded by logarithmic real matrix rank?'),
 (299,'§16.1 discussion','question','Construct explicit Boolean functions with strong general circuit lower bounds.'),
 (445,'§20.8','question','Determine the relationships between BQP and classical classes, particularly NP and BPP.')
 ],'The downloaded file is the 2007 author draft, not the final 2009 book; chapter and PDF pagination differ.')

note('expanders','A landmark survey connecting expansion with combinatorics, algorithms and complexity.',
     'Selected numbered questions and conjectures in the 2006 author draft.',[
 (48,'Open Problem 5.1','question','Sharply control sparse k-vertex induced subgraphs in regular graphs, including girth-related extremal bounds.'),
 (53,'Conjecture 5.13','conjecture','Do arbitrarily large d-regular Ramanujan graphs exist for every d≥3?'),
 (57,'Conjectures 6.8–6.10','conjecture','Find two-lifts or adjacency signings with the stated two-sided Ramanujan spectral bounds.'),
 (65,'Conjecture 7.8','conjecture','Are new eigenvalues of typical large lifts bounded by the universal-cover spectral radius plus o(1)?'),
 (66,'Open Problem 7.11','question','Determine the probability that random lifts satisfy exact Ramanujan eigenvalue bounds.'),
 (67,'Open Problem 7.12','question','Describe the coordinate distribution of nontrivial eigenvectors of random regular graphs.'),
 (87,'Open Problem 10.8','question','Explicitly construct regular graphs with vertex expansion approaching d−2 on small sets.'),
 (113,'Open Problem 13.11','question','Approximate the cut cone within constant distortion using a cone with efficient separation.')
 ],'Conjecture 13.12 is explicitly refuted in the source and is excluded. Other entries retain their historical status.')

note('arithmetic_circuits','A foundational survey of arithmetic circuit complexity and polynomial identity testing.',
     'Selected problem families from the 33 numbered questions; model variants remain distinguishable by their source numbers.',[
 (11,'Problem 1','question','Improve determinantal-complexity lower bounds for the permanent.'),
 (19,'Problems 2–4','question','Separate homogeneous, multilinear, syntactically multilinear and unrestricted algebraic models.'),
 (26,'Problem 6','question','Prove superpolynomial depth-four arithmetic circuit lower bounds in characteristic other than two.'),
 (31,'Problems 7–8; also p.32','question','Prove stronger general arithmetic-circuit lower bounds and superpolynomial formula lower bounds.'),
 (35,'Problem 10','question','Prove superpolynomial noncommutative circuit lower bounds.'),
 (38,'Problem 11','question','Prove superpolynomial depth-three circuit lower bounds over infinite fields.'),
 (42,'Problems 13–14; also p.44','question','Strengthen multilinear circuit lower bounds and separate multilinear from unrestricted formulas.'),
 (51,'Problem 15','question','Explicitly construct three-dimensional tensors with superlinear rank.'),
 (56,'Problem 16','question','Develop algebraic pseudorandom functions and an arithmetic natural-proofs analogue.'),
 (67,'Problem 17','question','Does efficient PIT for a circuit class force permanent lower bounds for that class?'),
 (69,'Problems 18–19','question','Derandomize depth-four black-box PIT and preserve bounded depth under factorization.'),
 (70,'Problems 20–21','question','Convert multilinear lower bounds into PIT, including deterministic subexponential testing for formulas.'),
 (75,'Problems 22–24; also p.76','question','Derandomize noncommutative PIT and establish analogous hardness-to-randomness implications.')
 ],'Historical depth-restricted problems are retained as posed, without asserting that they remain open today.')

note('fine_grained','An influential overview of conditional lower bounds inside polynomial time.',
     'Core hardness hypotheses and explicit remaining connections highlighted by the survey.',[
 (1,'Abstract and §§2–4','conjecture','Resolve the SETH, 3-SUM and APSP hypotheses underlying the survey’s conditional lower bounds.'),
 (14,'§4, tree edit distance','question','Is tree edit distance fine-grained equivalent to APSP?'),
 (16,'§5, Hitting Set','question','Does the Orthogonal Vectors hypothesis imply the Hitting Set hypothesis?'),
 (16,'§5, k-Clique','conjecture','Are the stated matrix-multiplication-based k-clique exponents optimal?'),
 (20,'§7, fine-grained cryptography','research_direction','Construct further cryptographic primitives, including one-way functions, from fine-grained assumptions.'),
 (20,'§7, time–space tradeoffs','research_direction','Prove strong unconditional lower bounds for suitably space-restricted 3-SUM algorithms.')
 ])

note('wigderson','A broad synthesis of complexity theory and its connections with mathematics.',
     'Selected major numbered questions from the 2019 final author draft.',[
 (38,'Open Problem 3.5','question','Does P equal NP?'),
 (43,'Conjecture 3.8','conjecture','Does NP differ from coNP?'),
 (45,'Conjecture 3.9','conjecture','Are there problems in NP∩coNP outside P?'),
 (58,'Conjecture 4.4','conjecture','Resolve the Unique Games Conjecture.'),
 (60,'Open Problem 4.6','question','Does worst-case NP hardness imply distributional average-case hardness?'),
 (63,'Open Problem 4.10','question','Do worst-case or average-case hardness assumptions imply one-way functions, or trapdoor functions?'),
 (66,'Conjecture 5.4','conjecture','Is NP outside polynomial-size Boolean circuits?'),
 (71,'Open Problem 5.19','question','Does majority admit monotone formulas of cubic size?'),
 (82,'Open Problem 6.10','question','Prove superpolynomial Frege proof-length lower bounds.'),
 (84,'Open Problem 6.12','question','Would NP circuit lower bounds imply superpolynomial Frege lower bounds?'),
 (88,'Open Problem 7.6','question','Does BPP equal P?')
 ])

note('algorithmic_game_theory','A foundational edited textbook spanning mechanisms, equilibria and network games.',
     'Selected explicit questions from Chapters 12 and 19; other chapters also contain open discussions.',[
 (331,'§12.2','question','Does truthful makespan scheduling on related machines admit a PTAS?'),
 (337,'§12.3','question','Obtain truthful constant-factor combinatorial-auction approximations, including submodular valuations.'),
 (338,'§12.3','research_direction','Determine approximation limitations of deterministic dominant-strategy truthful auctions.'),
 (341,'§12.4','question','Characterize domains where affine maximizers are the only implementable allocation rules.'),
 (348,'§12.5','question','Can efficient algorithmic implementation approximate better than every efficient dominant-strategy implementation?'),
 (529,'§19.2, Open Problems','question','Bound the local connection game’s price of anarchy by a constant for all edge-cost parameters.'),
 (529,'§19.2, Open Problems','research_direction','Extend network-formation efficiency bounds to heterogeneous costs, traffic and approximate equilibria.'),
 (531,'§19.3, Open Problems','research_direction','Determine tight equilibrium-efficiency bounds for undirected global connection and generalized cost-sharing games.'),
 (532,'§19.4, Open Problems','research_direction','Identify further pricing games with efficient equilibria and guarantees after limited play.')
 ],'These questions are historical to the 2007 volume. Multipart research directions remain grouped rather than becoming artificial separate problems.')
