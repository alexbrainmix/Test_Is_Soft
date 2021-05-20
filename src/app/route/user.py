from typing import List
from fastapi import APIRouter, HTTPException, Path, status
from crud import user, group
from models.models import UserDB, User


router = APIRouter()


@router.post("/", response_model=UserDB, status_code=status.HTTP_201_CREATED)
async def create_user(obj: User):
    group_obj = await group.get_by_id(obj.groups_id)
    if not group_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    user_id = await user.create(obj)
    response_object = {
        "id": user_id,
        "name": obj.name,
        "surname": obj.surname,
        "groups_id": obj.groups_id,
    }
    return response_object


@router.get("/{id}/", response_model=UserDB)
async def read_user(id: int = Path(..., gt=0),):
    user_obj = await user.get_by_id(id)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_obj


@router.get("/", response_model=List[UserDB])
async def read_all_users():
    return await user.get_all()


@router.put("/{id}/", response_model=UserDB)
async def update_user(obj: User, id: int = Path(..., gt=0), ):
    group_obj = await group.get_by_id(obj.groups_id)
    if not group_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")

    user_obj = await user.get_by_id(id)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_id = await user.update(id, obj)
    response_object = {
        "id": user_id,
        "name": obj.name,
        "surname": obj.surname,
        "groups_id": obj.groups_id,
    }
    return response_object


@router.delete("/{id}/", response_model=UserDB)
async def delete_user(id: int = Path(..., gt=0)):
    user_obj = await user.get_by_id(id)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    await user.delete(id)
    return user_obj
