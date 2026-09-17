"""Review the complete specified suffix-tree interface in O(r) total words."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7375';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the imported binary-text specialization, enumerated interface, deterministic uniform model, polynomial construction and O(r) total space target.',
 'Defined zero-based suffix ranks, the cyclic BWT predecessor, interval node handles, all query domains and returned values, including string depth at leaves.',
 'Separated polynomial construction workspace from the run-linear retained representation and temporary query workspace; all retained text and any access oracle count.',
 'Replaced the short 2017 source as the main theorem locator with the full 2019 revision, Theorem 9, Tables 3–4 and conclusion, later published in JACM 2020.',
 'Checked the July 2026 path-decomposition theorem: its O(r) space is additional to a text/LCE oracle and its stated interface omits several required operations.',
 'Corrected the non-overlapping paper’s conference provenance to SPIRE 2023, distinguished its 2024 repository posting and 2025 journal publication, and recorded access limits.',
 'Preserved importance 79 and the Lean-checked binary answer criterion; did not restore any separate character-access-only card.',
]
sources=[
 'Read Gagie–Navarro–Prezza, arXiv:1809.02792v2, revised 4 July 2019, later JACM 67(1), Article 2 (2020), DOI 10.1145/3375890: abstract, Sections 5–6, Theorem 9, Tables 3–4, construction discussion and concluding open questions on p.44. The full suffix-tree bound retains O(r log(n/r)) words; the table includes parent, tree depth, LCA and suffix links. The live arXiv history lists v2 as latest.',
 'Read Becker et al., ICALP 2026 Article 24, published 1 July 2026, full primary HTML: Introduction, Theorem 2, Corollary 3 and Sections 2.1.1–2.1.3. Its O(r) words exclude the text oracle supporting access and LCE. Its theorem does not provide parent, LCA, tree depth or suffix-link operations. The stated uncompressed oracle uses n log(sigma)+O(log n) bits. Checked the linked arXiv:2506.14734 history through v6 of 5 May 2026; did not independently audit all construction proofs.',
 'Read Tsuruzono–Arimura–Inenaga, arXiv:2607.01636v1, 2 July 2026: abstract and Section 2, pp.3–4. Its CDAWG construction assumes the older full suffix-tree black box, with O(r log(n/r)) space; it is not a new O(r)-space complete interface.',
 'Read Cenzato et al., Suffixient Arrays: A New Efficient Suffix Array Compression Technique, full primary Springer HTML, published 11 September 2026, DOI 10.1007/s00224-026-10287-6: abstract, Section 1.1 and Theorem 19. Its pattern-location guarantee assumes random access to the text and is not the complete interface here; the reverse-text run parameter is also distinguished from the card’s forward BWT run count.',
 'Checked the primary SPIRE 2023 proceedings record and the accessible indexed first page of Gibney–Macnichol–Thankachan, pp.260–270, DOI 10.1007/978-3-031-43980-3_21; the NSF full-PDF endpoint timed out, so its Section 3.1 was not newly read. The SSRN posting is 27 April 2024. Checked the primary journal abstract/metadata for TCS 1056, 115512, 21 November 2025, DOI 10.1016/j.tcs.2025.115512, but did not access its complete proof. Its non-overlapping-pattern reporting target is narrower than a full suffix-tree interface.',
 'Bounded later-work searches through 17 September 2026 located no verified resolution of the precise combined interface and total-space target. Newer results with a separate text oracle do not by themselves establish that target. This is a statement/scope review, not independent certification of every cited proof.',
]
complete(identifier,dict(
 title='Fully functional suffix trees in BWT-run-linear total space',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist constants \(C,K>0\), integers \(c\ge0\), \(p\ge1\), \(B\ge8\), and one uniform deterministic static data structure such that, for every \(n\ge2\) and every explicitly given text
\[
T\in\{0,1\}^{n-1}\#,
\]
it constructs a representation of the compact suffix tree in at most \(Kn^p\) word-RAM instructions, retains at most \(Cr\) words, and answers each operation specified below exactly in at most
\[
K\bigl(\log_2(n+2)\bigr)^c
\]
worst-case instructions, while the retained representation together with all temporary query work uses at most \(Cr\) words? Here \(r\) is the number of runs in the Burrows–Wheeler transform of \(T\), including its unique sentinel, and the word length is \(B\lceil\log_2(n+2)\rceil\). All constants and programs are chosen once, independently of the text and its length.''',
 definitions=r'''Text positions and suffix ranks are zero-based. The alphabet is ordered \(\#<0<1\); the sentinel \(\#\) occurs only at position \(n-1\). For \(0\le i<n\), the suffix beginning at \(i\) is \(T[i]\cdots T[n-1]\). The suffix array \(\operatorname{SA}[j]\) is the starting position of the suffix of lexicographic rank \(j\), and \(\operatorname{ISA}[i]\) is the unique rank \(j\) with \(\operatorname{SA}[j]=i\). Define
\[
\operatorname{BWT}[j]=T[(\operatorname{SA}[j]-1)\bmod n].
\]
The residue lies in \(\{0,\ldots,n-1\}\). A run is a maximal nonempty interval of equal symbols in this BWT array; \(r\) is its number of runs. The sentinel is counted in both \(n\) and \(r\).

The suffix trie contains the paths spelling all \(n\) suffixes, with the empty string at its root. Contract maximal paths whose intermediate vertices have just one child, concatenating their edge labels. The resulting compact suffix tree retains the root, branching vertices and leaves. Every edge has a nonempty string label. A node's path label is the concatenation of edge labels from the root to that node. Leaves are ordered by suffix rank. Every node is represented externally by the pair \([l,h]\) of smallest and largest ranks among its descendant leaves. These intervals uniquely identify explicit nodes; an interior point of an edge is not an additional queryable node. In particular, the root is \([0,n-1]\) and leaf rank \(j\) is \([j,j]\).

The complete required interface consists of the following operations. Node arguments are valid node intervals of the indexed text; ranks and positions lie in \(\{0,\ldots,n-1\}\).

- Return the root, or return the leaf of a supplied suffix rank.
- Given a node, return its parent, its lexicographically first child, or its next sibling in its parent's child order. Children are ordered by the first symbols of their edge labels. Return a distinguished marker \(\bot\) when the requested parent, child or sibling does not exist; in particular the root has no parent or sibling.
- Given a node and a symbol \(a\in\{\#,0,1\}\), return its child whose edge label begins with \(a\), or \(\bot\) if there is no such child.
- Given any node, return its tree depth, the number of edges from the root, or its string depth, the number of symbols in its path label. Both root depths are zero. A leaf for suffix position \(i\) has string depth \(n-i\).
- Given two nodes, return their lowest common ancestor, namely their common ancestor of maximum tree depth. A node is its own ancestor.
- Given a nonroot internal node with path label \(aU\), return its suffix link: the explicit node whose path label is \(U\). This node exists in this suffix tree; \(U\) may be empty, in which case the answer is the root. No suffix-link query on a leaf or on the root is required.
- Given \(j\), return \(\operatorname{SA}[j]\); given \(i\), return \(\operatorname{ISA}[i]\) or \(T[i]\).

Every query returns only a constant number of words. Arbitrary valid node intervals can be supplied directly; handles are not required to originate from a preceding traversal. Every operation must work after construction with no access to an uncounted input copy or external text-access service. All retained text, suffix samples, lookup tables, oracle implementations and internally retained handles count toward the space bound. Temporary query memory, including registers, also counts. Externally supplied arguments and the constant-size returned result may be excluded. Construction starts from the explicitly supplied text, one symbol per word, and may use additional temporary memory; construction instructions and initialization are charged to its polynomial time bound. That temporary memory is discarded before queries begin.

The machine is a sequential word RAM with a fixed finite program and the stated word length. Unit-cost instructions are word reads and writes, copying, comparisons, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder for a nonzero divisor. A shift by at least \(w\) returns zero. Values and addresses fit in words, and multiword operations pay for their constituent instructions. There is no randomness, nonuniform advice, uncharged preprocessing, free size-dependent table or input-dependent oracle. A static query starts without input-dependent private state outside the counted representation. The bounds hold for every text and every valid query, without amortization over a query sequence.

The binary alphabet and this explicitly enumerated interface are the retained editorial specialization of the broader suffix-tree question. “Fully functional” here means exactly these operations; no unlisted operation is silently required.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation. A positive answer must provide the uniform construction and all query algorithms, prove their exact behavior, and prove the simultaneous polynomial construction, run-linear total space and polylogarithmic worst-case query bounds.

A structure supporting only pattern counting, occurrence reporting or a proper subset of the required interface is insufficient. Space charged in addition to a separately stored text or access oracle does not establish the total-space target unless that additional representation is also included in the proved \(Cr\) bound. An extra logarithmic space factor does not meet the target. A conditional lower bound establishes only its conditional conclusion. There is no additive numerical tolerance on this existence question.''',
 source_formulation=dict(text='The full r-index treatment asks which text-access and suffix-array/tree capabilities can be supported in O(r) space, having obtained full tree functionality in O(r log(n/r)) words. This card retains the previously imported binary-text specialization and exact list of required operations; it does not assert equivalence to every possible suffix-tree interface.',caption='Gagie–Navarro–Prezza, 2019 revision, Section 6, Theorem 9, Tables 3–4 and concluding questions on p.44.',citation='primary',format='editorial_paraphrase'),
 why='A complete navigation index lets algorithms work directly on highly repetitive text without retaining an expanded tree. The question is whether this general interface, including direct suffix and text access, can fit at the same run-count scale as more specialized search indexes.',
 references=[
 ref('primary','Fully-Functional Suffix Trees and Optimal Text Searching in BWT-runs Bounded Space','Travis Gagie; Gonzalo Navarro; Nicola Prezza',2019,'https://arxiv.org/abs/1809.02792v2','4 July 2019 revision; Sections 5–6, Theorem 9, Tables 3–4, p.44 concluding questions; JACM 67(1), Article 2 (2020), DOI 10.1145/3375890'),
 ref('paths','Compressing Suffix Trees by Path Decompositions','Ruben Becker; Davide Cenzato; Travis Gagie; Ragnar Groot Koerkamp; Sung-Hwan Kim; Giovanni Manzini; Nicola Prezza',2026,'https://doi.org/10.4230/LIPIcs.ICALP.2026.24','ICALP 2026 Article 24, published 1 July; Theorem 2, Corollary 3 and Sections 2.1.1–2.1.3; O(r) additional space and explicit oracle assumptions'),
 ref('cdawg','Output-Sensitive Construction of CDAWGs from BWT-Runs','Yuta Tsuruzono; Hiroki Arimura; Shunsuke Inenaga',2026,'https://arxiv.org/abs/2607.01636v1','2 July 2026; abstract and Section 2, pp.3–4, assumed compressed suffix-tree interface'),
 ref('suffixient','Suffixient Arrays: A New Efficient Suffix Array Compression Technique','Davide Cenzato; Lore Depuydt; Travis Gagie; Sung-Hwan Kim; Giovanni Manzini; Francisco Olivares; Nicola Prezza',2026,'https://doi.org/10.1007/s00224-026-10287-6','Theory of Computing Systems 70, Article 50, 11 September 2026; abstract, Section 1.1 and Theorem 19; text-access requirement'),
 ref('nonoverlap','Non-overlapping Indexing in BWT-Runs Bounded Space','Daniel Gibney; Paul Macnichol; Sharma V. Thankachan',2023,'https://doi.org/10.1007/978-3-031-43980-3_21','SPIRE 2023, pp.260–270; primary first page/abstract and proceedings metadata; full NSF PDF not newly accessible'),
 ref('nonoverlapjournal','Non-overlapping indexing in BWT-runs bounded space','Daniel Gibney; Paul Macnichol; Sharma V. Thankachan',2025,'https://doi.org/10.1016/j.tcs.2025.115512','Theoretical Computer Science 1056, 115512, 21 November 2025; primary abstract/metadata only'),
 ],
 context_blocks=[
 block('Repeated text can have a small number of BWT runs even when its expanded suffix tree is large. The run-linear search index and the full navigation structure have different space guarantees.'),
 block(r'The checked full suffix-tree theorem uses \(O(r\log(2+n/r))\) words and supports the relevant operations in polylogarithmic time. The harmless 2 in the logarithm makes the bound explicit also when the run count is close to the text length.'),
 block('The ICALP 2026 path-decomposition result supports several tree operations with O(r) additional words. Its theorem assumes a separate text-access and longest-common-extension oracle and does not state all operations required here.','paths'),
 block('A July 2026 application to compact word graphs still invokes the earlier full suffix-tree representation as a black box with its logarithmic space overhead.','cdawg'),
 block('The September 2026 suffixient-array publication provides a different sampling and pattern-location interface with text-access assumptions. Its guarantees alone do not supply the combined tree interface and total-space bound on this card.','suffixient'),
 block('Non-overlapping occurrence reporting is another useful run-linear indexing task. The conference paper appeared in 2023, its repository posting in 2024, and its journal version in 2025; those dates do not denote a full-tree resolution.','nonoverlapjournal'),
 ],
 progress=[progress('2019-07-04','The full revision gives the compressed suffix-tree theorem and records remaining O(r)-space access questions.'),progress('2025-11-21','The non-overlapping reporting work appears in journal form; its task is narrower than the required suffix-tree interface.','nonoverlapjournal'),progress('2026-07-01','Path decompositions reduce the additional space for a specified subset of tree operations to O(r), under separate text-oracle assumptions.','paths'),progress('2026-09-11','The suffixient-array journal paper develops another compressed pattern-location interface requiring access to the underlying text.','suffixient')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the exact binary-text interface in O(r) total words. The July 2026 theorem charges its O(r) words in addition to a text oracle and states a narrower interface; the September sampling result also has distinct access assumptions. This review checks theorem scope and dates, not complete proofs of all cited work. The binary specialization and operation list remain editorial choices already present in the imported card.',summary=[
 'A binary text with a sentinel determines a suffix tree and a run count in its Burrows–Wheeler transform.',
 'The target stores the entire specified navigation and direct-access interface in space proportional to that run count.',
 'Every query must be exact and take polylogarithmic worst-case time after deterministic polynomial-time construction.',
 'The space budget includes the text representation and any access oracle, which distinguishes the target from recent partial-interface results.',
 'A complete Lean-checked answer must establish or refute all of these guarantees simultaneously.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
