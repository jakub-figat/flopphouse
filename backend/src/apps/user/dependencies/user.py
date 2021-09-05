from src.apps.user.data_access import UserDataAccess
from src.settings.database import AsyncSessionLocal


async def get_user_data_access() -> UserDataAccess:
    async with AsyncSessionLocal() as async_session:
        async with async_session.begin():
            yield UserDataAccess(async_session=async_session)
