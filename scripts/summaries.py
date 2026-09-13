"""Readable exports of summaries stored in canonical cards."""

def summary_markdown(data, group='small'):
    """A readable, source-linked export of active summaries in one bucket group."""
    if group not in {'small', 'large'}:
        raise ValueError(f'Unknown summary group: {group}')
    selected = [card for card in data['cards'] if card.get('working_summary')
                and card.get('selection_group') == group and not card.get('scope_exclusion')]
    lines = [
        f'# Working summaries — {group} categories', '',
        f'{len(selected):,} five-sentence working summaries, based on saved source material.',
        'These intermediate explanations preserve each record\'s existing evidence and status; '
        'they do not constitute completed research cards or a new open-status review.', '',
    ]
    for area in data['areas']:
        cards = [card for card in selected if card['area'] == area['area']]
        if not cards:
            continue
        lines.extend([f"## {area.get('label', area['area'])} ({len(cards)})", ''])
        for card in sorted(cards, key=lambda c: c['importance_rank']):
            summary = card['working_summary']
            lines.extend([
                f"### {card['id']} — {card['title']}", '',
                ' '.join(summary['sentences']), '',
            ])
            refs = {ref['id']: ref for ref in card['references']}
            sources = [refs[ref] for ref in summary['source_refs']] + summary.get('extra_sources', [])
            links = [f"[{ref['title'].replace('[', '(').replace(']', ')')}]({ref['url']})" for ref in sources]
            lines.extend([
                f"[Read in atlas](index.html#{card['id']}) · " + ' · '.join(links),
                f"Existing status: `{card['status']}` · Summary written: {summary['written_on']}", '',
            ])
    return '\n'.join(lines)
