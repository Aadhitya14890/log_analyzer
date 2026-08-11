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


def save_html_report(counts, filename):
    with open(filename, "w") as file:
        file.write("<html>")
        file.write("<head>")
        file.write("<title>Log Analysis Report</title>")
        file.write("</head>")

        file.write("<body>")
        file.write("<h1>Log Analysis Report</h1>")

        file.write("<table border='1'>")
        file.write("<tr>")
        file.write("<th>Log Level</th>")
        file.write("<th>Count</th>")
        file.write("</tr>")

        for level, count in counts.items():
            file.write("<tr>")
            file.write(f"<td>{level}</td>")
            file.write(f"<td>{count}</td>")
            file.write("</tr>")

        file.write("</table>")
        file.write("</body>")
        file.write("</html>")

