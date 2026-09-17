"""Specify a tight decrease-key charge for the unchanged standard two-pass heap."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7328';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained determination of the full asymptotic rate up to constant factors, rather than replacing it by an improved-bound barrier.',
 'Fixed the standard left-to-right pairing and right-to-left assembly passes, link order, handles and decrease-key cuts.',
 'Defined the aggregate cost inequality on every finite sequence from empty heaps with a global live-item bound.',
 'Included make-heap in constant-cost operations and charged links, cuts and operation overhead explicitly.',
 'Clarified that comparison constants in a matching lower bound may depend on the competing admissible charge function, but never on N or a sequence.',
 'Read Iacono’s warning that amortized operation bounds from different analyses cannot simply be combined.',
 'Recorded the July 2026 standard-heap improvement as an announcement, while distinguishing its proved pure-heap bound and the still-open tightness gap.',
 'Preserved importance and required a complete Lean-checked upper analysis and matching lower bound.',
]
sources=[
 'Read Tarjan–Xu, Pure Pairing Heaps, arXiv:2607.23118v1, 25 July 2026: abstract, Introduction pp.1–2, Section 2 pp.3–4 with the exact standard two-pass algorithm, and Section 10 p.21. The proved pure-heap decrease-key bound is O(log log n log log log n). The conclusion announces O((log log n)^2 log log log n) for standard heaps in a forthcoming companion paper and explicitly retains a tightness gap. No proof of that announced standard-heap result is supplied in this paper.',
 'Read Iacono, Improved Upper Bounds for Pairing Heaps, arXiv:1110.4428v1, 20 October 2011, an expanded account of earlier SWAT 2000 work: abstract, Introduction, Figure 1 p.2 and subsequent comparison pp.2–3. It gives constant amortized insert/meld with logarithmic extract-min and decrease-key. Figure 1 explicitly warns that amortized charges for different operations cannot be mixed between analyses. This verifies that the selected charge convention has admissible upper bounds.',
 'Read Pettie, Towards a Final Analysis of Pairing Heaps, Dagstuhl Seminar Proceedings 06091.5, published 30 November 2006, corresponding to FOCS 2005 work: abstract, Introduction Theorem 1, standard heap description and Section 5. This gives sublogarithmic charges to insert, meld and decrease-key simultaneously, with logarithmic delete-min. It is not asserted here to preserve constant insertion/meld charges. The downloaded PDF has corrupted mathematical font extraction, so the exponent is not reconstructed from garbled text; Iacono’s Figure 1 supplies the legible comparison.',
 'The Fredman 1999 lower bound is recorded from its explicit descriptions in the primary Iacono and Tarjan–Xu papers, not from a newly read full original proof. Both identify a logarithmic-logarithmic decrease-key obstruction under the other-operation bounds. This review does not independently verify that lower-bound proof.',
 'Bounded primary-source searches through 17 September 2026 found no verified tight analysis or independently checked companion proof resolving this target. Results for pure, multipass, lazy, smooth, slim or rank-pairing variants were distinguished from the specified algorithm.',
]
complete(identifier,dict(
 formal=r'''Determine an explicit asymptotic growth rate \(f:\mathbb N_{\ge1}\to[1,\infty)\) that is a tight amortized decrease-key charge for the standard two-pass pairing heap. For every finite legal operation sequence \(\mathcal S\) starting from empty heaps and having at most \(N\) live items in all heaps combined, require
\[
W(\mathcal S)\le C\bigl(a(\mathcal S)+b(\mathcal S)\log_2(N+2)+c(\mathcal S)f(N)\bigr)
\]
for one absolute \(C\). Here \(a\) counts make-heap, insert, meld and find-min operations, \(b\) counts delete-min operations, and \(c\) counts decrease-key operations. Tightness means that every charge function satisfying such an inequality is \(\Omega(f(N))\), with the quantifiers specified below. The algorithm itself and the other-operation charges are fixed.''',
 definitions=r'''Each heap is empty or is a single rooted tree of items. Every item has an opaque key in a totally ordered set and a stable identity. Ties are resolved by a fixed total order on identities, so every comparison has a deterministic winner. A parent’s key, including this tie-breaking order, is no greater than a child’s. Children form a left-to-right list. A link of two disjoint trees compares their roots and makes the losing root the new leftmost child of the winner. A cut removes one parent-child edge and detaches the entire child subtree while preserving the order of remaining children.

Make-heap creates an empty heap. Find-min returns its root, or an empty marker. Insert creates a new singleton item, links it with the heap’s root if present and returns a stable item handle. Meld takes two distinct item-disjoint heaps, links their roots when both are nonempty and returns the resulting heap, invalidating the old heap handles. If either is empty, the other tree is returned. Item handles remain valid until their items are deleted, including through melds.

Decrease-key receives a heap handle, a handle to an item in it and a new key no larger than its old key. Replace the key. If the item is not the root, cut its entire subtree and link that subtree to the heap root, even if no heap-order violation would have occurred without the cut. If it is the root, no link or cut is needed. The operation’s inputs and membership promises are supplied, so searching for the item is not required.

Delete-min requires a nonempty heap. Remove its root and detach its children into their existing ordered root list. In the pairing pass, link the first and second roots, then the third and fourth, and so on from left to right, leaving a final unpaired root unchanged. The resulting trees retain their pair order. In the assembly pass, start with the rightmost resulting tree and repeatedly link it to the next tree to its left, moving right to left until one tree remains. This becomes the heap. If the deleted root had no children, the result is empty. Changing the order of either pass, omitting the assembly pass, adding rank-driven restructuring or using multiple retained trees defines a different heap.

A direct pointer implementation stores a constant number of fields per item, including the key and enough child, sibling and parent information for a cut given a handle in constant time. Comparisons of keys or identities, pointer reads and writes, branches and allocating or releasing a constant-size record are unit-cost primitives. There is no arithmetic on keys and no hidden balancing operation. Let \(\lambda\) be the number of links and \(\chi\) the number of edges cut, including child edges detached during delete-min. Define
\[
W(\mathcal S)=a(\mathcal S)+b(\mathcal S)+c(\mathcal S)+\lambda+\chi.
\]
This is within constant factors of the work of the specified direct implementation. Only this fixed sequential deterministic algorithm is being analyzed.

The integer \(N\ge1\) is a global upper bound on simultaneously live items throughout the sequence, not its total insertions, length, number of heap objects or final size. Sequences may create arbitrarily many heaps, interleave operations on them, merge them and leave items undeleted at the end. Every operation contributes to its count, even if it returns an empty result or changes no key value. The inequality must hold for every \(N\) and every sequence obeying that live-item bound, with no uncharged initial nonempty heaps or additive credit depending on the sequence.

Call any function \(d:\mathbb N_{\ge1}\to[1,\infty)\) admissible if there exists a constant \(C_d\ge1\) such that the displayed inequality holds with \(d\) in place of \(f\), for all \(N\) and all permitted sequences. A tight answer consists of an explicit rate \(f\) which is admissible and satisfies
\[
\forall d\text{ admissible}\ \exists k_d>0\ \exists N_d\ge1\ \forall N\ge N_d:\quad d(N)\ge k_d f(N).
\]
The lower-comparison constants may depend on \(d\) and its admissibility constant, but not on \(N\) or a chosen sequence. Requiring one fixed lower-comparison constant for every rescaling of every admissible function would be inappropriate. No specific conjectured rate is imposed.''',
 answer_criterion=r'''Supply an explicit asymptotic rate and a complete mathematically correct Lean-checked proof of both admissibility and the matching universal lower statement. A characterization that merely renames the worst sequence cost or repeats the definition of admissibility is not a determination of the rate. Constants hidden by asymptotic notation must have the dependencies specified above.

A better upper bound without matching tightness does not complete the task. Neither does a tight bound for another heap variant, or an analysis that increases the allowed insert or meld charge without proving the displayed inequality. Amortized bounds for individual operations from separate analyses cannot be combined without a simultaneous total-cost proof. This is an asymptotic classification up to constant factors, not a finite numerical approximation task.''',
 source_formulation=dict(text='The long-standing question is the tight amortized complexity of decrease-key in the standard pairing heap. The 2026 pure-heap paper explicitly separates the standard algorithm and retains the gap between known lower bounds and its announced improvement. This card fixes the other-operation charges and asks for the complete asymptotic rate.',caption='Tarjan–Xu, Pure Pairing Heaps (25 July 2026), Introduction, §2 and §10; the constant insert/meld convention is checked against Iacono’s analysis.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Pure Pairing Heaps','Robert E. Tarjan; Xiaoyang Xu',2026,'https://arxiv.org/abs/2607.23118v1','25 July 2026; Introduction pp.1–2, standard algorithm in §2 pp.3–4, announcement and remaining gap in §10 p.21'),
 ref('charges','Improved Upper Bounds for Pairing Heaps','John Iacono',2011,'https://arxiv.org/abs/1110.4428v1','20 October 2011 expanded account of earlier SWAT 2000 work; Introduction and Figure 1 pp.2–3, simultaneous charge conventions'),
 ref('sublog','Towards a Final Analysis of Pairing Heaps','Seth Pettie',2006,'https://doi.org/10.4230/DagSemProc.06091.5','Published 30 November 2006, corresponding to FOCS 2005 work; Introduction Theorem 1 and §5, with nonconstant insert/meld charges'),
 ref('lower','On the Efficiency of Pairing Heaps and Related Data Structures','Michael L. Fredman',1999,'https://doi.org/10.1145/320211.320214','Decrease-key lower bound; scope checked through its descriptions in the Iacono and Tarjan–Xu primary papers, not a new full-proof audit'),
 ],
 context_blocks=[
 block('The immediate decrease-key operation uses only a constant number of pointer changes. Its amortized charge measures the extra work these changes can cause during later delete-min operations.'),
 block('A logarithmic-logarithmic lower bound rules out the original constant-amortized expectation under the relevant other-operation charges. This review records it through the later primary papers’ statements of Fredman’s result.','lower'),
 block('Iacono’s analysis gives constant insert and meld charges with logarithmic delete-min and decrease-key. Its comparison table explicitly warns against combining operation charges from unrelated amortized analyses.','charges'),
 block('Pettie’s sublogarithmic analysis also charges insert and meld a nonconstant amount. That result alone is not a simultaneous upper bound under this card’s constant-charge convention.','sublog'),
 block(r'The July 2026 paper proves \(O(\log\log N\,\log\log\log N)\) for pure heaps and announces \(O((\log\log N)^2\log\log\log N)\) for standard heaps in forthcoming work. The announcement and the remaining tightness question are distinct; no companion proof was independently checked.'),
 ],
 progress=[progress('1999','Fredman establishes a logarithmic-logarithmic decrease-key obstruction, as described in the later primary sources.','lower'),progress('2000','Iacono’s work establishes constant insert/meld charges while allowing logarithmic decrease-key; the expanded account appears on arXiv in 2011.','charges'),progress('2005','Pettie obtains sublogarithmic charges for insert, meld and decrease-key, retaining logarithmic delete-min.','sublog'),progress('2026-07-25','Pure heaps receive a near-log-log analysis; an improved standard-heap bound is announced, and a matching bound remains open.')],
),notes,sources,'The July 2026 source explicitly retains the tightness gap and distinguishes its proved pure-heap analysis from an announced standard-heap improvement. Bounded primary-source searches through 17 September 2026 found no verified tight analysis under the stated simultaneous charges. No independent verification of the announced companion proof or Fredman’s full lower-bound proof is claimed.',summary=[
 'The standard pairing heap performs a left-to-right pairing pass and a right-to-left assembly pass when deleting the minimum.',
 'The question asks for the tight asymptotic amortized cost of decrease-key while keeping the stated charges for all other operations.',
 'The bound must hold on every finite sequence from empty heaps, in terms of the maximum simultaneous live-item count.',
 'Different heap variants and operation charges from separate analyses cannot be substituted; a 2026 improvement for standard heaps is recorded as an announcement.',
 'A complete Lean-checked upper analysis and matching lower bound are required, not just another improvement.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
