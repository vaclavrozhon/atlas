"""Review worst-case logarithmic dynamic planar extreme-point queries."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7326';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the exact deterministic fully dynamic extreme-point interface, linear space and logarithmic worst-case time for each operation.',
 'Specified current-size accounting, empty sets, arbitrary degeneracies, stable deletion handles and online quantifiers.',
 'Made real-arithmetic and storage costs explicit and ruled out hidden uncharged rebuilding or a free copy of deleted input.',
 'Distinguished querying an implicit hull from explicitly reporting all changed hull vertices.',
 'Read the original full-version theorem, model and open-problems section and checked the 2026 engineering paper’s guarantees.',
 'Kept amortized algorithms and restricted geometric update orders separate from this unrestricted worst-case target.',
 'Preserved importance and required a complete Lean-checked binary answer without treating existing amortized optimality as a resolution.',
]
sources=[
 'Read Jacob–Brodal, Dynamic Planar Convex Hull, arXiv:1902.11169v1, 28 February 2019, author PDF https://cs.au.dk/~gerth/papers/arxiv1902.11169.pdf: abstract, Theorems 1–2 p.2, Sections 2.1–2.2 pp.5–6 and Section 12 p.81. The upper bound has logarithmic amortized updates, logarithmic queries and linear space. The lower bound is in the algebraic real-RAM setting. Section 12 explicitly leaves worst-case logarithmic updates with fast extreme-point queries open. The full version states that the main results appeared at FOCS 2002; 2019 is the full-version date, not the date of the original breakthrough.',
 'Read van der Hoog–Reinstädtler–Rotenberg, Engineering Fully Dynamic Convex Hulls, SEA 2026 article 22, DOI 10.4230/LIPIcs.SEA.2026.22, published 15 June 2026: full primary HTML abstract and Introduction. The implemented structure has O(log n log log n) amortized updates and O(log^2 n) query time. The introduction distinguishes explicit from implicit hulls, continues to cite the classical amortized optimum, and separates simple-path and ordered-update restrictions. These guarantees do not settle the selected worst-case target.',
 'Bounded primary-source searches through 17 September 2026 found no verified resolution. Results for insertion-only, deletion-only, simple-path or ordered deque updates and practical empirical performance were not treated as unrestricted worst-case logarithmic updates.',
]
complete(identifier,dict(
 formal=r'''Does there exist one uniform deterministic data structure and an absolute constant \(K\ge1\) that maintain a finite set \(P\subset\mathbb R^2\), initially empty, with the following guarantees on every finite valid online sequence? Each point insertion, point deletion and extreme-point query takes at most \(K\log_2(n+2)\) worst-case real-RAM steps, where \(n\) is the larger set size immediately before and after that operation. The stored representation uses at most \(K(1+|P|)\) cells. Given any \(u\in\mathbb R^2\setminus\{0\}\), an extreme-point query returns a point \(p\in P\) maximizing \(\langle u,p\rangle\), or an empty marker if \(P=\varnothing\).''',
 definitions=r'''Insert receives the two exact real coordinates of a point not currently in \(P\), adds it and returns a stable handle. Delete receives a valid handle for a currently present point and removes that point; the handle then becomes invalid. A previously deleted coordinate pair may be inserted again with a new handle. A handle is only a reference to an item, not an encoding of free auxiliary information. Each live handle must remain usable until its item is deleted, including across internal restructuring.

For \(u=(u_x,u_y)\) and \(p=(p_x,p_y)\), the objective is \(\langle u,p\rangle=u_xp_x+u_yp_y\). Any maximizing point is acceptable, chosen deterministically by the algorithm. All finite sets are allowed: no general-position, distinct-x-coordinate, noncollinearity, convex-position or bounded-coordinate promise is made. Updates may occur in arbitrary order. A query returns only one point or an empty marker, not a cyclic list of the entire convex hull, its edges, or all changes caused by an update.

Use an algebraic real RAM with a fixed finite program. A cell stores an exact real scalar, a pointer or a constant-size control value. Copying a cell, reading or writing an addressed cell, following or changing a pointer, comparison, branching, exact real addition, subtraction, multiplication and division by a nonzero value each cost one step. Allocating or releasing a constant-size record also costs one step. The program contains only fixed rational numerical constants and uses ordinary discrete address bookkeeping; a real coordinate is not an address encoding. No floor, bit extraction from a real, arbitrary-precision packing primitive, unbounded parallel operation, randomness, advice or oracle is supplied. There is no charge for coordinate bit length: these are exact real-arithmetic costs, not rational-input bit complexity.

All stored points, handles, indexes, auxiliary records and retained historical information count toward space. All comparisons, rebuilding, initialization and query work count toward time. Initialization on the empty set takes constant time and space. Between operations at most \(K(1+|P|)\) cells are retained; during an operation at most \(K(1+n)\) cells, including its workspace, are used, after enlarging the same universal constant if necessary. The client holds input coordinates and handles but supplies no uncharged index or preprocessing. Deleted data may be retained only within the current space bound.

The algorithm must finish each operation and return its answer before seeing the next. It has no advance knowledge of the sequence length, future operations, maximum eventual set size or coordinate values. The one program and constant \(K\) work for every sequence and every direction. Both time and space are measured against current size; an occasional expensive update cannot be paid for by averaging over other operations. Reading two input coordinates or returning one stored point takes constant work.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive proof must establish exact answers, linear total storage and a logarithmic bound for every individual insertion, deletion and query, with all rebuilding and workspace charged. A negative proof must rule out all data structures in the stated model unconditionally; a conditional lower bound is only a conditional result.

Logarithmic amortized updates, expected bounds, ordered or one-sided update restrictions, and data structures requiring superlinear storage do not meet the full target. An argument that explicitly reporting a changed hull can have linear output size does not refute this one-point query interface.''',
 source_formulation=dict(text='The full version leaves open whether logarithmic worst-case update time can coexist with fast extreme-point queries. This card retains the precise extreme-point-only interface, linear-space budget and deterministic exact real-arithmetic conventions already selected for that question.',caption='Jacob–Brodal, Dynamic Planar Convex Hull, full version of 28 February 2019, §12, p.81; main amortized result originally published at FOCS 2002.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Dynamic Planar Convex Hull','Riko Jacob; Gerth Stølting Brodal',2019,'https://arxiv.org/abs/1902.11169v1','28 February 2019 full version of FOCS 2002 results; Theorems 1–2 p.2, §§2.1–2.2 pp.5–6 and §12 p.81'),
 ref('engineering','Engineering Fully Dynamic Convex Hulls','Ivor van der Hoog; Henrik Reinstädtler; Eva Rotenberg',2026,'https://doi.org/10.4230/LIPIcs.SEA.2026.22','Published 15 June 2026; abstract and Introduction, implicit versus explicit hulls and amortized update guarantees'),
 ],
 context_blocks=[
 block('The known linear-space structure achieves logarithmic amortized update time and logarithmic extreme-point queries. The unresolved distinction is whether every individual update can satisfy the logarithmic time bound.'),
 block('One update may change many hull vertices. A query interface avoids having to list those changes, so an output-size argument for explicitly reporting a hull is not a lower bound for this target.'),
 block('The 2026 engineering paper develops a practical fully dynamic implementation with amortized logarithmic-times-log-log updates and logarithmic-squared queries. Its performance guarantees address a different endpoint.','engineering'),
 block('The same recent discussion distinguishes general updates from simple-path and ordered-update settings. Bounds for those restricted settings do not by themselves give the unrestricted guarantee here.','engineering'),
 ],
 progress=[progress('2002','The conference result achieves linear space and logarithmic amortized updates with logarithmic extreme-point queries.'),progress('2019-02-28','The full version supplies the detailed analysis and explicitly retains worst-case logarithmic updates as an open question.'),progress('2026-06-15','A new implemented fully dynamic structure improves practical performance, with amortized update guarantees.','engineering')],
),notes,sources,'The 2019 full version explicitly leaves worst-case logarithmic updates open. The 2026 engineering paper has different amortized guarantees and does not settle this extreme-point target. Bounded primary-source checks through 17 September 2026 found no verified resolution; the review is not an independent audit of every geometric data-structure proof.',summary=[
 'Maintain an arbitrary changing set of exact points in the plane, starting from the empty set.',
 'Insertions and deletions may occur in any order, and a query asks for one point farthest in a supplied direction.',
 'The target is deterministic logarithmic worst-case time for each operation and linear total space.',
 'Known optimal amortized bounds and recent practical implementations do not provide that per-operation guarantee.',
 'The answer must be a complete Lean-checked construction or unconditional refutation in the specified real-arithmetic model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
