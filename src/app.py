from fastapi import FastAPI
from loguru import logger

from db import init_db
from routers.room import router as RoomRouter

app = FastAPI()


@app.on_event("startup")
async def app_init():
    logger.info("Init application...")

    await init_db()


app.include_router(RoomRouter, tags=["Rooms"], prefix="/rooms")
