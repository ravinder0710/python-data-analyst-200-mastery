# ⚡ Python for Data Analysts — Quick Interview Revision Notes
### (Cheat Sheet for Live Machine Tests & Technical Rounds)

---

## 1. Core Python Traps & Interview Pearls
- **Mutable vs Immutable**:
  - *Immutable*: `int`, `float`, `str`, `tuple`, `frozenset`. (Cannot be changed in place; modifications create new objects).
  - *Mutable*: `list`, `dict`, `set`. (Can be modified in place. Watch out for default mutable arguments in functions: `def func(a=[])` is a major bug!).
- **`is` vs `==`**:
  - `==` checks value equality (`[1, 2] == [1, 2]` is `True`).
  - `is` checks memory reference identity (`id(a) == id(b)`).
- **List Methods**:
  - `list.append(x)`: Adds `x` as a single element (e.g. appending `[3, 4]` makes `[1, 2, [3, 4]]`).
  - `list.extend(iterable)`: Unpacks and appends each element (makes `[1, 2, 3, 4]`).
  - `sort()`: In-place sort, returns `None`.
  - `sorted()`: Returns a brand new sorted list.
- **Dictionary Lookups**:
  - `d['key']`: Raises `KeyError` if key is missing.
  - `d.get('key', default_value)`: Safe lookup without crashing.

---

## 2. Pandas Core Interview Commandments
- **`loc` vs `iloc`**:
  - `df.loc[row_label, col_label]`: Label-based. Stop index is **INCLUSIVE**!
  - `df.iloc[row_idx, col_idx]`: Integer position-based (0 to N-1). Stop index is **EXCLUSIVE**!
- **Boolean Masking Syntax**:
  - Always use `&` (AND), `|` (OR), `~` (NOT) with explicit parentheses:
    `df[(df['age'] > 30) & (df['salary'] > 50000)]`
- **`apply()` vs `transform()`**:
  - `df.groupby('dept')['salary'].apply(lambda x: x - x.mean())`: Can return aggregated or transformed structures.
  - `df.groupby('dept')['salary'].transform('mean')`: Returns a Series aligned with original DataFrame rows (perfect for adding a department average column without a merge!).
- **Handling Missing Values**:
  - Check nulls: `df.isnull().sum() / len(df) * 100` (Percentage of missingness).
  - Imputation: Mean for normal distributions, Median for skewed distributions with outliers.

---

## 3. NumPy & Statistical Essentials
- **SQL `CASE WHEN` Equivalent in Python**:
  - Single condition: `np.where(condition, value_if_true, value_if_false)`
  - Multiple conditions: `np.select(conditions_list, choices_list, default=default_val)`
- **Outlier Detection (IQR Method)**:
  - $IQR = Q3 - Q1$
  - Lower Bound = $Q1 - 1.5 \times IQR$
  - Upper Bound = $Q3 + 1.5 \times IQR$
- **Correlation**:
  - Pearson correlation measures linear relationships (-1 to +1).
  - `df.corr(numeric_only=True)`: Generates correlation matrix for heatmaps.

---

## 4. Key Performance Indicators (KPIs) Quick Formulas
- **Average Order Value (AOV)**: $\text{Total Revenue} / \text{Total Orders}$
- **Gross Profit Margin %**: $((\text{Revenue} - \text{COGS}) / \text{Revenue}) \times 100$
- **Churn Rate %**: $(\text{Lost Customers in Period} / \text{Total Active Customers at Start}) \times 100$
- **MoM Growth %**: $((\text{Current Month} - \text{Previous Month}) / \text{Previous Month}) \times 100$
