# TOPSIS: Condensed Concept & Implementation Guide

## 1. What is TOPSIS?

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) method. It ranks alternatives by how close they are to the ideal best and farthest from the ideal worst.

### Steps:

1. Normalize the decision matrix
2. Apply weights to criteria
3. Find ideal best/worst for each criterion
4. Calculate distances to ideal best/worst
5. Compute TOPSIS score (relative closeness)
6. Rank alternatives

## 2. Key Python Tools

**NumPy**: Fast, vectorized math (e.g., `np.linalg.norm`, `np.where`, `np.argsort`)

**Pandas**: DataFrame for CSV I/O, validation, and conversion to NumPy arrays

## 3. Main Formulas

- Normalization: $r_{ij} = x_{ij} / \sqrt{\sum x_{ij}^2}$
- Weighted: $v_{ij} = w_j \times r_{ij}$
- Ideal best/worst: max/min for beneficial/cost criteria
- Distance: $S_i^+ = \sqrt{\sum (v_{ij} - v_j^+)^2}$, $S_i^- = \sqrt{\sum (v_{ij} - v_j^-)^2}$
- Score: $C_i = S_i^- / (S_i^+ + S_i^-)$

## 4. Optimization & Validation

- Use vectorization and broadcasting (NumPy) for speed
- Validate: numeric data, correct argument count, weights/impacts match criteria, no zero-norm columns

## 5. Interview/Exam Quick Q&A

- **Why TOPSIS?** Simple, intuitive, handles multiple units, fast
- **Why NumPy?** C-speed, vectorized, memory efficient
- **Why Pandas?** Fast CSV, easy validation
- **Time complexity:** $O(n \times m)$
- **Key code:** `ranks = np.argsort(-scores).argsort() + 1` (fast ranking)

## 6. Takeaways

- TOPSIS: Distance-based, finds best compromise
- NumPy: Vectorized, fast math
- Pandas: Robust data handling
- Optimize: Avoid loops, use broadcasting
- Validate: Fail fast, clear errors

**Tip:** Always explain WHY, not just WHAT, in interviews.
