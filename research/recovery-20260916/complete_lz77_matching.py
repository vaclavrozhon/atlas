"""Review linear-time occurrence detection from a self-referential LZ parse."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0468';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the existing deterministic linear-time decision target, self-referential phrases, polynomial integer alphabet and linear working space.',
 'Specified positive phrase lengths, sequential overlap semantics, a constant-word phrase encoding and the lack of a greedy-parse promise.',
 'Made the alphabet and word-size constants, uniformity, all-input guarantees and charged preprocessing explicit.',
 'Kept integer division in the word RAM: the older lower bound excludes this operation and does not refute the selected model.',
 'Distinguished the linear-time grammar-input theorem and recent internal-pattern indexes from a linear-time algorithm on the supplied LZ input.',
 'Preserved the individually assigned importance and added a complete Lean-checked binary answer criterion and dated source audit.',
]
sources=[
 'Read Adaptive and Scalable Data Structures, Dagstuhl Seminar 25191, DOI 10.4230/DagRep.15.5.1, Section 5.4, p.17: Gawrychowski asks first for O(n+m) matching with compressed input length n; the second question concerns random access and is separate. Seminar held 4–9 May 2025.',
 'Read Gawrychowski, Pattern matching in Lempel-Ziv compressed strings: fast, simple, and deterministic, arXiv:1104.4203v1, 21 April 2011: preliminaries pp.3–4, self-reference conversion Lemma 8 p.8, Theorem 5 p.18 and Section 7 pp.18–19. The deterministic bound is O(z log(N/z)+m), with the logarithm convention adjusted at small ratios. The lower bound is explicitly for a division-free algebraic computation model, not the full word RAM used here. The paper writes copy-plus-next-character triples; its copy processing in Lemma 8 also permits a copy without an appended literal. This card retains its already specified literal/copy phrase convention and does not assume a free conversion to a smaller grammar.',
 'Read Ganardi–Gawrychowski, Pattern Matching on Grammar-Compressed Strings in Linear Time, arXiv:2111.05016v1, 9 November 2021, abstract and Introduction, Theorem 1 p.2. This is O(g+m) for a supplied straight-line grammar of size g, even without integer division. The Introduction explicitly separates the self-referential LZ lower-bound model and grammar case.',
 'Read Duyster–Kociumaka, Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts, Theory of Computing Systems 70, article 11, DOI 10.1007/s00224-026-10266-x, published 23 February 2026: abstract and compressed-input construction discussion. It indexes internal fragments with a length-ratio restriction and charges additional construction costs; it does not supply the all-preprocessing O(z+m) external-pattern decision algorithm asked here. The 22 June update concerns funding, not a new algorithm date.',
 'Bounded primary-source searches through 17 September 2026 found no verified resolution of this precise LZ-input target. This does not certify that every recent compressed-string paper has been checked.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''For every fixed integer \(c\ge1\), do there exist constants \(K\ge1\), an integer \(B\ge c+8\), and one uniform deterministic algorithm \(A\) with the following property? Given any valid \(z\)-phrase LZ77 representation of a text \(T\) of length \(N\ge1\), and an explicit nonempty pattern \(P\) of length \(m\), with symbols in \(\{1,\ldots,(z+m)^c\}\), the algorithm decides whether \(P\) occurs contiguously in \(T\) using at most \(K(z+m)\) word-RAM instructions and \(K(z+m)\) working words. Self-referential copy phrases are allowed, the word size is \(w=B\lceil\log_2(N+m+2)\rceil\), and all preprocessing is included.''',
 definitions=r'''The input contains \(z,N,m\), an array of \(z\ge1\) phrase descriptors, and the \(m\ge1\) pattern symbols. Each descriptor occupies three words: a type tag and two integer fields. A literal descriptor \((\mathrm{literal},a,0)\) appends the single symbol \(a\). A copy descriptor \((\mathrm{copy},s,\ell)\) has \(\ell\ge1\). If the next text position is \(p\), it requires \(1\le s<p\) and appends \(\ell\) symbols sequentially, setting \(T[p+j]=T[s+j]\) for \(j=0,\ldots,\ell-1\). The source position is always earlier than the destination, so it may refer to a symbol generated earlier in this same phrase. The copied interval need not end before \(p\). After all phrases the length is exactly \(N\). All literal and pattern symbols belong to the displayed alphabet. These conditions are input promises; no greedy or minimum-size parse is promised. In particular, \(z\le N\).

The required output is one bit, equal to one exactly when some \(i\) with \(1\le i\le N-m+1\) satisfies \(T[i+j]=P[j+1]\) for every \(0\le j<m\). If \(m>N\), it is zero. Occurrences may cross any phrase boundaries or lie inside an overlapping copy. The algorithm need not report positions or enumerate occurrences.

Use a sequential random-access machine with one fixed finite program, word-sized registers and addressed cells. A word stores an unsigned \(w\)-bit integer. Unit-cost operations are a read or write, comparison, branch, addition, subtraction and multiplication modulo \(2^w\), integer quotient and remainder with a nonzero divisor, bitwise Boolean operations and logical shifts; shifts by at least \(w\) give zero. Addresses fit in a word. Division is expressly allowed. There is no randomness, advice, oracle, quantum operation or unit-cost operation on an unbounded integer. Multiword calculations must be performed with charged word instructions.

The supplied compressed representation and explicit pattern are read-only input arrays. Working space counts every other word retained by the algorithm, including copies, tables, indexes and intermediate representations. Time counts reading the input and building any auxiliary representation. There is no separately supplied uncompressed text, grammar, text-access oracle or precomputed index. The larger word size reflects positions in the potentially very long decoded text, not permission to perform uncharged decompression.

The quantifier order is \(\forall c\,\exists(K,B,A)\,\forall(T\text{ represented by its supplied parse},P)\). The finite program and constants may depend on the fixed alphabet exponent \(c\), but not on \(N,z,m\), the phrase contents or the pattern. They must satisfy the bounds on every valid input.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of this existence proposition or its logical negation. A positive answer must implement the decision procedure uniformly in the specified word RAM and prove its correctness, worst-case time and working-space bounds for every permitted parse and pattern. A negative answer must rule out the stated algorithms in this model; a conditional lower bound is only a conditional result.

Time linear in the decoded length \(N\), or in the size of a supplied or newly constructed grammar that can exceed \(z\), does not meet the target. Neither does an uncharged preprocessing phase. A lower bound for a model lacking integer division does not refute this proposition.''',
 source_formulation=dict(text='Gawrychowski asks whether pattern matching on a Lempel–Ziv compressed text can run in time linear in the compressed text length plus the explicit pattern length. This card retains the decision version and the previously selected deterministic word-RAM model with self-references, integer division and linear working space.',caption='Adaptive and Scalable Data Structures, Seminar 25191 (May 2025), §5.4, first question, p.17; explicit model conventions retained and completed in the editorial review.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Adaptive and Scalable Data Structures','Paweł Gawrychowski (problem contributor); Michael A. Bender, John Iacono, László Kozma and Eva Rotenberg (editors)',2025,'https://doi.org/10.4230/DagRep.15.5.1','Seminar 25191, 4–9 May 2025; §5.4, first question, p.17'),
 ref('lz','Pattern matching in Lempel-Ziv compressed strings: fast, simple, and deterministic','Paweł Gawrychowski',2011,'https://arxiv.org/abs/1104.4203v1','21 April 2011; preliminaries, Lemma 8 p.8, Theorem 5 p.18 and §7 pp.18–19'),
 ref('grammar','Pattern Matching on Grammar-Compressed Strings in Linear Time','Moses Ganardi; Paweł Gawrychowski',2021,'https://arxiv.org/abs/2111.05016v1','9 November 2021; Introduction, Theorem 1 p.2'),
 ref('internal','Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts','Anouk Duyster; Tomasz Kociumaka',2026,'https://doi.org/10.1007/s00224-026-10266-x','Published 23 February 2026; abstract and compressed-input construction discussion'),
 ],
 context_blocks=[
 block('A small sequence of copying instructions may represent a much longer text. Requiring only the existence of a match avoids an output size proportional to the number of occurrences.'),
 block(r'The classical deterministic LZ bound is \(O(z\log(2+N/z)+m)\). Its additional logarithmic factor depends on the compression ratio. The same paper discusses a lower bound for a model without integer division; this card allows division.','lz'),
 block(r'A linear \(O(g+m)\) bound is known when a grammar of size \(g\) is the input. Constructing such a grammar from an LZ parse can increase the representation size, so this theorem does not immediately give the target measured in \(z\).','grammar'),
 block('The 2026 internal-pattern result answers queries between fragments of an indexed text. Its query interface and preprocessing requirements differ from a single external pattern supplied with an unindexed LZ representation.','internal'),
 ],
 progress=[progress('2011-04-21','A deterministic LZ matching algorithm obtains a compression-ratio logarithm beyond the linear input-size target.','lz'),progress('2021-11-09','Linear-time matching is obtained for a supplied straight-line grammar.','grammar'),progress('2025-05','The seminar explicitly retains linear-time matching on Lempel–Ziv input as an open question.'),progress('2026-02-23','Logarithmic-time internal-pattern queries are obtained in compressed and dynamic indexing settings, with a different query interface and charged construction.','internal')],
),notes,sources,'Open in the May 2025 seminar source. The bounded primary-source review through 17 September 2026 found no verified resolution in the specified self-referential LZ word-RAM model. The linear grammar-input theorem and later internal-pattern indexes do not by themselves establish this target; the older division-free lower bound does not refute it.',summary=[
 'A text is supplied as literal and copy phrases, and the pattern is an explicit string.',
 'Copies may overlap themselves, so the decoded text can be much longer than the input representation.',
 'The question asks for exact deterministic occurrence detection in time and working space linear in the phrase count plus pattern length.',
 'The machine allows integer division, and all preprocessing is charged.',
 'Linear time for grammar input is known, but does not automatically give the required bound for LZ input; a complete Lean-checked answer is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
