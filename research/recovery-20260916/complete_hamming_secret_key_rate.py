"""Apply the user's Hamming-family, maximal-key and normalized-rate choices."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0240';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied all three explicit user choices: Hamming-distance pairs of nearly maximal joint complexity, a key of maximal length up to logarithmic slack, and the asymptotic communication rate within pointwise absolute 1/100.',
 'Defined the Hamming layer by its exact cardinality, logarithmic deficiency with every fixed constant, and integer distance floor(theta*n), including all real relative distances from zero to one without a real-number oracle.',
 'Specified plain Kolmogorov complexity, the public exact complexity profile, independent private randomness, a public interactive bit protocol, worst-case communication and per-input joint success probability at least two thirds.',
 'Defined the rate through achievable eventual normalized bounds with an arbitrary positive rate slack; a different uniform protocol may depend on fixed parameters, but not on input length or the particular pair. No existence of a finite-length limit is assumed.',
 'Distinguished logarithmic key/secrecy losses from the 1/100 communication-rate tolerance, and Hamming-family results from finite-geometric lower bounds and Shannon average-input formulations.',
 'Preserved the prior importance assessment 63, replaced the unassessed placeholder significance, and recorded the bounded status check through September 2026.',
]
sources=[
 'Read Romashchenko–Shen–Zimand, 27 Open Problems in Kolmogorov Complexity, SIGACT News 52(4), 2021, source PDF p. 17, discussion preceding Q17 and Q17 itself. The example is strings at a specified Hamming distance; parties receive the complexity profile and seek maximal-length keys. The source does not fix one communication precision, so the user selected a normalized rate within 1/100.',
 'Read Gürpınar–Romashchenko, arXiv:2004.13411v6, submitted 9 May 2024, PDF header 13 May, §1 pp. 1–6 including Clarifications 1–3, equation (1), Theorem 2 and Remark 1; §3 Example 3 and §5 Theorems 3–4 pp. 24–27; concluding open-tradeoff discussion p. 28. The journal version removes the old polynomial bound on private randomness. Its exact secrecy convention is stronger than the card’s explicit logarithmic slack.',
 'The 2024 source’s representative Hamming example chooses theta with binary entropy one half. Its order-of-growth tradeoff does not determine the leading constant, and the conclusion explicitly records the remaining gap. The card’s whole distance curve and numerical precision are the selected editorial specialization of Q17, not a verbatim theorem from that example.',
 'Read Caillat-Grenier–Romashchenko–Zyavgarov, arXiv:2405.05831v3, revised 9 September 2025, §5 Theorem 4 pp. 15–16 and Remark 9: lower bounds for graph incidences with bounded common neighborhoods, including point–polynomial incidences. This was not substituted for a theorem covering Hamming layers.',
 'Read Romashchenko, MFCS 2025 Article 84, §§1.3 and 4.1 and the start of §4 in primary HTML. The new balanced-communication results concern incidences in finite projective planes; the stated treatment is deterministic or public-random, with the private-random extension left for further research. The author’s publication page records the 2026 Information and Computation version.',
 'Checked the author’s publication list updated 28 July 2026 and Matveev–Romashchenko arXiv:2602.16536v3, revised 1 July 2026, primary abstract: spectral conditions for the Ingleton inequality, not an announced determination of this Hamming communication-rate curve. No full proof audit of that paper was undertaken.',
 f'Bounded targeted searches through {DATE} found no verified pointwise 1/100 determination of the selected private-random, individual-input rate. No equivalence to an i.i.d. Shannon-source rate was assumed.',
]
complete(identifier,dict(
 title='Communication rate for secret-key agreement at fixed Hamming distance',
 criterion='resources',question_type='function',
 formal=r'''Determine the function
\[
 R:[0,1]\longrightarrow\mathbb R_{\ge0}
\]
to pointwise absolute accuracy \(1/100\). Here \(R(\theta)\) is the optimal asymptotic public-communication rate, in bits per input bit, for two parties with independent private randomness to agree on a secret key of maximal algorithmic-information length. Their inputs are pairs of \(n\)-bit strings at distance \(\lfloor\theta n\rfloor\) with nearly maximal joint Kolmogorov complexity in that Hamming layer. The precise family, secrecy condition and rate quantifiers are defined below.''',
 definitions=r'''Fix an optimal universal plain description machine \(U\) and effective binary encodings of finite tuples. Write \(C(a\mid b)\) for the length of the shortest program making \(U\), with auxiliary input \(b\), output \(a\); write \(C(a)\) when there is no auxiliary input. Joint complexity uses the fixed tuple encoding. All logarithms are base two. The algorithmic mutual information of two strings is
\[
 I(x:y)=C(x)+C(y)-C(x,y).
\]
Let \(\ell_n=\lceil\log_2(n+2)\rceil\).

For every real \(\theta\in[0,1]\), integer \(n\ge1\) and fixed integer \(c\ge1\), put \(t=\lfloor\theta n\rfloor\). The promised family \(\mathcal F_{n,\theta,c}\) consists of all ordered pairs \(x,y\in\{0,1\}^n\) satisfying
\[
 \operatorname{dist}_H(x,y)=t,\qquad
 C(x,y\mid n,t)\ge
 \left\lfloor\log_2\!\left(2^n\binom nt\right)\right\rfloor-c\ell_n.
\]
The Hamming distance counts coordinates where the bits differ. There are exactly \(2^n\binom nt\) pairs in the layer; the displayed condition makes the permitted complexity deficiency explicit. The constant \(c\) is fixed as \(n\) grows, and the rate must cover every such constant. The input pair is fixed, not sampled by the protocol from a probability distribution.

Alice receives \(x\), Bob receives \(y\), and both receive the public data
\[
 q=(n,t,C(x),C(y),C(x,y)).
\]
These exact complexity values are supplied as a promise, not computed by the parties. An eavesdropper also knows \(q\) and the full finite description of the protocol \(\Pi\), but receives neither private input nor either private random tape. There is no other shared secret or correlated resource. Each party has an independent tape of independent fair random bits. Random bits sent over the channel become public.

A protocol is a pair of uniform classical algorithms with unrestricted finite computation. One fixed finite program works over all input lengths; it has no oracle for Kolmogorov complexity or for a real parameter. The parties communicate by a public binary protocol: the next speaker and public termination are determined by the public data and the transcript so far, while each sent bit can depend on the sender's private input and coins. All transmitted bits count, including any control or framing bits. Timing supplies no extra information. There is no bound on the number of rounds, on local running time or on the number of private random bits, but every execution on finite inputs and every pair of random tapes must terminate after finitely many steps. Each party then outputs a finite binary string or a failure symbol. Totality is required even outside the promise; correctness is required only on promised pairs with the true profile.

For fixed \(\theta,c\), a protocol is valid if there is a constant \(K>0\) such that, for every \(n\ge1\) and every \((x,y)\in\mathcal F_{n,\theta,c}\), with probability at least \(2/3\) over the private coins the two outputs are the same string \(Z\) and simultaneously
\[
 \bigl||Z|-\max\{0,I(x:y)\}\bigr|\le K\ell_n,
 \qquad C(Z\mid T,q,\Pi)\ge |Z|-K\ell_n.
\]
Here \(T\) is the complete public transcript. Thus the key has maximal length up to logarithmic loss and remains nearly incompressible given everything public. Agreement, length and secrecy are one joint success event for each input pair. Secrecy is defined by description length, without a computational bound on the observer. It is not a claim of statistical uniformity for a distribution of inputs.

Let \(W_{\Pi,\theta,c}(n)\) be the supremum of the total number of transmitted bits over all pairs in \(\mathcal F_{n,\theta,c}\) and all private random tapes, including unsuccessful executions. The supremum of an empty family is taken as zero. Communication is a worst-case cost, not an expectation or a cost conditioned on successful agreement.

A real rate \(r\ge0\) is achievable at \(\theta\) if, for every integer \(c\ge1\) and every real \(\eta>0\), there exist a valid uniform protocol \(\Pi\) and an integer \(n_0\ge1\) such that
\[
 W_{\Pi,\theta,c}(n)\le(r+\eta)n\quad\text{for every integer }n\ge n_0.
\]
Set \(R(\theta)=\inf\{r\ge0:r\text{ is achievable at }\theta\}\). General secret-key agreement bounds ensure this set is nonempty and the infimum is finite. This definition does not assume that a finite-length optimum divided by \(n\) has a limit, or that the infimum is attained.

The protocol, its logarithmic-loss constant \(K\) and the threshold \(n_0\) may depend on the fixed parameters \(\theta,c,\eta\). They cannot depend on \(n\) or the particular input pair. Even for irrational \(\theta\), an admissible protocol has a finite description and sees the integer \(t\), not a real-number oracle. No effective procedure for selecting protocols from these fixed parameters is required. The unit of the requested function is total bits sent in both directions divided by the length \(n\) of one party's input, not by the combined length \(2n\).

The \(O(\log n)\) key and secrecy allowances are fixed by the constant \(K\) in each protocol. They do not permit losing a positive linear fraction of the key. Conversely, the requested accuracy \(1/100\) is in the asymptotic communication rate; it does not request a finite-length communication estimate with additive \(O(\log n)\) error.''',
 answer_criterion=r'''Supply a mathematically specified function \(a:[0,1]\to\mathbb R\) and a complete Lean-checked proof that
\[
 |a(\theta)-R(\theta)|\le1/100\qquad\text{for every real }\theta\in[0,1].
\]
Pointwise certified bounds \(L(\theta)\le R(\theta)\le U(\theta)\), with width at most \(1/50\) everywhere, qualify via their midpoint. An exact formula or another certified mathematical characterization meeting the accuracy also qualifies; a closed form, decimal table or efficient evaluation procedure is not required.

Upper and lower control must use the stated family, maximal-key criterion, private randomness and worst-case communication. Bounds up to unspecified multiplicative constants, a proof at just one distance, numerical evidence, a different key-length tradeoff, or a result that averages success over random inputs does not suffice. Merely restating the defining infimum is not a determination. Any transfer from a Shannon-source theorem or a different pair family must itself be proved for this model.''',
 why='Determine how the geometry of correlated binary data controls the public communication needed to realize all of its algorithmic mutual information as a shared secret. A sharp rate distinguishes inputs with the same information profile but different communication requirements.',
 source_formulation=dict(text='Question 17 asks for optimal communication in important examples of algorithmic secret-key agreement, explicitly suggesting strings at a given Hamming distance. The user selected nearly maximally complex pairs in that layer, a key of maximal information length, and the leading communication rate with pointwise absolute accuracy 1/100.',caption='Paraphrase of 27 Open Problems in Kolmogorov Complexity, Q17 and preceding discussion, specialized by the user’s three explicit scope choices on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','27 Open Problems in Kolmogorov Complexity','Andrei Romashchenko; Alexander Shen; Marius Zimand',2021,'https://www.cs.umd.edu/~gasarch/open/kolm.pdf','SIGACT News 52(4), pp. 31–54; source PDF p. 17, Q17 and preceding secret-key discussion'),
 ref('communication','Communication Complexity of the Secret Key Agreement in Algorithmic Information Theory','Emirhan Gürpınar; Andrei Romashchenko',2024,'https://arxiv.org/abs/2004.13411v6','Version 6, 9 May 2024; §1 Clarifications 1–3 and Remark 1; §3 Example 3; §5 Theorems 3–4 pp. 24–27; concluding discussion p. 28. TOCT 16(3), Article 13'),
 ref('mixing','Common Information in Well-Mixing Graphs and Applications to Information-Theoretic Cryptography','Geoffroy Caillat-Grenier; Andrei Romashchenko; Rustam Zyavgarov',2025,'https://arxiv.org/abs/2405.05831v3','Version 3, 9 September 2025, extending ITW 2024; §5 Theorem 4 pp. 15–16 and Remark 9, bounded-common-neighborhood graph incidences'),
 ref('algebraic','Algebraic Barriers to Halving Algorithmic Information Quantities in Correlated Strings','Andrei Romashchenko',2025,'https://doi.org/10.4230/LIPIcs.MFCS.2025.84','MFCS 2025 Article 84; §§1.3 and 4.1, finite projective-plane inputs; §4 explicitly treats deterministic and public-random protocols'),
 ],
 context_blocks=[
 block('The source makes maximal key length operational: the parties can turn their algorithmic mutual information into a shared secret, provided they receive the small complexity profile as auxiliary data. It separately asks how much communication particular input families require.'),
 block(r'The general upper bound is \(\min\{C(x\mid y),C(y\mid x)\}+O(\log n)\) communicated bits. Worst-case examples over all pairs make this bound tight, but that does not automatically establish the optimal rate for the Hamming family.','communication'),
 block(r'For a representative fixed Hamming distance, the 2024 source proves order-of-growth tradeoffs between communication and key length and explicitly leaves a gap between their constants. Such \(\Theta(n)\) information does not determine the normalized rate within \(1/100\).','communication'),
 block('The model is about individual input strings: every promised pair must have a high probability of success over the parties’ private coins. An average guarantee for independent samples from a probability distribution is a different quantifier.','communication'),
 block('The later graph-incidence results show that full-key communication can be forced onto one side in certain families. Their hypotheses do not establish the same conclusion for Hamming layers.','mixing'),
 block('The algebraic results concern balanced communication for incidences in finite projective planes. Their stated deterministic or public-random setting and geometric input family differ from the private-random Hamming-rate target.','algebraic'),
 ],
 progress=[progress('2021','The open-problems column explicitly asks for the communication cost on Hamming-distance input pairs.'),progress('2024-05-09','The extended paper removes the polynomial restriction on private randomness and records a remaining constant-factor gap in its Hamming example.','communication'),progress('2025-09-09','The revised graph-incidence paper gives additional full-key communication lower bounds for its stated graph families.','mixing'),progress('2025','Balanced communication is further analyzed for finite projective-plane inputs.','algebraic')],
),notes,sources,'The 2024 full paper explicitly leaves the sharp Hamming-family communication tradeoff unresolved. The checked 2025–2026 developments concern other input families or related information inequalities. Bounded primary-source checks through 17 September 2026 found no verified determination of the selected private-random maximal-key communication-rate function within pointwise absolute error 1/100. This does not certify an exhaustive literature search or independently verify every cited proof.',summary=[
 'Alice and Bob hold binary strings at a specified Hamming distance and may communicate on a channel observed by an eavesdropper.',
 'The input pair must have nearly the largest Kolmogorov complexity possible in that distance layer, and its complexity profile is public.',
 'Using independent private randomness, they must agree on a key whose length is their mutual information up to logarithmic loss and which remains nearly incompressible given the transcript.',
 'The target is the smallest asymptotic worst-case number of communicated bits per input bit, as a function of relative distance.',
 'An answer must prove the whole rate function within absolute error 1/100 in Lean, with success guaranteed separately for every promised input pair.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
choices=ROOT/'research/recovery-20260916/further-scope-choices.json'
rows=json.loads(choices.read_text()); row=next(r for r in rows if r['id']==identifier)
row.update(state='applied',applied_on=DATE)
choices.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
