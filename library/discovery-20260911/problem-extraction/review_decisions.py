"""Individual status and selection decisions, distinct from passage extraction."""
import json
from pathlib import Path
from review_inventory import ENTRIES

ROOT = Path(__file__).resolve().parent
DATE = '2026-09-11'
D = {}


def set_entry(identifier, **patch):
    assert identifier in {e['id'] for e in ENTRIES}, identifier
    D.setdefault(identifier, {}).update(patch)


def checked(identifier, status, note, urls, selection='not_imported_resolved'):
    set_entry(identifier, current_status=status, status_checked_on=DATE,
              verification_note=note, verification_urls=urls, selection=selection)


def by_title(title, **patch):
    found = [e for e in ENTRIES if e['title']==title]
    assert found, title
    for e in found:
        set_entry(e['id'], **patch)


def duplicate(title, ids, note='Same target is already represented; retain its existing identifier.'):
    by_title(title, selection='existing_record', catalogue_ids=ids, selection_note=note)


schrijver = 'https://homepages.cwi.nl/~lex/co/'
for number, status, note, urls in [
    (3,'resolved_negative','Santos disproved the Hirsch diameter bound; the author’s errata also records the correction.', ['https://arxiv.org/abs/1006.2814',schrijver]),
    (4,'resolved_positive','Orlin obtained O(nm) maximum flow; Schrijver explicitly marks Survey Question 4 answered.', [schrijver]),
    (6,'resolved_reported','Schrijver’s author errata says this question was already solved by Weinberger (1976). The original proof was not reread.', [schrijver]),
    (7,'resolved_negative','Rothvoss proves exponential extension complexity for the perfect-matching polytope. This rules out the proposed polynomial extended formulation.', ['https://arxiv.org/abs/1311.2369']),
    (11,'resolved_positive','Thomassen proves a fixed edge-connectivity threshold, settling the weak three-flow conjecture; this does not settle Tutte’s exact four-edge-connectivity conjecture.', ['https://orbit.dtu.dk/en/publications/the-weak-3-flow-conjecture-and-the-weak-circular-flow/']),
    (16,'resolved_positive','The Goldberg–Seymour bound was proved by Chen–Jing–Zang; the 2024 short proof supplies a further primary reference.', ['https://arxiv.org/abs/1901.10316','https://arxiv.org/abs/2407.09403']),
    (41,'resolved_positive','Scott–Seymour prove chi-boundedness of graphs with no odd hole.', ['https://arxiv.org/abs/1410.4118']),
    (42,'resolved_positive','Polynomial recognition was obtained by Chudnovsky and coauthors. Schrijver’s errata explicitly marks Question 42 answered.', [schrijver,'https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/FOCS03final.pdf']),
    (54,'resolved_reported','The author’s errata records a positive resolution by G. Pap in February 2006; no independent proof check was performed.', [schrijver]),
    (55,'resolved_reported','The author’s errata records a positive resolution by G. Pap in February 2006; no independent proof check was performed.', [schrijver]),
    (56,'resolved_complexity','Schrijver records NP-completeness proved by W. Schwaerzler, published in Combinatorica 29 (2009), 121–126. This settles the classification; it does not unconditionally prove absence of a polynomial algorithm.', [schrijver]),
]:
    checked(f'personal-234:Survey Question {number}',status,note,urls)

checked('personal-234:Survey Question 35','source_formulation_corrected',
        'Schrijver’s official errata explicitly adds the triangle inequality. The uncorrected source passage must not become a new nonmetric conjecture. The corrected metric target already has TCS-6589.',
        [schrijver], 'existing_record')
set_entry('personal-234:Survey Question 35',catalogue_ids=['TCS-6589'],
          corrected_question='Does the metric symmetric TSP subtour relaxation have integrality gap at most 4/3?')

decomp='https://arxiv.org/abs/1907.10937'
for i in [2,3,4,5]:
    checked(f'personal-283:Open Problem 11.{i}','resolved_positive',
            'Rozhon–Ghaffari’s deterministic polylogarithmic LOCAL network decomposition resolves this polylogarithmic target. General MIS covers the neighbourhood-independence restriction; proper vertex colouring also applies to the line graph for the stated edge palette.',[decomp])
checked('personal-280:Network decomposition, chapter notes','resolved_positive',
        'The historical deterministic polylogarithmic symmetry-breaking barrier is resolved by Rozhon–Ghaffari. Sharper round bounds remain separate questions.',[decomp])
checked('personal-283:Open Problem 11.1','partially_resolved_direction',
        'Rozhon–Ghaffari give polylogarithmic derandomization for locally checkable problems. This resolves the central polylogarithmic case, but the source’s unrestricted request for a general method is broader than a single theorem.',[decomp], 'not_imported_direction')

for identifier,status,note,urls in [
    ('personal-285:Conjecture 2.27','resolved_negative','Shitov gives counterexamples to the claimed equality for chromatic number under graph products.',['https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n2-p06-s.pdf']),
    ('personal-285:5, CSP dichotomy','resolved_positive','Bulatov’s dichotomy theorem settles the finite-template classification. Infinite-domain and promise variants remain different questions.',['https://arxiv.org/abs/1703.03021']),
    ('personal-292:14, nonrepetitive colouring','resolved_positive','Dujmovic, Esperet, Joret, Walczak and Wood prove an absolute bound for planar graphs.',['https://arxiv.org/abs/1904.05269']),
    ('personal-290:Bounded-degree graph limits','reported_negative_resolution','The two Aldous–Lyons papers give a negative resolution. Their claims were checked in the primary abstracts; the long proofs were not independently verified.',['https://arxiv.org/abs/2408.00110','https://arxiv.org/abs/2501.00173']),
    ('personal-270:12, product-state capacity','resolved_negative','Hastings disproves general additivity. The anniversary-edition preface itself notes this development; the older chapter passage is historical.',['https://arxiv.org/abs/0809.3972']),
    ('personal-274:Chapter 17','resolved_positive','The classical-oracle separation was announced by Bostanci–Haferkamp–Nirkhe–Zhandry in November 2025. Bostanci–Huang–Vaikuntanathan give another proof in February 2026. Neither separates unrelativized QMA from QCMA.',['https://eccc.weizmann.ac.il/report/2025/176/','https://eccc.weizmann.ac.il/report/2026/020/']),
    ('personal-274:Chapter 23','resolved_positive','Unbounded randomness-expansion protocols exceed the historical exponential target. Gross–Aaronson explicitly analyze the seed requirement for such a protocol.',['https://arxiv.org/abs/1410.8019','https://arxiv.org/abs/1402.4797']),
    ('personal-26:4.4.2, unknot certificates','resolved_positive','Lackenby proves a polynomial upper bound on moves needed to simplify an unknot diagram. This certificate-length theorem does not itself yield polynomial-time unknot recognition.',['https://arxiv.org/abs/1302.0180']),
]:
    checked(identifier,status,note,urls)

checked('personal-270:Problem 12.7, historical discussion','partially_resolved_direction',
        'The quantum channel coding theorem gives the regularized coherent-information characterization. A general effective single-letter formula or exact computation is not supplied by that theorem. The broad source question needs this distinction before reuse.',
        ['https://arxiv.org/abs/quant-ph/0304127'], 'not_imported_needs_formulation')

for title, ids in [
    ('P versus NP',['TCS-0001']),
    ('P versus NP intersect coNP',['TCS-0018']),
    ('NP inside BQP',['TCS-0037']),
    ('Quantum graph isomorphism',['TCS-6522']),
    ('Splay-tree dynamic optimality',['TCS-6498']),
    ('Matrix multiplication exponent two',['TCS-0007']),
    ('Unrestricted Frege lower bounds',['TCS-0025']),
    ('Existence of one-way functions',['TCS-7167']),
    ('Worst-case hardness and one-way functions',['TCS-0022']),
    ('Hadwiger conjecture',['TCS-6651']),
    ('Strongly polynomial linear programming',['TCS-0008']),
    ('P versus BPP',['TCS-0003']),
    ('Deterministic linear-time minimum spanning tree',['TCS-6536']),
    ('A logic capturing polynomial time',['TCS-7195']),
    ('Linear-time integer multiplication',['TCS-7174']),
    ('Unrestricted Fourier-transform circuit lower bounds',['TCS-7175']),
]:
    duplicate(title,ids)

duplicate('Shannon capacity of odd cycles',['TCS-6610'],
          'The existing C7 question is a prominent unsolved member of the source family. No additional generalization is imported without a separate significance review.')
set_entry('personal-25:Open Problem B.2',selection='related_existing_record',catalogue_ids=['TCS-6887'],
          selection_note='The generic explicit-circuit-lower-bound programme already has a source record. The concrete multiplication threshold was reviewed separately.')
set_entry('personal-270:Chapter 5, hidden-subgroup discussion',selection='related_existing_record',catalogue_ids=['TCS-7166'],
          selection_note='Efficient decoding of the hidden-subgroup information is part of the existing general hidden-subgroup goal; source representation details remain necessary.')
set_entry('personal-233:Bin packing',selection='related_existing_record',catalogue_ids=['TCS-6640'],
          selection_note='Additive one is stronger than the existing constant-additive-error target. No separate numerical strengthening is imported in this pass.')
set_entry('personal-55:Research Problem 12.1',selection='related_existing_record',catalogue_ids=['TCS-6504'],
          selection_note='Existing deterministic parallel matching target; consult the canonical general-perfect-matching card to distinguish matching variants.')

# Link exact newly authored targets to their stable IDs from the publication log.
atlas = ROOT.parents[2]
registry=json.loads((atlas/'data/id_registry.json').read_text())
publication=[json.loads((atlas/'data/cards'/(registry['reviewed:'+key]+'.json')).read_text()) for key in ['linear-size-boolean-integer-multiplication', 'polynomial-time-exact-addition-chain-length', 'perfect-versus-statistical-zero-knowledge', 'woodall-dijoin-packing-conjecture', 'conforti-cornuejols-packing-mfmc-conjecture']]
source_ids={
    'linear-size-boolean-integer-multiplication':'personal-25:B.2, multiplication example',
    'polynomial-time-exact-addition-chain-length':'personal-5:1, exponentiation',
    'perfect-versus-statistical-zero-knowledge':'personal-141:4.3.1.5',
    'woodall-dijoin-packing-conjecture':'personal-234:Survey Question 34',
    'conforti-cornuejols-packing-mfmc-conjecture':'personal-234:Survey Question 68',
}
for item in publication:
    canonical=item
    checked(source_ids[item['key']], 'open_checked', canonical['status_note'],
            [r['url'] for r in canonical['references']], 'added_reviewed_card')
    set_entry(source_ids[item['key']], catalogue_ids=[item['id']],
              selection_note=canonical['importance']['reason'])

checked('personal-25:B.3.2','open_checked',
        'The unrestricted linear-circuit lower-bound barrier is retained in the checked primary literature. Bounded-coefficient FFT lower bounds do not settle it. TCS-7175 already covers the stronger Fourier-transform lower-bound goal, so no second record is added.',
        ['https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2023.31',
         'https://www3.nd.edu/~jhauenst/preprints/ghilRigidity.pdf'], 'existing_record')

by_title('Physical universality of quantum computation',kind='research_direction',
         selection='not_imported_direction', selection_note='A physical modelling programme; the passage does not specify one mathematical proposition.')
by_title('Fast atomic shared-memory objects',kind='research_direction',
         selection='not_imported_direction', selection_note='The object, operation set and resource target need to be fixed before a card can be completed.')
by_title('Modular proof of the GHS algorithm',kind='expository_or_formalization_task',
         selection='not_imported_not_open_mathematical_problem',selection_note='A request for a better proof organization is not itself a new unresolved mathematical proposition.')
by_title('Square-lattice self-avoiding walk asymptotics',selection='not_imported_scope',
         selection_note='A general enumeration/statistical-physics asymptotic problem; no sufficient computational consequence was established for this catalogue’s selection policy.')

if __name__=='__main__':
    (ROOT/'decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(D)} individual source-entry dispositions')
