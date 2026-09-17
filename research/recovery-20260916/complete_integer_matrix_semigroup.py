"""Review unrestricted semigroup membership for two-dimensional integer matrices."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5921';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='decision',question_type='yes_no',
 formal=r'''Does there exist an algorithm which, for every finite list \(A_1,\ldots,A_k\in\mathbb Z^{2\times2}\), with \(k\ge1\), and every target \(B\in\mathbb Z^{2\times2}\), decides whether
\[
\exists \ell\ge1\ \exists i_1,\ldots,i_\ell\in\{1,\ldots,k\}:
A_{i_1}A_{i_2}\cdots A_{i_\ell}=B?
\]
All matrix entries are arbitrary signed integers; singular and nonsingular generators may occur together. The algorithm must halt on both positive and negative instances.''',
 definitions=r'''A \(2\times2\) integer matrix is an array of four integers, with multiplication
\[
(XY)_{ij}=\sum_{h=1}^{2}X_{ih}Y_{hj}.
\]
Equality requires equality in every entry. A matrix is singular when its determinant \(X_{11}X_{22}-X_{12}X_{21}\) is zero; no determinant restriction is imposed here.

The generated semigroup consists of all nonempty finite products of the listed generators. Their order matters, generators may be reused arbitrarily often, and there is no bound on the product length. Inverses are not automatically available. The identity matrix is an admissible target, but is accepted only if a nonempty product equals it. In particular the empty word is not a witness. The zero matrix and all rank-one matrices are also admissible as generators or targets. Duplicate generators are harmless. Allowing an empty input list would just add instances whose answer is always no.

Input uses explicit lists of all four entries of each matrix, encoded as signed binary integers with fixed length delimiters. The number of generators is part of the input and is unbounded. A decider means one deterministic Turing machine acting on these finite encodings, with no oracle or advice, which always terminates and gives the exact yes/no answer. No polynomial or other prescribed time bound is requested. The entries, generators and product length are not parameters that may be hardcoded into different machines.

Enumeration of all nonempty words gives a procedure that eventually accepts every positive instance. The requested decider must additionally terminate and reject when no product reaches the target. This is semigroup membership, not subgroup membership or membership in the topological closure of the generated set.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof that such a decider exists, including termination and both directions of correctness, or a proof that this exact decision problem is undecidable. A semidecision procedure, a bound applying only to nonsingular matrices, or a solution for determinants restricted to 0 and plus or minus 1 is insufficient. No efficient complexity bound or explicit product witness is required for an affirmative answer.',
 why='Dimension two is a sharp unresolved boundary for exact reachability by integer matrix products. The combination of rank loss and determinant growth escapes algorithms for several important restricted matrix classes.',
 importance=dict(score=82,method='editorial',reason='A longstanding low-dimensional decidability boundary for algebraic reachability, including matrix mortality and unrestricted mixtures of singular and nonsingular transitions.'),
 source_formulation=dict(text='The source explicitly leaves open decidability of membership for arbitrary 2 by 2 integer matrix semigroups, with nonempty generator products.',caption='ICALP 2019, Introduction, printed p.44:2.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On Reachability Problems for Low-Dimensional Matrix Semigroups','Thomas Colcombet; Joël Ouaknine; Pavel Semukhin; James Worrell',2019,'https://doi.org/10.4230/LIPIcs.ICALP.2019.44','Introduction p.44:2: nonempty-product convention, two decidable subclasses, and the unrestricted integer 2 by 2 question'),
 ref('later','Decidability of Membership Problems for Flat Rational Subsets of GL(2, Q) and Singular Matrices','Volker Diekert; Igor Potapov; Pavel Semukhin',2024,'https://doi.org/10.1137/22M1512612','SIAM J. Comput. 53(6), 1663–1708; accepted manuscript Introduction pp.1–3 and §9 pp.42–43; https://livrepository.liverpool.ac.uk/3186268/1/2024SIAMfinal_submittion.pdf'),
 ],
 context_blocks=[
 block('The 2019 account distinguishes decidability when all generators are nonsingular from decidability when every determinant is 0 or plus or minus 1. Neither restriction is imposed by this card.'),
 block('General integer matrix membership becomes undecidable in dimension three, whereas the unrestricted dimension-two case is left open in the source.'),
 block('The 2024 journal extension develops decidability for flat rational sets over specified matrix submonoids. Its Introduction still identifies open integer dimension-two problems, including mortality.','later'),
 block('Those flat-set theorems constrain how matrices outside the underlying submonoid may occur. They do not provide a decider for unrestricted products of every possible integer generator.','later'),
 block('Taking the target to be zero gives matrix mortality, a special case of this question. Taking an invertible target instead prevents singular factors from appearing in a successful product; allowing arbitrary targets is consequential.'),
 ],
 progress=[progress('2019','The source records decidable determinant-restricted cases and states the general integer dimension-two problem as open.'),progress('2024','The journal treatment extends structured rational-set decidability without claiming the unrestricted integer semigroup problem solved.','later')],
),[
 'Retained arbitrary integer entries, an unbounded input generator list, arbitrary target and nonempty product semantics.',
 'Made mixed singular/nonsingular generators and termination on negative instances explicit.',
 'Read the original open passage and the 2024 journal extension without treating restricted flat rational sets as arbitrary generated semigroups.',
 'Assessed importance individually and required complete Lean-checked decidability or undecidability.',
],[
 'Read ICALP 2019 Introduction p.44:2, including its explicit nonempty-product definition and unrestricted 2 by 2 integer question.',
 'Read the final accepted 2024 SIAM manuscript Introduction pp.1–3 and §9 pp.42–43. Checked the stated restrictions of the singular-matrix extension.',
 'Bounded primary-source searches through 17 September 2026 did not locate a resolution of arbitrary integer 2 by 2 semigroup membership.',
], 'Source-open for unrestricted 2 by 2 integer matrices and nonempty products. The 2024 structured rational-set extensions do not remove the determinant and product-form restrictions needed to decide the general case. Bounded status review through 17 September 2026.',summary=[
 'The input is a finite list of integer matrices of size two by two and a target matrix of the same size.',
 'The question asks whether any nonempty finite product of the listed matrices equals the target exactly.',
 'Generators may repeat and may include both singular and nonsingular matrices with arbitrary determinants.',
 'The desired algorithm must terminate on every input, without any prescribed running-time bound.',
 'A complete Lean-checked decision procedure or undecidability proof must cover the unrestricted input class.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
