from pydantic import BaseModel, Field
from enum import Enum

class FuelType(str, Enum):
    cng = "Cng"
    diesel = "Diesel"
    electric = "Electric"
    hybrid = "Hybrid"
    petrol = "Petrol"


class OwnerType(str, Enum):
    first = "First"
    second = "Second"
    third = "Third"
    fourth_plus = "Fourth+"


class TransmissionType(str, Enum):
    manual = "Manual"
    automatic = "Automatic"


class ModelName(str, Enum):
    series_3 = "3 series"
    a4 = "A4"
    amaze = "Amaze"
    bolero = "Bolero"
    c_class = "C-class"
    camry = "Camry"
    carens = "Carens"
    city = "City"
    civic = "Civic"
    corolla = "Corolla"
    creta = "Creta"
    e_class = "E-class"
    ecosport = "Ecosport"
    endeavour = "Endeavour"
    figo = "Figo"
    gla = "Gla"
    harrier = "Harrier"
    i20 = "I20"
    kicks = "Kicks"
    kushaq = "Kushaq"
    magnite = "Magnite"
    nexon = "Nexon"
    octavia = "Octavia"
    polo = "Polo"
    punch = "Punch"
    q3 = "Q3"
    q5 = "Q5"
    scorpio = "Scorpio"
    seltos = "Seltos"
    slavia = "Slavia"
    sonet = "Sonet"
    sunny = "Sunny"
    taigun = "Taigun"
    verna = "Verna"
    virtus = "Virtus"
    x1 = "X1"
    x3 = "X3"
    xuv700 = "Xuv700"
    yaris = "Yaris"


class UsedCarCreate(BaseModel):
    model_name: ModelName = Field(..., example="C-class")
    owner_type: OwnerType = Field(..., example="First")
    transmission: TransmissionType = Field(..., example="Manual")
    fuel_type: FuelType = Field(..., example="Diesel")
    year: int = Field(..., example=2020)
    engine_size_cc: float = Field(..., example=1500)
    power_hp: float = Field(..., example=150)
    kms_driven: float = Field(..., example=50000)
    accidents: int = Field(default=0, example=0, ge=0)


class UsedCarPredictionResponse(BaseModel):
    message: str
    price: float


class UsedCarResponse(BaseModel):
    id: int = Field(..., example=1)
    model_name: str = Field(..., example="C-class")
    owner_type: str = Field(..., example="First")
    transmission: str = Field(..., example="Manual")
    fuel_type: str = Field(..., example="Diesel")
    year: int = Field(..., example=2020)
    engine_size_cc: float = Field(..., example=1500)
    power_hp: float = Field(..., example=150)
    kms_driven: float = Field(..., example=50000)
    accidents: int = Field(..., example=0)
    price: float = Field(..., example=2500000)