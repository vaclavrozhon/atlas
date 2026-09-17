"""Complete unconditional gap hardness at the Goemans–Williamson threshold."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7281';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the universal rational-epsilon target and rational completeness/soundness thresholds for simple unweighted graphs.',
 'Defined the gap promise through an explicit deterministic polynomial-bit-time reduction from 3-SAT, including its input/output representation and parameter dependencies.',
 'Distinguished proving NP-hardness without a conjecture from proving nonexistence of polynomial algorithms; no P-versus-NP separation is assumed in the proposition.',
 'Read the primary conditional theorem, the original approximation guarantee and the unconditional 17/16-minus-epsilon convention, translating the latter to a retained fraction above 16/17.',
 'Checked the September 2025 special-graph improvement and July 2026 Max-3-Cut/quantum claims; neither resolves the classical two-part unconditional target.',
 'Preserved importance 94 and category; expanded the exact negation and required a complete Lean-checked proof.',
]
sources=[
 'Read Khot–Kindler–Mossel–O’Donnell, author manuscript dated 7 February 2007, title including its question mark, §2 pp. 3–4 and §6.1 Theorem 1 pp. 11–12. The theorem explicitly assumes the Unique Games Conjecture; §2 also discusses weighted/unweighted approximation equivalence. The card retains simple unweighted graphs and requires its own complete reduction guarantee.',
 'Read Goemans–Williamson, Journal of the ACM 42(6), 1995, pp. 1115–1145, author-hosted paper abstract: the randomized semidefinite-programming approximation benchmark.',
 'Read Håstad, Some optimal inapproximability results, author-hosted full manuscript, §8 Theorem 8.2 printed/PDF p. 62. It states hardness within 17/16-epsilon in the reciprocal approximation-factor convention. This corresponds to retained fractions strictly above 16/17, not to the Goemans–Williamson threshold.',
 'Read George–Louis–Paul, APPROX/RANDOM 2025 Article 27, published 15 September 2025, primary abstract. The better-than-GW guarantee assumes linearly many edge-disjoint triangles and applies to special graph families; it is not a general-graph improvement or an unconditional hardness result.',
 'Read Bhangale–Zhang, ICALP 2026 Article 30, primary introduction. It still cites the 16/17 Max-Cut hardness benchmark and addresses generalized group-equation CSPs rather than claiming the selected threshold.',
 'Read Heilman, arXiv:2608.00333v1, submitted 31 July 2026, primary abstract and version history. The Max-3-Cut and quantum product-state hardness claims both explicitly assume Unique Games. No full proof audit was undertaken; even the stated claims do not settle classical two-part unconditional hardness.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the selected proposition. Related TCS-0006 is the Unique Games conjecture itself, TCS-0088 concerns directed cuts and TCS-7282 concerns Vertex Cover approximation.',
]
complete(identifier,dict(
 criterion='reductions',question_type='yes_no',
 formal=r'''Let
\[
 \alpha_{\mathrm{GW}}=
 \min_{0<\theta\le\pi}\frac{2\theta}{\pi(1-\cos\theta)}.
\]
Is the following statement true? For every rational \(\varepsilon\) with \(0<\varepsilon<1-\alpha_{\mathrm{GW}}\), there exist rational constants \(0<b<a\le1\), with
\[
 \frac ba<\alpha_{\mathrm{GW}}+\varepsilon,
\]
and a deterministic polynomial-time many-one reduction \(R_\varepsilon\) from 3-SAT to simple unweighted Max-Cut such that, for every 3-CNF formula \(\varphi\), its output graph has at least one edge and satisfies
\[
 \varphi\text{ satisfiable}\ \Longrightarrow
       \operatorname{val}(R_\varepsilon(\varphi))\ge a,
 \qquad
 \varphi\text{ unsatisfiable}\ \Longrightarrow
       \operatorname{val}(R_\varepsilon(\varphi))\le b?
\]
The statement assumes no hardness conjecture.''',
 definitions=r'''A graph \(G=(V,E)\) is finite, simple and undirected: there are no loops, parallel edges or edge weights. Write \(V=\{1,\ldots,n\}\), with \(n\ge2\), and \(m=|E|\ge1\). A cut is a subset \(S\subseteq V\), representing the bipartition \((S,V\setminus S)\). Its size is the number of edges with exactly one endpoint in \(S\). Define the normalized optimum by
\[
 \operatorname{val}(G)=\frac1m\max_{S\subseteq V}
       |\{\{u,v\}\in E:|\{u,v\}\cap S|=1\}|.
\]
The constants \(a\) and \(b\) are fractions of all edges, not numbers of edges. The gap promise consists of YES graphs with value at least \(a\) and NO graphs with value at most \(b\). A procedure distinguishing these cases has no required behavior on graphs with value strictly between \(b\) and \(a\). The reduction must map every input formula into one of the two promised cases according to its satisfiability.

A 3-CNF formula is an explicit finite conjunction of clauses, each a disjunction of at most three Boolean literals, with each literal a variable or its negation. Satisfiability means that some assignment of Boolean values makes every clause true. Empty clauses are false and an empty conjunction is true. Variables and signs are listed in a standard binary encoding; let \(L\) be the full encoding length. Equivalent explicit encodings related by polynomial-time translations give the same reduction notion.

For each fixed \(\varepsilon\), the reduction is one finite deterministic Turing-machine program, uniform over all input lengths. There must exist constants \(K\ge1\) and an integer \(d\ge1\) such that it halts within \(K(L+1)^d\) bit operations on every valid formula. It outputs the graph explicitly, for example by its vertex count and binary adjacency matrix. Thus its output size is also polynomial in \(L\). A single output graph is required; oracle calls, a randomized reduction and a succinct implicit graph do not meet this definition.

The rationals \(a,b\), the program and its polynomial bound may depend on the fixed \(\varepsilon\), but not on \(\varphi\) or \(L\). The question does not require one reduction with polynomial dependence on the bit length of \(\varepsilon\), or an algorithm that constructs the reduction from \(\varepsilon\). Once chosen, each reduction itself is uniform and efficient in its formula input.

The constant \(\alpha_{\mathrm{GW}}\) is defined by the exact real expression above, with angles in radians and the usual constants \(\pi\) and cosine. Its approximate value \(0.878567\) is only explanatory; substituting a rounded decimal does not define the target. A multiplicative retained-fraction guarantee \(r\) for this maximization problem means a cut of size at least \(r\) times the optimal size. A gap with \(b/a<r\) separates satisfiable and unsatisfiable reductions for such a guaranteed approximation.

Here NP-hardness means precisely the displayed reduction from 3-SAT. It is a claim about the existence of polynomial-time reductions, not an assumed inequality between complexity classes. Proving those reductions does not itself prove \(\mathrm P\ne\mathrm{NP}\). The Unique Games Conjecture, Gap-ETH and other unproved hardness assumptions are not premises of the proposition.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the proposition or of its logical negation.

A positive answer must establish the reduction for every specified rational \(\varepsilon\), with rational thresholds, polynomial output size, deterministic polynomial bit complexity, and both correctness implications for all formulas. If an intermediate construction uses weighted graphs, parallel edges or a different constraint problem, its conversion to the required simple unweighted graph must be included with the required gap bound.

A negative answer must prove that some rational \(\varepsilon\) in the stated interval admits no pair of thresholds and deterministic polynomial-time reduction satisfying all the conditions. It is not enough to refute one proposed reduction or one conjecture used by a known construction.

An implication conditional on an unproved Unique Games assumption does not settle the unconditional proposition. An integrality gap for a particular relaxation, or an approximation algorithm without the further theorem needed to exclude NP-hardness, likewise does not alone establish either answer. No fixed additive numerical tolerance replaces the universal epsilon quantifier.''',
 source_formulation=dict(text='The source proves optimal Max-Cut inapproximability at the Goemans–Williamson ratio under the Unique Games Conjecture. The card asks whether ordinary unconditional NP-hardness can yield gaps arbitrarily close to that same ratio, retaining its approved simple-graph formulation.',caption='Paraphrase of Khot–Kindler–Mossel–O’Donnell (7 February 2007 author version), §2 and §6.1 Theorem 1; the requested removal of the conjectural premise is the card target.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Optimal Inapproximability Results for MAX-CUT and Other 2-Variable CSPs?','Subhash Khot; Guy Kindler; Elchanan Mossel; Ryan O’Donnell',2007,'https://www.stat.berkeley.edu/~mossel/publications/max_cut_final.pdf','Author manuscript dated 7 February 2007; §2 pp. 3–4 and §6.1 Theorem 1 pp. 11–12, explicit Unique Games premise'),
 ref('gw','Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems Using Semidefinite Programming','Michel X. Goemans; David P. Williamson',1995,'https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf','Journal of the ACM 42(6), pp. 1115–1145; abstract, randomized approximation benchmark'),
 ref('hastad','Some optimal inapproximability results','Johan Håstad',2001,'https://people.kth.se/~johanh/optimalinap.pdf','Author-hosted full manuscript, §8 Theorem 8.2 printed/PDF p. 62; reciprocal 17/16-minus-epsilon convention'),
 ref('triangles','Triangles Improve 0.878 Approximation for Maxcut','Fredie George; Anand Louis; Rameesh Paul',2025,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2025.27','15 September 2025; primary abstract, better ratio under an edge-disjoint-triangle structural condition'),
 ref('threecut','Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT','Steven Heilman',2026,'https://arxiv.org/abs/2608.00333v1','31 July 2026; primary abstract, both hardness claims retain Unique Games and concern different cut objectives; full proof not independently audited'),
 ],
 why='An unconditional reduction at this threshold would explain the limit of a landmark semidefinite approximation algorithm using ordinary NP-hardness, without adding a separate hardness conjecture.',
 context_blocks=[
 block('The Goemans–Williamson algorithm supplies the approximation benchmark through semidefinite programming and randomized rounding.','gw'),
 block(r'Håstad establishes unconditional hardness for retained fractions strictly above \(16/17\). This leaves a gap to \(\alpha_{\mathrm{GW}}\); the reciprocal convention in that paper should not be confused with the fraction used here.','hastad'),
 block('The source reaches the Goemans–Williamson threshold assuming Unique Games. The present target asks for the same limiting hardness scale without that conjectural premise.'),
 block('The 2025 improvement assumes a structural abundance of edge-disjoint triangles. It does not assert a better approximation for every graph or settle unconditional hardness.','triangles'),
 block('The July 2026 preprint states sharp hardness for three-part cuts and for a quantum product-state objective. Both statements explicitly retain the Unique Games assumption, so even their stated scope does not resolve this classical two-part question.','threecut'),
 ],
 progress=[progress('1995','Semidefinite rounding establishes the Goemans–Williamson approximation benchmark.','gw'),progress('2001','Unconditional Max-Cut hardness reaches the 16/17 retained-fraction threshold.','hastad'),progress('2007-02-07','The source theorem matches the Goemans–Williamson ratio assuming Unique Games.'),progress('2025-09-15','A better ratio is proved for graphs with sufficiently many edge-disjoint triangles.','triangles'),progress('2026-07-31','New sharp-hardness claims concern different cut objectives and retain Unique Games.','threecut')],
),notes,sources,'The checked primary sources give unconditional hardness at the weaker 16/17 scale and matching Goemans–Williamson hardness under Unique Games. Bounded checks through 17 September 2026 found no verified unconditional resolution of the exact simple-unweighted-graph gap statement. Recent special-graph and three-part or quantum results do not cover it; full new-preprint proofs were not independently audited.',summary=[
 'Max-Cut asks for a bipartition crossing as many edges of a graph as possible.',
 'The question asks for unconditional NP-hardness of approximation arbitrarily close to the Goemans–Williamson ratio.',
 'The requested proof must reduce every 3-SAT formula deterministically to a simple unweighted graph with a fixed satisfiable-versus-unsatisfiable gap.',
 'Matching known hardness uses Unique Games, while the checked newer cut results have different graph restrictions or objectives.',
 'A complete Lean-checked proof must establish the full reduction statement or its exact logical negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
