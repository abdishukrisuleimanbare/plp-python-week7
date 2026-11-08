import csv

try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("hubs.csv not found")      # missing line 1
    rows = []                         # missing line 1 (set rows to empty list)

total = 0
passed = 0

for row in rows:
    score = int(row["score"])         # missing line 2
    total += score
    if score >= 50:
        passed += 1                   # missing line 3

average = round(total / len(rows), 1)

with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(len(rows) - passed) + "\n")   # missing line 4
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")