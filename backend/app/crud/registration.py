from uuid import UUID

from fastapi_sqlalchemy import db
from sqlalchemy import select
from sqlalchemy import update as sql_update

from app import models, schemas


def create(registration: schemas.RegistrationCreate) -> models.Registration:
    db_registration = models.Registration(
        guest_id=registration.guest_id,
        event_id=registration.event_id,
        buddy=registration.buddy,
        arrived=registration.arrived,
    )
    db.session.add(db_registration)

    db.session.commit()
    return db_registration


def create_on_site(
    registration_on_site: schemas.RegistrationOnSite,
) -> models.Registration:
    db_guest = models.Guest(
        first_name=registration_on_site.guest.first_name,
        last_name=registration_on_site.guest.last_name,
        email=registration_on_site.guest.email,
        subscribed=registration_on_site.guest.subscribed,
    )
    db.session.add(db_guest)
    db.session.flush()

    registration = schemas.RegistrationCreate(
        guest_id=db_guest.id,
        event_id=registration_on_site.event_id,
        buddy=registration_on_site.buddy,
        arrived=registration_on_site.arrived,
    )

    db.session.commit()
    return create(registration)


def get(registration_id: UUID) -> models.Registration | None:
    return db.session.get(models.Registration, registration_id)


def get_list(
    arrived: bool | None,
    buddy: str | None,
    guest_id: UUID | None,
    event_id: UUID | None,
) -> list[models.Registration]:
    query = select(models.Registration)

    if arrived is not None:
        query = query.where(models.Registration.arrived == arrived)

    if buddy is not None:
        query = query.where(models.Registration.buddy == buddy)

    if guest_id is not None:
        query = query.join(models.Registration.guest).where(models.Guest.id == guest_id)

    if event_id is not None:
        query = query.join(models.Registration.event).where(models.Event.id == event_id)

    return db.session.scalars(query).all()


def update(
    registration_id: UUID, registration_update: schemas.RegistrationUpdate
) -> models.Registration:
    changes = registration_update.dict()

    query = (
        sql_update(models.Registration)
        .where(models.Registration.id == registration_id)
        .values(changes)
    )
    db.session.execute(query)

    db.session.commit()
    return get(registration_id)


def delete(registration_id: UUID):
    db_registration = get(registration_id)
    db.session.delete(db_registration)

    db.session.commit()
