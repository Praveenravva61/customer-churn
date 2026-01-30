import json
from pathlib import Path
from datetime import datetime

class ModelRegistry:
    def __init__(self, base_dir="artifacts/registry"):
        self.base = Path(base_dir)
        self.base.mkdir(parents=True, exist_ok=True)

    def register(self, model_name, metrics, artifact_path):
        record = {
            "model": model_name,
            "metrics": metrics,
            "artifact": str(artifact_path),
            "registered_at": datetime.utcnow().isoformat()
        }

        record_path = self.base / f"{model_name}_metadata.json"
        with open(record_path, "w") as f:
            json.dump(record, f, indent=2)

        return record_path