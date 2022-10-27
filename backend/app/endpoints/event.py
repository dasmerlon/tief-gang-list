from datetime import date
from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.post(
    "/event",
    response_model=schemas.Event,
    status_code=status.HTTP_201_CREATED,
)
async def create_event(event: schemas.EventCreate):
    return crud.event.create(event)


@app.get(
    "/event/list",
    response_model=list[schemas.Event],
    status_code=status.HTTP_200_OK,
)
async def get_list(start: date | None = None, end: date | None = None):
    return crud.event.get_list(start, end)


@app.get(
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
)
async def get_event(event_id: UUID):
    return crud.event.get(event_id)


@app.put(
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
)
async def update_event(event_id: UUID, event_update: schemas.EventUpdate):
    return crud.event.update(event_id, event_update)


@app.delete(
    "/event/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_event(event_id: UUID):
    crud.event.delete(event_id)
