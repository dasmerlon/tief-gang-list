from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db import Base


class Registration(Base):
    __tablename__ = "registrations"
    __table_args__ = (UniqueConstraint("guest_id", "event_id"),)

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    guest_id = Column(ForeignKey("guests.id", ondelete="CASCADE"), nullable=False)
    event_id = Column(ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    arrived = Column(Boolean, nullable=False)
    buddy = Column(String, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    guest = relationship("Guest", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")

    def __repr__(self):
        return (
            f"Registration(id={self.id}, "
            f"guest_id={self.guest_id}, "
            f"event_id={self.event_id}), "
            f"arrived={self.arrived}), "
            f"buddy={self.buddy}), "
            f"created_at={self.created_at}), "
        )
