# Day 3/numpy_math.py
"""
NumPy Lesson 3: Mathematical Operations and Vectorization
---------------------------------------------------------
NumPy is incredibly fast because of "vectorization" — operations run on whole arrays
in native C code without explicit loops. This file teaches arithmetic,
aggregate statistical functions, axis calculations, and matrix operations.
"""

import numpy as np

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("        🐍 LESSON 3: NUMPY MATHEMATICAL OPERATIONS 🐍        ")
    print("============================================================")
    
    # --- 1. ELEMENT-WISE ARITHMETIC ---
    print("\n1. ELEMENT-WISE ARITHMETIC:")
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print(f"   x = {x} | y = {y}")
    print(f"   • Addition (x + y):        {x + y}")
    print(f"   • Subtraction (x - y):     {x - y}")
    print(f"   • Multiplication (x * y):  {x * y}  (Note: Element-wise, not matrix dot product!)")
    print(f"   • Power (x ** 2):          {x ** 2}")

    print_separator()

    # --- 2. UNIVERSAL FUNCTIONS (UFUNCS) ---
    print("2. UNIVERSAL FUNCTIONS (Vectorized Math helpers):")
    arr = np.array([1, 4, 9])
    print(f"   arr = {arr}")
    print(f"   • Square Root (np.sqrt(arr)): {np.sqrt(arr)}")
    print(f"   • Exponential (np.exp(x)):    {np.exp(x)}")
    print(f"   • Logarithm (np.log(arr)):    {np.log(arr)}")

    print_separator()

    # --- 3. AGGREGATES & STATISTICS (AXIS SELECTION) ---
    print("3. AGGREGATE FUNCTIONS & THE 'AXIS' PARAMETER:")
    matrix = np.array([
        [1, 2],
        [3, 4]
    ])
    print(f"   Matrix:\n{matrix}")
    print(f"\n   • Total Sum (np.sum(matrix)):                {np.sum(matrix)}")
    print(f"   • Mean (np.mean(matrix)):                    {np.mean(matrix)}")
    print(f"   • Std Deviation (np.std(matrix)):            {np.std(matrix):.4f}")
    
    # Axis-based calculations:
    # axis=0 -> Column-wise (down rows)
    # axis=1 -> Row-wise (across columns)
    print(f"\n   • Column-wise Sum (np.sum(matrix, axis=0)):  {np.sum(matrix, axis=0)}")
    print(f"   • Row-wise Sum (np.sum(matrix, axis=1)):     {np.sum(matrix, axis=1)}")

    print_separator()

    # --- 4. MATRIX MULTIPLICATION ---
    print("4. MATRIX MULTIPLICATION (DOT PRODUCT):")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[2, 0], [1, 2]])
    print(f"   Matrix A:\n{a}")
    print(f"   Matrix B:\n{b}")
    
    # Multiplying using @ or np.dot
    matmul = a @ b
    print(f"\n   • Dot Product (a @ b):\n{matmul}")

    print_separator()

    # --- 5. BROADCASTING ---
    print("5. BROADCASTING (Arithmetic on arrays of different shapes):")
    grid = np.array([[10, 20, 30], [40, 50, 60]])
    row = np.array([1, 2, 3])
    print(f"   Grid (2x3):\n{grid}")
    print(f"   Row (1x3): {row}")
    
    # NumPy stretches the row to match the grid shape automatically!
    broadcasted = grid + row
    print(f"\n   • Broadcasted Addition (grid + row):\n{broadcasted}")

    print_separator()

    # --- 6. MINI-CHALLENGE ---
    print("💡 MINI-CHALLENGE: NumPy Math!")
    score = 0
    
    # Question 1
    print("Question 1: Let A = np.array([[1, 2], [3, 4]])")
    print("If you run: res = np.max(A, axis=0)")
    ans1 = input("What is the output? (Format: [3, 4] or similar): ").strip().replace(" ", "")
    if ans1 in ["[3,4]", "3,4", "array([3,4])"]:
        print("   ✅ Correct! axis=0 compares items down columns, so max of [1, 3] is 3, and max of [2, 4] is 4.")
        score += 1
    else:
        print("   ❌ Incorrect. Down the columns (axis=0), the maximum values are 3 and 4.")
        
    # Question 2
    print("\nQuestion 2: If x = np.array([1, 2]) and y = np.array([3, 4])")
    ans2 = input("What does x * y evaluate to? (Format: [3, 8] or similar): ").strip().replace(" ", "")
    if ans2 in ["[3,8]", "3,8", "array([3,8])"]:
        print("   ✅ Correct! Element-wise multiplication: 1*3=3 and 2*4=8.")
        score += 1
    else:
        print("   ❌ Incorrect. Element-wise multiplication yields [3, 8].")
        
    print(f"\nYour score: {score}/2")
    if score == 2:
        print("🎉 Math Wiz! You understand the mathematical power of NumPy!")
    else:
        print("👍 Good try! Review array math operations and run again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
