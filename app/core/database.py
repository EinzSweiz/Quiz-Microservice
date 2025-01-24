from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
    
metadata = Base.metadata

# SQLALCHEMY_DATABASE_URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///quizes.db"
# Create the async engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create a sessionmaker instance
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Dependency to get a database session
async def get_session():
    async with new_session() as session:
        yield session

# Base class for declarative models

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
