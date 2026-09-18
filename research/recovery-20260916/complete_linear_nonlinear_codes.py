"""Specify a positive asymptotic binary rate separation."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4968';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Do nonlinear binary codes have a strictly better asymptotic rate?',
 status='source_open',criterion='construction',question_type='yes_no',
 formal=r'''Does there exist a fixed real \(\delta\in(0,1/2)\) such that
\[
R_2(\delta)>R_2^{\mathrm{lin}}(\delta),
\]
where these are the optimal asymptotic rates of arbitrary binary codes and binary linear codes, respectively, at relative minimum Hamming distance \(\delta\), as defined below? Any fixed strictly positive gap qualifies.''',
 definitions=r'''For integers \(n\ge1\) and \(0\le d\le n\), let
\[
A_2(n,d)=\max\{|C|:\varnothing\ne C\subseteq\{0,1\}^n,
\ \forall x\ne y\in C,\ \Delta(x,y)\ge d\},
\]
where \(\Delta(x,y)=|\{j\in\{1,\ldots,n\}:x_j\ne y_j\}|\). Let \(A_2^{\mathrm{lin}}(n,d)\) be the same maximum restricted to vector subspaces \(C\le\mathbb F_2^n\), where addition is coordinatewise modulo two. The one-word code is allowed, and its pairwise distance condition is vacuous. Both finite maxima are well defined.

For a fixed real \(\delta\in(0,1/2)\), define
\[
R_2(\delta)=\limsup_{n\to\infty}\frac{\log_2 A_2(n,\lfloor\delta n\rfloor)}{n},\qquad
R_2^{\mathrm{lin}}(\delta)=\limsup_{n\to\infty}\frac{\log_2 A_2^{\mathrm{lin}}(n,\lfloor\delta n\rfloor)}{n}.
\]
These bounded-sequence limit superiors are real numbers in \([0,1]\), measured in message bits per transmitted bit. The limsup of \((a_n)\) means \(\inf_{N\ge1}\sup_{n\ge N}a_n\). No assumption that the ordinary limits exist is made. The distance fraction is fixed before taking either limit superior.

All finite codes are eligible regardless of encoding, decoding, description or construction complexity. The arbitrary-code side includes linear codes. The linear side permits every binary subspace and every dimension. Affine translates do not change attainable cardinality and distance, so permitting affine codes on that side gives the same maximum.

A positive answer establishes \(R_2(\delta)\ge R_2^{\mathrm{lin}}(\delta)+\eta\) for some fixed \(\delta\in(0,1/2)\) and \(\eta>0\). Neither constant has a prescribed magnitude. A negative answer proves equality of the two rates for every \(\delta\in(0,1/2)\), since the reverse inequality always follows from inclusion. An isolated finite-block advantage, a subexponential size advantage, or a comparison with one particular linear construction is not sufficient. This is a binary existence question, not a request to approximate the two entire rate curves.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the existence of a fixed relative distance with a strictly positive asymptotic rate gap. A positive result must compare with all binary linear codes, and a negative result must establish equality throughout (0,1/2). No minimum improvement such as 1/100 is imposed.',
 why='Linearity makes coding algebraically tractable, but it is unknown in this regime whether it sacrifices a positive fraction of information per transmitted bit. Resolving the comparison would distinguish a fundamental cost of linearity from limitations of known constructions and bounds.',
 importance=dict(score=88,method='editorial',reason='A positive-rate separation or universal equality would resolve a fundamental structural comparison in binary coding theory, beyond any particular efficient construction.'),
 source_formulation=dict(text='The source asks whether optimum codes are far from linear, then discusses a weaker bounded-sum condition relevant to its LP hierarchy. This card selects the binary asymptotic rate comparison at fixed relative distance, with any positive gap. The optional choice received no reply; the recommended specialization was announced and applied as an editorial decision.',caption='Coregliano–Jeronimo–Jones, ITCS 2022, §6 p.51:21; rate convention from §1 p.51:2.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A Complete Linear Programming Hierarchy for Linear Codes','Leonardo Nagami Coregliano; Fernando Granha Jeronimo; Chris Jones',2022,'https://doi.org/10.4230/LIPIcs.ITCS.2022.51','§1 p.51:2 defines the binary rate; §6 p.51:21 asks about distance from linearity and states the weaker condition (9)'),
 ref('lp2026','An Elementary Proof of the First LP Bound on the Rate of Binary Codes','Nati Linial; Elyassaf Loyfer',2026,'https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2026.48','Introduction pp.48:1–48:2; Theorem 1 and discussion of the unchanged asymptotic bound'),
 ],
 context_blocks=[
 block('The 2022 work gives a complete hierarchy of linear programs for optimum linear-code size. Its comparison with a collapsing hierarchy for broader codes motivates the question about how much linearity can cost.'),
 block('The bounded-sum condition in the source is weaker than full linearity and supports a separate hierarchy question. The selected target compares actual binary subspaces with unrestricted binary codes, rather than feasibility in a relaxation.'),
 block('The classical Gilbert–Varshamov lower bound applies to linear codes as well as general binary codes. Therefore, showing that a nonlinear family meets that lower bound alone would not separate the two optimum rates.'),
 block('The 2026 paper gives a new proof of the first LP upper bound and explicitly states that it obtains the same asymptotic bound. It also reports that the exact binary rate is unknown at every fixed distance strictly between zero and one half. This is broader rate-distance context, not a proof that the two optimum rates coincide.','lp2026'),
 ],
 progress=[progress('2022','The complete linear-code LP hierarchy motivates an explicit comparison between optimum codes and linearity.'),progress('2026','A new proof recovers the first LP rate bound without improving its asymptotic value or separating linear and unrestricted codes.','lp2026')],
),[
 'Selected a fixed-distance binary asymptotic rate gap from the source’s broad comparison; documented the unanswered optional choice as editorial.',
 'Defined both finite maxima, floor convention, limit superiors, binary linearity, units and absence of efficiency requirements.',
 'Accepted any fixed positive gap and excluded finite-block or subexponential advantages as insufficient for this selected target.',
 'Checked the original hierarchy discussion and the 2026 LP-bound paper without confusing a new proof with an improved bound.',
 'Individually assessed importance and required a complete Lean-checked proof or refutation.',
],[
 'Read ITCS 2022 §1, the rate definition and §6 including equation (9).',
 'Downloaded the RANDOM 2026 proceedings paper and read the introduction, Theorem 1 and its explicit no-improvement qualification.',
 'Bounded searches through 18 September 2026 found no matching positive-rate separation or equality theorem; finite-block and distance-tending-to-one-half constructions were not conflated with the selected fixed-distance target.',
], 'The selected asymptotic binary linear-versus-unrestricted rate comparison remains unresolved in the checked sources through 18 September 2026. The 2022 source motivates this specialization without stating its exact quantifiers, and the 2026 LP-bound result does not settle it. This is a bounded source review, not an exhaustive certification of current openness.',summary=[
 'Binary linear codes are vector subspaces, while arbitrary codes can be any sets of binary words.',
 'At each fixed relative minimum distance, compare their largest possible asymptotic information rates.',
 'The question asks whether arbitrary codes have a strictly higher rate at even one distance between zero and one half.',
 'Any fixed positive rate gap counts, but a finite-block advantage or a comparison with one construction does not.',
 'The source motivates the comparison through linear-programming hierarchies, and the checked later bound does not resolve it.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
