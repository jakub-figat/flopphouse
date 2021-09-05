from src.apps.user.data_access import EmailDataAccess
from src.settings.database import AsyncSessionLocal


async def get_email_data_access() -> EmailDataAccess:
    async with AsyncSessionLocal() as async_session:
        async with async_session.begin():
            yield EmailDataAccess(async_session=async_session)
