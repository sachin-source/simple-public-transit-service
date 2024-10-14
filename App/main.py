from fastapi import FastAPI, HTTPException
from services import get_next_schedules, get_closest_station
from models import TransitRequest, TransitResponse
app = FastAPI()

@app.post("/api/schedules", response_model=TransitResponse)
async def fetch_transit_schedules(request: TransitRequest):
    try:    
        closest_station = await get_closest_station(request.coordinates)

        if closest_station is None:
            raise HTTPException(status_code=404, detail="No nearby station found.")
        
        schedules = await get_next_schedules(
            origin_station_id=closest_station,
            destination_station_id=request.destination_station_id
        )
        
        return TransitResponse(next_schedules=schedules)
    except:
        print("Something went wrong")
        return HTTPException(status_code=500, detail="Something went wrong at server, please try again!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
