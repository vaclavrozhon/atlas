# Expand Dynamic graph algorithms to Dynamic algorithms

User-requested on 2026-09-11. The current display name is **Dynamic algorithms**.
The stable ID `dynamic`, internal key `Dynamic graph algorithms`, small-category
position, target 20 and two focus places remain.

## Review

The active catalogue scan covers 2,747 records. Saved questions and primary titles
yielded 113 possible matches; the broader summary scan added 132. All 245 candidate
titles were screened. The screening inventory identifies individual
boundary decisions separately from obvious title-level matches. Saved formulations,
excerpts and working summaries support the [detailed decisions](decisions.json).
Neither discovery matches nor topic review establish current open status.

## Transfers

Eighteen active records move, growing the category from 22 to **40**.

| Previous category | Moved |
| --- | ---: |
| Algorithms & data structures | 8 |
| Computational geometry and metric spaces | 3 |
| Optimization and numerics | 1 |
| Fine-grained complexity | 1 |
| String algorithms and bioinformatics | 2 |
| Database theory and finite model theory | 3 |

| ID | Problem | Reason |
| --- | --- | --- |
| TCS-0300 | The randomized complexity of online labeling | Online labeling maintains a sorted array or ordered labels under insertions; the measured cost is relabeling and moving existing items after updates. |
| TCS-1221 | It remains an open question to obtain a dynamic base packing algorithm that updates independent of the packing number. | Maintain a matroid base packing as elements are inserted or deleted, with update time independent of the packing number. |
| TCS-1425 | Can one achieve the conditionally optimal update time O(k 2 )? | A vertex-failure connectivity oracle must update its state after a batch of failed vertices; the target is the dependence of update time on the batch size. |
| TCS-2730 | Thus, even in the non-succinct case, designing worst-case update operations is an open problem. | Maintain indexed-list access under insertions and deletions with worst-case update guarantees, replacing amortized rebuilding. |
| TCS-2798 | We leave open the question of closing the gap between upper and lower bounds for the worker-task assignment problem: the upper bound is polylog(wt) and […] | Maintain a memoryless worker-task assignment as demand changes while bounding the number of workers that switch assignments. |
| TCS-3788 | It is an open problem whether randomization can speed up partitioning algorithms and lead, in particular, to faster data structures for the various operations considered […] | Improve the partition-maintenance algorithms underlying dynamic ordered sets with approximate rank/selection queries through randomization. |
| TCS-4799 | Limits of Quantum Speed-Ups for Computational Geometry and Other Problems: Fine-Grained Complexity via Quantum Walks — Unresolved-question passage on page 9 | Classify dynamic data-structure tasks admitting simultaneous determinism, efficiency and history independence across update sequences. |
| TCS-5825 | Dynamic Membership for Regular Languages — Conjecture 2.3 | The prefix-U1 conjecture concerns a sequence maintained under updates and prefix-product queries; its lower-bound target is dynamic regular-language membership. |
| TCS-0387 | Dynamic Planar Nearest Neighbors | Maintain exact planar nearest-neighbor queries under point insertions and deletions with logarithmic operation bounds. |
| TCS-3647 | It remains open whether the dynamic Hausdorff distance and discrete 1-center problem in dimensions d ≥ 3 can similarly be solved in sublinear time. | Maintain Hausdorff distance and discrete one-center under point insertions and deletions with sublinear update time in higher dimensions. |
| TCS-3902 | Updating an abstract Voronoi diagram, after deletion of one site, in deterministic linear time remains an open problem. | Update an abstract Voronoi diagram after a site deletion deterministically in time linear in the affected boundary complexity. |
| TCS-5612 | On the Facility Location Problem in Online and Dynamic Models — Explicit open question on PDF page 16 | The selected fully dynamic facility-location question asks for constant-quality solutions with fast updates or limited reassignment as clients arrive and depart. |
| TCS-3225 | Are there any 2D Grid Range problems solvable in O(n2− ) time, for some > 0, but require Ω(n3/2−o(1) ) time? | The target classifies the total complexity of sequences of two-dimensional range updates and queries, a non-graph dynamic maintenance problem. |
| TCS-3669 | We leave open the questions of whether the runs of a string (or other information sufficient for answering 2-Period Queries in Õ(1) time) can be […] | Maintain string runs or an equivalent query structure under edits while supporting fast 2-Period queries. |
| TCS-6930 | Develop efficient repetitive indexes supporting arbitrary text modifications, beyond appending/prepending and the restricted practical performance of existing constructions. | Maintain repetitive text indexes under arbitrary modifications rather than only appending or prepending. |
| TCS-2324 | Can membership in all context-free languages be maintained under changes of non-constant size? | Maintain context-free language membership under batches of string changes using first-order updates and auxiliary relations. |
| TCS-3331 | Can ParityExists be maintained with first-order updates rules? | Maintain the ParityExists query using first-order update rules; dynamic maintainability is the precise target. |
| TCS-4307 | It remains open whether the answer relation of ECRPQs can be maintained on general graphs, even when only insertions are allowed. | Maintain extended conjunctive regular path-query answers on changing graphs, including the insertion-only case. |

## Boundaries and focus

The scope includes maintained answers after changing inputs in matroids, geometry,
text indexes, range queries, first-order dynamic programs and optimization. General
heap/BST analysis, locality, streaming space and online competitiveness retain their
specialist homes. A static question does not move because its source uses dynamic
programming or an inverse-maintenance technique. Biological rearrangement distances,
dynamical systems and dynamic logic likewise have different targets.

The Top 100 pair remains deterministic connectivity (TCS-6625) and near-optimal
matching (TCS-6627), with saved scores 97 and 95. The transferred records retain
their scores (at most 70) and evidence levels. No focus choice is displaced.

## Verification

The migration preserves statements, references, evidence, status, importance scores,
stable IDs, original subjects and archived records. Verification
checks the exact 18 transfers, counts, quotas, focus membership and CSV label.
Browser validation checks the filter, card labels,
downloads, Top 100/1000, mobile and offline display.

## Concurrent user exclusion

After the category scan, another user-authorized edit excluded TCS-0474 and removed
it from the ADS focus choices. That exclusion is preserved. Sorting X+Y (TCS-0388)
fills the vacated fifth ADS place, retaining its original score and draft evidence.
The category decisions above describe the baseline screening; the later exclusion
is recorded separately in concurrent-exclusion.json.
The final active count is 2,746. This independent change does not alter the 18
dynamic transfers or the dynamic focus pair.
