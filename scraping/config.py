from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    # MongoDB configs
    MONGO_DATABASE_HOST: str = "mongodb://127.0.0.1:27017/scrabble"
    MONGO_DATABASE_NAME: str = "scrabble"

    LINKEDIN_USERNAME: str | None = None
    LINKEDIN_PASSWORD: str | None = None


settings = Settings()