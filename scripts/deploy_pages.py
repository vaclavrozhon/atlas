"""Push a consistent static reader snapshot to the GitHub Pages branch.

The temporary checkout contains only build/ output and follows the existing remote
deployment history. The source checkout, its index and its branches are untouched.
Enable Pages once with gh-pages as the branch and / as its source directory.
"""

import argparse
import fcntl
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from paths import ROOT, BUILD

BASE = ROOT
SITE = BUILD


def git(directory, *arguments):
    return subprocess.check_output(['git', '-C', str(directory), *arguments], text=True).strip()


def snapshot(destination):
    with (BASE / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        files = [path for path in SITE.rglob('*') if path.is_file()]
        if any(path.is_symlink() for path in SITE.rglob('*')):
            raise ValueError('The published reader must not contain symbolic links')
        if any(path.stat().st_size >= 100 * 1024**2 for path in files):
            raise ValueError('A reader file exceeds the GitHub Git-file size limit')
        version = json.loads((SITE / 'version.json').read_text())['version']
        catalogue = json.loads((SITE / 'catalog.json').read_text())
        if catalogue['meta']['version'] != version:
            raise ValueError('Incomplete publication: catalogue and version marker disagree')
        for name in ['index.html', 'style.css', 'app.js', 'community.js', 'votes.js', 'math.js',
                     'map.html', 'map.js', 'map.css', 'vendor/d3.min.js', 'data.js', '.nojekyll']:
            if not (SITE / name).is_file():
                raise ValueError(f'Missing reader asset: {name}')
        shutil.copytree(SITE, destination, dirs_exist_ok=True)
        return dict(version=version, files=len(files), bytes=sum(p.stat().st_size for p in files),
                    records=len(catalogue['cards']), categories=len(catalogue['areas']))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--remote', default='origin')
    parser.add_argument('--branch', default='gh-pages')
    parser.add_argument('--dry-run', action='store_true', help='Validate and copy the snapshot without pushing')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='atlas-pages-') as directory:
        checkout = Path(directory)
        if args.dry_run:
            print(json.dumps(dict(snapshot(checkout), dry_run=True)))
            return
        remote = git(BASE, 'remote', 'get-url', '--push', args.remote)
        name = git(BASE, 'config', 'user.name')
        email = git(BASE, 'config', 'user.email')
        git(checkout, 'init', '--quiet', '--initial-branch', args.branch)
        git(checkout, 'config', 'user.name', name)
        git(checkout, 'config', 'user.email', email)
        git(checkout, 'remote', 'add', 'origin', remote)
        reference = f'refs/heads/{args.branch}'
        if git(checkout, 'ls-remote', '--heads', 'origin', reference):
            git(checkout, 'fetch', '--quiet', '--depth=1', 'origin', reference)
            git(checkout, 'reset', '--mixed', 'FETCH_HEAD')
        report = snapshot(checkout)
        git(checkout, 'add', '--all')
        changes = subprocess.run(['git', '-C', str(checkout), 'diff', '--cached', '--quiet']).returncode
        if changes not in (0, 1):
            raise RuntimeError('Cannot compare the deployment snapshot')
        if changes:
            git(checkout, 'commit', '--quiet', '-m', f"Publish atlas {report['version']}")
            # A concurrent deployment is rejected by this ordinary, non-forced push.
            git(checkout, 'push', 'origin', f'HEAD:{reference}')
        report.update(branch=args.branch, commit=git(checkout, 'rev-parse', 'HEAD'), changed=bool(changes))
        print(json.dumps(report))


if __name__ == '__main__':
    main()
