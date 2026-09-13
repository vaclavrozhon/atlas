"""Check a snapshot of current inputs without modifying the working reader."""

import fcntl
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from paths import ROOT


def main():
    with tempfile.TemporaryDirectory(prefix='atlas-check-') as directory:
        snapshot = Path(directory)
        with (ROOT / '.publish.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            for name in ['data', 'scripts', 'web']:
                shutil.copytree(ROOT / name, snapshot / name, ignore=shutil.ignore_patterns('__pycache__'))
            (snapshot / 'tests').mkdir()
            for path in (ROOT / 'tests').glob('*.py'):
                shutil.copy2(path, snapshot / 'tests' / path.name)
        for script in ['scripts/publish.py', 'tests/ranking.py', 'tests/taxonomy.py', 'tests/test_related_problems.py',
                       'tests/test_publication.py', 'tests/test_pages.py']:
            subprocess.run([sys.executable, str(snapshot / script)], cwd=snapshot, check=True)


if __name__ == '__main__':
    main()
