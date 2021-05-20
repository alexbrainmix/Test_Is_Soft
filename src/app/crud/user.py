import datetime
from app.models.models import User
from app.db.users import users
from app.db.base import database


async def create(obj: User):
    query = users.insert().values(name=obj.name, surname=obj.surname, groups_id=obj.groups_id)
    return await database.execute(query=query)


async def get_by_id(obj_id: int):
    query = users.select().where(obj_id == users.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)


async def update(obj_id: int, obj: User):
    query = (
        users
        .update()
        .where(obj_id == users.c.id)
        .values(name=obj.name, surname=obj.surname, groups_id=obj.groups_id, updated_at=datetime.datetime.utcnow())
        .returning(users.c.id)
    )
    return await database.execute(query=query)


async def delete(obj_id: int):
    query = users.delete().where(obj_id == users.c.id)
    return await database.execute(query=query)
