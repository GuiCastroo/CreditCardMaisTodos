from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


user = "admin"
password = "admin"
host = "localhost"
port = "5432"
database = "credicard"

db_url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"

engine = create_async_engine(db_url, poolclass=NullPool, echo=False)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,

)


async def get_db() -> AsyncSession:
    async with Session() as session:
        yield session
