from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

# Yeh class hamari "crop_predictions" table ko represent karti hai
class CropPrediction(Base):
    __tablename__ = "crop_predictions"

    # Columns define kar rahe hain
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, index=True)
    region = Column(String)
    crop_name = Column(String, index=True) # Index=True isliye taaki search fast ho
    rainfall_mm = Column(Float)
    temperature_c = Column(Float)
    predicted_price = Column(Float)
    client_ip = Column(String) # Naya column metadata ke liye
    
    # default=datetime.utcnow apne aap current time save kar lega jab bhi naya record banega
    created_at = Column(DateTime, default=datetime.utcnow)