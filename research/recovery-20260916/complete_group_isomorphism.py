"""Specify the Cayley-table decision target and versioned status evidence."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6615'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved deterministic polynomial-time decision on two complete multiplication tables and the existing importance 94.',
 'Defined group axioms, one common multiplication-preserving bijection, explicit bit encoding and total handling of invalid tables.',
 'Corrected the inherited generic source metadata; the FSTTCS 2024 introduction explicitly states the general P-membership question despite the paper’s abelian dynamic focus.',
 'Checked March extension results, August restricted-depth circuit results and the corrected 8 September solvable-A-group statement against the unrestricted target.',
 'Recorded the separate March 2026 general-isomorphism claim without accepting or refuting its unverified proof; marked current resolution status uncertain and kept the card active.',
]
sources=[
 'Read Arvind et al., FSTTCS 2024 Article 4, abstract and §1 pp. 4:1–3. The Parallel Complexity of CGM and Group Isomorphism paragraph on p. 4:2 explicitly states that Group Isomorphism in P is open. The main dynamic results concern abelian groups, not unrestricted static isomorphism.',
 'Read Skresanov, arXiv:2602.15497v2, 8 March 2026, abstract and §1 pp. 1–3: Theorems 1.1–1.2 and Corollaries 1.3–1.4. The bounds are polynomial in n^k for fixed k; the abelian-by-cyclic corollary is a proper subclass. The supplied subgroup/quotient-isomorphism assumptions of Theorem 1.1 are not silently dropped.',
 'Read Grochow–Kardeş–Levet, arXiv:2608.26257v1, 26 August 2026, abstract and §1 pp. 1–3, Theorems A–B. The introduction explicitly says that the new depth bounds do not improve the worst-case serial running time; depth-two lower bounds do not establish a lower bound against all polynomial-time machines.',
 'Read Skresanov, arXiv:2605.26748v2, 8 September 2026, abstract and §1 pp. 1–3, especially Theorem 1.2. The revised title and statement require solvable groups with abelian Sylow subgroups; version 1’s broader title must not be copied as the current theorem.',
 'Read Ruixue Zhao, Preprints.org 202510.0113v4, posted 17 March 2026, abstract and the accessible §6 matrix/Latin-square matching discussion. It explicitly claims polynomial-time group isomorphism as a consequence. Its complete correctness argument and complexity bound were not verified or refuted in this review. The preprint landing page identifies the version as not peer-reviewed. Later specialist papers still present the unrestricted problem as open, so the conflicting claim is retained as unverified status evidence rather than used for archival.',
 f'Bounded later-work search through {DATE} found no independently verified general resolution. Search results about isomorphisms between Cayley graphs concern a different input object and predicate.',
]
status='The FSTTCS 2024 introduction and checked August/September 2026 specialist papers still present general Cayley-table Group Isomorphism in P as open. A separate March 2026 preprint explicitly claims a polynomial-time solution through broader matrix and quasigroup isomorphism algorithms; this review did not verify or refute that proof. The card is therefore active with uncertain resolution status. The special-class algorithms and restricted-depth circuit bounds do not by themselves settle the target.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',status='uncertain',
 formal=r'''Is isomorphism of finite groups given by their complete multiplication tables decidable in deterministic polynomial time?

Precisely, do there exist one uniform deterministic machine \(A\) and integers \(C,c\ge1\) such that, on every binary input of length \(L\), \(A\) halts within \(C(L+1)^c\) steps and outputs YES exactly when the input encodes two finite groups \(G,H\) and there is a bijection \(\varphi:G\to H\) satisfying
\[
\forall x,y\in G,\qquad
\varphi(x\cdot_G y)=\varphi(x)\cdot_H\varphi(y)?
\]
The constants and program are independent of the orders and structure of both groups.''',
 definitions=r'''A table of order \(n\ge1\) is a function \(T:[n]\times[n]\to[n]\), given by listing every one of its \(n^2\) entries. It defines a group precisely when the following three conditions hold:
\[
\begin{aligned}
&\forall x,y,z\in[n],\quad T(T(x,y),z)=T(x,T(y,z));\\
&\exists e\in[n]\ \forall x\in[n],\quad T(e,x)=x=T(x,e);\\
&\forall x\in[n]\ \exists y\in[n],\quad T(x,y)=e=T(y,x).
\end{aligned}
\]
The identity \(e\) in the inverse condition is the same identity supplied by the second condition. All entries already belong to \([n]\), so closure is part of the table definition. Commutativity is not required. A group of order one is allowed; an empty group is not.

The input contains tables \(T_G\) and \(T_H\) of orders \(n\) and \(m\), respectively. If \(n\ne m\), they cannot be isomorphic. When \(n=m\), an isomorphism uses one bijection on elements in all three positions of the multiplication equation. Independent permutations of table rows, columns and entries are not the definition of the predicate. The labels \(1,\ldots,n\) have no mathematical significance, and the identity need not have label one.

Encode a table by \(1^n0\), followed by its \(n^2\) entries in row-major order, each in exactly \(\ell_n=\lceil\log_2(n+1)\rceil\) bits, using ordinary most-significant-bit-first binary. Each entry must be in \(\{1,\ldots,n\}\). Concatenate exactly two such encodings, with no trailing bits. The input bit length is
\[
L=n+m+2+n^2\ell_n+m^2\ell_m.
\]
Malformed encodings, entries outside the indicated range and tables failing any group axiom are NO instances. Group axioms can be checked in polynomial time, so this total-language convention does not add a new algorithmic obstacle to the promised-group version.

The output is only the decision bit. An explicit isomorphism, a canonical table and generators of an automorphism group are not required. There is no restriction to abelian, solvable, nilpotent or prime-power-order groups, and no distinguished subgroups, generators or decompositions are supplied.

The machine is a deterministic multitape Turing machine with a fixed finite program, a fixed finite number of tapes and fixed finite tape alphabets. Its input tape is read-only; work tapes begin blank. Each transition accesses only the cells under the heads and moves each head by at most one cell. Parsing, checking the group axioms, accessing table entries, computing auxiliary data and returning the answer all count. There is no randomness, advice, oracle or free preprocessing.

Polynomial time is measured in the full explicit bit length \(L\). For equal-order groups this is polynomially equivalent to polynomial time in \(n\), since the table already has \(n^2\) entries. It is not polynomial time in \(\log n\), the length needed merely to name the group order. An input consisting only of generators, a presentation, matrices, permutations or oracle access to multiplication would define a different representation model.''',
 answer_criterion=r'''Supply a complete Lean-checked construction of \(A,C,c\), proving exact correctness and the polynomial worst-case bound on all encoded pairs and invalid strings; or supply a complete Lean-checked proof that no such deterministic polynomial-time decider exists. A lower bound for bounded-depth circuits or a restricted algorithmic method is not a lower bound for this entire machine class. An algorithm for only a proper family of groups, an average-case guarantee, a quasipolynomial bound or an unverified claimed general algorithm does not settle the target.''',
 source_formulation=dict(
 text='The FSTTCS 2024 introduction explicitly identifies whether Group Isomorphism belongs to P as an open question in the multiplication-table representation.',
 caption='Paraphrase of §1, Parallel Complexity of CGM and Group Isomorphism, p. 4:2.',
 citation='primary',format='editorial_paraphrase'),
 why='Group isomorphism asks whether two complete finite algebraic structures differ only in their element names. Even with every multiplication available explicitly, a polynomial-time algorithm for arbitrary groups has resisted decades of work. Resolving it would clarify both the complexity of finite algebra and a central algebraic special case of graph isomorphism.',
 references=[
 ref('primary','The Parallel Dynamic Complexity of the Abelian Cayley Group Membership Problem',
  'V. Arvind; Samir Datta; Asif Khan; Shivdutt Sharma; Yadu Vasudev; Shankar Ram Vasudevan',2024,
  'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2024.4',
  'FSTTCS 2024, Article 4, published 5 December 2024; §1, p. 4:2, Parallel Complexity of CGM and Group Isomorphism'),
 ref('extensions','Polynomial-time isomorphism test for k-generated extensions of abelian groups',
  'Saveliy V. Skresanov',2026,'https://arxiv.org/abs/2602.15497v2',
  'Version 2, 8 March 2026; §1, Theorems 1.1–1.2 and Corollaries 1.3–1.4, pp. 1–3'),
 ref('depth',r'Group Isomorphism and the Polylogarithmic-Time Hierarchy: Depth-\(2\frac12\) Circuits and Lower Bounds',
  'Joshua A. Grochow; Gülce Kardeş; Michael Levet',2026,'https://arxiv.org/abs/2608.26257v1',
  'Version 1, 26 August 2026; §1, pp. 1–3, Theorems A–B and explicit distinction from worst-case serial runtime'),
 ref('sylow','Polynomial-time isomorphism test for solvable groups with abelian Sylow subgroups',
  'Saveliy V. Skresanov',2026,'https://arxiv.org/abs/2605.26748v2',
  'Version 2, 8 September 2026; corrected title and main result, §1 Theorem 1.2, p. 2'),
 ref('claim','Polynomial-Time Algorithms for 0-1 Matrix Isomorphism, Graph Isomorphism and Latin Squares',
  'Ruixue Zhao',2026,'https://www.preprints.org/manuscript/202510.0113/v4',
  'Version 4, posted 17 March 2026; abstract and §6; unverified general-solution claim, not accepted resolution evidence'),
 ],
 context_blocks=[
 block('The inherited source studies dynamic membership and isomorphism for abelian groups, but its introduction separately states the unrestricted static P-membership question. The card keeps that general question.'),
 block(r'The standard general upper bound is \(n^{O(\log n)}\) for groups of order \(n\). The August 2026 paper explicitly distinguishes improvements in circuit depth from an improvement to polynomial sequential time. Its lower bound also concerns a restricted circuit depth.','depth'),
 block('The March 2026 preprint gives polynomial-time tests for several families of extensions of abelian groups, including abelian-by-cyclic groups. An abelian-by-cyclic group has an abelian normal subgroup whose quotient group is cyclic. This is a proper structural promise, absent from the target.','extensions'),
 block('The corrected September 2026 result requires solvable groups with abelian Sylow subgroups. The solvability restriction is explicit in version 2; the broader wording of the first version is not the current theorem. The restricted family does not contain all finite groups.','sylow'),
 block('A separate March 2026 preprint claims polynomial-time algorithms for broader isomorphism problems and explicitly draws a polynomial-time group-isomorphism consequence. Its proof was not verified or refuted in this review. This unresolved claim is the reason for uncertain status, while the checked later specialist literature continues to state the general problem as open.','claim'),
 ],
 progress=[
 progress('2024-12-05','The source explicitly states the unrestricted multiplication-table question while developing abelian dynamic algorithms.'),
 progress('2026-03-08','The versioned extension result handles proper structural families.','extensions'),
 progress('2026-03-17','A separate preprint claims a general polynomial-time consequence; this review does not certify its proof.','claim'),
 progress('2026-08-26','New upper and lower bounds concern circuit depth, without a polynomial sequential algorithm.','depth'),
 progress('2026-09-08','The revised Sylow-subgroup result explicitly includes solvability in its assumptions.','sylow'),
 progress(DATE,'The review fixes the complete-table bit model and retains active uncertain status because the general-solution claim is unverified.'),
 ],
),notes,sources,status,summary=[
 'Two finite groups are isomorphic when one bijection of their elements preserves every product.',
 'The input supplies both complete multiplication tables, and the target is deterministic polynomial-time decision in their explicit bit length.',
 'The algorithm must cover all finite groups without additional structural information.',
 'Recent algorithms for restricted families and lower bounds for shallow circuits do not settle this general target.',
 'A separate claimed general solution remains unverified in this review, so the card stays active with uncertain resolution status.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
