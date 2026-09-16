"""Complete the total-function BPP versus deterministic RP-oracle question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4771'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the explicit total-function BPPcc equals P-to-RPcc question, distinct from the constant-query hierarchy proved strict in the source.',
 'Defined public-coin worst-case communication, nonuniform function families and exact ideal oracle answers.',
 'Specified adaptive oracle protocols by weighted binary trees; each total oracle test is charged its one-sided-error communication cost plus one.',
 'Required a polylogarithmic bound across all input lengths, allowing the exponent to depend on the function family.',
 'Individually assessed importance from the scope of the general randomness-to-oracle simulation, not the presence of an open-question paragraph.',
 'Checked the August 2026 oracle-separation preprint: its separation statement permits partial functions and does not resolve this total-function target.',
]
sources=[
 'Read Pitassi–Shirley–Watson, ICALP 2020 Article 92: §1 p. 2 explicit BPPcc=P^RPcc question restricted to total functions; §1.1 pp. 3–4 and Theorems 1–3; §2 p. 6 public-coin RP model; §2.2 pp. 8–9 oracle cost convention. Also inspected the original ECCC TR19-043 manuscript; the conference version supplies the primary target.',
 'Read Watson, arXiv:2608.26425v1 submitted 26 August 2026, cover dated 28 August: abstract and §1 pp. 1–3, Figure 1, and §1.1 model definitions. The ambient functions there are partial; its BPP-not-subset-P^RP remark follows the older partial-function BPP-versus-P^NP separation. It is not a total-function separation. Full proof of the new MA-versus-NP^BPP theorem was not audited.',
 'Checked the arXiv:2407.20204v2 abstract and version date 6 May 2025: it separates constant-cost communication from reductions to fixed Hamming-distance oracles, a more restricted oracle family than every RP function. The source metadata was inspected, not the entire proof.',
 'Checked ECCC TR25-060 revision 1 accepted 31 March 2026: its abstract concerns sign-rank of fixed Hamming distance, not the total-function polylogarithmic RP-oracle equality. Bounded later searches through 16 September 2026 found no resolution of the selected equality.',
]
status=('The ICALP 2020 source explicitly leaves the total-function equality open. '
 'The checked August 2026 oracle-separation paper works in a partial-function setting, while recent Hamming-distance results restrict the oracle or change the resource bound. '
 'No resolution of the stated total-function equality was found in the bounded source review.')
complete(identifier,dict(
 title='Two-sided versus one-sided randomized communication',
 criterion='reductions',question_type='yes_no',
 formal=r'''For total Boolean two-party function families, is
\[
\mathrm{BPP}^{\mathrm{cc}}=\mathrm P^{\mathrm{RP}^{\mathrm{cc}}}\,?
\]
Here \(\mathrm{BPP}^{\mathrm{cc}}\) consists of families with public-coin randomized protocols using a polylogarithmic number of communicated bits and error at most \(1/3\) on every input. The class on the right consists of families computed exactly by deterministic protocols with adaptive access to ideal one-sided-error communication oracles, with polylogarithmic total charged cost as defined below.

Equivalently, does every total family \((F_n)_{n\ge1}\), where \(F_n:\{0,1\}^n\times\{0,1\}^n\to\{0,1\}\), with
\[
R_{1/3}^{\mathrm{pub}}(F_n)\le C(\log_2(n+2))^a
\]
for some fixed \(C\ge1,a\ge0\), admit deterministic oracle protocols of cost at most
\[
C'(\log_2(n+2))^b
\]
for some fixed \(C'\ge1,b\ge0\) and every \(n\)? The latter constants may depend on the family. There are no promised or undefined inputs.''',
 definitions=r'''Alice receives \(x\in\{0,1\}^n\), Bob receives \(y\in\{0,1\}^n\), and both know \(n\), the target function and their protocol. A deterministic protocol is a finite binary tree. At an internal node, the designated party sends one bit determined by that party's entire input and the public transcript. A leaf has a common output bit. Its cost is its maximum depth. Local computation, local storage and the size of the protocol description are unrestricted.

A public-coin randomized protocol is a distribution over such deterministic protocols, sampled using shared randomness independent of the inputs. Its cost is the maximum communication cost over its support, rather than an expected cost. It computes a total function \(G\) with two-sided error \(1/3\) if, on every pair \((x,y)\), its output equals \(G(x,y)\) with probability at least \(2/3\). Define \(R_{1/3}^{\mathrm{pub}}(G)\) as the least possible cost.

For a total function \(G\) on the same input domain, define \(R_{\mathrm{RP}}^{\mathrm{pub}}(G)\) using public-coin protocols that satisfy
\[
G(x,y)=0\ \Longrightarrow\ \Pr[\text{output }1]=0,\qquad
G(x,y)=1\ \Longrightarrow\ \Pr[\text{output }1]\ge\frac12 .
\]
Only false negatives are allowed. Every deterministic protocol in the support must obey the same worst-case communication bound. The constant \(1/2\) can be replaced by another fixed positive success probability using amplification. The cost is finite because exchanging both inputs computes any \(G\) exactly.

An ideal deterministic RP-oracle protocol is a finite binary tree with two permitted kinds of internal node. An ordinary communication node sends one locally determined bit and costs one. An oracle node is labelled by an arbitrary total Boolean function \(G_v(x,y)\). It reveals the exact bit \(G_v(x,y)\) to both parties and costs
\[
1+R_{\mathrm{RP}}^{\mathrm{pub}}(G_v).
\]
Its label and the next node may depend on the previous transcript and previous oracle answers. A leaf has a common output bit. The protocol must output \(F_n(x,y)\) exactly on every input, when all oracle answers are exact. Its charged cost is the maximum sum of node costs over root-to-leaf paths. In particular, the number of queries is counted and can grow polylogarithmically; it is not required to be a fixed constant.

Each \(G_v\) is defined on all \(n\)-bit input pairs, including those that never reach node \(v\). Private local transformations of an input can be included in \(G_v\), and their local computation is free. The oracle computes a joint function; it does not reveal the other party's input. Oracle answers are ideal exact answers to functions that possess one-sided-error protocols, not individual noisy samples from those protocols. Neither party has private information about an oracle's answers beyond the public returned bits.

This weighted-tree description is the communication-cost formulation of adaptive access to RP oracles: the cost of each requested computation is charged, and the extra one charges the query itself. Fixing any constant-factor variation in this charging convention gives the same polylogarithmic class. The oracle functions, ordinary protocol and public-coin distributions may depend on \(n\). There is no uniform algorithmic-generation or running-time requirement on these objects; the resource is communication.

A family belongs to either displayed class only if one fixed polynomial in \(\log_2(n+2)\) bounds its respective cost for all \(n\). The oracle class is contained in \(\mathrm{BPP}^{\mathrm{cc}}\): each test can be amplified and simulated with enough accuracy for the polylogarithmic sequence. Thus the substantive direction is the containment from two-sided randomized protocols to deterministic RP-oracle protocols.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the universal total-function containment in the formal question. A positive answer must cover every total family with polylogarithmic public-coin two-sided-error communication. A negative answer must establish a total family in \(\mathrm{BPP}^{\mathrm{cc}}\) for which no polylogarithmic charged-cost deterministic RP-oracle family exists. A separation only for partial functions, only against one particular oracle, or only for a fixed constant number of queries is insufficient. The target is a binary class equality; numerical \(1/100\) tolerance does not relax it.''',
 source_formulation=dict(text='The introduction asks whether two-sided-error communication and deterministic adaptive access to one-sided-error communication oracles have the same power for total functions.',
 caption='Paraphrase of ICALP 2020 Article 92, §1, p. 92:2; the one-sided public-coin model is defined in §2, p. 92:6.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=80,method='editorial',
 reason='The question compares the full polylogarithmic power of two-sided randomized communication with deterministic adaptive use of every one-sided randomized test, across all total functions.',
 basis='Individual assessment of a general structural randomness barrier and its links to oracle hierarchies; broader than separations for equality, fixed Hamming distance or constant numbers of queries.'),
 why='Many randomized communication algorithms use a few kinds of tests that can be wrong in only one direction. The question asks whether arbitrary two-sided randomized interaction can always be organized around such tests while retaining efficient communication. Either outcome would clarify the role of randomness in the structural hierarchy of two-party protocols.',
 references=[
 ref('primary','Nondeterministic and Randomized Boolean Hierarchies in Communication Complexity',
 'Toniann Pitassi; Morgan Shirley; Thomas Watson',2020,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.92',
 '§1 p. 92:2 total-function question; §1.1 Theorems 1–3; §2 p. 92:6 public-coin RP definition; §2.2 oracle-cost convention'),
 ref('later',r'Pseudodeterminism and \(\mathrm{MA}\ne\mathrm{NP}^{\mathrm{BPP}}\) in Communication Complexity',
 'Thomas Watson',2026,'https://arxiv.org/abs/2608.26425v1',
 'Submitted 26 August 2026, cover dated 28 August; §1 pp. 1–3, Figure 1 and §1.1; the ambient communication functions are partial'),
 ref('hamming','Constant-Cost Communication is not Reducible to k-Hamming Distance',
 'Yuting Fang; Mika Göös; Nathaniel Harms; Pooya Hatami',2025,
 'https://arxiv.org/abs/2407.20204v2',
 'Version 2, 6 May 2025; abstract, constant-cost separation from the specific fixed-Hamming-distance oracle family'),
 ],
 context_blocks=[
 block('Equality admits a very short public-coin fingerprinting protocol. The source explains that this particular oracle does not account for every efficient randomized communication problem. Enlarging the oracle class to all RP functions leads to the target here.'),
 block('An ideal oracle answer is exact even though the function is characterized by a one-sided-error protocol. Treating every oracle call as a fresh unamplified random answer would change the deterministic oracle model.'),
 block('The source proves that allowing successively more constant numbers of queries gives a strict hierarchy. This does not rule out a simulation using a growing polylogarithmic number of queries.'),
 block('Totality is a substantive restriction. The source distinguishes this open equality from known separations that use input promises.'),
 block('The August 2026 preprint studies stronger oracle and pseudodeterministic distinctions with partial functions. Its stated separation involving deterministic RP-oracle access therefore does not settle the all-total-input formulation.','later'),
 block('The 2025 Hamming-distance separation rules out a specific family of constant-cost oracle simulations. It does not exclude polylogarithmic adaptive access to arbitrary RP functions.','hamming'),
 ],
 progress=[
 progress('2020','The ICALP paper states the total-function equality as open and separates every fixed level of the randomized Boolean hierarchy.'),
 progress('2025-05-06','The revised Hamming-distance paper gives a separation for constant-cost reductions to those specific oracles.','hamming'),
 progress('2026-08-26','A new preprint separates further communication classes in an ambient partial-function setting.','later'),
 progress('2026-09-16','The review fixes totality, public randomness, adaptive exact oracle answers and polylogarithmic cost; no resolution of this target is found.'),
 ],
),notes,sources,status,summary=[
 'Two parties want to compute a total Boolean function using little communication.',
 'The question asks whether every efficient two-sided randomized protocol can be replaced by deterministic adaptive queries to one-sided randomized tests.',
 'Oracle answers are exact, and each query is charged the communication needed by its one-sided-error protocol.',
 'The total communication and query cost may grow polynomially in the logarithm of the input length.',
 'Known constant-query hierarchy separations and partial-function results do not resolve this total-function equality.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
