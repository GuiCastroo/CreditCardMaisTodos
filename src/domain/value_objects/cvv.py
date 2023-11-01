from pydantic import BaseModel, Field


class Cvv(BaseModel):
    value: int = Field(ge=100, le=9999)
