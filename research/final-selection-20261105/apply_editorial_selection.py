"""Apply the explicit per-category review; never consult or overwrite live edits."""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
RESEARCH = ROOT / 'research/final-selection-20261105'


def read(path):
    return json.loads(path.read_text())


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    reviews = read(RESEARCH / 'editorial-choices.json')
    registry = read(ROOT / 'data/categories.json')
    categories = {a['id']: dict(a, group=g['id']) for g in registry['groups'] for a in g['categories']}
    cards = {p.stem: read(p) for p in (ROOT / 'data/cards').glob('*.json')}
    chosen = {}
    for slug, review in reviews['areas'].items():
        category = categories[slug]
        target = 25 if category['group'] == 'large' else 10
        assert len(review['green']) == target, slug
        for identifier in review['green']:
            assert identifier not in chosen, identifier
            chosen[identifier] = category['key']
    assert set(reviews['areas']) == set(categories)

    moves = {m['id']: m for m in reviews['moves']}
    assert len(moves) == len(reviews['moves'])
    before = {}
    for identifier, move in moves.items():
        card = cards[identifier]
        if card['area'] != move['to']:
            before[identifier] = dict(area=card['area'], category_assignment=card.get('category_assignment'))
            card['area'] = move['to']
            card['category_assignment'] = dict(method='editorial_topic', reviewed_on=reviews['reviewed_on'], reason=move['reason'])
    for identifier, area in chosen.items():
        assert cards[identifier]['area'] == area, (identifier, area)

    # These are intentionally selected pairs, not a general category picker.
    # Every pair has exactly one large category and one small category.
    pairs = {}

    def pair(large, small, ids):
        assert categories[large]['group'] == 'large' and categories[small]['group'] == 'small'
        options = [categories[large]['key'], categories[small]['key']]
        for suffix in ids.split():
            identifier = 'TCS-' + suffix
            assert identifier not in pairs, identifier
            assert cards[identifier]['area'] in options, (identifier, options)
            pairs[identifier] = options

    pair('complexity', 'computability', '7159 7256')
    pair('complexity', 'proof', '6663 6601 7162 0025 5332')
    pair('semantics', 'proof', '1099 1098')
    pair('complexity', 'communication', '6603 6604 5326 5892 6710')
    pair('quantum', 'communication', '6605 6450')
    pair('learning', 'communication', '6581')
    pair('complexity', 'fine', '6595 6935 7313')
    pair('ads', 'fine', '6510 0557 6503 7179 6596 6598 6597 6937')
    pair('complexity', 'randomness', '0003 0026 6600 6699')
    pair('ads', 'randomness', '6662 5798')
    pair('complexity', 'parameterized', '6592 6593 6731')
    pair('ads', 'parameterized', '7233 4790 6594 6660 7035 7181 7241')
    pair('complexity', 'approximation', '0006 7160 7281')
    pair('ads', 'approximation', '6587 6588 7266 7282 7356 7358 6591 6659')
    pair('optimization', 'approximation', '5407')
    pair('geometry', 'approximation', '7353')
    pair('optimization', 'online', '7316')
    pair('geometry', 'online', '6576')
    pair('ads', 'online', '6638 7317 6721 6575 6676')
    pair('learning', 'online', '6577 7319')
    pair('complexity', 'beyond', '0012')
    pair('learning', 'beyond', '6656 6657 6684 5011')
    pair('optimization', 'beyond', '6658 7148')
    pair('ads', 'beyond', '7381 7388 7378 7379')
    pair('ads', 'sampling', '6621 6622 7404 6857')
    pair('complexity', 'counting', '6820 7221')
    pair('ads', 'counting', '6628 6629 7112 0805')
    pair('geometry', 'counting', '7240')
    pair('semantics', 'structural', '6654')
    pair('ads', 'structural', '6683')
    pair('ads', 'graph-algorithms', '7222 6536 6538 7228 7263 7343 6511 6539 7180 7285 7341 7346 0589 7342 7348 7394 0611 0771 0775 7344 7345 0594')
    pair('complexity', 'graph-algorithms', '6817')
    pair('ads', 'data-structures', '6498 6540 7331 7398 7334 5411 0300 7328 7497 7329 6586 7333 6508 0474')
    pair('ads', 'dynamic', '6625 6627 0478 6626 6670 7339 7495 7387 7326')
    pair('semantics', 'dynamic', '7437 7436 7494')
    pair('ads', 'strings', '6624 7322 7235 6623 6513 6669 7371 7367 7374 7375 0467 0468 7370')
    pair('geometry', 'strings', '7297')
    pair('optimization', 'game', '6639 0056 6674')
    pair('ads', 'algebra', '0007 7174 7113 6614 6615 7224')
    pair('geometry', 'algebra', '0055')
    pair('optimization', 'algebra', '4949')
    pair('complexity', 'algebraic-complexity', '0005 6888 6611 6666 6895 7262 1058 7321 1101 6890 0009 0010 1254')
    pair('semantics', 'lattices', '6571')
    pair('crypto', 'lattices', '6617 6618 6667 6864')
    pair('quantum', 'lattices', '7169 7234')
    pair('complexity', 'lattices', '0651')
    pair('ads', 'lattices', '6619 7265')
    pair('ads', 'coding', '1012 0013')
    pair('complexity', 'coding', '1020')
    pair('learning', 'testing', '5443 0672 3906')
    pair('parallel', 'testing', '6630 1033 1029 0848 4376 7384 7396 6672')
    pair('geometry', 'testing', '7385')
    pair('complexity', 'csp', '6635 6675 1807 6748 3678')
    pair('semantics', 'csp', '6636 7116')
    pair('ads', 'csp', '6637')
    pair('optimization', 'csp', '1555')
    pair('parallel', 'database', '6380')
    pair('ads', 'database', '6645')
    pair('semantics', 'database', '6680 0492 0494 0495')
    pair('automata', 'misc', '7518 7522')
    pair('ads', 'misc', '7177')

    selections = {}
    votes = {v['problem_id']: v for v in read(RESEARCH / 'votes.json')['votes']}
    for identifier, card in sorted(cards.items()):
        selection = dict(color='green' if identifier in chosen else 'red')
        if identifier in pairs:
            selection['alternate_area'] = next(a for a in pairs[identifier] if a != card['area'])
        if votes.get(identifier, {}).get('up') and identifier not in chosen:
            selection['upvoted_red_reason'] = reviews['upvoted_red'][identifier]
        selections[identifier] = selection
    assert len(chosen) == 500

    # Persist reviewed source changes and the default proposal only. Live manual
    # overrides are stored independently by the service and never touched here.
    for identifier in before:
        save(ROOT / 'data/cards' / (identifier + '.json'), cards[identifier])
    if before:
        archive_path = RESEARCH / 'selection-moves-before.json'
        assert not archive_path.exists(), 'Refuse to overwrite the before-image.'
        save(archive_path, before)
    save(ROOT / 'data/final_selection.json', dict(version=1, reviewed_on=reviews['reviewed_on'],
        targets=dict(large=25, small=10), cards=selections))
    focus = read(ROOT / 'data/benchmark_selection.json')
    for review in focus['areas']:
        review['selected'] = [entry for entry in review['selected'] if cards.get(entry['id'], {}).get('area') == review['area']]
        if review['area'] == categories['fine']['key'] and len(review['selected']) < 2:
            review['selected'].append(dict(id='TCS-0557', topic='Subquadratic 3SUM',
                reason='The canonical quadratic-time arithmetic barrier complements SETH after real-weight APSP moves to Algorithms.'))
    save(ROOT / 'data/benchmark_selection.json', focus)
    counts = collections.Counter(cards[i]['area'] for i in chosen)
    summary = dict(cards=len(cards), green=len(chosen), red=len(cards)-len(chosen), categories=len(categories),
        large=10, small=25, paired_cards=len(pairs), automatic_moves=len(moves),
        upvoted_red=[i for i,c in selections.items() if c.get('upvoted_red_reason')],
        resolved_green=[i for i in sorted(chosen) if cards[i]['status']=='resolved'],
        areas=[dict(id=slug, area=a['key'], label=a.get('label', a['key']),
            green=counts[a['key']], target=25 if a['group']=='large' else 10,
            candidates=sum(c['area']==a['key'] for c in cards.values()),
            minimum_green_importance=min(cards[i]['importance']['score'] for i in chosen if cards[i]['area']==a['key']))
            for slug,a in categories.items()])
    save(RESEARCH / 'selection-summary.json', summary)
    print({k:v for k,v in summary.items() if k!='areas'})


if __name__ == '__main__':
    main()
