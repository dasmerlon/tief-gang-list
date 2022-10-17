from datetime import datetime

from pydantic import UUID4, BaseModel

from app.schemas.event import Event
from app.schemas.guest import Guest


class RegistrationBase(BaseModel):
    pass


class RegistrationCreate(RegistrationBase):
    guest_id: UUID4
    event_id: UUID4


class Registration(RegistrationBase):
    id: UUID4
    created_at: datetime
    guest: Guest
    event: Event

    class Config:
        orm_mode = True
