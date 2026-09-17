"""Complete the selected infinite-family additive vertex-expansion target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-1008'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user choice of an infinite unbounded family of sizes, without requiring every size or a density bound on the size sequence.',
 'Expanded the original arbitrarily-large-constant-degree quantifier and required a single additive loss constant independent of the degree.',
 'Restored the source model of balanced bipartite multigraphs with numbered left-edge slots, distinct-neighbor vertex expansion and no right-regularity requirement.',
 'Defined full explicitness as uniform polylogarithmic bit-time neighbor evaluation for each fixed degree, with no size-dependent advice or free preprocessing.',
 'Separated the linear-size range of expanding sets from its degree-dependent density, and multiplicative loss from an absolute additive loss.',
 'Checked the 2025 constant-degree constructions and the September 2026 unbalanced result against these parameters; neither displayed theorem establishes the selected target.',
 'Preserved the previously assessed importance score 75 and required a complete Lean-checked construction or refutation.',
]
sources=[
 'Read Vadhan, Pseudorandomness, published December 2012 PDF: Definition 4.3 and Theorem 4.4, printed p. 82 (PDF 85); explicitness conventions, printed p. 103 (PDF 106); Open Problem 4.43, printed p. 116 (PDF 119). The source asks for arbitrarily large fixed degrees, not necessarily every integer degree.',
 'Read Hsieh–Lubotzky–Mohanty–Reiner–Zhang, Explicit Lossless Vertex Expanders, arXiv:2504.15087v1, submitted 21 April 2025: abstract, construction overview, §1.5 and Definition 2.1/Theorem 2.2/Remark 2.3, printed pp. 7–8. Theorem 2.2 states polynomial-time whole-graph construction and multiplicative (1-epsilon) expansion for degrees above epsilon-dependent thresholds. Section 1.5 discusses ultra-lossless edge expansion, which is not substituted for the present vertex target. Checked that v1 remains the listed arXiv version.',
 'Read Chattopadhyay–Gurumukhani–Ringach–Zhao, Two-Sided Lossless Expanders in the Unbalanced Setting, RANDOM 2026, Article 34: abstract, Definition 1, Theorem 2 and §1.2, pp. 34:1–34:3. Verified publisher date 9 September 2026 and DOI 10.4230/LIPIcs.APPROX/RANDOM.2026.34. The theorem has polynomial imbalance, polylogarithmic left degree and multiplicative loss, rather than the balanced fixed-degree additive-loss target.',
 f'Bounded primary-source searches through {DATE} also found Hambardzumyan et al., Spiky Rank and Its Applications to Rigidity and Circuits, ECCC TR26-030, §6.3 Theorem 6.5 p. 19 and discussion p. 26: its ultra-lossless vertex-expander application is conditional on a construction, not such a construction. This related sublinear-set-range statement is not treated as identical to Vadhan’s linear-range question. No resolution of the exact selected target was found.',
]
status='The original additive-loss construction question remains unresolved in the checked sources. The 2025 lossless constructions give a multiplicative loss with degree depending on the error parameter; the September 2026 construction addresses polynomially unbalanced graphs with nonconstant degree. Neither displayed result establishes a universal additive loss for balanced, fixed-degree, fully explicit families. This is a bounded literature check, not an exhaustive certification of open status.'
complete(identifier,dict(
 title='Fully explicit bipartite vertex expanders with constant additive loss',
 criterion='construction',question_type='yes_no',year=2026,
 formal=r'''Does there exist an integer \(C\ge1\) with the following property? For every integer \(D_0\ge1\), there is a fixed integer \(D\ge\max\{D_0,C+2\}\) and a fully explicit infinite family of bipartite multigraphs with \(N\) vertices on each side, left degree exactly \(D\), and
\[
 |\Gamma(S)|\ge(D-C)|S|\qquad
 \text{for all }S\subseteq[N]\text{ with }|S|\le\alpha_D N,
\]
where \(\alpha_D>0\) is independent of the family member? The available sizes \(N\) must be unbounded but need not include every positive integer. Full explicitness and all parameter dependencies are defined below.''',
 definitions=r'''For a positive integer \(N\), let \([N]=\{1,\ldots,N\}\). The left and right vertex sets are two disjoint copies of \([N]\). A graph is specified by a function \(g_N:[N]\times[D]\to[N]\): slot \(i\) of left vertex \(u\) is an edge to right vertex \(g_N(u,i)\). Different slots may give the same right vertex, so parallel edges are allowed and left degree counts multiplicity. Right degrees are unrestricted. The neighborhood is the set
\[
 \Gamma(S)=\{g_N(u,i):u\in S,\ i\in[D]\}.
\]
Its cardinality counts distinct right vertices, not edge slots. The condition is only on subsets of the left side. It imposes neither two-sided expansion nor a separate eigenvalue or unique-neighbor condition.

For each chosen degree \(D\), a family consists of a computable strictly increasing sequence of positive integers \(N_1,N_2,\ldots\), a rational constant \(0<\alpha_D\le1\), and one deterministic neighbor algorithm \(A_D\). On input \((N,u,i)\) in ordinary binary, with \(N=N_j\), \(u\in[N]\) and \(i\in[D]\), the algorithm outputs \(g_N(u,i)\) in at most
\[
 K_D\bigl\lceil\log_2(N+2)\bigr\rceil^{r_D}
\]
steps of a fixed finite-tape Turing machine, for constants \(K_D\ge1\) and integer \(r_D\ge1\). Every input/output bit operation and all preprocessing are charged. The program may depend on \(D\), but not on \(j\) or \(N\), and has no advice string, oracle or precomputed table depending on the graph size. This neighbor computation is the required full explicitness; merely printing an entire graph in polynomial time in \(N\) is weaker.

The size sequence must be generated by a total computable procedure; no efficiency or density condition is imposed on that procedure. The neighbor algorithm receives an available size \(N\), not an entire graph or a certificate of expansion. No graph or runtime guarantee is imposed at sizes outside the sequence. In particular, there is no requirement to supply all sufficiently large sizes, sizes within a bounded ratio of each other, or every power of two.

The universal loss \(C\) must work for unboundedly many degrees. For each such fixed \(D\), the positive set-density \(\alpha_D\), size sequence, neighbor program and its runtime constants may depend on \(D\), but not on the family index. Replacing a positive real density by a smaller rational one does not change the target. The statement does not require a single program taking an arbitrary degree as input or a family for every integer degree. These conventions express the source’s arbitrarily large constant degree and the user’s selected infinite-family size coverage.

For each family member the inequality must hold for every left set in the stated range, including the empty set. The density can decrease as the degree increases; it cannot decrease with \(N\) inside a fixed-degree family. Thus the expanding sets have size up to a positive linear fraction of \(N\) for that degree. In a guarantee \((1-\varepsilon)D\), the additive loss is \(\varepsilon D\). Choosing a small fixed \(\varepsilon\) while allowing unbounded \(D\) does not by itself bound this loss by a universal constant.''',
 answer_criterion=r'''Give a complete Lean-checked construction meeting the quantified statement, including proofs of the uniform neighbor runtime, unbounded effective size family and expansion for all required subsets, or give a complete Lean-checked refutation of that statement.

A probabilistic existence proof without the fully explicit neighbor algorithm does not meet the target. Neither does a construction for only bounded degrees, a loss growing with the degree, or expansion only for sets of sublinear size with no fixed positive density. A theorem whose admissible degree depends on an error parameter must justify that its parameters actually give a bounded additive loss. Numerical tolerance does not weaken the expansion inequality or the asymptotic resource requirement.''',
 source_formulation=dict(text='Open Problem 4.43 asks for explicit balanced bipartite expanders of arbitrarily large fixed left degree, expanding every set up to a positive linear size by the degree minus one universal constant. The user selected an infinite unbounded family of graph sizes rather than coverage of every size.',caption='Paraphrase of Vadhan, Pseudorandomness (2012), Open Problem 4.43, printed p. 116; explicitness convention on p. 103; size coverage selected by the user on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='These graphs would spread every small group of left vertices to nearly as many distinct neighbors as its edge budget permits, losing only a fixed amount per vertex even as the degree grows. Computing each neighbor locally would make this structure usable without first constructing a large graph.',
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf','Published December 2012 version; Definition 4.3 and Theorem 4.4 p. 82 (PDF 85); full explicitness p. 103 (PDF 106); Open Problem 4.43 p. 116 (PDF 119)'),
 ref('lossless2025','Explicit Lossless Vertex Expanders','Jun-Ting Hsieh; Alexander Lubotzky; Sidhanth Mohanty; Assaf Reiner; Rachel Yun Zhang',2025,'https://arxiv.org/abs/2504.15087v1','Version 1, 21 April 2025; abstract; §1.5 and Definition 2.1/Theorem 2.2/Remark 2.3, pp. 7–8'),
 ref('unbalanced2026','Two-Sided Lossless Expanders in the Unbalanced Setting','Eshan Chattopadhyay; Mohit Gurumukhani; Noam Ringach; Yunya Zhao',2026,'https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.34','RANDOM 2026, LIPIcs 392, Article 34, published 9 September 2026; abstract, Definition 1, Theorem 2 and §1.2, pp. 34:1–34:3'),
 ],
 context_blocks=[
 block('The textbook’s random-graph theorem already gives expansion with additive loss two for each fixed degree and a sufficiently small positive density. The question is therefore about efficiently and deterministically describing graphs with this quality, not their bare existence.'),
 block('Full explicitness lets an algorithm navigate a graph much larger than it can write down. This motivates measuring neighbor computation in the number of bits of a vertex label rather than in the number of vertices.'),
 block('The 2025 construction supplies constant-degree lossless vertex expanders, including bipartite variants, with degree thresholds depending on the chosen relative error. Its stated whole-graph runtime and multiplicative expansion theorem do not establish the stronger local-computation and constant-additive-loss requirements here.','lossless2025'),
 block('The September 2026 result proves two-sided lossless expansion for graphs with polynomial imbalance and polylogarithmic left degree. The paper itself separates that regime from balanced constant-degree families; its parameters do not settle this card.','unbalanced2026'),
 ],
 progress=[
 progress('2012','Open Problem 4.43 isolates the constant additive loss in a balanced fully explicit construction, beyond probabilistic existence and fixed relative-loss constructions.'),
 progress('2025-04-21','A preprint constructs constant-degree lossless vertex expanders with a fixed relative loss and degree depending on that loss; this does not establish a degree-independent additive loss.','lossless2025'),
 progress('2026-09-09','The RANDOM paper establishes two-sided lossless expansion in a polynomially unbalanced, nonconstant-degree regime.','unbalanced2026'),
 ],
),notes,sources,status,summary=[
 'The target is a balanced bipartite graph family in which every sufficiently small left set has at least D minus C times as many distinct right neighbors.',
 'One universal additive loss C must work for arbitrarily large fixed degrees D, while the positive density of expanding sets may depend on D.',
 'For each fixed degree, one deterministic algorithm must compute each numbered neighbor in time polynomial in the bit length of the vertex labels.',
 'The user selected an infinite effective family of unbounded sizes, without requiring every size or a dense size sequence.',
 'The checked recent multiplicative-loss constructions do not settle this target, which requires a complete Lean-checked construction or refutation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
