from fastapi import FastAPI

import models
from core.config import Settings
from database import engine
from routers.base import api_router


def create_table():
    models.Base.metadata.create_all(engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)
    create_table()
    include_router(app)
    return app


app = start_application()
