# Algorithms and Data structures split — 11 September 2026

The user approved a new small Data structures category and the rename of the
existing large category to Algorithms, including splay trees and static cell-probe
lower bounds as the two new focus topics. The individual assignments below apply
that scope to the existing cards. This is a category and selection review, not a
new mathematical, formulation, importance-score or current-open-status review.

## Result

| Category | Before | After | Selection target |
| --- | ---: | ---: | ---: |
| Algorithms | 120 | 99 | 50 |
| Data structures | 0 | 26 | 20 |
| Dynamic algorithms | 40 | 35 | 20 |

There are now 10 large and 25 small categories, assigning all 1,000 planned
places. Data structures sits immediately before Dynamic algorithms. The old
Algorithms ID and internal key remain unchanged, so stored category selections
and source provenance keep their identity. The new category has ID
`data-structures` and key `Data structures`. All 26 candidates stay active; the
Top 1000 takes its first 20 and the Top 100 its first two.

## Individual transfers

| Card | Previous category | Reason |
| --- | --- | --- |
| [TCS-6498](../../build/index.html#TCS-6498) — Are splay trees dynamically optimal? | Algorithms and data structures | Dynamic optimality compares legal binary-search-tree access strategies; the maintained search structure is the main object. |
| [TCS-6540](../../build/index.html#TCS-6540) — An explicit static problem requiring superlogarithmically many cell probes | Algorithms and data structures | The question asks for a general static cell-probe data-structure lower bound under explicit space and query constraints. |
| [TCS-6586](../../build/index.html#TCS-6586) — Can a static dictionary be built deterministically in linear time? | Algorithms and data structures | The target is construction and lookup performance of a static dictionary, a basic data-structure primitive. |
| [TCS-0949](../../build/index.html#TCS-0949) — Data Structure Lower Bound in the Cell Probe Model | Algorithms and data structures | The Boolean matrix-vector question measures memory accesses to a succinct preprocessed representation in the cell-probe model. |
| [TCS-6508](../../build/index.html#TCS-6508) — Do splay trees support deque operations in constant amortized time? | Algorithms and data structures | The target is the amortized cost of deque operations in a specified splay-tree implementation. |
| [TCS-6512](../../build/index.html#TCS-6512) — Does splaying every BST preorder take linear total time? | Algorithms and data structures | The target is the cost of a structured access sequence in a self-adjusting binary search tree. |
| [TCS-6509](../../build/index.html#TCS-6509) — Does recursively splitting a splay tree always take linear total time? | Algorithms and data structures | The target is the total cost of splitting a splay tree, including its restructuring operations. |
| [TCS-6514](../../build/index.html#TCS-6514) — Do pure pairing heaps support O(log log n) amortized decrease-key? | Algorithms and data structures | The question concerns the amortized operation bounds of pure pairing heaps. |
| [TCS-6502](../../build/index.html#TCS-6502) — Can lazy B-tree priority queues keep their I/O bounds with stable handles? | Algorithms and data structures | Stable handles and block-transfer bounds define an external-memory priority-queue interface. |
| [TCS-1913](../../build/index.html#TCS-1913) — This raises a natural question: does there exist a cache-oblivious priority queue that achieves the same amortized bounds on comparisons and I/Os? | Algorithms and data structures | The target is a cache-oblivious priority queue with simultaneous comparison and I/O guarantees. |
| [TCS-4997](../../build/index.html#TCS-4997) — Optimal Non-Adaptive Cell Probe Dictionaries and Hashing — Explicit open question on PDF page 4 | Algorithms and data structures | The requested constructive hashing scheme implements an optimal nonadaptive dictionary. |
| [TCS-5706](../../build/index.html#TCS-5706) — The Group Access Bounds for Binary Search Trees — Explicit open question on PDF page 3 | Algorithms and data structures | The unified access bound is a performance guarantee for a binary-search-tree data structure. |
| [TCS-5758](../../build/index.html#TCS-5758) — Pairing heaps: the forward variant — Explicit open question on PDF page 6 | Algorithms and data structures | The question measures decrease-key in a specified pairing-heap implementation. |
| [TCS-5768](../../build/index.html#TCS-5768) — What Does Dynamic Optimality Mean in External Memory? — Explicit open question on PDF page 2 | Algorithms and data structures | The saved question concerns adaptive search-tree competitiveness and its external-memory model. |
| [TCS-6290](../../build/index.html#TCS-6290) — Bottom-Up Rebalancing Binary Search Trees by Flipping a Coin — Unresolved-question passage on page 13 | Algorithms and data structures | The question asks for depth guarantees from local randomized binary-search-tree rebalancing. |
| [TCS-6480](../../build/index.html#TCS-6480) — Strongly History-Independent Storage Allocation: New Upper and Lower Bounds — Unresolved-question passage on page 19 | Algorithms and data structures | The target is space overhead of a history-independent storage allocator. |
| [TCS-1783](../../build/index.html#TCS-1783) — Is there a candidate data structure for the convex shelling antimatroid that is fast enough to sort optimally? | Algorithms and data structures | The requested object is a data structure supporting convex-shelling-antimatroid operations efficiently enough for sorting; the representation and operation costs define the target. |
| [TCS-5103](../../build/index.html#TCS-5103) — The Diameter of Caterpillar Associahedra — Explicit open question on PDF page 3 | Algorithms and data structures | The saved target is construction of an optimal static search tree under a target probability distribution, generalizing ordered-search data structures. |
| [TCS-0956](../../build/index.html#TCS-0956) — Succinct Representation for Functions on Graphs | Algorithms and data structures | The question compares succinct arbitrary query representations with representations constrained to remain graphs; local accessibility and storage are the main objects. |
| [TCS-1418](../../build/index.html#TCS-1418) — Can we design a data structure of size 2 o(n ) that provides a good approximation for the shortest path under three faults? | Algorithms and data structures | The saved target is a compact preprocessed distance oracle queried with edge failures, rather than an algorithm maintaining an evolving graph. Existing formulation gaps remain recorded. |
| [TCS-1798](../../build/index.html#TCS-1798) — Is there a sparse fault-tolerant exact or approximate distance oracle for an arbitrary subset P of V × V ? | Algorithms and data structures | The target is a sparse preprocessed distance oracle for prescribed pairs and failure queries. It does not ask to maintain a graph across an update sequence. |
| [TCS-0300](../../build/index.html#TCS-0300) — The randomized complexity of online labeling | Dynamic algorithms | Online labeling maintains a sorted array or ordered labels under insertion and measures relocations, a general order-maintenance primitive. |
| [TCS-2730](../../build/index.html#TCS-2730) — Thus, even in the non-succinct case, designing worst-case update operations is an open problem. | Dynamic algorithms | Indexed-list access and worst-case insertion/deletion guarantees concern a general-purpose sequence data structure. |
| [TCS-3788](../../build/index.html#TCS-3788) — It is an open problem whether randomization can speed up partitioning algorithms and lead, in particular, to faster data structures for the various operations considered […] | Dynamic algorithms | Approximate rank and selection are ordered-set operations; randomized partitioning is requested to improve the data structure implementing them. |
| [TCS-4799](../../build/index.html#TCS-4799) — Limits of Quantum Speed-Ups for Computational Geometry and Other Problems: Fine-Grained Complexity via Quantum Walks — Unresolved-question passage on page 9 | Dynamic algorithms | The target classifies data structures with simultaneous determinism, efficient operations, compact space and history independence; quantum walks supply an application. |
| [TCS-5825](../../build/index.html#TCS-5825) — Dynamic Membership for Regular Languages — Conjecture 2.3 | Dynamic algorithms | The prefix-U1 target is a word-RAM lower bound for a small-monoid sequence supporting updates and prefix queries, a data-structure primitive motivated by dynamic language membership. |

## Focus selections

Data structures:

1. **TCS-6498 — Splay-tree dynamic optimality:** adaptive search-tree performance.
2. **TCS-6540 — Static cell-probe lower bounds:** general information-access limits.

Algorithms:

1. **TCS-6537 — Integer sorting:** A foundational algorithmic primitive whose optimal complexity tests the computational power of the word RAM and would affect many tasks built on ordering integer keys.
2. **TCS-0388 — Structured comparison sorting:** Sorting all pairwise sums is a classical structured comparison problem: the output is quadratic, but exploiting the inherited order with equally efficient total computation remains the target. It adds real-key comparison algorithms alongside word-RAM integer sorting and data structures.
3. **TCS-0946 — Combinatorial sparsification:** A universal cut-preserving reduction of hypergraphs to few weighted hyperedges is a broad compression target supporting many downstream algorithms. Its focus is the size of a combinatorial sparsifier, with no query-interface guarantee.
4. **TCS-0477 — Offline comparison complexity:** Finding final survivors of a fully known heap-operation sequence isolates the comparison information needed for a batch answer. It does not require an online priority queue or intermediate query responses.
5. **TCS-0475 — Deterministic selection:** The ordinary groups-of-three median-of-medians algorithm gives a precisely specified selection primitive whose worst-case analysis remains the saved question. It adds selection to the two sorting models.

The three Algorithms replacements come from the retained pool and keep their
existing evidence and importance scores. TCS-6586 remains active in Data
structures immediately below the two focus choices. No other category changes
its explicit focus selection. TCS-5548 was considered for Algorithms but its
saved summary describes a local matroid-intersection barrier with an incomplete
question, so it was not promoted to the focus prefix.

## Boundary decisions

- **Dynamic algorithms:** graph connectivity, matching, spanning forests,
  changing geometric solutions, text indexes and dynamic language/query
  maintenance remain. The five transferred questions instead target general
  sequence/storage primitives or their operation bounds.
- **TCS-3225:** retain Dynamic algorithms. Its saved question classifies total
  complexity regimes for families of range-update/query sequences under a
  reduction framework; it is not a specified general-purpose storage interface.
- **TCS-0477:** retain Algorithms. The complete heap-operation sequence is known
  in advance and only its final survivors are requested; no online heap interface
  must be implemented.
- **TCS-0946 and other cut sparsifiers:** retain existing placements. The requested
  object is a smaller hypergraph preserving all cuts, with no query-time interface.
- **TCS-1418 and TCS-1798:** transfer static distance oracles. A failure is supplied
  as part of a query on preprocessed data; the saved question does not require
  maintaining an evolving graph across updates. Unspecified parameters remain
  recorded as formulation gaps.
- **TCS-0467, TCS-0470, TCS-3038, TCS-5208:** retain String algorithms and
  computational biology, since compressed-text navigation and edit-distance
  search are the specialist targets. TCS-5288 asks about compression quality,
  rather than dictionary lookup.
- **TCS-0411, TCS-0471, TCS-0472, TCS-1861, TCS-3537, TCS-4650, TCS-6427:**
  retain Geometry, topology and metric spaces for geometric point-location,
  intersection and range-search questions.
- **TCS-1957, TCS-3766, TCS-5705:** graph-class labeling questions remain outside
  the chosen scope of general data structures. Their existing placements are
  unchanged by this split.
- **TCS-5571:** retain Algebraic computation. The saved target is approximation
  of binary rank-one matrices by a subspace; data structures are a consequence.

## Preservation and validation

`decisions.json` retains the old and new assignment fields, original registry
and old/new focus choices. Only `area` and `category_assignment` are edited in
the 26 canonical cards. Statements, definitions, status, evidence, citations,
source notes and importance scores are preserved. Category counts, ranks and
benchmark membership are regenerated from canonical inputs.

`validation.json` records preservation checks, and `checks.log` records the
existing offline suite. `browser-validation.json` records category-filter,
focus, rename and mobile checks in the reader.
