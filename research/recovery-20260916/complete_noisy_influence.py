"""Archive the exact COLT 2025 conjecture after matching COLT 2026 Theorem 1."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1540'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Open Problem 1 and the independently resampled noisy bit-query model from the COLT 2025 paper.',
 'Specified a worst-input expected query count, adaptive randomized algorithms, fresh independent noise on every repeated query and error at most one third on every input.',
 'Expanded the asymptotic lower bound into a constant depending only on the fixed noise probability, uniformly over all Boolean functions and dimensions.',
 'Retained the source convention that t*log(t) is zero at zero, rather than silently strengthening the low-influence target.',
 'Matched the exact claim to published COLT 2026 Theorem 1, and checked the main graph-theorem specialization and relevant proof structure.',
 'Assessed importance individually and archived the original lower-bound question as resolved affirmatively.',
]
sources=[
 'Read Gu–Li–Xu, Tight Bounds for Noisy Computation of High-Influence Functions, Connectivity, and Threshold, COLT 2025, PMLR 291:2540–2591, introduction and §1.1, Theorem 1 and Open Problem 1, PDF pp. 2–4.',
 'Checked the publisher page and downloaded the final Gu–Li–Xu COLT 2026 paper, A Unified Lower Bound on the Noisy Query Complexity of Boolean Functions, PMLR 336:2940–2962, conference 29 June–3 July 2026. Read its definition of N_p, Theorem 1 PDF p. 2, and Theorems 2–3 with the degeneracy specialization PDF p. 3.',
 'Read arXiv:2606.11448v1 submitted 9 June 2026: §4.1 the three-phase simulation Proposition 7 and amplification step; §4.3 the weighted-degree Balance Lemma 9 and proof; and the final posterior-balance conclusion in §4.4. The general theorem and the influence corollary have the required all-function and expected-cost scope.',
 'Checked that the graph of sensitive edges has average degree equal to total influence and that a graph has degeneracy at least half its average degree. The main theorem with log(1+d) covers the bounded-degeneracy cases as well as the asymptotic large-influence regime.',
 'This is a model and published-result review with selected proof checks. The complete probability estimates in the main theorem were not independently reconstructed and no Lean certification is claimed.',
]
status=('Resolved affirmatively by Gu, Li and Xu, COLT 2026, Theorem 1. The published statement proves the exact universal influence lower bound '
 'for adaptive randomized noisy-query algorithms with worst-input expected cost and constant error. '
 'The June preprint and final conference version were matched to the original COLT 2025 Open Problem 1. '
 'The card is archived as a resolved historical question, without claiming an independent Lean formalization.')
complete(identifier,dict(
 title='Influence lower bound for noisy query complexity',
 criterion='resources',question_type='yes_no',status='resolved',
 formal=r'''Historical question, resolved affirmatively: for every fixed noise probability \(p\in(0,1/2)\), does there exist a constant \(c_p>0\) such that for every \(n\ge1\) and every total Boolean function \(f:\{0,1\}^n\to\{0,1\}\),
\[
\mathsf N_p(f)\ge c_p\,\mathsf I(f)\log_2\mathsf I(f)\ ?
\]
Here \(\mathsf N_p(f)\) is adaptive randomized noisy bit-query complexity with error at most \(1/3\), measured by the worst-input expected number of queries, and \(\mathsf I(f)\) is total influence under the uniform distribution. Both are defined below. The constant may depend on \(p\), but not on \(n\), \(f\) or the algorithm.''',
 definitions=r'''Fix a total Boolean function \(f\) and an unknown fixed input \(x=(x_1,\ldots,x_n)\). At its \(t\)-th query an algorithm selects an index \(i_t\in[n]\) and receives
\[
Y_t=x_{i_t}\oplus Z_t,\qquad
\Pr[Z_t=1]=p.
\]
The noise bits \(Z_t\) are mutually independent and independent of the algorithm's own random bits. An index can be queried repeatedly; every repetition receives fresh noise. The input itself is not resampled or corrupted permanently. The algorithm may know \(f,n,p\), and may choose its next query and stopping decision using the entire answer history and its private randomness. Local computation is free.

An admissible algorithm terminates almost surely on every input and outputs a bit \(A(x)\) satisfying
\[
\Pr[A(x)\ne f(x)]\le1/3\qquad\text{for every }x\in\{0,1\}^n.
\]
The probability includes query noise and private randomness. If \(T_A(x)\) is its random number of queries, define
\[
\mathsf N_p(f)=
\inf_{A\text{ admissible}}\ 
\max_{x\in\{0,1\}^n}\mathbb E[T_A(x)].
\]
An algorithm with infinite expected cost does not improve this infimum. The algorithm can be chosen separately for each \(f\); there is no uniformity or computation-time requirement. This is a worst-input expectation, not an average over uniformly random inputs or a bound that must hold for every noise realization.

For \(i\in[n]\), write \(x^{\oplus i}\) for the string obtained by flipping the \(i\)-th bit. The influence of that coordinate and total influence are
\[
\operatorname{Inf}_i(f)=
\Pr_{X\leftarrow\{0,1\}^n}[f(X)\ne f(X^{\oplus i})],
\qquad
\mathsf I(f)=\sum_{i=1}^{n}\operatorname{Inf}_i(f).
\]
Thus \(\mathsf I(f)\in[0,n]\) is the average, over uniform inputs, of the number of single-bit flips that change the answer. This averaging only defines the structural parameter; it does not weaken the algorithm's required correctness.

All logarithms in the target are base two, with \(t\log_2 t=0\) at \(t=0\). For \(0<t<1\) the right-hand side is nonpositive, and for \(t=1\) it is zero. These cases impose no additional positive lower bound. The substantive claim is uniform growth in the influence, including intermediate influence far below \(n\). It is not a statement with a constant uniform as \(p\) tends to zero or to \(1/2\).''',
 answer_criterion=r'''The original benchmark target is a complete Lean-checked proof or refutation of the displayed universal lower-bound proposition with exactly the specified noise, cost and error conventions. The published affirmative theorem settles the research question, but a bibliographic citation alone is not a Lean proof. A proof only for nonadaptive algorithms or only when total influence is a fixed positive fraction of \(n\) does not meet the original target. This is a binary asymptotic lower-bound assertion; numerical \(1/100\) tolerance does not alter its quantifiers or resource measure.''',
 source_formulation=dict(
 text='Open Problem 1 asks whether every Boolean function requires noisy-query complexity at least a constant times its total influence times the logarithm of that influence.',
 caption='Paraphrase of COLT 2025 §1.1, Open Problem 1, PDF p. 4; the fixed independent-noise convention is defined in the introduction.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=79,method='editorial',
 reason='The question seeks a uniform noise-specific query lower bound from a central structural parameter of every Boolean function, beyond the previously proved high-influence regime.',
 basis='Individual assessment of the all-function scope, the logarithmic cost of unreliable observations and its connection to average sensitivity; the historical significance is retained after resolution.'),
 why='A Boolean function may change on many single-bit perturbations, yet an adaptive algorithm can concentrate its effort unevenly. The theorem shows that average sensitivity still forces an additional logarithmic query cost under independently repeated noise. It gives a general structural lower bound instead of a separate argument for each computational task.',
 references=[
 ref('primary','Tight Bounds for Noisy Computation of High-Influence Functions, Connectivity, and Threshold',
 'Yuzhou Gu; Xin Li; Yinzhan Xu',2025,'https://proceedings.mlr.press/v291/gu25a.html',
 'COLT 2025, PMLR 291:2540–2591; §1.1, Theorem 1 and Open Problem 1, PDF pp. 3–4'),
 ref('resolution','A Unified Lower Bound on the Noisy Query Complexity of Boolean Functions',
 'Yuzhou Gu; Xin Li; Yinzhan Xu',2026,'https://proceedings.mlr.press/v336/gu26a.html',
 'COLT 2026, PMLR 336:2940–2962; Theorem 1 PDF p. 2, Theorems 2–3 and their implication PDF p. 3; conference 29 June–3 July 2026'),
 ref('preprint','A Unified Lower Bound on the Noisy Query Complexity of Boolean Functions',
 'Yuzhou Gu; Xin Li; Yinzhan Xu',2026,'https://arxiv.org/abs/2606.11448v1',
 'Submitted 9 June 2026; §§1.1 and 4, Proposition 7, Balance Lemma 9 and the concluding posterior-balance bound; preprint version of the published resolution'),
 ],
 context_blocks=[
 block('The COLT 2025 paper proves the proposed lower bound when total influence is proportional to the input length, and explicitly asks for the all-function extension.'),
 block('Fresh independent noise makes repeated queries useful. Persistent corruption or an adversary choosing erroneous answers defines a different problem and is not covered by the statement.'),
 block(r'Maximum sensitivity cannot replace average sensitivity in this logarithmic lower bound for arbitrary adaptive algorithms: the source notes that OR has maximum sensitivity \(n\) but noisy query complexity of order \(n\).'),
 block('The COLT 2026 theorem applies to every Boolean function and proves the original influence bound with a constant that depends only on the noise probability. It retains expected query cost and adaptive randomized algorithms.','resolution'),
 block('The resolving paper also proves a stronger statement based on subgraphs of the Boolean hypercube containing only edges where the function changes. The published influence theorem is an explicit consequence, not an extrapolation from selected examples.','resolution'),
 block('The original question asks for a lower bound, not an exact characterization of noisy query complexity. The stronger theorem and its further applications do not change the archived target.','resolution'),
 ],
 progress=[
 progress('2025','The COLT paper proves the high-influence case and poses the general statement as Open Problem 1.'),
 progress('2026-06-09','The authors post the all-function theorem in arXiv:2606.11448v1.','preprint'),
 progress('2026','The theorem is published in COLT 2026, PMLR volume 336.','resolution'),
 progress('2026-09-16','The model and exact theorem are matched to the original question, which is archived as resolved affirmatively.','resolution'),
 ],
),notes,sources,status,summary=[
 'Each bit query returns an independently corrupted answer, and an algorithm may adaptively repeat queries.',
 'The historical question asks whether total influence forces a matching influence-times-log-influence lower bound.',
 'Cost is the worst-input expected number of queries, with error at most one third on every input.',
 'The COLT 2026 theorem proves the claimed bound for every Boolean function and every fixed nonzero noise rate below one half.',
 'The original lower-bound target is preserved and archived as resolved affirmatively.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],
 archive_reason='Resolved affirmatively by Gu–Li–Xu, COLT 2026, PMLR 336:2940–2962, Theorem 1; exact match to COLT 2025 Open Problem 1 with adaptive worst-input expected noisy-query cost.')
