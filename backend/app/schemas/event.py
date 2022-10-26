from datetime import date, datetime

from pydantic import UUID4, BaseModel, validator


class EventBase(BaseModel):
    name: str
    date: date
    registration_deadline: datetime | None = None


class EventCreate(EventBase):
    pass


# Python is stupid.
# We have to use a type alias to avoid problems with the pipe operator.
better_date = date


class EventUpdate(EventBase):
    name: str | None = None
    date: better_date | None = None

    @validator("name", "date")
    def prevent_none(cls, value):
        assert value is not None, "May not be None."
        return value


class Event(EventBase):
    id: UUID4

    class Config:
        orm_mode = True
