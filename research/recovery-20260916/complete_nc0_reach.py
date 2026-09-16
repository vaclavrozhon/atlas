"""Individual completion of the selected directed-reachability proof-system question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0071'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Circuits, Logic and Games: Proof systems computed by NC⁰ circuit families','Karteek Sreenivasaiah',2016,
 'https://drops.dagstuhl.de/entities/document/10.4230/DagRep.5.9.105',
 'Dagstuhl Seminar 15401, held September–October 2015; report published 21 January 2016; §4.4, printed p. 123 (PDF p. 19)'),
 ref('paper','Small Depth Proof Systems','Andreas Krebs; Nutan Limaye; Meena Mahajan; Karteek Sreenivasaiah',2016,
 'https://people.iith.ac.in/karteek/assets/pdf/SmallDepthProofSystems.pdf',
 'ACM Transactions on Computation Theory 9(1), Article 2, October 2016; Definition 2.1, §4, Theorem 4.11 and Proposition 4.17; DOI 10.1145/2956229'),
 ref('preprint','Small Depth Proof Systems','Andreas Krebs; Nutan Limaye; Meena Mahajan; Karteek Sreenivasaiah',2013,
 'https://eccc.weizmann.ac.il/report/2013/102/',
 'ECCC TR13-102; earlier version records the open directed case and the positive undirected/unreachability cases'),
]
notes=[
 'Applied the user’s choice of directed reachability, rather than the separate regular-language characterization in the source.',
 'Defined a proof system as an exact surjection from all proof strings to the adjacency matrices of yes-instances, not a decision verifier.',
 'Fixed the two distinguished vertices, row-major n-by-n encoding, permitted loops and the complete quantifier order.',
 'Used the source’s nonuniform bounded-fanin constant-depth circuit convention; no efficient circuit-construction requirement is added.',
 'Explained that linear size and linearly many relevant proof bits follow after pruning from the constant depth and output count.',
 'Preserved the existing category and importance and required a complete Lean proof of the exact existence assertion.',
]
sources=[
 'Read Dagstuhl report §4.4, printed p. 123: it lists the directed-path existence question separately from regular-language characterization. Checked the January 2016 publication date versus the 2015 seminar date.',
 'Read the published Small Depth Proof Systems Definition 2.1 and §4 directed adjacency-matrix definition. The source uses all matrix entries, including diagonal entries.',
 'Read the introduction, Theorem 4.11 and Proposition 4.17: undirected reachability and directed unreachability have NC0 proof systems, while directed reachability remains explicitly open in that source.',
 'Checked the earlier ECCC/arXiv record and performed a bounded primary-source search through 16 September 2026. No later resolution was found; the review does not certify that every intervening paper has been covered.',
]
status=('The 2015 seminar question and the October 2016 journal paper explicitly leave directed reachability open. '
 'Their positive results concern undirected reachability or directed unreachability, which are different output languages. '
 'No later resolution was found in the bounded primary-source check through 16 September 2026. '
 'The user selected this directed-reachability target on that date.')
complete(identifier,dict(
 title=r'\(\mathrm{NC}^{0}\) proof systems for directed reachability',
 criterion='decision',question_type='yes_no',
 formal=r'''For \(n\ge2\), let
\[
R_n=\{A\in\{0,1\}^{n\times n}:
\text{the directed graph encoded by }A\text{ has a path from }1\text{ to }n\}.
\]
Does there exist an integer \(D\ge0\) such that for every integer \(n\ge2\) there are a nonnegative integer \(m_n\) and a Boolean circuit
\[
C_n:\{0,1\}^{m_n}\longrightarrow\{0,1\}^{n^2}
\]
of depth at most \(D\), using AND and OR gates of fan-in at most two and NOT gates, for which
\[
\{C_n(z):z\in\{0,1\}^{m_n}\}=R_n?
\]
The right side is identified with row-major adjacency-matrix encodings. Equivalently, every proof string must produce a graph with the required directed path, and every graph with that path must be produced by some proof string.''',
 definitions=r'''The graph has labeled vertices \(\{1,\ldots,n\}\), with distinguished vertices \(s=1\) and \(t=n\). The entry \(A_{ij}=1\) means that the edge \(i\to j\) is present. There are no parallel edges; self-loops are allowed. The output is the \(n^2\)-bit string \(A_{11},A_{12},\ldots,A_{nn}\), in row-major order. A directed path from \(1\) to \(n\) is a sequence \(v_0=1,v_1,\ldots,v_\ell=n\) with \(A_{v_{i-1},v_i}=1\) for every step. Existence is unchanged if one requires the vertices of the path to be distinct.

A Boolean circuit is a finite directed acyclic graph of input nodes, gates and designated outputs. Constants zero and one are allowed. AND and OR have at most two incoming wires, NOT has one, and an output may copy an input, constant or gate. Fan-out is unrestricted. Depth is the maximum number of gates on a path from an input or constant to an output. The same bound \(D\) must work at every \(n\).

This is the nonuniform \(\mathrm{NC}^0\) convention: circuits may be chosen separately for each \(n\), with no required running time for constructing their descriptions. After gates and proof bits that influence no output are removed, bounded fan-in and depth imply at most \(O(2^D n^2)\) gates and relevant input bits. Thus the family has linear size in its output length, without an extra size hypothesis. Each output bit depends on at most \(2^D\) input bits, possibly a different set for each output position.

A proof system here is a total generating map whose range is exactly the target language at the relevant output length. All \(2^{m_n}\) proof strings are allowed. There is no promise that an input is a valid path encoding and no separate test that may reject malformed proofs. Soundness is the universal requirement \(C_n(z)\in R_n\); completeness is surjectivity onto \(R_n\). The graph is the output, not an input to a one-bit acceptance circuit.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the displayed existence assertion. A positive answer must establish one fixed depth bound and soundness and completeness of the circuit family for every graph size. It may be nonuniform. A negative answer must show that every fixed depth fails at some size, for all circuits in this model. A depth lower bound for deciding reachability, or failure of one generating construction, is insufficient. This is an exact binary target; no error probability or numerical \(1/100\) tolerance is permitted.''',
 source_formulation=dict(text='The source asks whether the directed graphs with a path between two distinguished vertices can be exactly generated by a family of bounded-fan-in circuits of constant depth.',
 caption='Paraphrase of the directed-reachability item in §4.4; selected by the user on 16 September 2026. The source’s separate regular-language question is outside this card.',citation='primary',format='editorial_paraphrase'),
 why='The question asks whether a global directed-path property can be guaranteed by generating each edge from only constantly many proof bits, while still representing every yes-instance. The contrast with known local proof systems for undirected reachability and directed unreachability isolates the role of direction and global consistency in very weak proof systems.',
 references=refs,
 context_blocks=[
 block('Ordinary reachability algorithms receive a graph and search for a path. Here a proof string produces the entire graph. The generator must arrange that even arbitrary, inconsistent input bits produce a yes-instance, while retaining enough flexibility to produce every graph containing the distinguished path.','paper'),
 block('Constant depth with bounded fan-in makes each output edge depend on only a constant number of proof bits. Different edge positions may depend on different bits, and a proof bit may influence many edges. This local dependence is the substantive restriction; the proof need not be a list of path vertices.','paper'),
 block('The published paper constructs such proof systems for undirected reachability. Thus the mere fact that paths are global objects does not prove that a local generating map is impossible. Direction of edges remains an essential distinction in the open case.','paper'),
 block('It also constructs a proof system for directed unreachability: graphs having no path from the first distinguished vertex to the second. Complementing the output bits of that generator would complement individual edges, not complement the reachability property of the graph. The positive unreachability result therefore does not immediately transfer.','paper'),
 block('The class of languages with these proof systems is not determined simply by the difficulty of ordinary membership testing. The paper gives a depth obstruction even for the regular language of strings with exactly one one, alongside positive results for more complex languages.','paper'),
 block('The seminar report additionally asks for a characterization of regular languages admitting these systems. The user chose the directed graph problem as this card’s single target, so that separate classification task is recorded only as provenance.'),
 ],
 progress=[
 progress('2013','The earlier paper records positive results for the undirected and unreachability cases and leaves directed reachability open.','preprint'),
 progress('2015','The Dagstuhl seminar lists the directed-reachability proof-system question.'),
 progress('2016-10','The journal version defines the exact range convention and proves the neighboring positive cases.','paper'),
 progress('2026-09-16','The user selects directed reachability; the individual review fixes its encoding, circuit model and exact soundness/completeness conditions.'),
 ],
),notes,sources,status,summary=[
 'The target language consists of directed adjacency matrices with a path from vertex one to the last vertex.',
 'An NC⁰ proof system must generate exactly these matrices from arbitrary input bit strings.',
 'Each output edge depends on only constantly many proof bits, with one constant depth bound for all graph sizes.',
 'Such generators are known for undirected reachability and for directed unreachability.',
 'The selected directed-reachability existence question remains unresolved in the sources checked by this review.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
