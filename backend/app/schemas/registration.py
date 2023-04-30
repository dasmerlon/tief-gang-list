from datetime import datetime

from pydantic import UUID4, BaseModel

from app import schemas


class RegistrationBase(BaseModel):
    arrived: bool


class RegistrationCreate(RegistrationBase):
    guest_id: UUID4
    event_id: UUID4
    buddy: str


class RegistrationUpdate(RegistrationBase):
    pass


class Registration(RegistrationBase):
    id: UUID4
    created_at: datetime
    guest: schemas.Guest
    event: schemas.Event
    buddy: str

    class Config:
        orm_mode = True
