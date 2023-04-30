from pydantic import UUID4, BaseModel, EmailStr, validator

from app.helpers.validators import check_string_not_empty


class GuestBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr | None = None
    subscribed: bool = False

    _not_empty = validator("first_name", "last_name", allow_reuse=True)(
        check_string_not_empty
    )


class GuestCreate(GuestBase):
    pass


class GuestUpdate(GuestBase):
    pass


class Guest(GuestBase):
    id: UUID4

    class Config:
        orm_mode = True
