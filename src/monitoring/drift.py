import numpy as np

class DataDriftDetector:
    def __init__(self, threshold=0.1):
        self.threshold = threshold

    def detect(self, train_mean, inference_mean):
        diff = abs(train_mean - inference_mean)
        return bool(diff > self.threshold)\n