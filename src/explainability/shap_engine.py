import shap
import numpy as np

class ShapExplainer:
    def __init__(self, model):
        self.explainer = shap.Explainer(model)

    def explain(self, X):
        values = self.explainer(X)
        return {
            "mean_abs_shap": np.abs(values.values).mean(axis=0).tolist()
        }\n