from datetime import date, datetime, time

from dateutil.relativedelta import relativedelta
from dateutil.rrule import MONTHLY, SA, rrule
from faker import Faker
from sqlalchemy.orm import Session

from app import models
from app.db import engine as db_engine


def seed_db():
    """Fill the database with seed data.

    Use this function to fill an empty database with seed data.
    This is useful to get some stub data for testing in the dev environment
    """
    Faker.seed(0)
    fake = Faker()

    # We have to do our own session logic, as we're not in the context of
    # a FastAPI request
    session = Session(db_engine)

    event_names = [
        "Technotanker",
        "Technotanker #2",
        "Deepstate",
        "Psynauten",
        "Drumroll",
    ]
    event_names.reverse()

    # We make one event each month
    # Compute the dates for past events
    today = date.today()
    months_ago = today - relativedelta(months=len(event_names))
    dates = list(
        rrule(MONTHLY, count=len(event_names), byweekday=SA(1), dtstart=months_ago)
    )

    # Create a few events
    for event_name, event_date in zip(event_names, dates):
        event = models.Event(
            name=event_name,
            date=event_date,
            registration_deadline=datetime.combine(event_date, time(hour=18)),
        )

        session.add(event)
        session.flush()

    session.commit()
