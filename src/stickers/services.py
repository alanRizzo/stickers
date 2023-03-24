from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.database import get_session
from src.stickers.repositories import StickerRepository
from src.stickers.schemas import StickerModel

# AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]


class StickerService:
    def __init__(self, session: async_sessionmaker = Depends(get_session)) -> None:
        self.db_session = session

    async def get(self) -> list[StickerModel]:
        __import__("ipdb").set_trace()
        async with self.db_session.begin() as session:
            stickers = await StickerRepository.fetch_all(session)
            return StickerModel.from_orm(stickers)


#    @classmethod
#    async def get_by_attribute(cls, db_session, attribute: str) -> StickerModel:
#        return await StickerRepository.find_by_attribute(db_session, attribute)
#
#    @classmethod
#    async def create(cls, db_session, sticker: StickerModel) -> None:
#        return await StickerRepository.find_by_attribute(db_session, sticker)
#
#    @classmethod
#    async def remove(cls, db_session, sticker: StickerModel) -> None:
#        return await StickerRepository.find_by_attribute(db_session, sticker)
