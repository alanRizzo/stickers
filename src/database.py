from typing import AsyncIterator

from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    "postgresql+asyncpg://scott:tiger@localhost/test",
    echo=True,  # logging
)


AsyncSession = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    future=True,
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        yield AsyncSession
    except SQLAlchemyError as e:
        logger.exception(e)
