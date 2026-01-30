import time
from collections import defaultdict

class MetricsCollector:
    def __init__(self):
        self.metrics = defaultdict(list)

    def record_latency(self, name, duration):
        self.metrics[name].append(duration)

    def summary(self):
        return {
            k: {
                "count": len(v),
                "avg_ms": round(sum(v) / len(v), 4)
            }
            for k, v in self.metrics.items()
        }\n