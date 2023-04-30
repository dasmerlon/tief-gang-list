from datetime import date, datetime

from pydantic import UUID4, BaseModel, validator

from app.helpers.validators import check_string_not_empty


class EventBase(BaseModel):
    name: str
    date: date
    registration_deadline: datetime | None = None

    _not_empty = validator("name", allow_reuse=True)(check_string_not_empty)


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class Event(EventBase):
    id: UUID4

    class Config:
        orm_mode = True
