"""Individual review of the user-selected sharp fixed-width length target."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6767'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[0]['locator']='§7, Open Problem 15, printed pages 51–52; Open Problem 14 is a separate question'
refs += [
 ref('narrow2016','Narrow Proofs May Be Maximally Long','Albert Atserias; Massimo Lauria; Jakob Nordström',2016,
     'https://jakobnordstrom.se/docs/publications/LargeNarrowProofs_ToCL.pdf',
     'ACM Transactions on Computational Logic 17(3), article 19; Theorem 1.1 and concluding discussion of constants; also arXiv:1409.2731'),
 ref('tradeoff2016','A Tradeoff Between Length and Width in Resolution','Neil Thapen',2016,
     'https://www.theoryofcomputing.org/articles/v012a005/',
     'Theory of Computing 12(5), 1–14, abstract and main length–width tradeoff; resolves the separate survey Problem 14 direction'),
 ref('tree2025','Supercritical Size-Width Tree-Like Resolution Trade-Offs for Graph Isomorphism',
     'Christoph Berkholz; Moritz Lichter; Harry Vinall-Smeeth',2025,
     'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.18',
     'MFCS 2025, article 18; abstract and Definition 3 distinguish tree-like size and narrow width from general resolution'),
 ref('supercritical2025','Truly Supercritical Trade-Offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler–Leman',
     'Susanna F. de Rezende; Noah Fleming; Duri Andrea Janett; Jakob Nordström; Shuo Pang',2025,
     'https://jakobnordstrom.se/docs/publications/TrulySupercriticalTrade-offs_STOC.pdf',
     'STOC 2025, Theorems 1.2–1.4: depth restrictions and tree-like width–size tradeoffs'),
]
notes=[
 'Applied the explicit user selection: all sufficiently large fixed widths, linear-size 3-CNF families, width at most w, and unrestricted length Omega(n^(w-c)) with one absolute c.',
 'Separated survey Problems 14 and 15; the selected assertion is the sharp exponent question, not the already established existence of length–width tradeoffs.',
 'Specified formula size, syntactic resolution, unrestricted reuse, line counting, all width/size/family quantifiers, and Lean acceptance.',
 'Distinguished n^Omega(w) from n^(w-O(1)), and tree-like or depth-restricted lower bounds from an unrestricted length lower bound.',
]
sources=[
 'Read Nordström 2013 §7 Open Problems 14–15 and the motivation on printed pages 51–52.',
 'Read the saved Atserias–Lauria–Nordström full text Theorem 1.1, §1.2 and concluding constants discussion; checked the author journal PDF metadata and arXiv record.',
 'Read Thapen 2016 main result and publisher abstract; this answers the separate short-to-narrow conversion question.',
 'Checked MFCS 2025 graph-isomorphism paper abstract and proof-system definitions, and STOC 2025 supercritical paper Theorems 1.2–1.4 for absent restrictions.',
 'Bounded web search on 16 September 2026 found no proof or refutation of the stronger selected exponent-one assertion; source proof details were not independently reconstructed.',
]
status=('The survey posed this sharp fixed-width direction as Open Problem 15. Later work proves n^Omega(w) lower bounds, '
        'which do not establish the selected exponent w-c with one absolute c. The original grouped Problem 14 has a known tradeoff answer and is no longer part of the target. '
        'A bounded review on 16 September 2026, including 2025 tree-like and depth-restricted tradeoffs, found no resolution of this exact user-selected assertion. '
        'The check compares theorem statements and parameters; it is not an exhaustive literature certificate or a Lean verification.')
complete(identifier,dict(
 title='Sharp resolution length bounds at fixed width',
 question_type='yes_no',
 formal=r'''Do there exist integers \(c\ge1\) and \(w_0\ge\max\{3,c+1\}\) such that, for every integer \(w\ge w_0\), there are constants \(a_w,b_w,d_w>0\), an integer \(n_w\ge1\), and a family of unsatisfiable 3-CNF formulas \((F_{n,w})_{n\ge n_w}\) satisfying, for every integer \(n\ge n_w\),
\[
a_wn\le s(F_{n,w})\le b_wn,\qquad
W(F_{n,w})\le w,\qquad
L(F_{n,w})\ge d_wn^{\,w-c}?
\]
Here \(W\) is minimum refutation width and \(L\) is minimum refutation length without a width restriction. The absolute constant \(c\) is common to every width. The family and the other constants may depend on \(w\), which is fixed before \(n\) tends to infinity.''',
 definitions=r'''A Boolean variable takes a value in \(\{0,1\}\); a literal is a variable or its negation. A clause is a finite set of literals interpreted as their disjunction. Its width is its cardinality; the empty clause is false. A CNF formula is a finite set of clauses interpreted as their conjunction. A 3-CNF has clauses of width at most three, not necessarily exactly three. Tautological clauses, containing both signs of one variable, may be omitted. The formula is unsatisfiable if no assignment to its occurring variables makes every clause true.

Write \(v(F)\) for the number of distinct occurring variables and use the combinatorial formula size
\[
s(F)=v(F)+|F|+\sum_{C\in F}|C|.
\]
Variable names have no semantic significance. This is the customary variable/clause/occurrence size, rather than the bit length of a variable-index encoding or the size of a succinct description. For 3-CNF formulas the three displayed counts are bounded by constant multiples of the number of clauses. The parameter \(n\) indexes a family of linear combinatorial size; it is not an extra width or a proof-length parameter.

A resolution refutation is a finite sequence of clauses ending with the empty clause. Each line is an input clause of \(F\) or follows from two earlier clauses \(C\cup\{x\}\) and \(D\cup\{\neg x\}\) by deriving \(C\cup D\), where \(C,D\) contain neither sign of the pivot \(x\). No extension variables, semantic inference, or additional axioms are allowed. Duplicate literals in a resolvent are merged. Reusing any earlier line arbitrarily often is allowed, so the underlying proof is a directed acyclic graph and need not be a tree. Weakening is not an additional rule in this convention.

The length \(L(\pi)\) is the number of clause lines, including input-clause occurrences. The width \(W(\pi)\) is the maximum width of any line, including input lines. Define \(L(F)\) as the minimum length of any resolution refutation of \(F\), and \(W(F)\) as the minimum width. For unsatisfiable formulas these minima exist by completeness of resolution. The two minima need not be attained by the same proof. There is no bound on space, depth, or regularity.

In particular, the lower bound in the target ranges over all refutations, including those much wider than \(w\). Merely showing that every width-\(w\) refutation is long is insufficient. The family is not required to have a uniformly efficient construction. Requiring \(c\) to be a positive integer loses no positive-real-constant version, since it can be increased to its ceiling. The threshold \(w_0\) excludes widths with a vacuous nonpositive exponent.

This is the user's selected precise form of the survey's sharp fixed-width question. The original imported card also mentioned the separate short-proof-to-narrow-proof tradeoff question; that second direction is now background. No assertion that the present statement is equivalent to every phrasing in that broader source entry is made.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of the displayed quantified existence assertion, using the formula size and resolution rules above. An affirmative answer must establish one absolute \(c\) and all sufficiently large fixed widths, with a lower bound on unrestricted minimum length. A lower bound \(n^{\alpha w}\) for a fixed \(\alpha<1\), a tree-like lower bound, a restriction on proof depth, or a result for a single width does not suffice. A negative answer is the full logical negation of the assertion, not merely failure of a proposed construction. This is an asymptotic proposition, so the numerical-value tolerance does not replace its exponent requirement.''',
 references=refs,
 target_revision=dict(date='2026-09-16',previous_formal=old['formal'],
     authorization='User explicitly selected linear-size 3-CNFs and unrestricted Omega(n^(w-c)) length for all sufficiently large fixed w, with absolute c.',
     scope='Only the sharp fixed-width direction of Open Problem 15; no separate conversion tradeoff or uniform construction requirement.'),
 source_formulation=dict(text='The survey asks how close a fixed-width refutation can come to requiring length with exponent equal to that width. The selected version seeks linear-size 3-CNFs admitting width at most w but requiring unrestricted length at least a constant times n to the power w-c, for a common absolute c.',
     caption='Editorial paraphrase with the user-selected quantifiers',citation='primary',format='editorial_paraphrase'),
 context_blocks=[
     block(r'Width limits how many literals a proof line can mention together. For fixed \(w\), counting the possible clauses gives an \(n^{O(w)}\) length upper bound whenever a narrow refutation exists. The selected question asks whether nearly the whole width can be forced into the exponent, even when the shortest proof may use unrestricted width.'),
     block(r'Atserias, Lauria and Nordström established \(n^{\Omega(w)}\) hardness for narrow 3-CNF refutations. This makes the exponential dependence on width unavoidable. The coefficient hidden in that exponent is significant here: the selected target asks for \(w-c\), not an unspecified positive fraction of \(w\).','narrow2016'),
     block('Thapen established that forcing an already short proof to become narrow can require an exponential increase in length. That settles the different conversion direction grouped in the old draft. It does not supply the present fixed-width, nearly full-exponent lower bound.','tradeoff2016'),
     block('Recent supercritical tradeoffs impose tree structure or a depth restriction on proofs. Those are substantial results about other combinations of resources. The present lower bound must survive unrestricted reuse, width and depth in the proof whose length is being minimized.','supercritical2025'),
 ],
 why='A sharp answer would quantify the inherent exponent cost of narrow resolution, a foundational resource in SAT proof complexity. It would distinguish the optimal dependence on width from the already known qualitative exponential dependence, and sharpen what resolution-based proof search can achieve even when it is free to use wider clauses.',
 importance=dict(score=77,method='editorial',reason='A precise quantitative refinement of a central width-versus-length phenomenon in propositional proof complexity, with direct relevance to the limits of resolution-based search; narrower than the already settled qualitative tradeoff.'),
 progress=[
     progress('2013','The survey records the sharp fixed-width question as Open Problem 15.'),
     progress('2016',r'The narrow-proof lower bounds establish \(n^{\Omega(w)}\) dependence, leaving a distinction from the selected exponent \(w-c\).','narrow2016'),
     progress('2016','A length blow-up under width reduction was proved for the separate conversion question.','tradeoff2016'),
     progress('2025','New tree-like and depth-constrained tradeoffs address other proof-resource combinations.','tree2025'),
     progress('2026-09-16','The review separated these results from the exact user-selected assertion and retained source-open status with bounded verification.'),
 ],
),notes,sources,status,summary=[
 'Resolution width is the largest clause used in a refutation, and length counts its clause lines.',
 'The question asks for linear-size 3-CNF families whose narrow refutations coexist with an almost full-width exponent lower bound on every refutation length.',
 'One absolute exponent loss must work for all sufficiently large fixed widths, while family constants may depend on width.',
 'Known exponential dependence on width and newer restricted-proof tradeoffs do not by themselves give this sharper unrestricted lower bound.',
 'A resolution would sharpen the fundamental cost of narrow reasoning in propositional proof search.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
