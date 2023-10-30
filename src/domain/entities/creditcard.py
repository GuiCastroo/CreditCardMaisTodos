from src.domain.value_objects.cvv import Cvv
from creditcard import CreditCard as CreditCardNumber
from cryptography.fernet import Fernet


class CreditCard:
    def __init__(self, exp_date, holder, credit_card_number: CreditCardNumber, cvv: Cvv):
        self._exp_date = exp_date
        self._holder = holder
        self.__credit_card_number = credit_card_number
        self._cvv = cvv

    def get_exp_date(self):
        return self._exp_date

    def get_cvv(self):
        return self._cvv.value

    def verify_credit_card_number(self):
        self.__credit_card_number.number.is_valid()

    def get_credit_card_number(self):
        encryption_key = Fernet.generate_key()
        value = self.__credit_card_number.number
        fernet = Fernet(encryption_key)
        result = fernet.encrypt(value.encode())
        return result



