"""Complete the knot-input model while retaining uncertainty about the new claim."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,block,progress
from review_queue import read_claims
identifier='TCS-6528'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[2]['url']='https://arxiv.org/abs/1604.00290v3'
refs[3]['locator']='Oxford Topology Seminar, 15 March 2021; announcement states n^{O(log n)} for an n-crossing diagram; SoCG 2025 §1 still describes it as announced'
refs[4]['locator']='SoCG 2025, LIPIcs 332, Article 55; §1 separates worst-case complexity, experiments and the quasipolynomial announcement'
refs[5].update(url='https://arxiv.org/abs/2607.23350v1',
 locator='25 July 2026, v1; Theorem 1.1, Corollary 1.2, §9 and Proposition 9.1; iterations bounded in hierarchy parameters rather than input size')
refs[6].update(url='https://arxiv.org/abs/2609.06492v1',
 locator='6 September 2026, v1; Lemma 6 (p. 8), Lemmas 8–10 and Theorem 1/Corollary 1 (pp. 14–15); claimed polynomial-time result')
notes=[
 'Preserved deterministic polynomial bit time on explicit knot diagrams and the assessed importance.',
 'Specified tame knots, ambient isotopy, complete finite half-edge encoding, sphere embedding and the one-component test.',
 'Separated supplied bit length from minimum crossing number and disallowed compressed input by the actual encoding definition.',
 'Added universal algorithm/time constants and a full Lean proof criterion for either answer.',
 'Rechecked the fresh claim and its local-minimality and compressed-update dependencies; retained uncertain status rather than certifying a resolution.',
 'Rechecked the exact Reidemeister-move bound, certificate results and the limited complexity conclusion of the July 2026 hierarchy paper.',
]
sources=[
 'Read Hass–Lagarias–Pippenger’s author abstract and final bibliographic record: NP membership and deterministic exponential algorithms.',
 'Read the Annals publisher statement of Lackenby’s (236c)^11 Reidemeister-move bound and publication date.',
 'Read Lackenby arXiv 1604.00290v3 abstract and version history: unconditional NP certificates for knottedness.',
 'Read the Oxford seminar announcement dated 15 March 2021 and the SoCG 2025 final §1, which still calls the quasipolynomial result an announcement.',
 'Read Lackenby arXiv 2607.23350v1 §9 and Proposition 9.1: bound L(g+1)^L on iterations, with L and g not bounded there by the input.',
 'Read Musick arXiv 2609.06492v1 definitions, Lemma 6, Lemmas 7–10 and Theorem 1/Corollary 1. The core reduction of all relevant bridge isotopies to the grammar and compressed normalization accounting were not independently established.',
 'Checked the arXiv histories on 16 September 2026: no later version displayed for either 2026 paper. A bounded search found no independent validation or published correction of the September claim.',
]
status=('Musick’s 6 September 2026 v1 claims a deterministic polynomial-time solution. '
 'This review examined its statement and main proof dependencies but did not independently establish the local-minimality argument in Lemma 6 or all compressed-update bounds in Lemmas 8–10. '
 'No later revision or independent validation was located through 16 September 2026. '
 'The card therefore remains uncertain, rather than being declared resolved or unconditionally open. '
 'The July hierarchy paper, polynomial certificate theorems and earlier quasipolynomial announcement are recorded with their distinct scopes.')
complete(identifier,dict(
 status='uncertain',
 formal=r'''Do there exist a deterministic Turing machine \(M\), a real constant \(C>0\), and an integer \(k\ge1\) such that, for every valid explicit knot-diagram encoding \(D\) of bit length \(N\), the machine halts within \(C(N+1)^k\) steps and outputs
\[
M(D)=1
\quad\Longleftrightarrow\quad
\text{the knot represented by }D\text{ is ambient isotopic to the unknot}?
\]
It must output zero for every nontrivial knot. The same machine and constants must work for all diagrams, without auxiliary certificates or advice.''',
 definitions=r'''The \(3\)-sphere is \(S^3=\{x\in\mathbb R^4:\sum_{i=1}^4x_i^2=1\}\), equivalently the one-point compactification of \(\mathbb R^3\). A tame knot is an embedded circle in \(S^3\) that can be carried by an ambient isotopy to a finite polygonal embedded circle in \(\mathbb R^3\). Wild embeddings are excluded.

An ambient isotopy is a continuous map \(H:S^3\times[0,1]\to S^3\) such that each \(H_t=H(\,\cdot\,,t)\) is a homeomorphism and \(H_0\) is the identity. Two knots have the same type if some such \(H_1\) takes one onto the other. The unknot is the type of a round planar circle. Knots are not given an orientation.

A knot diagram is a plane drawing of one immersed circle with finitely many transverse double crossings and a choice of overpassing strand at every crossing. The drawing determines a tame knot by separating the two strands locally in the third coordinate. Its input representation is combinatorial, so real coordinates are unnecessary.

For a diagram with \(n\ge1\) crossings, encode a connected graph with \(n\) vertices and four half-edges at each vertex. A half-edge is one end of an edge; an explicitly listed pairing of the \(4n\) half-edges forms the edges. Loops and parallel edges are allowed. At every vertex list the four incident half-edges in cyclic order, and mark which of the two opposite pairs is overpassing. The other pair is underpassing. Also designate one face as the outer face.

The cyclic orders must define a cellular embedding in the sphere: replace each vertex by an oriented disc, join paired half-edges by bands respecting the orders, and cap each resulting boundary circle by a disc. The resulting surface must be a sphere. Equivalently for this connected rotation system, its face cycles must give Euler characteristic \(n-2n+f=2\), where \(f\) is their count. The outer face gives a plane drawing.

Following edges and continuing through the opposite half-edge at each crossing must trace a single unoriented closed component. Thus the representation describes a knot, not a multi-component link. A separate fixed code represents the crossing-free circle. All indices, pairings, cyclic lists and crossing bits are written explicitly in binary with fixed delimiters. They can be checked combinatorially in polynomial time; malformed encodings may be rejected.

The parameter \(N\) is the length of the supplied finite encoding. A standard indexing uses \(O(n\log(n+1))\) bits, with the crossing-free code handled separately. It is neither the smallest possible crossing number of the knot nor the length of a compressed program describing a larger diagram.

The algorithm is a single finite deterministic Turing-machine program with finitely many tapes. A step reads and writes a bounded number of tape symbols; arbitrary-length integer operations are not unit-cost operations. It receives no spanning disc, invariant, simplification sequence, random bits, oracle or length-dependent advice. The required output is one bit, not an isotopy or diagram simplification.''',
 answer_criterion=r'''Provide a complete mathematically correct proof checked in Lean of the displayed proposition or its logical negation. A positive proof must establish the algorithm’s correct answer on every valid diagram and one polynomial worst-case bit-time bound. A negative proof must exclude every deterministic polynomial-time recognizer in this input model, rather than only a selected algorithm or simplification rule. Short certificates, polynomial-length move sequences and successful finite experiments do not by themselves prove deterministic polynomial running time. The existence statement is binary and has no numerical approximation tolerance.''',
 references=refs,
 source_formulation=dict(text='Is there a deterministic polynomial-time algorithm for unknot recognition?',
 caption='Editorial paraphrase of the complexity question',citation='practical',format='editorial_paraphrase'),
 context_blocks=[
 block('A complicated knot diagram can represent a circle that has merely been drawn in an awkward way. The task is to distinguish such projections from actual knots, using a finite description of crossings and planar incidence. No physical model of rope or numerical geometry is involved.','np'),
 block('Both positive and negative instances have short efficiently checkable certificates. The NP theorem certifies unknottedness, and the coNP theorem certifies knottedness. These are existence statements about verifiable evidence; they do not show how to find the evidence in deterministic polynomial time.','conp'),
 block(r'Thus the problem belongs to \(\mathrm{NP}\cap\mathrm{coNP}\). Here NP consists of decision problems with polynomial-size witnesses verifiable in polynomial time, and coNP contains their complements. NP-hardness of this particular problem under polynomial-time reductions would imply \(\mathrm{NP}=\mathrm{coNP}\); a proof that it is outside P would in particular separate P from NP.','conp'),
 block(r'Lackenby proves that an unknot diagram with \(n\) crossings admits a simplification using at most \((236n)^{11}\) Reidemeister moves. These are local changes of diagrams that preserve knot type. The theorem bounds a successful sequence’s length, while an algorithm must determine appropriate moves without an uncontrolled search.','moves'),
 block(r'The March 2021 Oxford announcement states a recognition algorithm with running time \(n^{O(\log n)}\). The checked SoCG 2025 article still describes that result as announced. Such a quasipolynomial bound allows a growing exponent and therefore does not give the fixed exponent requested here.','quasipoly'),
 block('The SoCG 2025 factorisation work distinguishes practical performance from worst-case guarantees. It reports that Regina’s recognition algorithm behaves polynomially in experiments despite an exponential worst-case bound. Testing many diagrams cannot establish a bound for every possible input.','practical'),
 block(r'Lackenby’s July 2026 hierarchy algorithm gives another recognition method. Section 9 bounds iteration counts by \(L(g+1)^L\), where \(L\) is a hierarchy-length bound and \(g\) bounds surface pattern complexity. These parameters are not bounded there as functions of the original diagram size, and some operation costs also remain unspecified. The displayed iteration estimate is not a polynomial-time theorem for this card.','hierarchies'),
 block('Musick’s September 2026 preprint claims a positive solution. A bridge presentation separates the knot into trivial arcs in two balls. The preprint claims to find a locally minimal bridge presentation in polynomial time using compressed data, then invokes the fact that a locally minimal presentation of the unknot has one bridge.','claim'),
 block('The claim’s key dependencies include completeness of the permitted simplifications for local bridge minimality and polynomial manipulation of arc multiplicities. This review read those arguments but did not independently certify them. The scientific status remains uncertain pending validation; no counterexample to the claim is asserted.','claim'),
 ],
 progress=old['progress']+[
 progress('2026-09-16','The individual review checks the input model and the recent claim’s central dependencies while retaining uncertain status.','claim')
 ],
),notes,sources,status,summary=[
 'The input is an explicit finite crossing diagram of a tame knot.',
 'The question asks whether a deterministic algorithm can recognize the unknot in polynomial bit time.',
 'Both unknottedness and knottedness have polynomially verifiable certificates, which does not itself give such an algorithm.',
 'A September 2026 preprint claims a positive solution using locally minimal bridge presentations.',
 'The review has not independently certified that claim, so the card retains uncertain scientific status.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
