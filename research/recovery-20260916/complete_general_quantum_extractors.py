"""Complete the user-selected universal quantitative quantum stability question."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-5202'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user choice of error C*m*sqrt(epsilon) and conditional min-entropy threshold C*(k+log2(1/epsilon)), with one universal constant.',
 'Used the general weak seeded-extractor formulation stated in the cited operator-space paper, explicitly defining whether the seed is discarded and how strong extractors embed with the seed counted in output length.',
 'Defined the entire classical-quantum state model, arbitrary finite side-information dimension, guessing min-entropy, seed independence and trace-distance convention.',
 'Quantified over all finite extractor functions, not just efficiently computable constructions, and kept the threshold untruncated when it exceeds input length.',
 'Separated construction-specific quantum guarantees, dimension-dependent generic bounds and high-entropy bounds from the selected universal output-linear error estimate.',
 'Assessed importance individually at 83 and required a complete Lean-checked proof or a refutation of every possible universal constant.',
]
sources=[
 'Read the stored full text of Arnon-Friedman–Portmann–Scholz, TQC 2016 Article 2, introduction p. 2:2 and footnote 1. The open seeded multi-bit question is distinct from this paper’s multi-source Markov-model theorem; the footnote points to the quantitative compatibility of positive bounds with known negative examples.',
 'Read Berta–Fawzi–Scholz, Quantum-proof randomness extractors via operator space theory, arXiv:1409.3563v3, 4 May 2017 (published version), §I.A pp. 2–3, equations (1)–(8), the displayed open question on p. 3, §II.A Theorems II.3/II.4 pp. 6–7 and §III p. 9. Verified IEEE Transactions on Information Theory 63(4), 2480–2503 (2017), DOI 10.1109/TIT.2016.2627531. The paper uses full trace/ell1 norms; the half-norm convention below changes only universal constants, with the additional additive entropy constant absorbed since epsilon is at most one half.',
 'Read Foreman–Yeung–Edgington–Curchod, Cryptomite, arXiv:2402.09481v3, corrected 26 November 2025, abstract, §3.1 and Definition 4 pp. 10–11, §3.2.1 and the individual Circulant construction statement. Checked Quantum 9, 1584, published 8 January 2025, DOI 10.22331/q-2025-01-08-1584. This is a collection of specific constructions and source-model extensions, not a theorem giving the selected universal stability bound.',
 f'Bounded searches of primary papers and author publication records through {DATE} found specific quantum-proof constructions and generic bounds with other parameter dependence, not a proof or refutation of the selected universal estimate. Later-paper search metadata was not treated as a new publication date for old results.',
]
status='The checked operator-space source states this quantitative classical-to-quantum stability question as open. Its generic small-output and high-entropy bounds do not imply the requested estimate in all parameter regimes. The checked later construction literature, including the corrected November 2025 Cryptomite version, does not supply a resolution of this universal statement. Known failures of parameter-preserving quantum security do not by themselves refute the allowed entropy and error losses.'
complete(identifier,dict(
 title='Universal quantum stability of seeded extractors with output-linear error loss',
 criterion='resources',question_type='yes_no',year=2025,is_new=False,
 formal=r'''Is there a universal integer \(C\ge1\) such that every classical \((k,\varepsilon)\) seeded extractor
\[
 F:\{0,1\}^n\times\{0,1\}^d\longrightarrow\{0,1\}^m
\]
is quantum-proof with conditional min-entropy requirement
\[
 K=C\bigl(k+\log_2(1/\varepsilon)\bigr)
\]
and trace-distance error at most \(C m\sqrt{\varepsilon}\)? Quantify over all integers \(n,m\ge1\), \(d\ge0\), real \(0\le k\le n\), and \(0<\varepsilon\le1/2\). Use the general, or weak, seeded-extractor definition below: the uniform independent seed is averaged out, and \(m\) counts the entire retained classical output.''',
 definitions=r'''Write \(U_t\) for the uniform distribution on \(\{0,1\}^t\), including the unique empty string when \(t=0\). The min-entropy of a distribution \(P_X\) is \(H_{\min}(X)=-\log_2\max_x P_X(x)\). A function \(F\) is a classical \((k,\varepsilon)\) seeded extractor if, for every distribution \(X\) on \(n\) bits satisfying \(H_{\min}(X)\ge k\), and an independent seed \(S\sim U_d\),
\[
 \frac12\sum_{z\in\{0,1\}^m}
 \left|\Pr[F(X,S)=z]-2^{-m}\right|\le\varepsilon.
\]
The same function must work for all such input distributions. The question imposes no construction time, circuit-size, seed-length or output-length bound beyond these definitions. In particular, the quantified class includes arbitrary finite truth tables, not only named or efficiently evaluable extractors.

A classical-quantum input with side information \(E\) is a density matrix
\[
 \rho_{XE}=\sum_{x\in\{0,1\}^n}|x\rangle\langle x|\otimes\rho_E^x,
 \qquad \rho_E^x\succeq0,\qquad
 \sum_x\operatorname{Tr}\rho_E^x=1,
\]
on the classical register \(X\) and an arbitrary finite-dimensional complex Hilbert space \(E\). Here the matrices \(\rho_E^x\) include their probability weights, and \(\rho_E=\sum_x\rho_E^x\). There is no bound on the dimension of \(E\), computational restriction on the adversary or rational-entry assumption. Define
\[
 p_{\mathrm{guess}}(X\mid E)_\rho
 =\max_{\substack{M_x\succeq0\\\sum_xM_x=I_E}}
   \sum_x\operatorname{Tr}(M_x\rho_E^x),\qquad
 H_{\min}(X\mid E)_\rho=-\log_2p_{\mathrm{guess}}(X\mid E)_\rho.
\]
The maximization is over all measurements with an outcome labeled by each possible input string: each \(M_x\) is positive semidefinite and their sum is the identity. This is unsmoothed conditional min-entropy, measuring the best probability of guessing the whole input.

The seed is uniform and independent of the entire state \(\rho_{XE}\), so the initial joint state is \(\rho_{XE}\otimes\tau_d\), where \(\tau_t=2^{-t}\sum_y|y\rangle\langle y|\) is the uniform classical state on \(t\) bits. After evaluating \(F\) and discarding \(X,S\), the retained state is
\[
 \rho_{ZE}=2^{-d}\sum_{s\in\{0,1\}^d}\sum_{x\in\{0,1\}^n}
 |F(x,s)\rangle\langle F(x,s)|\otimes\rho_E^x.
\]
Being quantum-proof at parameters \((K,\eta)\) means that every such input with \(H_{\min}(X\mid E)_\rho\ge K\) satisfies
\[
 \frac12\|\rho_{ZE}-\tau_m\otimes\rho_E\|_1\le\eta,
 \qquad \|A\|_1=\operatorname{Tr}\sqrt{A^\dagger A}.
\]
Thus the ideal output is uniform and independent of all side information, and security is measured against unrestricted measurements, not efficient distinguishers.

The entropy requirement is literally \(C(k+\log_2(1/\varepsilon))\), without rounding or truncation to \(n\). If it exceeds \(n\), no normalized classical-quantum input meets the premise and the implication is vacuous. If \(Cm\sqrt{\varepsilon}\ge1\), the error bound is automatic because trace distance between states is at most one. The same constant \(C\) must work across all nonvacuous parameter regimes and all dimensions. Allowing separate universal constants for entropy and error would be equivalent by taking their maximum and then increasing to an integer.

For comparison, a strong seeded extractor \(G\) retains its seed and asks that \((S,G(X,S))\) be close to a uniform pair, also independent of \(E\) in the quantum case. It is represented here by \(F(x,s)=(s,G(x,s))\). In that representation \(m=d+m'\), where \(m'\) is the number of newly extracted bits. A stronger bound depending only on \(m'\) while revealing an arbitrarily long seed is not silently substituted for the general output-length formulation above. No independent-source or Markov condition is imposed on the single weak source and its quantum side information.''',
 answer_criterion=r'''Give a complete Lean-checked proof that one universal constant satisfies the stated implication, or a complete Lean-checked refutation. A refutation must establish that for every candidate constant there are parameters, a classically valid extractor and an allowed classical-quantum input meeting the increased entropy threshold whose output exceeds the claimed error. Failure at the original entropy threshold or with unchanged error is insufficient.

The theorem must cover arbitrary side-information dimension and arbitrary extractor functions. Proving it only for a particular construction, bounded quantum storage, one output bit, very high input entropy or a multi-source Markov model does not settle the question. There is no requested numerical approximation; the quantified error inequality itself is the exact target.''',
 source_formulation=dict(text='The TQC source asks whether arbitrary multi-bit seeded extractors retain security with quantum side information and points to the operator-space work. That work makes a quantitative conjecture: increasing the entropy requirement by a universal factor and a logarithmic error term should suffice for an error bounded by output length times the square root of the classical error, up to a universal constant.',caption='Paraphrase of Arnon-Friedman–Portmann–Scholz, TQC 2016 p. 2:2 and footnote 1, and Berta–Fawzi–Scholz, arXiv:1409.3563v3 §I.A p. 3; quantitative target selected by the user on 17 September 2026.',citation='operators',format='editorial_paraphrase'),
 importance=dict(score=83,method='editorial',reason='A universal stability theorem would transfer a broad class of classical randomness extractors to quantum side-information settings with controlled parameter loss; a refutation would expose a structural limit on that transfer.',basis='Individual assessment of the universal quantitative target and its relation to privacy amplification, rather than the existence of individual quantum-proof constructions.'),
 why='An adversary can store information about a weak random input in a quantum state. The question asks whether a classical extractor’s guarantee alone controls how much this changes the quality of its output, with a loss that grows only linearly in output length.',
 references=[
 ref('primary','Quantum-Proof Multi-Source Randomness Extractors in the Markov Model','Rotem Arnon-Friedman; Christopher Portmann; Volkher B. Scholz',2016,'https://doi.org/10.4230/LIPIcs.TQC.2016.2','TQC 2016, LIPIcs 61, Article 2; introduction p. 2:2 and footnote 1, seeded-extractor question distinct from the paper’s multi-source result'),
 ref('operators','Quantum-proof randomness extractors via operator space theory','Mario Berta; Omar Fawzi; Volkher B. Scholz',2017,'https://arxiv.org/abs/1409.3563v3','Published version, 4 May 2017; §I.A pp. 2–3, equations (1)–(8) and displayed open question; Theorems II.3/II.4 pp. 6–7; §III p. 9. IEEE TIT 63(4), 2480–2503; DOI 10.1109/TIT.2016.2627531'),
 ref('cryptomite','Cryptomite: A versatile and user-friendly library of randomness extractors','Cameron Foreman; Richie Yeung; Alec Edgington; Florian J. Curchod',2025,'https://arxiv.org/abs/2402.09481v3','Corrected version 3, 26 November 2025; abstract, §3.1 and Definition 4 pp. 10–11, §3.2.1; Quantum 9, 1584, published 8 January 2025, DOI 10.22331/q-2025-01-08-1584'),
 ],
 context_blocks=[
 block('Classical side information can be accommodated by a modest loss in entropy and error for any extractor. Quantum side information does not admit that immediate transfer, and known examples already rule out simply keeping the original parameters. The present question explicitly allows larger losses.','operators'),
 block('The operator-space paper gives generic quantum bounds for small outputs and for input entropy very close to its maximum. Their dependence on output length or the entropy deficit leaves the selected all-parameter estimate unresolved.','operators'),
 block('Several structured constructions, including suitable hashing and Trevisan-based extractors, have quantum-security proofs. Their existence does not establish the same guarantee for every function that passes the classical extractor test.','operators'),
 block('The corrected Cryptomite paper provides practical implementations and parameter analyses for specific extractors. Its construction and source-model guarantees illustrate useful positive results without supplying the universal stability statement here.','cryptomite'),
 ],
 progress=[
 progress('2016','The TQC paper identifies the general seeded multi-bit security question while proving a separate result for multi-source extractors in the Markov model.'),
 progress('2017-05-04','The published operator-space version states the quantitative open question and records generic small-output and high-entropy bounds.','operators'),
 progress('2025-11-26','The corrected Cryptomite preprint supplies implementations and construction-specific quantum guarantees, without a universal classical-to-quantum stability theorem.','cryptomite'),
 ],
),notes,sources,status,summary=[
 'The question asks whether every classical seeded extractor remains secure against arbitrary finite-dimensional quantum side information with a universal quantitative loss.',
 'The selected target increases required min-entropy to C times the sum of k and log base two of one over epsilon, and allows trace-distance error at most C times m times the square root of epsilon.',
 'One constant must work for every extractor and all parameters, without a bound on the adversary’s computation or storage dimension.',
 'The seed is averaged out in the general formulation; if retained as part of a strong extractor’s output, its bits count toward the output length m.',
 'Specific quantum-proof constructions and known parameter-preserving counterexamples do not settle this claim, which requires a complete Lean-checked proof or refutation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
