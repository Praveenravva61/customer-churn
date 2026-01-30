from sklearn.ensemble import RandomForestClassifier
from .base import BaseModel

class RandomForestModel(BaseModel):
    name = "random_forest"

    def build(self):
        return RandomForestClassifier(
            n_estimators=300,
            max_depth=None,
            min_samples_leaf=5,
            n_jobs=-1,
            random_state=42
        )
