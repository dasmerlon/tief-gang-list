from uuid import UUID

from fastapi_sqlalchemy import db

from app import models


def get(guest_id: UUID) -> models.Guest | None:
    return db.session.query(models.Guest).get(guest_id)


def delete(guest_id: UUID):
    db_guest = get(guest_id)
    db.session.delete(db_guest)
    db.session.commit()
