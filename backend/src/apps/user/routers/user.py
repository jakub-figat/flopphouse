from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.routing import APIRouter

from src.apps.user import actions
from src.apps.user.models import UserModel, UserRegisterModel

router = APIRouter()


@router.post("/register", tags=["users"], response_model=UserModel)
async def register_user(request: Request, user: UserRegisterModel):
    user_data = jsonable_encoder(user)
    user = await actions.register_user(user_data=user_data, mongo_db=request.app.mongo_db)

    return user
