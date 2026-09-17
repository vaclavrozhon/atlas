"""Complete the user-selected whole cryptogenography value function."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0218';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user selection of the full optimal-success function for every integer k at least two, at pointwise absolute accuracy 1/100.',
 'Specified the one-bit, one-owner, independent uniform prior; each uninformed player knows only that it is not the owner, and all communication and the final output are public.',
 'Defined protocols by finite public binary trees with arbitrary real local transition probabilities and independent private coins, without computational, communication or round budgets.',
 'Defined the observer by minimizing the joint success event, not merely maximizing the marginal posterior of the owner when the protocol can output the wrong bit.',
 'Used a supremum over finite protocols so no finite attainment is assumed; almost-surely terminating unbounded protocols have the same supremal value by finite truncation.',
 'Checked the 2019 improved two-player upper bound, including the paper’s correction for numerical SoS error; its two-player interval already has width less than 1/50, but it does not solve the selected function on all k.',
 'Preserved the individually assessed importance score 62 and required a complete Lean-checked pointwise bound for the entire function.',
]
sources=[
 'Read Brody’s Sublinear.info Problem 79, Banff 2017, saved revision oldid=1069, and the current short-link page: the question explicitly includes both two players and general k; its upper bound 0.361 is not used as current best.',
 'Read Brody–Jakobsen–Scheder–Winkler, Cryptogenography, ITCS 2014 pp. 13–22, DOI 10.1145/2554797.2554800, author-hosted proceedings PDF: §1.1 Theorems 1.1–1.4 pp. 14, §2 definition and Lemma 2.1 p. 15. The observer optimizes conditioned on the public output being correct. Lemma 2.1 changes a protocol into an always-correct one with the same joint success by adding k bits.',
 'Read Doerr–Künnemann, ICALP 2016 Article 150, DOI 10.4230/LIPIcs.ICALP.2016.150: abstract, §1 and §2.1–2.2 pp. 150:2–150:5. The model permits private randomness and unrestricted public communication; the published lower bound is 0.3384 and that work’s upper bound is 47/128. Infinite protocol trees and finite expected running time are distinguished from bounded-depth search.',
 'Read Scheder–Tang–Zhang, ISAAC 2019 Article 31, DOI 10.4230/LIPIcs.ISAAC.2019.31, published 28 November 2019: finite-tree model pp. 31:2–31:3, §1.2 table p. 31:3, §4 numerical-error correction p. 31:8, and §5 p. 31:9. The corrected two-player upper bound is 0.35183, rather than the raw optimization value 0.351612. Convergence of the proposed hierarchy to the actual optimum is itself left open there.',
 f'Bounded primary-source searches through {DATE} found no determination to the selected tolerance for all k. The two-player published certificates were inspected at the level stated above, not independently reproduced or formally verified.',
]
complete(identifier,dict(
 title='Optimal one-bit cryptogenography success for every number of players',criterion='characterization',question_type='function',year=2017,is_new=False,
 formal=r'''Determine the function \(p:\{2,3,4,\ldots\}\to[0,1]\), where
\[
 p(k)=\sup_{\Pi}\ \inf_{e}\Pr\bigl[Y_\Pi=X\ \text{and}\ e(T_\Pi)\ne J\bigr].
\]
Here \(X\) is a uniformly random secret bit, \(J\) is an independent uniformly random owner in \(\{1,\ldots,k\}\), \(\Pi\) ranges over the private-randomness public-communication protocols defined below, \(T_\Pi\) is the entire public transcript, and \(Y_\Pi\) is the protocol’s public output bit. The observer’s strategy \(e\) maps the transcript to one accused player and is chosen after the protocol is known. The requested answer is a function \(a\) with
\[
 |a(k)-p(k)|\le1/100\qquad\text{for every integer }k\ge2.
\]
There is no restriction on the time needed to evaluate or specify the answer.''',
 definitions=r'''There are \(k\) labeled cooperating players and one passive observer. Player \(J\) initially knows that it is the owner and knows \(X\). Every other player initially knows only that it is not the owner; it does not receive \(X\) or the identity of \(J\). The prior distribution of \((X,J)\), the number of players and the whole protocol are common knowledge. All players follow the protocol. They have independent private randomness, independent also of \((X,J)\), and have no private communication, prior secret keys, prior shared random string or quantum resources.

A protocol is a finite rooted binary tree. Each internal node \(v\) specifies the next speaker \(i_v\in\{1,\ldots,k\}\) and three numbers \(r_{v,*},r_{v,0},r_{v,1}\in[0,1]\). If the speaker is not the owner, it sends the bit \(1\) with probability \(r_{v,*}\). If it is the owner with secret \(x\), it sends \(1\) with probability \(r_{v,x}\). Otherwise it sends \(0\). The corresponding child is then visited. The conditional random choices can be made using fresh independent private coins. The parameters may be arbitrary real numbers: no effective sampling or local running-time constraint is imposed in this information-theoretic model.

The node is determined by the public prefix, so both the speaker schedule and the transmitted bits are visible to every player and the observer. A leaf \(t\) specifies a single output \(y_t\in\{0,1\}\), which is also public. All messages are broadcast; there is no anonymous channel, hidden timing signal or private preparatory phase. The tree can have arbitrarily large finite size and depth. There is no common upper bound on communication or number of rounds across the protocols in the supremum. This tree formulation records precisely the dependence on the speaker’s local input and the transcript; maintaining private state gives the same conditional-message description.

The observer knows the tree and all its probabilities and sees the full transcript, including its public output. It has unlimited computational power. It chooses one index \(e(t)\) for each possible transcript. The cooperating players win only when the public output is the actual secret and the accused player is not its original owner. If the output is incorrect, they lose regardless of the accusation. Their success probability is averaged over the uniform initial input and their private random choices; it is not a worst-case success guarantee for each owner or bit.

For clarity, put
\[
 w_{t,j}=\Pr[T_\Pi=t,\ X=y_t,\ J=j].
\]
The value of a fixed protocol is exactly
\[
 s(\Pi)=\sum_{t\text{ leaf}}\left(\sum_{j=1}^k w_{t,j}-\max_{1\le j\le k}w_{t,j}\right).
\]
Thus an optimal observer at \(t\) maximizes the joint posterior contribution of owner \(j\) and correctness of the public output. It need not maximize the marginal probability of \(J=j\) alone if the output can be wrong. Randomizing the accusation cannot improve the observer’s optimum. This formula also handles zero-probability transcripts without conditioning on them.

The target is the supremum \(p(k)=\sup_\Pi s(\Pi)\), not an assumption that a best finite protocol exists. Allowing protocols that terminate almost surely after an unbounded number of messages does not enlarge this supremum: their finite truncations can lose at most the probability of not yet terminating. The function includes every finite integer \(k\ge2\); it is not merely the two-player value, a large-\(k\) limit, a many-bit secret problem or a model with several original owners.''',
 answer_criterion=r'''Specify a real-valued function \(a\) on every integer \(k\ge2\) and give a complete Lean-checked proof that \(|a(k)-p(k)|\le1/100\) throughout that domain. Equivalently, a supplied interval for each \(k\), of width at most \(1/50\), with a complete Lean-checked containment proof, qualifies by taking its midpoint. Exact determination also qualifies, but neither a decimal expansion nor an efficient evaluation algorithm is required.

The argument must bound the supremum over all allowed protocols against the optimal observer. A list of experimental values, an uncertified optimization program, bounds only for finitely many player counts, or the defining supremum repeated without a determination does not satisfy the target. Matching the tolerance just for two players or just in the limit does not establish the function-wide requirement. If protocols approaching the lower bound are used, finite attainment of the supremum is not required.''',
 source_formulation=dict(text='The Banff problem asks how well a group can publicly reveal one secret bit while concealing its original owner, giving separate bounds for two players and for large groups. The user selected the optimal-success function for every number of players, with absolute accuracy one hundredth.',caption='Paraphrase of Sublinear.info Problem 79, Banff 2017, revision oldid=1069; full-function target selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='This model separates revealing information from revealing who supplied it, without relying on computational secrecy or a private channel. The function measures the best anonymity that cooperation alone can achieve as the group size changes.',
 references=[
 ref('primary','Problem 79: Cryptogenography','Joshua Brody',2017,'https://sublinear.info/79','Banff 2017 problem; saved revision oldid=1069; uniform one-bit owner model and separate two-player and large-k bounds'),
 ref('original','Cryptogenography','Joshua Brody; Sune K. Jakobsen; Dominik Scheder; Peter Winkler',2014,'https://doi.org/10.1145/2554797.2554800','ITCS 2014 pp. 13–22; §1.1 Theorems 1.1–1.4 p. 14; §2 definition of observer and success, and Lemma 2.1, p. 15; author PDF https://www.cs.swarthmore.edu/~brody/papers/itcs14-cryptogenography.pdf'),
 ref('protocols','Improved Protocols and Hardness Results for the Two-Player Cryptogenography Problem','Benjamin Doerr; Marvin Künnemann',2016,'https://doi.org/10.4230/LIPIcs.ICALP.2016.150','ICALP 2016, LIPIcs 55, Article 150; §1 pp. 150:2–150:3; §2.1–2.2 pp. 150:4–150:5; lower bound 0.3384 and finite-versus-infinite protocol distinction'),
 ref('sos','Searching for Cryptogenography Upper Bounds via Sum of Square Programming','Dominik Scheder; Shuyang Tang; Jiaheng Zhang',2019,'https://doi.org/10.4230/LIPIcs.ISAAC.2019.31','ISAAC 2019, LIPIcs 149, Article 31, published 28 November 2019; model pp. 31:2–31:3; §1.2 corrected-bound table p. 31:3; §4 numerical-error correction p. 31:8; §5 convergence question p. 31:9'),
 ],
 context_blocks=[
 block('The original work gives a one-third two-player protocol, a success probability of at least 0.5644 for sufficiently large groups, and an upper bound of three quarters for every group size. These do not determine the full function at the requested accuracy.','original'),
 block('The 2016 work improves the two-player lower bound to 0.3384. The 2019 work improves the upper bound to 0.35183 after accounting for numerical error in its sum-of-squares calculation. These published bounds already leave a two-player interval narrower than 1/50; they do not cover every k.','sos'),
 block('The upper-bound paper explicitly leaves convergence of its optimization hierarchy to the true optimum as an open question. Its numerical search should therefore not be treated as a certified approximation procedure for the full function.','sos'),
 block('A protocol can be required to reveal the bit correctly with certainty without changing the best joint success probability, by the original paper’s Lemma 2.1. The card keeps the direct joint-success definition so both correctness and anonymity are explicit.','original'),
 ],
 progress=[progress('2014','The original paper establishes the one-bit model and nontrivial two-player and general-group bounds.','original'),progress('2016','ICALP publishes an improved two-player protocol and upper bound.','protocols'),progress('2017','The Banff problem asks for improved bounds for two players and for larger groups.'),progress('2019-11-28','ISAAC publishes a corrected two-player upper bound of 0.35183, which is already close enough to the known lower bound for the card’s two-player tolerance alone.','sos')],
),notes,sources,'The checked published bounds already determine the two-player value to absolute error below 1/100, but no checked source establishes that accuracy for every k. The selected whole-function question remains a source-grounded open target after bounded later-work searches through 17 September 2026. Published numerical certificates have not been independently Lean-verified here.',summary=[
 'One uniformly chosen player knows a uniformly random secret bit and the group can communicate only in public.',
 'The players succeed when their public output is correct and an optimal observer accuses someone other than the original owner.',
 'The target is the best achievable success probability as a function of every number of players from two onward.',
 'Private randomness and arbitrarily long finite interaction are allowed, without computational secrecy or a private channel.',
 'A complete Lean-checked approximation within one hundredth is required at every player count, even though existing bounds already meet that precision for two players alone.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());next(r for r in a if r['id']==identifier).update(state='applied',applied_on=DATE);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
