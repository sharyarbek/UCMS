from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from fastapi import Depends
from typing import Annotated

class Base(DeclarativeBase):
    pass


engine = create_async_engine('sqlite+aiosqlite:///unisys.db')
new_async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with new_async_session() as session:
        yield session

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]