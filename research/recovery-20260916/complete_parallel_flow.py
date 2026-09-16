"""Individual review of the disjunctive parallel approximate-flow question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4763'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the source’s disjunction: an algorithm for at least one of the two complete problem classes is sufficient.',
 'Recovered the single-commodity, undirected, budgeted-throughput interpretation of minimum-cost flow from the source introduction.',
 'Defined fractional flows, exact capacities and budget feasibility, explicit output, vertex endpoint conventions and approximation of the maximum value.',
 'Expanded polynomially bounded integer data and inverse-polylogarithmic accuracy into quantified input regimes, rather than requiring an unstated fully polynomial dependence on accuracy.',
 'Made a uniform randomized word-PRAM convention explicit; its polylogarithmic overhead is absorbed in the requested resource bounds.',
 'Assessed importance individually and separated published general-graph subpolynomial depth from the restricted 2026 expander result.',
]
sources=[
 'Read FOCS 2025 pp. 1886–1887, Theorem 1 and the budgeted-flow definition, and §III, Open Problem 1, p. 1894.',
 'Read arXiv:2510.20456v1 (23 October 2025), §3.1, pp. 15–16, and Definitions 7.1–7.2, Theorem 7.3 and Remark 7.4, pp. 58–59: explicit edge output, exact capacity/budget feasibility and randomized correctness.',
 'Checked the primary SODA 2024 abstract, arXiv:2402.14950v1: near-linear-work/polylog-depth undirected edge-capacitated maximum flow, not vertex capacities or cost budgets.',
 'Read Kyng–Sulser, ICALP 2026 Article 136, abstract and §1 questions Q1–Q3: unit-capacity/unit-length expanders and a bicriteria congestion/cost guarantee, not a general-graph resolution.',
 'Checked arXiv:2503.13274, SPAA 2025, on exact min-cost flow: square-root depth does not meet the target. The 2025/2026 small vertex-connectivity result, arXiv:2504.06033, is not general capacitated s-t flow.',
 'Bounded primary-source review through 16 September 2026 found no resolution of either alternative. The cited algorithmic proofs were not independently reconstructed.',
]
status=('FOCS 2025 explicitly leaves nearly-linear work with polylogarithmic depth open for either alternative. '
 'The source’s general algorithm has subpolynomial overhead instead. The 2026 ICALP result concerns unit-data expanders with a bicriteria guarantee; it does not settle the general graph question. '
 'No matching resolution was found in the bounded review through 16 September 2026.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does at least one of the following two problems admit a uniform randomized parallel algorithm with nearly-linear work and polylogarithmic depth, in the precise regime below?

1. Edge-capacitated budgeted minimum-cost flow: given an undirected graph, terminals \(s,t\), edge capacities and nonnegative edge costs, and a total cost budget \(B\), output a feasible \(s\)-to-\(t\) flow whose value is at least \(\mathrm{OPT}/(1+\varepsilon)\), where \(\mathrm{OPT}\) is the largest flow value within both the capacities and budget.
2. Vertex-capacitated maximum flow: given an undirected graph, terminals \(s,t\), and vertex capacities, output a feasible \(s\)-to-\(t\) flow whose value is at least \(\mathrm{OPT}/(1+\varepsilon)\), where \(\mathrm{OPT}\) is the largest capacity-respecting value.

The assertion is a disjunction over the two entire problem classes. The algorithm may choose one class once and for all; choosing an easier alternative separately for each instance is not the assertion.''',
 definitions=r'''An input graph \(G=(V,E)\) is finite, simple and undirected, with \(V=\{1,\ldots,n\}\), \(n\ge2\), \(m=|E|\), and distinct named terminals \(s,t\). It is supplied by an explicit edge list; disconnected graphs and zero capacities are allowed. For each undirected edge \(\{u,v\}\), a flow has nonnegative values \(f_{uv},f_{vu}\). Put
\[
\mathrm{out}_f(v)=\sum_{w:\{v,w\}\in E}f_{vw},\qquad
\mathrm{in}_f(v)=\sum_{w:\{v,w\}\in E}f_{wv}.
\]
Require \(\mathrm{in}_f(s)=\mathrm{out}_f(t)=0\) and \(\mathrm{in}_f(v)=\mathrm{out}_f(v)\) for \(v\notin\{s,t\}\). The value is \(F=\mathrm{out}_f(s)=\mathrm{in}_f(t)\). Fractional flows are allowed. Internal circulations may occur but consume the same capacities and costs as other flow.

For the edge problem, each edge \(e=\{u,v\}\) has capacity \(u_e\ge0\) and cost \(c_e\ge0\). Feasibility requires
\[
f_{uv}+f_{vu}\le u_e,\qquad
\sum_{\{u,v\}\in E}c_{\{u,v\}}(f_{uv}+f_{vu})\le B.
\]
There are no vertex constraints in this alternative. The source calls maximization under this cost budget approximate minimum-cost flow; the card uses that source convention.

For the vertex problem, each \(v\) has capacity \(U_v\ge0\). Its load is \(\mathrm{out}_f(v)\) if \(v\ne t\), and \(\mathrm{in}_f(t)\) if \(v=t\). Require load at most \(U_v\) for every vertex, including both terminals. There are no edge capacities or cost objective in this alternative. Equivalently, in a decomposition into directed simple terminal paths, every unit uses capacity at each vertex on its path, including its endpoints; removable internal circulations do not improve the optimum.

In each alternative \(\mathrm{OPT}\) is the maximum \(F\) over feasible real flows. Zero flow is feasible, and instances with \(\mathrm{OPT}=0\) must also be handled. The output explicitly lists rational values for both orientations of every edge. On a successful run all feasibility inequalities hold exactly and \(F\ge\mathrm{OPT}/(1+\varepsilon)\); no capacity or budget violation is permitted.

Here is an explicit polynomial-data and inverse-polylogarithmic-accuracy convention. For every fixed integer \(a\ge1\), allow integral capacities and costs in \([0,n^a]\), and a budget \(B=b/d\) with integers \(0\le b\le n^a\), \(1\le d\le n^a\). Let
\[
L=\lceil\log_2(n+2)\rceil,\qquad
\varepsilon=1/q,\quad q\in\mathbb N,\quad 2\le q\le L^a.
\]
Input numbers, labels and \(q\) are encoded in binary. The same algorithm must cover every fixed \(a\); it receives the numerical instance and \(q\), not advice or a precomputed structure for the graph. Reciprocal-integer accuracies specify the source's inverse-polylogarithmic regime: intermediate accuracies can be met by requesting a smaller reciprocal accuracy. This does not require a fully polynomial bound for arbitrary inverse accuracy outside that regime.

Use a synchronous priority-CRCW word PRAM: processors execute one fixed finite program, have labelled shared-memory words, can read concurrently, and simultaneous writes to one location retain the value of the lowest-numbered writing processor. A step performs word arithmetic, comparison, a Boolean operation, a shift, a shared-memory access, or generation of one independent fair random bit. A word has \(C_a L\) bits for a fixed constant \(C_a\); larger integers and rational numerators or denominators use multiple words and their operations are charged accordingly. There is no exact-real or arbitrary-precision unit-cost primitive. Work counts all processor operations, including input handling and output; depth is the number of synchronous steps. The algorithm must halt within the stated bounds on every random tape and succeed with probability at least \(2/3\) on each valid input.

Nearly-linear work and polylogarithmic depth mean that, for every fixed \(a\), there are constants \(K_a>0\) and \(k_a\in\mathbb N\), independent of the graph, its numerical data and \(q\), such that
\[
\mathrm{work}\le K_a(n+m)L^{k_a},\qquad
\mathrm{depth}\le K_a L^{k_a}.
\]
These are explicit editorial model conventions for the source's parallel resource question. They count the finite precision needed by an actual implementation. Polynomially many processors without the work bound, or a subpolynomial factor that is not bounded by a fixed power of \(L\), is insufficient.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of this disjunctive existence assertion. A positive answer must specify one uniform algorithm for at least one whole alternative and establish its feasibility, approximation, per-instance success probability and simultaneous work/depth bounds for every fixed data-and-accuracy exponent \(a\). A negative answer must rule out the asserted algorithm for both alternatives in the stated model. The question is binary; there is no additional numerical \(1/100\) tolerance. A theorem about the optimum value alone must also supply the required flow output, and a capacity-violating bicriteria result alone does not meet the stated feasibility guarantee.''',
 source_formulation=dict(
 text='The authors ask whether either undirected edge-capacitated minimum-cost flow or undirected vertex-capacitated maximum flow admits a parallel approximation scheme with nearly-linear total work and polylogarithmic depth.',
 caption='Paraphrase of §III, Open Problem 1; the budgeted-throughput approximation convention is defined in §I.A.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=81,method='editorial',
 reason='This asks for work-efficient polylogarithmic parallel time for fundamental flow primitives that combine cost or vertex congestion with capacity constraints.',
 basis='Individual assessment of the simultaneous work/depth barrier, the general graph scope and the distinction from already parallelizable edge maximum flow.'),
 why='A small depth bound makes an algorithm useful on many processors only when the total work also remains close to input size. The question asks whether cost budgets or vertex bottlenecks force an additional parallel cost for basic flow optimization. Its resolution would clarify the boundary between known efficient parallel flow primitives and more general constrained routing.',
 references=[
 ref('primary','Parallel (1+ε)-Approximate Multi-Commodity Min-Cost Flow in Almost Optimal Depth and Work',
 'Bernhard Haeupler; Yonggang Jiang; Yaowei Long; Thatchaphol Saranurak; Shengzhe Wang',2025,
 'https://doi.org/10.1109/FOCS63196.2025.00099',
 'FOCS 2025, pp. 1886–1895; §I.A and Theorem 1, p. 1887; §III, Open Problem 1, p. 1894'),
 ref('full','Parallel (1+ε)-Approximate Multi-Commodity Mincost Flow in Almost Optimal Depth and Work',
 'Bernhard Haeupler; Yonggang Jiang; Yaowei Long; Thatchaphol Saranurak; Shengzhe Wang',2025,
 'https://arxiv.org/abs/2510.20456v1',
 'Version 1, 23 October 2025; §3.1, pp. 15–16; Definitions 7.1–7.2, Theorem 7.3 and Remark 7.4, pp. 58–59'),
 ref('edge','Parallel Approximate Maximum Flows in Near-Linear Work and Polylogarithmic Depth',
 'Arpit Agarwal; Sanjeev Khanna; Huan Li; Prathamesh Patil; Chen Wang; Nathan White; Peilin Zhong',2024,
 'https://doi.org/10.1137/1.9781611977912.140',
 'SODA 2024; primary preprint arXiv:2402.14950v1, abstract and main theorem'),
 ref('expanders','Back in the Saddle: Toward Parallel Approximate Minimum-Cost Flow',
 'Rasmus Kyng; Aurelio L. Sulser',2026,
 'https://doi.org/10.4230/LIPIcs.ICALP.2026.136',
 'ICALP 2026, Article 136; abstract and §1, questions Q1–Q3 and the unit-capacity/unit-length expander result'),
 ref('exact','Parallel Minimum Cost Flow in Near-Linear Work and Square Root Depth for Dense Instances',
 'Jan van den Brand; Hossein Gholizadeh; Yonggang Jiang; Tijn de Vos',2025,
 'https://arxiv.org/abs/2503.13274',
 'SPAA 2025; primary preprint, abstract: work near m+n^(3/2) and square-root depth'),
 ],
 context_blocks=[
 block('An undirected capacity bounds total flow through a resource; a cost budget bounds the sum of flow times edge cost. Vertex capacities instead constrain all traffic passing through a vertex. These impose different feasible regions even when the graph and terminals agree.'),
 block('The source studies the more general setting with costs and capacities on both edges and vertices. Its single-commodity theorem achieves almost-linear work and subpolynomial depth for inverse-polylogarithmic accuracy. The open question asks for the sharper polylogarithmic factors, already on either restricted alternative.'),
 block('The full version also treats concurrent and nonconcurrent multicommodity demands. Open Problem 1 is posed even for a single commodity. The broader multicommodity problem and its dependence on the number of commodities are not added to this target.','full'),
 block('SODA 2024 gives an undirected edge-capacitated maximum-flow approximation using work O(m ε^{-3} polylog n) and depth O(ε^{-3} polylog n). That result has neither the cost budget of the first alternative nor the vertex capacities of the second.','edge'),
 block('The ICALP 2026 result concerns unit capacities and unit lengths on expanders. For conductance φ it gives work near m/(εφ) and depth near 1/(εφ), with approximate congestion and cost while routing prescribed demand exactly. Its restricted graph class and bicriteria guarantee leave the general question here unresolved.','expanders'),
 block('The SPAA 2025 exact-flow algorithm has square-root, rather than polylogarithmic, depth. Its near m+n^{3/2} work is nearly linear on sufficiently dense instances; this does not supply the simultaneous bounds sought for all graphs.','exact'),
 ],
 progress=[
 progress('2024','Published work establishes nearly-linear work and polylogarithmic depth for approximate undirected edge-capacitated maximum flow.','edge'),
 progress('2025','FOCS gives the broader flow algorithm with subpolynomial overhead and explicitly poses the sharper resource target.'),
 progress('2026-07-01','ICALP publishes a polylogarithmic-depth result for the restricted unit-data expander setting, with a bicriteria guarantee.','expanders'),
 progress('2026-09-16','Individual review separates the two alternatives, the cost-budget meaning of approximation and the exact simultaneous work/depth requirements.'),
 ],
),notes,sources,status,summary=[
 'The question concerns parallel approximation of single-commodity flow in undirected graphs.',
 'It asks for an algorithm for at least one of two full classes: edge-capacitated flow under a cost budget, or vertex-capacitated maximum flow.',
 'The output must be a feasible flow with value within a factor of one plus the requested inverse-polylogarithmic error of optimum.',
 'The target combines nearly-linear total work with polylogarithmic depth, improving on general results with subpolynomial overhead.',
 'The checked 2026 expander result addresses a restricted case and does not settle this general graph question.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
