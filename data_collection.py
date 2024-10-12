import pandas as pd
from api_integration import fetch_flight_data, fetch_weather_data

# Function to collect and save flight data
def collect_flight_data(output_file="flight_data.csv"):
    flight_data = fetch_flight_data()
    if flight_data is not None:
        flight_data.to_csv(output_file, index=False)
        print(f"Flight data saved to {output_file}")

# Function to collect and save weather data for multiple cities
def collect_weather_data(cities, output_file="weather_data.csv"):
    weather_list = []
    for city in cities:
        weather = fetch_weather_data(city)
        if weather is not None:
            weather['city'] = city
            weather_list.append(weather)
    weather_df = pd.DataFrame(weather_list)
    weather_df.to_csv(output_file, index=False)
    print(f"Weather data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    collect_flight_data()
    collect_weather_data(cities=['New York', 'Los Angeles', 'Chicago'])