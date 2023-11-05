from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import MetaData

from src.settings import settings

engine = create_async_engine(settings.DB_URL, poolclass=NullPool, echo=False)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,

)

metadata = MetaData()
async def get_db() -> AsyncSession:
    async with Session() as session:
        yield session
