from xgboost import XGBClassifier
from .base import BaseModel

class XGBoostModel(BaseModel):
    name = "xgboost"

    def build(self):
        return XGBClassifier(
            n_estimators=400,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            n_jobs=-1
        )
