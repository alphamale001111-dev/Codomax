# 📊 Data Cleaning & Statistics Guide (Day 5)

Welcome to Day 5 of your data science journey! Today, we explore **Data Cleaning**, one of the most critical phases of data analysis. In the real world, data is rarely clean; it is often riddled with missing values, duplicate entries, inconsistent casing, and extreme outliers. 

Cleaning your data ensures your downstream models and analysis remain accurate and unbiased.

---

## ⚡ Key Concepts of Data Cleaning

### 1. Detecting & Handling Duplicate Rows
Duplicate data can artificially skew statistics and result in overfitting during machine learning.
*   **Identify Duplicates**: `df.duplicated()` returns a boolean Series indicating whether a row is a duplicate of a previous row.
*   **Count Duplicates**: `df.duplicated().sum()`
*   **Remove Duplicates**: `df.drop_duplicates(inplace=True)` drops exact duplicates. You can also specify subset columns: `df.drop_duplicates(subset=['Student_ID'], keep='first')`.

### 2. Handling Missing Data (`NaN`/Nulls)
Real-world datasets often have missing entries. You must decide whether to remove or impute them:
*   **Identify Missing Values**: `df.isnull().sum()` or `df.isna().sum()` returns the count of missing values per column.
*   **Drop Missing Values**: `df.dropna(inplace=True)` deletes any row with a missing value. Use this only when you have abundant data or when missing values cannot be estimated.
*   **Impute (Fill) Missing Values**: `df.fillna(value, inplace=True)` replaces missing values.
    *   **Numerical columns**: Fill with the **Mean** (average) or **Median** (middle value). The median is usually preferred if the column has outliers, as it is robust to extreme values.
    *   **Categorical columns**: Fill with the **Mode** (most frequent value) or a default placeholder (like `'Unknown'`).

### 3. String Standardization & Formatting
Text and categorical data are prone to typos, trailing spaces, and inconsistent casing (e.g., `'Male'`, `'MALE'`, `'male'`).
*   **Remove Whitespace**: `df['Column'] = df['Column'].str.strip()`
*   **Standardize Casing**: `df['Column'] = df['Column'].str.title()` (converts to Title Case) or `.str.lower()` (lowercase).

### 4. Detecting Outliers & Anomalies using Statistics
Outliers are values that lie far outside the normal range. They can be detected by looking at descriptive statistics:
*   **Summary Statistics**: `df.describe()` returns count, mean, standard deviation, min, max, and percentiles.
*   **Anomalies**: If the `min` score is `-10` or the `max` study hours is `168.0`, these are anomalies that must be fixed (either capped, dropped, or replaced with the median/mean).

---

## 📚 Day 5 Curriculum & Files

We have set up a dirty student scores dataset and a script to walk you through the cleaning process:

### 📁 Files Created:
1. **`Day 5/dirty_student_scores.csv`**: A raw dataset with missing values, duplicate entries, casing anomalies, and unrealistic outliers.
2. **`Day 5/data_cleaning.py`**: An interactive script showing step-by-step duplicate removal, imputation of missing data, text formatting, and outlier handling.
3. **`Day 5/cleaned_student_scores.csv`**: The output clean dataset generated after you run the script.

---

## 🚀 Running the Interactive Lesson

To run today's interactive lesson, clean the dataset, and test your understanding in the mini-challenge, run the following command in your terminal:

```bash
.venv/bin/python3 "Day 5/data_cleaning.py"
```

Observe how the dataset's shape, missing value count, and statistical summary change at each step of the cleaning pipeline!
