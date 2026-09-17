"""Recover the vertex-count exponential-time question for exact cutwidth."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0800'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the explicit c<2 vertex-count target from §6.18 of the seminar report.',
 'Defined unweighted undirected cutwidth over all linear vertex orderings, including empty and one-vertex graphs.',
 'Specified one deterministic uniform bit-machine algorithm with a fixed exponential saving and no extra graph parameter or structural promise.',
 'Explained why polynomial factors can be absorbed into a slightly larger base still below two and why absolute 1/100 output accuracy yields exact computation.',
 'Checked the vertex-cover and bipartite exact algorithms and the 2025 factor-two approximation against the all-graphs exact target.',
 'Preserved the existing individually assessed importance score.',
]
sources=[
 'Read Saket Saurabh, Cutwidth, §6.18 in the Dagstuhl Seminar 13331 report, printed pp. 69–70/individual report PDF pp. 30–31. The question explicitly asks for c^n time for some constant c<2, with n the vertex count; the next section concerns a different problem.',
 'Read Cygan–Lokshtanov–Pilipczuk–Pilipczuk–Saurabh, On Cutwidth Parameterized by Vertex Cover, author journal manuscript: abstract, introduction and context pp. 1–3, §2 algorithm definition and its stated bounds. Checked publisher metadata: online 8 November 2012; Algorithmica 68:940–953 (2014). The result uses the minimum vertex-cover size, and the bipartite corollary has time O*(2^(n/2)).',
 'Read Bentert–Fomin–Inamdar–Saurabh, ITCS 2025, Article 15: introduction pp. 15:2–3 explicitly identifies the exact cutwidth time question as open; Table 1, directed definition p. 15:4 and §3.2, Proposition 4 with proof. Its faster algorithm has approximation factor two. Publisher date is 11 February 2025.',
 f'Bounded primary-source searches through {DATE} also found 2026 graph-reconstruction work parameterized by cutwidth and algorithms for other problems supplied with a cutwidth layout. Their statements do not compute exact unrestricted cutwidth below base two. No resolution of the selected target was found.',
]
status='The source asks for an exponential base below two in the number of vertices on general graphs. The checked 2025 paper still identifies this exact optimization question as open and obtains only a faster constant-factor approximation. Vertex-cover, bipartite and bounded-width results do not give the required all-graphs guarantee; no later resolution was found in the bounded search.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a uniform deterministic algorithm that computes the cutwidth of every finite simple undirected graph on \(n\) vertices in time \(O(c^n)\) for some fixed constant \(c<2\)?

Precisely, do there exist one machine \(A\), a rational constant \(c\) with \(1<c<2\), and an integer \(K\ge1\) such that, on every graph \(G\) encoded as below, \(A\) outputs \(\operatorname{cw}(G)\) and halts within \(Kc^n\) transitions? Neither \(c\) nor \(K\) may depend on the graph, its size, its cutwidth or any auxiliary parameter.''',
 definitions=r'''The graph is \(G=([n],E)\), where \(n\ge0\), \([n]=\{1,\ldots,n\}\), and \(E\) is a set of unordered pairs of distinct vertices. Edges are unweighted and undirected, with no loops or parallel copies. There are no connectivity, degree, planarity or bipartiteness promises.

A linear layout is a permutation \(\pi=(v_1,\ldots,v_n)\) of the vertices. For every \(i\in\{0,\ldots,n\}\), let
\[
B_i(\pi)=
\{\{u,v\}\in E:\ |\{u,v\}\cap\{v_1,\ldots,v_i\}|=1\}.
\]
The width of \(\pi\) is \(\max_{0\le i\le n}|B_i(\pi)|\), and
\[
\operatorname{cw}(G)=\min_{\pi}\max_{0\le i\le n}|B_i(\pi)|.
\]
The empty permutation is the unique layout when \(n=0\); its width is zero. Thus empty, one-vertex and edgeless graphs have cutwidth zero. This objective minimizes the largest crossing-edge count, rather than the sum of crossing counts or the largest distance between adjacent vertices.

Encode \(G\) by \(1^n0\), followed by one adjacency bit for every pair \(1\le u<v\le n\) in lexicographic order, with no trailing bits. The output is the ordinary binary encoding of the nonnegative integer \(\operatorname{cw}(G)\), with zero encoded as \(0\). An optimal layout need not be output.

Computation uses a deterministic multitape Turing machine with a fixed finite program and fixed finite tape alphabets, a read-only input tape, initially blank work tapes and an append-only output tape. One transition accesses the cells under the heads and moves each head by at most one cell. All transitions count, including parsing, arithmetic and output. There is no random source, advice, oracle or uncharged preprocessing. Malformed inputs must be rejected in polynomial time in their length. Working space is unrestricted apart from what the time bound permits.

The exponent uses the number \(n\) of vertices. A running-time bound in terms of an independently bounded cutwidth or vertex-cover size does not suffice. A guarantee \(O(c_0^n(n+1)^d)\) for fixed \(1<c_0<2\) and fixed \(d\) does suffice: its polynomial factor can be absorbed into \(O(c^n)\) for any fixed \(c_0<c<2\). In contrast, \(2^{n-o(n)}\) need not have a fixed base below two. Requiring a rational \(c\) loses no existential base improvement.

The numerical output follows the benchmark's absolute \(1/100\) convention as well: an algorithm producing a rational \(a_G\) with \(|a_G-\operatorname{cw}(G)|\le1/100\) for every graph can be rounded to the unique nearest integer. Here a rational is given by a signed binary numerator and a positive binary denominator. Since \(0\le\operatorname{cw}(G)\le\binom n2\), rounding can use the leading \(O(\log(n+2))\) bits of these integers and their bit lengths, with polynomial-in-\(n\) work per emitted bit. This overhead can be absorbed into a slightly larger exponential base still below two. An exact integer algorithm directly qualifies. A constant-factor estimate, by itself, does not give the required additive accuracy.''',
 answer_criterion=r'''Supply a complete Lean-checked construction of \(A,c,K\), proving correct cutwidth output and the uniform \(Kc^n\) worst-case time bound for every graph; or supply a complete Lean-checked proof that no such deterministic algorithm and constants exist. An approximation algorithm qualifies only if its output can be converted to the required value within a running time of the stated form. A speedup on a proper graph class, an algorithm with possible random error, or a conditional lower bound based on an unproved hypothesis does not settle the full target.''',
 source_formulation=dict(
 text='The report asks whether the cutwidth of an arbitrary n-vertex graph can be found with an exponential running-time base strictly below two.',
 caption='Paraphrase of Saket Saurabh’s question in §6.18, printed pp. 69–70 of the Seminar 13331 report.',
 citation='primary',format='editorial_paraphrase'),
 why='Cutwidth measures how many connections must cross the busiest boundary in a sequential arrangement of a graph. Computing it requires coordinating a whole vertex order, and the standard subset-based running time has resisted a uniform exponential improvement. A faster exact algorithm would clarify how much of that subset enumeration is essential for a basic graph layout problem.',
 references=[
 ref('primary','Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time','Saket Saurabh (Cutwidth question); Thore Husfeldt; Ramamohan Paturi; Gregory B. Sorkin; Ryan Williams (report editors)',2013,
 'https://drops.dagstuhl.de/entities/document/10.4230/DagRep.3.8.40',
 'Dagstuhl Seminar 13331; §6.18, Cutwidth, printed pp. 69–70/individual report PDF pp. 30–31'),
 ref('cover','On Cutwidth Parameterized by Vertex Cover','Marek Cygan; Daniel Lokshtanov; Marcin Pilipczuk; Michał Pilipczuk; Saket Saurabh',2014,
 'https://link.springer.com/article/10.1007/s00453-012-9707-6',
 'Algorithmica 68:940–953 (2014); published online 8 November 2012; abstract, §1 and §2; preliminary IPEC 2011 version'),
 ref('approx','Exponential-Time Approximation (Schemes) for Vertex-Ordering Problems','Matthias Bentert; Fedor V. Fomin; Tanmay Inamdar; Saket Saurabh',2025,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.15',
 'ITCS 2025, Article 15, published 11 February 2025; introduction pp. 15:2–3, Table 1 and §3.2, Proposition 4'),
 ],
 context_blocks=[
 block('The original question measures time in the number of vertices and asks for the exact optimum over all layouts. Its separate remark about bipartite graphs is an existing special-case result.'),
 block(r'The vertex-cover algorithm runs in \(O^{*}(2^\tau)\) time, where \(\tau\) is the smallest number of vertices meeting every edge. For bipartite graphs it gives \(O^{*}(2^{n/2})\). On arbitrary graphs, \(\tau\) need not leave a linear fraction of \(n\) outside the exponent.','cover'),
 block(r'The 2025 paper explicitly retains the exact \(O^{*}(2^n)\) barrier and gives a faster factor-two approximation for directed cutwidth. Replacing each undirected edge by its two opposite arcs preserves every layout’s cut size, so the approximation also applies to this undirected objective; that observation does not make it exact.','approx'),
 ],
 progress=[
 progress('2013-12-11','The published seminar report states the all-graphs exponential-base question explicitly.'),
 progress('2014','The journal version records exact vertex-cover and bipartite speedups.','cover'),
 progress('2025-02-11','The approximation paper distinguishes faster factor-two computation from the still-open exact target.','approx'),
 progress(DATE,'The review fixes the vertex-count parameter and complete output semantics, and checks the scope of later approximation and structural results.'),
 ],
),notes,sources,status,summary=[
 'The cutwidth of a graph is the smallest possible maximum number of edges crossing a boundary between consecutive vertices in a linear ordering.',
 'The question asks for one deterministic algorithm computing this value on every graph in exponential time with a fixed base below two.',
 'The running-time exponent is measured in the number of vertices, with no promise about a smaller structural parameter.',
 'Faster exact algorithms for bipartite graphs and for graphs with a small vertex cover do not meet the unrestricted target.',
 'The checked 2025 progress gives a faster factor-two approximation, which does not determine the exact optimum.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
