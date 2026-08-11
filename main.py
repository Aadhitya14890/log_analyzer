# main.py

from file_handler import read_log_file
from analyzer import analyze_logs
from report import display_report


def main():
    filename = input("Enter log filename: ")

    log_lines = read_log_file(filename)

    if log_lines is None:
        return

    counts = analyze_logs(log_lines)

    display_report(counts)


if __name__ == "__main__":
    main()