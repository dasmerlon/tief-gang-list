from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.get(
    "/guests-on-site/{event_id}",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_200_OK,
)
async def read_guests_on_site(event_id: UUID):
    return {"guests_on_site": 123}


@app.post(
    "/entry-event",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_200_OK,
)
async def create_entry_event(entry_event: schemas.EntryEventCreate):
    count = crud.entry_event.create(entry_event)
    return {"guests_on_site": count}