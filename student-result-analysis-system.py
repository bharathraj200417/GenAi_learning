import pandas as pd

# Read CSV file
df = pd.read_csv("student.csv")

print("Student Details")
print(df)
print()

# Subject columns
subjects = ["Tamil", "English", "Maths", "Science", "Social"]

# Lists to store calculated values
total_list = []
average_list = []
grade_list = []

# Pass/Fail Count
pass_count = 0
fail_count = 0

# ---------------- Student Result Processing ----------------

for i in range(len(df)):

    name = df.loc[i, "Name"]

    # Calculate Total & Average
    total = df.loc[i, subjects].sum()
    average = total / len(subjects)

    # Grade Calculation
    if average >= 90:
        grade = "S"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"

    # Pass / Fail Count
    if average >= 50:
        pass_count += 1
    else:
        fail_count += 1

    total_list.append(total)
    average_list.append(average)
    grade_list.append(grade)

# Add new columns
df["Total"] = total_list
df["Average"] = average_list
df["Grade"] = grade_list

# ---------------- Result Summary ----------------

print("------ RESULT SUMMARY ------")
print("Total Pass :", pass_count)
print("Total Fail :", fail_count)
print("Pass Percentage :", round((pass_count / len(df)) * 100, 2), "%")
print()

print("Class Average :", round(df["Average"].mean(), 2))
print("Highest Average :", df["Average"].max())
print("Lowest Average :", df["Average"].min())
print()

# ---------------- Highest Scorer ----------------

highest_average = df["Average"].max()

print("Highest Scorer(s)")
for i in range(len(df)):
    if df.loc[i, "Average"] == highest_average:
        print(df.loc[i, "Name"], "-", highest_average)

print()

# ---------------- Subject-wise Toppers ----------------

print("Subject-wise Toppers")

for subject in subjects:

    highest_mark = df[subject].max()

    for i in range(len(df)):
        if df.loc[i, subject] == highest_mark:
            print(subject, ":", df.loc[i, "Name"], "-", highest_mark)

print()

# ---------------- Subject-wise Average ----------------

print("Subject-wise Average")

for subject in subjects:
    print(subject, ":", round(df[subject].mean(), 2))

print()

# ---------------- Student Ranking ----------------

df["Rank"] = df["Average"].rank(ascending=False, method="min").astype(int)

print("Student Ranking")
print(df[["Name", "Average", "Rank"]])

print()

# Sort by Rank
df = df.sort_values(by="Rank")

# Save to CSV
df.to_csv("output.csv", index=False)
print(df)
print()
print("output.csv file saved successfully!")
