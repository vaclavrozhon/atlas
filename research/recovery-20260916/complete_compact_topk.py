"""Complete the all-pattern compact-space top-k document-retrieval target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7362';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved compact O(n log sigma) bits and packed-pattern optimal query time for all pattern lengths and all requested output counts.',
 'Specified overlapping term frequency, document boundaries, duplicate documents as separate labelled items, sorted output and deterministic tie breaking.',
 'Expanded uniform deterministic construction, worst-case time, persistent storage and query workspace quantifiers; renamed the word-size constant to avoid collision with document count.',
 'Checked the SODA 2025 full theorem and corollaries rather than treating its CSA-relative or long-pattern guarantees as the complete target.',
 'Distinguished bits from words, sorted from unsorted reporting, and string occurrence frequency from semantic retrieval scores.',
 'Preserved importance 87 and the binary Lean-checked existence criterion.',
]
sources=[
 'Read Navarro–Nekrich, Top-k Document Retrieval in Compressed Space, author-hosted SODA 2025 PDF: abstract, Introduction, Table 1, Theorem 4.1, Corollaries 4.1–4.3 and Conclusions. The source explicitly leaves RAM-optimal queries in near-O(n log sigma) bits open. Its general sorted-output bound adds O(n log log n) bits to a CSA and a t_SA+log log n factor per reported document; its query workspace is separately O(k log n) bits. Long-pattern and unsorted-output corollaries do not cover this full target. No full proof or deterministic construction-time audit was performed.',
 'Read the primary SIAM metadata and abstract for the SODA 2025 paper, DOI 10.1137/1.9781611978322.137, published 7 January 2025, pp. 4009–4030. These confirm authors, date and the distinction between RAM-optimal O(n log n)-bit indexes and the unresolved compact-space target.',
 'Read the primary SIAM abstract of Navarro–Nekrich, Time-Optimal Top-k Document Retrieval, DOI 10.1137/140998949: O(n log n) bits suffice for the packed-pattern optimal time; compact variants retain dependence on the document-count logarithm and an extra time term. A webpage issue/crawl date in 2026 is not treated as the date of this older result.',
 'Checked the author publication list and bounded primary-source searches through 17 September 2026. No verified later result meeting the all-pattern, sorted term-frequency, compact-space target was located. Contemporary RAG retrieval papers use different relevance models and do not supply this exact static string-index guarantee.',
]
complete(identifier,dict(
 title='Optimal top-k document retrieval in compact space',criterion='construction',question_type='yes_no',
 formal=r'''Do there exist one uniform deterministic static indexing algorithm, one uniform deterministic query algorithm, absolute constants \(C,K>0\), and fixed integers \(p\ge1\), \(B\ge8\), with the following guarantees? For every ordered collection of \(d\ge1\) nonempty strings of total length \(n\ge2\) over an alphabet \(\{0,\ldots,\sigma-1\}\), where \(2\le\sigma\le n\), preprocessing takes at most \(K(n+1)^p\) word-RAM instructions and produces an index occupying at most
\[
 Cn\lceil\log_2\sigma\rceil\ \text{bits}.
\]
For every packed nonempty pattern \(P\) of length \(1\le m\le n\) and every \(1\le k\le d\), the index returns the top-\(k\) documents by occurrence frequency, in the specified order, within
\[
 K\left(1+\frac{m}{\log_\sigma n}+k\right)
 \quad\text{word-RAM instructions in the worst case}?
\]
The word length is \(w=B\lceil\log_2(n+2)\rceil\). All constants and programs must be independent of the collection and all query parameters.''',
 definitions=r'''The input collection is an ordered list \((D_1,\ldots,D_d)\); equal strings at different positions are different documents. Their total number of symbols is \(n=\sum_i|D_i|\). The document identifier is its position \(i\), so identifiers lie in \(\{1,\ldots,d\}\). A finite input representation supplies the alphabet size, packed strings and their lengths or boundaries. No occurrence may cross a document boundary.

For a pattern \(P\) of length \(m\), define the integer relevance of document \(i\) by
\[
 f_P(i)=\bigl|\{j:1\le j\le |D_i|-m+1,\ D_i[j..j+m-1]=P\}\bigr|.
\]
The set is empty when the document is shorter than the pattern. Overlapping occurrences count separately. Put \(h=|\{i:f_P(i)>0\}|\). Sort these \(h\) identifiers by decreasing frequency, breaking equal-frequency ties by increasing identifier. The answer is the first \(\min(k,h)\) identifiers in this order, with no duplicates and an explicit end indication. Only identifiers are required; frequencies and occurrence positions need not be output. When \(h=0\), the answer is empty.

The query supplies \(m,k\) and \(P\), whose symbols occupy \(\lceil\log_2\sigma\rceil\) bits each in a packed bit sequence. The logarithm in the time bound is \(\log_\sigma n=\log_2n/\log_2\sigma\). Up to fixed constants and rounding, the pattern occupies \(1+m/\log_\sigma n\) machine words. Each returned identifier occupies one word, and output instructions count toward query time.

Use a sequential word RAM with one fixed finite program for preprocessing and one for queries. Unit-cost instructions are word reads and writes, copying, comparison, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder with a nonzero divisor. A shift by at least \(w\) returns zero. Addresses and values fit in words. Multiword computation pays for its constituent instructions. There are no random instructions, advice, external oracles or free precomputed tables; initialization and table construction count toward preprocessing. Polynomial preprocessing workspace is allowed subject to the word-address model.

Index space is measured in bits, including every persistent word, retained text copy, boundary representation, table, auxiliary structure and input-dependent parameter. Counting an array as linear in words does not establish the required compact bit bound. The original collection is unavailable to a query except through its counted index. A query starts with no private input-dependent state from earlier queries and may not retain such state between queries. Query working memory, including registers and temporary copies but excluding the supplied read-only packed pattern and streamed output, also uses at most \(Cn\lceil\log_2\sigma\rceil\) bits; increasing the universal constant to bound both is allowed. The index itself remains available throughout.

Correctness and the query bound hold for every valid collection and query, with no restriction to long patterns, selected values of \(k\), small numbers of documents or typical text distributions. Relevance is the exact integer occurrence count defined here, not an externally supplied document rank or a semantic similarity score.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the stated existence proposition or its logical negation, with the same uniform deterministic model, output ordering and worst-case resource guarantees. A construction must justify both the compact bit space and the query bound simultaneously over the whole domain.

Optimal time with \(O(n\log n)\) bits, a dependence on the document-count logarithm that exceeds the specified space, extra \(O(n\log\log n)\) bits for a constant alphabet, or optimality only relative to a chosen compressed suffix-array primitive does not by itself meet the target. Neither long-pattern-only results nor unsorted output suffice. A conditional lower bound retains its hypothesis and is not an unconditional refutation. No additive numerical tolerance is imposed on this existence question.''',
 source_formulation=dict(text='The SODA 2025 paper explicitly asks whether the RAM-optimal top-k query bound can coexist with space close to the packed text size. This card retains the precise O(n log sigma)-bit target, exact occurrence-frequency ranking and sorted output for every pattern length.',caption='Navarro–Nekrich, SODA 2025, abstract and Introduction; resource and tie conventions made explicit.',citation='primary',format='editorial_paraphrase'),
 why='An index should rank documents containing an arbitrary substring without storing a word-sized record for every text position. Simultaneously attaining the packed-input query bound and space proportional to the text is a central time–space question for exact retrieval on string collections.',
 references=[
 ref('primary','Top-k Document Retrieval in Compressed Space','Gonzalo Navarro; Yakov Nekrich',2025,'https://users.dcc.uchile.cl/~gnavarro/ps/soda25.pdf','SODA 2025, pp. 4009–4030; abstract, Table 1, Theorem 4.1, Corollaries 4.1–4.3 and Conclusions; DOI 10.1137/1.9781611978322.137'),
 ref('optimal_time','Time-Optimal Top-k Document Retrieval','Gonzalo Navarro; Yakov Nekrich',2017,'https://doi.org/10.1137/140998949','SIAM Journal on Computing 46(1), pp. 80–113; primary abstract, word-space optimal-time result and compact tradeoffs'),
 ],
 context_blocks=[
 block('The query pattern can be any substring, so the problem differs from a dictionary of predefined search terms. Counting all its occurrences is also different from ranking distinct documents by their individual occurrence counts.'),
 block('Optimal packed-pattern time is known with O(n log n) bits. For a small alphabet, the text itself needs only O(n log sigma) bits, leaving a substantial space gap.','optimal_time'),
 block('The SODA 2025 construction adds O(n log log n) bits to a compressed suffix array and relates query time to that array’s search and access costs. This is progress toward compact retrieval, but the extra space already exceeds the target for a fixed alphabet.'),
 block('Its stronger long-pattern results distinguish sorted from unsorted reporting. The card requires the full frequency order, including the fixed tie rule, for short and long patterns alike.'),
 block('A source theorem’s workspace must also be counted: the 2025 statement separately permits O(k log n) temporary bits. The precise card model requires query workspace to fit the same asymptotic compact budget as the persistent index.'),
 ],
 progress=[progress('2017','Optimal packed-pattern query time is obtained using linear word space; compact variants trade additional parameters in space or query time.','optimal_time'),progress('2025-01-07','The SODA 2025 index improves compressed-space retrieval with O(n log log n) extra bits and stronger bounds for long patterns, without establishing the all-pattern compact target.')],
),notes,sources,'The SODA 2025 primary source explicitly leaves the compact-space RAM-optimal target open. Bounded later-work checks through 17 September 2026 located no verified resolution. Its general theorem and long-pattern or unsorted corollaries were checked separately; this is a formulation and statement-scope review, not an independent proof or implementation audit.',summary=[
 'The task is a static index for an ordered collection of strings using space proportional to their packed text size.',
 'A query ranks documents by the exact number of occurrences of an arbitrary pattern, counting overlaps.',
 'It must output the requested best identifiers in frequency order in time proportional to the packed pattern length plus k.',
 'The 2025 compressed-index result has additional space costs and stronger guarantees only in restricted output or pattern regimes.',
 'Acceptance requires a complete Lean-checked proof or refutation with uniform deterministic algorithms and the full stated bounds.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
