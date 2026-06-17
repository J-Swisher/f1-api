"""F1 Terminal backend package.

Importing this package configures the f1-db data location (so the read-only
``f1db`` query client finds its SQLite files) *before* anything imports ``f1db``
— its ``config`` module reads ``os.environ`` at import time.
"""
from __future__ import annotations

from f1_terminal.config import configure_f1db_env, settings

__version__ = "0.1.0"

# Must run before any `import f1db...` happens elsewhere in the package.
configure_f1db_env()

__all__ = ["settings", "configure_f1db_env", "__version__"]
