from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# 1. System Design Concept: Data Validation using Pydantic
# Yeh class ensure karegi ki frontend se aane wala data exactly is format mein ho.
class CropInput(BaseModel):
    State: str
    Region: str
    Crop: str
    Rainfall_mm: float
    Temperature_C: float

# 2. API Initialize karna
app = FastAPI(
    title="Smart Rural Economy System API",
    description="Backend API for agricultural predictions",
    version="1.0"
)

# 3. Model Load karna (Global Scope)
# Hum model ko bahar load kar rahe hain taaki API start hote hi model memory mein aa jaye,
# aur har request par baar-baar load na karna pade (Performance Booster).
print("Loading ML Model...")
try:
    model = joblib.load('crop_price_model.joblib')
except Exception as e:
    print(f"Error loading model: {e}")

# 4. Basic Root Endpoint (Check karne ke liye ki API chal rahi hai)
@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Rural Economy System API. Go to /docs for testing."}

# 5. Prediction Endpoint (POST request kyunki hum data bhej rahe hain)
@app.post("/predict-price")
def predict_crop_price(data: CropInput):
    try:
        # Pydantic data ko dictionary mein badalna aur fir Pandas DataFrame mein convert karna
        input_data = pd.DataFrame([data.model_dump()])
        
        # ML Model se predict karwana
        prediction = model.predict(input_data)[0]
        
        # Clean JSON format mein result wapas bhejna
        return {
            "status": "success",
            "input_data": data,
            "predicted_price_per_quintal": round(prediction, 2)
        }
    except Exception as e:
        # Agar koi error aaye toh server crash hone se bachana aur error message bhejna
        raise HTTPException(status_code=500, detail=str(e))