from sklearn.linear_model import LogisticRegression
from .base import BaseModel

class LogisticModel(BaseModel):
    name = "logistic"

    def build(self):
        return LogisticRegression(
            max_iter=1000,
            n_jobs=-1,
            class_weight="balanced"
        )
