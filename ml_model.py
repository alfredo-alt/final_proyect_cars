import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')

# Modelos disponibles en el mismo orden que las columnas Model_* del entrenamiento
MODELS = [
    "3 series", "A4", "Amaze", "Bolero", "C-class", "Camry", "Carens", "City",
    "Civic", "Corolla", "Creta", "E-class", "Ecosport", "Endeavour", "Figo",
    "Gla", "Harrier", "I20", "Kicks", "Kushaq", "Magnite", "Nexon", "Octavia",
    "Polo", "Punch", "Q3", "Q5", "Scorpio", "Seltos", "Slavia", "Sonet",
    "Sunny", "Taigun", "Verna", "Virtus", "X1", "X3", "Xuv700", "Yaris"
]

# Combustibles disponibles en el mismo orden que las columnas Fuel_Type_* del entrenamiento
FUEL_TYPES = ["Cng", "Diesel", "Electric", "Hybrid", "Petrol"]

# Owner_Type ordinal: mismo orden usado en el OrdinalEncoder
OWNER_TYPES = ["First", "Second", "Third", "Fourth+"]


def predict_price(model_name: str,
                  owner_type: str,
                  transmission_manual: int,
                  fuel_type: str,
                  year: int,
                  engine_size_cc: float,
                  power_hp: float,
                  kms_driven: float,
                  accidents: int) -> float:
    
    if model_name not in MODELS:
        raise ValueError(f"Modelo desconocido: {model_name}")
    if owner_type not in OWNER_TYPES:
        raise ValueError(f"Owner_Type desconocido: {owner_type}")
    if fuel_type not in FUEL_TYPES:
        raise ValueError(f"Fuel_Type desconocido: {fuel_type}")

    # Owner_Type como ordinal (0, 1, 2, 3)
    owner_type_encoded = float(OWNER_TYPES.index(owner_type))

    # Model_* one-hot
    model_dummies = [1.0 if m == model_name else 0.0 for m in MODELS]

    # Fuel_Type_* one-hot
    fuel_dummies = [1.0 if f == fuel_type else 0.0 for f in FUEL_TYPES]
    
    new_car_features = (
        [owner_type_encoded]
        + model_dummies
        + [float(transmission_manual)]
        + fuel_dummies
        + [year, engine_size_cc, power_hp, kms_driven, accidents]
    )

    new_car_data = np.array(new_car_features).reshape(1, -1)
    new_car_scaled = scaler_X.transform(new_car_data)
    predicted_price_scaled = model.predict(new_car_scaled)
    predicted_price = scaler_y.inverse_transform(predicted_price_scaled.reshape(-1, 1))
    price = round(float(predicted_price[0][0]), 2)
    return price