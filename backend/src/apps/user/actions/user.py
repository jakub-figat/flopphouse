from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.models import User
from src.settings.database import AsyncSessionLocal


async def register_user(*, async_session: AsyncSession) -> User:
    user = User()
    async_session.add(user)
    await async_session.commit()

    return user
