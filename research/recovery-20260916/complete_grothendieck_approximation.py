"""Archive the unrestricted approximation target already covered by SODA 2009."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7352'
claim=read_claims(ROOT)[identifier]
original=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
notes=[
 'Applied the user’s explicit choice to archive the known unrestricted approximation target rather than retain a new Lean formalization task.',
 'Preserved the unrestricted real Grothendieck constant and absolute 1/100 tolerance, without adding exact-value or efficient-computation requirements.',
 'Added Raghavendra–Steurer SODA 2009 Theorem 1.3 and §3.6, which give a finite-program approximation to arbitrary additive error.',
 'Separated the unconditional computation theorem from the paper’s distinct Unique Games hardness theorem.',
 'Corrected the older strict-bound reference from STOC 2011 to FOCS 2011 and fixed inspected preprint versions.',
 'Preserved assessed importance 94, explained why the printed interval between known bounds does not make this target open, and recorded that no LP was evaluated or proof Lean-certified here.',
]
sources=[
 'Read Raghavendra–Steurer, Towards Computing the Grothendieck Constant, SODA 2009 pp. 525–534, DOI 10.1137/1.9781611973068.58, author PDF: Theorem 1.3 on PDF p. 2, §§3.1–3.3 prerequisites and §3.6 on PDF p. 7. The computation theorem has no UGC hypothesis; §3.6 uses finite discretization and an LP for a reciprocal comparison factor. Its full analytic error proof and all discretization constants were not independently reconstructed.',
 'Checked the author-hosted PDF at https://www.dsteurer.org/paper/grothendieck.pdf and its downloaded redirect https://www.bayesianestimation.org/paper/grothendieck.pdf. The author publication list identifies SODA 2009; the publisher’s later online date is not the conference year.',
 'Read the inherited strict-bound source as arXiv:1103.6161v3, 17 August 2011, Braverman–Makarychev–Makarychev–Naor; corrected the conference to FOCS 2011, followed by Forum of Mathematics, Pi (2013).',
 'Read Saha–Li–Xue–Chaudhuri–Klivans–Kothari–Meka, arXiv:2608.11158v2, 12 August 2026, abstract and introduction. Its printed interval remains wider than 1/50, but this does not invalidate the earlier arbitrary-precision finite-program result. The new bounds are preprint claims and their proofs were not certified.',
 'No numerical LP was evaluated and no particular decimal approximation is asserted by this review. The user authorized archival as a known approximation task after the distinction was explained; details are saved in review_grothendieck_precision.md.',
]
status='Archived at the user’s request as a known approximation target. Raghavendra–Steurer, SODA 2009, Theorem 1.3 and §3.6 give unconditional computation to arbitrary additive error by a finite-program construction. This covers the card’s 1/100 tolerance with no time bound and with an unambiguous mathematical expression permitted. The exact value and practical computation are different questions and are not declared solved. No independent Lean formalization or evaluated decimal output is claimed.'
complete(identifier,dict(
 criterion='tightness',question_type='numerical_value',status='resolved',year=2026,
 formal=r'''Historical approximation target, covered by a known computation theorem: determine the unrestricted real Grothendieck constant \(K_G^{\mathbb R}\) to absolute error at most \(1/100\).

An unambiguous mathematical expression for the approximation is permitted, and there is no running-time bound. This archival decision concerns that approximation target, not an exact closed form or an efficient practical computation.''',
 definitions=original['definitions']+r'''

The admissible approximation is a fully specified real number \(a\) with \(|a-K_G^{\mathbb R}|\le1/100\). A proved interval \([l,u]\) containing the constant with \(u-l\le1/50\) qualifies through its midpoint. An expression may specify the value of a completely described finite optimization problem together with its conversion to an approximation of the constant. Merely renaming the original supremum over arbitrarily large matrices is not a determination. No bound on the size of an admissible finite expression or on the time to evaluate it is imposed.''',
 answer_criterion=r'''The original benchmark criterion was a specified real approximation and a complete Lean-checked proof of absolute error at most \(1/100\), including any finite-program construction, discretization error and reciprocal conversion used to define the approximation. An interval of width at most \(1/50\) suffices through its midpoint. A source citation is not itself that formal proof.

The research target is archived because the required approximation method is already known, as explicitly selected by the user. This review does not claim to have produced the Lean proof, evaluated the huge finite program or found the exact constant; a separate formalization task has not been substituted for the archived question.''',
 source_formulation=dict(text='The inherited record concerns the unrestricted real Grothendieck constant. Under the benchmark’s absolute 1/100 tolerance, unrestricted computation time and permission to use an unambiguous expression, the relevant target is already covered by the SODA 2009 arbitrary-additive-error computation theorem.',caption='Editorial scope of the inherited approximation card, matched to Raghavendra–Steurer, Theorem 1.3; archival explicitly selected by the user on 17 September 2026.',citation='computation',format='editorial_paraphrase'),
 why='The constant measures the largest universal loss between vector and sign optimization for real bilinear objectives. Its exact value remains a major quantitative issue, but a benchmark allowing any finite expression at fixed additive precision must distinguish that issue from the already known arbitrary-precision computation theorem.',
 references=[
 ref('computation','Towards Computing the Grothendieck Constant','Prasad Raghavendra; David Steurer',2009,'https://www.dsteurer.org/paper/grothendieck.pdf','SODA 2009, 525–534, DOI 10.1137/1.9781611973068.58; author PDF Theorem 1.3 p. 2 and §3.6 p. 7; unconditional finite-program computation'),
 ref('krivine','The Grothendieck constant is strictly smaller than Krivine’s bound','Mark Braverman; Konstantin Makarychev; Yury Makarychev; Assaf Naor',2013,'https://arxiv.org/abs/1103.6161v3','Version 3, 17 August 2011; definition and main strict upper bound; FOCS 2011, followed by Forum of Mathematics, Pi (2013)'),
 ref('bounds2026','New Lower and Upper Bounds for the Grothendieck Constant','Rahul Saha; Alan Li; Anton Xue; Swarat Chaudhuri; Adam Klivans; Pravesh K. Kothari; Raghu Meka',2026,'https://arxiv.org/abs/2608.11158v2','Version 2, 12 August 2026; abstract and introduction; reported bounds not independently certified'),
 ],
 context_blocks=[
 block('A real matrix defines a bilinear objective. Replacing each scalar sign by a unit vector can improve its optimum, and the constant bounds that improvement uniformly over every finite matrix.','krivine'),
 block('The SODA 2009 computation theorem applies to any prescribed additive error without assuming the Unique Games Conjecture. Its finite discretization leads to a linear program and a controlled conversion of its value. The neighboring conditional hardness theorem is a separate result.','computation'),
 block('Later improvements to explicit lower and upper numerical bounds remain relevant to the constant’s quantitative study. A wide printed interval does not show that an unrestricted finite-expression approximation task is open when a general computation theorem is already available.','bounds2026'),
 block('No numerical evaluation of the large program is claimed here. The user chose to remove this known approximation target from the active open-problem collection rather than turn it into a separate formalization exercise.','computation'),
 ],
 progress=[
 progress('2009','The SODA computation theorem gives an unconditional finite-program method for arbitrary additive accuracy.','computation'),
 progress('2011–2013','A strict improvement disproves the proposed optimality of Krivine’s bound; FOCS 2011 and the 2013 journal publication.','krivine'),
 progress('2026-08-12','The revised preprint reports further explicit bounds; this is separate from the already known unrestricted approximation method.','bounds2026'),
 ],
),notes,sources,status,summary=[
 'The unrestricted real Grothendieck constant is the worst ratio between vector and sign bilinear optima over all finite real matrices.',
 'This benchmark asks for absolute accuracy 1/100 and imposes no computation-time limit.',
 'The SODA 2009 theorem already supplies unconditional approximation to arbitrary additive error through a finite-program construction.',
 'Neither its exact value nor a practical decimal computation is claimed to follow from this editorial review.',
 'The user selected archival of the known approximation target; no independent Lean proof or evaluated finite program is claimed.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='Known unrestricted 1/100 approximation target: Raghavendra–Steurer SODA 2009 Theorem 1.3 and §3.6 provide arbitrary-additive-error finite-program computation; archival explicitly selected by the user.')
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
