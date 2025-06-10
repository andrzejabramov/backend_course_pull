from src.models.bookings import BookingsOrm
from src.models.facilities import FacilitiesOrm, RoomsFacilitiesOrm
from src.models.hotels import HotelsOrm
from src.models.rooms import RoomsOrm
from src.models.users import UsersOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.bookings import BookingDTO
from src.schemas.facilities import FacilityDTO, RoomFacilityDTO
from src.schemas.hotels import HotelDTO
from src.schemas.rooms import RoomDTO, RoomWithRelsDTO
from src.schemas.users import UserDTO


class HotelDataMapper(DataMapper):
    db_model = HotelsOrm
    schema = HotelDTO


class RoomDataMapper(DataMapper):
    db_model = RoomsOrm
    schema = RoomDTO


class RoomDataWithRelsMapper(DataMapper):
    db_model = RoomsOrm
    schema = RoomWithRelsDTO


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserDTO


class BookingDataMapper(DataMapper):
    db_model = BookingsOrm
    schema = BookingDTO


class FacilityDataMapper(DataMapper):
    db_model = FacilitiesOrm
    schema = FacilityDTO


class RoomFacilityDataMapper(DataMapper):
    db_model = RoomsFacilitiesOrm
    schema = RoomFacilityDTO
