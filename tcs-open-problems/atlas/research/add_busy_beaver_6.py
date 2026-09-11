"""User-requested exact determination of BB(6); primary sources checked 2026-09-10."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from authoring import finish, paragraph, ref, step


finish(
    'busy-beaver-6-exact-value',
    title='Determining the sixth Busy Beaver value BB(6)',
    area='Computability and algorithmic information',
    criterion='tightness',
    question_type='exact_value',
    formal=(
        'Determine the exact value of $BB(6)=S(6)$, the maximum number of steps '
        'taken before halting by a deterministic Turing machine with six nonhalting '
        'states, two tape symbols, and one initially all-zero, bi-infinite tape. '
        'The transition into a separate halting state counts as one step. '
        'Thus $BB(6)=\\max\\{T(M):M\\in\\mathcal{M}_6\\text{ halts on the blank tape}\\}$, '
        'where $T(M)$ counts executed transitions and the machine class is fixed below.'
    ),
    definitions=(
        'The states are A, B, C, D, E, F and a separate halting state Z; Z is not '
        'one of the six states being counted. Tape cells are indexed by the integers '
        'and contain 0 or 1. Initially every cell contains 0, the head is at cell 0, '
        'and the state is A. For each nonhalting state and scanned symbol, the '
        'transition table specifies a symbol to write, a move by exactly one cell '
        'left or right, and a next state. Execution stops on entering Z, including '
        'that final write-and-move transition in T(M). Unreachable states are allowed. '
        'The finite set of these transition tables is $\\mathcal{M}_6$. Here BB is '
        'the runtime (maximum-shift) function S, not the function $\\Sigma$ that '
        'maximizes the number of 1s left on the tape. In the progress note, '
        '$2\\uparrow\\uparrow k$ is a tower of k twos, and '
        '$2\\uparrow\\uparrow\\uparrow 1=2$, '
        '$2\\uparrow\\uparrow\\uparrow(k+1)=2\\uparrow\\uparrow(2\\uparrow\\uparrow\\uparrow k)$.'
    ),
    answer_criterion=(
        'Give an explicit positive integer N and prove BB(6)=N: exhibit a machine '
        'in the stated class that halts after exactly N transitions, and prove '
        'that every halting machine in this class takes at most N transitions. '
        'A finite, unambiguous expression using explicitly defined total operations '
        'is sufficient to specify N; its decimal expansion is not required. '
        'A larger lower bound or the analysis of only some remaining machines '
        'does not settle the question.'
    ),
    context=[
        paragraph(
            'Fixing the number of states leaves finitely many machines, so a maximum '
            'halting time exists. Nevertheless, enumerating their transition tables '
            'does not tell us when to stop waiting for the machines that never halt. '
            'The Busy Beaver function packages that obstruction into a sequence of '
            'finite integers. Noncomputability of the whole sequence does not prevent '
            'individual values from being established.',
            'model',
        ),
        paragraph(
            'The five-state case provides a concrete precedent: the bbchallenge '
            'collaboration proved S(5)=47,176,870 with the Coq proof assistant. '
            'Its proof combines a complete enumeration after symmetry reductions '
            'with methods that certify halting or nonhalting. The paper makes '
            'precise how a finite search can be accompanied by a universal proof.',
            'bb5',
        ),
        paragraph(
            'Six states introduce obstacles beyond running a larger search. The '
            'Antihydra machine has a halting question expressed through an integer '
            'recurrence whose parity behavior is still unresolved. A probabilistic '
            'heuristic about that behavior is not a proof that the machine runs '
            'forever. An exact Busy Beaver bound would also decide its halting '
            'behavior in principle, even if the required finite computation were '
            'physically infeasible.',
            'antihydra',
        ),
        paragraph(
            'The target is the exact six-state runtime maximum. Runtime and final '
            'tape output are different extremal quantities, and machine conventions '
            'matter. Existing catalogue questions about Busy Beaver growth, logical '
            'thresholds, or population protocols therefore remain separate problems.'
        ),
    ],
    why=(
        'This is a defining concrete problem in computability: identify the longest '
        'finite computation possible in a fixed, exceptionally small universal '
        'machine formalism. A proof would advance the boundary of complete '
        'mathematical understanding of small programs and test methods for '
        'nontermination proofs, recurrence analysis, and formal verification. '
        'The significance lies in establishing the exact boundary, not merely '
        'constructing a machine with an enormous runtime.'
    ),
    importance=dict(
        score=96,
        method='editorial',
        reason=(
            'A landmark finite problem at the frontier of computability and '
            'formal verification, asking for the next binary Busy Beaver runtime '
            'value after the resolved five-state case.'
        ),
        assessed_on='2026-09-10',
    ),
    progress=[
        step(
            '2025-06',
            'The project credits mxdys with a six-state halting machine establishing '
            '$S(6)>2\\uparrow\\uparrow\\uparrow 5$. This is a lower bound, not an '
            'exact determination.',
            'bb6',
        ),
        step(
            '2025-09-15; revised 2026-03-23',
            'The collaboration published its proof of S(5)=47,176,870, formally '
            'verified in Coq. The result settles the five-state case only.',
            'bb5',
        ),
        step(
            '2026-08-30',
            'The dated project list records 1,003 BB(6) holdouts after its '
            'equivalence reductions. This is a progress report from an informal '
            'search, not a certified exact value.',
            'holdouts',
        ),
        step(
            '2026-09-10 status check',
            'The project BB(6) page, revised on 3 September 2026, still lists '
            'the value as unsolved. Antihydra remains an example of the '
            'unresolved halting behaviors involved.',
            'bb6',
        ),
    ],
    references=[
        ref('bb6', 'BB(6)', 'Busy Beaver Challenge contributors', 2026,
            'https://wiki.bbchallenge.org/w/index.php?title=BB(6)&oldid=8417',
            'Revision of 3 September 2026; open status, champion, and holdouts'),
        ref('model', 'Story: Turing machines and the Busy Beaver function',
            'The bbchallenge Collaboration', 2024, 'https://bbchallenge.org/story',
            'Machine model and definition of BB; historical BB(5) sections contain outdated text'),
        ref('bb5', 'Determination of the fifth Busy Beaver value',
            'The bbchallenge Collaboration et al.', 2026,
            'https://arxiv.org/abs/2509.12337v2',
            'Abstract and main theorem; version 2, 23 March 2026; first submitted in 2025'),
        ref('antihydra', 'Antihydra', 'Busy Beaver Challenge contributors', 2026,
            'https://bbchallenge.org/antihydra',
            'Six-state halting obstruction; accessed 10 September 2026'),
        ref('holdouts', 'Holdouts lists', 'Busy Beaver Challenge contributors', 2026,
            'https://wiki.bbchallenge.org/wiki/Holdouts',
            'BB(6) table, 30 August 2026 entry shared by mxdys'),
    ],
    status='source_open',
    status_note=(
        'The primary project pages checked on 10 September 2026 still report '
        'BB(6) as unsolved. Lower bounds and holdout counts are attributed to '
        'the project; this review did not rerun its proofs or enumeration.'
    ),
    review_note=(
        'Added at the user’s explicit request. The convention is BB(6)=S(6), '
        'the runtime maximum, with six nonhalting states and two symbols. '
        'Checked against the catalogue for duplicates and against primary '
        'project sources for current status.'
    ),
    formulation_reviewed_on='2026-09-10',
)
