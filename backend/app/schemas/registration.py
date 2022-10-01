from pydantic import UUID4, BaseModel, EmailStr
from datetime import datetime

from app.schemas.guest import Guest
from app.schemas.event import Event


class RegistrationBase(BaseModel):
    pass

class RegistrationCreate(RegistrationBase):
    guest_id: UUID4
    event_id: UUID4

class Registration(RegistrationBase):
    id: UUID4
    created_at: datetime
    guest: Guest
    event: Event
    
