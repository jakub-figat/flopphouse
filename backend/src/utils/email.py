from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel

from src.settings.config import EmailSettings
from src.utils.schemas import EmailSchema


class EmailSender:
    def __init__(self) -> None:
        self.config = ConnectionConfig(**EmailSettings().dict())

    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        message = MessageSchema(
            subject=email_schema.subject,
            recipients=email_schema.recipients,
            template_body=body_schema.dict(),
        )

        fast_mail = FastMail(self.config)
        await fast_mail.send_message(message, template_name=email_schema.template_name)
