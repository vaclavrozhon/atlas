"""Complete the unrestricted planar oriented two-colour conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7254';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the exact two-colour proposition for every finite oriented planar graph, including directed triangles.',
 'Made the vertex-partition requirement, induced subdigraphs, directed cycles, empty graph and empty colour classes explicit.',
 'Separated directed acyclicity from proper colouring and undirected forests; no connectivity, degree, Eulerian or girth promise is added.',
 'Required a complete Lean-checked all-graph proof or a finite planar counterexample with every colouring excluded.',
 'Corrected the Garden posting date to 26 March 2007 and checked the final February 2026 partition paper and July 2026 feedback-vertex-set preprint.',
 'Preserved importance 92 and category; distinguished the 2026 list Erdős–Neumann–Lara and maximum-hypergraph-forest results from the selected conjecture.',
]
sources=[
 'Read Open Problem Garden, The Two Color Conjecture, posted by mdevos on 26 March 2007: exact orientation-of-simple-planar-graph statement; the bibliography attributes the original question to Neumann-Lara’s 1985 technical report.',
 'Read Li–Mohar, arXiv:1606.06114v1, 20 June 2016, primary abstract: two acyclic colours for planar digraphs of digirth at least four. No full proof audit was undertaken.',
 'Read Cambie–Dross–Knauer–La–Valicov, EJC 33(1), P1.27, final publisher PDF, published 13 February 2026: Introduction, Conjectures 3 and 4 p. 2, Definition 5, and Theorems 9–11 p. 4. The paper retains the general conjecture; its negative CAI-partition theorem refutes a proposed sufficient condition rather than two-colourability.',
 'Read Dreyer, arXiv:2607.13895v1, submitted 15 July 2026 (PDF dated 16 July), abstract and Introduction pp. 1–3. Conjecture 3 p. 2 explicitly retains the full two-colour problem. Its feedback-vertex-set bound gives one large acyclic induced set; it does not require that the removed set be acyclic. The full proof was not independently verified.',
 'Read the primary abstract of Harutyunyan–Picasarri-Arrieta–Puig i Surroca, arXiv:2603.01020, March 2026: the theorem concerns the list version of a chromatic-to-dichromatic-number conjecture for arbitrary graphs, a different assertion.',
 'Read Strausz, Maximum k-Forests Are Tight, primary Springer article published 1 September 2026, abstract and main theorem. This concerns k-uniform hypergraphs, separable edges and heterochromatic colourings; despite the Neumann-Lara attribution it is unrelated to planar oriented two-colouring.',
 f'Bounded primary-source searches through {DATE} found no verified proof or counterexample to the exact unrestricted target.',
]
complete(identifier,dict(
 title='Neumann–Lara conjecture',criterion='construction',question_type='yes_no',
 formal=r'''Is it true that for every finite oriented graph \(D=(V,A)\) whose underlying undirected graph is planar, there exists a map \(c:V\to\{0,1\}\) such that
\[
 D[c^{-1}(0)]\quad\text{and}\quad D[c^{-1}(1)]
\]
are both acyclic?''',
 definitions=r'''The vertex set \(V\) is any finite set, including the empty set. The arc set \(A\subseteq V\times V\) has no loops, and for distinct vertices \(u,v\) at most one of \((u,v)\) and \((v,u)\) belongs to \(A\). There are no repeated arcs. Thus \(D\) is an orientation of the simple undirected graph \(G\) with edge set
\[
 E(G)=\{\{u,v\}:(u,v)\in A\}.
\]
Planarity means that \(G\) has a drawing in the plane in which vertices are distinct points and edges are simple arcs whose interiors are mutually disjoint and avoid all vertices. A particular drawing is not part of the assertion.

For \(X\subseteq V\), the induced digraph \(D[X]\) has vertex set \(X\) and all arcs of \(A\) with both endpoints in \(X\). A directed cycle of length \(\ell\ge3\) is a sequence of distinct vertices \(v_0,\ldots,v_{\ell-1}\) with \((v_i,v_{(i+1)\bmod\ell})\in A\) for every \(i\). It need not be induced or bound a face in a planar drawing. A digraph is acyclic if it contains no such cycle. Loops and two-cycles are already excluded by the oriented-graph definition.

The two colour classes form a partition of all vertices; either may be empty. Every directed cycle must contain vertices of both colours. An arc may have both endpoints in the same class, so this is not proper vertex colouring. Nor must either class induce a forest in the underlying undirected graph: an undirected cycle with an acyclic orientation is allowed.

The quantifier includes disconnected graphs, isolated vertices and directed triangles. No bound on degree, connectivity or directed girth and no balance between in-degrees and out-degrees is assumed. The classes need not be connected, independent, equal in size or balanced in any specified way. The claim asks only for their existence; no running-time requirement is imposed on finding the colouring.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the assertion for every graph in the stated class, or a complete Lean-checked refutation. A negative answer can consist of one finite oriented graph together with verified planarity and a proof that every map of its vertices to two colours has a monochromatic directed cycle.

A theorem only for graphs without directed triangles, for Eulerian orientations, for bounded orders or for another proper subclass does not settle the proposition. Finding one large acyclic vertex set does not suffice unless its complement is also proved acyclic. A counterexample to a stronger auxiliary partition property does not by itself refute this assertion. No approximation tolerance applies to the exact yes/no question.''',
 source_formulation=dict(text='Every orientation of a finite simple planar graph should admit a vertex partition into two sets, each inducing an acyclic digraph. The source attributes this two-colour conjecture to Neumann-Lara’s 1985 report.',caption='Paraphrase of the Garden statement posted 26 March 2007, and Conjecture 3 in the July 2026 feedback-vertex-set preprint.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Two Color Conjecture','Open Problem Garden contributors; conjecture attributed to Víctor Neumann-Lara',2007,'https://www.openproblemgarden.org/op/partitioning_planar_digraphs','Posted 26 March 2007; conjecture statement and bibliography to the 1985 report'),
 ref('digirth','Planar digraphs of digirth four are 2-colourable','Zhentao Li; Bojan Mohar',2016,'https://arxiv.org/abs/1606.06114v1','20 June 2016; abstract, no directed cycle of length less than four'),
 ref('partitions','Partitions of planar (oriented) graphs into a connected acyclic and an independent set','Stijn Cambie; François Dross; Kolja Knauer; Hoang La; Petru Valicov',2026,'https://doi.org/10.37236/13673','EJC 33(1), P1.27, 13 February 2026; Conjectures 3–4 and Definition 5 p. 2, Theorems 9–11 p. 4'),
 ref('fvs','Feedback vertex sets in oriented graphs','Simon Dreyer',2026,'https://arxiv.org/abs/2607.13895v1','15 July 2026; abstract and Introduction, especially Conjecture 3 p. 2 and main results p. 3'),
 ],
 context_blocks=[
 block('The two classes may contain directed paths and branching structures. The only forbidden pattern within a class is a directed cycle, so ordinary proper-colouring restrictions would ask for substantially more.'),
 block('The known digirth-four theorem handles planar orientations without directed triangles. The general conjecture permits directed triangles while requiring every directed cycle, of any length, to use both colours.','digirth'),
 block('The 2026 partition paper studies a stronger condition: one connected acyclic part and one independent part. Its counterexample to a proposed intermediate decomposition does not show a graph with no partition into two arbitrary acyclic sets.','partitions'),
 block('The July 2026 preprint improves bounds on how many vertices need to be deleted to leave one acyclic digraph. The deleted vertices are not required to be acyclic themselves; the preprint explicitly keeps the two-colour conjecture open.','fvs'),
 ],
 progress=[progress('1985','The original conjecture is attributed to Neumann-Lara’s technical report.','primary'),progress('2016-06-20','The no-directed-triangle case is established.','digirth'),progress('2026-02-13','The partition paper retains the general conjecture while proving restricted positive results and a counterexample to an auxiliary condition.','partitions'),progress('2026-07-15','A preprint improves feedback-vertex-set bounds and explicitly retains the full two-colour conjecture.','fvs')],
),notes,sources,'The final February 2026 partition paper and the July 2026 feedback-vertex-set preprint explicitly retain the unrestricted two-colour conjecture. Bounded primary-source checks through 17 September 2026 found no verified resolution. The list-colouring and hypergraph-forest results carrying similar names concern different assertions; new proofs were not independently certified.',summary=[
 'The Neumann–Lara conjecture asks for two acyclic vertex classes in every orientation of a finite simple planar graph.',
 'Arcs within a class are allowed, but every directed cycle must use both colours.',
 'Directed triangles, disconnected graphs and unrestricted vertex degrees are included.',
 'Known results without directed triangles and bounds on one large acyclic set leave the full partition question open.',
 'A complete Lean-checked solution must prove the all-graph assertion or certify a finite planar counterexample.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
