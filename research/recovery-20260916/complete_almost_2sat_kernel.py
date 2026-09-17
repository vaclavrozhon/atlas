"""Complete the deterministic polynomial-time Almost 2-SAT kernel question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6749'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the precise clause-deletion problem from §6 and the first question of §8 of the original chapter.',
 'Corrected the source’s stray r-SAT notation in §8 to 2-SAT, as confirmed by its name and preceding definition.',
 'Specified literal and repeated-clause semantics, an explicit finite encoding, and the deletion budget as the only parameter.',
 'Required one deterministic polynomial-bit-time map to an equivalent instance of the same problem with polynomial total encoding length.',
 'Separated the 2025 quasipolynomial-time deterministic result from the polynomial-time target.',
 'Assessed importance individually from the common derandomization barrier in matroid-based kernelization.',
]
sources=[
 'Read Gutin–Yeo, Parameterized Constraint Satisfaction Problems: a Survey, Dagstuhl Follow-Ups 7 (2017), Chapter 7: §2, printed p. 182/PDF p. 4, kernel definitions; §6, printed p. 196/PDF p. 18, r-Sat-B(m) definition and the r=2 paragraph; §8, printed p. 201/PDF p. 23, first open problem. The source’s §8 writes r-Sat-B(m) but calls it Almost 2-Sat; the preceding discussion and inherited title fix r=2. Publisher metadata confirms 21 February 2017.',
 'Read Gurjar–Lokshtanov–Misra–Panolan–Saurabh–Zehavi, MFCS 2025, Article 54: abstract, introduction pp. 54:2–4, §3.2 and §4 pp. 54:13–14, especially Proposition 28 and Theorem 30. The deterministic kernel has polynomial size but quasipolynomial running time. The introduction explicitly identifies polynomial-time derandomization as open. Some representation proofs are deferred to the full version; no independent proof certification is claimed here.',
 f'Bounded searches through {DATE} for deterministic Almost 2-SAT kernels found the MFCS 2025 result and later work on different local or oracle-assisted kernelization models, but no polynomial-time deterministic resolution of this exact target.',
]
status='The 2017 chapter asks for a deterministic polynomial kernel for clause-deletion Almost 2-SAT. MFCS 2025 gives a polynomial-size kernel in deterministic quasipolynomial time and explicitly distinguishes the still-open polynomial-time derandomization. The bounded later-work check found no resolution of the simultaneous size and polynomial-time requirements.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does clause-deletion Almost 2-SAT admit a deterministic polynomial kernel parameterized by the number \(k\) of permitted clause deletions?

Precisely, do there exist a uniform deterministic algorithm \(K\), an integer \(C\ge1\), and integers \(a,b\ge0\) such that, on every encoded instance \((F,k)\) of length \(L\), the algorithm runs for at most \(C(L+1)^a\) bit-machine steps and outputs an instance \((F',k')\) of the same problem satisfying
\[
(F,k)\in\mathcal A_2\quad\Longleftrightarrow\quad(F',k')\in\mathcal A_2,
\qquad
|\operatorname{enc}(F',k')|\le C(k+1)^b?
\]
Here \(\mathcal A_2\) and the encoding are defined below. The algorithm and constants must work for every formula and every nonnegative budget.''',
 definitions=r'''A literal is a Boolean variable \(x_i\) or its negation \(\neg x_i\). A clause is the disjunction of at most two literal occurrences, and a 2-CNF formula \(F=(C_1,\ldots,C_m)\) is a finite list of clauses interpreted conjunctively. The empty disjunction is false and the empty conjunction is true. Repeated clauses remain separate occurrences: each copy costs one deletion. Repeated literals and tautological clauses are allowed. All clauses have unit deletion cost; binary-encoded weights are not part of this input model.

An instance consists of such a formula and an integer \(k\ge0\). Write \((F,k)\in\mathcal A_2\) if there are a set \(D\subseteq[m]\) with \(|D|\le k\) and an assignment \(z\in\{0,1\}^n\) satisfying every clause whose index is outside \(D\). Equivalently, one assignment makes at most \(k\) clause occurrences false. Variables are renamed \(x_1,\ldots,x_n\), each appearing somewhere in the formula; \(n=0\) is allowed. Deleting variables, changing literal values independently in different occurrences, or merely finding an approximately minimum deletion set does not define this decision problem.

Fix the following binary encoding. For a nonnegative integer \(u\), let \(w(u)\) be the ordinary binary representation of \(u+1\), let \(h(u)=|w(u)|\), and put \(\operatorname{code}(u)=1^{h(u)}0w(u)\). Encode an instance by \(\operatorname{code}(n)\operatorname{code}(m)\operatorname{code}(k)\), followed by its \(m\) clauses in order. Each clause starts with the code of its length in \(\{0,1,2\}\); each literal is then a sign bit followed by \(\operatorname{code}(i)\) for its variable index \(i\in[n]\). A sign bit zero denotes \(x_i\), and one denotes \(\neg x_i\). There are no trailing bits. The output uses the same encoding, with its own densely renamed variables. This makes the size bound a bound on the complete instance, including variable names, all clause occurrences and the new budget.

The machine is a deterministic multitape Turing machine over fixed finite alphabets, with a fixed finite program, a read-only input tape, initially blank work tapes and a write-only output tape. Each transition accesses only the cells under the heads and moves each head by at most one cell. Time counts parsing, all arithmetic and output writing. It has no random bits, advice, oracle or uncharged preprocessing. Malformed strings are rejected in polynomial time in their length.

The output parameter can be required to satisfy \(0\le k'\le m'\), where \(m'\) is its number of clauses: replacing a larger budget by \(m'\) preserves the answer. Consequently the total-size bound also bounds \(k'\) by a polynomial in \(k\). The output may introduce variables and clauses and need not be a subformula of the input. Only exact equivalence of the yes/no answers is required, not recovery of a particular input assignment.

Both exponents are fixed independently of \(k,n,m\). A bound \(f(k)L^a\) with unrestricted \(f\), or \(L^{O(\log L)}\), does not meet the running-time requirement. The kernel need not decide whether its output is a yes-instance; that smaller instance can be solved separately. A bound only on the number of variables is insufficient unless the complete encoding is also polynomially bounded in \(k\).''',
 answer_criterion=r'''Give a complete Lean-checked construction of \(K,C,a,b\), proving termination within the stated polynomial time, the output-size bound, and exact equivalence for every input instance; or give a complete Lean-checked proof that no such algorithm and constants exist. Randomized correctness, quasipolynomial preprocessing time, a polynomial-size compression whose target is not shown to convert to this decision problem, or a kernelization lower bound conditional on an unproved complexity hypothesis does not settle the stated existence question. No optimization of the polynomial degree is required.''',
 source_formulation=dict(
 text='The chapter asks whether Almost 2-SAT has a deterministic polynomial kernel. Its preceding definition asks for an assignment satisfying all but at most the parameter number of clauses.',
 caption='Paraphrase of Chapter 7, §6, printed p. 196, and the first question in §8, printed p. 201; individual chapter PDF pp. 18 and 23.',
 citation='primary',format='editorial_paraphrase'),
 why='A kernel compresses a large instance to a size governed only by its distance from satisfiability. Randomized algebraic methods provide this guarantee for Almost 2-SAT, but removing randomness while retaining polynomial preprocessing time is a central test of those methods. A resolution would clarify whether an important family of efficient data-reduction guarantees inherently depends on random choices.',
 importance=dict(score=82,method='editorial',
 reason='A canonical derandomization problem for polynomial kernelization, linked to broadly used matroid representations and explicitly singled out across the 2017 survey and 2025 work.',
 assessed_on=DATE,basis='Individual reading of the precise source question, kernel definitions and the later quasipolynomial-time derandomization.'),
 references=[
 ref('primary','Parameterized Constraint Satisfaction Problems: a Survey','Gregory Gutin; Anders Yeo',2017,
 'https://drops.dagstuhl.de/entities/document/10.4230/DFU.Vol7.15301.179',
 'The Constraint Satisfaction Problem: Complexity and Approximability, Chapter 7, pp. 179–203; published 21 February 2017; §2 p. 182, §6 p. 196, §8 p. 201'),
 ref('quasi','Quasipolynomial-Time Deterministic Kernelization and (Gammoid) Representation',
 'Rohit Gurjar; Daniel Lokshtanov; Pranabendu Misra; Fahad Panolan; Saket Saurabh; Meirav Zehavi',2025,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.54',
 'MFCS 2025, Article 54, published 20 August 2025; introduction pp. 54:2–4 and §4, Proposition 28 and Theorem 30, p. 54:14'),
 ],
 context_blocks=[
 block('The source distinguishes finding a small equivalent instance from solving the instance outright. The preprocessing must take polynomial time in the original input length, while the output size depends only on the deletion budget.'),
 block('Almost 2-SAT is fixed-parameter tractable, and the source records a randomized polynomial kernel due to Kratsch and Wahlström. These two facts leave the deterministic polynomial-time compression question open.'),
 block('The 2025 theorem gives deterministic polynomial-size kernels for Almost 2-SAT and several related deletion problems. Its extra cost lies in quasipolynomial running time, which is outside the requirement here.','quasi'),
 block('The later work ties this collection of derandomization questions to deterministic representations of gammoids and to representative-set computations. It explicitly identifies polynomial-time derandomization as a central remaining question.','quasi'),
 ],
 progress=[
 progress('2017-02-21','The survey explicitly records deterministic polynomial kernelization for Almost 2-SAT as an open problem.'),
 progress('2025-08-20','Theorem 30 obtains polynomial-size kernels deterministically when quasipolynomial preprocessing time is allowed.','quasi'),
 progress(DATE,'The review specifies the clause-occurrence deletion model and checks the exact polynomial-time versus quasipolynomial-time distinction without finding a resolution.'),
 ],
),notes,sources,status,summary=[
 'Almost 2-SAT asks whether deleting at most a specified number of clauses can make a Boolean formula with at most two literals per clause satisfiable.',
 'The question asks for deterministic polynomial-time preprocessing that replaces any instance by an equivalent smaller instance of the same problem.',
 'The complete output size must be bounded by a fixed polynomial in the deletion budget alone.',
 'Randomized polynomial kernels are known, and a 2025 result obtains deterministic polynomial-size kernels with quasipolynomial preprocessing time.',
 'The remaining target requires both polynomial time and polynomial output size, with exact correctness for every input.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
