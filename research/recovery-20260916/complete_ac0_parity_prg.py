"""Recover Vadhan's constant-error, mildly explicit AC0[2] generator target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6693'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Open Problem 7.33 verbatim in scope: depth k, output and gate-count bound m, error 1/4 and subpolynomial seed length.',
 'Preserved the source’s mildly explicit runtime poly(m,2^seed), rather than silently requiring polynomial-time generation in output length.',
 'Defined the unbounded-fan-in AND/OR/parity model with source gate-count and depth conventions, and no uniformity restriction on distinguishers.',
 'Expanded subpolynomial as a property of one family for each fixed depth, with all positive exponents and eventual cutoffs.',
 'Compared restricted-gate 2025 results and large-field/modular-sum 2026 results without treating them as general binary AC0[2] constructions.',
 'Assessed the foundational generator question individually.',
]
sources=[
 'Read Vadhan, Pseudorandomness, December 2012 published PDF: Definition 7.7 printed p. 217/PDF p. 220; Definition 7.26 printed p. 236; surrounding §7.4.3; Open Problem 7.33 printed p. 239/PDF p. 242. Definition 7.26 counts computation gates, and Definition 7.7 permits time poly(m,2^d(m)).',
 'Read Kumar, New Pseudorandom Generators and Correlation Bounds Using Extractors, ITCS 2025 Article 68: abstract, §1.1 pp. 3–4 and §1.2 p. 5. The restricted symmetric/threshold-gate and structured-polynomial results do not give the stated generator for arbitrary parity gates throughout the circuit.',
 'Checked Cohen–Doron–Goldgraber, arXiv:2602.10030v1, 10 February 2026, author abstract and submission history. The optimal-seed result assumes sufficiently large field characteristic and polynomial field size in the degree; the stated characteristic-free small-field extension is not a theorem for F2.',
 'Checked Krak, ECCC TR26-130 revision 5, 7 August 2026, author abstract: its tests are Boolean linear sums modulo a fixed integer, not arbitrary constant-depth compositions of AND, OR and parity gates. The new proof itself was not independently reviewed.',
 f'Bounded primary-source searches through {DATE} found these restricted constructions, without a claimed unconditional subpolynomial-seed generator for the complete circuit class in the source. This is not an exhaustive current-openness certificate.',
]
status=('The 2012 source poses the stated mildly explicit construction. Checked 2025 results cover restricted uses of symmetric or threshold gates and structured polynomials; checked 2026 results concern larger fields or individual modular sums. None supplies the all-circuits construction below, and no resolution was found in the bounded later-work check.')
complete(identifier,dict(
 criterion='construction',question_type='yes_no',
 formal=r'''For every fixed integer \(k\ge1\), is there an unconditional, mildly explicit generator family
\[
G_{k,m}:\{0,1\}^{d_k(m)}\longrightarrow\{0,1\}^{m}\qquad(m\ge1)
\]
whose integer seed length satisfies \(d_k(m)=m^{o(1)}\), and which fools every depth-at-most-\(k\), size-at-most-\(m\) \(\mathrm{AC}^{0}[2]\) circuit on \(m\) input bits with error at most \(1/4\)?

Precisely, for every such circuit \(C\),
\[
\left|\Pr_{s\sim U_{d_k(m)}}[C(G_{k,m}(s))=1]
-\Pr_{x\sim U_m}[C(x)=1]\right|\le1/4.
\]
The generator for a given \(k,m\) must work simultaneously for all the indicated circuits and cannot depend on \(C\). “Mildly explicit” means uniform deterministic evaluation in time polynomial in \(m\) and \(2^{d_k(m)}\), with the polynomial permitted to depend on \(k\).''',
 definitions=r'''A circuit is a finite directed acyclic graph with one output bit. Input nodes carry literals \(x_i\), their negations \(\neg x_i\), or constants \(0,1\), for \(1\le i\le m\). Every computation node is an AND, OR or parity gate with arbitrarily many predecessors. AND is one exactly when all its input bits are one; OR is one exactly when at least one is one; parity is the sum of its inputs modulo two. For no predecessors, AND is one and OR and parity are zero. Fan-out is unrestricted. Gates may be used at any depth, and parity gates may feed other parity gates or either Boolean gate type.

Size counts computation nodes only. Input literals and constants are free input nodes. Depth is the maximum number of computation nodes along a directed path from an input to the output; a literal or constant output has depth zero. There is no restriction on wires beyond a finite circuit description, and no requirement that the testing circuit descriptions be generated uniformly over lengths. Negations are available at inputs as in the source definition. Allowing complemented parity outputs or internal NOT gates gives the same all-fixed-depth target after routine constant changes in resources, but the formal statement uses the specified basis.

For an integer \(\ell\ge0\), \(U_\ell\) is the uniform distribution on all \(\ell\)-bit strings; \(U_0\) is concentrated on the empty string. Randomness consists only of the uniformly chosen seed. The generator is a deterministic map, may have collisions and outputs exactly \(m\) bits. The two probabilities use independent draws from the stated uniform domains.

For each fixed \(k\), a single function \(d_k:\mathbb N_{\ge1}\to\mathbb N_{\ge0}\) must satisfy
\[
\forall a>0\ \exists M_{k,a}\ \forall m\ge M_{k,a}:\ d_k(m)\le m^a.
\]
This defines the subpolynomial seed requirement. It does not ask merely for one fixed sublinear power, nor permit choosing a different generator family separately for each \(a\).

Uniform mild explicitness requires deterministic algorithms for computing \(d_k(m)\) and evaluating \(G_{k,m}(s)\). There are constants \(A_k\ge1,b_k\ge1\) such that on input \(1^m\) the first algorithm outputs the binary encoding of \(d_k(m)\), and on input \((1^m,s)\), with \(|s|=d_k(m)\), the second outputs \(G_{k,m}(s)\), each within
\[
A_k\bigl(m+2^{d_k(m)}+1\bigr)^{b_k}
\]
steps. Use the ordinary uniform deterministic multitape Turing model: finitely many tapes and finite alphabets, initially blank work tapes, and one-cell head moves per transition. Input access and output writing are charged. There is no advice, random construction, oracle, unbounded unit-cost arithmetic or assumed computational hardness. The programs and constants may depend on the fixed \(k\); no efficient procedure producing them from \(k\) is required. A fully explicit polynomial-in-\(m\) evaluation algorithm also qualifies, but is not required.

The size parameter is the source's number of computation gates and is set equal to the output length. The requested error bound is the absolute difference of acceptance probabilities, with no averaging over circuits. It must hold at every positive \(m\); only the seed-length estimate is asymptotic.''',
 answer_criterion=r'''Supply a complete Lean-checked construction or a proof that the asserted family cannot exist. A positive answer must prove the uniform evaluation bound, the subpolynomial seed condition and the \(1/4\) fooling guarantee for every fixed depth and every circuit in the stated class. A construction using a hardness assumption, treating only one depth, restricting the locations or number of parity gates, or providing only a fixed sublinear seed exponent does not suffice. This is an existence question with its own exact error threshold; numerical \(1/100\) answer tolerance does not replace the \(1/4\) pseudorandomness condition.''',
 source_formulation=dict(text='Open Problem 7.33 asks for a mildly explicit, error-one-quarter generator with subpolynomial seed length against every fixed-depth AC0[2] circuit, using output length as the circuit-size bound.',
 caption='Paraphrase of Open Problem 7.33, printed p. 239/PDF p. 242, with mild explicitness from Definition 7.7, in the December 2012 published monograph.',
 citation='primary',format='editorial_paraphrase'),
 why='Adding parity gates is a basic step beyond constant-depth AND/OR circuits, yet existing worst-case lower bounds do not supply the strong average-case guarantees used by standard generator constructions. A generator with the requested seed would permit deterministic seed enumeration in subexponential time for the entire fixed-depth class. The question probes a central gap between proving circuit lower bounds and turning them into useful pseudorandomness.',
 importance=dict(score=87,method='editorial',reason='A standard unconditional derandomization challenge for a canonical circuit class beyond AC0, exposing the gap between known lower bounds and the stronger average-case hardness needed for short seeds.',assessed_on=DATE,basis='Individual review of Vadhan’s exact construction target and the scope of later restricted-generator results.'),
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,
 'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf',
 'December 2012 published PDF; Definition 7.7 p. 217, Definition 7.26 p. 236, Open Problem 7.33 p. 239/PDF p. 242'),
 ref('restricted','New Pseudorandom Generators and Correlation Bounds Using Extractors','Vinayak M. Kumar',2025,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.68',
 'ITCS 2025 Article 68; abstract, §1.1 pp. 68:3–68:4 and §1.2 p. 68:5'),
 ref('fields','Optimal PRGs for Low-Degree Polynomials over Polynomial-Size Fields','Gil Cohen; Dean Doron; Noam Goldgraber',2026,
 'https://arxiv.org/abs/2602.10030v1',
 'Version 1, 10 February 2026; abstract, field-size and characteristic conditions'),
 ],
 context_blocks=[
 block('The monograph first constructs short-seed generators for circuits without parity gates. Parity itself provides useful hardness for that construction, but becomes directly computable once parity gates are allowed.'),
 block('The source discusses known worst-case lower bounds for the larger circuit class and explains that their available average-case form does not immediately give this generator.'),
 block('Mild explicitness permits evaluating a seed in time polynomial in the whole seed-space size. Enumerating all seeds still takes subexponential time when the seed length is subpolynomial.'),
 block('The 2025 work improves generators and correlation bounds for circuits with restricted symmetric or threshold gates, including a symmetric gate above AC0. This does not furnish the requested guarantee for unrestricted parity composition.','restricted'),
 block('The 2026 polynomial-generator result assumes a field and characteristic regime that excludes the binary-field case required here. It is a related advance, not a construction for this card.','fields'),
 ],
 progress=[
 progress('2012','The monograph states the fixed-depth, linear-size, error-one-quarter construction problem.'),
 progress('2025','Kumar improves generators and correlation bounds for several restricted models extending sparse binary polynomials.','restricted'),
 progress('2026-02-10','A large-characteristic field result improves polynomial generators without resolving the binary-field challenge.','fields'),
 progress(DATE,'The review restores mild explicitness and all seed/depth quantifiers; no full construction is found in the bounded source check.'),
 ],
),notes,sources,status,summary=[
 'The question asks for pseudorandom bits that fool constant-depth circuits built from AND, OR and parity gates.',
 'For each fixed depth, one generator family must work against every circuit with at most as many computation gates as output bits.',
 'The difference in acceptance probabilities must be at most one quarter for every permitted circuit.',
 'The seed length must eventually be smaller than every positive power of the output length.',
 'Uniform generation may take time polynomial in the number of seeds, and known restricted-circuit or larger-field results do not meet the whole target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
