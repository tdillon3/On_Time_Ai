import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

# Load the test dataset
merged_data = pd.read_csv("merged_flight_weather_data.csv")

# Remove any duplicate columns that may have appeared due to merging
merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

# Drop specific duplicate columns if they still exist
columns_to_drop = ['latitude.1', 'longitude.1']
for col in columns_to_drop:
    if col in merged_data.columns:
        merged_data = merged_data.drop(columns=[col])

# Load the feature columns used during training
with open("feature_columns.pkl", "rb") as f:
    feature_columns = joblib.load(f)

# Load the Random Forest model to inspect its feature expectations
rf_model = joblib.load("random_forest_model.pkl")
expected_features = rf_model.feature_names_in_ if hasattr(rf_model, 'feature_names_in_') else feature_columns
print("Expected feature columns by the model:", expected_features)

# Ensure X_test contains only the expected features in the correct order
X_test = merged_data[[col for col in expected_features if col in merged_data.columns]]
X_test = X_test.reindex(columns=expected_features)  # Enforce column order
y_test = merged_data['delayed']  # Load labels

# Verify that X_test matches the model's expected features exactly
print("Final Testing feature columns:", list(X_test.columns))

# Proceed to evaluate the model if everything is aligned
# Evaluate Random Forest model
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
print("Random Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Load and evaluate the SVM model if necessary
svm_model = joblib.load("svm_model.pkl")
y_pred_svm = svm_model.predict(X_test)
print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))
print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))
