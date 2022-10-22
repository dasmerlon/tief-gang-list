from sqlalchemy import Boolean, Column, DateTime, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db import Base


class Guest(Base):
    __tablename__ = "guest"

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
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
            f"Guest(id={self.id}, "
            f"first_name={self.first_name}, "
            f"last_name={self.last_name}), "
            f"buddy={self.buddy}), "
            f"email={self.email}), "
            f"subscribed={self.subscribed}), "
        )
