"""Reproducible owner-authorized target revisions; no selection mutations."""
import copy
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BEFORE = HERE / 'before'
BEFORE.mkdir(exist_ok=True)
decisions = {}


def original(number):
    ident = 'TCS-' + number
    path = ROOT / 'data/cards' / (ident + '.json')
    saved = BEFORE / path.name
    return json.loads((saved if saved.exists() else path).read_text())


def retain(number, reason):
    d = original(number)
    decisions[d['id']] = {'action': 'retained', 'reason': reason,
                          'question_type': d.get('question_type')}


def revise(number, title, formal, reason, summary, *, definitions=None,
           replace=(), context=None, criterion=None, refs=(), kind='yes_no'):
    d = original(number)
    old = copy.deepcopy(d)
    saved = BEFORE / (d['id'] + '.json')
    if not saved.exists():
        saved.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n')
    d.update(title=title, formal=formal, question_type=kind)
    if definitions is not None:
        d['definitions'] = definitions
    for a, b in replace:
        assert a in d['definitions'], (d['id'], a)
        d['definitions'] = d['definitions'].replace(a, b)
    if context:
        for i, text in context.items():
            d['context_blocks'][i]['text'] = text
    d['answer_criterion'] = criterion or (
        'Give a complete, mathematically correct Lean-checked proof of the '
        'displayed assertion or of its logical negation, with exactly the '
        'stated model, quantifier order and parameter dependence. A bound for '
        'a restricted subclass or one particular algorithm is insufficient '
        'to refute a universal existence assertion. Determining the entire '
        'optimal rate or a numerical approximation to it is not required.')
    assert len(summary) == 5
    d['working_summary'] = {
        'sentences': summary, 'basis': 'saved_sources',
        'source_basis': 'owner_authorized_binary_target_review',
        'written_on': '2026-11-06',
        'source_refs': [r['id'] for r in d.get('references', [])]
    }
    d['updated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    d['formulation_reviewed_on'] = '2026-11-06'
    d['statement_review'] = {
        'status': 'revised', 'reviewed_on': '2026-11-06', 'remaining_issue': '',
        'notes': [reason, 'Aligned the statement, definitions, answer criterion and summary with the selected target.'],
        'scope': 'Owner-authorized target selection and formulation review; the deferred whole-catalogue current-status audit was not resumed.'
    }
    d['quality_review'] = {
        'reviewed_on': '2026-11-06', 'state': 'revised',
        'reference_card': 'TCS-0001', 'changes': d['statement_review']['notes'],
        'checked_sources': list(refs),
        'scope': d['statement_review']['scope']
    }
    if 'context' in d and d.get('context_blocks'):
        d['context'] = '\n\n'.join(b['text'] for b in d['context_blocks'])
    for key in ('id', 'area', 'importance', 'status', 'evidence', 'benchmark_eligibility'):
        assert d.get(key) == old.get(key), (d['id'], key)
    (ROOT / 'data/cards' / (d['id'] + '.json')).write_text(
        json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    decisions[d['id']] = {
        'action': 'converted', 'previous_title': old['title'],
        'previous_question_type': old.get('question_type'), 'title': title,
        'target': formal, 'question_type': kind, 'reason': reason, 'source_urls': list(refs)
    }


revise('0007', 'Matrix multiplication exponent two',
       r'Does the matrix multiplication exponent over \(\mathbb C\) equal two? Precisely, for the exact arithmetic-circuit size \(s(n)\) defined below, is it true that \[\forall\varepsilon>0\ \exists C_\varepsilon>0\ \forall n\in\mathbb N_{\ge2},\qquad s(n)\le C_\varepsilon n^{2+\varepsilon}?\] The circuit family and its constants may depend on \(\varepsilon\); an \(O(n^2)\) bound is not required.',
       'Restored the source conjecture omega = 2, retaining nonuniform complex arithmetic circuits and nonattainment of the exponent infimum.',
       ['Matrix multiplication computes all entries of the product of two input matrices.', 'The card asks whether every exponent strictly above two is achievable by exact complex arithmetic circuits.', 'The circuit model allows nonuniform constants and charges arithmetic gates.', 'This does not require a quadratic-size family attaining the endpoint exponent.', 'A proof or refutation settles the quadratic-exponent conjecture.'],
       replace=[("The source’s conjecture \\(\\omega=2\\) is one possible value of the numerical target selected for this card.", r'The binary target is \(\omega=2\), with the positive-slack convention just stated.')],
       context={1: r'The selected target is the familiar conjecture \(\omega=2\). Because \(\omega\) is an infimum, a separate circuit family and constant are permitted for every positive slack in the exponent. This is weaker than requiring an \(O(n^2)\) circuit-size bound and is distinct from numerical approximation of the exponent.',
                4: r'An upper bound strictly above two does not by itself settle this binary question. Conversely, a negative answer must prove \(\omega>2\) for unrestricted circuits, rather than a barrier for one tensor framework.'},
       refs=['https://www.math.ias.edu/files/mathandcomp.pdf'])

d=original('0128')
defs=d['definitions'][:3]
defs.append(r'The function \(C(n)\) is the worst-case minimum complement size defined in the statement. The lower bound asks for arbitrarily large input-size bounds, not for a hard example at every size. The constant \(c\) is universal; the automaton may depend on the size bound. No construction-time bound is imposed.')
revise('0128', 'Exponential complementation lower bounds for unambiguous automata',
       r'Can complementing a binary unambiguous finite automaton require exponentially many states even if the complement may be represented ambiguously? For \[C(n)=\max_A\min\{|Q_B|:L(B)=\{0,1\}^{*}\setminus L(A)\},\] where \(A\) ranges over binary unambiguous automata with between one and \(n\) states and \(B\) over binary nondeterministic automata, does \[\exists c>0\ \forall N\ge1\ \exists n\ge N,\qquad C(n)\ge2^{cn}\] hold?',
       'Selected the exponential-lower-bound endpoint posed by the source, specializing explicitly to the existing binary alphabet and retaining ambiguous outputs.',
       ['An unambiguous automaton has at most one accepting run for each word.', 'Its complement must accept exactly the words that the input automaton rejects.', 'The card asks whether some binary inputs require exponentially many complement states at arbitrarily large sizes.', 'The output is allowed to be an arbitrary nondeterministic automaton.', 'The target concerns representation size rather than the time to build the complement.'],
       definitions=defs,
       context={0:'The source asks for better complementation bounds, with a broad binary-alphabet gap. This card selects its exponential-lower-bound endpoint instead of requesting the entire optimal growth function.',1:'The consolidated 2018 source asks whether general-alphabet complementation can require exponentially many states. The retained binary-alphabet formulation is an explicit specialization of that endpoint; it is not asserted to be equivalent to a growing-alphabet version.'},
       refs=['https://doi.org/10.4230/LIPIcs.ICALP.2018.138','https://arxiv.org/abs/2109.09155'])

d=original('0154')
defs=d['definitions'].split('The polynomial growth exponent is the infimum')[0]
defs+=r'The assertion \(s(n)=O(\log n)\) is expressed for all positive lengths using \(\log_2(n+1)\). One universal constant must cover every length and every pair of distinct words; no efficiency bound is imposed on constructing the separating automaton.'
revise('0154', 'Separating words problem',
       r'Does there exist a universal constant \(C>0\) such that any two distinct binary words of length \(n\ge1\) can be distinguished by a deterministic finite automaton with at most \(C\log_2(n+1)\) states? Distinguishing means accepting exactly one of the two words, with unrestricted behavior on all other words. The automaton may depend on the pair, and its complete one-pass transition model is defined below.',
       'Restored the source logarithmic-state conjecture under the later authorization to binarize asymptotic targets; this supersedes this card’s earlier 0.01 exponent target.',
       ['Two distinct binary strings are given at the same length.', 'A separating deterministic finite automaton must accept exactly one of them.', 'The question asks whether a logarithmic number of states always suffices.', 'The automaton may depend on both strings and has no restriction on other inputs.', 'This is stronger than merely asking whether the polynomial growth exponent is zero.'],
       definitions=defs, context={0:'The selected binary target is the original logarithmic-state question. A universal logarithmic bound would imply polynomial growth exponent zero, whereas exponent zero alone also permits faster-than-polylogarithmic growth. The owner’s later binary-target instruction supersedes the earlier numerical-exponent version of this card.'},
       refs=['https://automata.exchange/19.04-separating-words-problem/'])

d=original('0300')
defs=d['definitions']
start=defs.index('An upper rate')
end=defs.index('The array has fixed')
defs=defs[:start]+defs[end:]
defs=defs[:defs.index('Here \\(f(n)\\)')]
revise('0300', 'Logarithmic randomized online labeling',
       r'Is there one uniform randomized online list-labeling algorithm and a universal constant \(C>0\) such that, for every capacity \(n\ge2\) and every obliviously fixed valid sequence of \(M\ge0\) insertions and deletions, its expected total movement cost is at most \[C\bigl(n+M\log_2(n+2)\bigr)?\] At most \(n\) items are live, and their order-preserving labels must lie in \(\{1,\ldots,2n\}\). Cost, validity and the oblivious-adversary convention are defined below.',
       'Selected the logarithmic expected-amortized upper bound that closes the source’s log-log gap, retaining movement cost, deletions, constant slack and oblivious sequences.',
       ['Online labeling stores a changing ordered list in an array with spare slots.', 'An update can force existing items to change labels.', 'The question asks for logarithmic expected amortized movement with a constant fraction of spare space.', 'The adversary fixes the full update sequence independently of the random choices.', 'Local computation is free, so the target does not assert logarithmic machine running time.'],
       definitions=defs,
       context={5:'The selected target keeps constant slack, both insertions and deletions, and an oblivious adversary. It asks whether the known logarithmic lower-bound scale is achievable, without requesting the entire optimum if that endpoint fails.'},
       refs=['https://arxiv.org/abs/2405.00807'])

revise('0403', 'Near-linear-time exact Euclidean minimum spanning trees',
       r'For every fixed integer \(d\ge3\), is there one deterministic algorithm \(A_d\), a constant \(C_d>0\), and an integer \(a_d\ge1\) that compute an exact Euclidean minimum spanning tree of any \(n\ge2\) distinct points in \(\mathbb R^d\) in at most \[C_d n\bigl(\log_2(n+2)\bigr)^{a_d}\] worst-case steps in the real-arithmetic model below? The input is an array of coordinates \(p_1,\ldots,p_n\). The output is a list of \(n-1\) index pairs forming a connected acyclic graph \(T\) minimizing \(\sum_{\{i,j\}\in T}\|p_i-p_j\|_2\). The program and constants may depend on fixed \(d\), but not on \(n\) or the coordinates.',
       'Applied the owner’s explicit near-linear exact-MST example, preserving deterministic worst-case real arithmetic and every fixed dimension at least three.',
       ['A Euclidean minimum spanning tree connects the input points with minimum total edge length.', 'The complete graph is implicit in the point coordinates.', 'The question asks for exact computation in time equal to the number of points times a fixed power of its logarithm.', 'The guarantee must hold deterministically in every fixed dimension at least three.', 'Approximate trees and expected-time bounds alone do not meet this target.'],
       context={0:r'The original entry asks whether exact Euclidean MST computation can approach the sorting-scale \(\Omega(n\log n)\) lower bound. At the owner’s request, this card selects an \(n\operatorname{polylog}n\) deterministic worst-case upper bound in each fixed dimension. This is an explicit interpretation of “close,” without requiring the optimal logarithmic exponent.'},
       refs=['https://topp.openproblem.net/p5'])

revise('0408', 'Near-linear-time exact planar Euclidean matching',
       r'Is there one uniform deterministic algorithm and universal constants \(C>0\), \(a\in\mathbb N_{\ge1}\) that compute a minimum-length perfect matching of any \(2n\) distinct points in \(\mathbb R^2\), for every \(n\ge1\), in at most \[Cn\bigl(\log_2(n+2)\bigr)^a\] worst-case steps in the exact real-arithmetic model below? The output is a list of \(n\) unordered index pairs, each index occurring once, minimizing \(\sum_{\{i,j\}\in M}\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}\). The input consists only of the coordinates, with no bipartition or geometric promise.',
       'Selected a near-linear exact-algorithm target from the source’s optimal-time question, retaining unrestricted planar matching, Euclidean lengths and deterministic worst-case arithmetic.',
       ['A perfect matching pairs every planar input point with one other point.', 'Its objective is the sum of the ordinary Euclidean lengths of all pairs.', 'The question asks for an exact deterministic algorithm in near-linear worst-case time.', 'No red-blue bipartition or general-position promise is supplied.', 'Squared lengths and approximate matchings define different objectives.'],
       context={0:'The Open Problems Project asks for the optimal complexity of exact planar Euclidean matching. This card selects the concrete near-linear deterministic upper-bound target, retaining unrestricted matching rather than the separately mentioned bipartite variant.'},
       refs=['https://topp.openproblem.net/p6'])

d=original('2336')
game=d['formal'][d['formal'].index('For the prediction game'):d['formal'].index('Retain all logarithmic')]
revise('2336', 'Square-root multiclass regret from Littlestone dimension',
       r'Does there exist a universal constant \(C>0\) such that, for every pair of nonempty sets \(X,Y\), every nonempty class \(H\subseteq Y^X\) of Littlestone dimension at most \(d\), and all integers \(T\ge d\ge1\), the minimax expected regret satisfies \[R_T(H)\le C\sqrt{dT}?\] Infinite instance and label sets are allowed, and no regularity or computability restriction on the class is added. '+game,
       'Restored the source’s square-root multiclass regret conjecture, retaining unrestricted label sets and no minimax regularity assumption.',
       ['An online learner predicts a label and then observes the correct one.', 'Regret compares its expected mistakes with the best fixed hypothesis in hindsight.', 'Littlestone dimension measures the depth of binary prediction trees realizable by the class.', 'The question asks for a universal square-root dimension-times-horizon regret bound.', 'The constant cannot grow with the number of labels, even for infinite label spaces.'],
       context={4:'The binary question restores the source’s square-root upper-bound conjecture. It retains arbitrary instance and label sets and does not add the regularity condition used in some sharper special-case theorems. The known lower scale motivates this endpoint; a complete determination of an alternative rate is not required.'},
       refs=['https://proceedings.mlr.press/v195/hanneke23b.html'])

revise('3906', 'Linear-in-state-count symmetric Markov-chain identity testing',
       r'Does there exist one uniform randomized tester and a universal constant \(C>0\) that, for every integer \(n\ge2\), rational \(0<\varepsilon\le1/4\), and explicitly supplied symmetric reference transition matrix \(Q\), tests an unknown symmetric chain \(P\) using at most \(\lceil Cn/\varepsilon\rceil\) observed transitions of one trajectory? For every starting state it must accept with probability at least \(2/3\) when \(P=Q\) and reject with probability at least \(2/3\) when \[\Delta(P,Q)=1-\rho\!\left((\sqrt{P_{ij}Q_{ij}})_{i,j}\right)>\varepsilon.\] Here \(\rho\) is spectral radius. The access model below permits neither resets nor a chosen starting state; reducible chains are included.',
       'Selected the source’s n/epsilon trajectory-length upper-bound conjecture, retaining reducible chains, worst-case starts and the spectral discrepancy.',
       ['The tester observes one trajectory of an unknown symmetric Markov chain.', 'It is also given the complete transition matrix of a reference chain.', 'The question asks for a number of transitions proportional to the state count divided by the discrepancy tolerance.', 'The guarantee must hold from every starting state without restarts or irreducibility promises.', 'The spectral discrepancy avoids requiring distinctions that the observed trajectory cannot reveal.'],
       context={3:'The original sample cost counts observed states; this card counts transitions after the initial state, a difference of one. The selected binary target is the source’s conjectured linear-in-state-count, inverse-proximity upper bound, with its strict farness convention.'},
       refs=['https://proceedings.mlr.press/v75/daskalakis18a.html'])

revise('6558', 'Černý conjecture',
       r'Does every synchronizing complete deterministic finite automaton with \(n\ge1\) states have a reset word of length at most \((n-1)^2\)? The statement quantifies over all finite nonempty alphabets. A reset word sends every possible initial state to the same state, under the transition model below.',
       'Restored the classical Černý bound instead of requiring the full extremal reset-length function.',
       ['A synchronizing automaton has an input word that sends all states to one common state.', 'This word resets the system without observing its unknown initial state.', 'The Černý conjecture bounds the shortest reset word by the square of one less than the number of states.', 'The assertion covers every complete deterministic automaton and every finite alphabet.', 'Known extremal examples explain the exact quadratic threshold.'],
       definitions=r'An automaton is a finite transition system \(A=(Q,\Sigma,\delta)\), where \(|Q|=n\ge1\), \(\Sigma\) is a finite nonempty alphabet and \(\delta:Q\times\Sigma\to Q\) is total. Extend it to words by \(\delta(q,\epsilon)=q\) and \(\delta(q,wa)=\delta(\delta(q,w),a)\). A word \(w\) is a reset word if \(|\{\delta(q,w):q\in Q\}|=1\); its length is its number of letters. Synchronizing means that at least one reset word exists. Its final state is not prescribed. Initial and accepting states play no role, and the empty word handles \(n=1\). There is no strong-connectivity, fixed-alphabet or other structural promise. Partial or nondeterministic automata, and synchronization of only a prescribed subset of states, are different models. No time bound for constructing the word is imposed. In the context, \(T(n)\) denotes the maximum shortest-reset-word length over all such synchronizing automata with \(n\) states; duplicate letter transformations can be removed, so this maximum exists.',
       context={0:r'The selected binary question is the Černý conjecture. Its \((n-1)^2\) upper bound would match the classical worst-case family. A counterexample to the universal bound also answers this card; it need not determine the entire extremal function.'},
       refs=['https://doi.org/10.4213/rm10005e','https://arxiv.org/abs/2608.24245'])

revise('6529', r'Logarithmic \(\ell_1\) distortion lower bound for planar Earth Mover Distance',
       r'Do there exist universal constants \(c>0\) and \(n_0\ge2\) such that \[D(n)\ge c\log_2 n\qquad\text{for every integer }n\ge n_0?\] Here \(D(n)\), defined below, is the least bi-Lipschitz distortion into \(\ell_1\) of the space of all probability measures on \(\{0,1,\ldots,n-1\}^2\), equipped with Earth Mover Distance using Euclidean ground distances.',
       'Selected the logarithmic lower-bound endpoint, preserving the 2026 resolution and benchmark eligibility; constant distortion was already excluded before the cutoff.',
       ['Earth Mover Distance is the minimum cost of transporting one probability measure into another.', 'The input measures live on a planar square grid with Euclidean transport costs.', 'The question asks whether every embedding of the whole measure space into ell-one incurs at least logarithmic distortion.', 'Arbitrary nonlinear embeddings and all real probability weights are permitted.', 'The retained 2026 resolution proves this lower-bound target, whose Lean formalization remains a valid benchmark answer.'],
       context={0:r'Naor and Schechtman establish the historical gap between an \(\Omega(\sqrt{\log n})\) lower bound and an \(O(\log n)\) upper bound. The binary target selects the logarithmic lower endpoint that was open at the benchmark cutoff; constant distortion was already ruled out earlier.'},
       refs=['https://doi.org/10.1137/05064206X','https://doi.org/10.1145/3798129.3800785'])

d=original('6783')
defs=d['definitions'].replace('Both extrema exist because there are finitely many graphs on a fixed labeled vertex set and \\(H=G\\) is feasible. ', '')
revise('6783', 'Four-additive spanners with four-thirds-power size',
       r'Does there exist a universal constant \(C>0\) such that every connected simple undirected unweighted graph \(G\) on \(n\ge2\) vertices has a spanning subgraph \(H\) with \[|E(H)|\le Cn^{4/3}\qquad\text{and}\qquad d_H(u,v)\le d_G(u,v)+4\quad\text{for all }u,v\in V(G)?\] Distances count edges. New edges, weights and vertices are not permitted, and no construction-time bound is imposed.',
       'Restored the survey’s O(n^(4/3))-edge existence target for +4 additive error, with no logarithmic slack.',
       ['A spanner retains a subset of graph edges while approximately preserving distances.', 'This card permits an additive increase of at most four edges for every vertex pair.', 'It asks whether the retained subgraph always needs only a constant times n to the four-thirds edges.', 'Only original unweighted edges may be retained.', 'The statement is an existence question independent of construction time.'],
       definitions=defs, context={3:r'The selected question is the survey’s \(O(n^{4/3})\) upper-bound target. The constant is universal and no growing logarithmic factor is hidden. A refutation need not determine the alternative optimal edge count.'},
       refs=['https://arxiv.org/abs/1909.03152'])

d=original('7174')
defs=d['definitions']
a=defs.index('A matching rate')
b=defs.index('A fresh hardcoded')
defs=defs[:a]+r'The notation \(o(n\log n)\) means \(\lim_{n\to\infty}t_M(n)/(n\log_2(n+2))=0\). '+defs[b:]
revise('7174', 'Integer multiplication below n log n time',
       r'Does there exist one uniform deterministic multitape Turing machine \(M\) that exactly multiplies every pair of \(n\)-bit nonnegative binary integers, with explicit \(2n\)-bit output, and whose worst-case transition count satisfies \[\lim_{n\to\infty}\frac{t_M(n)}{n\log_2(n+2)}=0?\] The machine has a fixed finite alphabet and fixed number of tapes, and the same program must work for all input lengths. The bit and tape-access model is specified below.',
       'Selected the o(n log n) algorithmic threshold; merely asking for near-linear multiplication would be settled by the pre-cutoff O(n log n) theorem.',
       ['The inputs are two binary integers and the output is their exact product.', 'Time counts elementary transitions of a fixed multitape Turing machine.', 'The question asks whether the worst-case running time can be little-o of n log n.', 'Near-linear O(n log n) multiplication alone does not answer this stronger question.', 'Arithmetic instructions on unbounded integers and random-access machines are different models.'],
       definitions=defs,
       context={2:r'Harvey and van der Hoeven proved an \(O(n\log n)\) multitape upper bound in 2021. That theorem settles the earlier upper-bound conjecture, but does not prove optimality. Their 2025 paper records the absence of an unrestricted superlinear lower bound. The selected binary question asks whether the n log n scale can be improved by an unbounded factor; these are dated source bounds, not a fresh November 2026 status certification.'},
       refs=['https://annals.math.princeton.edu/2021/193-2/p04','https://arxiv.org/abs/2503.22848'])


def exponent_criterion(symbol, domain=''):
    return (r'Supply an unambiguously specified real answer '+symbol+domain+
            r' and a complete Lean-checked proof of absolute error at most \(1/100\) in the defined exponent. A certified enclosing interval of width at most \(1/50\) qualifies via its midpoint. Both sides of the interval must be justified. An exact value also qualifies. The infimum need not be attained, and no ordinary logarithmic growth limit is assumed. Matching logarithmic factors, leading constants and an algorithm attaining the endpoint exponent are not required. A one-sided improvement alone qualifies only if the resulting certified interval is sufficiently narrow.')


# The owner clarified that an interval without a canonical binary endpoint
# should retain its optimum to absolute 0.01; do not invent a cubic endpoint.
retain('0029', 'Retained the 0.01 randomized-versus-quantum exponent target: no source conjecture singles out the cubic endpoint over the quartic endpoint.')

d=original('6683')
defs=d['definitions'].split('Asymptotic convention.')[0]
defs+=r'Exponent convention. Define \[x_{\mathrm{grid}}=\inf\{a\in\mathbb R_{\ge0}:\exists C>0\ \exists r_0\ge2\ \forall r\in\mathbb Z_{\ge r_0},\ f(r)\le Cr^a\}.\] The known polynomial Grid-Minor Theorem makes this set nonempty; the cited ninth-power bound with polylogarithmic overhead gives \(x_{\mathrm{grid}}\le9\), and the quadratic-logarithmic lower bound gives \(x_{\mathrm{grid}}\ge2\). The exponent is equivalently the limit superior of \(\log f(r)/\log r\); no ordinary limit or attainment of the infimum is assumed. In particular, exponent two permits a growing logarithmic factor and does not assert \(f(r)=O(r^2)\). Constants may depend on a chosen positive slack in the exponent, but not on the grid side length or host graph. This is a structural existence exponent, not a running-time exponent for finding a grid.'
revise('6683', 'Excluded-grid treewidth exponent',
       r'Determine the excluded-grid exponent \(x_{\mathrm{grid}}\) to absolute error at most \(1/100\). For each integer \(r\ge2\), let \[f(r)=\min\{t\in\mathbb Z_{\ge0}:\forall G,\ \operatorname{tw}(G)\ge t\Longrightarrow Q_r\text{ is a minor of }G\},\] where \(G\) ranges over finite simple undirected graphs and \(Q_r\) is the \(r\)-by-\(r\) square grid. Define \[x_{\mathrm{grid}}=\inf\{a\ge0:f(r)=O(r^a)\}.\] The precise asymptotic quantifiers, treewidth and ordinary graph-minor model are given below. The parameter \(r\) is grid side length, not its \(r^2\) vertices. Logarithmic factors are outside the requested precision.',
       'Applied the owner’s explicit Excluded Grid correction: ask for the finite growth exponent within 0.01, without matching logarithmic factors or silently asserting an attained quadratic bound.',
       ['The Grid-Minor Theorem forces a large square grid minor when treewidth is sufficiently large.', 'The extremal threshold is measured against the side length of that grid.', 'The card asks for the polynomial growth exponent of this threshold to absolute accuracy 0.01.', 'A grid of side length r has r squared vertices, so the parameter convention matters.', 'Logarithmic factors and the exact threshold function are not part of this numerical target.'],
       definitions=defs, kind='numerical_value', criterion=exponent_criterion(r'\(a_*\)'),
       context={4:r'The selected numerical exponent distinguishes polynomial scales while ignoring logarithmic factors. In particular, a proved \(r^2\operatorname{polylog}r\) upper bound together with the known lower bound would give exponent exactly two and answer this card.',
                5:r'Chuzhoy and Tan prove \(f(r)\le Cr^9(\log r)^c\) for absolute constants \(C,c>0\). Together with the quadratic-logarithmic lower bound, this places the requested exponent in \([2,9]\). These are bounds recorded in the cited literature; the present formulation review does not certify a fresh catalogue-wide status audit.',
                6:r'Robertson, Seymour and Thomas predicted growth \(\Theta(r^2\log r)\), whereas Demaine and coauthors predicted cubic growth. These predictions would yield numerical exponents two and three respectively. Determining the exponent to absolute error \(1/100\) is the selected target; settling lower-order factors is not required.'},
       refs=['https://arxiv.org/abs/1901.07944'])


exec((HERE / 'standard_targets.py').read_text())
exec((HERE / 'exponent_targets.py').read_text())
exec((HERE / 'new_green_targets.py').read_text())
exec((HERE / 'wording_cleanup.py').read_text())

if __name__ == '__main__':
    (HERE / 'decisions.json').write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + '\n')
    print('Target decisions:', len(decisions))
