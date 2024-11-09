from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
