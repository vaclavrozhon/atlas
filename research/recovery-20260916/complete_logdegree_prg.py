"""Individual completion using the user's one-bit-saving convention."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1122'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Theory of Unconditional Pseudorandom Generators','Pooya Hatami; William M. Hoza',2023,
 'https://eccc.weizmann.ac.il/report/2023/019/revision/2/',
 'Revision 2, 14 April 2023; §1.4 explicitness; Theorem 2.4.2 and Open Problem 2.4.13, printed p. 29'),
 ref('viola','The Sum of d Small-Bias Generators Fools Polynomials of Degree d','Emanuele Viola',2009,
 'https://www.khoury.northeastern.edu/home/viola/papers/d.pdf',
 'Author version dated 15 April 2009; Theorem 2 and the following seed-length discussion, p. 2; Computational Complexity 18(2), 209–217'),
 ref('fractional','Fractional Pseudorandom Generators from Any Fourier Level','Eshan Chattopadhyay; Jason Gaitonde; Chin Ho Lee; Shachar Lovett; Abhishek Shetty',2020,
 'https://eccc.weizmann.ac.il/report/2020/121/revision/1/',
 'Revision 1; §4.1, Theorem 4.2 and its comparison with Viola’s construction'),
 ref('largefields','Optimal PRGs for Low-Degree Polynomials over Polynomial-Size Fields','Gil Cohen; Dean Doron; Noam Goldgraber',2026,
 'https://arxiv.org/abs/2602.10030v1',
 'Version 1, 10 February 2026; Definition 1.1, introduction and §1.1; the construction assumes sufficiently large field characteristic'),
]
notes=[
 'Applied the user’s 16 September choice: error 0.1, uniform polynomial time, and at least one saved seed bit for every sufficiently large n.',
 'Defined degree as floor(log2 n), with every multilinear polynomial over GF(2) of at most that degree allowed, including dense polynomials.',
 'Expanded both the probability guarantee and uniformity; no test polynomial, advice or extra randomness is supplied to the generator.',
 'Distinguished the chosen one-bit-saving target from stronger sublinear and polynomial-saving questions.',
 'Checked the scope of the February 2026 large-field result, which does not cover the binary field.',
]
sources=[
 'Read ECCC TR23-019 revision 2 Theorem 2.4.2 and Open Problem 2.4.13: the source says nontrivial without fixing the saved seed amount or error. Those choices were explicitly confirmed by the user.',
 'Read Viola’s April 2009 Theorem 2 and displayed seed bound O(d log n + d 2^d log(1/epsilon)); this does not give the selected saving at d=floor(log2 n).',
 'Read Chattopadhyay et al. revision 1 §4.1, Theorem 4.2 and its discussion: the alternative construction also retains exponential dependence on degree.',
 'Read Cohen–Doron–Goldgraber arXiv 2602.10030v1 abstract, Definition 1.1 and introduction/result scope. Its larger-characteristic construction does not instantiate over GF(2); the binary reduction is conditional on a different characteristic-unrestricted construction.',
 'Checked the 2024 published survey copy, Open Problem 2.2, and bounded later primary sources through 16 September 2026; no resolution of the chosen target was found. Related proofs were not fully reconstructed.',
]
status=('The source leaves “nontrivial” quantitative conventions unspecified. '
 'On 16 September 2026 the user selected saving at least one bit at error 0.1 in uniform polynomial time. '
 'The checked binary-field constructions do not achieve that guarantee at degree floor(log2 n). '
 'The February 2026 optimal-seed theorem concerns fields of sufficiently large characteristic, not GF(2). '
 'No resolution of this precise selected target was found in the bounded review.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a uniform explicit generator family
\[
G_n:\{0,1\}^{s(n)}\longrightarrow\{0,1\}^{n}
\]
and an integer \(n_0\ge2\) such that, for every integer \(n\ge n_0\),
\[
s(n)\le n-1
\]
and every polynomial \(p:\mathbb F_2^n\to\mathbb F_2\) of total degree at most \(d(n)=\lfloor\log_2 n\rfloor\) satisfies
\[
\left|\Pr_{Y\sim U_{s(n)}}[p(G_n(Y))=1]
-\Pr_{X\sim U_n}[p(X)=1]\right|\le\frac1{10}?
\]
The same generator must fool all such polynomials at that length. The seed saving is required at every sufficiently large length, not merely infinitely often.''',
 definitions=r'''\(\mathbb F_2=\{0,1\}\) is the field with addition modulo two and ordinary bit multiplication. On Boolean inputs every polynomial has a unique multilinear representation
\[
p(x)=\sum_{\substack{S\subseteq\{1,\ldots,n\}\\|S|\le d(n)}}a_S\prod_{i\in S}x_i,
\qquad a_S\in\mathbb F_2,
\]
where the empty product is one and the sum is computed modulo two. The test class consists of all coefficient choices in this display, including the zero and constant polynomials. There is no bound on the number of nonzero monomials or on the size of a circuit computing the test. “Degree” is the largest monomial size in this multilinear representation; the zero polynomial is included by convention.

\(U_r\) is uniform on the \(r\)-bit strings, also allowing \(r=0\). The input bits and polynomial values are identified with field elements. Because a test has two possible outputs, the displayed absolute difference is also the total-variation distance between its two output distributions.

Uniform explicitness means that fixed deterministic Turing machines \(S,G\) compute \(s(n)\) from \(1^n\), and \(G_n(y)\) from \((1^n,y)\), respectively, in at most \(Cn^k\) bit operations for some fixed \(C>0\) and integer \(k\ge1\). The polynomial \(p\) is not an input. Neither machine receives advice or an oracle, and the generator has no random bits beyond its seed. The machines and seed lengths are defined for every \(n\ge2\); the probability and saving requirements apply for \(n\ge n_0\).

The threshold \(n_0\), running-time constants and machines are existentially quantified once for the whole family. Saving at least one bit is the user-selected meaning of nontrivial. It does not impose \(s(n)=o(n)\) or a bound \(n^{1-\delta}\) with fixed \(\delta>0\). Unused seed bits may be added, so a shorter qualifying seed may equivalently be padded to length \(n-1\).''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of this existence assertion. A positive answer must specify the uniform algorithms and a threshold, and prove the running time, seed saving and error simultaneously for every allowed polynomial at every sufficiently large length. A negative answer must rule out the full family of such algorithms, not just sums of small-bias generators or another selected template. This binary question has no numerical \(1/100\) tolerance. Smaller constant degrees, sparse polynomials, larger fields, or infinitely many successful lengths do not meet the stated target.''',
 source_formulation=dict(text=r'The source asks for a polynomial-time explicit generator for binary polynomials of logarithmic degree that uses fewer random bits than its output. The user fixed the benchmark to one saved bit eventually, at error \(1/10\).',
 caption='Editorial paraphrase of Open Problem 2.4.13; the quantitative meaning of nontrivial was selected by the user on 16 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='Binary polynomial tests describe algebraic correlations of increasing order. At logarithmic degree the standard seed bounds stop giving a guaranteed saving, even though they are very effective at fixed degree. Resolving the selected minimal saving would cross that precise boundary without assuming the much stronger goal of a polylogarithmic seed.',
 references=refs,
 context_blocks=[
 block('Linear tests are parities of subsets of the input bits. Higher-degree tests can also multiply bits before taking their parity. The degree bounds how many distinct variables appear in one monomial, while the number of monomials can still be very large.'),
 block(r'Viola’s construction has seed \(O(d\log n+d\,2^d\log(1/\varepsilon))\) in the displayed analysis. For fixed degree and error this is logarithmic in \(n\). At \(d=\lfloor\log_2 n\rfloor\), the exponential degree term prevents that guarantee from proving even a one-bit saving. This is a limitation of the bound, not a general lower bound on generators.','viola'),
 block('The 2020 fractional-generator analysis provides a different construction while retaining exponential dependence on the degree. Its comparison with the earlier bound highlights the same logarithmic-degree obstruction. It does not prove impossibility beyond that regime.','fractional'),
 block('Over larger finite fields the relationship between degree and field size is different. The February 2026 paper reduces the field size needed for an optimal-seed construction, but retains a sufficiently large characteristic assumption. Since this card fixes characteristic two, that theorem does not provide a solution.','largefields'),
 block('A distribution supported on fewer than all bit strings can still approximate every test in a restricted class. The hard part here is producing such a distribution uniformly in polynomial time with a proof covering every logarithmic-degree polynomial. A separate generator chosen for each individual test would have a different quantifier order.'),
 block('The source’s qualitative word “nontrivial” allows several stronger interpretations. This card records the user’s least-demanding seed-saving choice explicitly, so future progress can be assessed against one definite statement rather than a moving asymptotic target.'),
 ],
 progress=[
 progress('2009-04-15','Viola’s displayed bound gives efficient short seeds at fixed degree, with exponential dependence on degree.','viola'),
 progress('2020','The fractional-generator result obtains another construction with exponential degree dependence.','fractional'),
 progress('2023-04-14','The survey poses the logarithmic-degree nontrivial-generator question.'),
 progress('2026-02-10','The new optimal-seed result applies over polynomial-size fields of sufficiently large characteristic, outside the fixed binary-field target.','largefields'),
 progress('2026-09-16','The user selects error one tenth and at least one saved bit at every sufficiently large length; individual review supplies the complete model.'),
 ],
),notes,sources,status,summary=[
 'The tests are all binary polynomials of degree at most the floor of log₂ n, without a sparsity restriction.',
 'One uniform polynomial-time generator must preserve every test’s output probability within one tenth.',
 'The user-selected goal is to save at least one random bit at every sufficiently large output length.',
 'Known binary-field constructions in the checked sources retain exponential dependence on degree.',
 'The 2026 optimal-seed construction over larger-characteristic fields does not settle this binary-field target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
