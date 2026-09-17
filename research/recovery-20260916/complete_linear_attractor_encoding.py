"""Complete the source's linear-word attractor reachability question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6928';claim=read_claims(ROOT)[identifier]
notes=[
 'Selected the primary O(gamma)-word reachability question; the inherited second question about any smaller improvement remains context only.',
 'Asked the user about the two target scales and, after allowing time for an optional reply, proceeded with the announced source-faithful recommended default. This is an editorial assumption, not recorded as explicit user approval.',
 'Defined the smallest attractor by coverage of an occurrence of every nonempty substring, rather than coverage of every occurrence.',
 'Expressed the target in bits, including all metadata, and specified a growing integer alphabet and uniform lossless encoding/decoding.',
 'Imposed no running-time or temporary-workspace bound; no fast random-access or indexing interface is part of this pure representation question.',
 'Read the survey, the 2023 independent open-status statement and the January 2026 reachability discussion, retaining their one-dimensional versus two-dimensional scope.',
 'Assessed importance individually and required a complete Lean-checked proof or refutation.',
]
sources=[
 'Read Navarro, Indexing Highly Repetitive String Collections, arXiv:2004.02781v10, 23 November 2022: Section 2 word/space conventions; Section 3.9, pp.23–24, definition of attractors and the question whether O(gamma) words always suffice; Section 3.10, pp.24–25, distinction from delta and the weaker o(gamma log n)-space question. The source explicitly separates representation reachability from efficient access supplied by known larger structures.',
 'Read Bernardini–Fici–Gawrychowski–Pissis, Substring Complexity in Sublinear Space, ISAAC 2023, DOI 10.4230/LIPIcs.ISAAC.2023.12, Introduction p.12:2. It explicitly records that O(gamma) machine-word representation remains unknown and distinguishes this from computing delta. The primary publisher gives 28 November 2023 as publication date.',
 'Read Carfagna–Manzini–Romana–Sciortino–Urbina, Generalization of Repetitiveness Measures for Two-Dimensional Strings, Theory of Computing Systems 70, Article 2, DOI 10.1007/s00224-025-10244-9, published 3 January 2026. Primary full HTML: Section 3, Definition 4 and its following paragraph define reachability and explicitly refer to the one-dimensional gamma question as unknown. Its new theorems are about two-dimensional measures and are not substituted for this target.',
 'Fresh searches through 17 September 2026 found related attractor matching, special-word attractor computations and compressed-query results, but no verified resolution of the general one-dimensional linear-word encoding question. The source’s finite integer-alphabet convention is made explicit as [0,n); encoding length includes the string length and any symbol information.',
 'The proposed default was presented as an optional scope question and announced before completion when no answer had arrived. A later different user choice should supersede this editorial default, without treating the current choice as user-confirmed.',
]
complete(identifier,dict(
 title='Linear-space encoding from smallest string attractors',criterion='resources',question_type='yes_no',
 importance=dict(score=87,method='editorial',reason='This asks whether a central representation-independent measure of repetitiveness actually controls lossless description length, separating an information-content question from the limitations of particular grammars, parsing methods and indexes.'),
 formal=r'''Do there exist a constant \(C\ge1\) and two uniform deterministic computable functions \(E,D\) such that, for every \(n\ge1\) and every string \(T\in\{0,\ldots,n-1\}^n\),
\[
D(E(T))=T
\quad\text{and}\quad
|E(T)|\le C\,\gamma(T)\,\lceil\log_2(n+2)\rceil?
\]
Here \(E(T)\) is a finite binary code, its length \(|E(T)|\) includes all metadata, and \(\gamma(T)\) is the minimum string-attractor size defined below. The decoder receives only the complete binary code. No time bound is imposed on encoding or decoding. Equivalently, the target is \(O(\gamma(T))\) words of \(\Theta(\log n)\) bits for a lossless representation.''',
 definitions=r'''Write \(T=T[0]T[1]\cdots T[n-1]\). A string attractor is a set \(\Gamma\subseteq\{0,\ldots,n-1\}\) such that every nonempty contiguous substring has an occurrence crossing \(\Gamma\). Precisely, for every \(0\le i\le j<n\), there is an integer \(p\) with \(0\le p\le n-(j-i+1)\) for which
\[
T[p\ldots p+j-i]=T[i\ldots j]
\quad\text{and}\quad
\Gamma\cap\{p,p+1,\ldots,p+j-i\}\ne\varnothing.
\]
The occurrence may overlap the original substring. One intersecting occurrence for each distinct substring is sufficient; the set need not meet every occurrence. Define \(\gamma(T)\) as the minimum cardinality of such a \(\Gamma\). It exists because all positions form an attractor, and \(1\le\gamma(T)\le n\). The alphabet may grow with \(n\); no binary or constant-alphabet promise is imposed. Symbols are explicit integers in \(\{0,\ldots,n-1\}\). Strings are ordinary finite linear strings, without a mandatory terminator, cyclic wrapping or a reversal equivalence.

Let \(\mathcal S=\bigcup_{n\ge1}\{0,\ldots,n-1\}^n\). The encoder \(E:\mathcal S\to\{0,1\}^*\) and decoder \(D:\{0,1\}^*\to\mathcal S\cup\{\bot\}\) each have one fixed finite deterministic Turing program. A string supplied to the encoder is represented by its length followed by its explicit list of binary integer symbols, using any fixed effective self-delimiting integer encoding. The encoder halts on every valid input, and the decoder halts on every finite code, returning either a finite string or the failure symbol \(\bot\). On every code actually produced by \(E\), it must return the original string exactly. Hence the code identifies the whole string, including its length and integer symbol names. No two different strings may have the same code.

Only the complete code length is measured. The encoder need not be given an optimal attractor, its size, or any auxiliary advice. The decoder is not supplied \(n\), \(\gamma(T)\), an attractor, a grammar, a dictionary, a seed or an external copy of the text for free; any input-dependent information it needs must be recoverable from the code. Both programs are independent of \(n,T\), with no nonuniform advice or oracle. Fixed program descriptions do not count toward per-string storage, but input-dependent tables do. The code is received as a complete finite bitstring, so a prefix-free concatenation convention is not required. All headers and any termination information actually used belong to the measured code.

There is no restriction on encoder/decoder running time or temporary workspace beyond termination. In particular, the bound does not require polynomial-time computation of a minimum attractor, fast extraction of one character, substring search, or decompression within the size of the compressed representation. The only resource target is the length of the retained lossless description. These conventions separate representability from efficient construction and query support.

The same absolute \(C\) and the same pair \(E,D\) must handle every allowed string. They may exploit any computable representation, not only copy-based parses, grammars, bidirectional schemes or existing indexing formats. The shifted logarithm handles short strings and is asymptotically the usual word length. Changing its fixed multiplicative word-size constant is absorbed in \(C\).''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive answer must establish one uniform lossless encoding/decoding scheme and the stated worst-case code-length bound for every allowed string. An impossibility result must apply to all such representations, rather than only one grammar, parsing format or data-structure model.

A logarithmic-factor overhead, a result for a special word family, or any weaker asymptotic improvement short of the linear-word bound does not answer this selected target. Hardness of finding a minimum attractor in polynomial time does not refute an encoding question with unrestricted computation time. No additive numerical tolerance applies.''',
 source_formulation=dict(text='Section 3.9 asks whether the smallest-attractor measure is reachable, meaning that every string has an O(gamma)-word representation. Section 3.10 also asks the weaker question of improving the general gamma log n scale. This card selects the former as its main target and does not add a fast-access requirement.',caption='Navarro, Sections 2, 3.9 and 3.10, pp.23–25 in arXiv:2004.02781v10; primary target selected as an announced editorial default on 17 September 2026, pending any different user preference.',citation='primary',format='editorial_paraphrase'),
 why='An attractor measures how a small set of positions witnesses all distinct substrings, independently of a particular compressor. If its size always controls description length to within a constant number of words, it supplies a general measure of how much information repetitive strings contain. A failure would expose a gap between substring coverage and lossless representability.',
 references=[
 ref('primary','Indexing Highly Repetitive String Collections','Gonzalo Navarro',2022,'https://arxiv.org/abs/2004.02781v10','23 November 2022 revision of the survey; Section 2 word-size conventions and Sections 3.9–3.10, pp.23–25; inherited catalogue cited the 2021 survey'),
 ref('status2023','Substring Complexity in Sublinear Space','Giulia Bernardini; Gabriele Fici; Paweł Gawrychowski; Solon P. Pissis',2023,'https://doi.org/10.4230/LIPIcs.ISAAC.2023.12','Published 28 November 2023; Introduction, p.12:2, explicit O(gamma)-word reachability question'),
 ref('status2026','Generalization of Repetitiveness Measures for Two-Dimensional Strings','Lorenzo Carfagna; Giovanni Manzini; Giuseppe Romana; Marinella Sciortino; Cristian Urbina',2026,'https://doi.org/10.1007/s00224-025-10244-9','Published 3 January 2026, Theory of Computing Systems 70, Article 2; Section 3, Definition 4 and following paragraph, including the one-dimensional open-status remark'),
 ],
 context_blocks=[
 block('The source measures storage in logarithmic-size machine words. The target is therefore proportional to gamma log n bits, rather than gamma bits.'),
 block('Known attractor-based representations have an additional logarithmic factor and can provide efficient access. The present question removes that factor while requiring only exact recovery of the full string.'),
 block('The optimum attractor size need not be efficiently computable for a short description to exist. Computational hardness of optimizing the attractor is a separate question.'),
 block('The 2023 paper explicitly distinguishes this open representation question from its own work on efficiently computing a different substring-complexity measure.','status2023'),
 block('The January 2026 article studies two-dimensional data but separately records that reachability of the ordinary one-dimensional attractor measure is still unknown. No two-dimensional theorem is treated as a solution here.','status2026'),
 ],
 progress=[progress('2022-11-23','The checked survey revision records the linear-word representation question and separates it from known larger access structures.'),progress('2023-11-28','The ISAAC paper independently records that O(gamma)-word representability is unknown.','status2023'),progress('2026-01-03','The two-dimensional generalization paper still describes the corresponding one-dimensional reachability question as unknown.','status2026')],
),notes,sources,'The January 2026 primary article explicitly records the one-dimensional gamma reachability question as unknown. Bounded later primary-source checks through 17 September 2026 found no verified resolution. The main linear-word question is retained as the announced recommended editorial default after an optional user scope question; no user confirmation is claimed, and a later different choice can supersede it.',summary=[
 'A string attractor is a set of positions crossed by some occurrence of each distinct nonempty substring.',
 'Its minimum size gamma measures repetitiveness without selecting a particular compression format.',
 'The question asks whether every string has a lossless code using only O(gamma) logarithmic-size words, including all metadata.',
 'The encoder and decoder are uniform and must terminate, but there is no time bound or fast-query requirement.',
 'A complete Lean-checked proof or refutation must cover arbitrary allowed strings and arbitrary computable lossless representations.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
