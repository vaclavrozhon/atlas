"""Review exact almost-linear directed vertex connectivity in all regimes."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7345';claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained the exact unweighted directed vertex-connectivity endpoint and output of an attaining separator.',
 'Preserved the at-most-one-remaining-vertex convention, including value zero on disconnected inputs and n-1 on complete bidirected inputs.',
 'Made the single uniform almost-linear algorithm, subpolynomial overhead and all-execution time bound explicit.',
 'Specified explicit adjacency-list input and packed separator output without adding a hidden connectivity promise.',
 'Read the SODA 2026 unweighted theorem and corrected the context to identify its running time as expected and its stated success probability as one half.',
 'Compared both approximation schemes, including the July 2026 version, with the exact endpoint and its precision cost.',
 'Preserved importance, linked the distinct edge-cut problem and required a complete Lean-checked answer.',
]
sources=[
 'Read Chuzhoy–Mosenzon–Trabelsi, Faster Algorithms for Global Minimum Vertex-Cut in Directed Graphs, arXiv:2512.24355v1, 30 December 2025, SODA 2026 DOI 10.1137/1.9781611978971.199, published online 7 January 2026: abstract, Introduction definitions and Theorem 1.2 p.4. For a simple unweighted directed graph containing a vertex-cut, the theorem gives expected O(min{m^{1+o(1)} k,n^{2+o(1)}}) time and success probability at least one half. The source excludes complete bidirected graphs from that theorem; the card’s n-1 convention supplies that easy case explicitly. The expected-time qualifier must not be omitted.',
 'Read Quanrud, Approximating Directed Connectivity in Almost-Linear Time, arXiv:2512.00176v1, submitted 28 November 2025, PDF cover 2 December 2025: Theorems 1.2–1.3 pp.2–3. The relative scheme has inverse-epsilon dependence; its exact integer-capacitated result retains a factor proportional to vertex connectivity, up to subpolynomial terms.',
 'Read Mosenzon, Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs, arXiv:2512.09080v3, 20 July 2026: Introduction, Table 1 and Theorem 1.2 p.3. The global vertex-cut approximation has inverse-precision cost and requires that a vertex-cut exists, equivalently that the directed graph is not complete. The authors describe exact recovery with a connectivity-dependent cost; this does not establish almost-linear exact time in all density and connectivity regimes.',
 'Bounded primary-source checks through 17 September 2026 found no verified resolution of the exact uniform endpoint. Undirected algorithms, edge-cut results, weighted approximation and parameter-dependent exact results were distinguished. No independent validation of the full new proofs is claimed.',
]
complete(identifier,dict(
 formal=r'''Do there exist one uniform randomized algorithm \(A\), a constant \(C\ge1\), an integer word-size constant \(d\ge4\), and a function \(h:\mathbb N_{\ge2}\to[1,\infty)\) satisfying
\[
\lim_{N\to\infty}\frac{\log h(N)}{\log N}=0,
\]
such that, on every simple unweighted directed graph \(G\) with \(n\ge2\) vertices and \(m\) arcs, every execution uses at most \(C(m+n)h(m+n)\) word-RAM instructions and, with probability at least \(2/3\), outputs the exact vertex connectivity \(\kappa(G)\) together with an attaining vertex set? Define
\[
\kappa(G)=\min\{|S|:S\subseteq V(G),\ G-S\text{ is not strongly connected or }|V(G)\setminus S|\le1\}.
\]
Both density and connectivity are unrestricted.''',
 definitions=old['definitions']+r'''

The explicit input consists of \(n,m\) and an array of \(m\) ordered endpoint pairs, one word per endpoint. The output separator is an \(n\)-bit incidence vector packed into words, and the reported connectivity is an integer word. Output writing is charged. A successful output satisfies both \(|S|=\kappa(G)\) and the displayed separator condition. Failed executions may return a failure symbol or an incorrect result, but must obey the same instruction limit. The word-size constant is at least four and may be larger if needed for the fixed algorithm’s addressing.

For a complete bidirected graph the answer is \(n-1\), achieved by leaving one vertex. Every noncomplete graph has two vertices missing at least one directed arc between them, so deleting the others supplies a separator leaving at least two vertices. Thus the stated convention agrees with the nonempty-left-and-right cut formulation throughout the noncomplete case. No strong-connectivity promise is imposed on the input.

The quantifier order is \(\exists(A,C,d,h)\,\forall G\). In particular, neither the program nor its almost-linear overhead can depend on the unknown \(\kappa(G)\), an edge-density promise or a requested fixed exponent. There is no separate space restriction beyond charged computation and word-addressable memory. Approximation of \(\kappa(G)\) is not an alternative output guarantee.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive proof must establish one uniform algorithm, exact value and separator correctness with the required probability, and the subpolynomial-overhead time bound on every execution for every input. A negative proof must rule out the full statement unconditionally; an assumption-based lower bound is only a conditional result.

An almost-linear approximation, an exact bound with an unrestricted extra connectivity factor, or a result confined to undirected graphs does not settle the target. An expected-time algorithm is sufficient only with a justified conversion to the stated bounded-error worst-case time guarantee. The at-most-one-remaining-vertex convention must also be handled. No numerical tolerance in the answer is allowed.''',
 source_formulation=dict(text='Recent work improves exact directed vertex-cut algorithms and obtains almost-linear relative approximation. This card retains the editorial endpoint of exact almost-linear computation for every unweighted directed graph, including all intermediate density and connectivity regimes.',caption='Chuzhoy–Mosenzon–Trabelsi, SODA 2026, unweighted Theorem 1.2; Quanrud, §1 exact-connectivity discussion; exact uniform endpoint and complete-graph convention are editorial specifications.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Faster Algorithms for Global Minimum Vertex-Cut in Directed Graphs','Julia Chuzhoy; Ron Mosenzon; Ohad Trabelsi',2026,'https://arxiv.org/abs/2512.24355v1','30 December 2025 preprint; SODA publication 7 January 2026, DOI 10.1137/1.9781611978971.199; Introduction and Theorem 1.2 p.4, expected time and success probability'),
 ref('approx','Approximating Directed Connectivity in Almost-Linear Time','Kent Quanrud',2025,'https://arxiv.org/abs/2512.00176v1','Submitted 28 November 2025; Theorems 1.2–1.3 pp.2–3, approximate and connectivity-dependent exact bounds'),
 ref('revised','Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs','Ron Mosenzon',2026,'https://arxiv.org/abs/2512.09080v3','20 July 2026 revision; Introduction, Table 1 and Theorem 1.2 p.3, vertex-cut approximation and inverse precision'),
 ],
 related=['TCS-7344','TCS-7346'],
 context_blocks=[
 block('Directed vertex connectivity measures resilience to vertex removals when reachability is asymmetric. The task asks for the most vulnerable separator anywhere in the graph.'),
 block(r'The SODA 2026 theorem gives randomized expected time \(O(\min\{m^{1+o(1)}\kappa,n^{2+o(1)}\})\), with its stated success probability at least one half. It covers useful low-connectivity and dense regimes, but does not give almost-linear time everywhere.'),
 block('Almost-linear relative approximation schemes are known. Their exact integer versions retain a connectivity-dependent cost, which is not uniformly subpolynomial.','approx'),
 block('The July 2026 revision supplies another vertex-cut scheme with inverse-precision dependence. Its noncomplete-graph requirement is separate from the easy complete-graph convention used here.','revised'),
 ],
 progress=[progress('2025-11-28','An almost-linear relative scheme and an exact algorithm with a connectivity factor are stated.','approx'),progress('2026-01-07','The SODA paper publishes its improved exact unweighted bound, measured in expected time.'),progress('2026-07-20','The revised approximation paper states a global vertex-cut guarantee with explicit inverse-precision dependence.','revised')],
),notes,sources,'The checked exact theorem has connectivity-dependent expected time, and the approximation schemes pay for inverse precision. Bounded primary-source checks through 17 September 2026 found no verified almost-linear exact algorithm for all unweighted directed inputs in the stated uniform model. This is an explicit editorial endpoint, not a verbatim conjecture or independent certification of all cited proofs.',summary=[
 'The input is any simple unweighted directed graph, with no connectivity or density promise.',
 'The output is the smallest number of vertices whose removal destroys strong connectivity, together with such a set.',
 'Leaving at most one vertex is allowed, so a complete bidirected graph has value n minus one.',
 'The target is exact almost-linear randomized computation on every input; known expected and approximation bounds have additional limitations.',
 'A complete Lean-checked construction or unconditional refutation must respect the worst-case time and bounded-error guarantees.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
