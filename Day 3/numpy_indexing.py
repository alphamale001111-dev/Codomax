# Day 3/numpy_indexing.py
"""
NumPy Lesson 2: Indexing, Slicing, and Boolean Masking
------------------------------------------------------
Accessing and filtering array data. Unlike Python lists, NumPy indexing supports
multi-dimensional notation and boolean logical masking, which allows fast filtering.
"""

import numpy as np

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("        🐍 LESSON 2: INDEXING, SLICING & MASKING 🐍        ")
    print("============================================================")
    
    # --- 1. 1D ARRAY INDEXING & SLICING ---
    print("\n1. 1D ARRAY INDEXING & SLICING:")
    arr = np.array([10, 20, 30, 40, 50])
    print(f"   Array: {arr}")
    print(f"   • Element at index 0 (arr[0]):       {arr[0]}")
    print(f"   • Last element (arr[-1]):           {arr[-1]}")
    print(f"   • Slice index 1 to 4 (arr[1:4]):    {arr[1:4]}")
    print(f"   • Reverse array (arr[::-1]):        {arr[::-1]}")

    print_separator()

    # --- 2. 2D ARRAY INDEXING & SLICING ---
    print("2. 2D ARRAY INDEXING & SLICING:")
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(f"   Matrix:\n{matrix}")
    print(f"\n   • Access single element (row 1, col 2) [matrix[1, 2]]: {matrix[1, 2]}")
    print(f"   • Access entire Row 0 [matrix[0, :]]:                 {matrix[0, :]}")
    print(f"   • Access entire Column 1 [matrix[:, 1]]:              {matrix[:, 1]}")
    print(f"   • Access sub-grid (rows 0-1, cols 1-2) [matrix[:2, 1:]]:\n{matrix[:2, 1:]}")

    print_separator()

    # --- 3. BOOLEAN INDEXING (LOGICAL MASKING) ---
    print("3. BOOLEAN INDEXING (POWERFUL FILTERING):")
    data = np.array([12, 45, 8, 19, 3, 27, 88])
    print(f"   Data Array: {data}")
    
    # Generate boolean mask
    mask = data > 20
    print(f"   • Mask condition (data > 20):\n     {mask}")
    
    # Apply mask
    filtered_data = data[mask]
    print(f"   • Filtered data (data[data > 20]):\n     {filtered_data}")

    print_separator()

    # --- 4. VIEW VS COPY (MUTATING SUBSETS) ---
    print("4. ARRAY VIEWS VS COPIES:")
    base = np.array([1, 2, 3, 4])
    print(f"   Base Array: {base}")
    
    # Slicing creates a 'view' - modifying it changes the original!
    view_slice = base[:2]
    view_slice[0] = 99
    print(f"   • After modifying view slice (view_slice[0] = 99):")
    print(f"     View: {view_slice} | Base Array (changed!): {base}")
    
    # Use .copy() to create an independent copy
    base2 = np.array([1, 2, 3, 4])
    copied_slice = base2[:2].copy()
    copied_slice[0] = 99
    print(f"\n   • After modifying explicit copy (copied_slice[0] = 99):")
    print(f"     Copy: {copied_slice} | Base Array (unchanged): {base2}")

    print_separator()

    # --- 5. MINI-CHALLENGE ---
    print("💡 MINI-CHALLENGE: Slicing & Sifting!")
    score = 0
    
    # Question 1
    print("Question 1: Given this matrix:")
    print("   arr = np.array([[10, 20], [30, 40]])")
    ans1 = input("What syntax extracts the second column? (e.g. arr[?, ?]): ").strip().replace(" ", "")
    if ans1 in ["arr[:,1]", "arr[:,-1]"]:
        print("   ✅ Correct! Using : selects all rows, and 1 selects the second column.")
        score += 1
    else:
        print("   ❌ Incorrect. The syntax is: arr[:, 1]")
        
    # Question 2
    print("\nQuestion 2: Given: data = np.array([5, 10, 15, 20])")
    print("What will be the output of: data[data % 10 == 0]")
    ans2 = input("Enter output (format: [10, 20] or similar): ").strip().replace(" ", "")
    if ans2 in ["[10,20]", "10,20", "array([10,20])"]:
        print("   ✅ Correct! 10 and 20 are the numbers divisible by 10 in the array.")
        score += 1
    else:
        print("   ❌ Incorrect. The output is [10, 20].")
        
    print(f"\nYour score: {score}/2")
    if score == 2:
        print("🎉 Slicing Star! You have conquered indexing and filtering!")
    else:
        print("👍 Good try! Review slice behavior and run again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
