import uvicorn

from app import app
from app.endpoints import *  # noqa F403 F401


def main():
    # run server
    uvicorn.run(app, host="0.0.0.0")
