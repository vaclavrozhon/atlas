"""Reinstate selected records without replacing their current text or stable IDs."""
import argparse,datetime,fcntl,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE))
from publish import _publish,atomic

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids',nargs='*',help='Stable IDs, for example TCS-1165')
    parser.add_argument('--all',action='store_true',help='Reinstate every still-quarantined record in this batch')
    parser.add_argument('--dry-run',action='store_true',help='Show the operation without changing any file')
    args=parser.parse_args()
    if not args.ids and not args.all:parser.error('Provide IDs or --all')
    if args.ids and args.all:parser.error('Use either IDs or --all')
    with (BASE/'.publish.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        path=HERE/'manifest.json';manifest=json.loads(path.read_text());records=manifest['records']
        ids=sorted(i for i,r in records.items() if r['state']=='quarantined') if args.all else sorted(set(args.ids))
        missing=set(ids)-records.keys()
        if missing:parser.error('IDs are not in this quarantine batch: '+', '.join(sorted(missing)))
        changed=[i for i in ids if records[i]['state']=='quarantined']
        if args.dry_run:
            print(json.dumps(dict(dry_run=True,restore=changed,count=len(changed)),indent=2));return
        if not changed:
            print(json.dumps(dict(restored=[],message='These records are already retained.')));return
        now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
        for id in changed:records[id].update(state='retained',restored_at=now)
        manifest.setdefault('restorations',[]).append(dict(date=now,ids=changed))
        atomic(path,json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        _publish()
        print(json.dumps(dict(restored=changed,count=len(changed)),indent=2))

if __name__=='__main__':main()
