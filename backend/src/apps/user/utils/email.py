from src.apps.user.schemas import EmailConfirmationBodySchema, UserSchema
from src.settings import config
from src.utils.email import EmailSender
from src.utils.schemas import EmailSchema


async def send_confirmation_email(*, user_schema: UserSchema, email_sender: EmailSender) -> None:
    email_schema = EmailSchema(
        subject="Flopphouse email confirmation",
        recipients=(user_schema.email,),
        template_name="email_confirmation.html",
    )

    body_schema = EmailConfirmationBodySchema(
        first_name=user_schema.first_name, domain=config.DOMAIN, confirmation_url="dupa"
    )

    await email_sender.send_email(email_schema=email_schema, body_schema=body_schema)
