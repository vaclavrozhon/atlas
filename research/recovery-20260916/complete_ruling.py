"""Individual completion of the user-selected n-dependent randomized lower bound."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete, ref, block, progress
from review_queue import read_claims

identifier='TCS-4193'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[0]['locator']='DISC 2017, §1 LOCAL/CONGEST conventions and §5 conclusion: extension of MIS lower bounds to 2-ruling sets'
refs += [
    ref('lower2020','Distributed Lower Bounds for Ruling Sets','Alkida Balliu; Sebastian Brandt; Dennis Olivetti',2020,
        'https://arxiv.org/abs/2004.08282v4','FOCS 2020; full version v4, 2 June 2022, abstract, §2.1 and randomized versus deterministic bounds'),
    ref('lowarb2026','Near-Optimal Distributed 2-Ruling Sets on Graphs with Low Arboricity',
        'Malte Baumecker; Rustam Latypov; Yannic Maus; Jara Uitto',2026,
        'https://arxiv.org/abs/2606.11974v3','14 September 2026 revision; §1.1 Theorems 1–2, low-arboricity and arbitrary-arboricity upper bounds'),
]
notes=[
    'Applied the explicit user choice of an n-dependent randomized LOCAL lower bound, with global success at least 1-1/n; did not transfer the source maximum-degree dependence indiscriminately.',
    'Defined 2-ruling sets, private randomness, identities, initial knowledge, unbounded messages/local computation, worst-case termination and the asymptotic quantifiers.',
    'Distinguished deterministic and randomized lower bounds and checked the 14 September 2026 low-arboricity results against the unrestricted-graph target.',
    'Preserved original provenance/category, individually assessed importance, and added Lean acceptance and a five-sentence summary.',
]
sources=[
    'Read original DISC 2017 PDF §1 and §5: exact independent-set/distance definition, LOCAL versus CONGEST, and the stated MIS lower-bound question.',
    'Read full 2004.08282v4 abstract, model §2.1 and introduction; its deterministic square-root-log bound differs from its randomized square-root-log-log bound.',
    'Read 2606.11974v3 dated 14 September 2026, abstract and §1.1 Theorems 1–2; O(log log n) holds for low arboricity, not arbitrary graphs.',
    'Current arXiv record and bounded 2025–2026 search checked on 16 September; no proof or refutation of the selected unrestricted randomized bound was identified.',
    'Recovered user decision: general graphs, Omega(sqrt(log n/log log n)), success at least 1-1/n. Explicit model and asymptotic conventions recorded.',
]
status=('The original source asks whether MIS lower bounds extend to 2-ruling sets. The user selected the unrestricted-graph randomized n-dependent bound stated here. '
        'The inspected 2020 lower-bound paper distinguishes deterministic and randomized guarantees; its deterministic bound is not a proof of this randomized assertion. '
        'The 14 September 2026 revision of the low-arboricity paper gives much faster algorithms on sparse graph classes and a separate arboricity-dependent bound, neither of which settles the selected worst case over all graphs. '
        'A bounded literature check on 16 September 2026 found no resolution of the precise selected target. Source theorem scopes were checked; full source proofs and a Lean formalization were not verified.')
complete(identifier,dict(
    question_type='yes_no',
    formal=r'''Is it true that every randomized LOCAL algorithm \(A\) that computes a 2-ruling set on every \(n\)-vertex graph with global success probability at least \(1-1/n\), for all \(n\ge2\), has worst-case round complexity
\[
T_A(n)=\Omega\!\left(\sqrt{\frac{\log_2 n}{\log_2\log_2 n}}\right)?
\]
Precisely, the proposed assertion is that for every such \(A\) there are constants \(c_A>0\) and \(n_A\ge4\) such that the displayed lower bound with multiplier \(c_A\) holds for every integer \(n\ge n_A\). The maximum ranges over all simple graphs, legal identifier and port assignments, and random outcomes in the model below. No maximum-degree or arboricity restriction is imposed.''',
    definitions=r'''The communication network is a finite simple undirected graph \(G=(V,E)\), with \(n=|V|\ge2\), possibly disconnected. Distance is the length of a shortest edge path and is infinite between different components. A 2-ruling set is a subset \(S\subseteq V\) with no edge joining two of its vertices and with every vertex at distance at most two from \(S\). In particular, isolated vertices must lie in \(S\). Maximal independent sets require distance at most one, which is a strictly stronger output condition.

Each vertex hosts a processor. Identifiers are an arbitrary injection \(V\to\{1,\ldots,n^3\}\). Each vertex's incident edges receive distinct local port numbers; the two port numbers on one edge need not agree. Initially a processor knows \(n\), its own identifier, its degree, its port numbers and its neighbors' identifiers, but not the whole graph. This fixes the usual polynomial identifier range and neighbor-knowledge convention. Giving neighbor identifiers initially changes the alternative convention by at most one communication round.

Processors execute the same finite algorithm, with identities and initial data as parameters. Rounds are synchronous: each processor performs finite local computation and sends one finite message of arbitrary length on each incident edge, and messages arrive by the end of the round. Local computation and memory are unrestricted and do not contribute to the round count. There are no additional communication links or free global coordination. Each vertex has its own independent stream of unbiased random bits; no correlated or graph-dependent advice is supplied.

Every processor must halt and irrevocably output a bit, marking membership in \(S\). Only algorithms with a finite deterministic worst-case round bound at each input size are under consideration. Let \(T_A(n)\) be the least integer bounding the time by which all processors halt, on every \(n\)-vertex graph, every legal identifier and port assignment, and every choice of random tapes. Thus this is not expected time or a running-time guarantee that may fail on a small-probability event.

For every fixed graph and identifier/port assignment, the probability over the independent tapes that all output bits together specify a valid 2-ruling set must be at least \(1-1/n\). This is one global correctness event, not a separate success bound per vertex. The constant \(c_A\) and threshold \(n_A\) in the target may depend on the algorithm, but not on an input graph, identifier assignment or random outcome. Logarithms in the formula have base two and the lower-bound formula is used only for \(n\ge4\).

The source asks broadly about extending MIS lower bounds, including degree-dependent forms. The user explicitly selected only the displayed dependence on \(n\), on general graphs, with the stated high-probability guarantee. A proof restricted to deterministic algorithms or to a different success/time convention does not establish this assertion.''',
    answer_criterion=r'Supply a complete Lean-checked proof or refutation of the quantified assertion above. An affirmative answer must apply to every uniform randomized algorithm in the stated LOCAL model, with the global success guarantee, and establish the lower bound for every sufficiently large input size. A negative answer must negate this full statement; no stronger little-o upper bound is imposed as an extra requirement on a refutation. A deterministic lower bound, a theorem about MIS rather than 2-ruling sets, or an algorithm only for a restricted graph class is insufficient. This is an asymptotic lower-bound proposition, not a numerical-value target with additive tolerance.',
    references=refs,
    target_revision=dict(date='2026-09-16',previous_formal=old['formal'],authorization='User selected the randomized general-graph n-dependent lower bound with success probability at least 1-1/n.',scope='Only the square-root-logarithmic bound in n is retained; other degree-dependent and CONGEST/message questions remain source context.'),
    source_formulation=dict(text='The source asks whether the LOCAL-model lower bounds for maximal independent set extend to 2-ruling sets. This card keeps the user-selected randomized bound as a function of graph order, without requiring every degree-dependent bound to transfer.',caption='Editorial paraphrase with user-selected lower-bound target',citation='primary',format='editorial_paraphrase'),
    context_blocks=[
        block('A ruling set relaxes maximal independent set by allowing a vertex to be covered from two communication hops away. The selected lower bound asks whether this extra radius still leaves a substantial worst-case barrier for randomized distributed symmetry breaking. It concerns time in the LOCAL model, where message size is unlimited.', 'primary'),
        block('Later work proved new ruling-set lower bounds, but deterministic and randomized complexities must be distinguished. A lower bound for deterministic processors does not automatically survive access to private random bits and a small global error probability.', 'lower2020'),
        block('The September 2026 preprint gives double-logarithmic time for graphs of low arboricity, where arboricity is the smallest number of forests whose union covers the edges. This shows that sparse families can admit far faster 2-ruling sets than the proposed unrestricted worst-case bound. Its separate bound for arbitrary arboricity does not refute the square-root-logarithmic target over all graphs.', 'lowarb2026'),
    ],
    why='The question tests how much a minimal relaxation of independence-based domination changes the locality of symmetry breaking. It separates the role of randomness, sparse structure and coverage radius from bandwidth restrictions, and would sharpen a central lower-bound boundary for distributed graph algorithms.',
    importance=dict(score=81,method='editorial',reason='A concrete unresolved extension of a central distributed symmetry-breaking barrier, distinguishing maximal independence from radius-two domination and randomized from deterministic locality.'),
    progress=[
        progress('2017','The source explicitly asks whether MIS lower bounds in LOCAL extend to 2-ruling sets.','primary'),
        progress('2020','New lower bounds for ruling sets distinguish deterministic and randomized algorithms; their quantifiers and model do not certify the selected stronger randomized n-bound.','lower2020'),
        progress('2026-09-14','The revised low-arboricity preprint gives fast algorithms on sparse classes and a separate general-arboricity bound.','lowarb2026'),
        progress('2026-09-16','A bounded later-work check retained the user-selected unrestricted-graph target as source-open, with explicit verification limits.','lowarb2026'),
    ],
),notes,sources,status,summary=[
    'A 2-ruling set is independent and covers every graph vertex within distance two.',
    'The question asks whether every highly reliable randomized LOCAL algorithm needs a square-root-logarithmic number of rounds in the worst case.',
    'Messages and local computation are unrestricted, and success means that the entire output set is correct with probability at least one minus one over the number of vertices.',
    'Deterministic lower bounds and faster algorithms for sparse graph classes do not by themselves settle the selected randomized bound on general graphs.',
    'A resolution would clarify how a small relaxation of maximal independence changes distributed symmetry-breaking complexity.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
