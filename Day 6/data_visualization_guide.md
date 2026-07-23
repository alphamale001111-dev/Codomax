# 📊 Data Visualization with Matplotlib (Day 6)

Welcome to Day 6 of your data science journey! Today, we transition from reading and cleaning tabular data to **Data Visualization**, the powerful art of converting raw data numbers into graphical insights. 

Visualizations help identify trends, correlations, outliers, and distributions in a way that tables of numbers cannot. We will be using **Matplotlib**, the foundational data visualization library in Python.

---

## ⚡ Key Concepts of Matplotlib

### 1. The Anatomy of a Plot
A Matplotlib visualization contains two main layers:
*   **Figure (`plt.figure`)**: The overall container/canvas that holds all plot elements (titles, legends, and axes).
*   **Axes (Subplots)**: The actual plotting area where data points are drawn, containing x and y coordinates.

### 2. Core Plotting Methods
*   **Scatter Plot (`plt.scatter(x, y)`)**: Represents individual data points. Excellent for showing relationships/correlations between two continuous numerical variables.
*   **Bar Chart (`plt.bar(x, height)`)**: Uses vertical/horizontal bars. Excellent for comparing categorical variables or distinct group metrics.
*   **Line Chart (`plt.plot(x, y)`)**: Draws lines connecting data points. Ideal for showing continuous trends, such as data changes over time or ascending values.

### 3. Plot Customizations
To make plots readable and professional, always apply these standards:
*   **Labels & Titles**: `plt.xlabel()`, `plt.ylabel()`, and `plt.title()` to give context.
*   **Legends**: `plt.legend()` to identify multiple lines or bar groups.
*   **Grids**: `plt.grid(True, linestyle='--', alpha=0.5)` to help read precise coordinates.
*   **Layout Safety**: `plt.tight_layout()` to automatically adjust subplot parameters so titles and labels don't clip.

### 4. Headless Execution (Backend Setup)
When running Python scripts on remote servers, containers, or terminal prompts without a GUI desktop display:
```python
import matplotlib
matplotlib.use('Agg') # Enable headless, non-interactive backend
import matplotlib.pyplot as plt
```
This prevents errors by forcing Matplotlib to write figures directly to files instead of attempting to open a popup window.

---

## 📚 Day 6 Curriculum & Files

We have created an interactive lesson that loads the cleaned student scores from Day 5 and plots several charts.

### 📁 Files Created:
1. **`Day 6/data_visualization.py`**: An interactive Python script that creates a scatter plot, grouped bar chart, and line chart, saves them as PNGs, and quizzes your understanding.
2. **`Day 6/data_visualization_guide.md`**: This learning reference guide.
3. **`Day 6/scatter_study_vs_math.png`**: Scatter plot comparing Study Hours vs. Math Score.
4. **`Day 6/bar_avg_scores_by_gender.png`**: Grouped bar chart comparing subject averages across gender.
5. **`Day 6/line_scores_trend_by_study_hours.png`**: Line chart showing grade trends as study hours increase.

---

## 🚀 Running the Interactive Lesson

To run today's interactive lesson and generate the charts, execute the following command in your terminal:

```bash
.venv/bin/python3 "Day 6/data_visualization.py"
```

Once run, look at the folder `Day 6/` to inspect the generated charts!
