"""Archive the user-selected low-entropy extractor branch under its exact known assumption."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1024';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Low-entropy extraction from samplable sources under Σ₅-oracle circuit hardness',
 status='resolved',criterion='construction',question_type='yes_no',
 formal=r'''Does the hardness assumption \(H_5\) defined below imply the following low-entropy extraction statement?

There is a rational constant \(\gamma\in(0,1)\) such that, for every integer \(c\ge2\), there exist integers \(b,n_0\ge1\), a constant \(K\ge1\), and one deterministic algorithm \(E_c\) which, for all \(n\ge n_0\) and integers \(\lceil n^{1-\gamma}\rceil\le k\le n\), computes a function
\[
\operatorname{Ext}_{n,k}:\{0,1\}^n\to\{0,1\}^{\lfloor k/2\rfloor}
\]
in at most \(Kn^b\) bit operations and satisfies
\[
\Delta\!\left(\operatorname{Ext}_{n,k}(S(U_r)),U_{\lfloor k/2\rfloor}\right)\le n^{-c}
\]
for every size-at-most-\(n^c\) sampling circuit \(S:\{0,1\}^r\to\{0,1\}^n\) whose output distribution has min-entropy at least \(k\)? This conditional statement has a positive resolution in the cited STOC 2025 work.''',
 definitions=r'''For an integer \(r\ge0\), \(U_r\) denotes the uniform distribution on \(\{0,1\}^r\); \(U_0\) is the point mass on the empty string. A sampling circuit is a finite directed acyclic Boolean circuit with input nodes, constant bits, fan-in-two AND and OR gates, fan-in-one NOT gates, and \(n\) ordered output wires. Its size is the number of nodes plus the number of wires, including input nodes and output wires. It may be nonuniform and depend on \(n\). The randomness in \(S(U_r)\) consists only of the independent fair input bits. There is no postselection or oracle in the sampler. Its input length is bounded by its size.

For a finite distribution \(Z\), define its min-entropy in bits by
\[
H_\infty(Z)=-\log_2\max_z\Pr[Z=z].
\]
For distributions \(P,Q\) on the same finite set, their statistical distance is
\[
\Delta(P,Q)=\tfrac12\sum_z|P(z)-Q(z)|.
\]
The guarantee must hold simultaneously for every admissible sampling circuit. The extractor receives only \((n,k,z)\), with \(n,k\) in binary and \(z\in\{0,1\}^n\) explicitly supplied. It receives neither the sampler description nor another sample, random seed or oracle. For each fixed \(c\), one uniform deterministic multitape Turing machine computes all the functions \(\operatorname{Ext}_{n,k}\). Its exponent and constants may depend on \(c\) and the fixed hardness witness, and may exceed the sampler's exponent. The bound applies to every supplied string \(z\), not just typical samples. The same \(\gamma\) works for every \(c\). Because \(n^{1-\gamma}<n/2\) for all sufficiently large \(n\), this crosses the historical entropy threshold.

To define \(H_5\), fix a canonical binary encoding of Boolean circuits and five blocks of quantified Boolean variables. Let \(Q_5\) be the language of valid encodings of true sentences
\[
\exists u_1\ \forall u_2\ \exists u_3\ \forall u_4\ \exists u_5:
C(u_1,u_2,u_3,u_4,u_5)=1,
\]
where the variable blocks are explicitly specified and \(C\) is an explicitly given Boolean circuit. Malformed encodings are rejected. Use a topologically ordered gate list with binary predecessor indices and unary block lengths; this fixes a standard complete language for the fifth existential level \(\Sigma_5^{\mathrm P}\) of the polynomial hierarchy. Each block ranges over all bit strings of its specified length.

A \(Q_5\)-oracle circuit has the ordinary Boolean gates above and arbitrary-fan-in gates that output whether the bit string on their ordered incoming wires is in \(Q_5\). Its size counts every gate, input node and wire, including all wires into oracle gates. The oracle circuits are nonuniform, their depth is unrestricted, and each must compute one Boolean output on every input of its length. The assumption \(H_5\) says there exist constants \(0<\beta<B\), a language \(L\subseteq\{0,1\}^*\) decided by a deterministic Turing machine in time \(O(2^{B\ell})\) on length-\(\ell\) inputs, and an integer \(\ell_0\), such that for every \(\ell\ge\ell_0\), no size-at-most-\(2^{\beta\ell}\) \(Q_5\)-oracle circuit computes the characteristic function of \(L\) correctly on all \(\ell\)-bit strings. Thus \(L\) belongs to \(\mathrm E=\mathrm{DTIME}(2^{O(\ell)})\), but is exponentially hard even for circuits with this powerful oracle. The oracle is part of the hardness assumption, not a computational resource available to the extractor.

The target is this implication from \(H_5\), not unconditional extraction, not an implication from ordinary P-versus-NP hardness, and not negligible error \(n^{-\omega(1)}\) for one fixed sampler-size exponent. Outputting half the promised entropy is a concrete specialization of the known theorem's arbitrary fixed fractional entropy loss.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the displayed implication from H_5 to the uniform extractor family. A positive proof must verify the statistical guarantee for every size-bounded sampler and the deterministic evaluation cost. An unconditional construction is sufficient but is not required. A proof under a stronger unrecorded hypothesis or with only large linear min-entropy does not establish this target. Archival does not claim that the result has already been formalized in Lean.',
 why='Efficiently samplable distributions model structured weak randomness without independent components. Crossing the half-entropy threshold shows that computational restrictions on the source can support deterministic extraction in a regime inaccessible to earlier techniques.',
 source_formulation=dict(text='Vadhan’s Open Problem 8.12 asks for extraction below the n/2 entropy threshold and/or with negligible error, under plausible assumptions. The user chose the low-entropy branch and archival of the known conditional result. The card fixes the published construction’s explicit Σ₅-oracle hardness assumption, polynomially small error and a half-entropy output specialization. It does not replace the unselected negligible-error branch by a claim of resolution.',caption='Vadhan, Pseudorandomness, §8.2.4 Open Problem 8.12, printed p.303 / PDF p.306.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf','§8.2.4, Open Problem 8.12, printed p.303 / PDF p.306'),
 ref('solution','Extractors for Samplable Distributions with Low Min-Entropy','Marshall Ball; Ronen Shaltiel; Jad Silbak',2025,'https://doi.org/10.1145/3717823.3718143','STOC 2025 pp.596–603; checked author full manuscript dated 16 December 2024, Theorem 1.4 p.2, Definitions 2.2–2.3 p.12 and 2.13–2.14 p.14'),
 ref('manuscript','Extractors for Samplable Distributions with Low Min-Entropy — full manuscript','Marshall Ball; Ronen Shaltiel; Jad Silbak',2024,'https://www.cs.haifa.ac.il/~ronen/online_papers/Extractor_for_Samplable_Distributions_with_Low_Min_Entropy.pdf','16 December 2024 version; Theorem 1.4 and §4.4.1 proof, pp.32–33'),
 ref('refinement','Extractors for Samplable Distribution with Polynomially Small Min-Entropy','Ronen Shaltiel',2025,'https://eccc.weizmann.ac.il/report/2025/054/','Report of 24 April 2025, Theorem 1.4 p.2; separately checked further entropy improvement'),
 ref('withdrawal','Near Optimal Extractors for Samplable Sources under Nondeterministic Hardness — retraction notice','Marshall Ball; Eshan Chattopadhyay; Mohit Gurumukhani; Yunya Zhao',2026,'https://eccc.weizmann.ac.il/report/2026/089/','Revision 1 of 4 June 2026: authors retract the paper because of a mistake in Lemma 5.9'),
 ],
 context_blocks=[
 block('The textbook treats sources produced by small sampling circuits. It explains that the extractor must be allowed greater computational complexity than the sampler, and asks to improve the entropy threshold or the error guarantee.'),
 block('The STOC 2025 theorem supplies a fixed positive entropy exponent improvement under exponential hardness for Σ₅-oracle circuits, with error n⁻ᶜ for samplers of size nᶜ. Choosing its output-loss parameter to be one half yields the formulation here.','solution'),
 block('The full manuscript defines the oracle-circuit hardness by counting both wires and gates and requiring hardness at every sufficiently large length. Its construction is deterministic once the fixed hard function is chosen; it is not given the sampling circuit at evaluation time.','manuscript'),
 block('Shaltiel’s April 2025 theorem further lowers the entropy threshold with a corresponding fixed polynomial-hierarchy oracle assumption. This improvement is separate from the earlier result already sufficient for this historical card.','refinement'),
 block('A May 2026 preprint claimed stronger extraction under nondeterministic hardness, but the authors withdrew it on 4 June 2026 after an error in Lemma 5.9. It is not used as evidence of resolution or as a weakening of the assumption in this card.','withdrawal'),
 ],
 progress=[progress('2012-12','The textbook records the low-entropy and negligible-error directions as separate alternatives.'),progress('2024-12','The full manuscript proves the low-entropy theorem subsequently published at STOC 2025.','manuscript'),progress('2025-06','STOC 2025 publishes the conditional construction crossing n/2 min-entropy.','solution'),progress('2026-06-04','The authors retract the separate near-optimal nondeterministic-hardness preprint; it is excluded from the resolution evidence.','withdrawal')],
),[
 'Applied the user-confirmed low-entropy branch and conditional archival rather than keeping an unspecified plausible assumption.',
 'Defined the exact fifth-level oracle language, circuit size and eventual exponential hardness in E.',
 'Specified uniform deterministic extraction, a separate sampler-size parameter, min-entropy, statistical distance and a concrete fractional output length.',
 'Read the known theorem with its inverse-polynomial error; did not claim the negligible-error alternative solved.',
 'Checked the 2026 retraction notice and excluded the withdrawn improvement from all resolution claims; retained assessed importance and required complete Lean checking.',
],[
 'Read Vadhan Open Problem 8.12 and its surrounding sampler-complexity discussion.',
 'Read the full December 2024 manuscript Theorem 1.4, sampling/extractor Definitions 2.2–2.3, circuit/hardness Definitions 2.13–2.14 and §4.4.1 parameter choices.',
 'Verified STOC 2025 publication metadata and DOI through the author institution’s publication record.',
 'Read the April 2025 refinement Theorem 1.4; checked the current ECCC 2026/089 record and its 4 June retraction notice rather than trusting the unrevised abstract.',
], 'Resolved as a conditional theorem by Ball–Shaltiel–Silbak, STOC 2025, under the explicitly stated H_5 assumption. The user selected this low-entropy branch and archival on 18 September 2026. The negligible-error alternative is not claimed resolved. The separate May 2026 near-optimal preprint was retracted on 4 June 2026 and is not used. The theorem statement and parameter specialization were checked, not the entire proof independently or a Lean formalization.',summary=[
 'The source asks whether deterministic extraction from efficiently samplable distributions can cross the half-entropy threshold.',
 'The user chose this historical low-entropy branch and its known conditional resolution.',
 'The fixed assumption requires an exponential-time language that remains exponentially hard for circuits with a fifth-level polynomial-hierarchy oracle.',
 'The STOC 2025 construction extracts a constant fraction of entropy with inverse-polynomial statistical error from sources below n/2 entropy.',
 'The card is archived under that precise assumption; the separate negligible-error direction and a retracted 2026 improvement are not claimed resolved.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='The user selected the historical low-entropy branch of Vadhan Open Problem 8.12 and archival. Ball–Shaltiel–Silbak, STOC 2025, gives the displayed deterministic construction below n/2 min-entropy under explicit exponential E hardness for Σ₅-oracle circuits. This archives a known conditional theorem, not an unconditional construction or the separate negligible-error target; the withdrawn May 2026 paper is not used.')
