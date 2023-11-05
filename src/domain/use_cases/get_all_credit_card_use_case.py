from src.domain.factories.creditcard_factory import CreditCardModelToDTOFactory
from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository


class GetAllCreditCardUseCase:
    def __init__(self, rep: ICreditCardRepository):
        self._rep = rep

    async def get_all(self):
        data = await self._rep.get_all()
        print(data)
        data.items = [CreditCardModelToDTOFactory().create(card) for card in data.items]
        return data
