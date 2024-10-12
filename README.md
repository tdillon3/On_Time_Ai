# Flight Delay Prediction Tool

## Overview
As a software engineer focused on expanding my knowledge in machine learning and data analysis, this project aims to predict flight delays based on real-time weather conditions and historical flight data. With the increasing demand for accurate scheduling and planning in the aviation industry, understanding potential flight delays can greatly benefit passengers, airlines, and airport operations.

The dataset used for this analysis is gathered from public APIs, including the **OpenSky Network** (for flight data) and **OpenWeatherMap** (for weather conditions). The data includes key features like flight schedule, airline, airport details, weather parameters (e.g., temperature, wind speed), and historical delay patterns. By leveraging machine learning algorithms, this tool seeks to provide accurate predictions of flight delays based on various external factors.

The primary goal of this software is to enable users to input relevant flight and weather data, and receive a prediction on whether their flight is likely to be delayed. This tool can assist both passengers in planning and airlines in optimizing their operations.

---

## Software Demo Video
*(Include a link to your software demo video here if available.)*

---

## Data Analysis Results
This project aimed to answer key questions about flight delay predictions using machine learning. Here are the key insights:

1. **What are the primary factors influencing flight delays?**

   **Answer**: The analysis revealed that weather conditions, including wind speed and precipitation, play a significant role in determining whether a flight is delayed. Additionally, flights scheduled during peak travel hours and flights departing from major airports are more prone to delays due to congestion.

2. **How accurate are the flight delay predictions?**

   **Answer**: Using machine learning models like Random Forest, the model achieved reasonable accuracy in predicting flight delays. While the model performed well in general scenarios, unexpected events (such as sudden weather changes or technical issues) still posed challenges for precise predictions.

3. **How does weather affect the likelihood of delays?**

   **Answer**: The machine learning model identified weather parameters, such as wind speed and temperature, as key indicators of potential delays. The model suggests that flights departing under adverse weather conditions have a higher likelihood of experiencing delays, particularly at busy airports with a high volume of traffic.

---

## Development Environment
**Tools**:  
The software was developed using **Visual Studio Community** for the backend and data processing, and **Flask** for a simple web-based user interface.

**Languages and Libraries**:  
The project was implemented in Python, utilizing the following libraries:
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For machine learning model implementation.
- **Requests**: For making API calls to the OpenSky Network and OpenWeatherMap.
- **Flask**: To build the web interface for user interaction.

---

## Useful Websites
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn: Machine Learning in Python](https://scikit-learn.org/stable/)
- [OpenSky Network API Documentation](https://opensky-network.org/apidoc/)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)

---

## Future Work
- **Data Expansion**: Expand the dataset by including more historical flight and weather data from different regions and airports to improve model accuracy and robustness.
- **Feature Enhancement**: Introduce additional features such as flight path data, real-time congestion levels, and air traffic control logs to provide a more comprehensive prediction model.
- **User Interface Improvement**: Further develop the user interface to make it more user-friendly. Implement visualizations for users to easily understand the factors contributing to the prediction.
- **Model Enhancement**: Explore more advanced machine learning models like Gradient Boosting or Neural Networks to improve prediction accuracy, especially in edge cases.

---

## How to Run

### Prerequisites:
- **Python 3.x** installed on your system.
- API keys for **OpenSky Network** and **OpenWeatherMap**.
  
### Steps:
1. Clone the repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt