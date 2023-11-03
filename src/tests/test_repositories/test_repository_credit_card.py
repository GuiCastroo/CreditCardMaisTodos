import unittest
from unittest.mock import Mock
from src.domain.entities.credit_card import CreditCard
from src.adapters.outbound.orm.models import CreditCardModel
from src.adapters.outbound.orm.database import SESSION
from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository
from src.adapters.outbound.repositories.credit_card_repository import CreditCardRepository


class TestCreditCardRepository(unittest.TestCase):

    def setUp(self):
        self.mock_session = Mock()
        self.mock_credit_card = CreditCard(
            identification="123",
            exp_date="12/23",
            holder="John Doe",
            credit_card_number="1234567890123456",
            cvv="123"
        )

    def test_get_all(self):
        self.mock_session.execute.return_value = Mock(scalars=lambda: [CreditCardModel()])
        repo = CreditCardRepository(self.mock_session)
        result = repo.get_all()
        self.assertIsNotNone(result)

    def test_get_by_filter(self):
        self.mock_session.execute.return_value = Mock(one=lambda: CreditCardModel())
        repo = CreditCardRepository(self.mock_session)
        result = repo.get_by_filter("123")
        self.assertIsNotNone(result)

    def test_create(self):
        repo = CreditCardRepository(self.mock_session)
        repo.create(self.mock_credit_card)
        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
