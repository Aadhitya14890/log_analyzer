# main.py

import logging
from file_handler import read_log_file
from analyzer import analyze_logs
from report import display_report
from config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.info("Log analysis started")

    filename = input("Enter log filename: ")

    logger.info("Reading file: %s", filename)

    log_lines = read_log_file(filename)

    if log_lines is None:
        logger.error("Could not read file: %s", filename)
        return

    counts = analyze_logs(log_lines)

    display_report(counts)

    logger.info("Log analysis completed")

if __name__ == "__main__":
    main()