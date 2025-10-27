import asyncio
import os
import sys
import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Add the app directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.orms.base import Base
from src.config import settings
from main import app

# Use a test database
TEST_DB_URL = str(settings.db_url).replace("mealy", "mealy_test")

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session")
async def test_engine():
    """Create a test database engine."""
    # Create test database engine without database name
    base_url = TEST_DB_URL.rsplit('/', 1)[0]
    db_name = TEST_DB_URL.rsplit('/', 1)[1]
    
    # Connect to default database to create test database
    engine = create_async_engine(f"{base_url}/postgres", isolation_level="AUTOCOMMIT")
    
    async with engine.begin() as conn:
        # Drop test database if it exists and create it again
        await conn.execute(f'DROP DATABASE IF EXISTS {db_name}')
        await conn.execute(f'CREATE DATABASE {db_name}')
    
    await engine.dispose()
    
    # Create engine for test database
    engine = create_async_engine(TEST_DB_URL, echo=True)
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Clean up
    await engine.dispose()
    
    # Connect to default database to drop test database
    engine = create_async_engine(f"{base_url}/postgres", isolation_level="AUTOCOMMIT")
    async with engine.begin() as conn:
        await conn.execute(f'DROP DATABASE IF EXISTS {db_name}')
    await engine.dispose()

@pytest_asyncio.fixture
async def test_session(test_engine):
    """Create a test database session."""
    async_session = sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False
    )
    
    async with async_session() as session:
        # Start a transaction
        async with session.begin():
            yield session
            # Rollback the transaction after the test
            await session.rollback()
    # Close the session
    await session.close()

@pytest_asyncio.fixture
async def client():
    """Create a test client for FastAPI application."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client