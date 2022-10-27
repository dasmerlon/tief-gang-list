from datetime import datetime
from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.post(
    "/entry-event",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_201_CREATED,
)
async def create_entry_event(entry_event: schemas.EntryEventCreate):
    guests_on_site = crud.entry_event.create(entry_event)
    return {"guests_on_site": guests_on_site}


@app.get(
    "/guests-on-site/{event_id}",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_200_OK,
)
async def get_guests_on_site(event_id: UUID):
    guests_on_site = crud.entry_event.get_guests_on_site(event_id)
    return {"guests_on_site": guests_on_site}


@app.get(
    "/entry-event/list",
    response_model=list[schemas.EntryEvent],
    status_code=status.HTTP_200_OK,
)
async def get_list(
    event_id: UUID | None = None,
    event_type: schemas.EntryEventType | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
):
    return crud.entry_event.get_list(event_id, event_type, start, end)
