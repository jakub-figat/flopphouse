from typing import Any
from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import DuplicateKeyError

from src.apps.user.models import UserModel
from src.apps.user.utils import password_context
from src.utils.errors import UniqueConstraintException


async def register_user(user_data: dict[str, Any], mongo_db: AsyncIOMotorDatabase) -> UserModel:
    user_data["_id"] = uuid4()
    raw_password = user_data.pop("password_2")
    user_data["password"] = password_context.hash(raw_password)

    try:
        inserted_user = await mongo_db.users.insert_one(user_data)
    except DuplicateKeyError as error:
        raise UniqueConstraintException(error=error)

    registered_user_data = await mongo_db.users.find_one({"_id": inserted_user.inserted_id})

    return UserModel(**registered_user_data)
