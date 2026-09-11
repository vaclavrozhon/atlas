"""Recorded title-review corrections to the transparent candidate classifier.
Numbers are stable proceedings-order record IDs, not a ranking of papers.
Abstract-dependent decisions are recorded separately in abstract_overrides.json.
"""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
DECISIONS={
'FOCS-2021':{
'crypto':[5], 'fg':[8,92], 'avg':[28,29], 'ds':[34], 'online':[47],
'game':[75,76], 'lattice':[99], 'graph':[104], 'cx':[109],
},
'FOCS-2022':{
'count':[12,14], 'cx':[15], 'alg':[19], 'q':[31,77], 'fg':[51],
'general':[73], 'learn':[74], 'ds':[89,90], 'crypto':[96], 'graph':[99],
'dist':[102], 'comm':[107],
},
'FOCS-2023':{
'proof':[2,74], 'geom':[8,77], 'game':[12], 'approx':[17,133,134],
'csp':[20], 'alg':[21,73], 'param':[38], 'cx':[42,58],
'graph':[46,48], 'learn':[61,123], 'prg':[68], 'comb':[71],
'dyn':[99], 'ds':[105,135], 'opt':[113], 'dp':[118],
},
'FOCS-2024':{
'graph':[3,6,93,116], 'approx':[13,98], 'comp':[21], 'cx':[24,132],
'q':[29,63], 'proof':[31,49,50], 'alg':[33,45,81,117,119,129],
'ds':[36,38,113], 'prg':[47], 'learn':[53,56,57,66,94,105],
'crypto':[69,71], 'game':[73,75], 'comb':[82,85], 'avg':[92],
'geom':[95,106], 'code':[100,101], 'online':[108], 'dist':[118], 'param':[121],
},
'FOCS-2025':{
'comb':[1,9,102,105], 'q':[2,50,63], 'online':[6,89,121],
'geom':[11,115], 'game':[14,18,99,119], 'cx':[16,19,56,103],
'graph':[20,48,132,134], 'alg':[21,66,92,108,113], 'avg':[22,101,128],
'learn':[28,57,78,130], 'ds':[35,49,120,124], 'dyn':[36],
'opt':[46,90,104,118], 'proof':[61,100,127], 'csp':[64,123],
'comm':[74], 'count':[91], 'dist':[93], 'crypto':[94,125,129],
'stream':[97], 'param':[137],
},
'STOC-2022':{
'q':[2,63], 'general':[6], 'online':[8,93], 'ds':[14,86],
'stream':[25], 'approx':[26], 'alg':[33,92], 'comb':[36,52],
'dist':[41], 'opt':[44,46], 'csp':[56], 'game':[58,59,60],
'crypto':[65,66,108], 'learn':[68,100,101,102,130], 'code':[77,109],
'proof':[81], 'cx':[82,94,96], 'geom':[84,85], 'dyn':[88],
'comm':[98], 'count':[114,115,116], 'fg':[118,120,121],
},
'STOC-2023':{
'prg':[1,4], 'count':[10,111], 'opt':[11,153,154], 'graph':[17,18,69,79,83,149],
'online':[21,29,30,48,65,66], 'dist':[27], 'fg':[32,113], 'alg':[35,36,37],
'dp':[40], 'comb':[54,55,70,78,147], 'game':[56,60,61,62,151],
'cx':[71,88], 'q':[77], 'learn':[82,136,140], 'dyn':[97], 'crypto':[102,124,126],
'top':[104], 'sched':[109], 'avg':[110], 'ds':[115], 'geom':[143],
},
'STOC-2024':{
'graph':[8,63,143], 'alg':[10,11,12,13,80,101,145], 'learn':[15,32,94,98,153,163],
'dp':[16], 'online':[17,44,112,150], 'game':[19,20,22,42], 'param':[24,25],
'approx':[26,148], 'crypto':[40,157,160], 'fg':[41,77,78], 'count':[47,84,100,154,156],
'avg':[50,99], 'cx':[56,81,110,116,125,129], 'proof':[58,132,181,182,185,186],
'comm':[59,118,119,176], 'code':[69,146], 'ds':[72,74,86,105], 'q':[93,120,138],
'dyn':[108], 'prg':[117,188], 'comb':[130,180], 'opt':[170], 'csp':[178],
},
'STOC-2025':{
'cx':[2,48,52,105,130], 'graph':[3,12,32,204,212], 'approx':[6,60,61,109,110],
'csp':[8], 'proof':[11,55,104,129], 'count':[13,83,99,106],
'crypto':[20,91,93,153,174,175], 'ds':[25,26,27,111,208,209], 'avg':[30,85],
'comb':[31,79,160], 'stream':[35], 'alg':[45,72,73,74,75,101,103],
'game':[46,47,144,145,146,148], 'comm':[53,54], 'q':[68,77,114,117,138],
'opt':[88,206], 'test':[98], 'dist':[124], 'online':[135,136,186],
'learn':[157,158,161,163,164,165,166,188,191,207], 'prg':[168],
'param':[197,198], 'geom':[214,215], 'dp':[216,217],
},
'STOC-2026':{
'game':[9,17,38,67,98,121,160], 'lattice':[11,84,159], 'proof':[15,29,74,85,90],
'alg':[18,106,135,155], 'avg':[19,35,163,185], 'geom':[21,25,66,96,197],
'opt':[22,50], 'ds':[23,65,95,103,104,124], 'stream':[24,209], 'q':[31,80,82,118,202],
'code':[36,138], 'learn':[37,72,100,111,156,194,199], 'comb':[41,42],
'graph':[62,127,132], 'online':[73,78,144,152], 'dist':[88], 'count':[91,93,109],
'param':[122], 'comp':[148], 'crypto':[151,170,186,196], 'approx':[172,200],
'cx':[177,191], 'comm':[187], 'sched':[192], 'fg':[193],
},
}
out={}
for prefix,groups in DECISIONS.items():
    for area,ns in groups.items():
        for n in ns:
            key=f'{prefix}-{n:03d}'
            assert key not in out,key
            out[key]={'area':area,'method':'reviewed_title','note':'Primary subject selected in title review; overlapping techniques do not receive additional counts.'}
if (BASE/'abstract_overrides.json').exists():
    out.update(json.loads((BASE/'abstract_overrides.json').read_text()))
(BASE/'overrides.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
