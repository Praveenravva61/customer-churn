class DataValidator:
    REQUIRED_COLUMNS = {"customerID", "Churn"}

    def validate(self, df):
        missing = self.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        if df["customerID"].duplicated().any():
            raise ValueError("Duplicate customerID detected")

        if not set(df["Churn"].unique()).issubset({"Yes", "No"}):
            raise ValueError("Invalid target values")

        return True
