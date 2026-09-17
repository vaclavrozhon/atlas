"""Apply the user's faster query-time choice for the linear-space mismatch index."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7366';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user’s 17 September 2026 choice: O(n) words and the sharper O(m+log^k(n)*log log(n)+occ) query time for every fixed k>=2.',
 'Removed the arbitrary polylogarithmic query exponent, whose weaker goal overlaps older linear-space results at least on constant alphabets.',
 'Specified exact Hamming matching, all pattern lengths from one to n, integer alphabet [0,n), all occurrences without duplicates and arbitrary reporting order.',
 'Made fixed-k uniformity, constants, polynomial preprocessing and total retained/query memory explicit; k is fixed before choosing the program.',
 'Read the main general-alphabet theorem, constant-alphabet comparison, long-pattern theorem and preprocessing caveat in the SODA 2026 source.',
 'Preserved the honest verification limit for the full alphabet scope of the 2011 slower-query result; it is not needed to justify or decide the newly selected faster target.',
 'Preserved importance 88, the existing relation to TCS-7367 and the complete Lean-checked binary answer criterion.',
]
sources=[
 'Read Kociumaka–Radoszewski, Space-Efficient k-Mismatch Text Indexes, arXiv:2510.26264v1, 30 October 2025, SODA 2026 DOI 10.1137/1.9781611978971.68, 7 January 2026, pp.1873–1902: Introduction, Table 1, Theorems 1.1, 1.2 and 1.5, and Section 9, pp.31–32 of the preprint. The general-alphabet theorem has O(n log^(k-1)n) words and O(m+log^k(n)*log log n+occ) queries. The long-pattern result has a length restriction and does not cover every m. The conclusion explicitly seeks further space reduction and separately notes missing efficient-construction analyses for black-box components.',
 'Read Chan–Lam–Sung–Tam–Wong’s primary CPM 2006 talk, https://cpm.cs.helsinki.fi/cpm06/03-tam.pdf, including the setup explicitly assuming a constant-size alphabet and its linear-space, larger-polylog-query guarantee. Read the primary Springer chapter abstract and two-page preview, DOI 10.1007/11780441_6. The 2011 journal abstract/metadata, DOI 10.1016/j.jda.2011.04.004, and Table 1 of the directly read 2026 paper attribute the O(n)-space query overhead log^(k(k+1))(n)*log log n. The 2011 full proof was inaccessible; its general-alphabet scope was not independently verified.',
 'Read Cohen-Addad–Feuilloley–Starikovskaya, Lower bounds for text indexing with mismatches and differences, SODA 2019, primary HAL paper https://hal.science/hal-01960182/document, Introduction and Figure 3. It records the old trade-off; its conditional/growing-k and pointer-model statements are not an unconditional refutation of this fixed-k word-RAM target.',
 'On 17 September 2026 the user explicitly selected the sharper source-style query bound with O(n) words over alphabet [0,n), after being told of the weak-target overlap and the limits of the 2011 alphabet verification. This supersedes the inherited arbitrary-polylogarithmic-overhead formulation.',
 'Fresh primary-source searches and arXiv metadata checks through 17 September 2026 found no verified resolution of the selected simultaneous space/query guarantee. The checked arXiv history still lists v1. This review does not certify unpublished near-linear preprocessing for the new structures; the card asks only polynomial preprocessing for each fixed k.',
]
complete(identifier,dict(
 title='Linear-space k-mismatch indexing with fast queries',criterion='resources',question_type='yes_no',
 formal=r'''For every fixed integer \(k\ge2\), do there exist constants \(C_k,K_k>0\), integers \(p_k\ge1\) and \(B_k\ge8\), and one uniform deterministic static indexing algorithm \(A_k\) with the following properties? For every \(n\ge2\) and text \(T\in\{0,\ldots,n-1\}^n\), it constructs an index in at most \(K_kn^{p_k}\) word-RAM instructions using at most \(C_kn\) retained words. Every subsequently supplied pattern \(P\in\{0,\ldots,n-1\}^m\), \(1\le m\le n\), has all its occurrences with at most \(k\) mismatches reported exactly in at most
\[
K_k\left(m+\bigl(\log_2(n+2)\bigr)^k
                  \log_2\log_2(n+2)+\mathrm{occ}\right)
\]
worst-case instructions. The index together with all temporary query work uses at most \(C_kn\) words. Here \(\mathrm{occ}\) is the number of reported positions and the word length is \(B_k\lceil\log_2(n+2)\rceil\).''',
 definitions=r'''The text and pattern are explicit arrays, one alphabet symbol per word, with zero-based indices. A mismatch is a position at which two aligned characters differ. The required output is the set
\[
\operatorname{Occ}_k(T,P)=
\left\{i\in\{0,\ldots,n-m\}:\left|\{j\in\{0,\ldots,m-1\}:T[i+j]\ne P[j]\}\right|\le k\right\},
\]
and \(\mathrm{occ}=|\operatorname{Occ}_k(T,P)|\). Every position in this set must be returned once, no other position may be returned, and any reporting order is allowed. Overlapping occurrences are included. Only substitutions are allowed; insertions, deletions, wildcards and cyclic rotations are not part of the matching condition. There is no promise on \(m\) relative to \(k\); if \(m\le k\), every possible alignment qualifies.

Preprocessing knows \(k,n,T\) but no query pattern. The text is static, and after construction the same representation must support every valid pattern. All retained text copies, samples, tables and auxiliary information count toward the linear word bound. A query begins without input-dependent private state outside that representation. Temporary query storage, including registers, also counts; the supplied read-only pattern and a write-only stream of reported positions may be excluded. Output memory cannot serve as uncharged working storage, and writing each reported position is included in the query time. Construction may use additional temporary storage, discarded before queries; all construction work is charged to the polynomial preprocessing bound.

For each fixed \(k\), both construction and query programs are fixed finite deterministic programs independent of \(n,T,P\). The constants, polynomial preprocessing exponent and word-size factor may depend on \(k\). This is a separate uniform algorithm for each fixed error budget, not a requirement that one program have comparable bounds when \(k\) grows with \(n\). The logarithmic query exponent is exactly the selected \(k\), not an unspecified larger function of \(k\). There is no restriction to a fixed-size alphabet: all \(n\) symbols may be used in arbitrary inputs. The shifted logarithms make the bound positive for every \(n\ge2\) without changing its asymptotic meaning.

Computation uses a sequential word RAM. Unit-cost instructions are word reads and writes, copying, comparisons, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder for a nonzero divisor. Shifts by at least \(w\) return zero. Addresses and stored values fit in words, and multiword computations pay for their constituent instructions. No randomization, advice, external oracle, uncharged preprocessing or free size-dependent lookup table is available. All initialization, input access, arithmetic and output writes count. The query guarantee is exact and worst-case for every valid pattern, not expected, amortized or averaged over a pattern distribution. Space is measured in words, not bits.

The quantifier order is \(\forall k\,\exists(A_k,C_k,K_k,p_k,B_k)\,\forall(n,T)\,\forall P\), with the representation constructed from \(T\) before \(P\) is known. The answer may establish the theorem for all fixed \(k\) by one general construction, but no computable uniform dependence of the selected programs on \(k\) is imposed beyond this stated quantification.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the displayed proposition or its logical negation. A positive answer must establish the full claim for every fixed \(k\ge2\), including exact reporting, polynomial construction, linear retained-plus-query space and the specified worst-case query bound over the full integer alphabet.

A linear-space index with a larger logarithmic query exponent, an index with an extra logarithmic space factor, or a result limited to long patterns or constant-size alphabets does not meet the target. Solving only one chosen error budget does not establish the universal positive answer; an unconditional refutation for one fixed allowed budget would refute it. Lower bounds for growing error budgets, restricted machines or additional conjectural assumptions establish only their stated conclusions. There is no additive numerical tolerance on this existence question.''',
 source_formulation=dict(text='The source asks to reduce k-mismatch index space further while its main theorem retains the k-errata-tree query bound. On 17 September 2026 the user selected the endpoint O(n) words with O(m+log^k(n) log log(n)+occ) queries for each fixed k>=2 over alphabet [0,n), replacing the previously imported arbitrary-polylogarithmic query allowance. Linear space is the chosen endpoint of the source’s broader space-reduction question, not a claimed quotation of an equivalent source conjecture.',caption='Kociumaka–Radoszewski, Theorem 1.1 and Section 9; explicit user scope decision of 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='Approximate text indexing serves many patterns against the same stored text. The question asks whether the fast fixed-error query interface can be kept in linear word space even when the alphabet grows, removing the storage overhead that can dominate large indexes.',
 references=[
 ref('primary','Space-Efficient k-Mismatch Text Indexes','Tomasz Kociumaka; Jakub Radoszewski',2026,'https://arxiv.org/abs/2510.26264v1','30 October 2025 preprint; SODA 2026, 7 January, pp.1873–1902, DOI 10.1137/1.9781611978971.68; Table 1, Theorems 1.1, 1.2, 1.5 and Section 9'),
 ref('oldtalk','A Linear Size Index for Approximate String Matching','Ho-Leung Chan; Tak-Wah Lam; Wing-Kin Sung; Siu-Lung Tam; Swee-Seong Wong',2006,'https://cpm.cs.helsinki.fi/cpm06/03-tam.pdf','Authors’ CPM 2006 talk, 5 July; setup explicitly assumes constant-size alphabet; larger-polylogarithm query trade-off'),
 ref('oldjournal','A linear size index for approximate pattern matching','Ho-Leung Chan; Tak-Wah Lam; Wing-Kin Sung; Siu-Lung Tam; Swee-Seong Wong',2011,'https://doi.org/10.1016/j.jda.2011.04.004','Journal of Discrete Algorithms 9(4):358–364; primary abstract/metadata only; query bound also recorded in Table 1 of the directly read SODA 2026 paper'),
 ref('lower','Lower bounds for text indexing with mismatches and differences','Vincent Cohen-Addad; Laurent Feuilloley; Tatiana Starikovskaya',2019,'https://hal.science/hal-01960182','SODA 2019; primary version submitted 21 December 2018; Introduction and Figure 3, model and growing-error scope'),
 ],
 context_blocks=[
 block('The text is indexed before the pattern arrives, so this problem differs from computing approximate matches for one already supplied pattern. Its output term pays for reporting every valid starting position.'),
 block(r'The main general-alphabet theorem uses \(O(n\log^{k-1}n)\) words while retaining query time \(O(m+\log^k n\log\log n+\mathrm{occ})\). The selected target removes the remaining space factor without relaxing that query bound.'),
 block('Older linear-space trade-offs permit a larger logarithmic query exponent. Their existence motivated replacing the inherited arbitrary-polylogarithmic goal with the faster query target explicitly selected by the user.'),
 block('The paper obtains stronger space savings for constant alphabets and a nearly linear index for sufficiently long patterns. These restrictions do not cover the full alphabet and all pattern lengths required here.'),
 block('The conclusion also discusses construction analyses missing for some components. This card requires polynomial construction for each fixed error budget; it does not credit an unproved near-linear construction bound.'),
 block('Existing conditional or model-specific lower bounds need their own error-budget and machine assumptions. They are not treated as an unconditional answer to this fixed-error word-RAM question.','lower'),
 ],
 progress=[progress('2006','The authors’ talk presents linear-space approximate indexing on constant alphabets with a slower polylogarithmic query term.','oldtalk'),progress('2011','The later journal trade-off is attributed a log^(k(k+1))(n) log log(n) overhead at linear space in the modern source; its full alphabet scope was not independently reverified.','oldjournal'),progress('2026-01-07','SODA 2026 presents the general-alphabet O(n log^(k-1)n)-space index at the selected fast query time and asks for further space reductions.')],
),notes,sources,'On 17 September 2026 the user selected linear space with the faster log^k(n) log log(n) query overhead, superseding the weaker arbitrary-polylog target. Bounded primary-source checks through that date found no verified resolution of the selected full-alphabet, all-pattern-length guarantee. The source explicitly asks for further space reductions; the older slower linear-space result’s full alphabet scope remains unverified and is not presented as a solution to this sharper target. Construction and lower-bound claims retain their stated verification limits.',summary=[
 'A fixed text is indexed so that later patterns can be searched with at most a fixed number of substitutions.',
 'Every matching starting position must be reported exactly, including overlaps.',
 'The user-selected target is linear word space with query cost O(m+log^k(n) log log(n)+occ) for each fixed k at least two.',
 'The guarantee must hold for all pattern lengths and an alphabet that can grow to the text length.',
 'A complete Lean-checked answer must prove or refute these simultaneous bounds; slower-query linear-space trade-offs do not suffice.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
