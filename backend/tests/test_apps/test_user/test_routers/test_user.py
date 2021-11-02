import pytest
from fastapi import status
from httpx import AsyncClient
from pytest_mock import MockerFixture
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from src.apps.user.models import User
from src.dependencies import get_async_session


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
async def override_get_async_session(async_session: AsyncSession):
    app.dependency_overrides[get_async_session] = lambda: async_session
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
