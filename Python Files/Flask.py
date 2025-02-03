from flask import Flask, request, jsonify
import joblib
import requests

app = Flask(__name__)

# Load the trained classification and regression models
classification_model = joblib.load('fertilizer_classification_model.pkl')
regression_model = joblib.load('fertilizer_regression_model.pkl')

# URL of your Spring Boot API (make sure it's running and accessible)
spring_boot_url = 'http://localhost:8078/fertilizer/predict'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure all required fields are present
    required_keys = ['Temperature', 'Humidity', 'Moisture', 'Soil Type', 'Crop Type', 'Nitrogen', 'Phosphorous', 'Potassium']
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing parameters"}), 400

    # Extract features in the order required by the model
    features = [[
        data['Temperature'], data['Humidity'], data['Moisture'],
        data['Soil Type'], data['Crop Type'], data['Nitrogen'],
        data['Phosphorous'], data['Potassium']
    ]]

    # Use the classification model to predict the fertilizer type
    fertilizer_prediction = classification_model.predict(features)[0]

    # Use the regression model to predict moisture or any other numeric target
    moisture_prediction = regression_model.predict(features)[0]

    # Prepare the data to send to the Spring Boot app
    data_to_send = {
        "Temperature": data['Temperature'],
        "Humidity": data['Humidity'],
        "Moisture": data['Moisture'],
        "Soil Type": data['Soil Type'],
        "Crop Type": data['Crop Type'],
        "Nitrogen": data['Nitrogen'],
        "Phosphorous": data['Phosphorous'],
        "Potassium": data['Potassium'],
        "FertilizerRecommendation": fertilizer_prediction,
        "MoisturePrediction": moisture_prediction
    }

    # Send the prediction data to Spring Boot app
    response = requests.post(spring_boot_url, json=data_to_send)

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify({
            "fertilizer_recommendation": fertilizer_prediction,
            "moisture_prediction": moisture_prediction
        })
    else:
        return jsonify({"error": "Failed to send data to Spring Boot app"}), 500

if __name__ == '__main__':
    app.run(debug=True)
