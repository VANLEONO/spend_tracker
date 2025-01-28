import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel, Column, String, Computed 

class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    login: str = Field(default=None, max_length=20)
    is_active: bool = True
    is_superuser: bool = False
    first_name: str | None = Field(default=None, max_length=255)
    second_name: str | None = Field(default=None, max_length=255)
    @property
    def full_name(self) -> str | None:
        if self.first_name and self.second_name:
            return f'{self.first_name} {self.second_name}'

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)

class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)
    login: str | None = Field(default=None, max_length=20)
    password: str | None = Field(default=None, min_length=8, max_length=40)

class UserPublic(UserBase):
    id: uuid.UUID
    email: EmailStr
    login: str
    is_superuser: bool
    is_active: bool
    full_name: str