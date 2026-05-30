from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pandas as pd
import joblib

# Hamari banayi hui files import kar rahe hain
import models
from database import engine, SessionLocal

# 1. Database tables create karna (Agar pehle se nahi hain)
models.Base.metadata.create_all(bind=engine)

# 2. Pydantic Validation Schema (Input ke liye)
class CropInput(BaseModel):
    state: str
    region: str
    crop_name: str
    rainfall_mm: float
    temperature_c: float

app = FastAPI(
    title="Smart Rural Economy System API",
    description="Backend API with ML and Database Tracking",
    version="2.0"
)

# 3. Model Load karna
print("Loading ML Model...")
try:
    model = joblib.load('crop_price_model.joblib')
except Exception as e:
    print(f"Error loading model: {e}")

# 4. Database Dependency (Safe Connection Manager)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Rural Economy System API v2.0"}

# 5. Updated Prediction Endpoint
@app.post("/predict-price")
def predict_crop_price(request: Request, data: CropInput, db: Session = Depends(get_db)):
    try:
        # A. Data ko DataFrame mein convert karna
        input_data = pd.DataFrame([data.model_dump()])
        
        # DataFrame ke columns capital letter wale hone chahiye (kyunki model waise train hua tha)
        input_data.columns = ['State', 'Region', 'Crop', 'Rainfall_mm', 'Temperature_C']
        
        # B. Model se predict karwana
        prediction = float(model.predict(input_data)[0])
        
        # C. Client ka IP Address nikalna
        client_ip = request.client.host

        # D. Database mein save karne ke liye record banana
        new_record = models.CropPrediction(
            state=data.state,
            region=data.region,
            crop_name=data.crop_name,
            rainfall_mm=data.rainfall_mm,
            temperature_c=data.temperature_c,
            predicted_price=prediction,
            client_ip=client_ip
        )
        
        # E. Record ko database mein daalna aur save (commit) karna
        db.add(new_record)
        db.commit()
        db.refresh(new_record) # Nayi generate hui ID wapas laane ke liye

        # F. Result return karna
        return {
            "status": "success",
            "record_id": new_record.id,
            "predicted_price_per_quintal": round(prediction, 2)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))