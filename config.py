# config.py

import logging

LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


def setup_logging():
    logging.basicConfig(
        filename="log_analyzer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )