from fastapi import Depends
from fastapi.routing import APIRouter

from src.apps.user.data_access import UserDataAccess
from src.apps.user.dependencies import get_user_data_access
from src.apps.user.schemas import UserRegisterSchema, UserSchema

router = APIRouter()


@router.post("/register", tags=["users"], response_model=UserSchema)
async def register_user(
    user_register_schema: UserRegisterSchema,
    user_data_access: UserDataAccess = Depends(get_user_data_access),
) -> UserSchema:
    user = await user_data_access.create_user(user_register_schema=user_register_schema)

    return user
