"""Complete the optimal deterministic preprocessing exponent for binary histograms."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7364';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the full optimal-preprocessing exponent with absolute 1/100 accuracy; did not automatically convert the newest upper bound into a barrier question.',
 'Specified binary histogram existence queries, contiguous substrings and exact constant-time answers with a linear-word stored index.',
 'Expanded deterministic uniformity, charged preprocessing, parameter-dependent programs and the order of the exponent-slack quantifiers.',
 'Separated construction workspace from retained index space and ruled out input-dependent free tables or query history.',
 'Checked the 2026 deterministic convolution consequence, alphabet restrictions in the old hardness paper and newer space/query tradeoffs.',
 'Preserved importance 84 and required an unconditional Lean-checked approximation to the infimum rather than only an algorithmic upper bound.',
]
sources=[
 'Read Amir–Chan–Lewenstein–Lewenstein, On Hardness of Jumbled Indexing, arXiv:1405.0189v1, 1 May 2014: abstract and Section 1.1. Binary histogram-existence queries have an O(n)-word, O(1)-query representation; the conditional hardness results concern growing alphabets or fixed alphabet sizes at least three. They are not an unconditional binary preprocessing lower bound. The live history contains only v1.',
 'Read Jin–Park–Saha–Xu, arXiv:2605.07150v2, 29 May 2026: Table 3, the following explanation of the binary-indexing consequence, Theorem 1.3 and Corollary 1.4. The deterministic monotone convolution theorem yields binary jumbled-index construction in n^(1.5+o(1)) time. The n^1.864 entry is the previous deterministic bound, not the new one.',
 'Read Cunha–Medina, Binary jumbled indexing: suffix tree histogram, Journal of Combinatorial Optimization 51, Article 32, published 14 March 2026: primary abstract, Introduction and Section 4 scope. The source describes practical gains and special-case linear behavior while retaining quadratic average growth. Claims about vectorized memory access are not treated as a universal linear word-RAM instruction bound; no independent proof audit of the source analysis was performed.',
 'Read Dinur–Golovnev, Improved Time-Space Tradeoffs for 3SUM-Indexing, ICALP 2026 Article 78: primary HTML abstract and Corollary 7, including its restatement in the applications section. The jumbled-indexing space/query tradeoff S=tilde O(n^(2.5-delta)), T=tilde O(n^delta), 0<=delta<=1, does not give the simultaneous linear-word space and constant query time of this card. An initial volume search snippet was adjacent to Article 79; the actual result was checked in Article 78, not misattributed.',
 'Bounded primary-source searches through 17 September 2026 located no verified unconditional interval of width 1/50 for the defined optimal deterministic exponent. Approximate, occurrence-reporting, larger-alphabet and practical distribution-dependent variants were kept separate.',
]
complete(identifier,dict(
 title='Preprocessing exponent of binary jumbled indexing',criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, to absolute error at most \(1/100\), the real number
\[
 \alpha_{\mathrm{BJ}}=inf\{a\in[1,\infty):
 \text{for every rational }\eta>0\text{ there is an admissible index with}
 \text{ preprocessing time }O(n^{a+\eta})\}.
\]
An admissible index is a uniform deterministic static index for every binary string of length \(n\ge2\), using \(O(n)\) stored words and answering each exact histogram-existence query in \(O(1)\) worst-case time. The input, query, machine model and quantifiers are specified below.''',
 definitions=r'''The input is an explicit binary string \(T\in\{0,1\}^{n}\), supplied with one symbol per word. A valid query is a pair of nonnegative integers \((u,v)\) with \(1\le u+v\le n\), supplied in two words. Its answer is yes exactly when some contiguous substring of \(T\) has \(u\) zeros and \(v\) ones. The order of symbols within the substring is irrelevant to this query, but contiguity is required. The query asks for existence only, not the number of occurrences, a witness position or a list of all occurrences. Every answer must be exact.

For a proposed real exponent \(a\ge1\) and fixed rational slack \(\eta>0\), the required index consists of finite deterministic preprocessing and query programs, an integer \(B\ge8\), and constants \(K,C,Q>0\). For all \(n\ge2\) and all input strings, preprocessing halts within \(Kn^{a+\eta}\) instructions and leaves at most \(Cn\) stored words. For every valid query on the resulting index, the query program returns the correct Boolean answer within \(Q\) instructions. The programs and constants may depend on \(a,\eta\), but not on \(n,T,u,v\). They receive no real-valued parameter as input. The same fixed pair of programs must handle every string and length for that parameter choice.

Use a sequential word RAM with \(w=B\lceil\log_2(n+2)\rceil\)-bit words. Allowed unit-cost instructions are word reads and writes, copying, comparison, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder with a nonzero divisor. Shifts by at least \(w\) return zero. Values and addresses fit words. Multiword operations pay for their constituent instructions. All initialization, input reading, arithmetic, temporary computation and index construction are charged to preprocessing. There is no randomness, advice, external oracle or free size-dependent lookup table.

Stored space includes the retained text, all input-dependent parameters and every persistent table or auxiliary structure. A query has access only to this counted index and its supplied pair; the original string is not otherwise available for free. Each query starts without input-dependent private state from previous queries and leaves no private persistent cache outside the counted index. Its temporary registers and memory are charged in the usual RAM model. Because a query takes constant time, it can access only constantly many working words. Construction workspace is not separately restricted to linear size, but its initialization and use count toward the preprocessing time and obey the word-address model. The stored-space bound is in words, equivalently \(O(n\log n)\) bits, not \(O(n)\) bits.

The infimum is over the above exponents and is unconditional. Ordinary quadratic preprocessing already makes the set nonempty; faster known construction bounds do not imply optimality. The infimum need not be attained by an algorithm with time \(O(n^{\alpha_{\mathrm{BJ}}})\). In particular, the quantifiers allow different finite programs for different positive slacks. They do not require a single program simultaneously realizing every slack, or efficient dependence of program descriptions on the slack. This card asks for the optimal exponent, not the exact logarithmic factors at that exponent.''',
 answer_criterion=r'''Supply a specified real number \(b\) and a complete mathematically correct proof checked in Lean that
\[
 |b-\alpha_{\mathrm{BJ}}|\le\frac1{100}.
\]
A proved enclosing interval of width at most \(1/50\) qualifies by its midpoint. A finite mathematical expression is acceptable; a decimal expansion is not required. Restating the defining infimum is not a determination.

The proof must concern the full admissible deterministic algorithm class with linear stored word space and constant worst-case query time. An upper bound from one construction, a lower bound only for a particular implementation or model restriction, or an assumed hardness conjecture does not by itself establish the required unconditional two-sided result. Bounds for larger alphabets or reporting all occurrences cannot be substituted without a valid reduction preserving the full guarantees. The tolerance is on the real exponent, not an additive tolerance on a big-O expression.''',
 source_formulation=dict(text='Binary jumbled indexing preprocesses a binary text so that a pair of symbol counts can be tested in constant time using linear word space. This card asks for the infimal deterministic preprocessing exponent, retaining the approved optimal-preprocessing topic and the numerical answer criterion.',caption='Editorial exponent target based on the binary indexing model and the 2026 deterministic convolution consequence.',citation='primary',format='editorial_paraphrase'),
 why='Binary histogram queries isolate a basic form of order-insensitive search while keeping queries and the stored index small. Determining the construction exponent would clarify the real cost of preparing all such queries and its connection to structured convolution.',
 references=[
 ref('primary','On Hardness of Jumbled Indexing','Amihood Amir; Timothy M. Chan; Moshe Lewenstein; Noa Lewenstein',2014,'https://arxiv.org/abs/1405.0189v1','1 May 2014; abstract and Section 1.1, binary indexing and the alphabet restrictions of hardness results'),
 ref('deterministic','Deterministic Monotone Min-Plus Product and Convolution','Ce Jin; Jaewoo Park; Barna Saha; Yinzhan Xu',2026,'https://arxiv.org/abs/2605.07150v2','29 May 2026 revision; Table 3, its following remark, Theorem 1.3 and Corollary 1.4'),
 ref('practical','Binary jumbled indexing: suffix tree histogram','Luís Cunha; Mário Medina',2026,'https://doi.org/10.1007/s10878-026-01407-6','Journal of Combinatorial Optimization 51, Article 32; 14 March 2026; abstract and Section 4'),
 ref('tradeoffs','Improved Time-Space Tradeoffs for 3SUM-Indexing','Itai Dinur; Alexander Golovnev',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.78','ICALP 2026, Article 78; abstract and Corollary 7 for jumbled indexing'),
 ],
 context_blocks=[
 block('A binary histogram has only two counts. Testing its existence differs from literal pattern matching and from reporting all matching substring positions; the constant query-time requirement here concerns just the Boolean answer.'),
 block('The old hardness paper separates binary indexing from alphabets of size at least three. Its conditional larger-alphabet bounds therefore do not determine this binary exponent.'),
 block('The 2026 derandomization gives a construction bound of n to the power 1.5 plus a vanishing exponent term. This is an upper-bound contribution, not a proof that the exponent is optimal.','deterministic'),
 block('Suffix-tree histogram methods can improve practical performance or special inputs while still exhibiting quadratic growth in the source’s general analysis. Vectorized memory-access claims do not count as constant-cost operations on arbitrary-length arrays in this RAM model.','practical'),
 block('The new 3SUM-indexing tradeoffs transfer to jumbled indexing, but their simultaneous space and query bounds differ from the linear-space, constant-query combination required here.','tradeoffs'),
 ],
 progress=[progress('2014-05-01','The primary source records the binary linear-word, constant-query representation and separately proves conditional hardness for larger alphabets.'),progress('2026-05-29','Deterministic monotone convolution yields binary jumbled-index preprocessing in n^(1.5+o(1)) time.','deterministic')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified unconditional determination of the optimal deterministic preprocessing exponent to absolute accuracy 1/100. The 2026 deterministic upper bound and other space/query or practical improvements do not supply a matching lower bound for this exact binary existence-query model. Complete cited proofs were not independently certified.',summary=[
 'A query asks whether a binary text contains a contiguous substring with two specified symbol counts.',
 'The index must use linear word space and answer every query exactly in constant worst-case time.',
 'The numerical target is the infimum of deterministic preprocessing exponents, allowing a separate program for each positive exponent slack.',
 'The 2026 construction gives an exponent upper bound of 1.5 without determining the optimal value.',
 'Acceptance requires a complete unconditional Lean-checked approximation to that exponent within 0.01.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
