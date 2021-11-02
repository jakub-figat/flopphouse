from sqlalchemy import Boolean, Column, Date, String

from src.settings.database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    username = Column(String(length=30), unique=True, nullable=False)
    password = Column(String, nullable=False)

    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    is_active = Column(Boolean, server_default="false", nullable=False)
