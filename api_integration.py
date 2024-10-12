
import requests
import pandas as pd

# OpenSky API credentials
OPENSKY_USERNAME = 'your_opensky_username'
OPENSKY_PASSWORD = 'your_opensky_password'

# OpenWeatherMap API key
OPENWEATHER_API_KEY = 'your_openweather_api_key'

# Function to fetch flight data from OpenSky API
def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url, auth=(OPENSKY_USERNAME, OPENSKY_PASSWORD))
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data['states'], columns=[
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 
            'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'heading',
            'vertical_rate', 'geo_altitude', 'squawk', 'spi', 'position_source'
        ])
    else:
        print("Failed to fetch flight data")
        return None

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city='New York'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'weather_desc': data['weather'][0]['description']
        }
    else:
        print("Failed to fetch weather data")
        return None

# Example of fetching data
if __name__ == "__main__":
    flight_data = fetch_flight_data()
    weather_data = fetch_weather_data()
    print(flight_data.head())
    print(weather_data)