from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequestAddDTO(BaseModel):
    email: EmailStr
    password: str


class UserAddDTO(BaseModel):
    email: EmailStr
    hashed_password: str


class UserDTO(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserWithHashedPassword(UserDTO):
    hashed_password: str
