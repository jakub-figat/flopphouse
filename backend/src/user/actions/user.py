from typing import Any
from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.user.models import UserModel
from src.user.utils import password_context


async def register_user(user_data: dict[str, Any], mongo_db: AsyncIOMotorDatabase) -> UserModel:
    user_data["_id"] = uuid4()
    raw_password = user_data.pop("password_2")
    user_data["password"] = password_context.hash(raw_password)
    inserted_user = await mongo_db.users.insert_one(user_data)

    registered_user_data = await mongo_db.users.find_one({"_id": inserted_user.inserted_id})

    return UserModel(**registered_user_data)
