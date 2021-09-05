from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import config

async_engine = create_async_engine(url=config.POSTGRES_URL, echo=True)


AsyncSessionLocal = sessionmaker(
    bind=async_engine, expire_on_commit=False, autoflush=False, autocommit=False, class_=AsyncSession
)

Base = declarative_base()
