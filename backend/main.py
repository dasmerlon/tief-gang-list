import uvicorn
from sqlalchemy import text
from sqlalchemy_utils.functions import create_database

from app.db import engine, Base
from app import app, models, endpoints  # noqa F403 F401


def main():
    db_url = engine.url
    create_database(db_url)

    with engine.connect() as connection:
        connection.execute(text('create extension if not exists "uuid-ossp";'))
        connection.execute(text("commit;"))

    Base.metadata.create_all()

    # run server
    uvicorn.run(app, host="0.0.0.0")


main()
