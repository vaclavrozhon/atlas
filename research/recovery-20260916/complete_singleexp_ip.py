"""Complete deterministic single-exponential integer feasibility in dimension."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7264';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained exact feasibility for unrestricted rational inequalities and the previously selected deterministic bit-computation target.',
 'Specified the two input dimensions, full rational encoding length, empty-dimensional conventions and a single uniform algorithm with universal constants.',
 'Separated polynomial dependence on encoding length from a dependence on numerical magnitude, and excluded unstated boundedness, rank or structural promises.',
 'Checked the 27 March 2026 Reis–Rothvoss revision and made explicit that its general polylogarithmic-base exponential algorithm is randomized.',
 'Checked the 13 September 2026 standard-form ILP revision: its new 2^{O(k)} factor retains numerical determinant dependence and uses row rank as its exponential parameter.',
 'Preserved importance 94 and category, cleared two now-inactive related IDs without rereviewing their archived bodies, and required a complete Lean-checked unconditional resolution.',
]
sources=[
 'Read Koutecký, IPEC 2025 Article 1, A Brief History of Parameterized Algorithms for Block-Structured Integer Programs, §1 introduction, the paragraph beginning with a small number of variables and the explicit open 2^{O(n)} poly(L) question. The card retains the already selected deterministic feasibility specialization.',
 'Read Reis–Rothvoss, arXiv:2303.14605v5 of 27 March 2026, abstract p. 1, historical introduction p. 2, Theorems 4–5 pp. 4–5 and Corollary 6 p. 5. The algorithm is randomized; Corollary 6 applies to general rational A,b,c and has (log(2n))^{O(n)} times polynomial encoding length. The full revised proof was not independently audited.',
 'Read Dadush–Eisenbrand–Rothvoss, From approximate to exact integer programming, Mathematical Programming 210, 2025, pp. 223–241, published online 24 April 2024: §§1 and 1.3 explicitly retain the singly exponential general question, and §1.1 distinguishes supplied solution remainders and other restricted single-exponential cases. The abstract describes the pre-Reis–Rothvoss baseline; §1.3 records subsequent work, so the older abstract is not treated as the current bound.',
 'Read Gribanov–Khayaleyev–Cherniavskii–Klimenko–Malyshev–Moiseev, arXiv:2604.09806v4, revised 13 September 2026, primary abstract and version history. Its refined feasibility bound is 2^{O(k)} Delta up to polynomial input factors, for full-row-rank k-by-n standard-form integer matrices, where Delta is the maximum absolute full-rank minor. This replaces the weaker bound visible in older search snippets, but its determinant factor still prevents it from supplying the selected unrestricted bit-length bound. Full proof not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified deterministic single-exponential-in-dimension algorithm for all rational systems. Related-ID activity was checked only by canonical-file existence; TCS-4054 and TCS-4195 are inactive.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',related_problem_ids=[],
 formal=r'''Do there exist a real constant \(C>0\), an integer constant \(c\ge1\), and one uniform classical deterministic Turing machine \(A\) such that, for every pair of integers \(m,n\ge0\), every explicitly given rational matrix \(Q\in\mathbb Q^{m\times n}\) and every rational vector \(b\in\mathbb Q^m\), the machine correctly decides whether
\[
 \exists x\in\mathbb Z^n\quad Qx\le b
\]
within at most
\[
 2^{Cn}(L+1)^c
\]
bit operations, where \(L\) is the total binary encoding length of the input? The inequalities are componentwise, and there is no boundedness or coefficient-size promise beyond the finite explicit encoding.''',
 definitions=r'''The dimension parameter \(n\) is the number of integer variables, and \(m\) is the number of inequalities. Both are supplied with the input. The matrix entries and right-hand-side entries are given exactly as signed binary numerators and positive binary denominators, with explicit lengths or delimiters; entries need not be reduced to lowest terms. The entire matrix is listed in row-major order, followed by \(b\). The encoding length \(L\) includes all coefficients, dimensions, signs, denominators and delimiters. There is no succinct circuit or oracle representation of the inequalities.

The inequality \(Qx\le b\) means
\[
 \sum_{j=1}^{n}Q_{ij}x_j\le b_i
 \quad\text{for every }i\in\{1,\ldots,m\}.
\]
Every coordinate of \(x\) must be an integer, with no a priori bound on its magnitude or sign. Nonnegativity restrictions are present only if encoded among the inequalities. The underlying real polyhedron may be empty, unbounded, lower dimensional, or contain lines; the matrix may be rank deficient. No bound is imposed on the number of inequalities, determinant magnitudes or width of the feasible region. There is no objective function.

For \(n=0\), \(\mathbb Z^0\) contains the single empty vector, and feasibility means \(0\le b_i\) for every row. For \(m=0\), the conjunction of inequalities is empty and the instance is feasible. These conventions also cover the completely empty system.

The output is one exact Boolean answer: YES if an integer solution exists, and NO otherwise. Producing a feasible point or a separate infeasibility certificate is not required by this decision target. A positive answer cannot be based solely on real feasibility or on satisfying relaxed or numerically perturbed inequalities.

The computation uses a fixed finite deterministic multitape Turing-machine program, independent of \(m,n,L,Q,b\). Time is the number of bit-level machine steps. All reading, parsing, exact integer or rational arithmetic, storage operations and output are charged. Arithmetic on an arbitrarily large number is not one operation. Randomness, nonuniform advice, real-number primitives and uncharged optimization or separation oracles are not available.

The constants \(C\) and \(c\) are universal for that one program. In particular, the polynomial exponent on \(L\) may not depend on \(n\), and the exponential base may not grow with \(n\), coefficient magnitude or the number of rows. A polynomial factor in numerical coefficient or determinant magnitude can be exponential in its binary encoding length and therefore is not automatically permitted. Any implementation that uses such a factor must prove that its full bit cost nevertheless meets the displayed bound on every input.

The phrase single-exponential dependence on dimension refers to the factor \(2^{Cn}\). Bounds of the form \((\log(n+2))^{Dn}\) with a fixed \(D>0\) have a growing base and do not meet that dependence as stated. A family of unrelated algorithms, one for each fixed dimension, also does not suffice without one uniform machine and the required universal bounds.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the stated deterministic algorithm's existence or a complete Lean-checked proof of its logical negation.

A positive answer must establish exact feasibility decisions and the total bit-operation bound for every encoded rational system, including unbounded and lower-dimensional cases. If the method first converts the input to another formulation, its cost, encoding growth and dependence on the number of integer variables must all be accounted for. An optimization algorithm is sufficient only if its proved guarantees include this feasibility task and the specified bound.

A negative answer must rule out every admissible uniform deterministic program and all fixed constants \(C,c\) in the statement. A lower bound conditional on ETH, \(\mathrm P\ne\mathrm{NP}\) or another unproved assumption does not establish this unconditional negation. Excluding subexponential time \(2^{o(n)}\) does not exclude the requested single-exponential bound.

A randomized algorithm, an algorithm restricted to bounded coefficients or a special block structure, an approximate integer-feasibility procedure, or a bound exponential in a different parameter does not decide the selected target without a proved extension.''',
 source_formulation=dict(text='The survey asks whether general integer programming can be solved with single-exponential dependence on the number of variables and polynomial dependence on the full input encoding length. This card retains the approved deterministic decision formulation for explicit rational inequalities.',caption='Paraphrase of Koutecký, IPEC 2025 Article 1, §1, paragraph on a fixed number of variables; the deterministic convention is the retained card specialization.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A Brief History of Parameterized Algorithms for Block-Structured Integer Programs','Martin Koutecký',2025,'https://drops.dagstuhl.de/storage/00lipics/lipics-vol358-ipec2025/html/LIPIcs.IPEC.2025.1/LIPIcs.IPEC.2025.1.html','§1 introduction, paragraph on a small number of variables and the explicit 2^{O(n)} poly(L) open question'),
 ref('flatness','The Subspace Flatness Conjecture and Faster Integer Programming','Victor Reis; Thomas Rothvoss',2026,'https://arxiv.org/abs/2303.14605v5','27 March 2026 revision of the FOCS 2023 work; abstract p. 1, Theorems 4–5 pp. 4–5 and Corollary 6 p. 5; randomized general algorithm'),
 ref('approximate','From approximate to exact integer programming','Daniel Dadush; Friedrich Eisenbrand; Thomas Rothvoss',2025,'https://link.springer.com/article/10.1007/s10107-024-02084-1','Published online 24 April 2024, volume 210 (2025), pp. 223–241; §§1, 1.1 and 1.3, supplied-remainder special case and subsequent general bound'),
 ref('standard2026',r'Algorithms for Standard-form ILP Problems via Komlós’ Discrepancy Setting (Refined \(2^{O(k)}\)-analysis)','Dmitry Gribanov; Tagir Khayaleyev; Mikhail Cherniavskii; Maxim Klimenko; Dmitry Malyshev; Stanislav Moiseev',2026,'https://arxiv.org/abs/2604.09806v4','Revision of 13 September 2026; primary abstract, row-rank parameter k and numerical determinant factor Delta; proof not independently audited'),
 ],
 why='Integer feasibility is a general optimization primitive. A fixed exponential base in the number of variables would sharpen the dimension dependence of a widely used fixed-parameter algorithmic tool without restricting the coefficients or constraint structure.',
 context_blocks=[
 block('Fixed-dimensional integer programming is tractable, but the dimension dependence controls how broadly that fact can be used. The survey explicitly separates the single-exponential target from the known growing-base bound.'),
 block(r'The March 2026 Reis–Rothvoss version gives a randomized \((\log(2n))^{O(n)}\operatorname{poly}(L)\) algorithm. Its bound is general, but both its growing exponential base and its randomization must be distinguished from the deterministic target here.','flatness'),
 block('The approximate-to-exact work gives a single-exponential procedure with additional information about a solution, and records the unrestricted single-exponential question as open. Those extra inputs are not supplied in this card.','approximate'),
 block(r'The September 2026 standard-form revision states feasibility time \(2^{O(k)}\Delta\operatorname{poly}(L)\), where \(k\) is row rank and \(\Delta\) bounds full-rank minors. The numerical determinant factor can be large despite a short binary encoding, so this statement does not give the requested unrestricted bound.','standard2026'),
 ],
 progress=[progress('2023','The Reis–Rothvoss work improves general integer programming to a polylogarithmic-base exponential randomized bound.','flatness'),progress('2025','The survey explicitly retains the single-exponential dimension target as open.'),progress('2026-03-27','The revised general bound is checked with its randomized computation convention.','flatness'),progress('2026-09-13','A refined standard-form bound gives a single-exponential row-rank factor while retaining determinant-magnitude dependence.','standard2026')],
),notes,sources,'The bounded primary-source review through 17 September 2026 found no verified deterministic 2^{O(n)} poly(L) algorithm or unconditional impossibility theorem for unrestricted rational integer feasibility. The March 2026 general result remains randomized with a growing exponential base, and the September 2026 standard-form result retains a numerical determinant factor. The full revised proofs were not independently audited.',summary=[
 'The input is an explicit system of rational linear inequalities whose variables must all be integers.',
 'The task is exact feasibility, with no boundedness, rank or coefficient-size promise.',
 'The question asks for one deterministic algorithm with a fixed exponential base in the number of variables and a fixed polynomial dependence on input length.',
 'The checked general randomized bound and recent determinant-dependent bound do not supply that guarantee.',
 'An accepted answer must give a complete Lean-checked construction or unconditional impossibility proof in the bit-computation model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
