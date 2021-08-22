from motor.motor_asyncio import AsyncIOMotorClient
from src.settings.config import MONGO_DATABASE, MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client[MONGO_DATABASE]
