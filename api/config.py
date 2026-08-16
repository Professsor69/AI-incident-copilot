"""
Application configuration — loaded from environment variables via pydantic-settings.

All secrets and tuneable parameters live here. Never hardcode API keys.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application-wide settings loaded from .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── API Keys ────────────────────────────────────────────────────────────
    google_api_key: str = ""
    openai_api_key: str = ""

    # ── Langfuse Observability ───────────────────────────────────────────────
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_host: str = "https://cloud.langfuse.com"

    # ── Storage Paths ────────────────────────────────────────────────────────
    sqlite_db_path: str = "data/incident_db.sqlite"
    chroma_db_path: str = "data/chroma_db"

    # ── Redis ────────────────────────────────────────────────────────────────
    redis_url: str = "redis://localhost:6379"

    # ── App Settings ─────────────────────────────────────────────────────────
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"

    # ── Model Selection ───────────────────────────────────────────────────────
    agent_llm_model: str = "gemini-2.5-flash"
    eval_judge_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    # ── Rate Limiting ─────────────────────────────────────────────────────────
    rate_limit_requests: int = 10
    rate_limit_window_seconds: int = 60

    # ── Caching ───────────────────────────────────────────────────────────────
    cache_ttl_seconds: int = 300

    @property
    def is_development(self) -> bool:
        """Return True if running in development mode."""
        return self.app_env.lower() == "development"


# Singleton instance — import this throughout the codebase
settings = Settings()
