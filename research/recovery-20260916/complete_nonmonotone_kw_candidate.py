"""Write the user-selected candidate characterization with explicit mapping reductions."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-2571';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A randomized-communication characterization of ordinary KW games',
 status='uncertain',criterion='characterization',question_type='yes_no',
 formal=r'''Is the following candidate characterization true? For every family of total two-party search relations \((R_n)_{n\ge2}\) with polynomially bounded input and answer lengths and deterministic polylogarithmic communication for verifying a proposed answer, the following are equivalent:

1. \(R_n\) has a public-coin randomized protocol with polylogarithmic communication and success probability at least \(2/3\) on every input pair.
2. \(R_n\) is equivalent, under deterministic polylogarithmic-communication mapping reductions in both directions, to the ordinary Karchmer–Wigderson game of a partial Boolean function on at most quasipolynomially many variables.

All bounds, quantifiers, models and reductions are specified below. This is a user-selected editorial candidate, not a conjecture asserted verbatim by the source.''',
 definitions=r'''For each integer \(n\ge2\), let \(X_n,Y_n\) be nonempty subsets of \(\{0,1\}^{n^{a}}\), let \(1\le\ell_n\le n^{a}\), and let
\[
R_n\subseteq X_n\times Y_n\times[\ell_n],\qquad [\ell]=\{1,\ldots,\ell\},
\]
where the integer \(a\ge1\) is fixed for the family. Totality means that for every \((x,y)\in X_n\times Y_n\), at least one \(i\in[\ell_n]\) satisfies \(R_n(x,y,i)\). Alice receives \(x\), Bob receives \(y\), and both must output a common valid \(i\).

A deterministic verification protocol is given \(i\) publicly, in addition to the split input \((x,y)\), and both parties determine exactly whether \(R_n(x,y,i)\) holds. Assume there are constants \(K>0\) and an integer \(b\ge1\), independent of \(n\), such that this uses at most \(K(\log_2(n+2))^b\) communicated bits on every input and every proposed answer. These are the communication analogues of total, efficiently verifiable search relations. There is no algorithmic uniformity, local-computation, or finite-description requirement on the family or its local operations; this is a communication-complexity assertion, not ordinary Turing-machine TFNP.

In condition 1, for each \(n\) a protocol has access to a finite public string of independent fair random bits. Its length is unrestricted and uncharged. Its worst-case number of communicated bits, over every input and random string, is at most \(K'(\log_2(n+2))^{b'}\) for constants \(K',b'\) fixed for the family. On every input pair, the probability that both parties output one common \(i\) satisfying \(R_n(x,y,i)\) is at least \(2/3\). The error is over the public randomness, not an input distribution. Local computation is free. Communication is by the ordinary binary protocol-tree model; speaker identity and termination are determined by the public transcript and randomness and do not transmit extra information for free.

An ordinary KW game is specified by two nonempty disjoint sets \(A_n,B_n\subseteq\{0,1\}^{m_n}\). Equivalently, a partial Boolean function \(f_n\) is zero on \(A_n\), one on \(B_n\), and undefined elsewhere. Alice receives \(u\in A_n\), Bob receives \(v\in B_n\), and a valid answer is any \(j\in[m_n]\) with \(u_j\ne v_j\). No order between these two bits is required. Neither set must be monotone, and no circuit-size, computational-uniformity or decidability bound is imposed on \(f_n\).

A deterministic \(t\)-bit mapping reduction from a relation \(S\subseteq X\times Y\times I\) to \(S'\subseteq X'\times Y'\times I'\) consists of local maps \(M_A:X\to X'\), \(M_B:Y\to Y'\), and a deterministic two-party decoder. Given \(x,y\) and any publicly supplied \(j\in I'\) with
\[
S'(M_A(x),M_B(y),j),
\]
the decoder uses at most \(t\) bits of communication and both parties output one common \(i\in I\) satisfying \(S(x,y,i)\). Correctness is required for every valid target answer, not just answers chosen by one preferred target solver. The decoder halts within its communication bound for all candidate \(j\), even if the target relation does not hold. The local maps incur no communication cost; their description and evaluation times are unrestricted. There is one mapped target instance and one returned answer, with no adaptive oracle calls.

Precisely, condition 2 says that there exist constants \(K''>0\), an integer \(b''\ge1\), and for every \(n\) an integer
\[
1\le m_n\le2^{K''(\log_2(n+2))^{b''}},
\]
a partial function \(f_n\) as above, and reductions in both directions between \(R_n\) and \(\operatorname{KW}(f_n)\), each with at most \(K''(\log_2(n+2))^{b''}\) bits of decoding communication. The two pairs of local maps need not be inverse functions. All choices may depend on the relation family and \(n\), but the constants and exponents must work for the entire family. The quasipolynomial dimension convention matches the exponential-in-verification-cost expansion in the source's monotone comparison. Merely representing an arbitrary relation with exponentially many coordinates in \(n\) does not meet this bound.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of this candidate equivalence for all relation families meeting the stated conditions. A proof must supply the quantified communication bounds and both mapping reductions, valid for every target answer. A refutation may give a family with cheap verification and randomized solution but no such ordinary-KW equivalence, with a complete impossibility proof. Proving only the necessary randomized upper bound, the monotone version, or a weaker one-way or randomized reduction does not settle the assertion.',
 why='An intrinsic characterization would explain which total communication search tasks arise from ordinary Boolean function separation. It would connect randomized communication with the structural reductions behind circuit-depth games, while distinguishing ordinary games from their monotone counterparts.',
 importance=dict(score=79,method='editorial',reason='A structural bridge between total search, communication and Boolean circuit games. The selected candidate makes a broad characterization program falsifiable, while its status must remain explicitly separate from the source’s established monotone theorem.'),
 source_formulation=dict(text='The source asks for a communication characterization of nonmonotone KW games after proving the analogous monotone representation theorem. It does not propose the equality with cheaply verifiable randomized-polylogarithmic search. The user explicitly selected that editorial candidate, with deterministic polylogarithmic mapping equivalence and the quasipolynomial dimension convention made precise here.',caption='Buss–Fleming–Impagliazzo, ITCS 2023, §3.1 pp.30:26–30:27 and §4 open question 3 p.30:32.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','TFNP Characterizations of Proof Systems and Monotone Circuits','Sam Buss; Noah Fleming; Russell Impagliazzo',2023,'https://doi.org/10.4230/LIPIcs.ITCS.2023.30','§3.1 communication definitions and Lemma 12 pp.30:26–30:27; §4 questions 3–4 p.30:32'),
 ref('randomized','On Communication Complexity of Fixed Point Computation','Anat Ganor; Karthik C. S.; Dömötör Pálvölgyi',2022,'https://arxiv.org/abs/1909.10958v3','Revision of 25 May 2022, Appendix D pp.31–33, ordinary versus monotone KW communication'),
 ],
 context_blocks=[
 block('The source’s Lemma 12 represents a total relation with t-bit answer verification as a monotone KW game on at most 2ᵗ times the number of answers coordinates, with t-bit mapping reductions in both directions. For polylogarithmic verification this allows a quasipolynomial number of coordinates.'),
 block('Ordinary KW asks only for a differing coordinate. Randomized fingerprinting can locate one with polylogarithmic communication, independently of the complexity of the underlying partial function; the cited discussion records an even sharper logarithmic bound. This gives a necessary randomized upper bound for relations reducing to such games.','randomized'),
 block('Monotone games impose a direction on the differing bits and can have polynomial randomized communication complexity. The ordinary-game characterization therefore cannot simply repeat the source’s unrestricted monotone TFNP representation.','randomized'),
 block('The difficult direction of the selected candidate is sufficiency: cheap verification and a randomized protocol would have to yield deterministic mapping equivalence to an ordinary game of the stated dimension. The reviewed sources neither state nor prove this exact assertion.'),
 block('The source’s next question concerns reductions between games versus low-depth reductions between Boolean functions. That is a separate target and is not substituted for the characterization selected here.'),
 ],
 progress=[
 progress('2022-05','The fixed-point communication manuscript contrasts logarithmic randomized complexity for ordinary KW with substantially harder monotone games.','randomized'),
 progress('2023-01','The source proves the monotone representation theorem and asks for a characterization in the ordinary nonmonotone case.'),
 ],
),[
 'Applied the user-confirmed candidate rather than attributing a new conjecture to the original source.',
 'Defined families, totality, answer verification, worst-case public-coin communication and absence of local computational uniformity requirements.',
 'Specified partial Boolean functions, ordinary unoriented differing-coordinate answers and quasipolynomial dimension growth.',
 'Defined both local mapping reductions and deterministic decoding for every valid returned answer, keeping them distinct from function reductions and randomized reductions.',
 'Recorded only a necessary randomized upper bound as known; marked the exact candidate’s current status uncertain and required a complete Lean-checked characterization or refutation.',
],[
 'Read ITCS 2023 §3.1 definitions and the complete statement and construction of Lemma 12, including 2^t times ell variables.',
 'Read §4 questions 3 and 4 and kept their distinct targets separate.',
 'Read Appendix D of the 25 May 2022 fixed-point manuscript, including its ordinary-KW randomized upper bound and monotone comparison.',
 'Checked related ITCS 2019 TFNP characterizations and bounded primary-source searches through 18 September 2026; found no explicit theorem or refutation for this exact candidate equivalence.',
], 'Uncertain current status of the precise editorial candidate. The source poses a broad ordinary-KW characterization problem, but not the proposed equivalence with cheaply verifiable randomized-polylogarithmic search. The user selected that candidate on 18 September 2026. The necessary randomized upper bound and the separate monotone representation theorem are supported by the checked sources; sufficiency was not established by this bounded review.',summary=[
 'An ordinary Karchmer–Wigderson game asks two parties to find a coordinate where their differently classified Boolean inputs disagree.',
 'The selected candidate says these games capture exactly total search tasks with cheap answer verification and cheap randomized communication.',
 'Capture means deterministic mapping reductions in both directions, with polylogarithmic communication and at most quasipolynomially many target coordinates.',
 'Ordinary games have cheap randomized protocols, whereas the known monotone representation theorem covers a broader class of total search tasks.',
 'The exact equivalence is a user-selected editorial candidate whose current status remains uncertain, not a conjecture quoted from the source.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
