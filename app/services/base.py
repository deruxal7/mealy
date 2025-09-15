from sqlalchemy.ext.asyncio import AsyncSession

from ..models.orms.base import BaseORM

class BaseCRUD:
    model = BaseORM

    @classmethod
    async def create(cls, session: AsyncSession, data: dict):
        await cls._before_create(session, data)
        _model = cls.model(**data)
        session.add(_model)
        await session.commit()
        await session.refresh(_model)
        await cls._after_create(session, data)
        return _model

    @classmethod
    async def _before_create(cls, session: AsyncSession, data):
        pass

    @classmethod
    async def _after_create(cls, session: AsyncSession, data):
        pass


def with_model(model):
    def dec(crud):
        crud.model = model
        model.crud = crud
        return crud

    return dec
