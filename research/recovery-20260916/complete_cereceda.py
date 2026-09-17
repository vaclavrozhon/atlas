"""Complete the approved minimum-palette quadratic recoloring conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6655'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the approved d+2-color target and allowed the quadratic constant to depend on the fixed degeneracy bound.',
 'Defined degeneracy, labeled proper colorings, one-vertex moves, path length and infinite distance, including the empty graph.',
 'Made the all-graphs/all-colorings quantifiers explicit and distinguished an existential diameter theorem from efficient path construction.',
 'Specified that a refutation must defeat every quadratic constant at one fixed degeneracy, rather than only exceed a proposed numerical constant.',
 'Corrected the generic source metadata and checked the exact scope of the general polynomial and 2026 restricted-class linear results.',
 'Preserved the existing individually assessed importance 94.',
]
sources=[
 'Read Wang–Lu, arXiv:2509.15456v2 (4 November 2025), abstract and §1 pp. 1–4, Conjecture 1.1, Theorem 1.2, Corollary 1.3 and Table 1; §2 definition of degeneracy. Checked the inherited publisher page and Crossref metadata for Discrete Mathematics 349(7), 115055 (July 2026), DOI 10.1016/j.disc.2026.115055. Full journal text was unavailable; the full author preprint was used for the statement locators.',
 'Read Bousquet–Heinrich, arXiv:1903.05619v1 (13 March 2019), abstract and §1 pp. 1–4, Theorems 1–2, Conjecture 3 and stronger Question 4. The authors explicitly distinguish d-dependent from absolute quadratic constants; the approved card selects the former. Checked publication metadata: Journal of Combinatorial Theory, Series B 155:1–16 (July 2022), DOI 10.1016/j.jctb.2022.01.006.',
 f'Bounded primary-source searches through {DATE} found later recoloring results for special graph classes, list coloring, more colors and modular decompositions, without a resolution of the general d+2-color quadratic target. The publisher introduction of a later 2026 planar list-recoloring article also retains the general conjecture; its future issue date was not treated as a past publication date.',
 'Did not import the 2025 author preprint’s unrelated claim equating outerplanar graphs and treewidth at most two. Only the stated restricted-class recoloring bounds are used here; their full proofs were not independently certified.',
]
status='The checked sources distinguish the proved polynomial diameter bound from the unresolved quadratic conjecture. The July 2026 source treats a linear bound on chordal and bounded-treewidth graphs with more available colors, not arbitrary d-degenerate graphs with d+2 colors. No full resolution of the selected target was found in the bounded later-work search.'
complete(identifier,dict(
 criterion='tightness',question_type='yes_no',year=2026,
 formal=r'''For every fixed integer \(d\ge0\), does there exist an integer \(C_d\ge1\) such that every finite simple \(d\)-degenerate graph \(G\) on \(n\) vertices satisfies
\[
\operatorname{diam}\bigl(R_{d+2}(G)\bigr)\le C_d n^2?
\]
Here \(R_{d+2}(G)\) is the graph of proper colorings using the fixed palette \(\{1,\ldots,d+2\}\), with one move changing the color of exactly one vertex.

Equivalently, for every \(d\) there must be one \(C_d\) such that, for every \(n\ge0\), every such graph and every pair of its proper \((d+2)\)-colorings \(\alpha,\beta\), a sequence of at most \(C_d n^2\) valid single-vertex moves transforms \(\alpha\) into \(\beta\). The constant may depend on \(d\) and on nothing else.''',
 definitions=r'''The graph \(G=(V,E)\) has a finite vertex set \(V\) of cardinality \(n\), and an edge set of unordered pairs of distinct vertices. There are no loops, parallel edges, weights, prescribed colors or extra structural promises.

For an integer \(d\ge0\), the graph is \(d\)-degenerate if every nonempty subset \(U\subseteq V\) contains a vertex with at most \(d\) neighbors in \(U\). Equivalently, its vertices can be ordered so that each vertex has at most \(d\) neighbors appearing later in the order. This is an upper bound on degeneracy, not a requirement that it equal \(d\); the maximum degree may be much larger than \(d\). A graph on no vertices satisfies the condition.

For \(q=d+2\), a proper coloring is a function \(\alpha:V\to\{1,\ldots,q\}\) such that \(\alpha(u)\ne\alpha(v)\) for every edge \(\{u,v\}\). The palette has exactly \(q\) available labels, but a coloring need not use every label. Colorings are not identified under permutation of color labels.

The vertices of \(R_q(G)\) are all these proper colorings. Two distinct colorings \(\alpha,\beta\) are adjacent exactly when
\[
\bigl|\{v\in V:\alpha(v)\ne\beta(v)\}\bigr|=1.
\]
A recoloring path of length \(t\) is a sequence \(\gamma_0,\ldots,\gamma_t\) of proper colorings, with consecutive colorings adjacent. The graph and palette stay fixed throughout. Every intermediate coloring must be proper; there is no temporary extra color, uncolored vertex or simultaneous change at several vertices. Changing an entire color class or a connected set is not one move.

The distance between two colorings is the smallest such \(t\), or \(+\infty\) if there is no path. The diameter is the maximum of these distances over all pairs. A \(d\)-degenerate graph has a proper \((d+1)\)-coloring and hence the set of \(q\)-colorings is nonempty. For \(n=0\) there is one empty coloring and diameter zero.

The order of quantifiers is \(\forall d\,\exists C_d\,\forall n\,\forall G\,\forall\alpha,\beta\). In particular, this card does not require one absolute constant working for all \(d\), nor a computable rule producing \(C_d\) from \(d\). It asks for existence of short paths, without a separate running-time requirement for finding them. The chosen palette is \(d+2\); a bound that uses more colors does not meet this target.

Although each finite distance is an integer, the question is the asymptotic quadratic upper-bound proposition. It does not request a numerical approximation to the diameter of one graph, so absolute \(1/100\) tolerance does not change the path-length bound or the quadratic exponent.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the displayed all-degeneracies quadratic bound, with the full graph and coloring quantifiers; or supply a complete Lean-checked proof of its negation. A negative answer must give one fixed \(d\) for which every proposed constant \(C\) fails on some graph and pair of colorings. A disconnected recoloring graph would also refute the bound, but merely finding a finite distance larger than one chosen \(C n^2\) does not rule out a larger \(C_d\). A polynomial upper bound with exponent greater than two, a bound for a proper graph class or a result allowing additional colors is insufficient.''',
 source_formulation=dict(
 text='The source recalls Cereceda’s proposed quadratic diameter bound once a d-degenerate graph has at least d+2 available colors. The approved card fixes the threshold palette d+2 and permits the constant to depend on d, as in the explicitly distinguished weaker formulation in Bousquet and Heinrich.',
 caption='Paraphrase of Wang–Lu, Conjecture 1.1, with the approved palette and constant convention; compare Bousquet–Heinrich, Conjecture 3 and stronger Question 4.',
 citation='primary',format='editorial_paraphrase'),
 why='A coloring may need to change while every intermediate assignment remains valid. Cereceda’s conjecture asks whether one extra color beyond the greedy guarantee always permits a quadratic-length transition, even when local degrees are large. It is a central test of how sparsity controls the geometry of a solution space, beyond merely ensuring that all solutions are connected.',
 references=[
 ref('primary','Linear recoloring diameter of degenerate chordal graphs and bounded treewidth graphs',
  'Yichen Wang; Mei Lu',2026,'https://doi.org/10.1016/j.disc.2026.115055',
  'Discrete Mathematics 349(7), 115055 (July 2026); checked arXiv:2509.15456v2, 4 November 2025, §1 Conjecture 1.1, Theorem 1.2, Corollary 1.3 and Table 1, pp. 2–4'),
 ref('polynomial','A polynomial version of Cereceda’s conjecture',
  'Nicolas Bousquet; Marc Heinrich',2022,'https://doi.org/10.1016/j.jctb.2022.01.006',
  'Journal of Combinatorial Theory, Series B 155:1–16 (July 2022); checked arXiv:1903.05619v1, 13 March 2019, §1 Theorems 1–2, Conjecture 3 and Question 4, pp. 3–4'),
 ],
 context_blocks=[
 block('Connectivity of the recoloring graph at this palette size is already known. The unresolved issue is a uniform quadratic upper bound on the lengths of the shortest connecting paths.'),
 block(r'Bousquet and Heinrich prove an \(O_d(n^{d+1})\) upper bound at the threshold palette. Their general quadratic result applies when the palette size is at least \(3(d+1)/2\). The first result proves polynomial diameter for fixed \(d\), but its exponent is not the requested two.','polynomial'),
 block('Bousquet and Heinrich explicitly distinguish a constant depending on degeneracy from one absolute constant for every degeneracy. This card retains the former convention rather than silently strengthening the conjecture.','polynomial'),
 block(r'The 2026 source obtains linear diameter for \(d\)-degenerate chordal graphs with at least \(2d+1\) colors, and for graphs of treewidth at most \(k\) with at least \(2k+1\) colors. Chordal means every cycle of length at least four has a chord. These structural restrictions and palette thresholds leave the general target unchanged.'),
 ],
 progress=[
 progress('2019-03-13','The general polynomial bound appears in the checked preprint, together with the explicit remaining quadratic conjecture.','polynomial'),
 progress('2022-07','The polynomial result is published in Journal of Combinatorial Theory, Series B.','polynomial'),
 progress('2026-07','The inherited source publishes stronger linear bounds for restricted graph classes and larger palettes.'),
 progress(DATE,'The review fixes the threshold palette, d-dependent constant and exact single-vertex move semantics; no general quadratic resolution is found.'),
 ],
),notes,sources,status,summary=[
 'A proper graph coloring can be changed one vertex at a time while remaining proper after every step.',
 'Cereceda’s conjecture asks whether any two colorings of a d-degenerate n-vertex graph can be connected in at most C_d n squared steps using d+2 available colors.',
 'The constant may depend on d, but not on the graph, its size or the chosen colorings.',
 'A general polynomial bound is known, but its exponent can exceed two.',
 'Recent linear bounds use special graph classes or more colors and do not settle this threshold-palette target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
