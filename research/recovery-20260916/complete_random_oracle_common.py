"""Complete logarithmic common-information extraction with an infinite random oracle."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0279';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the selected probability at least 2/3 over infinite fair independent oracle bits and logarithmic losses in the finite input-length bound n.',
 'Made the tolerance quantifiers explicit: for every input tolerance coefficient c there must be one output coefficient d working for all n and all input pairs.',
 'Required extraction of all mutual information up to logarithmic error; the witness and its short oracle programs may depend on the oracle, with no common extraction algorithm or witness assumed.',
 'Defined plain oracle Kolmogorov complexity with one fixed optimal uniformly relativizing interpreter, fixed pair coding, and no time, query or witness-length bound.',
 'Distinguished the finite-word auxiliary-information theorems from the infinite-oracle question, whose logarithmic tolerance cannot depend on the length or complexity of an arbitrarily long oracle prefix.',
 'Recorded a 2026 author claim about general Gray–Wyner profiles as unverified and not established to imply or refute this full-extraction statement; its full paper was not accessible in this check.',
 'Preserved importance 63 and required a complete Lean-checked proof of the quantified implication or its actual negation.',
]
sources=[
 'Read Alexander Shen’s §4.8, Extraction of mutual information about two strings, in Dagstuhl Seminar 12021 report, DOI 10.4230/DagRep.2.1.19, printed p. 35. The first question asks whether full extractability relative to a random oracle implies full extractability without it; the subsequent half-complexity oracle question is a separate problem and is not included.',
 'Read Muchnik–Romashchenko, A Random Oracle Does not Help Extract the Mutual Information, MFCS 2008 author PDF, pp. 1–3 and conclusion pp. 9–10: oracle y is a finite word, N includes its complexity, Conjecture 1 has logarithmic thresholds, Theorem 2 sublinear thresholds, and the conclusion asks separately about infinite oracles.',
 'Read the expanded author version of Muchnik–Romashchenko, Stability of Properties of Kolmogorov Complexity under Relativization, Problems of Information Transmission 46(1), 38–61 (2010): Conjecture 2 and Theorem 2 author pp. 3–4, Theorem 5 on stochastic tuples author pp. 6–7, and §7 author p. 22. The conclusion explicitly states that the paper has no results about infinite-oracle relativization.',
 'Read Romashchenko–Shen–Zimand, 27 Open Problems in Kolmogorov Complexity, SIGACT News 52(4), 31–54 (2021), DOI 10.1145/3510382.3510389, author column PDF §4 Q9 p. 10 and its preceding definitions. Q9 is the broader random-oracle stability question for information profiles, not an assertion that the 2010 finite-oracle theorem settled the 2012 infinite-oracle problem.',
 'Checked the indexed primary SSRN abstract of Tolga Topal, Extracting Common Information: Solutions to Q7, Q8, and Q9 of the 27 Open Problems, written 4 August 2026, posted 13 August 2026, DOI 10.2139/ssrn.7251558. It claims a pair and universal machine changing the Gray–Wyner profile. Direct retrieval returned HTTP 403; no full proof was available for checking tolerance robustness, fixed-machine quantifiers, or an implication for full common-information extraction. The claim is not recorded as a resolution.',
 f'Bounded later-work checks through {DATE} found no verified proof or refutation of the selected implication. Current status is marked uncertain because the related recent claim has not been fully assessed.',
]
complete(identifier,dict(
 title='Random-oracle invariance of fully extractable common information',criterion='reductions',question_type='yes_no',year=2012,is_new=False,status='uncertain',
 formal=r'''Is the following implication true? For every integer \(c\ge1\) there exists an integer \(d\ge1\) such that for every \(n\ge2\) and every pair of binary words \(x,y\) with \(|x|,|y|\le n\), put \(\ell_n=\lceil\log_2(n+2)\rceil\). If
\[
 \Pr_{X}\!\left[\exists b\in\{0,1\}^*:\
 \begin{array}{l}
 C^X(b\mid x)\le c\ell_n,\quad C^X(b\mid y)\le c\ell_n,\\
 |C^X(b)-I^X(x:y)|\le c\ell_n
 \end{array}\right]\ge2/3,
\]
where \(X\) is an infinite fair random binary oracle, must there exist a finite binary word \(z\) such that
\[
 C(z\mid x)\le d\ell_n,\qquad C(z\mid y)\le d\ell_n,\qquad
 |C(z)-I(x:y)|\le d\ell_n\ ?
\]
The coefficient \(d\) may depend on \(c\) and the fixed description conventions, but not on \(n,x,y\).''',
 definitions=r'''Fix one optimal plain universal oracle description machine \(U\). Its inputs are a finite binary program \(p\), a finite binary auxiliary word \(v\), and access to an oracle \(X\in\{0,1\}^{\mathbb N}\). It can query any natural-number position of \(X\); a halting computation makes finitely many queries and prints a finite word. There is no running-time, query-count or largest-query bound. Plain programs need not form a prefix-free set.

Optimality is uniform over oracles: for each other oracle description machine, a fixed finite compiler prefix simulates it under every \(X\), with additive program-length overhead independent of \(X,p,v\). Fix the ordinary no-oracle machine to be \(U\) with the all-zero computable oracle. Define
\[
 C^X(u\mid v)=\min\{|p|:U^X(p,v)=u\},\qquad C^X(u)=C^X(u\mid\epsilon),
\]
where \(\epsilon\) is the empty auxiliary word. Write \(C\) for the same definitions with the fixed all-zero oracle. Thus ordinary complexity is not measured using a different machine chosen for each input pair.

Fix a computable injective encoding \(\langle u,v\rangle\) of pairs, with computable decoding, and set
\[
 I^X(x:y)=C^X(x)+C^X(y)-C^X(\langle x,y\rangle),\qquad
 I(x:y)=C(x)+C(y)-C(\langle x,y\rangle).
\]
These are the stated integer expressions; small negative values caused by description conventions are not silently truncated. The permitted logarithmic errors absorb the usual fixed-machine changes. Bit length is denoted by \(|u|\), and every logarithm here is to base two.

The random oracle has independent unbiased bits: for every fixed binary prefix of length \(r\), the probability of that prefix is \(2^{-r}\). It is sampled independently of the fixed words \(x,y\). Probability refers to this product measure, not a finite random string, a random permutation or a computably generated sequence. The probability event in the statement is interpreted as an ordinary measurable event on this space; complexities and halting outputs are defined by the oracle computations just specified.

The existential witness \(b\), and the short programs showing its conditional complexities, may depend on \(X,x,y\). In particular, \(\Pr_X[\exists b\,\cdots]\) does not mean that one fixed \(b\) works for two thirds of the oracles. No uniform extractor must produce these witnesses. Their finite lengths and the positions queried from \(X\) can be arbitrarily large. What is required to be near the mutual information is the oracle-relative complexity \(C^X(b)\), not the unrelativized complexity or literal length of \(b\).

The conclusion asks only for existence of an ordinary common-information word \(z\). It need not equal any oracle-dependent witness. Its short descriptions from \(x\) and \(y\) receive no oracle and no transcript of communication. In both premise and conclusion the slack is measured by the original input-length bound \(n\), even if a witness or a finite prefix of the oracle used by a computation is much longer. The quantifier over \(d\) is outside the choice of inputs, so a constant chosen separately to cover each finite example does not establish the statement.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed implication with quantifiers \(\forall c\,\exists d\,\forall n,x,y\), or a complete Lean-checked refutation. A refutation must give some fixed \(c\) such that every proposed \(d\) fails on some pair meeting the two-thirds oracle-extraction premise but lacking an ordinary witness with that \(d\)-logarithmic loss.

Exact changes of a complexity value or information profile on a single fixed pair do not refute this asymptotic statement: the failure must survive every allowed output coefficient. Nor is it sufficient to alter some other part of a profile without changing full extractability. A theorem for finite auxiliary strings whose error depends on their complexity, or a conclusion with merely sublinear rather than logarithmic loss, does not meet the target. The assertion and the selected probability threshold require proof, not numerical tolerance.''',
 source_formulation=dict(text='Shen asks whether two words having fully extractable mutual information relative to a random oracle implies that the same holds without an oracle. The user selected success for at least two thirds of the infinite fair oracles and logarithmic losses in the finite input lengths.',caption='Paraphrase of Dagstuhl Seminar 12021 report §4.8, printed p. 35; probability and loss conventions selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='Mutual information is a number; representing it by a word recoverable from either input is a stronger property. This asks whether an unlimited independent random resource can change that property, even though ordinary complexity values are stable up to small losses with high probability.',
 references=[
 ref('primary','Extraction of mutual information about two strings, in Computability, Complexity and Randomness','Alexander Shen',2012,'https://doi.org/10.4230/DagRep.2.1.19','Dagstuhl Seminar 12021, held 8–13 January 2012; §4.8 printed p. 35, first question only; the source uses approximate equalities without a fixed probability threshold'),
 ref('finite','Stability of Properties of Kolmogorov Complexity under Relativization','An. A. Muchnik; A. E. Romashchenko',2010,'https://www.lirmm.fr/~romashchen/ps/itp2010.pdf','Problems of Information Transmission 46(1), 38–61; author version Conjecture 2 and Theorem 2 pp. 3–4, Theorem 5 pp. 6–7, §7 p. 22; finite auxiliary-word size parameter and explicit infinite-oracle limitation'),
 ref('survey','27 Open Problems in Kolmogorov Complexity','Andrei Romashchenko; Alexander Shen; Marius Zimand',2021,'https://www.cs.umd.edu/~gasarch/open/kolm.pdf','SIGACT News 52(4), 31–54, DOI 10.1145/3510382.3510389; author column §4 Q9 p. 10; broader information-profile stability formulation'),
 ref('claim','Extracting Common Information: Solutions to Q7, Q8, and Q9 of the 27 Open Problems','Tolga Topal',2026,'https://doi.org/10.2139/ssrn.7251558','Author manuscript written 4 August 2026, SSRN posting 13 August 2026; indexed abstract only; full paper inaccessible during this check, and no matching logarithmic-loss full-extraction conclusion verified'),
 ],
 context_blocks=[
 block('For a fixed finite tuple, adding independent random oracle access ordinarily changes its complexity values only by small amounts with high probability. The source asks whether the existence of a further common-information witness has the same stability.'),
 block('The 2010 paper proves finite-auxiliary-word results, including a sublinear-loss theorem and stronger statements for stochastic tuples. Its error parameter includes the auxiliary word’s complexity, and its conclusion explicitly says it has no results about infinite oracles.','finite'),
 block('The 2021 survey asks the broader stability question for Gray–Wyner and other profiles. Changing an arbitrary profile coordinate is not automatically the same as changing whether all mutual information can be extracted.','survey'),
 block('An August 2026 manuscript claims a random-oracle counterexample for Gray–Wyner profiles using a pair of words and a universal machine. Only its indexed abstract was accessible in this review. It is not established here that the claim survives the quantified logarithmic tolerance or resolves this particular full-extraction question.','claim'),
 ],
 progress=[progress('2010','Published finite-auxiliary-word stability results leave infinite-oracle relativization untreated.','finite'),progress('2012','The Dagstuhl report poses the full-extraction question for a random oracle.'),progress('2021','A survey records the broader random-oracle information-profile question.','survey'),progress('2026-08-13','SSRN posts a claimed result on broader Gray–Wyner-profile questions; only the abstract was checked, so it is not accepted as a resolution of this target.','claim')],
),notes,sources,'The original infinite-oracle full-extraction question is distinct from the proved finite-auxiliary-word results. A related August 2026 manuscript claims a Gray–Wyner-profile counterexample, but only its abstract was accessible and no implication for this quantified logarithmic-loss target was verified. The card remains active with uncertain current status; this review neither certifies nor rejects the uninspected proof.',summary=[
 'Two words have fully extractable common information when a word containing almost all their mutual information has short descriptions from either one.',
 'The premise allows such an extraction for at least two thirds of independent infinite fair random oracles.',
 'The question is whether an extraction must then exist without any oracle, with losses still logarithmic in the input lengths.',
 'Oracle-dependent witnesses may vary and use arbitrarily many oracle positions, so finite auxiliary-word results do not directly supply the required bound.',
 'A complete Lean-checked proof or refutation must respect the uniform loss constants; a recent broader profile claim has not been verified to settle this statement.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());next(r for r in a if r['id']==identifier).update(state='applied',applied_on=DATE);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
