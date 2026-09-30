"""Student Marks Analysis - a beginner data science project.

Generates a sample dataset of student marks, analyzes it with pandas,
and saves charts with matplotlib.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
os.makedirs("data", exist_ok=True)
os.makedirs("images", exist_ok=True)

# 1. Create sample data (100 students)
n = 100
hours = np.round(np.random.uniform(1, 8, n), 1)
df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "study_hours": hours,
    "math": np.clip(hours * 8 + np.random.normal(30, 8, n), 0, 100).round(),
    "science": np.clip(hours * 7 + np.random.normal(33, 8, n), 0, 100).round(),
    "english": np.clip(hours * 5 + np.random.normal(42, 8, n), 0, 100).round(),
})
df["total"] = df[["math", "science", "english"]].sum(axis=1)
df["average"] = (df["total"] / 3).round(1)
df.to_csv("data/student_marks.csv", index=False)

# 2. Analysis
print("=== Dataset preview ===")
print(df.head(), "\n")

print("=== Subject averages ===")
subjects = df[["math", "science", "english"]]
print(subjects.mean().round(1), "\n")

print("=== Top 5 students ===")
print(df.nlargest(5, "total")[["student_id", "study_hours", "total"]], "\n")

corr = df["study_hours"].corr(df["average"])
print(f"Correlation between study hours and average marks: {corr:.2f}")

# 3. Charts
subjects.mean().plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Average Marks by Subject")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/subject_averages.png")
plt.close()

plt.scatter(df["study_hours"], df["average"], alpha=0.7)
m, b = np.polyfit(df["study_hours"], df["average"], 1)
plt.plot(df["study_hours"], m * df["study_hours"] + b, color="red")
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study hours per day")
plt.ylabel("Average marks")
plt.tight_layout()
plt.savefig("images/hours_vs_marks.png")
plt.close()

print("\nCharts saved in the images/ folder.")
