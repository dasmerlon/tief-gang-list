from uuid import UUID

from fastapi_sqlalchemy import db

from app import models, schemas


def get(event_id: UUID) -> models.Event | None:
    return db.session.query(models.Event).get(event_id)


def create(event: schemas.EventCreate) -> models.Event:
    db_event = models.Event(
        name=event.name,
        date=event.date,
        registration_deadline=event.registration_deadline,
    )

    db.session.add(db_event)
    db.session.commit()
    return db_event
