import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, unique=True, nullable=False)
    user = Column(UUID(as_uuid=True), index=True, nullable=False)
    url = Column(String, nullable=False)
    build_date = Column(Integer(), index=True, nullable=False)
    build_type = Column(String, nullable=False)
    device = Column(String, index=True, nullable=False)
    dish = Column(String, nullable=False)
    downloads = Column(Integer(), nullable=False)
    filename = Column(String, nullable=False)
    md5 = Column(String, nullable=False)
    notes = Column(String)
    size = Column(Integer(), nullable=False)
    version = Column(String)
