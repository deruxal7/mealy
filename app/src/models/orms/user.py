from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

from .base import BaseORM

class UserORM(BaseORM):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False, nullable=False)