"""Make the ordinary uniform polynomial-time learning-to-PRF implication explicit."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5793'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the full question and the paper’s explicit caveats concerning nonuniformity and the exponential-security regime.',
 'Specified the ordinary uniform polynomial-time interpretation of efficient learning and cryptographic security.',
 'Defined the exact list of typical circuit classes, their size/depth conventions and improper learning with adaptive membership queries under the uniform distribution.',
 'Separated worst-case nonlearnability from the stronger hypothesis of an efficiently sampled hard target distribution.',
 'Defined an efficiently sampled distribution of target circuits in the same class without imposing an additional same-class restriction on the sampler.',
 'Checked the conditional 2021 uniformization result, the 2025 bounded-query PRF candidate and the 2026 average-case learning characterization; none proves the selected implication.',
]
sources=[
 'Read Oliveira–Santhanam, CCC 2017 Article 18, §1.1 Theorem 3 p. 18:4, the open question and qualifications p. 18:7, §2.1–2.2 pp. 18:14–18:16, Definitions 27–28 pp. 18:24–18:25 and Theorem 34/Corollary 35 with the uniformity remark p. 18:28.',
 'Read Binnendyk, ECCC TR21-132 revision 1, accepted 16 October 2021, abstract and introduction pp. 1–2. Its uniform conclusion requires a constructive procedure supplying distinguishers; it is not the unrestricted ordinary-hardness implication.',
 'Read Ball–Ducros–Erabelli–Kohl–Resch, Strong Pseudorandom Functions in AC0[2] in the Bounded-Query Setting, author manuscript dated 13 November 2025, abstract and §§1.1–1.4, especially the learning dichotomy question p. 7. The proposed function is a candidate, with restricted attacks analyzed and full security conjectured.',
 'Read Hirahara–Nanashima, A Sharp Characterization of Pessiland, ECCC TR26-052 as downloaded 16 September 2026, abstract and §1 pp. 1–2. Its equivalences concern average-case agnostic learning and do not remove the target-distribution requirement in this card.',
 'Bounded primary-source searches through 16 September 2026 found no theorem proving or refuting the selected uniform polynomial-time same-class implication. No assertion of independently checking the full cited proofs is made.',
]
status=('The source proves a related dichotomy for nonuniform learning and a different security/time regime, not the uniform polynomial-time implication specified here. '
 'The checked 2021 uniformization adds a constructive distinguisher premise, the 2025 work still asks a related bounded-query dichotomy, and the 2026 characterization concerns average-case learning. '
 'No resolution of the selected implication was found in the bounded review.')
complete(identifier,dict(
 title='Pseudorandom functions from worst-case hardness of learning',
 criterion='assumptions',question_type='yes_no',
 formal=r'''For every circuit class
\[
\mathcal C\in\{\mathrm{AC}^0,\ \mathrm{AC}^0[p]\ (p\text{ any fixed prime}),\
\mathrm{ACC}^0,\ \mathrm{TC}^0,\ \mathrm{NC}^1,\
\mathrm{Formula},\ \mathrm{Circuit}\},
\]
does the following implication hold?
\[
\neg\operatorname{Learn}_{\mathrm{poly}}(\mathcal C)
\quad\Longrightarrow\quad
\operatorname{PRF}_{\mathrm{poly}}(\mathcal C).
\]
Here learning means uniform randomized polynomial-time improper learning under the uniform input distribution, with adaptive membership queries. The conclusion is a uniformly polynomial-time samplable family of functions computed by polynomial-size \(\mathcal C\)-circuits, secure against every uniform probabilistic polynomial-time oracle distinguisher. Both notions are defined below.

The hypothesis is only worst-case failure of learning: each candidate learner may fail on its own target function. No efficiently samplable common distribution of hard targets is assumed.''',
 definitions=r'''All targets are Boolean functions on \(\{0,1\}^n\), with \(n\ge2\). Circuits are finite directed acyclic graphs with input bits, optional constants, and a single Boolean output. Size counts wires; depth is the longest input-to-output gate path. Negation gates have one input. General \(\mathrm{Circuit}\) uses AND and OR gates of fan-in at most two and NOT gates, with unrestricted depth. \(\mathrm{Formula}\) uses the same basis but has a tree of gates, with no reuse of a gate output. \(\mathrm{NC}^1\) uses that bounded-fan-in circuit basis with depth at most \(d\lceil\log_2(n+1)\rceil\) for a fixed integer \(d\).

For \(\mathrm{AC}^0\), AND/OR gates may have unbounded fan-in and depth is at most a fixed integer \(d\). The class \(\mathrm{AC}^0[p]\) additionally permits a gate testing whether the number of ones among its inputs is divisible by the fixed prime \(p\). For \(\mathrm{ACC}^0\) the same definition permits any fixed integer modulus \(m\ge2\); the modulus does not grow with \(n\). The class \(\mathrm{TC}^0\) instead additionally permits unweighted majority gates, which output one when at least half their inputs are one. Negations and constants are allowed in all classes. These conventions specify classes of target functions; targets need not themselves be uniformly generated.

A fixed polynomial subfamily is specified by an integer \(k\ge1\), the wire bound \(n^k\), and, where relevant, fixed \(d\) and \(m\). Write \(\mathcal C_{\theta,n}\) for the resulting set of \(n\)-input functions, where \(\theta\) collects these fixed constants. For \(\mathrm{AC}^0[p]\), \(p\) is fixed as part of the choice of class.

The assertion \(\operatorname{Learn}_{\mathrm{poly}}(\mathcal C)\) means that for every fixed \(\theta\) there is one probabilistic oracle Turing machine \(L_\theta\) and a polynomial \(P_\theta\) with the following property. For every \(n\ge2\), integer \(q\ge2\), and \(f\in\mathcal C_{\theta,n}\), the machine \(L_\theta^f(1^n,1^q)\) halts within \(P_\theta(n,q)\) steps on every execution and, with probability at least \(2/3\), outputs a finite ordinary Boolean circuit \(h\) satisfying
\[
\Pr_{x\leftarrow\{0,1\}^n}[h(x)\ne f(x)]\le 1/q.
\]
It may adaptively query any \(n\)-bit input and receive its exact value under \(f\); writing queries and the hypothesis counts toward its time. The hypothesis need not belong to \(\mathcal C\), and the target circuit description is not supplied. The polynomial running-time bound also holds for every other Boolean oracle. There is no advice depending on \(n\). Negating this definition gives the hardness premise with its quantifiers, including the possibility that the hard target depends on the learner and on \(n\).

The assertion \(\operatorname{PRF}_{\mathrm{poly}}(\mathcal C)\) means that for some fixed \(\theta\), some polynomial-time computable seed length \(a(n)\le n^r\), and a single deterministic polynomial-time sampler \(S\), every \(S(1^n,s)\), \(s\in\{0,1\}^{a(n)}\), describes a circuit for a function \(f_{n,s}\in\mathcal C_{\theta,n}\). The sampler runs in polynomial time in \(n\), including writing its entire output. It may be a general polynomial-time algorithm; only the sampled functions are required to have the stated \(\mathcal C\)-circuits.

For every uniform probabilistic oracle Turing machine \(D\) running in polynomial time in \(n\), the advantage
\[
\left|
\Pr_{s\leftarrow\{0,1\}^{a(n)}}[D^{f_{n,s}}(1^n)=1]
-
\Pr_{g\leftarrow\mathcal F_n}[D^g(1^n)=1]
\right|
\]
is negligible in \(n\), where \(\mathcal F_n\) is the set of all Boolean functions on \(n\) bits with its uniform distribution. Both probabilities include \(D\)'s random bits. The same sampled function answers all queries consistently. The distinguisher may choose polynomially many queries adaptively but does not receive the seed or circuit description. A nonnegative function \(\eta(n)\) is negligible when for every integer \(j\ge1\), \(\eta(n)\le n^{-j}\) for all sufficiently large \(n\). Security is eventual at all lengths, not merely on an unspecified infinite subsequence.

The implication is asked in the ordinary, unrelativized model. It does not require a black-box construction or an algorithm that extracts a sampler from a description of a hardness proof. This card fixes the uniform polynomial-time meaning of the source’s broader question; its exponential and nonuniform theorem is recorded separately as context.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the displayed implication for the specified classes and quantifiers. A proof must obtain the efficiently sampled same-class family from the stated learning-hardness premise alone. Assuming a samplable hard target distribution, proving only a nonuniform or exponential-time dichotomy, or supplying a conditional PRF candidate does not suffice. A refutation must establish a failure of this implication in the stated unrelativized model; a relativizing or black-box barrier alone is not a refutation. This is a binary implication question, with exact security and learning quantifiers; numerical \(1/100\) slack does not alter them.''',
 source_formulation=dict(
 text='The source asks whether ordinary failure of efficient learning already forces pseudorandom functions within the same circuit class, and distinguishes this from earlier results assuming a hard distribution over targets.',
 caption='Paraphrase of p. 18:7, with the uniform polynomial-time target made explicit and the paper’s nonuniform exponential-regime theorem kept separate.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=85,method='editorial',
 reason='The implication would connect generic worst-case learning hardness directly to cryptographic pseudorandomness while preserving the computational class of the target functions.',
 basis='Individual assessment of the generic scope across central circuit classes, the gap between worst-case and distributional hardness, and the uniformity and efficiency requirements.'),
 why='A function class may resist every efficient learner without coming with a usable way to sample difficult targets. Cryptographic pseudorandomness requires a single efficient sampling procedure whose outputs defeat every efficient observer. The question asks whether the first obstruction alone supplies the second object within the same class.',
 references=[
 ref('primary','Conspiracies Between Learning Algorithms, Circuit Lower Bounds, and Pseudorandomness',
 'Igor C. Oliveira; Rahul Santhanam',2017,'https://doi.org/10.4230/LIPIcs.CCC.2017.18',
 'CCC 2017, Article 18; p. 18:7; §§2.1–2.2; Definitions 27–28; Theorem 34 and Corollary 35 p. 18:28'),
 ref('uniform','Pseudo-random functions and uniform learnability',
 'Eric R. Binnendyk',2021,'https://eccc.weizmann.ac.il/report/2021/132/',
 'ECCC TR21-132, revision 1 accepted 16 October 2021; abstract and introduction pp. 1–2; manuscript cover dated May 2021'),
 ref('bounded','Strong Pseudorandom Functions in AC0[2] in the Bounded-Query Setting',
 'Marshall Ball; Clément Ducros; Saroja Erabelli; Lisa Kohl; Nicolas Resch',2025,
 'https://eprint.iacr.org/2025/2085',
 'Author manuscript dated 13 November 2025, §§1.1–1.4, especially open questions p. 7; checked copy https://ir.cwi.nl/pub/35800/35800.pdf'),
 ref('pessiland','A Sharp Characterization of Pessiland',
 'Shuichi Hirahara; Mikito Nanashima',2026,'https://eccc.weizmann.ac.il/report/2026/052/',
 'ECCC TR26-052 as downloaded 16 September 2026; abstract and §1 pp. 1–2, average-case agnostic-learning characterization'),
 ],
 context_blocks=[
 block('The source explicitly distinguishes a hard distribution of targets from the ordinary statement that every learner fails on some target. The card retains the latter premise; efficient sampling is part of the desired conclusion.'),
 block('The paper’s learning model uses the uniform distribution on input strings and allows adaptive membership queries. Its hypotheses are unrestricted Boolean circuits, so imposing proper learning would change the premise.'),
 block('The source obtains a nonuniform learning–pseudorandomness dichotomy in an exponential security/time regime. Theorem 34 and Corollary 35 do not assert that failure of uniform polynomial-time learning gives a uniformly sampled, polynomially secure family.'),
 block('The checked 2021 work studies uniform learners using a stronger constructive assumption that supplies suitable distinguishers. It therefore does not remove the additional premise needed for the ordinary implication stated here.','uniform'),
 block('The November 2025 manuscript proposes a low-depth PRF candidate and analyzes several restricted attack classes. Its full security is conjectural, and it separately lists a learning–PRF dichotomy in its bounded-query setting as open.','bounded'),
 block('The 2026 Pessiland characterization concerns average-case agnostic-learning tasks and approximation factors. Those distributional hypotheses and outputs differ from worst-case learning of every target in a fixed circuit class.','pessiland'),
 ],
 progress=[
 progress('2017','The source proves its nonuniform dichotomy and records the broader learning-hardness question with explicit caveats.'),
 progress('2021-10-16','The revised uniform-learnability report retains an additional constructive distinguisher premise.','uniform'),
 progress('2025-11-13','The checked low-depth PRF manuscript records a related bounded-query dichotomy as open.','bounded'),
 progress('2026','The Pessiland report sharpens average-case learning characterizations without settling this worst-case same-class implication.','pessiland'),
 progress('2026-09-16','The review fixes the uniform polynomial-time, improper membership-query learning and strong oracle-security conventions.'),
 ],
),notes,sources,status,summary=[
 'A learning algorithm receives query access to an unknown function and must output a circuit that predicts it accurately on uniformly random inputs.',
 'The question asks whether failure of efficient learning forces an efficiently sampled pseudorandom function family in the same circuit class.',
 'The premise permits a different hard target for each learner and does not assume a common samplable distribution of hard targets.',
 'Both the learner and the sampler are uniform polynomial-time algorithms, and security permits adaptive chosen queries.',
 'The source’s nonuniform exponential-regime theorem and the checked later qualified results do not establish this implication.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
