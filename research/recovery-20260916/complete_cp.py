"""Individually reviewed, user-selected coefficient simulation target."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/card-completion-20260913'))
from complete_review import complete, ref, block, progress
from review_queue import read_claims

identifier = 'TCS-6770'
old = json.loads((ROOT / 'data/cards' / f'{identifier}.json').read_text())
claim = read_claims(ROOT)[identifier]
references = old['references'] + [
    ref('handbook2021', 'Proof Complexity and SAT Solving', 'Sam Buss; Jakob Nordström', 2021,
        'https://doi.org/10.3233/FAIA200990',
        'Handbook of Satisfiability, second edition, Chapter 7; author chapter preprint §§7.6.1, 7.7.3, Open Problem 7.14 and equation (7.64)'),
    ref('bussclote1996', 'Cutting planes, connectivity, and threshold logic', 'Samuel R. Buss; Peter Clote', 1996,
        'https://mathweb.ucsd.edu/~sbuss/ResearchWeb/cuttingplanes/paper.pdf',
        'Annals of Pure and Applied Logic 83, 205–228; inspected author PDF dated 6 March 2002, §§2, 7–8'),
    ref('lifting2020', 'Lifting with Simple Gadgets and Applications to Circuit and Proof Complexity',
        'Susanna F. de Rezende; Or Meir; Jakob Nordström; Toniann Pitassi; Robert Robere; Marc Vinyals', 2020,
        'https://eccc.weizmann.ac.il/report/2019/186/',
        'ECCC TR19-186, February 2020 revision; coefficient separation with simultaneous line-space restrictions'),
    ref('tree2026', 'Superpolynomial Length Lower Bounds for Tree-Like Semantic Proof Systems with Bounded Line Size',
        'Susanna F. de Rezende; David Engström; Yassine Ghannane; Kilian Risse', 2026,
        'https://eccc.weizmann.ac.il/report/2026/078/',
        'May 2026 preprint; abstract and stated tree-like, bounded-line-size scope'),
]

definitions = "A CNF formula \\(F\\) is a finite list of clauses over Boolean variables \\(x_1,\\ldots,x_n\\), each taking values in \\(\\{0,1\\}\\). Each clause is a finite set of positive or negative literals. Duplicate literal occurrences are removed; tautological clauses and the empty clause are allowed. Variables are consecutively relabeled, and only variables occurring in the formula are counted. The empty conjunction is true and the empty clause is false. Fix the combinatorial input size\n\\[\nN(F)=1+n+|F|+\\sum_{C\\in F}|C|.\n\\]\nThis measure is polynomially equivalent to the bit length of an explicit clause-list encoding with binary variable indices. The choice fixes the size parameter, rather than granting a succinct circuit encoding of the input.\n\nA Cutting Planes line is a normalized integer inequality \\(\\sum_{i=1}^{n}a_i x_i\\ge b\\), with every \\(a_i,b\\in\\mathbb Z\\). Zero coefficients may be omitted in writing, but the coefficient vector is defined on all \\(n\\) variables. A clause with positive-variable set \\(P\\) and negative-variable set \\(M\\) contributes the input inequality \\(\\sum_{i\\in P}x_i-\\sum_{i\\in M}x_i\\ge1-|M|\\). If both signs occur, their coefficients cancel. Boolean axioms are \\(x_i\\ge0\\) and \\(-x_i\\ge-1\\); the harmless constant axiom \\(0\\ge0\\) is also permitted. No extension variables, semantic inference rules, or extra assumptions are allowed.\n\nA proof is a finite sequence of lines. Each line is an input inequality, a Boolean or constant axiom, or follows from earlier lines by one of these rules: addition of two inequalities; multiplication of one inequality by a positive integer; or division by a positive integer \\(d\\) that divides every coefficient on its left side, replacing \\(\\sum_i a_i x_i\\ge b\\) by \\(\\sum_i(a_i/d)x_i\\ge\\lceil b/d\\rceil\\). All sums are put in normalized form by collecting coefficients. Earlier lines may be reused arbitrarily many times, so these are general directed-acyclic proofs, not tree-like proofs. A refutation ends with \\(0\\ge1\\). Its length \\(L(\\pi)\\) is its number of lines, including input and axiom occurrences. No bound is placed on the number of lines simultaneously retained. In particular, proof length is not algorithmic runtime, total coefficient bit length, or a memory measure.\n\nDefine the magnitude of a proof by\n\\[\nM(\\pi)=\\max\\bigl(\\{1\\}\\cup\\{|a_i|,|b|:\\text{a line }\\sum_i a_i x_i\\ge b\\text{ occurs in }\\pi\\}\\bigr).\n\\]\nThe original proof may have arbitrarily large integer coefficients, written in binary. The replacement proof must bound the numerical magnitudes of all line coefficients and right-hand sides, not merely their bit lengths. Multiplication and division annotations are required to make the displayed inferences valid; the magnitude measure concerns the inequalities themselves. Every inference, including intermediate multiplication lines, counts toward length and is subject to the replacement bound.\n\nThe common polynomial bound in this card can equivalently be written \\(C(N+L)^k\\), for positive integers \\(C,k\\) independent of the formula and original proof. The same \\(C,k\\) bound both replacement length and coefficient magnitude. This is an existential comparison of proofs: it does not additionally require a polynomial-time algorithm that constructs the replacement proof from the original one. The parameter \\(N+L\\), one common polynomial, and the absence of a space bound are the user's explicit specification of the source question. Literature also discusses bounds polynomial only in input size and polynomial-time proof transformations; those additional requirements are not silently imposed here."

formal = "Do there exist positive integers \\(C,k\\) such that, for every CNF formula \\(F\\) and every Cutting Planes refutation \\(\\pi\\) of \\(F\\), there is a Cutting Planes refutation \\(\\pi'\\) of the same formula satisfying\n\\[\nL(\\pi')\\le C\\bigl(N(F)+L(\\pi)\\bigr)^k,\\qquad\nM(\\pi')\\le C\\bigl(N(F)+L(\\pi)\\bigr)^k?\n\\]\nBoth refutations use exactly the rules and variables defined below. The original coefficients are unrestricted, proof lines may be reused, and there is no space restriction. A negative answer is the full quantified negation: for every pair \\(C,k\\ge1\\), some \\(F,\\pi\\) admit no replacement satisfying both bounds. The violating instance may depend on \\(C,k\\)."

status = ('Open in the source tradition; the inspected 2021 handbook explicitly retains the coefficient-versus-length question as Open Problem 7.14. '
          'On 16 September 2026 this review checked the inference rules, the Buss–Clote exponential-magnitude normalization and the 2020 length–space separation. '
          'The latter imposes an additional space restriction and therefore does not refute the selected space-unrestricted statement. '
          'A bounded 2025–2026 search, including the scope of ECCC TR26-078, found no resolution of this exact user-specified target. '
          'The 2026 preprint is about tree-like bounded-line-size systems; its proof was not independently audited here. This is not an exhaustive literature certification or a Lean formalization.')

notes = [
    'Recovered and applied the user-approved single polynomial in input size plus original proof length; retained unrestricted space and separated existential simulation from an efficient proof-transforming algorithm.',
    'Specified Boolean CNFs, exact clause translation, syntactic Cutting Planes rules, reusable proof lines, formula size, line count, coefficient magnitude including right-hand sides, and all quantifiers.',
    'Separated coefficient bit length, polynomial magnitude and exponential magnitude; distinguished the known length–space separation from the requested length-only comparison.',
    'Retained original source provenance and category, individually assessed the previously unassessed importance, and supplied substantive context and Lean acceptance.',
]
checked = [
    'Inspected Buss–Clote author PDF §§2, 7–8, including the distinction between simulation and p-simulation and the exponential coefficient normalization.',
    'Inspected the Buss–Nordström 2021 chapter preprint §7.6.1 rules, Open Problem 7.14, and equation (7.64); checked that the tradeoff does not give a length-only separation.',
    'Inspected the saved 2020 lifting paper and the ECCC revision page, including its simultaneous length and line-space restrictions.',
    'Read ECCC TR26-078 abstract on 16 September 2026; its tree-like bounded-line-size scope differs from general reusable-line CP. Bounded current web search did not find a resolution.',
    'Recovered the explicit 16 September user selection from the prior thread; source statements with other polynomial conventions are not asserted equivalent to this editorial specification.',
]

complete(identifier, dict(
    formal=formal, definitions=definitions, question_type='yes_no',
    answer_criterion='Supply a complete Lean-checked proof of the displayed universally quantified simulation assertion or its full negation, for the precise syntactic proof system, \\(N\\), \\(L\\), and \\(M\\) defined here. An affirmative answer must establish one pair \\(C,k\\) working simultaneously for every input formula and every unrestricted-coefficient refutation. A negative answer must establish failure for every such pair; failure of one transformation or a lower bound with an additional memory restriction is insufficient. No numerical tolerance changes this proposition. A bibliography, experimental proof search, or a proof only for tree-like refutations does not substitute for the full theorem.',
    references=references,
    source_formulation=dict(text='The source asks whether arbitrary coefficients increase the strength of Cutting Planes over its polynomial-coefficient restriction. The user selected an existential, uniform polynomial bound in formula size plus original proof length, simultaneously on replacement length and coefficient magnitude, without a memory restriction.',caption='Editorial paraphrase with the user-selected polynomial convention',citation='handbook2021',format='editorial_paraphrase'),
    target_revision=dict(date='2026-09-16',previous_formal=old['formal'],authorization='User selected uniform polynomial simulation in the prior review thread.',scope='Existence of a replacement proof with one polynomial length-and-magnitude bound in N+L; no polynomial-time transformation or space bound is required.'),
    context_blocks=[
        block('Cutting Planes expresses Boolean constraints as integer linear inequalities. Its ability to add and round inequalities connects propositional proof complexity with integer programming and pseudo-Boolean reasoning. Numerical coefficients may compress information that takes many separate clauses to express. The question asks whether this numerical magnitude provides an indispensable advantage in the number of proof lines.', 'handbook2021'),
        block('The selected comparison permits a replacement proof to reorganize all inferences and to use arbitrary memory. It is consequently a statement about the existence of short bounded-magnitude certificates, rather than the runtime of a particular solver or conversion procedure. The uniform polynomial and its input parameter are fixed explicitly so that the benchmark has a definite truth value.', 'bussclote1996'),
        block('Buss and Clote showed that an exponential bound on numerical magnitudes suffices after a polynomial increase in length. Exponential magnitude can require only polynomially many bits, so this normalization does not supply the polynomial magnitude required here. The 2021 handbook still presents the general coefficient-strength comparison as an open question.', 'handbook2021'),
        block('The 2020 lifting result separates unrestricted and bounded coefficients when length and memory are constrained together. The relevant formulas still have short proofs when more memory is permitted, so that result does not answer this card. Later tree-like lower bounds likewise impose a restriction absent from the stated proof system.', 'lifting2020'),
    ],
    why='A resolution would determine whether the numerical size of coefficients is an essential resource for concise integer-inequality proofs, independently of memory. This is a central comparison among propositional proof systems and clarifies what short pseudo-Boolean certificates can express. It does not by itself guarantee an efficient algorithm for discovering those certificates.',
    importance=dict(score=84,method='editorial',reason='A central unresolved comparison in proof complexity: whether large integer coefficients provide a superpolynomial advantage in proof length after memory restrictions are removed. It isolates a fundamental resource of arithmetic reasoning rather than a parameter change in one solver.'),
    progress=[
        progress('1996','Buss and Clote established exponential-magnitude normalization with polynomial length overhead; this leaves polynomial magnitude unresolved.','bussclote1996'),
        progress('2020','A separation under simultaneous length and line-space restrictions was established, with no corresponding length-only separation asserted.','lifting2020'),
        progress('2021','The handbook retains the general coefficient-strength question as Open Problem 7.14 and separates it from the space question.','handbook2021'),
        progress('2026-09-16','The bounded status check distinguished newer tree-like, bounded-line-size lower bounds from the general proof system in this card.','tree2026'),
    ],
), notes, checked, status, summary=[
    'Cutting Planes refutes Boolean formulas by deriving contradictions from integer linear inequalities.',
    'The question asks whether every such proof can be replaced by one whose length and coefficient magnitudes obey a single polynomial bound in input size plus original proof length.',
    'Proof lines may be reused and memory is unrestricted, so the target is an existential comparison of certificates rather than an efficient conversion algorithm.',
    'Known exponential-magnitude normalization and separations involving memory do not settle this polynomial-magnitude target.',
    'A resolution would clarify whether large numerical coefficients are an essential resource for short arithmetic proofs of Boolean inconsistency.',
], expected_sha256=claim['input_sha256'], claim_token=claim['token'])
