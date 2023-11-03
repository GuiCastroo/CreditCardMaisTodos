from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository
from src.domain.factories.creditcard_factory import CreditCardModelToDTOFactory


class GetOneCreditCardUseCase:
    def __init__(self, rep: ICreditCardRepository):
        self._rep = rep

    async def get(self, identification: str):
        data = await self._rep.get_by_filter(identification)
        if data:
            result = CreditCardModelToDTOFactory().create(data)
        else:
            result = None
        return result
