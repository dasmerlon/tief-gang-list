from sqlalchemy import Column, DateTime, Enum, ForeignKey, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app import schemas
from app.db import Base

EntryEventType: Enum = Enum(
    schemas.EntryEventType,
    name="entry_event_type",
    metadata=Base.metadata,
)


class EntryEvent(Base):
    __tablename__ = "entry_events"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    event_type = Column(EntryEventType, nullable=False)
    event_id = Column(ForeignKey("events.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    event = relationship("Event")

    def __repr__(self):
        return (
            f"EntryEvent(id={self.id}, "
            f"event_type={self.event_type}, "
            f"event_id={self.event_id}), "
        )
