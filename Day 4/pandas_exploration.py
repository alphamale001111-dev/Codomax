# Day 4/pandas_exploration.py
"""
Pandas Lesson 1: Introduction to Pandas and Dataset Exploration
--------------------------------------------------------------
Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation 
library built on top of the Python programming language.

In this lesson, we will cover:
1. Importing Pandas
2. Loading a CSV Dataset
3. Exploring Rows (head, tail, sample, slicing)
4. Exploring Columns (columns list, selection, data types)
5. Exploring Dataset Info (shape, info, describe, missing values)
"""

import os
import pandas as pd

def print_separator():
    print("\n" + "="*70 + "\n")

def run_lesson():
    print("==============================================================")
    print("      🐼 LESSON 1: PANDAS DATASET LOADING & EXPLORATION 🐼   ")
    print("==============================================================")
    
    # Get current file path directory to locate student_scores.csv
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "student_scores.csv")
    
    # --- 1. IMPORTING PANDAS & LOADING DATASET ---
    print("\n1. IMPORTING PANDAS AND LOADING DATA:")
    print("   Code: import pandas as pd")
    print(f"   Code: df = pd.read_csv('{csv_path}')")
    
    try:
        df = pd.read_csv(csv_path)
        print("   ✅ Dataset loaded successfully!")
    except FileNotFoundError:
        print("   ❌ Error: 'student_scores.csv' file not found.")
        return

    print_separator()

    # --- 2. EXPLORING DATASET ROWS ---
    print("2. EXPLORING ROWS:")
    
    # head() - First 5 rows
    print("\n   • df.head() - First 5 rows of the dataset:")
    print(df.head())
    
    # tail() - Last 5 rows
    print("\n   • df.tail(3) - Last 3 rows of the dataset:")
    print(df.tail(3))
    
    # sample() - Random rows
    print("\n   • df.sample(2) - Random sample of 2 rows:")
    print(df.sample(2))
    
    # Row slicing (e.g. rows 10 to 14)
    print("\n   • Slicing rows 10 to 14 (df.iloc[10:15]):")
    print(df.iloc[10:15])

    print_separator()

    # --- 3. EXPLORING DATASET COLUMNS ---
    print("3. EXPLORING COLUMNS:")
    
    # List all columns
    print(f"\n   • Column names (df.columns):\n     {list(df.columns)}")
    
    # Column Data Types
    print("\n   • Column Data Types (df.dtypes):")
    print(df.dtypes)
    
    # Selecting a single column (returns a Series)
    print("\n   • Selecting single column (df['Name'].head()):")
    print(df['Name'].head())
    
    # Selecting multiple columns (returns a DataFrame)
    print("\n   • Selecting multiple columns (df[['Name', 'Math_Score', 'Science_Score']].head()):")
    print(df[['Name', 'Math_Score', 'Science_Score']].head())

    print_separator()

    # --- 4. EXPLORING DATASET INFORMATION ---
    print("4. EXPLORING DATASET INFORMATION:")
    
    # Dataset Shape (rows, columns)
    print(f"\n   • Dataset Shape (df.shape): {df.shape} ({df.shape[0]} rows, {df.shape[1]} columns)")
    
    # Detailed Info (dtypes, non-null counts, memory usage)
    print("\n   • Dataset Info Summary (df.info()):")
    # Capturing and printing df.info()
    df.info()
    
    # Check for Null/Missing values
    print("\n   • Missing values count per column (df.isnull().sum()):")
    print(df.isnull().sum())
    
    # Descriptive Statistics
    print("\n   • Statistical Summary (df.describe()):")
    print(df.describe())

    print_separator()

    # --- 5. MINI-CHALLENGE / QUIZ ---
    print("💡 MINI-CHALLENGE: Pandas Dataset Exploration!")
    score = 0
    
    # Question 1
    print("\nQuestion 1: Which Pandas function/method is used to load a CSV file?")
    print("   a) pd.load_csv()")
    print("   b) pd.read_csv()")
    print("   c) pd.open_csv()")
    ans1 = input("Your answer (a, b, or c): ").strip().lower()
    if ans1 == "b":
        print("   ✅ Correct! pd.read_csv() is the standard function to read CSVs.")
        score += 1
    else:
        print("   ❌ Incorrect. The correct function is pd.read_csv().")
        
    # Question 2
    print("\nQuestion 2: What is the shape of our 'student_scores.csv' dataset?")
    print(f"   a) (30, 9)")
    print(f"   b) (50, 5)")
    print(f"   c) (10, 10)")
    ans2 = input("Your answer (a, b, or c): ").strip().lower()
    if ans2 == "a":
        print(f"   ✅ Correct! The shape is indeed {df.shape} (30 rows, 9 columns).")
        score += 1
    else:
        print(f"   ❌ Incorrect. The correct shape is (30, 9).")
        
    # Question 3
    print("\nQuestion 3: Which method returns summary statistics (mean, min, max, std) for numerical columns?")
    print("   a) df.info()")
    print("   b) df.stats()")
    print("   c) df.describe()")
    ans3 = input("Your answer (a, b, or c): ").strip().lower()
    if ans3 == "c":
        print("   ✅ Correct! df.describe() computes key summary statistics.")
        score += 1
    else:
        print("   ❌ Incorrect. The correct method is df.describe().")
        
    print(f"\nYour score: {score}/3")
    if score == 3:
        print("🎉 Outstanding! You are ready to start analyzing datasets with Pandas!")
    else:
        print("👍 Nice try! Review the printouts above and try again.")
    print("==============================================================\n")

if __name__ == "__main__":
    run_lesson()
