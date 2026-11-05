"""Source-reviewed, deliberately varied Miscellaneous candidates. Run once."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from import_cards import import_cards

DATE = '2026-11-05'


def ref(id, title, authors, year, url, locator='Statement, introduction and abstract.'):
    return dict(id=id, title=title, authors=authors, year=year, url=url, locator=locator)


def card(key, title, formal, definitions, why, context, references, score, **extra):
    c = dict(key='misc:' + key, title=title, area='Miscellaneous',
        year=min(r['year'] for r in references), is_new=True,
        evidence='reviewed', status='source_open', criterion='construction',
        question_type='yes_no', formal=formal, definitions=definitions,
        answer_criterion='Give a complete Lean-checked proof or refutation of the stated proposition, with all its quantifiers and hypotheses. Verification of finitely many parameter values does not establish the universal assertion.',
        why=why, context_blocks=[dict(text=t, citation=cite) for t, cite in context],
        references=references,
        progress=[dict(date=str(references[-1]['year']), citation=references[-1]['id'],
            text=context[-1][0])],
        status_note='Primary sources and a bounded search for later work checked on 5 November 2026. The general target remains open in the checked specialist literature; this is not an exhaustive status certification.',
        model_self_contained=True, requires_context=False,
        statement_review=dict(status='revised', reviewed_on=DATE, remaining_issue='',
            notes=['Definitions and quantifiers written explicitly; checked against the cited primary sources.'],
            scope='Individual review of a new candidate requested for the broader TCS scope.'),
        importance=dict(score=score, method='editorial', assessed_on=DATE, reason=why,
            basis='Broader TCS relevance and diversity across extremal combinatorics, information, dynamics, probability and discrete structures.'),
        category_assignment=dict(method='editorial_topic', reviewed_on=DATE,
            reason='A foundational discrete-mathematics question with a broad TCS connection, rather than a narrowly algorithmic target.'),
        related=[], related_problem_ids=[])
    c.update(extra)
    return c


cards = [card('union-closed-sets', "Frankl's union-closed sets conjecture",
    r'''For every finite set \(U\) and every family \(\mathcal F\subseteq 2^U\) containing a nonempty member and closed under union, is there an element \(u\in U\) belonging to at least \(|\mathcal F|/2\) members of \(\mathcal F\)?''',
    r'''The power set \(2^U\) consists of all subsets of U. A family is a set of distinct subsets, with no multiplicities. Closure under union means that A and B in the family imply that their union is also in it. The frequency of u is the integer \(|\{A\in\mathcal F:u\in A\}|\). Empty members are permitted, but the family consisting only of the empty set is excluded.''',
    'A basic closure principle for set systems, connected to information inequalities through entropy methods.',
    [('Gilmer obtained a positive universal frequency bound by comparing the information in random members with the information in their union.', 'gilmer'),
     ('Costa and Sadhu report a bound above 0.38288 in 2026. Their target and result still distinguish this progress from the conjectured one-half threshold.', 'recent')],
    [ref('gilmer', 'A constant lower bound for the union-closed sets conjecture', 'Justin Gilmer', 2022, 'https://arxiv.org/abs/2211.09055'),
     ref('recent', "Beyond Liu's 0.382709 threshold for the union-closed sets conjecture", 'Simone Costa; Ankan Sadhu', 2026, 'https://arxiv.org/abs/2610.02295')], 92),

card('hadamard-existence', 'Hadamard matrices of every order divisible by four',
    r'''For every positive integer \(n\), does there exist a \(4n\)-by-\(4n\) matrix \(H\) whose entries belong to \(\{-1,1\}\) and satisfy \(HH^{\mathsf T}=4nI_{4n}\)?''',
    r'''Matrix multiplication is over the real numbers. The superscript T means transpose, and \(I_m\) is the m-by-m identity matrix. The displayed equation says that different rows have dot product zero; each row has squared length 4n. Such a sign matrix is called a Hadamard matrix. The target is existence at every stated order, with no efficiency requirement on a construction.''',
    'Orthogonal sign patterns are basic objects in coding, signal design and combinatorial constructions.',
    [('The 2026 construction survey records the general existence conjecture while supplying new individual orders and a list of orders still missing. Solving finitely many missing orders does not prove existence for all multiples of four.', 'survey')],
    [ref('survey', 'Recent progress in the construction of Hadamard matrices', 'Ronan Egan; Ilias S. Kotsireas; Stephen London; Pádraig Ó Catháin', 2026, 'https://arxiv.org/abs/2610.27175', 'Version 2, 3 November 2026; existence conjecture and open problems.')], 89),

card('cap-set-exponent', 'Asymptotic exponent of the largest cap set',
    r'''Determine, to additive accuracy \(0.01\), the exponent
\[\gamma=\lim_{n\to\infty}\frac{\log_3 M(n)}{n},\]
where \(M(n)\) is the largest size of a subset \(A\subseteq\mathbb F_3^n\) such that \(x+y+z=0\) for \(x,y,z\in A\) implies \(x=y=z\).''',
    r'''The field \(\mathbb F_3\) has elements 0, 1 and 2 with arithmetic modulo 3; vector addition is coordinatewise. A set satisfying the stated condition is a cap set: it contains no nonconstant three-term arithmetic progression. The logarithm has base 3. Cartesian products of cap sets are cap sets, so \(M(n+m)\ge M(n)M(m)\). Together with \(1\le M(n)\le3^n\), this ensures that the limit exists and equals the supremum of the displayed ratios. For ambient size \(N=3^n\), the maximum is \(N^{\gamma+o(1)}\).''',
    'This asks for the quantitative limit of the polynomial method in additive combinatorics, a source of techniques for algorithms and lower bounds.',
    [('Ellenberg and Gijswijt proved an exponential saving over the ambient space size. That breakthrough establishes an exponent below one, without determining it.', 'upper'),
     ('Tyrrell constructs cap sets of size at least 2.218 to the power n for sufficiently large n. The large gap between construction and upper-bound methods motivates an exponent target.', 'lower')],
    [ref('upper', 'On large subsets of F_q^n with no three-term arithmetic progression', 'Jordan S. Ellenberg; Dion Gijswijt', 2016, 'https://arxiv.org/abs/1605.09223'),
     ref('lower', 'New Lower Bounds for Cap Sets', 'Fred Tyrrell', 2022, 'https://arxiv.org/abs/2209.10045')], 88,
    criterion='tightness', question_type='numerical_value',
    answer_criterion=r'Output a rational number q and a complete Lean-checked proof that \(|q-\gamma|\le0.01\). Equivalently, prove matching upper and lower bounds trapping gamma in an interval of width at most 0.02 and return its midpoint. A construction alone or the assertion gamma < 1 is insufficient.'),

card('lonely-runner', 'Lonely runner conjecture',
    r'''For every integer \(k\ge1\) and all distinct positive integers \(v_1,\ldots,v_k\), does there exist a real number \(t\ge0\) such that
\[\min_{1\le i\le k}\|tv_i\|_{\mathbb R/\mathbb Z}\ge\frac1{k+1}?\]''',
    r'''Here \(\|x\|_{\mathbb R/\mathbb Z}=\min_{m\in\mathbb Z}|x-m|\) is distance to the nearest integer. Think of k runners of speeds v_i starting with a stationary observer on a circle of circumference one. The formula asks for a time when every moving runner is at least 1/(k+1) away from that observer around the circle. The number of runners and speeds are unrestricted; no time bound is required.''',
    'A simultaneous separation question linking number theory, discrete geometry and graph coloring.',
    [('The survey explains the integer-speed formulation and connections to covering radii and distance-graph coloring.', 'survey'),
     ('The 2026 paper on lonely-runner relations restricts where counterexamples could lie, while retaining the conjecture for arbitrary numbers of runners.', 'recent')],
    [ref('survey', 'The Lonely Runner Conjecture turns 60', 'Guillem Perarnau; Oriol Serra', 2024, 'https://arxiv.org/abs/2409.20160', 'Version 3, 12 August 2025; introduction, reductions and connections.'),
     ref('recent', 'Lonely Runner Relations', 'Matthias Beck; Samuel Everett', 2026, 'https://arxiv.org/abs/2609.06259')], 83),

card('nivat', "Nivat's conjecture on rectangular pattern complexity",
    r'''Let \(A\) be a finite nonempty alphabet and \(c:\mathbb Z^2\to A\) a configuration. If for some positive integers m,n the number \(P_c(m,n)\) of distinct m-by-n rectangular patterns occurring in c is at most mn, must c have a nonzero global period?''',
    r'''Put \(R_{m,n}=\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\). A pattern occurring at translation t is the function on this rectangle that sends z to c(z+t). The number of distinct such functions as \(t\in\mathbb Z^2\) varies is \(P_c(m,n)\). A nonzero global period is a vector \(h\in\mathbb Z^2\setminus\{(0,0)\}\) such that c(z+h)=c(z) for every z. Only one period is required, not two linearly independent periods.''',
    'This connects the information in local pictures to global regularity, extending a central theorem about words to two-dimensional symbolic systems.',
    [('The June 2026 paper proves the short-rectangle case with one side four. Its statement retains arbitrary rectangles as the general conjecture.', 'partial'),
     ('A public repository from September 2026 claims the complete theorem and supplies Lean code. Its author explicitly notes the absence of expert mathematical digestion. This card records the claim without independently certifying the proof.', 'claim')],
    [ref('partial', 'A Modular Structure Theorem for Minimal Periodic Decompositions and Periodicity of Configurations with P_eta(4,n) <= 4n', 'C. F. Colle; E. Garibaldi', 2026, 'https://arxiv.org/abs/2606.10193'),
     ref('claim', "Pattern complexity and Nivat's conjecture", 'boonsuan (repository maintainer)', 2026, 'https://github.com/boonsuan/nivat', 'README, Challenge.lean and Solution.lean; September 2026 public claim.')], 87,
    criterion='characterization', status='uncertain',
    status_note='A complete Lean-formalized solution is claimed publicly in September 2026. The statement in the repository matches this target; the proof and formalization have not been independently audited here. The June 2026 specialist paper still treats the general case as open. Retained under the user policy allowing problems resolved after 1 January 2026.'),

card('distinct-subset-sums', "Erdős's distinct subset sums conjecture",
    r'''Does there exist an absolute real constant \(c>0\) such that, for every integer \(n\ge1\) and every increasing sequence of positive integers \(a_1<\cdots<a_n\) with all \(2^n\) subset sums distinct, one has \(a_n\ge c\,2^n\)?''',
    r'''For a subset S of {1,...,n}, its subset sum is \(\sum_{i\in S}a_i\), with empty sum zero. Distinctness means that different subsets always produce different sums. The single constant c must work for every sequence and every n. A sequence of counterexamples would have to make \(a_n/2^n\) arbitrarily small; one unusually efficient finite example alone does not refute the assertion.''',
    'How economically can binary choices be encoded by adding integer weights? This is an extremal counterpart of subset-sum encoding.',
    [('Powers of two provide an immediate construction at the conjectured exponential scale. The difficulty is the uniform positive factor in the lower bound.', 'primary'),
     ('Steinerberger gives an analytic perspective on the problem and the known lower-bound scale with an additional square-root loss. That loss is precisely what the conjecture removes.', 'primary')],
    [ref('primary', 'Some Remarks on the Erdős Distinct Subset Sums Problem', 'Stefan Steinerberger', 2022, 'https://arxiv.org/abs/2208.12182')], 82,
    criterion='tightness'),

card('rota-bases', "Rota's basis conjecture for matroids",
    r'''For every integer \(n\ge1\), every finite matroid of rank n, and every n bases \(B_1,\ldots,B_n\), can the elements in each B_i be ordered as \(b_{i,1},\ldots,b_{i,n}\) so that, for every j, the set \(\{b_{1,j},\ldots,b_{n,j}\}\) is also a basis?''',
    r'''A matroid consists of a finite set E and a collection I of independent subsets. The empty set belongs to I; subsets of independent sets are independent; and if A,B are independent with |A|<|B|, some element of B outside A can be added to A while retaining independence. A basis is a maximal independent subset, and the rank is its size, the same for all bases. Input bases may overlap: occurrences in different rows are separately positioned, but a column must contain n distinct independent elements of E. The target concerns arbitrary finite matroids, not only independence of vectors over a field.''',
    'A universal exchange principle for independence systems underlying greedy algorithms and matroid optimization.',
    [('The conjecture asks for a square array whose rows and columns are all bases. It requires an exact decomposition.', 'primary'),
     ('Montgomery and Sauermann prove asymptotically optimal packing and covering results in 2025. These allow a vanishing relative error and leave the exact n-column assertion open.', 'primary')],
    [ref('primary', "Asymptotically-tight packing and covering with transversal bases in Rota's basis conjecture", 'Richard Montgomery; Lisa Sauermann', 2025, 'https://arxiv.org/abs/2508.05601')], 89),

card('feige-deviation', "Feige's small-deviation conjecture",
    r'''For every positive integer n and independent nonnegative real random variables \(X_1,\ldots,X_n\) with \(\mathbb E X_i\le1\), is
\[\mathbb P\!\left[\sum_{i=1}^n X_i<\sum_{i=1}^n\mathbb E X_i+1\right]\ge e^{-1}?\]''',
    r'''Variables are defined on an arbitrary probability space and may have discrete, continuous or mixed distributions. Nonnegative means almost surely at least zero. Their expectations are finite by the hypotheses; independence is joint independence. The symbol e denotes the base of the natural logarithm. The inequality inside the probability is strict. No bound on the values or variances is assumed.''',
    'A sharp probability bound for sums with minimal hypotheses, arising in randomized algorithms and probabilistic combinatorics.',
    [('Earlier work proves the conjecture for discrete log-concave distributions, a restricted family rather than arbitrary independent variables.', 'partial'),
     ('Fu and coauthors announce a sharp finite-n bound in July 2026 which implies the displayed inequality. The card remains a candidate under the 2026 cutoff; this pass checks the announced statement rather than certifying its proof.', 'claim')],
    [ref('partial', 'On a conjecture of Feige for discrete log-concave distributions', 'Abdulmajeed Alqasem; Heshan Aravinda; Arnaud Marsiglietti; James Melbourne', 2022, 'https://arxiv.org/abs/2208.12702'),
     ref('claim', 'Sharp small-deviation inequalities for sums of independent nonnegative random variables', 'Weibo Fu; Yanjun Han; Guanyang Wang; Jun Yan; Peng Zhang; Zhengqing Zhou', 2026, 'https://arxiv.org/abs/2607.23980')], 88,
    criterion='tightness', status='uncertain',
    status_note='A complete proof is announced in arXiv:2607.23980, first submitted 27 July 2026. Its abstract explicitly covers the exact strict-inequality target and arbitrary independent nonnegative variables with means at most one. This pass did not audit the proof; retain the post-cutoff solution claim and source rather than label it an established theorem.'),

card('langton-highway', "Period-104 highway conjecture for Langton's ant",
    r'''Does every finite initial set of black cells in the standard two-color Langton ant process eventually produce a period-104 diagonal highway? Precisely, do there always exist an integer \(T\ge0\) and \(v\in\{(-2,-2),(-2,2),(2,-2),(2,2)\}\) such that for every \(t\ge T\), the ant's position and direction satisfy \(p_{t+104}=p_t+v\) and \(d_{t+104}=d_t\)?''',
    r'''Cells are the integer lattice \(\mathbb Z^2\), initially white except for an arbitrary finite set. One ant starts at an arbitrary cell facing north, east, south or west. At a white cell it turns right by 90 degrees; at a black cell it turns left by 90 degrees. It then flips that cell's color and moves one unit forward. The position p_t and direction d_t refer to the state before step t. There is no finite boundary or wrap-around. The conclusion concerns the future walk and headings, not translation of the entire colored grid, which retains the trail.''',
    'A concrete prediction problem for a tiny computational dynamical system: does every finite perturbation eventually organize into a repeating drifting walk?',
    [('The standard two-color rule is crucial. The 2025 paper disproves analogous highway expectations for other, multicolor turn rules while retaining the original conjecture.', 'primary')],
    [ref('primary', 'Sideways on the highways', 'Victor Lutfalla', 2025, 'https://arxiv.org/abs/2505.05426', 'Introduction and Section 2; original period 104 and displacement (+/-2,+/-2).')], 76,
    criterion='characterization')]


if __name__ == '__main__':
    target = ROOT / 'research/final-selection-20261105'
    if (target / 'misc-import.json').exists():
        raise SystemExit('Already imported; edit existing cards instead of rerunning.')
    (target / 'misc-new-candidates.json').write_text(json.dumps(cards, ensure_ascii=False, indent=2) + '\n')
    result = import_cards(cards)
    (target / 'misc-import.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result)
