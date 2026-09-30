# 📊 Student Marks Analysis

A beginner data science project using **Python, pandas, NumPy, and Matplotlib**.

## Problem
Does studying more hours lead to better marks? Which subject do students score best in?

## What this project does
- Generates a sample dataset of 100 students (study hours + marks in Math, Science, English)
- Calculates totals, averages, and the top 5 students
- Finds the correlation between study hours and average marks
- Saves charts to the `images/` folder

## How to run
```bash
git clone https://github.com/<your-username>/student-marks-analysis.git
cd student-marks-analysis
pip install -r requirements.txt
python analysis.py
```

## Results
- Average marks are similar across subjects (about 63-64)
- Study hours and average marks show a strong positive correlation (about 0.96)

![Subject averages](images/subject_averages.png)
![Hours vs marks](images/hours_vs_marks.png)

*Note: the data is synthetic (randomly generated), so this is for learning practice.*

## What I learned
- Creating and cleaning DataFrames with pandas
- Basic statistics: mean, correlation
- Plotting with Matplotlib

## Next steps
- Try it on a real dataset from Kaggle
- Add a Streamlit dashboard
