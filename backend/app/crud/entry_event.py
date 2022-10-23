from fastapi_sqlalchemy import db

from app import models, schemas


def create(entry_event: schemas.EntryEventCreate) -> int:
    db_entry_event = models.EntryEvent(
        count_type=entry_event.count_type, event_id=entry_event.event_id
    )
    db.session.add(db_entry_event)
    db.session.commit()
    # TODO: retrun guests-on-site
    return 0
