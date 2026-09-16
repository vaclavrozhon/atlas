"""Review the width/direct-input-degree linearization conjecture over GF(2)."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1059'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Research Problem 13.14 together with the model in §13.8 of the author’s early draft.',
 'Defined degree as the number of direct input wires into an output gate, excluding all wires incident with the middle layer.',
 'Specified arbitrary Boolean gates, exact computation on every input, the binary field and global constant-factor bounds on both resources.',
 'Separated existence of a linear circuit from an efficient algorithm for finding the conversion.',
 'Included the equivalent low-rank plus row-sparse matrix formulation and the zero-resource boundary cases.',
 'Preserved the existing importance assessment and checked the later block-rigidity and data-structure formulations without treating their extra hypotheses as resolutions.',
]
sources=[
 'Read Jukna, Boolean Function Complexity, author-hosted early draft: §13.8 printed pp. 386–387 and Research Problem 13.14 printed p. 393, PDF p. 400, with neighboring Exercises 13.15–13.16. Internal draft cross-reference placeholders were not copied into the card.',
 'Read Mittal–Raz, Block Rigidity: Strong Multiplayer Parallel Repetition implies Super-Linear Lower Bounds for Turing Machines, ECCC TR20-173 revision 1 accepted 27 November 2020: §7 Definition 33, Conjecture 34 and Observation 35, pp. 13–14. This explicitly restates the same circuit model and its matrix interpretation.',
 'Read Ko, Efficient Linearization Implies the Multiphase Conjecture, ECCC TR22-122 published 30 August 2022, abstract and §1, including Conjectures 1.2 and 1.5. Its strengthened data-structure hypothesis is not the theorem sought here.',
 'Bounded later primary-source searches through 16 September 2026 found no proof or counterexample to the stated constant-factor width/degree conjecture. Results optimizing particular linear matrices do not compare them to arbitrary Boolean gates.',
]
status=('The author-hosted book draft poses this constant-factor linearization problem, and the checked later work restates it or studies strengthened data-structure variants. '
 'No general proof or counterexample was found in the bounded later-source review. The target concerns existence, without a running-time requirement on finding the linear circuit.')
complete(identifier,dict(
 title='Linearization conjecture for depth-two circuits',
 criterion='reductions',question_type='yes_no',
 formal=r'''Is there an absolute integer \(C\ge1\) with the following property?

For every \(n\ge1\), every matrix \(A\in\mathbb F_2^{n\times n}\), and all integers \(w,d\ge0\), if the linear map \(x\mapsto Ax\) is computed exactly by a depth-two circuit with arbitrary Boolean gates, width at most \(w\), and degree at most \(d\), then it is computed exactly by a linear depth-two circuit with width at most \(Cw\) and degree at most \(Cd\).

Width counts middle-layer gates. Degree counts, for each output separately, only the direct wires from the original input variables; it does not count wires through middle-layer gates. Both notions and the gate models are defined below. The constant \(C\) is independent of the matrix, dimensions and resource bounds.''',
 definitions=r'''The field \(\mathbb F_2=\{0,1\}\) uses addition modulo two and ordinary bit multiplication. For \(x=(x_1,\ldots,x_n)\), the required output has coordinates
\[
(Ax)_i=\bigoplus_{j:A_{ij}=1}x_j .
\]
The circuit is deterministic and may depend arbitrarily on \(A\); no uniformity requirement is imposed.

A depth-two circuit of width \(r\) has \(n\) input bits, \(r\) middle-layer gates computing arbitrary functions \(h_j:\{0,1\}^n\to\{0,1\}\), and \(n\) output gates. For each output \(i\), choose a fixed set \(S_i\subseteq[n]\) and an arbitrary Boolean function \(g_i\) such that the output is
\[
g_i\bigl(x_{S_i},h_1(x),\ldots,h_r(x)\bigr).
\]
The set \(S_i\) lists its direct input wires. Its middle-gate inputs can be any subset of the displayed values; unused arguments can be ignored. Gates have unrestricted fan-in and arbitrary truth tables. There are no edges between gates in the same layer. Input bits may connect directly to output gates. The width is \(r\), and the degree is \(\max_i|S_i|\). Neither the number of input-to-middle wires nor the number of middle-to-output wires is included in degree.

Such a circuit computes \(Ax\) exactly if every displayed output equals \((Ax)_i\) for every \(x\in\{0,1\}^n\). Agreement only on the standard basis vectors, or on most inputs, is not sufficient. An arbitrary gate may compute a nonlinear Boolean function even though the final map is linear.

A linear depth-two circuit has the same graph convention, but each gate computes a linear form over \(\mathbb F_2\): a parity of some of its inputs, including the empty parity zero. No nonzero constant term is needed. Thus, with \(r\) middle gates, its transformation has the form
\[
Ax=L(Rx)+Ex,\qquad
R\in\mathbb F_2^{r\times n},\quad
L\in\mathbb F_2^{n\times r},\quad
E\in\mathbb F_2^{n\times n}.
\]
Its direct-input degree is the maximum number of nonzero entries in a row of \(E\). Equivalently, the desired conclusion is that
\[
A=B+E,\qquad
\operatorname{rank}_{\mathbb F_2}(B)\le Cw,\qquad
\max_i|\{j:E_{ij}\ne0\}|\le Cd.
\]
A rank factorization of \(B\) gives the middle-layer linear forms, so this is precisely the same existence target.

The conclusion may choose new direct-input sets and a new middle layer; it need not preserve the input circuit graph. It must bound both width and degree simultaneously. The cases \(w=0\) and \(d=0\) use the displayed multiplicative bounds without additive slack. One may restrict \(0\le d\le n\), since larger direct degree adds no power. There is no restriction on truth-table description size, total circuit wire count or the time needed to find the linear circuit.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the universal constant-factor linearization statement. A proof may use either the circuit formulation or the equivalent rank-plus-row-sparsity formulation, with the equivalence justified. A refutation must show that no universal \(C\) works. A conversion with a growing factor, a result only for selected matrices, or agreement on a restricted set of inputs is insufficient. This is a binary proposition; \(1/100\) numerical tolerance does not alter either resource bound.''',
 source_formulation=dict(
 text='Research Problem 13.14 asks whether a linear operator computed with arbitrary depth-two gates can also be computed with linear gates while increasing both degree and width only by constant factors.',
 caption='Paraphrase of the author’s early draft, printed p. 393 (PDF p. 400); degree and width are defined in §13.8.',
 citation='primary',format='editorial_paraphrase'),
 why='A short nonlinear summary of the input might help answer many linear queries even when no equally short linear summary is available. The conjecture asks whether that advantage disappears up to constant factors when the only other resource is a few direct input bits per output. It would connect matrix-based lower bounds more closely to unrestricted Boolean computation.',
 references=[
 ref('primary','Boolean Function Complexity: Advances and Frontiers (author’s early draft)',
 'Stasys Jukna',2012,'https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf',
 '§13.8 printed pp. 386–387; Research Problem 13.14 printed p. 393, PDF p. 400; neighboring Exercises 13.15–13.16'),
 ref('block','Block Rigidity: Strong Multiplayer Parallel Repetition implies Super-Linear Lower Bounds for Turing Machines',
 'Kunal Mittal; Ran Raz',2020,'https://eccc.weizmann.ac.il/report/2020/173/',
 'ECCC TR20-173 revision 1, accepted 27 November 2020; §7 Definition 33, Conjecture 34 and Observation 35, pp. 13–14'),
 ref('data','Efficient Linearization Implies the Multiphase Conjecture',
 'Young Kun Ko',2022,'https://eccc.weizmann.ac.il/report/2022/122/',
 'ECCC TR22-122, published 30 August 2022; §1 Conjectures 1.2 and 1.5, distinction between circuit and data-structure linearization'),
 ],
 context_blocks=[
 block('This degree measure ignores the wires through the shared middle layer. Bounding ordinary gate fan-in, all graph degrees or total wires would give a different conjecture.'),
 block('A middle gate is an arbitrary one-bit summary of the whole input. Each output can inspect the shared summaries and its fixed collection of direct input bits. The question asks whether linear summaries are always comparably effective.'),
 block('For a linear circuit, the shared summaries correspond to a low-rank matrix, while direct input wires give a matrix sparse in every row. This connects the resource tradeoff to matrix rigidity.','block'),
 block('The source distinguishes representing a matrix on unit input vectors from computing its linear operator on every Boolean vector. Nonlinear circuits can behave quite differently in the representation problem, which does not refute this conjecture.'),
 block('The 2020 report restates the same conjecture and proves an implication from a stronger rigidity comparison. That conditional implication supplies additional motivation, not a proof of linearization.','block'),
 block('The 2022 report studies related linearization assumptions for data structures and derives consequences for the Multiphase Conjecture. Its extra model and hypotheses are not part of this card.','data'),
 ],
 progress=[
 progress('2012','The book draft records the explicit constant-factor degree-and-width question.'),
 progress('2020-11-27','The revised block-rigidity report restates it as Conjecture 34.','block'),
 progress('2022-08-30','The data-structure report studies stronger related linearization assumptions.','data'),
 progress('2026-09-16','The review expands the circuit resources and uniform constants and finds no general resolution in the bounded source check.'),
 ],
),notes,sources,status,summary=[
 'A depth-two Boolean circuit computes a linear transformation using shared middle-layer gates and direct input wires.',
 'The question asks whether all its gates can be made linear with only constant-factor increases in width and direct-input degree.',
 'Middle-layer gates may initially compute arbitrary Boolean functions, and every input vector must be handled exactly.',
 'The linear conclusion is equivalent to decomposing the matrix into a low-rank part and a part sparse in each row.',
 'The target is existence of such circuits, without a requirement to find the conversion efficiently.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
