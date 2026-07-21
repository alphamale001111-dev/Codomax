# 📊 Pandas Fundamentals Learning Guide (Day 4)

Welcome to Day 4 of your data science journey! Today, we introduce **Pandas**, the industry-standard Python library for data manipulation and analysis. 

While NumPy handles homogenous numerical grids, Pandas provides high-performance, easy-to-use data structures (Series and DataFrames) designed to work with structured, tabular, or heterogeneous data (like spreadsheets or database tables).

---

## ⚡ Key Concepts of Pandas

1. **Pandas Series**: A 1-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). Think of it as a single column of a table.
2. **Pandas DataFrame**: A 2-dimensional labeled data structure with columns of potentially different types. Think of it as an in-memory SQL table or an Excel spreadsheet.
3. **Data Alignment**: Pandas automatically aligns data based on labels (indexes) when performing operations.
4. **Handling Missing Data**: It has built-in support for cleaning, filtering, and filling missing values (`NaN`).

---

## 📚 Day 4 Curriculum & Lessons

We have created a realistic student score dataset and an interactive script to help you explore and practice loading data.

### 📁 Files Created:
1. **`Day 4/student_scores.csv`**: A CSV dataset containing scores, gender, attendance, and study hours for 30 students.
2. **`Day 4/pandas_exploration.py`**: An interactive Python script demonstrating dataset loading, row/column exploration, and statistical info analysis.

---

## 🔍 Core Exploration Commands Covered

Here are the key commands you will practice and learn about in today's lesson:

### 1. Importing & Loading Data
```python
import pandas as pd

# Load dataset
df = pd.read_csv('Day 4/student_scores.csv')
```

### 2. Exploring Rows
*   `df.head(n)`: View the first `n` rows (defaults to 5).
*   `df.tail(n)`: View the last `n` rows.
*   `df.sample(n)`: Return a random sample of `n` rows.
*   `df.iloc[start:end]`: Slice specific rows using index positions.

### 3. Exploring Columns
*   `df.columns`: List all column names in the dataset.
*   `df.dtypes`: Display data types of each column.
*   `df['Column_Name']`: Select a single column (returns a Series).
*   `df[['Col1', 'Col2']]`: Select multiple columns (returns a DataFrame).

### 4. Exploring Dataset Info & Statistics
*   `df.shape`: Returns a tuple `(rows, columns)`.
*   `df.info()`: Displays non-null counts, data types, and memory usage.
*   `df.describe()`: Generates summary statistics (mean, min, max, standard deviation, quartiles) for all numerical columns.
*   `df.isnull().sum()`: Checks for the count of missing (`NaN`) values per column.

---

## 🚀 Running the Interactive Lesson

To run today's interactive lesson and take the mini-challenge, execute the following command in your terminal:

```bash
.venv/bin/python3 "Day 4/pandas_exploration.py"
```

Explore the printouts, check the outputs, and complete the multiple-choice questions to confirm your understanding!
