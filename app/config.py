from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SPX AI Backend V1"
    environment: str = "development"
    demo_mode: bool = True

    openai_api_key: str | None = None
    openai_model: str = "gpt-5.5"

    # Comma-separated list of allowed origins.
    # Use "*" only during initial development.
    cors_origins: str = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        if self.cors_origins.strip() == "*":
            return ["*"]

        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


settings = Settings()
