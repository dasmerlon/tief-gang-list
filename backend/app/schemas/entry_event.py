from enum import Enum
from datetime import datetime
from pydantic import UUID4, BaseModel

from app import schemas


class EntryEventType(str, Enum):
    arrival = "arrival"
    departure = "departure"


class EntryEventBase(BaseModel):
    event_type: EntryEventType


class EntryEventCreate(EntryEventBase):
    event_id: UUID4


class EntryEvent(EntryEventBase):
    id: UUID4
    event: schemas.Event
    created_at: datetime

    class Config:
        orm_mode = True


class EntryEventList(BaseModel):
    entry_events: list[EntryEvent]


class GuestsOnSite(BaseModel):
    guests_on_site: int
