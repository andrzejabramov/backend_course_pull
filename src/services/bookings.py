from src.exceptions import ObjectNotFoundException, RoomNotFoundException
from src.schemas.bookings import BookingAddRequestDTO, BookingAddDTO
from src.schemas.hotels import HotelDTO
from src.schemas.rooms import RoomDTO
from src.services.base import BaseService


class BookingService(BaseService):
    async def add_booking(self, user_id: int, booking_data: BookingAddRequestDTO):
        try:
            room: RoomDTO = await self.db.rooms.get_one(id=booking_data.room_id)
        except ObjectNotFoundException as ex:
            raise RoomNotFoundException from ex
        hotel: HotelDTO = await self.db.hotels.get_one(id=room.hotel_id)
        room_price: int = room.price
        _booking_data = BookingAddDTO(
            user_id=user_id,
            price=room_price,
            **booking_data.dict(),
        )
        booking = await self.db.bookings.add_booking(_booking_data, hotel_id=hotel.id)
        await self.db.commit()
        return booking

    async def get_bookings(self):
        return await self.db.bookings.get_all()

    async def get_my_bookings(self, user_id: int):
        return await self.db.bookings.get_filtered(user_id=user_id)
