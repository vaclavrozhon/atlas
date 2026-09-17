"""Complete ordinary-LWE-only, depth-independent classical FHE."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6551';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the existing ordinary polynomial-modulus decisional-LWE convention and classical nonuniform security target.',
 'Specified one fixed key-generation algorithm with no evaluation-depth bound, bit-message chosen-plaintext indistinguishability including the evaluation key, and compactness independent of later circuits.',
 'Made correctness uniform over all polynomial circuit-size bounds, with a separate negligible error bound for each fixed polynomial, while the scheme and compactness polynomial remain fixed.',
 'Distinguished fresh-input FHE correctness from the stronger full-composability question, without silently adding that separate target.',
 'Checked the polynomial-modulus classical bootstrapping theorem, the additional assumptions of functional-encryption bootstrapping, and the explicit level parameters of two 2026 proposals.',
 'Added a June 2026 primary remark explicitly identifying unleveled FHE from plain LWE as unknown; preserved importance score 95.',
 'Required a complete Lean-checked construction from the exact assumption or refutation of the full implication; a restricted black-box separation or attack on one scheme is insufficient.',
]
sources=[
 'Read Brakerski–Vaikuntanathan, SIAM Journal on Computing 43(2), 831–871 (2014), DOI 10.1137/120868669, publisher abstract: ordinary LWE gives leveled FHE; removing the depth restriction adds weak circular security.',
 'Read Brakerski, Quantum FHE (Almost) As Secure As Classical, CRYPTO 2018, §3.3 Theorem 3.6 printed p. 16 (PDF p. 16): the underlying classical bootstrappable scheme allows polynomial modulus q above a fixed polynomial q0 and error D_{Z,2sqrt(n)}. Definitions 3.3 and Theorem 3.4 separate weak circular security and leveled bootstrapping. The PDF was readable through the web tool, though direct local download returned HTTP 403.',
 'Read Micciancio, Fully Homomorphic Encryption: definitional issues and open problems, May 2022 slides: PDF p. 10 asks the standard-LWE circular-security question; composition slides culminate in the separate FHE-to-CFHE question on PDF p. 24. The course-directory year 2023 is not the slide date.',
 'Reused and read the cached published Bitansky–Solomon ITCS 2023 Article 17, §1.1 Theorem 1 and nonuniform-adversary discussion pp. 17:1–17:2, syntax §1.2 p. 17:3. The functional-encryption instantiation uses assumptions beyond LWE; nonuniform security requires a further complexity assumption.',
 'Read Wang–Huang–Tang, Cybersecurity 9, Article 31, 18 February 2026, publisher HTML Definitions 2.2–2.4: Setup takes the maximum depth L, and compactness permits dependence on L. Read the cached Liu et al. arXiv:2604.23490v1 key generation and §3.4: L+1 key layers and a quantum evaluator. Neither matches the target.',
 'Read Hsieh–Jain–Li–Mathialagan, ECCC TR26-098, public 14 June 2026, Remark 11.20 printed p. 97: it explicitly says that unleveled FHE is not known from plain LWE. The report was received 11 June; source metadata distinguishes receipt and publication.',
 f'Bounded primary-source checks through {DATE} found no verified resolution. The separate September 2026 attack on a proposed CRT scheme was checked for TCS-6871 and is not a general impossibility result.',
]
complete(identifier,dict(
 criterion='assumptions',question_type='yes_no',
 formal=r'''Does the ordinary polynomial-modulus decisional Learning With Errors assumption specified below imply the existence of a classical compact fully homomorphic public-key encryption scheme whose keys are generated without a bound on the size or depth of the circuits subsequently evaluated?

The scheme must be secure against nonuniform polynomial-size classical adversaries given both its encryption and evaluation keys. Its only hardness assumption may be the stated ordinary LWE assumption; no independent circular-security or key-dependent-message assumption is allowed.''',
 definitions=r'''Fix the following precise LWE hypothesis. For every integer \(c\ge3\), let \(q_c(d)\) be the least prime at least \(d^c\). For every positive integer-valued polynomially bounded sample-count function \(M(d)\), sample independently
\[
 A\leftarrow\mathbb Z_{q_c(d)}^{M(d)\times d},\qquad
 s\leftarrow\mathbb Z_{q_c(d)}^d,\qquad
 u\leftarrow\mathbb Z_{q_c(d)}^{M(d)}
\]
uniformly, and let the coordinates of \(e\) be independent integers with probability proportional to \(\exp(-\pi z^2/(4d))\), reduced modulo \(q_c(d)\). Here \(\mathbb Z_q\) is the ring of integers modulo \(q\). The hypothesis is that the distributions
\[
 (A,As+e\bmod q_c(d))\quad\text{and}\quad(A,u)
\]
are computationally indistinguishable against every family of nonuniform classical randomized circuits of size polynomial in \(d\). That is, the absolute difference of their acceptance probabilities is negligible in \(d\). The integer \(c\) and the polynomial sample bound are fixed before \(d\) grows. A distinguisher may know them and \(d\). The noise is the discrete Gaussian \(D_{\mathbb Z,2\sqrt d}\); no encryptions of secrets, correlated auxiliary hints or circular-security statements are included in this assumption.

A nonnegative function \(\mu(t)\) is negligible if for every integer \(a\ge1\), there is \(t_a\) such that \(\mu(t)\le t^{-a}\) for every \(t\ge t_a\). Circuit size counts gates, input bits and private random bits, using fan-in-two Boolean gates and unary negation. Nonuniform means that each circuit may be chosen independently at each parameter value, with no efficient procedure producing the family. These are classical adversaries, not quantum ones.

The requested scheme has one fixed tuple of uniform classical algorithms
\[
 \operatorname{Gen}(1^\lambda)\to(pk,evk,sk),\quad
 \operatorname{Enc}(pk,b)\to c,\quad
 \operatorname{Eval}(evk,F,c_1,\ldots,c_t)\to c_F,\quad
 \operatorname{Dec}(sk,c)\to b.
\]
All algorithms may also receive \(1^\lambda\) implicitly. Generation, encryption and evaluation may use fresh independent fair random bits; decryption is deterministic. Generation and bit encryption have polynomial worst-case bit running time in \(\lambda\). Evaluation runs in time polynomial in \(\lambda\) and its complete input length. The model is an ordinary multitape Turing machine; no ideal cryptographic oracle is available.

Plaintexts are bits. The circuit \(F\) is explicitly given by its gate list, has \(t\) inputs and one output, and uses fan-in-two AND and OR and unary NOT. The generation algorithm receives no circuit, circuit-size bound or depth bound. There is one fixed polynomial \(P\) bounding the lengths of \(pk,evk,sk\), fresh bit ciphertexts and evaluated one-bit ciphertexts, as well as the time for decrypting these ciphertexts, by \(P(\lambda)\). This bound is independent of \(F\), its input count and its depth. All auxiliary public material is included in \(pk,evk\).

For every fixed polynomial \(p\), there must be a negligible function \(\mu_p(\lambda)\) such that, for every circuit \(F\) with size and input count at most \(p(\lambda)\) and every vector of input bits, independently encrypting those bits, evaluating \(F\), and decrypting yields \(F(b_1,\ldots,b_t)\) with probability at least \(1-\mu_p(\lambda)\). The probability includes all coins of generation, encryption and evaluation. Fresh bit decryption has negligible error as well. The algorithms and \(P\) are fixed before choosing \(p\). Thus one key-generation algorithm supports every polynomial circuit bound; choosing a large fixed polynomial depth during setup does not meet the quantifiers.

Security means that for every nonuniform polynomial-size classical circuit family \(T_\lambda\),
\[
 \left|\Pr[T_\lambda(pk,evk,\operatorname{Enc}(pk,0))=1]
       -\Pr[T_\lambda(pk,evk,\operatorname{Enc}(pk,1))=1]\right|
\]
is negligible in \(\lambda\). Each experiment generates a fresh key tuple and fresh encryption and adversary randomness. Since the public key allows arbitrary further encryptions, this is bit-message chosen-plaintext indistinguishability. The requested theorem must derive this security from the precise LWE hypothesis above. It is not a request to prove LWE hardness unconditionally.

There is no external trusted setup, subsequent secret-key assistance, random oracle or additional hardness premise. Bootstrapping and public encryptions involving secret-key bits are permitted if their security is proved from ordinary LWE. In particular, the absence of a circular-security assumption is a requirement on the proof, not a ban on a syntactic form of evaluation key. Polynomial hardness of LWE is the assumption: subexponential hardness, functional encryption and obfuscation may not simply be assumed independently.

The correctness condition is evaluation of one arbitrary polynomial-size circuit on fresh ciphertexts. A stronger guarantee for indefinitely composing new evaluations on already evaluated ciphertexts is not an extra requirement here. The related TCS-6871 instead asks for an operational reduction from worst-case polynomial-factor GapSVP, allowing quantum computation in that reduction; it has a different stated foundation.''',
 answer_criterion=r'''Give a complete Lean-checked construction of one scheme, its uniform running-time and compactness bounds, the correctness guarantee for every polynomial circuit-size bound, and a proof of its security from exactly the specified LWE hypothesis; or give a complete Lean-checked refutation of that implication.

An additional circular-security, functional-encryption, obfuscation or stronger-hardness assumption does not meet the positive target. A construction with depth-dependent setup, a quantum evaluator or noncompact decryption also does not qualify. Breaking one proposed scheme, or separating one restricted class of black-box reductions, does not refute the general existence implication. All assumptions of a conditional obstruction must remain explicit. Numerical approximation tolerance does not weaken these asymptotic security, correctness and resource requirements.''',
 source_formulation=dict(text='The source distinguishes known leveled LWE constructions from fully homomorphic encryption with depth-independent keys and asks for the latter from comparable standard lattice assumptions. This card preserves its existing ordinary polynomial-modulus LWE specialization, classical nonuniform security, and fresh-input correctness convention.',caption='Paraphrase of Bitansky–Solomon, ITCS 2023 §1.1–1.2 pp. 17:2–17:3, alongside Micciancio’s May 2022 standard-LWE and composition questions. The specific prime-modulus and discrete-Gaussian convention is retained from the existing card.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Bootstrapping Homomorphic Encryption via Functional Encryption','Nir Bitansky; Tomer Solomon',2023,'https://doi.org/10.4230/LIPIcs.ITCS.2023.17','ITCS 2023 Article 17; §1.1 Theorem 1 and nonuniform-adversary qualification pp. 17:1–17:2; FHE syntax §1.2 p. 17:3'),
 ref('lwe','Efficient Fully Homomorphic Encryption from (Standard) LWE','Zvika Brakerski; Vinod Vaikuntanathan',2014,'https://doi.org/10.1137/120868669','SIAM Journal on Computing 43(2), pp. 831–871; publisher abstract separates leveled LWE security from removing levels using weak circular security'),
 ref('polymodulus','Quantum FHE (Almost) As Secure As Classical','Zvika Brakerski',2018,'https://www.iacr.org/archive/crypto2018/10993383/10993383.pdf','CRYPTO 2018; Definition 3.3 and Theorem 3.4 p. 15; §3.3 Theorem 3.6 p. 16, underlying classical polynomial-modulus scheme and discrete-Gaussian error'),
 ref('ref2','Fully Homomorphic Encryption: definitional issues and open problems','Daniele Micciancio',2022,'https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf','Slides dated May 2022; PDF p. 10, standard-LWE circular-security question; PDF p. 24, separate FHE-to-CFHE question'),
 ref('multikey','Dynamic multi-key FHE without CRS from LWE','Junjie Wang; Ruwei Huang; Xiaolong Tang',2026,'https://doi.org/10.1186/s42400-025-00431-z','Cybersecurity 9, Article 31, 18 February 2026; Definitions 2.2–2.4, Setup and compactness depend on maximum depth L'),
 ref('quantum','Efficient Quantum Fully Homomorphic Encryption','Fengxia Liu; Zixian Gong; Kun Tian; Yi Zhang; Zhiming Zheng; Maozhi Xu',2026,'https://arxiv.org/abs/2604.23490v1','Version 1, 26 April 2026; Key Generation takes 1^L and §3.4 uses L+1 independent key layers; evaluator is quantum'),
 ref('plain','SNARGs for NP from Unprovability of Mathematical Theorems','YaoChing Hsieh; Abhishek Jain; Jiatu Li; Surya Mathialagan',2026,'https://eccc.weizmann.ac.il/report/2026/098/','ECCC TR26-098, received 11 June and published 14 June 2026; Remark 11.20 printed p. 97 explicitly identifies unleveled FHE from plain LWE as unknown'),
 ],
 context_blocks=[
 block('Compactness requires the returned ciphertext and its decryption cost to stay independent of the evaluated circuit. Supporting any chosen polynomial depth after fixing that depth during setup gives a leveled scheme, which has different quantifiers from this target.','lwe'),
 block('The functional-encryption construction removes the circular-security assumption but uses additional primitives. Its nonuniform-security extension also has a further complexity assumption, so it does not establish the sole-LWE proposition.'),
 block('The February 2026 dynamic multi-key construction explicitly gives its setup the maximum depth. Removing a common reference string or permitting more keys does not remove that level parameter.','multikey'),
 block('The April 2026 quantum proposal uses a quantum evaluator and a preselected number of independent key layers. Those features place it outside this classical, depth-independent target.','quantum'),
 block('A June 2026 primary paper explicitly declines an optimization because it would need unleveled FHE, which its authors state is not known from plain LWE. This supports the recorded open status without certifying every possible later claim.','plain'),
 block('Fresh-input FHE correctness and full composability are separate definitional questions. The present card requires the former; the latter is not silently added as a stronger acceptance condition.','ref2'),
 ],
 progress=[progress('2014','The journal construction separates leveled LWE security from the additional assumption used to remove levels.','lwe'),progress('2018','The classical bootstrappable construction is recorded with polynomial modulus and the stated discrete-Gaussian noise.','polymodulus'),progress('2023','Functional-encryption bootstrapping gives unbounded FHE under additional assumptions.'),progress('2026-02-18','A dynamic multi-key paper still takes a maximum depth in setup.','multikey'),progress('2026-06-14','A primary SNARG paper explicitly records unleveled FHE from plain LWE as unknown.','plain')],
),notes,sources,'The June 2026 primary remark explicitly records unleveled FHE from plain LWE as unknown. Checked functional-encryption constructions use additional assumptions; the examined 2026 dynamic multi-key and quantum proposals retain a depth bound. Bounded primary-source checks through 17 September 2026 found no verified resolution of the retained ordinary-LWE-only target. The full security proofs of the cited proposals were not independently certified.',summary=[
 'Fully homomorphic encryption evaluates Boolean computations on encrypted bits and returns a compact encrypted result.',
 'The question asks for one classical key-generation procedure that needs no advance bound on the depth of those computations.',
 'The only hardness premise is the specified ordinary polynomial-modulus LWE assumption, without independent circular security.',
 'Security must hold against polynomial-size nonuniform classical adversaries who also see the evaluation key.',
 'A complete Lean-checked answer must establish the entire implication and its uniform correctness and compactness guarantees, or refute it.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
