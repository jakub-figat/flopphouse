import datetime as dt

import pytest
from fastapi import status
from httpx import AsyncClient
from pytest_mock import MockerFixture
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from src.apps.user.data_access import EmailDataAccess, UserDataAccess
from src.apps.user.dependencies import get_email_data_access, get_user_data_access
from src.apps.user.models import User


@pytest.fixture(scope="module")
def user_register_data() -> dict[str, str]:
    return {
        "first_name": "name",
        "last_name": "name",
        "username": "usernameaasdasdasd",
        "email": "email@email.example",
        "password": "tost123",
        "password_2": "tost123",
        "date_of_birth": "2020-01-01",
    }


@pytest.fixture(autouse=True)
async def override_get_user_data_access(async_session: AsyncSession):
    app.dependency_overrides[get_user_data_access] = lambda: UserDataAccess(async_session=async_session)
    yield


@pytest.fixture(autouse=True)
async def override_get_email_data_access(async_session: AsyncSession):
    app.dependency_overrides[get_email_data_access] = lambda: EmailDataAccess(async_session=async_session)
    yield


@pytest.mark.asyncio
async def test_user_can_register(
    user_register_data: dict[str, str],
    async_client: AsyncClient,
    async_session: AsyncSession,
    mocker: MockerFixture,
):
    user_register_url = "users/register"
    mock_send_message = mocker.patch("fastapi_mail.FastMail.send_message")

    response = await async_client.post(user_register_url, json=user_register_data)
    assert response.status_code == status.HTTP_201_CREATED

    user = await async_session.scalar(select(User))

    assert user.username == user_register_data["username"]

    # TODO: fix mock called two times
