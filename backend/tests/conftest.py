import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.settings import config
from src.settings.database import AsyncSessionLocal, Base, async_engine


@pytest.fixture(autouse=True)
def patch_postgres_url(monkeypatch):
    postgres_url = (
        f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
        f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/test"
    )

    monkeypatch.setattr(config, "POSTGRES_URL", postgres_url)


@pytest.fixture(autouse=True)
async def clear_database():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        yield
        await connection.run_sync(Base.metadata.create_all)


@pytest.fixture(autouse=True)
async def async_session() -> AsyncSession:
    async with AsyncSessionLocal() as async_session:
        async with async_session.begin():
            yield async_session
