from typing import Any, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.data_access import EmailDataAccess
from src.apps.user.models import User
from src.apps.user.schemas import UserPasswordSchema, UserRegisterSchema, UserSchema
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

        user_password_schema = UserPasswordSchema(**user_data)
        user = User(**user_password_schema.dict())

        self._async_session.add(user)
        await self._async_session.flush()

        user_schema = UserSchema.from_orm(user)
        await self.send_confirmation_email(user_schema=user_schema, email_data_access_class=EmailDataAccess)

        return user_schema

    async def send_confirmation_email(
        self, *, user_schema: UserSchema, email_data_access_class: Type[EmailDataAccess]
    ) -> None:
        email_data_access = email_data_access_class(async_session=self._async_session)
        await email_data_access.create_confirmation_email(user_schema=user_schema)
