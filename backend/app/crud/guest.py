from uuid import UUID

from fastapi_sqlalchemy import db

from app.models.guest import Guest


def get(guest_id: UUID) -> Guest | None:
    return db.session.query(Guest).get(str(guest_id))
