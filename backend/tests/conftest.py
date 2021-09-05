import asyncio

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from src.settings import config
from src.settings.database import Base


@pytest.fixture(scope="session", autouse=True)
def meta_migrations():
    postgres_url = (
        f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
        f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/test"
    )
    sync_engine = create_engine(postgres_url, echo=True)

    Base.metadata.drop_all(bind=sync_engine)
    Base.metadata.create_all(bind=sync_engine)

    yield sync_engine
    Base.metadata.drop_all(bind=sync_engine)


@pytest.fixture(scope="session")
async def async_engine() -> AsyncEngine:
    postgres_url = (
        f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
        f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/test"
    )
    async_engine = create_async_engine(postgres_url, echo=True)

    yield async_engine


@pytest.fixture(scope="function")
async def async_session(async_engine: AsyncEngine) -> AsyncSession:
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
