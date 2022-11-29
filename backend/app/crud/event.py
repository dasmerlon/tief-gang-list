from datetime import date
from uuid import UUID

from fastapi_sqlalchemy import db

from app import models, schemas


def create(event: schemas.EventCreate) -> models.Event:
    db_event = models.Event(
        name=event.name,
        date=event.date,
        registration_deadline=event.registration_deadline,
    )

    db.session.add(db_event)
    db.session.commit()
    return db_event


def get(event_id: UUID) -> models.Event | None:
    return db.session.query(models.Event).get(event_id)


def get_list(start: date | None, end: date | None) -> list[models.Event]:
    query = db.session.query(models.Event)

    if start is not None:
        query = query.filter(models.Event.date >= start)

    if end is not None:
        query = query.filter(models.Event.date <= end)

    return query.all()


def update(event_id: UUID, event_update: schemas.EventUpdate) -> models.Event:
    changes = event_update.dict(exclude_unset=True)
    db.session.query(models.Event).filter(models.Event.id == event_id).update(changes)

    db.session.commit()
    return get(event_id)


def delete(event_id: UUID):
    db_event = get(event_id)
    db.session.delete(db_event)
    db.session.commit()
