from datetime import date

from pydantic import BaseModel, ConfigDict


class BookingAddRequestDTO(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class BookingAddDTO(BaseModel):
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    price: int


class BookingDTO(BookingAddDTO):
    id: int

    model_config = ConfigDict(from_attributes=True)
