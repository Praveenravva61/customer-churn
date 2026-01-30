import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("artifacts/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        LOG_DIR / "service.log",
        maxBytes=5_000_000,
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger\n