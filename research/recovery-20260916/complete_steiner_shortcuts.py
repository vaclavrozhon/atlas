"""Complete the unrestricted structural Steiner Shortcut Conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7342';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved Conjecture 2 as a structural existence statement with near-linear added arcs and polylogarithmic original-pair distance.',
 'Expanded the absolute quantifiers, finite augmentation, exact reachability preservation and unrestricted chains of Steiner vertices.',
 'Retained the harmless no-isolated-original-vertices convention and clarified why no independent Steiner-vertex budget is needed.',
 'Distinguished the old conjecture, bounded-thickness lower bounds and parallel construction requirements from the unrestricted target.',
 'Made explicit that a negative answer must defeat every proposed common choice of constants, not one numerical budget.',
 'Preserved importance 91 and category, and required a complete Lean-checked proof of either direction.',
]
sources=[
 'Read Bernstein–Fleischmann–Probst Gutenberg–Haeupler–Hoppenworth–Jiang–Li–Pettie–Saranurak–Schiller, arXiv:2510.24954v2, 30 October 2025: Introduction pp. 1–4, Conjecture 2 p. 2, Definition 1.2 and Theorem 1.3 pp. 2–3, and the discussion separating structural existence from parallel construction. The source explicitly leaves unrestricted Steiner shortcuts open. Its diameter condition in Conjecture 2 applies to reachable pairs of original vertices.',
 'Checked the live arXiv submission history: v2 of 30 October 2025 remains the latest listed version on 17 September 2026. Also read the official STOC 2026 publication abstract, DOI 10.1145/3798129.3800781, published 9 June 2026; it retains the distinction between unrestricted Steiner vertices and the restricted-thickness lower bound.',
 'The historical Hesse refutation and the failures of known old-vertex lower-bound constructions under Steiner augmentation are recorded through the directly read 2025/2026 primary paper. No independent full proof audit of Hesse’s original construction or of the new lower bounds is claimed.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of Conjecture 2. Other uses of Steiner vertices for shortest paths, Steiner point removal, and approximation algorithms for shortcut optimization were distinguished from the structural universal statement.',
]
complete(identifier,dict(
 title='Steiner Shortcut Conjecture',criterion='construction',question_type='yes_no',
 formal=r'''Do there exist an absolute real constant \(C>0\) and integers \(a,b\ge0\) such that every finite simple directed graph \(G=(V,E)\) with \(n=|V|\ge2\), \(m=|E|\ge1\) and no isolated vertices admits finite sets of new vertices \(W\) and new arcs \(F\) satisfying all of the following?
\[
 W\cap V=\varnothing,\qquad
 H=(V\cup W,E\cup F),\qquad
 |F|\le C m\bigl(\log_2(n+2)\bigr)^a.
\]
For every ordered pair \(u,v\in V\), a directed path from \(u\) to \(v\) exists in \(H\) if and only if one exists in \(G\). Moreover, whenever such a path exists, \(H\) has a \(u\)-to-\(v\) path containing at most
\[
 C\bigl(\log_2(n+2)\bigr)^b
\]
arcs. There is no restriction on the number of consecutive new vertices along a path and no construction-time requirement.''',
 definitions=r'''A finite simple directed graph has an arc set of ordered pairs of distinct vertices, without repeated arcs. Both opposite arcs may be present. Graphs are unweighted; a path's length is its number of arcs. A directed path follows the arc directions, and reachability permits the empty path, so every vertex reaches itself. An isolated vertex has neither an incoming nor an outgoing arc.

The vertices in \(W\) are called Steiner vertices. The new arcs \(F\) have endpoints in \(V\cup W\), are disjoint from \(E\), and keep \(H\) a simple directed graph. They may join two original vertices, an original and a Steiner vertex, or two Steiner vertices. All original vertices and arcs remain present. The augmentation may create cycles, but it may not create any previously absent reachability between original vertices, even through a sequence of Steiner vertices.

The distance bound concerns only ordered pairs in \(V\times V\) that were reachable in \(G\). It does not constrain distances for pairs having a Steiner endpoint or require originally unreachable pairs to become reachable. For each reachable pair, existence of one sufficiently short path suffices; other paths may be longer. All new arcs count toward \(|F|\), including arcs between Steiner vertices. Their number, rather than their encoding length, is the size measure.

No separate bound on \(|W|\) is imposed. Isolated Steiner vertices can be discarded, and every remaining Steiner vertex is incident to at least one new arc, giving \(|W|\le2|F|\). Original isolated vertices are omitted only to make \(n\le2m\); they can be restored without new arcs, and their only reachable original pair is their own diagonal pair. Thus they do not change the structural issue. The logarithmic bounds use the original \(n\), not the size of the augmented graph.

The constants \(C,a,b\) are chosen once before the graph. The sets \(W,F\) may depend on the entire graph, but the bounds must hold with those common constants for every allowed graph. This is a pure existence statement: no uniform algorithm, polynomial running time, parallel work bound, depth bound for construction or computable choice procedure is required. The bound on path length is a property of the resulting graph, not a time bound for constructing it.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the stated existence of common constants and augmentations, or a complete Lean-checked proof of its logical negation.

A positive answer must preserve the complete original reachability relation and satisfy both bounds for every graph, with unrestricted Steiner paths allowed. A negative answer must show that every proposed choice of \(C,a,b\) fails on some finite graph even when arbitrary finite Steiner augmentations are permitted. A lower bound forbidding Steiner vertices, limiting their consecutive occurrence, or considering only a smaller arc budget does not suffice. Refuting one fixed numerical choice of constants is not a refutation of their existence. No computational hypothesis or numerical approximation tolerance is part of acceptance.''',
 source_formulation=dict(text='Conjecture 2 permits new Steiner vertices and near-linearly many additional arcs while preserving the original transitive closure and reducing all finite distances between original vertices to a polylogarithm.',caption='Paraphrase of the Steiner Shortcut Conjecture, Conjecture 2, printed p. 2 of arXiv:2510.24954v2; STOC 2026 publication.',citation='primary',format='editorial_paraphrase'),
 why='Determine whether a directed reachability relation always has a compact augmentation with short witnessing paths. The structural answer would clarify an obstacle behind fast parallel graph algorithms, while efficient construction remains a separate requirement.',
 references=[
 ref('primary',"Reviving Thorup's Shortcut Conjecture",'Aaron Bernstein; Henry Fleischmann; Maximilian Probst Gutenberg; Bernhard Haeupler; Gary Hoppenworth; Yonggang Jiang; George Z. Li; Seth Pettie; Thatchaphol Saranurak; Leon Schiller',2025,'https://arxiv.org/abs/2510.24954v2','30 October 2025 version; Conjecture 2 p. 2, Definition 1.2 and Theorem 1.3 pp. 2–3, parallel-construction distinction pp. 3–4'),
 ref('published',"Reviving Thorup’s Shortcut Conjecture",'Aaron Bernstein; Henry Fleischmann; Maximilian Probst Gutenberg; Bernhard Haeupler; Gary Hoppenworth; Yonggang Jiang; George Z. Li; Seth Pettie; Thatchaphol Saranurak; Leon Schiller',2026,'https://doi.org/10.1145/3798129.3800781','STOC 2026, published 9 June 2026; primary abstract, unrestricted Steiner versus bounded-thickness scope'),
 ],
 context_blocks=[
 block('A directed path can encode a long chain of dependencies. Shortcuts aim to shorten witnesses of reachability without introducing a dependency that was absent from the original graph.'),
 block('Thorup’s original version allowed new arcs only between original vertices and was refuted. The present conjecture changes the representation by permitting new vertices, so the historical counterexamples require a further argument.'),
 block('The source shows that the known old-vertex lower-bound constructions can be efficiently shortcut when Steiner vertices are allowed. It nevertheless leaves the universal Steiner conjecture open.'),
 block('The negative result rules out certain augmentations in which every path has only a short run of consecutive Steiner vertices. This card imposes no such restriction, so that theorem does not refute its target.','published'),
 block('Existence of the augmentation and efficient construction of it are different assertions. Parallel algorithmic applications need a construction procedure with suitable work and depth in addition to the structural property.'),
 ],
 progress=[progress('2003','Hesse refutes the original conjecture without Steiner vertices, as documented in the later primary paper.'),progress('2025-10-30','The revised conjecture explicitly allows unrestricted Steiner vertices; restricted-thickness lower bounds leave it open.'),progress('2026-06-09','The STOC publication retains the distinction between the unrestricted conjecture and the restricted lower bound.','published')],
),notes,sources,'Conjecture 2 is explicitly open in the latest listed October 2025 version, and the June 2026 publication retains its unrestricted Steiner scope. Bounded primary-source checks through 17 September 2026 found no verified resolution. The historical and restricted-thickness lower bounds do not refute the precise statement here; their complete proofs were not independently audited.',summary=[
 'A directed graph may be augmented with new arcs and new Steiner vertices.',
 'Reachability between every pair of original vertices must remain exactly unchanged.',
 'The target permits near-linearly many new arcs and requires polylogarithmic paths for every reachable original pair.',
 'The earlier refutation and newer lower bounds impose restrictions absent from this conjecture.',
 'A complete Lean-checked answer concerns universal structural existence, without requiring a fast construction algorithm.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
