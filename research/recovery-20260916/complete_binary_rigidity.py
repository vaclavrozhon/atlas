"""Review explicit binary rigidity at the n/log log n rank scale."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1058';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist a real constant \(0<\varepsilon<1\), constants \(K>0\), \(b\in\mathbb N\), and one deterministic Turing machine which, for every integer \(n\ge4\), outputs a matrix \(A_n\in\mathbb F_2^{n\times n}\) within \(Kn^b\) steps, such that
\[
\forall c>0\ \exists N_c\ge4\ \forall n\ge N_c:
R_{A_n}^{\mathbb F_2}\!\left(
\min\!\left\{n,\left\lfloor\frac{cn}{\log_2\log_2 n}\right\rfloor\right\}
\right)\ge n^{1+\varepsilon}?
\]
Here \(c\) is real, \(N_c,n\) are integers, and \(R^{\mathbb F_2}\) is the minimum number of entries that must be changed to reduce rank to the indicated value. The same matrix family and the same \(\varepsilon\) must work for every fixed \(c\).''',
 definitions=r'''The field \(\mathbb F_2=\{0,1\}\) uses addition and multiplication modulo 2. For a matrix \(A\in\mathbb F_2^{n\times n}\) and an integer \(0\le r\le n\), define
\[
R_A^{\mathbb F_2}(r)=
\min\left\{
\bigl|\{(i,j):A_{ij}\ne B_{ij}\}\bigr|:
B\in\mathbb F_2^{n\times n},\ \operatorname{rank}_{\mathbb F_2}(B)\le r
\right\}.
\]
Rank is the dimension of the column span over \(\mathbb F_2\), not over the reals. Every entry of \(B\) can be chosen independently. The cost counts changed positions in the whole matrix, not a maximum or average per row, a norm of the changes, or their numerical magnitude. The minimum exists because the candidate set is finite and contains the zero matrix. This is ordinary matrix rigidity, not a separately constrained row/column version.

The construction algorithm receives \(1^n\) and outputs all \(n^2\) bits of \(A_n\), in row-major order, on a deterministic multi-tape Turing machine. Its time bound includes writing those bits. It has no random bits, advice, noncomputable constants or oracle access. It outputs one matrix at each length, rather than a list containing an unspecified rigid member. Polynomial time in \(n\) is required; logarithmic-time computation of an individual entry is not additionally required.

All logarithms in the rank threshold are base 2. For \(n\ge4\), the iterated logarithm is positive. The minimum with \(n\) makes the rank parameter valid even before the eventual guarantee begins. For each fixed \(c\), sufficiently large \(n\) have \(\log_2\log_2 n>c\), so the clipping eventually disappears. The threshold length \(N_c\) may depend on \(c\); the algorithm, \(K,b\) and \(\varepsilon\) may not. The comparison with \(n^{1+\varepsilon}\) is an ordinary real inequality against an integer rigidity value, equivalently a lower bound by its ceiling.

The target is unconditional existence of an explicit family and a proof of its rigidity. The algorithm is not required to compute rigidity or output a certificate with each matrix. The same \(\varepsilon>0\) is fixed for the whole family, with no prescribed numerical lower bound such as \(1/100\). A rank guarantee for just one fixed \(c\), or for ranks much smaller than \(n/\log\log n\), is not the quantified target here.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the explicit-family existence statement or its logical negation. A positive answer must specify and verify the deterministic construction and prove the rigidity inequality against every binary matrix of the allowed rank, for all fixed \(c\) and all sufficiently large lengths. A random-matrix existence proof, an unselected candidate list, an oracle construction, a conditional construction, or a rigidity bound over a different field is insufficient. A negative answer must exclude all constructions with the stated properties, not merely refute a familiar proposed family.''',
 why='A sufficiently rigid explicit binary matrix gives a linear transformation whose computation resists linear-size logarithmic-depth circuits. Random matrices have strong rigidity, but obtaining the required guarantees from a uniform deterministic construction remains a central explicit lower-bound challenge.',
 source_formulation=dict(text='Jukna asks for an explicit Boolean matrix with rigidity at least n^(1+epsilon) at rank O(n/ln ln n). This card fixes the field F_2, deterministic full-matrix construction, and a guarantee for every fixed constant in that rank scale, using one positive epsilon.',caption='Boolean Function Complexity, author’s early draft, Research Problem 13.34, printed p.387 (PDF p.394); neighboring GF(2) discussion and Proposition 13.35.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Boolean Function Complexity: Advances and Frontiers (author’s early draft)','Stasys Jukna',2012,'https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf','Research Problem 13.34, printed p.387/PDF p.394; GF(2) definitions and Proposition 13.35, printed pp.387–388'),
 ref('conditional','Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank','Nikolai Chukhin; Alexander S. Kulikov; Ivan Mihajlin; Arina Smirnova',2026,'https://doi.org/10.4230/LIPIcs.STACS.2026.28','Abstract; Theorem 6 p.28:4; §1.2 matrix-rigidity comparison and explicitness footnote, printed pp.28:6–7'),
 ref('spiky','Spiky Rank and Its Applications to Rigidity and Circuits','Lianna Hambardzumyan; Konstantin Myasnikov; Artur Riazanov; Morgan Shirley; Adi Shraibman',2026,'https://eccc.weizmann.ac.il/report/2026/030/','Manuscript dated 26 February 2026; §1.2.1, Theorem 1.1 and Open Problems 1.2–1.3, printed pp.5–6'),
 ],
 context_blocks=[
 block('The rank of a matrix can fall after some of its entries are changed. Rigidity asks how many changes are unavoidable, and a lower bound must cover every low-rank replacement matrix.'),
 block('The surrounding source discusses Boolean linear maps and parity circuits, so the relevant field here is F_2. The same bit matrix can have different rank and rigidity over other fields.'),
 block('Random-matrix counting proves strong existential bounds. The open construction target requires the matrix itself to be output deterministically in polynomial time, which a counting proof alone does not provide.'),
 block('The STACS 2026 conditional result constructs small families with a rigid member at a rank scale near the square root of the dimension, under a hardness assumption. The premise, rank regime and selection of one member all distinguish it from this card.','conditional'),
 block('The 2026 spiky-rank paper develops a new route to rigidity bounds and explicitly leaves strong explicit constructions open. Its proposed matrix parameters are tools toward rigidity, rather than a construction meeting the present binary near-linear rank requirement.','spiky'),
 ],
 progress=[progress('2012','The book records the explicit binary near-linear-rank rigidity target as Research Problem 13.34.'),progress('2026','The STACS paper gives conditional generators of candidate families and distinguishes them from the Valiant regime.','conditional'),progress('2026-02-26','The spiky-rank manuscript proposes another rigidity method and retains explicit-construction challenges.','spiky')],
),[
 'Resolved the field from the source’s GF(2) context and defined ordinary entrywise rigidity rather than row/column rigidity or real rank.',
 'Applied the announced recommended interpretation of O(n/log log n): one epsilon and one family working for every fixed rank-scale constant; optional clarification had not been answered.',
 'Required one unconditional deterministic full-matrix construction in polynomial bit time, at every sufficiently large dimension.',
 'Specified all rank, logarithm, rounding and eventual-length conventions without prescribing a fixed epsilon improvement.',
 'Read the current conditional and spiky-rank results and distinguished their assumptions, rank regime and candidate-family access from this target.',
 'Preserved the existing individually assessed importance and required a complete Lean-checked construction and universal rigidity proof or the exact negation.',
],[
 'Read Jukna bool-V7 author draft Research Problem 13.34, printed p.387/PDF p.394, the preceding binary linear-operator/rank discussion and Proposition 13.35 with its GF(2) counting argument on printed pp.387–388. The source’s O(n/ln ln n) notation requires a quantifier choice; this card explicitly uses every fixed constant with one family and exponent.',
 'Read Chukhin–Kulikov–Mihajlin–Smirnova STACS 2026 abstract, Theorem 6 p.28:4, and §1.2 matrix-rigidity discussion pp.28:6–7. The theorem is conditional on a MAX-3-SAT co-nondeterministic hardness hypothesis, promises a good seed rather than selecting it, and concerns rank n^(1/2-delta); these are not the present unconditional deterministic parameters.',
 'Read Hambardzumyan–Myasnikov–Riazanov–Shirley–Shraibman ECCC TR26-030, manuscript dated 26 February 2026, §1.2.1 Theorem 1.1 and subsequent open construction problems pp.5–6. The paper states that known explicit matrices fall short of the principal rigidity applications. Its real/spiky-rank statements are not transcribed as binary-field rigidity bounds.',
 'Bounded primary-source checks through 17 September 2026 found no construction or refutation resolving the chosen binary matrix target. This is not an independent proof audit of the cited later results.',
], 'Source-open for uniform deterministic binary matrices over F_2 with n^(1+epsilon) rigidity at every fixed multiple of n/log log n, for all sufficiently large dimensions. The 2026 conditional-generator and spiky-rank results do not provide this unconditional construction. Quantifiers and field are explicit; bounded status checks through 17 September 2026 identified no resolution.',summary=[
 'The target is a deterministic polynomial-time construction of one binary square matrix at each dimension.',
 'Reducing its rank over F_2 to any fixed multiple of n divided by log log n must require changing at least n^(1+epsilon) entries.',
 'One positive epsilon and the same family must work for all fixed multiples, with a separate sufficiently-large-length threshold allowed.',
 'Random matrices, conditional constructions and unselected lists of candidates do not meet the target.',
 'A complete Lean-checked construction and rigidity proof, or the precise negation, is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
