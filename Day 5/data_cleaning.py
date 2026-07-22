# Day 5/data_cleaning.py
"""
Pandas Lesson 2: Data Cleaning - Missing Values, Duplicates, and Statistics
--------------------------------------------------------------------------
Data cleaning is the process of fixing or removing incorrect, corrupted, 
incorrectly formatted, duplicate, or incomplete data within a dataset.

In this lesson, we will cover:
1. Detecting and Handling Duplicate Rows
2. Detecting and Handling Missing (Null) Values
3. Standardizing Categorical Values (Casing/Whitespace)
4. Identifying and Fixing Outliers/Anomalies using Statistics
5. Saving the Cleaned Dataset
"""

import os
import pandas as pd
import numpy as np

def print_separator(title=None):
    if title:
        print("\n" + "="*25 + f" {title} " + "="*25 + "\n")
    else:
        print("\n" + "="*70 + "\n")

def run_lesson():
    print("==============================================================")
    print("      🐼 LESSON 2: PANDAS DATA CLEANING & STATISTICS 🐼     ")
    print("==============================================================")
    
    # Get current file path directory to locate dirty_student_scores.csv
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "dirty_student_scores.csv")
    cleaned_csv_path = os.path.join(current_dir, "cleaned_student_scores.csv")
    
    # --- 1. LOAD THE DIRTY DATASET ---
    print_separator("1. LOADING DIRTY DATASET")
    try:
        df = pd.read_csv(csv_path)
        print("   ✅ Dirty dataset loaded successfully!")
        print(f"   📊 Initial shape of dataset: {df.shape} (rows, columns)")
    except FileNotFoundError:
        print(f"   ❌ Error: '{csv_path}' not found.")
        return

    # --- 2. DETECTING DUPLICATES ---
    print_separator("2. DETECTING & REMOVING DUPLICATE ROWS")
    # Count duplicates
    num_duplicates = df.duplicated().sum()
    print(f"   • Total exact duplicate rows found: {num_duplicates}")
    
    if num_duplicates > 0:
        print("\n   • Showing the duplicate rows:")
        print(df[df.duplicated(keep=False)].sort_values(by="Student_ID"))
        
        # Dropping duplicates
        print("\n   • Dropping duplicates using: df.drop_duplicates(inplace=True)")
        df.drop_duplicates(inplace=True)
        print(f"   • Shape after removing duplicates: {df.shape}")
    else:
        print("   • No duplicate rows found.")

    # --- 3. DETECTING & HANDLING MISSING VALUES ---
    print_separator("3. DETECTING & HANDLING MISSING VALUES")
    print("   • Missing value count per column (df.isnull().sum()):")
    print(df.isnull().sum())
    
    print("\n   • Strategies for Missing Values:")
    print("     1. Drop rows with missing values (df.dropna()) - risk of losing data.")
    print("     2. Impute (fill) missing values (df.fillna()) - keeps data size, uses statistical averages.")
    
    # Let's inspect rows with missing values before filling
    print("\n   • Displaying rows with missing (NaN) values:")
    print(df[df.isnull().any(axis=1)])
    
    # Fill Numerical columns with median (more robust to outliers than mean)
    print("\n   • Imputing missing numerical values with their column medians:")
    for col in ['Math_Score', 'Science_Score', 'Attendance_Pct', 'Study_Hours_Per_Week']:
        median_val = df[col].median()
        print(f"     - Filling missing values in {col} with median: {median_val:.1f}")
        df[col] = df[col].fillna(median_val)
        
    # Fill Categorical columns with mode or a default value
    print("\n   • Imputing missing categorical values:")
    # For Gender, fill with 'Unknown' for now
    print("     - Filling missing values in 'Gender' with 'Unknown'")
    df['Gender'] = df['Gender'].fillna('Unknown')
    
    # For Extra_Curricular, fill with 'No' (mode)
    curricular_mode = df['Extra_Curricular'].mode()[0]
    print(f"     - Filling missing values in 'Extra_Curricular' with mode: '{curricular_mode}'")
    df['Extra_Curricular'] = df['Extra_Curricular'].fillna(curricular_mode)

    print("\n   ✅ Missing values checked after imputation (df.isnull().sum()):")
    print(df.isnull().sum())

    # --- 4. STANDARDIZING CATEGORICAL VALUES (Casing/Whitespace) ---
    print_separator("4. STANDARDIZING CATEGORICAL VALUES")
    print("   • Unique values in 'Gender' before cleaning:")
    print(df['Gender'].unique())
    
    # Standardize casing to Title Case and strip whitespaces
    print("\n   • Standardizing 'Gender' casing: df['Gender'] = df['Gender'].str.strip().str.title()")
    df['Gender'] = df['Gender'].str.strip().str.title()
    
    print("   • Unique values in 'Gender' after cleaning:")
    print(df['Gender'].unique())

    # --- 5. DETECTING & HANDLING OUTLIERS ---
    print_separator("5. DETECTING & HANDLING OUTLIERS")
    print("   • Statistical summary (df.describe()):")
    print(df.describe())
    
    print("\n   ⚠️ Notice the anomalies in the summary statistics:")
    print("     - Math_Score Min is negative (-10.0), which is impossible for a test out of 100.")
    print("     - Study_Hours_Per_Week Max is 168.0, which means studying 24 hours a day for 7 days!")
    
    # Filter and view outliers
    print("\n   • Displaying rows with outlier/anomaly values:")
    outliers = df[(df['Math_Score'] < 0) | (df['Study_Hours_Per_Week'] > 100)]
    print(outliers)
    
    # Fix outliers
    print("\n   • Correcting outliers:")
    # Replace negative Math_Score with the median score
    math_median = df[df['Math_Score'] >= 0]['Math_Score'].median()
    print(f"     - Replacing negative Math_Score with median ({math_median}):")
    df.loc[df['Math_Score'] < 0, 'Math_Score'] = math_median
    
    # Replace study hours > 100 with median study hours
    hours_median = df[df['Study_Hours_Per_Week'] <= 100]['Study_Hours_Per_Week'].median()
    print(f"     - Replacing Study_Hours_Per_Week > 100 with median ({hours_median}):")
    df.loc[df['Study_Hours_Per_Week'] > 100, 'Study_Hours_Per_Week'] = hours_median

    print("\n   📊 Final statistical summary after outlier correction:")
    print(df.describe())

    # --- 6. SAVE CLEANED DATASET ---
    print_separator("6. SAVING CLEANED DATASET")
    df.to_csv(cleaned_csv_path, index=False)
    print(f"   ✅ Cleaned dataset successfully saved to: {cleaned_csv_path}")
    print(f"   📊 Final dataset shape: {df.shape}")

    # --- 7. MINI-CHALLENGE / QUIZ ---
    print_separator("💡 DAY 5 QUIZ: DATA CLEANING IN PANDAS")
    score = 0
    
    # Question 1
    print("\nQuestion 1: Which Pandas method returns a boolean Series indicating duplicate rows?")
    print("   a) df.is_duplicate()")
    print("   b) df.duplicated()")
    print("   c) df.drop_duplicates()")
    ans1 = input("Your answer (a, b, or c): ").strip().lower()
    if ans1 == "b":
        print("   ✅ Correct! df.duplicated() returns a boolean mask of duplicate rows.")
        score += 1
    else:
        print("   ❌ Incorrect. df.duplicated() identifies duplicates; drop_duplicates() removes them.")
        
    # Question 2
    print("\nQuestion 2: What is the primary difference between df.dropna() and df.fillna()?")
    print("   a) dropna() removes rows/columns with nulls; fillna() replaces nulls with specified values.")
    print("   b) dropna() fills nulls with zero; fillna() drops the column.")
    print("   c) There is no difference; they are aliases.")
    ans2 = input("Your answer (a, b, or c): ").strip().lower()
    if ans2 == "a":
        print("   ✅ Correct! dropna() discards missing data, while fillna() replaces it.")
        score += 1
    else:
        print("   ❌ Incorrect. dropna() deletes missing values; fillna() replaces them.")
        
    # Question 3
    print("\nQuestion 3: Why is the median often preferred over the mean when filling missing numerical scores?")
    print("   a) The median is faster to compute.")
    print("   b) The median is robust to extreme outliers (like a score of -10 or 999).")
    print("   c) The median is always higher than the mean.")
    ans3 = input("Your answer (a, b, or c): ").strip().lower()
    if ans3 == "c" or ans3 == "a":
        print("   ❌ Incorrect. Median is robust to outliers, meaning extreme values do not distort it.")
    elif ans3 == "b":
        print("   ✅ Correct! Outliers skew the mean, but the median remains a reliable center value.")
        score += 1
    else:
        print("   ❌ Invalid choice. The correct answer is b (median is robust to outliers).")
        
    print(f"\nYour score: {score}/3")
    if score == 3:
        print("🎉 Perfect! You've mastered duplicate removal, missing value imputation, and statistics-based cleaning!")
    else:
        print("👍 Good try! Review the code outputs and concepts and try running again.")
    print("==============================================================\n")

if __name__ == "__main__":
    run_lesson()
