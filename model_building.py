import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load cleaned datasets
flight_data_clean = pd.read_csv("flight_data_clean.csv")
weather_data_clean = pd.read_csv("weather_data_clean.csv")

# Merge flight and weather data
merged_data = pd.merge(flight_data_clean, weather_data_clean, left_on="latitude", right_on="city", how="left")

# Label: create a binary target for flight delay (1 = delayed, 0 = on-time)
merged_data['delayed'] = merged_data['baro_altitude'].apply(lambda x: 1 if x > 10000 else 0)

# Features and target variable
X = merged_data[['temperature', 'humidity', 'wind_speed', 'latitude', 'longitude']]
y = merged_data['delayed']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions and accuracy
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")