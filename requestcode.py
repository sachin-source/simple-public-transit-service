import requests

def fetch_transit_schedules():
    url = "http://localhost:8000/api/schedules"
    payload = {
        "origin_station_id": "station_123",
        "coordinates": {
            "latitude": "40.712776",
            "longitude": "-74.005974"
        },
        "destination_station_id": "station_456"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Call the function
fetch_transit_schedules()
