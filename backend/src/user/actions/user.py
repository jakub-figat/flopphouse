from typing import Any
from uuid import uuid4

from src.database import mongo_db
from src.user.models import UserModel


async def register_user(user_data: dict[str, Any]) -> UserModel:
    async with mongo_db() as db:
        user_data["_id"] = uuid4()
        inserted_user = await db.users.insert_one(user_data)
        registered_user_data = await db.users.find_one({"_id": inserted_user.inserted_id})

    return UserModel(**registered_user_data)
