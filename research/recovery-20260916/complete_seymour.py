"""Complete the exact second-neighborhood target, preserving the claim conflict."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7253'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved all finite nonempty oriented graphs and explicitly excluded loops and opposite arcs.',
 'Defined the second neighborhood by shortest directed distance exactly two, excluding first neighbors even if a two-step walk also reaches them.',
 'Required a complete Lean-checked universal proof or counterexample failing at every vertex, without numerical relaxation or an algorithmic time bound.',
 'Retained uncertain status for the unverified complete-proof claim, with exact arXiv version and submission dates distinguished from manuscript dates.',
 'Read the July 2026 revision’s refutation of its own stronger matching conjecture, separating that counterexample from the original cardinality conjecture.',
 'Added the precisely scoped Huang–Peng general constant-factor bound and preserved the individually assessed importance 94.',
]
sources=[
 'Read Bai–Li–Park, arXiv:2607.18047v2 (24 July 2026; manuscript date 27 July), abstract and §1 pp. 1–3, exact neighborhood definitions, Conjectures 1.1–1.3, Theorems 1.4–1.5 and Corollary 1.6; read the §3 description of the 36-vertex counterexample to the stronger matching conjectures. The paper explicitly retains the original second-neighborhood conjecture.',
 'Read Huang–Peng, arXiv:2412.20234v1 (28 December 2024), abstract and §1 pp. 1–2, shortest-distance definitions and Theorem 1.3. Its factor gamma is the unique root in [0,1] of 8x^5+4x^4-12x^3-7x^2+2x+4, approximately 0.715538; this is below the target factor one.',
 'Read Glover, arXiv:2501.00614v14 (30 May 2026; manuscript dated 2 June), abstract, introductory claim and Conjecture 1.1, concluding algorithm-complexity statement and conclusion. The manuscript claims a full proof and a linear-time algorithm. Its complete dependency chain was not verified or refuted; no Lean proof or independent validation of the full claim was established by this review.',
 f'Checked arXiv version histories and bounded primary-source searches through {DATE}. Later restricted-class papers and the July specialist preprint still distinguish the general assertion from partial results. No verified resolution of the conflicting full-proof claim was found. Secondary summaries were not treated as proof acceptance.',
]
status='The full-proof claim remains unverified in this review: Glover’s version 14, posted 30 May 2026, claims the entire conjecture, whereas Bai–Li–Park’s version 2, posted 24 July 2026, explicitly retains it as open. The latter paper refutes a stronger matching assertion, not the original cardinality inequality. The card therefore keeps uncertain status rather than certifying either a resolution or conclusive current openness.'
complete(identifier,dict(
 status='uncertain',criterion='decision',question_type='yes_no',
 formal=r'''Does every finite nonempty oriented graph \(D=(V,A)\) contain a vertex \(v\) whose second out-neighborhood is at least as large as its first out-neighborhood?
\[
\forall D\ \exists v\in V,\qquad
|N_D^{++}(v)|\ge |N_D^+(v)|.
\]
Here \(N_D^+(v)\) contains vertices at directed distance one from \(v\), and \(N_D^{++}(v)\) contains vertices at directed distance exactly two, as defined below.''',
 definitions=r'''An oriented graph consists of a finite vertex set \(V\) and an arc set \(A\subseteq V\times V\) such that \((v,v)\notin A\) for every vertex and, for distinct \(u,v\), at most one of \((u,v)\) and \((v,u)\) belongs to \(A\). There are no loops, opposite arc pairs or parallel arc copies. Some unordered pairs may have no arc in either direction. The vertex set must be nonempty.

A directed path of length \(r\) follows \(r\) arcs in their prescribed directions. The directed distance from \(v\) to \(w\) is the smallest length of such a path, with distance zero from \(v\) to itself and \(+\infty\) when no path exists.

The first and second out-neighborhoods are explicitly
\[
N_D^+(v)=\{u\in V:(v,u)\in A\}
\]
and
\[
N_D^{++}(v)=
\{w\in V\setminus(N_D^+(v)\cup\{v\}):
\exists u\in V,\ (v,u)\in A\ \text{and}\ (u,w)\in A\}.
\]
Thus a first out-neighbor is excluded from the second out-neighborhood even if it is also the endpoint of a directed two-arc path from \(v\). Each vertex is counted once, regardless of how many paths reach it. Neither incoming neighbors nor the number of outgoing arcs from an entire neighborhood is the requested quantity.

The outdegree of \(v\) is \(|N_D^+(v)|\). A sink has outdegree zero, so both out-neighborhoods are empty and it satisfies the conjectured inequality. Isolated vertices are allowed. There is no positive minimum-outdegree promise, no connectedness requirement and no planarity or density restriction. Graphs of every finite positive order are included.

The conclusion asks for at least one suitable vertex, which may depend on the whole graph. It does not require every vertex, a minimum-outdegree vertex or a positive fraction of vertices to satisfy the inequality. It also does not require a matching from the first neighborhood into the second; that is a stronger property.

This is an exact universal existence proposition with no running-time requirement for finding the vertex. The cardinality threshold is one: a theorem with a fixed factor smaller than one is a partial result. Absolute \(1/100\) approximation of a numerical target does not relax this Boolean assertion.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the universal statement, or supply a finite nonempty oriented graph together with complete Lean-checked proofs that it satisfies the arc restrictions and that
\[
\forall v\in V,\qquad |N_D^{++}(v)|<|N_D^+(v)|.
\]
Failure at only some vertices does not refute the conjecture. A graph with a loop or an opposite arc pair is outside the domain. A restricted graph-class theorem, a factor strictly below one, a finite-size check or a counterexample to a stronger neighborhood-matching property does not settle this exact target.''',
 source_formulation=dict(
 text='Conjecture 1.1 asks whether every oriented graph contains a vertex with second outdegree at least its outdegree. The source explicitly defines the second neighborhood by removing the vertex itself and all of its first out-neighbors from the endpoints of two-arc paths.',
 caption='Paraphrase of Bai–Li–Park, §1 pp. 1–2, neighborhood definition and Conjecture 1.1; the card makes the nonempty finite domain explicit.',
 citation='primary',format='editorial_paraphrase'),
 why='The conjecture predicts a universal local expansion phenomenon even in sparse directed graphs with no connectivity assumptions. Its statement involves only two steps of reachability, but a proof must find a favorable vertex in every orientation without opposite arcs. It is a central structural question about how directed degree constraints force neighborhood growth.',
 references=[
 ref('primary','Towards a strengthening of the second neighborhood conjecture',
  'Yandong Bai; Binlong Li; Boram Park',2026,'https://arxiv.org/abs/2607.18047v2',
  'Version 2, posted 24 July 2026; manuscript dated 27 July; §1 pp. 1–3, Conjectures 1.1–1.3, Theorems 1.4–1.5 and Corollary 1.6; §3 counterexample to the stronger assertions'),
 ref('bound','An improved bound on Seymour’s second neighborhood conjecture',
  'Hao Huang; Fei Peng',2024,'https://arxiv.org/abs/2412.20234v1',
  'Version 1, 28 December 2024; §1 pp. 1–2, distance conventions and Theorem 1.3'),
 ref('claim','A Minimum Counterexample Proof of the Seymour Second Neighborhood Conjecture via the Graph Level Order',
  'Charles N. Glover',2026,'https://arxiv.org/abs/2501.00614v14',
  'Version 14, posted 30 May 2026; manuscript dated 2 June; abstract, §1 Conjecture 1.1 and complete-proof claim, §5 Theorem 5.3 and §6 conclusion. Full claimed proof not independently verified or refuted'),
 ],
 context_blocks=[
 block('The first neighborhood measures one-step reach. The second counts new vertices reachable in two steps, excluding all first neighbors. Opposite arcs are excluded: a directed two-cycle would otherwise violate the assertion at both vertices.'),
 block('The tournament case, in which every pair has exactly one directed arc, is known. The general statement also allows missing adjacencies, so that special case does not settle it.'),
 block(r'Huang and Peng prove a general bound \(|N^{++}(v)|\ge\gamma|N^+(v)|\), where \(\gamma\approx0.715538\) is the unique root in \([0,1]\) of \(8x^5+4x^4-12x^3-7x^2+2x+4=0\). The conjecture requires the larger factor one.','bound'),
 block('Bai, Li and Park study a stronger condition: distinct first neighbors can be matched along arcs to distinct second neighbors. Their revised paper gives a 36-vertex counterexample to that stronger assertion, including a tournament version, while retaining the original inequality as open.'),
 block('Glover’s May 2026 version claims a complete proof and a linear-time search algorithm. This review has not verified or refuted that proof. The later specialist source’s open-problem statement creates a claim conflict that is recorded through uncertain status.','claim'),
 ],
 progress=[
 progress('2024-12-28','The general constant-factor bound improves to approximately 0.715538.','bound'),
 progress('2026-05-30','Version 14 of the separate manuscript claims the full conjecture; the claim remains unverified here.','claim'),
 progress('2026-07-24','The revised specialist preprint retains the original conjecture and reports a counterexample to its stronger matching formulation.'),
 progress(DATE,'The review fixes exact second-neighborhood semantics and retains uncertain status for the unresolved verification of the full-proof claim.'),
 ],
),notes,sources,status,summary=[
 'An oriented graph has directed edges but no loops or pair of opposite edges.',
 'Seymour’s conjecture asks for a vertex with at least as many new vertices reachable in two steps as vertices reachable in one step.',
 'A vertex already in the first neighborhood is excluded from the second even if a two-step path also reaches it.',
 'Known general constant-factor bounds and restricted-class results do not reach the exact universal inequality.',
 'A separate manuscript claims a full proof, but the later specialist literature retains the question; the card records that unverified claim conflict as uncertain.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
