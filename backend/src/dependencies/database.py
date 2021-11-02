from typing import Iterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.settings.database import AsyncSessionLocal


async def get_async_session() -> Iterator[AsyncSession]:
    async with AsyncSessionLocal() as async_session:
        async with async_session.begin():
            yield async_session
