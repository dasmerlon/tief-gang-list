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


def get(registration_id: UUID) -> models.Registration | None:
    return db.session.get(models.Registration, registration_id)


def get_list(arrived: bool | None) -> list[models.Registration]:
    query = select(models.Registration)

    if arrived is not None:
        query = query.where(models.Registration.arrived == arrived)

    return db.session.scalars(query).all()


def update(
    registration_id: UUID, registration_update: schemas.RegistrationUpdate
) -> models.Registration:
    changes = registration_update.dict(exclude_unset=True)

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
