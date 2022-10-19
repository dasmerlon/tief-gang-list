from uuid import UUID

from fastapi_sqlalchemy import db

from app import models


def get(guest_id: UUID) -> models.Guest | None:
    return db.session.query(models.Guest).get(guest_id)
