# Day 3/numpy_exercises.py
"""
NumPy Exercises: Practice Calculations
--------------------------------------
This script guides you through four practical array-based calculations.
It outputs the steps and calculations so you can see how NumPy is applied
in data science and machine learning.
"""

import numpy as np

def run_exercise_1():
    print("\n--- Exercise 1: Z-Score Normalization (Standardization) ---")
    print("Normalizing features is crucial in ML so no feature dominates.")
    print("Formula: Z = (X - mean) / std_dev")
    
    # Dataset (e.g. weights of items)
    X = np.array([55.0, 80.0, 45.0, 95.0, 60.0, 70.0])
    print(f"Original Dataset: {X}")
    
    # Calculate stats
    mean = np.mean(X)
    std = np.std(X)
    print(f"Calculated Mean: {mean:.2f} | Standard Deviation: {std:.2f}")
    
    # Normalize
    Z = (X - mean) / std
    print(f"Standardized Dataset (Z-scores):\n  {Z}")
    print(f"New Mean: {np.mean(Z):.2f} (Should be 0.00) | New Std Dev: {np.std(Z):.2f} (Should be 1.00)")

def run_exercise_2():
    print("\n--- Exercise 2: ReLU Activation (Clamping Negatives to 0) ---")
    print("In Neural Networks, the ReLU activation function sets all negative values to zero.")
    print("Formula: ReLU(x) = max(0, x)")
    
    # Raw layer weights/inputs
    inputs = np.array([
        [-1.5,  2.0, -0.5],
        [ 3.1, -2.2,  0.0],
        [-0.1,  4.5, -9.9]
    ])
    print("Raw Layer Inputs:")
    print(inputs)
    
    # Apply ReLU using boolean indexing
    outputs = inputs.copy()
    outputs[outputs < 0] = 0
    print("\nAfter ReLU Activation (outputs[outputs < 0] = 0):")
    print(outputs)
    
    # Alternative using np.maximum:
    # outputs_alt = np.maximum(0, inputs)

def run_exercise_3():
    print("\n--- Exercise 3: Linear Regression Prediction (Y_pred = X @ W + B) ---")
    print("Compute linear regression predictions for 3 houses.")
    print("Features (Size in 1000 sqft, Number of rooms): X")
    print("Weights (W) and Bias (B):")
    
    X = np.array([
        [1.5, 3],  # House 1
        [2.4, 4],  # House 2
        [0.9, 2]   # House 3
    ])
    W = np.array([100, 20])  # weights for sqft and rooms (in $1000s)
    B = 50                  # base price bias (in $1000s)
    
    print("House Features matrix X (3x2):")
    print(X)
    print(f"Weight Vector W: {W}")
    print(f"Bias B: {B}")
    
    # Calculate predicted prices: Y = X @ W + B
    predictions = (X @ W) + B
    print(f"\nPredicted House Prices (in $1000s): {predictions}")
    for i, price in enumerate(predictions, 1):
        print(f"  House {i}: ${price:,.2f}k")

def run_exercise_4():
    print("\n--- Exercise 4: Filtering Outliers (Standard Deviations) ---")
    print("Find data points that are outliers (more than 2 standard deviations from the mean).")
    
    # Height measurements in cm
    data = np.array([170, 172, 168, 250, 174, 169, 110, 171]) # 250 and 110 are outliers
    print(f"Data: {data}")
    
    mean = np.mean(data)
    std = np.std(data)
    print(f"Mean: {mean:.2f} | Std Dev: {std:.2f}")
    
    # Outlier criteria: absolute difference from mean is greater than 2 * std
    difference = np.abs(data - mean)
    outliers = data[difference > 2 * std]
    normal_data = data[difference <= 2 * std]
    
    print(f"\nOutliers (diff > 2*std): {outliers}")
    print(f"Normal Data (diff <= 2*std): {normal_data}")

def main():
    print("====================================================")
    print("           📊 NUMPY PRACTICE EXERCISES 📊           ")
    print("====================================================")
    
    while True:
        print("\nPractice Options:")
        print("1. Z-Score Normalization")
        print("2. ReLU Activation (Clamping Negatives)")
        print("3. Linear Regression Prediction (Matrix Multiply)")
        print("4. Outlier Filtering")
        print("5. Run All Exercises")
        print("6. Exit")
        
        choice = input("\nSelect an exercise to run (1-6): ").strip()
        
        if choice == '1':
            run_exercise_1()
        elif choice == '2':
            run_exercise_2()
        elif choice == '3':
            run_exercise_3()
        elif choice == '4':
            run_exercise_4()
        elif choice == '5':
            run_exercise_1()
            run_exercise_2()
            run_exercise_3()
            run_exercise_4()
        elif choice == '6':
            print("\nExiting exercises. Great practice today! 🚀")
            break
        else:
            print("❌ Invalid selection. Please enter a number between 1 and 6.")
            
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()
