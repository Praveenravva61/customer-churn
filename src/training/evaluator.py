from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import numpy as np

class Evaluator:
    def __init__(self, model, X, y, folds=5):
        self.model = model
        self.X = X
        self.y = y
        self.folds = folds

    def cross_validate(self):
        cv = StratifiedKFold(n_splits=self.folds, shuffle=True, random_state=42)
        scores = []

        for train_idx, val_idx in cv.split(self.X, self.y):
            X_train, X_val = self.X[train_idx], self.X[val_idx]
            y_train, y_val = self.y[train_idx], self.y[val_idx]

            self.model.fit(X_train, y_train)
            prob = self.model.predict_proba(X_val)[:, 1]
            scores.append(roc_auc_score(y_val, prob))

        return float(np.mean(scores))
