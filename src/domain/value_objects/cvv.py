from pydantic import BaseModel, Field


class Cvv(BaseModel):
    value: int = Field(ge=100, le=9999, description="CVV must be a 3 or 4-digit number (between 100 and 9999).")
