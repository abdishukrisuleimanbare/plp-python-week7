
import csv

# Step 1: Read learner data from the CSV file
try:
    with open("hubs.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

# Step 2: Initialize report calculations
total_score = 0
passed = 0
failed = 0

# Step 3: Calculate learner results
for row in rows:
    score = int(row["score"])

    total_score += score

    if score >= 50:
        passed += 1
    else:
        failed += 1

# Step 4: Calculate the average safely
total_learners = len(rows)

if total_learners > 0:
    average_score = round(total_score / total_learners, 1)
else:
    average_score = 0.0

# Step 5: Write the report to report.txt
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("LEARNER REPORT\n")
    file.write(f"Total learners: {total_learners}\n")
    file.write(f"Passed: {passed}\n")
    file.write(f"Failed: {failed}\n")
    file.write(f"Average score: {average_score}\n")

# Step 6: Confirm completion
print("Report written to report.txt")
