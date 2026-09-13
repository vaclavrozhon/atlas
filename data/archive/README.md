# Inactive cards

`cards/TCS-XXXX.json` preserves the complete content of an inactive card.
`index.json` maps inactive IDs to editorial reasons; all IDs and historical
import keys remain reserved. `activity.jsonl` records archival and explicit
restoration decisions. `recovery.json` records the provenance and limits of
the one-time historical recovery on 13 September 2026.

The archive is outside routine editorial work, formulation and source reviews,
validation, ranking, benchmark selection, publication and ordinary imports.
Do not scan or update these cards as part of improving the atlas. Old formats
are preserved without requiring schema repairs. Ordinary build/check commands
use only the index and, when needed, filenames to prevent accidental reactivation.
The local `.ignore` also excludes this directory from ordinary ripgrep searches;
it does not exclude the archive from Git. Explicit archival searches can use
`rg --no-ignore` when the user requests them.

Use `python3 scripts/archive_cards.py TCS-0123 --reason 'Specific reason.'`
from the repository root to deactivate an active card without losing content.
Only an explicit user request authorizes inspecting archived content or using
the same command with `--restore`. Restoration checks the requested card against
current active requirements and retains its original identity. See
[the data workflow](../README.md) and [the manifest](../../docs/MANIFEST.md).
