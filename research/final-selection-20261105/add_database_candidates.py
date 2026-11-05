"""Reviewed database additions; run from the repository root exactly once."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from import_cards import import_cards
from archive_cards import change_activity
from card_schema import canonical_record

AREA = 'Database theory and finite model theory'
DATE = '2026-11-05'


def card(key, title, year, formal, definitions, why, context, references, score):
    return dict(key=key, title=title, area=AREA, year=year, is_new=True,
        evidence='reviewed', status='source_open', criterion='decision',
        question_type='yes_no', formal=formal, definitions=definitions,
        answer_criterion='Give a complete Lean-checked proof or refutation of the stated proposition. Results for a restricted query family do not settle its universal scope. A conditional negative result must retain its unproved assumptions and is not an unconditional refutation.',
        why=why, context_blocks=context, references=references,
        progress=[dict(date=str(year), text='The primary source records the general question and partial results.', citation='primary')],
        status_note='Primary-source formulation checked on 5 November 2026, with a bounded search for later results. The general target remains open in the checked sources. This is not an independent proof audit or the deferred whole-catalog status review.',
        model_self_contained=True, requires_context=False,
        statement_review=dict(status='revised', reviewed_on=DATE, remaining_issue='',
            notes=['Defined database semantics, fixed versus input parameters, and the exact decision target.'],
            scope='Individual source and formulation review for an explicitly requested database addition.'),
        importance=dict(score=score, method='editorial', assessed_on=DATE, reason=why,
            basis='Database-category expansion: breadth, direct connection to data management and diversity relative to existing queries.'),
        category_assignment=dict(method='editorial_topic', reviewed_on=DATE,
            reason='The input, semantics and target explicitly concern database queries or constraints.'),
        related=[], related_problem_ids=[])


cqa = card('database:primary-key-cqa-dichotomy',
    'Dichotomy for consistent query answering under primary keys', 2023,
    r'''For every fixed finite relational schema with one designated nonempty primary key for each relation, and every fixed Boolean conjunctive query \(q\) over that schema, is the language \(\operatorname{CERTAINTY}(q)\) either in deterministic polynomial time or coNP-complete under polynomial-time many-one reductions?

The input to this language is an explicitly represented finite database \(D\), possibly violating its keys. It is accepted exactly when \(q\) is true in every inclusion-maximal subdatabase of \(D\) that satisfies the keys. Repeated occurrences of a relation in \(q\), called self-joins, are allowed.''',
    r'''A schema lists relation names and their positive integer arities. Each relation has a fixed nonempty subset of its positions as its primary key. A database is a finite set of tuples for each relation, with values encoded as finite binary strings. A key is satisfied if any two tuples agreeing in all key positions also agree in every position. A subdatabase deletes tuples without inserting or changing values. A repair is such a subdatabase that satisfies all keys and cannot be enlarged by putting back any deleted tuple while still satisfying them. Thus, for each nonempty group of conflicting tuples with one key value, a repair chooses exactly one tuple; this is inclusion maximality, not an optimization over all possible edits.

A Boolean conjunctive query is a finite nonempty conjunction of relational atoms with all its variables existentially quantified; variables may repeat within and across atoms, and fixed constants are allowed. It contains no negation, disjunction, inequality, function symbol or aggregation. Truth means that some assignment of its variables makes every atom a stored tuple. Query and schema, including keys, are fixed separately for each language; only the database varies. Time is measured in the total bit length of its explicit encoding, with constants and polynomial degree allowed to depend on the fixed query/schema.

P denotes languages decided by deterministic polynomial-time Turing machines. A language is in coNP if its complement has polynomial-size certificates verifiable in deterministic polynomial time. It is coNP-complete if it is in coNP and every coNP language reduces to it by one polynomial-time computable map preserving yes/no answers. The question asserts that every fixed query has one of these two complexities. It does not additionally require a computable classifier taking a query as input, nor assume that P differs from coNP.''',
    'Conflicting primary-key records are routine in integrated data. This question asks whether every fixed database query is either efficiently answerable with certainty across all repairs or computationally complete for a standard hard class.',
    [dict(text='Consistent answers retain only conclusions that survive every repair of inconsistent records. The difficulty comes from universal quantification over these alternative databases, even though evaluating the fixed query on one consistent database is easy.', citation='primary'),
     dict(text='The ICDT 2023 paper formulates the unrestricted primary-key dichotomy and gives a common polynomial-time method covering the known self-join-free and path-query tractable cases. It also explains why that method does not capture all tractable queries with self-joins.', citation='primary'),
     dict(text='For queries without repeated relation names, the 2019 result sharpens the tractable side to logarithmic space. That restricted classification leaves the universal self-join target stated here.', citation='selfjoinfree')],
    [dict(id='primary', title='A Simple Algorithm for Consistent Query Answering Under Primary Keys', authors='Diego Figueira; Anantha Padmanabha; Luc Segoufin; Cristina Sirangelo', year=2023, url='https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2023.24', locator='Abstract, introduction and definitions of primary keys, repairs and CERTAINTY(q).'),
     dict(id='selfjoinfree', title='Consistent Query Answering for Primary Keys in Logspace', authors='Paraschos Koutris; Jef Wijsen', year=2019, url='https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2019.23', locator='Abstract and Section 3; self-join-free restriction.')], 90)

resilience = card('database:relational-query-resilience-dichotomy',
    'Dichotomy for deletion resilience of relational queries', 2024,
    r'''For every fixed finite relational schema and every fixed Boolean union of conjunctive queries \(q\), is \(\operatorname{RES}(q)\) either in deterministic polynomial time or NP-complete under polynomial-time many-one reductions?

An input consists of a finite bag database \(D\) and a nonnegative integer \(k\). It belongs to \(\operatorname{RES}(q)\) if at most \(k\) individual tuple occurrences can be deleted so that \(q\) becomes false. All occurrences may be deleted, and all relation arities and self-joins are allowed.''',
    r'''A schema is a finite list of relation names of positive integer arity. A bag database gives an explicit list of tuple occurrences for each relation; duplicates are allowed and count as separate deletions. Domain values are finite binary strings. Multiplicities are represented by repeated occurrences, not exponentially compressed binary counts. The budget k is written in binary. Input length is the bit length of these lists and the budget.

The fixed query is a finite disjunction of Boolean conjunctive queries. Each disjunct is an existentially quantified, nonempty finite conjunction of relational atoms using variables, with no constants, equality, inequality, negation or function symbols. Every variable occurs in an atom. A disjunct is true when a variable assignment maps every atom to a tuple whose remaining multiplicity is positive. Repeated uses of one relation and disconnected conjunctions are permitted. Query truth uses the support of the remaining database, while deletion cost counts occurrences. The empty database therefore makes the query false. The minimum deletion cost is called its resilience; it is zero if the query is already false.

Only D and k vary in RES(q); the schema and query are fixed, so running-time constants and polynomial degree may depend on them. P denotes deterministic polynomial-time decidability. NP denotes decision languages with polynomial-size certificates verifiable in polynomial time. NP-completeness means membership in NP and polynomial-time many-one hardness for every NP language. The proposition asks whether an intermediate complexity can occur anywhere in this family. It does not demand an effective syntactic classifier or the stronger algebraic characterization from the source, and it does not assume P differs from NP.''',
    'Resilience measures how fragile a database answer is under deletion of records. A complete complexity dichotomy would identify whether all such fixed-query deletion problems have a tractable or NP-complete behavior, including repeated tables and higher-arity relations.',
    [dict(text='The 2024 paper studies bag-database resilience through valued constraint satisfaction. Its proposed algebraic tractability condition would imply the P/NP-complete dichotomy asked here. This card selects that complexity consequence, without requiring the stronger algebraic condition.', citation='primary'),
     dict(text='STACS 2026 establishes the dichotomy when the schema has a single binary relation, so the data are directed multigraphs. Several relations and arbitrary arities remain outside that theorem; the card deliberately retains the general relational question.', citation='digraph')],
    [dict(id='primary', title='The Complexity of Resilience Problems via Valued Constraint Satisfaction Problems', authors='Manuel Bodirsky; Žaneta Semanišinová; Carsten Lutz', year=2024, url='https://www.informatik.uni-leipzig.de/kr/research/papers/2024/BSL24.pdf', locator='LICS 2024, DOI 10.1145/3661814.3662071; Introduction, Section 8 and Conjecture 8.17. The decision dichotomy is a stated consequence of the stronger conjecture.'),
     dict(id='digraph', title='The Complexity of Resilience for Digraph Queries', authors='Manuel Bodirsky; Žaneta Semanišinová', year=2026, url='https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.15', locator='Abstract and main theorem; schema with one binary relation.')], 86)

linear = card('database:linear-rules-transitivity',
    'Decidability of query answering with linear rules and transitivity', 2015,
    r'''Is there one algorithm that, given a finite relational database \(D\), a finite set \(\Sigma\) of single-head linear existential rules and binary transitivity assertions, and a Boolean conjunctive query \(q\), decides whether \(D\cup\Sigma\models q\)?

Entailment ranges over all models, including infinite ones. The relation arities, rule set and query are part of the input; there is no bound on arity and no safety restriction on the linear rules.''',
    r'''A finite relational schema lists relation symbols and positive integer arities. A database is a finite set of ground relational atoms, with distinct constant names interpreted as distinct elements. A single-head linear existential rule has the form
\[\forall\bar x\,(R(\bar t)\;\Rightarrow\;\exists\bar y\,S(\bar u)),\]
where the body and head each consist of one relational atom. The tuple t consists of universally quantified variables, each of which occurs in the body; u uses body variables and the existential variables y. Repetitions are allowed. There are no constants in rules, function symbols, equality, inequality or negation. A binary transitivity assertion for T is \(\forall x,y,z\,(T(x,y)\wedge T(y,z)\Rightarrow T(x,z))\). Several designated binary relations may have these assertions, and those relations may also occur in linear rules.

A Boolean conjunctive query is a finite nonempty conjunction of relational atoms with every variable existentially quantified; fixed database constants and repeated relation names are allowed. A model is a nonempty relational structure that interprets the constants, contains all facts of D and satisfies all rules and assertions. D together with Sigma entails q if q holds in every such structure. In particular, no closed-world assumption declares unstored tuples false, and no restriction to finite completions is imposed. Inputs use ordinary finite encodings of the schema, facts, rules and query. The algorithm must halt on every well-formed input; no time or space bound is prescribed.''',
    'Incomplete databases often combine rules that imply missing records with transitive relations such as reachability. The question asks whether that combination still allows a general terminating procedure for answering multi-atom queries.',
    [dict(text='Linear existential rules may create new, unnamed elements. Transitivity connects arbitrarily long chains. The source proves decidability for atomic queries and for general conjunctive queries under an additional syntactic safety condition; unary/binary schemas satisfy that condition automatically.', citation='primary'),
     dict(text='The remaining target removes that condition for arbitrary-arity relations and general conjunctive queries. It concerns query entailment under incomplete information, rather than ordinary evaluation on a fully given finite table.', citation='primary')],
    [dict(id='primary', title='Combining Existential Rules and Transitivity: Next Steps', authors='Jean-François Baget; Meghyn Bienvenu; Marie-Laure Mugnier; Swan Rocher', year=2015, url='https://arxiv.org/abs/1504.07443', locator='IJCAI 2015, pp. 2720–2726; revised full version v2 (5 January 2017), preliminaries and conclusion.'),
     dict(id='collection', title='Open-world query answering with linear rules and transitivity assertions', authors='Antoine Amarilli', year=None, url='https://a3nm.net/work/research/questions/#open-world-query-answering-with-linear-rules-and-transitivity-assertions', locator='Existing Atlas TCS-0495 source; checked 5 November 2026.')], 80)

if __name__ == '__main__':
    target = ROOT / 'research/final-selection-20261105'
    if (ROOT / 'data/cards/TCS-0495.json').exists():
        raise SystemExit('TCS-0495 is already active; do not rerun the import.')
    oldpath = ROOT / 'data/archive/cards/TCS-0495.json'
    old = json.loads(oldpath.read_text())
    (target / 'database-restoration-before.json').write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n')
    linear.update(id='TCS-0495', is_new=old.get('is_new', False), legacy=old.get('legacy', {}))
    oldpath.write_text(json.dumps(canonical_record(linear), ensure_ascii=False, indent=2) + '\n')
    print(change_activity(['TCS-0495'], restore=True, reason='User-requested database-specific expansion: recover and complete the existing linear-rules/transitivity candidate using its primary paper, retaining its stable identity rather than creating a duplicate.'))
    (target / 'database-new-candidates.json').write_text(json.dumps([cqa, resilience], ensure_ascii=False, indent=2) + '\n')
    result = import_cards([cqa, resilience])
    (target / 'database-import.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result)
