"""Restore the edge operation in the perfect-graph modification question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7027'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered edge deletion, rather than vertex deletion, from the survey conventions and the original authors’ explicit concluding question.',
 'Defined perfectness through every induced subgraph, including empty graphs, and specified the unweighted edge budget as the sole parameter.',
 'Expanded FPT into one uniform deterministic machine, a total computable parameter function and a polynomial input-length exponent independent of the budget.',
 'Separated the known vertex-deletion hardness, equivalence with edge completion, and algorithms for proper subclasses of perfect graphs.',
 'Assessed importance individually from the broad graph-modification boundary, rather than retaining the provisional score.',
]
sources=[
 'Read the 2020 edge-modification survey, §1 conventions and §2.2, printed/PDF p. 13, Open Problem 2.17. Read the published 2023 Computer Science Review version, §1 and §2.2, printed/PDF p. 8, same numbered question. Deletion means edge deletion throughout this source.',
 'Read Heggernes–van ’t Hof–Jansen–Kratsch–Villanger, author manuscript dated 11 November 2011, abstract, §1, §2 perfect-graph definition and conclusion p. 12. The conclusion explicitly leaves Perfect Edge Deletion/Completion open after proving hardness of vertex deletion. Checked publisher metadata for the 2013 journal version: Theoretical Computer Science 511:172–180, 4 November 2013, DOI 10.1016/j.tcs.2012.03.013. The institutional journal PDF was not downloadable; the full author manuscript was read instead.',
 'Checked Jansen–Verhaegh, Journal of Computer and System Sciences 156 (March 2026), 103730, publisher abstract and accessible introduction. Its discussion of Perfect Deletion concerns essential vertices and explicitly uses vertex deletions, not the present edge operation; no full proof verification was needed for this scope distinction.',
 f'Bounded primary-source searches through {DATE} found no FPT algorithm or parameterized-hardness resolution of unrestricted Perfect Edge Deletion. Results for trivially perfect graphs, supplied vertex sets, other structural parameters and essential-vertex detection do not settle this target.',
]
status='The published 2023 survey explicitly leaves Perfect Edge Deletion open, and no later resolution was found in the bounded review. The older W[2]-hardness theorem concerns deleting vertices; 2026 essential-vertex work also concerns that different operation. The card preserves the unrestricted edge-deletion question, rather than interpreting the ambiguous short name as a resolved vertex problem.'
complete(identifier,dict(
 title='Fixed-parameter tractability of Perfect Edge Deletion',
 criterion='resources',question_type='yes_no',
 formal=r'''Is Perfect Edge Deletion fixed-parameter tractable when the only parameter is the number of edges allowed to be deleted?

Precisely, do there exist one uniform deterministic algorithm \(A\), an integer \(c\ge1\), and a total computable function \(f:\mathbb N\to\mathbb N_{\ge1}\) such that, for every input \((G,k)\) of bit length \(L\), \(A\) decides within \(f(k)(L+1)^c\) steps whether there is a set \(S\subseteq E(G)\) satisfying
\[
|S|\le k
\quad\text{and}\quad
(V(G),E(G)\setminus S)\text{ is perfect}?
\]
The exponent \(c\) is independent of \(k\), and the same program and function must work on every input graph.''',
 definitions=r'''The graph \(G=([n],E)\) is finite, simple, undirected and unweighted, with \(n\ge0\). Thus \(E\) is a set of unordered pairs of distinct vertices, with no loops or parallel copies. The budget \(k\ge0\) is an integer. There is no promise on connectedness, degree, planarity, treewidth, clique number or an already supplied modification set.

For any finite graph \(H\), its clique number \(\omega(H)\) is the largest cardinality of a set of pairwise adjacent vertices. Its chromatic number \(\chi(H)\) is the smallest nonnegative integer \(r\) for which the vertices can be assigned colors from \(\{1,\ldots,r\}\) with adjacent vertices receiving different colors. For the empty graph, both numbers are zero.

For \(U\subseteq V(H)\), the induced subgraph \(H[U]\) keeps exactly the edges of \(H\) whose two endpoints lie in \(U\). The graph \(H\) is perfect when
\[
\forall U\subseteq V(H),\qquad \chi(H[U])=\omega(H[U]).
\]
Equality only on \(H\) itself is not sufficient. This definition specifies the graph property, without assuming access to an oracle for recognition or coloring.

The allowed operation deletes an existing edge and keeps all vertices. The decision is YES if some set of at most \(k\) such deletions yields a perfect graph. It is not necessary to output the deletion set. Vertex deletion, edge insertion and unrestricted edge editing are different operations. A budget at least \(|E|\) always gives a YES instance because an edgeless graph is perfect; budget zero asks whether the input graph is already perfect.

Encode \(G\) by \(1^n0\), followed by the adjacency bits for \(1\le u<v\le n\) in lexicographic order. Append a self-delimiting code for \(k\): if \(b\) is the bit length of \(k+1\), the code is \(1^b0\) followed by the \(b\)-bit ordinary binary representation of \(k+1\). No trailing bits are permitted. The complete bit length, including the budget, is \(L\).

Computation uses a deterministic multitape Turing machine with one fixed finite program, fixed finite tape alphabets, a read-only input tape and initially blank work tapes. Each transition accesses the cells under the heads and moves each head by at most one cell. All transitions, including parsing, preprocessing, arithmetic and output, are charged. There is no advice, randomness, oracle or uncharged preprocessing. Malformed strings must be rejected in polynomial time in their length.

The function \(f\) must have a finite algorithm that computes \(f(k)\) on every integer \(k\). Its growth may be arbitrarily fast; no single-exponential bound or polynomial kernel is requested. The running-time bound must hold on every valid input, with exact correctness on YES and NO instances. A family of unrelated algorithms for each fixed \(k\), or a bound such as \((L+1)^{g(k)}\) whose exponent grows with \(k\), does not establish the required uniform fixed-parameter bound.''',
 answer_criterion=r'''Supply a complete Lean-checked construction of \(A,f,c\), with total computability of \(f\), exact correctness and the stated uniform running-time bound; or supply a complete Lean-checked proof that no such algorithm, function and exponent exist. A hardness reduction conditional on a separation of parameterized complexity classes establishes only that conditional obstruction, unless the needed separation is also proved. An algorithm for vertex deletion, a proper subclass of perfect graphs or a larger combined parameter does not meet the target.''',
 source_formulation=dict(
 text='Open Problem 2.17 asks whether deleting at most k edges to obtain a perfect graph is fixed-parameter tractable in k. The edge operation follows the survey’s global graph-modification convention and is explicit in the earlier cited paper’s conclusion.',
 caption='Paraphrase of the published survey, §2.2, Open Problem 2.17, p. 8; the 2020 preprint has the same question on p. 13.',
 citation='primary',format='editorial_paraphrase'),
 why='Perfect graphs form a broad class on which fundamental optimization problems become tractable. An algorithm for repairing a graph by a small number of edge deletions would locate an important boundary of parameterized graph modification. The distinction from vertex deletion is substantive: the vertex problem already has strong parameterized hardness, while the edge problem has remained unresolved across successive surveys.',
 importance=dict(score=82,method='editorial',
  reason='A long-standing parameterized graph-modification question for a central hereditary graph class. Its resolution would distinguish whether efficient recognition and the structure of perfect graphs extend to uniform repair by few edge changes, beyond established results for narrower classes.',
  basis='Individual review of the explicit 2011/2013 concluding question, its retention in the 2020/2023 survey, and the different vertex-deletion hardness.'),
 references=[
 ref('primary','A survey of parameterized algorithms and the complexity of edge modification',
  'Christophe Crespelle; Pål Grønås Drange; Fedor V. Fomin; Petr Golovach',2023,
  'https://doi.org/10.1016/j.cosrev.2023.100556',
  'Computer Science Review 48, article 100556, online 26 April 2023; §1 edge-modification conventions and §2.2, Open Problem 2.17, printed/PDF p. 8. Earlier arXiv:2001.06867v2, same question on p. 13.'),
 ref('vertex','Parameterized complexity of vertex deletion into perfect graph classes',
  'Pinar Heggernes; Pim van ’t Hof; Bart M. P. Jansen; Stefan Kratsch; Yngve Villanger',2013,
  'https://doi.org/10.1016/j.tcs.2012.03.013',
  'Theoretical Computer Science 511:172–180, 4 November 2013; checked full author manuscript dated 11 November 2011 at https://pimvanthof.github.io/perfectdeletion.pdf, abstract, §§1–2 and conclusion p. 12'),
 ref('essential','Search-space reduction via essential vertices revisited: Vertex multicut and cograph deletion',
  'Bart M. P. Jansen; Ruben F. A. Verhaegh',2026,
  'https://doi.org/10.1016/j.jcss.2025.103730',
  'Journal of Computer and System Sciences 156, article 103730, March 2026; publisher abstract and introduction, discussion of Perfect Deletion as vertex deletion'),
 ],
 context_blocks=[
 block('The survey uses Deletion for deleting edges. Recovering that convention is essential because the same short problem name is also used for a different vertex-deletion problem.'),
 block(r'The earlier paper proves \(\mathrm{W}[2]\)-hardness for deleting vertices to obtain a perfect graph, then explicitly asks whether edge deletion and edge completion are fixed-parameter tractable. The vertex hardness does not answer the edge question.','vertex'),
 block('Perfectness is preserved by taking the graph complement. Consequently, edge deletion on a graph and edge insertion on its complement have the same budget and equivalent outcomes; the earlier paper states this connection. The present card chooses edge deletion as its single formal operation.','vertex'),
 block('Recognizing a perfect graph is possible in polynomial time. Trying all small edge-deletion sets therefore gives polynomial time for each fixed budget, but the resulting exponent depends on the budget and does not establish fixed-parameter tractability.','vertex'),
 block('The 2026 essential-vertex paper also uses Perfect Deletion for the vertex operation. Its cited obstruction for detecting mandatory vertices is a different target from the unrestricted edge-deletion decision problem.','essential'),
 ],
 progress=[
 progress('2011-11-11','The checked author manuscript explicitly separates the proved vertex-deletion hardness from the open edge-deletion and completion questions.','vertex'),
 progress('2023-04-26','The published edge-modification survey retains the edge-deletion FPT question as Open Problem 2.17.'),
 progress('2026-03','The essential-vertex study discusses a different perfect-graph modification operation.','essential'),
 progress(DATE,'The review fixes edge deletion, the budget-only parameterization and the uniform deterministic FPT criterion; no later resolution is found in the bounded source search.'),
 ],
),notes,sources,status,summary=[
 'A graph is perfect if every induced subgraph needs exactly as many colors as the size of its largest clique.',
 'The problem asks whether at most a given number of edges can be deleted to make an arbitrary graph perfect.',
 'The desired algorithm has a polynomial input-size exponent independent of that deletion budget, with a computable budget-dependent factor.',
 'The source concerns edge deletion, whereas the known parameterized hardness concerns deleting vertices.',
 'The question remains open in the checked survey, and recent work on essential vertices does not resolve this edge-deletion target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
