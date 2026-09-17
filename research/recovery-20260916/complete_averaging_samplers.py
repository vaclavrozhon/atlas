"""Restore the indexed explicitness and simultaneous bounds of Vadhan's sampler question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6689'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the averaging guarantee from Definition 3.29 and simultaneous resource bounds from Open Problem 4.24.',
 'Retained indexed explicitness: one requested sample is computable in polynomial time in the seed and index lengths, without enumerating all samples.',
 'Used dyadic error and failure parameters to make a finite uniform input convention; rounding extends the target to arbitrary positive parameters with constant-factor resource overhead.',
 'Corrected the printed log(delta) sign typo to log(1/delta), as required by the preceding bounds and the later explicit restatement.',
 'Specified plain equal-weight averaging, possible repeated samples, and no dependence on the sampled function.',
 'Checked both CCC 2025 tradeoffs and the August 2025 revision metadata; neither gives both optimal bounds at once. Assessed importance individually.',
]
sources=[
 'Read Vadhan, Pseudorandomness, December 2012 published PDF: Definition 3.29 and Theorem 3.30; §4.2 table and Theorem 4.23; Open Problem 4.24 printed p. 101/PDF p. 104; paragraph immediately following it. Definition 3.29 requires polynomial-time indexed sample evaluation and defines a one-sided tail guarantee for all real-valued functions.',
 'The printed Open Problem 4.24 has log(delta) rather than log(1/delta). The preceding table, Theorem 3.30 and Xun–Zuckerman Problem 1 establish the intended positive logarithmic randomness cost; the negative printed term is not copied.',
 'Read Xun–Zuckerman, Near-Optimal Averaging Samplers and Matrix Samplers, CCC 2025 Article 6, published 29 July 2025: abstract; §1 pp. 2–3, Table 1, Problem 1 and Theorems 1–2. The first trades an arbitrary fixed positive exponent loss in sample complexity for optimal randomness; the second has optimal samples but an extra logarithmic factor in randomness.',
 'Checked ECCC TR24-097 revision 5 metadata and abstract, 15 August 2025: the near-optimal sample exponent remains. No proof of indexed evaluation for every cited construction is inferred from its merely efficient whole-output statement.',
 f'Bounded primary-source searches through {DATE} found the near-optimal construction and applications, but no claimed simultaneous optimal construction. This is not an exhaustive openness certificate or an independent verification of the cited proofs.',
]
status=('The CCC 2025 paper explicitly restates the simultaneous optimization question and nearly resolves it: one construction loses a fixed positive exponent in sample count, while another spends additional logarithmic randomness. The August 2025 revision retains that gap. No construction meeting both bounds and the source’s indexed explicitness was found in the bounded check.')
complete(identifier,dict(
 criterion='construction',question_type='yes_no',
 formal=r'''Do there exist universal constants \(C,D\ge1\) and an explicit family of averaging samplers that simultaneously use an optimal-order number of random bits and samples?

Precisely, for every three integers \(m,a,b\ge1\), set \(\varepsilon=2^{-a}\) and \(\delta=2^{-b}\). The family must give integers \(r\ge0,t\ge1\) and a deterministic map
\[
\operatorname{Samp}_{m,a,b}:\{0,1\}^{r}\longrightarrow(\{0,1\}^{m})^{t}
\]
such that
\[
r\le C(m+a+b),\qquad t\le D\,4^{a}b.
\]
For every function \(f:\{0,1\}^{m}\to[0,1]\), with
\(\mu_f=2^{-m}\sum_{z\in\{0,1\}^{m}}f(z)\), require
\[
\Pr_{s\sim U_r}\!\left[
\frac1t\sum_{i=1}^{t}f\!\left(\operatorname{Samp}_{m,a,b}(s)_i\right)
>\mu_f+2^{-a}
\right]\le2^{-b}.
\]
The sampler must satisfy the uniform indexed explicitness convention below, without any computational hardness assumption. The same constants and algorithms must work for all \(m,a,b\).''',
 definitions=r'''A seed is a uniformly random \(r\)-bit string; \(U_0\) is the single empty seed. A sampler deterministically turns the seed into an ordered list of \(t\) points in the domain \(\{0,1\}^m\). Points may repeat and may be correlated. The seed length and sample count depend only on \(m,a,b\), not on the seed or on \(f\).

The only estimator under consideration is the ordinary arithmetic mean of the \(t\) sampled values, with each position weighted by \(1/t\). It is not a median of block averages, an adaptively selected collection of queries, or a function-dependent postprocessing rule. The sampler has no oracle access to \(f\); its guarantee quantifies over every real-valued \(f\) with values in \([0,1]\), without an efficiency or finite-precision restriction on \(f\). For each fixed \(f\), probability is over the seed. One seed need not work simultaneously for all functions.

Indexed explicitness consists of two fixed uniform deterministic multitape Turing machines. The parameter machine receives \((1^m,1^a,1^b)\) and returns the binary encodings of \(r\) and \(t\). The evaluation machine receives these unary parameters, a seed \(s\in\{0,1\}^r\) and a binary index \(i\in\{1,\ldots,t\}\), and returns exactly the \(m\)-bit point \(\operatorname{Samp}_{m,a,b}(s)_i\). For some universal integers \(K\ge1,q\ge1\), both machines run in at most \(K(m+a+b+1)^q\) transitions on these valid inputs. Work tapes start blank; finite programs and alphabets and one-cell head moves are used. Input access, arithmetic and output writing are charged. No advice, random preprocessing, oracle, stored exponential-size graph or unbounded unit-cost operation is available.

This indexed requirement permits computing a requested sample without printing the preceding samples. The full sample list can be printed by \(t\) calls. The source's parameterization measures coordinate evaluation in time polynomial in seed length and index length. Since the seed may be padded with unused bits up to order \(m+a+b\), the displayed bound instantiates that convention uniformly in the parameters.

The one-sided probability inequality is the source's definition. Applying it to \(1-f\) gives the corresponding lower-tail bound. Thus the probability of an absolute estimation error greater than \(\varepsilon\) is at most \(2\delta\); replacing \(b\) by \(b+1\) yields a two-sided guarantee with failure at most \(\delta\), within the same universal resource bounds after changing constants.

Restricting to dyadic \(\varepsilon,\delta\) fixes an exact finite input convention. For arbitrary \(0<\varepsilon,\delta\le1/2\), rounding each down to the nearest power of two changes the seed budget additively by constants and the sample upper bound by a universal constant factor. Consequently the target is the original asymptotic requirement
\[
r=O\!\left(m+\log_2(1/\varepsilon)+\log_2(1/\delta)\right),\qquad
t=O\!\left(\varepsilon^{-2}\log_2(1/\delta)\right).
\]
No relation between the two error parameters, and no restriction such as inverse-polynomial error, is imposed. When the domain is small enough for complete enumeration, that construction is allowed if it meets the same resource bounds.''',
 answer_criterion=r'''Supply a complete Lean-checked construction with universal constants and the two uniform algorithms, proving all resource and probability guarantees, or prove that no such family exists. Both upper bounds must hold for the same sampler throughout the entire parameter range. A sample count raised to \(1+\eta\) for a fixed \(\eta>0\), an extra unbounded logarithmic factor in randomness, mere existence without indexed explicitness, or an estimator other than the ordinary sample mean does not meet the question. This is a binary construction target with specified asymptotic bounds; numerical \(1/100\) tolerance does not replace the user-specified error parameters of the sampler.''',
 source_formulation=dict(text='Open Problem 4.24 asks for explicit averaging samplers with logarithmic randomness overhead and the sample bound of independent averaging, simultaneously. Indexed explicitness and the one-sided tail convention are given in Definition 3.29.',
 caption='Paraphrase of Open Problem 4.24, printed p. 101/PDF p. 104, using Definition 3.29 in the December 2012 published monograph. The printed log(delta) typo is interpreted as log(1/delta), consistent with the surrounding bounds and the later restatement.',
 citation='primary',format='editorial_paraphrase'),
 why='Averaging is a basic way to estimate a large domain using few queries, and reusable sampling constructions also support extractors, codes and interactive proofs. Independent samples have the desired sample count but spend too many random bits, while correlations can save randomness at the cost of more samples. Achieving both bounds in one explicit construction would remove a long-standing loss in this general primitive.',
 importance=dict(score=82,method='editorial',reason='A long-standing, widely reusable pseudorandomness construction problem with a precise simultaneous resource barrier; the 2025 near-optimal result shows substantial progress while preserving a meaningful gap.',assessed_on=DATE,basis='Individual reading of the original sampler definition and target, and the 2025 explicit restatement and two tradeoffs.'),
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,
 'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf',
 'Definition 3.29 and Theorem 3.30; §4.2, Theorem 4.23 and Open Problem 4.24, printed p. 101/PDF p. 104'),
 ref('near','Near-Optimal Averaging Samplers and Matrix Samplers','Zhiyang Xun; David Zuckerman',2025,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2025.6',
 'Published 29 July 2025; §1 pp. 6:2–6:3, Table 1, Problem 1 and Theorems 1–2'),
 ref('revision','Near-Optimal Averaging Samplers and Matrix Samplers','Zhiyang Xun; David Zuckerman',2025,
 'https://eccc.weizmann.ac.il/report/2024/097/revision/5/',
 'Revision 5, 15 August 2025; abstract and revision metadata'),
 ],
 context_blocks=[
 block('Independent sampling meets the requested sample upper bound but uses fresh randomness for every point. Pairwise-independent sampling saves randomness while having worse dependence on the failure probability in sample count.'),
 block('The source describes a general sampling algorithm combining expander walks and pairwise independence, but it estimates the mean through a more involved operation. It does not meet the ordinary-averaging requirement.'),
 block(r'The 2025 near-optimal sampler has \(O((\varepsilon^{-2}\log(1/\delta))^{1+\eta})\) samples for any fixed \(\eta>0\), alongside optimal-order randomness in the stated regime. An arbitrarily small fixed exponent loss is still not a universal constant factor.','near'),
 block('A second 2025 construction attains the target sample count but incurs an extra logarithmic factor in its randomness overhead. The two bounds belong to different constructions and cannot be combined by taking the better entry from each.','near'),
 block('The original definition provides efficient access to any indexed sample. This is stronger than merely allowing time polynomial in the entire sample-list length to retrieve one point.'),
 ],
 progress=[
 progress('2012','The monograph records the simultaneous optimization question and attributes its earlier formulation to Bellare and Rompel.'),
 progress('2025-07-29','Xun and Zuckerman give two near-optimal tradeoffs and explicitly restate the unresolved simultaneous target.','near'),
 progress('2025-08-15','The later ECCC revision retains the positive sample exponent loss in its main guarantee.','revision'),
 progress(DATE,'The review fixes indexed uniformity, dyadic parameters and the source probability convention; the bounded later-work check finds no simultaneous optimum.'),
 ],
),notes,sources,status,summary=[
 'An averaging sampler estimates a function’s global mean by taking the ordinary mean of a short list of sampled values.',
 'The question asks for one explicit construction with both a logarithmic randomness budget and the sample count of independent sampling.',
 'Each sample must be computable efficiently from the seed and its index, without generating the whole list first.',
 'The guarantee applies to every function valued in the unit interval and to all positive error and failure regimes.',
 'The 2025 constructions approach both targets, but retain either an extra exponent in sample count or extra logarithmic randomness.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
