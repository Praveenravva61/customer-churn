import joblib
from pathlib import Path

class Trainer:
    def __init__(self, model, X, y):
        self.model = model
        self.X = X
        self.y = y

    def fit(self):
        self.model.fit(self.X, self.y)
        return self.model

    def save(self, path: Path):
        joblib.dump(self.model, path)
