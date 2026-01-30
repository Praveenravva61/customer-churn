import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from .schema import FEATURE_SCHEMA

class FeatureBuilder:
    def __init__(self):
        self.pipeline = None

    def fit(self, df: pd.DataFrame):
        num_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="median"))
        ])

        cat_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])

        self.pipeline = ColumnTransformer([
            ("num", num_pipe, FEATURE_SCHEMA["numerical"]),
            ("cat", cat_pipe, FEATURE_SCHEMA["categorical"])
        ])

        self.pipeline.fit(df)
        return self

    def transform(self, df: pd.DataFrame):
        if self.pipeline is None:
            raise RuntimeError("FeatureBuilder not fitted")

        X = self.pipeline.transform(df)
        y = df[FEATURE_SCHEMA["target"]].map({"Yes": 1, "No": 0}).values
        return X, y
