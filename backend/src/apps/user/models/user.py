from sqlalchemy import Boolean, Column, Date, String, text
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    email = Column(String, unique=True, nullable=False)
    username = Column(String(length=30), unique=True, nullable=False)
    password = Column(String, nullable=False)

    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    is_active = Column(Boolean, server_default="false", nullable=False)

    __mapper_args__ = {"eager_defaults": True}
