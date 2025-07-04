from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and label encoder
model = joblib.load("E:/UNIVERSITY/Semester 6/Big Data Analytics/LAB/ML_Assignment/ml/model.pkl")
label_encoder = joblib.load("E:/UNIVERSITY/Semester 6/Big Data Analytics/LAB/ML_Assignment/ml/label_encoder.pkl")


app = FastAPI(title="🌾 Crop Recommendation API")

# Define input schema
class CropInput(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Crop Recommendation API 🌱"}

@app.post("/predict")
def predict_crop(data: CropInput):
    features = np.array([[data.nitrogen, data.phosphorus, data.potassium,
                          data.temperature, data.humidity, data.ph,
                          data.rainfall]])
    prediction = model.predict(features)[0]
    crop_name = label_encoder.inverse_transform([prediction])[0]

    return {"predicted_crop": crop_name}
