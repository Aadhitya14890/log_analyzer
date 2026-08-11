# report.py
import csv

def display_report(counts):
    print("\nAnalysis Report")
    print("--------------------")

    for level, count in counts.items():
        print(f"{level:<10}: {count}")


def save_csv_report(counts, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["log level", "Count"])

        for level, count in counts.items():
            writer.writerow([level, count])

