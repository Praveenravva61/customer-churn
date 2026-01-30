from functools import lru_cache
import json

class PredictionCache:
    def __init__(self, size=256):
        self.size = size

    @lru_cache(maxsize=256)
    def get(self, key: str):
        return None

    def make_key(self, payload: dict):
        return json.dumps(payload, sort_keys=True)\n