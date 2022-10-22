from sqlalchemy import Column, Date, DateTime, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    registration_deadline = Column(DateTime)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    registrations = relationship("Registration", back_populates="event")

    def __repr__(self):
        return (
            f"Event(id={self.id}, "
            f"name={self.name}, "
            f"date={self.date}), "
            f"registration_deadline={self.registration_deadline}), "
        )
