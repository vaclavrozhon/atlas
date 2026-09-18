"""Select the source's easy-pattern-class question with explicit uncolored scope."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6025';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Subgraph detection with a sublinear treewidth exponent on some unbounded class',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a recursively enumerable class \(\mathcal H\) of finite simple undirected graphs with unbounded treewidth, a computable function \(f:\mathbb N_{\ge1}\to\mathbb N_{\ge1}\), a computable rational-valued function \(g:\mathbb N_{\ge0}\to\mathbb Q_{\ge2}\) with
\[
\lim_{t\to\infty}\frac{g(t)}t=0,
\]
and one uniform deterministic algorithm that, for every pattern \(H\in\mathcal H\) with \(k\ge1\) vertices and every host graph \(G\) with \(n\ge1\) vertices, decides whether \(G\) contains a subgraph isomorphic to \(H\) in at most
\[
f(k)(n+2)^{g(\operatorname{tw}(H))}
\]
bit operations? This is unweighted, uncolored, non-induced subgraph detection. The multiplicative factor may depend arbitrarily but computably on pattern size; the exponent must be sublinear in its treewidth.''',
 definitions=r'''Graphs have labeled vertices \([k]\) or \([n]\), no loops and no multiple edges. Input both full Boolean adjacency matrices, together with binary vertex counts. No tree decomposition or embedding is supplied. A subgraph embedding is an injective map \(\varphi:V(H)\to V(G)\) for which
\[
\{u,v\}\in E(H)\Longrightarrow\{\varphi(u),\varphi(v)\}\in E(G).
\]
Nonedges of \(H\) impose no restriction, so the copy need not be induced. There are no prescribed vertex colors, edge weights, labels constraining the embedding, or promises on the host beyond being a finite simple graph. If \(k>n\), the answer is no. The algorithm returns a decision bit; it need not count copies or output an embedding.

A tree decomposition of \(H\) is a finite nonempty tree \(T\) with a bag \(B_v\subseteq V(H)\) at each node, such that every graph vertex belongs to some bag, the two endpoints of every graph edge occur together in a bag, and for each graph vertex the tree nodes whose bags contain it form a connected subtree. Its width is \(\max_v|B_v|-1\). The treewidth \(\operatorname{tw}(H)\) is the minimum width. For nonempty edgeless graphs it is zero. The class has unbounded treewidth if for every integer \(M\ge1\) it contains a graph of treewidth at least \(M\).

A graph class is invariant under relabeling. Recursively enumerable means that some deterministic Turing machine, run without input, lists finite encodings of exactly its members, possibly with repetitions; every member eventually appears. Membership need not be decidable. The algorithm receives the whole pattern \(H\), not an unbounded advice string about it, and is promised that \(H\in\mathcal H\). One program must work for all members and hosts. It must halt on every valid graph pair, with its correctness and displayed time guarantee required on the promised pairs. Its running time includes reading the matrices, any preprocessing of \(H\), and writing the answer. Use a standard deterministic multitape Turing machine with finite alphabet; there are no random coins, oracles or advice.

The functions \(f,g\) and the graph-class enumerator are fixed with the algorithm. Their computability has no efficiency requirement. The limit means that for every real \(\eta>0\), there exists an integer \(t_0\) such that \(g(t)\le\eta t\) for all integers \(t\ge t_0\). No condition is imposed on how quickly \(t_0\) depends on \(\eta\). The lower bound \(g(t)\ge2\) accommodates the adjacency-matrix input and does not constrain the asymptotic sublinearity. A fixed factor improvement such as \(g(t)=0.9t\) does not qualify. Neither a bound only for average-case hosts nor a bound for one fixed pattern qualifies.

The assertion is unconditional. It is not a request merely to prove a lower bound assuming the Exponential Time Hypothesis, and it does not require classifying every pattern family. Colored subgraph detection, where each pattern vertex has a separate prescribed host color, is a different model unless an appropriate reduction preserving the selected class is proved.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of existence of the stated class, functions and algorithm. A positive answer must exhibit their effective descriptions and prove correctness, the time bound and unbounded treewidth. A negative answer must rule out every such class and uniform algorithm; a conditional lower bound must not be presented as an unconditional refutation. A fixed constant-factor reduction of the treewidth exponent, or a result only for colored copies without a class-preserving argument, is insufficient.',
 why='Treewidth controls the exponent of the generic dynamic-programming algorithm for subgraph detection. Finding an unbounded pattern class with a sublinear exponent would reveal a structural source of tractability that treewidth by itself misses.',
 importance=dict(score=84,method='editorial',reason='The question probes whether treewidth fundamentally governs the host-size exponent even after restricting the pattern family. It sits between general pattern-detection algorithms and structural lower bounds, rather than optimizing one fixed pattern.'),
 source_formulation=dict(text='After asking for a classification of maximally hard patterns, the source asks whether an unbounded-treewidth pattern class can admit a host-size exponent o(tw(H)). This card selects that concrete existence question, with ordinary uncolored subgraph detection, a recursively enumerable class and deterministic uniform bit computation. The recommendation was announced after the optional broad-classification-versus-existence question received no reply; it is an editorial specialization, not a received user confirmation.',caption='Bringmann–Slusallek, ICALP 2021, §3 final open question 3, p.40:13; §1.4 describes colored/uncolored transfers and their limits.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Current Algorithms for Detecting Subgraphs of Bounded Treewidth Are Probably Optimal','Karl Bringmann; Jasper Slusallek',2021,'https://doi.org/10.4230/LIPIcs.ICALP.2021.40','Introduction p.40:2; §1.4 Lemma 11 p.40:8; §3 final questions 2–3 p.40:13'),
 ref('marx','Can You Beat Treewidth?','Dániel Marx',2010,'https://doi.org/10.4086/toc.2010.v006a005','§6 pp.105–107, especially Corollaries 6.1–6.4 and the colored/uncolored distinction'),
 ref('linkage','Can You Link Up With Treewidth?','Radu Curticapean; Simon Döring; Daniel Neuen; Jiaheng Wang',2025,'https://arxiv.org/abs/2410.02606v2','Revision of 16 May 2025, §1.2: colorful detection, linkage capacity and Conjecture 1.7 pp.4–6; preliminary STACS 2025 Article 28'),
 ],
 context_blocks=[
 block('Color coding gives generic algorithms with exponent approximately tw(H)+1, apart from a computable pattern-size factor and logarithmic overhead. The 2021 source finds maximally hard examples under fine-grained hypotheses, then asks whether some unbounded classes are substantially easier.'),
 block('Marx’s general arbitrary-class lower bounds in Corollaries 6.1 and 6.2 concern partitioned subgraph isomorphism. His uncolored Corollary 6.4 additionally requires the patterns to be cores. These qualifications matter: the card does not claim that the same universal lower bound has been established for every uncolored pattern class.','marx'),
 block('Lemma 11 compares colored and uncolored algorithms across broader parameterized settings, but its reverse construction can change the pattern. A time guarantee only on an arbitrary chosen class cannot be transferred unless the transformed patterns remain in an appropriate class.'),
 block('The May 2025 linkage-capacity manuscript proves additional lower bounds for colorful detection and retains a conjecture about removing the logarithmic loss in treewidth-based lower bounds. These results support the broader structural program but do not resolve the selected unrestricted-host uncolored existence question.','linkage'),
 ],
 progress=[progress('2010','The treewidth lower-bound work distinguishes partitioned instances from the uncolored core-pattern specialization.','marx'),progress('2021-07','The source asks for an unbounded class with a sublinear treewidth exponent after proving hardness for selected patterns.'),progress('2025-05','The revised linkage-capacity work advances colorful-pattern lower bounds without supplying the class asked for here.','linkage')],
),[
 'Selected the source’s specific easy-class question as an announced editorial default after the optional target choice remained unanswered.',
 'Defined uncolored non-induced embeddings, explicit host and pattern input, tree decompositions and unbounded treewidth.',
 'Specified recursively enumerable classes, a uniform deterministic bit algorithm and computable pattern-dependent factors.',
 'Expanded little-o into its exact uniform asymptotic quantifiers and distinguished unconditional existence from conditional impossibility.',
 'Checked the original Marx corollaries and avoided an unsupported arbitrary-class colored-to-uncolored transfer; assessed importance and required complete Lean checking.',
],[
 'Read ICALP 2021 introduction, Lemma 11 and the entire final open-question list.',
 'Downloaded Marx 2010 and read §6 definitions, Corollaries 6.1–6.4 and the proof discussion restricting uncolored transfers to cores.',
 'Read the May 2025 linkage-capacity revision §1.2, including its colorful model and the treewidth conjecture. A publisher listing for a December 2026 journal issue was not treated as a newly checked future proof.',
 'Bounded primary-source searches through 18 September 2026 found no verified resolution of the selected class-existence question; restricted hosts and average-case detection results do not match it.',
], 'Source-open for the selected easy-pattern-class program in the bounded review through 18 September 2026. The card explicitly specializes to uncolored detection and effective classes. General colorful lower bounds and parameter-preserving reductions whose output patterns leave a selected class are not treated as a refutation. The original broad classification request has been narrowed editorially after an unanswered optional choice.',summary=[
 'The generic subgraph-detection algorithm has a host-size exponent controlled by the pattern’s treewidth.',
 'The selected question asks whether some effective class with unbounded treewidth admits an exponent that is sublinear in that treewidth.',
 'The pattern-size multiplier may be any computable function, but one deterministic algorithm must handle the whole class.',
 'Copies are uncolored and need not be induced, in completely arbitrary host graphs.',
 'Known colorful lower bounds require care because their transfers need not preserve an arbitrarily selected uncolored pattern class.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
