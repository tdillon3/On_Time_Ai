import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the datasets
flight_data = pd.read_csv("flight_data.csv")
weather_data = pd.read_csv("weather_data.csv")

# Preprocess the flight data
def preprocess_flight_data(flight_data):
    # Remove unnecessary columns
    flight_data_clean = flight_data.drop(columns=['icao24', 'origin_country', 'squawk', 'spi'])
    
    # Handle missing values (drop rows with missing critical data)
    flight_data_clean = flight_data_clean.dropna(subset=['longitude', 'latitude', 'baro_altitude'])
    
    return flight_data_clean

# Preprocess the weather data
def preprocess_weather_data(weather_data):
    weather_data_clean = weather_data.dropna()
    
    # Normalize temperature, humidity, and wind speed
    scaler = StandardScaler()
    weather_data_clean[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(
        weather_data_clean[['temperature', 'humidity', 'wind_speed']])
    
    return weather_data_clean

# Example preprocessing steps
flight_data_clean = preprocess_flight_data(flight_data)
weather_data_clean = preprocess_weather_data(weather_data)

# Save cleaned data
flight_data_clean.to_csv("flight_data_clean.csv", index=False)
weather_data_clean.to_csv("weather_data_clean.csv", index=False)