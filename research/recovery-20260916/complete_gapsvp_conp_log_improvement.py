"""Select the source's explicit logarithmic improvement for coNP certificates."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0657';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='coNP certificates for GapSVP at the square-root n/log n scale',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Is there an absolute constant \(C\ge2\) such that Euclidean \(\operatorname{GapSVP}_{\gamma_C(n)}\) belongs to coNP, where
\[
\gamma_C(n)=C\sqrt{\frac{n}{\log_2(n+2)}}\ ?
\]
Concretely, must every input lattice whose shortest nonzero vector has length greater than \(\gamma_C(n)r\) admit a polynomial-length, deterministically polynomial-time verifiable certificate, with no accepted certificate when the lattice has a nonzero vector of length at most \(r\)?''',
 definitions=r'''The input consists of an integer matrix \(B\in\mathbb Z^{m\times n}\), with \(m\ge n\ge1\) and linearly independent columns, and a positive rational radius \(r\). Dimensions, signed matrix entries and the numerator and positive denominator of \(r\) are written in binary using an explicit length-delimited encoding. Let \(L\) be its full bit length. The rank \(n\), ambient dimension \(m\), and all coefficient lengths are part of the input.

Define
\[
\mathcal L(B)=\{Bz:z\in\mathbb Z^n\},\qquad
\lambda_1(\mathcal L(B))=\min_{z\in\mathbb Z^n\setminus\{0\}}\|Bz\|_2,
\quad \|v\|_2=\left(\sum_i v_i^2\right)^{1/2}.
\]
The GapSVP promise distinguishes yes-instances with \(\lambda_1\le r\) from no-instances with \(\lambda_1>\gamma_C(n)r\). Inputs between those thresholds are outside the promise. The constant restriction \(C\ge2\) ensures \(\gamma_C(n)\ge1\) at every positive rank; changing finitely many small ranks does not affect the intended asymptotic scale. The logarithm is to base two, and the approximation factor depends on lattice rank, not total bit length.

Membership in coNP for this promise problem means that there are one deterministic multitape Turing machine \(V\), constants \(K>0\) and integers \(a,b\ge1\), with the following properties on every well-formed input. A certificate is a finite binary string \(w\) with \(|w|\le K(L+1)^a\), and verification takes at most \(K(L+1)^b\) bit operations for each such certificate. The same verifier and constants must satisfy
\[
\lambda_1>\gamma_C(n)r\quad\Longrightarrow\quad
\exists w:\ |w|\le K(L+1)^a\ \land\ V(B,r,w)=1,
\]
\[
\lambda_1\le r\quad\Longrightarrow\quad
\forall w:\ |w|\le K(L+1)^a\ \Longrightarrow\ V(B,r,w)=0.
\]
Longer strings can be rejected. Verification behavior is unconstrained inside the gap. There is no required efficient algorithm for finding certificates, but verification is uniform, classical and deterministic. Certificates contain only finitely many bits; exact real numbers, randomness, quantum states, interaction with a prover and auxiliary oracles are not supplied. Both the choice of \(C\) and all resource bounds are fixed independently of each input.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof that such a constant and verifier exist, including certificate length, deterministic bit complexity, completeness and soundness on the promise, or a proof of the negation of this existence claim. A randomized interactive coAM protocol, a polynomial-time verifier only at factor C√n, or a smaller-factor protocol with superpolynomial running time does not establish this target.',
 why='A short certificate that no sufficiently short lattice vector exists would strengthen the known upper bounds on lattice complexity. Matching the better approximation scale of interactive proofs with a single classical certificate would clarify the role of interaction in certifying lattice distance.',
 source_formulation=dict(text='Open Problem 4.2 offers improvements to coNP or coAM. Its following paragraph specifically asks whether the coNP approximation scale can reach O(√(n/log n)); this card selects that concrete target.',caption='The Complexity of the Shortest Vector Problem, Open Problem 4.2 and the immediately following paragraph, printed p.13 / PDF p.15.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','§4.1, Open Problem 4.2 and following specific coNP target, printed p.13 / PDF p.15; subsequent distinction between polynomial and superpolynomial protocols'),
 ref('certificates','Lattice Problems in NP ∩ coNP','Dorit Aharonov; Oded Regev',2005,'https://cims.nyu.edu/~regev/papers/cvpconp.pdf','8 September 2005 author version; Theorem 1.1 and Corollary 1.2 p.2, Speculation 1.5 p.5, Appendix A approximation-preserving reduction; JACM 52(5), 749–765'),
 ],
 context_blocks=[
 block('Aharonov and Regev prove coNP membership at approximation factor C√n. Their argument provides succinct classical evidence that no sufficiently short vector exists; merely exhibiting a short vector certifies the opposite side.','certificates'),
 block('The better scale √(n/log n) is known for a randomized interactive coAM protocol. The selected question asks whether deterministic checking of one polynomial-length certificate can reach the same scale.'),
 block('The 2005 paper already discusses the corresponding refinement for the closest-vector problem as Speculation 1.5. Its approximation-preserving reduction would also transfer that stronger result to shortest-vector certification.','certificates'),
 block('The source’s broader question also permits unspecified smaller improvements or a stronger coAM protocol. This card selects the explicit coNP target stated directly after Open Problem 4.2.'),
 block('Protocols with larger running time or proof length can trade resources for approximation quality. Such a tradeoff does not imply membership in coNP, which requires both resources to be polynomial in the encoded input length.'),
 ],
 progress=[progress('2005','Aharonov and Regev establish the C√n certificate bound and discuss a possible logarithmic refinement for closest-vector certification.','certificates'),progress('2023','The survey retains the coNP improvement as open and singles out the √(n/log n) target.')],
),[
 'Selected the source’s explicit coNP target at C√(n/log n), following an unanswered optional choice and an announced editorial default.',
 'Defined rank-based Euclidean GapSVP, the complete binary encoding, exact promise boundaries and the harmless n+2 logarithm convention.',
 'Specified one deterministic certificate verifier with polynomial certificate size and bit time and no required efficient certificate generation.',
 'Separated classical coNP certificates, randomized coAM interaction and superpolynomial-time protocols.',
 'Preserved the importance assessment and required a complete Lean-checked verifier or impossibility proof.',
],[
 'Read the full Open Problem 4.2 and its concrete coNP refinement paragraph in Bennett’s January 2023 survey, with adjacent protocol-time discussion.',
 'Read the September 2005 Aharonov–Regev author version’s Theorem 1.1, Corollary 1.2 and Speculation 1.5; its exact lower certificate bound is C√n.',
 'Bounded primary-source checks through 17 September 2026 did not locate a polynomial-length deterministic certificate result at the selected improved scale.',
], 'Source-open in Bennett’s Open Problem 4.2 and its explicit following coNP target. The selected refinement was announced as an editorial default after an unanswered optional question. Existing coAM protocols and superpolynomial-time tradeoffs do not provide the required deterministic polynomial verifier. Bounded later-work checks through 17 September 2026 found no matching resolution.',summary=[
 'GapSVP asks whether an input lattice has a vector of length at most a threshold or all nonzero vectors are longer by a promised factor.',
 'This card asks for short classical certificates of the second alternative at factor C√(n/log n).',
 'One deterministic verifier must check the certificates in polynomial time in the complete binary input length.',
 'Known certificates work at the larger scale C√n, while the smaller scale is known for an interactive randomized proof.',
 'The requested improvement and all promise guarantees require a complete Lean-checked proof or refutation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
