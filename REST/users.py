from datetime import datetime

from pydantic import BaseModel, constr, EmailStr


class SUser(BaseModel):
    email: EmailStr


class SUserSignUp(SUser):
    role: str
    first_name: str
    last_name: str
    age: int
    password: constr(min_length=8, max_length=24)


class SUserEdit(SUser):
    role: str
    first_name: str
    last_name: str
    age: int


class SUserLogin(SUser):
    password: constr(min_length=8, max_length=24)


class Simple(BaseModel):
    role: str
    first_name: str | None
    email: EmailStr | None
    salary: float | None
    job_title: str | None
    date_promotion: datetime | None


class SOkResponse(BaseModel):
    status: str = 'success'
    data: dict = {'ok': True}
    details: str | None = None