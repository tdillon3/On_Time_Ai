
import requests
import pandas as pd

# OpenSky API credentials
OPENSKY_USERNAME = 'tdillon3'
OPENSKY_PASSWORD = 'asdf'

# OpenWeatherMap API key
OPENWEATHER_API_KEY = 'fc1c5b3534ac2d13562d100cecc43538'

# Function to fetch flight data from OpenSky API
def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url, auth=(OPENSKY_USERNAME, OPENSKY_PASSWORD))
    
    if response.status_code == 200:
        data = response.json()
        
        # Print the number of columns and an example of the first row to inspect the data structure
        print(f"Number of columns returned: {len(data['states'][0])}")
        print(f"First row of data: {data['states'][0]}")
        
        # Now construct the DataFrame dynamically based on what is returned
        columns = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 
            'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'heading',
            'vertical_rate', 'geo_altitude', 'squawk', 'spi', 'position_source'
        ]
        
        # If the returned data has more columns than expected, capture that as well
        if len(data['states'][0]) > len(columns):
            # Dynamically create column names for any extra data
            extra_cols = [f"extra_col_{i}" for i in range(len(data['states'][0]) - len(columns))]
            columns.extend(extra_cols)
        
        return pd.DataFrame(data['states'], columns=columns)
    else:
        print("Failed to fetch flight data")
        return None

# Example of fetching data
if __name__ == "__main__":
    flight_data = fetch_flight_data()
    print(flight_data.head())