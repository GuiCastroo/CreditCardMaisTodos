from pydantic import BaseModel, Field


class Cvv(BaseModel):
    value: int = Field(ge=3, le=4)
