# Transit Schedule API

This is a FastAPI application that provides a RESTful API for fetching upcoming public transit schedules based on the user's location. The API finds the closest transit station to the user's coordinates and retrieves the schedules for the desired destination station.

## Features

- **Find Closest Station**: Automatically identifies the nearest transit station based on provided coordinates.
- **Fetch Schedules**: Returns upcoming transit schedules from the closest station to the specified destination station.

## Requirements

- Python 3.7+
- Python libraries are mentioned in requirements.txt file 

## Installation

1. **Clone the repository** :

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages** :
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application** :
    ```bash
    python App/main.py
    ```
    This command will start the server and allow you to access the API at http://127.0.0.1:8000/api/schedules  


4. **Test the API** :
    ```bash
    python requestcode.py
    ```  
