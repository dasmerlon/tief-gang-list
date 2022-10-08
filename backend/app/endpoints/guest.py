from uuid import UUID

from fastapi import status

from app import app, crud
from app.schemas.guest import Guest


@app.get(
    "/guest/{guest_id}",
    response_model=Guest,
    status_code=status.HTTP_200_OK,
)
async def read_guest(guest_id: UUID):
    return crud.guest.get(guest_id)
