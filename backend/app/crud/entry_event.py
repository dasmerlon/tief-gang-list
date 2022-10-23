from fastapi_sqlalchemy import db

from app import models, schemas


def create(entry_event: schemas.EntryEventCreate) -> int:
    db_entry_event = models.EntryEvent(
        event_type=entry_event.event_type, event_id=entry_event.event_id
    )
    db.session.add(db_entry_event)
    db.session.commit()

    arrived = (
        db.session.query(models.EntryEvent)
        .count()
        .filter(
            models.EntryEvent.event_type == schemas.EntryEvent.arrival,
            models.EntryEvent.event_id == entry_event.event_id,
        )
        .subquery()
    )

    departured = (
        db.session.query(models.EntryEvent)
        .count()
        .filter(
            models.EntryEvent.event_type == schemas.EntryEvent.departure,
            models.EntryEvent.event_id == entry_event.event_id,
        )
        .subquery()
    )

    guests_on_site = (
        db.session.query(arrived - departured).label("guests-on-site").one()
    )

    return guests_on_site
