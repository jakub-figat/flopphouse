from pydantic import BaseModel


class EmailConfirmationSchema(BaseModel):
    first_name: str
    domain: str
    confirmation_url: str
