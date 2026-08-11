# analyzer.py

from config import LOG_LEVELS


def analyze_logs(log_lines):
    counts = {}

    # Initialize all log levels to 0
    for level in LOG_LEVELS:
        counts[level] = 0

    # Check each line
    for line in log_lines:
        for level in LOG_LEVELS:
            if level in line:
                counts[level] += 1

    return counts