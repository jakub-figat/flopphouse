from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel

from src.settings import config
from src.utils.schemas import EmailSchema


class EmailSender:
    def __init__(self) -> None:
        self.config = ConnectionConfig(
            MAIL_USERNAME=config.MAIL_USERNAME,
            MAIL_PASSWORD=config.MAIL_PASSWORD,
            MAIL_FROM=config.MAIL_FROM,
            MAIL_PORT=config.MAIL_PORT,
            MAIL_SERVER=config.MAIL_SERVER,
            MAIL_FROM_NAME=config.MAIL_FROM_NAME,
            MAIL_TLS=config.MAIL_TLS,
            MAIL_SSL=config.MAIL_SSL,
            USE_CREDENTIALS=config.USE_CREDENTIALS,
            VALIDATE_CERTS=config.VALIDATE_CERTS,
        )

    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        message = MessageSchema(
            subject=email_schema.subject,
            recipients=email_schema.recipients,
            template_body=body_schema.dict(),
        )

        fast_mail = FastMail(self.config)
        await fast_mail.send_message(message, template_name=email_schema.template_name)
