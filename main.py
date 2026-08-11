# main.py

import logging
import argparse
from file_handler import read_log_file
from analyzer import analyze_logs
from report import display_report, save_csv_report, save_html_report
from config import setup_logging, load_config

config = load_config()
setup_logging(config)

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a log file and generate a report."
    )

    parser.add_argument(
        "filename",
        help="path to the log file"
    )

    args = parser.parse_args()
    filename = args.filename

    logger.info("Log analysis started")
    logger.info("Reading file: %s", filename)

    log_lines = read_log_file(filename)

    if log_lines is None:
        logger.error("Could not read file: %s", filename)
        return

    counts = analyze_logs(log_lines, config["log_levels"])

    display_report(counts)
    save_csv_report(counts, config["csv_report"])
    save_html_report(counts, config["html_report"])

    logger.info("Log analysis completed")

if __name__ == "__main__":
    main()