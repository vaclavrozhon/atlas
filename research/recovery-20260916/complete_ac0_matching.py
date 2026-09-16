"""Apply the selected graph-search approximation target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-3384'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user choice of graph matching with output size at least c*OPT^alpha for some fixed positive constants.',
 'Separated construction of actual disjoint edges from numerical estimation and removed the independent set-packing target.',
 'Recovered deterministic DLOGTIME-uniform AC0 from the source circuit definitions, with no random bits, threshold gates or advice.',
 'Specified the adjacency-matrix input and output, exact validity on every graph, uniformity, all constants and the empty graph convention.',
 'Assessed importance individually and checked the scope of recent monotone perfect-matching lower bounds.',
]
sources=[
 'Read SWAT 2020 Article 9 §2, p. 9:3, for DLOGTIME-uniform Boolean circuits and the multi-output functional class.',
 'Read §5.2, p. 9:14, including the open search question and Theorem 5.6 with its proof. The theorem outputs an approximation to packing cardinality, not a packing.',
 'Read the primary abstract and scope of Cavalar–Göös–Riazanov–Sofronova–Sokolov, ECCC TR25-102, revised 6 November 2025: the lower bound is for monotone exact perfect-matching decision.',
 'Bounded primary-source searches through 16 September 2026 found no construction or impossibility theorem for the selected unrestricted-Boolean AC0 search target. The user supplied the approximation scale, which the source leaves unspecified.',
]
status=('The 2020 source leaves approximate matching construction in AC0 open without fixing a ratio. '
 'On 16 September 2026 the user selected the polynomial-in-optimum graph-search variant formalized here. '
 'The checked 2025 monotone exact-decision lower bound does not settle this variant. No resolution was found in the bounded review.')
complete(identifier,dict(
 title=r'Polynomial-in-optimum graph matching in \(\mathrm{AC}^{0}\)',
 criterion='construction',question_type='yes_no',
 formal=r'''Do there exist constants \(c,\alpha>0\) and a DLOGTIME-uniform family of deterministic Boolean circuits \((C_n)_{n\ge1}\), of constant depth and polynomial size, such that every finite simple undirected graph \(G\) on \(\{1,\ldots,n\}\) is mapped to a matching \(M(G)\subseteq E(G)\) satisfying
\[
|M(G)|\ \ge\ c\,\nu(G)^\alpha?
\]
Here \(\nu(G)\) is the maximum cardinality of a matching in \(G\). The same constants and circuit family must work for all \(n\) and all graphs. The output must identify the actual chosen edges. The scale \(c\,\nu^\alpha\), and the restriction to graph matching rather than general set packing, were explicitly selected by the user.''',
 definitions=r'''A finite simple undirected graph has no loops or parallel edges. Its input is its \(n\times n\) adjacency matrix \(A\), in row-major order, with \(A_{ii}=0\), \(A_{ij}=A_{ji}\in\{0,1\}\), and \(A_{ij}=1\) exactly when \(\{i,j\}\in E(G)\). Thus \(C_n\) has \(n^2\) input bits. Correctness is required on every valid adjacency matrix; behavior on other bit strings is unrestricted.

The circuit has \(n^2\) output bits, interpreted as a matrix \(B\) in the same order. It must satisfy \(B_{ii}=0\), \(B_{ij}=B_{ji}\le A_{ij}\), and, for every vertex \(i\), at most one \(B_{ij}\) is one. The represented matching is
\[
M(G)=\{\{i,j\}:i<j,\ B_{ij}=1\}.
\]
A matching is any collection of edges with pairwise disjoint endpoint sets, and \(\nu(G)=\max\{|M|:M\text{ is a matching in }G\}\). This counts edges, not covered vertices. For an edgeless graph \(\nu(G)=0\), and the output is the empty matching; use \(0^\alpha=0\).

The permitted internal gates are AND and OR of unbounded fan-in and NOT of fan-in one, together with constant zero and one. Circuits are finite directed acyclic graphs; wires may fan out to many gates. There are fixed integers \(D,k\ge1\) and a constant \(K\ge1\) such that every \(C_n\) has depth at most \(D\) and at most \(K(n+1)^k\) gates and wires. Depth is the maximum number of internal gates on any input-to-output path. The circuits receive no randomness, advice or auxiliary graph information.

DLOGTIME uniformity means that the circuits admit gate addresses of \(O(\log(n+2))\) bits and a single deterministic random-access Turing machine describing their local wiring in \(O(\log(n+2))\) time. Given \(n\) in binary and gate addresses, it decides whether an address is valid, the gate type, and whether a directed wire joins two addressed gates; it also identifies the designated input and output gate for an addressed matrix coordinate. Random access means that the machine can query an input bit using its binary address. The machine and constants are independent of \(n\) and of the input graph. Hardwiring a separate arbitrary circuit description for each \(n\) is not uniformity.

The constants \(c,\alpha\) do not depend on \(n\) or on \(\nu(G)\). One may equivalently require rational \(0<c,\alpha\le1\): decreasing either positive constant preserves the assertion for integer \(\nu(G)\ge1\), and \(|M(G)|\le\nu(G)\) rules out a persistent exponent greater than one on graphs with unbounded optimum. The condition asks for a positive power of the optimum; it is not an assertion of a fixed ratio \(|M(G)|/\nu(G)\).''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of this exact existence assertion. A positive answer must specify the uniform circuit family and fixed constants and prove circuit size, depth, uniformity, output validity and the cardinality inequality for every graph. A negative answer must refute all choices of positive constants and all allowed circuit families. This binary question has no numerical \(1/100\) tolerance. Producing only an estimate of \(\nu(G)\), proving a limitation of monotone circuits, or handling a restricted input class alone does not meet this target.''',
 source_formulation=dict(
 text='The source leaves open whether AC0 circuits can construct approximate graph matchings, and then raises the more general set-packing question. Its positive approximation result concerns the optimum size alone.',
 caption='Paraphrase of §5.2 and Theorem 5.6. The precise polynomial-in-optimum guarantee is the user-selected specialization.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=66,method='editorial',
 reason='The problem isolates whether extremely shallow uniform Boolean computation can construct a growing set of compatible choices even when it can already estimate their attainable number.',
 basis='Individual assessment of the search-versus-estimation distinction, the weak circuit model and the broad graph input class.'),
 why='A matching requires many output decisions to be mutually consistent: selected edges may not share vertices. This creates a concrete test of the constructive power of uniform constant-depth circuits. A resolution would clarify how much of combinatorial approximation survives when the number of sequential logical layers is bounded independently of input size.',
 references=[
 ref('primary','Kernelizing the Hitting Set Problem in Linear Sequential and Constant Parallel Time',
 'Max Bannach; Malte Skambath; Till Tantau',2020,
 'https://doi.org/10.4230/LIPIcs.SWAT.2020.9',
 'SWAT 2020, Article 9; §2 circuit definitions, p. 9:3; §5.2 and Theorem 5.6, p. 9:14'),
 ref('monotone','Monotone Circuit Complexity of Matching',
 'Bruno Cavalar; Mika Göös; Artur Riazanov; Anastasia Sofronova; Dmitry Sokolov',2025,
 'https://eccc.weizmann.ac.il/report/2025/102/revision/1/',
 'Revision 1, 6 November 2025; abstract and Theorem 1: monotone circuits for exact perfect-matching decision'),
 ],
 context_blocks=[
 block('The source uses the functional version of AC0: a circuit can have many output bits, but still has constant depth, polynomial size and DLOGTIME uniformity. Its Boolean basis includes negation. Threshold or majority gates belong to the stronger TC0 model used separately in the paper.'),
 block('For hitting set, the paper gives AC0 circuits that output a hitting set with size polynomial in the optimum. The analogous passage for packing explicitly says that extracting a collection of disjoint sets remains an unresolved issue.'),
 block('Theorem 5.6 estimates the size of an optimum packing in a bounded-rank hypergraph. For graphs its guarantee gives a numerical lower estimate on the order of the square root of the optimum. The returned number does not identify disjoint edges, so it does not solve the search question.'),
 block('The source does not prescribe a matching approximation ratio. The selected target fixes a positive-power guarantee in the optimum, which can be substantially weaker than a constant-factor approximation. The source’s independent extension to general set packing remains provenance rather than a second task on this card.'),
 block('The 2025 monotone lower bound concerns deciding whether a perfect matching exists using AND and OR without negation. Both the restricted gate basis and the exact decision objective differ from the construction problem here. It therefore supplies context, not a negative resolution.','monotone'),
 ],
 progress=[
 progress('2020','The published paper gives uniform shallow-circuit packing-size estimates and leaves construction of approximate matchings open.'),
 progress('2025-11-06','A revised monotone perfect-matching lower bound concerns a different gate basis and exact decision task.','monotone'),
 progress('2026-09-16','The user selects graph matching with a positive-power-of-optimum output bound; the individual review specifies the complete circuit and output model.'),
 ],
),notes,sources,status,summary=[
 'The input is an arbitrary labelled simple graph, and the output must explicitly identify pairwise vertex-disjoint edges.',
 'One deterministic uniform AC0 circuit family must produce at least c times the optimum matching size to the power alpha, for fixed positive c and alpha.',
 'The circuits have constant depth, polynomial size and unrestricted-fan-in AND and OR gates together with negation.',
 'The source can estimate packing cardinality in this model but does not construct a corresponding packing.',
 'The selected search question remains unresolved in the checked sources and is distinct from recent monotone exact-matching lower bounds.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
