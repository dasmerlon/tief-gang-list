import json

import typer
import uvicorn
from fastapi.openapi.utils import get_openapi
from sqlalchemy import text
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from app import app, endpoints, models  # noqa F403 F401
from app.db import Base, engine
from app.helpers.seed import seed_db

cli = typer.Typer()

# Add the router
app.include_router(endpoints.api_router)


@cli.command()
def run():
    # run server
    uvicorn.run(app, host="0.0.0.0")


@cli.command()
def createdb():
    if database_exists(engine.url):
        print("Database already exists.")
        return

    print("Creating database")
    # Create the database
    create_database(engine.url)

    print("Initializing postgres extensions")
    with engine.connect() as connection:
        connection.execute(text('create extension if not exists "uuid-ossp";'))
        connection.execute(text("commit;"))

    # Create the actual database schema
    print("Creating schema")
    Base.metadata.create_all(bind=engine)


@cli.command()
def dropdb():
    if not database_exists(engine.url):
        print("Database doesn't exists.")
        return

    # Drop the database
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


@cli.command()
def seed():
    print("Creating seed data.")
    seed_db()


cli()
