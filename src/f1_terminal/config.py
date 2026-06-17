"""Application settings (pydantic-settings) + f1-db environment wiring.

The read-only ``f1db`` dependency resolves its SQLite paths from ``F1DB_*``
environment variables at import time (see ``external/f1-db/src/f1db/config.py``).
We let the user configure those via ``.env`` / settings here, then export them to
``os.environ`` before ``f1db`` is imported (done in ``f1_terminal/__init__.py``).
"""
from __future__ import annotations

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # --- f1-db (read-only source) location -------------------------------
    # Directory holding the built f1.db / f1_telemetry.db. The submodule ships
    # code only, so this typically points at a separate clone's data dir.
    f1db_data_dir: Path | None = Field(default=None)
    f1db_core_path: Path | None = Field(default=None)
    f1db_telemetry_path: Path | None = Field(default=None)

    # --- the terminal's own app database (separate from f1-db) ------------
    app_db_path: Path = Field(default=Path("data/f1_terminal.db"))

    # --- API --------------------------------------------------------------
    cors_origins: str = Field(default="http://localhost:5173,http://localhost:3000")

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()


def configure_f1db_env() -> None:
    """Export configured ``F1DB_*`` paths into the process environment.

    Uses ``setdefault`` so a value already present in the real environment (or set
    by the test harness) wins over the ``.env``-derived setting.
    """
    if settings.f1db_data_dir is not None:
        os.environ.setdefault("F1DB_DATA_DIR", str(settings.f1db_data_dir))
    if settings.f1db_core_path is not None:
        os.environ.setdefault("F1DB_CORE_PATH", str(settings.f1db_core_path))
    if settings.f1db_telemetry_path is not None:
        os.environ.setdefault("F1DB_TELEMETRY_PATH", str(settings.f1db_telemetry_path))
