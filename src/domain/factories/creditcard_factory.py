from creditcard import CreditCard as CreditCardNumber
from src.domain.value_objects.cvv import Cvv
from src.domain.entities.credit_card import CreditCard
from src.domain.value_objects.expiration_date import ExpirationDate
from src.domain.value_objects.holder import Holder
from src.domain.factories.protocol_factory import Factory
from src.domain.use_cases.dtos.creditcard_dtos import CreateNewCreditCardDTOIn, CreateNewCreditCardDTOOut
from src.adapters.outbound.orm.models import CreditCardModel


class CreditCardFactory(Factory):
    @classmethod
    def create(cls, dto: CreateNewCreditCardDTOIn) -> CreditCard:
        exp_date = ExpirationDate(exp_date=dto.exp_date)
        holder = Holder(name=dto.holder)
        credit_card_number = CreditCardNumber(dto.number)
        cvv = Cvv(value=dto.cvv)

        credit_card = CreditCard(exp_date=exp_date, holder=holder, credit_card_number=credit_card_number, cvv=cvv)

        return credit_card


class CreditCardModelToDTOFactory(Factory):
    def create(self, model: CreditCardModel) -> CreateNewCreditCardDTOOut:
        dto = CreateNewCreditCardDTOOut(
            identification=model.id,
            exp_date=model.expiration_date.strftime("%m/%Y"),  # Format the date as needed
            holder=model.holder,
            number=model.credit_card_number.decode(),  # Decode the bytea field to a string
            cvv=model.cvv,
            brand=model.brand
        )
        return dto