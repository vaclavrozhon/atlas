"""Review the exact almost-linear global directed edge-cut endpoint."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7344';claim=read_claims(ROOT)[identifier]
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Retained exact global outgoing edge-cut optimization, positive polynomial integer capacities and a single uniform almost-linear randomized algorithm for each fixed weight exponent.',
 'Kept the (m+n) input-size convention, all-random-executions time bound and bounded-error guarantee.',
 'Specified the explicit input/output arrays, a word size large enough for exact cut values, and the difference between one uniform almost-linear algorithm and separate fixed-exponent algorithms.',
 'Read both recent approximation schemes and their inverse-precision dependence; exact integer recovery does not preserve their constant-precision running time uniformly.',
 'Checked the August 2026 incremental-cut result at the primary abstract level and retained its connectivity-threshold dependence.',
 'Removed background-only references from the status evidence, preserved importance and required a complete Lean-checked exact answer.',
]
sources=[
 'Read Quanrud, Approximating Directed Connectivity in Almost-Linear Time, arXiv:2512.00176v1, submitted 28 November 2025 (PDF cover dated 2 December 2025): abstract, Theorem 1.1 p.2, the paragraph about exact algorithms following Theorem 1.2 and the small-connectivity discussion p.3. The global edge-cut scheme uses an inverse-epsilon number of polylogarithmically many flow calls; the paper explicitly describes nearly linear exact algorithms as a further goal.',
 'Read Mosenzon, Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs, arXiv:2512.09080v3, 20 July 2026; first submission 9 December 2025: Introduction, Table 1 and Theorem 1.1 p.3. The theorem outputs a (1+epsilon)-approximate edge cut with probability at least one half in O(m^{1+o(1)} log W / epsilon) time. For polynomially bounded weights the logarithm is subpolynomial, but an inverse-polynomial accuracy requirement is not. No independent verification of the full proof is claimed.',
 'Read the primary arXiv abstract and version metadata of Saranurak–Xie–Zhou, Incremental Directed Minimum Cut by Dynamizing Gabow’s Algorithm, arXiv:2608.16382v1, 17 August 2026. It states deterministic O(k m log n) total time to maintain a cut under insertions or certify value at least k. This is threshold-dependent dynamic progress, not the unrestricted exact static endpoint. Only the abstract was reviewed.',
 'Bounded primary-source searches through 17 September 2026 found no verified exact almost-linear algorithm for all directed graphs in the selected weighted model. Approximate, rooted, single-terminal-pair, unit-weight-only and small-connectivity guarantees were distinguished.',
]
complete(identifier,dict(
 formal=r'''For every fixed integer \(a\ge1\), do there exist one uniform randomized algorithm \(A\), constants \(C\ge1\), an integer \(d\ge a+4\), and a function \(h:\mathbb N_{\ge2}\to[1,\infty)\) with
\[
\lim_{N\to\infty}\frac{\log h(N)}{\log N}=0,
\]
such that every allowed directed graph on \(n\ge2\) vertices and \(m\) arcs is processed in at most \(C(m+n)h(m+n)\) word-RAM instructions on every random execution? Arc weights are positive integers at most \(n^a\). With probability at least \(2/3\), the output must be a nonempty proper set \(S\subset V\) minimizing
\[
\sum_{(u,v)\in E:\ u\in S,\ v\notin S}w(u,v)
\]
over all such sets, together with its exact integer value. There are no prescribed terminals.''',
 definitions=old['definitions']+r'''

For the explicit encoding, supply \(n,m\) and an array of \(m\) triples \((u,v,w(u,v))\), with each field in one word. The output set is its \(n\)-bit incidence vector, packed into words, and the cut value is an integer word. Requiring \(d\ge a+4\) in the word size makes all input values and any cut sum fit, since \(m<n^2\). The algorithm may choose a larger fixed \(d\) for its addressing needs. Failed executions may return an incorrect answer or a failure symbol, but must respect the same instruction bound.

The quantifier order is \(\forall a\,\exists(A,C,d,h)\,\forall G\). In particular, one program and one overhead function must work for every input at that fixed weight exponent. A separate algorithm for each desired fixed saving or overhead exponent is not a replacement for this uniform almost-linear target. The set \(S\), rather than only an estimate of its weight, must be output on successful executions. No extra space restriction beyond charged computation and the word-addressing model is imposed.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive answer must provide the uniform algorithm, a subpolynomial overhead valid for all input graphs, exact cut and value correctness with the required probability, and a time bound on every random execution. A negative proof must rule out the full proposition unconditionally; a conditional lower bound proves only its conditional statement.

A constant-precision approximation, an algorithm whose time also grows polynomially with the optimum cut value, or a procedure for a supplied terminal pair does not settle this exact global target. Expected-time guarantees require a justified conversion to the stated worst-case bounded-error guarantee. No additive or relative tolerance in the cut value is allowed.''',
 source_formulation=dict(text='The recent directed-connectivity work obtains almost-linear relative approximation and identifies nearly linear exact algorithms as a further goal. This card retains the previously chosen exact endpoint for global outgoing cuts with positive polynomially bounded integer weights.',caption='Quanrud, Approximating Directed Connectivity in Almost-Linear Time, §1 after Theorem 1.2, pp.2–3; the explicit uniform model and exact-output endpoint are editorial specifications.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Approximating Directed Connectivity in Almost-Linear Time','Kent Quanrud',2025,'https://arxiv.org/abs/2512.00176v1','Submitted 28 November 2025; PDF cover 2 December 2025; Theorem 1.1 and following exact-algorithm discussion, pp.2–3'),
 ref('approx','Almost-Optimal Approximation Algorithms for Global Minimum Cut in Directed Graphs','Ron Mosenzon',2026,'https://arxiv.org/abs/2512.09080v3','Version 3, 20 July 2026; first submission 9 December 2025; Introduction, Table 1 and Theorem 1.1 p.3'),
 ref('incremental','Incremental Directed Minimum Cut by Dynamizing Gabow’s Algorithm','Thatchaphol Saranurak; Kaiyang Xie; Zhaienhe Zhou',2026,'https://arxiv.org/abs/2608.16382v1','17 August 2026; primary abstract, threshold-dependent incremental guarantee'),
 ],
 context_blocks=[
 block('The cut removes communication in one direction across a partition. Which partition is cheapest is part of the problem, unlike a minimum cut for two supplied terminals.'),
 block('Recent schemes give almost-linear time for any fixed relative approximation accuracy. Their runtime also contains an inverse-accuracy factor. That dependence matters when the answer must be an exact integer.','approx'),
 block(r'For an optimum integer value \(\lambda>0\), relative error below \(1/\lambda\) is enough to force an integral approximation to equal \(\lambda\). But paying inverse precision can then introduce a factor depending on \(\lambda\), which need not be subpolynomial. This explains why the reviewed approximation theorem does not automatically settle the target.','approx'),
 block(r'The August 2026 incremental algorithm has total update time \(O(km\log n)\) and maintains a minimum cut or certifies value at least a threshold \(k\). That threshold factor remains distinct from unrestricted exact almost-linear time.','incremental'),
 ],
 progress=[progress('2025-11-28','An almost-linear relative approximation scheme is stated for weighted directed edge and vertex connectivity, with an inverse-precision cost.'),progress('2026-07-20','The revised independent approximation paper states its global edge-cut theorem with explicit inverse-precision dependence.','approx'),progress('2026-08-17','A deterministic incremental result retains a connectivity-threshold factor in total update time.','incremental')],
),notes,sources,'The checked recent papers give almost-linear relative approximation or connectivity-dependent exact and incremental guarantees. Bounded primary-source checks through 17 September 2026 found no verified resolution of the unrestricted exact weighted endpoint. The uniform word-RAM statement is an explicit editorial target; the review does not independently validate all cited proofs.',summary=[
 'The input is a directed graph with positive polynomially bounded integer arc weights.',
 'The algorithm must find the cheapest outgoing cut over all nontrivial vertex partitions and output its exact value.',
 'The target is one uniform almost-linear randomized algorithm, with bounded error and a time limit on every execution.',
 'Recent almost-linear approximations pay for inverse precision, while threshold-dependent exact results retain an extra connectivity factor.',
 'A complete Lean-checked exact construction or unconditional refutation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
