from uuid import uuid4

from sqlalchemy import (Column, DateTime, ForeignKey, String, UniqueConstraint,
                        func)
from sqlalchemy.orm import relationship

from app.db import Base


class Registration(Base):
    __tablename__ = "registration"
    __table_args__ = (UniqueConstraint("guest_id", "event_id"),)

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    guest_id = Column(ForeignKey("guest.id"), nullable=False)
    event_id = Column(ForeignKey("event.id"), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    guest = relationship("Guest", back_populates="events")
    event = relationship("Event", back_populates="guests")

    def __repr__(self):
        return (
            f"Registration(id={self.id!r}, "
            f"guest_id={self.guest_id!r}, "
            f"event_id={self.event_id!r}), "
            f"created_at={self.created_at!r}), "
        )
