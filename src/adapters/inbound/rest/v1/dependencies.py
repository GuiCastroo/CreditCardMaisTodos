from src.adapters.outbound.orm.database import AsyncSession, get_db
from fastapi import Depends
from src.adapters.outbound.repositories.credit_card_repository import CreditCardRepository


async def get_credit_card_repository(db: AsyncSession = Depends(get_db)):
    return CreditCardRepository(db)