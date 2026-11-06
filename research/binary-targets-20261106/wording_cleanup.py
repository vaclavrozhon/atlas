"""Align inherited prose with revised targets without a new status audit."""


def patch_card(number, *, replacements=(), contexts=None, titles=None, references=None):
    path = ROOT / 'data/cards' / f'TCS-{number}.json'
    d = json.loads(path.read_text())
    for field, old, new in replacements:
        assert old in d[field], (number, field, old)
        d[field] = d[field].replace(old, new)
    for index, value in (contexts or {}).items():
        d['context_blocks'][index]['text'] = value
    for index, value in (titles or {}).items():
        d['context_blocks'][index]['title'] = value
    for ref in d.get('references', []):
        if ref['id'] in (references or {}):
            ref.update(references[ref['id']])
    if 'context' in d and d.get('context_blocks'):
        d['context'] = '\n\n'.join(b['text'] for b in d['context_blocks'])
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


patch_card('0007', replacements=[('status_note',
    'The known interval displayed here remains wider than the requested numerical tolerance. A bounded primary-source search on 14 September 2026 found no verified determination at that precision.',
    'Those upper bounds do not establish the exponent-two assertion selected here. The recorded source search was bounded and took place on 14 September 2026.')])
patch_card('2336', replacements=[('status_note',
    'The source’s 2023 universal multiclass conjecture is retained as context for the previously authorized full minimax-rate target.',
    'The source’s 2023 universal multiclass conjecture is restored as the binary target.')])
patch_card('3906', replacements=[('status_note',
    'The minimax precision and exact-real computational primitives are explicitly recorded model specifications, not proof certification.',
    'The discrepancy, trajectory access and exact-real computational primitives are explicitly recorded model specifications, not proof certification.')])
patch_card('6575', replacements=[('status_note',
    'and hence settle the retained numerical target exactly.',
    'and establish the binary k-competitiveness assertion selected here.')])
patch_card('7317', replacements=[('status_note',
    'its explicitly quantitative constant-factor target',
    'the selected squared-logarithmic upper-bound target')],
    contexts={6: original('7317')['context_blocks'][6]['text'].replace(
        "this card's matching-asymptotics target", "the selected squared-logarithmic randomized upper bound")})
patch_card('6623', replacements=[('status_note',
    'Neither determines N_delta(n) up to constant factors.',
    'The cited quasipolynomial upper and polynomial lower bounds alone do not decide whether polynomially many traces suffice.')])
patch_card('6638', replacements=[('status_note',
    'Bounded searches found no determination of the infimum within absolute 1/100 or full matching solution claim. The known 3/2 lower bound assumes P differs from NP, while the quantity itself is unconditional. The tolerance target is an explicitly retained editorial reformulation; neither an old open-question statement nor absence of a search result independently certifies its current openness.',
    'The known 3/2 lower bound assumes P differs from NP. The selected existence question imposes no such hypothesis and asks for some fixed improvement below factor two. The historical bounded search does not independently certify present openness.')])
patch_card('6676', replacements=[('status_note',
    'No inspected result certifies the unconditional threshold to absolute 1/100.',
    'These conditional hardness statements do not unconditionally refute the selected existence question.')],
    contexts={12: r'The selected question asks whether some fixed positive improvement below factor two is possible in polynomial time. A qualifying algorithm settles it even if the optimal approximation ratio remains unknown. A negative answer requires an unconditional impossibility theorem; a conditional hardness statement must retain its hypothesis.'})
patch_card('7322', replacements=[('status_note',
    'They do not provide a tolerance-1/100 characterization of the unconditional numerical infimum.',
    'They do not settle the selected factor-two existence question for unrestricted algorithms.'),
    ('definitions', 'built into this numerical target.', 'built into this existence question.')])
patch_card('7337', replacements=[('status_note',
    ' The 1/100 tolerance is the atlas acceptance rule, not a tolerance proposed by these papers.', '')])
patch_card('7356', replacements=[('status_note',
    'Bounded primary-source checks through 17 September 2026 found no verified numerical determination of the unrestricted polynomial-time approximation infimum within 1/100. General approximation improvements, restricted-instance theorems and conditional hardness statements do not supply this unconditional two-sided estimate.',
    'The bounded primary-source checks through 17 September 2026 record improvements below factor 3/2, restricted-instance theorems and conditional hardness statements. The inspected results do not supply an unrestricted polynomial-time expected factor-4/3 algorithm or an unconditional refutation of its existence.')])
patch_card('6783', titles={3: 'The four-thirds sparsity target'})
patch_card('6710', contexts={2: r'For \(n\ge2\) and \(k\ge\max\{2,\lceil\log_2 n\rceil\}\), the 2020 result determines the communication cost as \(\Theta(1+\log_2 n/\log_2(1+k/\log_2 n))\), uniformly in that regime. The selected numerical exponent instead concerns each fixed player count as the universe size tends to infinity.',
    5: r'Each fixed player count has its own exponent and may use its own multiplicative constants. The answer must approximate every such exponent within \(1/100\), but no uniform control of these constants as the number of players grows is requested.'})
patch_card('7328', references={'charges': {
    'year': 2014, 'url': 'https://arxiv.org/abs/1110.4428v3',
    'locator': 'Revised 22 January 2014 expanded account of earlier SWAT 2000 work; Introduction and Figure 1, simultaneous charges and statement of Fredman’s lower bound'}})
patch_card('6590', replacements=[('status_note',
    'The 12 September 2026 edit adopts absolute 0.01 benchmark acceptance; the saved open-status evidence concerns the underlying exact question and does not independently certify openness at that tolerance.',
    'The 6 November 2026 formulation restores the factor-two conjecture. The recorded status checks retain their original dates and scope.'),
    ('definitions', r'c:V\times V\to R\ge 0', r'c:V\times V\to\mathbb R_{\ge0}')])

