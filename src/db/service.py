from typing import List

from beanie.operators import Eq

from models.room import Room


async def insert_room(room: Room) -> Room:
    return await room.create()


async def find_room_by_key(key: str) -> Room:
    return await Room.find_one(Eq(Room.key, key))


async def find_public_rooms() -> List[Room]:
    return await Room.find(Eq(Room.public, True)).to_list()
