"""Apply the user-selected full bandwidth-sensitive clique-detection target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6206'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user choice to determine optimal rounds as a function of n, clique size ell and bandwidth b, within absolute constant factors.',
 'Retained existential detection with constant joint success probability from the 2018 conference source; did not replace it by listing, local membership or global dissemination.',
 'Fixed ordinary edge-specific CONGEST messages, initial neighbor identifiers, private randomness, finite uniform local computation and worst-case round cost.',
 'Defined the optimization over algorithms correct on the full parameter domain, and required constants uniform in all three parameters.',
 'Separated the resolved historical linear-round threshold for fixed clique sizes from the sharper selected classification, and listing lower bounds from detection lower bounds.',
 'The user-selected bandwidth-sensitive classification is an editorial continuation of the source question, not a verbatim claim that the 2018 source asked for this entire constant-factor formula.',
]
sources=[
 'Read Czumaj–Konrad, DISC 2018 Article 16, §§1–1.2 pp. 16:1–16:4 and Theorem 5. The conference detection convention uses success at least 2/3; the open paragraph compares the square-root lower bound with the then-linear upper bound.',
 'Read Censor-Hillel–Chang–Le Gall–Leitersdorf, arXiv:2011.07405v1 (14 November 2020), abstract, §1.2 Theorem 1.1 and §1.4; checked the SODA 2021 publication DOI. The tightness statement concerns listing; detection tightness up to logarithms is specifically noted for K4.',
 'Checked the later journal version of Detecting Cliques in CONGEST Networks, DOI 10.1007/s00446-019-00368-w. Its high-probability definition is not silently substituted for the selected conference constant-success convention.',
 'Bounded primary-source searches through 16 September 2026 found no constant-factor characterization uniform in n, ell and b for the selected detection model. Results for congested clique, broadcast messages and clique listing were excluded as direct resolutions.',
]
status=('The historical possibility of sublinear rounds is settled positively for every fixed clique size at standard logarithmic bandwidth. '
 'The user instead selected a constant-factor characterization of detection complexity throughout the stated three-parameter domain. '
 'The checked tight listing theorem does not supply that characterization: its general listing lower bound is not a detection lower bound, and even its K4 comparison hides polylogarithmic factors. '
 'No resolution of the selected full target was found in this bounded review.')
complete(identifier,dict(
 title='Optimal clique-detection rounds in CONGEST',
 criterion='resources',question_type='asymptotic_complexity',
 formal=r'''Determine the optimal randomized round complexity
\[
T_{\mathrm{det}}(n,\ell,b)
\]
of detecting an \(\ell\)-vertex clique in an \(n\)-vertex communication graph, when each directed use of an edge can carry \(b\) bits per round. The parameter domain is
\[
n\ge16,\qquad 4\le\ell\le\lfloor\sqrt n\rfloor,\qquad b\ge1,
\]
with all three parameters integers.

The requested answer is an explicit asymptotic expression \(F(n,\ell,b)>0\) and absolute constants \(c,C>0\) such that, throughout this domain,
\[
cF(n,\ell,b)\le T_{\mathrm{det}}(n,\ell,b)
                 \le CF(n,\ell,b).
\]
The constants may not depend on \(n,\ell,b\). Polylogarithmic uncertainty is not sufficient. This full constant-factor target, rather than the historical question of whether a linear number of rounds is necessary, is the explicit user choice.''',
 definitions=r'''The input is any finite simple undirected graph \(G=(V,E)\) with \(|V|=n\); it need not be connected. A clique of size \(\ell\) is a set of \(\ell\) distinct vertices every two of which are adjacent. The communication links are exactly the edges of \(G\), with communication possible in both directions. Nodes have distinct identifiers in \(\{1,\ldots,n^3\}\), under an arbitrary assignment. Initially a node knows \(n,\ell,b\), its own identifier and the identifiers of all its neighbors, but no other edges. There is no instance-dependent advice or free preprocessing.

In a synchronous round, each node performs arbitrary finite local computation and sends one \(b\)-bit word to each neighbor, possibly a different word on every incident edge. Padding permits shorter content; there is no additional uncharged message channel. All of these words arrive at the end of the round, so a word sent in that round cannot depend on a word received in the same round. Nodes use independent private random bits. Local memory, computation and random-bit generation are uncharged, but each local phase terminates. The algorithm is one finite effective program that operates for every valid \(n,\ell,b\) and every identifier assignment.

At termination each node outputs one bit. On each input, with probability at least \(2/3\), the disjunction of all output bits equals the indicator that \(G\) contains an \(\ell\)-clique. Equivalently, a clique-containing graph must cause at least one node to output one, and a clique-free graph must cause all nodes to output zero, each with the stated joint probability. Either kind of error is allowed outside the successful event. The node outputting one need not belong to a clique or output its vertices. Nodes are not required to enumerate cliques, decide their own membership in a clique, or all learn the answer.

For an admissible algorithm \(A\), let \(r_A(n,\ell,b)\) be the least nonnegative integer bounding its number of rounds on every \(n\)-vertex graph, every identifier assignment and every random execution for those parameters; put \(r_A=\infty\) when no such finite bound exists. Define
\[
T_{\mathrm{det}}(n,\ell,b)=\inf_A r_A(n,\ell,b),
\]
where the infimum ranges over all uniform algorithms satisfying the correctness requirement on the entire parameter domain. Cost is thus worst-case bounded rounds, not expected rounds. The infimum is pointwise in the displayed parameters; admissibility never permits an algorithm that is correct only for a selected graph or parameter tuple.

The bandwidth \(b\) is an explicit positive integer, including values outside the usual \(b=\Theta(\log n)\) specialization. Both directions of an edge have their own \(b\)-bit capacity in each round. This is ordinary CONGEST, with different messages permitted for different neighbors. There are no direct links between nonneighbors. An explicit expression for \(F\) must characterize the dependence on the three integers; merely renaming the optimization defining \(T_{\mathrm{det}}\) is not an answer.''',
 answer_criterion=r'''Give a complete Lean-checked proof of matching upper and lower bounds within absolute constant factors for the entire specified parameter domain. The upper bound must be realized in the stated detection model, and the lower bound must apply to every admissible randomized algorithm. A bound only for listing all cliques, for broadcast communication, for fixed \(\ell\) with constants depending on \(\ell\), or only at logarithmic bandwidth does not by itself determine the requested function. The selected acceptance tolerance is multiplicative by absolute constants; additive \(1/100\) error is not the criterion for this asymptotic resource function.''',
 source_formulation=dict(
 text='The source leaves a gap between its bandwidth-dependent square-root lower bound for clique detection and the linear-round algorithm then known, and asks how much communication detecting cliques actually requires.',
 caption='Paraphrase of §1.2, p. 16:4. The user selected the stronger full constant-factor complexity question after later sublinear algorithms were checked.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=83,method='editorial',
 reason='Clique detection is a central distributed subgraph problem whose optimal communication cost remains distinct from the better-understood task of listing all cliques.',
 basis='Individual assessment of the basic graph primitive, the open detection-versus-listing gap and the demanding uniform dependence on clique size and edge bandwidth.'),
 why='A network can contain a dense local pattern without any one processor initially knowing all of its edges. The question measures how much communication is intrinsically needed merely to detect that pattern. Resolving the full parameter dependence would distinguish the cost of establishing existence from the cost of enumerating every occurrence.',
 references=[
 ref('primary','Detecting Cliques in CONGEST Networks',
 'Artur Czumaj; Christian Konrad',2018,'https://doi.org/10.4230/LIPIcs.DISC.2018.16',
 'DISC 2018, Article 16; §§1–1.2 pp. 16:1–16:4 and Theorem 5; constant-success conference formulation'),
 ref('listing','Tight Distributed Listing of Cliques',
 'Keren Censor-Hillel; Yi-Jun Chang; François Le Gall; Dean Leitersdorf',2021,
 'https://doi.org/10.1137/1.9781611976465.171',
 'SODA 2021, pp. 2878–2891; Theorem 1.1; checked author preprint arXiv:2011.07405v1, 14 November 2020, abstract, §§1.2 and 1.4'),
 ref('journal','Detecting cliques in CONGEST networks',
 'Artur Czumaj; Christian Konrad',2020,'https://doi.org/10.1007/s00446-019-00368-w',
 'Distributed Computing 33, pp. 533–543; published online 21 December 2019; later model convention and lower-bound statement'),
 ],
 context_blocks=[
 block(r'The conference source proves a lower bound of \(\Omega(\sqrt n/b)\) in the range \(4\le\ell=O(\sqrt n)\), and a corresponding \(n/(\ell b)\) scale for larger cliques. At standard logarithmic bandwidth, it compares this with a linear-round upper bound.'),
 block('The source also establishes a limitation of its two-party vertex-partition method for obtaining stronger clique lower bounds. That is a statement about the scope of the proof method, not an algorithm attaining the lower bound in a distributed network.'),
 block(r'The SODA 2021 result lists all \(\ell\)-cliques in \(\widetilde O(n^{1-2/\ell})\) rounds for each fixed \(\ell\ge4\), at standard logarithmic bandwidth. It therefore also gives sublinear detection for every fixed clique size. The tilde hides polylogarithmic factors.','listing'),
 block(r'For \(\ell=4\), that upper bound matches the known detection lower bound up to polylogarithmic factors. This does not establish a constant-factor formula even for this specialization.','listing'),
 block('For larger cliques, the paper’s matching general lower bound concerns listing, which requires reporting every occurrence. It cannot be transferred to existential detection merely because listing implies detection. Constants or other losses in a fixed-clique-size statement also cannot silently be taken as uniform when clique size grows.','listing'),
 block('The later journal presentation uses a high-probability detection convention. This card explicitly retains the constant-success convention of the original conference question and treats its full bandwidth dependence as the selected editorial continuation.','journal'),
 ],
 progress=[
 progress('2018','The source proves the bandwidth-dependent detection lower bound and states the remaining gap.'),
 progress('2020-11-14','The clique-listing preprint announces the fixed-size upper bounds and the K4 detection comparison.','listing'),
 progress('2021','The listing result appears at SODA, settling sublinear detectability for each fixed clique size at standard bandwidth.','listing'),
 progress('2026-09-16','The user selects the full optimal-rounds function within absolute constant factors; the review fixes detection, probability, initial-information and bandwidth conventions.'),
 ],
),notes,sources,status,summary=[
 'The input graph is also the communication network, and each edge carries at most b bits in each direction per round.',
 'The task is for some processor to report that a clique of the requested size exists, with joint success probability at least two thirds.',
 'The selected question asks for the optimal number of rounds as a function of graph size, clique size and bandwidth, within absolute constant factors.',
 'Known clique-listing algorithms already give sublinear detection for every fixed clique size at logarithmic bandwidth.',
 'Their tightness for listing does not settle the full detection function, and even the known four-clique comparison retains polylogarithmic uncertainty.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
