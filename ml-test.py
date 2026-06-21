import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')

print("Model and scalers loaded successfully!")

new_car_features = [
    0.0,  # Owner_Type (First=0, Second=1, Third=2, Fourth+=3 -> elegido First)
    0.0,  # Model_3 series
    0.0,  # Model_A4
    0.0,  # Model_Amaze
    0.0,  # Model_Bolero
    1.0,  # Model_C-class (Elegido)
    0.0,  # Model_Camry
    0.0,  # Model_Carens
    0.0,  # Model_City
    0.0,  # Model_Civic
    0.0,  # Model_Corolla
    0.0,  # Model_Creta
    0.0,  # Model_E-class
    0.0,  # Model_Ecosport
    0.0,  # Model_Endeavour
    0.0,  # Model_Figo
    0.0,  # Model_Gla
    0.0,  # Model_Harrier
    0.0,  # Model_I20
    0.0,  # Model_Kicks
    0.0,  # Model_Kushaq
    0.0,  # Model_Magnite
    0.0,  # Model_Nexon
    0.0,  # Model_Octavia
    0.0,  # Model_Polo
    0.0,  # Model_Punch
    0.0,  # Model_Q3
    0.0,  # Model_Q5
    0.0,  # Model_Scorpio
    0.0,  # Model_Seltos
    0.0,  # Model_Slavia
    0.0,  # Model_Sonet
    0.0,  # Model_Sunny
    0.0,  # Model_Taigun
    0.0,  # Model_Verna
    0.0,  # Model_Virtus
    0.0,  # Model_X1
    0.0,  # Model_X3
    0.0,  # Model_Xuv700
    0.0,  # Model_Yaris
    1.0,  # Transmission_Manual (1 = manual, 0 = automático)
    0.0,  # Fuel_Type_Cng
    1.0,  # Fuel_Type_Diesel (Elegido)
    0.0,  # Fuel_Type_Electric
    0.0,  # Fuel_Type_Hybrid
    0.0,  # Fuel_Type_Petrol
    2022, # Year
    2000, # Engine_CC
    194,  # Horsepower
    30000,# Kms_Driven
    0     # Accidents
]

# Convert to numpy array and reshape for the scaler
new_car_data = np.array(new_car_features).reshape(1, -1)

# Scale the new data using the pre-fitted scaler_X
new_car_scaled = scaler_X.transform(new_car_data)

# Make a prediction with the loaded model
predicted_price_scaled = model.predict(new_car_scaled)

# Inverse transform the predicted price to the original scale
predicted_price = scaler_y.inverse_transform(predicted_price_scaled.reshape(-1, 1))

print(f"Predicted price for the new car: ${predicted_price[0][0]:,.2f}")