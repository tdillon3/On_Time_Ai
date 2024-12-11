# ON TIME AI - Flight Delay Prediction Tool

## Overview
This project leverages machine learning to predict flight delays based on real-time weather conditions and historical flight data. Designed for both passengers and airlines, the tool aims to provide insights into potential delays, enabling better planning and optimization in the aviation industry.

The dataset integrates information from public APIs:
- **OpenSky Network**: Provides real-time flight data.
- **OpenWeatherMap**: Supplies weather data for the departure location.

Users can input flight details, including flight number, weather conditions, and departure coordinates, into a web interface to receive predictions. By combining weather and flight data, this tool delivers insights into the likelihood of delays under various conditions.

---

## Features
- **Flight Number Integration**: Predict delays based on specific flights when data is available, or general conditions otherwise.
- **Real-time API Integration**: Pulls up-to-date flight and weather data from the OpenSky Network and OpenWeatherMap APIs.
- **Machine Learning Models**: Employs Random Forest and SVM models to predict delays with high accuracy.
- **Web Interface**: A simple, user-friendly interface built with Flask for easy data entry and prediction display.
- **Extreme Condition Handling**: Automatically flags extreme weather conditions to predict delays reliably.

---

## Software Demo Video
*(Include a link to your software demo video here if available.)*

---

## Data Analysis Insights
1. **Primary Factors Influencing Delays**:
   - Weather conditions, particularly wind speed, humidity, and extreme temperatures.
   - Flight congestion during peak hours and at major airports.

2. **Model Accuracy**:
   - The Random Forest model achieves high accuracy in predicting delays, with effective handling of normal scenarios and edge cases.

3. **Impact of Weather**:
   - Adverse weather conditions, including high wind speeds and extreme temperatures, significantly increase the likelihood of delays.

---

## Development Environment
### Tools and Frameworks
- **Visual Studio Code**: For development.
- **Flask**: To build the web interface.
- **Jupyter Notebook**: For data exploration and visualization.

### Languages and Libraries
- **Python**: Primary language for implementation.
- **Pandas**: Data manipulation and preprocessing.
- **Scikit-learn**: Machine learning model implementation.
- **Requests**: API interaction with OpenSky Network and OpenWeatherMap.
- **Joblib**: Model serialization and storage.

---

## Useful Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [OpenSky Network API Documentation](https://opensky-network.org/apidoc/)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)

---

## Future Work
- **Enhanced Dataset**: Include additional historical data and expand coverage to more airports worldwide.
- **Feature Expansion**: Integrate flight path data and real-time air traffic updates.
- **User Interface Enhancements**: Add interactive charts and data visualizations to explain predictions.
- **Model Optimization**: Explore advanced models like Gradient Boosting or Neural Networks for further accuracy.

---

## How to Run

### Prerequisites:
- **Python 3.x** installed.
- API credentials for **OpenSky Network** and **OpenWeatherMap**.

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url/flight-delay-prediction.git
2. Navigate to the project directory:
   ```bash
   cd flight-delay-prediction
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
4. Update your API keys in api_integrations.py:
   ```python
    OPENSKY_USERNAME = 'your_opensky_username'
	OPENSKY_PASSWORD = 'your_opensky_password'
	OPENWEATHER_API_KEY = 'your_openweathermap_api_key'
5. Run the Flask app:
   ```bash
	python app.py
6. Access the application at http://127.0.0.1:5000 in your browser.


## Authors
- **Tanner Dillon**: Project lead and developer.