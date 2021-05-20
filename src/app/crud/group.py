import datetime
from app.models.models import Group
from app.db.groups import groups
from app.db.base import database


async def create(obj: Group):
    query = groups.insert().values(name=obj.name)
    return await database.execute(query=query)


async def get_by_id(obj_id: int):
    query = groups.select().where(obj_id == groups.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = groups.select()
    return await database.fetch_all(query=query)


async def update(obj_id: int, obj: Group):
    query = (
        groups
        .update()
        .where(obj_id == groups.c.id)
        .values(name=obj.name, updated_at=datetime.datetime.utcnow())
        .returning(groups.c.id)
    )
    return await database.execute(query=query)


async def delete(obj_id: int):
    query = groups.delete().where(obj_id == groups.c.id)
    return await database.execute(query=query)
