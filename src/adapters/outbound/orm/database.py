from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

user = "admin"
password = "admin"
host = "localhost"
port = "5432"
database = "credicard"

db_url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"

engine = create_async_engine(db_url)

SESSION = sessionmaker(
    engine=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    future=True,
    echo=True,
    poolclass=NullPool
)



