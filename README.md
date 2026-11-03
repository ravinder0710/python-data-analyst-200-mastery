# 🐍 Python for Data Analysis & Interview Mastery — 200 Questions Challenge
### (Target: Fresher & Junior Data Analyst | 0 — 1 Year Experience)

![Python Challenge](https://img.shields.io/badge/Python-200_Questions_Challenge-blue.svg)
![Target Role](https://img.shields.io/badge/Role-Data_Analyst_%280--1_Year%29-orange.svg)
![Progress](https://img.shields.io/badge/Progress-10%2F200_%285%25%29-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-In_Progress-brightgreen.svg)

A production-grade, highly curated repository containing **200 practical Python coding & data analysis interview questions** designed strictly for **Fresher & 0-1 Year Data Analyst** technical rounds, live machine tests, and case-study interviews (TCS, Accenture, Infosys, Amazon, Swiggy, FinTech startups).

---

## 🗂️ Module-Wise Curriculum & Progress Tracker (10 / 200)

| Module | Category / Focus Area | Target | Completed | Progress Status |
|:---:|:---|:---:|:---:|:---|
| **01** | **Python Core Basics & Logic** (Data types, string methods, slicing, dicts, loops, puzzles) | 50 | 10 | `[██░░░░░░░░] 20%` |
| **02** | **Pandas Mastery** (Dataframes, cleaning, nulls, loc/iloc, GroupBy, merge, pivot_table) | 60 | 0 | `[░░░░░░░░░░] 0%` |
| **03** | **NumPy & Basic Statistics** (Arrays, broadcasting, np.where, IQR, percentiles, correlation) | 50 | 0 | `[░░░░░░░░░░] 0%` |
| **04** | **Data Visualization & EDA** (Matplotlib, Seaborn, distributions, heatmaps, subplots) | 20 | 0 | `[░░░░░░░░░░] 0%` |
| **05** | **Real Business Scenarios** (AOV, Churn, Pareto 80/20, MoM/YoY Growth, RFM Segmentation) | 20 | 0 | `[░░░░░░░░░░] 0%` |
| **TOTAL** | **5 Core Analytical Modules** | **200** | **10** | **10 / 200 (5%)** |

---

## 📁 Repository Structure

```text
python-data-analyst-200-mastery/
├── README.md                                 # Master Curriculum & 200 Progress Tracker
├── INTERVIEW_QUICK_REVISION_NOTES.md         # Formula & Interviewer Defense Cheat Sheet
├── 01_Python_Core_Basics_and_Logic/          # (Q001 - Q050) Coding fluency & core logic
├── 02_Pandas_Mastery/                        # (Q051 - Q110) End-to-end data wrangling
├── 03_NumPy_and_Basic_Statistics/            # (Q111 - Q160) Array math, stats & outliers
├── 04_Data_Visualization_and_EDA/            # (Q161 - Q180) Exploratory charts & storytelling
└── 05_Real_Business_Scenarios/               # (Q181 - Q200) Real company KPIs & machine tests
```

---

## 📘 Detailed Syllabus Breakdown

### 📘 Module 1: Python Core Basics & Logic (50 Questions)
1. **Data Types & Typecasting**: `int`, `float`, `str`, `bool`, conversion problems, floating precision issue.
2. **String Methods & Cleaning**: `.strip()`, `.split()`, `.join()`, `.lower()`, `.upper()`, `.replace()`, f-strings formatting, slicing tricks.
3. **Lists & Slicing**: Indexing, negative slicing, `append()` vs `extend()`, `pop()`, `remove()`, sorting (`sort()` vs `sorted()`).
4. **Tuples & Sets**: Mutability differences, unique values extraction, set operations (union, intersection, difference).
5. **Dictionaries**: Key-value pairs, safe lookup with `.get()`, updating dicts, inverted dictionaries, `.items()`, `.keys()`.
6. **Loops & Conditions**: `if-elif-else`, nested conditions, `for` loops, `while` loops, `break`, `continue`, `enumerate()`, `zip()`.
7. **Comprehensions**: List comprehensions, Dict comprehensions, conditional filtering in one line.
8. **Functions & Lambdas**: `def`, default arguments, `*args`, `**kwargs`, anonymous `lambda` functions.
9. **Error Handling & File Reading**: `try-except-finally`, reading raw text/CSV files safely.
10. **Interview Live Puzzles**: Character frequency counter, duplicate finder, second largest number, palindrome check, missing number from 1 to N sequence, Two Sum logic.

### 📙 Module 2: Pandas Mastery (60 Questions)
1. **Series vs DataFrame**: Structure, creation from dicts/lists, `.shape`, `.columns`, `.dtypes`.
2. **Data Ingestion & Inspection**: `read_csv()`, `head()`, `tail()`, `.info()`, `.describe()` (5-number summary).
3. **Indexing & Slicing**: `loc` vs `iloc` (stop-index difference), conditional filtering (`&`, `|`, `~`), `.isin()`, `.between()`.
4. **Data Cleaning & Missing Values**: `.isnull().sum()`, percentage of nulls, `.dropna()`, `.fillna()` with Mean/Median/Mode, forward fill (`ffill`).
5. **Duplicates & Data Type Conversion**: `.duplicated()`, `.drop_duplicates()`, `.astype()`, `pd.to_numeric(..., errors='coerce')`.
6. **Pandas String Accessor**: `.str.strip()`, `.str.lower()`, `.str.contains()`, `.str.split()`, `.str.extract()` (regex).
7. **DateTime Operations**: `pd.to_datetime()`, `.dt.year`, `.dt.month`, `.dt.day_name()`, date difference (days).
8. **Sorting & Ranking**: `sort_values()` single/multi-column, `rank()` with `method='dense'` and `method='first'`.
9. **GroupBy & Aggregations**: `.groupby()`, `.agg()`, multiple aggregations (`sum`, `mean`, `count`, `min`, `max`), Named Aggregations.
10. **`transform()` vs `apply()`**: Comparing group mean without row collapse, custom lambda application.
11. **Reshaping Data**: `pivot_table()` with aggregation & margins (totals), `melt()` (wide data to unpivot tall).
12. **Merging & Joins**: `pd.merge()` (Inner, Left, Right, Outer joins), `indicator=True`, `pd.concat()` row-wise & column-wise.

### 📗 Module 3: NumPy & Basic Statistics (50 Questions)
1. **Arrays & Slicing**: `np.array()`, `np.arange()`, `np.linspace()`, 1D/2D arrays, indexing & slicing.
2. **Vectorization & Broadcasting**: Array math without loops, broadcasting rules.
3. **Conditional Logic (SQL CASE-WHEN)**: `np.where()` (IF-ELSE), `np.select()` (Multiple conditions).
4. **Boolean Masking**: Arrays filtering based on condition.
5. **Basic Descriptive Stats**: `np.mean()`, `np.median()`, `np.std()`, `np.var()`, `np.min()`, `np.max()`.
6. **Percentiles & Quantiles**: `np.percentile(25, 50, 75, 90)`, Quantiles calculation.
7. **Outlier Detection via IQR**: Interquartile Range ($Q3 - Q1$), lower fence ($Q1 - 1.5 \times IQR$) & upper fence ($Q3 + 1.5 \times IQR$).
8. **Handling Special Values**: `np.isnan()`, `np.isinf()`, `np.nanmean()`, `np.clip()` (bounding values).
9. **Correlation & Distributions**: `np.corrcoef()`, Pearson correlation, Skewness concept.
10. **Random Sampling**: Reproducible sampling with `np.random.seed()`.

### 📊 Module 4: Data Visualization / EDA (20 Questions)
1. **Matplotlib Structure**: `plt.figure()`, `plt.subplots()`, title, labels, legend, grid, `plt.tight_layout()`.
2. **Line Charts**: Time-series sales trend over months.
3. **Bar Charts & Countplots**: Top categories comparison, frequency distributions.
4. **Histograms & KDE**: Data distribution and skewness inspection.
5. **Box Plots**: Visually identifying outliers and comparing categories.
6. **Scatter Plots**: Two numerical variables correlation & clusters.
7. **Heatmap**: Correlation matrix visually plotted (`annot=True`, color maps).
8. **Multi-panel Subplots**: 2x2 grid charts layout.
9. **Chart Customization**: Axis formatting, data labels on bars, saving high-res chart (`dpi=300`).
10. **Storytelling with Charts**: Removing clutter and explaining business takeaways.

### 💼 Module 5: Real Business Scenarios (20 Questions)
1. **E-commerce KPIs**: Gross Revenue, Net Revenue, Average Order Value (AOV), Units per Order (UPT).
2. **Pareto 80/20 Rule**: Finding top 20% products driving 80% revenue.
3. **Customer Churn Analysis**: Inactive customers identification (no orders in last 60/90 days).
4. **Growth Calculations**: Month-over-Month (MoM) Growth % & Year-over-Year (YoY) Growth %.
5. **Product Return Rate**: High-return products and categories flagging.
6. **Discount Impact**: Analyzing if heavy discounts cause negative gross margins.
7. **Reconciliation & Anomaly**: Detecting duplicate transactions and volume spikes.
8. **RFM Segmentation (Basics)**: Recency, Frequency, Monetary value customer clustering.
9. **Lead Conversion Funnel**: Multi-stage funnel drop-off % calculation.
10. **End-to-End Mini Project**: Complete interview walk-through from raw CSV to executive insights.

---

## 🛠️ File Standards
Each question file (`.py`) contains:
- **Problem Statement & Interview Context**: Real business scenario.
- **Input Data / Test Case**: Ready-to-run data structures.
- **Production Solution**: Clean, idiomatic, PEP-8 compliant Python code.
- **Explanation & Common Traps**: Edge cases, time complexity, and alternative approaches.
