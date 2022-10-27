from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.post(
    "/registration",
    response_model=schemas.Registration,
    status_code=status.HTTP_201_CREATED,
)
async def create_registration(registration: schemas.RegistrationCreate):
    return crud.registration.create(registration)


@app.get(
    "/registration/list",
    response_model=list[schemas.Registration],
    status_code=status.HTTP_200_OK,
)
async def get_list(arrived: bool | None = None):
    return crud.registration.get_list(arrived)


@app.get(
    "/registration/{registration_id}",
    response_model=schemas.Registration,
    status_code=status.HTTP_200_OK,
)
async def get_registration(registration_id: UUID):
    return crud.registration.get(registration_id)


@app.put(
    "/registration/{registration_id}",
    response_model=schemas.Registration,
    status_code=status.HTTP_200_OK,
)
async def update_registration(
    registration_id: UUID, registration_update: schemas.RegistrationUpdate
):
    return crud.registration.update(registration_id, registration_update)


@app.delete(
    "/registration/{registration_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_registration(registration_id: UUID):
    crud.registration.delete(registration_id)
