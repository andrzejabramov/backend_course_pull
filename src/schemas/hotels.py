from pydantic import BaseModel


class HotelAddDTO(BaseModel):
    title: str
    location: str


class HotelDTO(HotelAddDTO):
    id: int


class HotelPatchDTO(BaseModel):
    title: str | None = None
    location: str | None = None
