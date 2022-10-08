from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.db import engine

app = FastAPI()

app.add_middleware(DBSessionMiddleware, custom_engine=engine)
