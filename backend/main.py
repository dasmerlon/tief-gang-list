import uvicorn
from sqlalchemy import text
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

import typer

from app.db import engine, Base
from app import app, models, endpoints  # noqa F403 F401

cli = typer.Typer()


@cli.command()
def run():
    # run server
    uvicorn.run(app, host="0.0.0.0")


@cli.command()
def createdb():
    if database_exists(engine.url):
        print("Database already exists.")
        return

    create_database(engine.url)

    with engine.connect() as connection:
        connection.execute(text('create extension if not exists "uuid-ossp";'))
        connection.execute(text("commit;"))

    Base.metadata.create_all()


@cli.command()
def dropdb():
    if not database_exists(engine.url):
        print("Database doesn't exists.")
        return

    drop_database(engine.url)


cli()
