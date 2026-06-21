from sqlalchemy import Column, Integer, Float, String
from database import Base

class UsedCar(Base):
    __tablename__ = "usedcars"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)       # ej. "C-class"
    owner_type = Column(String, nullable=False)        # ej. "First", "Second", "Third", "Fourth+"
    transmission = Column(String, nullable=False)      # ej. "Manual" o "Automatic"
    fuel_type = Column(String, nullable=False)         # ej. "Diesel", "Petrol", "Cng", "Electric", "Hybrid"
    year = Column(Integer, nullable=False)
    engine_size_cc = Column(Float, nullable=False)
    power_hp = Column(Float, nullable=False)
    kms_driven = Column(Float, nullable=False)
    accidents = Column(Integer, nullable=False, default=0)
    price = Column(Float, nullable=True)