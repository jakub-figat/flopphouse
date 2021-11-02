from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.apps.user.data_access import EmailDataAccess, UserDataAccess
from src.apps.user.schemas import UserRegisterSchema, UserSchema
from src.apps.user.utils.email import send_confirmation_email
from src.dependencies import get_async_session
from src.utils.email import EmailSender

router = APIRouter()


@router.post("/register", tags=["users"], status_code=status.HTTP_201_CREATED)
async def register_user(
    user_register_schema: UserRegisterSchema,
    async_session: AsyncSession = Depends(get_async_session),
) -> UserSchema:
    user_schema = await UserDataAccess(async_session=async_session).create_user(
        user_register_schema=user_register_schema
    )
    await EmailDataAccess(async_session=async_session).create_confirmation_email(user_schema=user_schema)

    return {"detail": "Confirmation email sent"}
