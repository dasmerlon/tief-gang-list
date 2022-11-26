from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.db import engine

tags_metadata = [
    {
        "name": "entry_event",
        "description": "The event when a guest arrives or departs.",
    },
]

app = FastAPI(
    title="tief-gang-list",
    version="0.0.1",
    description="A cool gang. 😎",
    openapi_tags=tags_metadata,
)

app.add_middleware(DBSessionMiddleware, custom_engine=engine)
