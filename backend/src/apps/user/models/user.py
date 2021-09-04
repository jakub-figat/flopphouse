from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    __mapper_args__ = {"eager_defaults": True}
