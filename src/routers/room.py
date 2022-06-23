from typing import List

from fastapi import APIRouter, Body, HTTPException

from db import service
from models.room import Room, ResponseModel

router = APIRouter()


@router.put("/", response_description="Add room", response_model=ResponseModel)
async def add_room(room: Room = Body(...)):
    return await service.insert_room(room)


@router.get("/public", response_description="Get public rooms", response_model=List[ResponseModel])
async def get_public_rooms():
    return await service.find_public_rooms()


@router.get("/{key}", response_description="Get room by key", response_model=ResponseModel)
async def get_room(key: str):
    room = await service.find_room_by_key(key)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
