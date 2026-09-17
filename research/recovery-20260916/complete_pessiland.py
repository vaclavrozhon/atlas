"""Complete the retained infinitely-often Pessiland implication."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6453';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the infinitely-often strong inversion convention and uniform classical adversaries, rather than replacing the target by eventual security or nonuniform security.',
 'Defined NP verification, an exact uniform polynomial-time sampler, and one fully polynomial randomized heuristic scheme with an explicitly represented accuracy parameter.',
 'Expanded the security quantifiers over inverters, inverse-polynomial thresholds and arbitrarily large lengths; any same-length preimage is successful inversion.',
 'Replaced the erroneous survey section locator by §§2.2–2.3, Definitions 11 and 14–15, and distinguished samplable distributions from other conventions for the notation DistNP.',
 'Checked the June revision and its correction to the April learning characterization, as well as August oracle results and September information-density characterizations, without treating them as a resolution.',
 'Preserved importance 95, removed speculative construction advice, and required a complete Lean-checked proof of the unrelativized implication or its actual logical negation.',
]
sources=[
 'Read Hirahara–Nanashima, ECCC TR26-052 Revision 1, 23 June 2026, abstract, §1 pp. 1–4 including Corollary 1.4, Theorem 1.5 and Corollary 1.6; §1.3 p. 7; §3 sampler definitions p. 14 and §3.1 Definition 3.1 p. 15. The source uses polynomial input/output length in a security parameter; the card retains the n-bit-input normalization and spells out its infinitely-often probability quantifiers.',
 'Checked the live ECCC report page on 17 September 2026: revision 1 is the latest listed version. Its change note identifies a flaw in the old Lemma 5.10 and replaces the small-superconstant advice regime by sufficiently large fixed advice constants. No full proof audit of the revised characterization was undertaken.',
 'Read Bogdanov–Trevisan, Average-Case Complexity, arXiv:cs/0606037v3 of 17 August 2021, §§2.2–2.3, Definitions 11 and 14–15. The card represents an inverse accuracy parameter by a unary integer k and retains the two-level input-versus-algorithm probability convention, using the equivalent constant success threshold two thirds.',
 'Read Chen–Morimae–Yamakawa, Quantum Pessiland, arXiv:2608.29493v1 of 30 August 2026, primary abstract and saved PDF p. 1. Its classical- and quantum-oracle separations are recorded as relativized statements, not an unrelativized negative answer to this classical implication.',
 'Read the primary abstract of Nandakumar–Pulari–S–Sarma, One-Way Functions and Polynomial-Time Dimension, APPROX/RANDOM 2026 Article 44, published 9 September 2026. Its reverse implication assumes an almost-sure uniform separation of two information-density notions over an efficiently sampled infinite-sequence source, not arbitrary average-case NP hardness. No full proof audit was performed.',
 f'Bounded targeted later-work searches through {DATE} found no verified resolution. Related 2026 results with an additional instance-hiding proof hypothesis were not identified with the unconditional average-case premise.',
]
complete(identifier,dict(
 criterion='reductions',question_type='yes_no',
 formal=r'''Does
\[
 \mathrm{DistNP}\not\subseteq\mathrm{HeurBPP}
 \quad\Longrightarrow\quad
 \text{an infinitely-often one-way function exists}
\]
hold under the uniform classical definitions below? In this card \(\mathrm{DistNP}\) uses exactly polynomial-time samplable input distributions, and infinitely-often security means that for every polynomial-time inverter and every inverse-polynomial success threshold there are arbitrarily large lengths at which the inverter's success falls below that threshold.''',
 definitions=r'''All algorithms are uniform classical Turing machines. A probabilistic polynomial-time algorithm uses independent fair random bits and has a polynomial worst-case running-time bound over every random tape. Its polynomial can depend on its fixed program. No nonuniform advice, quantum computation or external oracle is allowed.

A language \(L\subseteq\{0,1\}^*\) belongs to \(\mathrm{NP}\) if there exist a polynomial \(p\) and a deterministic polynomial-time verifier \(V\) such that
\[
 x\in L\quad\Longleftrightarrow\quad
 \exists w\in\{0,1\}^{\le p(|x|)}\ V(x,w)=1.
\]
Write \(L(x)\in\{0,1\}\) for its membership bit. An exactly polynomial-time samplable ensemble is a sequence \(D=(D_n)_{n\ge1}\) of distributions on \(\{0,1\}^n\) for which one probabilistic polynomial-time sampler \(S\), on unary input \(1^n\), always outputs an \(n\)-bit string with distribution exactly \(D_n\). Samplability does not require efficiently computing the probability assigned to a given output string. Here \(\mathrm{DistNP}\) is the class of all pairs \((L,D)\) with these properties; conventions using efficiently computable cumulative probabilities are not the definition of this card.

A pair \((L,D)\) belongs to \(\mathrm{HeurBPP}\) if there are one randomized algorithm \(A\) and one polynomial \(p\) such that, for every \(n\ge1\), every integer accuracy parameter \(k\ge2\), and every \(x\in\{0,1\}^n\), the computation \(A(x,1^k)\) always returns a bit in at most \(p(n+k)\) steps, and
\[
 \Pr_{x\sim D_n}\!\left[
   \Pr_{\omega}\bigl[A(x,1^k;\omega)=L(x)\bigr]\ge\frac23
 \right]\ge1-\frac1k.
\]
The inner probability is over the fresh coins of \(A\); the outer probability is over the input distribution. The unary parameter makes polynomial dependence on inverse accuracy explicit. The same program works for every \(n,k\); separate unrelated algorithms for different accuracies do not constitute this scheme. It may depend on the fixed language and sampler, but has no membership oracle for \(L\). No guarantee is required on the exceptional input fraction of size at most \(1/k\). This is an error-prone heuristic scheme, not an algorithm required to detect all its mistakes or output an explicit failure symbol.

Consequently, the premise states that there exist a language \(L\in\mathrm{NP}\) and one such sampler \(S\) for which no scheme satisfying all these bounds exists. It does not assume that every NP language, every sampler or every individual input is hard, or that hardness is present at all sufficiently large lengths.

A candidate one-way function is a total deterministic polynomial-time function \(f:\{0,1\}^*\to\{0,1\}^*\). Its output length is therefore polynomially bounded in its input length; injectivity and length preservation are not required. For a uniform probabilistic polynomial-time inverter \(J\), define
\[
 s_{f,J}(n)=
 \Pr_{x\leftarrow U_n,\,\omega}\!\left[
 z\in\{0,1\}^n\ \land\ f(z)=f(x),\quad
 z=J(1^n,f(x);\omega)
 \right],
\]
where \(U_n\) is uniform on all \(n\)-bit strings and is independent of the inverter's coins. Any preimage of the sampled image with length exactly \(n\) counts as success; recovering the particular sampled \(x\) is not required. Failure symbols or outputs of another length count as unsuccessful inversion. The unary length is supplied, so inversion is not made hard by concealing the input length. Running time is polynomial in the full inverter input length and hence polynomial in \(n\) in this experiment.

The function \(f\) is infinitely-often one-way if
\[
 \forall J\ \forall c\in\mathbb Z_{\ge1}\ \forall N\in\mathbb Z_{\ge2}\quad
 \exists n\in\mathbb Z_{\ge N}:\quad s_{f,J}(n)<n^{-c},
\]
where \(J\) ranges over all the uniform polynomial-time inverters just defined. The function \(f\) is chosen once and works against all of them. Hard lengths may depend on \(J\) and \(c\); this does not require one common infinite set of hard lengths for every inverter. Replacing the final quantifiers by a guarantee for every sufficiently large \(n\) would impose the stronger, eventual security target and is not this question.

The desired conclusion is existence of at least one such function from the stated average-case hardness premise alone. A positive answer may use any mathematical argument; it is not restricted to a black-box construction or a reduction with a predetermined number of oracle calls. The question is about ordinary unrelativized computation.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed implication, with the stated sampler, heuristic and inversion quantifiers, or a complete Lean-checked proof of its logical negation.

A negative answer must establish both that some \((L,D)\) satisfies the average-case hardness premise and that no total polynomial-time function has the specified security. The latter means that for every candidate \(f\) there are a uniform polynomial-time inverter \(J\), an integer \(c\ge1\) and a threshold \(N\ge2\) with
\[
 s_{f,J}(n)\ge n^{-c}\quad\text{for every }n\ge N.
\]
Showing only that a particular proposed construction is insecure, or giving an oracle separation, does not prove this unrelativized negation. A result requiring a special language, a special sampler or an additional cryptographic premise suffices only if the stated general assumption is proved to imply those extra hypotheses. Strengthening the premise to hardness at all sufficiently large lengths answers a different implication unless a reduction from the retained premise is supplied.''',
 source_formulation=dict(text='The revised source asks whether average-case NP hardness implies one-way functions, and explicitly uses infinitely-often one-way functions in Theorem 1.5. This card retains that weaker security target, with all quantifiers written out, rather than silently imposing security at every sufficiently large length.',caption='Editorial paraphrase of Hirahara–Nanashima, ECCC TR26-052 Revision 1, introduction, Corollary 1.4, Theorem 1.5 and Definition 3.1; n-bit normalization and infinitely-often convention retained from the card.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A Sharp Characterization of Pessiland','Shuichi Hirahara; Mikito Nanashima',2026,'https://eccc.weizmann.ac.il/report/2026/052/revision/1/','Revision 1, 23 June 2026; §1 pp. 1–4, Corollary 1.4 and Theorem 1.5; §1.3 p. 7; §3.1 Definition 3.1 p. 15; report page records the correction of the April version'),
 ref('averagecase','Average-Case Complexity','Andrej Bogdanov; Luca Trevisan',2006,'https://arxiv.org/abs/cs/0606037v3','October 2006 survey, revised 17 August 2021; §§2.2–2.3, Definitions 11 and 14–15, fully polynomial schemes and randomized heuristics'),
 ref('quantum','Quantum Pessiland','Boyang Chen; Tomoyuki Morimae; Takashi Yamakawa',2026,'https://arxiv.org/abs/2608.29493v1','30 August 2026; abstract and p. 1, explicit classical- and quantum-oracle qualifications'),
 ref('dimension','One-Way Functions and Polynomial-Time Dimension','Satyadev Nandakumar; Subin Pulari; Akhil S; Suronjona Sarma',2026,'https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.44','Published 9 September 2026; primary abstract, reverse implication from a uniform information-density separation over efficiently samplable sources; full proof not independently audited'),
 ],
 context_blocks=[
 block('The premise concerns difficulty of deciding membership on efficiently sampled inputs. The conclusion concerns finding preimages of an efficiently computed function on uniform inputs. The possibility of the former without the latter is the Pessiland question.'),
 block('A heuristic scheme has two distinct probability levels: it must answer reliably on most inputs, and it receives an accuracy parameter controlling the exceptional fraction. A fixed average error bound or worst-case NP hardness is not the premise defined here.','averagecase'),
 block(r'The June 2026 revision relates average-case NP hardness and one-way functions to two nearby approximation factors for a learning task, \(\ell^{1-o(1)}\) and \(O(\ell)\). It leaves that gap open. Its valid parameter regime uses sufficiently large fixed advice-complexity constants; the stronger regime asserted in April was corrected.'),
 block('Infinitely-often security is deliberate: the hard input lengths can recur sparsely and depend on the inverter. The source separately notes a route to eventual security when its average-case premise is strengthened to eventual hardness.'),
 block('The August 2026 quantum results construct relativized worlds with average-case hardness but absent cryptographic primitives. Their oracle qualifications prevent interpreting them as a negative solution in the ordinary classical model.','quantum'),
 block('The September information-density characterization gives another condition implying infinitely-often one-way functions. Its hypothesis is a particular separation over sampled infinite sequences, not the unrestricted average-case NP premise of this card.','dimension'),
 ],
 progress=[progress('2026-06-23','The revised learning characterization records a remaining quantitative gap and corrects the parameter regime of the April version.'),progress('2026-08-30','Quantum and classical oracle separations are announced for related cryptographic primitives.','quantum'),progress('2026-09-09','A further information-density characterization yields infinitely-often one-way functions from its specific separation hypothesis.','dimension')],
),notes,sources,'The latest listed June 2026 revision explicitly retains the Pessiland question. The checked August oracle separations and September information-density characterization do not establish either direction of the requested unrelativized resolution. Bounded primary-source checks through 17 September 2026 found no verified solution to this precise infinitely-often implication; the cited proofs were not independently certified.',summary=[
 'Some NP problems may remain hard to decide on inputs generated by an efficient sampler.',
 'This card asks whether such distributional hardness alone guarantees a polynomial-time function that is hard to invert at infinitely many lengths.',
 'The premise rules out one randomized heuristic scheme that works at every requested accuracy.',
 'The conclusion requires each polynomial-time inverter to have arbitrarily small inverse-polynomial success at arbitrarily large lengths, with those lengths allowed to depend on the inverter.',
 'A complete Lean-checked answer must settle the unrelativized implication, rather than a stronger eventual-hardness variant or an oracle-world separation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
