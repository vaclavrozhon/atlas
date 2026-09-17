"""Complete the deterministic static unit-cost tree-edit target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7374';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained exact unweighted edit distance on rooted ordered labelled trees and one deterministic almost-quadratic algorithm.',
 'Specified individual vertex edits, promotion of children on deletion, consecutive-child insertion and a fixed artificial super-root allowing intermediate forests.',
 'Expanded total input size, explicit labels and adjacency order, exact integer output and fully charged word-RAM instructions.',
 'Made the little-o quantifiers apply to the same program for every exponent slack, not a different program for each slack.',
 'Checked the 2025 static reduction and 2026 derandomization, and kept dynamic, weighted and low-distance results separate.',
 'Preserved importance 88 and required a complete Lean-checked binary answer.',
]
sources=[
 'Read Nogler–Polak–Saha–Vassilevska Williams–Xu–Ye, arXiv:2411.06502v3, 31 March 2025, STOC 2025: Introduction, edit operations, Table 1, Main Theorem 2 and Corollary 1.2. The unweighted algorithm reduces to bounded monotone min-plus product, with balanced-size exponent (3+omega)/2. The APSP equivalence concerns weighted TED. Ordered forests are explicitly permitted in the reduction. The live history lists v3 as latest.',
 'Read Jin–Park–Saha–Xu, Deterministic Monotone Min-Plus Product and Convolution, arXiv:2605.07150v2, 29 May 2026: abstract, Table 1, main theorem statements and Corollary 1.4. Their derandomization carries over to unweighted tree edit distance because the product oracle is its only randomized component. The resulting exponent remains above two. The live history lists v2 as latest; the ICALP 2026 publisher identifies Article 119.',
 'Read Hu–Nogler–Saha, ITCS 2026 Article 78, Hardness of Dynamic Tree Edit Distance and Friends: abstract, Introduction, Conjecture 2, Theorem 19 and Section 3 edit definitions. The unweighted lower bound is conditional, dynamic and restricted to combinatorial algorithms. Root deletion explicitly gives an ordered forest. This does not establish an unconditional static lower bound against arbitrary deterministic RAM algorithms.',
 'Read the primary abstract/history of Kociumaka–Shahali, arXiv:2507.02701v1, 3 July 2025, ESA 2025: O(n+k^6 log k) time concerns bounded distance k and does not give an almost-quadratic bound for arbitrary distances. Read the primary abstract of Moravec–Bača, arXiv:2609.03078v1, 2 September 2026: lower bounds there are practical distance-estimation filters, not complexity lower bounds or a faster exact general TED algorithm.',
 'Bounded primary-source later-work checks through 17 September 2026 located no verified resolution of the one-program deterministic n^(2+o(1)) target. The review checks definitions and theorem scope, not complete cited proofs or implementations.',
]
complete(identifier,dict(
 title='Almost-quadratic unweighted tree edit distance',criterion='resources',question_type='yes_no',
 formal=r'''Is there one uniform deterministic algorithm \(A\), an integer word-size constant \(B\ge8\), a constant \(K>0\), and a function \(g:\{2,3,\ldots\}\to[1,\infty)\) satisfying
\[
 \lim_{n\to\infty}\frac{\log g(n)}{\log n}=0,
\]
such that, for every two nonempty rooted ordered labelled trees with a total of \(n\ge2\) vertices, \(A\) outputs their exact unit-cost tree edit distance using at most
\[
 Kn^2g(n)
\]
word-RAM instructions in the worst case? Each vertex label is an integer in \(\{0,\ldots,n^2-1\}\), both trees are explicitly supplied, and the word length is \(B\lceil\log_2(n+2)\rceil\).''',
 definitions=r'''A rooted ordered tree has one designated root and a left-to-right order on the children of every vertex. It is supplied by explicitly listed vertex labels and ordered child lists. The parameter \(n\) is the sum of the numbers of ordinary vertices in the two input trees, not a bound on each tree separately. Vertex identifiers, labels and pointers each fit in one word. No balance, degree, depth, leaf-count, similarity or constant-alphabet promise is imposed.

To specify root edits without ambiguity, attach a permanent unlabelled super-root above each input root. It contributes no vertex to \(n\), cannot be edited, and is preserved in the final object. An intermediate object is an ordered forest of ordinary vertices below this super-root, possibly empty. Each of the following operations costs one:

1. Delete an ordinary vertex, replacing it in its parent's ordered child list by its own children in their existing order.
2. Insert one new labelled vertex as a child of an existing vertex or the super-root, placing beneath it a consecutive block of that parent's children. The block may be empty, in which case a leaf is inserted in a specified position.
3. Change the label of one ordinary vertex to another label from the input alphabet.

Insertion is the inverse of deletion. Deleting a vertex does not delete its descendants as a single operation. Moving or reordering a subtree is not a unit-cost operation. Intermediate ordinary labels belong to \(\{0,\ldots,n^2-1\}\). The final forest below the super-root must be a single rooted ordered labelled tree isomorphic to the second input, preserving all labels and sibling orders. Ordinary vertex identifiers themselves need not be preserved.

The distance \(\operatorname{TED}(T_1,T_2)\) is the minimum length of such an edit sequence. It is an integer between zero and \(n\): deleting every ordinary vertex and then inserting the target tree is always permitted. The output is this integer alone. No edit script, intermediate forest, alignment or approximate value is requested. This is a static computation on one pair of input trees, with no index or preprocessed dynamic state provided for free.

The algorithm is one finite sequential word-RAM program independent of the input size and trees. Unit-cost instructions are word reads and writes, copying, comparisons, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder with a nonzero divisor. Shifts by at least \(w\) return zero. All addresses and values fit in words; multiword computation pays for its constituent instructions. Every initialization, preprocessing step, table construction, arithmetic operation and output write is charged. There are no random instructions, advice, external oracles or free tables depending on size. There is no additional space restriction beyond this model and the charged running time.

The function \(g\) describes a subpolynomial overhead, not advice available to the program. Equivalently, the same algorithm has, for every fixed real \(\eta>0\), constants \(K_\eta,n_\eta\) such that its running time is at most \(K_\eta n^{2+\eta}\) whenever \(n\ge n_\eta\). A collection of unrelated algorithms, each with one chosen positive exponent slack, does not by itself establish this one-program assertion. The guarantee must hold on every valid input; it is not an average-case or expected-time bound.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the displayed proposition or its logical negation. A positive answer must provide one uniform deterministic program and prove that it returns the exact edit distance and satisfies the stated worst-case \(n^{2+o(1)}\) guarantee over all input trees.

A fixed exponent above two, merely subcubic time, an approximation, a small-distance promise, a restriction to paths or bounded-depth trees, or a dynamic amortized bound does not suffice. Complexity assumptions must be retained in any conditional lower bound. A conditional barrier for weighted costs or combinatorial dynamic algorithms is not an unconditional refutation of this unweighted static proposition. No additive numerical tolerance is applied.''',
 source_formulation=dict(text='The source line obtains faster exact unweighted tree edit distance through monotone min-plus multiplication and then derandomizes that approach. This card retains the stronger almost-quadratic static target, with uniform deterministic computation and the ordinary ordered-forest edit convention made explicit.',caption='Editorial almost-quadratic target grounded in the 2025 static algorithm and the 2026 deterministic extension.',citation='primary',format='editorial_paraphrase'),
 why='Tree edit distance compares hierarchical labelled data using local structural edits. An almost-quadratic exact algorithm would clarify how much ordered branching adds to the cost of ordinary string comparison and improve a basic structured dynamic-programming task.',
 references=[
 ref('primary','Faster Weighted and Unweighted Tree Edit Distance and APSP Equivalence','Jakob Nogler; Adam Polak; Barna Saha; Virginia Vassilevska Williams; Yinzhan Xu; Christopher Ye',2025,'https://arxiv.org/abs/2411.06502v3','31 March 2025 revision; Introduction, Main Theorem 2 and Corollary 1.2; STOC 2025'),
 ref('deterministic','Deterministic Monotone Min-Plus Product and Convolution','Ce Jin; Jaewoo Park; Barna Saha; Yinzhan Xu',2026,'https://arxiv.org/abs/2605.07150v2','29 May 2026 revision; Table 1 and Corollary 1.4; ICALP 2026 Article 119'),
 ref('dynamic','Hardness of Dynamic Tree Edit Distance and Friends','Bingbing Hu; Jakob Nogler; Barna Saha',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.78','Introduction, Conjecture 2, Theorem 19 and Section 3; dynamic and combinatorial scope'),
 ref('bounded','Faster Algorithm for Bounded Tree Edit Distance in the Low-Distance Regime','Tomasz Kociumaka; Ali Shahali',2025,'https://arxiv.org/abs/2507.02701v1','3 July 2025; primary abstract, distance-parameterized running time; ESA 2025'),
 ],
 context_blocks=[
 block('The order of siblings is part of the input, and deleting a vertex preserves its children. Different tree-edit conventions, especially deleting an entire subtree for one unit, define different distances.'),
 block('The 2025 algorithm improves the unweighted problem using bounded monotone min-plus multiplication. Its weighted APSP equivalence must not be transferred automatically to unit costs.'),
 block('The 2026 deterministic multiplication result also derandomizes unweighted tree edit distance. The reported exponent remains above two, so derandomization does not settle the almost-quadratic target.','deterministic'),
 block('Algorithms whose time depends strongly on a small edit distance can be much faster for similar trees. Their guarantees do not cover arbitrary input pairs at almost-quadratic cost.','bounded'),
 block('The 2026 unweighted dynamic barrier concerns updates, an unproved clique conjecture and combinatorial algorithms. It neither proves a static unconditional lower bound nor excludes the broader deterministic algorithm class used here.','dynamic'),
 ],
 progress=[progress('2025-03-31','The checked static revision obtains an unweighted bound based on the monotone min-plus exponent, substantially below cubic time.'),progress('2026-05-29','The deterministic monotone-product result transfers its derandomization to the unweighted tree-edit algorithm, still with an exponent above two.','deterministic')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified deterministic almost-quadratic algorithm for unrestricted static unit-cost ordered tree edit distance. The 2026 derandomization retains a larger exponent. The dynamic, weighted and small-distance results and the September practical filtering paper have different guarantees. This review checks mathematical scope and statements, not complete proofs.',summary=[
 'The inputs are two explicit rooted ordered trees with integer vertex labels.',
 'Unit-cost edits insert, delete or relabel individual vertices while preserving the order of surviving children.',
 'The target is the exact edit distance in almost-quadratic worst-case time using one deterministic program.',
 'Recent static and derandomization results improve the cubic bound but do not reach this target.',
 'A complete Lean-checked answer must prove or refute the proposition with the stated edit convention and quantifiers.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
