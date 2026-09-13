import json,sys,time,re
from pathlib import Path
import requests

version,commit,*ids=sys.argv[1:]
assert re.fullmatch(r"[0-9a-f]{40}",commit), "A full deployment commit is required"
root=Path('/home/vasek/atlas');base='https://vaclavrozhon.github.io/atlas/'
stamp=str(time.time_ns())
marker=requests.get(base+'version.json?quality='+stamp,timeout=30);marker.raise_for_status();marker=marker.json()
response=requests.get(base+'catalog.json?quality='+stamp,timeout=45);response.raise_for_status();catalog=response.json()
assert marker['version']==catalog['meta']['version'],(marker,catalog['meta']['version'])
assert catalog['meta']['version']==version,('expected deployment not yet live',version,catalog['meta']['version'])
cards={c['id']:c for c in catalog['cards']}
p=root/'research/card-quality-20260911/live-verification.json';report=json.loads(p.read_text())
for id in ids:
 local=json.loads((root/'data/cards'/f'{id}.json').read_text());c=cards[id]
 for field in ['formal','definitions','working_summary','quality_review','status']:
  assert c.get(field)==local.get(field),(id,field)
 report['cards'][id]={'status':c['status'],'quality_state':c['quality_review']['state']}
report.update(checked_on='2026-09-12',version_marker=marker,catalogue_version=catalog['meta']['version'])
p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
p=root/'research/card-quality-20260911/README.md';s=p.read_text()
if commit not in s:
 sentence=f"Deployment `{commit}` publishes catalogue `{version}`, including {', '.join(ids)}; these cards were read back from the public catalogue. "
 s=s.replace('`live-verification.json` records public read-back evidence.',sentence+'`live-verification.json` records public read-back evidence.')
 p.write_text(s)
print(json.dumps({'verified':ids,'version':catalog['meta']['version'],'deployment':commit}))
