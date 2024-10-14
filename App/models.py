from pydantic import BaseModel
from typing import List

class Schedule(BaseModel):
    transit_mode: str
    eta_origin: str
    eta_destination: str
