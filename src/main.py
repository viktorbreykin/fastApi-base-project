from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI()
main_app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)
