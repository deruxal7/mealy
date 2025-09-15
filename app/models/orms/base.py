from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ...config import settings

db_url = str(settings.DB_URL)

engine = create_async_engine(db_url)
asession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

Base = declarative_base()

class BaseORM(Base):
    __abstract__ = True
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseORM.metadata.create_all)

async def get_db():
    async with asession() as db:
        yield db 

