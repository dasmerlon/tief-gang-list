from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://localhost/tiefgang", echo=True, future=True
)

Base = declarative_base()
