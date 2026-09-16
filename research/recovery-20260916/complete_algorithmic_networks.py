"""Characterize source-demand network patterns for algorithmic cut sufficiency."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0254'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Q12 and its full algorithmic, rather than Shannon-random-variable, network model.',
 'Specified a network as a fixed finite directed acyclic graph together with source placement, terminal demands and finite-versus-unlimited channel types.',
 'Defined the cut inequalities using conditional plain Kolmogorov complexity and all vertex subsets.',
 'Expanded logarithmic precision into uniform quantified constants for cut slack, local information creation and capacity overhead.',
 'Required existential per-instance messages, preserving the source’s logarithmic nonuniformity rather than adding a uniform efficient encoder requirement.',
 'Preserved the existing importance assessment and distinguished ordinary cut inequalities from arbitrary information inequalities and linear coding restrictions.',
]
sources=[
 'Read Romashchenko–Shen–Zimand, 27 Open Problems in Kolmogorov Complexity, SIGACT News 52(4), 2021 issue, §6 pp. 11–14 in the editor-hosted PDF; Q12 p. 14, Figures 4–7 and the separate Q13/Q14 discussion.',
 'Read Shen, Multisource Algorithmic Information Theory, manuscript dated 10 March 2006, §§1, 7–10; checked the Dagstuhl publication DOI 10.4230/DagSemProc.06051.9, published 31 July 2006. Its formal model explicitly uses acyclic graphs, per-vertex conditional descriptions and capacities.',
 'The 2006 source’s §7 gives the incoming-cut inequality; §8 treats one-source broadcast and §9 explains why the Gray–Wyner cut conditions can fail. The 2021 source retains the classification as Q12.',
 'Checked bounded later primary-source searches through 16 September 2026 for this algorithmic classification. No general necessary-and-sufficient structural criterion was found. Results about Shannon network capacity, network-description complexity and practical network compression were not treated as resolutions.',
]
status=('The 2021 source asks for the general classification after exhibiting both sufficient and insufficient network patterns. '
 'The explicit target below retains its existential algorithmic-information interpretation and logarithmic tolerance. '
 'No general characterization was found in the bounded later-source check; this review does not assert that every special-case result has been exhaustively surveyed.')
complete(identifier,dict(
 title='Algorithmic networks characterized by cut inequalities',
 criterion='characterization',question_type='function',
 formal=r'''Characterize the finite directed acyclic network patterns \(\mathcal N\) for which the information-flow inequalities across all cuts are sufficient, with logarithmic precision, for transmitting arbitrary correlated input strings to their requested destinations.

Precisely, determine a necessary-and-sufficient condition on \(\mathcal N\) for the property
\[
\forall a\in\mathbb N\ \exists b,B\in\mathbb N_{\ge1}\
\forall n\ge2\ \forall x_1,\ldots,x_k\
\forall (u_e)_{e\in E_{\rm fin}}:
\quad
\operatorname{Cut}_a(\mathcal N,x,u,n)
\Longrightarrow
\operatorname{Code}_{b,B}(\mathcal N,x,u,n),
\]
where \(|x_i|\le n\) and \(u_e\in\{0,\ldots,n\}\). The definitions below specify both predicates. The constants \(b,B\) may depend on the fixed pattern and on \(a\), but not on \(n\), the strings or the capacities.

Equivalently, determine the Boolean characteristic function that assigns one exactly to patterns with this property. The characterization must be a condition on the finite network pattern, including source placement and demands, rather than a restatement of the quantification over strings and codes.''',
 definitions=r'''Fix an optimal universal machine for plain conditional Kolmogorov complexity:
\[
C(s\mid t)=\min\{|p|:\ U(p,t)\text{ halts with output }s\}.
\]
Use a fixed effective self-delimiting encoding of finite tuples and let \(C(s)=C(s\mid\epsilon)\), where \(\epsilon\) is the empty string. All complexity quantities here refer to this one fixed machine. There is no running-time restriction on the programs in the definition.

A pattern \(\mathcal N\) consists of a finite directed acyclic graph \(G=(V,E)\), a fixed integer \(k\ge1\) of input labels, two sets \(P_v,D_v\subseteq\{1,\ldots,k\}\) for each vertex \(v\), and a partition \(E=E_{\rm fin}\mathbin{\dot\cup}E_\infty\). The union of the \(P_v\) is all input labels. Vertex \(v\) initially possesses \(x_{P_v}\), the tuple of strings with indices in \(P_v\), and must recover \(x_{D_v}\). A label may be supplied at more than one vertex or requested at several vertices. Empty possession or demand sets are permitted. Vertices and edges have fixed orders for encoding tuples. The graph size, label count, placement and demand sets are not growing parameters.

An instance chooses any correlated binary strings \(x_1,\ldots,x_k\) of lengths at most \(n\) and nonnegative integer capacities \(u_e\le n\) for the finite channels. The scale \(n\) bounds both input lengths and finite capacities; all such scales and choices are quantified. Edges in \(E_\infty\) have no capacity constraint. Put \(L_n=\lceil\log_2(n+2)\rceil\).

For \(W\subseteq V\), write
\[
P(W)=\bigcup_{v\in W}P_v,\qquad
D(W)=\bigcup_{v\in W}D_v,\qquad
\delta^-(W)=\{(v,w)\in E:v\notin W,\ w\in W\}.
\]
The cut predicate \(\operatorname{Cut}_a\) requires, for every \(W\) whose entering edges all lie in \(E_{\rm fin}\),
\[
C\!\left(x_{D(W)}\mid x_{P(W)}\right)
\le \sum_{e\in\delta^-(W)}u_e+aL_n.
\]
The empty sum is zero. A cut with an unlimited entering edge imposes no inequality. These are ordinary incoming-cut bounds, not the family of all possible Shannon or non-Shannon information inequalities.

The code predicate \(\operatorname{Code}_{b,B}\) asserts the existence of a binary message \(m_e\) on every edge, each of length at most \((n+2)^B\), such that
\[
|m_e|\le u_e+bL_n\qquad(e\in E_{\rm fin})
\]
and, at every vertex \(v\),
\[
C\!\left(
  (m_e)_{e\in\operatorname{out}(v)},\,x_{D_v}
  \ \middle|\
  (m_e)_{e\in\operatorname{in}(v)},\,x_{P_v}
\right)\le bL_n.
\]
In particular, an internal processor can create only logarithmically much information beyond what it receives, and the terminal’s demanded strings must be recoverable from its local information with the same tolerance. The polynomial message-length convention is the source’s finite-scale convention; no polynomial-time encoding or decoding is required. Unlimited channels still carry finite messages.

Messages and the short local programs may depend on the entire instance. This is an existential coding question with logarithmic nonuniform descriptions, not a demand for one computable protocol that finds the messages from the strings alone. The acyclic graph specifies that incoming messages are available before outgoing messages are formed. There are no private random tapes, extra shared strings or uncharged side information beyond what is allowed in the displayed conditional descriptions.

The joint outgoing-tuple convention is equivalent, up to a pattern-dependent logarithmic constant, to bounding each outgoing message and requested output separately, because the pattern is fixed. Measuring finite capacity by message length is the explicit convention of the formal network model; its short-description formulation gives the same logarithmic-scale information interpretation. Allowing the constants to change absorbs the fixed universal-machine and tuple-encoding choices.''',
 answer_criterion=r'''Give a complete Lean-checked necessary-and-sufficient characterization of the finite source-demand patterns satisfying the quantified cut-sufficiency property. Equivalently, for its Boolean characteristic function \(\chi\), a real-valued function \(g\) is accepted if a complete Lean proof establishes \(|g(\mathcal N)-\chi(\mathcal N)|\le1/100\) for every finite pattern \(\mathcal N\). This approximation determines the classification by thresholding at \(1/2\); the supplied function need not itself be Boolean. Establish both directions of the classification. Classifying only a chosen special family, assuming independent source strings, restricting messages to linear codes, or replacing the model by Shannon block coding does not answer the full question. No algorithmic complexity requirement is imposed on the structural characterization. The numerical acceptance tolerance does not replace the separately quantified logarithmic tolerances inside the coding property.''',
 source_formulation=dict(
 text='After explaining cut conditions and examples where they do or do not suffice, Q12 asks which networks have information transmission completely characterized by those conditions.',
 caption='Paraphrase of Q12 in §6, editor-hosted PDF p. 14; local coding conventions are expanded using the cited algorithmic network framework.',
 citation='primary',format='editorial_paraphrase'),
 why='A cut counts how much information must enter a group of processors, but it does not describe whether the information can be packaged consistently for all destinations. The requested characterization would identify precisely when these numerical constraints capture the whole coding problem for individual correlated strings.',
 references=[
 ref('primary','27 Open Problems in Kolmogorov Complexity',
 'Andrei Romashchenko; Alexander Shen; Marius Zimand',2021,
 'https://www.cs.umd.edu/~gasarch/open/kolm.pdf',
 'SIGACT News 52(4), pp. 31–54; §6 pp. 11–14 in the editor-hosted PDF, Q12 p. 14, Figures 4–7; DOI 10.1145/3510382.3510389'),
 ref('model','Multisource Algorithmic Information Theory',
 'Alexander Shen',2006,'https://doi.org/10.4230/DagSemProc.06051.9',
 'Dagstuhl Seminar Proceedings 06051, pp. 1–12, published 31 July 2006; manuscript dated 10 March 2006, §§1 and 7–10'),
 ],
 context_blocks=[
 block('The question concerns individual finite strings. Their correlations are measured by conditional Kolmogorov complexity; no probability distribution on source strings is supplied.'),
 block('The formal network framework uses a directed acyclic graph and allows logarithmic descriptions at processors. It asks for the existence of compatible messages, so it is more permissive than requiring uniformly computable encoders with prescribed running time.','model'),
 block('The conditional-code network and the Slepian–Wolf source-reconstruction network are positive examples in the source: their cut constraints suffice at logarithmic precision. The source also records stronger efficient randomized encoding results for Slepian–Wolf with their own overhead conventions.'),
 block('The Gray–Wyner pattern is a negative example in general. Its three cut bounds only constrain the total information sent and the amounts reaching each receiver; for some correlated pairs these bounds do not guarantee the required common description.'),
 block('The placement and identity of requested strings are part of the pattern. Asking two terminals for different source strings can behave differently from broadcasting one common source, even when part of the underlying graph is similar.','model'),
 block('The source asks separately, in Q13 and Q14, about comparisons between Shannon and algorithmic coding. Those comparisons are not assumed by Q12 and are not folded into this characterization.'),
 ],
 progress=[
 progress('2006-07-31','The formal algorithmic network framework records cut necessity and contrasting positive and negative network examples.','model'),
 progress('2021','The survey poses the general classification as Q12, after the conditional-code and Slepian–Wolf examples.'),
 progress('2026-09-16','The review specifies source-demand patterns, all cuts, local descriptions and logarithmic tolerance, and finds no general classification in the bounded later-source check.'),
 ],
),notes,sources,status,summary=[
 'A network distributes correlated finite strings through directed channels with limited capacities.',
 'Each cut imposes a necessary bound on the information that must enter its vertices to meet their demands.',
 'The question asks exactly which fixed network patterns make all of these bounds sufficient for a coding solution.',
 'Codes are existential per-instance assignments with logarithmic local descriptions, without an efficient uniform-encoder requirement.',
 'The source gives both positive examples and networks where the cut bounds fail, leaving the general structural characterization open.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
