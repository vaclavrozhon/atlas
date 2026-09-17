"""Complete the selected worst-case GapSVP foundation for unbounded classical FHE."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6871';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user-selected polynomial-factor Euclidean GapSVP foundation and permission for a quantum security reduction; the encryption and evaluation algorithms themselves remain classical.',
 'Specified one key-generation algorithm with no circuit-depth or size parameter, compact bit ciphertexts and decryption, and correctness for every polynomial circuit-size bound under the same scheme.',
 'Made the meaning of based solely on worst-case hardness operational: a polynomial-time reduction must turn any inverse-polynomial distinguishing advantage into a solver on every promised lattice instance, rather than recognizing encryption equations as lattice-shaped.',
 'Used classical nonuniform polynomial-size distinguishing circuits, with their descriptions available to the reduction, so a black-box restriction is not added.',
 'Indexed the cryptographic security parameter by lattice rank and allowed an arbitrary fixed polynomial approximation factor; the reduction has polynomial loss for every fixed adversary-size and advantage exponent.',
 'Excluded an independent circular-security, functional-encryption, obfuscation, random-oracle or setup assumption, but did not prohibit bootstrapping or public secret-key encryptions whose security is derived from the stated reduction.',
 'Checked the 2023 functional-encryption construction, the revised 2026 leveled lattice-isomorphism construction, and September 2026 cryptanalysis of a claimed worst-case unbounded scheme.',
 'Assessed importance individually at 94 and required a complete Lean-checked construction and reduction or a refutation of the full existence target.',
]
sources=[
 'Read Peikert, A Decade of Lattice Cryptography, 2016 survey, ePrint 2015/939: §2.2.2 Definition 2.2.3 printed p. 8; §6.1.2 printed p. 66 and §6.1.3 p. 67; §7.2 Question 11 printed p. 76 (PDF p. 78). Question 10 about avoiding bootstrapping is separate. Question 11 does not name a specific worst-case problem; GapSVP is the user-selected specialization.',
 'Read Bitansky–Solomon, Bootstrapping Homomorphic Encryption via Functional Encryption, ITCS 2023 Article 17, DOI 10.4230/LIPIcs.ITCS.2023.17: abstract, §1.1 Theorem 1 pp. 17:1–17:2 and the syntax discussion p. 17:3. It avoids a circular-security assumption using functional encryption, and distinguishes uniform security from nonuniform security with a further assumption. It is not based only on polynomial-factor GapSVP.',
 'Checked Bennett–Lai–Stephens-Davidowitz, Advanced cryptography from lattice isomorphism—new constructions of IBE and FHE, ePrint 2026/465, received 5 March 2026, revised 28 July 2026, CRYPTO 2026: primary abstract and revision metadata explicitly say leveled FHE under a lattice-isomorphism assumption. Full proof not independently rechecked.',
 'Read Sung–Tibouchi, Cryptanalysis of an Unbounded Fully Homomorphic Encryption Scheme, Pragmatic Cybersecurity 1(2), 17, published 9 September 2026, DOI 10.53941/pc.2026.100017: abstract, concluding attack summary and Appendix C p. 16 on the direction and inadequacy of the claimed worst-case security reduction. It attacks Zheng and coauthors’ 2023 CRT construction; this is not an impossibility result for all unbounded FHE.',
 'Checked Liu and coauthors, Efficient Quantum Fully Homomorphic Encryption, arXiv:2604.23490v1, 26 April 2026: the scheme uses a quantum evaluator and its key-generation discussion explicitly generates L+1 independent key pairs. It therefore does not meet this classical depth-independent-key target, regardless of its abstract’s circularity claim.',
 f'Bounded later-work searches through {DATE} found no construction with the selected sole GapSVP reduction. The checked papers and reported attacks have not been independently formalized or exhaustively proof-audited.',
]
complete(identifier,dict(
 title='Unbounded fully homomorphic encryption from polynomial-factor GapSVP',criterion='assumptions',question_type='yes_no',year=2016,is_new=False,
 formal=r'''Does there exist a classical compact fully homomorphic public-key encryption scheme, with keys generated without any circuit-depth bound, and an integer \(a\ge1\), such that there is a quantum polynomial-time reduction from solving worst-case Euclidean \(\mathrm{GapSVP}_{n^a}\) to breaking its chosen-plaintext security, in the precise sense below? The scheme must support every polynomial-size Boolean circuit using the same key-generation algorithm. No independent circular-security or other cryptographic assumption may be used. A quantum reduction is permitted, while key generation, encryption, homomorphic evaluation and decryption are classical.''',
 definitions=r'''For a full-rank rational matrix \(B\in\mathbb Q^{n\times n}\), let
\[
 \mathcal L(B)=\{Bz:z\in\mathbb Z^n\},\qquad
 \lambda_1(\mathcal L)=\min_{v\in\mathcal L\setminus\{0\}}\|v\|_2.
\]
An instance of \(\mathrm{GapSVP}_{n^a}\) is \((B,r)\), where \(r>0\) is rational and either \(\lambda_1(\mathcal L(B))\le r\) (YES) or \(\lambda_1(\mathcal L(B))>n^a r\) (NO). There is no requirement in the gap between these cases. Matrix entries and \(r\) are encoded by signed binary numerators and positive binary denominators; \(L\) denotes their total bit length. The basis is arbitrary and is not sampled from the key-generation distribution or restricted to ideal lattices. The integer \(a\) is chosen once with the construction, independently of the attacker and input size.

A scheme consists of uniform classical algorithms
\[
 \operatorname{Gen}(1^n)\to(pk,evk,sk),\quad
 \operatorname{Enc}(pk,b)\to c,\quad
 \operatorname{Eval}(evk,F,c_1,\ldots,c_t)\to c_F,\quad
 \operatorname{Dec}(sk,c)\to b\in\{0,1\}.
\]
Generation and encryption may use fresh independent fair random bits; evaluation may also be randomized, and decryption is deterministic. Their time is measured in ordinary bit operations. Generation and encryption run in time polynomial in \(n\); evaluation runs in time polynomial in \(n\) and its full input length. The security parameter \(n\) is indexed by the lattice rank in the reduction below. The public encryption key \(pk\), public evaluation key \(evk\) and private key \(sk\) have length bounded by one fixed polynomial \(P(n)\).

The plaintexts are bits, and \(F\) is an explicitly encoded finite Boolean circuit with \(t\) inputs, one output, and fan-in-two AND and OR gates and unary NOT gates. Neither \(F\), its size, its depth nor an upper bound on these is an input to \(\operatorname{Gen}\). Both fresh ciphertexts and evaluated one-bit ciphertexts have length at most \(P(n)\); decryption of these ciphertexts takes at most \(P(n)\) bit operations, independently of \(F\). Thus returning a circuit and its original ciphertext inputs for the holder of the secret key to evaluate is not compact evaluation.

For every polynomial \(p\), there must be a negligible function \(\mu_p(n)\) such that, uniformly over all circuits of size and input count at most \(p(n)\), and all input bit vectors, independently encrypting those bits, applying \(\operatorname{Eval}\), and decrypting produces \(F(b_1,\ldots,b_t)\) with probability at least \(1-\mu_p(n)\). Probability includes all generation, encryption and evaluation coins. Ordinary fresh encryption has the same negligible-error correctness guarantee. A function \(\mu\) is negligible if for every integer \(u\ge1\), eventually \(\mu(n)\le n^{-u}\). The scheme and polynomial \(P\) are fixed before \(p\) is chosen. Unbounded therefore means arbitrary polynomial circuit size and depth without selecting a depth limit during key generation, rather than literal infinite computation.

To state the security reduction without leaving its quantifiers implicit, let \(A\) be a classical randomized Boolean circuit receiving \((pk,evk,c)\) and outputting a bit. Define its distinguishing advantage at parameter \(n\) by
\[
 \operatorname{Adv}_A(n)=
 \left|\Pr[A(pk,evk,\operatorname{Enc}(pk,0))=1]
       -\Pr[A(pk,evk,\operatorname{Enc}(pk,1))=1]\right|.
\]
Each experiment includes a fresh generation of the key tuple, encryption coins and the attacker’s private coins. The size of \(A\) counts its gates, input bits and random bits. The family of attacker circuits may be nonuniform; it need not be produced by one efficient algorithm. The public key allows further encryptions, so this is the usual bit-message chosen-plaintext indistinguishability requirement.

The requested reduction guarantee is the following. For every fixed integer \(u\ge1\), there exist a uniform quantum algorithm \(R_u\), a polynomial \(Q_u\), and an integer \(N_u\), such that whenever \(n\ge N_u\), \(|A|\le n^u\) and \(\operatorname{Adv}_A(n)\ge n^{-u}\), the algorithm
\[
 R_u(1^n,\langle A\rangle,B,r)
\]
correctly decides every promised rank-\(n\) instance \((B,r)\) of \(\mathrm{GapSVP}_{n^a}\) with probability at least \(2/3\), in time at most \(Q_u(n+L+|A|)\). The clock holds on every execution. Here \(\langle A\rangle\) is the full attacker circuit description, which the reduction may inspect; black-box access is not required. Quantum time uses a uniform finite gate model, for example Hadamard, T, CNOT and computational-basis measurements, together with charged classical bit operations. No ideal cryptographic oracle is supplied.

This states a polynomial-loss worst-case security foundation rather than assuming the scheme’s security outright. In particular, a nonnegligible polynomial-size attack yields a quantum polynomial-time solver on all promised lattice inputs at the corresponding infinitely many insecure ranks. Under worst-case GapSVP hardness against such nonuniform quantum solvers on infinitely many ranks, the scheme has negligible advantage against every polynomial-size classical attacker. The task does not ask for an unconditional proof that GapSVP is hard. Quantum algorithms in the security proof do not mean that the scheme itself uses quantum messages or that security against quantum attackers is additionally required.

All public auxiliary material must be generated by \(\operatorname{Gen}\) and included in the attacker’s view. Bootstrapping and encryptions involving secret-key bits may be used, but their security must follow from the stated reduction. There is no separate circular-security, key-dependent-message, obfuscation or functional-encryption assumption, no random oracle, and no external trusted setup. The evaluator receives no subsequent assistance from the secret-key holder.''',
 answer_criterion=r'''Give a complete Lean-checked construction of the scheme and its correctness, compactness and quantum worst-case reduction, with all the displayed quantifiers and bounds, or a complete Lean-checked refutation of this existence statement. A positive result must specify an actual fixed polynomial approximation factor; hardness of a superpolynomial-factor problem or an unspecified lattice problem does not establish this specialization.

A construction whose keys depend on a preselected depth, one that adds a circular-security or other independent assumption, or a scheme with a quantum evaluator does not meet the target. An attack on one candidate or a separation for one restricted type of security reduction does not rule out all the constructions allowed here. A conditional obstruction must retain its hypothesis unless that hypothesis is also proved. No numerical tolerance weakens the resource, security or correctness requirements.''',
 source_formulation=dict(text='Peikert asks whether unbounded fully homomorphic encryption can be based solely on a worst-case complexity assumption. The user selected Euclidean GapSVP with a polynomial approximation factor and allowed a quantum security reduction, while retaining classical compact encryption and keys generated without a depth bound. The neighboring question about avoiding bootstrapping is separate.',caption='Paraphrase of A Decade of Lattice Cryptography, §7.2 Question 11, printed p. 76 / PDF p. 78; specialization selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=94,method='editorial',reason='A sole worst-case lattice foundation would close a central assumption gap between leveled and unbounded encrypted computation, removing the separate security premise for key-dependent public material.',basis='Individual assessment of Peikert’s Question 11, the user-selected polynomial-factor GapSVP specialization and the distinction from constructions based on additional functional-encryption or obfuscation assumptions.'),
 why='Leveled encryption chooses its keys for a known computation depth. This asks for one reusable key setup supporting arbitrary polynomial-depth computation, with a security proof grounded entirely in a standard worst-case lattice problem.',
 references=[
 ref('primary','A Decade of Lattice Cryptography','Chris Peikert',2016,'https://eprint.iacr.org/2015/939','2016 survey; §2.2.2 Definition 2.2.3 printed p. 8; §6.1.2 pp. 66–67; §7.2 Question 11 printed p. 76 / PDF p. 78'),
 ref('functional','Bootstrapping Homomorphic Encryption via Functional Encryption','Nir Bitansky; Tomer Solomon',2023,'https://doi.org/10.4230/LIPIcs.ITCS.2023.17','ITCS 2023, LIPIcs 251, Article 17; abstract and §1.1 Theorem 1 pp. 17:1–17:2; syntax and depth-independent keys p. 17:3'),
 ref('isomorphism','Advanced cryptography from lattice isomorphism—new constructions of IBE and FHE','Huck Bennett; Zhengnan Lai; Noah Stephens-Davidowitz',2026,'https://eprint.iacr.org/2026/465','Received 5 March 2026, revised 28 July 2026; CRYPTO 2026 revision; primary abstract explicitly specifies leveled FHE and a lattice-isomorphism assumption'),
 ref('attack','Cryptanalysis of an Unbounded Fully Homomorphic Encryption Scheme','Hyewon Sung; Mehdi Tibouchi',2026,'https://doi.org/10.53941/pc.2026.100017','Pragmatic Cybersecurity 1(2), Article 17, published 9 September 2026; abstract, concluding attack summary, and Appendix C p. 16 on flaws of the claimed worst-case reduction'),
 ],
 context_blocks=[
 block('The survey separates two questions: reducing the cost or use of bootstrapping, and proving unbounded security solely from a worst-case assumption. This card selects the latter; a construction may bootstrap if its entire security proof meets the stated foundation.'),
 block('The 2023 construction avoids a circular-security assumption by using functional encryption under additional assumptions. Its nonuniform-security statement also needs a further complexity assumption. It therefore does not supply the selected sole GapSVP foundation.','functional'),
 block('The revised 2026 lattice-isomorphism construction is explicitly leveled and uses a different underlying assumption. The presence of fully homomorphic encryption in its title is not by itself a depth-independent-key guarantee.','isomorphism'),
 block('September 2026 cryptanalysis breaks a proposed unbounded CRT-based scheme and explains why expressing its encryption equation as a structured lattice task is not a worst-case security reduction. This rejects that candidate, not the possibility of the target construction.','attack'),
 ],
 progress=[progress('2016','The survey poses the sole worst-case foundation question separately from eliminating bootstrapping.'),progress('2023','A functional-encryption construction removes circularity while retaining additional assumptions.','functional'),progress('2026-07-28','A revised lattice-isomorphism preprint gives leveled FHE under its specified isomorphism assumption.','isomorphism'),progress('2026-09-09','Published cryptanalysis refutes a claimed unbounded CRT construction and examines its proposed worst-case foundation.','attack')],
 related_problem_ids=sorted(set(json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text()).get('related_problem_ids',[])+['TCS-6551'])),
),notes,sources,'The checked 2016 question remains distinct from later constructions using functional encryption, a different lattice problem, depth-dependent keys or quantum evaluation. September 2026 cryptanalysis rejects a specific claimed worst-case construction. Bounded checks through 17 September 2026 found no scheme with the selected sole polynomial-factor GapSVP reduction; cited proofs and attacks were not independently Lean-verified.',summary=[
 'The target is classical compact fully homomorphic encryption with keys generated before any computation-depth limit is chosen.',
 'One scheme must correctly evaluate every polynomial-size Boolean circuit while keeping ciphertexts and decryption bounded by one fixed polynomial in the security parameter.',
 'Its only security foundation is the worst-case difficulty of Euclidean GapSVP with a fixed polynomial approximation factor.',
 'A quantum security reduction may inspect a classical attacker and must turn its distinguishing advantage into a solver for arbitrary promised lattice instances.',
 'A complete Lean-checked construction or refutation is required; additional circular-security assumptions and depth-dependent constructions do not settle the target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());next(r for r in a if r['id']==identifier).update(state='applied',applied_on=DATE);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
