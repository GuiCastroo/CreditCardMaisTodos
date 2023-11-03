from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository
from src.domain.entities.credit_card import CreditCard
from sqlalchemy.future import select
from src.adapters.outbound.orm.models import CreditCardModel
from src.adapters.outbound.orm.database import SESSION
from fastapi_pagination.ext.sqlalchemy import paginate


class CreditCardRepository(ICreditCardRepository):
    def __init__(self, db):
        self._db = db

    async def get_all(self):
        async with SESSION() as session:
            stmt = await session.execute(
                select(CreditCardModel).order_by(CreditCardModel.expiration_date)
            )
            result = await paginate(session, stmt)
            return result

    async def get_by_filter(self, value: str):
        async with SESSION() as session:
            stmt = await session.execute(
                select(CreditCardModel).where(CreditCardModel.id == value)
            )
            result = stmt.one()
            return result

    async def create(self, data: CreditCard):
        async with SESSION() as session:
            session.add(
                CreditCardModel(
                    id=data.get_identification(),
                    expiration_date=data.get_exp_date(),
                    holder=data.get_holder(),
                    credit_card_number=data.get_credit_card_number(),
                    cvv=data.get_cvv(),
                    brand=data.get_brand(),
                )
            )
            await session.commit()



