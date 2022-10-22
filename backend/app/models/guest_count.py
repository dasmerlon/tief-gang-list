from sqlalchemy import Column, DateTime, Enum, ForeignKey, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app import schemas
from app.db import Base

GuestCountType: Enum = Enum(
    schemas.GuestCountType,
    name="guest_count_type",
    metadata=Base.metadata,
)


class GuestCount(Base):
    __tablename__ = "guest_count"

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    count_type = Column(GuestCountType, nullable=False)
    guest_id = Column(ForeignKey("guest.id"))
    event_id = Column(ForeignKey("event.id"), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    guest = relationship("Guest", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")

    def __repr__(self):
        return (
            f"GuestCount(id={self.id}, "
            f"count_type={self.count_type}, "
            f"event_id={self.event_id}), "
        )
