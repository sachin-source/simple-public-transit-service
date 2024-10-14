from models import Schedule

async def get_next_schedules(origin_station_id: str, destination_station_id: str) -> List[Schedule]:
    # This is a temporary code
    # The actual code to find the schedules based on origin_station_id, destination_station_id goes here
    # Submitting the Dummy response now
    return [
        Schedule(transit_mode="rail", eta_origin="2023-10-14 16:19:09", eta_destination="2023-10-14 17:19:09"),
        Schedule(transit_mode="bus", eta_origin="2023-10-14 16:30:09", eta_destination="2023-10-14 17:00:09"),
    ]

async def get_closest_station(coordinates) -> str:
    # This code to be replaced with a logic to find closest station
    return "station_123"
