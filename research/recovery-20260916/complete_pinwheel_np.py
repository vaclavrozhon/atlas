"""Complete NP membership for ordinary infinite pinwheel packing."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6078'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the ordinary infinite packing problem with an explicit list of binary periods; distinguished exact-spacing, compact-multiplicity and finite-visit variants.',
 'Defined every sliding window, idle slots and the full two-sided integer time axis, with no density promise.',
 'Expanded NP membership into one uniform polynomial-time verifier with polynomially bounded certificates; certificates need not explicitly list a periodic schedule.',
 'Updated the inherited hardness discussion using the April 2026 NP-hardness preprint, while retaining the unresolved membership question.',
 'Individually assessed importance from the infinite-schedule versus finite-certificate boundary, rather than retaining the provisional score.',
]
sources=[
 'Read Kobayashi–Lin, ISAAC 2025, Article 47, abstract and §1 pp. 47:1–47:5, including the ordinary packing definition, explicit NP-membership question on p. 47:2, distinctions from exact and dense variants, and input-size convention.',
 'Read Kleinberg–Mishra, arXiv:2604.13974v1 (15 April 2026), abstract, §1 pp. 1–3, §2 definitions and Lemma 2.2 p. 4, §3 approximate-decision definition p. 5, and Theorem 4.23 p. 16. The ordinary explicit-list problem is proved NP-hard; the introduction distinguishes prior compact encodings and retains the PSPACE upper bound without a smaller known class. The full hardness proof was not independently certified.',
 'Read Kanellopoulos, arXiv:2607.28574v2 (7 September 2026), abstract and introductory discussion of perpetual packing/covering, the recent weak NP-hardness result and the separate finite-visit problems. Finite NP-completeness is not an NP-membership result for the present infinite problem.',
 f'Checked arXiv version metadata and bounded later-work searches through {DATE}; no resolution of ordinary infinite packing membership in NP was found. The July 2026 journal extension of the inherited source was located, but its full theorems were not used without access to the full text.',
]
status='The 2025 source explicitly asks whether ordinary Pinwheel Packing belongs to NP. Kleinberg and Mishra’s April 2026 preprint proves NP-hardness for the ordinary explicit-list encoding, but retains the gap to the PSPACE upper bound. September 2026 work distinguishes this perpetual problem from NP-complete finite-visit variants. No resolution of NP membership was found in the bounded review.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does ordinary Pinwheel Packing belong to \(\mathrm{NP}\)?

An instance is an explicit finite list of positive integers \(a_1,\ldots,a_k\), written in binary, with \(k\ge1\). It is feasible if there exists a schedule \(\sigma:\mathbb Z\to\{0,1,\ldots,k\}\) such that
\[
\forall i\in\{1,\ldots,k\}\ \forall t\in\mathbb Z\
\exists j\in\{0,\ldots,a_i-1\},\qquad \sigma(t+j)=i.
\]
Thus one machine must execute task \(i\) at least once in every \(a_i\) consecutive time slots, forever.

Precisely, do there exist one uniform deterministic verifier \(V\) and integers \(C,c\ge1\) such that every valid encoded instance \(x\), of bit length \(L\), satisfies
\[
x\text{ is feasible}\quad\Longleftrightarrow\quad
\exists z\in\{0,1\}^{\ast}\ 
\bigl(|z|\le C(L+1)^c\ \text{and}\ V(x,z)=1\bigr),
\]
and \(V\) halts on every pair \((x,z)\) within \(C(|x|+|z|+1)^c\) steps?''',
 definitions=r'''Time is discrete and indexed by all integers. The value \(\sigma(t)=i>0\) means that the machine executes task \(i\) during slot \(t\); the value zero denotes an idle slot. At most one task executes in any slot. A task has unit execution time, may be executed arbitrarily many times, and must obey its recurrence requirement on every window, including windows crossing any chosen origin of time. There is no finite horizon, initial-state input, release date or online sequence of unknown tasks.

The number \(a_i\) is an upper bound on the gap between successive executions of task \(i\). Gaps need not equal \(a_i\), and executions may be more frequent. Every task is distinct, even if several periods coincide. Idle slots can be filled with task 1 without harming any recurrence requirement, so allowing them does not change feasibility for \(k\ge1\).

The instance contains the whole list of periods, with no compressed multiplicities. Encode it by \(1^k0\), followed in order by a code for each \(a_i\). For a positive integer \(a\), let \(b\) be the bit length of its ordinary binary representation; its code is \(1^b0\) followed by those \(b\) bits. Require a leading one in each binary representation and no trailing bits. Then
\[
L=k+1+\sum_{i=1}^k(2\lfloor\log_2 a_i\rfloor+3).
\]
Malformed strings are not feasible instances and must be rejected by the verifier for every certificate. The chosen encoding is polynomially interconvertible with the usual explicit binary-list encodings; periods are not written in unary.

There is no promise on the density \(\sum_i 1/a_i\), the number of distinct periods or their magnitudes. For example, all instances whose density exceeds one are infeasible, but the verifier must handle them as well. Restricting attention to density exactly one, a fixed number of tasks or finitely many required executions would change the scope.

The verifier is a deterministic multitape Turing machine with a fixed finite program, fixed finite tape alphabets, read-only inputs \(x,z\) and initially blank work tapes. Each transition accesses only the cells under its heads and moves each head by at most one cell. Parsing, arithmetic and all verification work are charged. There is no advice, randomness, oracle or free preprocessing.

The certificate \(z\) may be any finite binary string. A positive answer may use any sound certificate representation; it is not required to list the entire period of a schedule, or to provide a polynomial-time procedure for finding a certificate. The running-time guarantee applies to every supplied certificate, including incorrect and overlong ones. The membership equivalence only quantifies over certificates of the displayed length bound.

Feasibility is an exact decision property, so the numerical \(1/100\) approximation convention does not relax a recurrence deadline or permit any fraction of violated windows.''',
 answer_criterion=r'''Supply a complete Lean-checked construction of a verifier and constants satisfying the polynomial certificate, running-time, completeness and soundness conditions; or supply a complete Lean-checked proof that no such verifier and constants exist. An NP-hardness proof alone does not refute NP membership. A polynomial-space algorithm, an exponentially long explicit periodic schedule, an approximation that relaxes the periods, or an NP verifier for a finite-visit or restricted-density variant does not meet this target.''',
 source_formulation=dict(
 text='The ISAAC source records a PSPACE upper bound for Pinwheel Packing and explicitly leaves membership in NP open. The card asks this question for its ordinary infinite packing model, with the full explicit list of binary periods.',
 caption='Paraphrase of Kobayashi–Lin, §1.1, p. 47:2, with the encoding and certificate quantifiers expanded.',
 citation='primary',format='editorial_paraphrase'),
 why='A compact list of recurring service requirements describes an infinite scheduling obligation. NP membership would show that feasibility always has a short, efficiently checkable finite explanation, even when a directly listed repeating schedule may be very long. Together with the 2026 hardness result, a positive answer would classify this long-studied perpetual scheduling problem as NP-complete.',
 importance=dict(score=83,method='editorial',
  reason='A long-standing complexity-class boundary for a basic recurrent scheduling model, connecting infinite behavior, succinct numerical input and finite certificates. The recent NP-hardness theorem makes the unresolved gap between NP membership and the PSPACE upper bound particularly concrete.',
  basis='Individual review of the explicit ISAAC 2025 membership question, the April 2026 ordinary-encoding hardness theorem and the September 2026 distinction from finite scheduling.'),
 references=[
 ref('primary','Hardness and Fixed Parameter Tractability for Pinwheel Scheduling Problems',
  'Yusuke Kobayashi; Bingkai Lin',2025,
  'https://doi.org/10.4230/LIPIcs.ISAAC.2025.47',
  'ISAAC 2025, LIPIcs 359, Article 47; §1.1, pp. 47:1–47:2, definition and NP-membership question; §§1.2–1.3, variants and input convention'),
 ref('hardness','NP-Hardness and a PTAS for the Pinwheel Problem',
  'Robert Kleinberg; Ahan Mishra',2026,'https://arxiv.org/abs/2604.13974v1',
  'Preprint version 1, 15 April 2026; §1 pp. 1–3, §2 Lemma 2.2 p. 4, §3 p. 5 and Theorem 4.23 p. 16'),
 ref('finite','Finite Pinwheel Covering',
  'Sotiris Kanellopoulos',2026,'https://arxiv.org/abs/2607.28574v2',
  'Preprint version 2, 7 September 2026; abstract and §1, perpetual versus finite-visit packing and covering'),
 ],
 context_blocks=[
 block('The inherited question concerns membership in NP, independently of whether the problem is NP-hard. The source gives PSPACE as the established general upper bound.'),
 block(r'Every feasible integer-period instance has a periodic feasible schedule with period at most \(\prod_i a_i\). The state graph used to prove this has one coordinate for the elapsed time of each task. This bound can be exponential in the binary input length, so the existence of a periodic schedule alone does not provide a polynomial-length certificate.','hardness'),
 block('The April 2026 preprint proves NP-hardness for the ordinary explicit-list encoding, including instances of density one. Earlier hardness results for exact spacing or binary-encoded multiplicities did not establish this ordinary-encoding theorem.','hardness'),
 block('The same preprint gives an approximation scheme that permits multiplicative relaxation of the recurrence limits. Such a relaxation is different from verifying feasibility with every original deadline unchanged.','hardness'),
 block('The September 2026 finite-covering paper explicitly separates perpetual scheduling from finite-visit problems. NP-completeness of a model requiring only finitely many executions does not supply certificates for an unbounded schedule.','finite'),
 ],
 progress=[
 progress('2025','The source explicitly records ordinary Pinwheel Packing membership in NP as open.'),
 progress('2026-04-15','A preprint proves NP-hardness with the ordinary explicit list of periods and also gives an approximation scheme for relaxed recurrence limits.','hardness'),
 progress('2026-09-07','The revised finite-covering preprint retains the distinction between perpetual scheduling and NP-complete finite-visit variants.','finite'),
 progress(DATE,'The review states the exact binary-input NP-membership target and updates the hardness context without treating NP-hardness as a negative answer.'),
 ],
),notes,sources,status,summary=[
 'Pinwheel packing asks one machine to execute every recurring task often enough to meet all of its sliding-window deadlines.',
 'The input is an explicit list of positive recurrence limits written in binary, while the schedule extends indefinitely.',
 'The question is whether every feasible instance has a polynomial-length certificate checkable in polynomial time.',
 'A polynomial-space algorithm and finite periodic schedules are known, but the available period bound can be exponential in the input length.',
 'An April 2026 preprint proves NP-hardness, while the checked literature leaves membership in NP unresolved.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
