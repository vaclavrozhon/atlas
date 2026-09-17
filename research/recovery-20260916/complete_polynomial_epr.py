"""Complete the selected polynomial-EPR quantum communication target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-4991'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user-selected polynomial bound on the number of shared EPR pairs, with constant-factor communication overhead and a fixed constant increase in error.',
 'Preserved the source’s Boolean-function scope, including arbitrary promises, rather than general multi-output relations, channel simulation or nonlocal games.',
 'Specified arbitrary finite-dimensional input-independent prior states, unrestricted local quantum operations, charged two-way qubit communication and one designated Boolean output.',
 'Made the universal exponent and constants independent of the function, original protocol and original entanglement; no effective compiler or preservation of the original message pattern is required.',
 'Fixed initial error at most one quarter and final error at most one third to give a precise constant-loss convention, without an error-parameter-dependent entanglement bound.',
 'Separated the 2019 EPR-type universality theorem from a bound on EPR count, and checked why later relation, restricted-message and noisy-resource separations do not settle this target.',
 'Assessed importance individually at 83 and required a complete Lean-checked proof or refutation in the specified unrestricted interactive quantum model.',
]
sources=[
 'Read Coudron–Harrow, CCC 2019 Article 20, DOI 10.4230/LIPIcs.CCC.2019.20: abstract, §1.1 pp. 20:2–20:3, Theorem 1 and the subsequent distinction between entanglement type and amount; model discussion and the finite-dimensional theorem restatements. Theorem 1 allows arbitrary partial or total Boolean functions and O(Q/epsilon+log(1/epsilon)/epsilon) qubits, but does not bound the number of EPR pairs polynomially in input length.',
 'Read Arunachalam–Girish, Trade-Offs Between Entanglement and Communication, CCC 2023 Article 25, DOI 10.4230/LIPIcs.CCC.2023.25, published 10 July 2023: abstract and §1.1 Results 1–2 pp. 25:2–25:4. The lower-bound models are two-way classical, quantum simultaneous messages, and one-way classical communication; these do not exclude general two-way quantum replacements with polynomially many EPR pairs.',
 'Read Hasegawa–Le Gall–Modanese, Maximum Separation of Quantum Communication Complexity With and Without Shared Entanglement, arXiv:2505.16457v3, revised 17 April 2026: abstract, Theorems 1–3 and Table 2, pp. 1–4. Its zero-versus-linear quantum communication separation is for multi-output relations, with a linear EPR resource; Theorem 2 explicitly distinguishes function problems. Neither the output type nor the excluded entanglement regime matches a refutation of this polynomial-bound question.',
 'Read Kundu–Lalonde, Non-local games and communication complexity with noisy entanglement, arXiv:2609.05122v1, 4 September 2026: abstract and introductory communication results. Its resources are noisy copies, with relational noisy-versus-noiseless separations and a polynomial noisy-resource requirement for Equality. This card permits perfect EPR pairs, so these are recorded as a different model.',
 f'Bounded primary-source checks through {DATE} found no proof or refutation of the selected universal polynomial-EPR statement. Full proofs of the cited separation theorems were not independently certified.',
]
status='The checked source leaves reducing the amount of prior entanglement open while proving that EPR pairs suffice as its type, with constant communication overhead at fixed error. The 2023 restricted-model tradeoffs, April 2026 relational separation and September 2026 noisy-resource results do not settle the selected polynomial bound for unrestricted two-way quantum protocols computing Boolean functions. This is a bounded later-work check, not a certification of every cited proof.'
complete(identifier,dict(
 title='Polynomially many EPR pairs for bounded-error Boolean communication',
 criterion='resources',question_type='yes_no',year=2026,is_new=False,
 formal=r'''Do there exist universal constants \(C\ge1\), \(A\ge1\) and an integer \(d\ge1\) with the following property? For every \(n\ge1\), every promise set \(D\subseteq\{0,1\}^n\times\{0,1\}^n\), every Boolean function \(f:D\to\{0,1\}\), and every two-party quantum protocol computing \(f\) with worst-case error at most \(1/4\) using at most \(Q\ge1\) communicated qubits and arbitrary prior entanglement, there exists a protocol computing \(f\) with error at most \(1/3\), using at most \(CQ\) communicated qubits and at most
\[
 \lfloor A(n+1)^d\rfloor
\]
shared EPR pairs initially? Both protocols may use arbitrary two-way interaction. The replacement may change all local operations and the message pattern; it need not reproduce the original shared state or its internal evolution.''',
 definitions=r'''Alice receives only \(x\in\{0,1\}^n\), Bob receives only \(y\in\{0,1\}^n\), and the pair is promised to belong to \(D\). Both know the function, promise and protocol. Bob outputs one classical bit, which must equal \(f(x,y)\) with the stated probability on each promised pair. Total functions are the case \(D=\{0,1\}^n\times\{0,1\}^n\). Every promised input has one correct bit; the task is not to generate any of several jointly valid output pairs. There is no accuracy condition outside the promise.

A protocol uses finite-dimensional quantum registers divided between Alice and Bob. A state is a positive semidefinite complex matrix of trace one. The original shared resource may be any finite-dimensional bipartite state, fixed independently of the actual inputs. Its dimension may depend on \(n,f\) and the protocol without an a priori upper bound. Pure shared states suffice as a convention: a mixed state can be purified by assigning its purifying register to one party, with no initial communication charge. Private ancillas and private randomness are allowed, and local storage is unrestricted.

Local quantum operations act only on the acting party’s registers and may depend on its own input and its available classical outcomes. They are arbitrary finite-dimensional quantum channels or measurements, with no computational gate-count restriction. Concretely a channel is a map \(\rho\mapsto\sum_jK_j\rho K_j^\dagger\) with \(\sum_jK_j^\dagger K_j=I\); a measurement may retain the outcome \(j\), which occurs with probability \(\operatorname{Tr}(K_j\rho K_j^\dagger)\). The matrices may have arbitrary complex entries. Input-independent protocol design is nonuniform in the function and input length; no efficient or effective compilation from the old protocol to the new one is required.

Sending a register of \(q\) qubits costs \(q\), summed in both directions over the whole execution. One transmitted classical bit also costs one, as an orthogonal qubit encoding. Messages, their lengths and whose turn it is must follow the prescribed protocol or be communicated through charged registers; timing and silence are not extra channels. There is no restriction to one message, simultaneous messages or a fixed number of rounds. The protocol has finite local dimensions and finitely many rounds, with the communication bound holding on every branch of its measurement outcomes. All communication used to prepare an auxiliary resource after the initial state is supplied counts toward this bound. Unlimited classical communication is not free.

An EPR pair is the pure two-qubit state
\[
 |\Phi^+\rangle=(|0\rangle_A|0\rangle_B+|1\rangle_A|1\rangle_B)/\sqrt2.
\]
The replacement begins with exactly a tensor product of at most \(\lfloor A(n+1)^d\rfloor\) such pairs, together with local product ancillas; it has no other shared quantum state or separate free shared random string. The parties may measure pairs to obtain shared random bits. The bound counts pairs, or equivalently initially entangled qubits held by either party, rather than the dimension of the shared Hilbert space. With \(e\) pairs, each entangled local register has dimension \(2^e\), so the selected polynomial-qubit bound permits an exponential Hilbert-space dimension. Entanglement need not be returned at the end and may be consumed.

The constants \(C,A,d\) are universal, independent of the function, promise, input length, original protocol, communication cost and original state dimension. The replacement protocol itself may depend on all of those except the private inputs. The polynomial bound concerns initial entanglement; entanglement subsequently generated by charged messages is allowed. The positive-cost convention \(Q\ge1\) avoids an irrelevant zero-cost normalization case. The chosen errors \(1/4\) and \(1/3\) specify a constant increase below one half; they do not ask for an arbitrarily accurate simulation or for a bound uniform in an additional accuracy parameter.

Only the computed Boolean answer and its worst-case error are to be preserved. In particular, the new protocol need not approximate the old transcript distribution, the parties’ final quantum states, their individual measurements or the original entangled state. Bounds that forbid changing those objects are different statements.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the universal polynomial-EPR simulation statement, including its communication, entanglement and per-input error bounds, or a complete Lean-checked refutation. A refutation must rule out every choice of universal constants and polynomial exponent: for each candidate bound, there must be a Boolean function with an allowed original protocol but no allowed replacement meeting both budgets and the final error.

A lower bound for keeping the old operations fixed, for classical communication alone, for one-way or simultaneous-message protocols, for noisy entanglement, or for a relation with multiple valid outputs is insufficient. A lower bound excluding logarithmic or sublinear entanglement alone is also insufficient to rule out every polynomial amount. Numerical tolerance does not weaken these asymptotic resource and probability requirements.''',
 source_formulation=dict(text='The source asks whether a large shared entangled state can be replaced by a smaller one if the communication protocol may also change. Its theorem shows that maximally entangled resources suffice as a type, while leaving the amount unresolved. The user selected a polynomial number of EPR pairs in the input length, constant communication overhead and a fixed constant error increase.',caption='Paraphrase of Coudron–Harrow, CCC 2019 §1.1 pp. 20:2–20:3 and Theorem 1; polynomial-EPR target selected by the user on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=83,method='editorial',reason='A universal polynomial entanglement bound would control a resource currently left free in a central quantum communication model; a failure would show that even Boolean computation can require more shared quantum memory at essentially optimal communication.',basis='Individual assessment of the unrestricted interactive Boolean-function target, distinguishing prior-entanglement amount from its type and from relation or noise-model separations.'),
 why='Communication complexity counts the messages but usually gives the parties their shared entangled state for free. This question asks whether that hidden resource can always be bounded polynomially while keeping almost the same communication cost.',
 references=[
 ref('primary','Universality of EPR Pairs in Entanglement-Assisted Communication Complexity, and the Communication Cost of State Conversion','Matthew Coudron; Aram W. Harrow',2019,'https://doi.org/10.4230/LIPIcs.CCC.2019.20','CCC 2019, LIPIcs 137, Article 20; §1.1 pp. 20:2–20:3 and Theorem 1; finite-dimensional model and subsequent distinction between EPR type and count'),
 ref('tradeoffs','Trade-Offs Between Entanglement and Communication','Srinivasan Arunachalam; Uma Girish',2023,'https://doi.org/10.4230/LIPIcs.CCC.2023.25','CCC 2023, LIPIcs 264, Article 25, published 10 July 2023; §1.1 Results 1–2, pp. 25:2–25:4; lower-bound communication models explicitly distinguished'),
 ref('relations','Maximum Separation of Quantum Communication Complexity With and Without Shared Entanglement','Atsuya Hasegawa; François Le Gall; Augusto Modanese',2026,'https://arxiv.org/abs/2505.16457v3','Version 3, 17 April 2026, first submitted 22 May 2025; Theorems 1–3 and Table 2, pp. 2–4; relation-versus-function distinction'),
 ref('noise','Non-local games and communication complexity with noisy entanglement','Srijita Kundu; Olivier Lalonde',2026,'https://arxiv.org/abs/2609.05122v1','Version 1, 4 September 2026; abstract and introductory communication results, with noisy EPR resources rather than the perfect pairs allowed here'),
 ],
 context_blocks=[
 block('The 2019 theorem allows arbitrary prior entanglement to be replaced by EPR pairs at a constant-factor communication cost for fixed error. Its guarantee does not limit how many such pairs are supplied, which is the extra requirement here.'),
 block('The 2023 partial-function separations impose classical communication or simultaneous-message restrictions on the replacement model. They demonstrate sensitivity to entanglement in those settings but do not rule out a fully interactive quantum replacement with a universal polynomial budget.','tradeoffs'),
 block('The revised 2026 separation uses relation problems with several valid joint outputs and distinguishes linear shared entanglement from sublinear or absent entanglement. It explicitly treats zero-communication function problems separately; this does not settle a polynomial entanglement bound for Boolean functions.','relations'),
 block('The September 2026 paper studies noisy shared resources. Even a polynomial lower bound on the number of noisy copies for a function does not refute the present allowance of polynomially many perfect EPR pairs.','noise'),
 ],
 progress=[
 progress('2019','The CCC theorem establishes universality of EPR pairs as a resource type for partial and total Boolean communication, while leaving their required amount open.'),
 progress('2023-07-10','CCC publishes entanglement-versus-communication separations for specified classical and simultaneous-message models.','tradeoffs'),
 progress('2026-04-17','The revised preprint gives a maximal relation-problem separation between entangled and unentangled two-way quantum communication.','relations'),
 progress('2026-09-04','A preprint studies noisy-entanglement communication and nonlocal games, a distinct resource model.','noise'),
 ],
),notes,sources,status,summary=[
 'The target is to replace arbitrary prior entanglement in a Boolean quantum communication protocol by polynomially many perfect EPR pairs.',
 'One universal polynomial in the input length must work for all functions and promises, with only a constant factor more qubit communication.',
 'The selected constant-error convention allows error to increase from one quarter to one third on every promised input.',
 'Both parties may change the entire protocol and interact freely, while local computation and storage remain unbounded.',
 'Known EPR-type universality and later restricted-model separations do not settle this amount bound; a complete Lean-checked proof or refutation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
