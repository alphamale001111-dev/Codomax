# 📊 NumPy Fundamentals Learning Guide (Day 3)

Welcome to Day 3 of your Python journey! Today is all about **NumPy (Numerical Python)**, which is the foundational building block for Data Science, Machine Learning, and Deep Learning in Python.

---

## ⚡ Why NumPy?

In pure Python, lists can store different types, meaning Python has to check each item's type during loops. This causes significant overhead. 

NumPy solves this by introducing the **`ndarray`** (n-dimensional array):
1. **Contiguous Memory**: NumPy arrays are stored in a single, continuous block of memory, allowing quick lookups and caching.
2. **Homogeneous Data**: All elements in a NumPy array must be of the same data type (`dtype`), eliminating type-checking overhead.
3. **Vectorization**: Mathematical operations are passed directly to highly optimized C/Fortran libraries, avoiding Python loops entirely.

---

## 📚 Day 3 Curriculum & Lessons

Each file below is fully commented, runs in the terminal, and includes interactive challenges or exercises.

### 📝 Lessons

1. **NumPy Array Creation & Attributes**
   - **Topics**: Creating arrays from lists, using helpers (`zeros`, `ones`, `arange`, `linspace`, `random`), and inspecting attributes (`shape`, `ndim`, `size`, `dtype`).
   - **Interactive File**: [numpy_arrays.py](file:///Users/d.k./Desktop/Codomax%20internship/Day%203/numpy_arrays.py)
   - **Run Command**:
     ```bash
     .venv/bin/python3 "Day 3/numpy_arrays.py"
     ```

2. **Indexing, Slicing & Masking**
   - **Topics**: Slicing in 1D & 2D arrays, boolean indexing (logical filtering masks), and the difference between views vs copies.
   - **Interactive File**: [numpy_indexing.py](file:///Users/d.k./Desktop/Codomax%20internship/Day%203/numpy_indexing.py)
   - **Run Command**:
     ```bash
     .venv/bin/python3 "Day 3/numpy_indexing.py"
     ```

3. **Mathematical Operations & Universal Functions**
   - **Topics**: Element-wise arithmetic, universal mathematical functions (ufuncs), aggregation methods (sum, mean, std, min, max) with the `axis` parameter, matrix dot products (`@`), and broadcasting.
   - **Interactive File**: [numpy_math.py](file:///Users/d.k./Desktop/Codomax%20internship/Day%203/numpy_math.py)
   - **Run Command**:
     ```bash
     .venv/bin/python3 "Day 3/numpy_math.py"
     ```

---

### 🛠️ Practical Projects (Practice Calculations)

4. **NumPy Practice Calculations**
   - **Topics**: Step-by-step implementations of essential calculations:
     - **Z-Score Normalization (Standardization)**: Feature scaling for machine learning.
     - **ReLU Activation**: Clamping negative inputs to `0` for neural network layers.
     - **Linear Regression Prediction**: Matrix dot product vectorization `(X @ W + B)`.
     - **Outlier Filtering**: Using standard deviations to sift anomalies.
   - **Interactive File**: [numpy_exercises.py](file:///Users/d.k./Desktop/Codomax%20internship/Day%203/numpy_exercises.py)
   - **Run Command**:
     ```bash
     .venv/bin/python3 "Day 3/numpy_exercises.py"
     ```

---

## 🚀 How to Get Started

1. Ensure your terminal is open in the workspace.
2. Run any lesson file using the python interpreter inside your virtual environment (`.venv/bin/python3`). For example:
   ```bash
   .venv/bin/python3 "Day 3/numpy_arrays.py"
   ```
3. Complete the interactive challenges and inspect the source code to read the comments!
