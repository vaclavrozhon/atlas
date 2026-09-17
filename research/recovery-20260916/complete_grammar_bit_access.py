"""Complete the bit-space grammar-access target, preserving its selected scope."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0470';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained binary straight-line grammars, O(g log g) total persistent bits, logarithmic worst-case character access and polynomial-in-g preprocessing.',
 'Specified finite uniform construction and query programs, absolute constants and the relationship between word size and preprocessing exponent.',
 'Charged all persistent metadata, retained grammar bits, lookup tables and final-word padding, while preserving the selected temporary-query workspace allowance.',
 'Made clear that the query receives only the index and position, with no free copy of the grammar, expansion lengths or decompressed text.',
 'Read the 2026 encoding theorem and its future-work paragraph; the expansion-length term remains present.',
 'Read ICALP 2026 Theorems 1.1–1.2 and separated their space regime from the smaller bit budget here.',
 'Preserved importance and required a complete Lean-checked proof or refutation of this explicit specialization of the seminar question.',
]
sources=[
 'Read Navarro, A graph problem with applications to grammar compression, Adaptive and Scalable Data Structures, Dagstuhl Seminar 25191, DOI 10.4230/DagRep.15.5.1, Section 5.9 p.19. The source asks whether the expansion-length storage overhead can be removed while retaining efficient access; it does not itself specify the exact logarithmic query time or polynomial preprocessing convention. Those choices were already fixed in this card and are retained.',
 'Read Takasaka–I, Space-Efficient SLP Encoding for O(log N)-Time Random Access, Theory of Computing Systems 70, article 28, DOI 10.1007/s00224-025-10243-w, published 13 April 2026: Introduction Theorem 1, following discussion and Section 4. All three encodings contain an n ceil(log N) term for expansion lengths, where n denotes grammar variables. The authors explicitly discuss reducing that term as future work and do not establish its necessity.',
 'Read Duyster–Kociumaka, Random Access in Grammar-Compressed Strings: Optimal Trade-Offs in Almost All Parameter Regimes, ICALP 2026 article 86, DOI 10.4230/LIPIcs.ICALP.2026.86: abstract, Theorem 1.1 p.86:3, Theorem 1.2 p.86:4 and the following scope discussion. The upper bound assumes g log n < Mw < n log sigma, with M measured in words. The matching lower bound also assumes space above the g log n scale, with extra factors and a grammar-size restriction. Neither establishes or rules out the selected O(g log g)-bit representation for every grammar.',
 'Bounded primary-source checks through 17 September 2026 found no verified resolution of this target. The later results are checked for their stated parameter ranges, not treated as a full independent verification of their proofs.',
]
complete(identifier,dict(
 title=r'Grammar random access in \(O(g\log g)\) bits',
 formal=r'''Do there exist absolute constants \(K\ge1\), integers \(d\ge1\) and \(B\ge d+8\), and uniform deterministic construction and query algorithms with the following guarantee? For every binary straight-line program \(G\) with \(g\ge1\) reachable rules generating a binary string \(T\) of length \(N\), construction from \(G\) takes at most \(K(g+1)^d\) word-RAM instructions and produces a representation occupying at most \(Kg\log_2(g+2)\) persistent bits. Given any \(1\le i\le N\), a query returns \(T[i]\) in at most \(K\log_2(N+2)\) instructions. The word size is \(w=B\lceil\log_2(N+g+2)\rceil\); the space bound includes the retained grammar, every auxiliary index and final-word padding.''',
 definitions=r'''A binary straight-line program has ordered variables \(X_1,\ldots,X_g\), one production per variable and start variable \(X_g\). A production is \(X_j\to0\), \(X_j\to1\), or \(X_j\to X_aX_b\) with \(1\le a,b<j\). Every variable must be reachable from the start. Expanding the start produces exactly one nonempty binary string \(T\). The quantity \(g\) counts rules, not occurrences in the expanded derivation tree, and \(N=|T|\). No balance, height, minimality or polynomial upper bound on \(N\) in terms of \(g\) is promised. In fact \(N\le2^{g-1}\), so the logarithmic word size itself is at most linear in \(g\).

The input is an explicit packed binary list of the productions and the integer \(g\). Each production has a two-bit type tag, followed, for a concatenation, by two indices of \(\lceil\log_2(g+1)\rceil\) bits each. A self-delimiting binary header for \(g\) is included. Thus the description has \(O(g\log(g+2))\) bits. Construction receives this grammar, not its expanded string. The representation may replace the grammar and need not recover its original rule names or productions, but it must answer access queries to the generated string exactly.

Use a sequential word RAM with a fixed finite program, unsigned \(w\)-bit registers and word-addressed memory. Unit-cost operations are reads, writes, comparisons, branches, addition, subtraction and multiplication modulo \(2^w\), integer quotient and remainder with nonzero divisor, bitwise Boolean operations and logical shifts; shifts by at least \(w\) yield zero. There is no randomness, advice, input-dependent oracle, quantum operation or unbounded-integer primitive. All addresses fit in a word. Construction time includes reading and repacking the grammar and building all tables. Its temporary storage is unrestricted except for what the time and address bounds permit, and is discarded when construction ends.

The permanent representation is a finite contiguous array of words. Its charged size is the number of allocated words multiplied by \(w\), including unused bits of its final word. All metadata, any retained grammar, expansion lengths and auxiliary tables are part of this array. The machine program is fixed, with no input-dependent constants hidden in its code. The word width is part of the machine model. Any separately retained input-dependent value, including \(N\) or \(g\), must be charged to the representation.

Each query receives only this representation and the position \(i\), and starts with empty temporary storage. It may use at most \(K\log_2(N+2)\) temporary words, which are discarded after the query. This workspace is separate from the persistent-bit budget and cannot retain information between queries. Every query must work independently, including the first query. The original input grammar is unavailable unless stored in the charged representation; there is no free text-access oracle or uncompressed text.

The same constants and finite construction and query programs must work for every grammar and every valid query position. Time is worst-case, not amortized. Space linear in \(g\) words is not the requested guarantee when \(\log N\) is much larger than \(\log g\). Conversely, a representation of the right bit size with polynomial-in-\(N\) construction does not meet the polynomial-in-\(g\) preprocessing requirement.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive proof must supply uniform construction and query algorithms and establish exact access, all charged space, polynomial preprocessing from the grammar and the worst-case query bound. A negative proof must rule out the full proposition in the specified model unconditionally; a conditional lower bound is only a conditional result.

An upper or lower bound for a larger space regime does not decide this smaller bit budget. The task does not demand reconstructing the original grammar or reporting long substrings, and it does not forbid the specified temporary query workspace.''',
 source_formulation=dict(text='Navarro asks whether efficient random access to a grammar-compressed text can avoid the additional space used for all nonterminal expansion lengths. This card retains the previously chosen exact specialization: binary grammars, total space comparable to their encoded bit size, logarithmic character access and polynomial preprocessing from the grammar.',caption='Adaptive and Scalable Data Structures, Seminar 25191 (May 2025), §5.9, p.19; query time, alphabet and construction conventions are editorial specifications.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Adaptive and Scalable Data Structures','Gonzalo Navarro (problem contributor); Michael A. Bender, John Iacono, László Kozma and Eva Rotenberg (editors)',2025,'https://doi.org/10.4230/DagRep.15.5.1','Seminar 25191, 4–9 May 2025; §5.9, p.19'),
 ref('encoding',r'Space-Efficient SLP Encoding for \(O(\log N)\)-Time Random Access','Akito Takasaka; Tomohiro I',2026,'https://doi.org/10.1007/s00224-025-10243-w','Published 13 April 2026; Introduction, Theorem 1 and following discussion; §4, Conclusions and Future Work'),
 ref('tradeoffs','Random Access in Grammar-Compressed Strings: Optimal Trade-Offs in Almost All Parameter Regimes','Anouk Duyster; Tomasz Kociumaka',2026,'https://doi.org/10.4230/LIPIcs.ICALP.2026.86','Theorems 1.1–1.2, pp.86:3–86:4; source string length n becomes N here'),
 ],
 context_blocks=[
 block('A rule reference identifies one of g variables, whereas a text position identifies one of N expanded characters. A sequence of doubling productions can make the latter identifiers much longer. This creates the distinction between the grammar encoding and a word per stored expansion length.'),
 block(r'The April 2026 encodings achieve logarithmic access but retain a \(g\lceil\log_2 N\rceil\)-bit expansion-length term in this card’s notation. The authors discuss reducing that term as future work, without proving it necessary.','encoding'),
 block(r'The ICALP 2026 trade-off uses a bit-space parameter \(Mw\) above \(g\log N\). Its matching lower bound also has parameter restrictions. Those results do not by themselves settle space \(O(g\log g)\) when the expanded text is much larger than its grammar.','tradeoffs'),
 block('This card fixes one concrete version of the seminar’s broader efficient-access question. Total persistent bits and construction from compressed input are essential parts of the target.'),
 ],
 progress=[progress('2025-05','The seminar asks whether efficient access can avoid the expansion-length storage overhead.'),progress('2026-04-13','New succinct grammar encodings support logarithmic access but retain the leading expansion-length term.','encoding'),progress('2026','ICALP establishes improved and largely matching access trade-offs in a larger-space parameter range.','tradeoffs')],
),notes,sources,'Open in the seminar source, under the explicit specialization retained here. The April 2026 encoding theorem and ICALP 2026 trade-offs do not supply this all-grammar bit-space guarantee or rule it out. Bounded primary-source checks through 17 September 2026 found no verified resolution; the review does not independently certify every later proof.',summary=[
 'A binary straight-line grammar may describe a string exponentially longer than its list of rules.',
 'The question asks for exact character access in logarithmic time using total persistent storage of O(g log g) bits.',
 'The representation must be constructed in polynomial time from the grammar itself.',
 'All retained lengths, tables and grammar bits are charged, while each query has explicitly bounded temporary workspace.',
 'The reviewed 2026 results retain a larger expansion-length space scale; a complete Lean-checked proof or refutation of this smaller-space target is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
