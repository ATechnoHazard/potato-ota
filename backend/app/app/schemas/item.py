from typing import Optional

from pydantic import BaseModel, UUID4, HttpUrl


# Shared properties
class ItemBase(BaseModel):
    url: HttpUrl
    build_date: int
    build_type: str
    device: str
    dish: str
    downloads: int
    filename: str
    md5: str
    notes: Optional[str]
    size: int
    version: str


# Properties to receive on item creation
class ItemCreate(ItemBase):
    user: UUID4
    pass


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: UUID4
    user: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
