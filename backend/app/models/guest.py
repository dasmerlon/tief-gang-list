from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, String, func
from sqlalchemy.orm import relationship

from app.db import Base


class Guest(Base):
    __tablename__ = "guest"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    first_name = Column(String)
    last_name = Column(String)
    buddy = Column(String)
    email = Column(String)
    subscribed = Column(Boolean)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    registrations = relationship("Registration", back_populates="guest")

    def __repr__(self):
        return (
            f"Guest(id={self.id!r}, "
            f"first_name={self.first_name!r}, "
            f"last_name={self.last_name!r}), "
            f"buddy={self.buddy!r}), "
            f"email={self.email!r}), "
            f"subscribed={self.subscribed!r}), "
        )
