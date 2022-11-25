from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.db import engine

app = FastAPI(title="tief-gang-list", version="0.0.1", description="A cool gang. 😎")

app.add_middleware(DBSessionMiddleware, custom_engine=engine)
