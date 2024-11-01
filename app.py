from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model and feature columns
model = joblib.load("random_forest_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    wind_speed = float(request.form['wind_speed'])
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])

    # Extreme value thresholds
    EXTREME_TEMPERATURE = 45
    MINIMUM_TEMPERATURE = -30
    EXTREME_HUMIDITY = 90
    EXTREME_WIND_SPEED = 25

    # Check for extreme values to force a delay prediction
    if (temperature >= EXTREME_TEMPERATURE or
        temperature <= MINIMUM_TEMPERATURE or
        humidity >= EXTREME_HUMIDITY or
        wind_speed >= EXTREME_WIND_SPEED):
        prediction_text = "Flight Delay Prediction: Delayed"
    else:
        # Prediction with model if values are within normal range
        features = [[temperature, humidity, wind_speed, latitude, longitude]]
        prediction = model.predict(features)
        prediction_text = f"Flight Delay Prediction: {'Delayed' if prediction[0] == 1 else 'On Time'}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)