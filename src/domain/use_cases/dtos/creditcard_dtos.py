from pydantic import BaseModel
from datetime import datetime


class CreateNewCreditCardDTOIn(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int


class CreateNewCreditCardDTOOut(BaseModel):
    identification: str
    exp_date: str
    holder: str
    number: str
    cvv: int
    brand: str

