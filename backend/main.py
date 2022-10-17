import uvicorn
from sqlalchemy_utils.functions import create_database

from app.db import engine, Base
from app import app
from app.endpoints import *  # noqa F403 F401
from app.models import *  # noqa F403 F401


def main():
    db_url = engine.url
    create_database(db_url)
    Base.metadata.create_all()

    # run server
    uvicorn.run(app, host="0.0.0.0")


main()
