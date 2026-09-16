"""Complete randomized NOF disjointness with both parameters and full interaction."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6710'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered the early Rao–Yehudayoff draft’s randomized k-party intersection question and retained the full dependence on universe size and player count.',
 'Defined public-coin blackboard protocols with arbitrary interaction, worst-case bit cost, no free signalling through the identity of a speaker, and error at most one third on every input.',
 'Fixed the domain n>=1,k>=2 and absolute constant-factor matching bounds uniform in both parameters.',
 'Separated the shared-intersection predicate from pairwise disjointness and from number-in-hand communication.',
 'Retained the previously consolidated Jukna source as provenance, explaining that its narrower three-party super-polylogarithmic lower-bound question is already implied by known results.',
 'Individually assessed importance; compared the known logarithmically-many-player regime and the 2026 deterministic one-way result without treating either as the full randomized characterization.',
]
sources=[
 'Read Rao–Yehudayoff, Communication Complexity early author draft, introduction printed/PDF p. 16, k-party Disjointness, plus the draft’s model description. The draft is undated; its URL directory is not used as proof of a publication date. The concise introductory bounds omit factors and are not copied as precise uniform estimates.',
 'Read Jukna, Boolean Function Complexity author draft, Research Problem 5.3 printed p. 151/PDF p. 158. It asks a narrower deterministic three-party omega(log^3 n) lower bound; this is preserved as consolidated historical provenance, not as the active unresolved target.',
 'Read Sherstov, ECCC TR13-005, published 2 January 2013: abstract and §1 Theorem 1.1, including the randomized lower bound Omega(sqrt(n)/(2^k*k)). For k=3 this already implies the consolidated historical deterministic target. Full proof not independently audited.',
 'Read Podolskii–Sherstov, author-hosted 2020 manuscript of Inner Product and Set Disjointness: Beyond Logarithmically Many Parties: §§1–1.1, model and Theorem 1.1, and §4 statement of matching bounds. The author PDF retains placeholder ACM bibliographic fields, which were not copied. The actual publication is ACM Transactions on Computation Theory 12(4), Article 26, DOI 10.1145/3428671.',
 'Read Yang–Zhang, ECCC TR25-073 revision 3 accepted 5 July 2026: abstract and introduction. Its disjointness consequence concerns deterministic one-way three-party communication and is not a lower bound for unrestricted randomized interaction. Bounded later-source checks through 16 September 2026 found no characterization of the entire (n,k) domain.',
]
status=('Known results determine the constant-factor answer when the number of players is at least logarithmic in the universe size, and give strong lower bounds in smaller-player regimes. '
 'The bounded source review found no matching characterization over the full parameter domain. The consolidated historical three-player lower-bound threshold is already resolved, and the 2026 one-way deterministic result does not settle the active randomized target.')
complete(identifier,dict(
 title='Number-on-forehead disjointness complexity',
 criterion='resources',question_type='asymptotic_complexity',
 formal=r'''Determine, up to absolute constant factors, the randomized number-on-forehead communication complexity
\[
R(n,k)=R_{1/3}^{\mathrm{pub}}(\operatorname{DISJ}_{n,k})
\]
for all integers \(n\ge1\) and \(k\ge2\).

The input consists of \(k\) arbitrary subsets \(S_1,\ldots,S_k\subseteq[n]\). Player \(i\) sees every set except \(S_i\). The common output must be
\[
\operatorname{DISJ}_{n,k}(S_1,\ldots,S_k)
=\mathbf 1\!\left[\bigcap_{i=1}^k S_i=\varnothing\right].
\]
Players use public randomness and unrestricted interactive broadcasts, with error at most \(1/3\) on every input and communication measured by the maximum total number of broadcast bits.

The requested characterization is a specified noncircular asymptotic function \(g(n,k)>0\) and constants \(0<c\le C<\infty\), independent of both \(n\) and \(k\), such that
\[
c\,g(n,k)\le R(n,k)\le C\,g(n,k)
\qquad(n\ge1,\ k\ge2).
\]''',
 definitions=r'''The universe \([n]\) is \(\{1,\ldots,n\}\). Each \(S_j\) is represented by its characteristic vector \(x^{(j)}\in\{0,1\}^n\), where \(x^{(j)}_t=1\) means \(t\in S_j\). There is no restriction on set sizes, intersections, repeated sets, or the number of players relative to \(n\). In particular, \(k\) can exceed \(n\). The predicate asks for an empty intersection of all sets, not pairwise disjointness. Equivalently, the complementary predicate asks whether some row of the \(n\)-by-\(k\) incidence matrix is all ones; complementing the common output leaves the communication complexity unchanged.

All players know \(n,k\), their labels and the protocol. Player \(i\)'s initial view is the ordered tuple \((x^{(1)},\ldots,x^{(i-1)},x^{(i+1)},\ldots,x^{(k)})\). No player initially sees its missing column. This is the number-on-forehead model; it is different from giving player \(i\) only \(S_i\).

A deterministic protocol is a finite binary tree. An internal node specifies which player broadcasts the next bit. That bit can be any function of that player's visible input and the preceding public transcript. The bit is written once on a blackboard and is seen by all players; broadcasting one bit costs one bit, not \(k\) bits. Each leaf specifies a common output bit. The speaker and the decision to stop are determined by the public node, so they cannot transmit an uncharged input-dependent signal. The players may speak in any order prescribed by the tree and may return arbitrarily often; neither the number of rounds nor the number of messages is separately bounded.

A public-coin randomized protocol is a distribution over deterministic protocols, selected using shared randomness independent of the inputs. Its cost is the maximum depth of any tree in the support. This bound is over all inputs and all random outcomes, not an expectation. For every full input tuple, the probability that the common output equals \(\operatorname{DISJ}_{n,k}\) must be at least \(2/3\). No private communication, pre-shared secret or quantum resource is provided.

Local computation, storage and the complexity of the protocol description are free. Protocols may be chosen independently for each pair \((n,k)\); there is no uniform algorithm for generating them or local running-time requirement. The model therefore asks about communication alone.

Define \(R(n,k)\) to be the least integer \(d\ge0\) for which such a randomized protocol of cost at most \(d\) exists. This set of costs is nonempty: one player can transmit a missing column to another, who can broadcast the answer, using at most \(n+1\) bits. Both output values occur for every allowed \((n,k)\), so a zero-communication output independent of the input cannot attain error \(1/3\) on all inputs. Thus \(1\le R(n,k)\le n+1\).

The lower-bound part must apply to every allowed randomized interactive protocol. Restricting to one-way protocols or simultaneous messages gives a different lower-bound target. An upper bound may of course use a simpler protocol. All logarithms used to describe a proposed answer are base two. Constants hidden in the requested characterization cannot depend on the number of players.''',
 answer_criterion=r'''Provide a complete Lean-checked constant-factor characterization over the full domain \(n\ge1,k\ge2\), including both a protocol upper bound and a matching lower bound against every protocol in the stated model. The function \(g\) must describe the dependence on the parameters rather than merely rename the defining optimum over protocols. Bounds with a growing logarithmic or player-dependent gap, or a characterization only for a selected player-count regime, do not meet the target. Known regimes may be used as components of a full proof. This is an asymptotic-complexity question with the displayed multiplicative tolerance; additive \(1/100\) numerical tolerance is not the answer criterion.''',
 source_formulation=dict(text='The early draft describes the overlapping-input k-party intersection problem, compares deterministic and randomized communication bounds, and asks whether the randomized lower bound is tight.',
 caption='Paraphrase of Rao–Yehudayoff, early author draft, introduction p. 16, “k-party Disjointness”.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=88,method='editorial',
 reason='Multiparty set disjointness is a central explicit test problem for randomized communication with overlapping information; a sharp characterization would resolve a substantial general lower-bound gap even for small player counts.',
 basis='Individual assessment of its foundational role, the dependence on player count and its connections to proof and circuit lower bounds, while distinguishing already solved restricted regimes.'),
 why='Each player knows almost the entire input, which makes communication lower bounds much harder than in the ordinary split-input model. Set disjointness gives a concrete way to measure how this overlap and additional players change the power of randomized interaction. A full answer would clarify a basic limitation used in several connections between communication, circuits and proofs.',
 references=[
 ref('primary','Communication Complexity (early author draft)','Anup Rao; Amir Yehudayoff',None,
 'https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf',
 'Undated early draft; introduction, k-party Disjointness, printed/PDF p. 16'),
 ref('consolidated_1046_primary',"Boolean Function Complexity: Advances and Frontiers (author's early draft)",
 'Stasys Jukna',2012,'https://web.vu.lt/mif/s.jukna/boolean/bool-V7.pdf',
 'Research Problem 5.3, printed p. 151/PDF p. 158; narrower historical three-party lower-bound threshold'),
 ref('lower','Communication Lower Bounds Using Directional Derivatives','Alexander A. Sherstov',2013,
 'https://eccc.weizmann.ac.il/report/2013/005/',
 'ECCC TR13-005, published 2 January 2013; §1 Theorem 1.1, randomized disjointness lower bound'),
 ref('large','Inner Product and Set Disjointness: Beyond Logarithmically Many Parties',
 'Vladimir V. Podolskii; Alexander A. Sherstov',2020,
 'https://web.cs.ucla.edu/~sherstov/pdf/ip-disj-beyond-logn.pdf',
 'Author manuscript, §§1–1.1 Theorem 1.1 and §4; published ACM TOCT 12(4), Article 26, DOI 10.1145/3428671; disregard placeholder bibliographic fields in the manuscript'),
 ref('oneway','Deterministic Lifting Theorems for One-Way Number-on-Forehead Communication',
 'Guangxu Yang; Jiapeng Zhang',2026,'https://eccc.weizmann.ac.il/report/2025/073/',
 'Revision 3 accepted 5 July 2026; abstract and introduction, deterministic one-way three-party disjointness consequence'),
 ],
 context_blocks=[
 block('The overlapping views are essential: with two players this recovers the usual two-party problem, while additional players see different nearly complete views. A lower bound for private-input message passing cannot simply be substituted.','large'),
 block(r'For every fixed \(k\ge3\), the directional-derivative theorem yields a randomized lower bound of order \(\sqrt n\). Its explicit dependence is \(\Omega(\sqrt n/(2^k k))\). This does not match the general linear upper bound at a fixed small player count.','lower'),
 block(r'For \(n\ge2\) and \(k\ge\max\{2,\lceil\log_2 n\rceil\}\), the 2020 result determines the answer as \(\Theta(1+\log_2 n/\log_2(1+k/\log_2 n))\). Its constants are uniform in this regime. The full question also includes fewer players.','large'),
 block(r'The consolidated Jukna question only asks for a three-party deterministic lower bound growing faster than \((\log n)^3\). The known randomized polynomial lower bound already implies that historical threshold. It is not a second unresolved target here.','lower'),
 block('The July 2026 revision revisits disjointness with a deterministic one-way lower bound. Arbitrary randomized interaction is more powerful than that restricted protocol model, so the result is not a matching lower bound for this card.','oneway'),
 block('The requested bounds must be uniform as the number of players changes. Hiding a player-dependent constant in a fixed-player estimate can conceal precisely the dependence that the question asks to determine.'),
 ],
 progress=[
 progress('2013-01-02','The directional-derivative report gives the square-root randomized lower bound with explicit dependence on the player count.','lower'),
 progress('2020','The TOCT result determines the constant-factor complexity for at least logarithmically many players.','large'),
 progress('2026-07-05','The revised lifting report gives a deterministic one-way three-party consequence.','oneway'),
 progress('2026-09-16','The review fixes the full parameter domain and distinguishes known player regimes and restricted protocols; no full characterization is found.'),
 ],
),notes,sources,status,summary=[
 'Each of k players sees all input sets except the one assigned to that player.',
 'The goal is to decide whether the intersection of all sets is empty using public randomized communication.',
 'The card asks for matching bounds in both universe size and player count, with absolute constant factors.',
 'Protocols may interact arbitrarily, and their cost is the maximum total number of broadcast bits.',
 'The regime with at least logarithmically many players is understood, but it does not determine the answer for all smaller player counts.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
