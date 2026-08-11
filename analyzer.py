# analyzer.py

def analyze_logs(log_lines, log_levels):
    counts = {}

    # Initialize all log levels to 0
    for level in log_levels:
        counts[level] = 0

    # Check each line
    for line in log_lines:
        for level in log_levels:
            if level in line:
                counts[level] += 1

    return counts