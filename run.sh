#!/bin/bash
set -e

echo "Building features..."
python src/pipelines/train_pipeline.py


echo "Training models..."
python src/pipelines/training_pipeline.py

echo "Starting API..."
uvicorn api.main:app --host 0.0.0.0 --port 8000
