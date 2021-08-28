from contextlib import asynccontextmanager
from typing import AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.settings.config import MONGO_DATABASE, MONGO_URL


@asynccontextmanager
async def mongo_db() -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    mongo_client = AsyncIOMotorClient(MONGO_URL)
    try:
        yield mongo_client[MONGO_DATABASE]
    finally:
        mongo_client.close()
