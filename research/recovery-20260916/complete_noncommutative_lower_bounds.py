"""Review explicit-family lower bounds for unrestricted noncommutative circuits."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6890';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a family
\[
f_n\in\mathbb Q\langle x_1,\ldots,x_n\rangle\qquad(n\ge2)
\]
of polynomial degree with uniformly polynomial-time computable word coefficients, such that
\[
\forall k\ge1\ \forall N\ge2\ \exists n\ge N:
\operatorname{NC}_{\mathbb C}(f_n)>n^k?
\]
Here \(k,N,n\) are integers and \(\operatorname{NC}_{\mathbb C}\) is minimum size among unrestricted noncommutative arithmetic circuits with arbitrary complex constants. The family can be chosen freely subject to the explicitness and degree requirements below; it is not required to be a particular permanent or determinant family.''',
 definitions=r'''The free associative algebra \(\mathbb C\langle x_1,\ldots,x_n\rangle\) consists of finite complex linear combinations of words in the symbols \(x_1,\ldots,x_n\). Addition adds the coefficients of equal words. Multiplication concatenates words and distributes over sums; it is associative. Scalars commute with every word, but variable symbols do not commute. The empty word has value 1. Thus \(x_1x_2\) and \(x_2x_1\) are different monomials, and polynomial equality is exact equality of every word coefficient. This is not a problem about functions on scalar inputs or on matrices of one fixed dimension.

A circuit is a finite directed acyclic graph with one output. Input gates are variable symbols or arbitrary complex constants. An internal gate adds or multiplies two predecessor values. Each multiplication gate specifies a left and a right input; the same predecessor may occur in both positions. The size is the total number of gates, including inputs. There are no division gates, tests, approximation operations or limits. Fan-out, reuse of intermediate values and depth are unrestricted. Each scalar costs one input gate without a description-length restriction. Intermediate polynomials can have arbitrarily large degree and need not be homogeneous. \(\operatorname{NC}_{\mathbb C}(f)\) is the minimum size of any such circuit whose formal output is \(f\), with rational coefficients embedded in \(\mathbb C\).

Polynomial degree and uniform explicitness mean that there are fixed integers \(a,b\ge1\), a fixed real \(K>0\), and one deterministic multi-tape Turing machine \(M\) with the following properties. Every nonzero \(f_n\) has degree at most \(n^a\), where degree is the largest length of a word with nonzero coefficient; the zero polynomial is allowed. Given \(1^n\) and any explicitly listed word \(w\) of length \(\ell\) over \(\{1,\ldots,n\}\), \(M\) outputs the exact coefficient \([w]f_n\) in at most
\[
K\bigl(n+(\ell+1)\lceil\log_2(n+1)\rceil\bigr)^b
\]
Turing steps. Word symbols are written as fixed-width binary indices. The output is a reduced fraction \(p/q\) with binary integers \(p\), \(q>0\), and \(\gcd(|p|,q)=1\); zero is \(0/1\). Words of length greater than \(n^a\) have coefficient zero. The empty word is included. The bound includes writing the output and thus also limits coefficient bit lengths. No advice depending on \(n\) is supplied to \(M\).

The explicitness requirement prevents choosing arbitrary hard coefficient tables by counting. It concerns an algorithm to compute any one coefficient, not an algorithm to list all coefficients or a small arithmetic circuit for the full polynomial. Conversely, the circuits being ruled out are nonuniform and may use complex constants even though the target family has efficiently computable rational coefficients. The lower-bound quantifiers mean absence of every polynomial family-size upper bound, witnessed at arbitrarily large indices; they do not require an eventual lower bound at every index.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of this existence statement or its logical negation. A positive answer must define the family and its coefficient algorithm, prove the degree and uniform running-time bounds, and exclude every polynomial circuit-size upper bound in the stated unrestricted model. A negative answer must prove that every family meeting these requirements has a polynomial-size noncommutative circuit family over \(\mathbb C\). An exponential formula or branching-program lower bound does not suffice. Nor does a circuit lower bound for bounded depth, homogeneity, restricted syntactic degree, or a fixed polynomial exponent.''',
 why='Noncommutative computation retains the order of products and already supports strong formula lower bounds. Proving a superpolynomial bound that survives unrestricted reuse would establish a major circuit lower-bound milestone for an explicitly specified family.',
 importance=dict(score=89,method='editorial',reason='A central explicit algebraic circuit lower-bound challenge with unrestricted depth and sharing, still substantially beyond the polynomial unrestricted-circuit progress reported in 2026.'),
 source_formulation=dict(text='Open Problem 10 asks for superpolynomial noncommutative circuit lower bounds in the surrounding discussion of explicit polynomial-degree families. This card specifies efficient rational coefficient access and lower bounds over C. The 2021 source occurrence reiterates the general circuit challenge before addressing different restricted-model questions.',caption='Shpilka–Yehudayoff, §3.4, Theorem 3.6 and Open Problem 10, printed pp.29–30; Chatterjee, CCC 2021, Introduction p.7:2.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Arithmetic Circuits: A Survey of Recent Results and Open Questions','Amir Shpilka; Amir Yehudayoff',2010,'https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf','§3.4, Theorem 3.6 and Open Problem 10, printed pp.29–30; Open Problem 10 on PDF p.35'),
 ref('consolidated_6007_primary','Separating ABPs and Some Structured Formulas in the Non-Commutative Setting','Prerona Chatterjee',2021,'https://doi.org/10.4230/LIPIcs.CCC.2021.7','Introduction, p.7:2; general circuit question versus the paper’s formula/ABP research target'),
 ref('syntactic','Lower Bounds for Noncommutative Circuits with Low Syntactic Degree','Pratik Shastri',2026,'https://doi.org/10.4230/LIPIcs.ITCS.2026.115','23 January 2026; Introduction and coefficient explicitness footnote p.115:2; Theorems 2–4 pp.115:3–4'),
 ref('quadratic','A Quadratic Lower Bound for Noncommutative Circuits','Pratik Shastri',2026,'https://arxiv.org/abs/2604.20575v3','18 May 2026 revision; Introduction, explicitness footnote p.1, palindrome definition and Theorem 1.2 p.2, Definition 3.2 p.3'),
 ref('raz','Polynomial Lower Bounds for Arithmetic Circuits over Non-Commutative Rings','Ran Raz',2026,'https://eccc.weizmann.ac.il/report/2026/061/','Revision 1, 30 July 2026; abstract, §1.2 and §1.3, printed pp.1–4'),
 ],
 context_blocks=[
 block('The order of symbols gives a coefficient matrix method that proves exponential formula and branching-program lower bounds. A circuit can reuse an intermediate computation, so such a formula lower bound need not imply a comparably large circuit.'),
 block('Uniform coefficient computation is a precise way to require an explicit family. Allowing only polynomial degree also prevents repeated squaring of a huge-degree monomial from masquerading as a meaningful circuit lower bound.','syntactic'),
 block('The January 2026 low-syntactic-degree result improves polynomial lower bounds under an intermediate-degree restriction. Later work must be considered before treating its stated unrestricted frontier as current.','syntactic'),
 block(r'The May 2026 preprint states a tight \(\Omega(nd)\) bound for the palindrome polynomial on two groups of \(n\) variables and degree \(2d\), with no syntactic-degree restriction. At \(d=n\), this is quadratic in the number of variables. Its matching \(O(nd)\) recursive circuit makes that particular family insufficient for the superpolynomial target.','quadratic'),
 block(r'The July revision of the concurrent Raz paper states \(\Omega(d\sqrt n)\) non-scalar multiplication lower bounds and discusses the stronger total-size palindrome result. These 2026 advances change the polynomial frontier without proving the superpolynomial statement.','raz'),
 ],
 progress=[progress('2010','The survey separates exponential formula lower bounds from the open superpolynomial general circuit question.'),progress('2021','The CCC introduction repeats the unrestricted circuit challenge before studying formula and branching-program distinctions.','consolidated_6007_primary'),progress('2026-01-23','The ITCS paper improves bounds for low syntactic degree and states an efficient coefficient-access explicitness convention.','syntactic'),progress('2026-05-18','The revised preprint states the unrestricted quadratic palindrome lower bound, still matched by polynomial-size circuits.','quadratic'),progress('2026-07-30','The concurrent paper’s revision describes its multiplication lower bounds and the quadratic total-size progress.','raz')],
),[
 'Applied the announced recommended editorial default of an existential explicit rational-coefficient family over C; the optional choice was not treated as user confirmation.',
 'Specified polynomial degree, one bit-time coefficient algorithm, rational output encoding and unrestricted complex circuit constants.',
 'Defined associative free-word semantics, ordered binary multiplication, gate-count size and arbitrarily-large-index lower-bound quantifiers.',
 'Preserved the consolidated 2021 source occurrence without confusing its formula/ABP target with the general circuit question.',
 'Updated the January 2026 frontier using the May quadratic preprint and July concurrent revision, rather than incorrectly retaining Omega(n log n) as the current general bound.',
 'Individually assessed importance and required complete Lean-checked explicitness and unrestricted circuit lower-bound proofs or the precise negation.',
],[
 'Read Shpilka–Yehudayoff §3.4, printed pp.29–30, including Theorem 3.6, its small-circuit recursive witness and Open Problem 10. The source motivates explicit polynomial-degree families but does not fix the precise rational coefficient algorithm used here.',
 'Read Chatterjee CCC 2021 abstract and Introduction pp.7:1–7:2. It distinguishes the general noncommutative circuit challenge from its own formula-versus-ABP direction.',
 'Read Shastri ITCS 2026 abstract, Introduction, explicitness footnote p.115:2 and Theorems 2–4 pp.115:3–4. Its circuit improvements have syntactic-degree restrictions. Its introductory best-known claim is superseded by later 2026 work.',
 'Read Shastri arXiv:2604.20575v3, 18 May 2026, abstract and Introduction pp.1–2 including the coefficient explicitness footnote, palindrome definition, matching O(nd) upper bound and Theorem 1.2; read Definition 3.2 on p.3. The theorem is for general fan-in-two circuits over any field and is polynomial, not superpolynomial. The current arXiv record was checked and has no withdrawal notice as of 17 September 2026.',
 'Read Raz ECCC TR26-061 Revision 1, 30 July 2026, abstract and §1.2–1.3 pp.3–4. The paper states Omega(d sqrt(n)) non-scalar multiplication bounds and explicitly acknowledges Shastri’s concurrent Omega(dn) total-size result. Ring-function consequences are not silently substituted for free-algebra circuit complexity.',
 'Bounded primary-source searches through 17 September 2026 identified no superpolynomial resolution for the chosen explicit family target. Recent preprint theorem statements are reported with their dated status; their proofs were not independently verified here.',
], 'Source-open for an explicit polynomial-degree rational-coefficient family requiring superpolynomial unrestricted noncommutative circuits over C. The 2026 quadratic palindrome theorem and concurrent multiplication bounds are polynomial advances; they do not solve the selected target. Dated primary statements, including the May and July revisions, were checked through 17 September 2026 without independently verifying the full proofs.',summary=[
 'The target is some polynomial-degree family with rational coefficients and ordered noncommuting variables.',
 'One deterministic polynomial-time algorithm must compute any requested word coefficient exactly.',
 'Every polynomial size bound must fail for unrestricted arithmetic circuits over the complex numbers at arbitrarily large input lengths.',
 'Depth, sharing, intermediate degrees and complex constants are unrestricted, so formula or restricted-circuit bounds are insufficient.',
 'The answer must provide complete Lean-checked explicitness and circuit lower-bound proofs or prove the exact negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
