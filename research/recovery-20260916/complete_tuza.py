"""Complete Tuza's sharp integral inequality under the current barrier policy."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7252';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the 17 September 2026 MANIFEST/RULES preference for exact sharp conjectures: restored Tuza’s original factor-two proposition instead of the earlier numerical supremum reformulation.',
 'Kept finite simple undirected graphs, integral edge transversals and integral edge-disjoint triangle packings; shared vertices are allowed.',
 'Included empty and triangle-free graphs without a ratio or zero denominator, and required an unconditional all-graph theorem or a finite counterexample with certified optima.',
 'No numerical acceptance tolerance applies to this yes/no proposition, and neither an arbitrary positive improvement on the current general bound nor asymptotic additive losses settle it.',
 'Completed the 2025 dense-paper bibliography, corrected the Garden access year to its actual 2013 posting date, and checked the August and September 2026 preprints.',
 'Preserved importance 93, category and existing admission metadata; no unrelated archive was reviewed.',
]
sources=[
 'Read Open Problem Garden, Triangle-packing vs triangle edge-transversal, posted by fhavet on 6 March 2013, accessed 17 September 2026: the proposition is deletion of at most 2k edges when no packing has more than k edge-disjoint triangles. Its bibliography identifies Tuza’s 1990 paper as an original appearance.',
 'Read Chahua–Gutiérrez, On Tuza’s conjecture in dense graphs, publisher abstract and Introduction/Conjecture 1, plus the authors’ UTEC repository metadata. Discrete Applied Mathematics 377, 31 December 2025, pp. 225–233. The paper addresses dense split and tripartite graphs and complete four-partite graphs, retaining the unrestricted question.',
 'Read Gupta, arXiv:2608.06538v1, 6 August 2026, primary abstract. It claims the maximum-degree-seven case, using a catalogue of 1,144 machine-checked local certificates. This review did not run those verifiers or independently validate the proof, and the graph-class restriction remains material.',
 'Read Wang, arXiv:2609.13831v1, 12 September 2026, abstract, Introduction and Theorem 1 p. 1, and the proof description p. 2. It states the general factor 165/59, improving the long-standing 66/23 bound and later intermediate work. The manuscript says a Lean 4/Mathlib formalization is supplied; this review did not check that repository or execute its proof. Even the stated theorem leaves a factor strictly above two.',
 f'Bounded searches through {DATE} found no verified proof or counterexample for the exact unrestricted factor-two inequality. The new partial bound does not decide the target. Mathematical claims with other Tuza-labelled hypergraph or weak-saturation targets were not conflated with triangle packing and edge covering.',
]
complete(identifier,dict(
 title='Tuza’s triangle packing–covering conjecture',criterion='tightness',question_type='yes_no',
 formal=r'''Is it true that every finite simple undirected graph \(G\) satisfies
\[
 \tau_{\triangle}(G)\le 2\nu_{\triangle}(G),
\]
where \(\tau_{\triangle}(G)\) is the minimum number of edges meeting every triangle of \(G\), and \(\nu_{\triangle}(G)\) is the maximum number of pairwise edge-disjoint triangles?''',
 definitions=r'''A graph is a pair \(G=(V,E)\), where \(V\) is a finite set and \(E\) is a set of unordered two-element subsets of \(V\). Thus there are no loops, parallel edges, directions or weights. No bound on degree, density or chromatic number is imposed. Disconnected graphs and isolated vertices are allowed, as is the empty graph.

A triangle is a three-element vertex subset \(T\subseteq V\) for which all three two-element subsets are edges. Write \(E(T)\) for these three edges and \(\mathcal T(G)\) for the finite set of triangles. A triangle edge transversal is a subset \(F\subseteq E\) such that \(F\cap E(T)\ne\varnothing\) for every \(T\in\mathcal T(G)\). Equivalently, the graph \((V,E\setminus F)\) has no triangle. Define
\[
 \tau_{\triangle}(G)=
 \min\{|F|:F\subseteq E,\ F\cap E(T)\ne\varnothing
                  \text{ for all }T\in\mathcal T(G)\}.
\]
This is an edge-deletion number, not the number of vertices needed to meet the triangles.

A triangle packing is a subfamily \(\mathcal P\subseteq\mathcal T(G)\) such that \(E(T)\cap E(T')=\varnothing\) whenever \(T,T'\in\mathcal P\) are distinct. Define
\[
 \nu_{\triangle}(G)=\max\{|\mathcal P|:
       \mathcal P\text{ is a triangle packing in }G\}.
\]
Packed triangles may share vertices; they may not share edges. Both extrema exist because the graph is finite: the full edge set is a transversal and the empty family is a packing. Both numbers equal zero when the graph is triangle-free, including the empty graph. The conjectured inequality therefore includes these cases without dividing by zero.

All choices are integral: a transversal is an actual edge set, and each packed triangle is selected or not selected. Fractional weights, fractional linear-programming relaxations, vertex-disjoint packings and packings of longer cycles are different quantities. The statement concerns existence of the edge sets and their optimum cardinalities; it imposes no algorithmic time bound and does not ask for an efficient procedure to compute either optimum.

The factor two is exact and independent of the graph. No additive term, asymptotic error, exception for small graphs or restriction to a special graph family is allowed. The complete graph on four vertices has packing number one and transversal number two, so two is the candidate sharp universal factor. This is a prove-or-refute proposition, not a request for an approximation to the supremum of the ratios.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the inequality for all finite simple undirected graphs, or a complete Lean-checked refutation by a finite simple graph \(G\) with
\[
 \tau_{\triangle}(G)>2\nu_{\triangle}(G).
\]
For a counterexample, certify the necessary extremal bounds: for example, exhibit an integer \(k\ge0\), prove that every triangle packing has at most \(k\) members, and prove that every set of at most \(2k\) edges misses some triangle. A proposed graph together with an unverified solver output is insufficient. Exact values of both optima with the strict inequality also qualify.

The binary target has no \(1/100\) tolerance. A factor \(2+\varepsilon\), a numerical estimate of the optimal universal ratio, a vanishing additive loss, a fractional analogue or a proof only for bounded-degree, dense or other special graphs does not prove the conjecture. An improved upper bound that remains strictly above two is progress, not a resolution. Conditional statements under unproved assumptions do not unconditionally decide the target.''',
 source_formulation=dict(text='If a graph has at most k pairwise edge-disjoint triangles, Tuza asks whether deleting at most 2k edges always destroys every triangle. Taking k to be the maximum packing size gives the displayed inequality.',caption='Paraphrase of the Open Problem Garden statement posted 6 March 2013; the exact conjecture is also Conjecture 1 in Chahua–Gutiérrez (2025).',citation='question',format='editorial_paraphrase'),
 references=[
 ref('question','Triangle-packing vs triangle edge-transversal','Frédéric Havet (contributor); conjecture of Zsolt Tuza',2013,'https://www.openproblemgarden.org/op/triangle_packing_vs_triangle_edge_transversal','Posted 6 March 2013; conjecture and bibliography; accessed 17 September 2026'),
 ref('dense','On Tuza’s conjecture in dense graphs','Luis Chahua; Juan Gutiérrez',2025,'https://doi.org/10.1016/j.dam.2025.06.049','Discrete Applied Mathematics 377, 31 December 2025, pp. 225–233; abstract, Introduction and Conjecture 1'),
 ref('degree',"Tuza's conjecture for graphs of maximum degree at most seven",'Anish Gupta',2026,'https://arxiv.org/abs/2608.06538v1','6 August 2026; abstract, maximum-degree restriction and computer-checked-certificate claim; certificates not independently checked'),
 ref('recent',"A Bound Below 2.8 for Tuza's Conjecture",'Sichen Wang',2026,'https://arxiv.org/abs/2609.13831v1','12 September 2026; abstract, Introduction and Theorem 1 p. 1; Lean-formalization claim p. 2, not independently executed'),
 ],
 why='The conjecture asks whether the cost of destroying every triangle is always at most twice the largest edge-disjoint triangle packing, the exact factor already forced by a small complete graph.',
 context_blocks=[
 block('Packing and covering measure different ways of handling triangles: a packing collects obstructions that share no edge, whereas a transversal removes all obstructions at once. Tuza’s conjecture proposes an exact universal comparison.','question'),
 block('The factor cannot be smaller than two because of the complete graph on four vertices. The current formulation therefore retains the sharp conjecture itself, following the project’s rule for exact threshold propositions.','dense'),
 block('The dense-graph paper establishes selected split, tripartite and complete four-partite cases while retaining the unrestricted conjecture.','dense'),
 block('The August 2026 preprint claims the maximum-degree-seven case and reports a finite catalogue of checked local certificates. That catalogue has not been independently run in this review, and the degree restriction remains.','degree'),
 block(r'The September 2026 preprint states \(\tau_{\triangle}(G)\le(165/59)\nu_{\triangle}(G)\) for all finite simple graphs. This improves the earlier general factor but remains above two. Its claim of a Lean formalization is recorded without treating it as an independently checked benchmark proof.','recent'),
 ],
 progress=[progress('2013-03-06','The Garden records the exact factor-two conjecture.','question'),progress('2025-12-31','The dense-graph paper proves several special cases.','dense'),progress('2026-08-06','A preprint claims the maximum-degree-seven case, using machine-checked local certificates.','degree'),progress('2026-09-12','A new preprint states the improved universal factor 165/59 and reports a Lean formalization; the factor-two conjecture remains beyond this bound.','recent')],
 quantitative_review=dict(reviewed_on=DATE,disposition='sharp_binary_conjecture',reason='Applied the 17 September 2026 MANIFEST/RULES preference for sharp conjectures; replaced the earlier numerical ratio reformulation by Tuza’s exact original factor-two statement.',status_scope='Individual source and formulation review; recent partial-result proofs were not independently checked.'),
),notes,sources,'The unrestricted exact factor-two conjecture remains source-open in the bounded check through 17 September 2026. The 12 September preprint states a general factor 165/59, still strictly above two; the August result is restricted to maximum degree seven. Neither manuscript’s full proof or formal certificate was independently verified in this review.',summary=[
 'A triangle packing is a collection of triangles sharing no edges, although they may share vertices.',
 'A triangle edge transversal is a set of edges whose deletion destroys every triangle.',
 'Tuza’s conjecture says that the minimum transversal has size at most twice the maximum packing in every finite simple undirected graph.',
 'The factor two is sharp already for the complete graph on four vertices.',
 'The target requires a complete Lean-checked proof or counterexample to this exact inequality, with no numerical tolerance.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
