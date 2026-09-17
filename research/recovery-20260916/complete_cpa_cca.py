"""Complete the unrestricted plain-model CPA-to-CCA2 existence question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6548';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained an unrestricted classical nonuniform-security existence implication in the plain model, with full adaptive CCA2 rather than CCA1 or fixed-query bounded CCA.',
 'Defined the finite algorithms, total decryption on arbitrary bit strings, worst-case polynomial running times, uniform correctness and negligible-error quantifiers.',
 'Specified the two-stage challenge game, equal message lengths, pre/post-challenge oracle access, exact-string challenge exclusion and independent randomness.',
 'Made explicit that one scheme must withstand every polynomial attack bound and that the construction need not preserve efficiency or use the source primitive as a black box.',
 'Rechecked restricted separation, bounded-CCA and stronger-assumption constructions, including the July 2026 threshold-encryption revision.',
 'Preserved importance score 95 and required a complete Lean-checked proof of the existence implication or its ordinary-model negation.',
]
sources=[
 'Read Trevisan, CS276 Projects, undated primary course page, Impossibility Results item on CCA from CPA: explicitly asks both black-box derivability and derivability by any means.',
 'Read the primary indexed abstract of Gertner–Malkin–Myers, TCC 2007: separation is restricted to black-box constructions whose new decryption does not query the old encryption. Read the independent author discussion of this restriction in Choi et al., TCC 2008 p. 428–429.',
 'Read Choi–Dachman-Soled–Malkin–Wee, TCC 2008 author/proceedings PDF, introduction p. 428, Bounded CCA2 non-malleability: query bound q is fixed before scheme parameters, and the construction is parameterized by that bound. This does not meet one-scheme-for-all-polynomials security.',
 'Read Hohenberger–Koppula–Waters, CRYPTO 2020 author manuscript, abstract and introduction pp. 1–2: injective trapdoor functions suffice without lossiness/correlated-product assumptions; the CPA-to-CCA implication is explicitly the broader goal. Their discussion also distinguishes extra hinting-PRG security.',
 'Read the primary indexed abstract of Koppula–Waters, February 25 2019 manuscript hosted by NTT Research, and ePrint 2018/847 indexed hinting-property discussion: ordinary CPA security is supplemented by a special PRG security guarantee. The original IACR archive PDF link did not open in this check.',
 'Read Matsuda, ePrint 2023/1957, PKC 2025, primary abstract and dated revision note of 12 May 2025: a publicly verifiable noninteractive BARG remains an extra premise, with weaker succinctness than the known NIZK implication requires.',
 'Read Brzuska–Klooß–Woo, ePrint 2025/1665, PKC 2026, primary abstract and revision history through 17 July 2026: the arbitrary-CPA threshold transform is in the random-oracle model, while the other route needs semi-malicious CPA security and its other proof-system resources.',
 f'Bounded primary-source searches through {DATE} found no verified ordinary-model resolution of the unrestricted implication. The cited security reductions and impossibility proofs were not independently certified.',
]
complete(identifier,dict(
 title='Chosen-ciphertext security from ordinary public-key encryption',criterion='assumptions',question_type='yes_no',
 formal=r'''Does the existence of an IND-CPA-secure public-key encryption scheme imply the existence of an IND-CCA2-secure public-key encryption scheme in the plain model, with correctness and classical security as defined below, against all nonuniform polynomial-size adversaries? The sole premise is ordinary chosen-plaintext-secure public-key encryption, and the conclusion is full adaptive chosen-ciphertext security with no fixed bound on an attacker's polynomial number of decryption queries.''',
 definitions=r'''A public-key encryption scheme consists of one fixed triple of uniform classical algorithms
\[
 \operatorname{Gen}(1^n)\to(pk,sk),\qquad
 \operatorname{Enc}(pk,m)\to c,\qquad
 \operatorname{Dec}(sk,c)\to m\text{ or }\bot .
\]
Here \(n\ge1\) is a security parameter, and keys, messages and ciphertexts are finite binary strings. The symbol \(\bot\) is distinct from every message. Gen and Enc use independent fair random bits; Dec is deterministic. Each algorithm is a finite Turing program with worst-case time polynomial in its full input length, including \(n\), which may be included in the keys. In particular, Gen has polynomially bounded output length. Encryption supports arbitrary binary messages; decryption is defined and halts on every ciphertext string, with malformed encodings rejected. The algorithms use no external oracle or advice.

A function \(\mu:\mathbb N\to[0,1]\) is negligible if, for every integer \(a\ge1\), there is \(N_a\) such that \(\mu(n)\le n^{-a}\) for all \(n\ge N_a\). Correctness requires that, for every polynomial length bound \(p\), some negligible function \(\mu_p\) satisfies
\[
 \max_{|m|\le p(n)}
 \Pr_{(pk,sk)\leftarrow\operatorname{Gen}(1^n),\ \operatorname{Enc}}
 [\operatorname{Dec}(sk,\operatorname{Enc}(pk,m))\ne m]
 \le\mu_p(n).
\]
The maximum includes the empty message. Neither perfect correctness nor recovery of the encryption randomness is required.

An adversary is a nonuniform family of classical polynomial-size computations with polynomially many fair random bits and polynomial-size advice. Advice can depend on \(n\), but not on the independently sampled keys, challenge bit or honest encryption coins. Total running time, state, message lengths, oracle-query lengths and number of queries are bounded by some polynomial in \(n\) that may depend on the adversary. Equivalently, these are polynomial-size Boolean circuits with the specified adaptive oracle interfaces. Arbitrary polynomial-size auxiliary information independent of the fresh experiment is included in the advice.

In the IND-CPA experiment, generate \((pk,sk)\), give \((1^n,pk)\) to the first stage \(A_1\), and let it output two equal-length messages \(m_0,m_1\) and a state \(\sigma\). Choose an independent uniform bit \(b\), form \(c^*=\operatorname{Enc}(pk,m_b)\) with fresh coins, and give \((1^n,pk,\sigma,c^*)\) to \(A_2\), which outputs a bit \(\widehat b\). Its advantage is
\[
 \left|\Pr[\widehat b=b]-\frac12\right|.
\]
The probability includes all key-generation, challenge-encryption, challenge-bit and adversary randomness. The quantification is over adversaries obeying the equal-length challenge rule and producing a bit; failures to follow this syntax may instead be defined to yield an independent fair guess. Both stages can compute arbitrary encryptions themselves using the public algorithm, so a separate encryption oracle is unnecessary. The scheme is IND-CPA secure if this advantage is negligible for every adversary just defined.

The IND-CCA2 experiment is the same except for adaptive decryption access. Before the challenge, \(A_1\) may query any ciphertext \(c\), receiving \(\operatorname{Dec}(sk,c)\). After it chooses the messages and receives \(c^*\), \(A_2\) has the oracle
\[
 \mathcal D_{sk,c^*}(c)=
 \begin{cases}
 \bot,&c=c^*\text{ as binary strings},\\
 \operatorname{Dec}(sk,c),&c\ne c^*.
 \end{cases}
\]
Every later query may depend on the challenge and all earlier answers. The exclusion applies only after the challenge is issued; it does not retroactively invalidate a pre-challenge query. Any different string is permitted, even if it encodes related data or decrypts to the challenge plaintext. The scheme is IND-CCA2 secure if the same advantage is negligible for every such two-stage adversary.

For each security notion, one fixed scheme must satisfy the definition for every polynomially bounded adversary. The scheme cannot be chosen after fixing a maximum number of decryption queries. Its negligible bound may depend on the adversary. All security is classical; no quantum adversary is requested.

The plain model provides no ideal random oracle, externally supplied common reference string, trusted hardware or separate setup. The recipient's own random key generation is allowed. The question is an implication between existence statements. A resulting scheme may use the descriptions of the starting algorithms, change all formats and incur any fixed polynomial overhead. No particular compiler, black-box access discipline or preservation of the starting efficiency is required.''',
 answer_criterion=r'''Give a complete Lean-checked proof that an IND-CPA scheme implies an IND-CCA2 scheme satisfying the precise definitions, with proofs of uniform implementation, polynomial running time, correctness and security; or give a complete Lean-checked proof of the negation of this existence implication in the ordinary computational model.

Breaking a particular CPA scheme under chosen-ciphertext attack does not disprove the existence of a different secure scheme. A separation restricted to black-box constructions, or relative to an oracle, is not a negative resolution here. Additional trapdoor, proof-system, pseudorandomness or setup assumptions must themselves follow from the sole premise. Security only before the challenge, only against an a priori bounded number of decryption queries, or only against ciphertext modification without the stated decryption access is insufficient. No numerical approximation tolerance applies.''',
 source_formulation=dict(text='Trevisan explicitly poses the implication from CPA-secure to CCA-secure public-key encryption, both for black-box constructions and for arbitrary methods. This card retains the unrestricted existence question and specifies full adaptive CCA2 security in the ordinary plain model.',caption='Paraphrase of the undated CS276 project list, Impossibility Results section, item immediately preceding the Gertner–Malkin–Myers and Choi–Dachman-Soled–Malkin–Wee references.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','CS 276 — Projects','Luca Trevisan',None,'https://theory.stanford.edu/~trevisan/cs276/projects.html','Undated course page; Impossibility Results item asking CCA from CPA by black-box or arbitrary methods'),
 ref('barrier','Towards a Separation of Semantic and CCA Security for Public Key Encryption','Yael Gertner; Tal Malkin; Steven Myers',2007,'https://www.iacr.org/archive/tcc2007/43920433/43920433.pdf','TCC 2007 pp. 434–455; abstract, restriction on constructed decryption querying original encryption'),
 ref('bounded','Black-Box Construction of a Non-malleable Encryption Scheme from Any Semantically Secure One','Seung Geol Choi; Dana Dachman-Soled; Tal Malkin; Hoeteck Wee',2008,'https://www.cs.columbia.edu/~dglasner/MyPapers/non-mal.pdf','TCC 2008; introduction p. 428, Bounded CCA2 non-malleability, q fixed before parameters; separation discussion pp. 428–429'),
 ref('hinting','Realizing Chosen Ciphertext Security Generically in Attribute-Based Encryption and Predicate Encryption','Venkata Koppula; Brent Waters',2019,'https://eprint.iacr.org/2018/847','February 25, 2019 author manuscript; abstract and hinting-property discussion, additional PRG security'),
 ref('trapdoor','Chosen Ciphertext Security from Injective Trapdoor Functions','Susan Hohenberger; Venkata Koppula; Brent Waters',2020,'https://par.nsf.gov/servlets/purl/10295635','CRYPTO 2020; author manuscript abstract and introduction pp. 1–2, injective-TDF sufficient assumption and broader CPA-to-CCA goal'),
 ref('barg','Chosen Ciphertext Security via BARGs','Takahiro Matsuda',2025,'https://eprint.iacr.org/2023/1957','PKC 2025; primary abstract and revision note of 12 May 2025, weaker succinctness with a BARG still supplied'),
 ref('threshold','Threshold Public-Key Encryption: Definitions, Relations, and CPA-to-CCA Transforms','Chris Brzuska; Michael Klooß; Ivy K. Y. Woo',2026,'https://eprint.iacr.org/2025/1665','PKC 2026 full version, revised 17 July 2026; primary abstract distinguishes semi-malicious CPA and random-oracle routes'),
 ],
 context_blocks=[
 block('Public encryption already permits arbitrary chosen plaintexts. The stronger game additionally returns decryptions of adaptively selected ciphertexts, including queries after the challenge. The exact challenge string is excluded because its decryption would reveal the challenge message directly.'),
 block('The source asks whether some stronger scheme follows from the existence of a weaker one. An attack on an individual CPA-secure scheme does not settle that foundational implication.'),
 block('The 2007 separation applies to a restricted black-box class in which the new decryption does not query the original encryption algorithm. It does not exclude unrestricted constructions.','barrier'),
 block('The 2008 bounded-CCA result fixes the query bound before constructing the scheme. Here one scheme must handle every polynomial-time attacker, including attackers with a larger query polynomial.','bounded'),
 block('Injective trapdoor functions suffice without the extra lossiness or correlated-product guarantees required in earlier approaches. An ordinary encryption scheme need not recover its encryption randomness or provide such an injective function.','trapdoor'),
 block('A hinting pseudorandom generator supplies a stronger security property than ordinary pseudorandomness. The corresponding generic upgrade keeps that additional requirement.','hinting'),
 block('The revised batch-argument result reduces the proof-length saving required of the extra argument system. It does not remove that additional resource.','barg'),
 block('The threshold-encryption transforms have different prerequisites: the route from arbitrary CPA security uses a random oracle, while the other route assumes stronger security and further proof-system resources. Neither primary abstract establishes the exact plain-model implication here.','threshold'),
 ],
 progress=[progress('2007','A restricted black-box separation is proved.','barrier'),progress('2008','CPA encryption is upgraded to non-malleability and a bounded-CCA extension.','bounded'),progress('2019','Generic upgrades use an additional hinting PRG.','hinting'),progress('2020','Injective trapdoor functions are shown sufficient for CCA encryption.','trapdoor'),progress('2025-05-12','The BARG revision weakens succinctness while retaining the extra argument system.','barg'),progress('2026-07-17','The threshold-encryption revision retains its stronger-security or random-oracle prerequisites.','threshold')],
),notes,sources,'The primary course source poses the unrestricted CPA-to-CCA implication. The inspected separation is restricted to a black-box class, the bounded-CCA result fixes an a priori query bound, and later constructions retain additional primitives or model assumptions. Bounded primary-source checks through 17 September 2026 found no verified resolution of the exact plain-model classical nonuniform-security implication. Cited security proofs were not independently certified.',summary=[
 'Ordinary public-key encryption hides a chosen challenge message from an attacker who can encrypt messages independently.',
 'Full chosen-ciphertext security must still hide it when the attacker adaptively obtains decryptions of every other ciphertext.',
 'The question asks whether the weaker primitive alone implies the existence of the stronger one in the plain model.',
 'One fixed scheme must tolerate every polynomial attack bound, and the construction may use the original algorithms in an unrestricted way.',
 'A complete Lean-checked answer must establish this existence implication or refute it in the ordinary computational model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
