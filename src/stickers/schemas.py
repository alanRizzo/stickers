from pydantic import BaseModel, constr


class StickerModel(BaseModel):
    id: int
    name: constr(max_length=80)
    category: constr(max_length=80)

    class Config:
        orm_mode = True
