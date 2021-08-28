from fastapi import Body
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter

from src.user import actions
from src.user.models import UserModel, UserRegisterModel

router = APIRouter()


@router.post("/register", tags=["users"], response_model=UserModel)
async def register_user(user: UserRegisterModel = Body(...)):
    user_data = jsonable_encoder(user)
    user = await actions.register_user(user_data=user_data)

    return user
