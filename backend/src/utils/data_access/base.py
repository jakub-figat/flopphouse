from abc import ABCMeta, abstractmethod
from typing import Generic, Type, TypeVar

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

SchemaIn = TypeVar("SchemaIn", bound=BaseModel)
SchemaOut = TypeVar("SchemaOut", bound=BaseModel)
Model = TypeVar("Model")


class BaseDataAccess(Generic[SchemaIn, SchemaOut, Model], metaclass=ABCMeta):
    def __init__(self, *, async_session: AsyncSession) -> None:
        self._async_session = async_session

    @property
    @abstractmethod
    def _schema_in(self) -> Type[SchemaIn]:
        pass

    @property
    @abstractmethod
    def _schema_out(self) -> Type[SchemaOut]:
        pass

    @property
    @abstractmethod
    def _model(self) -> Type[Model]:
        pass

    async def get(self, **kwargs) -> SchemaOut:
        conditions = [getattr(self._model, key) == value for key, value in kwargs.items()]
        statement = select(self._model).filter(and_(True, *conditions))

        instance = await self._async_session.scalar(statement)
        if instance is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self._model.__name__} not found")

        return self._schema_out.from_orm(instance)

    async def create(self, schema_in: SchemaIn) -> SchemaOut:
        instance = self._model(**schema_in.dict())
        self._async_session.add(instance)
        await self._async_session.flush()

        return self._schema_out.from_orm(instance)

    async def update(self, schema_in: SchemaIn) -> SchemaOut:
        instance = await self.get(id=schema_in.id)
        for key, value in schema_in.dict().items():
            setattr(instance, key, value)

        await self._async_session.flush()
        return self._schema_out.from_orm(instance)
