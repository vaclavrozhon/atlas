"""Individual review of decidability of standard PL four-sphere recognition."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7242'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[0]['locator']='Journal of Applied and Computational Topology 6, 503–527; published 19 May 2022; §1, §2.1 and §2.5 Theorem 6, and §3.2'
refs[1].update(title='Frontiers of Sphere Recognition in Practice',
 locator='Applied Topology, Poznań, 15 July 2025; slides 3–4 and 7–8: PL-SPHERE(d), combinatorial manifolds, heuristic termination and bistellar equivalence')
refs += [ref('census2026','Small Triangulations of 4-Manifolds and the 4-Manifold Census',
 'Rhuaidi Burke; Benjamin Burton; Jonathan Spreer',2026,
 'https://link.springer.com/article/10.1007/s00454-026-00818-w',
 'Published online 25 February 2026; abstract, §1 and §2.1; finite census uses generalised triangulations')]
notes=[
 'Preserved the explicitly approved PL category, closed combinatorial four-manifold promise and unrestricted decidability target.',
 'Expanded the finite facet encoding, realization, link, standard sphere and PL-homeomorphism definitions.',
 'Specified a single deterministic machine with correct binary output and termination on every promised input, including disconnected manifolds.',
 'Made the Lean proof requirement explicit and stated the full algorithmic negation.',
 'Added the February 2026 census with its remaining PL-type ambiguity and different triangulation convention.',
]
sources=[
 'Read the final 2022 publisher text, §1 and Theorems 2 and 6, definitions in §2 and the finite-census account in §3.2.',
 'Read Joswig’s 15 July 2025 presentation slides 3–4 and 7–8: dimension four explicitly open, vertex-link definition and an UNDECIDED outcome in the heuristic.',
 'Read the 25 February 2026 final publisher abstract and introduction, including the unresolved PL types and §2.1 generalised triangulation convention.',
 'Checked the Hass–Kirby 2025 publisher abstract as a survey, not a new recognition theorem; its full text could not be fetched during this pass.',
 'A bounded primary-source search through 16 September 2026 found no claimed resolution of the full promised-input decidability target.',
]
status=('Joswig’s July 2025 presentation explicitly leaves PL-SPHERE(4) open. '
 'The February 2026 census paper treats bounded-size triangulations and retains unresolved PL types, rather than giving an all-input decision procedure. '
 'The card retains the approved standard PL sphere and closed combinatorial manifold promise. '
 'A bounded primary-source review through 16 September 2026 found no resolution; this is not an independent certification of every historical topological theorem.')
complete(identifier,dict(
 formal=r'''Does there exist one deterministic Turing machine \(M\) with the following property? For every finite abstract simplicial complex \(K\), encoded by its facets as below and promised to be a nonempty closed combinatorial \(4\)-manifold, \(M\) halts and outputs a bit satisfying
\[
M(\operatorname{enc}(K))=1
\quad\Longleftrightarrow\quad
K\cong_{\mathrm{PL}}\partial\Delta^5.
\]
Here \(\partial\Delta^5\) is the standard PL \(4\)-sphere. Output zero is required on every promised input that is not PL homeomorphic to it. There is no running-time or space bound, and connectedness is not part of the promise.''',
 definitions=r'''A finite abstract simplicial complex \(K\) is a finite family of finite subsets of a finite vertex set \(V\), containing the empty set and closed under taking subsets. Its members are faces; inclusion-maximal faces are facets. The dimension of a nonempty face \(\sigma\) is \(|\sigma|-1\). Pure dimension four means that all facets have exactly five vertices.

Vertex labels are distinct nonnegative integers. The input lists each facet once, sorting labels increasingly within facets and sorting the facet lists lexicographically. Each label is written in binary with no leading zero except for the label zero itself. A fixed separator between labels and a second separator between facets make this a finite string over a fixed alphabet. The full complex is the family of all subsets of the listed facets, and its vertex set is their union. Renaming vertices does not affect the correct answer.

The geometric realization \(|K|\) is the subset of \(\mathbb R^V\) consisting of vectors \((t_v)_{v\in V}\) with \(t_v\ge0\), \(\sum_vt_v=1\), and \(\{v:t_v>0\}\in K\). Each face is realized as the convex hull of its coordinate unit vectors. A finite simplicial subdivision is a finite triangulation of this realization by simplices contained in old simplices, whose union on each old simplex equals that simplex.

Two finite complexes are piecewise-linearly homeomorphic, written \(K\cong_{\mathrm{PL}}L\), when they admit finite subdivisions that are simplicially isomorphic. A simplicial isomorphism is a bijection on vertices taking faces to faces in both directions. Equivalently, their realizations have a homeomorphism that is affine on the simplices of suitable finite subdivisions.

The simplex \(\Delta^q\) is the complex of all subsets of a set of \(q+1\) vertices. Its boundary \(\partial\Delta^q\) consists of all proper subsets of that vertex set. The standard PL \(j\)-sphere is \(\partial\Delta^{j+1}\), up to PL homeomorphism.

The link of a vertex \(v\) is
\[
\operatorname{lk}_K(v)=
\{\sigma\in K:v\notin\sigma,\ \sigma\cup\{v\}\in K\}.
\]
In this card, a nonempty closed combinatorial \(4\)-manifold means a finite pure four-dimensional complex for which every vertex link is PL homeomorphic to \(\partial\Delta^4\). Multiple connected components are allowed. No orientation, simple-connectivity, homology-sphere or prior topological-sphere promise is imposed.

A deterministic Turing machine has a finite transition rule, finite tape alphabet and finitely many tapes; it starts with the encoded complex on its input tape. Halting with output one means acceptance, and halting with output zero means rejection. Termination and correctness are required on all and only promised inputs; behavior on malformed strings or complexes outside the promise is unrestricted. The same finite machine must work for complexes of every size.''',
 answer_criterion=r'''Supply a complete mathematically correct proof checked in Lean of existence of the stated machine or its logical negation. A positive answer must establish termination and the exact PL classification on every promised input, without additional unproved hypotheses. A negative answer must establish that every deterministic Turing machine has a promised input on which it either fails to halt with a bit or gives the wrong bit. A lower bound ruling out only polynomial time, a procedure that can return “unknown,” or a classifier proved correct only on a finite census does not settle this target. This is a binary decidability statement with no numerical approximation tolerance.''',
 references=refs,
 source_formulation=dict(text='Is recognition of the standard piecewise-linear four-sphere algorithmically decidable?',
 caption='Editorial paraphrase of PL-SPHERE(4)',citation='status',format='editorial_paraphrase'),
 context_blocks=[
 block('Finite input does not guarantee algorithmic decidability of a global geometric property. The question concerns existence of any always-terminating decision procedure, even one whose resource use is far beyond practical computation.','status'),
 block('The PL sphere-recognition problem is decidable through dimension three and undecidable in dimensions at least five. The four-dimensional case is the exceptional gap in the checked account. This card fixes that dimension and promises a manifold rather than asking for manifold recognition itself.','status'),
 block('The promise is local: links of vertices have the standard three-sphere type. The output concerns the entire four-dimensional space. Local manifold structure alone does not force the global space to be a sphere.','practice'),
 block('The topology category matters. A homeomorphism is a continuous bijection with continuous inverse, whereas PL equivalence adds finite piecewise-affine structure. The standard PL sphere cannot be replaced silently by a merely topological sphere.','practice'),
 block('Pachner’s theorem characterizes PL equivalence of closed triangulated manifolds by finite sequences of bistellar moves, local replacements that preserve PL type. Such finite certificates are useful for individual positive instances. Existence of a certificate does not ensure a recognition procedure terminates on negative instances.','practice'),
 block('The 2022 computational study explicitly allows an inconclusive outcome. Its successful classifications establish properties of those tested triangulations, without proving that every permitted input will eventually be classified.','practice'),
 block('The 2026 census work examines closed orientable four-manifolds with at most six four-dimensional simplices. Among triangulations topologically equivalent to the four-sphere, it leaves at most four potentially distinct PL types and conjectures that all are standard. These are unresolved classifications, not a proof that four distinct structures exist.','census2026'),
 block('That census uses generalised triangulations, permitting identifications among faces of a simplex. The card instead uses abstract simplicial complexes with the explicit vertex-set encoding. Neither the finite census limit nor its orientability restriction is added to the benchmark promise.','census2026'),
 block('An algorithm here must reject disconnected promised manifolds as well as connected non-spheres. It must also answer correctly for any PL structures that actually exist, without assuming a conjectural classification of four-manifolds.','status'),
 ],
 progress=[
 progress('1994–1995','Three-sphere recognition becomes decidable; the checked account identifies dimension four as the remaining gap.','practice'),
 progress('2022-05-19','The published computational study develops practical sphere-recognition heuristics with potentially inconclusive outcomes.','practice'),
 progress('2025-07-15','The research presentation explicitly marks PL-SPHERE(4) as open.','status'),
 progress('2026-02-25','A larger finite-census classification is published with residual PL-type ambiguities.','census2026'),
 progress('2026-09-16','The individual review retains unrestricted promised-input decidability and checks the scope of the newer census.','census2026'),
 ],
),notes,sources,status,summary=[
 'The input is a finite simplicial complex promised to be a closed combinatorial four-manifold.',
 'The question asks whether one deterministic algorithm can recognize the standard PL four-sphere on every such input.',
 'There is no time bound, but both termination and a correct binary answer are mandatory.',
 'Topological equivalence, finite experimental classifications and heuristics that may remain inconclusive do not supply this guarantee.',
 'The checked sources retain dimension four as the unresolved boundary in PL sphere recognition.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
