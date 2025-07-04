from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables and config file."""
    
    model_config = SettingsConfigDict(
        env_file="config",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Environment settings
    env: str = "locally-local"
    namespace: str = "local"
    service_name: str = "fully-vibe-code"
    service_version: str = "locally-version"
    
    # Database settings
    database_uri: str = "postgresql://postgres:postgres@fully-vibe-code-postgres:5432/postgres"
    
    # Argo settings
    argo_url: str = "does not even matter locally"
    
    @property
    def database_url(self) -> str:
        """Get the database URL for Alembic and SQLAlchemy."""
        return self.database_uri


# Global settings instance
settings = Settings() 