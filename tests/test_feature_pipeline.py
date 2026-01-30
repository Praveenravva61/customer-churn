import joblib
import pandas as pd

def test_feature_pipeline_load():
    pipeline = joblib.load("artifacts/feature_pipeline_v1.pkl")
    df = pd.DataFrame([{
        "customerID": "1",
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.5,
        "TotalCharges": 840.0,
        "Churn": "No"
    }])

    X = pipeline.transform(df)
    assert X.shape[0] == 1\n