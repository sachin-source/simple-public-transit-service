from pydantic import BaseModel
from typing import List

class Schedule(BaseModel):
    transit_mode: str
    eta_origin: str
    eta_destination: str


class Coordinates(BaseModel):
    latitude: str
    longitude: str

class TransitRequest(BaseModel):
    origin_station_id: str
    coordinates: Coordinates
    destination_station_id: str

class TransitResponse(BaseModel):
    next_schedules: List[Schedule]
