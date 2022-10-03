from datetime import date, time

from pydantic import UUID4, BaseModel


class EventBase(BaseModel):
    name: str
    date: date
    registration_deadline: time | None = None


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class Event(EventBase):
    id: UUID4
