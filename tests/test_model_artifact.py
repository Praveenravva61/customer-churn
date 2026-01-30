import joblib
from pathlib import Path

def test_model_exists():
    path = Path("artifacts/models/best_model.pkl")
    assert path.exists()
    model = joblib.load(path)
    assert hasattr(model, "predict_proba")\n