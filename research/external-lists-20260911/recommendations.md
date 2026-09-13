# Recommended additions — 11 September 2026

The user subsequently approved all fourteen candidates. They were added as
TCS-7241–TCS-7254; [the import record](imported.md) links the completed cards
and documents final formulation and status decisions. The recommendations below
retain the rationale of the preceding review.

I recommend the following **14 new candidates for discussion**. They are not
imports, completed cards, or new Top 100 selections. The first seven give the
most useful additional coverage for this Atlas; the remaining seven are strong
structural graph questions to compare against the category's existing 20-place
target. This ordering is editorial judgment, not a ranking established by the
sources.

The comparison includes active cards and the recovered historical catalogue.
No identical target was found for these fourteen. Nearby cards below were
checked at the statement/source level; a shared subject or an implication is
not being called an equivalence. Current-status checks mean reading the cited
research and searching for subsequent resolutions as of the review date. They
do not constitute verification of the underlying proofs.

## 1. FPT approximation of twin-width

**Target.** Are there computable functions `f,g` and a constant `c` such that an
algorithm, given a finite simple graph `G` and integer `k`, runs in
`f(k)|V(G)|^c` time and either correctly reports `tww(G)>k` or produces a
contraction sequence of width at most `g(k)`? Width is the maximum red degree
during the standard twin-width contraction process. No vertex order or
contraction sequence is supplied with the input.

**Why add it.** Finding the decomposition is the missing algorithmic ingredient
behind the use of twin-width for first-order model checking. This is a general
access-to-structure problem, not a request to improve one recognition algorithm.
Bonnet's research-project list poses precisely this question;
[*Twin-width one* (2025), introduction](https://arxiv.org/html/2501.00991v1#S1)
still identifies even XP approximation in general as open. Recognition of
twin-width one and approximation on ordered structures do not settle it.

**Atlas comparison.** TCS-0342 concerns twin-width of string graphs;
TCS-7181 concerns exact clique-width recognition. Neither asks for the above
general twin-width approximation. Archived TCS-5709 concerns CSPs beyond
twin-width, not this algorithm.

Discovery: [Bonnet, question 1](https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html).
Suggested category: Parameterized and exact algorithms.

## 2. Decidability of PL four-sphere recognition

**Target.** Is there a total algorithm which, given a finite triangulation of a
closed combinatorial 4-manifold, decides whether it is piecewise-linearly
homeomorphic to the standard 4-sphere? The manifold promise and PL category are
part of the question; recognizing a topological homotopy sphere is a different
target.

**Why add it.** This is a clean computability boundary in computational
topology. The corresponding recognition problems are decidable through
dimension three and undecidable from dimension five. The unresolved middle
dimension is explicitly identified in
[Joswig's July 2025 research presentation](https://page.math.tu-berlin.de/~joswig/presentations/Joswig-Applied%2BTopology-250715.pdf),
alongside the practical sphere-recognition work in
[*Frontiers of sphere recognition in practice*](https://link.springer.com/article/10.1007/s41468-022-00092-8).
No later resolution was found in the current search.

**Atlas comparison.** No four-sphere recognition target was found, including
in archived topology and geometry records. Three-sphere complexity and
unknot recognition concern a different dimension or object. Smooth Poincaré
is not a replacement formulation.

Discovery: [Garden's four-sphere question](https://www.openproblemgarden.org/op/is_there_an_algorithm_to_determine_if_a_triangulated_4_manifold_is_combinatorially_equivalent_to_the_4_sphere).
Suggested category: Computational geometry and metric spaces, with a computational-topology tag.

## 3. Linear-size Boolean circuits for stable ternary compaction

**Target.** For every `n`, does the map on `{0,1,2}^n` which moves all 2s to the
right while preserving the order of all 0s and 1s have a Boolean circuit of
size `O(n)`? Encode each symbol with two bits, require correctness on valid
encodings, use a fixed complete bounded-fan-in Boolean basis, and impose no
uniformity or depth requirement. The constant in `O(n)` is independent of `n`.

**Why add it.** This gives the circuit-lower-bound category an unusually concrete
function with a linear-time sequential implementation. Stability is essential.
[Regan's original question](https://www.openproblemgarden.org/op/linear_size_circuits_for_stable_0_1_2_sorting)
remains a useful precise target. The subsequent
[Asharov–Lin–Shi work, introduction](https://arxiv.org/html/2010.09884v2#S1)
distinguishes stable compaction from its small circuits for unstable compaction.
Lower bounds for indivisible payloads, and conditional network-coding lower
bounds, must not be reported as an unconditional answer for this Boolean model.
The search found no unconditional resolution of Regan's exact target.

**Atlas comparison.** No stable-compaction card was found in either pool.
Existing generic circuit lower bounds and integer sorting questions do not
specify this function. General lower-bound progress is related but is not
itself a duplicate.

Suggested category: Computational complexity, with a circuit-complexity tag.

## 4. Bounded Boolean dimension for planar cover graphs

**Target.** Is there an absolute constant `d` such that every finite poset whose
undirected cover graph is planar admits `d` linear orders of its elements and
a Boolean function `φ:{0,1}^d→{0,1}` which, for every pair of distinct elements
`x,y`, recovers `x<y` from the `d` comparisons of their positions in those
orders? The orders and function may depend on the poset.

**Why add it.** The question connects sparse graph structure to succinct
reachability representations. It is not merely an enumerative poset question.
The [Blake–Micek–Trotter paper](https://arxiv.org/abs/2206.06942) proves the
bound 13 with a unique minimal element and explains the reachability-labeling
consequence. The [2026 clique-width/dimension paper](https://doi.org/10.1112/plms.70116)
establishes bounded Boolean dimension for bounded clique-width, which does not
cover all planar cover graphs. No general resolution was found.

**Atlas comparison.** TCS-7177 (the 1/3–2/3 conjecture) and TCS-0805 (counting
linear extensions) ask different questions. No Boolean-dimension target was
found. Use **planar cover graph**, rather than silently substituting an upward
planar order diagram; both conventions occur in this literature.

Discovery: [Amarilli](https://a3nm.net/work/research/questions/#boolean-dimension-of-planar-posets)
and [Trotter](https://people.math.gatech.edu/~trotter/rprob.html).
Suggested category: Structural graph theory and graph algorithms.

## 5. Constant-factor subcubic treewidth sparsifiers

**Target.** Is there a universal constant `c>0` such that every finite simple
graph `G` has a subgraph `H` with maximum degree at most three and
`tw(H)≥tw(G)/c`? This is a subgraph-existence target. It asks neither for an
induced subgraph nor for an algorithm or a bound on `|V(H)|`.

**Why add it.** It asks whether all treewidth can be witnessed, up to a constant
factor, using bounded-degree structure. The distinction between constant and
polylogarithmic loss is the central structural assertion here, rather than a
construction-specific tuning parameter.
[Chekuri–Chuzhoy's degree-three sparsifier paper](https://home.ttic.edu/~cjulia/papers/treewidth-sparsifiers-SODA.pdf)
provides the foundational result; [Bonnet's 2025 paper](https://doi.org/10.1016/j.jctb.2025.03.002)
still describes the known guarantee with polylogarithmic loss. No later
constant-factor result was found.

**Atlas comparison.** TCS-6683 asks for the optimal grid-minor threshold.
An arbitrary subcubic witness can be quite different from a grid; a sharper
grid theorem is not an equivalent statement. The sparse-subgraph target was
not found in active or archived records. Keep the pathwidth question separate
if it is considered later.

Discovery: [Amarilli](https://a3nm.net/work/research/questions/#linear-treewidth-and-pathwidth-sparsifiers).
Suggested category: Structural graph theory and graph algorithms.

## 6. Polynomial-time minimum-color cycle

**Target.** Is there a deterministic polynomial-time algorithm that, given a
finite simple undirected graph with an explicit color label on each edge,
finds a simple cycle using the minimum number of distinct colors, or reports
that there is no cycle? The coloring need not be proper.

**Why add it.** A short, concrete optimization problem sits between a known
quasipolynomial algorithm and an unresolved polynomial bound.
[Fomin et al., SODA 2023](https://arxiv.org/abs/2211.04797), establish the
submodular-cycle algorithm that gives the quasipolynomial upper bound.
An oracle lower bound for arbitrary submodular costs does not settle the
explicit edge-color model. [Korhonen's current list, question 8](https://tuukkakorhonen.com/problems.html)
continues to ask for its complexity.

**Atlas comparison.** No matching target or source paper was found in either
pool. Minimum colored cut (the cstheory discussion) and shortest paths with
submodular costs are different problems. The new card must specify which
complexity assumptions are permitted in a negative resolution.

Suggested category: Structural graph theory and graph algorithms.

## 7. Automatizing dynamic programming for weighted independent set

**Target.** Let `τ(G)` be the minimum size of a tropical circuit that computes
the maximum independent-set weight in `G` for every assignment of nonnegative
vertex weights, using binary `max` and `+` gates. Is there one algorithm that,
given `G` and binary-encoded nonnegative integer weights, computes the optimum
in time polynomial in `τ(G)+n+L`, where `L` is their total bit length? The
circuit is not supplied. Fix the gate/constant conventions from the original
MWIS-circuit definition when writing the card.

**Why add it.** This tests whether the existence of a small dynamic program
can systematically be turned into efficient computation.
[Korhonen's ICALP 2021 paper](https://arxiv.org/abs/2102.06901) characterizes
optimal circuit size via treewidth on important graph classes; the uniform
algorithmic question is explicitly posed in
[his current list, question 4](https://tuukkakorhonen.com/problems.html).
The polynomial target should be one card; the weaker quasipolynomial
alternative should not be joined with it by an ambiguous “or”.

**Atlas comparison.** TCS-0481 asks for min-plus circuit lower bounds for
shortest paths. TCS-4982 concerns Frege automatability. Neither supplies this
uniform MWIS-versus-optimal-dynamic-program target, and no archived duplicate
was found. This is a newer, editorially selected addition whose conceptual
motivation carries more weight than its age.

Suggested category: Parameterized and exact algorithms.

## 8. Tutte's 5-flow conjecture

**Target.** Does every finite loopless bridgeless undirected multigraph admit
an orientation and values in `{1,2,3,4}` on its edges such that, at every
vertex, the sum entering equals the sum leaving **as integers**?

**Why add it.** This is a central global-flow existence assertion. It also has
concrete consequences for directed-cut packing, exhibited in
[Cornuéjols–Liu–Ravi (2025)](https://link.springer.com/article/10.1007/s00493-025-00159-x).
That paper states the 5-flow conjecture and uses the established 6-flow theorem
for its unconditional algorithmic guarantee. No general 5-flow resolution was
found. A modular formulation is equivalent, but the card should choose one.

**Atlas comparison.** TCS-7226 is Woodall's dijoin-packing conjecture. The
connection is a reason for interest, not an equivalence of these questions.
No 5-flow target was found in the two pools.

Discovery: [Garden](https://www.openproblemgarden.org/op/5_flow_conjecture),
[West](https://dwest.web.illinois.edu/openp/), item 59.
Suggested category: Structural graph theory and graph algorithms.

## 9. Berge–Fulkerson perfect-matching cover

**Target.** Does every finite loopless bridgeless cubic multigraph have a list
of six perfect matchings such that every edge belongs to exactly two of them?
Repetitions in the list are allowed.

**Why add it.** It asks for a remarkably rigid integral decomposition of
fractional matching structure. It remains distinct from the cycle-double-cover
theorem. A [July 2026 paper by Magalhães Júnior and Silva](https://arxiv.org/abs/2607.29511)
explicitly identifies the finite conjecture as open and studies its
relationship with infinite versions. No later resolution was found.

**Atlas comparison.** Existing matching algorithms and approximation cards
do not assert this exact six-matching decomposition. No active or archived
copy was found. Do not merge it into the resolved cycle-double-cover problem.

Discovery: [Garden](https://www.openproblemgarden.org/op/the_berge_fulkerson_conjecture),
[West](https://dwest.web.illinois.edu/openp/), item 62.
Suggested category: Structural graph theory and graph algorithms.

## 10. Barnette's Hamiltonicity conjecture

**Target.** Is every finite simple 3-connected cubic bipartite planar graph
Hamiltonian?

**Why add it.** It isolates a classical boundary between graph structure and
Hamiltonicity, with all hypotheses doing substantive work. The
[GD 2025 paper *Approximating Barnette's Conjecture*](https://doi.org/10.4230/LIPIcs.GD.2025.6)
states that it remains open and proves a relaxed book-embedding guarantee.
That relaxation is not a Hamiltonian cycle in the original graph. No general
resolution was found in the current search.

**Atlas comparison.** No Barnette target was found. Archived TCS-0337 is
partial vertex cover on planar bipartite graphs, an unrelated problem despite
the shared graph class. Algorithmic Hamiltonicity records do not imply this
structural existence assertion.

Discovery: [Garden](https://www.openproblemgarden.org/op/barnettes_conjecture),
[West](https://dwest.web.illinois.edu/openp/), item 46.
Suggested category: Structural graph theory and graph algorithms.

## 11. Caccetta–Häggkvist directed-girth conjecture

**Target.** For every integer `n≥2` and `1≤r≤n−1`, does every simple loopless
digraph on `n` vertices with minimum outdegree at least `r` contain a directed
cycle of length at most `ceil(n/r)`? Opposite arcs are allowed; parallel arcs
are not.

**Why add it.** This is a basic local-to-global assertion about directed
connectivity and short cycles. It complements the predominantly undirected
structural questions already in the Atlas.
[Guo's 2026 Discrete Mathematics article, Conjecture 1](https://umu.diva-portal.org/smash/get/diva2%3A2016769/FULLTEXT01.pdf)
states the general target while proving results for related rainbow-cycle
problems. These do not resolve the directed-girth conjecture. No general
resolution was found.

**Atlas comparison.** No exact target was found. TCS-0993 concerns algorithmic
graph-distance estimation. R13 below is related but asserts a different
neighborhood property; neither source is being used to claim equivalence.

Discovery: [Garden](https://www.openproblemgarden.org/op/caccetta_haggkvist_conjecture),
[West](https://dwest.web.illinois.edu/openp/), item 39.
Suggested category: Structural graph theory and graph algorithms.

## 12. Tuza's triangle packing–covering conjecture

**Target.** For every finite simple graph `G`, is `τ△(G)≤2ν△(G)`, where `τ△`
is the minimum number of edges meeting every triangle and `ν△` is the maximum
number of pairwise edge-disjoint triangles?

**Why add it.** It is a sharp min–max question about two canonical optimization
problems, extending well beyond one input family.
[*On Tuza's conjecture in dense graphs* (2025)](https://doi.org/10.1016/j.dam.2025.06.049)
explicitly leaves the general conjecture open. The
[August 2026 degree-seven result](https://arxiv.org/abs/2608.06538) concerns
a bounded-degree special case. Neither fractional duality nor known results
for random graphs resolve the stated integral worst-case inequality.

**Atlas comparison.** No triangle packing–covering inequality was found.
The occurrences of Tuza's name in TCS-0598 and papers on H-free independent
set are bibliographic, not duplicate statements.

Discovery: [Garden](https://www.openproblemgarden.org/op/triangle_packing_vs_triangle_edge_transversal).
Suggested category: Structural graph theory and graph algorithms.

## 13. Seymour's second-neighborhood conjecture

**Target.** Does every finite nonempty oriented graph have a vertex `v` with
at least as many vertices at directed distance exactly two as at distance
one? An oriented graph has no loops, parallel arcs, or opposite pair of arcs;
the two neighborhood sets are disjoint.

**Why add it.** This is a simple directed expansion principle with a long
independent literature. The [July 2026 Bai–Li–Park paper](https://arxiv.org/abs/2607.18047)
explicitly states that the general conjecture remains open and proves
restricted cases of a strengthening. Searches also encounter manuscripts
claiming complete proofs, including [Glover’s May 2026 revision](https://arxiv.org/abs/2501.00614); this review does not endorse those claims. The
contemporary specialist paper is the basis for treating the target as open,
with this claim-conflict recorded.

**Atlas comparison.** No duplicate was found. R11 concerns a minimum-degree
guarantee for a short directed cycle; this asks for a particular vertex's
neighborhood expansion. Their relationship should be documented if both
are selected, and they should compete for diversity in a short focus prefix.

Discovery: [Garden](https://www.openproblemgarden.org/op/seymours_second_neighbourhood_conjecture),
[West](https://dwest.web.illinois.edu/openp/2ndnbhd.html).
Suggested category: Structural graph theory and graph algorithms.

## 14. Neumann–Lara's planar two-color conjecture

**Target.** Can the vertices of every finite oriented planar graph be
partitioned into two sets, each inducing a digraph without a directed cycle?
The underlying undirected graph is simple; opposite arcs are forbidden.

**Why add it.** This supplies a directed counterpart to central planar
coloring questions and concerns decomposition into acyclic dependency
structures. [Li–Mohar](https://arxiv.org/abs/1606.06114) settle digirth at least
four, not all oriented planar graphs.
[Cambie et al.'s February 2026 paper, Conjecture 3](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p27/pdf) studies related
planar partitions. The current search found no resolution of the unrestricted
target. The 2026 result about the list version of the **Erdős–Neumann–Lara**
conjecture is a different conjecture and must not be used as a resolution here.

**Atlas comparison.** Existing undirected coloring, directed feedback-set
approximation and TCS-1168's promised-digraph coloring target do not state this
universal planar assertion. No archived copy was found.

Discovery: [Garden](https://www.openproblemgarden.org/op/partitioning_planar_digraphs).
Suggested category: Structural graph theory and graph algorithms.

## Selection consequences

The first seven are my preferred additions to the candidate pool. The seven
classical graph conjectures also merit consideration, but adopting all of them
would make the category allocation substantially more structural. Compare them
jointly with the existing graph shortlist; do not increase quotas or displace
the current focus selections automatically. R11 and R13 especially should not
both enter a very short diversity prefix without considering that overlap.

These are recommendations about scientific selection. Full card authoring
still needs definitions, checked source locators and the project's exact
resolution criterion. Difficulty of formalization was not used to exclude
any recommendation.
