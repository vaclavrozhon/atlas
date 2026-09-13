"""Repository paths for scripts run from any working directory."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
CARDS = DATA / 'cards'
ARCHIVE = DATA / 'archive'
ARCHIVED_CARDS = ARCHIVE / 'cards'
WEB = ROOT / 'web'
BUILD = ROOT / 'build'
