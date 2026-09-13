"""Reader exports and live-update files for an already prepared catalogue."""

import csv
import io
import json

from importance import ranking_exports
from benchmark_selection import GOAL, QUOTAS, write_exports as write_benchmark_exports
from summaries import summary_markdown


CATALOG_FIELDS = [
    'id', 'title', 'area', 'area_label', 'original_area', 'selection_group', 'selection_target',
    'importance_rank', 'importance_count',
    'importance_score', 'importance_method', 'importance_reason', 'focus_topic', 'focus_reason', 'year',
    'is_new', 'evidence', 'status', 'question_type', 'formal', 'question_excerpt',
    'definitions', 'answer_criterion', 'statement_review_status', 'statement_review_issue', 'context', 'why', 'status_note',
    'criterion', 'progress', 'references', 'related_problem_ids', 'textbook_notes', 'working_summary',
    'working_summary_date', 'working_summary_source_refs', 'working_summary_extra_sources',
]


def atomic(path, text):
    temporary = path.with_name(path.name + '.publishing')
    temporary.write_text(text, encoding='utf8')
    temporary.replace(path)


def jsdump(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def csvtext(rows, fields):
    stream = io.StringIO()
    stream.write('\ufeff')
    writer = csv.DictWriter(stream, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def catalog_rows(cards, areas):
    labels = {area['area']: area['label'] for area in areas}
    for card in cards:
        importance = card['importance']
        row = {key: card.get(key, '') for key in CATALOG_FIELDS}
        row.update(
            area_label=labels.get(card['area'], card['area']),
            question_excerpt=card.get('source_formulation', {}).get('text', ''),
            statement_review_status=card.get('statement_review', {}).get('status', ''),
            statement_review_issue=card.get('statement_review', {}).get('remaining_issue', ''),
            progress=' | '.join(p['date'] + ': ' + p['text'] for p in card['progress']),
            references=' | '.join(r['url'] for r in card['references']),
            importance_score=importance['score'],
            importance_method=importance['method'],
            importance_reason=importance['reason'],
            focus_topic=card.get('benchmark_focus', {}).get('topic', ''),
            focus_reason=card.get('benchmark_focus', {}).get('reason', ''),
            textbook_notes=jsdump(card.get('textbook_notes', [])),
            related_problem_ids=jsdump(card.get('related_problem_ids', [])),
            working_summary=' '.join(card.get('working_summary', {}).get('sentences', [])),
            working_summary_date=card.get('working_summary', {}).get('written_on', ''),
            working_summary_source_refs=jsdump(card.get('working_summary', {}).get('source_refs', [])),
            working_summary_extra_sources=jsdump(card.get('working_summary', {}).get('extra_sources', [])),
        )
        yield row


def category_summary(data):
    lines = [
        '# Current category sizes', '',
        GOAL, '',
        'Counts are saved candidate records, not verified distinct open problems.', '',
        '| Group | Category | Top 100 | Top 500 | Legacy Top 1000 | Candidates |',
        '| --- | --- | ---: | ---: | ---: | ---: |',
    ]
    lines.extend(
        f"| {a['group']} {a['position']} | {a['label']} | "
        + ' | '.join(str(quotas[a['group']]) for quotas in QUOTAS.values())
        + f" | {a['count']} |"
        for a in data['areas']
    )
    taxonomy = data['meta']['taxonomy']
    lines.extend([
        '',
        f"Candidate pool: {taxonomy['candidate_count']}. "
        f"Inactive records: {taxonomy['inactive_count']} (excluded from active work).",
        '',
        f"The legacy Top 1000 view has {taxonomy['assigned_target']} assigned places; "
        f"reserved places: {taxonomy['reserved_target']}. "
        'Inactive cards and their reasons are retained in data/archive/. '
        'Final quota selection and a comprehensive deduplication audit remain pending.',
    ])
    return '\n'.join(lines) + '\n'


def write_catalog_exports(site, data, textbook_report):
    """Write matching JSON, offline JavaScript, CSV and reader documentation."""
    cards = data['cards']
    atomic(site / 'catalog.json', json.dumps(data, ensure_ascii=False, indent=2))
    atomic(site / 'data.js', 'window.TCS_ATLAS=' + jsdump(data).replace('</', '<\\/') + ';\n')
    atomic(site / 'catalog.csv', csvtext(catalog_rows(cards, data['areas']), CATALOG_FIELDS))
    atomic(site / 'small-bucket-summaries.md', summary_markdown(data))
    atomic(site / 'large-bucket-summaries.md', summary_markdown(data, group='large'))

    ranking, overview = ranking_exports(data)
    atomic(site / 'importance-ranking.csv', csvtext(ranking, [
        'area', 'area_label', 'position', 'id', 'title', 'score', 'assessment', 'status', 'reason', 'focus_topic', 'focus_reason',
    ]))
    atomic(site / 'importance-overview.md', overview)

    sources = {
        ref['url']: ref
        for card in cards
        for ref in card['references'] + [n['reference'] for n in card.get('textbook_notes', [])]
    }
    atomic(site / 'sources.csv', csvtext(sources.values(), [
        'title', 'authors', 'year', 'url', 'pdf_url', 'locator',
    ]))
    atomic(site / 'textbook-additions.json', json.dumps(textbook_report, ensure_ascii=False, indent=2))
    atomic(site / 'textbook-additions.csv', csvtext(
        ({**entry, 'card_ids': ' | '.join(entry['card_ids'])} for entry in textbook_report['entries']),
        ['entry_key', 'card_ids', 'disposition', 'kind', 'summary', 'source', 'year', 'locator', 'url', 'pdf_url'],
    ))
    atomic(site / 'areas.csv', csvtext(data['areas'], [
        'id', 'area', 'label', 'group', 'position', 'target', 'count', 'reviewed',
        'importance_assessed', 'importance_provisional', 'before', 'added', 'after_pct',
    ]))
    coverage = dict(meta=data['meta'], areas=data['areas'], sources=len(sources))
    atomic(site / 'coverage.json', json.dumps(coverage, ensure_ascii=False, indent=2))
    atomic(site / 'category-sizes.md', category_summary(data))
    write_benchmark_exports(site, data, atomic)


def write_live_updates(site, data, changed, previous_version, previous_ids):
    """Commit the version marker last, after all exports; catalog.json is the full live snapshot."""
    version = data['meta']['version']
    now = data['meta']['updated_at']
    previous_ids = set(previous_ids)
    current_ids = {c['id'] for c in data['cards']}
    removed_ids = sorted(previous_ids - current_ids)
    payload = dict(
        version=version, published_at=now, changed_ids=changed,
        cards=data['cards'], meta=data['meta'], areas=data['areas'], snapshot=True,
    )
    changed_set = set(changed)
    delta = dict(
        version=version, base_version=previous_version, published_at=now,
        changed_ids=changed, cards=[c for c in data['cards'] if c['id'] in changed_set],
        meta=data['meta'], areas=data['areas'], removed_ids=removed_ids,
    )
    atomic(site / 'updates-delta.json', jsdump(delta))
    atomic(site / 'version.json', jsdump(dict(version=version, published_at=now, delta=True)))
    return payload
