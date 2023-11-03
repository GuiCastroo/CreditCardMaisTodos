import unittest
from src.domain.factories.creditcard_factory import CreditCardFactory
from src.domain.use_cases.dtos.creditcard_dtos import CreateNewCreditCardDTOIn


class TestCreditCardFactory(unittest.TestCase):
    def setUp(self):
        # Given
        self.dto = CreateNewCreditCardDTOIn(
            exp_date="02/2030",
            holder="Fulano",
            number="0000000000000001",
            cvv=123
        )
        self.credit_card = CreditCardFactory.create(self.dto)

    def test_given_valid_data_when_create_credit_card_then_attribute_exp_date_match(self):
        self.assertEqual(self.credit_card.get_exp_date(), "2030-02-28")

    def test_given_valid_data_when_create_credit_card_then_attribute_holder_match(self):
        self.assertEqual(self.credit_card.get_holder(), "FULANO")

    def test_given_valid_data_when_create_credit_card_then_attribute_credit_card_number_match(self):
        self.assertIsInstance(self.credit_card.get_credit_card_number(), bytes)

    def test_given_valid_data_when_create_credit_card_then_attribute_cvv_match(self):
        self.assertEqual(self.credit_card.get_cvv(), 123)


if __name__ == '__main__':
    unittest.main()
