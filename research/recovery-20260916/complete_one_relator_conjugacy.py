"""Complete the approved uniform one-relator conjugacy decision problem."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6642'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the previously selected uniform presentation-input decision target with no running-time bound.',
 'Defined the explicit word alphabet, inverse, free reduction, normal closure and quotient equality, including empty words and a trivial relator.',
 'Specified a total deterministic machine, both positive and negative termination, and the unrestricted finite conjugator.',
 'Distinguished a uniform undecidability proof from a fixed-group counterexample, which is sufficient but not necessary.',
 'Checked the August 2026 Diophantine theorem’s explicit nonconsequence for conjugacy and distinguished inverse monoids and prefix membership.',
 'Added complete Lean-checked acceptance and removed speculative solution routes; retained the assessed importance 95.',
]
sources=[
 'Read Linton–Nyberg-Brodda, arXiv:2501.18306v1 (30 January 2025), §1.8 opening and §1.8.1 printed pp. 67–69, Theorems 1.8.1 and 1.8.3, and §1.6.1 Theorem 1.6.3 recalling Newman’s 1968 torsion result. The survey distinguishes the known word algorithm and the open general conjugacy problem; its subgroup question is not substituted for the card. Checked that arXiv still lists v1.',
 'Read Nyberg-Brodda, arXiv:2608.01983v1 (3 August 2026), introduction pp. 1–2, Theorems A–B and the explicit paragraph stating that these results say nothing about undecidability of conjugacy. It notes that the conjugacy problem in the Baumslag–Gersten example B2 is already decidable. The new Diophantine proof was not independently certified.',
 'Read the primary abstract and submission history of Gray–Reilly, arXiv:2608.04650v1 (5 August 2026): inverse-monoid word-problem and group prefix-membership undecidability are distinct tasks. Also checked Gray–Levine, arXiv:2605.30535v1 (28 May 2026), abstract: nearby classes and subgroup-constrained equations. No claim about their full proofs is made.',
 f'Bounded primary-source searches through {DATE} found restricted structural results and related equation undecidability, but no resolution of the full uniform conjugacy target. The September 2026 journal issue for Gardam–Kielak–Logan concerns hyperbolic two-generator groups under additional assumptions, not all one-relator presentations.',
]
status='The checked 2025 survey and August 2026 primary paper retain general one-relator conjugacy as open. The latter explicitly states that its Diophantine undecidability results do not imply conjugacy undecidability. The card keeps the uniform presentation-input question; no solution of that target was found in the bounded later-work check.'
complete(identifier,dict(
 criterion='decision',question_type='yes_no',year=2026,
 formal=r'''Does there exist a single total deterministic Turing algorithm which, given any finite presentation with one relator
\[
G=\langle x_1,\ldots,x_k\mid r=1\rangle
\]
and two finite words \(u,v\) in those generators and their inverses, decides whether
\[
\exists w\in\{x_1,x_1^{-1},\ldots,x_k,x_k^{-1}\}^*,
\qquad w^{-1}uw=_Gv?
\]
The presentation is part of the input. There is no prescribed time or space bound, but the algorithm must halt correctly on both conjugate and nonconjugate pairs for every such presentation.''',
 definitions=r'''An input consists of an integer \(k\ge1\) and three explicitly written finite words \(r,u,v\) over the alphabet
\[
\Sigma_k=\{x_i,x_i^{-1}:1\le i\le k\}.
\]
Encode \(k\), word lengths and generator indices in binary with unambiguous boundaries, and encode the sign of each letter by one bit. Every letter occurrence is listed; exponents, circuits or other descriptions do not stand for omitted repetitions. Empty words and words with adjacent inverse pairs are allowed. An invalid encoding or an index outside \(\{1,\ldots,k\}\) is rejected. The requirement of totality also covers these invalid strings.

The free group \(F_k\) consists of reduced words, with adjacent pairs \(x_ix_i^{-1}\) and \(x_i^{-1}x_i\) cancelled. Its multiplication is concatenation followed by reduction; its identity is the empty word. The inverse of a word reverses its letters and changes each letter to its formal inverse.

Let \(N_r\) be the normal closure of \(r\) in \(F_k\). Explicitly, it consists of products
\[
\prod_{j=1}^{m} a_j r^{\varepsilon_j}a_j^{-1},
\qquad m\ge0,\quad a_j\in F_k,\quad\varepsilon_j\in\{-1,1\},
\]
interpreted as free-group elements; the empty product is included. The presented group is the quotient \(G=F_k/N_r\). Two words \(s,t\) satisfy \(s=_Gt\) exactly when \(st^{-1}\in N_r\). Thus the equation in the target is equality in this quotient, rather than literal string equality or equality only after free reduction. The one relator may reduce to the empty word, in which case the quotient is the free group.

The elements represented by \(u,v\) are conjugate if some finite word \(w\) satisfies the displayed equation. There is no bound on its length, no restriction to a subgroup and no requirement to output it. Every finite one-relator presentation is included: the number of generators and all three word lengths are unbounded, the relator may be a proper power, and no torsion, geometric or residual-finiteness promise is imposed.

Uniform means that the same finite machine receives all these inputs and outputs a bit, with one meaning conjugate and zero meaning nonconjugate. Its code and termination guarantee cannot depend on a separately fixed group. There is no oracle, advice or randomization. Separate decision procedures for each fixed presentation do not suffice unless there is an effective way to obtain and run them from the input presentation. No efficiency requirement is imposed beyond termination.

This is an exact algorithm-existence proposition. A routine that halts only on positive instances is a semidecision procedure, not the requested decision algorithm.''',
 answer_criterion=r'''Supply a total uniform algorithm and a complete Lean-checked proof of its correctness and termination on every encoded input, with the group equation interpreted exactly as above. Alternatively, supply a complete Lean-checked proof that the language of valid conjugate tuples \((k,r,u,v)\) is undecidable.

A fixed one-relator group with a proved undecidable conjugacy problem would suffice for a negative answer, but the uniform language could also be shown undecidable without such a fixed-group example. A result for a restricted family, a solution only of word equality, or undecidability of arbitrary systems of equations, subgroup membership or inverse-monoid problems does not settle this target.''',
 source_formulation=dict(text='The survey states that the conjugacy problem remains open for one-relator groups, despite the established word algorithm and positive conjugacy results for important subclasses. This card retains its previously selected uniform version, in which the finite presentation and the two words are all inputs to one machine.',caption='Paraphrase of Linton–Nyberg-Brodda, §1.8 and §1.8.1, printed pp. 66–69.',citation='primary',format='editorial_paraphrase'),
 why='One defining relation permits complicated infinite groups while still allowing ordinary word equality to be decided. Conjugacy adds an unrestricted search for a change of representative. Resolving its uniform decidability would locate a basic boundary between effective equality and effective existential questions in finitely presented algebra.',
 references=[
 ref('primary','The theory of one-relator groups: history and recent progress','Marco Linton; Carl-Fredrik Nyberg-Brodda',2025,'https://arxiv.org/abs/2501.18306v1','Version 1, 30 January 2025; §1.8 opening and §1.8.1, printed pp. 66–69; §1.6.1 Theorem 1.6.3 recalls the torsion conjugacy theorem'),
 ref('equations','Undecidability of the Diophantine problem for one-relator groups and one-relation monoids','Carl-Fredrik Nyberg-Brodda',2026,'https://arxiv.org/abs/2608.01983v1','Version 1, 3 August 2026; introduction pp. 1–2, Theorems A–B and the explicit nonconsequence for conjugacy following Theorem B'),
 ref('inverse','The word problem for two-generator one-relator inverse monoids','Robert D. Gray; Catherine Reilly',2026,'https://arxiv.org/abs/2608.04650v1','Version 1, 5 August 2026; primary abstract, distinguishing inverse-monoid word problems and group prefix membership'),
 ],
 context_blocks=[
 block('A presentation gives generators and equations that may be reused in arbitrarily long products. A single defining equation does not force the resulting group to be finite or simple. The card includes all finite strings describing that equation.'),
 block(r'Conjugacy is different from equality even in a free group: \(ab\) and \(ba\) are conjugate because \(a^{-1}(ab)a=ba\). The identity is conjugate only to itself, so conjugacy includes deciding whether a word represents the identity.'),
 block('Magnus’s word algorithm handles every one-relator group. The survey explains that the structural operations used for word equality do not automatically preserve decidability of conjugacy. Its harder examples in larger presentation classes do not give a one-relator counterexample.'),
 block('Newman’s classical theorem settles conjugacy for one-relator groups with torsion, and further special classes are also known. Here torsion means that some nonidentity element has finite order. The full target includes groups without that property.'),
 block('The August 2026 Diophantine theorem proves undecidability of arbitrary systems of equations in certain one-relator groups. It explicitly states that this does not prove conjugacy undecidable, and even notes a studied example whose conjugacy problem is decidable.','equations'),
 block('The separate August inverse-monoid result changes either the algebraic structure or the decision task. Its group prefix-membership example asks for membership in a specified submonoid, rather than existence of an unrestricted conjugator.','inverse'),
 ],
 progress=[
 progress('1932','Magnus’s word-equality algorithm supplies a positive result for a simpler decision problem, as recalled in the survey.'),
 progress('1968','Newman establishes conjugacy decidability in one-relator groups with torsion, as recorded in Theorem 1.6.3 of the survey.'),
 progress('2025-01-30','The comprehensive survey retains the general conjugacy question and describes positive subclasses and structural obstacles.'),
 progress('2026-08-03','Diophantine undecidability is proved for one-relator examples, with an explicit statement that conjugacy remains unaffected.','equations'),
 progress('2026-08-05','Two-generator inverse-monoid word and group prefix-membership undecidability provide related results for different targets.','inverse'),
 ],
),notes,sources,status,summary=[
 'A one-relator group is specified by finitely many generators and a single word required to equal the identity.',
 'Two input words are conjugate when an unrestricted finite word transforms one into the other by conjugation inside that group.',
 'The question asks for one always-terminating algorithm receiving both the presentation and the two words, with no efficiency bound.',
 'Known word algorithms and recent undecidability of more general equation systems do not decide this particular task.',
 'A complete Lean-checked solution must verify a uniform decision algorithm or prove that the full input language is undecidable.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
