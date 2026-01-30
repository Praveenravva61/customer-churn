from lightgbm import LGBMClassifier
from .base import BaseModel

class LightGBMModel(BaseModel):
    name = "lightgbm"

    def build(self):
        return LGBMClassifier(
            n_estimators=500,
            learning_rate=0.05,
            num_leaves=31,
            subsample=0.8,
            colsample_bytree=0.8,
            n_jobs=-1
        )
