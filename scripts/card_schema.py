"""Keep authored cards compact and derive reader-only fields at publication."""

OBSOLETE_FIELDS = {'rank', 'classification_method', 'importance_method'}
DERIVED_FIELDS = {'criterion_label', 'selection_group', 'selection_target',
                  'importance_rank', 'importance_count', 'benchmark_focus'}


def canonical_record(card):
    result = {key: value for key, value in card.items()
              if key not in OBSOLETE_FIELDS | DERIVED_FIELDS}
    if result.get('context_blocks'):
        context = '\n\n'.join(block['text'] for block in result['context_blocks'])
        if 'context' in result and result['context'] != context:
            raise ValueError('Context paragraphs and search text differ')
        result.pop('context', None)
    return result


def reader_record(card, criteria):
    result = canonical_record(card)
    if result.get('context_blocks'):
        result['context'] = '\n\n'.join(block['text'] for block in result['context_blocks'])
    if result.get('criterion') in criteria:
        result['criterion_label'] = criteria[result['criterion']]['label']
    return result
