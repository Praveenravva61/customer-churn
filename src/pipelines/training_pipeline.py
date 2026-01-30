import joblib
from pathlib import Path

from src.models.logistic import LogisticModel
from src.models.random_forest import RandomForestModel
from src.models.xgboost import XGBoostModel
from src.models.lightgbm import LightGBMModel
from src.training.evaluator import Evaluator
from src.training.selector import ModelSelector

FEATURE_PIPELINE_PATH = "artifacts/feature_pipeline_v1.pkl"
DATA_PATH = r"X:\Data Science\Free Bird Achievements\Projects\customer churn\data\processed\Telco_Customer_Churn.csv"

def run():
    feature_pipeline = joblib.load(FEATURE_PIPELINE_PATH)

    import pandas as pd
    df = pd.read_csv(DATA_PATH)
    X = feature_pipeline.transform(df)
    y = df["Churn"].map({"Yes": 1, "No": 0}).values

    model_defs = [
        LogisticModel(),
        RandomForestModel(),
        XGBoostModel(),
        LightGBMModel()
    ]

    results = []

    for model_def in model_defs:
        model = model_def.build()
        score = Evaluator(model, X, y).cross_validate()
        model.fit(X, y)

        results.append({
            "name": model_def.name,
            "model": model,
            "score": score
        })

    best = ModelSelector().select_and_save(results)

    print("Best model:", best["name"])
    print("ROC-AUC:", round(best["score"], 4))

if __name__ == "__main__":
    run()
