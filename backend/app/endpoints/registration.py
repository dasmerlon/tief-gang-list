from uuid import UUID

from fastapi import status

from app import crud, schemas

from . import api_router


@api_router.post(
    "/registration",
    response_model=schemas.Registration,
    status_code=status.HTTP_201_CREATED,
    tags=["registration"],
    response_description="The created registration.",
)
async def create_registration(registration: schemas.RegistrationCreate):
    return crud.registration.create(registration)


@api_router.post(
    "/registration/on-site",
    response_model=schemas.Registration,
    status_code=status.HTTP_201_CREATED,
    tags=["registration"],
    response_description="The created registration.",
)
async def create_registration_on_site(registration_on_site: schemas.RegistrationOnSite):
    """Create a registration for a new guest on site of an event."""
    return crud.registration.create_on_site(registration_on_site)


@api_router.get(
    "/registration/list",
    response_model=list[schemas.Registration],
    status_code=status.HTTP_200_OK,
    tags=["registration"],
    response_description="A list of existing registrations.",
)
async def get_list(
    arrived: bool | None = None,
    buddy: str | None = None,
    guest_id: UUID | None = None,
    event_id: UUID | None = None,
):
    """Get a list of existing registrations."""
    return crud.registration.get_list(arrived, buddy, guest_id, event_id)


@api_router.get(
    "/registration/{registration_id}",
    response_model=schemas.Registration,
    status_code=status.HTTP_200_OK,
    tags=["registration"],
    response_description="The requested registration.",
)
async def get_registration(registration_id: UUID):
    """Get an existing registration."""
    return crud.registration.get(registration_id)


@api_router.patch(
    "/registration/{registration_id}",
    response_model=schemas.Registration,
    status_code=status.HTTP_200_OK,
    tags=["registration"],
    response_description="The updated registration.",
)
async def update_registration(
    registration_id: UUID, registration_update: schemas.RegistrationUpdate
):
    """Update an existing registration."""
    return crud.registration.update(registration_id, registration_update)


@api_router.delete(
    "/registration/{registration_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["registration"],
)
async def delete_registration(registration_id: UUID):
    """Delete an existing registration."""
    crud.registration.delete(registration_id)
