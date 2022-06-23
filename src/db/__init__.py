from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import Settings
from models.room import Room


async def init_db():
    settings = Settings()
    client = AsyncIOMotorClient(settings.connection_string)

    await init_beanie(database=client.get_default_database(),
                      document_models=[Room])
