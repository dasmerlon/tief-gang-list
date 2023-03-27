from uuid import UUID

from fastapi import status

from app import crud, schemas

from . import api_router


@api_router.post(
    "/guest",
    response_model=schemas.Guest,
    status_code=status.HTTP_201_CREATED,
    tags=["guest"],
    response_description="The created guest.",
)
async def create_guest(guest: schemas.GuestCreate):
    """Create a new guest."""
    return crud.guest.create(guest)


@api_router.post(
    "/guest/registration",
    response_model=schemas.Registration,
    status_code=status.HTTP_201_CREATED,
    tags=["guest"],
    response_description="The created registration.",
)
async def create_guest_on_site(
    guest: schemas.GuestCreate, event_id: UUID, arrived: bool
):
    """Create a registration for a new guest on site of an event."""
    return crud.guest.create_on_site(guest, event_id, arrived)


@api_router.get(
    "/guest/list",
    response_model=list[schemas.Guest],
    status_code=status.HTTP_200_OK,
    tags=["guest"],
    response_description="A list of existing guests.",
)
async def get_list(
    first_name_start: str | None = None,
    last_name_start: str | None = None,
    buddy: str | None = None,
    subscribed: bool | None = None,
):
    """Get a list of existing guests."""
    return crud.guest.get_list(first_name_start, last_name_start, buddy, subscribed)


@api_router.get(
    "/guest/{guest_id}",
    response_model=schemas.Guest,
    status_code=status.HTTP_200_OK,
    tags=["guest"],
    response_description="The requested guest.",
)
async def get_guest(guest_id: UUID):
    """Get an existing guest."""
    return crud.guest.get(guest_id)


@api_router.patch(
    "/guest/{guest_id}",
    response_model=schemas.Guest,
    status_code=status.HTTP_200_OK,
    tags=["guest"],
    response_description="The updated guest.",
)
async def update_guest(guest_id: UUID, guest_update: schemas.GuestUpdate):
    """Update an existing guest."""
    return crud.guest.update(guest_id, guest_update)


@api_router.delete(
    "/guest/{guest_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["guest"],
)
async def delete_guest(guest_id: UUID):
    """Delete an existing guest."""
    crud.guest.delete(guest_id)
