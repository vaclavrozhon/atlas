"""Fix the hypothesis and quantum model for the explicit SVP lower bound."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0653';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A quantum 2^(0.2075n) lower bound for exact Euclidean SVP from QSETH',
 status='source_open',criterion='assumptions',question_type='yes_no',
 formal=r'''Does the Quantum Strong Exponential Time Hypothesis defined below imply that there are no constants \(K,a>0\) and no uniform bounded-error quantum algorithm which, for every explicitly given integer lattice basis of rank \(n\) and total binary input length \(L\), outputs an exact shortest nonzero vector using at most
\[
K\,2^{83n/400}(L+1)^a
\]
elementary operations on every execution? The exponent is the exact rational number \(83/400=0.2075\), and the norm is Euclidean.''',
 definitions=r'''An instance is a full-column-rank integer matrix \(B\in\mathbb Z^{m\times n}\), with \(m\ge n\ge1\). The dimensions and all signed entries are explicitly encoded in binary with delimiters; \(L\) is the complete encoding length. The lattice is
\[
\mathcal L(B)=\{Bz:z\in\mathbb Z^n\},\qquad
\lambda_1(\mathcal L(B))=\min_{z\in\mathbb Z^n\setminus\{0\}}\|Bz\|_2,
\quad \|v\|_2=\left(\sum_i v_i^2\right)^{1/2}.
\]
An acceptable classical output is a binary integer coefficient vector \(z\ne0\) with \(\|Bz\|_2=\lambda_1(\mathcal L(B))\). Either sign and any shortest vector are acceptable. The success probability must be at least \(2/3\) on each individual basis, over all internal measurements and randomness. No average-case or unique-shortest-vector promise is imposed. Reading the input and writing the output count toward the running time. The exponential parameter is the rank \(n\), not the ambient dimension \(m\) or the bit length \(L\).

Use the following uniform finite-gate quantum model for both the lattice problem and the hypothesis. A fixed classical multitape Turing machine controls qubits initialized to \(|0\rangle\), applies gates from \(\{H,T,T^{-1},\mathrm{CNOT}\}\), prepares fresh zero qubits, measures in the computational basis and finally writes a classical answer. Here \(H=2^{-1/2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\), \(T=\operatorname{diag}(1,e^{i\pi/4})\), and CNOT maps \(|u,v\rangle\) to \(|u,u\mathbin\oplus v\rangle\). The controller has the explicit classical input and may adapt to measurement outcomes. Each classical bit step, gate, preparation and measurement costs one operation. Gates may act on arbitrary finitely indexed qubits, but computing and writing their binary indices costs classical bit steps. There is no advice, postselection, external oracle or unit-cost coherent memory-lookup operation; any such lookup used by an algorithm must be implemented with counted gates. All classical control time is counted, and time is bounded on every measurement branch.

For an integer \(k\ge3\), a \(k\)-CNF formula is an explicitly listed conjunction of clauses, each a disjunction of at most \(k\) literals on \(N\) named Boolean variables. A literal is a variable or its negation. Let \(M\) be the complete binary encoding length. The Quantum Strong Exponential Time Hypothesis (QSETH) here is:
\[
\forall\varepsilon\in(0,1/2)\ \exists k\ge3:
\text{there is no uniform quantum algorithm deciding }k\text{-SAT}
\text{ in time }O\!\left(2^{(1/2-\varepsilon)N}(M+1)^b\right)
\]
for any constant \(b\), with error at most \(1/3\) on every formula. The algorithm and polynomial exponent may depend on \(k,\varepsilon\). The cost model is exactly the one above. Thus the reference exponent is \(1/2\), reflecting quantum search, rather than the classical exponent 1.

The card asks for the full logical implication from this specific hypothesis. It does not restrict a proof to many-one, nonadaptive or black-box reductions. Its conclusion excludes the displayed running time itself; it is not merely a statement that all still smaller exponents are impossible. The polynomial factor permits arbitrary explicit coefficient lengths.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the stated implication from QSETH, or prove its logical negation. A negative answer must establish QSETH together with an algorithm meeting the displayed time and per-input correctness guarantee. A barrier for a restricted family of reductions, a heuristic sieve cost, a lower bound only against classical algorithms, or an unspecified positive exponent does not settle this exact target.',
 why='Quantum attacks on lattice problems are often estimated from particular sieving algorithms. A rank-sensitive exponential lower bound under an independent SAT hypothesis would provide a much firmer basis for those estimates and would have to overcome substantial limitations of current reductions.',
 source_formulation=dict(text='Open Problem 2.6 asks for the absence of a 2^(0.2075n)-time quantum algorithm for exact Euclidean SVP under a standard complexity assumption. The preceding discussion describes quantum SETH. This card selects that hypothesis and an explicit uniform gate-cost convention, with a polynomial factor in the full binary input length.',caption='Bennett, The Complexity of the Shortest Vector Problem, §2.3 and Open Problem 2.6, printed pp.6–7 / PDF pp.8–9.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','§2.3, quantum algorithm estimates, Theorems 2.4–2.5 and Open Problem 2.6, printed pp.5–7 / PDF pp.7–9'),
 ref('barrier','On the (Classical and Quantum) Fine-Grained Complexity of Approximate CVP and Max-Cut','Jeremy Ahrens Huang; Young Kun Ko; Chunhao Wang',2026,'https://doi.org/10.4230/LIPIcs.ICALP.2026.111','ICALP 2026 conference version; abstract and §1.4 Our no-go theorems, pp.111:8–111:9'),
 ],
 context_blocks=[
 block('The source motivates 0.2075 from the space scale of plausible quantum sieving attacks. That motivation is an estimate for algorithmic approaches, not a lower bound against every quantum algorithm.'),
 block('The survey records exponential fine-grained hardness for several non-Euclidean norms and explains how quantum hypotheses change the SAT baseline by a factor of two. These results do not provide the requested Euclidean exponent.'),
 block('Its discussion already identifies obstacles to SAT-based proofs in the Euclidean norm. Selecting QSETH makes the target a particular conditional assertion rather than a search over unspecified assumptions.'),
 block('The ICALP 2026 paper extends a barrier to polynomial-size nonadaptive quantum reductions from SAT to Euclidean closest-vector problems, unless NP has the indicated quantum statistical zero-knowledge protocols. The theorem restricts reduction methods; it does not refute every QSETH implication or give a fast exact-SVP algorithm.','barrier'),
 block('The explicit finite-gate model counts coherent memory access when implemented and keeps the hypothesis and target in the same model. Consequently the card does not silently import an uncharged quantum-memory primitive from a heuristic algorithm estimate.'),
 ],
 progress=[progress('2023','The source poses the explicit Euclidean quantum exponent as Open Problem 2.6, with quantum SETH discussed immediately beforehand.'),progress('2026-07','The ICALP result adds a no-go theorem for a restricted class of quantum reductions to Euclidean CVP; it leaves the full selected implication unresolved.','barrier')],
),[
 'Applied the announced recommended QSETH and 0.2075 editorial default after an unanswered optional hypothesis-and-exponent question.',
 'Defined exact vector output, binary integer bases, lattice rank, per-instance bounded error and all-branch time.',
 'Used one explicit uniform finite-gate computation model in both QSETH and the target; counted classical control and memory-lookup implementations.',
 'Retained the exact numerical source target and the quantum one-half SAT baseline.',
 'Checked the July 2026 quantum reduction barrier, preserved assessed importance and supplied a full Lean-checked implication criterion.',
],[
 'Read the source’s algorithm estimates, quantum SETH paragraph, Theorems 2.4–2.5 and all of Open Problem 2.6 with its barrier and smaller-exponent qualifications.',
 'Downloaded and read the ICALP 2026 primary conference version, abstract and §1.4, checking the nonadaptive and complexity-collapse qualifications.',
 'Bounded primary-source searches through 17 September 2026 found no proof or refutation of the selected implication. The barrier is not recorded as a negative resolution.',
], 'The exact Euclidean quantum lower-bound target remains unresolved in the checked sources through 17 September 2026. The choice of QSETH was an announced editorial default after no reply to an optional question. The July 2026 barrier concerns restricted nonadaptive reductions and does not refute the unrestricted implication. The precise gate model and polynomial input-length factor are editorial specifications.',summary=[
 'Exact Euclidean SVP asks for a shortest nonzero vector of an explicitly given integer lattice.',
 'This card asks whether quantum SETH rules out time 2^(0.2075n) times a polynomial in the binary input length.',
 'The quantum SAT hypothesis uses the search baseline 2^(N/2), and both sides use the same uniform finite-gate model.',
 'Known barriers obstruct important families of reductions without resolving the full implication.',
 'A complete Lean-checked proof or refutation must establish the stated numerical exponent and computational guarantees.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
