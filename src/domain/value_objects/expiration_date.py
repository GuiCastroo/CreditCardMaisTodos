from datetime import date, timedelta
from pydantic import BaseModel, Field, field_validator


class ExpirationDate(BaseModel):
    exp_date: str = Field(..., description="Expiration date in the format 'yyyy-MM'")

    @field_validator("exp_date")
    def validate_exp_date(cls, value):
        try:
            year, month = value.split("-")
            year = int(year)
            month = int(month)
            last_day_of_month = (date(year, month % 12 + 1, 1) - timedelta(days=1)).day
            if month < 1 or month > 12:
                raise ValueError("Invalid month")
            if year < date.today().year or (year == date.today().year and month < date.today().month):
                raise ValueError("Expiration date is in the past")
            return f"{year:04d}-{month:02d}-{last_day_of_month:02d}"
        except (ValueError, TypeError):
            raise ValueError("Invalid expiration date format")
