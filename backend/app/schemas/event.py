from datetime import date, datetime

from pydantic import UUID4, BaseModel


class EventBase(BaseModel):
    name: str
    date: date
    registration_deadline: datetime | None = None


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class Event(EventBase):
    id: UUID4

    class Config:
        orm_mode = True
