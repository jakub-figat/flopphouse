from typing import Any, Type

from src.apps.user.models import User
from src.apps.user.schemas import UserPasswordSchema, UserRegisterSchema, UserSchema
from src.apps.user.utils import password_context
from src.utils.data_access.base import BaseDataAccess, Model, SchemaIn, SchemaOut


class UserDataAccess(BaseDataAccess[UserSchema, UserSchema, User]):
    @property
    def _schema_in(self) -> Type[SchemaIn]:
        return UserSchema

    @property
    def _schema_out(self) -> Type[SchemaOut]:
        return UserSchema

    @property
    def _model(self) -> Type[Model]:
        return User

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

        return self._schema_out.from_orm(user)
