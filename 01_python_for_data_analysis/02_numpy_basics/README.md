# Chapter 2: NumPy Basics

This chapter introduces vectorized numerical computing, transforming you from writing slow Python loops to leveraging NumPy's blazing-fast array operations. NumPy is the foundation for all scientific Python (Pandas, Scikit-learn, TensorFlow).

**By chapter end:** Process 10M+ records in seconds, compute statistics on multidimensional crime data, and build memory-efficient analytics pipelines.

---

## 📚 Curriculum & Learning Sequence

| Module | File | Core Analytics Focus | Prerequisites |
| :--- | :--- | :--- | :--- |
| **01** | [`01_array_creation_and_dtypes.py`](01_array_creation_and_dtypes.py) | NumPy arrays vs Python lists, creation methods (`arange`, `linspace`, `zeros`, `ones`, `random`), data types (`int32`, `float64`, `bool`), type casting | Ch. 1: Functions & Type Hints |
| **02** | [`02_array_indexing_and_slicing.py`](02_array_indexing_and_slicing.py) | 1D/2D/3D indexing, fancy indexing (integer arrays), boolean masking (filtering rows), conditional selection, slicing edge cases | Ch. 1: Comprehensions, Lambda Functions |
| **03** | [`03_vectorized_operations.py`](03_vectorized_operations.py) | Element-wise arithmetic, universal functions (`sqrt`, `exp`, `log`), broadcasting rules (core NumPy magic), comparison operations, performance vs loops | Ch. 1: Functional Programming (map/filter) |
| **04** | [`04_reshaping_and_axis_operations.py`](04_reshaping_and_axis_operations.py) | `reshape()`, `flatten()`, `transpose()`, axis-based aggregations (`sum`, `mean`, `std`), `np.concatenate()`, `np.stack()` | Lessons 01–03 |
| **05** | [`05_file_io_and_data_loading.py`](05_file_io_and_data_loading.py) | Loading arrays: `np.loadtxt()`, `np.genfromtxt()`, `np.save()/load()`, handling missing data, delimiters, headers | Ch. 1: Lesson 5 (File I/O), Error Handling |
| **06** | [`06_linear_algebra_basics.py`](06_linear_algebra_basics.py) | Dot product, matrix multiplication (`@` operator), matrix inverse, determinants, eigenvalues (PCA foundation), solving linear systems | Lessons 01–04 |
| **07** | [`07_random_and_statistics.py`](07_random_and_statistics.py) | Random sampling (`np.random.choice()`, distributions), descriptive statistics (`mean`, `median`, `std`, `percentile`), histogram computation | Ch. 1: Lesson 7 (Collections), Lessons 01–04 |
| **08** | [`08_capstone_data_pipeline_with_numpy.py`](08_capstone_data_pipeline_with_numpy.py) | **Capstone Mini-Project**: End-to-end crime analytics pipeline: load CSV → clean → transform → aggregate → analyze → export | All prior lessons + Ch. 1: Lesson 8 (Capstone) |

---

## 🎯 Detailed Lesson Objectives

### **Lesson 01: Array Creation & Data Types** ⭐ FOUNDATION
**Goal:** Understand NumPy's core data structure and memory model.

**Key Topics:**
- NumPy arrays vs Python lists (performance differences, memory layout)
- Array attributes: `.shape`, `.ndim`, `.dtype`, `.size`, `.itemsize`
- Array creation methods:
  - `np.array()` — from existing lists
  - `np.arange()` — numeric sequences with step
  - `np.linspace()` — evenly spaced values (N points)
  - `np.zeros()`, `np.ones()` — initialized arrays
  - `np.full()` — arrays filled with a value
  - `np.random.rand()`, `np.random.randn()` — random uniform and normal
- Data types: `int32`, `int64`, `float32`, `float64`, `bool`, `complex128`
- Type casting with `.astype()`, `dtype` parameter
- Structured arrays (intro)

**Practical Example:**
```python
# Represent crime incident timestamps and severity scores
timestamps = np.arange('2026-01-01', '2026-12-31', dtype='datetime64[D]')
severity_scores = np.linspace(1.0, 10.0, 365)  # 365 incidents
```

**Why for Crime Psychology:** Different data types optimize memory (dates use less space than floats). Large datasets demand efficiency.

---

### **Lesson 02: Indexing & Slicing** ⭐ CRITICAL
**Goal:** Master efficient data subsetting (powerful extension of Python list slicing).

**Key Topics:**
- 1D indexing: negative indices, `arr[::2]` (step slicing)
- 2D/3D indexing: `arr[row, col]`, `arr[0:5, 2:7]`
- Fancy indexing: `arr[[0, 2, 4]]` (integer array indexing)
- Boolean masking: `arr[arr > 5]`, `arr[(arr > 5) & (arr < 10)]`
- Conditional selection and assignment
- Common indexing patterns (first N, last N, every Kth)
- Index edge cases and gotchas

**Practical Example:**
```python
# Crime data: rows=incidents, cols=timestamp, location, severity, recidivism_flag
crimes = np.random.randn(100000, 5)

# Filter high-severity crimes in specific precincts
severe_crimes = crimes[crimes[:, 2] > 7.5]  # Boolean masking
recent_severe = crimes[(crimes[:, 0] > '2026-09-01') & (crimes[:, 2] > 8.0)]
```

**Why for Crime Psychology:** Quickly extract crimes by location, date, severity, or demographic patterns without looping.

---

### **Lesson 03: Vectorized Operations** ⭐ PERFORMANCE GAME-CHANGER
**Goal:** Replace slow Python loops with fast vectorized NumPy operations (50–1000x speedup).

**Key Topics:**
- Element-wise arithmetic: `+`, `-`, `*`, `/`, `**`, `//`, `%`
- Universal functions (ufuncs): 
  - Math: `np.sqrt()`, `np.exp()`, `np.log()`, `np.sin()`, `np.cos()`
  - Rounding: `np.ceil()`, `np.floor()`, `np.round()`
  - Logic: `np.abs()`, `np.maximum()`, `np.minimum()`
- Comparison operations: `<`, `>`, `==`, `!=` returning boolean arrays
- Broadcasting rules (alignment of different shapes automatically)
- Performance benchmarking (loop vs vectorization)
- When NOT to vectorize

**Practical Example:**
```python
# Normalize crime severity scores to 0–1 range (z-score)
mean = crimes[:, 2].mean()
std = crimes[:, 2].std()
normalized = (crimes[:, 2] - mean) / std  # Vectorized (fast)
# vs. slow: [((c - mean) / std) for c in crimes[:, 2]]

# Broadcasting: element-wise multiply each row by a scaling vector
scaling_factors = np.array([1.0, 1.5, 2.0, 0.8, 1.2])
scaled_data = crimes * scaling_factors  # Automatic row-wise expansion
```

**Why for Crime Psychology:** Crime datasets have 1M+ records. Vectorization means seconds vs. hours.

---

### **Lesson 04: Reshaping & Axis Operations** ⭐ CORE ANALYTICS
**Goal:** Restructure data and aggregate along specific dimensions (time, location, crime type).

**Key Topics:**
- `reshape()` — change array dimensions (preserves data order)
- `flatten()` — convert to 1D (copy)
- `ravel()` — convert to 1D (view, faster)
- `transpose()` and `.T` — swap axes
- Axis parameter in aggregations:
  - `arr.sum(axis=0)` — sum along rows (column totals)
  - `arr.mean(axis=1)` — mean along columns (row averages)
  - `arr.std(axis=None)` — overall statistic
- Multi-axis operations: `arr.sum(axis=(0, 1))`
- `np.concatenate()`, `np.vstack()`, `np.hstack()` — joining arrays
- `np.stack()` — creating new dimensions

**Practical Example:**
```python
# Crime data: 365 days × 24 hours × 12 precincts (3D array)
crimes_3d = np.random.randint(0, 100, (365, 24, 12))

# Aggregate by precinct (sum across days and hours)
by_precinct = crimes_3d.sum(axis=(0, 1))  # Shape: (12,)

# Aggregate by hour of day (across all days and precincts)
by_hour = crimes_3d.sum(axis=(0, 2))  # Shape: (24,)

# Average crimes per day by precinct
by_precinct_daily = crimes_3d.mean(axis=1)  # Shape: (365, 12)
```

**Why for Crime Psychology:** Criminal behavior is naturally multidimensional (temporal patterns × location × offense type × demographics).

---

### **Lesson 05: File I/O & Data Loading** 📁 PRACTICAL
**Goal:** Load real crime data from external files efficiently.

**Key Topics:**
- `np.loadtxt()` — simple homogeneous CSV/text files
- `np.genfromtxt()` — handles missing values, mixed types, irregular data
- `np.savetxt()` — export arrays to text format
- `np.save()` / `np.load()` — binary `.npy` format (fast, preserves dtype)
- `np.savez()` / `np.load()` — save multiple arrays as `.npz` archive
- Handling headers, delimiters, skipping rows, dtype specification
- Common data loading patterns (police records, court data, demographics)
- Integration with error handling (corrupt rows)

**Practical Example:**
```python
# Load crime incident data (CSV: date, location, offense_code, recidivism)
crimes = np.genfromtxt(
    'crime_incidents.csv',
    delimiter=',',
    dtype={'names': ('date', 'location', 'offense', 'recidivism'),
            'formats': ('U10', 'i4', 'U20', 'f4')},
    skip_header=1  # Skip column names
)

# Save processed data for fast reloading
np.save('crimes_processed.npy', crimes)
loaded = np.load('crimes_processed.npy')
```

**Why for Crime Psychology:** Real crime data comes from police databases, court records, demographic files—all in CSV/text format.

---

### **Lesson 06: Linear Algebra Basics** 🧮 MODELING FOUNDATION
**Goal:** Master matrix operations (preparation for regression, classification, PCA).

**Key Topics:**
- Dot product: `np.dot(a, b)`, `a @ b` (modern syntax)
- Matrix multiplication: `A @ B` (2D)
- Matrix inverse: `np.linalg.inv(A)`
- Determinant: `np.linalg.det(A)`
- Trace: `np.trace(A)`
- Eigenvalues & eigenvectors: `np.linalg.eig(A)` (foundation for PCA)
- Solving linear systems: `np.linalg.solve(A, b)` (Ax = b)
- Rank, condition number (numerical stability)
- Norm computation: `np.linalg.norm()`

**Practical Example:**
```python
# Compute correlation matrix between psychological features
X = np.random.randn(1000, 5)  # 1000 individuals, 5 psych measures
correlation = (X.T @ X) / X.shape[0]  # Covariance matrix
print(correlation)  # Insight: which factors correlate?

# Solve linear regression: y = X @ beta
# If we have: y = X @ beta + noise
# Solve: beta = (X.T @ X)^(-1) @ X.T @ y
beta = np.linalg.solve(X.T @ X, X.T @ y)
```

**Why for Crime Psychology:** Predictive models (recidivism, risk assessment) use regression and PCA—both require linear algebra.

---

### **Lesson 07: Random & Statistics** 📊 ANALYSIS POWER
**Goal:** Generate random data, compute statistics, analyze distributions for modeling.

**Key Topics:**
- Random number generation:
  - `np.random.rand()` — uniform [0, 1)
  - `np.random.randn()` — standard normal (μ=0, σ=1)
  - `np.random.normal(loc, scale, size)` — normal distribution
  - `np.random.choice()` — sampling with/without replacement
  - `np.random.shuffle()` — in-place shuffling
  - `np.random.seed()` — reproducibility
- Descriptive statistics:
  - Central tendency: `mean()`, `median()` (outlier-robust)
  - Spread: `std()`, `var()`, `ptp()` (peak-to-peak)
  - Extremes: `min()`, `max()`, `argmin()`, `argmax()`
  - Quantiles: `percentile()`, `quantile()`
- Histogram: `np.histogram()` (binning and counting)
- Correlation & covariance: `np.corrcoef()`, `np.cov()`

**Practical Example:**
```python
# Simulate recidivism rates from psychological profiles
# Hypothesis: mean 35% recidivism, std 8%
np.random.seed(42)  # Reproducible
recidivism_rates = np.random.normal(loc=0.35, scale=0.08, size=10000)

# Compute confidence intervals
p5 = np.percentile(recidivism_rates, 5)
p95 = np.percentile(recidivism_rates, 95)
print(f"95% CI: [{p5:.3f}, {p95:.3f}]")

# Binning for visualization
counts, bins = np.histogram(recidivism_rates, bins=20)
```

**Why for Crime Psychology:** Building confidence intervals, simulating scenarios, testing assumptions all require statistics.

---

### **Lesson 08: Capstone — Data Pipeline with NumPy** 🎯 INTEGRATION
**Goal:** End-to-end analytics project synthesizing all NumPy concepts.

**Project Scenario:** *Crime Incident Analytics & Psychology Modeling Pipeline*

**Pipeline Stages:**
1. **Load** crime incident data from CSV
   - Incident date, location (precinct), offense type, severity score
   - Defendant demographics (age, prior offenses, psychological evaluation)
   - Recidivism outcome (1 = reoffended within 3 years, 0 = no reoffense)

2. **Clean** using boolean masking
   - Remove outliers (severity > 10 or < 0)
   - Filter incomplete records (missing psychological evaluations)
   - Handle missing values (fill with median or exclude)

3. **Transform** using vectorized operations
   - Normalize features (z-score all numerical columns)
   - Bin continuous variables (age into cohorts)
   - Compute derived features (time since last offense, offense frequency)

4. **Aggregate** using reshaping & axis operations
   - Crimes by precinct, month, offense category
   - Average severity by precinct
   - Recidivism rate by demographic group

5. **Analyze** using statistics & linear algebra
   - Compute correlation between offense history and recidivism
   - Generate confidence intervals for recidivism rates
   - Calculate principal components (PCA) for psychological profiles

6. **Report** summary statistics
   - Export aggregated tables (CSV)
   - Save processed arrays (`.npy`)
   - Generate summary: mean/median/std for all metrics

7. **Visualize** (preparation for next chapter)
   - Create arrays ready for Matplotlib (histograms, scatter plots)
   - Compute binned data for plotting

**Expected Deliverables:**
- Cleaned NumPy arrays saved as `.npy` files
- Summary statistics JSON/CSV (crimes per precinct, recidivism rates)
- Feature-engineered dataset ready for machine learning
- Performance metrics (processing time, memory usage)

---

## 🗂️ File Structure

```
02_numpy_basics/
├── README.md                                    (this file)
├── 01_array_creation_and_dtypes.py
├── 02_array_indexing_and_slicing.py
├── 03_vectorized_operations.py
├── 04_reshaping_and_axis_operations.py
├── 05_file_io_and_data_loading.py
├── 06_linear_algebra_basics.py
├── 07_random_and_statistics.py
└── 08_capstone_data_pipeline_with_numpy.py
```

---

## 🚀 How to Run the Lessons

Execute any lesson script directly:

```bash
python 01_array_creation_and_dtypes.py
python 02_array_indexing_and_slicing.py
python 03_vectorized_operations.py
python 04_reshaping_and_axis_operations.py
python 05_file_io_and_data_loading.py
python 06_linear_algebra_basics.py
python 07_random_and_statistics.py
python 08_capstone_data_pipeline_with_numpy.py
```

Each lesson includes:
- Inline documentation and examples
- Interactive demonstrations
- Practical crime psychology use cases
- Performance comparisons

---

## 📊 Progression Map

```
Lesson 01: Arrays (Data Structure)
    ↓ (enables)
Lesson 02: Indexing (Data Access) [from Ch. 1: comprehensions]
    ↓ (enables)
Lesson 03: Vectorization (Performance) [from Ch. 1: functional programming]
    ↓ (enables)
Lesson 04: Reshaping (Data Organization) [builds on 01–03]
    ↓ (enables)
Lesson 05: File I/O (Real Data) [from Ch. 1: Lesson 5 + prior lessons]
    ↓ (enables)
Lesson 06: Linear Algebra (Mathematical Foundations) [for analytics]
    ↓ (enables)
Lesson 07: Statistics (Analytics Ready) [from Ch. 1: Lesson 7 + prior lessons]
    ↓ (enables)
Lesson 08: Capstone (Integration) [synthesizes all concepts]
```

---

## 🎓 Competencies by Lesson

| Competency | Lesson(s) | Crime Analytics Application |
|:---|:---|:---|
| **Data Structure Mastery** | 01 | Load large crime datasets efficiently; understand memory constraints |
| **Efficient Subsetting** | 02 | Extract crimes by location, date, severity, demographics in milliseconds |
| **Performance Optimization** | 03 | Process 10M+ crime records in seconds instead of hours |
| **Multidimensional Analysis** | 04 | Analyze crime trends across time × location × offense type × demographics |
| **External Data Integration** | 05 | Ingest police records, court data, demographic files, historical trends |
| **Predictive Foundations** | 06 | Build recidivism prediction models; understand PCA for psychology factors |
| **Statistical Rigor** | 07 | Compute confidence intervals, assess distribution, validate hypotheses |
| **End-to-End Pipelines** | 08 | Complete crime psychology research workflows: ingest → clean → analyze → report |

---

## ✅ Connection to Chapter 1: Intermediate Python

Each NumPy lesson builds directly on pure Python foundations:

| Ch. 1 Lesson | NumPy Application | Reinforcement |
|:---|:---|:---|
| Lesson 1: Functions | NumPy APIs | Type hints (`dtype`, `axis` parameters) everywhere |
| Lesson 2: Lambda/Functional | Vectorization | `np.sqrt(arr)` = functional `map()` but **100x faster** |
| Lesson 3: Comprehensions | Indexing/Masking | Boolean masking `arr[arr > 5]` = comprehension-on-steroids |
| Lesson 4: Error Handling | Data Validation | Cleaning real crime data requires exception handling |
| Lesson 5: File I/O | `np.loadtxt()` | Building on pathlib, CSV/JSON foundations |
| Lesson 6: Generators | Memory Efficiency | NumPy arrays = memory-efficient like generators |
| Lesson 7: Collections | Aggregations | `Counter` becomes `np.unique(..., return_counts=True)` |
| Lesson 8: Capstone | NumPy Capstone | Same ETL thinking, now with vectorized NumPy |

---

## 🎯 Learning Outcomes

By chapter completion, you will:

✅ Create and manipulate arrays from scratch  
✅ Subset data efficiently using boolean masking (1000x faster than loops)  
✅ Perform vectorized computations on 10M+ records  
✅ Reshape and aggregate multidimensional crime data  
✅ Load and save real datasets from CSV, text, binary formats  
✅ Compute statistics, correlations, and confidence intervals  
✅ Perform matrix operations for predictive modeling  
✅ Build complete data pipelines without leaving NumPy  
✅ Understand broadcasting semantics and axis conventions  
✅ Prepare feature-engineered datasets for machine learning  

---

## 📚 Next Chapter

Once you master NumPy Basics, proceed to **Chapter 03: Pandas Core** for high-level tabular data manipulation (DataFrames, groupby, merging).

**Progression:** Raw Python → NumPy arrays → Pandas DataFrames → Scikit-learn ML

---

## 💡 Key Insights for Crime Psychology Analytics

- **NumPy enables scale**: From 1,000 incident analysis to 10M+ record processing
- **Vectorization is mandatory**: Loop-based approaches timeout on real datasets
- **Multidimensional thinking**: Crime data exists in multiple dimensions (time, location, offense, demographics)
- **Reproducibility**: `np.random.seed()` ensures results are repeatable for research
- **Statistics foundation**: Confidence intervals, distributions, and hypothesis testing require NumPy
- **Bridge to ML**: NumPy arrays are the native format for Scikit-learn, TensorFlow, PyTorch
