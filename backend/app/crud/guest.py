from uuid import UUID

from fastapi_sqlalchemy import db
from sqlalchemy import func

from app import models, schemas


def create(guest: schemas.GuestCreate) -> models.Guest:
    db_guest = models.Guest(
        first_name=guest.first_name,
        last_name=guest.last_name,
        buddy=guest.buddy,
        email=guest.email,
        subscribed=guest.subscribed,
    )

    db.session.add(db_guest)
    db.session.commit()
    return db_guest


def get(guest_id: UUID) -> models.Guest | None:
    return db.session.query(models.Guest).get(guest_id)


def get_list(
    first_name_start: str | None,
    last_name_start: str | None,
    buddy: str | None,
    subscribed: bool | None,
) -> list[models.Guest]:
    query = db.session.query(models.Guest)

    if first_name_start is not None:
        query = query.filter(
            func.lower(models.Guest.first_name).startswith(func.lower(first_name_start))
        )

    if last_name_start is not None:
        query = query.filter(
            func.lower(models.Guest.last_name).startswith(func.lower(last_name_start))
        )

    if buddy is not None:
        query = query.filter(models.Guest.buddy == buddy)

    if subscribed is not None:
        query = query.filter(models.Guest.subscribed == subscribed)

    return query.all()


def update(guest_id: UUID, guest_update: schemas.GuestUpdate) -> models.Guest:
    changes = guest_update.dict(exclude_unset=True)
    db.session.query(models.Guest).filter(models.Guest.id == guest_id).update(changes)


def delete(guest_id: UUID):
    db_guest = get(guest_id)
    db.session.delete(db_guest)
    db.session.commit()
