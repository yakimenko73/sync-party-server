from typing import Optional, Final

from pydantic import BaseSettings

ROOM_KEY_LENGTH: Final[int] = 9


class Settings(BaseSettings):
    # mongodb config
    MONGODB_HOST: Optional[str] = None
    MONGODB_PORT: Optional[int] = None
    MONGODB_USERNAME: Optional[str] = None
    MONGODB_PASSWORD: Optional[str] = None
    MONGODB_DATABASE: Optional[str] = None

    @property
    def connection_string(self):
        return f"mongodb://{self.MONGODB_USERNAME}:{self.MONGODB_PASSWORD}@{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DATABASE}"

    class Config:
        orm_mode = True
