"""Match the historical optimal-resilience binary BA target to PODC 2026."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-2753'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the deterministic synchronous binary strong-BA target from the original §7 and conclusion, at n=2t+1 and O(n(f+1)) words for every actual fault count.',
 'Separated adaptation of communication cost to f from tolerance of an adversary choosing corruptions adaptively; both are present in the source model.',
 'Defined strong unanimity, reliable authenticated channels, trusted ideal threshold-signature setup, word cost and post-decision messages.',
 'Matched the target to published PODC 2026 Theorem 3.1, with the f=0 convention restored from the paper’s explicit footnote.',
 'Read the full-version synchronous retrieval and view/fallback proofs rather than inferring resolution from the abstract or from the large-scale disperser result.',
 'Distinguished the weaker-resilience 2023 result and stronger cryptographic primitives in the general multi-valued 2024 construction.',
 'Individually assessed the importance and preserved the historical complete record in the resolved archive.',
]
sources=[
 'Read Cohen–Keidar–Spiegelman OPODIS 2022 §§1–3, Table 1, §7 and conclusion: binary strong unanimity, adaptive adversary, n=2t+1, ideal threshold signatures, O(n) when f=0 and O(n^2) otherwise.',
 'Checked Civit et al. arXiv:2308.03524 abstract: n=(2+Omega(1))t+1 leaves a fixed resilience gap.',
 'Read DARE to agree, IACR ePrint 2024/403, introduction/Table 1 and cryptographic definitions: its general strong multi-valued instantiation uses multiverse threshold signatures; it was not silently treated as the same primitive interface.',
 'Read published Constantinescu–Dufay–Paramonov–Wattenhofer PODC 2026 Theorem 3.1, §4 model, §9.1, and the explicit convention replacing f by f+1 at f=0. Publication DOI 10.1145/3796701.3815964 and official proceedings listing were checked.',
 'Read arXiv:2505.19989v3, 17 June 2026, §10.1 with Lemmas 10.1–10.3 and Theorem 10.4, Appendix B.1 pseudocode, B.2 Lemmas B.1–B.11, B.3 SyncBA and Theorems B.13–B.14, and B.4 fallback analysis.',
 'Checked certificate intersection, preservation of strong validity, retrieval progress after f+1 honest leaders, O(n) communication per view, bounded post-decision replies and the O(n^2) fallback charged only when f=Omega(n). The cited Momose–Ren fallback is a published dependency, not independently re-proved here; this is not a Lean formalization.',
]
status=('Resolved positively by published PODC 2026 Theorem 3.1: deterministic synchronous binary strong Byzantine agreement with t<n/2 and O(n(f+1)) words, using the standard ideal signature/threshold-signature setting. '
 'At n=2t+1 this meets the historical question. The extra adaptive round bound is stronger than required. '
 'The synchronous proof and its full-version appendices were reviewed; the earlier quadratic fallback theorem is a cited dependency. '
 'The complete historical card is archived, not retained as a current open problem.')
complete(identifier,dict(
 status='resolved',title='Fault-adaptive Byzantine agreement at optimal resilience',
 criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a uniform deterministic synchronous protocol and an absolute constant \(C>0\) such that, for every integer \(t\ge0\), with \(n=2t+1\) named processes and trusted ideal signature setup as defined below, the protocol solves binary strong Byzantine agreement against every adaptive adversary corrupting at most \(t\) processes, and every execution with \(f\le t\) actual corruptions has total communication at most
\[
C\,n(f+1)
\]
words sent by processes while they follow the protocol? The protocol receives \(n,t\), identities and the setup, but not the eventual value of \(f\). The bound includes communication after a process decides. No bound on the number of rounds is imposed beyond eventual decision by every never-corrupted process.''',
 definitions=r'''Processes have distinct identities \(1,\ldots,n\), know the membership and threshold \(t\), and each starts with one input bit. Every pair has a reliable authenticated channel. Time is divided into synchronous rounds known to all processes. A message sent by a noncorrupted process to another noncorrupted process is delivered by the end of that round. A send to each of several recipients is charged separately; there is no free broadcast primitive.

An adversary may choose which processes to corrupt as the execution develops, after observing communication, with at most \(t\) distinct processes ever corrupted. Corruption is permanent and reveals the process’s state and signing capability. Corrupted processes may send inconsistent messages, omit messages, or stop. They cannot impersonate an uncorrupted sender or create signatures forbidden by the ideal signing interface. Honest messages already sent retain the stated reliable-delivery guarantee. Let \(f\) be the total number of distinct processes corrupted during the execution. Correct processes for agreement, termination and validity are those never corrupted.

Each correct process must eventually decide one bit, once and irrevocably. Agreement requires that all such decisions are equal. Strong unanimity requires that, if every correct process’s original input is the same bit \(b\), their decision is \(b\), regardless of the inputs and messages of corrupted processes. With mixed correct inputs, either bit is permitted.

The trusted setup occurs before the measured execution and supplies public verification information and private signing capabilities. Ordinary signatures are publicly verifiable and can be produced only by the named signer; once produced, they may be copied and forwarded. For any publicly specified threshold \(q\in\{1,\ldots,n\}\), an ideal threshold-signature instance permits each process to create a share on a specified message. Shares from at least \(q\) distinct processes on that same message can be combined locally into one constant-size publicly verifiable certificate. A certificate can be created only from the required distinct shares, or copied if already available. Corrupted signers can provide their own shares on arbitrary messages. This idealization rules out forgery exactly; it does not assert unconditional security of a physical cryptographic implementation. Setup and local signature operations incur no communication charge beyond transmitting their inputs or outputs.

A word carries a constant number of input bits, ordinary signatures, signature shares or threshold certificates, together with \(O(\log(n+2))\) ordinary control bits. These constants are fixed independently of \(n,t,f\). An arbitrary list of signers, values or certificates is charged for all its contents; compression into one threshold certificate is allowed only through the stated interface. Every nonempty message costs at least one word. Local computation is unrestricted. A protocol is uniform if a single finite algorithm specifies each process’s behavior from its identity, input, parameters, setup and local history. It uses no random choices outside the ideal setup.

The communication measure counts every word sent while a process is uncorrupted, including words sent by a process that is later corrupted, and all permitted protocol traffic after decisions. Arbitrary traffic sent after corruption is excluded. The bound holds in every allowed execution, not merely in expectation or in the worst case \(f=t\). The case \(t=0,n=1\) is included.''',
 answer_criterion=r'''A positive benchmark answer requires a complete Lean-checked protocol, correctness proof and uniform \(C n(f+1)\) word bound in the specified ideal model. A negative answer would require a Lean-checked impossibility proof for this quantified assertion. The target is binary existence with an asymptotic resource guarantee, so no numerical \(1/100\) tolerance applies. Published mathematics now gives the positive answer; this archived record does not claim that the protocol has already been formalized in Lean.''',
 source_formulation=dict(text='The source asks whether its optimal-resilience synchronous binary strong-agreement protocol, which is cheap only in fault-free runs, can attain O(n(f+1)) words for every actual number f of faults.',
 caption='Paraphrase of §7 and the conclusion; the binary value domain follows the protocol and open question in §7.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=78,method='editorial',
 reason='The problem asks whether optimal Byzantine resilience can coexist with communication proportional to actual faults, a central efficiency distinction for authenticated consensus.',
 basis='Individual review of strong validity, honest-majority resilience, actual-fault adaptivity and the subsequent matching published protocol.'),
 why='Worst-case quadratic communication can obscure much cheaper runs with few failures. This question asks for such savings all the way to the honest-majority resilience threshold, while preserving agreement and validity against adversarial behavior.',
 references=[
 ref('primary','Make Every Word Count: Adaptive Byzantine Agreement with Fewer Words',
 'Shir Cohen; Idit Keidar; Alexander Spiegelman',2022,'https://doi.org/10.4230/LIPIcs.OPODIS.2022.18',
 'OPODIS 2022, pp. 18:1–18:21; §§2–3, Table 1, §7 and §8 conclusion'),
 ref('gap','Strong Byzantine Agreement with Adaptive Word Complexity',
 'Pierre Civit; Seth Gilbert; Rachid Guerraoui; Jovan Komatovic; Manuel Vidigueira',2023,
 'https://arxiv.org/abs/2308.03524','Original preprint, 7 August 2023; resilience stated in abstract'),
 ref('dare','DARE to agree: Byzantine Agreement with Optimal Resilience and Adaptive Communication',
 'Pierre Civit; Muhammad Ayaz Dzulfikar; Seth Gilbert; Rachid Guerraoui; Jovan Komatovic; Manuel Vidigueira',2024,
 'https://eprint.iacr.org/2024/403','PODC 2024, DOI 10.1145/3662158.3662792; full version Table 1 and §3 cryptographic primitives'),
 ref('resolved','From Few to Many Faults: Optimal Adaptive Byzantine Agreement',
 'Andrei Constantinescu; Marc Dufay; Anton Paramonov; Roger Wattenhofer',2026,
 'https://doi.org/10.1145/3796701.3815964','PODC 2026, 6–10 July 2026; Theorem 3.1, §4 and §9.1; f+1 convention in introduction footnote 2'),
 ref('full','From Few to Many Faults: Optimal Adaptive Byzantine Agreement — full version',
 'Andrei Constantinescu; Marc Dufay; Anton Paramonov; Roger Wattenhofer',2026,
 'https://arxiv.org/abs/2505.19989v3','Version 3, 17 June 2026; §10.1, Theorem 3.1 and Appendix B.1–B.4, especially Theorems B.13–B.14'),
 ],
 context_blocks=[
 block('Strong unanimity requires a common input of all correct processes to be preserved even when faulty processes submit conflicting values. This is stronger than requiring unanimity only when there are no faults. The source uses binary values and the optimal honest-majority threshold.'),
 block('The word measure matters because a threshold certificate can encode many endorsements in constant space. A lower bound on the number of individual signatures does not automatically become the same lower bound on transmitted words. The trusted setup and certificate interface are part of the model.'),
 block(r'The 2022 source achieves \(O(n(f+1))\) words for Byzantine broadcast and a weaker agreement variant. For binary strong agreement it gives \(O(n)\) words when \(f=0\), with a quadratic fallback in other cases, and leaves full adaptivity open.'),
 block(r'The 2023 STRONG result attains adaptive word complexity with \(n=(2+\Omega(1))t+1\). That fixed resilience gap prevents it alone from settling the exact \(n=2t+1\) question.','gap'),
 block('The 2024 DARE work reaches the honest-majority threshold for general strong multi-valued agreement with adaptive word complexity. Its general strong-validity implementation uses multiverse threshold signatures; the later binary theorem provides a direct match to the standard threshold-signature interface.','dare'),
 block(r'Published PODC 2026 Theorem 3.1 gives the requested deterministic synchronous binary protocol with \(O(n(f+1))\) words and also \(O(f+1)\) decision rounds. The result applies at \(n=2t+1\), includes fault-free runs, and counts bounded protocol traffic after decisions. The separate large-system bounds involving dispersers are not needed for this resolution.','resolved'),
 ],
 progress=[
 progress('2022','The source leaves full actual-fault adaptivity open at optimal resilience for binary strong Byzantine agreement.'),
 progress('2023-08-07','STRONG obtains adaptive communication with a fixed gap from the optimal resilience threshold.','gap'),
 progress('2024','DARE gives optimal-resilience adaptive strong multi-valued agreement with the cryptographic primitives identified in its model.','dare'),
 progress('2026-07-06','The PODC 2026 theorem supplies a deterministic synchronous binary protocol matching the historical target, with an additional adaptive round guarantee.','resolved'),
 progress('2026-09-16','Individual source review checks the synchronous theorem and full-version proof dependencies and archives the resolved historical question.','full'),
 ],
),notes,sources,status,summary=[
 'The historical question asks for binary strong Byzantine agreement with the optimal honest-majority resilience threshold.',
 'Communication must use at most a constant times n(f+1) words when only f processes are actually corrupted.',
 'The synchronous model includes authenticated channels, adaptive corruptions and trusted ideal threshold signatures.',
 'A published PODC 2026 theorem provides the required protocol and also an adaptive bound on decision rounds.',
 'The reviewed historical card is therefore preserved in the resolved archive rather than listed as an open problem.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],
archive_reason='Resolved by PODC 2026 Theorem 3.1: deterministic synchronous binary strong Byzantine agreement at t<n/2 with O(n(f+1)) words; matched to the original ideal-threshold-signature model and reviewed against the full-version synchronous proofs.')
