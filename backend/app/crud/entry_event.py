from datetime import datetime
from uuid import UUID

from fastapi_sqlalchemy import db
from sqlalchemy import func, select

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
        select(func.count(models.EntryEvent.id))
        .where(
            models.EntryEvent.event_type == schemas.EntryEventType.arrival,
            models.EntryEvent.event_id == event_id,
        )
        .scalar_subquery()
    )

    departured = (
        select(func.count(models.EntryEvent.id))
        .where(
            models.EntryEvent.event_type == schemas.EntryEventType.departure,
            models.EntryEvent.event_id == event_id,
        )
        .scalar_subquery()
    )

    return db.session.execute(select(arrived - departured)).scalar()


def get_list(
    event_id: UUID | None,
    event_type: schemas.EntryEventType | None,
    start: datetime | None,
    end: datetime | None,
) -> list[models.EntryEvent]:
    query = select(models.EntryEvent)

    if event_id is not None:
        query = query.where(models.EntryEvent.event_id == event_id)

    if event_type is not None:
        query = query.where(models.EntryEvent.event_type == event_type)

    if start is not None:
        query = query.where(models.EntryEvent.created_at >= start)

    if end is not None:
        query = query.where(models.EntryEvent.created_at <= end)

    return db.session.scalars(query).all()
