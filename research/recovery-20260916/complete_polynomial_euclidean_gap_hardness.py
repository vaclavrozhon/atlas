"""Retain the Euclidean polynomial-factor target after checking August 2026 progress."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0655';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Polynomial-factor Euclidean SVP hardness assuming NP is not contained in RP',
 status='source_open',criterion='assumptions',question_type='yes_no',
 formal=r'''Is the following implication true?
\[
\mathrm{NP}\not\subseteq\mathrm{RP}
\quad\Longrightarrow\quad
\exists\varepsilon\in\mathbb Q,\ 0<\varepsilon<1/2:
\operatorname{GapSVP}^{(2)}_{n^\varepsilon}\notin\operatorname{PromiseBPP}.
\]
Thus the target is a fixed positive power of the lattice rank in the Euclidean norm, with no classical randomized polynomial-time algorithm under the specified standard assumption. The exponent may be arbitrarily small but must be independent of the input.''',
 definitions=r'''An input is an integer matrix \(B\in\mathbb Z^{m\times n}\) of full column rank, with \(m\ge n\ge2\), together with a positive rational \(r\). All dimensions, matrix entries and the numerator and denominator of \(r\) are explicitly given in binary with delimiters. Let \(L\) be the complete encoding length. Define
\[
\mathcal L(B)=\{Bz:z\in\mathbb Z^n\},\qquad
\lambda_1(\mathcal L(B))=\min_{z\in\mathbb Z^n\setminus\{0\}}\|Bz\|_2,
\quad \|v\|_2=\left(\sum_i v_i^2\right)^{1/2}.
\]
For a fixed \(\varepsilon\), the yes-instances have \(\lambda_1\le r\), the no-instances have \(\lambda_1>n^\varepsilon r\), and the inputs with \(r<\lambda_1\le n^\varepsilon r\) are outside the promise. The task is to output the correct yes/no bit; it does not ask for a lattice vector. The approximation factor is an exact mathematical threshold and depends on rank, not ambient dimension or coefficient bit length.

Membership in PromiseBPP means that there are one uniform classical probabilistic multitape Turing machine \(A\), with independent fair random bits, and constants \(K,a>0\), such that every run on a well-formed input halts within \(K(L+1)^a\) bit operations, every yes-instance is accepted with probability at least \(2/3\), and every no-instance is rejected with probability at least \(2/3\). Behavior inside the approximation gap is unrestricted. There are no quantum operations, advice or additional oracles. The machine and its constants may depend on the fixed \(\varepsilon\), but not on \(B,r\).

The class NP consists of finite-bit decision languages with polynomial-length witnesses checked by a uniform deterministic polynomial-time verifier. The class RP consists of languages with a uniform randomized polynomial-time decision algorithm that never accepts a no-instance and accepts each yes-instance with probability at least \(1/2\). The antecedent says that at least one NP language has no such RP algorithm. This is an ordinary decision-complexity hypothesis, not an assumption that a lattice problem is hard.

The conclusion requires one rational exponent for which no machine with the stated bounded-error guarantee exists. It does not merely rule out deterministic algorithms or one particular family of reduction algorithms. Restricting the existential exponent to rational values below \(1/2\) does not remove a possible positive-power hardness result: a solver for a smaller gap would also solve the promise problem for any larger gap. No common algorithm is required across different exponents if the conclusion fails.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the displayed implication, with an explicit rational exponent or a rigorous existence proof and all claimed algorithmic guarantees, or prove its logical negation. A refutation must establish NP ⊄ RP together with PromiseBPP membership for every rational exponent in (0,1/2). Hardness only in a norm p > 2, only for constant factors or for subpolynomial factors, or only under a stronger subexponential-time hypothesis does not settle this target.',
 why='Constant-factor Euclidean lattice hardness does not explain whether even a small fixed power of the rank remains difficult to approximate. Establishing this from the standard randomized NP-hardness assumption would close a major qualitative gap in the approximation landscape.',
 source_formulation=dict(text='Open Problem 2.3 asks for hardness at a fixed polynomial approximation factor under a standard assumption, in a discussion allowing different norms. This card selects the Euclidean case and the precise antecedent NP ⊄ RP. The August 2026 polynomial-factor theorem for p > 2 is recorded separately.',caption='The Complexity of the Shortest Vector Problem, §2.2 and Open Problem 2.3, printed p.5 / PDF p.7.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','§2.2 Theorem 2.2 and Open Problem 2.3, printed p.5 / PDF p.7'),
 ref('finite','Deterministic Hardness of Approximation For SVP in all Finite ℓ_p Norms','Isaac M Hair; Amit Sahai',2026,'https://arxiv.org/abs/2604.01451v2','6 April 2026 revision; Theorem 1.2 and formal Theorem 3.1, with a deterministic subexponential reduction and a subexponential-time assumption'),
 ref('constant','Euclidean SVP is deterministically NP-hard to approximate within any constant factor','Daqing Wan',2026,'https://arxiv.org/abs/2608.12664v2','8 September 2026 revision; Theorem 1.2 and Changes from the first version, p.2; retains fixed-factor results and withdraws dimension-dependent claims of the first version'),
 ref('polynomial','Polynomial-Factor Deterministic NP-Hardness for SVP in Every ℓ_p Norm with p > 2','Isaac M Hair; Amit Sahai',2026,'https://arxiv.org/abs/2608.14529v3','19 August 2026 revision; Theorem 1.1 p.2; technical overview paragraph Why the Argument Requires p > 2'),
 ],
 context_blocks=[
 block('The survey separates constant-factor hardness under NP ⊄ RP from stronger, still subpolynomial factors obtained under stronger running-time assumptions. The selected target asks for a fixed rank exponent under the former assumption.'),
 block('The April 2026 result covers the Euclidean norm through a deterministic subexponential-time reduction. Its stated hardness assumption and approximation regime do not establish this polynomial-factor, standard-assumption implication.','finite'),
 block('Wan’s September revision states deterministic hardness for every fixed constant approximation factor. It explicitly removes the first version’s dimension-dependent claims, so those older claims are not used to close this card.','constant'),
 block('The August 2026 theorem establishes fixed polynomial factors for every p > 2. Its allowed exponent is smaller than min{(p−2)/(4p),1/8}; the bound does not yield a positive exponent at p=2. The paper also explains directly why its Euclidean norm estimate fails to produce the required gap.','polynomial'),
 block('Consequently the historical request interpreted as allowing any norm now has positive progress that answers that broad variant. This card deliberately retains the Euclidean specialization, rather than presenting the whole any-norm question as still open.','polynomial'),
 ],
 progress=[progress('2023','The source asks for a polynomial-factor hardness result under a standard assumption, beyond its listed subpolynomial bounds.'),progress('2026-04','Hair and Sahai give deterministic subexponential reductions in all finite norms under a stronger subexponential-time assumption.','finite'),progress('2026-08-19','The latest checked Hair–Sahai polynomial-factor revision covers p > 2 and explicitly explains the obstacle at p=2.','polynomial'),progress('2026-09-08','Wan’s revised Euclidean paper retains arbitrary constant-factor hardness and does not retain the first version’s dimension-dependent claims.','constant')],
),[
 'Selected the Euclidean norm and the implication from NP ⊄ RP, following an unanswered optional assumption question and an announced editorial default.',
 'After discovering the August 2026 p>2 result, asked separately whether to archive the broader any-norm target; retained the recommended Euclidean specialization after no reply and explicitly announced that choice.',
 'Defined rank-sensitive binary-input Euclidean GapSVP and uniform bounded-error polynomial bit time on every promised instance.',
 'Checked the August polynomial-factor theorem and its explicit p=2 obstruction, and the September withdrawal of older dimension-dependent claims.',
 'Preserved the individual importance assessment and required a full Lean-checked implication or logical negation.',
],[
 'Read Bennett’s Theorem 2.2 and Open Problem 2.3 in their any-norm context.',
 'Read Hair–Sahai April 2026 Theorem 1.2 and formal Theorem 3.1, including the reduction running time and the stronger assumption.',
 'Read Wan’s 8 September 2026 revision Theorem 1.2 and its explicit Changes from the first version paragraph; no withdrawn dimension-dependent result is used.',
 'Downloaded and read Hair–Sahai 19 August 2026 version 3: abstract, Theorem 1.1 and the technical overview’s Why the Argument Requires p > 2 paragraph. Checked the current version and bounded later work through 17 September 2026.',
], 'The selected Euclidean implication remains unresolved in the checked primary sources through 17 September 2026. The August 2026 theorem resolves a broader any-norm interpretation for p > 2 but excludes p=2, and Wan’s September revision retains only fixed-factor claims. The norm and hypothesis were explicit announced editorial choices after unanswered optional questions; this card does not claim the entire original any-norm direction remains open.',summary=[
 'Euclidean GapSVP distinguishes lattices with a short nonzero vector from lattices whose shortest vector is longer by a promised approximation factor.',
 'The question asks whether NP ⊄ RP rules out a randomized polynomial-time algorithm for some fixed factor n^ε.',
 'The exponent is positive and independent of the input, and running time counts the complete binary representation.',
 'A 2026 theorem proves polynomial-factor hardness for p > 2, but it does not cover this Euclidean target.',
 'The card retains that precise open specialization and requires a complete Lean-checked implication or refutation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
