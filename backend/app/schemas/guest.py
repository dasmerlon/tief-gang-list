from pydantic import UUID4, BaseModel, EmailStr


class GuestBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr | None = None
    subscribed: bool = False


class GuestCreate(GuestBase):
    pass


class GuestUpdate(GuestBase):
    pass


class Guest(GuestBase):
    id: UUID4

    class Config:
        orm_mode = True
