# report.py

def display_report(counts):
    print("\nAnalysis Report")
    print("--------------------")

    for level, count in counts.items():
        print(f"{level:<10}: {count}")