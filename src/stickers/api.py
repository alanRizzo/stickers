from fastapi import APIRouter, Depends, status

from src.stickers.schemas import StickerModel
from src.stickers.services import StickerService

router = APIRouter(
    prefix="/stickers",
    tags=["stickers"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=None)
async def get_stickers(
    stickers: list[StickerModel] = Depends(StickerService),
) -> list[StickerModel]:
    return await stickers.get()


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
# async def create_sticker(
#    sticker: StickerModel, db_session: AsyncSession
# ) -> StickerModel:
#    await StickerService.create(db_session, sticker)
#
#
# @router.delete("/{sticker_id}", status_code=status.HTTP_200_OK, response_model=None)
# async def remove_sticker(sticker_id: int, db_session: AsyncSession) -> None:
#    await StickerService.remove(db_session, sticker_id)
