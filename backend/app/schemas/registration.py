from datetime import datetime

from pydantic import UUID4, BaseModel, validator

from app import schemas
from app.helpers.validators import check_string_not_empty


class RegistrationBase(BaseModel):
    arrived: bool


class RegistrationCreate(RegistrationBase):
    guest_id: UUID4
    event_id: UUID4
    buddy: str

    _not_empty = validator("buddy", allow_reuse=True)(check_string_not_empty)


class RegistrationOnSite(RegistrationBase):
    guest: schemas.GuestCreate
    event_id: UUID4
    buddy: str

    _not_empty = validator("buddy", allow_reuse=True)(check_string_not_empty)


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
