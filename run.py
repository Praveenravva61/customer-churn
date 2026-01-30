# run.py

from src.pipelines.train_pipeline import run as build_features
from src.pipelines.training_pipeline import run as train_models
import uvicorn


def main():
    print("🚀 Building features...")
    build_features()

    print("🚀 Training models...")
    train_models()

    print("🌐 Starting API...")
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000
    )


if __name__ == "__main__":
    main()
