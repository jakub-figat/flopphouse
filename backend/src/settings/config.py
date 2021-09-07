from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).parents[2]

DOMAIN = config("DOMAIN")


# database
POSTGRES_HOST = config("POSTGRES_HOST")
POSTGRES_DATABASE = config("POSTGRES_DATABASE")
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_PORT = config("POSTGRES_PORT", cast=int)

POSTGRES_URL = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@" f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
)

# email
MAIL_USERNAME = config("MAIL_USERNAME")
MAIL_PASSWORD = config("MAIL_PASSWORD")
MAIL_FROM = config("MAIL_FROM")
MAIL_PORT = config("MAIL_PORT", cast=int)
MAIL_SERVER = config("MAIL_SERVER")
MAIL_FROM_NAME = config("MAIL_FROM_NAME")
MAIL_TLS = True
MAIL_SSL = False
USE_CREDENTIALS = True
VALIDATE_CERTS = True
TEMPLATE_FOLDER = BASE_DIR / "templates"
