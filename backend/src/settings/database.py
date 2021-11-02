from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr, sessionmaker

from src.settings.config import settings

async_engine = create_async_engine(url=settings.postgres_url, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, expire_on_commit=False, autoflush=False, autocommit=False, class_=AsyncSession
)


@as_declarative()
class Base:
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))

    __mapper_args__ = {"eager_defaults": True}

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__tablename__.lower()
