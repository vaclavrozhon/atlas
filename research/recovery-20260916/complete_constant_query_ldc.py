"""Complete the binary constant-query, polynomial-blocklength LDC target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-1020';claim=read_claims(ROOT)[identifier]
notes=[
 'Read the exact textbook Open Problem 7.53 and its local-decoder Definition 7.35; retained existence rather than adding efficient explicit construction.',
 'Quantified one fixed positive corruption fraction, one constant query bound and one polynomial blocklength bound before all message lengths.',
 'Specified binary input and output alphabets, arbitrary nonlinear encodings, adaptive private-randomness decision trees and a per-message/per-corruption/per-index success guarantee.',
 'Excluded free access to the received word, shared secret randomness, restricted corruption channels, relaxed erasures, list outputs and amortized block queries.',
 'Checked general odd-query lower bounds, the August 2026 restricted matching-vector bounds, and the new 14 September amortized relaxed construction without conflating their models.',
 'Preserved importance 92, updated its provisional explanation, removed legacy drafting language and required complete Lean checking of either direction.',
]
sources=[
 'Read Vadhan, Pseudorandomness, December 2012 published author PDF: Definition 7.35 printed p. 241, Theorem 7.51 and surrounding query discussion pp. 251–252, Open Problem 7.53 printed p. 252 (PDF page 255). The source asks for binary codes with constant queries, constant positive decoding distance and polynomial blocklength; it does not demand an explicit construction in that question.',
 'Read Basu–Hsieh–Kothari–Lin, arXiv:2411.14361v1, 21 November 2024, Introduction and Theorem 1.1 pp. 1–2; checked FOCS 2025 author and conference entries. The stated general lower bounds cover possibly nonlinear binary codes but remain polynomial at fixed query count. The paper also distinguishes stronger local-correction lower bounds.',
 'Read Aggarwal–Obremski, ECCC TR26-141 Revision 2, 11 August 2026, primary abstract and revision metadata. The superpolynomial blocklength consequence is for three-query matching-vector codes over a fixed modulus, not for every constant-query binary code. Full proof not independently audited.',
 'Read Saraogi, arXiv:2608.27859v1, 28 August 2026, primary abstract: the new upper bound is on three-restricted matching-vector families with a restricted modulus range. It does not supply a general LDC impossibility theorem.',
 'Read Grigorescu–Kumar–Manohar–Mon, arXiv:2511.02633 primary abstract and STOC 2026 official accepted-paper entry. The results compare linear relaxed and full decodability at specific query counts; allowing the decoder to abort remains a different requirement.',
 'Read Yankovitz, ECCC TR25-168 Revision 1, 2 April 2026, primary abstract: constant information rate with polylogarithmic queries uses a growing output alphabet, not constant binary bit queries.',
 'Read Blocki–Zhang, arXiv:2609.16332v1, 14 September 2026, primary abstract: the new constant-rate, constant-locality result combines amortized block decoding with relaxed failure outputs. Neither relaxation is allowed in this card. Full proof not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified polynomial-blocklength constant-query binary LDC family or unconditional negation. Related TCS-6609 fixes constant rate and permits logarithmically many queries; TCS-6739 concerns the relaxed-versus-full distinction.',
]
complete(identifier,dict(
 title='Polynomial-length constant-query locally decodable codes',criterion='construction',question_type='yes_no',status='source_open',
 formal=r'''Do there exist an integer \(q\ge1\), real constants \(C\ge1\), \(d\ge1\) and \(0<\delta<1/2\), such that for every integer message length \(k\ge1\) there are an integer \(n\) with \(k\le n\le Ck^d\), an injective encoding
\[
 E_k:\{0,1\}^k\longrightarrow\{0,1\}^n,
\]
and randomized local decoders \(D_{k,i}\) for every \(i\in\{1,\ldots,k\}\), satisfying
\[
 \Pr[D_{k,i}^{\,z}=x_i]\ge\frac23
\]
for every message \(x\in\{0,1\}^k\) and every received word \(z\in\{0,1\}^n\) differing from \(E_k(x)\) in fewer than \(\delta n\) coordinates, while each decoder reads at most \(q\) bits of \(z\) on every execution?''',
 definitions=r'''Here \(k\) counts message bits and \(n\) counts stored codeword bits. The Hamming distance between two length-\(n\) words is the number of coordinates where they differ. The allowed corruptions are precisely the words at Hamming distance strictly less than \(\delta n\), as in the source definition. In particular the uncorrupted codeword is included. The constants \(q,C,d,\delta\) are fixed before \(k\); they do not depend on the message, requested coordinate, corruption or code length. The blocklength \(n=n(k)\), encoding and decoder descriptions may depend on \(k\). Polynomial blocklength does not require constant rate or a polynomial of any prescribed degree.

This is an existence question in the classical randomized bit-query model. For fixed \(k,n,i,E_k\), a deterministic query procedure is a finite binary decision tree of depth at most \(q\). Each internal node is labelled by a coordinate \(j\in\{1,\ldots,n\}\); the oracle returns the single bit \(z_j\), and this chooses the next child. Each leaf is labelled by the output bit zero or one. A randomized decoder is a probability distribution over such trees, fixed independently of \(x\) and \(z\). This describes adaptive queries: later coordinates may depend on earlier answers. Repeated queries count toward the same bound, and early stopping is allowed. The tree distribution may depend on the requested index and the code, but the only information it learns about the actual received word is through the queried bits.

The probability in the statement is solely over that decoder's private randomness. The guarantee holds separately for every triple \((x,z,i)\); a single random choice need not decode all message coordinates at once. Corruptions may depend on the full encoding and message and are computationally unrestricted, but \(z\) is fixed before the decoder draws its randomness. There is no secret key or randomness shared with the channel. The output is one bit: an erasure symbol, a candidate list or success only averaged over requested indices does not meet the definition.

Encoding linearity, systematic form and local correction of every codeword coordinate are not required. There is no bound on encoding time, decoder computation between queries or description length, and no additional requirement that one efficient uniform program construct the family. The finite decision-tree formulation makes the query resource explicit without granting access to any unqueried received bits. Codes must be available for every message length under one set of constants; a finite catalogue or a query bound growing with \(k\) does not suffice.''',
 answer_criterion=r'''Give a complete Lean-checked proof of this existence statement, specifying or proving the existence of the encodings and decoders and verifying the common constants, polynomial blocklength, worst-case query bound and all corruption/success quantifiers; or give a complete Lean-checked proof of its logical negation.

An efficient explicit construction is sufficient but is not required. A negative proof must rule out every fixed query count and every polynomial degree, including nonlinear codes and the unrestricted decoder model. A lower bound only for two or three queries, only for matching-vector constructions, or only for locally correctable codes does not establish that negation. Relaxed, approximate, list or amortized decoding and growing-alphabet symbol queries require a proved conversion meeting the exact binary single-bit requirements. No approximation tolerance applies to the yes/no target.''',
 source_formulation=dict(text='Are there binary locally decodable codes with a constant number of queries, a fixed positive decoding distance and blocklength polynomial in the message length?',caption='Paraphrase of Vadhan, Open Problem 7.53, printed p. 252 / PDF page 255; the per-coordinate success probability comes from Definition 7.35, printed p. 241.',citation='primary',format='editorial_paraphrase'),
 why='Determine whether a constant number of bit probes can recover any requested message bit despite a constant fraction of adversarial corruptions using only polynomial storage. This is a central locality-versus-redundancy question with connections to private information retrieval and complexity theory.',
 references=[
 ref('primary','Pseudorandomness','Salil P. Vadhan',2012,'https://people.seas.harvard.edu/~salil/pseudorandomness/pseudorandomness-published-Dec12.pdf','Definition 7.35 printed p. 241; Theorem 7.51 p. 251; Open Problem 7.53 printed p. 252 / PDF page 255'),
 ref('odd','Improved Lower Bounds for all Odd-Query Locally Decodable Codes','Arpon Basu; Jun-Ting Hsieh; Pravesh K. Kothari; Andrew D. Lin',2025,'https://arxiv.org/abs/2411.14361v1','FOCS 2025; November 2024 preprint, Introduction and Theorem 1.1 pp. 1–2, nonlinear binary codes'),
 ref('mv','Subexponential Upper Bounds for 3-Restricted Matching Vector Families','Divesh Aggarwal; Maciej Obremski',2026,'https://eccc.weizmann.ac.il/report/2026/141/','Revision 2, 11 August 2026; primary abstract, fixed-modulus matching-vector code consequence'),
 ref('mv2','Improved Subexponential Upper Bounds for 3-Restricted Matching Vector Families','Sidhant Saraogi',2026,'https://arxiv.org/abs/2608.27859v1','28 August 2026; primary abstract, bound for three-restricted families with restricted modulus range'),
 ref('relaxed','Relaxed vs. Full Local Decodability with Few Queries: Equivalence and Separations for Linear Codes','Elena Grigorescu; Vinayak M. Kumar; Peter Manohar; Geoffrey Mon',2026,'https://arxiv.org/abs/2511.02633','STOC 2026; primary abstract, linear-code equivalences at small query counts and separations for relaxed decoding'),
 ref('amortized','Amortized Relaxed Locally Decodable Codes','Jeremiah Blocki; Justin Zhang',2026,'https://arxiv.org/abs/2609.16332v1','14 September 2026; primary abstract, simultaneous block amortization and relaxed failure outputs'),
 ],
 context_blocks=[
 block('Local decoding retrieves one chosen message bit without scanning the stored codeword. The positive constant corruption fraction prevents a direct read of a systematically stored bit from meeting the requirement.'),
 block('The textbook gives polynomial-length binary codes with polylogarithmic query complexity and asks whether the query count can be constant. Its cited constant-query constructions instead have superpolynomial blocklength.'),
 block('The general odd-query lower bounds apply even to nonlinear binary codes. For each fixed query count their blocklength bounds are polynomial, so they leave open a sufficiently large polynomial exponent in this existence question.','odd'),
 block('The August 2026 matching-vector bound yields superpolynomial length within a particular three-query construction framework at fixed modulus. The target permits other encodings and any fixed query count.','mv'),
 block('The subsequent August preprint also bounds three-restricted matching-vector families, without claiming a lower bound for every binary locally decodable code.','mv2'),
 block('Relaxed decoders may report failure on some corrupted inputs. Their shorter codes and theorems comparing relaxed and full decoding do not automatically give the required success on every requested message bit.','relaxed'),
 block('The September 2026 construction combines relaxed outputs with amortizing queries over a consecutive block of message symbols. Constant queries per recovered symbol in that model are different from a constant total number of probes to recover any one requested bit.','amortized'),
 ],
 progress=[progress('2012','The textbook records polynomial length with polylogarithmic queries and poses the constant-query endpoint.','primary'),progress('2025','General odd-query lower bounds are improved while remaining polynomial for each fixed query count.','odd'),progress('2026','STOC work separates and relates relaxed and full local decoding for linear codes at specified query counts.','relaxed'),progress('2026-08-11','The matching-vector report states a superpolynomial length barrier for its fixed-modulus three-query framework.','mv'),progress('2026-08-28','A further matching-vector preprint sharpens bounds in a restricted modulus range.','mv2'),progress('2026-09-14','A constant-rate amortized relaxed construction is announced, with a different decoding requirement.','amortized')],
 importance=dict(score=92,method='editorial',assessed_on=DATE,reason='A central unrestricted existence question about whether constant bit-query locality and constant adversarial error tolerance can coexist with polynomial blocklength; distinct from the constant-rate logarithmic-query and relaxed-decoding questions.'),
 review_note='Individual source and formulation review. The exact textbook target is retained; query count is separated from efficient uniform construction. New preprint proofs have not been independently certified.',
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of polynomial-length constant-query binary local decoding in the unrestricted model. General fixed-query lower bounds remain polynomial, the August matching-vector bounds restrict the construction class, and the September constant-rate result permits amortized relaxed decoding. This is not an independent full audit of those results.',summary=[
 'A binary locally decodable code lets a decoder recover any requested message bit from a few bits of a corrupted codeword.',
 'The target is a fixed constant number of probes with a fixed positive fraction of arbitrary errors.',
 'The stored length may be any fixed polynomial in the message length, and nonlinear encodings are allowed.',
 'The question concerns existence, without an extra demand for an efficient uniform construction.',
 'A complete Lean-checked answer must establish this family or rule out all such constant-query polynomial-length families.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
