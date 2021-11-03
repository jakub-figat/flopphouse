from pathlib import Path

from pydantic import BaseSettings


class GeneralSettings(BaseSettings):
    ENV: str = "development"
    BASE_DIR: Path = Path(__file__).parents[2]
    DOMAIN: str
    TEMPLATE_FOLDER: Path = BASE_DIR / "templates"


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int

    @property
    def postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"
        )


class EmailSettings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    @property
    def email_sender_class(self):
        from src.utils.email import ConsoleEmailSender, EmailSender

        return ConsoleEmailSender if self.ENV == "development" else EmailSender


class Settings(GeneralSettings, DatabaseSettings, EmailSettings):
    pass


settings = Settings()
