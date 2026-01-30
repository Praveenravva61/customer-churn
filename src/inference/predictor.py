import joblib
import pandas as pd
from pathlib import Path

class Predictor:
    def __init__(self, model_path, feature_pipeline_path):
        self.model = joblib.load(model_path)
        self.pipeline = joblib.load(feature_pipeline_path)

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        X = self.pipeline.transform(df)
        prob = self.model.predict_proba(X)[0][1]
        return prob
