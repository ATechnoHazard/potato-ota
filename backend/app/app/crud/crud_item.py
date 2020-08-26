from typing import List

from fastapi.encoders import jsonable_encoder
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(
            self, db: Session, *, obj_in: ItemCreate, owner_id: UUID4
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user=owner_id)  # noqa
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
            self, db: Session, *, owner_id: UUID4, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        return (
            db.query(self.model)
                .filter(Item.user == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )


item = CRUDItem(Item)
