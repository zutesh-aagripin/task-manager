from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from db import database
from resources.routes import api_router

app = FastAPI(
    title="API documentation",
    description="Реализация сервиса из тестового задания",
    version="0.1.0",
)
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(Path(__file__).parent / "ui" / "index.html")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
