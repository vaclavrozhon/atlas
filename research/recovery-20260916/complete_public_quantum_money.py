"""Complete the static reusable public-key quantum-money implication."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7359';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the fixed polynomial LWE modulus and error distribution, quantum nonuniform security with classical advice, and unrestricted existence implication.',
 'Expanded the uniform quantum circuit model, finite-register encoding, negligible bounds and independent sampling conventions.',
 'Specified a static classical public key, no online bank interaction, and repeated verification of the returned residual state for every polynomial number of transfers.',
 'Retained the k-to-k+1 game including k=0, arbitrary serial strings and entanglement across output registers; one scheme must handle every polynomial attack bound.',
 'Read the anonymous-money definitions and counterfeiting game, the restricted evasive-obfuscation barrier, and the generic-group and time-dependent alternatives.',
 'Preserved importance 93 and category; excluded extra anonymity, tracing, quantum-lightning and expiring-token requirements from the target.',
]
sources=[
 'Read Cakan–Goyal–Yamakawa, arXiv:2411.04482v1, 7 November 2024: abstract, introduction, Section 6 Definitions 10–12 pp. 23–24, Section 7 assumptions and Appendix A Definition 19 counterfeiting game. Its money construction adds obfuscation and further quantitative assumptions; the LWE-only rerandomizable encryption primitive is not itself public-key money.',
 'Read the primary ePrint 2025/325 abstract and Zhandry author-publication entry for EUROCRYPT 2025. The barrier restricts the mint to classical obfuscation queries and the verifier to evaluation queries without obfuscation queries. The ePrint PDF download returned HTTP 403, so no full-proof read is claimed.',
 'Read Bostanci–Nehoran–Zhandry, STOC 2025, primary author-publication abstract: the group-action construction reduces to pre-action security, and the one-way-homomorphism alternative has additional conditions. This is not a reduction from the fixed decisional LWE premise.',
 'Read Doliskani, Public-Key Quantum Money From Standard Assumptions (In The Generic Model), current author-hosted PDF, abstract, introduction pp. 1–3, Section 2.2 and Section 3. Its reduction to group-action discrete logarithm retains the generic group-action oracle. The public minting mini-scheme is also a distinct interface from the bank-key game here. The full security proof was not independently audited.',
 'Read Doliskani–Mirzaei–Mousavi, Public-Key Quantum Money and Fast Real Transforms, current author-hosted PDF, abstract and introduction. It modifies the group-action construction using Hartley transforms; the abstract does not assert the required LWE-only implication.',
 'Read Barhoush–Salvail, How to Sign Quantum Messages, Quantum 10, 1980, 22 January 2026, primary journal abstract and arXiv:2304.06325v5 Section 7 pp. 32–35, Definitions 24–26 and Construction 5/Theorem 8. The pq-OWF route uses time-dependent verification-key announcements and banknotes with a prescribed lifespan, requiring replacement by the bank. This does not provide the static indefinitely polynomially reusable interface selected here. Full proof not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the precise ordinary-model LWE implication. Generic-model, stronger-assumption and time-dependent schemes were not promoted to a resolution.',
]
complete(identifier,dict(
 title='Public-key quantum money from LWE alone',criterion='assumptions',question_type='yes_no',
 formal=r'''Does quantum hardness of the fixed decisional Learning with Errors distributions below imply the existence of a reusable, unforgeable public-key quantum money scheme in the plain computational model? The scheme must have a static classical public key, polynomial-time quantum minting and verification, and security against every nonuniform polynomial-size quantum adversary with classical advice.''',
 definitions=r'''The security parameter is an integer \(\lambda\ge2\), supplied in unary. Let \(q_\lambda\) be the least prime at least \(\lambda^4\), let \(\mathbb Z_{q_\lambda}\) denote integers modulo this prime, and define an integer error distribution by
\[
 \chi_\lambda(z)=\frac{\exp(-\pi z^2/\lambda^2)}{\sum_{a\in\mathbb Z}\exp(-\pi a^2/\lambda^2)},\qquad z\in\mathbb Z.
\]
For every polynomially bounded function \(m:\mathbb N\to\mathbb N\), sample independently a uniform matrix \(A\in\mathbb Z_{q_\lambda}^{m(\lambda)\times\lambda}\), a uniform vector \(s\in\mathbb Z_{q_\lambda}^{\lambda}\), errors \(e_i\) independently from \(\chi_\lambda\), and a uniform vector \(u\in\mathbb Z_{q_\lambda}^{m(\lambda)}\). All field elements have their ordinary binary encodings. The LWE premise says that the two classical ensembles
\[
 (1^\lambda,A,As+e\bmod q_\lambda)
 \quad\text{and}\quad
 (1^\lambda,A,u)
\]
are computationally indistinguishable against the quantum adversaries defined below. That is, every such distinguishing circuit has negligible absolute difference between its two acceptance probabilities, for every such sample-count function. The discrete Gaussian specifies a probability law, rather than granting an exact sampling oracle to any algorithm.

A nonnegative function \(\mu(\lambda)\) is negligible if for every integer \(a\ge1\) it is at most \(\lambda^{-a}\) for all sufficiently large \(\lambda\). The threshold may depend on \(a\). A different negligible function may be used for each fixed adversary, sample-count function or repetition bound.

Quantum computations use qubits, the fixed Clifford-plus-T gate set, zero-state ancillas and computational-basis measurements, with polynomial-time classical control. A quantum state is a positive semidefinite trace-one operator on the finite qubit register concerned; mixed states are allowed. A uniform polynomial-time algorithm has one finite classical program generating and controlling these operations, with a fixed polynomial bound on the number of gates, qubits and classical bit operations on every measurement branch. Classical random bits may be generated by fair quantum measurements. A nonuniform polynomial-size adversary is a family of such circuits with polynomial-size classical descriptions and classical advice depending only on \(\lambda\). Its size and advice polynomial may depend on the adversary. There is no quantum advice or advice correlated with the fresh samples or keys. Uniform honest algorithms and nonuniform adversaries have no external oracle.

A money scheme is one fixed triple of uniform quantum polynomial-time algorithms
\[
 \operatorname{Gen}(1^\lambda)\to(pk,sk),\qquad
 \operatorname{Mint}(sk)\to(\sigma,\rho),\qquad
 \operatorname{Verify}(pk,\sigma,\rho)\to(b,\rho').
\]
Both keys and the serial number \(\sigma\) are classical binary strings; the keys may encode \(\lambda\). The note \(\rho\) occupies a register whose size is bounded by a fixed polynomial in \(\lambda\), as are all honest classical lengths. A scheme specifies its admissible serial and register formats and rejects malformed inputs. The bit \(b=1\) means acceptance. Verification returns the residual note register in its prescribed format, so it can be verified again with the same serial number. Its public inputs are only \((pk,\sigma,\rho)\): it has no secret key, persistent verifier state, external time input or interaction with the bank. Each call uses fresh ancillas and randomness. Mint calls are independent conditional on the classical secret key; the bank retains no correlated quantum minting state. All banknotes have one unit of value.

Reusable correctness requires that for every polynomially bounded integer function \(t(\lambda)\ge1\) there is a negligible \(\mu_t\) such that the following experiment succeeds with probability at least \(1-\mu_t(\lambda)\): generate the keys, mint one honest note, and invoke Verify on that note \(t(\lambda)\) times in succession, feeding each residual register into the next invocation with the unchanged public key and serial. Success means all invocations accept. The probability includes key generation, minting and all verification measurements. The scheme and the original minted note's size are not chosen as a function of \(t\); there is no prescribed expiration time or replacement by the bank.

For security, fix any polynomially bounded integer function \(k(\lambda)\ge0\) and any nonuniform polynomial-size quantum adversary \(\mathcal A\). Generate \((pk,sk)\), mint \(k(\lambda)\) independent notes under this secret key, and give \(1^\lambda\), \(pk\), all serials and all note registers to \(\mathcal A\). It outputs \(k(\lambda)+1\) serial/register pairs. Measure its classical serial outputs and run fresh local copies of Verify on the respective registers. The output registers may be jointly entangled; the acceptance event is the joint outcome of these local tests, not a product of their marginal probabilities. Security requires
\[
 \Pr[\text{all }k(\lambda)+1\text{ output notes are accepted}]
 \le\mu_{\mathcal A,k}(\lambda)
\]
for a negligible function \(\mu_{\mathcal A,k}\). The probability includes all honest randomness and all quantum measurements. Wrong output syntax is a loss. The serials may repeat or differ from those received; no condition of distinct serials weakens the game. The case \(k=0\) forbids creating an accepted note from the public key alone. Since Verify is a public algorithm, the adversary can run it as often as its polynomial circuit size permits. One fixed scheme must satisfy correctness and security for every polynomial repetition count, note count and adversary.

The question is an unrestricted implication between this LWE hardness statement and existence of such a money scheme. No black-box restriction, security-tightness requirement or preservation of the LWE parameter's numerical size is imposed on the reduction; polynomial overhead and polynomial reparameterization are permitted. No ideal random oracle, generic group oracle, trusted hardware, externally supplied setup or additional unproved hardness, obfuscation or leakage assumption is available. The bank's own randomized generation of its public and secret keys is allowed. Anonymity, tracing, public minting and quantum-lightning security are not additional requirements.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the stated implication, including the uniform polynomial-time algorithms, reusable correctness and security reduction to the fixed LWE premise; or give a complete Lean-checked proof of its logical negation in the ordinary computational model. The latter means the LWE premise holds while no scheme satisfying the full definition exists.

A broken candidate, a black-box barrier or an oracle separation alone does not refute this unrestricted existence implication. Schemes with private verification keys, changing public verification keys, expiring notes, a preselected polynomial transfer limit, generic oracles or additional unproved assumptions do not establish it. No numerical approximation tolerance applies to this yes/no target.''',
 source_formulation=dict(text='The sources construct public-key quantum money under stronger assumptions and study restricted barriers to obtaining it from standard cryptographic tools. This card selects the unrestricted implication from its explicitly fixed decisional LWE premise, with static public verification, repeated reuse and a many-note counterfeiting game.',caption='Editorial specialization of the 2024 money definitions and the 2025 evasive-obfuscation barrier; the exact LWE parameters and static reusable interface are fixed by this card.',citation='money',format='editorial_paraphrase'),
 references=[
 ref('money','Anonymous Public-Key Quantum Money and Quantum Voting','Alper Cakan; Vipul Goyal; Takashi Yamakawa',2024,'https://arxiv.org/abs/2411.04482v1','7 November 2024 version; Section 6 Definitions 10–12 pp. 23–24, Section 7 assumptions, Appendix A Definition 19'),
 ref('barrier','On Quantum Money and Evasive Obfuscation','Mark Zhandry',2025,'https://eprint.iacr.org/2025/325','EUROCRYPT 2025; primary abstract, restrictions on mint obfuscation queries and verifier evaluation queries'),
 ref('duality','A General Quantum Duality for Representations of Groups with Applications to Quantum Money, Lightning, and Fire','John Bostanci; Barak Nehoran; Mark Zhandry',2025,'https://mzhandry.github.io/pubs.quantum.html','STOC 2025 entry and abstract; pre-action security and one-way-homomorphism conditions'),
 ref('generic','Public-Key Quantum Money From Standard Assumptions (In The Generic Model)','Jake Doliskani',2025,'https://doliskani.net/jake/pdfs/qm_group_action.pdf','Author manuscript, ePrint 2025/092; abstract, introduction and Section 2.2, generic group-action oracle'),
 ref('timed','How to Sign Quantum Messages','Mohammed Barhoush; Louis Salvail',2026,'https://quantum-journal.org/papers/q-2026-01-22-1980/','Quantum 10, 1980, 22 January 2026; arXiv:2304.06325v5 Section 7 pp. 32–35, Definitions 24–26 and Construction 5/Theorem 8'),
 ],
 context_blocks=[
 block('Public verification and unclonability must coexist: anyone can execute the verifier, while a holder of several valid notes cannot produce one additional accepted note. The definition counts notes even when they share a serial number.','money'),
 block('The anonymous-money construction supplies additional privacy and tracing features under stronger assumptions. Its LWE-based auxiliary encryption primitive does not by itself give money from LWE alone.','money'),
 block('The evasive-obfuscation obstruction limits the oracle access used by the mint and verifier. The current target allows arbitrary constructions and reductions, so that restricted barrier is not its negation.','barrier'),
 block('The group-representation approach supplies money and lightning under group-action or specially structured homomorphism assumptions. These remain different premises from decisional LWE.','duality'),
 block('A reduction to group-action discrete logarithm can still retain an idealized group-action interface. The generic-model theorem does so, whereas this card requires ordinary finite quantum algorithms.','generic'),
 block('The 2026 time-dependent construction from post-quantum one-way functions uses public key announcements and banknotes that expire after their authentication layers are exhausted. Its transfer lifetime is chosen at minting and exhausted notes must return to the bank. The card instead requires a fixed note format reusable for every polynomial number of local verifications.','timed'),
 ],
 progress=[progress('2024-11-07','The anonymous-money preprint constructs public-key money using obfuscation in addition to LWE.','money'),progress('2025','A restricted black-box barrier is proved for evasive-obfuscation approaches.','barrier'),progress('2025','Group-representation constructions use pre-action security and structured homomorphism assumptions.','duality'),progress('2025','The generic group-action analysis reduces cloning to group-action discrete logarithm within that model.','generic'),progress('2026-01-22','Time-dependent public-key money from weaker assumptions is published, with expiring notes and a different verification interface.','timed')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the fixed-LWE implication for static, publicly verifiable and polynomially reusable notes. The stronger-assumption, generic-model and time-dependent results have materially different premises or interfaces; the evasive-obfuscation impossibility is restricted. This review does not independently certify the complete security proofs or exhaust the literature.',summary=[
 'A public-key quantum banknote can be checked using a classical public key without contacting the bank.',
 'The same note must survive every polynomial number of verifications with that fixed key.',
 'An efficient quantum holder of k valid notes must have negligible probability of producing k+1 accepted notes.',
 'The question asks whether a fixed quantum-hard Learning with Errors assumption alone guarantees such a scheme.',
 'A complete Lean-checked answer must prove this unrestricted implication or its ordinary-model negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
