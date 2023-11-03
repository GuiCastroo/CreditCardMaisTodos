from src.domain.ports.outbound.protocol_repositories.creditcard_repository import ICreditCardRepository
from src.domain.entities.credit_card import CreditCard
from sqlalchemy.future import select
from src.adapters.outbound.orm.models import CreditCardModel
from fastapi_pagination.ext.sqlalchemy import paginate
from src.adapters.outbound.orm.database import get_db
from datetime import datetime


class CreditCardRepository(ICreditCardRepository):
    def __init__(self, db: get_db):
        self._db = db

    async def get_all(self):
        async with self._db as session:
            query = select(CreditCardModel)
            paginated_results = await paginate(session, query)
            return paginated_results

    async def get_by_filter(self, value: str):
        async with self._db as session:
            stmt = await session.execute(
                select(CreditCardModel).where(CreditCardModel.id == value)
            )
            result = stmt.all()
            if result:
                return result[0].CreditCardModel
            return None

    async def create(self, data: CreditCard):
        async with self._db as session:
            session.add(
                CreditCardModel(
                    id=data.get_identification(),
                    expiration_date=datetime.strptime(data.get_exp_date(), "%Y-%m-%d").date(),
                    holder=data.get_holder(),
                    credit_card_number=data.get_credit_card_number(),
                    cvv=data.get_cvv(),
                    brand=data.get_brand(),
                )
            )
            await session.commit()
