from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.models import EmailConfirmation
from src.apps.user.schemas import EmailConfirmationSchema, UserSchema
from src.apps.user.utils.email import send_confirmation_email
from src.utils.email import EmailSender


class EmailDataAccess:
    def __init__(self, *, async_session: AsyncSession) -> None:
        self._async_session = async_session

    async def create_confirmation_email(self, *, user_schema: UserSchema) -> EmailConfirmationSchema:
        email_confirmation = EmailConfirmation(
            user_id=user_schema.id,
            token=uuid4(),
        )
        self._async_session.add(email_confirmation)
        await self._async_session.flush()

        await send_confirmation_email(user_schema=user_schema, email_sender=EmailSender())
