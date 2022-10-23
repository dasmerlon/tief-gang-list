from enum import Enum

from pydantic import UUID4, BaseModel

from app import schemas


class EntryEventType(str, Enum):
    arrival = "arrival"
    departure = "departure"


class EntryEventBase(BaseModel):
    count_type: EntryEventType


class EntryEventCreate(EntryEventBase):
    event_id: UUID4


class EntryEvent(EntryEventBase):
    id: UUID4
    event: schemas.Event

    class Config:
        orm_mode = True


class GuestsOnSite(BaseModel):
    guests_on_site: int
