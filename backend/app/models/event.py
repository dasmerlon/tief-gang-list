from uuid import uuid4

from sqlalchemy import Column, Date, DateTime, String, func

from app.db import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    registration_deadline = Column(DateTime)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __repr__(self):
        return (
            f"Event(id={self.id!r}, "
            f"name={self.name!r}, "
            f"date={self.date!r}), "
            f"registration_deadline={self.registration_deadline!r}), "
        )
