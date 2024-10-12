from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("flight_delay_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    wind_speed = float(request.form['wind_speed'])
    
    # Prediction
    features = [[temperature, humidity, wind_speed]]
    prediction = model.predict(features)
    
    return render_template('index.html', prediction_text=f'Flight Delay Prediction: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)