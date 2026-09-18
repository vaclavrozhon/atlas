"""Retain the exact binary entropic/submodular width separation question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4995';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Entropic width versus submodular width',status='source_open',criterion='models',question_type='yes_no',
 formal=r'''Does there exist a finite hypergraph \(H=(V,E)\), with \(V=\{1,\ldots,n\}\), \(n\ge1\), nonempty hyperedges and \(\bigcup E=V\), such that
\[
\operatorname{entw}(H)<\operatorname{subw}(H)?
\]
For a set function \(h:2^V\to\mathbb R\), define
\[
w_H(h)=\min_{(T,\chi)\in\operatorname{TD}(H)}\ \max_{t\in V(T)}h(\chi(t)),\qquad
\mathcal E_H=\{h:h(e)\le1\text{ for all }e\in E\}.
\]
The two widths are
\[
\operatorname{entw}(H)=\max_{h\in\overline{\Gamma_n^*}\cap\mathcal E_H}w_H(h),\qquad
\operatorname{subw}(H)=\max_{h\in\Gamma_n\cap\mathcal E_H}w_H(h),
\]
where \(\Gamma_n\) is the cone of normalized monotone submodular functions and \(\overline{\Gamma_n^*}\) is the closure of finite-alphabet entropy vectors, defined below. Any strictly positive gap suffices; no minimum gap such as \(1/100\) is prescribed.''',
 definitions=r'''A hypergraph has a finite vertex set and a set of nonempty subsets called hyperedges. Hyperedges may have arbitrary sizes and may contain other hyperedges; repeated copies are irrelevant. Every vertex must occur in an edge. A tree decomposition \((T,\chi)\) consists of a finite nonempty tree and a bag \(\chi(t)\subseteq V\) for every node. Each hyperedge must be contained in some bag, and, for every vertex \(v\), the nodes whose bags contain \(v\) must form a nonempty connected subtree. The set \(\operatorname{TD}(H)\) includes all such decompositions, with no bound on the number of nodes or on bag cardinalities. The minimum in \(w_H\) is taken separately for each \(h\); moving that minimum outside the maximum over \(h\) defines a different width.

The cone \(\Gamma_n\) consists of functions satisfying \(h(\varnothing)=0\), monotonicity \(h(A)\le h(B)\) whenever \(A\subseteq B\), and submodularity
\[
h(A)+h(B)\ge h(A\cup B)+h(A\cap B)\quad(A,B\subseteq V).
\]
These conditions imply nonnegativity. This is the polymatroid cone; neither integer-valuedness nor representability by vector spaces is required. The additional constraints \(h(e)\le1\) are imposed only on hyperedges, and are identical in both optimizations. There are no functional dependencies, conditional-degree constraints or unequal edge weights.

Choose jointly distributed random variables \(X_1,\ldots,X_n\), each with an arbitrary finite nonempty alphabet and arbitrary real probabilities. They need not be independent. For \(S\subseteq V\), let \(X_S\) be their joint tuple and let
\[
H(X_S)=-\sum_x\Pr[X_S=x]\log_2\Pr[X_S=x],
\]
using \(0\log_2 0=0\) and \(H(X_{\varnothing})=0\). The set \(\Gamma_n^*\) consists of the vectors \(h(S)=H(X_S)\) obtained this way. Its closure \(\overline{\Gamma_n^*}\) is in the ordinary Euclidean topology on the \(2^n\) real coordinates: \(h\) belongs to it exactly when a sequence of such vectors converges coordinate by coordinate to \(h\). Alphabet sizes may grow along the sequence. Edge bounds are imposed on the limiting vector; the approximating vectors need not meet the bounds exactly. No common finite alphabet bound is assumed.

Entropy vectors and their limits satisfy the polymatroid inequalities, giving \(\operatorname{entw}(H)\le\operatorname{subw}(H)\). Both feasible regions contain zero and are compact: every singleton is bounded by an edge containing it, and subadditivity then bounds every coordinate by \(n\). The decomposition minimum is well-defined and attained; its possible objective values come from maxima of subsets of the finitely many coordinates of \(h\). Equivalently, the minimum can be taken over finitely many distinct families of bags realizable by decompositions. This also makes \(w_H\) continuous, so the displayed maxima exist. These observations specify the real-valued optimization and do not establish whether the widths can differ.

A positive answer concerns one finite witness hypergraph, with any rigorous positive separation between the two real optima. A negative answer is equality for every finite hypergraph in the stated class. The target does not ask for a faster join algorithm, an efficient method to compute either width, or a lower bound for Boolean semiring circuits.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the existence of a strict gap, or a proof that the two widths are equal for every hypergraph in the stated class. A witness with a proved entropic upper bound strictly below a proved submodular lower bound suffices, without computing either optimum exactly. An unverified numerical optimization or a gap only after adding degree constraints is insufficient.',
 importance=dict(score=82,method='editorial',reason='A separation would distinguish actual information-theoretic constraints from the submodular relaxation underlying major join algorithms. It would clarify whether their structural exponent leaves room beyond Shannon inequalities, while equality would identify a robust limit of that route.'),
 why='Submodular width optimizes over a relaxation of all possible joint information profiles. Entropic width admits only limits of realizable profiles. Whether this relaxation changes the best decomposition cost is a structural question linking information inequalities to query complexity.',
 source_formulation=dict(text='The ICDT 2025 survey states that entropic width never exceeds submodular width and asks whether the inequality can be strict. The separate nearby question about Boolean semiring circuit lower bounds is not part of this card.',caption='The Quest for Faster Join Algorithms, pp.1:9–1:10.',citation='primary',format='editorial_paraphrase'),
 references=[ref('primary','The Quest for Faster Join Algorithms (Invited Talk)','Paraschos Koutris; Shaleen Deep; Austen Fan; Hangdong Zhao',2025,'https://doi.org/10.4230/LIPIcs.ICDT.2025.1','Towards Lower Bounds, pp.1:9–1:10'),ref('definitions','Generalized Covers for Conjunctive Queries','Paraschos Koutris',2025,'https://doi.org/10.4230/LIPIcs.ICDT.2025.28','§3: tree decompositions, entropy closure and entropic width'),ref('jaguar','Jaguar: A Primal Algorithm for Conjunctive Query Evaluation in Submodular-Width Time','Mahmoud Abo Khamis; Hubie Chen',2026,'https://arxiv.org/abs/2603.13624v2','§7, pp.18–19: open problems and entropic-width discussion')],
 context_blocks=[block('The question isolates a gap between two real structural invariants. The ordering of optimization over information profiles and tree decompositions is essential.'),block('The definition uses almost-entropic vectors, including limits with growing alphabets. Restricting to a fixed alphabet would change the feasible region.','definitions'),block('The 2026 Jaguar paper gives a new algorithm at the submodular-width exponent and discusses the remaining entropic-width algorithmic target. Its checked statements do not supply a hypergraph separating the two widths or prove their equality.','jaguar')],
 progress=[progress('2025','The survey explicitly records the strict-gap question as unresolved.'),progress('2026-04-06','The checked revised Jaguar preprint retains an algorithmic frontier involving entropic width without resolving this structural comparison.','jaguar')],
),['Retained the exact strict-gap question, rather than assigning an arbitrary numerical threshold.','Defined the closure of finite-alphabet entropy vectors, the polymatroid cone and the common edge normalization.','Specified the max-min-max order, tree decompositions and the distinction from degree-aware width.','Individually assessed importance at 82 and separated later algorithmic progress from a width separation.'],['Read the ICDT 2025 survey lower-bound discussion on pp.1:9–1:10.','Read §3 of Generalized Covers for Conjunctive Queries, including the closure convention and the displayed width definition.','Read the Jaguar 2026 abstract, submodular-width setup and §7 open problems; no verified strict gap or equality result was found in bounded later searches.'],'Explicitly source-open in the ICDT 2025 survey. The checked 2026 Jaguar discussion concerns algorithms measured by the two widths and does not establish a strict gap or general equality. Primary-source checks through 18 September 2026 support retaining the question, without claiming exhaustive current-status verification.',summary=['Both widths measure a hypergraph by choosing a tree decomposition after seeing an information profile on its vertices.','Submodular width permits every normalized monotone submodular profile.','Entropic width permits only limits of profiles realized as joint entropies of finite random variables.','The question asks whether this restriction ever makes the width strictly smaller.','Any positive gap on one finite hypergraph settles the existence question, while the opposite answer requires equality for all hypergraphs.'],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
