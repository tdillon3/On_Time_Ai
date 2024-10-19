import pandas as pd
from api_integration import fetch_flight_data, fetch_weather_data

# Function to collect and save flight data
def collect_flight_data(output_file="flight_data.csv"):
    flight_data = fetch_flight_data()
    if flight_data is not None:
        flight_data.to_csv(output_file, index=False)
        print(f"Flight data saved to {output_file}")

# Function to collect and save weather data for multiple cities with lat/lon
def collect_weather_data(cities_with_coords, output_file="weather_data.csv"):
    weather_list = []
    for city, lat, lon in cities_with_coords:  # Now using the correct variable
        weather = fetch_weather_data(lat, lon)  # Pass lat/lon, not city name
        if weather is not None:
            weather['city'] = city  # Add city name to the weather data
            weather_list.append(weather)
    weather_df = pd.DataFrame(weather_list)
    weather_df.to_csv(output_file, index=False)
    print(f"Weather data saved to {output_file}")

# Example usage with city coordinates
if __name__ == "__main__":
    collect_flight_data()
    
    # Add latitude and longitude for each city
    cities_with_coords = [
        ('New York', 40.7128, -74.0060),
        ('Los Angeles', 34.0522, -118.2437),
        ('Chicago', 41.8781, -87.6298)
    ]
    
    # Call the function with cities_with_coords instead of just cities
    collect_weather_data(cities_with_coords)