from datetime import date, datetime
from uuid import UUID

from fastapi import status

from app import app, schemas


@app.get(
    "/registration/{registration_id}",
    response_model=schemas.Registration,
    status_code=status.HTTP_200_OK,
)
async def get_registration(registration_id: UUID):
    return {
        "id": registration_id,
        "guest": {"id": registration_id},
        "event": {"id": registration_id, "name": "rofl", "date": date.today()},
        "arrived": False,
        "created_at": datetime.now(),
    }
