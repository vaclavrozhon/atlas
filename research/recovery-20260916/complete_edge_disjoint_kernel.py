"""Archive the historical kernel target with its explicit complexity assumption."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0784'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the explicit user instruction to archive the historical question as answered under NP not contained in coNP/poly.',
 'Recovered the original parameter as the number of requested terminal pairs, with a polynomial-time many-one kernel for general undirected graphs.',
 'Specified exact edge-disjoint feasibility, full output encoding size and the distinction between a kernel and a Turing kernel.',
 'Checked the 2023 reduction conclusion, including simple subcubic planar graphs with degree-one terminals and polynomial parameter growth.',
 'Explained why the result excludes a general-graph kernel as well, without imposing planarity on its output or asserting an unconditional impossibility.',
 'Preserved assessed importance 72 and separated the published conditional resolution from independent Lean certification.',
]
sources=[
 'Read the complete original §4.8 by Erik Jan van Leeuwen in Graph Modification Problems, Dagstuhl Reports 4(2), Seminar 14071 (2014), printed p. 58, DOI 10.4230/DagRep.4.2.38. It asks for a polynomial kernel on general graphs parameterized by the number of pairs.',
 'Read Włodarczyk–Zehavi, arXiv:2307.06792v1, 13 July 2023: introduction Theorem 1.3, §2.2 reduction overview, §5 opening and §5.6 Lemma 5.62, Theorem 5.63 and the final derivation, printed pp. 80–81. The construction outputs a simple subcubic planar instance with degree-one terminals and O(k^7) requests from Set Cover on a k-element universe.',
 'The final reduction from Set Cover also excludes kernels outputting general Edge-Disjoint Paths instances: such an output is an NP instance of polynomial length in the universe size and can be mapped back to Set Cover with polynomial universe size. This is a scope implication of the checked reduction, not a claim that a kernel must preserve input planarity.',
 'Checked FOCS 2023 acceptance and the authors’ institutional publication record: pp. 649–662, DOI 10.1109/FOCS57990.2023.00044, conference 6–9 November 2023. The record’s generic January date was not used as the conference date.',
 'The reduction endpoints and conditional inference were checked, but the full 82-page gadget construction was not independently reconstructed or Lean-certified.',
]
status='Archived at the user’s request as a resolved historical kernel question under the standard assumption NP is not contained in coNP/poly. Włodarczyk–Zehavi, FOCS 2023, Theorem 1.3 and the Set Cover reduction in Theorem 5.63 imply that a polynomial kernel would force that containment, even with planar inputs. This is a conditional negative answer, not an unconditional proof that no kernel exists.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',status='resolved',year=2023,
 formal=r'''Historical question, answered negatively under \(\mathrm{NP}\nsubseteq\mathrm{coNP}/\mathrm{poly}\): does Edge-Disjoint Paths on general finite undirected graphs admit a polynomial kernel when parameterized only by the number \(k\) of requested terminal pairs?

The published resolution proves the implication
\[
\text{a polynomial kernel exists}
\quad\Longrightarrow\quad
\mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}.
\]
The conditional archival status does not assert an unconditional separation of complexity classes.''',
 definitions=r'''An instance is a finite simple undirected graph \(G=(V,E)\) and an explicitly listed sequence of \(k\ge0\) unordered terminal pairs \((s_i,t_i)\) with distinct endpoints within each pair. Different requests may share terminals. The input is yes if there are paths \(P_1,\ldots,P_k\) such that \(P_i\) connects \(s_i\) to \(t_i\) and no edge belongs to two paths. Paths may share vertices, including terminals; each individual path has no repeated vertex. For \(k=0\), feasibility is vacuous. Neither capacities, directed edges nor a planar embedding are part of the problem.

Vertices are numbered and the complete adjacency matrix and terminal list are input, with every bit counted in input length \(L\). A polynomial kernel means one total deterministic Turing algorithm, with fixed constants \(C,d,e\ge1\), that on every valid instance outputs an instance \((G',T')\) of this same general-graph decision problem in at most \(C(L+1)^e\) bit operations. The input and output must have the same yes/no answer, and the full output encoding length must be at most \(C(k+1)^d\). Thus the output parameter \(k'=|T'|\) is also polynomially bounded in \(k\). The algorithm and exponents are independent of \(G,k\). Output uses an explicit graph and request list, not a succinct circuit or oracle representation.

The kernel produces one equivalent instance. A procedure making several decision-oracle calls is a different notion, a Turing kernel, and is not the historical target here. No claim about that different model or its distinct collapse assumption is needed for this archival decision.

The class \(\mathrm{NP}\) consists of binary languages accepted by nondeterministic polynomial-time Turing machines. A language is in \(\mathrm{NP}/\mathrm{poly}\) if such a machine may additionally use an advice string of polynomial length depending only on input length, with the same advice for all inputs of that length; advice need not be computable. The class \(\mathrm{coNP}/\mathrm{poly}\) consists of complements of languages in \(\mathrm{NP}/\mathrm{poly}\). The assumption is that at least one NP language is outside this latter class. Taking complements shows that the source’s containment \(\mathrm{coNP}\subseteq\mathrm{NP}/\mathrm{poly}\) is equivalent to \(\mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}\).

The lower-bound reduction already has simple planar subcubic input graphs, with distinct terminals of degree one. Its restriction is therefore contained in the general input class defined here. The proposed general-graph kernel would be allowed to output nonplanar graphs; the reduction still yields the stated complexity-class consequence.''',
 answer_criterion=r'''The retained formalization target for the published resolution is a complete Lean-checked proof that existence of the stated polynomial kernel implies \(\mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}\), hence its nonexistence under the displayed assumption. A source citation alone is not a Lean proof. The historical research question is archived on the strength of the published conditional result; independent formalization is not being claimed or retained as a new active task.''',
 source_formulation=dict(text='The original entry asks whether Edge-Disjoint Paths on general graphs admits a polynomial kernel parameterized by the number of terminal pairs, contrasting it with the already known conditional lower bound for vertex-disjoint paths.',caption='Paraphrase of Graph Modification Problems, Seminar 14071, §4.8, printed p. 58 (2014).',citation='primary',format='editorial_paraphrase'),
 why='A polynomial kernel would compress a potentially large routing instance to size controlled polynomially by its number of requests. The conditional lower bound rules out this form of efficient preprocessing even for planar inputs, while remaining consistent with fixed-parameter algorithms whose dependence on the request count is much larger.',
 references=[
 ref('primary','Graph Modification Problems: Existence of Polynomial Kernel for Edge-Disjoint Paths','Erik Jan van Leeuwen',2014,'https://doi.org/10.4230/DagRep.4.2.38','Dagstuhl Reports 4(2), Seminar 14071, §4.8, printed p. 58'),
 ref('resolution','Planar Disjoint Paths, Treewidth, and Kernels','Michał Włodarczyk; Meirav Zehavi',2023,'https://arxiv.org/abs/2307.06792v1','Version 1, 13 July 2023; Theorem 1.3 and §5.6, Lemma 5.62, Theorem 5.63 and final derivation, pp. 80–81; FOCS 2023, 649–662, DOI 10.1109/FOCS57990.2023.00044'),
 ],
 context_blocks=[
 block('Edge-disjoint routing allows different paths to meet at vertices, so a lower bound for vertex-disjoint routing cannot be transferred just by renaming the problem. The 2014 source explicitly identified this missing kernelization result.'),
 block('The 2023 paper supplies a reduction that applies to both routing variants. Its final instances are simple, subcubic and planar with degree-one terminals, where the required disjointness notions coincide. The number of requests grows polynomially in the universe size of the source Set Cover instance.','resolution'),
 block('This gives the usual conditional negative resolution: a small kernel would imply an unexpected nonuniform complexity-class containment. It does not establish that containment is false. The user explicitly selected archival with the assumption stated.','resolution'),
 ],
 progress=[
 progress('2014','The source asks whether a polynomial kernel exists on general graphs, with the number of pairs as the parameter.'),
 progress('2023-07-13','The author preprint gives the conditional lower bound even for planar Edge-Disjoint Paths; subsequently published at FOCS 2023.','resolution'),
 ],
),notes,sources,status,summary=[
 'The historical question asks whether a routing instance can be reduced in polynomial time to an equivalent instance of size polynomial in its number of terminal pairs.',
 'Routes must be edge-disjoint, but may share vertices, and the graph is undirected.',
 'The FOCS 2023 reduction rules out the stated kernel unless NP is contained in coNP/poly, already on planar inputs.',
 'This is a conditional negative result and does not claim an unconditional complexity-class separation.',
 'The user selected archival under the standard noncontainment assumption; a complete Lean formalization of the conditional theorem is not claimed.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='Resolved historical kernel question: FOCS 2023 proves no polynomial kernel unless NP is contained in coNP/poly, even on planar inputs; conditional archival explicitly selected by the user.')
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
