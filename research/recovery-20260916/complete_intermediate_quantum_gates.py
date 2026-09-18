"""Fix the user-selected decision-class interpretation of quantum gate sets."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4927';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A finite quantum gate set with decision power strictly between P and BQP',
 status='source_open',criterion='models',question_type='yes_no',
 formal=r'''Does there exist a finite set \(G\) of constant-arity unitary quantum gates with algebraic complex matrix entries such that
\[
\mathrm P\subsetneq Q_G\subsetneq\mathrm{BQP},
\]
and \(G\) is not contained in any common one-qubit conjugate of the Clifford gates? The bounded-error decision class \(Q_G\), the circuit interface, and the conjugation exclusion are defined below. Both strict containments are unconditional parts of the assertion.''',
 definitions=r'''A \(k\)-qubit gate is a \(2^k\)-by-\(2^k\) complex unitary matrix, for an integer \(k\ge1\). The set \(G\) is finite and independent of input length; its maximum arity is therefore a constant. Each matrix entry is algebraic over \(\mathbb Q\), and each gate can be specified exactly by its minimal polynomials and isolating data for the real and imaginary parts. These fixed descriptions are not input-dependent advice. Algebraicity is an explicit editorial finite-description convention.

A language \(L\subseteq\{0,1\}^*\) is in \(Q_G\) if one deterministic polynomial-time Turing machine, on each input \(x\), produces a polynomial-size circuit description \(C_x\) with polynomially many qubits, a computational-basis initial string \(b_x\), and one designated output qubit. Initialize the state to \(|b_x\rangle\). A gate from \(G\) may be applied to any ordered tuple of distinct qubits of the correct arity, with identity on all other qubits. There are no geometry or depth restrictions beyond the polynomial size bound. At the end, measure only the designated output qubit in the computational basis. Require
\[
x\in L\Longrightarrow\Pr[C_x\text{ outputs }1]\ge2/3,
\qquad
x\notin L\Longrightarrow\Pr[C_x\text{ outputs }1]\le1/3.
\]
The generator and polynomial bound may depend on \(L\) and \(G\), but not nonuniformly on input length. They count all classical bit operations. The generator may prepare additional \(|0\rangle\) and \(|1\rangle\) qubits by specifying them in \(b_x\), but no other initial states. Wires may be named arbitrarily. Only gates listed in \(G\) are available: inverses, controlled variants, and arbitrary one-qubit gates are not free. Intermediate measurements, postselection, classically controlled quantum branches, quantum advice, and joint-output sampling followed by unrestricted classical postprocessing are not part of this interface. The final single-bit output convention makes the selected decision target precise.

The class \(\mathrm P\) consists of languages decidable by one deterministic polynomial-bit-time Turing machine. Define \(\mathrm{BQP}\) by the same uniform bounded-error circuit convention using the universal gates
\[
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
T=\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix},\quad
\operatorname{CNOT}|a,b\rangle=|a,a\mathbin{\oplus}b\rangle.
\]
Classical preprocessing and basis preparation imply \(\mathrm P\subseteq Q_G\). Fixed algebraic gates are efficiently approximable, so \(Q_G\subseteq\mathrm{BQP}\). The strictness requirements mean that some language in \(Q_G\) is not in \(\mathrm P\), and some language in \(\mathrm{BQP}\) is not in \(Q_G\). Merely failing to densely generate every unitary is insufficient, since encoded computation can still give full BQP power.

For the Clifford exclusion, let
\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
and let \(\mathcal P_k=\{i^j P_1\otimes\cdots\otimes P_k:j\in\{0,1,2,3\},\ P_i\in\{I,X,Y,Z\}\}\) be the Pauli group. The Clifford group consists of the unitaries \(V\) satisfying \(V\mathcal P_kV^\dagger=\mathcal P_k\); global phase is immaterial. Require that there is no one-qubit unitary \(U\) such that, for every \(g\in G\) of arity \(k\),
\[
U^{\otimes k}g(U^\dagger)^{\otimes k}
\]
is Clifford. The same \(U\) must be tested for all gates, but it may be any complex unitary, not only an algebraic one. The condition is a structural exclusion, not an additional allowed operation.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of existence of a finite algebraic gate set satisfying both strict decision-class containments and the common-conjugate Clifford exclusion. Conditional sampling hardness, universality only after postselection, a separation for nonuniform circuits, or physical nonuniversality alone does not settle the statement. A positive proof must establish both strictness assertions in the specified uniform single-output model.',
 why='A genuine intermediate decision class generated only by a finite gate set would expose a computational regime beyond deterministic classical computation but below universal quantum computation. It would distinguish gate-induced limitations from restrictions on depth, state preparation or geometry.',
 importance=dict(score=87,method='editorial',reason='A fundamental structural question about quantum computational resources. The selected strict decision-class target is exceptionally strong and entails P differing from BQP; sampling evidence must therefore be kept separate.'),
 source_formulation=dict(text='The source asks whether gate sets other than conjugated stabilizer gates can have complexity neither contained in P nor equal to BQP. Its surrounding examples also involve sampling. The user explicitly selected a decision class strictly between P and BQP. Finite algebraic gates, input-dependent uniform circuit generation, basis-state initialization and a single final output qubit specify that interpretation; they are editorial model conventions rather than a verbatim theorem from the source.',caption='Aaronson–Grier–Schaeffer, ITCS 2017, introduction pp.23:2–23:3 and footnote 3.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Classification of Reversible Bit Operations','Scott Aaronson; Daniel Grier; Luke Schaeffer',2017,'https://doi.org/10.4230/LIPIcs.ITCS.2017.23','Introduction pp.23:2–23:3 and footnote 3'),
 ref('ccc','Complexity Classification of Conjugated Clifford Circuits','Adam Bouland; Joseph F. Fitzsimons; Dax Enshan Koh',2018,'https://doi.org/10.4230/LIPIcs.CCC.2018.21','Introduction p.21:2; §6 pp.21:20–21:21; §7 pp.21:21–21:22'),
 ref('criterion','A Criterion for Post-Selected Quantum Advantage','Chaitanya Karamchedu; Matthew Fox; Daniel Gottesman',2025,'https://arxiv.org/abs/2411.02369v2','Revision of 22 October 2025, introduction pp.1–3; Theorems 5.14–5.15 p.23'),
 ],
 context_blocks=[
 block('The classical reversible-gate classification motivates a quantum analogue. The source distinguishes dense unitary generation from universality through an encoding, and asks whether other finite gate sets support intermediate computational behavior.'),
 block('Conjugated Clifford circuits illustrate why the output interface matters: their full output distribution can be difficult to sample under complexity assumptions, while individual output-bit probabilities have an efficient classical strong simulation. They therefore do not supply the required decision separation in this card’s single-output model.','ccc'),
 block('The October 2025 revision classifies weak multiplicative simulation for additional conjugated Clifford fragments, including commuting cases. Its quantum-advantage statements concern sampling and use a noncollapsing polynomial-hierarchy assumption; they do not establish either unconditional strict decision-class containment here.','criterion'),
 block('A positive answer would in particular prove P distinct from BQP. Conversely, simply assuming that separation, excluding Clifford conjugates, or showing a generated group is not dense does not prove the displayed intermediate-class assertion.'),
 ],
 progress=[
 progress('2017-01','The source poses the intermediate-gate-set question as part of the program of classifying quantum gate resources.'),
 progress('2018-06','The conjugated-Clifford classification separates joint sampling hardness from easy simulation of a single output marginal.','ccc'),
 progress('2025-10','The revised postselected-advantage criterion extends sampling classifications to additional Clifford fragments without resolving the selected decision-class problem.','criterion'),
 ],
),[
 'Applied the user-confirmed decision-class target and explicitly required both strict containments.',
 'Specified finite algebraic gate descriptions, uniform input-dependent generation, basis states, unrestricted placement and one final measured output qubit.',
 'Defined the Pauli normalizer and a common conjugating one-qubit unitary across the whole gate set.',
 'Separated sampling hardness, postselected power, physical nonuniversality and encoded BQP universality.',
 'Read the 2018 single-marginal simulation statement and the revised 2025 sampling classification; assessed importance individually and required a complete Lean-checked answer.',
],[
 'Read the ITCS 2017 introduction and its footnote distinguishing gate-set restrictions from other restricted quantum models.',
 'Read CCC 2018 §6, including the efficient strong(1) simulation and the contrast with joint distributions.',
 'Read the November 2024 criterion manuscript, checked the arXiv revision history, then downloaded and checked the 22 October 2025 revision introduction and Theorems 5.14–5.15.',
 'Bounded primary-source searches through 18 September 2026 found no resolution of the exact strict uniform decision-class target. Related sampling classifications were not promoted to decision separations.',
], 'The source’s gate-set program remains unresolved for this user-selected strict decision-class interpretation in the bounded checks through 18 September 2026. The displayed model is an explicit specialization of an informal question. The reviewed 2018 and October 2025 classifications concern classical simulation, often of joint samples under assumptions; they do not prove P strictly contained in Q_G strictly contained in BQP. No exhaustive current-status or independent full-proof validation is claimed.',summary=[
 'A finite quantum gate set determines which polynomial-size uniform circuits can be built from its operations.',
 'The user-selected question asks for a bounded-error decision class strictly larger than P and strictly smaller than BQP.',
 'The gates must also escape every common one-qubit conjugate of the Clifford group.',
 'The card fixes algebraic gates, computational-basis inputs and one final measured output bit to make the computational model precise.',
 'Known hardness results for sampling restricted circuits do not establish this stronger unconditional decision-class separation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
