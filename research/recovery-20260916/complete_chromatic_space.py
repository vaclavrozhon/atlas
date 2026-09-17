"""Specify the deterministic base-two time and polynomial-space coloring target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6728'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the question immediately after Theorem 10.8 in §10.1.3, correcting the inherited §10.2 locator.',
 'Defined all finite simple graphs, exact chromatic number, one uniform deterministic algorithm, and simultaneous worst-case time and bit-space bounds.',
 'Fixed an explicit adjacency encoding and a multitape bit model; excluded advice, random error and unbounded unit-cost arithmetic.',
 'Distinguished the 2026 exponential-space improvement and fixed-color randomized algorithms from the all-graphs time-space target.',
 'Used the journal’s corrected 2.2356 base rather than the older preprint’s 2.2355 value.',
 'Assessed the canonical exponential-time/space tradeoff individually.',
]
sources=[
 'Read Parameterized Algorithms, author manuscript dated 30 May 2016: §10.1.3, Observation 10.7, recurrence (10.2), Theorem 10.8 and the following polynomial-space question, printed pp. 326–328/PDF pp. 342–344. The saved §10.2 locator referred to the next topic and is corrected.',
 'Read Gaspers–Lee, Faster Graph Coloring in Polynomial Space, published journal PDF, Algorithmica 85:584–609 (2023), online 11 October 2022: abstract, introduction’s inclusion-exclusion conversion, and concluding Theorem 1 for independent-set counting. The journal gives 1.2356 for counting and 2.2356 for coloring, differing from the older arXiv abstract.',
 'Checked the publisher abstract for Wu–Gu–Jiang–Shao–Xu, A space improved algorithm for chromatic number, Theoretical Computer Science 1059:115584, issue dated 4 January 2026; Crossref confirms authors and 2026 issue year despite 2025 in the DOI. The stated space is O*(2^(9n/25)), still exponential. Full article proof was not accessed or independently verified.',
 'Read Pratt, arXiv:2607.27159v1, 29 July 2026: abstract, Theorem 1 and §§1.1–2. The result is randomized, one-sided-error, and fixes the color count before the input size.',
 'Read Zamir, arXiv:2607.25973v2, 9 September 2026: introduction and §6 Discussion and open problems, PDF p. 27. It explicitly states that all known O*(2^n)-time chromatic-number algorithms use exponential space. The paper’s fixed-k and list-coloring results are not this target.',
 f'Bounded primary-source checks through {DATE} found no algorithm satisfying the exact simultaneous bounds. This does not independently certify the correctness of cited algorithms or exhaust the literature.',
]
status=('The textbook asks for the simultaneous time-space bound. A January 2026 article improves exponential space while preserving base-two time, and September 2026 work still states that known base-two chromatic-number algorithms use exponential space. The new randomized fixed-color results do not supply the requested deterministic all-graphs algorithm. No resolution was found in the bounded check.')
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Is there one uniform deterministic algorithm that computes the chromatic number of every \(n\)-vertex finite simple undirected graph in time \(O^{*}(2^n)\) and polynomial space?

Precisely, do there exist a deterministic machine \(A\) and fixed integers \(K\ge1,c,d\ge0\) such that, for every such graph \(G\), the machine outputs \(\chi(G)\), halts after at most
\[
K\,2^n(n+1)^c
\]
transitions, and uses at most
\[
K(n+1)^d
\]
work-tape cells throughout its computation? The graph encoding and computation model are defined below. Both bounds must hold for the same algorithm on the same input.''',
 definitions=r'''The input graph has vertex set \([n]=\{1,\ldots,n\}\), with \(n\ge0\), and an edge set consisting of unordered pairs of distinct vertices. There are no loops, parallel edges, weights or promises about the graph class. The input consists of \(1^n0\), followed by one adjacency bit for each pair \((i,j)\) with \(1\le i<j\le n\), in lexicographic order. Thus it has \(n+1+\binom n2\) bits. There are no trailing bits.

A proper \(q\)-coloring is a map \(h:[n]\to[q]\) such that \(h(i)\ne h(j)\) whenever \(\{i,j\}\) is an edge. The chromatic number is the least integer \(q\ge0\) for which such a map exists. In particular, \(\chi(G)=0\) for the empty graph and \(1\le\chi(G)\le n\) for a nonempty graph. The output is the ordinary binary encoding of this integer, using the string \(0\) for zero. A coloring itself is not required as output.

The computation model is a deterministic multitape Turing machine with a fixed finite program and finitely many tapes over fixed finite alphabets. It has a read-only input tape, initially blank work tapes and a write-only output tape. Heads start at cell zero; a transition reads or writes only the cells under the heads and moves each head by at most one cell. Tapes have nonnegative cell indices, with left moves at zero staying there. The time bound counts all transitions, including parsing, input access, arithmetic and output writing. Work space counts the total number of work-tape cells visited; the finite alphabets make this equivalent to bits up to a constant factor. The output tape is append-only and cannot serve as extra readable memory. The read-only input has polynomial length and does not affect the polynomial-space requirement.

There is no random source, advice depending on input length, oracle, unbounded-integer unit-cost operation or uncharged preprocessing. Malformed encodings must be rejected in time polynomial in their length. Constants and the machine are fixed once for all graphs and all \(n\). The bounds are worst-case bounds, not expected or average-case guarantees.

The notation \(O^{*}(2^n)\) suppresses only a factor polynomial in \(n\). A factor \(2^{o(n)}\) is not automatically permitted: for example, \(2^{n+\sqrt n}\) does not meet the displayed bound. A smaller exponential base does qualify if the same algorithm uses polynomial space.

The task is to determine the unrestricted chromatic number, so the number of colors may grow with \(n\). Separate algorithms for every fixed color count, with resources or advice depending on that count, do not by themselves give the required uniform bound. A procedure outputting a rational approximation to \(\chi(G)\) with proved absolute error at most \(1/100\) also yields an exact integer output by rounding; if it meets the stated resource bounds, this conversion incurs only polynomial overhead.''',
 answer_criterion=r'''Supply a complete Lean-checked algorithm and proofs of exact correctness, the \(K2^n(n+1)^c\) time bound and the \(K(n+1)^d\) space bound, or a complete Lean-checked proof that no such machine exists. Correctness must cover every finite simple graph, including inputs whose chromatic number grows with their size. A fixed-color algorithm, a randomized algorithm with possible error, an exponential-space construction, or a result conditional on an unproved hypothesis does not meet the target. The question asks for the existence of an algorithm with simultaneous resource bounds; approximate experimental running times or sampled graph tests are insufficient.''',
 source_formulation=dict(text='Immediately after the base-two time-and-space coloring theorem, the textbook asks whether the same running time can be attained with polynomial space.',
 caption='Paraphrase of the question after Theorem 10.8, §10.1.3, printed p. 327/PDF p. 343 of the author manuscript dated 30 May 2016.',
 citation='primary',format='editorial_paraphrase'),
 why='Fast exact coloring algorithms illustrate the power of storing information for all vertex subsets, but that table has exponential size. The question asks whether the time advantage survives when the algorithm can retain only polynomially many bits. A resolution would clarify a central time-space tradeoff in exact algorithms for graph partitioning problems.',
 importance=dict(score=84,method='editorial',reason='A canonical simultaneous time-space question for exact graph coloring, with long-standing algebraic and branching approaches and a clearly documented remaining gap even after 2026 progress.',assessed_on=DATE,basis='Individual reading of the textbook target, corrected journal polynomial-space bound and the latest fixed-color and space-improvement results.'),
 references=[
 ref('primary','Parameterized Algorithms','Marek Cygan; Fedor V. Fomin; Łukasz Kowalik; Daniel Lokshtanov; Dániel Marx; Marcin Pilipczuk; Michał Pilipczuk; Saket Saurabh',2016,
 'https://parameterized-algorithms.mimuw.edu.pl/parameterized-algorithms.pdf',
 'Author manuscript dated 30 May 2016; §10.1.3, Theorem 10.8 and following question, printed p. 327/PDF p. 343; published book 2015'),
 ref('polyspace','Faster Graph Coloring in Polynomial Space','Serge Gaspers; Edward J. Lee',2023,
 'https://link.springer.com/article/10.1007/s00453-022-01034-7',
 'Algorithmica 85:584–609, February 2023 issue; published online 11 October 2022; abstract, §1 and concluding Theorem 1'),
 ref('space','A space improved algorithm for chromatic number','Pu Wu; Huanyu Gu; Huiqin Jiang; Zehui Shao; Jin Xu',2026,
 'https://doi.org/10.1016/j.tcs.2025.115584',
 'Theoretical Computer Science 1059, Article 115584, 4 January 2026; publisher abstract, time and space bounds'),
 ref('fixed','k-Coloring is Faster than Computing the Chromatic Number','Or Zamir',2026,
 'https://arxiv.org/abs/2607.25973v2',
 'Version 2, 9 September 2026; introduction and §6, PDF p. 27, discussion of polynomial space'),
 ],
 context_blocks=[
 block(r'The textbook obtains \(O^{*}(2^n)\) time by storing counts associated with vertex subsets. The table occupies exponential space, so the time bound alone does not answer the question.'),
 block(r'The published Gaspers–Lee algorithm uses polynomial space and runs in \(O(2.2356^n)\) time. This supplies one side of the tradeoff but exceeds the requested exponential base.','polyspace'),
 block(r'The 2026 space improvement retains \(O^{*}(2^n)\) time and uses \(O^{*}(2^{9n/25})\) space. The smaller exponent is progress, but the memory bound is still exponential.','space'),
 block('The 2026 fixed-color algorithms improve the running-time base separately for each constant number of colors and use randomness. Their guarantees do not provide one deterministic algorithm with the requested memory bound for arbitrary chromatic number.','fixed'),
 block('The latest checked fixed-color paper explicitly lists removing randomness and achieving fast polynomial-space computation as further questions.','fixed'),
 ],
 progress=[
 progress('2016-05-30','The checked textbook manuscript records the base-two-time, polynomial-space question.'),
 progress('2022-10-11','The journal polynomial-space coloring algorithm is published online, with base 2.2356.','polyspace'),
 progress('2026-01-04','A new algorithm reduces exponential memory while preserving base-two time.','space'),
 progress('2026-09-09','The revised fixed-color paper still distinguishes the unresolved polynomial-space target.','fixed'),
 progress(DATE,'The review fixes the uniform deterministic bit model and checks recent coloring advances without finding the requested simultaneous bound.'),
 ],
),notes,sources,status,summary=[
 'The chromatic number is the minimum number of colors needed so that adjacent vertices receive different colors.',
 'The question asks for one deterministic algorithm computing it on every graph in base-two exponential time up to polynomial factors.',
 'The same algorithm must use only polynomially many bits of working memory.',
 'Known algorithms separately achieve base-two time with exponential memory or polynomial memory with a larger time base.',
 'Recent randomized algorithms for each fixed color count and improved exponential-space bounds do not meet the complete target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
