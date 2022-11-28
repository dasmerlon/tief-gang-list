import json

import uvicorn
from sqlalchemy import text
from sqlalchemy_utils.functions import create_database, database_exists, drop_database
from fastapi.openapi.utils import get_openapi
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


@cli.command()
def generate_api_spec():
    print("Generating openapi schema.")

    with open("openapi.json", "w") as file:
        json.dump(
            get_openapi(
                title=app.title,
                version=app.version,
                openapi_version=app.openapi_version,
                description=app.description,
                routes=app.routes,
            ),
            file,
            sort_keys=True,
            indent=4,
        )


cli()
