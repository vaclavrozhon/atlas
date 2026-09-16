"""Expand the polynomial-time hardness target using the source's Corollary 55."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-2202'
claim=read_claims(ROOT)[identifier]
notes=[
 'Read the formal public-randomness definition and the two probability thresholds of Cond-pK, rather than interpreting computing as outputting an exact numerical minimum.',
 'Used the source’s full Corollary 55 to specify the uniform padding-compatible randomized reduction required for its Pessiland consequence.',
 'Quantified over arbitrarily large polynomial decoding bounds, with one reduction per error exponent and the selected time exponent affecting its polynomial output-length schedules.',
 'Specified random access to the conditional input, all-input polynomial reduction time and the lack of cryptographic assumptions.',
 'Kept the known sublinear-time theorem separate and checked the March 2026 chain-rule report’s account of the remaining hardness question.',
 'Did not reproduce the reversed implication in the parenthetical sentence of full-version Corollary 55: its proof sketch gives that absence of infinitely-often one-way functions implies average-case tractability of NP under the proposed reduction.',
]
sources=[
 'Read Lu–Santhanam, ICALP 2024 Article 110, §1.1.1 pp. 110:3–110:5 and §1.3 p. 110:15, including the precise promise thresholds and Theorems 1–3.',
 'Read the full ECCC TR24-085 version, published 25 April 2024, §1.3 p. 16, Definitions 14–16 p. 17, and §4.4 Corollary 55 with its proof sketch pp. 36–37. The full statement places the randomized reduction before the universal polynomial time bound and permits time-bound-dependent polynomial length padding.',
 'Read Kabanets–Kolokolova, Kolmogorov’s Approach to P vs NP: Chain Rules for Time-Bounded Kolmogorov Complexity, ECCC TR25-089 revision 1 accepted 13 March 2026, introduction and §1.3 pp. 9–10. Its summary still identifies unconditional conditional-pK hardness only in the sublinear regime and distinguishes conditional deterministic-K hardness using witness encryption.',
 'Bounded primary-source checks through 16 September 2026 found no unconditional reduction meeting the selected polynomial-regime target. The cited chain-rule and cryptographic statements were checked for scope, not independently reproved.',
]
status=('The source proves randomized NP-hardness when the decoding program cannot read the entire conditional input, and asks for the polynomial-time regime. '
 'The full version specifies a padding-compatible reduction sufficient for its average-case consequence; that is the target expanded here. '
 'The checked March 2026 report retains the distinction, and no later unconditional construction or refutation was found.')
complete(identifier,dict(
 title='NP-hardness of conditional polynomial-time pKt',
 criterion='reductions',question_type='yes_no',
 formal=r'''Does conditional probabilistic time-bounded Kolmogorov complexity admit the following unconditional, uniform padding-compatible NP-hardness reduction in the polynomial-time regime?

For every integer \(\kappa\ge1\), there must exist one randomized polynomial-time map \(R_\kappa\) such that for every integer \(c\ge2\), there exist polynomially bounded, polynomial-time computable length functions \(n_c,m_c:\mathbb N\to\mathbb N_{\ge2}\) with the following property. For every Boolean 3-CNF formula \(z\) of encoded length \(v\ge2\),
\[
R_\kappa(z,1^{n_c(v)},1^{m_c(v)})=(x,y,1^s),
\qquad |x|=n_c(v),\quad |y|=m_c(v),
\]
and, with probability at least \(1-v^{-\kappa}\) over the reduction's random bits,
\[
\begin{aligned}
 z\text{ satisfiable}
 &\ \Longrightarrow\
 \mathrm{pK}_{2/3}^{\,\tau_c(|x|,|y|)}(x\mid y)\le s,\\
 z\text{ unsatisfiable}
 &\ \Longrightarrow\
 \mathrm{pK}_{1/3}^{\,\tau_c(|x|,|y|)}(x\mid y)>s,
\end{aligned}
\qquad
\tau_c(n,m)=(n+1)^c(m+1)^c.
\]
The same \(R_\kappa\) must work for all \(c\); \(c\) affects the chosen output-length schedules and is not a separate input or advice string to the reduction. The schedules may also depend on \(\kappa\). This is the quantified polynomial-regime target underlying the source's Corollary 55.''',
 definitions=r'''Fix a standard time-optimal universal machine \(U\) for binary programs with a read-only random input and random access to a finite conditional string \(y\). A query specifies a bit position in binary and returns that bit, or an end marker for a position outside the string. Writing a query and all ordinary computation count toward time; an oracle query itself takes one step. The machine has no other oracle or advice. Programs use a fixed paddable binary encoding. Polynomial simulation overhead is allowed in the universal-machine convention.

For strings \(x,y\), an integer time bound \(t\ge1\), and \(\lambda\in(0,1]\), let
\[
\mathrm{pK}^{t}_{\lambda}(x\mid y)
=\min\left\{k\in\mathbb N:
\Pr_{r\leftarrow\{0,1\}^{t}}\!
\left[\exists p\in\{0,1\}^{\le k}:
 U^y(p,r)\text{ halts within }t\text{ steps and outputs }x
\right]\ge\lambda
\right\}.
\]
The value is \(+\infty\) if no such \(k\) exists. The existential program is inside the probability: it may depend on the public random string \(r\). This is not the private-randomness measure that chooses one program before its coins. No probability is taken over \(x\) or \(y\).

For a fixed \(c\), the promise problem \(\operatorname{Cond\text{-}pK}[\tau_c]\) has instances \((x,y,1^s)\), with \(s\ge0\), and disjoint parts
\[
\begin{aligned}
\mathrm{YES}_c
 &=\{(x,y,1^s):
       \mathrm{pK}^{\tau_c(|x|,|y|)}_{2/3}(x\mid y)\le s\},\\
\mathrm{NO}_c
 &=\{(x,y,1^s):
       \mathrm{pK}^{\tau_c(|x|,|y|)}_{1/3}(x\mid y)>s\}.
\end{aligned}
\]
Disjointness follows because achieving probability \(2/3\) requires at least as much description length as achieving \(1/3\). Inputs in neither set carry no required answer. The problem is called computing conditional probabilistic complexity in the source, but its specified task is this promise decision problem, not evaluation of the exact integer \(\mathrm{pK}^t\).

Use a fixed ordinary binary encoding of Boolean formulas in conjunctive normal form with at most three literals per clause. Satisfiability asks whether an assignment makes every clause true. This standard NP-complete source problem makes NP-hardness concrete. Finitely many shorter encodings can be handled separately.

For each \(\kappa\), \(R_\kappa\) is one uniform probabilistic Turing machine whose time on every input \((z,1^n,1^m)\) and every random tape is bounded by a polynomial in \(|z|+n+m\). It always outputs a finite triple; for the length schedules selected in the statement, the displayed output lengths hold on every execution. The bound counts writing \(x,y,1^s\), so the output threshold is polynomially bounded as well. For a fixed \(\kappa,c\), composing with its length schedules is a randomized polynomial-time many-one reduction. There are no adaptive calls to a solver and no nonuniform advice depending on \(v\).

Requiring all \(c\ge2\) specifies arbitrarily generous polynomial decoding times at which the entire conditional string can be read. It also gives a cofinal explicit family of the source's polynomial time bounds; the required reduction is uniform across the family, as in its formal corollary. A different unrestricted reduction chosen independently for each exponent is not the full uniform assertion made here. The unary length arguments permit the padding dependence that the corollary expressly allows.

The reduction's probability is separate from the inner public-randomness probabilities defining the target promise. A successful reduction must land in the correct promise part. Landing outside the promise counts against its permitted failure probability.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the quantified reduction statement. An affirmative answer must supply the uniform reduction family, the polynomial length schedules, the running-time bounds, and both promise-preservation guarantees for every required exponent. A refutation must disprove that assertion in the stated unrelativized model. A sublinear decoding-time result, an additional cryptographic assumption, or a limitation of one reduction technique does not settle it. This is a binary existence question; \(1/100\) numerical tolerance does not replace the two promise thresholds or the reduction error bound.''',
 source_formulation=dict(
 text='The source asks whether computing conditional probabilistic Kolmogorov complexity is NP-hard in the polynomial-time regime and links such hardness to excluding Pessiland.',
 caption='Paraphrase of ICALP 2024 §1.3 p. 110:15; the promise and quantified reduction are expanded from §1.1.1 and full-version Corollary 55.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=87,method='editorial',
 reason='The proposed hardness transfer connects a concrete description-length problem to the gap between average-case NP hardness and one-way functions.',
 basis='Individual assessment of the consequence established for the source’s quantified reduction and the central distinction between sublinear and unrestricted polynomial decoding time.'),
 why='When a short program cannot inspect most of its conditional input, there is a provable source of hardness. Allowing it polynomial time to read and process the whole input removes that obstruction. Establishing the stated uniform hardness reduction would make a major connection between worst-case reductions and the existence of cryptographic hardness.',
 references=[
 ref('primary','Impagliazzo’s Worlds Through the Lens of Conditional Kolmogorov Complexity',
 'Zhenjian Lu; Rahul Santhanam',2024,'https://doi.org/10.4230/LIPIcs.ICALP.2024.110',
 'ICALP 2024, Article 110; §1.1.1 pp. 110:3–110:5 and §1.3 p. 110:15'),
 ref('full','Impagliazzo’s Worlds Through the Lens of Conditional Kolmogorov Complexity',
 'Zhenjian Lu; Rahul Santhanam',2024,'https://eccc.weizmann.ac.il/report/2024/085/',
 'ECCC TR24-085, published 25 April 2024; Definition 16 p. 17, §4.4 Corollary 55 and proof sketch pp. 36–37'),
 ref('chain','Kolmogorov’s Approach to P vs NP: Chain Rules for Time-Bounded Kolmogorov Complexity',
 'Valentine Kabanets; Antonina Kolokolova',2026,'https://eccc.weizmann.ac.il/report/2025/089/',
 'ECCC TR25-089 revision 1, accepted 13 March 2026; introduction and §1.3 pp. 9–10; polynomial-regime hardness remains an assumption'),
 ],
 context_blocks=[
 block('The source proves randomized NP-hardness for a regime in which the allowed time is sublinear in the length of the conditional string. A program may still run polynomially long in the output length, so sublinear here refers to the side input.'),
 block('Its polynomial regime instead permits time growing as a product of powers of the two string lengths. The decoder can inspect its entire conditional input, and the sublinear theorem does not extend automatically.'),
 block('The task has a probability gap between two public-randomness description thresholds. It is not a request to output an exact Kolmogorov-complexity number and does not exchange the order of the random tape and program quantifiers.'),
 block('The full corollary places one randomized reduction before the time-bound quantifier and permits the output lengths to vary polynomially with the chosen bound. This uniformity is part of the precise target used to support the claimed consequence.','full'),
 block('Under that reduction, the proof sketch combines average-case easiness of conditional probabilistic complexity with the non-existence of infinitely-often one-way functions to obtain average-case randomized tractability for NP. This is the direction relevant to excluding Pessiland.','full'),
 block('The March 2026 chain-rule report still separates the unconditional sublinear result from polynomial-regime hardness assumptions. A cited polynomial-regime result for deterministic conditional complexity uses witness encryption and concerns a different measure.','chain'),
 ],
 progress=[
 progress('2024-04-25','The full report states the public-randomness hardness question and the quantified reduction sufficient for the Pessiland consequence.','full'),
 progress('2024','The ICALP paper publishes the sublinear theorem and leaves the polynomial regime as an open problem.'),
 progress('2026-03-13','The revised chain-rule report retains polynomial-regime meta-complexity hardness as an assumption.','chain'),
 progress('2026-09-16','The review expands the promise thresholds and uniform padding quantifiers, and checks the later scope comparison.'),
 ],
),notes,sources,status,summary=[
 'Conditional probabilistic Kolmogorov complexity measures how short a program can be when it sees a conditional string and public random bits.',
 'The question asks for randomized NP-hardness even when decoding is allowed arbitrarily large polynomial time.',
 'The target is a promise decision problem with two success-probability thresholds, rather than an exact numerical evaluation.',
 'One reduction per error exponent must work across the time bounds through the permitted polynomial output-length padding.',
 'The known sublinear-time theorem and later conditional hardness statements do not establish this uniform polynomial-regime target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
