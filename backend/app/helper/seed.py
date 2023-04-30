import random
from datetime import date, datetime, time

from dateutil.relativedelta import relativedelta
from dateutil.rrule import MONTHLY, SA, rrule
from faker import Faker
from sqlalchemy.orm import Session

from app import models, schemas
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

    # Create a few random guests
    guests = create_guests(session, fake)

    # Create a few events
    for event_name, event_date in zip(event_names, dates):
        event = models.Event(
            name=event_name,
            date=event_date,
            registration_deadline=datetime.combine(event_date, time(hour=18)),
        )

        session.add(event)
        session.flush()
        # Create some registrations and entry events for this event
        entities_for_event_and_guests(session, fake, event, guests)

    session.commit()


def create_guests(session: Session, fake: Faker) -> list[models.Guest]:
    """Create a list of random guests."""
    guests = []

    for _ in range(10):
        guest = models.Guest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            buddy="crew",
            email=fake.ascii_free_email(),
            subscribed=fake.boolean(),
        )

        session.add(guest)
        session.flush()
        guests.append(guest)

    return guests


def entities_for_event_and_guests(
    session: Session, fake: Faker, event: models.Event, guests: list[models.Guest]
) -> list[models.Guest]:
    """Create Registration and EntryEvent entities.

    This function selects a few guests from the list and creates registrations
    and EntryEvents for these guests for the given event
    """

    # Select a random set of variable size from our guest list
    selected_guests = random.sample(guests, random.randint(1, len(guests)))

    for guest in selected_guests:
        # Register the guest for the event
        registration = models.Registration(
            guest_id=guest.id, event_id=event.id, arrived=True
        )
        session.add(registration)

        # The guest showed up to the event
        entry_event = models.EntryEvent(
            event_id=event.id,
            event_type=schemas.EntryEventType.arrival,
        )
        session.add(entry_event)

        # 50/50 chance that the guest was registered when they left
        if fake.boolean():
            entry_event = models.EntryEvent(
                event_id=event.id,
                event_type=schemas.EntryEventType.departure,
            )
            session.add(entry_event)

    session.flush()

    return guests
