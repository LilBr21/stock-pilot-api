# TODO: Implement Settings class using pydantic-settings
#
# Required settings:
# - database_url: str (PostgreSQL connection string)
# - secret_key: str (for JWT signing)
# - algorithm: str = "HS256"
# - access_token_expire_minutes: int = 30
# - refresh_token_expire_days: int = 7
# - finnhub_api_key: str
# - finnhub_base_url: str = "https://finnhub.io/api/v1"
# - cors_origins: list[str]
#
# Example:
# from pydantic_settings import BaseSettings, SettingsConfigDict
#
# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(env_file=".env")
#     database_url: str = "..."
#     ...
#
# settings = Settings()
