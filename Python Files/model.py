import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
import joblib
import os

# Load the dataset
data = pd.read_csv('FertilizerPrediction.csv')

# Handle missing values using imputation
imputer = SimpleImputer(strategy='mean')
data[['Temparature', 'Humidity', 'Moisture', 'Nitrogen', 'Phosphorous', 'Potassium']] = imputer.fit_transform(
    data[['Temparature', 'Humidity', 'Moisture', 'Nitrogen', 'Phosphorous', 'Potassium']]
)

# Encode categorical columns 'Soil Type' and 'Crop Type' to numerical values
label_encoder_soil = LabelEncoder()
label_encoder_crop = LabelEncoder()

data['Soil Type'] = label_encoder_soil.fit_transform(data['Soil Type'])
data['Crop Type'] = label_encoder_crop.fit_transform(data['Crop Type'])

# Separate features and labels
X = data[['Temparature', 'Humidity', 'Moisture', 'Soil Type', 'Crop Type', 'Nitrogen', 'Phosphorous', 'Potassium']]
y_classification = data['Fertilizer Name']
y_regression = data['Moisture']

# Split the data for training and testing
X_train, X_test, y_train_class, y_test_class = train_test_split(X, y_classification, test_size=0.2, random_state=42)
_, _, y_train_reg, y_test_reg = train_test_split(X, y_regression, test_size=0.2, random_state=42)

# Train classification model
classification_model = RandomForestClassifier(n_estimators=100, random_state=42)
classification_model.fit(X_train, y_train_class)

# Train regression model
regression_model = RandomForestRegressor(n_estimators=100, random_state=42)
regression_model.fit(X_train, y_train_reg)

# Evaluate classification model
y_pred_class = classification_model.predict(X_test)
classification_accuracy = accuracy_score(y_test_class, y_pred_class)
print(f"Classification Model Accuracy: {classification_accuracy * 100:.2f}%")

# Print classification report
print("\nClassification Report:\n", classification_report(y_test_class, y_pred_class))

# Print confusion matrix
print("\nConfusion Matrix:\n", confusion_matrix(y_test_class, y_pred_class))

# Evaluate regression model
y_pred_reg = regression_model.predict(X_test)
regression_mse = mean_squared_error(y_test_reg, y_pred_reg)
print(f"Regression Model Mean Squared Error: {regression_mse:.2f}")

# Define file paths for saving models
classification_model_path = 'D:/Development of an AI based Fertilizer Prediction System/fertilizer_classification_model.pkl'
regression_model_path = 'D:/Development of an AI based Fertilizer Prediction System/fertilizer_regression_model.pkl'

# Save both models
joblib.dump(classification_model, classification_model_path)
joblib.dump(regression_model, regression_model_path)

# Check if files were saved successfully
if os.path.exists(classification_model_path) and os.path.exists(regression_model_path):
    print("Models trained, evaluated, and saved successfully.")
else:
    print("Error: Model files were not found after saving.")
