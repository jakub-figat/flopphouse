from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel

from src.settings.config import settings
from src.utils.schemas import EmailSchema


class EmailSender:
    def __init__(self) -> None:
        self.config = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_SERVER,
            MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
            MAIL_TLS=settings.MAIL_TLS,
            MAIL_SSL=settings.MAIL_SSL,
            USE_CREDENTIALS=settings.USE_CREDENTIALS,
            VALIDATE_CERTS=settings.VALIDATE_CERTS,
        )

    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        message = MessageSchema(
            subject=email_schema.subject,
            recipients=email_schema.recipients,
            template_body=body_schema.dict(),
        )

        fast_mail = FastMail(self.config)
        await fast_mail.send_message(message, template_name=email_schema.template_name)
