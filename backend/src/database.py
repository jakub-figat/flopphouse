from motor.motor_asyncio import AsyncIOMotorClient

from src.settings.config import MONGO_DATABASE, MONGO_URL


async def start_mongo_connection() -> None:
    from main import app

    app.mongo_client = AsyncIOMotorClient(MONGO_URL)
    app.mongo_db = app.mongo_client[MONGO_DATABASE]


async def close_mongo_connection() -> None:
    from main import app

    app.mongo_client.close()
