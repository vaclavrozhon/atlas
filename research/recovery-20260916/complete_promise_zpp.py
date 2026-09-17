"""Expand the promise-class derandomization implication without a compiler requirement."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0854'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Conjecture 2.1 and Definitions 2.2–2.5 from Fortnow’s contribution, including the three-output bounded-time machine convention.',
 'Defined both canonical yes/no promise pairs directly from acceptance and rejection probabilities.',
 'Made the all-machines/existential-decider quantifiers explicit, with polynomial time on all inputs and arbitrary answers outside each promise.',
 'Distinguished this implication from total-language ZPP=P, from an efficient compiler, and from low-space reconstruction results.',
 'Preserved the existing importance assessment and related-card links.',
]
sources=[
 'Read Open Problems In Honor of Luca Trevisan, editor-hosted 2024 draft, entire §2 pp. 2–3: Conjecture 2.1, Definitions 2.2–2.5, promise-RP comparison and discussion of relativization. This PDF uses §2 numbering; the separately typeset publication uses different numbering.',
 'Read Pyne–Tell, Using Hardness vs Randomness to Design Low-Space Algorithms, ECCC TR26-045, manuscript dated 30 March 2026: abstract, §2 pp. 3–4 including footnote 5, and the reconstruction-versus-D2P discussion surrounding Problem 11. General deterministic reconstruction is related to prBPP=prZPP; the stated low-space constructions do not prove Fortnow’s unrelativized implication.',
 'Bounded primary-source searches for Promise-ZPP/Promise-BPP derandomization through 16 September 2026 found the original question and later reconstruction work, without a claimed resolution of this implication. This is not an exhaustive openness certificate.',
]
status=('Fortnow’s 2024 contribution explicitly conjectures the implication. The checked 2026 survey develops specialized low-space reconstruction and discusses distinct promise-class equalities; it does not resolve this general implication. No resolution was found in the bounded later-work check.')
complete(identifier,dict(
 criterion='models',question_type='yes_no',
 formal=r'''Does deterministic polynomial-time solvability of every zero-error randomized promise problem imply deterministic polynomial-time solvability of every bounded-error randomized promise problem?

More precisely, for every probabilistic polynomial-time machine \(M\) and every binary string \(x\), let \(p_i^M(x)=\Pr[M(x)=i]\), for \(i\in\{0,1\}\), and define
\[
Y_Z(M)=\{x:p_1^M(x)\ge1/2,\ p_0^M(x)=0\},\qquad
N_Z(M)=\{x:p_0^M(x)\ge1/2,\ p_1^M(x)=0\},
\]
\[
Y_B(M)=\{x:p_1^M(x)\ge2/3\},\qquad
N_B(M)=\{x:p_1^M(x)\le1/3\}.
\]
For \(S\in\{Z,B\}\), let \(\mathcal D_S\) be the statement that, for every such \(M\), there exists a deterministic polynomial-time decider \(D_M\) satisfying
\[
x\in Y_S(M)\Longrightarrow D_M(x)=1,\qquad
x\in N_S(M)\Longrightarrow D_M(x)=0
\]
for every binary string \(x\). Is the implication \(\mathcal D_Z\Longrightarrow\mathcal D_B\) true?''',
 definitions=r'''A probabilistic polynomial-time machine has one fixed finite multitape Turing-machine program, a read-only binary input, finitely many initially blank work tapes, and independent unbiased random bits. Every computation on an input of length \(n\), for every sequence of random choices, halts within \(C(n+1)^d\) transitions for some integers \(C\ge1,d\ge0\) depending only on the machine. Each transition accesses only the current tape cells and moves each head by at most one cell; requesting a random bit takes a transition. The possible final outputs are \(1\) (accept), \(0\) (reject), and \(\bot\) (do not know). There is no advice, oracle, shared external randomness or unbounded unit-cost operation.

The probabilities are over this machine's internal random bits. The worst-case polynomial time bound also bounds the number of bits read, so they can equivalently be evaluated using a uniformly random string of that length, with unused bits ignored. On an input in \(Y_Z(M)\), the machine never rejects and accepts with probability at least one half; otherwise it may output \(\bot\). On an input in \(N_Z(M)\) the symmetric guarantee holds. No guarantee is imposed on other inputs. In the bounded-error definition, both \(0\) and \(\bot\) count as nonacceptance.

A promise problem is a pair \((Y,N)\) of disjoint sets of binary strings. A solver must accept every member of \(Y\) and reject every member of \(N\). Its answer outside \(Y\cup N\) can be arbitrary. The four sets in the question specify the full promise associated with each randomized machine. Quantifying over these full promises is equivalent to quantifying over all promise problems solved by the corresponding randomized machines, including smaller promised subsets.

A deterministic polynomial-time decider is a uniform deterministic machine in the same tape model, with outputs \(0\) and \(1\), which halts on every input within \(C'(n+1)^{d'}\) transitions. The program and constants may depend on \(M\). The decider must run in polynomial time even on inputs outside the promise, but need not recognize whether the promise holds.

The quantifiers are \(\forall M\,\exists D_M,C',d'\), separately in the premise and conclusion. The description of \(M\) is not an additional input to \(D_M\). No effective, polynomial-time or uniform procedure transforming arbitrary machine descriptions into deciders is required. All machines themselves are uniform over their input lengths.

The premise is the source's “Promise-ZPP in P” and the conclusion its “Promise-BPP in P,” also written \(\mathrm{prZPP}\subseteq\mathrm{prP}\) and \(\mathrm{prBPP}\subseteq\mathrm{prP}\). The source uses bounded-time machines permitted to abstain as its zero-error convention. The promise need not cover every binary string; replacing these classes by the corresponding total-language classes changes the question.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of \(\mathcal D_Z\Longrightarrow\mathcal D_B\), with the exact machine, promise and quantifier conventions above. A positive answer must cover every bounded-error randomized promise problem under only the stated premise. A negative answer must establish the premise and failure of the conclusion in the ordinary, unrelativized setting. An oracle separation, a result for one restricted machine class, or the total-language equality \(\mathrm{ZPP}=\mathrm P\) alone does not resolve this implication. This is a binary mathematical proposition, so numerical \(1/100\) tolerance does not relax its correctness or probability thresholds.''',
 source_formulation=dict(text='Conjecture 2.1 asks whether placing Promise-ZPP in P forces Promise-BPP into P; the following definitions specify bounded-time randomized machines and deterministic answers on the promised inputs.',
 caption='Paraphrase of Fortnow’s contribution, §2 pp. 2–3, Conjecture 2.1 and Definitions 2.2–2.5, in the editor-hosted 2024 PDF.',
 citation='primary',format='editorial_paraphrase'),
 why='Zero-error computation can certify an answer when it produces one, while bounded-error computation may return a wrong answer. The question asks whether eliminating randomness for all promised certification tasks already removes its power for every efficient randomized decision task. It tests the strength of a broad derandomization principle and the role of promises in transferring that principle.',
 references=[
 ref('primary','Open Problems In Honor of Luca Trevisan — ZPP and Promise-ZPP','Lance Fortnow; column edited by William Gasarch',2024,
 'https://www.cs.umd.edu/~gasarch/open/LUCA/luca.pdf',
 'Editor-hosted PDF, §2 pp. 2–3, Conjecture 2.1 and Definitions 2.2–2.5'),
 ref('later','Using Hardness vs Randomness to Design Low-Space Algorithms','Edward Pyne; Roei Tell',2026,
 'https://eccc.weizmann.ac.il/report/2026/045/',
 'ECCC TR26-045; manuscript dated 30 March 2026; §2 pp. 3–4, footnote 5, and discussion preceding Problem 11'),
 ],
 context_blocks=[
 block('The implication concerns all promise problems in each class. It does not assert that a deterministic simulation only needs to work on randomized machines whose correctness condition holds on every input.'),
 block('The corresponding premise for one-sided-error promise algorithms is known to suffice for bounded-error promise derandomization. Fortnow asks whether the weaker zero-error premise also suffices.'),
 block('The reverse implication follows from the standard inclusion of zero-error promise computation in bounded-error promise computation, using constant repetition to reduce abstention probability. The unproved direction is the one stated in the question.'),
 block('The 2024 source distinguishes promises from total languages and explains why the familiar self-reduction argument for another promise class does not directly preserve the zero-error promise.'),
 block('The 2026 survey connects general deterministic reconstruction to equality of the two randomized promise classes and develops specialized low-space constructions. Those statements neither assume nor establish exactly the implication asked here.','later'),
 ],
 progress=[
 progress('2024','Fortnow formulates the implication explicitly and supplies the three-output promise conventions.'),
 progress('2026-03-30','Pyne and Tell survey specialized reconstruction tools and distinguish several promise-derandomization principles.','later'),
 progress('2026-09-16','The review expands both promise pairs and the simulation quantifiers; the checked later work gives no resolution of the general implication.'),
 ],
),notes,sources,status,summary=[
 'The question asks whether derandomizing every zero-error promise problem also derandomizes every bounded-error promise problem.',
 'Zero-error machines may abstain, but whenever a promised input receives a definite answer that answer is correct.',
 'Bounded-error machines instead distinguish acceptance probabilities at least two thirds from probabilities at most one third.',
 'Each randomized machine may have its own deterministic polynomial-time decider, which must halt on all inputs and be correct on the promise.',
 'The target is a general unrelativized implication; total-language equalities and specialized low-space results do not settle it.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
