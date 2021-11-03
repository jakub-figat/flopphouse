from abc import ABCMeta, abstractmethod

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from jinja2 import Template
from pydantic import BaseModel

from src.settings.config import EmailSettings, settings
from src.utils.schemas import EmailSchema


class BaseEmailSender(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.config = ConnectionConfig(**EmailSettings().dict())

    @abstractmethod
    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        pass


class ConsoleEmailSender(BaseEmailSender):
    def _get_template(self, template_name: str) -> Template:
        with open(settings.TEMPLATE_FOLDER / template_name, "r") as template_file:
            template = Template(template_file.read())

        return template

    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        template = self._get_template(email_schema.template_name)
        print(template.render(**body_schema.dict()))


class EmailSender(BaseEmailSender):
    async def send_email(self, email_schema: EmailSchema, body_schema: BaseModel) -> None:
        message = MessageSchema(
            subject=email_schema.subject,
            recipients=email_schema.recipients,
            template_body=body_schema.dict(),
        )

        fast_mail = FastMail(self.config)
        await fast_mail.send_message(message, template_name=email_schema.template_name)
