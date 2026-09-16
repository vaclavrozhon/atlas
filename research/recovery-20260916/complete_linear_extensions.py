"""Complete the exact source threshold after reviewing the August 2026 proof."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/card-completion-20260913'))
from complete_review import complete, ref, block, progress
from review_queue import read_claims

identifier = 'TCS-0805'
old = json.loads((ROOT / 'data/cards' / f'{identifier}.json').read_text())
claim = read_claims(ROOT)[identifier]
references = old['references']
references[0]['locator'] = 'Dagstuhl Seminar 13331, §6.13, printed p. 67: first question, exact counting with exponential base below two'
references += [
    ref('oka2026', r'Breaking the \(2^n\) Barrier for Counting Linear Extensions with a Short Elementary Algorithm',
        'Keigo Oka', 2026, 'https://arxiv.org/abs/2608.19505v1',
        '19 August 2026 preprint; Theorem 1, §§2–5 and Appendix A; full proof and ancillary verifier inspected'),
    ref('kozma2020', 'Exact Exponential Algorithms for Two Poset Problems', 'László Kozma', 2020,
        'https://doi.org/10.4230/LIPIcs.SWAT.2020.30', 'Theorem 1 and §2: two-dimensional posets'),
    ref('sparse2016', 'Counting Linear Extensions of Sparse Posets',
        'Kustaa Kangas; Teemu Hankala; Teppo Niinimäki; Mikko Koivisto', 2016,
        'https://www.ijcai.org/Proceedings/16/Papers/092.pdf', 'IJCAI 2016, pp. 603–609; introduction and restricted-poset scope'),
]
status = (
    'Resolved affirmatively by a checked preprint: Oka, arXiv:2608.19505v1 (19 August 2026), '
    'Theorem 1 gives deterministic exact O*(1.89^n) counting for arbitrary n-element posets. '
    'On 16 September 2026 this review read the original Dagstuhl question and the complete proof in §§2–5, '
    'checked profile decoding, deadline-state aggregation and total state counts, and verified both base inequalities by exact integer/rational arithmetic. '
    'The author verifier passed on all 5,231 naturally labeled posets of orders one through six, 100 random cases and 120 targeted cases. '
    'Finite tests support but do not replace the proof. This is an arXiv preprint, not represented as peer reviewed, and no Lean proof was checked. '
    'A polynomial overhead is absorbed by a fixed slightly larger base still below two, answering the original O(c^n) existence question.')
notes = [
    'Recovered the first exact question of Dagstuhl §6.13; kept the adjacent treewidth-parameterized question separate.',
    'Defined labeled posets, explicit relation input, exact binary output, deterministic bit-cost model, worst-case time and uniform quantifiers.',
    'Read the complete 2026 proof and ran supporting finite checks; recorded preprint status and absence of Lean verification.',
    'Completed and archived the resolved target without silently substituting an optimal-base problem; preserved the existing importance score and category.',
]
checked = [
    'Full Dagstuhl August 2013 issue, §6.13 printed p. 67: exact counting on arbitrary posets in O(c^n) for some c<2.',
    'Oka 2026 v1, §§2–5: chain-partition bound, profile-decoding Lemma 1, deadline Lemma 2, equations (6)–(10), integer bit lengths and Theorem 1.',
    'Current arXiv metadata checked on 16 September: v1 submitted 19 August 2026, with ancillary verification code.',
    'Saved author verifier executed with --max-n 6 --cross-n 0 --random 100 --targeted 100 --targeted-wide 20; every check passed.',
    'Both displayed exponential bases were certified below 189/100 using exact integer/rational powers.',
    'Saved Kozma 2020 and Kangas et al. 2016 introductions distinguish restricted-poset algorithms from the new unrestricted target.',
]
complete(identifier, dict(
    title='Exact counting of linear extensions below base two',
    status='resolved', question_type='yes_no',
    formal=r'Does there exist a uniform deterministic algorithm \(A\), constants \(K>0\) and \(1<c<2\), and an integer \(n_0\), such that, for every \(n\ge n_0\) and every partial order \(P\) on \([n]\), \(A\) outputs the exact number \(e(P)\) of linear extensions using at most \(Kc^n\) bit-cost random-access steps? It must also terminate correctly on every smaller valid input. There is no restriction on the width, height, dimension, sparsity or a graph parameter of \(P\).',
    definitions=r'''For \(n\ge0\), let \([n]=\{1,\ldots,n\}\), with \([0]=\varnothing\). A partial order \(\le_P\) is a reflexive, antisymmetric and transitive binary relation on \([n]\). The input consists of binary \(n\) and its explicit \(n\times n\) Boolean relation matrix in row-major order. A list of comparable pairs or a Hasse diagram can be converted to this representation in polynomial time. Invalid matrices may be rejected in polynomial time; the time bound ranges over valid posets.

A linear extension is a permutation \((v_1,\ldots,v_n)\) of the distinct labels such that \(x\le_P y\) and \(x\ne y\) imply that \(x\) precedes \(y\). The integer \(e(P)\) counts these permutations. Elements with identical comparabilities remain distinct. The empty poset has one linear extension, and \(1\le e(P)\le n!\) for every finite poset. The required algorithm outputs this exact integer in binary; a sample, relative approximation or count modulo one prime is insufficient.

Use a uniform deterministic random-access machine with finite binary-string registers. Reading and writing a register charges for its address and data bits. Comparisons, Boolean operations, shifts and elementary integer arithmetic charge for all operand and output bits using standard polynomial bit-cost arithmetic algorithms. No arithmetic on arbitrarily large integers is a unit-cost operation. Time includes reading the input and writing the output, and is worst-case over all \(n\)-element input posets. There is no additional polynomial-space requirement. This makes the source's exponential-time convention explicit; the reviewed construction uses polynomial-bit addresses and counters and polynomial work per state.

The constants \(K,c,n_0\) and the finite algorithm are fixed before the input is chosen. A bound \(O(b^n n^d)\) with fixed \(b<2\) and \(d\) answers the question: any fixed \(c\) between \(\max\{1,b\}\) and two absorbs the polynomial factor for sufficiently large \(n\). A \(2^{n-o(n)}\) bound does not suffice. The task asks for existence of a strict constant-base improvement, not determination of the optimal base. The second question in the same source passage, about treewidth of the Hasse diagram, is distinct.''',
    answer_criterion=r'A complete Lean-checked affirmative answer must specify one algorithm and prove exact correctness and termination for every finite input poset, together with the uniform worst-case bound for fixed \(c<2\) in the stated model. A negative answer must prove the full negation of this existence claim. This is an algorithm-existence proposition requiring exact output; numerical benchmark tolerance does not replace exact counting by approximation. A citation or finite collection of tests is not a substitute for the Lean theorem.',
    source_formulation=dict(text='The first question of §6.13 asks for exact counting on arbitrary posets in exponential time with a fixed base below two. The adjacent question about fixed-parameter tractability by the treewidth of the Hasse diagram has a separate objective.',caption='Editorial paraphrase of the first source question',citation='primary',format='editorial_paraphrase'),
    references=references,
    context_blocks=[
        block('A partial order specifies precedence constraints while allowing incomparable elements. Counting compatible total orders measures the number of full rankings or schedules consistent with those constraints. This differs fundamentally from finding one compatible ordering, which is possible in polynomial time.', 'primary'),
        block('The 2013 question concerns unrestricted inputs. Earlier improvements for sparse or two-dimensional posets did not alone answer that worst-case question. The separate treewidth question concerns a different parameterized bound.', 'sparse2016'),
        block(r'Oka’s August 2026 preprint proves deterministic exact \(O^{*}(1.89^n)\) counting on arbitrary posets. Absorbing the polynomial overhead into a slightly larger fixed base below two answers the selected target. The complete proof received the bounded review recorded here; peer review and Lean verification are not claimed.', 'oka2026'),
    ],
    why='The target asks whether a canonical exact counting problem can beat the all-subsets exponential barrier on every input, despite the ease of finding one feasible ordering. It connects precedence counting with the structure of exact exponential algorithms. The original target is retained historically because a checked 2026 preprint now answers it.',
    progress=[
        progress('2013','Koivisto posed the unrestricted exact counting question with a fixed exponential base below two.','primary'),
        progress('2020','Kozma improved the exponential bound for two-dimensional posets, a restricted input class.','kozma2020'),
        progress('2026-08-19',r'Oka’s preprint states and proves deterministic exact \(O^{*}(1.89^n)\) counting on every finite poset.','oka2026'),
        progress('2026-09-16','The full new proof, its target match and auxiliary finite checks were reviewed; the historical question was archived with explicit verification limits.','oka2026'),
    ],
), notes, checked, status, summary=[
    'A linear extension orders all labeled elements of a poset while respecting every precedence constraint.',
    'The question asks for an exact deterministic counting algorithm with a fixed exponential base below two.',
    'Inputs are arbitrary finite posets, with no promise on dimension or other structural parameters.',
    'An August 2026 preprint answers this target, and its complete proof and supporting finite tests received the recorded review.',
    'The card is archived as resolved by a checked preprint, without claiming peer review or Lean formalization.',
], expected_sha256=claim['input_sha256'], claim_token=claim['token'],
    archive_reason='Oka, arXiv:2608.19505v1, Theorem 1 answers exact unrestricted sub-base-two counting. The complete proof and supporting finite checks were reviewed on 16 September 2026. Preprint status and absence of Lean verification are explicit.')
