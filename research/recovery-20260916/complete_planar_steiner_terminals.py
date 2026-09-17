"""Archive the terminal-parameter Steiner question with its published ETH condition."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4637';claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the original unweighted undirected planar problem and distinguished terminal count from the number of edges of a solution.',
 'Specified a uniform deterministic subexponential parameter factor with one fixed polynomial input exponent and exact decision semantics.',
 'Verified the FOCS 2018 conditional negative theorem, first posted in the 2017 full version, and its final conversion to unit weights.',
 'Archived the historical question under ETH, without claiming an unconditional lower bound or a randomized lower bound under deterministic ETH.',
 'Pinned the full proof to arXiv version 1: version 2 was narrowed to Directed Subset TSP and is not the same full Steiner paper.',
 'Assessed the historical significance individually and separated the published resolution from a complete Lean certification.',
]
sources=[
 'Read Pilipczuk–Pilipczuk–Sankowski–van Leeuwen, STACS 2013, DOI 10.4230/LIPIcs.STACS.2013.353, Section 5, printed p.363 / PDF p.11. The selected question is the stronger parameterization by terminal count, not the solution-edge-count question or the adjacent Steiner Forest question.',
 'Read Marx–Pilipczuk–Pilipczuk, FOCS 2018, DOI 10.1109/FOCS.2018.00052, pp.474–484, primary proceedings PDF https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f474.pdf, Theorems I.2 and I.3 and their surrounding discussion on p.476. Theorem I.2 excludes 2^{o(k)} n^{O(1)} time under ETH already for unweighted undirected planar graphs.',
 'Read the original full version arXiv:1707.02190v1, 7 July 2017, Theorem 1.2 and Section 7, pp.40–41, Theorems 7.1–7.2, Lemma 7.3 and the implication proof, and the final unit-weight conversion on p.52. The reduction keeps O((n+m)/epsilon) terminals and allows graph size 2^{epsilon(n+m)} times a polynomial. Its quantifiers rule out a subexponential parameter factor with one fixed polynomial exponent. The full gadget correctness proof was not independently reconstructed.',
 'Inspected arXiv:1707.02190v2, 30 September 2022: its title and scope now concern Directed Subset Traveling Salesman; its introduction still cites the earlier Steiner lower bound. The archival reference is deliberately pinned to v1 for the complete Steiner proof.',
 'Fresh primary-source check through 17 September 2026 includes the abstract of Bhore–Esmer–Marx–Wegrzycki, arXiv:2511.07346v1, 10 November 2025. Its n^{O(sqrt(t))} geometric/planar comparisons have the graph size raised to a terminal-dependent exponent and are not the fixed-parameter target here. No checked source overturns the conditional resolution.',
]
status='Archived as a historical question answered negatively under the Exponential-Time Hypothesis. Marx–Pilipczuk–Pilipczuk prove this for unweighted undirected planar graphs in Theorem 1.2 of the 7 July 2017 full preprint and Theorem I.2 of FOCS 2018. This is a conditional deterministic lower bound, not an unconditional impossibility claim. The later n^{O(sqrt(k))} algorithm has a parameter-dependent polynomial exponent and does not meet the historical target.'
complete(identifier,dict(
 title='Subexponential Planar Steiner Tree by terminal count',status='resolved',year=2018,
 criterion='resources',question_type='yes_no',
 importance=dict(score=84,method='editorial',reason='The historical question tests whether planarity yields a subexponential fixed-parameter algorithm for a central network-design problem under its natural terminal parameter; the conditional negative result separates this parameter from solution size.'),
 formal=r'''Historical question, answered negatively under the Exponential-Time Hypothesis (ETH): does exact Steiner Tree on finite unweighted undirected planar graphs admit a uniform deterministic algorithm with running time \(2^{o(k)}L^{O(1)}\), where \(k\) is the number of terminals and \(L\) is the full input length in bits?

More precisely, do there exist one deterministic Turing algorithm \(A\), constants \(K>0\), \(c\ge1\), and a total computable function \(f:\mathbb N\to\mathbb N_{\ge1}\) satisfying
\[
\lim_{k\to\infty}\frac{\log_2 f(k)}{k}=0,
\]
such that \(A\) correctly decides every instance defined below in at most \(Kf(k)(L+1)^c\) bit steps? The published resolution establishes that this existence proposition implies the failure of ETH.''',
 definitions=r'''An instance consists of a finite simple undirected planar graph \(G=(V,E)\) with numbered vertices \(V=\{1,\ldots,n\}\), \(n\ge1\), a terminal set \(T\subseteq V\), and an integer budget \(b\in\{0,\ldots,n-1\}\). Every edge has cost one. The answer is yes exactly when there is a connected acyclic subgraph containing every terminal and having at most \(b\) edges. Vertices outside \(T\) may be used freely, subject to that edge budget. Disconnected graphs are allowed; terminals lying in different components give a no instance. For at most one terminal, the optimum cost is zero. Set \(k=|T|\).

The input is an explicit adjacency matrix, a terminal incidence vector and binary encodings of \(n,b\), with separators. Its full length is \(L\); there is no succinct graph representation or external graph oracle. Planarity is a promise on the input. A planar embedding need not be supplied. A Turing algorithm here has a fixed finite program, finitely many tapes and the usual bit-step cost. All input access and computation count. No advice, random bits or nonuniform precomputed tables are available. Correctness and the time bound must hold for every valid instance. Behavior outside the promise is irrelevant.

The algorithm, \(K,c,f\) are chosen once, before the input. In particular, the exponent \(c\) cannot grow with \(k\) or with a requested accuracy. The limit above defines the subexponential parameter factor. It is not a bound of the form \(n^{O(\sqrt{k})}\), nor a separate algorithm with an increasingly large polynomial exponent for each desired exponential base. Polynomial changes between explicit graph encodings do not change this existence target. The budget parameter is not counted in place of \(k\).

For this deterministic conditional statement, ETH means that there is a constant \(\delta>0\) for which no uniform deterministic algorithm decides satisfiability of every Boolean 3-CNF formula in time \(O(2^{\delta v}(|\varphi|+1)^d)\) for any fixed \(d\), where \(v\) is its number of variables and \(|\varphi|\) is its explicit encoding length. A 3-CNF formula is a conjunction of clauses, each a disjunction of at most three Boolean variables or their negations. The graph lower bound is an implication from this hypothesis; ETH is not proved by the archival decision. A claim about bounded-error randomized algorithms would require a corresponding randomized hardness hypothesis and is not asserted here.''',
 answer_criterion=r'''The retained formalization criterion for the published resolution is a complete Lean-checked proof that the specified Steiner algorithm would contradict ETH, equivalently that ETH implies its nonexistence. A citation is not such a formal proof. The research question is archived on the strength of the published conditional theorem; the archive does not claim that this theorem has already been certified in Lean or create a new active formalization task.''',
 source_formulation=dict(text='The conclusion asks whether Planar Steiner Tree has a subexponential-time algorithm parameterized by the number of terminals, separately from the number of edges in a solution studied by the paper.',caption='STACS 2013, Section 5, printed p.363; historical question subsequently answered under ETH.',citation='primary',format='editorial_paraphrase'),
 why='The terminal set describes the connection requests, whereas an optimal tree may contain far more edges and intermediate vertices. Distinguishing these parameters determines when planarity can support subexponential exact algorithms for network design.',
 references=[
 ref('primary','Subexponential-Time Parameterized Algorithm for Steiner Tree on Planar Graphs','Marcin Pilipczuk; Michał Pilipczuk; Piotr Sankowski; Erik Jan van Leeuwen',2013,'https://doi.org/10.4230/LIPIcs.STACS.2013.353','STACS 2013, pp.353–364; Section 5, printed p.363 / PDF p.11'),
 ref('resolution','On Subexponential Parameterized Algorithms for Steiner Tree and Directed Subset TSP on Planar Graphs','Dániel Marx; Marcin Pilipczuk; Michał Pilipczuk',2018,'https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f474.pdf','FOCS 2018, pp.474–484, DOI 10.1109/FOCS.2018.00052; Theorems I.2 and I.3, p.476'),
 ref('fullproof','On subexponential parameterized algorithms for Steiner Tree and Directed Subset TSP on planar graphs','Dániel Marx; Marcin Pilipczuk; Michał Pilipczuk',2017,'https://arxiv.org/abs/1707.02190v1','Version 1, 7 July 2017; Theorem 1.2 and Section 7, especially pp.40–41 and final unit-weight conversion on p.52; later version 2 has a narrower TSP scope'),
 ],
 context_blocks=[
 block('The source distinguishes terminal count from solution size. A tree may have few required vertices but need many edges to connect them; the algorithm for the larger parameter does not settle the terminal question.'),
 block(r'The later theorem excludes \(2^{o(k)}n^{O(1)}\) time under ETH even with unit edge costs. Its proof applies directly to the historical terminal parameter.','resolution'),
 block(r'The same work also gives an \(n^{O(\sqrt{k})}\) bound in the unit-weight case. This is compatible with the lower bound because the exponent of the graph size depends on \(k\).','resolution'),
 block('The full Steiner proof is in the original preprint version. A later version of the same arXiv identifier concentrates on a different problem, so an unversioned reference could conceal the needed proof.','fullproof'),
 ],
 progress=[progress('2013','The source asks for subexponential exact computation in the number of terminals, distinct from its solution-size parameter.'),progress('2017-07-07','The original full preprint states and proves the ETH-conditional negative result for unit-weight planar instances.','fullproof'),progress('2018-10','FOCS 2018 publishes the conditional lower bound as Theorem I.2.','resolution')],
),notes,sources,status,summary=[
 'The historical question asks for exact planar Steiner Tree in time subexponential in the number of required terminals, times one fixed polynomial in input length.',
 'The graph is undirected and unweighted, and intermediate nonterminal vertices may be used.',
 'The 2017 full preprint and FOCS 2018 theorem give a negative answer under the Exponential-Time Hypothesis.',
 'Algorithms whose graph-size exponent grows with the terminal count do not meet the requested fixed-parameter bound.',
 'The record is archived as conditionally resolved, without claiming an unconditional lower bound or an existing Lean formalization.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='Historical terminal-parameter Planar Steiner Tree question resolved negatively under ETH: Marx–Pilipczuk–Pilipczuk, FOCS 2018 Theorem I.2 and arXiv:1707.02190v1 Theorem 1.2, exclude 2^{o(k)} n^{O(1)} time even for unweighted undirected planar graphs. Conditional resolution, not an unconditional impossibility result.')
