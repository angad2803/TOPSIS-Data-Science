# TOPSIS Concept & Implementation Guide

## For Viva, Paper & Interview Preparation

---

## 1. TOPSIS Method Overview

**TOPSIS** = Technique for Order Preference by Similarity to Ideal Solution

### Core Concept:

- Multi-criteria decision-making (MCDM) method
- Ranks alternatives based on their distance from ideal solutions
- **Best alternative**: Closest to ideal best solution AND farthest from ideal worst solution

### Key Steps:

1. **Normalize** decision matrix (vector normalization)
2. **Weight** normalized matrix by criteria importance
3. Identify **ideal best** and **ideal worst** solutions
4. Calculate **separation measures** (Euclidean distance)
5. Compute **relative closeness** (TOPSIS score)
6. **Rank** alternatives

---

## 2. Python Libraries Used & Internal Concepts

### **NumPy** (`import numpy as np`)

#### What it does:

- Fast numerical computations using C-optimized arrays
- Vectorized operations (no explicit Python loops)
- Broadcasting: automatic expansion of arrays for element-wise operations

#### Functions used:

**`np.array(list)`**

- Converts Python list to NumPy ndarray
- **Internal**: Allocates contiguous memory block, faster access than Python lists
- **Why**: Enables vectorized math operations

**`np.asarray(data, dtype=float)`**

- Converts data to NumPy array without copying if already an array
- **dtype=float**: Ensures all elements are floating-point numbers
- **Why**: Memory efficient, type consistency

**`np.linalg.norm(data, axis=0)`**

- Computes Euclidean norm (vector magnitude): √(x₁² + x₂² + ... + xₙ²)
- **axis=0**: Column-wise norm (for each criterion)
- **axis=1**: Row-wise norm (for each alternative)
- **Internal**: Optimized BLAS/LAPACK routines (C/Fortran)
- **Why**: Faster than manual sqrt(sum(squares))

**`np.where(condition, x, y)`**

- Vectorized if-else: returns x where condition is True, else y
- **Internal**: Single pass through array, no Python loops
- **Example**: `np.where(impacts == "+", max_vals, min_vals)`
  - If criterion is beneficial (+), pick maximum
  - If criterion is cost (-), pick minimum

**`np.divide(a, b, out=, where=)`**

- Element-wise division with control over edge cases
- **out**: Pre-allocated output array (memory efficient)
- **where**: Perform division only where condition is True
- **Why**: Prevents division by zero errors gracefully

**`np.argsort(array)`**

- Returns indices that would sort the array
- **`-scores`**: Negative for descending order
- **`.argsort()`**: Double argsort gives ranks directly
- **Internal**: Efficient sorting algorithm (Timsort/Quicksort)
- **Example**:
  ```python
  scores = [0.8, 0.6, 0.9]
  np.argsort(-scores) = [2, 0, 1]  # indices of sorted values
  .argsort() again = [1, 2, 0]     # ranks: 2nd, 3rd, 1st
  ```

**`np.zeros_like(array)`**

- Creates array of zeros with same shape and type
- **Internal**: Single malloc call, initialized to zero
- **Why**: Fast default value initialization

**`np.any(array)`**

- Returns True if ANY element is True
- **Short-circuits**: Stops at first True (efficient)

---

### **Pandas** (`import pandas as pd`)

#### What it does:

- High-level data structures (DataFrame, Series)
- Built on NumPy for performance
- Easy CSV I/O and data validation

#### Functions used:

**`pd.read_csv(path)`**

- Reads CSV file into DataFrame
- **Internal**:
  - Uses fast C parser engine
  - Automatically infers data types
  - Handles encoding, delimiters, quotes
- **Why**: More robust than Python's csv module

**`df.shape`**

- Returns tuple `(rows, columns)`
- **Property access**: O(1) operation (stored in metadata)

**`df.iloc[:, 1:]`**

- Integer-location based indexing
- **[:, 1:]**: All rows, columns from index 1 onward
- **Why**: Skip first column (identifiers), get numeric data

**`df.to_numpy(dtype=float)`**

- Converts DataFrame to NumPy array
- **dtype=float**: Force conversion to floating-point
- **Internal**: Zero-copy when possible (shares memory)
- **Why**: Bridge to NumPy for mathematical operations

**`df.apply(func, axis=0)`**

- Apply function along axis
- **axis=0**: Column-wise operation
- **Why**: Vectorized validation across columns

**`pd.to_numeric(series, errors='coerce')`**

- Converts to numeric type
- **errors='coerce'**: Invalid values → NaN (Not a Number)
- **Why**: Detect non-numeric data for validation

**`.notna()`**

- Boolean array: True for non-NaN values
- **Opposite of**: `.isna()` or `.isnull()`

**`.all()`**

- Returns True if ALL elements are True
- **Chained `.all().all()`**: First checks each column, then checks all columns

**`df.to_csv(path, index=False)`**

- Writes DataFrame to CSV file
- **index=False**: Don't write row numbers
- **Internal**: Buffered writing for performance

---

## 3. TOPSIS Mathematical Formulas (Interview Questions)

### Step 1: Normalization

```
rᵢⱼ = xᵢⱼ / √(Σ xᵢⱼ²)
```

- Makes all criteria dimensionless and comparable
- **Vector normalization**: Each element divided by column's Euclidean norm

### Step 2: Weighted Normalized Matrix

```
vᵢⱼ = wⱼ × rᵢⱼ
```

- Apply importance weights to each criterion

### Step 3: Ideal Solutions

```
V⁺ = {v₁⁺, v₂⁺, ..., vₙ⁺}  (ideal best)
V⁻ = {v₁⁻, v₂⁻, ..., vₙ⁻}  (ideal worst)

For beneficial criterion (+): v⁺ = max, v⁻ = min
For cost criterion (-):       v⁺ = min, v⁻ = max
```

### Step 4: Separation Measures (Euclidean Distance)

```
S⁺ᵢ = √(Σ(vᵢⱼ - vⱼ⁺)²)  (distance from ideal best)
S⁻ᵢ = √(Σ(vᵢⱼ - vⱼ⁻)²)  (distance from ideal worst)
```

### Step 5: Relative Closeness (TOPSIS Score)

```
Cᵢ = S⁻ᵢ / (S⁺ᵢ + S⁻ᵢ)
```

- Range: [0, 1]
- Higher score = better alternative

### Step 6: Ranking

- Sort alternatives by Cᵢ in descending order
- Rank 1 = highest score (best alternative)

---

## 4. Code Optimization Techniques Used

### Vectorization

**Instead of**:

```python
for i in range(n):
    for j in range(m):
        result[i][j] = data[i][j] / norm[j]
```

**We use**:

```python
result = data / norms  # Broadcasting: NumPy handles loops in C
```

- **Speed**: 10-100x faster
- **Why**: Eliminates Python interpreter overhead

### Broadcasting

- NumPy automatically expands arrays to compatible shapes
- Example: `(8, 5) / (5,)` → broadcasts to `(8, 5) / (8, 5)`

### In-place Operations

- `out=` parameter reuses memory
- Prevents creating temporary arrays

### Single-pass Algorithms

- Compute what you need once, store it
- Example: Calculate norms once, use multiple times

---

## 5. Common Interview Questions & Answers

**Q: Why TOPSIS over other MCDM methods?**

- **A**: Simple, intuitive (geometric distance concept), handles multiple criteria with different units, computationally efficient

**Q: What if all values in a column are zero?**

- **A**: Normalization fails (division by zero). Our code detects this with `np.any(norms == 0)` and exits with error

**Q: Why use NumPy instead of pure Python?**

- **A**:
  - NumPy arrays are stored in contiguous memory (cache-friendly)
  - Operations compiled to C (no Python overhead)
  - BLAS/LAPACK libraries (decades of optimization)
  - Vectorization eliminates explicit loops

**Q: What's the time complexity?**

- **A**: O(n × m) where n = alternatives, m = criteria
  - Normalization: O(n × m)
  - Distance calculation: O(n × m)
  - Sorting for ranks: O(n log n)
  - Overall: O(n × m + n log n)

**Q: How does pandas improve code?**

- **A**:
  - Automatic type detection and validation
  - Fast CSV parsing (C engine)
  - Clean syntax for column operations
  - Built-in data validation (missing values, types)

**Q: Explain `ranks = np.argsort(-scores).argsort() + 1`**

- **A**:
  1. `np.argsort(-scores)`: Get indices for descending sort
  2. `.argsort()` again: Inverse permutation = ranks (0-indexed)
  3. `+ 1`: Convert to 1-indexed ranks
  - This is faster than sorting and manual rank assignment

**Q: What validations does your code perform?**

- **A**:
  1. Argument count (must be 4)
  2. File exists
  3. Minimum 3 columns
  4. Columns 2+ are numeric
  5. Weights are numeric
  6. Impacts are + or -
  7. Count match: weights = impacts = criteria columns
  8. No zero-norm columns

---

## 6. Key Takeaways

1. **TOPSIS**: Distance-based MCDM, finds best compromise solution
2. **NumPy**: Vectorized numerical computing, C-speed in Python
3. **Pandas**: High-level data manipulation, robust I/O
4. **Optimization**: Avoid loops, use broadcasting, minimize memory allocations
5. **Validation**: Fail fast with clear error messages
6. **Clean Code**: One function = one responsibility, descriptive names

---

## 7. Quick Revision Points

- **Vector normalization** makes criteria comparable
- **Weights** reflect relative importance
- **Ideal best** = best possible on each criterion
- **Euclidean distance** measures similarity
- **TOPSIS score** = closeness to ideal
- **np.linalg.norm** = efficient √(Σx²)
- **np.where** = vectorized conditional
- **Broadcasting** = automatic array expansion
- **Pandas** = structured data + fast I/O
- **Complexity** = O(n × m)

---

**Tip for Viva**: Always explain WHY you chose an approach, not just WHAT it does. Mention performance and edge case handling.
