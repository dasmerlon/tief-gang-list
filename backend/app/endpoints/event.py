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
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
)
async def read_event(event_id: UUID):
    return crud.event.get(event_id)


@app.delete(
    "/event/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_event(event_id: UUID):
    crud.event.delete(event_id)
