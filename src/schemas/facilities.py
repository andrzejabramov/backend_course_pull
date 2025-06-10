from pydantic import BaseModel, ConfigDict


class FacilityAddDTO(BaseModel):
    title: str


class FacilityDTO(FacilityAddDTO):
    id: int

    model_config = ConfigDict(from_attributes=True)


class RoomFacilityAddDTO(BaseModel):
    room_id: int
    facility_id: int


class RoomFacilityDTO(RoomFacilityAddDTO):
    id: int
