import pandas as pd
from geopy.distance import geodesic
from sklearn.model_selection import train_test_split, GridSearchCV
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

# Define extreme value thresholds
EXTREME_TEMPERATURE = 45  # Celsius, upper bound
MINIMUM_TEMPERATURE = -30  # Celsius, lower bound
EXTREME_HUMIDITY = 90      # Percent
EXTREME_WIND_SPEED = 25     # m/s

# Label: create a binary target for flight delay (1 = delayed, 0 = on-time)
def delay_label(row):
    if (row['temperature'] >= EXTREME_TEMPERATURE or
        row['temperature'] <= MINIMUM_TEMPERATURE or
        row['humidity'] >= EXTREME_HUMIDITY or
        row['wind_speed'] >= EXTREME_WIND_SPEED):
        return 1
    return 1 if row['baro_altitude'] > 10000 else 0

merged_data['delayed'] = merged_data.apply(delay_label, axis=1)

# Save the merged data to a CSV file for future evaluation
merged_data.to_csv("merged_flight_weather_data.csv", index=False)
print("Merged data saved to merged_flight_weather_data.csv")

# Strictly define feature columns
feature_columns = ['temperature', 'humidity', 'wind_speed', 'latitude', 'longitude']
X = merged_data[feature_columns]  # Only use specified columns
y = merged_data['delayed']

# Split data into training and testing sets (80% train, 20% test)
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning for Random Forest
print("Tuning Random Forest model...")
rf_param_grid = {
    'n_estimators': [50, 100, 200],  # Number of trees in the forest
    'max_depth': [None, 10, 20, 30],  # Maximum depth of trees
    'min_samples_split': [2, 5, 10],  # Minimum number of samples to split
    'min_samples_leaf': [1, 2, 4]  # Minimum number of samples per leaf
}

rf_grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=rf_param_grid,
    scoring='accuracy',
    cv=5,  # 5-fold cross-validation
    n_jobs=-1
)

rf_grid_search.fit(X_train, y_train)
rf_best_model = rf_grid_search.best_estimator_
print(f"Best Random Forest parameters: {rf_grid_search.best_params_}")
print(f"Best Random Forest accuracy: {rf_grid_search.best_score_}")

# Hyperparameter tuning for SVM
print("Tuning SVM model...")
svm_param_grid = {
    'C': [0.1, 1, 10, 100],  # Regularization parameter
    'gamma': [1, 0.1, 0.01, 0.001],  # Kernel coefficient
    'kernel': ['rbf', 'linear']  # Type of kernel
}

svm_grid_search = GridSearchCV(
    estimator=SVC(),
    param_grid=svm_param_grid,
    scoring='accuracy',
    cv=5,  # 5-fold cross-validation
    n_jobs=-1
)

svm_grid_search.fit(X_train, y_train)
svm_best_model = svm_grid_search.best_estimator_
print(f"Best SVM parameters: {svm_grid_search.best_params_}")
print(f"Best SVM accuracy: {svm_grid_search.best_score_}")

# Save the tuned models to disk
print("Saving the tuned models...")
joblib.dump(rf_best_model, 'tuned_random_forest_model.pkl')
joblib.dump(svm_best_model, 'tuned_svm_model.pkl')

# Save the feature columns to a file for consistency in evaluation
with open("feature_columns.pkl", "wb") as f:
    joblib.dump(feature_columns, f)

print("Feature columns saved successfully.")

# Save X_train to CSV for consistent evaluation later
X_train.to_csv("X_train_features.csv", index=False)
print("X_train features saved to X_train_features.csv")
