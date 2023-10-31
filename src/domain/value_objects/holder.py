from pydantic import BaseModel, Field, field_validator


class Holder(BaseModel):
    name: str = Field(min_length=3)

    @field_validator("name")
    def validate_name(cls, value):
        return value.upper()

