import pandas as pd
from geopy.distance import geodesic
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Load flight and weather data
flight_data = pd.read_csv("flight_data.csv")
weather_data = pd.read_csv("weather_data.csv")

# Manually add latitude and longitude for the cities in the weather data
city_coordinates = {
    'New York': (40.7128, -74.0060),
    'Los Angeles': (34.0522, -118.2437),
    'Chicago': (41.8781, -87.6298),
    'Houston': (29.7604, -95.3698),
    'Phoenix': (33.4484, -112.0740),
    # Add more cities as needed...
}

# Add latitude and longitude columns to the weather data
weather_data['latitude'] = weather_data['city'].map(lambda city: city_coordinates.get(city, (None, None))[0])
weather_data['longitude'] = weather_data['city'].map(lambda city: city_coordinates.get(city, (None, None))[1])

# Remove rows where latitude or longitude is missing (NaN)
weather_data = weather_data.dropna(subset=['latitude', 'longitude'])
flight_data = flight_data.dropna(subset=['latitude', 'longitude'])

# Function to calculate the distance between two sets of lat/lon coordinates
def calculate_distance(flight_row, weather_row):
    flight_coords = (flight_row['latitude'], flight_row['longitude'])
    weather_coords = (weather_row['latitude'], weather_row['longitude'])
    return geodesic(flight_coords, weather_coords).km  # Calculate the distance in kilometers

# Find the closest weather station for each flight
def find_closest_weather_station(flight_row, weather_data):
    weather_data['distance'] = weather_data.apply(lambda weather_row: calculate_distance(flight_row, weather_row), axis=1)
    closest_station = weather_data.loc[weather_data['distance'].idxmin()]  # Get the closest station
    return closest_station

# Apply the proximity matching for each flight to find the closest weather station
print("Matching flights with the closest weather stations based on proximity...")
matched_weather = flight_data.apply(lambda flight_row: find_closest_weather_station(flight_row, weather_data), axis=1)

# Concatenate the weather data to flight data
merged_data = pd.concat([flight_data.reset_index(drop=True), matched_weather.reset_index(drop=True)], axis=1)

# Label: create a binary target for flight delay (1 = delayed, 0 = on-time)
merged_data['delayed'] = merged_data['baro_altitude'].apply(lambda x: 1 if x > 10000 else 0)

# Features (input data) and target variable
X = merged_data[['temperature', 'humidity', 'wind_speed', 'latitude', 'longitude']]  # Features
y = merged_data['delayed']  # Target

# Split data into training and testing sets (80% train, 20% test)
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
print("Training Random Forest model...")
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Predictions and accuracy for Random Forest
y_pred_rf = rf_model.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf)}")

# Train an SVM model
print("Training SVM model...")
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Predictions and accuracy for SVM
y_pred_svm = svm_model.predict(X_test)
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred_svm)}")

# Save the trained models to disk
print("Saving the trained models...")
joblib.dump(rf_model, 'random_forest_model.pkl')
joblib.dump(svm_model, 'svm_model.pkl')

print("Models have been trained and saved successfully.")