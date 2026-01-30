from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

MODEL_DIR = Path("artifacts/models")
MODEL_PATH = MODEL_DIR / "best_model.pkl"
FEATURE_PIPELINE_PATH = Path("artifacts/feature_pipeline_v1.pkl")

app = FastAPI(title="Churn Inference Service")

class CustomerPayload(BaseModel):
    customerID: str
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.on_event("startup")
def load_artifacts():
    global model, feature_pipeline
    if not MODEL_PATH.exists():
        raise RuntimeError("Model artifact not found")
    if not FEATURE_PIPELINE_PATH.exists():
        raise RuntimeError("Feature pipeline not found")

    model = joblib.load(MODEL_PATH)
    feature_pipeline = joblib.load(FEATURE_PIPELINE_PATH)

@app.post("/predict")
def predict(payload: CustomerPayload):
    try:
        df = pd.DataFrame([payload.dict()])
        X = feature_pipeline.transform(df)
        prob = float(model.predict_proba(X)[0][1])
        return {
            "churn_probability": round(prob, 4),
            "churn_risk": "HIGH" if prob >= 0.7 else "LOW"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
