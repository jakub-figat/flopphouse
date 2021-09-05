from fastapi import Depends
from fastapi.routing import APIRouter

from src.apps.user.data_access import UserDataAccess
from src.apps.user.dependencies import get_user_data_access
from src.apps.user.schemas import UserRegisterSchema, UserSchema
from src.apps.user.utils.email import send_confirmation_email
from src.utils.email import EmailSender

router = APIRouter()


@router.post("/register", tags=["users"])
async def register_user(
    user_register_schema: UserRegisterSchema,
    user_data_access: UserDataAccess = Depends(get_user_data_access),
    email_sender: EmailSender = Depends(),
) -> UserSchema:
    user_schema = await user_data_access.create_user(user_register_schema=user_register_schema)
    await send_confirmation_email(user_schema=user_schema, email_sender=email_sender)

    return {"detail": "Confirmation email sent"}
