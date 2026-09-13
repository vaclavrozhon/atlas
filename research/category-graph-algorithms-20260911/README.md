# Structural graph theory and graph algorithms

User-approved expansion on 2026-09-11. The display label changes; the stable
category ID `structural`, key `Structural graph theory`, position, target 20 and
two focus places remain. Twelve active records move from Algorithms and data structures.

## Individual transfers

| ID | Problem | Reason |
| --- | --- | --- |
| TCS-6536 | Deterministic linear-time minimum spanning tree | The target is deterministic linear-time construction of a minimum spanning tree on a static weighted graph. |
| TCS-6538 | Almost-linear-time exact maximum matching in general graphs | The question asks for an almost-linear sequential algorithm for exact maximum-cardinality matching on static general graphs. |
| TCS-6539 | Almost-linear triangle detection | The target is an almost-linear triangle-detection algorithm on explicit static graphs, rather than a conditional reduction or lower bound. |
| TCS-6511 | Is Exact Matching on general graphs in deterministic polynomial time? | Deterministic Exact Matching is a static graph algorithm with a prescribed edge-color count. |
| TCS-0611 | Bipartite Exact Matching: deterministic polynomial time | The bipartite restriction of Exact Matching belongs with the general static graph problem; the recorded claimed resolution and uncertain status are preserved. |
| TCS-7180 | Is graph canonization polynomial-time reducible to graph isomorphism? | Computing a canonical graph representative using a graph-isomorphism oracle is a graph algorithm and structural-equivalence question. |
| TCS-0771 | Computational complexity of planar treewidth | Computing planar graph treewidth joins graph structure with static algorithms; no parameterized running-time target is specified. |
| TCS-0595 | Two anticomplete paths with unrestricted terminal pairing | The target is polynomial-time detection of two anticomplete paths in a static graph with four specified terminals. |
| TCS-0594 | Is 3-colorability polynomial-time decidable on diameter-two graphs? | The question is polynomial-time 3-colorability on diameter-two graphs, a static algorithmic classification of a graph class. |
| TCS-0773 | Near-linear algorithms for many-terminal vertex-disjoint surface paths | Near-linear computation of vertex-disjoint paths on surface-embedded graphs is a static graph algorithm. |
| TCS-0775 | Optimal exact-distance labels for planar graphs | Exact-distance labels for planar graphs encode graph distances and exploit graph structure, rather than general-purpose dictionary or cell-probe primitives. |
| TCS-0612 | Order-based labels for directed reachability | Order-based labels encode reachability in a static directed graph, making graph structure and graph queries the central target. |

## Focus selection

The graph pair is Hadwiger (TCS-6651) and deterministic linear-time MST (TCS-6536),
covering structure and algorithms. Erdős–Hajnal (TCS-6652) remains in the category
outside its two focus places. Almost-linear maximum matching (TCS-6538) moves with
the other static graph problems and remains available in the larger selection.

The ADS focus now covers splay-tree dynamic optimality (TCS-6498), integer sorting
(TCS-6537), cell-probe lower bounds (TCS-6540), deterministic static dictionaries
(TCS-6586), and working-set heaps (TCS-0474). The last two replace the transferred
MST and matching entries. This balances importance with distinct data-structure
targets; it does not change importance scores or promote draft evidence.

## Boundaries and publication

Moves are explicit per-record overrides. Dynamic, parallel/distributed, parameterized
and conditional fine-grained questions retain their specialist homes. General-purpose
data structures remain in ADS. Archived records and their decisions are untouched.
Bipartite Exact Matching retains its uncertain status and saved note about a claimed
resolution. This classification review is not a fresh verification of open status.

The registry drives UI labels and exports. The existing planar-treewidth taxonomy
expectation is updated to the newly accepted category. See [decisions.json](decisions.json)
for previous overrides and focus choices, and verification.json
for publication and browser checks.
