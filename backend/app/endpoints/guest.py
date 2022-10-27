from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.post(
    "/guest",
    response_model=schemas.Guest,
    status_code=status.HTTP_201_CREATED,
)
async def create_guest(guest: schemas.GuestCreate):
    return crud.guest.create(guest)


@app.post(
    "/guest/registration",
    response_model=schemas.Registration,
    status_code=status.HTTP_201_CREATED,
)
async def create_guest_on_site(
    guest: schemas.GuestCreate, event_id: UUID, arrived: bool
):
    return crud.guest.create_on_site(guest, event_id, arrived)


@app.get(
    "/guest/list",
    response_model=list[schemas.Guest],
    status_code=status.HTTP_200_OK,
)
async def get_list(
    first_name_start: str | None = None,
    last_name_start: str | None = None,
    buddy: str | None = None,
    subscribed: bool | None = None,
):
    return crud.guest.get_list(first_name_start, last_name_start, buddy, subscribed)


@app.get(
    "/guest/{guest_id}",
    response_model=schemas.Guest,
    status_code=status.HTTP_200_OK,
)
async def get_guest(guest_id: UUID):
    return crud.guest.get(guest_id)


@app.put(
    "/guest/{guest_id}",
    response_model=schemas.Guest,
    status_code=status.HTTP_200_OK,
)
async def update_guest(guest_id: UUID, guest_update: schemas.GuestUpdate):
    return crud.guest.update(guest_id, guest_update)


@app.delete(
    "/guest/{guest_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_guest(guest_id: UUID):
    crud.guest.delete(guest_id)
