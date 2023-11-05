from sqlalchemy.future import select

from src.adapters.inbound.rest.v1.token_jwt import UserCreate
from src.adapters.outbound.orm.models import UserModel


class UserRepository:
    def __init__(self, db):
        self._db = db

    async def create(self, data: UserCreate):
        async with self._db as session:
            session.add(
                UserModel(
                    username=data.username,
                    password=data.password
                )
            )
            await session.commit()

    async def get_by_filter(self, value: str):
        async with self._db as session:
            stmt = await session.execute(
                select(UserModel).where(UserModel.username == value)
            )
            result = stmt.all()
            if result:
                return result[0].UserModel
            return None
