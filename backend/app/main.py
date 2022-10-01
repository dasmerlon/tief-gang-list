from app import app

from .endpoints import *


def main():
    # run server
    uvicorn.run(app, host="0.0.0.0")
