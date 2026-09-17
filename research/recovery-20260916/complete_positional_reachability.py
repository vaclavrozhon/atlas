"""Apply the user-selected pure all-reachability, one-start equilibrium target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0571'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user choice of all-reachability objectives, pure positional strategies and one designated initial vertex.',
 'Defined finite deterministic turn-based arenas, unrestricted targets, plays, history-dependent unilateral deviations and binary payoffs.',
 'Distinguished an ordinary Nash equilibrium from a profile valid from every vertex or every history, and from a randomized memoryless equilibrium.',
 'Checked the MFCS 2026 result and conclusion; neither mixed-objective examples nor absorbing-target positive results resolve this selected question.',
 'Preserved assessed importance 67 and replaced the title-only statement with a self-contained proposition and complete Lean-checked acceptance criterion.',
]
sources=[
 'Read the complete Antonio Casares entry, Automata Exchange 24.2, dated 1 July 2024, on 17 September 2026. It asks about reachability, Buechi and parity separately; the user selected finite all-reachability games from one designated start.',
 'Read Alluwaym–Main–Schewe, arXiv:2607.07151v1, submitted 8 July 2026: introduction, §2 definitions, §3 Examples 1 and 3 and Theorems 2 and 4, Theorem 10 and §5 conclusion. Checked MFCS 2026 metadata, LIPIcs 386, 85:1–85:17, published 21 August 2026, DOI 10.4230/LIPIcs.MFCS.2026.85. The conclusion explicitly leaves pure all-reachability positional equilibria open. The full equilibrium-construction proof was not independently certified.',
 f'Bounded later-work search through {DATE} found no resolution of the user-selected pure all-reachability question. Detailed scope distinctions are saved in research/recovery-20260916/review_positional_scope.md.',
]
status='The MFCS 2026 paper gives randomized memoryless equilibria for a wider combination of objectives, but its conclusion explicitly leaves pure positional equilibrium existence open when all objectives are reachability. Its absorbing-target positive theorem imposes an extra restriction absent here. The selected ordinary equilibrium is required from one initial vertex, not simultaneously from all vertices.'
complete(identifier,dict(
 title='Pure positional Nash equilibria in reachability games',
 criterion='construction',question_type='yes_no',year=2026,
 formal=r'''Does every finite deterministic turn-based multiplayer game with a designated initial vertex and a reachability objective for each player admit a pure positional Nash equilibrium?

The equilibrium is evaluated from that one initial vertex. A unilateral deviating strategy may depend on the complete finite history, even though every strategy in the proposed equilibrium must depend only on the current vertex.''',
 definitions=r'''Fix any integer \(k\ge1\). An arena consists of a nonempty finite vertex set \(V\), a directed edge relation \(E\subseteq V\times V\), a partition \(V=V_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}V_k\), and an initial vertex \(v_0\in V\). Empty parts are allowed. Every vertex has at least one outgoing edge; self-loops are allowed. At a vertex in \(V_i\), player \(i\) chooses the next vertex along one outgoing edge. All players observe the full history. There are no simultaneous moves, random transitions or hidden information.

Player \(i\) has any target set \(T_i\subseteq V\), which may be empty or overlap other targets. Targets are not required to be absorbing: play may leave a target after reaching it. An infinite play \(\rho=v_0v_1v_2\cdots\) follows edges of \(E\). Its payoff to player \(i\) is
\[
u_i(\rho)=
\begin{cases}
1,&\text{if }v_t\in T_i\text{ for some integer }t\ge0,\\
0,&\text{otherwise.}
\end{cases}
\]
Thus a visit at time zero counts, and visiting a target once suffices forever. No player has a safety, recurrence or parity objective.

A pure strategy for player \(i\) assigns a legal successor to each finite path whose last vertex lies in \(V_i\). It can use the entire path and has no memory or computability restriction. A pure positional strategy is a function \(\sigma_i:V_i\to V\) satisfying \((v,\sigma_i(v))\in E\) for every \(v\in V_i\); at every occurrence of that vertex it makes the same choice.

A profile \(\sigma=(\sigma_1,\ldots,\sigma_k)\) determines one infinite play \(\operatorname{Out}(v_0,\sigma)\). It is a Nash equilibrium from \(v_0\) when, for every player \(i\) and every pure history-dependent strategy \(\tau_i\),
\[
u_i\bigl(\operatorname{Out}(v_0,\sigma)\bigr)
\ge
u_i\bigl(\operatorname{Out}(v_0,\sigma_{-i},\tau_i)\bigr).
\]
Here \((\sigma_{-i},\tau_i)\) replaces only player \(i\)'s strategy; every other player keeps the originally specified strategy, including at vertices not reached by the original play. A player already winning cannot improve. A losing player must have no unilateral way to reach its target.

The question quantifies over all finite arenas, all target sets, all player counts and every designated start, and asks for the existence of a positional profile for each such instance. The profile may depend on the start. It need not be an equilibrium from every vertex simultaneously or following every history, and no particular payoff vector is prescribed. No running-time bound or algorithm to find the profile is required. Randomized positional profiles do not meet the pure-strategy requirement. Allowing randomized deviations with expected binary payoffs would give the same equilibrium condition against a fixed pure profile: a positive probability of reaching a target entails a finite legal reaching history that can be followed by a pure deviation.''',
 answer_criterion=r'''Give a complete Lean-checked proof that every instance in the stated class has such a pure positional equilibrium, or a complete Lean-checked refutation. A refutation may provide one finite arena, target sets and initial vertex together with a proof that every pure positional profile has a profitable unilateral deviation.

A counterexample using other objective types, stochastic transitions, a required payoff vector, or equilibrium simultaneously from every vertex does not settle this proposition. Existence of randomized memoryless profiles or pure profiles with memory does not prove it. Positive results restricted to absorbing targets do not cover the full target.''',
 source_formulation=dict(text='Casares asks whether multiplayer graph games with reachability, Büchi or parity objectives always have Nash equilibria whose strategies are positional. The user selected reachability for every player, finite deterministic turn-based arenas and equilibrium from one designated start, with unrestricted unilateral deviations.',caption='Paraphrase of Automata Exchange 24.2, 1 July 2024; objective and start conventions explicitly selected by the user on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='A positional strategy stores no history and is directly implementable as one choice per vertex. The question asks whether all players can always make mutually stable choices of this form when their goals are to reach target sets, despite the extra power available to a deviating player who remembers the past.',
 references=[
 ref('primary','24.2 Positional Nash Equilibria','Antonio Casares',2024,'https://automata.exchange/24.02-positional-nash-equilibria/','Complete short entry, dated 1 July 2024; the reachability branch is selected here'),
 ref('simple','Simple Nash Equilibria for Qualitative Multiplayer Games','Mona Alluwaym; James C. A. Main; Sven Schewe',2026,'https://arxiv.org/abs/2607.07151v1','Version 1, 8 July 2026; §2 definitions, §3 Examples 1 and 3, Theorem 10 and §5 conclusion; MFCS 2026, LIPIcs 386, 85:1–85:17, published 21 August, DOI 10.4230/LIPIcs.MFCS.2026.85'),
 ],
 context_blocks=[
 block('A Nash equilibrium does not require everyone to win. It requires that each losing player remain unable to win by changing only their own choices while the other players keep theirs. The restrictions on equilibrium strategies and on deviations must therefore be stated separately.'),
 block('The current vertex does not generally record which targets the play visited earlier. Even with a finite arena and simple reachability goals, forgetting that history can affect which continuation is stable.'),
 block('The 2026 theorem allows randomization in memoryless strategies and establishes a stronger continuation-based equilibrium notion for its stated objective classes. Randomization is a resource absent from this card’s proposed profile.','simple'),
 block('The same paper proves a pure positional result when all relevant targets are absorbing. Its conclusion still leaves the all-reachability question without that restriction open. Examples mixing reachability with safety, or using other infinite-play objectives, do not settle the selected class.','simple'),
 ],
 progress=[
 progress('2024-07-01','The source asks about positional equilibria for reachability, Büchi and parity games.'),
 progress('2026-08-21','MFCS 2026 publishes randomized memoryless equilibrium results and a restricted absorbing-target positional result, while retaining the general pure all-reachability question.','simple'),
 ],
),notes,sources,status,summary=[
 'Every player in a finite deterministic turn-based game wants to visit their own target set at least once.',
 'The question asks for a Nash equilibrium in which each player always makes the same choice at the same vertex.',
 'A player testing a unilateral improvement may remember the entire play history while all other players keep their original choices.',
 'Equilibrium is required from one designated start, targets need not be absorbing, and neither a particular winning vector nor randomized strategies are allowed.',
 'A complete Lean-checked solution must prove universal existence or verify a counterexample; the 2026 randomized theorem leaves this pure all-reachability target open.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
