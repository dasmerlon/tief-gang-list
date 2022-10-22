from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    func,
    text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db import Base


class Registration(Base):
    __tablename__ = "registration"
    __table_args__ = (UniqueConstraint("guest_id", "event_id"),)

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    guest_id = Column(ForeignKey("guest.id"), nullable=False)
    event_id = Column(ForeignKey("event.id"), nullable=False)
    arrived = Column(Boolean, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    guest = relationship("Guest", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")

    def __repr__(self):
        return (
            f"Registration(id={self.id}, "
            f"guest_id={self.guest_id}, "
            f"event_id={self.event_id}), "
            f"arrived={self.arrived}), "
            f"created_at={self.created_at}), "
        )