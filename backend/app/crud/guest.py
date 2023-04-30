from uuid import UUID

from fastapi_sqlalchemy import db
from sqlalchemy import func, select
from sqlalchemy import update as sql_update

from app import crud, models, schemas


def create(guest: schemas.GuestCreate) -> models.Guest:
    db_guest = models.Guest(
        first_name=guest.first_name,
        last_name=guest.last_name,
        email=guest.email,
        subscribed=guest.subscribed,
    )
    db.session.add(db_guest)

    db.session.commit()
    return db_guest


def create_on_site(
    guest: schemas.GuestCreate, event_id: UUID, arrived: bool
) -> models.Registration:
    db_guest = models.Guest(
        first_name=guest.first_name,
        last_name=guest.last_name,
        email=guest.email,
        subscribed=guest.subscribed,
    )
    db.session.add(db_guest)
    db.session.flush()

    registration = schemas.RegistrationCreate(
        guest_id=db_guest.id, event_id=event_id, arrived=arrived
    )

    db.session.commit()
    return crud.registration.create(registration)


def get(guest_id: UUID) -> models.Guest | None:
    return db.session.get(models.Guest, guest_id)


def get_list(
    first_name_start: str | None,
    last_name_start: str | None,
    subscribed: bool | None,
) -> list[models.Guest]:
    query = select(models.Guest)

    if first_name_start is not None:
        query = query.where(
            func.lower(models.Guest.first_name).startswith(func.lower(first_name_start))
        )

    if last_name_start is not None:
        query = query.where(
            func.lower(models.Guest.last_name).startswith(func.lower(last_name_start))
        )

    if subscribed is not None:
        query = query.where(models.Guest.subscribed == subscribed)

    return db.session.scalars(query).all()


def update(guest_id: UUID, guest_update: schemas.GuestUpdate) -> models.Guest:
    changes = guest_update.dict(exclude_unset=True)

    query = sql_update(models.Guest).where(models.Guest.id == guest_id).values(changes)
    db.session.execute(query)

    db.session.commit()
    return get(guest_id)


def delete(guest_id: UUID):
    db_guest = get(guest_id)
    db.session.delete(db_guest)

    db.session.commit()
