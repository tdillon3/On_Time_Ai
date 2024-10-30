import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the test dataset
merged_data = pd.read_csv("merged_flight_weather_data.csv")

# Remove duplicate columns by renaming and then selecting only unique columns
merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

# Explicitly drop any unintended duplicate columns if they still exist
columns_to_drop = ['latitude.1', 'longitude.1']
merged_data = merged_data.drop(columns=[col for col in columns_to_drop if col in merged_data.columns])

# Load the saved feature set to ensure consistent structure
X_train_features = pd.read_csv("X_train_features.csv")  # Load exact feature structure from training
X_test = merged_data[X_train_features.columns]  # Use only these columns in the test set
y_test = merged_data['delayed']  # Load labels

# Load the trained models
rf_model = joblib.load("random_forest_model.pkl")
svm_model = joblib.load("svm_model.pkl")

# Evaluate Random Forest model
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
print("Random Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Evaluate SVM model
y_pred_svm = svm_model.predict(X_test)
print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))