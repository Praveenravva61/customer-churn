from src.data_ingestion.reader import DataReader
from src.data_ingestion.validator import DataValidator
from src.feature_store.builder import FeatureBuilder
from src.feature_store.serializer import FeatureSerializer

RAW_DATA_PATH = r"X:\Data Science\Free Bird Achievements\Projects\customer churn\data\processed\Telco_Customer_Churn.csv"


def run():
    df = DataReader(RAW_DATA_PATH).read()
    DataValidator().validate(df)

    feature_builder = FeatureBuilder()
    feature_builder.fit(df)
    X, y = feature_builder.transform(df)

    FeatureSerializer().save_pipeline(
        feature_builder.pipeline,
        version="v1"
    )

    print("Feature pipeline built successfully")
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")

if __name__ == "__main__":
    run()
