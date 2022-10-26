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
async def read_guests_on_site(event_id: UUID):
    guests_on_site = crud.entry_event.get_guests_on_site(event_id)
    return {"guests_on_site": guests_on_site}


@app.get(
    "/entry-events/{event_id}",
    response_model=schemas.EntryEventList,
    status_code=status.HTTP_200_OK,
)
async def read_entry_events(event_id: UUID):
    entry_events = crud.entry_event.get_entry_events(event_id)
    return {"entry_events": entry_events}
