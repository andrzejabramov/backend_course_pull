from src.schemas.hotels import HotelAddDTO
from src.utils.db_manager import DBManager


async def test_add_hotel(db: DBManager):
    hotel_data = HotelAddDTO(title="Hotel 5 stars", location="Сочи")
    await db.hotels.add(hotel_data)
    await db.commit()
