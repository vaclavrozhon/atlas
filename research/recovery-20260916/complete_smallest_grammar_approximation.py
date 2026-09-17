"""Review the universal constant-factor smallest-grammar approximation target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6513';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained deterministic polynomial bit-time, an unrestricted input alphabet and any absolute constant approximation ratio.',
 'Specified the exact acyclic one-rule-per-variable grammar, unique start expansion and total right-hand-side-symbol size measure.',
 'Made both input and output explicit binary encodings and charged all computation and output writing.',
 'Separated hardness for ratios below 8569/8568 from nonexistence of every constant approximation.',
 'Read the fixed-alphabet paper’s explicit Open Problem 2 and retained this target rather than exact optimization or a PTAS.',
 'Checked recent assembly-index work at the abstract level and distinguished empirical performance from an all-string approximation theorem.',
 'Preserved the assigned importance and added a complete Lean-checked answer criterion with an unconditional-versus-conditional distinction.',
]
sources=[
 'Read Charikar and coauthors, The Smallest Grammar Problem, IEEE Transactions on Information Theory 51(7), 2554–2576 (2005), DOI 10.1109/TIT.2005.850116, author-hosted January 2005 manuscript https://shelat.khoury.northeastern.edu/dl/GrammarIEEE.pdf: abstract, Introduction size definition, Section V-A Theorem 1 and Section VII approximation discussion. The hardness threshold is strictly below 8569/8568 unless P=NP; the upper bound is logarithmic in string length divided by optimum grammar size. The author-hosted draft has a byline differing from some journal metadata, so the reference identifies the author group without silently asserting identical bylines.',
 'Read Casel–Fernau–Gaspers–Gras–Schmid, On the Complexity of the Smallest Grammar Problem over Fixed Alphabets, DOI 10.1007/s00224-020-10013-w, online 13 November 2020, Theory of Computing Systems 65 (2021), 344–409: abstract, Section 2 grammar conventions and Section 6.2 including Open Problem 2. It explicitly asks for a constant-factor approximation and explains why APX-hardness on alphabets of size at least 17 does not settle that question. Read the full primary HTML after the linked HPI PDF returned HTTP 403.',
 'Read the primary arXiv abstract of Bieniawski, Assembly Theory and the Smallest Grammar Problem, arXiv:2608.19228, 2026. It describes an empirical evaluation on 408 strings and a branch-and-bound tie-resolving variant of Re-Pair. The abstract does not claim a uniform polynomial-time constant approximation for every input under this card’s size convention. Only the abstract was checked; no independent proof audit is claimed.',
 'Bounded primary-source searches through 17 September 2026 found no verified resolution of the universal constant-factor target. Fixed-alphabet exact hardness, particular compressor lower bounds, empirical comparisons and alternative assembly-size measures were kept separate.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist absolute constants \(C\ge1\), \(K\ge1\), an integer \(d\ge1\), and one uniform deterministic algorithm \(A\) such that, for every \(n\ge1\) and explicitly supplied string \(s\in\{1,\ldots,n\}^n\), the algorithm outputs an acyclic grammar \(G\) generating exactly \(s\), with
\[
|G|\le C\,g^*(s),
\]
in at most \(K(L(s)+1)^d\) Turing-machine bit steps? Here \(|G|\) is the total number of terminal and nonterminal occurrences on all right-hand sides, \(g^*(s)\) is the minimum such size among grammars generating \(s\), and \(L(s)\) is the explicit binary input length.''',
 definitions=r'''A permitted grammar consists of ordered nonterminals \(X_1,\ldots,X_r\), one production \(X_j\to\alpha_j\) per nonterminal, and start nonterminal \(X_r\). Each \(\alpha_j\) is a finite nonempty sequence whose entries are terminals from \(\{1,\ldots,n\}\) or references to \(X_i\) with \(i<j\). Every nonterminal is reachable from the start. The order makes the dependency graph acyclic, and each variable has exactly one expansion into terminals. The expansion of \(X_r\) must equal \(s\), symbol for symbol. There are no alternatives, cycles, empty productions, reversal instructions, iteration instructions or extra generated strings. Right-hand sides may have arbitrary positive length; they need not be binary concatenations.

The size is \(|G|=\sum_{j=1}^r|\alpha_j|\). Every occurrence of a terminal or a referenced nonterminal contributes one unit, even when the same entry occurs repeatedly. This counts neither just the number of productions nor the binary description length. A repeated block written many times on a right-hand side is charged for each occurrence; a run-length exponent is not a substitute. The optimum \(g^*(s)\) ranges over all permitted grammars, independently of the algorithm. It exists and satisfies \(1\le g^*(s)\le n\), since one production containing \(s\) is permitted. Ordering the acyclic dependencies and removing unreachable rules does not change the optimal value.

For definiteness, let \(\operatorname{code}(a)\), \(a\ge0\), consist of \(1^b0\) followed by the \(b\)-bit binary representation of \(a+1\), where \(b=\lfloor\log_2(a+1)\rfloor+1\). The input is \(\operatorname{code}(n)\), followed by the \(n\) symbols, each in \(\lceil\log_2(n+1)\rceil\) bits. Its full length is \(L(s)\). The alphabet is not required to have a fixed size, and symbols not used by \(s\) are allowed in the ambient alphabet.

The output explicitly lists \(r\), then for each production its right-hand-side length and all its entries. Lengths and identifiers use the same self-delimiting code, and each entry has a one-bit terminal/nonterminal tag. The start is \(X_r\). Writing this entire binary output counts toward runtime. The approximation inequality still uses the stated symbol-occurrence size, not the number of output bits.

The computational model is a fixed finite deterministic multitape Turing machine with finite tape alphabets, read-only binary input, initially blank work tapes and a binary output tape. Each step reads or writes the cells under its heads and moves each head at most one cell. All parsing, preprocessing, computation and output writing are charged. There is no advice, oracle, randomness, quantum computation or unit-cost arithmetic on unbounded integers. No separate workspace bound is imposed. Malformed inputs may be rejected in polynomial time.

The quantifier order is \(\exists(C,K,d,A)\,\forall n\,\forall s\). The approximation factor and runtime exponent cannot depend on string length, alphabet size, repetition pattern or optimum grammar size. The task is to produce a grammar, not only estimate its minimum size. Exact optimization and approximation arbitrarily close to one are stronger targets than required here.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive proof must construct one deterministic polynomial-time algorithm and prove its grammar is valid and within one fixed factor of the optimum for every allowed string. A negative proof must rule out every fixed constant factor and polynomial-time algorithm unconditionally. A theorem under \(\mathrm P\ne\mathrm{NP}\) or another unproved hypothesis must be identified as conditional and does not alone prove the logical negation.

Hardness of exact optimization, a PTAS, or some small approximation constants does not refute all constant factors. An empirical bound, a guarantee only for a restricted string family, or a lower bound for one particular compressor does not decide the proposition. A proof in a different grammar-size convention must justify its transfer to the convention stated here.''',
 source_formulation=dict(text='Open Problem 2 asks whether the smallest grammar problem admits a constant-factor approximation. This card retains the deterministic polynomial-time interpretation, the sum-of-right-hand-side-lengths size measure and an alphabet that can grow with the explicit input.',caption='Casel et al., On the Complexity of the Smallest Grammar Problem over Fixed Alphabets, §6.2, Open Problem 2; online November 2020, journal volume 2021.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On the Complexity of the Smallest Grammar Problem over Fixed Alphabets','Katrin Casel; Henning Fernau; Serge Gaspers; Benjamin Gras; Markus L. Schmid',2021,'https://doi.org/10.1007/s00224-020-10013-w','Online 13 November 2020; §2, grammar conventions; §6.2, Open Problem 2'),
 ref('classical','The Smallest Grammar Problem','Moses Charikar and coauthors',2005,'https://doi.org/10.1109/TIT.2005.850116','Introduction size definition, §V-A Theorem 1 and §VII approximation algorithms; author manuscript at https://shelat.khoury.northeastern.edu/dl/GrammarIEEE.pdf'),
 ref('empirical','Assembly Theory and the Smallest Grammar Problem','Wawrzyniec Bieniawski',2026,'https://arxiv.org/abs/2608.19228','Primary abstract: empirical evaluation and branch-and-bound Re-Pair variant; not a verified universal approximation theorem'),
 ],
 context_blocks=[
 block('A grammar names reusable pieces and combines them hierarchically. The optimum measures how economically this can be done, while the algorithm must find a comparably small representation from the explicit string.'),
 block(r'The classical guarantee is \(O(1+\log(n/g^*(s)))\). The same work excludes ratios strictly below \(8569/8568\) unless \(\mathrm P=\mathrm{NP}\). This leaves the possibility of a larger universal constant.','classical'),
 block('The fixed-alphabet paper proves APX-hardness for alphabet sizes at least 17 and separately retains constant-factor approximation as an open problem. Exact hardness and absence of a PTAS do not rule out every constant.'),
 block('Recent assembly-index work evaluates compressors on finite datasets. Such comparisons can assess practical performance but do not establish the worst-case all-string guarantee required here.','empirical'),
 ],
 progress=[progress('2005','Logarithmic approximation and a conditional inapproximability threshold below 8569/8568 leave a gap between known upper and lower guarantees.','classical'),progress('2020-11-13','Fixed-alphabet hardness is established, while constant-factor approximation remains an explicit separate open question.'),progress('2026','An empirical assembly-index study compares compression heuristics without claiming the universal target.','empirical')],
),notes,sources,'The constant-factor target is explicitly open in the fixed-alphabet paper. Bounded primary-source checks through 17 September 2026 found no verified general constant-factor algorithm or theorem ruling out every constant under the specified grammar-size convention. The recent empirical abstract was checked only for scope, not independently validated as a proof.',summary=[
 'The input is any explicit string over an integer alphabet that may grow with its length.',
 'The algorithm must output an acyclic grammar whose unique expansion is that string.',
 'Grammar size counts all symbols on production right-hand sides, and the target is one universal constant times the optimum.',
 'The algorithm must be deterministic and polynomial in the full input bit length; known small-factor hardness does not rule out every constant.',
 'A complete Lean-checked proof or unconditional refutation is required, with any conditional hardness result clearly distinguished.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
