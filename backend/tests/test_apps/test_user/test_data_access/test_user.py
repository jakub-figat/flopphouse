import datetime as dt

import pytest
from pytest_mock import MockerFixture
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.data_access import EmailDataAccess, UserDataAccess
from src.apps.user.models import User
from src.apps.user.schemas import UserRegisterSchema, UserSchema


@pytest.fixture(scope="module")
def user_register_schema() -> UserRegisterSchema:
    return UserRegisterSchema(
        first_name="name",
        last_name="name",
        username="username",
        email="email@email.email",
        password="tost123",
        password_2="tost123",
        date_of_birth=dt.date(2020, 1, 1),
    )


@pytest.fixture(scope="module")
def user_register_schema_2() -> UserRegisterSchema:
    return UserRegisterSchema(
        first_name="name",
        last_name="name",
        username="usernamea",
        email="email@email.emaila",
        password="tost123",
        password_2="tost123",
        date_of_birth=dt.date(2020, 1, 1),
    )


@pytest.mark.asyncio
async def test_user_data_access_can_register_user(
    user_register_schema: UserRegisterSchema,
    user_register_schema_2,
    async_session: AsyncSession,
):
    user_data_access = UserDataAccess(async_session=async_session)

    user_schema = await user_data_access.create_user(user_register_schema=user_register_schema)
    user_from_db = await async_session.scalar(select(User).filter(User.username == user_schema.username))
    user_schema_from_db = UserSchema.from_orm(user_from_db)

    assert user_schema == user_schema_from_db
