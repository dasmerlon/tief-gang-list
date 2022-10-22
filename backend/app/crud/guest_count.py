from fastapi_sqlalchemy import db

from app import models, schemas


def create(guest_count: schemas.GuestCountCreate) -> int:
    db_guest_count = models.GuestCount(
        count_type=guest_count.count_type, event_id=guest_count.event_id
    )
    db.session.add(db_guest_count)
    db.session.commit()
    # TODO: retrun guests-on-site
    return 0
