import unittest

from unittest.mock import AsyncMock
from src.domain.use_cases.create_new_creditcard_use_case import CreateNewCreditCardUseCase, CreateNewCreditCardDTOOut
from src.domain.use_cases.dtos.creditcard_dtos import CreateNewCreditCardDTOIn
from src.domain.factories.creditcard_factory import CreditCardFactory
from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository


class TestCreateNewCreditCardUseCase(unittest.TestCase):
    def setUp(self):
        # Create a mock for the repository
        self.mock_repository = AsyncMock(spec=ICreditCardRepository)

        # Create a use case instance with the mock repository
        self.use_case = CreateNewCreditCardUseCase(rep=self.mock_repository)
        self.input_data = CreateNewCreditCardDTOIn(
            exp_date="02/2026",
            holder="Fulano",
            number="4539578763621486",
            cvv="123"
        )
        self.output_date = CreateNewCreditCardDTOOut(
            identification="12313",
            exp_date='2026-02-28',
            holder='FULANO',
            number='gAAA',
            cvv=123,
            brand="visa"
        )
        self.credit_card = CreditCardFactory().create(self.input_data)
        self.mock_repository.create.return_value = self.credit_card

    async def test_create_new_credit_card(self):
        result = await self.use_case.create(self.input_data)
        self.output_date.identification = result.identification
        self.output_date.number = result.number
        self.assertEqual(result, self.output_date)


if __name__ == '__main__':
    unittest.main()
