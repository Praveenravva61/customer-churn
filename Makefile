build:
	pip install -r requirements.txt

train:
	python src/pipelines/train_pipeline.py
	python src/pipelines/training_pipeline.py

serve:
	uvicorn api.main:app --host 0.0.0.0 --port 8000

test:
	pytest -q
