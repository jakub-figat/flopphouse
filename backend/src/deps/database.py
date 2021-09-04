from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from src.settings.database import AsyncSessionLocal


@asynccontextmanager
async def get_async_session() -> AsyncSession:
    async_session = AsyncSessionLocal()
    try:
        yield async_session
    finally:
        await async_session.close()
