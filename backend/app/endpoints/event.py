from datetime import date
from uuid import UUID

from fastapi import status

from app import crud, schemas

from . import api_router


@api_router.post(
    "/event",
    response_model=schemas.Event,
    status_code=status.HTTP_201_CREATED,
    tags=["event"],
    response_description="The created event.",
)
async def create_event(event: schemas.EventCreate):
    """Create a new event."""
    return crud.event.create(event)


@api_router.get(
    "/event/list",
    response_model=list[schemas.Event],
    status_code=status.HTTP_200_OK,
    tags=["event"],
    response_description="A list of existing events.",
)
async def get_list(start: date | None = None, end: date | None = None):
    """Get a list of existing events."""
    return crud.event.get_list(start, end)


@api_router.get(
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
    tags=["event"],
    response_description="The requested event.",
)
async def get_event(event_id: UUID):
    """Get an existing event."""
    return crud.event.get(event_id)


@api_router.patch(
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
    tags=["event"],
    response_description="The updated event.",
)
async def update_event(event_id: UUID, event_update: schemas.EventUpdate):
    """Update an existing event."""
    return crud.event.update(event_id, event_update)


@api_router.delete(
    "/event/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["event"],
)
async def delete_event(event_id: UUID):
    """Delete an existing event."""
    crud.event.delete(event_id)
