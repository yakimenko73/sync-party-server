from typing import Final, Optional

from beanie import Document, Indexed
from pydantic import BaseModel, Field

from config import config

FIELDS_EXAMPLE: Final[dict] = {
    "key": "L1S-dS12_",
    "public": False,
    "host": "host_session_key",
}

COLLECTION_NAME: Final[str] = "rooms"


class Room(Document):
    key: Indexed(str, unique=True) = Field(max_length=config.ROOM_KEY_LENGTH)
    public: Optional[bool] = False
    host: str = Field(max_length=32)

    class Collection:
        name = COLLECTION_NAME

    class Config:
        schema_extra = {
            "example": FIELDS_EXAMPLE
        }


class ResponseModel(BaseModel):
    key: str
    public: bool
    host: str

    class Config:
        schema_extra = {
            "example": FIELDS_EXAMPLE
        }
        orm_mode = True
