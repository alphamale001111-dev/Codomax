# Day 3/numpy_arrays.py
"""
NumPy Lesson 1: NumPy Arrays Creation and Attributes
----------------------------------------------------
NumPy (Numerical Python) is the fundamental package for scientific computing in Python.
The core data structure in NumPy is the ndarray (n-dimensional array), which is a table of elements
(usually numbers), all of the same type, indexed by a tuple of non-negative integers.
"""

import numpy as np

def print_separator():
    print("\n" + "="*60 + "\n")

def run_lesson():
    print("============================================================")
    print("        🐍 LESSON 1: NUMPY ARRAY CREATION & PROPERTIES 🐍   ")
    print("============================================================")
    
    # --- 1. CREATING ARRAYS FROM PYTHON LISTS ---
    print("\n1. CREATING ARRAYS FROM LISTS:")
    py_list = [1, 2, 3, 4, 5]
    arr_1d = np.array(py_list)
    print(f"   Python List: {py_list} | Type: {type(py_list)}")
    print(f"   NumPy 1D Array: {arr_1d} | Type: {type(arr_1d)}")
    
    # Creating a 2D Array (Matrix)
    py_matrix = [[1, 2, 3], [4, 5, 6]]
    arr_2d = np.array(py_matrix)
    print(f"\n   NumPy 2D Array (Matrix):\n{arr_2d}")

    print_separator()

    # --- 2. ARRAY CREATION HELPERS ---
    print("2. NUMPY BUILT-IN CREATION FUNCTIONS:")
    
    # Array of Zeros
    zeros = np.zeros((2, 3))
    print(f"   • np.zeros((2, 3)) - float zeros:\n{zeros}")
    
    # Array of Ones
    ones = np.ones((3, 2), dtype=int)
    print(f"\n   • np.ones((3, 2), dtype=int) - integer ones:\n{ones}")
    
    # Sequential range (similar to Python's range)
    seq = np.arange(0, 10, 2)
    print(f"\n   • np.arange(0, 10, 2) - start, stop, step:\n     {seq}")
    
    # Linearly spaced numbers
    lin = np.linspace(0, 1, 5)
    print(f"\n   • np.linspace(0, 1, 5) - 5 evenly spaced numbers between 0 and 1:\n     {lin}")
    
    # Random arrays
    rand_float = np.random.rand(2, 2)
    print(f"\n   • np.random.rand(2, 2) - uniform float random [0, 1):\n{rand_float}")
    
    rand_int = np.random.randint(1, 100, size=5)
    print(f"\n   • np.random.randint(1, 100, size=5) - random integers:\n     {rand_int}")

    print_separator()

    # --- 3. KEY ARRAY PROPERTIES ---
    print("3. NDARRAY PROPERTIES (ATTRIBUTES):")
    a = np.array([[10, 20, 30], [40, 50, 60]])
    print(f"   Array:\n{a}")
    print(f"   • Shape (dimensions size):   a.shape  = {a.shape} (2 rows, 3 columns)")
    print(f"   • Dimensions count:          a.ndim   = {a.ndim}D")
    print(f"   • Total elements count:      a.size   = {a.size}")
    print(f"   • Data type of elements:     a.dtype  = {a.dtype}")
    print(f"   • Memory size of one item:   a.itemsize = {a.itemsize} bytes")

    print_separator()

    # --- 4. MINI-CHALLENGE ---
    print("💡 MINI-CHALLENGE: NumPy Arrays!")
    score = 0
    
    # Question 1
    print("Question 1: You run the code: arr = np.zeros((4, 5))")
    ans1 = input("What will be the output of arr.ndim? (Enter a number): ").strip()
    if ans1 == "2":
        print("   ✅ Correct! (4, 5) defines a 2D array, so the number of dimensions is 2.")
        score += 1
    else:
        print("   ❌ Incorrect. The dimensions count is 2 (2D array/matrix).")
        
    # Question 2
    print("\nQuestion 2: You run the code: arr = np.arange(1, 10, 3)")
    ans2 = input("What values will be in arr? (Format: 1, 4, 7 or similar): ").strip().replace(" ", "")
    if ans2 in ["1,4,7", "[1,4,7]"]:
        print("   ✅ Correct! np.arange start=1, stop=10 (exclusive), step=3 generates [1, 4, 7].")
        score += 1
    else:
        print("   ❌ Incorrect. It generates values starting at 1, increasing by 3, up to less than 10 (i.e. 1, 4, 7).")
        
    print(f"\nYour score: {score}/2")
    if score == 2:
        print("🎉 Great Job! You understand how to create and inspect NumPy arrays!")
    else:
        print("👍 Good try! Review the code examples and run again.")
    print("============================================================\n")

if __name__ == "__main__":
    run_lesson()
