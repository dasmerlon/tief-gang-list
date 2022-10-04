from datetime import date, datetime
from uuid import UUID

from fastapi import status

from app import app
from app.schemas.registration import Registration


@app.get(
    "/registration/{registration_id}",
    response_model=Registration,
    status_code=status.HTTP_200_OK,
)
async def read_registration(registration_id: UUID):
    return {
        "id": registration_id,
        "guest": {"id": registration_id},
        "event": {"id": registration_id, "name": "rofl", "date": date.today()},
        "created_at": datetime.now(),
    }