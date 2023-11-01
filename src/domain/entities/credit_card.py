from src.domain.value_objects.cvv import Cvv
from creditcard import CreditCard as CreditCardNumber
from src.domain.value_objects.expiration_date import ExpirationDate
from cryptography.fernet import Fernet
from src.domain.value_objects.holder import Holder
from typing import Optional
from uuid import uuid4


class CreditCard:
    def __init__(
            self,
            exp_date: ExpirationDate,
            holder: Holder,
            credit_card_number: CreditCardNumber,
            cvv: Cvv,
            identification: Optional[str] = None
    ):
        self._exp_date = exp_date
        self._holder = holder
        self.__credit_card_number = credit_card_number
        self._cvv = cvv
        self._identification = identification

    def get_identification(self):
        if not self._identification:
            self._identification = str(uuid4())
        return self._identification

    def get_exp_date(self):
        return self._exp_date.exp_date

    def get_cvv(self):
        return self._cvv.value

    def get_holder(self):
        return self._holder.name

    def get_brand(self):
        return self.__credit_card_number.get_brand()

    def verify_credit_card_number(self):
        return self.__credit_card_number.number.is_valid()

    def get_credit_card_number(self):
        encryption_key = Fernet.generate_key()
        value = self.__credit_card_number.number
        fernet = Fernet(encryption_key)
        result = fernet.encrypt(value.encode())
        return result



