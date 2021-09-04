from src.apps.user.models import User
from src.settings.database import AsyncSessionLocal


async def register_user() -> User:
    user = User()
    async with AsyncSessionLocal() as async_session:
        async_session.add(user)
        await async_session.commit()

    return user
