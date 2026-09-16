"""Quantified Presburger state complexity, with the approved leaderless semantics."""
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims

identifier='TCS-3381'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']+[
    ref('fast2024','Fast and Succinct Population Protocols for Presburger Arithmetic',
        'Philipp Czerner; Roland Guttenberg; Martin Helfrich; Javier Esparza',2024,
        'https://arxiv.org/abs/2202.11601v3',
        'Journal of Computer and System Sciences 140 (2024), 103481; inspected author v3 dated 30 October 2023, abstract and introduction: quantifier-free input size'),
    ref('ordered2026','Population Protocols over Ordered Agents',
        'Michael Blondin; Michaël Cadilhac; Benjamin Courchesne; Lucie Guillou; Corto Mascle; Isa Vialard',2026,
        'https://doi.org/10.4230/LIPIcs.ICALP.2026.167','ICALP 2026; abstract and introduction: agents equipped with an order, a distinct model'),
]
notes=[
    'Applied the user-selected leaderless model, binary pair interactions and stable agreement on every fair execution, without a synthesis-time or convergence-time requirement.',
    'Specified quantified Presburger syntax, natural-number quantification, binary coefficient encoding, original formula size and the global polynomial state bound.',
    'Recovered the source population-size-at-least-two convention and defined multiset transitions, global fairness, initial counts and unanimous eventual output explicitly.',
    'Separated known succinct quantifier-free protocols from succinctness in the original quantified formula, and separated existence from construction complexity.',
    'Individually assessed importance, retained provenance/category, and supplied context, progress, summary and Lean acceptance.',
]
sources=[
    'STACS 2020 full PDF §§2–3: Presburger predicates, multiset configurations, pairwise conversion, input population at least two, and global reachability fairness.',
    'STACS 2020 §4 Theorem 2: polynomial states for quantifier-free formulas; §7 printed p. 14: open quantified-formula state question and Theorem 13 on synthesis time.',
    'Fast and Succinct, saved arXiv:2202.11601v3 abstract and introduction: m is the binary size of a Boolean combination of threshold and remainder predicates; later time improvements do not measure size before quantifier elimination.',
    'ICALP 2026 Ordered Agents publisher abstract/introduction checked on 16 September; ordered identities change the model and do not settle the ordinary anonymous protocol target.',
    'Bounded current search for quantified Presburger state bounds found no resolution; the prior user explicitly selected leaderless pairwise stable consensus.',
]
status=('Open in the precise source distinction: STACS 2020 §7 asks for polynomial states in the original possibly quantified formula, while its main theorem covers the quantifier-free representation. '
        'The inspected 2024 fast-and-succinct result still measures a quantifier-free formula and does not establish the present bound before quantifier elimination. '
        'On 16 September 2026 a bounded later-work check found no resolution; the 2026 ordered-agent paper concerns a different model. '
        'This is an existential state-size question, not an efficient synthesis claim: the source separately proves a synthesis-time obstruction. '
        'Definitions and theorem scopes were inspected; full source proofs, exhaustive literature coverage and Lean formalization are not claimed.')
complete(identifier,dict(
    question_type='yes_no',
    formal=r'''Do there exist positive integers \(C,k\) such that every Presburger formula \(\varphi(x_1,\ldots,x_d)\), including arbitrary nested quantifiers, has a leaderless pairwise population protocol \(P_\varphi\) with
\[
|Q_\varphi|\le C(1+|\varphi|)^k
\]
that computes its truth value on every input \(\mathbf a\in\mathbb N^d\) with \(\sum_i a_i\ge2\), reaching permanent unanimous agreement under every fair execution?
The size is that of the original quantified formula, using the syntax and encoding below. The constants are independent of the formula and population size. No running-time bound is required for constructing the protocol or for reaching consensus.''',
    definitions=r'''All variables range over \(\mathbb N=\{0,1,2,\ldots\}\). Formulas are finite syntax trees built from linear comparisons \(\sum_i c_i z_i>b\) and congruences \(\sum_i c_i z_i\equiv b\pmod m\), Boolean connectives \(\neg,\wedge,\vee\), and quantifiers \(\exists z,\forall z\). Coefficients and thresholds are integers, and a congruence modulus is an integer \(m\ge2\). A congruence asserts integer divisibility of the difference by \(m\). Comparisons and sums are evaluated in the integers; quantified values remain nonnegative. Equality and other order relations are expressible using these primitives. Coefficient multiplication is by fixed encoded integers, not multiplication of two variables. Remainder atoms are the standard definitional extension used by the source.

The formula has a declared list of \(d\ge1\) free input variables. A sentence can be treated as independent of one dummy input variable. Encode the original syntax tree explicitly, with operator tags, parentheses or equivalent delimiters, variable binding/index information, and signed binary coefficients, thresholds and moduli. The size \(|\varphi|\) is the total bit length, including the free-variable list. Subexpressions are written at each occurrence; there are no shared circuit nodes, macros hiding large formulas, or uncharged quantifier elimination. Standard explicit encodings of this syntax are polynomially interconvertible, so the existence of some polynomial state bound is independent of their routine delimiter choices.

A leaderless pairwise population protocol consists of a finite state set \(Q\), an input map \(\iota:\{1,\ldots,d\}\to Q\), an output map \(o:Q\to\{0,1\}\), and a finite transition relation \(T\). A transition replaces a multiset of exactly two states by another multiset of exactly two states. Thus a rule may have the form \(\{p,q\}\to\{r,s\}\), allowing equal states; two occurrences of a state require two distinct agents in that state. Include the identity rule for every two-state multiset, so every configuration of at least two agents admits an infinite execution. Multiple rules with the same input multiset are allowed and are resolved by the scheduler. All agents are anonymous; there are no identifiers, order comparisons, extra leaders, initially supplied helper agents, or a known bound on the population.

A configuration is a multiplicity vector \(D:Q\to\mathbb N\). A rule with input multiset \(u\) and output multiset \(v\) is enabled when \(D\ge u\) coordinatewise and then produces \(D-u+v\). The input \(\mathbf a=(a_1,\ldots,a_d)\) gives exactly
\[
D_{\mathbf a}(q)=\sum_{\{i:\iota(i)=q\}}a_i
\]
agents in each state \(q\), with no additive initial population. Total population size is conserved. As in the source, correctness is required for all inputs with at least two agents; the zero-agent and one-agent cases are outside this protocol convention.

Write \(D\to^*E\) for reachability by finitely many legal transitions, including zero transitions. An infinite execution \(D_0,D_1,\ldots\) is globally fair if, for every configuration \(E\), whenever the set \(\{j:D_j\to^*E\}\) is infinite, the set \(\{j:D_j=E\}\) is also infinite. This is the source's configuration-reachability fairness, not merely the requirement that each pair of agent identities meet infinitely often.

The protocol computes \(\varphi\) when, for every allowed input and every fair execution starting at \(D_{\mathbf a}\), there is a finite index \(J\) such that for every \(j\ge J\) and every occupied state \(q\), \(o(q)\) equals the Boolean truth value of \(\varphi(\mathbf a)\). All agents must agree thereafter; they need not detect stabilization or stop interacting. The stabilization index can depend on both input and execution.

The resource being minimized is the number of states available to one agent, \(|Q|\), not its bit logarithm, the number of agents, or the time to consensus. Protocol descriptions depend on \(\varphi\) but not on its input vector. All transition rules are explicit finite rules; pairwise state semantics cannot hide an oracle for the predicate. The same \(C,k\) work for all formulas. The assertion is purely existential and does not add an efficient uniform synthesis procedure.''',
    answer_criterion=r'Supply a complete Lean-checked proof or refutation of the stated uniform polynomial bound. An affirmative proof must establish one pair \(C,k\) and the existence, for every original quantified formula, of a protocol with the required state count, leaderless initialization and correctness on every fair execution for every allowed input. A negative proof must establish the negation of that quantified assertion. A polynomial bound only after quantifier elimination, a protocol using extra leaders, or a lower bound only on construction time does not answer this target. No numerical tolerance changes the proposition, and no Lean proof is supplied merely by specifying a finite transition table.',
    references=refs,
    source_formulation=dict(text='The conclusion asks whether polynomially many states suffice for every Presburger formula, possibly with quantifiers, and distinguishes this from the known quantifier-free construction and the difficulty of synthesis. The user selected the leaderless pairwise model with stable consensus under all fair executions.',caption='Editorial paraphrase of §7 with the user-selected protocol semantics',citation='primary',format='editorial_paraphrase'),
    target_revision=dict(date='2026-09-16',previous_formal=old['formal'],authorization='User selected protocols without leaders, pairwise interactions and stable consensus on every fair run; no construction or convergence bound.',scope='State bound in the original quantified formula under standard anonymous population-protocol semantics.'),
    context_blocks=[
        block('Population protocols distribute computation among anonymous agents with a fixed finite repertoire of states. They determine properties of the initial counts of input types. Presburger arithmetic describes exactly the predicates computable in this model, but that expressiveness theorem does not determine how many states a short logical specification requires.', 'primary'),
        block('The 2020 theorem gives polynomially many states for quantifier-free combinations of linear thresholds and congruences. A quantified formula can be much shorter than a formula obtained by eliminating its quantifiers. Consequently, applying the known theorem to an expanded quantifier-free formula does not establish a polynomial bound in the original input size.', 'primary'),
        block('The source also distinguishes small protocols from efficiently finding them. The present target asks whether small protocols exist; its affirmative answer would not include a polynomial-time synthesis algorithm or a convergence-time guarantee. Later fast-and-succinct results strengthen the quantifier-free case, and their input-size parameter remains crucial.', 'fast2024'),
        block('Recent protocols over ordered agents allow interactions to inspect extra positional information. That changes the anonymous model specified here and does not provide an answer to this state-complexity question.', 'ordered2026'),
    ],
    why='The question compares the succinctness of logical descriptions with that of anonymous distributed computation. It asks whether quantifier compression forces an unavoidable increase in the number of local states, even when computation time is unrestricted. This separates representational power from synthesis and stabilization complexity.',
    importance=dict(score=76,method='editorial',reason='A structural succinctness question linking quantified logic and finite-state distributed computation; it isolates local state complexity beyond the established expressiveness and quantifier-free synthesis results.'),
    progress=[
        progress('2020','Theorem 2 establishes succinct leaderless protocols for quantifier-free formulas; §7 explicitly leaves state bounds for original quantified formulas open.','primary'),
        progress('2024','Fast-and-succinct protocols improve the quantifier-free size/time tradeoff, without establishing a bound before quantifier elimination.','fast2024'),
        progress('2026','Ordered-agent protocols study additional interaction capabilities and therefore a different computational model.','ordered2026'),
        progress('2026-09-16','The bounded update retained the quantified-formula state question as source-open and recorded the user-selected leaderless semantics.','primary'),
    ],
),notes,sources,status,summary=[
    'A population protocol uses anonymous finite-state agents whose pairwise interactions eventually decide a predicate of their initial counts.',
    'The question asks whether every quantified Presburger formula has such a leaderless protocol with polynomially many states in the original formula size.',
    'Correctness requires permanent unanimous agreement on every globally fair execution, without a time bound.',
    'Known succinct protocols for quantifier-free formulas do not control the expansion caused by eliminating quantifiers.',
    'A resolution would separate or equate the succinctness of quantified logical specifications and anonymous finite-state distributed computation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
