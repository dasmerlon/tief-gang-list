from uuid import UUID

from fastapi_sqlalchemy import db
from sqlalchemy import func

from app import models, schemas


def create(entry_event: schemas.EntryEventCreate) -> int:
    db_entry_event = models.EntryEvent(
        event_type=entry_event.event_type, event_id=entry_event.event_id
    )
    db.session.add(db_entry_event)
    db.session.commit()

    return get_guests_on_site(entry_event.event_id)


def get_guests_on_site(event_id: UUID) -> int:
    arrived = (
        db.session.query(func.count(models.EntryEvent.id))
        .filter(
            models.EntryEvent.event_type == schemas.EntryEventType.arrival,
            models.EntryEvent.event_id == event_id,
        )
        .scalar_subquery()
    )

    departured = (
        db.session.query(func.count(models.EntryEvent.id))
        .filter(
            models.EntryEvent.event_type == schemas.EntryEventType.departure,
            models.EntryEvent.event_id == event_id,
        )
        .scalar_subquery()
    )

    guests_on_site = db.session.query(
        (arrived - departured).label("guests-on-site")
    ).one()

    return guests_on_site[0]
