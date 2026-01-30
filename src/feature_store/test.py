import joblib
from pathlib import Path

class serilization:
    def __init__(self, base_path= "artifacts"):
        self.base = Path(base_path)
        self.base.mkdir(parents= True, exist_ok = True)
    
    def save_pipeline(self, pipeline, version= "v1"):
        path = self.base / f"feature_pipeline_{version}.pkl"
        joblib.dump(pipeline, path)
        return path
    