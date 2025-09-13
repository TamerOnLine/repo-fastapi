from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration settings using pydantic.

    Environment variables can be prefixed with 'APP_' and read from a .env file.
    """

    # ================================
    # Basic service configuration
    # ================================
    APP_NAME: str = "NeuroServe"
    ENV: str = Field("development", description="development | staging | production")
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    # ================================
    # Logging configuration
    # ================================
    LOG_LEVEL: str = "info"  # root/console level
    LOG_LEVEL_UVICORN: str = "warning"  # uvicorn.access
    LOG_LEVEL_PLUGINS: str = "info"  # plugins file
    LOG_CONSOLE_FORMAT: str = "%(asctime)s %(levelname)s [%(name)s] %(message)s"

    LOG_ERRORS_TO_FILE: bool = True
    ERROR_LOG_FILE: Path = Path("logs/errors.log")
    ERROR_LOG_MAX_BYTES: int = 1_048_576  # 1 MB
    ERROR_LOG_BACKUPS: int = 5

    LOG_PLUGINS_TO_FILE: bool = True
    PLUGINS_LOG_FILE: Path = Path("logs/plugins.log")

    # ================================
    # Device configuration
    # ================================
    DEVICE: str = Field(default="cuda:0", description="e.g., 'cuda:0', 'cpu', 'mps' (macOS), 'cuda:1', etc.")

    # ================================
    # Model cache paths
    # ================================
    MODEL_CACHE_ROOT: Path = Path("models_cache")
    HF_HOME: Optional[Path] = None
    TORCH_HOME: Optional[Path] = None
    TRANSFORMERS_CACHE: Optional[Path] = None

    # ================================
    # Static, templates, and upload directories
    # ================================
    STATIC_DIR: Path = Path("app/static")
    TEMPLATES_DIR: Path = Path("app/templates")
    UPLOAD_DIR: Path = Path("uploads")

    # ================================
    # CORS configuration
    # ================================
    CORS_ALLOW_ORIGINS: List[str] = Field(default_factory=lambda: ["*"])
    CORS_ALLOW_METHODS: List[str] = Field(default_factory=lambda: ["*"])
    CORS_ALLOW_HEADERS: List[str] = Field(default_factory=lambda: ["*"])
    CORS_ALLOW_CREDENTIALS: bool = False

    # ================================
    # Database (optional)
    # ================================
    DB_URL: Optional[str] = None  # Example: postgresql+psycopg://user:pass@host:5432/dbname

    # ================================
    # JWT security (optional)
    # ================================
    JWT_SECRET: Optional[str] = None
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24

    # ================================
    # pydantic-settings configuration
    # ================================
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_", case_sensitive=False, extra="ignore")

    # ================================
    # Validators
    # ================================
    @field_validator("HF_HOME", "TORCH_HOME", "TRANSFORMERS_CACHE", mode="before")
    @classmethod
    def default_cache_dirs(cls, v, info):
        """
        Set default subdirectories under MODEL_CACHE_ROOT for caching.
        """
        if v in (None, "", "None"):
            root = info.data.get("MODEL_CACHE_ROOT") or Path("models_cache")
            name = info.field_name.lower()
            if name == "hf_home":
                return Path(root) / "huggingface"
            if name == "torch_home":
                return Path(root) / "torch"
            if name == "transformers_cache":
                return Path(root) / "huggingface" / "hub"
        return Path(v) if isinstance(v, str) else v

    @field_validator(
        "MODEL_CACHE_ROOT", "STATIC_DIR", "TEMPLATES_DIR", "UPLOAD_DIR", "ERROR_LOG_FILE", "PLUGINS_LOG_FILE"
    )
    @classmethod
    def ensure_path(cls, v: Path):
        """
        Ensure the input value is converted to a Path object.
        """
        return Path(v)

    # ================================
    # Utilities
    # ================================
    def ensure_directories(self) -> None:
        """
        Create required directories if they do not exist.
        """
        for p in [
            self.MODEL_CACHE_ROOT,
            self.HF_HOME,
            self.TORCH_HOME,
            self.TRANSFORMERS_CACHE,
            self.STATIC_DIR,
            self.TEMPLATES_DIR,
            self.UPLOAD_DIR,
            self.ERROR_LOG_FILE.parent,
            self.PLUGINS_LOG_FILE.parent,
        ]:
            if p:
                Path(p).mkdir(parents=True, exist_ok=True)

    def export_env_for_caches(self) -> None:
        """
        Export cache directory paths to environment variables for libraries to respect them.
        """
        os.environ.setdefault("HF_HOME", str(self.HF_HOME))
        os.environ.setdefault("TORCH_HOME", str(self.TORCH_HOME))
        os.environ.setdefault("TRANSFORMERS_CACHE", str(self.TRANSFORMERS_CACHE))
        os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")

    def summary(self) -> dict:
        """
        Generate a summary dictionary useful for /env or /health endpoints.

        Returns:
            dict: A dictionary summarizing key environment and config information.
        """
        return {
            "app": self.APP_NAME,
            "env": self.ENV,
            "host": self.HOST,
            "port": self.PORT,
            "device": self.DEVICE,
            "model_cache_root": str(self.MODEL_CACHE_ROOT),
            "hf_home": str(self.HF_HOME),
            "torch_home": str(self.TORCH_HOME),
            "transformers_cache": str(self.TRANSFORMERS_CACHE),
            "static_dir": str(self.STATIC_DIR),
            "templates_dir": str(self.TEMPLATES_DIR),
            "upload_dir": str(self.UPLOAD_DIR),
            "db_url": bool(self.DB_URL),
            "jwt_enabled": bool(self.JWT_SECRET),
            "logs": {
                "console": self.LOG_LEVEL,
                "errors_file": str(self.ERROR_LOG_FILE) if self.LOG_ERRORS_TO_FILE else None,
                "plugins_file": str(self.PLUGINS_LOG_FILE) if self.LOG_PLUGINS_TO_FILE else None,
            },
        }


@lru_cache
def get_settings() -> Settings:
    """
    Cached singleton pattern to load application settings once.

    Returns:
        Settings: A cached instance of the application settings.
    """
    settings = Settings()
    settings.ensure_directories()
    settings.export_env_for_caches()
    return settings
