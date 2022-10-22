from enum import Enum

from pydantic import UUID4, BaseModel

from app import schemas


class GuestCountType(str, Enum):
    arrival = "arrival"
    departure = "departure"


class GuestCountBase(BaseModel):
    count_type: GuestCountType


class GuestCountCreate(GuestCountBase):
    guest_id: UUID4
    event_id: UUID4


class GuestCount(GuestCountBase):
    id: UUID4
    event: schemas.Event
    guest: schemas.Guest | None = None

    class Config:
        orm_mode = True
