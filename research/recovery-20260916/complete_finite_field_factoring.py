"""Complete the unconditional uniform finite-field factorization target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6614'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved deterministic worst-case polynomial bit time for all explicitly represented finite fields and dense inputs.',
 'Specified the supplied irreducible field modulus, exact residue representation, multiplication and complete factorization with multiplicities.',
 'Made one algorithm and one absolute polynomial bound uniform in degree, characteristic and extension degree; all preprocessing and output count.',
 'Distinguished promised field input from construction of its modulus, and factorization from irreducibility testing or root finding alone.',
 'Added the March 2026 decoding revision and checked the sparse-factorization oracle and characteristic dependence.',
 'Required complete Lean-checked algorithm correctness and complexity, or impossibility; preserved the assessed importance 95.',
]
sources=[
 'Read Altman, arXiv:2509.12705v1 (16 September 2025), abstract and §1 pp. 1–3, Theorem 1.1 and comparison with other factoring algorithms. Checked the arXiv submission history, which still lists v1. Its amortized algorithm ranges over primes and depends on splitting-field degree; the introduction explicitly retains general polynomial time as open even under GRH.',
 'Read Guo, author manuscript dated 16 November 2019, §1 and §1.1–1.2 pp. 1–3, complete versus proper factorization, the all-field input-size convention and conditional Galois-group restrictions. Published in Journal of Symbolic Computation (2020), DOI 10.1016/j.jsc.2019.02.011.',
 'Read Chatterjee–Harsha–Kumar, ECCC TR25-170 revision 1 (25 March 2026), abstract and §1 pp. 2–4, Theorem 1.1 and the factorization barrier discussion. Checked the author publication page for STOC 2026, pp. 2040–2051, DOI 10.1145/3798129.3800908. The algorithm uses additional received-word information for special bivariate instances; full proofs were not independently certified.',
 'Read Chuyoon–Shpilka, ECCC TR26-036 (8 March 2026), Remark 1.7 and §2.2 pp. 13–14, Theorems 2.7–2.8. The deterministic bound includes polynomial dependence on the characteristic, and the multivariate result explicitly charges univariate factorization.',
 f'Bounded primary-source searches through {DATE} found no unrestricted deterministic polynomial-bit-time factorization algorithm. The abstract and submission history of Umans–Wang, arXiv:2511.10851v1, were also checked: its conditional improvement to the degree exponent is not a general derandomization theorem and is not used as a resolution.',
]
status='The checked sources retain unconditional deterministic polynomial-time factorization over arbitrary finite fields as open. The 2026 list-decoding algorithm solves specially structured factorization instances with extra information. The recent sparse-factorization theorem retains characteristic or univariate-oracle costs, and neither gives the uniform bound required here.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2026,
 formal=r'''Does there exist one deterministic Turing algorithm \(A\) and absolute integers \(K,d\ge1\) such that, for every valid explicit field representation \(\mathbb F_q=\mathbb F_p[t]/(h(t))\) and every dense polynomial \(f\in\mathbb F_q[x]\) of degree \(n\ge1\), the algorithm outputs the complete irreducible factorization of \(f\) in at most
\[
K\bigl(n+\lceil\log_2q\rceil+1\bigr)^d
\]
bit operations?

The input includes the prime \(p\), the supplied monic irreducible field modulus \(h\), and every coefficient of \(f\). The algorithm and the constants are independent of \(n,p,h\) and \(f\), and no unproved number-theoretic assumption is allowed.''',
 definitions=r'''Let \(p\ge2\) be a prime, let \(e\ge1\), and let \(h(t)\in\mathbb F_p[t]\) be a monic irreducible polynomial of degree \(e\). The field \(\mathbb F_p\) is the integers modulo \(p\), and \(\mathbb F_q=\mathbb F_p[t]/(h(t))\), where \(q=p^e\), is the field of residue classes modulo \(h\). Its elements are represented uniquely by polynomials of degree less than \(e\), with each coefficient in \(\{0,\ldots,p-1\}\). Addition and multiplication mean polynomial addition and multiplication followed by reduction modulo \(p\) and \(h\).

The input writes \(p,e,n\) in binary, all coefficients of \(h\), and all \(n+1\) coefficients of \(f(x)=\sum_{j=0}^n a_jx^j\), with \(a_n\ne0\). Each field coefficient uses its full \(e\)-tuple of residues, each residue occupying \(\lceil\log_2p\rceil\) bits. Integer and array boundaries use a fixed unambiguous encoding. In particular, the polynomial is dense: zero coefficients are present, and neither a circuit nor an evaluation oracle substitutes for the coefficient list. The field representation is also part of the counted input, rather than fixed advice. Primality of \(p\) and irreducibility and degree of \(h\) are promises; constructing \(h\) from \(p,e\) is not an additional output task. No correctness condition is imposed on malformed or unpromised inputs.

A nonconstant polynomial \(g\in\mathbb F_q[x]\) is irreducible if it cannot be written as the product of two polynomials of positive degree over this same field. Monic means that its leading coefficient is one. A complete factorization consists of a nonzero field element \(u\), a list of pairwise distinct monic irreducible polynomials \(g_1,\ldots,g_r\) of positive degree, and positive binary integers \(m_1,\ldots,m_r\), satisfying the exact polynomial identity
\[
f=u\prod_{i=1}^r g_i^{m_i}.
\]
All factors are written as dense coefficient lists in the supplied field representation. The order of factors is irrelevant. Multiplicities are required, including for repeated factors in positive characteristic; there is no square-free or separability promise. Merely deciding irreducibility, returning a proper factor, or finding roots when they exist is not the specified output.

Time is worst-case deterministic bit time on a standard multitape Turing machine. Reading, arithmetic, conversions, preprocessing and writing the factorization all count. The full input length is polynomially related to \(n+\lceil\log_2q\rceil+1\), so the displayed bound is equivalent to a single polynomial bound in that length. It is not polynomial dependence on the numerical value of \(p\) or \(q\). There is no random tape, oracle, uncharged field operation or family of field-specific algorithms. Extension degree and characteristic may both grow with the input.

The target is an existence proposition about an exact symbolic factorization algorithm. Absolute numerical approximation does not replace the polynomial identity or irreducibility conditions.''',
 answer_criterion=r'''Supply an algorithm and a complete Lean-checked proof that it terminates with the specified complete factorization on every valid input and obeys one bound of the displayed form. Alternatively, supply a complete Lean-checked proof that no deterministic algorithm with any such absolute polynomial bound exists.

An expected-time randomized algorithm, an average over inputs or primes, polynomial dependence on the field cardinality or characteristic, a restriction on degree or Galois group, or a bound conditional on an unproved hypothesis does not settle this proposition. The failure of a particular method is not a proof of the negative answer.''',
 source_formulation=dict(text='Altman’s introduction asks for deterministic factorization into irreducibles in time polynomial in the degree and the logarithm of the prime, and states that no such general algorithm is known. Guo’s introduction states the corresponding complete-factorization question over arbitrary finite fields. The card makes their input-size convention explicit for a supplied polynomial-basis field representation.',caption='Paraphrase of Altman, §1 pp. 1–3, and Guo, §1–1.1 pp. 1–2.',citation='primary',format='editorial_paraphrase'),
 why='Finite-field factorization is a basic operation in computer algebra and coding theory. Randomized polynomial-time algorithms are available, while a deterministic algorithm must handle every coefficient list and every characteristic without trying a number of possibilities proportional to the field size. The question isolates a central derandomization gap in an exact algebraic task.',
 references=[
 ref('primary','Deterministic polynomial factorisation modulo many primes','Daniel Altman',2025,'https://arxiv.org/abs/2509.12705v1','Version 1, 16 September 2025; §1 pp. 1–3, input-size convention, Theorem 1.1 and comparison with deterministic GRH-based algorithms'),
 ref('guo','Deterministic polynomial factoring over finite fields: a uniform approach via P-schemes','Zeyu Guo',2020,'https://zeyuguo.bitbucket.io/papers/pscheme.pdf','Journal of Symbolic Computation, DOI 10.1016/j.jsc.2019.02.011; author manuscript dated 16 November 2019; §1–1.2 pp. 1–3'),
 ref('decoding','Deterministic list decoding of Reed-Solomon codes','Soham Chatterjee; Prahladh Harsha; Mrinal Kumar',2026,'https://eccc.weizmann.ac.il/report/2025/170/revision/1/','ECCC TR25-170 revision 1, 25 March 2026; §1 pp. 2–4 and Theorem 1.1; STOC 2026, 2040–2051, DOI 10.1145/3798129.3800908'),
 ref('sparse','On Factorization of Sparse Polynomials of Bounded Individual Degree','Aminadav Chuyoon; Amir Shpilka',2026,'https://eccc.weizmann.ac.il/report/2026/036/','ECCC TR26-036, 8 March 2026; Remark 1.7 and §2.2 pp. 13–14, Theorems 2.7–2.8'),
 ],
 context_blocks=[
 block('The field representation tells the algorithm how to perform exact arithmetic. Factoring the supplied polynomial asks for its irreducible building blocks over that field, including multiplicities. Factors over a larger extension field would be a different output.','guo'),
 block('Randomized polynomial-time factorization is classical. Unconditional deterministic bounds can depend polynomially on the characteristic, which is too costly when the characteristic is large relative to its binary encoding.','guo'),
 block('Altman factors reductions of one integer polynomial across many primes with an amortized guarantee depending on its splitting-field degree. This does not give the requested worst-case bound for an arbitrary polynomial over one input field.'),
 block('The general problem also remains open under the Generalised Riemann Hypothesis in the inherited account. Conditional quasipolynomial or special-Galois-group algorithms therefore should not be described as a full conditional solution.'),
 block('The 2026 Reed–Solomon decoding result removes randomness for the special factorization instances arising there by using information from the received word. It explicitly retains arbitrary univariate factorization as an open problem.','decoding'),
 block('The recent sparse-polynomial result states that its bounds must include the cost of univariate factorization. Its finite-field preliminary theorem gives polynomial dependence on the characteristic, not only on its logarithm.','sparse'),
 ],
 progress=[
 progress('2019–2020','The P-scheme framework supplies GRH-based algorithms for specified Galois groups while retaining the general derandomization problem.','guo'),
 progress('2025-09-16','An amortized deterministic algorithm across primes is obtained with dependence on the splitting-field degree.'),
 progress('2026-03-08','Sparse-factorization bounds explicitly retain univariate factorization and characteristic costs.','sparse'),
 progress('2026-03-25','The revised list-decoding paper gives deterministic polynomial time for its special instances; published at STOC 2026.','decoding'),
 ],
),notes,sources,status,summary=[
 'The input is a densely written polynomial over a finite field whose polynomial-basis representation is supplied.',
 'The requested output is every monic irreducible factor, its multiplicity, and the original leading scalar.',
 'One deterministic algorithm must run in time polynomial in the degree and the logarithm of the field size for all valid inputs.',
 'Randomized methods, special decoding instances, averages over primes and characteristic-dependent bounds do not provide that guarantee.',
 'A complete Lean-checked proof must establish both universal correctness and the uniform bit-time bound, or prove their impossibility.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
