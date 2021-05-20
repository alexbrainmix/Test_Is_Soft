from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    surname: str = Field(..., min_length=2, max_length=50)
    groups_id: int


class UserDB(User):
    id: int


class Group(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)


class GroupDB(Group):
    id: int
