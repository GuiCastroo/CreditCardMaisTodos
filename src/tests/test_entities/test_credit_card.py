import unittest
from unittest.mock import Mock
from src.domain.entities.credit_card import CreditCard


class TestCreditCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exp_date = Mock()
        cls.holder = Mock()
        cls.credit_card_number = Mock()
        cls.cvv = Mock()
        cls.credit_card = CreditCard(cls.exp_date, cls.holder, cls.credit_card_number, cls.cvv)

    def test_given_valid_credit_card_when_getting_exp_date_then_return_exp_date(self):
        result = self.credit_card.get_exp_date()
        self.assertEqual(result, self.exp_date.exp_date)

    def test_given_valid_credit_card_when_getting_cvv_then_return_cvv(self):
        result = self.credit_card.get_cvv()
        self.assertEqual(result, self.cvv.value)

    def test_given_valid_credit_card_when_getting_holder_then_return_holder(self):
        result = self.credit_card.get_holder()
        self.assertEqual(result, self.holder.name)

    def test_given_valid_credit_card_when_getting_credit_card_number_then_return_encrypted_number(self):
        self.credit_card_number.number = "1234567890123456"

        result = self.credit_card.get_credit_card_number()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
