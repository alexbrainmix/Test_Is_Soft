from fastapi import FastAPI
from app.db.base import database, metadata, engine
from app.route import group, user


metadata.create_all(bind=engine)

app = FastAPI(title="Test IsSoft", debug=True)
app.include_router(group.router, prefix="/group", tags=["group"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
