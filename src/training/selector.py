from pathlib import Path
import json
import joblib

class ModelSelector:
    def __init__(self, artifact_dir="artifacts/models"):
        self.dir = Path(artifact_dir)
        self.dir.mkdir(parents=True, exist_ok=True)

    def select_and_save(self, results):
        best = max(results, key=lambda x: x["score"])
        joblib.dump(best["model"], self.dir / "best_model.pkl")

        with open(self.dir / "model_scores.json", "w") as f:
            json.dump(
                {r["name"]: r["score"] for r in results},
                f,
                indent=2
            )
        return best
