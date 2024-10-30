from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest model and feature columns
model = joblib.load("random_forest_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        wind_speed = float(request.form['wind_speed'])
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])

        # Arrange the input features in the correct order
        features = np.array([[temperature, humidity, wind_speed, latitude, longitude]])

        # Prediction using the loaded Random Forest model
        prediction = model.predict(features)

        # Interpret the prediction
        prediction_text = 'Flight is likely to be delayed' if prediction[0] == 1 else 'Flight is likely to be on-time'
        
    except Exception as e:
        prediction_text = f"Error making prediction: {e}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)