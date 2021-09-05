from typing import Any
from uuid import uuid4

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.models import User
from src.apps.user.schemas import UserRegisterSchema, UserSchema
from src.apps.user.utils import password_context


class UserDataAccess:
    def __init__(self, *, async_session: AsyncSession) -> None:
        self._async_session = async_session

    async def _hash_password(self, *, user_data: dict[str, Any]) -> None:
        password_2 = user_data.pop("password_2")
        user_data["password"] = password_context.hash(password_2)

    async def create_user(self, *, user_register_schema: UserRegisterSchema) -> UserSchema:
        user_data = user_register_schema.dict()
        await self._hash_password(user_data=user_data)
        user = User(**user_data)

        self._async_session.add(user)
        await self._async_session.flush()

        return UserSchema.from_orm(user)
