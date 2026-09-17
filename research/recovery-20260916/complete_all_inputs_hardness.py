"""Preserve the full converse to Observation 3.11, with all-input rather than length hardness."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-1137'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the exact converse to Observation 3.11 requested by Open Problem 3.12, rather than a generic hardness-to-randomness question.',
 'Corrected the title to almost-all-inputs hardness: each adversary succeeds on only finitely many individual strings, a stronger requirement than failure on some string at each length.',
 'Retained a separate polynomial-time length-preserving function for every fixed adversarial time exponent, with finite exceptions depending on the adversary.',
 'Specified uniform randomized computation, whole-output success probability, and deterministic promise derandomization on all lengths.',
 'Separated the known low-depth converse and the 2024 implicit-output Heavy Avoid equivalences from the unrestricted target.',
 'Preserved the existing importance assessment and related-card links.',
]
sources=[
 'Read Chen–Tell, New ways of studying the BPP=P conjecture, ECCC TR23-094, 29 June 2023: §3.3 printed pp. 14–15/PDF pp. 16–17, Observation 3.11, its proof idea, Open Problem 3.12, Theorem 3.13 and footnote 11; also §5 printed pp. 23–24. The complete premise of Observation 3.11 is used, including its forall-c/exists-f quantifiers.',
 'Checked the publisher abstract and metadata of Chen–Tell, Hardness vs. Randomness, Revised: Uniform, Non-Black-Box, and Instance-wise, SIAM Journal on Computing, DOI 10.1137/22M1475491, published online 4 December 2024. The abstract retains the polynomial-size, depth-n^2 hypothesis and describes removing depth as a potential equivalence. The underlying full proof was not independently certified.',
 'Read Lu–Oliveira–Ren–Santhanam, On the Complexity of Avoiding Heavy Elements, ECCC TR24-115, submitted 14 July 2024 with manuscript dated 13 July: abstract, §1.1.3 Theorems 1.6–1.7, and §5.4 printed pp. 41–43 including Conjectures 5.15–5.16, local-computation convention and Theorem 5.18. Its polynomial-output implicit setting and weaker infinitely-often consequence are not identified with this card’s full-output, all-length conclusion.',
 f'Bounded primary-source searches through {DATE} found these related characterizations and the low-depth result, without a claimed proof of the unrestricted converse. Search coverage is not an exhaustive certification of openness.',
]
status=('The 2023 survey explicitly asks for the converse, and the December 2024 journal abstract still distinguishes the known low-depth theorem from the unrestricted statement. Heavy Avoid work gives related equivalences in an implicit-output setting and weaker simulations without the depth condition. No resolution of the stated converse was found in the bounded later-work check.')
complete(identifier,dict(
 title='Derandomization from almost-all-inputs uniform hardness',
 criterion='reductions',question_type='yes_no',
 formal=r'''Does the following uniform hardness assumption imply \(\mathrm{prBPP}=\mathrm{prP}\)?

For every integer \(c\ge1\), there is a total length-preserving function
\[
f_c:\{0,1\}^{*}\longrightarrow\{0,1\}^{*},\qquad |f_c(x)|=|x|,
\]
computable by a deterministic polynomial-time machine, such that every probabilistic machine \(A\) running in time \(O((n+1)^c)\) succeeds in producing \(f_c(x)\) on only finitely many individual inputs. Precisely,
\[
\forall c\ge1\ \exists f_c\in\mathrm{FP}\ 
\forall A\in\mathrm{RTIME}((n+1)^c)\ \exists N_A\
\forall x\ (|x|\ge N_A\Longrightarrow
\Pr_r[A(x;r)=f_c(x)]<2/3).
\]
Here \(\mathrm{RTIME}\) denotes the time-bounded randomized string-output machines defined below, without an additional correctness promise. The conclusion means that every bounded-error randomized promise problem has a deterministic polynomial-time solver correct on all of its promised inputs.''',
 definitions=r'''A machine is a uniform multitape Turing machine with a fixed finite program and tape alphabets, a read-only binary input, initially blank work tapes and an output tape. A transition reads or writes only the current cells and moves each tape head by at most one cell. Randomized machines additionally have independent unbiased random bits, each requested bit costing a transition. They have no advice or oracle. Runtime includes output writing and is bounded on every input and every sequence of random choices.

The notation \(A\in\mathrm{RTIME}((n+1)^c)\) means that some integer constant \(K_A\ge1\) bounds every run on every input of length \(n\) by \(K_A(n+1)^c\) transitions. The exponent \(c\) is fixed before the machine is chosen; its multiplicative constant may depend on the machine. The output is a finite binary string. A missing, malformed or wrong-length output is unsuccessful. Success requires equality of the entire output string with \(f_c(x)\), not merely correct prediction of one bit or a specified fraction of bits.

The assertion \(f_c\in\mathrm{FP}\) means that one deterministic machine outputs \(f_c(x)\) exactly on every input in time at most \(K_c(n+1)^{d_c}\), for finite integers \(K_c\ge1,d_c\ge0\). Its polynomial degree, program and function may depend on \(c\). No depth bound is imposed on circuits computing the function. There is no requirement that one function be hard for every polynomial time bound, nor that a procedure efficiently produce its program from \(c\).

For each fixed \(c,f_c,A\), the cutoff \(N_A\) is a finite integer that may depend on all three. The requirement applies to every string beyond that cutoff. It is equivalent to saying that the set of strings on which \(A\) outputs \(f_c(x)\) with probability at least \(2/3\) is finite. It is not average-case hardness under the uniform distribution, nor the weaker statement that each sufficiently large length has at least one hard input. The probabilities refer only to \(A\)'s internal random choices.

A bounded-error randomized promise problem is a pair \((Y,N)\) of disjoint sets of finite binary strings for which there exists a randomized polynomial-time machine \(B\), halting on every input and every random tape, whose output is a bit and satisfies
\[
x\in Y\Longrightarrow\Pr[B(x)=1]\ge2/3,\qquad
x\in N\Longrightarrow\Pr[B(x)=1]\le1/3.
\]
There is no correctness requirement outside \(Y\cup N\). The conclusion \(\mathrm{prBPP}=\mathrm{prP}\) requires that for every such pair there exist a uniform deterministic polynomial-time machine \(D\) with \(D(x)=1\) for every \(x\in Y\) and \(D(x)=0\) for every \(x\in N\). This machine must halt in polynomial time also outside the promise, where either answer is allowed. The decider and its polynomial bound may depend on the problem. No efficient compiler from randomized machine descriptions to deterministic ones is requested.

The premise uses all fixed positive integer exponents, so replacing the source's literal \(n^c\) bounds by bounds with fixed multiplicative constants and \(n+1\) preserves its quantified content by increasing the exponent. The conclusion concerns every input length; an infinitely-often or average-case simulation is weaker.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of the implication in the formal question. An affirmative answer may use any method, but must obtain full deterministic promise derandomization from exactly the stated hardness premise, with no added circuit-depth, circuit-hardness or cryptographic assumption. A negative answer must establish the premise and failure of the conclusion in the ordinary unrelativized setting. A theorem for low-depth hard functions, implicit single-bit access to longer outputs, selected input lengths or most inputs alone does not meet the target. Numerical \(1/100\) tolerance does not apply to this binary implication.''',
 source_formulation=dict(text='Observation 3.11 derives polynomial-time functions hard on almost every individual input from promise derandomization; Open Problem 3.12 asks for the converse. Theorem 3.13 proves a converse under an additional circuit-depth restriction.',
 caption='Paraphrase of §3.3, printed pp. 14–15/PDF pp. 16–17 of ECCC TR23-094, 29 June 2023.',
 citation='primary',format='editorial_paraphrase'),
 why='Classical worst-case derandomization uses hardness against arbitrary small circuits. This question asks whether hardness against uniform randomized algorithms, strengthened to cover almost every individual input, already suffices. A positive answer would characterize full promise derandomization through an algorithmic hardness assumption without requiring a circuit lower bound or a shallow implementation of the hard function.',
 references=[
 ref('primary',r'New ways of studying the \(\mathrm{BPP}=\mathrm P\) conjecture','Lijie Chen; Roei Tell',2023,
 'https://eccc.weizmann.ac.il/report/2023/094/',
 '29 June 2023 version; §3.3, Observation 3.11 and Open Problem 3.12, printed pp. 14–15/PDF pp. 16–17; Theorem 3.13 and §5'),
 ref('journal','Hardness vs. Randomness, Revised: Uniform, Non-Black-Box, and Instance-wise','Lijie Chen; Roei Tell',2024,
 'https://epubs.siam.org/doi/10.1137/22M1475491',
 'Published online 4 December 2024; abstract states the low-depth hypothesis and the proposed unrestricted equivalence'),
 ref('heavy','On the Complexity of Avoiding Heavy Elements','Zhenjian Lu; Igor C. Oliveira; Hanlin Ren; Rahul Santhanam',2024,
 'https://eccc.weizmann.ac.il/report/2024/115/',
 '14 July 2024 ECCC version; §1.1.3 Theorems 1.6–1.7; §5.4 printed pp. 41–43, Conjectures 5.15–5.16 and Theorem 5.18'),
 ],
 context_blocks=[
 block('The converse direction is already known: if every bounded-error promise problem has a deterministic polynomial-time solver, then the displayed hardness assumption holds for every fixed adversarial exponent. The missing implication would therefore give an equivalence.'),
 block('Multiple output bits matter. For a single output bit, the two constant-output machines together cover every input; both cannot fail on every sufficiently long input. Length-preserving outputs avoid this elementary obstruction.'),
 block(r'The known sufficient condition has a hard function computable by logspace-uniform polynomial-size Boolean circuits of depth \(n^2\), for a suitable universal adversarial time exponent. The question removes that depth restriction.','journal'),
 block('The cutoff depends on the adversary. It is not a common input-length cutoff excluding every possible finite program, since a program can contain the answer to any particular input.'),
 block('Heavy Avoid connects related hardness assumptions to algorithms that avoid high-probability outputs of circuit samplers. Its equivalence theorem uses implicit access to possibly longer outputs, and the paper still formulates full derandomization without a depth restriction as a conjecture.','heavy'),
 ],
 progress=[
 progress('2021','Chen and Tell introduce the instance-wise framework and prove a sufficient low-depth hardness condition, as summarized in the source survey.'),
 progress('2023-06-29','The survey explicitly asks for the converse to Observation 3.11.'),
 progress('2024-07-14','Heavy Avoid work supplies related implicit-output equivalences and states the unrestricted derandomization conjecture.','heavy'),
 progress('2024-12-04','The journal version retains the low-depth condition in its main hardness-to-randomness statement.','journal'),
 progress(DATE,'The review fixes almost-all-inputs quantifiers and the full promise conclusion; no general resolution is found in the bounded source check.'),
 ],
),notes,sources,status,summary=[
 'For every fixed time exponent, assume that some polynomial-time function defeats each faster randomized algorithm on all but finitely many inputs.',
 'The hard function outputs as many bits as its input, and success means computing the entire output correctly with probability at least two thirds.',
 'The question asks whether this assumption forces deterministic polynomial-time solutions to all bounded-error randomized promise problems.',
 'The hard function and its evaluation time may depend on the adversarial exponent, while the finite exceptional set may also depend on the adversary.',
 'A converse is known with a circuit-depth restriction; the target removes that restriction without weakening the derandomization conclusion.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
