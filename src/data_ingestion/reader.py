import pandas as pd
from pathlib import Path

class DataReader:
    def __init__(self, path: str):
        self.path = Path(path)

    def read(self) -> pd.DataFrame:
        if not self.path.exists():
            raise FileNotFoundError(f"Data not found: {self.path}")
        df = pd.read_csv(self.path)
        if df.empty:
            raise ValueError("Loaded dataframe is empty")
        return df


