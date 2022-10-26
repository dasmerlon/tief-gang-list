from uuid import UUID

from fastapi import status

from app import app, crud, schemas


@app.get(
    "/guest/{guest_id}",
    response_model=schemas.Guest,
    status_code=status.HTTP_200_OK,
)
async def read_guest(guest_id: UUID):
    return crud.guest.get(guest_id)


@app.delete(
    "/guest/{guest_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_guest(guest_id: UUID):
    crud.guest.delete(guest_id)
