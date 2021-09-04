from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user import actions
from src.deps.database import get_async_session

router = APIRouter()


@router.post("/register", tags=["users"])
async def register_user():
    user = await actions.register_user()

    return {"user_uuid": user.id}
