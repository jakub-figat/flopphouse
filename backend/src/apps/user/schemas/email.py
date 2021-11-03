import datetime as dt
from uuid import UUID

from pydantic import BaseModel


class EmailConfirmationSchema(BaseModel):
    id: UUID
    token: UUID
    created_at: dt.datetime

    @property
    async def is_valid(self) -> bool:
        return dt.datetime.utcnow() >= self.created_at


class EmailConfirmationBodySchema(BaseModel):
    first_name: str
    domain: str
    confirmation_url: str
