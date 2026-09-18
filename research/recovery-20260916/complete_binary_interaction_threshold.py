"""Define the positive-rate deterministic bit-flip threshold."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4802';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='The maximal error fraction for constant-rate binary two-way codes',
 status='source_open',criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, with certified absolute error at most \(1/100\), the constant
\[
\rho_* = \sup\{\rho\in[0,1]:\ \rho\text{ is achievable by a constant-rate deterministic binary two-way code}\}.
\]
Here Alice must transmit an arbitrary \(n\)-bit string to Bob; the speaking schedule is fixed before communication, and an adversary can flip up to a \(\rho\) fraction of all bits sent in both directions. Achievability and the cost model are defined below.''',
 definitions=r'''For each integer \(n\ge1\), a protocol consists of an integer \(T_n\ge1\), a fixed sequence \(p_n\in\{A,B\}^{T_n}\) specifying who sends each bit, deterministic local message functions, and a deterministic output function for Bob. Alice initially knows \(x\in\{0,1\}^n\); Bob has no private input. Both know \(n\), the protocol and the schedule. They have no shared secret, private randomness or public randomness.

Initially each party's local transcript is empty. At step \(t\), the designated sender computes a bit from its local transcript and, for Alice, her input \(x\). The sender appends that sent bit to its transcript. The receiver appends the received bit, which the adversary may replace by its complement. Both transcripts therefore have length \(t\), but may differ. After exactly \(T_n\) steps Bob outputs an \(n\)-bit string determined by his transcript. The speaking sequence and stopping time cannot depend on the input, received bits or adversary.

The adversary knows the input and protocol, sees the bits being sent, and may adapt its flips to the entire execution. It can corrupt either direction, with one shared budget of at most \(\lfloor\rho T_n\rfloor\) flips. Correctness requires Bob's final output to equal \(x\) for every input and every permitted corruption pattern. There are no erasures, insertions or deletions. A feedback bit from Bob costs one transmitted bit and is subject to the same corruption rule as a bit sent by Alice. Local computation, storage and protocol description size are unrestricted.

A fraction \(\rho\) is achievable at constant rate if there exist a real \(K>0\), an integer \(n_0\ge1\), and a family of such protocols, one for every \(n\ge n_0\), with
\[
T_n\le Kn
\]
and the stated exact correctness against \(\lfloor\rho T_n\rfloor\) flips. The rate is \(n/T_n\), including communication in both directions. The constants and protocol family may depend on \(\rho\), but \(K\) does not depend on \(n\). No efficient or uniform algorithm for producing the family is required. There is no fixed bound on the number of alternations between the parties.

The supremum exists: zero is achievable by transmitting the message directly, and the defining set is contained in \([0,1]\). It is a supremum, so a protocol family attaining exactly \(\rho_*\) is not required. The target is an explicit real number \(a\) with \(|a-\rho_*|\le1/100\), or an enclosing interval \([\ell,u]\) of width at most \(1/50\). Its midpoint then meets the requested absolute accuracy. An unambiguous mathematical expression is acceptable; no running-time bound for finding or evaluating it is imposed.

A lower certificate must establish that the supremum is at least \(\ell\), by an achievable fraction or rigorously approaching achievable fractions. An upper certificate must bound all constant-rate protocol families in the model. Allowing \(T_n/n\) to grow without bound, making Bob's feedback noiseless or free, allowing an adaptive speaking order, or simulating an arbitrary two-input communication task would change the quantity.''',
 answer_criterion='Supply a concrete real approximation and a complete mathematically correct Lean-checked proof of absolute error at most 1/100, or a Lean-checked interval containing ρ_* with width at most 1/50. The bounds must apply to the full fixed-schedule, deterministic, constant-rate message-transfer model with one corruption budget for both directions. A single improved lower or upper bound need not meet the criterion.',
 why='Interaction already allows binary message transmission beyond the classical one-way quarter-error threshold. Locating its ultimate constant-rate resilience measures the benefit of a dialogue when the feedback itself is costly and corruptible.',
 importance=dict(score=79,method='editorial',reason='The threshold isolates a fundamental benefit and limitation of interaction in adversarial binary communication, with a precise distinction from noiseless feedback and general protocol simulation.'),
 source_formulation=dict(text='The source asks for maximal noise tolerance at constant rate or even zero rate. This card selects constant rate, retaining the source’s deterministic fixed-schedule message-transfer model and applying the catalogue’s numerical accuracy criterion. The optional rate choice received no reply; the previously recommended constant-rate branch was announced and applied as an editorial decision.',caption='Efremenko–Kol–Saxena–Zhang, FOCS 2022, open question p.1; model §III pp.6–7; Theorem V.1 p.9.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Binary Codes with Resilience Beyond 1/4 via Interaction','Klim Efremenko; Gillat Kol; Raghuvansh R. Saxena; Zhijun Zhang',2022,'https://doi.org/10.1109/FOCS54457.2022.00008','Open question p.1; §III.B protocol, corruption and MsgTrans definitions pp.6–7; Theorem V.1 p.9'),
 ref('upper','Interactive Error Correcting Codes: New Constructions and Impossibility Bounds','Meghal Gupta; Rachel Yun Zhang',2023,'https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2023.32','Theorem 3 p.32:3; Definitions 4–5 p.32:4; §5 pp.32:9–32:12 gives the bit-flip impossibility bound'),
 ref('feedback','Round-Vs-Resilience Tradeoffs for Binary Feedback Channels','Mark Braverman; Klim Efremenko; Gillat Kol; Raghuvansh R. Saxena; Zhijun Zhang',2025,'https://doi.org/10.4230/LIPIcs.ITCS.2025.22','Discussion of two-way coding and noiseless-feedback distinctions pp.22:6–22:7; its quoted 2/7 bound is superseded by the 2023 result cited here'),
 ],
 context_blocks=[
 block('Theorem V.1 supplies deterministic protocols of length Kn tolerating a fraction 1/4 + 10⁻⁵ of bit flips. This shows that interaction improves the attainable resilience even when the communication rate stays bounded away from zero.'),
 block('The source fixes the order of speaking and counts errors over both parties’ transcripts. Its task is transmission of Alice’s message to Bob, not simulation of every two-input protocol.'),
 block('The 2023 Theorem 3 rules out resilience above 13/47 for sufficiently long messages. It improves the earlier upper bound 2/7 and applies without needing a constant-rate restriction. Hence it also bounds the selected supremum.','upper'),
 block('The verified interval [1/4 + 10⁻⁵, 13/47] has width greater than 1/50, so these two results alone do not meet the selected absolute-error criterion. A precise threshold or a narrower certified interval would.','upper'),
 block('Noiseless feedback has a different threshold and cost model. The 2025 feedback paper explicitly distinguishes it from two-way codes with noisy feedback; the older upper bound recalled in its discussion is not used as the best available bound here.','feedback'),
 ],
 progress=[progress('2022','A constant-rate deterministic construction exceeds one-quarter bit-flip resilience.'),progress('2023','The universal upper bound is improved from 2/7 to 13/47.','upper'),progress('2025','Work on noiseless-feedback rounds emphasizes the distinction from the two-way noisy-feedback model.','feedback')],
),[
 'Selected the announced constant-rate branch and kept its full numerical threshold rather than changing it to a fixed barrier question.',
 'Defined both local transcripts, predetermined speakers, exact recovery, nonuniform protocol families and one shared adversarial bit-flip budget.',
 'Checked the 2022 positive theorem and found the sharper 2023 upper bound, avoiding the outdated 2/7 value repeated in later context.',
 'Explained the supremum and two-sided 1/100 numerical certificate without requiring endpoint attainment.',
 'Individually assessed importance and required a complete Lean-checked numerical proof.',
],[
 'Read FOCS 2022 §III.B and Theorem V.1, including the linear communication length and deterministic model.',
 'Downloaded RANDOM 2023 and read Theorem 3, fixed-schedule Definitions 4–5 and the §5 impossibility setup.',
 'Read ITCS 2025 pp.22:6–22:7 for the noiseless-feedback versus noisy-two-way distinction.',
 'Bounded later searches through 18 September 2026 found no matching tighter certificate; a 2025 separate-budget result was not confused with the shared-budget model.',
], 'The checked sources give 1/4 + 10⁻⁵ ≤ ρ_* ≤ 13/47. This interval is wider than 1/50 and therefore does not yet certify the requested 1/100 approximation. No resolution matching the selected constant-rate deterministic fixed-schedule model was found in the bounded review through 18 September 2026. Results for erasures, free noiseless feedback, separate corruption budgets or general interactive-protocol simulation concern different targets.',summary=[
 'Alice sends an arbitrary binary message to Bob, and Bob may send costly, corruptible feedback bits.',
 'The speaking order is fixed, and an adversary may flip a bounded fraction of all transmitted bits in both directions.',
 'The target is the largest tolerable fraction with linear total communication, to certified absolute error 1/100.',
 'A construction tolerates slightly more than one quarter, while the checked upper bound is 13/47.',
 'Those bounds still leave too wide an interval, and noiseless-feedback results do not settle this model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
