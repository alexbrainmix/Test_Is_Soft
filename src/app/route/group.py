from typing import List
from fastapi import APIRouter, HTTPException, Path, status
from app.crud import group
from app.models.models import GroupDB, Group


router = APIRouter()


@router.post("/", response_model=GroupDB, status_code=status.HTTP_201_CREATED)
async def create_group(obj: Group):
    group_id = await group.create(obj)
    response_object = {
        "id": group_id,
        "name": obj.name,
    }
    return response_object


@router.get("/{id}/", response_model=GroupDB)
async def read_group(obj_id: int = Path(..., gt=0),):
    group_obj = await group.get_by_id(obj_id)
    if not group_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group_obj


@router.get("/", response_model=List[GroupDB])
async def read_all_groups():
    return await group.get_all()


@router.put("/{id}/", response_model=GroupDB)
async def update_group(obj: Group, obj_id: int = Path(..., gt=0), ):
    group_obj = await group.get_by_id(obj_id)
    if not group_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    group_id = await group.update(obj_id, obj)
    response_object = {
        "id": group_id,
        "name": obj.name,
    }
    return response_object


@router.delete("/{id}/", response_model=GroupDB)
async def delete_group(obj_id: int = Path(..., gt=0)):
    group_obj = await group.get_by_id(obj_id)
    if not group_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    await group.delete(obj_id)
    return group_obj
