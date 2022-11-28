from pydantic import UUID4, BaseModel, EmailStr


class GuestBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    # TODO: Move the buddy field to the registration entity
    # Buddies can differ between parties
    buddy: str | None = None
    email: EmailStr | None = None
    subscribed: bool | None = None


class GuestCreate(GuestBase):
    pass


class GuestUpdate(GuestBase):
    pass


class Guest(GuestBase):
    id: UUID4

    class Config:
        orm_mode = True
