from datetime import datetime

from pydantic import UUID4, BaseModel

from app import schemas


class RegistrationBase(BaseModel):
    pass


class RegistrationCreate(RegistrationBase):
    guest_id: UUID4
    event_id: UUID4


class Registration(RegistrationBase):
    id: UUID4
    created_at: datetime
    guest: schemas.Guest
    event: schemas.Event

    class Config:
        orm_mode = True
