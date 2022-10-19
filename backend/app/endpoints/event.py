from datetime import date
from uuid import UUID

from fastapi import status

from app import app, schemas


@app.get(
    "/event/{event_id}",
    response_model=schemas.Event,
    status_code=status.HTTP_200_OK,
)
async def read_event(event_id: UUID):
    return {"id": event_id, "name": "rofl", "date": date.today()}
