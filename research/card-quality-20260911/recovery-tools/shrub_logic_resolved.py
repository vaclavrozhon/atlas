import json
from review import card,save,DATE,DIRECTORY,write
i='TCS-6409';_,c=card(i);refs=c['references'];refs[0]['locator']='Definitions 2.2–2.4 give tree models, shrub-depth and vertex-set logic; Theorem 4.3 proves sufficiency and Conjecture 4.4 asks necessity on hereditary classes.'
refs += [dict(id='resolution',title='Forbidden Induced Subgraphs for Bounded Shrub-Depth and the Expressive Power of MSO',authors='Nikolas Mählmann',year=2025,url='https://doi.org/10.4230/LIPIcs.ICALP.2025.167',pdf_url='https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/LIPIcs.ICALP.2025.167/LIPIcs.ICALP.2025.167.pdf',locator='Published 30 June 2025. Theorem 1, equivalence of items 1 and 9, resolves the question; Section 2 specifies the adjacency signature and Section 6 proves the expressive-power separation. Full version arXiv:2501.13903.')]
save(i,dict(
title='Logical expressiveness on hereditary graph classes',
formal=r'''Historical question, resolved affirmatively: is it true that for every hereditary class \(\mathcal C\) of finite simple undirected graphs,
\[
\mathrm{FO}=\mathrm{MSO}_{1}\text{ on }\mathcal C
\quad\Longleftrightarrow\quad
\mathcal C\text{ has bounded shrub-depth}?
\]
Equality of expressive power and bounded shrub-depth are defined below. The reverse implication was known in the original source; Mählmann’s published ICALP 2025 Theorem 1 establishes the full equivalence.''',
definitions=r'''A finite simple undirected graph has a finite vertex set and a symmetric irreflexive adjacency relation \(E\). A graph class is closed under isomorphism. It is hereditary when, for every \(G\in\mathcal C\) and every \(U\subseteq V(G)\), the induced graph \(G[U]\) also belongs to \(\mathcal C\); this keeps exactly the edges of \(G\) whose endpoints both lie in \(U\).

First-order logic \(\mathrm{FO}\) uses vertex variables, equality, adjacency \(E(x,y)\), Boolean connectives and quantifiers over vertices. Monadic second-order logic \(\mathrm{MSO}_{1}\) additionally uses variables for arbitrary subsets of the vertex set, membership \(x\in X\), and quantifiers over those subsets. A sentence has no free variables. Both logics are interpreted on the graph itself, with no supplied vertex order, extra color predicates or auxiliary tree. There are no edge-set quantifiers in \(\mathrm{MSO}_{1}\).

Equality of expressive power on \(\mathcal C\) means
\[
\forall\text{ MSO}_{1}\text{ sentences }\varphi\
\exists\text{ FO sentence }\psi\
\forall G\in\mathcal C:\quad
G\models\varphi\iff G\models\psi.
\]
The sentence \(\psi\) may depend on \(\varphi\) and the fixed class \(\mathcal C\), but not on the individual graph. The opposite translation is automatic because FO is a fragment of \(\mathrm{MSO}_{1}\). No bound on translation time or on the length of \(\psi\) is part of this expressive-power assertion.

A tree model with \(m\ge1\) colors and depth \(d\ge1\) for a nonempty graph \(G\) consists of a finite rooted tree \(T\), a bijection from \(V(G)\) to its leaves, a color map \(\lambda:V(G)\to\{1,\ldots,m\}\), and a symmetric Boolean function
\[
F:\{1,\ldots,m\}^{2}\times\{0,\ldots,d-1\}\longrightarrow\{0,1\}.
\]
Every root-to-leaf path has exactly \(d\) edges. If \(u\ne v\) are leaves and \(h\) is the depth of their lowest common ancestor, then
\[
E(u,v)\iff F(\lambda(u),\lambda(v),h)=1.
\]
Symmetry means \(F(a,b,h)=F(b,a,h)\). The colors are labels for the representation, not a requirement that adjacent vertices have different colors. Depth of the lowest common ancestor is interchangeable with leaf distance because all leaves have depth \(d\).

The class has bounded shrub-depth when there exist fixed integers \(m,d\ge1\) such that every nonempty \(G\in\mathcal C\) admits such a tree model. Its tree, colors and function \(F\) may depend on \(G\); the same \(m,d\) must suffice for the entire class. The empty graph is included without a tree-model requirement. This harmless convention avoids a root-with-no-leaves exception and does not change boundedness. Allowing a separate number of colors growing with each graph would not be bounded shrub-depth.

The quantification is over all hereditary classes, without a decidability or effective enumeration assumption. This is a structural characterization of logical definability, rather than a running-time assertion for model checking.''',
question_type='yes_no',answer_criterion='The historical target is a proof of the displayed equivalence for every hereditary graph class under the stated graph signature and vertex-set semantics. In particular, necessity says that every hereditary class of unbounded shrub-depth has at least one MSO1 sentence with no equivalent FO sentence on that class. The cited published theorem supplies the missing direction.',
context_blocks=[
dict(title='The original source already proves one direction',text='Theorem 4.3 of the 2012 paper proves that bounded shrub-depth suffices for coincidence of FO and vertex-set monadic second-order logic. Conjecture 4.4 asks whether this structural condition is also necessary on hereditary classes.',citation='primary'),
dict(title='The full characterization is now published',text='Mählmann’s 2025 Theorem 1 explicitly lists bounded shrub-depth and equality of FO and MSO expressive power as equivalent properties of hereditary graph classes. The paper uses MSO for vertex-set logic on the adjacency signature, matching the original MSO1 question.',citation='resolution'),
dict(title='Edge quantification gives a different comparison',text='The source distinguishes this problem from the earlier characterization involving MSO2, which also permits quantification over edges and edge sets. The MSO1 target concerns bounded shrub-depth; substituting the edge-set language changes the theorem.',citation='primary'),
dict(title='Uniform bounds concern the class',text='Individual finite graphs can always be represented using sufficiently many colors. The substantive condition is that both representation depth and the number of colors remain bounded across the entire class.',citation='primary')],
why='This characterization identifies exactly when quantifying over arbitrary vertex sets adds no definable graph properties beyond quantifying over individual vertices. It links a logical boundary to a concrete form of dense graph structure, rather than to one particular model-checking algorithm.',
progress=[dict(date='2012',text='The source proves the bounded-shrub-depth implication and conjectures its converse for hereditary classes.',citation='primary'),dict(date='2025-01-23',text='Mählmann’s full preprint is first submitted, announcing the characterization.',citation='resolution'),dict(date='2025-06-30',text='ICALP publishes Theorem 1 with the equivalence of bounded shrub-depth and FO–MSO coincidence.',citation='resolution')],
references=refs,status='resolved',status_note='Checked the original tree-model and logic definitions, Theorem 4.3 and Conjecture 4.4, and the published ICALP 2025 paper, especially Theorem 1 and Section 6. The theorem explicitly settles this hereditary-class MSO1 characterization. Publication date and the full-version link were checked in the Dagstuhl record. This is verification of the published theorem’s scope, not an independent proof reconstruction.',
model_self_contained=True,requires_context=False,review_note='Reconstructed the complete characterization and replaced stale open status with the published 2025 resolution. Defined the graph signature, sentence equivalence, hereditary closure and class-wide tree-model bounds.',
importance=dict(score=c['importance']['score'],method='editorial',reason='A broad characterization connecting dense graph structure and the exact boundary between first-order and vertex-set logic. Existing score retained for the historical resolved question.',assessed_on=DATE),
working_summary=dict(sentences=['First-order graph logic quantifies over vertices, while MSO1 also quantifies over vertex sets.','The historical question asks on which hereditary graph classes those languages define exactly the same properties.','The proposed answer is precisely the classes of bounded shrub-depth.','This requires fixed bounds on both the depth and number of colors in tree representations of every graph in the class.','Mählmann’s published ICALP 2025 theorem proves the characterization.'],basis='saved_sources',written_on=DATE,source_refs=['primary','resolution'])),
notes=['Recovered Theorem 4.3 and Conjecture 4.4 instead of retaining the truncated introduction.','Defined class-wide logical and structural quantifiers.','Kept vertex-set logic separate from MSO2 edge quantification.','Confirmed the published 2025 resolution and updated status.'],
checked_sources=[r['url'] for r in refs]+['https://arxiv.org/abs/2501.13903'])
p=DIRECTORY/'queue.json';q=json.loads(p.read_text());_,c=card(i)
if not any(r['id']==i for r in q['dispositions']):q['dispositions'].append(dict(id=i,title=c['title'],state='resolved',reason=c['status_note'],card='data/cards/'+i+'.json'))
write(p,q)
