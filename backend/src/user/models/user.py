import datetime as dt
from uuid import uuid4

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, Field, validator


class UserModel(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id", const=True)
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    username: str = Field(..., max_length=30)
    date_of_birth: dt.date

    class Config:
        allow_population_by_field_name = True

    @validator("date_of_birth")
    def validate_date_of_birth(cls, date_of_birth: dt.date) -> None:
        if date_of_birth >= dt.date.today():
            raise ValueError("Date of birth must be in the past")

    @property
    def age(self):
        return relativedelta(dt.date.today() - self.date_of_birth).years
