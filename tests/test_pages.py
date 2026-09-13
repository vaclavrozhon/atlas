"""Exercise real deployment commits against a temporary bare Git remote."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import deploy_pages as pages

with tempfile.TemporaryDirectory(prefix='atlas-pages-test-') as directory:
    root = Path(directory)
    source, remote = root / 'source', root / 'remote.git'
    source.mkdir()
    site = source / 'site'
    site.mkdir()
    subprocess.run(['git', 'init', '--quiet', '--bare', str(remote)], check=True)
    pages.git(source, 'init', '--quiet', '--initial-branch', 'main')
    pages.git(source, 'config', 'user.name', 'Pages test')
    pages.git(source, 'config', 'user.email', 'pages@example.invalid')
    pages.git(source, 'remote', 'add', 'origin', str(remote))
    (source / 'working-note.txt').write_text('Local unpublished work')
    pages.git(source, 'add', 'working-note.txt')
    index = (source / '.git/index').read_bytes()
    for name in ['index.html', 'style.css', 'app.js', 'community.js', 'votes.js', 'math.js',
                 'map.html', 'map.js', 'map.css', 'vendor/d3.min.js', 'data.js', '.nojekyll', 'old-file.txt']:
        (site / name).parent.mkdir(parents=True, exist_ok=True)
        (site / name).write_text('' if name == '.nojekyll' else 'Fixture')

    def version(value):
        (site / 'version.json').write_text(json.dumps({'version': value}))
        (site / 'catalog.json').write_text(json.dumps({'meta': {'version': value}, 'cards': [], 'areas': []}))

    def head():
        return pages.git(remote, 'rev-parse', 'refs/heads/gh-pages')

    with patch.object(pages, 'BASE', source), patch.object(pages, 'SITE', site), patch.object(sys, 'argv', ['deploy_pages.py']):
        version('first')
        pages.main()
        first = head()
        files = pages.git(remote, 'ls-tree', '-r', '--name-only', first).splitlines()
        assert {'index.html', 'map.html', 'map.js', 'map.css', 'vendor/d3.min.js', '.nojekyll'} <= set(files)
        assert 'working-note.txt' not in files and not any(name.startswith('site/') for name in files)
        pages.main()
        assert head() == first, 'Unchanged content must not create a deployment commit'
        version('second')
        (site / 'old-file.txt').unlink()
        (site / 'new-file.txt').write_text('New asset')
        pages.main()
        second = head()
        assert pages.git(remote, 'rev-parse', second + '^') == first
        files = pages.git(remote, 'ls-tree', '-r', '--name-only', second).splitlines()
        assert 'old-file.txt' not in files and 'new-file.txt' in files
        assert pages.git(source, 'symbolic-ref', 'HEAD') == 'refs/heads/main'
        assert (source / '.git/index').read_bytes() == index
        assert (source / 'working-note.txt').read_text() == 'Local unpublished work'
        (site / 'version.json').write_text(json.dumps({'version': 'incomplete'}))
        try:
            pages.snapshot(root / 'invalid-snapshot')
        except ValueError:
            pass
        else:
            raise AssertionError('Incomplete publication must be rejected')

print(json.dumps({'checks': ['first deployment', 'unchanged deployment', 'history-preserving update',
    'removed files disappear', 'source branch and staged work preserved', 'incomplete publication rejected']}))
