"""Review the single-output nonnegative min-plus cubic lower-bound target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0481';claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained exact single-pair shortest-path evaluation on complete undirected graphs with arbitrary finite nonnegative real weights.',
 'Rewrote malformed mathematical notation and specified binary min/plus gates, unrestricted reuse and depth, optional zero/infinity constants, and nonuniform topology.',
 'Distinguished numerical equality on the nonnegative domain from producing exactly the formal path polynomial and from correctness on negative weights.',
 'Kept the full cubic lower-bound conjecture and its exact infinitely-often negation, without substituting an arbitrary improvement milestone.',
 'Re-read the 2025 seminar and 2015 conclusion, and checked the current author supplement; its linked problem is explicitly single-source with multiple outputs, so it is cited only as related context.',
 'Preserved importance, removed proof-sketch-style recurrence detail from context and required a complete Lean-checked answer.',
]
sources=[
 'Read Koutris, Circuit Size for Reachability, §4.1 of Semirings in Databases, Automata, and Logic, Dagstuhl Seminar 25081, DOI 10.4230/DagRep.15.2.89, printed p.105. It asks about the circuit for all simple 1-to-n paths in complete undirected K_n, interpreted over absorptive semirings; it records O(n^3) upper and Omega(n^2) lower bounds and explicitly says the matching lower bound is open even for the tropical case.',
 'Read Jukna, Lower Bounds for Tropical Circuits and Dynamic Programs, author manuscript corresponding to Theory of Computing Systems 57(1), 160–194 (2015), DOI 10.1007/s00224-014-9574-4: the Min model and polynomial conventions, Theorem 13, and Section 14 Conclusion, author-PDF p.28. The conclusion explicitly asks for a cubic Min lower bound for STCON and/or CONN and separates it from the all-pairs result. Negative-weight Min-minus and formal polynomial-production statements are different models.',
 'Fetched Jukna’s Supplements to Tropical Circuit Complexity and the linked problem-setA2.html on 17 September 2026. The index still describes the shortest-path optimality question as open. The linked page explicitly defines single-source output to all n-1 other vertices, unlike the one-output target here; it gives the all-pairs lower bound as related background. This narrower card is grounded directly in the 2025 seminar and 2015 conclusion, not in an incorrect relabeling of that linked problem.',
 'Bounded primary-source searches through 17 September 2026 found no verified resolution of this exact nonnegative-weight, single-output, unrestricted min-plus circuit question. Shortest-path algorithms with branching, all-pairs lower bounds, fixed-walk-length bounds and branching-program restrictions were not substituted.',
]
complete(identifier,dict(
 formal=r'''For \(n\ge2\), let \(K_n\) be the complete undirected graph on vertices \(1,\ldots,n\), with an arbitrary finite nonnegative real weight \(x_{ij}=x_{ji}\) on each edge \(\{i,j\}\). Let
\[
f_n(x)=\min_{P:\,1\leadsto n\text{ a simple path}}\sum_{e\in P}x_e.
\]
Write \(s(n)\) for the smallest number of binary gates in a circuit using only \(\min\) and addition, with optional constants \(0,+\infty\), that outputs \(f_n(x)\) exactly for every such weight assignment. Do there exist constants \(c>0\) and an integer \(n_0\ge2\) such that
\[
\forall n\ge n_0:\quad s(n)\ge c n^3?
\]
There is one output, with unrestricted circuit depth and reuse of intermediate values.''',
 definitions=r'''A simple path from 1 to \(n\) is a vertex sequence \((v_0,\ldots,v_t)\) of distinct vertices with \(v_0=1\), \(v_t=n\) and \(1\le t\le n-1\). Its weight is \(\sum_{a=0}^{t-1}x_{v_a v_{a+1}}\). Every pair of different vertices is an edge of \(K_n\), so the family of paths is finite and nonempty. In particular, \(f_n(x)\) is finite. Zero weights are permitted. There are \(\binom n2\) independent edge inputs, not separate variables for the two directions of an edge.

A circuit is a finite directed acyclic graph. Its input nodes are the variables \(x_{ij}\), \(1\le i<j\le n\), and optional constant sources \(0\) and \(+\infty\). Each operation gate has two incoming arguments and returns either their numerical minimum or their sum. Computation is in \([0,+\infty]\), with \(\min(a,+\infty)=a\) and \(a+(+\infty)=+\infty\). One designated node is the output. Size counts operation gates; input nodes, constant sources, wires and repeated use of a computed value are free. Fan-out and depth are unbounded.

The topology may depend on \(n\) but cannot depend on the numerical weights. No uniform procedure for generating the circuit descriptions is required. There are no other arithmetic operations, negative constants, Boolean comparison outputs, conditional gates, input-dependent routing, or addressable memory. A minimum gate returns a number; it does not expose which argument attained that number for use as a control bit. Arbitrary real weights are evaluated exactly by the specified operations; the resource measure is gate count, not finite-precision bit time.

Correctness means equality with \(f_n\) as a function on the whole nonnegative real input domain. It does not require that a formal expansion contain exactly one monomial for each simple path or exclude additional terms that never lower the numerical value on this domain. Requiring formal polynomial production, or correctness also for negative weights, would strengthen the model’s obligations and is not imposed. Only the distance from 1 to \(n\) is output, not an attaining path, all distances from 1, or all-pairs distances.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed cubic lower bound or its logical negation. A positive proof must apply to every correct circuit in the stated nonuniform model and use one positive constant \(c\) for every sufficiently large \(n\).

The negation is
\[
\forall c>0\;\forall n_0\ge2\;\exists n\ge n_0:\ s(n)<cn^3.
\]
A correct \(o(n^3)\)-size family at all sufficiently large lengths would suffice, but the negation does not require that stronger all-length upper bound. A lower bound for multiple outputs, negative weights, formulas, branching programs or formal polynomial production does not establish the selected claim without a valid transfer. An algorithm with weight-dependent control flow is not automatically a circuit of comparable size. No numerical approximation tolerance or additional unproved assumption is allowed.''',
 source_formulation=dict(text='The seminar asks whether the cubic upper bound is optimal for a circuit representing the sum over simple 1-to-n paths in complete undirected graphs. It expressly leaves the matching lower bound open for the tropical semiring.',caption='Koutris, Dagstuhl Seminar 25081, §4.1, printed p.105. The card retains the selected nonnegative min-plus instance and one numerical output.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Semirings in Databases, Automata, and Logic — Circuit Size for Reachability','Paris Koutris (problem contributor)',2025,'https://doi.org/10.4230/DagRep.15.2.89','Dagstuhl Seminar 25081, §4.1, printed p.105; complete undirected graph and simple 1-to-n paths'),
 ref('paper','Lower Bounds for Tropical Circuits and Dynamic Programs','Stasys Jukna',2015,'https://web.vu.lt/mif/s.jukna/ftp/tropical-manuscript.pdf','Min model, Theorem 13 and §14 Conclusion, author-PDF p.28; journal DOI 10.1007/s00224-014-9574-4'),
 ref('related','Is Bellman-Ford-Moore single source shortest paths (min,+) circuit optimal?','Stasys Jukna',2023,'https://web.vu.lt/mif/s.jukna/tropical/problem-setA2.html','Book supplement, accessed 17 September 2026; related single-source and all-pairs problems, not the exact single-output formulation'),
 ],
 context_blocks=[
 block('The numerical task asks for just one shortest-path distance. The restricted computational model is a fixed network of minimum and addition operations, so ordinary graph algorithms with data-dependent choices need not give circuits of comparable size.'),
 block(r'The checked source records an \(O(n^3)\) construction and only the elementary \(\Omega(n^2)\) input-dependence lower bound. Closing that gap is the selected conjecture.'),
 block('Tropical circuits can compute the correct numerical function without reproducing its exact formal polynomial expansion. This distinction matters for path families containing different lengths and is part of the source’s lower-bound discussion.','paper'),
 block('The cubic all-pairs lower bound uses the requirement to produce many distances. The author’s related single-source problem still requests several outputs. Neither statement may simply be relabeled as a lower bound for the one output here.','related'),
 ],
 progress=[progress('2015','The paper’s conclusion explicitly leaves a cubic nonnegative min-plus lower bound for the path/connectivity polynomials open.','paper'),progress('2025','The seminar restates the simple 1-to-n path question and the quadratic-versus-cubic gap.'),progress('2026-09-17','The checked author supplements continue to discuss related shortest-path optimality questions; their single-source and all-pairs outputs are distinguished.','related')],
),notes,sources,'The exact single-output nonnegative min-plus question is explicitly open in the 2025 seminar and consistent with the 2015 conclusion. Bounded primary-source searches through 17 September 2026 found no verified resolution. The author’s current linked single-source question has multiple outputs and is cited only as related evidence, not as the same formulation.',summary=[
 'The input gives nonnegative real weights on every edge of a complete undirected graph.',
 'A fixed circuit of minimum and addition gates must compute the exact distance between two designated vertices.',
 'The question is whether every such single-output circuit requires a cubic number of gates.',
 'The source records cubic upper and quadratic lower bounds; all-pairs and single-source results have different output requirements.',
 'A complete Lean-checked proof of the cubic lower bound or its exact logical negation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
