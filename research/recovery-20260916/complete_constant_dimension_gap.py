"""Complete the selected one-step locality-preserving quantum energy amplification."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-4734';claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user-selected one-step energy doubling with unchanged constraint arity and constant-factor term growth, and the follow-up choice of output local dimension bounded independently of instance size.',
 'Specified normalized ground energy of an explicit projective local Hamiltonian, not its spectral gap above the ground space and not energy restricted to product states.',
 'Made the one-step perfect-completeness target precise: preserve zero ground energy and ensure output energy at least min(2 times input energy, gamma), for a positive constant gamma.',
 'Allowed output local dimension to depend on fixed input arity and local dimension, but not the number of sites, constraints, coefficient precision or actual input instance.',
 'Used exact algebraic local matrices and deterministic polynomial bit-time construction so zero-energy preservation has an exact representation and rounding cannot silently alter the promise.',
 'Separated the source’s proved locality-increasing repetition theorem from the desired arity-preserving transformation; no conclusion that this step alone proves quantum PCP is asserted.',
 'Checked the July 2026 Simons announcement of combinatorial-gap amplification; its abstract does not establish the stated all-quantum-state normalized-energy soundness.',
 'Assessed importance individually at 89 and required a complete Lean-checked construction and all-state bound, or refutation.',
]
sources=[
 'Read Bergamaschi–Metger–Vidick–Zhang, Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians, CCC 2026 Article 15, DOI 10.4230/LIPIcs.CCC.2026.15: Definition 1.1 and Theorem 1.2 pp. 15:2–15:3, the full locality-preservation discussion in §1.1 p. 15:4, and Definition 1.6 p. 15:7. The proved repetition increases locality from k to 2tk and is subject to its layered-Hamiltonian hypotheses. The source’s open prose does not itself fix all constants used by this selected one-step target.',
 'Verified the full-version metadata for arXiv:2510.01333v1, submitted 1 October 2025, with no later version listed on 17 September 2026. The local theorem locators in this review use the published CCC paper, not an assumed later revision.',
 'Read the primary Simons Institute abstract for Quynh T. Nguyen, Gap Amplification for Local Hamiltonians with Combinatorial Soundness, 23 July 2026. It announces a locality-preserving template and a proved combinatorial gap; it does not supply the quantitative spectral-energy statement required here. No corresponding archival proof of this exact target was verified, and the video proof was not independently checked.',
 f'Bounded primary-source searches through {DATE} found no verified construction or refutation of this selected fixed-dimension, fixed-arity normalized-energy step. The July announcement is recorded as relevant progress, not silently promoted to full quantum soundness.',
]
complete(identifier,dict(
 title='Locality-preserving quantum gap amplification',criterion='construction',question_type='yes_no',year=2026,is_new=True,
 formal=r'''For every fixed integers \(k,q\ge2\), do there exist integers \(D\ge q\) and \(C\ge1\), a rational \(0<\gamma\le1\), and a deterministic classical polynomial-time transformation \(T_{k,q}\) with the following property? Given any explicit \(k\)-local projective Hamiltonian
\[
 H=\frac1m\sum_{j=1}^m P_j
\]
on \(n\) sites of local dimension \(q\), it outputs an explicit projective Hamiltonian
\[
 H'=\frac1{m'}\sum_{j=1}^{m'} P'_j
\]
with \(1\le m'\le Cm\), whose terms each act on at most \(k\) sites and whose site dimension is \(D\), such that
\[
 \lambda(H)=0\ \Longrightarrow\ \lambda(H')=0,
 \qquad
 \lambda(H')\ge\min\{2\lambda(H),\gamma\}.
\]
Here \(\lambda\) denotes the lowest eigenvalue of the normalized Hamiltonian. In particular, whenever \(0<\lambda(H)\le\gamma/2\), its normalized energy is at least doubled. All output-dimension, term-growth and energy-threshold constants are independent of the input instance and its size.''',
 definitions=r'''A site is a finite quantum system with state space \(\mathbb C^q\). An input has integers \(n,m\ge1\) and a list of \(m\) constraints. Constraint \(j\) specifies an ordered subset \(S_j\subseteq\{1,\ldots,n\}\), with \(1\le|S_j|\le k\), and the full \(q^{|S_j|}\)-by-\(q^{|S_j|}\) matrix of an orthogonal projection \(P_j\). Thus \(P_j=P_j^\dagger=P_j^2\). It acts as the identity on sites outside \(S_j\). Zero projections are allowed, and identical repeated constraints count separately. Projections on overlapping sites need not commute; there is no input bound on how many constraints contain a site.

The normalized energy is
\[
 \lambda(H)=\min_{\langle\psi,\psi\rangle=1}\langle\psi|H|\psi\rangle,
 \qquad |\psi\rangle\in(\mathbb C^q)^{\otimes n}.
\]
The minimum ranges over every unit vector, including arbitrarily entangled states, and lies in \([0,1]\). Equivalently it is the smallest eigenvalue of \(H\). Zero energy means that some state is simultaneously in the kernel of every \(P_j\). Energy is divided by the number of constraints before and after transformation, so increasing the number of identical constraints cannot by itself create the required amplification. This is ground-energy amplification, not enlargement of the difference between the two lowest eigenvalues of one Hamiltonian.

Each local matrix entry is an explicitly encoded complex algebraic number. Its real and imaginary parts are each represented by a nonzero integer polynomial, with all coefficients listed in binary, and rational isolating endpoints selecting one real root. The polynomial must have exactly one real root in the indicated interval. Rational numbers can be supplied by linear polynomials. This gives exact finite matrices, rather than a tolerance-dependent approximation oracle. Hermiticity and idempotence are promises about the exact entries. The total bit length \(L\) includes all matrix data, site lists, and unary encodings of \(n\) and \(m\); for fixed \(k,q\) this differs only polynomially from usual explicit input encodings.

The output uses the same exact algebraic-entry representation. It may introduce new sites and new constraints, and may change the interaction pattern. Every output site belongs to some declared output support; hence there are at most \(km'\) output sites. Output constraints are again orthogonal projections, supported on at most \(k\) sites, and \(H'\) is their equally weighted average. The normalization and unit-norm projection convention prevent amplification merely by multiplying the whole Hamiltonian by two.

The dimension \(D=D(k,q)\) may exceed \(q\), as selected by the user, but it is one fixed integer for the transformation. It cannot grow with \(n,m,L\), the coefficient degrees or precision, or any property of the particular instance. The same independence holds for \(C\) and \(\gamma\). The number of sites may change; what is preserved is the maximum number of sites touched by a single constraint. A bound of \(O(k)\) sites with a larger hidden constant is not the stated bound \(k\).

For each fixed \(k,q\), \(T_{k,q}\) is one finite deterministic program and there exist constants \(A,b\ge1\) such that it halts within \(A(L+1)^b\) elementary steps of a classical multitape Turing machine on every input encoding. This includes computing and writing all output matrices. Its guarantees apply to valid promised inputs; there is no requirement to recognize all invalid encodings. The constants and program may depend on \(k,q\), and no bound on an effective compiler from \(k,q\) to that program is requested.

The completeness condition is exact preservation of zero energy. The soundness condition holds on every valid input, with a constant plateau \(\gamma\) once the input energy is no longer small. This fixes a one-step, perfect-completeness version of the source’s broader template question. It does not ask for alphabet reduction, a complete quantum PCP theorem, or a bound uniform over an unbounded number of iterations. Enlarging the constant local dimension again in a later separate step is not part of the present guarantee.''',
 answer_criterion=r'''Give a complete Lean-checked construction of the transformations and their constants, polynomial bit-time bounds, exact zero-energy preservation, output arity and term-count bounds, and the displayed normalized-energy inequality for all states; or give a complete Lean-checked refutation of the existence statement for some fixed \(k,q\).

A lower bound proved only for product states, computational-basis states or another restricted witness class is insufficient. A locality-increasing construction, dimension growing with input size, superconstant multiplicative term growth, or an increase caused only by rescaling constraints does not meet the target. A single step does not by itself establish the other ingredients of a full quantum PCP theorem. The exact propositions and asymptotic resource bounds do not receive a numerical approximation tolerance.''',
 source_formulation=dict(text='The CCC paper identifies preservation of the number of variables in each constraint as a missing feature of attempted quantum versions of Dinur’s amplification. Its own repetition increases that locality. The user selected one energy-doubling step with constant-factor term growth, allowing a larger local dimension but requiring that dimension to remain independent of instance size.',caption='Paraphrase of Bergamaschi–Metger–Vidick–Zhang, CCC 2026 §1.1 p. 15:4; one-step target and constant local-dimension interpretation selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=89,method='editorial',reason='Preserving constraint arity while amplifying normalized quantum energy addresses a central structural obstacle in adapting the combinatorial PCP strategy. Even one such step would distinguish quantum soundness from the currently available locality-increasing or restricted-soundness constructions.',basis='Individual assessment of the CCC discussion and the July 2026 primary announcement; the selected step is one ingredient, not a claim of equivalence to the full quantum PCP conjecture.'),
 why='Checking a few quantum particles remains useful only if amplification does not make each check involve more and more particles. The question asks whether the energy penalty can grow while each individual constraint retains its original arity.',
 references=[
 ref('primary','Derandomised Tensor Product Gap Amplification for Quantum Hamiltonians','Thiago Bergamaschi; Tony Metger; Thomas Vidick; Tina Zhang',2026,'https://doi.org/10.4230/LIPIcs.CCC.2026.15','CCC 2026, LIPIcs 383, Article 15; Definition 1.1 and Theorem 1.2 pp. 15:2–15:3; locality-preservation question §1.1 p. 15:4; layered-Hamiltonian Definition 1.6 p. 15:7'),
 ref('full','Derandomised tensor product gap amplification for quantum Hamiltonians','Thiago Bergamaschi; Tony Metger; Thomas Vidick; Tina Zhang',2025,'https://arxiv.org/abs/2510.01333v1','Version 1, submitted 1 October 2025; full-version metadata checked on 17 September 2026, with no later listed revision; theorem discussion here uses the published CCC version'),
 ref('combinatorial','Gap Amplification for Local Hamiltonians with Combinatorial Soundness','Quynh T. Nguyen',2026,'https://simons.berkeley.edu/talks/quynh-t-nguyen-harvard-university-2026-07-23','Simons Institute talk, 23 July 2026; primary abstract announces a locality-preserving template with combinatorial soundness; no full spectral-energy theorem or video proof verified in this review'),
 ],
 context_blocks=[
 block('The published tensor-product construction amplifies normalized energy while increasing the locality from k to 2tk. Its iterability is useful progress, but it does not give the unchanged-arity step required here.'),
 block('The source distinguishes locality from the local alphabet or quantum dimension. This card permits an increase in the latter, while the user’s follow-up choice requires that increase to remain a constant independent of the input size.'),
 block('The July 2026 announcement reports a locality-preserving framework with combinatorial-gap amplification. Its checked abstract does not assert the all-state ground-energy inequality written here, so that announcement is recorded as related progress rather than as a resolution.','combinatorial'),
 ],
 progress=[progress('2025-10-01','The full preprint introduces derandomised tensor-product quantum gap amplification.','full'),progress('2026','CCC publishes the locality-increasing theorem and the explicit locality-preservation question.'),progress('2026-07-23','A Simons talk announces locality-preserving amplification with combinatorial soundness; the stronger all-state energy guarantee has not been verified from the available abstract.','combinatorial')],
),notes,sources,'The checked CCC theorem increases constraint arity. A July 2026 primary talk announcement reports a locality-preserving template with combinatorial soundness, but its abstract does not establish the selected normalized-energy inequality for all quantum states. Bounded checks through 17 September 2026 found no verified resolution of this precise one-step target; the announced proof and cited full theorems were not independently certified.',summary=[
 'The input is a collection of local quantum projection constraints, and its energy is the smallest possible average violation over all quantum states.',
 'The task is one polynomial-time transformation that preserves zero energy and at least doubles sufficiently small positive normalized energy.',
 'Each output constraint must still involve at most the original number of particles, and the number of constraints may grow only by a constant factor.',
 'The local quantum dimension may increase to a larger constant but cannot grow with the size of the input instance.',
 'A complete Lean-checked proof or refutation must control entangled states as well as all stated representation and resource bounds.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());r=next(r for r in a if r['id']==identifier);r.update(state='applied',applied_on=DATE);r['secondary_choice']['state']='applied';p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
