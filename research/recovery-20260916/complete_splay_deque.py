"""Complete the exact linear deque conjecture for bottom-up splaying."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6508';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the exact linear-total-cost conjecture, arbitrary initial tree and the four specified deque operations.',
 'Defined bottom-up splaying, rotations, the sequence cost and all quantifiers without leaving the machine primitives implicit.',
 'Charged extremal search as well as rotations and constant operation overhead; inserted extrema are made roots without an extra search.',
 'Allowed arbitrary valid interleavings and deletion to an empty tree, with no balance or monotone-deletion promise.',
 'Read Pettie’s explicit initial-n, m-operation theorem and the July 2026 splay preprint’s separate deque discussion.',
 'Kept almost-dynamic-optimality progress separate from a constant amortized deque theorem and preserved importance.',
 'Required a complete Lean-checked proof of the universal bound or its unbounded-ratio negation, with no numerical tolerance.',
]
sources=[
 'Read Pettie, Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture, arXiv:0707.2160v1, 14 July 2007, subsequently SODA 2008: Introduction p.2 specifies root insertion and extremal splay deletion; Theorem 5.1 p.9 states O((m+n) alpha-star(m+n)) for m operations starting from an n-node tree. This supplies the exact inherited operation convention and arbitrary-initial-tree scope.',
 'Read Chmel–Haeupler–Hladík–Koucký–Roeyskoe–Rozhoň–Sladký–Tarjan, Splay trees are almost dynamically optimal, arXiv:2607.18498v1, 20 July 2026: abstract, Introduction pp.1–2 and Appendix A deque bullet. It proves an O(log log n (log log log n)^2) competitive ratio for the general access problem and separately lists the deque conjecture with Pettie’s iterated-inverse-Ackermann bound. The general theorem is not asserted to prove constant amortized deque operations.',
 'Checked primary arXiv metadata and bounded subsequent-result searches through 17 September 2026. No verified resolution of the selected deque conjecture was found. A cached 2023 wait-free concurrent-deque paper was inspected and excluded as a different problem, not counted as progress on splay deques.',
]
complete(identifier,dict(
 formal=r'''Is there an absolute constant \(C\ge1\) such that, for every finite binary search tree \(T_0\) with \(n\ge0\) distinct ordered keys and every legal sequence \(\mathcal S\) of \(m\ge0\) deque operations, the specified bottom-up splay implementation satisfies
\[
W(T_0,\mathcal S)\le C(n+m)?
\]
The operations are insertion of a new minimum or maximum and deletion of the current minimum or maximum. Insertions make the new key the root; deletions splay the requested extremum to the root and remove it. The cost \(W\) counts operation overhead, search edges and rotations as defined below.''',
 definitions=r'''A binary search tree is a finite rooted tree with at most one left child and one right child per node. Each node carries a key; all keys in its left subtree are smaller, and all keys in its right subtree are larger. Keys are opaque elements of a totally ordered set and are used only through order comparisons. The initial tree may have any shape and is supplied as a tree, rather than built by charged insertions. The \(n\) term in the target is its allowed initial credit.

Insert-min supplies a key smaller than every currently present key. Allocate a new node with that key, no left child, and the former root as its right child; it becomes the root. Insert-max is symmetric. Both operations are allowed on an empty tree. Legality is promised, so no search to verify the new key’s extremal status is performed. A key that was deleted may be inserted again whenever the current extremal-order condition permits it.

Delete-min is allowed only on a nonempty tree. Follow left-child pointers from the root until reaching the leftmost node \(x\), splay \(x\) to the root, remove it and make its right child the root of the remaining tree. Delete-max follows right-child pointers, splays the rightmost node and retains its left subtree. Removing the only node leaves the tree empty. There are no searches for internal keys, other update operations, balance conditions or promises about the order of deletions.

A right rotation at a node \(p\) with left child \(x\) makes \(x\) replace \(p\), makes \(p\) the right child of \(x\), and makes the former right subtree of \(x\) the left subtree of \(p\), preserving all other attachments. A left rotation is the mirror image. Parent pointers and the root pointer are updated as needed. To splay \(x\), repeat until it is the root: if its parent \(p\) is the root, rotate \(x\) above \(p\) (zig); if \(x,p\) are both left children or both right children of their respective parents, first rotate \(p\) above its parent and then \(x\) above \(p\) (zig-zig); otherwise rotate \(x\) above \(p\) and then above its new parent (zig-zag). These are the standard bottom-up rules; the algorithm is fixed, not a choice among tree heuristics.

Let \(e\) be the total number of child edges traversed while finding extrema for deletions, and \(r\) the total number of single rotations performed by all splay steps. Define \(W=m+e+r\). A node has a constant number of child and parent pointers. Reading or changing one such pointer, comparing keys, allocating or deleting one node and executing a branch are constant-cost primitives. The standard direct implementation takes time within constant factors of \(W\), since each search edge, rotation and operation uses only a constant amount of additional work. Key bit lengths, memory-allocation system overhead and an alternative implementation’s avoidable extra work are not part of this combinatorial cost model.

The conjecture is a bound on the entire sequence, including sequences with insertions and deletions interleaved arbitrarily. It does not assert a constant worst-case cost for an individual deletion. The constant \(C\) must be independent of \(n,m\), all keys, the initial shape and the operation sequence. The empty sequence has cost zero.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed universal bound or its logical negation. A negative proof must show that for every proposed constant \(C\) there is a legal finite initial tree and sequence with \(W>C(n+m)\); equivalently, the cost ratio is unbounded over nonempty instances.

A constant-cost deque implemented by a different data structure does not answer this question. A slowly growing nonconstant amortized factor, a guarantee for only deletion sequences or special initial shapes, and a nonconstant competitive ratio against an optimal search tree do not establish the full linear bound. No additive approximation tolerance is allowed.''',
 source_formulation=dict(text='Tarjan’s deque conjecture, as stated by Pettie, says that splay-tree deque operations take constant amortized time. Pettie specifies new-root insertions and deletion by splaying the appropriate extremum. This card includes the initial-tree size explicitly, as in Pettie’s upper-bound theorem.',caption='Pettie, Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture, July 2007 preprint, Introduction p.2 and Theorem 5.1 p.9; SODA 2008.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Splay Trees, Davenport-Schinzel Sequences, and the Deque Conjecture','Seth Pettie',2007,'https://arxiv.org/abs/0707.2160v1','14 July 2007; Introduction p.2, operation convention; Theorem 5.1 p.9; published at SODA 2008'),
 ref('current','Splay trees are almost dynamically optimal','Petr Chmel; Bernhard Haeupler; Richard Hladík; Michal Koucký; Antti Roeyskoe; Václav Rozhoň; Ondřej Sladký; Robert E. Tarjan',2026,'https://arxiv.org/abs/2607.18498v1','20 July 2026; abstract, Introduction pp.1–2 and Appendix A deque discussion'),
 ],
 context_blocks=[
 block('A deque uses only the two extremes of an ordered set. Although a dedicated deque supports these operations easily, the conjecture concerns the behavior of the fixed splay-tree algorithm on every such sequence.'),
 block(r'Pettie proves \(O((n+m)\alpha^*(n+m))\) total time, where \(\alpha^*\) counts repeated applications of an inverse-Ackermann function until a fixed threshold is reached. Its growth is extremely slow but is not an absolute constant.'),
 block('The arbitrary initial tree matters: the first extremal deletion may traverse a long path. The additive initial-size allowance permits that cost while still asking for a linear bound over the whole sequence.'),
 block('The July 2026 preprint obtains a near-double-logarithmic competitive ratio for general splay accesses and separately records the deque conjecture. A nonconstant general competitiveness guarantee is not itself the constant amortized deque bound.','current'),
 ],
 progress=[progress('2007-07-14','The initial-tree-plus-sequence upper bound is reduced to a linear term times an iterated inverse-Ackermann factor; the result appears at SODA 2008.'),progress('2026-07-20','A preprint proves substantially improved general splay competitiveness while separately retaining the deque conjecture and its known nonconstant-factor bound.','current')],
),notes,sources,'The July 2026 primary preprint separately records the deque conjecture and the known iterated-inverse-Ackermann upper bound. Bounded primary-source checks through 17 September 2026 found no verified proof or counterexample for the exact linear target. The recent general competitiveness theorem is not treated as a resolution of this specific conjecture.',summary=[
 'Start with any binary search tree and update only the minimum or maximum end.',
 'New extrema become roots, while deleting an extremum first moves it to the root by standard bottom-up splaying.',
 'The conjecture asks whether total search and rotation work is linear in the initial size plus the number of operations.',
 'A known bound has an extremely slowly growing extra factor, and the 2026 general competitiveness result does not remove it here.',
 'A complete Lean-checked proof of the linear bound or an unbounded family of counterexample ratios is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
