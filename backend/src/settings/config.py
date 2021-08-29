from decouple import config
from fastapi_mail import ConnectionConfig

MONGO_DATABASE = config("MONGODB_INITDB_DATABASE")
MONGO_USERNAME = config("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = config("MONGO_INITDB_ROOT_PASSWORD")

MONGO_HOST = config("MONGO_HOST")
MONGO_PORT = config("MONGO_PORT")

MONGO_URL = (
    f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@" f"{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE}?authSource=admin"
)


email_config = ConnectionConfig(
    MAIL_USERNAME=config("EMAIL_USERNAME"),
    MAIL_PASSWORD=config("EMAIL_PASSWORD"),
    MAIL_FROM=config("EMAIL_USERNAME"),
    MAIL_PORT=config("EMAIL_PORT"),
    MAIL_SERVER=config("EMAIL_HOST"),
    MAIL_TLS=config("EMAIL_USE_TLS", cast=bool),
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=config("TEMPLATE_DIR"),
)
