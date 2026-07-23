# Day 6/data_visualization.py
"""
Pandas & Matplotlib Lesson 3: Data Visualization using Matplotlib
-----------------------------------------------------------------
Data visualization is the graphical representation of information and data.
By using visual elements like charts, graphs, and maps, data visualization tools
provide an accessible way to see and understand trends, outliers, and patterns.

In this lesson, we will cover:
1. Setting up Matplotlib (Headless mode for scripts)
2. Creating Scatter Plots (representing correlations)
3. Creating Grouped Bar Charts (comparing categorical metrics)
4. Creating Line Charts (representing trends across continuous variables)
5. Customizing Plots (titles, labels, colors, grids, and legends)
6. Saving Plots as high-quality image files
"""

import os
import pandas as pd
import numpy as np

# Set matplotlib backend to 'Agg' before importing pyplot to allow headless execution (no GUI window required)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def print_separator(title=None):
    if title:
        print("\n" + "="*25 + f" {title} " + "="*25 + "\n")
    else:
        print("\n" + "="*70 + "\n")

def run_lesson():
    print("==============================================================")
    print("      📊 LESSON 3: DATA VISUALIZATION WITH MATPLOTLIB 📊      ")
    print("==============================================================")
    
    # Resolve paths relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_csv_path = os.path.join(os.path.dirname(current_dir), "Day 5", "cleaned_student_scores.csv")
    
    # Ensure Day 6 output folder exists
    os.makedirs(current_dir, exist_ok=True)
    
    # --- 1. LOAD THE CLEANED DATASET ---
    print_separator("1. LOADING CLEANED DATASET")
    try:
        df = pd.read_csv(cleaned_csv_path)
        print("   ✅ Cleaned dataset loaded successfully!")
        print(f"   📊 Dataset Shape: {df.shape} (rows, columns)")
    except FileNotFoundError:
        print(f"   ❌ Error: '{cleaned_csv_path}' not found. Please run Day 5 first to prepare it.")
        return

    # --- 2. SCATTER PLOT: STUDY HOURS VS MATH SCORE ---
    print_separator("2. CREATING SCATTER PLOT (CORRELATION)")
    print("   • Objective: Explore the relationship between study hours and math scores.")
    print("   • Saving: scatter_study_vs_math.png")
    
    plt.figure(figsize=(8, 6))
    
    # Plot scatter points
    plt.scatter(
        df['Study_Hours_Per_Week'], 
        df['Math_Score'], 
        color='#008080',      # Teal color
        alpha=0.7, 
        edgecolors='black', 
        s=80, 
        label='Student Data'
    )
    
    # Calculate and plot a trend line (line of best fit) using numpy
    x = df['Study_Hours_Per_Week']
    y = df['Math_Score']
    m, c = np.polyfit(x, y, 1) # y = mx + c
    plt.plot(x, m*x + c, color='#d9534f', linestyle='--', linewidth=2, label=f'Trendline (slope={m:.2f})')
    
    # Customizations
    plt.title('Study Hours vs. Math Score Correlation', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Study Hours Per Week', fontsize=12)
    plt.ylabel('Math Score', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='lower right')
    
    # Save the figure
    scatter_img_path = os.path.join(current_dir, "scatter_study_vs_math.png")
    plt.tight_layout()
    plt.savefig(scatter_img_path, dpi=300)
    plt.close()
    print(f"   ✅ Scatter plot saved to: {scatter_img_path}")

    # --- 3. BAR CHART: AVERAGE SCORES BY GENDER ---
    print_separator("3. CREATING GROUPED BAR CHART (COMPARISON)")
    print("   • Objective: Compare average Math, Science, and English scores by Gender.")
    print("   • Saving: bar_avg_scores_by_gender.png")
    
    # Group by Gender and calculate averages
    gender_avg = df.groupby('Gender')[['Math_Score', 'Science_Score', 'English_Score']].mean()
    print("\n   • Computed Averages by Gender:")
    print(gender_avg)
    
    # Plot setup
    genders = gender_avg.index
    x_indices = np.arange(len(genders))
    bar_width = 0.25
    
    plt.figure(figsize=(9, 6))
    
    # Plot each subject's average side-by-side
    plt.bar(x_indices - bar_width, gender_avg['Math_Score'], width=bar_width, color='#ff7f0e', label='Math Avg', edgecolor='black', alpha=0.85)
    plt.bar(x_indices, gender_avg['Science_Score'], width=bar_width, color='#2ca02c', label='Science Avg', edgecolor='black', alpha=0.85)
    plt.bar(x_indices + bar_width, gender_avg['English_Score'], width=bar_width, color='#1f77b4', label='English Avg', edgecolor='black', alpha=0.85)
    
    # Customizations
    plt.title('Average Academic Scores by Gender', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Gender Group', fontsize=12)
    plt.ylabel('Average Score (0-100)', fontsize=12)
    plt.xticks(x_indices, genders, fontsize=11)
    plt.ylim(0, 110) # extra padding at the top for labels
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Add numerical labels on top of each bar
    for idx in x_indices:
        # Math labels
        plt.text(idx - bar_width, gender_avg['Math_Score'].iloc[idx] + 2, f"{gender_avg['Math_Score'].iloc[idx]:.1f}", ha='center', fontsize=9, fontweight='semibold')
        # Science labels
        plt.text(idx, gender_avg['Science_Score'].iloc[idx] + 2, f"{gender_avg['Science_Score'].iloc[idx]:.1f}", ha='center', fontsize=9, fontweight='semibold')
        # English labels
        plt.text(idx + bar_width, gender_avg['English_Score'].iloc[idx] + 2, f"{gender_avg['English_Score'].iloc[idx]:.1f}", ha='center', fontsize=9, fontweight='semibold')
        
    plt.legend(loc='upper right')
    
    # Save the figure
    bar_img_path = os.path.join(current_dir, "bar_avg_scores_by_gender.png")
    plt.tight_layout()
    plt.savefig(bar_img_path, dpi=300)
    plt.close()
    print(f"   ✅ Bar chart saved to: {bar_img_path}")

    # --- 4. LINE CHART: PERFORMANCE TREND BY STUDY HOUR BRACKETS ---
    print_separator("4. CREATING LINE CHART (TRENDS)")
    print("   • Objective: Track average exam performance as study hours scale up.")
    print("   • Saving: line_scores_trend_by_study_hours.png")
    
    # Bin study hours into small categories to find clear trends, e.g. round study hours to nearest integer
    df['Study_Hour_Group'] = df['Study_Hours_Per_Week'].round()
    
    # Group by Study Hour Group and compute mean
    trend_data = df.groupby('Study_Hour_Group')[['Math_Score', 'Science_Score', 'English_Score']].mean().sort_index()
    print("\n   • Computed Averages by Study Hours (Rounded):")
    print(trend_data.head())
    
    plt.figure(figsize=(10, 6))
    
    # Plot lines with custom markers and styles
    plt.plot(trend_data.index, trend_data['Math_Score'], marker='o', color='#ff7f0e', linestyle='-', linewidth=2.5, label='Math Score Trend')
    plt.plot(trend_data.index, trend_data['Science_Score'], marker='s', color='#2ca02c', linestyle='-.', linewidth=2.5, label='Science Score Trend')
    plt.plot(trend_data.index, trend_data['English_Score'], marker='^', color='#1f77b4', linestyle=':', linewidth=2.5, label='English Score Trend')
    
    # Customizations
    plt.title('Score Averages vs. Weekly Study Hours', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Weekly Study Hours (Rounded)', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='lower right')
    
    # Save the figure
    line_img_path = os.path.join(current_dir, "line_scores_trend_by_study_hours.png")
    plt.tight_layout()
    plt.savefig(line_img_path, dpi=300)
    plt.close()
    print(f"   ✅ Line chart saved to: {line_img_path}")

    # --- 5. MINI-CHALLENGE / QUIZ ---
    print_separator("💡 DAY 6 QUIZ: DATA VISUALIZATION IN MATPLOTLIB")
    score = 0
    
    # Question 1
    print("\nQuestion 1: Which matplotlib function is used to create a scatter plot?")
    print("   a) plt.plot()")
    print("   b) plt.scatter()")
    print("   c) plt.barplot()")
    ans1 = input("Your answer (a, b, or c): ").strip().lower()
    if ans1 == "b":
        print("   ✅ Correct! plt.scatter() creates point-wise bivariate plots.")
        score += 1
    else:
        print("   ❌ Incorrect. plt.scatter() is used for scatter plots; plt.plot() is for line plots.")
        
    # Question 2
    print("\nQuestion 2: What is the purpose of setting matplotlib.use('Agg') before importing pyplot?")
    print("   a) It makes plots look nicer by applying a custom CSS style.")
    print("   b) It allows running the script headlessly, saving figures directly without needing a graphical window/GUI.")
    print("   c) It increases plot saving speed by 10x.")
    ans2 = input("Your answer (a, b, or c): ").strip().lower()
    if ans2 == "b":
        print("   ✅ Correct! 'Agg' is a non-interactive backend that writes figures directly to disk.")
        score += 1
    else:
        print("   ❌ Incorrect. The 'Agg' backend handles headless execution, preventing errors in terminal shells.")
        
    # Question 3
    print("\nQuestion 3: How do you save a matplotlib plot to a file on your computer?")
    print("   a) plt.show('filename.png')")
    print("   b) plt.write_image('filename.png')")
    print("   c) plt.savefig('filename.png')")
    ans3 = input("Your answer (a, b, or c): ").strip().lower()
    if ans3 == "c":
        print("   ✅ Correct! plt.savefig() is the standard command to save plots.")
        score += 1
    else:
        print("   ❌ Incorrect. plt.savefig() writes the active Figure to disk.")
        
    print(f"\nYour score: {score}/3")
    if score == 3:
        print("🎉 Outstanding! You are fully equipped to visualize dataset trends with Matplotlib!")
    else:
        print("👍 Nice try! Review the outputs, check the generated images, and run again.")
    print("==============================================================\n")

if __name__ == "__main__":
    run_lesson()
