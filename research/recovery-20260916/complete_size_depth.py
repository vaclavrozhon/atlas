"""Complete and archive the existence question answered by STOC 2025."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5275'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']+[
 ref('stoc2025','Truly Supercritical Trade-Offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler–Leman',
     'Susanna F. de Rezende; Noah Fleming; Duri Andrea Janett; Jakob Nordström; Shuo Pang',2025,
     'https://jakobnordstrom.se/docs/publications/TrulySupercriticalTrade-offs_STOC.pdf',
     'STOC 2025, pp. 1371–1382, DOI 10.1145/3717823.3718271; §2.3 definitions, Theorems 2.5, 2.8 and 2.10, Lemma 2.9'),
 ref('full2024','Truly Supercritical Trade-offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler–Leman',
     'Susanna F. de Rezende; Noah Fleming; Duri Andrea Janett; Jakob Nordström; Shuo Pang',2024,
     'https://arxiv.org/abs/2411.14267v1',
     'Full preprint v1, 21 November 2024; §2.5 Theorem 2.8 (renumbered 2.10 in proceedings), §6 proof of resolution lifting'),
]
notes=[
 'Recovered the source existence question for resolution, distinct from the stronger question about all quasipolynomial-size Cutting Planes proofs of particular formulas.',
 'Specified proof line count, dependency depth, unrestricted reusable clauses, and superlinear depth under a nonvacuous polynomial size budget.',
 'Checked that the published STOC 2025 resolution theorem supplies a stronger witness, including a polynomial interval of size budgets; no width or tree-like restriction is imposed.',
 'Audited the parameter substitution and lifting argument, while explicitly recording reliance on the published compressed-game width–depth theorem.',
 'Completed the historical formulation and archived it as resolved rather than retaining an answered existence question in the active benchmark.',
]
sources=[
 'Read CCC 2021 §§1.1, 1.2 and 6, especially printed 6:26; the resolution existence question is distinct from Conjecture 6 for Cutting Planes.',
 'Read STOC 2025 §§2.3–2.5, Theorems 2.5, 2.8, 2.10 and Lemma 2.9, comparing the version numbering with the full November 2024 preprint.',
 'Read full preprint §6, including the independent-block restriction, surviving-width tail and union bound, and the line-by-line simulation in §2.5.',
 'Checked k=40, c=20, m=t^3 in published Theorem 2.10: formula size O(t^33), variable count O(t^24), short size O(t^172), size threshold at least 2^-60 t^180 and depth Omega(t^40). These give a polynomial-size supercritical witness.',
 'This is a theorem-scope and implication audit of a published result. The underlying compressed cop-robber lower bound and every upstream proof were not independently reconstructed; no Lean formalization was performed.',
]
status=('Resolved: the published STOC 2025 result gives supercritical size–depth tradeoffs for general resolution, stronger than the existence question extracted from CCC 2021. '
        'The 16 September 2026 review checked the proof model, the direct resolution theorem, its lifting proof and a concrete parameter substitution. '
        'The resolution witness has polynomial formula/proof size and superlinear depth even after a polynomial increase in the allowed proof size. '
        'This disposition relies on the published underlying width–depth theorem; it is not a claim that all source proofs or a Lean theorem were independently verified.')
complete(identifier,dict(
 title='Supercritical resolution size–depth tradeoffs',
 status='resolved',
 question_type='yes_no',
 formal=r'''Does there exist a family of unsatisfiable CNF formulas \((F_i)_{i\ge1}\), with numbers of occurring variables \(n_i\to\infty\), polynomially bounded formula sizes and positive integer proof-size budgets \(s_i\), such that
\[
\min_{\pi:F_i\vdash\bot}|\pi|\le s_i
\quad\text{and}\quad
\frac{\min\{D(\pi):\pi:F_i\vdash\bot,\ |\pi|\le s_i\}}{n_i}
\longrightarrow\infty?
\]
Polynomially bounded means that there are common constants \(C,a>0\) with \(s_i\le Cn_i^a\) and \(\operatorname{size}(F_i)\le Cn_i^a\) for all \(i\). The refutations are unrestricted general resolution proofs as defined below. This is a precise polynomial-size witness to the source's existence question about a supercritical size–depth tradeoff; a published stronger witness answers it affirmatively.''',
 definitions=r'''A Boolean literal is a variable or its negation. A clause is a finite disjunction of literals on distinct variables and is identified with their set. The empty clause \(\bot\) is false. A CNF formula is a finite set of clauses interpreted conjunctively; it is unsatisfiable when no Boolean assignment satisfies all its clauses. Only variables actually occurring in the formula are counted. Its formula size is the total number of literal occurrences, \(\operatorname{size}(F)=\sum_{C\in F}|C|\). No succinct encoding of the input formula is used.

A resolution refutation is an ordered finite sequence of clause lines. A line is either an input clause or is derived from two earlier lines \(C\vee x\) and \(D\vee\neg x\) by the rule deriving \(C\vee D\), with neither \(C\) nor \(D\) containing the pivot variable. The final line is empty. Earlier lines may be reused any number of times. There are no new extension variables, extra axioms, semantic inferences, or separate weakening rule during the proof.

The dependency graph has one vertex for each line and edges from each cited premise to the derived line. The proof size \(|\pi|\) is the number of lines, including input-clause occurrences. The depth \(D(\pi)\) is the maximum number of edges on a directed path in this graph; an input line has depth zero. This is neither clause width nor the number of lines held in memory. There is no width, regularity, tree structure, or space restriction.

The size-budget condition is nonvacuous: at least one refutation lies within each budget. The displayed minimum therefore exists. The limit means that for every real \(R>0\) there is an \(i_0\) such that, for every \(i\ge i_0\), every refutation of \(F_i\) using at most \(s_i\) lines has depth exceeding \(Rn_i\).

Without a size bound, every unsatisfiable formula on \(n_i\) variables has a resolution refutation of depth at most \(n_i\), obtained from the exhaustive Boolean decision tree with suitable input-clause leaves. Such a proof can have exponential size. Thus depth growing faster than \(n_i\) under a short-proof budget exceeds the unrestricted worst-case depth bound: this is the meaning of supercritical here.

The source did not demand this particular polynomial witness or a numerical tradeoff curve; it asked whether the phenomenon exists even for resolution. The more quantitative statement above records an affirmative witness to that question. The published theorem also permits a polynomial increase in the size budget while retaining superlinear depth, and is stronger still when depth is compared with formula size. Those stronger guarantees are known results, not new open targets.''',
 answer_criterion=r'''The historical target is a complete Lean-checked proof or refutation of the displayed existence statement, with nonempty sets of size-bounded refutations and depth measured in the unrestricted resolution dependency graph. An affirmative result must show the depth-to-variable-count ratio tends to infinity under a polynomial budget. A width restriction, tree-like restriction, or an empty size-bounded proof class does not establish this statement. The mathematical existence question is now answered by the cited published theorem and this card is archived; the record does not assert that a Lean proof has already been supplied.''',
 references=refs,
 source_formulation=dict(text='The source asks whether one can establish a supercritical size–depth tradeoff for resolution. This is posed as a first step toward related questions about Cutting Planes and monotone circuits.',
     caption='Editorial paraphrase of the source existence question',citation='primary',format='editorial_paraphrase'),
 context_blocks=[
     block('Proof size measures how much derivation is written down, while depth measures how many successive dependencies are necessary. Separate efficient proofs for the two resources need not be efficient for both at once. The source asks whether keeping the proof short can force depth beyond the linear bound available when size is unrestricted.'),
     block('The later published result answers this question for general resolution. It provides formulas with polynomial-size refutations for which every refutation within a larger polynomial budget has superlinear depth. Its theorem addresses reusable proof lines directly and does not rely on restricting the proof to a tree.','stoc2025'),
     block('This resolves the general existence question. It does not settle every stronger statement about particular Tseitin families, all quasipolynomial-size proofs, or the full quantitative tradeoff curve. Those are distinct claims and are not silently substituted for the original card.','primary'),
 ],
 why='The result demonstrates that short refutations may inherently require long sequential chains, even when shallow refutations exist with unrestricted size. It identifies a limitation of parallelizing compact logical reasoning and answers the specific existence question motivating the original candidate.',
 importance=dict(score=79,method='editorial',reason='A fundamental interaction between the size and parallel depth of propositional proofs, motivated by the limitations of branch-and-cut reasoning; retained as a historical assessment after resolution.'),
 progress=[
     progress('2021','The source explicitly asks for a supercritical size–depth tradeoff in resolution.'),
     progress('2024-11-21','The full preprint gives a stronger general-resolution size–depth theorem.','full2024'),
     progress('2025','The result appears at STOC, with the direct resolution tradeoff as Theorem 2.10.','stoc2025'),
     progress('2026-09-16','The review checked the model and a polynomial-size parameter witness, and archived the answered existence question.','stoc2025'),
 ],
),notes,sources,status,summary=[
 'Resolution proof size counts clause lines, while depth counts the longest chain of premise dependencies.',
 'The historical question asks whether polynomial-size refutations can necessarily have depth growing faster than the number of variables.',
 'This is supercritical because unrestricted-size resolution refutations always have a linear depth upper bound.',
 'A published STOC 2025 theorem provides a stronger witness for general resolution and answers the existence question.',
 'The completed card is therefore archived as resolved, with the scope of the source verification recorded.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],
archive_reason='Resolved by de Rezende et al., STOC 2025, Theorem 2.10: general resolution has polynomial-size refutations with superlinear depth forced under a larger polynomial size budget. The source question asks for existence, not a particular remaining tradeoff curve.')
