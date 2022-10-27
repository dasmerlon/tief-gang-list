from uuid import UUID

from fastapi_sqlalchemy import db

from app import models, schemas


def create(registration: schemas.RegistrationCreate) -> models.Registration:
    db_registration = models.Registration(
        guest_id=registration.guest_id,
        event_id=registration.event_id,
        arrived=registration.arrived,
    )

    db.session.add(db_registration)
    db.session.commit()
    return db_registration


def get(registration_id: UUID) -> models.Registration | None:
    return db.session.query(models.Registration).get(registration_id)


def get_list(arrived: bool | None) -> list[models.Registration]:
    query = db.session.query(models.Registration)

    if arrived is not None:
        query = query.filter(models.Registration.arrived == arrived)

    return query.all()


def update(
    registration_id: UUID, registration_update: schemas.RegistrationUpdate
) -> models.Registration:
    changes = registration_update.dict(exclude_unset=True)
    db.session.query(models.Registration).filter(
        models.Registration.id == registration_id
    ).update(changes)

    db.session.commit()
    return get(registration_id)


def delete(registration_id: UUID):
    db_registration = get(registration_id)
    db.session.delete(db_registration)
    db.session.commit()
