from datetime import datetime
from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.post(
    "/entry-event",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_201_CREATED,
    tags=["entry_event"],
    response_description="The number of guests on site of an event.",
)
async def create_entry_event(entry_event: schemas.EntryEventCreate):
    """Create a new entry event for an event."""
    guests_on_site = crud.entry_event.create(entry_event)
    return {"guests_on_site": guests_on_site}


@app.get(
    "/guests-on-site/{event_id}",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_200_OK,
    tags=["entry_event"],
    response_description="The number of guests on site of an event.",
)
async def get_guests_on_site(event_id: UUID):
    """Get the number of guests on site of an event."""
    guests_on_site = crud.entry_event.get_guests_on_site(event_id)
    return {"guests_on_site": guests_on_site}


@app.get(
    "/entry-event/list",
    response_model=list[schemas.EntryEvent],
    status_code=status.HTTP_200_OK,
    tags=["entry_event"],
    response_description="A list of existing entry events",
)
async def get_list(
    event_id: UUID | None = None,
    event_type: schemas.EntryEventType | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
):
    """Get a list of existing entry events."""
    return crud.entry_event.get_list(event_id, event_type, start, end)
