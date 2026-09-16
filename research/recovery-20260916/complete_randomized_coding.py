"""Review the existential, all-support coding question for private randomness."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5010'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the complete existential-coding question and the introductory definition of a pointwise coding theorem.',
 'Specified all strings in the support of each uniformly polynomial-time samplable distribution, not merely an average-case subset.',
 'Defined private-randomness complexity with a single program selected before its random tape, distinguishing it from public-randomness pK.',
 'Made the polynomial decoding time, logarithmic additive overhead and sampler-dependent constants explicit.',
 'Did not add a polynomial-time encoder requirement or assume the non-existence of one-way functions.',
 'Checked the December 2025 boundary-hardness paper, which explicitly still distinguishes the missing all-support coding theorem from the conditional average-case result.',
]
sources=[
 'Read Hirahara–Lu–Nanashima, FOCS 2024 pp. 369–374: introduction pp. 369–370, Theorems I.1–I.2, I.5–I.7 and the open passage p. 374, PDF p. 6. The introduction defines coding pointwise on the support and distinguishes existence from efficient encoding.',
 'Downloaded the full ECCC TR24-155 report, posted 11 October 2024, and checked the corresponding introductory discussion. The publication and full report are versions of the same work, not independent evidence.',
 'Read Liu–Pass, One-way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity, ECCC TR25-202, published 5 December 2025, abstract and §1.2 pp. 6–7. It explicitly identifies the missing unconditional all-support randomized coding theorem.',
 'Bounded primary-source searches through 16 September 2026 found no subsequent resolution of this existential all-support statement. The review checks the stated scope of the cited results, not every proof in those papers.',
]
status=('The FOCS 2024 paper leaves existential coding for all polynomial-time samplable distributions open. '
 'The December 2025 boundary-hardness paper again identifies the all-support theorem as unavailable. '
 'Its conditional average-case substitutes and the efficient-coding equivalences do not resolve the statement below; no later resolution was found in the bounded check.')
complete(identifier,dict(
 title='Unconditional coding theorem for randomized Kolmogorov complexity',
 criterion='construction',question_type='yes_no',
 formal=r'''Is the following coding statement true without a computational hardness or derandomization assumption?
\[
\forall D\in\mathrm{PSamp}\ \exists c,d\in\mathbb N_{\ge1}\
\forall n\ge2\ \forall x\in\operatorname{supp}(D_n):
\quad
\mathrm{rK}^{(n+2)^d}(x)
\le
\left\lceil\log_2\frac1{D_n(x)}\right\rceil
+c\left\lceil\log_2(n+2)\right\rceil .
\]
Here \(D=\{D_n\}_{n\ge2}\) ranges over uniformly polynomial-time samplable distributions on \(n\)-bit strings, and \(\mathrm{rK}^t\) uses private random bits and success probability at least \(2/3\), as defined below. The constants \(c,d\) may depend on the fixed sampler but must work for every length and every string in its support.

The target is existence of short polynomial-time randomized descriptions. No efficient algorithm for finding a description from \(x\) is required.''',
 definitions=r'''Fix one standard efficiently universal probabilistic Turing machine \(U\), with a binary program, a one-way tape of independent fair random bits and an output tape. Its simulation of any fixed machine has polynomial time overhead and a constant program-description overhead. The program receives no input string, length, advice, shared random tape or oracle for the sampler's distribution.

For \(t\in\mathbb N\), define
\[
\mathrm{rK}^{t}(x)=
\min\left\{
 |p|:
 \Pr_{r\leftarrow\{0,1\}^{t}}
 [U(p;r)\text{ halts within }t\text{ steps with output exactly }x]
 \ge\frac23
\right\}.
\]
A computation uses at most \(t\) random bits in \(t\) steps; unused bits are ignored. Failure to halt in time or outputting another string is failure. The minimum is \(+\infty\) if there is no such program. The same program \(p\) must succeed for the indicated fraction of random tapes. It may depend on \(D,n,x\), but it is chosen before the random tape. A description can encode the length and a sampler description within its counted program bits.

Membership \(D\in\mathrm{PSamp}\) means that there is one deterministic algorithm \(S\), a polynomially bounded, polynomial-time computable integer function \(a(n)\), and a polynomial time bound, such that for every \(n\ge2\) and every \(r\in\{0,1\}^{a(n)}\), the computation \(S(1^n,r)\) outputs exactly \(n\) bits within that bound. The law of \(S(1^n,R)\) for uniform \(R\) is \(D_n\). Thus \(D_n(x)\) is an exact rational probability and \(\operatorname{supp}(D_n)=\{x:D_n(x)>0\}\). The sampler is uniform and has no length-dependent advice.

The expression \(\log_2(1/D_n(x))\) is the information content, in bits, of the particular string. The inequality is pointwise on the entire support, including very unlikely strings. It is not only an expected-length bound or a guarantee outside a small exceptional set. There is one polynomial decoding-time exponent and one logarithmic-overhead constant for the whole sampler family.

For comparison, probabilistic complexity \(\mathrm{pK}^{t}(x)\) permits the short deterministic program to be chosen after seeing public random bits: its quantifiers have the form \(\Pr_r[\exists p\text{ short}:U(p;r)=x]\ge2/3\). That is a different measure from the single-program private-randomness measure in the question. Likewise, an efficient coding theorem would additionally require an efficient encoder that finds a short description; this card does not impose that requirement.

No assumption about one-way functions, average-case hardness or circuit lower bounds is part of the statement. The fixed universal-machine convention is harmless for this existential polynomial-time and logarithmic-overhead target, since the constants and exponent may change.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the displayed universal coding statement. An affirmative answer must cover every uniformly polynomial-time sampler and every supported string with the stated quantifier order. A negative answer must establish a sampler family for which no pair of constants \(c,d\) works. A conditional result, a coding theorem only for public-randomness complexity, an expected-length bound, or a theorem allowing exceptional strings does not suffice. This is a binary question; numerical \(1/100\) tolerance does not relax the coding inequality or its universal quantifiers.''',
 source_formulation=dict(
 text='The source leaves open whether all polynomial-time samplable distributions admit an existential coding theorem for polynomial-time randomized Kolmogorov complexity without assumptions.',
 caption='Paraphrase of FOCS 2024 p. 374, PDF p. 6, read with the pointwise coding and private-randomness definitions on pp. 369–370.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=86,method='editorial',
 reason='The question asks whether a basic information-content coding principle survives polynomial-time decoding with private randomness for the full class of efficient samplers.',
 basis='Individual assessment of the general sampling model, the distinction between public and private randomness, and the repeated role of the missing theorem in average-case complexity and cryptographic characterizations.'),
 why='A sampler may assign a string high probability without providing an obvious short description that a fast decoder can use. The question asks whether information content nevertheless always predicts description length, allowing private randomness and logarithmic overhead. A resolution would clarify a recurring gap between information-theoretic coding and computational descriptions.',
 references=[
 ref('primary','Optimal Coding for Randomized Kolmogorov Complexity and Its Applications',
 'Shuichi Hirahara; Zhenjian Lu; Mikito Nanashima',2024,
 'https://doi.org/10.1109/FOCS61266.2024.00030',
 'FOCS 2024, pp. 369–378; introduction pp. 369–370, Theorems I.1–I.2 and I.5–I.7; open passage p. 374 (PDF p. 6); full version ECCC TR24-155, posted 11 October 2024'),
 ref('boundary','One-way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity',
 'Yanyi Liu; Rafael Pass',2025,'https://eccc.weizmann.ac.il/report/2025/202/',
 'ECCC TR25-202, published 5 December 2025; §1.2 pp. 6–7, discussion of unconditional all-support coding'),
 ],
 context_blocks=[
 block('The classical coding principle bounds description length by information content when no decoding-time restriction is imposed. The card asks for a polynomial-time private-randomness version for arbitrary efficient samplers.'),
 block('Public-randomness descriptions may choose a different short program after seeing the shared random tape. The cited literature supplies stronger coding results in that model; they do not give the single fixed randomized program required here.'),
 block('The source proves efficient coding for next-bits predictable distributions, where conditional next-bit probabilities can be estimated to arbitrarily small inverse-polynomial accuracy. An efficient sampler alone is not that additional prediction guarantee.'),
 block('Theorems I.1–I.2 give conditional and average-case coding consequences under the non-existence of infinitely-often one-way functions. Their assumptions and allowance of exceptional instances differ from the unconditional pointwise statement.'),
 block('Theorem I.7 identifies a cryptographic obstruction to efficient encoding for all samplable distributions. It does not show that short descriptions fail to exist when the encoder is unrestricted.'),
 block('The December 2025 boundary-hardness paper still identifies the unconditional theorem for every string in the sampler support as missing, and explains why an average-case coding result does not supply that requirement.','boundary'),
 ],
 progress=[
 progress('2024','The FOCS paper obtains new conditional and predictable-distribution coding results while explicitly retaining the general existential question.'),
 progress('2025-12-05','The boundary-hardness report again records the missing unconditional all-support coding theorem.','boundary'),
 progress('2026-09-16','The review specifies the single-program randomization, pointwise quantifiers, decoding time and additive overhead.'),
 ],
),notes,sources,status,summary=[
 'An efficient sampler assigns a probability to each string it can produce.',
 'The question asks whether every such string has a short randomized description close to its information content.',
 'One fixed description must reconstruct the string in polynomial time with probability at least two thirds using private random bits.',
 'The guarantee must cover the whole sampler support, while the encoder that finds a description may be inefficient.',
 'Known conditional, average-case and public-randomness coding results do not establish the stated unconditional theorem.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
