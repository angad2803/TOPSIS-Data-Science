"""
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
Multi-criteria decision-making implementation using NumPy and Pandas.
Author: SURYA KANT TIWARI (102303737)
"""

import sys
import pandas as pd
import numpy as np


def error_and_exit(message: str) -> None:
    """Print error message and exit."""
    print(f"Error: {message}")
    sys.exit(1)


def parse_and_validate(weights_arg: str, impacts_arg: str, ncols: int):
    """Parse weights/impacts and validate against criteria count."""
    try:
        weights = np.array(
            [float(w.strip()) for w in weights_arg.split(",") if w.strip()]
        )
    except ValueError:
        error_and_exit("Weights must be numeric and separated by commas")

    impacts = [imp.strip() for imp in impacts_arg.split(",") if imp.strip()]
    if not all(imp in ("+", "-") for imp in impacts):
        error_and_exit("Impacts must be '+' or '-' and separated by commas")

    if len(weights) != ncols or len(impacts) != ncols:
        error_and_exit(f"Weights and impacts count must equal criteria count ({ncols})")

    return weights, np.array(impacts)


def read_and_validate_csv(path: str):
    """Read CSV and validate structure using pandas."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        error_and_exit("File not found")
    except Exception as e:
        error_and_exit(f"Unable to read file: {e}")

    if df.shape[1] < 3:
        error_and_exit("Input file must have at least 3 columns")

    # Validate numeric columns (skip first identifier column)
    if not df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce").notna().all().all():
        error_and_exit("Columns 2 onwards must contain only numeric values")

    return df


def topsis_calculation(data: np.ndarray, weights: np.ndarray, impacts: np.ndarray):
    """
    Complete TOPSIS algorithm:
    1. Normalize (vector normalization)
    2. Apply weights
    3. Find ideal best/worst
    4. Calculate separation measures
    5. Compute scores and ranks
    """
    # Step 1-2: Normalize and weight
    norms = np.linalg.norm(data, axis=0)
    if np.any(norms == 0):
        error_and_exit("Column with all zeros detected")

    weighted = (data / norms) * weights

    # Step 3: Ideal solutions
    ideal_best = np.where(impacts == "+", weighted.max(axis=0), weighted.min(axis=0))
    ideal_worst = np.where(impacts == "+", weighted.min(axis=0), weighted.max(axis=0))

    # Step 4: Separation measures (Euclidean distance)
    s_best = np.linalg.norm(weighted - ideal_best, axis=1)
    s_worst = np.linalg.norm(weighted - ideal_worst, axis=1)

    # Step 5: TOPSIS scores and ranks
    scores = np.divide(
        s_worst,
        s_best + s_worst,
        out=np.zeros_like(s_worst),
        where=(s_best + s_worst) != 0,
    )
    ranks = np.argsort(-scores).argsort() + 1  # Double argsort trick for ranking

    return scores, ranks


def run_topsis(
    input_path: str, weights_arg: str, impacts_arg: str, output_path: str
) -> None:
    """Main TOPSIS execution pipeline."""
    df = read_and_validate_csv(input_path)
    ncols = df.shape[1] - 1

    weights, impacts = parse_and_validate(weights_arg, impacts_arg, ncols)
    data = df.iloc[:, 1:].to_numpy(dtype=float)
    scores, ranks = topsis_calculation(data, weights, impacts)

    df["Topsis Score"] = scores
    df["Rank"] = ranks
    df.to_csv(output_path, index=False)


def main(argv=None) -> None:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 4:
        error_and_exit("Usage: <InputDataFile> <Weights> <Impacts> <OutputResultFile>")
    run_topsis(*args)
    print(f"Result written to {args[3]}")


def cli() -> None:
    main()
