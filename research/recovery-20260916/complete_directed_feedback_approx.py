"""Complete the weighted general-digraph constant-approximation question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6591'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the approved minimum-weight, arbitrary-digraph target and its assessed importance 93.',
 'Specified nonnegative binary rational weights, actual feasible output, a uniform deterministic polynomial-bit-time algorithm and one universal multiplicative constant.',
 'Included two-cycles, empty graphs and zero optimum, and excluded graph-class, expected-cost and additive-error substitutes.',
 'Corrected the inherited generic reference metadata and distinguished the source approximation gap from its separate kernel question.',
 'Checked the conditional general hardness and the July and September 2026 approximation results for quasi-transitive digraphs.',
]
sources=[
 'Read Mnich–van Leeuwen, STACS 2016, Article 55, abstract and introduction pp. 55:1–2. The paper records the general O(log n log log n) approximation and asks whether it is best possible, separately from its kernelization discussion. It does not literally state the present weighted constant-factor specialization.',
 'Read Svensson, Theory of Computing 9(24):759–781 (2013), abstract and §1 pp. 759–762, including Theorem 1.1. The introduction explicitly discusses the weighted general approximation. The theorem establishes Unique-Games hardness of every constant factor, already for unit weights; this is conditional complexity evidence, not an unconditional nonexistence theorem.',
 'Read Ghorbani–Mnich, ICALP 2026, Article 96, abstract and §1 pp. 96:1–2, including Theorem 1 and the rational nonnegative node-weight convention. The 9/4 guarantee requires quasi-transitivity. This review did not independently verify the later algorithmic proof.',
 'Read Ghorbani–Mnich, arXiv:2609.16723v1 submitted 15 September 2026, abstract and §1, Table 1 and Theorems 1–2, printed pp. 1–2/PDF pp. 2–3. It claims deterministic (2+epsilon)-approximation on tournaments and node-weighted quasi-transitive digraphs for every fixed positive epsilon. The cover carries an earlier manuscript date; the progress date records the arXiv submission.',
 f'Bounded primary-source searches through {DATE} found special-class approximations and fixed-parameter exact algorithms, but no constant-factor approximation or unconditional impossibility proof for all weighted digraphs.',
]
status='The weighted constant-factor approximation question for arbitrary digraphs remains open in the checked sources. The general polylogarithmic guarantee and Unique-Games hardness leave this unconditional existence target unsettled. The 2026 constant-factor improvements require quasi-transitivity; the September improvement is a versioned preprint claim, not a general-digraph result.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a uniform deterministic polynomial-time constant-factor approximation for minimum-weight Directed Feedback Vertex Set on arbitrary finite directed graphs?

Precisely, do there exist one machine \(A\) and integers \(C,K,d\ge1\) such that, for every valid input \((D,w)\) of bit length \(L\), the machine halts within \(K(L+1)^d\) transitions and outputs a set \(F\subseteq V(D)\) satisfying
\[
D-F\text{ is acyclic},\qquad
\sum_{v\in F}w(v)\le C\,\operatorname{OPT}(D,w)?
\]
The same \(C,K,d,A\) must work for every graph and every allowed assignment of weights.''',
 definitions=r'''A directed graph is \(D=([n],E)\), where \(n\ge0\) and \(E\subseteq\{(u,v)\in[n]^2:u\ne v\}\). There are no loops or parallel copies of an arc, but both \((u,v)\) and \((v,u)\) may be present. There is no promise of planarity, bounded degree, bounded genus, quasi-transitivity or tournament structure.

A directed cycle consists of distinct vertices \(v_1,\ldots,v_r\), with \(r\ge2\), and arcs \((v_i,v_{i+1})\) for \(1\le i<r\) and \((v_r,v_1)\). The induced digraph \(D-F\) deletes the vertices in \(F\) and all their incident arcs. It is acyclic if it contains no directed cycle. A directed feedback vertex set is any \(F\) for which this holds. In particular, the two opposite arcs between a pair of vertices form a cycle.

Each vertex has a nonnegative rational weight \(w(v)\). Define
\[
\operatorname{OPT}(D,w)=
\min\left\{\sum_{v\in F}w(v):
F\subseteq[n]\text{ and }D-F\text{ is acyclic}\right\}.
\]
The minimum always exists because deleting all vertices is feasible. Zero weights are allowed. If the optimum is zero, the output must have weight zero as well; the guarantee has no additive slack. The empty graph has optimum zero.

For a nonnegative integer \(a\), let \(b(a)\) be the length of the ordinary binary expansion of \(a+1\), and encode \(a\) by \(1^{b(a)}0\) followed by those \(b(a)\) binary digits. Encode an instance by \(1^n0\), then the adjacency bits for all ordered pairs \((u,v)\), \(u\ne v\), in lexicographic order, then \(n\) pairs of integer codes \((p_v,q_v)\), where \(p_v\ge0\), \(q_v\ge1\) and \(w(v)=p_v/q_v\). A reduced fraction is not required. No trailing bits are allowed. All these bits contribute to \(L\); the running time may not depend polynomially on the numerical weights while ignoring their bit lengths.

The output is the \(n\)-bit incidence vector of an actual set \(F\). Feasibility is required on every input, as is the stated multiplicative cost guarantee. An estimate of the optimum without a feasible set, an expected-cost bound or a success probability below one is a different target.

The machine model is a deterministic multitape Turing machine with a fixed finite program, fixed finite tape alphabets, a read-only input tape, initially blank work tapes and an append-only output tape. A transition accesses the cells under the heads and moves each head by at most one cell. All transitions, including arithmetic, parsing and output, count toward the polynomial bound. There is no randomness, advice, oracle or uncharged preprocessing. Malformed encodings must be rejected in polynomial time. No complexity conjecture is assumed. Restricting the approximation constant to an integer loses nothing: any finite real factor can be rounded upward to an integer.''',
 answer_criterion=r'''Supply a complete Lean-checked construction of \(A,C,K,d\), proving polynomial bit complexity, feasibility and the constant-factor guarantee on every weighted digraph; or supply a complete Lean-checked proof that no such machine and constants exist. A conditional inapproximability theorem based on an unproved complexity conjecture does not establish the unconditional negative answer. An algorithm for a proper class of digraphs or for only unit weights does not establish the full positive answer. The target concerns existence of a fixed multiplicative approximation factor, not numerical estimation of the optimal possible factor.''',
 source_formulation=dict(
 text='The source records a polylogarithmic approximation for general Directed Feedback Vertex Set and asks whether the approximation can be improved. The approved proposal selects the precise constant-factor existence question and its minimum-weight version.',
 caption='Editorial specialization of the approximation gap in STACS 2016, Article 55, §1, retaining the weighted target of the approved research proposal.',
 citation='primary',format='editorial_paraphrase'),
 why='Deleting vertices to destroy every directed cycle is a basic optimization problem for cyclic dependencies. Its approximation behavior differs sharply from the undirected version: special directed graph classes admit constant factors, while the general case has resisted them and has strong conditional hardness. Resolving the unrestricted weighted target would clarify a central boundary of efficient approximation for directed graphs.',
 references=[
 ref('primary','Polynomial Kernels for Deletion to Classes of Acyclic Digraphs','Matthias Mnich; Erik Jan van Leeuwen',2016,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.55',
 'STACS 2016, Article 55, published 16 February 2016; §1, pp. 55:1–2, general approximation discussion'),
 ref('hardness','Hardness of Vertex Deletion and Project Scheduling','Ola Svensson',2013,
 'https://theoryofcomputing.org/articles/v009a024/',
 'Theory of Computing 9(24):759–781, published 26 September 2013; §1, pp. 759–762, especially Theorem 1.1'),
 ref('quasi','A 9/4-Approximation for Directed Feedback Vertex Sets in Quasi-Transitive Digraphs','Ebrahim Ghorbani; Matthias Mnich',2026,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.96',
 'ICALP 2026, Article 96, published 1 July 2026; abstract and §1, especially Theorem 1, p. 96:2'),
 ref('september',r'A deterministic \((2+\varepsilon)\)-approximation for directed feedback vertex sets in tournaments','Ebrahim Ghorbani; Matthias Mnich',2026,
 'https://arxiv.org/abs/2609.16723v1',
 'Version 1, submitted 15 September 2026; abstract, §1, Table 1 and Theorems 1–2, printed pp. 1–2/PDF pp. 2–3'),
 ],
 context_blocks=[
 block(r'The source discusses the general \(O(\log n\log\log n)\) approximation and the open gap in approximation quality. Its polynomial-kernel question concerns a separate parameterized resource target.'),
 block('Svensson proves Unique-Games hardness of approximation within any fixed constant, already in the unweighted case. This gives a major conditional barrier, but it is not an unconditional proof that the algorithm asked for here does not exist.','hardness'),
 block(r'The ICALP 2026 result gives a deterministic \(9/4\)-approximation for nonnegative node weights on quasi-transitive digraphs. Quasi-transitivity requires that whenever distinct vertices have arcs \(u\to v\to z\), at least one of \(u\to z\) and \(z\to u\) is present. Arbitrary digraphs need not satisfy this condition.','quasi'),
 block(r'The September 2026 preprint claims a deterministic \((2+\varepsilon)\)-approximation for every fixed \(\varepsilon>0\) on tournaments and, more generally, on node-weighted quasi-transitive digraphs. This improves the special-class factor without providing the all-digraph guarantee.','september'),
 ],
 progress=[
 progress('2013-09-26','The published hardness result establishes the conditional barrier to every constant factor.','hardness'),
 progress('2016-02-16','The source records the polylogarithmic general guarantee and the unresolved approximation gap.'),
 progress('2026-07-01','The quasi-transitive result supplies a deterministic 9/4 guarantee on that graph class.','quasi'),
 progress('2026-09-15','A preprint claims a factor arbitrarily close to two on the same broader class containing tournaments.','september'),
 progress(DATE,'The review preserves the arbitrary weighted-digraph target, specifies its bit model and distinguishes conditional hardness and graph-class progress.'),
 ],
),notes,sources,status,summary=[
 'A directed feedback vertex set deletes vertices so that no directed cycle remains.',
 'The question asks for one deterministic polynomial-time algorithm whose output weight is at most a fixed constant times the minimum possible weight.',
 'The guarantee must hold for every directed graph and every nonnegative rational assignment of vertex weights.',
 'General approximation remains polylogarithmic in the checked sources, and every constant factor faces a conditional Unique-Games hardness barrier.',
 'Recent constant-factor improvements apply to quasi-transitive digraphs and do not settle the unrestricted question.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
