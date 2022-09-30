from .endpoints import *

from app import app


def main():
    # run server
    uvicorn.run(app, host="0.0.0.0")