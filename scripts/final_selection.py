"""Publish the initial review proposal; shared manual choices live in the service."""
import hashlib
import json
from paths import DATA


def apply_final_selection(data):
    source = json.loads((DATA / 'final_selection.json').read_text())
    if source.get('targets') != {'large': 25, 'small': 10}:
        raise ValueError('Expected final-selection targets 25/10')
    areas = {a['area']: a for a in data['areas']}
    manifest = dict(targets=source['targets'], categories={
        name: dict(id=a['id'], group=a['group'], label=a['label']) for name,a in areas.items()}, cards={})
    unreviewed = []
    for card in data['cards']:
        identifier, area = card['id'], card['area']
        entry = source['cards'].get(identifier)
        if entry is None:
            # New imports are visible as red until reviewed; publication never
            # invents green choices or rewrites previous human choices.
            entry = {'color': 'red'}
            unreviewed.append(identifier)
        if entry.get('color') not in {'green', 'red'}:
            raise ValueError(f'{identifier}: invalid selection color')
        options = [area]
        alternate = entry.get('alternate_area')
        if alternate:
            if alternate == area or alternate not in areas or areas[alternate]['group'] == areas[area]['group']:
                raise ValueError(f'{identifier}: category pair needs one large and one small category')
            options.append(alternate)
        value = dict(color=entry['color'], area=area, area_options=options)
        if entry.get('upvoted_red_reason'):
            value['upvoted_red_reason'] = entry['upvoted_red_reason']
        manifest['cards'][identifier] = value
        card['selection'] = value.copy()
        # The feedback archive retains this verbatim material. It is not part
        # of the final reader or its machine-readable catalogue.
        card.pop('community_reviews', None)
    serialized = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    manifest['version'] = hashlib.sha256(serialized.encode()).hexdigest()[:20]
    data['meta']['final_selection'] = dict(version=manifest['version'],
        reviewed_on=source['reviewed_on'], targets=source['targets'],
        green=sum(c['color']=='green' for c in manifest['cards'].values()),
        red=sum(c['color']=='red' for c in manifest['cards'].values()),
        unreviewed_ids=unreviewed)
    data['meta']['community_public'] = False  # Archived feedback stays outside the reader.
    data['meta']['public_comments'] = True
    return manifest


if __name__ == '__main__':
    import argparse
    from pathlib import Path
    from publish import load_catalog
    from taxonomy import apply_taxonomy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True,
                        help='Write the server-only module for the shared-selection service.')
    args = parser.parse_args()
    data = load_catalog()
    apply_taxonomy(data)
    manifest = apply_final_selection(data)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text('export const selectionManifest = ' +
        json.dumps(manifest, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print(json.dumps(dict(version=manifest['version'], cards=len(manifest['cards']))))
