from uuid import uuid4

from sqlalchemy import Boolean, Column, Date, String
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    username = Column(String(length=30), unique=True, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)

    __mapper_args__ = {"eager_defaults": True}
