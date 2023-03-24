from typing import AsyncIterator

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StickerRepository(Base):
    __tablename__ = "sticker"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(80), unique=True)
    category = Column(String(80))

    @classmethod
    async def fetch_all(cls, session: AsyncSession) -> AsyncIterator:
        __import__("ipdb").set_trace()
        stmt = select(cls)
        stream = await session.stream_scalars(stmt.order_by(cls.id))
        async for row in stream:
            yield row
