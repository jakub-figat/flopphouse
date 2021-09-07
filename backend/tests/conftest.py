import asyncio
from typing import AsyncIterator

import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine, event
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from main import app
from src.settings import config
from src.settings.database import Base


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop


def pytest_sessionfinish():
    asyncio.get_event_loop().close()


@pytest.fixture(scope="session", autouse=True)
def meta_migrations():
    postgres_url = (
        f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
        f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/test"
    )
    sync_engine = create_engine(postgres_url, echo=False)

    Base.metadata.drop_all(bind=sync_engine)
    Base.metadata.create_all(bind=sync_engine)

    yield
    Base.metadata.drop_all(bind=sync_engine)


@pytest.fixture(scope="session")
async def async_engine() -> AsyncIterator[AsyncEngine]:
    postgres_url = (
        f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
        f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/test"
    )
    async_engine = create_async_engine(postgres_url, echo=False)

    yield async_engine


@pytest.fixture(scope="function")
async def async_session(async_engine: AsyncEngine) -> AsyncIterator[AsyncSession]:
    connection = await async_engine.connect()
    transaction = await connection.begin()
    async_session = AsyncSession(bind=connection)

    await connection.begin_nested()

    @event.listens_for(async_session.sync_session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.begin_nested()

    yield async_session

    await async_session.close()
    await transaction.rollback()
    await connection.close()


@pytest.fixture(scope="function")
async def async_client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://localhost:8000/api/v1/") as async_client:
        yield async_client
