"""Second reading pass: specialist area sources, without matching catalogue problems."""
from reviewed import NOTES,note
SCOPE='Whole-document pass for explicit unresolved questions, conjectures and research directions, including topics outside the selection category. Numbered lists and unnumbered statements are both included; related variants may share an entry.'

def area_note(key,reason,rows,caution='',scope=SCOPE):
 note(key,reason,scope,rows,caution)
 NOTES[key]['review_pass']='area-expansion-2026-09-10'
 NOTES[key]['inventory_target']='all_explicit_unresolved_statements_in_downloaded_work'
 NOTES[key]['inventory_is_exhaustive_for_entire_work']=False

area_note('geometry_cabello','An invited specialist overview connecting geometric algorithms, parameterization and stochastic input.',[
(3,'§2, stochastic bounding box','question','Is expected bounding-box volume FPT in dimension, or is its decision version W[1]-hard?'),
(3,'§2, approximation','research_direction','Find approximation schemes for expected bounding-box volume with mild dimension dependence.'),
(3,'§3, uncolored intersections','question','Compute maximum matchings of unit-disk or unit-square intersection graphs in near-linear time.'),
(4,'§3, bichromatic intersections','question','Obtain near-linear maximum matching for bichromatic unit disks or squares.'),
(4,'§3, recognition variant','question','Can the corresponding matching-existence test be faster than constructing the matching?'),
(5,'§4, annular domain','question','Determine the complexity of barrier resilience for disks, including unit disks, in an annulus.'),
(5,'§4, shrinking; Figure 4','question','Is minimum total barrier shrinkage polynomial-time solvable or NP-hard in a rectangle?')
],'The §3 phrase “has a maximum matching” is ambiguous (every finite graph has one); the inventory records the intended existence-testing direction without silently replacing it by a precise perfect-matching claim. The source proves unbounded-dimension #P-hardness, so that is excluded.')

area_note('compact_databases','A data-structure survey on compressed representations and worst-case-optimal database joins.',[
(13,'§6, higher dimensions','research_direction','Scale compact join structures to many attributes, including hybrid worst-case-optimal and conventional query plans.'),
(13,'§6, functionality','research_direction','Efficiently combine graph patterns, regular paths, ranking, similarity joins and spatiotemporal predicates; define suitable optimality guarantees.'),
(13,'§6, real systems','research_direction','Integrate compact structures into complete SPARQL-capable graph database engines.'),
(14,'§6, analytics','research_direction','Support exact or approximate result counting without enumeration, and extend compact representations to analytical matrices.')
],scope=SCOPE+' All four §6 question families are represented, including their subdirections.')

area_note('query_enumeration','A focused survey of constant-delay query evaluation and the effect of logical and structural restrictions.',[
(7,'§6, bag semantics','research_direction','Determine enumeration complexity under bag semantics, retaining multiplicities of witnesses and supporting aggregate queries.'),
(7,'§6, unconditional lower bounds','question','Prove unconditional constant-delay enumeration lower bounds for natural queries such as the distance-two query.')
],'§5 describes established effects of output order and known extensions; these observations are not automatically new conjectures.')

area_note('regular_model_checking','A foundational survey of automata-based verification of infinite-state and parameterized systems.',[],
'No explicit unresolved research question was identified. The “Further Directions” section reports already-developed extensions; generic undecidability and reachability problem definitions are not open problems. Loop Termination provides the question-bearing specialist source for the verification category.')

area_note('pnp_fortnow','A specialist survey of P versus NP, barriers, average-case hardness, proofs and quantum computation.',[
(2,'§2','question','Does P equal NP?'),
(3,'§4.2','question','Prove superpolynomial general Boolean-circuit lower bounds for an NP-complete problem.'),
(3,'§4.3, general proof systems','question','Can all tautologies have polynomially bounded proofs in some propositional proof system?'),
(3,'§4.3, Frege','question','Prove superpolynomial lower bounds for unrestricted Frege proofs.'),
(3,'§5.1','question','Beat exhaustive assignment search for general formula satisfiability.'),
(4,'§5.4','question','Do NP-complete problems admit suitable worst-case-to-average-case reductions?'),
(4,'§6','conjecture','Resolve the Unique Games Conjecture.'),
(5,'§7.2','question','Can randomized polynomial-time computation be derandomized?'),
(5,'§8','question','Can quantum computers solve NP-complete problems in polynomial time?'),
(6,'§9, step 1','question','Establish the GCT program’s proposed polynomial-time LP/integer-feasibility correspondence.'),
(6,'§9, steps 2–3','research_direction','Find the required combinatorial feasibility algorithm and prove universal feasibility for the GCT polytopes.'),
(6,'§10, SAT','question','Prove that SAT requires more than near-linear time.'),
(6,'§10, time and space','question','Separate a given space bound from roughly the same time bound.'),
(6,'§11, formal independence','question','Could P versus NP be independent of standard mathematical axioms?')
],'The GCT roadmap is the informal historical formulation of this survey; its missing technical hypotheses are not reconstructed. Later developments are not checked.')

area_note('beyond_worst_case','A survey of stable instances, semi-random inputs, smoothed complexity and learning.',[
(8,'§4, planted clique','question','Can polynomial-time algorithms recover planted cliques asymptotically smaller than √n?'),
(9,'§5, sparse perturbations','question','Extend smoothed polynomial-time simplex analysis to perturbations preserving sparsity.'),
(10,'§5, local Max-Cut','conjecture','Does local search reach a Max-Cut local optimum in polynomial smoothed time on every graph?'),
(10,'§5, broader local search','research_direction','Establish polynomial smoothed convergence for broader natural local-search problems.'),
(11,'§6, optimization','research_direction','Explain rapid local or global convergence of neural-network optimization using realistic input structure.'),
(11,'§6, generalization','research_direction','Explain why overparameterized networks generalize, accounting for both data and training algorithms.')
],'Motivating questions answered by the survey’s theorems are excluded; general questions about good input models are represented by the concrete unresolved directions.')

area_note('nonabelian_crypto','A survey of noncommutative cryptography, including platform groups, attacks and quantum complexity.',[
(27,'§11 General 1–2','question','Which platform groups, finite or infinite, best support noncommutative cryptography?'),
(27,'§11 General 3,5–6','research_direction','Prove protocol security and choose appropriate practical, worst-case, average-case or generic-case security measures.'),
(27,'§11 General 4','research_direction','Construct public-key systems from further group-theoretic search and decision problems.'),
(27,'§11 General 7–8','research_direction','Design additional noncommutative signatures and authentication schemes.'),
(27,'§11 General 9','question','Which commuting subgroups of polycyclic groups yield secure protocols?'),
(27,'§11 Complexity 1','question','Determine polycyclic conjugacy-search complexity.'),
(27,'§11 Complexity 2','question','Determine polycyclic conjugacy-decision complexity, including the Eick–Ostheimer algorithm.'),
(27,'§11 Complexity 3','question','Determine collection-algorithm complexity for polycyclic normal forms.'),
(28,'§11 Complexity 4','question','Determine twisted conjugacy-search complexity in polycyclic groups.'),
(28,'§11 Complexity 5','question','Determine Reidemeister–Schreier rewriting complexity in free groups.'),
(28,'§11 Complexity 6','question','Determine generic-case polycyclic conjugacy-search complexity.'),
(28,'§11 Quantum, introduction and 1','question','Can quantum algorithms accelerate polycyclic conjugacy search and other cryptographic decision problems?'),
(28,'§11 Implementation 1–2','research_direction','Implement the proposed systems securely and practically, including possible GAP-based implementations.')
],scope=SCOPE+' All 18 numbered §11 items are represented; the quantum introduction is included. Earlier conjugacy-complexity discussions recur in that list.')

area_note('sync_automata','A dedicated survey of synchronization thresholds, decision complexity, random automata and algebraic methods.',[
(2,'Conjecture 1','conjecture','Every synchronizing n-state automaton admits a reset word of length at most (n−1)².'),
(3,'Conjecture 2','conjecture','The state-avoiding threshold is at most 2n−2, under the source’s avoidability convention.'),
(4,'Open Problem 4','question','Find tight avoid-or-compress bounds depending on subset sizes, including strongly connected synchronizing automata.'),
(4,'Conjecture 5','conjecture','Avoid any k<n states of a synchronizing automaton within O(kn) letters.'),
(4,'Conjecture 6','conjecture','Compress any specified state with another within O(n) letters in strongly connected synchronizing automata.'),
(5,'Conjecture 8','conjecture','Verify synchronization and the claimed 4n/3 compression threshold of the explicit A_k family.'),
(6,'Conjecture 9','conjecture','Prove Cardoso’s stated bound for synchronizing a specified subset.'),
(6,'Conjecture 11','conjecture','Some k-state subset synchronizes within O(kn) letters.'),
(6,'Open Problem 12','question','Bound words synchronizing a prescribed subset together with k additional states.'),
(7,'Open Problem 13','question','Beat quadratic-time synchronizability testing over a fixed alphabet, or establish conditional barriers.'),
(8,'Conjecture 16','conjecture','Random binary automata have reset threshold Θ(√n) with high probability.'),
(9,'Conjecture 17','conjecture','Random binary automata have expected reset threshold Θ(√n).'),
(11,'§2.8.2, unnumbered conjecture','conjecture','Is the Eulerian reset-threshold lower bound ⌊(n²−3)/2⌋ tight?'),
(13,'Open Problem 22','question','Determine tight initial-subspace dimension bounds for iterative algebraic synchronization methods.')
],'Numbering interleaves theorems, lemmas and propositions; those are not missing open questions. Random-automaton statements use the source’s convention for nonsynchronizing samples.')

area_note('rank_width','A specialist survey covering both algorithmic and structural questions about rank-width.',[
(3,'§2.3, Boolean-width','question','Can the quadratic rank-width bound on Boolean-width be replaced by a linear bound?'),
(6,'Question 1','question','Compute rank-width of circle graphs in polynomial time.'),
(6,'Question 2','question','Approximate rank-width with parameter-dependent output width in O(c^k n³) time.'),
(6,'Question 3','question','Obtain such an approximation with a subcubic dependence on n.'),
(7,'§3.4, unnumbered','question','Compute linear rank-width by an FPT algorithm parameterized by rank-width.'),
(7,'Question 4','question','Compute rank-width exactly in O(c^n) time for c<2.'),
(9,'§4.3, Geelen conjecture','conjecture','Excluding any fixed vertex-minor defines a χ-bounded graph class.'),
(10,'Question 5','conjecture','Large rank-width forces every fixed bipartite circle graph as a pivot-minor.'),
(10,'§4.5, unnumbered','question','Does sufficiently large linear rank-width force every fixed tree as a vertex-minor?'),
(11,'Question 6','question','Are all graphs well-quasi-ordered by pivot-minors?'),
(11,'Question 7','question','Detect any fixed pivot-minor or vertex-minor in polynomial time.')
],scope=SCOPE+' All seven numbered questions and four unnumbered questions/conjectures are included.')

area_note('algorithmic_randomness','A historical specialist survey connecting computability, randomness and effective dimension.',[
(35,'§4.4, Kolmogorov–Loveland randomness','conjecture','Do Kolmogorov–Loveland random sequences coincide with Martin-Löf random sequences?')
],'The broken-dimension question on p.36 is explicitly answered by Miller and is excluded; introductory conceptual questions are not claimed to be unresolved theorems.')

area_note('loop_termination','A focused verification survey linking linear loops, recurrence sequences and Diophantine approximation.',[
(2,'§1, Skolem Problem; also §4','question','Decide whether an integer linear recurrence ever equals zero, including the unresolved order-five case.'),
(2,'§1, Positivity','question','Decide nonnegativity of every term; unresolved cases include general order six and simple orders above nine.'),
(2,'§1, Ultimate Positivity','question','Decide eventual nonnegativity for arbitrary linear recurrences, already unresolved at order six.'),
(3,'§1, effective threshold','question','Compute eventual-positivity thresholds for simple recurrences beyond the established low-order cases.'),
(3,'§1 and §2, Diophantine barriers','research_direction','Make the relevant transcendental Diophantine-approximation bounds effective enough for recurrence decision procedures.'),
(6,'§3 and §4, integer loops','question','Decide termination over all integer starting states for general affine linear loops with nondiagonalizable updates.'),
(8,'§4, linear constraint loops','question','Decide termination for loops whose updates are general linear constraints between successive states.')
],'The nonnegativity convention is the formal one in the paper. Infinite occurrence of zero, real/rational universal termination and ultimate positivity of simple recurrences are already decidable here.')

area_note('numerical_sketching','A monographic survey of randomized numerical linear algebra, regression and low-rank approximation.',[
(20,'§2, sparse embedding conjecture','conjecture','Achieve optimal subspace-embedding dimension with the conjectured input-sparsity running time and failure dependence.'),
(127,'Open Question 1','question','Obtain relative spectral low-rank approximation in O(nnz(A))+n·poly(k/ε) time.'),
(127,'Open Question 2','question','Obtain polynomial-time relative low-rank approximation in entrywise ℓ₁ error.'),
(128,'Open Question 3','question','Prove an Ω(sdk/ε) communication bound for arbitrary-partition distributed low-rank approximation.'),
(129,'Open Question 4','question','Determine optimal linear-sketch dimension for constant-factor approximation of the nuclear norm.')
],scope=SCOPE+' All four concluding questions plus the earlier sparse-embedding conjecture are included.')

area_note('dynamic_graphs','An invited survey covering fully dynamic graph theory, implementations and evaluation methodology.',[
(1,'Abstract and introduction','research_direction','Engineer and evaluate dynamic graph algorithms whose practical performance remains unexplored.'),
(23,'§3, closeness centrality','research_direction','Develop the theory of fully dynamic closeness centrality beyond the isolated approximation result surveyed.'),
(28,'§5, generators','research_direction','Build realistic fully dynamic graph generators, covering both oblivious and adaptive adversaries.'),
(28,'§5, empirical data','research_direction','Expand representative real-world graph data containing both edge insertions and deletions.')
],'The source supplies a large table of algorithmic bounds, not a numbered theoretical problem list. Bound gaps are not automatically promoted to conjectures. OMv/APSP variants appear as assumptions supporting existing conditional lower bounds.')

area_note('unification','A specialist handbook chapter on syntactic and equational unification, algorithms and combinations of theories.',[
(40,'§3.4, distributivity with a unit','question','Is unification modulo two-sided distributivity together with a multiplicative unit decidable?'),
(39,'§3.4, associativity complexity','research_direction','Close the stated gap between NP-hardness and PSPACE for associative unification/word equations.'),
(40,'§3.4, distributivity complexity','research_direction','Determine tight complexity for unification with constants modulo two-sided distributivity.')
],'Only the first entry is explicitly called an open problem; the others record unresolved complexity gaps discussed by the authors. Broken “??” chapter references and equation symbols are not questions. This chapter does not cover higher-order unification comprehensively.')

area_note('knowledge_compilation','A foundational comparative survey and map of succinct knowledge representations, queries and transformations.',[
(9,'Table 3, DNNF / PI','question','Can prime-implicate representations always be expressed as polynomial-size DNNF?'),
(9,'Table 3, d-DNNF and sd-DNNF / PI','question','Can prime-implicate representations always be expressed as polynomial-size deterministic DNNF?'),
(9,'Table 3, d-DNNF and sd-DNNF / IP','question','Can prime-implicant representations always be expressed as polynomial-size deterministic DNNF?'),
(9,'Table 3, PI / MODS','question','Is prime-implicate representation polynomially succinct relative to explicit model enumeration?'),
(11,'Table 5, EQ for d-DNNF and sd-DNNF','question','Is equivalence testing polynomial-time for deterministic DNNF, equivalently its smooth variant?'),
(11,'Table 5, EQ for FBDD','question','Is equivalence testing polynomial-time for free binary decision diagrams?'),
(14,'Table 7, negation; discussion p.15','question','Are deterministic DNNF and smooth deterministic DNNF closed under polynomial-time negation?')
],'Unknown table cells were checked visually in the PDF. Smooth/nonsmooth duplicate cells are grouped using the paper’s polynomial equivalence; no implication direction is reversed.')

area_note('infinite_csp','A specialized survey of infinite-template CSPs, polymorphisms, logical representations and qualitative reasoning.',[
(14,'Question 1','research_direction','Identify natural subclasses of NP exhibiting a P/NP-complete dichotomy.'),
(14,'§6, finite-template dichotomy','conjecture','Every finite-template CSP is polynomial-time solvable or NP-complete.'),
(15,'Question 2','question','Is every NP problem polynomial-time equivalent to an ω-categorical-template CSP?'),
(15,'Question 3; §12.3','question','Can every CSP in SNP be represented by an ω-categorical template?'),
(20,'Question 4','question','Is the algebraic NP-hardness criterion of Theorem 10 necessary for ω-categorical-template CSPs?'),
(26,'§12.1','research_direction','Classify arbitrary-arity temporal, interval, partial/branching-time, RCC-5 and related qualitative CSP languages.'),
(26,'§12.2(a)','question','When can varieties replace pseudovarieties in capturing infinite-template CSP complexity?'),
(27,'§12.2(b)','research_direction','Develop tame congruence theory for oligomorphic algebras.'),
(27,'§12.2(c)','question','Lift complexity classifications from first-order definitions to first-order interpretations.'),
(27,'§12.2(d)','research_direction','Use model-theoretic and Jordan-group classifications to classify associated CSPs.'),
(27,'§12.3, final question','question','Which CSPs in NP are definable in SNP?')
],'This is a historical 2008 inventory. The finite-template dichotomy is retained as presented in this source, not asserted to remain open today.')

area_note('enumeration_strozecki','An expository monograph on enumeration complexity, algorithms, space, lower bounds and applications.',[
(22,'Open problem 3.1','question','Find a natural OutputP problem outside IncP, including the proposed K_t-free domination candidate.'),
(23,'Open problem 3.2','question','Weaken or reverse the ETH assumption behind the strict incremental-time hierarchy.'),
(32,'Open problem 4.1','question','Conditionally separate DelayP and IncP from their polynomial-space versions.'),
(32,'Open problem 4.2','question','Separate memoryless NextP from DelayP, preferably even polynomial-space DelayP.'),
(33,'Open problem 4.3','question','Enumerate binary-matroid circuits in incremental polynomial time and polynomial space.'),
(37,'Open problem 4.4','question','Amortize unknown incremental delay while retaining polynomial space and polynomial delay.'),
(41,'Open problem 5.1; Conjecture 5.1.1','conjecture','Exclude strong polynomial delay for DNF-model enumeration under a standard hypothesis.'),
(41,'Open problem 5.2; also p.61','question','Obtain sublinear-in-input-set-count average delay for union closure; settle strong polynomial delay.'),
(43,'Open problem 5.3','question','Conditionally separate strong polynomial delay from polynomial delay.'),
(45,'Open problem 5.4','question','Characterize when constant amortized enumeration becomes constant worst-case delay.'),
(47,'Open problem 5.5','question','Derive enumeration directly from random-walk or Boltzmann-sampling machinery.'),
(54,'Open problem 7.1','question','Find a natural hardness benchmark for DelayP inside a higher incremental-time class.'),
(54,'Open problem 7.2','question','Transfer hardness equivalences between strong-delay and incremental-time classes.'),
(54,'Open problem 7.3','question','Replace SETH by ETH in strongly-accessible-set-system enumeration lower bounds.'),
(55,'Open problem 7.4','question','Use SETH to exclude small delay for transversals, binary-matroid circuits or maximal cliques.'),
(58,'Open problem 7.5','question','Prove unconditional constant-pebble JAG lower bounds for distance-two query enumeration.'),
(58,'Open problem 7.6','research_direction','Develop enumeration circuit classes, unconditional separations and parallel/descriptive-complexity connections.'),
(59,'Open problem 7.7','question','Establish a finite-domain enumeration-CSP dichotomy.'),
(61,'Open problem 7.8','question','Prove IncP hardness for uniform closure under input-specified clones.'),
(61,'Open problem 7.9','question','Characterize supergraph enumeration for higher-arity clones and eliminate exponential space via reverse search.'),
(62,'Open problem 7.10','question','Can one unary operator affecting two components make closure membership NP-hard?'),
(66,'Open problem 7.11','question','Solve Mon-Factor for further polynomial classes; develop reverse-search polynomial-delay interpolation.'),
(66,'Open problem 7.12; continuation p.67','question','Compress previously enumerated monomials or interpolate with polynomial space.'),
(71,'Open problem 8.1','question','Obtain output-polynomial generation of molecular maps; bound the existing algorithm’s total time.'),
(77,'Open problem 9.1','question','Characterize enumeration via product/union circuits and tractable join extensions.'),
(77,'Open problem 9.2','research_direction','Find useful solution decompositions beyond unions and Cartesian products.'),
(79,'Open problem 9.3','question','Constant-factor under-approximate a natural problem not known to belong to IncP.'),
(80,'Open problem 9.4','question','Efficiently cover spanning trees or shortest paths under meaningful solution distances.'),
(80,'Open problem 9.5','question','Obtain distance-cover approximations through supergraph walks or flashlight search.'),
(80,'Open problem 9.6','question','Generate r spanning trees maximizing minimum pairwise Hamming distance in polynomial time.'),
(54,'§7.1, unnumbered transversal problem','question','Enumerate minimal hypergraph transversals in output-polynomial time.'),
(67,'§7.3.3, polynomial identity testing','question','Derandomize identity testing for explicitly represented arithmetic circuits.')
],'The stronger o(m)-delay DNF conjecture is explicitly disproved within this thesis and excluded. IncP₁ with polynomial space versus polynomial-space DelayP is also resolved here. The 30 numbered problems remain, with duplicate conjecture 5.1.1 grouped into 5.1.',scope=SCOPE+' All 30 numbered open problems, their subquestions and additional explicit unresolved discussions are represented.')

area_note('edge_modification','A specialist survey spanning edge editing, kernels, cuts, degree constraints, augmentation and geometric flips.',[
(8,'Open problem 2.1','question','Polynomial kernel for claw-free edge deletion?'),
(8,'Open problem 2.2','question','Polynomial kernel for line-graph edge deletion?'),
(9,'Open problem 2.3','question','Is Cograph Editing FPT above the vertex-disjoint-P₄ packing bound?'),
(10,'Open problem 2.4','question','Polynomial kernels for chordal edge deletion and editing?'),
(10,'Open problem 2.5','question','Extend Cai’s theorem naturally to chordal graphs.'),
(12,'Open problem 2.6','question','Polynomial kernel for Interval Completion?'),
(12,'Open problem 2.7','question','Polynomial kernel for Interval Deletion?'),
(12,'Open problem 2.8','question','Single-exponential FPT algorithm for Interval Deletion?'),
(12,'Open problem 2.9','question','Is Interval Editing FPT?'),
(12,'Open problem 2.10','question','Polynomial kernels for proper-interval deletion and editing?'),
(12,'Open problem 2.11','question','Is 5-Leaf Power Editing FPT?'),
(13,'Open problem 2.12','question','Polynomial kernel for Planar Deletion?'),
(13,'Open problem 2.13','question','Polynomial kernel for H-minor-free Deletion?'),
(13,'Open problem 2.14','question','Deterministic polynomial kernel for Edge Bipartization?'),
(13,'Open problem 2.15','question','Are comparability completion/deletion and permutation completion FPT?'),
(13,'Open problem 2.16','question','Is Proper Circular Arc Deletion FPT?'),
(13,'Open problem 2.17','question','Is Perfect Deletion FPT?'),
(15,'Open problem 2.18','question','Solve Proper Interval Completion in 2^{O(√k log k)}·n^{O(1)} time.'),
(15,'Open problem 2.19, surviving parts','question','Subexponential parameterized algorithms for planar deletion and 3-leaf-power completion?'),
(16,'Open problem 2.20','question','Can H-free completion/editing be subexponential yet exclude polynomial kernels?'),
(16,'Open problem 2.21','research_direction','Base modification lower bounds solely on P≠NP.'),
(17,'Open problem 2.22','question','Is König Edge Deletion FPT?'),
(18,'Open problem 3.1','question','Polynomial kernels for directed feedback vertex/arc set?'),
(18,'Open problem 3.2','question','Polynomial kernel for planar directed feedback vertex set?'),
(19,'Open problem 3.3','question','Single-exponential FPT for directed feedback sets, including planar vertex deletion?'),
(19,'Open problem 3.4','question','Classify directed three-terminal-pair Edge Multicut by cut size.'),
(19,'Open problem 3.5','question','Polynomial kernels for DAG Edge Multicut under the stated cut/terminal parameterizations?'),
(19,'Open problem 3.6','question','Classify planar Length-Bounded Edge-Cut by cut size.'),
(20,'Open problem 3.7','question','Classify weighted (μ,p,q)-Cut for nonedge and degree measures, parameterized separately by p or q.'),
(20,'Open problem 3.8','question','Classify exact-size vertex sets with bounded edge boundary, by size or boundary.'),
(20,'Open problem 3.9','question','Is Chain SAT FPT under the source’s stated parameter L?'),
(22,'Open problem 3.10','question','Polynomial kernel for 2-Club Cluster Deletion?'),
(23,'Open problem 4.1','question','Give efficient FPT degree-list editing algorithms parameterized by k+r.'),
(24,'Open problem 4.2','question','Polynomial kernel for connected exact-degree edge editing parameterized only by k?'),
(25,'Open problem 4.3','question','Classify connected degree-list edge editing, including bounded intervals.'),
(25,'Open problem 4.4','question','Classify directed degree-constraint editing variants.'),
(26,'Open problem 4.5','question','Classify degree-constraint editing on graph classes, including planar-preserving additions.'),
(27,'Open problem 4.6','question','Is an Eulerian subgraph with exactly m−k edges/arcs FPT?'),
(27,'Open problem 4.7','question','Classify strongly connected directed degree-balance editing.'),
(27,'Open problem 4.8','question','Is deleting k arcs to make every strong component Eulerian FPT?'),
(28,'Open problem 4.9','question','Classify weighted connected parity/degree-balance editing on graphs and multigraphs.'),
(28,'Open problem 4.10','question','Classify degree-congruence editing modulo d≥3, with and without connectivity.'),
(29,'Open problem 4.11','question','Find useful parameterized approximation for degree anonymization by edge modifications.'),
(29,'Open problem 4.12','question','Classify degree anonymization on restricted classes, including planar-preserving variants.'),
(30,'Open problem 4.13','question','Extend degree-sequence editing classifications to wider operation sets.'),
(30,'Open problem 4.14','question','Extend directed degree-sequence editing classifications to wider operation sets.'),
(31,'Open problem 5.1','question','Construct a uniform FPT algorithm for Planar Diameter Augmentation.'),
(32,'Open problem 5.2','question','Classify partial complementation into chordal, interval, P₅-free and bounded-minimum-degree classes.'),
(33,'Open problem 5.3','question','Polynomial kernel for geometric Flip Distance?'),
(34,'Open problem 5.4; following sentence','question','Is Strong Triadic Closure, or Cluster Deletion, FPT above maximum matching size?'),
(2,'Introduction, dichotomy','research_direction','Find a polynomial-time/NP-hard dichotomy for hereditary edge-deletion problems.'),
(6,'Table 1, line graphs; also p.9','question','Polynomial kernels for line-graph completion/editing; subexponential algorithms for all three operations?'),
(6,'Table 1, claw-free graphs','question','Polynomial kernels for claw-free completion and editing?'),
(6,'Table 1, claw-and-diamond-free graphs','question','Polynomial kernels for completion/editing; subexponential completion and sharper deletion algorithms?'),
(11,'Table 2, distance-hereditary; also p.12','question','Polynomial kernels for all distance-hereditary modification variants; improve generic FPT algorithms.'),
(11,'Table 2, H-minor-free graphs','question','Subexponential H-minor-free edge deletion?'),
(11,'Table 2, 4-leaf powers','question','Polynomial kernels for all 4-leaf-power modification variants?'),
(11,'Table 2, proper interval graphs','question','Subexponential proper-interval deletion and editing?'),
(11,'Table 2, interval graphs','question','Polynomial kernel for Interval Editing; subexponential interval deletion/editing?'),
(11,'Table 2, strongly chordal graphs','question','Classify strongly chordal deletion/editing; polynomial kernels and subexponential algorithms for all variants?'),
(11,'Table 2, chordal graphs','question','Subexponential chordal edge deletion and editing?'),
(6,'Tables 1–2, dash-marked cases','research_direction','Investigate the tables’ understudied cases: s-plex completion/deletion, star-forest/pseudosplit kernels, and remaining subexponential variants.'),
(13,'§2.2, graph classes','research_direction','Classify modification for comparability, co-comparability, permutation, circular-arc and circle graphs beyond the numbered cases.'),
(13,'§2.2, iterative compression','research_direction','Make iterative compression broadly effective for edge modifications.'),
(21,'§3.2, vertex connectivity','question','Determine complexity of unrestricted vertex-connectivity augmentation beyond increasing connectivity by one.'),
(31,'§5.1, classical complexity','question','Is Planar Diameter Augmentation polynomial-time solvable or NP-hard?'),
(33,'§5.2, pattern modifications','research_direction','Systematically parameterize edge modifications constrained by a pattern graph.')
], 'All 50 numbered problems are represented. Problem 2.19 conflicts with Tables 1–2: triangle-free deletion, linear-forest deletion and 3-leaf-power deletion/editing already have NOSUB lower bounds there; those subparts are excluded. Table-only questions are included and tables were inspected visually. Dash-marked cells are grouped as exploratory directions, following the authors’ weaker status. Problem 3.9 literally names parameter L although its setup also uses k; no silent correction is made.',scope=SCOPE+' Includes all numbered questions and table-only/open prose cases. Broad table directions group multiple operation variants.')

area_note('vadhan2012','A specialist monograph unifying pseudorandom generators, expanders, codes, extractors and derandomization.',[
(22,'Open Problem 2.10','question','Does P=RP?'),
(23,'Open Problem 2.14','question','Does P=BPP?'),
(24,'Open Problem 2.17','question','Which inclusions among P, ZPP, RP and BPP are strict?'),
(34,'Open Problems 2.36 and 7.32','question','Deterministically approximate the number of satisfying DNF assignments in polynomial time.'),
(38,'Open Problem 2.47','question','Do RL and BPL equal L?'),
(55,'Open Problem 3.4','question','Place BPP in quasipolynomial or subexponential deterministic time.'),
(57,'Open Problem 3.7','question','Explicitly construct the universal determinant-evaluation points, ideally in NC, to derandomize perfect matching.'),
(57,'Open Problems 3.9 and 4.48; p.124','question','Construct polynomial-length universal traversal sequences for arbitrary edge labelings.'),
(104,'Open Problem 4.24','question','Construct averaging samplers simultaneously optimal in randomness and sample count.'),
(119,'Open Problem 4.42','question','Give combinatorial constructions of Ramanujan or comparably strong constant-degree expanders.'),
(119,'Open Problem 4.43','question','Explicitly construct balanced bipartite vertex expanders with expansion D−O(1).'),
(119,'Open Problem 4.44','question','Explicitly construct undirected vertex expanders with expansion arbitrarily close to D.'),
(123,'Open Problem 4.47','question','Simulate RL deterministically in space log^c n for c<3/2.'),
(140,'Open Problem 5.9','question','Determine the optimal asymptotic binary rate–distance tradeoff.'),
(146,'Open Problem 5.20','question','Can full-length Reed–Solomon codes be combinatorially list-decoded beyond the stated square-root bound?'),
(154,'Open Problem 5.26','question','Construct explicit binary codes with efficient list decoding approaching capacity; see the formulation caveat.'),
(162,'Open Problems 5.36 and 6.35; p.197','question','Construct polylog-degree near-lossless unbalanced expanders, equivalently the specified near-optimal lossless condensers.'),
(202,'Open Problem 6.41','question','Construct logarithmic-seed extractors with constant entropy loss.'),
(203,'Open Problem 6.42','question','Construct extractors with seed length log n+O(1) and substantial output.'),
(203,'Open Problem 6.43','question','Give direct optimal-order seed/output extractor constructions.'),
(225,'Open Problem 7.13','question','Construct cryptographic PRGs from arbitrary one-way functions with seed length linear in input length.'),
(239,'Open Problem 7.25','question','Build linear-seed hardness-to-randomness generators of the specified black-box form.'),
(241,'Open Problem 7.31','question','Does BPAC⁰=AC⁰, or at least BPAC⁰⊆P?'),
(242,'Open Problem 7.33','question','Construct subpolynomial-seed PRGs fooling AC⁰[2].'),
(255,'Open Problem 7.53','question','Do constant-query locally decodable binary codes have polynomial blocklength?'),
(293,'Open Problem 8.5','question','Explicitly realize near-optimal unified Γ constructions with efficient local list decoding.'),
(295,'Open Problem 8.6','question','Fool width-four read-once branching programs with seed length o(log²m).'),
(297,'Open Problem 8.7','question','Derive strong uniform PRGs from EXP not contained in randomized subexponential time.'),
(298,'Open Problem 8.8','question','Does promise-BPP derandomization imply superpolynomial circuit lower bounds for E?'),
(298,'Open Problem 8.9','question','Does promise-BPP derandomization imply exponential-scale circuit lower bounds for NEXP?'),
(299,'Open Problem 8.10','question','Find natural combinatorial or algebraic complete problems for randomized classes.'),
(306,'Open Problem 8.11','question','Construct two-source extractors for every constant positive entropy rate.'),
(306,'Open Problem 8.12','question','Extract from circuit-samplable sources with low entropy or negligible error under plausible assumptions.'),
(36,'§2.4, directed reachability','question','Improve deterministic directed-reachability space, or achieve polynomial time with subpolynomial space.'),
(52,'§2, interactive proofs; also p.268','question','Derandomize AM to NP; in particular, establish NP certificates for graph nonisomorphism.'),
(154,'§5.2, large alphabets','question','Make the capacity-approaching large-alphabet code construction fully explicit and deterministic.'),
(181,'§6, seedless extraction','research_direction','Construct deterministic extractors for further structured source classes.'),
(243,'§7.5, NP hardness amplification','question','Obtain suitable worst-case-to-average-case reductions within NP.'),
(302,'§8.2.3, NP amplification','question','Achieve optimal exponential-scale hardness amplification within NP.'),
(303,'§8.2.3, uniform amplification','question','Match nonuniform high-end amplification uniformly, including optimal NP amplification parameters.')
], 'All 36 numbered Open Problem labels are covered, with three restatement pairs grouped. Open Problem 5.26 prints a rate inequality inconsistent with the capacity discussion and preceding bound; the entry records the intended capacity-construction topic without presenting that inequality as a valid target. Exercises, proved statements and citations-only occurrences are excluded.',scope=SCOPE+' Replaces the earlier selected inventory with all numbered Open Problem labels and unnumbered unresolved discussions.')

area_note('arithmetic_circuits','A specialist survey of arithmetic lower bounds, identity testing and reconstruction.',[
(11,'Open Problem 1','question','Improve permanent determinantal-complexity lower bounds.'),
(19,'Open Problem 2','question','Separate homogeneous and unrestricted formulas superpolynomially.'),
(19,'Open Problem 3','question','Separate multilinear and general circuits superpolynomially.'),
(19,'Open Problem 4','question','Separate semantic and syntactic multilinear circuits superpolynomially.'),
(21,'Open Problem 5','question','Compute all second derivatives with constant-factor circuit overhead.'),
(26,'Open Problem 6','question','Prove superpolynomial depth-four lower bounds outside characteristic two.'),
(31,'Open Problem 7','question','Improve general circuit lower bounds, including superlinear bounds for explicit constant-degree polynomials.'),
(32,'Open Problem 8','question','Prove superpolynomial arithmetic-formula lower bounds.'),
(33,'Open Problem 9','question','Separate monotone and general circuits for constant-degree polynomials.'),
(35,'Open Problem 10','question','Prove superpolynomial noncommutative-circuit lower bounds.'),
(38,'Open Problem 11','question','Prove superpolynomial ΣΠΣ lower bounds over infinite fields.'),
(41,'Open Problem 12','question','Prove superpolynomial, or even superlinear, lower bounds for the symmetric model’s m(f).'),
(42,'Open Problem 13','question','Prove superpolynomial multilinear-circuit lower bounds.'),
(44,'Open Problem 14','question','Separate multilinear and general formulas.'),
(51,'Open Problem 15','question','Construct explicit three-dimensional tensors with superlinear rank.'),
(56,'Open Problem 16','question','Develop algebraic pseudorandom functions and a corresponding natural-proofs barrier.'),
(67,'Open Problem 17','question','Does efficient PIT for a circuit class imply permanent lower bounds for that class?'),
(69,'Open Problem 18','question','Derandomize black-box depth-four PIT.'),
(69,'Open Problem 19','question','Preserve bounded depth under factorization, including factors linear in one variable.'),
(70,'Open Problem 20','question','Convert multilinear/formula lower bounds into restricted-model PIT algorithms.'),
(70,'Open Problem 21','question','Derandomize multilinear-formula PIT in subexponential time.'),
(75,'Open Problem 22','question','Derandomize black-box PIT for noncommutative formulas.'),
(76,'Open Problem 23','question','Derandomize PIT for noncommutative circuits.'),
(76,'Open Problem 24','question','Derive noncommutative black-box PIT from exponential noncommutative lower bounds.'),
(76,'Open Problem 25','question','Derandomize ΣΠΣ PIT in subexponential time.'),
(81,'Open Problem 26','question','Derandomize multilinear ΣΠΣ PIT in subexponential time.'),
(82,'Open Problem 27','question','Derandomize set-multilinear ΣΠΣ black-box PIT in subexponential time.'),
(89,'Open Problem 28','question','Obtain subexponential PIT for bounded-top-fanin depth-four circuits.'),
(95,'Open Problem 29','question','Obtain polynomial-time black-box PIT for read-once formulas.'),
(100,'Open Problem 30','question','Derandomize PIT for elementary symmetric polynomials applied to linear forms.'),
(102,'Open Problem 31','question','Reconstruct sums of few read-once formulas in subexponential time.'),
(104,'Open Problem 32','question','Does learning a circuit class imply permanent lower bounds against it?'),
(59,'§4 introduction, perfect matching','question','Derandomize the parallel perfect-matching algorithm.'),
(97,'§4.9, general factorization; also p.100','question','Deterministically factor multivariate polynomials efficiently; does PIT derandomization suffice?'),
(111,'§5.5, reconstruction','research_direction','Reconstruct circuit classes admitting PIT and strengthen reconstruction-hardness consequences.')
],scope=SCOPE+' Replaces the earlier selection with all 32 numbered problems and additional unresolved discussions.')

def extend_area(key, rows=(), caution=''):
    old=NOTES[key]
    original=[(p['pdf_page'],p['locator'],p['kind'],p['summary']) for p in old['problems']]
    area_note(key,old['selection_reason'],original+list(rows),
              ' '.join(x for x in [old['caution'],caution] if x))

extend_area('quantum_algorithms',[
(11,'§8, Boson Sampling','conjecture','Classical computers cannot efficiently sample the Boson Sampling distribution in the regime described in the source.')])

extend_area('understanding_ml',[
(112,'§8.1, randomized computation','question','Which inclusions among P, RP and NP are strict?')])

extend_area('raoyehudayoff',[
(42,'Open Problem 2.19','research_direction','Find a more direct geometric proof of the already established monochromatic-submatrix Lemma 2.14.'),
(53,'Chapter 3 introduction','research_direction','Prove optimal lower bounds in the general number-on-forehead communication model.'),
(100,'§8, perfect matching','question','Are there polynomial-size logarithmic-depth general Boolean circuits for perfect matching?')],
'Open Problem 2.19 requests a new proof of a known result, and is classified as a research direction rather than an unresolved theorem.')

extend_area('coding_theory',[
(148,'§7.2, inner-code construction; setup p.147','question','Construct the inner linear codes on the Gilbert–Varshamov bound in time polynomial in their own dimension, eliminating the exhaustive search.'),
(151,'§7.4 discussion, Zyablov bound','question','Improve the Zyablov bound in the high-distance regime using variants of concatenation.')],
'The p.148 cross-reference is literally “Open Question ??”. The inventory records only the construction question explicitly described by the surrounding paragraphs; no missing question number is reconstructed. Questions 7.2.1 and 7.2.3 are answered later in these chapters and are excluded.')

extend_area('repetitive_strings',[
(14,'§3, LZ-End measure','question','Are there string families with non-overlapping Lempel–Ziv phrase count z_no=o(z_e), where z_e is the stated LZ-End variant?'),
(19,'§3.5, collage systems','question','Are there string families with collage-system size c=o(z), even allowing general collage systems?'),
(22,'§3.7, lexicographic parsing','question','Are there string families with Lempel–Ziv size z=o(v), where v is the lexicographic parsing measure?'),
(23,'§3.9, string attractors; also pp.24–25','question','Can every string be represented in O(γ) words, where γ is its smallest attractor size? Can the O(γ log n) scale always be improved asymptotically?'),
(26,'§3.10, reachability of repetitiveness measures','question','What is the smallest reachable repetitiveness measure supporting efficient access or indexing? Specifically, obtain access in O(z_no) space and indexing in O(z_no) or O(v) space.'),
(60,'§8.2, dynamism','research_direction','Develop efficient repetitive indexes supporting arbitrary text modifications, beyond appending/prepending and the restricted practical performance of existing constructions.')],
'The resolved Burrows–Wheeler-transform conjecture is excluded. The construction entry covers the BWT, Lempel–Ziv and grammar subcases across pp.58–60; dynamism is recorded separately.')

extend_area('nordstrom2013',[
(12,'§2, cutting planes','question','Is unrestricted cutting planes strictly stronger than the polynomial-coefficient subsystem CP*?'),
(22,'§3.2, resolution refinements','question','Is linear resolution strictly weaker than general resolution?'),
(24,'§3.4, variable space','question','Is the resolution variable-space decision problem in PSPACE, closing the gap to the EXPSPACE upper bound?'),
(50,'Open Problem 9, qualified by §7 pp.54–56','research_direction','Strengthen space-faithful projections for cutting planes and polynomial calculus/PCR so that pebbling space bounds and tradeoffs transfer tightly beyond the partial results in the added-in-proof update.'),
(50,'Open Problem 12','research_direction','Give a direct proof that constant clause space implies polynomial resolution length, avoiding the known route through width.'),
(53,'§7, continues p.54; update pp.55–56','research_direction','Clarify the tight relationship of pebblings and pebbling formulas, and strengthen substitution-based hardness amplification for stronger proof systems.'),
(54,'§7, after Theorem 7.1, continues p.55','conjecture','Remove the proof-length logarithms from the PCR/CP pebbling bounds to obtain unconditional space lower bounds for these formulas.')],
'The 18 numbered questions were checked against §7. Problems 5 and 17 are resolved in the same source and excluded. Problem 9 has partial progress in the update, so only the remaining tight-transfer direction is retained. Problem 12 requests a new proof of an established statement.')

extend_area('goldreich2017',[
(180,'Exercise 7.3, footnote 31','question','Can completeness of the indistinguishability lower-bound method be proved without the threshold slack in the stated converse?'),
(220,'§8.5.1, intermediate complexity','question','Find natural dense-graph properties testable with fewer than tower(log(1/ε)) queries but requiring superpolynomial dependence on 1/ε, for example exponential query complexity.'),
(222,'§8.5.3, conjecture following examples','conjecture','For each t≥4, there are graph properties with nearly linear reciprocal-distance adaptive complexity and nonadaptive complexity Θ(ε^(−2+2/t)).'),
(227,'§8.6.3, randomized graph-property recognition','conjecture','Every nontrivial monotone property of k-vertex graphs requires Ω(k²) randomized adjacency queries for exact recognition.'),
(280,'§9.7, proximity-oblivious testers','research_direction','Complete the characterization of bounded-degree graph properties admitting constant-query one-sided proximity-oblivious testers, removing the stated combinatorial-conjecture dependency.'),
(283,'§9.7.2, directed acyclicity','question','Test acyclicity of bounded-degree digraphs using o(k) queries.'),
(354,'Corollary 11.31, footnote 46; setup p.353','question','Does testing m-grained distributions themselves (δ=0), for m=Θ(n), require Ω(n/log n) samples?'),
(377,'§12.6, motivating complexity conjecture','conjecture','P differs from NP.'),
(401,'§13, footnote 28','question','Is graph nonisomorphism in BPP?')],
'The explicitly unresolved strengthening in Exercise 7.3’s footnote is included, while the solved exercise itself is not. At p.280 the cited combinatorial conjecture is not stated in full, so only the source’s characterization direction is recorded.')

extend_area('markov_mixing',[
(115,'Chapter 7 notes, coloring lower bound','question','Can the c_(Δ,q) n log n lower bound for coloring Glauber dynamics use a universal positive constant independent of Δ and q?'),
(175,'Chapter 11 notes, computing cover time','question','Can the exact cover time of a finite graph be computed deterministically in polynomial time?'),
(257,'Chapter 16 notes; continues p.258','conjecture','For L≈n^α with 0<α<1, the L-reversal shuffle mixes in Θ(n^max(1,3−3α) log n) time, as conjectured by Durrett.'),
(338,'Chapter 22 notes, censoring','question','Does Potts Glauber dynamics started from a monochromatic configuration satisfy the same censoring property as Ising dynamics?'),
(350,'§23.5, exclusion-process cutoff','question','Establish cutoff for biased exclusion on the n-path in the regimes not covered by the fixed-bias result recorded on this same page.'),
(350,'§23.5, interchange process','question','Does the interchange process on the cycle exhibit cutoff?'),
(399,'Example B.3, self-avoiding walks','research_direction','Find an efficient algorithm for counting planar self-avoiding walks of a specified length.'),
(402,'Example B.5; also p.399','question','Analyze the convergence and mixing time of the pivot chain on self-avoiding walks.')],
'The broad coloring question on p.230 is grouped with Chapter 26 Question 7. The historical cyclic-to-random mixing-order question on p.129 is answered on p.130; only the remaining cutoff question is kept. Page 350 first calls biased-exclusion cutoff open, then gives a fixed-bias solution; the inventory explicitly restricts to the remaining regimes.')

area_note('fine_grained','A specialist survey defining the central fine-grained hypotheses and reductions.',[
(2,'§1, SAT lower bounds','question','Prove superlinear unconditional SAT time lower bounds in robust unrestricted computation models; establish stronger exponential lower bounds.'),
(2,'§1, P versus NP','conjecture','P differs from NP.'),
(4,'Hypothesis 1, SETH','conjecture','For every ε>0 some clause width k precludes randomized O(2^((1−ε)n)) time for k-SAT.'),
(5,'Hypothesis 2, 3-SUM','conjecture','Integer 3-SUM admits no randomized truly subquadratic algorithm.'),
(6,'Hypothesis 3, APSP','conjecture','Weighted APSP admits no randomized truly subcubic algorithm in the stated integer-weight regime.'),
(7,'Hypothesis 4, k-OV','conjecture','Boolean k-Orthogonal Vectors admits no randomized n^(k−ε) poly(d) algorithm for constant ε>0.'),
(9,'§3, diameter approximation','question','Improve the nearly n^(3/2) running time for 3/2-approximate diameter on sparse graphs, ideally to linear time.'),
(14,'§4, tree edit distance','question','Is tree edit distance fine-grained equivalent to APSP?'),
(15,'Hypothesis 5, HS','conjecture','Hitting Set on Boolean vectors admits no randomized truly subquadratic poly(d)-factor algorithm.'),
(16,'§5, relationship of hypotheses','question','Does the Orthogonal Vectors hypothesis imply the Hitting Set hypothesis?'),
(16,'Hypothesis 6, k-Clique','conjecture','The matrix-multiplication exponent ωk/3 for k-Clique, primarily for k divisible by three, cannot be improved by a constant in the exponent.'),
(16,'Hypothesis 7, Min-Weight k-Clique','conjecture','Edge-weighted Min-Weight k-Clique requires randomized n^(k−o(1)) time in the specified weight range.'),
(16,'Hypothesis 8, Exact k-Clique','conjecture','Exact-weight k-Clique requires randomized n^(k−o(1)) time in the specified weight range.'),
(16,'§5, comparison with 3-SUM','question','Determine fine-grained relationships between APSP and 3-SUM.'),
(17,'§5, combinatorial BMM','research_direction','Formalize and resolve the informal hypothesis that combinatorial Boolean matrix multiplication requires n^(3−o(1)) time.'),
(17,'Hypothesis 9, OMV','conjecture','Online Boolean matrix-vector multiplication for n queries requires randomized total time n^(3−o(1)).'),
(18,'Hypothesis 10, NSETH','conjecture','Refuting unsatisfiable k-CNF formulas for unbounded k requires nondeterministic 2^(n−o(n)) time.'),
(18,'§6, C-SETH and NC-SETH','conjecture','Circuit-SAT for the described richer representation classes, especially polynomial-size polylog-depth circuits, requires 2^(n−o(n)) time.'),
(19,'§6, disjunction of hypotheses','conjecture','At least one of SETH, the APSP hypothesis and the 3-SUM hypothesis is true.'),
(20,'§7, fine-grained cryptography','question','Construct further cryptographic primitives, including one-way functions, from fine-grained assumptions.'),
(20,'§7, algorithmic time–space tradeoffs','research_direction','Prove strong unconditional lower bounds for suitably space-restricted 3-SUM algorithms.')],
'All ten numbered hypotheses are included as conjectures, alongside explicitly unresolved prose questions. The source says the combinatorial BMM notion is not well defined. AM/MA versions of NSETH are refuted inside the source and excluded. Data-structure and I/O hypotheses merely attributed to other papers without statements are not reconstructed.')

# These existing source inventories already cover their explicit question lists.
for key in ['local_algorithms','williamson2011','peikert','dwork_roth','fair2022','scheduling2017','reconfig2020']:
    extend_area(key)

# Replace cautions whose earlier selective scope no longer describes this pass.
NOTES['coding_theory']['caution']='The PDF is a partial draft. The p.148 cross-reference is literally “Open Question ??”; only the construction question explicitly described by its surrounding paragraphs is recorded, without reconstructing a missing question number. Questions 7.2.1 and 7.2.3 are answered later in the same chapters and are excluded.'
NOTES['nordstrom2013']['caution']='The 18 numbered questions were checked against §7. Problems 5 and 17 are resolved in the same source and excluded. Problem 9 has partial progress in the update, so only the remaining tight-transfer direction is retained. Problem 12 requests a new proof of an established statement and is classified as a research direction.'
NOTES['raoyehudayoff']['caution']='This is a 120-page early draft, not the full published book. Publication year 2020 does not date this file. Open Problem 2.19 requests a new proof of a known result and is classified as a research direction.'
NOTES['quantum_algorithms']['caution']='The outlook supplies broad research directions, while Boson Sampling is a separate conjectural hardness statement. Consult the source for the sampling model and assumptions.'
NOTES['goldreich2017']['problems'][3]['summary']='Improve dense-graph bipartiteness testing below quadratic reciprocal-distance dependence; establish Conjecture 8.10 that the specified random induced subgraph preserves distance from bipartiteness.'
NOTES['markov_mixing']['problems'][6]['locator']='Chapter 26 Question 7; related question p.230'
NOTES['markov_mixing']['problems'][6]['summary']='Does coloring Glauber dynamics mix in O(n log n) for q>Δ+2? More broadly, does q>Δ+C imply polynomial or O(n log n) mixing?'
