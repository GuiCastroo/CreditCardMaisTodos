from src.domain.use_cases.dtos.creditcard_dtos import CreateNewCreditCardDTOIn, CreateNewCreditCardDTOOut
from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository
from src.domain.factories.creditcard_factory import CreditCardFactory


class CreateNewCreditCardUseCase:
    def __init__(self, rep: ICreditCardRepository):
        self._rep = rep

    async def create(self, data: CreateNewCreditCardDTOIn) -> CreateNewCreditCardDTOOut:
        new_credit_card = CreditCardFactory().create(data)
        new_credit_card.verify_credit_card_number()
        result = CreateNewCreditCardDTOOut(
            identification=new_credit_card.get_identification(),
            exp_date=new_credit_card.get_exp_date(),
            holder=new_credit_card.get_holder(),
            number=new_credit_card.get_credit_card_number(),
            cvv=new_credit_card.get_cvv(),
            brand=new_credit_card.get_brand()
        )
        await self._rep.create(new_credit_card)
        return result


