from uuid import UUID

from fastapi import status

from app import app, schemas


@app.get(
    "/guests-on-site/{event_id}",
    response_model=schemas.GuestsOnSite,
    status_code=status.HTTP_200_OK,
)
async def read_guest(event_id: UUID):
    return {"guests_on_site": 123}
