from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import BYTEA
from src.adapters.outbound.orm.database import engine
from asyncio import run


BASE = declarative_base()


class CreditCardModel(BASE):
    __tablename__ = 'creditcard'

    id = Column(String, primary_key=True)
    expiration_date = Column(DateTime)
    holder = Column(String)
    credit_card_number = Column(BYTEA)
    cvv = Column(Integer)
    brand = Column(String)


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(BASE.metadata.drop_all)
        await conn.run_sync(BASE.metadata.create_all)


if __name__ == "__main__":
    run(create_database())
